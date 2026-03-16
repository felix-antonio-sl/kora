---
_manifest:
  urn: urn:fxsl:skill:opm-specialist-knowledge-assessor:1.0.0
  type: lazy_load_endofunctor
---

## Proposito
Evaluar la comprension del usuario sobre OPM mediante preguntas de diferentes tipos y niveles, proporcionando feedback formativo.

## Input/Output
- **Input:** modo (generar|evaluar), nivel (basico|intermedio|avanzado), tema opcional (string?), respuesta_usuario opcional (string?), historial_desempeno opcional (string?)
- **Output:** pregunta O evaluacion de respuesta + feedback formativo

## Procedimiento
1. SELECCIONAR tipo de pregunta segun nivel:

   **Basico:**
   - Identificar si algo es objeto o proceso
   - Distinguir objeto fisico de informatico
   - Nombrar los tres tipos de transformacion
   - Reconocer tipos de enlaces basicos

   **Intermedio:**
   - Escribir OPL para un escenario dado
   - Identificar errores en un modelo OPM textual
   - Distinguir entre enlace de efecto y par entrada/salida
   - Clasificar habilitadores (agente vs instrumento)
   - Construir SD para un sistema simple

   **Avanzado:**
   - Modelar comportamiento condicional (condition links, XOR, OR)
   - Aplicar refinamiento (in-zooming vs unfolding)
   - Disenar SD completo con 5 componentes para sistema complejo
   - Identificar estados iniciales, finales, default
   - Manejar multiplicidad y restricciones

2. IF modo=generar → FORMULAR pregunta clara con contexto suficiente
3. IF modo=evaluar → ANALIZAR respuesta_usuario contra el concepto esperado
4. SI modo=evaluar:
   - IF correcta → confirmar, reforzar concepto clave, sugerir aumento de dificultad
   - IF parcial → identificar parte correcta, corregir parte incorrecta con explicacion
   - IF incorrecta → explicar respuesta correcta con referencia a concepto, sugerir mantener nivel
5. AJUSTAR recomendacion de dificultad segun historial_desempeno cuando exista

## Signature Output
Pregunta en Markdown + evaluacion (correcto|parcial|incorrecto) + feedback formativo.
