---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-patch-planner:1.0.0
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
        - references/patch-semantics-map.md
      assets:
        - assets/runtime-patch-template.yml
---

# CM-OPENCLAW-PATCH-PLANNER

## Proposito

Traducir diferencias de contrato o cambios deseados a patches selectivos y aplicables sobre config viva OpenClaw, con semántica explícita `merge|replace|remove`.

## Input/Output

- **Input:** patch_plan: object[], current_contract: object?, desired_contract: object?
- **Output:** RuntimePatchPlan

## Procedimiento

1. Consultar `references/patch-semantics-map.md`.
2. Convertir cada diferencia a una operación explícita:
   - `merge`: objetos con semántica de JSON merge patch
   - `replace`: arrays o scalars completos
   - `remove`: claves a eliminar usando `null`
3. Calcular `target_path` en surfaces OpenClaw reales:
   - `gateway.*`
   - `agents.defaults.*`
   - `agents.list[]`
   - `channels.*`
   - `tools.*`
   - `plugins.*`
4. Marcar impacto de restart:
   - `gateway.*`, `plugins`, `discovery`, `canvasHost` => restart requerido
   - `channels.*`, `agents.*`, `tools.*`, `session.*`, `messages.*` => sin restart por default
5. Emitir patch serializable bajo `patches/*.yml`.
6. Usar `assets/runtime-patch-template.yml` como shape de referencia.

## Signature Output

```yaml
runtime_patch:
  mode: "patch"
  operations:
    - target_path: "channels.telegram"
      op: "merge"
      value:
        silentErrorReplies: true
      restart_required: false
    - target_path: "gateway.bind"
      op: "replace"
      value: "lan"
      restart_required: true
```
