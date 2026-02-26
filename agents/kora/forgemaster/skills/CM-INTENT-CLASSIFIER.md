---
_manifest:
  urn: "urn:kora:skill:forgemaster-intent-classifier:2.0.0"
  type: "lazy_load_endofunctor"
version: "2.0.0"
status: published
lang: es
---
# CM-INTENT-CLASSIFIER

## Proposito
Clasifica la intencion del usuario al inicio de cada turno en la FSM WF-FORGEMASTER, determinando la capacidad requerida y el modo de operacion (guiado/libre).

## I/O

- **Input:** mensaje: string (mensaje del usuario), estado_actual: FSMState (estado FSM vigente), contexto_previo: SessionContext | null
- **Output:** IntentClassification (ver Signature Output)

## Procedimiento
1. Analizar mensaje: palabras clave, contexto previo, agentes mencionados, artefactos referenciados.
2. Clasificar capacidad: DESIGN(disenar nuevo), CREATE(scaffold workspace), IMPLEMENT(rellenar componentes), VALIDATE(verificar conformidad), OPERATE(diagnosticar/reparar/mantener), IMPROVE(optimizar/expandir), DEPRECATE(retirar), GUIDED(ciclo completo), END(finalizar).
3. Determinar modo: GUIADO(usuario quiere ciclo completo paso a paso), LIBRE(usuario quiere capacidad especifica directa).
4. Si hay progreso previo, identificar fase actual del ciclo.
5. Emitir clasificacion: {capacidad, modo, fase_actual, confianza}.

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| capacidad | enum(DESIGN\|CREATE\|IMPLEMENT\|VALIDATE\|OPERATE\|IMPROVE\|DEPRECATE\|GUIDED\|END) | Capacidad clasificada |
| modo | enum(GUIADO\|LIBRE) | Modo de operacion |
| fase_actual | enum\|null | Fase del ciclo si hay progreso previo |
| confianza | enum(alta\|media\|baja) | Nivel de confianza. Si baja, formular pregunta aclaratoria |
