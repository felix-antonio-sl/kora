---
_manifest:
  urn: "urn:ops:skill:orquestador-swarm-intent-classifier:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Clasificar la intencion del Operador en el contexto de orquestacion del enjambre para dirigir a la rama FSM correcta. Mapear input libre a uno de los intents validos del orquestador.

## Input/Output

- **Input:** user_message: string, current_state: FSM_State
- **Output:** intent: {type: EVENTO|GOLDEN_PATH|BACKPRESSURE|CIRCUITO|ESTADO|END, confidence: float, context: string}

## Procedimiento

1. **Extraer** tokens clave del mensaje: evento, PR, commit, alerta, deploy, golden path, cola, saturacion, circuit breaker, fallo, estado, resumen.
2. **Mapear** a intent:
   - Tokens evento, commit, PR, alerta, propuesta, eval, heartbeat, nuevo → EVENTO
   - Tokens golden path, ejecutar, rutear, historia, hotfix, infraestructura, flujo → GOLDEN_PATH
   - Tokens backpressure, cola, saturacion, presion, reducir, drenar → BACKPRESSURE
   - Tokens circuit breaker, fallo, cascada, contener, pausar, drift → CIRCUITO
   - Tokens estado, status, reporte, agentes, flujos, activos → ESTADO
   - Tokens terminar, fin, resumen, listo, cerrar → END
3. **Resolver ambiguedad**: IF multiples intents → priorizar por urgencia: CIRCUITO > BACKPRESSURE > EVENTO > GOLDEN_PATH > ESTADO > END.
4. **Validar contexto**: IF intent requiere estado previo (ej. GOLDEN_PATH sin evento clasificado) → redirigir a paso previo necesario.

## Signature Output

```yaml
intent:
  type: "EVENTO"
  confidence: 0.94
  context: "PR #245 new endpoint detectado"
  requires_prior: null
```
