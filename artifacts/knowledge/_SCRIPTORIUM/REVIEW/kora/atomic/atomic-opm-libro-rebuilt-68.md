---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-68
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
      n_propositions: 46
      segmented: true
      segment_role: segment
      segment_index: 68
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-68
---

# Atomic opm-libro-rebuilt - Segmento 68

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `46`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `68/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.14 Out-Zooming

- **P3498** · `fact` · Out-zooming is the inverse operation of in-zooming. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3499** · `fact` · A scenario in which the need for out-zooming arises is when the modeler observes that the current OPD is already over-crowded, making it necessary to hide the content of an in-zoomed process in the current OPD. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3500** · `fact` · In-diagram out-zooming does not create a new OPD, which implies removing and losing the subprocesses and objects inside the process being out- zoomed. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3501** · `fact` · Therefore, unless the modeler decides that these subprocesses are too detailed for the purpose at hand and is ready to delete them, in-diagram out-zooming does not make a lot of sense. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3502** · `constraint` · New-diagram in-zooming elaborates a refineable in an existing OPD, say SDn, where n is the current level of detail, by creating a new OPD, SDn+1, which elaborates the refineable at the next detail level by adding subprocesses, associated objects, and relevant links. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3503** · `constraint` · Figure 21.12 is a metamodel of the New- Diagram In-Zooming and New-Diagram Out-Zooming processes. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3504** · `fact` · The OPM model on the right uses in- diagram in-zooming of the model on the left to elaborate the two processes: New-Diagram In-Zooming, for creating a new-diagram in-zoomed context, filled in with subprocesses and objects, and New-Diagram Out-Zooming, for creating a new-diagram out-zoomed (empty) context. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3505** · `fact` · New-Diagram In-Zooming begins with Content Showing, followed by Link Refining. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3506** · `fact` · New-Diagram Out-Zooming begins with Link Abstracting, the inverse process of Link Refining, followed by Content Hiding, the inverse process of Content Showing. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3507** · `fact` · Semi-Zoomed OPD is an interim object, which is created and subsequently consumed during both New Diagram In-Zooming and New-Diagram Out-Zooming. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3508** · `fact` · This interim object appears only within the contexts of both New-Diagram In-Zooming and New-Diagram Out-Zooming. In Fig. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3509** · `constraint` · 21.13, the metamodel on the left hand side of Fig. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3510** · `constraint` · 21.12 is elaborated by embedding an actual OPDs inside its objects SDn, SDn+1, and Semi-Zoomed OPD. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3511** · `fact` · In this particular OPM model example, SDn, presented in Fig. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3512** · `constraint` · 21.13 at the top middle, includes the process P, which is a refineable about to be in-zoomed, as well as four objects: the consumee C, the agent A, the instrument D, and the resultee B, connected to P with the corresponding different procedural links. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3513** · `fact` · This OPD inside the meta-object SDn is instrument for the New-Diagram In-Zooming on the left. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3514** · `fact` · Content Showing is the first of the two New-Diagram In-Zooming subprocesses. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3515** · `fact` · During Content Showing, the boundary of P expands to make room for showing its content—the model subprocesses P1, P2, and P3, as well as the interim model object BP. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3516** · `fact` · The result of Content Showing is presented as the content of the interim object Semi-Zoomed OPD. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3517** · `fact` · This interim object is recognizable only in the context of New-Diagram In-Zooming. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3518** · `constraint` · The second subprocess, Link Refining, done by the modeler, consumes it while creating SDn+1 presented in Fig. 21.13 at the bottom in the middle. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3519** · `fact` · During Link Refining, the procedural links attached to the contour of P migrate to the appropriate subprocesses as determined by the modeler. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3520** · `fact` · Thus, since P1 consumes C, the consumption link arrowhead migrates from P to P1. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3521** · `constraint` · The agent A handles both P1 and P2, so in SDn+1 two agent links, one to P1 and the other to P2, replace the single one in SDn from A to P. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3522** · `fact` · P3 requires D, so the instrument link migrates from P to P3. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3523** · `fact` · Finally, since BP results from P1, and P3 consumes it, the corresponding result and consumption links are added, making BP an interim, internal object of P, recognizable only within the context of P. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3524** · `fact` · Likewise, P1, P2, and P3 are internal processes of P, and as such they are recognizable only within the context of P. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3525** · `constraint` · The OPD inside the meta-object SDn+1 is instrument for the New-Diagram Out- Zooming on the right. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3526** · `fact` · What happens next is the exact inverse of what we have seen, both in the order of the subprocesses and what each of them does. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3527** · `fact` · Link Abstracting is the first of the two New-Diagram Out-Zooming subprocesses. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3528** · `fact` · During Link Abstracting, the links connected to subprocesses and interim objects of P migrate to (the boundary, the ellipse circumference of) P itself, resulting in exactly the same Semi-Zoomed OPD that is depicted inside New-Diagram In-Zooming. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3529** · `constraint` · This Semi-Zoomed OPD interim object is consumed by Content Hiding, creating SDn presented in Fig. 21.13 at the top in the middle. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)
- **P3530** · `fact` · The boundary of P can now shrink, as it is empty and there is no need for making room to show its content (the model subprocesses P1, P2, and P3, as well as the interim model object BP), which is now hidden. · [src:S01:L8935-L8988](../../../INBOX/opm-libro.txt#L8935-L8988)

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.15 Simplifying an OPD

- **P3531** · `fact` · In-diagram out-zooming—the elimination of an in-zoomed process content—followed by new-diagram in-zooming can simplify an already-modeled OPD that the modeler deems overly complicated or overloaded with details. · [src:S01:L8990-L9026](../../../INBOX/opm-libro.txt#L8990-L9026)
- **P3532** · `fact` · In-diagram out-zooming reduces the cognitive load necessary to understand the complicated OPD at the expense of adding a new OPD to the OPD set, which is the result of the subsequent new-diagram in-zooming, which creates a new OPD at an interim level of detail, as explained next. out-zooming. · [src:S01:L8990-L9026](../../../INBOX/opm-libro.txt#L8990-L9026)
- **P3533** · `constraint` · On the left is the original OPD set with three OPDs: SD, SD1 and SD1.1. · [src:S01:L8990-L9026](../../../INBOX/opm-libro.txt#L8990-L9026)
- **P3534** · `requirement` · Realizing that SD1 is overly complicated, in order to simplify the model, the modeler decides that a set TO (Things to be Out-zoomed), comprising four things in SD1—P1, P2, and P3, along with BP—shall be replaced by a single new process P123 via new-diagram out-zooming. In the middle of Fig. · [src:S01:L8990-L9026](../../../INBOX/opm-libro.txt#L8990-L9026)
- **P3535** · `requirement` · 21.14, P123 undergoes new-diagram out-zooming, resulting in SD1.1[new] (in a real implementation, the new OPDs shall not be marked with [new]; this label only helps the explanation here). Here is how this is done. · [src:S01:L8990-L9026](../../../INBOX/opm-libro.txt#L8990-L9026)
- **P3536** · `fact` · The modeler indicates the things in the set TO (things to be out-zoomed) and the name of the new interim process to be created (P123 in our case). · [src:S01:L8990-L9026](../../../INBOX/opm-libro.txt#L8990-L9026)
- **P3537** · `fact` · The grey background denotes these candidate elements. · [src:S01:L8990-L9026](../../../INBOX/opm-libro.txt#L8990-L9026)
- **P3538** · `fact` · The process-to-be P123 now undergoes new-diagram out-zooming, following the two subprocesses described earlier: link abstracting and content hiding. · [src:S01:L8990-L9026](../../../INBOX/opm-libro.txt#L8990-L9026)
- **P3539** · `constraint` · As a result of link abstracting, the links that were connected to subprocesses of the future P123 process migrated to the contour of the now- created P123, and as a result of content hiding, P123 becomes empty, as shown in SD1[new]. zooming yields a new OPM model on the left, in which SD1[new] and SD1.1[new] replace SD1 In order to preserve the model facts that were eliminated (such as the model facts that A is agent to P1 and P2), a new OPD, SD1.1[new], was created with these facts. Hence, on the right of Fig. · [src:S01:L8990-L9026](../../../INBOX/opm-libro.txt#L8990-L9026)
- **P3540** · `constraint` · 21.14 is the new OPD set, which now has four OPDs: SD[new], SD1[new], SD1.1[new], and SD1.1.1[new], renumbered to reflect the new OPD hierarchy, In this augmented hierarchy, the complicated OPD SD1 has been replaced by two simpler OPDs – SD1[new] and SD1.1[new]. · [src:S01:L8990-L9026](../../../INBOX/opm-libro.txt#L8990-L9026)
- **P3541** · `fact` · Examining SD1[new], we see that it is indeed less complicated and less crowded than the original SD1, since it has a net of five fewer elements: three removed processes, P1, P2, and P3, one removed object, BP, two removed links, and one added process, P123. · [src:S01:L8990-L9026](../../../INBOX/opm-libro.txt#L8990-L9026)
- **P3542** · `constraint` · This new OPD is inserted into the process hierarchy, pushing the old SD1.1, which remains unchanged, one detail level down, from detail level 2 to detail level 3. · [src:S01:L8990-L9026](../../../INBOX/opm-libro.txt#L8990-L9026)
- **P3543** · `constraint` · Due to the addition of SD1.1[new], SD1.1is renumbered to be SD1.1.1[new]. · [src:S01:L8990-L9026](../../../INBOX/opm-libro.txt#L8990-L9026)
