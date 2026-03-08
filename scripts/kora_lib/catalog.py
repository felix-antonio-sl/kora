import os

import yaml

from .artifacts import get_artifact_title, load_yaml_safe
from .config import CATALOG_PATH, IGNORED_DIRS, IGNORED_FILES, KORA_ROOT


def load_catalog():
    doc, _ = load_yaml_safe(CATALOG_PATH)
    if not doc or "Catalog" not in doc:
        return None
    return doc


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
    known_urns.add(doc["_manifest"]["urn"])
    return known_urns, urn_to_entry


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
    extensions = {".yaml", ".yml", ".md", ".json"}

    for root, dirs, files in os.walk(KORA_ROOT):
        dirs[:] = [directory for directory in dirs if directory not in IGNORED_DIRS]

        for file_name in files:
            file_path = KORA_ROOT / os.path.relpath(os.path.join(root, file_name), KORA_ROOT)
            if file_name in IGNORED_FILES and file_path.parent == KORA_ROOT:
                continue
            if file_path.suffix not in extensions:
                continue
            if file_path.absolute() == CATALOG_PATH.absolute():
                continue

            doc, err = load_yaml_safe(file_path)
            if err:
                print(f"[WARN] Error parsing {file_path.relative_to(KORA_ROOT)}: {err}")
                continue

            if (
                doc
                and isinstance(doc, dict)
                and "_manifest" in doc
                and "urn" in doc["_manifest"]
            ):
                urn = doc["_manifest"]["urn"]
                title = get_artifact_title(doc, file_path)
                rel_path = str(file_path.relative_to(KORA_ROOT))

                entry = {
                    "urn": urn,
                    "title": title,
                    "file": rel_path,
                    "status": doc.get("status", doc.get("Status", "published")),
                }

                parts = urn.split(":")
                obj_type = parts[2] if len(parts) >= 3 else "unknown"

                if obj_type in ("agent", "agent-bootstrap"):
                    catalog["Catalog"]["Agents"].append(entry)
                elif obj_type == "skill":
                    catalog["Catalog"]["Skills"].append(entry)
                elif obj_type in ("kb", "core", "domain"):
                    catalog["Catalog"]["Knowledge"].append(entry)
                elif obj_type in ("doc", "sys", "ref", "tool"):
                    catalog["Catalog"]["Documents"].append(entry)
                else:
                    catalog["Catalog"]["Other"].append(entry)

                count += 1

    CATALOG_PATH.parent.mkdir(exist_ok=True)
    with open(CATALOG_PATH, "w", encoding="utf-8") as handle:
        yaml.dump(
            catalog,
            handle,
            sort_keys=False,
            allow_unicode=True,
            default_flow_style=False,
        )

    print(f"Successfully indexed {count} artifacts into {CATALOG_PATH.relative_to(KORA_ROOT)}!")


def cmd_resolve(urn):
    doc = load_catalog()
    if not doc or "Catalog" not in doc:
        print("Error: Catalog not found or invalid. Run 'kora index' first.")
        raise SystemExit(1)

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
