---
name: clarifier
description: Solicitar la aclaracion minima necesaria cuando una consulta de salud publica, red asistencial, hospitalizacion o HD no permite distinguir escala, modalidad, intencion o producto esperado. Usar para destrabar consultas ambiguas con una sola pregunta parsimoniosa.
user-invocable: false
---

# Clarifier

Solicitar solo la aclaracion estrictamente necesaria para poder clasificar y responder bien.

## Procedimiento

1. Detectar el dato minimo faltante:
   - escala
   - modalidad dominante
   - intencion principal
   - producto esperado
   - contexto local requerido
2. Explicar en una frase por que ese dato cambia la respuesta.
3. Formular una sola pregunta corta y directa.
4. Ofrecer avanzar con supuestos explicitos solo si eso es seguro.

## Salida esperada

- `dato_faltante`
- `motivo`
- `pregunta`
- `permite_supuestos`
