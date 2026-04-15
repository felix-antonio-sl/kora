---
_manifest:
  urn: urn:kora:kb:cat-governance-lattice-p02
  provenance:
    created_by: FS
    created_at: '2026-02-26'
    source: Davey & Priestley (Introduction to Lattices and Order), KORA gobernanza
      v1.3.0, spec-md v2.1.0, md-spec v2.0.0
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
extensions:
  kora:
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:kora:kb:cat-governance-lattice
---

# Governance as Lattice: Precedence, Transformation, and Spec Hierarchy - Parte 02

## 4. The Full Picture

### 4.1 KORA as a Categorical System

Assembling documents 00-05, KORA is formalized as:

```
KORA = (Eco, Psh(F), Free ⊣ Forget, L, {K, C, G})

where:
 Eco = 2-category of agents (03)
 Psh(F) = presheaf of discoverable Skills over Eco (04)
 Free ⊣ Forget = adjunction between CMs and Skills (02)
 L = governance lattice of specs (05)
 K, C, G = transformation functors producing KORA artifacts (05 §2)
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
