---
_manifest:
  urn: "urn:fxsl:kb:opm-opcloud-operational-guide"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-03-25"
    source: "synthesis:opcloud-tutorial-videos,metodologia-modelamiento-opm,opm-opl-es"
version: "0.1.0"
status: draft
tags: [opcloud, opm, tutorial, operational-guide, workflow, modeling-tool]
lang: es
extensions:
  kora:
    family: tutorial
    depends_on:
      - "urn:fxsl:kb:opm-corpus-architecture"
      - "urn:fxsl:kb:opcloud-tutorial-videos"
      - "urn:fxsl:kb:opm-iso-19450"
      - "urn:fxsl:kb:opm-opl-es"
---

# OPM OPCloud Operational Guide

## Definicion

Esta guia describe como operar OPCloud sin confundir workflow de herramienta con semantica base de OPM. OPCloud implementa y operacionaliza reglas del corpus, pero no las sustituye.

## Regla de Autoridad

| Tema | Autoridad |
|------|-----------|
| Semantica OPM y notacion | [OPM ISO 19450](urn:fxsl:kb:opm-iso-19450) |
| OPL en espanol | [OPL-ES](urn:fxsl:kb:opm-opl-es) |
| UI, wizard, settings, simulation y features de OPCloud | Este artefacto |

## Scope

Esta guia SI cubre:

- SD Wizard
- Navegacion y jerarquia de OPDs
- Settings relevantes para modelado
- Computacion y simulacion en OPCloud
- Requirements modeling en OPCloud
- Model analysis y enforcement terminologico

Esta guia NO cubre:

- Gramatica OPL
- Taxonomias completas de links
- Justificacion semantica profunda de OPM

## SD Wizard

El wizard implementa una secuencia guiada para construir el SD.

### Uso correcto

1. Tomar el wizard como interfaz, no como autoridad semantica.
2. Si el modelo es en espanol, mantener la semantica del wizard pero aplicar naming y OPL segun [OPL-ES](urn:fxsl:kb:opm-opl-es).
3. Si una restriccion del wizard difiere de una regla semantica del corpus, prevalece [OPM ISO 19450](urn:fxsl:kb:opm-iso-19450).

### Mapeo operacional

| Paso UI | Validar contra |
|---------|----------------|
| Main process | ISO 19450 + OPL-ES si `lang: es` |
| Beneficiary group | ISO 19450 + OPL-ES si `lang: es` |
| Beneficiary attribute/states | ISO 19450 |
| Agent/instruments/environment | ISO 19450 |
| System name | ISO 19450 + politica de idioma del corpus |

## Operacion del Modelo

### Jerarquia y navegacion

- OPD Navigator, system map y sub-models son ayudas de navegacion.
- La jerarquia visual NO reemplaza el juicio semantico sobre refinement.
- El modelador DEBE decidir si usa in-zooming o unfolding antes de operar la UI.

### Name coherency y ontology enforcement

- Name coherency sirve para evitar duplicados y visual instances incorrectas.
- Ontology enforcement sirve para higiene terminologica de equipo.
- Ninguna de estas funciones redefine por si sola el canon del corpus.

## Computacion y Simulacion

Cuando el modelo se implementa computacionalmente en OPCloud:

1. Definir atributos computacionales y aliases.
2. Configurar calculos y rangos.
3. Modelar user input, si existe, como workflow de OPCloud y no como regla general de OPM.
4. Verificar visualmente la presencia de `{}` en procesos computacionales dentro de la herramienta.

## Requirements Modeling

En este corpus, requirements en OPCloud se trata como capacidad de herramienta.

Reglas operativas:

- Usar links estructurales, no procedurales
- Usar la convencion `satisfies` si se requiere trazabilidad
- Mantener claro que esto es una practica operacional del modelo en OPCloud

## Model Analysis

Features como `System Map`, `Model Informativeness Grading` y `Identification of Missing Knowledge` deben leerse como instrumentos de inspeccion, no como autoridad semantica.

## Escalacion

Detener la operacion y salir de OPCloud cuando la duda sea:

- el significado de un link
- la legalidad de una estructura OPM
- la surface form correcta en espanol

En esos casos, consultar primero el artefacto de autoridad correspondiente.
