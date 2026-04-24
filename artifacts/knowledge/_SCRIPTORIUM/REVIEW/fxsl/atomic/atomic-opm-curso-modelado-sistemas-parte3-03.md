---
_manifest:
  urn: urn:fxsl:kb:atomic-opm-curso-modelado-sistemas-parte3-03
  provenance:
    created_by: atomize
    created_at: '2026-04-24'
    source: /home/felix/kora/artifacts/knowledge/_SCRIPTORIUM/INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt
version: 1.0.0
status: borrador
tags:
- atomic
- knowledge
- opm-curso-modelado-sistemas-parte3
lang: es
extensions:
  kora:
    family: atomic
    atomic:
      producer: urn:kora:artefacto:atomize
      source_corpus: /home/felix/kora/artifacts/knowledge/_SCRIPTORIUM/INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt
      n_propositions: 35
      segmented: true
      segment_role: segment
      segment_index: 3
      segment_count: 3
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:fxsl:kb:atomic-opm-curso-modelado-sistemas-parte3-03
---

# Atomic opm-curso-modelado-sistemas-parte3 - Segmento 03

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/artifacts/knowledge/_SCRIPTORIUM/INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt`
- Proposiciones: `35`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `03/03`

## Indice de fuentes

- `S01` · [fx_curso_modelado_sistemas_parte3.txt](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt) · fx curso modelado sistemas parte3

## fx curso modelado sistemas parte3 · Parte 3 / Object refinement

- **P084** · `fact` · After we learned to refine synchronous and asynchronous processes in SD1, the first detailed level of an OPM model, it's time to learn how to refine objects. · [src:S01:L321-L340](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L321-L340)
- **P085** · `fact` · With this last piece of knowledge, you will be able to model an electric car system that will adhere to the strict standards of ISO. · [src:S01:L321-L340](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L321-L340)
- **P086** · `fact` · Let's go back to the model we created for alerting the driver regarding dangers on the road. · [src:S01:L321-L340](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L321-L340)
- **P087** · `fact` · We refined the main process of this system as asynchronous, by unfolding it. · [src:S01:L321-L340](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L321-L340)
- **P088** · `fact` · In our model, the system is an object that serves as an instrument of the main process. · [src:S01:L321-L340](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L321-L340)
- **P089** · `fact` · It exhibits the attribute Representation Set - another object in its own right. · [src:S01:L321-L340](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L321-L340)
- **P090** · `fact` · This object consists of three parts: ''Vehicle-in-Front Representation'', ''Pedestrian-in-Front Representation'' and ''Lane Set Representation''. · [src:S01:L321-L340](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L321-L340)
- **P091** · `fact` · We refined the object ''Mobileye System'' into four objects: System structure three parts and one attribute. · [src:S01:L321-L340](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L321-L340)
- **P092** · `fact` · If we wish to group the entire structure of "Mobileye System'' into a single OPD, we can do this by unfolding the refined object. Let's do this now. Good! · [src:S01:L321-L340](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L321-L340)
- **P093** · `fact` · We created a new OPD, which shows us the system's structure · [src:S01:L321-L340](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L321-L340)
- **P094** · `fact` · it only includes objects, not processes. This diagram shows an ''object tree'' · [src:S01:L341-L342](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L341-L342)
- **P095** · `fact` · the main object · [src:S01:L343](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L343)
- **P096** · `requirement` · the “refineable” - and its “refines” - its parts and attributes. Now, let's turn to another model we created: State suppression a synchronous process of the same system, to learn about state suppression and expression. Here, we can see all the possible states of ''Vehicle-in-Front Representation''. However, do we need this in SD? After all, here we used an effect link, which only tells us that the linked process somehow changes the object from one state to another. Only in SD1 we show the details of how specific sub-processes change these states. Therefore, in SD, we shall hide the states, or suppress them, to make the OPD simpler and easier to understand. In general, we should suppress (or hide) states that in some OPD are not linked to any process and therefore do not add to our understanding of the model when looking at that OPD. Notice that when one or more states are suppressed, a pseudo-state - a small state with three dots - appears at the bottom right corner of the object, indicating that the object has at least one more state, which is suppressed. For this model, there is no need to show any state of ''Vehicle-in-Front Representation'' in SD, so we shall hide them. Now, all the states are suppressed. However, in the first detail level, SD1, the states are still expressed, and we can see them linked to the sub-processes that change them. Emergence Very good! Before saying good bye for now, let's discuss a central concept in systems engineering called ''emergence''. Emergence is the appearance of a capability, or functionality that characterizes the entire system, but not any one of its constituent parts. A good example of emergence, is the Road Danger Warning system, which we modeled in a previous unit. This system consists of many parts, objects and processes For the system to perform its function and fulfill its purpose of lowering the probability of a crash · [src:S01:L344-L375](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L344-L375)
- **P097** · `requirement` · all those parts must be coordinated and work together. If we separate the system into its various parts, they would not be able to do what the system as a whole does: Conclusion The combination of the system's structure and behavior, which gives rise to its emergence, is the system architecture. Through emergence, the system's architecture enables it to function and deliver the benefit to its beneficiaries. This was what we have done so far: we began with SD and its related components purpose, function, enablers, environment, and problem occurrence - and refined it in SD1. See you soon! · [src:S01:L376-L385](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L376-L385)

## fx curso modelado sistemas parte3 · Parte 3 / Objects y processes as features of each other

- **P098** · `fact` · Before we move on to the next chapter, let's learn about the use of the exhibition-characterization relation between objects and processes! · [src:S01:L390-L431](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L390-L431)
- **P099** · `fact` · Here is a model of the Road Danger Alerting system that we have recently constructed. · [src:S01:L390-L431](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L390-L431)
- **P100** · `fact` · The Mobileye System is an object, which is an instrument of the process Road Danger Alerting. · [src:S01:L390-L431](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L390-L431)
- **P101** · `fact` · The two are related by an instrument link, which is procedural. · [src:S01:L390-L431](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L390-L431)
- **P102** · `fact` · In addition, the Mobileye System has another relation to the process - one that is not procedural, but structural: Road Danger Alerting is an operation of Mobileye System. Let us show this. · [src:S01:L390-L431](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L390-L431)
- **P103** · `fact` · The OPL sentence says: “Mobileye System exhibits Road Danger Alerting.” The exhibition-characterization link is the only structural link that can connect objects with processes. · [src:S01:L390-L431](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L390-L431)
- **P104** · `fact` · All the other structural links connect either objects with objects, or processes with processes. · [src:S01:L390-L431](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L390-L431)
- **P105** · `fact` · As a rule, in human-made systems, the object whose name ends with the word 'System' Characterization link is the instrument of the main process, and it will always exhibit the main process as its operation. · [src:S01:L390-L431](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L390-L431)
- **P106** · `fact` · Operation is a process that characterizes an object - what the object does or can do. · [src:S01:L390-L431](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L390-L431)
- **P107** · `fact` · Operation is analogous to attribute in that both characterize the object that exhibits them. · [src:S01:L390-L431](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L390-L431)
- **P108** · `fact` · Operation Just like we said that an object and a process are specialization of a thing, We now say that attribute and operation are specializations of Feature. · [src:S01:L390-L431](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L390-L431)
- **P109** · `fact` · Feature is a thing that characterizes another thing - the thing that exhibits that feature. and an operation - a feature which is a process. · [src:S01:L390-L431](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L390-L431)
- **P110** · `fact` · Those of you who program, are familliar with the term "Method". Operation is the same as "Method". · [src:S01:L390-L431](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L390-L431)
- **P111** · `fact` · Tree Take for example a simplified OPM model of how a tree grows. Tree Growing is an operation of Tree. Let us model this. · [src:S01:L390-L431](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L390-L431)
- **P112** · `fact` · The OPL sentence says: “Tree exhibits Tree Growing.” From a procedural view point, "Growing" effects "Tree", so we say that tree is an "effectee" of growing , and we denote this by an effect link between the two. · [src:S01:L390-L431](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L390-L431)
- **P113** · `fact` · The exhibition-characterization can also work in the other direction: Attribute An object can be an attribute of a process. · [src:S01:L390-L431](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L390-L431)
- **P114** · `definition` · To see what this means, let's look again at the Airplane Flying system model from the previous chapter. · [src:S01:L390-L431](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L390-L431)
- **P115** · `fact` · In this simplified model, origin and destination are states of Airplane rather than states of its location attribute. · [src:S01:L390-L431](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L390-L431)
- **P116** · `fact` · Flying is an operation of Airplane - a process that Airplane can do. Let's show this in the model. The OPL sentence reads: · [src:S01:L390-L431](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L390-L431)
- **P117** · `fact` · “Airplane exhibits Flying.” Flying itself has attributes, which are objects. For example: Flight number, and Flight Path and Average Speed. The OPL sentence reads: “Flying exhibits Flight Number, Flight Path and Average Speed." Attributes are always informatical, because they describe a thing · [src:S01:L432-L438](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L432-L438)
- **P118** · `fact` · they provide information or data about that thing. Operations, however, can be either physical or informatical. For example, Flying is physical, because it entails moving the physical Airplane with the Passenger Group in it from origin to destination. Commanding and Advising, however, are informatical, because it entails passing information on actions that need or should be done. Excellent! Let's have HopCat summarize this for us, And I will see you in the next section. Attribute is an object that characterizes or describes a thing. Operation is a process that characterizes a thing, which performs it. Feature is a thing that characterizes or describes a thing. It generalizes attribute and operation, each being a refinee. · [src:S01:L439-L451](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L439-L451)
