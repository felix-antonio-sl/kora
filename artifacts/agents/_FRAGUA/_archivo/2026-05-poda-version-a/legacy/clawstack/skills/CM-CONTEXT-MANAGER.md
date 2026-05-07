---
_manifest:
  urn: urn:ops:skill:clawstack-context-manager:1.0.0
  type: lazy_load_endofunctor
---

# CM-CONTEXT-MANAGER

## Proposito
Detecta cambios de contexto durante la conversacion multi-turno, preservando la informacion necesaria para redirigir una solicitud legacy a `kora/clawforge`.

## Input/Output
- **Input:** mensaje_actual: string, estado_fsm: string, foco_previo: string | null
- **Output:** ContextClassification (ver Signature Output)

## Procedimiento
1. Comparar tema del mensaje actual con el foco previo y estado FSM activo.
2. Clasificar:
   - **continuar**: sigue la misma redireccion pendiente.
   - **nuevo**: cambia la solicitud legacy que debe migrarse.
   - **terminar**: indica cierre.
   - **fuera**: tema no relacionado con la compatibilidad OpenClaw.
3. Preservar entre turnos solo lo necesario para la redireccion:
   - solicitud_legacy
   - capacidad_inferida
   - artefactos o rutas mencionadas
   - target_recomendado=`kora/clawforge`
4. Emitir clasificacion con shift y detalle para consumo de la FSM.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| shift | enum | continuar, nuevo, terminar, fuera |
| detalle | string | Explicacion del cambio detectado |
| estado_preservado | object | Contexto minimo para la redireccion |
