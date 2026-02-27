---
_manifest:
  urn: "urn:dev:skill:sentinel-intent-classifier:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-INTENT-CLASSIFIER

## Proposito
Clasifica la intencion del usuario en la FSM WF-SENTINEL.

## Procedimiento
1. Analizar mensaje: palabras clave, artefactos mencionados (context files, metricas, evals, tarjetas purpura).
2. Clasificar capacidad: CONTEXT_HYGIENE(drift, convenciones, arquitectura, coherencia), SWARM_AUDIT(rendimiento, metricas, agentes, topologia), EVAL_AUDIT(cobertura, gaps, golden dataset, obsolescencia), PURPLE_CARD(proponer, mejora, optimizar), SELF_EVAL(auto-evaluacion, meta-eval, sentinel health), END(terminar).
3. Verificar diversidad de modelo: si el provider actual es el mismo que el enjambre, ABORTAR.
4. Emitir clasificacion: {capacidad, diversidad_ok, confianza}.

## Output
Clasificacion: `capacidad` (enum), `diversidad_ok` (bool), `confianza` (alta|media|baja). Si diversidad_ok=false, ABORTAR.
