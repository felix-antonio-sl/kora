#!/usr/bin/env python3
"""
Normaliza las referencias de catálogo en todos los agentes de kora.

Cambios:
1. _manifest.dependencies.catalog.file -> "catalog/catalog_master_kora.yml"
2. _manifest.dependencies.catalog.urn -> "urn:knowledge:koda:catalog:master-kora:1.0.0"
3. Menciones textuales de catálogos legacy en KODA_Runtime_Instructions y otros campos string.

Uso:
  python normalize_agent_catalogs.py          # Dry run
  python normalize_agent_catalogs.py --apply  # Aplicar cambios
"""

import os
import sys
import re
import glob

AGENTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "agents")

# Catálogos legacy a reemplazar
LEGACY_CATALOG_FILES = [
    "catalog/catalog_master_fxsl.yml",
    "catalog/catalog_master_gorenuble.yml",
    "catalog/catalog_master_koda.yml",
    "catalog/catalog_master_tde.yml",
    "catalog/catalog_master_orko.yml",
    "catalog/catalog_master_korvo.yml",
]

LEGACY_CATALOG_URNS = [
    "urn:knowledge:fxsl:catalog:master:1.0.0",
    "urn:knowledge:gorenuble:catalog:master:1.0.0",
    "urn:knowledge:koda:catalog:master:1.0.0",
    "urn:knowledge:tde:catalog:master:1.0.0",
    "urn:knowledge:orko:catalog:master:1.0.0",
    "urn:knowledge:korvo:catalog:master:1.0.0",
]

# Patrones textuales legacy en Runtime Instructions
LEGACY_TEXT_PATTERNS = [
    (r'catalog_master_fxsl\.yml', 'catalog_master_kora.yml'),
    (r'catalog_master_gorenuble\.yml', 'catalog_master_kora.yml'),
    (r'catalog_master_koda\.yml', 'catalog_master_kora.yml'),
    (r'catalog_master_tde\.yml', 'catalog_master_kora.yml'),
    (r'catalog_master_orko\.yml', 'catalog_master_kora.yml'),
    (r'catalog_master_korvo\.yml', 'catalog_master_kora.yml'),
]

NEW_CATALOG_FILE = "catalog/catalog_master_kora.yml"
NEW_CATALOG_URN = "urn:knowledge:koda:catalog:master-kora:1.0.0"

def process_agent_file(filepath, apply=False):
    """Procesa un archivo de agente YAML, reemplazando referencias de catálogo."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changes = []

    # 1. Reemplazar rutas de archivo de catálogo
    for legacy_file in LEGACY_CATALOG_FILES:
        # Manejar con y sin comillas
        for pattern in [
            f'file: "{legacy_file}"',
            f"file: '{legacy_file}'",
            f'file: {legacy_file}',
            f'file: "{legacy_file}",',
            f"file: '{legacy_file}',",
        ]:
            if pattern in content:
                replacement = pattern.replace(legacy_file, NEW_CATALOG_FILE)
                content = content.replace(pattern, replacement)
                changes.append(f"  catalog.file: {legacy_file} -> {NEW_CATALOG_FILE}")

    # 2. Reemplazar URNs de catálogo
    for legacy_urn in LEGACY_CATALOG_URNS:
        if legacy_urn in content:
            content = content.replace(legacy_urn, NEW_CATALOG_URN)
            changes.append(f"  catalog.urn: {legacy_urn} -> {NEW_CATALOG_URN}")

    # 3. Reemplazar menciones textuales en Runtime Instructions y otros strings
    for pattern, replacement in LEGACY_TEXT_PATTERNS:
        matches = re.findall(pattern, content)
        if matches:
            content = re.sub(pattern, replacement, content)
            if f"  text: {pattern}" not in [c for c in changes]:
                changes.append(f"  text: {matches[0]} -> {replacement}")

    # Eliminar duplicados de cambios textuales (porque el paso 1 ya hizo algunos)
    # Simplemente deduplicar
    # El paso 3 puede producir duplicados con el paso 1 si ya se reemplazó
    # pero re.sub sobre contenido ya modificado simplemente no matcha => OK

    if content != original:
        agent_name = os.path.basename(os.path.dirname(filepath))
        print(f"✏️  {agent_name}:")
        for change in changes:
            print(change)

        if apply:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✅ Guardado")
        else:
            print(f"  ⏸️  (dry run)")

        return len(changes)
    return 0


def main():
    apply = "--apply" in sys.argv
    mode = "APLICANDO" if apply else "DRY RUN"
    print(f"\n{'='*60}")
    print(f"  Normalización de Catálogos en Agentes — {mode}")
    print(f"{'='*60}\n")

    total_changes = 0
    total_agents = 0

    # Buscar todos los archivos agent_*.yaml
    for agent_dir in sorted(glob.glob(os.path.join(AGENTS_DIR, "*"))):
        if not os.path.isdir(agent_dir):
            continue
        for yaml_file in glob.glob(os.path.join(agent_dir, "agent_*.yaml")):
            changes = process_agent_file(yaml_file, apply=apply)
            if changes:
                total_agents += 1
                total_changes += changes

    print(f"\n{'='*60}")
    print(f"  Resumen: {total_changes} cambios en {total_agents} agentes")
    if not apply:
        print(f"  Para aplicar: python {os.path.basename(__file__)} --apply")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
