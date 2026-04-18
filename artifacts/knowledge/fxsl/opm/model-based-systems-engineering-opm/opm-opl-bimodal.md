---
_manifest:
  urn: urn:fxsl:kb:opm-opl-bimodal
  provenance:
    created_by: kora/curator
    created_at: '2026-03-25'
    source: OPERATIONS/source/fxsl/opm-methodology/opm-libro-opl-bimodal.md
version: 1.0.0
status: published
tags:
- opm
- opl
- bimodal
- text-graphics
- simulation
- metamodel
- tesperanto
lang: en
extensions:
  kora:
    family: textbook
    depends_on:
    - urn:fxsl:kb:opm-iso-19450
    - urn:fxsl:kb:opl-es
    book_source: Dori, D. (2015). Model-Based Systems Engineering with OPM and SysML.
      Springer.
    chapters:
    - 2
    - 11
relations:
  cites:
  - urn:fxsl:kb:opl-es
  - urn:fxsl:kb:opm-iso-19450
---


# OPM OPL Bimodal — Graphic-Text Equivalence and Textual Specification

## Resumen

Object-Process Language (OPL) is the textual modality of OPM, a formal subset of English that expresses the same model facts as Object-Process Diagrams (OPDs). OPM's bimodal representation exploits the dual-channel cognitive assumption: graphics and text reinforce comprehension through parallel visual and verbal processing. OPL serves dual purpose: human communication (stakeholder validation, error detection) and machine generation (code synthesis, simulation, schema generation). OPL syntax is defined by ~400 EBNF production rules in ISO 19450 Annex A. For formal OPL specification, see [OPM ISO 19450](urn:fxsl:kb:opm-iso-19450). For Spanish localization, see [OPL ES](urn:fxsl:kb:opl-es).

## OPL Definition and Nature

**Object-Process Language (OPL)** — subset of English that expresses textually the OPM model that the OPD set expresses graphically.

Core properties:

- Auto-generated from OPD constructs in real time by CASE tools (OPCAT/OPCloud)
- Devoid of programming language crypticism; readable by non-technical stakeholders
- Formally parseable via context-free grammar (EBNF, ~400 production rules, ISO 19450 Annex A)
- Default language: English; extensible to any natural language via graphic intermediation

**Model fact** — relation between two or more things in an OPM model; expressed simultaneously in both modalities (OPD construct + OPL sentence).

## Graphics-Text Equivalence Principle

**The Graphics-Text Equivalence OPM Principle**: any model fact expressed graphically in an OPD is also expressed textually in the corresponding OPL paragraph.

Structural definitions:

- **OPD element** — graphical expression of a thing or a link
- **OPD construct** — collection of connected OPD elements expressing a model fact
- **OPL paragraph** — collection of OPL sentences expressing textually the same model facts as one OPD
- **OPL specification** — collection of all unique OPL sentences expressing all model facts in the OPD set

Bidirectional reconstruction: at any consistent model state (no unlinked things), OPD reconstructable from OPL paragraph and vice versa.

## Dual Purpose of OPL

| Direction | Goal | Mechanism |
|-----------|------|-----------|
| Human-oriented | Convert OPD set into natural language for stakeholder communication | Readable English subset; enables non-technical participation in requirements elicitation and validation |
| Machine-oriented | Provide formal basis for automated artifact generation | EBNF-parseable text enables executable code generation, simulation, UI generation, database schema definition |

### Human-Oriented Benefits

- Customer-side stakeholders (domain experts, executives, lawyers) validate requirements via text without diagram literacy
- Modelers receive immediate textual feedback per graphic edit, enabling error detection at creation time
- Novice OPM users accelerate learning by inspecting text-graphic pairs in tandem
- OPL specification serves as formal textual document matching graphical spec ("for free")

### Machine-Oriented Benefits

- Context-free grammar enables parsing equivalent to programming language compilation
- OPL text file serves as basis for round-trip engineering: analysis/design changes propagate to application artifacts
- Enables automated generation of executable code, database schemas, simulation

## Metamodel of OPM Model Structure

The OPM metamodel (model of a model) reveals two parallel hierarchies—graphic and textual—with correspondence at every level:

| Graphic Hierarchy | Textual Hierarchy | Relation |
|-------------------|-------------------|----------|
| OPD Set | OPL Spec | Mutual specification of full model |
| OPD | OPL Paragraph | Same model context (diagram scope) |
| OPD Construct | OPL Sentence | Same model fact |
| Link | Reserved Phrase | Textual specification of graphic connector |
| Thing | Name (non-reserved phrase) | Identity correspondence |

Top-level structure (OPL self-description):

- OPM Model specifies System
- OPM Model consists of OPD Set and OPL Spec
- OPD Construct consists of Thing Set (2..*) and Link Set (1..*)
- OPL Sentence consists of Phrases (3..*) and Punctuation Marks (1..*)
- Thing exhibits Name
- Link graphically specifies Reserved Phrase
- Thing can be in-zoomed to create OPD

## Reserved vs Non-Reserved OPL Phrases

**OPL phrase** — sequence of one or more words in an OPL sentence.

| Phrase Type | Definition | Examples | Visual Convention |
|-------------|-----------|----------|-------------------|
| Non-reserved | Modeler-defined; expresses system/domain-specific entity or relation name | Object names, process names, state names, user-defined tagged relations | **Bold** Arial; color-coded (green=object, blue=process, brown=state) |
| Reserved | Built into EBNF syntax; connects non-reserved phrases | `requires`, `yields`, `consumes`, `affects`, `consists of`, `and`, `or`, `exactly one of` | Regular (non-bold) Arial |

**Bolding OPL Convention**: non-reserved phrases in bold, reserved phrases in regular font, punctuation marks bolded.

Analogy: reserved phrases are mortar; non-reserved phrases are building blocks.

## OPL Sentence Families

OPL formal sentences belong to four families (per EBNF production rules):

1. **Thing description sentence** — declares objects, processes, states, attributes
2. **Procedural sentence** — expresses dynamic behavior (enabling, transformation, consumption, effect)
3. **Structural sentence** — expresses structural relations (aggregation, generalization, exhibition, characterization)
4. **Context management sentence** — manages diagram hierarchy (in-zooming, unfolding)

Each family corresponds to specific OPD construct patterns and reserved phrase sets.

## States and Simulation

### States

**State** — situation, position, or value at which an object can exist for a positive time duration. States belong exclusively to their owning object; no independent existence.

Conventions:

- State symbol: rounded-corner rectangle (rountangle) inside object rectangle
- State names: always lowercase (e.g., `possibly injured`, `being helped`, `off`, `standby`, `on`)
- Thing names (objects, processes): capitalized first letter of each word
- OPL generation: `Object can be state1, state2, or state3.`

### Effect and State Change

| Link Type | OPL Expression | Specificity |
|-----------|---------------|-------------|
| Effect link (bidirectional) | `Process affects Object.` | Implicit: some state change occurred |
| Input-output link pair (two unidirectional arrows) | `Process changes Object from input_state to output_state.` | Explicit: specifies source and target states |

Effect link expresses that a process changed an object in some way. Input-output link pair (replacing effect link) explicates the exact state transition.

### Animated Simulation

OPM models are executable via animated simulation in CASE tools. Three-stage execution cycle:

1. **Pre-process** — input state solid (active); process inactive
2. **In-process** — process solid (executing); both states semi-solid (transitioning); red dots travel along input-output links
3. **Post-process** — output state solid (active); process terminated

Simulation benefits:

- Dynamic visualization aid for modeler and audience
- Debugger-equivalent for logical design verification
- Recommended: animate frequently during model construction to prevent error accumulation

## Bimodal Motivation and Cognitive Basis

### Dual-Channel Assumption

Humans possess separate cognitive channels for visual and verbal processing (Clark & Paivio 1991; Baddeley 1992; Mayer 2003). OPD+OPL caters to both channels simultaneously.

- Visually-inclined individuals prefer OPD diagrams
- Text-oriented individuals prefer OPL sentences
- Combined presentation reinforces comprehension and error detection across both channels

OPM is the first conceptual modeling language to formally combine graphic and textual modalities (USPTO 7,099,809, 2006).

### Stakeholder Engagement

Bimodal representation enables:

- Real-time OPL feedback per graphic edit enables immediate error detection
- Non-technical customer participation in modeling sessions (reading OPL, not diagrams)
- Early stakeholder buy-in reduces resistance to change
- Customer "sign-off" on model as system blueprint
- Requirements-design gap closure: OPL bridges free-prose requirements and formal OPM specification

### Error Detection via Bimodal Cross-Check

Modeling errors produce semantically incorrect OPL. Example: using result link instead of effect link generates `Process yields Object` instead of `Process affects Object` — immediately detectable by reading OPL output.

## Tesperanto

**Tesperanto** — enhancement of OPL that applies heuristics for improved human readability of auto-generated text (Blekhman & Dori 2013).

Improvements over raw OPL:

- Sentence length adjustment
- Synonym variation
- Word ordering optimization
- Phrase recurrence reduction
- Less mechanical, repetitive output

Example difference: where OPL repeats a process name four times (once per procedural relation), Tesperanto consolidates to single mention.

Status: research-stage; not standardized. OPL remains the formal modality.
