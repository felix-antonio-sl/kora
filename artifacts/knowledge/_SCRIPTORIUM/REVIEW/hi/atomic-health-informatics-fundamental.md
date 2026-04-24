---
_manifest:
  urn: "urn:hi:kb:atomic-health-informatics-fundamental"
  provenance:
    created_by: "FS"
    created_at: "2026-04-23"
    source: "artifacts/knowledge/_SCRIPTORIUM/INBOX/hi/hi.md — atomizacion del Fundamental Knowledge in Health Informatics; output de /atomize 2026-04-10"
version: "1.0.0"
status: borrador
tags: [atomic, health-informatics, fundamental-knowledge, hi]
lang: es
extensions:
  kora:
    family: atomic
    atomic:
      n_propositions: 761
      producer: "urn:kora:artefacto:atomize"
      source_corpus: "Fundamental Knowledge in Health Informatics (curso HI)"
---

# Fundamental Knowledge in Health Informatics
<!-- /atomize · 761 proposiciones · ~480 entidades · 1 archivo · 2026-04-10 -->
<!-- Consultar: buscar por [P###], por tipo (DEFINICIÓN, HECHO, REGLA...), o por entidad -->

## Section 1: Fundamental Knowledge in Health Informatics

### Ch 1: An Introduction to Health Informatics

- [P001] **DEFINICIÓN** — health informatics: especialidad interdisciplinaria integrando ciencias salud, computación, información → gestionar/comunicar datos/información/conocimiento/sabiduría en atención sanitaria
- [P002] **HECHO** — IOM report "To Err is Human" (2000) discutió errores médicos, fundamentó necesidad tecnología para entender/reducir errores
- [P003] **HECHO** — "Crossing the Quality Chasm" (IOM, 2001) evidenció necesidad IT mejorar seguridad paciente, enfatizó EHRs, CDS, analytics, automatización
- [P004] **HECHO** — James (2013) estimó 440,000 estadounidenses hospitalizados/año experimentan eventos adversos prevenibles contribuyendo a muerte; daño grave 10-20x más común que daño letal
- [P005] **HECHO** — Makary & Daniel (2016) publicaron "Medical Error—Third Leading Cause of Death in US" en BMJ
- [P006] **DEFINICIÓN** — error médico (Reason): falla acción planificada completarse como previsto (error ejecución) / uso plan incorrecto para alcanzar objetivo (error planificación)
- [P007] **HECHO** — modelo Swiss cheese (Reason): defensas organizacionales tienen agujeros → errores médicos pasan cuando agujeros se alinean
- [P008] **HECHO** — fuentes comunes errores médicos: eventos adversos medicamentos, UTI por catéter, infecciones línea central, caídas, úlceras presión, neumonía ventilador, sitio/procedimiento equivocado, TVP, diagnóstico erróneo
- [P009] **HECHO** — IOM (2003) identificó 5 competencias core profesionales salud: atención centrada paciente, equipos interdisciplinarios, medicina basada evidencia, mejora calidad, uso informática
- [P010] **HECHO** — AACN Essentials Series incluye Domain 8: Informatics and Healthcare Technologies
- [P011] **HECHO** — AHIMA define health informatics como disciplina científica interesada en tareas cognitivas/procesamiento información/comunicación en práctica/educación/investigación sanitaria
- [P012] **HECHO** — AMIA define biomedical informatics como campo interdisciplinario persiguiendo usos efectivos datos/información/conocimiento biomédico para investigación/resolución problemas/toma decisiones
- [P013] **HECHO** — NLM define health informatics como estudio interdisciplinario diseño/desarrollo/adopción/aplicación innovaciones IT en servicios salud
- [P014] **ALCANCE** — tres temas comunes definiciones health informatics: (1) especialidad interdisciplinaria, (2) vinculada uso IT en salud, (3) enfocada recolección/procesamiento datos/toma decisiones
- [P015] **HECHO** — ARRA proporcionó impulso/financiamiento inicial para implementar EHRs
- [P016] **HECHO** — cuádruple objetivo healthcare: seguridad paciente, calidad atención, reducción costos, alivio carga proveedor (Bodenheimer & Sinsky, 2014)
- [P017] **HECHO** — HITECH Act implementado 2009 con objetivo modernizar infraestructura IT salud US; incentivos financieros adopción EHR
- [P018] **HECHO** — 2015: 84% hospitales adoptaron sistema EHR básico
- [P019] **HECHO** — elegibilidad HITECH: solo hospitales acute care corto plazo elegibles programa incentivos; adopción EHR aumentó 3.2% → 14.2% entre facilities elegibles
- [P020] **HECHO** — uso EHR asociado con reducción tasas mortalidad a lo largo tiempo (Lin et al., 2018)
- [P021] **HECHO** — HIPAA, HITECH Act, MACRA = legislación principal gobernando privacidad/seguridad/IT información salud
- [P022] **HECHO** — datos MPSMS (2012-2013): pacientes cardiovasculares/cirugía/neumonía con tratamiento EHR completo 17-30% menos probabilidad eventos adversos intrahospitalarios

### Ch 2: Theoretical Frameworks

- [P023] **DEFINICIÓN** — alfabetización básica (UNESCO): capacidad identificar, entender, interpretar, crear, comunicar, computar usando materiales impresos/escritos
- [P024] **DEFINICIÓN** — personas FIT (National Academy of Science): fluentes en IT; poseen 3 tipos conocimiento: habilidades contemporáneas, conceptos fundacionales, capacidades intelectuales
- [P025] **DEFINICIÓN** — alfabetización informacional (ACRL 2016): conjunto habilidades integradas abarcando descubrimiento reflexivo información, comprensión producción/valoración información, uso información crear nuevo conocimiento
- [P026] **HECHO** — ACRL Framework for Information Literacy tiene 6 marcos: autoridad construida/contextual, creación información como proceso, información tiene valor, investigación como indagación, academia como conversación, búsqueda como exploración estratégica
- [P027] **DEFINICIÓN** — alfabetización digital (ALA 2013): capacidad usar ICT para encontrar, entender, evaluar, crear, comunicar información digital; requiere habilidades cognitivas + técnicas
- [P028] **DEFINICIÓN** — personal health literacy (Healthy People 2030): grado individuos pueden encontrar/entender/usar información/servicios para informar decisiones salud
- [P029] **DEFINICIÓN** — organizational health literacy (Healthy People 2030): grado organizaciones permiten equitativamente individuos encontrar/entender/usar información/servicios para decisiones salud
- [P030] **DEFINICIÓN** — sistema (Von Bertalanffy): conjunto partes relacionadas interactuantes encerradas en frontera; puede ser abierto (frontera semipermeable) o cerrado (frontera impermeable)
- [P031] **REGLA** — principio GIGO: calidad input requerida para calidad output; aplica a cualquier sistema abierto
- [P032] **DEFINICIÓN** — sistema tiene 3 características: propósito (razón existencia), estructura (modelos jerárquicos/red), funciones (cómo sistema logra propósito)
- [P033] **DEFINICIÓN** — subsistema = sistema dentro sistema objetivo; supersistema = estructura general conteniendo sistema objetivo
- [P034] **DEFINICIÓN** — 6 conceptos cambio en sistemas: homeostasis dinámica, equifinalidad (diferentes caminos → mismo fin), entropía (descomposición), negentropía (crecimiento/complejidad), especialización, reverberación
- [P035] **DEFINICIÓN** — sistema adaptativo complejo (CAS): muchas partes diversas/autónomas, interrelacionadas/interdependientes, comportándose como todo unificado, aprendiendo de experiencia
- [P036] **HECHO** — características CAS: interdependencias no lineales, control distribuido, aprendizaje constante, auto-organización, comportamientos emergentes, co-evolución con entorno
- [P037] **HECHO** — Cynefin Framework (Snowden & Boone, 2007): 5 dominios gestión incertidumbre: simple, complicado, complejo, caótico, desorden
- [P038] **HECHO** — modelo información-comunicación Shannon-Weaver (1948): sender → transmitter/encoder → channel → decoder → receiver; ruido ocupa espacio canal; información medida en bits
- [P039] **HECHO** — tres niveles análisis comunicación: (1) técnico (hardware/software), (2) semántico (mensaje transmite significado), (3) efectividad (mensaje produce resultado deseado)
- [P040] **DEFINICIÓN** — modelo Blum: datos = elementos no interpretados; información = datos procesados/mostrados; conocimiento = relaciones formalizadas entre datos/información
- [P041] **HECHO** — Graves & Corcoran (1989) "Study of Nursing Informatics" usó conceptos Blum + 4 tipos conocimiento Carper → fundamento definiciones nursing informatics
- [P042] **DEFINICIÓN** — modelo DIKW Nelson: datos → información → conocimiento → sabiduría; sabiduría = uso apropiado conocimiento gestionar/resolver problemas humanos
- [P043] **HECHO** — ANA incluyó modelo DIKW en Nursing Informatics: Scope and Standards of Practice (2008)
- [P044] **DEFINICIÓN** — sistema información procesa datos → outputs información; DSS usa conocimiento/reglas → outputs recomendaciones; sistema experto implementa decisiones sin intervención usuario
- [P045] **HECHO** — teoría cambio planificado Lewin: 3 etapas = descongelamiento, movimiento (implementación), recongelamiento (mantenimiento)
- [P046] **HECHO** — difusión innovación Rogers: 5 categorías adoptantes distribución normal: innovadores (2.5%), adoptantes tempranos (13.5%), mayoría temprana (34%), mayoría tardía (34%), rezagados (16%)
- [P047] **HECHO** — 5 atributos innovación afectando tasa adopción: ventaja relativa, compatibilidad, complejidad, probabilidad prueba, observabilidad
- [P048] **HECHO** — 5 características organizacionales prediciendo respuesta innovación: centralización, complejidad, formalización, interconexión, holgura organizacional
- [P049] **HECHO** — proceso decisión innovación 5 etapas: conocimiento → persuasión → decisión → implementación → confirmación
- [P050] **HECHO** — SLCM Staggers-Nelson representado como espiral; 8 pasos: analizar, planificar, desarrollar/comprar, probar, implementar/go-live, mantener/evolucionar, evaluar (cada paso), retornar a analizar
- [P051] **HECHO** — fases análisis + planificación requieren ~70% tiempo/recursos proyecto
- [P052] **HECHO** — TAM (Fred Davis, 1989): utilidad percibida + facilidad uso percibida → actitud → intención comportamental → uso real; basado en Theory of Reasoned Action
- [P053] **HECHO** — UTAUT sintetiza 8 modelos aceptación tecnología; constructos: expectativa rendimiento, expectativa esfuerzo, influencia social, condiciones facilitadoras → intención → uso
- [P054] **HECHO** — modelo sociotécnico Sittig & Singh: 8 dimensiones interdependientes para estudiar HIT en sistemas CAS
- [P055] **HECHO** — NASSS framework (Greenhalgh): non-adoption, abandonment, scale-up, spread, sustainability; considera enfermedad, tecnología, propuesta valor, adoptantes, organización, evolución temporal

### Ch 3: Health Systems and Information Flow

- [P056] **DEFINICIÓN** — learning health system (LHS): sistema abierto usando datos/información/conocimiento/sabiduría → mejorar seguridad paciente, eficiencia, satisfacción
- [P057] **DEFINICIÓN** — data lake: repositorio almacenando datos estructurados + no estructurados en estado natural/crudo; datos organizados en capas (Raw, Refined, Publishing)
- [P058] **DEFINICIÓN** — data warehouse: almacena datos procesados (recolectados, estructurados, filtrados); datos fijos/difíciles alterar
- [P059] **HECHO** — ~80% datos EHR = texto libre no estructurado (narrativa clínica), requiriendo NLP para analizar
- [P060] **DEFINICIÓN** — visualización datos: proceso transformar datos crudos / información numérica abstracta en visuales con atributos físicos
- [P061] **HECHO** — IDC predice datos globales crecerán 33 zettabytes (2018) → 175 zettabytes 2025; 49% almacenados en cloud pública
- [P062] **HECHO** — tipos datos estructurados EHR: demographics paciente, códigos ICD (diagnósticos), LOINC (valores lab), códigos CPT (procedimientos)
- [P063] **DEFINICIÓN** — NLP: asiste computadores entender lenguaje natural; transforma datos no estructurados → datos estructurados para análisis
- [P064] **HECHO** — 8 niveles sistemas Boulding: niveles 1-3 cerrados (estructuras estáticas, mecanismos reloj, mecanismos control); niveles 4-8 abiertos
- [P065] **HECHO** — GST desarrollada por Karl Ludwig von Bertalanffy; aserta sistemas adaptables entre disciplinas
- [P066] **HECHO** — Watson identificó 6 atributos esenciales datos: compartibles, transportables, seguros, precisos, oportunos, relevantes
- [P067] **HECHO** — informaticists aseguran información compartible/comparable usando terminologías (ICD-10, LOINC, SNOMED) y estándares mensajería (HL7)
- [P068] **DEFINICIÓN** — 3 modelos control acceso: MAC (mandatorio, más restrictivo), DAC (discrecional, menos restrictivo), RBAC (basado roles, principio mínimo privilegio, más usado)
- [P069] **HECHO** — AMIA define informática como "ciencia de cómo usar datos, información, conocimiento para mejorar salud humana y prestación servicios salud"
- [P070] **HECHO** — modelos datos estandarizados para EDWs incluyen OMOP, i2b2, Sentinel, PCORnet; adopción sigue siendo barrera
- [P071] **HECHO** — TIGER International Framework identifica competencias core health informatics en 30 áreas incluyendo computer science aplicada, CDS por IT, analytics datos, interoperabilidad

### Ch 4: Informatics-Related Standards and Standard Setting

- [P072] **DEFINICIÓN** — interoperabilidad: extensión sistemas/dispositivos salud pueden intercambiar datos e interpretar datos compartidos (HIMSS)
- [P073] **DEFINICIÓN** — estándar (ISO): especificación/guía/característica establecida describiendo medición/material/producto/procesos/servicios requeridos para propósito específico
- [P074] **HECHO** — estándares establecidos por 2 procesos: vendors dominantes (de facto) / SSO oficial (de jure usando consenso/comunicación abierta)
- [P075] **DEFINICIÓN** — terminología: colección conceptos representativos en dominio especificado, organizada jerárquicamente por relaciones semánticas; vocabulario = lista alfabética palabras/frases
- [P076] **DEFINICIÓN** — terminología referencia: recurso representando conocimiento dominio para recolección/procesamiento/agregación datos; terminología interfaz: términos orientados tarea soportando entrada/display datos en EHRs
- [P077] **DEFINICIÓN** — ontología vs terminología: ontología especifica formalmente significado concepto usando propiedades/relaciones a través herencia; razonador software puede auto-clasificar
- [P078] **HECHO** — UMLS Metathesaurus contiene >190 terminologías fuente, >4.4M conceptos, >16.1M nombres únicos; distribuido por NLM cada 6 meses
- [P079] **HECHO** — LOINC establecido 1994 por Regenstrief Institute; codificación estandarizada observaciones lab/clínicas; 6 ejes: componente, propiedad, timing, sistema/muestra, escala, método; >80,000 términos
- [P080] **HECHO** — SNOMED CT = terminología clínica más comprehensiva, estándar internacional codificación datos salud; gestionado IHTSDO; estructura árbol jerárquica; gratuito países miembros IHTSDO
- [P081] **HECHO** — ICD copyright WHO; reporta mortalidad/morbilidad mundial; usado facturación/reembolso ~70% gastos salud mundiales; ICD-10 endosado 1990, implementado US octubre 2015; ICD-11 en desarrollo
- [P082] **HECHO** — CPT clasificación usada procedimientos quirúrgicos ambulatorios (mandado CMS); DRG agrupa casos similares usando códigos ICD/CPT para reembolso vía IPPS
- [P083] **HECHO** — RxNorm: sistema normalizado nombres medicamentos NLM de 14 terminologías; contiene nombres genéricos/marca medicamentos US; soporta e-prescribing con conocimiento interacciones
- [P084] **HECHO** — ANA reconoce 10 terminologías healthcare para enfermería: 7 específicas enfermería (CCC, ICNP, NANDA-I, NIC, NOC, Omaha System, PNDS) + 3 multidisciplinarias (LOINC, SNOMED CT, ABC Codes)
- [P085] **HECHO** — ISO/TS 18104:2014 provee estructuras categoriales diagnósticos/acciones enfermería en sistemas terminológicos
- [P086] **HECHO** — NANDA-I: primera terminología enfermería reconocida ANA (desde 1970); 235 diagnósticos enfermería en 47 clases / 13 dominios (release 2015-2017)
- [P087] **HECHO** — NIC: >550 intervenciones enfermería en 30 clases / 7 dominios; ~13,000 declaraciones actividad narrativa
- [P088] **HECHO** — NOC: 540 resultados en 34 clases / 7 dominios; escalas Likert 5 puntos medir niveles resultado
- [P089] **HECHO** — CCC v2.5: 176 diagnósticos enfermería (528 resultados vía 3 modificadores) + 201 intervenciones (804 acciones vía 4 tipos acción); organizados bajo 21 componentes cuidado / 4 patrones healthcare
- [P090] **HECHO** — Omaha System: 3 esquemas (Problem Classification, Intervention, Problem Rating Scale for Outcomes); 42 declaraciones problema; 75 intervenciones target; 4 categorías acción → `ANA`
- [P091] **HECHO** — HL7 desde 1987: provee framework/estándares para intercambio/integración/compartición/recuperación información salud electrónica; estándares clave = CDA (documentos clínicos XML) y FHIR (intercambio datos basado recursos)
- [P092] **DEFINICIÓN** — recursos FHIR simulan "formularios" papel replicando información clínica/administrativa; diseñados intercambio inpatient, SNF, long-term care mundial
- [P093] **HECHO** — C-CDA Release 1.1 requerida por Meaningful Use stage 2 para intercambio información paciente (transiciones cuidado, portabilidad datos, engagement paciente)
- [P094] **DEFINICIÓN** — armonización terminológica: esfuerzo consolidar/mejorar cobertura conocimiento dominio; cross-mapping preserva significado información intercambiada entre sistemas dispares
- [P095] **HECHO** — ANA recomienda SNOMED CT + LOINC para intercambio C-CDA con otro setting para problemas/planes cuidado
- [P096] **HECHO** — CMS estableció Meaningful Use (ahora Promoting Interoperability) programa incentivos uso EHR certificado; funciones básicas incluyen e-prescribing, listas problemas/medicamentos, gestión cuidado

### Ch 5: Evaluation of Health Information Systems

- [P097] **DEFINICIÓN** — evaluación HIS: acto medir/explorar propiedades HIS (durante planificación/desarrollo/implementación/operación), resultado informa decisión sobre sistema en contexto específico
- [P098] **DEFINICIÓN** — HIS = sistema computador usado adquirir/almacenar/entregar/analizar datos médicos; intervención HIS = intervención para desarrollar/introducir/sostener nuevo HIS
- [P099] **HECHO** — 3 niveles sociotécnicos HIS: (1) social (contexto interno/externo), (2) humano (características/necesidades/limitaciones usuario), (3) técnico (tecnología)
- [P100] **HECHO** — ciclo vida HIS 4 fases: planificación, desarrollo, implementación, operación
- [P101] **DEFINICIÓN** — evaluación formativa: resultados usados feedback mejora continua; evaluación sumativa: resultados usados evaluar propiedades/mérito programa
- [P102] **HECHO** — framework ELICIT (Kukhareva et al., 2022): 12 tipos estudio evaluación a través fases ciclo vida HIS y niveles sociotécnicos
- [P103] **DEFINICIÓN** — jerarquía perspectivas teóricas: teorías (explican mecanismos, alcance más amplio) → frameworks (describen determinantes/medición) → modelos (específicos programa, más prácticos)
- [P104] **HECHO** — CDS Taxonomy (Wright et al.): 53 tipos sistemas CDS en grupos: soporte dosificación medicamentos, facilitadores órdenes, alertas/recordatorios POC, displays información relevante, sistemas expertos, soporte workflow
- [P105] **HECHO** — program logic model describe 4 componentes: inputs, actividades, resultados, outputs
- [P106] **HECHO** — Situation Awareness (Endsley): 3 niveles = (1) percepción (ver estímulo), (2) comprensión (significado), (3) proyección (qué pasará/qué puedo hacer)
- [P107] **HECHO** — modelo PDCA (Plan-Do-Check-Act) de Deming (1950s): mejora calidad iterativa; cada ciclo puede ser tan corto como 1 hora
- [P108] **HECHO** — UTAUT predice intenciones usuario como función expectativa rendimiento, expectativa esfuerzo, influencia social, condiciones facilitadoras; moderadores = género, edad, uso mandado; explica ~70% varianza intención uso
- [P109] **HECHO** — CFIR (Damschroder et al., 2009): 5 dominios principales (características intervención, setting externo, setting interno, características individuales, procesos implementación) con 38 constructos
- [P110] **HECHO** — NPT (May & Finch, 2009): 4 fases clave implementación = coherencia, participación cognitiva, acción colectiva, monitoreo reflexivo
- [P111] **HECHO** — RE-AIM framework: 5 constructos medir implementación: Reach, Effectiveness, Adoption, Implementation, Maintenance
- [P112] **HECHO** — modelo estructura-proceso-resultado Donabedian: medidas estructurales (recursos), medidas proceso (tareas/decisiones), medidas resultado (resultados medibles cuidado)
- [P113] **HECHO** — teoría éxito SI DeLone & McLean (1992, revisada 2003): calidad sistema, calidad información, calidad servicio → uso, satisfacción usuario → resultados
- [P114] **HECHO** — framework GRASP (Khalifa et al.): gradúa herramientas predictivas C3 (validación interna) → A1 (estudios experimentales post-implementación)
- [P115] **HECHO** — instrumentos evaluación validados: SUS (System Usability Scale, 10 ítems, 0-100); NASA-TLX (carga trabajo percibida); PAM (Patient Activation Measure, 0-100); SERVQUAL (calidad servicio, 5 escalas)
- [P116] **HECHO** — estándar reporte cualitativo: criterios RATS = Relevance, Appropriateness, Transparency, Soundness
- [P117] **HECHO** — diseños estudio recomendados evaluación HIS: pre-post, análisis series tiempo interrumpidas (preferido sobre simple pre-post), RCT (gold standard pero difícil para HIT), baseline múltiple single-subject
- [P118] **HECHO** — sistemas CDS habilitados AI requieren evaluación/monitoreo continuo; afectados por sesgos datos entrenamiento; necesitan evaluación rigurosa impacto estructura/proceso/resultado/equidad cuidado

## Section 2: Health Information Systems and Applications

### Ch 6: Technical Infrastructure

- [P119] **DEFINICIÓN** — infraestructura IT healthcare (arquitectura) = todos componentes requeridos operar/gestionar servicios/entornos IT dentro setting healthcare
- [P120] **DEFINICIÓN** — workstation (thick client) = computador recibe input, procesa/almacena datos, funciona independientemente de red
- [P121] **DEFINICIÓN** — thin client = dispositivo cuyo procesamiento principal realizado en servidor remoto; sin datos paciente almacenados localmente; robo físico no compromete confidencialidad
- [P122] **REGLA** — bajo HIPAA, entidades healthcare transmitiendo datos son "covered entities" requeridas cumplir criterios estrictos precisión/seguridad datos
- [P123] **REGLA** — GINA restringe acceso información genética; prohíbe empleadores/aseguradores salud discriminar basado factores riesgo genético identificados para enfermedad no manifestada
- [P124] **HECHO** — HITECH Act (2009) estableció requerimiento datos compartidos como EHRs; vinculó reembolso CMS a meaningful use sistemas electrónicos
- [P125] **HECHO** — 21st Century Cures Act aprobada 2016 para acelerar desarrollo productos médicos / mejorar innovación healthcare
- [P126] **HECHO** — ONC desarrolló Cures Act Final Rule soportando acceso/intercambio/uso seguro/sin fricciones información salud electrónica
- [P127] **HECHO** — Cures 2.0 Act (2021 draft) autorizaría ARPA-H dentro NIH, integraría cuidadores en equipo cuidado paciente, aumentaría acceso telehealth/testing genético
- [P128] **DEFINICIÓN** — ciclo vida datos = 8 pasos: generación, recolección, procesamiento, almacenamiento, gestión, análisis, visualización, interpretación; EHR agrega 9° paso: compartición
- [P129] **DEFINICIÓN** — EMR = documentación paciente único en localización única; equivalente aproximado historia clínica papel; soporta tracking/trending/CDS dentro un sitio
- [P130] **DEFINICIÓN** — EHR = extiende EMR compartiendo datos entre proveedores/instituciones; incorpora equipo cuidado completo incluyendo pacientes/familias
- [P131] **DEFINICIÓN** — CDR (clinical data repository) = componente almacenamiento registros clínicos paciente; almacena resultados lab, órdenes medicamentos, signos vitales, demographics, datos financieros
- [P132] **DEFINICIÓN** — interoperabilidad = capacidad intercambiar y hacer uso significativo datos entre sistemas
- [P133] **HECHO** — LOINC originalmente limitado observaciones lab médico; ahora incluye Nursing Minimum Data Set (NMDS); tiene Nursing Subcommittee
- [P134] **HECHO** — SNOMED-CT = terminología multilingüe información salud clínica
- [P135] **HECHO** — RxNorm estandariza nombres medicamentos genéricos/marca, significados, atributos (potencia, dosis), relaciones
- [P136] **DEFINICIÓN** — modelo almacenamiento central = repositorio único almacena todos/mayoría datos clínicos; requiere mapeo terminología común antes almacenamiento
- [P137] **DEFINICIÓN** — modelo almacenamiento distribuido = cada aplicación almacena datos en propio repositorio; datos federados acceso real-time; provee confiabilidad si un repositorio falla
- [P138] **DEFINICIÓN** — MPI (Master Person Index) = conjunto información identificando cada persona/paciente; almacena demographics, identificadores organizacionales; crea "golden record"
- [P139] **DEFINICIÓN** — RHIO = organización cuasi-pública sin fines lucro compartiendo datos dentro región, típicamente iniciada con grant/financiamiento público
- [P140] **DEFINICIÓN** — HIE = health information exchange con organización proveedora ancla, frecuentemente iniciada vía incentivos financieros
- [P141] **HECHO** — eHealth Exchange (antes NwHIN) gestionado por The Sequoia Project; incluye organizaciones 50 estados + 4 agencias federales (SSA, DoD, VA, HHS)
- [P142] **DEFINICIÓN** — herramientas CDS integradas EHRs: plantillas documentación, guías clínicas, alertas/notificaciones, order-sets, herramientas evaluación específicas enfermedad
- [P143] **HECHO** — 21st Century Cures Act define interoperabilidad como tecnología habilitando intercambio información seguro sin esfuerzo especial usuario + acceso completo toda información salud electrónicamente accesible
- [P144] **DEFINICIÓN** — ransomware = ataque cyber explotando brechas seguridad para encriptar covertamente datos/repositorio, demandando pago por clave desencriptación
- [P145] **HECHO** — ataque ransomware UVM Medical Center 2020 encriptó EHR/payroll/otros IT; bloqueado un mes; costo estimado $50 millones
- [P146] **DEFINICIÓN** — phishing = hacking social explotando usuarios humanos vía email/comunicaciones fraudulentas para robar datos/credenciales/dinero

### Ch 7: The Electronic Health Record and Precision Care

- [P147] **HECHO** — NAHIT (2008) bajo DHHS definió EHR como registro electrónico conforme estándares interoperabilidad nacionalmente reconocidos, creado/gestionado/consultado entre >1 organización healthcare
- [P148] **ALCANCE** — objetivo EHR = registro nacimiento-a-muerte (prenatal a postmortem) de múltiples fuentes; EMR limitado a organización/práctica única
- [P149] **DEFINICIÓN** — PHR = registro controlado principalmente por paciente/consumidor; objetivo: conformar estándares nacionales, integrarse en sistemas mayores
- [P150] **HECHO** — reportes IOM "To Err Is Human" (2000) y "Crossing Quality Chasm" (2001) impulsaron necesidad sistemas EHR aumentar seguridad paciente / reducir errores
- [P151] **HECHO** — ARRA (2009) incluyó HITECH Act expandir adopción EHR; autorizó programas mejorar calidad/seguridad/eficiencia healthcare vía HIT
- [P152] **HECHO** — CARES Act (2020) = estímulo $2 trillones; asignó $127 mil millones facilities healthcare respuesta COVID-19 incluyendo telehealth/PPE/vacunas
- [P153] **HECHO** — programa meaningful use CMS (2011) renombrado Promoting Interoperability (PI) en 2018; desplegado en 3 etapas
- [P154] **HECHO** — MACRA (2015) cambió reembolso Medicare de fee-for-service a value-based care; llevó a MIPS incluyendo programa PI + APMs
- [P155] **HECHO** — encuesta 2019: 94% hospitales US adoptaron tecnología EHR certificada; >50% utilizan HIEs estatales/regionales/locales
- [P156] **HECHO** — HIMSS identifica 5 áreas desarrollo estándares: vocabularios/terminologías, contenido datos/documentos, transporte mensajes, privacidad/seguridad, identificadores únicos
- [P157] **HECHO** — reporte IOM 2003 delineó 8 componentes esenciales entrega cuidado EHR: procesos administrativos, comunicación/conectividad, soporte decisión, dentistry/optometry, datos/info salud, gestión entry órdenes, soporte paciente, gestión resultados + gestión salud poblacional
- [P158] **DEFINICIÓN** — CPOE = software permitiendo proveedores autorizados ingresar/procesar/rastrear/actualizar/completar órdenes vía computador; elimina errores transcripción órdenes manuscritas
- [P159] **DEFINICIÓN** — eMAR = registro electrónico administración medicamentos; provee medio ver/documentar uso medicamentos; muestra nombre droga, hora, dosis, vía
- [P160] **HECHO** — concepto BCMA introducido 1992 por enfermera en hospital VHA; sistema escanea badge enfermero + pulsera paciente + código barras medicamento; verifica 5 rights (paciente, droga, dosis, hora, vía)
- [P161] **DEFINICIÓN** — RFID administración medicamentos: RFID pasivo usa scanner como barcoding; RFID activo transmite señales automáticamente sin scanner
- [P162] **HECHO** — DICOM = estándar global transmisión, almacenamiento, display información imagenología médica
- [P163] **HECHO** — PACS almacena imágenes diagnósticas digitales para display en EHR; provee mejor contraste/claridad/capacidad ampliación
- [P164] **HECHO** — NDC = identificador universal medicinas requerido FDA
- [P165] **HECHO** — NDF-RT agrupa drogas por clases; RxNorm contiene nombres marca/genéricos con ingredientes activos, potencia, dosis, interacciones
- [P166] **DEFINICIÓN** — PGHD = datos relacionados salud creados/registrados/recopilados por pacientes/familia/cuidadores para abordar problema salud
- [P167] **HECHO** — costos implementación EHR: práctica privada grande ~$233,297 primer año; hospitales $25M a $10B; mantenimiento anual ~18-20% precio compra
- [P168] **⚠ TENSIÓN** — carga documentación: enfermeros gastaban 23% tiempo documentando post-EHR vs 9% pre-EHR; preocupaciones menos tiempo con pacientes, disrupción workflow
- [P169] **DEFINICIÓN** — medicina de precisión = ciencia emergente usando big data, genómica, machine learning personalizar tratamiento/prevención basado genética, estilo vida, factores socioculturales
- [P170] **DEFINICIÓN** — biobanks = repositorios material médico/biológico/genético enlazables a EHRs para investigación
- [P171] **HECHO** — encuesta KFF 2019: 88% respondientes indicaron proveedor usa EHR; solo 45% dijeron EHRs mejoraron cuidado/comunicación; 1 de 5 reportó errores en registro médico

### Ch 8: Administrative Applications in Healthcare

- [P172] **DEFINICIÓN** — FIS = sistema almacenando/registrando operaciones fiscales para reporte/toma decisiones en organización healthcare
- [P173] **DEFINICIÓN** — general ledger = registro todas transacciones financieras; rastrear activos, pasivos, patrimonio
- [P174] **REGLA** — EMTALA requiere pacientes tratados en emergencias independientemente capacidad pago
- [P175] **DEFINICIÓN** — clean claims = reclamaciones conteniendo toda info crítica (demographics, cargos, procedimientos, codificación) habilitando pago seguro rápido
- [P176] **DEFINICIÓN** — ACO = red doctores/hospitales compartiendo responsabilidad cuidado grupo paciente específico; recibe bonos controlar costos cumpliendo benchmarks calidad
- [P177] **DEFINICIÓN** — pay for performance (P4P) = concepto vinculando pago calidad cuidado/resultados paciente en vez volumen servicios
- [P178] **HECHO** — ACA incluye Hospital Readmissions Reduction Program reduciendo pagos 1% hospitales con readmisiones evitables excesivas para infarto/insuficiencia cardíaca/neumonía
- [P179] **HECHO** — desde inicio ACA (2010), >440 Medicare ACOs creados; 54% disminuyeron gastos generando $383M ahorros netos Medicare
- [P180] **DEFINICIÓN** — value-based care = entregar mejor resultado por dólares invertidos; requiere integración datos clínicos + financieros nivel poblacional
- [P181] **DEFINICIÓN** — PHM (Population Health Management) = enfoque mejorar resultados salud para población especificada
- [P182] **DEFINICIÓN** — PMS (Practice Management System) = sistema información soportando funciones oficina proveedor: demographics, scheduling, documentación, facturación, cobros
- [P183] **HECHO** — códigos CPT tienen RVU (Relative Value Unit) adjunto definido por Medicare; wRVU mide productividad/reembolso médico
- [P184] **HECHO** — archivo maestro supply items típicamente contiene 30,000-100,000 ítems; archivo maestro vendors típicamente 200-500 proveedores
- [P185] **DEFINICIÓN** — charge description master file = lista todos precios servicios (DRGs, HCPCS, CPT) o bienes proporcionados pacientes; base facturación
- [P186] **DEFINICIÓN** — BI (Business Intelligence) = adquisición, correlación, transformación datos en información accionable a través analytics
- [P187] **HECHO** — mercado vendors HIS hospital 2013: top 5 por revenue = McKesson ($3.4B), Cerner ($2.9B), Siemens ($1.8B), Epic ($1.7B), Allscripts ($1.4B)
- [P188] **HECHO** — mercado vendors software healthcare proyectado alcanzar $25 mil millones para 2024
- [P189] **HECHO** — estadía promedio hospital US para mayoría procedimientos = 4.8 días
- [P190] **DEFINICIÓN** — HRIS = sistema integrando software/hardware/políticas automatizar actividades HR estratégicas/operacionales
- [P191] **HECHO** — aproximadamente 1400 Free and Charitable Clinics en US proveen healthcare asequible a no asegurados/sub-asegurados

### Ch 9: Community Health Systems

- [P192] **HECHO** — home health por cuidadores formales originó 1800s basado modelo district nursing William Rathbone en Inglaterra; 71 agencias antes 1900, 600 para 1909 en US
- [P193] **HECHO** — Lillian Wald y Mary Brewster establecieron Henry Street Settlement House (1893) NYC; convencieron Metropolitan Life Insurance incluir visitas domiciliarias como beneficio
- [P194] **HECHO** — Medicare (1965) incluyó servicios home health para personas ≥65; requirió plan cuidado, firma médico, visitas intermitentes/cortas
- [P195] **HECHO** — Florence Wald estableció Connecticut Hospice (1974) primer hospice US con staff interprofesional; reembolso Medicaid hospice comenzó 1980, Medicare 1983
- [P196] **HECHO** — Donabedian (1966) describió framework estructura-proceso-resultado evaluar calidad cuidado médico
- [P197] **HECHO** — Lawrence Weed desarrolló problem-oriented medical record (1968) adaptable computarización
- [P198] **DEFINICIÓN** — OASIS = dataset estandarizado agencias home health certificadas Medicare; determina pago, mide calidad/resultados; recolectado admisión/transferencia/alta
- [P199] **HECHO** — OASIS-D implementado enero 1, 2019; OASIS-D1 comenzó enero 1, 2020; OASIS-E propuesto enero 1, 2023 con 31 páginas en secciones A-Q
- [P200] **DEFINICIÓN** — HIS (Hospice Item Set) = medidas calidad estandarizadas requeridas reporte hospice per ACA 2010; versión actual efectiva febrero 16, 2021
- [P201] **HECHO** — ANA reconoce 12 terminologías referencia y point-of-care (interfaz) para enfermería
- [P202] **DEFINICIÓN** — Omaha System = terminología point-of-care reconocida ANA mapeada SNOMED CT/LOINC; 3 componentes: Problem Classification Scheme, Intervention Scheme, Problem Rating Scale for Outcomes
- [P203] **HECHO** — Omaha System desarrollado a través 4 proyectos investigación federales (1975-1993) por VNA of Omaha, Nebraska; existe dominio público sin copyright/licensing fees
- [P204] **ALCANCE** — Problem Classification Scheme: 4 dominios (Environmental, Psychosocial, Physiological, Health-related Behaviors) con 42 problemas paciente segundo nivel
- [P205] **ALCANCE** — Intervention Scheme: 4 categorías (Teaching/Guidance/Counseling, Treatments/Procedures, Case Management, Surveillance) con 75 targets + 1 "other"
- [P206] **DEFINICIÓN** — Problem Rating Scale for Outcomes: 3 escalas Likert cinco puntos midiendo Knowledge, Behavior, Status de 1 (sin conocimiento) a 5 (superior)
- [P207] **HECHO** — Triple Aim (2008, Berwick): mejor cuidado individuos, mejor salud poblaciones, reducción costos per-cápita; Quadruple Aim (2014) agregó mejorar experiencia clínica/bienestar equipo cuidado
- [P208] **DEFINICIÓN** — hospice = servicios pacientes expectativa vida ≤6 meses que agotaron tratamiento curativo; incluye seguimiento duelo
- [P209] **DEFINICIÓN** — palliative care = enfoca calidad vida pacientes/familias enfrentando enfermedad amenazante vida; comienza cuando cura ya no posible; puede ser largo plazo
- [P210] **HECHO** — ~5800 programas hospice en 2018; ~4639 certificados Medicare; ~1.55M beneficiarios Medicare recibieron hospice (2018); estadía promedio 89.6 días
- [P211] **HECHO** — ~35,000 agencias home health en US; 11,356 certificadas Medicare; Medicare 23% / Medicaid 17% reembolso total; sirven 12-15M pacientes con >600M visitas/año
- [P212] **HECHO** — >250 centros salud gestionados enfermería en US; Philadelphia tiene más; sirven poblaciones desatendidas
- [P213] **HECHO** — desde 2008, departamentos salud locales perdieron 31,000 de ~184,000 posiciones por presupuestos decrecientes/despidos/attrición

### Ch 10: Public Health Informatics

- [P214] **DEFINICIÓN** — public health informatics = especialidad usando métodos/herramientas informática resolver problemas salud pública o soportar objetivos salud poblacional/pública
- [P215] **DEFINICIÓN** — salud pública = esfuerzos comunidad organizados dirigidos prevención enfermedad y promoción salud (IOM 1988)
- [P216] **HECHO** — expectativa vida US declinó 78.8 años (2019) → 77.8 años (2020); mayor impacto pandemia COVID-19
- [P217] **HECHO** — declive expectativa vida 2019-2020 por raza: Non-Hispanic Black -2.7 años, Hispanic -1.9 años, Non-Hispanic White -0.8 años
- [P218] **HECHO** — PHS Act forma fundamento autoridad legal HHS respuesta emergencias salud pública; enmendado por PAHPA (2006) y PAHPRA (2013)
- [P219] **HECHO** — IOM (1988) framework define 3 funciones core salud pública: assessment, policy development, assurance; con 10 servicios esenciales
- [P220] **HECHO** — Florence Nightingale recolectó sistemáticamente datos mortalidad soldados durante Guerra Crimea; creó Nightingale Rose Diagram visualización datos; considerada early public health informatics
- [P221] **HECHO** — John Snow usó mapeo información salud determinar causa cólera en Londres (1854)
- [P222] **ALCANCE** — infraestructura public health informatics = 3 componentes interconectados: fuerza trabajo calificada, sistemas información actualizados, interoperabilidad con sistemas/agencias esenciales
- [P223] **HECHO** — AMIA ofrece 2 certificaciones informaticists: clinical informatics y health informatics
- [P224] **REGLA** — HIPAA Privacy Rule permite covered entities divulgar PHI sin autorización a autoridades salud pública para prevención/control enfermedad, reporte eventos vitales, vigilancia, investigaciones
- [P225] **DEFINICIÓN** — vigilancia sindrómica = proceso detectar/entender/monitorear eventos salud antes diagnóstico; sistema alerta temprana niveles enfermedad inusuales
- [P226] **HECHO** — JHCRC (Johns Hopkins Coronavirus Resource Center) comenzó enero 22, 2020 con mapas rastreo global; evolucionó marzo 3, 2020 centro recursos completo; recolecta datos 260 fuentes incluyendo 182 agencias
- [P227] **HECHO** — medidas HEDIS usadas planes salud monitorear desempeño ~100 áreas; reportadas NCQA; permite público evaluar calidad plan healthcare
- [P228] **DEFINICIÓN** — infodemic = información rápida generalizada conteniendo datos precisos/imprecisos
- [P229] **HECHO** — pandemia H1N1 (2009) llevó creación aplicación monitoreo enfermedad automatizada específica caso para compartición info local/estatal/nacional
- [P230] **HECHO** — brote Ebola 2015 en US expuso necesidad mejorar sistemas monitoreo electrónico y centro "inteligencia salud pública"
- [P231] **HECHO** — 79% apps healthcare venden o comparten datos recolectados (Grundy et al., 2019); desarrolladores apps terceros no cubiertos por HIPAA
- [P232] **HECHO** — Craven et al. identificó enfoque 5 pilares preparación pandemia: sistema siempre-listo, vigilancia enfermedad, agenda prevención, capacidad healthcare, I+D

## Section 3: Decision-Making and the Digitally Engaged Patient

### Ch 11: Evidence-Based Informatics

- [P233] **DEFINICIÓN** — EBP = integración mejor evidencia investigación, expertise clínico, preferencia paciente → producir decisiones best-practice
- [P234] **DEFINICIÓN** — PBE = diseño investigación prospectivo innovador usando datos práctica actual identificar qué procesos cuidado funcionan mundo real; EBP usa evidencia guiar práctica, PBE obtiene evidencia de práctica
- [P235] **DEFINICIÓN** — learning health system (LHS) = entidad que rutinaria/continuamente busca generar y aprender de datos para mejorar salud individual/poblacional (Guise et al., 2018)
- [P236] **DEFINICIÓN** — knowledge transformation = conversión hallazgos investigación desde descubrimiento a través serie etapas/formas aumentar relevancia, accesibilidad, utilidad evidencia en POC (Stevens, 2015)
- [P237] **DEFINICIÓN** — CPGs = declaraciones sistemáticamente desarrolladas asistir decisiones practicante/paciente sobre healthcare apropiada para circunstancias clínicas específicas (IOM, 2011)
- [P238] **HECHO** — "To Err Is Human" (IOM, 2000) estimó ~100,000 pacientes dañados anualmente por sistema healthcare; 2014 expertos sugieren mortalidad errores médicos rango 210,000-400,000 anualmente
- [P239] **HECHO** — "Crossing Quality Chasm" (IOM, 2001) identificó EBP como solución; recomendó principios STEEEP: Safe, Timely, Effective, Efficient, Equitable, Patient-centered
- [P240] **HECHO** — AHRQ National Healthcare QDR reports publicados anualmente desde 2003; calidad/disparidades integradas documento único desde 2014
- [P241] **HECHO** — tasas HAC reducidas 17% entre 2010-2013 y 13% entre 2014-2017; cuidado recomendado entregado solo 70% del tiempo
- [P242] **HECHO** — Stevens ACE Star Model tiene 5 puntos: (1) investigación descubrimiento, (2) resumen evidencia, (3) traducción guías, (4) integración práctica, (5) evaluación
- [P243] **HECHO** — >10,000 nuevos artículos investigación publicados anualmente en medicina; ~12.8M estudios médicos/salud publicados 1980-2012
- [P244] **HECHO** — Cochrane Database Systematic Reviews incluyó 8,715 SRs a octubre 2021
- [P245] **REGLA** — SRs = enlace central entre investigación y toma decisiones clínica (IOM, 2008); considerado gold standard resúmenes evidencia
- [P246] **HECHO** — USPSTF gradúa recomendaciones A-D más I; A = alta certeza beneficio neto sustancial → ofrecer/proveer; D = recomendar contra; I = evidencia insuficiente
- [P247] **HECHO** — tres categorías modelos EBP: (1) EBP/uso investigación/transformación conocimiento, (2) cambio estratégico/organizacional, (3) intercambio/síntesis conocimiento (Mitchell et al., 2010)
- [P248] **HECHO** — instrumento AGREE II: herramienta 23 ítems colaboración internacional evaluar CPGs; evalúa alcance/propósito, participación stakeholders, rigor, claridad, aplicación, independencia editorial
- [P249] **HECHO** — tamaño muestra típico PBE 800-2000+; diseño observacional/descriptivo; aspecto temporal prospectivo
- [P250] **REGLA** — PBE mitiga debilidades diseño observacional vía: (1) caracterización exhaustiva paciente, (2) muestras grandes/diversas, (3) documentación intervención estandarizada detallada, (4) inclusión clínicos/pacientes primera línea
- [P251] **HECHO** — estudio PBE tiene 6 pasos: crear PCT multi-sitio, controlar severidad paciente, implementar recolección datos intensiva, crear database estudio, probar hipótesis sucesivamente, validar/implementar hallazgos
- [P252] **HECHO** — CSI = medida específica enfermedad/edad con >2,200 indicadores clínicos medir severidad enfermedad en estudios PBE
- [P253] **HECHO** — CDRNs PCORI permiten investigación efectividad comparativa/PBE proveyendo soluciones informáticas compartición datos multi-institucional
- [P254] **HECHO** — ONC 2020 publicó 2 objetivos / 9 prioridades investigación HIT: aprovechar datos EHR alta calidad para investigación + avanzar infraestructura HIT investigación
- [P255] **HECHO** — TeamSTEPPS promovido healthcare militar desde 1995; rollout civil 2006; mejora comunicación/trabajo equipo → mejor cuidado paciente

### Ch 12: Clinical Decision Support

- [P256] **DEFINICIÓN** — CDS = herramientas/intervenciones proveyendo clínicos/staff/pacientes conocimiento e información persona-específica, inteligentemente filtrada/presentada tiempos apropiados, mejorar salud/healthcare (Osheroff et al., 2007)
- [P257] **DEFINICIÓN** — NQF definió CDS = cualquier herramienta/técnica mejorando toma decisiones por clínicos/pacientes/sustitutos en prestación/gestión healthcare (NQF, 2010)
- [P258] **HECHO** — ~22,000 muertes prevenibles/año settings inpatient por errores médicos (Rodwin et al., 2020)
- [P259] **HECHO** — pacientes US reciben solo 54.9% procesos cuidado médico recomendados (McGlynn et al., 2003)
- [P260] **HECHO** — primer estudio CDS: de Dombal et al. (1972) diagnóstico computer-aided dolor abdominal agudo; sistema Bayesiano precisión diagnóstica 91.8% vs médico 79.6%
- [P261] **HECHO** — McDonald (1976) RCT seminal Regenstrief Institute: médicos reaccionaron 51% eventos con recordatorios CDS vs 21% sin
- [P262] **HECHO** — HELP System (LDS Hospital, Salt Lake City, finales 1960s-21st century) incluyó 4 categorías CDS: alertas, críticas, sugerencias on-demand, QA retrospectivo
- [P263] **HECHO** — taxonomía Delphi Wright et al. (2011): 6 categorías CDS / 53 subtipos: dosificación medicamentos, facilitadores órdenes, alertas/recordatorios POC, display información relevante, sistemas expertos, soporte workflow
- [P264] **HECHO** — Bates et al. (2003) "Ten Commandments for Effective CDS": velocidad, anticipar necesidades, ajustar workflow, intervenciones simples, monitorear impacto, gestionar sistemas conocimiento
- [P265] **HECHO** — CDS Five Rights (Osheroff/HIMSS): información correcta, persona correcta, formato CDS correcto, canal correcto, punto correcto en workflow
- [P266] **HECHO** — Kawamoto et al. (2005) revisión sistemática 70 RCTs: provisión automática CDS como parte workflow clínico = feature más crítica (OR ajustado 112.1, P<.00001)
- [P267] **HECHO** — Brigham and Women's Hospital CPOE con CDS redujo errores serios medicación no interceptados 86% (Bates et al., 1999)
- [P268] **HECHO** — sistema CDS ventilador ARDS → 60% supervivencia vs esperada ~35% (Thomsen et al., 1993)
- [P269] **HECHO** — CDS asistente antibióticos: pacientes gestionados per CDS redujeron LOS (10.0 vs 16.7 días) y costos menores ($26,315 vs $44,865) (Evans et al., 1998)
- [P270] **HECHO** — VHA estimó inversiones HIT generaron >$3B beneficios netos; CDS catalizador importante ROI
- [P271] **HECHO** — alert fatigue = clínicos ignorando alertas por triggers excesivos/irrelevantes; abordajes incluyen priorizar, contextualizar, governance, analytics predictivo filtrado
- [P272] **HECHO** — Infobuttons aprovechan atributos contextuales EHR proveer links automatizados recursos conocimiento relevante; respondieron preguntas clínicas >69% sesiones (Cook et al., 2017)
- [P273] **HECHO** — estándares CDS alineados HL7 FHIR: interfaz datos FHIR, integración apps SMART, web services CDS Hooks, representación lógica CQL, FHIR Clinical Reasoning
- [P274] **HECHO** — 21st Century Cures Act Final Rule requiere sistemas EHR soportar estándares HL7 FHIR y SMART
- [P275] **HECHO** — 2009 gobierno federal US ~$30B incentivos "Meaningful Use" sistemas EHR
- [P276] **⚠ TENSIÓN** — beneficios financieros CDS pueden acumularse stakeholders distintos quienes invierten (org invierte CDS vacunación → pierde revenue hospitalización; sociedad/aseguradores benefician)

### Ch 13: The Evolving ePatient

- [P277] **DEFINICIÓN** — ePatient = persona tomando rol activo decisiones salud/healthcare; acuñado Tom Ferguson (1975); caracterizado como equipped, enabled, empowered, engaged
- [P278] **DEFINICIÓN** — eHealth = campo emergente intersección medical informatics/salud pública/negocios referente servicios/información salud entregados/mejorados internet (Eysenbach, 2001)
- [P279] **DEFINICIÓN** — participatory healthcare/medicine = modelo cooperativo incentivando participación activa pacientes, cuidadores, profesionales healthcare continuo cuidado completo
- [P280] **DEFINICIÓN** — PGHD = datos salud creados/registrados/recopilados por pacientes/familia/cuidadores abordar problema salud
- [P281] **DEFINICIÓN** — quantified self = persona rastreando métricas salud personal (PA, ejercicio, sueño, dieta) usando herramientas personal informatics auto-monitoreo
- [P282] **HECHO** — Slack et al. (1966) primeros probaron entrevistas médicas computer-based conducidas paciente en 1960s
- [P283] **HECHO** — evolución Web: 1.0 read-only → 2.0 social/comunidad → 3.0 semántica/personalizada → 4.0 mobile/siempre-conectada
- [P284] **HECHO** — usuarios internet: 16M (1995) → 147M (1998 lanzamiento Google) → 500M (2001) → 4.66B/~60% población mundial (Oct 2020)
- [P285] **HECHO** — Pew: 8/10 usuarios internet buscan info salud online; 87% teens/jóvenes adultos buscaron info salud online
- [P286] **HECHO** — Human Genome Project: 13 años, ~$3B (completado 2003); 23andMe (lanzado 2007) info genética directa consumidor <$500 (2021: $99)
- [P287] **HECHO** — >350,000 apps salud/fitness disponibles vía smartphone (IQVIA, 2021)
- [P288] **HECHO** — OpenAPS = sistema páncreas artificial open-source; >2,300 individuos crearon sistemas DIY closed-loop julio 2021; usuarios auto-reportan menos peaks/valleys glucosa, HbA1c reducido
- [P289] **HECHO** — proyecto OpenNotes comenzó 2010; 2020 >250 organizaciones salud participando representando >50M pacientes; antes implementación 29% médicos pensaban compartir notas beneficioso → después 71%
- [P290] **HECHO** — abril 5, 2021 reglas federales implementaron 21st Century Cures Act: 8 tipos notas clínicas no deben bloquearse; deben estar disponibles gratis pacientes
- [P291] **HECHO** — solo 15-30% pacientes usan portales paciente online pese disponibilidad generalizada (US GAO)
- [P292] **HECHO** — IOM (2001) "10 simple rules 21st century healthcare": beyond visits, individualización, control, información, ciencia, seguridad, transparencia, anticipación, valor, cooperación
- [P293] **HECHO** — 2026 proyectadas 8.8B suscripciones mobile, 91% mobile broadband (Ericsson, 2021)
- [P294] **⚠ TENSIÓN** — digital divide: pese proliferación tecnología, COVID-19 expuso disparidades acceso broadband/smartphone entre grupos raciales/étnicos/socioeconómicos

### Ch 14: Digital Health: Managing Health and Wellness

- [P295] **DEFINICIÓN** — digital health = conecta/empodera personas gestionar salud/bienestar vía equipos proveedores accesibles en entornos cuidado digitalmente habilitados (HIMSS/Snowdon, 2020)
- [P296] **DEFINICIÓN** — mHealth = práctica médica/salud pública soportada dispositivos móviles: teléfonos, dispositivos monitoreo paciente, PDAs, dispositivos wireless (WHO GOe)
- [P297] **HECHO** — suscriptores teléfono móvil crecieron <1B (2000) → >10B (2020), superando población mundial 7.88B; 93% mundo tiene acceso red mobile-broadband
- [P298] **HECHO** — taxonomía Labrique et al. (2013): 12 dominios aplicación mHealth comunes incluyendo educación cliente, sensores/diagnósticos POC, registros, recolección datos, EHR, soporte decisión
- [P299] **HECHO** — apps salud: ~40,000 (2013) → 165,000 (2015) → >318,000 (2018); >200 apps agregadas diariamente; dos tercios apuntan wellness, un cuarto gestión enfermedad
- [P300] **HECHO** — justificación SMS para mHealth: (1) más económico que llamadas, (2) versátil, (3) recuperado conveniencia usuario, (4) disponible todos tipos teléfono
- [P301] **HECHO** — WHO publicó primeras guías evidence-based intervenciones salud digital 2019
- [P302] **HECHO** — FDA publicó guidance mobile medical apps 2013; supervisará subconjunto risk-based apps (alto riesgo requiere aprobación premarket); ejerce discreción regulatoria apps riesgo moderado
- [P303] **HECHO** — Goldman Sachs pronosticó oportunidad ahorros $305B healthcare digital para US
- [P304] **HECHO** — mercado mHealth ~$13B 2015; anticipado ~40% crecimiento 6 años
- [P305] **HECHO** — evidencia alta calidad identificada intervenciones mHealth: cesación tabaco + adherencia terapia antirretroviral (Cochrane reviews)
- [P306] **HECHO** — 5 poblaciones pacientes con evidencia clínica apps pueden reducir utilización cuidado agudo ahorrando US ~$7B/año: prevención diabetes, diabetes, asma, rehab cardíaca, rehab pulmonar (IQVIA, 2017)
- [P307] **HECHO** — MARS (Mobile App Rating Scale) = herramienta 5 medidas calidad app: engagement, funcionalidad, estética, información, calidad subjetiva (Stoyanov et al., 2015)
- [P308] **HECHO** — tres mayores desafíos mHealth US (Economist Intelligence): (1) malinterpretación datos paciente, (2) decisiones salud pobres, (3) riesgos privacidad datos/legales
- [P309] **RESTRICCIÓN** — herramientas soporte decisión AI-driven tienen categorías sesgo inherentes: sesgo captura conocimiento + sesgo procesamiento (Gurupur & Wan, 2020)
- [P310] **HECHO** — ONC Federal Health IT Strategic Plan 2020-2025: 7 áreas oportunidad incluyendo empoderamiento paciente, value-based care, interoperabilidad, nuevas tecnologías, reducción carga regulatoria

### Ch 15: Personal Health Records

- [P311] **DEFINICIÓN** — PHR = aplicación privada/segura a través de la cual individuo puede acceder/gestionar/compartir información salud; puede incluir datos ingresados consumidor y/o datos farmacias/labs/proveedores
- [P312] **DEFINICIÓN** — tres aspectos esenciales PHR: (1) agregador/almacenamiento información, (2) suite herramientas gestión salud, (3) intencionalmente evita palabra "paciente" — para salud/bienestar no solo enfermedad
- [P313] **DEFINICIÓN** — standalone (untethered) PHR = almacena info dispositivo individuo o web app separada EHR; connected (tethered) PHR = enlazado clínica/sistema salud único, frecuentemente llamado portal paciente
- [P314] **HECHO** — VHA MyHealtheVet (2003) = uno primeros portales paciente; dos niveles: PHR web standalone para cualquiera + funciones completas EHR-linked para veteranos
- [P315] **HECHO** — concepto Blue Button desarrollado 2010 workgroup Markle Foundation; despliegue inicial VHA agosto 2010; clic único pacientes acceder registros formato legible humano/máquina
- [P316] **HECHO** — Google Health (2008-12) y Microsoft HealthVault (2007-19) discontinuados principalmente por falta adopción generalizada; Apple Health lanzado 2018
- [P317] **HECHO** — Stage 2 Meaningful Use: pacientes deben acceder datos EHR electrónicamente; ≥5% pacientes deben usar; regla VDT: view/download/transmit info ≤36h alta hospital o 4 días visita ambulatoria
- [P318] **HECHO** — 21st Century Cures Act 2.0: clínicos deben proveer pacientes registros electrónicos "sin demora" y sin cargo; disponible descarga smartphone/app fin 2022
- [P319] **HECHO** — sistemas hospital ofreciendo acceso online paciente EHR: 27% (2012) → 93% (2017)
- [P320] **HECHO** — encuesta HINTS: uso paciente registros médicos online 25.6% (2014) → 31.4% (2018) → 39.5% (2020)
- [P321] **HECHO** — usuarios PHR más frecuentes: jóvenes, non-Hispanic white, femenino, ingreso mayor; feature más usada = revisión resultados lab
- [P322] **HECHO** — ~25% estadounidenses usan smartwatch/fitness tracker; estimado 1M GB datos salud por persona durante vida
- [P323] **HECHO** — estándares intercambio datos interoperabilidad PHR: CCR, CDA, CCD, FHIR
- [P324] **HECHO** — HIPAA (1996) requiere individuos acceso registros salud upon request + audit trail quién accedió su info
- [P325] **HECHO** — Quadruple Aim = mejorar experiencia paciente + mejorar salud poblacional + reducir costos + mejorar balance vida-trabajo proveedor (Berwick/IHI triple aim + Bodenheimer/Sinsky cuarto aim)
- [P326] **HECHO** — barreras adopción PHR: preferencia comunicación presencial (64%), sin necesidad percibida (49%), incomodidad computadores (26%), preocupaciones privacidad (23%), problemas login (19%), múltiples portales (9%)
- [P327] **HECHO** — pacientes incentivados por proveedor usar PHR ~2x más probabilidad acceder; prácticas usando ≥5 técnicas promoción vieron ~3x mayor adopción PHR
- [P328] **⚠ TENSIÓN** — PHR incrementa mensajería/comunicación paciente → incrementa carga trabajo clínico; mucho este workload no reembolsable; evidencia limitada comunicación incrementada mejora calidad

### Ch 16: Social Media Tools for Health Informatics

- [P329] **DEFINICIÓN** — social media (término primer uso 2004) = comunicación digital donde usuarios crean contenido información publicar/compartir online relacionado intereses personales/profesionales
- [P330] **HECHO** — seis principios core diferenciando social media: participación, colectividad, transparencia, independencia, persistencia, emergencia (Kaplan & Haenlein, 2010)
- [P331] **HECHO** — herramientas social media 5 categorías: (1) redes sociales (Facebook/LinkedIn), (2) blogging/wikis, (3) microblogging (Twitter), (4) social bookmarking (Pinterest/Reddit), (5) video/imagen (YouTube/Instagram/TikTok)
- [P332] **HECHO** — 2021: 70% estadounidenses usan social media (subió 65% en 2015); YouTube/Facebook dominantes; adultos <30 favorecen Instagram/TikTok/Snapchat
- [P333] **HECHO** — >40% consumidores healthcare influenciados social media para asuntos salud; solo 26% hospitales US usando social media; ≥53% médicos tienen página Facebook oficina
- [P334] **REGLA** — proveedores healthcare deben mantener cumplimiento HIPAA en social media; PHI incluye info salud individualmente identificable; detalles perfil pueden revelar identidad paciente
- [P335] **REGLA** — ANA Code Ethics: enfermeros obligados mantener confidencialidad toda info paciente; AMA Code: médicos no deben compartir info confidencial sin consentimiento previo; estándares aplican incluso fuera roles clínicos
- [P336] **HECHO** — guías profesionales social media existen de: AMA, ANA, NCSBN, NMC, RCN, INRC, Federation of State Medical Boards
- [P337] **DEFINICIÓN** — infodemic = explosión información (verdadera + falsa) durante crisis salud pública causando confusión/desconfianza/miedo (concepto WHO); ejemplificado durante COVID-19
- [P338] **DEFINICIÓN** — apomediation = estar disponible dirigir consumidores información internet alta calidad en vez interponerse entre consumidor e información (Eysenbach, 2008)
- [P339] **HECHO** — Dear Pandemic (lanzado marzo 2020 Instagram/Facebook): equipo científicas interdisciplinario femenino combatiendo desinformación COVID-19 vía comunicación científica social media
- [P340] **HECHO** — cyberbullying laboral estimado 3%-43% (D'Souza et al., 2018); social media habilita cyberstalking/acoso anónimo
- [P341] **HECHO** — NLRB/NLRA protege derechos empleados discutir condiciones trabajo incluyendo vía social media; comenzó recibir cargos sobre políticas social media empleadores 2010
- [P342] **RESTRICCIÓN** — políticas social media deben balancear: no demasiado lenientes (inefectivas) / no demasiado estrictas (contraproducentes); deben ser congruentes legislación federal/estatal/local
- [P343] **REGLA** — política social media debe abordar: límites divulgación información, integridad profesional, cuentas personales/profesionales separadas, límites uso aceptable, consecuencias, congruencia regulaciones

## Section 4: Lifecycle Management

### Ch 17: Project Management Principles

- [P344] **DEFINICIÓN** — project management = enfoque sistemático planificar/guiar procesos proyecto inicio a fin
- [P345] **DEFINICIÓN** — proyecto = emprendimiento temporal/time-bound entregando producto/servicio particular, involucrando conocimiento/habilidades ejecutar plan acción (PMI 2014)
- [P346] **DEFINICIÓN** — program management = coordinación cohesiva varios proyectos interrelacionados gestionados juntos; menos costoso/más eficiente controlar proyectos similares juntos
- [P347] **DEFINICIÓN** — portfolio management = gestión centralizada procesos/metodologías/tecnologías usadas por PMs/PMOs; determina mix recursos óptimo para objetivos operacionales/financieros
- [P348] **HECHO** — estudios PMI: 80% proyectos fallan cumplir objetivos sin metodología proyecto estructurada (PMI 2006)
- [P349] **HECHO** — PMI Pulse Profession: organizaciones alto rendimiento cumplen metas planeadas 2.5x más frecuentemente que bajo rendimiento; alto rendimiento desperdician ~13x menos dinero
- [P350] **ALCANCE** — cuatro grupos proceso PM: Initiation, Planning, Execution, Closure
- [P351] **REGLA** — cada fase PM tiene entregables/pasos específicos que deben completarse antes siguiente fase
- [P352] **DEFINICIÓN** — Initiation = recopilar info/estimaciones recursos iniciales evaluar viabilidad proyecto; incluye propuesta formal/business case, aprobación capital
- [P353] **REGLA** — omitir/completar inadecuadamente fase planificación típicamente obstaculiza progreso durante vida proyecto y afecta resultados largo plazo
- [P354] **DEFINICIÓN** — scope creep = aumento no controlado desde alcance proyecto original; debe gestionarse vía documento scope evitar retrasos
- [P355] **HECHO** — nueve áreas conocimiento PMI: integración proyecto, gestión alcance, gestión tiempo, gestión costos, gestión calidad, gestión HR, gestión comunicación, gestión riesgos, gestión adquisiciones
- [P356] **DEFINICIÓN** — WBS (Work Breakdown Structure) = descomposición entregables proyecto en tareas trabajables parte plan proyecto general
- [P357] **DEFINICIÓN** — project charter/management plan = delinea dirección/gestión ejecución proyecto general, monitoreo, procesos control scope/schedule/recursos
- [P358] **REGLA** — resource managers no deberían servir simultáneamente como project managers — necesidades conflictivas afectan negativamente resultados proyectos HIT
- [P359] **DEFINICIÓN** — portfolio rationalization = proceso evaluar/refinar contenidos portfolio; Gartner provee 4 desafíos clave
- [P360] **HECHO** — 10%-20% aplicaciones responsables gasto operaciones/mantenimiento/mejoras (Gartner)
- [P361] **REGLA** — racionalización aplicaciones debería enfocarse primero en aplicaciones representando 80% presupuesto dentro área prioridad dada
- [P362] **HECHO** — organizaciones altamente efectivas portfolio management: 62% cumplieron/excedieron targets ROI esperados; 89% senior managers entendieron significado/uso portfolio management
- [P363] **REGLA** — más efectivo priorizar inicio año fiscal, no re-priorizar continuamente a menos issues urgentes ocurran

### Ch 18: Strategic Planning and Information System Selection

- [P364] **DEFINICIÓN** — plan estratégico = documento formal proyectando 3-5 años futuro; involucra declaraciones visión/misión, objetivos, estrategias; puede usar análisis SWOT
- [P365] **HECHO** — mayoría organizaciones healthcare ya usan EHR por incentivos Meaningful Use bajo ARRA; implementación EHR ahora más probable reemplazo que transición papel-a-EHR
- [P366] **DEFINICIÓN** — burnout clínico = reacción estrés largo plazo marcada agotamiento emocional, despersonalización, falta logro personal (definición AHRQ); EHRs contribuyente conocido
- [P367] **REGLA** — implementar EHR es proyecto clínico — clínicos deberían estar altamente involucrados y servir líderes proyecto; líderes mejor elegidos de opinion leaders clínicos
- [P368] **ALCANCE** — Clayton's Framework implementación EHR (5 componentes en orden): 1) Compromiso institucional, 2) Liderazgo, 3) Personas, 4) Infraestructura, 5) Software
- [P369] **HECHO** — costos EHR incluyen: hardware, licensing software, implementación/configuración/soporte, training (incluyendo productividad clínico perdida), mantenimiento continuo
- [P370] **REGLA** — equipo proyecto EHR debería tener amplia representación clínica (enfermeros, médicos, farmacéuticos); expertos business/admin no deberían tomar decisiones clave features/funcionalidad/workflow a menos también provean cuidado paciente
- [P371] **DEFINICIÓN** — RFI = Request for Information (fase planificación); RFP = Request for Proposals (elicita ofertas vendor, scoring ponderado); RFQ = Request for Quotation (requerimientos claros)
- [P372] **REQUISITO** — contenidos RFP: background/descripción institucional, calificaciones vendor, requerimientos específicos (funcional/técnico/negocio), timing, restricciones financieras, proceso/timeline/criterios selección
- [P373] **REGLA** — site visits organizadas por comprador más valiosas que organizadas por vendor; 5 min con clínico cansado en scrubs genera más info que hora con ejecutivo
- [P374] **DEFINICIÓN** — best of breed vs sistema integrado = usar vendors departamentales especializados vs vendor EHR único para todos sistemas; tendencia secular favorece vendors dominantes
- [P375] **HECHO** — mensajería estándar entre sistemas vendors diferentes usa protocolos como HL7 2.4
- [P376] **REGLA** — contrato debería incluir: alcance/costos servicios implementación, licensing software/hardware costos, pagos mantenimiento anuales, criterios aceptación, cláusulas rendimiento/falla
- [P377] **DEFINICIÓN** — BATNA (Best Alternative To Negotiated Agreement) = mantener opción vendor backup durante negociaciones contrato
- [P378] **REGLA** — organización no compra EHR — lo licencia; pagos mantenimiento constituyen mayoría pagos vendor con el tiempo
- [P379] **RESTRICCIÓN** — contrato debe abordar: responsabilidad por daño paciente problemas software, remedios por misconfiguration vendor causando downtime, cláusulas hold harmless

### Ch 19: Contract Negotiations and Software Licensing

- [P380] **DEFINICIÓN** — acuerdo licencia software = contrato vinculante entre vendor (licensor) y HCO (licensee) creando obligaciones legalmente ejecutables como prerequisito uso software
- [P381] **REGLA** — formulario acuerdo vendor es unilateral, diseñado proteger vendor no HCO; HCO no debería subestimar su leverage negociar mejores términos
- [P382] **REQUISITO** — composición equipo negociación contrato: CFO, abogado (IP/contract law), CIO, usuarios clave (CMIO/CNIO), administradores contrato, compliance officer (HIPAA/Stark/anti-kickback), experto seguridad
- [P383] **DEFINICIÓN** — copyright protege software como "work of authorship" — protege expresión no ideas/métodos/hechos; patente protege invención; trade secret protege info no generalmente conocida
- [P384] **DEFINICIÓN** — SaaS = Software as a Service; modelo distribución software donde aplicaciones hosted por vendor, disponibles clientes vía red
- [P385] **DEFINICIÓN** — on-premises licensing = software instalado/ejecuta computador/red HCO; cloud licensing = software reside/ejecuta servidores vendor, HCO accede vía internet
- [P386] **DEFINICIÓN** — source code = lenguaje programación legible humano; executable code = código máquina compilado; interpretive code = interpretado on-the-fly runtime
- [P387] **REGLA** — cláusula Entire Agreement significa HCO debe poner todo en lo que confió en acuerdo escrito; declaraciones verbales/demos/materiales marketing no cuentan a menos incorporados
- [P388] **REGLA** — respuesta RFP vendor debería incorporarse en acuerdo licencia; si vendor objeta, HCO debería insistir confió en respuesta para selección vendor
- [P389] **ALCANCE** — componentes principales acuerdo licencia: definiciones, cronograma, alcance licencia, alcance uso, derivative works, escrow, especificaciones, warranties, SLA, aceptación, mantenimiento/soporte, pagos, resolución disputas, terminación, limitaciones responsabilidad, cláusulas especiales
- [P390] **DEFINICIÓN** — software escrow = tercero neutral mantiene source code/documentación; condiciones liberación incluyen bancarrota vendor, breach mantenimiento, discontinuación soporte
- [P391] **DEFINICIÓN** — SaaS escrow = incluye compañía escrow manteniendo mirror/solución similar propio servidor activable si condición liberación ocurre
- [P392] **DEFINICIÓN** — SLA = Service Level Agreement definiendo niveles servicio y consecuencias falla; niveles comunes abordan uptime, rendimiento, tiempo resolución, remedios
- [P393] **HECHO** — 99.999% uptime generalmente considerado gold standard; 100% uptime típicamente no factible — cada incremento hacia 100% aumenta gastos dramáticamente
- [P394] **REGLA** — downtime mantenimiento programado comúnmente no contabilizado como downtime; eventos force majeure frecuentemente excluidos cálculos uptime
- [P395] **RESTRICCIÓN** — remedio SLA típicamente crédito contra pagos futuros; si crédito limitado 25% tarifa SaaS, HCO aún paga 75% incluso 0% uptime — HCO debería insistir derecho terminación si niveles SLA significativa/continuamente incumplidos
- [P396] **HECHO** — tarifas mantenimiento/soporte típicamente 15%-22% tarifa licencia inicial/año; rango 10%-40%; bajo SaaS, incluidas tarifas recurrentes
- [P397] **REGLA** — compromiso soporte/mantenimiento vendor debería ser ≥5 años, suficiente cubrir ROI esperado; HCO no debería quedar bloqueado usar servicios mismo período — preservar derecho terminación
- [P398] **REGLA** — HCO debería insistir terminación por breach requiere: 1) breach "material," 2) notificación escrita, 3) oportunidad cura 30 días; si cura necesita >30 días, extensión si cura comenzada
- [P399] **REGLA** — para software mission-critical, HCO debería negociar licencia sobreviva terminación — vendor retiene protecciones IP pero HCO continúa uso dentro alcance licenciado
- [P400] **REGLA** — cláusula período transición: si acuerdo terminado/expira y seguridad paciente amenazada, HCO tiene derecho período transición razonable (hasta 1 año) migrar solución sustituta
- [P401] **DEFINICIÓN** — limitation of liability = limita responsabilidad agregada vendor (e.g., tarifa licencia pagada); estrategia HCO: negociar tope múltiplo tarifa licencia (300%-500%)
- [P402] **DEFINICIÓN** — exclusion of liability = excluye totalmente ciertos tipos daño de recuperación (consecuenciales, indirectos, especiales, punitivos, incidentales, pérdida ganancias/datos)
- [P403] **REGLA** — cláusulas feedback pueden requerir HCO asignar propiedad sugerencias/ideas/mejoras a vendor; como máximo, debería otorgar vendor solo licencia no exclusiva usar feedback "as is"
- [P404] **REGLA** — acuerdo licencia debería prohibir vendor usar nombre/marca/logo HCO en marketing sin consentimiento escrito
- [P405] **REGLA** — propiedad datos HCO debe especificarse en acuerdo, especialmente datos agregados/salud poblacional; provisiones deberían proteger datos paciente incluso si de-identificados

### Ch 20: Implementing and Upgrading an Information System

- [P406] **HECHO** — ARRA promulgada 2009, generando HITECH Act; objetivo primario: cada persona US tenga registro médico digital certificado 2014 con intercambio información salud electrónica
- [P407] **HECHO** — HITECH creó programa incentivos $27B federalmente financiado proveyendo pagos Medicare/Medicaid 5-10 años a proveedores/hospitales elegibles/critical access hospitals
- [P408] **HECHO** — MU Stage 1 comenzó 2011 (captura datos paciente); Stage 2 comenzó 2014 (prácticas clínicas avanzadas/portales paciente); Stage 3 comenzó 2017 (interoperabilidad/resultados paciente)
- [P409] **HECHO** — CCHIT comenzó testear/certificar aplicaciones software 2006; cesó operaciones 2014; ONC ahora gestiona programa certificación EHR (comenzó 2010)
- [P410] **HECHO** — adopción EHR hospitales US: 16% (2009) → 35% (2011) → 76% EHR básico (2014) → 9 de 10 hospitales usando EHR informar práctica (2019 reporte AHA)
- [P411] **HECHO** — 21st Century Cures Act firmada diciembre 13, 2016; objetivo: mejorar acceso/intercambio/utilización electrónica información salud pacientes/proveedores
- [P412] **DEFINICIÓN** — information blocking = práctica por desarrollador HIT, red/exchange información salud, o proveedor healthcare probablemente interfiriendo acceso/intercambio/uso EHI
- [P413] **HECHO** — Cures Act especifica 8 excepciones information blocking: Preventing Harm, Privacy, Security, Infeasibility, Health IT Performance, Licensing, Fees, Content/Manner
- [P414] **HECHO** — USCDI requiere 8 tipos notas clínicas disponibles pacientes sin cargo: consulta, resumen alta, H&P, narrativas imagen, reportes lab, reportes patología, notas procedimiento, notas progreso
- [P415] **DEFINICIÓN** — e-iatrogenesis = tipo crítico nuevo errores introducidos por EHRs, incluyendo errores yuxtaposición (seleccionar paciente/medicamento equivocado de lista) (Weiner et al. 2007)
- [P416] **HECHO** — estudio TRIP (AHRQ 1999): promedio 10-20 años incorporar nuevos hallazgos clínicos práctica general ("lethal lag"); CDS/EBP puede acelerar
- [P417] **DEFINICIÓN** — scope creep contexto SDLC = expansión no controlada alcance producto/proyecto sin ajustes tiempo/costo/recursos (HIMSS 2017); mitigado control cambios estricto
- [P418] **ALCANCE** — grupos proceso PMBOK: Initiating, Planning, Executing, Monitoring/Controlling, Closing; etapas SDLC: Planning, Requirements Gathering, Design, Coding, Testing, Deployment/Maintenance
- [P419] **DEFINICIÓN** — superuser = staff organizacional con training adicional que entiende nuevos workflows, provee soporte at-the-elbow durante go-live y después
- [P420] **DEFINICIÓN** — UAT (User Acceptance Testing) = etapa testing final antes go-live donde vendor/HCO depuran software funcionalidad final; tres features clave: estrategia, escenarios, scripts
- [P421] **DEFINICIÓN** — big bang go-live = todas aplicaciones/módulos implementados a la vez; menor costo total, implementación más corta, pero caída productividad significativa inicialmente
- [P422] **DEFINICIÓN** — phased/incremental go-live = procesos viejos y nuevos coexisten; permite tiempo para build/cambios workflow pero mayor costo total, duración más larga
- [P423] **REGLA** — fecha go-live debería evitar fines semana/lunes/viernes/feriados importantes cuando soporte vendor menos disponible; excepciones: sistemas financieros (deben iniciar medianoche 1° día mes)
- [P424] **DEFINICIÓN** — change freeze/moratorium = período (típicamente 1-2 semanas antes a ~1 semana después go-live) donde ningún otro cambio sistema permitido
- [P425] **DEFINICIÓN** — data abstraction = proceso ingresar/poblar chart electrónico con datos clínicos registros papel u otras fuentes
- [P426] **REGLA** — training end-user debería ocurrir no más 4-6 semanas antes go-live facilitar retención; ambiente práctica disponible post-clase ejercicios competencia
- [P427] **REQUISITO** — categorías training: superuser training (training adicional + comprensión workflow), role-based training (médico/enfermero/terapeuta), process-based training (workflow como admisión hospital)
- [P428] **HECHO** — 2015 Edition Cures Update introdujo criterios certificación técnica requiriendo HL7 FHIR Release 4 para export/acceso paciente EHI, más criterios cybersecurity (encripción, auth multi-factor)
- [P429] **HECHO** — Tall Man lettering (mixed-case) usada nombres medicamentos look-alike per recomendación ISMP disminuir errores medicación; ejemplos: NiFEDipine vs niCARdipine, DOBUTamine vs DOPamine

### Ch 21: Downtime and Disaster Recovery for HIS

- [P430] **DEFINICIÓN** — downtime = período sistemas computador no disponibles usuarios; causado errores humanos, fallas software/hardware, cables energía cortados, malware/ransomware, desastres naturales
- [P431] **HECHO** — 2016 Ponemon Institute: costo promedio downtime healthcare $740,357 por incidente (~$8,800/min)
- [P432] **HECHO** — 2020: 92 ataques ransomware afectaron >600 clínicas/hospitales, >18M registros pacientes; costo estimado ~$21B (Comparitech/Bischoff 2021)
- [P433] **REGLA** — planificación downtime debería ocurrir desde inicio proyecto hasta soporte/mantenimiento sistema; debe incluir todos sistemas/infraestructura existentes
- [P434] **ALCANCE** — elementos infraestructura IT planificación downtime: software EHR, sistemas clínicos/ancilares, PACS, apps lab/cardiología/radiología, software revenue cycle, interfaces/engine interfaces, enterprise data warehouse
- [P435] **ALCANCE** — elementos infraestructura física: servidores, almacenamiento, energía eléctrica, switches/hubs/firewalls red, puntos acceso wireless, dispositivos biomédicos, workstations/impresoras, componentes edificio, UPS, generadores
- [P436] **DEFINICIÓN** — CMDB (Configuration Management Database) = best practice ITIL mantener inventario/documentación sistema con ítems configuración únicos organización
- [P437] **ALCANCE** — niveles downtime: Level 1 (parte sistema, <1h, impacto mínimo) → Level 2 (sistema completo, hasta 4h) → Level 3 (múltiples sistemas, >4h) → Level 4 (todos sistemas/red, causa raíz conocida) → Level 5 (todos sistemas/red, ransomware/catastrófico, rebuild requerido)
- [P438] **DEFINICIÓN** — hot site = facilidad recuperación con hardware standby, habilita recuperación Tier I ≤24h; warm site = intermedio; cold site = capacidad hospedar sistemas pero tiempo recuperación mayor (e.g., 30 días)
- [P439] **OBLIGACIÓN** — organizaciones obligadas mantener planes contingencia/desastre per HIPAA security rule 1996, requerimientos HHS, cuerpos acreditación
- [P440] **DEFINICIÓN** — business continuity management = complementario disaster recovery; alcance mayor incluyendo disponibilidad servicios admin/healthcare, determinando qué sistemas recuperar primero usando sistema tiers
- [P441] **ALCANCE** — tiers business continuity: Tier I (crítico, recuperar primero, ≤24h, requiere hot site); Tier II (≤72h); Tier III (≤1 semana); Tier IV (≤1 mes)
- [P442] **DEFINICIÓN** — Downtime Determinator = herramienta risk assessment (Brazelton/Lyons); x-axis = tiempo recuperación, y-axis = impacto/riesgo; grafica 7 componentes riesgo en 4 cuadrantes
- [P443] **REGLA** — sistemas redundantes/backup deben proveer subconjunto datos críticos durante downtime: demographics, órdenes, MAR, vitales recientes, valores lab, reportes imagen, notas progreso proveedor
- [P444] **REGLA** — máquinas downtime redundantes deben cumplir requerimientos HIPAA seguridad/privacidad/confidencialidad; requieren capa encripción extra prevenir robo info si removidas hospital
- [P445] **DEFINICIÓN** — ciclo vida servicio ITIL: estrategia, diseño, transición, operación, mejora continua
- [P446] **REGLA** — manuales planificación desastre deben estar disponibles múltiples formatos media incluyendo formatos no-dependientes red; evaluados/actualizados ≥anualmente y probados/simulados
- [P447] **REGLA** — cada unidad clínica/negocio necesita políticas/procedimientos downtime específicos; debe incluir instrucciones sobre ingreso datos requerido registro EHR permanente conclusión downtime
- [P448] **REQUISITO** — downtime box best practice: todas unidades paciente/áreas negocio mantienen caja física con formularios documentación, instrucciones papel, formularios ≥24 horas, instrucciones restocking
- [P449] **REGLA** — cinco componentes plan comunicación downtime: quién necesita saber, qué detalles necesarios, qué media/modos usados, quién comunica qué, qué sistemas/workflows afectados
- [P450] **HECHO** — teléfonos analógicos deberían estar disponibles áreas clave hospital (identificados color diferente, e.g., rojo) porque funcionan durante downtimes red/eléctricos cuando teléfonos VOIP no
- [P451] **REGLA** — ejercicios desastre/downtime requeridos por agencias regulatorias/acreditación (The Joint Commission); training todos nuevos empleados orientación, actualizado ≥anualmente como componente competencia

## Section 5: Usability, Analytics, and Education

### Ch 22: Improving the User Experience for Health IT

- [P452] **DEFINICIÓN** — usabilidad (ISO 9241-11, 1998) = extensión producto puede ser usado por usuarios específicos contexto específico lograr objetivos específicos con efectividad, eficiencia, satisfacción
- [P453] **DEFINICIÓN** — tres objetivos usabilidad ISO: (1) efectividad = precisión/completitud logro objetivos incluyendo seguridad; (2) eficiencia = recursos gastados relativo precisión; (3) satisfacción = comfort/aceptabilidad usuarios asocian con producto
- [P454] **DEFINICIÓN** — UCD = tres axiomas: (1) enfoque temprano/central en usuarios, (2) diseño iterativo, (3) medidas sistemáticas interacciones usuario-producto (Gould & Lewis; Rubin & Chisnell 2008)
- [P455] **REGLA** — UCD requiere mínimo tres rondas diseño iterativo; un diseño nunca es adecuado
- [P456] **DEFINICIÓN** — human factors (HFES 2012) = disciplina científica entendiendo interacciones humanos/otros elementos sistema optimizar bienestar humano y rendimiento sistema general
- [P457] **DEFINICIÓN** — ergonomía = intercambiable con human factors en Europa; en US enfoca rendimiento humano con características físicas herramientas/sistemas; distinción: ergonomía física (diseño workstation) vs ergonomía cognitiva (diseño interfaz)
- [P458] **DEFINICIÓN** — HCI = estudio cómo personas diseñan, implementan, evalúan sistemas computador interactivos contexto tareas/trabajo usuarios
- [P459] **DEFINICIÓN** — cognitive informatics combina ciencias cognitivas/información aumentar comprensión/descripción/predicción productos/resultados healthcare; puede usar miles/millones interacciones registradas vs 5-15 usuarios estudios usabilidad
- [P460] **HECHO** — TJC 2015 evaluó 3375 reportes eventos adversos, identificó 120 eventos sentinel relacionados HIT; 1/3 provenientes factores interfaz humano-computador, 24% issues workflow/comunicación
- [P461] **HECHO** — AMA 2014 emitió llamado firmado 30 organizaciones médicas soluciones EHRs pobremente diseñados
- [P462] **HECHO** — evaluaciones admisión acute care pueden tomar 30-60 minutos involucrando 532 clicks
- [P463] **HECHO** — frameworks HCI disponibles: FITT (Ammenwerth 2006), UFuRT/TURF (Zhang & Butler), framework error technology-induced (Borycki 2012), SEIPS (Carayon 2020)
- [P464] **DEFINICIÓN** — SEIPS 3.0 = modelo centrado sistemas trabajo y centralidad paciente; enfoque expandido journey paciente, episodios cuidado distribuidos tiempo/localización
- [P465] **DEFINICIÓN** — framework HHCI elementos: usuarios, productos, contexto, tareas, información, interacciones, timeline desarrollo; información = mecanismo intercambio (Staggers)
- [P466] **DEFINICIÓN** — discount usability methods (Nielsen 1993) = técnicas reduciendo usuarios requeridos, usando prototipos diseño temprano; técnica más común = heuristic evaluation (HE)
- [P467] **HECHO** — HE por 3-5 expertos dual domain puede encontrar 81-90% problemas usabilidad existentes (Nielsen 1992)
- [P468] **HECHO** — sets heurísticos disponibles: Nielsen 10 (1995), Zhang et al. 14 (2003), Dix et al. 10 (2004), Shneiderman 8 golden rules (2005), HIMSS 9 principios usabilidad (2009)
- [P469] **HECHO** — escala severidad Zhang: 0=sin problema, 1=cosmético, 2=menor, 3=mayor, 4=catástrofe usabilidad (debe corregirse antes release, especialmente relacionado seguridad paciente)
- [P470] **DEFINICIÓN** — think-aloud protocol = usuarios hablan en voz alta mientras interactúan producto; tan pocos como 5 usuarios pueden detectar 60-80% errores diseño (Nielsen); 5-8 usuarios suficientes mayoría tests usabilidad tempranos
- [P471] **DEFINICIÓN** — task analysis = término genérico >100 técnicas desde análisis tarea cognitiva a interacciones usuario observables; usado temprano ciclo vida sistemas
- [P472] **HECHO** — cuestionarios usabilidad: SUS (Brooke 1986, estándar industria, 10 ítems, disponible público), QUIS, Purdue Usability Testing Questionnaire (100 open-ended), SUMI
- [P473] **REGLA** — investigadores recomiendan ≥15 usuarios testing usabilidad sumativo (Virzi 1992)
- [P474] **HECHO** — FDA ha requerido testing usabilidad dispositivos médicos >20 años; otros vendors HIT/organizaciones salud solo comenzando emplear principios usabilidad
- [P475] **HECHO** — ONC publicó ONC Change Package for Improving EHR Usability ayudar sistemas healthcare incorporar conceptos/herramientas usabilidad básica (2018)
- [P476] **HECHO** — Nielsen Norman Group estimó ganancias productividad rediseño intranet: 8x costos (1000 empleados), 20x (10,000), 50x (100,000); incremento productividad usuario promedio 161%

### Ch 23: Data Science and Analytics in Healthcare

- [P477] **DEFINICIÓN** — data science = conocimiento, organización, testing, entendimiento métodos/procesos científicos asociados datos estructurados/no estructurados; ecosistema incluye datos, computación, programación, estadística/analytics, ML, matemáticas
- [P478] **DEFINICIÓN** — 5 Vs big data: Volume, Velocity, Variety, Veracity, Value (Eaton 2012)
- [P479] **DEFINICIÓN** — Volume = cantidad datos pura. Velocity = velocidad generación/cambio datos. Variety = datos múltiples fuentes/formatos simultáneamente
- [P480] **DEFINICIÓN** — Veracity = precisión/completitud ("verdad") datos. Value = propósitos recolectar/procesar/analizar datos deben llenar necesidad
- [P481] **HECHO** — gastos healthcare US = 17.7% PIB 2019, incremento 4.6% año anterior (CMS 2020)
- [P482] **DEFINICIÓN** — tres categorías analytics: (1) descriptive = análisis datos retrospectivo; (2) predictive = modelos matemáticos relaciones resultados; (3) prescriptive = modelos determinando acciones alternativas alto valor
- [P483] **DEFINICIÓN** — EDA incluye estadísticas descriptivas, resúmenes, visualizaciones datos; produce dashboards/reportes decision-makers
- [P484] **DEFINICIÓN** — tipos problemas predictive analytics: regression (predicción outcome), classification (predicción categoría), clustering (agrupación observaciones similares), association rules
- [P485] **DEFINICIÓN** — métodos prescriptive analytics: decision trees, modelos colas, programación matemática/optimización, simulación
- [P486] **DEFINICIÓN** — CRISP-DM = proceso estándar cross-industry data mining; 6 fases: comprensión negocio, comprensión datos, preparación datos, modelado, evaluación, despliegue; naturaleza cíclica/iterativa
- [P487] **DEFINICIÓN** — ETL = Extract, Transform, Load; proceso database administrators acceder datasets; gramática manipulación datos: select, filter, mutate, arrange, group by, summarize, join
- [P488] **DEFINICIÓN** — NLP / extracción información = métodos identificando información significativa secuencias texto; pipeline multistep computacionalmente costoso lidiando desambiguación/negación palabras
- [P489] **HECHO** — consideraciones preprocessing datos codificados: distribución, frecuencia, datos missing, sparsity, outliers, identificadores, datos erróneos
- [P490] **DEFINICIÓN** — métodos ML: decision trees (C4.5, CART), decision rules, artificial neural networks, support vector machines, ensemble methods (random forests, boosting, bagging), Bayesian networks
- [P491] **DEFINICIÓN** — métricas evaluación modelo regression: MAE, MSE, RMSE. Classification: confusion matrix generando accuracy, sensitivity, specificity, PPV, NPV
- [P492] **DEFINICIÓN** — ROC curve = gráfico fracción false-positive vs fracción true-positive; AUC = probabilidad caso positivo aleatorio rankeado más alto que negativo aleatorio; AUC=0.5 = azar
- [P493] **DEFINICIÓN** — k-fold cross-validation = datos divididos k partes (comúnmente k=10); cada fold usado testing mientras restantes entrenan modelo; genera estimación media + desviación estándar error
- [P494] **HECHO** — diagrama Venn habilidades data science Drew Conway: 3 áreas requeridas = hacking/programación computador, matemáticas/estadística, expertise dominio
- [P495] **HECHO** — categorías herramientas analytics: spreadsheets/visualización (Excel, Tableau, Power BI), programas estadísticos (SAS, SPSS, Weka, KNIME), lenguajes programación (R, Python, Matlab, Scala, Julia)
- [P496] **DEFINICIÓN** — data governance = toma decisiones y autoridad sobre asuntos relacionados datos; incluye estructuras organizacionales, reglas/políticas, derechos decisión, métodos accountability; DGI provee framework 10 componentes
- [P497] **HECHO** — Floridi & Cowls cinco principios core AI ético: beneficencia, no-maleficencia, autonomía, justicia, explicabilidad
- [P498] **HECHO** — HIPAA Privacy Rule protege PHI incluyendo condición salud física/mental, prestación healthcare, provisiones pago, datos demográficos
- [P499] **HECHO** — Buolamwini & Gebru (2018): datasets análisis facial abrumadoramente sujetos piel clara; tasa error mujeres negras hasta 34.7% vs 0.8% hombres blancos clasificación género comercial

### Ch 24: Safety and Quality Initiatives in Health Informatics

- [P500] **DEFINICIÓN** — calidad cuidado IOM (1990) = grado servicios salud para individuos/poblaciones incrementan probabilidad resultados salud deseados consistentes conocimiento profesional actual
- [P501] **DEFINICIÓN** — seis aims calidad IOM (Crossing Quality Chasm, 2001): safe, effective, patient-centered, timely, efficient, equitable
- [P502] **DEFINICIÓN** — seguridad paciente IOM = libertad lesión accidental por cuidado médico/errores; error = falla acción planificada completarse como previsto o uso plan incorrecto
- [P503] **DEFINICIÓN** — seguridad paciente ICPS/WHO = reducción riesgo daño innecesario asociado healthcare a mínimo aceptable
- [P504] **HECHO** — 2017: 96% facilities acute care usaron EHR certificado, 99% hospitales grandes (>300 camas) tenían HIS efectivo
- [P505] **HECHO** — CDC reporta 72.3% proveedores healthcare office-based usan EHRs/EMRs certificados; ~90% usando algún tipo sistema
- [P506] **DEFINICIÓN** — framework Donabedian = medir calidad basado tres dominios: estructura (atributos setting), proceso (gerencial/clínico), resultados (resultados estructuras/procesos)
- [P507] **DEFINICIÓN** — framework PSQRD construye sobre Donabedian; continuo seguridad-calidad = "vector of egregiousness" — eventos calidad (frecuentes, menor inmediatez) un extremo, eventos seguridad paciente (inmediatos, alta causalidad) otro
- [P508] **DEFINICIÓN** — Singh & Sittig Sociotechnical Model = 8 dimensiones CAS interrelacionadas: infraestructura hardware/software, contenido clínico, HCI, personas, workflow/comunicación, políticas org internas, reglas/regulaciones externas, medición/monitoreo sistema
- [P509] **HECHO** — cinco rights seguridad medicación: paciente correcto, hora correcta, droga correcta, dosis correcta, vía correcta
- [P510] **HECHO** — BCMA/eMAR aprovechan barcoding pulseras paciente/medicamentos asegurar adherencia cinco rights y documentar administración droga tiempo real
- [P511] **HECHO** — adopción smart infusion pump duplicó 2005-2012; encuesta ASHP 2012 mostró 77% tasa adopción IV smart pumps hospitales US
- [P512] **HECHO** — cumplimiento scanning BCMA frecuentemente subóptimo; un estudio encontró cumplimiento solo 55.3% (Franklin 2007); enfermeros bypasean scanning creando workarounds
- [P513] **DEFINICIÓN** — workarounds = cualquier uso sistema operativo fuera protocolo diseñado; más comunes durante etapa implementación, pueden crear nuevas rutas errores
- [P514] **HECHO** — CMS identificó condiciones adquiridas hospital prevenibles (Deficit Reduction Act 2006) por las cuales hospitales no reciben pago adicional; incluye úlceras presión, caídas paciente con lesión
- [P515] **HECHO** — características implementación HIT exitosa: soporte liderazgo, estrategia implementación/adopción comprehensiva, HIT como "herramienta" dentro intervención multifacética, engagement paciente, participación end-user, soporte peer champion
- [P516] **HECHO** — estándares datos calidad requieren: value sets estándar, taxonomías, concept codes, atributos, estructuras datos. Terminologías clave: SNOMED CT, ICD-10 CM, LOINC, RxNorm, CPT-4, NDF-RT, HL7
- [P517] **DEFINICIÓN** — interoperabilidad semántica = datos intercambiados sin pérdida contexto/significado, reutilizables sin esfuerzo especial usuario; requiere todas organizaciones adopten mismos estándares
- [P518] **HECHO** — CMS 2018 renombró EHR Incentive Program a Promoting Interoperability Program
- [P519] **HECHO** — website eCQI coordinado CMS/ONC provee medidas actualizadas, herramientas, recursos para mejora calidad clínica electrónica

### Ch 25: Informatics in the Curriculum

- [P520] **HECHO** — IOM 2003 report listó 5 competencias core todos profesionales salud: patient-centered care, interdisciplinary teams, evidence-based practice, quality improvement, informatics
- [P521] **DEFINICIÓN** — ANA 2022 definición nursing informatics: especialidad que transforma datos en información necesaria y aprovecha tecnologías mejorar equidad/seguridad/calidad/resultados salud/healthcare
- [P522] **HECHO** — ANA primero reconoció nursing informatics como especialidad 1992; integra nursing science, computer science, information science
- [P523] **HECHO** — AACN 2021 Essentials: 10 dominios; Domain 8 = Informatics and Healthcare Technologies con 4 competencias
- [P524] **HECHO** — competencias informática educación médica Hersh et al. (2014): knowledge-based info cuidado paciente, implementación CDS, gestión salud poblacional, privacidad/seguridad, seguridad paciente vía IT, medición calidad, uso HIE, engagement paciente vía PHR/portales, telemedicina, medicina precisión
- [P525] **HECHO** — fellowship clinical informatics ACGME: 5 milestone levels desde fellow entrante a practitioner avanzado; sub-competencias incluyen seguridad paciente, evaluación tecnología, sistemas CDS, project management
- [P526] **HECHO** — dominios informática farmacéutica AACP (revisión 2019): legal/regulatorio, interoperabilidad/estandarización, resultados paciente, informática healthcare/clínica/biomédica, desarrollo/educación practicante, tecnologías emergentes
- [P527] **HECHO** — EU*US eHealth Work Project 2017 encuesta (>1000 respondientes): 5 brechas principales = falta conocimiento/habilidades proveedores, falta conocimiento/habilidades facultad, disponibilidad cursos, calidad/cantidad materiales training
- [P528] **HECHO** — AACN reporta edad promedio facultad enfermería con doctoral degree: profesor 62.4, asociado 57.2, asistente 51.2 años; mayoría no educada sobre informática durante propia formación
- [P529] **HECHO** — cuerpos acreditación health informatics: CAHIIM (health informatics), LCME (medicina), CCNE/ACEN (enfermería), CAPTE (terapia física), AOTA (terapia ocupacional)
- [P530] **HECHO** — cuerpos certificación: ANCC (nursing informatics), ABMS (medical informatics), CPHIMS/HIMSS (CIOs/profesionales salud), CHIME CHCIO (CIOs/ejecutivos IT)
- [P531] **HECHO** — AMIA estableció Advanced Interprofessional Informatics Certification (AIIC) para profesionales informática no-médicos; también colaboró ABMS/ABP certificación subspecialty board clinical informatics
- [P532] **DEFINICIÓN** — LHS = loops feedforward/feedback orientados objetivos creando información accionable mejorar salud poblacional y disminuir costo cuidado evidence-based
- [P533] **HECHO** — HITECH Act 2009 promulgada como parte ARRA; proveyó recursos ONC; soporte financiero/técnico CMS impulsar implementación EHR rápida
- [P534] **HECHO** — 21st Century Cures Act (2016): promueve compartición datos vía interoperabilidad expandida, prohíbe bloqueo datos, manda acceso/portabilidad inmediata información salud electrónica personal
- [P535] **HECHO** — primeros EHRs aparecieron 1960s; versión temprana desarrollada Mayo Clinic, Rochester MN; 1965 ~73 proyectos info hospital/clínica y 29 proyectos almacenamiento/recuperación documentos
- [P536] **HECHO** — ONC 2010 estimó déficit 51,000 trabajadores HIT calificados; otorgó $84M a 16 universidades/community colleges entrenar >50,000 nuevos profesionales HIT; 12 roles workforce HIT clave identificados
- [P537] **HECHO** — dominios informática AMIA: translational bioinformatics, clinical informatics, clinical research informatics, consumer health informatics, public health informatics
- [P538] **HECHO** — ciencia informática es inherentemente interprofesional; se nutre computer science, decision science, information science, management science, cognitive science, data science, teoría organizacional
- [P539] **DEFINICIÓN** — tres categorías teoría pedagogía: behaviorista (cambio comportamiento = "know what"), cognitiva (memoria/motivación/reflexión = "know how"), constructivismo (interpretar/personalizar conocimiento = "know why")
- [P540] **HECHO** — competencia QSEN prelicensure: enfermeros deberían usar información/tecnología comunicar, gestionar conocimiento, mitigar error, soportar toma decisiones en entorno caring/seguro

### Ch 26: Distance Education — A New Frontier

- [P541] **DEFINICIÓN** — educación distancia = instrucción/aprendizaje planificado donde profesor/aprendiz separados por localización; enseñanza/aprendizaje ocurren varios tiempos; material entregado electrónicamente o impreso
- [P542] **DEFINICIÓN** — asynchronous learning = aprendiz ve contenido educacional diferente tiempo que presentado. Synchronous = evento educativo y aprendizaje mismo tiempo. Blended = combinación ambos
- [P543] **DEFINICIÓN** — distributed education = personaliza entorno aprendizaje estilos aprendizaje; métodos delivery más inclusivos; puede incluir distancia, híbrido, on-site
- [P544] **DEFINICIÓN** — eLearning = training involucrando solo medios electrónicos/tecnologías internet; 3 elementos: asíncrono, diferente localización, dispositivos electrónicos interacción. mLearning = dispositivo móvil como herramienta educativa just-in-time
- [P545] **HECHO** — cuatro fases históricas educación distancia: (1) cursos correspondencia (mid-late 1800s), (2) broadcast media/films/radio/TV (1920s-early 1980s), (3) educación online (mid-late 1980s-1990s), (4) contenido user-generated/Web 2.0 (late 1990s-presente)
- [P546] **HECHO** — Anna Ticknor fundó Boston Society to Encourage Studies at Home (1873) — educación superior mujeres por mujeres. Chautauqua Correspondence College fundada 1881
- [P547] **DEFINICIÓN** — CMS/LMS = software permitiendo desarrollo/entrega cursos sin conocimiento programación; LMS más amplio que CMS incluyendo gestión cursos + registración, integración HR, features admin
- [P548] **HECHO** — market share CMS (NYC Design 2021): WordPress 41%, Drupal 19%, OmniUpdate 9.5%, Cascade CMS 7%, Adobe Experience Manager 4%
- [P549] **HECHO** — criterios selección CMS: objetivos/metas, features, integración sistemas institucionales, compatibilidad, base usuarios, customización/mantenimiento, escalabilidad, usabilidad, medidas resultados, cumplimiento SCORM, costo
- [P550] **DEFINICIÓN** — SCORM = Sharable Content Object Reference Model; incentiva estandarización LMSs
- [P551] **DEFINICIÓN** — Community of Inquiry Model: tres conceptos = social presence (comunidad aprendizaje supportive), cognitive presence (construir conocimiento reflexión/discusión), teaching presence (diseñar/guiar experiencias aprendizaje)
- [P552] **DEFINICIÓN** — estilos aprendizaje VARK: Visual (representaciones gráficas), Aural (info escuchada/hablada), Read/Write (palabras todas formas), Kinesthetic (experiencias/hands-on); validado instrumento confiable
- [P553] **HECHO** — DMCA 1998 protege trabajo copyrightable; prohíbe circumvención tecnologías protección, limita responsabilidad proveedor servicio online
- [P554] **HECHO** — TEACH Act 2002 permite performance/display materiales copyrighted educación distancia bajo condiciones: institución acreditada sin fines lucro, solo estudiantes inscritos, live/asíncrono permitido, info copyright provista, acceso time-limited
- [P555] **HECHO** — HEOA 2008: requiere instituciones publicar calculadora precio neto, políticas seguridad/copyright; facultad debe enviar requerimientos libros texto antes registración; instituciones deben verificar identidad estudiante
- [P556] **HECHO** — FERPA requiere colleges/universidades dar estudiantes acceso registros educacionales y mantener confidencialidad registros personally identifiable
- [P557] **HECHO** — Quality Matters = proceso peer review certificar calidad cursos online/blended
- [P558] **DEFINICIÓN** — adult learners quieren educación aplicable inmediatamente situación específica; se apoyan experiencias previas aprendiendo nuevos conceptos; benefician aprendizaje auto-dirigido

## Section 6: Data Governance, Legal, and Regulatory Issues

### Ch 27: Legal Issues, Federal Regulations, and Accreditation

- [P559] **HECHO** — gobierno federal US tres ramas: legislativa, ejecutiva, judicial; cada una juega rol leyes/regulaciones HIT
- [P560] **DEFINICIÓN** — poderes expresos = poderes explícitamente otorgados Congreso (e.g., regular comercio interestatal, recaudar impuestos)
- [P561] **HECHO** — Congreso usó poderes expresos/implícitos implementar HIPAA, requerimientos Meaningful Use, PPACA
- [P562] **REGLA** — ley federal preempta ley estatal conflictiva a menos ley estatal provea mayores protecciones (e.g., California CMIA provee más protecciones privacidad que HIPAA)
- [P563] **HECHO** — dos agencias acreditación hospital principales: The Joint Commission (TJC) y Det Norske Veritas (DNV) Healthcare
- [P564] **HECHO** — FDA regula/aprueba drogas y dispositivos médicos; responsable framework regulatorio risk-based para HIT
- [P565] **HECHO** — CMS emite regulaciones Medicare/Medicaid incluyendo Conditions of Participation; enforce leyes Stark/Anti-Kickback
- [P566] **HECHO** — ONC establece programas/regulaciones mejorar seguridad/calidad/eficiencia vía HIT; establece estándares/criterios certificación EHR
- [P567] **HECHO** — Office Civil Rights enforce cumplimiento HIPAA/HITECH
- [P568] **HECHO** — Department Justice enforce False Claims Act y estatutos Anti-Kickback
- [P569] **HECHO** — HITECH Act aprobada 2009; requirió OCR implementar programa auditoría evaluando cumplimiento HIPAA
- [P570] **DEFINICIÓN** — Stark law (1992) = ley auto-referencia médico para pacientes Medicare/Medicaid; prohíbe referir pacientes designated health services (DHS) a entidades con las que médico tiene relación financiera
- [P571] **ALCANCE** — DHS bajo Stark incluye: lab clínico, terapia física/ocupacional, speech-language pathology, radiología, terapia radiación, durable medical equipment, suministros parenteral/enteral, prótesis, home health, Rx ambulatorio, servicios hospital in/outpatient
- [P572] **REGLA** — dos relaciones financieras activan Stark: (1) interés ownership/inversión médico/familia en entidad DHS; (2) acuerdo compensación con médico/familia (directo o indirecto)
- [P573] **DEFINICIÓN** — Federal Anti-Kickback statute = estatuto criminal prohibiendo intercambio/oferta cualquier cosa valor inducir referencia beneficiario programa healthcare federal (42 U.S.C. 1320a-7b)
- [P574] **HECHO** — PPACA clarificó: conocimiento real o intención específica no necesario para condena Anti-Kickback
- [P575] **HECHO** — penalidad Anti-Kickback: violación única hasta $25,000 multa + hasta 5 años prisión + exclusión mandatoria programa healthcare federal; penalties civiles = triple daños + $50,000/violación
- [P576] **REQUISITO** — criterios safe harbor Anti-Kickback: acuerdos escritos/firmados >1 año; especifica todos servicios/productos/espacio; especifica intervalos/cargos part-time; pago fijado anticipado fair market value no considerando volumen/valor referrals
- [P577] **HECHO** — EHR donation safe harbor creado 2006; revisado/extendido 2021; donor puede pagar hasta 85% costo comprar/implementar tecnología EHR; EHR debe cumplir criterios certificación actuales
- [P578] **REGLA** — cybersecurity donation safe harbor (2021 final rule): protege donación software cybersecurity + cierto hardware sin requerimiento contribución (donor puede cubrir 100%)
- [P579] **DEFINICIÓN** — False Claims Act (FCA) = impone responsabilidad civil persona presentando claim gobierno federal conocido/debería-conocerse falso; penalidades = 3x monto claim + $11,000 por claim
- [P580] **REGLA** — bajo PPACA, proveedor recibiendo sobrepago Medicare tiene 60 días reportar/devolver dinero antes enfrentar responsabilidad FCA
- [P581] **DEFINICIÓN** — Qui Tam suits = ciudadanos privados llevando acciones enforcement FCA; relators pueden recuperar porción juicio/settlement; DOJ revisa todos casos
- [P582] **HECHO** — Healthcare Fraud statute (18 U.S.C. 1347): defraudar knowingly/willfully programa beneficio healthcare → multa/prisión ≤10 años; aplica cualquier pagador (público o privado)
- [P583] **HECHO** — wire fraud: penalidades criminales presentación claims computarizados fraudulentos; cada claim = cuenta separada; hasta $1,000 multa + hasta 5 años prisión por violación
- [P584] **HECHO** — CMS publicó toolkit detección fraude/abuso EHR; recomendaciones clave: features anti-fraude, audit logs operacionales, audit trail mostrando quién modificó registro/cuándo
- [P585] **HECHO** — TJC usa programa survey/audit Standards; DNV usa programa NIAHO integrando ISO 9001 con Medicare Conditions of Participation
- [P586] **HECHO** — TJC Sentinel Event Alert 42 (dic 2008): identificó interfaz humano-máquina + diseño sistema HIT como factores primarios eventos adversos prevenibles
- [P587] **HECHO** — TJC Sentinel Event Alert 54 (mar 2015): analizó >3375 eventos adversos; 3 áreas debilidad mayores: (1) interfaz humano-computador (1/3 eventos), (2) workflow/comunicación, (3) diseño contenido clínico/soporte decisión
- [P588] **HECHO** — clases dispositivos médicos FDA: Class I (bajo riesgo, 47%), Class II (medio, 43%), Class III (alto, 10%)
- [P589] **HECHO** — FDASIA aprobada 2012; Sección 618 requirió FDA+ONC+FCC crear framework regulatorio risk-based para HIT incluyendo mobile medical apps
- [P590] **HECHO** — guidance "General Wellness" FDA (ene 2015): FDA no regulará wearable devices wellness general; test dos partes: (1) solo claims wellness general, (2) sin riesgos seguridad inherentes
- [P591] **HECHO** — Interstate Medical Licensure Compact (IMLC) y Enhanced Nurse Licensure Compact (eNLC) creados preservar regulación estatal facilitando telehealth cross-state
- [P592] **HECHO** — apps mHealth no son covered entities bajo HIPAA → sin prohibición federal recolección/uso/divulgación PHI recolectado por apps

### Ch 28: Privacy and Security

- [P593] **DEFINICIÓN** — privacidad = derecho individuos controlar acceso persona (body privacy) o información sobre sí mismos (information privacy)
- [P594] **DEFINICIÓN** — confidencialidad = datos/información no disponibles/divulgados personas/procesos no autorizados
- [P595] **DEFINICIÓN** — integridad = datos/información no alterados/destruidos manera no autorizada
- [P596] **DEFINICIÓN** — disponibilidad = datos/información accesibles y utilizables on demand por persona autorizada
- [P597] **DEFINICIÓN** — seguridad = proteger información/sistemas acceso/uso/divulgación/interrupción/modificación/destrucción no autorizados proveer confidencialidad, integridad, disponibilidad
- [P598] **REGLA** — privacidad concierne persona (derechos paciente); confidencialidad concierne información (responsabilidad proveedor); seguridad concierne salvaguardas administrativas/técnicas/físicas
- [P599] **HECHO** — Fair Information Practice Principles (FIPPs) redactados 1970s; 8 principios reconocidos internacionalmente: transparencia, participación individual, especificación propósito, minimización datos, limitación uso, calidad/integridad datos, seguridad, accountability/auditoría
- [P600] **HECHO** — EU Court Justice Google Spain SL v. AEPD sostuvo derecho ser olvidado en internet = derecho todos miembros EU
- [P601] **DEFINICIÓN** — consentimiento informado requiere: capacidad tomar decisiones, información suficiente comprensión paciente razonable, consentimiento voluntario sin fraude/coacción
- [P602] **DEFINICIÓN** — HIPAA = autoridad legal primaria US privacidad información salud; aplica solo covered entities: proveedores healthcare, clearinghouses, planes salud
- [P603] **DEFINICIÓN** — HIPAA tiene 3 reglas amplias: Privacy Rule, Security Rule, Breach Notification Rule
- [P604] **DEFINICIÓN** — PHI = información relacionada condición salud física/mental individuo, healthcare provisto/recomendado, o información pago, que identifica/puede razonablemente identificar persona específica
- [P605] **REGLA** — PHI solo puede usarse razones treatment-related permitidas Privacy Rule o con autorización escrita individuo
- [P606] **REGLA** — HIPAA Security Rule aplica PHI electrónica; requiere covered entities conducir análisis riesgo regulares, minimizar vulnerabilidades, tener protocolos detectar/prevenir software malicioso, usar access controls
- [P607] **DEFINICIÓN** — breach (45 CFR 164.402) = adquisición/acceso/uso/divulgación PHI manera no permitida comprometiendo seguridad/privacidad; cualquier uso impermisible presuntivamente breach requiriendo notificación
- [P608] **REGLA** — notificación breach requerida a: HHS, individuos afectados, y dependiendo circunstancias, público vía media
- [P609] **DEFINICIÓN** — designated record set = registros médicos/facturación + info seguro salud/gestión claims + otros registros usados toma decisiones; excluye notas psicoterapia + info procedimientos legales
- [P610] **PLAZO** — proveedores deben cumplir solicitudes derecho acceso ≤30 días calendario; una extensión permitida si notificación escrita provista con razón/fecha
- [P611] **DEFINICIÓN** — business associate = individuo/organización separado covered entity realizando servicios involucrando PHI; debe firmar business associate agreements delineando usos/divulgaciones permisibles PHI
- [P612] **HECHO** — OCR enforce HIPAA; quejas deben presentarse ≤180 días; organización tiene 30 días después notificación presentar evidencia defensa
- [P613] **HECHO** — categorías penalidad HIPAA: Cat 1 (no sabía) = $100-$50,000/violación, $25,000/año; Cat 2 (no negligencia willful) = $1,000-$50,000, $100,000/año; Cat 3 (negligencia willful, remediada ≤30 días) = $10,000-$50,000, $250,000/año; Cat 4 (negligencia willful, no remediada) = $50,000 min, $1,500,000/año
- [P614] **HECHO** — HITECH promulgada 2009; HHS Final Rule implementar no hasta 2013; destinada impulsar adopción EHR proveyendo privacidad/seguridad
- [P615] **HECHO** — HITECH implementó "meaningful use program" proveyendo incentivos monetarios implementación EHR; término reemplazado CMS "promoting interoperability"
- [P616] **REGLA** — HITECH extendió reglas privacidad/seguridad HIPAA a business associates; mejoró requerimientos risk assessment + breach notification; proveyó derecho obtener PHI forma electrónica
- [P617] **HECHO** — PSQIA 2005: legislación federal creando repositorio datos salud paciente de-identificados para investigación/revisión errores cuidado médico; participación voluntaria
- [P618] **REGLA** — datos recolectados bajo PSQIA establecidos como work product privilegiado para litigios estatal/federal; organizaciones seguridad paciente no pueden divulgar datos a menos de-identificados
- [P619] **HECHO** — GINA promulgada 2008; prohíbe discriminación cobertura seguro salud y empleo basada información genética individuo
- [P620] **ALCANCE** — GINA Title I: prohíbe aseguradores salud solicitar/requerir información genética o usarla decisiones seguros; Title II: prohíbe empleadores usar información genética decisiones empleo
- [P621] **EXCLUSIÓN** — GINA no aplica seguros vida, seguros discapacidad, o seguros cuidado largo plazo; no aplica condiciones salud diagnosticadas/síntomas, solo información genética misma
- [P622] **DEFINICIÓN** — biometric identifiers = datos biológicos usados identificar individuo: huellas dactilares, geometría facial, scans retina/iris, voiceprints
- [P623] **HECHO** — solo 3 estados aprobaron BIPAs: Illinois, Texas, Washington; Illinois BIPA incluye private right of action
- [P624] **DEFINICIÓN** — ransomware = malware diseñado extorsionar pagos rescate infectando computador, deshabilitando funciones, demandando pago restaurar funcionalidad
- [P625] **HECHO** — GDPR aprobada EU 2016; requiere: informar pacientes uso datos, usar solo propósito legítimo, retener solo hasta propósito completado, notificación breach ≤72 horas
- [P626] **HECHO** — GDPR Article 17 = derecho ser olvidado: organizaciones deben borrar información salud upon request si propósito cumplido/solo usado marketing/consentimiento revocado
- [P627] **HECHO** — Canadá PIPEDA: ley protección datos salud primaria; 10 principios equitativos: accountability, identificación propósitos, consentimiento, limitar recolección, limitar uso/divulgación/retención, precisión, salvaguardas, apertura, acceso individual, desafiar cumplimiento
- [P628] **HECHO** — Brasil LGPD aprobada agosto 14, 2018; modelada GDPR; define datos personales incluir datos salud/genéticos/biométricos
- [P629] **HECHO** — Japón APPI aprobada 2003; una primeras leyes privacidad asiáticas; estableció Personal Information Protection Commission (PPC)
- [P630] **HECHO** — China Cybersecurity Law aprobada nov 6, 2016, efectiva junio 2017; PRC aprobó PIPL agosto 20, 2021, efectiva nov 1, 2021

### Ch 29: MACRA and Interoperability

- [P631] **HECHO** — CMS estableció Medicare/Medicaid EHR Incentive Programs 2011 (ahora Promoting Interoperability Programs) incentivar adopción/meaningful use CEHRT
- [P632] **HECHO** — Stage 1: fundamento captura electrónica datos clínicos + proveer pacientes copias electrónicas info salud
- [P633] **HECHO** — Stage 2: procesos clínicos avanzados, intercambio datos estructurados, alineado National Quality Strategy
- [P634] **HECHO** — Stage 3 (oct 2015 final rule, efectiva 2017+): enfocado usar CEHRT mejorar resultados salud
- [P635] **DEFINICIÓN** — MACRA (2015) estableció Quality Payment Program; dos tracks: (1) MIPS y (2) Advanced Alternative Payment Models (APMs)
- [P636] **HECHO** — categoría MIPS Promoting Interoperability enfoca meaningful use tecnología EHR certificada
- [P637] **HECHO** — ONC 2015 Congressional Report concluyó information blocking = problema serio; recomendó Congreso prohibirlo con penalidades/enforcement
- [P638] **HECHO** — 21st Century Cures Act promulgada marzo 9, 2020; HHS/CMS promulgaron Information Blocking Rule (CMS Interoperability and Patient Access Rule)
- [P639] **DEFINICIÓN** — information blocking = interferencia con/prevención de/desaliento material acceso/intercambio/uso información salud electrónica; aplica proveedores healthcare, desarrolladores HIT, exchanges, networks
- [P640] **HECHO** — Information Blocking Rule adoptada mayo 1, 2020; requerimientos efectivos ene 1, 2021 o ene 2022; aplica MA organizations, Medicaid FFS, Medicaid managed care, CHIP managed care, QHP issuers
- [P641] **REQUISITO** — aseguradores salud deben hacer disponible Patient Access API incluyendo claims adjudicados, encounters proveedores capitated, datos clínicos/resultados lab no más 1 día hábil después claim adjudicado
- [P642] **REQUISITO** — Provider Directory API debe incluir nombres/direcciones/teléfonos/especialidades proveedores + datos directorio farmacia; disponible ≤30 días calendario recibir info directorio proveedor
- [P643] **REQUISITO** — intercambio datos payer-to-payer: planes salud aplicables deben intercambiar datos USCDI v1 solicitud enrollee; datos con fecha servicio desde ene 1, 2016; implementación completa ene 1, 2022
- [P644] **REQUISITO** — hospitales con registros médicos electrónicos deben enviar notificaciones registro/admisión/alta/transferencia paciente a proveedores post-acute care, practicantes cuidado primario, otros practicantes identificados
- [P645] **HECHO** — 8 excepciones Information Blocking Rule: preventing harm, privacy, security, infeasibility, health IT performance, content/manner, fees, licensing
- [P646] **HECHO** — Cures Act: desarrolladores HIT/redes/exchanges información salud sujetos penalidades monetarias civiles hasta $1M por violación information blocking; penalidades proveedores vía "appropriate disincentives" TBD
- [P647] **REQUISITO** — ONC Cures Act Final Rule requiere uso estándar HL7 FHIR (Release 4) + SMART Application Launch Framework (OAuth 2.0); establece USCDI como alcance EHI paciente vía API certificada
- [P648] **REQUISITO** — desarrolladores API certificados deben publicar términos/condiciones + documentación business/técnica públicamente vía hyperlink; deben soportar servicios API-enabled single-patient y multi-patient
- [P649] **REQUISITO** — planes salud aplicables deben participar trusted exchange networks capaces: intercambiar PHI entre jurisdicciones; conectar EHRs inpatient/ambulatorio; soportar mensajería segura/querying electrónico
- [P650] **REQUISITO** — registros médicos hospital deben retenerse forma original/legalmente reproducida ≥5 años
- [P651] **REQUISITO** — excepción infeasibility: actor debe proveer respuesta escrita solicitante ≤10 días hábiles explicando por qué solicitud infeasible
- [P652] **REQUISITO** — excepción licensing: actor debe comenzar negociaciones licencia ≤10 días hábiles de solicitud; negociar licencia ≤30 días hábiles

### Ch 30: Health Policy and Health Informatics

- [P653] **DEFINICIÓN** — health policy = define objetivos salud nivel internacional/nacional/local; especifica decisiones/planes/acciones alcanzar objetivos
- [P654] **HECHO** — policy no es ley; policy guía/delinea qué hacer alcanzar objetivo; leyes son estándares/principios/procedimientos que deben seguirse
- [P655] **HECHO** — IOM 2001 report delineó preocupaciones calidad disminuida, costos excesivos, errores evitables; llamó nuevas herramientas/métodos incluyendo adopción EHR universal
- [P656] **HECHO** — organizaciones stakeholder HIT incluyen HIMSS, AMIA, AHIMA, AMDIS, ANI, JPHIT, más vendors EHR/tecnología
- [P657] **HECHO** — posición National Coordinator for HIT creada 2004 vía Executive Order; codificada HITECH Act 2009
- [P658] **HECHO** — ONC 2020-2025 Federal Health IT Strategic Plan: 4 goals = (1) promover salud/bienestar, (2) mejorar prestación/experiencia cuidado, (3) construir ecosistema datos seguro investigación/innovación, (4) conectar healthcare con datos salud
- [P659] **HECHO** — HITECH = inversión $49B vía ARRA 2009 acelerar adopción HIT calidad/seguridad/eficiencia
- [P660] **HECHO** — tres etapas Meaningful Use: Stage 1 (2011) captura datos/compartición; Stage 2 (2014) procesos clínicos/HIE/ePrescription/acceso paciente; Stage 3 (2017) reemplazado "Advancing Care Information" bajo MACRA
- [P661] **HECHO** — 2015: 84% hospitales non-federal acute care adoptaron al menos EHR básico con notas clínicas
- [P662] **HECHO** — MACRA eliminó fórmula Sustainable Growth Rate; todos médicos elegibles MIPS pero sujetos penalidades; "Advancing Care Information" = 25% MIPS Final Score
- [P663] **HECHO** — IOM 1999 "To Err Is Human" estimó hasta 98,000 vidas perdidas anualmente por errores médicos hospitalarios
- [P664] **HECHO** — 2011 IOM "HIT and Patient Safety" report: recomendó HHS asegurar vendors soporten libre intercambio experiencias HIT; ONC trabaje sector privado experiencias usuario comparativas; HHS financie Health IT Safety Council
- [P665] **HECHO** — AHRQ publicó National Quality Strategy marzo 2011: primer framework nacional mejora calidad reconociendo HIT como crítico

### Ch 31: Health Information Technology Governance

- [P666] **DEFINICIÓN** — health IT governance = estructuras/procesos organizacionales asegurando alineación IT con objetivos estratégicos institucionales + priorización efectiva recursos IT limitados
- [P667] **HECHO** — dos necesidades fundamentales impulsando health IT governance: (1) asegurar alineación recursos IT con prioridades institucionales; (2) priorizar efectivamente recursos IT entre demandas competitivas
- [P668] **HECHO** — componentes core health IT governance: procesos propuesta proyecto formales, planificar direcciones futuras, evaluar/priorizar proyectos, aprobar financiamiento, monitorear ROI
- [P669] **HECHO** — estructura governance muestra: board directors + executive management → comité governance IT clínico (CMO, CNO, CMIO, CNIO, CIO, COO, CFO, chairs departamento) → varios comités operacionales
- [P670] **REGLA** — health IT governance debería ser independiente elecciones tecnología específicas; governance debería guiar selección tecnología
- [P671] **HECHO** — concepto "bimodal IT" Gartner: Mode 1 = operaciones predecibles; Mode 2 = innovación exploratoria; governance debe habilitar ambos
- [P672] **HECHO** — punto partida governance recomendado: evaluar estructura/cultura IT actual usando análisis SWOT; investigar enfoques organizaciones pares
- [P673] **HECHO** — 21st Century Cures Act (2016) habilita innovaciones third-party digital health integrarse directamente con EHR y su interfaz usuario
- [P674] **REQUISITO** — charter governance debería proveer principios guía, alcance responsabilidades, membresía comité, procesos, toma decisiones; impacto debería evaluarse activamente incluyendo consecuencias no intencionadas

## Section 7: Global and Future Perspectives in Health Informatics

### Ch 32: Global Health Informatics

- [P675] **HECHO** — 2021: ~4.6B usuarios internet activos = 59% población global (ITU 2021)
- [P676] **HECHO** — 93% población mundial tiene acceso red mobile-broadband (ITU 2021)
- [P677] **HECHO** — cobertura red 4G aumentó 2x globalmente entre 2015-2020
- [P678] **HECHO** — en LDCs, 17% población rural sin cobertura mobile; 19% rural cubierta solo por 2G (ITU 2021)
- [P679] **HECHO** — 72% hogares urbanos tenían acceso internet hogar (2019) vs ~38% rural globalmente
- [P680] **HECHO** — 10% incremento velocidad internet → 1.3% incremento crecimiento económico en LMICs
- [P681] **DEFINICIÓN** — eHealth = plataformas electrónicas provisión información/servicios salud, recolección/gestión datos; cuando usado teléfonos móviles = mHealth
- [P682] **DEFINICIÓN** — digital health expande eHealth incluir consumidores digitales, dispositivos smart/conectados; alcance incluye mHealth, HIT, wearables, telehealth/telemedicine, medicina personalizada
- [P683] **DEFINICIÓN** — GHI (Global health informatics) = disciplina informática enfocada empoderar personas usar tecnología apropiada soluciones basadas información perspectiva global soportando healthcare para todos (Richards et al. 2013)
- [P684] **HECHO** — resolución WHO WHA58.28 (2005) urgió Member States desarrollar plan estratégico largo plazo servicios eHealth/infraestructura ICT
- [P685] **HECHO** — resolución WHO WHA66.24 (2013) urgió Member States desarrollar políticas/mecanismos legislativos enlazados estrategia eHealth nacional + estandarización/interoperabilidad
- [P686] **HECHO** — iniciativa Digital REACH lanzada 2017 East African Community: Burundi, Kenya, Rwanda, South Sudan, Tanzania, Uganda
- [P687] **HECHO** — resolución WHO WHA71.7 (mayo 2018) sobre digital health → desarrollar estrategia global digital health
- [P688] **HECHO** — UN Secretary General's High-Level Panel Digital Cooperation (2019) recomendó 2030 cada adulto debería tener acceso asequible redes digitales + servicios financieros/salud digitalmente habilitados
- [P689] **HECHO** — Lancet / Financial Times joint Commission (oct 2019) enfocó convergencia digital health, AI, y cobertura universal salud
- [P690] **HECHO** — Global Strategy Digital Health 2020-2025 endosada por WHA73 (2020)
- [P691] **ALCANCE** — WHO Global Strategy Digital Health 2020-2025 tiene 4 objetivos estratégicos: (1) promover colaboración global/transferencia conocimiento, (2) avanzar estrategias digital health nacionales, (3) fortalecer governance global/regional/nacional, (4) abogar sistemas salud people-centered habilitados digital health
- [P692] **HECHO** — término "artificial intelligence" acuñado 1956; rama computer science dealing simulación comportamiento inteligente computadores
- [P693] **ALCANCE** — intervenciones salud AI-driven en LMICs encajan 4 categorías: (a) diagnóstico, (b) evaluación riesgo mortalidad/morbilidad, (c) predicción/vigilancia brotes enfermedad, (d) política/planificación salud
- [P694] **⚠ TENSIÓN** — AI en LMICs enfrenta desafíos: diseño apropiado impulsado necesidades locales, sesgos étnicos/socioeconómicos/género durante desarrollo, necesidad nuevos protocolos compartición datos e interoperabilidad
- [P695] **DEFINICIÓN** — ML = proceso a través del cual computadores/modelos/algoritmos aprenden y mejoran de datos y procesos; usado clasificación, clustering, predicción
- [P696] **DEFINICIÓN** — cloud computing = usar red servidores remotos almacenar/gestionar/acceder/procesar datos; 3 modelos servicio: SaaS, PaaS, IaaS (NIST)
- [P697] **DEFINICIÓN** — IoT = sistema dispositivos digitales wireless, interrelacionados, conectados que recolectan/envían/almacenan datos sobre red sin requerir interacción humano-a-humano o humano-a-computador
- [P698] **HECHO** — arquitectura IoT healthcare tiene 3 capas: (1) capa procesada/sensor, (2) capa red (wired/wireless), (3) capa aplicación
- [P699] **RESTRICCIÓN** — riesgo cyber es obstáculo principal adopción IoT amplia; privacidad paciente debe asegurarse prevenir identificación/rastreo no autorizado
- [P700] **DEFINICIÓN** — telehealth/telemedicine = uso dispositivos telecomunicación entrega remota cuidado médico; intercambiando información médica un sitio a otro vía comunicación electrónica
- [P701] **REQUISITO** — 7 componentes clave sistemas salud LMIC adoptar telemedicine: aprobaciones gobierno, identificación usuarios, elección plataforma tech, alineación incentivos financieros, definición workflows, training trabajadores salud, engagement paciente
- [P702] **HECHO** — India Ministry Health publicó guías práctica telemedicina nacional marzo 2020
- [P703] **HECHO** — China publicó guías aumentando reembolso consultas follow-up online + entrega recetas puerta-a-puerta vía "internet hospitals" durante COVID-19
- [P704] **DEFINICIÓN** — PHR = aplicación electrónica a través individuos acceden/gestionan/comparten info salud entorno privado/seguro/confidencial; 3 tipos: standalone, tethered, interconnected
- [P705] **HECHO** — OpenMRS = EHR open-source liderado Regenstrief Institute + Partners in Health; implementado inicialmente Kenya
- [P706] **HECHO** — Bahmni = software clínico integrado combinando OpenMRS (registros paciente) + OpenELIS (gestión lab) + OpenERP/Odoo (contabilidad hospital); desplegado India, Bangladesh, Nepal
- [P707] **HECHO** — DHIS2 = plataforma open-source web-based recolección/validación/análisis datos salud; primera introducción University of Oslo 1994
- [P708] **HECHO** — implementación DHIS2 mejoró reporting cobertura inmunización, visitas ANC, tasa parto facility en Uganda y Kenya
- [P709] **DEFINICIÓN** — mHealth = práctica médica/salud pública soportada dispositivos móviles (WHO 2011)
- [P710] **HECHO** — SMS = herramienta tecnología mHealth más común usada a través settings healthcare
- [P711] **HECHO** — India lanzó Integrated Disease Surveillance Project (IDSP) formalmente 2004; IDSR implementado mayoría países africanos
- [P712] **REQUISITO** — 5 áreas enfoque críticas escalar digital health en LMICs: (1) características programa intrínsecas con beneficios tangibles, (2) engagement/training stakeholders, (3) simplicidad técnica/interoperabilidad/adaptabilidad, (4) infraestructura apropiada, (5) alineación política healthcare + financiamiento sostenible
- [P713] **HECHO** — Health Data Collaborative (HDC) y Principles for Digital Development son partnerships globales enfocados estándares interoperabilidad
- [P714] **HECHO** — Digital Impact Alliance (DIAL) y Digital Square buscan mejorar datos salud inversiones compartidas global goods escala digital health

### Ch 33: Informatics and the Future of Healthcare

- [P715] **HECHO** — gasto healthcare US proyectado crecimiento anual 5.4% para 2019-2028; puede alcanzar $6.2 trillones 2028
- [P716] **HECHO** — proyecciones gasto US actuales $2.5 trillones menos originalmente proyectado por ACA + recesión late 2000s
- [P717] **HECHO** — población global ≥60 años crecerá 600M (2000) → >2B (2050) (WHO 2011)
- [P718] **HECHO** — enfermedad cardíaca isquémica = 16% muertes globales anualmente; diabetes global predicha aumentar 382M (2013) → 592M 2035
- [P719] **HECHO** — 2030: seniors US esperados aumentar 55% vs 2015; estimado 1M enfermeros retirados 2017-2030; déficit nacional 40,800-104,900 médicos esperado 2030
- [P720] **DEFINICIÓN** — futures research (futurología) = estudio racional/sistemático futuro con objetivo identificar futuros posibles, probables, preferibles; enfoque 5-50 años adelante
- [P721] **HECHO** — Toffler publicó "Future Shock" 1970 sobre adaptación/falla adaptación cambio; Naisbitt publicó "Megatrends" 1982 identificando 10 tendencias societales
- [P722] **DEFINICIÓN** — trend analysis = examinar datos históricos identificar tendencias tiempo; extrapolation = extender datos históricos futuro; patrón S-curve: crecimiento inicial lento → crecimiento rápido → desaceleración límite natural
- [P723] **HECHO** — CMS + ONC crearon nuevas guidelines/políticas interoperabilidad, acceso paciente datos médicos, HIE mejorado usando estándares FHIR y USCDI
- [P724] **DEFINICIÓN** — person-centered health = término genérico abarcando person-centered care, patient-centered care, precision medicine, consumer-centered care; 6 principios: cuidado persona completa, respeto/valor, elección, dignidad, auto-determinación, vida propositiva
- [P725] **DEFINICIÓN** — precision (personalized) medicine = intervenciones salud tailored diferencias individuales específicas: genoma, ambientes, estilo vida
- [P726] **HECHO** — mercado global apps mHealth valuado $40B (2020); tasa crecimiento esperada >17% desde 2021-2028
- [P727] **HECHO** — CMMI soportó Emergency Triage, Treat, and Transport (ET3) model permitiendo EMS proveer cuidado on-scene con control médico virtual real-time, potencialmente sin transporte hospital
- [P728] **DEFINICIÓN** — SDOH = factores no-médicos influenciando resultados salud incluyendo educación, inseguridad alimentaria, acceso servicios salud (WHO 2017)
- [P729] **REQUISITO** — ONC recomienda mejorar infraestructura soportar uso datos SDOH aplicaciones clínicas; sistemas salud necesitarán redes CBO comunicarse con EHRs integración significativa
- [P730] **HECHO** — University Vermont Medical Center empleados bloqueados EHR casi 1 mes por ataque ransomware; impacto estimado ~$50M revenue perdido
- [P731] **HECHO** — >1/3 organizaciones healthcare globalmente reportaron ser target ransomware 2020 (Sophos 2021)
- [P732] **DEFINICIÓN** — optimization (EHR) = esfuerzos iniciales y post-implementación incluyendo evaluaciones, training continuo, re-tailoring sistema; instalaciones no terminan con go-live sino transformación continua
- [P733] **⚠ TENSIÓN** — usabilidad EHR vinculada burnout proveedor médicos y enfermeros; Mandl & Kohane argumentan vendors propagaron mito complejidad precluding innovación (NEJM 2012)
- [P734] **HECHO** — 21st Century Cures Act aborda information blocking (con penalidades) e interoperabilidad semántica; integra FHIR, LOINC, ICD, SNOMED política nacional
- [P735] **HECHO** — USCDI = estándar datos todos vendors EHR requeridos exponer vía API; catalizador nuevos modelos cuidado desacoplados enfoques tradicionales sistema-healthcare-centrados
- [P736] **HECHO** — solo ~2% pacientes actualmente usando apps mHealth integradas suites aplicación facility (Accenture 2015)
- [P737] **DEFINICIÓN** — human factors engineering (HFE) = disciplina científica enfocada interacción humanos/elementos sistema, enfatizando bienestar humano y rendimiento sistema; raíces mid-1900s aviación/diseño militar
- [P738] **HECHO** — SEIPS 2.0 model = modelo sociotécnico proveyendo enfoque holístico factores healthcare: personas, organizaciones, herramientas/tecnología, ambiente interno, ambiente externo, tareas (Holden et al. 2013)
- [P739] **HECHO** — IBM estima 2.5 quintillones bytes información generados por día globalmente
- [P740] **DEFINICIÓN** — predictive analytics = uso datos pasados predecir tendencias futuras; objetivo presentar datos decision makers tan cerca real time como posible
- [P741] **DEFINICIÓN** — Learning Healthcare System introducido 2007 US IOM (ahora National Academy Medicine) = sistema donde ciencia/informática/incentivos/cultura alineados mejora continua, best practices embebidas prestación, pacientes participantes activos, nuevo conocimiento capturado como by-product
- [P742] **HECHO** — primera ola aplicaciones ML healthcare apuntó ineficiencias operacionales: NLP extracción billing codes, predicción length of stay, predicción tasas no-show
- [P743] **⚠ TENSIÓN** — modelos ML pueden resultar mayor inequidad asignación recursos healthcare; técnicas necesarias reducir sesgo y proteger poblaciones vulnerables mayor marginalización
- [P744] **DEFINICIÓN** — ML interpretability = cualquier método ML que puede explicar predicciones manera humano puede entender; modelos interpretables construyen confianza clínica + habilitan clinical override predicciones
- [P745] **ALCANCE** — 3 niveles cambio (Nelson & Englebardt 2002): 1st-level = hace proceso existente más eficiente (menos disruptivo); 2nd-level = cambia cómo resultado logrado; 3rd-level = altera proceso y reenfoca objetivo (nivel societal/institucional)
- [P746] **HECHO** — tendencias clinical informatics futuras agrupadas: (1) person-centered health, (2) tendencias técnicas (IoT, cybersecurity), (3) clinical informatics (beyond EHRs, UX, predictive analytics, visualización datos)
- [P747] **HECHO** — nuevos roles liderazgo HIT emergiendo: Chief Clinical Informatics Officer, Chief Innovation Officer, Chief Digital Officer, Chief Content Officer, Chief Data Scientist
