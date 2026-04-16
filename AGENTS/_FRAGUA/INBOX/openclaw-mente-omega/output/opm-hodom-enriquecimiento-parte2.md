# Enriquecimiento del Modelo OPM HODOM — Parte 2: SD1.4 Ampliado + SD1.4a Logística + SD1.4b Entrega de Turno

**Fuente:** Modelo Categórico HODOM v4.1 (27 fuentes, datos reales HSC)
**Fecha:** 2026-04-01

---

## A. Corrección SD1.4 — Ampliación a 9 Subprocesos Paralelos

El SD1.4 actual contiene 6 subprocesos paralelos. Se agregan 3 nuevos subprocesos (A1, A2, A3) que completan la operación asistencial directa del programa, alcanzando un total de **9 subprocesos paralelos**. La operación Logística Diaria (A3) se refina en SD1.4a (Sección B).

### A1. Wound Care Executing — Ejecutar Curación

Proceso clínico especializado, documentalmente diferenciado de los cuidados de enfermería genéricos. Dispone de formulario propio (Registro de Curaciones) y genera prestaciones codificadas en la Canasta HODOM (CuracionSimple, CuracionAvanzada, códigos MAI).

#### Tabla de Elementos — A1

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Wound Care Executing* | Físico | Sistémico | — |
| Objeto | **Wound Status** | Informatical | Sistémico | `active`, `healing`, `resolved` |
| Objeto | **Wound Care Record** | Informatical | Sistémico | — |
| Objeto | **Clinical Supply** | Físico | Sistémico | — |
| Agente | **Clinical Nurse** | Físico | Sistémico | — |

#### Tabla de Enlaces — A1

| Tipo | Origen | Destino | Notas |
|------|--------|---------|-------|
| Agente | **Clinical Nurse** | *Wound Care Executing* | H1 |
| Transformee | *Wound Care Executing* | **Wound Status** | Efecto: `active` → `healing` / `resolved` |
| Consumo | *Wound Care Executing* | **Clinical Supply** | Apósitos y materiales de cura |
| Resultado | *Wound Care Executing* | **Wound Care Record** | T2 |
| Exhibition | **Patient Group** | **Wound Status** | Cada paciente puede exhibir estado de herida |

#### OPL-EN — A1

```
Wound Care Executing affects Patient Group.
Wound Status can be active, healing or resolved.
State active of Wound Status is initial.
State healing of Wound Status is default.
State resolved of Wound Status is final.
Wound Care Executing changes Wound Status from active to healing.
Wound Care Executing changes Wound Status from healing to resolved.
Wound Care Executing requires Therapeutic Plan in active.
Wound Care Executing consumes Clinical Supply.
Wound Care Executing yields Wound Care Record.
Clinical Nurse handles Wound Care Executing.
Patient Group exhibits Wound Status.
```

#### OPL-ES — A1

```
*Ejecutar Curación* afecta **Grupo de Pacientes**.
**Estado de Herida** puede estar `activo`, `en cicatrización` o `resuelto`.
Estado `activo` de **Estado de Herida** es inicial.
Estado `en cicatrización` de **Estado de Herida** es por defecto.
Estado `resuelto` de **Estado de Herida** es final.
*Ejecutar Curación* cambia **Estado de Herida** de `activo` a `en cicatrización`.
*Ejecutar Curación* cambia **Estado de Herida** de `en cicatrización` a `resuelto`.
*Ejecutar Curación* requiere **Plan Terapéutico** en `activo`.
*Ejecutar Curación* consume **Insumo Clínico**.
*Ejecutar Curación* genera **Registro de Curación**.
**Enfermero Clínico** maneja *Ejecutar Curación*.
**Grupo de Pacientes** exhibe **Estado de Herida**.
```

#### Trazabilidad A1

| Elemento | Fuente |
|----------|--------|
| Registro de Curaciones | Modelo categórico §10.6 — Formularios del sistema |
| CuracionSimple / CuracionAvanzada (códigos MAI) | Modelo categórico §16.4 — Canasta HODOM |
| Wound Status como estado informatical | Metodología OPM §3 (atributo informatical de Patient Group) |

---

### A2. Speech Therapy Executing — Ejecutar Fonoaudiología

Proceso especializado con profesional dedicado. Presenta la mayor frecuencia de visitas dentro del programa (1.279 visitas/año en HSC) y restricción operativa de disponibilidad L-V.

#### Tabla de Elementos — A2

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Speech Therapy Executing* | Físico | Sistémico | — |
| Objeto | **Swallowing and Speech Status** | Informatical | Sistémico | `impaired`, `improving`, `functional` |
| Objeto | **Speech Therapy Record** | Informatical | Sistémico | — |
| Objeto | **Operational Mode** | Informatical | Sistémico | `full_weekday`, `extended` |
| Agente | **Speech Therapist** | Físico | Sistémico | — |

#### Tabla de Enlaces — A2

| Tipo | Origen | Destino | Notas |
|------|--------|---------|-------|
| Agente | **Speech Therapist** | *Speech Therapy Executing* | H1; agente complementario ya presente en SD2 |
| Transformee | *Speech Therapy Executing* | **Swallowing and Speech Status** | Efecto: `impaired` → `improving` → `functional` |
| Resultado | *Speech Therapy Executing* | **Speech Therapy Record** | T2 |
| Requiere (instrumento estado) | *Speech Therapy Executing* | **Operational Mode** | Condición instrumento: solo opera en `full_weekday` |
| Exhibition | **Patient Group** | **Swallowing and Speech Status** | RF2 |

#### OPL-EN — A2

```
Speech Therapy Executing affects Patient Group.
Swallowing and Speech Status can be impaired, improving or functional.
State impaired of Swallowing and Speech Status is initial.
State improving of Swallowing and Speech Status is default.
State functional of Swallowing and Speech Status is final.
Speech Therapy Executing changes Swallowing and Speech Status from impaired to improving.
Speech Therapy Executing changes Swallowing and Speech Status from improving to functional.
Speech Therapy Executing requires Therapeutic Plan in active.
Speech Therapy Executing yields Speech Therapy Record.
Operational Mode can be full_weekday or extended.
Speech Therapy Executing requires Operational Mode in full_weekday.
Speech Therapist handles Speech Therapy Executing.
Patient Group exhibits Swallowing and Speech Status.
```

#### OPL-ES — A2

```
*Ejecutar Fonoaudiología* afecta **Grupo de Pacientes**.
**Estado de Deglución y Habla** puede estar `alterado`, `en mejora` o `funcional`.
Estado `alterado` de **Estado de Deglución y Habla** es inicial.
Estado `en mejora` de **Estado de Deglución y Habla** es por defecto.
Estado `funcional` de **Estado de Deglución y Habla** es final.
*Ejecutar Fonoaudiología* cambia **Estado de Deglución y Habla** de `alterado` a `en mejora`.
*Ejecutar Fonoaudiología* cambia **Estado de Deglución y Habla** de `en mejora` a `funcional`.
*Ejecutar Fonoaudiología* requiere **Plan Terapéutico** en `activo`.
*Ejecutar Fonoaudiología* genera **Registro de Fonoaudiología**.
**Modo Operacional** puede estar `días hábiles completo` o `extendido`.
*Ejecutar Fonoaudiología* requiere **Modo Operacional** en `días hábiles completo`.
**Fonoaudiólogo** maneja *Ejecutar Fonoaudiología*.
**Grupo de Pacientes** exhibe **Estado de Deglución y Habla**.
```

#### Trazabilidad A2

| Elemento | Fuente |
|----------|--------|
| Fonoaudiólogo como agente obligatorio | Metodología OPM §6.5 — Agent link reservado a humanos; SD2 como complementario → obligatorio aquí |
| 1.279 visitas/año fonoaudiológicas | Modelo categórico §4.4 — Tabla de visitas 2024 (HSC) |
| Restricción L-V (full_weekday) | Modelo categórico §16.5 — Consolidado de prestaciones (fono solo días hábiles) |
| Codificación operacional FONO | Metodología OPM §6.1 — Nombre de proceso + infinitivo EN |

---

### A3. Daily Logistics Managing — Gestionar Logística Diaria

Subsistema logístico recurrente que se ejecuta diariamente y determina la capacidad efectiva del programa. Es el único subproceso paralelo de SD1.4 que se refina en un OPD propio (SD1.4a), dada su complejidad interna. El resto de los subprocesos se ejecutan dentro de la ventana logística habilitada por este proceso.

#### Tabla de Elementos — A3

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Daily Logistics Managing* | Informatical | Sistémico | — |
| Objeto | **Daily Schedule Status** | Informatical | Sistémico | `pending`, `assigned`, `executed` |
| Objeto | **Daily Schedule** | Informatical | Sistémico | — |
| Objeto | **Visit Schedule** | Informatical | Sistémico | — |
| Objeto | **Transport Vehicle** | Físico | Sistémico | — |
| Agente | **Coordination Professional** | Físico | Sistémico | — |

#### Tabla de Enlaces — A3

| Tipo | Origen | Destino | Notas |
|------|--------|---------|-------|
| Agente | **Coordination Professional** | *Daily Logistics Managing* | H1 |
| Transformee | *Daily Logistics Managing* | **Daily Schedule Status** | Efecto: `pending` → `assigned` → `executed` |
| Requiere | *Daily Logistics Managing* | **Visit Schedule** | Instrumento (enabler) |
| Requiere | *Daily Logistics Managing* | **Transport Vehicle** | Instrumento (enabler) |
| Resultado | *Daily Logistics Managing* | **Daily Schedule** | T2 |

#### OPL-EN — A3

```
Daily Logistics Managing changes Daily Schedule Status from pending to assigned.
Daily Logistics Managing changes Daily Schedule Status from assigned to executed.
Daily Schedule Status can be pending, assigned or executed.
State pending of Daily Schedule Status is initial.
State assigned of Daily Schedule Status is default.
State executed of Daily Schedule Status is final.
Daily Logistics Managing requires Visit Schedule.
Daily Logistics Managing requires Transport Vehicle.
Daily Logistics Managing yields Daily Schedule.
Coordination Professional handles Daily Logistics Managing.
```

#### OPL-ES — A3

```
*Gestionar Logística Diaria* cambia **Estado de Programación Diaria** de `pendiente` a `asignada`.
*Gestionar Logística Diaria* cambia **Estado de Programación Diaria** de `asignada` a `ejecutada`.
**Estado de Programación Diaria** puede estar `pendiente`, `asignada` o `ejecutada`.
Estado `pendiente` de **Estado de Programación Diaria** es inicial.
Estado `asignada` de **Estado de Programación Diaria** es por defecto.
Estado `ejecutada` de **Estado de Programación Diaria** es final.
*Gestionar Logística Diaria* requiere **Programa de Visitas**.
*Gestionar Logística Diaria* requiere **Vehículo de Transporte**.
*Gestionar Logística Diaria* genera **Programación Diaria**.
**Profesional Coordinador** maneja *Gestionar Logística Diaria*.
```

#### Trazabilidad A3

| Elemento | Fuente |
|----------|--------|
| Programación Diaria con datos reales (35 días, 4 zonas) | Modelo categórico §16.13 — Programación Diaria |
| Profesional Coordinador como agente de logística | Metodología OPM §6.5; SD1.3 ya lo establece en SD1 como agente de programación |
| Visit Schedule como input | SD1.3 — *Programar Visitas Domiciliarias* genera **Programa de Visitas** |

---

### Sentencia SD1.4 Actualizada — 9 Subprocesos Paralelos

#### OPL-EN SD1.4 Actualizada

```
SD1 is refined by in-zooming Therapeutic Plan Executing in SD1.4.
Therapeutic Plan Executing zooms into parallel Medical Visit Performing, Nursing Care Executing, Kinesiological Therapy Executing, Medication Administering, Remote Care Regulating, Patient and Caregiver Educating, Wound Care Executing, Speech Therapy Executing and Daily Logistics Managing.

Medical Visit Performing affects Patient Group.
Medical Visit Performing requires Therapeutic Plan in active.
Medical Visit Performing requires Medical Equipment.
Medical Visit Performing requires Transport Vehicle.
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
Regulating Physician handles Remote Care Regulating.
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
Speech Therapy Executing changes Swallowing and Speech Status from impaired to improving.
Speech Therapy Executing changes Swallowing and Speech Status from improving to functional.
Speech Therapy Executing requires Therapeutic Plan in active.
Speech Therapy Executing yields Speech Therapy Record.
Operational Mode can be full_weekday or extended.
Speech Therapy Executing requires Operational Mode in full_weekday.
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
```

#### OPL-ES SD1.4 Actualizada

```
SD1 se refina por descomposición de *Ejecutar Plan Terapéutico* en SD1.4.
*Ejecutar Plan Terapéutico* se descompone en paralelo *Realizar Visita Médica*, *Ejecutar Cuidados de Enfermería*, *Ejecutar Terapia Kinesiológica*, *Administrar Medicamentos*, *Regular Atención a Distancia*, *Educar a Paciente y Cuidador*, *Ejecutar Curación*, *Ejecutar Fonoaudiología* y *Gestionar Logística Diaria*.

*Realizar Visita Médica* afecta **Grupo de Pacientes**.
*Realizar Visita Médica* requiere **Plan Terapéutico** en `activo`.
*Realizar Visita Médica* requiere **Equipamiento Médico**.
*Realizar Visita Médica* requiere **Vehículo de Transporte**.
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
**Médico Regulador** maneja *Regular Atención a Distancia*.
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
*Ejecutar Fonoaudiología* cambia **Estado de Deglución y Habla** de `alterado` a `en mejora`.
*Ejecutar Fonoaudiología* cambia **Estado de Deglución y Habla** de `en mejora` a `funcional`.
*Ejecutar Fonoaudiología* requiere **Plan Terapéutico** en `activo`.
*Ejecutar Fonoaudiología* genera **Registro de Fonoaudiología**.
**Modo Operacional** puede estar `días hábiles completo` o `extendido`.
*Ejecutar Fonoaudiología* requiere **Modo Operacional** en `días hábiles completo`.
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
```

---

## B. SD1.4a — Refinamiento de *Daily Logistics Managing* / *Gestionar Logística Diaria*

**Refinamiento:** in-zooming (subprocesos secuenciales). El proceso padre *Gestionar Logística Diaria* se descompone en 5 subprocesos que ocurren en secuencia diaria: la asignación de pacientes a ruta (B1) precede a la asignación de profesionales (B2), que precede al secuenciamiento de visitas (B3), cuyo resultado puede requerir resolución de visitas sin ruta (B4), y todo el ciclo cierra con el monitoreo de ejecución vía GPS (B5).

**Decisión de diseño:** in-zooming secuencial, no paralelismo, porque la secuencia de asignación tiene dependencia causal directa (B2 necesita el resultado de B1; B3 necesita B2; B4 es condicional sobre la existencia de visitas sin ruta asignada).

---

### B1. Patient Route Assigning — Asignar Pacientes a Ruta

Cada jornada, aproximadamente 20 pacientes activos se distribuyen entre 3 conductores según ubicación geográfica. Este subproceso consume el estado `pending` del **Daily Schedule Status** y genera la **Asignación de Ruta** en estado `unassigned`.

#### Tabla de Elementos — B1

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Patient Route Assigning* | Informatical | Sistémico | — |
| Objeto | **Route Assignment** | Informatical | Sistémico | `unassigned`, `assigned`, `staffed` |
| Objeto | **Patient Home** | Físico | Ambiental | — |
| Agente | **Coordination Professional** | Físico | Sistémico | — |
| Agente | **Driver** | Físico | Sistémico | — |

#### Tabla de Enlaces — B1

| Tipo | Origen | Destino | Notas |
|------|--------|---------|-------|
| Agente | **Coordination Professional** | *Patient Route Assigning* | H1 |
| Agente | **Driver** | *Patient Route Assigning* | H1 (dual agent — ejecuta la ruta) |
| Transformee | *Patient Route Assigning* | **Route Assignment** | Efecto: `unassigned` → `assigned` |
| Requiere | *Patient Route Assigning* | **Patient Home** | Para geolocalización |

#### OPL-EN — B1

```
Patient Route Assigning changes Route Assignment from unassigned to assigned.
Route Assignment can be unassigned, assigned or staffed.
State unassigned of Route Assignment is initial.
State assigned of Route Assignment is default.
Patient Route Assigning requires Patient Home.
Coordination Professional handles Patient Route Assigning.
Driver handles Patient Route Assigning.
```

#### OPL-ES — B1

```
*Asignar Pacientes a Ruta* cambia **Asignación de Ruta** de `sin asignar` a `asignada`.
**Asignación de Ruta** puede estar `sin asignar`, `asignada` o `con equipo`.
Estado `sin asignar` de **Asignación de Ruta** es inicial.
Estado `asignada` de **Asignación de Ruta** es por defecto.
*Asignar Pacientes a Ruta* requiere **Domicilio del Paciente**.
**Profesional Coordinador** maneja *Asignar Pacientes a Ruta*.
**Conductor** maneja *Asignar Pacientes a Ruta*.
```

#### Trazabilidad B1

| Elemento | Fuente |
|----------|--------|
| ~20 pacientes activos diarios | Modelo categórico §16.13 — datos de programación real |
| 3 conductores | Metodología OPM §6.5 — Driver como agente (humano); SD1.4a nota de datos categóricos |
| Distribución geográfica | Metodología OPM §9.14 — Patient Home como objeto implícito en texto source |

---

### B2. Staff Route Assigning — Asignar Profesionales a Ruta

Enfermera, kinesiólogo y fonoaudiólogo se asignan a la ruta del conductor que pasa por sus pacientes. La composición del equipo varía cada jornada según la geografía de las visitas. Este subproceso consume la **Asignación de Ruta** en estado `assigned` y la lleva a `staffed`.

#### Tabla de Elementos — B2

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Staff Route Assigning* | Informatical | Sistémico | — |
| Objeto | **Healthcare Team** | Físico | Sistémico | — |
| Agente | **Coordination Professional** | Físico | Sistémico | — |
| Agente | **Driver** | Físico | Sistémico | — |

#### Tabla de Enlaces — B2

| Tipo | Origen | Destino | Notas |
|------|--------|---------|-------|
| Agente | **Coordination Professional** | *Staff Route Assigning* | H1 |
| Agente | **Driver** | *Staff Route Assigning* | H1; ejecuta la ruta asignada |
| Transformee | *Staff Route Assigning* | **Route Assignment** | Efecto: `assigned` → `staffed` |
| Requiere | *Staff Route Assigning* | **Healthcare Team** | Para composición del equipo |

#### OPL-EN — B2

```
Staff Route Assigning changes Route Assignment from assigned to staffed.
Staff Route Assigning requires Healthcare Team.
Coordination Professional handles Staff Route Assigning.
Driver handles Staff Route Assigning.
```

#### OPL-ES — B2

```
*Asignar Profesionales a Ruta* cambia **Asignación de Ruta** de `asignada` a `con equipo`.
*Asignar Profesionales a Ruta* requiere **Equipo de Salud**.
**Profesional Coordinador** maneja *Asignar Profesionales a Ruta*.
**Conductor** maneja *Asignar Profesionales a Ruta*.
```

#### Trazabilidad B2

| Elemento | Fuente |
|----------|--------|
| Composición variable del equipo por jornada | Modelo categórico §16.13 — 4 zonas de asignación con equipos diferenciados |
| Healthcare Team como conjunto de profesionales | Metodología OPM §6.5 — Agent link solo humanos; SD (level 0) ya define Healthcare Team |

---

### B3. Visit Sequencing — Secuenciar Visitas

Ordenamiento cronológico y geográfico de las paradas de la jornada (08:00, 09:30, 11:00...) optimizando distancia y ventanas de disponibilidad de pacientes y profesionales. Genera la **Programación Diaria** final y afecta la **Asignación de Ruta** (contea de pacientes por ruta).

#### Tabla de Elementos — B3

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Visit Sequencing* | Informatical | Sistémico | — |
| Objeto | **Daily Schedule** | Informatical | Sistémico | — |
| Agente | **Coordination Professional** | Físico | Sistémico | — |
| Agente | **Driver** | Físico | Sistémico | — |

#### Tabla de Enlaces — B3

| Tipo | Origen | Destino | Notas |
|------|--------|---------|-------|
| Agente | **Coordination Professional** | *Visit Sequencing* | H1 |
| Agente | **Driver** | *Visit Sequencing* | H1; ejecuta la secuencia |
| Resultado | *Visit Sequencing* | **Daily Schedule** | T2; programación horaria final |
| Afecta | *Visit Sequencing* | **Route Assignment** | Conteo y orden de pacientes |

#### OPL-EN — B3

```
Visit Sequencing yields Daily Schedule.
Visit Sequencing affects Route Assignment.
Coordination Professional handles Visit Sequencing.
Driver handles Visit Sequencing.
```

#### OPL-ES — B3

```
*Secuenciar Visitas* genera **Programación Diaria**.
*Secuenciar Visitas* afecta **Asignación de Ruta**.
**Profesional Coordinador** maneja *Secuenciar Visitas*.
**Conductor** maneja *Secuenciar Visitas*.
```

#### Trazabilidad B3

| Elemento | Fuente |
|----------|--------|
| Ventanas horarias (08:00, 09:30, 11:00…) | Modelo categórico §16.13 — datos de programación real |
| Optimización de distancia | Metodología OPM §9.14 — proceso sin objeto geográfico explícito → Patient Home como proxy |

---

### B4. Unrouted Visit Resolving — Resolver Visitas sin Ruta

Las zonas 2-4 de la programación real no tienen conductor asignado de forma estable. Los profesionales se desplazan por cuenta propia o se reasignan dinámicamente a conductores con disponibilidad residual. Este proceso es **condicional**: solo ocurre si existe al menos una **Visita sin Ruta Asignada**.

#### Tabla de Elementos — B4

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Unrouted Visit Resolving* | Informatical | Sistémico | — |
| Objeto | **Unrouted Visit** | Informatical | Sistémico | `unresolved`, `resolved` |
| Objeto | **Daily Schedule** | Informatical | Sistémico | — |
| Agente | **Coordination Professional** | Físico | Sistémico | — |

#### Tabla de Enlaces — B4

| Tipo | Origen | Destino | Notas |
|------|--------|---------|-------|
| Agente | **Coordination Professional** | *Unrouted Visit Resolving* | H1 |
| Transformee | *Unrouted Visit Resolving* | **Unrouted Visit** | CT2: ocurre solo si existe |
| Afecta | *Unrouted Visit Resolving* | **Daily Schedule** | Actualiza la programación con visita reasignada |
| Condición (proceso) | *Unrouted Visit* | *Unrouted Visit Resolving* | CS2: `occurs if Unrouted Visit exists` |

#### OPL-EN — B4

```
Unrouted Visit can be unresolved or resolved.
State unresolved of Unrouted Visit is initial.
Unrouted Visit Resolving occurs if Unrouted Visit exists, in which case Unrouted Visit Resolving changes Unrouted Visit from unresolved to resolved, otherwise Unrouted Visit Resolving is skipped.
Unrouted Visit Resolving affects Daily Schedule.
Coordination Professional handles Unrouted Visit Resolving.
```

#### OPL-ES — B4

```
**Visita sin Ruta Asignada** puede estar `sin resolver` o `resuelta`.
Estado `sin resolver` de **Visita sin Ruta Asignada** es inicial.
*Resolver Visitas sin Ruta* ocurre si **Visita sin Ruta Asignada** existe, en cuyo caso *Resolver Visitas sin Ruta* cambia **Visita sin Ruta Asignada** de `sin resolver` a `resuelta`, de lo contrario *Resolver Visitas sin Ruta* se omite.
*Resolver Visitas sin Ruta* afecta **Programación Diaria**.
**Profesional Coordinador** maneja *Resolver Visitas sin Ruta*.
```

#### Trazabilidad B4

| Elemento | Fuente |
|----------|--------|
| Zonas 2-4 sin conductor estable | Modelo categórico §16.13 — 4 zonas de asignación; zonas 2-4 con disponibilidad irregular |
| Condición de opcionalidad (occurs if) | Metodología OPM §10.1 — Condition link para proceso opcional |
| Profesional se desplaza por cuenta propia | Metodología OPM §6.5 — Driver como agente opcional en estas zonas |

---

### B5. Route Execution Monitoring — Monitorear Ejecución de Rutas

Cierre del ciclo logístico diario. La telemetría GPS permite verificar visitas efectivamente realizadas (match 500m + 120min), detectar anomalías (paradas extra, velocidades excesivas) y calcular la productividad operacional. El **GPS Tracking System** es un instrumento informatical, no un agente.

#### Tabla de Elementos — B5

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Route Execution Monitoring* | Informatical | Sistémico | — |
| Objeto | **Route Execution Report** | Informatical | Sistémico | — |
| Objeto | **Operational Productivity** | Informatical | Sistémico | `below_target`, `on_target`, `above_target` |
| Objeto | **GPS Tracking System** | Informatical | Sistémico | — |
| Agente | **Coordination Professional** | Físico | Sistémico | — |

#### Tabla de Enlaces — B5

| Tipo | Origen | Destino | Notas |
|------|--------|---------|-------|
| Agente | **Coordination Professional** | *Route Execution Monitoring* | H1 |
| Instrumento | *Route Execution Monitoring* | **GPS Tracking System** | H2; instrument, no agent (software/sistema) |
| Resultado | *Route Execution Monitoring* | **Route Execution Report** | T2 |
| Afecta | *Route Execution Monitoring* | **Operational Productivity** | Efecto sobre productividad calculada |

#### OPL-EN — B5

```
Route Execution Monitoring requires GPS Tracking System.
Route Execution Monitoring yields Route Execution Report.
Route Execution Monitoring affects Operational Productivity.
Operational Productivity can be below_target, on_target or above_target.
Coordination Professional handles Route Execution Monitoring.
```

#### OPL-ES — B5

```
*Monitorear Ejecución de Rutas* requiere **Sistema de Rastreo GPS**.
*Monitorear Ejecución de Rutas* genera **Reporte de Ejecución de Rutas**.
*Monitorear Ejecución de Rutas* afecta **Productividad Operacional**.
**Productividad Operacional** puede estar `bajo objetivo`, `en objetivo` o `sobre objetivo`.
**Profesional Coordinador** maneja *Monitorear Ejecución de Rutas*.
```

#### Trazabilidad B5

| Elemento | Fuente |
|----------|--------|
| GPS Tracking System como instrument (no agent) | Metodología OPM §6.5 — software/robots = instrument; agent link = solo humanos |
| Match 500m + 120min | Modelo categórico §16.13 — 87% match programación↔GPS |
| Productividad 39.2% de jornada formal | Modelo categórico §16.13 — productividad operacional real |

---

### Datos de Trazabilidad Cuantitativa — SD1.4a

Los siguientes datos provienen del modelo categórico §16.13 y constituyen la base empírica del diseño del subsistema logístico:

| Dato cuantitativo | Valor | Implicación para el modelo |
|-------------------|-------|---------------------------|
| Vehículos disponibles | 3 (2 cuarto turno L-D; 1 SUV solo L-V) | Restricción hard de capacidad; Operational Mode `extended` requiere vehículo SUV |
| Direcciones geocodificadas | 145 | Patient Home como conjunto finito; geocodificación habilita B1 |
| Eventos GPS en 83 días | 7.587 | GPS Tracking System como instrument informatical con datos reales |
| Match programación↔GPS | 87% | Valida Route Execution Monitoring con alta cobertura |
| Productividad actual | 39.2% de jornada formal | Operational Productivity `below_target` como estado por defecto |
| Capacidad ociosa (bloque 17:30-20:00) | 1.818 horas/trimestre | Oportunidad de mejora: capacidad recuperable |
| Capacidad recuperable | +50-67% (de ~24 a ~36-40 visitas/día) | Productividad mejorable a `on_target` o `above_target` sin recursos adicionales |

> **Nota:** Estos datos constituyen la base para simulación cuantitativa futura (OPM §12). El modelo cualitativo actual establece la estructura; los valores numéricos se incorporan como Transformation Rate en los enlaces de consumo/resultado cuando el modelo se implemente en OPCloud.

---

### OPL-EN Completo — SD1.4a

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

---

### OPL-ES Completo — SD1.4a

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

---

## C. SD1.4b — Refinamiento de *Shift Handover Executing* / *Ejecutar Entrega de Turno*

*Shift Handover Executing* se agrega como subproceso paralelo número 10 de SD1.4. Es el mecanismo de continuidad operacional diario: produce el snapshot clínico más rico de todos los pacientes activos y registra movimientos de altas e ingresos. Se refina en SD1.4b con 3 subprocesos secuenciales.

**Decisión de diseño:** in-zooming secuencial porque la transferencia de responsabilidad clínica requiere que el reporte de estado (C1) y el registro de movimientos (C2) precedan a la transferencia formal de responsabilidad (C3).

**Extensión documentada:** la misma estructura aplica para la entrega de turno de kinesiología, con **Kinesiologist** como agente alternativo del turno saliente. Se indica en nota de trazabilidad.

---

### C1. Active Patient Status Reporting — Reportar Estado de Pacientes Activos

Cada turno saliente produce un snapshot estructurado de cada paciente activo: diagnóstico, tratamientos activos, invasivos, rehabilitación, observaciones y pendientes.

#### Tabla de Elementos — C1

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Active Patient Status Reporting* | Informatical | Sistémico | — |
| Objeto | **Patient Snapshot** | Informatical | Sistémico | `outdated`, `current` |
| Agente | **Clinical Nurse** (turno saliente) | Físico | Sistémico | — |

#### Tabla de Enlaces — C1

| Tipo | Origen | Destino | Notas |
|------|--------|---------|-------|
| Agente | **Clinical Nurse** | *Active Patient Status Reporting* | H1; turno saliente |
| Transformee | *Active Patient Status Reporting* | **Patient Snapshot** | Efecto: `outdated` → `current` |

#### OPL-EN — C1

```
Active Patient Status Reporting changes Patient Snapshot from outdated to current.
Patient Snapshot can be outdated or current.
State outdated of Patient Snapshot is initial.
State current of Patient Snapshot is final.
Clinical Nurse handles Active Patient Status Reporting.
```

#### OPL-ES — C1

```
*Reportar Estado de Pacientes Activos* cambia **Snapshot de Pacientes** de `desactualizado` a `actual`.
**Snapshot de Pacientes** puede estar `desactualizado` o `actual`.
Estado `desactualizado` de **Snapshot de Pacientes** es inicial.
Estado `actual` de **Snapshot de Pacientes** es final.
**Enfermero Clínico** maneja *Reportar Estado de Pacientes Activos*.
```

#### Trazabilidad C1

| Elemento | Fuente |
|----------|--------|
| Snapshot clínico estructurado por paciente | Modelo categórico §16.3 — Entrega de turno (enfermería: 7 columnas por paciente) |
| 7 columnas por paciente | Metodología OPM §9.14 — Patient Snapshot como objeto implícito en el proceso de entrega |

---

### C2. Day Movement Registering — Registrar Movimientos del Día

Registra altas e ingresos del turno, permitiendo trazabilidad de la variación de la población activa entre turnos.

#### Tabla de Elementos — C2

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Day Movement Registering* | Informatical | Sistémico | — |
| Objeto | **Movement Record** | Informatical | Sistémico | — |
| Agente | **Clinical Nurse** (turno saliente) | Físico | Sistémico | — |

#### Tabla de Enlaces — C2

| Tipo | Origen | Destino | Notas |
|------|--------|---------|-------|
| Agente | **Clinical Nurse** | *Day Movement Registering* | H1; turno saliente |
| Resultado | *Day Movement Registering* | **Movement Record** | T2 |

#### OPL-EN — C2

```
Day Movement Registering yields Movement Record.
Clinical Nurse handles Day Movement Registering.
```

#### OPL-ES — C2

```
*Registrar Movimientos del Día* genera **Registro de Movimientos**.
**Enfermero Clínico** maneja *Registrar Movimientos del Día*.
```

#### Trazabilidad C2

| Elemento | Fuente |
|----------|--------|
| Registro de altas e ingresos | Modelo categórico §16.3 — Entrega de turno |
| Movimiento Record como documento operacional | Metodología OPM §6.8 — Objetos de resultado para registro |

---

### C3. Clinical Responsibility Transferring — Transferir Responsabilidad Clínica

Cierre formal de la entrega de turno. El **Estado de Turno** cambia de `pending` a `handed_over`, habilitando al turno entrante para continuar la operación.

#### Tabla de Elementos — C3

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Clinical Responsibility Transferring* | Informatical | Sistémico | — |
| Objeto | **Shift Status** | Informatical | Sistémico | `pending`, `handed_over` |
| Objeto | **Shift Handover Record** | Informatical | Sistémico | — |
| Agente | **Clinical Nurse** (turno saliente) | Físico | Sistémico | — |
| Agente | **Clinical Nurse** (turno entrante) | Físico | Sistémico | — |

#### Tabla de Enlaces — C3

| Tipo | Origen | Destino | Notas |
|------|--------|---------|-------|
| Agente | **Clinical Nurse** (turno saliente) | *Clinical Responsibility Transferring* | H1 |
| Agente | **Clinical Nurse** (turno entrante) | *Clinical Responsibility Transferring* | H1; dual agent para transferencia |
| Transformee | *Clinical Responsibility Transferring* | **Shift Status** | Efecto: `pending` → `handed_over` |
| Resultado | *Clinical Responsibility Transferring* | **Shift Handover Record** | T2 |

#### OPL-EN — C3

```
Clinical Responsibility Transferring changes Shift Status from pending to handed_over.
Shift Status can be pending or handed_over.
State pending of Shift Status is initial.
State handed_over of Shift Status is final.
Clinical Responsibility Transferring yields Shift Handover Record.
Clinical Nurse handles Clinical Responsibility Transferring.
```

#### OPL-ES — C3

```
*Transferir Responsabilidad Clínica* cambia **Estado de Turno** de `pendiente` a `entregado`.
**Estado de Turno** puede estar `pendiente` o `entregado`.
Estado `pendiente` de **Estado de Turno** es inicial.
Estado `entregado` de **Estado de Turno** es final.
*Transferir Responsabilidad Clínica* genera **Registro de Entrega de Turno**.
**Enfermero Clínico** maneja *Transferir Responsabilidad Clínica*.
```

#### Trazabilidad C3

| Elemento | Fuente |
|----------|--------|
| Estructura de entrega de turno (7 columnas paciente + registro FC kinesiología) | Modelo categórico §16.3 — Entrega de Turno |
| Dual agent (turno saliente + entrante) | Metodología OPM §6.5 — ambos son humanos con agent link válido |
| Shift Handover Record como output final | Metodología OPM §6.8 — Result link para objeto creado al completar proceso |

---

### Nota de Extensión — Entrega de Turno de Kinesiología

La misma estructura de SD1.4b aplica para la entrega de turno del equipo de kinesiología, con las siguientes adaptaciones:

| Elemento | Versión Enfermería | Versión Kinesiología |
|----------|-------------------|---------------------|
| Agente (turno saliente) | Clinical Nurse | Kinesiologist |
| Agente (turno entrante) | Clinical Nurse | Kinesiologist |
| Snapshot de estado | Patient Snapshot (diagnóstico, tratamientos, observaciones) | Snapshot Kinésico (COBERTURA, REGISTRO FC — frecuencia cardíaca) |
| Registro específico | Movement Record (altas e ingresos) | Registro de Cobertura Kinésica |

La diferencia de estructura (COBERTURA / REGISTRO FC) respecto a las 7 columnas de enfermería refleja la naturaleza de la prestación kinésica: su entrega de turno registra cobertura de visitas ejecutadas y параметры fisiológicos derivados, no diagnósticos clínicos. Esta distinción se modela como especialización del **Movement Record** o como objeto de resultado propio.

---

### OPL-EN Completo — SD1.4b

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

---

### OPL-ES Completo — SD1.4b

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

---

## Sentencia SD1.4 Actualizada — 10 Subprocesos Paralelos (con Shift Handover)

Con la adición de *Shift Handover Executing*, SD1.4 alcanza **10 subprocesos paralelos**. Se presenta solo la sentencia de descomposición actualizada; los elementos comunes se mantienen del modelo original.

#### OPL-EN SD1.4 (10 paralelos)

```
SD1 is refined by in-zooming Therapeutic Plan Executing in SD1.4.
Therapeutic Plan Executing zooms into parallel Medical Visit Performing, Nursing Care Executing, Kinesiological Therapy Executing, Medication Administering, Remote Care Regulating, Patient and Caregiver Educating, Wound Care Executing, Speech Therapy Executing, Daily Logistics Managing and Shift Handover Executing.
```

#### OPL-ES SD1.4 (10 paralelos)

```
SD1 se refina por descomposición de *Ejecutar Plan Terapéutico* en SD1.4.
*Ejecutar Plan Terapéutico* se descompone en paralelo *Realizar Visita Médica*, *Ejecutar Cuidados de Enfermería*, *Ejecutar Terapia Kinesiológica*, *Administrar Medicamentos*, *Regular Atención a Distancia*, *Educar a Paciente y Cuidador*, *Ejecutar Curación*, *Ejecutar Fonoaudiología*, *Gestionar Logística Diaria* y *Ejecutar Entrega de Turno*.
```

---

## Nota de Trazabilidad al Modelo Categórico

Las siguientes tablas consolidan la trazabilidad de todas las secciones nuevas hacia las fuentes del modelo categórico HODOM v4.1.

### Objetos nuevos y su trazabilidad

| Objeto | Tipo | Trazabilidad categórica | Tipo de esencia |
|--------|------|------------------------|-----------------|
| **Wound Status** | Informatical | §10.6 Registro de Curaciones | Atributo informatical de Patient Group |
| **Wound Care Record** | Informatical | §10.6 Registro de Curaciones; §16.4 Canasta HODOM | Resultado documental |
| **Swallowing and Speech Status** | Informatical | §4.4 tabla de visitas; §16.5 Consolidado | Atributo informatical de Patient Group |
| **Speech Therapy Record** | Informatical | §4.4 tabla de visitas (1.279 fono 2024) | Resultado documental |
| **Operational Mode** | Informatical | §16.5 Consolidado (fono solo días hábiles) | Estado operacional del sistema |
| **Speech Therapist** (agente) | Físico | §4.4; SD2 como complementario → obligatorio aquí | Humano (agent link válido) |
| **Daily Schedule Status** | Informatical | §16.13 Programación Diaria (35 días datos reales) | Atributo de estado del sistema |
| **Daily Schedule** | Informatical | §16.13 Programación Diaria | Resultado documental-logístico |
| **Route Assignment** | Informatical | §16.13 Programación Diaria | Estado transitorio del proceso B |
| **Unrouted Visit** | Informatical | §16.13 (zonas 2-4 sin conductor) | Objeto condicional en B4 |
| **GPS Tracking System** | Informatical | §16.13 (7.587 eventos GPS en 83 días) | Instrumento (software, no agente) |
| **Route Execution Report** | Informatical | §16.13 (87% match prog↔GPS) | Resultado de monitoreo |
| **Operational Productivity** | Informatical | §16.13 (39.2% productividad) | Atributo del sistema |
| **Driver** (agente) | Físico | §16.13 (3 vehículos, 3 conductores) | Humano (agent link válido) |
| **Patient Snapshot** | Informatical | §16.3 Entrega de Turno (7 columnas por paciente) | Snapshot documental |
| **Movement Record** | Informatical | §16.3 Entrega de Turno | Registro transitorio de movimiento |
| **Shift Status** | Informatical | §16.3 Entrega de Turno | Estado formal de entrega |
| **Shift Handover Record** | Informatical | §16.3 Entrega de Turno | Documento formal de transferencia |

### Decisiones de modelamiento y su justificación

| Decisión | Justificación | Referencia OPM |
|----------|--------------|----------------|
| GPS Tracking System como instrument, no agent | §6.5: agent link reservado a humanos; software/sistemas = instrument | §6.5, §15 |
| Speech Therapist como agent obligatorio | Ya existía en SD2 como complementario; aquí es parte integral del programa HODOM con 1.279 visitas/año | §6.5 |
| Dual agent en Clinical Responsibility Transferring | Turno saliente + entrante; ambos humanos con agent link válido | §6.5 |
| In-zooming secuencial en SD1.4a y SD1.4b | Dependencia causal entre subprocesos (B2 requiere B1; C3 requiere C1+C2) | §7.1, §7.2 |
| B4 como proceso condicional (occurs if) | Visitas sin ruta pueden no existir ciertos días; process opcional requiere condition link | §10.1, §10.2 |
| Route Assignment con estado intermedio `staffed` | Transición de `assigned` a `staffed` refleja cambio de estado significativo (agregado de equipo) | §10.9 |
| Patient Home como Requiere en B1 | Geolocalización habilita distribución geográfica de pacientes a rutas | §6.8, §9.14 |
| Operational Productivity como Informatical | Derivada de match GPS y datos cuantitativos; atributo emergente del sistema | §3, §9.5 |

---

## Inventario de OPDs del enriquecimiento

| OPD | Refinamiento | Tipo | Subprocesos | Entidades aprox. |
|-----|-------------|------|-------------|-----------------|
| SD1.4 (actualizado) | Therapeutic Plan Executing | In-zooming paralelo | 10 paralelos | ~40+ entidades |
| SD1.4a | Daily Logistics Managing | In-zooming secuencial | 5 secuenciales | ~16 entidades |
| SD1.4b | Shift Handover Executing | In-zooming secuencial | 3 secuenciales | ~12 entidades |

> **Verificación de complejidad:** SD1.4 contiene 10 subprocesos paralelos; por la regla de complejidad §4.6 y §7.1, se mantiene como diagrama de alto nivel. Los detalles internos se delegan a SD1.4a y SD1.4b, respetando el límite de 20-25 entidades por OPD. SD1.4a (16 entidades) y SD1.4b (12 entidades) cumplen holgadamente el límite de 20-25.
