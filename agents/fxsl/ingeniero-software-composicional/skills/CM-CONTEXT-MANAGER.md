---
_manifest:
  urn: "urn:fxsl:skill:ingeniero-software-composicional-context-manager:2.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Detectar cambios de contexto en la conversacion multi-turno y gestionar transiciones de estado.

## I/O

- **Input:** Mensaje del usuario, estado FSM actual, pipeline categorico en curso
- **Output:** Clasificacion de cambio de contexto y accion recomendada

## Procedimiento

1. Comparar tema del mensaje vs estado FSM actual
2. Clasificar: nuevo tema, cambio de proyecto, solicitud de cierre, informacion contradictoria
3. Mantener pipeline categorico: D->R->S->API->Code en curso
4. Detectar si el cambio es lateral (mismo pipeline) o radical (nuevo pipeline)
5. Emitir accion: continuar, cambiar estado, o redirigir a S-DISPATCHER

## Signature Output

Clasificacion: {tipo_cambio, estado_actual, accion_recomendada, pipeline_status}.
