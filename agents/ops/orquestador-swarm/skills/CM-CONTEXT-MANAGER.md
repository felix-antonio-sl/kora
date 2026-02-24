---
_manifest:
  urn: "urn:ops:skill:orquestador-swarm-context-manager:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Gestionar contexto multi-turno de la sesion de orquestacion. Mantener estado acumulado (eventos procesados, golden paths ejecutados, backpressure, circuit breakers) y generar resumen de sesion en nodo terminal.

## Input/Output

- **Input:** session_history: {turns: Turn[], events_processed: EventClassification[], golden_paths_executed: GoldenPathExecution[], backpressure_activations: BackpressureAction[], circuit_breakers_triggered: CircuitBreakerEvent[], agent_dispatches: AgentDispatch[]}
- **Output:** session_summary: {events_total: number, events_by_type: TypeCount, golden_paths_completed: number, golden_paths_failed: number, backpressure_activations: number, circuit_breakers_triggered: number, agents_dispatched: number, timeline: TimelineEntry[], final_health: string, recommendations: string[]}

## Procedimiento

1. **Agregar eventos procesados**:
   - Contar eventos por tipo (commit, PR, alerta, config_change, etc.)
   - Contar eventos por riesgo (lectura, escritura, destructiva)
   - Contar eventos por golden path asignado

2. **Agregar golden paths**:
   - Paths completados exitosamente
   - Paths fallidos (y causa del fallo)
   - Paths en HOLD al cierre de sesion
   - Tiempo promedio de ejecucion por tipo de path

3. **Agregar backpressure**:
   - Numero de activaciones durante sesion
   - Duracion total en estado backpressure
   - PRs diferidos por backpressure
   - Agentes redirigidos y tareas alternativas ejecutadas

4. **Agregar circuit breakers**:
   - Breakers disparados durante sesion
   - Para cada disparo: modo, causa, duracion, acciones de contencion
   - Breakers resueltos vs abiertos al cierre

5. **Compilar timeline**:
   - Secuencia cronologica de acciones significativas
   - Timestamps por cada evento, despacho, activacion
   - Puntos de intervencion humana (HOLD, vetos)

6. **Detectar patrones y recomendar**:
   - IF backpressure frecuente → recomendar aumentar capacidad verificacion
   - IF circuit breaker cascada recurrente → recomendar aumentar periodo observacion entre batches
   - IF golden paths fallidos > 30% → recomendar revision de pipeline de verificacion
   - IF agente especifico frecuentemente despachado → analizar si requiere refuerzo

## Signature Output

```yaml
session_summary:
  events_total: 15
  events_by_type: {pr: 8, commit: 3, alert: 2, heartbeat: 2}
  events_by_risk: {lectura: 5, escritura: 7, destructiva: 1}
  golden_paths_completed: 6
  golden_paths_failed: 1
  golden_paths_hold: 1
  backpressure_activations: 1
  backpressure_duration_min: 35
  circuit_breakers_triggered: 0
  agents_dispatched: 23
  timeline:
    - timestamp: "2026-02-24T10:00:00Z"
      action: "EVENT_CLASSIFIED"
      detail: "PR #245 → escritura → estandar"
    - timestamp: "2026-02-24T10:01:00Z"
      action: "AGENT_DISPATCHED"
      detail: "ops/integrador → merge_check PR #245"
    - timestamp: "2026-02-24T10:15:00Z"
      action: "BACKPRESSURE_ACTIVATED"
      detail: "Cola: 28/20. Reduccion: 50%"
    - timestamp: "2026-02-24T10:50:00Z"
      action: "BACKPRESSURE_RESOLVED"
      detail: "Cola: 12/20. Tasa restaurada"
  final_health: "healthy"
  recommendations:
    - "Considerar aumentar capacidad de verificacion: backpressure activada 1 vez en sesion"
    - "PR #246 fallo en eval_regresion: investigar causa raiz antes de retry"
```
