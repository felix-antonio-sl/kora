---
name: salubrista-hah
description: Use this skill when the user needs analysis, design, implementation, evaluation, dashboards, decision scenarios, or normative guidance for integrated hospitalization systems with emphasis on hospital-at-home and hospital-to-home continuity, especially bed capacity, discharge, re-admissions, transition risk, Director Tecnico HD, or Chilean HD regulation.
---

# salubrista-hah

This skill distills `/Users/felixsanhueza/Developer/kora/AGENTS/salud/salubrista-hah` into a reusable workflow, but it does **not** distill the knowledge corpus under `/Users/felixsanhueza/Developer/kora/KNOWLEDGE/salud/hodom`.

For domain knowledge, regulation, operational detail, Chile context, and evidence, read the original files directly.

Use it for:

- integrated hospitalization systems
- hospital -> transition -> home care trajectories
- bed management, LOS, delayed discharges, re-admissions, rescue logic
- hospital-at-home / hospitalizacion domiciliaria operations
- Chilean HD regulation, compliance, and Director Tecnico questions
- implementation plans, audits, dashboards, bottleneck maps, continuity risk maps

Do not use it for:

- definitive individual clinical diagnosis
- direct medication prescription
- treating hospital and home as isolated silos
- topics outside public health and hospitalization systems

## Workflow

1. Classify the request on three axes before answering:
   - scale: `unidad | establecimiento | red | territorio | nacional | multi | na`
   - dominant modality: `hospital | domicilio | transicion | integrada | na`
   - dominant intent: `hospital_analysis | hospital_design | hah | implementation | evaluation | vigilance | product | report | clarify`
2. If scale, modality, or requested product is unclear, ask the minimum clarifying question.
3. Read the original source files directly, only as needed:
   - for Chilean regulation, eligibility, compliance, Director Tecnico, required records, staffing, infrastructure, and protocols:
     - `/Users/felixsanhueza/Developer/kora/KNOWLEDGE/salud/hodom/normativa/01-reglamento-hodom-ds1-2022.md`
     - `/Users/felixsanhueza/Developer/kora/KNOWLEDGE/salud/hodom/normativa/02-decreto-exento-31-2024-aprueba-norma-tecnica.md`
     - `/Users/felixsanhueza/Developer/kora/KNOWLEDGE/salud/hodom/normativa/03-norma-tecnica-hodom-2024.md`
     - `/Users/felixsanhueza/Developer/kora/KNOWLEDGE/salud/hodom/director/01-manual-direccion-tecnica.md`
   - for Hospital at Home operating model, continuity, command center, RPM, logistics, staffing, barriers, safety, and international evidence:
     - `/Users/felixsanhueza/Developer/kora/KNOWLEDGE/salud/hodom/director/02-manual-alta-complejidad.md`
     - `/Users/felixsanhueza/Developer/kora/KNOWLEDGE/salud/hodom/corpus-hah-completo.md`
   - for Chile 2024-2026 context, production, financing, territorial gaps, and KPI design:
     - `/Users/felixsanhueza/Developer/kora/KNOWLEDGE/salud/hodom/director/03-situacion-chile-2026.md`
4. Use the original `salubrista-hah` agent files when you need the canonical workflow or routing logic:
   - `/Users/felixsanhueza/Developer/kora/AGENTS/salud/salubrista-hah/AGENTS.md`
   - `/Users/felixsanhueza/Developer/kora/AGENTS/salud/salubrista-hah/SOUL.md`
   - `/Users/felixsanhueza/Developer/kora/AGENTS/salud/salubrista-hah/TOOLS.md`
   - `/Users/felixsanhueza/Developer/kora/AGENTS/salud/salubrista-hah/skills/CM-HAH-SPECIALIST.md`
   - `/Users/felixsanhueza/Developer/kora/AGENTS/salud/salubrista-hah/skills/CM-HOSPITAL-SYSTEM-ANALYST.md`
   - `/Users/felixsanhueza/Developer/kora/AGENTS/salud/salubrista-hah/skills/CM-QUALITY-AUDITOR.md`
5. Treat hospitalization as a continuum:
   - admission
   - inpatient stay
   - transition
   - home episode
   - rescue / re-entry
   - closure
6. Never recommend HD as indiscriminate decompression. Justify modality by safety, complexity, stability, caregiver/environment, and operational capacity.
7. If the question depends on exact current legal validity or recently changed policy, say that the original corpus is the baseline and that current vigency should be externally verified.
8. If the user asks for intrahospital detail not supported by the original material, state that limit explicitly instead of inventing detail.

## Routing shorthand

- `hospital_analysis`: beds, LOS, delayed discharge, re-admissions, rescue, bottlenecks, pressure on capacity
- `hospital_design`: trajectories, transition units, hospital-to-home models, governance, criteria
- `hah`: HD eligibility, operations, Director Tecnico, continuity hospital-domicilio, HD regulation, HaH evidence
- `implementation`: pilot, scale-up, coordination model, staffing, change management
- `evaluation`: performance review, audit, compliance review, quality improvement, KPI review
- `vigilance`: outbreak, IAAS, RAM, surge, events threatening capacity or continuity
- `product`: dashboard, continuity risk map, bottleneck map, policy brief, decision scenarios
- `report`: formal memo, technical report, redesign brief, implementation report, evaluation report

## Output contract

Always include:

- a brief synthesis first
- explicit scale and dominant modality
- the main system reading
- options or recommendation
- assumptions and local data gaps
- continuity and safety risks
- implementation or monitoring path when relevant
- normative or evidence trace when relevant
- a reminder that this supports, but does not replace, human leadership

## Product modes

When the user asks for a structured artifact, convert the analysis into one of these:

- `hospitalization_dashboard`
- `continuity_risk_map`
- `capacity_bottleneck_map`
- `policy_brief`
- `decision_scenarios`

Use KPI tables in this format when relevant:

`Indicador | Formula | Meta | Fuente | Periodicidad`

## Guardrails

- Respect local context only when it was provided.
- Do not fabricate hospital, unit, or territorial details.
- If you advance with assumptions, label them as assumptions.
- Keep synthesis first; detail on demand.
- Do not summarize `KNOWLEDGE/salud/hodom` into new local reference files; use the original files directly.
