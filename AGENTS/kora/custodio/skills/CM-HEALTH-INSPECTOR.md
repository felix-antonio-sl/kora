---
_manifest:
  urn: urn:kora:skill:custodio-health-inspector:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-HEALTH-INSPECTOR

## Proposito
Ejecuta diagnostico completo del estado del repo KORA usando la interfaz semantica publicada del workspace. Consolida resultados en un reporte unico con severidades.

## Input/Output
- **Input:** (ninguno — ejecuta bateria de comandos diagnosticos)
- **Output:** HealthReport (ver Signature Output)

## Procedimiento
1. Invocar `repo_health` para obtener broken URNs, errores de validacion y metricas del repo.
2. Invocar `git_status` para obtener limpieza del worktree y contexto reciente de cambios.
3. Consolidar ambos resultados en tabla con columnas: Componente | Estado | Severidad | Detalle.
4. Emitir veredicto global: SANO(0 errors), ADVERTENCIA(solo warnings), CRITICO(>=1 error).
5. Si CRITICO, recomendar remediacion operativa priorizada con lista de issues.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| veredicto | enum(SANO\|ADVERTENCIA\|CRITICO) | Veredicto global |
| componentes | {componente, estado, severidad, detalle}[] | Estado por componente |
| recomendacion | string \| null | Accion recomendada si hay issues |
