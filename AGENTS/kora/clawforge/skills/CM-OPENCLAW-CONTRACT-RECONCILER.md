---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-contract-reconciler:1.0.0
  type: lazy_load_endofunctor
---

# CM-OPENCLAW-CONTRACT-RECONCILER

## Proposito

Reconciliar un `platform_contract` existente con nuevos fragmentos o cambios deseados, priorizando patch incremental antes que regeneracion total.

## Input/Output

- **Input:** current_contract: object?, new_fragments: object[], desired_contract: object?
- **Output:** ContractReconciliationReport

## Procedimiento

1. Si no existe contrato previo, devolver modo `regenerate`.
2. Comparar por dominio:
   - `config_projection.gateway`
   - `config_projection.agents.*`
   - `config_projection.channels.*`
   - `config_projection.tools.*`
   - `managed_installs.*`
   - `deployment_hints.*`
3. Clasificar cambios:
   - `reuse`
   - `patch`
   - `regenerate`
4. Si el cambio afecta identidad, topologia estructural o surfaces incompatibles, marcar `regenerate`.
5. Si el cambio afecta solo un subconjunto no colidente, emitir `patch_plan`.

## Signature Output

```yaml
reconciliation:
  mode: "patch"
  unchanged_domains:
    - "managed_installs"
  changed_domains:
    - "channels.telegram"
  patch_plan:
    - path: "config_projection.channels.telegram"
      action: "replace"
```
