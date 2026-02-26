---
_manifest:
  urn: "urn:kora:skill:curator-intent-classifier:2.0.0"
  type: "lazy_load_endofunctor"
version: "2.0.0"
status: published
lang: es
---
# CM-INTENT-CLASSIFIER

## Proposito
Clasifica la intencion del usuario al inicio de cada turno en la FSM WF-CURATOR, determinando la capacidad requerida, el tipo de artefacto y el modo de operacion.

## I/O

- **Input:** mensaje: string (mensaje del usuario), estado_actual: FSMState (estado FSM vigente), contexto_previo: SessionContext | null
- **Output:** IntentClassification (ver Signature Output)

## Procedimiento
1. Analizar mensaje: palabras clave, contexto previo, artefactos mencionados, documentos referenciados.
2. Clasificar capacidad: DESIGN(planificar nuevo), KORAFICATE(transformar doc humano a KORA/MD), CRYSTALLIZE(formalizar decisiones a KORA/Spec-MD), AUDIT(validar conformidad), EDIT(modificar existente), REPAIR(diagnosticar/corregir), IMPROVE(optimizar), DEPRECATE(retirar), GUIDED(ciclo completo), END(finalizar).
3. Determinar tipo artefacto: descriptivo(KORA/MD — hechos, datos, procedimientos), prescriptivo(KORA/Spec-MD — reglas, specs, protocolos), ambiguo(necesita clarificacion).
4. Determinar modo: GUIADO(usuario quiere ciclo completo paso a paso), LIBRE(usuario quiere capacidad especifica directa).
5. Si hay progreso previo, identificar fase actual del ciclo.
6. Emitir clasificacion: {capacidad, tipo_artefacto, modo, fase_actual, confianza}.

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| capacidad | enum(DESIGN\|KORAFICATE\|CRYSTALLIZE\|AUDIT\|EDIT\|REPAIR\|IMPROVE\|DEPRECATE\|GUIDED\|END) | Capacidad clasificada |
| tipo_artefacto | enum(descriptivo\|prescriptivo\|ambiguo) | Tipo de artefacto detectado |
| modo | enum(GUIADO\|LIBRE) | Modo de operacion |
| fase_actual | enum\|null | Fase del ciclo si hay progreso previo |
| confianza | enum(alta\|media\|baja) | Nivel de confianza. Si baja, formular pregunta aclaratoria |
