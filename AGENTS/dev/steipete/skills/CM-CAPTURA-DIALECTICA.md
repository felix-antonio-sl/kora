---
_manifest:
  urn: urn:dev:skill:captura-dialectica:1.0.0
  type: lazy_load_endofunctor
---

## Proposito

Extraer obsesivamente las necesidades del operador mediante diálogo propositivo e iterativo. Nunca bloquear por falta de información — capturar lo mínimo para un primer movimiento.

## Input/Output

- **Input:** Mensaje del operador (idea, necesidad, instrucción parcial, screenshot)
- **Output:** Interpretación estructurada: { intención, incremento_ejecutable, ambigüedades_residuales, propuesta_concreta }

## Procedimiento

1. Leer mensaje del operador. Identificar: verbo (qué quiere), sustantivo (sobre qué), contexto (por qué, para quién).
2. Si el mensaje es claro → formular intención + primer incremento ejecutable.
3. Si el mensaje es ambiguo → NO preguntar en abstracto. Proponer la interpretación más probable: "Entiendo que necesitas [X] que hace [Y] para [Z]. Propongo empezar por [incremento concreto]. Corrijo algo?"
4. Incorporar corrección del operador. Refinar interpretación.
5. Repetir hasta tener intención clara para al menos un incremento ejecutable.
6. Regla de escape: máximo 2 ciclos de captura antes de proponer algo ejecutable. Si después de 2 rondas sigue ambiguo, proponer el incremento más conservador y aprender del resultado.

## Signature Output

```
## Captura
- Intención: [qué necesita Felix]
- Primer incremento: [qué se puede ejecutar ahora]
- Ambigüedades: [qué falta por clarificar, se refinará en incrementos posteriores]
- Propuesta: [interpretación concreta presentada al operador]
```
