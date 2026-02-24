---
_manifest:
  urn: "urn:ops:agent-bootstrap:observer-cm-intent-classifier:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Clasificar la intencion del Operador en una de las categorias del dominio de observabilidad para rutear al estado FSM correcto.

## Input/Output

- **Input:** user_message: string (mensaje del Operador en lenguaje natural)
- **Output:** classification: {intent: MONITOR|ANOMALIA|CORRELACION|DIAGNOSTICO|ALERTA|END, confidence: float, reasoning: string}

## Procedimiento

1. **Extraer senales del mensaje:**
   - Palabras clave de monitoreo: "salud", "estado", "metricas", "como esta", "health", "uptime"
   - Palabras clave de anomalia: "raro", "spike", "subio", "bajo", "anomalia", "inusual", "degradado"
   - Palabras clave de correlacion: "causa", "por que", "deploy", "cambio", "correlacion", "que paso"
   - Palabras clave de diagnostico: "diagnostico", "hipotesis", "que recomiendas", "accion", "rollback"
   - Palabras clave de alerta: "alerta", "notificar", "avisar", "escalar", "configurar alertas"
   - Palabras clave de fin: "gracias", "listo", "terminar", "fin"

2. **Evaluar contexto de sesion:**
   - Si hay anomalia activa y el Operador pregunta "por que" → CORRELACION
   - Si hay correlacion activa y pide accion → DIAGNOSTICO
   - Si pide enviar notificacion → ALERTA

3. **Clasificar con confianza:**
   - Confianza > 80%: rutear directamente
   - Confianza 50-80%: rutear con confirmacion implicita
   - Confianza < 50%: preguntar al Operador

## Signature Output

```yaml
classification:
  intent: "MONITOR"
  confidence: 0.92
  reasoning: "Operador pregunta por estado del sistema. Senales: 'como esta produccion'"
```
