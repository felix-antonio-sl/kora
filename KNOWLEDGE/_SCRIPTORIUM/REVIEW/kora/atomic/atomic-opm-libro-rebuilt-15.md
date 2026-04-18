---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-15
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
      n_propositions: 55
      segmented: true
      segment_role: segment
      segment_index: 15
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-15
---

# Atomic opm-libro-rebuilt - Segmento 15

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `55`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `15/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 9 Conceptual Modeling: Purpose and Context / 9.2.4 The Object-Process Assertion: The Basis for OPM

- **P0735** · `fact` · Combining the Object-Process Corollary with the Model Complexity Assertion, we get the following Object-Process Assertion. · [src:S01:L2306-L2320](../../../INBOX/opm-libro.txt#L2306-L2320)
- **P0736** · `fact` · The Object-Process Assertion Using stateful objects, processes, and relations among them, along with refinement mechanisms of in-zooming and unfolding, one can conceptually model systems in any domain and at any level of complexity. · [src:S01:L2306-L2320](../../../INBOX/opm-libro.txt#L2306-L2320)
- **P0737** · `requirement` · Combining the Object-Process Theorem, according to which stateful objects, processes, and relations among them constitute a minimal universal ontology, with the minimal ontology principle, the optimal conceptual modeling language must have just two types of concepts—stateful objects and processes, collectively called things—along with relations among them. · [src:S01:L2306-L2320](../../../INBOX/opm-libro.txt#L2306-L2320)
- **P0738** · `fact` · Collectively, things and relations are the only two OPM’s elements. · [src:S01:L2306-L2320](../../../INBOX/opm-libro.txt#L2306-L2320)
- **P0739** · `requirement` · Things in the same system must be related, either directly or indirectly. · [src:S01:L2306-L2320](../../../INBOX/opm-libro.txt#L2306-L2320)
- **P0740** · `fact` · Graphically, these relation are expressed by links. · [src:S01:L2306-L2320](../../../INBOX/opm-libro.txt#L2306-L2320)
- **P0741** · `fact` · Things and links are collectively called elements, and so element is the top-level OPM concept. An OPM element is a thing or a link. · [src:S01:L2306-L2320](../../../INBOX/opm-libro.txt#L2306-L2320)

## opm libro · Chapter 9 Conceptual Modeling: Purpose and Context / 9.2.5 Why Not Just One Kind of Thing? A Graph with Nodes and Links?

- **P0742** · `fact` · One may argue that an even more minimalistic representation than three kinds of elements—objects, processes, and relations among them—could be just two: things and relations among them. · [src:S01:L2322-L2355](../../../INBOX/opm-libro.txt#L2322-L2355)
- **P0743** · `fact` · Indeed, quite a number of knowledge representation frameworks have come up with this idea of representing knowledge via a graph with nodes of just one kind and links connecting them. · [src:S01:L2322-L2355](../../../INBOX/opm-libro.txt#L2322-L2355)
- **P0744** · `constraint` · Some of these frameworks, which vary in their level of formality, are surveyed in Dori (2004). · [src:S01:L2322-L2355](../../../INBOX/opm-libro.txt#L2322-L2355)
- **P0745** · `constraint` · These include the concept maps (Arnheim 1969), entity-relationship diagram (Chen 1976), semantic networks (Lehman 1999), conceptual graphs (Chein and Mugnier 1992), and systemigrams (Blair et al. 2007). · [src:S01:L2322-L2355](../../../INBOX/opm-libro.txt#L2322-L2355)
- **P0746** · `requirement` · Looking at examples of graphs expressed in these approaches, one quickly reveals that since there is only one kind of node, there is no distinction between an object and a process, so the ability to distinguish between structure and behavior—the two distinct facets that must be represented in any model—is severely crippled, or even nonexistent. · [src:S01:L2322-L2355](../../../INBOX/opm-libro.txt#L2322-L2355)
- **P0747** · `fact` · At the small price of increasing the number of elements in the ontology from two to three, we gain a tremendous capability of concurrently modeling both the structure and the behavior of a system. Indeed, objects are the things that exist. · [src:S01:L2322-L2355](../../../INBOX/opm-libro.txt#L2322-L2355)
- **P0748** · `fact` · Relations among them constitute the structure of the system. · [src:S01:L2322-L2355](../../../INBOX/opm-libro.txt#L2322-L2355)
- **P0749** · `fact` · This is the static, structural aspect of the system. · [src:S01:L2322-L2355](../../../INBOX/opm-libro.txt#L2322-L2355)
- **P0750** · `fact` · To understand the system’s dynamic, procedural aspect, to know what happens to objects in the system and how it operates to provide value, a second, complementary type of thing is needed—a process. · [src:S01:L2322-L2355](../../../INBOX/opm-libro.txt#L2322-L2355)
- **P0751** · `fact` · We know of the existence of an object if we can name it and refer to its unconditional, relatively stable existence, but without processes we can neither tell how this object is created or destroyed, nor how its states change over its lifetime. · [src:S01:L2322-L2355](../../../INBOX/opm-libro.txt#L2322-L2355)
- **P0752** · `fact` · A stateless object is an object that has no states. · [src:S01:L2322-L2355](../../../INBOX/opm-libro.txt#L2322-L2355)
- **P0753** · `fact` · A stateful object is an object that has one or more states. · [src:S01:L2322-L2355](../../../INBOX/opm-libro.txt#L2322-L2355)
- **P0754** · `fact` · These states are stable in the sense that it takes a process to switch an object from one of its states to another, and as long as no process acts on the object, the object remains in the same state. respectively shown as the first (left-most) group of symbols. · [src:S01:L2322-L2355](../../../INBOX/opm-libro.txt#L2322-L2355)
- **P0755** · `fact` · The rest of the symbols are links: structural links are shown in the middle group and procedural links—in the right-most group. · [src:S01:L2322-L2355](../../../INBOX/opm-libro.txt#L2322-L2355)
- **P0756** · `fact` · Their names and semantics have been mentioned in Part I, and will be further elaborated as we proceed. · [src:S01:L2322-L2355](../../../INBOX/opm-libro.txt#L2322-L2355)
- **P0757** · `fact` · Objects and processes, collectively referred to as OPM things, are the two types of OPM’s universal building blocks. · [src:S01:L2322-L2355](../../../INBOX/opm-libro.txt#L2322-L2355)
- **P0758** · `fact` · OPM views objects and processes as being on equal footing, so processes are not necessarily subordinate to or owned by objects. · [src:S01:L2322-L2355](../../../INBOX/opm-libro.txt#L2322-L2355)
- **P0759** · `constraint` · Symmetrically, objects are not necessarily inferior to processes, nor are processes necessarily owned by objects. State is depicted in Fig. 9.1 between object and process. · [src:S01:L2322-L2355](../../../INBOX/opm-libro.txt#L2322-L2355)
- **P0760** · `fact` · Discussed in more detail later on, state is a situation in which an object can be at some point during its lifetime. · [src:S01:L2322-L2355](../../../INBOX/opm-libro.txt#L2322-L2355)

## opm libro · Chapter 9 Conceptual Modeling: Purpose and Context / 9.2.6 The Thing Importance OPM Principle

- **P0761** · `fact` · In OO, objects “own” processes, which in the OO jargon are called operations, or services, or methods. · [src:S01:L2357-L2377](../../../INBOX/opm-libro.txt#L2357-L2377)
- **P0762** · `fact` · OPM takes a different stand: Major system-level processes can be as important as, or even more important than objects in the system model. · [src:S01:L2357-L2377](../../../INBOX/opm-libro.txt#L2357-L2377)
- **P0763** · `fact` · In particular, we already noted that the top-level process of a system (or subsystem) is its function, the top-level value-providing and purpose-serving process, for the performance of which the system is built and used. · [src:S01:L2357-L2377](../../../INBOX/opm-libro.txt#L2357-L2377)
- **P0764** · `requirement` · Hence, a process must be amenable to being modeled independently of any particular set of objects involved in its occurrence. · [src:S01:L2357-L2377](../../../INBOX/opm-libro.txt#L2357-L2377)
- **P0765** · `fact` · Therefore, OPM views both objects and processes as first-class citizens. · [src:S01:L2357-L2377](../../../INBOX/opm-libro.txt#L2357-L2377)
- **P0766** · `fact` · They stand on equal footing; neither has supremacy over the other. · [src:S01:L2357-L2377](../../../INBOX/opm-libro.txt#L2357-L2377)
- **P0767** · `fact` · Rather, their importance is related the model hierarchy as expressed in the following thing importance OPM Principle. · [src:S01:L2357-L2377](../../../INBOX/opm-libro.txt#L2357-L2377)
- **P0768** · `fact` · The Thing Importance OPM Principle The importance of a thing T in an OPM model is directly related to the highest OPD in the OPD hierarchy where T appears. · [src:S01:L2357-L2377](../../../INBOX/opm-libro.txt#L2357-L2377)
- **P0769** · `fact` · For example, the object ACR System and the process Automatic Crash Responding in Fig. · [src:S01:L2357-L2377](../../../INBOX/opm-libro.txt#L2357-L2377)
- **P0770** · `constraint` · 1.2 are of the same relative importance, as they show up for the first time in SD, the System Diagram, which is the top- level OPD. · [src:S01:L2357-L2377](../../../INBOX/opm-libro.txt#L2357-L2377)
- **P0771** · `fact` · Indeed, the object ACR System is required for the process Automatic Crash Responding to take place, so one cannot argue for the supremacy of the object ACR System over the process Automatic Crash Responding or vice versa. · [src:S01:L2357-L2377](../../../INBOX/opm-libro.txt#L2357-L2377)
- **P0772** · `fact` · Being able to tell objects and processes apart and use them properly in a model is key to modeling in OPM. · [src:S01:L2357-L2377](../../../INBOX/opm-libro.txt#L2357-L2377)
- **P0773** · `definition` · To define these fundamental concepts and to communicate their semantics, we next discuss the concepts of existence and transformation. · [src:S01:L2357-L2377](../../../INBOX/opm-libro.txt#L2357-L2377)

## opm libro · Chapter 9 Conceptual Modeling: Purpose and Context / 9.3 Object, State, Transformation, and Process Defined

- **P0774** · `definition` · Since objects OPM can be physical or informatical (cybernetic), we define object as something that captures these two facets without committing to either one, while including the element of “existence throughout time.” An object is a thing that exists or can exist physically or informatically. · [src:S01:L2379-L2404](../../../INBOX/opm-libro.txt#L2379-L2404)
- **P0775** · `fact` · The object’s existence can be physical or informatical. · [src:S01:L2379-L2404](../../../INBOX/opm-libro.txt#L2379-L2404)
- **P0776** · `fact` · It can be as simple as a block of ice, a word in a book or a record in a file, or as complex as an organization, the Internet, a human brain, or a galaxy. · [src:S01:L2379-L2404](../../../INBOX/opm-libro.txt#L2379-L2404)
- **P0777** · `fact` · A state is a possible situation or position at which an object can be for some positive amount of time. · [src:S01:L2379-L2404](../../../INBOX/opm-libro.txt#L2379-L2404)
- **P0778** · `fact` · This definition implies that a state has a meaning only within and in the context of an object. · [src:S01:L2379-L2404](../../../INBOX/opm-libro.txt#L2379-L2404)
- **P0779** · `fact` · A state has no meaning out of the contexts of its owning object. · [src:S01:L2379-L2404](../../../INBOX/opm-libro.txt#L2379-L2404)
- **P0780** · `fact` · For example, states of the object Organization can be private or public, and states of the object Record can be locked or unlocked. · [src:S01:L2379-L2404](../../../INBOX/opm-libro.txt#L2379-L2404)
- **P0781** · `fact` · The states private and locked have no meaning outside the context of their respective owning objects. · [src:S01:L2379-L2404](../../../INBOX/opm-libro.txt#L2379-L2404)
- **P0782** · `constraint` · Transformation is (1) creation (generation, construction), (2) consumption (elimination, destruction), or (3) effect—change in the state of an object. · [src:S01:L2379-L2404](../../../INBOX/opm-libro.txt#L2379-L2404)
- **P0783** · `fact` · Transformation takes a positive amount of time. · [src:S01:L2379-L2404](../../../INBOX/opm-libro.txt#L2379-L2404)
- **P0784** · `requirement` · By this definition, a process must be associated with at least one object: the one which that process transforms. · [src:S01:L2379-L2404](../../../INBOX/opm-libro.txt#L2379-L2404)
- **P0785** · `fact` · For example, Freezing is a process that changes the state of Water form liquid to ice. · [src:S01:L2379-L2404](../../../INBOX/opm-libro.txt#L2379-L2404)
- **P0786** · `fact` · This is the basis for the object transformation by process OPM principle. · [src:S01:L2379-L2404](../../../INBOX/opm-libro.txt#L2379-L2404)
- **P0787** · `requirement` · The Object Transformation by Process OPM principle In a complete OPM model, each process must be connected to at least one object that the process transforms or one state of the object that the process transforms. · [src:S01:L2379-L2404](../../../INBOX/opm-libro.txt#L2379-L2404)
- **P0788** · `definition` · A non-trivial synchronous process (i.e., a process whose subprocesses have a defined order of execution) comprises a hierarchical network of subprocesses. · [src:S01:L2379-L2404](../../../INBOX/opm-libro.txt#L2379-L2404)
- **P0789** · `requirement` · At every level of the process hierarchy there is a time-induced partial order on the processes, i.e., some processes must end before others start, while others can occur in parallel to other processes or as their alternatives. · [src:S01:L2379-L2404](../../../INBOX/opm-libro.txt#L2379-L2404)
