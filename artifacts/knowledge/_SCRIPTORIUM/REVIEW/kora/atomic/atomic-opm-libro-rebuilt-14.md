---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-14
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
      n_propositions: 52
      segmented: true
      segment_role: segment
      segment_index: 14
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-14
---

# Atomic opm-libro-rebuilt - Segmento 14

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `52`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `14/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 9 Conceptual Modeling: Purpose and Context / 9.2 A Foundational Systems Engineering OPM Ontology

- **P0683** · `fact` · Ontology is a set of concepts and their relations in some domain of discourse. · [src:S01:L2177-L2231](../../../INBOX/opm-libro.txt#L2177-L2231)
- **P0684** · `fact` · The size of the ontology is the number of concepts and relation in the ontology. · [src:S01:L2177-L2231](../../../INBOX/opm-libro.txt#L2177-L2231)
- **P0685** · `definition` · Systems science and engineering are in need of a well-defined foundational, universal, general, necessary and sufficient ontology that would underpin concepts and terms it uses in order for them to be precise and unambiguous. · [src:S01:L2177-L2231](../../../INBOX/opm-libro.txt#L2177-L2231)
- **P0686** · `fact` · The following minimal ontology principle provides a good starting point for our discussion. · [src:S01:L2177-L2231](../../../INBOX/opm-libro.txt#L2177-L2231)
- **P0687** · `fact` · The minimal ontology principle If a system can be specified at the same level of accuracy and detail by two languages of different ontology sizes, then the language with the smaller size is preferable to the one with the larger size, provided that the specification comprehensibility of the former is at least comparable with that of the latter. · [src:S01:L2177-L2231](../../../INBOX/opm-libro.txt#L2177-L2231)
- **P0688** · `constraint` · Not only does this principle make perfect sense; it is also in line with the long accepted Ockham’s Razor (Ockham, 1495)—a principle attributed to 14th Century logician and Franciscan friar William of Ockham, England, which states that “Entities should not be multiplied unnecessarily” (in Latin: “Pluralitas non est ponenda sine necessitate”). · [src:S01:L2177-L2231](../../../INBOX/opm-libro.txt#L2177-L2231)
- **P0689** · `constraint` · Often called the principle of parsimony, three more useful variation on Ockham’s Razor follow. “When you have two competing theories that make exactly the same predictions, the simpler one is the better.” “One should not increase, beyond what is necessary, the number of entities required to explain anything” (Helighen 1997). “One should always choose the simplest explanation of a phenomenon, the one that requires the fewest leaps of logic.” The reason for adding to the minimal ontology principle the condition “… provided that the specification comprehensibility of the former is at least comparable with that of the latter” is that taken to extreme, one can argue that the binary code of 0 and 1 is the shortest, so it is the best. · [src:S01:L2177-L2231](../../../INBOX/opm-libro.txt#L2177-L2231)
- **P0690** · `fact` · This is true for computers, for which real human comprehension is (still?) meaningless anyway. · [src:S01:L2177-L2231](../../../INBOX/opm-libro.txt#L2177-L2231)
- **P0691** · `fact` · For humans, from a semantic viewpoint, a binary specification of any non-trivial system (e.g., a computer program in machine code, to make the case clearer) is completely undecipherable without disproportionate effort. · [src:S01:L2177-L2231](../../../INBOX/opm-libro.txt#L2177-L2231)
- **P0692** · `fact` · Therefore we require that both ontologies enable specification (or modeling) of systems with about the same level of comprehensibility, or better yet, that the specification that uses the smaller ontology is more comprehensible. · [src:S01:L2177-L2231](../../../INBOX/opm-libro.txt#L2177-L2231)
- **P0693** · `definition` · If the ontology is defined carefully and is grounded on deep philosophical foundations, there is not necessarily a tradeoff between the size of the ontology and the specification length or comprehensibility of the system modeled based on that ontology. · [src:S01:L2177-L2231](../../../INBOX/opm-libro.txt#L2177-L2231)
- **P0694** · `constraint` · Ockham’s Razor inspired also the minimum description length (MDL) principle (Rissanen 1978), a method for inductive inference that provides a generic solution to the model selection problem, i.e., how does one decide among competing explanations of data given limited observations. · [src:S01:L2177-L2231](../../../INBOX/opm-libro.txt#L2177-L2231)
- **P0695** · `fact` · MDL is based on the insight that any regularity in a given set of data can be used to compress the data by describing it with fewer symbols than the number of symbols needed to describe the original data. · [src:S01:L2177-L2231](../../../INBOX/opm-libro.txt#L2177-L2231)
- **P0696** · `fact` · In a similar vein, we formulate the following minimal conceptual modeling language OPM principle. · [src:S01:L2177-L2231](../../../INBOX/opm-libro.txt#L2177-L2231)
- **P0697** · `fact` · The Minimal Conceptual Modeling Language OPM Principle A symbol system—a language—that can conceptually model a given system using ontology with fewer diagram kinds and fewer symbols and relations among them is preferable to a larger language with more diagram kinds and more symbols and relations among them. · [src:S01:L2177-L2231](../../../INBOX/opm-libro.txt#L2177-L2231)
- **P0698** · `fact` · Using the smaller ontology puts less cognitive load on the human modeler, making the conceptual model more comprehensible and communicable to all the stakeholders without compromising the fidelity and detail level of the model. · [src:S01:L2177-L2231](../../../INBOX/opm-libro.txt#L2177-L2231)
- **P0699** · `fact` · We can rephrase the above principle almost inversely: A language with fewer symbols and fewer diagram kinds that is based on a universal ontology can describe any system with better comprehensibility than a language with more symbols and more diagram kinds. · [src:S01:L2177-L2231](../../../INBOX/opm-libro.txt#L2177-L2231)
- **P0700** · `requirement` · Alleviating the human cognitive load is highly desirable, because the modeler must cope with the inherent, irreducible complexities of man-made systems to be built (systems engineering) or natural systems to be investigated (science), so reducing the unnecessary complexity (often called complicatedness) by providing a simpler language is of tremendous value. · [src:S01:L2177-L2231](../../../INBOX/opm-libro.txt#L2177-L2231)

## opm libro · Chapter 9 Conceptual Modeling: Purpose and Context / 9.2.1 Objects Exist, Processes Happen? Some Thought-Provoking Q&As

- **P0701** · `fact` · If we accept the minimal ontology principle, then we need to find the minimal universal ontology—the ontology that is necessary and sufficient to model the universe and systems in it. · [src:S01:L2233-L2251](../../../INBOX/opm-libro.txt#L2233-L2251)
- **P0702** · `fact` · We start by first asserting that anything in the universe either exists or happens. · [src:S01:L2233-L2251](../../../INBOX/opm-libro.txt#L2233-L2251)
- **P0703** · `fact` · We proceed with a series of questions and answers designed to lead us to insights about a possible minimal universal ontology. · [src:S01:L2233-L2251](../../../INBOX/opm-libro.txt#L2233-L2251)
- **P0704** · `fact` · Q1: Assuming that everything in the universe is a thing, what can things in the universe “do”? A1: Things can exist or happen. Any thing can either exist or happen. · [src:S01:L2233-L2251](../../../INBOX/opm-libro.txt#L2233-L2251)
- **P0705** · `fact` · Nothing can be said to neither exist nor happen, in fact or potentially, and physically or informatically. · [src:S01:L2233-L2251](../../../INBOX/opm-libro.txt#L2233-L2251)
- **P0706** · `fact` · Q2: What would be a general name for all the things in the universe that exist or might exist physically or conceptually? A2: Objects exist or might exist. · [src:S01:L2233-L2251](../../../INBOX/opm-libro.txt#L2233-L2251)
- **P0707** · `fact` · Q3: What are the things in the universe that happen or might exist physically or conceptually? A3: Processes happen or might happen. · [src:S01:L2233-L2251](../../../INBOX/opm-libro.txt#L2233-L2251)
- **P0708** · `fact` · Processes cannot just happen in vacuum, without “doing” something, which leads to the next question. · [src:S01:L2233-L2251](../../../INBOX/opm-libro.txt#L2233-L2251)
- **P0709** · `fact` · Q4: What are the things to which processes happen? · [src:S01:L2233-L2251](../../../INBOX/opm-libro.txt#L2233-L2251)
- **P0710** · `fact` · A4: Processes happen or might happen to objects. Q5: What do processes do to objects? A5: Processes transform objects. · [src:S01:L2233-L2251](../../../INBOX/opm-libro.txt#L2233-L2251)
- **P0711** · `fact` · Q6: What does it mean for a process to transform an object? · [src:S01:L2233-L2251](../../../INBOX/opm-libro.txt#L2233-L2251)
- **P0712** · `fact` · A6: Transforming an object by a process means one of the following three options: · [src:S01:L2233-L2251](../../../INBOX/opm-libro.txt#L2233-L2251)
- **P0713** · `fact` · creating (generating) an object, · [src:S01:L2252](../../../INBOX/opm-libro.txt#L2252)
- **P0714** · `fact` · destroying (consuming) an object, or · [src:S01:L2253](../../../INBOX/opm-libro.txt#L2253)
- **P0715** · `requirement` · affecting (changing) an object. Q7: What does it mean for a process to affect an object? A7: A process affects an object by changing its state. Hence, objects must be stateful, i.e., they must have states. Q8: In what way are things semantically associated? Is this the only way? A8: Things are semantically associated through relations. Relations are the only way we can think about the way things relate or refer to or are associated with each other. Q9: Is there a difference between how objects and processes are related? A9: Objects are associated to objects (and processes to processes) via structural (static) relations, while objects and processes are associated via time-dependent procedural (dynamic) relations. Q10: what are the two universal aspects, i.e., the two aspects from which things in the universe can be viewed, considered, and described? A10: The two universal aspects are (1) structure—the way objects relate to each other and processes relate to each other—and (2) behavior—the way processes transform objects over time. · [src:S01:L2254-L2269](../../../INBOX/opm-libro.txt#L2254-L2269)

## opm libro · Chapter 9 Conceptual Modeling: Purpose and Context / 9.2.2 The Object-Process Theorem

- **P0716** · `fact` · The answers to the questions above can be thought of as universal axioms, because while they make sense, they are difficult to prove. · [src:S01:L2271-L2288](../../../INBOX/opm-libro.txt#L2271-L2288)
- **P0717** · `fact` · If we accept these axioms, the conclusion is that things—stateful objects and processes—and relations among them are the only three elements needed to describe the universe! · [src:S01:L2271-L2288](../../../INBOX/opm-libro.txt#L2271-L2288)
- **P0718** · `fact` · We can use the universal axioms to prove the following Object-Process Theorem. · [src:S01:L2271-L2288](../../../INBOX/opm-libro.txt#L2271-L2288)
- **P0719** · `fact` · The Object-Process Theorem Stateful objects, processes, and relations among them constitute a minimal universal ontology. · [src:S01:L2271-L2288](../../../INBOX/opm-libro.txt#L2271-L2288)
- **P0720** · `constraint` · Proof: The proof is based on (1) necessity and (2) sufficiency of stateful objects, processes, and relations among them as the only three kinds of elements needed to constitute a minimal universal ontology. · [src:S01:L2271-L2288](../../../INBOX/opm-libro.txt#L2271-L2288)
- **P0721** · `fact` · Accordingly, the proof is divided in two parts: necessity and sufficiency. · [src:S01:L2271-L2288](../../../INBOX/opm-libro.txt#L2271-L2288)
- **P0722** · `constraint` · Part 1—necessity: Stateful objects and processes are necessary to specify the two universal aspects, structure and behavior: Specifying the structural, static system aspect requires stateful objects and relations among them. · [src:S01:L2271-L2288](../../../INBOX/opm-libro.txt#L2271-L2288)
- **P0723** · `fact` · Specifying the procedural, dynamic system aspect requires processes and relations between them and the objects they transform. · [src:S01:L2271-L2288](../../../INBOX/opm-libro.txt#L2271-L2288)
- **P0724** · `constraint` · Part 2—sufficiency: Things can either exist (we call these things stateful objects) or happen (we call them processes) and nothing else. · [src:S01:L2271-L2288](../../../INBOX/opm-libro.txt#L2271-L2288)
- **P0725** · `fact` · Things can be associated with each other only through relations. · [src:S01:L2271-L2288](../../../INBOX/opm-libro.txt#L2271-L2288)
- **P0726** · `fact` · Therefore, things (objects and processes) and relations among them are the only elements needed to specify facts or ideas. Q.E.D. · [src:S01:L2271-L2288](../../../INBOX/opm-libro.txt#L2271-L2288)

## opm libro · Chapter 9 Conceptual Modeling: Purpose and Context / 9.2.3 The Object-Process Corollary

- **P0727** · `fact` · The Object-Process Theorem gives rise to the following Object-Process Corollary. · [src:S01:L2290-L2304](../../../INBOX/opm-libro.txt#L2290-L2304)
- **P0728** · `fact` · The Object-Process Corollary Using stateful objects, processes, and relations among them, one can conceptually model any system in any domain. · [src:S01:L2290-L2304](../../../INBOX/opm-libro.txt#L2290-L2304)
- **P0729** · `fact` · Since according to the Object-Process Theorem stateful objects, processes, and relations among them constitute a minimal universal ontology, and the universe is the union of all the domains it comprises, this assertion makes sense. · [src:S01:L2290-L2304](../../../INBOX/opm-libro.txt#L2290-L2304)
- **P0730** · `fact` · One possible exception to this is the subatomic particle quantum domain, where our macro-world distinction between objects and processes becomes blurry. · [src:S01:L2290-L2304](../../../INBOX/opm-libro.txt#L2290-L2304)
- **P0731** · `fact` · For example, electrons and photons are described as both particles (objects) and waves (processes). · [src:S01:L2290-L2304](../../../INBOX/opm-libro.txt#L2290-L2304)
- **P0732** · `fact` · As soon as we step into the atomic and molecular level, e.g., molecular biology (Somekh et al. · [src:S01:L2290-L2304](../../../INBOX/opm-libro.txt#L2290-L2304)
- **P0733** · `constraint` · 2014), the Object-Process Corollary becomes valid, and OPM becomes a viable and attractive modeling paradigm. · [src:S01:L2290-L2304](../../../INBOX/opm-libro.txt#L2290-L2304)
- **P0734** · `fact` · This first version of the Object-Process Corollary says nothing about the level of complexity of the systems that are amenable to being modeled with stateful objects, processes, and relations among them. · [src:S01:L2290-L2304](../../../INBOX/opm-libro.txt#L2290-L2304)
