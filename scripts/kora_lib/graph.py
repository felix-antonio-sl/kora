from dataclasses import dataclass
from functools import lru_cache
import json
import os
import re

from .catalog import load_catalog
from .config import AGENT_ROUTE_PATTERN, IGNORED_DIRS, IGNORED_FILES, KORA_ROOT, URN_REF_PATTERN
from .artifacts import load_yaml_safe
from .workspaces import extract_cm_refs, extract_declared_tool_headings, iter_agent_workspaces

FORMAL_TRACE_PATTERN = re.compile(r"formal/([0-9]{2})")


@dataclass(frozen=True)
class GraphEdge:
    kind: str
    source: object
    target: str
    fragment: str = ""


def iter_repository_files():
    for root, dirs, files in os.walk(KORA_ROOT):
        dirs[:] = [directory for directory in dirs if directory not in IGNORED_DIRS]
        for file_name in files:
            file_path = os.path.join(root, file_name)
            path = KORA_ROOT / os.path.relpath(file_path, KORA_ROOT)
            if file_name in IGNORED_FILES and path.parent == KORA_ROOT:
                continue
            yield path


@lru_cache(maxsize=1)
def build_formal_trace_lookup():
    lookup = {}
    formal_root = KORA_ROOT / "knowledge" / "kora" / "categorical-foundations"
    if not formal_root.exists():
        return lookup

    for file_path in sorted(formal_root.glob("*.md")):
        doc, _err = load_yaml_safe(file_path)
        urn = doc.get("_manifest", {}).get("urn") if isinstance(doc, dict) else None
        prefix = file_path.name.split("-", 1)[0]
        if urn and re.fullmatch(r"[0-9]{2}", prefix):
            lookup[prefix] = urn
    return lookup


def collect_urn_edges(file_path, content):
    edges = []
    in_code_block = False
    formal_lookup = build_formal_trace_lookup()
    for line in content.split("\n"):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        if stripped.lower().startswith("**incorrecto"):
            continue
        if "Traces to:" in line:
            for doc_id in FORMAL_TRACE_PATTERN.findall(line):
                if doc_id in formal_lookup:
                    edges.append(GraphEdge("TracesTo", file_path, formal_lookup[doc_id]))
        for found in URN_REF_PATTERN.findall(line):
            base_urn, _, fragment = found.partition("#")
            edges.append(GraphEdge("XRef", file_path, base_urn, fragment))
    return edges


def collect_workspace_edges(file_path):
    edges = []
    if file_path.name == "AGENTS.md":
        for cm_ref in sorted(extract_cm_refs(file_path)):
            edges.append(GraphEdge("InvokesSkill", file_path, cm_ref))
        content = file_path.read_text(encoding="utf-8")
        for namespace, name in sorted(set(AGENT_ROUTE_PATTERN.findall(content))):
            edges.append(GraphEdge("RoutesToAgent", file_path, f"{namespace}/{name}"))
    elif file_path.name == "TOOLS.md":
        _, valid_tools, _ = extract_declared_tool_headings(file_path)
        for tool_name in sorted(valid_tools):
            edges.append(GraphEdge("DeclaresTool", file_path, tool_name))
    elif file_path.name == "config.json":
        config_data = json.loads(file_path.read_text(encoding="utf-8"))
        for kb_urn in config_data.get("allowed_kb", []):
            edges.append(GraphEdge("AllowsKB", file_path, kb_urn))
        for tool_name in config_data.get("tools", {}).get("allow", []):
            edges.append(GraphEdge("AllowsTool", file_path, tool_name))
    return edges


def build_reference_graph():
    edges = []
    scanned_files = 0
    for file_path in iter_repository_files():
        if file_path.suffix not in (".yml", ".yaml", ".md", ".json"):
            continue
        try:
            content = file_path.read_text(encoding="utf-8")
        except Exception:
            continue
        scanned_files += 1
        edges.extend(collect_urn_edges(file_path, content))
        try:
            edges.extend(collect_workspace_edges(file_path))
        except Exception as exc:
            rel_path = file_path.relative_to(KORA_ROOT)
            raise RuntimeError(f"Failed to collect workspace edges from {rel_path}: {exc}") from exc
    return scanned_files, edges


def workspace_node_id(namespace, name):
    return f"workspace:{namespace}/{name}"


def tool_node_id(tool_name):
    return f"tool:{tool_name}"


def classify_catalog_node_kind(entry):
    urn = entry.get("urn", "")
    file_path = entry.get("file", "")
    if ":skill:" in urn:
        return "skill"
    if file_path.startswith("specs/"):
        return "spec"
    if ":kb:" in urn:
        return "knowledge"
    return "artifact"


def build_graph_payload():
    catalog = load_catalog()
    if not catalog or "Catalog" not in catalog:
        print("Error: Catalog not found or invalid. Run 'kora index' first.")
        raise SystemExit(1)

    nodes = {}
    edges_payload = []
    path_to_urn = {}
    workspace_skill_urns = {}

    for category, items in catalog["Catalog"].items():
        for item in items:
            urn = item["urn"]
            rel_path = item["file"]
            abs_path = KORA_ROOT / rel_path
            node_kind = classify_catalog_node_kind(item)
            parts = urn.split(":")
            nodes[urn] = {
                "id": urn,
                "kind": node_kind,
                "category": category,
                "urn": urn,
                "title": item.get("title"),
                "path": rel_path,
                "namespace": parts[1] if len(parts) > 1 else None,
            }
            path_to_urn[str(abs_path)] = urn
            if node_kind == "skill":
                workspace_skill_urns[(str(abs_path.parent.parent), abs_path.stem)] = urn

    for workspace_dir in iter_agent_workspaces():
        namespace = workspace_dir.parent.name
        name = workspace_dir.name
        node_id = workspace_node_id(namespace, name)
        nodes[node_id] = {
            "id": node_id,
            "kind": "workspace",
            "workspace": f"{namespace}/{name}",
            "namespace": namespace,
            "path": str(workspace_dir.relative_to(KORA_ROOT)),
        }
        for artifact_path in sorted(workspace_dir.glob("*.md")):
            artifact_urn = path_to_urn.get(str(artifact_path))
            if artifact_urn:
                edges_payload.append(
                    {
                        "kind": "ContainsArtifact",
                        "source": node_id,
                        "target": artifact_urn,
                    }
                )
        config_urn = path_to_urn.get(str(workspace_dir / "config.json"))
        if config_urn:
            edges_payload.append(
                {
                    "kind": "ContainsArtifact",
                    "source": node_id,
                    "target": config_urn,
                }
            )
        for skill_path in sorted((workspace_dir / "skills").glob("*.md")) if (workspace_dir / "skills").exists() else []:
            skill_urn = path_to_urn.get(str(skill_path))
            if skill_urn:
                edges_payload.append(
                    {
                        "kind": "ContainsSkill",
                        "source": node_id,
                        "target": skill_urn,
                    }
                )

    scanned_files, raw_edges = build_reference_graph()
    for edge in raw_edges:
        source_path = edge.source
        source_urn = path_to_urn.get(str(source_path))
        source_workspace = workspace_node_id(source_path.parent.parent.name, source_path.parent.parent.name)
        if source_path.name == "config.json":
            source_workspace = workspace_node_id(source_path.parent.parent.name, source_path.parent.name)
        elif source_path.name in {"TOOLS.md", "AGENTS.md", "SOUL.md", "USER.md"}:
            source_workspace = workspace_node_id(source_path.parent.parent.name, source_path.parent.name)

        if edge.kind in {"XRef", "TracesTo"}:
            target_id = edge.target
            if edge.target.startswith("urn:") and edge.target not in nodes:
                nodes[target_id] = {
                    "id": target_id,
                    "kind": "artifact",
                    "urn": edge.target,
                }
            edges_payload.append(
                {
                    "kind": edge.kind,
                    "source": source_urn or f"file:{source_path.relative_to(KORA_ROOT)}",
                    "target": target_id,
                    "fragment": edge.fragment or None,
                    "source_path": str(source_path.relative_to(KORA_ROOT)),
                }
            )
        elif edge.kind == "InvokesSkill":
            target_id = workspace_skill_urns.get((str(source_path.parent), edge.target))
            if not target_id:
                skill_file = source_path.parent / "skills" / f"{edge.target}.md"
                target_id = path_to_urn.get(str(skill_file), f"missing-skill:{source_path.parent.name}/{edge.target}")
            edges_payload.append(
                {
                    "kind": edge.kind,
                    "source": source_urn or f"file:{source_path.relative_to(KORA_ROOT)}",
                    "target": target_id,
                    "source_path": str(source_path.relative_to(KORA_ROOT)),
                }
            )
        elif edge.kind == "RoutesToAgent":
            namespace, name = edge.target.split("/", 1)
            edges_payload.append(
                {
                    "kind": edge.kind,
                    "source": workspace_node_id(source_path.parent.parent.name, source_path.parent.name),
                    "target": workspace_node_id(namespace, name),
                    "source_path": str(source_path.relative_to(KORA_ROOT)),
                }
            )
        elif edge.kind in {"DeclaresTool", "AllowsTool"}:
            target_id = tool_node_id(edge.target)
            if target_id not in nodes:
                nodes[target_id] = {
                    "id": target_id,
                    "kind": "tool",
                    "name": edge.target,
                }
            edges_payload.append(
                {
                    "kind": edge.kind,
                    "source": source_workspace,
                    "target": target_id,
                    "source_path": str(source_path.relative_to(KORA_ROOT)),
                }
            )
        elif edge.kind == "AllowsKB":
            edges_payload.append(
                {
                    "kind": edge.kind,
                    "source": workspace_node_id(source_path.parent.parent.name, source_path.parent.name)
                    if source_path.name != "config.json"
                    else workspace_node_id(source_path.parent.parent.name, source_path.parent.name),
                    "target": edge.target,
                    "source_path": str(source_path.relative_to(KORA_ROOT)),
                }
            )

    edge_kind_counts = {}
    for item in edges_payload:
        edge_kind_counts[item["kind"]] = edge_kind_counts.get(item["kind"], 0) + 1

    node_kind_counts = {}
    for item in nodes.values():
        node_kind_counts[item["kind"]] = node_kind_counts.get(item["kind"], 0) + 1

    return {
        "meta": {
            "scanned_files": scanned_files,
            "node_count": len(nodes),
            "edge_count": len(edges_payload),
        },
        "node_kind_counts": dict(sorted(node_kind_counts.items())),
        "edge_kind_counts": dict(sorted(edge_kind_counts.items())),
        "nodes": sorted(nodes.values(), key=lambda item: (item["kind"], item["id"])),
        "edges": sorted(
            edges_payload,
            key=lambda item: (item["kind"], item["source"], item["target"]),
        ),
    }


def cmd_graph(json_output=False):
    payload = build_graph_payload()
    if json_output:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return

    print("=== KORA Graph ===")
    print(f"  Nodes: {payload['meta']['node_count']}")
    print(f"  Edges: {payload['meta']['edge_count']}")
    print(f"  Scanned files: {payload['meta']['scanned_files']}")
    print("Node kinds:")
    for kind, count in payload["node_kind_counts"].items():
        print(f"  {kind}: {count}")
    print("Edge kinds:")
    for kind, count in payload["edge_kind_counts"].items():
        print(f"  {kind}: {count}")
