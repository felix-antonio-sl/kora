---
_manifest:
  urn: "urn:fxsl:skill:planner-intent-classifier:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-INTENT-CLASSIFIER

## Proposito
Clasifica la intencion del usuario en la FSM WF-PLANNER, determinando la capacidad de planificacion requerida.

## Procedimiento
1. Analizar mensaje: palabras clave, contexto previo, artefactos mencionados (OKRs, epicas, historias, backlog).
2. Clasificar capacidad: OKR(definir objetivos, ciclo, key results), EPICA(descomponer, desglosar), HISTORIA(refinar, criterios, aceptacion, complejidad, riesgo), BACKLOG(priorizar, flujo, siguiente), PREDICTIVO(proponer, sugerir, patrones), RETRO(retrospectiva, metricas, ciclo cerrado), END(terminar).
3. Detectar sombrero activo: PO(definiendo valor) vs Operador(configurando). Alertar si hay mezcla.
4. Emitir clasificacion: {capacidad, sombrero, confianza}.

## Output
Clasificacion con campos: `capacidad` (enum), `sombrero` (PO|Operador|ambiguo), `confianza` (alta|media|baja). Si confianza=baja, formular pregunta aclaratoria.
