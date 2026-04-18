---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-plugin-bundle-manager:1.0.0
  type: lazy_load_endofunctor
extensions:
  kora:
    skill:
      form: extended
      allowed_tools:
        - oc_docs_search
        - spec_consult
      requires: []
      references:
        - references/plugin-bundle-map.md
      assets:
        - assets/managed-installs-template.yml
---

# CM-OPENCLAW-PLUGIN-BUNDLE-MANAGER

## Proposito

Modelar `managed_installs` para Skills, plugins y bundles OpenClaw, distinguiendo entre contenido que debe vivir en el workspace y capacidades que deben instalarse por vias nativas de registry/marketplace.

## Input/Output

- **Input:** necesidad: string, source_kind: workspace|skill|plugin|bundle
- **Output:** ManagedInstallsReport

## Procedimiento

1. Consultar `references/plugin-bundle-map.md`.
2. Clasificar la necesidad:
   - skill local del agente
   - skill gestionado por registry
   - plugin nativo OpenClaw
   - bundle compatible de marketplace
3. Decidir destino:
   - `workspace_target.skills`
   - `managed_installs.skills`
   - `managed_installs.plugins`
   - `managed_installs.bundles`
4. Si la capacidad existe en ClawHub, marketplace o install surface nativa, preferir install gestionado antes que copiar artefactos ad hoc.
5. Verificar si hay:
   - trust/enable step
   - version pin
   - compatibilidad de plugin SDK
   - restricciones de runtime
6. Emitir `manual_inputs_required` si falta locator, marketplace, version o decision de pinning.
7. Emitir salida mecanizable en tres bloques:
   - `managed_installs`
   - `contract_fragment`
   - `validation_checks`
8. Usar `assets/managed-installs-template.yml` como shape de referencia.

## Signature Output

```yaml
managed_installs:
  workspace_skills: []
  skills: []
  plugins:
    - locator: "clawhub:openclaw-codex-app-server"
      version: "1.2.3"
      source: "clawhub"
      enable_after_install: true
  bundles: []
  contract_fragment:
    deployment_hints:
      managed_installs_required: true
      manual_inputs_required: []
  validation_checks:
    - "plugin_locator_resuelto"
    - "version_pinned_o_explicita"
  warnings: []
```
