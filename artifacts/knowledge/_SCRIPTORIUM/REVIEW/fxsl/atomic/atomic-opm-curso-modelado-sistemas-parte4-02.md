---
_manifest:
  urn: urn:fxsl:kb:atomic-opm-curso-modelado-sistemas-parte4-02
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
      n_propositions: 39
      segmented: true
      segment_role: segment
      segment_index: 2
      segment_count: 2
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:fxsl:kb:atomic-opm-curso-modelado-sistemas-parte4-02
---

# Atomic opm-curso-modelado-sistemas-parte4 - Segmento 02

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/artifacts/knowledge/_SCRIPTORIUM/INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt`
- Proposiciones: `39`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `02/02`

## Indice de fuentes

- `S01` · [fx_curso_modelado_sistemas_parte4.txt](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt) · fx curso modelado sistemas parte4

## fx curso modelado sistemas parte4 · Parte 4 / System diagram 3

- **P044** · `fact` · The conference you organized and modeled in the previous videos was a great success! · [src:S01:L149-L177](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L149-L177)
- **P045** · `fact` · Now, we need to begin managing the relationships you created there. This is what Social Networks are for. So how do we model such a network? · [src:S01:L149-L177](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L149-L177)
- **P046** · `fact` · A system like this is a socio-technical system. · [src:S01:L149-L177](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L149-L177)
- **P047** · `fact` · An artificial system, which integrates technological and social aspects. · [src:S01:L149-L177](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L149-L177)
- **P048** · `fact` · As we can see, a registered user can manage the user profile, send messages to other users, and look for jobs. · [src:S01:L149-L177](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L149-L177)
- **P049** · `fact` · Modeling As always, we will start modeling with the purpose of the system and its main process. · [src:S01:L149-L177](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L149-L177)
- **P050** · `fact` · The main process is: "Online Professional Identity Managing''. and the benefit you get from the system is improved professional success. · [src:S01:L149-L177](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L149-L177)
- **P051** · `fact` · The OPL sentence reads: “Online Professional Identity Managing changes Professional Success of user from current to improved.” Very good! What about the function of the system? · [src:S01:L149-L177](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L149-L177)
- **P052** · `fact` · The system enables managing an online professional profile. · [src:S01:L149-L177](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L149-L177)
- **P053** · `fact` · Let's review what we did by reading the OPL sentence: “Online Professional Identity Managing changes Online Professional Profile of user from unmanaged to managed“ Review The professional profile represents you! A physical user. · [src:S01:L149-L177](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L149-L177)
- **P054** · `fact` · To express this let's get familiar with the tag structural link. · [src:S01:L149-L177](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L149-L177)
- **P055** · `fact` · We use this kind of link when we wish to express a structural relation between Things, for which none of the fundamental structural relations is appropriate. · [src:S01:L149-L177](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L149-L177)
- **P056** · `constraint` · We allreay learned about 3 of the 4 fundamental structural relations: · [src:S01:L149-L177](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L149-L177)
- **P057** · `definition` · aggregation-participation, exhibition-characterization and generalization-specialization. In a tagged structural relation, we, as modelers, can insert any structural relation in order to express the meaning of the relation. So here, we add the word “represents” as our user-defined tag. The OPL sentence will simply be the concatenation of the source thing name, the tag, and the destination thing name. Indeed, as we can see here, the new OPL sentence reads: “Online Professional Profile represents User.” Nice! Here comes HopCat with a definition. A tagged structural link is structural link with a tag recorded along it, describing the nature of the relation between the linked things. Great! Now let's model the enablers of the main process. As we always do when modeling technological systems, we will add the instrument "Online Professional Identity Managing System'' to SD. One agent of the main process is, of course, the user. Since there is no point in a one-person social network, we will add ''Other User Group'' as another agent. What about environmental Things? Well, to use the system, we must be connected to the Internet, so we add it as an environmental instrument of the main process. And what about the problem which the system solves? The growing dynamicity of the professional and business world is growing. Career management requires that we keep in touch with people from around the world, so we can be constantly updated on advances in our field. Managing one's identity exclusively offline, with no online presence is no longer viable for achieving professional success! We will therefore add the environmental process Offline Professional Identity Managing. Let's show how this process causes the problem. The new OPL sentences read: "Offline Professional Identity Managing yields Professional Success of User at state current and Online Professional Profile at state unmanaged. " Next time, we will continue modeling this system's first detailed level, SD1. and learn how to manage your professional identity! · [src:S01:L178-L212](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L178-L212)

## fx curso modelado sistemas parte4 · Parte 4 / Recapitulación hasta parte 4

- **P058** · `fact` · Welcome Hello, friends. · [src:S01:L216-L259](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L216-L259)
- **P059** · `fact` · We have completed the first stage of our journey together. · [src:S01:L216-L259](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L216-L259)
- **P060** · `fact` · I'm proud of you for getting here, and I hope you will continue with me to the advanced course. · [src:S01:L216-L259](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L216-L259)
- **P061** · `fact` · For now, let's stop and look with pride at what we have accomplished so far. · [src:S01:L216-L259](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L216-L259)
- **P062** · `fact` · You began without knowledge of conceptual modeling and no job in systems engineering, but you quickly learned how to model different systems. · [src:S01:L216-L259](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L216-L259)
- **P063** · `fact` · Recap Remember how we lost your luggage at the start of our journey? · [src:S01:L216-L259](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L216-L259)
- **P064** · `fact` · Not only did you end up retrieving it, but you also got a job as an engineer in an exciting company that develops and manufactures fast-charging electric car batteries. · [src:S01:L216-L259](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L216-L259)
- **P065** · `fact` · You learned a highly expressive yet compact conceptual modeling language - OPM. · [src:S01:L216-L259](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L216-L259)
- **P066** · `fact` · We had some coffee and you modeled a coffee making system. · [src:S01:L216-L259](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L216-L259)
- **P067** · `fact` · We got to know some airports around the world, and we modeled an airplane flying system too. · [src:S01:L216-L259](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L216-L259)
- **P068** · `fact` · We also modeled ways to manufacture cars using advanced robots. · [src:S01:L216-L259](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L216-L259)
- **P069** · `fact` · On our way, we gained valuable insights about biological systems and their models from a Nobel laureate. · [src:S01:L216-L259](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L216-L259)
- **P070** · `fact` · We learned and modeled how autonomous driving systems detect dangers on the road, how hurricanes are formed, how to plan conferences, and how to manage professional relationships! · [src:S01:L216-L259](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L216-L259)
- **P071** · `requirement` · Hotcut And of course, we must thank our loyal friend, HopCat! · [src:S01:L216-L259](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L216-L259)
- **P072** · `exclusion` · For me, this journey has been an exceptional and challenging experience. · [src:S01:L216-L259](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L216-L259)
- **P073** · `fact` · I was happy to leave the research laboratory and lecture halls to meet you through the small screen and help advance your career while developing your systems thinking and conceptual modeling skills. · [src:S01:L216-L259](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L216-L259)
- **P074** · `fact` · I think you will find what you have learned useful for solving problems, planning and performing projects, and facing various other challenges during your professional lives. · [src:S01:L216-L259](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L216-L259)
- **P075** · `fact` · This is an appropriate opportunity to thank our invaluable team that has worked tirelessly to make all this knowledge accessible to you in the best way possible: Dr. · [src:S01:L216-L259](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L216-L259)
- **P076** · `fact` · Rea Lavi for managing the instructional design of this course, Mr. · [src:S01:L216-L259](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L216-L259)
- **P077** · `fact` · Kave Shafran for advising us on the media approach to make this course highly engaging, Dr. Niva Wengrowicz and Dr. · [src:S01:L216-L259](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L216-L259)
- **P078** · `fact` · Ahmad Jbara, the lecturers of the Hebrew and Arabic versions of this course, Shai Granot, our capable photographer, Hanan Kohen, Galina Katsev, Ziv Krimberg and others who contributed, each in her or his way, to the success of this course. · [src:S01:L216-L259](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L216-L259)
- **P079** · `fact` · Conclusion I hope you will continue with us to the next part of the course "Advanced Approaches to Systems Engineering with OPM''. · [src:S01:L216-L259](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L216-L259)
- **P080** · `fact` · In this course, we will learn how to model complex behaviors and control structures like iterations, events, conditions, and probabilities, while studying fascinating systems like the International Space Station!” Finally, I would like to thank you for being with us. · [src:S01:L216-L259](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L216-L259)
- **P081** · `fact` · I'm Dov Dori, the inventor of Object-Process Methodology, and a Professor at the Technion and the Massachusetts Institute of Technology. It has been my privilege to be your mentor. · [src:S01:L216-L259](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L216-L259)
- **P082** · `fact` · Please, leave your feedback about the Foundations Course in the forum. Say goodbye, HopCat! We will meet again soon. · [src:S01:L216-L259](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte4.txt#L216-L259)
