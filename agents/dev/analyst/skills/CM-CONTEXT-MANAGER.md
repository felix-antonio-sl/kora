---
_manifest:
  urn: "urn:dev:skill:analyst-context-manager:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-CONTEXT-MANAGER

## Proposito
Gestiona el contexto multi-turno del analyst: detecta cambios de tarea, mantiene coherencia entre turnos, preserva el Ciclo y metricas en contexto.

## Procedimiento
1. Comparar tema del mensaje actual vs estado FSM activo.
2. Detectar granularidad: snapshot(un dato puntual) vs drill-down(profundizar metrica actual) vs pivot(cambiar dimension/metrica).
3. Clasificar: CONTINUA(mismo tema, mismo estado), NUEVO(tema diferente), ATRAS(retoma anterior), TERMINAR(fin), FUERA(fuera de scope).
4. IF CONTINUA → mantener estado, proceder. Preservar Ciclo y metricas en contexto.
5. IF NUEVO → transicionar a S-DISPATCHER.
6. IF ATRAS → restaurar contexto anterior (Ciclo, metricas, dimension).
7. IF TERMINAR → transicionar a S-END.
8. IF FUERA → aplicar regla de rejection.

## Output
Clasificacion: {tipo, estado_actual, estado_destino, ciclo_en_contexto, metricas_preservadas}.
