---
_manifest:
  urn: urn:kora:kb:cat-harness-lattice
  provenance:
    created_by: Claude
    created_at: '2026-06-08'
    source: harness-spec v1.1.0 (PMI×LFS); Davey & Priestley (Introduction to Lattices
      and Order); Libkind-Spivak (Poly) via icas-agencia; KORA categorial audit 2026-06-07
  version: 1.0.0
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

# The Harness Space as Product Lattice (and its open relation to the Agent Coalgebra)

## Purpose

This document brings the foundation of the PMI×LFS ontological space — defined
operationally in `harness-spec` — into the official KORA formal layer, and does
so **honestly**: it formalizes the part that is a theorem and records, as an
explicit open problem, the part that is not.

Concretely it:

1. Formalizes the PMI×LFS space as a **bounded product lattice** in **Pos**.
2. Proves that the five inter-axis consistency laws (`harness-spec` §4.1) cut the
   space down to a **bounded sublattice** of well-formed vectors — the structure
   that `_check_vector_laws` enforces mechanically.
3. States precisely the relationship between this lattice and the agent
   **F-coalgebra** of [01-agent-coalgebra](urn:kora:kb:cat-agent-coalgebra): a
   **shared origin**, but **not a demonstrated morphism**. The bridge between the
   two structures is left as an open problem, not asserted.

This resolves the audit finding (2026-06-07, eje 7 / rec. 1) that the
constitution-level claim "PMI×LFS" rested formally only on auxiliary,
non-normative corpus. The order-theoretic content is absorbed here; the
coalgebraic bridge is not absorbed because it does not (yet) exist as a proof.

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

## 5. Relationship to the Agent F-Coalgebra — an Open Problem

This is the honest core of the document, and the resolution of the audit's
critical finding.

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

### 5.3 Why the plausible bridges fail (today)

There is **no demonstrated morphism** `V → Kl(M)-Coalg`. The natural candidates
do not hold as written:

- **Not a functor `Pos → Kl(M)-Coalg`.** Lattice monotonicity (more capability)
  and coalgebra morphisms (preserve observable behavior up to bisimulation) pull
  in opposite directions. Raising Μ (adding persistent memory) enlarges the
  carrier `U` and **breaks** bisimulation with the lower vector's agent — the
  opposite of what a behavior-preserving morphism requires. So `v ≤ v'` does not
  induce a coalgebra morphism.
- **Not a (demonstrated) Grothendieck fibration.** The tempting reading "the
  vector indexes a family of coalgebras" would need, for each `v`, a designated
  category of `F_v`-coalgebras *and* functorial reindexing along `≤`. Nothing of
  the sort is constructed. `harness-spec` mentions "fibración de Grothendieck"
  only once, for the Λ axis in isolation (§ atlas table), as a word, not a
  construction.
- **The only genuine point of contact is local and already isolated.**
  Structural safety `S_struct` (a sub-coalgebra `S ⊆ U` closed under the cofree
  dynamics, `α(S) ⊆ F(S)`) is declared by `harness-spec` §4.2 as a **property
  derived from Μ and Ξ, not an independent axis**. It is realized by the FSM
  check `coalgebra-conformance` over a finite state machine — a derived property
  *inside* an axis, not a morphism *between* the two global structures.

### 5.4 Status of the claim (the honest statement)

- The **order-theoretic** content of PMI×LFS — the product lattice and the five
  laws (sublattice `W`) — is a **theorem**, formalized here and mechanized by
  `vector-laws`. This part is now founded in the official formal layer.
- The **bridge** from the harness lattice to the agent coalgebra is **not** a
  theorem and is **not** absorbed. PMI×LFS remains, for its conceptual origin,
  founded on the auxiliary corpus `icas-*` (in `artifacts/knowledge/fxsl/cat/`,
  non-normative per the KORA Formal Layer rule). This document does **not**
  manufacture a morphism to disguise that gap.

### 5.5 Open problem

> **Conjecture (harness–coalgebra fibration).** There is a fibration
> `p : E → W` whose fiber over a well-formed vector `v` is a category of
> `F_v`-coalgebras realizing capability `v`, with reindexing along `≤`
> compatible with `T_R`. Proving or refuting this would turn the shared origin
> of §5.1 into an actual morphism.

This is a legitimate research question, not a settled result. If it is proved,
it constitutes **new ontological doctrine** and its adoption into `harness-spec`
requires an explicit ADR (the spec is under partial freeze, `gobernanza` §8.3).

## 6. What This Document Does and Does Not Establish

**Establishes (theorems):**

- Each axis is a bounded lattice; V is a bounded product lattice (§1–§2).
- The five inter-axis laws carve out a **bounded sublattice** `W` of well-formed
  vectors, closed under join and meet (§3) — the exact contract of the
  `vector-laws` check.

**Does NOT establish (recorded as open / modest):**

- That "×" is a categorical product — it is a lattice product (§2 remark).
- That there is a functor or fibration from the harness lattice to the agent
  F-coalgebra — open problem (§5.5).

**Governance note.** `harness-spec` may, in the future, point to this document
as the formal foundation of its order structure through the formal-layer
traceability discipline. Establishing that link edits `harness-spec`, which is
under partial freeze (`gobernanza` §8.3); it is therefore deferred to an
explicit ADR and is **not** performed by creating this document.
