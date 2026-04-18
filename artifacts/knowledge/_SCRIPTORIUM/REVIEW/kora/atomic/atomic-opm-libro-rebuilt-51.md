---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-51
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
      n_propositions: 44
      segmented: true
      segment_role: segment
      segment_index: 51
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-51
---

# Atomic opm-libro-rebuilt - Segmento 51

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `44`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `51/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 17 Aggregation-Participation / 17.4 Aggregate Naming

- **P2628** · `fact` · Frequently during the analysis, we encounter situations in which we need to name an aggregate, which has no single word in natural language. · [src:S01:L6836-L6858](../../../INBOX/opm-libro.txt#L6836-L6858)
- **P2629** · `fact` · To illustrate the point of aggregate naming and the importance of appropriate phrase generation, consider a transportation, civil, and systems engineering development team, whose assignment is to improve the traffic in a city. · [src:S01:L6836-L6858](../../../INBOX/opm-libro.txt#L6836-L6858)
- **P2630** · `fact` · After some thought and discussion, the team agrees that an essential object in the system is the composition of a car and the person that drives it in the city streets. · [src:S01:L6836-L6858](../../../INBOX/opm-libro.txt#L6836-L6858)
- **P2631** · `fact` · This object is much more central to the system than a car alone or a driver alone. · [src:S01:L6836-L6858](../../../INBOX/opm-libro.txt#L6836-L6858)
- **P2632** · `fact` · The role a car without a driver plays is restricted to parking issues, while the driver without the car should be considered a pedestrian. · [src:S01:L6836-L6858](../../../INBOX/opm-libro.txt#L6836-L6858)
- **P2633** · `fact` · Nonetheless, having agreed that the car along with its driver is a major object that needs to be accounted for in the system, our team still lacks an elegant way of referring to it. · [src:S01:L6836-L6858](../../../INBOX/opm-libro.txt#L6836-L6858)
- **P2634** · `constraint` · Since there is no single word in English (and most likely in any other natural language) for this object, the team has come up with the name Car-Driver Complex, as illustrated in Fig. 17.3. · [src:S01:L6836-L6858](../../../INBOX/opm-libro.txt#L6836-L6858)
- **P2635** · `requirement` · As we will see, these situations are not unique to aggregates; they are also encountered in a variety of other circumstances, such as naming an attribute when only the names of its values are explicit.2 In cases like these, we must exercise our creativity to generate an appropriate phrase that best captures the essence of what we wish to express. · [src:S01:L6836-L6858](../../../INBOX/opm-libro.txt#L6836-L6858)
- **P2636** · `fact` · The capability of inventing meaningful names, or generating expressive phrases, is a very important component of the analysis process. · [src:S01:L6836-L6858](../../../INBOX/opm-libro.txt#L6836-L6858)
- **P2637** · `fact` · It provides us with the power to abstract into a whole a collection of things that would otherwise be very difficult to think about and relate to as a unity. · [src:S01:L6836-L6858](../../../INBOX/opm-libro.txt#L6836-L6858)
- **P2638** · `fact` · Recall that indeed the first OPM principle—the Function-as-a-Seed OPM Principle—calls for starting the process of modeling a system by defining, naming, and depicting the function of the system. · [src:S01:L6836-L6858](../../../INBOX/opm-libro.txt#L6836-L6858)
- **P2639** · `requirement` · The name of the function shall express what the system is designed to do, and what value its beneficiaries will gain from using it. · [src:S01:L6836-L6858](../../../INBOX/opm-libro.txt#L6836-L6858)

## opm libro · Chapter 17 Aggregation-Participation / 17.5 Composite and Shared Aggregation in UML and SysML

- **P2640** · `constraint` · SysML adopted from UML 2 all the definitions related to class diagram (and several other diagram kinds) “as is.” SysML block diagram inherits the same semantics as UML 2 class diagram. · [src:S01:L6861-L6914](../../../INBOX/opm-libro.txt#L6861-L6914)
- **P2641** · `constraint` · Hence, in UML 2 and SysML class diagrams there are two types of aggregation: composite aggregation and shared aggregation (Object Management Group 2010, p. 39). · [src:S01:L6861-L6914](../../../INBOX/opm-libro.txt#L6861-L6914)
- **P2642** · `fact` · Composite aggregation, depicted as a black diamond next to the whole end of the link, (see Fig. · [src:S01:L6861-L6914](../../../INBOX/opm-libro.txt#L6861-L6914)
- **P2643** · `constraint` · 17.4) “indicates that the composite object has responsibility for the existence and storage of the composed objects (parts).” Composite aggregation, also referred to as strong aggregation, or the composition relationship, or standard composite aggregation, or non-shared association, is considered a “strong” form of containment or aggregation: A part can belong to just one aggregate, and if the aggregate is consumed, all its parts are consumed along with it. · [src:S01:L6861-L6914](../../../INBOX/opm-libro.txt#L6861-L6914)
- **P2644** · `definition` · Originally defined for UML, responsibility and storage in the composite aggregation definition are software-related concepts. · [src:S01:L6861-L6914](../../../INBOX/opm-libro.txt#L6861-L6914)
- **P2645** · `constraint` · SysML, which is supposed to accommodate systems of any kind, not just software, has inherited this definition, as is the case with many other definitions. +scrollbar +title +body 1 Slider Header Panel In OPM the distinction between composite and shared aggregation is not necessary, since one can model exactly what part or parts are consumed when the whole is consumed and what parts remain, as the OPM model in Fig. · [src:S01:L6861-L6914](../../../INBOX/opm-libro.txt#L6861-L6914)
- **P2646** · `constraint` · 17.5 demonstrates: After Crashing, the whole Car and its Chassis are gone, but the Powertrain remains (and can be reused). · [src:S01:L6861-L6914](../../../INBOX/opm-libro.txt#L6861-L6914)

## opm libro · Chapter 17 Aggregation-Participation / 17.6 Expressing Parts Order

- **P2647** · `definition` · Sometimes, the order of the parts that comprise the whole is significant. · [src:S01:L6919-L6941](../../../INBOX/opm-libro.txt#L6919-L6941)
- **P2648** · `fact` · Sets are abstract collections of things that consist of elements or members. · [src:S01:L6919-L6941](../../../INBOX/opm-libro.txt#L6919-L6941)
- **P2649** · `fact` · A set may therefore be thought of as an aggregate (whole) and its elements—as parts. Each element in the set is unique. · [src:S01:L6919-L6941](../../../INBOX/opm-libro.txt#L6919-L6941)
- **P2650** · `fact` · Since aggregation-participation is a structural relation, everything that applies to a fork is true for aggregation-participation, including the way orderability is indicated. · [src:S01:L6919-L6941](../../../INBOX/opm-libro.txt#L6919-L6941)
- **P2651** · `fact` · Being a fork, the Aggregation-Participation relation exhibits the Boolean Orderability property, which denotes whether or not the set of parts is ordered. · [src:S01:L6919-L6941](../../../INBOX/opm-libro.txt#L6919-L6941)
- **P2652** · `fact` · The two values of Orderability are ordered and unordered, with the default value being unordered. · [src:S01:L6919-L6941](../../../INBOX/opm-libro.txt#L6919-L6941)
- **P2653** · `fact` · Let us again consider the RDF triple case (Klyne et al. · [src:S01:L6919-L6941](../../../INBOX/opm-libro.txt#L6919-L6941)
- **P2654** · `constraint` · 2004): An RDF triple is conventionally written in the order subject, predicate, object. · [src:S01:L6919-L6941](../../../INBOX/opm-libro.txt#L6919-L6941)
- **P2655** · `constraint` · RDF Triple from left to right (in the OPD on the left) or top-down (in the OPD on the right) We model graphically the fact that the three elements of an RDF triple are ordered by adding the label ordered next to the black triangle symbolizing the aggregation-participation relation, as shown in the OPD in Fig. 17.6. · [src:S01:L6919-L6941](../../../INBOX/opm-libro.txt#L6919-L6941)
- **P2656** · `constraint` · The parts can be ordered with no sematic difference either from left to right, as the OPD on 230 Aggregation-Participation the left shows, or top-down, as the OPD on the right shows. · [src:S01:L6919-L6941](../../../INBOX/opm-libro.txt#L6919-L6941)
- **P2657** · `fact` · The corresponding OPL phrase is “in that sequence”, which follows a comma after the name of the last part in the ordered list. The OPD in Fig. · [src:S01:L6919-L6941](../../../INBOX/opm-libro.txt#L6919-L6941)
- **P2658** · `constraint` · 17.7 is an example of an aggregation hierarchy, which specifies the reading order of a scientific paper, i.e., the order in which the parts of the paper should be read, with participation constraints, which are discussed in Chap. 15. · [src:S01:L6919-L6941](../../../INBOX/opm-libro.txt#L6919-L6941)
- **P2659** · `constraint` · When dealing with processes, orderability is intimately related to the top-to-bottom timeline within an in-zoomed process, which dictates the process execution order. We elaborate on this in Chap. 21 while discussing complexity management. · [src:S01:L6919-L6941](../../../INBOX/opm-libro.txt#L6919-L6941)

## opm libro · Chapter 17 Aggregation-Participation / 17.7 Aggregation and Tagged Structural Relations

- **P2660** · `fact` · In the next example, we illustrate an OPM model that combines aggregation-participation with tagged structural relations. · [src:S01:L6943-L6949](../../../INBOX/opm-libro.txt#L6943-L6949)
- **P2661** · `constraint` · Consider the sentence extracted from the RDF Primer (Manola and Miller 2003): RDF models statements as nodes and arcs in a graph. · [src:S01:L6943-L6949](../../../INBOX/opm-libro.txt#L6943-L6949)
- **P2662** · `fact` · In order to model this sentence in OPM, using our prior knowledge about graphs and assuming that a graph has at least two nodes and one arc (which is the case with RDF graphs), we break the sentence above into the following three simpler, more explicit sentences: · [src:S01:L6943-L6949](../../../INBOX/opm-libro.txt#L6943-L6949)
- **P2663** · `fact` · A graph consists of at least two nodes and one arc. · [src:S01:L6952](../../../INBOX/opm-libro.txt#L6952)
- **P2664** · `fact` · RDF graph is a graph. · [src:S01:L6953](../../../INBOX/opm-libro.txt#L6953)
- **P2665** · `constraint` · An RDF graph models at least one RDF statement. Sentence (1) above is modeled in Fig. 17.8. As in the previous example, the black triangle denotes aggregation, where the object Graph is the whole, while Node and Arc are the parts. The plus (+) symbol above Arc denotes the “at least one” (+) participation constraint, while the “2..” symbol above Node denotes the participation constraint “2 to many”. The fact that has been added in the second OPL sentence is that an RDF Graph is a (specialization of) Graph. As such, it inherits the structure of Graph. To express the fact that an RDF Graph models at least one RDF Statement, a unidirectional tagged structural relation is used, and the tag reads “models”. We ended up with two similar OPL sentences, obtained from two W3C proposed recommendations: “RDF Statement consists of Subject, Predicate, and Object.” (Manola and Miller 2003), and “RDF Triple consists of Subject, Predicate, and Object.” (Klyne et al. 2004) Under the assumption that if two things consist of exactly the same set of parts, or components, they are equivalent (if not the same), one can deduce that RDF Triple and RDF Statement are equivalent. This statement is expressed in the OPM model depicted in Fig. 17.9 by the (vertical) null tag bidirectional structural link between these two objects, which combines model facts from Figs. 17.6 and 17.8. This OPD also expresses that Subject and Object in an RDF Graph are Nodes in a general Graph, and that Predicate in an RDF Graph is an Arc in a Graph. Another example for the use of the null tag bidirectional structural relation is when we model the sentence from Sect. 6.1 of (Klyne et al. 2004) The predicate is also known as the property of the triple. This is expressed in the OPD of Fig. 17.9, where Property is linked to Predicate with a null tag bidirectional structural link to indicate that they are equivalent, assuming that the null tag default is “equivalent”. This translates to the OPL sentence “RDF Triple and RDF Statement are equivalent.” 232 Aggregation-Participation · [src:S01:L6954-L6978](../../../INBOX/opm-libro.txt#L6954-L6978)

## opm libro · Chapter 17 Aggregation-Participation / 17.8 Non-Comprehensive Aggregation

- **P2666** · `fact` · Being a specialization of fork, aggregation inherits the Boolean Comprehensiveness property just as it inherits the Boolean Orderability property. · [src:S01:L6981-L6991](../../../INBOX/opm-libro.txt#L6981-L6991)
- **P2667** · `fact` · The default aggregation Comprehensiveness value is comprehensive: we assume that if nothing is indicated, then all the parts are specified in the model. · [src:S01:L6981-L6991](../../../INBOX/opm-libro.txt#L6981-L6991)
- **P2668** · `constraint` · If we wish to denote that the aggregation is non-comprehensive, we add the non-comprehensiveness symbol— a short horizontal bar below the aggregation black triangle symbol, as shown in Figs. 17.10 and 17.11. · [src:S01:L6981-L6991](../../../INBOX/opm-libro.txt#L6981-L6991)
- **P2669** · `constraint` · The corresponding OPL phrase is “and at least one other part”, used in the last OPL sentence in Fig. 17.10. · [src:S01:L6981-L6991](../../../INBOX/opm-libro.txt#L6981-L6991)
- **P2670** · `fact` · If an aggregation symbol is both ordered and non-comprehensive, the OPL phrase for non- comprehensiveness precedes that for the orderability. For example, if in Fig. · [src:S01:L6981-L6991](../../../INBOX/opm-libro.txt#L6981-L6991)
- **P2671** · `constraint` · 17.10 the aggregation symbol attached to Body, which is non-comprehensive, would also be ordered, the resulting OPL sentence would be: Body consists of at least one Section, optional Figures, and at least one other part, in that sequence. · [src:S01:L6981-L6991](../../../INBOX/opm-libro.txt#L6981-L6991)
