---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-67
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
      n_propositions: 41
      segmented: true
      segment_role: segment
      segment_index: 67
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-67
---

# Atomic opm-libro-rebuilt - Segmento 67

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `41`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `67/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.12 The System Map and the Ultimate OPD

- **P3457** · `constraint` · There is exactly one System Diagram, SD—the top-level OPD, the level 0 OPD. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3458** · `fact` · It often contains one main, core systemic process, which is the value-delivering function of the system. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3459** · `constraint` · Recursive new- diagram process in-zooming iterations result in a set of OPDs that are organized in a (hierarchical) tree structure, with SD being the root (detail level 0) of the OPD tree, SD1, SD2, etc. being at detail level 1 of the OPD hierarchy, SD1.1, SD1.2, … SD 2.1, SD2.2… being at detail level 2 of the OPD hierarchy, and so on. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3460** · `fact` · An OPD tree is a directed tree graph whose nodes are OPDs obtained by recursive refinement (in-zooming and/or unfolding) of processes in the system, starting with the function—the process in SD. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3461** · `fact` · The OPD set is the set of all the nodes in the OPD tree. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3462** · `fact` · Detail level of an OPD is the number of nodes in the OPD tree that need to be traversed from that OPD to the root, SD, including SD itself. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3463** · `fact` · The OPD tree is a tree of processes—a graph whose nodes are OPDs. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3464** · `constraint` · The root is SD, the System Diagram, and the other nodes are the descendant OPDs, marked with their OPD labels, such as SD1, which is at detail level 1, SD2.3, which is at detail level 2, etc. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3465** · `fact` · The directed edges of an OPD tree have labels with each edge pointing from the parent OPD, which contains the refineable element, to a child OPD containing refinees, which elaborates a process in the parent OPD via new-diagram in-zooming for synchronous subprocesses or new-diagram aggregation unfolding for asynchronous subprocesses. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3466** · `fact` · Since in-zooming has the semantics of aggregation-participation, each in-zooming in the hierarchy is also interpreted as aggregation-participation in order to preserve the tree structure. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3467** · `constraint` · Figure 21.10 shows at the top the OPD tree—the hierarchy of the Product Lifecycle Engineering system OPM model (Dori and Shpitalni 2005). The OPD set of the model in Fig. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3468** · `constraint` · 21.10 has 11 OPDs spanning 4 levels of detail. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3469** · `fact` · While the OPD tree is presented like a file hierarchy (see Fig. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3470** · `constraint` · 21.10 top), the system map, shown at the bottom of Fig. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3471** · `constraint` · 21.10, is a more elaborate presentation of the OPD tree. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3472** · `fact` · The system map is an elaborate OPD tree, in which each node in the tree is a miniaturized icon of the OPD, with thick grey arrows pointing from each process in one OPD to its refined (in-zoomed or unfolded) version in the child OPD. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3473** · `fact` · The system map explicitly depicts the elements (things and links) in each OPD (node). · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3474** · `requirement` · Because the system map may become very large and unwieldy, mechanisms shall allow access to model content and the associations among elements. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3475** · `fact` · The system map helps navigate in a complex system that may comprise hundreds of OPDs at many levels of detail. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3476** · `constraint` · As an example, the executable OPM model of the mRNA decay model in Somekh et al. (2014) contains hundreds of objects and processes in over 40 OPDs at 9 levels of detail, with hyperlinks from a thing in the model to the paper from which the model fact was extracted. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3477** · `constraint` · 2014), showing it being at an OPD SD2.4.2.2.1.2.4.2 – elF4F Dissociates Cap and Decaysome in-zoomed, as indicated also by the frame around this process in the OPD tree on the left. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3478** · `fact` · This OPD demonstrates the self-similarity of OPDs: regardless of what detail level an OPD is at, it used only stateful objects, processes, and relations among them. Currently, the system in Fig. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3479** · `constraint` · 21.11 is executing in parallel four subprocesses (in dark blue), after having completed the subprocess elF4F Dissociates Cap above them. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3480** · `fact` · The dissociation is manifested in each of these four subprocesses by consuming a link, modeled as an object in its own right, between two objects, e.g., the factor Xrn1 and the protein elF4E at the bottom are dissociated by the process elF4E and Xrn1 Dissociation. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3481** · `fact` · Below the OPD is the lifespan diagram, enabling inspection of each object and process at each point in time. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3482** · `constraint` · The browser on the left is open on the relevant paper, one of the 43 papers from which the model facts in this OPD were taken, obtained by clicking on the in-zoomed process. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3483** · `fact` · This example demonstrates the indispensability of the refinement mechanisms, and in particular in- zooming. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3484** · `fact` · Without it, it would be impossible to comprehensibly show the hundreds of things in the model and the thousands of links among them in a single OPD or in any other kind of diagram. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3485** · `fact` · In addition, an OPM tool set should provide a mechanism for creating views, as OPDs with associated OPL sentences, of objects and processes that meet specific criteria. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3486** · `fact` · These views may include the critical path for minimal system execution duration, or a list of system agents and instruments, or an OPD of objects and processes involved in a specific kind of link or set of links. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3487** · `constraint` · For example, an OPD can be created by (1) refining (unfolding or in-zooming) an object or (2) collecting and presenting in a new OPD things that appear in various OPDs for expressing assignment of system sub-functions to system-module objects. model The ultimate OPD is single flat representation of the OPM system model. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3488** · `fact` · The ultimate OPD is obtained by recursively flattening the OPD tree from the bottom up all the way to the OPD tree toot, such that the entire model is represented in this single OPD. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3489** · `fact` · Except for very small system models, the ultimate OPD is definitely unfit for use by humans due to our limited cognitive capacity. · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)
- **P3490** · `constraint` · However, for computer processing—knowledge management, navigation, querying, etc., the ultimate OPD is very useful. level 8—SD2.4.2.2.1.2.4.2—elF4F Dissociates Cap and Decaysome in-zoomed · [src:S01:L8844-L8916](../../../INBOX/opm-libro.txt#L8844-L8916)

## opm libro · Chapter 21 Complexity Management: Refinement and Abstraction / 21.13 The OPD Object Tree and Forest

- **P3491** · `fact` · Unlike the OPD (process) tree, which results from process refinement and has a single root, there can be many OPD object trees, at least one from each refineable object, which together constitute a forest. · [src:S01:L8918-L8933](../../../INBOX/opm-libro.txt#L8918-L8933)
- **P3492** · `fact` · An OPD object tree is a tree whose root is an object B and whose nodes are things that result from recursively refining B via unfolding and in-zooming, where each in- zooming is converted to aggregation-participation. · [src:S01:L8918-L8933](../../../INBOX/opm-libro.txt#L8918-L8933)
- **P3493** · `fact` · Each tree stems from a distinct refineable object that unfolds or in-zooms to reveal its details—not necessarily just parts as in the process in-zooming, but possibly also features, specializations, or instances. · [src:S01:L8918-L8933](../../../INBOX/opm-libro.txt#L8918-L8933)
- **P3494** · `fact` · Rather than identifying the possible flow of execution control as in the OPD (process) tree, each OPD object tree encapsulates the information about an object as a hierarchical structure. · [src:S01:L8918-L8933](../../../INBOX/opm-libro.txt#L8918-L8933)
- **P3495** · `fact` · Since in- zooming has the semantics of aggregation-participation, like the OPD tree, each in-zooming in the hierarchy of the OPD process is also interpreted as aggregation-participation in order to preserve the tree structure. · [src:S01:L8918-L8933](../../../INBOX/opm-libro.txt#L8918-L8933)
- **P3496** · `constraint` · Complete or partial OPD object trees can be presented as views (see Sect. 21.18). · [src:S01:L8918-L8933](../../../INBOX/opm-libro.txt#L8918-L8933)
- **P3497** · `constraint` · The root of each OPD object tree can be attached as a child of the node in the OPD (process) tree, creating the system map (see Sect. 21.12). · [src:S01:L8918-L8933](../../../INBOX/opm-libro.txt#L8918-L8933)
