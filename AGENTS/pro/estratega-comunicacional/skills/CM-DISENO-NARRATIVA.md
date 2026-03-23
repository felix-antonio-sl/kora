---
_manifest:
  urn: urn:pro:skill:estratega-diseno-narrativa:1.0.0
  type: lazy_load_endofunctor
---

## Proposito

Construir la narrativa comunicacional en 5 dimensiones, produciendo una estructura que ancle toda la comunicacion posterior: posicionamiento, ejes, mensajes clave y prueba de coherencia.

## Input/Output

- **Input:** Diagnostico estrategico previo (o contexto directo del usuario).
- **Output:** NarrativaEstrategica { propuesta_valor, posicionamiento, ejes_narrativos, mensajes_clave, prueba_coherencia }

## Procedimiento

1. **PROPUESTA DE VALOR** — Que ofrece que otros no, en una oracion. Si no hay diferencia real, senalarlo como gap estrategico.
2. **POSICIONAMIENTO** — En que categoria compite y como se diferencia. Marco: categoria + diferencial + audiencia.
3. **EJES NARRATIVOS** — 2-3 temas recurrentes que anclan toda comunicacion. Deben ser sostenibles, verificables y relevantes para stakeholders clave.
4. **MENSAJES CLAVE** — 3-5 afirmaciones para repetir consistentemente. Cada mensaje: idea central + evidencia + conexion emocional.
5. **PRUEBA DE COHERENCIA** — La narrativa resiste contraste con realidad? Testear: lo que decimos vs lo que hacemos vs lo que perciben. Si hay gap, senalarlo.

## Signature Output

```
Narrativa Estrategica:
PROPUESTA DE VALOR: <oracion>
POSICIONAMIENTO: <categoria + diferencial>
EJES NARRATIVOS: 1. <eje> 2. <eje> 3. <eje>
MENSAJES CLAVE: 1. <mensaje> ... 5. <mensaje>
COHERENCIA: <resultado prueba>
```
