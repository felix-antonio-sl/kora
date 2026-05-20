---
_manifest:
  urn: urn:fxsl:kb:atomic-opm-curso-modelado-sistemas-parte2-04
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
      n_propositions: 43
      segmented: true
      segment_role: segment
      segment_index: 4
      segment_count: 6
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:fxsl:kb:atomic-opm-curso-modelado-sistemas-parte2-04
---

# Atomic opm-curso-modelado-sistemas-parte2 - Segmento 04

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/artifacts/knowledge/_SCRIPTORIUM/INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt`
- Proposiciones: `43`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `04/06`

## Indice de fuentes

- `S01` · [fx_curso_modelado_sistemas_parte2.txt](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt) · fx curso modelado sistemas parte2

## fx curso modelado sistemas parte2 · Parte 2 / Process enablers

- **P149** · `fact` · We are about to take off! · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P150** · `fact` · Let's recap what we have done so far: When modeling the SD of any system in OPM, we should consider five components. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P151** · `fact` · We have already learned about two: Purpose and Function. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P152** · `fact` · Until our airplane takes off, let's learn about the third component: Enablers. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P153** · `fact` · Our pilots are waiting for confirmation from the air traffic control tower before taking off. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P154** · `fact` · Let's watch a video showing an air traffic control system. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P155** · `fact` · The crew at the air traffic control tower is responsible for controlling the traffic of airplanes in the airport. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P156** · `fact` · Airplanes can only take off with their approval, and only within specified routes. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P157** · `requirement` · Airplane landing is also coordinated and must be approved by an air traffic controller. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P158** · `fact` · Here is a simple model of an Air Traffic Controlling System. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P159** · `fact` · The system's purpose is to increase the safety of people within and around all the airplanes at the airport and in the airspace they are responsible for. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P160** · `fact` · The OPL sentence reads: "Air Traffic Controlling changes Safety Level of Human Group from low to high and Safety Level of Airplane Set from low to high." Since we do not use the plural form in OPM, we use Airplane Set instead of Airplanes, and Human Group instead of People. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P161** · `fact` · We convert humans to singular and add the word Group, while for anything other than humans we add the word Set. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P162** · `fact` · The function of the system, which attains the purpose of increasing the safety level, is to coordinate the flight routes of the airplanes. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P163** · `fact` · In OPL: "Air Traffic Controlling changes Flight Route Set of Airplane Set from uncoordinated to coordinated." In OPM, a human enabler of any process is a physical object called Agent. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P164** · `fact` · Agents are goal-oriented and have natural intelligence. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P165** · `fact` · Both Air Traffic Controller and a Pilot are agents of the Air Traffic Controlling process. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P166** · `fact` · The relation between an Agent and the process it enables is expressed graphically by an Agent link. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P167** · `fact` · This link has a solid circle at its enabled process end, and is therefore nicknamed “Black lollipop”. But hold on a second! · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P168** · `fact` · Is pilot part of the Air Traffic control system? · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P169** · `exclusion` · On one hand, we need pilots to enable the main process, but on the other hand, as systems engineers of the Air Traffic Control system, we cannot influence the pilots, as they are beyond the scope of our system. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P170** · `fact` · We will therefore designate Pilot as an environmental object, by changing its contour from solid to dashed. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P171** · `definition` · HopCat is always around to give us some definitions: An enabler is an object that is required for a process to occur. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P172** · `fact` · An agent is an enabler who is a human or a group of humans. Thanks, HopCat! · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P173** · `fact` · In addition to people, there are also non-human, usually inanimate objects that enable processes. These are instruments. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P174** · `fact` · The main instrument of Air Traffic Controlling is the Air Traffic Control Tower. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P175** · `fact` · A major instrument in the SD of any artificial system model is the system itself. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P176** · `fact` · As a default, the name of this instrument is the name of the system's function, or its main process, if it includes the transformee, followed by the word System. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P177** · `fact` · Thus, in our case, the instrument name would be: "Air Traffic Controlling System". · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P178** · `fact` · Often, the system has a commonly accepted name: "Air Traffic Control Tower" in our case, so we will use it instead. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P179** · `fact` · To designate an object as an instrument of a process, we use the instrument link. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P180** · `exclusion` · It is similar to the agent link, except that the circle at the process end is empty, giving it the nickname “White lollipop”. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P181** · `fact` · The OPL sentence reads: "Air Traffic Controlling requires Air Traffic Control Tower." Our airplane finally received approval to take off! Excellent! Let's get in line for boarding. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P182** · `fact` · I'm glad we were able to learn about enablers: Agents, who are always humans, and Instruments, which are inanimate objects. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P183** · `fact` · Unlike transformees, enablers of a process are not transformed by the process they enable, but like transformees, without them the process will not happen. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P184** · `fact` · Information systems, which are not physical, also have enablers. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P185** · `fact` · For example, "the MOOC"-Massive Open Online Course you are now taking, is an Instrument that enables your MOOC Learning process. Are you an agent of the main process? Yes! · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P186** · `fact` · But more importantly, you are also a transformee of MOOC Learning, as your knowledge level of Model-Based Systems Engineering with OPM hopefully increases. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P187** · `fact` · Back to our learning system, its purpose is expressed by the OPL sentence: "MOOC Learning changes Knowledge Level of Learner Group from low to high" The function of the system is expressed by the sentence: "MOOC Learning changes Study Stage of MOOC of Student Group from registered to completed." The agent of the MOOC Learning process is Learner Group. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P188** · `fact` · In OPL: "Learner Group handles MOOC Learning." The instrument of the main process is the MOOC. MOOC Learning requires MOOC. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P189** · `fact` · MOOC is also the Benefit-Providing object in our system! Did you fasten your seatbelt? · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P190** · `fact` · Excellent, we're over the airport, landing any minute now. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
- **P191** · `fact` · When we leave the airport, while we wait for our suitcase to hopefully show up, we will go through the fourth component of the SD: the system's Environment. See you soon. · [src:S01:L273-L359](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L273-L359)
