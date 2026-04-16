---
name: intent-omega
description: Clasificar consultas complejas en la ruta cognitiva correcta antes de entrar a profundidad. Usar cuando la pregunta sea ambigua, multidimensional o pueda escalar innecesariamente a investigación/arquitectura sin un buen encuadre inicial.
user-invocable: false
---

# Intent Omega

## Procedimiento

1. Leer la consulta completa.
2. Clasificar la ruta dominante:
   - investigacion profunda
   - analisis
   - formalizacion / modelado
   - diseño de sistema
   - base de datos
   - migracion
   - sintesis / encuadre
   - clarificacion previa
3. Identificar si falta contexto crítico.
4. Identificar si la profundidad pedida es proporcional al problema o si conviene empezar más simple.
5. Si la consulta es ambigua, devolver una pregunta breve de encuadre antes de profundizar.

## Salida esperada

- `ruta_dominante`
- `profundidad_inicial_sugerida`
- `contexto_faltante`
- `clarificacion_requerida`
- `motivo`
