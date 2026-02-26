---
_manifest:
  urn: "urn:fxsl:skill:reviewer-context-manager:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-CONTEXT-MANAGER

## Proposito
Gestiona contexto multi-turno del reviewer: detecta cambios de tarea, verifica diversidad de modelo, mantiene estado de review entre turnos.

## Procedimiento
1. Comparar tema del mensaje actual vs estado FSM activo.
2. SIEMPRE verificar diversidad de modelo al inicio de cada review:
   - Preguntar o inferir: que modelo/provider uso el coder para este PR?
   - Verificar que el reviewer esta usando un provider DIFERENTE.
   - Si mismo provider: ABORTAR. No hay review valida sin diversidad.
3. Clasificar: CONTINUA(mismo PR, siguiente fase), NUEVO(PR diferente), ATRAS(volver a fase anterior del review actual), TERMINAR(fin), FUERA(fuera de scope).
4. IF CONTINUA → avanzar a siguiente fase del review (REVIEW→SEGURIDAD→EVAL→VEREDICTO).
5. IF NUEVO → iniciar review fresco. Verificar diversidad de nuevo.
6. IF ATRAS → volver a fase anterior con hallazgos previos preservados.
7. IF TERMINAR → S-END con resumen.
8. IF FUERA → rejection.

## Output
Clasificacion: {tipo, pr_activo?, fase_actual?, diversidad_ok: bool, alerta?}.
