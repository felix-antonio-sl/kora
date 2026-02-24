---
_manifest:
  urn: "urn:ops:skill:orquestador-swarm-system-status:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Generar reporte completo del estado del sistema nervioso del enjambre. Consolidar informacion de todos los flujos: eventos en cola, golden paths activos, agentes ejecutando, backpressure, circuit breakers, heartbeats.

## Input/Output

- **Input:** system_snapshot: {event_queue: Event[], active_paths: GoldenPathExecution[], agent_registry: AgentStatus[], backpressure: BackpressureState, circuit_breakers: CircuitBreakerState[], heartbeats: HeartbeatLog[]}
- **Output:** status_report: {summary: SystemSummary, event_queue: EventQueueReport, golden_paths: GoldenPathReport[], agents: AgentReport[], backpressure: BackpressureReport, circuit_breakers: CircuitBreakerReport[], health: healthy|degraded|critical}

## Procedimiento

1. **Consolidar cola de eventos**:
   - Total eventos pendientes
   - Desglose por tipo (commit, PR, alerta, etc.)
   - Desglose por prioridad
   - Tiempo promedio en cola

2. **Reportar golden paths activos**:
   - Para cada golden path en ejecucion: tipo, paso actual, agente ejecutando, tiempo transcurrido
   - Paths completados en sesion: exitosos vs fallidos
   - Paths en HOLD esperando aprobacion

3. **Reportar estado de agentes**:
   - Para cada agente: estado (idle, executing, queued), tarea actual, tiempo de ejecucion
   - Agentes disponibles vs ocupados
   - Agentes redirigidos por backpressure

4. **Reportar backpressure**:
   - Estado: inactive|active|critical
   - Nivel actual de cola vs umbral
   - Factor de reduccion activo
   - Tiempo estimado de drenaje

5. **Reportar circuit breakers**:
   - Estado de cada uno de los 4 breakers: closed|open|half-open
   - Si abierto: causa, timestamp, acciones de contencion

6. **Reportar heartbeats**:
   - Ultimo heartbeat de cada agente critico
   - Agentes con heartbeat perdido

7. **Calcular salud general**:
   - healthy: todos los breakers cerrados, backpressure inactiva, agentes respondiendo
   - degraded: backpressure activa OR algun breaker abierto OR heartbeat perdido
   - critical: multiples breakers abiertos OR backpressure critica OR agente critico sin heartbeat

## Signature Output

```yaml
status_report:
  summary:
    health: "degraded"
    reason: "Backpressure activa, cola en drenaje"
    timestamp: "2026-02-24T10:30:00Z"
  event_queue:
    total: 12
    by_type: {pr: 8, commit: 2, heartbeat: 2}
    by_priority: {1: 1, 2: 2, 3: 5, 4: 3, 5: 1}
    avg_wait_min: 8
  golden_paths:
    - path: "estandar"
      event: "PR #245"
      step: "3/7 eval_regresion"
      agent: "ops/tester"
      elapsed_min: 12
    - path: "hotfix"
      event: "Alert #89"
      step: "2/5 fix_test"
      agent: "fxsl/coder"
      elapsed_min: 5
  agents:
    active: 4
    idle: 2
    redirected: 1
  backpressure:
    status: "active"
    queue_depth: 28
    threshold: 20
    reduction_factor: 0.5
    estimated_drain_min: 20
  circuit_breakers:
    cascade_deploys: "closed"
    pipeline_saturation: "closed"
    infra_drift: "closed"
    observer_failure: "closed"
  heartbeats:
    all_responding: true
    last_check: "2026-02-24T10:29:00Z"
```
