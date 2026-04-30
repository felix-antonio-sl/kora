import os
from pathlib import Path

import yaml

from .artifacts import get_artifact_title, load_yaml_safe
from .config import (
    CATALOG_PATH,
    DEPRECATED_URN_ALIASES,
    IGNORED_DIRS,
    IGNORED_FILES,
    KORA_ROOT,
    LEGACY_BOOTSTRAP_URN_PATTERN,
    RETIRED_KB_URNS,
    ROOT_IGNORED_DIRS,
)
from .lifecycle import (
    is_deprecated_status,
    is_retired_status,
    read_declared_status,
)


def load_catalog():
    doc, _ = load_yaml_safe(CATALOG_PATH)
    if not doc or "Catalog" not in doc:
        return None
    return doc


def canonicalize_urn_reference(urn):
    current = urn
    visited = set()
    while current in DEPRECATED_URN_ALIASES and current not in visited:
        visited.add(current)
        current = DEPRECATED_URN_ALIASES[current]
    return current


def is_special_non_catalog_urn(urn):
    return bool(LEGACY_BOOTSTRAP_URN_PATTERN.fullmatch(urn))


def is_historical_urn(urn):
    return canonicalize_urn_reference(urn) in RETIRED_KB_URNS


def urn_is_known(urn, known_urns):
    canonical = canonicalize_urn_reference(urn)
    return (
        urn in known_urns
        or canonical in known_urns
        or canonical in RETIRED_KB_URNS
        or is_special_non_catalog_urn(urn)
    )


def get_reference_entry(urn, urn_to_entry):
    canonical = canonicalize_urn_reference(urn)
    return urn_to_entry.get(urn) or urn_to_entry.get(canonical)


def build_catalog_lookup(doc):
    urn_to_entry = {}
    known_urns = set()
    for category, items in doc["Catalog"].items():
        for item in items:
            urn = item.get("urn")
            if not urn:
                continue
            urn_to_entry[urn] = {
                "category": category,
                "file": KORA_ROOT / item["file"],
                "entry": item,
            }
            known_urns.add(urn)
    for alias, canonical in DEPRECATED_URN_ALIASES.items():
        canonical_entry = urn_to_entry.get(canonical)
        if canonical_entry:
            urn_to_entry[alias] = canonical_entry
            known_urns.add(alias)
    known_urns.add(doc["_manifest"]["urn"])
    known_urns.update(RETIRED_KB_URNS)
    return known_urns, urn_to_entry


def classify_catalog_category(urn, file_path):
    rel_path = str(file_path).replace("\\", "/")
    parts = urn.split(":")
    obj_type = parts[2] if len(parts) >= 3 else "unknown"

    if obj_type in ("agent", "agent-bootstrap"):
        return "Agents"
    if obj_type == "skill":
        return "Skills"
    if obj_type == "artefacto":
        if rel_path.startswith("artifacts/skills/") or rel_path.endswith("/SKILL.md"):
            return "Skills"
        if rel_path.startswith("artifacts/agents/") or rel_path.endswith("/AGENT.md"):
            return "Agents"
    if obj_type in ("kb", "core", "domain"):
        return "Knowledge"
    if obj_type in ("doc", "sys", "ref", "tool"):
        return "Documents"
    return "Other"


def cmd_index():
    print(f"Indexing KORA Monorepo at {KORA_ROOT}...")

    catalog = {
        "_manifest": {
            "urn": "urn:kora:catalog:master:2.0.0",
            "federation": {"visibility": "public"},
            "description": "Auto-generated Kora Monorepo Catalog",
        },
        "Catalog": {
            "Agents": [],
            "Skills": [],
            "Knowledge": [],
            "Documents": [],
            "Other": [],
        },
    }

    count = 0
    deprecated_count = 0
    extensions = {".yaml", ".yml", ".md", ".json"}

    for root, dirs, files in os.walk(KORA_ROOT):
        at_root = Path(root) == KORA_ROOT
        dirs[:] = sorted(
            directory for directory in dirs
            if directory not in IGNORED_DIRS
            and not (at_root and directory in ROOT_IGNORED_DIRS)
        )

        for file_name in sorted(files):
            file_path = KORA_ROOT / os.path.relpath(os.path.join(root, file_name), KORA_ROOT)
            if file_name in IGNORED_FILES and file_path.parent == KORA_ROOT:
                continue
            if file_path.suffix not in extensions:
                continue
            if file_path.absolute() == CATALOG_PATH.absolute():
                continue

            doc, err = load_yaml_safe(file_path)
            if err:
                # "No YAML frontmatter found" es un no-evento: muchos .md
                # auxiliares (READMEs locales, AGENTS.md raíz, etc.) no tienen
                # ni necesitan frontmatter. La validacion estructural es de
                # lint-md, no del indexador.
                if err != "No YAML frontmatter found":
                    print(f"[WARN] Error parsing {file_path.relative_to(KORA_ROOT)}: {err}")
                continue

            if (
                doc
                and isinstance(doc, dict)
                and "_manifest" in doc
                and "urn" in doc["_manifest"]
            ):
                manifest = doc["_manifest"]
                urn = manifest["urn"]
                status = read_declared_status(doc, default="publicado")

                if is_deprecated_status(status) or is_retired_status(status):
                    deprecated_count += 1
                    continue

                title = get_artifact_title(doc, file_path)
                rel_path = str(file_path.relative_to(KORA_ROOT))

                entry = {
                    "urn": urn,
                    "title": title,
                    "file": rel_path,
                    "status": status,
                }

                category = classify_catalog_category(urn, rel_path)
                catalog["Catalog"][category].append(entry)

                count += 1

    for category in catalog["Catalog"]:
        catalog["Catalog"][category].sort(key=lambda e: e.get("urn", ""))

    CATALOG_PATH.parent.mkdir(exist_ok=True)
    with open(CATALOG_PATH, "w", encoding="utf-8") as handle:
        yaml.dump(
            catalog,
            handle,
            sort_keys=False,
            allow_unicode=True,
            default_flow_style=False,
        )

    summary = f"Successfully indexed {count} artifacts into {CATALOG_PATH.relative_to(KORA_ROOT)}!"
    if deprecated_count:
        summary += f" ({deprecated_count} deprecated/retired skipped)"
    print(summary)


def cmd_resolve(urn):
    doc = load_catalog()
    if not doc or "Catalog" not in doc:
        print("Error: Catalog not found or invalid. Run 'kora index' first.")
        raise SystemExit(1)

    if urn in DEPRECATED_URN_ALIASES:
        urn = DEPRECATED_URN_ALIASES[urn]

    prefix_matches = []
    for category, items in doc["Catalog"].items():
        for item in items:
            item_urn = item.get("urn", "")
            if item_urn == urn:
                path = KORA_ROOT / item["file"]
                print(f"[{category}] {item_urn} -> {path.absolute()}")
                return
            if item_urn.startswith(urn):
                prefix_matches.append((category, item))

    if len(prefix_matches) == 1:
        category, item = prefix_matches[0]
        path = KORA_ROOT / item["file"]
        print(f"[{category}] {item['urn']} -> {path.absolute()}")
        return

    if prefix_matches:
        print(f"URN prefix '{urn}' is ambiguous. Matches:")
        for category, item in prefix_matches[:10]:
            print(f"  [{category}] {item['urn']}")
        raise SystemExit(1)

    print(f"URN '{urn}' not found in catalog.")
    raise SystemExit(1)
