---
_manifest:
  urn: "urn:pro:kb:gestion-redes-urgencias"
  provenance:
    created_by: "FS"
    created_at: "2026-03-03"
    source: "Síntesis multi-fuente: OPS, IHI, NICE, AHRQ, MINSAL, AHA, ACC, ESC, Cochrane"
version: "2.0.0"
status: draft
tags: [gestion-redes, urgencias, emergencias, EMS, SUH, protocolos, triaje, desastres, MCI]
lang: es
---

# Gestión de Redes Asistenciales — Red de Urgencias

## 18. Arquitectura de la red de urgencias

### 18.1 Dispositivos (EMS, SAPU/SAR, SUH)

Red escalonada de dispositivos de urgencia articulados por nivel de complejidad, cobertura territorial y capacidad resolutiva. Cada nodo tiene cartera definida y rutas preferentes de derivación.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| SAPU | Urgencia APS baja complejidad, 24/7 zonas urbanas, resolución C4-C5 |
| SAR | Punto urgencia rural, horario extendido, estabilización y derivación |
| SUH baja complejidad | Hospital comunitario, cirugía menor, laboratorio básico, imagenología convencional |
| SUH mediana complejidad | Hospital base, especialidades de guardia, pabellón 24/7, UCI/UTI |
| SUH alta complejidad | Centro de referencia regional, hemodinamia, neurocirugía, centro trauma |
| EMS/SAMU | Sistema prehospitalario: despacho, ambulancias BLS/ALS, helicóptero (según red) |
| Centro Regulador | Coordinación despacho, gestión camas urgencia, derivaciones inter-SUH |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cobertura territorial urgencia | Población a ≤30 min de SUH / Población total × 100 | ≥90 % | OMS ≥80 % | OMS Emergency Care 2019 | Anual |
| Resolutividad SAPU | Consultas resueltas SAPU / Total consultas SAPU × 100 | ≥85 % | — | MINSAL 2023 | Trimestral |
| Tasa derivación SAPU→SUH | Traslados a SUH / Consultas SAPU × 100 | ≤15 % | — | MINSAL 2023 | Mensual |
| Disponibilidad SUH alta complejidad | Horas operativas reales / Horas programadas × 100 | ≥99 % | — | Gestión interna | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Saturación SUH por consultas no urgentes | Fortalecimiento resolutividad SAPU, educación comunitaria, triaje telefónico |
| Brecha cobertura rural | SAR con telemedicina, ambulancias posicionadas en hotspots rurales |
| Fragmentación sin coordinación | Centro Regulador con visibilidad en tiempo real de camas y recursos |

Ref: Ley 19.937; DS 58/2008 (prestaciones de urgencia); OMS Emergency Care Systems Framework 2019; NT Urgencia MINSAL.

### 18.2 Regionalización y derivaciones

Asignación territorial de población a dispositivos de urgencia según complejidad y patología tiempo-dependiente. Rutas preferentes definidas por protocolo, no por proximidad geográfica exclusiva.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Mapa isócrono | Cobertura por tiempo de traslado (15/30/60 min) para cada nivel |
| Cartera diferenciada | Prestaciones por nivel de SUH, actualizadas anualmente |
| Bypass autorizado | Derivación directa a centro de referencia saltando SUH intermedio (IAM, ACV, trauma mayor) |
| Convenios inter-red | Acuerdos entre Servicios de Salud para patologías de baja frecuencia |

**IF/THEN — Destino según condición:**

| Condición | Destino | Base |
|-----------|---------|------|
| IF STEMI o sospecha ACV con déficit focal | THEN SUH con hemodinamia/neurointervención (bypass SUH intermedio) | AHA/ACC 2023; AHA/ASA 2024 |
| IF trauma mayor (ISS ≥16) o politraumatizado | THEN centro trauma nivel I/II (bypass) | ACS-COT 2022 |
| IF quemadura ≥20 % SCT o vía aérea comprometida | THEN centro quemados regional (bypass) | ABA 2023 |
| IF emergencia obstétrica (eclampsia, DPPNI, rotura uterina) | THEN SUH con maternidad de alta complejidad y UCIN | MINSAL GES |
| IF C4-C5 sin criterios de bypass | THEN SAPU/SAR más cercano | NT Urgencia MINSAL |
| IF paciente pediátrico crítico sin SUH pediátrico cercano | THEN estabilización en SUH más cercano + traslado a centro pediátrico | MINSAL 2023 |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cumplimiento ruta preferente | Pacientes derivados según protocolo / Total derivaciones × 100 | ≥90 % | — | Centro Regulador | Mensual |
| Tiempo traslado inter-SUH | Mediana tiempo salida SUH origen → llegada SUH destino | ≤60 min (urbano) | — | EMS registros | Mensual |
| Bypass efectivo STEMI | STEMI con bypass directo a hemodinamia / Total STEMI × 100 | ≥75 % | AHA: ≥80 % | AHA 2023 | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Bypass a centro colapsado | Consulta en tiempo real al Centro Regulador antes de despacho |
| Desactualización de cartera | Revisión anual de cartera + auditoría de capacidad resolutiva real |

Ref: ACS Committee on Trauma — Resources for Optimal Care 2022; AHA Mission: Lifeline 2023; NT Urgencia MINSAL.

### 18.3 Centro Regulador y despacho

Unidad operativa 24/7 que coordina despacho EMS, gestión de camas de urgencia y derivaciones inter-SUH mediante comunicación estandarizada y geolocalización.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Central telefónica 131 | Recepción llamadas, clasificación telefónica, despacho |
| Plataforma CAD (Computer-Aided Dispatch) | Geolocalización ambulancias, asignación automática por proximidad y competencia |
| Panel de camas SUH | Visibilidad en tiempo real: ocupación, disponibilidad por tipo (reanimación, observación, box) |
| Protocolos despacho | Algoritmos por categoría de llamada (A-D), priorización |
| Interoperabilidad | Integración con EDIS de SUH, registros EMS, HCE |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tiempo respuesta telefónica | Tiempo ring → contestación p90 | ≤15 seg | NENA: ≤15 seg (90 %) | NENA 2020 | Mensual |
| Tiempo despacho | Tiempo contestación → salida ambulancia p90 | ≤90 seg | NFPA 1710: ≤80 seg | NFPA 2020 | Mensual |
| Precisión clasificación telefónica | Concordancia categoría telefónica vs. categoría real en escena | ≥85 % | — | Auditoría interna | Trimestral |
| Uso geolocalización | % despachos con asignación automática GPS | ≥95 % | — | CAD | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Sobrecarga telefónica en MCI | Protocolos de escalamiento, líneas dedicadas MCI, desborde a SAPU |
| Falla sistema CAD | Respaldo manual con mapas y radio, redundancia TI |
| Descoordinación inter-Servicios de Salud | Convenios operativos, protocolos unificados, radio interoperable |

Ref: NFPA 1710/1720 (tiempos respuesta); NENA 911 Standards; MINSAL Orientaciones Red Urgencia.

## 19. Prehospitalario — EMS

### 19.1 Forecast y cobertura geoespacial

Planificación dinámica de cobertura EMS basada en demanda histórica, análisis geoespacial y posicionamiento estratégico de unidades para optimizar tiempos de respuesta.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Posts dinámicos | Ubicación de ambulancias ajustada por hora/día/estacionalidad según hotspots de demanda |
| Análisis hotspots | Mapeo de calor de eventos por geolocalización, concentración temporal |
| Modelo predictivo demanda | Series temporales + variables exógenas (clima, eventos masivos, festivos) |
| Isócronas de cobertura | Polígonos de tiempo-respuesta desde cada post (8/15/30 min) |
| System Status Management (SSM) | Reposicionamiento proactivo según nivel de disponibilidad |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tiempo respuesta urbano p90 | Minutos desde despacho → llegada a escena (percentil 90) | ≤10 min | NFPA 1710: ≤9 min (ALS) | NFPA 2020 | Mensual |
| Tiempo respuesta rural p90 | Minutos desde despacho → llegada a escena (percentil 90) | ≤20 min | NFPA 1720: variable | NFPA 2020 | Mensual |
| Cobertura 8 min | % población cubierta en ≤8 min por unidad ALS | ≥90 % urbano | UK Ambulance: 75 % Cat 1 en 8 min | NHS England 2023 | Trimestral |
| Unit Hour Utilization (UHU) | Tiempo en misión / Tiempo total disponible | 0.25–0.35 | NASEMSO: 0.25–0.40 | NASEMSO 2021 | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Modelo predictivo desactualizado | Recalibración trimestral, validación con datos reales |
| Déficit de unidades en picos | Convenios con transporte privado, ambulancias de reserva |

Ref: NFPA 1710/1720; NASEMSO Model EMS Guidelines 2021; Stout 1983 (SSM).

### 19.2 Tipología de ambulancias y dotación

Clasificación de recursos móviles EMS según capacidad resolutiva, equipamiento y competencias del equipo a bordo.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| BLS (Basic Life Support) | Técnicos paramédicos, DEA, inmovilización, O₂, traslado |
| ALS (Advanced Life Support) | Médico/enfermero + paramédico, monitorización, fármacos IV, intubación, cardioversión |
| Ambulancia de rescate | Equipo extricación vehicular, rescate en altura, HAZMAT básico |
| Helicóptero sanitario (HEMS) | Traslado crítico larga distancia, equipo ALS + intervención avanzada |
| Vehículo primera respuesta (VPR) | Respuesta rápida movilidad alta, sin capacidad traslado, estabilización inicial |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Ratio ALS/población | Unidades ALS / 100.000 hab | ≥1.0 | Variable por país | NASEMSO 2021 | Anual |
| Disponibilidad operativa flota | Unidades operativas / Unidades totales × 100 | ≥90 % | — | Gestión EMS | Mensual |
| Certificaciones vigentes tripulación | % personal con ACLS/PHTLS vigente / Total personal EMS | 100 % | — | RRHH EMS | Semestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Ambulancia ALS no disponible en zona rural | Cross-training BLS en procedimientos críticos, telemedicina en ruta |
| Equipamiento vencido o sin mantención | Checklist diario, mantenimiento preventivo programado |

Ref: NASEMSO 2021; NAEMSP Position Statements; DS 58/2008 MINSAL.

### 19.3 Protocolos clínicos prehospitalarios

Protocolos estandarizados de intervención prehospitalaria por patología tiempo-dependiente. Cada protocolo define intervención, meta temporal, criterio activación código y nivel de tripulación requerido.

**Protocolos por condición:**

| Condición | Intervención clave | Meta temporal | Activación código | Tripulación mínima |
|-----------|-------------------|---------------|-------------------|-------------------|
| IAM STEMI | ECG 12 derivaciones, aspirina, heparina, nitroglicerina, activar código IAM | ECG ≤10 min desde contacto | Elevación ST en ECG prehospitalario | ALS |
| ACV (sospecha) | Escala Cincinnati/RACE, glicemia, hora inicio, pre-notificación | Hora inicio síntomas documentada | ≥1 criterio Cincinnati positivo | ALS |
| Trauma mayor | ABCDE, control hemorragia (torniquete), inmovilización, fluidoterapia restrictiva | Tiempo en escena ≤10 min (load & go) | ISS estimado ≥16, mecanismo alto impacto | ALS |
| Sepsis | qSOFA prehospitalario, acceso venoso, fluidos, lactato POC si disponible | Fluidos iniciados en ruta | qSOFA ≥2 | ALS |
| Paro cardiorrespiratorio | RCP alta calidad, DEA/desfibrilación, adrenalina, manejo vía aérea | Desfibrilación ≤3 min desde llegada | Paciente en paro | BLS/ALS |
| Intoxicación aguda | Identificar tóxico, antídoto específico si disponible, descontaminación, monitorización | Antídoto ≤30 min si indicado | Exposición tóxica confirmada/sospechada | ALS |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| ECG prehospitalario en dolor torácico | ECG realizado / Dolor torácico atendido × 100 | ≥95 % | AHA: ≥90 % | AHA 2023 | Mensual |
| Pre-notificación código IAM/ACV | Casos con pre-notificación / Total códigos × 100 | ≥90 % | — | Registros EMS | Mensual |
| Tiempo en escena trauma | Mediana minutos en escena (trauma penetrante/contuso mayor) | ≤10 min | PHTLS: ≤10 min | NAEMT 2020 | Mensual |
| Sobrevida paro extrahospitalario (ROSC) | ROSC al ingreso SUH / Total paros atendidos × 100 | ≥30 % | Cardiac Arrest Registry: 30-35 % | CARES 2023 | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Variabilidad en adherencia a protocolos | Auditoría de registros, feedback individual, simulación trimestral |
| ECG de mala calidad | Entrenamiento técnico, transmisión a cardiólogo para validación remota |

Ref: AHA/ACC STEMI Guidelines 2023; AHA/ASA Stroke Guidelines 2024; PHTLS 10th ed.; Surviving Sepsis Campaign 2021; ILCOR 2023.

### 19.4 Telemedicina prehospitalaria

Soporte remoto especializado al equipo EMS en terreno mediante telecomunicaciones en tiempo real. Permite diagnóstico precoz, activación de códigos y orientación de manejo avanzado.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Tele-ECG | Transmisión ECG 12 derivaciones desde ambulancia a cardiólogo, interpretación remota, activación hemodinamia |
| Tele-stroke | Videoconsulta con neurólogo desde escena o ambulancia, escala NIHSS remota, decisión IVT/trombectomía |
| Tele-trauma | Guía remota por cirujano/emergenciólogo para estabilización avanzada en escena |
| Videoconferencia en ruta | Enlace audiovisual ambulancia→SUH para handoff anticipado |
| Consentimiento telemedicina | Registro verbal documentado, excepto urgencia vital (consentimiento presunto) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tele-ECG transmitidos | ECG transmitidos / ECG realizados en ambulancia × 100 | ≥90 % | — | Registros EMS | Mensual |
| Concordancia diagnóstica tele-ECG | Diagnóstico remoto concordante con diagnóstico final / Total × 100 | ≥95 % | — | Auditoría clínica | Trimestral |
| Tiempo interpretación remota | Mediana tiempo envío ECG → informe especialista | ≤5 min | — | Plataforma telemedicina | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Falla conectividad en zona rural | Redundancia satelital, transmisión diferida con store-and-forward |
| Responsabilidad médico-legal en teleconsulta | Protocolos documentados, registro audio/video, consentimiento |

Ref: NT Telemedicina MINSAL 2022; AHA Policy Statement Telemedicine 2021; ESC Position Paper Telecardiology 2022.

### 19.5 Seguridad operativa y del paciente

Protocolos de seguridad para protección del equipo EMS y del paciente durante la atención prehospitalaria.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Checklist pre-turno | Revisión vehículo, equipamiento, fármacos, comunicaciones |
| EPP escalonado | Precauciones estándar → contacto → aerosol según riesgo |
| IPC prehospitalario | Higiene de manos, limpieza ambulancia post-traslado, manejo cortopunzante |
| Seguridad en escena | Evaluación de riesgo ambiental (violencia, HAZMAT, estructura colapsada) antes de ingreso |
| Conducción segura | Velocidad regulada, uso cinturón, paciente asegurado, escolta policial si necesario |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Incidentes ocupacionales EMS | Eventos lesión/exposición / 1.000 misiones | ≤2.0 | — | Prevención de riesgos | Mensual |
| Cumplimiento checklist pre-turno | Checklists completos / Turnos totales × 100 | ≥98 % | — | Supervisión | Mensual |
| Accidentes vehículo EMS | Colisiones / 100.000 km recorridos | ≤1.0 | — | Gestión flota | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Agresión al equipo EMS | Protocolo escena insegura, escolta policial, botón de pánico |
| Exposición a patógenos | EPP disponible en ambulancia, protocolo post-exposición, vacunación completa |

Ref: OSHA EMS Worker Safety Guidelines; NAEMSP Crew Resource Management; MINSAL IPC.

### 19.6 Indicadores EMS

Tablero consolidado de indicadores prehospitalarios. Sistema de medición integral del desempeño EMS alineado con estándares internacionales.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Indicadores de despacho | Tiempo contestación, tiempo despacho, precisión categorización |
| Indicadores de respuesta | Tiempo respuesta, cobertura geográfica, disponibilidad unidades |
| Indicadores de escena | Tiempo en escena, adherencia protocolos, intervenciones realizadas |
| Indicadores de transporte | Tiempo transporte, destino correcto, pre-notificación |
| Indicadores de resultado | ROSC, sobrevida a alta, satisfacción usuario |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tiempo total llamada-hospital | Llamada 131 → llegada SUH (mediana) | ≤45 min urbano | — | Registros EMS | Mensual |
| Tasa LWBS prehospitalario | Pacientes que rechazan traslado / Total atenciones × 100 | ≤10 % | — | Registros EMS | Mensual |
| Mortalidad ajustada prehospitalaria | Fallecidos prehospitalarios / Total atenciones ajustado por gravedad | Benchmark local | Utstein ≤50 % paro | Utstein 2015 | Trimestral |
| Documentación completa | Registros con campos obligatorios completos / Total registros × 100 | ≥95 % | NEMSIS ≥90 % | NEMSIS 2023 | Mensual |

Para tablero completo de indicadores y plantillas de medición, → `urn:pro:kb:gestion-redes-herramientas` Anexo A.

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Subregistro de datos EMS | Registro electrónico obligatorio, validación automática campos |
| Indicadores sin acción correctiva | Revisión mensual con plan de mejora por indicador en rojo |

Ref: NEMSIS Data Dictionary 2023; Utstein Style Guidelines; NASEMSO Model EMS Guidelines 2021.
## 20. Flujo intrahospitalario en SUH

### 20.1 Pre-arribo y pre-notificación

Comunicación estandarizada entre EMS y SUH previo a la llegada del paciente. Permite activación anticipada de recursos y reducción de tiempos puerta-intervención.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Códigos de activación | Código IAM (STEMI), Código ACV, Código Trauma, Código Sepsis — cada uno con criterios de activación definidos |
| Canal de aviso | Radio dedicada, aplicación móvil, línea directa SUH — redundancia mínima 2 canales |
| Formato SBAR | Situation-Background-Assessment-Recommendation — estructura estandarizada de comunicación |
| Pre-activación equipo | Notificación automática a especialistas de guardia según código activado |
| Preparación box/sala | Equipamiento listo en box de reanimación o sala procedimientos según código |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tasa pre-notificación | Ingresos con pre-notificación / Total ingresos EMS × 100 | ≥90 % | — | Registros SUH | Mensual |
| Tiempo pre-aviso → llegada | Minutos entre pre-notificación y arribo ambulancia | ≥10 min | — | Registros EMS/SUH | Mensual |
| Activación código en pre-arribo | Códigos activados pre-arribo / Total códigos activados × 100 | ≥80 % | — | Registros SUH | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Sobre-activación de códigos (falsos positivos) | Auditoría concordancia código vs. diagnóstico final, feedback a EMS |
| Falla comunicación radio | Redundancia celular + radio, protocolos de contingencia |

Ref: AHA Mission: Lifeline 2023; NAEMSP Pre-notification Guidelines; Joint Commission NPSG.

### 20.2 Recepción y triaje (ESI/CTAS/MTS/SAT)

Clasificación estructurada de pacientes al ingreso del SUH mediante sistema validado de triaje en 5 niveles. Determina prioridad de atención, circuito asignado y tiempo máximo de espera.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| ESI (Emergency Severity Index) | 5 niveles basados en agudeza + recursos esperados; más usado en Chile |
| MTS (Manchester Triage System) | 5 niveles por flujogramas por queja principal + discriminadores |
| CTAS (Canadian Triage and Acuity Scale) | 5 niveles, queja principal + modificadores primer/segundo orden |
| SAT (Sistema de Atención de Triage) | Adaptación chilena MINSAL, compatible con ESI |
| Triaje electrónico | Soporte decisional informatizado, registro estructurado, timestamps automáticos |
| Re-evaluación | Protocolo de re-triaje según tiempos definidos por nivel |

**IF/THEN — Niveles ESI:**

| Nivel ESI | Condición | Acción | Tiempo máximo espera |
|-----------|-----------|--------|---------------------|
| IF ESI 1 (Resucitación) | Riesgo vital inminente: paro, shock, compromiso vía aérea | THEN atención inmediata en box reanimación | 0 min |
| IF ESI 2 (Emergencia) | Alto riesgo: dolor torácico, déficit neurológico, intoxicación grave | THEN atención prioritaria, monitorización continua | ≤10 min |
| IF ESI 3 (Urgencia) | Requiere ≥2 recursos, signos vitales estables pero alterados | THEN circuito estándar, evaluación completa | ≤30 min |
| IF ESI 4 (Menos urgente) | Requiere 1 recurso (laboratorio o imagen) | THEN fast track si disponible | ≤60 min |
| IF ESI 5 (No urgente) | No requiere recursos, consulta simple | THEN fast track, considerar derivación a APS | ≤120 min |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Door-to-triage | Mediana minutos ingreso → clasificación triaje | ≤10 min | ACEP: ≤5 min | ACEP 2023 | Mensual |
| Concordancia inter-evaluador triaje | Kappa de Cohen entre enfermeras de triaje | ≥0.70 | ESI validación ≥0.80 | Tanabe 2004 | Semestral |
| Sobre-triaje ESI 1-2 | % ESI 1-2 dados de alta sin intervención crítica / Total ESI 1-2 | ≤15 % | — | Auditoría clínica | Trimestral |
| Sub-triaje | Eventos adversos en pacientes clasificados ESI 4-5 / Total ESI 4-5 | ≤1 % | — | Registros seguridad | Trimestral |
| LWBS (Left Without Being Seen) | Pacientes que abandonan sin ser vistos / Total consultas SUH × 100 | ≤3 % | ACEP: ≤2 % | ACEP 2023 | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Sub-triaje en adultos mayores (presentación atípica) | Protocolo geriátrico de triaje, discriminadores ajustados por edad |
| Sesgo en triaje (género, etnia, idioma) | Algoritmo estandarizado, auditoría de equidad, facilitador intercultural |

Ref: ESI Implementation Handbook v4 (AHRQ 2020); Manchester Triage Group 2014; NT Urgencia MINSAL; ACEP Policy Statement Triage 2023.

### 20.3 Circuitos (fast track, estándar, reanimación)

Diferenciación de flujos internos del SUH según severidad y tipo de atención requerida. Streaming clínico para optimizar tiempos y evitar contaminación cruzada de circuitos.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Circuito reanimación | ESI 1, box dedicado, equipo trauma/paro, acceso inmediato a imagenología y laboratorio |
| Circuito estándar | ESI 2-3, boxes de evaluación, acceso a diagnóstico completo |
| Fast track | ESI 4-5, atención rápida, médico dedicado, alta en ≤2h |
| Circuito pediátrico | Separación física, personal pediátrico, ambiente diferenciado |
| Circuito psiquiátrico | Espacio seguro, contención disponible, evaluación psiquiátrica dedicada |
| Sala de procedimientos menores | Suturas, drenajes, reducción fracturas simples — evita ocupar box estándar |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Estadía fast track | Mediana minutos ingreso → alta (ESI 4-5) | ≤120 min | UK NHS: ≤120 min | NHS England 2023 | Mensual |
| Estadía circuito estándar | Mediana minutos ingreso → decisión destino (ESI 2-3) | ≤240 min | ACEP: 240 min | ACEP 2023 | Mensual |
| Uso fast track | % consultas ESI 4-5 atendidas en fast track / Total ESI 4-5 | ≥80 % | — | EDIS | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Fast track colapsado por volumen | Límite WIP, derivación a SAPU, médico de refuerzo |
| Mezcla de circuitos por falta de espacio | Diseño físico con separación, señalética, protocolos de desborde |

Ref: ACEP Emergency Department Design Guidelines 2023; NHS Emergency Care Standard; Australasian College for Emergency Medicine 2022.

### 20.4 Diagnóstico y apoyo urgente

Servicios de apoyo diagnóstico con disponibilidad 24/7 para SUH. Laboratorio point-of-care, imagenología urgente y teleradiología para SUH sin radiólogo presencial.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Laboratorio POC (point-of-care) | Troponina, lactato, gasometría, hemoglucotest, βHCG — resultado ≤15 min |
| Laboratorio central urgente | Panel completo: hemograma, bioquímica, coagulación, toxicología |
| Radiología convencional 24/7 | Rx tórax/extremidades/abdomen disponible en SUH |
| TC urgente | Scanner dedicado o prioridad SUH, protocolo ACV/politrauma/TEP |
| Ecografía POCUS | Point-of-care ultrasound en box de reanimación (FAST, ecocardiograma) |
| Teleradiología | Lectura remota para SUH sin radiólogo presencial nocturno |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| TAT laboratorio POC | Mediana minutos solicitud → resultado disponible (troponina, lactato) | ≤15 min | CAP: ≤15 min POC | CAP 2023 | Mensual |
| TAT laboratorio central urgente | Mediana minutos solicitud → resultado panel básico | ≤45 min | — | LIS | Mensual |
| TAT TC urgente | Mediana minutos solicitud → informe preliminar | ≤30 min | NICE: ≤60 min trauma | NICE 2023 | Mensual |
| Disponibilidad POCUS | % turnos con operador POCUS certificado | ≥80 % | — | RRHH SUH | Mensual |
| TAT teleradiología nocturna | Mediana minutos envío imagen → informe preliminar | ≤30 min | — | RIS | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| TAT excesivo en laboratorio central | Tubo neumático, corredor dedicado, priorización muestras SUH |
| Falta POCUS nocturno | Capacitación cruzada médicos SUH, programa certificación POCUS |

Ref: CAP Point-of-Care Testing Guidelines 2023; ACR Appropriateness Criteria; ACEP Ultrasound Guidelines 2023.

### 20.5 Interconsultas y enlace

Gestión de interconsultas desde SUH a especialidades intrahospitalarias. SLA definidos por prioridad, sistemas de comunicación estandarizados y registro de tiempos.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| SLA interconsulta urgente | Respuesta especialista ≤30 min para ESI 1-2, ≤60 min ESI 3 |
| Sistema paging/código | Llamado directo a especialista de guardia, escalonamiento automático |
| eConsult | Consulta electrónica asincrónica para casos no urgentes, resolución sin presencia física |
| Handoff estructurado | SBAR para transferencia de información entre SUH y especialidad |
| Registro de tiempos | Timestamp solicitud → aceptación → presencia física → resolución |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tiempo respuesta interconsulta urgente | Mediana minutos solicitud → presencia especialista (ESI 1-2) | ≤30 min | — | EDIS | Mensual |
| Cumplimiento SLA interconsulta | Interconsultas respondidas en plazo / Total × 100 | ≥90 % | — | EDIS | Mensual |
| Tasa eConsult resolutiva | eConsults resueltas sin presencia física / Total eConsults × 100 | ≥60 % | — | Sistema eConsult | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Especialista no responde en plazo | Escalonamiento automático a jefatura, registro de incumplimiento |
| Interconsulta innecesaria | Criterios de interconsulta explícitos, protocolos de manejo SUH |

Ref: ACEP Policy on Consultations 2022; Joint Commission Standard PC.02.02.01.

### 20.6 Observación de Corta Estadía (UOCS)

Unidad de observación con permanencia protocolizada ≤24h para pacientes que requieren evaluación seriada, tratamiento breve o espera de resultados antes de decisión de destino.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Criterios de ingreso | Dolor torácico bajo riesgo, crisis asmática, deshidratación, TEC leve, intoxicación leve |
| Criterios de exclusión | Necesidad de UCI, cirugía urgente, inestabilidad hemodinámica |
| Bundles UOCS | Evaluación seriada protocolizada por patología (ej. troponina seriada 0/3h) |
| Límite estadía | ≤24h; excedido → decisión formal (hospitalización o alta) |
| Criterios de egreso | Mejoría clínica, resultados negativos, plan de seguimiento ambulatorio |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Estadía UOCS | Mediana horas ingreso → egreso UOCS | ≤18h | ACEP: ≤24h | ACEP 2023 | Mensual |
| Tasa alta desde UOCS | Altas desde UOCS / Total ingresos UOCS × 100 | ≥70 % | — | EDIS | Mensual |
| Readmisión 72h post-UOCS | Reconsulta SUH ≤72h post-alta UOCS / Total altas UOCS × 100 | ≤5 % | — | EDIS | Mensual |
| Tasa conversión a hospitalización | Hospitalizados desde UOCS / Total ingresos UOCS × 100 | ≤30 % | — | EDIS | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| UOCS como "cama de boarding encubierta" | Auditoría de estadía, límite estricto 24h, dashboard en tiempo real |
| Alta prematura desde UOCS | Protocolos de egreso, control ambulatorio precoz, instrucciones claras |

Ref: ACEP Observation Medicine Section; American College of Observation Medicine 2022.

### 20.7 Decisión de destino

Punto de decisión crítico post-evaluación en SUH. Reglas explícitas para alta, hospitalización, traslado o derivación a hospitalización domiciliaria según condición clínica y disponibilidad de recursos.

**IF/THEN — Decisión de destino:**

| Condición | Destino | Criterio | Responsable |
|-----------|---------|----------|-------------|
| IF estable, diagnóstico cerrado, plan ambulatorio viable | THEN alta con instrucciones + control | Criterios de alta seguros, teach-back completado | Médico SUH |
| IF requiere monitoreo continuo, tratamiento IV, diagnóstico pendiente | THEN hospitalización (sala general o UTI/UCI según gravedad) | Criterios de ingreso por patología | Médico SUH + Bed manager |
| IF estable, requiere tratamiento ≤14 días, domicilio adecuado | THEN hospitalización domiciliaria (HaH) | Criterios inclusión HaH (→ `urn:pro:kb:gestion-redes-unidades` cap 17) | Coordinación HaH |
| IF requiere capacidad no disponible en SUH actual | THEN traslado a SUH de mayor complejidad | Protocolo derivación + coordinación Centro Regulador | Médico SUH + Centro Regulador |
| IF ESI 4-5 sin patología aguda | THEN derivación a APS/SAPU con hora garantizada ≤48h | Convenio red, disponibilidad confirmada | Médico SUH |

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Bed management | Gestión centralizada camas: solicitud, asignación, liberación anticipada |
| Early discharge rounds | Ronda matinal de egresos tempranos para liberar camas antes de peak SUH |
| Dashboard ocupación | Visualización en tiempo real: camas libres por servicio, UCI/UTI, UOCS |
| Criterios explícitos por patología | Guías de ingreso/alta por condición (NAC, ICC, dolor torácico, etc.) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tiempo decisión de destino | Mediana minutos ingreso SUH → decisión (alta/hospitalización/traslado) | ≤240 min | UK NHS: 4h target | NHS England 2023 | Mensual |
| Boarding time | Mediana minutos decisión hospitalización → salida SUH a cama | ≤60 min | ACEP: ≤60 min | ACEP 2023 | Mensual |
| Derivación HaH desde SUH | Pacientes derivados a HaH / Total hospitalizaciones × 100 | ≥10 % | — | EDIS + HaH | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Boarding prolongado por falta de camas | Early discharge, camas swing, escalamiento surge |
| Alta insegura por presión de flujo | Checklist de alta segura, criterios explícitos, re-evaluación si duda |

Ref: NHS 4-Hour Standard; ACEP Boarding Policy 2023; IHI Flow and Capacity Management.

## 21. Capacidad y flujo en urgencias

### 21.1 Predicción de demanda

Modelos predictivos de afluencia al SUH para planificación de dotación, insumos y capacidad instalada. Variables: día de la semana, hora, estacionalidad, clima, eventos masivos y epidemias.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Series temporales | ARIMA, Prophet: predicción demanda diaria/horaria con estacionalidad |
| Variables exógenas | Temperatura, lluvia, festividades, eventos deportivos, brotes epidémicos |
| Segmentación por triaje | Predicción separada ESI 1-2 vs. ESI 3-5 (perfiles de demanda distintos) |
| Horizonte de predicción | Corto plazo (24-72h) para dotación, mediano plazo (3-6 meses) para planificación |
| Dashboard predictivo | Visualización demanda esperada vs. capacidad disponible por turno |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Error predicción demanda | MAPE (Mean Absolute Percentage Error) | ≤15 % | — | Modelo predictivo | Mensual |
| Cobertura del modelo | % turnos con predicción disponible | 100 % | — | Dashboard | Mensual |
| Ajuste dotación a demanda | Correlación dotación real vs. demanda predicha | r ≥0.80 | — | RRHH + Modelo | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Evento no anticipado (MCI, brote) | Protocolo surge independiente del modelo, capacidad de reserva |
| Modelo obsoleto | Reentrenamiento trimestral con datos actualizados |

Ref: Wargon et al. 2009 (ED demand forecasting); IHI Flow and Capacity; Jones 2009 (forecasting models).

### 21.2 Staff planning y turnos

Planificación de dotación y programación de turnos del equipo SUH alineada con demanda predicha, competencias requeridas y normativa laboral.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Skill mix | Proporción médicos emergenciólogos, médicos generales, enfermería, paramédicos por turno |
| Reglas de cobertura mínima | Mínimo por turno según volumen: ≥1 emergenciólogo, ≥2 enfermeras triaje, ≥1 POCUS |
| Turnos escalonados | Inicio de turnos desfasado para cubrir peaks (11:00-23:00 refuerzo) |
| Pool de refuerzo | Personal de reserva activable en ≤2h para surge |
| Normativa laboral | Ley 19.378 (APS), Código del Trabajo: descanso, jornada máxima, turnos nocturnos |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Ratio médico/consulta-hora | Consultas por hora / Médicos en turno | ≤2.5 pac/méd/hora | ACEP: 2.0-2.5 | ACEP 2023 | Mensual |
| Cobertura turnos críticos | Turnos con dotación completa / Turnos programados × 100 | ≥95 % | — | RRHH | Mensual |
| Horas extra no programadas | Horas extra / Horas totales × 100 | ≤10 % | — | RRHH | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Déficit crónico de emergenciólogos | Formación de especialistas, incentivos retención, telemedicina de apoyo |
| Fatiga por turnos extendidos | Límite jornada, descanso mínimo inter-turno, monitoreo bienestar |

Ref: ACEP Workforce Policy 2023; Código del Trabajo Chile; EUNACOM — requisitos formación emergencia.

### 21.3 Colas en sala de espera/box

Gestión de colas y tiempos de espera dentro del SUH. Estrategias para reducir waiting time y optimizar throughput sin comprometer seguridad.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Límites WIP (Work In Progress) | Máximo pacientes simultáneos por circuito: reanimación (2-3), estándar (según boxes), fast track (según dotación) |
| Médico de triaje | Evaluación médica inicial en triaje para ESI 2-3: solicitar estudios anticipadamente |
| Pull system | Paciente "jala" al siguiente paso cuando hay capacidad, no empuje desde cola |
| Señalización tiempos | Pantalla pública con tiempo espera estimado por nivel de triaje |
| Rondas de espera | Enfermería revisa pacientes en espera cada 30 min (analgesia, re-evaluación, hidratación) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tiempo espera ESI 3 | Mediana minutos triaje → primer contacto médico (ESI 3) | ≤30 min | ACEP: ≤30 min | ACEP 2023 | Mensual |
| LWBS | Pacientes que abandonan sin ser vistos / Total consultas × 100 | ≤3 % | ACEP: ≤2 % | ACEP 2023 | Mensual |
| Ocupación SUH | Pacientes presentes / Capacidad nominal SUH × 100 | ≤100 % | — | EDIS | Tiempo real |
| Throughput médico | Pacientes dados de alta + hospitalizados por hora / Médicos en turno | ≥1.5 pac/méd/hora | — | EDIS | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Espera prolongada sin re-evaluación | Rondas de enfermería, re-triaje protocolizado |
| WIP excedido sin acción | Gatillo automático de surge al exceder 120 % capacidad |

Ref: IHI Optimizing Patient Flow 2003; Lean Healthcare — Toyota Production System; ACEP Crowding Solutions 2023.

### 21.4 Boarding y exit block

Pacientes con decisión de hospitalización que permanecen en SUH por falta de cama disponible (boarding). Principal causa de saturación y deterioro de indicadores de urgencia.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Boarding | Paciente con orden de hospitalización en SUH esperando cama de destino |
| Exit block | Bloqueo de salida: camas hospitalarias ocupadas por pacientes con alta demorada |
| Early discharge rounds | Ronda 08:00 para identificar altas del día, liberar camas antes de peak SUH |
| Camas swing | Camas polivalentes asignables a cualquier servicio según demanda |
| Full capacity protocol | Distribución de pacientes boarding a pasillos de servicios clínicos (no solo SUH) |
| Smoothing quirúrgico | Programación cirugía electiva lunes-viernes para evitar peak egresos lunes |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Boarding time | Mediana horas decisión hospitalización → salida SUH a cama | ≤2h | ACEP: ≤60 min; UK NHS: ≤4h total | ACEP 2023 | Mensual |
| Pacientes boarding >6h | N° pacientes con boarding >6h / Total boarding × 100 | ≤10 % | — | EDIS | Mensual |
| Hora alta efectiva | Mediana hora del día en que paciente deja cama hospitalaria | ≤11:00 | — | HCE | Mensual |
| Ocupación hospitalaria | Camas ocupadas / Camas habilitadas × 100 | 85-90 % | IHI: ≤85 % para flujo óptimo | IHI 2019 | Diario |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Mortalidad aumentada por boarding | Full capacity protocol, escalamiento a dirección, notificación SEREMI |
| Resistencia de servicios a camas swing | Directriz institucional, gobernanza de camas centralizada |

Ref: ACEP Boarding Statement 2023; IHI Whole-System Flow; Innes et al. 2019 (boarding mortality); NHS England Urgent and Emergency Care.

### 21.5 Gatillos y contingencia (surge)

Sistema de niveles de contingencia con gatillos objetivos y acciones predefinidas para manejo de sobrecarga del SUH.

**IF/THEN — Niveles surge:**

| Nivel | Gatillo | Acciones | Responsable |
|-------|---------|----------|-------------|
| IF VERDE (normal) | Ocupación SUH ≤100 %, boarding ≤5 pacientes, LWBS ≤3 % | THEN operación estándar, monitoreo continuo | Jefe turno SUH |
| IF AMARILLO (alerta) | Ocupación 100-120 %, boarding 6-10 pacientes, espera ESI 3 >45 min | THEN activar médico de triaje, abrir boxes adicionales, ronda early discharge, notificar bed manager | Jefe turno SUH + Bed manager |
| IF ROJO (crisis) | Ocupación >120 %, boarding >10 pacientes, LWBS >5 %, espera ESI 3 >60 min | THEN full capacity protocol, redistribuir boarding a servicios, suspender cirugía electiva, convocar pool de refuerzo, notificar dirección | Director de turno + Dirección |
| IF NEGRO (catastrófico) | MCI o colapso sostenido >12h en nivel rojo | THEN activar plan MCI/HICS, desvío de ambulancias a SUH alternativo, solicitar apoyo inter-SS | Dirección + Centro Regulador |

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Tablero surge | Dashboard tiempo real con semáforo automático basado en gatillos |
| Protocolo de desborde | Secuencia de acciones por nivel, checklist ejecutable |
| Comunicación de nivel | Notificación automática a stakeholders según nivel (SMS, email, radio) |
| Revisión post-surge | Debriefing estructurado post-evento para mejora continua |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Horas en nivel rojo | Horas acumuladas en nivel rojo / Horas totales mes × 100 | ≤5 % | — | Dashboard surge | Mensual |
| Tiempo respuesta a gatillo | Minutos entre activación gatillo y primera acción documentada | ≤15 min | — | Registros surge | Mensual |
| Frecuencia surge amarillo | N° activaciones amarillo / mes | Tendencia decreciente | — | Dashboard surge | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Normalización del nivel rojo | Análisis causa raíz mensual, plan de acción institucional |
| Fatiga de alarma | Umbrales calibrados trimestralmente, evitar sobre-gatillos |

Ref: IHI Surge Management; ACEP Crowding Solutions Toolkit 2023; NHS Operational Pressures Escalation Levels (OPEL).

## 22. Protocolos críticos y rutas tiempo-dependientes

### 22.1 Código ACV (IVT/Trombectomía)

Protocolo de activación y manejo del accidente cerebrovascular isquémico agudo. Ventana IVT ≤4.5h, trombectomía mecánica ≤24h (seleccionados). Cada minuto sin reperfusión = 1.9 millones de neuronas perdidas.

**Hitos tiempo-dependientes:**

| Hito | Meta | Benchmark | Responsable |
|------|------|-----------|-------------|
| Door-to-CT | ≤20 min | AHA/ASA 2024: ≤25 min | Enfermería triaje + radiólogo |
| Door-to-needle (IVT) | ≤60 min | AHA 2024: ≤45 min | Neurólogo/médico SUH |
| Door-to-groin (trombectomía) | ≤90 min | AHA 2024: ≤90 min | Neurointervencionista |
| Door-in-door-out (centro primario→comprensivo) | ≤45 min | AHA 2024 | Equipo SUH |
| NIHSS al ingreso | Documentado en ≤10 min | AHA 2024 | Médico SUH/neurólogo |
| Glicemia capilar | ≤5 min desde ingreso | AHA 2024 | Enfermería triaje |

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Activación código ACV | ≥1 criterio Cincinnati + hora inicio conocida → activación |
| Centro ACV primario | IVT disponible 24/7, TC sin contraste, laboratorio urgente |
| Centro ACV comprensivo | IVT + trombectomía mecánica 24/7, neuro-UCI, neurocirugía |
| Telemedicina ACV | Tele-stroke para centros sin neurólogo presencial: evaluación remota NIHSS, decisión IVT |
| Kit ACV | Alteplasa/tenecteplasa pre-preparada, protocolo dosis, checklist contraindicaciones |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tasa IVT | Pacientes con IVT / ACV isquémico elegible × 100 | ≥25 % | AHA: ≥25 % | AHA 2024 | Trimestral |
| Door-to-needle ≤60 min | % IVT con DTN ≤60 min / Total IVT × 100 | ≥75 % | AHA: ≥75 % | AHA 2024 | Trimestral |
| Mortalidad intrahospitalaria ACV | Fallecidos / Total ACV ingresados × 100 | ≤15 % | — | GRD/HCE | Trimestral |
| mRS 0-2 a 90 días | Independencia funcional a 3 meses / Total ACV seguidos × 100 | ≥40 % | Ensayos trombectomía: 46 % | MR CLEAN 2015 | Semestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Hora de inicio desconocida (wake-up stroke) | Protocolo RM-DWI/FLAIR mismatch, selección por imagen avanzada |
| Demora por consultas internas | Protocolo de activación paralela (lab + imagen + neurólogo simultáneos) |

Ref: AHA/ASA Guidelines Acute Ischemic Stroke 2024; ESO Guidelines 2022; MINSAL GES ACV.

### 22.2 Código IAM (STEMI/NSTEMI)

Protocolo de activación y manejo del síndrome coronario agudo. STEMI: reperfusión urgente (ICP primaria o fibrinólisis). NSTEMI: estratificación de riesgo y cateterismo según timing.

**Hitos tiempo-dependientes:**

| Hito | Meta | Benchmark | Responsable |
|------|------|-----------|-------------|
| Door-to-ECG | ≤10 min | AHA/ACC 2023: ≤10 min | Enfermería triaje |
| FMC-to-balloon (ICP primaria) | ≤90 min | ESC 2023: ≤60 min | Hemodinamia |
| Door-to-needle (fibrinólisis) | ≤30 min | AHA 2023: ≤30 min | Médico SUH |
| Door-to-balloon (ICP) | ≤60 min | AHA/ACC 2023 | Hemodinamia |
| ECG seriado si primer ECG no diagnóstico | Cada 15-30 min | AHA 2023 | Enfermería SUH |
| Troponina alta sensibilidad | Resultado ≤60 min (protocolo 0/1h o 0/3h) | ESC 2023 | Laboratorio |

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Activación código IAM | Elevación ST en ECG (prehospitalario o SUH) → activación hemodinamia |
| Red STEMI | Hospitales con hemodinamia 24/7 como hubs, SUH periféricos como spokes con fibrinólisis |
| Estrategia farmacoinvasiva | Fibrinólisis en SUH sin ICP + traslado a ICP en 2-24h |
| NSTEMI risk stratification | GRACE score: alto riesgo → cateterismo ≤24h; muy alto riesgo → ≤2h |
| Doble antiagregación | Aspirina + inhibidor P2Y12 según protocolo local |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| FMC-to-balloon ≤90 min | % STEMI con FMC-balloon ≤90 min / Total STEMI reperfundidos × 100 | ≥75 % | AHA: ≥75 % | AHA 2023 | Trimestral |
| Tasa reperfusión STEMI | STEMI reperfundidos (ICP o fibrinólisis) / Total STEMI × 100 | ≥90 % | ESC: ≥90 % | ESC 2023 | Trimestral |
| Mortalidad intrahospitalaria STEMI | Fallecidos / Total STEMI × 100 | ≤7 % | ESC registros: 4-6 % | ESC 2023 | Trimestral |
| Door-to-ECG ≤10 min | % dolor torácico con ECG ≤10 min / Total dolor torácico × 100 | ≥90 % | AHA: ≥90 % | AHA 2023 | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Hemodinamia no disponible 24/7 | Estrategia farmacoinvasiva + red de traslado, rotación equipos |
| STEMI no reconocido (ECG atípico) | ECG seriado, segunda lectura remota, umbral bajo activación |

Ref: AHA/ACC STEMI Guidelines 2023; ESC STEMI/NSTEMI Guidelines 2023; MINSAL GES IAM.

### 22.3 Sepsis (bundle 1h/3h)

Protocolo de detección precoz y manejo protocolizado de sepsis y shock séptico. Bundle hora-1 como estándar de atención. Cada hora de retraso en antibióticos aumenta mortalidad en 4-7 %.

**Hitos tiempo-dependientes:**

| Hito | Meta | Benchmark | Responsable |
|------|------|-----------|-------------|
| Lactato sérico | ≤1h desde sospecha | SSC 2021 | Laboratorio/enfermería |
| Hemocultivos (≥2 sets) | Antes de antibiótico | SSC 2021 | Enfermería SUH |
| Antibiótico empírico | ≤1h desde sospecha de sepsis | SSC 2021: ≤1h | Médico SUH |
| Fluidos cristaloides (30 ml/kg) | ≤3h si hipotensión o lactato ≥4 | SSC 2021 | Médico/enfermería SUH |
| Re-evaluación lactato | ≤6h si lactato inicial elevado | SSC 2021 | Médico SUH |
| Vasopresores si PAM <65 post-fluidos | Inicio durante o post-reanimación con fluidos | SSC 2021 | Médico SUH/UCI |

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Screening sepsis | qSOFA, NEWS, SIRS modificado — tamizaje en triaje y re-evaluación |
| Bundle hora-1 SSC | Lactato + hemocultivos + antibiótico + fluidos (si indicados) + vasopresores (si indicados) |
| Kit sepsis | Antibióticos empíricos pre-seleccionados, fluidos, sets hemocultivo, POC lactato |
| Alerta electrónica | Gatillo automático en EDIS/HCE al cumplir criterios sepsis (NEWS ≥5, qSOFA ≥2) |
| Escalamiento a UCI | Criterios: vasopresores, ventilación mecánica, falla multiorgánica |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cumplimiento bundle hora-1 | Pacientes con bundle hora-1 completo / Total sepsis × 100 | ≥80 % | SSC: meta global | SSC 2021 | Mensual |
| Antibiótico ≤1h | Sepsis con antibiótico ≤1h / Total sepsis × 100 | ≥90 % | SSC 2021 | SSC 2021 | Mensual |
| Mortalidad sepsis intrahospitalaria | Fallecidos sepsis / Total sepsis × 100 | ≤20 % | SSC registros: 15-25 % | SSC 2021 | Trimestral |
| Lactato POC ≤1h | Lactato obtenido ≤1h / Total sepsis × 100 | ≥90 % | — | EDIS/LIS | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Sepsis no reconocida en adulto mayor (presentación atípica) | Tamizaje NEWS en todos ≥65 años, umbral bajo sospecha |
| Resistencia antibiótica por empírico inadecuado | Antibiograma local actualizado, de-escalación a 48-72h |

Ref: Surviving Sepsis Campaign Guidelines 2021; SSC Bundle Update 2018; MINSAL GES Sepsis.

### 22.4 Trauma mayor (ATLS)

Protocolo de activación y manejo del paciente politraumatizado. Abordaje ATLS estandarizado con activación de equipo trauma. Triada letal: hipotermia, acidosis, coagulopatía.

**Hitos tiempo-dependientes:**

| Hito | Meta | Benchmark | Responsable |
|------|------|-----------|-------------|
| Activación equipo trauma | ≤5 min desde pre-notificación | ACS-COT 2022 | Enfermería triaje/líder trauma |
| Evaluación primaria (ABCDE) | ≤10 min desde ingreso | ATLS 10th ed. | Líder trauma |
| FAST/eFAST | ≤10 min desde ingreso | ATLS 10th ed. | Emergenciólogo/cirujano |
| TC body (pan-scan) | ≤30 min si estable hemodinámicamente | NICE Trauma 2023 | Radiólogo |
| Pabellón (cirugía de control de daños) | ≤60 min si inestable post-reanimación | ACS-COT 2022 | Cirujano de trauma |
| Transfusión masiva | Activación ≤15 min si criterios cumplidos | ACS-COT 2022 | Banco de sangre + equipo trauma |

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Equipo trauma | Cirujano, emergenciólogo, anestesista, enfermería, paramédico — roles preestablecidos |
| Protocolo transfusión masiva | 1:1:1 (GR:PFC:plaquetas), ácido tranexámico ≤3h, fibrinógeno |
| Cirugía control de daños | Hemostasia, descontaminación, cierre temporal — UCI para estabilización |
| Prevención triada letal | Calentamiento activo, reanimación hemostática, monitoreo TEG/ROTEM |
| Nivel activación trauma | Nivel 1 (equipo completo) vs. nivel 2 (parcial) según mecanismo y criterios clínicos |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Mortalidad trauma severo (ISS ≥16) | Fallecidos / Total trauma ISS ≥16 × 100 | ≤20 % | TARN UK: 15-20 % | TARN 2023 | Trimestral |
| Tiempo a pabellón (inestable) | Mediana minutos ingreso → inicio cirugía (inestable) | ≤60 min | ACS-COT 2022 | Registros quirúrgicos | Trimestral |
| Tasa sobre-activación trauma | Activaciones nivel 1 sin criterio / Total activaciones nivel 1 × 100 | ≤30 % | ACS-COT: ≤30 % | ACS-COT 2022 | Trimestral |
| Adherencia ATLS | Evaluación primaria documentada completa / Total trauma × 100 | ≥95 % | — | Auditoría clínica | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Demora pabellón por disponibilidad | Pabellón trauma dedicado 24/7 o prioridad absoluta |
| Coagulopatía no detectada precozmente | TEG/ROTEM en reanimación, protocolo transfusión masiva protocolizado |

Ref: ATLS 10th ed. (ACS); ACS-COT Resources for Optimal Care 2022; NICE Major Trauma NG39; CRASH-2 Trial (ácido tranexámico).

### 22.5 Paro cardiorrespiratorio y post-ROSC

Protocolo de reanimación cardiopulmonar avanzada y manejo post-retorno de circulación espontánea (ROSC). Cadena de supervivencia intra y extrahospitalaria.

**Hitos tiempo-dependientes:**

| Hito | Meta | Benchmark | Responsable |
|------|------|-----------|-------------|
| Inicio RCP | ≤1 min (intrahospitalario), inmediato (prehospitalario) | ILCOR 2023 | Primer respondedor |
| Desfibrilación (ritmo desfibrilable) | ≤3 min desde detección | AHA 2023: ≤3 min | Equipo RCP/DEA |
| Adrenalina (ritmo no desfibrilable) | ≤3 min desde inicio RCP | AHA 2023 | Enfermería/médico |
| Adrenalina (ritmo desfibrilable) | Después de 2° descarga | AHA 2023 | Enfermería/médico |
| Manejo avanzado vía aérea | Cuando indicado, sin interrumpir compresiones | ILCOR 2023 | Médico/enfermería |
| Temperatura objetivo (TTM) post-ROSC | 32-36 °C por ≥24h, inicio ≤6h | ILCOR 2023 | UCI |

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Cadena supervivencia | Reconocimiento → Activación → RCP precoz → Desfibrilación → Soporte avanzado → Post-paro |
| ACLS algorithms | FV/TV sin pulso → Descarga + RCP. AESP/Asistolia → RCP + causas reversibles (5H/5T) |
| Carro de paro | Estandarizado, verificación diaria, ubicación señalizada |
| Debriefing post-paro | Revisión estructurada ≤24h post-evento: calidad RCP, tiempos, resultados |
| Neuropronóstico | ≥72h post-ROSC, multimodal (clínico + EEG + biomarcadores + imagen) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Sobrevida a alta paro intrahospitalario | Sobrevivientes / Total paro intrahospitalario × 100 | ≥25 % | GWTG-R: 25-30 % | AHA GWTG 2023 | Trimestral |
| ROSC sostenido | ROSC >20 min / Total RCP × 100 | ≥50 % | — | Registros paro | Trimestral |
| Fracción compresiones torácicas | Tiempo con compresiones / Tiempo total RCP × 100 | ≥80 % | AHA: ≥80 % | Desfibrilador (data download) | Por evento |
| Debriefing post-paro | Debriefings realizados / Total paros × 100 | ≥90 % | — | Registros calidad | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| RCP de mala calidad (interrupciones, profundidad insuficiente) | Feedback en tiempo real del desfibrilador, simulación trimestral |
| TTM no iniciado por falta de protocolo | Kit TTM disponible, protocolo escrito, capacitación UCI |

Ref: AHA/ILCOR Guidelines CPR and ECC 2023; ERC Guidelines 2021; TTM2 Trial 2021; MINSAL NT RCP.

### 22.6 Tóxicos/antídotos y quemados

Protocolos de manejo de intoxicaciones agudas y quemaduras graves. Acceso oportuno a antídotos específicos y derivación a centro de referencia cuando corresponde.

**Hitos tiempo-dependientes:**

| Hito | Meta | Benchmark | Responsable |
|------|------|-----------|-------------|
| Identificación del tóxico | ≤30 min desde ingreso | — | Médico SUH |
| Antídoto específico administrado | ≤30 min si indicado y disponible | — | Médico SUH + farmacia |
| Descontaminación (si indicada) | ≤1h desde exposición (carbón activado, lavado cutáneo) | — | Equipo SUH |
| Consulta centro toxicológico (CITUC) | ≤15 min si tóxico no identificado o antídoto no disponible | — | Médico SUH |
| Evaluación quemadura (SCT, profundidad) | ≤30 min desde ingreso | ABA 2023 | Médico SUH |
| Derivación centro quemados | ≤2h si criterios ABA de derivación | ABA 2023 | Médico SUH + Centro Regulador |

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Stock antídotos SUH | N-acetilcisteína, naloxona, flumazenil, atropina, pralidoxima, anticuerpos anti-digoxina, glucagón, hidroxocobalamina |
| CITUC | Centro de Información Toxicológica UC — consulta telefónica 24/7 |
| Criterios derivación quemados | ≥20 % SCT adulto, ≥10 % SCT niño, quemadura vía aérea, eléctrica, química, circunferencial |
| Resucitación quemados | Parkland (4 ml/kg/% SCT), monitoreo diuresis, analgesia precoz |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Antídoto ≤30 min | Pacientes con antídoto ≤30 min / Total con indicación × 100 | ≥90 % | — | Registros farmacia/SUH | Trimestral |
| Disponibilidad stock antídotos | Antídotos con stock vigente / Total antídotos lista × 100 | 100 % | — | Farmacia | Mensual |
| Derivación quemados en plazo | Derivaciones ≤2h / Total derivaciones quemados × 100 | ≥90 % | — | Centro Regulador | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Antídoto no disponible en SUH | Stock mínimo protocolizado, convenio inter-hospitalario, kit antídotos regionales |
| Tóxico no identificado | Consulta CITUC, toxicología POC, muestra conservada para análisis diferido |

Ref: ABA Burn Center Referral Criteria 2023; AACT/EAPCCT Guidelines; CITUC protocolos; MINSAL NT Quemados.

### 22.7 Emergencias obstétricas y pediátricas

Protocolos de manejo de emergencias obstétricas y pediátricas en SUH general. Estabilización inicial y derivación oportuna a unidad especializada.

**Hitos tiempo-dependientes:**

| Hito | Meta | Benchmark | Responsable |
|------|------|-----------|-------------|
| Cesárea perimortem | ≤5 min desde paro materno | AHA 2023 | Obstetra/cirujano disponible |
| Sulfato de magnesio (eclampsia) | ≤15 min desde diagnóstico | ACOG 2023 | Médico SUH/obstetra |
| Transfusión masiva obstétrica | Activación ≤15 min si hemorragia post-parto refractaria | ACOG 2023 | Banco sangre + obstetra |
| Evaluación triángulo pediátrico (TEP) | ≤2 min desde ingreso | APLS/PALS | Enfermería triaje |
| Dosis por peso (Broselow) | Verificación ≤5 min si fármacos de emergencia | PALS 2023 | Enfermería/médico |
| Activación equipo pediátrico | ≤10 min desde triaje ESI 1-2 pediátrico | — | Jefe turno SUH |

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Carro obstétrico de emergencia | Sulfato magnesio, oxitocina, misoprostol, kit parto precipitado, balón Bakri |
| Carro pediátrico (Broselow) | Fármacos y equipos por peso/color, cinta de Broselow |
| Protocolo hemorragia obstétrica | Masaje uterino, uterotónicos, balón intrauterino, protocolo transfusión masiva |
| Morbilidad materna severa (near-miss) | Criterios OMS para detección y registro |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Near-miss materno | Casos near-miss / Total partos × 1.000 | ≤10 ‰ | OMS: variable | OMS 2023 | Trimestral |
| Mortalidad pediátrica en SUH | Fallecidos ≤15 años en SUH / Total consultas pediátricas SUH × 10.000 | ≤1 / 10.000 | — | Registros SUH | Semestral |
| Disponibilidad carro Broselow | Verificaciones completas / Verificaciones programadas × 100 | 100 % | — | Enfermería | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Error dosificación pediátrica | Cinta Broselow obligatoria, doble verificación, sistema prescripción electrónico |
| SUH sin obstetra de guardia | Protocolo estabilización + traslado urgente, tele-obstetricia |

Ref: ACOG Practice Bulletins 2023; AHA Maternal Cardiac Arrest 2023; PALS Provider Manual 2023; OMS Near-miss Criteria.

### 22.8 Crisis de salud mental en urgencias

Para manejo completo, ver [Crisis y urgencias psiquiátricas](urn:pro:kb:gestion-redes-salud-mental) cap 30. Esta sección cubre el protocolo específico del SUH.

**Hitos tiempo-dependientes:**

| Hito | Meta | Benchmark | Responsable |
|------|------|-----------|-------------|
| Evaluación riesgo suicida (C-SSRS) | ≤30 min desde triaje | Joint Commission NPSG 2023 | Médico/enfermería SUH |
| Evaluación psiquiátrica formal | ≤4h desde ingreso | NICE CG136 | Psiquiatra de guardia |
| Contención proporcional (si necesaria) | Documentada, re-evaluación cada 15-30 min | Ley 21.331 | Enfermería + médico |
| Seguridad del entorno | Evaluación inmediata al ingreso (ligaduras, objetos cortantes) | Joint Commission 2023 | Enfermería SUH |

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Sala de evaluación psiquiátrica | Espacio seguro, sin objetos de riesgo, privacidad, acompañamiento |
| Protocolo contención | Verbal → farmacológica → mecánica (último recurso, proporcional, documentada) |
| Criterios hospitalización involuntaria | Ley 21.331: riesgo vital inminente, evaluación por dos médicos, autorización judicial ≤72h |
| Enlace con red SM | Derivación a COSAM/hospital psiquiátrico, seguimiento ≤48h post-alta SUH |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tiempo a evaluación psiquiátrica | Mediana horas ingreso → evaluación psiquiátrica formal | ≤4h | NICE: ≤4h | NICE 2023 | Mensual |
| Contención mecánica | Episodios contención mecánica / Total consultas SM SUH × 100 | ≤5 % | — | Registros enfermería | Mensual |
| Seguimiento post-alta SM | Pacientes con contacto SM ≤48h post-alta SUH / Total altas SM × 100 | ≥80 % | NICE: ≥80 % | Registros red SM | Mensual |
| Tamizaje riesgo suicida en SUH | C-SSRS aplicado / Total consultas SM SUH × 100 | 100 % | Joint Commission 2023 | EDIS | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Autolesión en SUH | Ambiente seguro, vigilancia continua, protocolo 1:1 si alto riesgo |
| Boarding psiquiátrico prolongado | Enlace directo con red SM, camas psiquiátricas de emergencia, tele-psiquiatría |

Ref: Ley 21.331 (Derechos SM Chile); NICE CG136 Self-harm; Joint Commission NPSG 15 (Suicide Risk); ACEP Mental Health Policy 2023.

## 23. Calidad, seguridad y experiencia en urgencias

Marco base: ver [Calidad, seguridad y gestión de riesgos](urn:pro:kb:gestion-redes-general) cap 10. Esta sección agrega los deltas específicos de urgencias.

### 23.1 Analgesia oportuna

Manejo del dolor como indicador de calidad en urgencias. Evaluación, tratamiento y re-evaluación protocolizados desde triaje.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Evaluación dolor en triaje | EVA/NRS documentada al ingreso, re-evaluación post-analgesia |
| Protocolo analgesia por enfermería | Administración de analgesia por enfermería según protocolo antes de evaluación médica (ESI 2-5 con dolor ≥4) |
| Analgesia multimodal | Escalonamiento: paracetamol → AINE → opioide débil → opioide fuerte, bloqueos regionales |
| Ketamina subdisociativa | Alternativa a opioides para dolor severo, protocolo SUH |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Door-to-analgesia | Mediana minutos ingreso → primera dosis analgésica (dolor ≥7) | ≤30 min | ACEP: ≤30 min | ACEP 2023 | Mensual |
| Evaluación dolor en triaje | % pacientes con EVA documentada en triaje / Total consultas × 100 | ≥90 % | — | EDIS | Mensual |
| Re-evaluación dolor post-analgesia | % con re-evaluación ≤60 min post-dosis / Total analgesia administrada × 100 | ≥80 % | — | EDIS | Mensual |
| Satisfacción manejo dolor | PREMs ítem dolor (escala 1-5) | ≥4.0 | — | Encuesta paciente | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Oligoanalgesia (tratamiento insuficiente del dolor) | Protocolo nurse-initiated, auditoría tiempos, formación continua |
| Uso inadecuado de opioides | Protocolo multimodal, monitoreo sedación, naloxona disponible |

Ref: ACEP Clinical Policy Pain Management 2023; NICE CG140 Acute Pain; Ley 20.584 (derecho al manejo del dolor).

### 23.2 Medicación segura en SUH

Prácticas de seguridad en prescripción, preparación y administración de medicamentos en el entorno de alta presión del SUH.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Tall-man lettering | Diferenciación visual de medicamentos look-alike/sound-alike (ej. DOPamina vs. DOBUtamina) |
| Segregación física | Almacenamiento separado de medicamentos de alto riesgo (KCl, insulina, heparina, opioides) |
| Doble chequeo | Verificación por segundo operador para medicamentos de alto riesgo y dosis pediátricas |
| Conciliación medicamentosa | Registro de medicación habitual al ingreso SUH, verificación interacciones |
| Prescripción electrónica | CPOE con alertas de dosis, alergias, interacciones — reduce errores vs. prescripción manual |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Errores de medicación en SUH | Errores reportados / 1.000 administraciones | ≤2.0 | — | Sistema reporte EA | Mensual |
| Doble chequeo alto riesgo | % medicamentos alto riesgo con doble chequeo / Total alto riesgo × 100 | 100 % | — | Auditoría farmacia | Mensual |
| Conciliación al ingreso SUH | % pacientes con conciliación medicamentosa / Total ingresos × 100 | ≥80 % | Joint Commission: 100 % | Joint Commission 2023 | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Presión temporal que omite verificación | Cultura de seguridad, doble chequeo como norma no negociable |
| Falta identificación alergias | Pulsera de alergias, alerta en EDIS, verificación verbal |

Ref: Joint Commission IPSG.3 (Medication Safety); ISMP High-Alert Medications; NICE Medicines Optimisation; Política Nacional Seguridad Paciente MINSAL 2022.

### 23.3 Imagen segura y caídas

Protección contra radiación innecesaria y prevención de caídas en el entorno del SUH.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Criterios de imagen apropiada | Reglas de decisión clínica: Ottawa (tobillo/rodilla), Canadian C-Spine, Nexus, Wells |
| Protección radiológica | Principio ALARA, protección gonadal en pediátricos, registro dosis acumulada |
| Prevención de caídas SUH | Evaluación riesgo caídas en triaje (adulto mayor, sedación, alteración conciencia) |
| Camilla con barandas | Barandas levantadas en pacientes con riesgo, freno activado |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Caídas en SUH | Caídas / 1.000 visitas SUH | ≤1.0 | — | Reporte EA | Mensual |
| Adherencia reglas de decisión clínica | % casos con regla aplicada (Ottawa, C-Spine) / Total elegibles × 100 | ≥80 % | — | Auditoría clínica | Trimestral |
| Imagen redundante | Estudios imagen repetidos ≤48h / Total estudios × 100 | ≤5 % | — | RIS | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Sobreuso imagen por medicina defensiva | Reglas de decisión clínica, retroalimentación de adherencia |
| Caída con lesión en paciente sedado | Protocolo vigilancia post-sedación, acompañamiento 1:1 |

Ref: ACR Appropriateness Criteria; Choosing Wisely — ACEP; Joint Commission NPSG (Fall Prevention).

### 23.4 Alta segura desde SUH (teach-back)

Proceso estructurado de alta que garantiza comprensión del paciente sobre diagnóstico, tratamiento, signos de alarma y plan de seguimiento.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Instrucciones de alta escritas | Lenguaje claro, nivel lectura ≤6° básico, multilingüe si aplica |
| Teach-back | Paciente verbaliza instrucciones en sus palabras — verifica comprensión |
| Signos de alarma | Lista explícita de motivos de reconsulta urgente por patología |
| Seguimiento programado | Hora de control APS/especialista ≤48-72h para ESI 2-3 dados de alta |
| Reconsulta 72h | Monitoreo de pacientes que reconsultan ≤72h como indicador de alta segura |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Teach-back documentado | % altas con teach-back registrado / Total altas × 100 | ≥80 % | — | EDIS | Mensual |
| Reconsulta no programada ≤72h | Reconsultas ≤72h / Total altas SUH × 100 | ≤5 % | — | EDIS | Mensual |
| Instrucciones entregadas | % altas con instrucciones escritas / Total altas × 100 | 100 % | — | EDIS | Mensual |
| Seguimiento ambulatorio confirmado | Altas con hora de control programada / Total altas ESI 2-3 × 100 | ≥70 % | — | EDIS + APS | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Barrera idiomática o baja alfabetización | Material pictográfico, facilitador intercultural, familiar acompañante |
| Alta en horario nocturno sin control accesible | Teléfono de consulta 24h, instrucciones reforzadas |

Ref: AHRQ IDEAL Discharge Planning; ACEP Transitions of Care Policy 2023; Ley 20.584 (derecho a información).

### 23.5 Experiencia del paciente en urgencias

Gestión de la experiencia del paciente en SUH con foco en comunicación, tiempos de espera percibidos y acompañamiento.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Host/flow manager | Profesional dedicado a comunicación con pacientes y familiares en sala de espera: explica tiempos, proceso, actualizaciones |
| PREMs SUH | Encuesta experiencia específica urgencias: comunicación, dolor, espera, trato, información al alta |
| Gestión de reclamos SUH | Canal reclamo accesible, respuesta ≤15 días, análisis causal |
| Acompañamiento | Ley 20.584: derecho a acompañante significativo, extensivo a adulto mayor y niños |
| Comunicación proactiva | Actualización a familiares cada 60 min si paciente en evaluación |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| PREMs SUH score global | Puntuación agregada encuesta experiencia / Máximo posible × 100 | ≥75 % | NHS: 75 % | NHS Urgent Care Survey 2023 | Trimestral |
| Reclamos SUH | Reclamos formales / 1.000 consultas SUH | ≤3.0 | — | OIRS | Mensual |
| Satisfacción comunicación | PREMs ítem comunicación (escala 1-5) | ≥4.0 | — | Encuesta paciente | Trimestral |
| Tiempo espera percibido | PREMs ítem espera (escala 1-5, 5 = aceptable) | ≥3.5 | — | Encuesta paciente | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Encuesta con baja tasa de respuesta | Multicanal (digital + presencial), incentivo no monetario |
| Foco en satisfacción sobre seguridad | PREMs como complemento, no sustituto de indicadores clínicos |

Ref: NHS Urgent and Emergency Care Survey 2023; Press Ganey ED Benchmarks; Ley 20.584; ACEP Patient Experience Policy.

## 24. Tecnología y datos para urgencias

Marco base: ver [Salud digital e interoperabilidad](urn:pro:kb:gestion-redes-general) cap 11. Esta sección agrega los deltas específicos de urgencias.

### 24.1 EDIS y triaje electrónico

Sistema de información específico del SUH (Emergency Department Information System) que gestiona flujo de pacientes, triaje, órdenes, resultados y métricas en tiempo real.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| EDIS core | Registro ingreso, triaje, tracking paciente, órdenes, resultados, alta — timeline completo |
| Triaje electrónico | Soporte decisional algorítmico (ESI/MTS), timestamps automáticos, discriminadores |
| Integración HCE | Bidireccional: EDIS → HCE (episodio urgencia) y HCE → EDIS (antecedentes, alergias, medicación) |
| Tablero tiempo real | Visualización de todos los pacientes por estado, tiempo en SUH, pendientes, alertas |
| Alertas clínicas | Gatillos automáticos: sepsis (NEWS ≥5), deterioro (MEWS), tiempo excedido por triaje |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Adopción EDIS | % consultas registradas en EDIS / Total consultas SUH × 100 | 100 % | — | EDIS | Mensual |
| Disponibilidad EDIS | Uptime EDIS / Horas totales × 100 | ≥99.5 % | — | TI | Mensual |
| Timestamp automático triaje | % triajes con timestamp automático / Total triajes × 100 | ≥98 % | — | EDIS | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Caída EDIS (single point of failure) | Contingencia con formulario papel + ingreso retrospectivo, infraestructura redundante |
| Alert fatigue | Priorización de alertas, revisión periódica de umbrales, supresión de alertas de bajo valor |

Ref: ACEP Health IT Policy; HIMSS EDIS Selection Guide; NT HCE MINSAL.

### 24.2 RTLS y dashboards RT

Sistemas de localización en tiempo real (Real-Time Location Systems) y dashboards para gestión visual del flujo SUH.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| RTLS pacientes | Tags en pulsera identificatoria, tracking por zona (sala espera, box, imagenología, UOCS) |
| RTLS equipos | Localización de equipos compartidos (ecógrafo, bombas infusión, monitores portátiles) |
| Dashboard flujo | Mapa visual SUH en tiempo real: ocupación por zona, tiempos acumulados, alertas |
| Dashboard surge | Semáforo automático verde/amarillo/rojo/negro basado en métricas de flujo |
| Reporting automatizado | Generación automática de indicadores mensuales desde datos RTLS + EDIS |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Precisión RTLS | Localización correcta / Total lecturas × 100 | ≥95 % | — | RTLS | Mensual |
| Uso dashboard por jefatura | Accesos dashboard / Turnos × 100 | ≥90 % | — | Log sistema | Mensual |
| Reducción búsqueda equipos | Tiempo promedio localización equipo post-RTLS vs. pre-RTLS | Reducción ≥50 % | — | Estudio pre-post | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Costo implementación alto | ROI documentado: reducción tiempos búsqueda, mejora flujo, reducción LWBS |
| Resistencia del personal (percepción de vigilancia) | Comunicación transparente: foco en flujo y seguridad, no control individual |

Ref: RTLS in Healthcare (HIMSS); IHI Flow Improvement; ACEP Technology Policy.

### 24.3 Tele-urgencias (apoyo remoto SAR/APS)

Soporte remoto especializado a SAPU/SAR y puntos de urgencia rurales mediante teleconsulta sincrónica con emergenciólogo o especialista.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Teleconsulta sincrónica | Videoconsulta SAPU/SAR → emergenciólogo SUH para apoyo decisional |
| Tele-triaje | Evaluación remota para definir necesidad de traslado vs. resolución local |
| Tele-procedimiento | Guía remota para procedimientos (intubación, drenaje, cardioversión) |
| Tele-ECG desde APS | Transmisión ECG 12 derivaciones desde SAPU/SAR a cardiólogo |
| Plataforma integrada | Videoconferencia + compartir pantalla (imagen, laboratorio) + registro en HCE |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Teleconsultas urgencia realizadas | N° teleconsultas / mes | Tendencia creciente | — | Plataforma telemedicina | Mensual |
| Traslados evitados por teleconsulta | Pacientes resueltos localmente post-teleconsulta / Total teleconsultas × 100 | ≥40 % | — | Registros telemedicina | Trimestral |
| Satisfacción equipo remoto | Encuesta satisfacción profesional SAPU/SAR con soporte | ≥80 % | — | Encuesta interna | Semestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Conectividad insuficiente en zona rural | Conexión satelital de respaldo, modo store-and-forward |
| Responsabilidad legal difusa | Protocolo claro de responsabilidades, registro de teleconsulta en HCE |

Ref: NT Telemedicina MINSAL 2022; OMS Telemedicine Guidelines; ACEP Telemedicine Policy 2023.

### 24.4 IA para clasificación/predicción

Aplicaciones de inteligencia artificial en urgencias para apoyo a triaje, predicción de deterioro y optimización de flujo.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| IA triaje | Modelos ML como soporte decisional al enfermero de triaje (no reemplazo) |
| Predicción deterioro | NEWS/MEWS automatizado + modelos predictivos de deterioro a 4-12h |
| Predicción demanda | ML para forecast de afluencia horaria (complementa modelos estadísticos) |
| NLP en triaje | Procesamiento de lenguaje natural para texto libre de triaje → códigos estructurados |
| Interpretación imagen IA | Soporte radiológico IA para fracturas, hemorragia intracraneal, neumotórax |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Sensibilidad IA deterioro | VP / (VP + FN) para predicción deterioro clínico | ≥85 % | — | Validación modelo | Semestral |
| Especificidad IA triaje | VN / (VN + FP) | ≥80 % | — | Validación modelo | Semestral |
| Aceptación clínica | % recomendaciones IA aceptadas por clínico / Total recomendaciones × 100 | ≥70 % | — | Registros EDIS | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Sesgo algorítmico (edad, género, etnia) | Validación con datos locales, auditoría de equidad, dataset representativo |
| Sobreconfianza en IA (automation bias) | IA como soporte, decisión final siempre del clínico, formación en limitaciones |

Ref: FDA AI/ML Medical Devices Framework; WHO Ethics & Governance of AI for Health 2021; ACEP AI Policy 2023.

### 24.5 Seguridad y continuidad TI 24/7

Garantía de disponibilidad y seguridad de sistemas de información críticos para operación continua del SUH.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Redundancia infraestructura | Servidores espejo, UPS, generador respaldo, conectividad dual |
| RTO/RPO SUH | RTO ≤15 min (restauración servicio), RPO ≤5 min (pérdida máxima datos) |
| Soporte TI 24/7 | Guardia TI con respuesta ≤15 min para sistemas críticos SUH |
| Contingencia sin sistema | Formularios papel, protocolos manuales, re-ingreso datos post-restauración |
| Ciberseguridad | Segmentación red SUH, antimalware, parches, auditoría acceso |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Uptime sistemas críticos SUH | Horas operativas / Horas totales × 100 | ≥99.9 % | — | TI | Mensual |
| Incidentes TI críticos SUH | N° incidentes con impacto en atención / mes | 0 | — | Mesa ayuda TI | Mensual |
| Tiempo restauración (RTO real) | Mediana minutos desde falla → restauración | ≤15 min | — | TI | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Ransomware con impacto en SUH | Backup offline, segmentación de red, plan DRP específico SUH |
| Falla eléctrica prolongada | UPS + generador + prueba mensual, protocolo operación manual |

Ref: ISO 27001:2022; ECRI Top 10 Health Technology Hazards; HIPAA Security Rule; NT HCE MINSAL.

## 25. Desastres y MCI

### 25.1 HICS para urgencias

Hospital Incident Command System adaptado al SUH. Define roles, cadena de mando y activación escalonada ante incidentes con múltiples víctimas o desastres.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Comandante de incidente (IC) | Director de turno o jefe SUH; autoridad máxima durante MCI |
| Oficial de operaciones | Coordina áreas clínicas: triaje, tratamiento (rojo/amarillo/verde), transporte |
| Oficial de logística | Insumos, equipos, alimentación, comunicaciones, refuerzo personal |
| Oficial de planificación | Registro pacientes, seguimiento recursos, proyección |
| Oficial de enlace | Comunicación con bomberos, policía, ONEMI/SENAPRED, medios, familiares |
| Niveles de activación | Nivel I (parcial): ≤10 víctimas; Nivel II (total): 11-50; Nivel III (regional): >50 o CBRNE |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Simulacros MCI realizados | Simulacros ejecutados / Simulacros programados × 100 | ≥2/año | Joint Commission: ≥2/año | Joint Commission 2023 | Anual |
| Tiempo activación HICS | Minutos desde notificación MCI → HICS operativo | ≤15 min | — | Registros ejercicios | Por ejercicio |
| Personal que conoce su rol HICS | % personal SUH con rol asignado y capacitado / Total personal SUH × 100 | ≥90 % | — | RRHH | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Plan desactualizado | Revisión anual + post-ejercicio, incorporación lecciones aprendidas |
| Rotación de personal sin capacitación | Inducción HICS obligatoria para todo personal nuevo SUH |

Ref: HICS 2014 (CHA); Joint Commission Environment of Care Standards; SENAPRED protocolos; DS 58/2008 MINSAL.

### 25.2 Triage START/JumpSTART/CBRNE

Sistemas de triaje masivo para asignación rápida de prioridad en escena con múltiples víctimas. Algoritmos simplificados para primera respuesta.

**Categorías de triaje masivo:**

| Categoría | Color | Criterio START | Acción |
|-----------|-------|---------------|--------|
| Inmediata | ROJO | Respiración presente post-apertura vía aérea, FR >30 o <10, llenado capilar >2s, no obedece órdenes | Tratamiento prioritario, traslado urgente |
| Retardada | AMARILLO | Respiración normal, llenado capilar ≤2s, obedece órdenes, lesiones que requieren atención pero toleran espera | Tratamiento diferido, monitoreo |
| Menor | VERDE | Ambulatorio, lesiones menores, puede caminar | Autotriaje, zona de espera |
| Expectante/Fallecido | NEGRO | No respira post-apertura vía aérea (START), o pronóstico incompatible con sobrevida en contexto MCI | Cuidados paliativos o morgue |

**Componentes:**

| Componente | Detalle |
|------------|---------|
| START | Simple Triage and Rapid Treatment — adultos, algoritmo 30-2-can do (FR, perfusión, estado mental) |
| JumpSTART | Adaptación pediátrica de START — incluye ventilaciones de rescate |
| SALT | Sort-Assess-Lifesaving interventions-Treatment/Transport — alternativa validada |
| CBRNE triage | Triaje específico para Chemical-Biological-Radiological-Nuclear-Explosive: decontaminación antes de clasificación |
| Tarjetas de triaje | Tarjetas físicas codificadas por color, resistentes al agua, con datos mínimos |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Sobre-triaje MCI | Pacientes triaje rojo sin criterio / Total rojo × 100 | ≤50 % | ACS-COT: ≤50 % (aceptable en MCI) | ACS-COT 2022 | Por evento |
| Sub-triaje MCI | Pacientes críticos clasificados amarillo/verde / Total críticos × 100 | ≤5 % | ACS-COT: ≤5 % | ACS-COT 2022 | Por evento |
| Tiempo triaje por víctima | Segundos promedio por víctima en triaje START | ≤30 seg | — | Ejercicio simulación | Por ejercicio |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Personal no entrenado en triaje masivo | Capacitación anual obligatoria, tarjetas con algoritmo impreso |
| Colapso emocional del triador | Rotación de triadores, apoyo psicológico post-evento |

Ref: START Triage (Newport Beach Fire Dept. 1983); JumpSTART (Romig 2002); SALT (CDC 2011); ACS-COT MCI Guidelines.

### 25.3 Zonas caliente/tibia/fría; descontaminación

Delimitación de zonas operativas en incidentes HAZMAT/CBRNE para protección del personal y prevención de contaminación cruzada.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Zona caliente (Hot zone) | Área contaminada, acceso solo personal con EPP nivel A/B, rescate y extracción |
| Zona tibia (Warm zone) | Corredor de descontaminación, EPP nivel B/C, triaje primario post-decon |
| Zona fría (Cold zone) | Área limpia, puesto médico avanzado, triaje secundario, tratamiento, transporte |
| Descontaminación masiva | Estación portátil con duchas, desvestido, retención de efluentes |
| Descontaminación técnica | Individual, detallada, para personal de primera respuesta post-exposición |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tiempo montaje descontaminación | Minutos desde activación → estación operativa | ≤30 min | — | Ejercicio simulación | Por ejercicio |
| Throughput descontaminación | Víctimas descontaminadas / hora | ≥60 / hora (masiva) | — | Ejercicio simulación | Por ejercicio |
| Contaminación secundaria | Casos contaminación secundaria personal / Total personal expuesto × 100 | 0 % | — | Registros incidente | Por evento |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Víctimas llegan directamente a SUH sin descontaminación | Protocolo lock-down SUH, descontaminación en acceso, señalética |
| EPP insuficiente | Stock EPP CBRNE en SUH, revisión trimestral, ejercicio con EPP |

Ref: OSHA HAZWOPER 1910.120; NFPA 473; CHEMPACK (CDC); MINSAL Plan CBRNE.

### 25.4 Comando unificado (EMS/bomberos/policía)

Estructura de comando multi-agencia para coordinación en escena de incidentes complejos. Unifica toma de decisiones entre servicios de emergencia.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Comando unificado (UC) | EMS + bomberos + policía + SENAPRED en un solo puesto de mando |
| Comunicaciones interoperables | Radio multi-frecuencia, canal común designado, lenguaje estandarizado |
| Sectorización de escena | División geográfica: sector rescate, sector triaje, sector transporte, sector morgue |
| Plan de acción del incidente (IAP) | Objetivos, estrategia, recursos, comunicaciones — actualizado cada período operacional |
| Ejercicios conjuntos | Simulacros multi-agencia ≥1/año con evaluación formal |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Ejercicios conjuntos realizados | Ejercicios multi-agencia / año | ≥1 | NIMS: ≥1 | FEMA NIMS 2017 | Anual |
| Tiempo establecimiento UC | Minutos desde arribo primera agencia → UC operativo | ≤20 min | — | Registros ejercicios | Por ejercicio |
| Interoperabilidad radio | % incidentes con canal común operativo / Total incidentes multi-agencia × 100 | 100 % | — | Registros comunicaciones | Por evento |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Conflicto de autoridad entre agencias | Protocolos pre-establecidos de jurisdicción, entrenamiento conjunto |
| Falla comunicaciones en terreno | Radio satelital de respaldo, mensajeros físicos |

Ref: NIMS (FEMA 2017); ICS 100/200/300 (FEMA); SENAPRED protocolos inter-agenciales.

### 25.5 Post-evento: debriefing y salud del equipo

Proceso estructurado de revisión post-incidente y apoyo psicosocial al equipo de respuesta.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Hot debrief | Inmediato post-evento (≤2h), foco operativo: qué funcionó, qué no, acciones inmediatas |
| Cold debrief | 48-72h post-evento, análisis estructurado con participación multi-agencia |
| After-action report (AAR) | Documento formal: cronología, análisis, lecciones aprendidas, plan de mejora |
| Apoyo psicológico | Defusing grupal ≤24h, evaluación individual de estrés agudo, seguimiento ≤30 días |
| Peer support | Programa de apoyo entre pares capacitados para primera contención emocional |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Hot debrief realizado | Debriefs post-evento / Total eventos MCI × 100 | 100 % | — | Registros calidad | Por evento |
| AAR completado | AAR con plan de mejora / Total eventos MCI × 100 | 100 % | — | Registros calidad | Por evento |
| Evaluación estrés post-evento | % personal con evaluación psicológica post-MCI / Total personal participante × 100 | ≥90 % | — | Salud ocupacional | Por evento |
| Acciones correctivas implementadas | Acciones del AAR implementadas / Total acciones identificadas × 100 | ≥80 % | — | Seguimiento AAR | ≤90 días post-evento |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| TEPT no detectado en personal | Screening a 30 y 90 días, acceso a psicólogo sin estigma |
| Lecciones aprendidas no implementadas | AAR con responsable y fecha por acción, seguimiento formal |

Ref: CISM (Critical Incident Stress Management); Mitchell Model; WHO Psychological First Aid; IASC Guidelines on Mental Health in Emergencies.

## 26. Talento en urgencias

Marco base: ver [Personas, liderazgo y cultura](urn:pro:kb:gestion-redes-general) cap 9. Esta sección agrega los deltas específicos de urgencias.

### 26.1 Competencias y certificaciones (ATLS/ACLS/PALS/TCCC)

Certificaciones clínicas obligatorias y recomendadas para el equipo de urgencias según rol y nivel de complejidad del dispositivo.

**Certificaciones por rol:**

| Certificación | Descripción | Audiencia objetivo | Vigencia | Renovación |
|---------------|-------------|-------------------|----------|------------|
| ACLS | Advanced Cardiovascular Life Support | Médicos SUH, enfermería SUH, paramédicos ALS | 2 años | Re-certificación con evaluación práctica |
| ATLS | Advanced Trauma Life Support | Médicos SUH, cirujanos de guardia | 4 años | Re-certificación con casos simulados |
| PALS | Pediatric Advanced Life Support | Médicos y enfermería SUH con atención pediátrica | 2 años | Re-certificación con evaluación práctica |
| TCCC | Tactical Combat Casualty Care | Personal EMS en contextos de violencia/HAZMAT | 2 años | Re-certificación con simulación |
| PHTLS | Prehospital Trauma Life Support | Paramédicos, enfermería EMS | 4 años | Re-certificación |
| BLS | Basic Life Support | Todo personal clínico SUH y EMS | 2 años | Re-certificación |
| ALSO | Advanced Life Support in Obstetrics | Médicos SUH sin obstetra de guardia | 4 años | Re-certificación |
| Triaje certificado | Certificación ESI/MTS/CTAS | Enfermería de triaje | 2 años | Re-evaluación con concordancia inter-evaluador |

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Plan de certificación | Inventario de brechas por rol, cronograma de certificación, presupuesto asignado |
| Simulación de alta fidelidad | Entrenamiento in-situ con simuladores, escenarios estandarizados, debriefing |
| Recertificación tracking | Sistema de seguimiento de vigencia, alertas de vencimiento ≥3 meses antes |
| Formación continua | Sesiones clínicas semanales, revisión de casos, M&M conferences |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cobertura ACLS médicos SUH | Médicos con ACLS vigente / Total médicos SUH × 100 | 100 % | — | RRHH | Semestral |
| Cobertura ATLS médicos SUH | Médicos con ATLS vigente / Total médicos SUH × 100 | ≥80 % | ACS-COT: 100 % centros trauma | ACS-COT 2022 | Semestral |
| Horas simulación/año | Horas simulación por profesional SUH / año | ≥16 h | — | Centro simulación | Anual |
| Brecha de certificación | Roles sin certificación requerida / Total roles × 100 | ≤10 % | — | RRHH | Semestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Costo elevado de certificaciones | Presupuesto anual asignado, priorización por riesgo, cursos institucionales |
| Certificación sin competencia real | Evaluación práctica in-situ, no solo teórica |

Ref: AHA Education Programs; ACS-COT Verification Requirements; NAEMSP Education Standards; EUNACOM.

### 26.2 Cultura de seguridad

Entorno organizacional en el SUH donde los errores se reportan sin temor, se analizan sistemáticamente y generan mejora. Complementa la cultura de seguridad general de la institución con elementos específicos de urgencias.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Reporte sin culpa | Sistema anónimo de notificación de incidentes, near-miss y condiciones inseguras |
| Just culture | Distinción entre error humano (consolar), comportamiento de riesgo (coaching) y negligencia (sanción) |
| Survey cultura seguridad | AHRQ SOPS (Survey on Patient Safety Culture) — módulo SUH, aplicación anual |
| Safety huddle diario | Reunión breve inicio turno: riesgos del día, aprendizajes, alertas pendientes |
| M&M conference SUH | Revisión mensual de casos con mortalidad/morbilidad, análisis causa raíz, sin culpa |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tasa de reporte de incidentes | Reportes voluntarios / 1.000 consultas SUH | ≥5.0 | NHS: cultura madura >10 | AHRQ SOPS | Mensual |
| Score cultura seguridad | AHRQ SOPS composite score SUH (escala 1-5) | ≥3.5 | AHRQ DB: 3.4-3.8 | AHRQ SOPS 2023 | Anual |
| Safety huddle cumplimiento | Huddles realizados / Turnos × 100 | ≥95 % | — | Registros jefatura | Mensual |
| M&M realizadas | Sesiones M&M / mes | ≥1 | — | Registros calidad | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Cultura punitiva encubierta | Evaluación anónima, protección legal del reporte, liderazgo visible |
| Fatiga de reportes sin retroalimentación | Feedback mensual al equipo: qué se reportó, qué se mejoró |

Ref: AHRQ SOPS 2023; Reason 1997 (Just Culture); Dekker 2007 (Just Culture); Política Nacional Seguridad Paciente MINSAL.

### 26.3 Bienestar del equipo de urgencias

Estrategias específicas para prevención de burnout, apoyo emocional y cuidado del equipo que trabaja en el entorno de alta presión del SUH.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Pausas protegidas | Descanso ≥30 min cada 6h de turno, espacio físico de descanso en SUH |
| Apoyo post-evento crítico | Defusing ≤24h, CISM (Critical Incident Stress Management), derivación si necesario |
| Screening burnout | MBI (Maslach Burnout Inventory) semestral, acción si agotamiento emocional alto |
| Peer support | Red de pares capacitados para contención emocional entre colegas |
| Flexibilidad de turnos | Opciones de intercambio, turnos preferenciales, reducción jornada post-incidente |
| Espacios de reconocimiento | Reconocimiento formal del buen desempeño, no solo del error |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Burnout equipo SUH (MBI) | % personal con agotamiento emocional alto / Total personal SUH | ≤30 % | EE.UU. Emergency Medicine: 60 % (2022) | Shanafelt 2022 | Semestral |
| Rotación personal SUH | Personal que renuncia / Dotación total SUH × 100 / año | ≤15 % | — | RRHH | Anual |
| Ausentismo SUH | Días ausencia no programada / Días programados × 100 | ≤5 % | — | RRHH | Mensual |
| Satisfacción laboral | Encuesta satisfacción equipo SUH (escala 1-5) | ≥3.5 | — | Encuesta interna | Semestral |
| Apoyo post-evento realizado | Sesiones apoyo post-evento / Total eventos críticos × 100 | 100 % | — | Salud ocupacional | Por evento |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Estigma por buscar ayuda | Normalización, confidencialidad, liderazgo que modela |
| Burnout crónico normalizado | Indicadores en tablero directivo, plan de acción institucional |

Ref: Shanafelt et al. 2022 (Physician Burnout); NAM Clinician Well-Being 2019; ACEP Physician Wellness Policy; Dr. Lorna Breen Heroes Act 2022.

### 26.4 Investigación e innovación

Promoción de investigación aplicada e innovación en urgencias para mejora continua basada en evidencia.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Registro de datos para investigación | EDIS como fuente de datos estructurados, anonimización, consentimiento |
| Redes de investigación | Participación en registros multicéntricos (CARES, GWTG, registros nacionales) |
| Ciclos PDSA | Mejora continua: proyectos locales de calidad con metodología IHI |
| Innovación en procesos | Lean/Six Sigma aplicado a flujo SUH, diseño centrado en usuario |
| Comité ético-científico | Revisión de protocolos de investigación en urgencias, consentimiento diferido |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Proyectos PDSA activos | N° proyectos mejora en curso en SUH | ≥2 | — | Registros calidad | Semestral |
| Publicaciones/presentaciones | Trabajos publicados o presentados en congresos / año | ≥1 | — | Registro académico | Anual |
| Participación en registros | Registros multicéntricos con aporte activo de datos | ≥1 | — | Coordinación investigación | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Investigación sin tiempo protegido | Asignación horas dedicadas, reconocimiento académico |
| Consentimiento en contexto urgencia | Protocolo consentimiento diferido aprobado por CEC, marco regulatorio Ley 20.120 |

Ref: Ley 20.120 (Investigación en humanos); ACEP Research Policy; IHI PDSA Methodology; WMA Declaration of Helsinki.
