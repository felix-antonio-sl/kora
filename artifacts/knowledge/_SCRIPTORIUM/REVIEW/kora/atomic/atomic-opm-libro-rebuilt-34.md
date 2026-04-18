---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-34
  provenance:
    created_by: atomize
    created_at: '2026-04-18'
    source: /home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt
version: 1.0.0
status: draft
tags:
- atomic
- knowledge
- opm-libro-rebuilt
lang: es
extensions:
  kora:
    family: atomic
    atomic:
      producer: urn:kora:skill:atomize:1.0.0
      source_corpus: /home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt
      n_propositions: 55
      segmented: true
      segment_role: segment
      segment_index: 34
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-34
---

# Atomic opm-libro-rebuilt - Segmento 34

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `55`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `34/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 12 SysML: Foundations and Diagrams / 12.9.5 Activity Diagrams Compared with OPDs

- **P1745** · `fact` · As noted, flows in an activity diagram can be of two kinds: control flow and object (or block) flow. · [src:S01:L4602-L4649](../../../INBOX/opm-libro.txt#L4602-L4649)
- **P1746** · `fact` · A control flow designates the flow from one action to another without explicit mention of an object. · [src:S01:L4602-L4649](../../../INBOX/opm-libro.txt#L4602-L4649)
- **P1747** · `constraint` · Figure 12.7 is an example where all the flows are control flows; the message being passed from one action to the next is implicit. · [src:S01:L4602-L4649](../../../INBOX/opm-libro.txt#L4602-L4649)
- **P1748** · `fact` · In contrast, an object flow has a specific object that is an output of one action and is input to the next. · [src:S01:L4602-L4649](../../../INBOX/opm-libro.txt#L4602-L4649)
- **P1749** · `constraint` · There are two ways to model object flow, both shown in Fig. 12.15. · [src:S01:L4602-L4649](../../../INBOX/opm-libro.txt#L4602-L4649)
- **P1750** · `fact` · The one at the top is the pin notation: Blueprint is both the output on the pin of the Designing action and the input on the pin of the Manufacturing action. · [src:S01:L4602-L4649](../../../INBOX/opm-libro.txt#L4602-L4649)
- **P1751** · `requirement` · The type of the input and output must be the same. · [src:S01:L4602-L4649](../../../INBOX/opm-libro.txt#L4602-L4649)
- **P1752** · `fact` · The second way to model object flow, shown at the bottom of Fig. · [src:S01:L4602-L4649](../../../INBOX/opm-libro.txt#L4602-L4649)
- **P1753** · `constraint` · 12.15, is the explicit object notation: The object (or block) is depicted as both the output and input. The activity diagram at the bottom of Fig. 12.15 looks very similar to an OPD. · [src:S01:L4602-L4649](../../../INBOX/opm-libro.txt#L4602-L4649)
- **P1754** · `constraint` · It looks like all we need to do is replace the activity symbol—the rountangle—with the OPD symbol for process—the ellipse, we will get a semantically equivalent model. Doing this produces the OPD in Fig. 12.16. · [src:S01:L4602-L4649](../../../INBOX/opm-libro.txt#L4602-L4649)
- **P1755** · `fact` · The two models really look isomorphic: just replace the shape and voila! · [src:S01:L4602-L4649](../../../INBOX/opm-libro.txt#L4602-L4649)
- **P1756** · `fact` · However, to gain insight into the exact semantics of this OPD, we should read its OPL paragraph: Designing yields Blueprint. Manufacturing consumes Blueprint. Is this really what we wanted to model? · [src:S01:L4602-L4649](../../../INBOX/opm-libro.txt#L4602-L4649)
- **P1757** · `fact` · Is Blueprint really consumed by Manufacturing? · [src:S01:L4602-L4649](../../../INBOX/opm-libro.txt#L4602-L4649)
- **P1758** · `fact` · What we really want to model is that once ready, Blueprint enables Manufacturing. · [src:S01:L4602-L4649](../../../INBOX/opm-libro.txt#L4602-L4649)
- **P1759** · `fact` · However, Manufacturing does not consume Blueprint, but rather references it, so Blueprint is an enabler, or, more specifically, an instrument: It is required by the Manufacturing process, but it is not destroyed by it. · [src:S01:L4602-L4649](../../../INBOX/opm-libro.txt#L4602-L4649)
- **P1760** · `fact` · Moreover, while Blueprint is an informatical object, Manufacturing is a physical process. · [src:S01:L4602-L4649](../../../INBOX/opm-libro.txt#L4602-L4649)
- **P1761** · `constraint` · The OPL paragraph of this OPD is indeed more telling and it confirms our improved graphical model (Fig. 12.17): Designing yields Blueprint. Manufacturing is physical. Manufacturing requires Blueprint. · [src:S01:L4602-L4649](../../../INBOX/opm-libro.txt#L4602-L4649)
- **P1762** · `fact` · Contemplating on the thought process that this exercise involved, we realize that the semantics of the activity diagram is less expressive than that of the OPD. · [src:S01:L4602-L4649](../../../INBOX/opm-libro.txt#L4602-L4649)
- **P1763** · `fact` · Arrows between an activity and an object in an activity diagram have flow semantics, while in OPM they have transformation semantics—creation, consumption, or state change. · [src:S01:L4602-L4649](../../../INBOX/opm-libro.txt#L4602-L4649)
- **P1764** · `fact` · The Blueprint in the activity diagram simply “flows” between the two actions, implicitly changing its logical location as it does so, but weather Blueprint is consumed by Manufacturing or it just enables it is not specified. · [src:S01:L4602-L4649](../../../INBOX/opm-libro.txt#L4602-L4649)
- **P1765** · `fact` · Conversely, the OPM arrows do not have flow semantics—they do not imply that the object involved changes its location, only that it undergoes some transformation. · [src:S01:L4602-L4649](../../../INBOX/opm-libro.txt#L4602-L4649)
- **P1766** · `fact` · The activity diagram cannot distinguish between an instrument and a consumee (neither can any other SysML diagram type, at least not directly). · [src:S01:L4602-L4649](../../../INBOX/opm-libro.txt#L4602-L4649)
- **P1767** · `fact` · The distinction between the informatical essence of Designing and Blueprint on one hand and the physical essence of Manufacturing on the other hand cannot be modeled either. · [src:S01:L4602-L4649](../../../INBOX/opm-libro.txt#L4602-L4649)
- **P1768** · `fact` · Neither this essence distinction nor the distinction between an enabler and a transformee can be modeled in a straightforward manner by any one of the nine SysML diagram kinds. activity diagram · [src:S01:L4602-L4649](../../../INBOX/opm-libro.txt#L4602-L4649)

## opm libro · Chapter 12 SysML: Foundations and Diagrams / 12.9.6 Flow of Control in Activity Diagrams Versus OPDs

- **P1769** · `constraint` · The flow of control in activity diagrams is achieved through decision nodes, which are diamond-shaped nodes from which two or more control flow lines emanate, as shown in Fig. 12.18. On the left hand side of Fig. · [src:S01:L4651-L4662](../../../INBOX/opm-libro.txt#L4651-L4662)
- **P1770** · `constraint` · 12.18 is a relevant portion of the OPD, while on the right hand side is the equivalent activity diagram. · [src:S01:L4651-L4662](../../../INBOX/opm-libro.txt#L4651-L4662)
- **P1771** · `fact` · Examining the two models, we see that OPM does not require the special decision symbol—the diamond in the activity diagram. · [src:S01:L4651-L4662](../../../INBOX/opm-libro.txt#L4651-L4662)
- **P1772** · `fact` · Rather an object with two states—a Boolean object—is used. · [src:S01:L4651-L4662](../../../INBOX/opm-libro.txt#L4651-L4662)
- **P1773** · `fact` · Moreover, the decision symbol often requires, as is the case here, a note (whose symbol is a piece of paper with its top right corner folded; see Fig. · [src:S01:L4651-L4662](../../../INBOX/opm-libro.txt#L4651-L4662)
- **P1774** · `constraint` · 12.18) with the reserved word «decisionInput» in order to be able to specify what is being decided in the decision node. · [src:S01:L4651-L4662](../../../INBOX/opm-libro.txt#L4651-L4662)
- **P1775** · `fact` · Notes are informal annotations that prevent automating the model execution. · [src:S01:L4651-L4662](../../../INBOX/opm-libro.txt#L4651-L4662)
- **P1776** · `fact` · Moreover, the decision variable is often an object or part of an object in and of itself (e.g., a message or the result of a function), possibly with states, attributes, and other refinees, but using a decision node does not provide for modeling that object. · [src:S01:L4651-L4662](../../../INBOX/opm-libro.txt#L4651-L4662)

## opm libro · Chapter 12 SysML: Foundations and Diagrams / 12.9.7 OPM Implementation of a Requirements Diagram

- **P1777** · `fact` · As with other SysML diagrams we have seen, OPM enables modeling requirements with no need for a specialized symbol set. · [src:S01:L4664-L4690](../../../INBOX/opm-libro.txt#L4664-L4690)
- **P1778** · `requirement` · Consider, for example, the following requirement, called Flow Rate Regulation: “Gasoline flow rate shall be directly proportional to the piston pressure and inversely proportional to the injector demand and to the number of pistons.” This requirement is presented in the requirements diagram in Fig. 12.19. · [src:S01:L4664-L4690](../../../INBOX/opm-libro.txt#L4664-L4690)
- **P1779** · `definition` · In OPM we define an informatical object class Requirement, which has an instance to Flow Rate Regulation. · [src:S01:L4664-L4690](../../../INBOX/opm-libro.txt#L4664-L4690)
- **P1780** · `fact` · Since Flow Rate satisfies this requirement, extending the OPD in Fig. · [src:S01:L4664-L4690](../../../INBOX/opm-libro.txt#L4664-L4690)
- **P1781** · `constraint` · 12.14, we express this relation using OPM’s tagged structural link satisfies in Fig. 12.20. · [src:S01:L4664-L4690](../../../INBOX/opm-libro.txt#L4664-L4690)
- **P1782** · `fact` · Another approach is to formally model the requirement and derive the textual requirement specification from the resulting OPL text, rather than writing freestyle requirements. · [src:S01:L4664-L4690](../../../INBOX/opm-libro.txt#L4664-L4690)
- **P1783** · `fact` · Using the exhibition- characterization relation, we can model the Requirement in Fig. · [src:S01:L4664-L4690](../../../INBOX/opm-libro.txt#L4664-L4690)
- **P1784** · `constraint` · 12.20 as exhibiting several parts, including Client Free Text, Vitality, Urgency, Satisfying Status, and Deriving Requirement. · [src:S01:L4664-L4690](../../../INBOX/opm-libro.txt#L4664-L4690)
- **P1785** · `requirement` · The value of the attribute Client Free Text of the instance Flow Rate Regulation will be “Gasoline flow rate shall be directly proportional to the piston pressure and inversely proportional to the injector demand and to the number of pistons”. · [src:S01:L4664-L4690](../../../INBOX/opm-libro.txt#L4664-L4690)
- **P1786** · `constraint` · To increase the generality we can model the object Piston Set whose Size attribute value is a parameter instead of the number 4 in the mathematical expression which is part of the process name “Flow Rate as Pressure/(4(Injector Demand)) Calculating”. · [src:S01:L4664-L4690](../../../INBOX/opm-libro.txt#L4664-L4690)
- **P1787** · `fact` · Furthermore, instead of including this expression in the process name, we can in-zoom and model how the result is computed step-by-step using the parameters. · [src:S01:L4664-L4690](../../../INBOX/opm-libro.txt#L4664-L4690)
- **P1788** · `fact` · This way if any one of the parameters or even the expression changes, the process name does not need to be changed. · [src:S01:L4664-L4690](../../../INBOX/opm-libro.txt#L4664-L4690)

## opm libro · Chapter 12 SysML: Foundations and Diagrams / 12.10 SysML–OPM Synergies

- **P1789** · `constraint` · Grobshtein and Dori (2011) evaluated aspects of SysML and OPM on the basis of a concrete sample problem, in which multiple aspects of the system were modeled in both SysML and OPM. · [src:S01:L4692-L4699](../../../INBOX/opm-libro.txt#L4692-L4699)
- **P1790** · `fact` · OPM was found advantageous in presenting the system different hierarchy levels and combining structure with behavior, while SysML was found more convenient for modeling detailed views of some aspects. · [src:S01:L4692-L4699](../../../INBOX/opm-libro.txt#L4692-L4699)
- **P1791** · `fact` · This finding was corroborated in a later empirical work, which pointed out that for answering particular focused questions, a certain SysML view, which was automatically generated from an OPM model, may provide a better answer quicker. · [src:S01:L4692-L4699](../../../INBOX/opm-libro.txt#L4692-L4699)
- **P1792** · `fact` · Hence there is apparent potential synergy of combining advantages of these two languages. · [src:S01:L4692-L4699](../../../INBOX/opm-libro.txt#L4692-L4699)

## opm libro · Chapter 13 The Dynamic System Aspect

- **P1793** · `fact` · Every day we are confronted with systems that have an inherent tendency to change. · [src:S01:L4740-L4748](../../../INBOX/opm-libro.txt#L4740-L4748)
- **P1794** · `constraint` · The weather, the stock market, or the economic situation, are examples. Meinhardt (1995) Systems change over time. · [src:S01:L4740-L4748](../../../INBOX/opm-libro.txt#L4740-L4748)
- **P1795** · `fact` · An important motivation in the development of OPM has been to strike a needed balance in a system’s conceptual model between the structural, static and procedural, dynamic aspects of the system. · [src:S01:L4740-L4748](../../../INBOX/opm-libro.txt#L4740-L4748)
- **P1796** · `fact` · The dynamic aspect of a system specifies how the system operates to attain its function, complementing its static aspect. · [src:S01:L4740-L4748](../../../INBOX/opm-libro.txt#L4740-L4748)
- **P1797** · `fact` · OPM is at least process-oriented as it is object-oriented. · [src:S01:L4740-L4748](../../../INBOX/opm-libro.txt#L4740-L4748)
- **P1798** · `fact` · Indeed, OPM models unify structure and behavior in one coherent frame of reference, with time being the fundamental underlying concept. · [src:S01:L4740-L4748](../../../INBOX/opm-libro.txt#L4740-L4748)
- **P1799** · `fact` · This chapter addresses modeling the dynamics aspect of a system. · [src:S01:L4740-L4748](../../../INBOX/opm-libro.txt#L4740-L4748)
