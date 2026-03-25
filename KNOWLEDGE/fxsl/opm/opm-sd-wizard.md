---
_manifest:
  urn: "urn:fxsl:kb:opm-sd-wizard"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-03-25"
    source: "OPERATIONS/source/fxsl/opm-methodology/opm-curso-sd-wizard.md"
version: "1.0.0"
status: published
tags: [opm, system-diagram, wizard, protocol, sd-construction, checklist]
lang: en
extensions:
  kora:
    depends_on:
      - "urn:fxsl:kb:opm-iso-19450"
      - "urn:fxsl:kb:opm-mbse-foundations"
      - "urn:fxsl:kb:opm-applied-system-modeling"
---

# OPM SD Wizard — System Diagram Construction Protocol

## 1 Definition

This specification defines a 9-step wizard for constructing the System Diagram (SD) of an OPM model. The SD is the top-level, level-zero OPD (Object-Process Diagram) that provides all stakeholders with a bird's-eye view of the system. This wizard covers SD structural construction (Steps 1-9). For the complete 10-step methodology including Problem Occurrence, SD1 refinement, and complexity management, see [Metodologia de Modelamiento OPM](urn:fxsl:kb:metodologia-modelamiento-opm). For formal OPM notation, see [OPM ISO 19450](urn:fxsl:kb:opm-iso-19450). For SD component semantics and worked examples, see [OPM Applied System Modeling](urn:fxsl:kb:opm-applied-system-modeling).

## 2 Definitions

| Term | Definition |
|------|-----------|
| System Diagram (SD) | Top-level OPD defining the system's purpose, scope, and main function in terms of its main object, main process, boundary, and stakeholders |
| Beneficiary | Stakeholder who extracts value and benefits from the system |
| Beneficiary Attribute | Informatical object describing how the beneficiary benefits from the system |
| Transformee | Object that the main process transforms |
| Benefit-Providing Object | Main object of the system, affected by the main process directly or through its attributes |
| Benefit-Providing Attribute | Attribute of the Benefit-Providing Object whose value change delivers the benefit |
| Agent | Human enabler of the main process |
| Instrument | Non-human enabler of the main process |

## 3 Step 1: Main Process Identification

The modeler MUST identify the main process that provides the system's benefit.

The process name MUST end with a verb in gerund form (suffix "-ing").

**Correcto:** `Battery Charging`, `Airplane Flying`, `Road Danger Warning`
**Incorrecto:** `Charge Battery`, `Fly Airplane`, `Road Danger Warn`

The main process SHOULD combine the transformee name followed by the gerund verb when clarity is needed.

## 4 Step 2: Beneficiary Group

The modeler MUST identify the beneficiary group — the stakeholders who extract value from the system.

The beneficiary group name MUST be singular per the Singular Name OPM Principle:
- For humans: add suffix "Group" (e.g., "Passenger Group", "Learner Group")
- For inanimate objects: add suffix "Set" (e.g., "Airplane Set")

The beneficiary group MUST be represented as a physical object.

## 5 Step 3: Beneficiary Attribute and States

The modeler MUST define a beneficiary attribute — an informatical object describing how the beneficiary benefits.

The modeler MUST define exactly two states (values) for this attribute:
- **Input state** (current/problematic): the state before the system operates
- **Output state** (desired/improved): the state after the system delivers its benefit

The main process MUST be connected to these states via an input-output link pair.

The resulting OPL sentence MUST read: "[Main Process] changes [Beneficiary Attribute] of [Beneficiary Group] from [input state] to [output state]."

## 6 Step 4: Agent Identification

The modeler MUST determine whether the beneficiary is also the system's agent.

If agents exist, they MUST be human or groups of humans.

Each agent MUST be connected to the main process via an agent link (solid circle / "black lollipop").

The resulting OPL sentence MUST read: "[Agent] handles [Main Process]."

## 7 Step 5: System Naming

The system is the instrument that enables the main process.

The default system name SHOULD be the main process name followed by "System" (e.g., "Battery Charging System").

The modeler MAY use a commonly accepted name instead (e.g., "Air Traffic Control Tower" instead of "Air Traffic Controlling System").

The main process MUST be modeled as an operation (feature) of the system via exhibition-characterization.

## 8 Step 6: Instrument Identification

The modeler MUST identify instruments — non-human enablers required throughout the process duration.

Each instrument MUST be connected to the main process via an instrument link (open circle / "white lollipop").

The resulting OPL sentence MUST read: "[Main Process] requires [Instrument]."

Instrument names MUST be singular. For multiple instances: use "Set" suffix for inanimate (e.g., "Robot Set"), "Group" suffix for humans.

## 9 Step 7: Input Objects

The modeler MUST identify objects consumed by the main process (inputs that cease to exist after the process).

Each consumed object MUST be connected via a consumption link.

If an object is both input and output (affected, not consumed), it SHOULD be defined in Step 8 instead.

## 10 Step 8: Output Objects

The modeler MUST identify objects created or affected by the main process.

If an output object is also an input (i.e., it exists before and after, but its state changes), the modeler MUST connect it via an input-output link pair specifying the state transition.

## 11 Step 9: Environmental Objects

The modeler MUST identify objects that affect the system's operation but are outside the system engineer's control.

Environmental objects MUST be represented with dashed contour (dashed lines).

Environmental objects MAY serve as instruments or agents of the main process.

## 12 Invariants

The following invariants apply to SD construction. For the complete set including SD1 and deeper levels, see [Metodologia OPM §9](urn:fxsl:kb:metodologia-modelamiento-opm).

| Invariant | Enforcement |
|-----------|-------------|
| Main process name ends in gerund ("-ing") | lint |
| All thing names are singular | lint |
| Beneficiary group is physical object | lint |
| Beneficiary attribute is informatical object | lint |
| Exactly one main process per SD | schema |
| Agent links connect only to humans | manual |
| Instrument links connect only to non-humans | manual |
| Every enabling object persists unchanged after process | manual |
| Environmental objects have dashed contour | lint |
| System exhibits main process via exhibition-characterization | manual |

## 13 Validation

SD-level checks. For the complete multi-level checklist (SD + SD1 + SD2+ + Global), see [Metodologia OPM §10](urn:fxsl:kb:metodologia-modelamiento-opm).

| Check | Condition | Severity |
|-------|-----------|----------|
| Purpose defined | SD contains beneficiary + beneficiary attribute + state transition | CRITICAL |
| Function defined | SD contains main process + main transformee | CRITICAL |
| Enablers present | At least one agent or instrument connected | HIGH |
| Environment identified | At least one environmental object exists | MEDIUM |
| Problem occurrence modeled | Environmental process causes negative state | MEDIUM |
| OPL sentence readable | Generated OPL accurately describes each SD component | HIGH |
| Singular names | All thing names are singular with Set/Group suffixes | HIGH |
| Gerund naming | Main process name uses gerund form | HIGH |
