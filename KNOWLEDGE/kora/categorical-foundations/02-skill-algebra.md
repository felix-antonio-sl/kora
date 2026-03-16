---
_manifest:
  urn: urn:kora:kb:cat-skill-algebra
  provenance:
    created_by: FS
    created_at: '2026-02-26'
    source: "Mac Lane (CWM, Ch. IV Adjunctions), Awodey (Category Theory, Ch. 10 Monads), KORA skill-spec-md v1.0.0"
version: 1.0.0
status: published
tags:
- category-theory
- adjunction
- free-forget
- skill
- formal-layer
- kora
lang: en
---

# Skills as Free Algebra: The Adjunction Free ⊣ Forget

## Purpose

This document formalizes KORA Skills as the free construction over Cognitive Models (CMs). The adjunction Free ⊣ Forget is the mathematical engine that guarantees backward compatibility (every existing CM is a valid Skill) while enabling extension (Skills can have scripts, references, and assets that CMs cannot).

## Prerequisites

All notation and definitions from [00-foundations](urn:kora:kb:cat-foundations). The agent model from [01-agent-coalgebra](urn:kora:kb:cat-agent-coalgebra), specifically: endofunctors on U (§2), lazy evaluation, and the interface functor F (§4).

## 1. The Two Categories

### 1.1 CM_Cat: The Category of Cognitive Models

**Definition.** CM_Cat is the category where:

**Objects:** Cognitive Models — files CM-*.md with exactly 4 sections:

```
CM = (Purpose, IO, Procedure, SignatureOutput)
```

Each section is a structured text block. The 4-tuple is ordered and complete.

**Morphisms:** CM transformations τ: CM₁ → CM₂ that preserve structure:
- τ maps Purpose₁ to Purpose₂ (preserving cognitive intent)
- τ maps IO₁ to IO₂ (preserving input/output types)
- τ maps Procedure₁ to Procedure₂ (preserving procedural steps)
- τ maps SignatureOutput₁ to SignatureOutput₂ (preserving output format)

**Identity:** id_CM = identity on all 4 sections.
**Composition:** (τ₂ ∘ τ₁)(section) = τ₂(τ₁(section)) for each section.

### 1.2 Skill_Cat: The Category of Skills

**Definition.** Skill_Cat is the category where:

**Objects:** Skills — either degenerate (CM-only) or extended (directory with SKILL.md):

```
Skill = (CMCore, Scripts, References, Assets, Metadata)

where:
  CMCore     = (Purpose, IO, Procedure, SignatureOutput)    — mandatory
  Scripts    ∈ P(File)                                       — optional (powerset of files)
  References ∈ P(File)                                       — optional
  Assets     ∈ P(File)                                       — optional
  Metadata   = (name, description, version, allowed-tools, requires)  — extended frontmatter
```

**Morphisms:** Skill transformations σ: Skill₁ → Skill₂ that:
- Preserve CMCore (all 4 sections mapped preserving structure)
- Map Scripts₁ to Scripts₂ (preserving executable semantics)
- Map References₁ to References₂
- Map Assets₁ to Assets₂
- Map Metadata₁ to Metadata₂ (preserving compatibility constraints)

**Identity and Composition:** Standard.

### 1.3 The Inclusion

**Observation.** CM_Cat embeds into Skill_Cat via the degenerate form: a CM is a Skill with empty Scripts, References, Assets, and minimal Metadata. This embedding is the key to the adjunction.

## 2. The Adjunction Free ⊣ Forget

### 2.1 The Forget Functor

**Definition.** Forget: Skill_Cat → CM_Cat extracts the CM Core:

```
Forget(Skill) = Forget(CMCore, Scripts, References, Assets, Metadata)
              = CMCore
              = (Purpose, IO, Procedure, SignatureOutput)
```

On morphisms: Forget(σ) = σ|_{CMCore} (restrict the skill transformation to the CM Core component).

**Properties:**
- Forget is faithful: distinct skill morphisms that agree on CMCore are identified
- Forget is NOT full: not every CM transformation lifts to a skill transformation (you'd need to also transform Scripts, etc.)
- Forget forgets Scripts, References, Assets, and extended Metadata

### 2.2 The Free Functor

**Definition.** Free: CM_Cat → Skill_Cat wraps a CM in a Skill structure:

```
Free(CM) = Free(Purpose, IO, Procedure, SignatureOutput)
         = (CM, ∅, ∅, ∅, Metadata_default)

where:
  CMCore     = CM                           — preserved exactly
  Scripts    = ∅                            — empty directory
  References = ∅                            — empty directory
  Assets     = ∅                            — empty directory
  Metadata   = derived from CM frontmatter  — minimal metadata
```

On morphisms: Free(τ) applies τ to the CMCore and identity to the empty directories.

**Properties:**
- Free preserves all CM structure
- Free adds no new information (empty optional directories)
- Free is faithful

### 2.3 The Unit η

**Definition.** η: Id_{CM_Cat} ⇒ Forget ∘ Free is the natural transformation:

```
η_CM: CM → Forget(Free(CM))
     = CM → Forget(CM, ∅, ∅, ∅, Metadata_default)
     = CM → CM
     = id_CM
```

**Theorem (η is isomorphism).** For every CM, η_CM is the identity — hence an isomorphism.

```
η_CM = id: CM ≅ Forget(Free(CM))
```

*Meaning:* Wrapping a CM in a Skill (Free) and then extracting the CM back (Forget) returns the original CM unchanged. **This is the backward compatibility guarantee.** Every existing CM-*.md in the KORA monorepo is automatically a valid Skill without modification.

### 2.4 The Counit ε

**Definition.** ε: Free ∘ Forget ⇒ Id_{Skill_Cat} is the natural transformation:

```
ε_Skill: Free(Forget(Skill)) → Skill
       = Free(CMCore) → (CMCore, Scripts, References, Assets, Metadata)
       = (CMCore, ∅, ∅, ∅, Metadata_default) → (CMCore, Scripts, References, Assets, Metadata)
```

ε maps the free skill (with empty directories) to the original skill by:
- Identity on CMCore (preserved exactly)
- Inclusion ∅ ↪ Scripts (empty maps to actual scripts)
- Inclusion ∅ ↪ References
- Inclusion ∅ ↪ Assets
- Inclusion Metadata_default ↪ Metadata

**Theorem (ε is surjection but NOT isomorphism).** ε_Skill is surjective (every component of the original Skill is in the image) but NOT injective (the free version has empty directories while the original may have content).

```
ε is surjective: im(ε) = Skill
ε is NOT iso:    ker(ε) = {Scripts, References, Assets} ≠ ∅ (in general)
```

*Meaning:* Taking a Skill, forgetting its scripts/assets (Forget), and then re-wrapping it (Free) produces a Skill that is a "stripped" version of the original. **The scripts are lost in the round-trip.** This is the fundamental asymmetry: CMs are losslessly embeddable in Skills, but Skills lose their executable content when projected down to CMs.

### 2.5 Triangle Identities

**Theorem.** The triangle identities hold:

1. (Forget ε) ∘ (η Forget) = id_Forget

```
Forget(Skill) --η--> Forget(Free(Forget(Skill))) --Forget(ε)--> Forget(Skill)
     CM       --id-->          CM                  --id-->          CM
```

Both are identity because η is identity on CMs and Forget(ε) is identity on CMCore.

2. (ε Free) ∘ (Free η) = id_Free

```
Free(CM) --Free(η)--> Free(Forget(Free(CM))) --ε--> Free(CM)
(CM,∅,∅,∅) --id-->    (CM,∅,∅,∅)            --id--> (CM,∅,∅,∅)
```

Both are identity because Free(η) = Free(id) = id and ε on a free skill is identity (nothing to lose).

*Conclusion:* Free ⊣ Forget is a legitimate adjunction. ∎

## 3. Progressive Disclosure as Categorical Operation

### 3.1 The Three Phases

The progressive disclosure lifecycle maps directly to categorical operations:

| Phase | Operation | Input | Output | Tokens |
|-------|-----------|-------|--------|--------|
| **Discover** | Metadata projection | Skill | (name, description) | ~100 |
| **Activate** | Forget | Skill | CM (4 sections) | ≤5000 |
| **Execute** | Identity (if degenerate) or inclusion (if extended) | CM or Skill | Full Skill | Variable |

### 3.2 Formal Definition

**Definition (Progressive Disclosure Functor).** PD is not a single functor but a sequence of projections with increasing information:

```
PD₁ = π_meta ∘ Forget:  Skill_Cat → Set         (discover: just metadata)
PD₂ = Forget:           Skill_Cat → CM_Cat       (activate: CM Core)
PD₃ = Id:               Skill_Cat → Skill_Cat    (execute: everything)
```

with natural transformations:
```
PD₁ ↪ PD₂ ↪ PD₃
```

each injection adds more information to the context window.

### 3.3 Token Economy as Constraint

**Definition.** The token budget T is a natural number constraint on the size of injected content:

```
|Forget(Skill)| ≤ T_activate = 5000 tokens
|π_meta(Skill)| ≤ T_discover = 100 tokens
```

**Theorem (Token Monotonicity).** |PD₁(s)| ≤ |PD₂(s)| ≤ |PD₃(s)| for all Skills s. Progressive disclosure is monotonically increasing in token cost.

## 4. Degenerate vs Extended: Two Objects, One Category

### 4.1 The Degenerate Embedding

**Definition.** A degenerate Skill is an object of Skill_Cat of the form:

```
Skill_deg = (CM, ∅, ∅, ∅, Metadata_minimal)
```

**Theorem.** The subcategory of degenerate Skills is isomorphic to CM_Cat:

```
CM_Cat ≅ Skill_deg ↪ Skill_Cat
```

via the embedding CM ↦ (CM, ∅, ∅, ∅, derived_metadata).

*This is η expressed as a functor.* The degenerate Skills ARE CMs, living inside Skill_Cat.

### 4.2 The Extended Form

**Definition.** An extended Skill is an object with at least one non-empty optional component:

```
Skill_ext = (CM, Scripts, References, Assets, Metadata_full)
where Scripts ∪ References ∪ Assets ≠ ∅
```

**Theorem (Extension is Information Gain).** For any extended Skill s:

```
Free(Forget(s)) ≠ s    (strict inequality — information is lost)
```

The difference d(s) = s \ Free(Forget(s)) = (Scripts, References, Assets) is the **executable content** that the adjunction cannot recover.

### 4.3 Promotion

**Definition (Promotion).** Promoting a degenerate Skill to extended is the operation:

```
Promote: Skill_deg → Skill_ext
Promote(CM, ∅, ∅, ∅, M_min) = (CM, Scripts_new, Refs_new, Assets_new, M_full)
```

**Theorem.** Promotion preserves the CM Core:

```
Forget(Promote(s)) = Forget(s)    for all degenerate Skills s
```

*Meaning:* You can add scripts/assets to a Skill without changing its cognitive content. The CM Core is invariant under promotion.

## 5. Integration with Agent Architecture

### 5.1 Skills as Endofunctors on U

**Connection to 01-agent-coalgebra.** A CM is an endofunctor on the state space U:

```
CM: U → U    (transforms the agent's state)
```

A Skill extends this with executable side-effects:

```
Skill: U → M(U)    (transforms the agent's state with effects)
```

The Forget functor projects Skill back to the pure CM:

```
Forget(Skill): U → U    (the pure cognitive transformation, without scripts)
```

### 5.2 Lazy Evaluation = Forget + Inject

When the FSM invokes a Skill at runtime:

1. **Lazy mode (default):** The runtime applies Forget, extracting the CM Core, and injects only the 4 sections into the context window. Cost: ≤5000 tokens.

2. **Full mode:** The runtime keeps the full Skill (identity functor), mounting scripts and references as needed. Cost: variable.

The choice between modes is determined by the Skill's complexity and the FSM's requirements.

### 5.3 allowed-tools ⊆ F

**Theorem (Tool Containment).** For any Skill s in an agent with interface functor F_declared:

```
allowed-tools(s) ⊆ F_declared
```

The tools a Skill can use are a subset of the tools the agent can use. This is a functorial constraint: the inclusion Skill ↪ Agent respects the interface functor.

### 5.4 requires ⊆ M

**Theorem (Monad Compatibility).** For any Skill s in an agent with effect monad M:

```
requires(s) ⊆ capabilities(M)
```

The dependencies a Skill declares must be satisfiable by the agent's monad. If M = strict sandbox with no Bash access, a Skill requiring Bash is incompatible.

## 6. The Algebra of Skill Composition

### 6.1 Sequential Composition

**Definition.** Given Skills s₁: U → M(U) and s₂: U → M(U), their sequential composition is Kleisli composition:

```
s₂ >=> s₁: U → M(U)
(s₂ >=> s₁)(u) = s₁(u) >>= s₂
```

*Meaning:* Execute s₁, feed its result to s₂. The monad M handles effects between steps.

### 6.2 Parallel Composition

**Definition.** Given Skills s₁: U₁ → M(U₁) and s₂: U₂ → M(U₂) operating on independent fibers:

```
s₁ ⊗ s₂: U₁ × U₂ → M(U₁ × U₂)
(s₁ ⊗ s₂)(u₁, u₂) = do { u₁' ← s₁(u₁); u₂' ← s₂(u₂); return (u₁', u₂') }
```

**Theorem.** Parallel composition preserves the adjunction:

```
Forget(s₁ ⊗ s₂) = Forget(s₁) ⊗ Forget(s₂)
```

Forgetting a parallel composition = parallel composition of forgotten Skills.

## Sources

- Mac Lane, S. "Categories for the Working Mathematician" — Chapter IV (Adjunctions)
- Awodey, S. "Category Theory" — Chapter 10 (Monads and Algebras)
- Barr & Wells. "Category Theory for Computing Science" — Chapter 3 (Free constructions)
