---
_manifest:
  urn: "urn:ops:agent-bootstrap:deployer-cm-post-deploy-verifier:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Verificar estado post-deploy comparando metricas actuales contra baseline pre-deploy. Determinar si deploy es estable para expansion o si requiere rollback.

## Input/Output

- **Input:** deploy_result: DeployResult, baseline: MetricsBaseline, strategy: StrategyConfig
- **Output:** verification: {status: stable|degraded|critical, metrics_current: MetricsSnapshot, comparison: MetricsDiff, recommendation: expand|hold|rollback}

## Procedimiento

1. **Esperar ventana observacion**:
   - fast-track: 5min
   - canary: 15min por step de expansion
   - Muestreo: cada 30s durante ventana

2. **Recolectar metricas actuales**:
   - Latencia: p50, p95, p99 (ms)
   - Tasa error: 4xx rate, 5xx rate (%)
   - Recursos: CPU (%), memoria (%)
   - Throughput: requests/sec

3. **Comparar contra baseline**:
   - latencia_diff = (current - baseline) / baseline * 100
   - error_diff = current_error_rate - baseline_error_rate
   - resource_diff = (current - baseline) / baseline * 100

4. **Evaluar thresholds**:
   - STABLE: todos los diffs dentro de thresholds
   - DEGRADED: algun diff supera threshold pero < 2x threshold
   - CRITICAL: algun diff supera 2x threshold

5. **Correlacion canary** (si modo canary):
   - Comparar cohorte canary (con flag ON) vs cohorte control (sin flag)
   - IF canary peor que control en cualquier metrica → degraded
   - IF canary similar a control → stable

6. **Recomendar**:
   - stable → expand (siguiente step: 5%→25%→50%→100%)
   - degraded → rollback (automatico, sin esperar aprobacion)
   - critical → rollback + alerta operador

7. **Verificacion final** (al llegar a 100%):
   - Observacion extendida: 30min
   - IF estable → deploy confirmado
   - IF degradado → rollback a version anterior

## Signature Output

```yaml
verification:
  status: "stable"
  observation_window_min: 15
  metrics_current:
    latency_p50_ms: 45
    latency_p95_ms: 128
    latency_p99_ms: 310
    error_rate_4xx: 1.2
    error_rate_5xx: 0.35
    cpu_percent: 47
    memory_percent: 62
  comparison:
    latency_p95_diff_percent: 6.7
    error_rate_5xx_diff: 0.05
    cpu_diff_percent: 4.4
  thresholds_exceeded: []
  canary_correlation:
    canary_cohort_p95_ms: 128
    control_cohort_p95_ms: 122
    delta_percent: 4.9
  recommendation: "expand"
  next_step: "expand to 25%"
```
