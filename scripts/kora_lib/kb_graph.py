"""Knowledge graph materialization for KORA.

Reads all artifacts in KNOWLEDGE/, extracts their URNs, relations, and metadata,
and produces a typed directed graph (nodes + edges) as JSON.
"""

import json
import os
from pathlib import Path

from .artifacts import load_yaml_safe
from .config import KNOWLEDGE_ROOT, KORA_ROOT, GENERATED_DOCS_DIR


def collect_knowledge_nodes():
    """Walk KNOWLEDGE/ and collect all artifacts with valid _manifest."""
    nodes = []
    # Scan KNOWLEDGE/ and specs/ for knowledge artifacts
    scan_roots = [KNOWLEDGE_ROOT]
    specs_dir = KORA_ROOT / "specs"
    if specs_dir.exists():
        scan_roots.append(specs_dir)

    for scan_root in scan_roots:
        for root, _dirs, files in os.walk(scan_root):
            for fname in sorted(files):
                if not fname.endswith(".md") or fname == "README.md":
                    continue
                path = Path(root) / fname
                frontmatter, err = load_yaml_safe(path)
                if err or not isinstance(frontmatter, dict):
                    continue
                manifest = frontmatter.get("_manifest", {})
                urn = manifest.get("urn", "")
                if not urn or ":kb:" not in urn:
                    continue

                rel_path = str(path.relative_to(KORA_ROOT))
                if scan_root == KNOWLEDGE_ROOT:
                    parts = path.relative_to(KNOWLEDGE_ROOT).parts
                    namespace = parts[0] if parts else "unknown"
                else:
                    namespace = "kora"

                nodes.append({
                    "urn": urn,
                    "namespace": namespace,
                    "status": frontmatter.get("status", "unknown"),
                    "version": frontmatter.get("version", ""),
                    "tags": frontmatter.get("tags", []),
                    "file": rel_path,
                    "relations": frontmatter.get("relations", {}),
                })
    return nodes


def build_graph(nodes):
    """Build edges from the relations declared in each node's frontmatter."""
    edges = []
    node_urns = {n["urn"] for n in nodes}

    for node in nodes:
        relations = node.get("relations", {})
        if not isinstance(relations, dict):
            continue
        for rel_type in ("cites", "depends", "supersedes", "refines"):
            targets = relations.get(rel_type, [])
            if isinstance(targets, str):
                targets = [targets]
            if not isinstance(targets, list):
                continue
            for target_urn in targets:
                edges.append({
                    "from": node["urn"],
                    "to": target_urn,
                    "type": rel_type,
                })

    # Stats
    by_namespace = {}
    for n in nodes:
        ns = n["namespace"]
        by_namespace[ns] = by_namespace.get(ns, 0) + 1

    by_relation_type = {}
    for e in edges:
        rt = e["type"]
        by_relation_type[rt] = by_relation_type.get(rt, 0) + 1

    connected_urns = {e["from"] for e in edges} | {e["to"] for e in edges}
    orphan_nodes = sum(1 for n in nodes if n["urn"] not in connected_urns)

    broken_edges = [e for e in edges if e["to"] not in node_urns]

    # Cycle detection in depends subgraph (DFS)
    depends_adj = {}
    for e in edges:
        if e["type"] == "depends":
            depends_adj.setdefault(e["from"], []).append(e["to"])

    cycles = 0
    visited = set()
    in_stack = set()

    def has_cycle(node):
        nonlocal cycles
        if node in in_stack:
            cycles += 1
            return
        if node in visited:
            return
        visited.add(node)
        in_stack.add(node)
        for neighbor in depends_adj.get(node, []):
            has_cycle(neighbor)
        in_stack.discard(node)

    for start in depends_adj:
        has_cycle(start)

    stats = {
        "total_nodes": len(nodes),
        "total_edges": len(edges),
        "by_namespace": dict(sorted(by_namespace.items(), key=lambda x: -x[1])),
        "by_relation_type": by_relation_type,
        "orphan_nodes": orphan_nodes,
        "broken_edges": len(broken_edges),
        "cycles_in_depends": cycles,
    }

    # Clean nodes for output (remove relations field)
    clean_nodes = []
    for n in nodes:
        clean_nodes.append({
            "urn": n["urn"],
            "namespace": n["namespace"],
            "status": n["status"],
            "version": n["version"],
            "tags": n["tags"],
        })

    return {
        "nodes": clean_nodes,
        "edges": edges,
        "broken_edges": broken_edges,
        "stats": stats,
    }


def render_kb_graph_markdown(graph):
    """Render a human-readable markdown summary of the knowledge graph."""
    stats = graph["stats"]
    lines = [
        "# KORA Knowledge Graph",
        "",
        f"Generated: {__import__('datetime').datetime.now().isoformat()}",
        "",
        "## Summary",
        "",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Nodes | {stats['total_nodes']} |",
        f"| Edges | {stats['total_edges']} |",
        f"| Orphan nodes | {stats['orphan_nodes']} |",
        f"| Broken edges | {stats['broken_edges']} |",
        f"| Cycles in depends | {stats['cycles_in_depends']} |",
        "",
    ]
    if stats["by_namespace"]:
        lines.append("## By Namespace")
        lines.append("")
        lines.append("| Namespace | Nodes |")
        lines.append("|-----------|-------|")
        for ns, count in stats["by_namespace"].items():
            lines.append(f"| {ns} | {count} |")
        lines.append("")

    if stats["by_relation_type"]:
        lines.append("## By Relation Type")
        lines.append("")
        lines.append("| Type | Count |")
        lines.append("|------|-------|")
        for rt, count in stats["by_relation_type"].items():
            lines.append(f"| {rt} | {count} |")
        lines.append("")

    if graph["broken_edges"]:
        lines.append("## Broken Edges")
        lines.append("")
        for e in graph["broken_edges"]:
            lines.append(f"- `{e['from']}` --{e['type']}--> `{e['to']}` (target not found)")
        lines.append("")

    # Top connected nodes
    edge_counts = {}
    for e in graph["edges"]:
        edge_counts[e["from"]] = edge_counts.get(e["from"], 0) + 1
        edge_counts[e["to"]] = edge_counts.get(e["to"], 0) + 1
    if edge_counts:
        top = sorted(edge_counts.items(), key=lambda x: -x[1])[:15]
        lines.append("## Most Connected Nodes")
        lines.append("")
        lines.append("| URN | Edges |")
        lines.append("|-----|-------|")
        for urn, count in top:
            lines.append(f"| `{urn}` | {count} |")
        lines.append("")

    return "\n".join(lines)


def cmd_kb_graph(json_output=False, check_cycles=False):
    nodes = collect_knowledge_nodes()
    graph = build_graph(nodes)

    if json_output:
        GENERATED_DOCS_DIR.mkdir(parents=True, exist_ok=True)
        out_path = GENERATED_DOCS_DIR / "kb-graph.json"
        with open(out_path, "w") as f:
            json.dump(graph, f, indent=2, ensure_ascii=False)
        md_path = GENERATED_DOCS_DIR / "kb-graph.md"
        md_path.write_text(render_kb_graph_markdown(graph), encoding="utf-8")
        print(f"Knowledge graph written to {out_path} and {md_path}")

    stats = graph["stats"]
    print(f"\n=== KORA Knowledge Graph ===")
    print(f"  Nodes: {stats['total_nodes']}")
    print(f"  Edges: {stats['total_edges']}")
    print(f"  Orphan nodes (no relations): {stats['orphan_nodes']}")
    print(f"  Broken edges: {stats['broken_edges']}")
    print(f"  Cycles in depends: {stats['cycles_in_depends']}")

    if stats["by_namespace"]:
        print(f"\n  By namespace:")
        for ns, count in stats["by_namespace"].items():
            print(f"    {ns}: {count}")

    if stats["by_relation_type"]:
        print(f"\n  By relation type:")
        for rt, count in stats["by_relation_type"].items():
            print(f"    {rt}: {count}")

    if graph["broken_edges"]:
        print(f"\n  Broken edges:")
        for e in graph["broken_edges"][:10]:
            print(f"    {e['from']} --{e['type']}--> {e['to']} (target not found)")

    if check_cycles and stats["cycles_in_depends"] > 0:
        print(f"\nERROR: {stats['cycles_in_depends']} cycle(s) detected in depends graph")
        raise SystemExit(1)
