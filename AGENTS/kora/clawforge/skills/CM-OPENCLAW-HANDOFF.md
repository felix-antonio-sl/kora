---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-handoff:1.0.0
  type: lazy_load_endofunctor
---

# CM-OPENCLAW-HANDOFF

## Proposito
Emitir el handoff disciplinado hacia `ops/clawstack` para deploy o re-sync productivo.

## Input/Output
- **Input:** output_dir: string, manifest_path: string, platform_contract: object
- **Output:** HandoffReport

## Procedimiento
1. Verificar que staging y contract esten completos.
2. Resumir prerequisites, `manual_inputs_required` y topologia target.
3. Emitir ruta exacta de `_transmutation.yml` y frontera operativa hacia `ops/clawstack`.
4. Nunca ejecutar host mutations, auth setup ni pairing.

## Signature Output
```yaml
handoff:
  ready: true
  next_agent: "ops/clawstack"
  manifest_path: "/path/_transmutation.yml"
```
