---
_manifest:
  urn: urn:gn:kb:manual-operacional-dgi
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/dgi/kb_gn_manual_operacional_dgi_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- dgi
- gestion-institucional
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/dgi/kb_gn_manual_operacional_dgi_koda.yml
    source_hashes:
      domains/gn/dgi/kb_gn_manual_operacional_dgi_koda.yml: 79a279016f3a7730f0e7052faf44f20199fee3379b6a80654a95170b4b5bd967
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.28
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 23
    meat_count: 574
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/manuales__manual-operacional-dgi.md.json
---

# Manual Operacional DGI
## ID
MANUAL-OPERACIONAL-DGI-KODA-01

## Version
1.0.0

## Status
Published

## Human Creator
felixsanhueza

## Human Editor
felixsanhueza

## Model Collaborator
KODA-ARCHITECT

## Creation Date
2026-01-29

## Modification Date
2026-01-29

## Source
manual_operacional_dgi.md

## Ctx
Manual Operacional del Departamento de Gestión Institucional GORE Ñuble

## XRef Required
urn:knowledge:koda:core:spec:1.0.0

## LLM Parsing Instructions
### ID
KODA-LLM-PARSER-01
### Req
Mandatory block following Metadata.
### Prohib
Using for artifact creation or translation.
### Content
BEGIN_LLM_INSTRUCTIONS
You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).

LEXICON (expand before processing): Act->Action, Cond->Condition, Ctx->Context, Ctx_Required->Required External Reference, Ctx_Optional->Optional External Reference, Def->Definition, Ex->Example, Mssn->Mission, Obj->Objective, Proc->Process, Purp->Purpose, Ref->Reference, XRef->Cross-Artifact Reference, XRef_Required->Mandatory Cross-Artifact Reference, Req->Requirement, Res->Result, Src->Source, Prohib->Prohibition, Warn->Warning, Just->Justification, Rec->Recommendation

REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. XRef/XRef_Required: are external only—must point to a URN (optionally with #ID fragment) in another artifact. External documents without specific ID use Ctx:, Ctx_Required:, or Ctx_Optional:.

LANGUAGE POLICY: Keywords in English, content in original language. Never translate content.
END_LLM_INSTRUCTIONS


## Scope
### Includes
- Marco institucional y normativo del DGI
- Estructura organizacional y roles
- Procesos operativos de las 4 áreas
- Protocolos de coordinación institucional
### Excludes
- Plantillas vacías
- Anexos de formularios

## Metrics
### Source Chars
42255
### Artifact Chars
28000
### CR
1.51
### FS
100%

## GeneralProvisions
-
  #### ID
  DGI-GEN-01
  #### Title
  Objeto del Manual
  #### Text
  Establece el marco operativo del DGI del GORE Ñuble, definiendo estructura, funciones, procesos y mecanismos de coordinación institucional.
-
  #### ID
  DGI-GEN-02
  #### Title
  Alcance
  #### Text
  Aplicable a todo el personal del DGI y a las interacciones con divisiones, unidades y actores externos relacionados con sus funciones.
-
  #### ID
  DGI-GEN-03
  #### Title
  Definiciones Operacionales
  #### Definitions
  | Term | Def |
  | --- | --- |
  | DGI | Departamento de Gestión Institucional |
  | AR | Administración Regional |
  | TD | Transformación Digital |
  | TDE | Transformación Digital del Estado (Ley 21.180) |
  | KB | Knowledge Base / Base de Conocimiento |
  | BPMN | Business Process Model and Notation |
  | KPI | Key Performance Indicator |
  | GORE | Gobierno Regional |
  | ERD | Estrategia Regional de Desarrollo |
-
  #### ID
  DGI-GEN-04
  #### Title
  Marco Normativo
  #### Sources
  -
    #### Ley 19.175
    Orgánica Constitucional sobre Gobierno y Administración Regional
  -
    #### Ley 21.180
    Transformación Digital del Estado
  -
    #### DS 14/2014
    Modelo de Gestión de Procesos
  -
    #### Resolución 22/2023
    Normas Técnicas de Interoperabilidad
  -
    #### PMG
    Programa de Mejoramiento de la Gestión
-
  #### ID
  DGI-GEN-05
  #### Title
  Principios Rectores
  #### Principles
  | ID | Name | Desc |
  | --- | --- | --- |
  | PR-01 | Orientación al servicio | Foco en necesidades de usuarios internos y finales |
  | PR-02 | Basado en datos | Decisiones sustentadas en información verificable |
  | PR-03 | Mejora continua | Optimización sistemática de procesos |
  | PR-04 | Colaboración | Trabajo conjunto con todas las divisiones |
  | PR-05 | Transparencia | Información accesible y trazable |
  | PR-06 | Innovación | Adopción de mejores prácticas y tecnologías |

## OrganizationalStructure
-
  #### ID
  DGI-ORG-01
  #### Title
  Misión DGI
  #### Text
  Facilitar la gestión efectiva del GORE Ñuble mediante control de gestión,
modernización de procesos, transformación digital y gestión del conocimiento,
apoyando la toma de decisiones de la Administración Regional y la mejora
continua de los servicios a la ciudadanía.
-
  #### ID
  DGI-ORG-02
  #### Title
  Visión DGI
  #### Text
  Ser reconocido como referente de gestión institucional en los Gobiernos
Regionales de Chile, destacando por la calidad de su asesoría, innovación
metodológica y uso efectivo de tecnologías para la gestión pública.
-
  #### ID
  DGI-ORG-03
  #### Title
  Áreas Funcionales
  #### Domains
  | ID | Name | Description |
  | --- | --- | --- |
  | DOM-CG | Control de Gestión | Monitoreo de indicadores, dashboards, alertas, informes ejecutivos |
  | DOM-MP | Modernización de Procesos | Levantamiento BPMN, análisis de mejora, diseño de automatizaciones |
  | DOM-TD | Transformación Digital | Cumplimiento TDE, Comité TD, administración funcional de sistemas |
  | DOM-KC | Gestión del Conocimiento | Curación KB, administración agentes IA, capacitación y gestión del cambio |
-
  #### ID
  DGI-ORG-04
  #### Title
  Perfiles de Cargo
  #### Roles
  #### JefeDGI
  #### Name
  Jefe(a) Departamento de Gestión Institucional
  #### Dependencia
  Administración Regional
  #### Functions
  - Dirigir y coordinar el equipo DGI
  - Asesorar a AR en materias de gestión institucional
  - Representar al DGI en instancias colegiadas
  - Gestionar recursos del departamento
  - Reportar estado de iniciativas a AR
  #### EspecialistaProcesos
  #### Name
  Especialista en Modernización de Procesos
  #### Dependencia
  Jefe DGI
  #### Functions
  - Levantar y modelar procesos BPMN
  - Identificar oportunidades de mejora
  - Diseñar automatizaciones
  - Acompañar implementación de cambios
  - Documentar procedimientos optimizados
  #### EspecialistaTD
  #### Name
  Especialista en Transformación Digital
  #### Dependencia
  Jefe DGI
  #### Functions
  - Monitorear cumplimiento TDE
  - Gestionar secretaría técnica Comité TD
  - Curar y mantener base de conocimiento
  - Administrar agentes IA institucionales
  - Facilitar interoperabilidad de sistemas
  #### EspecialistaControl
  #### Name
  Especialista en Control de Gestión
  #### Dependencia
  Jefe DGI
  #### Functions
  - Definir y monitorear indicadores
  - Elaborar y mantener dashboards
  - Detectar y analizar desviaciones
  - Generar informes ejecutivos
  - Proponer acciones correctivas
-
  #### ID
  DGI-ORG-05
  #### Title
  Matriz RACI
  #### RACI
  | Activity | Jefe | Procesos | TD | Control | Division | AR |
  | --- | --- | --- | --- | --- | --- | --- |
  | Diseñar indicadores | C | I | I | R | C | A |
  | Levantar procesos | C | R | I | I | C | I |
  | Gestionar KB | C | I | R | I | I | I |
  | Administrar dashboards | C | I | I | R | I | I |
  | Reportar a AR | R | C | C | C | I | A |
  | Coordinar con divisiones | R | C | C | C | C | A |
  #### Legend
  R=Responsable, A=Aprueba, C=Consultado, I=Informado

## ControlGestion
-
  #### ID
  DGI-CG-01
  #### Title
  Monitoreo de Indicadores Institucionales
  #### Obj
  Mantener visibilidad permanente sobre el estado de gestión del GORE
  #### Process
  | Step | Actions |
  | --- | --- |
  | Definición de indicadores | ['Identificar objetivos estratégicos (ERD, Ñuble 250)', 'Definir indicadores SMART para cada objetivo', 'Establecer metas y umbrales de alerta', 'Documentar ficha de cada indicador'] |
  | Recolección de datos | ['Identificar fuentes de datos por indicador', 'Establecer frecuencia de actualización', 'Definir responsable de provisión de datos', 'Validar calidad de datos recibidos'] |
  | Cálculo y análisis | ['Aplicar fórmulas definidas', 'Comparar con metas y períodos anteriores', 'Identificar tendencias y desviaciones', 'Documentar hallazgos'] |
  | Comunicación | ['Actualizar dashboard', 'Generar alertas si corresponde', 'Informar a responsables'] |
-
  #### ID
  DGI-CG-02
  #### Title
  Tipos de Dashboard
  #### Dashboards
  | Type | Audience | Content | Frequency |
  | --- | --- | --- | --- |
  | Ejecutivo | AR, Gobernador | KPIs agregados, alertas críticas | Actualización diaria |
  | División | Jefe División | Indicadores de la división | Semanal |
  | Operativo | Equipos | Detalle de tareas y estados | Diario |
  | Temático | Comités | Foco específico (IPR, TD, etc.) | Según comité |
-
  #### ID
  DGI-CG-03
  #### Title
  Detección de Cuellos de Botella
  #### Obj
  Identificar proactivamente puntos de fricción en la operación
  #### AlertSignals
  - Indicadores bajo umbral por más de 2 períodos
  - Acumulación de trabajo pendiente
  - Incremento en tiempos de ciclo
  - Reclamos o consultas recurrentes sobre mismo tema
  - Desviaciones presupuestarias significativas
  #### InvestigationProcess
  - Detección: Sistema de alertas o reporte de división
  - Verificación: Confirmar que el problema es real y significativo
  - Análisis: Identificar causa raíz (5 porqués, Ishikawa)
  - Propuesta: Formular recomendación de solución
  - Comunicación: Informar a responsable y AR
  - Seguimiento: Verificar implementación y efectividad
-
  #### ID
  DGI-CG-04
  #### Title
  Estructura Informe Estado Situacional
  #### Sections
  - 1. RESUMEN EJECUTIVO: Estado general (semáforo), principales logros, alertas activas
  - 2. INDICADORES CLAVE: Tabla resumen con tendencia, gráficos de evolución
  - 3. ALERTAS Y RIESGOS: Problemas detectados, acciones en curso, riesgos emergentes
  - 4. AVANCE DE INICIATIVAS: Estado de proyectos DGI, hitos cumplidos/pendientes
  - 5. RECOMENDACIONES: Decisiones requeridas, acciones sugeridas
  - 6. PRÓXIMO PERÍODO: Prioridades, hitos esperados
  #### Frequency
  Semanal (resumen) / Mensual (completo)

## ModernizacionProcesos
-
  #### ID
  DGI-MP-01
  #### Title
  Levantamiento y Modelado BPMN
  #### Obj
  Documentar los procesos institucionales de manera estandarizada
  #### Phases
  #### Preparacion
  - Identificar proceso a levantar
  - Definir alcance (inicio, fin, actores)
  - Programar sesiones con participantes
  - Preparar materiales
  #### Recoleccion
  - Realizar entrevistas con ejecutores
  - Observar proceso en terreno si es posible
  - Revisar documentación existente
  - Identificar variantes y excepciones
  #### Modelado
  - Crear diagrama BPMN del proceso AS-IS
  - Identificar roles y sistemas involucrados
  - Documentar reglas de negocio
  - Validar con participantes
  #### Documentacion
  - Completar ficha de proceso
  - Registrar métricas actuales (tiempos, volúmenes)
  - Identificar puntos de dolor
  - Almacenar en repositorio institucional
  #### MinBPMNElements
  - Eventos de inicio y fin
  - Actividades con responsable
  - Flujos de secuencia
  - Compuertas de decisión
  - Pools/lanes por actor
  - Anotaciones explicativas
-
  #### ID
  DGI-MP-02
  #### Title
  Análisis de Oportunidades de Mejora
  #### Obj
  Identificar y priorizar mejoras a los procesos levantados
  #### AnalysisDimensions
  | Dimension | Question |
  | --- | --- |
  | Valor | ¿Cada actividad agrega valor al resultado? |
  | Duplicación | ¿Hay actividades redundantes? |
  | Esperas | ¿Dónde se acumula trabajo sin procesar? |
  | Movimientos | ¿Hay traslados innecesarios de información? |
  | Errores | ¿Dónde ocurren más errores o reprocesos? |
  | Automatización | ¿Qué actividades son repetitivas y basadas en reglas? |
  #### PrioritizationProcess
  - Listar todas las oportunidades identificadas
  - Evaluar cada una por: Impacto (alto/medio/bajo), Esfuerzo (alto/medio/bajo), Urgencia
  - Priorizar: Alto impacto + Bajo esfuerzo primero
  - Validar priorización con División responsable
  - Incorporar al plan de trabajo
-
  #### ID
  DGI-MP-03
  #### Title
  Tipos de Automatización
  #### Types
  | Type | Desc | Ex |
  | --- | --- | --- |
  | RPA | Automatización de tareas repetitivas | Carga de datos entre sistemas |
  | Flujos de trabajo | Orquestación de aprobaciones | Circuito de visación |
  | Notificaciones | Alertas automáticas | Vencimiento de convenio |
  | Reportes | Generación programada | Informe semanal |
  | Integraciones | Conexión entre sistemas | SIGFE - Dashboard |
-
  #### ID
  DGI-MP-04
  #### Title
  Proceso de Implementación
  #### Phases
  | Phase | Actions |
  | --- | --- |
  | Preparación | ['Confirmar recursos disponibles', 'Comunicar cambio a afectados', 'Preparar materiales de capacitación', 'Configurar ambiente'] |
  | Piloto | ['Implementar en alcance reducido', 'Monitorear intensivamente', 'Recoger feedback', 'Ajustar si es necesario'] |
  | Despliegue | ['Extender a alcance completo', 'Capacitar usuarios', 'Documentar procedimiento actualizado', 'Comunicar nuevo proceso'] |
  | Estabilización | ['Monitorear indicadores', 'Atender incidentes', 'Refinar configuración', 'Cerrar proyecto formal'] |
  | Mejora continua | ['Medir resultados vs. línea base', 'Identificar nuevas oportunidades', 'Documentar lecciones aprendidas'] |

## TransformacionDigital
-
  #### ID
  DGI-TD-01
  #### Title
  Coordinación Cumplimiento Ley 21.180
  #### Obj
  Asegurar que el GORE avance hacia el cumplimiento de la TDE
  #### Responsibilities
  #### Monitoreo
  - Mantener inventario de procesos y su nivel de digitalización
  - Identificar brechas respecto a requisitos TDE
  - Reportar estado al Comité de TD
  #### Planificacion
  - Proponer roadmap de cumplimiento
  - Priorizar procesos a digitalizar
  - Estimar recursos requeridos
  #### Facilitacion
  - Apoyar a divisiones en digitalización de sus procesos
  - Coordinar con Unidad de Operaciones aspectos técnicos
  - Gestionar dependencias entre iniciativas
  #### Verificacion
  - Validar que implementaciones cumplan normas técnicas
  - Documentar evidencia de cumplimiento
  - Preparar información para auditorías
  #### ComplianceChecklist
  - Procedimiento documentado
  - Firma electrónica implementada
  - Notificaciones electrónicas habilitadas
  - Expediente electrónico configurado
  - Interoperabilidad especificada
  - Autenticación con ClaveÚnica (si aplica)
-
  #### ID
  DGI-TD-02
  #### Title
  Gestión del Comité de TD
  #### Obj
  Proveer soporte técnico al Comité de TD institucional
  #### Functions
  #### SecretariaTecnica
  - Preparar tabla y materiales para sesiones
  - Elaborar actas
  - Dar seguimiento a acuerdos
  #### AnalisisPropuestas
  - Presentar estado de avance TDE
  - Proponer iniciativas para decisión
  - Evaluar factibilidad de solicitudes
  #### Coordinacion
  - Articular a las divisiones en temas transversales
  - Gestionar dependencias entre proyectos
  - Escalar impedimentos
  #### Frequency
  Mínimo mensual, o con mayor frecuencia según agenda
-
  #### ID
  DGI-TD-03
  #### Title
  Administración Funcional de Sistemas
  #### Obj
  Asegurar que los sistemas de gestión de trabajo operen correctamente
  #### ResponsibilityMatrix
  | Function | DGI | TI |
  | --- | --- | --- |
  | Definir requisitos funcionales | R | C |
  | Configurar reglas de negocio | R | I |
  | Definir perfiles y roles | R | C |
  | Habilitar cuentas y accesos | I | R |
  | Mantener infraestructura/seguridad | I | R |
  | Resolver incidentes de negocio | R | I |
  | Resolver incidentes técnicos | C | R |
  | Evolucionar plataforma | R | C |
-
  #### ID
  DGI-TD-04
  #### Title
  Interoperabilidad y Datos
  #### Obj
  Avanzar hacia un ecosistema de datos integrado
  #### Principles
  - Datos como activo: Los datos institucionales son un activo estratégico
  - Fuente única de verdad: Cada dato tiene una fuente autoritativa definida
  - Interoperabilidad por diseño: Los sistemas deben poder intercambiar datos
  #### DataManagementProcess
  #### Inventario
  - Identificar conjuntos de datos críticos
  - Documentar ubicación y formato
  - Identificar dueño de datos
  #### Calidad
  - Definir estándares de calidad por conjunto
  - Monitorear cumplimiento
  - Gestionar correcciones
  #### Integracion
  - Especificar necesidades de intercambio
  - Diseñar interfaces (APIs, archivos)
  - Implementar y monitorear

## GestionConocimiento
-
  #### ID
  DGI-KC-01
  #### Title
  Curación y Actualización de KB
  #### Obj
  Mantener la base de conocimiento institucional actualizada y útil
  #### CurationProcess
  | Phase | Actions |
  | --- | --- |
  | Identificación | ['Detectar conocimiento nuevo o actualizado', 'Evaluar relevancia institucional', 'Priorizar incorporación'] |
  | Estructuración | ['Formatear según estándares KODA', 'Asignar metadatos (URN, categorías)', 'Vincular con artefactos relacionados'] |
  | Validación | ['Verificar exactitud del contenido', 'Validar con expertos de dominio', 'Aprobar publicación'] |
  | Publicación | ['Incorporar al catálogo', 'Actualizar índices y referencias', 'Comunicar disponibilidad'] |
  | Mantenimiento | ['Revisar vigencia periódicamente', 'Actualizar cuando hay cambios normativos', 'Deprecar contenido obsoleto'] |
  #### PrioritizationCriteria
  - Frecuencia de consulta esperada
  - Criticidad para operación
  - Riesgo de información desactualizada
  - Demanda explícita de usuarios
-
  #### ID
  DGI-KC-02
  #### Title
  Administración de Agentes IA
  #### Obj
  Gestionar el ciclo de vida de los agentes de IA institucionales
  #### Lifecycle
  #### Diseno
  - Definir propósito y alcance del agente
  - Especificar fuentes de conocimiento
  - Diseñar flujos de interacción
  - Establecer límites de actuación
  #### Desarrollo
  - Configurar agente según especificación
  - Entrenar con conocimiento relevante
  - Probar funcionamiento
  #### Despliegue
  - Habilitar acceso a usuarios
  - Capacitar en uso
  - Monitorear adopción
  #### Operacion
  - Monitorear interacciones
  - Detectar respuestas inadecuadas
  - Refinar entrenamiento
  - Actualizar conocimiento
  #### Evolucion
  - Evaluar efectividad
  - Identificar mejoras
  - Implementar versiones mejoradas
  #### AIGovernance
  - Todo agente debe tener un dueño funcional
  - Las respuestas deben ser auditables
  - El conocimiento base debe estar documentado
  - Los usuarios deben saber que interactúan con IA
-
  #### ID
  DGI-KC-03
  #### Title
  Capacitación y Gestión del Cambio
  #### Obj
  Facilitar la adopción de nuevas prácticas y herramientas
  #### Principles
  - Cambio centrado en personas: La tecnología es medio, no fin
  - Comunicación permanente: Informar el porqué antes del qué
  - Participación: Involucrar a afectados en diseño de soluciones
  - Gradualidad: Cambios incrementales sobre revoluciones
  #### ChangeManagementProcess
  | Phase | Actions |
  | --- | --- |
  | Preparación | ['Identificar stakeholders', 'Evaluar impacto del cambio', 'Diseñar estrategia de comunicación', 'Identificar resistencias potenciales'] |
  | Comunicación | ['Explicar el porqué del cambio', 'Mostrar beneficios concretos', 'Responder dudas y preocupaciones', 'Mantener comunicación constante'] |
  | Capacitación | ['Diseñar programa según audiencia', 'Ejecutar capacitaciones prácticas', 'Proveer materiales de apoyo', 'Evaluar aprendizaje'] |
  | Acompañamiento | ['Proveer soporte durante transición', 'Resolver problemas emergentes', 'Celebrar éxitos tempranos', 'Ajustar según feedback'] |
  | Consolidación | ['Verificar adopción', 'Reforzar nuevas prácticas', 'Documentar lecciones aprendidas'] |

## EnablementFunctions
| ID | Title | Purpose | KeyConcepts |
| --- | --- | --- | --- |
| DGI-EF-01 | Gestión Arquitectural | Diseñar estructura organizacional saludable (Meyer) | ['Golden Rule: Autoridad = Responsabilidad', 'Dominios Precisos: Sin superposiciones', 'Sinergias: Agrupación de especialistas'] |
| DGI-EF-02 | Dinámica de Producción | Gestionar flujo de trabajo (Lean/Kanban) | ['Visualización de flujo (Tableros)', 'Límites WIP', 'Métricas: Throughput, Lead Time'] |
| DGI-EF-03 | Navegación Social | Gestión del cambio y relaciones (ADKAR) | ['Lobbista Interno: Facilitar, no imponer', 'Modelo ADKAR: Awareness, Desire, Knowledge, Ability, Reinforcement', 'Influencia Ética: Reciprocidad, prueba social'] |

## CoordinacionInstitucional
-
  #### ID
  DGI-CI-01
  #### Title
  Relación con Administración Regional
  #### Canal
  Reunión semanal de coordinación
  #### Content
  - Estado de iniciativas DGI
  - Alertas y escalamientos
  - Decisiones requeridas
  - Prioridades para próximo período
  #### Escalamiento
  Temas que requieren decisión de AR se escalan mediante Informe Ejecutivo con opciones y recomendación
-
  #### ID
  DGI-CI-02
  #### Title
  Matriz de Interacción con Divisiones
  #### Interactions
  | Division | InteractionType | Frequency |
  | --- | --- | --- |
  | Gabinete | Agenda estratégica, comunicación política | Según necesidad |
  | DAF | Indicadores presupuestarios, rendiciones | Semanal |
  | DIPIR | Cartera IPR, estados de avance | Semanal |
  | Jurídica | Convenios, resoluciones, cumplimiento | Quincenal |
  | DIPLADE | Indicadores ERD, planificación | Mensual |
  | Unidad Operaciones | Sistemas, interoperabilidad, infraestructura | Mensual (Mesa Técnica) |
  | Auditoría Interna | Cumplimiento, control interno | Trimestral |
-
  #### ID
  DGI-CI-03
  #### Title
  Protocolo de Escalamiento
  #### Levels
  | Level | Situation | EscalateTo | Deadline |
  | --- | --- | --- | --- |
  | 1 | Incidente operativo | Jefe DGI | 4 horas |
  | 2 | Bloqueo de proyecto | Administración Regional | 24 horas |
  | 3 | Conflicto entre divisiones | Administración Regional | 48 horas |
  | 4 | Decisión estratégica | Gobernador (vía AR) | Según urgencia |
  #### RequiredInfo
  - Descripción del problema
  - Impacto si no se resuelve
  - Opciones de solución
  - Recomendación
  - Plazo requerido para decisión
  - Firma responsable del escalamiento
-
  #### ID
  DGI-CI-04
  #### Title
  Participación en Comités
  #### Committees
  | Name | Role | Frequency |
  | --- | --- | --- |
  | Comité de Transformación Digital | Secretaría técnica | Mensual |
  | Comité de Coordinación Regional | Informante | Según convocatoria |
  | Mesas de trabajo temáticas | Facilitador técnico | Según necesidad |
