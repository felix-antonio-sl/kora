---
_manifest:
  urn: "urn:kora:skill:curator-context-manager:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-CONTEXT-MANAGER

## Proposito
Gestiona el contexto multi-turno del agente: detecta cambios de tema, retornos a fases anteriores, finalizaciones y solicitudes fuera de scope.

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

## Output
Clasificacion de contexto: {accion: CONTINUAR|NUEVO|ATRAS|TERMINAR|FUERA, estado_destino: string?, contexto_preservar: {}?}.
