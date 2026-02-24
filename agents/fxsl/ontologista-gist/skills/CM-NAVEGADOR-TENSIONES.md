---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:ontologista-gist-cm-navegador-tensiones:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Identificar tensiones dialecticas generales en el discurso del usuario. Heredado del Pensador-Generador. Usado como semilla generativa para alternativas de modelado.

## Input/Output

- **Input:** Discurso del usuario, problema de modelado
- **Output:** Tensiones identificadas, clasificadas y formuladas como preguntas generativas

## Procedimiento

1. Escuchar el discurso del usuario
2. Identificar tensiones implicitas
3. Clasificar en taxonomia:

**A1_SER:**
- Entidad ↔ Evento
- Concreto ↔ Abstracto
- Token ↔ Type
- Todo ↔ Partes

**A2_DEVENIR:**
- Estatico ↔ Dinamico
- Instantaneo ↔ Durativo
- Secuencial ↔ Paralelo

**A3_CONOCER:**
- Conocido ↔ Desconocido
- Cierto ↔ Incierto
- Explicito ↔ Tacito

**A4_EXPRESAR:**
- Formal ↔ Informal
- Compacto ↔ Verboso
- Detalle ↔ Abstraccion

4. Formular pregunta explicitadora
5. Usar como semilla generativa para alternativas

## Signature Output

```
TENSION: {polo_A} ↔ {polo_B}
CATEGORIA: {A1_SER|A2_DEVENIR|A3_CONOCER|A4_EXPRESAR}
PREGUNTA: {pregunta explicitadora}
```
