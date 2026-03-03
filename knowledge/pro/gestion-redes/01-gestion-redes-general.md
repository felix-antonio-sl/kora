---
_manifest:
  urn: "urn:pro:kb:gestion-redes-general"
  provenance:
    created_by: "FS"
    created_at: "2026-03-03"
    source: "Síntesis multi-fuente: OPS, IHI, NICE, AHRQ, MINSAL, Cochrane"
version: "2.0.0"
status: draft
tags: [gestion-redes, gobernanza, calidad, procesos, digital, finanzas, cambio, red-asistencial]
lang: es
---

# Gestión de Redes Asistenciales — Marco General

## 1. Fundamentos y marco conceptual

### 1.1 Red integrada, continuidad, niveles de atención

Estructura organizacional que articula establecimientos de distintos niveles de complejidad para garantizar continuidad asistencial longitudinal, relacional e informacional.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| APS | Puerta de entrada, resolutividad ≥85 %, adscripción territorial |
| Nivel secundario | Especialidades ambulatorias, CDT/CRS, hospital de día |
| Nivel terciario | Alta complejidad, UCI/UTI, cirugía mayor, trasplantes |
| Continuidad informacional | HCE compartida, resumen de alta estandarizado (HL7 CDA) |
| Continuidad relacional | Médico de cabecera, equipo de sector, panel asignado |
| Continuidad gestional | Protocolos de derivación-contrarreferencia bidireccional |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Resolutividad APS | Consultas resueltas APS / Total consultas × 100 | ≥85 % | OCDE 85-90 % | OCDE 2023 | Trimestral |
| Tasa de referencia | Derivaciones / Consultas APS × 100 | ≤15 % | UK NHS 5-10 % | NHS England 2022 | Mensual |
| Continuidad relacional (UPC) | Consultas con mismo médico / Total consultas | ≥0.75 | — | Jee & Cabana 2006 | Semestral |
| Contrarreferencia efectiva | Contrarreferencias recibidas / Derivaciones enviadas × 100 | ≥80 % | — | MINSAL 2019 | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Fragmentación de la red | Gobernanza compartida, convenios interinstitucionales |
| Pérdida de seguimiento post-derivación | Trazabilidad electrónica, navigator de pacientes |
| Sobreuso nivel terciario | Fortalecimiento resolutividad APS, telemedicina |

Ref: Ley 19.937 (Autoridad Sanitaria); OPS/OMS RISS 2010; Starfield 1998; WHO Framework on Integrated People-Centred Health Services 2016.

### 1.2 Cuádruple Meta

Marco estratégico que alinea cuatro objetivos simultáneos: experiencia del paciente, salud poblacional, costo per cápita y bienestar del equipo de salud.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Experiencia del paciente | PREMs, NPS, tiempos de espera percibidos |
| Salud poblacional | AVPP, AVISA, prevalencia condiciones crónicas |
| Costo per cápita | Gasto total / población adscrita, ajustado por riesgo |
| Bienestar del equipo | Burnout (MBI), satisfacción laboral, rotación |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| NPS pacientes | % Promotores − % Detractores | ≥50 | Top quartile ≥62 | Press Ganey 2023 | Trimestral |
| AVPP | Años de vida potencial perdidos / 100.000 hab | Reducción ≥2 %/año | OCDE promedio 3.400 | OCDE 2023 | Anual |
| Costo per cápita ajustado | Gasto total / Población ajustada por ACG | Crecimiento ≤IPC+1 % | — | IHI 2019 | Anual |
| Burnout equipo (MBI) | % personal con agotamiento emocional alto | ≤25 % | EE.UU. 44 % (2022) | Shanafelt 2022 | Semestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Optimizar una meta a expensas de otra | Tablero balanceado con las 4 dimensiones |
| Bienestar como retórica sin acción | Indicadores de bienestar en evaluación directiva |

Ref: IHI Triple Aim 2008; Bodenheimer & Sinsky 2014 (Quadruple Aim); OCDE Health at a Glance 2023.

### 1.3 Topología de red

Configuración estructural de nodos asistenciales y sus conexiones según modelo geográfico-funcional.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Hub & spoke | Hospital base (hub) + establecimientos satélite (spokes) |
| Integración vertical | Articulación entre niveles (APS→secundario→terciario) |
| Integración horizontal | Coordinación entre establecimientos del mismo nivel |
| Regionalización | Asignación territorial de población a nodos específicos |
| Redes temáticas | Redes funcionales por patología (oncología, cardiovascular, trauma) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cobertura geográfica | Población a ≤30 min del nodo más cercano / Población total × 100 | ≥90 % | — | OPS 2020 | Anual |
| Densidad de red | Nodos operativos / 100.000 hab | Según norma país | OCDE 3.0 camas/1.000 hab | OCDE 2023 | Anual |
| Índice de conectividad | Enlaces activos / Enlaces posibles entre nodos | ≥0.6 | — | Análisis de red social | Semestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Duplicación de servicios entre nodos | Cartera de servicios diferenciada por nivel |
| Brechas de acceso rural | Telemedicina, postas rurales, rondas médicas |

Ref: OPS Redes Integradas 2010; Shortell 2000; Provan & Milward 1995 (network effectiveness).

### 1.4 Determinantes sociales, equidad e interculturalidad

Incorporación sistemática de factores socioeconómicos, culturales y territoriales en planificación y operación de la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Determinantes estructurales | Ingreso, educación, empleo, vivienda, ruralidad |
| Determinantes intermediarios | Conductas, exposiciones ambientales, acceso a servicios |
| Equidad en acceso | Ajuste de oferta por vulnerabilidad (FONASA A-B priorizado) |
| Pertinencia cultural | Facilitadores interculturales, protocolos pueblos originarios |
| Enfoque de género | Brechas de acceso y resultados por sexo/género |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Brecha de mortalidad evitable | Tasa AVPP quintil I / Tasa AVPP quintil V | ≤1.5 | UK ≤1.3 | MINSAL-DEIS 2023 | Anual |
| Cobertura controles crónicos en FONASA A | % cobertura vs. % población FONASA A | Razón ≥1.0 | — | MINSAL 2023 | Semestral |
| Satisfacción pueblos originarios | PREMs ajustados por pertinencia cultural | ≥70 % | — | MINSAL Intercultural 2021 | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Universalismo sin focalización | Estratificación por ISAPRE/FONASA tramo + índice vulnerabilidad |
| Tokenismo intercultural | Participación vinculante de comunidades indígenas |

Ref: OMS CDSS 2008; Marmot Review 2010; Ley 20.584 art. 7 (pertinencia cultural); MINSAL Política de Salud Intercultural 2006.

### 1.5 Ética, derechos y experiencia del paciente

Marco normativo-ético que garantiza derechos, consentimiento informado, participación y trato digno en la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Derechos del paciente | Información, consentimiento, segunda opinión, acompañamiento, reclamo |
| Consentimiento informado | Proceso documentado, capacidad, voluntades anticipadas |
| Comité de ética asistencial | Consultas caso a caso, proporcionalidad, futilidad |
| Participación ciudadana | Consejos consultivos, encuestas, codiseño |
| Experiencia del paciente | Journey mapping, PREMs, gestión de reclamos OIRS |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Reclamos OIRS | N° reclamos / 1.000 egresos | ≤5 | — | MINSAL 2023 | Mensual |
| Consentimiento documentado | % procedimientos con CI firmado / Total procedimientos | 100 % | 100 % | Ley 20.584 | Mensual |
| Respuesta reclamos ≤15 días | Reclamos respondidos en plazo / Total reclamos × 100 | ≥90 % | — | Ley 19.880 | Mensual |
| Satisfacción global | PREMs score agregado | ≥80 % | NHS 75 % | NHS Patient Survey 2023 | Semestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Consentimiento como trámite burocrático | Capacitación en comunicación, check de comprensión |
| Subregistro de reclamos | Canal digital + presencial, cultura no punitiva |

Ref: Ley 20.584 (Derechos y Deberes); Ley 20.120 (Investigación en humanos); Beauchamp & Childress 2019; NHS Patient Experience Framework 2023.

## 2. Gobernanza y arquitectura decisional

### 2.1 Modelo de gobierno de la red

Estructura formal de gobernanza que define órganos, roles y mecanismos de toma de decisiones a nivel de red asistencial.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Consejo directivo de red | Directores de establecimientos, Servicio de Salud, representantes APS |
| Gobernanza clínica | Comités técnicos por línea (médico-quirúrgico, materno-infantil, salud mental) |
| Charter de red | Documento constitutivo: misión, alcance, autoridad, rendición de cuentas |
| Secretaría técnica | Equipo permanente de coordinación, agenda, actas, seguimiento |
| Participación comunitaria | Consejo consultivo de usuarios integrado a gobernanza |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Sesiones consejo directivo | N° sesiones realizadas / N° programadas × 100 | ≥90 % | — | Gestión interna | Trimestral |
| Acuerdos implementados | Acuerdos ejecutados / Acuerdos tomados × 100 | ≥80 % | — | Actas consejo | Semestral |
| Participación activa miembros | Asistencia promedio / Miembros totales × 100 | ≥75 % | — | Gestión interna | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Gobernanza nominal sin poder efectivo | Charter con mandato explícito y presupuesto asignado |
| Captura por un establecimiento dominante | Rotación de presidencia, voto ponderado |

Ref: Ley 19.937 (Servicios de Salud); NHS Clinical Governance Framework 2019; OPS Gobernanza RISS 2010.

### 2.2 Arquitectura decisional

Catálogo explícito de decisiones, niveles de autoridad y procesos de escalamiento en la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Catálogo de decisiones | Inventario tipificado: operativas, tácticas, estratégicas |
| Matriz RACI | Responsable, Aprobador, Consultado, Informado por tipo de decisión |
| Niveles de autoridad | Local (establecimiento), red (comité), Servicio de Salud, MINSAL |
| Delegación formal | Resoluciones exentas con límites definidos (monto, alcance) |
| Trazabilidad | Registro digital de decisiones, fundamentos y resultados |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Decisiones con RACI definido | Decisiones con RACI / Total decisiones catálogo × 100 | 100 % | — | Gestión interna | Semestral |
| Tiempo promedio decisión táctica | Días desde solicitud hasta resolución | ≤5 días | — | Sistema de gestión | Mensual |
| Escalamientos fuera de protocolo | N° escalamientos no protocolizados / Total escalamientos × 100 | ≤10 % | — | Registro escalamientos | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Parálisis por exceso de niveles | Simplificar a máximo 3 niveles de aprobación |
| Decisiones sin registro | Sistema digital obligatorio con firma electrónica |

Ref: MINSAL Orientaciones Gestión en Red 2018; ISO 9001:2015 §5.3 (roles y autoridades); RACI framework PMI 2021.

### 2.3 Coordinación interinstitucional

Mecanismos formales de articulación entre instituciones de la red (públicas, privadas, intersectoriales).

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Convenios marco | Acuerdos institucionales con alcance, plazos, financiamiento |
| Convenios docente-asistenciales | Campos clínicos, supervisión, acreditación ASOFAMECH |
| eReferral | Derivación electrónica estandarizada con tracking bidireccional |
| Mesas intersectoriales | Educación, vivienda, desarrollo social (Chile Crece Contigo, SENDA) |
| Compra de servicios | Licitaciones y convenios con prestadores privados (PPV, CAEC) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Convenios vigentes | N° convenios activos / N° convenios requeridos × 100 | ≥90 % | — | Subdirección gestión | Semestral |
| Derivaciones electrónicas | Derivaciones vía eReferral / Total derivaciones × 100 | ≥80 % | NZ 95 % | NZ Health 2022 | Trimestral |
| Cumplimiento SLA convenios | Prestaciones en plazo / Prestaciones comprometidas × 100 | ≥85 % | — | Gestión convenios | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Convenios sin monitoreo | Tablero de seguimiento con alertas automáticas |
| Dependencia excesiva sector privado | Plan de contingencia con capacidad pública de respaldo |

Ref: Ley 19.937 art. 26 (convenios); Ley 19.886 (compras públicas); NHS e-Referral Service 2021; NZ Integrated Care Framework 2022.

### 2.4 Contratos de gestión y SLA

Instrumentos formales que definen compromisos, metas, indicadores y consecuencias entre niveles de la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Compromisos de gestión | Metas anuales Servicio de Salud–MINSAL (Ley 19.937) |
| Convenios de desempeño | Acuerdos director de establecimiento–Servicio de Salud |
| SLA internos | Acuerdos de servicio entre unidades (laboratorio, imagenología, farmacia) |
| Incentivos | Asignación de desempeño colectivo (Ley 19.813), COMGES |
| Penalidades | Planes de mejora obligatorios ante incumplimiento >2 trimestres |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cumplimiento COMGES | Metas cumplidas / Metas comprometidas × 100 | ≥90 % | — | MINSAL-COMGES | Trimestral |
| SLA laboratorio (TAT) | Muestras informadas en plazo / Total muestras × 100 | ≥95 % | CAP ≥90 % | CAP 2023 | Mensual |
| SLA imagenología | Informes entregados ≤24h / Total informes × 100 | ≥90 % | ACR ≥85 % | ACR 2022 | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Gaming de indicadores | Auditoría cruzada, indicadores de resultado (no solo proceso) |
| SLA desactualizados | Revisión anual con benchmark externo |

Ref: Ley 19.937 art. 25 (compromisos de gestión); Ley 19.813 (asignación desempeño); MINSAL COMGES 2024; CAP Laboratory Accreditation 2023.

### 2.5 Gestión de conflictos y escalamiento

Protocolos para resolver disputas entre actores de la red, con niveles progresivos de intervención.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Nivel 1 — Negociación directa | Entre jefaturas involucradas, plazo 5 días |
| Nivel 2 — Mediación | Secretaría técnica de red como facilitador, plazo 10 días |
| Nivel 3 — Arbitraje | Consejo directivo de red resuelve con carácter vinculante |
| Nivel 4 — Escalamiento institucional | Director Servicio de Salud / Subsecretaría de Redes |
| Registro de conflictos | Base de datos con tipología, resolución y tiempo |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Resolución en Nivel 1 | Conflictos resueltos N1 / Total conflictos × 100 | ≥60 % | — | Registro conflictos | Trimestral |
| Tiempo medio resolución | Días promedio desde detección hasta cierre | ≤15 días | — | Registro conflictos | Trimestral |
| Recurrencia | Conflictos repetidos misma díada / Total conflictos × 100 | ≤10 % | — | Registro conflictos | Semestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Conflictos no reportados | Canal anónimo, cultura de resolución temprana |
| Escalamiento prematuro | Checklist obligatorio de agotamiento de nivel previo |

Ref: MINSAL Orientaciones Gestión en Red 2018; Thomas-Kilmann Conflict Model; NHS Dispute Resolution Framework 2020.

## 3. Planificación estratégica de la red

### 3.1 Análisis poblacional

Caracterización demográfica, epidemiológica y socioeconómica de la población adscrita como base de planificación.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Pirámide poblacional | Estructura etaria, proyecciones INE, envejecimiento |
| Carga de enfermedad | AVISA, AVPP, principales GBD por territorio |
| Perfil epidemiológico | Prevalencia crónicas (DM2, HTA, EPOC, SM), incidencia cáncer |
| Mapa socioeconómico | Quintiles ingreso, Registro Social de Hogares, ruralidad |
| Demanda histórica | Series temporales de consultas, egresos, urgencias (≥3 años) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tasa de uso servicios | Consultas (o egresos) / Población adscrita × 1.000 | Según norma | OCDE 6.8 consultas/hab | OCDE 2023 | Anual |
| Razón de dependencia | (Pob <15 + Pob ≥65) / Pob 15-64 × 100 | Monitorear tendencia | Chile 52 % (2023) | INE 2023 | Anual |
| Brechas de prevalencia vs. bajo control | % bajo control / % prevalencia estimada × 100 | ≥60 % | UK QOF 70-80 % | MINSAL ENS 2017 | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Datos desactualizados | Actualización anual con DEIS, INE, Registro Social |
| Subregistro epidemiológico | Cruce fuentes (GRD, GES, notificación obligatoria) |

Ref: MINSAL-DEIS Estadísticas; INE Proyecciones Poblacionales 2023; GBD Study 2019; OCDE Health at a Glance 2023.

### 3.2 Estratificación de riesgo

Clasificación poblacional por nivel de riesgo clínico-social para asignación diferenciada de recursos y seguimiento.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Modelos clínicos | ACG (Johns Hopkins), CDPS, HCC (CMS), Charlson |
| Modelos sociales | Índice de vulnerabilidad territorial, Registro Social de Hogares |
| Pirámide de Kaiser | Nivel 1 (prevención), Nivel 2 (autogestión), Nivel 3 (gestión de caso), Nivel 4 (cuidados complejos) |
| Registros clínicos | Panel management, registros de crónicos por CESFAM |
| Segmentación operativa | Bajo riesgo (80 %), riesgo moderado (15 %), alto riesgo (5 %) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Población estratificada | Población con score de riesgo / Población adscrita × 100 | ≥80 % | UK NHS 100 % | NHS England 2023 | Anual |
| Concordancia modelo | C-statistic del modelo predictivo | ≥0.70 | ACG 0.75-0.80 | Johns Hopkins 2022 | Anual |
| Cobertura alto riesgo | Pacientes alto riesgo con plan activo / Total alto riesgo × 100 | ≥90 % | — | Panel management | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Sesgo del modelo por datos incompletos | Validación local, calibración anual |
| Estigmatización por etiqueta de riesgo | Comunicación centrada en necesidades, no en categorías |

Ref: Kaiser Permanente Risk Stratification; Johns Hopkins ACG System 2022; NHS England Population Health Management 2023; MINSAL MAIS 2013.

### 3.3 Cartera de servicios por nivel

Definición explícita de prestaciones ofertadas en cada nodo de la red según nivel de complejidad y normativa.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Cartera APS | MAIS, PSCV, control sano, salud mental comunitaria, urgencia rural |
| Cartera secundaria | 56 especialidades, CDT, procedimientos ambulatorios, hospital de día |
| Cartera terciaria | UCI, neurocirugía, cardiocirugía, trasplantes, neonatología |
| Cartera GES | 87 patologías con garantías de acceso, oportunidad, protección financiera |
| Brechas | Análisis oferta vs. demanda por prestación y territorio |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cobertura cartera normada | Prestaciones disponibles / Prestaciones normadas × 100 | ≥95 % | — | MINSAL 2023 | Anual |
| Brecha GES | Garantías incumplidas / Total garantías activadas × 100 | ≤2 % | — | FONASA-GES | Mensual |
| Resolución quirúrgica ambulatoria | CMA / Total cirugías elegibles × 100 | ≥60 % | OCDE 60-80 % | OCDE 2023 | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Cartera desalineada con perfil epidemiológico | Revisión bienal basada en carga de enfermedad local |
| Duplicación entre niveles | Protocolos de derivación con criterios explícitos |

Ref: DS 4/2013 (Reglamento GES); MINSAL Norma Cartera de Servicios 2018; OCDE Health at a Glance 2023.

### 3.4 Topología de la red (mapa SIG, tiempos, regionalización)

Representación geoespacial de la red con análisis de accesibilidad temporal y asignación territorial.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Mapa SIG | Georreferenciación de establecimientos, población, vías |
| Isócronas | Mapas de tiempo de viaje (30, 60, 120 min) a nodos críticos |
| Micro-redes | Agrupación funcional de establecimientos por territorio |
| Puntos ciegos | Zonas sin cobertura dentro de isócrona normada |
| Infraestructura crítica | Establecimientos con rol de respaldo ante contingencia |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Acceso ≤60 min a urgencia | Población a ≤60 min de SU / Población total × 100 | ≥95 % | UK 95 % (8 min ambulancia) | NHS 2023 | Anual |
| Puntos ciegos identificados | Zonas sin cobertura / Total zonas × 100 | ≤5 % | — | SIG Servicio de Salud | Anual |
| Actualización SIG | Fecha última actualización | ≤12 meses | — | Gestión interna | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Datos geográficos desactualizados | Convenio con IGM/INE, actualización anual |
| Accesibilidad teórica vs. real | Validación con tiempos reales (GPS flota SAMU) |

Ref: MINSAL Orientaciones Planificación de Red 2019; OPS Mapeo de Redes 2015; UK NHS Ambulance Response Programme 2023.

### 3.5 Roadmap y priorización

Hoja de ruta estratégica con priorización de iniciativas por valor, factibilidad y urgencia.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Matriz valor/esfuerzo | 4 cuadrantes: quick wins, proyectos estratégicos, relleno, evitar |
| Quick wins | Implementables en ≤90 días, alto impacto, bajo costo |
| Horizonte temporal | Corto (1 año), mediano (2-3 años), largo (5+ años) |
| Dependencias | Mapa de prerequisitos entre iniciativas |
| Gobernanza del roadmap | Revisión trimestral en consejo directivo |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Avance roadmap | Hitos completados / Hitos planificados × 100 | ≥80 % | — | PMO red | Trimestral |
| Quick wins ejecutados | QW completados ≤90 días / QW identificados × 100 | ≥70 % | — | PMO red | Trimestral |
| Inversión alineada | Presupuesto en iniciativas priorizadas / Presupuesto total × 100 | ≥75 % | — | Finanzas red | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Roadmap estático ante cambio de contexto | Revisión trimestral con ventana de ajuste |
| Priorización política sobre técnica | Criterios explícitos documentados y publicados |

Ref: Eisenhower Matrix; Lean Portfolio Management (SAFe 2023); NHS Long Term Plan 2019.

## 4. Integración clínica y continuidad

### 4.1 Rutas asistenciales integradas

Secuencias estandarizadas de actividades clínicas que articulan múltiples niveles y disciplinas para una condición específica.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Ruta E2E | Desde sospecha diagnóstica hasta seguimiento post-tratamiento |
| Bundles de cuidado | Paquetes de intervenciones basadas en evidencia (3-5 elementos) |
| Variabilidad clínica | Monitoreo de adherencia a ruta y análisis de desviaciones |
| Ownership | Líder clínico responsable por ruta (champion) |
| Revisión basada en evidencia | Actualización ≤3 años o ante nueva evidencia nivel I |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Adherencia a ruta | Pacientes con ≥80 % de hitos cumplidos / Total pacientes ruta × 100 | ≥75 % | — | HCE/auditoría | Trimestral |
| Bundle compliance | Pacientes con 100 % elementos del bundle / Total elegibles × 100 | ≥95 % | IHI ≥95 % | IHI 2019 | Mensual |
| Tiempo E2E | Mediana días desde ingreso a ruta hasta resolución | Según patología | — | Sistema trazabilidad | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Rutas desactualizadas | Trigger de revisión: nueva GPC, alerta AHRQ, >2 años |
| Baja adherencia por desconocimiento | Capacitación al ingreso, recordatorios en HCE |

Ref: NHS Map of Medicine; IHI Bundles 2019; NICE Pathways; MINSAL GPC por patología GES.

### 4.2 Coordinación APS–especialidad–hospital–comunidad

Mecanismos operativos de articulación entre niveles asistenciales y recursos comunitarios.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Consultorías | Especialista en APS (presencial/teleconsultoría), transferencia de conocimiento |
| Gestión de caso | Coordinador asignado para pacientes complejos (≥3 comorbilidades) |
| Reuniones clínicas integradas | Caso conjunto APS-especialista, frecuencia quincenal mínima |
| Recursos comunitarios | Mapeo y derivación a organizaciones locales (social prescribing) |
| Contrarreferencia activa | Informe estructurado + plan de seguimiento + próximo control |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Teleconsultorías realizadas | N° teleconsultorías / Total interconsultas elegibles × 100 | ≥30 % | — | MINSAL Telemedicina 2023 | Trimestral |
| Pacientes con gestor de caso | Pac. complejos con gestor / Total pac. complejos × 100 | ≥80 % | UK 100 % para alto riesgo | NHS 2023 | Trimestral |
| Reuniones integradas realizadas | Reuniones realizadas / Reuniones programadas × 100 | ≥90 % | — | Gestión interna | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Especialista no contrarreferencia | Indicador en COMGES, auditoría |
| Recursos comunitarios no mapeados | Directorio actualizado semestralmente |

Ref: MINSAL MAIS 2013; NHS Social Prescribing 2023; Wagner Chronic Care Model 2001; Starfield Primary Care 1998.

### 4.3 Gestión de transiciones (alta segura)

Proceso estructurado para garantizar continuidad y seguridad durante transferencias entre niveles o servicios.

**IF/THEN por tipo de alta:**

| Tipo alta | Condición | Acción |
|-----------|-----------|--------|
| Alta médica estándar | Paciente estable, red de apoyo presente | Epicrisis + recetas + control APS ≤72h + educación al paciente/cuidador |
| Alta desde SUH | Consulta urgencia sin hospitalización | Informe de atención urgencia → APS en 24h, teleconsulta seguimiento si alto riesgo |
| Hospitalización domiciliaria (HaD) | Criterios HaD cumplidos, cuidador capacitado | Equipo HaD asume, visita ≤24h, protocolo de re-hospitalización definido |
| Alta psiquiátrica | Estabilización aguda, plan ambulatorio listo | Contacto COSAM ≤48h, control psiquiatría ≤7 días, plan de crisis entregado |

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Checklist de alta segura | Medicación conciliada, educación, control agendado, alerta a APS |
| Conciliación medicamentosa | Revisión farmacéutica al ingreso, traslado y alta |
| Teach-back | Verificación comprensión del paciente sobre plan de alta |
| Handoff estandarizado | I-PASS o SBAR entre equipos |
| Seguimiento post-alta | Llamada ≤48h, control ≤7 días para alto riesgo |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Readmisión 30 días | Reingresos ≤30 días / Total egresos × 100 | ≤12 % | CMS 15.6 % (2023) | CMS 2023 | Mensual |
| Conciliación medicamentosa al alta | Altas con conciliación / Total altas × 100 | ≥95 % | ISMP 100 % | ISMP 2022 | Mensual |
| Llamada post-alta ≤48h | Llamadas realizadas ≤48h / Total altas elegibles × 100 | ≥80 % | — | Gestión interna | Mensual |
| Control APS ≤7 días post-alta | Controles realizados / Total altas × 100 | ≥70 % | — | Trazabilidad red | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Alta prematura por presión de camas | Criterios de alta explícitos, auditoría de reingresos precoces |
| Paciente no acude a control post-alta | Navegación activa, rescate telefónico |

Ref: Project RED (Boston University); IHI STAAR Initiative 2019; NICE NG27 Transition between inpatient and community 2015; MINSAL Norma Alta Segura 2019.

### 4.4 Coproducción del cuidado y navegación

Modelo de atención que integra al paciente como socio activo y provee apoyo para navegar la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Planes de cuidado compartidos | Objetivos definidos conjuntamente paciente-equipo |
| Navegadores de pacientes | Rol dedicado para acompañar trayectoria en la red |
| Herramientas de autogestión | Planes de acción, apps, material educativo validado |
| Grupos de pares | Programas de apoyo entre pacientes (diabetes, oncología) |
| Decisiones compartidas | Herramientas de ayuda a la decisión (option grids) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Pacientes con plan compartido | Pac. crónicos con plan / Total pac. crónicos × 100 | ≥60 % | UK NHS ≥50 % | NHS Personalised Care 2023 | Semestral |
| Activación del paciente (PAM) | Score PAM promedio | ≥60 | — | Insignia Health PAM | Anual |
| Navegación efectiva | Pac. navegados que completan ruta / Total navegados × 100 | ≥80 % | — | Programa navegación | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Carga adicional sobre paciente vulnerable | Adaptar nivel de coproducción a capacidad del paciente |
| Navegadores sin formación | Programa de capacitación estandarizado ≥40 horas |

Ref: NHS Personalised Care 2023; Hibbard PAM 2004; NICE Shared Decision Making 2021; Freeman Navigation Model 2012.

### 4.5 Comorbilidad y multimorbilidad

Gestión integrada de pacientes con ≥2 condiciones crónicas simultáneas, superando la lógica de enfermedad única.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Panel management | Registro activo de población a cargo con condiciones indexadas |
| PCI (Plan de Cuidados Integrado) | Plan unificado priorizando carga de tratamiento y preferencias |
| Polimedicación | Revisión farmacéutica estructurada (STOPP/START, Beers) |
| Complejidad clínica | Escalas INTERMED, Patient Complexity Tool |
| Coordinación multiprofesional | Ronda clínica semanal para pacientes de alta complejidad |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cobertura PCI | Pac. multimórbidos con PCI / Total pac. multimórbidos × 100 | ≥70 % | — | Panel management | Trimestral |
| Polifarmacia revisada | Pac. ≥5 fármacos con revisión ≤12 meses / Total polifarmacia × 100 | ≥80 % | UK QOF ≥80 % | NICE MO 2016 | Semestral |
| Hospitalizaciones evitables (ACSCs) | Egresos por ACSCs / Total egresos × 100 | ≤10 % | OCDE 5-8 % | OCDE 2023 | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Fragmentación por múltiples especialistas | Médico de cabecera como integrador, PCI único |
| Carga de tratamiento excesiva | Minimally Disruptive Medicine, priorización con paciente |

Ref: NICE NG56 Multimorbidity 2016; Muth 2014 (Multimorbidity guidelines); OCDE Health at a Glance 2023; May 2009 (Minimally Disruptive Medicine).

## 5. Gestión por procesos y mejora

### 5.1 Levantamiento y modelamiento

Técnicas para mapear, documentar y analizar procesos asistenciales y de soporte como base para rediseño.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| SIPOC | Suppliers, Inputs, Process, Outputs, Customers — vista macro |
| VSM (Value Stream Mapping) | Flujo de valor con tiempos de espera, ciclo y % valor agregado |
| BPMN 2.0 | Notación estándar para modelamiento detallado de procesos |
| Diagrama de carriles (swimlane) | Responsabilidades por rol/unidad en cada paso |
| Voz del cliente (VOC) | Requerimientos del paciente traducidos a CTQ (Critical to Quality) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Procesos críticos mapeados | Procesos con VSM / Total procesos críticos × 100 | ≥80 % | — | Gestión procesos | Anual |
| Ratio valor agregado | Tiempo valor agregado / Tiempo total proceso × 100 | ≥30 % | Lean benchmark 25-50 % | Lean Enterprise 2020 | Por proyecto |
| Actualización de mapas | Procesos actualizados ≤24 meses / Total mapeados × 100 | ≥90 % | — | Gestión documental | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Mapeo como ejercicio teórico sin acción | Vincular cada mapeo a proyecto de mejora con sponsor |
| Participación insuficiente del equipo clínico | Gemba walk obligatorio, mapeo in situ |

Ref: Lean Healthcare (Graban 2018); BPMN 2.0 (OMG); IHI Process Improvement 2019; NHS Improvement 2020.

### 5.2 Rediseño Lean/Six Sigma

Metodologías de mejora continua aplicadas a procesos asistenciales y administrativos.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Kaizen (mejora rápida) | Eventos de 3-5 días, equipo multidisciplinario, resultado inmediato |
| 5S | Clasificar, ordenar, limpiar, estandarizar, sostener — áreas clínicas |
| DMAIC | Define, Measure, Analyze, Improve, Control — proyectos Six Sigma |
| A3 Thinking | Formato una página: problema, análisis, contramedidas, plan |
| Gestión visual | Tableros Kanban, semáforos, señalética estandarizada |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Proyectos de mejora activos | N° proyectos en curso / Total áreas críticas | ≥1 por área | — | PMO mejora | Trimestral |
| Resultados sostenidos 6 meses | Proyectos con mejora sostenida a 6m / Total completados × 100 | ≥70 % | — | Auditoría mejora | Semestral |
| ROI proyectos mejora | (Beneficio − Costo proyecto) / Costo proyecto × 100 | ≥200 % | — | Finanzas | Por proyecto |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Herramienta sin cultura de mejora | Formación en pensamiento Lean para liderazgo |
| Mejoras puntuales sin sostenibilidad | Control chart post-proyecto, auditoría a 3, 6, 12 meses |

Ref: Lean Hospitals (Graban 2018); Six Sigma for Healthcare (Lighter 2019); IHI Model for Improvement; NHS QSIR Programme 2023.

### 5.3 Estándares y catálogos transversales

Repositorios centralizados de estándares, nomenclaturas y catálogos maestros que aseguran coherencia en la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Catálogo de prestaciones | FONASA MAI/MAE, codificación única |
| Nomenclaturas clínicas | SNOMED CT, CIE-10/CIE-11, LOINC, ATC |
| Estándares de proceso | SOPs transversales (triage, conciliación, consentimiento) |
| Catálogo de roles | Perfiles de cargo estandarizados por nivel |
| Catálogo de formularios | Formularios clínicos y administrativos normados |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Codificación correcta egresos | Egresos con CIE-10 validado / Total egresos × 100 | ≥95 % | — | GRD/DEIS | Mensual |
| Catálogos actualizados | Catálogos vigentes / Total catálogos × 100 | 100 % | — | Gestión documental | Semestral |
| Adherencia a nomenclatura | Registros con código estándar / Total registros × 100 | ≥90 % | — | HCE | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Proliferación de códigos locales | Gobernanza de terminología centralizada |
| Resistencia a codificación estandarizada | Integración en HCE con asistentes de codificación |

Ref: FONASA Catálogo MAI/MAE; OMS CIE-11 2022; SNOMED International 2023; MINSAL Normas de Codificación GRD 2020.

### 5.4 Gestión documental

Sistema estructurado para crear, aprobar, distribuir, revisar y retirar documentos normativos de la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Jerarquía documental | Política → Norma → SOP → WI (Work Instruction) → Checklist |
| Ciclo de vida | Borrador → Revisión → Aprobación → Vigente → Revisión periódica → Obsoleto |
| Control de versiones | Codificación única, historial de cambios, firma electrónica |
| Distribución controlada | Repositorio digital único, notificación automática de actualizaciones |
| Revisión periódica | Máximo 3 años para políticas, 2 años para SOPs |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Documentos vigentes | Documentos dentro de fecha revisión / Total documentos × 100 | ≥90 % | ISO 9001 100 % | ISO 9001:2015 | Trimestral |
| Accesibilidad | % personal que accede al repositorio en último mes | ≥70 % | — | Analytics repositorio | Mensual |
| Tiempo aprobación | Días promedio desde borrador hasta aprobación | ≤30 días | — | Gestión documental | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Documentos obsoletos en circulación | Marca de agua automática, retiro controlado |
| Exceso burocrático documental | Fast-track para actualizaciones menores |

Ref: ISO 9001:2015 §7.5 (Información documentada); Joint Commission Document Control Standards 2023; NHS Document Control Policy 2022.

### 5.5 Automatización

Aplicación de tecnologías de automatización a procesos administrativos y operativos repetitivos.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| RPA (Robotic Process Automation) | Bots para tareas repetitivas: agendamiento, digitación, conciliación datos |
| Orquestación de procesos | BPM engine para flujos multi-actor (derivaciones, autorizaciones) |
| Formularios inteligentes | Auto-completado, validaciones, ruteo condicional |
| Alertas automatizadas | Triggers por reglas: resultados críticos, vencimientos, quiebres stock |
| Integración API | Conexión entre sistemas (HCE, ERP, LIMS) sin intervención manual |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Horas liberadas por RPA | Horas manuales reemplazadas / mes | ≥100 h/mes | — | Monitoreo RPA | Mensual |
| Tasa de error post-automatización | Errores en proceso automatizado / Total transacciones × 100 | ≤1 % | — | QA procesos | Mensual |
| Procesos automatizados | Procesos con RPA o BPM / Total procesos elegibles × 100 | ≥30 % | — | PMO digital | Semestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Automatizar proceso deficiente | Rediseñar primero, automatizar después |
| Dependencia de proveedor único | Estándares abiertos, contratos con cláusula de portabilidad |

Ref: HIMSS RPA in Healthcare 2022; Gartner Hyperautomation 2023; NHS Digital Automation Programme 2023.

## 6. Acceso, demanda y listas de espera

### 6.1 Gestión de la demanda

Predicción y modulación de la demanda de servicios para dimensionar capacidad y reducir variabilidad.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Forecast estadístico | Series temporales (ARIMA, Prophet), horizontes 1-12 meses |
| Estacionalidad | Patrones por mes, día de semana, festivos, epidemias |
| Demanda inducida | Efecto de nuevos programas, campañas, cambios GES |
| Segmentación | Urgente vs. electiva, nueva vs. control, presencial vs. virtual |
| Demand smoothing | Distribución uniforme de electivas para reducir peaks |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Error de pronóstico (MAPE) | Σ|Real−Pronóstico| / Real × 100 / n | ≤15 % | — | Gestión demanda | Mensual |
| Variabilidad artificial | CV demanda electiva diaria | ≤0.20 | — | Agendamiento | Mensual |
| Ratio nueva/control | Consultas nuevas / Consultas control | Según especialidad | — | Gestión ambulatoria | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Pronóstico errado por evento imprevisto | Escenarios múltiples, actualización rolling |
| Demanda reprimida no visible | Encuestas de necesidad insatisfecha, datos Lista de Espera |

Ref: IHI Optimizing Patient Flow 2003; Litvak 2005 (variability methodology); NHS Demand & Capacity Guide 2022.

### 6.2 Criterios de derivación y backlogs

Protocolos explícitos de derivación y gestión de listas de espera acumuladas.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Criterios de derivación | Guías por especialidad con umbrales clínicos para referencia |
| Priorización clínica | Categorías P1 (urgente ≤7d), P2 (semi-urgente ≤30d), P3 (electivo) |
| Validación de interconsultas | Revisión por especialista antes de aceptación (pre-triage) |
| Limpieza de lista | Contacto activo, depuración de duplicados, pacientes fallecidos/resueltos |
| Backlog management | Plan de reducción: sobrecupo, extensión horaria, compra servicios |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Interconsultas rechazadas | IC devueltas / Total IC recibidas × 100 | ≤15 % | — | eReferral | Mensual |
| Lista de espera quirúrgica | N° pacientes en espera / Producción mensual | ≤3 meses de stock | UK NHS ≤18 sem | NHS 2023 | Mensual |
| Depuración lista | Registros depurados / Total lista × 100 | ≥10 %/año | — | Gestión LE | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Derivación inadecuada satura especialidad | Teleconsultoría previa, capacitación APS |
| Lista de espera oculta (intra-servicio) | Registro único centralizado |

Ref: MINSAL Orientaciones Gestión Lista de Espera 2023; NHS RTT Waiting Times 2023; NZ Elective Services 2022.

### 6.3 Centros de coordinación de acceso

Unidades centralizadas que gestionan la demanda entrante, triaje y asignación de recursos.

**IF/THEN para ruteo de triage:**

| Condición | Prioridad | Ruteo |
|-----------|-----------|-------|
| Sospecha patología GES | P1 | Ruta GES directa, confirmación ≤30 días |
| Criterio de derivación urgente | P1 | Agenda preferente especialidad ≤7 días |
| Derivación semi-urgente | P2 | Agenda especialidad ≤30 días |
| Derivación electiva estándar | P3 | Lista de espera con fecha estimada |
| Consulta resoluble por teleconsultoría | — | Retorno a APS con recomendación especialista |
| Información incompleta | — | Devolución a APS con checklist requerido |

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Contact center | Canal telefónico + digital para agendamiento y consultas |
| Centro regulador | Gestión de camas, traslados, interconsultas de urgencia |
| eReferral hub | Plataforma de derivación electrónica con triage centralizado |
| Callback system | Rellamada programada para reducir abandono |
| Dashboard de acceso | Tiempos de espera en tiempo real por especialidad |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tasa de abandono llamadas | Llamadas abandonadas / Total llamadas × 100 | ≤5 % | — | Contact center | Mensual |
| Tiempo respuesta eReferral | Días desde recepción hasta aceptación/rechazo | ≤3 días | UK ≤2 días | NHS 2023 | Mensual |
| Derivaciones GES en plazo | GES confirmadas en plazo / Total GES × 100 | ≥98 % | — | SIGGES | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Cuello de botella en centro regulador | Turnos 24/7, automatización de ruteo estándar |
| Triage inadecuado por personal no clínico | Protocolos validados, supervisión clínica |

Ref: MINSAL SIGGES; NHS e-Referral Service 2023; IHI Patient Flow 2019; Australasian Triage Scale.

### 6.4 Tiempos de oportunidad/garantía GES

Gestión de garantías legales de acceso y oportunidad del régimen GES/AUGE.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Garantía de acceso | Derecho a prestación dentro de la red |
| Garantía de oportunidad | Plazo máximo por patología/prestación (DS 4/2013) |
| SIGGES | Sistema de registro y monitoreo de garantías |
| Alerta GES | Notificación automática al 50 %, 75 % y 90 % del plazo |
| Recurso de protección | Consecuencia legal por incumplimiento |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cumplimiento oportunidad GES | Garantías cumplidas en plazo / Total garantías × 100 | ≥98 % | — | SIGGES-FONASA | Mensual |
| GES retrasadas activas | N° garantías vencidas sin resolver | 0 | — | SIGGES | Semanal |
| Tiempo promedio resolución | Días promedio desde activación hasta cierre GES | ≤70 % del plazo máximo | — | SIGGES | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Incumplimiento masivo por capacidad | Plan de contingencia: compra servicios, extensión horaria |
| Subregistro de activación GES | Auditoría cruzada con GRD y egresos |

Ref: Ley 19.966 (GES/AUGE); DS 4/2013; Superintendencia de Salud; FONASA Normas GES 2024.

### 6.5 Intervenciones de descongestión

Estrategias tácticas para reducir listas de espera y mejorar tiempos de acceso.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Extensión horaria | Turnos vespertinos y fines de semana para electivas |
| Sobrecupo programado | Agendas expandidas temporales con tope de seguridad |
| Compra de servicios | PPV a prestadores privados para especialidades críticas |
| Telemedicina | Teleconsultas para controles y seguimientos |
| Resolución en APS | Transferencia de competencias (ecografía, dermatoscopía, espirometría) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Reducción lista de espera | (LE mes anterior − LE mes actual) / LE mes anterior × 100 | ≥5 %/mes durante intervención | — | Gestión LE | Mensual |
| Producción adicional | Prestaciones extra / Producción base × 100 | ≥20 % durante campaña | — | Gestión producción | Mensual |
| Costo por caso adicional | Costo total intervención / Casos resueltos adicionales | ≤120 % costo estándar | — | Finanzas | Por campaña |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Burnout por sobrecarga sostenida | Intervenciones acotadas (≤3 meses), voluntariedad |
| Efecto rebote post-intervención | Abordar causa raíz simultáneamente |

Ref: MINSAL Plan Nacional de Reducción LE 2023; NHS Elective Recovery Programme 2023; IHI Reducing Waiting Times 2004.

## 7. Capacidad, recursos y programación

### 7.1 Infraestructura y flujos físicos

Diseño y gestión del espacio físico para optimizar flujos de pacientes, personal e insumos.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Zonificación | Áreas limpias/sucias, flujos unidireccionales, segregación pacientes infecciosos |
| Señalética | Wayfinding estandarizado, código de colores por área |
| Capacidad física | m² por cama (10 m² norma), distancia entre camillas, ventilación |
| Seguridad estructural | Normativa sísmica NCh433, evacuación, sistemas contra incendio |
| Facility management | Mantención preventiva infraestructura, HVAC, gases clínicos |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Mantención preventiva cumplida | MP realizadas / MP programadas × 100 | ≥90 % | Joint Commission ≥95 % | JCI 2023 | Mensual |
| Incidentes infraestructura | N° fallas críticas (electricidad, agua, gases) / mes | 0 | — | Facility management | Mensual |
| Cumplimiento normativa | Items conformes / Total items auditoría SEREMI × 100 | ≥95 % | — | SEREMI Salud | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Infraestructura obsoleta | Plan maestro de inversiones con priorización por riesgo |
| Flujos cruzados contaminación | Auditoría de flujos trimestral, rediseño si necesario |

Ref: MINSAL Norma Técnica Básica de Establecimientos 2017; ASHRAE 170 (ventilación); FGI Guidelines for Design and Construction of Hospitals 2022; NCh433 (sísmica).

### 7.2 Camas, pabellones, box y agendas

Dimensionamiento y gestión de la capacidad instalada para maximizar productividad y acceso.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Gestión de camas | Ocupación óptima 85 %, census tracking, discharge planning |
| Pabellones | Utilización quirúrgica (first case on time, turnover, cancellation rate) |
| Box de atención | Productividad ambulatoria (consultas/box/día) |
| Agendas | Configuración por tipo (nuevas/controles), overbooking calculado |
| Productividad | Benchmarks por especialidad (egresos/cama, CMA/pabellón) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Ocupación de camas | Días-cama ocupados / Días-cama disponibles × 100 | 85 % (±5 %) | OCDE 75 % | OCDE 2023 | Diaria |
| Utilización pabellón | Minutos cirugía / Minutos disponibles × 100 | ≥80 % | — | Gestión quirúrgica | Mensual |
| Suspensión quirúrgica | Cirugías suspendidas / Total programadas × 100 | ≤5 % | — | Gestión quirúrgica | Mensual |
| Productividad ambulatoria | Consultas realizadas / Horas médicas contratadas | ≥4/hora | — | Gestión ambulatoria | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Ocupación >90 % genera boarding y riesgo | Gatillo de contingencia a 90 %, plan de desborde |
| Suspensiones por falta de insumos | Checklist pre-quirúrgico estandarizado |

Ref: IHI Optimizing Patient Flow 2003; OCDE Health at a Glance 2023; Association for Perioperative Practice 2023; MINSAL Norma Gestión del Bloque Quirúrgico 2018.

### 7.3 Teoría de colas y simulación

Modelos matemáticos para dimensionar recursos y predecir congestión en la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| M/M/s | Modelo Erlang-C: tasa de llegada (λ), servicio (μ), servidores (s) |
| Simulación de eventos discretos | Arena, SimPy, AnyLogic para escenarios complejos |
| Ley de Little | L = λ × W (pacientes en sistema = tasa × tiempo estancia) |
| Ley de Kingman | Tiempo espera ∝ (utilización / (1−utilización)) × variabilidad |
| What-if analysis | Escenarios de capacidad ante cambios de demanda |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Utilización del recurso crítico | λ / (s × μ) | ≤85 % | Erlang-C target | Análisis de colas | Mensual |
| Probabilidad de espera (Pw) | P(espera > 0) calculada por Erlang-C | ≤20 % | — | Modelo de colas | Trimestral |
| Validación del modelo | Error predicción vs. real | ≤10 % | — | Simulación | Semestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Modelo demasiado simplificado | Validar con datos reales, iterar complejidad |
| Sobre-inversión basada en peor escenario | Usar percentil 95, no máximo absoluto |

Ref: Erlang-C (Gross & Harris 2008); Little's Law; Kingman's Formula; Litvak 2005 (healthcare queuing); NHS Capacity Planning Tools 2023.

### 7.4 Programación maestra

Planificación integrada de recursos para equilibrar carga y minimizar variabilidad artificial.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Master Surgical Schedule | Asignación semanal fija de pabellones por especialidad |
| Block scheduling | Bloques protegidos para urgencias, electivas, ambulatorias |
| Smoothing | Distribución uniforme de admisiones electivas entre días |
| Overbooking calculado | Tasa de no-show por especialidad → sobrecupo ajustado |
| Reconciliación semanal | Ajuste fino según censo, urgencias y contingencias |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Adherencia al master schedule | Sesiones realizadas según plan / Total sesiones plan × 100 | ≥85 % | — | Gestión quirúrgica | Semanal |
| No-show rate | Pacientes que no asisten / Total citados × 100 | ≤10 % | — | Agendamiento | Mensual |
| Variabilidad admisiones electivas | CV admisiones electivas diarias | ≤0.15 | Litvak target ≤0.10 | Litvak 2005 | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Urgencias desplazan electivas crónicamente | Bloques protegidos con política de invasión explícita |
| No-show alto por barreras de acceso | Recordatorios multicanal (SMS, llamada), lista de espera activa |

Ref: Litvak 2005 (surgical smoothing); IHI Patient Flow 2019; AORN Perioperative Standards 2023.

### 7.5 Equipamiento biomédico

Gestión del ciclo de vida de equipos médicos: adquisición, mantención, calibración y baja.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Inventario | Registro completo con código, ubicación, vida útil, riesgo |
| Mantención preventiva (PM) | Programa según fabricante y criticidad (Clase I/II/III) |
| Calibración | Verificación periódica de parámetros de medición |
| Obsolescencia | Evaluación vida útil, costo mantención vs. reposición |
| Tecnovigilancia | Reporte de incidentes ISP, alertas fabricante, recalls |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| PM cumplida | PM realizadas / PM programadas × 100 | ≥95 % | ECRI ≥90 % | ECRI 2023 | Mensual |
| Disponibilidad equipos críticos | Horas operativas / Horas programadas × 100 | ≥98 % | — | Ingeniería biomédica | Mensual |
| Equipos fuera de vida útil | Equipos >vida útil / Total inventario × 100 | ≤10 % | — | Inventario | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Falla equipo crítico sin respaldo | Plan de contingencia, equipos de respaldo para críticos |
| Mantención por personal no calificado | Contratos de servicio con fabricante, certificación técnicos |

Ref: ECRI Institute 2023; ISP Tecnovigilancia Chile; IEC 62353 (pruebas equipos médicos); MINSAL Norma Técnica Equipamiento 2016.

## 8. Operación y coordinación en tiempo real

### 8.1 Centro de comando (NOC)

Unidad centralizada de monitoreo y coordinación operacional en tiempo real de la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| War room / NOC | Espacio físico con pantallas, datos RT, equipo dedicado |
| Tableros en tiempo real | Census, ocupación, tiempos espera, alertas, flujo urgencia |
| Reglas de activación | Umbrales predefinidos que gatillan acciones (semáforo) |
| Huddles operacionales | Reuniones breves (≤15 min) a las 09:00 y 14:00 |
| Escalamiento RT | Protocolo quién-contacta-a-quién según nivel de alerta |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tiempo detección-respuesta | Minutos desde alerta hasta acción correctiva | ≤30 min | — | NOC log | Diaria |
| Huddles realizados | Huddles ejecutados / Huddles programados × 100 | ≥95 % | — | NOC log | Semanal |
| Alertas resueltas mismo turno | Alertas cerradas en turno / Total alertas × 100 | ≥80 % | — | NOC log | Diaria |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Fatiga de alertas (alarm fatigue) | Priorización, reducir alertas no accionables a <10 % |
| NOC sin autoridad para actuar | Mandato formal del consejo directivo |

Ref: GE Healthcare Command Centers 2020; IHI Real-Time Demand Capacity Management 2019; NHS Command Centre Model 2022.

### 8.2 Gestión de camas y traslados

Coordinación en tiempo real de asignación de camas, egresos y transferencias entre establecimientos.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Bed board digital | Visualización RT: ocupación, pendientes de alta, limpieza, bloqueos |
| Discharge planning | Predicción de alta (ML o reglas), planificación desde ingreso |
| Limpieza y habilitación | Workflow limpieza → inspección → habilitación, target ≤60 min |
| Traslados inter-establecimientos | Protocolo de solicitud, aceptación, transporte, handoff |
| Código de desborde | Activación cuando ocupación >95 %, plan de contingencia |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tiempo cama vacía a ocupada | Minutos desde egreso hasta ingreso siguiente | ≤120 min | Best practice ≤90 min | IHI 2019 | Diaria |
| Egresos antes mediodía | Altas antes 12:00 / Total altas × 100 | ≥40 % | — | Bed board | Diaria |
| Boarding time urgencia | Horas desde decisión hospitalizar hasta cama asignada | ≤2 h | — | SU-NOC | Diaria |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Boarding prolongado en urgencia | Meta de alta matutina, ronda de alta temprana |
| Traslado sin cama confirmada | Regla: no traslado sin aceptación + cama asignada |

Ref: IHI Patient Flow 2019; ACEP Boarding Position Statement 2022; NHS Discharge Planning Guidance 2023.

### 8.3 Reglas de control de flujo

Mecanismos tipo pull/push y límites de trabajo en proceso para regular el flujo de pacientes.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Sistema pull | Cama disponible "jala" al siguiente paciente (no push desde urgencia) |
| WIP limits | Máximo de pacientes simultáneos por área/profesional |
| FIFO con prioridad | Orden de llegada modulado por urgencia clínica |
| Señales Kanban | Visual: verde (<80 % capacidad), amarillo (80-90 %), rojo (>90 %) |
| Balanceo de carga | Distribución equitativa entre servicios/pisos disponibles |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| WIP promedio por servicio | Pacientes promedio en servicio / Capacidad × 100 | ≤85 % | — | Census RT | Diaria |
| Tiempo en cola interno | Minutos espera entre etapas del flujo | ≤30 min | — | Trazabilidad | Diaria |
| Violaciones WIP limit | Eventos sobre WIP limit / Total turnos × 100 | ≤5 % | — | NOC log | Semanal |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Cultura de push ("no tengo camas pero envío") | Entrenamiento, regla formal de no-push |
| WIP limits rígidos bloquean urgencias | Override protocolizado con escalamiento |

Ref: Lean Healthcare Flow (Graban 2018); Theory of Constraints (Goldratt); IHI Patient Flow 2019.

### 8.4 Alertas operacionales y contingencia

Sistema escalonado de alertas que activa respuestas progresivas ante saturación o eventos adversos.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Nivel verde | Operación normal, indicadores dentro de rango |
| Nivel amarillo | Pre-saturación: ocupación 85-95 %, LE creciente, suspensión electivas parcial |
| Nivel rojo | Saturación: ocupación >95 %, activación plan desborde, desvío ambulancias |
| Nivel negro | Catástrofe: activación HICS, plan de emergencia |
| Comunicación | Notificación automática por nivel a lista de distribución definida |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tiempo en nivel rojo | Horas en nivel rojo / Horas totales × 100 | ≤5 % | — | NOC log | Mensual |
| Activaciones contingencia | N° activaciones plan desborde / mes | Monitorear tendencia | — | NOC log | Mensual |
| Adherencia al protocolo | Acciones ejecutadas según protocolo / Acciones requeridas × 100 | ≥90 % | — | Post-activación review | Por evento |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Demora en escalamiento | Activación automática por regla, no por juicio individual |
| Nivel rojo prolongado normalizado | Análisis de causa raíz obligatorio post >24h en rojo |

Ref: NHS OPEL Framework 2023; ACEP Emergency Department Crowding 2022; IHI Surge Management 2020.

### 8.5 Cuadros de mando y huddles

Reuniones estructuradas con tableros visuales para coordinación operativa por niveles organizacionales.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Tier 1 — Huddle de unidad | Diario, 10 min, equipo de turno, problemas inmediatos |
| Tier 2 — Huddle de servicio | Diario, 15 min, jefaturas, flujo y recursos |
| Tier 3 — Huddle de dirección | Semanal, 30 min, equipo directivo, táctico |
| Tier 4 — Comité estratégico | Mensual, 60 min, indicadores macro, decisiones estratégicas |
| Visual management | Tableros físicos + digitales con métricas actualizadas |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Adherencia a huddles | Huddles realizados / Huddles programados × 100 | ≥95 % | — | Registro huddles | Semanal |
| Problemas escalados y resueltos | Problemas resueltos ≤24h / Total escalados × 100 | ≥80 % | — | Registro huddles | Semanal |
| Participación promedio | Asistentes / Esperados × 100 | ≥80 % | — | Registro huddles | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Huddles como ritual vacío | Formato estandarizado, foco en acción y escalamiento |
| Exceso de reuniones sin valor | Auditoría trimestral de utilidad percibida |

Ref: Lean Daily Management (Mann 2015); IHI Huddles 2019; NHS Improvement Tiered Huddle System 2022.

## 9. Personas, liderazgo y cultura

### 9.1 Roles, perfiles y dotación

Definición de estructura de cargos, competencias requeridas y cálculo de dotación para la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Perfiles de cargo | Descripción estandarizada: requisitos, competencias, dependencia |
| Dotación normada | Cálculo según normas técnicas MINSAL (enfermería, médica, etc.) |
| Brecha de RRHH | Dotación requerida vs. disponible por estamento |
| Competencias transversales | Trabajo en equipo, comunicación, gestión del cambio |
| Reclutamiento y retención | Estrategias para zonas de difícil provisión (ruralidad, especialidades críticas) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Brecha de dotación | (Dotación requerida − Dotación actual) / Dotación requerida × 100 | ≤10 % | — | RRHH red | Semestral |
| Rotación voluntaria | Renuncias voluntarias / Dotación promedio × 100 | ≤12 % | OCDE salud 15 % | OCDE 2023 | Anual |
| Vacantes >90 días | N° vacantes abiertas >90 días / Total vacantes × 100 | ≤15 % | — | RRHH red | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Déficit crónico de especialistas | Formación local, telemedicina, incentivos zona |
| Perfiles desactualizados | Revisión bienal con participación de jefaturas |

Ref: MINSAL Normas de Dotación 2019; OMS Global Strategy on Human Resources for Health 2030; Ley 18.834 (Estatuto Administrativo); Ley 19.664 (Médicos).

### 9.2 Liderazgo clínico-organizacional

Modelo de liderazgo que integra perspectiva clínica y de gestión en todos los niveles de la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Triadas de gestión | Médico + enfermera + gestor por servicio/unidad |
| Gemba walk | Ronda directiva semanal en terreno (observar, preguntar, no juzgar) |
| Liderazgo distribuido | Empoderar líderes de equipo en cada nivel |
| Coaching y mentoring | Programa formal para nuevas jefaturas (≥6 meses) |
| Accountability | Objetivos individuales vinculados a indicadores de servicio |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Gemba walks realizados | Walks ejecutados / Programados × 100 | ≥90 % | — | Dirección | Mensual |
| Satisfacción con liderazgo | Score encuesta clima (dimensión liderazgo) | ≥70 % | — | Encuesta clima | Anual |
| Jefaturas con coaching | Jefaturas en programa / Total jefaturas nuevas × 100 | 100 % | — | RRHH | Semestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Liderazgo clínico sin formación en gestión | Diploma obligatorio en gestión para jefaturas clínicas |
| Gemba walk como supervisión punitiva | Protocolo de gemba: observación apreciativa, no auditoría |

Ref: IHI Leadership Alliance 2020; NHS Leadership Academy 2023; Lean Management (Mann 2015); Toyota Kata (Rother 2009).

### 9.3 Bienestar y burnout

Estrategias para prevenir, detectar y abordar el desgaste profesional en equipos de salud.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Medición sistemática | MBI (Maslach Burnout Inventory) o ProQOL anual |
| Factores organizacionales | Carga laboral, autonomía, equidad, comunidad (Maslach 6 áreas) |
| Programa de apoyo | Psicólogo organizacional, peer support, línea confidencial |
| Intervenciones estructurales | Redistribución carga, flexibilidad horaria, pausas protegidas |
| Post-incidente | Defusing y debriefing tras eventos críticos |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Prevalencia burnout | % personal con MBI alto en agotamiento emocional | ≤25 % | EE.UU. 44 % (2022) | Shanafelt 2022 | Anual |
| Licencias médicas por SM | Días licencia SM / Total días licencia × 100 | Monitorear tendencia | — | RRHH | Trimestral |
| Uso programa de apoyo | Consultas programa apoyo / Dotación × 100 | ≥10 % (indicador de acceso, no de morbilidad) | — | Programa apoyo | Semestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Estigma impide búsqueda de ayuda | Canal confidencial, cultura de seguridad psicológica |
| Medición sin acción | Plan de mejora obligatorio post-encuesta |

Ref: Maslach & Leiter 2016; Shanafelt et al. 2022; NAM Clinician Well-Being 2019; IHI Joy in Work Framework 2017.

### 9.4 Formación y simulación

Sistema de educación continua, entrenamiento y simulación clínica para mantener competencias.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Plan de capacitación anual | Basado en brechas de competencia y prioridades de la red |
| Simulación clínica | Escenarios de alta fidelidad: emergencia, quirúrgica, trabajo en equipo |
| E-learning | Plataforma LMS con cursos obligatorios y electivos |
| Recertificación | Programa de actualización por especialidad (CONACEM, EUNACOM) |
| Inducción | Programa estandarizado para nuevos ingresos (≥40 horas) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Horas capacitación per cápita | Total horas capacitación / Dotación | ≥40 h/año | — | RRHH | Anual |
| Simulacros realizados | Simulacros ejecutados / Programados × 100 | ≥90 % | — | Centro simulación | Semestral |
| Inducción completada | Nuevos ingresos con inducción completa / Total nuevos × 100 | 100 % | — | RRHH | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Capacitación no alineada con necesidades | Detección de necesidades anual con jefaturas y análisis de EA |
| Personal no liberado para capacitación | Horas protegidas en programación de turnos |

Ref: MINSAL Norma de Capacitación; CONACEM Recertificación; SSH (Society for Simulation in Healthcare) 2023; WHO Patient Safety Curriculum 2011.

### 9.5 Desempeño y reconocimiento

Evaluación del desempeño individual y colectivo con sistemas de incentivos alineados a metas de red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Evaluación de desempeño | Ciclo anual: objetivos → seguimiento → evaluación → retroalimentación |
| OKR/BSC individual | Objetivos alineados a BSC de servicio y red |
| Asignación desempeño colectivo | Ley 19.813: metas institucionales, componente variable |
| Reconocimiento no monetario | Programa de reconocimiento entre pares, ceremonia trimestral |
| Plan de desarrollo | Acuerdos de desarrollo individual post-evaluación |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Evaluaciones completadas | Evaluaciones realizadas / Dotación evaluable × 100 | ≥95 % | — | RRHH | Anual |
| Cumplimiento OKR | OKR logrados / OKR comprometidos × 100 | ≥70 % | — | Gestión desempeño | Trimestral |
| Satisfacción con retroalimentación | Score encuesta (dimensión feedback) | ≥65 % | — | Encuesta clima | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Evaluación como trámite burocrático | Formación en feedback, calibración entre evaluadores |
| Incentivos generan competencia disfuncional | Componente colectivo ≥60 % del incentivo variable |

Ref: Ley 19.813 (Asignación Desempeño); MINSAL Orientaciones Evaluación del Desempeño; Kaplan & Norton BSC 1996; Doerr OKR 2018.

## 10. Calidad, seguridad y gestión de riesgos

### 10.1 Sistema de calidad

Marco integrado para planificar, asegurar, controlar y mejorar la calidad en toda la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| PDSA/PDCA | Ciclo de mejora: Plan → Do → Study → Act, iteraciones rápidas |
| Auditoría clínica | Revisión sistemática contra estándar, con plan de mejora |
| Acreditación | Estándar nacional (Ley 19.937) + internacional (JCI/ACHS) |
| Comité de calidad | Multidisciplinario, sesión mensual, reporte a dirección |
| Cultura de calidad | Reporte no punitivo, aprendizaje organizacional, transparencia |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Proyectos PDSA activos | N° ciclos PDSA en curso / Total unidades | ≥1 por unidad | — | Comité calidad | Trimestral |
| Estándares de acreditación cumplidos | Items conformes / Total items estándar × 100 | ≥90 % | JCI ≥85 % | JCI 2023 | Anual |
| Auditorías completadas | Auditorías realizadas / Programadas × 100 | ≥90 % | — | Comité calidad | Semestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Calidad como departamento aislado | Integrar indicadores de calidad en gestión de línea |
| Acreditación como fin, no como medio | Mejora continua post-acreditación, no solo preparación |

Ref: Ley 19.937 (Acreditación); SIC (Superintendencia Salud) Estándares Acreditación 2023; IHI Model for Improvement; JCI Standards 7th Edition 2023.

### 10.2 Seguridad del medicamento e IPC

Prácticas basadas en evidencia para uso seguro de medicamentos y prevención/control de infecciones.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| 5 correctos + | Paciente, medicamento, dosis, vía, hora + documentación |
| Medicamentos de alto riesgo | Lista ISMP, doble chequeo, almacenamiento segregado |
| Conciliación medicamentosa | Ingreso, traslado, alta — farmacéutico clínico |
| Bundles IPC | Higiene manos (5 momentos OMS), CVC, CUP, NAV/NIH, sitio quirúrgico |
| Antimicrobial stewardship | PROA: restricción, auditoría prospectiva, desescalamiento |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Adherencia higiene manos | Oportunidades cumplidas / Total oportunidades observadas × 100 | ≥80 % | OMS ≥80 % | OMS 2023 | Mensual |
| Tasa IAAS (ITS-CVC) | Infecciones CVC / 1.000 días-CVC | ≤1.0 | NHSN 0.8 (2022) | CDC NHSN 2022 | Mensual |
| Errores de medicación graves | Eventos centinela medicación / 10.000 prescripciones | ≤0.5 | — | Farmacovigilancia | Mensual |
| Consumo antibióticos (DDD) | DDD / 1.000 días-cama | Reducción ≥5 %/año | — | PROA | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Subregistro de errores de medicación | Sistema de reporte anónimo, cultura justa |
| Resistencia antimicrobiana creciente | PROA activo, vigilancia MO resistentes, aislamiento |

Ref: OMS 5 Momentos Higiene de Manos; ISMP High-Alert Medications 2023; CDC NHSN 2022; MINSAL PROA 2019; IHI Medication Safety 2019.

### 10.3 Eventos adversos y análisis

Sistema de detección, reporte, análisis y aprendizaje a partir de eventos adversos e incidentes.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Sistema de reporte | Voluntario + obligatorio (eventos centinela), confidencial, no punitivo |
| Clasificación | ICPS (OMS): near miss, incidente sin daño, EA leve/moderado/grave/centinela |
| IFA (Investigación Falla Asistencial) | Análisis profundo de eventos graves |
| RCA (Root Cause Analysis) | Diagrama Ishikawa, 5 Why, árbol de causas |
| HFMEA | Healthcare Failure Mode and Effect Analysis — prospectivo |
| Acciones correctivas | Plan con responsable, plazo, verificación de efectividad |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tasa de reporte | Reportes / 1.000 egresos | ≥40 | UK NHS ≥50 | NHS Patient Safety 2023 | Mensual |
| RCA completados en plazo | RCA finalizados ≤45 días / Total RCA requeridos × 100 | ≥90 % | Joint Commission 100 % | JCI 2023 | Trimestral |
| Acciones correctivas implementadas | AC implementadas / AC definidas × 100 | ≥85 % | — | Comité calidad | Trimestral |
| Eventos centinela | N° eventos centinela / año | 0 (aspiracional) | — | Reporte EA | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Cultura punitiva inhibe reporte | Política de cultura justa documentada y comunicada |
| Análisis sin acción | Seguimiento formal de AC con cierre verificado |

Ref: OMS ICPS 2009; Joint Commission Sentinel Event Policy 2023; NHS Patient Safety Strategy 2019; AHRQ Patient Safety Primers; MINSAL Norma EA 2017.

### 10.4 Experiencia y PROMs/PREMs

Medición sistemática de la experiencia reportada por pacientes y resultados percibidos.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| PREMs | Patient-Reported Experience Measures: trato, comunicación, tiempos, ambiente |
| PROMs | Patient-Reported Outcome Measures: funcionalidad, dolor, calidad de vida |
| Journey mapping | Mapeo de experiencia por punto de contacto (touchpoint) |
| Co-diseño | Mejoras diseñadas con pacientes (Experience-Based Co-Design) |
| Gestión de reclamos | OIRS + feedback digital, análisis temático, cierre de brechas |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tasa respuesta PREMs | Encuestas respondidas / Egresos elegibles × 100 | ≥30 % | UK NHS ≥25 % | NHS 2023 | Trimestral |
| Score PREMs global | Promedio ponderado dimensiones | ≥80 % | NHS 75 % | NHS Patient Survey 2023 | Trimestral |
| PROMs recolectados | Pacientes con PROMs pre+post / Total elegibles × 100 | ≥50 % | — | HCE | Semestral |
| Reclamos respondidos en plazo | Respuestas ≤15 días / Total reclamos × 100 | ≥90 % | — | OIRS | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Baja tasa de respuesta sesga resultados | Multicanal (digital, presencial, telefónico), incentivos |
| PROMs no integrados a decisiones clínicas | Visualización en HCE, discusión en ronda clínica |

Ref: NHS PROMs Programme 2023; ICHOM Standard Sets; OECD PaRIS Survey 2023; Point of Care Foundation EBCD 2022.

### 10.5 Cumplimiento y auditorías

Verificación sistemática de adherencia a normas, protocolos y regulaciones aplicables.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Auditoría programada | Calendario anual, alcance definido, equipos auditores internos |
| Auditoría sorpresa | Sin aviso previo, foco en prácticas de rutina (higiene, identificación) |
| Checklist de cumplimiento | Items verificables por área (farmacia, esterilización, urgencia) |
| Plan de acción correctiva | Hallazgo → causa raíz → acción → responsable → plazo → verificación |
| Auditoría externa | SEREMI, Superintendencia, acreditadores |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Auditorías ejecutadas | Realizadas / Programadas × 100 | ≥95 % | — | Calidad | Semestral |
| No conformidades críticas | NC críticas abiertas | 0 | — | Auditoría | Continuo |
| Cierre NC en plazo | NC cerradas en plazo / Total NC × 100 | ≥90 % | — | Calidad | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Auditoría como inspección punitiva | Enfoque formativo, participación del auditado |
| Hallazgos recurrentes sin solución | Escalamiento a dirección tras segunda recurrencia |

Ref: ISO 19011:2018 (Auditoría de sistemas de gestión); SIC Estándares Acreditación 2023; MINSAL Fiscalización SEREMI.

### 10.6 Análisis de riesgos y BIA

Identificación, evaluación y priorización de riesgos operacionales y su impacto en la continuidad.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Registro de riesgos | Inventario con probabilidad, impacto, score, owner, mitigación |
| Matriz de riesgos | 5×5 (probabilidad × impacto), clasificación por cuadrante |
| BIA (Business Impact Analysis) | Procesos críticos, RTO, RPO, dependencias, recursos mínimos |
| Apetito de riesgo | Declaración formal del consejo directivo |
| Monitoreo continuo | Dashboard de riesgos top-10, revisión trimestral |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Riesgos evaluados | Riesgos con score actualizado / Total riesgos registrados × 100 | 100 % | — | Registro riesgos | Trimestral |
| BIA actualizado | Procesos con BIA ≤12 meses / Total procesos críticos × 100 | 100 % | ISO 22301 | ISO 22301:2019 | Anual |
| Mitigaciones implementadas | Controles implementados / Controles planificados × 100 | ≥85 % | — | Registro riesgos | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Registro estático sin actualización | Trigger de revisión: incidente, cambio organizacional, auditoría |
| BIA teórico sin validación | Ejercicio tabletop anual por proceso crítico |

Ref: ISO 31000:2018 (Gestión de riesgos); ISO 22301:2019 (Continuidad de negocio); ASIS Business Impact Analysis 2019; NHS Risk Management Standards 2023.

### 10.7 Plan de Continuidad (BCP/COOP) y DRP TI

Planes para mantener servicios esenciales durante interrupciones y recuperar sistemas de información.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| BCP/COOP | Plan de continuidad operacional: servicios esenciales, dotación mínima, suministros |
| DRP TI | Disaster Recovery Plan: backup, replicación, sitio alterno, RTO/RPO |
| Servicios esenciales | Urgencia, UCI, pabellón urgencia, farmacia, laboratorio, imagenología |
| Cadena de mando | Sucesión de autoridad ante ausencia de directivos |
| Comunicación de crisis | Protocolo: portavoz único, canales, mensajes clave, frecuencia |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| BCP actualizado | Planes vigentes / Total planes requeridos × 100 | 100 % | ISO 22301 | ISO 22301:2019 | Anual |
| RTO cumplido en ejercicio | Servicios recuperados dentro de RTO / Total servicios × 100 | ≥90 % | — | Ejercicio DRP | Anual |
| Backup verificado | Backups restaurados exitosamente / Total backups × 100 | 100 % | — | TI | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Plan no probado | Ejercicio anual obligatorio (tabletop + funcional) |
| DRP sin sitio alterno | Contrato con proveedor cloud/colocation |

Ref: ISO 22301:2019; NIST SP 800-34 (Contingency Planning); MINSAL Plan de Emergencia Hospitalario; HIMSS DRP Guidelines 2022.

### 10.8 Sistema de Comando de Incidentes (HICS/ICS)

Estructura organizacional estandarizada para gestión de emergencias y desastres en establecimientos de salud.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Comando del incidente | Jefe de incidente (IC), oficial de seguridad, enlace, información pública |
| Sección operaciones | Atención médica, triage, tratamiento, evacuación |
| Sección planificación | Situación, recursos, documentación, desmobilización |
| Sección logística | Suministros, comunicaciones, alimentación, transporte |
| Sección finanzas/admin | Costos, contratos, compensación, registro de tiempo |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Personal capacitado HICS | Personal con curso HICS / Personal clave × 100 | ≥80 % | — | Emergencia | Anual |
| Tiempo activación HICS | Minutos desde declaración hasta equipo operativo | ≤15 min | — | Ejercicios | Por ejercicio |
| Ejercicios HICS realizados | Ejercicios ejecutados / Programados × 100 | ≥90 % | — | Plan emergencia | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Estructura paralela desconocida por personal | Capacitación recurrente, señalética, chalecos de rol |
| HICS activado tardíamente | Criterios de activación explícitos, autoridad delegada |

Ref: HICS (Hospital Incident Command System) 2014; FEMA NIMS 2017; MINSAL Plan Nacional de Emergencias en Salud 2018.

### 10.9 Desastres, CBRNE y eventos masivos

Preparación y respuesta ante desastres naturales, agentes CBRNE y eventos con víctimas masivas.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Amenazas naturales | Terremoto, tsunami, erupción volcánica, aluvión, incendio forestal |
| CBRNE | Químico, Biológico, Radiológico, Nuclear, Explosivo |
| MCI (Mass Casualty Incident) | Evento con víctimas que superan capacidad instalada |
| Triage de desastre | START/JumpSTART, etiquetas de color (rojo/amarillo/verde/negro) |
| Surge capacity | Expansión de capacidad: espacios, personal, insumos, equipos |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Capacidad de surge | Camas expandibles / Camas base × 100 | ≥20 % | — | Plan emergencia | Anual |
| Kit CBRNE disponible | Kits completos / Kits requeridos × 100 | 100 % | — | Emergencia | Semestral |
| Personal capacitado triage desastre | Personal urgencia con curso / Total personal urgencia × 100 | ≥90 % | — | Emergencia | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Stock de emergencia vencido | Rotación FIFO, inventario trimestral |
| Comunicaciones caídas | Redundancia: radio, satélite, mensajería offline |

Ref: ONEMI/SENAPRED Chile; OPS/OMS Hospital Seguro; FEMA NIMS 2017; START Triage System; MINSAL Plan CBRNE 2019.

### 10.10 Ejercicios y simulacros

Programa estructurado de ejercicios para validar planes y mantener preparación operativa.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Tabletop | Ejercicio teórico de discusión, bajo costo, alta participación |
| Funcional | Activación parcial de plan, prueba de comunicaciones y logística |
| Full-scale | Simulacro completo con víctimas simuladas, multiagencia |
| After Action Review (AAR) | Análisis post-ejercicio: qué funcionó, brechas, acciones correctivas |
| Calendario de ejercicios | Mínimo: 1 tabletop trimestral, 1 funcional semestral, 1 full-scale anual |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Ejercicios ejecutados | Ejercicios realizados / Programados × 100 | ≥90 % | — | Plan emergencia | Anual |
| Brechas identificadas | N° brechas por ejercicio | Documentar todas | — | AAR | Por ejercicio |
| Brechas corregidas | Brechas corregidas / Brechas identificadas en AAR previo × 100 | ≥80 % | — | Seguimiento AAR | Semestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Ejercicios rutinarios sin aprendizaje | Escenarios variados, inyectos sorpresa |
| AAR sin seguimiento | Integrar hallazgos en plan de mejora con seguimiento formal |

Ref: HSEEP (Homeland Security Exercise and Evaluation Program) 2020; OPS Hospital Seguro; MINSAL Plan de Emergencia; US Army AAR Framework.

## 11. Salud digital e interoperabilidad

### 11.1 HIS/EHR y módulos de red

Ecosistema de sistemas de información en salud que soporta la operación de la red asistencial.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| HCE (EHR) | Historia clínica electrónica compartida, acceso multi-establecimiento |
| EMPI | Enterprise Master Patient Index: identificación única de pacientes |
| LIS | Laboratory Information System: órdenes, resultados, trazabilidad |
| RIS/PACS | Radiology IS + Picture Archiving: órdenes, imágenes, informes |
| Módulos de red | Referencia/contrarreferencia, gestión de camas, GES, lista de espera |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cobertura HCE | Establecimientos con HCE operativa / Total establecimientos × 100 | 100 % | — | TI red | Semestral |
| Duplicados EMPI | Registros duplicados / Total registros × 100 | ≤2 % | HIMSS ≤1 % | HIMSS 2023 | Trimestral |
| Disponibilidad sistemas críticos | Uptime sistemas core / Tiempo total × 100 | ≥99.5 % | — | TI | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Sistemas heterogéneos no integrados | Bus de integración (ESB/iPaaS), estándares abiertos |
| Caída de HCE sin contingencia | Procedimiento manual documentado, DRP TI |

Ref: HIMSS EMRAM 2023; HL7 International; MINSAL Estrategia Digital en Salud 2023; OMS Digital Health 2020.

### 11.2 Interoperabilidad

Capacidad de sistemas de información para intercambiar datos con significado preservado.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| HL7 FHIR R4 | Estándar de interoperabilidad basado en APIs RESTful |
| HL7 v2/CDA | Mensajería y documentos clínicos (legado, transición) |
| SNOMED CT | Terminología clínica: diagnósticos, procedimientos, hallazgos |
| LOINC | Nomenclatura universal de laboratorio y observaciones clínicas |
| CIE-10/CIE-11 | Clasificación estadística de enfermedades |
| Niveles de interoperabilidad | Técnica → sintáctica → semántica → organizacional |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| APIs FHIR publicadas | APIs operativas / APIs requeridas × 100 | ≥50 % | — | TI red | Semestral |
| Codificación SNOMED | Registros con código SNOMED / Total registros clínicos × 100 | ≥60 % | — | HCE | Trimestral |
| Mensajes HL7 exitosos | Mensajes procesados OK / Total mensajes × 100 | ≥99 % | — | Bus integración | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Mapeo terminológico incorrecto | Validación por comité clínico, mapas de referencia SNOMED |
| Vendor lock-in | Cláusulas de interoperabilidad en contratos, APIs abiertas |

Ref: HL7 FHIR R4; SNOMED International 2023; LOINC (Regenstrief); MINSAL Estándar de Interoperabilidad 2023; OMS Digital Health 2020.

### 11.3 Telemedicina y atención virtual

Prestación de servicios clínicos a distancia mediante tecnologías de información y comunicación.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Teleconsulta sincrónica | Videoconsulta médico-paciente en tiempo real |
| Teleconsultoría | Médico APS–especialista, asincrónica (store & forward) o sincrónica |
| Telemonitoreo | Dispositivos remotos (presión, glicemia, saturación) con alertas |
| Tele-urgencia | Soporte especialista a distancia para urgencias remotas |
| Regulación | Ley 21.541 (Telemedicina Chile), consentimiento específico |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Teleconsultas / Total consultas | Teleconsultas / (Teleconsultas + Presenciales) × 100 | ≥20 % | — | Agendamiento | Trimestral |
| Satisfacción teleconsulta | PREMs teleconsulta | ≥80 % | — | Encuesta | Trimestral |
| Resolución teleconsultoría | IC resueltas por teleconsultoría / Total teleconsultorías × 100 | ≥60 % | — | eReferral | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Brecha digital en pacientes vulnerables | Puntos de telemedicina asistida en APS, capacitación digital |
| Calidad técnica insuficiente | Estándares mínimos de conectividad y equipamiento |

Ref: Ley 21.541 (Telemedicina Chile); OMS Telemedicine Guidelines 2022; ATA Practice Guidelines 2023; MINSAL Orientaciones Telemedicina 2023.

### 11.4 Analítica e IA clínica/operativa

Aplicación de ciencia de datos e inteligencia artificial para mejorar decisiones clínicas y operativas.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Analítica descriptiva | Dashboards, reportería automatizada, data warehouse |
| Analítica predictiva | Modelos de riesgo (readmisión, deterioro, no-show, demanda) |
| Analítica prescriptiva | Optimización de agendas, asignación de recursos |
| IA clínica | Soporte diagnóstico (imagenología, patología), alertas tempranas (NEWS) |
| Model cards | Documentación estandarizada: performance, sesgos, limitaciones, validación |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Modelos en producción | Modelos desplegados / Modelos desarrollados × 100 | ≥30 % | — | Data science | Semestral |
| Alertas accionadas | Alertas que generaron acción clínica / Total alertas × 100 | ≥50 % | — | HCE | Trimestral |
| Sesgo validado | Modelos con análisis de equidad documentado / Total modelos × 100 | 100 % | — | Model cards | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Sesgo algorítmico reproduce inequidad | Análisis de equidad por subgrupo, auditoría periódica |
| Sobre-confianza en predicciones | IA como apoyo, decisión final siempre humana |

Ref: WHO Ethics and Governance of AI for Health 2021; FDA AI/ML Action Plan 2023; NICE Evidence Standards for Digital Health Technologies 2022; MINSAL Estrategia Digital 2023.

### 11.5 Gobierno de datos y seguridad

Marco de gobernanza para gestionar datos como activo estratégico con protección de privacidad y seguridad.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Data stewards | Responsables de calidad y uso de datos por dominio |
| Diccionario de datos | Catálogo con definiciones, formatos, reglas de validación |
| Privacidad | Ley 19.628 (Datos personales), Ley 20.584 (Ficha clínica), anonimización |
| Seguridad | ISO 27001, control de acceso, cifrado, monitoreo de brechas |
| Continuidad | ISO 22301, backup, DRP, pruebas de restauración |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Incidentes de seguridad datos | N° brechas de datos / año | 0 | — | CISO | Anual |
| Completitud diccionario | Variables documentadas / Total variables sistemas × 100 | ≥80 % | — | Data governance | Semestral |
| Cumplimiento ISO 27001 | Controles conformes / Total controles Anexo A × 100 | ≥90 % | — | Auditoría TI | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Fuga de datos clínicos | DLP (Data Loss Prevention), cifrado, auditoría de accesos |
| Datos sin dueño | Asignación obligatoria de data steward por sistema |

Ref: Ley 19.628 (Datos Personales Chile); Ley 20.584 art. 12-13 (Ficha clínica); ISO 27001:2022; ISO 22301:2019; HIPAA (referencia internacional).

## 12. Datos, indicadores, desempeño y madurez

### 12.1 Modelo de datos y calidad

Arquitectura de datos que asegura disponibilidad, integridad y trazabilidad para la toma de decisiones.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Data warehouse / data lake | Repositorio centralizado para analítica (star schema / raw) |
| Diccionario de datos | Definición, formato, dominio, fuente, responsable por variable |
| Linaje de datos | Trazabilidad origen→transformación→consumo |
| Calidad de datos (DQ) | Dimensiones: completitud, exactitud, oportunidad, consistencia |
| ETL/ELT | Procesos de extracción, transformación y carga con validación |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Completitud datos clave | Campos obligatorios completos / Total campos obligatorios × 100 | ≥95 % | — | DQ report | Mensual |
| Oportunidad | Datos disponibles en plazo / Total datos × 100 | ≥90 % | — | ETL monitoring | Mensual |
| Score DQ compuesto | Promedio ponderado 4 dimensiones | ≥85 % | — | Data governance | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Silos de datos no integrados | Bus de integración, catálogo de fuentes autoritativas |
| Datos de baja calidad generan malas decisiones | Reglas de validación en origen, DQ dashboard |

Ref: DAMA DMBOK 2.0 (Data Management); HIMSS Data Quality Framework 2023; MINSAL Estándar de Datos en Salud 2023.

### 12.2 KPI clínicos y operativos

Catálogo estandarizado de indicadores clave para monitorear desempeño clínico y operativo de la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| KPI clínicos | Mortalidad ajustada, readmisión, IAAS, bundle compliance, PROMs |
| KPI operativos | Ocupación, estancia media, lista espera, tiempo puerta-aguja, productividad |
| KPI financieros | Costo por egreso, costo por case-mix, ejecución presupuestaria |
| KPI experiencia | NPS, PREMs, reclamos, tiempo espera percibido |
| Ficha técnica del indicador | Nombre, definición, fórmula, fuente, periodicidad, responsable, meta, benchmark |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Catálogo KPI documentado | KPI con ficha técnica / Total KPI × 100 | 100 % | — | Calidad/gestión | Anual |
| KPI con dato disponible | KPI con medición ≤1 mes / Total KPI × 100 | ≥90 % | — | BI | Mensual |
| KPI en meta | KPI que cumplen meta / Total KPI medidos × 100 | ≥70 % | — | BSC | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Exceso de indicadores sin priorización | Máximo 20 KPI por nivel (operativo/táctico/estratégico) |
| Definiciones inconsistentes entre establecimientos | Ficha técnica única y validada por comité de red |

Ref: AHRQ Quality Indicators 2023; OCDE Health Care Quality Indicators; NHS Outcomes Framework 2023; MINSAL Indicadores de Gestión Hospitalaria.

### 12.3 Tableros y BSC/OKR

Herramientas de visualización y marcos de gestión para alinear desempeño con estrategia.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Dashboard operativo | Actualización diaria/RT: flujo, camas, urgencia, alertas |
| Dashboard táctico | Actualización semanal/mensual: producción, listas espera, calidad |
| Dashboard estratégico | Actualización trimestral: Cuádruple Meta, BSC, avance roadmap |
| BSC (Balanced Scorecard) | 4 perspectivas: paciente, procesos, aprendizaje, financiera |
| OKR (Objectives & Key Results) | Ciclos trimestrales, alineamiento vertical y horizontal |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Uso de dashboards | Usuarios activos / Usuarios con acceso × 100 | ≥60 % | — | BI analytics | Mensual |
| BSC actualizado | Indicadores BSC con dato vigente / Total indicadores BSC × 100 | ≥95 % | — | BSC | Trimestral |
| OKR completados | KR logrados (≥70 %) / Total KR × 100 | ≥70 % | — | OKR review | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Dashboard no consultado | Integrar en huddles, hacer accionable |
| OKR desalineados con estrategia | Cascada desde dirección, revisión trimestral |

Ref: Kaplan & Norton BSC 1996; Doerr OKR 2018; NHS Model Hospital Dashboard 2023; Few 2006 (Dashboard Design).

### 12.4 Evaluación de impacto

Métodos para medir el efecto real de intervenciones, proyectos y programas en la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Antes-después | Comparación pre/post con serie temporal interrumpida (ITS) |
| Grupo control | Diseño cuasi-experimental cuando sea factible |
| Análisis costo-efectividad | Costo por AVAC ganado, costo por caso evitado |
| Evaluación de beneficios | Tangibles (ahorro, producción) + intangibles (satisfacción, clima) |
| Framework RE-AIM | Reach, Effectiveness, Adoption, Implementation, Maintenance |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Proyectos con evaluación de impacto | Proyectos evaluados / Proyectos completados × 100 | ≥50 % | — | PMO | Anual |
| ROI promedio proyectos | (Beneficio − Inversión) / Inversión × 100 promedio | ≥100 % | — | Finanzas | Anual |
| Evaluaciones publicadas | N° evaluaciones con reporte formal | ≥3/año | — | Calidad/investigación | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Atribución incorrecta de causalidad | Métodos rigurosos (ITS, difference-in-differences) |
| Evaluación solo de éxitos | Incluir proyectos fallidos en análisis |

Ref: RE-AIM Framework (Glasgow 2019); Campbell & Stanley (quasi-experimental); NICE Guidelines Manual (economic evaluation); Drummond 2015.

### 12.5 Transparencia y rendición de cuentas

Mecanismos para comunicar resultados a la comunidad, autoridades y stakeholders.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Cuenta pública | Presentación anual obligatoria (Ley 20.285) |
| Portal de transparencia | Indicadores publicados, presupuesto, dotación |
| Reporte a Superintendencia | Indicadores de acreditación, reclamos, GES |
| Participación ciudadana | Consejos consultivos con acceso a datos de desempeño |
| Benchmarking público | Comparación entre establecimientos (anonimizado o nominal) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Solicitudes transparencia respondidas | Solicitudes respondidas en plazo / Total solicitudes × 100 | ≥95 % | Ley 20.285 | Portal Transparencia | Mensual |
| Indicadores publicados | KPI publicados en portal / KPI del catálogo × 100 | ≥50 % | — | Portal web | Semestral |
| Cuenta pública realizada | Cumplimiento anual | 100 % | — | Dirección | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Transparencia selectiva (solo buenos resultados) | Publicación de todos los indicadores, incluidos rojos |
| Datos sin contexto generan alarma | Acompañar con explicación y plan de mejora |

Ref: Ley 20.285 (Transparencia); Ley 20.730 (Lobby); Superintendencia de Salud; OCDE Government at a Glance 2023.

### 12.6 Modelos de madurez

Rúbricas escalonadas para evaluar el nivel de desarrollo de capacidades de gestión de la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Nivel 1 — Inicial | Procesos ad hoc, reactivo, sin estandarización |
| Nivel 2 — Repetible | Procesos documentados en algunas áreas, incipiente medición |
| Nivel 3 — Definido | Procesos estandarizados transversalmente, KPI operativos |
| Nivel 4 — Gestionado | Decisiones basadas en datos, mejora continua sistemática |
| Nivel 5 — Optimizado | Innovación proactiva, benchmarking, learning organization |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Score de madurez global | Promedio ponderado de dimensiones evaluadas (1-5) | ≥3.0 | — | Autoevaluación | Anual |
| Dimensiones en nivel ≥3 | Dimensiones ≥3 / Total dimensiones × 100 | ≥60 % | — | Autoevaluación | Anual |
| Progresión anual | Score año actual − Score año anterior | ≥+0.3 | — | Serie temporal | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Autoevaluación inflada | Validación cruzada con evidencia documental |
| Modelo genérico no aplica | Adaptar dimensiones al contexto de red asistencial chilena |

Ref: HIMSS EMRAM (digital maturity); NHS Improvement Maturity Matrix 2022; CMMI Institute; EFQM Excellence Model 2020.

### 12.7 Auditorías clínicas y operativas

Revisión sistemática de prácticas contra estándares definidos para identificar brechas y mejorar.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Auditoría de ficha clínica | Completitud, calidad registro, adherencia a GPC |
| Auditoría de codificación | Calidad CIE-10, GRD, coherencia diagnóstico-procedimiento |
| Auditoría de procesos | Cumplimiento SOP, tiempos, flujos |
| Peer review | Revisión entre pares de casos complejos o con resultado adverso |
| Auditoría de uso de recursos | Pertinencia de exámenes, estadía, derivaciones |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Fichas auditadas | Fichas revisadas / Total egresos × 100 | ≥10 % | — | Calidad | Trimestral |
| Concordancia codificación | Concordancia auditor-codificador / Total auditados × 100 | ≥85 % | — | GRD | Semestral |
| Peer reviews realizados | Casos revisados / Casos elegibles × 100 | ≥80 % | — | Comité clínico | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Auditoría percibida como persecución | Marco formativo, confidencialidad, feedback constructivo |
| Hallazgos sin plan de acción | Cierre obligatorio con AC verificada |

Ref: NHS Clinical Audit Standards 2023; NICE Clinical Audit Criteria; MINSAL Norma Auditoría Médica 2018; ACHS Estándares Acreditación.

### 12.8 Benchmarking y Learning Health System

Comparación sistemática de desempeño entre establecimientos y ciclo de aprendizaje organizacional continuo.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Benchmarking interno | Comparación entre servicios/establecimientos de la misma red |
| Benchmarking externo | Comparación con redes similares nacionales e internacionales |
| Learning Health System | Ciclo: datos→conocimiento→práctica→datos (IOM/NAM) |
| Comunidades de práctica | Grupos inter-establecimiento por tema (GPC, gestión, TI) |
| Transferencia de buenas prácticas | Repositorio de innovaciones con evaluación de replicabilidad |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| KPI con benchmark externo | KPI comparados con referente externo / Total KPI × 100 | ≥30 % | — | BI | Anual |
| Buenas prácticas transferidas | Prácticas replicadas de otra unidad / Prácticas identificadas × 100 | ≥20 % | — | Gestión conocimiento | Anual |
| Comunidades de práctica activas | Comunidades con ≥4 sesiones/año / Total comunidades × 100 | ≥80 % | — | Gestión conocimiento | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Comparación injusta por case-mix diferente | Ajuste por riesgo (GRD, ACG) |
| Benchmark sin acción | Plan de mejora para KPI bajo percentil 25 |

Ref: NAM Learning Health System 2013; NHS Model Hospital Benchmarking 2023; IHI Collaborative Model; Wenger Communities of Practice 1998.

### 12.9 Lecciones aprendidas (AAR)

Proceso estructurado para capturar, documentar y difundir aprendizajes de eventos, proyectos y ejercicios.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| After Action Review | ¿Qué debía ocurrir? ¿Qué ocurrió? ¿Por qué? ¿Qué haremos diferente? |
| Formato estandarizado | Evento, participantes, hallazgos, acciones, responsable, plazo |
| Repositorio de lecciones | Base de datos búsqueda por tema, área, tipo de evento |
| Difusión | Resumen ejecutivo a toda la red, incorporación en capacitación |
| Cierre de ciclo | Verificación de que la lección se incorporó a procesos/protocolos |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| AAR realizados | AAR post-evento o proyecto / Eventos elegibles × 100 | ≥80 % | — | Gestión conocimiento | Trimestral |
| Lecciones incorporadas | Lecciones que modificaron proceso / Total lecciones × 100 | ≥50 % | — | Gestión conocimiento | Semestral |
| Repositorio consultado | Consultas al repositorio / mes | ≥10 | — | Analytics | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| AAR como trámite sin aprendizaje | Facilitador entrenado, participación de involucrados |
| Lecciones no accesibles | Repositorio digital con búsqueda, tags, alertas |

Ref: US Army AAR Framework; NASA Lessons Learned; NHS After Action Review Guide 2022; Collison & Parcell 2004.

### 12.10 Publicación y transferencia de conocimiento

Mecanismos para sistematizar y compartir el conocimiento generado en la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Publicaciones científicas | Artículos en revistas indexadas a partir de datos de la red |
| Reportes técnicos | Documentos internos con hallazgos, metodología, recomendaciones |
| Congresos y jornadas | Presentación de experiencias en foros nacionales e internacionales |
| Colaboración académica | Convenios con universidades para investigación operativa |
| Knowledge management | Estrategia explícita de gestión del conocimiento organizacional |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Publicaciones anuales | N° artículos publicados en revistas indexadas | ≥3 | — | Investigación | Anual |
| Presentaciones en congresos | N° trabajos presentados | ≥5 | — | Investigación | Anual |
| Convenios académicos activos | N° convenios vigentes con universidades | ≥2 | — | Dirección | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Datos no disponibles para investigación | Data governance con política de uso secundario |
| Publicación sin autorización ética | Comité de ética institucional para toda investigación |

Ref: CONICYT/ANID; Ley 20.120 (Investigación en humanos); ICMJE Recommendations; NHS Research Governance Framework 2023.

## 13. Finanzas y cadena de suministro

### 13.1 Presupuestación y costeo

Sistemas de planificación financiera y determinación de costos para la gestión eficiente de la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Presupuesto público | Ley de Presupuestos, programa presupuestario, subtítulos |
| Costeo ABC | Activity-Based Costing: asignación por actividades consumidas |
| GRD/DRG | Grupos Relacionados por el Diagnóstico: costeo por case-mix |
| Costo por egreso | Benchmark para comparación entre establecimientos |
| Proyección financiera | Escenarios a 3-5 años con supuestos de demanda y costos |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Ejecución presupuestaria | Gasto ejecutado / Presupuesto aprobado × 100 | 95-100 % | — | Finanzas | Mensual |
| Costo por egreso ajustado | Costo total / Egresos ajustados por case-mix | Según benchmark | — | GRD | Trimestral |
| Variación costo real vs. presupuesto | (Costo real − Presupuesto) / Presupuesto × 100 | ≤5 % | — | Finanzas | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Subejecución por procesos de compra lentos | Planificación de adquisiciones alineada con presupuesto |
| Costeo impreciso sin ABC | Implementación progresiva ABC en servicios de mayor costo |

Ref: DIPRES Chile (Dirección de Presupuestos); MINSAL Manual GRD; Kaplan & Anderson TDABC 2007; HFMA Cost Accounting Standards 2023.

### 13.2 Compras públicas y logística clínica

Gestión de adquisiciones y cadena de suministro de insumos médicos y farmacéuticos.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Compras Ley 19.886 | ChileCompra, convenio marco, licitación pública, trato directo |
| CENABAST | Central de Abastecimiento del SNSS: compra consolidada |
| Gestión de inventario | ABC/XYZ, punto de reposición, stock de seguridad |
| Cadena de frío | Vacunas, hemoderivados, biológicos: trazabilidad térmica |
| Farmacovigilancia | Notificación RAM, retiros de mercado, trazabilidad lotes |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Quiebre de stock crítico | Días con quiebre insumo crítico / Días totales × 100 | ≤2 % | — | Farmacia/abastecimiento | Mensual |
| Rotación de inventario | Consumo anual / Inventario promedio | ≥6 | — | Logística | Trimestral |
| Ahorro por compra consolidada | (Precio unitario mercado − Precio CENABAST) / Precio mercado × 100 | ≥15 % | — | CENABAST | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Quiebre de insumo crítico | Stock de seguridad 15 días, proveedores alternativos |
| Sobrestock y vencimiento | Rotación FIFO, inventario ABC, consumo proyectado |

Ref: Ley 19.886 (Compras Públicas); CENABAST; MINSAL Norma de Farmacia; WHO Good Distribution Practices 2022.

### 13.3 Pago por valor y desempeño

Modelos de financiamiento que vinculan remuneración a resultados de calidad y eficiencia.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Fee-for-service | Pago por prestación individual (modelo base Chile) |
| Per cápita | Pago por persona adscrita ajustado por riesgo (APS) |
| Bundled payment | Pago único por episodio completo de cuidado |
| Pay-for-performance (P4P) | Componente variable según cumplimiento de indicadores |
| Penalidades por calidad | Descuento por readmisiones evitables, IAAS, eventos centinela |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| % financiamiento vinculado a calidad | Monto P4P / Presupuesto total × 100 | ≥10 % | CMS 9 % (2023) | CMS 2023 | Anual |
| Cumplimiento metas P4P | Metas P4P cumplidas / Total metas × 100 | ≥80 % | — | Gestión financiera | Trimestral |
| Penalidades aplicadas | Monto penalidades / Presupuesto total × 100 | ≤2 % | — | Finanzas | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Cherry-picking (selección adversa de pacientes) | Ajuste por riesgo, indicadores de equidad |
| Gaming de indicadores | Auditoría externa, indicadores de resultado |

Ref: CMS Value-Based Programs 2023; NHS Payment by Results 2023; FONASA Mecanismos de Pago; Porter & Kaplan 2016 (VBHC).

### 13.4 Inversiones y evaluación económica

Evaluación técnico-económica de proyectos de inversión en infraestructura, tecnología y programas.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| ETS (Evaluación Tecnologías Sanitarias) | Eficacia, seguridad, costo-efectividad, impacto presupuestario |
| VAN/TIR | Valor Actual Neto, Tasa Interna de Retorno (proyectos infraestructura) |
| Análisis costo-efectividad | ICER: costo incremental por AVAC ganado |
| Análisis de impacto presupuestario | Efecto en presupuesto de incorporar nueva tecnología/programa |
| Metodología SNI | Sistema Nacional de Inversiones (MIDESO) para inversión pública |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Proyectos con evaluación económica | Proyectos evaluados / Total proyectos inversión × 100 | 100 % | SNI requerido | SNI-MIDESO | Por proyecto |
| VAN positivo | Proyectos con VAN > 0 / Total proyectos evaluados × 100 | ≥80 % | — | Finanzas | Anual |
| Ejecución inversiones | Inversión ejecutada / Inversión aprobada × 100 | ≥85 % | — | Finanzas | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Inversión sin evaluación de impacto posterior | Evaluación ex-post obligatoria a 2 años |
| Sesgo optimista en proyecciones | Reference class forecasting, análisis de sensibilidad |

Ref: MIDESO SNI Chile; NICE Technology Appraisals; Drummond 2015 (Economic Evaluation); WHO-CHOICE 2023.

### 13.5 Fraude, desperdicio y abuso (FWA)

Prevención, detección y respuesta ante uso indebido de recursos en la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Fraude | Acción deliberada para obtener beneficio indebido (licencias falsas, sobrefacturación) |
| Desperdicio | Uso ineficiente de recursos sin intención dolosa (sobreuso, duplicación) |
| Abuso | Prácticas que exceden lo necesario (exámenes innecesarios, estadía prolongada) |
| Analítica de detección | Algoritmos de anomalía en facturación, prescripción, licencias |
| Canal de denuncia | Línea confidencial, protección al denunciante |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Casos FWA detectados | N° casos investigados / año | Monitorear tendencia | — | Auditoría | Anual |
| Recupero financiero | Monto recuperado por FWA / Monto total FWA estimado × 100 | ≥50 % | — | Finanzas | Anual |
| Denuncias procesadas | Denuncias investigadas / Denuncias recibidas × 100 | 100 % | — | Canal denuncia | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Cultura de tolerancia al desperdicio | Sensibilización, indicadores de eficiencia visibles |
| Represalias contra denunciantes | Ley 20.205 (Protección funcionario denunciante) |

Ref: CMS FWA Prevention 2023; NHCAA (National Health Care Anti-Fraud Association); Ley 20.205; Contraloría General de la República.

## 14. Gestión del cambio e implementación

### 14.1 Caso para el cambio y stakeholders

Construcción del argumento para el cambio y mapeo de actores clave.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Burning platform | Datos que demuestran urgencia del cambio (brechas, riesgos, benchmarks) |
| Visión del estado futuro | Descripción concreta del resultado deseado |
| Mapa de stakeholders | Poder × interés, estrategia por cuadrante |
| Análisis de resistencia | Fuentes, intensidad, estrategia de abordaje por grupo |
| Coalición de liderazgo | Grupo sponsor multidisciplinario con poder de decisión |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Stakeholders mapeados | Stakeholders con estrategia definida / Total identificados × 100 | 100 % | — | PMO cambio | Al inicio |
| Coalición operativa | Miembros activos coalición / Miembros definidos × 100 | ≥80 % | — | PMO cambio | Mensual |
| Comprensión del caso | % personal que entiende el caso para el cambio (encuesta) | ≥70 % | — | Encuesta | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Caso no convincente | Datos locales, testimonios de pacientes/equipo |
| Coalición sin poder real | Incluir director y jefes de servicio clave |

Ref: Kotter 8 Steps 2012; Prosci ADKAR; NHS Change Model 2018; IHI Psychology of Change 2018.

### 14.2 Metodologías

Marcos de gestión del cambio que guían la transformación organizacional.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| ADKAR | Awareness, Desire, Knowledge, Ability, Reinforcement |
| Lean-Agile | Sprints de mejora, iteraciones cortas, feedback continuo |
| Kotter 8 pasos | Urgencia → coalición → visión → comunicar → empoderar → quick wins → consolidar → anclar |
| Modelo IHI | Driver diagram + PDSA cycles + medición + propagación |
| Hybrid | Combinar ADKAR (gestión personas) + Lean (gestión procesos) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Avance ADKAR | % personas en fase Ability o superior | ≥60 % a 6 meses | Prosci benchmark 50 % | Prosci 2023 | Trimestral |
| Sprints completados | Sprints finalizados / Sprints planificados × 100 | ≥85 % | — | PMO | Quincenal |
| Velocidad de adopción | % usuarios activos del nuevo proceso/sistema por mes | Curva S objetivo | — | Analytics | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Metodología como receta sin adaptación | Contextualizar al entorno público de salud chileno |
| Fatiga de cambio | Priorizar iniciativas, no superponer más de 2 cambios mayores |

Ref: Prosci ADKAR 2023; Kotter 2012; IHI Spread Framework 2006; SAFe Lean-Agile 2023.

### 14.3 PMO, riesgos y dependencias

Estructura de gestión de proyectos para coordinar implementación de cambios en la red.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| PMO (Project Management Office) | Oficina de proyectos: estándares, portafolio, reporting |
| RAID log | Risks, Assumptions, Issues, Dependencies — seguimiento continuo |
| Gantt / Kanban | Planificación temporal + gestión visual de tareas |
| Gestión de dependencias | Mapa de prerequisitos entre proyectos y áreas |
| Reporting ejecutivo | Status report semanal: RAG (Red/Amber/Green) por proyecto |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Proyectos en plazo | Proyectos según cronograma / Total proyectos × 100 | ≥70 % | PMI 60 % | PMI Pulse 2023 | Mensual |
| Issues críticos abiertos | N° issues rojos sin plan de acción | 0 | — | RAID log | Semanal |
| Dependencias gestionadas | Dependencias con owner / Total dependencias × 100 | 100 % | — | RAID log | Quincenal |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| PMO burocrática sin valor | Foco en facilitación, no control excesivo |
| Dependencias ocultas | Mapeo explícito al inicio, revisión en cada sprint |

Ref: PMI PMBOK 7th Edition 2021; PRINCE2 2023; SAFe Portfolio Management; NHS Project Delivery Framework 2023.

### 14.4 Comunicación y engagement

Estrategia de comunicación para generar comprensión, compromiso y participación durante el cambio.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Plan de comunicación | Audiencia, mensaje, canal, frecuencia, responsable |
| Canales múltiples | Email, intranet, reuniones, cartelería, WhatsApp institucional, video |
| Storytelling | Casos de éxito, testimonios, journey del paciente |
| Feedback bidireccional | Encuestas pulso, buzón sugerencias, town halls |
| Champions de cambio | Red de agentes de cambio en cada unidad |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Alcance comunicación | Personas alcanzadas / Audiencia objetivo × 100 | ≥80 % | — | Analytics comunicación | Mensual |
| Engagement | Tasa de apertura/interacción en canales digitales | ≥40 % | — | Analytics | Mensual |
| Champions activos | Champions con ≥1 acción/mes / Total champions × 100 | ≥70 % | — | Red de champions | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Comunicación unidireccional | Town halls, encuestas pulso, espacios de diálogo |
| Mensaje inconsistente | Kit de comunicación centralizado, vocería alineada |

Ref: Prosci Communication Best Practices 2023; NHS Engage and Involve 2022; IHI Science of Improvement Communications.

### 14.5 Escalamiento y sostenibilidad

Métodos para expandir intervenciones exitosas y asegurar permanencia de los cambios.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Spread framework | IHI: Setup → Develop the Better Idea → Test → Spread → Sustain |
| Stick rate | % de adopción sostenida a 6 y 12 meses post-implementación |
| Estandarización | Incorporar cambio en SOPs, protocolos, sistemas (hardwire) |
| Monitoreo post-implementación | Control charts, auditorías periódicas |
| Retiro de soporte | Plan gradual de reducción de apoyo externo |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Stick rate 6 meses | Unidades sosteniendo cambio a 6m / Total unidades × 100 | ≥80 % | — | PMO | Semestral |
| Stick rate 12 meses | Unidades sosteniendo cambio a 12m / Total unidades × 100 | ≥70 % | — | PMO | Anual |
| Escalamiento exitoso | Unidades expandidas con resultados positivos / Total expandidas × 100 | ≥75 % | — | PMO | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Regresión al estado anterior | Hardwire en sistemas, auditoría, indicadores en BSC |
| Escalamiento prematuro sin validación | Criterios de go/no-go para expandir |

Ref: IHI Framework for Spread 2006; NHS Sustainability Model 2017; Fixsen Implementation Science 2005.

### 14.6 Plan 30-60-90 días y quick wins

Hoja de ruta de implementación temprana con victorias rápidas para generar momentum.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| 0-30 días | Diagnóstico rápido, quick wins, coalición, comunicación de lanzamiento |
| 31-60 días | Implementación piloto, primeros PDSA, entrenamiento inicial |
| 61-90 días | Evaluación piloto, ajustes, plan de escalamiento |
| Quick wins | Mejoras visibles de bajo costo/esfuerzo que generan credibilidad |
| Métricas tempranas | Indicadores de proceso que confirmen avance |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Quick wins logrados | QW completados / QW planificados × 100 | ≥80 % a 30 días | — | PMO | Día 30 |
| Piloto lanzado en plazo | Piloto operativo ≤60 días (sí/no) | Sí | — | PMO | Día 60 |
| Plan de escalamiento aprobado | Aprobación formal ≤90 días (sí/no) | Sí | — | Consejo directivo | Día 90 |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Quick wins triviales sin impacto | Seleccionar QW visibles para usuarios y pacientes |
| Plan 30-60-90 demasiado ambicioso | Scope realista, buffer para imprevistos |

Ref: Watkins First 90 Days 2013; IHI 90-Day Process 2017; Prosci Quick Wins Guidance 2023.

### 14.7 MVP por línea de cuidado

Producto mínimo viable aplicado a la transformación de una línea de cuidado específica.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Selección de línea | Criterios: volumen, brecha, factibilidad, visibilidad |
| MVP scope | Funcionalidad mínima que entrega valor (ej.: ruta E2E para 1 patología) |
| Build-Measure-Learn | Ciclo iterativo: construir → medir → aprender → iterar |
| Criterios de éxito | KPIs específicos que validan el MVP |
| Pivote o escala | Decisión formal post-MVP: ajustar, escalar o descartar |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| MVP lanzado en plazo | Días desde aprobación hasta go-live | ≤90 días | — | PMO | Por MVP |
| Criterios de éxito cumplidos | Criterios cumplidos / Total criterios × 100 | ≥70 % | — | Evaluación MVP | Post-MVP |
| Satisfacción usuarios MVP | Score encuesta usuarios (equipo + pacientes) | ≥70 % | — | Encuesta | Post-MVP |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| MVP demasiado ambicioso | Ruthless prioritization, scope box |
| MVP exitoso no escala | Plan de escalamiento como entregable del MVP |

Ref: Lean Startup (Ries 2011); IHI Scale-up Framework; NHS Innovation Accelerator 2023.

### 14.8 Hitos y adopción

Seguimiento de la curva de adopción y cumplimiento de hitos clave del programa de cambio.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Milestone plan | Hitos críticos con fecha, responsable, criterio de logro |
| Curva de adopción | Rogers: innovadores (2.5 %) → early adopters (13.5 %) → mayoría (68 %) → rezagados (16 %) |
| Go/No-go gates | Puntos de decisión formales antes de avanzar a siguiente fase |
| Métricas de adopción | Uso del sistema, adherencia al proceso, satisfacción |
| Intervenciones por segmento | Estrategia diferenciada para early adopters vs. rezagados |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Hitos cumplidos en plazo | Hitos logrados en fecha / Total hitos × 100 | ≥80 % | — | PMO | Mensual |
| Tasa de adopción | Usuarios activos / Usuarios objetivo × 100 | ≥80 % a 6 meses | — | Analytics | Mensual |
| Early majority alcanzada | Adopción ≥50 % (sí/no, fecha) | ≤4 meses | — | Analytics | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Estancamiento en early adopters | Intervención focalizada: capacitación, soporte, incentivos |
| Hitos desactualizados | Revisión mensual con ajuste documentado |

Ref: Rogers Diffusion of Innovations 2003; Prosci Adoption Metrics 2023; NHS Digital Adoption Framework 2023.

### 14.9 Gobernanza de beneficios

Gestión sistemática de los beneficios esperados del programa de cambio.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Registro de beneficios | Beneficio, tipo (financiero/calidad/experiencia), indicador, baseline, meta, owner |
| Trazabilidad | Vinculación beneficio → proyecto → actividad |
| Medición | Baseline pre-cambio, medición periódica, atribución |
| Reporting | Informe trimestral de beneficios realizados vs. esperados |
| Responsable de beneficios | Rol distinto al project manager: foco en realización |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Beneficios realizados | Beneficios logrados / Beneficios comprometidos × 100 | ≥70 % | — | Registro beneficios | Trimestral |
| Beneficios con baseline | Beneficios con medición baseline / Total beneficios × 100 | 100 % | — | Registro beneficios | Al inicio |
| Valor financiero realizado | Monto ahorrado o generado / Monto proyectado × 100 | ≥60 % | — | Finanzas | Semestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Beneficios declarados sin medición | Baseline obligatorio antes de aprobar proyecto |
| Atribución incorrecta | Metodología rigurosa, grupo control cuando factible |

Ref: Managing Successful Programmes (AXELOS 2020); PMI Benefits Realization Management 2019; NHS Benefits Management Framework 2023.

### 14.10 Cierre y handover

Proceso formal de cierre de proyectos y transferencia a operación continua.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Criterios de cierre | Entregables completados, beneficios en medición, documentación lista |
| Handover pack | SOPs actualizados, capacitación completa, soporte transicional |
| Transferencia a operación | Equipo operativo asume ownership, sponsor valida |
| Lecciones aprendidas | AAR formal, documentación en repositorio |
| Celebración | Reconocimiento al equipo, comunicación de logros |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Proyectos cerrados formalmente | Cierres formales / Total proyectos finalizados × 100 | 100 % | — | PMO | Trimestral |
| Handover completo | Items handover entregados / Total items checklist × 100 | 100 % | — | PMO | Por proyecto |
| AAR realizado | AAR completados / Proyectos cerrados × 100 | 100 % | — | PMO | Por proyecto |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Proyecto que nunca cierra | Fecha de cierre obligatoria en charter, revisión trimestral |
| Handover incompleto genera retroceso | Checklist de handover estandarizado, firma de aceptación |

Ref: PMI PMBOK 7th Edition (Close Phase) 2021; PRINCE2 Closing a Project 2023; NHS Project Closure Guidance 2022.
