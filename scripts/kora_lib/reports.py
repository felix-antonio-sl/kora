import json

from .agent_audit import write_agent_audit_docs
from .artifacts import load_yaml_safe
from .config import AGENT_REQUIRED_FILES, CATALOG_PATH, GENERATED_DOCS_DIR
from .contracts import build_operating_core_payload, render_operating_core_markdown
from .fxsl_cat import write_fxsl_cat_ledger_docs
from .graph import build_graph_payload
from .workspaces import get_workspace_missing_files, iter_agent_workspaces


def compute_stats_payload():
    doc, _ = load_yaml_safe(CATALOG_PATH)
    if not doc or "Catalog" not in doc:
        print("Error: Catalog not found. Run 'kora index' first.")
        raise SystemExit(1)

    workspaces = iter_agent_workspaces()
    complete_workspaces = [
        workspace
        for workspace in workspaces
        if not get_workspace_missing_files(workspace, AGENT_REQUIRED_FILES)
    ]

    bootstrap_count = len(doc["Catalog"].get("Agents", []))

    total = 0
    category_counts = {}
    for category, items in doc["Catalog"].items():
        count = len(items)
        category_counts[category] = count
        total += count

    ns_counts = {}
    for category, items in doc["Catalog"].items():
        for item in items:
            urn = item.get("urn", "")
            parts = urn.split(":")
            namespace = parts[1] if len(parts) >= 2 else "unknown"
            ns_counts[namespace] = ns_counts.get(namespace, 0) + 1

    return {
        "agent_workspaces": len(complete_workspaces),
        "incomplete_workspaces": len(workspaces) - len(complete_workspaces),
        "agent_bootstrap_artifacts": bootstrap_count,
        "catalog_counts": category_counts,
        "total_catalog_entries": total,
        "by_namespace": dict(sorted(ns_counts.items(), key=lambda item: -item[1])),
    }


def render_stats_markdown(payload):
    lines = [
        "# KORA Generated Stats",
        "",
        "Este documento es generado por `scripts/kora sync-docs`. No editar a mano.",
        "",
        "## Resumen",
        "",
        f"- Agent workspaces completos: {payload['agent_workspaces']}",
        f"- Workspaces incompletos: {payload['incomplete_workspaces']}",
        f"- Artefactos bootstrap de agente: {payload['agent_bootstrap_artifacts']}",
        f"- Entradas totales de catalogo: {payload['total_catalog_entries']}",
        "",
        "## Catalogo por categoria",
        "",
        "| Categoria | Conteo |",
        "|-----------|--------|",
    ]

    for category, count in payload["catalog_counts"].items():
        lines.append(f"| {category} | {count} |")

    lines.extend(
        [
            "",
            "## Catalogo por namespace",
            "",
            "| Namespace | Entradas |",
            "|-----------|----------|",
        ]
    )

    for namespace, count in payload["by_namespace"].items():
        lines.append(f"| {namespace} | {count} |")

    lines.append("")
    return "\n".join(lines)


def write_generated_stats_docs(payload):
    GENERATED_DOCS_DIR.mkdir(parents=True, exist_ok=True)
    json_path = GENERATED_DOCS_DIR / "repo-stats.json"
    md_path = GENERATED_DOCS_DIR / "repo-stats.md"
    json_path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    md_path.write_text(render_stats_markdown(payload), encoding="utf-8")
    return json_path, md_path


def write_generated_graph_docs():
    GENERATED_DOCS_DIR.mkdir(parents=True, exist_ok=True)
    payload = build_graph_payload()
    json_path = GENERATED_DOCS_DIR / "repo-graph.json"
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return payload, json_path


def write_generated_operating_core_docs():
    GENERATED_DOCS_DIR.mkdir(parents=True, exist_ok=True)
    payload = build_operating_core_payload()
    json_path = GENERATED_DOCS_DIR / "operating-core-contracts.json"
    md_path = GENERATED_DOCS_DIR / "operating-core-contracts.md"
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    md_path.write_text(render_operating_core_markdown(payload), encoding="utf-8")
    return payload, json_path, md_path


def sync_generated_docs():
    stats_payload = compute_stats_payload()
    stats_json_path, stats_md_path = write_generated_stats_docs(stats_payload)
    graph_payload, graph_json_path = write_generated_graph_docs()
    contracts_payload, contracts_json_path, contracts_md_path = write_generated_operating_core_docs()
    fxsl_payload, fxsl_json_path, fxsl_md_path = write_fxsl_cat_ledger_docs(GENERATED_DOCS_DIR)
    audit_payload, audit_json_path, audit_md_path = write_agent_audit_docs(GENERATED_DOCS_DIR)
    return {
        "stats": {
            "payload": stats_payload,
            "json_path": stats_json_path,
            "md_path": stats_md_path,
        },
        "graph": {
            "payload": graph_payload,
            "json_path": graph_json_path,
        },
        "operating_core": {
            "payload": contracts_payload,
            "json_path": contracts_json_path,
            "md_path": contracts_md_path,
        },
        "fxsl_cat": {
            "payload": fxsl_payload,
            "json_path": fxsl_json_path,
            "md_path": fxsl_md_path,
        },
        "agent_audit": {
            "payload": audit_payload,
            "json_path": audit_json_path,
            "md_path": audit_md_path,
        },
    }
