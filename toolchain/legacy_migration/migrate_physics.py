#!/usr/bin/env python3
"""
kora-migrator: Fase 3 — Migración Física de Archivos y Mutación AST
Copia los artefactos desde los workspaces satélites a `kora/`, al mismo
tiempo que muta estructuralmente todas sus URNs internas y referencias.
"""

import sys
from pathlib import Path
import json
import yaml
import csv
import re
import argparse

KORA_ROOT = Path("/Users/felixsanhueza/Developer/kora")
DEV_DIR = Path("/Users/felixsanhueza/Developer")

LOOKUP_CSV = Path("/tmp/koda_lookup_table.csv")
MOVEMENT_MAP = KORA_ROOT / "scripts" / "file_movement_map.json"

URN_PATTERN = re.compile(
    r"urn:knowledge:[a-z0-9_-]+:[a-z0-9_:-]+:[a-z0-9_.-]+:[0-9.*]+"
)


def load_lookup_table(csv_path: Path) -> dict:
    lookup = {}
    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            lookup[row["urn_legacy"]] = row["urn_new"]
    return lookup


def migrate_value(value, lookup: dict) -> tuple:
    if not isinstance(value, str):
        return value, False

    if not value.startswith("urn:knowledge:"):
        matches = URN_PATTERN.findall(value)
        if not matches:
            return value, False
        changed = False
        new_value = value
        for match in matches:
            if match in lookup:
                new_value = new_value.replace(match, lookup[match])
                changed = True
        return new_value, changed

    if value in lookup:
        return lookup[value], True
    return value, False


def walk_and_migrate(obj, lookup: dict, path: str = "", changes: list = None):
    if changes is None:
        changes = []

    if isinstance(obj, dict):
        for key in list(obj.keys()):
            child_path = f"{path}.{key}"
            if isinstance(obj[key], str):
                new_val, changed = migrate_value(obj[key], lookup)
                if changed:
                    changes.append(
                        {"path": child_path, "old": obj[key], "new": new_val}
                    )
                    obj[key] = new_val
            elif isinstance(obj[key], (dict, list)):
                walk_and_migrate(obj[key], lookup, child_path, changes)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            child_path = f"{path}[{i}]"
            if isinstance(item, str):
                new_val, changed = migrate_value(item, lookup)
                if changed:
                    changes.append({"path": child_path, "old": item, "new": new_val})
                    obj[i] = new_val
            elif isinstance(item, (dict, list)):
                walk_and_migrate(item, lookup, child_path, changes)

    return changes


def main():
    parser = argparse.ArgumentParser(
        description="KORA Migrator - Fase 3: Archivos Físicos"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Reportar sin copiar archivos"
    )
    args = parser.parse_args()

    if not LOOKUP_CSV.exists() or not MOVEMENT_MAP.exists():
        print("❌ Faltan archivos base (Lookup CSV o Movement Map)")
        sys.exit(1)

    lookup = load_lookup_table(LOOKUP_CSV)
    with open(MOVEMENT_MAP, "r") as f:
        movements = json.load(f)

    print(f"{'=' * 60}")
    print(f"KORA Migrator — Fase 3: Migración Física y AST")
    print(f"{'=' * 60}")
    print(f"📋 Archivos a migrar: {len(movements)}")
    print(f"🔧 Modo: {'DRY RUN' if args.dry_run else 'EJECUCIÓN REAL'}")

    successes = 0
    failures = 0
    total_mutations = 0

    for m in movements:
        src_path = DEV_DIR / m["workspace"] / m["old_path"]
        dst_path = KORA_ROOT / m["new_path"]

        if not src_path.exists():
            print(f"   ⚠️  [MISSING] {m['workspace']}/{m['old_path']}")
            failures += 1
            continue

        try:
            with open(src_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"   ⚠️  [READ ERROR] {src_path.name}: {e}")
            failures += 1
            continue

        # Realizar reemplazo de strings brutalmente efectivo y seguro
        new_content = content
        mutations_in_file = 0

        # Encontrar todas las URNs en el texto
        matches = URN_PATTERN.findall(content)
        for match in set(matches):
            if match in lookup:
                new_content = new_content.replace(match, lookup[match])
                mutations_in_file += (
                    new_content.count(lookup[match])
                    - content.count(lookup[match])
                    + content.count(match)
                )
                # Count might be slightly off due to multiple replacements, but this is roughly how many instances matched

        # Recuento real de mutaciones
        actual_mutations = 0
        for old_urn, new_urn in lookup.items():
            if old_urn in content:
                actual_mutations += content.count(old_urn)
                new_content = new_content.replace(old_urn, new_urn)

        total_mutations += actual_mutations

        if not args.dry_run:
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            try:
                with open(dst_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(
                    f"   ✅ [MIGRADO] {m['new_path']} ({actual_mutations} refs adaptadas)"
                )
                successes += 1
            except Exception as e:
                print(f"   ❌ [WRITE ERROR] {dst_path.name}: {e}")
                failures += 1
        else:
            if actual_mutations > 0:
                print(
                    f"   ℹ️  [DRY-RUN] {m['old_path']} -> {m['new_path']} ({actual_mutations} mutaciones)"
                )
            else:
                print(
                    f"   ℹ️  [DRY-RUN] {m['old_path']} -> {m['new_path']} (0 mutaciones)"
                )
            successes += 1

    print(f"\n{'=' * 60}")
    print(f"📊 Resumen Fase 3:")
    print(f"   Procesados con éxito: {successes}")
    print(f"   Fallos/Extraviados:   {failures}")
    print(f"   Referencias mutadas:  {total_mutations}")
    if args.dry_run:
        print("\nPara ejecutar realmente: python3 scripts/migrate_physics.py")


if __name__ == "__main__":
    main()
