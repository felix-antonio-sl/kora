---
_manifest:
  urn: "urn:kora:skill:custodio-context-manager:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-CONTEXT-MANAGER

## Proposito
Gestiona el contexto multi-turno del custodio: detecta cambios de tarea, mantiene coherencia entre turnos, evita drift de estado.

## Procedimiento
1. Comparar tema del mensaje actual vs estado FSM activo.
2. Clasificar: CONTINUA(mismo tema, mismo estado), NUEVO(tema diferente, requiere otro estado), ATRAS(retoma tema anterior), TERMINAR(usuario quiere finalizar), FUERA(tema fuera de scope).
3. IF CONTINUA → mantener estado, proceder.
4. IF NUEVO → transicionar a S-DISPATCHER para reclasificar.
5. IF ATRAS → restaurar estado anterior si contexto disponible.
6. IF TERMINAR → transicionar a S-END.
7. IF FUERA → aplicar regla de rejection del scope.

## Output
Clasificacion de contexto: {tipo, estado_actual, estado_destino, razon}.
