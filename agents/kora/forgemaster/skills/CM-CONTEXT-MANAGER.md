---
_manifest:
  urn: "urn:kora:skill:forgemaster-context-manager:2.0.0"
  type: "lazy_load_endofunctor"
version: "2.0.0"
status: published
lang: es
---
# CM-CONTEXT-MANAGER

## Proposito
Detecta cambios de contexto entre turnos comparando el tema del mensaje entrante con el estado FSM actual, activando CONTEXT_SHIFT cuando corresponde.

## I/O

- **Input:** mensaje: string (mensaje entrante), estado_actual: FSMState, tema_previo: string | null
- **Output:** ContextDecision (ver Signature Output)

## Procedimiento
1. Capturar estado FSM actual y tema del ultimo turno desde contexto de sesion.
2. Analizar mensaje entrante: identificar tema principal, intencion, agentes referenciados.
3. Comparar tema entrante vs estado actual: coherente(mismo hilo), nuevo(tema diferente), atras(retomar fase anterior), terminar(finalizar sesion), fuera_de_scope(ajeno a ciclo de vida agentes).
4. Clasificar tipo de cambio:
   - coherente → continuar en estado actual sin interrupcion.
   - nuevo → emitir CONTEXT_SHIFT, proponer transicion a estado apropiado.
   - atras → emitir CONTEXT_SHIFT con memoria de fase anterior.
   - terminar → transicionar a S-END.
   - fuera_de_scope → aplicar Guard Set (REJECT_OUT_OF_SCOPE).
5. Si cambio radical(tema completamente distinto) → S-DISPATCHER para reclasificacion.
6. Actualizar contexto de sesion con estado nuevo y tema actual.

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| tipo_cambio | enum(coherente\|nuevo\|atras\|terminar\|fuera_de_scope) | Tipo de cambio detectado |
| accion | string | Accion a tomar (continuar, CONTEXT_SHIFT, S-END, REJECT) |
| estado_destino | FSMState\|null | Estado FSM destino si hay transicion |
| mensaje_usuario | string\|null | Mensaje al usuario si aplica |
