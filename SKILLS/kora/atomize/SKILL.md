---
_manifest:
  urn: "urn:kora:skill:atomize:1.0.0"
  type: lazy_load_endofunctor
name: atomize
description: >-
  Productor canonico de la familia documental `atomic` (md-spec v7.1 §5.6,
  knowledge-spec §12). Extrae proposiciones atomicas de carpetas de documentos
  y emite artefactos KORA/MD conformes a `md-spec`, con segmentacion automatica
  (≤5.000 palabras y ≤200 proposiciones por artefacto) y dedup multi-source.
  Output canonico: `KNOWLEDGE/_SCRIPTORIUM/REVIEW/atomic-{slug}.md` (pipeline
  descentralizado v8). Este registro KORA refleja el skill operativo del
  harness Claude Code en `~/.claude/skills/atomize/`.
allowed-tools: Read Glob Write Bash
metadata:
  kora:
    urn: "urn:kora:skill:atomize:1.0.0"
    lifecycle:
      status: active
      created: "2026-04-16"
      updated: "2026-04-16"
    tools: ["Read", "Glob", "Write", "Bash"]
    knowledge:
      - "urn:kora:kb:md-spec"
      - "urn:kora:kb:knowledge-spec"
    composable_with: []
    domain: ["knowledge", "atomic", "koraficacion"]
    level: L1
    external_origin: "~/.claude/skills/atomize/SKILL.md"
---

# Atomize — Productor canonico de la familia `atomic`

## Purpose

Transforma un corpus de documentos humanos en un artefacto KORA/MD de familia
`atomic`, conformado a `md-spec §5.6` y al registro de productores canonicos
de `knowledge-spec §12`. Extrae proposiciones atomicas tipadas, las comprime
preservando FS=100% y las emite en un artefacto direccionable por LLMs como
alternativa a RAG para corpus densos.

Este skill es el **productor canonico de la familia `atomic`**: es la unica
herramienta autorizada para generar artefactos de esa familia cumpliendo sus
invariantes.

## Input / Output

**Input:**
- Path a una carpeta con documentos (.md, .txt, .rst) hasta 3 niveles de
  profundidad.
- Flags opcionales: `--slug`, `--output`, `--legacy`.

**Output canonico (pipeline descentralizado v8):**
- `KNOWLEDGE/_SCRIPTORIUM/REVIEW/atomic-{slug}.md` si el corpus produce
  ≤5.000 palabras y ≤200 proposiciones.
- `KNOWLEDGE/_SCRIPTORIUM/REVIEW/atomic-{slug}-index.md` + N segmentos
  `atomic-{slug}-{NN}.md` si excede los umbrales.

Al promover via `kora promote`, el artefacto migra a `KNOWLEDGE/kora/atomic/`
con `status: published`.

**URNs asignados** (templates, no URNs resolubles):

```
# artefacto unico
urn:kora:kb:atomic-<slug>

# corpus segmentado
urn:kora:kb:atomic-<slug>-index
urn:kora:kb:atomic-<slug>-<NN>
```

**Frontmatter emitido:**
- `status: draft` (pasa por `kora promote` para publicar).
- `extensions.kora.family: atomic`
- `extensions.kora.atomic.producer: "urn:kora:skill:atomize:1.0.0"`
- `extensions.kora.atomic.source_corpus`, `n_propositions`, `segmented`,
  `segment_index`, `total_segments`, `hand_edited`.

## Procedimiento

El procedimiento completo vive en el skill operativo del harness Claude Code:
`~/.claude/skills/atomize/SKILL.md`. Se resume aqui:

1. **Detectar contexto KORA** — buscar ancestros con `KNOWLEDGE/`, `SKILLS/`
   y `specs/` para fijar el output canonico.
2. **Detectar archivos** — hasta 20 archivos directo; chunking interno para
   archivos >5.000 palabras.
3. **Extraer proposiciones** — tipo del enum cerrado (11 tipos),
   autocontenidas, con IDs secuenciales globales.
4. **Comprimir** — abreviaturas de dominio, simbolos, preservar cifras
   y nombres propios.
5. **Dedup multi-source** — consolidar equivalentes; conflictos semanticos
   generan proposiciones `tension` sin perder las originales.
6. **Jerarquizar** — raiz + dominios (H2) + entidades.
7. **Segmentar** si supera umbrales.
8. **Verificacion pre-escritura** — checks `md-spec §6.10` + `§6.11`.
9. **Escribir artefactos** con frontmatter conforme.
10. **Reportar** estadisticas y siguiente paso (`kora index`, `kora check`,
    `kora promote`).

## Signature Output

- Artefactos conformes a `md-spec §5.6` familia `atomic`.
- `## Indice de fuentes` obligatorio.
- Proposiciones con formato `- **Pxxx** · \`tipo\` · texto · [src](...)` o con
  sublista de fuentes en dedup multi-source.
- FS=100% sobre cifras, fechas, excepciones, nombres propios y referencias
  legales.
- IDs `Pxxx` unicos (globalmente en conjunto segmentado).
- `status: draft` en `KNOWLEDGE/_SCRIPTORIUM/REVIEW/`.

## Retrocompatibilidad

El flag `--legacy` produce el formato plano `_ATOMIC_GRAPH.md` sin frontmatter.
Este formato queda **deprecado** por `md-spec §10.4`; solo existe para compat
con consumidores externos mientras se migran.

## Relacion con otros artefactos

- Citado por: `specs/knowledge-spec.md §12.2` como productor canonico de
  familia `atomic`.
- Consume invariantes de: `specs/md-spec.md §5.6` y `§5.6.1`.
- Pipeline de publicacion: atomize -> `KNOWLEDGE/_SCRIPTORIUM/REVIEW/` ->
  `kora check` -> `kora promote` -> `KNOWLEDGE/kora/atomic/`.
