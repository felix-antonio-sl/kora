---
_manifest:
  urn: urn:fxsl:kb:atomic-opm-curso-modelado-sistemas-parte2-02
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
      n_propositions: 56
      segmented: true
      segment_role: segment
      segment_index: 2
      segment_count: 6
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:fxsl:kb:atomic-opm-curso-modelado-sistemas-parte2-02
---

# Atomic opm-curso-modelado-sistemas-parte2 - Segmento 02

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `/home/felix/kora/artifacts/knowledge/_SCRIPTORIUM/INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt`
- Proposiciones: `56`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `02/06`

## Indice de fuentes

- `S01` · [fx_curso_modelado_sistemas_parte2.txt](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt) · fx curso modelado sistemas parte2

## fx curso modelado sistemas parte2 · Parte 2 / System purpose

- **P041** · `fact` · Hello, dear engineer! · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P042** · `fact` · We are at the airport, on our way to the robotics lab. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P043** · `fact` · You were tasked by your CEO with modeling the top-level part of a model of a robotic system for manufacturing electric cars. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P044** · `fact` · Until we get to the check-in counter, let's spend some time to understand the system's "purpuse" -the first component of the System Diagram, or SD for short - the top-level view of our system model. Let's look around! · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P045** · `fact` · Many systems surround us, each with its own purpose. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P046** · `fact` · Artificial systems aim to benefit people: someone planned for whom the system will operate, and for what purpose. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P047** · `fact` · When describing an existing system, we start with the purpose. So let's begin modeling. First, we identify the beneficiaries. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P048** · `fact` · In an Airplane Flying system, the beneficiaries are the passengers. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P049** · `fact` · They benefit from the system by shortening the time it takes them to arrive at a distant location. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P050** · `fact` · To model the system purpose in SD, we first identify the Beneficiary Group. Here, we call them Passenger Group. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P051** · `requirement` · By OPM conventions, object names must be singular, so for humans, we represent plurality by adding the word ''Group'', and the group is single. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P052** · `fact` · Humans are physical, so the Passenger Group is represented in OPM as a physical object. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P053** · `definition` · Here comes HopCat to provide us with a definition. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P054** · `fact` · A beneficiary is a stakeholder who extracts value and benefits from the system. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P055** · `fact` · A beneficiary group is a group of two or more beneficiaries. Thank you, HopCat! · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P056** · `fact` · Now, we need to identify the Beneficiary Attribute. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P057** · `fact` · An OPM attribute is an informatical object, like this one. States of an attribute are called "values". · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P058** · `fact` · The Beneficiary Attribute is an attribute of the Beneficiary Group whose value changes, and this change benefits the Beneficiary Group. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P059** · `fact` · In an Airplane Flying system, this attribute of Passenger Group is Travel Time, and its possible values are long and short. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P060** · `fact` · Shortening the Travel Time through the Flying process is the benefit that the Passenger Group receives. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P061** · `fact` · Beneficiary attribute is an attribute that describes the beneficiary in terms of how she or he benefits from the system. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P062** · `fact` · To express the fact that Travel Time is an attribute of Passenger Group, let us introduce a new kind of structural relation - Exhibition-Characterization. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P063** · `fact` · This is the relation between a thing and its attribute. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P064** · `fact` · In our case, the object Passenger Group exhibits the attribute Travel Time. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P065** · `fact` · Graphically, this relation is the link depicted by a line with a black-in-white triangle along it. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P066** · `fact` · The tip of the triangle points to the exhibitor - the thing that exhibits the attribute, while the base of the triangle is connected to the attribute. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P067** · `fact` · Once we added this link to our model, a new OPL sentence was created: "Passenger Group exhibits Travel Time." Our time as engineers traveling to the robotics lab is precious, so we want to save as much time as possible. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P068** · `requirement` · The system's purpose is to save passengers travel time. How shall we describe this in OPM? · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P069** · `fact` · We will specify that Airplane Flying changes the value of Travel Time from long to short. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P070** · `fact` · First, we add long and short as two values of Travel Time. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P071** · `fact` · The new OPL sentence we now got is: "Travel Time of Passenger Group can be long or short." This is indeed what we wanted to say, so we are doing OK! · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P072** · `fact` · What changes the value of the Travel Time from long to short? The Flying process! · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P073** · `fact` · To express this, we will connect the two values of Travel Time to the Flying process using an input-output link pair, or in-out link pair, for short. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P074** · `fact` · The resulting OPL sentence reads: “Airplane Flying changes Travel Time of Passenger Group from long to short.” This sentence clearly expresses the system's purpose - exactly what we aimed to do!! · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P075** · `fact` · System purpose - A key benefit that an artificial system is expected to provide to its beneficiaries. Let's look around the airport. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P076** · `fact` · We should be able to identify the purpose of every system we see: shops, coffee houses, and the electronic flights information screen. What about the people around us? Is there a system that produces them? · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P077** · `fact` · People are created by an incredible natural system: the womb. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P078** · `fact` · Let's model this system in OPM and while doing this, learn an important difference between artificial and natural systems. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P079** · `fact` · Purpose relates to humans and their intentions and goals. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P080** · `fact` · In science, we analyze observations to understand root causes of natural and social phenomena. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P081** · `exclusion` · These were not designed by humans, so we cannot talk about purpose here. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P082** · `fact` · In model-based system engineering, we treat such phenomena as systems. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P083** · `fact` · We ascribe to a natural or social system an outcome rather than a purpose. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P084** · `fact` · The outcome of a natural system will depend on the modeler's objective and focus of research. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P085** · `fact` · Who is the beneficiary of the Fetus Developing system? The fetus. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P086** · `fact` · And what is the Beneficiary Attribute of Fetus? · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P087** · `definition` · We can define Developmental Stage as this attribute, with the values embryo and baby. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P088** · `fact` · But we can simplify our model by removing the Beneficiary Attribute and assigning embryo and baby as states of Fetus itself. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P089** · `fact` · Since Fetus is an object, which is not an attribute, embryo and baby are now states rather than values of Fetus. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P090** · `fact` · The updated OPL sentence is: "Fetus can be embryo or baby." Let's now add the main process, Fetus Developing, and connect it with the states of Fetus using an in-out link pair. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P091** · `fact` · The OPL sentence reads: “Fetus Developing changes Fetus from embryo to baby.” We couldn't say this better! · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P092** · `fact` · More examples of natural systems we could model are: Tree growing, the water cycle, and the cell division mechanism. HopCat seems anxious to jump in. Let's see what it wants to say. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P093** · `permission` · System outcome - A result or effect that a natural system can have on its “affectees”, which may be beneficial or detrimental. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P094** · `fact` · We're approaching the check-in counter, where we will hand in our suitcase and receive the boarding pass. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P095** · `fact` · Meanwhile, we have learned how to model the purpose of artificial systems and the outcome of natural ones. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
- **P096** · `fact` · In the next video, we will learn about another important aspect of SD - the main function of the system. · [src:S01:L82-L172](../../../INBOX/curso-dov-dori/fx_curso_modelado_sistemas_parte2.txt#L82-L172)
