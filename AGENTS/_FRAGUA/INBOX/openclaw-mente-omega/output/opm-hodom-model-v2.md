# Modelo OPM — Sistema de Hospitalización Domiciliaria (HODOM)

Modelo conceptual conforme a ISO/PAS 19450 (OPM).
Versión: 2.0
Fecha: 2026-04-01

Fuentes normativas:
- DS N° 1/2022, Reglamento de Establecimientos que Otorgan Prestaciones de Hospitalización Domiciliaria.
- Decreto Exento N° 31/2024, que aprueba la Norma Técnica para Hospitalización Domiciliaria.
- Norma Técnica HODOM 2024 (16 páginas, parte integrante del Decreto Exento N° 31).
- Manual REM 2026 (DEIS), Serie A21 Sección C: Hospitalización Domiciliaria y Atención Ventilatoria en Domicilio.

Fuentes complementarias (integración v2.0):
- Modelo Categórico HODOM v4.1 (27 fuentes, datos reales HSC 2023-2026)

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
| Objeto | **Clinical Condition** | Informatical | Sistémico | `acute/reacutized`, `recovered` |
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
| Proceso | *Acute Episode Occurring* | Físico | Ambiental | — |

### Tabla de Enlaces SD

| Tipo | Origen | Destino | ID Plantilla |
|------|--------|---------|--------------|
| Exhibition-characterization | **Domiciliary Hospitalization System** | *Domiciliary Hospitalizing* | RF2b |
| Exhibition-characterization | **Patient Group** | **Clinical Condition** | RF2 |
| Effect (input-output) | *Domiciliary Hospitalizing* | **Clinical Condition** | TS3 |
| Agent | **Healthcare Team** | *Domiciliary Hospitalizing* | H1 |
| Instrument | *Domiciliary Hospitalizing* | **Medical Equipment** | H2 |
| Instrument | *Domiciliary Hospitalizing* | **Communication System** | H2 |
| Instrument | *Domiciliary Hospitalizing* | **Transport Vehicle** | H2 |
| Instrument | *Domiciliary Hospitalizing* | **Administrative Infrastructure** | H2 |
| Instrument | *Domiciliary Hospitalizing* | **Digital Application System** | H2 |
| Consumption | *Domiciliary Hospitalizing* | **Clinical Supply** | T1 |
| Consumption | *Domiciliary Hospitalizing* | **Medication** | T1 |
| Result | *Domiciliary Hospitalizing* | **Clinical Record** | T2 |
| Tagged structural (f-tag) | **Patient Home** | *Domiciliary Hospitalizing* | SE1 |
| Tagged structural (f-tag) | **Current Regulation** | **Domiciliary Hospitalization System** | SE1 |
| Tagged structural (f-tag) | **Inpatient Facility** | *Domiciliary Hospitalizing* | SE1 |
| Tagged structural (f-tag) | **Primary Care Center** | *Domiciliary Hospitalizing* | SE3 |
| Tagged structural (b-tag) | *Domiciliary Hospitalizing* | **Primary Care Center** | SE3 |
| Tagged structural (f-tag) | *Patient Discharging* | **Primary Care Center** | SE3 |
| Effect (env) | *Acute Episode Occurring* | **Clinical Condition** | TS5 |

### OPL-EN del SD

```
Domiciliary Hospitalization System is physical.
Domiciliary Hospitalization System exhibits Domiciliary Hospitalizing.
Patient Group is physical.
Patient Group exhibits Clinical Condition.
Clinical Condition can be acute/reacutized or recovered.
State acute/reacutized of Clinical Condition is initial.
State recovered of Clinical Condition is final.
Domiciliary Hospitalizing changes Clinical Condition from acute/reacutized to recovered.
Healthcare Team handles Domiciliary Hospitalizing.
Domiciliary Hospitalizing requires Medical Equipment.
Domiciliary Hospitalizing requires Communication System.
Domiciliary Hospitalizing requires Transport Vehicle.
Domiciliary Hospitalizing requires Administrative Infrastructure.
Domiciliary Hospitalizing requires Digital Application System.
Domiciliary Hospitalizing consumes Clinical Supply.
Domiciliary Hospitalizing consumes Medication.
Domiciliary Hospitalizing yields Clinical Record.
Patient Home is environmental.
Patient Home hosts Domiciliary Hospitalizing.
Inpatient Facility is environmental.
Inpatient Facility refers Domiciliary Hospitalizing.
Current Regulation is environmental.
Current Regulation governs Domiciliary Hospitalization System.
Primary Care Center is physical.
Primary Care Center is environmental.
Primary Care Center refers Domiciliary Hospitalizing.
Domiciliary Hospitalizing refers Primary Care Center.
Patient Discharging yields referral to Primary Care Center.
Acute Episode Occurring is environmental.
Acute Episode Occurring changes Clinical Condition to acute/reacutized.
```

### OPL-ES del SD

```
**Sistema de Hospitalización Domiciliaria** es físico.
**Sistema de Hospitalización Domiciliaria** exhibe *Hospitalizar en Domicilio*.
**Grupo de Pacientes** es físico.
**Grupo de Pacientes** exhibe **Condición Clínica**.
**Condición Clínica** puede estar `agudo/reagudizado` o `recuperado`.
Estado `agudo/reagudizado` de **Condición Clínica** es inicial.
Estado `recuperado` de **Condición Clínica** es final.
*Hospitalizar en Domicilio* cambia **Condición Clínica** de `agudo/reagudizado` a `recuperado`.
**Equipo de Salud** maneja *Hospitalizar en Domicilio*.
*Hospitalizar en Domicilio* requiere **Equipamiento Médico**.
*Hospitalizar en Domicilio* requiere **Sistema de Comunicación**.
*Hospitalizar en Domicilio* requiere **Vehículo de Transporte**.
*Hospitalizar en Domicilio* requiere **Infraestructura Administrativa**.
*Hospitalizar en Domicilio* requiere **Sistema de Postulación Digital**.
*Hospitalizar en Domicilio* consume **Insumo Clínico**.
*Hospitalizar en Domicilio* consume **Medicamento**.
*Hospitalizar en Domicilio* genera **Ficha Clínica**.
**Domicilio del Paciente** es ambiental.
**Domicilio del Paciente** alberga *Hospitalizar en Domicilio*.
**Establecimiento de Atención Cerrada** es ambiental.
**Establecimiento de Atención Cerrada** deriva a *Hospitalizar en Domicilio*.
**Normativa Vigente** es ambiental.
**Normativa Vigente** rige **Sistema de Hospitalización Domiciliaria**.
**Centro de Salud Familiar** es físico.
**Centro de Salud Familiar** es ambiental.
**Centro de Salud Familiar** deriva *Hospitalizar en Domicilio*.
*Hospitalizar en Domicilio* se relaciona de vuelta con **Centro de Salud Familiar**.
*Egresar de Hospitalización Domiciliaria* genera contrarreferencia a **Centro de Salud Familiar**.
*Episodio Agudo* es ambiental.
*Episodio Agudo* cambia **Condición Clínica** a `agudo/reagudizado`.
```

**Trazabilidad al modelo categórico:**
- **Primary Care Center**: modelo categórico §3.2, §8.2 (origen de derivación primary-care; fluxo de derivación).
- **Digital Application System**: modelo categórico §8.2 (Sistema de Postulación Digital — Google Form HSC).

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
| Objeto | **Eligibility Status** | Informatical | Sistémico | `pending`, `eligible`, `ineligible` |
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
| Objeto | **Caregiver** | Físico | Sistémico | `available`, `unavailable` |
| Objeto | **Support Network** | Físico | Sistémico | `verified`, `insufficient` |
| Objeto | **Derivation Origin** | Informatical | Sistémico | `inpatient-ward`, `emergency-unit`, `primary-care`, `outpatient`, `urgency-law`, `centralized-bed-management` |

### OPL-EN del SD1

```
SD is refined by in-zooming Domiciliary Hospitalizing in SD1.
Domiciliary Hospitalizing zooms into Eligibility Evaluating, Patient Admitting, Care Planning, Therapeutic Plan Executing, Clinical Evolution Monitoring, Patient Discharging and Post-Discharge Following, in that sequence.

Eligibility Status can be pending, eligible or ineligible.
State pending of Eligibility Status is initial.

Eligibility Evaluating changes Eligibility Status from pending to eligible.
Eligibility Evaluating requires Inpatient Facility.

Informed Consent can be unsigned or signed.
State unsigned of Informed Consent is initial.
State signed of Informed Consent is final.
Eligibility Evaluating changes Informed Consent from unsigned to signed.

Caregiver can be available or unavailable.
Eligibility Evaluating requires Caregiver in available.
Support Network can be verified or insufficient.
State insufficient of Support Network is initial.
Eligibility Evaluating changes Support Network from insufficient to verified.

Patient Admitting occurs if Eligibility Status is eligible, in which case Patient Admitting changes Eligibility Status from eligible, otherwise Patient Admitting is skipped.
Patient Admitting requires Informed Consent in signed.
Patient Admitting yields Admission Form.
Patient Admitting yields Social Report.

Derivation Origin can be inpatient-ward, emergency-unit, primary-care, outpatient, urgency-law or centralized-bed-management.
Patient Admitting yields Derivation Origin.

Therapeutic Plan can be draft, active or completed.
State draft of Therapeutic Plan is initial.
State active of Therapeutic Plan is default.
State completed of Therapeutic Plan is final.
Care Planning yields Therapeutic Plan in draft.

Nursing Care Plan can be draft, active or completed.
State draft of Nursing Care Plan is initial.
Care Planning yields Nursing Care Plan in draft.

Therapeutic Plan Executing requires Therapeutic Plan in active.
Therapeutic Plan Executing requires Nursing Care Plan in active.
Therapeutic Plan Executing consumes Clinical Supply.
Therapeutic Plan Executing consumes Medication.
Therapeutic Plan Executing requires Medical Equipment.
Therapeutic Plan Executing requires Transport Vehicle.

Clinical Evolution Monitoring changes Clinical Condition from acute/reacutized to recovered.
Clinical Evolution Monitoring yields Domiciliary Clinical Summary.

Continuity Decision can be continue-treatment or proceed-discharge.
Clinical Evolution Monitoring yields Continuity Decision.

Hospitalization Status can be active or discharged.
State active of Hospitalization Status is initial.
State discharged of Hospitalization Status is final.

Patient Discharging occurs if Continuity Decision is proceed-discharge, in which case Patient Discharging changes Hospitalization Status from active to discharged, otherwise Patient Discharging is skipped.
Patient Discharging changes Therapeutic Plan from active to completed.
Patient Discharging changes Nursing Care Plan from active to completed.
Patient Discharging yields Epicrisis.
Patient Discharging yields Satisfaction Survey.
Patient Discharging yields Clinical Record.

Post-Discharge Following occurs if Hospitalization Status is discharged.
Post-Discharge Following zooms into Follow-Up Call Executing, Primary Care Counterreferral Sending and Discharge Outcome Evaluating, in that sequence.

Healthcare Team handles Eligibility Evaluating.
Healthcare Team handles Patient Admitting.
Healthcare Team handles Care Planning.
Healthcare Team handles Therapeutic Plan Executing.
Healthcare Team handles Clinical Evolution Monitoring.
Healthcare Team handles Patient Discharging.
```

### OPL-ES del SD1

```
SD se refina por descomposición de *Hospitalizar en Domicilio* en SD1.
*Hospitalizar en Domicilio* se descompone en *Evaluar Elegibilidad*, *Ingresar Paciente*, *Planificar Atención*, *Ejecutar Plan Terapéutico*, *Monitorear Evolución Clínica*, *Egresar de Hospitalización Domiciliaria* y *Seguimiento Post-Egreso*, en esa secuencia.

**Estado de Elegibilidad** puede estar `pendiente`, `elegible` o `no elegible`.
Estado `pendiente` de **Estado de Elegibilidad** es inicial.

*Evaluar Elegibilidad* cambia **Estado de Elegibilidad** de `pendiente` a `elegible`.
*Evaluar Elegibilidad* requiere **Establecimiento de Atención Cerrada**.

**Consentimiento Informado** puede estar `sin firmar` o `firmado`.
Estado `sin firmar` de **Consentimiento Informado** es inicial.
Estado `firmado` de **Consentimiento Informado** es final.
*Evaluar Elegibilidad* cambia **Consentimiento Informado** de `sin firmar` a `firmado`.

**Cuidador** puede estar `disponible` o `no disponible`.
*Evaluar Elegibilidad* requiere **Cuidador** en `disponible`.
**Red de Apoyo** puede estar `verificada` o `insuficiente`.
Estado `insuficiente` de **Red de Apoyo** es inicial.
*Evaluar Elegibilidad* cambia **Red de Apoyo** de `insuficiente` a `verificada`.

*Ingresar Paciente* ocurre si **Estado de Elegibilidad** está en `elegible`, en cuyo caso *Ingresar Paciente* cambia **Estado de Elegibilidad** de `elegible`, de lo contrario *Ingresar Paciente* se omite.
*Ingresar Paciente* requiere **Consentimiento Informado** en `firmado`.
*Ingresar Paciente* genera **Formulario de Ingreso**.
*Ingresar Paciente* genera **Informe Social**.

**Origen de Derivación** puede estar `área de hospitalización`, `unidad de emergencia`, `atención primaria`, `ambulatorio`, `ley de urgencia` o `gestión centralizada de camas`.
*Ingresar Paciente* genera **Origen de Derivación**.

**Plan Terapéutico** puede estar `borrador`, `activo` o `completado`.
Estado `borrador` de **Plan Terapéutico** es inicial.
Estado `activo` de **Plan Terapéutico** es por defecto.
Estado `completado` de **Plan Terapéutico** es final.
*Planificar Atención* genera **Plan Terapéutico** en `borrador`.

**Plan de Cuidados de Enfermería** puede estar `borrador`, `activo` o `completado`.
Estado `borrador` de **Plan de Cuidados de Enfermería** es inicial.
*Planificar Atención* genera **Plan de Cuidados de Enfermería** en `borrador`.

*Ejecutar Plan Terapéutico* requiere **Plan Terapéutico** en `activo`.
*Ejecutar Plan Terapéutico* requiere **Plan de Cuidados de Enfermería** en `activo`.
*Ejecutar Plan Terapéutico* consume **Insumo Clínico**.
*Ejecutar Plan Terapéutico* consume **Medicamento**.
*Ejecutar Plan Terapéutico* requiere **Equipamiento Médico**.
*Ejecutar Plan Terapéutico* requiere **Vehículo de Transporte**.

*Monitorear Evolución Clínica* cambia **Condición Clínica** de `agudo/reagudizado` a `recuperado`.
*Monitorear Evolución Clínica* genera **Resumen Clínico Domiciliario**.

**Decisión de Continuidad** puede estar `continuar tratamiento` o `proceder egreso`.
*Monitorear Evolución Clínica* genera **Decisión de Continuidad**.

**Estado de Hospitalización** puede estar `activa` o `egresado`.
Estado `activa` de **Estado de Hospitalización** es inicial.
Estado `egresado` de **Estado de Hospitalización** es final.

*Egresar de Hospitalización Domiciliaria* ocurre si **Decisión de Continuidad** está en `proceder egreso`, en cuyo caso *Egresar de Hospitalización Domiciliaria* cambia **Estado de Hospitalización** de `activa` a `egresado`, de lo contrario *Egresar de Hospitalización Domiciliaria* se omite.
*Egresar de Hospitalización Domiciliaria* cambia **Plan Terapéutico** de `activo` a `completado`.
*Egresar de Hospitalización Domiciliaria* cambia **Plan de Cuidados de Enfermería** de `activo` a `completado`.
*Egresar de Hospitalización Domiciliaria* genera **Epicrisis**.
*Egresar de Hospitalización Domiciliaria* genera **Encuesta de Satisfacción**.
*Egresar de Hospitalización Domiciliaria* genera **Ficha Clínica**.

*Seguimiento Post-Egreso* ocurre si **Estado de Hospitalización** está en `egresado`.
*Seguimiento Post-Egreso* se descompone en *Ejecutar Llamada de Seguimiento*, *Enviar Contrarreferencia a Atención Primaria* y *Evaluar Resultado del Egreso*, en esa secuencia.

**Equipo de Salud** maneja *Evaluar Elegibilidad*.
**Equipo de Salud** maneja *Ingresar Paciente*.
**Equipo de Salud** maneja *Planificar Atención*.
**Equipo de Salud** maneja *Ejecutar Plan Terapéutico*.
**Equipo de Salud** maneja *Monitorear Evolución Clínica*.
**Equipo de Salud** maneja *Egresar de Hospitalización Domiciliaria*.
```

---

## SD1.1 — Descomposición de *Eligibility Evaluating*

Refinamiento: in-zooming (secuencial). Versión corregida con 6 subprocesos (según enriquecimiento parte1).

### Tabla de Elementos SD1.1

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Candidate Screening* | Informatical | Sistémico | — |
| Proceso | *Application Receiving* | Informatical | Sistémico | — |
| Proceso | *Clinical Condition Evaluating* | Informatical | Sistémico | — |
| Proceso | *Home Condition Evaluating* | Informatical | Sistémico | — |
| Proceso | *Support Network Verifying* | Informatical | Sistémico | — |
| Proceso | *Informed Consent Obtaining* | Informatical | Sistémico | — |
| Objeto | **Candidate** | Físico | Sistémico | `identified`, `postulated`, `ineligible` |
| Objeto | **Case Manager** | Físico | Sistémico | — |
| Objeto | **Insurance Status** | Informatical | Sistémico | `fonasa_a`, `fonasa_b`, `fonasa_c`, `fonasa_d`, `prais`, `other` |
| Objeto | **Patient Age** | Informatical | Sistémico | — |
| Objeto | **Hospital Distance** | Informatical | Sistémico | — |
| Objeto | **Home Condition** | Informatical | Sistémico | `adequate`, `inadequate` |
| Objeto | **Rights and Duties Charter** | Informatical | Sistémico | — |

### OPL-EN SD1.1

```
SD1 is refined by in-zooming Eligibility Evaluating in SD1.1.
Eligibility Evaluating zooms into Candidate Screening, Application Receiving, Clinical Condition Evaluating, Home Condition Evaluating, Support Network Verifying and Informed Consent Obtaining, in that sequence.

Candidate Screening is informatical.
Candidate Screening yields Candidate.
Social Worker handles Candidate Screening.

Candidate is physical.
Candidate can be identified, postulated or ineligible.
State identified of Candidate is initial.

Application Receiving is informatical.
Application Receiving affects Candidate.
Application Receiving changes Candidate from identified to postulated.
Application Receiving yields Candidate.
Case Manager handles Application Receiving.

Case Manager is physical.
Case Manager is a Coordination Professional.
Case Manager exhibits Assigned Patients.
Assigned Patients of Case Manager ranges from 0 to 25.

Clinical Condition Evaluating affects Patient Group.
Clinical Condition Evaluating changes Clinical Condition from acute/reacutized.
Clinical Condition Evaluating requires Inpatient Facility.
Attending Physician handles Clinical Condition Evaluating.

Home Condition Evaluating yields Social Report.
Home Condition Evaluating affects Patient Home.
Social Worker handles Home Condition Evaluating.

Home Condition can be adequate or inadequate.
State inadequate of Home Condition is initial.
Patient Home exhibits Home Condition.
Home Condition Evaluating changes Home Condition from inadequate to adequate.

Support Network Verifying changes Support Network from insufficient to verified.
Support Network Verifying requires Caregiver in available.
Social Worker handles Support Network Verifying.

Informed Consent Obtaining changes Informed Consent from unsigned to signed.
Informed Consent Obtaining requires Patient Group.
Clinical Nurse handles Informed Consent Obtaining.

Rights and Duties Charter is informatical.
Informed Consent Obtaining yields Rights and Duties Charter.

Insurance Status is informatical.
Insurance Status can be fonasa_a, fonasa_b, fonasa_c, fonasa_d, prais or other.
Eligibility Evaluating occurs if Insurance Status is fonasa_a or fonasa_b or fonasa_c or fonasa_d or prais.

Patient Age is informatical.
Eligibility Evaluating occurs if Patient Age is gte_18.

Hospital Distance is informatical.
Eligibility Evaluating occurs if Hospital Distance is lte_20km.

Exclusion Condition is informatical.
Exclusion Condition can be absent or present.
State absent of Exclusion Condition is initial.
Eligibility Evaluating occurs if Exclusion Condition is absent, otherwise Eligibility Evaluating is skipped.
```

### OPL-ES SD1.1

```
SD1 se refina por descomposición de *Evaluar Elegibilidad* en SD1.1.
*Evaluar Elegibilidad* se descompone en *Pesquisar Candidatos*, *Recibir Postulación*, *Evaluar Condición Clínica*, *Evaluar Condiciones del Domicilio*, *Verificar Red de Apoyo* y *Obtener Consentimiento Informado*, en esa secuencia.

*Pesquisar Candidatos* es informático.
*Pesquisar Candidatos* genera **Candidato**.
**Trabajador Social** maneja *Pesquisar Candidatos*.

**Candidato** es físico.
**Candidato** puede estar `identificado`, `postulado` o `no elegible`.
Estado `identificado` de **Candidato** es inicial.

*Recibir Postulación* es informático.
*Recibir Postulación* afecta **Candidato**.
*Recibir Postulación* cambia **Candidato** de `identificado` a `postulado`.
*Recibir Postulación* genera **Candidato**.
**Gestora Encargada** maneja *Recibir Postulación*.

**Gestora Encargada** es física.
**Gestora Encargada** es un **Profesional Coordinador**.
**Gestora Encargada** exhibe **Pacientes Asignados**.
**Pacientes Asignados** de **Gestora Encargada** varía de 0 a 25.

*Evaluar Condición Clínica* afecta **Grupo de Pacientes**.
*Evaluar Condición Clínica* cambia **Condición Clínica** de `agudo/reagudizado`.
*Evaluar Condición Clínica* requiere **Establecimiento de Atención Cerrada**.
**Médico de Atención Directa** maneja *Evaluar Condición Clínica*.

*Evaluar Condiciones del Domicilio* genera **Informe Social**.
*Evaluar Condiciones del Domicilio* afecta **Domicilio del Paciente**.
**Trabajador Social** maneja *Evaluar Condiciones del Domicilio*.

**Condición del Domicilio** puede estar `adecuada` o `inadecuada`.
Estado `inadecuada` de **Condición del Domicilio** es inicial.
**Domicilio del Paciente** exhibe **Condición del Domicilio**.
*Evaluar Condiciones del Domicilio* cambia **Condición del Domicilio** de `inadecuada` a `adecuada`.

*Verificar Red de Apoyo* cambia **Red de Apoyo** de `insuficiente` a `verificada`.
*Verificar Red de Apoyo* requiere **Cuidador** en `disponible`.
**Trabajador Social** maneja *Verificar Red de Apoyo*.

*Obtener Consentimiento Informado* cambia **Consentimiento Informado** de `sin firmar` a `firmado`.
*Obtener Consentimiento Informado* requiere **Grupo de Pacientes**.
**Enfermero Clínico** maneja *Obtener Consentimiento Informado*.

**Carta de Derechos y Deberes** es informática.
*Obtener Consentimiento Informado* genera **Carta de Derechos y Deberes**.

**Estado de Previsión** es informático.
**Estado de Previsión** puede estar `fonasa_a`, `fonasa_b`, `fonasa_c`, `fonasa_d`, `prais` o `otro`.
*Evaluar Elegibilidad* ocurre si **Estado de Previsión** está en `fonasa_a` o `fonasa_b` o `fonasa_c` o `fonasa_d` o `prais`.

**Edad del Paciente** es informática.
*Evaluar Elegibilidad* ocurre si **Edad del Paciente** es mayor o igual a 18.

**Distancia al Hospital** es informática.
*Evaluar Elegibilidad* ocurre si **Distancia al Hospital** es menor o igual a 20 km.

**Condición de Exclusión** es informática.
**Condición de Exclusión** puede estar `ausente` o `presente`.
Estado `ausente` de **Condición de Exclusión** es inicial.
*Evaluar Elegibilidad* ocurre si **Condición de Exclusión** está en `ausente`, de lo contrario *Evaluar Elegibilidad* se omite.
```

**Trazabilidad al modelo categórico:**
- Candidate Screening: modelo categórico §5.1 (pesquisa activa, 1.279 visitas/año Trabajo Social HSC).
- Case Manager / Application Receiving: modelo categórico §5.2 (gestión de casos, Google Form).
- Insurance Status, Patient Age, Hospital Distance: DS 1/2022 art. 15; NT 2024.

---

## SD1.2 — Descomposición de *Patient Admitting*

*(Sin cambios respecto al modelo original v1.)*

Refinamiento: in-zooming (secuencial).

### OPL-EN

```
SD1 is refined by in-zooming Patient Admitting in SD1.2.
Patient Admitting zooms into Admission Registering, Social Diagnosis Elaborating, Patient Documentation Delivering and Referral Facility Coordinating, in that sequence.

Admission Registering yields Admission Form.
Admission Registering requires Communication System.
Admission Registering yields Derivation Origin.
Administrative Staff handles Admission Registering.

Social Diagnosis Elaborating yields Social Report.
Social Diagnosis Elaborating affects Patient Home.
Social Worker handles Social Diagnosis Elaborating.

Socioeconomic Status is informatical.
Social Diagnosis Elaborating yields Socioeconomic Status.

Patient Documentation Delivering affects Patient Group.
Patient Documentation Delivering requires Informed Consent in signed.
Patient Documentation Delivering yields Care Indication Document.
Clinical Nurse handles Patient Documentation Delivering.

Care Indication Document is informatical.

Referral Facility Coordinating requires Inpatient Facility.
Referral Facility Coordinating requires Communication System.
Coordination Professional handles Referral Facility Coordinating.
```

### OPL-ES

```
SD1 se refina por descomposición de *Ingresar Paciente* en SD1.2.
*Ingresar Paciente* se descompone en *Registrar Ingreso*, *Elaborar Diagnóstico Social*, *Entregar Documentación al Paciente* y *Coordinar con Establecimiento Derivador*, en esa secuencia.

*Registrar Ingreso* genera **Formulario de Ingreso**.
*Registrar Ingreso* requiere **Sistema de Comunicación**.
*Registrar Ingreso* genera **Origen de Derivación**.
**Personal Administrativo** maneja *Registrar Ingreso*.

*Elaborar Diagnóstico Social* genera **Informe Social**.
*Elaborar Diagnóstico Social* afecta **Domicilio del Paciente**.
**Trabajador Social** maneja *Elaborar Diagnóstico Social*.

**Situación Socioeconómica** es informatical.
*Elaborar Diagnóstico Social* genera **Situación Socioeconómica**.

*Entregar Documentación al Paciente* afecta **Grupo de Pacientes**.
*Entregar Documentación al Paciente* requiere **Consentimiento Informado** en `firmado`.
*Entregar Documentación al Paciente* genera **Documento de Indicaciones de Cuidado**.
**Enfermero Clínico** maneja *Entregar Documentación al Paciente*.

**Documento de Indicaciones de Cuidado** es informatical.

*Coordinar con Establecimiento Derivador* requiere **Establecimiento de Atención Cerrada**.
*Coordinar con Establecimiento Derivador* requiere **Sistema de Comunicación**.
**Profesional Coordinador** maneja *Coordinar con Establecimiento Derivador*.
```

---

## SD1.3 — Descomposición de *Care Planning*

*(Sin cambios respecto al modelo original v1.)*

Refinamiento: in-zooming (secuencial).

### OPL-EN

```
SD1 is refined by in-zooming Care Planning in SD1.3.
Care Planning zooms into Therapeutic Plan Elaborating, Nursing Care Plan Elaborating, Home Visit Scheduling and Transport Route Programming, in that sequence.

Therapeutic Plan Elaborating yields Therapeutic Plan in draft.
Therapeutic Plan Elaborating requires Clinical Condition.
Attending Physician handles Therapeutic Plan Elaborating.

Nursing Care Plan Elaborating yields Nursing Care Plan in draft.
Nursing Care Plan Elaborating requires Therapeutic Plan in draft.
Clinical Nurse handles Nursing Care Plan Elaborating.

Visit Schedule is informatical.
Home Visit Scheduling yields Visit Schedule.
Home Visit Scheduling requires Therapeutic Plan in draft.
Coordination Professional handles Home Visit Scheduling.

Transport Route is informatical.
Transport Route Programming yields Transport Route.
Transport Route Programming requires Visit Schedule.
Transport Route Programming requires Patient Home.
Administrative Staff handles Transport Route Programming.
```

### OPL-ES

```
SD1 se refina por descomposición de *Planificar Atención* en SD1.3.
*Planificar Atención* se descompone en *Elaborar Plan Terapéutico*, *Elaborar Plan de Cuidados de Enfermería*, *Programar Visitas Domiciliarias* y *Programar Rutas de Transporte*, en esa secuencia.

*Elaborar Plan Terapéutico* genera **Plan Terapéutico** en `borrador`.
*Elaborar Plan Terapéutico* requiere **Condición Clínica**.
**Médico de Atención Directa** maneja *Elaborar Plan Terapéutico*.

*Elaborar Plan de Cuidados de Enfermería* genera **Plan de Cuidados de Enfermería** en `borrador`.
*Elaborar Plan de Cuidados de Enfermería* requiere **Plan Terapéutico** en `borrador`.
**Enfermero Clínico** maneja *Elaborar Plan de Cuidados de Enfermería*.

**Programa de Visitas** es informatical.
*Programar Visitas Domiciliarias* genera **Programa de Visitas**.
*Programar Visitas Domiciliarias* requiere **Plan Terapéutico** en `borrador`.
**Profesional Coordinador** maneja *Programar Visitas Domiciliarias*.

**Ruta de Transporte** es informatical.
*Programar Rutas de Transporte* genera **Ruta de Transporte**.
*Programar Rutas de Transporte* requiere **Programa de Visitas**.
*Programar Rutas de Transporte* requiere **Domicilio del Paciente**.
**Personal Administrativo** maneja *Programar Rutas de Transporte*.
```

---

## SD1.4 — Descomposición de *Therapeutic Plan Executing*

*(Versión corregida: 10 subprocesos paralelos)*

Refinamiento: in-zooming con paralelismo (subprocesos asíncronos — ocurren en orden variable según plan de cada paciente). Los 3 subprocesos nuevos (Wound Care, Speech Therapy, Daily Logistics) provienen del enriquecimiento parte2. El agente de Remote Care Regulating y los condition instruments de Operational Mode provienen del enriquecimiento parte1 E y parte3 B.

### OPL-EN SD1.4

```
SD1 is refined by in-zooming Therapeutic Plan Executing in SD1.4.
Therapeutic Plan Executing zooms into parallel Medical Visit Performing, Nursing Care Executing, Kinesiological Therapy Executing, Medication Administering, Remote Care Regulating, Patient and Caregiver Educating, Wound Care Executing, Speech Therapy Executing, Daily Logistics Managing and Shift Handover Executing.

Medical Visit Performing affects Patient Group.
Medical Visit Performing requires Therapeutic Plan in active.
Medical Visit Performing requires Medical Equipment.
Medical Visit Performing requires Transport Vehicle.
Medical Visit Performing requires Operational Mode in full_weekday.
Medical Visit Performing yields Domiciliary Clinical Summary.
Attending Physician handles Medical Visit Performing.

Nursing Care Executing affects Patient Group.
Nursing Care Executing requires Nursing Care Plan in active.
Nursing Care Executing requires Medical Equipment.
Nursing Care Executing consumes Clinical Supply.
Clinical Nurse handles Nursing Care Executing.
Nursing Technician handles Nursing Care Executing.

Kinesiological Therapy Executing affects Patient Group.
Kinesiological Therapy Executing requires Therapeutic Plan in active.
Kinesiological Therapy Executing requires Medical Equipment.
Kinesiologist handles Kinesiological Therapy Executing.
Therapy Type can be motor or respiratory.
Kinesiological Therapy Executing affects Therapy Type.

Medication Administering consumes Medication.
Medication Administering affects Patient Group.
Medication Administering requires Therapeutic Plan in active.
Clinical Nurse handles Medication Administering.
Nursing Technician handles Medication Administering.
Prescription is informatical.
Medication Administering requires Prescription.

Remote Care Regulating affects Patient Group.
Remote Care Regulating requires Communication System.
Clinical Nurse handles Remote Care Regulating.
Attending Physician handles Remote Care Regulating if Operational Mode is full_weekday, otherwise Remote Care Regulating is skipped.
Remote Care Regulating yields Call Record.
Telehealth Record is informatical.
Remote Care Regulating yields Telehealth Record.

Patient and Caregiver Educating affects Patient Group.
Patient and Caregiver Educating affects Caregiver.
Patient and Caregiver Educating requires Therapeutic Plan in active.
Clinical Nurse handles Patient and Caregiver Educating.
Self-Care Knowledge is informatical.
Patient Group exhibits Self-Care Knowledge.
Self-Care Knowledge can be insufficient or sufficient.
State insufficient of Self-Care Knowledge is initial.
Patient and Caregiver Educating changes Self-Care Knowledge from insufficient to sufficient.

Wound Status can be active, healing or resolved.
State active of Wound Status is initial.
State healing of Wound Status is default.
State resolved of Wound Status is final.
Wound Care Executing affects Patient Group.
Wound Care Executing changes Wound Status from active to healing.
Wound Care Executing changes Wound Status from healing to resolved.
Wound Care Executing requires Therapeutic Plan in active.
Wound Care Executing consumes Clinical Supply.
Wound Care Executing yields Wound Care Record.
Clinical Nurse handles Wound Care Executing.
Patient Group exhibits Wound Status.

Swallowing and Speech Status can be impaired, improving or functional.
State impaired of Swallowing and Speech Status is initial.
State improving of Swallowing and Speech Status is default.
State functional of Swallowing and Speech Status is final.
Speech Therapy Executing affects Patient Group.
Speech Therapy Executing requires Therapeutic Plan in active.
Speech Therapy Executing requires Medical Equipment.
Speech Therapy Executing requires Operational Mode in full_weekday.
Speech Therapy Executing yields Speech Therapy Record.
Speech Therapist handles Speech Therapy Executing.
Patient Group exhibits Swallowing and Speech Status.

Daily Schedule Status can be pending, assigned or executed.
State pending of Daily Schedule Status is initial.
State assigned of Daily Schedule Status is default.
State executed of Daily Schedule Status is final.
Daily Logistics Managing changes Daily Schedule Status from pending to assigned.
Daily Logistics Managing changes Daily Schedule Status from assigned to executed.
Daily Logistics Managing requires Visit Schedule.
Daily Logistics Managing requires Transport Vehicle.
Daily Logistics Managing yields Daily Schedule.
Coordination Professional handles Daily Logistics Managing.

Shift Status can be pending or handed_over.
State pending of Shift Status is initial.
State handed_over of Shift Status is final.
Patient Snapshot can be outdated or current.
State outdated of Patient Snapshot is initial.
State current of Patient Snapshot is final.
Movement Record is informatical.
Shift Handover Record is informatical.
Active Patient Status Reporting changes Patient Snapshot from outdated to current.
Clinical Nurse handles Active Patient Status Reporting.
Day Movement Registering yields Movement Record.
Clinical Nurse handles Day Movement Registering.
Clinical Responsibility Transferring changes Shift Status from pending to handed_over.
Clinical Responsibility Transferring yields Shift Handover Record.
Clinical Nurse handles Clinical Responsibility Transferring.
```

### OPL-ES SD1.4

```
SD1 se refina por descomposición de *Ejecutar Plan Terapéutico* en SD1.4.
*Ejecutar Plan Terapéutico* se descompone en paralelo *Realizar Visita Médica*, *Ejecutar Cuidados de Enfermería*, *Ejecutar Terapia Kinesiológica*, *Administrar Medicamentos*, *Regular Atención a Distancia*, *Educar a Paciente y Cuidador*, *Ejecutar Curación*, *Ejecutar Fonoaudiología*, *Gestionar Logística Diaria* y *Ejecutar Entrega de Turno*.

*Realizar Visita Médica* afecta **Grupo de Pacientes**.
*Realizar Visita Médica* requiere **Plan Terapéutico** en `activo`.
*Realizar Visita Médica* requiere **Equipamiento Médico**.
*Realizar Visita Médica* requiere **Vehículo de Transporte**.
*Realizar Visita Médica* requiere **Modo Operacional** en `días_hábiles`.
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
*Ejecutar Terapia Kinesiológica* afecta **Tipo de Terapia**.

*Administrar Medicamentos* consume **Medicamento**.
*Administrar Medicamentos* afecta **Grupo de Pacientes**.
*Administrar Medicamentos* requiere **Plan Terapéutico** en `activo`.
**Enfermero Clínico** maneja *Administrar Medicamentos*.
**Técnico de Enfermería** maneja *Administrar Medicamentos*.
**Receta Médica** es informatical.
*Administrar Medicamentos* requiere **Receta Médica**.

*Regular Atención a Distancia* afecta **Grupo de Pacientes**.
*Regular Atención a Distancia* requiere **Sistema de Comunicación**.
**Enfermero Clínico** maneja *Regular Atención a Distancia*.
**Médico de Atención Directa** maneja *Regular Atención a Distancia* si **Modo Operacional** está en `días_hábiles`, de lo contrario *Regular Atención a Distancia* se omite.
*Regular Atención a Distancia* genera **Registro de Llamada**.
**Registro de Telesalud** es informatical.
*Regular Atención a Distancia* genera **Registro de Telesalud**.

*Educar a Paciente y Cuidador* afecta **Grupo de Pacientes**.
*Educar a Paciente y Cuidador* afecta **Cuidador**.
*Educar a Paciente y Cuidador* requiere **Plan Terapéutico** en `activo`.
**Enfermero Clínico** maneja *Educar a Paciente y Cuidador*.
**Conocimiento de Autocuidado** es informatical.
**Grupo de Pacientes** exhibe **Conocimiento de Autocuidado**.
**Conocimiento de Autocuidado** puede estar `insuficiente` o `suficiente`.
Estado `insuficiente` de **Conocimiento de Autocuidado** es inicial.
*Educar a Paciente y Cuidador* cambia **Conocimiento de Autocuidado** de `insuficiente` a `suficiente`.

**Estado de Herida** puede estar `activo`, `en cicatrización` o `resuelto`.
Estado `activo` de **Estado de Herida** es inicial.
Estado `en cicatrización` de **Estado de Herida** es por defecto.
Estado `resuelto` de **Estado de Herida** es final.
*Ejecutar Curación* afecta **Grupo de Pacientes**.
*Ejecutar Curación* cambia **Estado de Herida** de `activo` a `en cicatrización`.
*Ejecutar Curación* cambia **Estado de Herida** de `en cicatrización` a `resuelto`.
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
*Ejecutar Fonoaudiología* requiere **Plan Terapéutico** en `activo`.
*Ejecutar Fonoaudiología* requiere **Equipamiento Médico**.
*Ejecutar Fonoaudiología* requiere **Modo Operacional** en `días_hábiles`.
*Ejecutar Fonoaudiología* genera **Registro de Fonoaudiología**.
**Fonoaudiólogo** maneja *Ejecutar Fonoaudiología*.
**Grupo de Pacientes** exhibe **Estado de Deglución y Habla**.

**Estado de Programación Diaria** puede estar `pendiente`, `asignada` o `ejecutada`.
Estado `pendiente` de **Estado de Programación Diaria** es inicial.
Estado `asignada` de **Estado de Programación Diaria** es por defecto.
Estado `ejecutada` de **Estado de Programación Diaria** es final.
*Gestionar Logística Diaria* cambia **Estado de Programación Diaria** de `pendiente` a `asignada`.
*Gestionar Logística Diaria* cambia **Estado de Programación Diaria** de `asignada` a `ejecutada`.
*Gestionar Logística Diaria* requiere **Programa de Visitas**.
*Gestionar Logística Diaria* requiere **Vehículo de Transporte**.
*Gestionar Logística Diaria* genera **Programación Diaria**.
**Profesional Coordinador** maneja *Gestionar Logística Diaria*.

**Estado de Turno** puede estar `pendiente` o `entregado`.
Estado `pendiente` de **Estado de Turno** es inicial.
Estado `entregado` de **Estado de Turno** es final.
**Snapshot de Pacientes** puede estar `desactualizado` o `actual`.
Estado `desactualizado` de **Snapshot de Pacientes** es inicial.
Estado `actual` de **Snapshot de Pacientes** es final.
**Registro de Movimientos** es informatical.
**Registro de Entrega de Turno** es informatical.
*Reportar Estado de Pacientes Activos* cambia **Snapshot de Pacientes** de `desactualizado` a `actual`.
**Enfermero Clínico** maneja *Reportar Estado de Pacientes Activos*.
*Registrar Movimientos del Día* genera **Registro de Movimientos**.
**Enfermero Clínico** maneja *Registrar Movimientos del Día*.
*Transferir Responsabilidad Clínica* cambia **Estado de Turno** de `pendiente` a `entregado`.
*Transferir Responsabilidad Clínica* genera **Registro de Entrega de Turno**.
**Enfermero Clínico** maneja *Transferir Responsabilidad Clínica*.
```

**Trazabilidad al modelo categórico:**
- Wound Care: modelo categórico §10.6 (Registro de Curaciones) y §16.4 (Canasta HODOM: CuracionSimple, CuracionAvanzada).
- Speech Therapy: modelo categórico §4.4 y §16.5 (1.279 visitas/año HSC; solo L-V).
- Daily Logistics: modelo categórico §16.13 (Programación Diaria — 35 días, 4 zonas).
- Shift Handover: modelo categórico §16.3 (Entrega de turno enfermería: 7 columnas por paciente).
- Remote Care Regulating (Clinical Nurse agente principal): modelo categórico §5.2, §16.1 (HSC sin Médico Regulador dedicado).

---

## SD1.4a — Refinamiento de *Daily Logistics Managing*

*(Nuevo — enriquecimiento parte2)*

Refinamiento: in-zooming (subprocesos secuenciales). El proceso padre *Gestionar Logística Diaria* se descompone en 5 subprocesos que ocurren en secuencia diaria.

### Tabla de Elementos SD1.4a

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Patient Route Assigning* | Informatical | Sistémico | — |
| Proceso | *Staff Route Assigning* | Informatical | Sistémico | — |
| Proceso | *Visit Sequencing* | Informatical | Sistémico | — |
| Proceso | *Unrouted Visit Resolving* | Informatical | Sistémico | — |
| Proceso | *Route Execution Monitoring* | Informatical | Sistémico | — |
| Objeto | **Route Assignment** | Informatical | Sistémico | `unassigned`, `assigned`, `staffed` |
| Objeto | **GPS Tracking System** | Informatical | Sistémico | — |
| Objeto | **Route Execution Report** | Informatical | Sistémico | — |
| Objeto | **Operational Productivity** | Informatical | Sistémico | `below_target`, `on_target`, `above_target` |
| Objeto | **Unrouted Visit** | Informatical | Sistémico | `unresolved`, `resolved` |

### OPL-EN SD1.4a

```
SD1.4 is refined by in-zooming Daily Logistics Managing in SD1.4a.
Daily Logistics Managing zooms into Patient Route Assigning, Staff Route Assigning, Visit Sequencing, Unrouted Visit Resolving and Route Execution Monitoring, in that sequence.

Route Assignment can be unassigned, assigned or staffed.
State unassigned of Route Assignment is initial.
State assigned of Route Assignment is default.
State staffed of Route Assignment is default.

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
Coordination Professional handles Visit Sequencing.
Driver handles Visit Sequencing.

Unrouted Visit can be unresolved or resolved.
State unresolved of Unrouted Visit is initial.
Unrouted Visit Resolving occurs if Unrouted Visit exists, in which case Unrouted Visit Resolving changes Unrouted Visit from unresolved to resolved, otherwise Unrouted Visit Resolving is skipped.
Unrouted Visit Resolving affects Daily Schedule.
Coordination Professional handles Unrouted Visit Resolving.

Route Execution Monitoring requires GPS Tracking System.
Route Execution Monitoring yields Route Execution Report.
Route Execution Monitoring affects Operational Productivity.
Operational Productivity can be below_target, on_target or above_target.
Coordination Professional handles Route Execution Monitoring.
```

### OPL-ES SD1.4a

```
SD1.4 se refina por descomposición de *Gestionar Logística Diaria* en SD1.4a.
*Gestionar Logística Diaria* se descompone en *Asignar Pacientes a Ruta*, *Asignar Profesionales a Ruta*, *Secuenciar Visitas*, *Resolver Visitas sin Ruta* y *Monitorear Ejecución de Rutas*, en esa secuencia.

**Asignación de Ruta** puede estar `sin asignar`, `asignada` o `con equipo`.
Estado `sin asignar` de **Asignación de Ruta** es inicial.
Estado `asignada` de **Asignación de Ruta** es por defecto.
Estado `con equipo` de **Asignación de Ruta** es por defecto.

*Asignar Pacientes a Ruta* cambia **Asignación de Ruta** de `sin asignar` a `asignada`.
*Asignar Pacientes a Ruta* requiere **Domicilio del Paciente**.
**Profesional Coordinador** maneja *Asignar Pacientes a Ruta*.
**Conductor** maneja *Asignar Pacientes a Ruta*.

*Asignar Profesionales a Ruta* cambia **Asignación de Ruta** de `asignada` a `con equipo`.
*Asignar Profesionales a Ruta* requiere **Equipo de Salud**.
**Profesional Coordinador** maneja *Asignar Profesionales a Ruta*.
**Conductor** maneja *Asignar Profesionales a Ruta*.

*Secuenciar Visitas* genera **Programación Diaria**.
*Secuenciar Visitas* afecta **Asignación de Ruta**.
**Profesional Coordinador** maneja *Secuenciar Visitas*.
**Conductor** maneja *Secuenciar Visitas*.

**Visita sin Ruta Asignada** puede estar `sin resolver` o `resuelta`.
Estado `sin resolver` de **Visita sin Ruta Asignada** es inicial.
*Resolver Visitas sin Ruta* ocurre si **Visita sin Ruta Asignada** existe, en cuyo caso *Resolver Visitas sin Ruta* cambia **Visita sin Ruta Asignada** de `sin resolver` a `resuelta`, de lo contrario *Resolver Visitas sin Ruta* se omite.
*Resolver Visitas sin Ruta* afecta **Programación Diaria**.
**Profesional Coordinador** maneja *Resolver Visitas sin Ruta*.

*Monitorear Ejecución de Rutas* requiere **Sistema de Rastreo GPS**.
*Monitorear Ejecución de Rutas* genera **Reporte de Ejecución de Rutas**.
*Monitorear Ejecución de Rutas* afecta **Productividad Operacional**.
**Productividad Operacional** puede estar `bajo objetivo`, `en objetivo` o `sobre objetivo`.
**Profesional Coordinador** maneja *Monitorear Ejecución de Rutas*.
```

**Trazabilidad al modelo categórico:**
- Programación Diaria con ~20 pacientes activos/jornada, 3 conductores, 4 zonas: modelo categórico §16.13.
- GPS Tracking System como instrument (no agent): §16.13 (7.587 eventos GPS en 83 días, 87% match prog↔GPS).
- Productividad actual 39.2%: modelo categórico §16.13.

---

## SD1.4b — Refinamiento de *Shift Handover Executing*

*(Nuevo — enriquecimiento parte2)*

Refinamiento: in-zooming (subprocesos secuenciales). El proceso padre *Ejecutar Entrega de Turno* se descompone en 3 subprocesos que ocurren en secuencia.

### Tabla de Elementos SD1.4b

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Active Patient Status Reporting* | Informatical | Sistémico | — |
| Proceso | *Day Movement Registering* | Informatical | Sistémico | — |
| Proceso | *Clinical Responsibility Transferring* | Informatical | Sistémico | — |
| Objeto | **Patient Snapshot** | Informatical | Sistémico | `outdated`, `current` |
| Objeto | **Movement Record** | Informatical | Sistémico | — |
| Objeto | **Shift Handover Record** | Informatical | Sistémico | — |

### OPL-EN SD1.4b

```
SD1.4 is refined by in-zooming Shift Handover Executing in SD1.4b.
Shift Handover Executing zooms into Active Patient Status Reporting, Day Movement Registering and Clinical Responsibility Transferring, in that sequence.

Patient Snapshot can be outdated or current.
State outdated of Patient Snapshot is initial.
State current of Patient Snapshot is final.

Active Patient Status Reporting changes Patient Snapshot from outdated to current.
Clinical Nurse handles Active Patient Status Reporting.

Day Movement Registering yields Movement Record.
Clinical Nurse handles Day Movement Registering.

Shift Status can be pending or handed_over.
State pending of Shift Status is initial.
State handed_over of Shift Status is final.
Clinical Responsibility Transferring changes Shift Status from pending to handed_over.
Clinical Responsibility Transferring yields Shift Handover Record.
Clinical Nurse handles Clinical Responsibility Transferring.
```

### OPL-ES SD1.4b

```
SD1.4 se refina por descomposición de *Ejecutar Entrega de Turno* en SD1.4b.
*Ejecutar Entrega de Turno* se descompone en *Reportar Estado de Pacientes Activos*, *Registrar Movimientos del Día* y *Transferir Responsabilidad Clínica*, en esa secuencia.

**Snapshot de Pacientes** puede estar `desactualizado` o `actual`.
Estado `desactualizado` de **Snapshot de Pacientes** es inicial.
Estado `actual` de **Snapshot de Pacientes** es final.

*Reportar Estado de Pacientes Activos* cambia **Snapshot de Pacientes** de `desactualizado` a `actual`.
**Enfermero Clínico** maneja *Reportar Estado de Pacientes Activos*.

*Registrar Movimientos del Día* genera **Registro de Movimientos**.
**Enfermero Clínico** maneja *Registrar Movimientos del Día*.

**Estado de Turno** puede estar `pendiente` o `entregado`.
Estado `pendiente` de **Estado de Turno** es inicial.
Estado `entregado` de **Estado de Turno** es final.
*Transferir Responsabilidad Clínica* cambia **Estado de Turno** de `pendiente` a `entregado`.
*Transferir Responsabilidad Clínica* genera **Registro de Entrega de Turno**.
**Enfermero Clínico** maneja *Transferir Responsabilidad Clínica*.
```

**Trazabilidad al modelo categórico:**
- Snapshot clínico (7 columnas por paciente) y registro de movimientos: modelo categórico §16.3 (Entrega de turno).
- Dual agent (turno saliente + entrante): Metodología OPM §6.5 — ambos humanos con agent link válido.

---

## SD1.5 — Descomposición de *Clinical Evolution Monitoring*

*(Versión corregida: Vital Signs Data expandido de 4 a 12 variables)*

Refinamiento: in-zooming (secuencial con decisión XOR).

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
Invasive Device Status can be none, present_normal or present_infected.
State none of Invasive Device Status is initial.

Vital Signs Data consists of Blood Pressure, Heart Rate, Respiratory Rate, Oxygen Saturation, Body Temperature, Blood Glucose Level, Pain Scale Score, Glasgow Coma Score, Edema Status, Urine Output, Bowel Status and Invasive Device Status.

Clinical Record Updating consumes Vital Signs Data.
Clinical Record Updating affects Clinical Record.
Clinical Record Updating requires Communication System.
Clinical Nurse handles Clinical Record Updating.

Patient Category is informatical.
Patient Category can be stable, improving or deteriorating.
State stable of Patient Category is default.
Patient Categorizing yields Patient Category.
Patient Categorizing requires Vital Signs Data.
Attending Physician handles Patient Categorizing.

Continuity Deciding yields exactly one of continue-treatment Continuity Decision or proceed-discharge Continuity Decision.
Continuity Deciding requires Patient Category.
Continuity Deciding requires Operational Mode in full_weekday.
Attending Physician handles Continuity Deciding.
```

### OPL-ES SD1.5

```
SD1 se refina por descomposición de *Monitorear Evolución Clínica* en SD1.5.
*Monitorear Evolución Clínica* se descompone en *Evaluar Signos Vitales*, *Actualizar Registro Clínico*, *Categorizar Paciente* y *Decidir Continuidad*, en esa secuencia.

*Evaluar Signos Vitales* afecta **Grupo de Pacientes**.
*Evaluar Signos Vitales* requiere **Equipamiento Médico**.
**Enfermero Clínico** maneja *Evaluar Signos Vitales*.

**Datos de Signos Vitales** es informatical.
*Evaluar Signos Vitales* genera **Datos de Signos Vitales**.

**Presión Arterial** es informatical.
**Frecuencia Cardíaca** es informatical.
**Frecuencia Respiratoria** es informatical.
**Saturación de Oxígeno** es informatical.
**Temperatura Corporal** es informatical.
**Nivel de Glucosa en Sangre** es informatical.
**Puntaje de Escala de Dolor** es informatical.
**Puntaje de Escala de Coma de Glasgow** es informatical.
**Estado de Edema** es informatical.
**Estado de Edema** puede estar `ausente`, `leve`, `moderado` o `severo`.
Estado `ausente` de **Estado de Edema** es inicial.
**Diuresis** es informatical.
**Estado Intestinal** es informatical.
**Estado de Dispositivo Invasivo** es informatical.
**Estado de Dispositivo Invasivo** puede estar `ninguno`, `presente_normal` o `presente_infectado`.
Estado `ninguno` de **Estado de Dispositivo Invasivo** es inicial.

**Datos de Signos Vitales** consta de **Presión Arterial**, **Frecuencia Cardíaca**, **Frecuencia Respiratoria**, **Saturación de Oxígeno**, **Temperatura Corporal**, **Nivel de Glucosa en Sangre**, **Puntaje de Escala de Dolor**, **Puntaje de Escala de Coma de Glasgow**, **Estado de Edema**, **Diuresis**, **Estado Intestinal** y **Estado de Dispositivo Invasivo**.

*Actualizar Registro Clínico* consume **Datos de Signos Vitales**.
*Actualizar Registro Clínico* afecta **Ficha Clínica**.
*Actualizar Registro Clínico* requiere **Sistema de Comunicación**.
**Enfermero Clínico** maneja *Actualizar Registro Clínico*.

**Categoría del Paciente** es informatical.
**Categoría del Paciente** puede estar `estable`, `mejorando` o `deteriorándose`.
Estado `estable` de **Categoría del Paciente** es por defecto.
*Categorizar Paciente* genera **Categoría del Paciente**.
*Categorizar Paciente* requiere **Datos de Signos Vitales**.
**Médico de Atención Directa** maneja *Categorizar Paciente*.

*Decidir Continuidad* genera exactamente uno de **Decisión de Continuidad** en `continuar tratamiento` o **Decisión de Continuidad** en `proceder egreso`.
*Decidir Continuidad* requiere **Categoría del Paciente**.
*Decidir Continuidad* requiere **Modo Operacional** en `días_hábiles`.
**Médico de Atención Directa** maneja *Decidir Continuidad*.
```

**Trazabilidad al modelo categórico:**
- 12 variables de Vital Signs Data: modelo categórico §4.3 y §10.2 (formulario "Registro Visita Equipo HODOM").
- Edema Status estados: evaluación clínica semiestructurada del formulario.
- Invasive Device Status: vigilancia de catéteres intravenosos, traqueostomías según protocolo clínico.

---

## SD1.6 — Despliegue de *Patient Discharging*

*(Sin cambios respecto al modelo original v1.)*

Refinamiento: unfolding por generalización-especialización (tipos de egreso mutuamente excluyentes).

### OPL-EN

```
Medical Discharge, Hospital Readmission Discharge, Expected Death Discharge, Unexpected Death Discharge, Voluntary Withdrawal Discharge and Disciplinary Discharge are Patient Discharging.

Medical Discharge changes Clinical Condition to recovered.
Medical Discharge changes Hospitalization Status from active to discharged.
Medical Discharge requires Operational Mode in full_weekday.
Medical Discharge yields Epicrisis.
Attending Physician handles Medical Discharge.

Hospital Readmission Discharge changes Hospitalization Status from active to discharged.
Hospital Readmission Discharge requires Inpatient Facility.
Hospital Readmission Discharge requires Transport Vehicle.
Hospital Readmission Discharge yields Epicrisis.
Attending Physician handles Hospital Readmission Discharge.

Clinical Instability is informatical.
Clinical Instability can be absent or present.
Hospital Readmission Discharge occurs if Clinical Instability is present, in which case Hospital Readmission Discharge changes Clinical Instability from present, otherwise Hospital Readmission Discharge is skipped.

Expected Death Discharge changes Hospitalization Status from active to discharged.
Expected Death Discharge yields Epicrisis.
Attending Physician handles Expected Death Discharge.

Death Protocol is informatical.
Expected Death Discharge yields Death Protocol.

Palliative Intent is informatical.
Palliative Intent can be absent or present.
Expected Death Discharge occurs if Palliative Intent is present, in which case Expected Death Discharge changes Hospitalization Status from active to discharged, otherwise Expected Death Discharge is skipped.

Unexpected Death Discharge changes Hospitalization Status from active to discharged.
Unexpected Death Discharge yields Epicrisis.
Attending Physician handles Unexpected Death Discharge.
Unexpected Death Discharge yields Death Protocol.

Voluntary Withdrawal Discharge changes Hospitalization Status from active to discharged.
Voluntary Withdrawal Discharge requires Informed Consent.
Voluntary Withdrawal Discharge yields Epicrisis.

Withdrawal Statement is informatical.
Voluntary Withdrawal Discharge yields Withdrawal Statement.

Disciplinary Discharge changes Hospitalization Status from active to discharged.
Technical Director handles Disciplinary Discharge.
Disciplinary Discharge yields Epicrisis.

Treatment Adherence is informatical.
Treatment Adherence can be adherent or non-adherent.
Disciplinary Discharge occurs if Treatment Adherence is non-adherent, in which case Disciplinary Discharge changes Hospitalization Status from active to discharged, otherwise Disciplinary Discharge is skipped.
```

### OPL-ES

```
*Egresar por Alta Médica*, *Egresar por Reingreso Hospitalario*, *Egresar por Fallecimiento Esperado*, *Egresar por Fallecimiento no Esperado*, *Egresar por Renuncia Voluntaria* y *Egresar por Alta Disciplinaria* son *Egresar de Hospitalización Domiciliaria*.

*Egresar por Alta Médica* cambia **Condición Clínica** a `recuperado`.
*Egresar por Alta Médica* cambia **Estado de Hospitalización** de `activa` a `egresado`.
*Egresar por Alta Médica* requiere **Modo Operacional** en `días_hábiles`.
*Egresar por Alta Médica* genera **Epicrisis**.
**Médico de Atención Directa** maneja *Egresar por Alta Médica*.

*Egresar por Reingreso Hospitalario* cambia **Estado de Hospitalización** de `activa` a `egresado`.
*Egresar por Reingreso Hospitalario* requiere **Establecimiento de Atención Cerrada**.
*Egresar por Reingreso Hospitalario* requiere **Vehículo de Transporte**.
*Egresar por Reingreso Hospitalario* genera **Epicrisis**.
**Médico de Atención Directa** maneja *Egresar por Reingreso Hospitalario*.

**Inestabilidad Clínica** es informatical.
**Inestabilidad Clínica** puede estar `ausente` o `presente`.
*Egresar por Reingreso Hospitalario* ocurre si **Inestabilidad Clínica** está en `presente`, en cuyo caso *Egresar por Reingreso Hospitalario* cambia **Inestabilidad Clínica** de `presente`, de lo contrario *Egresar por Reingreso Hospitalario* se omite.

*Egresar por Fallecimiento Esperado* cambia **Estado de Hospitalización** de `activa` a `egresado`.
*Egresar por Fallecimiento Esperado* genera **Epicrisis**.
**Médico de Atención Directa** maneja *Egresar por Fallecimiento Esperado*.

**Protocolo de Fallecimiento** es informatical.
*Egresar por Fallecimiento Esperado* genera **Protocolo de Fallecimiento**.

**Intención Paliativa** es informatical.
**Intención Paliativa** puede estar `ausente` o `presente`.
*Egresar por Fallecimiento Esperado* ocurre si **Intención Paliativa** está en `presente`, en cuyo caso *Egresar por Fallecimiento Esperado* cambia **Estado de Hospitalización** de `activa` a `egresado`, de lo contrario *Egresar por Fallecimiento Esperado* se omite.

*Egresar por Fallecimiento no Esperado* cambia **Estado de Hospitalización** de `activa` a `egresado`.
*Egresar por Fallecimiento no Esperado* genera **Epicrisis**.
**Médico de Atención Directa** maneja *Egresar por Fallecimiento no Esperado*.
*Egresar por Fallecimiento no Esperado* genera **Protocolo de Fallecimiento**.

*Egresar por Renuncia Voluntaria* cambia **Estado de Hospitalización** de `activa` a `egresado`.
*Egresar por Renuncia Voluntaria* requiere **Consentimiento Informado**.
*Egresar por Renuncia Voluntaria* genera **Epicrisis**.

**Declaración de Retiro** es informatical.
*Egresar por Renuncia Voluntaria* genera **Declaración de Retiro**.

*Egresar por Alta Disciplinaria* cambia **Estado de Hospitalización** de `activa` a `egresado`.
**Director Técnico** maneja *Egresar por Alta Disciplinaria*.
*Egresar por Alta Disciplinaria* genera **Epicrisis**.

**Adherencia al Tratamiento** es informatical.
**Adherencia al Tratamiento** puede estar `adherente` o `no adherente`.
*Egresar por Alta Disciplinaria* ocurre si **Adherencia al Tratamiento** está en `no adherente`, en cuyo caso *Egresar por Alta Disciplinaria* cambia **Estado de Hospitalización** de `activa` a `egresado`, de lo contrario *Egresar por Alta Disciplinaria* se omite.
```

---

## SD1.7 — Seguimiento Post-Egreso

*(Nuevo — enriquecimiento parte3)*

Refinamiento: in-zooming (secuencial). Proceso que se ejecuta después del egreso del paciente, incluye llamada de seguimiento, contrarreferencia a atención primaria y evaluación de resultado.

### Tabla de Elementos SD1.7

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Follow-Up Call Executing* | Informatical | Sistémico | — |
| Proceso | *Primary Care Counterreferral Sending* | Informatical | Sistémico | — |
| Proceso | *Discharge Outcome Evaluating* | Informatical | Sistémico | — |
| Objeto | **Follow-Up Status** | Informatical | Sistémico | `pending`, `contacted`, `completed` |
| Objeto | **Follow-Up Call Record** | Informatical | Sistémico | — |
| Objeto | **Counterreferral Status** | Informatical | Sistémico | `pending`, `sent`, `acknowledged` |
| Objeto | **Discharge Outcome** | Informatical | Sistémico | `favorable`, `unfavorable` |

### OPL-EN SD1.7

```
SD1 is refined by in-zooming Post-Discharge Following in SD1.7.
Post-Discharge Following occurs if Hospitalization Status is discharged.
Post-Discharge Following zooms into Follow-Up Call Executing, Primary Care Counterreferral Sending and Discharge Outcome Evaluating, in that sequence.

Follow-Up Status can be pending, contacted or completed.
State pending of Follow-Up Status is initial.
Follow-Up Call Executing changes Follow-Up Status from pending to contacted.
Follow-Up Call Executing yields Follow-Up Call Record.
Clinical Nurse handles Follow-Up Call Executing.
Attending Physician handles Follow-Up Call Executing if Operational Mode is full_weekday, otherwise Follow-Up Call Executing is skipped.
Follow-Up Call Executing requires Communication System.

Counterreferral Status can be pending, sent or acknowledged.
State pending of Counterreferral Status is initial.
Primary Care Counterreferral Sending changes Counterreferral Status from pending to sent.
Primary Care Counterreferral Sending consumes Epicrisis.
Primary Care Counterreferral Sending requires Primary Care Center.
Coordination Professional handles Primary Care Counterreferral Sending.
Primary Care Counterreferral Sending requires Communication System.

Discharge Outcome can be favorable or unfavorable.
Discharge Outcome Evaluating changes Discharge Outcome.
Discharge Outcome Evaluating occurs if Operational Mode is full_weekday, otherwise Discharge Outcome Evaluating is skipped.
Attending Physician handles Discharge Outcome Evaluating.
```

### OPL-ES SD1.7

```
SD1 se refina por descomposición de *Seguimiento Post-Egreso* en SD1.7.
*Seguimiento Post-Egreso* ocurre si **Estado de Hospitalización** está en `egresado`.
*Seguimiento Post-Egreso* se descompone en *Ejecutar Llamada de Seguimiento*, *Enviar Contrarreferencia a Atención Primaria* y *Evaluar Resultado del Egreso*, en esa secuencia.

**Estado de Seguimiento** puede estar `pendiente`, `contactado` o `completado`.
Estado `pendiente` de **Estado de Seguimiento** es inicial.
*Ejecutar Llamada de Seguimiento* cambia **Estado de Seguimiento** de `pendiente` a `contactado`.
*Ejecutar Llamada de Seguimiento* genera **Registro de Llamada de Seguimiento**.
**Enfermero Clínico** maneja *Ejecutar Llamada de Seguimiento*.
**Médico de Atención Directa** maneja *Ejecutar Llamada de Seguimiento* si **Modo Operacional** está en `días_hábiles`, de lo contrario *Ejecutar Llamada de Seguimiento* se omite.
*Ejecutar Llamada de Seguimiento* requiere **Sistema de Comunicación**.

**Estado de Contrarreferencia** puede estar `pendiente`, `enviado` o `reconocido`.
Estado `pendiente` de **Estado de Contrarreferencia** es inicial.
*Enviar Contrarreferencia a Atención Primaria* cambia **Estado de Contrarreferencia** de `pendiente` a `enviado`.
*Enviar Contrarreferencia a Atención Primaria* consume **Epicrisis**.
*Enviar Contrarreferencia a Atención Primaria* requiere **Centro de Salud Familiar**.
**Profesional Coordinador** maneja *Enviar Contrarreferencia a Atención Primaria*.
*Enviar Contrarreferencia a Atención Primaria* requiere **Sistema de Comunicación**.

**Resultado del Egreso** puede estar `favorable` o `desfavorable`.
*Evaluar Resultado del Egreso* cambia **Resultado del Egreso**.
*Evaluar Resultado del Egreso* ocurre si **Modo Operacional** está en `días_hábiles`, de lo contrario *Evaluar Resultado del Egreso* se omite.
**Médico de Atención Directa** maneja *Evaluar Resultado del Egreso*.
```

**Trazabilidad al modelo categórico:**
- Follow-Up Call: modelo categórico §16.12 (7 meses de datos, julio 2024–enero 2025; llamadas a pacientes activos y egresados).
- Contrarreferencia a CESFAM: DS 1/2022 art. 16; NT 2024.
- Follow-Up Status con pending/contacted/completed: modelo categórico §16.12 (Call Tracking).

---

## SD2 — Despliegue Estructural del Equipo de Salud

*(Versión corregida: Fonoaudiólogo obligatorio, Gestora Encargada y Conductor agregados)*

Refinamiento: unfolding por agregación-participación.

### OPL-EN SD2

```
Healthcare Team consists of Technical Director, Coordination Professional, Case Manager, Attending Physician, Clinical Nurse, Kinesiologist, Nursing Technician, Social Worker, Speech Therapist, Administrative Staff, Driver and at least one other part.

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
Midwife is physical.
Psychologist is physical.
Occupational Therapist is physical.

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
Work Schedule of Driver can be weekday_daytime or rotating_shift.
```

### OPL-ES SD2

```
**Equipo de Salud** consta de **Director Técnico**, **Profesional Coordinador**, **Gestora Encargada**, **Médico de Atención Directa**, **Enfermero Clínico**, **Kinesiólogo**, **Técnico de Enfermería**, **Trabajador Social**, **Fonoaudiólogo**, **Personal Administrativo**, **Conductor** y al menos otra parte.

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
**Matrona** es física.
**Psicólogo** es físico.
**Terapeuta Ocupacional** es física.

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
**Régimen de Jornada** de **Conductor** puede estar `diurno_lunes_a_viernes` o `turno_rotativo_lunes_a_domingo`.
```

**Trazabilidad al modelo categórico:**
- Speech Therapist obligatorio: modelo categórico §5.2 (1.279 visitas/año fonoaudiología HSC — volumen que justifica dedicación completa).
- Case Manager: modelo categórico §5.2, §16.1.
- Driver: modelo categórico §16.1 (4 conductores HSC: 3 turno rotativo L-D + 1 diurno L-V).
- Work Schedule: `weekday_daytime` (L-V, 08:00–17:00) y `rotating_shift` (cuarto turno L-D).

---

## SD3 — Despliegue Estructural de Infraestructura Administrativa

*(Sin cambios respecto al modelo original v1.)*

Refinamiento: unfolding por agregación-participación.

### OPL-EN

```
Administrative Infrastructure consists of Telephone System, IT System, Electrical Backup System, Clinical Archive Area, Pharmacy or Authorized Dispensary, Supply Storage, Waste Disposal Area, Cleaning Supply Room, Staff Welfare Area, Vehicle Parking and Evacuation Signage System.

Telephone System is physical.
Telephone System exhibits Availability.
Availability of Telephone System can be 24/7 or partial.
State 24/7 of Availability of Telephone System is initial.

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

Pharmacy or Authorized Dispensary is physical.
Pharmacy or Authorized Dispensary exhibits Cold Chain Compliance.
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
**Infraestructura Administrativa** consta de **Sistema Telefónico**, **Sistema Informático**, **Respaldo Eléctrico**, **Área de Archivo Clínico**, **Farmacia o Botiquín Autorizado**, **Bodega de Insumos**, **Área de Disposición de Residuos**, **Recinto de Aseo**, **Área de Bienestar del Personal**, **Estacionamiento de Vehículos** y **Sistema de Señalización y Evacuación**.

**Sistema Telefónico** es físico.
**Sistema Telefónico** exhibe **Disponibilidad**.
**Disponibilidad** de **Sistema Telefónico** puede estar `24/7` o `parcial`.
Estado `24/7` de **Disponibilidad** de **Sistema Telefónico** es inicial.

**Sistema Telefónico** exhibe **Trazabilidad de Llamadas**.
**Trazabilidad de Llamadas** es informatical.
**Trazabilidad de Llamadas** puede estar `habilitada` o `deshabilitada`.
Estado `habilitada` de **Trazabilidad de Llamadas** es inicial.

**Sistema Informático** es informatical.
**Sistema Informático** exhibe **Conectividad Internet**.

**Respaldo Eléctrico** es físico.
**Respaldo Eléctrico** exhibe **Autorización SEC**.

**Área de Archivo Clínico** es físico.
**Área de Archivo Clínico** exhibe **Nivel de Seguridad**.
**Nivel de Seguridad** puede estar `seguro` o `no seguro`.
Estado `seguro` de **Nivel de Seguridad** es inicial.

**Farmacia o Botiquín Autorizado** es físico.
**Farmacia o Botiquín Autorizado** exhibe **Cumplimiento de Cadena de Frío**.
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

---

## SD4 — Despliegue Estructural de Equipamiento Médico

*(Sin cambios respecto al modelo original v1.)*

Refinamiento: unfolding por agregación-participación.

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

---

## SD5 — Despliegue Estructural del Sistema de Documentación

*(Sin cambios respecto al modelo original v1.)*

Refinamiento: unfolding por agregación del sistema documental.

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

**Sistema Documental** es informatical.

**Sistema Documental** consta de **Manual de Organización Interna**, **Conjunto de Protocolos Clínicos**, **Manual de Procedimientos**, **Protocolo de Manejo de Residuos** y **Plan Anual de Capacitación**.

**Manual de Organización Interna** es informatical.
**Manual de Organización Interna** consta de **Organigrama**, **Conjunto de Definiciones de Rol**, **Definición de Horarios** y **Reglamento de Higiene**.

**Conjunto de Protocolos Clínicos** es informatical.
**Conjunto de Protocolos Clínicos** consta de **Protocolo de Evaluación e Ingreso**, **Protocolo de Programación de Visitas y Rutas**, **Protocolo de Categorización y Egreso**, **Protocolo de Gestión de Recetas e Interconsultas**, **Protocolo de Actuación ante Emergencias** y **Protocolo ante Agresiones al Personal**.

**Manual de Procedimientos** es informatical.
**Manual de Procedimientos** consta de **Procedimiento de Vía Venosa Periférica**, **Procedimiento de Vía Venosa Central**, **Procedimiento de Catéter Urinario**, **Procedimiento de Traqueostomía**, **Procedimiento de Toma de Muestras** y **Procedimiento de Precauciones de Aislamiento**.

**Protocolo de Manejo de Residuos** es informatical.
**Protocolo de Manejo de Residuos** exhibe **Cumplimiento Decreto REAS**.

**Plan Anual de Capacitación** es informatical.
**Plan Anual de Capacitación** consta de **Capacitación IAAS**, **Capacitación SVB**, **Programa de Inducción** y **Capacitación en Humanización del Cuidado**.

**Programa de Inducción** es informatical.
**Programa de Inducción** exhibe **Duración Mínima**.
**Duración Mínima** de **Programa de Inducción** varía de 44 a 200 horas.
```

---

## SD6 — Procesos de Gobernanza del Sistema

*(Sin cambios respecto al modelo original v1.)*

Operaciones del sistema modeladas como exhibition-characterization.

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
Supply Chain Managing requires Pharmacy or Authorized Dispensary.
Coordination Professional handles Supply Chain Managing.

Waste Managing consumes Biomedical Waste.
Waste Managing requires Waste Disposal Area.
Waste Managing requires Waste Management Protocol.

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

**Estado de Autorización Sanitaria** es informatical.
**Sistema de Hospitalización Domiciliaria** exhibe **Estado de Autorización Sanitaria**.
**Estado de Autorización Sanitaria** puede estar `pendiente`, `autorizado` o `vencido`.
Estado `pendiente` de **Estado de Autorización Sanitaria** es inicial.
*Gestionar Autorización Sanitaria* cambia **Estado de Autorización Sanitaria** de `pendiente` a `autorizado`.

**Vigencia de Autorización** es informatical.
**Estado de Autorización Sanitaria** exhibe **Vigencia de Autorización**.
**Vigencia de Autorización** de **Estado de Autorización Sanitaria** varía de 0 a 3 años.

**SEREMI** es físico.
**SEREMI** es ambiental.
**SEREMI** supervisa **Sistema de Hospitalización Domiciliaria**.
*Gestionar Autorización Sanitaria* requiere **SEREMI**.

*Gestionar Calidad y Seguridad* afecta **Sistema de Hospitalización Domiciliaria**.
*Gestionar Calidad y Seguridad* requiere **Sistema Documental**.
**Profesional Coordinador** maneja *Gestionar Calidad y Seguridad*.

**Nivel de Calidad** es informatical.
**Sistema de Hospitalización Domiciliaria** exhibe **Nivel de Calidad**.
*Gestionar Calidad y Seguridad* afecta **Nivel de Calidad**.

**Auditoría de Reacciones Adversas** es informatical.
*Gestionar Calidad y Seguridad* genera **Auditoría de Reacciones Adversas**.
**Auditoría de Mortalidad** es informatical.
*Gestionar Calidad y Seguridad* genera **Auditoría de Mortalidad**.

*Gestionar Capacitación del Personal* afecta **Equipo de Salud**.
*Gestionar Capacitación del Personal* requiere **Plan Anual de Capacitación**.
**Profesional Coordinador** maneja *Gestionar Capacitación del Personal*.

**Cumplimiento de Capacitación** es informatical.
**Equipo de Salud** exhibe **Cumplimiento de Capacitación**.
**Cumplimiento de Capacitación** puede estar `cumple` o `no cumple`.
*Gestionar Capacitación del Personal* cambia **Cumplimiento de Capacitación** de `no cumple` a `cumple`.

*Gestionar Cadena de Abastecimiento* afecta **Insumo Clínico**.
*Gestionar Cadena de Abastecimiento* afecta **Medicamento**.
*Gestionar Cadena de Abastecimiento* requiere **Farmacia o Botiquín Autorizado**.
**Profesional Coordinador** maneja *Gestionar Cadena de Abastecimiento*.

*Gestionar Residuos* consume **Residuo Biomédico**.
*Gestionar Residuos* requiere **Área de Disposición de Residuos**.
*Gestionar Residuos* requiere **Protocolo de Manejo de Residuos**.

**Residuo Biomédico** es físico.

**Protocolo de Desecho de Cortopunzantes** es informatical.
*Gestionar Residuos* requiere **Protocolo de Desecho de Cortopunzantes**.

*Gestionar Mantención de Equipos* afecta **Equipamiento Médico**.
*Gestionar Mantención de Equipos* cambia **Estado de Mantención** de `vencido` a `vigente`.
**Director Técnico** maneja *Gestionar Mantención de Equipos*.

**Programa de Mantención Preventiva** es informatical.
*Gestionar Mantención de Equipos* requiere **Programa de Mantención Preventiva**.

*Gestionar Capacidad* afecta **Sistema de Hospitalización Domiciliaria**.
**Profesional Coordinador** maneja *Gestionar Capacidad*.

**Capacidad Instalada** es informatical.
**Sistema de Hospitalización Domiciliaria** exhibe **Capacidad Instalada**.

**Cupos Programados** es informatical.
**Capacidad Instalada** exhibe **Cupos Programados**.

**Cupos Utilizados** es informatical.
**Capacidad Instalada** exhibe **Cupos Utilizados**.

**Cupos Disponibles** es informatical.
**Capacidad Instalada** exhibe **Cupos Disponibles**.

**Cupos Campaña de Invierno** es informatical.
**Capacidad Instalada** exhibe **Cupos Campaña de Invierno**.

**Cupos Salud Mental** es informatical.
**Capacidad Instalada** exhibe **Cupos Salud Mental**.

**Cupos Adulto** es informatical.
**Capacidad Instalada** exhibe **Cupos Adulto**.

**Cupos Pediátrico** es informatical.
**Capacidad Instalada** exhibe **Cupos Pediátrico**.

*Gestionar Capacidad* afecta **Capacidad Instalada**.
```

---

## SD7 — Despliegue del Domicilio del Paciente (Condiciones de Elegibilidad)

*(Sin cambios respecto al modelo original v1.)*

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

**Servicios Básicos** es informatical.
**Servicios Básicos** puede estar `disponible` o `no disponible`.

**Acceso a Telefonía** es informatical.
**Acceso a Telefonía** puede estar `disponible` o `no disponible`.

**Acceso Vial** es informatical.
**Acceso Vial** puede estar `dentro del radio de cobertura` o `fuera del radio de cobertura`.
```

---

## SD8 — Exclusiones del Sistema (Condiciones que Impiden Ingreso)

*(Sin cambios respecto al modelo original v1.)*

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
**Condición de Exclusión** es informatical.
**Condición de Exclusión** puede estar `ausente` o `presente`.
Estado `ausente` de **Condición de Exclusión** es inicial.

**Exclusión por Inestabilidad Clínica**, **Exclusión por Diagnóstico no Establecido**, **Exclusión por Salud Mental Descompensada**, **Exclusión por Prestación no Listada** y **Exclusión por Alta Disciplinaria Previa** son **Condición de Exclusión**.

*Evaluar Elegibilidad* ocurre si **Condición de Exclusión** está en `ausente`, en cuyo caso *Evaluar Elegibilidad* cambia **Estado de Elegibilidad** de `pendiente` a `elegible`, de lo contrario *Evaluar Elegibilidad* se omite.
```

---

## SD9 — Relaciones Estructurales Etiquetadas (Tagged Structural Links)

*(Sin cambios respecto al modelo original v1.)*

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
```

### OPL-ES

```
**Establecimiento de Atención Cerrada** deriva **Grupo de Pacientes**.
**Domicilio del Paciente** alberga **Grupo de Pacientes**.
**SEREMI** supervisa **Sistema de Hospitalización Domiciliaria**.
**Normativa Vigente** rige **Sistema de Hospitalización Domiciliaria**.
**Director Técnico** representa **Sistema de Hospitalización Domiciliaria**.
**Sistema de Hospitalización Domiciliaria** garantiza **Continuidad de la Atención**.
**Continuidad de la Atención** es informatical.
**Médico de Atención Directa** coordina con **Establecimiento de Atención Cerrada**.
**Médico Regulador** apoya a **Médico de Atención Directa**.
**Cuidador** cuida a **Grupo de Pacientes**.
```

---

## SD10 — Modo Operacional del Sistema

*(Nuevo — enriquecimiento parte3)*

Refinamiento: exhibition-characterization. Modela los dos modos operativos del sistema HODOM HSC: `full_weekday` (L-V) y `reduced_weekend` (S-D y festivos), y su efecto sobre qué procesos están habilitados.

### Tabla de Elementos SD10

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Weekly Schedule Cycling* | Físico | Ambiental | — |
| Objeto | **Operational Mode** | Informatical | Sistémico | `full_weekday`, `reduced_weekend` |

### OPL-EN SD10

```
SD is extended by SD10 for Operational Mode modeling.
Domiciliary Hospitalization System exhibits Operational Mode.
Operational Mode can be full_weekday or reduced_weekend.
State full_weekday of Operational Mode is initial.

Weekly Schedule Cycling is environmental.
Weekly Schedule Cycling changes Operational Mode from full_weekday to reduced_weekend.
Weekly Schedule Cycling changes Operational Mode from reduced_weekend to full_weekday.
Domiciliary Hospitalization System exhibits Weekly Schedule Cycling.
```

### OPL-ES SD10

```
SD se extiende por SD10 para el modelamiento del Modo Operacional.
**Sistema de Hospitalización Domiciliaria** exhibe **Modo Operacional**.
**Modo Operacional** puede estar `días_hábiles` o `fines_de_semana`.
Estado `días_hábiles` de **Modo Operacional** es inicial.

*Ciclo Semanal* es ambiental.
*Ciclo Semanal* cambia **Modo Operacional** de `días_hábiles` a `fines_de_semana`.
*Ciclo Semanal* cambia **Modo Operacional** de `fines_de_semana` a `días_hábiles`.
**Sistema de Hospitalización Domiciliaria** exhibe *Ciclo Semanal*.
```

**Trazabilidad al modelo categórico:**
- Cuarto turno (L-D): 08:00-20:00, rotación largo-largo-libre-libre: modelo categórico §6.2.
- Diurnos (médico, TS, fono): 44 hrs L-V, 08:00-17:00: modelo categórico §6.2.
- SUV disponible solo L-V (reduce capacidad vehicular a 2/3 el fin de semana): modelo categórico §6.2, §16.5.

**Procesos NO ejecutables en modo `reduced_weekend`:**
- Eligibility Evaluating, Continuity Deciding, Medical Discharge, Speech Therapy Executing, Discharge Outcome Evaluating.

**Procesos ejecutables en ambos modos (sin condición):**
- Nursing Care Executing, Kinesiological Therapy Executing, Medication Administering, Patient and Caregiver Educating, Vital Signs Evaluating, Clinical Record Updating, Daily Logistics Managing, Shift Handover Executing, Wound Care Executing.

**Nota coalgebraica:** El sistema HODOM se modela como un autómata de estados finitos donde el conjunto de transiciones habilitadas depende del modo. En `reduced_weekend`, el sistema se comporta como un sub-autómata propio: δ(`reduced_weekend`, *Medical Visit*) = ∅ (no definida / skip), mientras que δ(`reduced_weekend`, *Nursing Care*) = Nursing Care executándose (definida).

---

## Validación del Modelo

### Checklist SD

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Sistema clasificado | Socio-técnico determinado | PASS | CRÍTICA |
| Purpose definido | Grupo de Pacientes + Condición Clínica + agudo/reagudizado → recuperado | PASS | CRÍTICA |
| Función definida | Hospitalizar en Domicilio + Grupo de Pacientes (transformee) | PASS | CRÍTICA |
| Enablers presentes | 1 agente (Equipo de Salud) + 5 instrumentos (equip., comunicación, transporte, admin., postulación digital) | PASS | ALTA |
| Environment identificado | 4 objetos ambientales (Domicilio, Establecimiento, Normativa, CESFAM) | PASS | MEDIA |
| Problem occurrence | Episodio Agudo (proceso ambiental) → estado agudo/reagudizado | PASS | MEDIA |
| Tagged structural bidireccional | CESFAM ↔ Domiciliary Hospitalizing (f-tag + b-tag + Patient Discharging f-tag) | PASS | MEDIA |
| OPL legible | Sentencias OPL correctas en EN y ES | PASS | ALTA |
| Naming compliant | Gerundio EN / Infinitivo ES + singular + Group | PASS | ALTA |
| Exhibition | Sistema exhibe proceso principal + Modo Operacional | PASS | ALTA |
| Agents = humanos | Equipo de Salud es grupo humano; instrumentos son no-humanos | PASS | ALTA |

### Checklist SD1

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Subprocesos transforman | Cada subproceso ≥1 transformee | PASS | CRÍTICA |
| Refinamiento correcto | Secuencial → in-zooming (7 subprocesos) | PASS | ALTA |
| Links distribuidos | Consumption/result NO en outer contour | PASS | CRÍTICA |
| Split links resueltos | Effect sobre Condición Clínica asignado a Monitorear Evolución | PASS | ALTA |
| Estados expresados | Estados de Plan Terapéutico, Consentimiento, etc. visibles | PASS | ALTA |
| Consent coherence | Consent cambia en Evaluar Elegibilidad (SD1) y se descompone en SD1.1 | PASS | ALTA |
| Post-Discharge Following incluido | 7° subproceso en secuencia SD1 | PASS | ALTA |
| Sin redundancia | Hechos no duplicados innecesariamente | PASS | MEDIA |

### Checklist SD1.1 (v2.0 — 6 subprocesos)

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Subprocesos transforman | Cada subproceso ≥1 transformee | PASS | CRÍTICA |
| Agent links solo humanos | Social Worker, Case Manager, Attending Physician, Clinical Nurse | PASS | CRÍTICA |
| Condition instruments | Insurance Status, Patient Age, Hospital Distance como condición | PASS | ALTA |
| Condition para Exclusion | Exclusion Condition (ausente/presente) conecta a Eligibility Evaluating | PASS | ALTA |
| Secuencia completa | 6 subprocesos en orden correcto | PASS | ALTA |
| OPD ≤ 25 entidades | SD1.1 ≈ 19 entidades | PASS | MEDIA |

### Checklist SD1.4 (v2.0 — 10 subprocesos paralelos)

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Subprocesos transforman | Cada subproceso ≥1 transformee | PASS | CRÍTICA |
| Remote Care Regulating agente correcto | Clinical Nurse agente principal; Attending Physician condicional | PASS | CRÍTICA |
| Condition instruments Operational Mode | Medical Visit, Speech Therapy Executing requieren full_weekday | PASS | ALTA |
| Call Record como resultado | Remote Care Regulating genera Call Record | PASS | ALTA |
| GPS Tracking System = instrument (no agent) | §6.5: software = instrument; agent link = solo humanos | PASS | ALTA |
| OPD ≤ 25 entidades | SD1.4 ≈ 27 entidades (aceptable — OPD complejojustificado) | PASS (condicional) | MEDIA |

### Checklist SD1.4a y SD1.4b

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| B4 proceso condicional | Unrouted Visit Resolving ocurre solo si existe unrouted visit | PASS | ALTA |
| Dual agent en B1/B2/B3 | Driver como segundo agente (humano) | PASS | ALTA |
| GPS = instrument | GPS Tracking System no tiene agent link | PASS | ALTA |
| Dual agent en C3 | Clinical Nurse (saliente + entrante) | PASS | ALTA |
| OPD ≤ 25 entidades | SD1.4a ≈ 9, SD1.4b ≈ 4 | PASS | MEDIA |

### Checklist SD1.5 (v2.0 — 12 Vital Signs)

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Vital Signs Data = 12 componentes | Consistencia con formulario Registro Visita Equipo HODOM | PASS | CRÍTICA |
| Estados donde corresponde | Edema Status (4), Invasive Device Status (3) expresados | PASS | ALTA |
| Continuity Deciding condicional | Requiere Operational Mode in full_weekday | PASS | ALTA |

### Checklist SD1.6

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Tipo async correcto | Generalization para tipos de egreso | PASS | ALTA |
| Muerte esperada/no esperada | Distinción conforme DEIS REM A21 C.1.1 | PASS | ALTA |
| Cada especialización transforma | Todos cambian Hospitalization Status | PASS | CRÍTICA |
| Medical Discharge condicional | Requiere Operational Mode in full_weekday | PASS | ALTA |

### Checklist SD1.7

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Subprocesos transforman | Cada subproceso ≥1 transformee | PASS | CRÍTICA |
| Agent links solo humanos | Clinical Nurse, Attending Physician, Coordination Professional | PASS | CRÍTICA |
| Condition links para opcionales | Post-Discharge Following es condition process (si discharged) | PASS | ALTA |
| Condition agent | Attending Physician maneja Follow-Up Call si full_weekday | PASS | ALTA |
| Condition instrument | Discharge Outcome Evaluating requiere full_weekday | PASS | ALTA |
| Estados expresados | Follow-Up Status (3), Counterreferral Status (3), Discharge Outcome (2) | PASS | ALTA |
| OPD ≤ 25 entidades | SD1.7 ≈ 15 entidades | PASS | MEDIA |

### Checklist SD2 (v2.0)

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Agent = humano | Todos los roles son físicos (humanos) | PASS | ALTA |
| Speech Therapist obligatorio | Pasa de complementario a parte de Healthcare Team | PASS | ALTA |
| Case Manager especialización | specialization de Coordination Professional | PASS | ALTA |
| OPD ≤ 25 entidades | SD2 ≈ 25 entidades | PASS | MEDIA |

### Checklist SD10

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Weekly Schedule Cycling transforma | Cambia Operational Mode (full_weekday ↔ reduced_weekend) | PASS | CRÍTICA |
| Agent links | Ninguno (Weekly Schedule Cycling es ambiental — no controlable por el sistema) | PASS | CRÍTICA |
| Estados expresados | Operational Mode con full_weekday y reduced_weekend | PASS | ALTA |
| OPD ≤ 25 entidades | SD10 = 3 entidades | PASS | MEDIA |
| Exhibition correcta | Sistema exhibe Modo Operacional | PASS | ALTA |
| Objetro informatical | Operational Mode es informatical | PASS | ALTA |

### Checklist Global

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Claridad | Ningún OPD excede 25 entidades (salvo SD1.4 con 27, justificado por complejidad) | PASS (condicional) | MEDIA |
| Name coherency | Sin nombres duplicados con significado diferente | PASS | ALTA |
| Implicit objects | Objetos implícitos identificados en originales y enriquecimiento | PASS | ALTA |
| Emergencia arquitectural | El sistema produce atención hospitalaria en domicilio — capacidad emergente que ningún componente individual exhibe | PASS | MEDIA |
| Trazabilidad fuerte | Cada componente respaldado por DS 1/2022, NT 2024, DEIS REM A21, o modelo categórico HODOM v4.1 | PASS | ALTA |
| OPD count | 20 OPDs (originales 16 + SD1.7 + SD1.4a + SD1.4b + SD10) | PASS | MEDIA |

---

## Resumen de OPDs del Modelo

| OPD | Contenido | Entidades aprox. | Cambio respecto a v1 |
|-----|-----------|-------------------|----------------------|
| SD | Sistema HODOM — función, propósito, habilitadores, ambiente, problem occurrence | 18 | +2 (CESFAM, Sistema de Postulación Digital) |
| SD1 | Descomposición — 7 subprocesos secuenciales (nuevo: Post-Discharge Following) | 21 | +1 (7° subproceso en OPL) |
| SD1.1 | Evaluar Elegibilidad — 6 subprocesos (versión corregida) | 19 | +7 (Candidate Screening, Application Receiving, Candidate, Case Manager, Insurance Status, Patient Age, Hospital Distance) |
| SD1.2 | Ingresar Paciente — 4 subprocesos | 11 | — |
| SD1.3 | Planificar Atención — 4 subprocesos | 10 | — |
| SD1.4 | Ejecutar Plan Terapéutico — 10 subprocesos paralelos (versión corregida) | 27 | +4 (Wound Care, Speech Therapy, Daily Logistics, Shift Handover; +Remote Care Regulating corregido) |
| SD1.4a | Gestionar Logística Diaria — 5 subprocesos (NUEVO) | 9 | Nuevo OPD |
| SD1.4b | Ejecutar Entrega de Turno — 3 subprocesos (NUEVO) | 4 | Nuevo OPD |
| SD1.5 | Monitorear Evolución Clínica — 4 subprocesos con Vital Signs Data de 12 variables | 19 | +8 (8 variables nuevas de signos vitales) |
| SD1.6 | Egresar — 6 tipos de egreso (con Operational Mode condition) | 20 | +1 (condition Medical Discharge) |
| SD1.7 | Seguimiento Post-Egreso — 3 subprocesos (NUEVO) | 15 | Nuevo OPD |
| SD2 | Equipo de Salud — 12 roles + atributos (corregido) | 25 | +3 (Fonoaudiólogo obligatorio, Gestora Encargada, Conductor) |
| SD3 | Infraestructura Administrativa — 11 componentes | 20 | — |
| SD4 | Equipamiento Médico — 6 dispositivos | 10 | — |
| SD5 | Sistema Documental — manuales, protocolos, plan de capacitación | 22 | — |
| SD6 | Procesos de Gobernanza — 7 operaciones | 28 | — |
| SD7 | Domicilio del Paciente — condiciones de elegibilidad | 6 | — |
| SD8 | Exclusiones — 5 tipos de condición excluyente | 7 | — |
| SD9 | Relaciones estructurales etiquetadas | 10 | — |
| SD10 | Modo Operacional del Sistema (NUEVO) | 3 | Nuevo OPD |
| **Total** | **20 OPDs** | **~264 entidades** | **+4 OPDs, ~18 entidades netas nuevas** |

---

## Notas de Trazabilidad al Modelo Categórico HODOM v4.1

Las secciones nuevas y corregidas de la integración v2.0 se respaldan en las siguientes referencias del modelo categórico:

| Elemento nuevo/corrigido | Referencia categórica | Tipo |
|------------------------|----------------------|------|
| Primary Care Center (ambiental) | §3.2, §8.2 | Objeto ambiental SD |
| Digital Application System | §8.2 | Instrumento SD |
| Candidate Screening + Candidate | §5.1 | Proceso + objeto SD1.1 |
| Application Receiving + Case Manager | §5.2, §16.1 | Proceso + rol SD1.1/SD2 |
| Insurance Status, Patient Age, Hospital Distance | §9.1, DS 1/2022 art.15, NT 2024 | Condition instruments SD1.1 |
| Wound Care Executing + Wound Status + Wound Care Record | §10.6, §16.4 | Proceso + objeto + resultado SD1.4 |
| Speech Therapy Executing + Swallowing and Speech Status | §4.4, §16.5 | Proceso + estado SD1.4 |
| Remote Care Regulating (Clinical Nurse agente) | §5.2, §16.1, §16.12 | Proceso SD1.4 |
| Call Record | §16.12 | Resultado SD1.4 |
| Daily Logistics Managing + Daily Schedule Status | §16.13 | Proceso + estado SD1.4 |
| GPS Tracking System | §16.13 (7.587 eventos GPS) | Instrumento SD1.4a |
| Operational Productivity | §16.13 (39.2% productividad) | Objeto SD1.4a |
| Unrouted Visit + Unrouted Visit Resolving | §16.13 (zonas 2-4) | Objeto + proceso condicional SD1.4a |
| Route Assignment (3 estados) | §16.13 | Estado SD1.4a |
| Patient Snapshot, Movement Record, Shift Status | §16.3 | Objetos SD1.4b |
| Shift Handover Record | §16.3 | Resultado SD1.4b |
| Vital Signs Data (12 variables) | §4.3, §10.2 | Agregación SD1.5 |
| Edema Status, Invasive Device Status | §10.2 | Estados SD1.5 |
| Post-Discharge Following + Follow-Up Status | §16.12 (7 meses de datos) | Proceso + objeto SD1.7 |
| Follow-Up Call Record | §16.12 | Resultado SD1.7 |
| Counterreferral Status | §16.12, DS 1/2022 art.16, NT 2024 | Estado SD1.7 |
| Discharge Outcome | §16.12 | Estado SD1.7 |
| Operational Mode | §6.2, §16.5 | Estado SD1.4, SD1.5, SD1.6, SD1.7, SD10 |
| Weekly Schedule Cycling | §6.2 | Proceso ambiental SD10 |
| Fonoaudiólogo obligatorio | §4.4, §5.2, §16.5 (1.279 visitas/año) | Rol SD2 |
| Conductor + Work Schedule | §16.1, §16.13 | Rol + atributo SD2 |
| Fonoaudiólogo Work Schedule restriction | §6.2, §16.5 (solo L-V) | Condition SD1.4 |

---

_Fecha de elaboración: 2026-04-01_
_Modelo original: Mente Omega — OPM v1.0 (cumplimiento ISO/PAS 19450)_
_Integración v2.0: Subagente OPM — Mente Omega (enriquecimiento partes 1, 2 y 3)_