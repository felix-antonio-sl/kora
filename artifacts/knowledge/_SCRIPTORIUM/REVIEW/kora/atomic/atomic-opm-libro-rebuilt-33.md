---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-33
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
      n_propositions: 53
      segmented: true
      segment_role: segment
      segment_index: 33
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-33
---

# Atomic opm-libro-rebuilt - Segmento 33

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `53`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `33/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 12 SysML: Foundations and Diagrams / 12.8 Parametric Diagram and Constraint Property Blocks

- **P1692** · `fact` · The SysML parametric diagram provides for expressing constrains between properties, thereby enabling integration of mathematical calculations or engineering analyses, such as performance and reliability models, with SysML design models. · [src:S01:L4445-L4492](../../../INBOX/opm-libro.txt#L4445-L4492)
- **P1693** · `fact` · Constraint property blocks can also specify a network of quantitative constraints stemming from mathematical expressions of physical properties of a system. · [src:S01:L4445-L4492](../../../INBOX/opm-libro.txt#L4445-L4492)
- **P1694** · `fact` · The constraints are captured in constraint property blocks—ConstraintBlock constructs, expressed as equations that include the underlying parameters. · [src:S01:L4445-L4492](../../../INBOX/opm-libro.txt#L4445-L4492)
- **P1695** · `fact` · For example, a ConstraintBlock can have the parameters F, m, and a, and the constraint {F=ma}. · [src:S01:L4445-L4492](../../../INBOX/opm-libro.txt#L4445-L4492)
- **P1696** · `constraint` · Another example is the kinetic energy equation E=mv2/2. · [src:S01:L4445-L4492](../../../INBOX/opm-libro.txt#L4445-L4492)
- **P1697** · `fact` · Performance parameters and their relationships to other parameters can be tracked throughout the system life cycle. · [src:S01:L4445-L4492](../../../INBOX/opm-libro.txt#L4445-L4492)
- **P1698** · `fact` · SysML constraint property blocks enable the integration of engineering analysis, such as performance and reliability models, with other SysML models. A constraint block (see Fig. · [src:S01:L4445-L4492](../../../INBOX/opm-libro.txt#L4445-L4492)
- **P1699** · `constraint` · 12.12 left) includes the constraint, normally in terms of a mathematical equation, and the parameters of the constraint, such as E, m, and v for energy, mass, and velocity. · [src:S01:L4445-L4492](../../../INBOX/opm-libro.txt#L4445-L4492)
- **P1700** · `definition` · For reuse purposes, constraint blocks are defined in a Block Definition Diagram. · [src:S01:L4445-L4492](../../../INBOX/opm-libro.txt#L4445-L4492)
- **P1701** · `fact` · Parametric Diagrams use constraint blocks to constrain the value properties of other blocks. · [src:S01:L4445-L4492](../../../INBOX/opm-libro.txt#L4445-L4492)
- **P1702** · `fact` · Constraint blocks may thus be reused on block definition diagrams and packaged into general-purpose or domain-specific model libraries. · [src:S01:L4445-L4492](../../../INBOX/opm-libro.txt#L4445-L4492)
- **P1703** · `constraint` · This constraining is done by binding the constraint parameters (such as m in the example above) to specific actual value properties of a block (such as the mass of a vehicle). A parametric diagram example appears in Fig. 12.13. · [src:S01:L4445-L4492](../../../INBOX/opm-libro.txt#L4445-L4492)
- **P1704** · `constraint` · Figure 12.14 is an OPD representation of this parametric diagram.1 A parametric diagram (see Fig. · [src:S01:L4445-L4492](../../../INBOX/opm-libro.txt#L4445-L4492)
- **P1705** · `constraint` · 12.12 right) uses one or more constraint property blocks to constrain the properties of one or more other blocks by binding the parameters through a mathematical relation. · [src:S01:L4445-L4492](../../../INBOX/opm-libro.txt#L4445-L4492)
- **P1706** · `constraint` · A constraint property may be shown on a parametric diagram using a standard form of internal property rectangle with the «constraint» keyword (short for constraintProperty) preceding its name (see Fig. 12.12 left). · [src:S01:L4445-L4492](../../../INBOX/opm-libro.txt#L4445-L4492)
- **P1707** · `fact` · However, a constraint property may also be shown on a parametric diagram using a rountangle (see shown within the rountangle. · [src:S01:L4445-L4492](../../../INBOX/opm-libro.txt#L4445-L4492)
- **P1708** · `constraint` · Using this shape enables avoiding the need to explicitly record the «constraint» keyword. fuel pressure through the relation FuelFlow = Pressure/(4(InjectorDemand)), presumably due the fact that this is a 4-cylinder engine. · [src:S01:L4445-L4492](../../../INBOX/opm-libro.txt#L4445-L4492)
- **P1709** · `fact` · Any mathematical operation, from the basic four arithmetic operations to the most complex computation, can be viewed in OPM in terms of a calculating (informatical) process that uses (but not consumes) one or more input parameters to produce an output. · [src:S01:L4445-L4492](../../../INBOX/opm-libro.txt#L4445-L4492)
- **P1710** · `fact` · With this in mind, any SysML parametric diagram can be presented as an OPD where the constraint is a Calculating process preceded by the mathematical expression that binds and constrains the input parameters. · [src:S01:L4445-L4492](../../../INBOX/opm-libro.txt#L4445-L4492)
- **P1711** · `constraint` · The input parameters are instruments, unless we wish to specify that they are not kept after the Calculating process ends. v1.3, p.199) Adopting this simple concept transformation, Fig. · [src:S01:L4445-L4492](../../../INBOX/opm-libro.txt#L4445-L4492)
- **P1712** · `constraint` · 12.14 is an OPD representation of the parametric diagram in Fig. 12.13. · [src:S01:L4445-L4492](../../../INBOX/opm-libro.txt#L4445-L4492)
- **P1713** · `constraint` · In addition to this compact graphic representation, we get “for free” the OPL textual representation, which can be readily translated to code in any programming language or even directly executed to compute Pressure/(4(Injector Demand)). · [src:S01:L4445-L4492](../../../INBOX/opm-libro.txt#L4445-L4492)
- **P1714** · `constraint` · Another, more involved example for doing calculations in OPM appears in Figs. 22.5 and 22.6. · [src:S01:L4445-L4492](../../../INBOX/opm-libro.txt#L4445-L4492)

## opm libro · Chapter 12 SysML: Foundations and Diagrams / 12.9 SysML–OPM Comparison

- **P1715** · `fact` · In this section we compare SysML to OPM first in terms of relating to each language as a whole and then by discussing and showing how OPM can be applied to model several SysML diagram kinds. · [src:S01:L4495-L4544](../../../INBOX/opm-libro.txt#L4495-L4544)
- **P1716** · `constraint` · Table 12.1 provides a compact comparison between SysML and OPM in terms of various attributes. · [src:S01:L4495-L4544](../../../INBOX/opm-libro.txt#L4495-L4544)
- **P1717** · `constraint` · Table 12.1 Comparison between SysML and OPM attributes Feature SysML OPM Theoretical foundation UML; · [src:S01:L4495-L4544](../../../INBOX/opm-libro.txt#L4495-L4544)
- **P1718** · `fact` · Object-Oriented paradigm Minimal universal ontology; · [src:S01:L4495-L4544](../../../INBOX/opm-libro.txt#L4495-L4544)
- **P1719** · `constraint` · Object-Process Theorem Standard documentation number of pages 1670=700 (UML Infrastructure) + 700 (UML Superstructure) + 270 (OMG SysML) 180=100 (ISO 19450 main standard) + 80 (appendices) Standardization body OMG ISO Number of diagram kinds 9 1 Top-level concept Block (UML object class) Thing (object or process) Complexity management guiding principle Aspect-based decomposition Detail-level-based decomposition Hierarchical decomposition In some diagram kinds Yes Number of symbols 120 20 Graphic modality Yes Yes Textual modality No2 Yes Built-in physical-informatical distinction No Yes Systemic-environmental distinction Partial (using boundaries) Yes Logical relations (OR, XOR, AND) No Yes Probability modeling No Yes Execution, animated simulation, validation and verification capability Partial (in some tools for some diagram kinds) Yes Tool availability Many, some free Currently one free (OPCAT) from Cloud-based tool under development · [src:S01:L4495-L4544](../../../INBOX/opm-libro.txt#L4495-L4544)

## opm libro · Chapter 12 SysML: Foundations and Diagrams / 12.9.1 OPM Processes as First Class Citizens

- **P1720** · `fact` · Underlying OPM is a philosophy stipulating that in order to faithfully and naturally model, analyze, and design systems in any domain, processes need to be recognized as “first class citizens.” Like objects, OPM processes are considered as bona fide, stand-alone “things” rather than being encapsulated within objects, as the object-oriented (OO) approach advocates. · [src:S01:L4550-L4559](../../../INBOX/opm-libro.txt#L4550-L4559)
- **P1721** · `fact` · The lack of a direct acknowledgement of process as a foundational ontological concept beside object results in a multitude of terms and symbols for process in UML and SysML: use case, activity, action, method, and sequence. · [src:S01:L4550-L4559](../../../INBOX/opm-libro.txt#L4550-L4559)
- **P1722** · `definition` · All of these are processes, but each has some nuance or connotation that is not explicitly defined. · [src:S01:L4550-L4559](../../../INBOX/opm-libro.txt#L4550-L4559)
- **P1723** · `fact` · Objects in OPM are things that persist, while processes are transient things that transform objects. · [src:S01:L4550-L4559](../../../INBOX/opm-libro.txt#L4550-L4559)
- **P1724** · `constraint` · Processes transform objects in one of three ways: (1) affecting their state, (2) generating new objects, or (3) consuming existing objects. · [src:S01:L4550-L4559](../../../INBOX/opm-libro.txt#L4550-L4559)

## opm libro · Chapter 12 SysML: Foundations and Diagrams / 12.9.2 Physical and Informatical Things

- **P1725** · `fact` · Geared for systems engineering from the outset and treating software systems as specializations of general systems, OPM has no inherent “software-oriented” language semantics. · [src:S01:L4561-L4568](../../../INBOX/opm-libro.txt#L4561-L4568)
- **P1726** · `fact` · For example, OPM objects and processes can be informatical, or cybernetic, which may exist in models of both software systems and other general systems, or physical, which is atypical of pure software systems but obviously essential for systems in general. · [src:S01:L4561-L4568](../../../INBOX/opm-libro.txt#L4561-L4568)
- **P1727** · `fact` · Both objects and processes can be physical or informatical. · [src:S01:L4561-L4568](../../../INBOX/opm-libro.txt#L4561-L4568)
- **P1728** · `fact` · Not only can objects and processes be physical or informational, they can also be systemic (part of the system) or environmental (part of the environment interacting with the system). · [src:S01:L4561-L4568](../../../INBOX/opm-libro.txt#L4561-L4568)

## opm libro · Chapter 12 SysML: Foundations and Diagrams / 12.9.3 Model Multiplicity Versus Model Singularity

- **P1729** · `fact` · A major difference between SysML and OPM is the number of views (diagram types) used in each language. · [src:S01:L4570-L4584](../../../INBOX/opm-libro.txt#L4570-L4584)
- **P1730** · `constraint` · While OPM is based on a single diagram type—Object-Process Diagram (OPD), SysML has inherited UML’s model multiplicity (Peleg and Dori 2000), i.e., it presents each one of the system’s aspects in a different view, using a different diagram type. · [src:S01:L4570-L4584](../../../INBOX/opm-libro.txt#L4570-L4584)
- **P1731** · `fact` · SysML includes a subset of UML diagrams, as well as two new types of diagrams for systems engineering: Requirement Diagram and Parametric Diagram. · [src:S01:L4570-L4584](../../../INBOX/opm-libro.txt#L4570-L4584)
- **P1732** · `fact` · A set of inter-related Object-Process Diagrams (OPDs), showing portions of the system at various levels of detail, constitutes the graphical, visual OPM formalism. · [src:S01:L4570-L4584](../../../INBOX/opm-libro.txt#L4570-L4584)
- **P1733** · `fact` · OPD, OPM’s single type of diagram, may be missing some elements that are important for systems engineering, such as the SysML parametric constraints, although these can be treated in OPM as attributes with values that are manipulated by processes that are mathematical operations. · [src:S01:L4570-L4584](../../../INBOX/opm-libro.txt#L4570-L4584)
- **P1734** · `fact` · Both languages support hierarchical representation of the model. · [src:S01:L4570-L4584](../../../INBOX/opm-libro.txt#L4570-L4584)
- **P1735** · `definition` · However, in contrast to SysML, where the model is represented in separate views with partial support of hierarchy, in OPM the entire system model is based on a well-defined hierarchy of OPDs. · [src:S01:L4570-L4584](../../../INBOX/opm-libro.txt#L4570-L4584)
- **P1736** · `fact` · These are but few of several dissimilarities between the languages, which make it interesting to study and compare the differences between them. · [src:S01:L4570-L4584](../../../INBOX/opm-libro.txt#L4570-L4584)

## opm libro · Chapter 12 SysML: Foundations and Diagrams / 12.9.4 Graphics Versus Bimodal Graphics-Text Combination

- **P1737** · `fact` · OPM combines mathematically-grounded formal yet simple graphical language with natural language sentences to express the function, structure, and behavior of systems in an integrated, single model. · [src:S01:L4588-L4600](../../../INBOX/opm-libro.txt#L4588-L4600)
- **P1738** · `fact` · The two semantically equivalent modalities, one graphic and the other textual, jointly express the same OPM model. · [src:S01:L4588-L4600](../../../INBOX/opm-libro.txt#L4588-L4600)
- **P1739** · `fact` · While the visual-graphic and the verbal-textual modalities are semantically equivalent, they appeal to two different information processing channels of the brain, the visual and the lingual. · [src:S01:L4588-L4600](../../../INBOX/opm-libro.txt#L4588-L4600)
- **P1740** · `fact` · OPM is a prime vehicle for carrying out the tasks that are involved in system development. · [src:S01:L4588-L4600](../../../INBOX/opm-libro.txt#L4588-L4600)
- **P1741** · `fact` · It does so in a straightforward, friendly, unambiguous manner. · [src:S01:L4588-L4600](../../../INBOX/opm-libro.txt#L4588-L4600)
- **P1742** · `fact` · One important reason for this is that the design of OPM has not been influenced by what current programming languages can or cannot do, but rather, what makes the most sense when trying to represent and conceptually model systems as best as possible. · [src:S01:L4588-L4600](../../../INBOX/opm-libro.txt#L4588-L4600)
- **P1743** · `fact` · Due to the resulting intuitiveness, OPM is communicable to both technical and non-technical stakeholders of the system being developed, including peers, customers and implementers. · [src:S01:L4588-L4600](../../../INBOX/opm-libro.txt#L4588-L4600)
- **P1744** · `fact` · At the same time, the formality of OPM makes it amenable to computer manipulation for generating, automatically or semi-automatically, large portions of the conceived system, notably program code and database schema. · [src:S01:L4588-L4600](../../../INBOX/opm-libro.txt#L4588-L4600)
