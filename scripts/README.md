# Scripts de KORA

Este directorio mezcla toolchain activa, soporte de namespace y utilitarios historicos. No todo lo que vive en `scripts/` forma parte del core operativo del repo.

Las superficies operacionales locales (`inbox/`, `source/`, `drafts/`, `build/`) viven fisicamente bajo `OPERATIONS/` en la raiz del repo y quedan fuera del clone portable via `.gitignore`.

## Core Soportado

- `kora`: entrypoint oficial de la CLI del monorepo.
- `kora.bat`, `kora.ps1`: wrappers del entrypoint para otros shells.
- `kora_lib/`: implementacion soportada de `index`, `resolve`, `health`, `validate`, `stats`, `graph`, `migrate`, `sync-docs` e `intake`.

Estos artefactos son la superficie estable que debe funcionar en cualquier clon del repo.

## Soporte Acotado

- `sync_openclaw_docs_mirror.py`: mirror operativo para `KNOWLEDGE/agengai/openclaw/documentacion-oficial`. Esta coleccion es una excepcion explicita y soportada dentro del repo, aunque el script siga requiriendo root upstream explicito por CLI o variables de entorno.
- `gn_rebuild.py`, `gn_rebuild_map.yml`: pipeline de rebuild del dominio `gn`. No forman parte del core general de KORA.

Estos scripts pueden seguir siendo utiles, pero no deben confundirse con la CLI base del repo.

## Excepcion Soportada

- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/` es una excepcion institucional del repo.
- Su mecanismo de sincronizacion soportado es `scripts/sync_openclaw_docs_mirror.py`.
- Esta excepcion no convierte el resto de utilitarios de `scripts/` en superficie core.

## Utilitarios Ad-Hoc

- `source_mapper.py`: generador de mapeo de fuentes para trabajo editorial y de migracion.
- `telegraph_audit_repair.py`: reparador puntual de estilo/prosa.
- `check_counts.py`: conteo rapido de manifests YAML.
- `kora_transmuter.py`: codemod masivo de URNs de una fase previa.

Estos scripts no deben asumirse como entrypoints estables ni como parte del flujo recomendado del monorepo.

## Legacy Congelado

- `legacy_migration/`: scripts de migracion historica.
- `file_movement_map.json`: insumo de la migracion historica.

Su funcion es trazabilidad y soporte de migraciones pasadas. No son la toolchain actual y no deben usarse como base para automatizacion nueva.

## Regla Operativa

Si un flujo necesita ser soportado de forma institucional:

1. debe exponerse via `scripts/kora`
2. debe vivir en `scripts/kora_lib/`
3. debe tener cobertura de pruebas

Si no cumple esas tres condiciones, tratelo como soporte acotado, ad-hoc o legacy.
