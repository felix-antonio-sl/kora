---
_manifest:
  urn: urn:kora:kb:atomic-opm-libro-rebuilt-74
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
      n_propositions: 62
      segmented: true
      segment_role: segment
      segment_index: 74
      segment_count: 81
      hand_edited: false
      soft_segment_target_chars: 15000
      hard_segment_max_propositions: 200
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:atomic-opm-libro-rebuilt-74
---

# Atomic opm-libro-rebuilt - Segmento 74

## Resumen

- Productor canonico: `urn:kora:skill:atomize:1.0.0`
- Corpus fuente: `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- Proposiciones: `62`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `74/81`

## Indice de fuentes

- `S01` · [opm-libro.txt](../../../INBOX/opm-libro.txt) · opm libro

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.6.3 Undertime Exception Link

- **P3805** · `fact` · The undertime exception link connects the source process with a destination undertime handling process to specify that if at runtime the performance time of the source process instance is below its Minimal Duration value, then an event initiates the destination process, which is an undertime handling process. · [src:S01:L9824-L9860](../../../INBOX/opm-libro.txt#L9824-L9860)
- **P3806** · `fact` · A minimal-timed process is a process for which the modeler determines a minimal duration. · [src:S01:L9824-L9860](../../../INBOX/opm-libro.txt#L9824-L9860)
- **P3807** · `fact` · An undertime handling process is a time exception process that determines what to do in case the time performance of a minimal timed process falls short of its minimal duration. · [src:S01:L9824-L9860](../../../INBOX/opm-libro.txt#L9824-L9860)
- **P3808** · `fact` · An undertime exception link is a procedural link from a minimal-timed process to an undertime exception process, indicating that if the time performance of a timed process falls short of its minimal allowable time, the undertime exception process is initiated. · [src:S01:L9824-L9860](../../../INBOX/opm-libro.txt#L9824-L9860)
- **P3809** · `fact` · The control modifier for the undertime exception link is a pair of parallel slanted close short bars crossing the link near the overtime exception process. · [src:S01:L9824-L9860](../../../INBOX/opm-libro.txt#L9824-L9860)
- **P3810** · `constraint` · Figure 22.3 is an example of Undertime Exception Handling. · [src:S01:L9824-L9860](../../../INBOX/opm-libro.txt#L9824-L9860)
- **P3811** · `constraint` · Here, {instance id=2} is a particular instance (occurrence) of Processing, whose Duration is 3.4 min. · [src:S01:L9824-L9860](../../../INBOX/opm-libro.txt#L9824-L9860)
- **P3812** · `definition` · Since this value is less than 30.0 min—the minimal time duration defined for the process class Processing, Undertime Exception Handling takes place. · [src:S01:L9824-L9860](../../../INBOX/opm-libro.txt#L9824-L9860)
- **P3813** · `fact` · A source process may have both overtime and undertime links, each connected to a different destination time exception handling process. Suppose in the example in Fig. · [src:S01:L9824-L9860](../../../INBOX/opm-libro.txt#L9824-L9860)
- **P3814** · `constraint` · 22.3 we add an Overtime Exception Handling process, then the additional OPL sentence would be: Overtime Exception Handling occurs if duration of Processing exceeds 60.0 min. · [src:S01:L9824-L9860](../../../INBOX/opm-libro.txt#L9824-L9860)
- **P3815** · `fact` · Unlike most procedural links, which connect an object and a process, but similar to the invocation link, the two time exception links are procedural links that connect two processes directly. · [src:S01:L9824-L9860](../../../INBOX/opm-libro.txt#L9824-L9860)
- **P3816** · `fact` · An implicit interim object Overtime Exception Message or Undertime Exception Message is created by the OPM’s process execution mechanism upon realizing that the process failed to terminate by the maximal allotted time or ended prematurely, falling short of the minimal allotted time, respectively. · [src:S01:L9824-L9860](../../../INBOX/opm-libro.txt#L9824-L9860)
- **P3817** · `fact` · Since the OPM operational mechanism creates and immediately consumes these objects, their depiction is not explicit in the model. · [src:S01:L9824-L9860](../../../INBOX/opm-libro.txt#L9824-L9860)
- **P3818** · `fact` · This is similar to the invocation link, which suppresses the creation of an interim object by the source process and its immediate consumption by the destination process. · [src:S01:L9824-L9860](../../../INBOX/opm-libro.txt#L9824-L9860)
- **P3819** · `constraint` · Table 22.10 summarizes the two time exception links. · [src:S01:L9824-L9860](../../../INBOX/opm-libro.txt#L9824-L9860)
- **P3820** · `fact` · The exceptions these links handle relate only to time, but they can also be used for modeling execution exceptions. · [src:S01:L9824-L9860](../../../INBOX/opm-libro.txt#L9824-L9860)
- **P3821** · `constraint` · For instance, if a process with minimal time duration attached to an undertime exception link is skipped, which means its duration was 0, then the exception handling process is initiated. · [src:S01:L9824-L9860](../../../INBOX/opm-libro.txt#L9824-L9860)

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.7 Transformation Rate

- **P3822** · `constraint` · Often the need arises to model consumption of a consumee or effect on an affectee or creation of a resultee not as a one-time event but rather as a continuous process or a discrete process with a quantity larger than 1, transformed over time. · [src:S01:L9862-L9890](../../../INBOX/opm-libro.txt#L9862-L9890)
- **P3823** · `definition` · We have defined property as an attribute of an OPM element. · [src:S01:L9862-L9890](../../../INBOX/opm-libro.txt#L9862-L9890)
- **P3824** · `fact` · For example, Perseverance is a property of OPM Thing. · [src:S01:L9862-L9890](../../../INBOX/opm-libro.txt#L9862-L9890)
- **P3825** · `fact` · If the value of that property is persistent, the Thing is an Object; if it is transient—it is a Process. · [src:S01:L9862-L9890](../../../INBOX/opm-libro.txt#L9862-L9890)
- **P3826** · `fact` · In other words, we can say that a property is an attribute at the metamodel level, where Thing and Link are OPM Elements. · [src:S01:L9862-L9890](../../../INBOX/opm-libro.txt#L9862-L9890)
- **P3827** · `fact` · Perseverance is an example of a property of a Thing. · [src:S01:L9862-L9890](../../../INBOX/opm-libro.txt#L9862-L9890)
- **P3828** · `fact` · Transformation Rate is a property of a (transforming) Link. · [src:S01:L9862-L9890](../../../INBOX/opm-libro.txt#L9862-L9890)
- **P3829** · `constraint` · Table 22.10 Time exception links summary Transformation rate is a property of a procedural link connecting a transformee B and a process P whose value is the rate of transformation of B by P. · [src:S01:L9862-L9890](../../../INBOX/opm-libro.txt#L9862-L9890)
- **P3830** · `fact` · Just as transformation specializes into consumption, effect, and result, so does transformation rate. · [src:S01:L9862-L9890](../../../INBOX/opm-libro.txt#L9862-L9890)
- **P3831** · `fact` · Consumption rate is the transformation rate of a consumption link connecting a consumee B and a process P whose value is the rate of consumption of B by P. · [src:S01:L9862-L9890](../../../INBOX/opm-libro.txt#L9862-L9890)
- **P3832** · `fact` · Yield rate is the transformation rate of a result link connecting a resultee B and a process P whose value is the rate of creation of B by P. · [src:S01:L9862-L9890](../../../INBOX/opm-libro.txt#L9862-L9890)
- **P3833** · `fact` · Effect rate is the transformation rate of an effect link connecting an affectee B and a process P whose value is the rate of affecting B by P. · [src:S01:L9862-L9890](../../../INBOX/opm-libro.txt#L9862-L9890)
- **P3834** · `fact` · Effect rate can be expressed more specifically as state change rate. · [src:S01:L9862-L9890](../../../INBOX/opm-libro.txt#L9862-L9890)
- **P3835** · `fact` · State change rate is the transformation rate of an in-out link pair whose input and output links connect the input state bi and output state bo of an affectee B to a process P, whose value is the rate of changing the state of B by P from bi to bo. exception if the quantity of the resultee or the consumee is less than the rate times the expected process duration. · [src:S01:L9862-L9890](../../../INBOX/opm-libro.txt#L9862-L9890)

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.8 Computing with OPM

- **P3836** · `fact` · OPM models can be used to carry out numeric calculations. · [src:S01:L9892-L9923](../../../INBOX/opm-libro.txt#L9892-L9923)
- **P3837** · `fact` · The atomic processes for calculations are the four basic arithmetic operations Adding, Subtracting, Multiplying, and Dividing. · [src:S01:L9892-L9923](../../../INBOX/opm-libro.txt#L9892-L9923)
- **P3838** · `fact` · These are used to devise more involved calculations such as Averaging, Geometric Mean Computing, etc. · [src:S01:L9892-L9923](../../../INBOX/opm-libro.txt#L9892-L9923)
- **P3839** · `requirement` · Care must be exercised with operations that are not commutative, like Dividing, where the roles of the Dividend and the Divisor must be explicit in order to get the correct Quotient. · [src:S01:L9892-L9923](../../../INBOX/opm-libro.txt#L9892-L9923)
- **P3840** · `fact` · Since the mathematical expressions are much more compact and understood, once a sufficiently low level of computing is reached, the actual formulae can be recorded as parts of the calculating process names. · [src:S01:L9892-L9923](../../../INBOX/opm-libro.txt#L9892-L9923)
- **P3841** · `fact` · As an industrial example, suppose for the system in Fig. · [src:S01:L9892-L9923](../../../INBOX/opm-libro.txt#L9892-L9923)
- **P3842** · `constraint` · 22.4 we wish to compute the value of residue—the final value of Length of Steel Rod in meters after it has been cut. This is modeled in Fig. · [src:S01:L9892-L9923](../../../INBOX/opm-libro.txt#L9892-L9923)
- **P3843** · `constraint` · 22.5 by the process Residue Length Computing and Fig. · [src:S01:L9892-L9923](../../../INBOX/opm-libro.txt#L9892-L9923)
- **P3844** · `constraint` · 22.6, where Residue Length Computing is in- zoomed. · [src:S01:L9892-L9923](../../../INBOX/opm-libro.txt#L9892-L9923)
- **P3845** · `constraint` · The initial Length of the Steel Rod, il, is 3.00 m. · [src:S01:L9892-L9923](../../../INBOX/opm-libro.txt#L9892-L9923)
- **P3846** · `constraint` · The Machining process, which lasts 3 hr, consumes the Steel Rod at a consumption rate of 0.66 m/hr. · [src:S01:L9892-L9923](../../../INBOX/opm-libro.txt#L9892-L9923)
- **P3847** · `constraint` · The Machining process generates Shaft at a yield rate of 3 units/hr, therefore in 3 hours we get 9 Shafts, as indicated by the participation constraint near Shaft. · [src:S01:L9892-L9923](../../../INBOX/opm-libro.txt#L9892-L9923)
- **P3848** · `constraint` · The length of each Shaft is 0.22 m and the Size of the Shaft Batch (cut during 3 hr) is 9. · [src:S01:L9892-L9923](../../../INBOX/opm-libro.txt#L9892-L9923)
- **P3849** · `constraint` · All these data are provided in the model in Fig. 22.5. · [src:S01:L9892-L9923](../../../INBOX/opm-libro.txt#L9892-L9923)
- **P3850** · `constraint` · Zooming into Residue Length Computing in Fig. 22.6, we see that it has two subprocesses. · [src:S01:L9892-L9923](../../../INBOX/opm-libro.txt#L9892-L9923)
- **P3851** · `fact` · The first is Used Length Computing (u=sl) and the second—Residue Computing (residue=il–u). · [src:S01:L9892-L9923](../../../INBOX/opm-libro.txt#L9892-L9923)
- **P3852** · `fact` · The names of the processes contain in parentheses the arithmetic expressions to be carried out by each process. · [src:S01:L9892-L9923](../../../INBOX/opm-libro.txt#L9892-L9923)
- **P3853** · `fact` · The expression on the first subprocess computes u, the value of Used Length of Rod, as u=sl. · [src:S01:L9892-L9923](../../../INBOX/opm-libro.txt#L9892-L9923)
- **P3854** · `constraint` · It takes s=9 as the value of the Size of the Shaft Batch and l=0.22 m as the Length of each Shaft. · [src:S01:L9892-L9923](../../../INBOX/opm-libro.txt#L9892-L9923)
- **P3855** · `constraint` · The product, u=sl =90.22 =1.98 m, is the input for the next subprocess, in which the model computes residue=il-u, since the length of the residue is the difference between il, the value of the initial Length of the Rod, 3.00 m, and u, the value of Used Length of Rod, so residue=il–u=3.00–0.22=1.02 m. · [src:S01:L9892-L9923](../../../INBOX/opm-libro.txt#L9892-L9923)
- **P3856** · `fact` · Different parameter values will, of course, yield different results. · [src:S01:L9892-L9923](../../../INBOX/opm-libro.txt#L9892-L9923)
- **P3857** · `fact` · This example demonstrates how OPM enables mixing conceptual modeling with quantitative modeling which provides reasoning for the various mathematical steps involved in the computation. · [src:S01:L9892-L9923](../../../INBOX/opm-libro.txt#L9892-L9923)

## opm libro · Chapter 22 OPM Operational Semantics and Control Links / 22.9 Sets and Iterations

- **P3858** · `constraint` · A set is a collection of object instances of the same class. An example of set is provided in Fig. 22.7. · [src:S01:L9925-L9940](../../../INBOX/opm-libro.txt#L9925-L9940)
- **P3859** · `fact` · Shaft Batch is a set of nine object instances from the class Shaft, so creating Shaft Batch implies iteration of Machining nine times, each time producing one Shaft. · [src:S01:L9925-L9940](../../../INBOX/opm-libro.txt#L9925-L9940)
- **P3860** · `fact` · This is a short formal way in OPM to model iteration: Whenever a process is attached with two procedural links of the same kind such that one is a link to a set of n members and the other to a member of the set, the semantics is iteration. · [src:S01:L9925-L9940](../../../INBOX/opm-libro.txt#L9925-L9940)
- **P3861** · `fact` · In our example, the two links are result links: one result link is from Machining to the set Shaft Batch, and the other—from Machining to Shaft. · [src:S01:L9925-L9940](../../../INBOX/opm-libro.txt#L9925-L9940)
- **P3862** · `fact` · The semantics of this template is iteration nine times of creating Shaft. · [src:S01:L9925-L9940](../../../INBOX/opm-libro.txt#L9925-L9940)
- **P3863** · `fact` · This is made more explicit when we zoom into Machining in SD1, expressing the fact that Cutting and Lathing are performed sequentially and iteratively nine times to yield the nine Shafts. · [src:S01:L9925-L9940](../../../INBOX/opm-libro.txt#L9925-L9940)
- **P3864** · `fact` · Each Machining occurrence is a process instance of Machining, within which Cutting and Lathing occur to create each of the nine instances of Shaft. · [src:S01:L9925-L9940](../../../INBOX/opm-libro.txt#L9925-L9940)
- **P3865** · `fact` · Iteration can combine any subset of the procedural links. · [src:S01:L9925-L9940](../../../INBOX/opm-libro.txt#L9925-L9940)
- **P3866** · `fact` · Iteration can, of course, be applied to informatical objects as well, providing a convenient, short way to model iterations, for example, in algorithms, and serve, among many other control constructs (such as Boolean objects), for automated code generation. · [src:S01:L9925-L9940](../../../INBOX/opm-libro.txt#L9925-L9940)
