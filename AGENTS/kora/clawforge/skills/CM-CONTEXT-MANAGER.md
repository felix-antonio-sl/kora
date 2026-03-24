---
_manifest:
  urn: urn:kora:skill:clawforge-context-manager:1.0.0
  type: lazy_load_endofunctor
---

# CM-CONTEXT-MANAGER

## Proposito
Detectar desvio entre la fase OpenClaw activa y la solicitud actual.

## Input/Output
- **Input:** fase_activa: string, solicitud: string
- **Output:** ContextAssessment

## Procedimiento
1. Comparar solicitud con la fase activa.
2. Si la solicitud cambia de dominio relevante, reenviar a `S-DISPATCHER`.
3. Preservar `agente_target`, `topology_target`, `contract_path` y hallazgos pendientes.

## Signature Output
```yaml
context:
  shift: false
  preserved:
    - "agente_target"
    - "contract_path"
```
