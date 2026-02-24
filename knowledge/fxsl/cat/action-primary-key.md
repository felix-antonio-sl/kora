---
_manifest:
  urn: urn:fxsl:kb:action-primary-key
  provenance:
    created_by: FS
    created_at: '2025-12-14'
    source: 'Action is the primary key: a categorical framework for episode description
      and logical reasoning (Fukada, 2024)'
version: 2.0.0
status: published
tags:
- category-theory
- action
- episodic-memory
- primary-key
- categorical-framework
- fxsl
lang: en
---

# Action as Primary Key

## Thesis

- The central thesis: action is not an attribute of a state or transition
- it is the primary key that indexes and structures episodic memory.


## Categorical Framework

### Core Definitions

- **World as Category**: Model the world as a category C. The structure resides in morphisms (actions), and objects (states) are secondary or inferred from the network of actions.

- **Database Functor**: If a database schema S is considered, data are a functor I: S → Set. For each object X in S, I(X) is the set of data instances.

- **Schema**: Information is represented via schema S, a finitely-presented category. Objects are entity types; morphisms are structural relations.

- **Grothendieck Construction**: Transition from Data to Info modeled via the category of elements ∫I, where individual data are "glued" following schema structure.

- **Knowledge via Logic**: Knowledge modeled through the internal logic of the category (typically a Topos or regular category).

- **Constraints**: Expressed as limits (pullbacks, equalizers) that must commute; business rules as commutative diagrams for valid instances.

## DIK Hierarchy

### Data

- Observations—atomic hechos (facts), discrete events.
- Modeled as a discrete category D or as terminal objects in an instance category.


### Information

- Data + relations (structure): how data relate.
- Represented as schema S (category).
- Data conform via functor I:
- S → Set with formula Info ≅ ∫ I →π S.


### Knowledge

- Information + rules/logic (semantics): inference, validation.
- Modeled through internal logic (Topos, regular category); constraints; and Proof.
- Inference: composition of morphisms.
- For Fukada's framework: allows inferring the "why" and "for what" of an action, connecting disjoint episodes in coherent narrative.


## Episode Modeling: Action as Primary Key

### Action Category A

- Category A with objects (states/contexts) and morphisms (actions that transform one context into another).


### Indexation Functor

- Action is the entity that indexes; proposes an indexation functor Idx:
- E → A where E is the category of episodes, and each episode maps to a canonical action.


### Compositionality of Episodes

- If episode E1 ends in a state that initiates E2, they compose:
- E1 ;
- E2.
- Allows constructing complex episodes (stories, processes) from atomic actions while preserving logical structure.


## Conclusions

- Formalizes the intuition: action is the axis of episodic memory.


- **Rigor**: Eliminates ambiguity in what constitutes an episode.
- **Interoperability**: Modeling Data, Info, Knowledge as categorical structures (functors, schemas, logic) facilitates integration with other knowledge systems.
- **Reasoning**: Primary-key structure in action enables efficient queries and robust logical deductions about agent behavior.
