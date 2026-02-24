---
_manifest:
  urn: "urn:ops:agent-bootstrap:deployer-cm-rollback-executor:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Ejecutar rollback atomico cuando verificacion post-deploy detecta degradacion. Revertir a version anterior, desactivar feature flag, verificar normalizacion de metricas, alertar operador con diagnostico.

## Input/Output

- **Input:** deploy_result: DeployResult, verification: VerificationResult, rollback_plan: RollbackPlan
- **Output:** rollback_result: {status: success|failed, reverted_to: string, flag_deactivated: boolean, metrics_normalized: boolean, diagnosis: Diagnosis, actions_log: ActionLog[]}

## Procedimiento

1. **Desactivar feature flag** (inmediato):
   - Flag → OFF (0% trafico)
   - Log: FLAG_DEACTIVATED
   - Esto detiene impacto inmediatamente
   - IF flag desactivacion falla → ALERTA CRITICA operador

2. **Revert version**:
   - Identificar version anterior (de deploy_result)
   - Apply version anterior a environment
   - Log: REVERT_START, REVERT_SUCCESS|REVERT_FAILED
   - IF revert falla → ALERTA CRITICA operador + escalamiento

3. **Verificar normalizacion**:
   - Esperar 2min post-rollback
   - Comparar metricas actuales vs baseline original
   - Metricas DEBEN volver a rango baseline (+/- 5%)
   - IF no normalizan en 5min → ALERTA CRITICA

4. **Rollback batch** (si deploy fue batch):
   - Rollback atomico: revertir TODO el batch, no parcial
   - Secuencia inversa: ultimo deploy primero
   - Verificar normalizacion despues de cada reversion
   - Log cada paso del batch rollback

5. **Construir diagnostico**:
   - Que fallo: metricas que superaron thresholds
   - Cuando fallo: timestamp de deteccion
   - Impacto: porcentaje trafico afectado, duracion
   - Causa probable: correlacion con cambios deployados
   - Accion tomada: rollback steps ejecutados
   - Estado actual: metricas post-rollback

6. **Alertar operador**:
   - Enviar diagnostico completo
   - Incluir: version revertida, version actual, metricas pre/post
   - Recomendar: investigar causa raiz antes de re-deploy

## Signature Output

```yaml
rollback_result:
  status: "success"
  reverted_to: "2.3.1"
  flag_deactivated: true
  metrics_normalized: true
  normalization_time_sec: 90
  actions_log:
    - action: "FLAG_DEACTIVATED"
      status: "success"
      timestamp: "2026-02-24T10:20:00Z"
    - action: "REVERT"
      from: "2.4.0-abc123"
      to: "2.3.1"
      status: "success"
      timestamp: "2026-02-24T10:20:30Z"
    - action: "METRICS_VERIFIED"
      status: "normalized"
      timestamp: "2026-02-24T10:22:00Z"
  diagnosis:
    trigger: "latency_p95 exceeded threshold"
    detected_at: "2026-02-24T10:17:05Z"
    impacted_traffic_percent: 5
    impact_duration_sec: 180
    probable_cause: "New endpoint /api/v2/orders causing DB connection pool exhaustion"
    metrics_at_detection:
      latency_p95_ms: 340
      baseline_p95_ms: 120
      delta_percent: 183
    recommendation: "Investigate DB connection pooling before re-deploy"
```
