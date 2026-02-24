---
_manifest:
  urn: "urn:fxsl:skill:reviewer-intent-classifier:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-INTENT-CLASSIFIER

## Proposito
Clasifica la intencion del usuario en la FSM WF-REVIEWER.

## Procedimiento
1. Analizar mensaje: palabras clave, artefactos mencionados (PRs, diffs, hallazgos, evals).
2. Clasificar capacidad: REVIEW(revisar PR, code review, analizar cambios), SEGURIDAD(vulnerabilidad, security, OWASP, injection), EVAL(regresion, alucinacion, dataset, eval), END(terminar).
3. Si el mensaje contiene un PR o diff → REVIEW.
4. Si el mensaje pregunta especificamente sobre seguridad → SEGURIDAD.
5. Si el mensaje pide ejecutar evals → EVAL.
6. Verificar diversidad de modelo ANTES de clasificar: si el provider actual es el mismo que uso el coder, ABORTAR.
7. Emitir clasificacion: {capacidad, diversidad_ok, confianza}.

## Output
Clasificacion: `capacidad` (enum), `diversidad_ok` (bool), `confianza` (alta|media|baja). Si diversidad_ok=false, ABORTAR review.
