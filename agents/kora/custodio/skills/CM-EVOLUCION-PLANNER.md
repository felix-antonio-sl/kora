---
_manifest:
  urn: "urn:kora:skill:custodio-evolucion-planner:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-EVOLUCION-PLANNER

## Proposito
Planifica mejoras estructurales al repo KORA como entidad: reorganizacion de directorios, nuevas convenciones, nuevos scripts CLI, optimizacion de pipeline.

## I/O

- **Input:** estado_actual: HealthReport | StructureAuditReport (diagnosticos previos), areas_friccion: string[] | null
- **Output:** EvolutionPlan (ver Signature Output)

## Procedimiento
1. Analizar estado actual: metricas (kora stats), estructura (filesystem scan), gaps detectados en auditorias previas.
2. Identificar areas de friccion: procesos manuales repetitivos, convenciones inconsistentes, scripts faltantes, pipeline con cuellos de botella.
3. Proponer mejoras como lista priorizada:
   - Impacto: alto|medio|bajo.
   - Esfuerzo: alto|medio|bajo.
   - Riesgo: alto|medio|bajo.
4. Para cada mejora aprobada:
   - Disenar plan de implementacion paso a paso.
   - Identificar archivos afectados.
   - Definir criterio de exito verificable.
5. Implementar mejoras aprobadas secuencialmente. Verificar cada paso.
6. Post-implementacion: ejecutar kora health para confirmar que no se introdujeron regresiones.

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| mejoras | {mejora, impacto, esfuerzo, riesgo, archivos_afectados}[] | Plan priorizado de mejoras |
| verificacion | enum(PASS\|FAIL) \| null | Resultado post-implementacion (si se implemento) |
