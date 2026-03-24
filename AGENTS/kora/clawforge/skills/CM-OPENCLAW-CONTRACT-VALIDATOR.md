---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-contract-validator:1.0.0
  type: lazy_load_endofunctor
---

# CM-OPENCLAW-CONTRACT-VALIDATOR

## Proposito

Validar `platform_contract` antes de handoff u operacion local, detectando colisiones, omisiones y contradicciones entre runtime config, topology, sandbox, channels y managed installs.

## Input/Output

- **Input:** platform_contract: object
- **Output:** ContractValidationReport

## Procedimiento

1. Verificar estructura minima:
   - `config_projection`
   - `managed_installs`
   - `deployment_hints`
   - `provenance`
   - `runtime_exclusions`
2. Verificar colisiones y contradicciones frecuentes:
   - `gateway.bind` vs topologia declarada
   - `trusted-proxy` sin `allowedOrigins` cuando corresponde
   - Telegram multi-account sin `defaultAccount`
   - `dmPolicy: allowlist` sin `allowFrom`
   - `tools.profile` incompatible con denies/allow criticos
   - backend `openshell` sin config o modo asociado
   - installs duplicados por locator/slug
   - `deployment_hints.manual_inputs_required` no resueltos antes de handoff
3. Verificar que `deployment_hints.validation_checks` acumulados esten cubiertos o declarados pendientes.
4. Emitir PASS|WARN|FAIL con lista de colisiones y fixes concretos.

## Signature Output

```yaml
contract_validation:
  result: "PASS"
  collisions: []
  missing_inputs: []
  checks_applied:
    - "gateway_count_justificado"
    - "allowFrom_numerico"
```
