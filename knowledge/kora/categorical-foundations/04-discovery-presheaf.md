---
_manifest:
  urn: urn:kora:kb:cat-discovery-presheaf
  provenance:
    created_by: FS
    created_at: '2026-02-26'
    source: "Fong & Spivak (Seven Sketches, Ch. 7 Sheaves), Mac Lane & Moerdijk (Sheaves in Geometry and Logic), KORA agent-spec-md v6.0.0 §14"
version: 1.0.0
status: published
tags:
- category-theory
- presheaf
- discovery
- dynamic-capability
- formal-layer
- kora
lang: en
---

# The Discovery Presheaf Psh(F)

## Purpose

This document formalizes the mechanism by which KORA agents discover Skills at runtime without violating the closed algebra property of the interface functor F. The solution is a presheaf Psh(F) over the Eco 2-category that assigns to each agent its set of discoverable Skills, and a fibered coproduct F_eff that composes declared tools with discovered Skills.

This is the formal foundation for dynamic capability — the ability of agents to grow their capabilities while maintaining design-time verifiability.

## Prerequisites

All notation from [00-foundations](urn:kora:kb:cat-foundations) §8-9 (coproducts, presheaves). The agent model from [01-agent-coalgebra](urn:kora:kb:cat-agent-coalgebra) §4 (interface functor F). The 2-category from [03-ecosystem-2cat](urn:kora:kb:cat-ecosystem-2cat).

## 1. The Problem

### 1.1 The Tension

From 01-agent-coalgebra §4.1, the interface functor F has closed algebra:

```
Theorem (Closure): The agent can only invoke tools declared in F_declared.
```

But dynamic ecosystems need agents to discover new Skills at runtime. A goreologo agent that discovers a new legal analysis Skill should be able to use it without modifying TOOLS.md.

### 1.2 The Constraint

Any solution must preserve:
1. **Design-time verifiability:** F_declared must remain checkable without executing the agent
2. **Runtime extensibility:** The agent can discover and use new Skills
3. **Security filtering:** The monad M (config.json) filters what can be discovered
4. **Monotonicity:** Once discovered, a Skill doesn't disappear during the session

### 1.3 The Solution Strategy

Distinguish between F_declared (immutable, closed) and F_discovered (growing, filtered). Compose them via fibered coproduct into F_eff (the effective interface). The presheaf Psh(F) formalizes which Skills are discoverable by each agent.

## 2. The Discovery Functor D

### 2.1 The Registry Category

**Definition.** Reg is the category of Skill registries:

**Objects:** Registries — collections of Skills indexed by metadata:

```
Registry = { (name, description, urn, location, requires, allowed-tools) }
```

Each registry is a set of Skill metadata records.

**Morphisms:** Inclusions i: R₁ ↪ R₂ where every record in R₁ appears in R₂.

**Properties:**
- Reg is a poset (ordered by inclusion)
- Reg has joins (union of registries) and meets (intersection)
- Reg has an initial object (empty registry) and a terminal object (universal registry containing all Skills)

### 2.2 Key Registries in KORA

| Registry | Location | Contents |
|----------|----------|----------|
| R_local(A) | agents/{ns}/{name}/skills/ | Skills in agent A's workspace |
| R_federated(ns) | skills/{ns}/ | Federated Skills for namespace ns |
| R_global | skills/ (all namespaces) | All federated Skills |
| R_catalog | catalog/catalog_master_kora.yml | All indexed Skills in monorepo |

**Inclusion chain:**

```
R_local(A) ↪ R_federated(ns) ↪ R_global ↪ R_catalog
```

### 2.3 The Discovery Functor

**Definition.** D: Reg → Set maps registries to sets of discoverable Skills:

```
D(R) = { Skill s ∈ R | s is well-formed per skill-spec-md }
```

On morphisms (inclusions):

```
D(i: R₁ ↪ R₂): D(R₁) ↪ D(R₂)
```

D maps inclusions to inclusions (functorial on the poset Reg).

**Theorem (Functoriality of D).**

1. D(id_R) = id_{D(R)} (identity preserved)
2. D(j ∘ i) = D(j) ∘ D(i) (composition preserved)
3. If R₁ ⊆ R₂ then D(R₁) ⊆ D(R₂) (monotone)

*Proof:* Each follows from the monotonicity of inclusion.

### 2.4 Filtered Discovery

**Definition (M-Filtering).** Given an agent A with effect monad M_A (materialized as config.json), the filtered discovery functor is:

```
D_M: Reg → Set
D_M(R) = { s ∈ D(R) | compatible(s, M_A) }

where compatible(s, M_A) ⟺
  allowed-tools(s) ⊆ tools.allow(M_A)  AND
  allowed-tools(s) ∩ tools.deny(M_A) = ∅  AND
  requires(s) satisfiable in sandbox(M_A)
```

**Theorem (D_M is a subfunctor of D).** D_M(R) ⊆ D(R) for all R, and D_M preserves inclusions.

*Meaning:* The monad M acts as a filter on discovery. An agent with strict sandbox can only discover Skills that don't require forbidden tools. This is the security boundary.

**Example:**

```
Agent: goreologo (sandbox: strict, tools.deny: [web_search])
Registry R contains: CM-evaluador-riesgo (allowed-tools: [search_kb])
                     CM-web-scraper (allowed-tools: [web_search])

D_M(R) = { CM-evaluador-riesgo }    (web-scraper filtered out by M)
```

## 3. The Presheaf Psh(F)

### 3.1 Definition

**Definition.** Psh(F): Eco^op → Set is the presheaf that assigns to each agent its set of discoverable Skills:

```
Psh(F)(A) = D_M_A(R_accessible(A))
```

where R_accessible(A) is the union of all registries accessible to agent A.

On 1-cells (contravariant): given T: A → B in Eco, the induced map is:

```
Psh(F)(T): Psh(F)(B) → Psh(F)(A)
```

### 3.2 Contravariance Explained

**Theorem.** Psh(F) is contravariant: if there's a 1-cell T: A → B (A maps to B), then the discoverable Skills of B restrict to discoverable Skills of A.

*Intuition:* A 1-cell T: A → B means "A can play the role of B" (there's a translation). But that doesn't mean A can discover everything B can — the discoverable set restricts along the translation.

**Formally:** The restriction map Psh(F)(T) is:

```
Psh(F)(T)(s) = s ∘ T    for Skill s discoverable by B
```

The Skill s, originally designed for B, is "pulled back" along T to work with A. This pullback may fail (if T doesn't preserve the tools s needs), in which case s is not in the image.

### 3.3 Yoneda Perspective

**Theorem (Representability).** For a fixed registry R, the presheaf Psh(F) is the subfunctor of the representable presheaf y(R) filtered by M:

```
Psh(F) ↪ Hom_Eco(−, R_global)
```

*Meaning:* The discoverable Skills of agent A are (a subset of) the ways A can "reach" the global registry. The Yoneda lemma tells us this is determined by the agent's structure.

## 4. The Effective Interface F_eff

### 4.1 The Fibered Coproduct

**Definition.** The effective interface of agent A is the fibered coproduct (pushout):

```
F_eff(A) = F_declared(A) +_D F_discovered(A)
```

where:
- F_declared(A) = tools declared in TOOLS.md (closed, immutable)
- F_discovered(A) = D_M_A(R_accessible(A)) = Skills discovered at runtime
- The fibration is over D: tools that appear in both F_declared and F_discovered are identified (no duplicates)

**Construction:** The pushout is computed as:

```
           D
     F_declared ←--- D(R) ---→ F_discovered
          \                      /
           \                    /
            ↘                  ↙
              F_eff = F_declared +_D F_discovered
```

where D(R) maps to F_declared via the tool declarations and to F_discovered via the discovery functor.

### 4.2 Properties

**Theorem 1 (F_declared Embeds).** The canonical injection ι₁: F_declared ↪ F_eff is injective. Every declared tool remains available.

**Theorem 2 (F_discovered Embeds).** The canonical injection ι₂: F_discovered ↪ F_eff is injective (after identification of duplicates).

**Theorem 3 (No Duplicates).** If a tool t appears in both F_declared and F_discovered, it appears exactly once in F_eff (identified by the pushout).

**Theorem 4 (Design-Time Closure Preserved).** F_declared is verifiable without executing D. The closure theorem from 01-agent-coalgebra §4.1 applies to F_declared, not to F_eff.

**Theorem 5 (Monotonicity).** During a session, F_discovered can only grow:

```
F_discovered(t₁) ⊆ F_discovered(t₂)    for t₁ ≤ t₂ (time ordering)
```

Once a Skill is discovered, it remains in F_eff for the rest of the session.

*Proof:* D_M is monotone on Reg. During a session, the accessible registries can only grow (new registries become accessible) or stay constant (no registry removal). Therefore D_M(R_accessible) is monotone in time.

### 4.3 F_eff and the Agent Coalgebra

**Theorem (Extended Coalgebra).** The agent with effective interface is an F_eff-coalgebra:

```
(U, c_eff: U → F_eff(U))    in Kl(M)
```

where c_eff extends c by allowing transitions that invoke discovered Skills. The original c (using only F_declared) factors through c_eff:

```
c = ι₁ ∘ c_eff|_{F_declared}
```

*Meaning:* The original agent behavior is a sub-behavior of the extended agent. Everything the agent could do before, it can still do. Discovery only adds new capabilities.

## 5. Progressive Disclosure in the Presheaf

### 5.1 The Four Phases

The progressive disclosure lifecycle (02-skill-algebra §3) maps to presheaf operations:

| Phase | Presheaf operation | F involved | Tokens |
|-------|-------------------|------------|--------|
| **Bootstrap** | — | F_declared | TOOLS.md size |
| **Discover** | Evaluate Psh(F)(A) | D scans registries | ~100/skill |
| **Activate** | Forget(selected Skill) | F_eff grows | ≤5000 |
| **Execute** | Id(selected Skill) | F_eff complete | Variable |

### 5.2 Formal Lifecycle

```
1. Bootstrap:  agent loads with F = F_declared
2. Discover:   runtime evaluates Psh(F)(A) → metadata set (name, description per Skill)
3. FSM gates:  transition condition determines if a discovered Skill should be activated
4. Activate:   F_eff = F_declared + {selected Skill}
               runtime injects Forget(Skill) = CM Core into context window
5. Execute:    if CM Core references scripts, runtime mounts full Skill directory
6. Loop:       return to step 2 (more Skills may become discoverable)
```

### 5.3 Presheaf Consistency

**Theorem (Session Consistency).** Within a single session, the presheaf evaluation is consistent:

```
If Psh(F)(A) = S at time t₁, then Psh(F)(A) ⊇ S at time t₂ > t₁
```

The set of discoverable Skills never shrinks during a session.

*Proof:* Registries don't lose entries during a session (registry mutations are session-external). D_M is monotone. Therefore Psh(F) is monotone in time.

## 6. Invariants

### 6.1 Summary of Invariants

| # | Invariant | Formal statement | Traces to |
|---|-----------|-----------------|-----------|
| I1 | Monotonicity | F_discovered(t₁) ⊆ F_discovered(t₂) for t₁ ≤ t₂ | §4.2 Theorem 5 |
| I2 | Filtered Discovery | D_M(R) ⊆ D(R) and compatible(s, M) for all s ∈ D_M(R) | §2.4 |
| I3 | Design-time Closure | F_declared is verifiable without executing D | §4.2 Theorem 4 |
| I4 | Presheaf Functoriality | Psh(F)(S ∘ T) = Psh(F)(T) ∘ Psh(F)(S) (contravariant) | §3.1 |
| I5 | No Shrinkage | Psh(F)(A) never shrinks during a session | §5.3 |
| I6 | M-Boundary | D_M ⊆ D (monad filters discovery) | §2.4 |

### 6.2 Violation Detection

| Invariant violated | Symptom | Root cause |
|--------------------|---------|------------|
| I1 (Monotonicity) | Skill disappears mid-session | Registry mutation during session |
| I2 (Filtered) | Agent uses forbidden tool via Skill | D_M not checking allowed-tools vs M |
| I3 (Design-time) | Cannot validate agent without running it | F_declared contaminated with runtime data |
| I4 (Functoriality) | Inconsistent discovery across composed agents | Psh(F) not respecting 1-cell contravariance |
| I5 (No shrinkage) | Fewer Skills available later in session | Registry or filter changed mid-session |
| I6 (M-Boundary) | Strict-sandbox agent discovers unsafe Skill | M filter bypassed or misconfigured |

## 7. Relationship to Other Documents

| Document | Connection |
|----------|------------|
| 01-agent-coalgebra §4 | Psh(F) extends the closed algebra of F to F_eff |
| 02-skill-algebra §3 | Progressive Disclosure maps to presheaf evaluation phases |
| 02-skill-algebra §5.3 | allowed-tools ⊆ F_declared is preserved: allowed-tools ⊆ F_eff |
| 03-ecosystem-2cat §3.1 | Promotion (Type P) 1-cells are the morphisms induced by Psh(F) |
| 03-ecosystem-2cat §3.3 | D-based discovery creates the 1-cells that Eco classifies |

## Sources

- Mac Lane, S. & Moerdijk, I. "Sheaves in Geometry and Logic" — Chapter I (presheaves)
- Fong & Spivak. "Seven Sketches in Compositionality" — Chapter 7 (sheaves and information flow)
- Awodey, S. "Category Theory" — Chapter 8 (presheaves, Yoneda)
