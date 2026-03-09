---
_manifest:
  urn: urn:dev:skill:analyst-context-manager:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-CONTEXT-MANAGER

## Proposito
Gestiona el contexto multi-turno del analyst: detecta cambios de tarea, mantiene coherencia entre turnos y preserva el contexto semantico util.

## Input/Output
- **Input:** foco_actual: string | null, mensaje_usuario: string
- **Output:** ContextDecision (ver Signature Output)

## Procedimiento
1. Comparar tema del mensaje actual vs foco de trabajo activo.
2. Detectar granularidad: snapshot(un dato puntual) vs drill-down(profundizar metrica actual) vs pivot(cambiar dimension/metrica).
3. Clasificar: CONTINUA(mismo tema), NUEVO(tema diferente), ATRAS(retoma anterior), TERMINAR(fin), FUERA(fuera de scope).
4. Si CONTINUA: preservar Ciclo y metricas relevantes en contexto.
5. Si NUEVO: marcar que el foco actual requiere reinterpretacion.
6. Si ATRAS: restaurar contexto anterior (Ciclo, metricas, dimension) si existe.
7. Si TERMINAR: marcar cierre solicitado.
8. Si FUERA: aplicar regla de rejection.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| clasificacion | enum(CONTINUA\|NUEVO\|ATRAS\|TERMINAR\|FUERA) | Tipo de cambio de contexto |
| requiere_revision_de_foco | bool | True si el foco actual debe reinterpretarse |
| ciclo_en_contexto | string \| null | Referencia semantica al Ciclo en curso |
| metricas_preservadas | string[] | Metricas que conviene mantener en contexto |
