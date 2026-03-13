---
_manifest:
  urn: "urn:pro:kb:gestion-redes-unidades"
  provenance:
    created_by: "FS"
    created_at: "2026-03-03"
    source: "Síntesis multi-fuente: OPS, IHI, NICE, AHRQ, MINSAL, Cochrane, NotebookLM 46 fuentes HaH"
version: "2.0.0"
status: draft
tags: [gestion-redes, unidades, ambulatorio, hospitalario, hospital-at-home, HaH, asistencial]
lang: es
---

# Gestión de Redes Asistenciales — Gestión por Tipo de Unidad

## 15. Unidades ambulatorias y de apoyo

### 15.1 APS/CESFAM/Clínicas comunitarias

Primer contacto y resolutividad. Modelo de Atención Integral de Salud (MAIS) con enfoque familiar y comunitario, equipos de sector adscritos territorialmente, cartera APS definida por norma. Continuidad longitudinal como eje.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Modelo MAIS | Enfoque biopsicosocial, equipo de cabecera, ciclo vital, participación comunitaria |
| Cartera APS | Prestaciones definidas MINSAL: controles, crónicos, EMPA/EFAM, GES, urgencia |
| Equipo de sector | Médico, enfermera, matrona, TENS, trabajador social — panel 3.500-5.000 inscritos |
| Continuidad longitudinal | Médico de cabecera asignado, agenda protegida, seguimiento proactivo |
| Derivación-contrarreferencia | Protocolo bidireccional con nivel secundario, trazabilidad electrónica |
| Programa crónicos | PSCV, DM2, HTA, asma/EPOC — estratificación riesgo, controles programados |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cobertura efectiva PSCV | Compensados / Total inscritos PSCV × 100 | ≥50 % | OCDE 55-65 % | MINSAL 2023 | Trimestral |
| Contrarreferencia oportuna | Contrarreferencias recibidas ≤7d / Total derivaciones × 100 | ≥80 % | — | MINSAL 2019 | Mensual |
| Control crónicos compensados | HbA1c <7 % (DM2) + PA <140/90 (HTA) / Total inscritos × 100 | ≥50 % | UK QOF 60-70 % | NHS QOF 2023 | Trimestral |
| Resolutividad APS | Consultas resueltas sin derivar / Total consultas × 100 | ≥85 % | OCDE 85-90 % | OCDE 2023 | Trimestral |
| Consultas urgencia evitable | Consultas SUH categoría C4-C5 de población inscrita / Total consultas SUH × 100 | ≤30 % | — | MINSAL 2022 | Mensual |
| EMPA/EFAM cobertura | Exámenes realizados / Población meta × 100 | ≥50 % | — | MINSAL 2023 | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Baja resolutividad → sobreuso urgencia | Telemedicina, eConsult, ecografía point-of-care en APS |
| Pérdida de seguimiento crónicos | Alerta automática en HCE, rescate telefónico, visita domiciliaria |
| Rotación profesional alta | Incentivos zona, formación en servicio, ratio ≤1:4.000 inscritos |
| Fragmentación información | HCE compartida con nivel secundario, interoperabilidad FHIR |

Ref: Modelo de Atención Integral de Salud Familiar y Comunitaria MINSAL 2013; Ley 19.378 (Estatuto APS); OMS PHC 2018; Starfield 1998.

### 15.2 Centros de especialidad ambulatoria/CRS

Concentración de especialidades ambulatorias con modelo de triaje de interconsultas, gestión activa de listas de espera y maximización de productividad por box. eConsult como estrategia de resolución sin presencialidad.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Triaje de interconsultas | Priorización clínica (P1: <30d, P2: <90d, P3: <180d), rechazo justificado con retroalimentación a APS |
| Gestión listas de espera | Tablero por especialidad, depuración periódica, contactabilidad, oferta-demanda |
| Productividad box | Rendimiento hora/médico, agendas protegidas, control ausentismo |
| eConsult/telemedicina | Resolución asincrónica especialista-APS, evita derivación innecesaria |
| Coordinación SOME | Central de agendamiento integrada, confirmación telefónica/SMS |
| Exámenes previos | Protocolo de preparación, paquetes diagnósticos por patología |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Espera mediana por especialidad | Mediana días desde IC aceptada hasta atención | ≤90 d (P2) | UK RTT 62 % <18 wk | MINSAL-SIGTE 2023 | Mensual |
| Productividad agenda | Pacientes atendidos / Cupos agendados × 100 | ≥85 % | — | MINSAL 2022 | Mensual |
| eConsult resolución | eConsult resueltas sin presencial / Total eConsult × 100 | ≥30 % | UCSF 40-70 % | AHRQ 2021 | Trimestral |
| Ausentismo consulta | Inasistencias / Citados × 100 | ≤15 % | NHS 5-8 % | NHS England 2023 | Mensual |
| IC rechazadas con retroalimentación | IC rechazadas con informe / Total IC rechazadas × 100 | 100 % | — | Buena práctica | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Listas de espera crecientes | Priorización clínica, oferta complementaria (telemedicina, compra servicios) |
| Ausentismo alto | Confirmación 48h antes (SMS/IVR), sobre-agendamiento controlado |
| IC innecesarias | Protocolos de referencia APS, eConsult, capacitación bidireccional |

Ref: Orientaciones Técnicas Listas de Espera MINSAL 2022; NICE NG94 referral guidelines 2023; AHRQ eConsult evidence 2021.

### 15.3 Hospital de día médico/quirúrgico

Atención de procedimientos y tratamientos que requieren observación <12h sin pernocta. Selección rigurosa de casos, protocolos fast-track y alta segura mismo día.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Selección de casos | Criterios ASA I-II, procedimiento compatible, red apoyo domiciliario |
| Protocolos fast-track | Ayuno mínimo, analgesia multimodal, movilización precoz, alta criterios |
| Circuito paciente | Admisión → preparación → procedimiento → recuperación → alta con indicaciones |
| Gestión de sillones/camas día | Programación por bloques, rotación AM/PM, overbooking controlado |
| Quimioterapia ambulatoria | Protocolos oncología, premedicación, monitoreo reacciones |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cancelaciones mismo día | Cancelaciones / Programados × 100 | <5 % | BADS UK 3-5 % | BADS 2022 | Mensual |
| Complicaciones <72h | Pacientes con complicación / Total atendidos × 100 | <2 % | BADS UK 1-2 % | AHRQ 2021 | Mensual |
| Ocupación silla/cama día | Horas ocupadas / Horas disponibles × 100 | ≥80 % | — | NICE 2019 | Mensual |
| Conversión a hospitalización | Pacientes que requieren pernocta / Total × 100 | <3 % | — | BADS 2022 | Mensual |
| Satisfacción paciente | Score encuesta post-atención | ≥85 % | — | IHI 2022 | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Complicación post-alta sin supervisión | Llamada telefónica 24h, indicaciones escritas, línea emergencia |
| Selección inadecuada de pacientes | Checklist criterios estandarizado, evaluación preanestésica |
| Cancelaciones por falta de insumos | Stock mínimo protegido, gestión abastecimiento dedicada |

Ref: BADS (British Association of Day Surgery) Directory 2022; NICE CG45; IAAS International Association for Ambulatory Surgery 2021.

### 15.4 Imagenología, teleradiología

Servicios de diagnóstico por imagen (RX, US, CT, RM) con priorización clínica, integración RIS/PACS/HIS y cobertura teleradiología para centros remotos.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Priorización clínica | Urgente (<1h informe), preferente (<24h), rutina (<48-72h) |
| RIS/PACS/HIS | Integración trazabilidad solicitud-imagen-informe, DICOM, HL7/FHIR |
| Teleradiología | Lectura remota para centros sin radiólogo presencial, 24/7 |
| Protocolos contraste | Evaluación función renal, consentimiento, manejo reacción adversa |
| Control dosis radiación | DLP/CTDIvol registro, auditoría ALARA, niveles referencia diagnósticos |
| Mantención equipos | Plan mantención preventiva, certificación ISP, obsolescencia programada |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Turnaround informe (urgente) | Mediana tiempo solicitud→informe definitivo | <1 h | ACR <1h crítico | ACR 2020 | Mensual |
| Turnaround informe (rutina) | Mediana tiempo solicitud→informe definitivo | <48 h | — | ACR 2020 | Mensual |
| Repeat rate | Exámenes repetidos / Total exámenes × 100 | <5 % | ACR <5 % | ACR 2020 | Trimestral |
| Incidentes contraste | Reacciones adversas / Total exámenes con contraste × 100 | <1 % | 0.2-0.7 % | ACR Manual Contrast 2021 | Trimestral |
| Disponibilidad equipos | Horas operativas / Horas programadas × 100 | ≥95 % | — | OMS 2017 | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Demora informes críticos | Alerta automática hallazgos críticos (ACR), comunicación directa con clínico |
| Falla PACS/pérdida imagen | Redundancia almacenamiento, backup diario, disaster recovery |
| Sobreuso CT/RM | Criterios de pertinencia (ACR Appropriateness Criteria), auditoría |

Ref: ACR Practice Parameters 2020; ACR Appropriateness Criteria; MINSAL Orientaciones Imagenología 2019; ISP regulación equipos.

### 15.5 Laboratorio clínico y bancos de sangre

Gestión del ciclo pre-analítico → analítico → post-analítico con control TAT por tipo de prueba, seguridad transfusional y acreditación.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Fase pre-analítica | Identificación positiva, toma de muestra estandarizada, transporte cadena frío |
| TAT por tipo | Urgentes <1h, rutina <4h ambulatorio / <24h hospitalizado, especializados según protocolo |
| Control calidad | QC interno diario, programa externo (PEEC), acreditación ISO 15189 |
| Banco de sangre | Tamizaje, tipificación, compatibilidad, hemovigilancia, stock mínimo por grupo |
| LIS/HIS integración | Resultados automáticos en HCE, alertas valores críticos, delta-check |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| TAT p90 (urgente) | Percentil 90 tiempo recepción→resultado | <60 min | CAP <60 min | CAP 2022 | Mensual |
| Tasa hemólisis | Muestras hemolizadas / Total muestras × 100 | <2 % | CAP <2 % | CAP 2022 | Mensual |
| Stock hemocomponentes | Días cobertura por grupo sanguíneo | ≥3 d | OMS ≥3d | OMS Blood Safety 2022 | Semanal |
| Valores críticos notificados <30 min | Notificados en tiempo / Total valores críticos × 100 | ≥95 % | CAP 95 % | CAP 2022 | Mensual |
| Reacciones transfusionales | Reacciones / Total transfusiones × 100 | <0.5 % | 0.1-0.3 % | AABB 2023 | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Error identificación muestra | Pulsera + verificación positiva en cabecera, código de barras |
| Desabastecimiento hemocomponentes | Red de bancos, convenios interinstitucionales, stock seguridad |
| Resultado erróneo por interferencia | Delta-check automático, QC diario, repetición ante discordancia |

Ref: ISO 15189:2022; CAP Accreditation Checklist 2022; AABB Standards 2023; MINSAL Norma Técnica Bancos de Sangre.

### 15.6 Farmacia clínica y logística de medicamentos

Trazabilidad completa del medicamento, conciliación en transiciones asistenciales, gestión diferenciada de medicamentos de alto riesgo (MAR) y dispensación segura.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Trazabilidad | Recepción → almacenamiento → dispensación → administración, código de barras/RFID |
| Conciliación medicamentosa | Ingreso, traslado, alta — listado completo verificado con paciente/cuidador |
| Medicamentos alto riesgo (MAR) | ISMP lista, almacenamiento segregado, doble verificación, etiquetado especial |
| Dispensación unitaria | Dosis unitaria, carro automatizado (Pyxis/Omnicell), verificación farmacéutica |
| Farmacovigilancia | Notificación RAM, análisis causalidad, reporte ISP |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Errores medicación | Errores detectados / 1.000 prescripciones | <5 ‰ | ISMP <5 ‰ | ISMP 2022 | Mensual |
| Stock-out medicamentos esenciales | Días con quiebre / Días totales × 100 | <2 % | — | OMS 2022 | Mensual |
| Conciliación al ingreso | Pacientes con conciliación completa / Ingresos × 100 | ≥90 % | IHI 95 % | IHI 2022 | Mensual |
| Conciliación al alta | Pacientes con conciliación + educación / Altas × 100 | ≥85 % | — | NICE NG5 2015 | Mensual |
| Cumplimiento MAR | Auditoría doble-check MAR cumplido / Total MAR × 100 | ≥95 % | — | ISMP 2022 | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Error de prescripción | CPOE con alertas, farmacéutico clínico en ronda |
| Quiebre stock crítico | Stock seguridad, alternativas terapéuticas predefinidas, compra de emergencia |
| Omisión conciliación en transiciones | Automatización alerta HCE en ingreso/traslado/alta |

Ref: ISMP High-Alert Medications 2022; NICE NG5 Medicines Optimisation 2015; OMS Medication Without Harm 2017; Ley 20.724 (Farmacovigilancia Chile).

### 15.7 Esterilización (CME)

Central de mezclas estériles y esterilización de instrumental. Flujos unidireccionales sucio→limpio, trazabilidad completa set-paciente-procedimiento, control biológico.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Flujo sucio-limpio | Unidireccional: recepción → lavado → inspección → empaque → esterilización → almacén estéril |
| Trazabilidad | Código de barras por set, registro ciclo-autoclave-lote, vinculación paciente-procedimiento |
| Control biológico | Indicador biológico cada carga (Geobacillus stearothermophilus), integrador químico clase 5/6 |
| Mantención autoclaves | Plan preventivo, calificación IQ/OQ/PQ, registro parametría cada ciclo |
| Instrumental externo/préstamo | Protocolo recepción, reprocesamiento completo, cuarentena |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Fallas esterilidad | Indicadores biológicos positivos / Total cargas × 100 | 0 % | 0 % | AAMI ST79 | Por carga |
| Rotación set quirúrgico | Sets utilizados / Sets disponibles | ≥2 rotaciones/d | — | AORN 2022 | Mensual |
| No conformidades | Incidentes proceso / Total sets procesados × 1.000 | <2 ‰ | — | ISO 17665 | Mensual |
| Tiempo reprocesamiento | Tiempo recepción sucio → disponible estéril | <4 h estándar | — | AAMI 2017 | Mensual |
| Trazabilidad completa | Sets con registro completo ciclo+paciente / Total × 100 | 100 % | — | Buena práctica | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Contaminación post-esterilización | Almacenamiento sellado, control ambiental, caducidad empaque |
| Falla autoclave sin detección | Indicador biológico obligatorio, cuarentena hasta resultado |
| Rotura cadena trazabilidad | Código barras obligatorio, auditoría semanal |

Ref: AAMI ST79:2017; ISO 17665-1:2006; AORN Guidelines Perioperative 2022; MINSAL Norma Técnica CME.

### 15.8 Rehabilitación/Kinesiología

Servicios de rehabilitación integral (kinesiología, fonoaudiología, terapia ocupacional) con énfasis en adherencia, continuidad hospital-domicilio y medición de resultados funcionales (PROMs).

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Evaluación funcional estandarizada | FIM, Barthel, TUG, 6MWT según condición |
| Plan rehabilitación individualizado | Metas SMART, frecuencia, modalidad (presencial/tele/domiciliario) |
| Continuidad hospital-domicilio | Alta kinésica con plan domiciliario, derivación CESFAM, tele-rehabilitación |
| Adherencia | Monitoreo asistencia, rescate inasistentes, ajuste plan según barreras |
| PROMs | Medición al inicio, intermedia y alta con instrumentos validados |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Asistencia a sesiones | Sesiones asistidas / Sesiones programadas × 100 | ≥80 % | — | OMS Rehab 2030 | Mensual |
| PROMs funcionales (mejora) | Pacientes con mejora ≥MCID / Total × 100 | ≥70 % | — | ICHOM 2022 | Trimestral |
| Alta oportuna rehabilitación | Altas dentro plazo plan / Total altas × 100 | ≥75 % | — | NHS Rehab 2022 | Trimestral |
| Derivación continuidad APS | Pacientes derivados con plan a APS / Total altas × 100 | ≥90 % | — | Buena práctica | Mensual |
| Inicio rehabilitación precoz | Inicio ≤48h post-evento (ACV, cirugía) / Total indicados × 100 | ≥80 % | ESO 2022 <24h ACV | ESO Guidelines 2022 | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Abandono tratamiento | Tele-rehabilitación, horarios flexibles, educación al paciente |
| Pérdida funcional por inicio tardío | Protocolo movilización precoz, alerta automática en HCE |
| Falta de continuidad post-alta | Coordinación APS, plan escrito al paciente, control telefónico |

Ref: OMS Rehabilitation 2030; ESO Guidelines ACV 2022; ICHOM Standard Sets; NHS Rehabilitation Framework 2022.

### 15.9 Odontología

Atención odontológica programada (GES odontológico: 6 años, embarazada, 60 años, urgencia) y de urgencia. Control riguroso IPC por aerosoles.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| GES odontológico | Salud oral integral 6 años, embarazada, 60 años — canasta prestaciones definida |
| Urgencia dentaria | Triage odontológico, atención <24h dolor/infección/trauma |
| Control IPC | Precauciones estándar + aerosoles, esterilización rotatorio, barrera ambiental |
| Odontología comunitaria | Programa preventivo escolar (sellantes, flúor), educación |
| Registro clínico | Odontograma digital, integración HCE, trazabilidad materiales |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Oportunidad GES odontológico | Pacientes atendidos en plazo GES / Total garantías × 100 | 100 % | Garantía legal | MINSAL-GES 2023 | Mensual |
| TAT urgencia odontológica | Mediana tiempo consulta→resolución | <24 h | — | MINSAL 2022 | Mensual |
| IAAS asociada procedimiento dental | Infecciones post-procedimiento / Total procedimientos × 1.000 | <1 ‰ | — | CDC Dental IPC 2016 | Trimestral |
| Cobertura sellantes 6 años | Niños sellados / Población meta × 100 | ≥70 % | OMS 80 % | MINSAL 2023 | Anual |
| Cumplimiento protocolo IPC | Auditoría cumplimiento / Total auditorías × 100 | ≥95 % | — | CDC 2016 | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Contaminación cruzada aerosoles | Aspiración alto volumen, ventilación, EPP completo |
| Incumplimiento GES por demanda | Extensión horaria, listas de espera con priorización |
| Falla esterilización instrumental rotatorio | Autoclave clase B dedicado, trazabilidad por ciclo |

Ref: MINSAL Norma Técnica Odontológica GES 2023; CDC Guidelines Dental IPC 2016; FDI Vision 2030.

### 15.10 Atención domiciliaria y cuidados paliativos

Atención domiciliaria de BAJA complejidad: cuidados crónicos, postrados, paliativos, curaciones, seguimiento post-alta. NO corresponde a hospitalización aguda domiciliaria.

> **Nota**: para hospitalización aguda domiciliaria (Hospital at Home) con monitorización remota, tratamiento IV y sustitución de cama hospitalaria, ver [cap 17](#17-hospitalización-domiciliaria--hospital-at-home).

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Programa postrados/dependientes severos | Visita domiciliaria programada, plan cuidados, cuidador capacitado |
| Cuidados paliativos | Alivio del dolor y síntomas, GES paliativos, acompañamiento familiar, voluntades anticipadas |
| Curaciones avanzadas | Úlceras, heridas crónicas — protocolo TIME, insumos domicilio |
| Seguimiento post-alta | Visita ≤72h post-alta en pacientes de riesgo (polimorbilidad, >75 años, reingreso previo) |
| Coordinación red | Enlace CESFAM-hospital, registro visitas, derivación oportuna |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Reingresos evitables 30d | Reingresos 30d en pacientes con seguimiento / Total × 100 | <12 % | — | AHRQ 2022 | Mensual |
| Satisfacción familiar | Score encuesta familiar/cuidador | ≥85 % | — | NICE NG142 2019 | Trimestral |
| Visitas cumplidas | Visitas realizadas / Visitas programadas × 100 | ≥90 % | — | Buena práctica | Mensual |
| Dolor controlado (paliativos) | Pacientes con EVA ≤3 / Total paliativos × 100 | ≥80 % | — | OMS Palliative Care 2020 | Mensual |
| Cobertura GES paliativos | Pacientes ingresados GES / Población estimada × 100 | ≥80 % | Garantía legal | MINSAL-GES 2023 | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Deterioro no detectado | Protocolo signos alarma para cuidador, línea telefónica 24/7 |
| Sobrecarga cuidador | Screening Zarit, respiro, apoyo psicosocial |
| Falta insumos domicilio | Kit domiciliario estandarizado, reposición programada |

Ref: MINSAL Programa Postrados 2023; NICE NG142 End of Life Care 2019; OMS Palliative Care 2020; GES Alivio del Dolor y Cuidados Paliativos.

### 15.11 Admisión y OIRS

Primer contacto administrativo del paciente. Identificación segura, orientación, gestión de reclamos y satisfacción usuaria. OIRS como mecanismo formal de participación.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Admisión | Identificación positiva (2 datos), registro, asignación cama/box, verificación previsión |
| OIRS | Oficina de información, reclamos y sugerencias — Ley 20.584, plazos legales |
| Gestión reclamos | Recepción → investigación → respuesta ≤15d hábiles (Ley 19.880) → seguimiento |
| Encuestas satisfacción | PREMs estandarizados, NPS, análisis y plan mejora |
| Señalética y orientación | Wayfinding, acompañamiento, información derechos y deberes |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tiempo admisión | Mediana tiempo llegada→registro completo | <15 min | — | Buena práctica | Mensual |
| Reclamos resueltos ≤15d | Reclamos resueltos en plazo / Total reclamos × 100 | ≥90 % | Ley 19.880 | MINSAL 2022 | Mensual |
| NPS | Net Promoter Score | ≥50 | — | IHI 2022 | Trimestral |
| Reclamos repetidos | Mismo motivo recurrente / Total reclamos × 100 | <10 % | — | Buena práctica | Trimestral |
| Error identificación admisión | Errores detectados / Total admisiones × 10.000 | <5 por 10.000 | — | JCI 2022 | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Error identificación paciente | Doble verificación, pulsera, protocolo JCI IPSG.1 |
| Reclamos sin respuesta en plazo | Workflow automatizado, escalamiento, reporte gerencia |
| Insatisfacción por desinformación | Protocolo comunicación, pantallas info, app paciente |

Ref: Ley 20.584 (Derechos del Paciente); Ley 19.880 (Procedimientos Administrativos); JCI IPSG.1; MINSAL Orientaciones OIRS 2022.

### 15.12 Transporte sanitario programado

Traslado programado de pacientes entre establecimientos o domicilio-hospital. No incluye transporte de emergencia (ver cap. 18 EMS).

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Programación | Solicitud anticipada ≥24h, coordinación con agenda clínica, confirmación paciente |
| Clasificación | Ambulancia básica, vehículo liviano, transporte sentado — según condición paciente |
| Seguridad traslado | Checklist pre-traslado, documentación clínica, equipamiento según complejidad |
| Flota y mantención | Plan mantención preventiva, certificación SAMU/SEREMI, GPS tracking |
| Coordinación inter-establecimiento | Central de coordinación, horarios protegidos, priorización |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Puntualidad | Traslados en horario ±15 min / Total × 100 | ≥90 % | — | NHS Patient Transport 2022 | Mensual |
| Incidentes transporte | Eventos adversos / Total traslados × 1.000 | <1 ‰ | — | AHRQ 2021 | Trimestral |
| Utilización flota | Horas operativas / Horas disponibles × 100 | ≥75 % | — | Buena práctica | Mensual |
| Satisfacción paciente transporte | Score encuesta | ≥80 % | — | NHS 2022 | Trimestral |
| Cancelación por falta vehículo | Traslados cancelados por disponibilidad / Total solicitudes × 100 | <5 % | — | Buena práctica | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Deterioro clínico durante traslado | Checklist pre-traslado, equipamiento, comunicación continua |
| Demora que afecta agenda clínica | Buffer horario, coordinación centralizada, priorización clínica |
| Falla mecánica en ruta | Mantención preventiva, vehículo de respaldo, GPS-alerta |

Ref: NHS Patient Transport Standards 2022; MINSAL Norma Transporte Sanitario; SAMU normativa vigente.

### 15.13 Docencia e investigación clínica

Campos clínicos para formación de pregrado/postgrado médico y de salud. Investigación clínica con cumplimiento ético, protección de datos y retorno institucional.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Campos clínicos | Convenios universidad-servicio, cupos definidos, supervisión docente asistencial |
| Comité de ética (CEC) | Evaluación protocolos, consentimiento informado, seguimiento eventos adversos investigación |
| Protección datos investigación | Anonimización, cumplimiento Ley 20.120 (investigación en seres humanos), Ley 19.628 (datos personales) |
| Formación continua | Programa capacitación institucional, créditos acreditación, simulación |
| Publicaciones y difusión | Incentivo publicación, acceso bases datos, protección propiedad intelectual |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cumplimiento ético | Protocolos con aprobación CEC vigente / Total activos × 100 | 100 % | Regulatorio | Ley 20.120 | Trimestral |
| Publicaciones indexadas | Publicaciones WoS/Scopus por año | Tendencia creciente | — | Institución | Anual |
| Satisfacción docente (internos) | Score encuesta internos/residentes | ≥80 % | — | ASOFAMECH 2022 | Semestral |
| Eventos adversos investigación | Eventos reportados / Total participantes × 100 | <1 % | — | ICH-GCP 2022 | Trimestral |
| Convenios campo clínico vigentes | Convenios vigentes / Total requeridos × 100 | 100 % | Regulatorio | MINSAL 2022 | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Investigación sin aprobación ética | Registro obligatorio CEC previo, auditoría |
| Conflicto asistencia-docencia | Ratio alumnos/paciente definido, supervisión, prioridad asistencial |
| Brecha protección datos | Capacitación Ley 19.628, encriptación, acceso controlado |

Ref: Ley 20.120 (Investigación en Seres Humanos Chile); ICH-GCP E6(R2) 2022; Declaración de Helsinki 2013; ASOFAMECH normativa campos clínicos.

### 15.14 Servicios generales (aseo, alimentación, residuos)

Servicios de soporte no clínico: aseo hospitalario (IPC), alimentación (seguridad alimentaria), gestión de residuos (REAS). Impacto directo en IAAS y experiencia.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Aseo hospitalario | Protocolos diferenciados por área (crítica/semicrítica/no crítica), productos EPA/ISP, frecuencia |
| Alimentación y nutrición | Régimen por patología, seguridad alimentaria (HACCP), cadena frío, alérgenos |
| Gestión REAS | Segregación (cortopunzante, infeccioso, químico, doméstico), almacenamiento transitorio, retiro autorizado |
| Control IPC ambiental | Cultivos de superficie, control agua, ventilación HEPA áreas críticas |
| Externalización y fiscalización | Contratos con SLA, supervisión institucional, auditoría cumplimiento |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| IAAS asociada ambiente | Brotes ambientales / Total IAAS × 100 | <5 % | — | CDC 2019 | Trimestral |
| No conformidades aseo | Auditorías con incumplimiento / Total auditorías × 100 | <10 % | — | Buena práctica | Mensual |
| Cumplimiento HACCP | Puntos críticos controlados / Total PCC × 100 | 100 % | Regulatorio | RSA Chile | Mensual |
| Segregación correcta REAS | Residuos correctamente segregados / Total auditado × 100 | ≥95 % | — | DS 6/2009 MINSAL | Trimestral |
| Satisfacción alimentación | Score encuesta pacientes | ≥75 % | — | NHS Patient Survey 2022 | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Brote IAAS por falla limpieza | Auditoría ATP/fluorescencia, capacitación, supervisión IPC |
| Toxiinfección alimentaria | HACCP estricto, trazabilidad, control temperatura continuo |
| Accidente con REAS | Capacitación segregación, contenedores normados, EPP, plan emergencia |

Ref: DS 6/2009 (REAS Chile); Reglamento Sanitario de Alimentos Chile; CDC Environmental Infection Control 2019; OMS WASH in HCF 2022.

---

## 16. Unidades hospitalarias

### 16.1 Hospitalización médico-quirúrgica

Gestión de camas de hospitalización aguda. Plan de cuidados estandarizado, gestión de alta desde el ingreso, prevención eventos adversos y reingresos.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Plan de cuidados | Estandarizado por GRD/diagnóstico, metas diarias, ronda multidisciplinaria |
| Gestión de altas | Planificación desde ingreso, estimated discharge date (EDD), checklist alta segura |
| Prevención EA | Caídas (Morse), UPP (Braden), TEV (Padua/Caprini), delirium (CAM) — bundles preventivos |
| Ronda multidisciplinaria | Médico, enfermera, farmacéutico, kinesiólogo, trabajador social — diaria |
| Transiciones seguras | Conciliación medicamentosa, informe alta estructurado, derivación continuidad |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| LOS ajustada (case-mix) | Promedio días estada ajustado por GRD | Según benchmark GRD | OCDE mediana 6.5d | OCDE 2023 | Mensual |
| Reingresos 30d (no planificados) | Reingresos ≤30d / Egresos × 100 | <10 % | CMS 15.5 % all-cause | CMS 2022 | Mensual |
| Eventos adversos (EA) | EA / 1.000 días-cama | <15 ‰ | — | AHRQ PSI 2022 | Trimestral |
| Caídas con daño | Caídas con lesión / 1.000 días-cama | <3 ‰ | NDNQI 3-5 ‰ | NDNQI 2022 | Mensual |
| Cumplimiento profilaxis TEV | Pacientes con profilaxis adecuada / Indicados × 100 | ≥95 % | JCI ≥95 % | JCI IPSG 2022 | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Estancia prolongada (boarding) | EDD al ingreso, ronda de gestión camas 2×/d, altas AM |
| Reingreso evitable | Seguimiento telefónico 48-72h, transición segura, derivación APS |
| Evento adverso prevenible | Bundles seguridad, checklist, cultura reporte no punitiva |

Ref: AHRQ Patient Safety Indicators 2022; NDNQI Nursing Quality 2022; JCI International Patient Safety Goals; MINSAL Norma GRD 2023.

### 16.2 UCI/UTI/UPC

Unidades de paciente crítico. Ratios enfermería estrictos, bundles de prevención IAAS asociadas a dispositivo, scoring pronóstico y decisión de limitación terapéutica.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Ratios dotación | Enfermera:paciente 1:1-1:2 (UCI), 1:3-1:4 (UTI); kinesiólogo 1:4-1:6 |
| Bundle CVC | Higiene manos, barrera máxima, clorhexidina, sitio óptimo, revisión diaria necesidad |
| Bundle VAP | Cabecera 30-45°, vacaciones sedación, prueba ventilación espontánea, higiene oral clorhexidina |
| Bundle CAUTI | Indicación estricta, inserción aséptica, mantención sistema cerrado, revisión diaria necesidad |
| Scoring pronóstico | APACHE IV, SOFA — evaluación diaria, comunicación familia |
| Movilización precoz | Protocolo escalado, kinesioterapia intensiva, sedación mínima |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Mortalidad ajustada (SMR) | Muertes observadas / Muertes esperadas (APACHE) | <1.0 | ANZICS 0.8-0.9 | ANZICS 2022 | Trimestral |
| CLABSI | Bacteriemias asociadas CVC / 1.000 días-CVC | <1.0 ‰ | NHSN mediana 0.8 | NHSN 2022 | Mensual |
| VAP | Neumonía asociada VM / 1.000 días-VM | <2.0 ‰ | NHSN mediana 0.9 | NHSN 2022 | Mensual |
| CAUTI | ITU asociada catéter / 1.000 días-catéter | <2.0 ‰ | NHSN mediana 1.7 | NHSN 2022 | Mensual |
| Cumplimiento bundles | Auditoría cumplimiento completo / Total auditorías × 100 | ≥95 % | — | IHI 2022 | Semanal |
| Movilización precoz <48h | Pacientes movilizados ≤48h / Elegibles × 100 | ≥70 % | — | Schweickert 2009 | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| IAAS asociada dispositivo | Bundles con auditoría, retiro oportuno, comité IAAS |
| Ratio enfermería insuficiente | Dotación normada, pool de relevo, monitoreo carga laboral |
| Delirium UCI | Protocolo ABCDEF (A: analgesia, B: despertar, C: coordinación, D: delirium CAM-ICU, E: ejercicio, F: familia) |

Ref: Surviving Sepsis Campaign 2021; NHSN Device-Associated Module 2022; ANZICS CORE 2022; IHI Bundles; protocolo ABCDEF ICU Liberation.

### 16.3 Pabellones/quirófanos

Gestión del block quirúrgico: programación, utilización de salas, prevención cancelaciones y seguridad intraoperatoria (checklist OMS).

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Programación quirúrgica | Tabla semanal, priorización (urgencia, oncológica, electiva), overbooking controlado |
| Checklist quirúrgico OMS | Sign-in, time-out, sign-out — verificación obligatoria 100 % cirugías |
| Gestión tiempos | Primer corte 08:00, turnover <30 min, minimizar tiempo muerto |
| Pabellón de urgencia | Sala dedicada 24/7, protocolo activación, priorización por gravedad |
| Conteo seguro | Instrumental, gasas, agujas — protocolo doble conteo, radiografía ante discrepancia |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Utilización sala | Tiempo quirúrgico / Tiempo disponible × 100 | ≥80 % | NHS 85 % | NHS Getting It Right 2022 | Mensual |
| Cancelaciones mismo día | Canceladas el día / Programadas × 100 | <5 % | NHS <5 % | NHS 2022 | Mensual |
| Primer caso a tiempo | Cirugías que inician ±10 min de hora programada / Total 1er caso × 100 | ≥80 % | — | AORN 2022 | Mensual |
| Checklist OMS cumplimiento | Checklists completos (3 fases) / Total cirugías × 100 | 100 % | OMS 100 % | OMS Safe Surgery 2009 | Mensual |
| Infección sitio quirúrgico (ISQ) | ISQ / Total cirugías × 100 | <2 % (limpia) | NHSN 1-3 % | NHSN 2022 | Trimestral |
| Turnover tiempo | Mediana minutos salida→entrada siguiente paciente | <30 min | — | AORN 2022 | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Cirugía en paciente/sitio equivocado | Checklist OMS obligatorio, marcaje sitio, time-out |
| Cancelación por falta de cama UCI | Coordinación cama previo programación, plan contingencia |
| Retención cuerpo extraño | Protocolo doble conteo, Rx ante discrepancia, cultura reporte |

Ref: OMS Safe Surgery Saves Lives 2009; AORN Perioperative Standards 2022; NHS Getting It Right First Time (GIRFT) 2022; NHSN SSI Module.

### 16.4 Obstetricia y Neonatología

Atención segura del parto, emergencia obstétrica y cuidado neonatal. Foco en prevención morbilidad materna severa y mortalidad neonatal precoz.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Parto seguro | Partograma, monitoreo fetal, acompañamiento continuo (Ley 21.030), decisión cesárea con criterio |
| Emergencia obstétrica | Protocolo hemorragia (código rojo), preeclampsia severa, distocia — simulación periódica |
| Neonatología niveles | Nivel I (básico), II (intermedio), III (UCI neonatal) — según complejidad |
| Lactancia | IHAN (Hospital Amigo del Niño), contacto piel-piel, alojamiento conjunto |
| Tamizaje neonatal | Metabólico, auditivo, cardiopatía (oximetría), displasia cadera |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Morbilidad materna severa | Casos MMS / Total partos × 1.000 | <10 ‰ | — | OMS 2023 | Trimestral |
| Tasa cesárea (Robson) | Cesáreas / Total partos × 100, análisis por grupo Robson | 19-25 % (población) | OMS 10-15 % ideal | OMS Robson 2017 | Mensual |
| APGAR <7 a 5 min | RN con APGAR <7 / Total RN vivos × 100 | <2 % | — | MINSAL 2022 | Mensual |
| Lactancia materna exclusiva al alta | RN con LME / Total RN vivos × 100 | ≥80 % | OMS/UNICEF ≥80 % | IHAN 2022 | Mensual |
| Mortalidad neonatal precoz | Muertes <7d / Total RN vivos × 1.000 | <3 ‰ | OCDE 2.5 ‰ | OCDE 2023 | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Hemorragia post-parto no controlada | Código rojo obstétrico, kit emergencia, simulacro trimestral |
| Asfixia neonatal | Reanimación neonatal certificada (NRP), equipo disponible 24/7 |
| Cesárea innecesaria | Auditoría Robson, segunda opinión, protocolos inducción/conducción |

Ref: OMS Clasificación Robson 2017; IHAN/UNICEF Baby-Friendly Hospital 2022; MINSAL Norma Perinatal 2022; NRP (Neonatal Resuscitation Program) 2021.

### 16.5 Pediatría

Hospitalización pediátrica con énfasis en seguridad de medicamentos (dosificación por peso), prevención de EA específicos y experiencia niño/familia.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Seguridad medicamento pediátrico | Dosis kg/peso, doble-check, formulario pediátrico, bombas programadas |
| Hospitalización acompañada | Derecho acompañamiento 24h (Ley 20.584), participación cuidador en plan |
| Dolor pediátrico | Escalas edad-específicas (FLACC, Wong-Baker, EVA), protocolo analgesia |
| Juego terapéutico | Preparación procedimientos, distracción, ambiente amigable |
| Transición a adulto | Protocolo para crónicos pediátricos (>15 años), derivación coordinada |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Eventos dosificación | Errores dosis pediátrica / Total prescripciones pediátricas × 1.000 | <3 ‰ | — | ISMP 2022 | Mensual |
| Satisfacción cuidadores | Score encuesta padres/cuidadores | ≥85 % | — | Picker Institute 2022 | Trimestral |
| Reingresos 7d (pediátrico) | Reingresos ≤7d / Egresos pediátricos × 100 | <5 % | — | AHRQ PDI 2022 | Mensual |
| Dolor controlado | Pacientes con score dolor ≤3 / Total evaluados × 100 | ≥80 % | — | IHI 2022 | Mensual |
| Cumplimiento doble-check MAR | Auditoría MAR pediátrico / Total MAR × 100 | 100 % | — | ISMP 2022 | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Error dosificación 10× | Peso obligatorio en prescripción, CPOE pediátrico, doble verificación |
| Angustia niño/familia | Preparación pre-procedimiento, juego terapéutico, ambiente |
| Deterioro rápido | PEWS (Pediatric Early Warning Score), escalamiento protocolizado |

Ref: ISMP Pediatric Medication Safety 2022; AHRQ Pediatric Quality Indicators 2022; Picker Institute Patient Experience; PEWS validación.

### 16.6 Oncología integral

Gestión del continuo oncológico: sospecha → confirmación → etapificación → tratamiento → seguimiento. Tiempos como métrica clave (GES oncológicos). Seguridad en quimioterapia.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Tiempos diagnóstico-tratamiento | GES: sospecha→confirmación ≤30d, confirmación→etapificación ≤15d, etapificación→tratamiento según patología |
| Comité oncológico | Multidisciplinario (cirugía, oncología médica, radio, patología, enfermería), decisión consensuada |
| Seguridad quimioterapia | Preparación centralizada (campana flujo laminar), verificación esquema, extravasación, derrames |
| Cuidados de soporte | Antiemesis, dolor, nutrición, psicooncología, rehabilitación |
| Navegación paciente | Navigator oncológico, coordinación exámenes/tratamientos, apoyo GES |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tiempo sospecha→tratamiento | Mediana días desde IC sospecha hasta inicio tratamiento | Según GES por patología | UK 62d cancer target | NHS Cancer Waiting Times 2023 | Mensual |
| Eventos adversos quimioterapia | EA grado ≥3 (CTCAE) / Total ciclos × 100 | <10 % | — | ASCO 2022 | Mensual |
| Mortalidad ≤30d post-quimio | Muertes ≤30d / Total pacientes en QT × 100 | <3 % (curativo) | NCRAS UK 2.5 % | NCRAS 2022 | Trimestral |
| Comité oncológico | Pacientes discutidos en comité / Total pacientes nuevos × 100 | ≥90 % | — | NICE IOG 2022 | Mensual |
| Supervivencia 1 año proxy | Sobrevida 1 año por tipo tumoral | Según registro nacional | — | RNT Chile | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Demora diagnóstica (pérdida ventana) | Vía rápida oncológica, navigator, alerta lista espera |
| Error preparación quimio | Preparación centralizada, doble verificación, código barras |
| Extravasación vesicante | Protocolo extravasación, kit antídoto, capacitación enfermería |

Ref: GES oncológicos MINSAL 2023; ASCO/ONS Chemotherapy Safety Standards 2022; NICE Improving Outcomes Guidance 2022; NHS Cancer Waiting Times.

### 16.7 Gestión de camas

Asignación dinámica de camas, gestión del boarding en SUH, promoción de altas matutinas y coordinación con alternativas a la hospitalización.

> La hospitalización domiciliaria (cap 17) libera camas físicas para pacientes de mayor agudeza — efecto backfill: cada cama HaH permite ingresar un paciente de mayor complejidad, generando margen incremental.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Asignación dinámica | Central de camas 24/7, priorización por gravedad y flujo, matching cama-necesidad |
| Gestión boarding | Tiempo máximo boarding SUH <4h, protocolo escalamiento, expansión camas |
| Altas matutinas | Meta altas antes 12:00, ronda alta 08:00, trámites noche previa |
| Alternativas hospitalización | Hospital at Home (cap 17), hospital de día, alta con seguimiento telefónico |
| Dashboards tiempo real | Ocupación por servicio, camas disponibles, EDD, boarding, flujo entrada/salida |

**IF/THEN — Decisión gestión camas:**

| Condición | Acción |
|-----------|--------|
| IF ocupación ≥90 % | THEN activar protocolo contingencia: acelerar altas, evaluar HaH, suspender electivas |
| IF boarding SUH >4h | THEN escalar a dirección, apertura camas contingencia, redistribución |
| IF ocupación <70 % (sostenido) | THEN consolidar unidades, redistribuir dotación, oferta a red |
| IF paciente elegible HaH | THEN derivar a equipo HaH (cap 17), liberar cama física |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Ocupación camas | Días-cama ocupados / Días-cama disponibles × 100 | 85-90 % | NHS 85 % ideal | NHS 2023 | Diario |
| Boarding SUH >4h | Pacientes con boarding >4h / Total ingresos desde SUH × 100 | <10 % | — | ACEP 2022 | Diario |
| Altas antes 12:00 | Altas ≤12:00 / Total altas del día × 100 | ≥33 % | NHS ECIST 33 % | NHS ECIST 2022 | Diario |
| Camas liberadas por HaH | Pacientes derivados a HaH / Total egresos × 100 | ≥5 % (en programas activos) | — | HaH evidence | Mensual |
| Estancia social (bed-blocking) | Días-cama por causa social / Total días-cama × 100 | <5 % | — | NHS Delayed Transfers 2023 | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Sobreocupación (>95 %) → EA | Protocolo contingencia, HaH, compra servicios, derivación red |
| Alta prematura → reingreso | Checklist alta segura, EDD con criterios clínicos, seguimiento 48h |
| Bed-blocking social | Coordinación trabajo social precoz, red sociosanitaria, hogar protegido |

Ref: NHS ECIST (Emergency Care Intensive Support Team) 2022; ACEP Boarding Position Statement 2022; AHRQ Bed Management 2021; evidencia HaH backfill.

---

## 17. Hospitalización domiciliaria — Hospital at Home

### 17.1 Modelos y evidencia

Dos modelos principales: evitación de ingreso (admission avoidance) y alta precoz apoyada (early supported discharge). Evidencia robusta de ensayos controlados y revisiones sistemáticas.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Admission avoidance | Paciente identificado en SUH/urgencia, derivado a domicilio en lugar de hospitalización convencional |
| Early supported discharge (ESD) | Paciente estabilizado en hospital (24-72h), completa tratamiento en domicilio |
| Modelo híbrido | Combinación según perfil clínico y capacidad operativa del programa |

**Evidencia síntesis:**

| Desenlace | Hospital at Home | Hospitalización convencional | Fuente |
|-----------|-----------------|------------------------------|--------|
| Mortalidad (RR) | 0.77-0.84 | 1.0 (referencia) | Cochrane Shepperd 2016; Levine 2020 |
| Reingresos 30d | 7-8.6 % | 15.6-23 % | Levine 2020; MGB 2022 |
| Costo por episodio | 19-38 % menor | Referencia | CMS AHCAH 2023; Levine 2020 |
| LOS (días) | 3.2 (mediana) | 4.9-5.5 | Leff 2005; Caplan 2012 |
| Satisfacción (score) | 90.7 % | 83.9 % | Leff 2005; Federman 2018 |
| Delirium | 9 % | 24 % | Caplan 2006; Levine 2020 |
| Caídas | Similar o menor | Referencia | Cochrane 2016 |
| Actividad física (accelerómetro) | +17 min/d ambulando | Referencia | Levine 2020 |

**IF/THEN — Selección de modelo:**

| Condición | Modelo recomendado |
|-----------|-------------------|
| IF paciente en SUH con criterio de ingreso + elegible + sin necesidad UCI | THEN admission avoidance |
| IF paciente hospitalizado ≥24h, estable, en trayectoria mejoría | THEN early supported discharge |
| IF programa incipiente (<6 meses operación) | THEN iniciar con ESD (menor riesgo operacional), escalar a admission avoidance |
| IF domicilio no cumple criterios ambientales | THEN hospitalización convencional (no elegible HaH) |
| IF cuidador no disponible o no capacitable | THEN evaluar caso a caso; considerar cuidador profesional o excluir |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Mortalidad HaH | Muertes / Total episodios HaH × 100 | ≤2 % | Cochrane RR 0.77-0.84 | Cochrane 2016 | Trimestral |
| Reingresos 30d HaH | Reingresos / Egresos HaH × 100 | <10 % | Levine 7-8.6 % | Levine 2020 | Mensual |
| Costo vs. hospitalización convencional | Costo HaH / Costo convencional × 100 | ≤80 % | 62-81 % | CMS 2023 | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Deterioro no detectado en domicilio | RPM continuo, escalamiento protocolizado, umbral bajo para re-hospitalización |
| Selección inadecuada de modelo | Criterios estandarizados, experiencia ESD antes de admission avoidance |
| Sesgo de selección (solo pacientes "fáciles") | Ampliar criterios progresivamente, auditoría case-mix |

Ref: Cochrane Shepperd et al. 2016; Levine et al. JAMA IM 2020; Leff et al. JAGS 2005; Caplan et al. MJA 2012; CMS AHCAH 2023.

### 17.2 Elegibilidad y criterios de admisión

Selección rigurosa del paciente: criterios clínicos, funcionales, ambientales y de consentimiento. Patologías prevalentes definidas por evidencia y viabilidad operativa.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Criterio clínico general | Requiere hospitalización (no ambulatorio), no requiere UCI, condición en lista elegible |
| Patologías prevalentes | NAC, ICC descompensada, EPOC exacerbada, celulitis, ITU/pielonefritis, TVP/TEP estable |
| Criterio funcional | Consciente, capaz de comunicar síntomas (o cuidador), cooperador |
| Criterio ambiental | Domicilio con electricidad, agua potable, teléfono/conectividad, radio ≤30 km del hospital |
| Criterio social | Cuidador disponible ≥parte del día, red apoyo, consentimiento informado firmado |
| Exclusiones | Inestabilidad hemodinámica, necesidad monitorización invasiva, riesgo social grave, adicción activa no controlada, psiquiatría aguda |

**IF/THEN — Elegibilidad:**

| Condición | Decisión |
|-----------|----------|
| IF paciente requiere hospitalización + condición en lista + no UCI | THEN evaluar criterios ambientales y sociales |
| IF domicilio sin electricidad o agua potable | THEN excluir HaH |
| IF sin cuidador y paciente autovalente + bajo riesgo | THEN evaluar caso a caso con visita previa |
| IF paciente rechaza o retira consentimiento | THEN hospitalización convencional (derecho irrenunciable) |
| IF radio >30 km y sin base periférica | THEN excluir HaH (tiempo respuesta inseguro) |
| IF adicción activa con riesgo de abandono tratamiento IV | THEN excluir HaH |
| IF paciente con demencia sin cuidador capacitado | THEN excluir HaH |
| IF condición clínica no en lista pero médico tratante fundamenta | THEN evaluar en comité HaH, ampliar criterio si pertinente |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tasa elegibilidad | Pacientes elegibles / Total ingresos hospitalarios × 100 | 10-30 % | Johns Hopkins 25-30 % | Leff 2005 | Mensual |
| Aceptación paciente | Pacientes que aceptan / Pacientes elegibles × 100 | ≥70 % | — | MGB 2022 | Mensual |
| Tasa escalamiento (retorno hospital) | Pacientes retornados / Total HaH × 100 | ≤10 % | 7-10 % | Levine 2020 | Mensual |
| Screening completado | Evaluaciones elegibilidad realizadas / Candidatos identificados × 100 | ≥90 % | — | Buena práctica | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Criterios demasiado restrictivos → bajo volumen | Revisión periódica, benchmarking, ampliación progresiva |
| Criterios laxos → eventos adversos | Auditoría escalamientos, mortalidad, comité calidad |
| Sesgo socioeconómico en elegibilidad | Evaluación equidad, apoyo transporte/conectividad, equipo social |

Ref: Levine et al. Annals IM 2020 (criterios JHH); Leff et al. JAGS 2005; CMS AHCAH Waiver criteria 2023; Hospital Clínic Barcelona protocolo 2022.

### 17.3 Modelo operativo y dotación

Equipo multidisciplinario dedicado con cobertura 24/7, logística de medicamentos e insumos a domicilio y centro de mando como eje coordinador.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Médico | Visita presencial diaria (o cada 48h si estable), disponibilidad 24/7 (telemedicina + presencial urgente) |
| Enfermería | 1-2 visitas/día, ratio 1:4-1:6 pacientes, procedimientos (IV, curación, monitoreo) |
| Paramédico/TENS | Apoyo enfermería, toma muestras, transporte insumos, educación cuidador |
| Kinesiología/TO | Según indicación: rehabilitación respiratoria, movilización, AVD |
| Trabajo social | Evaluación ambiental, apoyo cuidador, gestión red sociosanitaria |
| Centro de mando (command center) | Recepción alertas RPM, coordinación visitas, triage telefónico, despacho emergencia |
| Farmacia | Dispensación y entrega domiciliaria (incl. medicamentos IV), conciliación |
| Logística equipos | Oxígeno domiciliario, bombas infusión, concentrador O2, equipo diagnóstico portátil |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tiempo respuesta emergencia | Minutos desde alerta hasta llegada equipo al domicilio | <60 min | — | Buena práctica HaH | Mensual |
| Visitas cumplidas | Visitas realizadas / Visitas programadas × 100 | ≥95 % | — | Buena práctica | Semanal |
| Ratio enfermería | Pacientes activos / Enfermeras turno | 1:4-1:6 | JHH 1:4 | Johns Hopkins HaH | Diario |
| Disponibilidad 24/7 | Horas con cobertura efectiva / 168 h semana × 100 | 100 % | — | CMS AHCAH requisito | Semanal |
| Medicamentos entregados oportunamente | Entregas en tiempo / Total entregas × 100 | ≥95 % | — | Buena práctica | Semanal |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Dotación insuficiente → sobrecarga | Ratio estricto, pool de relevo, expansión gradual censo |
| Demora respuesta emergencia | Zona geográfica acotada, vehículo dedicado, protocolo SAMU complementario |
| Falla entrega medicamento IV | Stock buffer domicilio, farmacia con delivery, protocolo contingencia oral |

Ref: Johns Hopkins Hospital at Home Model; Mount Sinai HaH operational guide; CMS AHCAH Conditions of Participation 2023; MGB Home Hospital operations 2022.

### 17.4 Infraestructura tecnológica y RPM

Monitorización remota de pacientes (RPM) como pilar de seguridad. Dispositivos, plataforma de telesalud, integración con HCE y sistemas de alerta con soporte de inteligencia artificial.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Dispositivos RPM | SpO2, presión arterial, frecuencia cardíaca, temperatura, frecuencia respiratoria, ECG single-lead, peso, glucómetro |
| Plataforma telesalud | Videollamada paciente-equipo, chat asincrónico, educación multimedia |
| Integración HCE | Flujo bidireccional FHIR R4: signos vitales RPM → HCE, órdenes HCE → dispositivos |
| Alertas y CDS | Umbrales personalizados por patología, escalamiento automático, trending |
| IA predictiva | Modelos de deterioro temprano (MEWS modificado, redes neuronales sobre series temporales RPM) |
| Conectividad | Tablet/smartphone con datos móviles provistos, gateway Bluetooth, hotspot si necesario |

**IF/THEN — Alertas RPM:**

| Condición | Acción |
|-----------|--------|
| IF SpO2 <90 % (o caída >4 % desde basal) | THEN alerta roja → llamada inmediata + evaluar visita presencial/SAMU |
| IF PA sistólica >180 o <90 mmHg | THEN alerta roja → contacto médico, evaluación presencial |
| IF FC >120 o <50 bpm (sostenido >10 min) | THEN alerta naranja → evaluación enfermería telefónica + presencial si persiste |
| IF temperatura >38.5 °C | THEN alerta naranja → contacto enfermería, evaluación foco, hemocultivos si indicados |
| IF peso +1.5 kg en 24h (ICC) | THEN alerta naranja → ajuste diurético, restricción hídrica, evaluación médica |
| IF sin transmisión datos >4h (paciente despierto) | THEN alerta técnica → llamada verificación, visita si no contactable |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Adherencia RPM | Transmisiones recibidas / Transmisiones esperadas × 100 | ≥85 % | — | CMS AHCAH 2023 | Semanal |
| Tiempo respuesta alerta roja | Minutos desde alerta hasta contacto clínico | <15 min | — | Buena práctica | Mensual |
| Falsas alarmas | Alertas sin acción clínica / Total alertas × 100 | <30 % | — | Literature RPM 2022 | Mensual |
| Integración HCE | Datos RPM volcados automáticamente / Total datos × 100 | ≥95 % | — | Estándar FHIR | Trimestral |
| Satisfacción tecnología (paciente) | Score facilidad de uso dispositivos | ≥80 % | — | SUS Scale | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Brecha digital paciente/cuidador | Capacitación in-situ, dispositivos simplificados, soporte técnico 24/7 |
| Fatiga de alertas (alert fatigue) | Umbrales personalizados, IA filtrado, priorización |
| Falla conectividad | Gateway offline con buffer, hotspot respaldo, protocolo llamada |
| Ciberseguridad datos salud | Encriptación end-to-end, cumplimiento HIPAA/Ley 19.628, auditoría accesos |

Ref: CMS AHCAH RPM requirements 2023; Current Health (Best Buy) platform; Biofourmis AI; FHIR R4 Vital Signs IG; Ley 19.628 (Datos Personales Chile).

### 17.5 Vías clínicas prevalentes

Protocolos clínico-operativos por patología. Cada vía define: tratamiento estándar, monitoreo específico, criterios de switch terapéutico y umbrales de escalamiento.

**ICC descompensada:**

| Componente | Detalle |
|------------|---------|
| Tratamiento | Diuréticos IV (furosemida) → transición oral según respuesta, IECA/ARA2, betabloqueadores |
| Monitoreo | Peso diario (alerta +1.5 kg/24h), balance hídrico, SpO2, PA, FC, ingesta Na |
| Switch IV→oral | IF diuresis >1 L en 4h + peso descendente + SpO2 >93 % THEN switch a oral |
| Escalamiento | IF no respuesta diurético 48h OR SpO2 <88 % OR edema pulmonar THEN retorno hospital |

**EPOC exacerbado:**

| Componente | Detalle |
|------------|---------|
| Tratamiento | Broncodilatadores nebulizados, corticoides sistémicos (5d), O2 titulado (meta SpO2 88-92 %), antibiótico si purulento |
| Monitoreo | SpO2 continuo, FR, volumen esputo, disnea (escala mMRC), flujo espiratorio |
| Switch | IF SpO2 estable >90 % sin O2 + FR <24 + mejoría subjetiva THEN suspender O2, mantener inhaladores |
| Escalamiento | IF SpO2 <85 % OR FR >30 OR deterioro conciencia THEN retorno hospital/UCI |

**NAC (Neumonía adquirida en la comunidad):**

| Componente | Detalle |
|------------|---------|
| Tratamiento | Antibiótico IV (ceftriaxona ± azitromicina según CURB-65/PSI), switch therapy |
| Monitoreo | Temperatura, SpO2, FR, respuesta clínica 48-72h, Rx portátil control |
| Switch IV→oral | IF afebril ≥24h + SpO2 >93 % + tolerancia oral + mejoría clínica THEN switch amoxicilina-clavulánico oral |
| Escalamiento | IF fiebre persistente >72h OR SpO2 <90 % OR inestabilidad THEN retorno hospital, re-evaluación |

**ITU/Pielonefritis:**

| Componente | Detalle |
|------------|---------|
| Tratamiento | Antimicrobiano IV (ceftriaxona/gentamicina), hidratación, control función renal |
| Monitoreo | Temperatura, diuresis, creatinina seriada, urocultivo control |
| Switch IV→oral | IF afebril ≥24h + creatinina estable/descendente THEN switch ciprofloxacino/cefalosporina oral |
| Escalamiento | IF fiebre >72h OR deterioro función renal OR sepsis THEN retorno hospital |

**Celulitis:**

| Componente | Detalle |
|------------|---------|
| Tratamiento | Antibiótico IV (cloxacilina/cefazolina), elevación, marcación diaria del borde |
| Monitoreo | Fotografía diaria con regla, temperatura, marcación borde lesión, PCR seriada |
| Switch IV→oral | IF reducción eritema + afebril 24h + PCR descendente THEN switch cloxacilina oral |
| Escalamiento | IF progresión pese a 48h IV OR fiebre persistente OR sospecha fascitis THEN retorno hospital |

**TVP/TEP estable:**

| Componente | Detalle |
|------------|---------|
| Tratamiento | Anticoagulación (HBPM → DOAC), compresión elástica (TVP), analgesia |
| Monitoreo | Edema (circunferencia), SpO2 (TEP), signos sangrado, adherencia anticoagulante |
| Switch | IF HBPM ≥5d + estable THEN switch DOAC oral |
| Escalamiento | IF aumento edema + dolor OR SpO2 <92 % OR sangrado THEN retorno hospital |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Switch IV→oral oportuno | Switches en criterio / Total elegibles × 100 | ≥85 % | — | Buena práctica HaH | Mensual |
| Escalamiento a hospital | Retornos / Total episodios por patología × 100 | ≤10 % | 7-10 % global | Levine 2020 | Mensual |
| Cumplimiento protocolo vía | Auditoría adherencia protocolo / Total casos × 100 | ≥90 % | — | Buena práctica | Trimestral |
| Resolución clínica | Pacientes con resolución completa al egreso HaH / Total × 100 | ≥85 % | — | HaH literature | Mensual |
| Rx portátil en NAC | Rx realizado en domicilio / Rx indicado × 100 | ≥90 % | — | Buena práctica | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Switch prematuro → recaída | Criterios objetivos documentados, evaluación médica presencial pre-switch |
| Demora en escalamiento | Umbrales claros, educación cuidador en signos alarma, alerta RPM |
| Resistencia antimicrobiana | Cultivo previo a antibiótico, de-escalamiento según antibiograma |

Ref: IDSA/ATS NAC Guidelines 2019; ESC ICC Guidelines 2021; GOLD EPOC 2023; NICE CG191 TEP; Johns Hopkins HaH clinical pathways; Hospital Clínic Barcelona vías clínicas HaH.

### 17.6 Calidad, seguridad y experiencia del paciente

Marco de calidad específico HaH: seguridad medicamentosa, evaluación ambiental, protocolos de escalamiento, preservación funcional y experiencia superior del paciente.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Seguridad medicamentosa | Conciliación al ingreso HaH, doble verificación IV, almacenamiento seguro domicilio, devolución al egreso |
| Checklist ambiental domicilio | Caídas (alfombras, iluminación, baño), seguridad O2 (no fumar, ventilación), eléctrica (enchufes, extensiones), mascotas |
| Protocolo escalamiento | Criterios retorno hospital predefinidos por patología, umbral bajo, tasa retorno ~10 % aceptable |
| Preservación funcional | Menos inmovilización que hospital, accelerómetro: +17 min/d ambulando, menos delirium (9 % vs 24 %) |
| Experiencia paciente | Confort domicilio, privacidad, sueño no interrumpido, alimentación propia, acompañamiento familiar continuo |
| Eventos adversos | Registro, análisis, clasificación (medicamentosos, caídas, deterioro, infección dispositivo) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Eventos adversos HaH | EA / 1.000 días-paciente HaH | <10 ‰ | Similar o menor a hospitalización | Levine 2020 | Mensual |
| Satisfacción paciente HaH | Score encuesta experiencia | ≥90 % | 90.7 % HaH vs 83.9 % convencional | Leff 2005 | Trimestral |
| Delirium incidente | Nuevos delirium / Total pacientes >65 años × 100 | <10 % | 9 % HaH vs 24 % convencional | Caplan 2006 | Trimestral |
| Caídas con daño | Caídas con lesión / 1.000 días-paciente | <3 ‰ | Similar hospitalización | Cochrane 2016 | Mensual |
| Checklist ambiental cumplido | Checklists completos / Total ingresos × 100 | 100 % | — | Buena práctica | Mensual |
| Tasa retorno hospital | Retornos / Total episodios × 100 | ≤10 % | 7-10 % | Levine 2020 | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Caída domiciliaria | Evaluación ambiental pre-ingreso, adaptaciones, kinesiólogo |
| Incidente con O2 domiciliario | Checklist seguridad O2, educación no fumar, ventilación |
| Subregistro de EA | Cultura reporte, entrevista egreso, seguimiento post-alta |

Ref: Levine et al. Annals IM 2020; Leff et al. JAGS 2005; Caplan et al. MJA 2006; AHRQ Patient Safety in HaH 2022; IHI Framework for Safe Reliable and Effective Care.

### 17.7 Cuidadores informales y entorno

El cuidador informal es co-productor de la atención en HaH. Requiere capacitación, soporte emocional y evaluación de sobrecarga. El entorno domiciliario debe ser clínicamente seguro.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Capacitación cuidador | Lectura dispositivos RPM, administración medicamentos orales, signos alarma por patología, cuándo llamar |
| Soporte emocional | Screening sobrecarga (Zarit abreviado), derivación apoyo psicológico, grupos pares |
| Evaluación ambiental | Visita pre-ingreso: espacio, higiene, accesibilidad, seguridad, almacenamiento medicamentos |
| Brecha digital | Evaluación alfabetización digital, capacitación en dispositivos, soporte técnico |
| Tensiones culturales | Respeto creencias, comunicación intercultural, mediador si necesario |
| Relevo cuidador | Identificar cuidador secundario, planificación turnos, reconocer fatiga |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Zarit cuidador (screening) | Cuidadores evaluados / Total cuidadores × 100 | 100 % | — | Buena práctica | Al ingreso + semanal |
| Sobrecarga cuidador (Zarit ≥24) | Cuidadores con sobrecarga / Total evaluados × 100 | <20 % | — | Zarit literature | Mensual |
| Capacitación completada | Cuidadores capacitados pre-inicio / Total × 100 | 100 % | — | Buena práctica | Por ingreso |
| Llamadas alarma apropiadas | Llamadas por signos alarma reales / Total llamadas cuidador × 100 | ≥60 % | — | Buena práctica | Mensual |
| Satisfacción cuidador | Score encuesta experiencia cuidador | ≥80 % | — | Literature HaH | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Burnout cuidador → abandono | Screening Zarit, relevo, apoyo psicosocial, respiro |
| Incapacidad digital → pérdida monitoreo | Dispositivos simplificados, soporte técnico, visita adicional enfermería |
| Conflicto familiar por decisiones | Mediación, consentimiento claro, rol definido del cuidador |
| Domicilio inseguro (no detectado) | Visita pre-ingreso obligatoria, re-evaluación periódica |

Ref: Zarit Burden Interview validación; Cuidador informal OPS 2019; Levine et al. 2020 (caregiver experience); Hospital Clínic Barcelona programa cuidador HaH.

### 17.8 Economía, sostenibilidad y reembolso

HaH reduce costos 19-38 % por episodio. Efecto backfill amplifica el impacto financiero. Modelos de pago variados según sistema sanitario.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Costo directo por episodio | 19-38 % menor que hospitalización convencional (estudios USA, Australia, España) |
| Efecto backfill | Cama liberada por HaH → ingresa paciente mayor agudeza → mayor ingreso GRD/DRG → margen incremental |
| Costos fijos programa | Centro de mando, flota, equipos RPM, stock medicamentos — requiere volumen mínimo para break-even |
| Break-even | Típicamente 8-12 pacientes simultáneos para programa sostenible |
| Costo evitado sistema | Menos IAAS, menos delirium, menos desacondicionamiento → menores costos downstream |

**Modelos de reembolso:**

| Modelo | País/Sistema | Detalle |
|--------|-------------|---------|
| DRG parity (AHCAH waiver) | USA / CMS | Mismo pago DRG que hospitalización convencional → margen para hospital por menor costo |
| Value-based | USA / ACO-REACH | Ahorro compartido, penalización reingresos, calidad |
| Capitado | Integrados (Kaiser, VA) | HaH como alternativa de menor costo dentro del per cápita |
| Presupuesto global | UK NHS / Virtual Wards | Financiamiento NHS Trusts, eficiencia cama |
| GRD nacional | España, Chile, Australia | Codificación HaH como hospitalización, mismo GRD ajustado |
| Fee-for-service ajustado | Francia | Tarifas específicas HAD (Hospitalisation à Domicile) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Costo por episodio HaH vs. convencional | Ratio costo HaH / costo convencional | ≤0.80 | 0.62-0.81 | CMS 2023; Levine 2020 | Trimestral |
| Volumen programa (census) | Pacientes simultáneos promedio | ≥8 (break-even) | JHH 15-20 | Johns Hopkins 2022 | Mensual |
| Margen backfill | Ingreso incremental por camas liberadas / mes | >0 (positivo) | — | Análisis interno | Trimestral |
| Costo por día-paciente HaH | Costo total programa / Total días-paciente | Benchmarking interno | USD 400-600/d vs 700-1200/d | USA literature | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Volumen insuficiente → programa deficitario | Criterios elegibilidad amplios, marketing interno, derivación protocolizada |
| No reconocimiento pagador | Advocacy regulatoria, evidencia local, piloto con evaluación |
| Costos ocultos (cuidador, tiempo familia) | Evaluación costo social, apoyo cuidador, comunicación transparente |

Ref: CMS AHCAH Financial Impact Report 2023; Levine et al. Annals IM 2020; Klein et al. Health Affairs 2022 (backfill); Hospital Clínic Barcelona coste-efectividad 2021.

### 17.9 Normativa, habilitación y consentimiento

Marco regulatorio para operar HaH. Consentimiento informado específico, habilitación sanitaria, privacidad de datos RPM y responsabilidad profesional.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Habilitación sanitaria | Autorización SEREMI/Servicio de Salud según normativa local, estándares de acreditación |
| Consentimiento informado | Documento específico HaH: riesgos, condiciones re-hospitalización, monitoreo, responsabilidades cuidador, derecho a retirarse |
| Privacidad datos RPM | Cumplimiento Ley 19.628 (datos personales), encriptación, consentimiento explícito para monitorización |
| Responsabilidad profesional | Cobertura seguro, protocolos de actuación, registro clínico completo en HCE |
| Derechos del paciente | Ley 20.584 aplicable en domicilio: información, consentimiento, confidencialidad, acompañamiento |
| Acreditación | Integración en proceso acreditación institucional, estándares específicos HaH |

**Contenido mínimo consentimiento HaH:**

| Sección | Contenido |
|---------|-----------|
| Naturaleza | Descripción del programa, equivalencia a hospitalización, equipo tratante |
| Riesgos | Posibilidad deterioro, tiempo respuesta, limitaciones vs. hospital |
| Monitorización | Dispositivos, frecuencia visitas, datos transmitidos, quién accede |
| Condiciones retorno | Criterios clínicos de re-hospitalización, proceso, transporte |
| Responsabilidades cuidador | Rol esperado, capacitación, límites, derecho a solicitar apoyo |
| Derecho retiro | Puede solicitar hospitalización convencional en cualquier momento, sin consecuencias |
| Privacidad | Uso de datos, almacenamiento, compartición con equipo tratante |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Consentimiento firmado | Consentimientos firmados / Total ingresos HaH × 100 | 100 % | Regulatorio | Ley 20.584 | Por ingreso |
| Cumplimiento normativo | Auditoría cumplimiento / Total ítems regulatorios × 100 | 100 % | Regulatorio | SEREMI | Anual |
| Reclamos privacidad | Reclamos relacionados privacidad/datos | 0 | — | Buena práctica | Trimestral |
| Registro clínico completo | Episodios con registro completo HCE / Total × 100 | 100 % | — | Acreditación | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Vacío normativo (Chile: no regulación HaH específica) | Resolución interna, protocolo con respaldo jurídico, advocacy MINSAL |
| Consentimiento insuficiente → litigio | Documento revisado por jurídico, checklist comprensión, testigo |
| Brecha privacidad datos RPM | Encriptación, acceso restringido, auditoría, política datos |

Ref: Ley 20.584 (Derechos del Paciente Chile); Ley 19.628 (Datos Personales); CMS AHCAH Conditions of Participation 2023; RD 1030/2006 (España — HAD); SEHAD recomendaciones jurídicas.

### 17.10 Programas internacionales de referencia

Panorama global de programas HaH consolidados. Modelos, escala, lecciones aprendidas y tendencias.

**Componentes:**

| País/Sistema | Programa | Escala | Modelo predominante | Detalle clave |
|-------------|----------|--------|---------------------|---------------|
| USA — CMS | AHCAH Waiver | >300 hospitales, >140 sistemas | Admission avoidance + ESD | Waiver extendido a 2030, pago DRG parity, 2 visitas/d RN, RPM obligatorio |
| USA — Johns Hopkins | Hospital at Home (pionero) | Desde 1995, modelo replicado globalmente | Admission avoidance | Evidencia fundacional (Leff, Levine), criterios elegibilidad de referencia |
| USA — Mount Sinai | Mobile Acute Care Team | NYC, >5.000 pacientes | Admission avoidance | Integración paramédicos, telemedicina, comunidad urbana |
| USA — MGB | Home Hospital | Boston, Mass General Brigham | Admission avoidance | RCT Levine 2020: -38 % costo, -7d LOS, satisfacción superior |
| UK — NHS | Virtual Wards | ~12.000 camas equivalentes (2024) | Ambos | Scaling nacional, RPM + visitas, integración community trusts |
| España — SEHAD | Hospitalización a Domicilio | >100 unidades, >4.000 camas | Ambos | Hospital Clínic Barcelona: referencia mundial, >30 años experiencia, 80+ camas |
| Australia | HITH (Hospital in the Home) | ~6 % días-cama Victoria | Ambos | Marco regulatorio consolidado, financiamiento estatal, evaluación AIHW |
| Francia | HAD (Hospitalisation à Domicile) | >20.000 plazas | Ambos | Financiamiento específico T2A, cobertura nacional, Fédération FNEHAD |
| Israel | Sheba, Clalit | Programas hospitalarios + HMO | Admission avoidance | Adopción rápida post-COVID, integración digital avanzada |
| Canadá | Ontario, Alberta | Programas hospitalarios provinciales | ESD predominante | Expansión post-COVID, integración home care agencies |

**Lecciones aprendidas (síntesis internacional):**

| Lección | Detalle |
|---------|---------|
| Escala mínima | 8-12 pacientes simultáneos para viabilidad operativa y financiera |
| Tecnología como enabler, no driver | RPM facilita seguridad pero no reemplaza visita presencial |
| Cultura organizacional | Requiere cambio mental: hospital sin paredes, confianza en domicilio |
| Cuidador como aliado | Capacitación y soporte emocional son inversiones, no costos |
| Regulación habilita escala | Sin marco normativo claro, programas permanecen pilotos pequeños |
| COVID como acelerador | Pandemia demostró viabilidad a escala, ahora desafío es sostener post-pandemia |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Benchmark internacional mortalidad | Mortalidad HaH propia vs. publicada | ≤benchmark | RR 0.77-0.84 | Cochrane 2016 | Anual |
| Benchmark reingresos | Reingresos HaH propios vs. publicados | ≤10 % | 7-8.6 % | Levine 2020 | Anual |
| Benchmark costo | Ratio costo propio vs. publicado | ≤0.80 | 0.62-0.81 | CMS 2023 | Anual |
| Adherencia modelo operativo | Cumplimiento estándares CMS/SEHAD / Total ítems × 100 | ≥90 % | — | CMS/SEHAD | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Trasplantar modelo sin adaptación local | Contextualización: geografía, cultura, sistema salud, regulación |
| Dependencia de waiver/excepción regulatoria | Advocacy para regulación permanente, evidencia local |
| Post-COVID deceleration | Institucionalización, demostración valor financiero sostenido |

Ref: CMS AHCAH Waiver Extension 2024; Leff et al. JAGS 2005; Levine et al. Annals IM 2020; NHS England Virtual Wards 2024; SEHAD España; FNEHAD Francia; AIHW HITH Australia 2023; Hospital Clínic Barcelona HaD.
