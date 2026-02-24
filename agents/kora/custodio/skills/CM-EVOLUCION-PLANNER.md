---
_manifest:
  urn: "urn:kora:skill:custodio-evolucion-planner:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-EVOLUCION-PLANNER

## Proposito
Planifica mejoras estructurales al repo KORA como entidad: reorganizacion de directorios, nuevas convenciones, nuevos scripts CLI, optimizacion de pipeline.

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

## Output
Plan de evolucion: tabla {mejora, impacto, esfuerzo, riesgo, archivos_afectados}. Post-implementacion: reporte de verificacion.
