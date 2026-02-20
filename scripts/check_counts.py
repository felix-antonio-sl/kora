import os
import yaml
from pathlib import Path

KORA_ROOT = Path("/Users/felixsanhueza/Developer/kora")

yaml_files = list(KORA_ROOT.rglob("*.yml")) + list(KORA_ROOT.rglob("*.yaml"))
yaml_files = [
    f for f in yaml_files if ".git" not in str(f) and "scripts/" not in str(f)
]

indexed = 0
not_indexed = []

for f in yaml_files:
    try:
        with open(f, "r") as fp:
            doc = yaml.safe_load(fp)
        if isinstance(doc, dict) and "_manifest" in doc and "urn" in doc["_manifest"]:
            indexed += 1
        else:
            not_indexed.append(f.relative_to(KORA_ROOT))
    except Exception as e:
        not_indexed.append(f"{f.relative_to(KORA_ROOT)} (Error: {e})")

print(f"Total YAML files: {len(yaml_files)}")
print(f"Indexed (has _manifest.urn): {indexed}")
print(f"Not indexed ({len(not_indexed)}):")
for f in not_indexed:
    print(f"  - {str(f)}")
