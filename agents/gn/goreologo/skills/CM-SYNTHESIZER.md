---
_manifest:
  urn: "urn:gn:skill:goreologo-synthesizer:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-SYNTHESIZER

## Proposito
Integrar, calibrar y estructurar el analisis GORE en una respuesta clara, operable y bien etiquetada para el usuario.

## Procedimiento
1. Recibir el analisis producido por CM-DOMAIN-ANALYZER.
2. Integrar dimensiones en una narrativa coherente: de lo general (marco) a lo especifico (operacion/contexto Nuble).
3. Calibrar profundidad segun tipo de consulta:
   - Consulta puntual: respuesta directa en 3-5 items.
   - Analisis multidimensional: estructura Concepto → Marco Legal → Proceso → Contexto Nuble → Fuente.
   - Ambigua: tabla comparativa de alternativas + pregunta de clarificacion.
4. Aplicar etiquetas de certeza en cada afirmacion relevante: [norma vigente], [dato institucional], [interpretacion], [incertidumbre].
5. Incluir referencia a fuente oficial (nombre del instrumento, articulo si aplica).
6. Verificar calibracion: chunks <= 5, progresion logica, sin informacion redundante.

## Output
Respuesta final calibrada con estructura visible, etiquetas de certeza, cita de fuente oficial, y nota de incertidumbre si aplica. Lista de recursos adicionales si el tema lo amerita.
