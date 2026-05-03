---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-47
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
      n_propositions: 44
      segmented: true
      segment_role: segment
      segment_index: 47
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-47
---

# Atomic opm-libro-rebuilt - Segmento 47

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `44`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `47/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 15 Participation Constraints and Forks / 15.8.2 Fork Comprehensiveness

- **P2444** · `fact` · While omission of irrelevant tine things helps eliminate the excess clutter frequently caused in OPDs of real life systems, it may also mislead the reader of an individual OPD into thinking that the tine thing set presented in that particular OPD is comprehensive, i.e., all the tine things that can be linked to the handle thing are indeed linked. · [src:S01:L6273-L6306](../../../INBOX/opm-libro.txt#L6273-L6306)
- **P2445** · `fact` · To avoid such confusion, it is important to indicate whether all the things in the tine thing set that can be linked to the handle are indeed linked. · [src:S01:L6273-L6306](../../../INBOX/opm-libro.txt#L6273-L6306)
- **P2446** · `definition` · To this end, we define the fork’s comprehensiveness property value as follows. · [src:S01:L6273-L6306](../../../INBOX/opm-libro.txt#L6273-L6306)
- **P2447** · `fact` · Fork comprehensiveness is a Boolean property of a fork which is positive if all the things in the tine thing set are attached to the fork’s handle and negative otherwise. · [src:S01:L6273-L6306](../../../INBOX/opm-libro.txt#L6273-L6306)
- **P2448** · `fact` · Being a Boolean property, Comprehensiveness has two values: positive, if the fork is comprehensive, i.e., all the things in the tine thing set are attached to the fork’s handle, and negative otherwise. · [src:S01:L6273-L6306](../../../INBOX/opm-libro.txt#L6273-L6306)
- **P2449** · `fact` · Using the fork’s comprehensiveness property, one can indicate whether the structure implied by the fork is comprehensive or non-comprehensive. · [src:S01:L6273-L6306](../../../INBOX/opm-libro.txt#L6273-L6306)
- **P2450** · `fact` · The importance of fork comprehensiveness is that it tells the diagram reader whether all the tine things that can potentially be linked to the handle object are indeed linked. · [src:S01:L6273-L6306](../../../INBOX/opm-libro.txt#L6273-L6306)
- **P2451** · `fact` · A non-comprehensive fork is marked by a short bar perpendicular to the fork near the handle thing. Continuing the example in Fig. · [src:S01:L6273-L6306](../../../INBOX/opm-libro.txt#L6273-L6306)
- **P2452** · `constraint` · 15.11, suppose in some OPD we wish to show only those countries or areas that were historically “behind the iron curtain”. Examining the OPD in Fig. · [src:S01:L6273-L6306](../../../INBOX/opm-libro.txt#L6273-L6306)
- **P2453** · `constraint` · 15.13, we see that Germany and Austria were removed. · [src:S01:L6273-L6306](../../../INBOX/opm-libro.txt#L6273-L6306)
- **P2454** · `fact` · Graphically, the non-comprehensiveness of this fork is marked by the non-comprehensive fork symbol—the short bar perpendicular to the fork near the handle object. · [src:S01:L6273-L6306](../../../INBOX/opm-libro.txt#L6273-L6306)
- **P2455** · `fact` · This non-comprehensive fork symbol expresses the fact that not all the countries through which the Danube River passes are represented in this OPD. · [src:S01:L6273-L6306](../../../INBOX/opm-libro.txt#L6273-L6306)
- **P2456** · `constraint` · The OPL reserved phrase that expresses the fact that the fork is non-comprehensive is “and more”, which is appended at the end of the list of fork objects, as the OPL sentence in Fig. 15.13 demonstrates. · [src:S01:L6273-L6306](../../../INBOX/opm-libro.txt#L6273-L6306)
- **P2457** · `fact` · The default value of the fork’s Comprehensiveness property is positive, meaning that the fork is comprehensive and indicating that all the objects in the tine set of the fork are attached to the fork’s handle. · [src:S01:L6273-L6306](../../../INBOX/opm-libro.txt#L6273-L6306)
- **P2458** · `fact` · In this default case the handle will not be marked with the non-comprehensive fork symbol. · [src:S01:L6273-L6306](../../../INBOX/opm-libro.txt#L6273-L6306)
- **P2459** · `fact` · The other value of Comprehensiveness is negative, so the fork is non-comprehensive, implying that the tine set is incomplete, as at least one tine thing is missing. · [src:S01:L6273-L6306](../../../INBOX/opm-libro.txt#L6273-L6306)
- **P2460** · `constraint` · The OPL reserved phrase “and at least one more” at the end of the OPL sentence in Fig. 15.13 expresses this. · [src:S01:L6273-L6306](../../../INBOX/opm-libro.txt#L6273-L6306)
- **P2461** · `fact` · A non-comprehensive fork can be made comprehensive by completing the missing things in the forks’ tine thing set while removing the non- comprehensive fork symbol, thereby changing its Comprehensiveness state from negative to positive. · [src:S01:L6273-L6306](../../../INBOX/opm-libro.txt#L6273-L6306)

## opm libro · Chapter 15 Participation Constraints and Forks / 15.8.3 Fork Orderability

- **P2462** · `fact` · The elements of a set in general, and the things in the tine thing set of a fork in particular, can be ordered or unordered. · [src:S01:L6308-L6339](../../../INBOX/opm-libro.txt#L6308-L6339)
- **P2463** · `fact` · This is determined by the fork’s orderability property. · [src:S01:L6308-L6339](../../../INBOX/opm-libro.txt#L6308-L6339)
- **P2464** · `fact` · Orderability is a Boolean property of a fork’s thing tine set, which is positive if the things in the tine thing set are ordered and negative otherwise. · [src:S01:L6308-L6339](../../../INBOX/opm-libro.txt#L6308-L6339)
- **P2465** · `fact` · Like Comprehensiveness, Orderability is a Boolean attribute of the Tine Set of a Fork, whose values are positive and negative. · [src:S01:L6308-L6339](../../../INBOX/opm-libro.txt#L6308-L6339)
- **P2466** · `fact` · A Tine Set with negative Orderability is an Unordered Tine Set, and this is the default, so it requires no special indication. · [src:S01:L6308-L6339](../../../INBOX/opm-libro.txt#L6308-L6339)
- **P2467** · `constraint` · For a thing tine set with positive orderability, there often (but not always) exists some logical relation of the things in the tine thing set {T1 … TN} such that T (j) T (j+1) for each T (j) in {T (1) ,T (2) ,..,T (N)}. For example, if Ti; · [src:S01:L6308-L6339](../../../INBOX/opm-libro.txt#L6308-L6339)
- **P2468** · `constraint` · 1 < i < N is a set of N natural numbers, and is the < inequality symbol, then the orderability of the tine thing set is positive. · [src:S01:L6308-L6339](../../../INBOX/opm-libro.txt#L6308-L6339)
- **P2469** · `fact` · If the tine thing set is the parts of a scientific paper {header, body, footer} there is no that determines this order. · [src:S01:L6308-L6339](../../../INBOX/opm-libro.txt#L6308-L6339)
- **P2470** · `fact` · A Tine Set with positive Orderability is an Ordered Tine Set. · [src:S01:L6308-L6339](../../../INBOX/opm-libro.txt#L6308-L6339)
- **P2471** · `constraint` · To denote that a fork’s tine set is ordered, the word ordered appears next to the handle of the fork, as demonstrated in the OPD in Fig. 15.14. · [src:S01:L6308-L6339](../../../INBOX/opm-libro.txt#L6308-L6339)
- **P2472** · `fact` · The word ordered is a graphic symbol rather than a reserved OPL phrase, because it is part of the OPD just like the non-comprehensiveness fork symbol. As Fig. · [src:S01:L6308-L6339](../../../INBOX/opm-libro.txt#L6308-L6339)
- **P2473** · `constraint` · 15.14 shows, the OPL reserved phrase for denoting that a tine thing set is ordered, is “in this order”, which is added after a comma at the end of the sentence. · [src:S01:L6308-L6339](../../../INBOX/opm-libro.txt#L6308-L6339)
- **P2474** · `fact` · For a non-comprehensive and ordered fork, the OPL phrase is “and at least one more, in that sequence”. · [src:S01:L6308-L6339](../../../INBOX/opm-libro.txt#L6308-L6339)
- **P2475** · `requirement` · To express the order graphically, the things in the tine thing set must be arranged either horizontally from left to right, as in Fig. 15.15, or vertically, from top to bottom. · [src:S01:L6308-L6339](../../../INBOX/opm-libro.txt#L6308-L6339)
- **P2476** · `fact` · The object boxes may not be ordered nicely even though the orderability of the tine thing set is positive. · [src:S01:L6308-L6339](../../../INBOX/opm-libro.txt#L6308-L6339)
- **P2477** · `fact` · To resolve this potential ambiguity, the ordering algorithm is to arrange the objects by the left-to-right order of their leftmost side of the object box (increasing x coordinate), and for those with the same left side coordinate, arrange by top-to-bottom order of the topmost side of the object box (decreasing y coordinate, or increasing if we consider the coordinates of pixels in a monitor). · [src:S01:L6308-L6339](../../../INBOX/opm-libro.txt#L6308-L6339)
- **P2478** · `fact` · The same applies to processes, where the box is the one that encloses the process ellipse. · [src:S01:L6308-L6339](../../../INBOX/opm-libro.txt#L6308-L6339)

## opm libro · Chapter 15 Participation Constraints and Forks / 15.8.4 Tine Thing Set Order Rule

- **P2479** · `fact` · The order of the things in the tine thing set can be based on some rule. · [src:S01:L6341-L6353](../../../INBOX/opm-libro.txt#L6341-L6353)
- **P2480** · `fact` · Order rule is a property of an ordered tine thing set, which specifies textually in the OPD the rule or criterion according to which the things in the tine thing set are ordered. · [src:S01:L6341-L6353](../../../INBOX/opm-libro.txt#L6341-L6353)
- **P2481** · `fact` · The Order Rule can be null, which is the default, or any other phrase written in lower-case letters. · [src:S01:L6341-L6353](../../../INBOX/opm-libro.txt#L6341-L6353)
- **P2482** · `fact` · Order Rule whose value is null means that there is no order criterion, and nothing (if there is no order) or “ordered” (if there is order but the rule is trivial, such as the order of the days of the week) is written next to the handle. · [src:S01:L6341-L6353](../../../INBOX/opm-libro.txt#L6341-L6353)
- **P2483** · `fact` · If there is an ordering rule that needs to be specified, the phrase “ordered by” rather than “ordered” is used in the OPD next to the fork, and recorded below it is the order criterion itself. For example, the OPD in Fig. · [src:S01:L6341-L6353](../../../INBOX/opm-libro.txt#L6341-L6353)
- **P2484** · `constraint` · 15.15 indicates an ordered tine set with the order rule “river flow”, implying that the countries are ordered by following the flow of the Danube River. · [src:S01:L6341-L6353](../../../INBOX/opm-libro.txt#L6341-L6353)

## opm libro · Chapter 16 Fundamental Structural Relations

- **P2485** · `fact` · Four structural relations are most prevalent and play an especially important role in specifying and understanding systems. · [src:S01:L6420-L6430](../../../INBOX/opm-libro.txt#L6420-L6430)
- **P2486** · `fact` · Termed the fundamental structural relations, these relations are: Aggregation-participation, which denotes the relation between a whole and its parts, Exhibition-characterization, which denotes the relation between an exhibitor—a thing exhibiting a one or more features (attributes and/or operations) and the things that characterize the exhibitor, Generalization-specialization, which denotes the relation between a general thing and its specializations, giving rise to inheritance, and Classification-instantiation, which denotes the relation between a class of things and an instance of that class. · [src:S01:L6420-L6430](../../../INBOX/opm-libro.txt#L6420-L6430)
- **P2487** · `fact` · This chapter is devoted to discussing these structural relations, while subsequent chapters deal with each of them separately. · [src:S01:L6420-L6430](../../../INBOX/opm-libro.txt#L6420-L6430)
