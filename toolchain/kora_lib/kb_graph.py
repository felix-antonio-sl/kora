"""Knowledge graph materialization for KORA.

Reads all artifacts in artifacts/knowledge/, extracts their URNs, relations, and metadata,
and produces a typed directed graph (nodes + edges) as JSON.
"""

import json
import os
from pathlib import Path

from .artifacts import load_yaml_safe
from .catalog import canonicalize_urn_reference, is_historical_urn
from .config import KNOWLEDGE_ROOT, KORA_ROOT, GENERATED_DOCS_DIR


def collect_knowledge_nodes():
    """Walk artifacts/knowledge/ and collect all artifacts with valid _manifest.

    Excluye artifacts/knowledge/_SCRIPTORIUM/ (staging pre-categorial) — sus artefactos
    no forman parte del grafo de conocimiento publicado.
    """
    from .config import SPEC_ROOTS
    nodes = []
    scan_roots = [KNOWLEDGE_ROOT]
    for spec_root in SPEC_ROOTS:
        if spec_root.exists():
            scan_roots.append(spec_root)

    for scan_root in scan_roots:
        for root, dirs, files in os.walk(scan_root):
            # Poda: no descender en _SCRIPTORIUM/
            dirs[:] = [d for d in dirs if d != "_SCRIPTORIUM"]
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
                    # Specs — namespace derivado del URN, no del path
                    namespace = "kora"

                nodes.append({
                    "urn": urn,
                    "namespace": namespace,
                    "status": frontmatter.get("status", "unknown"),
                    "version": frontmatter.get("version", ""),
                    "tags": frontmatter.get("tags", []),
                    "file": rel_path,
                    "relations": frontmatter.get("relations", {}),
                    "orphan_intencional": (
                        (frontmatter.get("extensions") or {}).get("kora", {}).get("orphan_intencional") is True
                    ),
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
        for rel_type in ("cites", "depends", "supersedes", "refines", "traces_requirements"):
            targets = relations.get(rel_type, [])
            if isinstance(targets, str):
                targets = [targets]
            if not isinstance(targets, list):
                continue
            for target_urn in targets:
                canonical_target = canonicalize_urn_reference(target_urn)
                edges.append({
                    "from": node["urn"],
                    "to": canonical_target,
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

    # Clasificacion de huerfanos (sin cites/depends/supersedes/refines/traces_requirements
    # entrantes ni salientes) en tres clases functorialmente distintas:
    #   - root: spec constitucional (namespace kora + tag spec sin relations salientes
    #     hacia nodos no-constitucionales) — legitimos por ser el arranque del grafo.
    #   - intencional: el autor declaro orphan_intencional=true en extensions.kora.
    #   - real: huerfano que requiere curacion.
    CONSTITUTIONAL_URNS = {
        "urn:kora:kb:gobernanza",
        "urn:kora:kb:harness-spec",
        "urn:kora:kb:md-spec",
    }
    orphans_root = []
    orphans_intencional = []
    orphans_real = []
    for n in nodes:
        if n["urn"] in connected_urns:
            continue
        if n["urn"] in CONSTITUTIONAL_URNS:
            orphans_root.append(n["urn"])
        elif n.get("orphan_intencional"):
            orphans_intencional.append(n["urn"])
        else:
            orphans_real.append({"urn": n["urn"], "file": n.get("file", ""), "namespace": n["namespace"]})

    broken_edges = [e for e in edges if e["to"] not in node_urns and not is_historical_urn(e["to"])]

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
        "orphan_nodes": len(orphans_root) + len(orphans_intencional) + len(orphans_real),
        "orphans_root": len(orphans_root),
        "orphans_intencional": len(orphans_intencional),
        "orphans_real": len(orphans_real),
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
        "orphans_root": orphans_root,
        "orphans_intencional": orphans_intencional,
        "orphans_real": orphans_real,
        "stats": stats,
    }


def render_kb_graph_markdown(graph):
    """Render a human-readable markdown summary of the knowledge graph."""
    stats = graph["stats"]
    lines = [
        "# KORA Knowledge Graph",
        "",
        "## Summary",
        "",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Nodes | {stats['total_nodes']} |",
        f"| Edges | {stats['total_edges']} |",
        f"| Orphan nodes (total) | {stats['orphan_nodes']} |",
        f"| Orphans — root (constitutional) | {stats.get('orphans_root', 0)} |",
        f"| Orphans — intencional | {stats.get('orphans_intencional', 0)} |",
        f"| Orphans — real (require curation) | {stats.get('orphans_real', 0)} |",
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


def render_orphans_markdown(graph):
    """Render a markdown report of orphan classification."""
    stats = graph["stats"]
    lines = [
        "# KORA Knowledge Graph — Orphans Classification",
        "",
        "## Summary",
        "",
        f"| Class | Count | Meaning |",
        f"|-------|-------|---------|",
        f"| Root (constitutional) | {stats['orphans_root']} | Specs raíz del grafo (gobernanza, harness-spec, md-spec) |",
        f"| Intencional | {stats['orphans_intencional']} | Declarados con `extensions.kora.orphan_intencional: true` |",
        f"| Real | {stats['orphans_real']} | Requieren curacion (agregar `cites`/`depends` o marcar intencional) |",
        "",
    ]
    if graph.get("orphans_root"):
        lines += ["## Root (constitutional)", ""]
        for urn in graph["orphans_root"]:
            lines.append(f"- `{urn}`")
        lines.append("")
    if graph.get("orphans_intencional"):
        lines += ["## Intencional", ""]
        for urn in graph["orphans_intencional"]:
            lines.append(f"- `{urn}`")
        lines.append("")
    if graph.get("orphans_real"):
        lines += [
            "## Real — requieren curacion",
            "",
            "| URN | Namespace | File |",
            "|-----|-----------|------|",
        ]
        for n in sorted(graph["orphans_real"], key=lambda x: (x["namespace"], x["urn"])):
            lines.append(f"| `{n['urn']}` | {n['namespace']} | `{n['file']}` |")
        lines.append("")
    return "\n".join(lines)


def cmd_kb_graph(json_output=False, check_cycles=False, orphans=False):
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

    if orphans:
        GENERATED_DOCS_DIR.mkdir(parents=True, exist_ok=True)
        orphans_md = GENERATED_DOCS_DIR / "kb-orphans.md"
        orphans_md.write_text(render_orphans_markdown(graph), encoding="utf-8")
        print(f"Orphan classification written to {orphans_md}")

    stats = graph["stats"]
    print(f"\n=== KORA Knowledge Graph ===")
    print(f"  Nodes: {stats['total_nodes']}")
    print(f"  Edges: {stats['total_edges']}")
    print(f"  Orphans: {stats['orphan_nodes']} "
          f"(root={stats['orphans_root']}, intencional={stats['orphans_intencional']}, real={stats['orphans_real']})")
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
