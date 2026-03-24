---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-troubleshooter:1.0.0
  type: lazy_load_endofunctor
---

# CM-OPENCLAW-TROUBLESHOOTER

## Proposito
Diagnosticar y corregir fallas de bootstrap, contrato, config local, sandbox, tooling, gateway o topologia en agentes OpenClaw.

## Input/Output
- **Input:** sintoma: string, alcance: string, telegram_report: object?, sandbox_report: object?, managed_installs_report: object?, topology_report: object?, runtime_evidence: object?
- **Output:** TroubleshootReport

## Procedimiento
1. Clasificar la falla por capa: workspace, config, gateway, host, docker, canal o federation.
2. Si la falla es de canal/ACL/UX Telegram, consumir `telegram_report` como mapa de verdad.
3. Si la falla es de sandbox o tools, consumir `sandbox_report`.
4. Si la falla es de install/compatibilidad, consumir `managed_installs_report`.
5. Si la falla es topologica o de gateway/proxy, consumir `topology_report`.
6. Recolectar evidencia con `oc_cli`, `workspace_read`, `artifact_read`, `diff_compute` u herramientas equivalentes permitidas.
7. Si el fix toca workspace o contrato, emitir remediacion minima via el surgeon co-listado en el estado.
8. Si el problema es de stack remoto o host-level, cortar y derivar a `external-openclaw-ops`.
9. Verificar con doctor/status/logs cuando exista runtime local o `runtime_evidence` previa.

## Signature Output
```yaml
troubleshoot:
  cause: "config_drift"
  fixed: true
  layer: "gateway"
```
