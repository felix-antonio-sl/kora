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

Emitir el handoff disciplinado hacia `kora/forgemaster` o `ops/clawstack` segun los artefactos verificados disponibles, sin ejecutar provision ni deploy productivo.

## Input/Output

- **Input:** output_dir: string, contract_path: string, contract_validation: object?, manifest_path: string?, manifest_validation: object?
- **Output:** HandoffReport

## Procedimiento

1. Verificar que staging y `platform_contract` esten completos.
2. Exigir `contract_validation.result` compatible con handoff (`PASS` o `WARN` justificado).
3. Resumir prerequisites, `deployment_hints.manual_inputs_required`, `deployment_hints.validation_checks` y topologia target.
4. Si existe `manifest_path`, ejecutar `scripts/verify_handoff_manifest.py` o consumir `manifest_validation` equivalente.
5. Solo si el manifest valida por estructura minima, hashes fuente y provenance compatible con transmutacion KORA, emitir frontera operativa hacia `ops/clawstack`.
6. Si NO existe `_transmutation.yml`, marcar handoff listo para `kora/forgemaster` a fin de transmutar antes del deploy productivo.
7. Nunca ejecutar host mutations, auth setup ni pairing.

## Signature Output
```yaml
handoff:
  ready: true
  next_target: "kora/forgemaster"
  contract_path: "/path/contracts/platform-contract.yml"
  manifest_path: null
  manifest_verified: false
  requires_transmutation: true
```
