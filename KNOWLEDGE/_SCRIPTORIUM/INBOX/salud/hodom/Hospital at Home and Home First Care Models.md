# Hospital at Home and Home First Care Models
<!-- /atomize · 148 proposiciones · 38 entidades · 1 archivo · 2026-04-10 -->
<!-- Consultar: buscar por [P###], por tipo (REQUISITO, EXCLUSION...), o por entidad -->

## hah.txt

### Introduction — The Changing Face of Healthcare

- [P001] **HECHO** — WHO proyecta: para 2030, 1/6 personas globalmente tendrá ≥60 años
- [P002] **HECHO** — enfermedades no transmisibles (NCDs) representan ~75% muertes globales
- [P003] **HECHO** — pandemia COVID-19 aceleró adopción tecnologías salud digital y programas HaH a escala global
- [P004] **DEFINICION** — atención centrada en paciente prioriza preferencias, necesidades y valores del individuo en cada decisión → `patient-centric care`
- [P005] **HECHO** — investigación muestra: atención domiciliaria reduce readmisiones hospitalarias, acorta recuperación, reduce costos, menos infecciones nosocomiales, mejor adherencia medicación

### Introduction — Defining HaH and Home First

- [P006] **DEFINICION** — HaH: programa estructurado que provee atención nivel hospitalario en domicilio: monitoreo clínico continuo, supervisión médica, terapia IV, oxígeno, imagenología, laboratorio
- [P007] **ALCANCE** — HaH efectivo para: neumonía, insuficiencia cardíaca, COPD, recuperación post-quirúrgica
- [P008] **HECHO** — pacientes HaH recuperan más rápido, menos complicaciones, mayor satisfacción vs. hospitalización tradicional
- [P009] **DEFINICION** — Home First: filosofía que prioriza domicilio como destino predeterminado para atención/recuperación en vez de hospital o cuidados prolongados
- [P010] **ALCANCE** — Home First especialmente beneficioso para pacientes ancianos recuperándose de estancias hospitalarias
- [P011] **REGLA** — Home First evita institucionalización innecesaria, promueve independencia, reduce complicaciones nosocomiales

### Chapter 2 — Origins and History of HaH

- [P012] **HECHO** — HaH emergió de tradiciones: enfermería comunitaria, servicios domiciliarios, cuidados paliativos comunitarios, innovación sistemas salud
- [P013] **HECHO** — fuerzas clave formando HaH: tradiciones enfermería, presiones sistema salud, evidencia ensayos, mejoras tecnológicas

### Chapter 2 — Core Principles and Framework

- [P014] **REQUISITO** — HaH: atención debe cumplir mismos estándares clínicos que atención hospitalaria para condiciones tratadas → `equivalencia clínica`
- [P015] **REQUISITO** — HaH requiere vías clínicas claras, protocolos escalamiento, capacidad transferencia rápida hospital
- [P016] **REQUISITO** — HaH requiere selección cuidadosa pacientes mediante criterios elegibilidad
- [P017] **REQUISITO** — HaH despliega equipo multidisciplinario: médicos, enfermeros, terapeutas (físicos/ocupacionales), farmacéuticos, trabajadores sociales, coordinadores → `MDT`
- [P018] **REQUISITO** — HaH requiere supervisión clínica 24/7 y escalamiento rápido con vías predefinidas
- [P019] **REQUISITO** — HaH requiere vías atención estandarizadas, checklists, documentación
- [P020] **REQUISITO** — HaH debe integrarse con servicios emergencia, atención primaria, farmacias, especialistas vía EHR y planes compartidos
- [P021] **REQUISITO** — HaH requiere evaluación preparación domicilio: entorno físico, presencia cuidador, riesgos seguridad
- [P022] **REQUISITO** — programas HaH rastrean: resultados clínicos, tasas readmisión, satisfacción paciente/cuidador, eventos adversos, costos

### Chapter 2 — Types of Patients and Contraindications

- [P023] **ALCANCE** — HaH indicado: exacerbaciones agudas condiciones crónicas (IC, COPD, asma), infecciones (neumonía, celulitis), recuperación post-operatoria, terapias infusión/parenterales, cuidados paliativos/fin de vida, observación diagnóstica
- [P024] **EXCLUSION** — HaH contraindicado: inestabilidad hemodinámica, procedimientos quirúrgicos complejos, falla respiratoria severa requiriendo ventilación mecánica, delirium severo/deterioro cognitivo sin soporte domiciliario, entornos domésticos inseguros
- [P025] **REGLA** — selección pacientes es clínica y contextual: evalúa datos médicos + soportes sociales + seguridad domicilio + preferencias paciente

### Chapter 2 — Technology in HaH

- [P026] **DEFINICION** — telemedicina: rondas médicas virtuales, conferencias familiares, evaluaciones urgentes vía video
- [P027] **DEFINICION** — RPM: wearables/dispositivos domiciliarios transmiten frecuencia cardíaca, saturación O2, presión arterial, temperatura, peso → `Remote Patient Monitoring`
- [P028] **DEFINICION** — pruebas point-of-care: glucosa portátil, paneles metabólicos, ultrasonido portátil, flebotomía móvil
- [P029] **HECHO** — tecnología genera preocupaciones: seguridad datos, alfabetización digital, confiabilidad internet, riesgo sobredependencia tecnológica

### Chapter 2 — Benefits

- [P030] **HECHO** — atención domiciliaria reduce exposición infecciones hospitalarias, delirium, desorientación por estancias prolongadas
- [P031] **OBLIGACION** — HaH puede aumentar responsabilidades cuidadores; programas deben proveer capacitación, respiro, servicios apoyo
- [P032] **REGLA** — HaH libera camas hospitalarias para casos más agudos
- [P033] **HECHO** — HaH demuestra costos menores por episodio de atención vs. estancias hospitalarias cuando estructurado adecuadamente

### Chapter 3 — Home First Philosophy

- [P034] **REGLA** — Home First desafía asunción: pregunta "¿por qué debe quedarse en hospital?" en vez de "¿por qué debe ir a casa?"
- [P035] **DEFINICION** — deconditioning: pérdida fuerza muscular, movilidad y confianza por inactividad/entorno desconocido en hospitalizaciones prolongadas
- [P036] **DEFINICION** — valores Home First: dignidad/autonomía, bienestar holístico, independencia/empoderamiento, atención centrada en comunidad

### Chapter 3 — HaH vs Home First

- [P037] **REGLA** — HaH: atención aguda nivel hospitalario como alternativa a admisión; Home First: alta temprana + recuperación domiciliaria
- [P038] **REGLA** — HaH foco: fase enfermedad aguda; Home First foco: fase post-aguda/transicional
- [P039] **REGLA** — HaH: intervenciones médicas intensivas (IV, oxígeno, monitoreo); Home First: rehabilitación, rehablement, cuidado personal, soporte comunitario
- [P040] **RESTRICCION** — HaH duración: corto plazo (días-semanas); Home First: mediano plazo (semanas-meses)
- [P041] **REGLA** — HaH y Home First son complementarios: pacientes pueden iniciar en HaH y transicionar a Home First

### Chapter 3 — Early Discharge and Reablement

- [P042] **REGLA** — planificación alta Home First inicia desde día admisión, no cuando paciente listo para alta
- [P043] **DEFINICION** — reablement: componente central Home First — ayudar individuos recuperar capacidad realizar tareas diarias independientemente → diferente de asistencia domiciliaria tradicional
- [P044] **REGLA** — Home First conecta pacientes con organizaciones voluntarias, grupos apoyo locales, proveedores atención primaria

### Chapter 3 — Case Studies (UK, Canada, Australia)

- [P045] **DEFINICION** — NHS "Discharge to Assess" (D2A): pacientes sin necesidad atención aguda dados de alta rápido, evaluaciones completadas en domicilio → `NHS`
- [P046] **HECHO** — NHS Home First: redujo estancias hospitalarias, mejoró satisfacción, menores readmisiones, redujo "bed blocking"
- [P047] **REGLA** — Ontario Home First: nadie ingresa cuidados prolongados directamente desde hospital si puede ir a casa con soportes adecuados → `Ontario`
- [P048] **HECHO** — Ontario: caída significativa pacientes ALC (alternate level of care) ocupando camas hospitalarias
- [P049] **HECHO** — Australia: programas Early Supported Discharge reducen estancias hospitalarias hasta 30% → `Australia`

### Chapter 3 — Social Care and Family

- [P050] **REGLA** — equipos cuidado social evalúan entornos domiciliarios, gestionan equipamiento adaptativo, coordinan trabajadores soporte
- [P051] **REGLA** — familias en Home First son socios activos: reciben capacitación medicación, movilidad segura, signos alarma + soporte respiro

### Chapter 4 — Interdisciplinary Team

- [P052] **REQUISITO** — equipo MDT core: médicos, enfermeros, terapeutas (PT/OT/habla), trabajadores sociales, farmacéuticos, coordinadores atención
- [P053] **DEFINICION** — coordinadores atención: eje del programa, facilitan comunicación, rastrean progreso, primer punto contacto paciente

### Chapter 4 — Patient Selection

- [P054] **REQUISITO** — elegibilidad HaH/Home First: condición estable sin equipo hospitalario intensivo, monitoreable vía telemedicina, bajo riesgo deterioro súbito
- [P055] **ALCANCE** — condiciones aptas HaH: exacerbaciones COPD, manejo CHF, recuperación post-quirúrgica vitales estables, neumonía/celulitis/infecciones leves con IV, cuidados paliativos
- [P056] **REQUISITO** — evaluación psicosocial: voluntad paciente, capacidad familia/cuidador, condición física hogar, disponibilidad tecnología comunicación
- [P057] **REGLA** — consentimiento debe ser voluntario, basado en comprensión, no presión; respetar autonomía paciente

### Chapter 4 — Home Assessment

- [P058] **REQUISITO** — evaluación domicilio: accesibilidad, iluminación/ventilación, preparación emergencias, saneamiento/higiene
- [P059] **REGLA** — si se identifican riesgos: equipo gestiona modificaciones (barras agarre, rampas, camas ajustables)
- [P060] **REQUISITO** — hogar puede necesitar: dispositivos médicos (concentradores O2, bombas infusión, monitores), herramientas salud digital, ayudas movilidad, conectividad internet confiable

### Chapter 4 — Individualized Care Plans

- [P061] **REQUISITO** — plan atención individualizado incluye: esquema clínico, metas rehabilitación, servicios apoyo, protocolos emergencia, calendario seguimiento
- [P062] **REQUISITO** — planes deben evolucionar según condición paciente con revisiones semanales o datos monitoreo remoto
- [P063] **REGLA** — pacientes deben participar activamente en decisiones: fomenta apropiación y empoderamiento

### Chapter 4 — Integration and Coordination

- [P064] **REGLA** — EHR compartidos permiten proveedores hospital/comunidad acceder datos actualizados, previniendo duplicación y errores
- [P065] **REQUISITO** — comunicación alta debe detallar: medicamentos, citas seguimiento, puntos contacto
- [P066] **REQUISITO** — hospitales, aseguradoras, agencias gobierno deben alinear políticas: marcos reembolso, capacitación, infraestructura comunitaria
- [P067] **REGLA** — alianzas comunitarias (clínicas locales, voluntarios, centros rehabilitación) extienden alcance atención más allá necesidades médicas

### Chapter 5 — Telehealth

- [P068] **HECHO** — telesalud elimina tiempo viaje, ayudando pacientes zonas remotas/rurales acceder especialistas
- [P069] **REGLA** — plataformas telesalud combinan videoconferencia, mensajería segura, registros digitales para replicar experiencia clínica virtualmente

### Chapter 5 — Remote Patient Monitoring

- [P070] **REGLA** — RPM permite detección temprana, empoderamiento paciente, reducción readmisiones, atención personalizada vía datos
- [P071] **HECHO** — ejemplo: paciente IC con parche conectado monitoreando ritmo cardíaco y balance fluidos; alertas automáticas al equipo clínico

### Chapter 5 — EHR Integration

- [P072] **DEFINICION** — EHR centralizan historia médica, medicamentos, resultados lab, imágenes, planes atención en sistema digital único accesible por profesionales autorizados → `Electronic Health Records`
- [P073] **REQUISITO** — interoperabilidad EHR requiere estándares unificados, protocolos intercambio datos seguros, colaboración proveedores tecnología/autoridades salud

### Chapter 5 — AI in Home Care

- [P074] **DEFINICION** — AI analytics predictivo detecta patrones sutiles (cambios frecuencia cardíaca, O2) señalando deterioro para intervención temprana
- [P075] **DEFINICION** — chatbots AI responden preguntas pacientes, proveen recordatorios medicación, soporte emocional 24/7
- [P076] **HECHO** — reconocimiento voz/movimiento en smart homes detecta caídas, cambios patrones habla (Parkinson, recuperación ACV)
- [P077] **REGLA** — AI más efectiva complementando empatía humana; tecnología provee insight, humanos proveen sanación

### Chapter 5 — Data Privacy and Security

- [P078] **REQUISITO** — pacientes deben ser informados: qué datos se recopilan, cómo se usan/comparten, quién tiene acceso, derecho retirar consentimiento
- [P079] **REQUISITO** — ciberseguridad requiere: encriptación end-to-end, autenticación multifactor, auditorías seguridad regulares, protocolos respaldo
- [P080] **RESTRICCION** — algoritmos AI entrenados con datos sesgados producen resultados inequitativos; deben desarrollarse/testearse con poblaciones diversas

### Chapter 6 — Cost Comparison

- [P081] **HECHO** — atención domiciliaria nivel hospitalario cuesta 30-50% menos que tratamiento equivalente internación (estudios US, Australia, UK)
- [P082] **HECHO** — factores reducción costo: menor infraestructura, menor personal, menor estancia, menos complicaciones

### Chapter 6 — Payment and Reimbursement

- [P083] **REGLA** — modelos atención basados en valor más compatibles con HaH/Home First que modelos fee-for-service
- [P084] **HECHO** — Medicare Acute Hospital Care at Home permite hospitales facturar atención aguda domiciliaria como si fuera intrahospitalaria → `CMS`
- [P085] **DEFINICION** — pagos bundled: pago único cubre episodio completo (hospitalización + atención domiciliaria + seguimiento)
- [P086] **DEFINICION** — modelos capitación: monto fijo por paciente, incentivando mantenimiento salud y prevención readmisiones
- [P087] **REGLA** — alianzas público-privadas ayudan expandir acceso compartiendo riesgo financiero

### Chapter 6 — Economic Benefits and Readmissions

- [P088] **REGLA** — HaH optimiza utilización camas, reduce readmisiones, mejora eficiencia personal, aumenta satisfacción paciente
- [P089] **HECHO** — readmisiones hospitalarias entre ineficiencias más costosas del sistema salud; indican planificación alta inadecuada
- [P090] **OBLIGACION** — políticas deben asegurar atención domiciliaria no traslade carga económica injustamente a familias; necesarios: estipendios cuidadores, cobertura suministros, servicios respiro

### Chapter 7 — Psychological Benefits

- [P091] **HECHO** — recuperación domiciliaria reduce ansiedad/depresión vs. hospital; presencia familiar reduce miedo/aislamiento
- [P092] **HECHO** — recuperación domiciliaria mejora sueño sin interrupciones hospitalarias (ruido, controles vitales, iluminación)
- [P093] **HECHO** — pacientes domicilio sienten mayor control, autonomía y dignidad; actos simples (elegir cuándo comer/descansar) restauran independencia

### Chapter 7 — Cultural and Social Factors

- [P094] **HECHO** — aceptación atención domiciliaria influida por: condiciones socioeconómicas, roles género, confianza tecnología, comunidad/fe
- [P095] **HECHO** — mujeres frecuentemente cuidadoras primarias; responsabilidades adicionales aumentan estrés sin sistemas soporte adecuados
- [P096] **REGLA** — atención domiciliaria soporta dignidad fin de vida: transición pacífica rodeada de familia

### Chapter 8 — Clinical Metrics

- [P097] **HECHO** — pacientes HaH bien manejados: mortalidad similar o menor vs. internados
- [P098] **HECHO** — HaH reduce tasas readmisión mediante monitoreo efectivo e intervención temprana
- [P099] **HECHO** — HaH acorta duración tratamiento agudo → recuperación más rápida, costos reducidos
- [P100] **HECHO** — sistemas salud usan PROMs y PREMs para capturar satisfacción paciente → `Patient-Reported Outcome/Experience Measures`

### Chapter 8 — Safety and Quality

- [P101] **REGLA** — control infecciones domiciliario: educación, suministros saneamiento, supervisión regular; resultado frecuente: menos infecciones que hospital
- [P102] **REQUISITO** — cada hogar HaH: evaluación seguridad verificando peligros (desorden, mascotas, accesibilidad limitada)
- [P103] **REQUISITO** — cada programa HaH debe establecer vías escalamiento claras con sistemas respuesta rápida
- [P104] **REQUISITO** — programas rastrean resultados vs. benchmarks nacionales/institucionales; auditorías regulares y revisiones desempeño
- [P105] **HECHO** — organismos acreditación (Joint Commission US, CQC UK) tienen criterios específicos atención domiciliaria: seguridad, personal, tecnología, derechos paciente
- [P106] **REQUISITO** — programas acreditados deben publicar reportes desempeño

### Chapter 9 — Institutional Resistance

- [P107] **HECHO** — resistencia institucional HaH: inercia cultural/profesional, miedo riesgo/responsabilidad, barreras financieras/estructurales
- [P108] **⚠ TENSION** — ingresos hospitalarios dependen admisiones/ocupación camas; transición atención domiciliaria puede reducir ingresos sin financiamiento alternativo

### Chapter 9 — Legal and Regulatory

- [P109] **⚠ TENSION** — "atención hospitalaria" definida legalmente por infraestructura física en muchas jurisdicciones; atención domiciliaria carece reconocimiento legal explícito
- [P110] **⚠ TENSION** — responsabilidad incierta cuando atención fuera límites físicos hospital: supervisión médica, delegación enfermería, respuesta emergencia
- [P111] **RESTRICCION** — datos paciente dispositivos domiciliarios deben cumplir HIPAA (US) o GDPR (Europa); países desarrollo pueden carecer leyes protección datos

### Chapter 9 — Workforce and Technology Gaps

- [P112] **⚠ TENSION** — escasez global profesionales salud tensa hospitales; redirigir clínicos a atención domiciliaria puede exacerbar escasez
- [P113] **REQUISITO** — atención domiciliaria requiere habilidades únicas: toma decisiones independiente, comunicación/empatía, competencia telemedicina, sensibilidad cultural
- [P114] **RESTRICCION** — internet no confiable, cobertura red pobre, electricidad inconsistente restringen severamente telesalud en áreas rurales/desatendidas
- [P115] **RESTRICCION** — costos equipamiento digital pueden hacer implementación prohibitiva en países desarrollo
- [P116] **⚠ TENSION** — riesgo: modelos HaH/Home First solo sirvan quienes tienen vivienda estable, soporte familiar, acceso digital — profundizando desigualdades
- [P117] **RESTRICCION** — familias bajos ingresos pueden carecer condiciones: espacios limpios, refrigeración medicamentos, comunicación confiable

### Chapter 10 — Training and Skills

- [P118] **REQUISITO** — clínicos domiciliarios deben asumir responsabilidades amplias: evaluaciones complejas, tratamientos, educación familiar, enlace remoto médicos
- [P119] **REQUISITO** — capacitación debe incluir módulos: telesalud, evaluación seguridad domiciliaria, engagement paciente-familia
- [P120] **REGLA** — aprendizaje basado en simulación permite profesionales practicar escenarios atención domiciliaria en entornos controlados

### Chapter 10 — Leadership and Retention

- [P121] **REGLA** — enfermeros/terapeutas/auxiliares frontline pueden empoderarse como micro-líderes: identificando desafíos, implementando innovaciones, mentoreando pares
- [P122] **REQUISITO** — retención workforce requiere: horarios flexibles, cargas razonables, acceso consejería, pago competitivo, reembolso viajes
- [P123] **OBLIGACION** — gobiernos deben: financiar desarrollo profesional, establecer ratios dotación seguros, integrar atención domiciliaria en estrategias nacionales salud

### Chapter 11 — US Case Studies

- [P124] **HECHO** — Johns Hopkins pioneró HaH en US en 1990s; demostró 30-40% reducción costos/admisión, menos complicaciones, mayor satisfacción → `Johns Hopkins`
- [P125] **HECHO** — Mayo Clinic Advanced Care at Home: diseño hub-and-spoke tecnológico; centro comando monitorea pacientes 24/7, coordinando enfermeros/técnicos visitas domiciliarias → `Mayo Clinic`
- [P126] **HECHO** — Mount Sinai extendió HaH a población urbana diversa NYC, enfatizando equidad para barrios bajos ingresos → `Mount Sinai`
- [P127] **HECHO** — waiver Medicare "Acute Hospital Care at Home" de CMS asegura sostenibilidad financiera programas US → `CMS`

### Chapter 11 — UK Case Studies

- [P128] **REGLA** — NHS Home First (Discharge to Assess): pacientes médicamente estables dados alta ASAP; evaluación/rehabilitación en domicilio → `NHS`
- [P129] **HECHO** — NHS Home First redujo altas retrasadas, mejoró moral paciente, mejoró colaboración salud-cuidado social

### Chapter 11 — Australia and Developing Countries

- [P130] **HECHO** — Australia HITH reconocido como alternativa mainstream financiada públicamente desde 1990s → `HITH`
- [P131] **HECHO** — HITH Australia: reducciones costo 20-40% vs. atención hospitalaria
- [P132] **HECHO** — India ASHA workers, Ethiopia Health Extension Program, Rwanda Community Health Program: modelos impulsados por CHW en naciones desarrollo → `ASHA`, `CHW`
- [P133] **HECHO** — Rwanda redujo mortalidad materna/infantil mediante visitas domiciliarias y supervisión soporte telesalud
- [P134] **HECHO** — tecnologías mHealth empoderan CHW en entornos recursos limitados: registrar datos, acceder teleconsultas, monitorear enfermedades crónicas

### Chapter 12 — Regulatory Framework

- [P135] **HECHO** — CMS introdujo waiver Acute Hospital Care at Home estableciendo criterios nacionales US (2021) → `CMS`
- [P136] **HECHO** — CQC supervisa Home First y servicios atención comunitaria en UK → `CQC`
- [P137] **HECHO** — Joint Commission e ISO Health Management Systems proveen acreditación atención domiciliaria → `Joint Commission`

### Chapter 12 — Informed Consent and Patient Rights

- [P138] **REQUISITO** — consentimiento informado debe cubrir: naturaleza/alcance atención domiciliaria, riesgos/beneficios/limitaciones vs. hospital, roles cuidadores/tecnologías, derecho retirar/solicitar transferencia
- [P139] **REQUISITO** — atención domiciliaria debe mantener derechos: privacidad/confidencialidad, atención segura/competente, dignidad/respeto, información alternativas/costos
- [P140] **REGLA** — pacientes nunca deben sentirse presionados elegir atención domiciliaria por conveniencia financiera/institucional

### Chapter 12 — Liability and Government Support

- [P141] **REGLA** — responsabilidad eventos adversos puede recaer en hospital, agencia domiciliaria, o paciente/familia — documentación clara y acuerdos necesarios
- [P142] **HECHO** — US CARES Act + CMS Waiver permitió hospitales facturar Medicare atención aguda domiciliaria → `CARES Act`
- [P143] **HECHO** — UK NHS Long Term Plan invierte en servicios comunitarios integrados para reducir dependencia hospitalaria
- [P144] **REGLA** — incentivos gobierno incluyen: paridad reembolso, grants telesalud, beneficios fiscales salud digital, capacitación workforce
- [P145] **OBLIGACION** — leyes licenciamiento deben reconocer atención domiciliaria como práctica médica legítima

### Chapter 13 — Faith, Spirituality, Community

- [P146] **HECHO** — espiritualidad promueve resiliencia emocional, tolerancia dolor, bienestar general en pacientes
- [P147] **HECHO** — comunidades fe (iglesias) sirven como pilares alcance salud: visitan enfermos, proveen comidas, oración, cuidado respiro

### Chapter 14 — Future of Home-Based Healthcare

- [P148] **DEFINICION** — hospital virtual: plataformas digitales, telemedicina, tecnologías salud conectadas para atención nivel hospitalario remota sin edificio físico → `virtual hospital`
