---
_manifest:
  urn: urn:kora:kb:cat-governance-lattice
  provenance:
    created_by: FS
    created_at: '2026-02-26'
    source: "Davey & Priestley (Introduction to Lattices and Order), KORA gobernanza v1.3.0, spec-md v2.1.0, md-spec v2.0.0"
version: 1.0.0
status: published
tags:
- category-theory
- lattice
- governance
- precedence
- functors
- formal-layer
- kora
lang: en
---

# Governance as Lattice: Precedence, Transformation, and Spec Hierarchy

## Purpose

This document formalizes the KORA governance structure as a lattice of specifications with functorial transformations. It provides the mathematical foundation for: (1) the precedence hierarchy that resolves inter-spec conflicts, (2) the transformation functors (Koraficación K, Agentificación G, Crystallization C) that produce KORA artifacts, and (3) the relationship between the formal layer (this series) and the operational specs.

## Prerequisites

All notation from [00-foundations](urn:kora:kb:cat-foundations). Familiarity with the agent and skill models from documents 01-04.

## 1. The Spec Lattice

### 1.1 Definition

**Definition.** The KORA specification ecosystem forms a bounded lattice (L, ≤) where:

**Objects:** Specifications and governance documents:

```
L = { gobernanza, spec-md, md-spec, agent-spec-md, skill-spec-md,
      ext-ns₁, ext-ns₂, ..., ext-ns_k }
```

**Order (≤):** Precedence. s₁ ≤ s₂ means "s₂ prevails over s₁ in case of conflict."

**Join (∨):** Given conflicting specs, the resolution is their join (the lowest spec that prevails over both).

**Meet (∧):** The most specific rule that both specs agree on.

### 1.2 The Lattice Structure

```
                    gobernanza (⊤)
                    /          \
              spec-md          md-spec
                |                |
           agent-spec-md         |
              /    \             |
    skill-spec-md   \            |
         |      runtime-spec-md  |
         |           |           |
    swarm-spec-md    |           |
                \    |         /
                 ext-namespace (⊥ ... ⊥)
```

**Formally:**

| Level | Spec | Precedence |
|-------|------|-----------|
| 4 (⊤) | gobernanza | Prevails over all. Meta-rules. |
| 3 | spec-md, md-spec | Each governs its domain (prescriptive vs descriptive). Neither prevails over the other outside its domain. |
| 2a | agent-spec-md | Governs agent workspaces. Cannot contradict level 3. |
| 2b | skill-spec-md | Governs Skills. Cannot contradict level 2a or 3. |
| 2c | runtime-spec-md | Governs cross-platform deployment. Cannot contradict levels above. |
| 2d | swarm-spec-md | Governs multi-agent orchestration. Cannot contradict levels above. |
| 1 | Operational sections | Guides within specs. Cannot contradict declarative rules. |
| 0 (⊥) | Namespace extensions | Domain-specific rules. Cannot contradict any higher level. |

**Theorem (Bounded Lattice).** (L, ≤) is a bounded lattice with:
- Top ⊤ = gobernanza (prevails over everything)
- Bottom ⊥ = namespace extensions (lowest precedence)
- Join s₁ ∨ s₂ = lowest common ancestor in the hierarchy
- Meet s₁ ∧ s₂ = most specific shared consequence

### 1.3 The Domain Partition

**Definition.** Specs at level 3 partition the artifact domain:

```
Domain(spec-md) = { prescriptive documents }
Domain(md-spec) = { descriptive documents }
Domain(agent-spec-md) = { agent workspaces }
Domain(skill-spec-md) = { Skills }
Domain(swarm-spec-md) = { multi-agent swarms }
```

**Theorem (Domain Disjointness at Level 3).**

```
Domain(spec-md) ∩ Domain(md-spec) = ∅
```

Prescriptive and descriptive documents are disjoint types. Conflict between spec-md and md-spec is resolved by domain: each prevails within its own domain.

**Theorem (Domain Nesting at Level 2).**

```
Domain(skill-spec-md) ⊂ Domain(agent-spec-md)
```

Skills live within agent workspaces. skill-spec-md governs Skills; agent-spec-md governs the workspace that contains them.

### 1.4 The Silence Rule

**Theorem (Restrictive Default).** If spec S does not address topic T, the absence of a rule is NOT permission. The default interpretation is the most restrictive option compatible with the spirit of S.

*Categorical formulation:* The lattice L has no "free variables." Every point in the artifact space is either explicitly governed by some spec or implicitly restricted by the silence rule.

## 2. Transformation Functors

### 2.1 The Three Functors

KORA defines three transformation functors that produce artifacts from source material:

| Functor | Notation | Domain → Codomain | Purpose |
|---------|----------|-------------------|---------|
| Koraficación | K | DocHumano → KORA/MD | Transform human documents into RAG-optimized knowledge |
| Crystallization | C | Decisions → KORA/Spec-MD | Transform implicit practices into explicit specs |
| Agentificación | G | Requirements → KORA/Agent | Transform specs/YAMLs into agent workspaces |

### 2.2 Koraficación Functor K

**Definition.** K: DocHumano → KORA/MD

**Properties:**
- **Faithful:** Every fact in the source appears in K(doc). Nothing is lost.
- **Telegraphic:** K(doc) is maximally compressed. All communicative entropy is removed.
- **Promoter:** Inline content is promoted to structured format (prose → bullets, tables, code blocks).
- **Normalizing:** Dates → ISO 8601, names → canonical form.
- **Idempotent:** K(K(doc)) = K(doc). Applying K twice produces the same result.
- **Language-invariant:** K preserves the source language.

**Composition with pipeline:**

```
inbox/ --source--> source/ --K--> drafts/ --review--> knowledge/
```

K is applied at the source/ → drafts/ transition.

### 2.3 Crystallization Functor C

**Definition.** C: {Decisions ∪ Practices ∪ Restrictions} → KORA/Spec-MD

The input is heterogeneous: design decisions (explicit or tacit), existing practices (informal conventions), and constraints (technical, organizational, legal).

**Properties:**
- **Crystallizer:** Implicit decisions become explicit rules with RFC 2119 keywords.
- **Formalizer:** Informal conventions become rules with exactly one reading.
- **Disambiguator:** Multiple interpretations are forced to exactly one.
- **Exemplifier:** Complex rules include Correcto/Incorrecto pairs.

### 2.4 Agentificación Functor G

**Definition.** G operates in two modes:

```
G₁: Requirements → KORA/Agent    (construction from scratch)
G₂: KODA/Agent   → KORA/Agent    (transmutation from legacy)
```

**Properties:**
- **Faithful:** Every state and transition is preserved. No morphisms lost.
- **Segregating:** Components c, F, U, M are separated into independent files.
- **Promoting:** Inline content is promoted (personality inline → SOUL.md, policies inline → config.json).
- **Bisimilar:** G(agent) ~ agent. The workspace produces indistinguishable outputs.
- **Idempotent:** G(G(agent)) = G(agent).

### 2.5 Functor Composition

**Theorem.** The transformation functors compose with the governance lattice:

```
C produces documents governed by spec-md (level 3)
K produces documents governed by md-spec (level 3)
G produces workspaces governed by agent-spec-md (level 2a)
```

**Theorem (Governance Preservation).** Each functor produces artifacts that satisfy their governing spec:

```
K(doc) ⊨ md-spec       for all documents doc
C(dec) ⊨ spec-md       for all decision sets dec
G(req) ⊨ agent-spec-md for all requirements req
```

where ⊨ means "satisfies all rules of."

## 3. The Formal-Operational Bridge

### 3.1 The Two-Layer Architecture

**Definition.** The KORA knowledge system has two layers:

```
FORMAL LAYER (this series: 00-05)
    ↕ traces-to
OPERATIONAL LAYER (specs: gobernanza, md-spec, spec-md, agent-spec-md, skill-spec-md, runtime-spec-md, swarm-spec-md)
    ↕ instances
RUNTIME LAYER (agents, skills, knowledge artifacts)
```

### 3.2 The Traceability Functor

**Definition.** Trace: Operational → Formal is a functor that maps each operational rule to its formal justification:

```
Trace(rule) = { theorem, definition, or property in formal layer that justifies rule }
```

**Properties:**
- **Surjective on image:** Every rule that has a categorical justification traces to it.
- **NOT total:** Some rules are pragmatic (token budgets, file naming) and have no formal justification. These are operational-only.
- **Injective on theorems:** Each formal theorem may justify multiple rules, but each rule traces to at most one theorem.

### 3.3 Traceability Map

The following table maps operational rules in the v7.0.0 specs to their formal justifications. Section numbers reference agent-spec-md v7.0.0 and other v2.0.0/v3.0.0 specs.

| Operational Rule | Spec Section | Formal Justification |
|------------------|-------------|---------------------|
| 5 mandatory files per agent | agent-spec §4.1 | 01 §7: Segregation is Necessary theorem |
| FSM no personality | agent-spec §5.1 | 01 §2.2: Fiber Independence theorem |
| config.json immutable from LLM | agent-spec §5.3 | 01 §1.3: M-Immutability theorem |
| Every CM is a valid Skill | agent-spec §5.6 | 02 §2.3: η is isomorphism theorem |
| Skills ≤5000 tokens | skill-spec §8.3 | (pragmatic — no formal justification) |
| Sub-agents dissipate SOUL/USER | agent-spec §7 | 01 §2.3: Dissipation theorem |
| Interface declared closed at design-time | agent-spec §14.4 | 04 §4.2: Design-time Closure theorem |
| Discovered Skills persist in session | agent-spec §14.6 | 04 §4.2: Monotonicity theorem |
| Security filters discovery | agent-spec §14.3 | 04 §2.4: D_M subfunctor theorem |
| Co-induction at terminal states | agent-spec §3.1 | 01 §3.3: Coinductive Verification definition |
| Behavioral equivalence = substitutability | agent-spec §12.5 | 01 §5.2: Substitutability theorem |
| Wiring preserves compositionality | agent-spec §3.5 | 01 §6.3: Compositionality theorem |
| gobernanza prevails over all specs | gobernanza §4.1 | 05 §1.2: Bounded Lattice, ⊤ = gobernanza |
| skill-spec-md cannot contradict agent-spec-md | gobernanza §4.1 | 05 §1.2: Level 2b ≤ Level 2a in lattice |
| Silence is restrictive | gobernanza §4.3 | 05 §1.4: Restrictive Default theorem |
| Cross-platform behavioral equivalence | runtime-spec §8.1 | 01 §5.2: Substitutability theorem |
| Golden Path = Kleisli chain of Skills | swarm-spec §4.1 | 02 §6.1: Kleisli composition >=> |
| Circuit breaker verifies health before continuing | swarm-spec §5.1 | 01 §3.3: Coinductive Verification |
| Backpressure as monad constraint | swarm-spec §6.1 | 00 §5: Monad laws — bind respects constraints |
| Swarm composition preserves compositionality | swarm-spec §3.3 | 01 §6.3: Compositionality theorem |
| Sub-agents in swarm dissipate SOUL/USER | swarm-spec §3.4 | 01 §2.3: Dissipation theorem |
| Discovered Skills in swarm persist monotonically | swarm-spec §8.5 | 04 §4.2: Monotonicity theorem |
| Security filters event routing | swarm-spec §8.2 | 04 §2.4: D_M subfunctor theorem |
| Swarm membership only grows during session | swarm-spec §8.1 | 04 §4.2: Monotonicity (extended to agents) |
| Koraficación preserves truth | md-spec §5.5 | 05 §2.2: Koraficación Functor K — Faithful property |
| model_routing in config.json immutable from LLM | runtime-spec §11.4 | 01 §1.3: M-Immutability theorem (model_routing inherits immutability as config.json property) |
| Model routing enforced by orchestration, not LLM | runtime-spec §11.4, §13.2 | 01 §1.3: M-Immutability theorem (LLM operates inside Kl(M), cannot change external parameters) |
| Security filters inter-agent inputs | swarm-spec §12.2 | 04 §2.4: D_M subfunctor (extended by analogy from discovery to input filtering) |
| config.json immutable across agents | swarm-spec §12.2 | 01 §1.3: M-Immutability theorem |
| Evals approximate bisimulation | agent-spec §16.4 | 01 §5: Bisimulation (empirical approximation for finite input subset) |
| Sentinel coinductive monitoring | swarm-spec §13.3 | 01 §3.3: Coinductive Verification (analogy from intra-agent to inter-agent) |

### 3.4 Rules Without Formal Justification

The following operational rules are pragmatic and have no categorical theorem backing them. They exist because they work, not because they're mathematically necessary:

| Rule | Reason |
|------|--------|
| Token budget ≤5000 per CM Core | Empirical: LLM context windows have finite capacity |
| File naming conventions (CM-*.md) | Convention: human-readable organization |
| Spanish vs English language choice | Pragmatic: training data distribution |
| Frontmatter YAML schema | Implementation: YAML is the metadata format |
| Progressive Disclosure 3 phases | Design pattern: progressive information revelation |
| SemVer versioning | Convention: industry-standard version numbering |
| Tier system T1/T2/T3/T4 | Convention: capacity/cost nomenclature for LLM models |
| Complexity signal (simple/estandar/complejo/critico) | Operational taxonomy for task classification |
| Fallback chains as ordered list | Resilience engineering, not categorical structure |
| Budget thresholds (tokens, cost) | Economic parameters, not structural |
| Eval types (Regression, Hallucination, Tool-calling, Cost, Security, Adversarial) | Empirical quality categories |
| limits in config.json (policy_flags, quotas) | Operational discipline constraints |
| Sandbox boolean shorthand (true/false) | Syntactic convenience |
| Model diversity (cross-provider auditing) | Audit independence practice |
| Sentinel heartbeat cycle | Observability pattern |
| Prompt injection prevention in swarms | Security engineering practice |

These rules are valid but NOT derived from category theory. They are **operational constraints** that complement the formal foundations.

## 4. The Full Picture

### 4.1 KORA as a Categorical System

Assembling documents 00-05, KORA is formalized as:

```
KORA = (Eco, Psh(F), Free ⊣ Forget, L, {K, C, G})

where:
  Eco           = 2-category of agents (03)
  Psh(F)        = presheaf of discoverable Skills over Eco (04)
  Free ⊣ Forget = adjunction between CMs and Skills (02)
  L             = governance lattice of specs (05)
  K, C, G       = transformation functors producing KORA artifacts (05 §2)
```

### 4.2 What This System Covers

| Dimension of Agentic Space | Formal Coverage | Document |
|----------------------------|----------------|----------|
| Agent definition | F-coalgebra in Kl(M) | 01 |
| Agent identity | Bisimulation | 01 §5 |
| Component architecture | Fiber decomposition + segregation | 01 §2, §7 |
| Security model | Monad M, immutability theorem | 01 §1.3 |
| Agent composition | Wiring diagrams, adjunctions | 01 §6 |
| Skill model | Free ⊣ Forget adjunction | 02 |
| Skill lifecycle | Progressive disclosure phases | 02 §3 |
| Backward compatibility | η isomorphism | 02 §2.3 |
| Skill composition | Kleisli composition >=> | 02 §6 |
| Inter-agent relationships | 2-category Eco | 03 |
| Interoperability | 1-cells (T, C, R, P) | 03 §3 |
| Migration and versioning | 2-cells (natural transformations) | 03 §4 |
| Dynamic capability | Presheaf Psh(F) | 04 |
| Skill discovery | Discovery functor D | 04 §2 |
| Runtime extensibility | Fibered coproduct F_eff | 04 §4 |
| Governance hierarchy | Spec lattice L | 05 §1 |
| Multi-agent orchestration | Kleisli composition + coinduction | swarm-spec (01 §6, 02 §6, 01 §3.3) |
| Artifact transformation | Functors K, C, G | 05 §2 |
| Formal-operational bridge | Traceability functor | 05 §3 |

### 4.3 What This System Does NOT Cover

| Dimension | Status | Why |
|-----------|--------|-----|
| Runtime execution (interpreter, scheduler) | Out of scope | Implementation detail, not mathematical structure |
| Inter-session memory | Partially covered (U_epi fiber) | Persistence mechanisms are platform-dependent |
| Observability (metrics, tracing) | Not covered | Engineering concern, no categorical model proposed |
| Dynamic negotiation between agents | Not covered | Would require game-theoretic extension |
| Empirical evaluation (benchmarks) | Not covered | Experimental, not formal |
| Token optimization algorithms | Not covered | Computational, not structural |

These dimensions are acknowledged as outside the formal layer. They are legitimate engineering concerns that the operational specs may address without requiring categorical justification.

## Sources

- Davey, B.A. & Priestley, H.A. "Introduction to Lattices and Order" — Chapters 1-2
- Mac Lane, S. "Categories for the Working Mathematician" — Chapter IV (functors, natural transformations)
- KORA gobernanza v1.3.0 — §4 (precedence hierarchy)
- KORA spec-md v2.1.0 — §1.2 (crystallization functor)
- KORA md-spec v2.0.0 — §6 (koraficación functor)
