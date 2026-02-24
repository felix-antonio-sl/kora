---
_manifest:
  urn: "urn:fxsl:skill:coder-intent-classifier:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-INTENT-CLASSIFIER

## Proposito
Clasifica la intencion del usuario en la FSM WF-CODER, determinando la capacidad de implementacion requerida.

## Procedimiento
1. Analizar mensaje: palabras clave, artefactos mencionados (historias, PRs, bugs, codigo), contexto previo.
2. Clasificar capacidad: PLANIFICAR(historia nueva, consumir, descomponer), IMPLEMENTAR(codear, TDD, escribir), INTEGRAR(PR, commit, lint), REFACTORIZAR(limpiar, deuda, verde, duplicacion), DEPURAR(bug, fallo, error, test rojo), END(terminar).
3. Si el mensaje contiene una historia con ACs → PLANIFICAR.
4. Si el mensaje describe un bug o test fallando → DEPURAR.
5. Si el mensaje pide mejora de codigo existente sin historia nueva → REFACTORIZAR.
6. Emitir clasificacion: {capacidad, confianza}.

## Output
Clasificacion: `capacidad` (enum), `confianza` (alta|media|baja). Si confianza=baja, preguntar.
