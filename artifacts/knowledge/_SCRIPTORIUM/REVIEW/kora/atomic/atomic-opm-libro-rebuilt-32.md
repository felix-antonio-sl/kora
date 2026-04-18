---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-32
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
      n_propositions: 49
      segmented: true
      segment_role: segment
      segment_index: 32
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-32
---

# Atomic opm-libro-rebuilt - Segmento 32

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `49`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `32/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 12 SysML: Foundations and Diagrams / 12.7 Requirements Diagram

- **P1643** · `fact` · The requirement diagram and the parametric diagram are two totally new kinds of diagrams that SysML has added to UML and are not part of UML. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1644** · `fact` · Requirement diagrams bridge typical requirements management tools and the system model. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1645** · `fact` · As the official OMG SysML Site indicates, SysML requirements diagram is a graphical construct for representing text-based requirements and relate them to other model elements. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1646** · `fact` · The requirements diagram captures requirement hierarchies and derivations. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1647** · `fact` · It can be used to verify relationships between requirements and their implementation by allowing the modeler to relate a requirement to a model element that satisfies or verifies the requirement. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1648** · `constraint` · The main symbols of a SysML requirements diagram are presented in Fig. 12.10. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1649** · `fact` · A requirement is depicted as a block with the reserved word «requirement» at its top. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1650** · `constraint` · In the SysML 1.3 document this is referred to as a stereotype of UML class that is subject to a set of constraints. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1651** · `fact` · The containment relationship, depicted as a crossed circle (like the one under the Parent in Fig. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1652** · `constraint` · 12.10) denotes that the requirement attached to the circle contains the ones linked to it. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1653** · `fact` · This provides for creating requirement hierarchies. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1654** · `constraint` · Three additional main dependency relations between blocks, denoted by dashed arrows, are shown in Fig. 12.10. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1655** · `fact` · The stereotype «copy» denotes that the “Slave” is a copy of the “Master” (to which the arrow points). · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1656** · `fact` · The stereotype «deriveReqt» denotes that the “Client” requirement is derived from the “Supplier” (to which the arrow points). · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1657** · `fact` · The stereotype «satisfy» denotes that the block “namedElement” is a system component that satisfies the requirement to which the arrow points. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1658** · `fact` · Three other dependencies of similar nature are «verify», «refine», and «trace». · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1659** · `fact` · The «verify» dependency is between a requirement and a block that provides a way of verifying it. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1660** · `fact` · This can be a block having the stereotype «testCase». · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1661** · `fact` · The «refine» dependency denotes that some elaborate requirement refines a more general requirement, e.g., a client’s requirement. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1662** · `fact` · The «trace» dependency denotes that some block provide a way to trace a requirement. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1663** · `fact` · The «trace» dependency provides a way to keep track of where requirements are fulfilled in the system, as it is often the case that requirements are difficult to trace or it is not clear why some component was included in the model. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1664** · `fact` · A standard requirement includes properties to specify its unique identifier and text requirement. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1665** · `fact` · Additional properties such as verification status, can be specified by the user. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1666** · `fact` · Indeed, requirements diagrams are depicted in a large variety of forms and styles. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1667** · `fact` · The diagram in the top left is titled req TV Remote Control. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1668** · `fact` · It contains four requirements, the main of which is also called TV Remote Control. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1669** · `fact` · The three others, called Weight, Color, and Eco-Friendliness, are “children”—lower-level requirements that are subordinates of the parent requirement TV Remote Control. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1670** · `constraint` · This is designated by the lines with the crossed circles at their ends, in accord with the standard specification in Fig. 12.10. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1671** · `fact` · In addition to the text and ID attributes, each requirement here has the attributes source, kind, verifyMethod, risk, and status. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1672** · `fact` · The diagram in the top right is titled Requirement Diagram Top-Level User Requirements. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1673** · `fact` · The standard specifies that req be used to designate a Requirement Diagram. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1674** · `fact` · The use of the black diamond, which is a symbol from block definition diagram (bdd) is another non-standard application. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1675** · `fact` · The containment symbol should be used instead. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1676** · `fact` · The diagram in the bottom left, titled req Detection Performance, shows the use of all the six dependency kinds discussed above. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1677** · `fact` · For example, «testCase» Low SNR Target Without Interference «verify» «requirement» Sensor2 Detection Performance. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1678** · `fact` · Another example is «block» Signal Processor «satisfy» «requirement» Sensor2 Detection Performance. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1679** · `fact` · None of the requirements in this diagram has the feature compartment with the minimal set of features—text and ID, but the standard (Sect. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1680** · `constraint` · 16.3.1.2) does allow to elide (leave out) this compartment. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1681** · `fact` · Interestingly, Scan Environment, which is a use case, is at the origin of the «refine» dependency. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1682** · `constraint` · This does not seem to be allowed by the standard, since according to OMG SysML v1.3 Sect. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1683** · `constraint` · 16.3.1.1 (p.144) “The Requirement Diagram can only display requirements, packages, other classifiers, test cases, and rationale.” However, this link between use cases and requirements can be useful. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1684** · `constraint` · Trying to defend the legality of mixing symbols from various diagrams, we find that the informative Annex A—Diagrams of SysML v1.3 Standard (p. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1685** · `constraint` · 168) states: “Although the taxonomy provides a logical organization for the various major kinds of diagrams, it does not preclude the careful mixing of different kinds of diagram types, as one might do when one combines structural and behavioral elements (e.g., showing a state machine nested inside a compartment of a block). · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1686** · `fact` · However, it is critical that the types of diagram elements that can appear on a particular diagram kind be constrained and well-specified. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1687** · `fact` · The diagram elements tables in each clause describe what symbols can appear in the diagram, but do not specify the different combinations of symbols that can be used.” This paragraph essentially grants SysML modelers complete freedom to mix and match any symbol from any SysML diagram kind with any other symbol. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1688** · `fact` · All one has to do is “careful mixing” and ensuring that “the types of diagram elements that can appear on a particular diagram kind be constrained and well-specified.” However, what “constrained and well-specified” means is itself not specified, leaving it open to any interpretation of the modeler. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1689** · `constraint` · Finally, the diagram in the bottom right, titled CLD Dispenser Requirements, shows in the top compartment of each requirement, in addition to the name (e.g., Fuel Type Delivery) also the requirement’s priority (e.g., {Requirement Type=Non-Functional}) and type (e.g., {Type=1}). · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1690** · `fact` · The feature compartment contains relatively elaborate text (e.g., “Only one type of fuel can be delivered”), but it does not contain an ID. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
- **P1691** · `fact` · Three blocks (Valve, Dispenser Controller, and FT) satisfy the Dispenser Fuel Type requirement, which is derived from another, more comprehensive requirement. · [src:S01:L4367-L4443](../../../INBOX/opm-libro.txt#L4367-L4443)
