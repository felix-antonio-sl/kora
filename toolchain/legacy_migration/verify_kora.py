#!/usr/bin/env python3
"""
kora-validator: Fase 4 — Validación Estática de Integridad
Verifica que cada ruta de archivo registrada en catalog_master_kora.yml
tenga un archivo existente, y que el _manifest.urn interno coincida.
"""

import sys
from pathlib import Path
import yaml
import re

KORA_ROOT = Path(__file__).resolve().parent.parent


def check_catalog():
    catalog_path = KORA_ROOT / "catalog" / "catalog_master_kora.yml"
    if not catalog_path.exists():
        print(f"❌ Catálogo no encontrado en {catalog_path}")
        sys.exit(1)

    with open(catalog_path, "r") as f:
        data = yaml.safe_load(f)

    cat = data.get("Catalog", {})
    entries = []

    # Recopilar todos
    entries.extend(cat.get("Agents", []))
    entries.extend(cat.get("Skills", []))
    entries.extend(cat.get("IDE_Tools", []))
    entries.extend(cat.get("Domains", []))

    total = len(entries)
    errors = 0
    warnings = 0

    # Extrae el URN con regex simple para archivos como SKILL.md o YAMLs donde safe_load falla fácilmente
    urn_regex = re.compile(r"urn:\s*(urn:knowledge:koda:[^\s]+)")

    for entry in entries:
        expected_urn = entry.get("urn")
        rel_path = entry.get("file")

        if not rel_path:
            continue

        full_path = KORA_ROOT / rel_path
        if not full_path.exists():
            print(f"❌ [MISSING FILE] {rel_path} (Referenciado por {expected_urn})")
            errors += 1
            continue

        try:
            with open(full_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Buscar urn en el contenido
            matches = urn_regex.findall(content)
            if not matches:
                # Intento 2 con comillas si las hay
                urn_regex2 = re.compile(r'urn:\s*"?(urn:knowledge:koda:[^"\s]+)"?')
                matches = urn_regex2.findall(content)

            if matches:
                internal_urn = matches[0]
                if internal_urn != expected_urn:
                    print(f"⚠️  [URN MISMATCH] {rel_path}")
                    print(f"   Catálogo dice: {expected_urn}")
                    print(f"   Archivo dice:  {internal_urn}")
                    warnings += 1
            else:
                # Algunos SKILL.md u otros no tienen manifest.urn, los ignoramos con warning
                # Pero en KODA deberían tener
                print(f"⚠️  [NO URN FOUND] {rel_path}")
                warnings += 1

        except Exception as e:
            print(f"❌ [READ ERROR] {rel_path}: {e}")
            errors += 1

    print(f"\n============================================================")
    print(f"✅ Validación Completada")
    print(f"📊 Totales analizados: {total}")
    print(f"❌ Errores Críticos:  {errors}")
    print(f"⚠️  Advertencias:      {warnings}")

    if errors > 0:
        sys.exit(1)


if __name__ == "__main__":
    check_catalog()
