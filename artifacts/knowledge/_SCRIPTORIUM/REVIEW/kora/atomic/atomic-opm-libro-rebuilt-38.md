---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-38
  provenance:
    created_by: atomize
    created_at: '2026-04-18'
    source: /home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt
version: 1.0.0
status: draft
tags:
- atomic
- knowledge
- opm-libro-rebuilt
lang: es
extensions:
  kora:
    family: atomic
    atomic:
      producer: urn:kora:skill:atomize:1.0.0
      source_corpus: /home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt
      n_propositions: 54
      segmented: true
      segment_role: segment
      segment_index: 38
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-38
---

# Atomic opm-libro-rebuilt - Segmento 38

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `54`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `38/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 13 The Dynamic System Aspect / 13.5.3 Enabling Links: Agent and Instrument Links

- **P1985** · `fact` · Enables are linked to processes through enabling links. · [src:S01:L5123-L5155](../../../INBOX/opm-libro.txt#L5123-L5155)
- **P1986** · `fact` · An enabling link is a procedural link that connects a process with an enabler of that process. · [src:S01:L5123-L5155](../../../INBOX/opm-libro.txt#L5123-L5155)
- **P1987** · `fact` · An agent link is an enabling link that connects a process with an agent of that process. · [src:S01:L5123-L5155](../../../INBOX/opm-libro.txt#L5123-L5155)
- **P1988** · `fact` · An instrument link is a procedural link that connects a process with an enabler of that process. Graphically, as Fig. · [src:S01:L5123-L5155](../../../INBOX/opm-libro.txt#L5123-L5155)
- **P1989** · `constraint` · 13.7 shows, an enabling link is a “lollipop”, a line leading from the enabler (Baker) to the process (Cake Making) it enables, which ends with a circle touching the process side. · [src:S01:L5123-L5155](../../../INBOX/opm-libro.txt#L5123-L5155)
- **P1990** · `fact` · If the enabler is a human or a group of humans, the enabling link is an agent link, denoted as a “black lollipop”, i.e., its ending circle is filled in (black). · [src:S01:L5123-L5155](../../../INBOX/opm-libro.txt#L5123-L5155)
- **P1991** · `fact` · The distinction between a human and a non-human enabler is important, since for humans to interact with the system, a dedicated interface needs to be designed. · [src:S01:L5123-L5155](../../../INBOX/opm-libro.txt#L5123-L5155)
- **P1992** · `constraint` · Hence, an optional stick figure can be added at the top-left corner of the agent’s object symbol, as shown in Fig. 13.7. · [src:S01:L5123-L5155](../../../INBOX/opm-libro.txt#L5123-L5155)
- **P1993** · `requirement` · This optional stick figure is especially useful when the human in the model is an affectee, i.e., she or he is affected by the process to which it is linked, in which case we must use the effect link rather than the agent link. · [src:S01:L5123-L5155](../../../INBOX/opm-libro.txt#L5123-L5155)
- **P1994** · `fact` · In this case, the stick figure retains the information that a human is involved. · [src:S01:L5123-L5155](../../../INBOX/opm-libro.txt#L5123-L5155)
- **P1995** · `fact` · If the enabler is an instrument, the enabling link is a “white lollipop”, i.e., its ending circle is blank (white). · [src:S01:L5123-L5155](../../../INBOX/opm-libro.txt#L5123-L5155)
- **P1996** · `fact` · The two OPL sentences associated with these links are: Agent handles Processing. Processing requires Instrument. · [src:S01:L5123-L5155](../../../INBOX/opm-libro.txt#L5123-L5155)
- **P1997** · `fact` · The OPL syntax of the first (agent) sentence is designed such that the agent appears first, followed by the reserved OPL phrase handles, followed by the process name. · [src:S01:L5123-L5155](../../../INBOX/opm-libro.txt#L5123-L5155)
- **P1998** · `fact` · For the instrument sentence, the OPL syntax is such that the process name appears first, followed by the reserved OPL phrase requires, followed by the instrument name. · [src:S01:L5123-L5155](../../../INBOX/opm-libro.txt#L5123-L5155)
- **P1999** · `fact` · This difference in both the OPL phrases and the order of the enablers in the sentences underlines that being humans, agents are more important than instruments. · [src:S01:L5123-L5155](../../../INBOX/opm-libro.txt#L5123-L5155)
- **P2000** · `requirement` · All the process enablers must be present throughout the execution of the process which they enables. For example, in Fig. · [src:S01:L5123-L5155](../../../INBOX/opm-libro.txt#L5123-L5155)
- **P2001** · `requirement` · 13.7 both the agent Baker and the instrument Oven must be present throughout a Cake Baking process. affectee of Servicing · [src:S01:L5123-L5155](../../../INBOX/opm-libro.txt#L5123-L5155)

## opm libro · Chapter 13 The Dynamic System Aspect / 13.5.4 Enabler Versus Affectee

- **P2002** · `fact` · Enabler and affectee are possible roles that an object plays with respect to some processes. · [src:S01:L5157-L5164](../../../INBOX/opm-libro.txt#L5157-L5164)
- **P2003** · `fact` · The same object can be an enabler for one process but not for another, or it can be an enabler for one process and an affectee for another. · [src:S01:L5157-L5164](../../../INBOX/opm-libro.txt#L5157-L5164)
- **P2004** · `fact` · For example, the (environmental) process Servicing in Fig. · [src:S01:L5157-L5164](../../../INBOX/opm-libro.txt#L5157-L5164)
- **P2005** · `constraint` · 13.8, which the moving company applies periodically to its Moving Truck, changes the state of Moving Truck from in need of service to serviced, hence Moving Truck is an affectee of Servicing. · [src:S01:L5157-L5164](../../../INBOX/opm-libro.txt#L5157-L5164)
- **P2006** · `fact` · However, with respect to the (systemic) process Moving, Moving Truck is an enabler—an instrument for Moving, while Location of Furniture is an affectee, as Moving changes the value (attribute state) of the Location attribute of Furniture from old apartment to new apartment. · [src:S01:L5157-L5164](../../../INBOX/opm-libro.txt#L5157-L5164)

## opm libro · Chapter 13 The Dynamic System Aspect / 13.6 The Preprocess and Postprocess Object Sets

- **P2007** · `fact` · Recall that the involved object set is the union of the preprocess object set and postprocess object set. As Fig. · [src:S01:L5166-L5188](../../../INBOX/opm-libro.txt#L5166-L5188)
- **P2008** · `constraint` · 13.9 shows, if the involved object-set contains enablers (agents and/or instruments), they are common to the preprocess and postprocess object sets, because their presence is required throughout the duration of the process they enable. · [src:S01:L5166-L5188](../../../INBOX/opm-libro.txt#L5166-L5188)
- **P2009** · `fact` · Each process has its own involved object set, preprocess object set, and postprocess object set, and each can contain any number of objects. · [src:S01:L5166-L5188](../../../INBOX/opm-libro.txt#L5166-L5188)
- **P2010** · `fact` · Affectees are also common to the pre-process and post-process object sets, because they had existed before the affecting process started and remain existent after this process ended. · [src:S01:L5166-L5188](../../../INBOX/opm-libro.txt#L5166-L5188)
- **P2011** · `fact` · Consumees disappear, so they belong only to the pre-process object set, while resultees are created, so they belong only to the post- process object set. · [src:S01:L5166-L5188](../../../INBOX/opm-libro.txt#L5166-L5188)
- **P2012** · `fact` · The Preprocess Object Set and the Postprocess Object Set are not necessarily disjoint—they may be overlapping. Indeed, in Fig. · [src:S01:L5166-L5188](../../../INBOX/opm-libro.txt#L5166-L5188)
- **P2013** · `constraint` · 13.9, the overlapping members are the two enablers—Agent and Instrument, and one transformee—the Affectee. · [src:S01:L5166-L5188](../../../INBOX/opm-libro.txt#L5166-L5188)
- **P2014** · `fact` · Agent and Instrument might belong to both object sets, because, by their definition, being enablers, they are required throughout the process (and are not supposed to change as a result of the occurrence of the process they enable). · [src:S01:L5166-L5188](../../../INBOX/opm-libro.txt#L5166-L5188)
- **P2015** · `fact` · Affectee belongs to both the preprocess object set and postprocess object set, because it continues to exist after the process occurred, albeit in a different state. · [src:S01:L5166-L5188](../../../INBOX/opm-libro.txt#L5166-L5188)
- **P2016** · `fact` · Consumee is the only involved object which is not in the Postprocess Object Set, because the Processing process consumed it, so it does not exist after Processing terminated. · [src:S01:L5166-L5188](../../../INBOX/opm-libro.txt#L5166-L5188)
- **P2017** · `fact` · In an anti-symmetric manner, Resultee is the only involved object which is not in the Preprocess Object Set, because Processing generated it, so it did not exist prior to the beginning of Processing. · [src:S01:L5166-L5188](../../../INBOX/opm-libro.txt#L5166-L5188)
- **P2018** · `constraint` · The procedural links are summarized in Table 13.1. · [src:S01:L5166-L5188](../../../INBOX/opm-libro.txt#L5166-L5188)

## opm libro · Chapter 13 The Dynamic System Aspect / 13.7 State-Specified Procedural Links

- **P2019** · `fact` · It is often the case that we wish to specify in our model not just that an object is transformed or that it enables a process, but also at what state an enabler has to be in order for it to enable the process. · [src:S01:L5190-L5205](../../../INBOX/opm-libro.txt#L5190-L5205)
- **P2020** · `fact` · We may also wish to be able to specify not just the object that a process generates, but also the particular state at which that object is generated as a result of the occurrence of a process. · [src:S01:L5190-L5205](../../../INBOX/opm-libro.txt#L5190-L5205)
- **P2021** · `fact` · Likewise, one may wish to specify not just what object a process consumes, but also the particular state that the object needs to be at in order for the process to be able to consume it. · [src:S01:L5190-L5205](../../../INBOX/opm-libro.txt#L5190-L5205)
- **P2022** · `fact` · State-specified procedural links provide for this. · [src:S01:L5190-L5205](../../../INBOX/opm-libro.txt#L5190-L5205)
- **P2023** · `fact` · A state-specified procedural link is a procedural link that connects a process to a state of an object. · [src:S01:L5190-L5205](../../../INBOX/opm-libro.txt#L5190-L5205)
- **P2024** · `fact` · For each procedural link there is a state-specified version. · [src:S01:L5190-L5205](../../../INBOX/opm-libro.txt#L5190-L5205)
- **P2025** · `fact` · State-specified procedural links differ from their non-state-specified version in that rather than connecting the (transforming or enabled) process to the involved object (transformee or enabler), they connect the process to one of the involved object’s states. · [src:S01:L5190-L5205](../../../INBOX/opm-libro.txt#L5190-L5205)
- **P2026** · `fact` · Thus, state-specified procedural links are elaborate versions of their regular procedural counterparts. · [src:S01:L5190-L5205](../../../INBOX/opm-libro.txt#L5190-L5205)
- **P2027** · `constraint` · Table 13.1 Procedural links, their semantics, symbols, source, and destination · [src:S01:L5190-L5205](../../../INBOX/opm-libro.txt#L5190-L5205)

## opm libro · Chapter 13 The Dynamic System Aspect / 13.8 State-Specified Enabling Links

- **P2028** · `definition` · State-specified enabling links—agent link and instrument link—are defined as follows. · [src:S01:L5207-L5229](../../../INBOX/opm-libro.txt#L5207-L5229)
- **P2029** · `requirement` · A state-specified agent link is an agent link that originates from a specific state s of an agent G to process P, denoting that in order for G to handle P, G must be at state s throughout the duration of P. · [src:S01:L5207-L5229](../../../INBOX/opm-libro.txt#L5207-L5229)
- **P2030** · `fact` · Like its state-specified consumption link and result link counterparts, the state-specified instrument link originates from a specific state and terminates at a process. · [src:S01:L5207-L5229](../../../INBOX/opm-libro.txt#L5207-L5229)
- **P2031** · `fact` · The semantics of this link is that the process is enabled if and only if the object exists and is at the state from which the link originates. · [src:S01:L5207-L5229](../../../INBOX/opm-libro.txt#L5207-L5229)
- **P2032** · `fact` · This is contrasted with the “regular” instrument link, which originates from the enabling instrument but not from any particular state of that instrument. · [src:S01:L5207-L5229](../../../INBOX/opm-libro.txt#L5207-L5229)
- **P2033** · `requirement` · For example, a pilot must be sober in order to qualify as an agent for the flying process of an Airplane. In OPL: Sober Pilot handles Flying. · [src:S01:L5207-L5229](../../../INBOX/opm-libro.txt#L5207-L5229)
- **P2034** · `requirement` · A state-specified instrument link is an instrument link that originates from a specific state s of the instrument I to process P, denoting that in order for P to execute, I must be at state s throughout the duration of P. · [src:S01:L5207-L5229](../../../INBOX/opm-libro.txt#L5207-L5229)
- **P2035** · `fact` · The difference between the two instrument link types is demonstrated in Fig. · [src:S01:L5207-L5229](../../../INBOX/opm-libro.txt#L5207-L5229)
- **P2036** · `constraint` · 13.10, where on the left hand side, the object Moving Truck is the instrument for Moving, implying that the state at which this Moving Truck is does not matter. · [src:S01:L5207-L5229](../../../INBOX/opm-libro.txt#L5207-L5229)
- **P2037** · `fact` · On the right hand side, the instrument link originates from the state serviced of Moving Truck, implying that only if Moving Truck is serviced, Moving can take place. Moving. · [src:S01:L5207-L5229](../../../INBOX/opm-libro.txt#L5207-L5229)
- **P2038** · `constraint` · Right: State-specified instrument link—serviced Moving Truck is an instrument of Moving Table 13.2 summarizes the semantics, symbols, source, and destination of the two state-specified enabling links. · [src:S01:L5207-L5229](../../../INBOX/opm-libro.txt#L5207-L5229)
