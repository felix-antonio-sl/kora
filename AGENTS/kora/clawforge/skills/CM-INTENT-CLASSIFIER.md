---
_manifest:
  urn: urn:kora:skill:clawforge-intent-classifier:1.0.0
  type: lazy_load_endofunctor
---

# CM-INTENT-CLASSIFIER

## Proposito
Clasificar la solicitud OpenClaw-oriented hacia la fase correcta del ciclo de vida.

## Input/Output
- **Input:** solicitud: string
- **Output:** IntentClassification

## Procedimiento
1. Detectar si la solicitud pide consulta documental, diseno, scaffold, contract, validacion, deploy, operacion, auditoria, fix o evolucion.
2. Detectar si el modo es guiado o libre.
3. Identificar si el primer paso correcto es documental/fundacional antes que accion operacional.

## Signature Output
```yaml
intent:
  state: "S-CONSULT"
  mode: "libre"
  requires_handoff: false
```
