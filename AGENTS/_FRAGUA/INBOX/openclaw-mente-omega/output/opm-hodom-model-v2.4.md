# Modelo OPM — Sistema de Hospitalización Domiciliaria (HODOM)

Modelo conceptual conforme a ISO/PAS 19450 (OPM).
Versión: 2.5 (auditoría exhaustiva profunda — 11 hallazgos de auditoría v2.5)
Fecha: 2026-04-02

Fuentes normativas:
- DS N° 1/2022, Reglamento de Establecimientos que Otorgan Prestaciones de Hospitalización Domiciliaria.
- Decreto Exento N° 31/2024, que aprueba la Norma Técnica para Hospitalización Domiciliaria.
- Norma Técnica HODOM 2024 (16 páginas, parte integrante del Decreto Exento N° 31).
- Manual REM 2026 (DEIS), Serie A21 Sección C: Hospitalización Domiciliaria y Atención Ventilatoria en Domicilio.

Fuentes complementarias:
- Modelo Categórico HODOM v4.1 (27 fuentes, datos reales HSC 2023-2026)

---

## Changelog v2.4 → v2.5

| ID | Severidad | Corrección aplicada |
|----|-----------|---------------------|
| H1 | CRÍTICA | SD1.6: 6 nombres EN de tipos de egreso corregidos a gerundio (Medical Discharging, Hospital Readmission Discharging, Expected Death Discharging, Unexpected Death Discharging, Voluntary Withdrawal Discharging, Disciplinary Discharging) — invariante §15 ISO naming |
| H2 | ALTA | SD1: ciclo iterativo tratamiento-monitoreo modelado con invocación condicional (Clinical Evolution Monitoring invokes Therapeutic Plan Executing si continue-treatment) |
| H3 | ALTA | SD1: Clinical Record creado por Patient Admitting (yields), finalizado por Patient Discharging (changes active→finalized) — corrige inconsistencia temporal |
| H4 | ALTA | SD1.2: Social Diagnosis Elaborating `affects Patient Home` → `requires Patient Home` (instrumento, no affectee) |
| H5 | ALTA | SD1/SD1.2: Derivation Origin con XOR result fan state-specified (6 estados mutuamente excluyentes) |
| H6 | MEDIA | SD1.6: sentencias compuestas con condition+effect sobre objetos distintos separadas en sentencias conformes (Expected Death Discharging, Disciplinary Discharging) |
| H7 | MEDIA | SD1.6: redundancia en Expected Death Discharging eliminada (resuelta por H6) |
| H8 | MEDIA | SD1.4a: Operational Productivity cambiado de affects a yields; estado default agregado |
| H9 | MEDIA | SD1.1: Insurance Status condition normalizado a sintaxis OR fan (`at least one of`) |
| H10 | BAJA | SD1.4a: GPS Tracking System anclado como parte de Communication System |
| H11 | BAJA | SD3/SD6: `Pharmacy or Authorized Dispensary` renombrado a `Medication Dispensary` / `Dispensario de Medicamentos` — Singular Name Principle |

---

## Changelog v2.3 → v2.4

| ID | Severidad | Corrección aplicada |
|----|-----------|---------------------|
| G1 | CRÍTICA | §4.3: Referral Facility Coordinating sin transformee en SD1.2 — agregado `yields Referral Coordination Record` |
| G2 | CRÍTICA | §7.4: Split link no resuelto — `Clinical Evolution Monitoring changes Clinical Condition` removido de SD1; transición asignada exclusivamente a `Medical Discharge changes Clinical Condition from acute-reacutized to recovered` en SD1.6 (split output link) |
| G3 | ALTA | §7.4: Split link no resuelto — `Eligibility Evaluating changes Eligibility Status from pending to eligible` delegada a `Informed Consent Obtaining` como último subproceso en SD1.1 |
| G4 | ALTA | SD1 vs SD8 inconsistencia — Eligibility Evaluating en SD1 armonizado como condicional conforme a SD8 |
| G5 | ALTA | SD1.6: Voluntary Withdrawal Discharge sin agente — agregado `Attending Physician handles Voluntary Withdrawal Discharge` |
| G6 | ALTA | SD1/SD1.6: doble propiedad de Clinical Condition→recovered — resuelta a favor de Medical Discharge como único propietario (ver G2) |
| G7 | ALTA | SD6: Waste Managing sin agente — agregado `Coordination Professional handles Waste Managing` |
| G8 | ALTA | SD1.4: Speech Therapy Executing sin link a Swallowing and Speech Status — agregado `affects Swallowing and Speech Status` |
| G9 | MEDIA | SD1: Nursing Care Plan sin default/final — agregado `State active is default` y `State completed is final` |
| G10 | MEDIA | SD1.5: Patient Category sin initial — agregado `State stable is initial` |
| G11 | MEDIA | SD1: Hospitalization Status sin proceso creador — agregado `Patient Admitting yields active Hospitalization Status` |
| G12 | MEDIA | OPL-ES: `es informatical` normalizado a `es informático/a` con concordancia de género en ~60 instancias |
| G13 | BAJA | Nombres de proceso ES: plurales residuales corregidos (Condiciones→Condición, Pacientes→Paciente, Profesionales→Profesional) |
| G14 | BAJA | Nombres de proceso ES >4 palabras acortados: *Enviar Contrarreferencia* (antes 5 palabras); *Reportar Estado Clínico* (antes 5 palabras) |

---

## Changelog v2.2 → v2.3

| ID | Severidad | Corrección aplicada |
|----|-----------|---------------------|
| F1a | CRÍTICA | §4.4: Wound Care Executing — dual changes Wound Status reemplazado por single `affects Wound Status`; transiciones multi-paso diferidas a futuro SD1.4c (in-zooming de Wound Care Executing) |
| F1b | CRÍTICA | §4.4: Daily Logistics Managing — dual changes Daily Schedule Status reemplazado por single `affects Daily Schedule Status`; transiciones distribuidas a subprocesos en SD1.4a (Visit Sequencing changes pending→assigned; Route Execution Monitoring changes assigned→executed) |
| F1c | CRÍTICA | §4.4: Weekly Schedule Cycling — dual changes Operational Mode reemplazado por single `affects Operational Mode` |
| F2 | CRÍTICA | §4.3: Clinical Condition Evaluating sin transformee — agregado `yields Clinical Assessment Record` como producto documental del proceso |
| F3a | ALTA | Estado muerto `ineligible` eliminado de Eligibility Status (SD1) — inalcanzable por skip semantics de condition links |
| F3b | ALTA | Estado muerto `ineligible` eliminado de Candidate (SD1.1) — inalcanzable |
| F4 | ALTA | Post-Discharge Following sin transformee en SD1 — agregado `yields Discharge Outcome` como transformee representativo |
| F5 | ALTA | Acute Clinical Instability output-state indeterminado — cambiado a `changes from present to absent` (input-output-specified) |
| F6 | ALTA | Therapy Type: `requires` (wait) cambiado a condition instrument con skip — semántica correcta para terapias no universalmente prescritas |
| F7 | ALTA | Convención de agencia documentada: nota arquitectural explícita justifica asignación de agentes como partes (aggregation) del Healthcare Team en lugar de especializaciones (ISO §9.9 override). Justificación: el dominio clínico opera por roles profesionales reglamentados, no por especialización taxonómica |
| F8a | ALTA | Patient Documentation Delivering: `affects Patient Group` → `requires Patient Group` — el proceso entrega documentos, no transforma al paciente |
| F8b | ALTA | Convención de `affects Patient Group` genérico documentada en nota: efecto incremental distribuido entre encuentros clínicos; transiciones específicas de Clinical Condition modeladas en SD1.5 |
| F9 | ALTA | OPL-EN: sintaxis state-specified normalizada — `X in state` → `state X` conforme EBNF ISO en ~20 instancias (yields, requires) |
| F10 | MEDIA | Redundancia eliminada: `Home Condition Evaluating affects Patient Home` removido — cubierto por `changes Home Condition from inadequate to adequate` |
| F13 | MEDIA | Voluntary Withdrawal Discharge: `requires Informed Consent` → `requires signed Informed Consent` |
| F14 | MEDIA | Derivation Origin: `initial` state eliminado intencionalmente — XOR fan runtime, estado determinado por context de derivación |
| F15 | BAJA | SD1.4 checklist: 26 entidades cambiado de PASS a WARN (consistente con tratamiento de SD6) |

---

## Changelog v2.1 → v2.2

| ID | Severidad | Corrección aplicada |
|----|-----------|---------------------|
| H1 | CRÍTICA | Unicidad de rol en SD1 Care Planning: elimina doble rol yields+changes; reemplaza por yields in active (draft→active es detalle de SD1.3) |
| H2 | CRÍTICA | Unicidad de rol en SD1.3 Plan Activating: elimina dos requires (el input-specified effect link ya porta la precondición) |
| H3 | ALTA | SD10: elimina exhibition de Weekly Schedule Cycling (proceso ambiental no es feature del sistema) |
| H4 | ALTA | SD: esencia de Acute Episode Occurring corregida de Informatical a Physical/Físico (tabla + OPL-EN + OPL-ES) |
| H5 | ALTA | SD1.7: estados muertos eliminados — Follow-Up Status: elimina `completed`; Counterreferral Status: elimina `acknowledged` |
| H6 | ALTA | SD1: Eligibility Status — agrega estado `admitted`; Patient Admitting con transición explícita eligible→admitted |
| H7 | ALTA | Satisfaction Survey: herencia corregida — eliminada de Patient Discharging (SD1); asignada a Medical Discharge y Voluntary Withdrawal Discharge (SD1.6) |
| H8 | ALTA | SD1 tabla: Support Network esencia corregida de Físico a Informatical |
| H10 | ALTA | Plurales ES corregidos: Pesquisar Candidatos→Pesquisar Candidato; Resolver Visitas sin Ruta→Resolver Visita sin Ruta |
| H11 | MEDIA | SD1 tabla: Caregiver afiliación corregida de Sistémico a Ambiental |
| H12 | MEDIA | SD1.4: Caregiver Educating con transición explícita de atributo Caregiver Knowledge |
| H13 | MEDIA | SD1.4: Therapy Type cambia de affects a requires (condition instrument, no effect) |
| H14 | MEDIA | SD1.4b: dual agent en Clinical Responsibility Transferring (Outgoing + Incoming Clinical Nurse) |
| H15 | MEDIA | SD9 y SD: Primary Care Center bidireccional con tags semánticos (refers/counterrefers) |
| H16 | MEDIA | SD1.6: Clinical Instability renombrado a Acute Clinical Instability en todas las ocurrencias |
| H17 | BAJA | SD1.1: default state de Patient Age y Hospital Distance eliminados (condition links ya expresan la condición) |

---

## Changelog v2.0 → v2.1

| ID | Severidad | Corrección aplicada |
|----|-----------|---------------------|
| C1 | CRÍTICA | 5 tagged structural links objeto↔proceso reemplazados por links conformes (instrument links + tagged structural obj↔obj) |
| C2 | CRÍTICA | Brecha draft→active cerrada: nuevo subproceso *Plan Activating* en SD1.3 |
| C3 | CRÍTICA | Result link duplicado eliminado en Application Receiving↔Candidate (SD1.1); solo effect link |
| C4 | CRÍTICA | Doble default state corregido en Route Assignment (SD1.4a); solo `assigned` es default |
| A1 | ALTA | Scope leaks eliminados: hechos de SD1.7 removidos de SD1; hechos de SD1.4b removidos de SD1.4; referencia a Patient Discharging removida del SD |
| A2 | ALTA | Nombre de proceso ES corregido: *Episodio Agudo* → *Ocurrir Episodio Agudo* |
| A3 | ALTA | Condition agent sin skip clause: Remote Care Regulating y Follow-Up Call Executing corregidos (agente condicional sin skip porque existe agente incondicional) |
| A4 | ALTA | Consumption→instrument: Clinical Record Updating requiere (no consume) Vital Signs Data |
| A5 | ALTA | Consumption→instrument: Counterreferral Sending requiere (no consume) Epicrisis |
| A6 | ALTA | Regulating Physician integrado a SD2 como parte opcional y conectado a procesos en SD9 |
| A7 | ALTA | Social Report: Home Condition Evaluating genera Preliminary Social Report; Social Diagnosis Elaborating genera Social Report (nombres diferenciados) |
| A8 | ALTA | Clinical Condition Evaluating: effect link removido; reemplazado por condition instrument (verifica condición clínica como precondición) |
| A9 | ALTA | Validación SD6: flaggeado correctamente como excedente de 25 entidades |
| A10 | ALTA | Estados renombrados: `gte_18`→`adulto`, `lte_20km`→`dentro_de_cobertura` |
| M1 | MEDIA | Midwife, Psychologist, Occupational Therapist movidos a colección incompleta ("at least one other part") |
| M2 | MEDIA | Operational Mode: links cambiados a condition instrument (skip semantics) para procesos que no ocurren fin de semana |
| M3 | MEDIA | Weekly Schedule Cycling: esencia corregida de Físico a Informatical |
| M4 | MEDIA | Discharge Outcome Evaluating: XOR fan explícito para estados favorable/unfavorable |
| M5 | MEDIA | Nombre largo corregido: *Egresar por Fallecimiento no Esperado* → *Egresar por Muerte Inesperada* |
| M6 | MEDIA | Nombre ES de proceso ambiental corregido (cubierto por A2) |
| M7 | MEDIA | Referencias normativas primarias agregadas a secciones que carecían |
| B1 | BAJA | Typo "Objetro" corregido a "Objeto" en checklist SD10 |
| B2 | BAJA | Estados normalizados: underscores reemplazados por guiones en nombres de estado |
| B3 | BAJA | Coexistencia tagged structural + procedural de Caregiver declarada explícitamente |

---

## Clasificación del Sistema

**Tipo:** Socio-técnico
**Justificación:** Combina agentes humanos (equipo clínico multidisciplinario), infraestructura física (equipamiento médico, vehículos, oficinas), sistemas informaticales (fichas clínicas, comunicaciones, protocolos) y un marco normativo-regulatorio con supervisión estatal. Las relaciones entre actores, pacientes, cuidadores e instituciones son inherentemente sociales. Se modelan los 5 componentes completos del SD. Se usan tagged structural links para relaciones institucionales.

---

## SD — System Diagram (Nivel 0)

### Tabla de Elementos SD

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Domiciliary Hospitalizing* | Físico | Sistémico | — |
| Objeto | **Patient Group** | Físico | Sistémico | — |
| Objeto | **Clinical Condition** | Informatical | Sistémico | `acute-reacutized`, `recovered` |
| Objeto | **Domiciliary Hospitalization System** | Físico | Sistémico | — |
| Objeto | **Healthcare Team** | Físico | Sistémico | — |
| Objeto | **Medical Equipment** | Físico | Sistémico | — |
| Objeto | **Communication System** | Físico | Sistémico | — |
| Objeto | **Transport Vehicle** | Físico | Sistémico | — |
| Objeto | **Administrative Infrastructure** | Físico | Sistémico | — |
| Objeto | **Clinical Supply** | Físico | Sistémico | — |
| Objeto | **Medication** | Físico | Sistémico | — |
| Objeto | **Clinical Record** | Informatical | Sistémico | — |
| Objeto | **Patient Home** | Físico | Ambiental | — |
| Objeto | **Inpatient Facility** | Físico | Ambiental | — |
| Objeto | **Current Regulation** | Informatical | Ambiental | — |
| Objeto | **Primary Care Center** | Físico | Ambiental | — |
| Objeto | **Digital Application System** | Informatical | Sistémico | — |
| Proceso | *Acute Episode Occurring* | Physical | Ambiental | — |

### Tabla de Enlaces SD

| Tipo | Origen | Destino | Justificación |
|------|--------|---------|---------------|
| Exhibition-characterization | **Domiciliary Hospitalization System** | *Domiciliary Hospitalizing* | Sistema exhibe función principal |
| Exhibition-characterization | **Patient Group** | **Clinical Condition** | Beneficiario exhibe atributo de valor |
| Effect (input-output) | *Domiciliary Hospitalizing* | **Clinical Condition** | Transformación principal |
| Agent | **Healthcare Team** | *Domiciliary Hospitalizing* | Agente humano |
| Instrument | *Domiciliary Hospitalizing* | **Medical Equipment** | Enabler no humano |
| Instrument | *Domiciliary Hospitalizing* | **Communication System** | Enabler no humano |
| Instrument | *Domiciliary Hospitalizing* | **Transport Vehicle** | Enabler no humano |
| Instrument | *Domiciliary Hospitalizing* | **Administrative Infrastructure** | Enabler no humano |
| Instrument | *Domiciliary Hospitalizing* | **Digital Application System** | Enabler no humano |
| Instrument | *Domiciliary Hospitalizing* | **Patient Home** | Contexto espacial habilitante [C1] |
| Consumption | *Domiciliary Hospitalizing* | **Clinical Supply** | Consumible |
| Consumption | *Domiciliary Hospitalizing* | **Medication** | Consumible |
| Result | *Domiciliary Hospitalizing* | **Clinical Record** | Producto documental |
| Tagged structural (obj↔obj) | **Inpatient Facility** | **Patient Group** | Derivación: Inpatient Facility refers Patient Group [C1] |
| Tagged structural (obj↔obj) | **Primary Care Center** | **Patient Group** | Derivación y contrarreferencia [C1] |
| Tagged structural (obj↔obj) | **Domiciliary Hospitalization System** | **Primary Care Center** | Bidireccional con tags: refers/counterrefers [H15] |
| Tagged structural (obj↔obj) | **Current Regulation** | **Domiciliary Hospitalization System** | Normativa rige sistema |
| Effect (env) | *Acute Episode Occurring* | **Clinical Condition** | Problem occurrence |

### OPL-EN del SD

```
Domiciliary Hospitalization System is physical.
Domiciliary Hospitalization System exhibits Domiciliary Hospitalizing.
Patient Group is physical.
Patient Group exhibits Clinical Condition.
Clinical Condition can be acute-reacutized or recovered.
State acute-reacutized of Clinical Condition is initial.
State recovered of Clinical Condition is final.
Domiciliary Hospitalizing changes Clinical Condition from acute-reacutized to recovered.
Healthcare Team handles Domiciliary Hospitalizing.
Domiciliary Hospitalizing requires Medical Equipment.
Domiciliary Hospitalizing requires Communication System.
Domiciliary Hospitalizing requires Transport Vehicle.
Domiciliary Hospitalizing requires Administrative Infrastructure.
Domiciliary Hospitalizing requires Digital Application System.
Domiciliary Hospitalizing requires Patient Home.
Domiciliary Hospitalizing consumes Clinical Supply.
Domiciliary Hospitalizing consumes Medication.
Domiciliary Hospitalizing yields Clinical Record.
Inpatient Facility is physical.
Inpatient Facility is environmental.
Inpatient Facility refers Patient Group.
Primary Care Center is physical.
Primary Care Center is environmental.
Primary Care Center refers Patient Group.
Domiciliary Hospitalization System refers Primary Care Center.
Primary Care Center counterrefers Domiciliary Hospitalization System.
Current Regulation is informatical.
Current Regulation is environmental.
Current Regulation governs Domiciliary Hospitalization System.
Acute Episode Occurring is physical.
Acute Episode Occurring is environmental.
Acute Episode Occurring changes Clinical Condition to acute-reacutized.
```

### OPL-ES del SD

```
**Sistema de Hospitalización Domiciliaria** es físico.
**Sistema de Hospitalización Domiciliaria** exhibe *Hospitalizar en Domicilio*.
**Grupo de Pacientes** es físico.
**Grupo de Pacientes** exhibe **Condición Clínica**.
**Condición Clínica** puede estar `agudo-reagudizado` o `recuperado`.
Estado `agudo-reagudizado` de **Condición Clínica** es inicial.
Estado `recuperado` de **Condición Clínica** es final.
*Hospitalizar en Domicilio* cambia **Condición Clínica** de `agudo-reagudizado` a `recuperado`.
**Equipo de Salud** maneja *Hospitalizar en Domicilio*.
*Hospitalizar en Domicilio* requiere **Equipamiento Médico**.
*Hospitalizar en Domicilio* requiere **Sistema de Comunicación**.
*Hospitalizar en Domicilio* requiere **Vehículo de Transporte**.
*Hospitalizar en Domicilio* requiere **Infraestructura Administrativa**.
*Hospitalizar en Domicilio* requiere **Sistema de Postulación Digital**.
*Hospitalizar en Domicilio* requiere **Domicilio del Paciente**.
*Hospitalizar en Domicilio* consume **Insumo Clínico**.
*Hospitalizar en Domicilio* consume **Medicamento**.
*Hospitalizar en Domicilio* genera **Ficha Clínica**.
**Establecimiento de Atención Cerrada** es físico.
**Establecimiento de Atención Cerrada** es ambiental.
**Establecimiento de Atención Cerrada** deriva **Grupo de Pacientes**.
**Centro de Salud Familiar** es físico.
**Centro de Salud Familiar** es ambiental.
**Centro de Salud Familiar** deriva **Grupo de Pacientes**.
**Sistema de Hospitalización Domiciliaria** deriva a **Centro de Salud Familiar**.
**Centro de Salud Familiar** contrarefiere a **Sistema de Hospitalización Domiciliaria**.
**Normativa Vigente** es informática.
**Normativa Vigente** es ambiental.
**Normativa Vigente** rige **Sistema de Hospitalización Domiciliaria**.
*Ocurrir Episodio Agudo* es físico.
*Ocurrir Episodio Agudo* es ambiental.
*Ocurrir Episodio Agudo* cambia **Condición Clínica** a `agudo-reagudizado`.
```

Ref. normativa: DS 1/2022 art. 2 (definición HODOM); NT 2024 §1 (alcance); DS 1/2022 art. 15 (criterios de ingreso).

---

## SD1 — Descomposición de *Domiciliary Hospitalizing*

Refinamiento: in-zooming (subprocesos secuenciales).

### Tabla de Elementos SD1

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Eligibility Evaluating* | Informatical | Sistémico | — |
| Proceso | *Patient Admitting* | Informatical | Sistémico | — |
| Proceso | *Care Planning* | Informatical | Sistémico | — |
| Proceso | *Therapeutic Plan Executing* | Físico | Sistémico | — |
| Proceso | *Clinical Evolution Monitoring* | Informatical | Sistémico | — |
| Proceso | *Patient Discharging* | Informatical | Sistémico | — |
| Proceso | *Post-Discharge Following* | Informatical | Sistémico | — |
| Objeto | **Eligibility Status** | Informatical | Sistémico | `pending`, `eligible`, `admitted` [H6, F3a] |
| Objeto | **Informed Consent** | Informatical | Sistémico | `unsigned`, `signed` |
| Objeto | **Therapeutic Plan** | Informatical | Sistémico | `draft`, `active`, `completed` |
| Objeto | **Nursing Care Plan** | Informatical | Sistémico | `draft`, `active`, `completed` |
| Objeto | **Social Report** | Informatical | Sistémico | — |
| Objeto | **Admission Form** | Informatical | Sistémico | — |
| Objeto | **Domiciliary Clinical Summary** | Informatical | Sistémico | — |
| Objeto | **Epicrisis** | Informatical | Sistémico | — |
| Objeto | **Satisfaction Survey** | Informatical | Sistémico | — |
| Objeto | **Continuity Decision** | Informatical | Sistémico | `continue-treatment`, `proceed-discharge` |
| Objeto | **Hospitalization Status** | Informatical | Sistémico | `active`, `discharged` |
| Objeto | **Caregiver** | Físico | Ambiental [H11] | `available`, `unavailable` |
| Objeto | **Support Network** | Informatical [H8] | Sistémico | `verified`, `insufficient` |
| Objeto | **Derivation Origin** | Informatical | Sistémico | `inpatient-ward`, `emergency-unit`, `primary-care`, `outpatient`, `urgency-law`, `centralized-bed-management` |

### OPL-EN del SD1

```
SD is refined by in-zooming Domiciliary Hospitalizing in SD1.
Domiciliary Hospitalizing zooms into Eligibility Evaluating, Patient Admitting, Care Planning, Therapeutic Plan Executing, Clinical Evolution Monitoring, Patient Discharging and Post-Discharge Following, in that sequence.

Therapeutic Plan Executing and Clinical Evolution Monitoring execute iteratively: Clinical Evolution Monitoring invokes Therapeutic Plan Executing if Continuity Decision is continue-treatment.

Eligibility Status can be pending, eligible or admitted.
State pending of Eligibility Status is initial.

Eligibility Evaluating occurs if Exclusion Condition is absent, in which case Eligibility Evaluating changes Eligibility Status from pending to eligible, otherwise Eligibility Evaluating is skipped.
Eligibility Evaluating requires Inpatient Facility.
Note [G4]: Condition harmonized with SD8. Exclusion Condition governs skip semantics.

Informed Consent can be unsigned or signed.
State unsigned of Informed Consent is initial.
State signed of Informed Consent is final.
Eligibility Evaluating changes Informed Consent from unsigned to signed.

Caregiver can be available or unavailable.
Eligibility Evaluating requires available Caregiver.
Support Network can be verified or insufficient.
State insufficient of Support Network is initial.
Eligibility Evaluating changes Support Network from insufficient to verified.

Patient Admitting occurs if Eligibility Status is eligible, in which case Patient Admitting changes Eligibility Status from eligible to admitted, otherwise Patient Admitting is skipped.
Patient Admitting requires signed Informed Consent.
Patient Admitting yields Admission Form.
Patient Admitting yields Social Report.
Patient Admitting yields Clinical Record.
Patient Admitting yields active Hospitalization Status.

Derivation Origin can be inpatient-ward, emergency-unit, primary-care, outpatient, urgency-law or centralized-bed-management.
Note [F14]: Derivation Origin has no initial state by design — the state at creation is determined by runtime context (XOR fan: exactly one origin per admission). Declaring any single state as initial would misrepresent the domain.
Patient Admitting yields exactly one of inpatient-ward Derivation Origin, emergency-unit Derivation Origin, primary-care Derivation Origin, outpatient Derivation Origin, urgency-law Derivation Origin or centralized-bed-management Derivation Origin.

Therapeutic Plan can be draft, active or completed.
State draft of Therapeutic Plan is initial.
State active of Therapeutic Plan is default.
State completed of Therapeutic Plan is final.
Care Planning yields active Therapeutic Plan.

Nursing Care Plan can be draft, active or completed.
State draft of Nursing Care Plan is initial.
State active of Nursing Care Plan is default.
State completed of Nursing Care Plan is final.
Care Planning yields active Nursing Care Plan.

Therapeutic Plan Executing requires active Therapeutic Plan.
Therapeutic Plan Executing requires active Nursing Care Plan.
Therapeutic Plan Executing consumes Clinical Supply.
Therapeutic Plan Executing consumes Medication.
Therapeutic Plan Executing requires Medical Equipment.
Therapeutic Plan Executing requires Transport Vehicle.

Clinical Evolution Monitoring yields Domiciliary Clinical Summary.
Note [G2/G6]: Clinical Condition transition (acute-reacutized→recovered) removed from Clinical Evolution Monitoring. Owned exclusively by Medical Discharging in SD1.6 to resolve split-link ambiguity and eliminate double declaration.

Continuity Decision can be continue-treatment or proceed-discharge.
Clinical Evolution Monitoring yields Continuity Decision.

Hospitalization Status can be active or discharged.
State active of Hospitalization Status is initial.
State discharged of Hospitalization Status is final.

Patient Discharging occurs if Continuity Decision is proceed-discharge, in which case Patient Discharging changes Hospitalization Status from active to discharged, otherwise Patient Discharging is skipped.
Patient Discharging changes Therapeutic Plan from active to completed.
Patient Discharging changes Nursing Care Plan from active to completed.
Patient Discharging yields Epicrisis.
Patient Discharging changes Clinical Record from active to finalized.

Post-Discharge Following occurs if Hospitalization Status is discharged.
Post-Discharge Following yields Discharge Outcome.

Healthcare Team handles Eligibility Evaluating.
Healthcare Team handles Patient Admitting.
Healthcare Team handles Care Planning.
Healthcare Team handles Therapeutic Plan Executing.
Healthcare Team handles Clinical Evolution Monitoring.
Healthcare Team handles Patient Discharging.

Clinical Record can be active or finalized.
State active of Clinical Record is initial.
State finalized of Clinical Record is final.

Healthcare Team handles Post-Discharge Following.
```

### OPL-ES del SD1

```
SD se refina por descomposición de *Hospitalizar en Domicilio* en SD1.
*Hospitalizar en Domicilio* se descompone en *Evaluar Elegibilidad*, *Ingresar Paciente*, *Planificar Atención*, *Ejecutar Plan Terapéutico*, *Monitorear Evolución Clínica*, *Egresar de Hospitalización Domiciliaria* y *Seguimiento Post-Egreso*, en esa secuencia.

*Ejecutar Plan Terapéutico* y *Monitorear Evolución Clínica* se ejecutan iterativamente: *Monitorear Evolución Clínica* invoca *Ejecutar Plan Terapéutico* si **Decisión de Continuidad** está en `continuar tratamiento`.

**Estado de Elegibilidad** puede estar `pendiente`, `elegible` o `admitido`.
Estado `pendiente` de **Estado de Elegibilidad** es inicial.

*Evaluar Elegibilidad* ocurre si **Condición de Exclusión** está en `ausente`, en cuyo caso *Evaluar Elegibilidad* cambia **Estado de Elegibilidad** de `pendiente` a `elegible`, de lo contrario *Evaluar Elegibilidad* se omite.
*Evaluar Elegibilidad* requiere **Establecimiento de Atención Cerrada**.
Nota [G4]: Condición armonizada con SD8. **Condición de Exclusión** gobierna semántica de skip.

**Consentimiento Informado** puede estar `sin firmar` o `firmado`.
Estado `sin firmar` de **Consentimiento Informado** es inicial.
Estado `firmado` de **Consentimiento Informado** es final.
*Evaluar Elegibilidad* cambia **Consentimiento Informado** de `sin firmar` a `firmado`.

**Cuidador** puede estar `disponible` o `no disponible`.
*Evaluar Elegibilidad* requiere **Cuidador** en `disponible`.
**Red de Apoyo** puede estar `verificada` o `insuficiente`.
Estado `insuficiente` de **Red de Apoyo** es inicial.
*Evaluar Elegibilidad* cambia **Red de Apoyo** de `insuficiente` a `verificada`.

*Ingresar Paciente* ocurre si **Estado de Elegibilidad** está en `elegible`, en cuyo caso *Ingresar Paciente* cambia **Estado de Elegibilidad** de `elegible` a `admitido`, de lo contrario *Ingresar Paciente* se omite.
*Ingresar Paciente* requiere **Consentimiento Informado** en `firmado`.
*Ingresar Paciente* genera **Formulario de Ingreso**.
*Ingresar Paciente* genera **Ficha Clínica**.
*Ingresar Paciente* genera **Informe Social**.
*Ingresar Paciente* genera **Estado de Hospitalización** en `activa`.

**Origen de Derivación** puede estar `área de hospitalización`, `unidad de emergencia`, `atención primaria`, `ambulatorio`, `ley de urgencia` o `gestión centralizada de camas`.
*Ingresar Paciente* genera exactamente uno de **Origen de Derivación** en `área de hospitalización`, **Origen de Derivación** en `unidad de emergencia`, **Origen de Derivación** en `atención primaria`, **Origen de Derivación** en `ambulatorio`, **Origen de Derivación** en `ley de urgencia` o **Origen de Derivación** en `gestión centralizada de camas`.

**Plan Terapéutico** puede estar `borrador`, `activo` o `completado`.
Estado `borrador` de **Plan Terapéutico** es inicial.
Estado `activo` de **Plan Terapéutico** es por defecto.
Estado `completado` de **Plan Terapéutico** es final.
*Planificar Atención* genera **Plan Terapéutico** en `activo`.

**Plan de Cuidados de Enfermería** puede estar `borrador`, `activo` o `completado`.
Estado `borrador` de **Plan de Cuidados de Enfermería** es inicial.
Estado `activo` de **Plan de Cuidados de Enfermería** es por defecto.
Estado `completado` de **Plan de Cuidados de Enfermería** es final.
*Planificar Atención* genera **Plan de Cuidados de Enfermería** en `activo`.

*Ejecutar Plan Terapéutico* requiere **Plan Terapéutico** en `activo`.
*Ejecutar Plan Terapéutico* requiere **Plan de Cuidados de Enfermería** en `activo`.
*Ejecutar Plan Terapéutico* consume **Insumo Clínico**.
*Ejecutar Plan Terapéutico* consume **Medicamento**.
*Ejecutar Plan Terapéutico* requiere **Equipamiento Médico**.
*Ejecutar Plan Terapéutico* requiere **Vehículo de Transporte**.

*Monitorear Evolución Clínica* genera **Resumen Clínico Domiciliario**.
Nota [G2/G6]: Transición de **Condición Clínica** (agudo-reagudizado→recuperado) removida de *Monitorear Evolución Clínica*. Propiedad exclusiva de *Egresar por Alta Médica* en SD1.6.

**Decisión de Continuidad** puede estar `continuar tratamiento` o `proceder egreso`.
*Monitorear Evolución Clínica* genera **Decisión de Continuidad**.

**Estado de Hospitalización** puede estar `activa` o `egresado`.
Estado `activa` de **Estado de Hospitalización** es inicial.
Estado `egresado` de **Estado de Hospitalización** es final.

*Egresar de Hospitalización Domiciliaria* ocurre si **Decisión de Continuidad** está en `proceder egreso`, en cuyo caso *Egresar de Hospitalización Domiciliaria* cambia **Estado de Hospitalización** de `activa` a `egresado`, de lo contrario *Egresar de Hospitalización Domiciliaria* se omite.
*Egresar de Hospitalización Domiciliaria* cambia **Plan Terapéutico** de `activo` a `completado`.
*Egresar de Hospitalización Domiciliaria* cambia **Plan de Cuidados de Enfermería** de `activo` a `completado`.
*Egresar de Hospitalización Domiciliaria* genera **Epicrisis**.
*Egresar de Hospitalización Domiciliaria* cambia **Ficha Clínica** de `activa` a `finalizada`.

*Seguimiento Post-Egreso* ocurre si **Estado de Hospitalización** está en `egresado`.
*Seguimiento Post-Egreso* genera **Resultado del Egreso**.

**Equipo de Salud** maneja *Evaluar Elegibilidad*.
**Equipo de Salud** maneja *Ingresar Paciente*.
**Equipo de Salud** maneja *Planificar Atención*.
**Equipo de Salud** maneja *Ejecutar Plan Terapéutico*.
**Equipo de Salud** maneja *Monitorear Evolución Clínica*.
**Equipo de Salud** maneja *Egresar de Hospitalización Domiciliaria*.

**Ficha Clínica** puede estar `activa` o `finalizada`.
Estado `activa` de **Ficha Clínica** es inicial.
Estado `finalizada` de **Ficha Clínica** es final.

**Equipo de Salud** maneja *Seguimiento Post-Egreso*.
```

Ref. normativa: DS 1/2022 art. 6 (prestaciones); NT 2024 §3 (proceso asistencial); DS 1/2022 art. 16 (egreso y seguimiento).

---

## SD1.1 — Descomposición de *Eligibility Evaluating*

Refinamiento: in-zooming (secuencial). 6 subprocesos.

### Tabla de Elementos SD1.1

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Candidate Screening* | Informatical | Sistémico | — |
| Proceso | *Application Receiving* | Informatical | Sistémico | — |
| Proceso | *Clinical Condition Evaluating* | Informatical | Sistémico | — |
| Proceso | *Home Condition Evaluating* | Informatical | Sistémico | — |
| Proceso | *Support Network Verifying* | Informatical | Sistémico | — |
| Proceso | *Informed Consent Obtaining* | Informatical | Sistémico | — |
| Objeto | **Candidate** | Físico | Sistémico | `identified`, `postulated` [F3b] |
| Objeto | **Case Manager** | Físico | Sistémico | — |
| Objeto | **Insurance Status** | Informatical | Sistémico | `fonasa-a`, `fonasa-b`, `fonasa-c`, `fonasa-d`, `prais`, `other` |
| Objeto | **Patient Age** | Informatical | Sistémico | `adulto`, `menor-de-edad` |
| Objeto | **Hospital Distance** | Informatical | Sistémico | `dentro-de-cobertura`, `fuera-de-cobertura` |
| Objeto | **Home Condition** | Informatical | Sistémico | `adequate`, `inadequate` |
| Objeto | **Preliminary Social Report** | Informatical | Sistémico | — |
| Objeto | **Clinical Assessment Record** | Informatical | Sistémico | — |
| Objeto | **Rights and Duties Charter** | Informatical | Sistémico | — |

### OPL-EN SD1.1

```
SD1 is refined by in-zooming Eligibility Evaluating in SD1.1.
Eligibility Evaluating zooms into Candidate Screening, Application Receiving, Clinical Condition Evaluating, Home Condition Evaluating, Support Network Verifying and Informed Consent Obtaining, in that sequence.

Candidate Screening is informatical.
Candidate Screening yields Candidate.
Social Worker handles Candidate Screening.

Candidate is physical.
Candidate can be identified or postulated.
State identified of Candidate is initial.

Application Receiving is informatical.
Application Receiving changes Candidate from identified to postulated.
Case Manager handles Application Receiving.

Case Manager is physical.
Case Manager is a Coordination Professional.
Case Manager exhibits Assigned Patients.
Assigned Patients of Case Manager ranges from 0 to 25.

Clinical Condition Evaluating occurs if Clinical Condition is acute-reacutized, otherwise Clinical Condition Evaluating is skipped.
Clinical Condition Evaluating requires Inpatient Facility.
Clinical Assessment Record is informatical.
Clinical Condition Evaluating yields Clinical Assessment Record.
Attending Physician handles Clinical Condition Evaluating.

Home Condition Evaluating yields Preliminary Social Report.
Social Worker handles Home Condition Evaluating.

Home Condition can be adequate or inadequate.
State inadequate of Home Condition is initial.
Patient Home exhibits Home Condition.
Home Condition Evaluating changes Home Condition from inadequate to adequate.

Support Network Verifying changes Support Network from insufficient to verified.
Support Network Verifying requires available Caregiver.
Social Worker handles Support Network Verifying.

Informed Consent Obtaining changes Informed Consent from unsigned to signed.
Informed Consent Obtaining changes Eligibility Status from pending to eligible.
Informed Consent Obtaining requires Patient Group.
Clinical Nurse handles Informed Consent Obtaining.

Rights and Duties Charter is informatical.
Informed Consent Obtaining yields Rights and Duties Charter.

Insurance Status is informatical.
Insurance Status can be fonasa-a, fonasa-b, fonasa-c, fonasa-d, prais or other.
Eligibility Evaluating occurs if Insurance Status is at least one of fonasa-a, fonasa-b, fonasa-c, fonasa-d or prais, otherwise Eligibility Evaluating is skipped.

Patient Age is informatical.
Patient Age can be adulto or menor-de-edad.
Eligibility Evaluating occurs if Patient Age is adulto.

Hospital Distance is informatical.
Hospital Distance can be dentro-de-cobertura or fuera-de-cobertura.
Eligibility Evaluating occurs if Hospital Distance is dentro-de-cobertura.

Exclusion Condition is informatical.
Exclusion Condition can be absent or present.
State absent of Exclusion Condition is initial.
Eligibility Evaluating occurs if Exclusion Condition is absent, otherwise Eligibility Evaluating is skipped.
```

### OPL-ES SD1.1

```
SD1 se refina por descomposición de *Evaluar Elegibilidad* en SD1.1.
*Evaluar Elegibilidad* se descompone en *Pesquisar Candidato*, *Recibir Postulación*, *Evaluar Condición Clínica*, *Evaluar Condición del Domicilio*, *Verificar Red de Apoyo* y *Obtener Consentimiento Informado*, en esa secuencia.

*Pesquisar Candidato* es informático.
*Pesquisar Candidato* genera **Candidato**.
**Trabajador Social** maneja *Pesquisar Candidato*.

**Candidato** es físico.
**Candidato** puede estar `identificado` o `postulado`.
Estado `identificado` de **Candidato** es inicial.

*Recibir Postulación* es informático.
*Recibir Postulación* cambia **Candidato** de `identificado` a `postulado`.
**Gestora Encargada** maneja *Recibir Postulación*.

**Gestora Encargada** es física.
**Gestora Encargada** es un **Profesional Coordinador**.
**Gestora Encargada** exhibe **Pacientes Asignados**.
**Pacientes Asignados** de **Gestora Encargada** varía de 0 a 25.

*Evaluar Condición Clínica* ocurre si **Condición Clínica** está en `agudo-reagudizado`, de lo contrario *Evaluar Condición Clínica* se omite.
*Evaluar Condición Clínica* requiere **Establecimiento de Atención Cerrada**.
**Registro de Evaluación Clínica** es informático.
*Evaluar Condición Clínica* genera **Registro de Evaluación Clínica**.
**Médico de Atención Directa** maneja *Evaluar Condición Clínica*.

*Evaluar Condición del Domicilio* genera **Informe Social Preliminar**.
**Trabajador Social** maneja *Evaluar Condición del Domicilio*.

**Condición del Domicilio** puede estar `adecuada` o `inadecuada`.
Estado `inadecuada` de **Condición del Domicilio** es inicial.
**Domicilio del Paciente** exhibe **Condición del Domicilio**.
*Evaluar Condición del Domicilio* cambia **Condición del Domicilio** de `inadecuada` a `adecuada`.

*Verificar Red de Apoyo* cambia **Red de Apoyo** de `insuficiente` a `verificada`.
*Verificar Red de Apoyo* requiere **Cuidador** en `disponible`.
**Trabajador Social** maneja *Verificar Red de Apoyo*.

*Obtener Consentimiento Informado* cambia **Consentimiento Informado** de `sin firmar` a `firmado`.
*Obtener Consentimiento Informado* cambia **Estado de Elegibilidad** de `pendiente` a `elegible`.
*Obtener Consentimiento Informado* requiere **Grupo de Pacientes**.
**Enfermero Clínico** maneja *Obtener Consentimiento Informado*.

**Carta de Derechos y Deberes** es informática.
*Obtener Consentimiento Informado* genera **Carta de Derechos y Deberes**.

**Estado de Previsión** es informática.
**Estado de Previsión** puede estar `fonasa-a`, `fonasa-b`, `fonasa-c`, `fonasa-d`, `prais` o `otro`.
*Evaluar Elegibilidad* ocurre si **Estado de Previsión** está en al menos uno de `fonasa-a`, `fonasa-b`, `fonasa-c`, `fonasa-d` o `prais`, de lo contrario *Evaluar Elegibilidad* se omite.

**Edad del Paciente** es informática.
**Edad del Paciente** puede estar `adulto` o `menor-de-edad`.
*Evaluar Elegibilidad* ocurre si **Edad del Paciente** está en `adulto`.

**Distancia al Hospital** es informática.
**Distancia al Hospital** puede estar `dentro-de-cobertura` o `fuera-de-cobertura`.
*Evaluar Elegibilidad* ocurre si **Distancia al Hospital** está en `dentro-de-cobertura`.

**Condición de Exclusión** es informática.
**Condición de Exclusión** puede estar `ausente` o `presente`.
Estado `ausente` de **Condición de Exclusión** es inicial.
*Evaluar Elegibilidad* ocurre si **Condición de Exclusión** está en `ausente`, de lo contrario *Evaluar Elegibilidad* se omite.
```

Ref. normativa: DS 1/2022 art. 15 (criterios de ingreso, previsión, edad ≥18, radio ≤20 km); NT 2024 §2 (exclusiones).
Trazabilidad categórica: §5.1 (pesquisa activa), §5.2 (gestión de casos, Google Form), §9.1 (criterios de elegibilidad).

---

## SD1.2 — Descomposición de *Patient Admitting*

Refinamiento: in-zooming (secuencial).

### OPL-EN

```
SD1 is refined by in-zooming Patient Admitting in SD1.2.
Patient Admitting zooms into Admission Registering, Social Diagnosis Elaborating, Patient Documentation Delivering and Referral Facility Coordinating, in that sequence.

Admission Registering yields Admission Form.
Admission Registering requires Communication System.
Admission Registering yields exactly one of inpatient-ward Derivation Origin, emergency-unit Derivation Origin, primary-care Derivation Origin, outpatient Derivation Origin, urgency-law Derivation Origin or centralized-bed-management Derivation Origin.
Administrative Staff handles Admission Registering.

Social Diagnosis Elaborating yields Social Report.
Social Diagnosis Elaborating requires Patient Home.
Social Worker handles Social Diagnosis Elaborating.

Socioeconomic Status is informatical.
Social Diagnosis Elaborating yields Socioeconomic Status.

Patient Documentation Delivering requires Patient Group.
Patient Documentation Delivering requires signed Informed Consent.
Patient Documentation Delivering yields Care Indication Document.
Clinical Nurse handles Patient Documentation Delivering.

Care Indication Document is informatical.

Referral Coordination Record is informatical.
Referral Facility Coordinating requires Inpatient Facility.
Referral Facility Coordinating requires Communication System.
Referral Facility Coordinating yields Referral Coordination Record.
Coordination Professional handles Referral Facility Coordinating.
```

### OPL-ES

```
SD1 se refina por descomposición de *Ingresar Paciente* en SD1.2.
*Ingresar Paciente* se descompone en *Registrar Ingreso*, *Elaborar Diagnóstico Social*, *Entregar Documentación al Paciente* y *Coordinar con Establecimiento Derivador*, en esa secuencia.

*Registrar Ingreso* genera **Formulario de Ingreso**.
*Registrar Ingreso* requiere **Sistema de Comunicación**.
*Registrar Ingreso* genera exactamente uno de **Origen de Derivación** en `área de hospitalización`, **Origen de Derivación** en `unidad de emergencia`, **Origen de Derivación** en `atención primaria`, **Origen de Derivación** en `ambulatorio`, **Origen de Derivación** en `ley de urgencia` o **Origen de Derivación** en `gestión centralizada de camas`.
**Personal Administrativo** maneja *Registrar Ingreso*.

*Elaborar Diagnóstico Social* genera **Informe Social**.
*Elaborar Diagnóstico Social* requiere **Domicilio del Paciente**.
**Trabajador Social** maneja *Elaborar Diagnóstico Social*.

**Situación Socioeconómica** es informática.
*Elaborar Diagnóstico Social* genera **Situación Socioeconómica**.

*Entregar Documentación al Paciente* requiere **Grupo de Pacientes**.
*Entregar Documentación al Paciente* requiere **Consentimiento Informado** en `firmado`.
*Entregar Documentación al Paciente* genera **Documento de Indicaciones de Cuidado**.
**Enfermero Clínico** maneja *Entregar Documentación al Paciente*.

**Documento de Indicaciones de Cuidado** es informático.

**Registro de Coordinación con Derivador** es informático.
*Coordinar con Establecimiento Derivador* requiere **Establecimiento de Atención Cerrada**.
*Coordinar con Establecimiento Derivador* requiere **Sistema de Comunicación**.
*Coordinar con Establecimiento Derivador* genera **Registro de Coordinación con Derivador**.
**Profesional Coordinador** maneja *Coordinar con Establecimiento Derivador*.
```

Nota [A7]: **Preliminary Social Report** (SD1.1, producto de Home Condition Evaluating) es un informe preliminar de habitabilidad. **Social Report** (SD1.2, producto de Social Diagnosis Elaborating) es el informe social completo de ingreso. Son objetos distintos con nombres diferenciados.

Ref. normativa: DS 1/2022 art. 7 (documentación de ingreso); NT 2024 §3.1 (registro de ingreso).

---

## SD1.3 — Descomposición de *Care Planning*

Refinamiento: in-zooming (secuencial). 5 subprocesos (v2.1: +1 Plan Activating para cerrar brecha draft→active; v2.2: elimina requires duplicados para respetar unicidad de rol [H2]).

### OPL-EN

```
SD1 is refined by in-zooming Care Planning in SD1.3.
Care Planning zooms into Therapeutic Plan Elaborating, Nursing Care Plan Elaborating, Home Visit Scheduling, Transport Route Programming and Plan Activating, in that sequence.

Therapeutic Plan Elaborating yields draft Therapeutic Plan.
Therapeutic Plan Elaborating requires Clinical Condition.
Attending Physician handles Therapeutic Plan Elaborating.

Nursing Care Plan Elaborating yields draft Nursing Care Plan.
Nursing Care Plan Elaborating requires draft Therapeutic Plan.
Clinical Nurse handles Nursing Care Plan Elaborating.

Visit Schedule is informatical.
Home Visit Scheduling yields Visit Schedule.
Home Visit Scheduling requires draft Therapeutic Plan.
Coordination Professional handles Home Visit Scheduling.

Transport Route is informatical.
Transport Route Programming yields Transport Route.
Transport Route Programming requires Visit Schedule.
Transport Route Programming requires Patient Home.
Administrative Staff handles Transport Route Programming.

Plan Activating changes Therapeutic Plan from draft to active.
Plan Activating changes Nursing Care Plan from draft to active.
Attending Physician handles Plan Activating.
```

### OPL-ES

```
SD1 se refina por descomposición de *Planificar Atención* en SD1.3.
*Planificar Atención* se descompone en *Elaborar Plan Terapéutico*, *Elaborar Plan de Cuidados de Enfermería*, *Programar Visitas Domiciliarias*, *Programar Rutas de Transporte* y *Activar Planes*, en esa secuencia.

*Elaborar Plan Terapéutico* genera **Plan Terapéutico** en `borrador`.
*Elaborar Plan Terapéutico* requiere **Condición Clínica**.
**Médico de Atención Directa** maneja *Elaborar Plan Terapéutico*.

*Elaborar Plan de Cuidados de Enfermería* genera **Plan de Cuidados de Enfermería** en `borrador`.
*Elaborar Plan de Cuidados de Enfermería* requiere **Plan Terapéutico** en `borrador`.
**Enfermero Clínico** maneja *Elaborar Plan de Cuidados de Enfermería*.

**Programa de Visitas** es informático.
*Programar Visitas Domiciliarias* genera **Programa de Visitas**.
*Programar Visitas Domiciliarias* requiere **Plan Terapéutico** en `borrador`.
**Profesional Coordinador** maneja *Programar Visitas Domiciliarias*.

**Ruta de Transporte** es informática.
*Programar Rutas de Transporte* genera **Ruta de Transporte**.
*Programar Rutas de Transporte* requiere **Programa de Visitas**.
*Programar Rutas de Transporte* requiere **Domicilio del Paciente**.
**Personal Administrativo** maneja *Programar Rutas de Transporte*.

*Activar Planes* cambia **Plan Terapéutico** de `borrador` a `activo`.
*Activar Planes* cambia **Plan de Cuidados de Enfermería** de `borrador` a `activo`.
**Médico de Atención Directa** maneja *Activar Planes*.
```

Ref. normativa: NT 2024 §3.2 (planificación de atención); DS 1/2022 art. 8 (plan terapéutico).

---

## SD1.4 — Descomposición de *Therapeutic Plan Executing*

Refinamiento: in-zooming con paralelismo (10 subprocesos asíncronos). Los subprocesos nuevos (Wound Care, Speech Therapy, Daily Logistics, Shift Handover) provienen del enriquecimiento v2.0. Corregido en v2.1: condition agents sin skip clause; condition instruments con skip para Operational Mode. v2.2: Therapy Type como condition instrument [H13]; Caregiver Knowledge con transición explícita [H12].

### OPL-EN SD1.4

```
SD1 is refined by in-zooming Therapeutic Plan Executing in SD1.4.
Therapeutic Plan Executing zooms into parallel Medical Visit Performing, Nursing Care Executing, Kinesiological Therapy Executing, Medication Administering, Remote Care Regulating, Patient and Caregiver Educating, Wound Care Executing, Speech Therapy Executing, Daily Logistics Managing and Shift Handover Executing.

Medical Visit Performing affects Patient Group.
Medical Visit Performing requires active Therapeutic Plan.
Medical Visit Performing requires Medical Equipment.
Medical Visit Performing requires Transport Vehicle.
Medical Visit Performing occurs if Operational Mode is full-weekday, otherwise Medical Visit Performing is skipped.
Medical Visit Performing yields Domiciliary Clinical Summary.
Attending Physician handles Medical Visit Performing.

Nursing Care Executing affects Patient Group.
Nursing Care Executing requires active Nursing Care Plan.
Nursing Care Executing requires Medical Equipment.
Nursing Care Executing consumes Clinical Supply.
Clinical Nurse handles Nursing Care Executing.
Nursing Technician handles Nursing Care Executing.

Kinesiological Therapy Executing affects Patient Group.
Kinesiological Therapy Executing requires active Therapeutic Plan.
Kinesiological Therapy Executing requires Medical Equipment.
Kinesiologist handles Kinesiological Therapy Executing.
Therapy Type can be motor or respiratory.
Kinesiological Therapy Executing occurs if Therapy Type exists, else Kinesiological Therapy Executing is skipped.

Medication Administering consumes Medication.
Medication Administering affects Patient Group.
Medication Administering requires active Therapeutic Plan.
Clinical Nurse handles Medication Administering.
Nursing Technician handles Medication Administering.
Prescription is informatical.
Medication Administering requires Prescription.

Remote Care Regulating affects Patient Group.
Remote Care Regulating requires Communication System.
Clinical Nurse handles Remote Care Regulating.
Attending Physician handles Remote Care Regulating if Operational Mode is full-weekday.
Remote Care Regulating yields Call Record.
Telehealth Record is informatical.
Remote Care Regulating yields Telehealth Record.

Caregiver Knowledge is informatical.
Caregiver exhibits Caregiver Knowledge.
Caregiver Knowledge can be insufficient or sufficient.
State insufficient of Caregiver Knowledge is initial.
Patient and Caregiver Educating changes Caregiver Knowledge from insufficient to sufficient.
Patient and Caregiver Educating affects Patient Group.
Patient and Caregiver Educating requires active Therapeutic Plan.
Clinical Nurse handles Patient and Caregiver Educating.

Wound Status can be active, healing or resolved.
State active of Wound Status is initial.
State healing of Wound Status is default.
State resolved of Wound Status is final.
Wound Care Executing affects Patient Group.
Wound Care Executing affects Wound Status.
Wound Care Executing requires active Therapeutic Plan.
Wound Care Executing consumes Clinical Supply.
Wound Care Executing yields Wound Care Record.
Clinical Nurse handles Wound Care Executing.
Patient Group exhibits Wound Status.

Swallowing and Speech Status can be impaired, improving or functional.
State impaired of Swallowing and Speech Status is initial.
State improving of Swallowing and Speech Status is default.
State functional of Swallowing and Speech Status is final.
Speech Therapy Executing affects Patient Group.
Speech Therapy Executing affects Swallowing and Speech Status.
Speech Therapy Executing requires active Therapeutic Plan.
Speech Therapy Executing requires Medical Equipment.
Speech Therapy Executing occurs if Operational Mode is full-weekday, otherwise Speech Therapy Executing is skipped.
Speech Therapy Executing yields Speech Therapy Record.
Speech Therapist handles Speech Therapy Executing.
Patient Group exhibits Swallowing and Speech Status.

Daily Schedule Status can be pending, assigned or executed.
State pending of Daily Schedule Status is initial.
State assigned of Daily Schedule Status is default.
State executed of Daily Schedule Status is final.
Daily Logistics Managing affects Daily Schedule Status.
Daily Logistics Managing requires Visit Schedule.
Daily Logistics Managing requires Transport Vehicle.
Daily Logistics Managing yields Daily Schedule.
Coordination Professional handles Daily Logistics Managing.

Shift Status can be pending or handed-over.
State pending of Shift Status is initial.
State handed-over of Shift Status is final.
Shift Handover Executing changes Shift Status from pending to handed-over.
Clinical Nurse handles Shift Handover Executing.
```

### OPL-ES SD1.4

```
SD1 se refina por descomposición de *Ejecutar Plan Terapéutico* en SD1.4.
*Ejecutar Plan Terapéutico* se descompone en paralelo *Realizar Visita Médica*, *Ejecutar Cuidados de Enfermería*, *Ejecutar Terapia Kinesiológica*, *Administrar Medicamentos*, *Regular Atención a Distancia*, *Educar a Paciente y Cuidador*, *Ejecutar Curación*, *Ejecutar Fonoaudiología*, *Gestionar Logística Diaria* y *Ejecutar Entrega de Turno*.

*Realizar Visita Médica* afecta **Grupo de Pacientes**.
*Realizar Visita Médica* requiere **Plan Terapéutico** en `activo`.
*Realizar Visita Médica* requiere **Equipamiento Médico**.
*Realizar Visita Médica* requiere **Vehículo de Transporte**.
*Realizar Visita Médica* ocurre si **Modo Operacional** está en `días-hábiles`, de lo contrario *Realizar Visita Médica* se omite.
*Realizar Visita Médica* genera **Resumen Clínico Domiciliario**.
**Médico de Atención Directa** maneja *Realizar Visita Médica*.

*Ejecutar Cuidados de Enfermería* afecta **Grupo de Pacientes**.
*Ejecutar Cuidados de Enfermería* requiere **Plan de Cuidados de Enfermería** en `activo`.
*Ejecutar Cuidados de Enfermería* requiere **Equipamiento Médico**.
*Ejecutar Cuidados de Enfermería* consume **Insumo Clínico**.
**Enfermero Clínico** maneja *Ejecutar Cuidados de Enfermería*.
**Técnico de Enfermería** maneja *Ejecutar Cuidados de Enfermería*.

*Ejecutar Terapia Kinesiológica* afecta **Grupo de Pacientes**.
*Ejecutar Terapia Kinesiológica* requiere **Plan Terapéutico** en `activo`.
*Ejecutar Terapia Kinesiológica* requiere **Equipamiento Médico**.
**Kinesiólogo** maneja *Ejecutar Terapia Kinesiológica*.
**Tipo de Terapia** puede estar `motora` o `respiratoria`.
*Ejecutar Terapia Kinesiológica* ocurre si **Tipo de Terapia** existe, de lo contrario *Ejecutar Terapia Kinesiológica* se omite.

*Administrar Medicamentos* consume **Medicamento**.
*Administrar Medicamentos* afecta **Grupo de Pacientes**.
*Administrar Medicamentos* requiere **Plan Terapéutico** en `activo`.
**Enfermero Clínico** maneja *Administrar Medicamentos*.
**Técnico de Enfermería** maneja *Administrar Medicamentos*.
**Receta Médica** es informática.
*Administrar Medicamentos* requiere **Receta Médica**.

*Regular Atención a Distancia* afecta **Grupo de Pacientes**.
*Regular Atención a Distancia* requiere **Sistema de Comunicación**.
**Enfermero Clínico** maneja *Regular Atención a Distancia*.
**Médico de Atención Directa** maneja *Regular Atención a Distancia* si **Modo Operacional** está en `días-hábiles`.
*Regular Atención a Distancia* genera **Registro de Llamada**.
**Registro de Telesalud** es informático.
*Regular Atención a Distancia* genera **Registro de Telesalud**.

**Conocimiento del Cuidador** es informático.
**Cuidador** exhibe **Conocimiento del Cuidador**.
**Conocimiento del Cuidador** puede estar `insuficiente` o `suficiente`.
Estado `insuficiente` de **Conocimiento del Cuidador** es inicial.
*Educar a Paciente y Cuidador* cambia **Conocimiento del Cuidador** de `insuficiente` a `suficiente`.
*Educar a Paciente y Cuidador* afecta **Grupo de Pacientes**.
*Educar a Paciente y Cuidador* requiere **Plan Terapéutico** en `activo`.
**Enfermero Clínico** maneja *Educar a Paciente y Cuidador*.

**Estado de Herida** puede estar `activo`, `en cicatrización` o `resuelto`.
Estado `activo` de **Estado de Herida** es inicial.
Estado `en cicatrización` de **Estado de Herida** es por defecto.
Estado `resuelto` de **Estado de Herida** es final.
*Ejecutar Curación* afecta **Grupo de Pacientes**.
*Ejecutar Curación* afecta **Estado de Herida**.
*Ejecutar Curación* requiere **Plan Terapéutico** en `activo`.
*Ejecutar Curación* consume **Insumo Clínico**.
*Ejecutar Curación* genera **Registro de Curación**.
**Enfermero Clínico** maneja *Ejecutar Curación*.
**Grupo de Pacientes** exhibe **Estado de Herida**.

**Estado de Deglución y Habla** puede estar `alterado`, `en mejora` o `funcional`.
Estado `alterado` de **Estado de Deglución y Habla** es inicial.
Estado `en mejora` de **Estado de Deglución y Habla** es por defecto.
Estado `funcional` de **Estado de Deglución y Habla** es final.
*Ejecutar Fonoaudiología* afecta **Grupo de Pacientes**.
*Ejecutar Fonoaudiología* afecta **Estado de Deglución y Habla**.
*Ejecutar Fonoaudiología* requiere **Plan Terapéutico** en `activo`.
*Ejecutar Fonoaudiología* requiere **Equipamiento Médico**.
*Ejecutar Fonoaudiología* ocurre si **Modo Operacional** está en `días-hábiles`, de lo contrario *Ejecutar Fonoaudiología* se omite.
*Ejecutar Fonoaudiología* genera **Registro de Fonoaudiología**.
**Fonoaudiólogo** maneja *Ejecutar Fonoaudiología*.
**Grupo de Pacientes** exhibe **Estado de Deglución y Habla**.

**Estado de Programación Diaria** puede estar `pendiente`, `asignada` o `ejecutada`.
Estado `pendiente` de **Estado de Programación Diaria** es inicial.
Estado `asignada` de **Estado de Programación Diaria** es por defecto.
Estado `ejecutada` de **Estado de Programación Diaria** es final.
*Gestionar Logística Diaria* afecta **Estado de Programación Diaria**.
*Gestionar Logística Diaria* requiere **Programa de Visitas**.
*Gestionar Logística Diaria* requiere **Vehículo de Transporte**.
*Gestionar Logística Diaria* genera **Programación Diaria**.
**Profesional Coordinador** maneja *Gestionar Logística Diaria*.

**Estado de Turno** puede estar `pendiente` o `entregado`.
Estado `pendiente` de **Estado de Turno** es inicial.
Estado `entregado` de **Estado de Turno** es final.
*Ejecutar Entrega de Turno* cambia **Estado de Turno** de `pendiente` a `entregado`.
**Enfermero Clínico** maneja *Ejecutar Entrega de Turno*.
```

Trazabilidad categórica: Wound Care §10.6, §16.4; Speech Therapy §4.4, §16.5; Daily Logistics §16.13; Shift Handover §16.3; Remote Care §5.2, §16.1, §16.12.
Ref. normativa: NT 2024 §3.3 (ejecución del plan); DS 1/2022 art. 9 (visitas domiciliarias); DS 1/2022 art. 10 (atención a distancia).

---

## SD1.4a — Refinamiento de *Daily Logistics Managing*

Refinamiento: in-zooming (5 subprocesos secuenciales).

### OPL-EN SD1.4a

```
SD1.4 is refined by in-zooming Daily Logistics Managing in SD1.4a.
Daily Logistics Managing zooms into Patient Route Assigning, Staff Route Assigning, Visit Sequencing, Unrouted Visit Resolving and Route Execution Monitoring, in that sequence.

Route Assignment can be unassigned, assigned or staffed.
State unassigned of Route Assignment is initial.
State assigned of Route Assignment is default.

Patient Route Assigning changes Route Assignment from unassigned to assigned.
Patient Route Assigning requires Patient Home.
Coordination Professional handles Patient Route Assigning.
Driver handles Patient Route Assigning.

Staff Route Assigning changes Route Assignment from assigned to staffed.
Staff Route Assigning requires Healthcare Team.
Coordination Professional handles Staff Route Assigning.
Driver handles Staff Route Assigning.

Visit Sequencing yields Daily Schedule.
Visit Sequencing affects Route Assignment.
Visit Sequencing changes Daily Schedule Status from pending to assigned.
Coordination Professional handles Visit Sequencing.
Driver handles Visit Sequencing.

Unrouted Visit can be unresolved or resolved.
State unresolved of Unrouted Visit is initial.
Unrouted Visit Resolving occurs if Unrouted Visit exists, in which case Unrouted Visit Resolving changes Unrouted Visit from unresolved to resolved, otherwise Unrouted Visit Resolving is skipped.
Unrouted Visit Resolving affects Daily Schedule.
Coordination Professional handles Unrouted Visit Resolving.

Route Execution Monitoring requires GPS Tracking System.
GPS Tracking System is physical.
GPS Tracking System is a part of Communication System.
Route Execution Monitoring yields Route Execution Report.
Route Execution Monitoring yields Operational Productivity.
Route Execution Monitoring changes Daily Schedule Status from assigned to executed.
Operational Productivity can be below-target, on-target or above-target.
State on-target of Operational Productivity is default.
Coordination Professional handles Route Execution Monitoring.
```

### OPL-ES SD1.4a

```
SD1.4 se refina por descomposición de *Gestionar Logística Diaria* en SD1.4a.
*Gestionar Logística Diaria* se descompone en *Asignar Paciente a Ruta*, *Asignar Profesional a Ruta*, *Secuenciar Visitas*, *Resolver Visita sin Ruta* y *Monitorear Ejecución de Rutas*, en esa secuencia.

**Asignación de Ruta** puede estar `sin asignar`, `asignada` o `con equipo`.
Estado `sin asignar` de **Asignación de Ruta** es inicial.
Estado `asignada` de **Asignación de Ruta** es por defecto.

*Asignar Paciente a Ruta* cambia **Asignación de Ruta** de `sin asignar` a `asignada`.
*Asignar Paciente a Ruta* requiere **Domicilio del Paciente**.
**Profesional Coordinador** maneja *Asignar Paciente a Ruta*.
**Conductor** maneja *Asignar Paciente a Ruta*.

*Asignar Profesional a Ruta* cambia **Asignación de Ruta** de `asignada` a `con equipo`.
*Asignar Profesional a Ruta* requiere **Equipo de Salud**.
**Profesional Coordinador** maneja *Asignar Profesional a Ruta*.
**Conductor** maneja *Asignar Profesional a Ruta*.

*Secuenciar Visitas* genera **Programación Diaria**.
*Secuenciar Visitas* afecta **Asignación de Ruta**.
*Secuenciar Visitas* cambia **Estado de Programación Diaria** de `pendiente` a `asignada`.
**Profesional Coordinador** maneja *Secuenciar Visitas*.
**Conductor** maneja *Secuenciar Visitas*.

**Visita sin Ruta Asignada** puede estar `sin resolver` o `resuelta`.
Estado `sin resolver` de **Visita sin Ruta Asignada** es inicial.
*Resolver Visita sin Ruta* ocurre si **Visita sin Ruta Asignada** existe, en cuyo caso *Resolver Visita sin Ruta* cambia **Visita sin Ruta Asignada** de `sin resolver` a `resuelta`, de lo contrario *Resolver Visita sin Ruta* se omite.
*Resolver Visita sin Ruta* afecta **Programación Diaria**.
**Profesional Coordinador** maneja *Resolver Visita sin Ruta*.


*Monitorear Ejecución de Rutas* requiere **Sistema de Rastreo GPS**.
**Sistema de Rastreo GPS** es físico.
**Sistema de Rastreo GPS** es parte de **Sistema de Comunicación**.
*Monitorear Ejecución de Rutas* genera **Reporte de Ejecución de Rutas**.
*Monitorear Ejecución de Rutas* genera **Productividad Operacional**.
*Monitorear Ejecución de Rutas* cambia **Estado de Programación Diaria** de `asignada` a `ejecutada`.
**Productividad Operacional** puede estar `bajo objetivo`, `en objetivo` o `sobre objetivo`.
Estado `en objetivo` de **Productividad Operacional** es por defecto.
**Profesional Coordinador** maneja *Monitorear Ejecución de Rutas*.
```

Trazabilidad categórica: §16.13 (~20 pacientes activos/jornada, 3 conductores, 4 zonas; GPS 7.587 eventos en 83 días; productividad 39.2%).

---

## SD1.4b — Refinamiento de *Shift Handover Executing*

Refinamiento: in-zooming (3 subprocesos secuenciales). v2.2: Clinical Responsibility Transferring con dual agent (Outgoing + Incoming Clinical Nurse) [H14].

### OPL-EN SD1.4b

```
SD1.4 is refined by in-zooming Shift Handover Executing in SD1.4b.
Shift Handover Executing zooms into Active Patient Status Reporting, Day Movement Registering and Clinical Responsibility Transferring, in that sequence.

Patient Snapshot can be outdated or current.
State outdated of Patient Snapshot is initial.
State current of Patient Snapshot is final.

Active Patient Status Reporting changes Patient Snapshot from outdated to current.
Clinical Nurse handles Active Patient Status Reporting.

Movement Record is informatical.
Day Movement Registering yields Movement Record.
Clinical Nurse handles Day Movement Registering.

Shift Handover Record is informatical.
Clinical Responsibility Transferring changes Shift Status from pending to handed-over.
Clinical Responsibility Transferring yields Shift Handover Record.
Outgoing Clinical Nurse handles Clinical Responsibility Transferring.
Incoming Clinical Nurse handles Clinical Responsibility Transferring.
Note: Outgoing Clinical Nurse and Incoming Clinical Nurse are Clinical Nurse.
```

### OPL-ES SD1.4b

```
SD1.4 se refina por descomposición de *Ejecutar Entrega de Turno* en SD1.4b.
*Ejecutar Entrega de Turno* se descompone en *Reportar Estado Clínico*, *Registrar Movimientos del Día* y *Transferir Responsabilidad Clínica*, en esa secuencia.

**Snapshot de Pacientes** puede estar `desactualizado` o `actual`.
Estado `desactualizado` de **Snapshot de Pacientes** es inicial.
Estado `actual` de **Snapshot de Pacientes** es final.

*Reportar Estado Clínico* cambia **Snapshot de Pacientes** de `desactualizado` a `actual`.
**Enfermero Clínico** maneja *Reportar Estado Clínico*.

**Registro de Movimientos** es informático.
*Registrar Movimientos del Día* genera **Registro de Movimientos**.
**Enfermero Clínico** maneja *Registrar Movimientos del Día*.

**Registro de Entrega de Turno** es informático.
*Transferir Responsabilidad Clínica* cambia **Estado de Turno** de `pendiente` a `entregado`.
*Transferir Responsabilidad Clínica* genera **Registro de Entrega de Turno**.
**Enfermero Clínico Saliente** maneja *Transferir Responsabilidad Clínica*.
**Enfermero Clínico Entrante** maneja *Transferir Responsabilidad Clínica*.
Nota: **Enfermero Clínico Saliente** y **Enfermero Clínico Entrante** son **Enfermero Clínico**.
```

Trazabilidad categórica: §16.3 (snapshot clínico 7 columnas por paciente; dual agent turno saliente + entrante — ambos humanos con agent link válido per §6.5 Metodología).

---

## SD1.5 — Descomposición de *Clinical Evolution Monitoring*

Refinamiento: in-zooming (secuencial con decisión XOR). 12 variables de signos vitales.

### OPL-EN SD1.5

```
SD1 is refined by in-zooming Clinical Evolution Monitoring in SD1.5.
Clinical Evolution Monitoring zooms into Vital Signs Evaluating, Clinical Record Updating, Patient Categorizing and Continuity Deciding, in that sequence.

Vital Signs Evaluating affects Patient Group.
Vital Signs Evaluating requires Medical Equipment.
Clinical Nurse handles Vital Signs Evaluating.

Vital Signs Data is informatical.
Vital Signs Evaluating yields Vital Signs Data.

Blood Pressure is informatical.
Heart Rate is informatical.
Respiratory Rate is informatical.
Oxygen Saturation is informatical.
Body Temperature is informatical.
Blood Glucose Level is informatical.
Pain Scale Score is informatical.
Glasgow Coma Score is informatical.
Edema Status is informatical.
Edema Status can be absent, mild, moderate or severe.
State absent of Edema Status is initial.
Urine Output is informatical.
Bowel Status is informatical.
Invasive Device Status is informatical.
Invasive Device Status can be none, present-normal or present-infected.
State none of Invasive Device Status is initial.

Vital Signs Data consists of Blood Pressure, Heart Rate, Respiratory Rate, Oxygen Saturation, Body Temperature, Blood Glucose Level, Pain Scale Score, Glasgow Coma Score, Edema Status, Urine Output, Bowel Status and Invasive Device Status.

Clinical Record Updating requires Vital Signs Data.
Clinical Record Updating affects Clinical Record.
Clinical Record Updating requires Communication System.
Clinical Nurse handles Clinical Record Updating.

Patient Category is informatical.
Patient Category can be stable, improving or deteriorating.
State stable of Patient Category is initial.
State stable of Patient Category is default.
Patient Categorizing yields Patient Category.
Patient Categorizing requires Vital Signs Data.
Attending Physician handles Patient Categorizing.

Continuity Deciding yields exactly one of continue-treatment Continuity Decision or proceed-discharge Continuity Decision.
Continuity Deciding requires Patient Category.
Continuity Deciding occurs if Operational Mode is full-weekday, otherwise Continuity Deciding is skipped.
Attending Physician handles Continuity Deciding.
```

### OPL-ES SD1.5

```
SD1 se refina por descomposición de *Monitorear Evolución Clínica* en SD1.5.
*Monitorear Evolución Clínica* se descompone en *Evaluar Signos Vitales*, *Actualizar Registro Clínico*, *Categorizar Paciente* y *Decidir Continuidad*, en esa secuencia.

*Evaluar Signos Vitales* afecta **Grupo de Pacientes**.
*Evaluar Signos Vitales* requiere **Equipamiento Médico**.
**Enfermero Clínico** maneja *Evaluar Signos Vitales*.

**Datos de Signos Vitales** es informático.
*Evaluar Signos Vitales* genera **Datos de Signos Vitales**.

**Presión Arterial** es informática.
**Frecuencia Cardíaca** es informática.
**Frecuencia Respiratoria** es informática.
**Saturación de Oxígeno** es informática.
**Temperatura Corporal** es informática.
**Nivel de Glucosa en Sangre** es informático.
**Puntaje de Escala de Dolor** es informático.
**Puntaje de Glasgow** es informático.
**Estado de Edema** es informático.
**Estado de Edema** puede estar `ausente`, `leve`, `moderado` o `severo`.
Estado `ausente` de **Estado de Edema** es inicial.
**Diuresis** es informática.
**Estado Intestinal** es informático.
**Estado de Dispositivo Invasivo** es informático.
**Estado de Dispositivo Invasivo** puede estar `ninguno`, `presente-normal` o `presente-infectado`.
Estado `ninguno` de **Estado de Dispositivo Invasivo** es inicial.

**Datos de Signos Vitales** consta de **Presión Arterial**, **Frecuencia Cardíaca**, **Frecuencia Respiratoria**, **Saturación de Oxígeno**, **Temperatura Corporal**, **Nivel de Glucosa en Sangre**, **Puntaje de Escala de Dolor**, **Puntaje de Glasgow**, **Estado de Edema**, **Diuresis**, **Estado Intestinal** y **Estado de Dispositivo Invasivo**.

*Actualizar Registro Clínico* requiere **Datos de Signos Vitales**.
*Actualizar Registro Clínico* afecta **Ficha Clínica**.
*Actualizar Registro Clínico* requiere **Sistema de Comunicación**.
**Enfermero Clínico** maneja *Actualizar Registro Clínico*.

**Categoría del Paciente** es informática.
**Categoría del Paciente** puede estar `estable`, `mejorando` o `deteriorándose`.
Estado `estable` de **Categoría del Paciente** es inicial.
Estado `estable` de **Categoría del Paciente** es por defecto.
*Categorizar Paciente* genera **Categoría del Paciente**.
*Categorizar Paciente* requiere **Datos de Signos Vitales**.
**Médico de Atención Directa** maneja *Categorizar Paciente*.

*Decidir Continuidad* genera exactamente uno de **Decisión de Continuidad** en `continuar tratamiento` o **Decisión de Continuidad** en `proceder egreso`.
*Decidir Continuidad* requiere **Categoría del Paciente**.
*Decidir Continuidad* ocurre si **Modo Operacional** está en `días-hábiles`, de lo contrario *Decidir Continuidad* se omite.
**Médico de Atención Directa** maneja *Decidir Continuidad*.
```

Trazabilidad categórica: 12 variables §4.3, §10.2 (formulario Registro Visita Equipo HODOM).
Ref. normativa: NT 2024 §3.4 (monitoreo y evolución clínica).

---

## SD1.6 — Despliegue de *Patient Discharging*

Refinamiento: unfolding por generalización-especialización (6 tipos de egreso mutuamente excluyentes). v2.2: Clinical Instability renombrado a Acute Clinical Instability [H16]; Satisfaction Survey asignada a Medical Discharging y Voluntary Withdrawal Discharging [H7].

### OPL-EN

```
Medical Discharging, Hospital Readmission Discharging, Expected Death Discharging, Unexpected Death Discharging, Voluntary Withdrawal Discharging and Disciplinary Discharging are Patient Discharging.

Medical Discharging changes Clinical Condition from acute-reacutized to recovered.
Medical Discharging changes Hospitalization Status from active to discharged.
Medical Discharging occurs if Operational Mode is full-weekday, otherwise Medical Discharging is skipped.
Medical Discharging yields Epicrisis.
Medical Discharging yields Satisfaction Survey.
Attending Physician handles Medical Discharging.

Hospital Readmission Discharging changes Hospitalization Status from active to discharged.
Hospital Readmission Discharging requires Inpatient Facility.
Hospital Readmission Discharging requires Transport Vehicle.
Hospital Readmission Discharging yields Epicrisis.
Attending Physician handles Hospital Readmission Discharging.

Acute Clinical Instability is informatical.
Acute Clinical Instability can be absent or present.
Hospital Readmission Discharging occurs if Acute Clinical Instability is present, in which case Hospital Readmission Discharging changes Acute Clinical Instability from present to absent, otherwise Hospital Readmission Discharging is skipped.

Expected Death Discharging changes Hospitalization Status from active to discharged.
Expected Death Discharging yields Epicrisis.
Attending Physician handles Expected Death Discharging.

Death Protocol is informatical.
Expected Death Discharging yields Death Protocol.

Palliative Intent is informatical.
Palliative Intent can be absent or present.
Expected Death Discharging occurs if Palliative Intent is present, otherwise Expected Death Discharging is skipped.
Expected Death Discharging changes Hospitalization Status from active to discharged.

Unexpected Death Discharging changes Hospitalization Status from active to discharged.
Unexpected Death Discharging yields Epicrisis.
Attending Physician handles Unexpected Death Discharging.
Unexpected Death Discharging yields Death Protocol.

Voluntary Withdrawal Discharging changes Hospitalization Status from active to discharged.
Voluntary Withdrawal Discharging requires signed Informed Consent.
Voluntary Withdrawal Discharging yields Epicrisis.
Voluntary Withdrawal Discharging yields Satisfaction Survey.
Attending Physician handles Voluntary Withdrawal Discharging.

Withdrawal Statement is informatical.
Voluntary Withdrawal Discharging yields Withdrawal Statement.

Disciplinary Discharging changes Hospitalization Status from active to discharged.
Technical Director handles Disciplinary Discharging.
Disciplinary Discharging yields Epicrisis.

Treatment Adherence is informatical.
Treatment Adherence can be adherent or non-adherent.
Disciplinary Discharging occurs if Treatment Adherence is non-adherent, otherwise Disciplinary Discharging is skipped.
Disciplinary Discharging changes Hospitalization Status from active to discharged.
```

### OPL-ES

```
*Egresar por Alta Médica*, *Egresar por Reingreso Hospitalario*, *Egresar por Muerte Esperada*, *Egresar por Muerte Inesperada*, *Egresar por Renuncia Voluntaria* y *Egresar por Alta Disciplinaria* son *Egresar de Hospitalización Domiciliaria*.

*Egresar por Alta Médica* cambia **Condición Clínica** de `agudo-reagudizado` a `recuperado`.
*Egresar por Alta Médica* cambia **Estado de Hospitalización** de `activa` a `egresado`.
*Egresar por Alta Médica* ocurre si **Modo Operacional** está en `días-hábiles`, de lo contrario *Egresar por Alta Médica* se omite.
*Egresar por Alta Médica* genera **Epicrisis**.
*Egresar por Alta Médica* genera **Encuesta de Satisfacción**.
**Médico de Atención Directa** maneja *Egresar por Alta Médica*.

*Egresar por Reingreso Hospitalario* cambia **Estado de Hospitalización** de `activa` a `egresado`.
*Egresar por Reingreso Hospitalario* requiere **Establecimiento de Atención Cerrada**.
*Egresar por Reingreso Hospitalario* requiere **Vehículo de Transporte**.
*Egresar por Reingreso Hospitalario* genera **Epicrisis**.
**Médico de Atención Directa** maneja *Egresar por Reingreso Hospitalario*.

**Inestabilidad Clínica Aguda** es informática.
**Inestabilidad Clínica Aguda** puede estar `ausente` o `presente`.
*Egresar por Reingreso Hospitalario* ocurre si **Inestabilidad Clínica Aguda** está en `presente`, en cuyo caso *Egresar por Reingreso Hospitalario* cambia **Inestabilidad Clínica Aguda** de `presente` a `ausente`, de lo contrario *Egresar por Reingreso Hospitalario* se omite.

*Egresar por Muerte Esperada* cambia **Estado de Hospitalización** de `activa` a `egresado`.
*Egresar por Muerte Esperada* genera **Epicrisis**.
**Médico de Atención Directa** maneja *Egresar por Muerte Esperada*.

**Protocolo de Fallecimiento** es informático.
*Egresar por Muerte Esperada* genera **Protocolo de Fallecimiento**.

**Intención Paliativa** es informática.
**Intención Paliativa** puede estar `ausente` o `presente`.
*Egresar por Muerte Esperada* ocurre si **Intención Paliativa** está en `presente`, de lo contrario *Egresar por Muerte Esperada* se omite.
*Egresar por Muerte Esperada* cambia **Estado de Hospitalización** de `activa` a `egresado`.

*Egresar por Muerte Inesperada* cambia **Estado de Hospitalización** de `activa` a `egresado`.
*Egresar por Muerte Inesperada* genera **Epicrisis**.
**Médico de Atención Directa** maneja *Egresar por Muerte Inesperada*.
*Egresar por Muerte Inesperada* genera **Protocolo de Fallecimiento**.

*Egresar por Renuncia Voluntaria* cambia **Estado de Hospitalización** de `activa` a `egresado`.
*Egresar por Renuncia Voluntaria* requiere **Consentimiento Informado** en `firmado`.
*Egresar por Renuncia Voluntaria* genera **Epicrisis**.
*Egresar por Renuncia Voluntaria* genera **Encuesta de Satisfacción**.
**Médico de Atención Directa** maneja *Egresar por Renuncia Voluntaria*.

**Declaración de Retiro** es informática.
*Egresar por Renuncia Voluntaria* genera **Declaración de Retiro**.

*Egresar por Alta Disciplinaria* cambia **Estado de Hospitalización** de `activa` a `egresado`.
**Director Técnico** maneja *Egresar por Alta Disciplinaria*.
*Egresar por Alta Disciplinaria* genera **Epicrisis**.

**Adherencia al Tratamiento** es informática.
**Adherencia al Tratamiento** puede estar `adherente` o `no adherente`.
*Egresar por Alta Disciplinaria* ocurre si **Adherencia al Tratamiento** está en `no adherente`, de lo contrario *Egresar por Alta Disciplinaria* se omite.
*Egresar por Alta Disciplinaria* cambia **Estado de Hospitalización** de `activa` a `egresado`.
```

Ref. normativa: DS 1/2022 art. 16 (tipos de egreso); NT 2024 §3.5 (egreso); DEIS REM A21 C.1.1 (clasificación de egresos).

---

## SD1.7 — Descomposición de *Post-Discharge Following*

Refinamiento: in-zooming (3 subprocesos secuenciales). v2.2: estados muertos eliminados — Follow-Up Status: sin `completed`; Counterreferral Status: sin `acknowledged` [H5].

### OPL-EN SD1.7

```
SD1 is refined by in-zooming Post-Discharge Following in SD1.7.
Post-Discharge Following occurs if Hospitalization Status is discharged.
Post-Discharge Following zooms into Follow-Up Call Executing, Primary Care Counterreferral Sending and Discharge Outcome Evaluating, in that sequence.

Follow-Up Status can be pending or contacted.
State pending of Follow-Up Status is initial.
State contacted of Follow-Up Status is final.
Follow-Up Call Executing changes Follow-Up Status from pending to contacted.
Follow-Up Call Executing yields Follow-Up Call Record.
Clinical Nurse handles Follow-Up Call Executing.
Attending Physician handles Follow-Up Call Executing if Operational Mode is full-weekday.
Follow-Up Call Executing requires Communication System.

Counterreferral Status can be pending or sent.
State pending of Counterreferral Status is initial.
State sent of Counterreferral Status is final.
Primary Care Counterreferral Sending changes Counterreferral Status from pending to sent.
Primary Care Counterreferral Sending requires Epicrisis.
Primary Care Counterreferral Sending requires Primary Care Center.
Coordination Professional handles Primary Care Counterreferral Sending.
Primary Care Counterreferral Sending requires Communication System.

Discharge Outcome can be favorable or unfavorable.
Discharge Outcome Evaluating yields exactly one of favorable Discharge Outcome or unfavorable Discharge Outcome.
Discharge Outcome Evaluating occurs if Operational Mode is full-weekday, otherwise Discharge Outcome Evaluating is skipped.
Attending Physician handles Discharge Outcome Evaluating.
```

### OPL-ES SD1.7

```
SD1 se refina por descomposición de *Seguimiento Post-Egreso* en SD1.7.
*Seguimiento Post-Egreso* ocurre si **Estado de Hospitalización** está en `egresado`.
*Seguimiento Post-Egreso* se descompone en *Ejecutar Llamada de Seguimiento*, *Enviar Contrarreferencia* y *Evaluar Resultado del Egreso*, en esa secuencia.

**Estado de Seguimiento** puede estar `pendiente` o `contactado`.
Estado `pendiente` de **Estado de Seguimiento** es inicial.
Estado `contactado` de **Estado de Seguimiento** es final.
*Ejecutar Llamada de Seguimiento* cambia **Estado de Seguimiento** de `pendiente` a `contactado`.
*Ejecutar Llamada de Seguimiento* genera **Registro de Llamada de Seguimiento**.
**Enfermero Clínico** maneja *Ejecutar Llamada de Seguimiento*.
**Médico de Atención Directa** maneja *Ejecutar Llamada de Seguimiento* si **Modo Operacional** está en `días-hábiles`.
*Ejecutar Llamada de Seguimiento* requiere **Sistema de Comunicación**.

**Estado de Contrarreferencia** puede estar `pendiente` o `enviado`.
Estado `pendiente` de **Estado de Contrarreferencia** es inicial.
Estado `enviado` de **Estado de Contrarreferencia** es final.
*Enviar Contrarreferencia* cambia **Estado de Contrarreferencia** de `pendiente` a `enviado`.
*Enviar Contrarreferencia* requiere **Epicrisis**.
*Enviar Contrarreferencia* requiere **Centro de Salud Familiar**.
**Profesional Coordinador** maneja *Enviar Contrarreferencia*.
*Enviar Contrarreferencia* requiere **Sistema de Comunicación**.

**Resultado del Egreso** puede estar `favorable` o `desfavorable`.
*Evaluar Resultado del Egreso* genera exactamente uno de **Resultado del Egreso** en `favorable` o **Resultado del Egreso** en `desfavorable`.
*Evaluar Resultado del Egreso* ocurre si **Modo Operacional** está en `días-hábiles`, de lo contrario *Evaluar Resultado del Egreso* se omite.
**Médico de Atención Directa** maneja *Evaluar Resultado del Egreso*.
```

Trazabilidad categórica: §16.12 (7 meses de datos, julio 2024–enero 2025; llamadas a pacientes activos y egresados).
Ref. normativa: DS 1/2022 art. 16 (seguimiento post-egreso); NT 2024 §3.6 (contrarreferencia).

---

## SD2 — Despliegue Estructural del Equipo de Salud

Refinamiento: unfolding por agregación-participación. Versión corregida v2.1: Regulating Physician integrado como parte opcional; Midwife, Psychologist, Occupational Therapist movidos a colección incompleta.

### OPL-EN SD2

```
Healthcare Team consists of Technical Director, Coordination Professional, Case Manager, Attending Physician, Clinical Nurse, Kinesiologist, Nursing Technician, Social Worker, Speech Therapist, Administrative Staff, Driver, an optional Regulating Physician, and at least one other part.

Technical Director is physical.
Coordination Professional is physical.
Case Manager is physical.
Case Manager is a Coordination Professional.
Case Manager exhibits Assigned Patients.
Assigned Patients of Case Manager ranges from 0 to 25.
Attending Physician is physical.
Clinical Nurse is physical.
Kinesiologist is physical.
Nursing Technician is physical.
Social Worker is physical.
Speech Therapist is physical.
Administrative Staff is physical.
Driver is physical.
Regulating Physician is physical.

Technical Director exhibits Clinical Experience.
Clinical Experience of Technical Director ranges from 2 to 40 years.
Technical Director exhibits Postgraduate Management Training.
Technical Director exhibits IAAS Prevention Course.
Technical Director exhibits Weekly Dedication.
Weekly Dedication of Technical Director ranges from 22 to 44 hours.

Coordination Professional exhibits Clinical Experience.
Clinical Experience of Coordination Professional ranges from 5 to 40 years.
Coordination Professional exhibits Management Training.
Coordination Professional exhibits IAAS Course.

Attending Physician exhibits Clinical Experience.
Clinical Experience of Attending Physician ranges from 2 to 40 years.
Attending Physician exhibits IAAS Course.
Attending Physician exhibits BLS Certification.

Clinical Nurse exhibits Clinical Experience.
Clinical Experience of Clinical Nurse ranges from 2 to 40 years.
Clinical Nurse exhibits BLS Certification.

Kinesiologist exhibits Clinical Experience.
Clinical Experience of Kinesiologist ranges from 2 to 40 years.
Kinesiologist exhibits BLS Certification.

Nursing Technician exhibits Clinical Experience.
Clinical Experience of Nursing Technician ranges from 1 to 40 years.
Nursing Technician exhibits BLS Certification.

Speech Therapist exhibits Clinical Experience.
Clinical Experience of Speech Therapist ranges from 2 to 40 years.
Speech Therapist exhibits BLS Certification.

Driver exhibits Work Schedule.
Work Schedule of Driver can be weekday-daytime or rotating-shift.

Regulating Physician exhibits Clinical Experience.
Clinical Experience of Regulating Physician ranges from 2 to 40 years.
Regulating Physician exhibits IAAS Course.
Regulating Physician exhibits BLS Certification.
```

### OPL-ES SD2

```
**Equipo de Salud** consta de **Director Técnico**, **Profesional Coordinador**, **Gestora Encargada**, **Médico de Atención Directa**, **Enfermero Clínico**, **Kinesiólogo**, **Técnico de Enfermería**, **Trabajador Social**, **Fonoaudiólogo**, **Personal Administrativo**, **Conductor**, un opcional **Médico Regulador**, y al menos otra parte.

**Director Técnico** es físico.
**Profesional Coordinador** es físico.
**Gestora Encargada** es física.
**Gestora Encargada** es un **Profesional Coordinador**.
**Gestora Encargada** exhibe **Pacientes Asignados**.
**Pacientes Asignados** de **Gestora Encargada** varía de 0 a 25.
**Médico de Atención Directa** es físico.
**Enfermero Clínico** es físico.
**Kinesiólogo** es físico.
**Técnico de Enfermería** es físico.
**Trabajador Social** es físico.
**Fonoaudiólogo** es físico.
**Personal Administrativo** es físico.
**Conductor** es físico.
**Médico Regulador** es físico.

**Director Técnico** exhibe **Experiencia Clínica**.
**Experiencia Clínica** de **Director Técnico** varía de 2 a 40 años.
**Director Técnico** exhibe **Formación de Postgrado en Gestión**.
**Director Técnico** exhibe **Curso de Prevención de IAAS**.
**Director Técnico** exhibe **Dedicación Semanal**.
**Dedicación Semanal** de **Director Técnico** varía de 22 a 44 horas.

**Profesional Coordinador** exhibe **Experiencia Clínica**.
**Experiencia Clínica** de **Profesional Coordinador** varía de 5 a 40 años.
**Profesional Coordinador** exhibe **Formación en Gestión**.
**Profesional Coordinador** exhibe **Curso IAAS**.

**Médico de Atención Directa** exhibe **Experiencia Clínica**.
**Experiencia Clínica** de **Médico de Atención Directa** varía de 2 a 40 años.
**Médico de Atención Directa** exhibe **Curso IAAS**.
**Médico de Atención Directa** exhibe **Certificación SVB**.

**Enfermero Clínico** exhibe **Experiencia Clínica**.
**Experiencia Clínica** de **Enfermero Clínico** varía de 2 a 40 años.
**Enfermero Clínico** exhibe **Certificación SVB**.

**Kinesiólogo** exhibe **Experiencia Clínica**.
**Experiencia Clínica** de **Kinesiólogo** varía de 2 a 40 años.
**Kinesiólogo** exhibe **Certificación SVB**.

**Técnico de Enfermería** exhibe **Experiencia Clínica**.
**Experiencia Clínica** de **Técnico de Enfermería** varía de 1 a 40 años.
**Técnico de Enfermería** exhibe **Certificación SVB**.

**Fonoaudiólogo** exhibe **Experiencia Clínica**.
**Experiencia Clínica** de **Fonoaudiólogo** varía de 2 a 40 años.
**Fonoaudiólogo** exhibe **Certificación SVB**.

**Conductor** exhibe **Régimen de Jornada**.
**Régimen de Jornada** de **Conductor** puede estar `diurno-lunes-a-viernes` o `turno-rotativo`.

**Médico Regulador** exhibe **Experiencia Clínica**.
**Experiencia Clínica** de **Médico Regulador** varía de 2 a 40 años.
**Médico Regulador** exhibe **Curso IAAS**.
**Médico Regulador** exhibe **Certificación SVB**.
```

Nota [M1]: Las especialidades complementarias (Matrona, Psicólogo, Terapeuta Ocupacional) están cubiertas por "at least one other part" — colección incompleta per ISO §Aggregation-participation. No se nombran individualmente porque no participan como agentes en ningún proceso del modelo actual.

Nota [F7 — Convención de agencia]: En ISO §9.9, el mecanismo de override de links procedurales heredados opera sobre especializaciones (generalization-specialization). En este modelo, los roles profesionales (Attending Physician, Clinical Nurse, Social Worker, etc.) son PARTES del Healthcare Team (aggregation-participation), no especializaciones. La asignación de agent links a partes en lugar de especializaciones es una convención de dominio justificada: el sistema de salud chileno opera por roles profesionales reglamentados (DS 1/2022 art. 11-14), donde cada rol tiene competencias normativas fijas que no constituyen una taxonomía del equipo sino una composición funcional. El Healthcare Team no se "especializa" en Clinical Nurse — se COMPONE de Clinical Nurse. Consecuencia formal: los agent links en subprocesos no son overrides de herencia sino asignaciones directas a partes del agente agregado. Esto es conforme a ISO §Enabling Links (cualquier objeto humano puede ser agent de cualquier proceso) pero no usa el mecanismo de override §9.9.

Nota [F8b — Convención de `affects Patient Group`]: Múltiples procesos en SD1.4 declaran `affects Patient Group` sin especificar transiciones de estado. Justificación: Patient Group es el beneficiario del sistema cuya transformación principal (Clinical Condition: acute-reacutized→recovered) se modela explícitamente en SD1.5 (Clinical Evolution Monitoring). Los `affects` distribuidos en procesos terapéuticos (Medical Visit Performing, Nursing Care Executing, Kinesiological Therapy Executing, etc.) representan el efecto incremental acumulativo de cada intervención clínica sobre el paciente. Modelar transiciones de estado específicas para cada uno requeriría un atributo de progreso clínico granular que excede el scope actual del modelo. La resolución completa se difiere a un posible SD1.4c (in-zooming de procesos terapéuticos individuales).

Nota [B3]: **Cuidador** tiene simultáneamente un tagged structural link (SD9: "Caregiver cares-for Patient Group") y un procedural link (SD1.1: condition instrument). Esta coexistencia es intencional: el tagged structural link expresa la relación permanente cuidador↔paciente; el procedural link expresa la habilitación condicional del proceso de elegibilidad.

Ref. normativa: DS 1/2022 art. 11-14 (dotación, competencias, dedicación horaria); NT 2024 §2 (equipo base y complementario).
Trazabilidad categórica: §5.2 (1.279 visitas/año fonoaudiología HSC); §16.1 (4 conductores: 3 turno rotativo L-D + 1 diurno L-V); §5.2 (HSC sin Médico Regulador dedicado — rol cubierto condicionalmente por Médico de Atención Directa).

---

## SD3 — Despliegue Estructural de Infraestructura Administrativa

*(Sin cambios respecto a v2.0.)*

### OPL-EN

```
Administrative Infrastructure consists of Telephone System, IT System, Electrical Backup System, Clinical Archive Area, Medication Dispensary, Supply Storage, Waste Disposal Area, Cleaning Supply Room, Staff Welfare Area, Vehicle Parking and Evacuation Signage System.

Telephone System is physical.
Telephone System exhibits Availability.
Availability of Telephone System can be 24-7 or partial.
State 24-7 of Availability of Telephone System is initial.

Telephone System exhibits Call Traceability.
Call Traceability is informatical.
Call Traceability can be enabled or disabled.
State enabled of Call Traceability is initial.

IT System is informatical.
IT System exhibits Internet Connectivity.

Electrical Backup System is physical.
Electrical Backup System exhibits SEC Authorization.

Clinical Archive Area is physical.
Clinical Archive Area exhibits Security Level.
Security Level can be secured or unsecured.
State secured of Security Level is initial.

Medication Dispensary is physical.
Medication Dispensary exhibits Cold Chain Compliance.
Cold Chain Compliance can be compliant or non-compliant.
State compliant of Cold Chain Compliance is initial.

Supply Storage is physical.
Supply Storage exhibits Temperature Control.

Waste Disposal Area is physical.
Waste Disposal Area exhibits REAS Compliance.
REAS Compliance can be compliant or non-compliant.

Staff Welfare Area is physical.
Staff Welfare Area consists of Dining Access, Hygiene Facilities, Lockers and Break Room.
```

### OPL-ES

```
**Infraestructura Administrativa** consta de **Sistema Telefónico**, **Sistema Informático**, **Respaldo Eléctrico**, **Área de Archivo Clínico**, **Dispensario de Medicamentos**, **Bodega de Insumos**, **Área de Disposición de Residuos**, **Recinto de Aseo**, **Área de Bienestar del Personal**, **Estacionamiento de Vehículos** y **Sistema de Señalización y Evacuación**.

**Sistema Telefónico** es físico.
**Sistema Telefónico** exhibe **Disponibilidad**.
**Disponibilidad** de **Sistema Telefónico** puede estar `24-7` o `parcial`.
Estado `24-7` de **Disponibilidad** de **Sistema Telefónico** es inicial.

**Sistema Telefónico** exhibe **Trazabilidad de Llamadas**.
**Trazabilidad de Llamadas** es informática.
**Trazabilidad de Llamadas** puede estar `habilitada` o `deshabilitada`.
Estado `habilitada` de **Trazabilidad de Llamadas** es inicial.

**Sistema Informático** es informático.
**Sistema Informático** exhibe **Conectividad Internet**.

**Respaldo Eléctrico** es físico.
**Respaldo Eléctrico** exhibe **Autorización SEC**.

**Área de Archivo Clínico** es físico.
**Área de Archivo Clínico** exhibe **Nivel de Seguridad**.
**Nivel de Seguridad** puede estar `seguro` o `no seguro`.
Estado `seguro` de **Nivel de Seguridad** es inicial.

**Dispensario de Medicamentos** es físico.
**Dispensario de Medicamentos** exhibe **Cumplimiento de Cadena de Frío**.
**Cumplimiento de Cadena de Frío** puede estar `cumple` o `no cumple`.
Estado `cumple` de **Cumplimiento de Cadena de Frío** es inicial.

**Bodega de Insumos** es físico.
**Bodega de Insumos** exhibe **Control de Temperatura**.

**Área de Disposición de Residuos** es físico.
**Área de Disposición de Residuos** exhibe **Cumplimiento REAS**.
**Cumplimiento REAS** puede estar `cumple` o `no cumple`.

**Área de Bienestar del Personal** es físico.
**Área de Bienestar del Personal** consta de **Acceso a Alimentación**, **Servicios Higiénicos**, **Casilleros** y **Sala de Estar**.
```

Ref. normativa: DS 1/2022 art. 17-22 (infraestructura, equipamiento, farmacia); NT 2024 §4 (condiciones físicas).

---

## SD4 — Despliegue Estructural de Equipamiento Médico

*(Sin cambios respecto a v2.0.)*

### OPL-EN

```
Medical Equipment consists of Blood Pressure Monitor, Pulse Oximeter, Cardiac Monitor, Thermometer, Defibrillator and Specialty Instrument Set.

Blood Pressure Monitor is physical.
Pulse Oximeter is physical.
Cardiac Monitor is physical.
Thermometer is physical.
Defibrillator is physical.
Specialty Instrument Set is physical.

Medical Equipment exhibits Maintenance Status.
Maintenance Status can be current or overdue.
State current of Maintenance Status is initial.

Medical Equipment exhibits Sanitary Authorization.
Sanitary Authorization can be authorized or unauthorized.
State authorized of Sanitary Authorization is initial.
```

### OPL-ES

```
**Equipamiento Médico** consta de **Monitor de Presión Arterial**, **Oxímetro de Pulso**, **Monitor Cardíaco**, **Termómetro**, **Desfibrilador** y **Conjunto de Instrumentos Especializados**.

**Monitor de Presión Arterial** es físico.
**Oxímetro de Pulso** es físico.
**Monitor Cardíaco** es físico.
**Termómetro** es físico.
**Desfibrilador** es físico.
**Conjunto de Instrumentos Especializados** es físico.

**Equipamiento Médico** exhibe **Estado de Mantención**.
**Estado de Mantención** puede estar `vigente` o `vencido`.
Estado `vigente` de **Estado de Mantención** es inicial.

**Equipamiento Médico** exhibe **Autorización Sanitaria**.
**Autorización Sanitaria** puede estar `autorizado` o `no autorizado`.
Estado `autorizado` de **Autorización Sanitaria** es inicial.
```

Ref. normativa: DS 1/2022 art. 19 (equipamiento médico, mantención preventiva).

---

## SD5 — Despliegue Estructural del Sistema de Documentación

*(Sin cambios respecto a v2.0.)*

### OPL-EN

```
Domiciliary Hospitalization System exhibits Documentation System as well as Domiciliary Hospitalizing.

Documentation System is informatical.
Documentation System consists of Internal Organization Manual, Clinical Protocol Set, Procedures Manual, Waste Management Protocol and Annual Training Plan.

Internal Organization Manual is informatical.
Internal Organization Manual consists of Organizational Chart, Role Definition Set, Schedule Definition and Hygiene Regulation.

Clinical Protocol Set is informatical.
Clinical Protocol Set consists of Admission Evaluation Protocol, Visit and Route Scheduling Protocol, Categorization and Discharge Protocol, Prescription and Referral Management Protocol, Emergency Response Protocol and Staff Aggression Protocol.

Procedures Manual is informatical.
Procedures Manual consists of Peripheral Venous Line Procedure, Central Venous Line Procedure, Urinary Catheter Procedure, Tracheostomy Procedure, Sample Collection Procedure and Isolation Precaution Procedure.

Waste Management Protocol is informatical.
Waste Management Protocol exhibits REAS Decree Compliance.

Annual Training Plan is informatical.
Annual Training Plan consists of IAAS Training, BLS Training, Staff Induction Program and Humanized Care Training.

Staff Induction Program is informatical.
Staff Induction Program exhibits Minimum Duration.
Minimum Duration of Staff Induction Program ranges from 44 to 200 hours.
```

### OPL-ES

```
**Sistema de Hospitalización Domiciliaria** exhibe **Sistema Documental** así como *Hospitalizar en Domicilio*.

**Sistema Documental** es informático.

**Sistema Documental** consta de **Manual de Organización Interna**, **Conjunto de Protocolos Clínicos**, **Manual de Procedimientos**, **Protocolo de Manejo de Residuos** y **Plan Anual de Capacitación**.

**Manual de Organización Interna** es informático.
**Manual de Organización Interna** consta de **Organigrama**, **Conjunto de Definiciones de Rol**, **Definición de Horarios** y **Reglamento de Higiene**.

**Conjunto de Protocolos Clínicos** es informático.
**Conjunto de Protocolos Clínicos** consta de **Protocolo de Evaluación e Ingreso**, **Protocolo de Programación de Visitas y Rutas**, **Protocolo de Categorización y Egreso**, **Protocolo de Gestión de Recetas e Interconsultas**, **Protocolo de Actuación ante Emergencias** y **Protocolo ante Agresiones al Personal**.

**Manual de Procedimientos** es informático.
**Manual de Procedimientos** consta de **Procedimiento de Vía Venosa Periférica**, **Procedimiento de Vía Venosa Central**, **Procedimiento de Catéter Urinario**, **Procedimiento de Traqueostomía**, **Procedimiento de Toma de Muestras** y **Procedimiento de Precauciones de Aislamiento**.

**Protocolo de Manejo de Residuos** es informático.
**Protocolo de Manejo de Residuos** exhibe **Cumplimiento Decreto REAS**.

**Plan Anual de Capacitación** es informático.
**Plan Anual de Capacitación** consta de **Capacitación IAAS**, **Capacitación SVB**, **Programa de Inducción** y **Capacitación en Humanización del Cuidado**.

**Programa de Inducción** es informático.
**Programa de Inducción** exhibe **Duración Mínima**.
**Duración Mínima** de **Programa de Inducción** varía de 44 a 200 horas.
```

Ref. normativa: DS 1/2022 art. 23-28 (protocolos obligatorios, manual de organización, plan de capacitación).

---

## SD6 — Procesos de Gobernanza del Sistema

*(Sin cambios sustantivos respecto a v2.0. Flaggeado en validación como >25 entidades.)*

### OPL-EN

```
Domiciliary Hospitalization System exhibits Sanitary Authorization Managing as well as Quality and Safety Managing as well as Staff Training Managing as well as Supply Chain Managing as well as Waste Managing as well as Equipment Maintenance Managing as well as Capacity Managing.

Sanitary Authorization Managing affects Domiciliary Hospitalization System.
Sanitary Authorization Managing requires Current Regulation.
Technical Director handles Sanitary Authorization Managing.

Sanitary Authorization Status is informatical.
Domiciliary Hospitalization System exhibits Sanitary Authorization Status.
Sanitary Authorization Status can be pending, authorized or expired.
State pending of Sanitary Authorization Status is initial.
Sanitary Authorization Managing changes Sanitary Authorization Status from pending to authorized.

Authorization Validity is informatical.
Sanitary Authorization Status exhibits Authorization Validity.
Authorization Validity of Sanitary Authorization Status ranges from 0 to 3 years.

SEREMI is physical.
SEREMI is environmental.
SEREMI supervises Domiciliary Hospitalization System.
Sanitary Authorization Managing requires SEREMI.

Quality and Safety Managing affects Domiciliary Hospitalization System.
Quality and Safety Managing requires Documentation System.
Coordination Professional handles Quality and Safety Managing.

Quality Level is informatical.
Domiciliary Hospitalization System exhibits Quality Level.
Quality and Safety Managing affects Quality Level.

Adverse Reaction Audit is informatical.
Quality and Safety Managing yields Adverse Reaction Audit.
Mortality Audit is informatical.
Quality and Safety Managing yields Mortality Audit.

Staff Training Managing affects Healthcare Team.
Staff Training Managing requires Annual Training Plan.
Coordination Professional handles Staff Training Managing.

Training Compliance is informatical.
Healthcare Team exhibits Training Compliance.
Training Compliance can be compliant or non-compliant.
Staff Training Managing changes Training Compliance from non-compliant to compliant.

Supply Chain Managing affects Clinical Supply.
Supply Chain Managing affects Medication.
Supply Chain Managing requires Medication Dispensary.
Coordination Professional handles Supply Chain Managing.

Waste Managing consumes Biomedical Waste.
Waste Managing requires Waste Disposal Area.
Waste Managing requires Waste Management Protocol.
Coordination Professional handles Waste Managing.

Biomedical Waste is physical.

Sharps Disposal Protocol is informatical.
Waste Managing requires Sharps Disposal Protocol.

Equipment Maintenance Managing affects Medical Equipment.
Equipment Maintenance Managing changes Maintenance Status from overdue to current.
Technical Director handles Equipment Maintenance Managing.

Preventive Maintenance Program is informatical.
Equipment Maintenance Managing requires Preventive Maintenance Program.

Capacity Managing affects Domiciliary Hospitalization System.
Coordination Professional handles Capacity Managing.

Installed Capacity is informatical.
Domiciliary Hospitalization System exhibits Installed Capacity.

Programmed Slots is informatical.
Installed Capacity exhibits Programmed Slots.

Utilized Slots is informatical.
Installed Capacity exhibits Utilized Slots.

Available Slots is informatical.
Installed Capacity exhibits Available Slots.

Winter Campaign Slots is informatical.
Installed Capacity exhibits Winter Campaign Slots.

Mental Health Slots is informatical.
Installed Capacity exhibits Mental Health Slots.

Adult Slots is informatical.
Installed Capacity exhibits Adult Slots.

Pediatric Slots is informatical.
Installed Capacity exhibits Pediatric Slots.

Capacity Managing affects Installed Capacity.
```

### OPL-ES

```
**Sistema de Hospitalización Domiciliaria** exhibe *Gestionar Autorización Sanitaria* así como *Gestionar Calidad y Seguridad* así como *Gestionar Capacitación del Personal* así como *Gestionar Cadena de Abastecimiento* así como *Gestionar Residuos* así como *Gestionar Mantención de Equipos* así como *Gestionar Capacidad*.

*Gestionar Autorización Sanitaria* afecta **Sistema de Hospitalización Domiciliaria**.
*Gestionar Autorización Sanitaria* requiere **Normativa Vigente**.
**Director Técnico** maneja *Gestionar Autorización Sanitaria*.

**Estado de Autorización Sanitaria** es informático.
**Sistema de Hospitalización Domiciliaria** exhibe **Estado de Autorización Sanitaria**.
**Estado de Autorización Sanitaria** puede estar `pendiente`, `autorizado` o `vencido`.
Estado `pendiente` de **Estado de Autorización Sanitaria** es inicial.
*Gestionar Autorización Sanitaria* cambia **Estado de Autorización Sanitaria** de `pendiente` a `autorizado`.

**Vigencia de Autorización** es informática.
**Estado de Autorización Sanitaria** exhibe **Vigencia de Autorización**.
**Vigencia de Autorización** de **Estado de Autorización Sanitaria** varía de 0 a 3 años.

**SEREMI** es físico.
**SEREMI** es ambiental.
**SEREMI** supervisa **Sistema de Hospitalización Domiciliaria**.
*Gestionar Autorización Sanitaria* requiere **SEREMI**.

*Gestionar Calidad y Seguridad* afecta **Sistema de Hospitalización Domiciliaria**.
*Gestionar Calidad y Seguridad* requiere **Sistema Documental**.
**Profesional Coordinador** maneja *Gestionar Calidad y Seguridad*.

**Nivel de Calidad** es informático.
**Sistema de Hospitalización Domiciliaria** exhibe **Nivel de Calidad**.
*Gestionar Calidad y Seguridad* afecta **Nivel de Calidad**.

**Auditoría de Reacciones Adversas** es informática.
*Gestionar Calidad y Seguridad* genera **Auditoría de Reacciones Adversas**.
**Auditoría de Mortalidad** es informática.
*Gestionar Calidad y Seguridad* genera **Auditoría de Mortalidad**.

*Gestionar Capacitación del Personal* afecta **Equipo de Salud**.
*Gestionar Capacitación del Personal* requiere **Plan Anual de Capacitación**.
**Profesional Coordinador** maneja *Gestionar Capacitación del Personal*.

**Cumplimiento de Capacitación** es informático.
**Equipo de Salud** exhibe **Cumplimiento de Capacitación**.
**Cumplimiento de Capacitación** puede estar `cumple` o `no cumple`.
*Gestionar Capacitación del Personal* cambia **Cumplimiento de Capacitación** de `no cumple` a `cumple`.

*Gestionar Cadena de Abastecimiento* afecta **Insumo Clínico**.
*Gestionar Cadena de Abastecimiento* afecta **Medicamento**.
*Gestionar Cadena de Abastecimiento* requiere **Dispensario de Medicamentos**.
**Profesional Coordinador** maneja *Gestionar Cadena de Abastecimiento*.

*Gestionar Residuos* consume **Residuo Biomédico**.
*Gestionar Residuos* requiere **Área de Disposición de Residuos**.
*Gestionar Residuos* requiere **Protocolo de Manejo de Residuos**.
**Profesional Coordinador** maneja *Gestionar Residuos*.

**Residuo Biomédico** es físico.

**Protocolo de Desecho de Cortopunzantes** es informático.
*Gestionar Residuos* requiere **Protocolo de Desecho de Cortopunzantes**.

*Gestionar Mantención de Equipos* afecta **Equipamiento Médico**.
*Gestionar Mantención de Equipos* cambia **Estado de Mantención** de `vencido` a `vigente`.
**Director Técnico** maneja *Gestionar Mantención de Equipos*.

**Programa de Mantención Preventiva** es informático.
*Gestionar Mantención de Equipos* requiere **Programa de Mantención Preventiva**.

*Gestionar Capacidad* afecta **Sistema de Hospitalización Domiciliaria**.
**Profesional Coordinador** maneja *Gestionar Capacidad*.

**Capacidad Instalada** es informática.
**Sistema de Hospitalización Domiciliaria** exhibe **Capacidad Instalada**.

**Cupos Programados** es informático.
**Capacidad Instalada** exhibe **Cupos Programados**.

**Cupos Utilizados** es informático.
**Capacidad Instalada** exhibe **Cupos Utilizados**.

**Cupos Disponibles** es informático.
**Capacidad Instalada** exhibe **Cupos Disponibles**.

**Cupos Campaña de Invierno** es informático.
**Capacidad Instalada** exhibe **Cupos Campaña de Invierno**.

**Cupos Salud Mental** es informático.
**Capacidad Instalada** exhibe **Cupos Salud Mental**.

**Cupos Adulto** es informático.
**Capacidad Instalada** exhibe **Cupos Adulto**.

**Cupos Pediátrico** es informático.
**Capacidad Instalada** exhibe **Cupos Pediátrico**.

*Gestionar Capacidad* afecta **Capacidad Instalada**.
```

Ref. normativa: DS 1/2022 art. 29-35 (autorización sanitaria, SEREMI, calidad, residuos); NT 2024 §5 (gobernanza y gestión).

---

## SD7 — Despliegue del Domicilio del Paciente (Condiciones de Elegibilidad)

*(Sin cambios respecto a v2.0.)*

### OPL-EN

```
Patient Home exhibits Home Condition as well as Basic Services as well as Telephony Access as well as Road Access.

Home Condition can be adequate or inadequate.
State inadequate of Home Condition is initial.
State adequate of Home Condition is final.

Basic Services is informatical.
Basic Services can be available or unavailable.

Telephony Access is informatical.
Telephony Access can be available or unavailable.

Road Access is informatical.
Road Access can be within-coverage-radius or outside-coverage-radius.
```

### OPL-ES

```
**Domicilio del Paciente** exhibe **Condición del Domicilio** así como **Servicios Básicos** así como **Acceso a Telefonía** así como **Acceso Vial**.

**Condición del Domicilio** puede estar `adecuada` o `inadecuada`.
Estado `inadecuada` de **Condición del Domicilio** es inicial.
Estado `adecuada` de **Condición del Domicilio** es final.

**Servicios Básicos** es informático.
**Servicios Básicos** puede estar `disponible` o `no disponible`.

**Acceso a Telefonía** es informático.
**Acceso a Telefonía** puede estar `disponible` o `no disponible`.

**Acceso Vial** es informático.
**Acceso Vial** puede estar `dentro del radio de cobertura` o `fuera del radio de cobertura`.
```

Ref. normativa: DS 1/2022 art. 15 (condiciones del domicilio, servicios básicos, acceso vehicular).

---

## SD8 — Exclusiones del Sistema (Condiciones que Impiden Ingreso)

*(Sin cambios respecto a v2.0.)*

### OPL-EN

```
Exclusion Condition is informatical.
Exclusion Condition can be absent or present.
State absent of Exclusion Condition is initial.

Clinical Instability Exclusion, Unestablished Diagnosis Exclusion, Decompensated Mental Health Exclusion, Unlisted Service Exclusion and Prior Disciplinary Discharge Exclusion are Exclusion Condition.

Eligibility Evaluating occurs if Exclusion Condition is absent, in which case Eligibility Evaluating changes Eligibility Status from pending to eligible, otherwise Eligibility Evaluating is skipped.
```

### OPL-ES

```
**Condición de Exclusión** es informática.
**Condición de Exclusión** puede estar `ausente` o `presente`.
Estado `ausente` de **Condición de Exclusión** es inicial.

**Exclusión por Inestabilidad Clínica**, **Exclusión por Diagnóstico no Establecido**, **Exclusión por Salud Mental Descompensada**, **Exclusión por Prestación no Listada** y **Exclusión por Alta Disciplinaria Previa** son **Condición de Exclusión**.

*Evaluar Elegibilidad* ocurre si **Condición de Exclusión** está en `ausente`, en cuyo caso *Evaluar Elegibilidad* cambia **Estado de Elegibilidad** de `pendiente` a `elegible`, de lo contrario *Evaluar Elegibilidad* se omite.
```

Ref. normativa: DS 1/2022 art. 15 (exclusiones); NT 2024 §2.2 (criterios de exclusión).

---

## SD9 — Relaciones Estructurales Etiquetadas (Tagged Structural Links)

Versión corregida v2.1: todos los links son objeto↔objeto (homogéneos). Regulating Physician integrado. v2.2: Primary Care Center bidireccional con tags semánticos (refers/counterrefers) [H15].

### OPL-EN

```
Inpatient Facility refers Patient Group.
Patient Home hosts Patient Group.
SEREMI supervises Domiciliary Hospitalization System.
Current Regulation governs Domiciliary Hospitalization System.
Technical Director represents Domiciliary Hospitalization System.
Domiciliary Hospitalization System guarantees Continuity of Care.
Continuity of Care is informatical.
Attending Physician coordinates Inpatient Facility.
Regulating Physician supports Attending Physician.
Caregiver cares-for Patient Group.
Primary Care Center refers Patient Group.
Domiciliary Hospitalization System refers Primary Care Center.
Primary Care Center counterrefers Domiciliary Hospitalization System.
```

### OPL-ES

```
**Establecimiento de Atención Cerrada** deriva **Grupo de Pacientes**.
**Domicilio del Paciente** alberga **Grupo de Pacientes**.
**SEREMI** supervisa **Sistema de Hospitalización Domiciliaria**.
**Normativa Vigente** rige **Sistema de Hospitalización Domiciliaria**.
**Director Técnico** representa **Sistema de Hospitalización Domiciliaria**.
**Sistema de Hospitalización Domiciliaria** garantiza **Continuidad de la Atención**.
**Continuidad de la Atención** es informática.
**Médico de Atención Directa** coordina con **Establecimiento de Atención Cerrada**.
**Médico Regulador** apoya a **Médico de Atención Directa**.
**Cuidador** cuida a **Grupo de Pacientes**.
**Centro de Salud Familiar** deriva **Grupo de Pacientes**.
**Sistema de Hospitalización Domiciliaria** deriva a **Centro de Salud Familiar**.
**Centro de Salud Familiar** contrarefiere a **Sistema de Hospitalización Domiciliaria**.
```

Nota [A6]: **Regulating Physician** está ahora declarado en SD2 como parte opcional del Healthcare Team y conectado en SD9 vía tagged structural link (supports) al Attending Physician. En el modelo HSC actual, este rol es cubierto condicionalmente por el Attending Physician (§5.2 modelo categórico).

Nota [B3]: La coexistencia de tagged structural link (**Caregiver** cares-for **Patient Group**) con el procedural link de SD1.1 (condition instrument de Eligibility Evaluating) es intencional y conforme a ISO — los links estructurales y procedurales operan en capas semánticas distintas (time-invariant vs time-dependent).

Ref. normativa: DS 1/2022 art. 5 (relación con establecimiento derivador); DS 1/2022 art. 16 (continuidad de la atención).

---

## SD10 — Modo Operacional del Sistema

Versión corregida v2.1: esencia de Weekly Schedule Cycling corregida a Informatical. v2.2: elimina exhibition de Weekly Schedule Cycling [H3].

### Tabla de Elementos SD10

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Weekly Schedule Cycling* | Informatical | Ambiental | — |
| Objeto | **Operational Mode** | Informatical | Sistémico | `full-weekday`, `reduced-weekend` |

### OPL-EN SD10

```
SD is extended by SD10 for Operational Mode modeling.
Domiciliary Hospitalization System exhibits Operational Mode.
Operational Mode can be full-weekday or reduced-weekend.
State full-weekday of Operational Mode is initial.

Weekly Schedule Cycling is informatical.
Weekly Schedule Cycling is environmental.
Weekly Schedule Cycling affects Operational Mode.
```

Note [F1c]: Per §4.4 (procedural link uniqueness), the dual changes (full-weekday→reduced-weekend and reduced-weekend→full-weekday) constituted two distinct procedural links between the same object-process pair. Replaced by single `affects` link. Specific state transitions are implicit in the cyclic nature of the environmental process and SHOULD be detailed in a future in-zooming of Weekly Schedule Cycling if needed.

### OPL-ES SD10

```
SD se extiende por SD10 para el modelamiento del Modo Operacional.
**Sistema de Hospitalización Domiciliaria** exhibe **Modo Operacional**.
**Modo Operacional** puede estar `días-hábiles` o `fin-de-semana`.
Estado `días-hábiles` de **Modo Operacional** es inicial.

*Ciclar Programación Semanal* es informático.
*Ciclar Programación Semanal* es ambiental.
*Ciclar Programación Semanal* afecta **Modo Operacional**.
```

**Procesos con condition instrument (skip si `reduced-weekend`) [M2]:**
- Medical Visit Performing, Speech Therapy Executing, Continuity Deciding, Medical Discharging, Discharge Outcome Evaluating.

**Procesos con condition agent (médico condicional, enfermera incondicional) [A3]:**
- Remote Care Regulating, Follow-Up Call Executing.

**Procesos ejecutables en ambos modos (sin condición):**
- Nursing Care Executing, Kinesiological Therapy Executing, Medication Administering, Patient and Caregiver Educating, Vital Signs Evaluating, Clinical Record Updating, Daily Logistics Managing, Shift Handover Executing, Wound Care Executing.

Trazabilidad categórica: §6.2 (cuarto turno L-D, diurnos L-V); §16.5 (SUV solo L-V — reduce capacidad vehicular a 2/3 fin de semana).
Ref. normativa: NT 2024 §2.1 (dotación por turno y jornada).

---

## Validación del Modelo v2.4

### Checklist SD

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Sistema clasificado | Socio-técnico determinado | PASS | CRÍTICA |
| Purpose definido | Patient Group + Clinical Condition + acute-reacutized → recovered | PASS | CRÍTICA |
| Función definida | Domiciliary Hospitalizing + Patient Group (transformee) | PASS | CRÍTICA |
| Enablers presentes | 1 agente (Healthcare Team) + 6 instrumentos (equip., comunicación, transporte, admin., postulación digital, domicilio) | PASS | ALTA |
| Environment identificado | 4 objetos ambientales (Patient Home como instrument, Inpatient Facility, Current Regulation, Primary Care Center) | PASS | MEDIA |
| Problem occurrence | Acute Episode Occurring (proceso ambiental) → estado acute-reacutized [H4: esencia Physical] | PASS | MEDIA |
| Tagged structural homogéneos | Todos obj↔obj. Ningún link obj↔proceso [C1 corregido] | PASS | ALTA |
| OPL legible | Sentencias OPL correctas en EN y ES | PASS | ALTA |
| Naming compliant | Gerundio EN / Infinitivo o -ción ES + singular + Group [A2 corregido] | PASS | ALTA |
| Exhibition | Sistema exhibe proceso principal + Modo Operacional | PASS | ALTA |
| Agents = humanos | Healthcare Team es grupo humano; instrumentos son no-humanos | PASS | ALTA |
| Acute Episode Occurring esencia | Physical (no Informatical) [H4] | PASS | ALTA |
| Primary Care Center bidireccional | Tagged structural con tags refers/counterrefers [H15] | PASS | ALTA |

### Checklist SD1

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Subprocesos transforman | Cada subproceso ≥1 transformee | PASS | CRÍTICA |
| Refinamiento correcto | Secuencial → in-zooming (7 subprocesos) | PASS | ALTA |
| Links distribuidos | Consumption/result NO en outer contour | PASS | CRÍTICA |
| Transición draft→active | Plan Activating cierra brecha [C2 corregido]; sin requires duplicados [H2] | PASS | CRÍTICA |
| Unicidad de rol Care Planning | Care Planning yields (sin changes) — transición en SD1.3 [H1] | PASS | CRÍTICA |
| Post-Discharge Following atómico en SD1 | Hechos de SD1.7 NO aparecen en SD1 [A1 corregido] | PASS | ALTA |
| Eligibility Status sin dead states | 3 estados: pending, eligible, admitted [H6, F3a] | PASS | ALTA |
| Patient Admitting output explícito | Transición eligible→admitted [H6] | PASS | ALTA |
| Satisfaction Survey herencia | No yield en Patient Discharging; yield en Medical Discharging y Voluntary Withdrawal Discharging [H7] | PASS | ALTA |
| Support Network esencia | Informatical (no Físico) [H8] | PASS | ALTA |
| Caregiver afiliación | Ambiental (no Sistémico) [H11] | PASS | MEDIA |
| Eligibility Evaluating condicional | Armonizado con SD8: condition input-output-specified effect con skip [G4] | PASS | ALTA |
| Clinical Condition transición única | Propiedad exclusiva de Medical Discharge en SD1.6 [G2/G6] | PASS | CRÍTICA |
| Nursing Care Plan default/final | active=default, completed=final [G9] | PASS | MEDIA |
| Hospitalization Status creador | Patient Admitting yields active Hospitalization Status [G11] | PASS | ALTA |
| Sin redundancia | Hechos no duplicados innecesariamente | PASS | MEDIA |

### Checklist SD1.1

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Subprocesos transforman | Cada subproceso ≥1 transformee | PASS | CRÍTICA |
| Agent links solo humanos | Social Worker, Case Manager, Attending Physician, Clinical Nurse | PASS | CRÍTICA |
| Unicidad de link procedural | Application Receiving↔Candidate: solo effect link [C3 corregido] | PASS | CRÍTICA |
| Condition instruments | Insurance Status, Patient Age, Hospital Distance como condición | PASS | ALTA |
| Estados descriptivos | `adulto`, `dentro-de-cobertura` [A10 corregido] | PASS | ALTA |
| Default state eliminados | No default para Patient Age ni Hospital Distance [H17] | PASS | ALTA |
| Clinical Condition Evaluating | Condition instrument + yields Clinical Assessment Record (transformee presente) [A8+F2] | PASS | CRÍTICA |
| Social Report diferenciado | Preliminary Social Report ≠ Social Report [A7 corregido] | PASS | ALTA |
| Plurales ES corregidos | Pesquisar Candidato (singular) [H10] | PASS | ALTA |
| Eligibility Status split link resuelto | Informed Consent Obtaining cambia pending→eligible [G3] | PASS | CRÍTICA |
| OPD ≤ 25 entidades | SD1.1 ≈ 19 entidades | PASS | MEDIA |

### Checklist SD1.2

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Subprocesos transforman | Cada subproceso ≥1 transformee — Referral Facility Coordinating yields Referral Coordination Record [G1] | PASS | CRÍTICA |

### Checklist SD1.3

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Plan Activating presente | Nuevo subproceso cierra transición draft→active [C2 corregido] | PASS | CRÍTICA |
| Unicidad de rol Plan Activating | Sin requires duplicados — input-specified effect link porta precondición [H2] | PASS | CRÍTICA |
| Secuencia completa | 5 subprocesos en orden correcto | PASS | ALTA |
| OPD ≤ 25 entidades | SD1.3 ≈ 12 entidades | PASS | MEDIA |

### Checklist SD1.4

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Subprocesos transforman | Cada subproceso ≥1 transformee | PASS | CRÍTICA |
| Condition agent sin skip | Remote Care Regulating: Attending Physician condicional, Clinical Nurse incondicional → proceso NO se salta [A3 corregido] | PASS | ALTA |
| Condition instrument con skip | Medical Visit, Speech Therapy: skip si reduced-weekend [M2 corregido] | PASS | ALTA |
| GPS Tracking System = instrument | §6.5: software = instrument; agent link = solo humanos | PASS | ALTA |
| Shift Handover atómico en SD1.4 | Hechos de SD1.4b NO aparecen en SD1.4 [A1 corregido] | PASS | ALTA |
| Therapy Type como condition instrument | condition instrument con skip [F6] | PASS | MEDIA |
| Caregiver Knowledge con transición | Atributo Caregiver Knowledge con transición insufficient→sufficient [H12] | PASS | MEDIA |
| Wound Care: unicidad de link | single `affects Wound Status` (transiciones diferidas a SD1.4c) [F1a] | PASS | CRÍTICA |
| Speech Therapy: affects Swallowing Status | Link explícito a Swallowing and Speech Status [G8] | PASS | ALTA |
| OPD ≤ 25 entidades | SD1.4 ≈ 26 entidades — excede 25 [F15] | WARN | MEDIA |

### Checklist SD1.4a

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Route Assignment un solo default | Solo `assigned` es default [C4 corregido] | PASS | CRÍTICA |
| Proceso condicional | Unrouted Visit Resolving: condition consumption válido | PASS | ALTA |
| Dual agent humano | Driver + Coordination Professional | PASS | ALTA |
| Plural ES corregido | Resolver Visita sin Ruta (singular) [H10] | PASS | ALTA |
| OPD ≤ 25 entidades | SD1.4a ≈ 9 entidades | PASS | MEDIA |

### Checklist SD1.4b

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Dual agent Clinical Responsibility Transferring | Outgoing Clinical Nurse + Incoming Clinical Nurse [H14] | PASS | CRÍTICA |
| Nota de especialización | Outgoing/Incoming son Clinical Nurse [H14] | PASS | MEDIA |
| OPD ≤ 25 entidades | SD1.4b ≈ 6 entidades | PASS | MEDIA |

### Checklist SD1.5

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Vital Signs Data = 12 componentes | Consistente con formulario HODOM | PASS | CRÍTICA |
| Clinical Record Updating: instrument (no consumption) | Vital Signs Data como instrument [A4 corregido] | PASS | ALTA |
| Continuity Deciding: condition instrument | Skip si reduced-weekend [M2 corregido] | PASS | ALTA |
| Patient Category initial state | stable es initial y default [G10] | PASS | MEDIA |
| OPD ≤ 25 entidades | SD1.5 ≈ 19 entidades | PASS | MEDIA |

### Checklist SD1.6

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Tipo async correcto | Generalización para tipos de egreso | PASS | ALTA |
| Muerte esperada/inesperada | Distinción conforme DEIS REM A21 C.1.1 | PASS | ALTA |
| Cada especialización transforma | Todos cambian Hospitalization Status | PASS | CRÍTICA |
| Medical Discharge: condition instrument | Skip si reduced-weekend [M2 corregido] | PASS | ALTA |
| Nombres ≤4 palabras | *Egresar por Muerte Inesperada* = 4 tokens [M5 corregido] | PASS | MEDIA |
| Acute Clinical Instability | Nombre corregido (no Clinical Instability) [H16] | PASS | ALTA |
| Satisfaction Survey en Medical Discharge y Voluntary Withdrawal | Yields explícitos [H7] | PASS | ALTA |
| Voluntary Withdrawal Discharge agente | Attending Physician handles [G5] | PASS | ALTA |
| Clinical Condition propietario único | Medical Discharge changes from acute-reacutized to recovered [G2/G6] | PASS | CRÍTICA |

### Checklist SD1.7

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Subprocesos transforman | Cada subproceso ≥1 transformee | PASS | CRÍTICA |
| Agent links solo humanos | Clinical Nurse, Attending Physician, Coordination Professional | PASS | CRÍTICA |
| Condition agent sin skip | Follow-Up Call: Attending Physician condicional, Clinical Nurse incondicional [A3 corregido] | PASS | ALTA |
| Epicrisis como instrument (no consumption) | Counterreferral Sending requiere Epicrisis [A5 corregido] | PASS | ALTA |
| XOR fan para Discharge Outcome | Exactly one of favorable/unfavorable [M4 corregido] | PASS | ALTA |
| Estados muertos eliminados | Follow-Up Status: sin `completed`; Counterreferral Status: sin `acknowledged` [H5] | PASS | ALTA |
| Estados finales explícitos | contacted (Follow-Up) y sent (Counterreferral) son finales [H5] | PASS | ALTA |
| OPD ≤ 25 entidades | SD1.7 ≈ 13 entidades | PASS | MEDIA |

### Checklist SD2

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Agent = humano | Todos los roles son físicos (humanos) | PASS | ALTA |
| Speech Therapist obligatorio | Parte del Healthcare Team | PASS | ALTA |
| Case Manager especialización | Specialization de Coordination Professional | PASS | ALTA |
| Regulating Physician integrado | Parte opcional del Healthcare Team [A6 corregido] | PASS | ALTA |
| Colección incompleta declarada | "at least one other part" cubre complementarios [M1 corregido] | PASS | MEDIA |
| OPD ≤ 25 entidades | SD2 ≈ 22 entidades | PASS | MEDIA |

### Checklist SD6

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Waste Managing agente | Coordination Professional handles Waste Managing [G7] | PASS | ALTA |

### Checklist SD10

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Weekly Schedule Cycling transforma | Cambia Operational Mode (full-weekday ↔ reduced-weekend) | PASS | CRÍTICA |
| Esencia correcta | Weekly Schedule Cycling es Informatical [M3 corregido] | PASS | ALTA |
| Agent links | Ninguno (proceso ambiental — no controlable por el sistema) | PASS | ALTA |
| Objeto informatical | Operational Mode es informatical | PASS | ALTA |
| Sin exhibition de Weekly Schedule Cycling | Proceso ambiental no es feature del sistema [H3] | PASS | ALTA |
| OPD ≤ 25 entidades | SD10 = 3 entidades | PASS | MEDIA |

### Checklist Global

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Claridad | SD6 (28 entidades) excede límite de 25; candidato a split en SD6a/SD6b [A9 flaggeado] | WARN | MEDIA |
| Claridad | SD1.4 (26 entidades) excede límite de 25 [F15] | WARN | MEDIA |
| Name coherency | Sin nombres duplicados con significado diferente [A7 corregido] | PASS | ALTA |
| Implicit objects | Objetos implícitos identificados y modelados | PASS | ALTA |
| Emergencia arquitectural | El sistema produce atención hospitalaria en domicilio — capacidad emergente que ningún componente individual exhibe | PASS | MEDIA |
| Trazabilidad fuerte | Cada componente respaldado por DS 1/2022, NT 2024, DEIS REM A21, o modelo categórico HODOM v4.1 | PASS | ALTA |
| Trazabilidad normativa primaria | Referencias a artículos específicos de DS 1/2022 y NT 2024 incluidas en cada sección [M7 corregido] | PASS | MEDIA |
| OPD count | 20 OPDs | PASS | MEDIA |
| Estados normalizados | Guiones en vez de underscores [B2 corregido] | PASS | BAJA |
| OPL-ES esencia normalizada | `es informático/a` con concordancia de género [G12] | PASS | MEDIA |
| Nombres ES singulares | Plurales residuales corregidos [G13] | PASS | BAJA |
| Nombres ES ≤4 palabras | Nombres largos acortados [G14] | PASS | BAJA |

---

## Resumen de OPDs del Modelo v2.4

| OPD | Contenido | Entidades aprox. | Cambio respecto a v2.1 |
|-----|-----------|-------------------|------------------------|
| SD | Sistema HODOM — función, propósito, habilitadores, ambiente, problem occurrence | 18 | Acute Episode Occurring: esencia Physical [H4]; Primary Care Center bidireccional [H15] |
| SD1 | Descomposición — 7 subprocesos secuenciales | 21 | Care Planning: yields in active sin changes [H1]; Eligibility Status 3 estados [H6,F3a]; Post-Discharge Following +yields Discharge Outcome [F4]; Satisfaction Survey removida de Patient Discharging [H7]; Support Network Informatical [H8]; Caregiver Ambiental [H11] |
| SD1.1 | Evaluar Elegibilidad — 6 subprocesos | 20 | +Clinical Assessment Record [F2]; Candidate 2 estados [F3b]; Default state eliminados [H17]; Pesquisar Candidato (singular) [H10] |
| SD1.2 | Ingresar Paciente — 4 subprocesos | 11 | — |
| SD1.3 | Planificar Atención — 5 subprocesos | 12 | Plan Activating sin requires duplicados [H2] |
| SD1.4 | Ejecutar Plan Terapéutico — 10 subprocesos paralelos | 26 | Therapy Type: condition instrument [F6]; Wound Care: single affects [F1a]; Caregiver Knowledge con transición [H12]; WARN: >25 entidades [F15] |
| SD1.4a | Gestionar Logística Diaria — 5 subprocesos | 9 | Resolver Visita sin Ruta (singular) [H10] |
| SD1.4b | Ejecutar Entrega de Turno — 3 subprocesos | 6 | Dual agent Clinical Responsibility Transferring [H14] |
| SD1.5 | Monitorear Evolución Clínica — 4 subprocesos con 12 variables | 19 | — |
| SD1.6 | Egresar — 6 tipos de egreso | 20 | Acute Clinical Instability [H16]; Satisfaction Survey en Medical Discharge y Voluntary Withdrawal [H7] |
| SD1.7 | Seguimiento Post-Egreso — 3 subprocesos | 13 | Estados muertos eliminados (completed, acknowledged) [H5] |
| SD2 | Equipo de Salud — 12 roles + opcionales | 22 | — |
| SD3 | Infraestructura Administrativa — 11 componentes | 20 | — |
| SD4 | Equipamiento Médico — 6 dispositivos | 10 | — |
| SD5 | Sistema Documental — manuales, protocolos, plan de capacitación | 22 | — |
| SD6 | Procesos de Gobernanza — 7 operaciones | 28 | WARN: excede 25 entidades [A9] |
| SD7 | Domicilio del Paciente — condiciones de elegibilidad | 6 | — |
| SD8 | Exclusiones — 5 tipos de condición excluyente | 7 | — |
| SD9 | Relaciones estructurales etiquetadas | 12 | Primary Care Center bidireccional con tags [H15] |
| SD10 | Modo Operacional del Sistema | 3 | Sin exhibition [H3]; single affects Operational Mode [F1c] |
| **Total** | **20 OPDs** | **~265 entidades** | **14 correcciones v2.4 aplicadas** |

---

## Nota sobre SD6 (WARN)

SD6 tiene 28 entidades, excediendo el límite heurístico de 25 (§4.6 Metodología). La recomendación es dividir en:
- **SD6a**: Gestión Regulatoria y de Calidad (Autorización Sanitaria, Calidad y Seguridad, Capacitación)
- **SD6b**: Gestión Operativa (Cadena de Abastecimiento, Residuos, Mantención de Equipos, Capacidad)

Se mantiene como WARN para resolución futura.

---

_Fecha de elaboración: 2026-04-01_
_Modelo original: Mente Omega — OPM v1.0 (cumplimiento ISO/PAS 19450)_
_Integración v2.0: Subagente OPM — Mente Omega (enriquecimiento partes 1, 2 y 3)_
_Corrección v2.1: Mente Omega — auditoría exhaustiva y remediación (24 hallazgos corregidos)_
_Corrección v2.2: Mente Omega — auditoría de unicidad de rol y 15 hallazgos adicionales (16 hallazgos corregidos)_
_Corrección v2.3: Mente Omega — auditoría profunda descarnada contra corpus normativo completo (16 hallazgos: 4 CRIT, 7 ALTA, 3 MEDIA, 2 BAJA)_
_Corrección v2.4: Mente Omega — auditoría exhaustiva descarnada v2.4 (14 hallazgos: 2 CRIT, 6 ALTA, 4 MEDIA, 2 BAJA)_
