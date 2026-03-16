---
_manifest:
  urn: "urn:ops:agent-bootstrap:deployer-tools:1.0.0"
  type: "bootstrap_tools"
---

## change_classify

- **Firma:** changeset: {files: string[], pr_metadata: PRInfo} → classification: {risk: lectura|escritura|destructiva, reason: string, affected_systems: string[]}
- **Cuando usar:** S-CLASIFICAR. Clasificar riesgo de un PR o changeset antes de seleccionar estrategia.
- **Cuando NO usar:** Clasificacion ya realizada en turno actual.
- **Notas:** Inputs: diff de archivos, metadata PR, labels. Heuristicas: schema changes→destructiva, new endpoints→escritura, config/docs→lectura.

## strategy_select

- **Firma:** classification: {risk, affected_systems} → strategy: {mode: fast-track|canary|manual, config: StrategyConfig}
- **Cuando usar:** S-ESTRATEGIA. Seleccionar estrategia deploy basada en clasificacion riesgo.
- **Cuando NO usar:** Estrategia ya seleccionada o deploy ya en ejecucion.
- **Notas:** fast-track: deploy inmediato, flag ON. canary: 5% trafico, monitoreo 15min. manual: hold para aprobacion.

## deploy_execute

- **Firma:** strategy: StrategyConfig, changeset: Changeset → deploy_result: {status: success|failed, version: string, environment: string, timestamp: ISO8601}
- **Cuando usar:** S-EJECUTAR. Ejecutar deploy segun estrategia seleccionada.
- **Cuando NO usar:** Sin clasificacion previa, sin estrategia, sin DoD completo, sin feature flag configurado.
- **Notas:** Build imagen → push registry → apply environment → activar flag. Log cada paso.

## feature_flag_manage

- **Firma:** action: create|activate|deactivate|expand, flag_config: {name: string, percentage?: number} → flag_status: {name: string, state: on|off, percentage: number}
- **Cuando usar:** Toda operacion de feature flag: crear flag pre-deploy, activar en deploy, expandir en canary, desactivar en rollback.
- **Cuando NO usar:** Flag ya en estado deseado.
- **Notas:** Primitiva base del deployer. Todo deploy requiere flag. Expansion canary: 5%→25%→50%→100%.

## post_deploy_verify

- **Firma:** deploy_result: DeployResult, baseline: MetricsBaseline → verification: {status: stable|degraded, metrics: MetricsSnapshot, comparison: MetricsDiff}
- **Cuando usar:** S-VERIFICAR. Comparar metricas post-deploy contra baseline pre-deploy.
- **Cuando NO usar:** Deploy no ejecutado o ya verificado.
- **Notas:** Metricas: latencia (p50, p95, p99), tasa error (4xx, 5xx), recursos (CPU, memoria). Thresholds: latencia +20% = degraded, error rate +1% = degraded.

## rollback_execute

- **Firma:** deploy_result: DeployResult, flag_name: string → rollback_result: {status: success|failed, reverted_to: string, metrics_normalized: boolean, diagnosis: string}
- **Cuando usar:** S-ROLLBACK. Cuando verificacion post-deploy detecta degradacion o fallo de build/push.
- **Cuando NO usar:** Metricas estables, deploy no ejecutado.
- **Notas:** Desactivar flag → revert version → verificar metricas normalizadas → alertar operador. Atomico por batch.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Clasificar tema → resolver URN → priorizar KB.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Xanpan metodologia, DoD, pipeline | urn:fxsl:kb:xanpan-agents-metodologia |
| Swarm ops, deploy, batching | urn:fxsl:kb:swarm-ops-metodologia |
| Agent spec, workspace, FSM | urn:kora:kb:agent-spec-md |
