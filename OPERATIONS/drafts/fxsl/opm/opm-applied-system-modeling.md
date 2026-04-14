---
_manifest:
  urn: "urn:fxsl:kb:opm-applied-system-modeling"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-03-25"
    source: "source/fxsl/opm-methodology/opm-curso-applied-modeling.md"
version: "1.0.0"
status: draft
tags: [opm, system-diagram, sd-method, worked-examples, natural-systems, social-systems, applied-mbse, mobileye, problem-occurrence]
lang: en
extensions:
  kora:
    family: textbook
    depends_on:
      - "urn:fxsl:kb:opm-iso-19450"
      - "urn:fxsl:kb:opm-mbse-foundations"
      - "urn:fxsl:kb:opm-dynamic-behavior"
      - "urn:fxsl:kb:opm-structural-relations"
      - "urn:fxsl:kb:opm-complexity-management"
    course_source: "Dori, D. Model-based Systems Engineering with OPM (MOOC, Technion/edX)."
---

# OPM Applied System Modeling — System Categories, SD Method, and Worked Examples

## Resumen

Este artefacto captura el contenido unico del curso MOOC de Dov Dori sobre MBSE con OPM: el metodo de 5 componentes para construir System Diagrams (SD), la taxonomia de sistemas (artificial/natural/social/socio-tecnico), worked examples completos (Airplane Flying, Mobileye ADAS, Rainstorm, Conference, Professional Network), y aplicaciones industriales. Para definiciones formales ver [OPM Foundations](urn:fxsl:kb:opm-mbse-foundations). Para notacion formal ver [OPM ISO 19450](urn:fxsl:kb:opm-iso-19450).

## System Categories

OPM modela cuatro categorias de sistemas, cada una con particularidades en la construccion del SD.

| Categoria | Proposito/Outcome | Agentes | Problem Occurrence | Ejemplo |
|-----------|-------------------|---------|-------------------|---------|
| Artificial (technological) | Purpose: beneficio intencional para beneficiarios | Humanos | Si (mirror image of purpose) | Electric Car Manufacturing |
| Natural | Outcome: efecto sobre affectees (beneficial o detrimental) | No humanos involucrados | Generalmente no aplica | Rainstorm, Fetus Developing, Tree Growing |
| Social | Purpose: beneficio via interaccion humana | Humanos | Si | Conference, Community |
| Socio-technical | Purpose: integra tecnologia + aspectos sociales | Humanos + instruments | Si | Professional Network, MOOC |

### Natural Systems — Outcome vs Purpose

Los sistemas naturales no fueron disenados por humanos → no tienen purpose. El modelador asigna un **outcome** dependiendo de su objetivo de investigacion. Un outcome puede ser beneficial o detrimental.

Componentes del SD de un sistema natural:
- Main function: si
- Process enablers: si (pero sin agentes humanos)
- Environment: si
- Purpose: **no** → se reemplaza por outcome
- Problem occurrence: **generalmente no**

### Socio-Technical Systems — Tagged Structural Links

Los sistemas socio-tecnicos frecuentemente requieren **tagged structural links** para expresar relaciones que no caen en las cuatro fundamentales. Ejemplo: "Online Professional Profile **represents** User" — una relacion user-defined entre un objeto informatical y un objeto fisico.

## System Diagram (SD) — 5-Component Method

El SD es el nivel cero (top-level) del modelo OPM. Debe ser simple y claro, con minimos detalles tecnicos. Todos los stakeholders — managers, customers, suppliers, domain experts — deben poder entender el SD sin expertise tecnico.

### Component 1: Purpose

Identifica:
1. **Beneficiary Group** — grupo de personas que reciben valor del sistema
2. **Beneficiary Attribute** — atributo informatical del beneficiary cuyo valor cambia beneficiosamente
3. **Input state** (problematico) y **output state** (deseado)

OPL pattern: "[Main Process] changes [Beneficiary Attribute] of [Beneficiary Group] from [input] to [output]."

### Component 2: Main Function

Identifica:
1. **Main Process** — gerund naming (ej: "Airplane Flying")
2. **Main Transformee** (Benefit-Providing Object) — objeto principal transformado
3. **Benefit-Providing Attribute** — atributo del transformee que cambia de problematic a satisfactory

La funcion combina transformee + proceso: "Airplane Flying", "Baggage Transporting", "Battery Charging".

Cuando el main process transforma multiples transformees, solo el Benefit-Providing Object es parte de la funcion. Otros transformees (ej: Heat producido por Battery Charging, Electric Energy consumido) son importantes pero no definen la funcion.

### Component 3: Enablers

- **Agent** (humano): solid circle link ("black lollipop"). OPL: "[Agent] handles [Process]."
- **Instrument** (inanimado): open circle link ("white lollipop"). OPL: "[Process] requires [Instrument]."

El sistema mismo es siempre un instrument de su main process. Default naming: "[Function] System" (ej: "Air Traffic Controlling System").

Un object puede ser simultaneamente agent de un proceso y transformee de otro. Ejemplo: Learner es agent de MOOC Learning pero tambien transformee (knowledge level cambia).

### Component 4: Environment

Identifica things (objects y processes) que afectan el sistema pero estan fuera del control del systems engineer.

- **Systemic things**: contour solido
- **Environmental things**: contour dashed (dashed lines)

Un mismo objeto puede ser systemic en un modelo y environmental en otro. Ejemplo: Air Traffic Control Tower es systemic en el Air Traffic Controlling System pero environmental en el Airplane Flying System.

### Component 5: Problem Occurrence

Mirror image del purpose y main function. Modela:
1. **Environmental process** que causa el problema
2. El problema causa que el beneficiary attribute este en su **negative state** (input state del purpose)
3. Y que el benefit-providing attribute este en su **problematic state**

OPL pattern: "[Environmental Process] yields [Beneficiary Attribute] of [Beneficiary Group] at state [negative] and [Benefit-Providing Attribute] at state [problematic]."

Ejemplo: "Human-centered Electric Car Manufacturing yields Business Success of Company Stakeholder Group at state current and Manufacturing Automation Level of Electric Car at state partial."

## Worked Examples — Complete SD Constructions

### Airplane Flying (artificial, physical)

| SD Component | Valor |
|-------------|-------|
| Beneficiary | Passenger Group |
| Beneficiary Attribute | Travel Time (long → short) |
| Main Process | Airplane Flying |
| Main Transformee | Airplane |
| Benefit-Providing Attribute | Location (origin → destination) |
| Agents | Air Traffic Controller, Pilot (environmental) |
| Instruments | Air Traffic Control Tower, Airplane |
| Environment | Air Traffic Control Tower (when modeled from Flying system perspective) |

### Baggage Transporting (artificial, physical+informatical)

| SD Component | Valor |
|-------------|-------|
| Beneficiary | Passenger Group |
| Main Process | Baggage Transporting |
| Main Transformee | Baggage |
| Benefit-Providing Attribute | Airport Location (origin → destination) |
| Environment | Electrical Energy |

Physical system con componentes informaticales (location tracking). Un thing con partes physical e informatical se clasifica como physical.

### Battery Charging (artificial, multi-transformee)

| SD Component | Valor |
|-------------|-------|
| Main Process | Battery Charging |
| Main Transformee | Battery |
| Benefit-Providing Attribute | Charge Level (depleted → fully charged) |
| Other Transformees | Electric Energy (consumed), Thermal Energy (produced/result) |

Demuestra que el main process puede conectarse a multiples transformees, pero la funcion solo incluye el Benefit-Providing Object.

### Fetus Developing (natural, beneficial outcome)

| SD Component | Valor |
|-------------|-------|
| Outcome | Fetus development from embryo to baby |
| Main Process | Fetus Developing |
| Main Transformee | Fetus (embryo → baby) |
| Agents | None (natural system) |

Simplificacion: Developmental Stage attribute puede eliminarse asignando embryo/baby como states del Fetus directamente.

### Mobileye ADAS (artificial, safety-critical)

| SD Component | Valor |
|-------------|-------|
| Beneficiary | Driver |
| Beneficiary Attribute | Crash Probability (high → low) |
| Main Process | Vehicle-in-Front Detecting & Crash Alerting |
| Instruments | Mobileye System (systemic), Vehicle-in-Front (environmental) |
| Environment | Driver (environmental — no controla el sistema), Car |
| Problem | Car approaching → Driver not aware → Crash probability increases |

### Rainstorm (natural, detrimental outcome)

| SD Component | Valor |
|-------------|-------|
| Outcome | Safety Level of Passenger Group decreases (high → low) — detrimental |
| Main Process | Rain Storm Forming |
| Instruments | Warm Ocean Water |
| Environment | Ocean, Atmosphere |
| Agents | None (natural) |

Demuestra que el outcome de un sistema natural puede ser detrimental.

### Conference (social)

| SD Component | Valor |
|-------------|-------|
| Beneficiary | Company Stakeholder Group |
| Beneficiary Attribute | Business Success (current → improved) |
| Main Process | Conference Occurring |
| Main Function | Business Cooperation (loose → tight) |
| Agents | Organizer, Usher Group |
| Instruments | Equipment |
| Environment | Weather (state-specified instrument: good) |
| Problem | Business Declining (environmental process) |

Demuestra **state-specified enabling link**: Weather connected via state "good" al proceso (solo con buen clima el proceso ocurre).

### Professional Network (socio-technical)

| SD Component | Valor |
|-------------|-------|
| Beneficiary | User |
| Beneficiary Attribute | Professional Success (current → improved) |
| Main Process | Online Professional Identity Managing |
| Main Function | Online Professional Profile (unmanaged → managed) |
| Agents | User, Other User Group |
| Instruments | Online Professional Identity Managing System |
| Environment | Internet (environmental instrument) |
| Tagged Structural Link | "Online Professional Profile **represents** User" |
| Problem | Offline Professional Identity Managing (environmental process) |

## SD1 Refinement — First Detail Level

SD1 refina el main process de SD, exponiendo sub-procesos y objetos asociados.

### Synchronous Process Refinement (Mobileye)

Refinamiento por **in-zooming**: nuevo OPD con main process inflado, sub-procesos dispuestos verticalmente segun **Timeline OPM Principle** (top = primero, bottom = ultimo).

Sub-procesos del Mobileye ADAS:

| Sub-proceso | Transformacion de Vehicle-in-Front Representation |
|-------------|---------------------------------------------------|
| Detecting | not detected → detected (braking time 10s) |
| Informing | detected → driver informed (braking time ≤ 2.5s, green display) |
| Alerting | driver informed → driver warned (braking time ≤ 1.2s, red + beep) |
| Crash Alerting | driver warned → crash alerting (braking time ≤ 0.7s, big red icon + beeps) |

**Reglas de modelado SD1:**
- Todo sub-proceso DEBE estar conectado a al menos un transformee
- Vehicle-in-Front Representation es attribute de Mobileye System (exhibition-characterization)
- En SD: effect link (sin detalle de estados). En SD1: input-output link pairs (estados explicitos)
- State suppression en SD, state expression en SD1
- Evitar redundancia: no repetir enablers ya modelados en SD

### Asynchronous Process Refinement (Road Danger Warning)

Refinamiento por **unfolding**: nuevo OPD con sub-procesos conectados al main process via **generalization-specialization** (cada sub-proceso es un tipo de alerta, no una parte secuencial).

Sub-procesos:
- Vehicle-in-Front Crash Alerting
- Pedestrian-in-Front Crash Alerting
- Lane Deviation Alerting

Cada sub-proceso transforma su propio objeto representacional. Un objeto general "Road Danger Representation" generaliza las tres representaciones especificas y se agrega al SD (no las tres individuales, para mantener simplicidad).

### Object Refinement

Los objetos se refinan en SD1 via unfolding (no in-zooming, pues los objetos son estaticos). Ejemplo: Mobileye System refinado a 3 partes (aggregation) + 1 atributo (exhibition):
- Camera, Computer, Display (parts)
- Representation Set (attribute)

El OPD resultante muestra un "object tree": refineable + refinee (parts + attributes).

## Industrial Applications of OPM

| Organizacion | Aplicacion |
|-------------|-----------|
| Whirlpool Corporation | Diseno innovador de electrodomesticos (refrigerators, dishwashers) |
| Aircraft manufacturers | Modelado de sistemas de aviones comerciales, knowledge management, business processes |
| Car industry | End-to-end vehicle control |
| International Space Station | Robotic arm design and operation |
| Insurance industry | New product design |
| Molecular biology research | Research systems modeling |
| Mobileye (Intel) | ADAS systems for autonomous vehicles |
| Technion Robotics Lab | Fruit serving robots, manufacturing automation |

## Emergence in System Architecture

> Emergence is the appearance of a capability or functionality that characterizes the entire system but not any one of its constituent parts.

La combinacion de structure + behavior que da lugar a emergence es la **system architecture**. La arquitectura habilita al sistema a funcionar y entregar beneficio.

Ejemplo: Road Danger Warning system — separar sus partes individuales (camera, computer, display, algorithms) no produce la capacidad de alerta; solo el sistema integrado la exhibe.
