from .migration import migrate_agents
from .reports import compute_stats_payload, sync_generated_docs
from .config import KORA_ROOT

import json


def cmd_stats():
    cmd_stats_json(False)


def cmd_stats_json(json_output=False):
    payload = compute_stats_payload()
    if json_output:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return

    print("=== KORA Monorepo Stats ===")
    print(f"  Agent Workspaces: {payload['agent_workspaces']}")
    if payload["incomplete_workspaces"]:
        print(f"  Incomplete Workspace Directories: {payload['incomplete_workspaces']}")
    print(f"  Agent Bootstrap Artifacts: {payload['agent_bootstrap_artifacts']}")
    for category, count in payload["catalog_counts"].items():
        if category == "Agents":
            continue
        if count > 0:
            print(f"  {category}: {count}")
    print(f"  TOTAL Catalog Entries: {payload['total_catalog_entries']}")

    print("\nBy namespace (catalog entries):")
    for namespace, count in payload["by_namespace"].items():
        print(f"  {namespace}: {count}")


def cmd_migrate(profile="transitional", dry_run=False, cohort=None):
    print(f"Running KORA migration codemods ({profile}, dry_run={dry_run})...")
    changed_paths = migrate_agents(profile=profile, dry_run=dry_run, cohort=cohort)
    unique_paths = sorted({str(path.relative_to(KORA_ROOT)) for path in changed_paths})
    print(f"Migration complete. Changed paths: {len(unique_paths)}")
    for rel in unique_paths[:40]:
        print(f"  {rel}")
    if len(unique_paths) > 40:
        print(f"  ... {len(unique_paths) - 40} more")


def cmd_sync_docs():
    outputs = sync_generated_docs()
    print("Generated public docs:")
    print(f"  {outputs['stats']['json_path'].relative_to(KORA_ROOT)}")
    print(f"  {outputs['stats']['md_path'].relative_to(KORA_ROOT)}")
    print(f"  {outputs['graph']['json_path'].relative_to(KORA_ROOT)}")
    print(f"  {outputs['fxsl_cat']['json_path'].relative_to(KORA_ROOT)}")
    print(f"  {outputs['fxsl_cat']['md_path'].relative_to(KORA_ROOT)}")
