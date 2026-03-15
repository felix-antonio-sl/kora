import os
from pathlib import Path

from .artifacts import load_yaml_safe
from .catalog import load_catalog
from .config import KORA_ROOT, physical_to_logical_repo_path, resolve_logical_repo_path, resolve_operational_dir


def provenance_source_from_artifact(artifact):
    provenance = artifact.get("_manifest", {}).get("provenance", {})
    if isinstance(provenance, dict):
        return provenance.get("source", "")
    if isinstance(provenance, str):
        return provenance
    return ""


def cmd_intake():
    source_dir = resolve_operational_dir("source")
    drafts_dir = resolve_operational_dir("drafts")

    if not source_dir.exists():
        print("No source/ directory found.")
        return

    source_files = []
    for root, _dirs, files in os.walk(source_dir):
        for file_name in files:
            if file_name.startswith("."):
                continue
            source_files.append(Path(root) / file_name)

    if not source_files:
        print("No source files found.")
        return

    doc = load_catalog()
    catalog_sources = {}
    if doc and "Catalog" in doc:
        for category, items in doc["Catalog"].items():
            for item in items:
                urn = item.get("urn", "")
                file_path = KORA_ROOT / item.get("file", "")
                artifact, _ = load_yaml_safe(file_path)
                if artifact and isinstance(artifact, dict) and "_manifest" in artifact:
                    prov_source = provenance_source_from_artifact(artifact)
                    if prov_source:
                        catalog_sources[prov_source] = {
                            "urn": urn,
                            "status": item.get("status", "unknown"),
                            "file": item.get("file", ""),
                        }

    draft_sources = {}
    if drafts_dir.exists():
        for root, _dirs, files in os.walk(drafts_dir):
            for file_name in files:
                if not file_name.endswith(".md") or file_name.startswith("."):
                    continue
                draft_path = Path(root) / file_name
                artifact, _ = load_yaml_safe(draft_path)
                if artifact and isinstance(artifact, dict) and "_manifest" in artifact:
                    prov_source = provenance_source_from_artifact(artifact)
                    if prov_source:
                        draft_sources[prov_source] = str(draft_path.relative_to(KORA_ROOT))

    print("=== KORA Intake Status ===\n")
    counts = {"PENDING": 0, "PROCESSING": 0, "PUBLISHED": 0}

    for source_file in sorted(source_files):
        rel = str(physical_to_logical_repo_path(source_file))
        if rel in catalog_sources:
            status = "PUBLISHED"
            info = catalog_sources[rel]
            print(f"  [{status}] {rel} → {info['file']} ({info['urn']})")
        elif rel in draft_sources:
            status = "PROCESSING"
            print(f"  [{status}] {rel} → {draft_sources[rel]}")
        else:
            status = "PENDING"
            print(f"  [{status}] {rel}")
        counts[status] += 1

    orphan_count = 0
    for source_path, info in catalog_sources.items():
        if source_path.startswith("source/") and not resolve_logical_repo_path(source_path).exists():
            print(f"  [ORPHAN] {info['file']} → {source_path} (source missing)")
            orphan_count += 1

    print(
        f"\nSummary: {counts['PUBLISHED']} published, {counts['PROCESSING']} processing, {counts['PENDING']} pending, {orphan_count} orphan(s)"
    )
