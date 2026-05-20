---
_manifest:
  urn: urn:fxsl:kb:atomic-opm-curso-modelado-sistemas-parte2-05
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
      n_propositions: 41
      segmented: true
      segment_role: segment
      segment_index: 5
      segment_count: 6
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:fxsl:kb:atomic-opm-curso-modelado-sistemas-parte2-05
---

# Atomic opm-curso-modelado-sistemas-parte2 - Segmento 05

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/artifacts/knowledge/_SCRIPTORIUM/INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt`
- Proposiciones: `41`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `05/06`

## Indice de fuentes

- `S01` · [fx_curso_modelado_sistemas_parte2.txt](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt) · fx curso modelado sistemas parte2

## fx curso modelado sistemas parte2 · Parte 2 / System boundary and environment

- **P192** · `fact` · We have landed at our destination, and we are waiting for our suitcases before hitting the road to the robotics lab! · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P193** · `fact` · There, we hope to get ideas for how to develop an automated system for manufacturing electric cars. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P194** · `fact` · When describing an existing system, or designing a new one, it is important to understand not just the elements of the system, but also its environment. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P195** · `fact` · The system interacts with its environment, which, in turn, affects the operation of the system. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P196** · `fact` · So as we are walking to the baggage claim area, let's talk about the system's environment. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P197** · `fact` · Look at SD of the Airplane Flying system, we can try to identify what environmental Things - Objects and Processes - affect its operation. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P198** · `fact` · We see that the Takeoff and Landing processes require the approval of the Air Traffic Control Tower. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P199** · `fact` · In our Air Traffic Controlling System model, the Air Traffic Control Tower is, of course, systemic: it is the main object in the system we are modeling. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P200** · `fact` · However, in the Airplane Flying system, the Air Traffic Control Tower is beyond our control. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P201** · `fact` · We, as the systems engineers of the Airplane Flying System, have no influence over the Air Traffic Control Tower. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P202** · `requirement` · But, we certainly must take it into consideration when modeling our Airplane Flying System. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P203** · `requirement` · Therefore, we shall designate it as an environmental object. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P204** · `fact` · Most things in our model are systemic, not environmental. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P205** · `fact` · Systemic things are represented by a solid contour, while environmental ones - by a dashed contour. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P206** · `fact` · Affiliation is the attribute of a Thing whose values are systemic and environmental. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P207** · `fact` · The system's boundary is an imaginary border in the system model that separates things whose Affiliation is systemic from those with environmental Affiliation. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P208** · `definition` · Here comes cute HopCat to help us nail down a couple of definitions. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P209** · `fact` · Thing Affiliation: An attribute of a thing that specifies or environmental - part of the system's environment. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P210** · `fact` · System Boundary: An imaginary border in the system model that separates systemic things from environmental ones. Well said, HopCat! · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P211** · `fact` · We have just arrived at the baggage claim area, so you should start looking for your suitcase. I will help you! · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P212** · `fact` · Here is SD of the Baggage Transporting System. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P213** · `fact` · The environment of this system includes, for example, the electrical energy needed for moving the conveyer belt. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P214** · `fact` · As developers or operators of this system, we have no control over the airport's electricity supply. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P215** · `fact` · Yet, it is very important to include electrical energy in our model, because without it, passengers will not get their baggage! · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P216** · `fact` · The relevant OPL sentences read: "Electrical Energy is environmental." "Baggage Transporting requires Electrical Energy." That is not your suitcase... · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P217** · `fact` · The one coming our way is not yours either... there it is! Pick it up! Quickly! Great! We are now ready to go! · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P218** · `fact` · Let's get in the electric car and drive to the robotics lab. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P219** · `fact` · Have you ever driven a car designed for dirt roads? · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P220** · `fact` · Driving on a dirt road is more difficult than driving on a paved road. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P221** · `requirement` · It is important that we identify the system's environment, because this is where our system shall operate, so our design must account for its conditions. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P222** · `fact` · The type of terrain the car is supposed to drive on is an example of the electric car system's environment. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P223** · `fact` · The environment of an electric car system also includes things that are informatical rather than physical. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P224** · `requirement` · For example, developing an electric car must account for the regulations - the laws of the target market countries. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P225** · `fact` · The type of terrain and regulations are not part of the Electric Car Driving System, but they can certainly affect the design and operation of the system. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P226** · `fact` · This is true in general: environmental things affect the operation of the system we are designing or describing, Let's examine the SD of the Electric Car Driving System model, and add to it the two environmental objects: Terrain and Regulation Set. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P227** · `fact` · These are the elements of the system's purpose. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P228** · `fact` · These are the main function's elements, and here are the enablers of the main process. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P229** · `fact` · Now, let's add to our model the object Terrain, which is physical as well as environmental. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P230** · `fact` · And now we will add Regulation Set as an informatical and environmental object. · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P231** · `fact` · Our SD now shows the system's purpose, its main function, the enablers of the main process, and objects in the system's environment. We are on track to completing the SD! · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
- **P232** · `fact` · With the knowledge you acquired, you are ready to visit the robotics lab and model a robotics-based system for manufacturing electric cars that you will be proud to present to your CEO. This will happen when we meet next time. Mark your calendar 😉 · [src:S01:L363-L433](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L363-L433)
