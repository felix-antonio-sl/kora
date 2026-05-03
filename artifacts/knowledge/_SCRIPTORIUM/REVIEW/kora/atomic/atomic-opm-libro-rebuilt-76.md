---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-76
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
      n_propositions: 45
      segmented: true
      segment_role: segment
      segment_index: 76
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-76
---

# Atomic opm-libro-rebuilt - Segmento 76

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `45`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `76/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.10.4 Split State-Specified Link Pairs

- **P3916** · `fact` · When a process that changes an object from an input state to an output state is in-zoomed, the OPD, either in-diagram or new-diagram, becomes underspecified. · [src:S01:L10048-L10069](../../../INBOX/opm-libro.txt#L10048-L10069)
- **P3917** · `requirement` · To restore specification, the modeler must attach both the state-specified input link and the state-specified output link to one of the subprocesses in a temporally-feasible manner. · [src:S01:L10048-L10069](../../../INBOX/opm-libro.txt#L10048-L10069)
- **P3918** · `fact` · A split in-out-specified link pair of process P is an input-output specified link pair whose input and output link constituents connect different subprocesses of P. · [src:S01:L10048-L10069](../../../INBOX/opm-libro.txt#L10048-L10069)
- **P3919** · `fact` · A split input link is the input link of the split in-out-specified link pair. · [src:S01:L10048-L10069](../../../INBOX/opm-libro.txt#L10048-L10069)
- **P3920** · `fact` · A split output link is the output link of the split in-out-specified link pair. In Fig. · [src:S01:L10048-L10069](../../../INBOX/opm-libro.txt#L10048-L10069)
- **P3921** · `constraint` · 22.13, the OPD in the middle is underspecified because if P1 changes A from s1 to s2, P2 cannot do this again, but it can go the other way—change A from s2 back to s1, but neither is explicitly specified. · [src:S01:L10048-L10069](../../../INBOX/opm-libro.txt#L10048-L10069)
- **P3922** · `fact` · P1 can change A from s1, i.e., take it out of s1 and leave it in transition between s1 and s2. · [src:S01:L10048-L10069](../../../INBOX/opm-libro.txt#L10048-L10069)
- **P3923** · `fact` · In- between P1 and P2 there may be one or more other interim subprocesses, during which A is still in that transition. P2 then changes A to s2. · [src:S01:L10048-L10069](../../../INBOX/opm-libro.txt#L10048-L10069)
- **P3924** · `fact` · The OPD on the right models this case (without interim subprocesses), creating a split input link from s1 of A to P1 and a split output link from P2 to s2. · [src:S01:L10048-L10069](../../../INBOX/opm-libro.txt#L10048-L10069)
- **P3925** · `constraint` · Table 22.12 summarizes the split input-output specified effect link pair. · [src:S01:L10048-L10069](../../../INBOX/opm-libro.txt#L10048-L10069)
- **P3926** · `fact` · There are no control-modified versions of the split input-specified effect link, because this can cause the of effect link semantics to be distorted. For example, if in Fig. · [src:S01:L10048-L10069](../../../INBOX/opm-libro.txt#L10048-L10069)
- **P3927** · `constraint` · 22.13 P1 is skipped, A stays in s1, so if P2 is not skipped, A was not taken out of s1, so it cannot change to s2 according to the semantics of the effect link. · [src:S01:L10048-L10069](../../../INBOX/opm-libro.txt#L10048-L10069)
- **P3928** · `constraint` · Table 22.12 Split input-output specified effect link pair · [src:S01:L10048-L10069](../../../INBOX/opm-libro.txt#L10048-L10069)

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.11 Involved Object Set Instance Transformations

- **P3929** · `fact` · As a consequence of link distribution, the following constraints apply to operational instances of transformees. · [src:S01:L10071-L10088](../../../INBOX/opm-libro.txt#L10071-L10088)
- **P3930** · `requirement` · Each consumee instance in the preprocess object set of a process shall cease to exist at the beginning of the most detailed subprocess of the process that consumes the instance, so that instance is not a member of the postprocess object set of that process. · [src:S01:L10071-L10088](../../../INBOX/opm-libro.txt#L10071-L10088)
- **P3931** · `requirement` · Each affectee instance in the preprocess object set of a process that changes that instance as a consequence of the process performance shall exit from its input state at the beginning of the deepest (most detailed) subprocess that changes the affectee. · [src:S01:L10071-L10088](../../../INBOX/opm-libro.txt#L10071-L10088)
- **P3932** · `requirement` · Each affectee instance in the postprocess object set of a process that changes that operational instance as a consequence of the process performance shall enter its output state at the completion of the deepest subprocess that changes the affectee. · [src:S01:L10071-L10088](../../../INBOX/opm-libro.txt#L10071-L10088)
- **P3933** · `requirement` · Each resultee instance in the postprocess object set of a process shall be created and begin to exist at the completion of the most detailed subprocess that yields the resultee instance. · [src:S01:L10071-L10088](../../../INBOX/opm-libro.txt#L10071-L10088)
- **P3934** · `fact` · A stateful object B for which the execution of process P has the effect of changing the state of B, exits from the input state at the beginning of the most detailed subprocess of P that changes B, and enters the output state at the end of the same subprocess of P or some subsequent subprocess of P. · [src:S01:L10071-L10088](../../../INBOX/opm-libro.txt#L10071-L10088)
- **P3935** · `fact` · Since process P execution takes a positive amount of time, that object B is in transition between states, from its input state to its output state: it has left its input state but has not yet arrived at its output state. · [src:S01:L10071-L10088](../../../INBOX/opm-libro.txt#L10071-L10088)

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.12 UML’s Object Constraint Language (OCL)

- **P3936** · `fact` · The OPM Parameterized Participation Constraint (PPC) mini-language described in Sect. · [src:S01:L10092-L10111](../../../INBOX/opm-libro.txt#L10092-L10111)
- **P3937** · `constraint` · 17.3 is somewhat reminiscent of Object Constrain Language (OCL), developed by Warmer and Kleppe (1998). · [src:S01:L10092-L10111](../../../INBOX/opm-libro.txt#L10092-L10111)
- **P3938** · `constraint` · OCL is “a precise text language that provides constraint and object query expressions that cannot be expressed by diagrammatic notation.” The current OMG OCL version (OMG OCL 2014), explains the motivation for developing OCL by arguing that “a UML diagram, such as a class diagram, is typically not refined enough to provide all the relevant aspects of a specification. · [src:S01:L10092-L10111](../../../INBOX/opm-libro.txt#L10092-L10111)
- **P3939** · `fact` · There is, among other things, a need to describe additional constraints about the objects in the model. · [src:S01:L10092-L10111](../../../INBOX/opm-libro.txt#L10092-L10111)
- **P3940** · `fact` · Such constraints are often described in natural language. · [src:S01:L10092-L10111](../../../INBOX/opm-libro.txt#L10092-L10111)
- **P3941** · `fact` · Practice has shown that this will always result in ambiguities. … OCL has been developed to fill this gap. · [src:S01:L10092-L10111](../../../INBOX/opm-libro.txt#L10092-L10111)
- **P3942** · `constraint` · It is a formal language that remains easy to read and write.” Comparing OPM’s PPC mini-language to OCL, we note that while OCL is a complete language whose current OMG 2014 specification holds 262 pages, the PPC mini-language can be specified in a few pages. · [src:S01:L10092-L10111](../../../INBOX/opm-libro.txt#L10092-L10111)
- **P3943** · `fact` · It is expressed in the OPD and translated as part of the OPL, and unlike OCL it does not provide for querying. · [src:S01:L10092-L10111](../../../INBOX/opm-libro.txt#L10092-L10111)
- **P3944** · `constraint` · With respect to the claim that OCL “remains easy to read and write” let us consider the constraint example provided in OMG OCL (2014, p. 20): Married people are of age >= 18. · [src:S01:L10092-L10111](../../../INBOX/opm-libro.txt#L10092-L10111)
- **P3945** · `constraint` · The OCL syntax for this constraint is as follows. context Person inv: (self.wife->notEmpty() implies self.wife.age >= 18) and (self.husband->notEmpty() implies self.husband.age >= 18) The corresponding OPM model is provided in Fig. 22.14. · [src:S01:L10092-L10111](../../../INBOX/opm-libro.txt#L10092-L10111)
- **P3946** · `fact` · The OPL of this model seems to be a bit more humanly comprehensible than the OCL specification above. · [src:S01:L10092-L10111](../../../INBOX/opm-libro.txt#L10092-L10111)

## opm libro · Chapter 23 Logical Operators and Probabilities

- **P3947** · `fact` · Logic and probability theory are two of the main tools in the formal study of reasoning, and have been fruitfully applied in areas as diverse as philosophy, artificial intelligence, cognitive science and mathematics. · [src:S01:L10168-L10175](../../../INBOX/opm-libro.txt#L10168-L10175)
- **P3948** · `constraint` · Stanford Encyclopedia of Philosophy (2013) Logical operators, including AND, NOT, OR, and XOR (exclusive OR) enable modeling complex conditions on performance of processes. · [src:S01:L10168-L10175](../../../INBOX/opm-libro.txt#L10168-L10175)
- **P3949** · `fact` · Using XOR, OPM can also assign probabilities to such outcomes as creating one of several possible objects, or an object in a specific state. We discuss these in this chapter. · [src:S01:L10168-L10175](../../../INBOX/opm-libro.txt#L10168-L10175)

## opm libro · Chapter 23 Logical Operators and Probabilities / 23.1 Logical AND Procedural Links

- **P3950** · `fact` · Two or more procedural links of the same kind that originate from, or arrive at, different points along the process ellipse circumference (the process context), have the semantics of the logical AND operator. · [src:S01:L10177-L10198](../../../INBOX/opm-libro.txt#L10177-L10198)
- **P3951** · `fact` · Graphically, the links with AND semantics do not touch each other on the process contour. · [src:S01:L10177-L10198](../../../INBOX/opm-libro.txt#L10177-L10198)
- **P3952** · `fact` · We have been using this operator all along as the default without explicitly stating this, as it seems natural. · [src:S01:L10177-L10198](../../../INBOX/opm-libro.txt#L10177-L10198)
- **P3953** · `fact` · Indeed, textually, the OPL reserved phrase “and” is used to express the logical AND. · [src:S01:L10177-L10198](../../../INBOX/opm-libro.txt#L10177-L10198)
- **P3954** · `fact` · The next three examples show the use of AND in various procedural links. In the OPD in Fig. · [src:S01:L10177-L10198](../../../INBOX/opm-libro.txt#L10177-L10198)
- **P3955** · `constraint` · 23.1 (right), the Safe Opening process requires both Safe Owner A and Safe Owner B. In Fig. · [src:S01:L10177-L10198](../../../INBOX/opm-libro.txt#L10177-L10198)
- **P3956** · `constraint` · 23.1 (left), opening the Safe requires all three keys. In Fig. · [src:S01:L10177-L10198](../../../INBOX/opm-libro.txt#L10177-L10198)
- **P3957** · `constraint` · 23.2 (left), Meal Preparing yields all three of the dishes. In Fig. · [src:S01:L10177-L10198](../../../INBOX/opm-libro.txt#L10177-L10198)
- **P3958** · `constraint` · 23.2 (right), Meal Eating consumes all three dishes. In the OPD on the left of Fig. · [src:S01:L10177-L10198](../../../INBOX/opm-libro.txt#L10177-L10198)
- **P3959** · `constraint` · 23.3, Interest Rate Changing affects the three objects Exchange Rate, Price Index, and Interest Rate. · [src:S01:L10177-L10198](../../../INBOX/opm-libro.txt#L10177-L10198)
- **P3960** · `fact` · In the OPD on the right, all three effects of Interest Rate Raising on Exchange Rate, Price Index, and Interest Rate are made explicit via three pairs of in-out-specified effect links. · [src:S01:L10177-L10198](../../../INBOX/opm-libro.txt#L10177-L10198)
