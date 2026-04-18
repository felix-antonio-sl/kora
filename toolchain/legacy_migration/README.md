# Legacy Migration

`legacy_migration/` conserva scripts de transicion usados durante fases previas de reorganizacion del repo.

Estado operativo:

- congelado
- fuera de la toolchain soportada
- sin garantia de portabilidad entre clones o entornos

Regla de uso:

- no agregar automatizacion nueva aqui
- no tomar estos scripts como referencia para el core actual
- si una capacidad sigue siendo necesaria, reimplementarla en `scripts/kora_lib/` y exponerla via `scripts/kora`
