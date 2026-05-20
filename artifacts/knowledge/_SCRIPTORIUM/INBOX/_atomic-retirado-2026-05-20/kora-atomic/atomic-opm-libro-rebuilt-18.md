---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-18
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
      producer: urn:kora:artefacto:atomize
      source_corpus: /home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt
      n_propositions: 57
      segmented: true
      segment_role: segment
      segment_index: 18
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-18
---

# Atomic opm-libro-rebuilt - Segmento 18

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `57`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `18/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 9 Conceptual Modeling: Purpose and Context / 9.4.6 System Architecture

- **P0896** · `definition` · With the understanding of what structure and behavior are, we can define a system’s architecture. · [src:S01:L2617-L2637](../../../INBOX/opm-libro.txt#L2617-L2637)
- **P0897** · `fact` · Architecture of a system is the combination of the system’s structure and behavior which enables it to perform its function. · [src:S01:L2617-L2637](../../../INBOX/opm-libro.txt#L2617-L2637)
- **P0898** · `fact` · It might be interesting to compare our definition of architecture to the one used by the U.S. · [src:S01:L2617-L2637](../../../INBOX/opm-libro.txt#L2617-L2637)
- **P0899** · `constraint` · DoD Architecture Framework (DoDAF 2007), which is based on IEEE STD 610.12: Architecture: the structure of components, their relationships, and the principles and guidelines governing their design and evolution over time. · [src:S01:L2617-L2637](../../../INBOX/opm-libro.txt#L2617-L2637)
- **P0900** · `constraint` · TOGAF (2011) provides a similar definition in response to the question “What is an Architecture?” An Architecture is the fundamental organization of something, embodied in its components, their relationships to each other and the environment, and the principles governing its design and evolution. · [src:S01:L2617-L2637](../../../INBOX/opm-libro.txt#L2617-L2637)
- **P0901** · `fact` · The common element in both definitions and our definition of architecture is the system’s structure. · [src:S01:L2617-L2637](../../../INBOX/opm-libro.txt#L2617-L2637)
- **P0902** · `fact` · However, the DoDAF and TOGAF definitions lack the integration of the structure with the behavior to provide the function. · [src:S01:L2617-L2637](../../../INBOX/opm-libro.txt#L2617-L2637)
- **P0903** · `fact` · On the other hand, the DoDAF definition includes “the principles and guidelines governing the design and evolution of the system’s component over time”. · [src:S01:L2617-L2637](../../../INBOX/opm-libro.txt#L2617-L2637)
- **P0904** · `fact` · However, these do not seem to be part of the system’s architecture. · [src:S01:L2617-L2637](../../../INBOX/opm-libro.txt#L2617-L2637)
- **P0905** · `fact` · Rather, principles and guidelines govern the architecting process, which culminates in the system’s architecture. · [src:S01:L2617-L2637](../../../INBOX/opm-libro.txt#L2617-L2637)
- **P0906** · `constraint` · Interestingly, DoDAF Architecture Framework Version 2.02, Change 1 (DoDAF 2015), the version of January 2015 does not contain any clear definition of architecture (and neither does the 2009 edition)! · [src:S01:L2617-L2637](../../../INBOX/opm-libro.txt#L2617-L2637)

## opm libro · Chapter 9 Conceptual Modeling: Purpose and Context / 9.4.7 System Environment and Thing’s Affiliation

- **P0907** · `fact` · In recent years, the term environment has increasingly taken on the meaning of the ecosystem of planet earth in which we all live and which is continuously compromised as a result of cumulative effects of large-scale man-made systems (such as power plants) and a large number of smaller scale man-made system (such as automobiles and aircrafts). · [src:S01:L2639-L2660](../../../INBOX/opm-libro.txt#L2639-L2660)
- **P0908** · `fact` · Our definition of the system’s environment is indeed compatible with this realization, as it provides for the possibility that the environment can change as a result of the system’s function. · [src:S01:L2639-L2660](../../../INBOX/opm-libro.txt#L2639-L2660)
- **P0909** · `fact` · The system’s environment is a collection of things that are outside the system but interact with it. · [src:S01:L2639-L2660](../../../INBOX/opm-libro.txt#L2639-L2660)
- **P0910** · `fact` · The interaction of the system with its environment causes the system, and possibly its environment, to change. · [src:S01:L2639-L2660](../../../INBOX/opm-libro.txt#L2639-L2660)
- **P0911** · `requirement` · To ensure sustainability, systems engineers must make sure to prevent or undo this adverse change, especially as it pertains to possibly irreversible detrimental effects of current and contemplated systems on global warming and natural resource depletion. · [src:S01:L2639-L2660](../../../INBOX/opm-libro.txt#L2639-L2660)
- **P0912** · `fact` · This is not just a moral or ethical obligation— it is a matter of securing sustainable life on earth of all organisms, including people, beyond the next couple of decades… A thing which is part of the system is systemic, while a thing which is part of the system’s environment is environmental. · [src:S01:L2639-L2660](../../../INBOX/opm-libro.txt#L2639-L2660)
- **P0913** · `fact` · The OPM thing’s attribute whose values are systemic and environmental is affiliation. · [src:S01:L2639-L2660](../../../INBOX/opm-libro.txt#L2639-L2660)
- **P0914** · `fact` · Making the distinction between systemic and environmental things is very important in modeling, as it indicates what are the things that the architect can have control of and what should be considered as given. · [src:S01:L2639-L2660](../../../INBOX/opm-libro.txt#L2639-L2660)
- **P0915** · `fact` · For example, in designing a gas station, is the car systemic or environmental? · [src:S01:L2639-L2660](../../../INBOX/opm-libro.txt#L2639-L2660)
- **P0916** · `requirement` · Obviously, cars and their drivers are going to interact with the gas station, but the gas station architect does not have a control over the sizes of the cars and the locations of their gas tank openings—these are given and must be accounted for. · [src:S01:L2639-L2660](../../../INBOX/opm-libro.txt#L2639-L2660)
- **P0917** · `fact` · Therefore, car is environmental to gas station. · [src:S01:L2639-L2660](../../../INBOX/opm-libro.txt#L2639-L2660)

## opm libro · Chapter 9 Conceptual Modeling: Purpose and Context / 9.4.8 Function Versus Behavior

- **P0918** · `fact` · The above definitions lead to the conclusion that the function of a system is its top-level process. · [src:S01:L2664-L2683](../../../INBOX/opm-libro.txt#L2664-L2683)
- **P0919** · `fact` · Moreover, the architecture of the system, namely its structure-behavior combination, is what enables the system to execute its top-level process, thereby to perform its function and deliver value to its beneficiary. · [src:S01:L2664-L2683](../../../INBOX/opm-libro.txt#L2664-L2683)
- **P0920** · `fact` · The value of the function to the beneficiary is often implicit; it is expressed in process terms, which emphasize what happens, rather than the purpose for which the top-level process happens. · [src:S01:L2664-L2683](../../../INBOX/opm-libro.txt#L2664-L2683)
- **P0921** · `fact` · This implicit function statement can explain why the function of a system is often confused with the behavior or dynamics of the system. · [src:S01:L2664-L2683](../../../INBOX/opm-libro.txt#L2664-L2683)
- **P0922** · `fact` · However, it is critical to clearly and unambiguously distinguish between the two, namely between function and behavior. · [src:S01:L2664-L2683](../../../INBOX/opm-libro.txt#L2664-L2683)
- **P0923** · `fact` · Behavior is how the system changes along the time dimension. · [src:S01:L2664-L2683](../../../INBOX/opm-libro.txt#L2664-L2683)
- **P0924** · `fact` · Function is what value the system delivers to its beneficiary through its operation. · [src:S01:L2664-L2683](../../../INBOX/opm-libro.txt#L2664-L2683)
- **P0925** · `fact` · Hence, behavior is objective—it is the way the system changes, regardless of who describes the change, while function is subjective—it is the value gained from the beneficiary’s perspective. · [src:S01:L2664-L2683](../../../INBOX/opm-libro.txt#L2664-L2683)
- **P0926** · `fact` · This distinction between function and behavior is of utmost importance since in many cases a system’s function can be achieved by different architectures, i.e., different combinations of processes (system behavior) and objects (system structure). · [src:S01:L2664-L2683](../../../INBOX/opm-libro.txt#L2664-L2683)
- **P0927** · `fact` · Consider, for example, a system for enabling humans to cross a river with their vehicles. · [src:S01:L2664-L2683](../../../INBOX/opm-libro.txt#L2664-L2683)
- **P0928** · `fact` · Two obvious architectures are ferry and bridge. · [src:S01:L2664-L2683](../../../INBOX/opm-libro.txt#L2664-L2683)
- **P0929** · `fact` · While the two systems’ function and top-level process—river crossing—are identical, they differ dramatically in their structure and behavior. · [src:S01:L2664-L2683](../../../INBOX/opm-libro.txt#L2664-L2683)
- **P0930** · `fact` · Failure to recognize this difference between function and behavior may lead to a premature choice of a sub-optimal architecture. · [src:S01:L2664-L2683](../../../INBOX/opm-libro.txt#L2664-L2683)
- **P0931** · `fact` · In the example above, this may amount to making a decision to build a bridge without considering the ferry option altogether. · [src:S01:L2664-L2683](../../../INBOX/opm-libro.txt#L2664-L2683)

## opm libro · Chapter 9 Conceptual Modeling: Purpose and Context / 9.5 Language and Modeling

- **P0932** · `fact` · We now turn to definitions that concern language and modeling. · [src:S01:L2685-L2693](../../../INBOX/opm-libro.txt#L2685-L2693)
- **P0933** · `fact` · A language is a means of communication among humans, and possibly also machines, to express concepts, ideas, processes, and methods. · [src:S01:L2685-L2693](../../../INBOX/opm-libro.txt#L2685-L2693)
- **P0934** · `fact` · A language comprises two components: syntax and semantics. · [src:S01:L2685-L2693](../../../INBOX/opm-libro.txt#L2685-L2693)
- **P0935** · `fact` · Syntax is the language’s set of symbols and rules that specify how the symbols can be combined to yield syntactically-legal constructs. · [src:S01:L2685-L2693](../../../INBOX/opm-libro.txt#L2685-L2693)
- **P0936** · `fact` · Not any syntactically-legal construct in the language is meaningful. · [src:S01:L2685-L2693](../../../INBOX/opm-libro.txt#L2685-L2693)
- **P0937** · `fact` · Semantics is the meaning that a subset of the language’s syntactically-legal constructs conveys. · [src:S01:L2685-L2693](../../../INBOX/opm-libro.txt#L2685-L2693)

## opm libro · Chapter 9 Conceptual Modeling: Purpose and Context / 9.5.1 Model and Modeling

- **P0938** · `fact` · Languages not only enable humans and machines to communicate; they are also means to building models. · [src:S01:L2695-L2718](../../../INBOX/opm-libro.txt#L2695-L2718)
- **P0939** · `fact` · A model is an abstraction of some portion of conceived reality (the system “as-is”) or of a contemplated system (the system “to-be”) expressed in some language. · [src:S01:L2695-L2718](../../../INBOX/opm-libro.txt#L2695-L2718)
- **P0940** · `fact` · For example, a sufficiently detailed textual description of a machine part in free English text can be considered a model of that part. · [src:S01:L2695-L2718](../../../INBOX/opm-libro.txt#L2695-L2718)
- **P0941** · `fact` · However, this model is not formal as it is expressed in English, a natural, non-formal language. · [src:S01:L2695-L2718](../../../INBOX/opm-libro.txt#L2695-L2718)
- **P0942** · `fact` · Hence, at least with current technology, it cannot be automatically constructed or analyzed, requiring a human in the loop. · [src:S01:L2695-L2718](../../../INBOX/opm-libro.txt#L2695-L2718)
- **P0943** · `fact` · A modeling language is a language for constructing models in some domain. · [src:S01:L2695-L2718](../../../INBOX/opm-libro.txt#L2695-L2718)
- **P0944** · `fact` · A formal modeling language is a modeling language that has a mathematically- grounded syntax definition, enabling its automated analysis, checking, and synthesis. · [src:S01:L2695-L2718](../../../INBOX/opm-libro.txt#L2695-L2718)
- **P0945** · `fact` · For example, machine drawings of mechanical parts utilize a formal modeling language, drafting, in which symbols convey formal syntax with agreed-upon semantics that mechanical engineers understand and share. · [src:S01:L2695-L2718](../../../INBOX/opm-libro.txt#L2695-L2718)
- **P0946** · `fact` · Thus, a dash-dotted line expressed an axis of symmetry, a dimension set with arrows, guides and a text box expresses a part’s dimension, etc. · [src:S01:L2695-L2718](../../../INBOX/opm-libro.txt#L2695-L2718)
- **P0947** · `fact` · A formal modeling language is expressed using one or two modalities, i.e., modes of expression. · [src:S01:L2695-L2718](../../../INBOX/opm-libro.txt#L2695-L2718)
- **P0948** · `fact` · Two prominent modalities for expressing models are graphics and text. · [src:S01:L2695-L2718](../../../INBOX/opm-libro.txt#L2695-L2718)
- **P0949** · `fact` · OPM is unique in that it is the only known modeling language which uses these two modalities interchangeably and in tandem. · [src:S01:L2695-L2718](../../../INBOX/opm-libro.txt#L2695-L2718)
- **P0950** · `fact` · Modeling is the process of creating a model in some domain using a modeling language that is appropriate for that domain. · [src:S01:L2695-L2718](../../../INBOX/opm-libro.txt#L2695-L2718)
- **P0951** · `fact` · Modeling is a foundational engineering activity. · [src:S01:L2695-L2718](../../../INBOX/opm-libro.txt#L2695-L2718)
- **P0952** · `fact` · The resulting model is a centerpiece infrastructural entity that supports the evolution of the system throughout its lifecycle in a “model-based” or “model- driven” context. · [src:S01:L2695-L2718](../../../INBOX/opm-libro.txt#L2695-L2718)
