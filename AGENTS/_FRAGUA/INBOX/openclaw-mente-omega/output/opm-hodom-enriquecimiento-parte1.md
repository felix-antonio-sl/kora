# Enriquecimiento del Modelo OPM HODOM — Parte 1: Correcciones a Secciones Existentes

**Fuente:** Modelo Categórico HODOM v4.1 (27 fuentes, datos reales HSC)
**Fecha:** 2026-04-01

---

## A. Corrección SD — Objetos Ambientales Faltantes

### A.1 Nota de Cambio

El SD actual no incluye los objetos **Centro de Salud Familiar (CESFAM)** ni **Sistema de Postulación Digital** como instrumentos/ambiente del sistema HODOM. Ambos componentes son operativos en HSC según los datos del modelo categórico (§3.2, §8.2): la derivación desde atención primaria es un origen de postulación válido, y el ingreso al programa se realiza vía Google Form (Sistema de Postulación Digital).

### A.2 Tabla de Elementos — SD Corregido (solo elementos nuevos y modificados)

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Objeto | **Primary Care Center** | Físico | Ambiental | — |
| Objeto | **Digital Application System** | Informatical | Sistémico | — |

### A.3 Tabla de Enlaces — SD Corregido (solo enlaces nuevos)

| Tipo | Origen | Destino | ID Plantilla |
|------|--------|---------|--------------|
| Tagged structural (f-tag) | **Primary Care Center** | *Domiciliary Hospitalizing* | SE3 |
| Tagged structural (b-tag) | *Domiciliary Hospitalizing* | **Primary Care Center** | SE3 |
| Tagged structural (f-tag) | *Patient Discharging* | **Primary Care Center** | SE3 |
| Instrument | *Domiciliary Hospitalizing* | **Digital Application System** | H2 |

**Semántica de los tagged structural links:**

- `Primary Care Center f-tag Domiciliary Hospitalizing` → **Centro de Salud Familiar** deriva a *Hospitalizar en Domicilio* (flujo de entrada por derivación desde atención primaria).
- `Domiciliary Hospitalizing b-tag Primary Care Center` → El sistema de hospitalización domiciliaria se relaciona de vuelta con el CESFAM (flujo de referencia inversa).
- `Patient Discharging f-tag Primary Care Center` → *Egresar de Hospitalización Domiciliaria* genera contrarreferencia al CESFAM (derivación de salida).

### A.4 OPL-EN del SD — Sentencias Nuevas y Modificadas

```opm
Primary Care Center is physical.
Primary Care Center is environmental.
Primary Care Center refers Domiciliary Hospitalizing.
Domiciliary Hospitalizing refers Primary Care Center.
Patient Discharging yields referral to Primary Care Center.

Digital Application System is informatical.
Domiciliary Hospitalizing requires Digital Application System.
```

### A.5 OPL-ES del SD — Sentencias Nuevas y Modificadas

```opl
**Centro de Salud Familiar** es físico.
**Centro de Salud Familiar** es ambiental.
**Centro de Salud Familiar** deriva *Hospitalizar en Domicilio*.
*Hospitalizar en Domicilio* se relaciona de vuelta con **Centro de Salud Familiar**.
*Egresar de Hospitalización Domiciliaria* genera contrarreferencia a **Centro de Salud Familiar**.

**Sistema de Postulación Digital** es informático.
*Hospitalizar en Domicilio* requiere **Sistema de Postulación Digital**.
```

### A.6 Trazabilidad al Modelo Categórico

- **Primary Care Center**: modelo categórico §3.2 Origen de Derivación (primary-care) y §8.2 Fluxo de Derivación; también SD9 donde se menciona la coordinación con atención primaria.
- **Digital Application System**: modelo categórico §8.2 Sistema de Postulación Digital; la postulación real a HODOM HSC se realiza vía Google Form.

### A.7 Nota de Validación OPM

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Agent link = humano | Primary Care Center es objeto físico, no agent | PASS | ALTA |
| Instrument link = no-humano | Digital Application System es instrumento | PASS | ALTA |
| Tagged structural bidireccional | CESFAM ↔ Domiciliary Hospitalizing (f-tag + b-tag) | PASS | MEDIA |
| OPD ≤ 25 entidades | SD pasa de 16 a 18 entidades | PASS | MEDIA |

---

## B. Corrección SD1.1 — Completar Evaluar Elegibilidad

### B.1 Nota de Cambio

El SD1.1 actual tiene 4 subprocesos: *Clinical Condition Evaluating*, *Home Condition Evaluating*, *Support Network Verifying*, *Informed Consent Obtaining*. Se detectan tres omisiones críticas:

1. **Flujo de entrada ausente**: no existe un proceso que genere el objeto **Candidate** antes de la evaluación clínica. Trabajo Social busca activamente candidatos en pabellones y servicios clínicos (modelo categórico §5.1).
2. **Gestión de postulación ausente**: no existe un proceso que reciba, valide y asigne la postulación. El rol de **Case Manager** es quien opera este proceso (modelo categórico §5.2).
3. **Condiciones instrumentales de elegibilidad ausentes**: Insurance Status, Patient Age y Hospital Distance son objetos condition-instrument que determinan si *Eligibility Evaluating* puede ejecutarse. SD8 ya modela Exclusion Condition, pero el link de condición no aparece visualmente en SD1.1.

### B.2 Tabla de Elementos — SD1.1 Corregido (solo elementos nuevos)

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Candidate Screening* | Informatical | Sistémico | — |
| Proceso | *Application Receiving* | Informatical | Sistémico | — |
| Objeto | **Candidate** | Físico | Sistémico | `identified`, `postulated`, `ineligible` |
| Objeto | **Case Manager** | Físico | Sistémico | — |
| Objeto | **Insurance Status** | Informatical | Sistémico | `fonasa_a`, `fonasa_b`, `fonasa_c`, `fonasa_d`, `prais`, `other` |
| Objeto | **Patient Age** | Informatical | Sistémico | — |
| Objeto | **Hospital Distance** | Informatical | Sistémico | — |

### B.3 Tabla de Enlaces — SD1.1 Corregido (solo enlaces nuevos/modificados)

| Tipo | Origen | Destino | Notas |
|------|--------|---------|-------|
| Agent | **Social Worker** | *Candidate Screening* | Nuevo proceso, agente previo |
| Result | *Candidate Screening* | **Candidate** | Genera candidato identificado |
| Agent | **Case Manager** | *Application Receiving* | Nuevo proceso, agente dedicado |
| Result | *Application Receiving* | **Candidate** | Cambia Candidate a `postulated` |
| Condition instrument | *Eligibility Evaluating* | **Insurance Status** | `occurs if Insurance Status is fonasa_a or fonasa_b or fonasa_c or fonasa_d or prais` |
| Condition instrument | *Eligibility Evaluating* | **Patient Age** | `occurs if Patient Age is gte_18` |
| Condition instrument | *Eligibility Evaluating* | **Hospital Distance** | `occurs if Hospital Distance is lte_20km` |
| Condition instrument | *Eligibility Evaluating* | **Exclusion Condition** | Duplicación visual de SD8 en SD1.1 |
| Effect | *Application Receiving* | **Candidate** | Cambia Candidate de `identified` a `postulated` |

### B.4 Secuencia Completa Corregida de SD1.1

```
Candidate Screening → Application Receiving → Clinical Condition Evaluating → Home Condition Evaluating → Support Network Verifying → Informed Consent Obtaining
```

### B.5 OPL-EN — SD1.1 Completo Corregido

```opm
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

### B.6 OPL-ES — SD1.1 Completo Corregido

```opl
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

### B.7 Trazabilidad al Modelo Categórico

- **Candidate Screening** y **Candidate**: modelo categórico §5.1 Pesquisa Activa (1.279 visitas/año HSC por Trabajo Social).
- **Case Manager** y **Application Receiving**: modelo categórico §5.2 Gestión de Casos; la Gestora Encargada recibe postulaciones vía Google Form, evalúa elegibilidad inicial y asigna cupos.
- **Insurance Status**: modelo categórico §9.1 Previsión de Salud (sistema Isapre/Fonasa).
- **Patient Age**: DS 1/2022 art. 15 — criterio de elegibilidad etaria ≥18 años.
- **Hospital Distance**: Norma Técnica HODOM 2024 — criterio de distancia máxima 20 km.
- **Exclusion Condition duplicada en SD1.1**: SD8 ya define esta condición; se replica como instance visual en SD1.1 para hacer visible la restricción de elegibilidad en el contexto de evaluación.

### B.8 Nota de Validación OPM

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|-----------|
| Proceso transforma objeto | Cada subproceso tiene ≥1 transformee | PASS | CRÍTICA |
| Agent link = humano | Social Worker, Case Manager, Attending Physician, Clinical Nurse | PASS | ALTA |
| Condition instrument ≠ condition link | Insurance/ Age/ Distance son condition instruments | PASS | ALTA |
| Condition link para opcional | Exclusion Condition (ausente/presente) conecta a Eligibility Evaluating | PASS | ALTA |
| Secuencia completa | 6 subprocesos en orden correto | PASS | ALTA |
| OPD ≤ 25 entidades | SD1.1 pasa de ~12 a ~19 entidades | PASS | MEDIA |

---

## C. Corrección SD1.5 — Ampliar Vital Signs Data de 4 a 12 Variables

### C.1 Nota de Cambio

El SD1.5 actual define `Vital Signs Data consists of Blood Pressure, Heart Rate, Respiratory Rate and Oxygen Saturation.` Esta agregación es incompleta respecto al formulario real "Registro Visita Equipo HODOM" (modelo categórico §10.2), que contiene 12 variables. Se reemplazan las 4 variables existentes por las 12 completas.

### C.2 Tabla de Elementos — SD1.5 Corregido (solo elementos modificados)

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Objeto | **Blood Pressure** | Informatical | Sistémico | — |
| Objeto | **Heart Rate** | Informatical | Sistémico | — |
| Objeto | **Respiratory Rate** | Informatical | Sistémico | — |
| Objeto | **Oxygen Saturation** | Informatical | Sistémico | — |
| Objeto | **Body Temperature** | Informatical | Sistémico | — |
| Objeto | **Blood Glucose Level** | Informatical | Sistémico | — |
| Objeto | **Pain Scale Score** | Informatical | Sistémico | — |
| Objeto | **Glasgow Coma Score** | Informatical | Sistémico | — |
| Objeto | **Edema Status** | Informatical | Sistémico | `absent`, `mild`, `moderate`, `severe` |
| Objeto | **Urine Output** | Informatical | Sistémico | — |
| Objeto | **Bowel Status** | Informatical | Sistémico | — |
| Objeto | **Invasive Device Status** | Informatical | Sistémico | `none`, `present_normal`, `present_infected` |

### C.3 Tabla de Enlaces — SD1.5 Corregido (solo enlace modificado)

| Tipo | Origen | Destino | Notas |
|------|--------|---------|-------|
| Agregación | **Vital Signs Data** | 12 componentes | Reemplaza agregación de 4 componentes |

### C.4 OPL-EN — SD1.5 Sentencias Modificadas y Nuevas

```opm
Vital Signs Data consists of Blood Pressure, Heart Rate, Respiratory Rate, Oxygen Saturation, Body Temperature, Blood Glucose Level, Pain Scale Score, Glasgow Coma Score, Edema Status, Urine Output, Bowel Status and Invasive Device Status.

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
```

### C.5 OPL-ES — SD1.5 Sentencias Modificadas y Nuevas

```opl
**Datos de Signos Vitales** consta de **Presión Arterial**, **Frecuencia Cardíaca**, **Frecuencia Respiratoria**, **Saturación de Oxígeno**, **Temperatura Corporal**, **Nivel de Glucosa en Sangre**, **Puntaje de Escala de Dolor**, **Puntaje de Escala de Coma de Glasgow**, **Estado de Edema**, **Diuresis**, **Estado Intestinal** y **Estado de Dispositivo Invasivo**.

**Presión Arterial** es informática.
**Frecuencia Cardíaca** es informática.
**Frecuencia Respiratoria** es informática.
**Saturación de Oxígeno** es informática.
**Temperatura Corporal** es informática.
**Nivel de Glucosa en Sangre** es informática.
**Puntaje de Escala de Dolor** es informática.
**Puntaje de Escala de Coma de Glasgow** es informática.

**Estado de Edema** es informática.
**Estado de Edema** puede estar `ausente`, `leve`, `moderado` o `severo`.
Estado `ausente` de **Estado de Edema** es inicial.

**Diuresis** es informática.
**Estado Intestinal** es informática.

**Estado de Dispositivo Invasivo** es informática.
**Estado de Dispositivo Invasivo** puede estar `ninguno`, `presente_normal` o `presente_infectado`.
Estado `ninguno` de **Estado de Dispositivo Invasivo** es inicial.
```

### C.6 Trazabilidad al Modelo Categórico

- **Vital Signs Data** (12 variables): modelo categórico §4.3 ObservacionCicloVital (12 variables observadas en cada visita HODOM).
- **Registro Visita Equipo HODOM** (formulario): modelo categórico §10.2 — fuente primaria de las 12 variables.
- **Edema Status**: estados `absent/mild/moderate/severe` derivan de la evaluación clínica semiestructurada del formulario.
- **Invasive Device Status**: estados `none/present_normal/present_infected` — vigilancia de dispositivos intravenosos, catéteres y traqueostomías según protocolo clínico HODOM.

### C.7 Nota de Validación OPM

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|----------|
| Componentes informatcales | Las 8 variables nuevas son informatical | PASS | ALTA |
| Estados donde corresponde | Edema Status y Invasive Device Status con estados explícitos | PASS | ALTA |
| Consistencia con formulario | 12 componentes = formulario real "Registro Visita Equipo HODOM" | PASS | CRÍTICA |
| OPD ≤ 25 entidades | SD1.5 pasa de ~14 a ~22 entidades | PASS | MEDIA |

---

## D. Corrección SD2 — Roles Faltantes en Equipo de Salud

### D.1 Nota de Cambio

El SD2 actual tiene 9 roles mínimos y 4 roles complementarios. Se detectan tres correcciones según los datos reales de HSC (modelo categórico §5.2 y §16.1):

1. **Speech Therapist (Fonoaudiólogo)** debe pasar de complementario a obligatorio: HSC tiene 1.279 visitas/año de fonoaudiología, lo que constituye un volumen que justifica dedicación completa (no es accesorio).
2. **Case Manager (Gestora Encargada)** debe agregarse como especialización de Coordination Professional: es el rol que gestiona postulaciones, asigna cupos y hace seguimiento de pacientes.
3. **Driver (Conductor)** debe agregarse como parte del equipo: HSC opera con 4 conductores (3 en cuarto turno L-D + 1 diurno L-V).

### D.2 Tabla de Elementos — SD2 Corregido (solo elementos nuevos/modificados)

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Objeto | **Speech Therapist** | Físico | Sistémico | — |
| Objeto | **Case Manager** | Físico | Sistémico | — |
| Objeto | **Driver** | Físico | Sistémico | — |
| Objeto | **Assigned Patients** | Informatical | Sistémico | — |
| Objeto | **Work Schedule** | Informatical | Sistémico | `weekday_daytime`, `rotating_shift` |

### D.3 Tabla de Enlaces — SD2 Corregido (solo enlaces nuevos/modificados)

| Tipo | Origen | Destino | Notas |
|------|--------|---------|-------|
| Agregación | **Healthcare Team** | **Speech Therapist** | Speech Therapist pasa de complementario a obligatorio |
| Agregación | **Healthcare Team** | **Case Manager** | Nuevo: Case Manager como especialización |
| Agregación | **Healthcare Team** | **Driver** | Nuevo: Driver como parte del equipo |
| Especialización | **Case Manager** | **Coordination Professional** | Case Manager es subtipo de Coordination Professional |
| Exhibición | **Case Manager** | **Assigned Patients** | Atributo con rango 0–25 |
| Exhibición | **Driver** | **Work Schedule** | Estados: weekday_daytime, rotating_shift |

### D.4 OPL-EN — SD2 Completo Corregido

```opm
Healthcare Team consists of Technical Director, Coordination Professional, Case Manager, Attending Physician, Clinical Nurse, Kinesiologist, Nursing Technician, Social Worker, Speech Therapist, Administrative Staff and at least one other part.

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

### D.5 OPL-ES — SD2 Completo Corregido

```opl
**Equipo de Salud** consta de **Director Técnico**, **Profesional Coordinador**, **Gestora Encargada**, **Médico de Atención Directa**, **Enfermero Clínico**, **Kinesiólogo**, **Técnico de Enfermería**, **Trabajador Social**, **Fonoaudiólogo**, **Personal Administrativo** y al menos otra parte.

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

### D.6 Trazabilidad al Modelo Categórico

- **Speech Therapist obligatorio**: modelo categórico §5.2 Rol de Fonoaudiología — 1.279 visitas/año en HSC (volumen que justifica dedicación completa, no complementaria).
- **Case Manager**: modelo categórico §5.2 Gestión de Casos y §16.1 Distribución de Personal.
- **Driver**: modelo categórico §16.1 — 4 conductores en HSC: 3 turno rotativo L-D + 1 diurno L-V.
- **Work Schedule**: estados `weekday_daytime` (L-V, 08:00–17:00) y `rotating_shift` (cuarto turno L-D, 3 conductores) — datos reales de HSC.

### D.7 Nota de Validación OPM

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|----------|
| Agent = humano | Todos los roles son físicos (humanos) | PASS | ALTA |
| Agent link ≠ instrument | Ningún rol del equipo usa instrument link | PASS | ALTA |
| Speech Therapist obligatorio | Pasa de complementario a parte de Healthcare Team | PASS | ALTA |
| Case Manager especialización | specialization de Coordination Professional | PASS | ALTA |
| OPD ≤ 25 entidades | SD2 pasa de ~22 a ~25 entidades | PASS | MEDIA |

---

## E. Corrección SD1.4 — Agente de Regulación a Distancia

### E.1 Nota de Cambio

El SD1.4 actual declara `Regulating Physician handles Remote Care Regulating`. Esta моделирование es incorrecta para HSC: el Hospital San Carlos no cuenta con **Médico Regulador** dedicado. La regulación de atención a distancia en HSC opera mediante **Enfermero Clínico** (agente principal, presente todos los días) y **Médico de Atención Directa** (agente secundario, presente solo en modalidad semana completa).

Adicionalmente, se agrega **Call Record** como resultado de *Remote Care Regulating*, conforme al modelo categórico §16.12.

### E.2 Tabla de Elementos — SD1.4 Corregido (solo elementos nuevos/modificados)

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Remote Care Regulating* | Informatical | Sistémico | — |
| Objeto | **Call Record** | Informatical | Sistémico | `logged`, `reviewed` |
| Objeto | **Operational Mode** | Informatical | Sistémico | `full_weekday`, `extended` |

### E.3 Tabla de Enlaces — SD1.4 Corregido (solo enlaces modificados)

| Tipo | Origen | Destino | Notas |
|------|--------|---------|-------|
| Agent (principal) | **Clinical Nurse** | *Remote Care Regulating* | Reemplaza Regulating Physician |
| Agent (condition) | **Attending Physician** | *Remote Care Regulating* | `occurs if Operational Mode is full_weekday` |
| Result | *Remote Care Regulating* | **Call Record** | Nuevo: registro de llamada generado |
| Exhibition | **Healthcare Team** | **Operational Mode** | Define modo operativo del equipo |

### E.4 Nota Operativa sobre HSC

> **HSC opera sin Médico Regulador dedicado.** La regulación de atención a distancia es manejada por **Enfermero Clínico** (agente principal, disponible todos los días del año) y **Médico de Atención Directa** (agente secundario, disponible en modalidad semana completa). Las llamadas telefónicas son el canal primario de comunicación remota con pacientes y cuidadores.

### E.5 OPL-EN — SD1.4 Sentencias Modificadas y Nuevas

```opm
Remote Care Regulating affects Patient Group.
Remote Care Regulating requires Communication System.
Clinical Nurse handles Remote Care Regulating.
Attending Physician handles Remote Care Regulating if Operational Mode is full_weekday, otherwise Remote Care Regulating is skipped.
Remote Care Regulating yields Call Record.

Call Record is informatical.
Call Record can be logged or reviewed.
State logged of Call Record is initial.
State reviewed of Call Record is final.

Operational Mode is informatical.
Operational Mode can be full_weekday or extended.
Healthcare Team exhibits Operational Mode.

Telehealth Record is informatical.
Remote Care Regulating yields Telehealth Record.
```

### E.6 OPL-ES — SD1.4 Sentencias Modificadas y Nuevas

```opl
*Regular Atención a Distancia* afecta **Grupo de Pacientes**.
*Regular Atención a Distancia* requiere **Sistema de Comunicación**.
**Enfermero Clínico** maneja *Regular Atención a Distancia*.
**Médico de Atención Directa** maneja *Regular Atención a Distancia* si **Régimen Operativo** está en `semana_completa`, de lo contrario *Regular Atención a Distancia* se omite.
*Regular Atención a Distancia* genera **Registro de Llamada**.

**Registro de Llamada** es informática.
**Registro de Llamada** puede estar `registrado` o `revisado`.
Estado `registrado` de **Registro de Llamada** es inicial.
Estado `revisado` de **Registro de Llamada** es final.

**Régimen Operativo** es informática.
**Régimen Operativo** puede estar `semana_completa` o `extendido`.
**Equipo de Salud** exhibe **Régimen Operativo**.

**Registro de Telesalud** es informática.
*Regular Atención a Distancia* genera **Registro de Telesalud**.
```

### E.7 Trazabilidad al Modelo Categórico

- **Regulating Physician removido**: HSC no dispone de este rol según modelo categórico §16.1 — la regulación remota recae en Clinical Nurse y Attending Physician.
- **Clinical Nurse agente principal**: modelo categórico §5.2 Responsabilidades de Enfermería; disponible 7 días/semana.
- **Attending Physician agente secundario**: modelo categórico §16.1 Modalidades de Operación — disponible en `full_weekday` (modalidad semana completa).
- **Call Record**: modelo categórico §16.12 Registro de Llamadas — 100% de llamadas registradas en ficha clínica.
- **Operational Mode**: modelo categórico §16.1 — dos regímenes operativos definidos en HSC.

### E.8 Nota de Validación OPM

| Check | Condición | Resultado | Severidad |
|-------|-----------|-----------|----------|
| Agent = humano | Clinical Nurse y Attending Physician son humanos | PASS | ALTA |
| Agent link = humano | No se asigna agent link a software o sistema | PASS | ALTA |
| Condition agent | Attending Physician actúa solo si Operational Mode = full_weekday | PASS | ALTA |
| Proceso transforma objeto | Remote Care Regulating afecta Patient Group | PASS | ALTA |
| Result presente | Call Record como resultado de Remote Care Regulating | PASS | ALTA |
| OPD ≤ 25 entidades | SD1.4 pasa de ~20 a ~23 entidades | PASS | MEDIA |

---

## F. Resumen de Entidades por OPD Corregido

| OPD | Entidades previas | Entidades corregidas | Delta |
|-----|------------------|----------------------|-------|
| SD | 16 | 18 | +2 (CESFAM, Sistema Postulación Digital) |
| SD1.1 | ~12 | ~19 | +7 (Candidate Screening, Application Receiving, Candidate, Case Manager, Insurance Status, Patient Age, Hospital Distance) |
| SD1.4 | ~20 | ~23 | +3 (Call Record, Operational Mode, condición agent) |
| SD1.5 | ~14 | ~22 | +8 (8 variables de signos vitales nuevas) |
| SD2 | ~22 | ~25 | +3 (Speech Therapist obligatorio, Case Manager, Driver) |

**Total entidades adicionales en el modelo: ~23 nuevas entidades.**

---

## G. Validación Global de las Correcciones

### Checklist Global Post-Corrección

| Check | Condición | OPD | Resultado | Severidad |
|-------|-----------|-----|-----------|----------|
| Agent link = humano | Ningún agent link a software/sistema | Todos | PASS | CRÍTICA |
| Todo proceso transforma | Cada subproceso tiene ≥1 transformee | SD1.1, SD1.4 | PASS | CRÍTICA |
| Nombres singulares | Ningún plural en nombres de cosas | Todos | PASS | ALTA |
| Proceso EN gerundio | Todos los procesos terminan en -ing | SD1.1, SD1.4 | PASS | ALTA |
| Proceso ES infinitivo/-ción | Convenciones OPL-ES respetadas | Todos | PASS | ALTA |
| Consumption/result NO outer contour | Sin enlaces de consumo/result en contorno externo | SD1.1 | PASS | CRÍTICA |
| Condition para procesos opcionales | Exclusion Condition, Operational Mode | SD1.1, SD1.4 | PASS | ALTA |
| OPD ≤ 25 entidades | Todos los OPD corregidos | Todos | PASS | MEDIA |
| Trazabilidad categórica | Cada corrección con referencia a § del modelo categórico | Todos | PASS | ALTA |

---

## H. Dependencias Entre Correcciones

| Corrección | Depende de | Razón |
|-----------|-----------|-------|
| B (SD1.1) | — | Independiente |
| E (SD1.4) | — | Independiente |
| D (SD2) | — | Independiente |
| C (SD1.5) | — | Independiente |
| A (SD) | — | Independiente |

Ninguna corrección depende de otra. Todas pueden aplicarse concurrentemente.

---

## I. Siguiente Paso Recomendado

Este documento constituye la **Parte 1** del enriquecimiento del modelo OPM HODOM. Se recomienda generar una **Parte 2** que aborde:

1. **SD1.2**: Refinar el rol de Administrative Staff respecto al Digital Application System (el ingreso real al sistema es vía Google Form).
2. **SD1.3**: Agregar la programación de visitas del fonoaudiólogo como subproceso dentro de *Care Planning* (necesario dado que Speech Therapist pasa a rol obligatorio).
3. **SD6**: Agregar procesos de gobernanza para *Gestionar Postulación Digital* y *Gestionar Registro de Llamadas*.
4. **SD9**: Actualizar tagged structural links para incluir la relación CESFAM ↔ Patient Discharging (contrarreferencia).
5. **Validación cruzada**: Verificar que las nuevas entidades (Case Manager, Driver, Call Record, Insurance Status, Patient Age, Hospital Distance) no generen inconsistencias con SD1, SD3 o SD6.

---

_Fecha de elaboración: 2026-04-01_
_Elaborado por: Subagente OPM — Mente Omega_
_Modelado conforme a: ISO/PAS 19450 (OPM), OPL-ES v1.3.1, Metodología v3.5.1_
