---
_manifest:
  urn: urn:gn:kb:plan-potenciamiento-dgi
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/dgi/kb_gn_plan_potenciamiento_dgi_koda.yml; core/gestion/kb_gn_lean6_core_koda.yml;
      core/gestion/kb_gn_meyer_org_structure_koda.yml
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- dgi
- dmaic
- gestion-cambio
- meyer
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/dgi/kb_gn_plan_potenciamiento_dgi_koda.yml
    - core/gestion/kb_gn_lean6_core_koda.yml
    - core/gestion/kb_gn_meyer_org_structure_koda.yml
    source_hashes:
      domains/gn/dgi/kb_gn_plan_potenciamiento_dgi_koda.yml: d2c4322fdf40eb020556b0352b85ec2503bf02fb23ae0a6a952a3c9f6692690a
      core/gestion/kb_gn_lean6_core_koda.yml: f6f48ca09c86336ca3b66c0e3bd58dfd4ccb26249407a7ee6dd58cf8d2a277f8
      core/gestion/kb_gn_meyer_org_structure_koda.yml: 1ece75045862071173bac3b13b9670c91fd120db27235b046a408ca14783a02b
    source_type: mixed
    transformation_mode: korafy_composite
    fs: 100
    cr: 26.45
    run_id: gn-smoke
    review_gate: auto
    scope_statement: Plan DGI con dependencias core declaradas.
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 56
    meat_count: 1244
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/gobernanza__plan-potenciamiento-dgi.md.json
---

# Plan de Potenciamiento DGI

## Alcance
Plan DGI con dependencias core declaradas.

## Fuente principal
- `domains/gn/dgi/kb_gn_plan_potenciamiento_dgi_koda.yml`
## Source
implementation_plan.md

## XRef Required
- KODA Core Spec 1.0.0
- urn:mgmt:kb:meyer-org-structure
- urn:mgmt:kb:lean6

## Scope
### Includes
- Síntesis de perspectivas Meyer y Lean Six Sigma
- Modelo de integración estructural y metodológico
- Navegación social y gestión del cambio
- Modelos cognitivos para AR Virtual
### Excludes
- Plantillas vacías para proyectos específicos

## Metrics
### Source Chars
24568
### Artifact Chars
18500
### CR
1.33
### FS
100%

## PerspectiveSynthesis
-
  #### ID
  POT-SYN-01
  #### Title
  Perspectiva Meyer: Estructura como Ciencia
  #### XRef
  urn:mgmt:kb:meyer-org-structure
  #### Principles
  | ID | Name | Application |
  | --- | --- | --- |
  | MEYER-P1 | Regla de Oro | Autoridad y responsabilidad deben coincidir. El DGI asesora pero NO decide por las divisiones. |
  | MEYER-P2 | Especialización + Trabajo en Equipo | Cada rol del DGI debe ser experto de clase mundial en su dominio, colaborando con pares especializados. |
  | MEYER-P3 | Dominios Precisos | Límites claros entre Control de Gestión, Procesos y TD sin superposiciones ni brechas. |
  | MEYER-P4 | Base para Subestructura | Subdividir por especialidad técnica (qué producen), no por cliente o proceso interno. |
  | MEYER-P5 | Evitar Conflictos de Interés | No mezclar funciones de auditoría con servicios; no mezclar estabilidad con innovación. |
  | MEYER-P6 | Agrupar por Sinergias Profesionales | Mantener especialistas similares juntos para intercambio profesional y economías de escala. |
  | MEYER-P7 | Negocio Dentro del Negocio | Cada rol del DGI es un 'emprendedor interno' que vende productos/servicios a clientes internos. |
-
  #### ID
  POT-SYN-02
  #### Title
  Perspectiva Lean Six Sigma: Mejora Sistemática
  #### XRef
  urn:mgmt:kb:lean6
  #### Concepts
  | ID | Name | Application |
  | --- | --- | --- |
  | LEAN-C1 | 5S | Organización visual del conocimiento institucional y flujos de trabajo. |
  | LEAN-C2 | DMAIC | Ciclo sistemático para proyectos de mejora: Definir → Medir → Analizar → Mejorar → Controlar. |
  | LEAN-C3 | Eliminación de Desperdicios | Identificar y reducir actividades que no agregan valor en procesos del GORE. |
  | LEAN-C4 | Control Estadístico | Uso de datos para detectar desviaciones antes de que escalen. |
  | LEAN-C5 | Kaizen | Cultura de mejora continua pequeña y constante vs. grandes revoluciones. |

## IntegrationArchitecture
-
  #### ID
  POT-ARQ-01
  #### Title
  Arquitectura de Building Blocks (Meyer)
  #### Description
  Organización del DGI según los principios de especialización y dominios precisos,
donde cada rol opera como un 'negocio dentro del negocio'.
  #### BuildingBlocks
  | Block | Roles | Products |
  | --- | --- | --- |
  | Engineers (Base) | ['Especialista Procesos', 'Especialista TD'] | ['Modelos BPMN, diseños de automatización, especificaciones técnicas', 'Configuraciones KB, agentes IA, arquitecturas de integración'] |
  | Service Providers (Asset-based) | ['Especialista Control'] | ['Dashboards, informes periódicos, alertas operativas'] |
  | Coordinators | ['Jefe DGI'] | ['Planificación estratégica, facilitación de consensos, gestión de prioridades'] |
  | Sales & Marketing (Internal) | ['Navegador Institucional'] | ['Mapeo stakeholders, estrategia de influencia, acompañamiento en transiciones'] |
-
  #### ID
  POT-ARQ-02
  #### Title
  Catálogo de Productos DGI
  #### Catalog
  #### EngineersProcesos
  - Modelo BPMN proceso AS-IS
  - Diseño proceso TO-BE
  - Especificación de automatización
  - Análisis de causa raíz
  #### EngineersTD
  - Artefacto conocimiento estructurado
  - Agente IA configurado
  - Integración entre sistemas
  - Capacitación técnica
  #### ServiceProvidersControl
  - Dashboard ejecutivo (diario)
  - Informe estado situacional (semanal)
  - Alerta de desviación (continuo)
  - Métrica calculada y verificada
  #### CoordinatorsJefatura
  - Plan de trabajo consensuado
  - Priorización de iniciativas
  - Resolución de conflictos
  - Comunicación con AR
-
  #### ID
  POT-ARQ-03
  #### Title
  Relaciones Cliente-Proveedor
  #### Paradigm
  Business Within a Business
  #### InternalClients
  - Administración Regional: estrategia, prioridades
  - Divisiones: mejoras operativas, cumplimiento TDE
  - Comité TD: secretaría técnica
  #### InteractionModel
  - Catálogo de servicios publicado
  - Solicitudes canalizadas formalmente
  - SLAs definidos por tipo de producto
  - Feedback estructurado post-entrega
  #### KeyPrinciple
  El DGI PROPONE y FACILITA; las divisiones DECIDEN y EJECUTAN.
Autoridad para decidir = Responsabilidad por resultados.

## DMAICFramework
-
  #### ID
  POT-DMAIC-01
  #### Title
  Marco Operativo DMAIC para DGI
  #### Description
  Cada proyecto de mejora del DGI sigue el ciclo DMAIC
  #### Phases
  #### Define
  - Identificar problema/oportunidad
  - Establecer alcance y objetivos SMART
  - Definir stakeholders y sponsor
  - Documentar caso de negocio
  #### Measure
  - Establecer línea base con métricas actuales
  - Recopilar datos del proceso AS-IS
  - Validar sistema de medición
  - Crear Value Stream Map si aplica
  #### Analyze
  - Análisis de causa raíz (5 Porqués, Ishikawa)
  - Identificar cuellos de botella
  - Cuantificar oportunidades de mejora
  - Priorizar causas según impacto
  #### Improve
  - Diseñar solución TO-BE
  - Prototipar y pilotear
  - Implementar cambios
  - Capacitar usuarios
  #### Control
  - Establecer controles estadísticos
  - Documentar nuevo estándar
  - Crear alertas automáticas
  - Transferir a operación normal
-
  #### ID
  POT-DMAIC-02
  #### Title
  Sistema 5S para Gestión del Conocimiento
  #### Application
  Aplicar 5S japonés al ecosistema de conocimiento institucional
  #### S5Mapping
  | S | Application |
  | --- | --- |
  | Seiri (Clasificar) | Auditar artefactos, deprecar obsoletos, categorizar por utilidad |
  | Seiton (Ordenar) | URNs consistentes, catálogo maestro, taxonomía clara |
  | Seiso (Limpiar) | Revisión periódica de vigencia, corrección de errores |
  | Seiketsu (Estandarizar) | Plantillas KODA, procesos de curación, naming conventions |
  | Shitsuke (Disciplina) | Cultura de actualización, governance de KB, capacitación continua |
-
  #### ID
  POT-DMAIC-03
  #### Title
  Proyecto Piloto DMAIC Sugerido
  #### Candidate
  Flujo de Visación de Actos Administrativos
  #### Phases
  #### Define
  #### Output
  Charter del proyecto con objetivo de reducir tiempo de visación en 30%
  #### Measure
  #### Output
  VSM actual, tiempos de ciclo por etapa, volumen mensual
  #### Analyze
  #### Output
  Identificación de esperas, reprocesos, cuellos de botella
  #### Improve
  #### Output
  Automatización de notificaciones, checklist digital, flujo en paralelo
  #### Control
  #### Output
  Dashboard de seguimiento, alertas de SLA, revisión mensual
-
  #### ID
  POT-DMAIC-04
  #### Title
  Tablero Kanban para Gestión de Iniciativas
  #### Columns
  - BACKLOG
  - EN DISEÑO (DMAIC D-M-A)
  - EN IMPLEMENTACIÓN (DMAIC I)
  - EN VERIFICACIÓN (DMAIC C)
  - COMPLETADO
  #### WIPLimits
  #### Diseño
  2
  #### Implementación
  3
  #### Verificación
  2

## SocialNavigation
-
  #### ID
  POT-SOC-01
  #### Title
  El Rol del Navegador Institucional
  #### BuildingBlock
  Sales & Marketing (Internal)
  #### AlternateName
  Gestor de Relaciones y Cambio
  #### Definition
  Profesional que cultiva relaciones estratégicas con stakeholders clave,
facilita la adopción de cambios, y "vende" internamente el valor del DGI
sin imponer ni auditar.
  #### GuidingPrinciple
  "No vendemos productos; ayudamos a las divisiones a descubrir cómo 
nuestros servicios pueden resolver sus dolores operativos."
  #### Products
  - Mapeo de stakeholders actualizado
  - Diagnóstico de clima organizacional por división
  - Estrategia de influencia por iniciativa
  - Acompañamiento en transiciones
  - Comunicación de éxitos y valor generado
  - Feedback estructurado desde divisiones
-
  #### ID
  POT-SOC-02
  #### Title
  Mapa de Stakeholders GORE
  #### Levels
  #### Estrategico
  | Actor | Power | DGIInterest | Strategy |
  | --- | --- | --- | --- |
  | Gobernador Regional | Alto | Variable (depende de agenda política) | Demostrar impacto en ERD y ciudadanía |
  | Administrador/a Regional | Alto | Alto (sponsor natural) | Mantener informado, visibilizar quick wins |
  #### Tactico
  | Actor | Power | DGIInterest | Strategy |
  | --- | --- | --- | --- |
  | Jefes de División | Medio-Alto | Variable (algunos resistentes) | Identificar campeones, resolver dolores primero, no amenazar autonomía |
  | Comité de Transformación Digital | Medio | Alto | Proveer secretaría técnica impecable |
  #### Operativo
  | Actor | Power | DGIInterest | Strategy |
  | --- | --- | --- | --- |
  | Profesionales de divisiones | Bajo individual, Alto colectivo | Variable | Capacitación como servicio, celebrar adopciones, crear red de embajadores |
-
  #### ID
  POT-SOC-03
  #### Title
  Modelo ADKAR para Gestión del Cambio
  #### Phases
  | Phase | Question | Action |
  | --- | --- | --- |
  | Awareness | ¿Por qué cambiar? | Comunicar el problema claramente, usar datos |
  | Desire | ¿Qué gano yo? | Mostrar beneficios concretos para cada stakeholder |
  | Knowledge | ¿Cómo lo hago? | Capacitar, proveer materiales, acompañar |
  | Ability | ¿Puedo hacerlo? | Pilotear, ajustar, dar tiempo de práctica |
  | Reinforcement | ¿Seguirá funcionando? | Celebrar éxitos, medir, reconocer |
-
  #### ID
  POT-SOC-04
  #### Title
  Tácticas de Influencia Ética
  #### Note
  El Navegador Institucional utiliza influencia, NO manipulación
  #### Tactics
  | Name | Description | Example |
  | --- | --- | --- |
  | Reciprocidad | Dar antes de pedir | Resolver un dolor pequeño de una división antes de proponer proyecto mayor |
  | Prueba Social | Mostrar que otros ya adoptaron | La División X ya usa el dashboard y redujo 30% sus consultas |
  | Autoridad | Citar fuentes creíbles | Según la normativa TDE, esto debe implementarse para 2026 |
  | Escasez | Crear urgencia legítima | Si no priorizamos esto ahora, no cumpliremos el plazo del PMG |
  | Consistencia | Anclar a compromisos previos | En la última reunión de Comité, se acordó avanzar en esta línea |
  | Simpatía | Construir relación genuina | Reuniones periódicas informales, conocer las personas |
-
  #### ID
  POT-SOC-05
  #### Title
  Detección y Manejo de Resistencias
  #### Types
  | Type | Symptoms | Response |
  | --- | --- | --- |
  | Racional | Objeciones técnicas, preguntas sobre viabilidad | Escuchar, incorporar feedback, ajustar propuesta |
  | Emocional | Frustración, comentarios sobre 'otra moda más' | Empatizar, reconocer fatiga de cambios, ir gradual |
  | Política | Sabotaje pasivo, demoras, 'no es mi prioridad' | Identificar intereses, buscar win-win, escalar si es necesario |
  #### Protocol
  - Paso 1: Escuchar genuinamente la objeción
  - Paso 2: Validar la preocupación legítima
  - Paso 3: Explorar intereses subyacentes
  - Paso 4: Buscar alternativa que satisfaga ambas partes
  - Paso 5: Documentar y ajustar enfoque
  - Paso 6: Si persiste: escalar a AR con propuesta de solución
-
  #### ID
  POT-SOC-06
  #### Title
  Métricas de Éxito Social
  #### Metrics
  | Indicator | Target | Measurement |
  | --- | --- | --- |
  | NPS interno del DGI | > 50 | Encuesta trimestral a divisiones |
  | Tasa de adopción voluntaria | > 70% | % de divisiones que solicitan servicios |
  | Tiempo de respuesta a solicitudes | < 48h | Registro en sistema |
  | Proyectos completados sin escalamiento | > 80% | Conteo de escalamientos a AR |
  | Red de embajadores | 1 por división | Conteo de personas identificadas |

## CognitiveModels
| ID | Title | Purpose | Dimensions |
| --- | --- | --- | --- |
| POT-CM-01 | CM-LEAN-THINKING | Evaluar situaciones desde la perspectiva de mejora continua | ['Identificar desperdicios (7+1 mudas): sobreproducción, esperas, transporte, sobreproceso, inventario, movimiento, defectos, talento subutilizado', 'Aplicar ciclo PDCA: Plan-Do-Check-Act', 'Priorizar por impacto/esfuerzo', 'Buscar causa raíz antes de solucionar', 'Preferir mejoras pequeñas y constantes'] |
| POT-CM-02 | CM-STRUCTURE-PRINCIPLES | Evaluar propuestas organizacionales según ciencia de Meyer | ['Verificar coincidencia autoridad-responsabilidad', 'Confirmar dominios precisos sin superposición', 'Evaluar especialización vs. generalización', 'Detectar conflictos de interés potenciales', 'Validar agrupación por sinergias profesionales', "Aplicar paradigma 'negocio dentro del negocio'"] |
| POT-CM-03 | CM-SOCIAL-NAVIGATION | Evaluar dimensión social de cambios organizacionales | ['Mapear stakeholders y sus intereses', 'Aplicar ADKAR: ¿Tiene awareness, desire, knowledge, ability, reinforcement?', 'Seleccionar táctica de influencia apropiada', 'Detectar tipo de resistencia (racional, emocional, política)', 'Planificar comunicación y acompañamiento'] |
| POT-CM-04 | CM-DMAIC-EVALUATOR | Evaluar proyectos de mejora según metodología DMAIC | ['DEFINE: ¿Problema claro? ¿Alcance definido? ¿Sponsor identificado?', 'MEASURE: ¿Línea base establecida? ¿Datos confiables?', 'ANALYZE: ¿Causa raíz identificada? ¿Priorización por impacto?', 'IMPROVE: ¿Solución diseñada? ¿Pilotaje realizado?', 'CONTROL: ¿Controles establecidos? ¿Transferencia a operación?'] |

## Fuentes derivadas
### Kb gn lean6 core koda
- Fuente: `core/gestion/kb_gn_lean6_core_koda.yml`
- Tipo: estructurado
- Claves: _manifest, ID, Version, Status, Human-Creator, Human-Editor, Model-Collaborator, Creation-Date, Modification-Date, Source
### Kb gn meyer org structure koda
- Fuente: `core/gestion/kb_gn_meyer_org_structure_koda.yml`
- Tipo: estructurado
- Claves: _manifest, ID, Version, Status, Format, Human-Creator, Human-Editor, Model-Collaborator, AI-Remediator, Creation-Date
