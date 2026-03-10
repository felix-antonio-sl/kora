---
_manifest:
  urn: urn:fxsl:skill:opm-specialist-intent-classifier:1.0.0
  type: lazy_load_endofunctor
---

# CM-INTENT-CLASSIFIER

## Proposito
Clasificar la consulta del usuario en dimensiones semanticas de consulta OPM para apoyar un despacho consistente.

## Input/Output
- **Input:** mensaje del usuario (string)
- **Output:** {modo_consulta: concepto|guia|ejemplo|evaluacion, scope_status: dentro_scope|fuera_scope, claridad: suficiente|ambigua, cierre_solicitado: bool, confidence: float, topic: string?}

## Procedimiento
1. Analizar el mensaje del usuario buscando senales lexicas y semanticas.
2. Determinar `modo_consulta` segun patron:
   - `concepto`: pregunta sobre terminologia, definiciones, "que es", "como funciona", "diferencia entre", "explica"
   - `guia`: solicitud de modelado paso a paso, "modelar", "construir SD", "guiame", "quiero crear un modelo"
   - `ejemplo`: solicitud de ejemplo, "ejemplo de", "muestrame", "como se ve", "aplica OPM a"
   - `evaluacion`: solicitud de evaluacion, "preguntame", "quiz", "evalua", "prueba mi conocimiento"
3. Determinar `scope_status`: `fuera_scope` si la solicitud cae fuera de OPM o de la KB autorizada; `dentro_scope` en caso contrario.
4. Determinar `claridad`: `ambigua` si no hay evidencia suficiente para una clasificacion confiable; `suficiente` en caso contrario.
5. Determinar `cierre_solicitado`: `true` si el mensaje expresa cierre, despedida o suficiencia del intercambio; `false` en caso contrario.
6. Retornar la clasificacion compuesta junto con `confidence` y `topic` extraido cuando corresponda.

## Signature Output
```json
{"modo_consulta": "concepto", "scope_status": "dentro_scope", "claridad": "suficiente", "cierre_solicitado": false, "confidence": 0.95, "topic": "effect link"}
```
