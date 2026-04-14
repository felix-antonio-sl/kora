---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-operator:1.0.0
  type: lazy_load_endofunctor
---

# CM-OPENCLAW-OPERATOR

## Proposito
Mantener el agente OpenClaw en operacion local o no productiva: re-sync, higiene runtime, validaciones recurrentes y cambios declarativos de configuracion.

## Input/Output
- **Input:** objetivo: string, cambio: string?, telegram_report: object?, sandbox_report: object?, managed_installs_report: object?, topology_report: object?, reconciliation_report: object?, execution_mode: string?
- **Output:** OperationReport

## Procedimiento
1. Verificar health actual, config viva y drift relevante.
2. Si hay cambios de canal, ACL, UX o multi-account, consumir `telegram_report`.
3. Si hay cambios de policy o aislamiento, consumir `sandbox_report`.
4. Si hay altas/bajas/updates de skills, plugins o bundles, consumir `managed_installs_report`.
5. Si hay cambios topologicos o federacion, consumir `topology_report`.
6. Si existe contrato previo, consumir `reconciliation_report` para privilegiar patch incremental.
7. Traducir el `patch_plan` a operaciones aplicables sobre config viva.
8. Si `execution_mode=dry-run`, emitir el plan validado sin mutar runtime.
9. Aplicar cambios declarativos sobre runtime local o productivo y reiniciar solo cuando corresponda.
10. Si el cambio exige host mutations, pasos destructivos o alcance productivo remoto, exigir confirmacion explicita y continuar bajo las fases operativas de `clawforge`.
11. Ejecutar re-sync desde artefactos verificados cuando haya cambios fuente.
12. Preservar `agentDir`, auth por agente y estado sensible.

## Signature Output
```yaml
operation:
  result: "OK"
  restart_required: false
  drift_checked: true
  reconciliation_mode: "patch"
```
