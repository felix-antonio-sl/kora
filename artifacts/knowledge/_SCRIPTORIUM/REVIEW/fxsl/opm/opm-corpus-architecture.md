---
_manifest:
  urn: "urn:fxsl:kb:opm-corpus-architecture"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-03-25"
    source: "synthesis:opm-iso-19450,opm-opl-es,metodologia-modelamiento-opm,opcloud-tutorial-videos"
version: "0.1.0"
status: draft
tags: [opm, corpus-architecture, ssot, curation, information-architecture, artifact-boundaries]
lang: es
extensions:
  kora:
    family: specification
    depends_on:
      - "urn:fxsl:kb:opm-iso-19450"
      - "urn:fxsl:kb:opm-opl-es"
      - "urn:fxsl:kb:metodologia-modelamiento-opm"
      - "urn:fxsl:kb:opcloud-tutorial-videos"
---

# OPM Corpus Architecture

## Resumen

Este draft define la arquitectura documental objetivo del corpus OPM cuando el set minimo publicado se apoya en cuatro piezas: [OPM ISO 19450](urn:fxsl:kb:opm-iso-19450), [OPL-ES](urn:fxsl:kb:opm-opl-es), [Metodologia de Modelamiento OPM](urn:fxsl:kb:metodologia-modelamiento-opm) y [OPCloud Tutorial Videos](urn:fxsl:kb:opcloud-tutorial-videos). El objetivo es eliminar SSOT duplicado, fijar precedencia y preparar una reparticion limpia hacia artefactos mas estrechos.

## Precedencia

| Nivel | Artefacto | Autoridad |
|------|-----------|-----------|
| 1 | `urn:fxsl:kb:opm-iso-19450` | Semantica OPM, notacion, dinamica, ejecucion, naming EN, procedimiento base del SD |
| 2 | `urn:fxsl:kb:opm-opl-es` | Realizacion OPL en espanol, decisiones lexicas EN -> ES, roundtrip y restricciones de surface form |
| 3 | `urn:fxsl:kb:metodologia-modelamiento-opm-protocolo` | Protocolo de modelamiento, decisiones de fase, heuristicas y gates de validacion |
| 4 | `urn:fxsl:kb:opm-opcloud-operational-guide` | Workflows de herramienta, capacidades UI, limitaciones y operacion en OPCloud |
| 5 | `urn:fxsl:kb:opm-opl-es-practical-companion` | Ejemplos, companion practice y notas de implementacion derivadas de OPL-ES |

## Reglas de Borde

### ISO 19450

- SIEMPRE retiene definiciones, taxonomias completas, semantica de links, simulacion base, guidance de naming EN y procedimiento base del SD.
- NUNCA delega su semantica a una herramienta.

### OPL-ES

- SIEMPRE retiene gramatica, reglas de transformacion, equivalencia semantica y convenciones de realizacion en espanol.
- PUEDE incluir ejemplos minimos solo si sirven a la gramatica.
- NO DEBERIA cargar tutoriales largos, operacion de herramienta ni ejemplos worked-example extensos.

### Metodologia-Protocolo

- SIEMPRE retiene secuencia de trabajo, arboles de decision, anti-patterns, heuristicas, gates de validacion y reglas de precedencia entre artefactos.
- PUEDE resumir semantica solo cuando sea estrictamente necesaria para una decision operativa.
- NO DEBERIA replicar taxonomias completas, EBNF, ni walkthroughs de UI.

### OPCloud Operational Guide

- SIEMPRE retiene wizard flows, jerarquia de OPDs, constraints de UI, features de computacion, requirements, settings y analysis features.
- DEBE marcar explicitamente cuando una regla proviene de ISO o de OPL-ES.
- NO DEBERIA presentarse como fuente primaria de semantica OPM.

### OPL-ES Practical Companion

- SIEMPRE retiene ejemplos worked-example, decisiones de implementacion bilingue y uso practico.
- NO DEBERIA redefinir la gramatica formal.

## Receptores Draft

| URN draft | Rol objetivo |
|----------|--------------|
| `urn:fxsl:kb:metodologia-modelamiento-opm-protocolo` | Receptor del protocolo limpio |
| `urn:fxsl:kb:opm-opcloud-operational-guide` | Receptor de contenido tool-specific |
| `urn:fxsl:kb:opm-opl-es-practical-companion` | Receptor de ejemplo y notas practicas de OPL-ES |

## Matriz de Migracion

| Origen actual | Bloque | Destino recomendado | Accion |
|--------------|--------|---------------------|--------|
| `metodologia-modelamiento-opm` | Definiciones, fundamentos, principios base | ISO 19450 via referencia | Comprimir a resumen corto o reemplazar por cross-ref |
| `metodologia-modelamiento-opm` | SD, SD1, complejidad, heuristicas, gates | Metodologia-Protocolo | Conservar y adelgazar |
| `metodologia-modelamiento-opm` | Ontology enforcement, system map, grading, requirements OPCloud, user input, stereotypes | OPCloud Operational Guide | Extraer |
| `opm-opl-es` | Ejemplo completo de empanadas | OPL-ES Practical Companion | Extraer |
| `opm-opl-es` | Notas de implementacion bilingue y OPCloud localization | OPL-ES Practical Companion | Extraer |
| `opcloud-tutorial-videos` | Afirmaciones semanticas dispersas | Mantener en tutorial con cita a ISO/OPL-ES | Encapsular |

## Criterio de Publicacion

Un artefacto esta listo para subir a `KNOWLEDGE/` solo si cumple simultaneamente:

1. Tiene un rol unico y no intercambiable con otro artefacto del corpus.
2. Su dependencia de autoridad queda explicita en frontmatter y en el cuerpo.
3. No reescribe taxonomias completas ya presentes en ISO u OPL-ES.
4. No mezcla semantica base con operacion de herramienta.
5. Pasa lint y la lectura cruzada no genera conflictos de precedencia.

## Orden de Ejecucion

1. Publicar arquitectura del corpus.
2. Publicar metodologia-protocolo.
3. Publicar guia operacional OPCloud.
4. Publicar companion practico de OPL-ES.
5. Recien entonces adelgazar los publicados actuales sin perdida de FS.
