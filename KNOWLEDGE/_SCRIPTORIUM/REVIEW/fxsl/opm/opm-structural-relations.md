---
_manifest:
  urn: "urn:fxsl:kb:opm-structural-relations"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-03-25"
    source: "source/fxsl/opm-methodology/opm-libro-structural-relations.md"
version: "1.0.0"
status: draft
tags: [opm, structural-relations, aggregation, exhibition, generalization, classification, states, participation-constraints, forks]
lang: en
extensions:
  kora:
    family: textbook
    depends_on:
      - "urn:fxsl:kb:opm-iso-19450"
      - "urn:fxsl:kb:opm-mbse-foundations"
    book_source: "Dori, D. (2015). Model-Based Systems Engineering with OPM and SysML. Springer."
    chapters: [14, 15, 16, 17, 18, 19, 20]
---

# OPM Structural Relations — Fundamental Relations, States, and Hierarchies

## Resumen

OPM structural relations son asociaciones time-independent entre things del mismo perseverance (objects con objects, processes con processes). Se expresan graficamente como structural links (flechas con punta abierta). Cuatro relaciones son fundamentales y tienen simbolos triangulares dedicados: aggregation-participation, exhibition-characterization, generalization-specialization, classification-instantiation. Participation constraints controlan multiplicity, y forks aplican la ley distributiva para compactar diagramas. States y values agregan expresividad al modelar cambio en objetos. Para notacion formal, ver [OPM ISO 19450](urn:fxsl:kb:opm-iso-19450).

## Structural Relations Fundamentals

### Structural Relation

> A structural relation is a linkage, connection, or association between two objects or between two processes that holds in the system for at least some time.

No es contingente a condiciones time-dependent. Binary structural relations son bidireccionales: si T1 se relaciona con T2 via σ, entonces T2 se relaciona con T1 via σ'. N-ary relations (n≥3) se descomponen en sets de binary relations.

### Structural Link

> A structural link is an arrow with an open head that represents a binary structural relation in an OPD from a source object to a destination object.

Punta abierta (→) contrasta con puntas triangulares cerradas de transforming links. La relacion entre structural link y structural relation es analoga a la de procedural link y procedural relation: el link expresa graficamente lo que la relacion expresa verbalmente.

### Forward and Backward Relations

- **Forward relation** (σ): relacion vista desde source thing hacia destination thing
- **Backward relation** (σ'): relacion inversa, vista desde destination hacia source
- **Symmetric**: σ = σ' (ej: "touches" → "touches")
- **Anti-symmetric**: σ y σ' son inversas (ej: "is parent of" → "is child of")

### Structural Tag and Tagged Structural Link

> A structural tag is a phrase that expresses the semantics of the structural relation between two things.

> A tagged structural link is a structural link with a structural tag recorded along it.

> A bidirectional tagged structural link is a combination of two tagged structural links in opposite directions.

Representacion grafica: harpoon-shaped arrow (⇌) con tags en ambas direcciones.

### Null Tags

- **Unidirectional default null tag**: OPL reserved phrase "relates to"
- **Bidirectional default null tag**: OPL reserved phrase "related"
- **Model-specific null tag**: user-defined override del default para un modelo, empresa o dominio

## Properties of Structural Relations

### Reciprocity

> Reciprocity is a property of a structural relation that denotes whether its forward and backward structural relations have the same semantics.

| Valor | Significado | Ejemplos |
|-------|-------------|----------|
| positive | σ = σ' (identicas) | touches, connected, adjacent, equivalent, congruent |
| neutral (default) | ni identicas ni opuestas | likes, dislikes, is indifferent to |
| negative | σ y σ' opuestas | is father of, is on top of, surrounds, consists of |

**Reciprocal structural link**: bidirectional tagged link donde forward y backward tags identicos se reemplazan por un solo reciprocity tag. OPL: "A and B are [tag]." Ejemplo: "Engine and Gearbox are attached."

### Transitivity

> A transitive structural relation is one for which if A σ B and B σ C, then A σ C.

| Valor | Significado | Ejemplos |
|-------|-------------|----------|
| positive | siempre transitiva | contains, feeds, is ancestor of, surrounds, consists of |
| neutral (default) | puede o no ser transitiva | adjacent, is next to, is friend of |
| negative | nunca transitiva | is father of, directly contains, directly feeds |

Transitive relations yield hierarchies. Knowledge de reciprocity y transitivity permite deducir relaciones remotas automaticamente.

## Structural Relations as State-Preserving Processes

Tags como surrounds, contains, holds, supports, owns son verb forms de state-preserving processes. No pasan el process test: no cumplen object transformation criterion ni time association criterion. Su semantica es de continuidad y steady state.

**Misma palabra, distinta semantica**: "Highway surrounds City" (structural relation — static) vs "Police surrounds House" (process — dynamic, cambia House de non-surrounded a surrounded). Distinguir requiere entender la semantica del modelo.

## Participation Constraints

### Definition

> A participation constraint is a number or mathematical expression recorded along a link next to an object, denoting the multiplicity of that object in that relation.

Default: 1 (implicito). Aplica tanto a structural como procedural links.

### Types

| Tipo | Definicion |
|------|-----------|
| Structural participation constraint | Recorded along a structural link |
| Procedural participation constraint | Recorded along a procedural link |
| Source participation constraint | On the source side of the link |
| Destination participation constraint | On the destination side of the link |
| Parameterized participation constraint | Mathematical expression with parameters |
| Range participation constraint | Lower and upper bounds (qmin..qmax) |

### Abbreviated Symbols

| Simbolo | Rango | OPL Reserved Phrase |
|---------|-------|---------------------|
| ? | 0..1 | optional |
| * | 0..* | (none — zero or more) |
| (nothing) | 1..1 | (default, implicit) |
| + | 1..* | at least one |

### Cardinality

> Cardinality is a property of a link whose value depends on the combination of source and destination participation constraints.

Denotacion: [qmin..qmax, q'min..q'max]. Combinando pares de {?, *, 1, +} se obtienen 16 cardinality kinds. Las 4 clasicas (one-to-one, one-to-many, many-to-one, many-to-many) son un subconjunto del cuadrante inferior derecho.

### Procedural Participation Constraints

La cantidad de procesos siempre es 1 (no hay participation constraint en el extremo del proceso). Enablers pueden ser opcionales (*) o requeridos en cierta cantidad. La PPC mini-language usa sintaxis similar a lenguajes de programacion (=, !=, <, >, <=, >=, in, not in).

## Forks and Distributive Law

### Distributive Law

> If A, B, and C are all objects or processes, and σ is a structural relation, then A σ B, A σ C ≡ A σ (B, C).

Analogia algebraica: ab + ac = a(b+c). En OPD, unir origenes de links con mismo tag produce un fork.

### Fork

> A fork is a combination of two or more structural links with the same semantics expressed by the same tag.

| Termino | Definicion |
|---------|-----------|
| Handle | Joint origin-side edge of the fork |
| Tine | Split destination-side edge of the fork |
| Handle thing | Thing linked to the handle |
| Tine thing | Thing linked to a tine |
| Object fork | Set of objects connected by a fork |
| Process fork | Set of processes connected by a fork |
| Tine thing set | Set of all things linked to the tines |

Todos los things conectados por un fork tienen el mismo perseverance (todos objetos o todos procesos).

### Fork Properties

| Propiedad | Tipo | Definicion |
|-----------|------|-----------|
| Degree | integer | Size of the tine thing set |
| Comprehensiveness | Boolean (default: positive) | Positive si todos los tine things estan attached; negative si faltan. Non-comprehensive fork marcado con barra perpendicular cerca del handle. OPL: "and at least one more" |
| Orderability | Boolean (default: negative) | Positive si los tine things estan ordenados. OPL: "in that sequence" |
| Order rule | string (default: null) | Criterio textual de ordenamiento. OPD: "ordered by [criterio]" |

## Four Fundamental Structural Relations

Cuatro relaciones con prevalencia especial tienen simbolos triangulares dedicados:

| Relacion | Forward [Refineable] | Backward [Refinee] | Simbolo | OPL Forward |
|----------|---------------------|---------------------|---------|-------------|
| Aggregation-Participation | Whole | Part | ▲ (solid black) | "consists of" |
| Exhibition-Characterization | Exhibitor | Feature | △ (open, tip down) | "exhibits" |
| Generalization-Specialization | General | Specialization | △ (open, tip up) | "are [General]s" |
| Classification-Instantiation | Class | Instance | △ (open, underlined) | "are instances of" |

### Refineable and Refinee

> Refineable is a thing amenable to refinement via a fundamental structural relation.

> Refinee is a thing that refines a refineable.

Refineable = ancestor (parent) en la jerarquia. Refinee = descendant (child). Short names (bold): Aggregation, Characterization, Generalization, Classification.

### Hierarchies and Transitivity

Las primeras tres relaciones inducen jerarquias transitivas:
- **Aggregation**: part puede ser whole de sub-parts. If A consists of B, B consists of C → A indirectly consists of C
- **Characterization**: feature puede ser exhibitor de sub-features. If A exhibits B, B exhibits C → A indirectly exhibits C
- **Generalization**: specialization puede generalizar sub-specializations. If A generalizes B, B generalizes C → A indirectly generalizes C
- **Classification**: NOT transitive — instance solo puede ser leaf en generalization hierarchy

## Aggregation-Participation

> Aggregation-participation denotes that a whole aggregates one or more parts.

### Gestalt Theory and Emergence

"The whole is something else than the sum of its parts" (Koffka 1935). Holism: la condicion de emergence — la funcion emergente del sistema que ninguna parte sola exhibe. Aplica tanto a objetos (whole = aggregate object) como procesos (whole = aggregate process, outcome emergente ≠ suma de subprocesos).

### Key Semantics

- Forward direction (aggregation): reserved phrase "consists of"
- Backward direction (participation): "is part of" (not reserved)
- "has a" evitado por ambiguedad semantica ("Dave has a stepmother" ≠ whole-part)
- Decomposition depth: se detiene en el nivel suficiente para explicar funcion, estructura y comportamiento

### Aggregation Properties (inherited from Fork)

- **Orderability**: "ordered" label junto al triangulo. OPL: "in that sequence"
- **Comprehensiveness**: non-comprehensive marcado con barra horizontal bajo el triangulo. OPL: "and at least one other part"
- **Partial aggregation consumption**: se puede modelar que un Consuming process consume el whole + subset de parts, preservando otros parts

### OPM vs UML/SysML Aggregation

| Aspecto | UML/SysML | OPM |
|---------|-----------|-----|
| Tipos | Shared (◇) + Composite (◆) | Unico (▲) |
| Distinguir que parts sobreviven | Requiere eleccion a priori shared/composite | Se modela explicitamente que parts se consumen y cuales permanecen |
| Fork | No disponible — requiere simbolo separado por part | Fork agrupa multiples parts en un link |

## Exhibition-Characterization

> Exhibition-characterization denotes that a feature characterizes an exhibitor.

Short name: characterization. Unica relacion fundamental donde las 4 combinaciones perseverance exhibitor × perseverance feature son posibles.

### Feature Types

| Feature type | Perseverance | Definicion |
|-------------|-------------|-----------|
| Attribute | Object (static) | Feature that is an object characterizing a thing |
| Operation | Process (dynamic) | Feature that is a process characterizing a thing |

### Four Exhibitor-Feature Combinations

| Exhibitor | Feature | Ejemplo |
|-----------|---------|---------|
| Object | Attribute (object) | Car exhibits Color, Weight |
| Object | Operation (process) | Car exhibits Accelerating |
| Process | Attribute (object) | Manufacturing exhibits Duration |
| Process | Operation (process) | Manufacturing exhibits Quality Checking |

### Attribute Properties

| Propiedad | Valores | Significado |
|-----------|---------|-------------|
| Explicitness | explicit (default) / implicit | Explicit: separate object linked via exhibition. Implicit: values assigned directly to exhibitor |
| Mode | qualitative (default) / quantitative | Qualitative: non-numerical values. Quantitative: numerical values |
| Touch | hard (default) / soft | Hard: value cannot be deduced from other attributes. Soft: computable from others |
| Emergence | inherent (default) / emergent | Inherent: at least one part exhibits it. Emergent: no single part exhibits it |

### Link Homogeneity

> A link is homogeneous if it connects two things with the same perseverance value. Non-homogeneous if opposite perseverance.

Default: homogeneous for structural links, non-homogeneous for procedural links.

## States and Values

### State

> A state is a situation or position at which an object can exist for some period of time during its existence.

Un objeto no puede estar en mas de un estado a la vez (XOR semantics). State enumeration OPL: "Planet can be visible or invisible." Capitalization: lower-case.

### Special States

| Tipo | Definicion | Notacion OPD |
|------|-----------|--------------|
| Initial state | State at which object is upon generation or system start | Bold frame |
| Final state | State from which object cannot exit | Double frame |
| Default state | State expected when not specified | Open arrow pointing at state |

### Value

> Value is a state of an attribute; therefore it is a specialization of state.

Solo estados de atributos (no de objetos directamente) se llaman values.

### State Transition and Lifespan

> State transition is an unstable period during which a process changes an object's state.

During transition, the object is between input state and output state. A **lifespan diagram** shows, for any point in time, what objects exist, their states, and what processes are active.

### State-Specified Tagged Structural Link

> A state-specified tagged structural link connects a state of an object to another object or to a state of another object.

### Compound States and State Space

> An atomic state is not combined of other states. A compound state combines at least two states.

> The state space of an object is the Cartesian product of the sets of states of all attributes and parts of the object.

## Generalization-Specialization

> Generalization-specialization is a fundamental structural relation between a general thing G and one or more specializations S1, S2, ..., Sn.

OPL: "S1, S2, and S3 are Gs." Transitive: if A is a B and B is a C, then A is a C.

### Inheritance

> Inheritance is assignment of OPM elements — things and links — of a general to its specializations.

OPM inheritance es mas fuerte que OO inheritance: incluye features, parts, structural links, procedural links, y states. States de specializations pueden override inherited states.

Applies to both objects and processes. UML/SysML: generalization solo aplica a objects (blocks/classes), no processes.

### Link Under/Over-Specification

- **Under-specification**: dejar links generalizados cuando existen especializados → ambiguedad
- **Over-specification**: incluir links generalizados Y especializados → redundancia

Ambos deben evitarse.

## Classification-Instantiation

> Classification-instantiation is the relation between a class of things and a unique instance belonging to that class.

OPL: "Instance A and Instance B are instances of Class."

### Key Concepts

- **Class**: template from which instances are generated
- **Instance**: relative term — specialization in one system can be instance in another
- **Process instance**: particular occurrence of a process at a given point in time, with involved object set of object instances
- NOT transitive (instance is always a leaf in the hierarchy)

### Class vs Specialization

| Concepto | Generalization-Specialization | Classification-Instantiation |
|----------|------------------------------|------------------------------|
| Tipo | General → Specialization | Class → Instance |
| Transitivity | Transitive | Not transitive |
| Hierarchy position | Any level | Instance = leaf only |
| Example | "Dog is a Pet" | "Rex is an instance of Dog" |
