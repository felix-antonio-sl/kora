---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-contractor:1.0.0
  type: lazy_load_endofunctor
extensions:
  kora:
    skill:
      form: extended
      allowed_tools:
        - spec_consult
        - artifact_write
      requires: []
      assets:
        - assets/platform-contract-template.yml
---

# CM-OPENCLAW-CONTRACTOR

## Proposito

Derivar el `platform_contract` OpenClaw con `config_projection`, `managed_installs`, `deployment_hints` y `runtime_exclusions`.

## Input/Output

- **Input:** workspace: object, topology_target: string
- **Output:** PlatformContractReport

## Procedimiento

1. Releer blueprint y, si hay dudas de plataforma, consultar `CM-OPENCLAW-KNOWLEDGE-NAVIGATOR`.
2. Usar `assets/platform-contract-template.yml` como shape minima del contrato.
3. Proyectar `config.json` a superficies nativas OpenClaw.
4. Consumir explicitamente outputs de:
   - `CM-OPENCLAW-TOPOLOGIST`
   - `CM-OPENCLAW-TELEGRAM-ARCHITECT`
   - `CM-OPENCLAW-SANDBOX-ARCHITECT`
   - `CM-OPENCLAW-PLUGIN-BUNDLE-MANAGER`
5. Pasar `base_contract` + fragmentos a `CM-OPENCLAW-CONTRACT-ASSEMBLER`.
6. Si hay colisiones, detener el ensamblaje y devolverlas para remediacion; no resolverlas implicitamente.
7. Separar skills locales, installs gestionados y runtime state excluido.
8. Llenar `deployment_hints` con:
   - topologia recomendada
   - bind requirements
   - mounts RO/RW
   - `manual_inputs_required`
   - prerequisitos de auth, channel setup, proxy o federation
9. Acumular `validation_checks` emitidos por las skills verticales para que `CM-OPENCLAW-CONTRACT-VALIDATOR`, deploy y audit los consuman despues.
10. Emitir `manual_inputs_required` cuando falten datos criticos no deducibles estructuradamente.
11. Nunca inferir datos de deploy critico desde `TOOLS.md` si el contrato puede expresarlos.

## Signature Output

```yaml
platform_contract:
  config_projection:
    gateway: {}
    agents:
      defaults: {}
      list: []
  managed_installs:
    workspace_skills: []
    skills: []
    plugins: []
    bundles: []
  deployment_hints:
    topology:
      recommended: "single-gateway-multi-agent"
    manual_inputs_required: []
  validation_checks:
    - "gateway_count_justificado"
    - "allowFrom_numerico"
  provenance:
    channels.telegram: "CM-OPENCLAW-TELEGRAM-ARCHITECT"
  manual_inputs_required: []
```
