---
_manifest:
  urn: "urn:kora:skill:smith-context-manager:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-CONTEXT-MANAGER

## Proposito
Detecta cambios de contexto entre turnos comparando el tema del mensaje entrante con el estado FSM actual, activando CONTEXT_SHIFT cuando corresponde.

## Procedimiento
1. Capturar estado FSM actual y tema del ultimo turno desde contexto de sesion.
2. Analizar mensaje entrante: identificar tema principal, intencion, artefactos referenciados.
3. Comparar tema entrante vs estado actual: coherente (mismo hilo), nuevo (tema diferente), atras (retomar fase anterior), terminar (finalizar sesion), fuera_de_scope (ajeno a construccion agentes).
4. Clasificar tipo de cambio:
   - coherente → continuar en estado actual sin interrupcion.
   - nuevo → emitir CONTEXT_SHIFT, proponer transicion a estado apropiado.
   - atras → emitir CONTEXT_SHIFT con memoria de fase anterior.
   - terminar → transicionar a S-END.
   - fuera_de_scope → aplicar Guard Set (REJECT_OUT_OF_SCOPE).
5. Si cambio radical (tema completamente distinto) → S-DISPATCHER para reclasificacion.
6. Actualizar contexto de sesion con estado nuevo y tema actual.

## Output
Decision de continuidad: {tipo_cambio, accion, estado_destino, mensaje_usuario_si_aplica}. Si CONTEXT_SHIFT → notificar al usuario de forma transparente antes de transicionar.
