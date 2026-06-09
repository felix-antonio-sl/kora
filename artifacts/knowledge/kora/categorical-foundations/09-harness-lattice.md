---
_manifest:
  urn: urn:kora:kb:cat-harness-lattice
  provenance:
    created_by: Claude
    created_at: '2026-06-08'
    source: harness-spec v1.1.0 (PMI×LFS); Davey & Priestley (Introduction to Lattices
      and Order); Libkind-Spivak (Poly) via icas-agencia; KORA categorial audit 2026-06-07
    updated_at: '2026-06-09'
    update_note: '§5 open problem resolved (negatively): naive fibration refuted with
      cause; one restricted interface fibration proved + one carrier reindexing isolated;
      successor open problem restated as a double category. Via adversarial double-attack
      (construct vs refute) under cat-thinking. harness-spec untouched (freeze §8.3).'
  version: 1.1.0
  status: published
  tags:
  - category-theory
  - lattice
  - poset
  - pmi-lfs
  - harness
  - formal-layer
  - kora
  lang: en
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:cat-harness-lattice
relations:
  depends:
    - "urn:kora:kb:cat-foundations"
  cites:
    - "urn:kora:kb:cat-agent-coalgebra"
    - "urn:fxsl:kb:icas-agencia"
---

# The Harness Space as Product Lattice (and its relation to the Agent Coalgebra)

## Purpose

This document brings the foundation of the PMI×LFS ontological space — defined
operationally in `harness-spec` — into the official KORA formal layer, and does
so **honestly**: it formalizes the part that is a theorem (the lattice) and
settles the part that is not (the bridge to the coalgebra) by refuting the naive
fibration with cause, isolating what genuinely survives, and leaving a sharpened
successor open problem.

Concretely it:

1. Formalizes the PMI×LFS space as a **bounded product lattice** in **Pos**.
2. Proves that the five inter-axis consistency laws (`harness-spec` §4.1) cut the
   space down to a **bounded sublattice** of well-formed vectors — the structure
   that `_check_vector_laws` enforces mechanically.
3. States precisely the relationship between this lattice and the agent
   **F-coalgebra** of [01-agent-coalgebra](urn:kora:kb:cat-agent-coalgebra): a
   **shared origin**, but **not a single fibration**. The naive bridge is
   **refuted** with cause (§5.3–§5.4, §6.1), one restricted fibration is proved
   and one carrier reindexing isolated (§6.2), and the correct global object is
   restated as a **double category** (§6.3, the successor open problem).

This resolves the audit finding (2026-06-07, eje 7 / rec. 1) that the
constitution-level claim "PMI×LFS" rested formally only on auxiliary,
non-normative corpus. The order-theoretic content is absorbed here. The
coalgebraic bridge is **also** settled, but negatively: the §6 conjecture of a
single fibration `E → W` is shown impossible (mixed variance over a uniform
order), so nothing is manufactured to disguise a gap; what is absorbed is the
*impossibility theorem* plus the two genuine fibration/opfibration fragments it
leaves behind.

## Prerequisites

All notation from [00-foundations](urn:kora:kb:cat-foundations). The
open-problem section assumes the agent model of
[01-agent-coalgebra](urn:kora:kb:cat-agent-coalgebra). The operational
definitions of the six axes are in `harness-spec` §3.

## 1. The Six Axes as Bounded Lattices

**Definition (axes).** An artifact is characterized by a vector over six axes,
two semantic triples (`harness-spec` §3):

```
PMI (structural):  Π ∈ {0,1,2,3}   Μ ∈ {0,1,2,3}   Ξ ∈ {0,1,2,3,4}
LFS (contextual):  Λ ∈ {0,1,2,3}   Φ ∈ {0,1,2,3,4}   Σ ∈ {0,1,2,3}^5
```

`Σ = [safety_norm, fairness, transparency, accountability, sustainability]`.

**Proposition (each axis is a bounded lattice).** Each of Π, Μ, Ξ, Λ, Φ is a
finite **chain** `0 < 1 < … < n`; a finite chain is a bounded lattice with
`x ∨ y = max(x,y)`, `x ∧ y = min(x,y)`, top `n`, bottom `0`. Σ is a finite
product of five chains `{0..3}`, hence itself a bounded lattice under the
componentwise order, with `⊤_Σ = [3,3,3,3,3]` and `⊥_Σ = [0,0,0,0,0]`.

This is the formal content of "Cada eje es un retículo (poset con join y meet)"
(`harness-spec` §4).

## 2. The Product Lattice V

**Definition (PMI×LFS space).** The harness space is the product

```
V = Π × Μ × Ξ × Λ × Φ × Σ
```

ordered componentwise: `v ≤ w  ⇔  v.k ≤ w.k for every axis k` (with Σ compared
componentwise on its five entries).

**Theorem (bounded product lattice).** `(V, ≤)` is a bounded lattice. Join and
meet are computed componentwise (`(v ∨ w).k = v.k ∨ w.k`, dually for ∧); the top
`⊤_V = (3,3,4,3,4,[3,3,3,3,3])` and bottom `⊥_V = (0,0,0,0,0,[0,0,0,0,0])`.

*Proof.* A finite product of bounded lattices is a bounded lattice, with all
operations componentwise. ∎

**Remark (on the symbol "×").** The "×" in "PMI×LFS" is the **lattice/poset
product**, *not* a categorical product with a universal property. V has
projections `π_k : V → axis_k` that are lattice homomorphisms, but the claim
proved here is order-theoretic (a retículo), the modest and correct reading. The
audit (2026-06-07, eje 6) already established this; this document records it as
the official statement rather than letting "producto categorial" be inferred.

**Remark (semidirect structure ⋉).** `harness-spec` §2 (after `icas-agencia`,
Libkind-Spivak) writes the artifact as `(m_p × c_q × Ξ) ⋉ (Contexto)`: the
contextual triple LFS **modulates** the structural triple PMI, it does not act
freely. Formally this modulation is *not* an extra operation on V; it is exactly
the coupling expressed by the inter-axis laws of §3. The space is a product
lattice whose admissible region is constrained, not a free direct product.

## 3. The Inter-Axis Laws as a Bounded Sublattice

The axes are **not independent**. `harness-spec` §4.1 imposes five obligatory
consistency laws. We give them as order constraints and prove they carve out a
sublattice.

**Definition (the five laws).** For `v ∈ V`:

```
L1   v.Π ≥ 3  ⇒  v.Μ ≥ 1            (fixed-point plans need state)
L2   v.Ξ ≥ 4  ⇒  v.Λ ≥ 1            (operadic interaction needs composition scope)
L3   v.Φ ≥ 2  ⇒  v.Μ ≥ 1            (collaborative coupling needs memory)
L4   v.Σ.accountability ≥ 2 ⇒ v.Σ.transparency ≥ 2   (no attribution without explainability)
L5   v.Λ ≥ 3  ⇒  v.Σ.i ≥ 2 for all i ∈ Σ             (societal scope needs full ethics)
```

A vector that satisfies all five is **well-formed**. Let
`W = { v ∈ V : v ⊨ L1 ∧ L2 ∧ L3 ∧ L4 ∧ L5 }`.

**Lemma (a Horn-monotone constraint cuts a sublattice).** Let `a, b` be two
coordinates of V (entries of axes, with Σ entries counting as coordinates) and
consider a constraint of the form `C : a ≥ k ⇒ b ≥ m` for fixed thresholds
`k, m`. Then `{v ∈ V : v ⊨ C}` is closed under both ∨ and ∧.

*Proof.* Take `v, w ⊨ C`.
- **Meet.** `(v ∧ w).a = min(v.a, w.a)`. If `(v ∧ w).a ≥ k` then `v.a ≥ k` *and*
  `w.a ≥ k`, so `v.b ≥ m` and `w.b ≥ m`, hence
  `(v ∧ w).b = min(v.b, w.b) ≥ m`.
- **Join.** `(v ∨ w).a = max(v.a, w.a)`. If `(v ∨ w).a ≥ k` then `v.a ≥ k` *or*
  `w.a ≥ k`; whichever holds gives `(·).b ≥ m`, hence
  `(v ∨ w).b = max(v.b, w.b) ≥ m`. ∎

**Theorem (W is a bounded sublattice of V).** The set of well-formed vectors `W`
is a sublattice of V closed under ∨ and ∧, with the same top and bottom:
`⊤_V ∈ W` and `⊥_V ∈ W`.

*Proof.* L1, L2, L3, L4 are each Horn-monotone constraints, so by the Lemma each
defines a sublattice. L5 is the finite conjunction of the Horn-monotone
constraints `Λ ≥ 3 ⇒ Σ.i ≥ 2` over the five entries `i`, hence also defines a
sublattice (an intersection of sublattices). `W` is the intersection of all
five, and an intersection of sublattices of V is a sublattice of V. For the
bounds: at `⊥_V` every antecedent (`≥ k`) is false, so all implications hold
vacuously, `⊥_V ∈ W`; at `⊤_V` every consequent is at its maximum, so all
implications hold, `⊤_V ∈ W`. ∎

**Corollary (design closure).** Combining two well-formed artifacts by join
(taking the stronger capability on each axis) or restricting by meet (taking the
weaker) **stays well-formed**. Well-formedness is preserved by the two basic
design operations of the space.

**Mechanization.** `W`-membership is exactly what `_check_vector_laws`
(`toolchain/kora_lib/checks.py`, check `vector-laws`) decides per artifact: a
vector outside `W` is rejected as mal-formado. This theorem is therefore not
decorative — it is the specification of a live check.

## 4. Morphisms of the Space

`harness-spec` §4.3 gives the morphisms of V:

- **Elevation / projection by ≤** — internal to the lattice: `v → v'` when
  `v ≤ v'` (join `v ∨ v'`) or `v'' ≤ v` (meet `v ∧ v'`).
- **Transmutation** — the functor `T_R : V → Ideal_R` to a runtime's realizable
  ideal (see `transmutation-spec` and
  [07-behavioral-preservation](urn:kora:kb:cat-behavioral-preservation)).

**Observation.** The only functor *out of* V that KORA actually constructs lands
in runtimes (`T_R`), not in the category of agent coalgebras. This is the pivot
for §5.

## 5. Relationship to the Agent F-Coalgebra — the diagnosis

This is the honest core of the document, and the resolution of the audit's
critical finding. §5 diagnoses precisely what each axis moves and where the naive
bridge breaks; §6 settles the conjecture on that basis.

### 5.1 Shared origin

Both the PMI×LFS lattice (this document) and the agent F-coalgebra
`(U, c : U → M((Out × U)^In))` of
[01-agent-coalgebra](urn:kora:kb:cat-agent-coalgebra) descend from the **same**
source, `icas-agencia` (Libkind-Spivak): the irreducible triple of a finite
plan (free monad `m_p`), an infinite matter (cofree comonad `c_q`), and an
interaction law `Ξ`. `harness-spec` reads the axes Π, Μ, Ξ directly off this
triple (§3.1).

### 5.2 Divergent readings

The shared origin is read in two different directions:

| | PMI×LFS lattice (doc 09) | Agent coalgebra (doc 01) |
|---|---|---|
| What it captures | **capability classification** | **observable behavior** |
| Ambient category | **Pos** (product lattice) | **Kl(M)-Coalg** |
| Characteristic morphism | order ≤ (elevation/projection) | coalgebra map (preserves behavior) |
| Equivalence | equality of vectors | **bisimulation** |

### 5.3 What each axis actually moves (the localization theorem)

The previous version listed three informal reasons "the bridges fail". They are
now made precise. The key is to ask, for each axis, **which part of the agent
coalgebra `(U, c : U → M(F U))` it controls** — the endofunctor `F`, which
*defines* a fiber, or the object `(U, c)` *inside* a fixed fiber.

Recall `F(U) = (Out × U)^In` (doc 01 §1.1), so `F` is pinned down by the
**interface types `(In, Out)`** alone; by doc 01 §4.1–§4.2 `F` is the *closed,
design-time algebra of declared actions* — the observation boundary, nothing
more.

**Theorem (axis localization).** Under the operational reading of `harness-spec`
§3, the six axes distribute over the coalgebraic data as follows:

| Axis | What it controls (doc 01 / harness §3) | Layer it touches |
|---|---|---|
| **Ξ** interaction | the interface polynomial `p`: positions = `Out`, directions = `In` (`icas-interaccion`) | **the endofunctor `F`** (the would-be base) |
| **Π** plan | the structure map `c = eval ∘ classify`, the FSM (doc 01 §3.1) | object *inside* a fiber |
| **Μ** matter | the carrier `U` (doc 01 §2.1, fibre `U_epi`); Μ↑ enlarges `U` | object *inside* a fiber |
| **Σ** ethics | the effect monad `M` (logging/sandbox), doc 01 §1.3 | the ambient category `Kl(M)` |
| **Λ** sociotechnical | external index level (harness §6) | a *separate* base |
| **Φ** human-AI coupling | re-types `(In, Out)` to add the human channel; coupled to Μ by L3 | partly `F`, partly fiber |

*Proof.* Direct from `F(U) = (Out × U)^In`: only `In, Out` enter `F`, and by
`icas-interaccion` positions/directions are exactly `Out/In`, which Ξ defines.
Π enters only `c` (doc 01 §3.1). Μ enters only the carrier (doc 01 §2.1; harness
§3.1, "Μ-1: coalgebra con `U` acotada"). Σ parametrizes `M`, which by doc 01 §1.3
(M-Immutability) is *immutable from within* — it changes the ambient `Kl(M)`, not
an object of it. Λ is the socio-technical level, external to the single-agent
model. ∎

**Corollary (the conjecture over-indexes).** Two vectors differing only in Μ
(e.g. a delegate with Μ=1 and a persona with Μ=2, harness §5.1) name the **same**
`F` and ought to be two *objects of one fiber*, `(U,c)` and `(U',c')`, not two
*fibers* `F_v ≠ F_{v'}`. Writing `F_v` with the index running over the whole
vector mistakes fiber-content (Π, Μ) for the base. The honest fiber is
"coalgebras over a **fixed** `F`" — which is also the only place where
bisimulation is even well-typed (doc 07 §2.1; doc 01 §5.1).

### 5.4 The variance obstruction (why no fibration over W)

Even after removing the over-indexing, the single axis that *does* move `F`,
namely Ξ, collides with the order of `W`.

**Theorem (mixed variance of the interface functor).** As a functor of its
interface parameters, `F(U) = (Out × U)^In` is **covariant in `Out`** and
**contravariant in `In`** (the exponent `(−)^In`). Hence if `v ≤ v'` enlarges
capability so that both `In_v ↪ In_{v'}` and `Out_v ↪ Out_{v'}`, the induced
components point in **opposite directions**:

```
Out-component:  F_v  ⇒ F_{v'}     (covariant, toward v')
In-component:   F_{v'} ⇒ F_v      (contravariant, toward v)
```

*Proof.* `Out ↪ Out'` gives `(Out × U)^In → (Out' × U)^In`, a natural
transformation `F ⇒ F'`. `In ↪ In'` gives, by restriction along the inclusion,
`(Out × U)^{In'} → (Out × U)^{In}`, a natural transformation `F' ⇒ F`. ∎

**Corollary (no fibration `p : E → W`).** There is no uniform natural
transformation `F_v ⇒ F_{v'}` (nor `F_{v'} ⇒ F_v`) along `≤`, hence no functor of
reindexing between fibers indexed by the *product order* of `W`. A Grothendieck
fibration needs a (pseudo)functor `W^op → Cat` of a **single** variance; an
interface functor of mixed variance can at most be classified over
`W_In^op × W_Out` (two copies of the order, one dualized), **not over `W`**. The
conjecture's fibration `p : E → W` is therefore variance-ill-typed. The category
that *does* absorb this mixed variance by construction is **Poly** (positions
forward, directions backward, `icas-interaccion`); the lattice order of `W` — all
coordinates rising covariantly together — is the wrong variance to flatten Poly
onto. This is the precise form of the old, informal "pull in opposite
directions".

**Remark (`M` is orphan).** Independently, `M` (the effect monad, doc 01 §1.3) is
**no axis of the vector** — beware `Μ`-matter ≠ `M`-effects. If the fibration
fixes one global `M`, the fiber is too coarse (a Powerset agent and an Identity
agent with the same vector are forced together though they are not bisimilar); if
`M` is meant to co-vary, that is false by M-Immutability. Either way `W`
underspecifies the fiber.

## 6. Resolution of the conjecture

The question that the previous version of §5 left open was:

> **Conjecture (harness–coalgebra fibration).** There is a fibration
> `p : E → W` whose fiber over a well-formed vector `v` is a category of
> `F_v`-coalgebras realizing capability `v`, with reindexing along `≤`
> compatible with `T_R`.

It is now settled.

### 6.1 Negative part — the conjecture is refuted

By the Corollary of §5.3 and the Corollary of §5.4, no such fibration over `W`
exists. The failure is structural and threefold — base/fiber type error (Π, Μ
index fiber-content, not the base), mixed variance over a uniform order, and
orphan `M` — not a missing coherence lemma. Independent double-attack (one
construction pass, one refutation pass, under `cat-thinking`) converges on the
same obstruction.

### 6.2 Positive part — two genuine sub-structures

The mixed variance splits into two coherent halves: one a full theorem, one a
reindexing functor whose opfibration status is left open.

> **Theorem (interface fibration).** Fix Π, Μ, Λ, Φ, Σ and `M`; let `W_Ξ ⊆ W`
> vary only Ξ. Then `Φ_Ξ : W_Ξ^op → Cat`, `v ↦ F_v`-`Coalg` in `Kl(M)`, is a
> pseudofunctor whose reindexing along `v ≤ v'` is the dependent lens
> `λ : p_v → p_{v'}` (`icas-interaccion`): `λ^*(U, c) = (U, F_λ ∘ c)`, with
> `F_λ : F_{v'} ⇒ F_v` induced by `(λ_1` forward on `Out`, `λ^♯` backward on
> `In)`. Its Grothendieck construction `∫Φ_Ξ → W_Ξ` (`icas-extension`) is a
> fibration.
>
> *Proof.* Lenses compose (positions forward, directions backward); precomposition
> with the induced natural transformation is functorial; pseudo-functoriality
> follows from associativity of lens composition; the Grothendieck construction of
> any pseudofunctor is a fibration. ∎

> **Proposition (carrier reindexing).** Fix the interface `(In, Out)` (hence `F`)
> and `M`; let `B ⊆ W` vary only Μ and Π. Then `v ≤ v'` induces a **co**variant
> reindexing `F-Coalg_v → F-Coalg_{v'}` given by the sub-coalgebra inclusion
> `S ⊆ U'` of structural safety `S_struct` (harness §4.2, `α(S) ⊆ F(S)`): a genuine
> coalgebra morphism (doc 00 §6), not a comparison *between* the two global
> structures but an inclusion *within* one fiber — the "only genuine point of
> contact" the previous version had isolated, decided by the
> `coalgebra-conformance` / `safety-closure` checks over a finite state machine.
>
> *Open step (honest boundary).* Whether this reindexing assembles into a full
> **opfibration** `E_B → B` (with opcartesian liftings and their universal
> property) is **not** proved here; it is the vertical half of the successor
> problem (§6.3). The reindexing functor is established; its opcartesian
> universality is conjectural. The interface fibration above is the only half
> proved outright.

### 6.3 The correct global object is a double category, not a fibration

The two results of §6.2 are the **horizontal** (interface; Ξ; contravariant;
lenses; proved a fibration) and **vertical** (carrier; Μ, Π; covariant;
sub-coalgebra inclusions; reindexing established, opfibration pending) edges of a
**double category** whose cells are agents. This is the ambient
(`Org`, `icas-agencia`) that tolerates mixed variance without forcing one
direction. It is *not* a fibration over `W`, and naming it correctly is part of
the result.

> **Successor open problem (harness double category).** Construct explicitly the
> double category `𝔻` with objects = interfaces `(In,Out)`, horizontal morphisms =
> interface lenses (Ξ), vertical morphisms = carrier inclusions (Μ, Π), and cells =
> `F`-coalgebras; prove its interchange law and identify which sub-double-category
> `T_R` preserves. This *replaces* the refuted §6 conjecture.

### 6.4 Compatibility with `T_R`

Where reindexing exists, `T_R` is compatible only **laxly**: `transmutation-spec`
§3.2 makes `T_R` monotone in Π by construction and *declares* (does not yet
mechanize) preservation of the `S_struct` inclusion; transmutation admits declared
loss, so the square commutes only up to the 2-cell of declared loss recorded in
`_transmutation.yml`. The clause does not rescue the general conjecture; it is
vacuous exactly where the reindexing is undefined.

### 6.5 Status and governance after resolution

- The negative result **confirms** — and sharpens to a theorem — the conservative
  statement that `harness-spec` already carries (§4 trace: "no morfismo
  demostrado"). It is now "no fibration *can* exist over `W`, by mixed variance".
  No edit to `harness-spec` is required and **no ADR is triggered**: refuting the
  conjecture adds no doctrine to the frozen spec (`gobernanza` §8.3).
- The two positive theorems (§6.2) are **new formal-layer content**, recorded
  here. Pointing `harness-spec` at them as a foundation *would* edit the frozen
  spec and is therefore deferred to an explicit ADR — not performed here.
- The double-category reconstruction (§6.3) is the **successor open problem**,
  replacing the conjecture this document refutes.

## 7. What This Document Does and Does Not Establish

**Establishes (theorems):**

- Each axis is a bounded lattice; V is a bounded product lattice (§1–§2).
- The five inter-axis laws carve out a **bounded sublattice** `W` of well-formed
  vectors, closed under join and meet (§3) — the exact contract of the
  `vector-laws` check.
- **Axis localization (§5.3):** only Ξ moves the endofunctor `F`; Π and Μ move the
  object *inside* a fiber; Σ moves the ambient `M`; Λ is an external index.
- **Variance obstruction (§5.4):** `F = (Out × U)^In` has mixed variance, so **no
  fibration exists over the uniform order of `W`** — the conjecture is refuted
  with cause (§6.1).
- **The interface fibration over Ξ (§6.2):** lens reindexing, proved a fibration
  via the Grothendieck construction. (Its vertical companion, the carrier
  reindexing over (Μ, Π), is established as a functor but its opfibration status
  is left open — §6.2 open step.)

**Does NOT establish (recorded as open / modest):**

- That "×" is a categorical product — it is a lattice product (§2 remark).
- The single fibration over the full lattice is **refuted** (§6.1), not left
  open. The correct global object is a **double category**, whose explicit
  construction and interchange law are the **successor open problem** (§6.3).

**Governance note.** `harness-spec` may, in the future, point to this document
as the formal foundation of its order structure through the formal-layer
traceability discipline. Establishing that link edits `harness-spec`, which is
under partial freeze (`gobernanza` §8.3); it is therefore deferred to an
explicit ADR and is **not** performed by creating this document.
