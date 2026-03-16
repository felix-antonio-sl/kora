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
- **Input:** mensaje_actual: string, contexto_previo: ContextSummary | null, invariantes_activos: string[] | null
- **Output:** ContextDecision (ver Signature Output)

## Procedimiento
1. Comparar tema actual con el contexto retenido.
2. Detectar continuidad, cierre o desvio de dominio.
3. Retener solo restricciones e invariantes relevantes.
4. Emitir clasificacion de continuidad sin codificar transiciones FSM.

## Signature Output
```yaml
context_decision:
  continuidad: "CONTINUA"
  invariantes_retenidos:
    - "precedencia_normativa"
```
