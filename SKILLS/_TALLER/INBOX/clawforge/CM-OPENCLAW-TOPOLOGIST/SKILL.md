---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-topologist:1.0.0
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
        - references/topology-map.md
      assets:
        - assets/topology-contract-template.yml
---

# CM-OPENCLAW-TOPOLOGIST

## Proposito

Elegir y justificar la topologia OpenClaw correcta para el agente o conjunto de agentes: un gateway con multiples agentes, gateways aislados, perfiles separados, remote mode, federation o trusted-proxy.

## Input/Output

- **Input:** escenario: string, trust_boundary: string, isolation_need: string
- **Output:** TopologyReport

## Procedimiento

1. Consultar `references/topology-map.md`.
2. Elegir por defecto `single-gateway-multi-agent`.
3. Escalar a gateways aislados solo si existe una razon estructural:
   - frontera de confianza
   - rescate operacional
   - aislamiento de estado
   - incompatibilidad de routing o canales
4. Si hay multiples gateways:
   - preferir `--profile`
   - separar `OPENCLAW_STATE_DIR`
   - separar `OPENCLAW_CONFIG_PATH`
   - separar puertos derivados
5. Si hay reverse proxy:
   - resolver si corresponde `trusted-proxy`
   - exigir `allowedOrigins`
   - no degradar auth por comodidad
6. Si hay federation:
   - justificar `bind: lan`
   - delimitar mounts, hooks y surface expuesta
7. Emitir salida mecanizable en tres bloques:
   - `config_fragment`
   - `contract_fragment`
   - `validation_checks`
8. Usar `assets/topology-contract-template.yml` como shape de referencia.

## Signature Output

```yaml
topology:
  recommended: "single-gateway-multi-agent"
  config_fragment:
    gateway:
      bind: "loopback"
      auth:
        mode: "token"
  contract_fragment:
    deployment_hints:
      topology:
        recommended: "single-gateway-multi-agent"
        gateway_count: 1
        requires_profiles: false
        requires_trusted_proxy: false
      ports:
        spacing_min: 20
  validation_checks:
    - "gateway_count_justificado"
    - "bind_mode_coherente"
  warnings: []
```
