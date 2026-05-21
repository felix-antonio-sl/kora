---
_manifest:
  urn: "urn:kora:kb:handoff-2026-05-21-colapso-familias-documentales"
  provenance:
    created_by: "Claude Opus 4.7"
    created_at: "2026-05-21"
    source: "Directiva HITL operador 2026-05-21: 'Lo de las familias documentales no esta muy inflado? Colapsemos aun mas'"
version: "1.0.0"
status: publicado
tags: [handoff, familias-documentales, colapso, convergencia, md-spec-v12]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:adr-colapso-familias-documentales-2026-05-21"
    - "urn:kora:kb:md-spec"
    - "urn:kora:kb:adr-poda-radical-2026-05-21"
---

# Handoff — Colapso radical de familias documentales (2026-05-21)

## Resumen ejecutivo

Tras la poda radical de la mañana, el operador audito la taxonomia
de familias documentales y detecto inflado. Auditoria sobre 579
artefactos productivos:

- 15 familias declaradas en `md-spec v11`.
- `note` (catch-all) cubre 32% del corpus.
- 4 familias con <= 3 declaraciones (`glossary` 1, `inventory` 3,
  `organigram` 2, `cq_catalog` 0).
- `guide` y `faq` con invariantes practicamente intercambiables.
- `cq_catalog` con 0 declaraciones (subperfil ornamental).
- Solo `spec` y `adr` tenian invariantes diferenciales fuertes
  verificables.

Decision (`urn:kora:kb:adr-colapso-familias-documentales-2026-05-21`):
colapso a **2 familias canonicas + 2 auxiliares = 4 familias**.

## Que se hizo

### Capa doctrinal

- **md-spec v11.0.0 → v12.0.0** (`urn:kora:kb:md-spec`):
  - §5.6 reescrita: tabla canonica de 11 → 2 entradas (`spec`, `note`);
    tabla auxiliar de 4 → 2 entradas (`source`, `bok`).
  - Nueva sub-seccion "Sub-shapes opcionales sobre `note`": `adr`
    se promueve a sub-shape opt-in via presencia de
    `extensions.kora.adr.*` en frontmatter.
  - §5.6.1 (perfil `spec` delegado a spec-md) se preserva sin
    cambios.
  - §9 tabla validacion: fila "Resumen obligatorio por familia"
    reemplazada por "Sub-shape ADR conforme".
  - §10.0 nuevo: contrato vigente v12 con migracion documentada.
  - Frontmatter source extendido + version bump major.

- **ADR canonico**:
  `artifacts/knowledge/kora/adr/adr-colapso-familias-documentales-2026-05-21.md`
  publicado en zona productiva con factorizacion categorica:
  `decision = colapsar_a_2_canonicas ∘ promover_adr_a_shape_opt_in ∘
  migrar_270_artefactos_a_note ∘ preservar_invariantes_reales_en_extensions`.

### Capa de toolchain

- `toolchain/kora_lib/validation.py`:
  - `VALID_FAMILIES` reducida a `{"spec", "note", "source", "bok"}`
    (era 16 entradas con atomic ya retirado; ahora 4).
  - `FAMILY_MAX_LINES_PER_PRIMARY_CHUNK`, `FAMILY_MAX_TOTAL_LINES_BEFORE_SPLIT`,
    `FAMILY_MAX_PRIMARY_SECTIONS_PER_FILE`: 11 entradas → 4. Clave
    `"note"` reemplaza a `"generic"` como entrada del fallback.
  - `resolve_document_family`: default cambia de `"generic"` a `"note"`.
  - `resolve_max_total_lines_per_file` y `resolve_max_primary_sections_per_file`:
    lookup default usa `"note"`.

### Capa de artefactos

- **289 artefactos productivos** con `family:` actualizada:
  - `guide` → `note`: 86
  - `faq` → `note`: 86
  - `normative` → `note`: 65
  - `catalog` → `note`: 22
  - `generic` → `note`: 9
  - `adr` → `note`: 7 (`extensions.kora.adr.*` preservado)
  - `source-alias` → `source`: 6
  - `inventory` → `note`: 3
  - `organigram` → `note`: 2
  - `glossary` → `note`: 1
  - `normative-technical` → `note`: 1
  - `record` → `note`: 1

- Ninguno se movio de directorio. La estructura tematica de
  `artifacts/knowledge/*/` se preserva como discriminacion fina
  (la familia ya no la captura, los directorios y tags si).

### Capa de tests

- `tests/test_artifacts.py::test_md_spec_restores_koraficacion_contract`:
  expectativas actualizadas (v11 → v12, agregado "Contrato vigente v12").
- `tests/test_semantic_validation.py::test_split_kora_markdown_parts_splits_large_note_body`:
  renombrado de `..._normative_body`; cuerpo escalado a 15 secciones
  para superar el nuevo `max_total=320` de `note`.
- Refs `family: normative` en test_semantic_validation.py reemplazadas
  por `family: note` (3 ocurrencias).

## Validacion

| Check | Resultado |
|-------|-----------|
| `kora index` | 697 artefactos indexados (13 deprecated/retired skipped) |
| `kora check --strict` | 27/29 verdes. Los 2 restantes son **preexistentes** y NO los introdujo este cambio: (a) HIGH `HANDOFF.md` con `status: handoff` en zona productiva — WIP del operador; (b) MEDIUM `spec-procedure-coherence` en un handoff archivado (refs a flag legacy `--artefacto`). |
| Suite tests | 332/332 verdes |

## Tradeoff aplicado

**Se pierde**: granularidad nominal de 11 sub-familias. Distinciones
"este es un FAQ", "este es un glosario", "este es un catalogo" ya no
se capturan en `family:` — viven ahora en `tags`, estructura de
directorios, o en la lectura humana del titulo. Invariantes blandos
como "## Resumen recomendado" o "## por pregunta" se vuelven
convencion editorial, no contrato verificable.

**Se gana**: 15 → 4 familias. La taxonomia deja de pretender
clasificacion exhaustiva y captura solo la distincion ontologica
real: **regimen documental** (descriptivo vs prescriptivo) + tipo
crudo (material fuente). El catalogo se vuelve honesto sobre lo que
discrimina.

## Doctrina nueva

**Familias declarables** (4):
- `spec`: descriptivo + prescriptivo (cumple md-spec + spec-md).
- `note`: descriptivo (catch-all).
- `source`: material crudo.
- `bok`: corpus grande (derivacion por URN/tags, no se declara).

**Sub-shape `adr`**: activado por presencia de `extensions.kora.adr.*`
en frontmatter de un `note`. Mantiene el contrato estructural
completo (5 campos obligatorios + 5 secciones de body + factorizacion
categorica explicita). Esto es categorialmente mas limpio que
declarar una family separada para 6-7 ADRs: shape por presencia de
campos, no por etiqueta.

## Lo que sigue intacto

- 41 agents/skills productivos.
- 4 runtime-extensions canonicas (claude-code/codex/openclaw/hermes).
- 9 specs activas (gobernanza, harness-spec, qa-spec, risk-register,
  autoria-spec v2.0, md-spec v12.0, spec-md v1.0, knowledge-spec v3.0,
  runtime-spec-md, transmutation-spec, multiagente-spec).
- 6 ADRs canonicos en `artifacts/knowledge/kora/adr/`.
- WIP del operador (hodom glosario + hermes-agent-specialist) sin
  tocar.
- INBOX pre-categorial (excluido de checks): los `family: ssot`,
  `family: tutorial`, `family: curation-inventory` siguen alli como
  estaban (deuda preexistente, no introducida por este cambio).

## Riesgos abiertos

- **Catalog navegable mas plano**: queries sobre "todos los catalogos"
  o "todos los FAQs" ya no funcionan via `family:`. Si esa
  discriminacion vuelve a hacer falta, el camino correcto es `tags:`
  o convencion de directorio, no resucitar familias.
- **Refs en handoffs antiguos** a familias retiradas siguen valiendo
  como historia (los handoffs viven en archive; no se tocan).

## Pendientes

Ninguno doctrinal. Sin nuevos frentes abiertos. Si el operador valida,
se cierra con commit + push.
