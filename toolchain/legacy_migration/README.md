# Legacy Migration

`legacy_migration/` conserva scripts de transicion usados durante fases previas de reorganizacion del repo.

Estado operativo:

- congelado
- fuera de la toolchain soportada
- sin garantia de portabilidad entre clones o entornos

Regla de uso:

- no agregar automatizacion nueva aqui
- no tomar estos scripts como referencia para el core actual
- si una capacidad sigue siendo necesaria, reimplementarla en `toolchain/kora_lib/` y exponerla via `toolchain/kora`
- este subarbol esta **excluido del check `portabilidad-tests`** por diseño:
  son archivos arqueologicos con paths literales esperables

Scripts one-shot incorporados en 2026-04-19 desde `toolchain/` top-level:

- `analyze_hd_routes.py` — analisis de rutas HDOS (enero-marzo 2026)
- `migrate_to_agentfile.py` — migracion 5-file -> AGENT.md (autoria-spec v1.0)
- `migrate_hodom_to_ideal.py` + `generate_hodom_ideal_workbook.py` — migracion del workbook HODOM 2025 al template ideal
