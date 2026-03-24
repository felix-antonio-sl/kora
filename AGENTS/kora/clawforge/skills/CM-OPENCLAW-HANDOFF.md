---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-handoff:1.0.0
  type: lazy_load_endofunctor
---

# CM-OPENCLAW-HANDOFF

## Proposito
Emitir el handoff disciplinado hacia `kora/forgemaster` o `ops/clawstack` segun los artefactos disponibles, sin ejecutar deploy productivo.

## Input/Output
- **Input:** output_dir: string, contract_path: string, manifest_path: string?
- **Output:** HandoffReport

## Procedimiento
1. Verificar que staging y `platform_contract` esten completos.
2. Resumir prerequisites, `deployment_hints.manual_inputs_required`, `deployment_hints.validation_checks` y topologia target.
3. Si existe `_transmutation.yml`, emitir frontera operativa hacia `ops/clawstack`.
4. Si NO existe `_transmutation.yml`, marcar handoff listo para `kora/forgemaster` a fin de transmutar antes del deploy productivo.
5. Nunca ejecutar host mutations, auth setup ni pairing.

## Signature Output
```yaml
handoff:
  ready: true
  next_agent: "kora/forgemaster"
  contract_path: "/path/contracts/platform-contract.yml"
  manifest_path: null
  requires_transmutation: true
```
