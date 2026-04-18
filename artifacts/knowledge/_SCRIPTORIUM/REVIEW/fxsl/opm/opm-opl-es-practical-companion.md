---
_manifest:
  urn: "urn:fxsl:kb:opm-opl-es-practical-companion"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-03-25"
    source: "synthesis:opm-opl-es,opcloud-tutorial-videos"
version: "0.1.0"
status: draft
tags: [opm, opl-es, spanish, companion, worked-example, implementation-notes]
lang: es
extensions:
  kora:
    family: textbook
    depends_on:
      - "urn:fxsl:kb:opm-corpus-architecture"
      - "urn:fxsl:kb:opm-opl-es"
      - "urn:fxsl:kb:opcloud-tutorial-videos"
---

# OPM OPL-ES Practical Companion

## Definicion

Este companion absorbe contenido practico que no deberia cargar la especificacion base de [OPL-ES](urn:fxsl:kb:opm-opl-es): ejemplos worked-example, decisiones de implementacion bilingue y lineamientos de uso con herramientas.

## Boundary

| Esto vive en... | No vive aqui |
|-----------------|--------------|
| Ejemplos completos en espanol | EBNF formal |
| Casos de naming EN/ES | Taxonomias completas de links |
| Notas de roundtrip y parsing | Semantica base de OPM |
| Uso practico con OPCloud y modelos bilingues | Reescritura de la ISO |

## Companion de Naming

### Procesos

| Idioma | Canon |
|--------|-------|
| EN | gerundio |
| ES | infinitivo |

### Colecciones

| Tipo | EN | ES |
|------|----|----|
| Humanos | Group | Grupo |
| Inanimados | Set | Conjunto |

## Ejemplo Minimo

### SD corto

- Proceso principal ES: `Preparar Empanadas`
- Beneficiario: `Grupo de Comensales`
- Atributo del beneficiario: `Nivel de Satisfaccion`
- Estado input: `insatisfecho`
- Estado output: `satisfecho`

### OPL-ES minimo

```text
Preparar Empanadas cambia Nivel de Satisfaccion de Grupo de Comensales de insatisfecho a satisfecho.
Cocinero maneja Preparar Empanadas.
Preparar Empanadas requiere Horno.
Preparar Empanadas genera Empanada.
```

### OPL-EN equivalente

```text
Preparing Empanadas changes Satisfaction Level of Diner Group from unsatisfied to satisfied.
Cook handles Preparing Empanadas.
Preparing Empanadas requires Oven.
Preparing Empanadas yields Empanada.
```

## Implementacion Bilingue

### Roundtrip

- EN -> ES -> EN DEBERIA preservar la sentencia canonica.
- Las variantes de entrada no canonicas DEBERIAN normalizarse antes del roundtrip.

### Parsing

- El verbo principal sirve como ancla para detectar idioma.
- El modelo semantico DEBE permanecer independiente del idioma de la realizacion OPL.

### Modelos mixtos

- NO se recomiendan por defecto.
- Si una herramienta los permite, DEBE existir una politica explicita de localizacion y normalizacion.

## Uso con OPCloud

- Si la UI esta en ingles, los prompts del wizard NO invalidan las reglas de OPL-ES.
- La herramienta puede generar o mostrar OPL en otros idiomas, pero el canon de OPL-ES sigue viviendo en [OPL-ES](urn:fxsl:kb:opm-opl-es).

## Criterio de Extraccion desde OPL-ES

Un bloque DEBERIA vivir en este companion y no en la spec base cuando:

1. su funcion principal es pedagogica
2. depende de ejemplos largos
3. habla de implementacion de tooling
4. no cambia la gramativa ni la equivalencia semantica
