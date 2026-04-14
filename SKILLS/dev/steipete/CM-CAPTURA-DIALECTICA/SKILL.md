---
_manifest:
  urn: urn:dev:skill:captura-dialectica:1.1.2
  type: lazy_load_endofunctor
---

## Proposito

Extraer obsesivamente las necesidades del operador mediante dialogo propositivo e iterativo. Nunca bloquear por falta de informacion — capturar lo minimo para un primer movimiento.

## Input/Output

- **Input:** Mensaje del operador (idea, necesidad, instruccion parcial, screenshot)
- **Output:** Interpretacion estructurada: { intencion, incremento_ejecutable, ambiguedades_residuales, propuesta_concreta }

## Procedimiento

1. Leer mensaje del operador. Identificar: verbo (que quiere), sustantivo (sobre que), contexto (por que, para quien).
2. Si el mensaje es claro → formular intencion + primer incremento ejecutable.
3. Si el mensaje es ambiguo → NO preguntar en abstracto. Proponer la interpretacion mas probable: "Entiendo que necesitas [X] que hace [Y] para [Z]. Propongo empezar por [incremento concreto]. Corrijo algo?"
4. Incorporar correccion del operador. Refinar interpretacion.
5. Repetir hasta tener intencion clara para al menos un incremento ejecutable.
6. Regla de escape: si persiste ambiguedad despues de 2 ciclos propositivos, proponer el incremento mas conservador y aprender del resultado.

## Signature Output

```
## Captura
- Intencion: [que necesita Felix]
- Primer incremento: [que se puede ejecutar ahora]
- Ambiguedades: [que falta por clarificar, se refinara en incrementos posteriores]
- Propuesta: [interpretacion concreta presentada al operador]
```
