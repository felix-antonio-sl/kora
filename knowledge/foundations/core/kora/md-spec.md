---
_manifest:
  urn: "urn:kora:kb:md-spec:1.0.0"
  federation:
    visibility: public
    license: "CC-BY-4.0"
  compatibility:
    min_consumer_version: "2.0.0"
  dependencies:
    requires:
      - "urn:kora:kb:spec:2.0.0"
  provenance:
    created_by: "FS"
    created_at: "2026-02-20"
    note: "KORA/MD v1.0 — Spec for LLM-First Markdown Knowledge Artifacts"
id: KORA-MD-SPEC-01
version: 1.0.0
status: published
tags: [spec, markdown, llm, knowledge, format]
---

# KORA/MD — Markdown for LLM Knowledge v1.0

## 1. Definition

**KORA/MD** is a constrained Markdown dialect optimized exclusively for LLM consumption via RAG. It is NOT designed for human readability. It applies the KORA philosophy of Skeleton (structure), Meat (information), and zero Fat (rhetoric) to the Markdown format.

**Design axiom**: If a human finds a KORA/MD artifact pleasant to read, it probably has too much fat.

### 1.1 Relationship to KORA/Spec

KORA/Spec defines the knowledge engineering philosophy (Fidelity, SSOT, Token Economy). KORA/MD inherits all principles and defines the **physical format** — replacing YAML as the content container while preserving YAML exclusively for the frontmatter manifest.

### 1.2 When to Use

| Use Case                                      | Format              |
| --------------------------------------------- | ------------------- |
| Knowledge artifacts (KBs, guides, references) | **KORA/MD** (.md)   |
| Agent definitions (FSM, states, transitions)  | YAML (.yaml)        |
| Schemas and validation                        | JSON Schema (.json) |
| Catalog and configuration                     | YAML (.yml)         |

---

## 2. Document Anatomy

Every KORA/MD artifact has exactly **3 layers**:

```
┌─────────────────────────────────┐
│  LAYER 1: YAML Frontmatter     │  ← Manifest (machine metadata)
│  (---  ...  ---)                │
├─────────────────────────────────┤
│  LAYER 2: LLM Directive        │  ← Parse instructions (1 block)
│  (> BEGIN_KORA ... END_KORA)    │
├─────────────────────────────────┤
│  LAYER 3: Knowledge Body       │  ← Pure information (headings + content)
│  (# → ## → ### → content)      │
└─────────────────────────────────┘
```

### Layer 1: YAML Frontmatter (Mandatory)

The ONLY YAML in the file. Contains machine-readable metadata.

```yaml
---
_manifest:
  urn: "urn:{namespace}:{type}:{id}:{version}"
  federation:
    visibility: public|internal
    license: "CC-BY-4.0"
  dependencies:
    requires: []
  provenance:
    created_by: "{author}"
    created_at: "{YYYY-MM-DD}"
    source: "{original document URL or reference}"
id: "{ARTIFACT-ID}"
version: "{semver}"
status: draft|published|deprecated
tags: [tag1, tag2, tag3]
domain: "{domain}"
lang: "{es|en}"
---
```

**Rules:**
- `_manifest.urn` is mandatory and must follow KORA URN format.
- `tags` enables RAG retrieval filtering. Minimum 3 tags.
- `source` traces the original human document.
- `lang` declares content language.

### Layer 2: LLM Directive (Mandatory)

A single blockquote immediately after frontmatter. Instructs the consuming LLM on parse behavior.

```markdown
> BEGIN_KORA_PARSE
> Fidelity: absolute. Preserve all information. Ignore formatting aesthetics.
> Lexicon: H2=Topic, H3=Subtopic, H4=Detail. Bold=Key term. Table=Structured data. List=Enumeration.
> References: `[URN]` = cross-artifact link. `[→ Section]` = internal link.
> Fat: zero. No rhetoric, no filler, no transitions, no hedging.
> END_KORA_PARSE
```

**Rules:**
- Exactly one directive block per document.
- Must be a blockquote (`>`).
- Content is fixed template — no customization per artifact.

### Layer 3: Knowledge Body (The Artifact)

Pure information organized via Markdown structural elements. Zero prose. Zero transitions. Zero rhetoric.

---

## 3. Structural Grammar

### 3.1 Heading Hierarchy = Semantic Skeleton

| Level  | Semantic Role                | Example                       |
| ------ | ---------------------------- | ----------------------------- |
| `#`    | Artifact title               | `# Gestión de IPR`            |
| `##`   | Major topic / domain section | `## Fase 1: Formulación`      |
| `###`  | Subtopic / component         | `### Requisitos BIP`          |
| `####` | Atomic detail / leaf node    | `#### Excepciones Ley 19.175` |

**Rules:**
- Maximum depth: `####` (4 levels). Deeper nesting signals need to split artifact.
- Every `##` must be independently retrievable (RAG chunk boundary).
- Headings are **telegraphic**: noun phrases, not sentences.

### 3.2 Content Elements = Information Meat

| Element                 | Use For                            | Anti-pattern                |
| ----------------------- | ---------------------------------- | --------------------------- |
| **Bold**                | Key term definition, first mention | Emphasis or decoration      |
| *Italic*                | Foreign term, technical qualifier  | Stylistic emphasis          |
| `code`                  | Identifiers, URNs, literal values  | General highlighting        |
| Unordered list (`-`)    | Enumeration (no order matters)     | Narrative as bullets        |
| Ordered list (`1.`)     | Sequential steps, procedures       | Priorities without sequence |
| Table                   | Structured comparison, matrix data | Aesthetic formatting        |
| Blockquote (`>`)        | Reserved for LLM Directive only    | Human-facing callouts       |
| Horizontal rule (`---`) | Major section separator            | Decorative breaks           |

### 3.3 Prohibited Elements (Fat)

The following are BANNED from KORA/MD artifacts:

- ❌ Introductory sentences ("En este documento veremos...")
- ❌ Transitional phrases ("A continuación", "Por otro lado")
- ❌ Hedging ("Podría ser que", "En general")
- ❌ Rhetorical questions
- ❌ Greeting/closing formulas
- ❌ Emoji (except as semantic markers in tables)
- ❌ Repeated information (violates SSOT)
- ❌ Images without alt-text that carries information
- ❌ HTML tags
- ❌ Footnotes (use inline URN references instead)
- ❌ Nested blockquotes (`>>`)

### 3.4 Cross-Referencing

**Internal references** (within same artifact):
```markdown
[→ Fase 3: Ejecución]
```

**Cross-artifact references** (to other KORA artifacts):
```markdown
[urn:gn:kb:gestion-prpto:1.0.0]
```

**External references** (to documents outside KORA):
```markdown
[EXT: Ley 19.175 Art. 24]
```

---

## 4. Token Economy Rules

### 4.1 Telegraphic Writing

| Human (Fat)                                                                                                                                       | KORA/MD (Meat)                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| "El proceso de formulación de un proyecto de inversión pública regional consta de las siguientes etapas que deben ser seguidas por el formulador" | **Formulación IPR** — etapas obligatorias: |
| "Es importante señalar que según lo establecido en la normativa vigente, específicamente la Ley 19.175"                                           | Según Ley 19.175:                          |
| "A continuación se presenta una tabla que resume las principales diferencias entre los tipos de inversión"                                        | (table directly, no preamble)              |

### 4.2 Density Metrics

A well-formed KORA/MD artifact should have:

| Metric              | Target     | Measurement                                              |
| ------------------- | ---------- | -------------------------------------------------------- |
| Information density | >80%       | (content tokens) / (total tokens)                        |
| Structural tokens   | <15%       | (heading + list markers + table syntax) / (total tokens) |
| Fat tokens          | <5%        | (filler + transitions + rhetoric) / (total tokens)       |
| Avg sentence length | 8-15 words | Shorter = better for retrieval                           |
| Tables per artifact | ≥1         | Structured data should be in tables                      |

### 4.3 Chunking Alignment

Each `##` section must be **self-contained enough to be retrieved independently** by a RAG system without losing critical context. This means:

- Key terms defined at first use within each `##` section (or via URN reference).
- No forward references ("as we will see in...").
- No backward dependencies ("as mentioned above..."). Use `[→ Section]` instead.

---

## 5. Transformation Playbook

### 5.1 Input: Human Document

Any document originally written for human readers: PDF, Word, HTML, plaintext, wiki page.

### 5.2 Pipeline

```
Human Doc → [P1: Extract] → [P2: Decompose] → [P3: Compress] → [P4: Structure] → [P5: Validate] → KORA/MD
```

#### P1: Extract — Bone Extraction

1. Read entire source document.
2. Identify **every distinct fact, rule, procedure, definition, constraint, exception**.
3. Tag each with a domain label.
4. Discard: greetings, context-setting paragraphs, acknowledgments, formatting artifacts, redundant restatements.

**Output**: Flat list of tagged atomic information units.

#### P2: Decompose — Skeleton Construction

1. Group information units by domain topic.
2. Arrange into heading hierarchy (max 4 levels).
3. One `##` per RAG-retrievable chunk.
4. Verify: each `##` is independently meaningful.

**Output**: Heading skeleton with assigned information units.

#### P3: Compress — Fat Removal

For EACH information unit:

1. Remove introductory clauses.
2. Remove hedging and qualifiers that add no information.
3. Remove transitional connectors.
4. Convert verbose descriptions to:
   - **Tables** (if comparing/contrasting).
   - **Lists** (if enumerating).
   - **Bold key-term + colon + definition** (if defining).
5. Preserve ALL technical content, numbers, dates, legal references, exceptions.

**Rule**: If removing a word changes the meaning → keep it. If removing a word only changes the tone → remove it.

#### P4: Structure — Markdown Assembly

1. Write YAML frontmatter with manifest.
2. Add LLM Directive (fixed template).
3. Assemble heading skeleton with compressed content.
4. Add cross-references as `[urn:...]` or `[→ Section]`.
5. Add tables for all structured comparisons.
6. Add horizontal rules (`---`) between major `##` sections.

#### P5: Validate — Quality Gate

| Check              | Criterion                                 | Action if fail            |
| ------------------ | ----------------------------------------- | ------------------------- |
| YAML valid         | Frontmatter parses without error          | Fix syntax                |
| URN exists         | `_manifest.urn` registered in catalog     | Register via `kora index` |
| No fat             | Zero introductions, transitions, rhetoric | Remove                    |
| Density            | >80% information tokens                   | Compress further          |
| Chunk independence | Each `##` retrievable alone               | Add missing context       |
| No duplication     | Each fact appears exactly once            | Deduplicate via SSOT      |
| Cross-refs valid   | All `[urn:...]` resolve                   | Fix or remove             |
| Tags               | Minimum 3 tags in frontmatter             | Add tags                  |

---

## 6. Example: Before and After

### Source (Human Document)

> La gestión de rendiciones de cuentas en el contexto del Gobierno Regional de Ñuble es un proceso fundamental que permite asegurar la correcta utilización de los recursos públicos transferidos a las distintas entidades beneficiarias. Este proceso se rige principalmente por las disposiciones de la Contraloría General de la República y se ejecuta a través del Sistema de Rendición Electrónica de Cuentas (SISREC).
>
> Es importante señalar que existen distintos plazos según el tipo de fondos transferidos. Para los fondos FNDR, el plazo máximo es de 60 días hábiles. Para los fondos sectoriales, el plazo puede variar entre 30 y 90 días hábiles según lo establecido en el convenio respectivo.

### KORA/MD Transformation

```markdown
---
_manifest:
  urn: "urn:gn:kb:gestion-rendiciones:2.0.0"
  provenance:
    created_by: "FS"
    created_at: "2026-02-20"
    source: "Manual de Rendiciones GORE Ñuble v3"
id: KB-GN-020
version: 2.0.0
status: published
tags: [rendiciones, sisrec, cgr, plazos, gore-nuble]
domain: gn
lang: es
---

> BEGIN_KORA_PARSE
> Fidelity: absolute. Preserve all information. Ignore formatting aesthetics.
> Lexicon: H2=Topic, H3=Subtopic, H4=Detail. Bold=Key term. Table=Structured data.
> References: `[URN]` = cross-artifact link. `[→ Section]` = internal link.
> Fat: zero. No rhetoric, no filler, no transitions, no hedging.
> END_KORA_PARSE

# Gestión de Rendiciones de Cuentas

## Definición

**Rendición de cuentas** — proceso de verificación del uso de recursos públicos transferidos. Regulado por CGR. Ejecutado vía SISREC.

## Plazos por Tipo de Fondo

| Tipo de Fondo | Plazo              | Base Legal     |
| ------------- | ------------------ | -------------- |
| FNDR          | 60 días hábiles    | Res. CGR       |
| Sectoriales   | 30-90 días hábiles | Según convenio |
```

---

## 7. Naming Convention

```
{id}_{nombre-kebab}.md

Examples:
- kb_gn_019_gestion-ipr.md
- kb_gn_020_gestion-rendiciones.md
- kb_core_001_spec.md
```

---

## 8. Compatibility with Existing Tools

| Tool                | Compatibility                                   |
| ------------------- | ----------------------------------------------- |
| `kora index`        | ✅ Reads YAML frontmatter `_manifest.urn`        |
| `kora resolve`      | ✅ URNs work identically                         |
| `kora health`       | ✅ Scans `.md` files for URN references          |
| `kora validate`     | 🔧 Needs extension for MD frontmatter validation |
| RAG systems         | ✅ Native Markdown chunking by `##` headings     |
| Git/GitHub          | ✅ Native rendering and diffs                    |
| LLM context windows | ✅ ~20-30% more token-efficient than YAML        |
