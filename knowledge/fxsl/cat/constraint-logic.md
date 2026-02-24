---
_manifest:
  urn: "urn:fxsl:kb:constraint-logic"
  provenance:
    created_by: "FS"
    created_at: "2025-12-05"
    source: "Unified Constraint Logic for categorical artifacts"
version: "2.0.0"
status: published
tags: [category-theory, constraints, sketches, regular-logic, satisfaction]
lang: en
---

# Unified Constraint Logic

## Constraint Language L_CT

Fragment of regular logic expressible in categories.

**Components**:
- **Sorts**: Category objects (types, entities).
- **Terms**: Morfismos and compositions (paths).
- **Formulas**:
  - Path Equation: path₁ = path₂ (in all instances I, I(path₁) = I(path₂)).
  - Existence: ∃x. φ(x) (required limit/colimit exists).
  - Uniqueness: ∃!x. φ(x) (universal property).
  - Inclusion: A ↪ B (monomorfismo; instance I(A) ⊆ I(B)).
  - Surjection: A ↠ B (epimorfismo; instance I(f) surjective).

**Theory**: T = (S, Σ) where S is schema and Σ is set of formulas.

## Satisfaction

**Definition**: Instance I: S→Set satisfies T = (S, Σ) iff all formulas in Σ satisfied.

**Notation**: I ⊨ T.

**Procedure**:
1. For each φ ∈ Σ, verify:
   - Path equations: I(path₁) = I(path₂).
   - Existence formulas: required object/limit exists.
   - Mono/epi: injectivity/surjectivity of I(f).
2. If all pass → I ⊨ T; else report violated formulas.

## Model Category

**Mod(T)**: Category of T models (valid instances) + natural transformations preserving T.

**Use**: Study space of valid instances conforming to schema with constraints.

## Constraints in Contexts

### Database Constraints

- **PRIMARY KEY**: Morfismo to singleton type (uniqueness).
- **FOREIGN KEY**: f: A→B with existence constraint in I(B).
- **UNIQUE**: Monomorfismo.
- **NOT NULL**: Codominio non-empty.
- **CHECK**: Path equation or subobject inclusion.

### MBSE Constraints

- **Block Composition**: Diagram as category; composition = connection.
- **Port Compatibility**: Type equations on connected ports.
- **Consistency**: Pullback existence between models.

### KODA Constraints

- **Ref Valid**: Internal morfismo well-defined.
- **XRef Resolves**: External morfismo with target in KB.
- **Proc Complete**: Process field for operative concepts.
- **Version Match**: metadata.Version = urn.version.

## Constraint Preservation by Migrations

**Definition**: Funtor F: S→T preserves constraint φ iff F(φ) satisfiable in T.

**Types**:
- **Strict**: I ⊨ φ ⟹ F*(I) ⊨ F(φ). Always preserved.
- **Weak**: ∃I such that F*(I) ⊨ F(φ). Some models preserve.

**Rules for Adjoint**:
- **Δ_F** (pullback): ALWAYS preserves path equations.
- **Σ_F** (pushforward): NOT ALWAYS; may collapse distinctions.
- **Π_F** (right pushforward): Preserves existence constraints.

## Constraint Audit

**Procedure**:
1. Extract theory T_source = (S, Σ_S) from source schema.
2. Extract T_target = (T, Σ_T) from target.
3. Identify funtor F: S → T.
4. For each φ ∈ Σ_S: verify F(φ) in Σ_T or derivable.
5. For each ψ ∈ Σ_T not from Σ_S: verify migration can satisfy.
6. Report preservation gaps.

## Theory Audit

**Procedure**:
1. Extract schema S and constraints.
2. Verify internal consistency (no contradictions).
3. Verify satisfiability (exists at least one model I ⊨ T).
4. Verify completeness (important constraints declared).
5. Report issues per dimension.
