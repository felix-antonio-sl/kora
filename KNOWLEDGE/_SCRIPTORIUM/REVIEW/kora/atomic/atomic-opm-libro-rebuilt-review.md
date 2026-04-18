---
review_type: atomic_acceptance
decision: reject
publish_ready: false
reviewer: agent
generated_at: '2026-04-18T05:47:55+00:00'
review_target: /home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/REVIEW/kora/atomic/atomic-opm-libro-rebuilt-index.md
bundle_root: atomic-opm-libro-rebuilt
review_artifact: /home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/REVIEW/kora/atomic/atomic-opm-libro-rebuilt-review.md
requested_sample_size: 8
sample_size: 8
source_corpus: /home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt
bundle_stats:
  record_count: 4199
  tension_count: 5
  multi_source_count: 9
  negation_or_exception_count: 628
  high_risk_count: 855
  type_counts:
    constraint: 788
    definition: 125
    fact: 3137
    requirement: 144
    tension: 5
checks:
  bundle_integrity: pass
  editorial_quality: fail
  fidelity_packet: pass
blockers:
- editorial_quality
- decision_reject
---

# Atomic Acceptance Review

## Target

- Bundle root: `atomic-opm-libro-rebuilt`
- Target path: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/REVIEW/kora/atomic/atomic-opm-libro-rebuilt-index.md`
- Review artifact: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/REVIEW/kora/atomic/atomic-opm-libro-rebuilt-review.md`
- Reviewer: `agent`
- Decision: `reject`
- Publish ready: `no`
- Requested sample size: `8`
- Effective sample size: `8`

## Summary

Control de cierre previo al handoff; bundle util como referencia pero aun con residuos editoriales.

## Bundle Risk Summary

- `record_count`: `4199`
- `tension_count`: `5`
- `multi_source_count`: `9`
- `negation_or_exception_count`: `628`
- `high_risk_count`: `855`
- `type_counts`: `constraint=788, definition=125, fact=3137, requirement=144, tension=5`

## Gate Results

- `bundle_integrity`: `pass`
- `editorial_quality`: `fail`
- `fidelity_packet`: `pass`

## Blockers

- `editorial_quality`
- `decision_reject`

## Bundle Integrity

        - Exit code: `0`
        - Command: `/usr/bin/python3 /home/felix/kora/SKILLS/kora/atomize/scripts/check_atomic_bundle.py /home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/REVIEW/kora/atomic/atomic-opm-libro-rebuilt-index.md`

        ```text
        atomic-opm-libro-rebuilt-index.md
  family: atomic
  role: index
  propositions: 0
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-01.md
  family: atomic
  role: segment
  propositions: 48
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-02.md
  family: atomic
  role: segment
  propositions: 58
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-03.md
  family: atomic
  role: segment
  propositions: 59
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-04.md
  family: atomic
  role: segment
  propositions: 63
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-05.md
  family: atomic
  role: segment
  propositions: 51
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-06.md
  family: atomic
  role: segment
  propositions: 41
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-07.md
  family: atomic
  role: segment
  propositions: 63
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-08.md
  family: atomic
  role: segment
  propositions: 64
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-09.md
  family: atomic
  role: segment
  propositions: 48
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-10.md
  family: atomic
  role: segment
  propositions: 44
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-11.md
  family: atomic
  role: segment
  propositions: 59
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-12.md
  family: atomic
  role: segment
  propositions: 49
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-13.md
  family: atomic
  role: segment
  propositions: 35
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-14.md
  family: atomic
  role: segment
  propositions: 52
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-15.md
  family: atomic
  role: segment
  propositions: 55
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-16.md
  family: atomic
  role: segment
  propositions: 55
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-17.md
  family: atomic
  role: segment
  propositions: 51
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-18.md
  family: atomic
  role: segment
  propositions: 57
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-19.md
  family: atomic
  role: segment
  propositions: 60
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-20.md
  family: atomic
  role: segment
  propositions: 43
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-21.md
  family: atomic
  role: segment
  propositions: 47
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-22.md
  family: atomic
  role: segment
  propositions: 65
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-23.md
  family: atomic
  role: segment
  propositions: 58
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-24.md
  family: atomic
  role: segment
  propositions: 58
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-25.md
  family: atomic
  role: segment
  propositions: 62
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-26.md
  family: atomic
  role: segment
  propositions: 60
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-27.md
  family: atomic
  role: segment
  propositions: 33
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-28.md
  family: atomic
  role: segment
  propositions: 56
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-29.md
  family: atomic
  role: segment
  propositions: 50
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-30.md
  family: atomic
  role: segment
  propositions: 51
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-31.md
  family: atomic
  role: segment
  propositions: 47
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-32.md
  family: atomic
  role: segment
  propositions: 49
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-33.md
  family: atomic
  role: segment
  propositions: 53
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-34.md
  family: atomic
  role: segment
  propositions: 55
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-35.md
  family: atomic
  role: segment
  propositions: 61
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-36.md
  family: atomic
  role: segment
  propositions: 61
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-37.md
  family: atomic
  role: segment
  propositions: 63
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-38.md
  family: atomic
  role: segment
  propositions: 54
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-39.md
  family: atomic
  role: segment
  propositions: 46
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-40.md
  family: atomic
  role: segment
  propositions: 52
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-41.md
  family: atomic
  role: segment
  propositions: 42
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-42.md
  family: atomic
  role: segment
  propositions: 56
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-43.md
  family: atomic
  role: segment
  propositions: 55
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-44.md
  family: atomic
  role: segment
  propositions: 60
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-45.md
  family: atomic
  role: segment
  propositions: 41
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-46.md
  family: atomic
  role: segment
  propositions: 53
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-47.md
  family: atomic
  role: segment
  propositions: 44
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-48.md
  family: atomic
  role: segment
  propositions: 54
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-49.md
  family: atomic
  role: segment
  propositions: 33
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-50.md
  family: atomic
  role: segment
  propositions: 53
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-51.md
  family: atomic
  role: segment
  propositions: 44
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-52.md
  family: atomic
  role: segment
  propositions: 44
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-53.md
  family: atomic
  role: segment
  propositions: 41
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-54.md
  family: atomic
  role: segment
  propositions: 50
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-55.md
  family: atomic
  role: segment
  propositions: 63
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-56.md
  family: atomic
  role: segment
  propositions: 57
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-57.md
  family: atomic
  role: segment
  propositions: 59
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-58.md
  family: atomic
  role: segment
  propositions: 45
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-59.md
  family: atomic
  role: segment
  propositions: 63
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-60.md
  family: atomic
  role: segment
  propositions: 58
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-61.md
  family: atomic
  role: segment
  propositions: 55
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-62.md
  family: atomic
  role: segment
  propositions: 56
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-63.md
  family: atomic
  role: segment
  propositions: 42
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-64.md
  family: atomic
  role: segment
  propositions: 50
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-65.md
  family: atomic
  role: segment
  propositions: 59
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-66.md
  family: atomic
  role: segment
  propositions: 43
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-67.md
  family: atomic
  role: segment
  propositions: 41
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-68.md
  family: atomic
  role: segment
  propositions: 46
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-69.md
  family: atomic
  role: segment
  propositions: 60
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-70.md
  family: atomic
  role: segment
  propositions: 55
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-71.md
  family: atomic
  role: segment
  propositions: 58
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-72.md
  family: atomic
  role: segment
  propositions: 48
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-73.md
  family: atomic
  role: segment
  propositions: 40
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-74.md
  family: atomic
  role: segment
  propositions: 62
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-75.md
  family: atomic
  role: segment
  propositions: 49
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-76.md
  family: atomic
  role: segment
  propositions: 45
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-77.md
  family: atomic
  role: segment
  propositions: 57
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-78.md
  family: atomic
  role: segment
  propositions: 47
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-79.md
  family: atomic
  role: segment
  propositions: 54
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-80.md
  family: atomic
  role: segment
  propositions: 48
  indexed_sources: 1
  lint: OK
atomic-opm-libro-rebuilt-81.md
  family: atomic
  role: segment
  propositions: 33
  indexed_sources: 1
  lint: OK
bundle_ids: OK
        ```

## Editorial Quality

        - Exit code: `1`
        - Command: `/usr/bin/python3 /home/felix/kora/SKILLS/kora/atomize/scripts/review_atomic_quality.py /home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/REVIEW/kora/atomic/atomic-opm-libro-rebuilt-index.md --source /home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`

        ```text
        bundle_files: 82
propositions: 4199
source: /home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt
source_chars: 825160
source_lines: 10911
chars_per_proposition: 196.5
microsegments: OK
density: OK
contamination: WARN
  - atomic-opm-libro-rebuilt-03.md P0136: In doing so, the reader reinforces familiarity with the specification and can more easily detect design errors or omissions.
  - atomic-opm-libro-rebuilt-05.md P0277: Figure 3.4 displays Vehicle Occupants Group as a physical object by its shading.
  - atomic-opm-libro-rebuilt-06.md P0281: Figure 3.4 shows this via the effect link, which is the bidirectional arrow between Crashing and Vehicle.
  - atomic-opm-libro-rebuilt-08.md P0410: Figure 5.2, which is a screenshot of OPCAT, shows both the top-level OPD, SD (in the left window), and the new one, called SD1—Automatic Crash Responding in-zoo
  - atomic-opm-libro-rebuilt-08.md P0411: Figure 5.2 also shows at the OPD hierarchy pane on the left hand side the OPD process tree, which currently has just two OPDs: SD and SD1. zoomed (right).
  - atomic-opm-libro-rebuilt-08.md P0433: Figure 5.3 shows Crash Severity linked to Vehicle via an exhibition-characterization structural relation.
  - atomic-opm-libro-rebuilt-09.md P0449: Figure 5.4 shows the system after the (environmental) process Crashing has changed the state of Vehicle from intact to crashed, which was the event that has ini
  - atomic-opm-libro-rebuilt-12.md P0625: The merging of Message Creating and Message Sending results in process out-zooming, in which two or more processes are abstracted them into a higher-level proce
  - atomic-opm-libro-rebuilt-12.md P0630: Figure 8.2 indeed looks simpler than its previous version in Fig. 8.1.
  - atomic-opm-libro-rebuilt-13.md P0650: Figure 8.4 shows the automatically-generated structural view of the ACR System, after manual rearrangements for improved readability.
  - atomic-opm-libro-rebuilt-14.md P0708: Processes cannot just happen in vacuum, without “doing” something, which leads to the next question.
  - atomic-opm-libro-rebuilt-26.md P1364: Figure 10.11 demonstrates the notions of transient object and invocation link.
anchors: OK
        ```

## Semantic Fidelity Packet

        - Exit code: `0`
        - Command: `/usr/bin/python3 /home/felix/kora/SKILLS/kora/atomize/scripts/prepare_atomic_fidelity_review.py /home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/REVIEW/kora/atomic/atomic-opm-libro-rebuilt-index.md --sample-size 8 --source /home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`

        ```text
        packet_type: semantic_fidelity_review
bundle_files: 82
record_count: 4199
tension_count: 5
multi_source_count: 9
negation_or_exception_count: 628
high_risk_count: 855
sample_size: 8
sample_contains_tension: yes
type_counts: constraint=788, definition=125, fact=3137, requirement=144, tension=5
source: /home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt
note: este script no juzga la fidelidad semantica por si solo; prepara evidencia para revision del agente o humana.

[01] atomic-opm-libro-rebuilt-30.md P1563 `tension`
risk_flags: tension, numeric
selection_reason: tension
proposition: SysML reuses a subset of UML 2 and provides additional extensions in order to satisfy the RFP requirements.
source_1: ../../../INBOX/opm-libro.txt#L4121-L4138
excerpt:
A general-purpose modeling language for systems engineering, SysML is intended to support
specification, analysis, design, verification, and validation of complex systems. The systems may be of
broad range, and can include hardware, software, data, personnel, procedures, facilities, and more. SysML
reuses a subset of UML 2 and provides additional extensions in order to satisfy the RFP requirements. As
a visual modeling language, SysML offers several kinds of diagrams which can reflect various aspects of
a system.
SysML diagrams are commonly categorized into four “pillars”—structure, behavior, requirements,
and parametric relationships. In addition, SysML provides means to cross-connect the different model
elements. Figure 12.1, adapted from Friedenthal et al. (2012), shows examples of key SysML diagram
types. Overall, SysML includes nine types of diagrams: four types of structure diagrams, four types of
behavior diagrams, and a requirements diagram.
SysML diagram taxonomy is presented in Fig. 12.2. Using OPM notation, Fig. 12.2 shows what
diagrams were adopted from UML without change, what diagrams were adopted from UML with change
and what diagrams are new. Four SysML diagrams are the same as their UML counterpart: Use Case
diagram, Package diagram, Sequence diagram, and State Machine diagram. Three are modified from
UML 2: Block Definition diagram, Internal Block diagram, and Activity diagram. Finally, two new
diagrams are added: Requirements diagram and Parametrics diagram. Each of the four SysML pillars is
described next.
review:
- ¿La proposicion esta totalmente soportada por el excerpt?
- ¿Perdio negaciones, cuantificadores, excepciones o condiciones?
- ¿Fusiona mas de un hecho distinguible?
- ¿Introduce interpretacion no sustentada por la fuente?

[02] atomic-opm-libro-rebuilt-31.md P1601 `tension`
risk_flags: tension, numeric, date_or_duration
selection_reason: tension
proposition: Activities and activity diagrams exist also in UML, but SysML provides several extensions (Bock 2006), including means to support “continuous” flow modeling, such as rate restrictions.
source_1: ../../../INBOX/opm-libro.txt#L4199-L4240
excerpt:
As expressed in Fig. 12.2, SysML specifies four types of behavioral diagrams: activity diagram, sequence
diagram, state machine diagram, and use case diagram.
Dori – Model-Based Systems Engineering with OPM and SysML
139
Control
Flow
Fill
Order
Ship
Order
Create
Invoice
Invoice
Send
Invoice
Object
Flow
Object
Flow
Fig. 12.3 A simple SysML activity diagram with block and action nodes and control and object flows
Activity is the fundamental behavioral element in the various SysML behavioral diagrams (excluding
the use case diagram). The role of the activity diagram (see Fig. 12.3) is to represent the flow of inputs
and outputs and the flow of control between actions. To this end, the activity diagram incorporates
sequences and conditions for coordinating activities. Activities and activity diagrams exist also in UML,
but SysML provides several extensions (Bock 2006), including means to support “continuous” flow
modeling, such as rate restrictions. Support for probabilities and extensions to control (known as “control
as data”) were added to SysML activity diagrams. In addition, to smoothly align SysML with the widely-
used classical systems engineering behavior diagram (known as EFFBD—Enhanced Functional Flow
Block Diagrams; Bock, 2005), the «effbd» stereotype is specified. When this stereotype is applied to an
activity, it means that the activity must conform to the constraints necessary for EFFBD.
The use case diagram is intended to describe basic high-level functionally by specifying the usage of
the system by its actors to achieve a goal. It is often the first kind of diagram used to specify semi-
formally with the customer to define the function and scope of the system to be developed.
Activity diagram is the only behavioral diagram kind that is extended in SysML with respect to UML
2, while the other three SysML behavioral diagram kinds remain unchanged or were eliminated.
Sequence diagram is used to represent message-based flow of control between interacting entities, which
may be actors, systems, or parts of a system. The state machine diagram models state-based behavior
using object states and transitions.
An action (denoted by a rountangle) is a basic (usually atomic) unit of process in an activity diagram.
As Fig. 12.3 shows, an activity diagram is composed of nodes and edges, where a node can be an action
or a block (denoted by a rectangle), and an edge can be a control flow if it is between actions, or an object
flow (or block flow) if it is between a block and an action.
review:
- ¿La proposicion esta totalmente soportada por el excerpt?
- ¿Perdio negaciones, cuantificadores, excepciones o condiciones?
- ¿Fusiona mas de un hecho distinguible?
- ¿Introduce interpretacion no sustentada por la fuente?

[03] atomic-opm-libro-rebuilt-31.md P1602 `tension`
risk_flags: tension
selection_reason: tension
proposition: Support for probabilities and extensions to control (known as “control as data”) were added to SysML activity diagrams.
source_1: ../../../INBOX/opm-libro.txt#L4199-L4240
excerpt:
As expressed in Fig. 12.2, SysML specifies four types of behavioral diagrams: activity diagram, sequence
diagram, state machine diagram, and use case diagram.
Dori – Model-Based Systems Engineering with OPM and SysML
139
Control
Flow
Fill
Order
Ship
Order
Create
Invoice
Invoice
Send
Invoice
Object
Flow
Object
Flow
Fig. 12.3 A simple SysML activity diagram with block and action nodes and control and object flows
Activity is the fundamental behavioral element in the various SysML behavioral diagrams (excluding
the use case diagram). The role of the activity diagram (see Fig. 12.3) is to represent the flow of inputs
and outputs and the flow of control between actions. To this end, the activity diagram incorporates
sequences and conditions for coordinating activities. Activities and activity diagrams exist also in UML,
but SysML provides several extensions (Bock 2006), including means to support “continuous” flow
modeling, such as rate restrictions. Support for probabilities and extensions to control (known as “control
as data”) were added to SysML activity diagrams. In addition, to smoothly align SysML with the widely-
used classical systems engineering behavior diagram (known as EFFBD—Enhanced Functional Flow
Block Diagrams; Bock, 2005), the «effbd» stereotype is specified. When this stereotype is applied to an
activity, it means that the activity must conform to the constraints necessary for EFFBD.
The use case diagram is intended to describe basic high-level functionally by specifying the usage of
the system by its actors to achieve a goal. It is often the first kind of diagram used to specify semi-
formally with the customer to define the function and scope of the system to be developed.
Activity diagram is the only behavioral diagram kind that is extended in SysML with respect to UML
2, while the other three SysML behavioral diagram kinds remain unchanged or were eliminated.
Sequence diagram is used to represent message-based flow of control between interacting entities, which
may be actors, systems, or parts of a system. The state machine diagram models state-based behavior
using object states and transitions.
An action (denoted by a rountangle) is a basic (usually atomic) unit of process in an activity diagram.
As Fig. 12.3 shows, an activity diagram is composed of nodes and edges, where a node can be an action
or a block (denoted by a rectangle), and an edge can be a control flow if it is between actions, or an object
flow (or block flow) if it is between a block and an action.
review:
- ¿La proposicion esta totalmente soportada por el excerpt?
- ¿Perdio negaciones, cuantificadores, excepciones o condiciones?
- ¿Fusiona mas de un hecho distinguible?
- ¿Introduce interpretacion no sustentada por la fuente?

[04] atomic-opm-libro-rebuilt-55.md P2828 `tension`
risk_flags: tension, negation_or_exception
selection_reason: tension
proposition: The idea of attributes for processes is a natural extension to attributes for objects and poses no special conceptual difficulty.
source_1: ../../../INBOX/opm-libro.txt#L7351-L7381
excerpt:
Like objects, processes require adequate representation in the model of any system. Just like objects,
processes might require attributes—objects that describe them. The idea of attributes for processes is a
natural extension to attributes for objects and poses no special conceptual difficulty.
So far, we have seen that the first and second thing-feature combinations—an object describing an
object and a process describing an object—are the corresponding object-oriented concepts for attribute
and operation (or service, or method). However, the third thing-feature combination—an object
Dori – Model-Based Systems Engineering with OPM and SysML
247
describing a process—is not explicitly defined in the OO approach. Here we refer to an object B1—the
attribute—that characterizes a higher level process P1. Conversely, we say that the process P1 exhibits the
attribute B1. Few examples of pairs of a process and its attribute are Diving—Depth, Commanding—
Language, Printing—Quality, Striking—Duration, Manufacturing—Quantity, Watching—Effectiveness,
Singing—Volume, Skiing—Location, and Flying—Speed.
Fig. 18.7 Examples of attributes of processes
Figure 18.7 presents OPM models that correspond to the first four process-attribute pairs. Each of
these process-attribute pairs can be embedded in a natural language sentence. Here are possible examples,
where the processes are bold and their attributes are italicized:
(1) Diving at a depth of 30 meters or more requires the diver to make decompression stops.
(2) The language the office was using for commanding was foreign and strange.
(3) The printing of this device is of poor quality.
(4) The employees have been striking for duration of over two weeks.
While all the processes in these examples are nouns having the gerund form, they can be easily
converted into sentences where the processes are verbs, with the same semantics as before:
(1) A diver who dives at a depth of 30 meters or more is required to make decompression stops.
(2) The officer commands in a foreign language.
(3) This device prints with poor quality.
(4) The employees strike, and this has been lasting for a duration of over two weeks.
As these examples show, this OPM extension of the OO, UML and SysML attribute and operation
concepts is a direct consequence of recognizing processes as bona fide independent kind of things
besides, rather than being necessarily subordinates of objects, or second-class citizens that are owned
objects.
review:
- ¿La proposicion esta totalmente soportada por el excerpt?
- ¿Perdio negaciones, cuantificadores, excepciones o condiciones?
- ¿Fusiona mas de un hecho distinguible?
- ¿Introduce interpretacion no sustentada por la fuente?

[05] atomic-opm-libro-rebuilt-55.md P2836 `tension`
risk_flags: tension, long_statement
selection_reason: tension
proposition: As these examples show, this OPM extension of the OO, UML and SysML attribute and operation concepts is a direct consequence of recognizing processes as bona fide independent kind of things besides, rather than being necessarily subordinates of objects, or second-class citizens that are owned objects.
source_1: ../../../INBOX/opm-libro.txt#L7351-L7381
excerpt:
Like objects, processes require adequate representation in the model of any system. Just like objects,
processes might require attributes—objects that describe them. The idea of attributes for processes is a
natural extension to attributes for objects and poses no special conceptual difficulty.
So far, we have seen that the first and second thing-feature combinations—an object describing an
object and a process describing an object—are the corresponding object-oriented concepts for attribute
and operation (or service, or method). However, the third thing-feature combination—an object
Dori – Model-Based Systems Engineering with OPM and SysML
247
describing a process—is not explicitly defined in the OO approach. Here we refer to an object B1—the
attribute—that characterizes a higher level process P1. Conversely, we say that the process P1 exhibits the
attribute B1. Few examples of pairs of a process and its attribute are Diving—Depth, Commanding—
Language, Printing—Quality, Striking—Duration, Manufacturing—Quantity, Watching—Effectiveness,
Singing—Volume, Skiing—Location, and Flying—Speed.
Fig. 18.7 Examples of attributes of processes
Figure 18.7 presents OPM models that correspond to the first four process-attribute pairs. Each of
these process-attribute pairs can be embedded in a natural language sentence. Here are possible examples,
where the processes are bold and their attributes are italicized:
(1) Diving at a depth of 30 meters or more requires the diver to make decompression stops.
(2) The language the office was using for commanding was foreign and strange.
(3) The printing of this device is of poor quality.
(4) The employees have been striking for duration of over two weeks.
While all the processes in these examples are nouns having the gerund form, they can be easily
converted into sentences where the processes are verbs, with the same semantics as before:
(1) A diver who dives at a depth of 30 meters or more is required to make decompression stops.
(2) The officer commands in a foreign language.
(3) This device prints with poor quality.
(4) The employees strike, and this has been lasting for a duration of over two weeks.
As these examples show, this OPM extension of the OO, UML and SysML attribute and operation
concepts is a direct consequence of recognizing processes as bona fide independent kind of things
besides, rather than being necessarily subordinates of objects, or second-class citizens that are owned
objects.
review:
- ¿La proposicion esta totalmente soportada por el excerpt?
- ¿Perdio negaciones, cuantificadores, excepciones o condiciones?
- ¿Fusiona mas de un hecho distinguible?
- ¿Introduce interpretacion no sustentada por la fuente?

[06] atomic-opm-libro-rebuilt-01.md P0031 `constraint`
risk_flags: constraint, negation_or_exception, numeric, date_or_duration, long_statement
selection_reason: negation_or_exception
proposition: In 2000, when I attended a Technical Meeting of OMG in which UML was considered for progression from version 1 to 2, I proposed considering UML for being extended to handle not just software systems, but systems at large, a proposal that was dismissed off-hand by most attendees, who were software people.
source_1: ../../../INBOX/opm-libro.txt#L12-L97
excerpt:
The quest for simplicity in a complex world has occupied thinkers for millennia. How to conceptualize
what humans observe around them and what they wish to design in order to improve the quality of
people’s lives has been one of the major driving forces in advancing civilization. The advent of
computers in the middle of the previous century was a great impetus to fostering thoughts about how to
conceptually represent things in the real world. The initial accepted train of thought produced procedural
programming, which put procedures, routines, functions, etc. at the center of programming. Further
contemplations have led to the idea of putting objects, which are more static in nature, as the anchor of
programs. The shift to the object oriented (OO) paradigm for programming languages, which occurred in
the 1980s and 1990s, was followed by the idea that programming should be preceded by analysis and
design of the programs, or, more generally, the systems those programs represent and serve. Naturally,
the approach which was taken is also object-oriented.
In the early 1990, a plethora of some three dozen object-oriented analysis and design methods and
notations flourished, leading to what was known as the “Methods War”. Around that time, in 1991, when
I moved from University of Kansas to Technion, Israel Institute of Technology, as I was tasked with
teaching software design, I got interested in these topics. It was not long before I realized that just as the
procedural approach to software was inadequate, so was the “pure” OO approach, which puts objects as
the sole “first class” citizens, with “methods” (or “services”) being their second-class subordinate
procedures. However, I could not put my finger on what was missing.
My Eureka moment was in 1993, when I and colleagues from University of Washington were trying
to model a system for automated transforming of hand-made engineering drawings to CAD models, a
topic around which my research focused during that time. Drawing objects as the model’s building blocks
and connecting them on the white board, it dawned on me that not all the boxes in the model were really
objects; some were things that happen to objects. When I circled those things, a pattern of a bipartite
graph emerged, where the nodes representing objects—the things that exist—were mediated by those
circled nodes, which I immediately called processes. This was the first object-process diagram (OPD)
ever drawn. I realized then that the pendulum of the previously accepted procedural software to the
primarily static OO paradigm moved too drastically. While the shift from procedures to objects as the
focus of interest was a right move, it went too far, as it suppressed the systems’ procedural aspect, which
is essential to faithfully describe how systems change over time.
Forbidding processes, such as cake baking or check cashing, from being conceptual entities in their
own right, and allowing their representation only as methods of object classes, results in distorted models,
in which a check “owns” the cashing method or the cake owns the baking process. In real life, however,
baking is a pattern of transformation of ingredients making up the dough that requires a baker, an oven,
and energy to prepare the dough and convert it into a cake. Similarly, a check cannot cash itself; it
requires a check writer having an account with sufficient funds, a check casher, and a bank clerk or an
ATM. Each of the objects involved in these methods could just as well be the owner of the method.
Modeling baking and cashing as stand-alone processes—conceptual things that represent physical or
informatical object transformation patterns—open the door for creating models that are much more
faithful to the way we conceive reality and convey it to others.
ix
x Preface
Indeed, recognizing processes as bona fide conceptual modeling building blocks beside, rather than
underneath objects, is the prime foundation of Object-Process Methodology (OPM). OPM is founded on
a universal minimal ontology, according to which objects exist, while processes transform them.
Transformation includes object creation and consumption, as well as change of the state of an object.
Therefore, OPM objects are stateful—they can have states. Hence, stateful objects and processes that
transform them are the only two concepts in OPM’s universal minimal ontology. Two other cornerstones
of OPM are its bimodal graphical-textual representation and its built- in refinement-abstraction
complexity management mechanisms of in-zooming and unfolding of a single type of diagram—OPD.
When I tried to publish a paper titled “Object-Process Analysis: Maintaining the Balance between
System Structure and Behavior” with the buds of these ideas in 1993, it was serially rejected off hand
with claims along the line that it had already been proven that what I was suggesting is impossible, like
“mixing water with oil.” Finally, the Journal of Logic and Computation accepted it, perhaps because
being mathematics- rather than software-oriented, it was more tolerant toward ideas that went against the
then new and glorious OO paradigm.
Meanwhile, in 1997, the “Methods Wars” culminated in the adoption of the Unified Modeling
Languages (UML), by the Object Management Group (OMG), making it the de-facto standard for software
design. UML 1 had nine types of diagrams. In 2000, when I attended a Technical Meeting of OMG in
which UML was considered for progression from version 1 to 2, I proposed considering UML for being
extended to handle not just software systems, but systems at large, a proposal that was dismissed off-hand
by most attendees, who were software people. However, following a 2001 initiative of the International
Council on Systems Engineering (INCOSE), in 2003 OMG issued the UML for Systems Engineering
Request for Proposals, and in 2006 OMG adopted SysML (Systems Modeling Language) 1.0
specification, which is based on UML 2. Since then, SysML has become the de-facto standard for
systems engineering.
Meanwhile, the first book on OPM, Object-Process Methodology—a Holistic Systems Paradigm,
(Dori, 2002) was published, and OPM has been successfully applied and papers published in many
diverse domains, ranging from the Semantic Web to defense and to molecular biology. In December 2015,
after six years of work, ISO adopted and published OPM as ISO 19450—Automation systems and
integration—Object-Process Methodology.
The realization and recognition that models can and should become the central artifact in system
lifecycles has been gaining momentum in recent years, giving rise to model-based systems engineering
(MBSE) as an evolving filed in the area of systems engineering. SysML and OPM have been serving as
the two MBSE languages, but since SysML was adopted as a standard about eight years before OPM and
has been backed by top-notch vendors, its adoption is currently more widespread. However, OPM is
rapidly gaining acceptance in academia and its application in diverse industry segments is spreading.
This textbook, designed for both self-learning and as an undergraduate or graduate course, endows its
readers with deep understanding of MBSE ideas, principles, and applications through modeling systems
using both OPM and SysML. The book is comprised of three parts that encompass 24 chapters. Each
chapter ends with a bulleted summary and a set of problems. Solutions to problems may be available in
http://esml.iem.technion.ac.il/.Part I introduces OPM and SysML via step-by-step modeling of a car automatic crash response
system. Chapter 1 starts with a description of the system and its initial OPM model. In Chap 2 we
enhance the model with text and animated simulation. Chapter 3 introduces links that connect things in
Preface xi
the model. In Chap. 4 we introduce and use SysML’s first three diagrams. Chapter 5 presents ways for
managing the complexity of systems, while the dynamic aspect of the system is modeled in Chaps. 6 and
review:
- ¿La proposicion esta totalmente soportada por el excerpt?
- ¿Perdio negaciones, cuantificadores, excepciones o condiciones?
- ¿Fusiona mas de un hecho distinguible?
- ¿Introduce interpretacion no sustentada por la fuente?

[07] atomic-opm-libro-rebuilt-01.md P0048 `definition`
risk_flags: definition, negation_or_exception, numeric, date_or_duration, long_statement
selection_reason: negation_or_exception
proposition: Abstraction and refinement mechanisms as means to manage complexity are the focus of Chap. 8, the last chapter in Part I. Part II, Model-Based Systems Engineering Fundamentals, is a formal, theory-grounded exposure to OPM and SysML that discusses MBSE ontology, conceptual modeling constructs, and applications. Chapter 9 introduces and defines conceptual modeling. Chapter 10 presents the two basic building blocks of OPM—objects and processes, while Chap. 11 is about the textual modality of OPM—OPL. In Chap. 12 we turn to an orderly study of SysML with its four pillars and nine kinds of diagrams. The dynamic, time-dependent aspect of systems is the focus of Chap. 13, followed by studying the structural, time- independent system aspect in Chap. 14. Following Chap. 15, which deals with participation constraints and fork links, in Chap. 16 we introduce the four fundamental structural relations. In Part III, Structure and Behavior: Diving In, we go to the heart of conceptual modeling, elaborating on the four fundamental structural relations and whole system aspects, including complexity management and control. Chapters 17 and 18 discuss aggregation-participation and exhibition-characterization, respectively. Chapter 19 is about states and values, concepts that are needed for generalization- specialization and classification-instantiation, both of which are elaborated on in Chap. 20. Chapter 21 concerns complexity management and the refinement-abstraction mechanisms of OPM, as well as complexity management in SysML. Chapter 22 is about OPM operational semantics and control links— the way control is managed during execution of the system. In Chap. 23 we specify how to model logical operators and probabilities. Finally, Chap. 24 is an overview of ISO 19450—Automation Systems and Integration—Object-Process Methodology, adopted by the International organization for Standardization in December 2015.With respect to OPM, this book can be considered a superset of ISO 19450. While OPM, as specified in this book, is ISO 19450-complaint, the book provides in-depth motivation, rationale, and philosophical foundations for decisions made during the design of ISO 19450. These cannot be elaborated on in a standard, which, by its nature, is expected to be short and decisive, with little justifications. OPM points in the book that are not covered in ISO 19450 can be considered optional, or, in ISO nomenclature, informative, as opposed to normative—abiding ISO specifications. This book is a product of six years of work, during which I have made all efforts to make it accurate, consistent, and formal, while also not lose the human touch and the interest of the future reader. It is my sincere hope that the book will serve as a reliable reference to MBSE in general and to OPM and SysML in particular. Examining the above word cloud of this book (created by a program developed skillfully by Jason Davies),2 based on close to 140,000 words contained in this book, we can see that the most frequent words are process, object, and link. Indeed, this is a most faithful testimony that OPM focuses on how to model systems (two other most frequent words in the cloud) by relating processes to objects using links. Relation is there too, along with other notable words, including diagram, attribute, structural, procedural, semantics, state, control, change, effect, agent, time, constraint, and function. Of course, SysML is there between process and model, near OPD (Object-Process Diagram—OPM’s graphical modality) and OPL (Object-Process Language—OPM’s textual modality). This list gives a good idea of what this book is about. I wish to thank my three MIT collaborators, Prof. Ed Crawley and Prof. Oli de Weck from Engineering Systems Division and the Aero-Astro Department, and Pat Hale, Director of Systems Design and Management Program. Special thanks to my PhD student, Yaniv Mordecai, who provided insightful comments on many of the chapters in this book. I thank the Technion, Israel Institute of Technology, which provided me with the environment to develop OPM and with the 2013-4 sabbatical to complete this book. Finally, I wish to thank my beloved wife, Prof. Judy Dori, who provided pedagogical guidance and moral support, which made it possible for me to finish the book. Dov Dori Massachusetts Institute of Technology, July 2015
source_1: ../../../INBOX/opm-libro.txt#L98-L146
excerpt:
7. Abstraction and refinement mechanisms as means to manage complexity are the focus of Chap. 8, the
last chapter in Part I.
Part II, Model-Based Systems Engineering Fundamentals, is a formal, theory-grounded exposure to
OPM and SysML that discusses MBSE ontology, conceptual modeling constructs, and applications.
Chapter 9 introduces and defines conceptual modeling. Chapter 10 presents the two basic building blocks
of OPM—objects and processes, while Chap. 11 is about the textual modality of OPM—OPL. In Chap.
12 we turn to an orderly study of SysML with its four pillars and nine kinds of diagrams. The dynamic,
time-dependent aspect of systems is the focus of Chap. 13, followed by studying the structural, time-
independent system aspect in Chap. 14. Following Chap. 15, which deals with participation constraints
and fork links, in Chap. 16 we introduce the four fundamental structural relations.
In Part III, Structure and Behavior: Diving In, we go to the heart of conceptual modeling, elaborating
on the four fundamental structural relations and whole system aspects, including complexity management
and control. Chapters 17 and 18 discuss aggregation-participation and exhibition-characterization,
respectively. Chapter 19 is about states and values, concepts that are needed for generalization-
specialization and classification-instantiation, both of which are elaborated on in Chap. 20. Chapter 21
concerns complexity management and the refinement-abstraction mechanisms of OPM, as well as
complexity management in SysML. Chapter 22 is about OPM operational semantics and control links—
the way control is managed during execution of the system. In Chap. 23 we specify how to model logical
operators and probabilities. Finally, Chap. 24 is an overview of ISO 19450—Automation Systems and
Integration—Object-Process Methodology, adopted by the International organization for Standardization
in December 2015.With respect to OPM, this book can be considered a superset of ISO 19450. While OPM, as specified
in this book, is ISO 19450-complaint, the book provides in-depth motivation, rationale, and philosophical
foundations for decisions made during the design of ISO 19450. These cannot be elaborated on in a
standard, which, by its nature, is expected to be short and decisive, with little justifications. OPM points
in the book that are not covered in ISO 19450 can be considered optional, or, in ISO nomenclature,
informative, as opposed to normative—abiding ISO specifications.
This book is a product of six years of work, during which I have made all efforts to make it accurate,
consistent, and formal, while also not lose the human touch and the interest of the future reader. It is my
sincere hope that the book will serve as a reliable reference to MBSE in general and to OPM and SysML
in particular.
xii
Preface
Examining the above word cloud of this book (created by a program developed skillfully by Jason
Davies),2 based on close to 140,000 words contained in this book, we can see that the most frequent
words are process, object, and link. Indeed, this is a most faithful testimony that OPM focuses on how to
model systems (two other most frequent words in the cloud) by relating processes to objects using links.
Relation is there too, along with other notable words, including diagram, attribute, structural,
procedural, semantics, state, control, change, effect, agent, time, constraint, and function. Of course,
SysML is there between process and model, near OPD (Object-Process Diagram—OPM’s graphical
modality) and OPL (Object-Process Language—OPM’s textual modality). This list gives a good idea of
what this book is about.
I wish to thank my three MIT collaborators, Prof. Ed Crawley and Prof. Oli de Weck from
Engineering Systems Division and the Aero-Astro Department, and Pat Hale, Director of Systems Design
and Management Program. Special thanks to my PhD student, Yaniv Mordecai, who provided insightful
comments on many of the chapters in this book. I thank the Technion, Israel Institute of Technology,
which provided me with the environment to develop OPM and with the 2013-4 sabbatical to complete
this book. Finally, I wish to thank my beloved wife, Prof. Judy Dori, who provided pedagogical guidance
and moral support, which made it possible for me to finish the book.
Dov Dori Massachusetts Institute of Technology, July 2015
review:
- ¿La proposicion esta totalmente soportada por el excerpt?
- ¿Perdio negaciones, cuantificadores, excepciones o condiciones?
- ¿Fusiona mas de un hecho distinguible?
- ¿Introduce interpretacion no sustentada por la fuente?

[08] atomic-opm-libro-rebuilt-03.md P0119 `constraint`
risk_flags: constraint, negation_or_exception, numeric, date_or_duration, long_statement
selection_reason: negation_or_exception
proposition: Jonathan Swift, Gulliver’s Travels (1726) Winograd and Flores (1987) noted that “Nothing exists except through language… In saying that some ‘thing’ exists (or that it has some property) we have brought it into a domain of articulated objects and qualities that exist in language.” Indeed, language greatly enhances our ability to understand systems and communicate our understanding to others.
source_1: ../../../INBOX/opm-libro.txt#L676-L690
excerpt:
We went next to the School of Languages. … The first Project was to shorten
Discourse by cutting Polysyllables into one, and leaving out Verbs and Participle,
because in Reality all things imaginable are but Nouns. … However, many of the most
Learned and Wise adhere to the new Scheme of expressing themselves by Things.
Jonathan Swift, Gulliver’s Travels (1726)
Winograd and Flores (1987) noted that “Nothing exists except through language… In saying that some
‘thing’ exists (or that it has some property) we have brought it into a domain of articulated objects and
qualities that exist in language.”
Indeed, language greatly enhances our ability to understand systems and communicate our
understanding to others. This chapter presents two enhancements to OPM models: textual model
representation and animated model simulation.
We introduce the object-process language (OPL) as the textual modality of OPM that complements
the graphical representation through OPDs (object-process diagrams). We show the equivalence between
this graphical specification and the natural language specification through OPL. The chapter also shows
another important means of enhancing model understanding: its animated simulation.
review:
- ¿La proposicion esta totalmente soportada por el excerpt?
- ¿Perdio negaciones, cuantificadores, excepciones o condiciones?
- ¿Fusiona mas de un hecho distinguible?
- ¿Introduce interpretacion no sustentada por la fuente?
        ```
