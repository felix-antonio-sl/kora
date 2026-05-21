---
_manifest:
  urn: "urn:fxsl:kb:opm-libro-curado-index"
  provenance:
    created_by: "FS"
    created_at: "2026-04-23"
    source: "artifacts/knowledge/_SCRIPTORIUM/INBOX/opm-libro-curado/ — 24 capitulos curados del libro Dori (2015) Model-Based Systems Engineering with OPM and SysML"
version: "1.0.0"
status: borrador
tags: [opm, libro-curado, dori-2015, mbse, sysml, indice, fxsl]
lang: es
extensions:
  kora:
    family: note
---

# OPM Libro Curado — Indice

Curacion capitulo-a-capitulo del libro de Dov Dori (2015): *Model-Based Systems Engineering with OPM and SysML*. Springer.

## Composicion

Material fuente pre-categorial en `artifacts/knowledge/_SCRIPTORIUM/INBOX/opm-libro-curado/`, 24 archivos organizados por capitulo:

| Archivo | Contenido |
|---------|-----------|
| `00-preface.md` | Preface — Quest for simplicity, advent of computers, OPM vision |
| `01-chapter-01.md` | Ready to Start Modeling? (Box quote; modelos y utilidad) |
| `02-chapter-02.md` | (contenido por confirmar) |
| `03-chapter-03.md` | (contenido por confirmar) |
| `04-chapter-04.md` | (contenido por confirmar) |
| `05-chapter-05.md` | (contenido por confirmar) |
| `06-chapter-06.md` | (contenido por confirmar) |
| `07-chapter-07.md` | (contenido por confirmar) |
| `08-chapter-08.md` | (contenido por confirmar) |
| `09-chapter-09.md` | Conceptual Modeling: Purpose and Context (referenciado en opm-methodology) |
| `10-chapter-10.md` | Things: Objects and Processes (referenciado en opm-methodology) |
| `11-chapter-11.md` | (contenido por confirmar) |
| `12-chapter-12.md` | (contenido por confirmar) |
| `13-chapter-13.md` | (contenido por confirmar) |
| `14-chapter-14.md` | (contenido por confirmar) |
| `15-chapter-15.md` | (contenido por confirmar) |
| `16-chapter-16.md` | (contenido por confirmar) |
| `17-chapter-17.md` | (contenido por confirmar) |
| `18-chapter-18.md` | (contenido por confirmar) |
| `19-chapter-19.md` | (contenido por confirmar) |
| `20-chapter-20.md` | (contenido por confirmar) |
| `21-chapter-21.md` | (contenido por confirmar) |
| `22-chapter-22.md` | (contenido por confirmar) |
| `23-chapter-23.md` | (contenido por confirmar) |
| `24-chapter-24.md` | (contenido por confirmar) |

## Proximos pasos

1. Ejecutar `atomize` sobre los 24 archivos para emitir familia `atomic` con proposiciones direccionables (output en `_SCRIPTORIUM/REVIEW/kora/atomic/`).
2. Si la curacion es estable, promover cada capitulo a `artifacts/knowledge/fxsl/opm-libro-curado/` como familia `guide` bajo el regimen `urn:fxsl:kb:opm-libro-cap-NN`.
3. Cross-link con `urn:fxsl:kb:icas-*` donde el capitulo toque composicion, representacion o agencia.

## Relacion con el corpus existente

- `urn:fxsl:kb:opm-iso-19450` — estandar canonico (capa normativa).
- `urn:fxsl:kb:opl-es` — OPL bilingue.
- `urn:fxsl:kb:opm-iso-19450-figuras` — catalogo de figuras (en REVIEW).
- `artifacts/knowledge/_SCRIPTORIUM/INBOX/fxsl/opm-methodology/` — material de metodologia curado del mismo libro; contiene `opm-libro-foundations.md`, `opm-libro-sysml.md`, `opm-libro-complexity-management.md`, `opm-libro-dynamic-behavior.md`, `opm-libro-structural-relations.md`, `opm-libro-acr-tutorial.md`, `opm-libro-opl-bimodal.md`.
