---
_manifest:
  urn: urn:hi:kb:atomic-health-informatics-fundamental-03
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
      n_propositions: 200
      producer: urn:kora:artefacto:atomize
      source_corpus: Fundamental Knowledge in Health Informatics (curso HI)
      segmented: true
      segment_role: segment
      hand_edited: true
      segment_index: 3
      segment_count: 4
---

# Fundamental Knowledge in Health Informatics - Segmento 03

## Resumen

- Productor canonico: `urn:kora:artefacto:atomize`
- Corpus fuente: `../../INBOX/hi/hi.md`
- Proposiciones: `200`
- Fuentes: `1`
- Segmentado: `si`
- Segmento: `03/04`
- Rango: `P401-P600`

## Indice de fuentes

- `S01` · [hi.md](../../INBOX/hi/hi.md) · Fuente primaria del corpus atomizado

## Proposiciones

Segmento 03 del corpus atomizado.

- **P401** · `definition` · limitation of liability = limita responsabilidad agregada vendor (e.g., tarifa licencia pagada); estrategia HCO: negociar tope múltiplo tarifa licencia (300%-500%) · [src:S01](../../INBOX/hi/hi.md)
- **P402** · `definition` · exclusion of liability = excluye totalmente ciertos tipos daño de recuperación (consecuenciales, indirectos, especiales, punitivos, incidentales, pérdida ganancias/datos) · [src:S01](../../INBOX/hi/hi.md)
- **P403** · `rule` · cláusulas feedback pueden requerir HCO asignar propiedad sugerencias/ideas/mejoras a vendor; como máximo, debería otorgar vendor solo licencia no exclusiva usar feedback "as is" · [src:S01](../../INBOX/hi/hi.md)
- **P404** · `rule` · acuerdo licencia debería prohibir vendor usar nombre/marca/logo HCO en marketing sin consentimiento escrito · [src:S01](../../INBOX/hi/hi.md)
- **P405** · `rule` · propiedad datos HCO debe especificarse en acuerdo, especialmente datos agregados/salud poblacional; provisiones deberían proteger datos paciente incluso si de-identificados · [src:S01](../../INBOX/hi/hi.md)

### Ch 20: Implementing and Upgrading an Information System

- **P406** · `fact` · ARRA promulgada 2009, generando HITECH Act; objetivo primario: cada persona US tenga registro médico digital certificado 2014 con intercambio información salud electrónica · [src:S01](../../INBOX/hi/hi.md)
- **P407** · `fact` · HITECH creó programa incentivos $27B federalmente financiado proveyendo pagos Medicare/Medicaid 5-10 años a proveedores/hospitales elegibles/critical access hospitals · [src:S01](../../INBOX/hi/hi.md)
- **P408** · `fact` · MU Stage 1 comenzó 2011 (captura datos paciente); Stage 2 comenzó 2014 (prácticas clínicas avanzadas/portales paciente); Stage 3 comenzó 2017 (interoperabilidad/resultados paciente) · [src:S01](../../INBOX/hi/hi.md)
- **P409** · `fact` · CCHIT comenzó testear/certificar aplicaciones software 2006; cesó operaciones 2014; ONC ahora gestiona programa certificación EHR (comenzó 2010) · [src:S01](../../INBOX/hi/hi.md)
- **P410** · `fact` · adopción EHR hospitales US: 16% (2009) → 35% (2011) → 76% EHR básico (2014) → 9 de 10 hospitales usando EHR informar práctica (2019 reporte AHA) · [src:S01](../../INBOX/hi/hi.md)
- **P411** · `fact` · 21st Century Cures Act firmada diciembre 13, 2016; objetivo: mejorar acceso/intercambio/utilización electrónica información salud pacientes/proveedores · [src:S01](../../INBOX/hi/hi.md)
- **P412** · `definition` · information blocking = práctica por desarrollador HIT, red/exchange información salud, o proveedor healthcare probablemente interfiriendo acceso/intercambio/uso EHI · [src:S01](../../INBOX/hi/hi.md)
- **P413** · `fact` · Cures Act especifica 8 excepciones information blocking: Preventing Harm, Privacy, Security, Infeasibility, Health IT Performance, Licensing, Fees, Content/Manner · [src:S01](../../INBOX/hi/hi.md)
- **P414** · `fact` · USCDI requiere 8 tipos notas clínicas disponibles pacientes sin cargo: consulta, resumen alta, H&P, narrativas imagen, reportes lab, reportes patología, notas procedimiento, notas progreso · [src:S01](../../INBOX/hi/hi.md)
- **P415** · `definition` · e-iatrogenesis = tipo crítico nuevo errores introducidos por EHRs, incluyendo errores yuxtaposición (seleccionar paciente/medicamento equivocado de lista) (Weiner et al. 2007) · [src:S01](../../INBOX/hi/hi.md)
- **P416** · `fact` · estudio TRIP (AHRQ 1999): promedio 10-20 años incorporar nuevos hallazgos clínicos práctica general ("lethal lag"); CDS/EBP puede acelerar · [src:S01](../../INBOX/hi/hi.md)
- **P417** · `definition` · scope creep contexto SDLC = expansión no controlada alcance producto/proyecto sin ajustes tiempo/costo/recursos (HIMSS 2017); mitigado control cambios estricto · [src:S01](../../INBOX/hi/hi.md)
- **P418** · `scope` · grupos proceso PMBOK: Initiating, Planning, Executing, Monitoring/Controlling, Closing; etapas SDLC: Planning, Requirements Gathering, Design, Coding, Testing, Deployment/Maintenance · [src:S01](../../INBOX/hi/hi.md)
- **P419** · `definition` · superuser = staff organizacional con training adicional que entiende nuevos workflows, provee soporte at-the-elbow durante go-live y después · [src:S01](../../INBOX/hi/hi.md)
- **P420** · `definition` · UAT (User Acceptance Testing) = etapa testing final antes go-live donde vendor/HCO depuran software funcionalidad final; tres features clave: estrategia, escenarios, scripts · [src:S01](../../INBOX/hi/hi.md)
- **P421** · `definition` · big bang go-live = todas aplicaciones/módulos implementados a la vez; menor costo total, implementación más corta, pero caída productividad significativa inicialmente · [src:S01](../../INBOX/hi/hi.md)
- **P422** · `definition` · phased/incremental go-live = procesos viejos y nuevos coexisten; permite tiempo para build/cambios workflow pero mayor costo total, duración más larga · [src:S01](../../INBOX/hi/hi.md)
- **P423** · `rule` · fecha go-live debería evitar fines semana/lunes/viernes/feriados importantes cuando soporte vendor menos disponible; excepciones: sistemas financieros (deben iniciar medianoche 1° día mes) · [src:S01](../../INBOX/hi/hi.md)
- **P424** · `definition` · change freeze/moratorium = período (típicamente 1-2 semanas antes a ~1 semana después go-live) donde ningún otro cambio sistema permitido · [src:S01](../../INBOX/hi/hi.md)
- **P425** · `definition` · data abstraction = proceso ingresar/poblar chart electrónico con datos clínicos registros papel u otras fuentes · [src:S01](../../INBOX/hi/hi.md)
- **P426** · `rule` · training end-user debería ocurrir no más 4-6 semanas antes go-live facilitar retención; ambiente práctica disponible post-clase ejercicios competencia · [src:S01](../../INBOX/hi/hi.md)
- **P427** · `requirement` · categorías training: superuser training (training adicional + comprensión workflow), role-based training (médico/enfermero/terapeuta), process-based training (workflow como admisión hospital) · [src:S01](../../INBOX/hi/hi.md)
- **P428** · `fact` · 2015 Edition Cures Update introdujo criterios certificación técnica requiriendo HL7 FHIR Release 4 para export/acceso paciente EHI, más criterios cybersecurity (encripción, auth multi-factor) · [src:S01](../../INBOX/hi/hi.md)
- **P429** · `fact` · Tall Man lettering (mixed-case) usada nombres medicamentos look-alike per recomendación ISMP disminuir errores medicación; ejemplos: NiFEDipine vs niCARdipine, DOBUTamine vs DOPamine · [src:S01](../../INBOX/hi/hi.md)

### Ch 21: Downtime and Disaster Recovery for HIS

- **P430** · `definition` · downtime = período sistemas computador no disponibles usuarios; causado errores humanos, fallas software/hardware, cables energía cortados, malware/ransomware, desastres naturales · [src:S01](../../INBOX/hi/hi.md)
- **P431** · `fact` · 2016 Ponemon Institute: costo promedio downtime healthcare $740,357 por incidente (~$8,800/min) · [src:S01](../../INBOX/hi/hi.md)
- **P432** · `fact` · 2020: 92 ataques ransomware afectaron >600 clínicas/hospitales, >18M registros pacientes; costo estimado ~$21B (Comparitech/Bischoff 2021) · [src:S01](../../INBOX/hi/hi.md)
- **P433** · `rule` · planificación downtime debería ocurrir desde inicio proyecto hasta soporte/mantenimiento sistema; debe incluir todos sistemas/infraestructura existentes · [src:S01](../../INBOX/hi/hi.md)
- **P434** · `scope` · elementos infraestructura IT planificación downtime: software EHR, sistemas clínicos/ancilares, PACS, apps lab/cardiología/radiología, software revenue cycle, interfaces/engine interfaces, enterprise data warehouse · [src:S01](../../INBOX/hi/hi.md)
- **P435** · `scope` · elementos infraestructura física: servidores, almacenamiento, energía eléctrica, switches/hubs/firewalls red, puntos acceso wireless, dispositivos biomédicos, workstations/impresoras, componentes edificio, UPS, generadores · [src:S01](../../INBOX/hi/hi.md)
- **P436** · `definition` · CMDB (Configuration Management Database) = best practice ITIL mantener inventario/documentación sistema con ítems configuración únicos organización · [src:S01](../../INBOX/hi/hi.md)
- **P437** · `scope` · niveles downtime: Level 1 (parte sistema, <1h, impacto mínimo) → Level 2 (sistema completo, hasta 4h) → Level 3 (múltiples sistemas, >4h) → Level 4 (todos sistemas/red, causa raíz conocida) → Level 5 (todos sistemas/red, ransomware/catastrófico, rebuild requerido) · [src:S01](../../INBOX/hi/hi.md)
- **P438** · `definition` · hot site = facilidad recuperación con hardware standby, habilita recuperación Tier I ≤24h; warm site = intermedio; cold site = capacidad hospedar sistemas pero tiempo recuperación mayor (e.g., 30 días) · [src:S01](../../INBOX/hi/hi.md)
- **P439** · `obligation` · organizaciones obligadas mantener planes contingencia/desastre per HIPAA security rule 1996, requerimientos HHS, cuerpos acreditación · [src:S01](../../INBOX/hi/hi.md)
- **P440** · `definition` · business continuity management = complementario disaster recovery; alcance mayor incluyendo disponibilidad servicios admin/healthcare, determinando qué sistemas recuperar primero usando sistema tiers · [src:S01](../../INBOX/hi/hi.md)
- **P441** · `scope` · tiers business continuity: Tier I (crítico, recuperar primero, ≤24h, requiere hot site); Tier II (≤72h); Tier III (≤1 semana); Tier IV (≤1 mes) · [src:S01](../../INBOX/hi/hi.md)
- **P442** · `definition` · Downtime Determinator = herramienta risk assessment (Brazelton/Lyons); x-axis = tiempo recuperación, y-axis = impacto/riesgo; grafica 7 componentes riesgo en 4 cuadrantes · [src:S01](../../INBOX/hi/hi.md)
- **P443** · `rule` · sistemas redundantes/backup deben proveer subconjunto datos críticos durante downtime: demographics, órdenes, MAR, vitales recientes, valores lab, reportes imagen, notas progreso proveedor · [src:S01](../../INBOX/hi/hi.md)
- **P444** · `rule` · máquinas downtime redundantes deben cumplir requerimientos HIPAA seguridad/privacidad/confidencialidad; requieren capa encripción extra prevenir robo info si removidas hospital · [src:S01](../../INBOX/hi/hi.md)
- **P445** · `definition` · ciclo vida servicio ITIL: estrategia, diseño, transición, operación, mejora continua · [src:S01](../../INBOX/hi/hi.md)
- **P446** · `rule` · manuales planificación desastre deben estar disponibles múltiples formatos media incluyendo formatos no-dependientes red; evaluados/actualizados ≥anualmente y probados/simulados · [src:S01](../../INBOX/hi/hi.md)
- **P447** · `rule` · cada unidad clínica/negocio necesita políticas/procedimientos downtime específicos; debe incluir instrucciones sobre ingreso datos requerido registro EHR permanente conclusión downtime · [src:S01](../../INBOX/hi/hi.md)
- **P448** · `requirement` · downtime box best practice: todas unidades paciente/áreas negocio mantienen caja física con formularios documentación, instrucciones papel, formularios ≥24 horas, instrucciones restocking · [src:S01](../../INBOX/hi/hi.md)
- **P449** · `rule` · cinco componentes plan comunicación downtime: quién necesita saber, qué detalles necesarios, qué media/modos usados, quién comunica qué, qué sistemas/workflows afectados · [src:S01](../../INBOX/hi/hi.md)
- **P450** · `fact` · teléfonos analógicos deberían estar disponibles áreas clave hospital (identificados color diferente, e.g., rojo) porque funcionan durante downtimes red/eléctricos cuando teléfonos VOIP no · [src:S01](../../INBOX/hi/hi.md)
- **P451** · `rule` · ejercicios desastre/downtime requeridos por agencias regulatorias/acreditación (The Joint Commission); training todos nuevos empleados orientación, actualizado ≥anualmente como componente competencia · [src:S01](../../INBOX/hi/hi.md)

## Section 5: Usability, Analytics, and Education

### Ch 22: Improving the User Experience for Health IT

- **P452** · `definition` · usabilidad (ISO 9241-11, 1998) = extensión producto puede ser usado por usuarios específicos contexto específico lograr objetivos específicos con efectividad, eficiencia, satisfacción · [src:S01](../../INBOX/hi/hi.md)
- **P453** · `definition` · tres objetivos usabilidad ISO: (1) efectividad = precisión/completitud logro objetivos incluyendo seguridad; (2) eficiencia = recursos gastados relativo precisión; (3) satisfacción = comfort/aceptabilidad usuarios asocian con producto · [src:S01](../../INBOX/hi/hi.md)
- **P454** · `definition` · UCD = tres axiomas: (1) enfoque temprano/central en usuarios, (2) diseño iterativo, (3) medidas sistemáticas interacciones usuario-producto (Gould & Lewis; Rubin & Chisnell 2008) · [src:S01](../../INBOX/hi/hi.md)
- **P455** · `rule` · UCD requiere mínimo tres rondas diseño iterativo; un diseño nunca es adecuado · [src:S01](../../INBOX/hi/hi.md)
- **P456** · `definition` · human factors (HFES 2012) = disciplina científica entendiendo interacciones humanos/otros elementos sistema optimizar bienestar humano y rendimiento sistema general · [src:S01](../../INBOX/hi/hi.md)
- **P457** · `definition` · ergonomía = intercambiable con human factors en Europa; en US enfoca rendimiento humano con características físicas herramientas/sistemas; distinción: ergonomía física (diseño workstation) vs ergonomía cognitiva (diseño interfaz) · [src:S01](../../INBOX/hi/hi.md)
- **P458** · `definition` · HCI = estudio cómo personas diseñan, implementan, evalúan sistemas computador interactivos contexto tareas/trabajo usuarios · [src:S01](../../INBOX/hi/hi.md)
- **P459** · `definition` · cognitive informatics combina ciencias cognitivas/información aumentar comprensión/descripción/predicción productos/resultados healthcare; puede usar miles/millones interacciones registradas vs 5-15 usuarios estudios usabilidad · [src:S01](../../INBOX/hi/hi.md)
- **P460** · `fact` · TJC 2015 evaluó 3375 reportes eventos adversos, identificó 120 eventos sentinel relacionados HIT; 1/3 provenientes factores interfaz humano-computador, 24% issues workflow/comunicación · [src:S01](../../INBOX/hi/hi.md)
- **P461** · `fact` · AMA 2014 emitió llamado firmado 30 organizaciones médicas soluciones EHRs pobremente diseñados · [src:S01](../../INBOX/hi/hi.md)
- **P462** · `fact` · evaluaciones admisión acute care pueden tomar 30-60 minutos involucrando 532 clicks · [src:S01](../../INBOX/hi/hi.md)
- **P463** · `fact` · frameworks HCI disponibles: FITT (Ammenwerth 2006), UFuRT/TURF (Zhang & Butler), framework error technology-induced (Borycki 2012), SEIPS (Carayon 2020) · [src:S01](../../INBOX/hi/hi.md)
- **P464** · `definition` · SEIPS 3.0 = modelo centrado sistemas trabajo y centralidad paciente; enfoque expandido journey paciente, episodios cuidado distribuidos tiempo/localización · [src:S01](../../INBOX/hi/hi.md)
- **P465** · `definition` · framework HHCI elementos: usuarios, productos, contexto, tareas, información, interacciones, timeline desarrollo; información = mecanismo intercambio (Staggers) · [src:S01](../../INBOX/hi/hi.md)
- **P466** · `definition` · discount usability methods (Nielsen 1993) = técnicas reduciendo usuarios requeridos, usando prototipos diseño temprano; técnica más común = heuristic evaluation (HE) · [src:S01](../../INBOX/hi/hi.md)
- **P467** · `fact` · HE por 3-5 expertos dual domain puede encontrar 81-90% problemas usabilidad existentes (Nielsen 1992) · [src:S01](../../INBOX/hi/hi.md)
- **P468** · `fact` · sets heurísticos disponibles: Nielsen 10 (1995), Zhang et al. 14 (2003), Dix et al. 10 (2004), Shneiderman 8 golden rules (2005), HIMSS 9 principios usabilidad (2009) · [src:S01](../../INBOX/hi/hi.md)
- **P469** · `fact` · escala severidad Zhang: 0=sin problema, 1=cosmético, 2=menor, 3=mayor, 4=catástrofe usabilidad (debe corregirse antes release, especialmente relacionado seguridad paciente) · [src:S01](../../INBOX/hi/hi.md)
- **P470** · `definition` · think-aloud protocol = usuarios hablan en voz alta mientras interactúan producto; tan pocos como 5 usuarios pueden detectar 60-80% errores diseño (Nielsen); 5-8 usuarios suficientes mayoría tests usabilidad tempranos · [src:S01](../../INBOX/hi/hi.md)
- **P471** · `definition` · task analysis = término genérico >100 técnicas desde análisis tarea cognitiva a interacciones usuario observables; usado temprano ciclo vida sistemas · [src:S01](../../INBOX/hi/hi.md)
- **P472** · `fact` · cuestionarios usabilidad: SUS (Brooke 1986, estándar industria, 10 ítems, disponible público), QUIS, Purdue Usability Testing Questionnaire (100 open-ended), SUMI · [src:S01](../../INBOX/hi/hi.md)
- **P473** · `rule` · investigadores recomiendan ≥15 usuarios testing usabilidad sumativo (Virzi 1992) · [src:S01](../../INBOX/hi/hi.md)
- **P474** · `fact` · FDA ha requerido testing usabilidad dispositivos médicos >20 años; otros vendors HIT/organizaciones salud solo comenzando emplear principios usabilidad · [src:S01](../../INBOX/hi/hi.md)
- **P475** · `fact` · ONC publicó ONC Change Package for Improving EHR Usability ayudar sistemas healthcare incorporar conceptos/herramientas usabilidad básica (2018) · [src:S01](../../INBOX/hi/hi.md)
- **P476** · `fact` · Nielsen Norman Group estimó ganancias productividad rediseño intranet: 8x costos (1000 empleados), 20x (10,000), 50x (100,000); incremento productividad usuario promedio 161% · [src:S01](../../INBOX/hi/hi.md)

### Ch 23: Data Science and Analytics in Healthcare

- **P477** · `definition` · data science = conocimiento, organización, testing, entendimiento métodos/procesos científicos asociados datos estructurados/no estructurados; ecosistema incluye datos, computación, programación, estadística/analytics, ML, matemáticas · [src:S01](../../INBOX/hi/hi.md)
- **P478** · `definition` · 5 Vs big data: Volume, Velocity, Variety, Veracity, Value (Eaton 2012) · [src:S01](../../INBOX/hi/hi.md)
- **P479** · `definition` · Volume = cantidad datos pura. Velocity = velocidad generación/cambio datos. Variety = datos múltiples fuentes/formatos simultáneamente · [src:S01](../../INBOX/hi/hi.md)
- **P480** · `definition` · Veracity = precisión/completitud ("verdad") datos. Value = propósitos recolectar/procesar/analizar datos deben llenar necesidad · [src:S01](../../INBOX/hi/hi.md)
- **P481** · `fact` · gastos healthcare US = 17.7% PIB 2019, incremento 4.6% año anterior (CMS 2020) · [src:S01](../../INBOX/hi/hi.md)
- **P482** · `definition` · tres categorías analytics: (1) descriptive = análisis datos retrospectivo; (2) predictive = modelos matemáticos relaciones resultados; (3) prescriptive = modelos determinando acciones alternativas alto valor · [src:S01](../../INBOX/hi/hi.md)
- **P483** · `definition` · EDA incluye estadísticas descriptivas, resúmenes, visualizaciones datos; produce dashboards/reportes decision-makers · [src:S01](../../INBOX/hi/hi.md)
- **P484** · `definition` · tipos problemas predictive analytics: regression (predicción outcome), classification (predicción categoría), clustering (agrupación observaciones similares), association rules · [src:S01](../../INBOX/hi/hi.md)
- **P485** · `definition` · métodos prescriptive analytics: decision trees, modelos colas, programación matemática/optimización, simulación · [src:S01](../../INBOX/hi/hi.md)
- **P486** · `definition` · CRISP-DM = proceso estándar cross-industry data mining; 6 fases: comprensión negocio, comprensión datos, preparación datos, modelado, evaluación, despliegue; naturaleza cíclica/iterativa · [src:S01](../../INBOX/hi/hi.md)
- **P487** · `definition` · ETL = Extract, Transform, Load; proceso database administrators acceder datasets; gramática manipulación datos: select, filter, mutate, arrange, group by, summarize, join · [src:S01](../../INBOX/hi/hi.md)
- **P488** · `definition` · NLP / extracción información = métodos identificando información significativa secuencias texto; pipeline multistep computacionalmente costoso lidiando desambiguación/negación palabras · [src:S01](../../INBOX/hi/hi.md)
- **P489** · `fact` · consideraciones preprocessing datos codificados: distribución, frecuencia, datos missing, sparsity, outliers, identificadores, datos erróneos · [src:S01](../../INBOX/hi/hi.md)
- **P490** · `definition` · métodos ML: decision trees (C4.5, CART), decision rules, artificial neural networks, support vector machines, ensemble methods (random forests, boosting, bagging), Bayesian networks · [src:S01](../../INBOX/hi/hi.md)
- **P491** · `definition` · métricas evaluación modelo regression: MAE, MSE, RMSE. Classification: confusion matrix generando accuracy, sensitivity, specificity, PPV, NPV · [src:S01](../../INBOX/hi/hi.md)
- **P492** · `definition` · ROC curve = gráfico fracción false-positive vs fracción true-positive; AUC = probabilidad caso positivo aleatorio rankeado más alto que negativo aleatorio; AUC=0.5 = azar · [src:S01](../../INBOX/hi/hi.md)
- **P493** · `definition` · k-fold cross-validation = datos divididos k partes (comúnmente k=10); cada fold usado testing mientras restantes entrenan modelo; genera estimación media + desviación estándar error · [src:S01](../../INBOX/hi/hi.md)
- **P494** · `fact` · diagrama Venn habilidades data science Drew Conway: 3 áreas requeridas = hacking/programación computador, matemáticas/estadística, expertise dominio · [src:S01](../../INBOX/hi/hi.md)
- **P495** · `fact` · categorías herramientas analytics: spreadsheets/visualización (Excel, Tableau, Power BI), programas estadísticos (SAS, SPSS, Weka, KNIME), lenguajes programación (R, Python, Matlab, Scala, Julia) · [src:S01](../../INBOX/hi/hi.md)
- **P496** · `definition` · data governance = toma decisiones y autoridad sobre asuntos relacionados datos; incluye estructuras organizacionales, reglas/políticas, derechos decisión, métodos accountability; DGI provee framework 10 componentes · [src:S01](../../INBOX/hi/hi.md)
- **P497** · `fact` · Floridi & Cowls cinco principios core AI ético: beneficencia, no-maleficencia, autonomía, justicia, explicabilidad · [src:S01](../../INBOX/hi/hi.md)
- **P498** · `fact` · HIPAA Privacy Rule protege PHI incluyendo condición salud física/mental, prestación healthcare, provisiones pago, datos demográficos · [src:S01](../../INBOX/hi/hi.md)
- **P499** · `fact` · Buolamwini & Gebru (2018): datasets análisis facial abrumadoramente sujetos piel clara; tasa error mujeres negras hasta 34.7% vs 0.8% hombres blancos clasificación género comercial · [src:S01](../../INBOX/hi/hi.md)

### Ch 24: Safety and Quality Initiatives in Health Informatics

- **P500** · `definition` · calidad cuidado IOM (1990) = grado servicios salud para individuos/poblaciones incrementan probabilidad resultados salud deseados consistentes conocimiento profesional actual · [src:S01](../../INBOX/hi/hi.md)
- **P501** · `definition` · seis aims calidad IOM (Crossing Quality Chasm, 2001): safe, effective, patient-centered, timely, efficient, equitable · [src:S01](../../INBOX/hi/hi.md)
- **P502** · `definition` · seguridad paciente IOM = libertad lesión accidental por cuidado médico/errores; error = falla acción planificada completarse como previsto o uso plan incorrecto · [src:S01](../../INBOX/hi/hi.md)
- **P503** · `definition` · seguridad paciente ICPS/WHO = reducción riesgo daño innecesario asociado healthcare a mínimo aceptable · [src:S01](../../INBOX/hi/hi.md)
- **P504** · `fact` · 2017: 96% facilities acute care usaron EHR certificado, 99% hospitales grandes (>300 camas) tenían HIS efectivo · [src:S01](../../INBOX/hi/hi.md)
- **P505** · `fact` · CDC reporta 72.3% proveedores healthcare office-based usan EHRs/EMRs certificados; ~90% usando algún tipo sistema · [src:S01](../../INBOX/hi/hi.md)
- **P506** · `definition` · framework Donabedian = medir calidad basado tres dominios: estructura (atributos setting), proceso (gerencial/clínico), resultados (resultados estructuras/procesos) · [src:S01](../../INBOX/hi/hi.md)
- **P507** · `definition` · framework PSQRD construye sobre Donabedian; continuo seguridad-calidad = "vector of egregiousness" — eventos calidad (frecuentes, menor inmediatez) un extremo, eventos seguridad paciente (inmediatos, alta causalidad) otro · [src:S01](../../INBOX/hi/hi.md)
- **P508** · `definition` · Singh & Sittig Sociotechnical Model = 8 dimensiones CAS interrelacionadas: infraestructura hardware/software, contenido clínico, HCI, personas, workflow/comunicación, políticas org internas, reglas/regulaciones externas, medición/monitoreo sistema · [src:S01](../../INBOX/hi/hi.md)
- **P509** · `fact` · cinco rights seguridad medicación: paciente correcto, hora correcta, droga correcta, dosis correcta, vía correcta · [src:S01](../../INBOX/hi/hi.md)
- **P510** · `fact` · BCMA/eMAR aprovechan barcoding pulseras paciente/medicamentos asegurar adherencia cinco rights y documentar administración droga tiempo real · [src:S01](../../INBOX/hi/hi.md)
- **P511** · `fact` · adopción smart infusion pump duplicó 2005-2012; encuesta ASHP 2012 mostró 77% tasa adopción IV smart pumps hospitales US · [src:S01](../../INBOX/hi/hi.md)
- **P512** · `fact` · cumplimiento scanning BCMA frecuentemente subóptimo; un estudio encontró cumplimiento solo 55.3% (Franklin 2007); enfermeros bypasean scanning creando workarounds · [src:S01](../../INBOX/hi/hi.md)
- **P513** · `definition` · workarounds = cualquier uso sistema operativo fuera protocolo diseñado; más comunes durante etapa implementación, pueden crear nuevas rutas errores · [src:S01](../../INBOX/hi/hi.md)
- **P514** · `fact` · CMS identificó condiciones adquiridas hospital prevenibles (Deficit Reduction Act 2006) por las cuales hospitales no reciben pago adicional; incluye úlceras presión, caídas paciente con lesión · [src:S01](../../INBOX/hi/hi.md)
- **P515** · `fact` · características implementación HIT exitosa: soporte liderazgo, estrategia implementación/adopción comprehensiva, HIT como "herramienta" dentro intervención multifacética, engagement paciente, participación end-user, soporte peer champion · [src:S01](../../INBOX/hi/hi.md)
- **P516** · `fact` · estándares datos calidad requieren: value sets estándar, taxonomías, concept codes, atributos, estructuras datos. Terminologías clave: SNOMED CT, ICD-10 CM, LOINC, RxNorm, CPT-4, NDF-RT, HL7 · [src:S01](../../INBOX/hi/hi.md)
- **P517** · `definition` · interoperabilidad semántica = datos intercambiados sin pérdida contexto/significado, reutilizables sin esfuerzo especial usuario; requiere todas organizaciones adopten mismos estándares · [src:S01](../../INBOX/hi/hi.md)
- **P518** · `fact` · CMS 2018 renombró EHR Incentive Program a Promoting Interoperability Program · [src:S01](../../INBOX/hi/hi.md)
- **P519** · `fact` · website eCQI coordinado CMS/ONC provee medidas actualizadas, herramientas, recursos para mejora calidad clínica electrónica · [src:S01](../../INBOX/hi/hi.md)

### Ch 25: Informatics in the Curriculum

- **P520** · `fact` · IOM 2003 report listó 5 competencias core todos profesionales salud: patient-centered care, interdisciplinary teams, evidence-based practice, quality improvement, informatics · [src:S01](../../INBOX/hi/hi.md)
- **P521** · `definition` · ANA 2022 definición nursing informatics: especialidad que transforma datos en información necesaria y aprovecha tecnologías mejorar equidad/seguridad/calidad/resultados salud/healthcare · [src:S01](../../INBOX/hi/hi.md)
- **P522** · `fact` · ANA primero reconoció nursing informatics como especialidad 1992; integra nursing science, computer science, information science · [src:S01](../../INBOX/hi/hi.md)
- **P523** · `fact` · AACN 2021 Essentials: 10 dominios; Domain 8 = Informatics and Healthcare Technologies con 4 competencias · [src:S01](../../INBOX/hi/hi.md)
- **P524** · `fact` · competencias informática educación médica Hersh et al. (2014): knowledge-based info cuidado paciente, implementación CDS, gestión salud poblacional, privacidad/seguridad, seguridad paciente vía IT, medición calidad, uso HIE, engagement paciente vía PHR/portales, telemedicina, medicina precisión · [src:S01](../../INBOX/hi/hi.md)
- **P525** · `fact` · fellowship clinical informatics ACGME: 5 milestone levels desde fellow entrante a practitioner avanzado; sub-competencias incluyen seguridad paciente, evaluación tecnología, sistemas CDS, project management · [src:S01](../../INBOX/hi/hi.md)
- **P526** · `fact` · dominios informática farmacéutica AACP (revisión 2019): legal/regulatorio, interoperabilidad/estandarización, resultados paciente, informática healthcare/clínica/biomédica, desarrollo/educación practicante, tecnologías emergentes · [src:S01](../../INBOX/hi/hi.md)
- **P527** · `fact` · EU*US eHealth Work Project 2017 encuesta (>1000 respondientes): 5 brechas principales = falta conocimiento/habilidades proveedores, falta conocimiento/habilidades facultad, disponibilidad cursos, calidad/cantidad materiales training · [src:S01](../../INBOX/hi/hi.md)
- **P528** · `fact` · AACN reporta edad promedio facultad enfermería con doctoral degree: profesor 62.4, asociado 57.2, asistente 51.2 años; mayoría no educada sobre informática durante propia formación · [src:S01](../../INBOX/hi/hi.md)
- **P529** · `fact` · cuerpos acreditación health informatics: CAHIIM (health informatics), LCME (medicina), CCNE/ACEN (enfermería), CAPTE (terapia física), AOTA (terapia ocupacional) · [src:S01](../../INBOX/hi/hi.md)
- **P530** · `fact` · cuerpos certificación: ANCC (nursing informatics), ABMS (medical informatics), CPHIMS/HIMSS (CIOs/profesionales salud), CHIME CHCIO (CIOs/ejecutivos IT) · [src:S01](../../INBOX/hi/hi.md)
- **P531** · `fact` · AMIA estableció Advanced Interprofessional Informatics Certification (AIIC) para profesionales informática no-médicos; también colaboró ABMS/ABP certificación subspecialty board clinical informatics · [src:S01](../../INBOX/hi/hi.md)
- **P532** · `definition` · LHS = loops feedforward/feedback orientados objetivos creando información accionable mejorar salud poblacional y disminuir costo cuidado evidence-based · [src:S01](../../INBOX/hi/hi.md)
- **P533** · `fact` · HITECH Act 2009 promulgada como parte ARRA; proveyó recursos ONC; soporte financiero/técnico CMS impulsar implementación EHR rápida · [src:S01](../../INBOX/hi/hi.md)
- **P534** · `fact` · 21st Century Cures Act (2016): promueve compartición datos vía interoperabilidad expandida, prohíbe bloqueo datos, manda acceso/portabilidad inmediata información salud electrónica personal · [src:S01](../../INBOX/hi/hi.md)
- **P535** · `fact` · primeros EHRs aparecieron 1960s; versión temprana desarrollada Mayo Clinic, Rochester MN; 1965 ~73 proyectos info hospital/clínica y 29 proyectos almacenamiento/recuperación documentos · [src:S01](../../INBOX/hi/hi.md)
- **P536** · `fact` · ONC 2010 estimó déficit 51,000 trabajadores HIT calificados; otorgó $84M a 16 universidades/community colleges entrenar >50,000 nuevos profesionales HIT; 12 roles workforce HIT clave identificados · [src:S01](../../INBOX/hi/hi.md)
- **P537** · `fact` · dominios informática AMIA: translational bioinformatics, clinical informatics, clinical research informatics, consumer health informatics, public health informatics · [src:S01](../../INBOX/hi/hi.md)
- **P538** · `fact` · ciencia informática es inherentemente interprofesional; se nutre computer science, decision science, information science, management science, cognitive science, data science, teoría organizacional · [src:S01](../../INBOX/hi/hi.md)
- **P539** · `definition` · tres categorías teoría pedagogía: behaviorista (cambio comportamiento = "know what"), cognitiva (memoria/motivación/reflexión = "know how"), constructivismo (interpretar/personalizar conocimiento = "know why") · [src:S01](../../INBOX/hi/hi.md)
- **P540** · `fact` · competencia QSEN prelicensure: enfermeros deberían usar información/tecnología comunicar, gestionar conocimiento, mitigar error, soportar toma decisiones en entorno caring/seguro · [src:S01](../../INBOX/hi/hi.md)

### Ch 26: Distance Education — A New Frontier

- **P541** · `definition` · educación distancia = instrucción/aprendizaje planificado donde profesor/aprendiz separados por localización; enseñanza/aprendizaje ocurren varios tiempos; material entregado electrónicamente o impreso · [src:S01](../../INBOX/hi/hi.md)
- **P542** · `definition` · asynchronous learning = aprendiz ve contenido educacional diferente tiempo que presentado. Synchronous = evento educativo y aprendizaje mismo tiempo. Blended = combinación ambos · [src:S01](../../INBOX/hi/hi.md)
- **P543** · `definition` · distributed education = personaliza entorno aprendizaje estilos aprendizaje; métodos delivery más inclusivos; puede incluir distancia, híbrido, on-site · [src:S01](../../INBOX/hi/hi.md)
- **P544** · `definition` · eLearning = training involucrando solo medios electrónicos/tecnologías internet; 3 elementos: asíncrono, diferente localización, dispositivos electrónicos interacción. mLearning = dispositivo móvil como herramienta educativa just-in-time · [src:S01](../../INBOX/hi/hi.md)
- **P545** · `fact` · cuatro fases históricas educación distancia: (1) cursos correspondencia (mid-late 1800s), (2) broadcast media/films/radio/TV (1920s-early 1980s), (3) educación online (mid-late 1980s-1990s), (4) contenido user-generated/Web 2.0 (late 1990s-presente) · [src:S01](../../INBOX/hi/hi.md)
- **P546** · `fact` · Anna Ticknor fundó Boston Society to Encourage Studies at Home (1873) — educación superior mujeres por mujeres. Chautauqua Correspondence College fundada 1881 · [src:S01](../../INBOX/hi/hi.md)
- **P547** · `definition` · CMS/LMS = software permitiendo desarrollo/entrega cursos sin conocimiento programación; LMS más amplio que CMS incluyendo gestión cursos + registración, integración HR, features admin · [src:S01](../../INBOX/hi/hi.md)
- **P548** · `fact` · market share CMS (NYC Design 2021): WordPress 41%, Drupal 19%, OmniUpdate 9.5%, Cascade CMS 7%, Adobe Experience Manager 4% · [src:S01](../../INBOX/hi/hi.md)
- **P549** · `fact` · criterios selección CMS: objetivos/metas, features, integración sistemas institucionales, compatibilidad, base usuarios, customización/mantenimiento, escalabilidad, usabilidad, medidas resultados, cumplimiento SCORM, costo · [src:S01](../../INBOX/hi/hi.md)
- **P550** · `definition` · SCORM = Sharable Content Object Reference Model; incentiva estandarización LMSs · [src:S01](../../INBOX/hi/hi.md)
- **P551** · `definition` · Community of Inquiry Model: tres conceptos = social presence (comunidad aprendizaje supportive), cognitive presence (construir conocimiento reflexión/discusión), teaching presence (diseñar/guiar experiencias aprendizaje) · [src:S01](../../INBOX/hi/hi.md)
- **P552** · `definition` · estilos aprendizaje VARK: Visual (representaciones gráficas), Aural (info escuchada/hablada), Read/Write (palabras todas formas), Kinesthetic (experiencias/hands-on); validado instrumento confiable · [src:S01](../../INBOX/hi/hi.md)
- **P553** · `fact` · DMCA 1998 protege trabajo copyrightable; prohíbe circumvención tecnologías protección, limita responsabilidad proveedor servicio online · [src:S01](../../INBOX/hi/hi.md)
- **P554** · `fact` · TEACH Act 2002 permite performance/display materiales copyrighted educación distancia bajo condiciones: institución acreditada sin fines lucro, solo estudiantes inscritos, live/asíncrono permitido, info copyright provista, acceso time-limited · [src:S01](../../INBOX/hi/hi.md)
- **P555** · `fact` · HEOA 2008: requiere instituciones publicar calculadora precio neto, políticas seguridad/copyright; facultad debe enviar requerimientos libros texto antes registración; instituciones deben verificar identidad estudiante · [src:S01](../../INBOX/hi/hi.md)
- **P556** · `fact` · FERPA requiere colleges/universidades dar estudiantes acceso registros educacionales y mantener confidencialidad registros personally identifiable · [src:S01](../../INBOX/hi/hi.md)
- **P557** · `fact` · Quality Matters = proceso peer review certificar calidad cursos online/blended · [src:S01](../../INBOX/hi/hi.md)
- **P558** · `definition` · adult learners quieren educación aplicable inmediatamente situación específica; se apoyan experiencias previas aprendiendo nuevos conceptos; benefician aprendizaje auto-dirigido · [src:S01](../../INBOX/hi/hi.md)

## Section 6: Data Governance, Legal, and Regulatory Issues

### Ch 27: Legal Issues, Federal Regulations, and Accreditation

- **P559** · `fact` · gobierno federal US tres ramas: legislativa, ejecutiva, judicial; cada una juega rol leyes/regulaciones HIT · [src:S01](../../INBOX/hi/hi.md)
- **P560** · `definition` · poderes expresos = poderes explícitamente otorgados Congreso (e.g., regular comercio interestatal, recaudar impuestos) · [src:S01](../../INBOX/hi/hi.md)
- **P561** · `fact` · Congreso usó poderes expresos/implícitos implementar HIPAA, requerimientos Meaningful Use, PPACA · [src:S01](../../INBOX/hi/hi.md)
- **P562** · `rule` · ley federal preempta ley estatal conflictiva a menos ley estatal provea mayores protecciones (e.g., California CMIA provee más protecciones privacidad que HIPAA) · [src:S01](../../INBOX/hi/hi.md)
- **P563** · `fact` · dos agencias acreditación hospital principales: The Joint Commission (TJC) y Det Norske Veritas (DNV) Healthcare · [src:S01](../../INBOX/hi/hi.md)
- **P564** · `fact` · FDA regula/aprueba drogas y dispositivos médicos; responsable framework regulatorio risk-based para HIT · [src:S01](../../INBOX/hi/hi.md)
- **P565** · `fact` · CMS emite regulaciones Medicare/Medicaid incluyendo Conditions of Participation; enforce leyes Stark/Anti-Kickback · [src:S01](../../INBOX/hi/hi.md)
- **P566** · `fact` · ONC establece programas/regulaciones mejorar seguridad/calidad/eficiencia vía HIT; establece estándares/criterios certificación EHR · [src:S01](../../INBOX/hi/hi.md)
- **P567** · `fact` · Office Civil Rights enforce cumplimiento HIPAA/HITECH · [src:S01](../../INBOX/hi/hi.md)
- **P568** · `fact` · Department Justice enforce False Claims Act y estatutos Anti-Kickback · [src:S01](../../INBOX/hi/hi.md)
- **P569** · `fact` · HITECH Act aprobada 2009; requirió OCR implementar programa auditoría evaluando cumplimiento HIPAA · [src:S01](../../INBOX/hi/hi.md)
- **P570** · `definition` · Stark law (1992) = ley auto-referencia médico para pacientes Medicare/Medicaid; prohíbe referir pacientes designated health services (DHS) a entidades con las que médico tiene relación financiera · [src:S01](../../INBOX/hi/hi.md)
- **P571** · `scope` · DHS bajo Stark incluye: lab clínico, terapia física/ocupacional, speech-language pathology, radiología, terapia radiación, durable medical equipment, suministros parenteral/enteral, prótesis, home health, Rx ambulatorio, servicios hospital in/outpatient · [src:S01](../../INBOX/hi/hi.md)
- **P572** · `rule` · dos relaciones financieras activan Stark: (1) interés ownership/inversión médico/familia en entidad DHS; (2) acuerdo compensación con médico/familia (directo o indirecto) · [src:S01](../../INBOX/hi/hi.md)
- **P573** · `definition` · Federal Anti-Kickback statute = estatuto criminal prohibiendo intercambio/oferta cualquier cosa valor inducir referencia beneficiario programa healthcare federal (42 U.S.C. 1320a-7b) · [src:S01](../../INBOX/hi/hi.md)
- **P574** · `fact` · PPACA clarificó: conocimiento real o intención específica no necesario para condena Anti-Kickback · [src:S01](../../INBOX/hi/hi.md)
- **P575** · `fact` · penalidad Anti-Kickback: violación única hasta $25,000 multa + hasta 5 años prisión + exclusión mandatoria programa healthcare federal; penalties civiles = triple daños + $50,000/violación · [src:S01](../../INBOX/hi/hi.md)
- **P576** · `requirement` · criterios safe harbor Anti-Kickback: acuerdos escritos/firmados >1 año; especifica todos servicios/productos/espacio; especifica intervalos/cargos part-time; pago fijado anticipado fair market value no considerando volumen/valor referrals · [src:S01](../../INBOX/hi/hi.md)
- **P577** · `fact` · EHR donation safe harbor creado 2006; revisado/extendido 2021; donor puede pagar hasta 85% costo comprar/implementar tecnología EHR; EHR debe cumplir criterios certificación actuales · [src:S01](../../INBOX/hi/hi.md)
- **P578** · `rule` · cybersecurity donation safe harbor (2021 final rule): protege donación software cybersecurity + cierto hardware sin requerimiento contribución (donor puede cubrir 100%) · [src:S01](../../INBOX/hi/hi.md)
- **P579** · `definition` · False Claims Act (FCA) = impone responsabilidad civil persona presentando claim gobierno federal conocido/debería-conocerse falso; penalidades = 3x monto claim + $11,000 por claim · [src:S01](../../INBOX/hi/hi.md)
- **P580** · `rule` · bajo PPACA, proveedor recibiendo sobrepago Medicare tiene 60 días reportar/devolver dinero antes enfrentar responsabilidad FCA · [src:S01](../../INBOX/hi/hi.md)
- **P581** · `definition` · Qui Tam suits = ciudadanos privados llevando acciones enforcement FCA; relators pueden recuperar porción juicio/settlement; DOJ revisa todos casos · [src:S01](../../INBOX/hi/hi.md)
- **P582** · `fact` · Healthcare Fraud statute (18 U.S.C. 1347): defraudar knowingly/willfully programa beneficio healthcare → multa/prisión ≤10 años; aplica cualquier pagador (público o privado) · [src:S01](../../INBOX/hi/hi.md)
- **P583** · `fact` · wire fraud: penalidades criminales presentación claims computarizados fraudulentos; cada claim = cuenta separada; hasta $1,000 multa + hasta 5 años prisión por violación · [src:S01](../../INBOX/hi/hi.md)
- **P584** · `fact` · CMS publicó toolkit detección fraude/abuso EHR; recomendaciones clave: features anti-fraude, audit logs operacionales, audit trail mostrando quién modificó registro/cuándo · [src:S01](../../INBOX/hi/hi.md)
- **P585** · `fact` · TJC usa programa survey/audit Standards; DNV usa programa NIAHO integrando ISO 9001 con Medicare Conditions of Participation · [src:S01](../../INBOX/hi/hi.md)
- **P586** · `fact` · TJC Sentinel Event Alert 42 (dic 2008): identificó interfaz humano-máquina + diseño sistema HIT como factores primarios eventos adversos prevenibles · [src:S01](../../INBOX/hi/hi.md)
- **P587** · `fact` · TJC Sentinel Event Alert 54 (mar 2015): analizó >3375 eventos adversos; 3 áreas debilidad mayores: (1) interfaz humano-computador (1/3 eventos), (2) workflow/comunicación, (3) diseño contenido clínico/soporte decisión · [src:S01](../../INBOX/hi/hi.md)
- **P588** · `fact` · clases dispositivos médicos FDA: Class I (bajo riesgo, 47%), Class II (medio, 43%), Class III (alto, 10%) · [src:S01](../../INBOX/hi/hi.md)
- **P589** · `fact` · FDASIA aprobada 2012; Sección 618 requirió FDA+ONC+FCC crear framework regulatorio risk-based para HIT incluyendo mobile medical apps · [src:S01](../../INBOX/hi/hi.md)
- **P590** · `fact` · guidance "General Wellness" FDA (ene 2015): FDA no regulará wearable devices wellness general; test dos partes: (1) solo claims wellness general, (2) sin riesgos seguridad inherentes · [src:S01](../../INBOX/hi/hi.md)
- **P591** · `fact` · Interstate Medical Licensure Compact (IMLC) y Enhanced Nurse Licensure Compact (eNLC) creados preservar regulación estatal facilitando telehealth cross-state · [src:S01](../../INBOX/hi/hi.md)
- **P592** · `fact` · apps mHealth no son covered entities bajo HIPAA → sin prohibición federal recolección/uso/divulgación PHI recolectado por apps · [src:S01](../../INBOX/hi/hi.md)

### Ch 28: Privacy and Security

- **P593** · `definition` · privacidad = derecho individuos controlar acceso persona (body privacy) o información sobre sí mismos (information privacy) · [src:S01](../../INBOX/hi/hi.md)
- **P594** · `definition` · confidencialidad = datos/información no disponibles/divulgados personas/procesos no autorizados · [src:S01](../../INBOX/hi/hi.md)
- **P595** · `definition` · integridad = datos/información no alterados/destruidos manera no autorizada · [src:S01](../../INBOX/hi/hi.md)
- **P596** · `definition` · disponibilidad = datos/información accesibles y utilizables on demand por persona autorizada · [src:S01](../../INBOX/hi/hi.md)
- **P597** · `definition` · seguridad = proteger información/sistemas acceso/uso/divulgación/interrupción/modificación/destrucción no autorizados proveer confidencialidad, integridad, disponibilidad · [src:S01](../../INBOX/hi/hi.md)
- **P598** · `rule` · privacidad concierne persona (derechos paciente); confidencialidad concierne información (responsabilidad proveedor); seguridad concierne salvaguardas administrativas/técnicas/físicas · [src:S01](../../INBOX/hi/hi.md)
- **P599** · `fact` · Fair Information Practice Principles (FIPPs) redactados 1970s; 8 principios reconocidos internacionalmente: transparencia, participación individual, especificación propósito, minimización datos, limitación uso, calidad/integridad datos, seguridad, accountability/auditoría · [src:S01](../../INBOX/hi/hi.md)
- **P600** · `fact` · EU Court Justice Google Spain SL v. AEPD sostuvo derecho ser olvidado en internet = derecho todos miembros EU · [src:S01](../../INBOX/hi/hi.md)
