---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-patch-applier:1.1.0
  type: lazy_load_endofunctor
extensions:
  kora:
    skill:
      form: extended
      allowed_tools:
        - oc_cli
        - oc_docs_search
      requires: []
      scripts:
        - scripts/validate_runtime_patch.py
      references:
        - references/apply-evidence-map.md
---

# CM-OPENCLAW-PATCH-APPLIER

## Proposito

Aplicar patches selectivos sobre config viva OpenClaw en entornos locales o no productivos, con semantica explicita, `dry-run` soportado y verificacion posterior.

## Input/Output

- **Input:** runtime_patch: object, gateway_target: string, execution_mode: string?
- **Output:** PatchApplyReport

## Procedimiento

1. Consultar `references/apply-evidence-map.md` y resolver hechos OpenClaw via `oc_docs_search` antes de materializar el patch.
2. Validar `runtime_patch` con `scripts/validate_runtime_patch.py`.
3. Agrupar operaciones por estrategia de aplicación:
   - `openclaw config set` para cambios puntuales de un key path
   - `config.patch` para merges parciales de objetos
   - `config.patch` con `null` para removals
4. Si `execution_mode=dry-run`, devolver el plan validado y no mutar runtime.
5. Aplicar en orden estable y registrar resultado por operacion.
6. Si alguna operacion toca superficie con restart requerido, ejecutar restart controlado al final del batch.
7. Verificar con `openclaw doctor` o `status --deep` segun el area afectada.
8. Si el target corresponde a deploy productivo remoto, abortar y derivar a `external-openclaw-ops`.

## Signature Output

```yaml
patch_apply:
  status: "OK"
  execution_mode: "dry-run"
  operations_applied: 0
  restart_executed: false
```
