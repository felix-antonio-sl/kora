---
_manifest:
  urn: urn:kora:skill:clawforge-lifecycle-orchestrator:1.0.0
  type: lazy_load_endofunctor
---

# CM-LIFECYCLE-ORCHESTRATOR

## Proposito
Coordinar el ciclo guiado CONSULT -> DESIGN -> CREATE -> CONFIGURE -> VALIDATE -> HANDOFF -> PROVISION/DEPLOY -> AUDIT.

## Input/Output
- **Input:** objetivo: string, fase_actual: string
- **Output:** GuidedLifecycleReport

## Procedimiento
1. Consolidar entregables y checkpoints de cada fase.
2. Verificar que el `platform_contract` exista, tenga `deployment_hints.validation_checks` y haya sido materializado en staging antes de pasar a HANDOFF.
3. Verificar que el handoff identifique correctamente si el siguiente paso es la transmutación KORA (transmutacion) o la propia fase operativa de `clawforge` (`S-PROVISION` o `S-DEPLOY`) cuando `_transmutation.yml` ya esta verificado.

## Signature Output
```yaml
guided:
  next_phase: "handoff"
  checkpoints_ok: true
```
