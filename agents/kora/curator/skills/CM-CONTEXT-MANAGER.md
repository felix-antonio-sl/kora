---
_manifest:
  urn: urn:kora:skill:curator-context-manager:2.0.0
  type: lazy_load_endofunctor
version: 2.0.0
status: published
lang: es
---

# CM-CONTEXT-MANAGER

## Proposito
Gestiona el contexto multi-turno del agente: detecta cambios de tema, retornos a fases anteriores, finalizaciones y solicitudes fuera de scope.

## Input/Output
- **Input:** mensaje_actual: string (mensaje del usuario), foco_actual: string | null, contexto_sesion: SessionContext | null
- **Output:** ContextClassification (ver Signature Output)

## Procedimiento
1. COMPARAR tema del mensaje actual vs foco de trabajo activo:
   - ¿El tema es coherente con la tarea actual?
   - ¿El usuario esta pidiendo algo nuevo?
   - ¿El usuario quiere volver a una fase anterior?
   - ¿El usuario quiere terminar?
   - ¿El tema esta fuera del scope de curator?
2. CLASIFICAR cambio:
   - CONTINUAR: tema coherente con el foco actual.
   - NUEVO: tema requiere re-clasificacion por la FSM.
   - ATRAS: usuario quiere retomar una fase previa.
   - TERMINAR: usuario indica fin.
   - FUERA: tema fuera scope.
3. PRESERVAR contexto relevante para la FSM:
   - Si cambio dentro del ciclo guiado: mantener estado acumulado.
   - Si cambio radical: limpiar contexto y pedir re-clasificacion.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| accion | enum(CONTINUAR\|NUEVO\|ATRAS\|TERMINAR\|FUERA) | Tipo de cambio de contexto |
| requiere_reclasificacion | bool | True si la FSM debe volver a despachar |
| fase_sugerida | string \| null | Etiqueta semantica de la fase previa si el usuario quiere retomar |
| contexto_preservar | object \| null | Datos a mantener al transicionar |
