---
_manifest:
  urn: "urn:fxsl:skill:pensador-generador-navegador-tensiones:2.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Identificar las tensiones dialecticas subyacentes en cualquier problema. Motor MBT: usa tensiones como semillas generativas o criticas.

## I/O

- **Input:** Discurso del usuario sobre lo que modela/analiza, contexto del problema
- **Output:** Tensiones identificadas, clasificadas por categoria (A1-A4), formuladas como preguntas explicitas

## Procedimiento

1. Escuchar el discurso del usuario sobre lo que modela/analiza
2. Identificar tensiones implicitas que estan siendo navegadas
3. Clasificar en categoria: A1-SER, A2-DEVENIR, A3-CONOCER, A4-EXPRESAR
4. Formular pregunta que haga explicita la tension
5. Usar la tension como semilla generativa o critica

Taxonomia de tensiones:

A1-SER (Ontologicas):
- Entidad <-> Evento
- Concreto <-> Abstracto
- Token <-> Type
- Todo <-> Partes
- General <-> Particular
- Simetrico <-> Asimetrico

A2-DEVENIR (Dinamicas):
- Estatico <-> Dinamico
- Instantaneo <-> Durativo
- Secuencial <-> Paralelo
- Causa <-> Efecto
- Agente <-> Paciente
- Determinista <-> Probabilista

A3-CONOCER (Epistemologicas):
- Conocido <-> Desconocido
- Cierto <-> Incierto
- Hecho <-> Supuesto
- Explicito <-> Tacito
- Situado <-> Universal

A4-EXPRESAR (Semioticas):
- Visual <-> Textual
- Formal <-> Informal
- Compacto <-> Verboso
- Prescriptivo <-> Descriptivo
- Detalle <-> Abstraccion
- Modular <-> Monolitico

## Signature Output

Tension identificada: [Polo A] <-> [Polo B] (Categoria: [A1-A4]). Pregunta que hace explicita la tension. Implicacion de cada polo.
