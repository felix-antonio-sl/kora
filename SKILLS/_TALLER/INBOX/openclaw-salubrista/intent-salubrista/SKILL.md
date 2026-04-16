---
name: intent-salubrista
description: Clasificar consultas de salud publica o sistemas de salud por intencion dominante, escala operativa, objeto y producto esperado, y decidir si deben derivar a especializacion en hospitalizacion o HD antes de profundizar. Usar como dispatcher general del agente.
---

# Intent Salubrista

## Procedimiento

1. Leer la consulta completa.
2. Determinar intencion dominante, escala principal, objeto operativo y producto esperado si aplica.
3. Detectar si la consulta debe derivar a hospitalizacion o HD.
4. Si falta informacion minima para distinguir escala o intencion, devolver `clarificacion_requerida = true` y explicar el minimo faltante.

## Salida esperada

- `intencion_dominante`
- `escala`
- `objeto`
- `tipo_producto`
- `derivar_a_hospitalizacion`
- `clarificacion_requerida`
