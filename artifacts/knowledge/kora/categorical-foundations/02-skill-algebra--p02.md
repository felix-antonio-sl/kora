---
_manifest:
  urn: urn:kora:kb:cat-skill-algebra-p02
  provenance:
    created_by: FS
    created_at: '2026-02-26'
    source: Mac Lane (CWM, Ch. IV Adjunctions), Awodey (Category Theory, Ch. 10 Monads),
      KORA skill-spec-md v1.0.0
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
extensions:
  kora:
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:kora:kb:cat-skill-algebra
---

# Skills as Free Algebra: The Adjunction Free ⊣ Forget - Parte 02

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
