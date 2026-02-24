---
_manifest:
  urn: "urn:kora:skill:forgemaster-intent-classifier:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-INTENT-CLASSIFIER

## Proposito
Clasifica la intencion del usuario al inicio de cada turno en la FSM WF-FORGEMASTER, determinando la capacidad requerida y el modo de operacion (guiado/libre).

## Procedimiento
1. Analizar mensaje: palabras clave, contexto previo, agentes mencionados, artefactos referenciados.
2. Clasificar capacidad: DESIGN(disenar nuevo), CREATE(scaffold workspace), IMPLEMENT(rellenar componentes), VALIDATE(verificar conformidad), OPERATE(diagnosticar/reparar/mantener), IMPROVE(optimizar/expandir), DEPRECATE(retirar), GUIDED(ciclo completo), END(finalizar).
3. Determinar modo: GUIADO(usuario quiere ciclo completo paso a paso), LIBRE(usuario quiere capacidad especifica directa).
4. Si hay progreso previo, identificar fase actual del ciclo.
5. Emitir clasificacion: {capacidad, modo, fase_actual, confianza}.

## Output
Clasificacion con campos: `capacidad` (enum), `modo` (GUIADO|LIBRE), `fase_actual` (enum|null), `confianza` (alta|media|baja). Si confianza=baja, formular pregunta aclaratoria antes de transicionar.
