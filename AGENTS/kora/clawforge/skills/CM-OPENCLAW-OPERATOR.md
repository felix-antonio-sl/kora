---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-operator:1.0.0
  type: lazy_load_endofunctor
---

# CM-OPENCLAW-OPERATOR

## Proposito
Mantener el agente OpenClaw en operacion: re-sync, higiene runtime, validaciones recurrentes y cambios declarativos de configuracion.

## Input/Output
- **Input:** objetivo: string, cambio: string?
- **Output:** OperationReport

## Procedimiento
1. Verificar health actual, config viva y drift relevante.
2. Si hay cambios de canal, ACL, UX o multi-account, reusar las decisiones de `CM-OPENCLAW-TELEGRAM-ARCHITECT`.
3. Si hay cambios de policy o aislamiento, reusar `CM-OPENCLAW-SANDBOX-ARCHITECT`.
4. Si hay altas/bajas/updates de skills, plugins o bundles, reusar `CM-OPENCLAW-PLUGIN-BUNDLE-MANAGER`.
5. Si hay cambios topologicos o federacion, reusar `CM-OPENCLAW-TOPOLOGIST`.
6. Si existe contrato previo, invocar `CM-OPENCLAW-CONTRACT-RECONCILER` y privilegiar patch incremental.
7. Traducir el `patch_plan` con `CM-OPENCLAW-PATCH-PLANNER`.
8. Aplicar cambios declarativos al runtime con `CM-OPENCLAW-PATCH-APPLIER` y reiniciar solo cuando corresponda.
9. Ejecutar re-sync desde artefactos verificados cuando haya cambios fuente.
10. Preservar `agentDir`, auth por agente y estado sensible.

## Signature Output
```yaml
operation:
  result: "OK"
  restart_required: false
  drift_checked: true
  reconciliation_mode: "patch"
```
