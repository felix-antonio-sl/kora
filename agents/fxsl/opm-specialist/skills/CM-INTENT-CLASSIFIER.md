---
_manifest:
  urn: urn:fxsl:skill:opm-specialist-intent-classifier:1.0.0
  type: lazy_load_endofunctor
---

# CM-INTENT-CLASSIFIER

## Proposito
Clasificar la intencion del usuario en categorias semanticas de consulta OPM para producir un despacho consistente.

## Input/Output
- **Input:** mensaje del usuario (string)
- **Output:** {intent: concepto|guia|ejemplo|evaluacion|terminar|fuera_scope|ambiguo, confidence: float, topic: string?}

## Procedimiento
1. Analizar el mensaje del usuario buscando senales lexicas y semanticas.
2. Clasificar segun patron:
   - `concepto`: pregunta sobre terminologia, definiciones, "que es", "como funciona", "diferencia entre", "explica"
   - `guia`: solicitud de modelado paso a paso, "modelar", "construir SD", "guiame", "quiero crear un modelo"
   - `ejemplo`: solicitud de ejemplo, "ejemplo de", "muestrame", "como se ve", "aplica OPM a"
   - `evaluacion`: solicitud de evaluacion, "preguntame", "quiz", "evalua", "prueba mi conocimiento"
   - `terminar`: despedida, "terminar", "gracias", "suficiente"
3. Si la solicitud cae fuera de OPM o de la KB autorizada, clasificar como `fuera_scope`.
4. Si no hay evidencia suficiente para una clasificacion confiable, clasificar como `ambiguo`.
5. Retornar `intent`, `confidence` y `topic` extraido cuando corresponda.

## Signature Output
```json
{"intent": "concepto", "confidence": 0.95, "topic": "effect link"}
```
