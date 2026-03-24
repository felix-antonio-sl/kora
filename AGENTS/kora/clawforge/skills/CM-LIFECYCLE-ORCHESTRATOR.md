---
_manifest:
  urn: urn:kora:skill:clawforge-lifecycle-orchestrator:1.0.0
  type: lazy_load_endofunctor
---

# CM-LIFECYCLE-ORCHESTRATOR

## Proposito
Coordinar el ciclo guiado DESIGN -> CREATE -> CONFIGURE -> VALIDATE -> DEPLOY -> AUDIT.

## Input/Output
- **Input:** objetivo: string, fase_actual: string
- **Output:** GuidedLifecycleReport

## Procedimiento
1. Consolidar entregables y checkpoints de cada fase.
2. Verificar que el `platform_contract` exista y que haya sido materializado en staging antes de pasar a DEPLOY.
3. Verificar que deploy y audit cierren con health, runtime checks nativos, validacion de colisiones y patching aplicable cuando corresponda.

## Signature Output
```yaml
guided:
  next_phase: "S-DEPLOY"
  checkpoints_ok: true
```
