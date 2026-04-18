#!/usr/bin/env python3
"""
koda-migrator: Fase 2 — Consolidación de Catálogos para Kora
Une los 6 catálogos migrados (en /tmp/koda_migration_backups/) en un único
catalog_master_kora.yml, reescribiendo los paths físicos hacia la estructura canónica.
Además, genera un file_movement_map.json para la Fase 3.
"""

from pathlib import Path
import yaml
import json
import re

# Configuración
TEMP_DIR = Path("/tmp/koda_migration_backups")
KODA_ROOT = Path("/Users/felixsanhueza/Developer/koda")
KORA_ROOT = Path("/Users/felixsanhueza/Developer/kora")

# Lista de catálogos migrantes
CATALOGS = [
    ("koda", KODA_ROOT / "catalog" / "catalog_master_koda.yml"),
    ("fxsl", TEMP_DIR / "catalog_master_fxsl_migrated.yml"),
    ("gorenuble", TEMP_DIR / "catalog_master_gorenuble_migrated.yml"),
    ("tde", TEMP_DIR / "catalog_master_tde_migrated.yml"),
    ("orko", TEMP_DIR / "catalog_master_orko_migrated.yml"),
    ("korvo", TEMP_DIR / "catalog_master_korvo_migrated.yml"),
]


def parse_urn(urn_str: str):
    parts = urn_str.replace("urn:knowledge:", "").split(":")
    if len(parts) >= 4:
        return parts[0], parts[1], ":".join(parts[2:-1]), parts[-1]
    return None, None, None, None


def get_canonical_path(domain, artifact, old_path):
    """Calcula la ruta canónica en kora basada en la convención del resolver."""
    ext = Path(old_path).suffix if old_path else ".yml"
    if not ext:
        ext = ".yml"

    artifact_underscore = artifact.replace("-", "_")

    if domain == "agents":
        return f"agents/{artifact}/agent_{artifact_underscore}.yaml"
    elif domain == "skills":
        return f"skills/own/{artifact}/skill_{artifact_underscore}.yaml"
    elif domain == "tools":
        return f"tools/{artifact}{ext}"
    elif domain == "catalog":
        return "catalog/catalog_master_kora.yml"
    else:
        return f"knowledge/domains/{domain}/{artifact}{ext}"


def main():
    print("=" * 60)
    print("KORA Migrator — Fase 2: Consolidación de Catálogo Maestro")
    print("=" * 60)

    consolidated = {
        "_manifest": {
            "urn": "urn:knowledge:koda:catalog:master-kora:1.0.0",
            "federation": {"visibility": "public", "license": "CC-BY-4.0"},
            "provenance": {
                "created_by": "Koda Migrator",
                "created_at": "2026-02-20",
                "note": "Consolidación de koda, fxsl, gorenuble, tde, orko, korvo",
            },
        },
        "Catalog": {"Agents": [], "Skills": [], "IDE_Tools": [], "Domains": []},
        "Statistics": {
            "total_artifacts": 0,
            "agents": 0,
            "skills": 0,
            "tools": 0,
            "domains": 0,
        },
    }

    movement_map = []
    seen_urns = set()

    for ws_name, path in CATALOGS:
        if not path.exists():
            print(f"⚠️  No encontrado: {path}")
            continue

        try:
            with open(path, "r") as f:
                data = yaml.safe_load(f)
        except Exception as e:
            print(f"Error parseando {path}: {e}")
            continue

        print(f"📦 Procesando {ws_name}...")

        # Helper recursivo
        def process_entries(entries_list, category):
            if not entries_list:
                return
            for entry in entries_list:
                urn = entry.get("urn")
                if not urn or urn in seen_urns:
                    continue
                seen_urns.add(urn)

                ns, domain, artifact, version = parse_urn(urn)
                if not ns:
                    continue

                old_file = entry.get("file", "")

                # Excepciones que no movemos (registros virtuales, Gist base, o ya integrados)
                if "catalog:master-" in urn:
                    continue

                new_file = get_canonical_path(domain, artifact, old_file)
                entry["file"] = new_file

                # Añadir a map
                if old_file:
                    movement_map.append(
                        {
                            "urn": urn,
                            "workspace": ws_name,
                            "old_path": old_file,
                            "new_path": new_file,
                            "type": domain,
                        }
                    )

                if domain == "agents":
                    consolidated["Catalog"]["Agents"].append(entry)
                    consolidated["Statistics"]["agents"] += 1
                elif domain == "skills":
                    consolidated["Catalog"]["Skills"].append(entry)
                    consolidated["Statistics"]["skills"] += 1
                elif domain == "tools":
                    consolidated["Catalog"]["IDE_Tools"].append(entry)
                    consolidated["Statistics"]["tools"] += 1
                else:
                    consolidated["Catalog"]["Domains"].append(entry)
                    consolidated["Statistics"]["domains"] += 1

                consolidated["Statistics"]["total_artifacts"] += 1

        cat = data.get("Catalog", {})

        # Procesar listas comunes
        process_entries(cat.get("Agents", []), "agents")
        process_entries(cat.get("Skills", []), "skills")
        process_entries(cat.get("IDE_Tools", []), "tools")
        process_entries(cat.get("Domains", []), "domains")

        # El catálogo original de koda podría tener Core_Guides y Schemas
        process_entries(cat.get("Core_Guides", []), "domains")
        process_entries(cat.get("Schemas", []), "domains")

        # fxsl tiene un Gist[] manual
        process_entries(cat.get("Gist", []), "domains")

    output_catalog = KORA_ROOT / "catalog" / "catalog_master_kora.yml"
    with open(output_catalog, "w") as f:
        yaml.dump(
            consolidated,
            f,
            default_flow_style=False,
            sort_keys=False,
            allow_unicode=True,
        )

    output_map = KORA_ROOT / "scripts" / "file_movement_map.json"
    KORA_ROOT.joinpath("scripts").mkdir(parents=True, exist_ok=True)
    with open(output_map, "w") as f:
        json.dump(movement_map, f, indent=2)

    print(f"\n✅ Catálogo unificado generado: {output_catalog}")
    print(f"📊 Estadísticas finales:")
    print(f"   - Agentes: {consolidated['Statistics']['agents']}")
    print(f"   - Dominios (Artefactos): {consolidated['Statistics']['domains']}")
    print(f"   - Total Entradas: {consolidated['Statistics']['total_artifacts']}")
    print(f"\n✅ Movement map generado: {output_map}")


if __name__ == "__main__":
    main()
