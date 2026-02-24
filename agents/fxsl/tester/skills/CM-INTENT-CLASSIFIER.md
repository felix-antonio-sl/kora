---
_manifest:
  urn: "urn:fxsl:skill:tester-intent-classifier:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-INTENT-CLASSIFIER

## Proposito
Clasifica la intencion del usuario en la FSM WF-TESTER, determinando la capacidad de verificacion requerida.

## Procedimiento
1. Analizar mensaje: palabras clave, artefactos mencionados (historias, ACs, suites, cobertura, endpoints), contexto previo.
2. Clasificar capacidad: ACCEPTANCE(historia, ACs, criterios, aceptacion, story), INTEGRATION(boundary, api, endpoint, cross-component, integracion, servicio), EXECUTE(ejecutar, run, correr, suite, pasar tests), COVERAGE(cobertura, coverage, gaps, reporte, untested), END(terminar).
3. Si el mensaje contiene una historia con ACs → ACCEPTANCE.
4. Si el mensaje menciona endpoints, APIs o boundaries entre componentes → INTEGRATION.
5. Si el mensaje pide ejecutar o correr tests → EXECUTE.
6. Si el mensaje pide reporte de cobertura o gaps → COVERAGE.
7. Si el mensaje pide escribir codigo de produccion → RECHAZAR (fuera de scope).
8. Emitir clasificacion: {capacidad, confianza}.

## Output
Clasificacion: `capacidad` (enum), `confianza` (alta|media|baja). Si confianza=baja, preguntar.
