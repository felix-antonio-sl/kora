---
_manifest:
  urn: urn:kora:skill:custodio-context-manager:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-CONTEXT-MANAGER

## Proposito
Gestiona el contexto multi-turno del custodio: detecta cambios de tarea, mantiene coherencia entre turnos, evita drift de estado.

## Input/Output
- **Input:** mensaje_actual: string (mensaje del usuario), foco_actual: string | null, contexto_sesion: SessionContext | null
- **Output:** ContextClassification (ver Signature Output)

## Procedimiento
1. Comparar tema del mensaje actual vs foco operativo activo.
2. Clasificar: CONTINUA(mismo tema), NUEVO(tema diferente, requiere re-clasificacion), ATRAS(retoma tarea anterior), TERMINAR(usuario quiere finalizar), FUERA(tema fuera de scope).
3. Si CONTINUA → preservar foco y proceder.
4. Si NUEVO → marcar que la FSM debe volver a despachar.
5. Si ATRAS → restaurar referencia semantica de la tarea anterior si contexto disponible.
6. Si TERMINAR → marcar cierre solicitado.
7. Si FUERA → aplicar regla de rejection del scope sin codificar transiciones.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| accion | enum(CONTINUA\|NUEVO\|ATRAS\|TERMINAR\|FUERA) | Tipo de cambio de contexto |
| requiere_reclasificacion | bool | True si la FSM debe volver a clasificar |
| foco_recomendado | string \| null | Referencia semantica a la tarea previa o recomendada |
| razon | string | Justificacion de la clasificacion |
