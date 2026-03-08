---
_manifest:
  urn: "urn:fxsl:skill:opm-specialist-intent-classifier:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Clasificar el intent del usuario en una de las categorias del FSM de opm-specialist para producir una salida de despacho consistente.

## Input/Output

- **Input:** mensaje del usuario (string)
- **Output:** {intent: CONCEPT|GUIDE|EXAMPLE|ASSESS|END|AMBIGUO, confidence: float, topic: string?}

## Procedimiento

1. ANALIZAR mensaje del usuario buscando senales lexicas
2. CLASIFICAR segun patron:
   - CONCEPT: pregunta sobre terminologia, definiciones, "que es", "como funciona", "diferencia entre", "explica"
   - GUIDE: solicitud de modelado paso a paso, "modelar", "construir SD", "guiame", "quiero crear un modelo"
   - EXAMPLE: solicitud de ejemplo, "ejemplo de", "muestrame", "como se ve", "aplica OPM a"
   - ASSESS: solicitud de evaluacion, "preguntame", "quiz", "evalua", "prueba mi conocimiento"
   - END: despedida, "terminar", "gracias", "suficiente"
3. IF no hay evidencia suficiente → clasificar como AMBIGUO
4. RETORNAR intent + topic extraido

## Signature Output

```json
{"intent": "CONCEPT", "confidence": 0.95, "topic": "effect link"}
```
