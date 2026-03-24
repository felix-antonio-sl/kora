---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-deployer:1.0.0
  type: lazy_load_endofunctor
---

# CM-OPENCLAW-DEPLOYER

## Proposito
Desplegar y activar un agente OpenClaw de punta a punta usando `platform_contract`, config nativa y herramientas runtime/host segun corresponda.

## Input/Output
- **Input:** transmutation_path: string, gateway_target: string, topology_target: string
- **Output:** DeployReport

## Procedimiento
1. Cargar `_transmutation.yml` y verificar hashes, `platform_contract` y artefactos emitidos.
2. Ejecutar `CM-OPENCLAW-CONTRACT-VALIDATOR` antes de aplicar nada. Si hay colisiones o `manual_inputs_required` sin resolver, abortar.
3. Consultar `CM-OPENCLAW-KNOWLEDGE-NAVIGATOR` si el deploy depende de topologia, auth mode, proxy o sandbox backend no trivial.
4. Materializar `workspace_target`, `config_projection` y `managed_installs` sin reinterpretar `TOOLS.md` como autoridad de deploy.
5. Aplicar config nativa OpenClaw por superficies estructuradas:
   - `agents.defaults`
   - `agents.list[]`
   - `tools.*`
   - `sandbox.*`
   - `channels.*`
   - `gateway.*`
6. Si el contrato indica Telegram, resolver config con el patron de `CM-OPENCLAW-TELEGRAM-ARCHITECT`.
7. Si el contrato indica sandbox complejo, validar backend y modo con `CM-OPENCLAW-SANDBOX-ARCHITECT`.
8. Si el contrato indica installs gestionados, ejecutar lo derivado por `CM-OPENCLAW-PLUGIN-BUNDLE-MANAGER`.
9. Si la topologia es multi-gateway, aplicar decision de `CM-OPENCLAW-TOPOLOGIST` antes de abrir binds, proxy o puertos derivados.
10. Ejecutar `openclaw doctor`, `openclaw status --deep` y chequeos minimos del runtime.
11. Si el deploy falla, clasificar causa y reenviar a `S-CONFIGURE` o `S-TROUBLESHOOT`.

## Signature Output
```yaml
deploy:
  status: "DEPLOYED"
  doctor: "PASS"
  status_deep: "OK"
  topology_applied: "single-gateway-multi-agent"
```
