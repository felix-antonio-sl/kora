---
_manifest:
  urn: "urn:fxsl:skill:planner-context-manager:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-CONTEXT-MANAGER

## Proposito
Gestiona el contexto multi-turno del planner: detecta cambios de tarea, detecta mezcla de sombreros PO/Operador, mantiene coherencia entre turnos.

## Procedimiento
1. Comparar tema del mensaje actual vs estado FSM activo.
2. Detectar sombrero: PO(definiendo valor, priorizando, aceptando) vs Operador(configurando, optimizando, infraestructura).
3. Si detecta mezcla de sombreros: alertar. "Estas mezclando sombreros. Cuando llevas el sombrero PO, prioriza por valor de negocio sin dejarte seducir por la elegancia tecnica."
4. Clasificar: CONTINUA(mismo tema, mismo estado), NUEVO(tema diferente), ATRAS(retoma anterior), TERMINAR(fin), FUERA(fuera de scope).
5. IF CONTINUA → mantener estado, proceder.
6. IF NUEVO → transicionar a S-DISPATCHER.
7. IF ATRAS → restaurar contexto anterior.
8. IF TERMINAR → transicionar a S-END.
9. IF FUERA → aplicar regla de rejection.

## Output
Clasificacion: {tipo, sombrero_detectado, estado_actual, estado_destino, alerta_sombrero?}.
