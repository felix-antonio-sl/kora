---
_manifest:
  urn: urn:fxsl:kb:atomic-opm-curso-modelado-sistemas-parte4-01
  provenance:
    created_by: atomize
    created_at: '2026-04-24'
    source: /home/felix/kora/artifacts/knowledge/_SCRIPTORIUM/INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt
version: 1.0.0
status: borrador
tags:
- atomic
- knowledge
- opm-curso-modelado-sistemas-parte4
lang: es
extensions:
  kora:
    family: atomic
    atomic:
      producer: urn:kora:artefacto:atomize
      source_corpus: /home/felix/kora/artifacts/knowledge/_SCRIPTORIUM/INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt
      n_propositions: 43
      segmented: true
      segment_role: segment
      segment_index: 1
      segment_count: 2
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:fxsl:kb:atomic-opm-curso-modelado-sistemas-parte4-01
---

# Atomic opm-curso-modelado-sistemas-parte4 - Segmento 01

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/artifacts/knowledge/_SCRIPTORIUM/INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt`
- Proposiciones: `43`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `01/02`

## Indice de fuentes

- `S01` · [fx_curso_modelado_sistemas_parte4.txt](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt) · fx curso modelado sistemas parte4

## fx curso modelado sistemas parte4 · Parte 4 / System diagram 1

- **P001** · `fact` · Your journey as a successful engineer and an expert in systems modeling continues. · [src:S01:L5-L28](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L5-L28)
- **P002** · `fact` · Now, the company is asking you to adapt the autonomous car for driving in various weather conditions, including a rainstorm. · [src:S01:L5-L28](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L5-L28)
- **P003** · `fact` · Therefore, your task now is to develop a weather simulation system. · [src:S01:L5-L28](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L5-L28)
- **P004** · `fact` · Your first assignment is to model a rainstorm system. · [src:S01:L5-L28](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L5-L28)
- **P005** · `fact` · Unlike most of the systems we have modeled so far, a rainstorm is a natural system, not an artificial one. What's the difference, you ask? · [src:S01:L5-L28](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L5-L28)
- **P006** · `fact` · The top-level diagram of the model, SD, of a natural system shares three components with an artificial system: main function, main process enablers, and system environment, but the system purpose and problem creation are usually not relevant for a natural system. · [src:S01:L5-L28](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L5-L28)
- **P007** · `fact` · A natural system was not designed by humans, and therefore, in such systems we refer to the outcome rather than the purpose of the system. · [src:S01:L5-L28](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L5-L28)
- **P008** · `fact` · For a similar reason, problem creation is not relevant to the SD of a natural system. So let's start modeling a rain storm system! · [src:S01:L5-L28](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L5-L28)
- **P009** · `fact` · To do that, we are going to watch a couple of short videos made by NASA, the US National Aeronautics and Space Administration. · [src:S01:L5-L28](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L5-L28)
- **P010** · `fact` · NASA does not only explore outer space, but also the earth. · [src:S01:L5-L28](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L5-L28)
- **P011** · `fact` · Monitoring the weather is a major NASA activity, and an important part of it is monitoring the formation of various kinds of rain systems. · [src:S01:L5-L28](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L5-L28)
- **P012** · `fact` · A tropical rain system, for example, begins in the ocean, as we can see in the video. · [src:S01:L5-L28](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L5-L28)
- **P013** · `permission` · can develop into a dangerous storm that causes floods and other damages. So what is the outcome of our modeled system? This depends on our point of view, and what we are interested in. Let's start modeling by depicting the main process of the system - Rain Storm Forming. What is the beneficiary group of the system? although it is doubtful that the rain is causing them any pleasure :) This will happen later, when the car we are designing will get through the storm, and the passengers will remain dry. So as we see, the outcome of a natural system for the beneficiary group, can be positive, a benefit or negative -detrimental or damaging A human made system - the car in our case - will be designed to minimize or eliminate that damage, but right now our focus is on the natural system. What attribute of the beneficiary group is transformed as a result of the main process? Since we are interested first and foremost in safety, we can say that the safety level of the passenger decreases as a result of the rain storm forming. This is indeed a detriment! We will validate this by reading the OPL sentence: "Rain Storm Forming changes Safety Level of Passenger Group from high to low''." Natural System outcome: A key effect that a natural system has on its affectees, which may be beneficial or detrimental. Thanks, HopCat! Now, let's turn to the system's main function · [src:S01:L30-L54](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L30-L54)
- **P014** · `fact` · what is the main transformee of the system? In our case, we are focusing on the car's surrounding atmosphere, so we can say it changes from ''dry'' to ''rainy''. What about the main process enablers? Natural systems, in which people are not involved, do not have agents. Indeed, no person is involved in forming the storm. And what about instruments? Well, a tropical rainstorm forms above an ocean with warm water, so we will add ''Warm Ocean Water'' as an instrument of the main process. The OPL sentence describes the main process enabler: “Rain Storm Forming requires Warm Ocean Water.” Now, let's turn to the system's environment. What is the meaning of environment for a natural system? In a technological system, we distinguished between systematic things, over which developers and operators have control, and environmental things, which affect the system, but over which we have no control. How will we distinguish between systemic and environmental things in a natural system? In our case, we want to understand how a rain system forms. Therefore, anything outside of the storm, but which still affects it, will be included in the system environment. A tropical rainstorm depends on the existence of an ocean and the Earth's atmosphere. We will therefore add the ocean and the atmosphere as environmental objects, and connect the atmosphere as an instrument to the main process - the storm requires the atmosphere air. Of course, Warm Ocean Water is part of Ocean. We will express this using an aggregation-participation link. A systemic thing can be part of an environmental thing, as is the case here. Good! We modeled the SD of a rain forming system. Next time, we will model the sub-processes of the main process. See you soon! · [src:S01:L55-L83](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L55-L83)

## fx curso modelado sistemas parte4 · Parte 4 / System diagram 2

- **P015** · `fact` · Having modeled a technological system - a car, and a natural system - a rain storm you are now assigned to organize a conference on autonomous cars, Modeling the conference system, will be an opportunity to see how OPM can be used to model social systems, such as a public debate, a family, or a community. · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P016** · `fact` · A social system is artificial much like a technological one. · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P017** · `fact` · And as such, modeling its SD involves the same components: purpose, main function, enablers, environment and problem occurrence. · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P018** · `fact` · So, let’s start modeling your small conference! First, what is the system's purpose? · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P019** · `fact` · The CEO is expecting the conference to increase business cooperation and improve company's success. · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P020** · `fact` · Who are the main beneficiaries? supplies, providers and employees, including you, of course! In short - the company stakeholders. HopCat, can you explain this please? · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P021** · `fact` · A stakeholder, or stakeholder group is an individual, an organization, or a group of people that has an interest in, or might be affected by, a system. Thank you HopCat! · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P022** · `fact` · The attribute of the Beneficiary Group is Business Success with the values: current and improved. What is the main process? Conference Occurring. · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P023** · `fact` · As usual, we will check our model by reading the OPL sentence that was just created: “Conference Occurring changes Business Success of Company Stakeholder Group from current to improved” Good! This was what we wanted to say. · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P024** · `fact` · Having modeled the system's purpose, let's model the main function of the system. · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P025** · `fact` · The main function of the system is increasing the business cooperation for the company's stakeholders. · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P026** · `fact` · Before the conference, business cooperation was loose, and following the conference, business cooperation is tight. · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P027** · `fact` · The OPL sentence says: “Conference occurring changes Business Cooperation of company stakeholder group from loose to tight.” Very good! · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P028** · `fact` · Now, let's turn to the enablers of the main process. · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P029** · `fact` · Our conference does not have a dedicated instrument, but meeting room, tables, chairs, stages, and audio-visual accessories are all instruments. . We aggregate these objects as “Equipment”. · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P030** · `fact` · Of course, there are also agents: you - the organizer, and Ushers, who register attendees and ensure that the conference runs smoothly. · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P031** · `fact` · The OPL sentences read: ''Conference occurring requires Equipment.'' ''Organizer and Usher Group handle Conference Occurring'' Good! What about the system environment? Well, the weather is one of them. · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P032** · `fact` · We would not want to have a conference on a day with rain, snow or storm, because many people will not show up! · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P033** · `fact` · So we include Weather with states good and bad as environmental instrument. · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P034** · `fact` · Up until now, we connected the source of an enabling link to an object and the destination to the enabled process. · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P035** · `fact` · Here, we can be more specific, and connect the source to a particular state of the enabler. · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P036** · `fact` · Let's do it now: we connect the state 'good' of Weather to Conference Occurring. · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P037** · `fact` · The last remaining component is problem occurrence. · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P038** · `fact` · The CEO, sees his company's business declining, as more companies enter the market. · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P039** · `fact` · Business Declining is the environmental process that causes the problem. · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P040** · `fact` · The CEO is seeking to increase business cooperation - which will lead to improved business success. · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P041** · `fact` · The new OPL sentence reads: ''Business Declining yields Business Success of Company Stakeholder Group at state curent and Business Cooperation at state loose. Good! · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P042** · `fact` · We are done modeling SD, the top view of the system. · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
- **P043** · `fact` · Next time, we will model SD1, the first detail level. See you soon! · [src:S01:L87-L145](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L87-L145)
