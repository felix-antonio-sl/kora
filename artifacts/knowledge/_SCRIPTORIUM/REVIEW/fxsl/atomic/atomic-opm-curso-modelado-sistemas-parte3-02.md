---
_manifest:
  urn: urn:fxsl:kb:atomic-opm-curso-modelado-sistemas-parte3-02
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
      n_propositions: 23
      segmented: true
      segment_role: segment
      segment_index: 2
      segment_count: 3
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:fxsl:kb:atomic-opm-curso-modelado-sistemas-parte3-02
---

# Atomic opm-curso-modelado-sistemas-parte3 - Segmento 02

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/artifacts/knowledge/_SCRIPTORIUM/INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt`
- Proposiciones: `23`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `02/03`

## Indice de fuentes

- `S01` · [fx_curso_modelado_sistemas_parte3.txt](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt) · fx curso modelado sistemas parte3

## fx curso modelado sistemas parte3 · Parte 3 / Modelling principles

- **P061** · `fact` · We are continuing to model the first detail level of the synchronous process that detects vehicles and alerts the driver of a crash. Here is where we got to last time. · [src:S01:L179-L202](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L179-L202)
- **P062** · `fact` · Vehicle in front representation There is an informatical object, which is transformed by each one of the sub processes; this is ''Vehicle-in-Front Representation'', which the Mobileye system generates. · [src:S01:L179-L202](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L179-L202)
- **P063** · `fact` · The first sub-process transitions the state of this object from ''not detected'' to ''detected''. · [src:S01:L179-L202](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L179-L202)
- **P064** · `fact` · Since ''Vehicle-in-Front Representation'' is an important attribute of Mobileye System, we will add it also in SD and connect it with an exhibition-characterization link to Mobileye System. · [src:S01:L179-L202](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L179-L202)
- **P065** · `requirement` · How shall we link ''Vehicle-in-Front Representation'' to the main process? · [src:S01:L179-L202](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L179-L202)
- **P066** · `fact` · Well, since we already modeled the various state transitions in SD1, there is no need to repeat the same detailed model facts in SD, which needs to be simpler and more abstract. · [src:S01:L179-L202](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L179-L202)
- **P067** · `fact` · Therefore, we will connect it to the main process using an effect link. · [src:S01:L179-L202](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L179-L202)
- **P068** · `fact` · The meaning of this link is that the process transforms the object by changing its states, but there are no details about the changes themselves. · [src:S01:L179-L202](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L179-L202)
- **P069** · `fact` · In SD1, the object ''Vehicle-in-Front Representation'' is connected to the sub-processes with input-output link pairs. · [src:S01:L179-L202](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L179-L202)
- **P070** · `fact` · In any OPD, any specific object can be connected to a specific process with a single type of procedural link. · [src:S01:L179-L202](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L179-L202)
- **P071** · `fact` · Procedural link uniqueness This is the procedural link uniqueness OPM principle. · [src:S01:L179-L202](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L179-L202)
- **P072** · `exclusion` · For example, an object can not be linked to a process by both an instrument link and a consumption link. · [src:S01:L179-L202](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L179-L202)
- **P073** · `fact` · We will let HopCat explain: The Procedural Link Uniqueness OPM Principle · [src:S01:L179-L202](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L179-L202)
- **P074** · `fact` · At any level of detail, a process and an object or any of its states can be connected with at most one procedural link, which uniquely determines the role of the object with respect to the process. Let's continue to model SD1. here it is also important to think about agents and instruments of the various sub-processes. Usually, every process has at least one enabler. The Mobileye system enables each one of the sub-processes of SD1. · [src:S01:L203-L210](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L203-L210)
- **P075** · `exclusion` · in more than one OPD unless the duplicate model fact adds to our understanding of that OPD. To avoid redundancy, we will not add Mobileye System to SD1. For the same reason, we will not add in SD1 ''Car'' or ''Vehicle-in-Front''. In SD1, we dive deeper into the structure, behavior, and function of the system, still without extensive use of technical terms. It is important that we know how to model our system at this level, so that the autonomous car we are developing receives an ISO standard - like OPM 19450:2015, so it will be allowed on the road. Next time we meet, we will learn how to refine an asynchronous process. Drive safe! :) · [src:S01:L212-L222](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L212-L222)

## fx curso modelado sistemas parte3 · Parte 3 / Asynchronus process refinement

- **P076** · `fact` · Hello again! Last time we met, we modeled a synchronous process · [src:S01:L226-L227](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L226-L227)
- **P077** · `fact` · a process comprising sub-processes that occur in a specific sequence. We will now learn how to model asynchronous processes processes comprising sub-processes that are independent of each other and can occur in parallel or in a different sequence every time the system operates. We will look again at the smart car system we are modeling in this section. We can see that the system has two functions in addition to alerting about potential crashes in front of the car: · [src:S01:L228-L234](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L228-L234)
- **P078** · `definition` · Pedestrian-in-Front Crash Alerting and - Deviation from lane without indicating. This is a wider view than the one we had when we modeled a synchronous part of the system. There we focused on a specific scenario, in which the braking time before crashing into a vehicle in the front was getting shorter and shorter. Now we want to model the system's operation in a more comprehensive manner. Here is the model of the system's top view - the SD. We call the main process Road Danger Warning. The SD is similar to the SD of the previous model we saw, where we refined a synchronous process. As we have just seen, the main process can be modeled as being comprised of three independent sub-processes. But before we do that, we will ask HopCat to provide us with a definition. An asynchronous process is a process whose sub-processes do not have a predefined, fixed order. Thanks, HopCat! Now, we will refine the main process. However, while previously we did this by in-zooming, which determines process execution order and is therefore fit for synchronous processes, we will now do this by unfolding. A new OPD labeled SD1 is created. We will add to it the three sub-processes we talked about earlier: · [src:S01:L235-L252](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L235-L252)
- **P079** · `fact` · Vehicle-in-Front Crash Alerting, · [src:S01:L253](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L253)
- **P080** · `fact` · Pedestrian-in-Front Crash Alerting and · [src:S01:L254](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L254)
- **P081** · `fact` · Lane Deviation Alerting. How should we connect these sub-processes to the main process? Using a structural link, of course. There are two types of structural links we can use when connecting asynchronous processes: · [src:S01:L255-L258](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L255-L258)
- **P082** · `fact` · Aggregation-Participation, which we have already seen, and generalization-specialization, which we will learn about now. · [src:S01:L259-L260](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L259-L260)
- **P083** · `exclusion` · Generalization-Specialization, expresses a relationship between a general thing and its specializations, or in other words, between a type and its sub-types. For example, car is a specialization of vehicle, and truck is another specialization of vehicle. So what relation should we use here? Aggregation-Participation or Generalization-Specialization? Are the sub-processes part of the main process, or specializations of it? In this system, each sub-process is a specialization - a type of alert from dangers on the road. Therefore, we will use a generalization-specialization link. The OPL sentence reads: ''Vehicle-in-Front Crash Alerting, Pedestrian-in-Front Crash Alerting, and Lane Deviation Alerting are Road Danger Warning''. Good! This shows us that the link we chose expresses what we wish to model. Now, we must confirm that each sub-process transforms an object. Let's go process by process. The first sub-process deals with something we are already familiar with: warning about crashing into another vehicle. We will model this by adding an informatical object called ''Vehicle-in-Front Representation'' with two states: ''not yet detected'' and ''crash alert''. The process transforms the object by changing its states. The second sub-process executes a transformation similar to that of the first one, this time for the representation of pedestrians. We will therefore add an informatical object called ''Pedestrian-in-Front Representation'' with two states: ''detected'' and ''run-over alert''. Again, the process is what causes the state transition. Regarding the third sub-process, deviating from the lane, we will add ''Lane Set Representation'', with two states: ''not detected'' and ''deviation alert'', with a state transition carried out by the corresponding sub-process, “Lane Deviation Alerting”. Let's review what we modeled by inspecting the OPL sentences created: ''Vehicle-in-Front Crash Alerting changes Vehicle-in-Front Representation from not detected to crash alert''. ''Pedestrian-in-Front Crash Alerting changes Pedestrian-in-Front Representation from not detected to run-over alert''. ''Lane Deviation Alerting changes Lane Set Representation from not detected to deviation alert''. Now, every sub-process transforms an object. What about environmental transformees? To achieve the benefit of the system - reducing the probability of crash the system creates representations of environmental objects: Vehicle-in-Front, Pedestrian-in-Front, and Lane Set. We will add ''Pedestrian'' to SD1, and connect it to the appropriate sub-process with an agent link. Let us add this object also to SD, and connect it to the main process with an agent link. Finally, the sub-process ''Lane Set Warning'' is made possible only when driving on a road with clearly marked traffic lanes. We will model this in both SD and SD1. What about the various representations we modeled in SD1? If we include all of them in SD, it will become cluttered with too many objects and cris-crossing links, which will render SD incomprehensible. So instead, we will create in SD1 a new object called ''Road Danger Representation''. Since each one of the three representations is a specialization of a road danger, we connect it to the three objects with a generalization-specialization link. Only this more abstract, general object ''Road Danger Representation'' will be added to SD and connected to Mobileye System with an exhibition-characterization link. Additionally, we will connect it to the main process with an effect link. We learned how to model asynchronous processes at the first detail level. You are now one-step closer to being able to model a system that will be recognized as an ISO standard, which is what your CEO asked. Next time we meet, you will learn how to refine objects. I'll see you soon! · [src:S01:L261-L316](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L261-L316)
