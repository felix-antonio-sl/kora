---
_manifest:
  urn: "urn:kora:kb:adr-colapso-familias-documentales-2026-05-21"
  provenance:
    created_by: "Claude Opus 4.7"
    created_at: "2026-05-21"
    source: "Directiva HITL operador 2026-05-21: 'Lo de las familias documentales no esta muy inflado? Colapsemos aun mas'. Auditoria con grep sobre artefactos productivos."
version: "1.0.0"
status: publicado
tags: [adr, familias-documentales, colapso, convergencia, simpleza]
lang: es
extensions:
  kora:
    family: note
    adr:
      contexto: "Auditoria de uso real de familias documentales en 579 artefactos productivos: 4 familias tienen <=3 declaraciones (glossary, inventory, organigram, cq_catalog); cq_catalog tiene 0; guide y faq tienen invariantes practicamente intercambiables; note (catch-all) cubre 32%. Categoria de 'familia documental' inflada: la mayoria son taxonomia decorativa sin invariantes diferenciales operacionales. md-spec v11 declara 11 canonicas + 4 auxiliares = 15. La distincion ontologica real es regimen (descriptivo vs prescriptivo) + material crudo."
      alternativas:
        - "Status quo: 15 familias con invariantes blandos para la mayoria"
        - "Poda intermedia: retirar las 4 sub-1% pero mantener guide/faq/normative/catalog (6-7 canonicas)"
        - "Colapso radical: 2 canonicas (spec, note) + 2 auxiliares (source, bok); adr como sub-shape opt-in (elegida)"
      factorizacion_elegida: "decision = colapsar_a_2_canonicas ∘ promover_adr_a_shape_opt_in ∘ migrar_270_artefactos_a_note ∘ preservar_invariantes_reales_en_extensions"
      consecuencias:
        - "15 familias → 4 (2 canonicas + 2 auxiliares)"
        - "270 artefactos productivos cambian family declarada (mecanico, no se mueven)"
        - "adr deja de ser family — se enforce por presencia de extensions.kora.adr.*"
        - "guide/faq/normative/catalog/glossary/inventory/organigram/cq_catalog → note"
        - "source-alias → source"
        - "generic (fallback) → note (fallback)"
        - "md-spec v11 → v12 (major bump por reduccion drastica de la taxonomia)"
        - "VALID_FAMILIES en validation.py se reduce a {spec, note, source, bok}"
        - "FAMILY_MAX_* mappings consolidados"
      estado: aceptada
relations:
  cites:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:md-spec"
    - "urn:kora:kb:spec-md"
    - "urn:kora:kb:adr-poda-radical-2026-05-21"
  refines:
    - "urn:kora:kb:adr-poda-radical-2026-05-21"
---

# ADR — Colapso radical de familias documentales

## Contexto

Directiva HITL del operador (2026-05-21):

> "Lo de las familias documentales no esta muy inflado? Colapsemos aun mas."

Auditoria con grep sobre 579 artefactos productivos en
`artifacts/knowledge/` + capas normativas:

| Familia | Declarados | Diagnostico |
|---------|------------|-------------|
| `note` | 187 (32%) | catch-all genuino |
| `guide` | 86 (15%) | invariante muy blando ("## Resumen recomendado") |
| `faq` | 86 (15%) | invariante blando ("## por pregunta") |
| `normative` | 71 (12%) | invariantes editoriales (condiciones → tablas), pero T1-T7 de md-spec §5.4 ya capturan lo mismo |
| `spec` | 35 (6%) | invariantes prescriptivos fuertes via spec-md |
| `source` (aux) | 43 | usada por convencion `fuentes/` |
| `catalog` | 22 (4%) | invariantes tabulares razonables, pero el shape se puede expresar via convencion de body |
| `generic` (aux) | 18 | fallback del toolchain |
| `adr` | 6 (1%) | frontmatter `extensions.kora.adr.*` obligatorio — invariante real pero declarable por presencia del campo |
| `source-alias` (aux) | 6 | distincion blanda con `source` |
| `inventory` | 3 (<1%) | marginal |
| `organigram` | 2 (<1%) | marginal |
| `glossary` | 1 (<1%) | casi orfanito |
| `cq_catalog` | 0 | ornamental — subperfil sin uso |
| `bok` (aux) | 0 declarados | derivacion heuristica por URN/tags |

Tres patologias detectadas:

1. **`note` es el catch-all real** (32%). Significa que las
   distinciones finas no se usan; el operador prefiere "note + tags"
   sobre familia especifica.
2. **`guide`/`faq` son sinonimos operacionales** — invariantes
   practicamente intercambiables.
3. **Subperfiles ornamentales** — `cq_catalog` (subperfil de catalog
   sin uso), `source-alias` (subperfil blando de source).

La distincion ontologica real es **regimen documental**:

- **Descriptivo** — describe hechos, conocimiento, decisiones, manuales.
- **Prescriptivo** — regula comportamiento (RFC 2119, Traces to, etc.).

Y un tipo crudo:

- **Material fuente** — preservado para trazabilidad, no koraficado aun.

15 familias para cubrir 3 distinciones reales = inflado.

## Alternativas consideradas

### A1. Status quo

Mantener 15 familias. Aceptar carga conceptual del catalogo
hipertrofiado.

**Por que NO**: contradice la directiva HITL.

### A2. Poda intermedia (6-7 canonicas)

Retirar las 4 sub-1% (`glossary`, `inventory`, `organigram`, `cq_catalog`)
+ fusionar guide+faq.

**Por que NO**: queda inflado todavia. La distincion `guide` vs
`normative` vs `catalog` sigue siendo nominal mas que ontologica.

### A3. Colapso radical (2 canonicas + 2 auxiliares) — ELEGIDA

- Canonicas: `spec`, `note`
- Auxiliares: `source`, `bok`
- `adr` deja de ser family; se enforce por presencia de
  `extensions.kora.adr.*`

**Por que SI**:
- Refleja la distincion ontologica real (regimen).
- Elimina taxonomia decorativa.
- Convergencia categorial maxima.
- 270 artefactos se reclasifican mecanicamente sin perdida de
  contenido.

## Decision

**KORA queda con 4 familias documentales** (2 canonicas + 2 auxiliares):

| Familia | Rol | Como se declara |
|---------|-----|------------------|
| `spec` | documento **prescriptivo** que cumple `spec-md` | `family: spec` explicito en frontmatter |
| `note` | documento **descriptivo** (catch-all unico) | `family: note` o fallback |
| `source` (aux) | **material crudo** preservado para trazabilidad | convencion de directorio `fuentes/` o sufijo `.source.{txt,md}` |
| `bok` (aux) | corpus grande, chunks permisivos (1000 L) | heuristica por URN `:kb:bok-*` o `tags: [body-of-knowledge]` |

### `adr` como sub-shape opt-in

Los artefactos ADR mantienen su frontmatter estructurado obligatorio
(`extensions.kora.adr.{contexto, alternativas, factorizacion_elegida,
consecuencias, estado}`) y secciones de cuerpo fijas. **La diferencia**:
ya no se declara `family: adr`; se declara `family: note` + presencia
de `extensions.kora.adr.*`.

El toolchain detecta presencia de `extensions.kora.adr` y aplica los
invariantes ADR (frontmatter shape, secciones de body) sin necesidad
de family separada.

### Migracion

Cambios mecanicos en frontmatter de ~270 artefactos:

| family viejo | family nuevo | Conteo aprox |
|--------------|--------------|--------------|
| `guide` | `note` | 86 |
| `faq` | `note` | 86 |
| `normative` | `note` | 71 |
| `catalog` | `note` | 22 |
| `cq_catalog` | `note` | 0 |
| `inventory` | `note` | 3 |
| `organigram` | `note` | 2 |
| `glossary` | `note` | 1 |
| `adr` | `note` (+ preserva `extensions.kora.adr.*`) | 6 |
| `source-alias` | `source` | 6 |
| `generic` | (sin declarar, fallback es `note`) | 18 |

Total: ~270 artefactos con cambio de family. Ninguno se mueve de
lugar fisico.

### Toolchain

- `VALID_FAMILIES` queda `{"spec", "note", "source", "bok"}`.
- `FAMILY_MAX_LINES_PER_PRIMARY_CHUNK` reducido a 3 entradas:
  `note` (120), `bok` (1000), `spec` (500).
- `FAMILY_MAX_TOTAL_LINES_BEFORE_SPLIT` y
  `FAMILY_MAX_PRIMARY_SECTIONS_PER_FILE` idem.
- `_extract_raw_family` y `resolve_document_family` simplificados.
- `source` y `bok` siguen siendo derivaciones del toolchain (no
  declaradas explicitamente).
- Nuevo check `adr-shape` que valida frontmatter + body cuando
  `extensions.kora.adr` esta presente. Reemplaza el invariante de
  family adr.

### Lo que se preserva

- Contenido de todos los artefactos productivos (nadie cambia de
  lugar fisico).
- `extensions.kora.adr.*` en los 6 ADRs vivos (frontmatter
  estructurado).
- `extensions.kora.bok.*` o equivalentes en bok-derived.
- Invariantes editoriales generales de md-spec §5 (T1-T7,
  contraejemplos, fidelidad) — siguen aplicando a `note`.

### Lo que se pierde

- Granularidad nominal de las 11 sub-familias (guide, faq, normative,
  etc.). Los artefactos antes etiquetados como `guide` o `faq` o
  `catalog` se distinguen ahora por su contenido y tags, no por
  family.
- Invariantes blandos por familia (`## Resumen recomendado`,
  `## por pregunta`): eran convencion editorial, no contrato verificable.

## Consecuencias

### Positivas

- **15 → 4 familias**. El catalogo deja de pretender taxonomia
  exhaustiva.
- **Distincion ontologica honesta**: regimen (descriptivo vs
  prescriptivo) + material crudo.
- **adr mas limpio categorialmente**: shape opt-in por presencia de
  campo, no por etiqueta de family.
- **Toolchain mas simple**: VALID_FAMILIES con 4 entradas en lugar
  de 16.

### Negativas

- 270 artefactos cambian metadata. El git diff es voluminoso pero el
  cambio es mecanico.
- Refs externas a "familia X" en handoffs antiguos quedan obsoletas
  (los handoffs viven en archive, no se tocan).

### Riesgos

- **Tests que asumen familias especificas**: revisar. Los tests que
  verifican shape (`md_spec_*`) pueden requerir actualizacion.
- **Catalog navegable**: si los 270 artefactos cambian a `note`,
  perdemos discriminacion en queries. Mitigacion: los tags y la
  estructura de directorios siguen siendo navegables.

## Trazabilidad

Esta ADR refines `urn:kora:kb:adr-poda-radical-2026-05-21` (que retiró
codigo dead pero no toco la taxonomia de familias). Este colapso es la
continuacion natural sobre la dimension doctrinal.

## Estado

`aceptada` — implementacion en mismo commit que produce este ADR.
