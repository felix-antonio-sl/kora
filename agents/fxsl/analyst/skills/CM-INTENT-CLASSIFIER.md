---
_manifest:
  urn: "urn:fxsl:skill:analyst-intent-classifier:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-INTENT-CLASSIFIER

## Proposito
Clasifica la intencion del usuario en la FSM WF-ANALYST, determinando la capacidad analitica requerida.

## Procedimiento
1. Analizar mensaje: palabras clave, contexto previo, artefactos mencionados (metricas, dashboard, reporte, tendencia, backlog).
2. Clasificar capacidad: METRICAS(cph, ta, cycle time, tokens, coste, aceptacion), DASHBOARD(tablero, dimensiones, neural, panorama), REPORTE(retrospectiva, retro, ciclo cerrado, okr progreso, fin de ciclo), TENDENCIA(trend, inter-ciclo, comparar, inflexion, curva, historico), BACKLOG_HEALTH(flujo, wip, bottleneck, stale, cola, profundidad), END(terminar).
3. Detectar granularidad solicitada: snapshot(un Ciclo) vs comparativa(multi-Ciclo) vs drill-down(una metrica especifica).
4. Emitir clasificacion: {capacidad, granularidad, confianza}.

## Output
Clasificacion con campos: `capacidad` (enum), `granularidad` (snapshot|comparativa|drill_down), `confianza` (alta|media|baja). Si confianza=baja, formular pregunta aclaratoria.
