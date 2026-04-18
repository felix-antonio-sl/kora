# HCAI: Foundations and Approaches
<!-- /atomize · 180 proposiciones · 48 entidades · 1 archivo · 2026-04-06 -->
<!-- Consultar: buscar por [P###], por tipo (REQUISITO, DEFINICION...), o por entidad -->

## Human-Centered Artificial Intelligence: Foundations and Approaches (Wei Xu)

### Abstract & Keywords

- [P001] **HECHO** — autor: Wei Xu, HCAI Labs, California, USA; ORCID 0000-0001-8913-2672
- [P002] **DEFINICION** — HCAI: filosofia de diseno y complemento metodologico a paradigmas AI technology-centered
- [P003] **REGLA** — HCAI busca que sistemas AI sirvan, aumenten y empoderen humanos, no danen ni reemplacen
- [P004] **HECHO** — keywords: human-centered AI, human-centered design, human-AI interaction, HCAI methodology, HCAI practice

### 1. Introduction

- [P005] **HECHO** — incidentes AI subieron a 233 en 2024, +56.4% interanual → `Stanford HAI` 2025
- [P006] **HECHO** — AI Incident Database registro docenas mas en mid-2025 → `AIID`
- [P007] **HECHO** — telemetria seguridad: automatizacion AI genera 36,000 scans/segundo y credential abuse creciente → `Fortinet` 2025
- [P008] **HECHO** — `EU AI Act` y `NIST AI RMF` reflejan esfuerzo acelerado alinear AI con valores humanos, accountability, seguridad
- [P009] **DEFINICION** — HCAI emergio como paradigma investigacion: AI debe desarrollarse *para* y *con* humanos → `Shneiderman` 2020; `Xu` 2019
- [P010] **HECHO** — paralelo historico: boom PC 1980s → diseno centrado-maquina; `Norman` (1986) propuso HCD como respuesta
- [P011] **HECHO** — practicas HCD impulsaron emergencia campos UX y HCI → `Shneiderman` 1987; `Xu` 2003a
- [P012] **REGLA** — descuidar principios human-centered en avance AI puede generar consecuencias mucho mas severas que en eras previas computing

### 2.1 Transitioning to Human-AI Interaction

- [P013] **DEFINICION** — HCI: campo cross-disciplinary era PC, estudia interaccion humanos con sistemas computing no-AI
- [P014] **HECHO** — transicion HCI → human-AI interaction marca cambio paradigmatico en engagement humano con tecnologia
- [P015] **REGLA** — sistemas no-AI: algoritmos fijos, logica determinista, sin capacidad adaptacion
- [P016] **REGLA** — sistemas AI: aprendizaje, adaptacion, auto-ejecucion; comportamientos pueden evolucionar, ser inciertos o sesgados
- [P017] **REGLA** — sistemas no-AI: herramientas asistiendo tareas humanas; AI: posibles colaboradores con autonomia variable
- [P018] **REGLA** — output no-AI: deterministico/predecible; output AI: probabilistico, incierto, context-dependent
- [P019] **REGLA** — interaccion no-AI: unidireccional (humano→maquina); AI: bidireccional colaborativa
- [P020] **REGLA** — no-AI: sin complementariedad, asignacion funcional estatica; AI: complementariedad dinamica inteligencia humana-maquina
- [P021] **HECHO** — sistemas AI poseen sensing tipo-humano via tecnologias multimodal; no-AI carecen
- [P022] **HECHO** — sistemas AI poseen grados variables capacidades cognitivas tipo-humano (reconocimiento patrones, aprendizaje, razonamiento)
- [P023] **REGLA** — no-AI requiere activacion manual; AI ejecuta independientemente en contextos especificos
- [P024] **REGLA** — AI puede adaptarse ambientes impredecibles segun diseno; no-AI no puede
- [P025] **REGLA** — en no-AI solo humanos inician acciones; en AI ambos humanos y maquinas inician proactivamente
- [P026] **REGLA** — no-AI: confianza/control unidireccional humano; AI: confianza compartida, situation awareness mutua, ejecucion colaborativa preservando autoridad decisional humana
- [P027] **REGLA** — no-AI: intervencion humana siempre requerida; AI: oversight humano crucial pero sistemas pueden actuar proactivamente

### 2.2 Emerging Human-Machine Relationship

- [P028] **HECHO** — evolucion relacion humano-maquina: pre-WWII machine-centered → post-WWII human-centered → HCI → human-AI interaction
- [P029] **HECHO** — en era AI, agentes AI evolucionan mas alla herramientas auxiliares hacia interaccion colaborativa bidireccional
- [P030] **DEFINICION** — human-AI collaboration: AI funciona simultaneamente como herramienta + colaborador ("tool + collaborator") → `Brill/Cummings` 2018; `Xu & Ge` 2020
- [P031] **DEFINICION** — HAJCS (Human-AI Joint Cognitive Systems): framework que trata AI como agente cognitivo realizando tareas cognitivas AI-enabled → `Xu & Gao` 2024
- [P032] **REGLA** — HAJCS usa teoria situation awareness de `Endsley` para procesamiento informacion agentes cognitivos humano/maquina
- [P033] **REQUISITO** — HAJCS enfatiza liderazgo humano y autoridad ultima en human-AI collaboration
- [P034] **TENSION** — debate persiste: AI como teammate vs herramienta → `NAS` 2021; `Naikar et al.` 2025; paradigma teaming puede arriesgar perdida oversight humano → `Shneiderman` 2021, 2022
- [P035] **DEFINICION** — human-AI collaboration = partnership complementaria colaborativa enfatizando liderazgo humano, no reemplazo/competencia
- [P036] **REGLA** — human-AI hybrid intelligence: AI complementa capacidades humanas logrando ganancias sinergicas inalcanzables por separado

### 2.3 Double-Edged Sword Effect of AI

- [P037] **REGLA** — AI double-edged sword: desarrollo responsable → mejora bienestar; mal uso/diseno inadecuado → riesgos eticos/sociales/seguridad significativos
- [P038] **HECHO** — AI Incident Database documenta >1,000 accidentes AI: vehiculos autonomos fatales, flash crashes mercados, arrestos erroneos reconocimiento facial → `AIID`
- [P039] **HECHO** — base datos AIAAIC: incidentes/controversias AI reportados ~26x mayor que 2012 → `Stanford HAI` 2025
- [P040] **REGLA** — limitacion AI: Vulnerability — desempeno pobre ante categorias comportamiento nuevas o distribuciones datos diferentes al entrenamiento
- [P041] **REGLA** — limitacion AI: Perception Limitations — input incorrecto disrumpe aprendizaje cognitivo superior
- [P042] **REGLA** — limitacion AI: Potential Bias — datasets limitados/sesgados generan output sesgado
- [P043] **REGLA** — limitacion AI: Uninterpretability — "black box effect" algoritmos ML dificulta interpretar outputs
- [P044] **REGLA** — limitacion AI: Lack of Causal Models — ML basado en pattern recognition, no comprende relaciones causales
- [P045] **REGLA** — limitacion AI: Development Bottleneck — dificil simular capacidades cognitivas superiores humanas aisladamente
- [P046] **REGLA** — limitacion AI: Autonomy Effect — puede causar automation confusion, reduccion situation awareness, "out-of-the-loop", decision bias, degradacion habilidades manuales
- [P047] **REGLA** — limitacion AI: Ethical Issues — privacidad datos, justicia usuarios, fairness
- [P048] **REGLA** — limitacion AI: Independent Operability — AI sola no maneja situaciones complejas/desconocidas; humanos deben retener poder decision final
- [P049] **TENSION** — a diferencia tech nuclear/bioquimica (centralizada, pocos paises), desarrollo AI es descentralizado, global, baja barrera entrada → regulacion efectiva especialmente desafiante

### 2.4 Third Wave of AI

- [P050] **DEFINICION** — 3 olas AI: 1a (1950s-1980s) simbolismo/conexionismo; 2a (1990s-2010s) modelos estadisticos/redes neuronales; 3a (2010s-presente) deep learning/big data → `Xu` 2019
- [P051] **DEFINICION** — 3a ola caracterizada por: mejora tecnologica + soluciones orientadas aplicacion + enfoque human-centered
- [P052] **REGLA** — 1a/2a olas: academia-driven, foco tecnico, necesidades humanas no satisfechas; 3a: comienza soluciones AI practicas con diseno eticamente alineado
- [P053] **REGLA** — 3a ola redefine AI de busqueda puramente tecnica a ingenieria de sistemas cross-disciplinary mas alla limites CS
- [P054] **HECHO** — 3a ola: AI direcciona necesidades genuinas usuarios con modelos negocio sostenibles — departure fundamental de olas previas
- [P055] **DEFINICION** — Human-Machine Hybrid Enhanced Intelligence: humanos como nodos cognitivos/decisionales en loop inteligente para hybrid intelligence mas robusta
- [P056] **DEFINICION** — "Data + Knowledge" Dual-Driven AI: combina big data/deep learning con knowledge bases para superar limitaciones ambos enfoques
- [P057] **REQUISITO** — AI Interpretability: resultados transparentes/interpretables para decisiones informadas y confianza → `Gunning et al.` 2019
- [P058] **HECHO** — Ethical AI: gobiernos/empresas establecen frameworks eticos para valores humanos, fairness, proteccion datos, privacidad
- [P059] **DEFINICION** — Human-Controllable AI: conceptos meaningful human control para accountability y prevencion consecuencias autonomas no intencionadas → `de Sio & den Hoven` 2018
- [P060] **REGLA** — 3a ola = cambio paradigmatico: technology-centered → human-centered mindset
- [P061] **REGLA** — humanos mantienen rol irremplazable en desarrollo y uso sistemas AI en 3a ola

### 3.1.1 Shneiderman's Frameworks

- [P062] **DEFINICION** — `Shneiderman` (2020a): framework HCAI bidimensional con ejes grado-control-humano y grado-autonomia-AI
- [P063] **REGLA** — insight clave: mayor autonomia no implica necesariamente menor control humano; disenadores deben buscar alta automatizacion Y alto control humano simultaneamente
- [P064] **REGLA** — over-automation (alta automatizacion, bajo control) y over-control (alto control, baja automatizacion) introducen riesgos distintos
- [P065] **DEFINICION** — `Shneiderman` (2022): 4 metaforas diseno HCAI — Supertools, Tele-bots, Active Appliances, Control Centers
- [P066] **DEFINICION** — Supertools: UIs potentes amplificando intencion humana via displays info-rich, manipulacion directa, acciones reversibles
- [P067] **DEFINICION** — Tele-bots: mantienen autoridad humana sobre efectores remotos via teleoperacion con feedback continuo alta-fidelidad
- [P068] **DEFINICION** — Active Appliances: encapsulan autonomia dentro limites tarea bien definidos (ej. lavadoras, elevadores)
- [P069] **DEFINICION** — Control Centers: orquestan sistemas automatizados via oversight humano, auditabilidad, mecanismos intervencion responsiva
- [P070] **REGLA** — principio unificador metaforas: claridad responsabilidad via interaccion human-AI efectiva y UIs
- [P071] **DEFINICION** — `Shneiderman` (2020c): 2 grand goals AI — emulation (replicar cognicion humana) y application (productos practicos mejorando capacidades humanas)
- [P072] **HECHO** — 4 design mismatches: intelligent agent vs powerful tool, simulated teammate vs teleoperated device, autonomous system vs supervisory control, humanoid robot vs mechanoid appliance
- [P073] **REGLA** — compromise strategies integran AI con metodos HCI; AI confiable requiere reliability, safety, control usuario via UIs comprensibles/predecibles/controlables
- [P074] **DEFINICION** — `Shneiderman` (2020b): estructura governance RST (reliable, safe, trustworthy) AI en 4 niveles: team, organizacion, industria, gobierno
- [P075] **REGLA** — 3 pilares governance: reliability (validacion ingenieria/bias testing/audit trails), safety culture (liderazgo/near-miss reporting/review boards), trustworthy certification (auditores independientes/standards/reguladores)
- [P076] **HECHO** — 15 recomendaciones accionables spanning niveles team, organizacional, industria/regulatorio
- [P077] **REGLA** — HCAI no realizable solo via algoritmos; requiere procesos robustos, evidencia verificable, accountability duradera

### 3.1.2 Wei Xu's Frameworks

- [P078] **DEFINICION** — `Xu` (2019): THE Triangle (Technology-Human Factors-Ethics) integra innovacion tecnologica, principios human factors, alineamiento etico
- [P079] **REGLA** — perspectivas THE: Technology (que puede construirse), Human Factors (como interactuan humanos/AI), Ethics (que debe hacerse / por que)
- [P080] **REGLA** — solucion HCAI optima reside en zona interseccion central 3 perspectivas (optimal integration zone)
- [P081] **REGLA** — AI solo tech → dana humanidad; sin human factors → adopcion falla; sin tech → sin innovacion/escalabilidad
- [P082] **DEFINICION** — `Xu & Gao` (2025): iSTS (Intelligent Sociotechnical Systems) framework extiende teoria STS a era AI; prioriza human-AI joint optimization sobre classical joint optimization
- [P083] **DEFINICION** — `Xu & Gao` (2025): hHCAI (Hierarchical HCAI) — paradigma multi-nivel: individual → organizacional → ecosistema → macrosocial
- [P084] **REGLA** — niveles hHCAI: human-in/on-the-loop, organization-in-the-loop, ecosystem-in-the-loop, society-in-the-loop
- [P085] **REQUISITO** — adopcion AI sostenible/responsable requiere coherencia simultanea todos niveles hHCAI
- [P086] **DEFINICION** — `Xu, Gao & Dainoff` (2025): HCAI-MF con 5 componentes: requirement hierarchy, method taxonomy, process, interdisciplinary collaboration, multi-level design paradigms
- [P087] **REGLA** — HCAI-MF busca transformar HCAI de filosofia diseno a metodologia practica sistematica accionable
- [P088] **DEFINICION** — `Winby & Xu` (2025): HCAI-MM (Maturity Model) — 5 niveles: Ad Hoc → Repeatable → Defined → Managed → Optimizing
- [P089] **DEFINICION** — HCAI-MM Level 1 (Ad Hoc): practicas HCAI no sistematicas, dependientes esfuerzos individuales
- [P090] **DEFINICION** — HCAI-MM Level 2 (Repeatable): guidelines HCAI basicas parcialmente aplicadas respondiendo presiones externas
- [P091] **DEFINICION** — HCAI-MM Level 3 (Defined): practicas estandarizadas, procesos formalizados, colaboracion cross-disciplinary
- [P092] **DEFINICION** — HCAI-MM Level 4 (Managed): monitoreo continuo, indicadores HCAI medibles (fairness audits, usability metrics, incident reporting)
- [P093] **DEFINICION** — HCAI-MM Level 5 (Optimizing): HCAI institucionalizado como cultura/estrategia organizacional, aprendizaje continuo, governance predictivo
- [P094] **REGLA** — frameworks Xu evolucionan: fundamentos conceptuales → guia metodologica → practica organizacional → integracion ecosistema/sociotecnica escalable
- [P095] **HECHO** — avances recientes Xu: HC-HAC (Gao, Xu et al. 2025), HC-HAII (Xu 2025), HCP approach AI (Sun, Xu & Gao 2025), HC-ASI (Pan, Xu & Gao 2025)

### 3.1.3 Six HCAI Grand Challenges

- [P096] **HECHO** — 26 expertos internacionales liderados `Shneiderman` y `Salvendy` alcanzaron consenso 6 HCAI Grand Challenges → `Ozmen Garibay et al.` 2023
- [P097] **DEFINICION** — 6 challenges: (1) Human well-being, (2) Responsible AI, (3) Privacy, (4) Human-centered design/evaluation, (5) Governance/oversight, (6) Human-AI interaction
- [P098] **REGLA** — abordar challenges requiere integrar sociotechnical design, ethics-by-design, metodologias participativas across AI lifecycle

### 3.1.3b Other Emerging HCAI Concepts

- [P099] **HECHO** — otras perspectivas HCAI: Humanistic AI Design (`Auernhammer` 2020), Human-Centered Explainable AI (`Ehsan et al.` 2020), Human-Centered ML (`Kaluarachchi et al.` 2021)
- [P100] **HECHO** — HCAI explorado en sectores: medicina, workplace, LLMs, social computing → `Regis et al.` 2025; `Germanakos et al.` 2025
- [P101] **HECHO** — `Capel & Brereton` (2023): analizaron 250+ estudios; 4 temas HCAI: explainable AI, human-centered design/evaluation, human-AI teaming, ethical AI
- [P102] **DEFINICION** — `Schmager et al.` (2025): HCAI busca augmentar capacidades humanas manteniendo control humano considerando necesidad, contexto, condiciones eticas/legales
- [P103] **DEFINICION** — `Desolda et al.` (2025): sistemas HCAI disenados/desarrollados/evaluados involucrando usuarios para incrementar performance/satisfaccion, siendo utiles, usables, confiables, seguros, trustworthy

### 3.1.4 Summary

- [P104] **DEFINICION** — entendimiento comun HCAI: principio guia diseno y contrapeso metodologico al desarrollo AI technology-centered
- [P105] **REGLA** — HCAI coloca humanos al centro enfatizando necesidades, valores, etica, controlabilidad, capacidades, experiencias throughout AI lifecycle
- [P106] **HECHO** — HCAI evoluciono: foco integracion etica/tecnica → perspectivas multi-nivel organizacional/ecosistema/sociotecnica → metodologias/governance practicos

### 3.2 HCAI Guiding Principles

- [P107] **DEFINICION** — 9 principios guia HCAI: human augmentation, human controllability, ethical alignment, user experience, human-led collaboration, transparency/explainability, accountability/responsibility, safety/reliability, sustainability
- [P108] **TENSION** — trade-offs entre principios: privacy vs personalization, explainability vs performance — requieren balanceo context-sensitive
- [P109] **TENSION** — diferencias culturales/contextuales complican guidelines globalmente aplicables pero localmente relevantes
- [P110] **TENSION** — muchos principios HCAI (ethical, fair, trustworthy, responsible AI) se superponen conceptualmente

### 3.2.1 Human Augmentation

- [P111] **REGLA** — human augmentation: AI debe mejorar/empoderar capacidades humanas, no reemplazar/disminuir
- [P112] **REGLA** — valor verdadero AI: complementar fortalezas humanas (juicio, creatividad, empatia, etica) compensando limitaciones (memoria, atencion, procesamiento datos, escalabilidad)

### 3.2.2 Human Controllability

- [P113] **REQUISITO** — human controllability: sistemas AI deben permanecer bajo autoridad/control humano en contextos safety, etica, high-stakes
- [P114] **REQUISITO** — requiere capacidad dirigir, supervisar, intervenir, override acciones AI — across entero AI lifecycle incluyendo governance organizacional/societal

### 3.2.3 Ethical Alignment

- [P115] **REGLA** — ethical alignment: AI consistente con valores humanos, derechos, expectativas sociales — fairness, inclusivity, dignidad humana
- [P116] **REGLA** — ethical alignment = proceso continuo dialogo, monitoreo, recalibracion — no esfuerzo unico

### 3.2.4 User Experience

- [P117] **REQUISITO** — UX: sistemas AI deben ser usables, accesibles, comprensibles, satisfactorios — extiende mas alla usabilidad a dinamicas emocionales, cognitivas, sociales
- [P118] **REGLA** — UX requiere embeber metodos HCD (user research, participatory design, iterative prototyping, usability testing, feedback loops) throughout AI lifecycle

### 3.2.5 Human-Led Collaboration

- [P119] **REGLA** — human-led collaboration: humanos lideran tareas compartidas, AI como colaborador adaptativo aportando fortalezas complementarias
- [P120] **REGLA** — a diferencia modelos automation-driven, humanos retienen liderazgo, goal-setting, decisiones finales, capacidad intervencion

### 3.2.6 Transparency and Explainability

- [P121] **DEFINICION** — transparency: apertura sobre como sistemas AI disenados, entrenados, validados, deployed
- [P122] **DEFINICION** — explainability: outputs/rationales user-facing que humanos pueden entender, interpretar, actuar — tailored por tipo stakeholder
- [P123] **REGLA** — previene problema AI "black box", fomenta oversight informado, confianza, decision-making responsable

### 3.2.7 Accountability and Responsibility

- [P124] **REQUISITO** — accountability/responsibility: humanos (developers, deployers, operators) permanecen accountable por AI outcomes — no la AI misma
- [P125] **REQUISITO** — requiere documented design choices, audit trails, traceable interaction logs, decision attribution across AI lifecycle
- [P126] **REQUISITO** — nivel societal/regulatorio: politicas enforceable, liability frameworks, ethical standards asegurando atribucion dano a actores humanos responsables

### 3.2.8 Safety and Reliability

- [P127] **REGLA** — safety: minimizar riesgos dano en dominios fisico, psicologico, social
- [P128] **REGLA** — reliability: performance consistente/predecible; sistemas error-tolerant con alertas usuario, emergency shutdowns, procesos recovery transparentes

### 3.2.9 Sustainability

- [P129] **REGLA** — sustainability: consideracion sostenibilidad tecnica, ambiental, economica, social en diseno AI
- [P130] **REGLA** — ambiental: reducir huella ecologica (demandas energia/recursos), algoritmos eficientes, infraestructura green
- [P131] **REGLA** — social: AI no debe exacerbar digital divides, desplazar grupos vulnerables, erosionar cohesion social

### 4. HCAI Methodological Framework (HCAI-MF)

- [P132] **HECHO** — implementacion practica HCAI permanece largely underdeveloped; carece metodologias comprensivas bridging filosofia y ejecucion
- [P133] **DEFINICION** — HCAI-MF extendido incluye 6 componentes: requirement hierarchy, method taxonomy, process, interdisciplinary collaboration, multi-level design paradigm, maturity model

### 4.1 HCAI Requirement Hierarchy

- [P134] **DEFINICION** — HCAI-RH (`Xu, Gao & Dainoff` 2025): 4 niveles — HCAI Design Goals → Guiding Principles → Design Guidelines → Product-Level Requirements
- [P135] **REGLA** — 3 features definitorias HCAI-RH: means-end alignment (consistencia vertical), one-to-many mapping (cobertura comprensiva), goal-directed flow (top-down linkage)
- [P136] **REGLA** — HCAI-RH bridges gap aspiraciones estrategicas ↔ implementacion operacional; traduce goals en product requirements concretos/testables

### 4.2 HCAI Method Taxonomy

- [P137] **DEFINICION** — HCAI-MT (`Xu, Gao & Dainoff` 2025): 5 categorias — human-centered strategy, human-centered computing, interaction technology/design, human-centered controllability, AI risk management/governance
- [P138] **HECHO** — 16 metodos HCAI representativos mapeados across AI lifecycle (Table 5)
- [P139] **REGLA** — 3 beneficios HCAI-MT: goal-oriented design, estructura comprensiva/escalable, guidance accionable para practica

### 4.3-4.4.1 Design Paradigms — Human-in/on-the-loop

- [P140] **DEFINICION** — hHCAI framework define paradigma diseno multi-nivel: individual → organizacional → ecosistema → macrosocial
- [P141] **DEFINICION** — HITL (Human-in-the-loop): participacion humana activa continua en decisiones criticas, intervencion real-time, juicio etico
- [P142] **DEFINICION** — HOTL (Human-on-the-loop): control supervisorio donde humanos monitorean sistemas autonomos e intervienen segun necesidad, promoviendo escalabilidad
- [P143] **REGLA** — paradigma diseno human-in/on-the-loop HCAI abarca entero AI lifecycle, no solo interacciones operacionales
- [P144] **REGLA** — humanos embedded como: requirement definers, interaction designers, model trainers, evaluators, feedback providers, decision participants, collaboration leaders, operational controllers, autoridades ultimas

### 4.4.2 Organization-in-the-loop

- [P145] **DEFINICION** — OITL paradigm: organizaciones son enablers/mediators/regulators influencia AI, no solo usuarios → `Herrmann & Pfeiffer` 2023
- [P146] **REGLA** — OITL prioriza integracion sistemica human-technology-organization via 4 loops dinamicos: use, customization, task, context
- [P147] **REGLA** — sin alineamiento organizacional deliberado, disrupciones AI arriesgan undermining trust, fairness, bienestar empleados

### 4.4.3 Ecosystem-in-the-loop

- [P148] **DEFINICION** — intelligent ecosystems: ambientes interconectados large-scale donde multiples sistemas AI, humanos, organizaciones interactuan dinamicamente
- [P149] **DEFINICION** — human-AI joint cognitive ecosystem: sistemas cognitivos distribuidos donde cognicion/control emergen de actividades coordinadas across agentes
- [P150] **REGLA** — 4 pilares fundamentales: ecosystem-oriented system design, human-centered governance/ethics, dynamic collaboration/distributed intelligence, adaptation/learning/co-evolution

### 4.4.4 Society-in-the-loop

- [P151] **DEFINICION** — society-in-the-loop paradigm embebe valores, preocupaciones, contextos sociales en full AI lifecycle
- [P152] **DEFINICION** — bajo iSTS framework: inteligencia = propiedad emergente de interacciones humanos, AI, procesos organizacionales, instituciones sociales
- [P153] **REGLA** — 6 core approaches: systematic design thinking, human-centered design, multi-level design, organizational adaptation, human-AI co-learning, open ecosystem perspective
- [P154] **DEFINICION** — 9 subsistemas no-tecnicos clave: institutional environment, organizational structures, culture/values, human factors, social networks, trust/legitimacy, resource/economic structures, education/knowledge, political context

### 4.4.5 Implications Multi-Design Paradigms

- [P155] **REGLA** — HCAI practice debe extenderse mas alla human-AI interaction individual; implementacion completa requerida en todos niveles via multi-design paradigms
- [P156] **REGLA** — desde perspectiva sociotecnica, proyectos AI ya no son proyectos ingenieria sino proyectos sistema sociotecnico requiriendo colaboracion interdisciplinary

### 4.4 HCAI Process

- [P157] **TENSION** — desafio actual: fases tempranas diseno AI dependen practicas software engineering tradicionales; practitioners HCAI involucrados solo despues de fijar requirements
- [P158] **DEFINICION** — HCAI process integra HCD con ciclo desarrollo sistemas AI general → `ISO` 2019; `ISO/IEC` 2023
- [P159] **REGLA** — 4 features clave HCAI process: human-centered focus, iterative improvement, ethical development, interdisciplinary collaboration

### 4.5 HCAI Interdisciplinary Collaboration

- [P160] **REGLA** — colaboracion interdisciplinary es foundational (no meramente supportive) para realizacion HCAI
- [P161] **REGLA** — CS/AI sola carece grounding en necesidades/valores humanos; HCI/human factors sola carece poder computacional — su integracion hace HCAI viable
- [P162] **REGLA** — 8 estrategias estructuradas: shared goals, interdisciplinary teams, co-design stakeholders, resolucion sistematica conflictos eticos, procesos institucionalizados, frameworks decision transparentes, comunicacion continua, medicion exito holistica

### 4.6 HCAI Maturity Model (as HCAI-MF component)

- [P163] **DEFINICION** — HCAI-MM assessment spans 5 dimensiones: design/engineering practices, risk/incident management, organizational governance, metrics/evaluation, culture/ecosystem engagement
- [P164] **DEFINICION** — HCAI-MM 5 niveles elaborados: Initial (ad-hoc, sin input usuario) → Developing (understanding basica, usability testing temprano) → Defined (governance establecido, guidelines publicados, training lanzado) → Managed (HCAI en estrategia org, KPIs, involvement usuario continuo) → Optimizing (HCAI integral cultura/estrategia, lider industria, mejora continua)

### 5.1 Integrative Multi-Level Approaches

- [P165] **REGLA** — estrategia integrativa combina approach jerarquico hHCAI con implementacion tres-capas (project → organization → society) across AI lifecycle
- [P166] **REGLA** — capa proyecto: formacion equipo, proceso, metodos; capa organizacion: goals, guidelines, governance, cultura; capa societal: politicas, estandares, cultivacion talento

### 5.2 Enterprise Strategy

- [P167] **REGLA** — practica HCAI = transformacion empresarial integrando HCAI en strategic planning, business process reengineering, work-system redesign
- [P168] **HECHO** — frameworks globales (`OECD AI Principles`, `EU AI Act`, `NIST AI RMF`) proveen guidance accionable para alineamiento organizacional HCAI
- [P169] **REGLA** — HCAI-driven business reengineering: redisenar workflows para transparency, participatory design, accountability, human-led collaboration con AI

### 5.3 AI Risk Management and Governance

- [P170] **REGLA** — AI risk management efectivo: embeber consideraciones humanas/eticas en programa lifecycle continuo, mapear riesgos sociotecnicos colaborativamente con stakeholders diversos
- [P171] **REQUISITO** — integrar frameworks reconocidos: `NIST AI RMF` (Govern-Map-Measure-Manage), `ISO/IEC 23894`:2023, `ISO/IEC 42001`:2023
- [P172] **REQUISITO** — governance requiere traceability policy→control→evidence; sistema AI governance centralizado documentando proposito, data lineage, resultados evaluacion, performance post-deployment

### 5.4 Design Strategy

- [P173] **REGLA** — enterprise design strategy: integrar design thinking, UX design, HITL/HOTL design como componentes integrales AI lifecycle
- [P174] **REGLA** — organizaciones deben establecer AI readiness assessments evaluando design maturity, user trust, HCAI/ethical preparedness

### 5.5 Methodological Strategy

- [P175] **REGLA** — organizaciones deben tailorizar HCAI-MF a su tamano, madurez, goals
- [P176] **REGLA** — estrategia incluye: alinear HCAI con business objectives, pilot projects, leadership advocacy, training, KPIs trust/ethical compliance, toolkits estandarizados, proyectos high-impact

### 5.6 Progressive HCAI Practice

- [P177] **REGLA** — practica HCAI = proceso evolutivo progresando through HCAI-MM 5 niveles: Initial → Developing → Defined → Managed → Optimizing
- [P178] **REGLA** — madurez HCAI demostrada via: incremento stakeholder engagement, governance estructurado, ethical oversight, colaboracion interdisciplinary, aprendizaje continuo, outcomes medibles human-AI performance

### 6. Structure of Handbook

- [P179] **HECHO** — handbook organizado 10 secciones: Overview/Foundations, Human-AI Interaction, HCAI Design, HCAI Computing, Human Controllability, AI Risk Management, AI Governance, LLMs, Sectoral Applications, HCAI Practice — 59+ capitulos

### 7. Conclusion

- [P180] **REGLA** — exito AI medido no solo por sofisticacion tecnica sino por capacidad mejorar performance humano, salvaguardar dignidad, fortalecer beneficios/confianza societal
