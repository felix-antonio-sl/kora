---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-25
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
      n_propositions: 62
      segmented: true
      segment_role: segment
      segment_index: 25
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-25
---

# Atomic opm-libro-rebuilt - Segmento 25

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `62`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `25/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 10 Things: Objects and Processes / 10.8 Thing Defined

- **P1284** · `fact` · We have seen that objects and processes are two types of tightly coupled and complementary things. · [src:S01:L3419-L3445](../../../INBOX/opm-libro.txt#L3419-L3445)
- **P1285** · `fact` · Objects cannot be transformed (generated, affected or eliminated) without processes, while processes have no meaning without the objects they transform, and often also the objects that enable their occurrence. · [src:S01:L3419-L3445](../../../INBOX/opm-libro.txt#L3419-L3445)
- **P1286** · `requirement` · The extent of this coupling is so intense that if we wish to be able to analyze and design systems in any domain as intuitively and naturally as possible, we must consider objects and processes concurrently. · [src:S01:L3419-L3445](../../../INBOX/opm-libro.txt#L3419-L3445)
- **P1287** · `fact` · Objects exist as relatively persistent, static things, while processes occur as transient, dynamic things. · [src:S01:L3419-L3445](../../../INBOX/opm-libro.txt#L3419-L3445)
- **P1288** · `requirement` · The extent to which objects and processes are interwoven is even lager; we must be able to specify what state an object was at before the process affected it, which objects were consumed, and which were generated. · [src:S01:L3419-L3445](../../../INBOX/opm-libro.txt#L3419-L3445)
- **P1289** · `fact` · At the same time, we need to be able to show how parts, features and specializations (discussed later) of these objects play role in subprocesses of the higher-level process. · [src:S01:L3419-L3445](../../../INBOX/opm-libro.txt#L3419-L3445)
- **P1290** · `requirement` · As we shall see, objects and processes have much in common in terms of being specified through structural relations such as aggregation, generalization, and characterization. · [src:S01:L3419-L3445](../../../INBOX/opm-libro.txt#L3419-L3445)
- **P1291** · `fact` · The need to talk about these two concepts in a generalized way, without repeating “object or process” over and over again, necessitates the advent of a yet more abstract term. · [src:S01:L3419-L3445](../../../INBOX/opm-libro.txt#L3419-L3445)
- **P1292** · `fact` · We call this simply a “thing.” Thing is a generalization of object and process. · [src:S01:L3419-L3445](../../../INBOX/opm-libro.txt#L3419-L3445)
- **P1293** · `fact` · The concept of “thing” enables us to think and express ourselves in terms of this abstraction and refer to it without the need to reiterate the words “object or process”. · [src:S01:L3419-L3445](../../../INBOX/opm-libro.txt#L3419-L3445)
- **P1294** · `constraint` · Based on the ontology of Bunge (1987, 1989), Wand and Weber (1989, 1993) have used the term thing as a synonym to what we refer to as object. · [src:S01:L3419-L3445](../../../INBOX/opm-libro.txt#L3419-L3445)
- **P1295** · `fact` · Their first premise is that the world is made of things that have properties. · [src:S01:L3419-L3445](../../../INBOX/opm-libro.txt#L3419-L3445)
- **P1296** · `fact` · According to this definition, thing seems to be synonymous with object. · [src:S01:L3419-L3445](../../../INBOX/opm-libro.txt#L3419-L3445)
- **P1297** · `fact` · However, during the last two decades, the term object has become deeply rooted, at least in the software engineering community. · [src:S01:L3419-L3445](../../../INBOX/opm-libro.txt#L3419-L3445)
- **P1298** · `fact` · In SysML and UML, object has been replaced by the terms block and class, respectively. · [src:S01:L3419-L3445](../../../INBOX/opm-libro.txt#L3419-L3445)
- **P1299** · `fact` · Interestingly, the emergence of the term “Internet of Things” (IoT; · [src:S01:L3419-L3445](../../../INBOX/opm-libro.txt#L3419-L3445)
- **P1300** · `constraint` · Weber and Weber 2010) is in line with the notion of thing as a generalization of object and process since IoT is about processes taking place among physical interconnected objects. · [src:S01:L3419-L3445](../../../INBOX/opm-libro.txt#L3419-L3445)

## opm libro · Chapter 10 Things: Objects and Processes / 10.9 Properties of OPM Things

- **P1301** · `fact` · A property is an attribute at the metamodel level. · [src:S01:L3447-L3467](../../../INBOX/opm-libro.txt#L3447-L3467)
- **P1302** · `fact` · Property can be thought of as a meta-attribute—an attribute of an element in a metamodel of OPM. · [src:S01:L3447-L3467](../../../INBOX/opm-libro.txt#L3447-L3467)
- **P1303** · `fact` · Property is an attribute of an OPM model element. · [src:S01:L3447-L3467](../../../INBOX/opm-libro.txt#L3447-L3467)
- **P1304** · `fact` · Unlike “regular” attribute, whose values can change during the execution of an OPM model, a property value of any element in an OPM model is fixed. · [src:S01:L3447-L3467](../../../INBOX/opm-libro.txt#L3447-L3467)
- **P1305** · `fact` · We will see an example at the end of this section. · [src:S01:L3447-L3467](../../../INBOX/opm-libro.txt#L3447-L3467)
- **P1306** · `fact` · All OPM things have the following three properties: Perseverance, which pertains to the thing’s persistence and denotes whether the thing is static (persistent), i.e. an Object, or dynamic (transient), i.e. a Process. · [src:S01:L3447-L3467](../../../INBOX/opm-libro.txt#L3447-L3467)
- **P1307** · `fact` · Boundary examples of static, persistent processes and dynamic, transient objects exist, as discussed later in this chapter. · [src:S01:L3447-L3467](../../../INBOX/opm-libro.txt#L3447-L3467)
- **P1308** · `fact` · Based on the value of Perseverance, this property of Thing discriminates between an Object and a Process. · [src:S01:L3447-L3467](../../../INBOX/opm-libro.txt#L3447-L3467)
- **P1309** · `fact` · At the model level we call such attributes discriminating attributes, as discussed in a later chapter. · [src:S01:L3447-L3467](../../../INBOX/opm-libro.txt#L3447-L3467)
- **P1310** · `fact` · Essence, which pertains to the thing’s nature and denotes whether the thing is physical or informatical. · [src:S01:L3447-L3467](../../../INBOX/opm-libro.txt#L3447-L3467)
- **P1311** · `fact` · Affiliation, which pertains to the thing’s scope and denotes whether the thing is systemic, i.e., part of the system, or environmental, i.e., part of the system’s environment. Graphically, as shown in Fig. · [src:S01:L3447-L3467](../../../INBOX/opm-libro.txt#L3447-L3467)
- **P1312** · `constraint` · 10.8, shading effects denote physical OPM things and dashed lines denote environmental OPM things. · [src:S01:L3447-L3467](../../../INBOX/opm-libro.txt#L3447-L3467)
- **P1313** · `constraint` · All eight Perseverance-Essence-Affiliation property combinations of an OPM thing shown in Fig. 10.8 may occur. The lower portion of Fig. · [src:S01:L3447-L3467](../../../INBOX/opm-libro.txt#L3447-L3467)
- **P1314** · `constraint` · 10.8 expresses, from left to right and top to bottom, the OPL sentences corresponding to the graphical elements. · [src:S01:L3447-L3467](../../../INBOX/opm-libro.txt#L3447-L3467)
- **P1315** · `fact` · We noted that a property value of any element in an OPM model is fixed. · [src:S01:L3447-L3467](../../../INBOX/opm-libro.txt#L3447-L3467)
- **P1316** · `fact` · Indeed looking at the example of Perseverance, a property of an OPM Thing, if the value of a certain Thing in an OPM model is set as static (i.e., the Thing is an Object), then this value is fixed and the Object cannot become a Process. · [src:S01:L3447-L3467](../../../INBOX/opm-libro.txt#L3447-L3467)

## opm libro · Chapter 10 Things: Objects and Processes / 10.9.1 Default Values of Thing Generic Properties

- **P1317** · `fact` · The Affiliation property of thing is by default systemic. · [src:S01:L3472-L3496](../../../INBOX/opm-libro.txt#L3472-L3496)
- **P1318** · `fact` · With respect to Essence, we note that the majority of things in non-trivial systems tends to have the same property value: either most of the things in the system are physical or most of them are informatical. · [src:S01:L3472-L3496](../../../INBOX/opm-libro.txt#L3472-L3496)
- **P1319** · `fact` · For example, Data processing systems are informatical, although they have physical components. · [src:S01:L3472-L3496](../../../INBOX/opm-libro.txt#L3472-L3496)
- **P1320** · `fact` · Transportation systems, such as a railway system or an aviation system, are physical, although they have informatical components. · [src:S01:L3472-L3496](../../../INBOX/opm-libro.txt#L3472-L3496)
- **P1321** · `fact` · A system’s primary essence is the Essence value of the majority of the things in the system. · [src:S01:L3472-L3496](../../../INBOX/opm-libro.txt#L3472-L3496)
- **P1322** · `fact` · The default essence value of a thing is the primary essence of the system. · [src:S01:L3472-L3496](../../../INBOX/opm-libro.txt#L3472-L3496)
- **P1323** · `fact` · The motivation, based on experience, for defining the primary essence is to save the modeler the need to mark the vast majority of the things in the system as either informatical or physical. · [src:S01:L3472-L3496](../../../INBOX/opm-libro.txt#L3472-L3496)
- **P1324** · `fact` · A supporting tool should therefore provide an option for the modeler to specify a system’s primary essence as a means to reduce the amount of things for which the modeler has to specify their essence. · [src:S01:L3472-L3496](../../../INBOX/opm-libro.txt#L3472-L3496)
- **P1325** · `fact` · The OPL paragraph corresponding to an OPD should not include an OPL sentence to indicate the Essence or Affiliation value of a thing if it is the default, unless the thing is isolated—it has not yet been connected to any other thing during the course of the modeling process. · [src:S01:L3472-L3496](../../../INBOX/opm-libro.txt#L3472-L3496)
- **P1326** · `fact` · The reason for this is the need to avoid violating the graphics-text OPM principle. · [src:S01:L3472-L3496](../../../INBOX/opm-libro.txt#L3472-L3496)
- **P1327** · `constraint` · Suppose the default essence of the OPDs in Fig. 10.9 is physical. · [src:S01:L3472-L3496](../../../INBOX/opm-libro.txt#L3472-L3496)
- **P1328** · `requirement` · Upon drawing the physical object Car and prior to linking it to anything, the OPL sentence “Car is physical” shall appear, as shown in the OPD on the left, otherwise there would be a thing (Car) depicted in the OPD that has no mention in the OPL, violating the graphics-text OPM principle. · [src:S01:L3472-L3496](../../../INBOX/opm-libro.txt#L3472-L3496)
- **P1329** · `requirement` · However, as soon as the isolated thing becomes linked to another thing, as shown in the OPD on the right, the OPL sentence dedicated to specifying the thing’s default Essence or Affiliation shall be removed. · [src:S01:L3472-L3496](../../../INBOX/opm-libro.txt#L3472-L3496)
- **P1330** · `fact` · ABS, the first sentence is removed from the OPL sentence · [src:S01:L3472-L3496](../../../INBOX/opm-libro.txt#L3472-L3496)

## opm libro · Chapter 10 Things: Objects and Processes / 10.10 Boundary Cases of Things

- **P1331** · `fact` · While objects are persistent and processes are transient, boundary case of state-preserving (persistent) processes and transient objects, exist. These are discussed in this section. · [src:S01:L3498-L3499](../../../INBOX/opm-libro.txt#L3498-L3499)

## opm libro · Chapter 10 Things: Objects and Processes / 10.10.1 State-Preserving Processes

- **P1332** · `definition` · We have defined a process as a thing that transforms an object. · [src:S01:L3501-L3524](../../../INBOX/opm-libro.txt#L3501-L3524)
- **P1333** · `fact` · There are cases in which the absence of a process, rather than its occurrence, causes a change in the state of the object. · [src:S01:L3501-L3524](../../../INBOX/opm-libro.txt#L3501-L3524)
- **P1334** · `fact` · One example is supporting: Any object on Planet Earth (or on any other planet for that matter) is maintained in its vertical position by a Supporting process that prevents it from freely falling. · [src:S01:L3501-L3524](../../../INBOX/opm-libro.txt#L3501-L3524)
- **P1335** · `fact` · There is a whole family of such state-preserving processes that have a static connotation as they act to maintain the state of an object rather than change it. · [src:S01:L3501-L3524](../../../INBOX/opm-libro.txt#L3501-L3524)
- **P1336** · `fact` · A state-preserving process is a process that acts to maintain a steady state or status quo of an object rather than to change it. · [src:S01:L3501-L3524](../../../INBOX/opm-libro.txt#L3501-L3524)
- **P1337** · `fact` · The process of existing is the most prominent example, describing a situation of an object being “out there” without specifying any change in that object. · [src:S01:L3501-L3524](../../../INBOX/opm-libro.txt#L3501-L3524)
- **P1338** · `fact` · For biological objects, existing entails maintenance of the necessary life processes, so they are definitely not static. · [src:S01:L3501-L3524](../../../INBOX/opm-libro.txt#L3501-L3524)
- **P1339** · `fact` · Non-biological systems such as the solar system or the global air traffic control system also exist while constantly changing. · [src:S01:L3501-L3524](../../../INBOX/opm-libro.txt#L3501-L3524)
- **P1340** · `fact` · Members of this state-preserving process family include such processes as Supporting, Holding, Maintaining, Keeping, Staying, Waiting, Prolonging, Delaying, Occupying, Persisting, Including, Containing, Continuing, Enclosing, Fastening, Connecting, Postponing, Dragging, Storing, Owning, Restraining, Drawing, Attracting, and Remaining. · [src:S01:L3501-L3524](../../../INBOX/opm-libro.txt#L3501-L3524)
- **P1341** · `fact` · Rather than induce any real change, the semantics of these verbs is leaving the current state of the object as is, in its status quo, for some more time. · [src:S01:L3501-L3524](../../../INBOX/opm-libro.txt#L3501-L3524)
- **P1342** · `fact` · Each one of these processes can be considered as a change-preventing process—a process that works against some “force” which would otherwise change the operand—the object being operated on. · [src:S01:L3501-L3524](../../../INBOX/opm-libro.txt#L3501-L3524)
- **P1343** · `fact` · For example, Supporting of a Laptop can be rephrased as Fall Preventing, Keeping of a Coin can be rephrased as its Loss Preventing, and Holding of a Hostage can be rephrased as Escape Preventing of that Hostage. · [src:S01:L3501-L3524](../../../INBOX/opm-libro.txt#L3501-L3524)
- **P1344** · `fact` · Due to their nature as state-preserving, these “pseudo-processes” might rather be modeled using tagged structural relations between two objects. · [src:S01:L3501-L3524](../../../INBOX/opm-libro.txt#L3501-L3524)
- **P1345** · `fact` · We discuss this in the context of structural relations. · [src:S01:L3501-L3524](../../../INBOX/opm-libro.txt#L3501-L3524)
