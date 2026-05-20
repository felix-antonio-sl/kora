---
_manifest:
  urn: urn:hi:kb:atomic-health-informatics-fundamental-04
  provenance:
    created_by: FS
    created_at: '2026-04-23'
    source: artifacts/knowledge/_SCRIPTORIUM/INBOX/hi/hi.md — atomizacion del Fundamental
      Knowledge in Health Informatics; output de /atomize 2026-04-10
version: 1.0.0
status: borrador
tags:
- atomic
- health-informatics
- fundamental-knowledge
- hi
lang: es
extensions:
  kora:
    family: atomic
    atomic:
      n_propositions: 147
      producer: urn:kora:artefacto:atomize
      source_corpus: Fundamental Knowledge in Health Informatics (curso HI)
      segmented: true
      segment_role: segment
      hand_edited: true
      segment_index: 4
      segment_count: 4
---

# Fundamental Knowledge in Health Informatics - Segmento 04

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `../../INBOX/hi/hi.md`
- Proposiciones: `147`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `04/04`
- Rango: `P601-P747`

## Indice de fuentes

- `S01` · [hi.md](../../INBOX/hi/hi.md) · Fuente primaria del corpus atomizado

## Proposiciones

Segmento 04 del corpus atomizado.

- **P601** · `definition` · consentimiento informado requiere: capacidad tomar decisiones, información suficiente comprensión paciente razonable, consentimiento voluntario sin fraude/coacción · [src:S01](../../INBOX/hi/hi.md)
- **P602** · `definition` · HIPAA = autoridad legal primaria US privacidad información salud; aplica solo covered entities: proveedores healthcare, clearinghouses, planes salud · [src:S01](../../INBOX/hi/hi.md)
- **P603** · `definition` · HIPAA tiene 3 reglas amplias: Privacy Rule, Security Rule, Breach Notification Rule · [src:S01](../../INBOX/hi/hi.md)
- **P604** · `definition` · PHI = información relacionada condición salud física/mental individuo, healthcare provisto/recomendado, o información pago, que identifica/puede razonablemente identificar persona específica · [src:S01](../../INBOX/hi/hi.md)
- **P605** · `rule` · PHI solo puede usarse razones treatment-related permitidas Privacy Rule o con autorización escrita individuo · [src:S01](../../INBOX/hi/hi.md)
- **P606** · `rule` · HIPAA Security Rule aplica PHI electrónica; requiere covered entities conducir análisis riesgo regulares, minimizar vulnerabilidades, tener protocolos detectar/prevenir software malicioso, usar access controls · [src:S01](../../INBOX/hi/hi.md)
- **P607** · `definition` · breach (45 CFR 164.402) = adquisición/acceso/uso/divulgación PHI manera no permitida comprometiendo seguridad/privacidad; cualquier uso impermisible presuntivamente breach requiriendo notificación · [src:S01](../../INBOX/hi/hi.md)
- **P608** · `rule` · notificación breach requerida a: HHS, individuos afectados, y dependiendo circunstancias, público vía media · [src:S01](../../INBOX/hi/hi.md)
- **P609** · `definition` · designated record set = registros médicos/facturación + info seguro salud/gestión claims + otros registros usados toma decisiones; excluye notas psicoterapia + info procedimientos legales · [src:S01](../../INBOX/hi/hi.md)
- **P610** · `deadline` · proveedores deben cumplir solicitudes derecho acceso ≤30 días calendario; una extensión permitida si notificación escrita provista con razón/fecha · [src:S01](../../INBOX/hi/hi.md)
- **P611** · `definition` · business associate = individuo/organización separado covered entity realizando servicios involucrando PHI; debe firmar business associate agreements delineando usos/divulgaciones permisibles PHI · [src:S01](../../INBOX/hi/hi.md)
- **P612** · `fact` · OCR enforce HIPAA; quejas deben presentarse ≤180 días; organización tiene 30 días después notificación presentar evidencia defensa · [src:S01](../../INBOX/hi/hi.md)
- **P613** · `fact` · categorías penalidad HIPAA: Cat 1 (no sabía) = $100-$50,000/violación, $25,000/año; Cat 2 (no negligencia willful) = $1,000-$50,000, $100,000/año; Cat 3 (negligencia willful, remediada ≤30 días) = $10,000-$50,000, $250,000/año; Cat 4 (negligencia willful, no remediada) = $50,000 min, $1,500,000/año · [src:S01](../../INBOX/hi/hi.md)
- **P614** · `fact` · HITECH promulgada 2009; HHS Final Rule implementar no hasta 2013; destinada impulsar adopción EHR proveyendo privacidad/seguridad · [src:S01](../../INBOX/hi/hi.md)
- **P615** · `fact` · HITECH implementó "meaningful use program" proveyendo incentivos monetarios implementación EHR; término reemplazado CMS "promoting interoperability" · [src:S01](../../INBOX/hi/hi.md)
- **P616** · `rule` · HITECH extendió reglas privacidad/seguridad HIPAA a business associates; mejoró requerimientos risk assessment + breach notification; proveyó derecho obtener PHI forma electrónica · [src:S01](../../INBOX/hi/hi.md)
- **P617** · `fact` · PSQIA 2005: legislación federal creando repositorio datos salud paciente de-identificados para investigación/revisión errores cuidado médico; participación voluntaria · [src:S01](../../INBOX/hi/hi.md)
- **P618** · `rule` · datos recolectados bajo PSQIA establecidos como work product privilegiado para litigios estatal/federal; organizaciones seguridad paciente no pueden divulgar datos a menos de-identificados · [src:S01](../../INBOX/hi/hi.md)
- **P619** · `fact` · GINA promulgada 2008; prohíbe discriminación cobertura seguro salud y empleo basada información genética individuo · [src:S01](../../INBOX/hi/hi.md)
- **P620** · `scope` · GINA Title I: prohíbe aseguradores salud solicitar/requerir información genética o usarla decisiones seguros; Title II: prohíbe empleadores usar información genética decisiones empleo · [src:S01](../../INBOX/hi/hi.md)
- **P621** · `exclusion` · GINA no aplica seguros vida, seguros discapacidad, o seguros cuidado largo plazo; no aplica condiciones salud diagnosticadas/síntomas, solo información genética misma · [src:S01](../../INBOX/hi/hi.md)
- **P622** · `definition` · biometric identifiers = datos biológicos usados identificar individuo: huellas dactilares, geometría facial, scans retina/iris, voiceprints · [src:S01](../../INBOX/hi/hi.md)
- **P623** · `fact` · solo 3 estados aprobaron BIPAs: Illinois, Texas, Washington; Illinois BIPA incluye private right of action · [src:S01](../../INBOX/hi/hi.md)
- **P624** · `definition` · ransomware = malware diseñado extorsionar pagos rescate infectando computador, deshabilitando funciones, demandando pago restaurar funcionalidad · [src:S01](../../INBOX/hi/hi.md)
- **P625** · `fact` · GDPR aprobada EU 2016; requiere: informar pacientes uso datos, usar solo propósito legítimo, retener solo hasta propósito completado, notificación breach ≤72 horas · [src:S01](../../INBOX/hi/hi.md)
- **P626** · `fact` · GDPR Article 17 = derecho ser olvidado: organizaciones deben borrar información salud upon request si propósito cumplido/solo usado marketing/consentimiento revocado · [src:S01](../../INBOX/hi/hi.md)
- **P627** · `fact` · Canadá PIPEDA: ley protección datos salud primaria; 10 principios equitativos: accountability, identificación propósitos, consentimiento, limitar recolección, limitar uso/divulgación/retención, precisión, salvaguardas, apertura, acceso individual, desafiar cumplimiento · [src:S01](../../INBOX/hi/hi.md)
- **P628** · `fact` · Brasil LGPD aprobada agosto 14, 2018; modelada GDPR; define datos personales incluir datos salud/genéticos/biométricos · [src:S01](../../INBOX/hi/hi.md)
- **P629** · `fact` · Japón APPI aprobada 2003; una primeras leyes privacidad asiáticas; estableció Personal Information Protection Commission (PPC) · [src:S01](../../INBOX/hi/hi.md)
- **P630** · `fact` · China Cybersecurity Law aprobada nov 6, 2016, efectiva junio 2017; PRC aprobó PIPL agosto 20, 2021, efectiva nov 1, 2021 · [src:S01](../../INBOX/hi/hi.md)

### Ch 29: MACRA and Interoperability

- **P631** · `fact` · CMS estableció Medicare/Medicaid EHR Incentive Programs 2011 (ahora Promoting Interoperability Programs) incentivar adopción/meaningful use CEHRT · [src:S01](../../INBOX/hi/hi.md)
- **P632** · `fact` · Stage 1: fundamento captura electrónica datos clínicos + proveer pacientes copias electrónicas info salud · [src:S01](../../INBOX/hi/hi.md)
- **P633** · `fact` · Stage 2: procesos clínicos avanzados, intercambio datos estructurados, alineado National Quality Strategy · [src:S01](../../INBOX/hi/hi.md)
- **P634** · `fact` · Stage 3 (oct 2015 final rule, efectiva 2017+): enfocado usar CEHRT mejorar resultados salud · [src:S01](../../INBOX/hi/hi.md)
- **P635** · `definition` · MACRA (2015) estableció Quality Payment Program; dos tracks: (1) MIPS y (2) Advanced Alternative Payment Models (APMs) · [src:S01](../../INBOX/hi/hi.md)
- **P636** · `fact` · categoría MIPS Promoting Interoperability enfoca meaningful use tecnología EHR certificada · [src:S01](../../INBOX/hi/hi.md)
- **P637** · `fact` · ONC 2015 Congressional Report concluyó information blocking = problema serio; recomendó Congreso prohibirlo con penalidades/enforcement · [src:S01](../../INBOX/hi/hi.md)
- **P638** · `fact` · 21st Century Cures Act promulgada marzo 9, 2020; HHS/CMS promulgaron Information Blocking Rule (CMS Interoperability and Patient Access Rule) · [src:S01](../../INBOX/hi/hi.md)
- **P639** · `definition` · information blocking = interferencia con/prevención de/desaliento material acceso/intercambio/uso información salud electrónica; aplica proveedores healthcare, desarrolladores HIT, exchanges, networks · [src:S01](../../INBOX/hi/hi.md)
- **P640** · `fact` · Information Blocking Rule adoptada mayo 1, 2020; requerimientos efectivos ene 1, 2021 o ene 2022; aplica MA organizations, Medicaid FFS, Medicaid managed care, CHIP managed care, QHP issuers · [src:S01](../../INBOX/hi/hi.md)
- **P641** · `requirement` · aseguradores salud deben hacer disponible Patient Access API incluyendo claims adjudicados, encounters proveedores capitated, datos clínicos/resultados lab no más 1 día hábil después claim adjudicado · [src:S01](../../INBOX/hi/hi.md)
- **P642** · `requirement` · Provider Directory API debe incluir nombres/direcciones/teléfonos/especialidades proveedores + datos directorio farmacia; disponible ≤30 días calendario recibir info directorio proveedor · [src:S01](../../INBOX/hi/hi.md)
- **P643** · `requirement` · intercambio datos payer-to-payer: planes salud aplicables deben intercambiar datos USCDI v1 solicitud enrollee; datos con fecha servicio desde ene 1, 2016; implementación completa ene 1, 2022 · [src:S01](../../INBOX/hi/hi.md)
- **P644** · `requirement` · hospitales con registros médicos electrónicos deben enviar notificaciones registro/admisión/alta/transferencia paciente a proveedores post-acute care, practicantes cuidado primario, otros practicantes identificados · [src:S01](../../INBOX/hi/hi.md)
- **P645** · `fact` · 8 excepciones Information Blocking Rule: preventing harm, privacy, security, infeasibility, health IT performance, content/manner, fees, licensing · [src:S01](../../INBOX/hi/hi.md)
- **P646** · `fact` · Cures Act: desarrolladores HIT/redes/exchanges información salud sujetos penalidades monetarias civiles hasta $1M por violación information blocking; penalidades proveedores vía "appropriate disincentives" TBD · [src:S01](../../INBOX/hi/hi.md)
- **P647** · `requirement` · ONC Cures Act Final Rule requiere uso estándar HL7 FHIR (Release 4) + SMART Application Launch Framework (OAuth 2.0); establece USCDI como alcance EHI paciente vía API certificada · [src:S01](../../INBOX/hi/hi.md)
- **P648** · `requirement` · desarrolladores API certificados deben publicar términos/condiciones + documentación business/técnica públicamente vía hyperlink; deben soportar servicios API-enabled single-patient y multi-patient · [src:S01](../../INBOX/hi/hi.md)
- **P649** · `requirement` · planes salud aplicables deben participar trusted exchange networks capaces: intercambiar PHI entre jurisdicciones; conectar EHRs inpatient/ambulatorio; soportar mensajería segura/querying electrónico · [src:S01](../../INBOX/hi/hi.md)
- **P650** · `requirement` · registros médicos hospital deben retenerse forma original/legalmente reproducida ≥5 años · [src:S01](../../INBOX/hi/hi.md)
- **P651** · `requirement` · excepción infeasibility: actor debe proveer respuesta escrita solicitante ≤10 días hábiles explicando por qué solicitud infeasible · [src:S01](../../INBOX/hi/hi.md)
- **P652** · `requirement` · excepción licensing: actor debe comenzar negociaciones licencia ≤10 días hábiles de solicitud; negociar licencia ≤30 días hábiles · [src:S01](../../INBOX/hi/hi.md)

### Ch 30: Health Policy and Health Informatics

- **P653** · `definition` · health policy = define objetivos salud nivel internacional/nacional/local; especifica decisiones/planes/acciones alcanzar objetivos · [src:S01](../../INBOX/hi/hi.md)
- **P654** · `fact` · policy no es ley; policy guía/delinea qué hacer alcanzar objetivo; leyes son estándares/principios/procedimientos que deben seguirse · [src:S01](../../INBOX/hi/hi.md)
- **P655** · `fact` · IOM 2001 report delineó preocupaciones calidad disminuida, costos excesivos, errores evitables; llamó nuevas herramientas/métodos incluyendo adopción EHR universal · [src:S01](../../INBOX/hi/hi.md)
- **P656** · `fact` · organizaciones stakeholder HIT incluyen HIMSS, AMIA, AHIMA, AMDIS, ANI, JPHIT, más vendors EHR/tecnología · [src:S01](../../INBOX/hi/hi.md)
- **P657** · `fact` · posición National Coordinator for HIT creada 2004 vía Executive Order; codificada HITECH Act 2009 · [src:S01](../../INBOX/hi/hi.md)
- **P658** · `fact` · ONC 2020-2025 Federal Health IT Strategic Plan: 4 goals = (1) promover salud/bienestar, (2) mejorar prestación/experiencia cuidado, (3) construir ecosistema datos seguro investigación/innovación, (4) conectar healthcare con datos salud · [src:S01](../../INBOX/hi/hi.md)
- **P659** · `fact` · HITECH = inversión $49B vía ARRA 2009 acelerar adopción HIT calidad/seguridad/eficiencia · [src:S01](../../INBOX/hi/hi.md)
- **P660** · `fact` · tres etapas Meaningful Use: Stage 1 (2011) captura datos/compartición; Stage 2 (2014) procesos clínicos/HIE/ePrescription/acceso paciente; Stage 3 (2017) reemplazado "Advancing Care Information" bajo MACRA · [src:S01](../../INBOX/hi/hi.md)
- **P661** · `fact` · 2015: 84% hospitales non-federal acute care adoptaron al menos EHR básico con notas clínicas · [src:S01](../../INBOX/hi/hi.md)
- **P662** · `fact` · MACRA eliminó fórmula Sustainable Growth Rate; todos médicos elegibles MIPS pero sujetos penalidades; "Advancing Care Information" = 25% MIPS Final Score · [src:S01](../../INBOX/hi/hi.md)
- **P663** · `fact` · IOM 1999 "To Err Is Human" estimó hasta 98,000 vidas perdidas anualmente por errores médicos hospitalarios · [src:S01](../../INBOX/hi/hi.md)
- **P664** · `fact` · 2011 IOM "HIT and Patient Safety" report: recomendó HHS asegurar vendors soporten libre intercambio experiencias HIT; ONC trabaje sector privado experiencias usuario comparativas; HHS financie Health IT Safety Council · [src:S01](../../INBOX/hi/hi.md)
- **P665** · `fact` · AHRQ publicó National Quality Strategy marzo 2011: primer framework nacional mejora calidad reconociendo HIT como crítico · [src:S01](../../INBOX/hi/hi.md)

### Ch 31: Health Information Technology Governance

- **P666** · `definition` · health IT governance = estructuras/procesos organizacionales asegurando alineación IT con objetivos estratégicos institucionales + priorización efectiva recursos IT limitados · [src:S01](../../INBOX/hi/hi.md)
- **P667** · `fact` · dos necesidades fundamentales impulsando health IT governance: (1) asegurar alineación recursos IT con prioridades institucionales; (2) priorizar efectivamente recursos IT entre demandas competitivas · [src:S01](../../INBOX/hi/hi.md)
- **P668** · `fact` · componentes core health IT governance: procesos propuesta proyecto formales, planificar direcciones futuras, evaluar/priorizar proyectos, aprobar financiamiento, monitorear ROI · [src:S01](../../INBOX/hi/hi.md)
- **P669** · `fact` · estructura governance muestra: board directors + executive management → comité governance IT clínico (CMO, CNO, CMIO, CNIO, CIO, COO, CFO, chairs departamento) → varios comités operacionales · [src:S01](../../INBOX/hi/hi.md)
- **P670** · `rule` · health IT governance debería ser independiente elecciones tecnología específicas; governance debería guiar selección tecnología · [src:S01](../../INBOX/hi/hi.md)
- **P671** · `fact` · concepto "bimodal IT" Gartner: Mode 1 = operaciones predecibles; Mode 2 = innovación exploratoria; governance debe habilitar ambos · [src:S01](../../INBOX/hi/hi.md)
- **P672** · `fact` · punto partida governance recomendado: evaluar estructura/cultura IT actual usando análisis SWOT; investigar enfoques organizaciones pares · [src:S01](../../INBOX/hi/hi.md)
- **P673** · `fact` · 21st Century Cures Act (2016) habilita innovaciones third-party digital health integrarse directamente con EHR y su interfaz usuario · [src:S01](../../INBOX/hi/hi.md)
- **P674** · `requirement` · charter governance debería proveer principios guía, alcance responsabilidades, membresía comité, procesos, toma decisiones; impacto debería evaluarse activamente incluyendo consecuencias no intencionadas · [src:S01](../../INBOX/hi/hi.md)

## Section 7: Global and Future Perspectives in Health Informatics

### Ch 32: Global Health Informatics

- **P675** · `fact` · 2021: ~4.6B usuarios internet activos = 59% población global (ITU 2021) · [src:S01](../../INBOX/hi/hi.md)
- **P676** · `fact` · 93% población mundial tiene acceso red mobile-broadband (ITU 2021) · [src:S01](../../INBOX/hi/hi.md)
- **P677** · `fact` · cobertura red 4G aumentó 2x globalmente entre 2015-2020 · [src:S01](../../INBOX/hi/hi.md)
- **P678** · `fact` · en LDCs, 17% población rural sin cobertura mobile; 19% rural cubierta solo por 2G (ITU 2021) · [src:S01](../../INBOX/hi/hi.md)
- **P679** · `fact` · 72% hogares urbanos tenían acceso internet hogar (2019) vs ~38% rural globalmente · [src:S01](../../INBOX/hi/hi.md)
- **P680** · `fact` · 10% incremento velocidad internet → 1.3% incremento crecimiento económico en LMICs · [src:S01](../../INBOX/hi/hi.md)
- **P681** · `definition` · eHealth = plataformas electrónicas provisión información/servicios salud, recolección/gestión datos; cuando usado teléfonos móviles = mHealth · [src:S01](../../INBOX/hi/hi.md)
- **P682** · `definition` · digital health expande eHealth incluir consumidores digitales, dispositivos smart/conectados; alcance incluye mHealth, HIT, wearables, telehealth/telemedicine, medicina personalizada · [src:S01](../../INBOX/hi/hi.md)
- **P683** · `definition` · GHI (Global health informatics) = disciplina informática enfocada empoderar personas usar tecnología apropiada soluciones basadas información perspectiva global soportando healthcare para todos (Richards et al. 2013) · [src:S01](../../INBOX/hi/hi.md)
- **P684** · `fact` · resolución WHO WHA58.28 (2005) urgió Member States desarrollar plan estratégico largo plazo servicios eHealth/infraestructura ICT · [src:S01](../../INBOX/hi/hi.md)
- **P685** · `fact` · resolución WHO WHA66.24 (2013) urgió Member States desarrollar políticas/mecanismos legislativos enlazados estrategia eHealth nacional + estandarización/interoperabilidad · [src:S01](../../INBOX/hi/hi.md)
- **P686** · `fact` · iniciativa Digital REACH lanzada 2017 East African Community: Burundi, Kenya, Rwanda, South Sudan, Tanzania, Uganda · [src:S01](../../INBOX/hi/hi.md)
- **P687** · `fact` · resolución WHO WHA71.7 (mayo 2018) sobre digital health → desarrollar estrategia global digital health · [src:S01](../../INBOX/hi/hi.md)
- **P688** · `fact` · UN Secretary General's High-Level Panel Digital Cooperation (2019) recomendó 2030 cada adulto debería tener acceso asequible redes digitales + servicios financieros/salud digitalmente habilitados · [src:S01](../../INBOX/hi/hi.md)
- **P689** · `fact` · Lancet / Financial Times joint Commission (oct 2019) enfocó convergencia digital health, AI, y cobertura universal salud · [src:S01](../../INBOX/hi/hi.md)
- **P690** · `fact` · Global Strategy Digital Health 2020-2025 endosada por WHA73 (2020) · [src:S01](../../INBOX/hi/hi.md)
- **P691** · `scope` · WHO Global Strategy Digital Health 2020-2025 tiene 4 objetivos estratégicos: (1) promover colaboración global/transferencia conocimiento, (2) avanzar estrategias digital health nacionales, (3) fortalecer governance global/regional/nacional, (4) abogar sistemas salud people-centered habilitados digital health · [src:S01](../../INBOX/hi/hi.md)
- **P692** · `fact` · término "artificial intelligence" acuñado 1956; rama computer science dealing simulación comportamiento inteligente computadores · [src:S01](../../INBOX/hi/hi.md)
- **P693** · `scope` · intervenciones salud AI-driven en LMICs encajan 4 categorías: (a) diagnóstico, (b) evaluación riesgo mortalidad/morbilidad, (c) predicción/vigilancia brotes enfermedad, (d) política/planificación salud · [src:S01](../../INBOX/hi/hi.md)
- **P694** · `tension` · AI en LMICs enfrenta desafíos: diseño apropiado impulsado necesidades locales, sesgos étnicos/socioeconómicos/género durante desarrollo, necesidad nuevos protocolos compartición datos e interoperabilidad · [src:S01](../../INBOX/hi/hi.md)
- **P695** · `definition` · ML = proceso a través del cual computadores/modelos/algoritmos aprenden y mejoran de datos y procesos; usado clasificación, clustering, predicción · [src:S01](../../INBOX/hi/hi.md)
- **P696** · `definition` · cloud computing = usar red servidores remotos almacenar/gestionar/acceder/procesar datos; 3 modelos servicio: SaaS, PaaS, IaaS (NIST) · [src:S01](../../INBOX/hi/hi.md)
- **P697** · `definition` · IoT = sistema dispositivos digitales wireless, interrelacionados, conectados que recolectan/envían/almacenan datos sobre red sin requerir interacción humano-a-humano o humano-a-computador · [src:S01](../../INBOX/hi/hi.md)
- **P698** · `fact` · arquitectura IoT healthcare tiene 3 capas: (1) capa procesada/sensor, (2) capa red (wired/wireless), (3) capa aplicación · [src:S01](../../INBOX/hi/hi.md)
- **P699** · `constraint` · riesgo cyber es obstáculo principal adopción IoT amplia; privacidad paciente debe asegurarse prevenir identificación/rastreo no autorizado · [src:S01](../../INBOX/hi/hi.md)
- **P700** · `definition` · telehealth/telemedicine = uso dispositivos telecomunicación entrega remota cuidado médico; intercambiando información médica un sitio a otro vía comunicación electrónica · [src:S01](../../INBOX/hi/hi.md)
- **P701** · `requirement` · 7 componentes clave sistemas salud LMIC adoptar telemedicine: aprobaciones gobierno, identificación usuarios, elección plataforma tech, alineación incentivos financieros, definición workflows, training trabajadores salud, engagement paciente · [src:S01](../../INBOX/hi/hi.md)
- **P702** · `fact` · India Ministry Health publicó guías práctica telemedicina nacional marzo 2020 · [src:S01](../../INBOX/hi/hi.md)
- **P703** · `fact` · China publicó guías aumentando reembolso consultas follow-up online + entrega recetas puerta-a-puerta vía "internet hospitals" durante COVID-19 · [src:S01](../../INBOX/hi/hi.md)
- **P704** · `definition` · PHR = aplicación electrónica a través individuos acceden/gestionan/comparten info salud entorno privado/seguro/confidencial; 3 tipos: standalone, tethered, interconnected · [src:S01](../../INBOX/hi/hi.md)
- **P705** · `fact` · OpenMRS = EHR open-source liderado Regenstrief Institute + Partners in Health; implementado inicialmente Kenya · [src:S01](../../INBOX/hi/hi.md)
- **P706** · `fact` · Bahmni = software clínico integrado combinando OpenMRS (registros paciente) + OpenELIS (gestión lab) + OpenERP/Odoo (contabilidad hospital); desplegado India, Bangladesh, Nepal · [src:S01](../../INBOX/hi/hi.md)
- **P707** · `fact` · DHIS2 = plataforma open-source web-based recolección/validación/análisis datos salud; primera introducción University of Oslo 1994 · [src:S01](../../INBOX/hi/hi.md)
- **P708** · `fact` · implementación DHIS2 mejoró reporting cobertura inmunización, visitas ANC, tasa parto facility en Uganda y Kenya · [src:S01](../../INBOX/hi/hi.md)
- **P709** · `definition` · mHealth = práctica médica/salud pública soportada dispositivos móviles (WHO 2011) · [src:S01](../../INBOX/hi/hi.md)
- **P710** · `fact` · SMS = herramienta tecnología mHealth más común usada a través settings healthcare · [src:S01](../../INBOX/hi/hi.md)
- **P711** · `fact` · India lanzó Integrated Disease Surveillance Project (IDSP) formalmente 2004; IDSR implementado mayoría países africanos · [src:S01](../../INBOX/hi/hi.md)
- **P712** · `requirement` · 5 áreas enfoque críticas escalar digital health en LMICs: (1) características programa intrínsecas con beneficios tangibles, (2) engagement/training stakeholders, (3) simplicidad técnica/interoperabilidad/adaptabilidad, (4) infraestructura apropiada, (5) alineación política healthcare + financiamiento sostenible · [src:S01](../../INBOX/hi/hi.md)
- **P713** · `fact` · Health Data Collaborative (HDC) y Principles for Digital Development son partnerships globales enfocados estándares interoperabilidad · [src:S01](../../INBOX/hi/hi.md)
- **P714** · `fact` · Digital Impact Alliance (DIAL) y Digital Square buscan mejorar datos salud inversiones compartidas global goods escala digital health · [src:S01](../../INBOX/hi/hi.md)

### Ch 33: Informatics and the Future of Healthcare

- **P715** · `fact` · gasto healthcare US proyectado crecimiento anual 5.4% para 2019-2028; puede alcanzar $6.2 trillones 2028 · [src:S01](../../INBOX/hi/hi.md)
- **P716** · `fact` · proyecciones gasto US actuales $2.5 trillones menos originalmente proyectado por ACA + recesión late 2000s · [src:S01](../../INBOX/hi/hi.md)
- **P717** · `fact` · población global ≥60 años crecerá 600M (2000) → >2B (2050) (WHO 2011) · [src:S01](../../INBOX/hi/hi.md)
- **P718** · `fact` · enfermedad cardíaca isquémica = 16% muertes globales anualmente; diabetes global predicha aumentar 382M (2013) → 592M 2035 · [src:S01](../../INBOX/hi/hi.md)
- **P719** · `fact` · 2030: seniors US esperados aumentar 55% vs 2015; estimado 1M enfermeros retirados 2017-2030; déficit nacional 40,800-104,900 médicos esperado 2030 · [src:S01](../../INBOX/hi/hi.md)
- **P720** · `definition` · futures research (futurología) = estudio racional/sistemático futuro con objetivo identificar futuros posibles, probables, preferibles; enfoque 5-50 años adelante · [src:S01](../../INBOX/hi/hi.md)
- **P721** · `fact` · Toffler publicó "Future Shock" 1970 sobre adaptación/falla adaptación cambio; Naisbitt publicó "Megatrends" 1982 identificando 10 tendencias societales · [src:S01](../../INBOX/hi/hi.md)
- **P722** · `definition` · trend analysis = examinar datos históricos identificar tendencias tiempo; extrapolation = extender datos históricos futuro; patrón S-curve: crecimiento inicial lento → crecimiento rápido → desaceleración límite natural · [src:S01](../../INBOX/hi/hi.md)
- **P723** · `fact` · CMS + ONC crearon nuevas guidelines/políticas interoperabilidad, acceso paciente datos médicos, HIE mejorado usando estándares FHIR y USCDI · [src:S01](../../INBOX/hi/hi.md)
- **P724** · `definition` · person-centered health = término genérico abarcando person-centered care, patient-centered care, precision medicine, consumer-centered care; 6 principios: cuidado persona completa, respeto/valor, elección, dignidad, auto-determinación, vida propositiva · [src:S01](../../INBOX/hi/hi.md)
- **P725** · `definition` · precision (personalized) medicine = intervenciones salud tailored diferencias individuales específicas: genoma, ambientes, estilo vida · [src:S01](../../INBOX/hi/hi.md)
- **P726** · `fact` · mercado global apps mHealth valuado $40B (2020); tasa crecimiento esperada >17% desde 2021-2028 · [src:S01](../../INBOX/hi/hi.md)
- **P727** · `fact` · CMMI soportó Emergency Triage, Treat, and Transport (ET3) model permitiendo EMS proveer cuidado on-scene con control médico virtual real-time, potencialmente sin transporte hospital · [src:S01](../../INBOX/hi/hi.md)
- **P728** · `definition` · SDOH = factores no-médicos influenciando resultados salud incluyendo educación, inseguridad alimentaria, acceso servicios salud (WHO 2017) · [src:S01](../../INBOX/hi/hi.md)
- **P729** · `requirement` · ONC recomienda mejorar infraestructura soportar uso datos SDOH aplicaciones clínicas; sistemas salud necesitarán redes CBO comunicarse con EHRs integración significativa · [src:S01](../../INBOX/hi/hi.md)
- **P730** · `fact` · University Vermont Medical Center empleados bloqueados EHR casi 1 mes por ataque ransomware; impacto estimado ~$50M revenue perdido · [src:S01](../../INBOX/hi/hi.md)
- **P731** · `fact` · >1/3 organizaciones healthcare globalmente reportaron ser target ransomware 2020 (Sophos 2021) · [src:S01](../../INBOX/hi/hi.md)
- **P732** · `definition` · optimization (EHR) = esfuerzos iniciales y post-implementación incluyendo evaluaciones, training continuo, re-tailoring sistema; instalaciones no terminan con go-live sino transformación continua · [src:S01](../../INBOX/hi/hi.md)
- **P733** · `tension` · usabilidad EHR vinculada burnout proveedor médicos y enfermeros; Mandl & Kohane argumentan vendors propagaron mito complejidad precluding innovación (NEJM 2012) · [src:S01](../../INBOX/hi/hi.md)
- **P734** · `fact` · 21st Century Cures Act aborda information blocking (con penalidades) e interoperabilidad semántica; integra FHIR, LOINC, ICD, SNOMED política nacional · [src:S01](../../INBOX/hi/hi.md)
- **P735** · `fact` · USCDI = estándar datos todos vendors EHR requeridos exponer vía API; catalizador nuevos modelos cuidado desacoplados enfoques tradicionales sistema-healthcare-centrados · [src:S01](../../INBOX/hi/hi.md)
- **P736** · `fact` · solo ~2% pacientes actualmente usando apps mHealth integradas suites aplicación facility (Accenture 2015) · [src:S01](../../INBOX/hi/hi.md)
- **P737** · `definition` · human factors engineering (HFE) = disciplina científica enfocada interacción humanos/elementos sistema, enfatizando bienestar humano y rendimiento sistema; raíces mid-1900s aviación/diseño militar · [src:S01](../../INBOX/hi/hi.md)
- **P738** · `fact` · SEIPS 2.0 model = modelo sociotécnico proveyendo enfoque holístico factores healthcare: personas, organizaciones, herramientas/tecnología, ambiente interno, ambiente externo, tareas (Holden et al. 2013) · [src:S01](../../INBOX/hi/hi.md)
- **P739** · `fact` · IBM estima 2.5 quintillones bytes información generados por día globalmente · [src:S01](../../INBOX/hi/hi.md)
- **P740** · `definition` · predictive analytics = uso datos pasados predecir tendencias futuras; objetivo presentar datos decision makers tan cerca real time como posible · [src:S01](../../INBOX/hi/hi.md)
- **P741** · `definition` · Learning Healthcare System introducido 2007 US IOM (ahora National Academy Medicine) = sistema donde ciencia/informática/incentivos/cultura alineados mejora continua, best practices embebidas prestación, pacientes participantes activos, nuevo conocimiento capturado como by-product · [src:S01](../../INBOX/hi/hi.md)
- **P742** · `fact` · primera ola aplicaciones ML healthcare apuntó ineficiencias operacionales: NLP extracción billing codes, predicción length of stay, predicción tasas no-show · [src:S01](../../INBOX/hi/hi.md)
- **P743** · `tension` · modelos ML pueden resultar mayor inequidad asignación recursos healthcare; técnicas necesarias reducir sesgo y proteger poblaciones vulnerables mayor marginalización · [src:S01](../../INBOX/hi/hi.md)
- **P744** · `definition` · ML interpretability = cualquier método ML que puede explicar predicciones manera humano puede entender; modelos interpretables construyen confianza clínica + habilitan clinical override predicciones · [src:S01](../../INBOX/hi/hi.md)
- **P745** · `scope` · 3 niveles cambio (Nelson & Englebardt 2002): 1st-level = hace proceso existente más eficiente (menos disruptivo); 2nd-level = cambia cómo resultado logrado; 3rd-level = altera proceso y reenfoca objetivo (nivel societal/institucional) · [src:S01](../../INBOX/hi/hi.md)
- **P746** · `fact` · tendencias clinical informatics futuras agrupadas: (1) person-centered health, (2) tendencias técnicas (IoT, cybersecurity), (3) clinical informatics (beyond EHRs, UX, predictive analytics, visualización datos) · [src:S01](../../INBOX/hi/hi.md)
- **P747** · `fact` · nuevos roles liderazgo HIT emergiendo: Chief Clinical Informatics Officer, Chief Innovation Officer, Chief Digital Officer, Chief Content Officer, Chief Data Scientist · [src:S01](../../INBOX/hi/hi.md)
