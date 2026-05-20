---
_manifest:
  urn: urn:fxsl:kb:atomic-opm-curso-modelado-sistemas-parte2-01
  provenance:
    created_by: atomize
    created_at: '2026-04-24'
    source: /home/felix/kora/artifacts/knowledge/_SCRIPTORIUM/INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt
version: 1.0.0
status: borrador
tags:
- atomic
- knowledge
- opm-curso-modelado-sistemas-parte2
lang: es
extensions:
  kora:
    family: atomic
    atomic:
      producer: urn:kora:artefacto:atomize
      source_corpus: /home/felix/kora/artifacts/knowledge/_SCRIPTORIUM/INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt
      n_propositions: 40
      segmented: true
      segment_role: segment
      segment_index: 1
      segment_count: 6
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:fxsl:kb:atomic-opm-curso-modelado-sistemas-parte2-01
---

# Atomic opm-curso-modelado-sistemas-parte2 - Segmento 01

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/artifacts/knowledge/_SCRIPTORIUM/INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt`
- Proposiciones: `40`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `01/06`

## Indice de fuentes

- `S01` · [fx_curso_modelado_sistemas_parte2.txt](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt) · fx curso modelado sistemas parte2

## fx curso modelado sistemas parte2 · Parte 2 / Top level of model

- **P001** · `fact` · Introduction At the end of the previous section, you were accepted for the position of engineer. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P002** · `fact` · Your first assignment is to prepare a model for a robotics-based electric car manufacturing system. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P003** · `fact` · The CEO of your company is eager to see the result! · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P004** · `fact` · To get you started with your modeling assignment, let's watch these robots. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P005** · `fact` · They are performing hosting tasks to help celebrate the New Year with the Technion's President. So let's model this system! · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P006** · `fact` · Description The first step in modeling a system in OPM is to describe it so all the stakeholders can understand what the system is for and what it does, even if they lack domain expertise. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P007** · `fact` · This will help us communicate the system's function, structure and behavior to managers, customers, suppliers and experts from other fields. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P008** · `fact` · What we have just seen can be described as a system for picking, transporting, and serving fruit. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P009** · `fact` · In OPM, the overall description of the system is expressed in the first OPD we create, called the System Diagram or SD for short. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P010** · `requirement` · System Diagram SD aims to provide all the stakeholders with a top-level, bird's eye view of the system, It therefore must be simple and clear, with minimal technical details. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P011** · `fact` · SD has five components: purpose, function, enablers, environment, and problem occurrence. The first component is the system's purpose. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P012** · `fact` · Who are the beneficiaries (The people for whom the system was developed)? · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P013** · `fact` · What benefit does the system provide to them? · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P014** · `fact` · In our case, the purpose of the system is to provide people with fruit effortlessly. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P015** · `fact` · The second SD component is the system's main function: What is the main process and the object it transforms that together deliver the benefit? · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P016** · `fact` · Our system picks, transports, and delivers fruit. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P017** · `fact` · The third component, enablers, includes the objects that enable the system's main process: allowing the system to operate. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P018** · `fact` · There are two kinds of enablers: agents and instruments. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P019** · `fact` · Here, the instruments are the robots, the table, the table cloth, and the plate. Agents are always people. In our system, they operate the robots. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P020** · `fact` · The fourth SD component is the system's environment: what things - objects and processes - are not part of our system, but still affect its operation? · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P021** · `fact` · Here, we include the fruit trees and the robots transportation path. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P022** · `fact` · We can also include processes, such as 'wind blowing' and 'rain falling', which can also affect the system's operation. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P023** · `fact` · The fifth and last SD component is the problem occurrence. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P024** · `fact` · Any artificial system aims to solve some problem. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P025** · `fact` · In our case, people are hungry and want to eat fresh fruit without having to leave their seat! · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P026** · `fact` · The Technion's President, who benefited from the system, is an example of someone for whom we would usually present only the System Diagram, SD, with its five components. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P027** · `fact` · Your assignment is to present your CEO with the SD of the robotics-based electric cars manufacturing system. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P028** · `fact` · So let's order flight tickets to get to the robotics lab, and take the opportunity to model the SD of the flight tickets ordering system. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P029** · `fact` · Unlike the system we modeled before, which was physical, this system is informatical, as it focuses on ordering flight tickets, rather than actually flying. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P030** · `fact` · The system's website allows us to easily and quickly find and order flight tickets. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P031** · `fact` · The system's purpose is thus to shorten travelers time and improve their convenience of finding flights and ordering tickets. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P032** · `fact` · The function of the system is to change the status of a seat in a flight from available to purchased. and the instrument - the Website. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P033** · `fact` · The environment includes Internet connection, which is also an instrument of the main process. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P034** · `fact` · Finally, the problem this system solves is the difficulty of finding flights and ordering tickets. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P035** · `fact` · Let's summarize: when modeling SD, we represent five system components: Summary purpose, function, enablers, environment and problem occurrence. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P036** · `fact` · Using the online flight ticketing system, we now have tickets for our flight, and in the next video, we will meet at the airport. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P037** · `definition` · The System Diagram, SD, defines the system's purpose, scope, and main function in terms of its main object, main process, boundary, and stakeholders. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P038** · `fact` · SD aims to provide all the stakeholders with a top-level, bird's eye view of the system, focusing on its function and the benefit it delivers. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P039** · `requirement` · It therefore must be simple and clear, with minimal technical details. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
- **P040** · `fact` · A steakholder is an individual, a group of people or an organization, that has an interest in or might be affected by, a system. · [src:S01:L5-L78](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L5-L78)
