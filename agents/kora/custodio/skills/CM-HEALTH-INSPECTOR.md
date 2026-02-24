---
_manifest:
  urn: "urn:kora:skill:custodio-health-inspector:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-HEALTH-INSPECTOR

## Proposito
Ejecuta diagnostico completo del estado del repo KORA. Consolida resultados de multiples herramientas en un reporte unico con severidades.

## Procedimiento
1. Ejecutar `scripts/kora health` → capturar broken URNs.
2. Ejecutar `scripts/kora validate` → capturar errores de validacion de agentes.
3. Ejecutar `scripts/kora stats` → capturar metricas (artifacts, agents, namespaces, skills).
4. Ejecutar `git status` + `git log --oneline -5` → capturar estado git.
5. Consolidar en tabla con columnas: Componente | Estado | Severidad | Detalle.
6. Emitir veredicto global: SANO(0 errors), ADVERTENCIA(solo warnings), CRITICO(>=1 error).
7. Si CRITICO, recomendar transicion a S-CIRUGIA con lista de issues.

## Output
Reporte tabular con veredicto global. Formato: tabla markdown + veredicto + recomendacion.
