---
_manifest:
  urn: "urn:ops:skill:orquestador-swarm-circuit-breaker-manager:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Monitorear los cuatro modos de fallo definidos en Swarm::Ops §10. Detectar condiciones de fallo. Activar circuit breakers para contener. Alertar al Operador con diagnostico. Gestionar recuperacion.

## Input/Output

- **Input:** system_metrics: {deploy_timeline: DeployResult[], pipeline_queue: QueueStatus, infra_state: InfraState, observer_heartbeat: HeartbeatLog, time_window_min: number}
- **Output:** circuit_status: {breakers: CircuitBreaker[], containment_actions: Action[], operator_alert: AlertPayload, system_health: healthy|degraded|critical}

## Procedimiento

1. **Evaluar Modo 1: Cascada de deploys defectuosos** (Swarm::Ops §10.1):
   - Contar deploys fallidos en ventana temporal (default 15min)
   - IF failures >= threshold (default 3) → ABRIR circuit breaker
   - Accion: pausar deploys, rollback atomico del batch completo
   - Regla: periodo observacion obligatorio entre batches

2. **Evaluar Modo 2: Saturacion pipeline por rafaga** (Swarm::Ops §10.2):
   - Monitorear profundidad cola y tiempo feedback
   - IF cola > umbral critico (default 50) OR feedback_time > 60min → ABRIR circuit breaker
   - Accion: activar backpressure agresiva, pausar generacion PRs
   - Delegar a CM-BACKPRESSURE-CONTROLLER para gestion detallada

3. **Evaluar Modo 3: Drift infraestructura** (Swarm::Ops §10.3):
   - Verificar resultado ultimo terraform plan / drift check
   - IF drift detectado → clasificar: trivial (tags, config menor) vs significativo (recursos, permisos)
   - Accion trivial: reconciliacion automatica
   - Accion significativa: ABRIR circuit breaker, pausar cambios infra, consultar Operador

4. **Evaluar Modo 4: Fallo agente-observer** (Swarm::Ops §10.4):
   - Verificar heartbeat del observer
   - IF heartbeat perdido > timeout (default 5min) → ABRIR circuit breaker
   - Accion: activar alertas clasicas Prometheus como backstop
   - Alerta critica: "El observador ha dejado de observar"

5. **Generar diagnostico para Operador**:
   - Modo de fallo detectado
   - Evidencia (metricas, timestamps, deploys afectados)
   - Acciones de contencion tomadas automaticamente
   - Acciones recomendadas que requieren decision humana

## Signature Output

```yaml
circuit_status:
  breakers:
    - mode: "cascade_deploys"
      state: "open"
      triggered_at: "2026-02-24T10:15:00Z"
      evidence: "3 deploys fallidos en 12 min"
    - mode: "pipeline_saturation"
      state: "closed"
    - mode: "infra_drift"
      state: "closed"
    - mode: "observer_failure"
      state: "closed"
  containment_actions:
    - action: "deploys_paused"
      automated: true
    - action: "batch_rollback"
      automated: true
      reverted_to: "v2.3.0"
  operator_alert:
    severity: "HIGH"
    message: "Circuit breaker activado: cascada deploys defectuosos"
    diagnosis: "PRs #245, #246, #247 deployados en sucesion rapida. 3 fallos en 12min."
    recommended_actions:
      - "Investigar causa raiz de fallos"
      - "Revisar interdependencias entre PRs"
      - "Aumentar periodo observacion entre batches"
  system_health: "degraded"
```
