---
_manifest:
  urn: "urn:dev:skill:sentinel-context-manager:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-CONTEXT-MANAGER

## Proposito
Gestiona contexto multi-turno del sentinel. Verifica diversidad de modelo. Mantiene estado de auditoria entre turnos.

## Procedimiento
1. Comparar tema del mensaje actual vs estado FSM activo.
2. SIEMPRE verificar diversidad de modelo:
   - ¿Que providers usa el enjambre (coder, reviewer)?
   - ¿El sentinel esta usando un provider DIFERENTE a todos?
   - Si mismo provider que cualquier agente del enjambre: ABORTAR.
3. Clasificar: CONTINUA(misma auditoria), NUEVO(nueva auditoria), ATRAS(retoma anterior), TERMINAR(fin), FUERA(fuera de scope).
4. IF CONTINUA → mantener estado, avanzar.
5. IF NUEVO → iniciar auditoria fresca.
6. IF ATRAS → restaurar contexto previo.
7. IF TERMINAR → S-END con resumen.
8. IF FUERA → rejection.

## Output
Clasificacion: {tipo, auditoria_activa?, diversidad_ok: bool, providers_enjambre: string[], provider_sentinel: string}.
