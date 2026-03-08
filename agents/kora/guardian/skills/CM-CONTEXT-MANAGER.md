---
_manifest:
  urn: urn:kora:skill:guardian-context-manager:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-CONTEXT-MANAGER

## Proposito
Mantener continuidad conversacional y detectar desvio fuera del dominio de resguardo fundacional.

## Input/Output
- **Input:** Tema actual, estado FSM y restricciones activas.
- **Output:** Decision de continuidad con contexto retenido.

## Procedimiento
1. Comparar tema actual con el estado activo.
2. Detectar continuidad, cierre o desvio de dominio.
3. Retener solo restricciones e invariantes relevantes.

## Signature Output
```yaml
context_decision:
  action: "keep"
  next_state: "S-CONSULTA"
```
