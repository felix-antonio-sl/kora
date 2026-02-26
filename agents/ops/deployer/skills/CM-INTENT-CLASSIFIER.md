---
_manifest:
  urn: "urn:ops:skill:deployer-intent-classifier:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Clasificar la intencion del operador en el contexto de deploy para dirigir a la rama FSM correcta. Mapear input libre a uno de los intents validos del deployer.

## I/O

- **Input:** user_message: string, current_state: FSM_State
- **Output:** intent: {type: CLASIFICAR|ESTRATEGIA|EJECUTAR|VERIFICAR|ROLLBACK|END, confidence: float, context: string}

## Procedimiento

1. **Extraer** tokens clave del mensaje: PR number, changeset, riesgo, deploy, rollback, verificar, status, metricas.
2. **Mapear** a intent:
   - Tokens PR, cambio, clasificar, riesgo, diff → CLASIFICAR
   - Tokens estrategia, modo, canary, fast-track, manual, flag → ESTRATEGIA
   - Tokens deploy, ejecutar, push, release, activar → EJECUTAR
   - Tokens verificar, metricas, status, health, baseline → VERIFICAR
   - Tokens rollback, revert, deshacer, degradado, fallo → ROLLBACK
   - Tokens terminar, fin, resumen, listo → END
3. **Resolver ambiguedad**: IF multiples intents → priorizar por urgencia: ROLLBACK > VERIFICAR > EJECUTAR > ESTRATEGIA > CLASIFICAR > END.
4. **Validar contexto**: IF intent requiere estado previo (ej. EJECUTAR sin clasificacion) → redirigir a paso previo necesario.

## Signature Output

```yaml
intent:
  type: "CLASIFICAR"
  confidence: 0.92
  context: "PR #142 config change detectado"
  requires_prior: null
```
