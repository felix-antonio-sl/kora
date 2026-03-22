---
_manifest:
  urn: urn:gn:skill:goreologo-context-manager:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-CONTEXT-MANAGER

## Proposito
Detectar cambios de contexto, tema o fase en conversacion multi-turno del Goreologo, determinando si la solicitud actual es continuacion de la fase activa o requiere re-dispatch.

## Input/Output
- **Input:** Mensaje actual del usuario + estado FSM activo + tema de turno anterior
- **Output:** {shift_detected: boolean, shift_type: string, action: string}

## Procedimiento
1. Comparar el tema de la solicitud actual contra el estado FSM activo y el tema del turno anterior.
2. Clasificar el resultado:
   - Continuacion: el tema es consistente con la fase activa. No hay shift.
   - Cambio de tema intra-GORE: el tema cambia pero sigue dentro del dominio GOREs. shift_type=TOPIC_CHANGE, action=S-DISPATCHER.
   - Fuera de scope: el tema sale del dominio GOREs. shift_type=OUT_OF_SCOPE, action=rejection_response + S-DISPATCHER.
   - Retroceso: el usuario quiere volver a una fase anterior. shift_type=BACKTRACK, action=S-DISPATCHER.
   - Terminar: el usuario indica cierre. shift_type=TERMINATE, action=S-END.
3. Retornar resultado estructurado.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| shift_detected | boolean | true si se detecto cambio relevante |
| shift_type | CONTINUATION \| TOPIC_CHANGE \| OUT_OF_SCOPE \| BACKTRACK \| TERMINATE | Tipo de cambio detectado |
| action | string | Estado FSM o accion recomendada |
