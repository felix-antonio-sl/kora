# Modelo OPM — Sistema de Hospitalización Domiciliaria (HODOM)
# Modelo Normativo

Modelo conceptual conforme a ISO/PAS 19450 (OPM).
Tipo: Normativo — modela el sistema como la normativa prescribe que debe funcionar.
Versión: 1.0
Fecha: 2026-04-02

Fuentes normativas (únicas):
- DS N° 1/2022, Reglamento de Establecimientos que Otorgan Prestaciones de Hospitalización Domiciliaria.
- Decreto Exento N° 31/2024, que aprueba la Norma Técnica para Hospitalización Domiciliaria.
- Norma Técnica HODOM 2024 (16 páginas, parte integrante del Decreto Exento N° 31).

Restricción metodológica: ningún hecho del modelo proviene de fuente distinta a los tres documentos listados.

---

## Clasificación del Sistema

**Tipo:** Socio-técnico
**Evidencia:** DS 1/2022 arts. 1-3 (modalidad asistencial con equipo humano multidisciplinario), arts. 12-14 (dotación clínica humana), arts. 18-22 (infraestructura física + sistemas informáticos), arts. 4-6 (marco regulatorio con SEREMI). Combina agentes humanos, infraestructura física, sistemas informaticales y relaciones institucionales reguladas.
**Consecuencia:** Aplican los 5 componentes del SD: purpose, main function, enablers, environment, problem occurrence. Se usan tagged structural links para relaciones institucionales.

---

## Traza del Wizard SD

| Etapa | Output | Hecho del modelo | Ref. normativa |
|-------|--------|-----------------|----------------|
| 0 | Clasificar sistema | Socio-técnico | DS 1/2022 arts. 1-3, 12-14, 18-22 |
| 1 | Proceso principal | *Domiciliary Hospitalizing* / *Hospitalizar en Domicilio* | DS 1/2022 art. 1 |
| 2 | Beneficiario | **Patient Group** (físico, sistémico) | DS 1/2022 art. 15; NT 2024 definiciones |
| 3 | Atributo de valor | **Clinical Condition**: `acute-reacutized` → `recovered` | DS 1/2022 art. 16; NT 2024 definición "Condición Clínica Estable" |
| 4 | Función principal | **Domiciliary Hospitalization System** exhibe *Domiciliary Hospitalizing* | DS 1/2022 art. 1 |
| 5 | Agencia humana | **Healthcare Team** handles *Domiciliary Hospitalizing* | DS 1/2022 arts. 12-14 |
| 6 | Sistema + exhibition | **Domiciliary Hospitalization System** + doble exhibition (función + gobernanza) | DS 1/2022 arts. 1, 7-11 |
| 7 | Instrumentos | **Patient Home**, **Medical Equipment**, **Transport Vehicle** | DS 1/2022 art. 15; NT 2024 §Equipamiento |
| 8 | Inputs/outputs | Consumes **Medication**; yields **Clinical Record** | DS 1/2022 art. 9; NT 2024 §Registros |
| 9 | Contexto externo | **Inpatient Facility**, **Current Regulation** | DS 1/2022 arts. 1, 18 |
| 10 | Problem occurrence | *Acute Episode Occurring* → `acute-reacutized` | DS 1/2022 art. 15 |
| 11 | Gate de consistencia | PASS (ver checklist SD) | — |

---

## SD — System Diagram (Nivel 0)

### Tabla de Elementos SD

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Domiciliary Hospitalizing* | Físico | Sistémico | — |
| Proceso | *System Governing* | Informatical | Sistémico | — |
| Proceso | *Acute Episode Occurring* | Físico | Ambiental | — |
| Objeto | **Patient Group** | Físico | Sistémico | — |
| Objeto | **Clinical Condition** | Informatical | Sistémico | `acute-reacutized`, `recovered` |
| Objeto | **Domiciliary Hospitalization System** | Físico | Sistémico | — |
| Objeto | **Healthcare Team** | Físico | Sistémico | — |
| Objeto | **Technical Director** | Físico | Sistémico | — |
| Objeto | **Patient Home** | Físico | Ambiental | — |
| Objeto | **Medical Equipment** | Físico | Sistémico | — |
| Objeto | **Transport Vehicle** | Físico | Sistémico | — |
| Objeto | **Medication** | Físico | Sistémico | — |
| Objeto | **Clinical Record** | Informatical | Sistémico | — |
| Objeto | **Inpatient Facility** | Físico | Ambiental | — |
| Objeto | **Current Regulation** | Informatical | Ambiental | — |

### Tabla de Enlaces SD

| Tipo | Origen | Destino | Plantilla | Ref. normativa |
|------|--------|---------|-----------|----------------|
| Exhibition-characterization | **Domiciliary Hospitalization System** | *Domiciliary Hospitalizing* | RF2b | DS 1/2022 art. 1 |
| Exhibition-characterization | **Domiciliary Hospitalization System** | *System Governing* | RF2b | DS 1/2022 arts. 7-11 |
| Exhibition-characterization | **Patient Group** | **Clinical Condition** | RF2 | DS 1/2022 art. 15 |
| Effect (input-output) | *Domiciliary Hospitalizing* | **Clinical Condition** | TS3 | DS 1/2022 art. 16 |
| Agent | **Healthcare Team** | *Domiciliary Hospitalizing* | H1 | DS 1/2022 arts. 12-14 |
| Agent | **Technical Director** | *System Governing* | H1 | DS 1/2022 arts. 7-10 |
| Instrument | *Domiciliary Hospitalizing* | **Patient Home** | H2 | DS 1/2022 art. 15 |
| Instrument | *Domiciliary Hospitalizing* | **Medical Equipment** | H2 | NT 2024 §Equipamiento |
| Instrument | *Domiciliary Hospitalizing* | **Transport Vehicle** | H2 | NT 2024 §Equipamiento |
| Consumption | *Domiciliary Hospitalizing* | **Medication** | T1 | DS 1/2022 art. 9 |
| Result | *Domiciliary Hospitalizing* | **Clinical Record** | T2 | NT 2024 §Registros |
| Tagged structural (uni) | **Inpatient Facility** | **Patient Group** | SE1 | DS 1/2022 art. 1 (derives) |
| Tagged structural (bidi) | **Domiciliary Hospitalization System** | **Inpatient Facility** | SE3 | DS 1/2022 art. 9 (readmits-to / derives) |
| Tagged structural (uni) | **Current Regulation** | **Domiciliary Hospitalization System** | SE1 | DS 1/2022 art. 18 (governs) |
| Effect (env) | *Acute Episode Occurring* | **Clinical Condition** | TS5 | DS 1/2022 art. 15 |

### OPL-EN del SD

```
Domiciliary Hospitalization System is physical.
Domiciliary Hospitalization System exhibits Domiciliary Hospitalizing as well as System Governing.

Patient Group is physical.
Patient Group exhibits Clinical Condition.
Clinical Condition is informatical.
Clinical Condition can be acute-reacutized or recovered.
State acute-reacutized of Clinical Condition is initial.
State recovered of Clinical Condition is final.

Domiciliary Hospitalizing changes Clinical Condition from acute-reacutized to recovered.

Healthcare Team is physical.
Healthcare Team handles Domiciliary Hospitalizing.

Technical Director is physical.
Technical Director handles System Governing.

Domiciliary Hospitalizing requires Patient Home.
Domiciliary Hospitalizing requires Medical Equipment.
Domiciliary Hospitalizing requires Transport Vehicle.
Domiciliary Hospitalizing consumes Medication.
Domiciliary Hospitalizing yields Clinical Record.

Patient Home is physical.
Patient Home is environmental.

Inpatient Facility is physical.
Inpatient Facility is environmental.
Inpatient Facility refers Patient Group.
Domiciliary Hospitalization System readmits-to Inpatient Facility.

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
**Sistema de Hospitalización Domiciliaria** exhibe *Hospitalizar en Domicilio* así como *Gobernar Sistema*.

**Grupo de Pacientes** es físico.
**Grupo de Pacientes** exhibe **Condición Clínica**.
**Condición Clínica** es informática.
**Condición Clínica** puede estar `agudo-reagudizado` o `recuperado`.
Estado `agudo-reagudizado` de **Condición Clínica** es inicial.
Estado `recuperado` de **Condición Clínica** es final.

*Hospitalizar en Domicilio* cambia **Condición Clínica** de `agudo-reagudizado` a `recuperado`.

**Equipo de Salud** es físico.
**Equipo de Salud** maneja *Hospitalizar en Domicilio*.

**Director Técnico** es físico.
**Director Técnico** maneja *Gobernar Sistema*.

*Hospitalizar en Domicilio* requiere **Domicilio del Paciente**.
*Hospitalizar en Domicilio* requiere **Equipamiento Médico**.
*Hospitalizar en Domicilio* requiere **Vehículo de Transporte**.
*Hospitalizar en Domicilio* consume **Medicamento**.
*Hospitalizar en Domicilio* genera **Ficha Clínica**.

**Domicilio del Paciente** es físico.
**Domicilio del Paciente** es ambiental.

**Establecimiento de Atención Cerrada** es físico.
**Establecimiento de Atención Cerrada** es ambiental.
**Establecimiento de Atención Cerrada** deriva **Grupo de Pacientes**.
**Sistema de Hospitalización Domiciliaria** reingresa a **Establecimiento de Atención Cerrada**.

**Normativa Vigente** es informática.
**Normativa Vigente** es ambiental.
**Normativa Vigente** rige **Sistema de Hospitalización Domiciliaria**.

*Ocurrir Episodio Agudo* es físico.
*Ocurrir Episodio Agudo* es ambiental.
*Ocurrir Episodio Agudo* cambia **Condición Clínica** a `agudo-reagudizado`.
```

### Validación SD

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Sistema clasificado | Socio-técnico determinado | PASS | CRÍTICA |
| Purpose definido | Patient Group + Clinical Condition + acute-reacutized → recovered | PASS | CRÍTICA |
| Función definida | Domiciliary Hospitalizing + Patient Group (transformee) | PASS | CRÍTICA |
| Enablers presentes | 1 agente + 3 instrumentos | PASS | ALTA |
| Environment identificado | 3 objetos ambientales (Patient Home, Inpatient Facility, Current Regulation) | PASS | MEDIA |
| Problem occurrence | Acute Episode Occurring → acute-reacutized | PASS | MEDIA |
| Naming | Gerundio EN / Infinitivo ES | PASS | ALTA |
| Exhibition | Sistema exhibe proceso principal + gobernanza | PASS | ALTA |
| Agents = humanos | Healthcare Team, Technical Director | PASS | ALTA |
| Tagged structural homogéneos | Todos obj↔obj | PASS | ALTA |
| OPD ≤ 25 | 15 entidades | PASS | MEDIA |

Ref. normativa: DS 1/2022 art. 1 (definición HODOM), art. 15 (criterios de ingreso), art. 16 (causales de egreso), arts. 7-11 (gobernanza).

---

## SD1 — Descomposición de *Domiciliary Hospitalizing*

Refinamiento: in-zooming (5 subprocesos secuenciales).

### Tabla de Elementos SD1

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Eligibility Evaluating* | Informatical | Sistémico | — |
| Proceso | *Patient Admitting* | Informatical | Sistémico | — |
| Proceso | *Care Planning* | Informatical | Sistémico | — |
| Proceso | *Domiciliary Care Delivering* | Físico | Sistémico | — |
| Proceso | *Patient Discharging* | Informatical | Sistémico | — |
| Objeto | **Eligibility Status** | Informatical | Sistémico | `pending`, `eligible` |
| Objeto | **Informed Consent** | Informatical | Sistémico | `unsigned`, `signed` |
| Objeto | **Caregiver** | Físico | Ambiental | `available`, `unavailable` |
| Objeto | **Therapeutic Plan** | Informatical | Sistémico | `draft`, `active` |
| Objeto | **Hospitalization Status** | Informatical | Sistémico | `active`, `discharged` |
| Objeto | **Epicrisis** | Informatical | Sistémico | — |
| Objeto | **Attending Physician** | Físico | Sistémico | — |

Objetos heredados del SD: Clinical Condition, Patient Group, Healthcare Team, Patient Home, Medical Equipment, Transport Vehicle, Medication, Clinical Record, Inpatient Facility.

### Tabla de Enlaces SD1

| Tipo | Origen | Destino | Plantilla | Ref. normativa |
|------|--------|---------|-----------|----------------|
| Effect (input-output) | *Eligibility Evaluating* | **Eligibility Status** | TS3 | DS 1/2022 art. 15 |
| Instrument | *Eligibility Evaluating* | **Patient Home** | H2 | DS 1/2022 art. 15 (condiciones domicilio) |
| Instrument | *Eligibility Evaluating* | **Inpatient Facility** | H2 | DS 1/2022 art. 1 (derivación) |
| Instrument (condition) | *Eligibility Evaluating* | **Caregiver** | HS2 | DS 1/2022 art. 15 (red de apoyo) |
| Effect (input-output) | *Patient Admitting* | **Informed Consent** | TS3 | DS 1/2022 art. 15 (consentimiento) |
| Result | *Patient Admitting* | **Clinical Record** | T2 | NT 2024 §Registros |
| Result (state-specified) | *Patient Admitting* | **Hospitalization Status** | TS2 | DS 1/2022 art. 15 |
| Result (state-specified) | *Care Planning* | **Therapeutic Plan** | TS2 | DS 1/2022 art. 1 (plan terapéutico) |
| Effect (input-output) | *Care Planning* | **Therapeutic Plan** | TS3 | DS 1/2022 art. 1 |
| Agent | **Attending Physician** | *Care Planning* | H1 | DS 1/2022 art. 12 (indicar tratamiento) |
| Instrument (state-specified) | *Domiciliary Care Delivering* | **Therapeutic Plan** | HS2 | DS 1/2022 art. 1 (requiere plan activo) |
| Effect | *Domiciliary Care Delivering* | **Patient Group** | T3 | DS 1/2022 arts. 12-14 |
| Effect | *Domiciliary Care Delivering* | **Clinical Condition** | T3 | DS 1/2022 art. 12 |
| Effect | *Domiciliary Care Delivering* | **Clinical Record** | T3 | NT 2024 §Registros (resumen clínico) |
| Instrument | *Domiciliary Care Delivering* | **Medical Equipment** | H2 | NT 2024 §Equipamiento |
| Instrument | *Domiciliary Care Delivering* | **Transport Vehicle** | H2 | NT 2024 §Equipamiento |
| Instrument | *Domiciliary Care Delivering* | **Patient Home** | H2 | DS 1/2022 art. 15 |
| Consumption | *Domiciliary Care Delivering* | **Medication** | T1 | DS 1/2022 art. 9 |
| Effect (input-output) | *Patient Discharging* | **Hospitalization Status** | TS3 | DS 1/2022 art. 16 |
| Result | *Patient Discharging* | **Epicrisis** | T2 | NT 2024 §Registros |
| Agent (outer) | **Healthcare Team** | *Domiciliary Hospitalizing* | H1 | DS 1/2022 arts. 12-14 |

### OPL-EN del SD1

```
SD is refined by in-zooming Domiciliary Hospitalizing in SD1.
Domiciliary Hospitalizing zooms into Eligibility Evaluating, Patient Admitting, Care Planning, Domiciliary Care Delivering and Patient Discharging, in that sequence.

Eligibility Status is informatical.
Eligibility Status can be pending or eligible.
State pending of Eligibility Status is initial.
State eligible of Eligibility Status is final.
Eligibility Evaluating changes Eligibility Status from pending to eligible.
Eligibility Evaluating requires Patient Home.
Eligibility Evaluating requires Inpatient Facility.
Eligibility Evaluating requires available Caregiver.

Caregiver is physical.
Caregiver is environmental.
Caregiver can be available or unavailable.

Informed Consent is informatical.
Informed Consent can be unsigned or signed.
State unsigned of Informed Consent is initial.
State signed of Informed Consent is final.
Patient Admitting changes Informed Consent from unsigned to signed.
Patient Admitting yields Clinical Record.

Hospitalization Status is informatical.
Hospitalization Status can be active or discharged.
State active of Hospitalization Status is initial.
State discharged of Hospitalization Status is final.
Patient Admitting yields active Hospitalization Status.

Therapeutic Plan is informatical.
Therapeutic Plan can be draft or active.
State draft of Therapeutic Plan is initial.
State active of Therapeutic Plan is final.
Care Planning yields draft Therapeutic Plan.
Care Planning changes Therapeutic Plan from draft to active.
Attending Physician handles Care Planning.

Domiciliary Care Delivering requires active Therapeutic Plan.
Domiciliary Care Delivering affects Patient Group.
Domiciliary Care Delivering affects Clinical Condition.
Domiciliary Care Delivering affects Clinical Record.
Domiciliary Care Delivering requires Medical Equipment.
Domiciliary Care Delivering requires Transport Vehicle.
Domiciliary Care Delivering requires Patient Home.
Domiciliary Care Delivering consumes Medication.

Patient Discharging changes Hospitalization Status from active to discharged.
Patient Discharging yields Epicrisis.

Healthcare Team handles Eligibility Evaluating.
Healthcare Team handles Patient Admitting.
Healthcare Team handles Domiciliary Care Delivering.
Healthcare Team handles Patient Discharging.
```

### OPL-ES del SD1

```
SD se refina por descomposición de *Hospitalizar en Domicilio* en SD1.
*Hospitalizar en Domicilio* se descompone en *Evaluar Elegibilidad*, *Ingresar Paciente*, *Planificar Atención*, *Entregar Cuidados en Domicilio* y *Egresar Paciente*, en esa secuencia.

**Estado de Elegibilidad** es informático.
**Estado de Elegibilidad** puede estar `pendiente` o `elegible`.
Estado `pendiente` de **Estado de Elegibilidad** es inicial.
Estado `elegible` de **Estado de Elegibilidad** es final.
*Evaluar Elegibilidad* cambia **Estado de Elegibilidad** de `pendiente` a `elegible`.
*Evaluar Elegibilidad* requiere **Domicilio del Paciente**.
*Evaluar Elegibilidad* requiere **Establecimiento de Atención Cerrada**.
*Evaluar Elegibilidad* requiere **Cuidador** en `disponible`.

**Cuidador** es físico.
**Cuidador** es ambiental.
**Cuidador** puede estar `disponible` o `no disponible`.

**Consentimiento Informado** es informático.
**Consentimiento Informado** puede estar `sin firmar` o `firmado`.
Estado `sin firmar` de **Consentimiento Informado** es inicial.
Estado `firmado` de **Consentimiento Informado** es final.
*Ingresar Paciente* cambia **Consentimiento Informado** de `sin firmar` a `firmado`.
*Ingresar Paciente* genera **Ficha Clínica**.

**Estado de Hospitalización** es informático.
**Estado de Hospitalización** puede estar `activa` o `egresado`.
Estado `activa` de **Estado de Hospitalización** es inicial.
Estado `egresado` de **Estado de Hospitalización** es final.
*Ingresar Paciente* genera **Estado de Hospitalización** en `activa`.

**Plan Terapéutico** es informático.
**Plan Terapéutico** puede estar `borrador` o `activo`.
Estado `borrador` de **Plan Terapéutico** es inicial.
Estado `activo` de **Plan Terapéutico** es final.
*Planificar Atención* genera **Plan Terapéutico** en `borrador`.
*Planificar Atención* cambia **Plan Terapéutico** de `borrador` a `activo`.
**Médico de Atención Directa** maneja *Planificar Atención*.

*Entregar Cuidados en Domicilio* requiere **Plan Terapéutico** en `activo`.
*Entregar Cuidados en Domicilio* afecta **Grupo de Pacientes**.
*Entregar Cuidados en Domicilio* afecta **Condición Clínica**.
*Entregar Cuidados en Domicilio* afecta **Ficha Clínica**.
*Entregar Cuidados en Domicilio* requiere **Equipamiento Médico**.
*Entregar Cuidados en Domicilio* requiere **Vehículo de Transporte**.
*Entregar Cuidados en Domicilio* requiere **Domicilio del Paciente**.
*Entregar Cuidados en Domicilio* consume **Medicamento**.

*Egresar Paciente* cambia **Estado de Hospitalización** de `activa` a `egresado`.
*Egresar Paciente* genera **Epicrisis**.

**Equipo de Salud** maneja *Evaluar Elegibilidad*.
**Equipo de Salud** maneja *Ingresar Paciente*.
**Equipo de Salud** maneja *Entregar Cuidados en Domicilio*.
**Equipo de Salud** maneja *Egresar Paciente*.
```

### Validación SD1

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Subprocesos transforman | Cada uno ≥1 transformee | PASS | CRÍTICA |
| Refinamiento correcto | Secuencial → in-zooming | PASS | ALTA |
| Links distribuidos | Consumption/result no en outer contour | PASS | CRÍTICA |
| Agent outer contour | Healthcare Team distribuye a todos | PASS | ALTA |
| Split link resuelto | Clinical Condition: affects en Care Delivering; transición específica en SD1.2 Medical Discharging | PASS | ALTA |
| Art. 1 mapeado | 4 requisitos estructurales: indicación médica, plan terapéutico, control médico, término por egreso | PASS | ALTA |
| OPD ≤ 25 | 21 entidades | PASS | MEDIA |
| Naming | Gerundio EN / Infinitivo ES | PASS | ALTA |

Ref. normativa: DS 1/2022 art. 1 (requisitos estructurales), art. 15 (ingreso), art. 16 (egreso); NT 2024 §Registros, §Protocolos.

---

## SD1.1 — Descomposición de *Domiciliary Care Delivering*

Refinamiento: in-zooming con paralelismo (4 modalidades de cuidado asíncronas).

### Tabla de Elementos SD1.1

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Clinical Visiting* | Físico | Sistémico | — |
| Proceso | *Nursing Care Executing* | Físico | Sistémico | — |
| Proceso | *Rehabilitative Therapy Delivering* | Físico | Sistémico | — |
| Proceso | *Patient Educating* | Informatical | Sistémico | — |
| Objeto | **Attending Physician** | Físico | Sistémico | — |
| Objeto | **Clinical Nurse** | Físico | Sistémico | — |
| Objeto | **Kinesiologist** | Físico | Sistémico | — |
| Objeto | **Caregiver Knowledge** | Informatical | Sistémico | `insufficient`, `sufficient` |

Objetos heredados: Patient Group, Medical Equipment, Transport Vehicle, Patient Home, Medication, Clinical Record, Therapeutic Plan, Caregiver.

### Tabla de Enlaces SD1.1

| Tipo | Origen | Destino | Plantilla | Ref. normativa |
|------|--------|---------|-----------|----------------|
| Effect | *Clinical Visiting* | **Patient Group** | T3 | DS 1/2022 art. 12 (evaluar e indicar tratamiento) |
| Effect | *Clinical Visiting* | **Clinical Record** | T3 | NT 2024 §Registros |
| Instrument | *Clinical Visiting* | **Medical Equipment** | H2 | NT 2024 §Equipamiento |
| Agent | **Attending Physician** | *Clinical Visiting* | H1 | DS 1/2022 art. 12 |
| Effect | *Nursing Care Executing* | **Patient Group** | T3 | DS 1/2022 art. 13 (gestionar cuidados) |
| Effect | *Nursing Care Executing* | **Clinical Record** | T3 | NT 2024 §Registros |
| Instrument | *Nursing Care Executing* | **Medical Equipment** | H2 | NT 2024 §Equipamiento |
| Consumption | *Nursing Care Executing* | **Medication** | T1 | DS 1/2022 art. 9 |
| Agent | **Clinical Nurse** | *Nursing Care Executing* | H1 | DS 1/2022 art. 13 |
| Effect | *Rehabilitative Therapy Delivering* | **Patient Group** | T3 | DS 1/2022 art. 13 (terapias motoras y respiratorias) |
| Instrument | *Rehabilitative Therapy Delivering* | **Medical Equipment** | H2 | NT 2024 §Equipamiento |
| Agent | **Kinesiologist** | *Rehabilitative Therapy Delivering* | H1 | DS 1/2022 art. 13 |
| Exhibition-characterization | **Caregiver** | **Caregiver Knowledge** | RF2 | DS 1/2022 art. 13 (educar cuidadores) |
| Effect (input-output) | *Patient Educating* | **Caregiver Knowledge** | TS3 | DS 1/2022 art. 13 |
| Effect | *Patient Educating* | **Patient Group** | T3 | DS 1/2022 art. 13 |
| Agent | **Clinical Nurse** | *Patient Educating* | H1 | DS 1/2022 art. 13 |
| Instrument (outer) | *Domiciliary Care Delivering* | **Transport Vehicle** | H2 | NT 2024 §Equipamiento |
| Instrument (outer) | *Domiciliary Care Delivering* | **Patient Home** | H2 | DS 1/2022 art. 15 |
| Instrument (outer) | *Domiciliary Care Delivering* | **Therapeutic Plan** | HS2 | DS 1/2022 art. 1 |

### OPL-EN SD1.1

```
SD1 is refined by in-zooming Domiciliary Care Delivering in SD1.1.
Domiciliary Care Delivering zooms into parallel Clinical Visiting, Nursing Care Executing, Rehabilitative Therapy Delivering and Patient Educating.

Clinical Visiting affects Patient Group.
Clinical Visiting affects Clinical Record.
Clinical Visiting requires Medical Equipment.
Attending Physician handles Clinical Visiting.

Nursing Care Executing affects Patient Group.
Nursing Care Executing affects Clinical Record.
Nursing Care Executing requires Medical Equipment.
Nursing Care Executing consumes Medication.
Clinical Nurse handles Nursing Care Executing.

Rehabilitative Therapy Delivering affects Patient Group.
Rehabilitative Therapy Delivering requires Medical Equipment.
Kinesiologist handles Rehabilitative Therapy Delivering.

Caregiver Knowledge is informatical.
Caregiver exhibits Caregiver Knowledge.
Caregiver Knowledge can be insufficient or sufficient.
State insufficient of Caregiver Knowledge is initial.
State sufficient of Caregiver Knowledge is final.
Patient Educating changes Caregiver Knowledge from insufficient to sufficient.
Patient Educating affects Patient Group.
Clinical Nurse handles Patient Educating.

Domiciliary Care Delivering requires active Therapeutic Plan.
Domiciliary Care Delivering requires Transport Vehicle.
Domiciliary Care Delivering requires Patient Home.
```

### OPL-ES SD1.1

```
SD1 se refina por descomposición de *Entregar Cuidados en Domicilio* en SD1.1.
*Entregar Cuidados en Domicilio* se descompone en paralelo *Visitar Clínicamente*, *Ejecutar Cuidados de Enfermería*, *Entregar Terapia Rehabilitadora* y *Educar al Paciente*.

*Visitar Clínicamente* afecta **Grupo de Pacientes**.
*Visitar Clínicamente* afecta **Ficha Clínica**.
*Visitar Clínicamente* requiere **Equipamiento Médico**.
**Médico de Atención Directa** maneja *Visitar Clínicamente*.

*Ejecutar Cuidados de Enfermería* afecta **Grupo de Pacientes**.
*Ejecutar Cuidados de Enfermería* afecta **Ficha Clínica**.
*Ejecutar Cuidados de Enfermería* requiere **Equipamiento Médico**.
*Ejecutar Cuidados de Enfermería* consume **Medicamento**.
**Enfermero Clínico** maneja *Ejecutar Cuidados de Enfermería*.

*Entregar Terapia Rehabilitadora* afecta **Grupo de Pacientes**.
*Entregar Terapia Rehabilitadora* requiere **Equipamiento Médico**.
**Kinesiólogo** maneja *Entregar Terapia Rehabilitadora*.

**Conocimiento del Cuidador** es informático.
**Cuidador** exhibe **Conocimiento del Cuidador**.
**Conocimiento del Cuidador** puede estar `insuficiente` o `suficiente`.
Estado `insuficiente` de **Conocimiento del Cuidador** es inicial.
Estado `suficiente` de **Conocimiento del Cuidador** es final.
*Educar al Paciente* cambia **Conocimiento del Cuidador** de `insuficiente` a `suficiente`.
*Educar al Paciente* afecta **Grupo de Pacientes**.
**Enfermero Clínico** maneja *Educar al Paciente*.

*Entregar Cuidados en Domicilio* requiere **Plan Terapéutico** en `activo`.
*Entregar Cuidados en Domicilio* requiere **Vehículo de Transporte**.
*Entregar Cuidados en Domicilio* requiere **Domicilio del Paciente**.
```

### Validación SD1.1

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Subprocesos transforman | Cada uno ≥1 transformee | PASS | CRÍTICA |
| Refinamiento correcto | Async paralelo → in-zooming con parallel keyword | PASS | ALTA |
| Links distribuidos | Consumption migrada a Nursing Care; Transport/Home/Plan en outer contour (instruments OK) | PASS | CRÍTICA |
| Agent = humano | Attending Physician, Clinical Nurse, Kinesiologist — todos humanos | PASS | ALTA |
| Patient Educating transformee | Caregiver Knowledge (atributo de objeto ambiental) — transformación fuera del sistema | PASS | ALTA |
| OPD ≤ 25 | 14 entidades | PASS | MEDIA |
| Naming | Gerundio EN / Infinitivo ES | PASS | ALTA |

Ref. normativa: DS 1/2022 arts. 12-14 (funciones por rol profesional); NT 2024 §Equipamiento.

---

## SD1.2 — Despliegue de *Patient Discharging*

Refinamiento: unfolding por generalización-especialización (5 tipos de egreso mutuamente excluyentes).

### Tabla de Elementos SD1.2

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Medical Discharging* | Informatical | Sistémico | — |
| Proceso | *Hospital Readmission Discharging* | Informatical | Sistémico | — |
| Proceso | *Death Discharging* | Informatical | Sistémico | — |
| Proceso | *Voluntary Withdrawal Discharging* | Informatical | Sistémico | — |
| Proceso | *Disciplinary Discharging* | Informatical | Sistémico | — |
| Objeto | **Technical Director** | Físico | Sistémico | — |

Objetos heredados: Clinical Condition, Hospitalization Status, Epicrisis, Attending Physician, Informed Consent, Inpatient Facility, Transport Vehicle.

### Tabla de Enlaces SD1.2

| Tipo | Origen | Destino | Plantilla | Ref. normativa |
|------|--------|---------|-----------|----------------|
| Generalization-specialization | 5 procesos | *Patient Discharging* | RF3 | DS 1/2022 art. 16 |
| Effect (input-output) | *Medical Discharging* | **Clinical Condition** | TS3 | DS 1/2022 art. 16 (alta por recuperación) |
| Effect (input-output) | *Medical Discharging* | **Hospitalization Status** | TS3 | DS 1/2022 art. 16 |
| Result | *Medical Discharging* | **Epicrisis** | T2 | NT 2024 §Registros |
| Agent | **Attending Physician** | *Medical Discharging* | H1 | DS 1/2022 art. 12 |
| Effect (input-output) | *Hospital Readmission Discharging* | **Hospitalization Status** | TS3 | DS 1/2022 art. 16 (reingreso) |
| Instrument | *Hospital Readmission Discharging* | **Inpatient Facility** | H2 | DS 1/2022 art. 9 (traslado) |
| Instrument | *Hospital Readmission Discharging* | **Transport Vehicle** | H2 | DS 1/2022 art. 9 (traslado oportuno) |
| Result | *Hospital Readmission Discharging* | **Epicrisis** | T2 | NT 2024 §Registros |
| Agent | **Attending Physician** | *Hospital Readmission Discharging* | H1 | DS 1/2022 art. 12 |
| Effect (input-output) | *Death Discharging* | **Hospitalization Status** | TS3 | DS 1/2022 art. 16 (fallecimiento) |
| Result | *Death Discharging* | **Epicrisis** | T2 | NT 2024 §Registros |
| Agent | **Attending Physician** | *Death Discharging* | H1 | DS 1/2022 art. 12 |
| Effect (input-output) | *Voluntary Withdrawal Discharging* | **Hospitalization Status** | TS3 | DS 1/2022 art. 16 (renuncia) |
| Instrument (state-specified) | *Voluntary Withdrawal Discharging* | **Informed Consent** | HS2 | DS 1/2022 art. 15 |
| Result | *Voluntary Withdrawal Discharging* | **Epicrisis** | T2 | NT 2024 §Registros |
| Agent | **Attending Physician** | *Voluntary Withdrawal Discharging* | H1 | DS 1/2022 art. 12 |
| Effect (input-output) | *Disciplinary Discharging* | **Hospitalization Status** | TS3 | DS 1/2022 art. 16 f) |
| Result | *Disciplinary Discharging* | **Epicrisis** | T2 | NT 2024 §Registros |
| Agent | **Technical Director** | *Disciplinary Discharging* | H1 | DS 1/2022 art. 16 f) (Dirección Técnica) |

### OPL-EN SD1.2

```
SD1 is refined by unfolding Patient Discharging in SD1.2.
Medical Discharging, Hospital Readmission Discharging, Death Discharging, Voluntary Withdrawal Discharging and Disciplinary Discharging are Patient Discharging.

Medical Discharging changes Clinical Condition from acute-reacutized to recovered.
Medical Discharging changes Hospitalization Status from active to discharged.
Medical Discharging yields Epicrisis.
Attending Physician handles Medical Discharging.

Hospital Readmission Discharging changes Hospitalization Status from active to discharged.
Hospital Readmission Discharging requires Inpatient Facility.
Hospital Readmission Discharging requires Transport Vehicle.
Hospital Readmission Discharging yields Epicrisis.
Attending Physician handles Hospital Readmission Discharging.

Death Discharging changes Hospitalization Status from active to discharged.
Death Discharging yields Epicrisis.
Attending Physician handles Death Discharging.

Voluntary Withdrawal Discharging changes Hospitalization Status from active to discharged.
Voluntary Withdrawal Discharging requires signed Informed Consent.
Voluntary Withdrawal Discharging yields Epicrisis.
Attending Physician handles Voluntary Withdrawal Discharging.

Disciplinary Discharging changes Hospitalization Status from active to discharged.
Disciplinary Discharging yields Epicrisis.
Technical Director handles Disciplinary Discharging.
```

### OPL-ES SD1.2

```
SD1 se refina por despliegue de *Egresar Paciente* en SD1.2.
*Egresar por Alta Médica*, *Egresar por Reingreso Hospitalario*, *Egresar por Fallecimiento*, *Egresar por Renuncia Voluntaria* y *Egresar por Alta Disciplinaria* son *Egresar Paciente*.

*Egresar por Alta Médica* cambia **Condición Clínica** de `agudo-reagudizado` a `recuperado`.
*Egresar por Alta Médica* cambia **Estado de Hospitalización** de `activa` a `egresado`.
*Egresar por Alta Médica* genera **Epicrisis**.
**Médico de Atención Directa** maneja *Egresar por Alta Médica*.

*Egresar por Reingreso Hospitalario* cambia **Estado de Hospitalización** de `activa` a `egresado`.
*Egresar por Reingreso Hospitalario* requiere **Establecimiento de Atención Cerrada**.
*Egresar por Reingreso Hospitalario* requiere **Vehículo de Transporte**.
*Egresar por Reingreso Hospitalario* genera **Epicrisis**.
**Médico de Atención Directa** maneja *Egresar por Reingreso Hospitalario*.

*Egresar por Fallecimiento* cambia **Estado de Hospitalización** de `activa` a `egresado`.
*Egresar por Fallecimiento* genera **Epicrisis**.
**Médico de Atención Directa** maneja *Egresar por Fallecimiento*.

*Egresar por Renuncia Voluntaria* cambia **Estado de Hospitalización** de `activa` a `egresado`.
*Egresar por Renuncia Voluntaria* requiere **Consentimiento Informado** en `firmado`.
*Egresar por Renuncia Voluntaria* genera **Epicrisis**.
**Médico de Atención Directa** maneja *Egresar por Renuncia Voluntaria*.

*Egresar por Alta Disciplinaria* cambia **Estado de Hospitalización** de `activa` a `egresado`.
*Egresar por Alta Disciplinaria* genera **Epicrisis**.
**Director Técnico** maneja *Egresar por Alta Disciplinaria*.
```

### Validación SD1.2

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Tipo async correcto | Generalización para tipos de egreso (variantes del mismo patrón) | PASS | ALTA |
| Cada especialización transforma | Todos cambian Hospitalization Status | PASS | CRÍTICA |
| Medical Discharging único con Clinical Condition | Solo el alta médica transiciona a recovered | PASS | ALTA |
| Agent = humano | Attending Physician (4 tipos) + Technical Director (disciplinaria) | PASS | ALTA |
| Separación autoridad clínica/institucional | Disciplinary Discharging → Technical Director | PASS | ALTA |
| OPD ≤ 25 | ~12 entidades | PASS | MEDIA |
| Naming | Gerundio EN / Infinitivo ES | PASS | ALTA |

Ref. normativa: DS 1/2022 art. 16 (causales de egreso); art. 16 f) (alta disciplinaria por Dirección Técnica).

---

## SD3 — Descomposición de *System Governing*

Refinamiento: in-zooming con paralelismo (5 procesos de gobernanza asíncronos).

### Tabla de Elementos SD3

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Sanitary Authorization Managing* | Informatical | Sistémico | — |
| Proceso | *Protocol Governing* | Informatical | Sistémico | — |
| Proceso | *Supply and Equipment Managing* | Informatical | Sistémico | — |
| Proceso | *Quality and Safety Auditing* | Informatical | Sistémico | — |
| Proceso | *Staff Training Managing* | Informatical | Sistémico | — |
| Objeto | **Coordination Professional** | Físico | Sistémico | — |
| Objeto | **Sanitary Authorization Status** | Informatical | Sistémico | `pending`, `authorized`, `expired` |
| Objeto | **Protocol Set** | Informatical | Sistémico | `outdated`, `current` |
| Objeto | **Training Compliance** | Informatical | Sistémico | `non-compliant`, `compliant` |
| Objeto | **SEREMI** | Físico | Ambiental | — |

Objetos heredados: Technical Director, Current Regulation, Medical Equipment, Medication, Clinical Record, Healthcare Team, Domiciliary Hospitalization System.

### Tabla de Enlaces SD3

| Tipo | Origen | Destino | Plantilla | Ref. normativa |
|------|--------|---------|-----------|----------------|
| Exhibition-characterization | **Domiciliary Hospitalization System** | **Sanitary Authorization Status** | RF2 | DS 1/2022 arts. 4-6 |
| Effect (input-output) | *Sanitary Authorization Managing* | **Sanitary Authorization Status** | TS3 | DS 1/2022 art. 4 |
| Instrument | *Sanitary Authorization Managing* | **Current Regulation** | H2 | DS 1/2022 art. 4 |
| Instrument | *Sanitary Authorization Managing* | **SEREMI** | H2 | DS 1/2022 art. 4 |
| Agent | **Technical Director** | *Sanitary Authorization Managing* | H1 | DS 1/2022 arts. 7-10 |
| Effect (input-output) | *Protocol Governing* | **Protocol Set** | TS3 | DS 1/2022 art. 9 (aprobar manuales) |
| Instrument | *Protocol Governing* | **Current Regulation** | H2 | DS 1/2022 art. 9 |
| Agent | **Technical Director** | *Protocol Governing* | H1 | DS 1/2022 art. 9 |
| Effect | *Supply and Equipment Managing* | **Medical Equipment** | T3 | DS 1/2022 art. 9 (mantención) |
| Effect | *Supply and Equipment Managing* | **Medication** | T3 | DS 1/2022 art. 9 (stock) |
| Agent | **Coordination Professional** | *Supply and Equipment Managing* | H1 | DS 1/2022 art. 11 |
| Effect | *Quality and Safety Auditing* | **Domiciliary Hospitalization System** | T3 | DS 1/2022 art. 9 (auditorías) |
| Instrument | *Quality and Safety Auditing* | **Clinical Record** | H2 | DS 1/2022 art. 9 |
| Agent | **Technical Director** | *Quality and Safety Auditing* | H1 | DS 1/2022 art. 9 |
| Exhibition-characterization | **Healthcare Team** | **Training Compliance** | RF2 | NT 2024 §Inducción |
| Effect (input-output) | *Staff Training Managing* | **Training Compliance** | TS3 | DS 1/2022 art. 11; NT 2024 §PAC |
| Agent | **Coordination Professional** | *Staff Training Managing* | H1 | DS 1/2022 art. 11 |

### OPL-EN SD3

```
SD is refined by in-zooming System Governing in SD3.
System Governing zooms into parallel Sanitary Authorization Managing, Protocol Governing, Supply and Equipment Managing, Quality and Safety Auditing and Staff Training Managing.

Sanitary Authorization Status is informatical.
Sanitary Authorization Status can be pending, authorized or expired.
State pending of Sanitary Authorization Status is initial.
Domiciliary Hospitalization System exhibits Sanitary Authorization Status.
Sanitary Authorization Managing changes Sanitary Authorization Status from pending to authorized.
Sanitary Authorization Managing requires Current Regulation.
Sanitary Authorization Managing requires SEREMI.
Technical Director handles Sanitary Authorization Managing.

SEREMI is physical.
SEREMI is environmental.

Protocol Set is informatical.
Protocol Set can be outdated or current.
State outdated of Protocol Set is initial.
Protocol Governing changes Protocol Set from outdated to current.
Protocol Governing requires Current Regulation.
Technical Director handles Protocol Governing.

Supply and Equipment Managing affects Medical Equipment.
Supply and Equipment Managing affects Medication.
Coordination Professional handles Supply and Equipment Managing.

Quality and Safety Auditing affects Domiciliary Hospitalization System.
Quality and Safety Auditing requires Clinical Record.
Technical Director handles Quality and Safety Auditing.

Training Compliance is informatical.
Training Compliance can be non-compliant or compliant.
State non-compliant of Training Compliance is initial.
Healthcare Team exhibits Training Compliance.
Staff Training Managing changes Training Compliance from non-compliant to compliant.
Coordination Professional handles Staff Training Managing.
```

### OPL-ES SD3

```
SD se refina por descomposición de *Gobernar Sistema* en SD3.
*Gobernar Sistema* se descompone en paralelo *Gestionar Autorización Sanitaria*, *Gobernar Protocolos*, *Gestionar Abastecimiento y Equipos*, *Auditar Calidad y Seguridad* y *Gestionar Capacitación del Personal*.

**Estado de Autorización Sanitaria** es informático.
**Estado de Autorización Sanitaria** puede estar `pendiente`, `autorizado` o `vencido`.
Estado `pendiente` de **Estado de Autorización Sanitaria** es inicial.
**Sistema de Hospitalización Domiciliaria** exhibe **Estado de Autorización Sanitaria**.
*Gestionar Autorización Sanitaria* cambia **Estado de Autorización Sanitaria** de `pendiente` a `autorizado`.
*Gestionar Autorización Sanitaria* requiere **Normativa Vigente**.
*Gestionar Autorización Sanitaria* requiere **SEREMI**.
**Director Técnico** maneja *Gestionar Autorización Sanitaria*.

**SEREMI** es físico.
**SEREMI** es ambiental.

**Conjunto de Protocolos** es informático.
**Conjunto de Protocolos** puede estar `desactualizado` o `vigente`.
Estado `desactualizado` de **Conjunto de Protocolos** es inicial.
*Gobernar Protocolos* cambia **Conjunto de Protocolos** de `desactualizado` a `vigente`.
*Gobernar Protocolos* requiere **Normativa Vigente**.
**Director Técnico** maneja *Gobernar Protocolos*.

*Gestionar Abastecimiento y Equipos* afecta **Equipamiento Médico**.
*Gestionar Abastecimiento y Equipos* afecta **Medicamento**.
**Profesional Coordinador** maneja *Gestionar Abastecimiento y Equipos*.

*Auditar Calidad y Seguridad* afecta **Sistema de Hospitalización Domiciliaria**.
*Auditar Calidad y Seguridad* requiere **Ficha Clínica**.
**Director Técnico** maneja *Auditar Calidad y Seguridad*.

**Cumplimiento de Capacitación** es informático.
**Cumplimiento de Capacitación** puede estar `no cumple` o `cumple`.
Estado `no cumple` de **Cumplimiento de Capacitación** es inicial.
**Equipo de Salud** exhibe **Cumplimiento de Capacitación**.
*Gestionar Capacitación del Personal* cambia **Cumplimiento de Capacitación** de `no cumple` a `cumple`.
**Profesional Coordinador** maneja *Gestionar Capacitación del Personal*.
```

### Validación SD3

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Subprocesos transforman | Cada uno ≥1 transformee | PASS | CRÍTICA |
| Refinamiento correcto | Async paralelo → in-zooming con parallel keyword | PASS | ALTA |
| Agent = humano | Technical Director (3), Coordination Professional (2) | PASS | ALTA |
| SEREMI ambiental | Fuera del control del sistema | PASS | MEDIA |
| Separación Director/Coordinador | 3 procesos Director (representación, protocolos, auditoría) + 2 Coordinador (abastecimiento, capacitación) | PASS | ALTA |
| OPD ≤ 25 | 11 entidades | PASS | MEDIA |
| Naming | Gerundio EN / Infinitivo ES | PASS | ALTA |

Ref. normativa: DS 1/2022 arts. 4-6 (autorización sanitaria), arts. 7-10 (Dirección Técnica), art. 11 (Coordinación); NT 2024 §PAC, §Inducción.

---

## Validación Global

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Claridad | Ningún OPD excede 25 entidades (máx: SD1 con 21) | PASS | MEDIA |
| Name coherency | Sin nombres duplicados con significado diferente | PASS | ALTA |
| Implicit objects | Therapeutic Plan, Protocol Set, Sanitary Authorization Status, Training Compliance — todos identificados y modelados explícitamente | PASS | ALTA |
| Emergencia | El sistema produce atención hospitalaria en domicilio — capacidad emergente que ningún componente individual exhibe | PASS | MEDIA |
| Trazabilidad | Cada hecho respaldado por artículo específico de DS 1/2022, DE 31/2024 o NT 2024 | PASS | ALTA |
| Bimodal | Todo OPD tiene párrafo OPL equivalente en EN y ES | PASS | ALTA |
| Structural links homogéneos | Todos obj↔obj (excepción: exhibition-characterization) | PASS | ALTA |
| Agent exclusivamente humano | Todos los agent links conectan a humanos o grupos humanos | PASS | ALTA |
| OPD count | 5 OPDs | PASS | MEDIA |

---

## Resumen de OPDs

| OPD | Tipo | Entidades | Qué dice |
|-----|------|-----------|----------|
| SD | Nivel 0 | 15 | Función principal (hospitalizar) + gobernanza + enablers + ambiente + problem occurrence |
| SD1 | In-zooming seq. | 21 | 5 fases: Evaluar → Ingresar → Planificar → Cuidar → Egresar |
| SD1.1 | In-zooming par. | 14 | 4 modalidades paralelas de cuidado: médica, enfermería, rehabilitación, educación |
| SD1.2 | Unfolding gen-spec. | 12 | 5 tipos de egreso: 1 exitoso (alta médica) + 4 fallas legítimas |
| SD3 | In-zooming par. | 11 | 5 procesos de gobernanza: 3 del Director Técnico + 2 del Coordinador |
| **Total** | **5 OPDs** | **~42 entidades únicas** | **Sistema completo: capa clínica + capa de gobierno** |

---

## Notas Arquitecturales

**N1 — Dos capas del sistema.** El SD exhibe dos procesos: la función principal (*Domiciliary Hospitalizing*) y la gobernanza (*System Governing*). Estas capas operan con agentes distintos (Healthcare Team vs Technical Director), sobre objetos distintos (Patient Group vs Protocol Set), en temporalidades distintas (episódica vs continua). La conexión entre ambas capas es el Protocol Set: los protocolos que el Director Técnico gobierna en SD3 rigen el comportamiento del equipo clínico en SD1.

**N2 — Clinical Condition: split link resuelto.** En SD1, Domiciliary Care Delivering `affects` Clinical Condition (efecto incremental no especificado). Solo Medical Discharging en SD1.2 transiciona de `acute-reacutized` a `recovered`. Los otros 4 tipos de egreso NO producen recuperación. El purpose del SD (Clinical Condition → recovered) es el caso exitoso; los 4 modos de falla son legítimos.

**N3 — Cuidador: triple rol.** El Cuidador es simultáneamente: (a) condition instrument de Eligibility Evaluating (gate de entrada), (b) exhibitor de Caregiver Knowledge (beneficiario de educación), (c) co-productor implícito de cuidados entre visitas (no modelado por falta de evidencia normativa directa). La normativa lo menciona en DS 1/2022 art. 15 (requisito de ingreso) y art. 13 (destinatario de educación) pero no define estándares de competencia verificables.

**N4 — Relación bidireccional con hospital.** Inpatient Facility deriva pacientes al sistema (tagged structural: refers) y el sistema readmits-to Inpatient Facility (tagged structural bidireccional). DS 1/2022 art. 9: "coordinar agudización y requerimiento de reingreso hospitalario." El sistema opera como extensión del hospital con cordón umbilical permanente.

**N5 — Ficha Clínica como spine.** Clinical Record se crea en Patient Admitting, se actualiza en Domiciliary Care Delivering (todos los subprocesos de SD1.1), y se usa como instrumento en Quality and Safety Auditing (SD3). Es el único objeto que atraviesa ambas capas del sistema y todos los niveles de refinamiento.

**N6 — Atención a distancia: base normativa existente.** DS 1/2022 arts. 12-13 habilitan el uso de TICs con "el mismo alcance clínico" para Médico Regulador y Médico de Atención Directa, y para "otros profesionales designados por Dirección Técnica." La normativa habilita una modalidad remota que este modelo no refina, pero que un modelo TO-BE debería incorporar como quinta modalidad de cuidado en SD1.1.

---

_Fecha de elaboración: 2026-04-02_
_Modelo: Mente Omega — OPM Normativo HODOM v1.0_
_Fuentes: exclusivamente DS 1/2022 + DE 31/2024 + NT 2024_
_Restricción: ningún hecho proviene de fuente distinta a las tres normativas_
_Método: ISO/PAS 19450 conforme a skill opm-modeler_
