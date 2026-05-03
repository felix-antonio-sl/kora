---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-handoff:1.1.0
  type: lazy_load_endofunctor
extensions:
  kora:
    skill:
      form: extended
      allowed_tools:
        - artifact_read
      requires: []
      scripts:
        - scripts/verify_handoff_manifest.py
      references:
        - references/handoff-basis.md
---

# CM-OPENCLAW-HANDOFF

## Proposito

Emitir el handoff disciplinado dentro del propio `clawforge`, resolviendo si el siguiente paso es la transmutación KORA (cuando falta transmutacion) o la ejecucion operativa local (`S-PROVISION` o `S-DEPLOY`) cuando el paquete OpenClaw ya esta verificado.

## Input/Output

- **Input:** output_dir: string, contract_path: string, contract_validation: object?, manifest_path: string?, manifest_validation: object?
- **Output:** HandoffReport

## Procedimiento

1. Verificar que staging y `platform_contract` esten completos.
2. Exigir `contract_validation.result` compatible con handoff (`PASS` o `WARN` justificado).
3. Resumir prerequisites, `deployment_hints.manual_inputs_required`, `deployment_hints.validation_checks` y topologia target.
4. Si existe `manifest_path`, ejecutar `scripts/verify_handoff_manifest.py` o consumir `manifest_validation` equivalente.
5. Solo si el manifest valida por estructura minima, hashes fuente y provenance compatible con transmutacion KORA, marcar el paquete como listo para `S-PROVISION` o `S-DEPLOY` dentro del mismo `clawforge`.
6. Si NO existe `_transmutation.yml`, marcar handoff listo para la transmutación KORA a fin de transmutar antes del deploy productivo.
7. Nunca ejecutar host mutations, auth setup ni pairing dentro del propio handoff; esas operaciones comienzan recien al entrar en `S-PROVISION` o `S-DEPLOY`.

## Signature Output
```yaml
handoff:
  ready: true
  next_target: "S-DEPLOY"
  contract_path: "/path/contracts/platform-contract.yml"
  manifest_path: "/path/output/_transmutation.yml"
  manifest_verified: true
  requires_transmutation: false
```
