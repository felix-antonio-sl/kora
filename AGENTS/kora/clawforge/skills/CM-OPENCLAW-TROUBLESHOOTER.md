---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-troubleshooter:1.0.0
  type: lazy_load_endofunctor
---

# CM-OPENCLAW-TROUBLESHOOTER

## Proposito
Diagnosticar y corregir fallas de bootstrap, config, sandbox, tooling, gateway o topologia en agentes OpenClaw.

## Input/Output
- **Input:** sintoma: string, alcance: string
- **Output:** TroubleshootReport

## Procedimiento
1. Clasificar la falla por capa: workspace, config, gateway, host, docker, canal o federation.
2. Si la falla es de canal/ACL/UX Telegram, usar `CM-OPENCLAW-TELEGRAM-ARCHITECT` como mapa de verdad.
3. Si la falla es de sandbox o tools, usar `CM-OPENCLAW-SANDBOX-ARCHITECT`.
4. Si la falla es de install/compatibilidad, usar `CM-OPENCLAW-PLUGIN-BUNDLE-MANAGER`.
5. Si la falla es topologica o de gateway/proxy, usar `CM-OPENCLAW-TOPOLOGIST`.
6. Recolectar evidencia con `oc_cli`, `host_exec`, `docker_exec`, `artifact_read`, `diff_compute` u herramientas equivalentes.
7. Aplicar fix minimo reversible.
8. Verificar con doctor/status/logs y reenviar a `S-AUDIT`.

## Signature Output
```yaml
troubleshoot:
  cause: "config_drift"
  fixed: true
  layer: "gateway"
```
