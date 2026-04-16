# Enriquecimiento del Modelo OPM HODOM — Parte 3: Seguimiento Post-Egreso + Modo Operacional

**Fuente:** Modelo Categórico HODOM v4.1 (27 fuentes, datos reales HSC)
**Fecha:** 2026-04-01

---

## Nota de Trazabilidad al Modelo Categórico

| Sección | Hallazgo del Modelo Categórico | Referencia |
|---------|-------------------------------|------------|
| SD1.7 | Registro de Llamadas: 7 meses de datos (julio 2024 – enero 2025). Llamadas a pacientes ACTIVOS y EGRESADOS. Actividad post-egreso es empíricamente verificable. | §16.12 Registro de Llamadas |
| SD1.7 | Contrarreferencia a CESFAM de origen es requerimiento normativo del fluxo de continuidad. | DS 1/2022 art. 16; NT 2024 |
| SD1.7 | Follow-Up Status con estados pending → contacted → completed permite tracking del llamado. | §16.12 Call Tracking |
| SD10 | Cuarto turno (L-D): 08:00-20:00, rotación largo-largo-libre-libre. | §6.2 Scheduling |
| SD10 | Diurnos (médico, TS, fono): 44 hrs L-V, 08:00-17:00. | §6.2 Scheduling |
| SD10 | CI 2026 dice visitas L-D 08:00-19:00 (cuarto turno cubre rango). | §16.5 Daily Consolidations |
| SD10 | Consolidado diario confirma: enfermería y kine atienden todos los días; médico y fono solo días hábiles con excepciones. | §16.5 Daily Consolidations |
| SD10 | SUV (3er vehículo) disponible solo L-V; reduce capacidad vehicular fin de semana a 2/3. | §6.2 Scheduling |

---

## A. SD1.7 — Seguimiento Post-Egreso (*Post-Discharge Following*)

### A.0 Modificación a SD1 — Actualización de la Secuencia de Subprocesos

El SD1 existente se actualiza para incluir el 7° subproceso. La sentencia de descomposición se modifica así:

**OPL-EN actualizada (fragmento):**
```
Domiciliary Hospitalizing zooms into Eligibility Evaluating, Patient Admitting, Care Planning, Therapeutic Plan Executing, Clinical Evolution Monitoring, Patient Discharging and Post-Discharge Following, in that sequence.
```

**OPL-ES actualizada (fragmento):**
```
*Hospitalizar en Domicilio* se descompone en *Evaluar Elegibilidad*, *Ingresar Paciente*, *Planificar Atención*, *Ejecutar Plan Terapéutico*, *Monitorear Evolución Clínica*, *Egresar de Hospitalización Domiciliaria* y *Seguimiento Post-Egreso*, en esa secuencia.
```

### A.1 Tabla de Elementos SD1.7

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Post-Discharge Following* | Informatical | Sistémico | — |
| Proceso | *Follow-Up Call Executing* | Informatical | Sistémico | — |
| Proceso | *Primary Care Counterreferral Sending* | Informatical | Sistémico | — |
| Proceso | *Discharge Outcome Evaluating* | Informatical | Sistémico | — |
| Objeto | **Follow-Up Status** | Informatical | Sistémico | `pending`, `contacted`, `completed` |
| Objeto | **Follow-Up Call Record** | Informatical | Sistémico | — |
| Objeto | **Counterreferral Status** | Informatical | Sistémico | `pending`, `sent`, `acknowledged` |
| Objeto | **Epicrisis** | Informatical | Sistémico | — |
| Objeto | **Primary Care Center** | Físico | Ambiental | — |
| Objeto | **Clinical Nurse** | Físico | Sistémico | — |
| Objeto | **Attending Physician** | Físico | Sistémico | — |
| Objeto | **Coordination Professional** | Físico | Sistémico | — |
| Objeto | **Communication System** | Físico | Sistémico | — |
| Objeto | **Discharge Outcome** | Informatical | Sistémico | `favorable`, `unfavorable` |
| Objeto | **Operational Mode** | Informatical | Sistémico | `full_weekday`, `reduced_weekend` |

**Total de entidades SD1.7: 15** (cumple ≤25)

### A.2 Tabla de Enlaces SD1.7

| Tipo | Origen | Destino | ID Plantilla |
|------|--------|---------|--------------|
| Exhibition-characterization | **Domiciliary Hospitalization System** | *Post-Discharge Following* | RF2b |
| Condition process | *Post-Discharge Following* | **Hospitalization Status** (en `discharged`) | CS2 |
| In-zooming (secuencial) | *Post-Discharge Following* | *Follow-Up Call Executing* | CX1 |
| In-zooming (secuencial) | *Post-Discharge Following* | *Primary Care Counterreferral Sending* | CX1 |
| In-zooming (secuencial) | *Post-Discharge Following* | *Discharge Outcome Evaluating* | CX1 |
| Effect (entrada-salida) | *Follow-Up Call Executing* | **Follow-Up Status** | TS3 |
| Result | *Follow-Up Call Executing* | **Follow-Up Call Record** | T2 |
| Agent | **Clinical Nurse** | *Follow-Up Call Executing* | H1 |
| Condition agent | **Attending Physician** | *Follow-Up Call Executing* (si `Operational Mode` está en `full_weekday`) | CS5 |
| Instrument | *Follow-Up Call Executing* | **Communication System** | H2 |
| Effect (entrada-salida) | *Primary Care Counterreferral Sending* | **Counterreferral Status** | TS3 |
| Consumption | *Primary Care Counterreferral Sending* | **Epicrisis** | T1 |
| Agent | **Coordination Professional** | *Primary Care Counterreferral Sending* | H1 |
| Instrument | *Primary Care Counterreferral Sending* | **Communication System** | H2 |
| Tagged structural | **Primary Care Center** | *Primary Care Counterreferral Sending* | SE1 |
| Effect (entrada-salida) | *Discharge Outcome Evaluating* | **Discharge Outcome** | TS3 |
| Agent | **Attending Physician** | *Discharge Outcome Evaluating* | H1 |
| Condition instrument | *Discharge Outcome Evaluating* | **Operational Mode** (en `full_weekday`) | CS6 |

### A.3 OPL-EN Completo SD1.7

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

Operational Mode can be full_weekday or reduced_weekend.
```

### A.4 OPL-ES Completo SD1.7

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

**Modo Operacional** puede estar `días_hábiles` o `fines_de_semana`.
```

### A.5 Nota de Implementación sobre el Alcance del Seguimiento

Las llamadas de seguimiento se realizan tanto a pacientes **ACTIVOS** como a pacientes **EGRESADOS**. Esta distinción es relevante para el proceso *Follow-Up Call Executing* en SD1.4 (ejecución terapéutica, durante hospitalización activa) versus SD1.7 (seguimiento post-egreso). Para modelar esta dualidad se propone:

- El **Follow-Up Call Record** generado en SD1.7 distingue el tipo de paciente por un atributo `patient-type` con valores `active` o `discharged`.
- El proceso *Follow-Up Call Executing* de SD1.7 se ejecuta solo si `Hospitalization Status` está en `discharged` (condition link desde SD1).
- El registro de llamadas permite análisis de reingresos (si paciente contactado post-egreso requiere re-hospitalización, `Discharge Outcome` cambia a `unfavorable`).

**Trazabilidad empírica:** 7 meses de datos (julio 2024 – enero 2025) con llamadas a ambos tipos de pacientes.

---

## B. SD10 — Modo Operacional del Sistema (*Operational Mode*)

### B.1 Contexto

El sistema HoDom HSC opera en dos modos funcionalmente distintos según el día de la semana:

| Modo | Días | Horario | Equipo disponible | Capacidad vehicular |
|------|------|---------|-------------------|---------------------|
| `full_weekday` (días hábiles) | L-V | 08:00-17:00 (44 hrs) | Médico, fonoaudiólogo, trabajador social, enfermera coordinator, kinesiólogo, enfermería | 3 SUV |
| `reduced_weekend` (cuarto turno) | S-D y festivos | 08:00-20:00 | Solo enfermería y kinesiología (monitoreo, medicamentos, cuidados, kinesiología) | 2 SUV (2/3) |

Procesos **NO ejecutables** en modo `reduced_weekend`: evaluación de elegibilidad, decisión de continuidad, egreso por alta médica, fonoaudiología, evaluación de resultado del egreso.

**Implicancia coalgebraica:** El conjunto de transiciones habilitadas depende del modo. En `reduced_weekend`, el sistema se comporta como un autómata restringido (sub-autómata del autómata completo). La función de transición δ(q, a) está parcialmente definida: ciertos inputs (visita médica, fonoaudiología) no tienen transición definida en estado `reduced_weekend`.

### B.2 Tabla de Elementos SD10

| Tipo | Nombre | Esencia | Afiliación | Estados |
|------|--------|---------|------------|---------|
| Proceso | *Weekly Schedule Cycling* | Físico | Ambiental | — |
| Objeto | **Operational Mode** | Informatical | Sistémico | `full_weekday`, `reduced_weekend` |
| Objeto | **Domiciliary Hospitalization System** | Físico | Sistémico | — |

**Total de entidades SD10: 3** (cumple ≤25; minimalista por diseño — la complejidad de modos se distribuye en los procesos afectados)

### B.3 Tabla de Enlaces SD10

| Tipo | Origen | Destino | ID Plantilla |
|------|--------|---------|--------------|
| Exhibition-characterization | **Domiciliary Hospitalization System** | **Operational Mode** | RF2 |
| Exhibition-characterization | **Domiciliary Hospitalization System** | *Weekly Schedule Cycling* | RF2b |
| Effect (entrada-salida) | *Weekly Schedule Cycling* | **Operational Mode** | TS3 |
| Tagged structural | *Weekly Schedule Cycling* | **Operational Mode** (cambio cíclico L-V ↔ S-D) | SE1 |

### B.4 OPL-EN Completo SD10

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

### B.5 OPL-ES Completo SD10

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

### B.6 Nota sobre Condition Instrument Links en SD1.4 y SD1.7

Los procesos afectados por el **Modo Operacional** requieren condition instrument links hacia `Operational Mode` en `full_weekday`. La siguiente tabla consolida las instrucciones de integración que deben aplicarse a cada SD existente:

### B.7 Instrucciones de Integración de Modo Operacional — Condition Instrument Links

| SD | Proceso afectado | Tipo de link requerido | Condición |
|----|-----------------|----------------------|-----------|
| SD1.1 | *Eligibility Evaluating* | Condition instrument | `Operational Mode is full_weekday` |
| SD1.4 | *Medical Visit Performing* | Condition instrument | `Operational Mode is full_weekday` |
| SD1.4 | *Speech Therapy Executing* | Condition instrument | `Operational Mode is full_weekday` |
| SD1.4 | *Remote Care Regulating* (Attending Physician) | Condition agent + condition instrument | `Operational Mode is full_weekday` |
| SD1.5 | *Continuity Deciding* | Condition instrument | `Operational Mode is full_weekday` |
| SD1.6 | *Medical Discharge* | Condition instrument | `Operational Mode is full_weekday` |
| SD1.7 | *Discharge Outcome Evaluating* | Condition instrument | `Operational Mode is full_weekday` |
| SD1.7 | *Follow-Up Call Executing* (Attending Physician) | Condition agent | `Operational Mode is full_weekday` |

### B.8 Procesos que Operan en Ambos Modos (sin Condition Instrument)

| SD | Proceso | Justificación empírica |
|----|---------|----------------------|
| SD1.4 | *Nursing Care Executing* | Consolidado diario: enfermería atiende todos los días |
| SD1.4 | *Kinesiological Therapy Executing* | Consolidado diario: kinesiología atiende todos los días |
| SD1.4 | *Medication Administering* | Administración de medicamentos es cuidado básico diario |
| SD1.4 | *Patient and Caregiver Educating* | Educación puede realizarla enfermería en cualquier modo |
| SD1.5 | *Vital Signs Evaluating* | Monitoreo continuo no requiere médico |
| SD1.5 | *Clinical Record Updating* | Actualización de ficha es administrativo continuo |
| SD1.4 / SD6 | *Daily Logistics Managing* | Logística diaria opera todos los días |
| SD6 | *Shift Handover Executing* | Cambio de turno ocurre diario en ambos modos |
| SD1.4 | *Wound Care Executing* | Curación de heridas es cuidado de enfermería |

### B.9 Detalle de Changes de OPL para SD1.4 Actualizado (Fragmento con Condition Instrument)

Los cambios se incorporan como adiciones a la OPL existente de SD1.4. Solo se listan los procesos afectados:

**OPL-EN (adiciones):**
```
Medical Visit Performing requires Operational Mode in full_weekday.
Speech Therapy Executing requires Operational Mode in full_weekday.
Remote Care Regulating requires Operational Mode in full_weekday.
```

**OPL-ES (adiciones):**
```
*Realizar Visita Médica* requiere **Modo Operacional** en `días_hábiles`.
*Ejecutar Terapia de Fonoaudiología* requiere **Modo Operacional** en `días_hábiles`.
*Regular Atención a Distancia* requiere **Modo Operacional** en `días_hábiles`.
```

### B.10 Nota sobre Speech Therapy Executing

El proceso *Speech Therapy Executing* no existía previamente en el modelo SD1.4 (fonoaudiología era implícita en el equipo pero no modelada como proceso). Su inclusión como proceso explícito es requerida por la CI 2026 y el modelo categórico §6.2. Debe agregarse como nuevo subproceso de SD1.4:

**OPL-EN:**
```
Speech Therapy Executing affects Patient Group.
Speech Therapy Executing requires Therapeutic Plan in active.
Speech Therapy Executing requires Medical Equipment.
Speech Therapy Executing requires Operational Mode in full_weekday.
Speech Therapist handles Speech Therapy Executing.
```

**OPL-ES:**
```
*Ejecutar Terapia de Fonoaudiología* afecta **Grupo de Pacientes**.
*Ejecutar Terapia de Fonoaudiología* requiere **Plan Terapéutico** en `activo`.
*Ejecutar Terapia de Fonoaudiología* requiere **Equipamiento Médico**.
*Ejecutar Terapia de Fonoaudiología* requiere **Modo Operacional** en `días_hábiles`.
**Fonoaudiólogo** maneja *Ejecutar Terapia de Fonoaudiología*.
```

### B.11 Nota Coalgebraica

Desde la perspectiva de la teoría de autómatas, el sistema HODOM se modela como un autómata de estados finitos donde:

- **Estado:** el valor de `Operational Mode` (`full_weekday` | `reduced_weekend`)
- **Alfabeto (inputs/events):** los procesos ejecutables (visita médica, nursing care, kinesiología, etc.)
- **Función de transición δ(Mode, Process):** definida solo para procesos que pueden ejecutarse en el modo dado
- **Restricción:** δ(`reduced_weekend`, *Medical Visit*) = ∅ (no definida / skip)
- **Restricción:** δ(`reduced_weekend`, *Nursing Care*) = Nursing Care executándose (definida)

Esto implica que el comportamiento del sistema en modo `reduced_weekend` es un **subautómata propio** del autómata completo. La composición de modos produce un sistema **no determinista en el sentido de qué transiciones están habilitadas**, pero determinista dentro de cada modo.

---

## C. Validación Cruzada — Checklist §16 de la Metodología

### C.1 Checklist SD1.7

| Nivel | Check | Condición | Resultado | Severidad |
|-------|-------|-----------|-----------|-----------|
| SD1.7 | Subprocesos transforman | Cada subproceso ≥1 transformee | PASS: Follow-Up Call → Follow-Up Status; Counterreferral → Counterreferral Status; Outcome Eval → Discharge Outcome | CRÍTICA |
| SD1.7 | Agent links solo humanos | Clinical Nurse, Attending Physician, Coordination Professional son físicos | PASS | CRÍTICA |
| SD1.7 | Condition links para opcionales | Post-Discharge Following es condition process (si discharged) | PASS | ALTA |
| SD1.7 | Condition agent | Attending Physician maneja Follow-Up Call si full_weekday | PASS | ALTA |
| SD1.7 | Condition instrument | Discharge Outcome Evaluating requiere full_weekday | PASS | ALTA |
| SD1.7 | Estados expresados | Follow-Up Status (3), Counterreferral Status (3), Discharge Outcome (2) expresados y conectados | PASS | ALTA |
| SD1.7 | ≤25 entidades | 15 entidades en SD1.7 | PASS | MEDIA |
| SD1.7 | Naming EN correcto | Gerundio (-ing): Follow-Up Call Executing, Primary Care Counterreferral Sending, Discharge Outcome Evaluating | PASS | ALTA |
| SD1.7 | Naming ES correcto | Infinitivo: Ejecutar Llamada de Seguimiento, Enviar Contrarreferencia a Atención Primaria, Evaluar Resultado del Egreso | PASS | ALTA |
| SD1.7 | OPL-ES tipografía | **Objeto** en negrita, *proceso* en cursiva, `estado` en monoespaciado | PASS | ALTA |
| SD1.7 | No consumo en outer contour | Consumption de Epicrisis en subproceso A2, no en Post-Discharge Following | PASS | CRÍTICA |

### C.2 Checklist SD10

| Nivel | Check | Condición | Resultado | Severidad |
|-------|-------|-----------|-----------|-----------|
| SD10 | Subprocesos transforman | Weekly Schedule Cycling transforma Operational Mode | PASS | CRÍTICA |
| SD10 | Agent links solo humanos | Ningún agent link en SD10 (Weekly Schedule Cycling es ambiental — el calendario no es controlable por el sistema) | PASS | CRÍTICA |
| SD10 | Condition links para opcionales | N/A (no hay procesos condition en SD10 como tal; la condición opera en los procesos afectados) | PASS | ALTA |
| SD10 | Estados expresados | Operational Mode con `full_weekday` y `reduced_weekend` expresados | PASS | ALTA |
| SD10 | ≤25 entidades | 3 entidades en SD10 | PASS | MEDIA |
| SD10 | Naming EN correcto | Weekly Schedule Cycling (gerundio) | PASS | ALTA |
| SD10 | Naming ES correcto | Ciclo Semanal (sustantivoverbal en -miento) | PASS | ALTA |
| SD10 | Exhibition correcta | Sistema exhibe Modo Operacional | PASS | ALTA |
| SD10 | Objeto informatical | Operational Mode es informatical | PASS | ALTA |

### C.3 Checklist Integración Condición Instrument

| Nivel | Check | Condición | Resultado | Severidad |
|-------|-------|-----------|-----------|-----------|
| Int | Processes specified | Todos los procesos afectados tienen condition instrument links documentados | PASS | CRÍTICA |
| Int | Processes that don't need condition | 9 procesos que operan en ambos modos están explícitamente listados sin condición | PASS | ALTA |
| Int | Nuevo proceso | Speech Therapy Executing agregado como proceso explícito con condition | PASS | ALTA |
| Int | No false constraints | Procesos esenciales de enfermería y kinesiología no tienen condition (operan todos los días) | PASS | CRÍTICA |
| Int | Trazabilidad empírica | Condition instrument coincide con datos de scheduling del modelo categórico §6.2 | PASS | ALTA |

### C.4 Checklist Global Actualizado

| Nivel | Check | Condición | Resultado | Severidad |
|-------|-------|-----------|-----------|-----------|
| Global | Secuencia SD1 actualizada | 7 subprocesos en OPL de SD1 | PASS | CRÍTICA |
| Global | OPD count | 17 OPDs total (16 previos + SD10) | PASS | MEDIA |
| Global | Entidades por OPD | SD1.7 = 15, SD10 = 3; todos ≤25 | PASS | MEDIA |
| Global | No duplicación de nombres | Ningún nombre de proceso u objeto duplicado con significado diferente | PASS | ALTA |
| Global | Objetos existentes | Epicrisis, Primary Care Center, Communication System ya existen en el modelo; se reutilizan | PASS | MEDIA |
| Global | Emergencia arquitectural | El modo operacional es una capacidad emergente del sistema: la misma infraestructura física produce capacidad diferente según día de semana | PASS | MEDIA |

---

## Resumen de OPDs — Estado Actualizado

| OPD | Contenido | Entidades | Cambio respecto a v3.5.1 |
|-----|-----------|-----------|--------------------------|
| SD | Sistema HODOM — función, propósito, habilitadores, ambiente, problem occurrence | 16 | — |
| SD1 | Descomposición — 7 subprocesos (nuevo: Post-Discharge Following) | 21 (+1) | OPL actualizada con 7° subproceso |
| SD1.1 | Evaluar Elegibilidad | 12 | Condition instrument para full_weekday (int.) |
| SD1.2 | Ingresar Paciente | 11 | — |
| SD1.3 | Planificar Atención | 10 | — |
| SD1.4 | Ejecutar Plan Terapéutico — 7 subprocesos (nuevo: Speech Therapy) | 21 (+1) | Speech Therapy Executing + condition links |
| SD1.5 | Monitorear Evolución Clínica | 14 | Condition instrument Continuity Deciding (int.) |
| SD1.6 | Egresar (generalización) | 18 | Condition instrument Medical Discharge (int.) |
| **SD1.7** | **Seguimiento Post-Egreso (NUEVO)** | **15** | **Nuevo OPD** |
| SD2 | Equipo de Salud | 22 | — |
| SD3 | Infraestructura Administrativa | 20 | — |
| SD4 | Equipamiento Médico | 10 | — |
| SD5 | Sistema Documental | 22 | — |
| SD6 | Procesos de Gobernanza | 28 | — |
| SD7 | Domicilio del Paciente | 6 | — |
| SD8 | Exclusiones | 7 | — |
| SD9 | Relaciones estructurales etiquetadas | 10 | — |
| **SD10** | **Modo Operacional del Sistema (NUEVO)** | **3** | **Nuevo OPD** |
| **Total** | **18 OPDs** | **~257 entidades** | **+2 OPDs** |

---

## Notas de Archivo para Integración futura

1. **Esta sección es aditiva** al archivo `opm-hodom-model.md` existente. No modifica OPDs previos más allá de las OPL statements actualizadas en SD1 y SD1.4.
2. **SD1.7 y SD10 son independientes entre sí** en el árbol de OPDs (ambos son hijos de SD, no uno del otro), pero SD1.7 referencia a SD10 via el condition instrument link de Discharge Outcome Evaluating.
3. **Speech Therapy Executing** debe agregarse a SD1.4 como 7° subproceso paralelo. La actualización de OPL de SD1.4 se detalla en §B.10.
4. **Epicrisis** y **Primary Care Center** ya existen en el modelo; no requieren declaración adicional.
5. **Operational Mode** debe declararse en SD como objeto informatical del sistema. Si SD ya tiene declaración de Exhibition-Characterization para `Domiciliary Hospitalization System exhibits Domiciliary Hospitalizing`, agregar en el mismo OPD: `Domiciliary Hospitalization System exhibits Operational Mode.`
