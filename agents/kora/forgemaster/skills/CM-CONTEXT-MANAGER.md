---
_manifest:
  urn: urn:kora:skill:forgemaster-context-manager:2.0.0
  type: lazy_load_endofunctor
version: 2.0.0
status: published
lang: es
---

# CM-CONTEXT-MANAGER

## Proposito
Detecta cambios de contexto entre turnos comparando el tema del mensaje entrante con el foco de trabajo actual y emitiendo una decision semantica de continuidad.

## Input/Output
- **Input:** mensaje: string (mensaje entrante), foco_actual: string | null, tema_previo: string | null
- **Output:** ContextDecision (ver Signature Output)

## Procedimiento
1. Capturar foco de trabajo actual y tema del ultimo turno desde contexto de sesion.
2. Analizar mensaje entrante: identificar tema principal, intencion, agentes referenciados.
3. Comparar tema entrante vs foco actual: coherente(mismo hilo), nuevo(tema diferente), atras(retomar fase anterior), terminar(finalizar sesion), fuera_de_scope(ajeno a ciclo de vida agentes).
4. Clasificar tipo de cambio:
   - coherente → continuar sin interrupcion.
   - nuevo → marcar requiere_reclasificacion.
   - atras → recuperar fase recordada y marcar requiere_reclasificacion.
   - terminar → marcar cierre solicitado.
   - fuera_de_scope → aplicar Guard Set (REJECT_OUT_OF_SCOPE).
5. Si cambio radical(tema completamente distinto) → marcar requiere_reclasificacion.
6. Actualizar contexto de sesion con foco nuevo y tema actual.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| tipo_cambio | enum(coherente\|nuevo\|atras\|terminar\|fuera_de_scope) | Tipo de cambio detectado |
| accion | string | Accion semantica a tomar (continuar, reclasificar, cerrar_sesion, reject) |
| requiere_reclasificacion | bool | True si la FSM debe volver a despachar |
| fase_recordada | string\|null | Etiqueta semantica de la fase previa si aplica |
| mensaje_usuario | string\|null | Mensaje al usuario si aplica |
