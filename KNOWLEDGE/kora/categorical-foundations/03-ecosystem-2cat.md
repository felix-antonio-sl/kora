---
_manifest:
  urn: urn:kora:kb:cat-ecosystem-2cat
  provenance:
    created_by: FS
    created_at: '2026-02-26'
    source: "Leinster (Basic Category Theory), Spivak (Categorical Systems Theory), Benabou (2-categories), KORA agent-spec-md v6.0.0 §13"
version: 1.0.0
status: published
tags:
- category-theory
- 2-category
- ecosystem
- interoperability
- formal-layer
- kora
lang: en
---

# The 2-Category Eco: Interoperability of Agents

## Purpose

This document formalizes the KORA agent ecosystem as a 2-category **Eco**. While 01-agent-coalgebra defines a single agent, this document defines how multiple agents relate, compose, migrate, and interoperate. The 2-categorical structure provides the formal basis for interoperability — the ability to translate, compose, restrict, and promote agents across the ecosystem.

## Prerequisites

All notation and definitions from [00-foundations](urn:kora:kb:cat-foundations) §10 (2-categories). The agent model from [01-agent-coalgebra](urn:kora:kb:cat-agent-coalgebra).

## 1. Definition of Eco

### 1.1 The 2-Category

**Definition.** Eco is a 2-category with:

**0-cells (objects):** Agents. Each 0-cell is an F-coalgebra (U, c: U → F(U)) in Kl(M) with a valid workspace (5 components + skills/).

**1-cells (morphisms):** Inter-agent functors. A 1-cell T: A → B is a structure-preserving transformation between agents that maps states to states, transitions to transitions, and tools to tools.

**2-cells (2-morphisms):** Natural transformations between 1-cells. A 2-cell α: T ⇒ T' (where T, T': A → B) is a coherent family of adaptations between two inter-agent functors.

### 1.2 Composition

**1-cell composition.** Given T: A → B and S: B → C, the composite S ∘ T: A → C is defined componentwise:
- (S ∘ T)_states = S_states ∘ T_states
- (S ∘ T)_transitions = S_transitions ∘ T_transitions
- (S ∘ T)_tools = S_tools ∘ T_tools

**2-cell vertical composition.** Given α: T ⇒ T' and β: T' ⇒ T'' (all A → B):
- (β • α)_u = β_u ∘ α_u for each state u ∈ U_A

**2-cell horizontal composition.** Given α: T ⇒ T' (both A → B) and β: S ⇒ S' (both B → C):
- (β ∗ α): S ∘ T ⇒ S' ∘ T'

**Theorem (Interchange Law).** For composable 2-cells:

```
(β' • α') ∗ (β • α) = (β' ∗ β) • (α' ∗ α)
```

*Proof:* Follows from the naturality of 2-cells and the functoriality of composition.

### 1.3 Identity

**0-cell identity.** For each agent A, the identity 1-cell id_A: A → A maps everything to itself.

**1-cell identity.** For each 1-cell T: A → B, the identity 2-cell 1_T: T ⇒ T is the identity natural transformation.

## 2. 0-Cells: Agents as Objects

### 2.1 Agent Identity

**Definition.** Two 0-cells A₁ and A₂ are **equal** in Eco iff they are bisimilar:

```
A₁ = A₂  in Eco  ⟺  A₁ ~ A₂  (bisimilar)
```

*Consequence:* An agent's identity is its behavior, not its implementation. Two workspaces with different file contents but identical observable behavior are the same 0-cell.

### 2.2 The Agent Inventory

**Observation (KORA Monorepo Q1 2026).** The current monorepo contains 51 0-cells distributed across 7 namespaces:

| Namespace | 0-cells | Domain |
|-----------|---------|--------|
| fxsl | 20 | Technical/personal |
| gn | 12 | Regional governance |
| kora | 8 | Framework governance |
| ops | 7 | Operations/swarm |
| korvo | 2 | Personal assistant |
| orko | 1 | Specialized domain |
| tde | 1 | Digital transformation |

### 2.3 Fiber Preservation

**Theorem.** A valid 0-cell must have its state space decomposed into orthogonal fibers (01-agent-coalgebra §2.1). The segregation principle ensures that 0-cell identity depends only on the control fiber (c, F), not the phenomenological fiber (U_phen).

**Corollary.** Changing SOUL.md (personality) while keeping AGENTS.md and TOOLS.md fixed produces a bisimilar agent — hence the same 0-cell in Eco.

## 3. 1-Cells: Inter-Agent Functors

### 3.1 Classification

**Definition.** The 1-cells of Eco classify into 4 types based on what they preserve and transform:

#### Type T (Translation)

```
T: A → B
```

Maps the states and transitions of agent A to states and transitions of agent B. T preserves the FSM structure.

**Formal definition:** T consists of:
- T_obj: Ob(FSM_A) → Ob(FSM_B) (state mapping)
- T_mor: Mor(FSM_A) → Mor(FSM_B) (transition mapping)
- T_tools: F_A → F_B (tool mapping)

such that T preserves composition and identity (functorial).

**Examples:**
- Agentification G₂: KODA_agent → KORA_agent (document 01-agent-coalgebra, derived from agent-spec-md §12)
- Version migration: goreologo_v2 → goreologo_v3

#### Type C (Composition)

```
C: A × B → AB
```

Composes two agents into a multi-agent system via a wiring diagram W.

**Formal definition:** C consists of:
- The wiring diagram W that connects outputs of A to inputs of B (and vice versa)
- The composite state space U_AB = U_A × U_B
- The composite transition c_AB determined by W

**Examples:**
- orquestador-swarm + deployer → deployment pipeline
- Master + sub-agent adjunction (Left ⊣ Right from 01-agent-coalgebra §6.2)

#### Type R (Restriction)

```
R: A → A'    where A' is a "smaller" agent
```

Restricts the interface functor F or the effect monad M of an agent, producing a constrained version.

**Formal definition:** R consists of:
- R_tools: F_A → F_A'  where F_A' ⊆ F_A (tool subset)
- R_monad: M_A → M_A'  where M_A' is more restrictive than M_A
- Identity on states and transitions (FSM unchanged)

**Examples:**
- Sandboxing: agent with permissive M → agent with strict M
- Sub-agent instantiation: master → child (inherits c and restricted F, dissipates U_phen)

#### Type P (Promotion)

```
P: A → A+    where A+ has more capabilities
```

Extends the interface functor F with discovered Skills, producing an enhanced version.

**Formal definition:** P consists of:
- P_tools: F_A ↪ F_A+  where F_A ⊆ F_A+ (tool superset)
- Identity on states, transitions, and monad
- The additional tools come from the Discovery Presheaf (document 04)

**Examples:**
- Skill discovery: agent discovers new Skills at runtime, F grows monotonically
- Capability upgrade: agent v1 → agent v1 + new skill

### 3.2 Bisimulation Preservation

**Theorem (Fundamental Property of 1-cells).** Every 1-cell in Eco preserves bisimulation:

```
If u₁ ~ u₂ in A, then T(u₁) ~ T(u₂) in B
```

for any 1-cell T: A → B.

*Proof:* For type T (Translation), the bisimulation relation R lifts along T: if (u₁, u₂) ∈ R then (T(u₁), T(u₂)) ∈ T(R) because T preserves transitions. For type R (Restriction), restricting tools cannot break bisimulation — it can only make more behaviors equivalent (fewer distinguishing tools). For type P (Promotion), adding tools never breaks existing bisimulations.

*Consequence:* Interoperable agents remain interchangeable under any 1-cell transformation.

### 3.3 Integration with Existing Constructions

**Theorem.** The constructions defined in 01-agent-coalgebra are 1-cells of Eco:

| Construction | 1-cell type | Source |
|--------------|-------------|--------|
| Wiring diagram W | Composition (C) | 01-agent-coalgebra §6 |
| Sub-agent adjunction Left ⊣ Right | Composition (C) + Restriction (R) | 01-agent-coalgebra §6.2 |
| Agentification functor G | Translation (T) | agent-spec-md §12 |
| Koraficación functor K | Not a 1-cell in Eco (operates on documents, not agents) | md-spec §6 |

## 4. 2-Cells: Natural Transformations

### 4.1 Definition

**Definition.** A 2-cell α: T ⇒ T' (where T, T': A → B) assigns to each state u of agent A a morphism:

```
α_u: T(u) → T'(u)    in agent B
```

such that for every transition t: u → v in A:

```
        T(t)
  T(u) -----→ T(v)
   |            |
   | α_u        | α_v
   ↓            ↓
  T'(u) ----→ T'(v)
        T'(t)
```

commutes.

### 4.2 Naturality = Coherence

**Theorem (Commutativity).** The commutativity of the naturality square guarantees that the adaptation α is coherent: adapting before or after a transition yields the same result.

*Meaning:* If α adapts functor T to T', it does so uniformly across all states. There's no "state-dependent adaptation" — the adaptation is systematic.

### 4.3 Cases of Use

#### Version Migration

**Definition.** Given Agentification functors G_v5 and G_v6 (both translating KODA agents to KORA workspaces), a 2-cell α: G_v5 ⇒ G_v6 adapts v5-style workspaces to v6-style workspaces.

```
For every KODA agent X:
  G_v5(X) --α_X--> G_v6(X)
  v5 workspace      v6 workspace (with §13, §14)
```

Naturality ensures that for any KODA transformation f: X → Y:

```
G_v5(f) followed by α_Y  =  α_X followed by G_v6(f)
```

*Meaning:* It doesn't matter whether you first migrate the agent and then upgrade the workspace format, or first upgrade the format and then migrate. The result is the same.

#### Cross-Vendor Interop

**Definition.** Given translation functors T_claude and T_gpt (both A → B, adapting an agent for Claude vs GPT runtimes), a 2-cell α: T_claude ⇒ T_gpt adapts Claude-optimized agents to GPT-optimized agents.

**Constraints on α:**
- α must preserve CMCore (Forget(α(Skill)) = Forget(Skill))
- α may change injection format (XML tags for Claude → Markdown headers for GPT)
- α must preserve bisimulation (runtime change doesn't change behavior)

#### Runtime Adaptation

**Definition.** Given injection strategies inject_lazy and inject_full (both Skill_Cat → Context_Window), a 2-cell α: inject_lazy ⇒ inject_full adapts from lazy evaluation (Forget + inject) to full evaluation (identity + inject).

```
inject_lazy(Skill) --α--> inject_full(Skill)
(CM Core only)             (CM Core + scripts + refs)
```

## 5. Properties of Eco

### 5.1 Eco is Locally Small

**Theorem.** For any two 0-cells A, B in Eco, the hom-category Eco(A, B) (whose objects are 1-cells A → B and morphisms are 2-cells between them) is a small category.

*Proof:* The set of 1-cells from A to B is bounded by the finite set of FSM state mappings × tool mappings × monad mappings. The set of 2-cells between any two 1-cells is bounded by the product of morphism sets at each state.

### 5.2 Eco Has Identities at All Levels

- Every 0-cell A has identity 1-cell id_A
- Every 1-cell T has identity 2-cell 1_T
- Composition is associative and unital at both levels

### 5.3 Eco is Enriched over Cat

**Theorem.** Eco is a Cat-enriched category (a strict 2-category). The hom-categories Eco(A, B) are categories in their own right, and composition of 1-cells is a functor:

```
∘: Eco(B, C) × Eco(A, B) → Eco(A, C)
```

*This means:* Composition respects the 2-cell structure. If you have 2-cells adapting functors, the adapted composite is the composite of adaptations.

## 6. The Landscape of Eco (KORA Q1 2026)

### 6.1 Current 1-Cells in the Monorepo

| 1-Cell | Type | Source | Target |
|--------|------|--------|--------|
| orquestador-swarm → deployer | C (Composition) | ops/orquestador-swarm | ops/deployer |
| orquestador-swarm → tester | C (Composition) | ops/orquestador-swarm | ops/tester |
| orquestador-swarm → observer | C (Composition) | ops/orquestador-swarm | ops/observer |
| orquestador-swarm → integrador | C (Composition) | ops/orquestador-swarm | ops/integrador |
| orquestador-swarm → security | C (Composition) | ops/orquestador-swarm | ops/security |
| ingeniero-goreos → goreologo | C (Composition) | gn/ingeniero-goreos | gn/goreologo |
| G₂ (Agentification) | T (Translation) | KODA agents | KORA agents |

### 6.2 Current 2-Cells

| 2-Cell | Between | Effect |
|--------|---------|--------|
| G_v5 ⇒ G_v6 | Agentification versions | Adds §13 (Eco) and §14 (Presheaf) to output workspace |

### 6.3 Unrealized 1-Cells (Gaps)

The following 1-cells are structurally implied but not yet declared in any agent:

| Potential 1-cell | Type | Why it's needed |
|------------------|------|-----------------|
| Cross-namespace composition | C | gn agents composing with fxsl agents |
| Runtime-to-runtime translation | T | Claude ↔ GPT agent adaptation |
| Hierarchical restriction | R | Formal sandboxing beyond config.json |
| Skill-based promotion | P | Agents gaining capabilities from discovery |

## Sources

- Leinster, T. "Basic Category Theory" — Chapter 1.3 (2-categories)
- Benabou, J. "Introduction to Bicategories" — 2-categorical foundations
- Spivak, D. "Categorical Systems Theory" — Chapter 7 (compositional systems)
- Kelly, G.M. "Basic Concepts of Enriched Category Theory" — Cat-enriched categories
