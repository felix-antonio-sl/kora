---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-69
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
      n_propositions: 60
      segmented: true
      segment_role: segment
      segment_index: 69
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-69
---

# Atomic opm-libro-rebuilt - Segmento 69

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `60`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `69/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.16 Abstraction Accounts for Procedural Link Precedence

- **P3544** · `fact` · Recall that the procedural link uniqueness OPM principle asserts that at any level of detail, an object and a process can be connected with at most one procedural link, which uniquely determines the role of the object with respect to the process at that detail level. · [src:S01:L9028-L9056](../../../INBOX/opm-libro.txt#L9028-L9056)
- **P3545** · `fact` · When the modeler performs abstraction via state suppression, folding, or out-zooming, the procedural links between refinees and other things in the OPD that are not refinees, migrate to the context (graphically the contour, or circumference) of the refineable. For example, suppressing the states in Fig. · [src:S01:L9028-L9056](../../../INBOX/opm-libro.txt#L9028-L9056)
- **P3546** · `constraint` · 10.4, the pair of input-output links migrates from the two states to Person to become an effect link. Another example is P123 in Fig. 21.14. · [src:S01:L9028-L9056](../../../INBOX/opm-libro.txt#L9028-L9056)
- **P3547** · `fact` · This migration may cause a conflict, in which two or more procedural links of different kinds link an object and a process. · [src:S01:L9028-L9056](../../../INBOX/opm-libro.txt#L9028-L9056)
- **P3548** · `fact` · According to the procedural link uniqueness OPM principle an object or an object state can link to a process only by a single, unique procedural link. · [src:S01:L9028-L9056](../../../INBOX/opm-libro.txt#L9028-L9056)
- **P3549** · `constraint` · Figure 21.15 demonstrates the problem of procedural link abstraction. · [src:S01:L9028-L9056](../../../INBOX/opm-libro.txt#L9028-L9056)
- **P3550** · `definition` · In SD1, the result link from P1 to B is more significant, or is semantically stronger, than the effect link from P2 to B, so when the process P in SD1 is out-zoomed in SD, the result link prevails. · [src:S01:L9028-L9056](../../../INBOX/opm-libro.txt#L9028-L9056)
- **P3551** · `fact` · To sustain this principle, OPM resolves the conflict between candidate links by determining, based on the links’ semantic strength, which link remains or which new link replaces the candidates in the abstract OPD. · [src:S01:L9028-L9056](../../../INBOX/opm-libro.txt#L9028-L9056)
- **P3552** · `fact` · The loss of detail information is consistent with the notion of abstraction. · [src:S01:L9028-L9056](../../../INBOX/opm-libro.txt#L9028-L9056)
- **P3553** · `fact` · Semantic strength and link precedence are two concepts to guide the determination of which links to retain and which to hide when an OPD is out-zoomed or folded. · [src:S01:L9028-L9056](../../../INBOX/opm-libro.txt#L9028-L9056)
- **P3554** · `definition` · Semantic strength of a procedural link is the significance of the information that the link carries. · [src:S01:L9028-L9056](../../../INBOX/opm-libro.txt#L9028-L9056)
- **P3555** · `definition` · Information concerning a change in existence, either creation or elimination, is more significant than information about change to an existing thing. · [src:S01:L9028-L9056](../../../INBOX/opm-libro.txt#L9028-L9056)
- **P3556** · `fact` · The relative semantic strength of the two conflicting procedural links determines the link precedence. · [src:S01:L9028-L9056](../../../INBOX/opm-libro.txt#L9028-L9056)
- **P3557** · `fact` · When two or more procedural links compete to remain represented in an OPD that is being abstracted (out-zoomed, folded, or state-suppressed), the link that prevails is the one with the highest semantic strength. · [src:S01:L9028-L9056](../../../INBOX/opm-libro.txt#L9028-L9056)

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.16.1 Precedence Among Transforming Links

- **P3558** · `fact` · Transforming links include result, effect, and consumption links, and their variants having the event or condition control modifiers. · [src:S01:L9058-L9072](../../../INBOX/opm-libro.txt#L9058-L9072)
- **P3559** · `fact` · Link precedence is an ordered list of procedural links with diminishing sematic strength. · [src:S01:L9058-L9072](../../../INBOX/opm-libro.txt#L9058-L9072)
- **P3560** · `constraint` · Table 21.1 Link precedence among the transforming links Table 21.1 shows link precedence among the transforming links: P in the upper left corner is out- zoomed. · [src:S01:L9058-L9072](../../../INBOX/opm-libro.txt#L9058-L9072)
- **P3561** · `fact` · The column headings show the three possible transforming links between P1 and B, while the row headings show the three possible links between P2 and B. · [src:S01:L9058-L9072](../../../INBOX/opm-libro.txt#L9058-L9072)
- **P3562** · `fact` · The table cells show the prevailing link between B and P after P is out-zoomed. · [src:S01:L9058-L9072](../../../INBOX/opm-libro.txt#L9058-L9072)
- **P3563** · `fact` · Cells marked as “Invalid” indicate the impossibility of the combination. · [src:S01:L9058-L9072](../../../INBOX/opm-libro.txt#L9058-L9072)
- **P3564** · `fact` · For example, inspecting the center cell, if P1 consumes B, then B no longer exists when P2 later tries to consume it again. · [src:S01:L9058-L9072](../../../INBOX/opm-libro.txt#L9058-L9072)
- **P3565** · `constraint` · Since object creation and consumption are semantically stronger (i.e., they have higher semantic strength) than affecting the object by changing its state, result and consumption links have precedence over effect links, as demonstrated in Table 21.1. · [src:S01:L9058-L9072](../../../INBOX/opm-libro.txt#L9058-L9072)
- **P3566** · `requirement` · However, since result and consumption links are semantically equivalent, when they compete, the prevailing link shall be the effect link because the effect link allows both creation and elimination as effects. · [src:S01:L9058-L9072](../../../INBOX/opm-libro.txt#L9058-L9072)

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.16.2 Precedence Among Transforming and Enabling Links

- **P3567** · `fact` · Transforming links are semantically stronger than enabling links, because the transforming linksdenote creation, consumption, or change of the linked object, while the enabling links only denote enablement. · [src:S01:L9074-L9088](../../../INBOX/opm-libro.txt#L9074-L9088)
- **P3568** · `constraint` · A transforming link therefore has precedence over an enabling link as shown in Fig. 21.16. · [src:S01:L9074-L9088](../../../INBOX/opm-libro.txt#L9074-L9088)
- **P3569** · `requirement` · Within the enabling links, an agent link has precedence over an instrument link, because in artificial systems the humans are central to the process, they handle the system and must ensure its proper operation. · [src:S01:L9074-L9088](../../../INBOX/opm-libro.txt#L9074-L9088)
- **P3570** · `fact` · In addition, wherever there is human interaction, an interface should exist and this information should be available to the modeler of a refineable so that they can design the human-system interface according to the conceptual model specification. · [src:S01:L9074-L9088](../../../INBOX/opm-libro.txt#L9074-L9088)
- **P3571** · `fact` · Summarizing the semantic strength of the procedural non-control links, the primary link precedence is as follows: Consumption = Result > Effect > Agent > Instrument Here, the = and > symbols refer to the semantic strength of the links. · [src:S01:L9074-L9088](../../../INBOX/opm-libro.txt#L9074-L9088)
- **P3572** · `fact` · State-specified links have higher precedence than basic links that do not specify states. · [src:S01:L9074-L9088](../../../INBOX/opm-libro.txt#L9074-L9088)

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.16.3 Precedence Among Same-Kind Non-control Links and Control Links

- **P3573** · `fact` · Each non-control link kind has a corresponding event and condition link that are useful for determining finer, secondary precedence distinction within each kind of procedural link. · [src:S01:L9090-L9098](../../../INBOX/opm-libro.txt#L9090-L9098)
- **P3574** · `fact` · A secondary link precedence exists within each procedural link in the primary link precedence. · [src:S01:L9090-L9098](../../../INBOX/opm-libro.txt#L9090-L9098)
- **P3575** · `fact` · The event link has higher semantic strength than its corresponding non-control link, while the condition link has a weaker semantic strength than its corresponding non-control link. · [src:S01:L9090-L9098](../../../INBOX/opm-libro.txt#L9090-L9098)
- **P3576** · `fact` · The semantic strength of an event link is stronger than the semantic strength of its corresponding non-control link, because any event link has semantics of both its corresponding non-control link plus the event capable of initiating a process. · [src:S01:L9090-L9098](../../../INBOX/opm-libro.txt#L9090-L9098)
- **P3577** · `fact` · The semantic strength of a conditional link is weaker than the semantic strength of its corresponding non-control link, because the condition modifier weakens the precondition satisfaction criteria for the connecting process. · [src:S01:L9090-L9098](../../../INBOX/opm-libro.txt#L9090-L9098)

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.16.4 Summary of the Procedural Link Precedence

- **P3578** · `fact` · Summarizing the semantic strength of the procedural links based on the distinction between primary and secondary precedence, the complete order of precedence is as follows: · [src:S01:L9100-L9101](../../../INBOX/opm-libro.txt#L9100-L9101)
- **P3579** · `fact` · consumption event > consumption · [src:S01:L9102](../../../INBOX/opm-libro.txt#L9102)
- **P3580** · `fact` · consumption = result · [src:S01:L9103](../../../INBOX/opm-libro.txt#L9103)
- **P3581** · `fact` · result > consumption condition · [src:S01:L9104](../../../INBOX/opm-libro.txt#L9104)
- **P3582** · `fact` · consumption condition > effect event · [src:S01:L9105](../../../INBOX/opm-libro.txt#L9105)
- **P3583** · `fact` · effect event > effect · [src:S01:L9106](../../../INBOX/opm-libro.txt#L9106)
- **P3584** · `fact` · effect > effect condition · [src:S01:L9107](../../../INBOX/opm-libro.txt#L9107)
- **P3585** · `fact` · effect condition > agent event · [src:S01:L9108](../../../INBOX/opm-libro.txt#L9108)
- **P3586** · `fact` · agent event > agent · [src:S01:L9109](../../../INBOX/opm-libro.txt#L9109)
- **P3587** · `fact` · agent > agent condition · [src:S01:L9110](../../../INBOX/opm-libro.txt#L9110)
- **P3588** · `fact` · agent condition > instrument event · [src:S01:L9113](../../../INBOX/opm-libro.txt#L9113)
- **P3589** · `fact` · instrument event > instrument · [src:S01:L9114](../../../INBOX/opm-libro.txt#L9114)
- **P3590** · `fact` · instrument > instrument condition · [src:S01:L9115](../../../INBOX/opm-libro.txt#L9115)

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.17 Link Migration upon In-Zooming

- **P3591** · `fact` · The context (graphically, the outer circumference) of a process P acts as parentheses in algebra that are used to express the distributive law: Any procedural link attached to P is thus viewed as is it is attached to each one of P’s subprocesses. An example appears in Fig. · [src:S01:L9117-L9134](../../../INBOX/opm-libro.txt#L9117-L9134)
- **P3592** · `fact` · As the modeler adds subprocesses, she or he often fails to manually migrate procedural links to the specific subprocesses, causing them to be implicitly attached to superfluous procedural links that invalidate the model. · [src:S01:L9117-L9134](../../../INBOX/opm-libro.txt#L9117-L9134)
- **P3593** · `fact` · To help avoid these situations, as soon as a modeler draws the first subprocess P1 inside and in-zoomed process P, a modeling tool should automatically move to P1 all the procedural and control links that were attached to P in the parent OPD. An example is Fig. · [src:S01:L9117-L9134](../../../INBOX/opm-libro.txt#L9117-L9134)
- **P3594** · `constraint` · 5.1, which shows the Automatic Crash Responding process after it was in-zoomed and after its first subprocess, Crash Severity Measuring, was drawn inside it near the top of the enclosing ellipse of the Automatic Crash Responding process. · [src:S01:L9117-L9134](../../../INBOX/opm-libro.txt#L9117-L9134)
- **P3595** · `fact` · The links that were attached to Automatic Crash Responding have migrated to be attached to Crash Severity Measuring. · [src:S01:L9117-L9134](../../../INBOX/opm-libro.txt#L9117-L9134)
- **P3596** · `fact` · It is the modeler’s role to see to it that the various transforming links that are now attached to P1 will be put back to P or moved to subsequent subprocesses. · [src:S01:L9117-L9134](../../../INBOX/opm-libro.txt#L9117-L9134)
- **P3597** · `fact` · Similarly, enabling links may need to be migrated to one or more specific subprocesses, where the linked enabler is really needed. · [src:S01:L9117-L9134](../../../INBOX/opm-libro.txt#L9117-L9134)
- **P3598** · `fact` · As an alternative to the automatic link migration, the tool can check the validity of the links after the insertion of each new subprocess and alert the modeler as needed. · [src:S01:L9117-L9134](../../../INBOX/opm-libro.txt#L9117-L9134)

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.18 View Creating: The Fourth Refinement Mechanism

- **P3599** · `fact` · View creating—the fourth refinement mechanism after state expression, in-zooming and unfolding, is achieved by collecting model facts from various OPDs in the OPD set and putting them together in a new OPD called View for the purpose of demonstrating a specific aspect. · [src:S01:L9136-L9146](../../../INBOX/opm-libro.txt#L9136-L9146)
- **P3600** · `constraint` · Examples include (1) a process tree—a complete or partial tree of the process hierarchy of the system, which is a purely procedural view of the system, (2) an object tree—a complete or partial tree of the object hierarchy of the system, which is a purely structural view of the system, (3) an allocation view, showing what objects are allocated to perform what functions (processes) in the system model, and (4) an animated simulation motivated view, aimed at easing the concurrent inspection of how certain objects and processes from disparate OPDs interact. · [src:S01:L9136-L9146](../../../INBOX/opm-libro.txt#L9136-L9146)
- **P3601** · `requirement` · In a modeling tool, views shall not be edited to add, remove, or change any model fact. · [src:S01:L9136-L9146](../../../INBOX/opm-libro.txt#L9136-L9146)
- **P3602** · `fact` · Rather, this should be done in the non-view OPDs and reflected automatically in the pertinent views. · [src:S01:L9136-L9146](../../../INBOX/opm-libro.txt#L9136-L9146)
- **P3603** · `fact` · The inverse of view creating is view deleting. · [src:S01:L9136-L9146](../../../INBOX/opm-libro.txt#L9136-L9146)
