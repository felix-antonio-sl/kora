---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-patch-applier:1.0.0
  type: lazy_load_endofunctor
---

# CM-OPENCLAW-PATCH-APPLIER

## Proposito

Aplicar patches selectivos sobre config viva OpenClaw con semántica explícita y verificación posterior.

## Input/Output

- **Input:** runtime_patch: object, gateway_target: string
- **Output:** PatchApplyReport

## Procedimiento

1. Validar que `runtime_patch.operations[]` no contenga conflictos internos.
2. Agrupar operaciones por estrategia de aplicación:
   - `openclaw config set` para cambios puntuales de un key path
   - `config.patch` para merges parciales de objetos
   - `config.patch` con `null` para removals
3. Aplicar en orden estable y registrar resultado por operación.
4. Si alguna operación toca superficie con restart requerido, ejecutar restart controlado al final del batch.
5. Verificar con `openclaw doctor` o `status --deep` según el área afectada.

## Signature Output

```yaml
patch_apply:
  status: "OK"
  operations_applied: 2
  restart_executed: true
```
