---
_manifest:
  urn: "urn:ops:skill:integrador-intent-classifier:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Clasificar la intencion del operador en el contexto de integracion para dirigir a la rama FSM correcta. Mapear input libre a uno de los intents validos del integrador.

## Input/Output

- **Input:** user_message: string, current_state: FSM_State
- **Output:** intent: {type: MERGE|COHERENCIA|CONFLICTO|COLA|END, confidence: float, context: string}

## Procedimiento

1. **Extraer** tokens clave del mensaje: PR number, merge, coherencia, conflicto, cola, queue, backpressure, prioridad, status, resolver.
2. **Mapear** a intent:
   - Tokens PR, merge, integrar, branch, diff, semantico → MERGE
   - Tokens coherencia, cross-PR, verificar, overlap, zona, patrones → COHERENCIA
   - Tokens conflicto, resolver, trivial, substantivo, competidores, incompatible → CONFLICTO
   - Tokens cola, queue, prioridad, backpressure, throughput, depth → COLA
   - Tokens terminar, fin, resumen, listo → END
3. **Resolver ambiguedad**: IF multiples intents → priorizar por urgencia: CONFLICTO > COHERENCIA > MERGE > COLA > END.
4. **Validar contexto**: IF intent requiere estado previo (ej. CONFLICTO sin merge analizado) → redirigir a paso previo necesario.

## Signature Output

```yaml
intent:
  type: "MERGE"
  confidence: 0.94
  context: "PR #205 solicitado para merge semantico"
  requires_prior: null
```
