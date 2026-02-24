---
_manifest:
  urn: "urn:ops:skill:verificador-intent-classifier:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Clasificar la intencion del Operador en el contexto de verificacion para dirigir a la rama FSM correcta. Mapear input libre a uno de los intents validos del verificador.

## Input/Output

- **Input:** user_message: string, current_state: FSM_State
- **Output:** intent: {type: VERIFICAR|CAPA_CI|CAPA_REGRESION|CAPA_DIVERSIDAD|CAPA_SEGURIDAD|CAPA_HUMANA|END, confidence: float, context: string}

## Procedimiento

1. **Extraer** tokens clave del mensaje: PR, changeset, verificar, lint, types, tests, regresion, diversidad, seguridad, humano, aprobar, rechazar, resumen.
2. **Mapear** a intent:
   - Tokens verificar, PR, cambio, completo, orquestar, 5 capas → VERIFICAR
   - Tokens lint, types, tests, CI, unitarios, build → CAPA_CI
   - Tokens regresion, dataset, degradacion, golden, anchor → CAPA_REGRESION
   - Tokens diversidad, cross-eval, provider, modelo diferente, reviewer → CAPA_DIVERSIDAD
   - Tokens seguridad, SAST, DAST, privilegios, OWASP, vulnerabilidad → CAPA_SEGURIDAD
   - Tokens humano, aprobar, gate, destructivo, aprobacion, operador → CAPA_HUMANA
   - Tokens terminar, fin, resumen, listo → END
3. **Resolver ambiguedad**: IF multiples intents → priorizar por contexto de sesion: IF capas en progreso → siguiente capa pendiente. IF sin contexto → VERIFICAR (orquestacion completa).
4. **Validar contexto**: IF intent requiere estado previo (ej. CAPA_DIVERSIDAD sin CI ejecutado) → redirigir a capa prerequisito.

## Signature Output

```yaml
intent:
  type: "VERIFICAR"
  confidence: 0.94
  context: "PR #210 detectado, orquestacion completa solicitada"
  requires_prior: null
```
