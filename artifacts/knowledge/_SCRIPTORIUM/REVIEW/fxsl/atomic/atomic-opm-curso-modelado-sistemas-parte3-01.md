---
_manifest:
  urn: urn:fxsl:kb:atomic-opm-curso-modelado-sistemas-parte3-01
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
      n_propositions: 60
      segmented: true
      segment_role: segment
      segment_index: 1
      segment_count: 3
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:fxsl:kb:atomic-opm-curso-modelado-sistemas-parte3-01
---

# Atomic opm-curso-modelado-sistemas-parte3 - Segmento 01

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/artifacts/knowledge/_SCRIPTORIUM/INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt`
- Proposiciones: `60`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `01/03`

## Indice de fuentes

- `S01` · [fx_curso_modelado_sistemas_parte3.txt](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt) · fx curso modelado sistemas parte3

## fx curso modelado sistemas parte3 · Parte 3 / Process refinement

- **P001** · `fact` · After a long journey, during which you studied different systems, you were able to model SD, the top-level diagram of a robotics-based electric cars manufacturing system. · [src:S01:L5-L12](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L5-L12)
- **P002** · `fact` · The CEO of the company is happy, and I am so proud to be your mentor! · [src:S01:L5-L12](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L5-L12)
- **P003** · `fact` · Now, the company you work for is involved in a new and exciting project converting an electric car into an autonomous one! · [src:S01:L5-L12](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L5-L12)
- **P004** · `fact` · You were asked to model this system so the company can submit it to ISO - the International Organization for Standardization · [src:S01:L5-L12](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L5-L12)
- **P005** · `definition` · as a proposal for a new International Standard for autonomous cars! To convert a human-driven car into an autonomous one, we first need to integrate a few systems into it, including a system for monitoring and interpreting the environment. A major task of this system is to detect vehicles and pedestrians, and alert the driver before a collision happens. Mobileye, which is part of the global Intel corporation, develops and integrates such systems in many millions of cars worldwide. Here, we can see such a system in operation inside an experimental autonomous car. In the next few videos, we will learn how to model it. For an autonomous car to receive regulatory approval, it must adhere to standards that require modeling the system conceptually. Therefore, the CEO wants you to create a detailed OPM system model for submission to ISO. In this section, you will learn how to model the first detail level of every system. We called the top-level System Diagram, or SD, and this was level zero. The first detail level is called SD1, and this is level one. At this level, we specify what processes make up the main process from SD. Here, we also refine objects from SD. Recall that SD answers the big questions about the system: its purpose, main function, enablers of the main process, the system's environment, and how the problem it solves occurs. In SD1, we start fleshing out the system by specifying details about its structure, behavior, and function. Here comes HopCat who is so helpful with definitions! in which the main process is refined, exposing its sub processes and objects associated with them. Detail hierarchy OPM principle - Whenever an OPD becomes hard to comprehend due to an excessive amount of details, a new, descendant OPD shall be created. To begin learning how to model SD1, let's look at Mobileye - a system that monitors the car's environment, detects vehicles and pedestrians in the front, and escalates alerting the driver before a crash is eminent. A common scenario is a car getting closer and closer to a car in front of it. Here, several processes occur in sequence, one after the other: First, the system detects a car in the front, but being far enough, it doesn't alert the driver. As we get closer to the car in front, the time in seconds, needed for stopping, is displayed in green. As we get even closer, the braking time is displayed in red, and a single short beep is sounded. Finally, if we come to a crashing distance, a big red car icon is displayed, and we hear several frequent, short loud beeps. We can see that the main process we described is comprised of four smaller sub processes, occurring in a fixed order: Detecting, Informing, Alerting and Crash Alerting. A process, whose sub processes occur sequentially in a fixed, known order, is a synchronous process. Here are two examples of synchronous processes, one in a technological system and the other in a natural one: Airplane Flying always starts with Takeoff and Ascending, continues with Cruising, then Descending, Landing, Taxiing, and finally Parking. Tree Growing always starts with Germinating, continues with Seedling, Sapling and Maturing, and it ends with Decaying and Withering. In contrast with a synchronous process, an asynchronous process comprises sub processes that are not dependent on each other and can occur in any order. For example, in an Email Managing System, the main process is ''Email Managing''. It comprises sub processes that have no specific order of occurrence. We can, for example, send a new message, read some messages in our inbox, or delete spam messages. These processes refine the main process, but do not occur at any particular order. Another example of an asynchronous process is shopping at a mall: We can buy clothes before we buy electronic products, then do some window shopping, but the order in which we do it is immaterial. The operation of the human brain is also asynchronous, as many different, complex processes happen within our heads in parallel and in numerous various sequences. What about this MOOC? Is your learning process synchronous or asynchronous? That depends on your learning style. Some of you learn this course synchronously, according to the prescribed order of the various learning activities, while others might go back and forth in case they want to make sure they fully understand some topic. This is an example where a process can be modeled either synchronously or asynchronously. Like processes, objects can be refined too. For example, in the Mobileye model, we might want to specify the system's camera and computer. Unlike processes, which are dynamic and time-dependent, objects are static. so synchronicity is irrelevant for objects. Let's summarize: We learned how to construct SD1 - the first detail level of an OPM system model, which refines things in SD, providing more information about the system's function, structure and behavior. We also learned about synchronous and asynchronous processes and how they differ from each other. In the next videos in this section, we will learn how to refine OPM processes and objects as we learn more about the Mobileye system. See you soon! · [src:S01:L13-L87](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L13-L87)

## fx curso modelado sistemas parte3 · Parte 3 / Synchronus process refinement

- **P006** · `fact` · Hello, my engineer friend! · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P007** · `fact` · The previous time we met, we learned about Mobileye system for detecting vehicles and pedestrians on the road, and alerting from potential crashes. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P008** · `fact` · We concluded that the main process is synchronous, as it is comprises sub-processes occurring in a specific sequence. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P009** · `fact` · Now, let's lets model the 1st detailed level of this system - SD1. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P010** · `fact` · We will start with modeling SD - the top level, and proceed with SD1. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P011** · `fact` · The scenario we will model is when cars get ever closer causing decrease in the breaking time needed to avoid collision. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P012** · `fact` · We have already determined that the system's main process is ''Vehicle-in-Front Detecting & Crash Alerting''. What is the purpuse of the system? · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P013** · `fact` · What is the benefit that the system provides? · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P014** · `fact` · The system reduces the probability of the driver crashing into the vehicle in front. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P015** · `fact` · The main function of the system is to provide the car with the ability to detect vehicles in the front and alert the driver when the braking time is too short. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P016** · `fact` · The enabler of the main process is the Mobileye system, which is an instrument. The system is part of the car. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P017** · `fact` · Notice that the driver is not an agent of the system, because he or she does not handle it. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P018** · `fact` · The driver is enviromental relative to our system of interest. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P019** · `fact` · So let's change the driver's affiliation from systemic to environmental. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P020** · `fact` · Another environmental object in our system is the car. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P021** · `fact` · The system architecture engineer have no control over the car. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P022** · `fact` · But the system has to be installed in it, and use information it provides. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P023** · `fact` · The vehicle in front is also environmental, and it is an instrument of the main process, as our system does not transform it, but without it, there would be nothing to detect! · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P024** · `fact` · And finally, problem occurrence - what problem does this system solve? · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P025** · `fact` · The answer is related to the system purpose, described previously. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P026** · `fact` · The problem occurs when a car gets close to a vehicle in front of it, and the car's driver is at state "not aware" of the approaching danger. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P027** · `fact` · Lack of timely alert increases the probability of crashing. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P028** · `fact` · Having modeled SD, let's dive down and model final details of the system in SD1. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P029** · `constraint` · Detection of the vehicle in the front starts at a relatively large distance when the braking time is 10 seconds. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P030** · `fact` · But, at this point no signal is given to the driver. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P031** · `constraint` · When the calulated breaking time is 2.5 seconds or less, the little round display installed in the car shows this time in green digits. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P032** · `constraint` · When breaking time drops to 1.2 seconds or less, the system alerts the driver by changing the braking time to red and soundning a single beep. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P033** · `constraint` · When the braking time is 0.7 seconds of less, the system provides alerting for a crash. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P034** · `fact` · The display screen shows a big red car and multiple freequent beeps are sounded. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P035** · `fact` · Having review this sequence of processes, let's refine the main process using them! · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P036** · `fact` · Since we are modeling a synchronous process, we will carry out a refinement operation called in-zooming. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P037** · `fact` · A new OPD SD1 is created with the main process inflated in the middle. How should we add the sub-processes to SD1? · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P038** · `requirement` · We shall use the timeline OPM principle, according to which, sub-processes within a synchronous process are arranged vertically by their order of occurrence. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P039** · `fact` · The first sub-process will be at the top, followed by the next in line, and so on... till the last to occur, which will be placed at the bottom of the inflated elipse of the in-zoom process. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P040** · `fact` · The timeline principle is key to modeling every synchronous process, so we should remember and use it! · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P041** · `fact` · Applying these principle, lets add the sub-processes inside the main process. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P042** · `fact` · These are parts of the main process that contain them. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P043** · `fact` · So there is an aggregation-participation relation here. the relation is expressed by the containment of the participating sub-processes inside the aggregating process. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P044** · `definition` · We can see that the OPD we constructed expressed in the following OPL sentences: Here comes HopCat to give us a definition. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P045** · `definition` · A synchronous process is a process whose subprocesses have predefined fixed order. is directed by default from the top of the in-zoomed process ellipse to its bottom. Thank you, Hopcat! · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P046** · `fact` · Now, we will check or add details of the structure, behavior, and function of the system like we did in SD. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P047** · `fact` · Let's start with the system's purpose - can it be linked to a specific sub-process in SD1? · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P048** · `fact` · Well, we can say that the last sub-process - ''Crash Alerting'' - is the one delivering the system's benefit. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P049** · `fact` · Indeed, this sub-process is connected the object ''Crash Probability''. What about the main function of the system? · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P050** · `fact` · Is there a specific sub-process that is responsible for it? Yes! · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P051** · `fact` · The first sub-process enables the detection of the vehicle in front of the car. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P052** · `fact` · Indeed, the object ''Vehicle-in-Front Alerting Ability'' in SD1 is connected to the first sub-process. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P053** · `requirement` · In OPM, every process must be linked to at least one transformee. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P054** · `fact` · To comply, let's go process by process and add a transformee to each one. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P055** · `fact` · What object is transformed by the first sub-process, Detecting? · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P056** · `fact` · This sub-process transitions the state of Vehicle-in-Front Representation from 'not detected' to 'detected'. Good! · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P057** · `fact` · What about the second sub-process, Informing? · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P058** · `fact` · Here we can also show a state transition - again of Vehicle-in-Front Representation, but this time from 'detected' to 'driver informed'. What about the next sub-process, Alerting? · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P059** · `fact` · It changes Vehicle-in-Front Representation from 'driver informed' to 'driver warned', as braking time becomes even shorter. · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
- **P060** · `constraint` · Finally, the last sub-process, Crash Alerting, changes Vehicle-in-Front Representation from 'driver warned' to 'crash alerting', when braking time is less than 0.7 seconds. See you soon! · [src:S01:L91-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte3.txt#L91-L174)
