---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-operator:1.0.0
  type: lazy_load_endofunctor
---

# CM-OPENCLAW-OPERATOR

## Proposito
Mantener el agente OpenClaw en operacion local o no productiva: re-sync, higiene runtime, validaciones recurrentes y cambios declarativos de configuracion.

## Input/Output
- **Input:** objetivo: string, cambio: string?
- **Output:** OperationReport

## Procedimiento
1. Verificar health actual, config viva y drift relevante.
2. Si hay cambios de canal, ACL, UX o multi-account, consumir el telegram architecture report de entrada.
3. Si hay cambios de policy o aislamiento, consumir el sandbox architecture report de entrada.
4. Si hay altas/bajas/updates de skills, plugins o bundles, consumir el managed installs report de entrada.
5. Si hay cambios topologicos o federacion, consumir el topology report de entrada.
6. Si existe contrato previo, consumir el reconciliation report para privilegiar patch incremental.
7. Traducir el `patch_plan` a operaciones aplicables sobre config viva.
8. Aplicar cambios declarativos solo sobre runtime local/no productivo y reiniciar solo cuando corresponda.
9. Si el cambio exige host mutations o alcance productivo remoto, derivar a `ops/clawstack`.
10. Ejecutar re-sync desde artefactos verificados cuando haya cambios fuente.
11. Preservar `agentDir`, auth por agente y estado sensible.

## Signature Output
```yaml
operation:
  result: "OK"
  restart_required: false
  drift_checked: true
  reconciliation_mode: "patch"
```
