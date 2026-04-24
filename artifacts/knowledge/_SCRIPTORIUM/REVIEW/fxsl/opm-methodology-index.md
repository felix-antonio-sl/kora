---
_manifest:
  urn: "urn:fxsl:kb:opm-methodology-index"
  provenance:
    created_by: "FS"
    created_at: "2026-04-23"
    source: "artifacts/knowledge/_SCRIPTORIUM/INBOX/fxsl/opm-methodology/ — 14 archivos de metodologia OPM extraidos y curados desde Dori (2015), material de cursos OpCloud, ISO 19450 y tutoriales"
version: "1.0.0"
status: borrador
tags: [opm, metodologia, dori-2015, iso-19450, opcloud, indice, fxsl]
lang: es
extensions:
  kora:
    family: catalog
---

# OPM Methodology — Indice

Corpus curado de metodologia OPM. Fuentes mezcladas: libro Dori 2015, estandar ISO 19450, cursos OpCloud, tutoriales YouTube y la version personal de Felix.

## Archivos

| Archivo | Fuente / Tema |
|---------|---------------|
| `opm-libro-foundations.md` | Dori 2015 caps 1, 9, 10 — fundamentos MBSE con OPM |
| `opm-libro-sysml.md` | Dori 2015 — OPM <-> SysML crosswalk |
| `opm-libro-complexity-management.md` | Dori 2015 — in-zooming, unfolding, state-expression |
| `opm-libro-dynamic-behavior.md` | Dori 2015 — procesos, transformaciones, state-tracking |
| `opm-libro-structural-relations.md` | Dori 2015 — aggregation, exhibition, generalization, classification |
| `opm-libro-opl-bimodal.md` | Dori 2015 — bimodalidad OPD/OPL |
| `opm-libro-acr-tutorial.md` | Dori 2015 — tutorial ACR (Abstraction, Completeness, Refinement) |
| `opm-iso.md` | ISO 19450 — estandar canonico |
| `opm-opl-es.md` | OPL bilingue con plantillas en espanol |
| `opm-curso-sd-wizard.md` | OpCloud — wizard System Diagram |
| `opm-curso-applied-modeling.md` | OpCloud — applied modeling |
| `opcloud-tutorial-videos.md` | OpCloud — transcripciones tutoriales |
| `opm_youtube.md` | YouTube — tutoriales externos |
| `OPM version felix.md` | Version personal de Felix con anotaciones |

## Proximos pasos

1. Cada archivo puede promoverse individualmente a `urn:fxsl:kb:opm-{slug}` como familia `guide` cuando su curacion este estable.
2. `opm-iso.md` y `opm-opl-es.md` ya tienen equivalentes productivos (`urn:fxsl:kb:opm-iso-19450`, `urn:fxsl:kb:opl-es`); verificar si este material es superconjunto.
3. Cross-link con `urn:fxsl:kb:opm-iso-19450-figuras` (catalogo de figuras) al promover.

## Relacion con el agente productivo

El agente `urn:fxsl:artefacto:opm-specialist` referencia el corpus via `conocimiento_permitido` actual (solo `opm-iso-19450` y `opl-es`); al promover estos archivos se amplia su base de conocimiento.
