---
_manifest:
  urn: "urn:ops:agent-bootstrap:deployer-cm-strategy-selector:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Seleccionar la estrategia de deploy optima basada en la clasificacion de riesgo. Configurar feature flags y parametros de observacion segun el modo seleccionado.

## Input/Output

- **Input:** classification: {risk: lectura|escritura|destructiva, affected_systems: string[]}, environment: string
- **Output:** strategy: {mode: fast-track|canary|manual, flag_config: FlagConfig, observation: ObservationConfig, rollback_plan: RollbackPlan}

## Procedimiento

1. **Mapear riesgo a modo**:
   - lectura → fast-track: deploy inmediato, flag ON 100%, observacion 5min
   - escritura → canary: flag ON 5%, observacion 15min, expansion gradual (5%→25%→50%→100%)
   - destructiva → manual: flag OFF, HOLD hasta aprobacion humana explicita

2. **Configurar feature flag**:
   - Nombre: ff-{pr_id}-{short_description}
   - Estado inicial: segun modo (ON 100% | ON 5% | OFF)
   - Scope: affected_systems
   - TTL: 72h (auto-cleanup si no se confirma)

3. **Definir plan observacion**:
   - fast-track: 5min, metricas basicas (latencia, errores)
   - canary: 15min por step, metricas completas (latencia p50/p95/p99, errores 4xx/5xx, CPU, memoria)
   - manual: sin observacion automatica hasta aprobacion

4. **Definir plan rollback** (obligatorio antes de proceder):
   - Accion: desactivar flag → revert version → verificar baseline
   - Trigger automatico: IF metricas degradadas segun thresholds
   - Trigger manual: operador puede forzar rollback en cualquier momento
   - Batch: rollback atomico del batch completo si batch deploy

5. **Validar**: rollback plan DEBE existir antes de retornar estrategia. Sin rollback plan → no hay estrategia valida.

## Signature Output

```yaml
strategy:
  mode: "canary"
  flag_config:
    name: "ff-142-api-orders"
    initial_state: "on"
    initial_percentage: 5
    expansion_steps: [25, 50, 100]
    scope: ["api-gateway", "orders-service"]
    ttl_hours: 72
  observation:
    window_min: 15
    metrics: ["latency_p50", "latency_p95", "latency_p99", "error_4xx", "error_5xx", "cpu", "memory"]
    thresholds:
      latency_increase_percent: 20
      error_rate_increase_percent: 1
  rollback_plan:
    trigger: "auto_on_degradation"
    steps: ["deactivate_flag", "revert_version", "verify_baseline"]
    batch_atomic: true
```
