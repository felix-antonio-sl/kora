---
_manifest:
  urn: "urn:fxsl:skill:ontologista-gist-tension-ontologica:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Identificar y navegar tensiones especificas del modelado ontologico. Extiende CM-NAVEGADOR-TENSIONES con taxonomia de tensiones propias del dominio Gist/ontologico.

## I/O

- **Input:** Problema de modelado, contexto de diseno ontologico
- **Output:** Tension identificada, categoria, pregunta explicitadora, semillas generativas para alternativas

## Procedimiento

1. Identificar tension ontologica subyacente
2. Clasificar en categoria especifica:

**Ontological_Identity:**
- Class ↔ Category (formal vs informal taxonomy)
- Class ↔ Instance (TBox vs ABox)
- Primitive ↔ Defined Class
- Named Individual ↔ Anonymous Node

**Ontological_Structure:**
- Subclass ↔ Instance (is-a vs membership)
- Inheritance ↔ Composition
- Monolithic ↔ Modular
- Single Namespace ↔ Federated Namespaces

**Ontological_Semantics:**
- Open World ↔ Closed World
- Necessary ↔ Sufficient Conditions
- Domain/Range constraints ↔ Flexibility
- Disjointness assertion ↔ Open classification

**Gist_Specific:**
- Extend Gist ↔ Create parallel hierarchy
- Category paradigm ↔ Class subtyping
- Reference Data ↔ Ontology axioms
- TemporalRelation pattern ↔ Direct properties

3. Formular pregunta que explicite la tension
4. Usar como semilla generativa para alternativas de modelado

## Signature Output

```
TENSION: {polo_A} ↔ {polo_B}
CATEGORIA: {Ontological_Identity|Structure|Semantics|Gist_Specific}
PREGUNTA: {pregunta explicitadora}
SEMILLAS: [{alternativa_1}, {alternativa_2}]
```
