---
_manifest:
  urn: "urn:fxsl:kb:notas-reencuadre-opm-2026-04-14"
  provenance:
    created_by: "FS"
    created_at: "2026-04-23"
    source: "artifacts/knowledge/_SCRIPTORIUM/INBOX/fxsl/NOTAS-REENCUADRE-2026-04-14.md — decision editorial del reencuadre del corpus OPM ES como adaptacion canonica autocontenida en espanol"
version: "1.0.0"
status: borrador
tags: [opm, editorial, reencuadre, corpus-es, fxsl]
lang: es
extensions:
  kora:
    family: adr
---

---
title: "Reencuadre editorial del corpus OPM ES"
summary: "Decision editorial de presentar el corpus como adaptacion canonica en espanol de OPM con capas internas autocontenidas"
date: 2026-04-14
---

# Reencuadre Editorial OPM ES

## Decision

Desde esta fecha, `opm-ssot-es` se presenta como una adaptacion canonica en espanol de OPM.

El corpus deja de hablar desde la procedencia de sus materiales y pasa a hablar desde sus propias capas internas:

- `opm-es`: nucleo conceptual
- `opl-es`: capa textual canonica
- `opd-es`: capa visual canonica
- `manual-metodologico-opm-es`: practica, heuristica y operacion

## Alcance del cambio

- Se eliminaron referencias explicitas de procedencia a fuentes externas en las cinco piezas nucleares del corpus.
- Se mantuvieron los nombres historicos de archivo para no romper referencias internas del repo.
- Se actualizaron URNs, dependencias y contratos editoriales para que la autoridad del corpus quede autocontenida.

## Criterios editoriales adoptados

- El nucleo conserva la ontologia y las restricciones semanticas de OPM.
- OPL se trata como realizacion canonica en espanol, no como traduccion comentada.
- OPD se trata como gramatica visual propia del corpus, no como aparato de citas.
- El manual metodologico absorbe heuristicas, gobernanza, computacion, requisitos y patrones operativos como conocimiento natural del corpus.

## Delimitaciones activas

- La capa base no fija politica detallada de superficie textual ni geometria exhaustiva.
- La capa textual no gobierna decisiones de layout o navegacion visual.
- La capa visual no gobierna politica terminologica.
- El manual metodologico puede extender practica y operacion, pero no redefinir semantica de `opm-es`.

## Correcciones relevantes

- El `Mapa del Sistema` queda descrito como indice navegable del contenido de cada OPD, incluyendo cosas y enlaces.
- La columna de autoridad del manual deja de depender de etiquetas de procedencia externa y pasa a usar capas propietarias del corpus.
- Las notas sobre computacion, trazabilidad de requisitos y operaciones de herramienta se normalizan como guia metodologica general.

## Verificacion

Busqueda final sin residuos explicitos en `*.md` del corpus para:

- `ISO`
- `ISO/PAS`
- `Annex`
- `Anexo`
- `OPCloud`
- `Dori`
- `provenance`
- `source:`
