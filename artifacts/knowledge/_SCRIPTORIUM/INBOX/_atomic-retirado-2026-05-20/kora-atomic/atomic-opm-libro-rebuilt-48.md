---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-48
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
      n_propositions: 54
      segmented: true
      segment_role: segment
      segment_index: 48
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-48
---

# Atomic opm-libro-rebuilt - Segmento 48

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `54`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `48/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 16 Fundamental Structural Relations / 16.1 Relation Symbols and Participants

- **P2488** · `fact` · Due to the prevalence of the fundamental structural relations, in order to avoid writing their tags over and over again and make them readily graphically identifiable, each one of the four fundamental structural relations is assigned with a unique triangular symbol. · [src:S01:L6432-L6509](../../../INBOX/opm-libro.txt#L6432-L6509)
- **P2489** · `constraint` · Table 16.1 lists the fundamental structural relations with their respective triangular symbols as they appear linked in an OPD, and the OPL sentence that corresponds to each OPD. · [src:S01:L6432-L6509](../../../INBOX/opm-libro.txt#L6432-L6509)
- **P2490** · `fact` · While all the OPD examples are of objects linked to objects (except for Operation B), being structural relations, the four fundamental structural relations exist between processes and can be depicted also linking processes. · [src:S01:L6432-L6509](../../../INBOX/opm-libro.txt#L6432-L6509)
- **P2491** · `definition` · To begin, we next define refineable and refinee. · [src:S01:L6432-L6509](../../../INBOX/opm-libro.txt#L6432-L6509)
- **P2492** · `fact` · Refineable is a thing amenable to refinement via a fundamental structural relation. · [src:S01:L6432-L6509](../../../INBOX/opm-libro.txt#L6432-L6509)
- **P2493** · `fact` · Each Refineable is the ancestor (parent) of the two-level hierarchy induced by the fundamental structural relation. · [src:S01:L6432-L6509](../../../INBOX/opm-libro.txt#L6432-L6509)
- **P2494** · `constraint` · Hence, as Table 16.1 presents in brackets in the leftmost column, a Refineable can be a Whole, an Exhibitor, a General, or a Class. · [src:S01:L6432-L6509](../../../INBOX/opm-libro.txt#L6432-L6509)
- **P2495** · `fact` · Each of the four refineables corresponds to one of the four fundamental structural relation. · [src:S01:L6432-L6509](../../../INBOX/opm-libro.txt#L6432-L6509)
- **P2496** · `fact` · Refinee is a thing that refines a refineable. · [src:S01:L6432-L6509](../../../INBOX/opm-libro.txt#L6432-L6509)
- **P2497** · `fact` · Each Refinee is the descendant (child) of the two-level hierarchy induced by the fundamental structural relation. · [src:S01:L6432-L6509](../../../INBOX/opm-libro.txt#L6432-L6509)
- **P2498** · `constraint` · Table 16.1 presents in brackets in the second-from-left column the four Refinees corresponding to the refineables in the structural relations: a Part, a Feature, a Specialization, and an Instance. · [src:S01:L6432-L6509](../../../INBOX/opm-libro.txt#L6432-L6509)
- **P2499** · `fact` · As we discuss later, Feature, in turn, specializes into Attribute (a structural feature) and Operation (a procedural feature). · [src:S01:L6432-L6509](../../../INBOX/opm-libro.txt#L6432-L6509)
- **P2500** · `constraint` · Table 16.1 The fundamental structural relation names, OPD symbols, and OPL sentences Structural Relation Name [Participant Name] OPL Sentence(s) Graphic Symbol with OPD usage Forward [Refineable] Backward [Refinee] Forward Backward Whole Aggregation [Whole] Participation [Part] Whole consists of Part A and Part B. · [src:S01:L6432-L6509](../../../INBOX/opm-libro.txt#L6432-L6509)
- **P2501** · `fact` · Part A Part B Exhibition [Exhibitor] Characterization [Feature: Attribute or Operation] Exhibitor Attribute A Operation B Exhibitor exhibits Attribute A as well as Operation B. · [src:S01:L6432-L6509](../../../INBOX/opm-libro.txt#L6432-L6509)
- **P2502** · `fact` · General Thing Generalization [General] Specialization [Specialization] Specialization A Specialization B Specialization A and Specialization B are General Things. · [src:S01:L6432-L6509](../../../INBOX/opm-libro.txt#L6432-L6509)
- **P2503** · `fact` · Class Classification [Class] Instantiation [Instance] Instance A Instance B Instance A and Instance B are instances of Class. · [src:S01:L6432-L6509](../../../INBOX/opm-libro.txt#L6432-L6509)

## opm libro · Chapter 16 Fundamental Structural Relations / 16.2 Relation Names and OPL Sentences

- **P2504** · `constraint` · The name of each fundamental structural relation consists of a pair of dash-separated words.1 As Table 16.1 presents, the first word in each such pair is the forward relation name, i.e., the name of the relation as seen from the viewpoint of the thing up in the hierarchy—the ancestor, or parent—while looking down the hierarchy. · [src:S01:L6511-L6548](../../../INBOX/opm-libro.txt#L6511-L6548)
- **P2505** · `fact` · The second word is the backward (or reverse) relation name, i.e., the name of the relation as seen from the viewpoint of the thing down in the hierarchy—the descendant, or child—of that relation while looking up the hierarchy. · [src:S01:L6511-L6548](../../../INBOX/opm-libro.txt#L6511-L6548)
- **P2506** · `fact` · The first fundamental structural relation, aggregation-participation, denotes the relation between a whole thing and its parts. · [src:S01:L6511-L6548](../../../INBOX/opm-libro.txt#L6511-L6548)
- **P2507** · `fact` · Exhibition-characterization denotes the relation between a thing and its features (attributes and operations). · [src:S01:L6511-L6548](../../../INBOX/opm-libro.txt#L6511-L6548)
- **P2508** · `fact` · Generalization-specialization denotes the relation between a general thing and its specializations. · [src:S01:L6511-L6548](../../../INBOX/opm-libro.txt#L6511-L6548)
- **P2509** · `fact` · Finally, classification-instantiation denotes the relation between a class of things and the instances of that class. · [src:S01:L6511-L6548](../../../INBOX/opm-libro.txt#L6511-L6548)
- **P2510** · `fact` · Since the full names of these relations are rather long, each has a short version, which is either the forward or backward structural relation name only. · [src:S01:L6511-L6548](../../../INBOX/opm-libro.txt#L6511-L6548)
- **P2511** · `constraint` · The short name, denoted in Table 16.1 by bold letters, is selected to be the more meaningful of the two: Aggregation, Characterization, Generalization, and Classification. · [src:S01:L6511-L6548](../../../INBOX/opm-libro.txt#L6511-L6548)
- **P2512** · `constraint` · As Table 16.1 shows, all the four fundamental structural relation symbols are equilateral triangles linked via orthonormal polylines, i.e., lines whose segments are parallel to either one of the diagram axes (also called Manhattan lines). · [src:S01:L6511-L6548](../../../INBOX/opm-libro.txt#L6511-L6548)
- **P2513** · `constraint` · The tip of the triangle is linked through an orthonormal polyline to the root of the hierarchy tree—the aggregate or whole in our case (Whole, in the first row of Table 16.1, for example). · [src:S01:L6511-L6548](../../../INBOX/opm-libro.txt#L6511-L6548)
- **P2514** · `fact` · The triangle’s base is linked through other orthonormal polylines to each one of the parts of the aggregate (Part A and Part B in our example). · [src:S01:L6511-L6548](../../../INBOX/opm-libro.txt#L6511-L6548)
- **P2515** · `fact` · The fact that the links of the fundamental structural relations run horizontally or vertically but not diagonally (like all the procedural links) helps differentiate them visually from procedural links. · [src:S01:L6511-L6548](../../../INBOX/opm-libro.txt#L6511-L6548)
- **P2516** · `fact` · Using different colors for different links that cross each other (which should be avoided as much as possible) is also helpful in crowded OPDs. · [src:S01:L6511-L6548](../../../INBOX/opm-libro.txt#L6511-L6548)
- **P2517** · `fact` · The OPL sentences of the fundamental structural relations are also either in the forward or the backward direction. · [src:S01:L6511-L6548](../../../INBOX/opm-libro.txt#L6511-L6548)
- **P2518** · `fact` · The direction was similarly determined by how natural the sentence sounds in plain English. · [src:S01:L6511-L6548](../../../INBOX/opm-libro.txt#L6511-L6548)
- **P2519** · `fact` · The forward direction is used for aggregation and characterization: Whole consists of Part A and Part B. · [src:S01:L6511-L6548](../../../INBOX/opm-libro.txt#L6511-L6548)
- **P2520** · `fact` · Exhibitor exhibits Attribute A, as well as Operation B. · [src:S01:L6511-L6548](../../../INBOX/opm-libro.txt#L6511-L6548)
- **P2521** · `fact` · The backward direction is used for generalization and classification: Specialization A and Specialization B are General Things. · [src:S01:L6511-L6548](../../../INBOX/opm-libro.txt#L6511-L6548)
- **P2522** · `fact` · Instance A and Instance B are instances of Class. · [src:S01:L6511-L6548](../../../INBOX/opm-libro.txt#L6511-L6548)
- **P2523** · `fact` · As usual, the multiple versions of these two OPL sentences, which include three or more refinees, are: Specialization A, Specialization B, and Specialization C are General Things. · [src:S01:L6511-L6548](../../../INBOX/opm-libro.txt#L6511-L6548)
- **P2524** · `fact` · Instance A, Instance B, and Instance C are instances of Class. · [src:S01:L6511-L6548](../../../INBOX/opm-libro.txt#L6511-L6548)

## opm libro · Chapter 16 Fundamental Structural Relations / 16.3 Structural Hierarchies, Transitivity, User-Defined Symbols

- **P2525** · `fact` · The special graphic symbols assigned to the four fundamental structural relations due to their prevalence and usefulness do not make them particularly special; diagramming convenience, avoiding multiple tags, and ease of diagram reading have motivated the introduction of these symbols. · [src:S01:L6550-L6580](../../../INBOX/opm-libro.txt#L6550-L6580)
- **P2526** · `fact` · Yet, the first three of these four relations do have in common the hierarchy and transitivity they induce (examples are given in the relevant chapters that follow, discussing each relation separately): In Aggregation, a part can be the whole of yet smaller parts, creating an aggregation-participation hierarchy. · [src:S01:L6550-L6580](../../../INBOX/opm-libro.txt#L6550-L6580)
- **P2527** · `fact` · This hierarchy is transitive: If A consists of B (and other parts) and B consists of C (and other parts), then A (indirectly) consists of C (and other parts). · [src:S01:L6550-L6580](../../../INBOX/opm-libro.txt#L6550-L6580)
- **P2528** · `fact` · In Characterization, a feature (attribute or operation) can be the exhibitor of lower-level features, creating an exhibition-characterization hierarchy. · [src:S01:L6550-L6580](../../../INBOX/opm-libro.txt#L6550-L6580)
- **P2529** · `fact` · This hierarchy is transitive: If A exhibits B and B exhibits C, then A (indirectly) exhibits C. · [src:S01:L6550-L6580](../../../INBOX/opm-libro.txt#L6550-L6580)
- **P2530** · `fact` · In Generalization, a specialization can generalize lower-level specializations, creating a generalization-specialization hierarchy. · [src:S01:L6550-L6580](../../../INBOX/opm-libro.txt#L6550-L6580)
- **P2531** · `fact` · This hierarchy is transitive: If A generalizes B (and possibly other specializations) and B consists of C (and possibly other specializations), then A (indirectly) generalizes C (and possibly other specializations). · [src:S01:L6550-L6580](../../../INBOX/opm-libro.txt#L6550-L6580)
- **P2532** · `fact` · With respect to Classification, as explained in Chap. · [src:S01:L6550-L6580](../../../INBOX/opm-libro.txt#L6550-L6580)
- **P2533** · `constraint` · 20, an instance can only be a leaf in a generalization-specialization hierarchy. · [src:S01:L6550-L6580](../../../INBOX/opm-libro.txt#L6550-L6580)
- **P2534** · `fact` · Therefore, the classification-instantiation relation cannot be transitive. · [src:S01:L6550-L6580](../../../INBOX/opm-libro.txt#L6550-L6580)
- **P2535** · `fact` · Complex hierarchies can be created by mixing combinations of the four relations. · [src:S01:L6550-L6580](../../../INBOX/opm-libro.txt#L6550-L6580)
- **P2536** · `fact` · Following this idea of denoting a frequently used relation by a special symbol, it is possible to add a symbol for one or more structural relations that are widely used within a specialized domain. · [src:S01:L6550-L6580](../../../INBOX/opm-libro.txt#L6550-L6580)
- **P2537** · `fact` · Consider an example from the domain of chemical laboratory testing of industrial lots. · [src:S01:L6550-L6580](../../../INBOX/opm-libro.txt#L6550-L6580)
- **P2538** · `fact` · In this domain, the phrase “is a sample of” is a very prevalent and useful structural relation between a sample and the lot from which it was taken. · [src:S01:L6550-L6580](../../../INBOX/opm-libro.txt#L6550-L6580)
- **P2539** · `fact` · A dedicated graphic symbol and a corresponding reserved phrase “is a sample of” can be introduced in this domain to enable quicker and easier modeling. · [src:S01:L6550-L6580](../../../INBOX/opm-libro.txt#L6550-L6580)
- **P2540** · `fact` · The symbol selected in a real case in work done at ISCAR Ltd.—an enterprise operating in the domain of metal cutting tool manufacturing by sintering technology—was a piece cut out of a cake, symbolizing that the taste of the piece of cake—the sample— is the same of the entire cake—the lot from which the sample was taken. · [src:S01:L6550-L6580](../../../INBOX/opm-libro.txt#L6550-L6580)
- **P2541** · `fact` · The four fundamental structural relations are so central to conceptual modeling that the next chapters are devoted to discussing each one of them. · [src:S01:L6550-L6580](../../../INBOX/opm-libro.txt#L6550-L6580)
