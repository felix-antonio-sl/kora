#!/usr/bin/env python3
"""
kora-deprecate: Marca los repositorios satélites como obsoletos
después de la consolidación exitosa en kora.
"""

from pathlib import Path
import datetime

KORA_ROOT = Path(__file__).resolve().parent.parent
DEV_DIR = KORA_ROOT.parent

SATELLITES = ["fxsl", "gorenuble", "tde", "orko", "korvo"]

DEPRECATION_NOTICE = f"""# ⚠️ REPOSITORIO DEPRECADO (KODA)

Este repositorio ha sido oficialmente deprecado como workspace del ecosistema KODA en fecha {datetime.date.today().isoformat()}.

> **Migración a Monorepo:** 
> Todos los agentes, artefactos de conocimiento y herramientas han sido migrados estructural y lógicamente al nuevo monorepo unificado:
> **`{KORA_ROOT}`**

## Consecuencias:
- El catálogo maestro original (`catalog/catalog_master_*.yml`) ha dejado de ser la fuente de verdad.
- Las URNs originales (ej. `urn:knowledge:fxsl:*`) han sido unificadas bajo el namespace canónico `koda:*`.
- Cualquier modificación a agentes KODA debe realizarse exclusivamente en el repositorio `kora`.

*Este repositorio puede conservarse para propósitos de código funcional o tooling legacy (ej. base de datos), pero la capa cognitiva KODA ha sido extraída.*
"""


def main():
    for sat in SATELLITES:
        sat_path = DEV_DIR / sat
        if not sat_path.exists():
            continue

        dep_file = sat_path / "KODA_DEPRECATED.md"
        with open(dep_file, "w", encoding="utf-8") as f:
            f.write(DEPRECATION_NOTICE)

        print(f"✅ Deprecado: {sat_path.name}")


if __name__ == "__main__":
    main()
