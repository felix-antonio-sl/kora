---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-contract-validator:1.1.0
  type: lazy_load_endofunctor
extensions:
  kora:
    skill:
      form: extended
      allowed_tools:
        - artifact_read
        - oc_docs_search
        - spec_consult
      requires: []
      scripts:
        - scripts/validate_contract.py
      references:
        - references/contract-validation-map.md
      assets:
        - assets/contract-fixture-minimal.yml
---

# CM-OPENCLAW-CONTRACT-VALIDATOR

## Proposito

Validar `platform_contract` antes de handoff u operacion local, detectando colisiones, omisiones y contradicciones entre runtime config, topology, sandbox, channels y managed installs con apoyo mecanizable reproducible.

## Input/Output

- **Input:** contract_path: string?, platform_contract: object?, validation_context: object?
- **Output:** ContractValidationReport

## Procedimiento

1. Consultar `references/contract-validation-map.md` para fijar reglas doctrinales y fuentes factuales.
2. Resolver hechos OpenClaw relevantes via `oc_docs_search` antes de afirmar semantica de surfaces nativas.
3. Si existe `contract_path`, ejecutar `scripts/validate_contract.py` como verificacion mecanica base.
4. Verificar estructura minima:
   - `config_projection`
   - `managed_installs`
   - `deployment_hints`
   - `provenance`
   - `runtime_exclusions`
5. Verificar colisiones y contradicciones frecuentes:
   - `gateway.bind` vs topologia declarada
   - `trusted-proxy` sin `allowedOrigins` cuando corresponde
   - Telegram multi-account sin `defaultAccount`
   - `dmPolicy: allowlist` sin `allowFrom`
   - `tools.profile` incompatible con denies/allow criticos
   - backend `openshell` sin config o modo asociado
   - installs duplicados por locator/slug
   - `deployment_hints.manual_inputs_required` no resueltos antes de handoff
6. Verificar que `deployment_hints.validation_checks` acumulados esten cubiertos o declarados pendientes.
7. Emitir PASS|WARN|FAIL con lista de colisiones y fixes concretos, distinguiendo evidencia mecanica de interpretacion normativa.

## Signature Output

```yaml
contract_validation:
  result: "PASS"
  script_result: "PASS"
  collisions: []
  missing_inputs: []
  checks_applied:
    - "gateway_count_justificado"
    - "allowFrom_numerico"
```
