---
_manifest:
  urn: "urn:kora:skill:curator-context-manager:2.0.0"
  type: "lazy_load_endofunctor"
version: "2.0.0"
status: published
lang: es
---
# CM-CONTEXT-MANAGER

## Proposito
Gestiona el contexto multi-turno del agente: detecta cambios de tema, retornos a fases anteriores, finalizaciones y solicitudes fuera de scope.

## I/O

- **Input:** mensaje_actual: string (mensaje del usuario), estado_fsm: FSMState (estado FSM activo), contexto_sesion: SessionContext | null
- **Output:** ContextClassification (ver Signature Output)

## Procedimiento
1. COMPARAR tema del mensaje actual vs estado FSM activo:
   - ¿El tema es coherente con el estado actual?
   - ¿El usuario esta pidiendo algo nuevo?
   - ¿El usuario quiere volver a una fase anterior?
   - ¿El usuario quiere terminar?
   - ¿El tema esta fuera del scope de curator?
2. CLASIFICAR cambio:
   - CONTINUAR: tema coherente con estado actual → seguir en estado.
   - NUEVO: tema requiere capacidad diferente → CONTEXT_SHIFT → S-DISPATCHER.
   - ATRAS: usuario quiere volver a fase anterior → transicionar a fase.
   - TERMINAR: usuario indica fin → S-END.
   - FUERA: tema fuera scope → aplicar rejection_response, mantener estado.
3. PRESERVAR contexto relevante al transicionar:
   - Si cambio dentro del ciclo guiado: mantener estado acumulado.
   - Si cambio radical: limpiar contexto, re-clasificar desde S-DISPATCHER.

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| accion | enum(CONTINUAR\|NUEVO\|ATRAS\|TERMINAR\|FUERA) | Tipo de cambio de contexto |
| estado_destino | string \| null | Estado FSM destino (si aplica transicion) |
| contexto_preservar | object \| null | Datos a mantener al transicionar |
