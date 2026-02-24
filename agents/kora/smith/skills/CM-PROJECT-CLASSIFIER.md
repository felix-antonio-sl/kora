---
_manifest:
  urn: "urn:kora:skill:smith-project-classifier:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-PROJECT-CLASSIFIER

## Proposito
Clasifica la intencion del usuario al inicio de cada turno en la FSM WF-SMITH, determinando la tarea (NEW_AGENT|VALIDATE|ITERATE|CONSULT|END) y el modo de conocimiento requerido.

## Procedimiento
1. Analizar el mensaje del usuario: palabras clave, contexto previo, artefactos mencionados.
2. Clasificar tarea principal: NEW_AGENT (construir desde cero), VALIDATE (verificar agent.yaml existente), ITERATE (modificar agente en progreso), CONSULT (pregunta KORA/agente), END (finalizar sesion).
3. Si hay progreso previo en sesion, identificar fase actual (REQUIREMENTS|ARCHITECTURE|CONSTRUCTION|VALIDATION|DEPLOYMENT).
4. Determinar Knowledge Mode requerido: KB_BASED (artefactos curados), LLM_NATIVE (razonamiento puro), WEB_AUGMENTED (busqueda web), HYBRID_WEB_KB (KB + web).
5. Emitir clasificacion estructurada: {tarea, fase_actual, kb_mode, confianza}.

## Output
Clasificacion con campos: `tarea` (enum), `fase_actual` (enum|null), `kb_mode` (enum), `confianza` (alta|media|baja). Si confianza=baja, formular pregunta aclaratoria antes de transicionar.
