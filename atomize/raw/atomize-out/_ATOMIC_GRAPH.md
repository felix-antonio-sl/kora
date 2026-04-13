# Codex Nexus Vitalis
<!-- /atomize · 334 proposiciones · ~350 entidades · 1 archivo · 2026-04-10 -->
<!-- Source: Health Informatics: An Interprofessional Approach, Hardy, 3rd ed., 2024 -->
<!-- Consultar: buscar por [P###], por tipo (DEFINICIÓN, HECHO, REGLA...), o por entidad -->

## Section 1: Fundamental Knowledge in Health Informatics

### Ch 1: An Introduction to Health Informatics

- [P001] **DEFINICIÓN** — health informatics: especialidad interdisciplinaria integrando ciencias salud, computación, información → gestionar/comunicar datos/información/conocimiento/sabiduría en atención sanitaria
- [P002] **HECHO** — IOM report "To Err is Human" (2000) discutió errores médicos, fundamentó necesidad tecnología para entender/reducir errores
- [P003] **HECHO** — "Crossing the Quality Chasm" (IOM, 2001) evidenció necesidad IT mejorar seguridad paciente, enfatizó EHRs, CDS, analytics, automatización
- [P004] **HECHO** — James (2013) estimó 440,000 estadounidenses hospitalizados/año experimentan eventos adversos prevenibles contribuyendo a muerte; daño grave 10-20x más común que daño letal
- [P005] **HECHO** — Makary & Daniel (2016) publicaron "Medical Error—Third Leading Cause of Death in US" en BMJ
- [P006] **DEFINICIÓN** — error médico (Reason): falla acción planificada completarse como previsto (error ejecución) / uso plan incorrecto alcanzar objetivo (error planificación)
- [P007] **HECHO** — modelo Swiss cheese (Reason): defensas organizacionales tienen agujeros → errores pasan cuando agujeros se alinean
- [P008] **HECHO** — IOM (2003) identificó 5 competencias core profesionales salud: patient-centered care, equipos interdisciplinarios, EBM, quality improvement, informatics
- [P009] **HECHO** — AACN Essentials Series incluye Domain 8: Informatics and Healthcare Technologies
- [P010] **ALCANCE** — tres temas comunes definiciones health informatics: (1) especialidad interdisciplinaria, (2) vinculada uso IT en salud, (3) enfocada recolección/procesamiento datos/toma decisiones
- [P011] **HECHO** — HITECH Act implementado 2009 objetivo modernizar infraestructura IT salud US; incentivos financieros adopción EHR
- [P012] **HECHO** — 2015: 84% hospitales adoptaron sistema EHR básico
- [P013] **HECHO** — HIPAA, HITECH Act, MACRA = legislación principal gobernando privacidad/seguridad/IT información salud
- [P014] **HECHO** — datos MPSMS (2012-2013): pacientes con tratamiento EHR completo 17-30% menos probabilidad eventos adversos intrahospitalarios

### Ch 2: Theoretical Frameworks

- [P015] **DEFINICIÓN** — sistema (Von Bertalanffy): conjunto partes relacionadas interactuantes encerradas en frontera; puede ser abierto (semipermeable) o cerrado (impermeable)
- [P016] **DEFINICIÓN** — 6 conceptos cambio sistemas: homeostasis dinámica, equifinalidad, entropía, negentropía, especialización, reverberación
- [P017] **DEFINICIÓN** — CAS: muchas partes diversas/autónomas, interrelacionadas, comportándose como todo unificado, aprendiendo de experiencia; interdependencias no lineales, control distribuido, auto-organización
- [P018] **HECHO** — Cynefin Framework (Snowden & Boone, 2007): 5 dominios gestión incertidumbre: simple, complicado, complejo, caótico, desorden
- [P019] **HECHO** — modelo Shannon-Weaver (1948): sender → transmitter → channel → decoder → receiver; información medida en bits
- [P020] **DEFINICIÓN** — modelo DIKW Nelson: datos → información → conocimiento → sabiduría; sabiduría = uso apropiado conocimiento gestionar problemas humanos
- [P021] **HECHO** — ANA incluyó modelo DIKW en Nursing Informatics: Scope and Standards of Practice (2008)
- [P022] **HECHO** — teoría cambio planificado Lewin: 3 etapas = descongelamiento, movimiento, recongelamiento
- [P023] **HECHO** — difusión innovación Rogers: innovadores (2.5%), early adopters (13.5%), early majority (34%), late majority (34%), laggards (16%)
- [P024] **HECHO** — 5 atributos innovación afectando adopción: ventaja relativa, compatibilidad, complejidad, trialability, observabilidad
- [P025] **HECHO** — SLCM Staggers-Nelson: espiral 8 pasos; análisis + planificación requieren ~70% tiempo/recursos proyecto
- [P026] **HECHO** — TAM (Davis, 1989): utilidad percibida + facilidad uso percibida → actitud → intención → uso; basado Theory of Reasoned Action
- [P027] **HECHO** — UTAUT sintetiza 8 modelos aceptación tecnología; explica ~70% varianza intención uso
- [P028] **HECHO** — modelo sociotécnico Sittig & Singh: 8 dimensiones interdependientes estudiar HIT en CAS
- [P029] **HECHO** — NASSS framework (Greenhalgh): non-adoption, abandonment, scale-up, spread, sustainability

### Ch 3: Health Systems and Information Flow

- [P030] **DEFINICIÓN** — LHS: sistema abierto usando datos/información/conocimiento/sabiduría → mejorar seguridad, eficiencia, satisfacción
- [P031] **DEFINICIÓN** — data lake: repositorio datos estructurados + no estructurados estado crudo; capas Raw/Refined/Publishing
- [P032] **DEFINICIÓN** — data warehouse: almacena datos procesados/estructurados/filtrados; datos fijos
- [P033] **HECHO** — ~80% datos EHR = texto libre no estructurado, requiriendo NLP
- [P034] **HECHO** — IDC predice datos globales 33 zettabytes (2018) → 175 zettabytes 2025; 49% cloud pública
- [P035] **DEFINICIÓN** — 3 modelos control acceso: MAC (mandatorio), DAC (discrecional), RBAC (role-based, más usado)
- [P036] **HECHO** — modelos datos estandarizados EDWs: OMOP, i2b2, Sentinel, PCORnet
- [P037] **HECHO** — TIGER International Framework identifica competencias core health informatics 30 áreas

### Ch 4: Informatics-Related Standards and Standard Setting

- [P038] **DEFINICIÓN** — interoperabilidad: extensión sistemas salud pueden intercambiar datos e interpretar datos compartidos (HIMSS)
- [P039] **DEFINICIÓN** — terminología referencia: conocimiento dominio recolección/agregación datos; terminología interfaz: términos orientados tarea entrada datos EHRs
- [P040] **HECHO** — UMLS Metathesaurus: >190 terminologías fuente, >4.4M conceptos, >16.1M nombres únicos; NLM cada 6 meses
- [P041] **HECHO** — LOINC establecido 1994 Regenstrief Institute; 6 ejes codificación; >80,000 términos
- [P042] **HECHO** — SNOMED CT = terminología clínica más comprehensiva; gestionado IHTSDO; gratuito países miembros
- [P043] **HECHO** — ICD copyright WHO; ~70% gastos salud mundiales; ICD-10 implementado US octubre 2015
- [P044] **HECHO** — RxNorm: NLM sistema normalizado nombres medicamentos 14 terminologías; soporta e-prescribing
- [P045] **HECHO** — ANA reconoce 10 terminologías healthcare enfermería: 7 nursing-specific + 3 multidisciplinarias (LOINC, SNOMED CT, ABC Codes)
- [P046] **HECHO** — NANDA-I: 235 diagnósticos enfermería 47 clases / 13 dominios
- [P047] **HECHO** — NIC: >550 intervenciones enfermería 30 clases / 7 dominios; ~13,000 actividades
- [P048] **HECHO** — NOC: 540 resultados 34 clases / 7 dominios; escalas Likert 5 puntos
- [P049] **HECHO** — HL7 desde 1987: estándares clave = CDA (documentos clínicos XML) y FHIR (intercambio datos basado recursos)
- [P050] **DEFINICIÓN** — recursos FHIR simulan "formularios" papel replicando información clínica/administrativa
- [P051] **HECHO** — ANA recomienda SNOMED CT + LOINC para intercambio C-CDA
- [P052] **HECHO** — CMS estableció Meaningful Use (ahora Promoting Interoperability) programa incentivos EHR certificado

### Ch 5: Evaluation of Health Information Systems

- [P053] **DEFINICIÓN** — evaluación HIS: medir/explorar propiedades HIS, resultado informa decisión sistema contexto específico
- [P054] **DEFINICIÓN** — formativa: feedback mejora continua; sumativa: evaluar mérito programa
- [P055] **HECHO** — ELICIT framework (Kukhareva et al., 2022): 12 tipos estudio evaluación ciclo vida HIS
- [P056] **HECHO** — CDS Taxonomy (Wright et al.): 53 tipos CDS en 6 grupos
- [P057] **HECHO** — Situation Awareness (Endsley): 3 niveles = percepción, comprensión, proyección
- [P058] **HECHO** — PDCA (Deming, 1950s): mejora calidad iterativa; ciclo puede ser tan corto como 1 hora
- [P059] **HECHO** — CFIR (Damschroder, 2009): 5 dominios principales, 38 constructos implementación
- [P060] **HECHO** — RE-AIM: 5 constructos implementación: Reach, Effectiveness, Adoption, Implementation, Maintenance
- [P061] **HECHO** — Donabedian estructura-proceso-resultado: medidas estructurales, proceso, resultado
- [P062] **HECHO** — DeLone & McLean IS success (1992/2003): calidad sistema/información/servicio → uso/satisfacción → resultados
- [P063] **HECHO** — instrumentos validados: SUS (10 ítems, 0-100), NASA-TLX (carga trabajo), PAM (activación paciente), SERVQUAL
- [P064] **HECHO** — sistemas CDS AI requieren evaluación/monitoreo continuo; afectados sesgos datos entrenamiento

## Section 2: Health Information Systems and Applications

### Ch 6: Technical Infrastructure

- [P065] **DEFINICIÓN** — infraestructura IT healthcare = todos componentes requeridos operar/gestionar servicios IT dentro setting healthcare
- [P066] **DEFINICIÓN** — thin client: procesamiento en servidor remoto; sin datos paciente locales; robo físico no compromete confidencialidad
- [P067] **REGLA** — bajo HIPAA, entidades transmitiendo datos son "covered entities" requeridas cumplir criterios estrictos precisión/seguridad
- [P068] **HECHO** — HITECH Act (2009) estableció requerimiento datos compartidos como EHRs; vinculó reembolso CMS a meaningful use
- [P069] **HECHO** — 21st Century Cures Act aprobada 2016 acelerar desarrollo productos médicos / mejorar innovación healthcare
- [P070] **DEFINICIÓN** — ciclo vida datos = 8 pasos: generación, recolección, procesamiento, almacenamiento, gestión, análisis, visualización, interpretación; EHR agrega 9°: compartición
- [P071] **DEFINICIÓN** — EMR = documentación paciente único localización única; EHR = extiende EMR compartiendo datos entre proveedores/instituciones
- [P072] **DEFINICIÓN** — CDR = componente almacenamiento registros clínicos: resultados lab, órdenes medicamentos, signos vitales, demographics
- [P073] **DEFINICIÓN** — almacenamiento central = repositorio único, requiere mapeo terminología; distribuido = cada app propio repositorio, datos federados real-time
- [P074] **DEFINICIÓN** — MPI = conjunto info identificando persona/paciente; crea "golden record"
- [P075] **HECHO** — eHealth Exchange (antes NwHIN) gestionado Sequoia Project; organizaciones 50 estados + 4 agencias federales (SSA, DoD, VA, HHS)
- [P076] **DEFINICIÓN** — ransomware = ataque cyber encriptando covertamente datos, demandando pago clave desencriptación
- [P077] **HECHO** — UVM Medical Center 2020 ransomware encriptó EHR/payroll; bloqueado 1 mes; costo $50M

### Ch 7: The Electronic Health Record and Precision Care

- [P078] **ALCANCE** — EHR = registro nacimiento-a-muerte múltiples fuentes; EMR limitado organización única
- [P079] **HECHO** — ARRA (2009) incluyó HITECH expandir adopción EHR; CARES Act (2020) $2T estímulo, $127B healthcare COVID-19
- [P080] **HECHO** — meaningful use CMS (2011) renombrado Promoting Interoperability (PI) 2018; 3 etapas
- [P081] **HECHO** — MACRA (2015) cambió reembolso Medicare fee-for-service → value-based care; MIPS + APMs
- [P082] **HECHO** — encuesta 2019: 94% hospitales US adoptaron EHR certificado; >50% utilizan HIEs
- [P083] **DEFINICIÓN** — CPOE = software proveedores autorizados ingresar/procesar órdenes vía computador; elimina errores transcripción manuscrita
- [P084] **HECHO** — BCMA introducido 1992 enfermera VHA; escanea badge + pulsera + código barras; verifica 5 rights (paciente, droga, dosis, hora, vía)
- [P085] **HECHO** — DICOM = estándar global transmisión/almacenamiento/display imagenología; PACS almacena imágenes digitales
- [P086] **DEFINICIÓN** — PGHD = datos salud creados/registrados por pacientes/familia/cuidadores abordar problema salud
- [P087] **HECHO** — costos EHR: práctica privada grande ~$233,297 año 1; hospitales $25M-$10B; mantenimiento anual ~18-20% precio compra
- [P088] **⚠ TENSIÓN** — carga documentación: enfermeros 23% tiempo documentando post-EHR vs 9% pre-EHR; menos tiempo con pacientes
- [P089] **DEFINICIÓN** — medicina precisión = ciencia emergente usando big data, genómica, ML personalizar tratamiento basado genética/estilo vida/factores socioculturales
- [P090] **HECHO** — encuesta KFF 2019: 88% indicaron proveedor usa EHR; solo 45% dijeron mejoraron cuidado; 1/5 reportó errores

### Ch 8: Administrative Applications in Healthcare

- [P091] **DEFINICIÓN** — ACO = red doctores/hospitales compartiendo responsabilidad cuidado; bonos controlar costos cumpliendo benchmarks calidad
- [P092] **DEFINICIÓN** — P4P = concepto vinculando pago calidad cuidado/resultados en vez volumen servicios
- [P093] **HECHO** — ACA Hospital Readmissions Reduction Program reduce pagos 1% hospitales readmisiones evitables excesivas
- [P094] **HECHO** — desde ACA (2010), >440 Medicare ACOs; 54% disminuyeron gastos, $383M ahorros netos
- [P095] **DEFINICIÓN** — value-based care = mejor resultado por dólares invertidos; requiere integración datos clínicos + financieros nivel poblacional
- [P096] **HECHO** — códigos CPT tienen RVU adjunto definido Medicare; wRVU mide productividad/reembolso médico
- [P097] **DEFINICIÓN** — BI = adquisición/correlación/transformación datos en información accionable analytics
- [P098] **HECHO** — mercado vendors HIS 2013 top 5: McKesson ($3.4B), Cerner ($2.9B), Siemens ($1.8B), Epic ($1.7B), Allscripts ($1.4B)
- [P099] **REGLA** — EMTALA requiere pacientes tratados emergencias independientemente capacidad pago

### Ch 9: Community Health Systems

- [P100] **HECHO** — home health originó 1800s modelo district nursing Rathbone, Inglaterra; Lillian Wald estableció Henry Street Settlement House (1893) NYC
- [P101] **HECHO** — Medicare (1965) incluyó home health personas ≥65; Florence Wald estableció Connecticut Hospice (1974) primer US
- [P102] **HECHO** — Donabedian (1966) framework estructura-proceso-resultado evaluar calidad cuidado médico
- [P103] **DEFINICIÓN** — OASIS = dataset estandarizado agencias home health Medicare; determina pago, mide calidad/resultados
- [P104] **DEFINICIÓN** — Omaha System = terminología POC reconocida ANA mapeada SNOMED CT/LOINC; 3 componentes, 42 problemas, 75 targets, 4 categorías acción; dominio público
- [P105] **HECHO** — Triple Aim (2008, Berwick): mejor cuidado individuos, mejor salud poblaciones, reducción costos; Quadruple Aim (2014) agregó bienestar equipo
- [P106] **DEFINICIÓN** — hospice = servicios pacientes expectativa vida ≤6 meses agotaron tratamiento curativo
- [P107] **DEFINICIÓN** — palliative care = calidad vida pacientes enfermedad amenazante; comienza cuando cura no posible
- [P108] **HECHO** — ~35,000 agencias home health US; 11,356 certificadas Medicare; sirven 12-15M pacientes >600M visitas/año

### Ch 10: Public Health Informatics

- [P109] **DEFINICIÓN** — public health informatics = especialidad métodos/herramientas informática resolver problemas salud pública
- [P110] **HECHO** — expectativa vida US declinó 78.8 (2019) → 77.8 (2020); Non-Hispanic Black -2.7 años, Hispanic -1.9, White -0.8
- [P111] **HECHO** — Florence Nightingale: datos mortalidad soldados Crimea, Nightingale Rose Diagram; John Snow: mapeo cólera Londres 1854
- [P112] **REGLA** — HIPAA Privacy Rule permite divulgar PHI sin autorización a autoridades salud pública prevención/control enfermedad
- [P113] **DEFINICIÓN** — vigilancia sindrómica = detectar/monitorear eventos salud antes diagnóstico; alerta temprana niveles enfermedad inusuales
- [P114] **HECHO** — JHCRC comenzó ene 22, 2020 rastreo global COVID-19; 260 fuentes, 182 agencias
- [P115] **DEFINICIÓN** — infodemic = información rápida generalizada conteniendo datos precisos/imprecisos
- [P116] **HECHO** — 79% apps healthcare venden/comparten datos recolectados (Grundy 2019); desarrolladores apps terceros no cubiertos HIPAA

## Section 3: Decision-Making and the Digitally Engaged Patient

### Ch 11: Evidence-Based Informatics

- [P117] **DEFINICIÓN** — EBP = integración mejor evidencia investigación + expertise clínico + preferencia paciente → decisiones best-practice
- [P118] **DEFINICIÓN** — PBE = diseño investigación prospectivo usando datos práctica actual; EBP usa evidencia guiar práctica, PBE obtiene evidencia de práctica
- [P119] **HECHO** — Stevens ACE Star Model 5 puntos: descubrimiento, resumen evidencia, traducción guías, integración práctica, evaluación
- [P120] **HECHO** — Cochrane Database: 8,715 SRs octubre 2021; >10,000 artículos investigación publicados anualmente medicina
- [P121] **REGLA** — SRs = enlace central investigación y decisión clínica (IOM, 2008); gold standard resúmenes evidencia
- [P122] **HECHO** — USPSTF gradúa recomendaciones A-D + I; A = certeza alta beneficio sustancial → ofrecer
- [P123] **HECHO** — AGREE II: 23 ítems evaluar CPGs; evalúa alcance, stakeholders, rigor, claridad, aplicación, independencia editorial
- [P124] **HECHO** — TeamSTEPPS: healthcare militar desde 1995; civil 2006; mejora comunicación/teamwork → mejor cuidado
- [P125] **HECHO** — PCORI CDRNs permiten investigación efectividad comparativa proveyendo soluciones informáticas multi-institucional

### Ch 12: Clinical Decision Support

- [P126] **DEFINICIÓN** — CDS = herramientas proveyendo conocimiento persona-específico, inteligentemente filtrado tiempos apropiados, mejorar salud (Osheroff 2007)
- [P127] **HECHO** — pacientes US reciben solo 54.9% procesos cuidado recomendados (McGlynn 2003)
- [P128] **HECHO** — primer CDS: de Dombal (1972) diagnóstico dolor abdominal; Bayesiano 91.8% vs médico 79.6%
- [P129] **HECHO** — taxonomía Wright (2011): 6 categorías CDS / 53 subtipos
- [P130] **HECHO** — CDS Five Rights (Osheroff/HIMSS): información correcta, persona correcta, formato correcto, canal correcto, punto workflow correcto
- [P131] **HECHO** — Kawamoto (2005): provisión automática CDS parte workflow = feature más crítica (OR 112.1, P<.00001)
- [P132] **HECHO** — Brigham Women's CPOE+CDS redujo errores serios medicación no interceptados 86%
- [P133] **HECHO** — CDS ventilador ARDS → 60% supervivencia vs ~35% esperada
- [P134] **HECHO** — VHA estimó inversiones HIT >$3B beneficios netos; CDS catalizador importante ROI
- [P135] **HECHO** — alert fatigue: clínicos ignoran alertas triggers excesivos; abordajes: priorizar, contextualizar, governance, predictive filtering
- [P136] **HECHO** — estándares CDS alineados HL7 FHIR: SMART apps, CDS Hooks, CQL, Clinical Reasoning
- [P137] **⚠ TENSIÓN** — beneficios financieros CDS pueden acumularse stakeholders distintos quienes invierten (incentivos desalineados)

### Ch 13: The Evolving ePatient

- [P138] **DEFINICIÓN** — ePatient = persona rol activo decisiones salud; Tom Ferguson (1975); equipped, enabled, empowered, engaged
- [P139] **HECHO** — usuarios internet: 16M (1995) → 4.66B/~60% población mundial (Oct 2020)
- [P140] **HECHO** — Human Genome Project: 13 años, ~$3B (2003); 23andMe: info genética directa consumidor $99 (2021)
- [P141] **HECHO** — >350,000 apps salud/fitness disponibles smartphone (IQVIA 2021)
- [P142] **HECHO** — OpenAPS: páncreas artificial open-source; >2,300 sistemas DIY closed-loop julio 2021
- [P143] **HECHO** — OpenNotes: 2020 >250 organizaciones, >50M pacientes; antes 29% médicos pro → después 71%
- [P144] **HECHO** — abril 5, 2021: 8 tipos notas clínicas no deben bloquearse per 21st Century Cures Act
- [P145] **HECHO** — solo 15-30% pacientes usan portales online pese disponibilidad (US GAO)
- [P146] **⚠ TENSIÓN** — digital divide: COVID-19 expuso disparidades acceso broadband/smartphone entre grupos raciales/socioeconómicos

### Ch 14: Digital Health: Managing Health and Wellness

- [P147] **DEFINICIÓN** — mHealth = práctica médica/salud pública soportada dispositivos móviles (WHO GOe)
- [P148] **HECHO** — apps salud: ~40,000 (2013) → >318,000 (2018); >200 agregadas diario; 2/3 wellness, 1/4 disease management
- [P149] **HECHO** — WHO publicó primeras guías evidence-based intervenciones salud digital 2019
- [P150] **HECHO** — FDA guidance mobile medical apps 2013; supervisará subconjunto risk-based; discreción regulatoria riesgo moderado
- [P151] **HECHO** — Goldman Sachs pronosticó $305B ahorros healthcare digital US
- [P152] **HECHO** — evidencia alta calidad mHealth: cesación tabaco + adherencia terapia antirretroviral (Cochrane)
- [P153] **HECHO** — 5 poblaciones: diabetes prevention, diabetes, asma, rehab cardíaca/pulmonar → apps reducen cuidado agudo ahorrando ~$7B/año (IQVIA 2017)
- [P154] **RESTRICCIÓN** — herramientas CDS AI-driven tienen sesgos inherentes: captura conocimiento + procesamiento (Gurupur & Wan, 2020)

### Ch 15: Personal Health Records

- [P155] **DEFINICIÓN** — PHR = aplicación privada/segura individuo accede/gestiona/comparte info salud; evita palabra "paciente" — salud/bienestar no solo enfermedad
- [P156] **DEFINICIÓN** — standalone PHR = separado EHR; connected (tethered) = enlazado sistema salud, portal paciente
- [P157] **HECHO** — VHA MyHealtheVet (2003): primeros portales paciente; Blue Button (2010, Markle Foundation) clic único acceder registros
- [P158] **HECHO** — Google Health (2008-12) y HealthVault (2007-19) discontinuados falta adopción; Apple Health lanzado 2018
- [P159] **HECHO** — Stage 2 MU: pacientes acceder EHR electrónicamente; ≥5% usar; VDT ≤36h alta hospital
- [P160] **HECHO** — portales paciente hospital: 27% (2012) → 93% (2017); uso HINTS: 25.6% (2014) → 39.5% (2020)
- [P161] **HECHO** — barreras adopción PHR: preferencia presencial 64%, sin necesidad 49%, incomodidad 26%, privacidad 23%
- [P162] **⚠ TENSIÓN** — PHR incrementa mensajería paciente → incrementa carga clínica no reembolsable; evidencia limitada mejora calidad

### Ch 16: Social Media Tools for Health Informatics

- [P163] **HECHO** — 2021: 70% estadounidenses usan social media; YouTube/Facebook dominantes; <30 favorecen Instagram/TikTok
- [P164] **REGLA** — proveedores deben mantener cumplimiento HIPAA social media; ANA/AMA: mantener confidencialidad toda info paciente
- [P165] **DEFINICIÓN** — infodemic = explosión información verdadera+falsa crisis salud pública (WHO); ejemplificado COVID-19
- [P166] **DEFINICIÓN** — apomediation = dirigir consumidores info internet alta calidad en vez interponerse (Eysenbach 2008)
- [P167] **HECHO** — NLRB/NLRA protege derechos empleados discutir condiciones trabajo vía social media
- [P168] **RESTRICCIÓN** — políticas social media: no demasiado lenientes/estrictas; congruentes legislación; no pueden regular comportamiento empleado legalmente protegido

## Section 4: Lifecycle Management

### Ch 17: Project Management Principles

- [P169] **DEFINICIÓN** — proyecto = emprendimiento temporal entregando producto/servicio particular (PMI 2014)
- [P170] **HECHO** — PMI: 80% proyectos fallan sin metodología estructurada; alto rendimiento cumplen metas 2.5x más frecuente
- [P171] **ALCANCE** — 4 grupos proceso PM: Initiation, Planning, Execution, Closure
- [P172] **DEFINICIÓN** — scope creep = aumento no controlado alcance original; gestionar vía scope document
- [P173] **HECHO** — 9 áreas conocimiento PMI: integración, scope, tiempo, costos, calidad, HR, comunicación, riesgos, adquisiciones
- [P174] **DEFINICIÓN** — WBS = descomposición entregables proyecto en tareas trabajables
- [P175] **REGLA** — resource managers no deberían servir simultáneamente project managers — necesidades conflictivas

### Ch 18: Strategic Planning and Information System Selection

- [P176] **DEFINICIÓN** — plan estratégico = documento formal 3-5 años futuro; visión/misión, objetivos, SWOT
- [P177] **DEFINICIÓN** — burnout clínico = estrés largo plazo: agotamiento emocional, despersonalización, falta logro (AHRQ); EHRs contribuyente
- [P178] **REGLA** — implementar EHR es proyecto clínico — clínicos líderes, no solo técnicos
- [P179] **ALCANCE** — Clayton's Framework EHR (orden): Compromiso institucional → Liderazgo → Personas → Infraestructura → Software
- [P180] **DEFINICIÓN** — RFI (información), RFP (propuestas, scoring ponderado), RFQ (cotización, requerimientos claros)
- [P181] **REGLA** — site visits comprador más valiosas que vendor; 5 min clínico en scrubs > 1h ejecutivo
- [P182] **REGLA** — organización no compra EHR — lo licencia; mantenimiento = mayoría pagos vendor tiempo
- [P183] **DEFINICIÓN** — BATNA = mantener opción vendor backup durante negociaciones

### Ch 19: Contract Negotiations and Software Licensing

- [P184] **REGLA** — formulario vendor unilateral protege vendor; HCO no subestimar leverage negociar
- [P185] **REQUISITO** — equipo negociación: CFO, abogado IP, CIO, CMIO/CNIO, compliance officer HIPAA/Stark, experto seguridad
- [P186] **DEFINICIÓN** — SaaS = aplicaciones hosted vendor, clientes acceden vía red; on-premises = instalado computador HCO
- [P187] **DEFINICIÓN** — software escrow = tercero neutral mantiene source code; condiciones: bancarrota, breach mantenimiento, discontinuación soporte
- [P188] **DEFINICIÓN** — SLA = niveles servicio + consecuencias falla; 99.999% uptime gold standard; 100% no factible
- [P189] **REGLA** — downtime mantenimiento no contabilizado; force majeure excluido cálculos uptime
- [P190] **HECHO** — tarifas mantenimiento típicamente 15%-22% licencia/año; rango 10%-40%
- [P191] **REGLA** — soporte vendor ≥5 años cubrir ROI; HCO preservar derecho terminación
- [P192] **REGLA** — terminación breach requiere: breach "material" + notificación escrita + 30 días cura
- [P193] **REGLA** — software mission-critical: licencia sobrevive terminación; vendor retiene IP, HCO continúa uso
- [P194] **REGLA** — período transición: si seguridad paciente amenazada, HCO derecho hasta 1 año migrar solución sustituta
- [P195] **DEFINICIÓN** — limitation liability = tope responsabilidad vendor (tarifa licencia); HCO negociar 300%-500%
- [P196] **REGLA** — propiedad datos HCO debe especificarse; proteger datos paciente incluso de-identificados

### Ch 20: Implementing and Upgrading an Information System

- [P197] **HECHO** — HITECH creó programa incentivos $27B; pagos Medicare/Medicaid 5-10 años proveedores/hospitales elegibles
- [P198] **HECHO** — MU Stage 1 (2011) captura datos; Stage 2 (2014) prácticas avanzadas/portales; Stage 3 (2017) interoperabilidad/resultados
- [P199] **HECHO** — adopción EHR hospitales US: 16% (2009) → 76% básico (2014) → 9/10 usando 2019
- [P200] **DEFINICIÓN** — information blocking = práctica interfiriendo acceso/intercambio/uso EHI; 8 excepciones Cures Act
- [P201] **HECHO** — USCDI requiere 8 tipos notas clínicas disponibles pacientes sin cargo
- [P202] **DEFINICIÓN** — e-iatrogenesis = errores introducidos EHRs: errores yuxtaposición seleccionar paciente/medicamento equivocado lista
- [P203] **HECHO** — TRIP (AHRQ 1999): 10-20 años incorporar hallazgos clínicos práctica general ("lethal lag")
- [P204] **DEFINICIÓN** — superuser = staff training adicional, soporte at-the-elbow durante go-live
- [P205] **DEFINICIÓN** — big bang = todo implementado vez, menor costo total pero caída productividad; phased = procesos coexisten
- [P206] **REGLA** — training end-user no más 4-6 semanas antes go-live facilitar retención
- [P207] **HECHO** — Tall Man lettering per ISMP: NiFEDipine vs niCARdipine, DOBUTamine vs DOPamine

### Ch 21: Downtime and Disaster Recovery for HIS

- [P208] **HECHO** — 2016 Ponemon: costo promedio downtime healthcare $740,357/incidente (~$8,800/min)
- [P209] **HECHO** — 2020: 92 ataques ransomware >600 clínicas/hospitales, >18M registros, ~$21B costo
- [P210] **DEFINICIÓN** — CMDB = ITIL best practice inventario/documentación sistema configuration items
- [P211] **ALCANCE** — niveles downtime: L1 (<1h) → L2 (sistema, ≤4h) → L3 (múltiples, >4h) → L4 (todos, causa conocida) → L5 (ransomware, rebuild)
- [P212] **DEFINICIÓN** — hot site: recovery ≤24h; warm site: intermedio; cold site: capacidad pero >30 días
- [P213] **ALCANCE** — tiers continuidad: Tier I (≤24h, hot site), Tier II (≤72h), Tier III (≤1 semana), Tier IV (≤1 mes)
- [P214] **OBLIGACIÓN** — planes contingencia/desastre obligatorios per HIPAA security rule, HHS, acreditación
- [P215] **REGLA** — sistemas redundantes proveer demographics, órdenes, MAR, vitales, labs, imaging, notas progreso durante downtime
- [P216] **REGLA** — manuales desastre múltiples formatos no-dependientes red; evaluados ≥anualmente; simulados
- [P217] **REQUISITO** — downtime box: caja física formularios/instrucciones papel ≥24h todas unidades
- [P218] **HECHO** — teléfonos analógicos áreas clave hospital (color rojo) funcionan downtimes red/eléctricos cuando VOIP no
- [P219] **REGLA** — ejercicios desastre requeridos Joint Commission; training nuevos empleados orientación, actualizado ≥anual

## Section 5: Usability, Analytics, and Education

### Ch 22: Improving the User Experience for Health IT

- [P220] **DEFINICIÓN** — usabilidad (ISO 9241-11): producto usado usuarios específicos contexto específico lograr objetivos con efectividad, eficiencia, satisfacción
- [P221] **DEFINICIÓN** — UCD 3 axiomas: enfoque temprano usuarios, diseño iterativo, medidas sistemáticas interacciones; mínimo 3 rondas
- [P222] **DEFINICIÓN** — HCI = estudio diseño/implementación/evaluación sistemas computador interactivos contexto tareas usuario
- [P223] **HECHO** — TJC 2015: 120 eventos sentinel HIT; 1/3 interfaz humano-computador, 24% workflow/comunicación
- [P224] **HECHO** — evaluaciones admisión acute care: 30-60 min, 532 clicks
- [P225] **DEFINICIÓN** — SEIPS 3.0: modelo centrado sistemas trabajo y centralidad paciente; journey paciente, episodios distribuidos tiempo/localización
- [P226] **DEFINICIÓN** — discount usability (Nielsen 1993): técnicas reduciendo usuarios; HE por 3-5 expertos encuentra 81-90% problemas
- [P227] **HECHO** — sets heurísticos: Nielsen 10, Zhang 14, Shneiderman 8 golden rules, HIMSS 9 principios
- [P228] **DEFINICIÓN** — think-aloud: usuarios hablan mientras interactúan; 5 usuarios detectan 60-80% errores diseño
- [P229] **HECHO** — SUS (Brooke 1986): estándar industria usabilidad, 10 ítems, disponible público
- [P230] **HECHO** — FDA requiere testing usabilidad dispositivos médicos >20 años; otros HIT solo comenzando
- [P231] **HECHO** — Nielsen Norman Group: productividad intranet redesign 8x-50x costos; incremento promedio 161%

### Ch 23: Data Science and Analytics in Healthcare

- [P232] **DEFINICIÓN** — 5 Vs big data: Volume, Velocity, Variety, Veracity, Value (Eaton 2012)
- [P233] **DEFINICIÓN** — analytics: descriptive (retrospectivo), predictive (modelos matemáticos), prescriptive (acciones alto valor)
- [P234] **DEFINICIÓN** — CRISP-DM: 6 fases cíclicas: comprensión negocio, comprensión datos, preparación, modelado, evaluación, despliegue
- [P235] **DEFINICIÓN** — ETL = Extract, Transform, Load; gramática: select, filter, mutate, arrange, group by, summarize, join
- [P236] **DEFINICIÓN** — métodos ML: decision trees, neural networks, SVM, ensemble (random forests, boosting), Bayesian networks
- [P237] **DEFINICIÓN** — ROC curve: false-positive vs true-positive; AUC 0.5 = azar; k-fold cross-validation (k=10 común)
- [P238] **HECHO** — Conway data science Venn: programación + matemáticas/estadística + expertise dominio
- [P239] **DEFINICIÓN** — data governance = toma decisiones autoridad datos; estructuras, reglas, derechos decisión, accountability; DGI 10 componentes
- [P240] **HECHO** — Floridi & Cowls 5 principios AI ético: beneficencia, no-maleficencia, autonomía, justicia, explicabilidad
- [P241] **HECHO** — Buolamwini & Gebru (2018): error facial analysis mujeres negras 34.7% vs hombres blancos 0.8%

### Ch 24: Safety and Quality Initiatives

- [P242] **DEFINICIÓN** — calidad cuidado IOM (1990): grado servicios aumentan probabilidad resultados deseados consistentes conocimiento actual
- [P243] **DEFINICIÓN** — 6 aims IOM: safe, effective, patient-centered, timely, efficient, equitable
- [P244] **DEFINICIÓN** — Singh & Sittig Sociotechnical: 8 dimensiones CAS: hardware/software, contenido clínico, HCI, personas, workflow, políticas, regulaciones, medición
- [P245] **HECHO** — 5 rights medicación: paciente, hora, droga, dosis, vía; BCMA/eMAR verifican vía barcoding
- [P246] **HECHO** — smart infusion pumps: adopción duplicó 2005-2012; 77% hospitales US (ASHP 2012)
- [P247] **DEFINICIÓN** — workarounds = uso sistema fuera protocolo diseñado; más comunes implementación; crean nuevas rutas error
- [P248] **HECHO** — CMS: HACs prevenibles sin pago adicional (Deficit Reduction Act 2006): úlceras presión, caídas con lesión
- [P249] **DEFINICIÓN** — interoperabilidad semántica = datos intercambiados sin pérdida contexto/significado; requiere mismos estándares todas organizaciones

### Ch 25: Informatics in the Curriculum

- [P250] **HECHO** — ANA reconoció nursing informatics especialidad 1992; integra nursing + computer + information science
- [P251] **HECHO** — AACN 2021 Essentials Domain 8: Informatics Healthcare Technologies, 4 competencias
- [P252] **HECHO** — ACGME clinical informatics fellowship: 5 milestone levels; sub-competencias: seguridad, CDS, project management, lifecycle
- [P253] **HECHO** — EU*US eHealth Work 2017: brechas principales = falta conocimiento proveedores, falta conocimiento facultad, disponibilidad cursos
- [P254] **HECHO** — certificaciones: ANCC (nursing), ABMS (medical), CPHIMS/HIMSS, CHIME CHCIO, AMIA AIIC (interprofesional)
- [P255] **HECHO** — ONC 2010 estimó déficit 51,000 trabajadores HIT; $84M 16 universidades entrenar >50,000 profesionales
- [P256] **HECHO** — primeros EHRs 1960s Mayo Clinic; 1965: ~73 proyectos info hospital/clínica

### Ch 26: Distance Education

- [P257] **DEFINICIÓN** — educación distancia: profesor/aprendiz separados localización; asíncrono/síncrono/blended
- [P258] **DEFINICIÓN** — eLearning: solo medios electrónicos/internet; mLearning: dispositivo móvil just-in-time
- [P259] **DEFINICIÓN** — Community of Inquiry: social presence + cognitive presence + teaching presence
- [P260] **DEFINICIÓN** — VARK: Visual, Aural, Read/Write, Kinesthetic; validado instrumento confiable
- [P261] **HECHO** — TEACH Act 2002: materiales copyrighted educación distancia bajo condiciones; FERPA: confidencialidad registros educacionales
- [P262] **HECHO** — Quality Matters = proceso peer review certificar calidad cursos online/blended

## Section 6: Data Governance, Legal, and Regulatory Issues

### Ch 27: Legal Issues, Federal Regulations, and Accreditation

- [P263] **REGLA** — ley federal preempta ley estatal conflictiva a menos ley estatal provea mayores protecciones (e.g., California CMIA > HIPAA)
- [P264] **HECHO** — dos agencias acreditación hospital: TJC y DNV Healthcare
- [P265] **HECHO** — FDA regula drogas/dispositivos médicos; CMS regulaciones Medicare/Medicaid; ONC estándares/certificación EHR; OCR enforce HIPAA/HITECH; DOJ enforce FCA/Anti-Kickback
- [P266] **DEFINICIÓN** — Stark law (1992): prohíbe médicos referir pacientes DHS entidades con relación financiera; triggers: ownership/inversión o compensación
- [P267] **ALCANCE** — DHS Stark: lab clínico, terapia física/ocupacional, radiología, DME, home health, Rx ambulatorio, servicios hospital
- [P268] **DEFINICIÓN** — Anti-Kickback statute: criminal, prohíbe intercambio valor inducir referencia beneficiario federal; hasta $25,000 + 5 años prisión + exclusión; civiles = triple daños + $50,000/violación
- [P269] **REQUISITO** — safe harbor Anti-Kickback: acuerdos escritos >1 año, servicios especificados, pago anticipado fair market value no considerando volumen referrals
- [P270] **HECHO** — EHR donation safe harbor (2006/2021): donor paga hasta 85% costo EHR; cybersecurity safe harbor: donor 100%
- [P271] **DEFINICIÓN** — FCA: responsabilidad civil claims falsos gobierno federal; 3x monto + $11,000/claim; Qui Tam: ciudadanos privados enforcement
- [P272] **REGLA** — PPACA: proveedor recibiendo sobrepago Medicare tiene 60 días reportar/devolver antes responsabilidad FCA
- [P273] **HECHO** — TJC Sentinel Event Alert 54 (2015): >3375 eventos adversos; 1/3 interfaz humano-computador, workflow, diseño CDS
- [P274] **HECHO** — clases dispositivos médicos FDA: Class I 47%, Class II 43%, Class III 10%
- [P275] **HECHO** — FDA "General Wellness" (2015): no regulará wearables wellness general; test: (1) solo claims wellness, (2) sin riesgos seguridad
- [P276] **HECHO** — IMLC + eNLC creados facilitar telehealth cross-state preservando regulación estatal
- [P277] **HECHO** — apps mHealth no covered entities HIPAA → sin prohibición federal recolección/divulgación PHI por apps

### Ch 28: Privacy and Security

- [P278] **DEFINICIÓN** — privacidad = derecho controlar acceso persona/información; confidencialidad = info no divulgada no autorizados; seguridad = proteger info CIA
- [P279] **HECHO** — FIPPs (1970s): 8 principios internacionales: transparencia, participación, propósito, minimización, limitación uso, calidad, seguridad, accountability
- [P280] **DEFINICIÓN** — HIPAA = autoridad legal primaria US privacidad salud; 3 reglas: Privacy, Security, Breach Notification; solo covered entities
- [P281] **DEFINICIÓN** — PHI = info condición salud/healthcare/pago identificando persona; solo para treatment-related o con autorización escrita
- [P282] **REGLA** — Security Rule: PHI electrónica requiere risk analysis regulares, protocolos malware, access controls
- [P283] **DEFINICIÓN** — breach = acceso/uso PHI no permitido comprometiendo seguridad; presuntivamente requiere notificación HHS + individuos + media
- [P284] **PLAZO** — derecho acceso: proveedores cumplir ≤30 días; 1 extensión notificación escrita
- [P285] **HECHO** — penalidades HIPAA: Cat 1 $100-$50K/$25K año; Cat 2 $1K-$50K/$100K; Cat 3 $10K-$50K/$250K; Cat 4 $50K min/$1.5M
- [P286] **REGLA** — HITECH extendió HIPAA a business associates; mejoró risk assessment/breach notification; derecho PHI electrónica
- [P287] **HECHO** — PSQIA 2005: repositorio datos de-identificados errores médicos; datos privilegiados para litigios; participación voluntaria
- [P288] **HECHO** — GINA (2008): prohíbe discriminación seguro/empleo basada info genética; no aplica seguros vida/discapacidad/cuidado largo plazo
- [P289] **EXCLUSIÓN** — GINA no aplica condiciones diagnosticadas/síntomas, solo información genética no manifestada
- [P290] **HECHO** — BIPAs solo 3 estados: Illinois (private right action), Texas, Washington
- [P291] **HECHO** — GDPR EU 2016: notificación breach ≤72h; Art.17 derecho ser olvidado; LGPD Brasil 2018; APPI Japón 2003; PIPL China 2021

### Ch 29: MACRA and Interoperability

- [P292] **DEFINICIÓN** — MACRA (2015) Quality Payment Program: MIPS + Advanced APMs
- [P293] **HECHO** — Promoting Interoperability: Stage 1 (captura datos), Stage 2 (procesos clínicos), Stage 3 (resultados, 2017+)
- [P294] **DEFINICIÓN** — information blocking = interferencia acceso/intercambio/uso EHI; aplica proveedores, desarrolladores HIT, exchanges
- [P295] **HECHO** — Information Blocking Rule mayo 2020; 8 excepciones; penalidades hasta $1M/violación desarrolladores; proveedores TBD
- [P296] **REQUISITO** — Patient Access API: claims adjudicados, encounters, datos clínicos/lab ≤1 día hábil post-adjudicación
- [P297] **REQUISITO** — Provider Directory API: nombres/direcciones/especialidades ≤30 días; payer-to-payer exchange USCDI v1 ene 2022
- [P298] **REQUISITO** — hospitales enviar notificaciones registro/admisión/alta/transferencia proveedores post-acute/primario
- [P299] **REQUISITO** — ONC Cures Act Final Rule: HL7 FHIR R4 + SMART (OAuth 2.0); USCDI alcance EHI vía API certificada
- [P300] **REQUISITO** — registros médicos hospital retenidos forma original ≥5 años

### Ch 30: Health Policy and Health Informatics

- [P301] **HECHO** — National Coordinator HIT creado 2004 Executive Order; codificado HITECH 2009
- [P302] **HECHO** — ONC 2020-2025: 4 goals: salud/bienestar, cuidado, ecosistema datos, conectar healthcare datos
- [P303] **HECHO** — HITECH = inversión $49B vía ARRA acelerar adopción HIT
- [P304] **HECHO** — MACRA eliminó Sustainable Growth Rate; Advancing Care Information = 25% MIPS Final Score
- [P305] **HECHO** — IOM 1999 estimó 98,000 vidas/año errores hospitalarios; 2011 recomendó HHS/ONC Health IT Safety Council

### Ch 31: Health IT Governance

- [P306] **DEFINICIÓN** — health IT governance = estructuras/procesos asegurando alineación IT objetivos estratégicos + priorización recursos limitados
- [P307] **HECHO** — componentes core: propuestas proyecto formales, planificar futuro, evaluar/priorizar, aprobar financiamiento, monitorear ROI
- [P308] **HECHO** — estructura: board + executive → comité governance IT clínico (CMO, CNO, CMIO, CNIO, CIO) → comités operacionales
- [P309] **HECHO** — Gartner bimodal IT: Mode 1 operaciones predecibles; Mode 2 innovación exploratoria; governance habilita ambos
- [P310] **HECHO** — 21st Century Cures Act habilita innovaciones third-party integrarse directamente EHR

## Section 7: Global and Future Perspectives in Health Informatics

### Ch 32: Global Health Informatics

- [P311] **HECHO** — 2021: ~4.6B usuarios internet = 59% global; 93% acceso mobile-broadband (ITU)
- [P312] **HECHO** — LDCs: 17% rural sin cobertura mobile; 72% hogares urbanos internet vs ~38% rural
- [P313] **HECHO** — 10% incremento velocidad internet → 1.3% crecimiento económico LMICs
- [P314] **DEFINICIÓN** — GHI = informática empoderar personas usar tecnología apropiada soluciones info perspectiva global healthcare todos
- [P315] **HECHO** — WHO WHA58.28 (2005), WHA66.24 (2013), WHA71.7 (2018): resoluciones estrategias eHealth/digital health
- [P316] **HECHO** — Global Strategy Digital Health 2020-2025 endosada WHA73; 4 objetivos: colaboración, estrategias nacionales, governance, people-centered
- [P317] **⚠ TENSIÓN** — AI en LMICs: sesgos étnicos/socioeconómicos/género desarrollo, necesidad protocolos datos locales, interoperabilidad
- [P318] **DEFINICIÓN** — cloud computing: SaaS, PaaS, IaaS (NIST); IoT: dispositivos wireless interrelacionados sin interacción humana
- [P319] **HECHO** — OpenMRS: EHR open-source Regenstrief+Partners in Health, Kenya; Bahmni: OpenMRS+OpenELIS+Odoo, India/Bangladesh/Nepal
- [P320] **HECHO** — DHIS2: open-source University Oslo 1994; mejoró reporting inmunización/ANC Uganda/Kenya
- [P321] **HECHO** — SMS = herramienta mHealth más común; India IDSP 2004; IDSR mayoría países africanos
- [P322] **REQUISITO** — 5 áreas escalar digital health LMICs: beneficios tangibles, engagement stakeholders, simplicidad técnica, infraestructura, política+financiamiento

### Ch 33: Informatics and the Future of Healthcare

- [P323] **HECHO** — gasto healthcare US: crecimiento 5.4%/año; $6.2T 2028; población ≥60: 600M (2000) → >2B (2050)
- [P324] **HECHO** — 2030: seniors US +55%; 1M enfermeros retirados 2017-2030; déficit 40,800-104,900 médicos
- [P325] **DEFINICIÓN** — person-centered health: 6 principios: whole-person, respeto, elección, dignidad, auto-determinación, vida propositiva
- [P326] **DEFINICIÓN** — SDOH = factores no-médicos influenciando resultados: educación, inseguridad alimentaria, acceso servicios (WHO 2017)
- [P327] **HECHO** — >1/3 organizaciones healthcare target ransomware 2020; UVM Medical Center bloqueado 1 mes, ~$50M
- [P328] **⚠ TENSIÓN** — usabilidad EHR vinculada burnout médicos/enfermeros; Mandl & Kohane: vendors propagaron mito complejidad (NEJM 2012)
- [P329] **HECHO** — USCDI = estándar datos vendors EHR exponen vía API; catalizador nuevos modelos cuidado
- [P330] **HECHO** — 21st Century Cures Act: information blocking con penalidades + interoperabilidad semántica; integra FHIR, LOINC, ICD, SNOMED
- [P331] **DEFINICIÓN** — LHS (IOM/NAM, 2007): ciencia/informática/incentivos/cultura alineados mejora continua; best practices embebidas; conocimiento como by-product
- [P332] **⚠ TENSIÓN** — modelos ML pueden resultar mayor inequidad asignación recursos; técnicas necesarias reducir sesgo proteger poblaciones vulnerables
- [P333] **DEFINICIÓN** — ML interpretability = explicar predicciones manera humano entienda; construye confianza clínica + habilita override
- [P334] **HECHO** — nuevos roles HIT: Chief Clinical Informatics Officer, Chief Innovation Officer, Chief Digital Officer, Chief Data Scientist
