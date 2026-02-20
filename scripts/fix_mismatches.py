#!/usr/bin/env python3
"""
kora-fixer: Sincroniza las URNs internas que quedaron desajustadas.
Lee el catálogo, y si el archivo físico tiene una URN interna diferente,
hace el replace exacto de esa cadena de texto por la URN esperada en el catálogo.
"""

import sys
from pathlib import Path
import yaml
import re

KORA_ROOT = Path(__file__).resolve().parent.parent


def fix_mismatches():
    catalog_path = KORA_ROOT / "catalog" / "catalog_master_kora.yml"

    with open(catalog_path, "r") as f:
        data = yaml.safe_load(f)

    cat = data.get("Catalog", {})
    entries = []
    entries.extend(cat.get("Agents", []))
    entries.extend(cat.get("Skills", []))
    entries.extend(cat.get("IDE_Tools", []))
    entries.extend(cat.get("Domains", []))

    urn_regex = re.compile(r"urn:\s*(urn:knowledge:koda:[^\s]+)")
    urn_regex2 = re.compile(r'urn:\s*"?(urn:knowledge:koda:[^"\s]+)"?')

    fixes = 0

    for entry in entries:
        expected_urn = entry.get("urn")
        rel_path = entry.get("file")
        if not rel_path:
            continue

        full_path = KORA_ROOT / rel_path
        if not full_path.exists():
            continue

        try:
            with open(full_path, "r", encoding="utf-8") as f:
                content = f.read()

            matches = urn_regex.findall(content)
            if not matches:
                matches = urn_regex2.findall(content)

            if matches:
                internal_urn = matches[0]
                if internal_urn != expected_urn:
                    # Fix it!
                    print(f"🔧 Arreglando {rel_path}: {internal_urn} -> {expected_urn}")
                    new_content = content.replace(internal_urn, expected_urn)
                    with open(full_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    fixes += 1

        except Exception as e:
            pass

    print(f"✅ {fixes} archivos corregidos exitosamente.")


if __name__ == "__main__":
    fix_mismatches()
