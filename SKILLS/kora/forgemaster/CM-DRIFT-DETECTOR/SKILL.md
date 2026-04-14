---
_manifest:
  urn: urn:kora:skill:forgemaster-drift-detector:1.0.0
  type: lazy_load_endofunctor
---

# CM-DRIFT-DETECTOR

## Proposito
Compara el workspace fuente KORA con los artefactos derivados existentes para detectar drift (divergencia), identificando que componentes requieren re-transmutacion.

## Input/Output
- **Input:** agent_path: string, derived_path: string
- **Output:** DriftReport (ver Signature Output)

## Procedimiento
1. Leer `_transmutation.yml` del directorio derivado. Si no existe → reportar "sin manifest, re-transmutacion completa requerida".
2. Para cada componente registrado en manifest.source.hashes:
   - Calcular hash SHA-256 actual del archivo fuente.
   - Comparar con hash almacenado en manifest.
   - Si difiere → marcar como DRIFT.
   - Si archivo fuente no existe → marcar como DELETED.
3. Verificar si hay archivos nuevos en workspace fuente no registrados en manifest (skills nuevos, componentes agregados) → marcar como NEW.
4. Calcular edad del manifest: dias desde manifest.metadata.transmitted_at.
5. Generar tabla de drift:
   ```
   | Componente | Hash Fuente | Hash Derivado | Estado |
   |------------|-------------|---------------|--------|
   | AGENTS.md  | abc123...   | abc123...     | OK     |
   | SOUL.md    | def456...   | aaa111...     | DRIFT  |
   | skills/CM-X| (nuevo)     | —             | NEW    |
   ```
6. Si hay drift → recomendar re-transmutacion selectiva de componentes afectados.
7. Si sin drift → confirmar que derivados estan sincronizados.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| has_drift | boolean | True si algun componente diverge |
| drift_components | string[] | Componentes con drift |
| new_components | string[] | Componentes nuevos no transmutados |
| deleted_components | string[] | Componentes eliminados en fuente |
| manifest_age_days | number | Dias desde ultima transmutacion |
| drift_table | DriftEntry[] | Tabla detallada componente por componente |
