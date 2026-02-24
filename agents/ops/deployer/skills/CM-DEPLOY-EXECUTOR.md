---
_manifest:
  urn: "urn:ops:agent-bootstrap:deployer-cm-deploy-executor:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Ejecutar el deploy segun la estrategia seleccionada. Orquestar: build, push, apply, activacion de feature flag. Registrar cada accion para auditoria y rollback.

## Input/Output

- **Input:** strategy: StrategyConfig, changeset: Changeset, environment: string
- **Output:** deploy_result: {status: success|failed, version: string, environment: string, flag_status: FlagStatus, actions_log: ActionLog[], timestamp: ISO8601, baseline_snapshot: MetricsBaseline}

## Procedimiento

1. **Pre-flight checks**:
   - Verificar DoD completo (9/9 pasos)
   - Verificar feature flag creado
   - Verificar rollback plan definido
   - Capturar baseline metricas pre-deploy
   - IF cualquier check falla → ABORT con razon

2. **Build**:
   - Construir imagen/artefacto desde changeset
   - Tag: {version}-{commit_short}-{timestamp}
   - Log: BUILD_START, BUILD_SUCCESS|BUILD_FAILED
   - IF build falla → ABORT, retornar status: failed

3. **Push**:
   - Push artefacto a registry/repositorio
   - Verificar integridad (checksum)
   - Log: PUSH_START, PUSH_SUCCESS|PUSH_FAILED
   - IF push falla → ABORT, retornar status: failed

4. **Apply**:
   - Aplicar a environment target
   - Segun modo:
     - fast-track: apply directo, flag ON 100%
     - canary: apply con routing, flag ON 5%
     - manual: apply staging, flag OFF (espera aprobacion)
   - Log: APPLY_START, APPLY_SUCCESS|APPLY_FAILED

5. **Activar feature flag**:
   - Segun estrategia: ON 100% | ON 5% | OFF
   - Registrar estado flag
   - Log: FLAG_ACTIVATED, porcentaje

6. **Batching** (si aplica):
   - IF multiples changesets en ventana → agrupar
   - Deploy secuencial con periodo observacion entre cada uno
   - Correlacion: cada batch con su propio flag
   - IF fallo en batch N → rollback atomico batches N..1

7. **Registrar** actions_log completo para auditoria y rollback.

## Signature Output

```yaml
deploy_result:
  status: "success"
  version: "2.4.0-abc123-20260224"
  environment: "production"
  flag_status:
    name: "ff-142-api-orders"
    state: "on"
    percentage: 5
  actions_log:
    - action: "BUILD"
      status: "success"
      timestamp: "2026-02-24T10:00:00Z"
    - action: "PUSH"
      status: "success"
      timestamp: "2026-02-24T10:01:30Z"
    - action: "APPLY"
      status: "success"
      timestamp: "2026-02-24T10:02:00Z"
    - action: "FLAG_ACTIVATED"
      status: "success"
      percentage: 5
      timestamp: "2026-02-24T10:02:05Z"
  baseline_snapshot:
    latency_p95_ms: 120
    error_rate_5xx: 0.3
    cpu_percent: 45
  timestamp: "2026-02-24T10:02:05Z"
```
