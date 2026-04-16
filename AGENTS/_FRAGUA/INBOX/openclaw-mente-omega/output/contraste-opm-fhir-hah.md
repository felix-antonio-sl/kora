# Contraste: Modelo OPM HODOM vs HL7 FHIR vs Corpus HaH Internacional

## Encuadre

Se contrastan tres artefactos de naturaleza distinta:

1. **Modelo OPM HODOM** — modelo conceptual de sistema (ISO 19450) construido desde la normativa chilena (DS 1/2022, NT 2024, DEIS REM A21). Captura estructura, procesos, agentes, instrumentos y estados del sistema de hospitalización domiciliaria tal como lo regula Chile.

2. **HL7 FHIR R5** — estándar de interoperabilidad para intercambio de datos clínicos. No modela sistemas; define recursos (estructuras de datos) y sus relaciones para que sistemas heterogéneos se comuniquen.

3. **Corpus HaH** — compilación de 113+ fuentes de evidencia internacional sobre Hospital at Home. Describe lo que la evidencia dice que funciona, falla, cuesta y produce en outcomes clínicos.

Son tres capas complementarias: el OPM modela el *qué es* del sistema chileno; FHIR define el *cómo se representan los datos* para interoperar; el corpus captura el *qué dice la evidencia* sobre qué funciona. El contraste identifica brechas, alineamientos y oportunidades de integración.

---

## I. MAPEO OPM → FHIR: Correspondencia Recurso por Recurso

### Entidades del SD (Nivel 0)

| Entidad OPM | Recurso FHIR | Cobertura | Tensión |
|---|---|---|---|
| **Patient Group** | `Patient` | Alta | FHIR modela paciente individual, no grupo. Para cohorte: `Group` |
| **Clinical Condition** (estados: agudo/reagudizado → recuperado) | `Condition` + `ClinicalStatus` (active, resolved) | Alta | FHIR usa terminología estandarizada (SNOMED CT, ICD-10). El modelo OPM usa estados binarios sin binding terminológico |
| **Healthcare Team** | `CareTeam` + `PractitionerRole` + `Practitioner` | Alta | FHIR descompone hasta el rol individual con período de participación. OPM agrupa en SD2 con roles similares |
| **Domiciliary Hospitalization System** | `Organization` + `HealthcareService` | Parcial | FHIR no tiene un recurso "sistema de salud domiciliario" nativo. Se modela como Organization que ofrece HealthcareService tipo hospital-at-home |
| **Medical Equipment** | `Device` + `DeviceDefinition` | Alta | FHIR tiene granularidad de dispositivo individual con UDI, estado de mantenimiento, calibración |
| **Communication System** | Sin recurso directo | Baja | FHIR no modela infraestructura de telecomunicaciones. Sí tiene `Communication` para mensajes clínicos |
| **Transport Vehicle** | `Transport` (R5) | Media | Recurso nuevo en R5, maturity 1. Cubre logística de transporte de personas/especímenes |
| **Administrative Infrastructure** | `Location` | Parcial | Location modela lugares físicos (oficina UHD, bodega). No cubre infraestructura eléctrica o de residuos |
| **Clinical Supply** | `SupplyDelivery` + `SupplyRequest` | Media | FHIR modela el flujo de suministros, no el inventario estático. `InventoryItem` (R5, maturity 0) es incipiente |
| **Medication** | `Medication` + `MedicationRequest` + `MedicationAdministration` | Alta | Cobertura madura. Incluye prescripción, dispensación y administración con trazabilidad completa |
| **Clinical Record** | `DocumentReference` + `Composition` | Alta | FHIR soporta documentos clínicos estructurados y no estructurados |
| **Patient Home** | `Location` (type: patient's home) | Alta | Location con tipo "kind" = pa (patient's home). Soporta dirección, coordenadas, accesibilidad |
| **Inpatient Facility** | `Organization` + `Location` | Alta | Modelo maduro para establecimientos de salud |
| **Current Regulation** | Sin recurso directo | Nula | FHIR no modela normativa legal. La conformidad regulatoria es externa al estándar |

### Procesos del SD1 (Flujo Clínico)

| Proceso OPM | Recurso(s) FHIR | Patrón de workflow | Tensión |
|---|---|---|---|
| *Eligibility Evaluating* | `ServiceRequest` (status: draft → active) + criterios como `Questionnaire`/`QuestionnaireResponse` | Request pattern | FHIR no tiene recurso nativo de elegibilidad clínica domiciliaria. Los criterios de exclusión del SD8 serían `DetectedIssue` o extensions |
| *Patient Admitting* | `Encounter` (status: planned → in-progress, class: HH) + `EpisodeOfCare` | Event pattern | `Encounter.class` = HH (home health) es el mapeo directo. `EpisodeOfCare` envuelve el episodio completo |
| *Care Planning* | `CarePlan` (status: draft → active) + `Goal` | Request pattern | Cobertura alta. CarePlan referencia Condition, CareTeam, Goal, Activity |
| *Therapeutic Plan Executing* | `Procedure` + `MedicationAdministration` + `Encounter` (visitas) | Event pattern | Cada visita domiciliaria = un Encounter hijo del EpisodeOfCare. Procedimientos y administraciones se registran como eventos |
| *Clinical Evolution Monitoring* | `Observation` (signos vitales) + `ClinicalImpression` | Event pattern | Observation es normativo (maturity N). Panel de signos vitales estandarizado. ClinicalImpression captura la evaluación clínica |
| *Patient Discharging* | `Encounter` (status: finished) + `EpisodeOfCare` (status: finished) | Event pattern | Los 6 tipos de egreso del SD1.6 se mapean a `Encounter.dischargeDisposition` con ValueSet extensible |

### Objetos Informaticales del SD1

| Objeto OPM | Recurso FHIR | Notas |
|---|---|---|
| **Informed Consent** | `Consent` | Recurso dedicado (maturity 2). Soporta scope, category, provision |
| **Therapeutic Plan** | `CarePlan` | Mapeo directo |
| **Nursing Care Plan** | `CarePlan` (con category = nursing) | Mismo recurso, diferente categoría |
| **Epicrisis** | `Composition` (type = discharge summary) | Composition con DocumentReference |
| **Satisfaction Survey** | `QuestionnaireResponse` | Questionnaire define la encuesta; QR registra respuestas |
| **Derivation Origin** | `Encounter.hospitalization.admitSource` | ValueSet extensible para origen de derivación |
| **Vital Signs Data** | `Observation` (category = vital-signs) | Perfiles estandarizados: BP, HR, RR, SpO2, Temperature |
| **Visit Schedule** | `Appointment` + `Schedule` + `Slot` | Modelo maduro de agendamiento |

### Lo que FHIR agrega que el modelo OPM no cubre

| Capacidad FHIR | Relevancia para HODOM | Prioridad |
|---|---|---|
| **Terminología estandarizada** (SNOMED CT, ICD-10-CL, LOINC) | Codificación de diagnósticos, procedimientos, observaciones. El modelo OPM usa nombres descriptivos sin binding | ALTA |
| **API RESTful** (CRUD + search + operations) | Interoperabilidad entre UHD, hospital derivador, APS, DEIS | ALTA |
| **Subscription/Notification** (R5) | Alertas en tiempo real: deterioro clínico, cumplimiento de visitas | MEDIA |
| **Provenance + AuditEvent** | Trazabilidad de quién hizo qué, cuándo, en qué contexto. Requisito de la NT 2024 (trazabilidad de llamadas) | ALTA |
| **Coverage + Claim** | Modelo financiero: previsión, facturación FONASA/ISAPRE, PPV | MEDIA |
| **MeasureReport** | Reporte estadístico tipo DEIS REM A21. Medidas de calidad e indicadores | ALTA |
| **Consent granular** (provision, except, data) | Consentimiento informado con granularidad de datos compartidos, períodos, excepciones | MEDIA |
| **Security labels + compartments** | Control de acceso a datos domiciliarios. Patient compartment aísla datos por paciente | ALTA |

### Lo que el modelo OPM cubre y FHIR no modela nativamente

| Capacidad OPM | Limitación FHIR |
|---|---|
| **Procesos de gobernanza** (SD6: autorización sanitaria, calidad, capacitación, residuos, mantención, capacidad) | FHIR es un estándar de datos, no de gestión organizacional. Estos procesos son dominio de sistemas ERP/calidad |
| **Exclusiones del sistema** (SD8: condiciones que impiden ingreso) | FHIR soporta criterios de elegibilidad vía PlanDefinition + Library, pero no tiene un patrón nativo de exclusión de programa |
| **Relaciones institucionales etiquetadas** (SD9: SEREMI supervisa, Director Técnico representa) | FHIR modela relaciones organizacionales vía OrganizationAffiliation, pero las relaciones regulatorias son externas |
| **Problem occurrence** (Acute Episode Occurring como proceso ambiental) | FHIR modela condiciones, no la causalidad sistémica del episodio agudo como trigger ambiental |
| **Capacidad instalada** (cupos programados/utilizados/disponibles) | Sin recurso nativo de capacity management. Se implementaría con extensions sobre HealthcareService o Location |
| **Sistema documental completo** (SD5: manuales, protocolos, plan de capacitación) | FHIR puede referenciar documentos vía DocumentReference, pero no modela el corpus documental regulatorio como estructura |

---

## II. CONTRASTE OPM vs CORPUS HaH: Modelo Regulatorio Chileno vs Evidencia Internacional

### A. Alineamientos Fuertes

| Dimensión | Modelo OPM (Chile) | Corpus HaH | Valoración |
|---|---|---|---|
| **Equipo multidisciplinario** | SD2: 9 roles mínimos + 4 complementarios (médico, enfermera, kinesiólogo, TS, TENS, etc.) | F08 Nikmanesh: comunicación/coordinación en top-7 componentes. F34 Presbyterian: equipo incluye médico, enfermeras, paramédicos, terapeutas, TS | ✅ Alineado. El modelo chileno es más prescriptivo que la mayoría de modelos internacionales en composición mínima |
| **Consentimiento informado** | SD1.1: proceso explícito con carta de derechos y deberes | F17 Nature Medicine: consentimiento informado como dimensión ética clave. F75 Milbank: "consentimiento financiero informado" propuesto | ✅ Alineado. Chile lo norma como requisito; la evidencia lo confirma como necesario |
| **Criterios de elegibilidad** | SD8: 5 tipos de exclusión + condiciones de domicilio (SD7) | F02 Levine: exclusiones por instituciones, sustancias controladas, alto riesgo. F24 HTA NY: criterios excluyen inseguridad habitacional, falta de tecnología | ✅ Alineado en lógica, pero Chile es más restrictivo en condiciones de vivienda |
| **Tipos de egreso** | SD1.6: 6 tipos (alta médica, reingreso, fallecimiento esperado/no esperado, renuncia, disciplinaria) | DEIS REM A21: misma clasificación. F24 HTA NY: escalación 7.2%, >90% completan en domicilio | ✅ Alineado con clasificación DEIS. Consistente con tasas internacionales |
| **Satisfacción como outcome** | SD1: Satisfaction Survey como resultado del proceso de egreso | F01 Cochrane: satisfacción superior en HaH. 5/5 RCTs en HTA NY: igual o superior | ✅ Alineado. La medición es consistente con la evidencia |
| **Cuidador como enabler** | SD1: Caregiver con estado available/unavailable como precondición | F75 Milbank: "Gasto promedio cuidador: 24h/semana + gastos de bolsillo". F42 JAGS: prioridad abordar SDOH | ✅ Alineado en requerimiento; la evidencia alerta sobre carga oculta al cuidador |

### B. Brechas del Modelo Chileno respecto a la Evidencia Internacional

| Brecha | En el Modelo OPM | En el Corpus HaH | Severidad | Recomendación |
|---|---|---|---|---|
| **Remote Patient Monitoring (RPM)** | No modelado. Communication System es genérico (teléfono, TI) | F05 Levine 2024 npj: sensores biofísicos (PPG, acústicos, mecánicos), parches torácicos, wearables. F02 Levine 2020: VitalConnect patch + tablet para monitoreo remoto continuo. F54 CADTH: RPM con signos vitales + tablets + videollamadas | 🔴 ALTA | Agregar RPM como instrumento especializado del SD. Es la brecha tecnológica más significativa entre la regulación chilena y el estado del arte internacional |
| **Admisión por evitación (AA) vs alta temprana (ESD)** | El modelo no distingue entre modelos AA y ESD. DEIS registra origen de derivación pero no tipifica el modelo | F06 Leong 2021 umbrella: "Priorizar AA sobre ESD por beneficios potenciales en costos y outcomes". F24 HTA NY: todos los estudios elegibles son AA | 🟡 MEDIA | Agregar Hospitalization Model como atributo discriminante de EpisodeOfCare. La distinción tiene implicaciones clínicas y de outcomes |
| **Medición de outcomes clínicos estandarizados** | El modelo captura estado (agudo → recuperado) pero no métricas de resultado intermedias | F24 HTA NY: mortalidad 30d/90d/6m, reingresos 30d, LOS, traslado a larga estancia, costos. F44 Thomsen RCT: EQ-5D-5L como outcome primario | 🔴 ALTA | Integrar Outcome Measurement como proceso de SD6 (gobernanza). Definir indicadores clave: mortalidad no anticipada (0.36% MedPAC), escalación (7.2%), reingresos |
| **Equidad y determinantes sociales** | SD7 captura condiciones del domicilio (servicios básicos, telefonía, acceso vial) pero no SDOH | F40 Equity UK SR: VWs pueden amplificar inequidades existentes. F10 CMS: pacientes AHCAH más blancos, urbanos, menos Medicaid. F41 Mayo: variables a nivel de código postal influyen en outcomes | 🟡 MEDIA | Agregar Social Determinant Assessment como subproceso de Eligibility Evaluating. Modelar riesgo de exclusión digital y socioeconómica |
| **Costo-efectividad** | No modelado. El sistema regulatorio chileno no exige análisis de costos al sistema HD | F02 Levine 2020: costo agudo 38% menor. F03 Leff 2005: 32% menor. F37 Australia: primera RS de costos en desarrollo. F39 Health Affairs: HaH $10.500 vs $17.500 hospital | 🟡 MEDIA | No es brecha del modelo conceptual sino del marco regulatorio. Sin embargo, SD6 podría incluir Cost-Effectiveness Managing |
| **Rehabilitación integrada** | SD1.4: Kinesiological Therapy (motora/respiratoria) es el único componente rehabilitador | F74 Corpus: CMS AHCAH incluye terapia física, ocupacional y del habla como servicios requeridos. F03 Leff: función a 2 semanas sin diferencias en ADL/IADL | 🟡 MEDIA | El modelo ya incluye Fonoaudiólogo y Terapeuta Ocupacional como profesionales complementarios (SD2). Faltaría modelar sus intervenciones como subprocesos paralelos de SD1.4 |
| **Salud mental** | El DEIS reporta Cupos de Salud Mental pero el modelo no descompone el pathway | F52 Corpus: "Brecha mayor. Sin RS ni RCTs específicos de HaH para salud mental aguda" | 🟠 BAJA | Brecha compartida: ni el modelo chileno ni la evidencia internacional la resuelven. La capacidad del modelo de incluir Mental Health Slots es un primer paso |
| **Pediátrico** | DEIS distingue cupos adulto/pediátrico. El modelo no diferencia pathways | F50 Corpus: 1 solo RCT pediátrico UK. F51 AAP: campo incipiente | 🟠 BAJA | Brecha compartida. La regulación chilena permite pediatría; la evidencia internacional es insuficiente |
| **IA y analítica predictiva** | No modelado | F59-F60 Corpus: LLMs para procesamiento datos; ML para alertas tempranas. Campo emergente, no maduro | 🟠 BAJA | No es brecha actual sino oportunidad futura. El modelo es extensible |

### C. Fortalezas del Modelo Chileno no presentes en la Evidencia Internacional

| Fortaleza | Detalle | Relevancia |
|---|---|---|
| **Marco regulatorio formal** | DS 1/2022 como decreto con fuerza de ley + NT 2024 + DEIS. La mayoría de países HaH operan bajo waivers temporales (CMS AHCAH expiró sept 2025) o sin marco propio | ALTA. Chile tiene marco permanente; EE.UU. depende de extensiones congresionales |
| **Autorización sanitaria con vigencia** | SD6: SEREMI autoriza con vigencia 0-3 años. Proceso de supervisión estatal explícito | ALTA. La evidencia internacional (F31 Appelbaum) critica la falta de estándares, medición y auditoría en EE.UU. |
| **Sistema documental prescriptivo** | SD5: 6 protocolos clínicos obligatorios, manual de procedimientos, plan de capacitación con inducción ≥44h | ALTA. F25 Cochrane qualitative: "protocolos claros" como facilitador clave de implementación |
| **Distinción fallecimiento esperado/no esperado** | SD1.6: modelado como especializaciones separadas del egreso, conforme DEIS | MEDIA. La mayoría de los estudios internacionales reportan mortalidad agregada sin distinguir intención paliativa |
| **Capacidad instalada como variable de gestión** | SD6: cupos programados/utilizados/disponibles + campaña invierno + salud mental | MEDIA. F11 MedPAC reporta concentración (26 hospitales = 71% altas) pero no modela capacidad instalada como indicador |
| **Médico regulador 24/7** | SD2: rol explícito de regulación a distancia con atención remota 24/7 | ALTA. F11 MedPAC waiver: requiere "conexión audio remota on-demand" pero sin rol diferenciado de médico regulador |

---

## III. SÍNTESIS: TRES CAPAS DE UN MISMO PROBLEMA

```
┌─────────────────────────────────────────────────┐
│  EVIDENCIA (Corpus HaH)                         │
│  Qué funciona, qué no, a qué costo, con qué    │
│  outcomes. 113+ fuentes, 28 ejes temáticos.     │
│  Informa diseño y evaluación.                   │
├─────────────────────────────────────────────────┤
│  MODELO CONCEPTUAL (OPM HODOM)                  │
│  Estructura, procesos, agentes, instrumentos,   │
│  estados. 16 OPDs, ~246 entidades.              │
│  Diseño del sistema según normativa chilena.    │
├─────────────────────────────────────────────────┤
│  INTEROPERABILIDAD (HL7 FHIR R5)                │
│  Recursos, APIs, terminología, seguridad.       │
│  150+ recursos, RESTful, extensible.            │
│  Implementación técnica del intercambio.        │
└─────────────────────────────────────────────────┘
```

### Hallazgos principales

1. **El modelo OPM es más completo que cualquier modelo HaH individual del corpus en estructura regulatoria.** Captura 16 OPDs con gobernanza, documentación, capacidad y exclusiones que ningún estudio internacional modela con esa profundidad.

2. **La brecha más crítica del modelo es tecnológica: RPM.** La evidencia internacional ha convergido en que el monitoreo remoto continuo (parches, wearables, tablets) es un componente activo de las intervenciones HaH efectivas. El modelo chileno se queda en "Sistema de Comunicación" (teléfono + TI), que es insuficiente para capturar esta dimensión.

3. **FHIR es la capa de implementación natural.** Todo el modelo OPM es representable en FHIR, pero hacerlo requiere: (a) perfiles chilenos (IG nacional) para Encounter class HH, CarePlan de HD, CareTeam de UHD; (b) terminología local (ICD-10-CL, códigos FONASA); (c) extensions para capacidad instalada, origen de derivación DEIS, cupos.

4. **La evidencia de outcomes no tiene expresión en el modelo conceptual ni en la capa FHIR actual.** Los meta-análisis del corpus (mortalidad, reingresos, costos, satisfacción) deberían alimentar un circuito de calidad modelado en SD6 y reportado vía FHIR MeasureReport.

5. **El modelo chileno tiene una ventaja estructural sobre el waiver estadounidense:** marco legal permanente vs extensiones congresionales temporales. Pero carece de la infraestructura de medición de outcomes que la CMS sí tiene (N=11.907 pacientes HaH + 643.634 controles comparativos).

### Recomendaciones priorizadas

| # | Acción | Capa | Esfuerzo | Impacto |
|---|---|---|---|---|
| 1 | Agregar RPM como instrumento especializado del SD con subprocesos en SD1.4 y SD1.5 | OPM | Medio | 🔴 Alto |
| 2 | Diseñar FHIR Implementation Guide chileno para HD (Encounter HH, CarePlan HD, CareTeam UHD, perfiles de Observation para signos vitales domiciliarios) | FHIR | Alto | 🔴 Alto |
| 3 | Agregar Outcome Measurement como proceso de gobernanza en SD6 con indicadores del corpus (mortalidad no anticipada, escalación, reingresos 30d) | OPM | Bajo | 🔴 Alto |
| 4 | Modelar AA vs ESD como atributo discriminante del episodio HD | OPM | Bajo | 🟡 Medio |
| 5 | Integrar SDOH Assessment en Eligibility Evaluating (SD1.1) alineado con FHIR Gravity Project | OPM+FHIR | Medio | 🟡 Medio |
| 6 | Diseñar MeasureReport DEIS para reporte estadístico REM A21 C.1 vía FHIR | FHIR | Medio | 🟡 Medio |
| 7 | Expandir intervenciones terapéuticas de SD1.4 (agregar Fonoaudiología, TO, Psicología como subprocesos) | OPM | Bajo | 🟠 Bajo |
| 8 | Modelar pathway pediátrico como variante condicional del flujo principal | OPM | Medio | 🟠 Bajo |
