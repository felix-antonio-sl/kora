---
_manifest:
  urn: urn:fxsl:kb:atomic-opm-curso-modelado-sistemas-parte1-02
  provenance:
    created_by: atomize
    created_at: '2026-04-24'
    source: /home/felix/kora/artifacts/knowledge/_SCRIPTORIUM/INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt
version: 1.0.0
status: borrador
tags:
- atomic
- knowledge
- opm-curso-modelado-sistemas-parte1
lang: es
extensions:
  kora:
    family: atomic
    atomic:
      producer: urn:kora:artefacto:atomize
      source_corpus: /home/felix/kora/artifacts/knowledge/_SCRIPTORIUM/INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt
      n_propositions: 48
      segmented: true
      segment_role: segment
      segment_index: 2
      segment_count: 7
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:fxsl:kb:atomic-opm-curso-modelado-sistemas-parte1-02
---

# Atomic opm-curso-modelado-sistemas-parte1 - Segmento 02

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/artifacts/knowledge/_SCRIPTORIUM/INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt`
- Proposiciones: `48`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `02/07`

## Indice de fuentes

- `S01` · [fx_curso_modelado_sistemas_parte1.txt](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt) · fx curso modelado sistemas parte1

## fx curso modelado sistemas parte1 · Parte 1 / 03 Objects

- **P056** · `fact` · When modeling a system, the first thing we think about are objects. But, what are objects? · [src:S01:L91-L98](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L91-L98)
- **P057** · `fact` · Imagine landing at an airport after a long flight, and finding out that your luggage has not arrived. · [src:S01:L91-L98](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L91-L98)
- **P058** · `fact` · This can be especially annoying if you have an important job interview the next day, and your laptop, as well as the clothes you prepared for the interview, are in your suitcase! · [src:S01:L91-L98](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L91-L98)
- **P059** · `fact` · Being a good systems engineer, you begin to think about possible solutions to your problem. · [src:S01:L91-L98](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L91-L98)
- **P060** · `fact` · You start by looking around you, and you see many inanimate objects: service counters, conveyer belts, and the slip you received when you handed your luggage at your departure airport. · [src:S01:L91-L98](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L91-L98)
- **P061** · `exclusion` · You also see suitcases of all kinds, except for yours, of course! · [src:S01:L91-L98](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L91-L98)
- **P062** · `fact` · These are all called 'objects' in OPM, but this is the last of your concerns. · [src:S01:L91-L98](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L91-L98)
- **P063** · `fact` · Aside from inanimate objects, you can also see people · [src:S01:L91-L98](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L91-L98)
- **P064** · `fact` · a lot of them! Some are security guards, others are passengers like yourself, and others are airline crew members and service people. In OPM, people are also classified as objects. Along with inanimate objects and people, you can see many kinds of information items around you: information about flights on display screens, and directions to various airport destinations on big signs. Information items, which are of course not physical, are also classified as OPM objects. Luggage management systems are complex. You can model complex systems such as these using OPM. In OPM, objects are represented by rectangles with green borders. Here is what an object looks like in OPM. As we have said, the people in the airport, and people in general, are also objects, so we will also represent them using green rectangles. Information items, such as those displayed in the arriving flights information screen, are also represented by green rectangles. However, unlike physical objects, informatical objects in OPM are not shaded, indicating that they are logical, and therefore they do not occupy any physical space. Let's recap: this is what a physical object looks like in OPM, and this is the look of an informatical OPM object. For example, the suitcase is physical, so we will represent it as a shaded rectangle. The weight of the suitcase, however, is informatical, and will therefore be represented as a flat rectangle without shading. Equipped with knowledge of how physical and informatical objects are represented in OPM, we can get back to looking for our lost luggage! As we have seen, we are surrounded by objects. Moreover, we, people, are objects too! A good model depicts different kinds of objects - any object that is relevant to the system being modeled. The airplane, passengers, and crew are all physical objects, while the temperature, wind direction, and flight destination are all informatical objects. What is an Object? Let's call HopCat our helping cat. An object is a thing that exists or might exist physically or informatically. Thanks HopCat. Identifying the various objects around us will help us locate our suitcase and pass the job interview with flying colors. How can we do this? We will discuss this in the next video. · [src:S01:L99-L120](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L99-L120)

## fx curso modelado sistemas parte1 · Parte 1 / 05 Object States

- **P065** · `fact` · In the previous section, we found our lost suitcase, and now we continue on our way to your dream job interview for an engineer position at StoreDot - the fast-charging company. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P066** · `definition` · We found our lost suitcase, which means it has changed its state - from lost to found. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P067** · `fact` · Having explained what objects and processes are, the last piece of the puzzle for OPM is: States! So states is what we'll talk about now. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P068** · `fact` · Right now our goal is for you to get this wonderful job. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P069** · `definition` · This means your state will change from candidate to that of an employee. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P070** · `fact` · To understand this better, let's go back to the flight journey - the system we modeled previously. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P071** · `fact` · The passenger can be in a pre-ticketed state, or in a ticketed state. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P072** · `fact` · The passenger can be with a boarding pass; on board; and finally, at the destination airport. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P073** · `fact` · In each one of these cases, the passenger is at a different state. Watch the airplane landing. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P074** · `fact` · The airplane is an object, undergoing a process of landing. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P075** · `fact` · What are the states of airplane before and after landing? · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P076** · `fact` · First, it was in the air - airborne, and now it has landed and it is on the ground. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P077** · `fact` · The landing process changes the state of the airplane from airborne to landed. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P078** · `fact` · In OPM states are represented as “roundtangles”- rounded corner rectangles. Here is how it looks like. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P079** · `fact` · Note that since a state belongs to an object, graphically it can exist only within the object box. It has no meaning outside of this box. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P080** · `fact` · Your suitcase also changed states: first it was lost, and now it's found! · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P081** · `fact` · And I promise you, if you continue to learn conceptual modeling, you will soon make the state transition from candidate to employee. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P082** · `fact` · As we said previously, a state of an object is a specific situation of position that the object is in at some point in time. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P083** · `fact` · For example, an engineer in a company can be junior, senior, or R&D manager - these are all states. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P084** · `fact` · Every object in your system model can have any number of states - or even no states at all. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P085** · `fact` · Whether the object is stateful, that is it has states or stateless depends on what it is you want to model. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P086** · `fact` · For example, in the system where you are the object passenger and your flight is a process Flying, it made perfect sense to model your different situations such as onground and airborne as states. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P087** · `fact` · However, when modeling the airport's air-conditioning system; we do not need to add the states to passenger because they are not relevant to the problem at hand. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P088** · `fact` · However, the states hot, warm and cold of the terminal's indoor air, now become relevant. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P089** · `fact` · So we model them as states of the object Indoor Air. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P090** · `requirement` · The last thing we need to know about states is that if we modeled an object as stateful, then in any point in time it must be in at most one state. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P091** · `fact` · We say "at most" because if a process is currently transforming this object, then the object is in transition between two states. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P092** · `fact` · The "Input state" - the state it has left when the process started, and the "Output state" - the state it is going to enter once the process is over. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P093** · `fact` · For example, an airplane can be either airborne - up in the air, or landed - on the ground. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P094** · `fact` · The Landing process changes the state of the airplane from 'airborne' to 'landed' but this is not instantaneous. It normally does take a few seconds. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P095** · `fact` · During that short time, the airplane is no longer airborne but it has not yet landed. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P096** · `fact` · It is in transition between these two states. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P097** · `fact` · If we wish to focus on what happens during this short period of time, we can model this situation as a new, additional state, called touchdown, which takes place between the states "airborne" and "landed". Hold on! · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P098** · `fact` · While you're thinking about airplanes, be aware that your job interview is taking place in the next video. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P099** · `fact` · So, you need to change your location from the airport to the train station! · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P100** · `fact` · This change in your location is also a transition of states. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P101** · `fact` · And it's time for changing your employment status from candidate to having a great job in a wonderful company! And change your bank account balance too. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P102** · `fact` · Engineers who know how to model systems make more money. Hopcat.. psss...Hopcat.. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
- **P103** · `fact` · A state is a possible situation or position at which an object can be for some amount of time. · [src:S01:L126-L174](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte1.txt#L126-L174)
