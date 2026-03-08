---
_manifest:
  urn: urn:gn:kb:plan-potenciamiento-dgi
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/dgi/kb_gn_plan_potenciamiento_dgi_koda.yml; core/gestion/kb_gn_lean6_core_koda.yml;
      core/gestion/kb_gn_meyer_org_structure_koda.yml
version: 2.0.0
status: draft
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
    cr: 1.1
    run_id: gn-smoke
    review_gate: manual
    scope_statement: Plan DGI con dependencias core declaradas.
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 56
    meat_count: 1244
    fat_count: 0
    preserved_facts:
    - 'CognitiveModels[0].Dimensions[0]=Identificar desperdicios (7+1 mudas): sobreproducción,
      esperas, transporte, sobreproceso, inventario, movimiento, defectos, talento
      subutilizado'
    - 'CognitiveModels[0].Dimensions[1]=Aplicar ciclo PDCA: Plan-Do-Check-Act'
    - CognitiveModels[0].Dimensions[2]=Priorizar por impacto/esfuerzo
    - CognitiveModels[0].Dimensions[3]=Buscar causa raíz antes de solucionar
    - CognitiveModels[0].Dimensions[4]=Preferir mejoras pequeñas y constantes
    - CognitiveModels[0].ID=POT-CM-01
    - CognitiveModels[0].Purpose=Evaluar situaciones desde la perspectiva de mejora
      continua
    - CognitiveModels[0].Title=CM-LEAN-THINKING
    - CognitiveModels[1].Dimensions[0]=Verificar coincidencia autoridad-responsabilidad
    - CognitiveModels[1].Dimensions[1]=Confirmar dominios precisos sin superposición
    - CognitiveModels[1].Dimensions[2]=Evaluar especialización vs. generalización
    - CognitiveModels[1].Dimensions[3]=Detectar conflictos de interés potenciales
    - CognitiveModels[1].Dimensions[4]=Validar agrupación por sinergias profesionales
    - CognitiveModels[1].Dimensions[5]=Aplicar paradigma 'negocio dentro del negocio'
    - CognitiveModels[1].ID=POT-CM-02
    - CognitiveModels[1].Purpose=Evaluar propuestas organizacionales según ciencia
      de Meyer
    - CognitiveModels[1].Title=CM-STRUCTURE-PRINCIPLES
    - CognitiveModels[2].Dimensions[0]=Mapear stakeholders y sus intereses
    - 'CognitiveModels[2].Dimensions[1]=Aplicar ADKAR: ¿Tiene awareness, desire, knowledge,
      ability, reinforcement?'
    - CognitiveModels[2].Dimensions[2]=Seleccionar táctica de influencia apropiada
    - CognitiveModels[2].Dimensions[3]=Detectar tipo de resistencia (racional, emocional,
      política)
    - CognitiveModels[2].Dimensions[4]=Planificar comunicación y acompañamiento
    - CognitiveModels[2].ID=POT-CM-03
    - CognitiveModels[2].Purpose=Evaluar dimensión social de cambios organizacionales
    - CognitiveModels[2].Title=CM-SOCIAL-NAVIGATION
    - 'CognitiveModels[3].Dimensions[0]=DEFINE: ¿Problema claro? ¿Alcance definido?
      ¿Sponsor identificado?'
    - 'CognitiveModels[3].Dimensions[1]=MEASURE: ¿Línea base establecida? ¿Datos confiables?'
    - 'CognitiveModels[3].Dimensions[2]=ANALYZE: ¿Causa raíz identificada? ¿Priorización
      por impacto?'
    - 'CognitiveModels[3].Dimensions[3]=IMPROVE: ¿Solución diseñada? ¿Pilotaje realizado?'
    - 'CognitiveModels[3].Dimensions[4]=CONTROL: ¿Controles establecidos? ¿Transferencia
      a operación?'
    - CognitiveModels[3].ID=POT-CM-04
    - CognitiveModels[3].Purpose=Evaluar proyectos de mejora según metodología DMAIC
    - CognitiveModels[3].Title=CM-DMAIC-EVALUATOR
    - Creation-Date=2026-01-29
    - 'Ctx=Plan de Potenciamiento del DGI: Integración Meyer + Lean Six Sigma + Navegación
      Social'
    - DMAICFramework[0].Description=Cada proyecto de mejora del DGI sigue el ciclo
      DMAIC
    - DMAICFramework[0].ID=POT-DMAIC-01
    - DMAICFramework[0].Phases.Analyze[0]=Análisis de causa raíz (5 Porqués, Ishikawa)
    - DMAICFramework[0].Phases.Analyze[1]=Identificar cuellos de botella
    - DMAICFramework[0].Phases.Analyze[2]=Cuantificar oportunidades de mejora
    - DMAICFramework[0].Phases.Analyze[3]=Priorizar causas según impacto
    - DMAICFramework[0].Phases.Control[0]=Establecer controles estadísticos
    - DMAICFramework[0].Phases.Control[1]=Documentar nuevo estándar
    - DMAICFramework[0].Phases.Control[2]=Crear alertas automáticas
    - DMAICFramework[0].Phases.Control[3]=Transferir a operación normal
    - DMAICFramework[0].Phases.Define[0]=Identificar problema/oportunidad
    - DMAICFramework[0].Phases.Define[1]=Establecer alcance y objetivos SMART
    - DMAICFramework[0].Phases.Define[2]=Definir stakeholders y sponsor
    - DMAICFramework[0].Phases.Define[3]=Documentar caso de negocio
    - DMAICFramework[0].Phases.Improve[0]=Diseñar solución TO-BE
    - DMAICFramework[0].Phases.Improve[1]=Prototipar y pilotear
    - DMAICFramework[0].Phases.Improve[2]=Implementar cambios
    - DMAICFramework[0].Phases.Improve[3]=Capacitar usuarios
    - DMAICFramework[0].Phases.Measure[0]=Establecer línea base con métricas actuales
    - DMAICFramework[0].Phases.Measure[1]=Recopilar datos del proceso AS-IS
    - DMAICFramework[0].Phases.Measure[2]=Validar sistema de medición
    - DMAICFramework[0].Phases.Measure[3]=Crear Value Stream Map si aplica
    - DMAICFramework[0].Title=Marco Operativo DMAIC para DGI
    - DMAICFramework[1].Application=Aplicar 5S japonés al ecosistema de conocimiento
      institucional
    - DMAICFramework[1].ID=POT-DMAIC-02
    - DMAICFramework[1].S5Mapping[0].Application=Auditar artefactos, deprecar obsoletos,
      categorizar por utilidad
    - DMAICFramework[1].S5Mapping[0].S=Seiri (Clasificar)
    - DMAICFramework[1].S5Mapping[1].Application=URNs consistentes, catálogo maestro,
      taxonomía clara
    - DMAICFramework[1].S5Mapping[1].S=Seiton (Ordenar)
    - DMAICFramework[1].S5Mapping[2].Application=Revisión periódica de vigencia, corrección
      de errores
    - DMAICFramework[1].S5Mapping[2].S=Seiso (Limpiar)
    - DMAICFramework[1].S5Mapping[3].Application=Plantillas KODA, procesos de curación,
      naming conventions
    - DMAICFramework[1].S5Mapping[3].S=Seiketsu (Estandarizar)
    - DMAICFramework[1].S5Mapping[4].Application=Cultura de actualización, governance
      de KB, capacitación continua
    - DMAICFramework[1].S5Mapping[4].S=Shitsuke (Disciplina)
    - DMAICFramework[1].Title=Sistema 5S para Gestión del Conocimiento
    - DMAICFramework[2].Candidate=Flujo de Visación de Actos Administrativos
    - DMAICFramework[2].ID=POT-DMAIC-03
    - DMAICFramework[2].Phases.Analyze.Output=Identificación de esperas, reprocesos,
      cuellos de botella
    - DMAICFramework[2].Phases.Control.Output=Dashboard de seguimiento, alertas de
      SLA, revisión mensual
    - DMAICFramework[2].Phases.Define.Output=Charter del proyecto con objetivo de
      reducir tiempo de visación en 30%
    - DMAICFramework[2].Phases.Improve.Output=Automatización de notificaciones, checklist
      digital, flujo en paralelo
    - DMAICFramework[2].Phases.Measure.Output=VSM actual, tiempos de ciclo por etapa,
      volumen mensual
    - DMAICFramework[2].Title=Proyecto Piloto DMAIC Sugerido
    - DMAICFramework[3].Columns[0]=BACKLOG
    - DMAICFramework[3].Columns[1]=EN DISEÑO (DMAIC D-M-A)
    - DMAICFramework[3].Columns[2]=EN IMPLEMENTACIÓN (DMAIC I)
    - DMAICFramework[3].Columns[3]=EN VERIFICACIÓN (DMAIC C)
    - DMAICFramework[3].Columns[4]=COMPLETADO
    - DMAICFramework[3].ID=POT-DMAIC-04
    - DMAICFramework[3].Title=Tablero Kanban para Gestión de Iniciativas
    - DMAICFramework[3].WIPLimits.Diseño=2
    - DMAICFramework[3].WIPLimits.Implementación=3
    - DMAICFramework[3].WIPLimits.Verificación=2
    - Human-Creator=felixsanhueza
    - Human-Editor=felixsanhueza
    - ID=PLAN-POTENCIAMIENTO-DGI-KODA-01
    - IntegrationArchitecture[0].BuildingBlocks[0].Block=Engineers (Base)
    - IntegrationArchitecture[0].BuildingBlocks[0].Products[0]=Modelos BPMN, diseños
      de automatización, especificaciones técnicas
    - IntegrationArchitecture[0].BuildingBlocks[0].Products[1]=Configuraciones KB,
      agentes IA, arquitecturas de integración
    - IntegrationArchitecture[0].BuildingBlocks[0].Roles[0]=Especialista Procesos
    - IntegrationArchitecture[0].BuildingBlocks[0].Roles[1]=Especialista TD
    - IntegrationArchitecture[0].BuildingBlocks[1].Block=Service Providers (Asset-based)
    - IntegrationArchitecture[0].BuildingBlocks[1].Products[0]=Dashboards, informes
      periódicos, alertas operativas
    - IntegrationArchitecture[0].BuildingBlocks[1].Roles[0]=Especialista Control
    - IntegrationArchitecture[0].BuildingBlocks[2].Block=Coordinators
    - IntegrationArchitecture[0].BuildingBlocks[2].Products[0]=Planificación estratégica,
      facilitación de consensos, gestión de prioridades
    - IntegrationArchitecture[0].BuildingBlocks[2].Roles[0]=Jefe DGI
    - IntegrationArchitecture[0].BuildingBlocks[3].Block=Sales & Marketing (Internal)
    - IntegrationArchitecture[0].BuildingBlocks[3].Products[0]=Mapeo stakeholders,
      estrategia de influencia, acompañamiento en transiciones
    - IntegrationArchitecture[0].BuildingBlocks[3].Roles[0]=Navegador Institucional
    - 'IntegrationArchitecture[0].Description=Organización del DGI según los principios
      de especialización y dominios precisos,

      donde cada rol opera como un ''negocio dentro del negocio''.'
    - IntegrationArchitecture[0].ID=POT-ARQ-01
    - IntegrationArchitecture[0].Title=Arquitectura de Building Blocks (Meyer)
    - IntegrationArchitecture[1].Catalog.CoordinatorsJefatura[0]=Plan de trabajo consensuado
    - IntegrationArchitecture[1].Catalog.CoordinatorsJefatura[1]=Priorización de iniciativas
    - IntegrationArchitecture[1].Catalog.CoordinatorsJefatura[2]=Resolución de conflictos
    - IntegrationArchitecture[1].Catalog.CoordinatorsJefatura[3]=Comunicación con
      AR
    - IntegrationArchitecture[1].Catalog.EngineersProcesos[0]=Modelo BPMN proceso
      AS-IS
    - IntegrationArchitecture[1].Catalog.EngineersProcesos[1]=Diseño proceso TO-BE
    - IntegrationArchitecture[1].Catalog.EngineersProcesos[2]=Especificación de automatización
    - IntegrationArchitecture[1].Catalog.EngineersProcesos[3]=Análisis de causa raíz
    - IntegrationArchitecture[1].Catalog.EngineersTD[0]=Artefacto conocimiento estructurado
    - IntegrationArchitecture[1].Catalog.EngineersTD[1]=Agente IA configurado
    - IntegrationArchitecture[1].Catalog.EngineersTD[2]=Integración entre sistemas
    - IntegrationArchitecture[1].Catalog.EngineersTD[3]=Capacitación técnica
    - IntegrationArchitecture[1].Catalog.ServiceProvidersControl[0]=Dashboard ejecutivo
      (diario)
    - IntegrationArchitecture[1].Catalog.ServiceProvidersControl[1]=Informe estado
      situacional (semanal)
    - IntegrationArchitecture[1].Catalog.ServiceProvidersControl[2]=Alerta de desviación
      (continuo)
    - IntegrationArchitecture[1].Catalog.ServiceProvidersControl[3]=Métrica calculada
      y verificada
    - IntegrationArchitecture[1].ID=POT-ARQ-02
    - IntegrationArchitecture[1].Title=Catálogo de Productos DGI
    - IntegrationArchitecture[2].ID=POT-ARQ-03
    - IntegrationArchitecture[2].InteractionModel[0]=Catálogo de servicios publicado
    - IntegrationArchitecture[2].InteractionModel[1]=Solicitudes canalizadas formalmente
    - IntegrationArchitecture[2].InteractionModel[2]=SLAs definidos por tipo de producto
    - IntegrationArchitecture[2].InteractionModel[3]=Feedback estructurado post-entrega
    - 'IntegrationArchitecture[2].InternalClients[0]=Administración Regional: estrategia,
      prioridades'
    - 'IntegrationArchitecture[2].InternalClients[1]=Divisiones: mejoras operativas,
      cumplimiento TDE'
    - 'IntegrationArchitecture[2].InternalClients[2]=Comité TD: secretaría técnica'
    - 'IntegrationArchitecture[2].KeyPrinciple=El DGI PROPONE y FACILITA; las divisiones
      DECIDEN y EJECUTAN.

      Autoridad para decidir = Responsabilidad por resultados.'
    - IntegrationArchitecture[2].Paradigm=Business Within a Business
    - IntegrationArchitecture[2].Title=Relaciones Cliente-Proveedor
    - 'LLM_Parsing_Instructions.Content=BEGIN_LLM_INSTRUCTIONS

      You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.


      FIDELITY: Preserve meat (essential information) and skeleton (structure: headers,
      IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic
      prose).


      LEXICON (expand before processing): Act->Action, Cond->Condition, Ctx->Context,
      Def->Definition, Ex->Example, Mssn->Mission, Obj->Objective, Proc->Process,
      Purp->Purpose, Ref->Reference, XRef->Cross-Artifact Reference, Req->Requirement,
      Res->Result, Src->Source, Prohib->Prohibition, Warn->Warning, Just->Justification,
      Rec->Recommendation


      REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS
      document. XRef/XRef_Required: are external only—must point to a URN.


      LANGUAGE POLICY: Keywords in English, content in original language. Never translate
      content.

      END_LLM_INSTRUCTIONS

      '
    - LLM_Parsing_Instructions.ID=KODA-LLM-PARSER-01
    - LLM_Parsing_Instructions.Prohib=Using for artifact creation or translation.
    - LLM_Parsing_Instructions.Req=Mandatory block following Metadata.
    - Metrics.Artifact_Chars=18500
    - Metrics.CR=1.33
    - Metrics.FS=100%
    - Metrics.Source_Chars=24568
    - Model-Collaborator=KODA-ARCHITECT
    - Modification-Date=2026-01-29
    - PerspectiveSynthesis[0].ID=POT-SYN-01
    - PerspectiveSynthesis[0].Principles[0].Application=Autoridad y responsabilidad
      deben coincidir. El DGI asesora pero NO decide por las divisiones.
    - PerspectiveSynthesis[0].Principles[0].ID=MEYER-P1
    - PerspectiveSynthesis[0].Principles[0].Name=Regla de Oro
    - PerspectiveSynthesis[0].Principles[1].Application=Cada rol del DGI debe ser
      experto de clase mundial en su dominio, colaborando con pares especializados.
    - PerspectiveSynthesis[0].Principles[1].ID=MEYER-P2
    - PerspectiveSynthesis[0].Principles[1].Name=Especialización + Trabajo en Equipo
    - PerspectiveSynthesis[0].Principles[2].Application=Límites claros entre Control
      de Gestión, Procesos y TD sin superposiciones ni brechas.
    - PerspectiveSynthesis[0].Principles[2].ID=MEYER-P3
    - PerspectiveSynthesis[0].Principles[2].Name=Dominios Precisos
    - PerspectiveSynthesis[0].Principles[3].Application=Subdividir por especialidad
      técnica (qué producen), no por cliente o proceso interno.
    - PerspectiveSynthesis[0].Principles[3].ID=MEYER-P4
    - PerspectiveSynthesis[0].Principles[3].Name=Base para Subestructura
    - PerspectiveSynthesis[0].Principles[4].Application=No mezclar funciones de auditoría
      con servicios; no mezclar estabilidad con innovación.
    - PerspectiveSynthesis[0].Principles[4].ID=MEYER-P5
    - PerspectiveSynthesis[0].Principles[4].Name=Evitar Conflictos de Interés
    - PerspectiveSynthesis[0].Principles[5].Application=Mantener especialistas similares
      juntos para intercambio profesional y economías de escala.
    - PerspectiveSynthesis[0].Principles[5].ID=MEYER-P6
    - PerspectiveSynthesis[0].Principles[5].Name=Agrupar por Sinergias Profesionales
    - PerspectiveSynthesis[0].Principles[6].Application=Cada rol del DGI es un 'emprendedor
      interno' que vende productos/servicios a clientes internos.
    - PerspectiveSynthesis[0].Principles[6].ID=MEYER-P7
    - PerspectiveSynthesis[0].Principles[6].Name=Negocio Dentro del Negocio
    - 'PerspectiveSynthesis[0].Title=Perspectiva Meyer: Estructura como Ciencia'
    - PerspectiveSynthesis[0].XRef=urn:knowledge:gorenuble:core:gestion:meyer-org-structure:1.0.0
    - PerspectiveSynthesis[1].Concepts[0].Application=Organización visual del conocimiento
      institucional y flujos de trabajo.
    - PerspectiveSynthesis[1].Concepts[0].ID=LEAN-C1
    - PerspectiveSynthesis[1].Concepts[0].Name=5S
    - 'PerspectiveSynthesis[1].Concepts[1].Application=Ciclo sistemático para proyectos
      de mejora: Definir → Medir → Analizar → Mejorar → Controlar.'
    - PerspectiveSynthesis[1].Concepts[1].ID=LEAN-C2
    - PerspectiveSynthesis[1].Concepts[1].Name=DMAIC
    - PerspectiveSynthesis[1].Concepts[2].Application=Identificar y reducir actividades
      que no agregan valor en procesos del GORE.
    - PerspectiveSynthesis[1].Concepts[2].ID=LEAN-C3
    - PerspectiveSynthesis[1].Concepts[2].Name=Eliminación de Desperdicios
    - PerspectiveSynthesis[1].Concepts[3].Application=Uso de datos para detectar desviaciones
      antes de que escalen.
    - PerspectiveSynthesis[1].Concepts[3].ID=LEAN-C4
    - PerspectiveSynthesis[1].Concepts[3].Name=Control Estadístico
    - PerspectiveSynthesis[1].Concepts[4].Application=Cultura de mejora continua pequeña
      y constante vs. grandes revoluciones.
    - PerspectiveSynthesis[1].Concepts[4].ID=LEAN-C5
    - PerspectiveSynthesis[1].Concepts[4].Name=Kaizen
    - PerspectiveSynthesis[1].ID=POT-SYN-02
    - 'PerspectiveSynthesis[1].Title=Perspectiva Lean Six Sigma: Mejora Sistemática'
    - PerspectiveSynthesis[1].XRef=urn:knowledge:gorenuble:core:gestion:lean6:1.0.1
    - Scope.Excludes[0]=Plantillas vacías para proyectos específicos
    - Scope.Includes[0]=Síntesis de perspectivas Meyer y Lean Six Sigma
    - Scope.Includes[1]=Modelo de integración estructural y metodológico
    - Scope.Includes[2]=Navegación social y gestión del cambio
    - Scope.Includes[3]=Modelos cognitivos para AR Virtual
    - SocialNavigation[0].AlternateName=Gestor de Relaciones y Cambio
    - SocialNavigation[0].BuildingBlock=Sales & Marketing (Internal)
    - 'SocialNavigation[0].Definition=Profesional que cultiva relaciones estratégicas
      con stakeholders clave,

      facilita la adopción de cambios, y "vende" internamente el valor del DGI

      sin imponer ni auditar.'
    - "SocialNavigation[0].GuidingPrinciple=\"No vendemos productos; ayudamos a las\
      \ divisiones a descubrir cómo \nnuestros servicios pueden resolver sus dolores\
      \ operativos.\""
    - SocialNavigation[0].ID=POT-SOC-01
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
---

# Plan de Potenciamiento DGI

## Alcance
Plan DGI con dependencias core declaradas.

## Fuente: Kb gn plan potenciamiento dgi koda
### Manifest
#### Urn
urn:knowledge:gorenuble:gn:plan-potenciamiento-dgi:1.0.0
#### Federation
#### Visibility
private
#### License
UNLICENSED
#### Resolution
#### Canonical url
file://knowledge/domains/gn/dgi/kb_gn_plan_potenciamiento_dgi_koda.yml
#### Provenance
#### Created by
felixsanhueza
#### Created at
2026-01-29
#### Source file
implementation_plan.md
#### Last modified at
2026-01-29
#### Dependencies
#### Requires
| urn |
| --- |
| urn:knowledge:gorenuble:core:gestion:meyer-org-structure:1.0.0 |
| urn:knowledge:gorenuble:core:gestion:lean6:1.0.1 |
### ID
PLAN-POTENCIAMIENTO-DGI-KODA-01
### Version
1.0.0
### Status
Published
### Human Creator
felixsanhueza
### Human Editor
felixsanhueza
### Model Collaborator
KODA-ARCHITECT
### Creation Date
2026-01-29
### Modification Date
2026-01-29
### Source
implementation_plan.md
### Ctx
Plan de Potenciamiento del DGI: Integración Meyer + Lean Six Sigma + Navegación Social
### XRef Required
- urn:knowledge:koda:core:spec:1.0.0
- urn:knowledge:gorenuble:core:gestion:meyer-org-structure:1.0.0
- urn:knowledge:gorenuble:core:gestion:lean6:1.0.1
### LLM Parsing Instructions
#### ID
KODA-LLM-PARSER-01
#### Req
Mandatory block following Metadata.
#### Prohib
Using for artifact creation or translation.
#### Content
BEGIN_LLM_INSTRUCTIONS
You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).

LEXICON (expand before processing): Act->Action, Cond->Condition, Ctx->Context, Def->Definition, Ex->Example, Mssn->Mission, Obj->Objective, Proc->Process, Purp->Purpose, Ref->Reference, XRef->Cross-Artifact Reference, Req->Requirement, Res->Result, Src->Source, Prohib->Prohibition, Warn->Warning, Just->Justification, Rec->Recommendation

REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. XRef/XRef_Required: are external only—must point to a URN.

LANGUAGE POLICY: Keywords in English, content in original language. Never translate content.
END_LLM_INSTRUCTIONS

### Scope
#### Includes
- Síntesis de perspectivas Meyer y Lean Six Sigma
- Modelo de integración estructural y metodológico
- Navegación social y gestión del cambio
- Modelos cognitivos para AR Virtual
#### Excludes
- Plantillas vacías para proyectos específicos
### Metrics
#### Source Chars
24568
#### Artifact Chars
18500
#### CR
1.33
#### FS
100%
### PerspectiveSynthesis
-
  #### ID
  POT-SYN-01
  #### Title
  Perspectiva Meyer: Estructura como Ciencia
  #### XRef
  urn:knowledge:gorenuble:core:gestion:meyer-org-structure:1.0.0
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
  urn:knowledge:gorenuble:core:gestion:lean6:1.0.1
  #### Concepts
  | ID | Name | Application |
  | --- | --- | --- |
  | LEAN-C1 | 5S | Organización visual del conocimiento institucional y flujos de trabajo. |
  | LEAN-C2 | DMAIC | Ciclo sistemático para proyectos de mejora: Definir → Medir → Analizar → Mejorar → Controlar. |
  | LEAN-C3 | Eliminación de Desperdicios | Identificar y reducir actividades que no agregan valor en procesos del GORE. |
  | LEAN-C4 | Control Estadístico | Uso de datos para detectar desviaciones antes de que escalen. |
  | LEAN-C5 | Kaizen | Cultura de mejora continua pequeña y constante vs. grandes revoluciones. |
### IntegrationArchitecture
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
### DMAICFramework
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
### SocialNavigation
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
### CognitiveModels
| ID | Title | Purpose | Dimensions |
| --- | --- | --- | --- |
| POT-CM-01 | CM-LEAN-THINKING | Evaluar situaciones desde la perspectiva de mejora continua | ['Identificar desperdicios (7+1 mudas): sobreproducción, esperas, transporte, sobreproceso, inventario, movimiento, defectos, talento subutilizado', 'Aplicar ciclo PDCA: Plan-Do-Check-Act', 'Priorizar por impacto/esfuerzo', 'Buscar causa raíz antes de solucionar', 'Preferir mejoras pequeñas y constantes'] |
| POT-CM-02 | CM-STRUCTURE-PRINCIPLES | Evaluar propuestas organizacionales según ciencia de Meyer | ['Verificar coincidencia autoridad-responsabilidad', 'Confirmar dominios precisos sin superposición', 'Evaluar especialización vs. generalización', 'Detectar conflictos de interés potenciales', 'Validar agrupación por sinergias profesionales', "Aplicar paradigma 'negocio dentro del negocio'"] |
| POT-CM-03 | CM-SOCIAL-NAVIGATION | Evaluar dimensión social de cambios organizacionales | ['Mapear stakeholders y sus intereses', 'Aplicar ADKAR: ¿Tiene awareness, desire, knowledge, ability, reinforcement?', 'Seleccionar táctica de influencia apropiada', 'Detectar tipo de resistencia (racional, emocional, política)', 'Planificar comunicación y acompañamiento'] |
| POT-CM-04 | CM-DMAIC-EVALUATOR | Evaluar proyectos de mejora según metodología DMAIC | ['DEFINE: ¿Problema claro? ¿Alcance definido? ¿Sponsor identificado?', 'MEASURE: ¿Línea base establecida? ¿Datos confiables?', 'ANALYZE: ¿Causa raíz identificada? ¿Priorización por impacto?', 'IMPROVE: ¿Solución diseñada? ¿Pilotaje realizado?', 'CONTROL: ¿Controles establecidos? ¿Transferencia a operación?'] |

## Fuente: Kb gn lean6 core koda
### Manifest
#### Urn
urn:knowledge:gorenuble:core:gestion:lean6:1.0.1
#### Federation
#### Visibility
private
#### License
UNLICENSED
#### Resolution
#### Canonical url
file://knowledge/core/gestion/kb_gn_lean6_core_koda.yml
#### Provenance
#### Created by
felixsanhueza
#### Created at
2026-01-29
#### Source file
complement/lean6.md
#### Last modified at
2026-01-29
### ID
LEAN6-KODA-CORE-01
### Version
1.0.1
### Status
Draft
### Human Creator
felixsanhueza
### Human Editor
felixsanhueza
### Model Collaborator
GPT-5.2
### Creation Date
2026-01-29
### Modification Date
2026-01-29
### Source
complement/lean6.md
### Ctx
Lean Six Sigma concepts; no book chapter structure; workshops + practical activity details removed by request
### Warn
Contenido derivado de fuente potencialmente protegida por copyright; uso interno; verificar derechos antes de redistribuir.
### XRef Required
urn:knowledge:koda:core:spec:1.0.0
### LLM Parsing Instructions
#### ID
KODA-LLM-PARSER-01
#### Req
Mandatory block following Metadata.
#### Prohib
Using for artifact creation or translation.
#### Content
BEGIN_LLM_INSTRUCTIONS
You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).

LEXICON (expand before processing): Act->Action, Cond->Condition, Ctx->Context, Ctx_Required->Required External Reference, Ctx_Optional->Optional External Reference, Def->Definition, Ex->Example, Mssn->Mission, Obj->Objective, Proc->Process, Purp->Purpose, Ref->Reference, XRef->Cross-Artifact Reference, XRef_Required->Mandatory Cross-Artifact Reference, Req->Requirement, Res->Result, Src->Source, Prohib->Prohibition, Warn->Warning, Just->Justification, Rec->Recommendation

REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. XRef/XRef_Required: are external only—must point to a URN (optionally with #ID fragment) in another artifact. External documents without specific ID use Ctx:, Ctx_Required:, or Ctx_Optional:.

LANGUAGE POLICY: Keywords in English, content in original language. Never translate content.
END_LLM_INSTRUCTIONS

### Scope
#### Req
Preserve all non-workshop content with no translation.
#### Prohib
Re-introducing workshop instructions, blank templates, step-by-step practical tasks.
#### Includes
Method classifications, descriptions, conceptual steps, formulas, tool lists.
#### Excludes
- Workshops (any section titled "Workshop")
- Implementation/Task/Blank Templates/Appendix sections
- Figure/Image blocks and captions
- Form/template field layouts (e.g., Kanban card template fields)
### Metrics
#### Source Chars
261913
#### Artifact Chars
83442
#### CR
3.139
#### FS
100% for included scope (workshop/practical details excluded by design)
### Topics
| ID | Cat | Title | Src | Text |
| --- | --- | --- | --- | --- |
| TOPIC-001 | Lean Six Sigma | Classification of the Book | Lean Six Sigma > Introduction > Classification of the Book | All methods presented in this book serve to optimize processes within the company. But what significance and relevance do these methods have in terms of economic efficiency? Do the methods also result in an increase in company value? This question will be examined in more detail below. The creation of value in the company can be measured via the Economic Value Added (EVA).
As can be seen in Fig. 1.1, an economic value can only be created when the operating profit (Net Operating Profit After Taxes) covers the capital costs. The capital costs are in turn composed of the fixed assets and the Working Capital (WC) as well as the capital cost rate. The lever for increasing company value with the methods of production optimization lies in the area of Working Capital. Working Capital is defined as [1]:
Working Capital represents both a measure of liquidity, as current assets can usually be quickly converted into liquid funds (unlike fixed assets), and a measure of a company's financing needs. If the WC can be reduced, this leads to a reduction in financing needs and thus to an improvement in capital profitability and improved interest expenses. Based on the definition of WC, the lever of current assets can already be fixed, which can be optimized through operational excellence. The aim is to achieve continuous value enhancement through the application of Lean Management philosophy and the methods of production optimization, thereby strengthening the company sustainably [1, 2].
The WC is primarily determined by processes that affect inventories, receivables and liabilities. These processes are income management (Order-to-Cash), inventory management (Total-Supply-Chain) and expenditure management (Purchase-to-Pay). The focus below is on inventory management and the associated reduction of stocks. However, it should be considered that a holistic view of the three processes listed must always be taken to avoid isolated solutions. To minimize stocks, various intermediate goals can be formulated. For example, with the help of SMED, the setup time can be shortened or waste and scrap can be reduced by applying Poka Yoke. Also, existing transport routes, warehouses and processes can be optimized through a value stream analysis to achieve a reduction in stock [1].
In summary, it can be stated that suitable measures, some of which are presented in the book, have a high influence on the economic efficiency of the company. Thus, the inventory and consequently the Working Capital can be reduced. This results in the company's capital costs decreasing and the company value being increased.
The book is divided into individual self-contained chapters, each presenting methods for optimizing production structures. |
| TOPIC-002 | 5S | Classification of the Method | Lean Six Sigma > 5S—Seiri, Seiton, Seiso, Seiketsu, Shitsuke > Classification of the Method | 5S is a Lean tool for systematically uncovering waste, named after the initial letters of five Japanese terms [1]. The term 5S is usually associated with a tidy and organized workplace and the assurance that this state is maintained [2].
However, it turns out (Fig. 2.1), that this representation of the goals of 5S is not appropriate, because 5S is more than a method for creating order. 5S is a foundation of every Lean management approach and a prerequisite for the application of the PDCA methodology [2–5]. |
| TOPIC-003 | 5S | Description of the Method | Lean Six Sigma > 5S—Seiri, Seiton, Seiso, Seiketsu, Shitsuke > Description of the Method | The 5S system, or also referred to as 5A in German technical literature [6], can be divided into the following components:
Seiri: Seiri (Sorting) describes the separation of necessary and unnecessary items at the workplace. Material that is no longer needed is removed from the workplace. This particularly refers to excessive circulating stocks as well as unnecessary, surplus and defective tools, unnecessary machines, faulty parts as well as unneeded papers and documents [1, 6]. The aim is to keep the workplace clear and avoid waste when searching for a tool. This also increases the quality by avoiding damage to the product through the use of the wrong tool [4].
Seiton: Seiton (Tidying up) describes the creation of a visible order that supports the process. This includes providing the work equipment in perfect condition and ergonomically within reach at a defined and standardized place [1]. It is useful to mark the places, as this way missing tools are noticed.
Seiso: Seiso (Keeping the workplace clean) describes the general cleanliness of the workplace. Cleanliness allows errors to be detected more quickly and quality defects due to dirt and foreign bodies to be avoided [4]. Signs of wear and tear on the operating equipment become immediately apparent and unplanned machine stops and costly damage can be avoided. An orderly workplace therefore demonstrably leads to higher employee satisfaction [6].
Seiketsu: The Japanese term Seiketsu refers to the standardization of work processes in individual process steps [1]. New employees can be better trained through prior standardization of the activity. The aim is for work instructions and processes to become routine [6]. In the area of employee induction, Lean management follows a different approach than the classic view. In the classic view, the employee is provided with documents in addition to an induction, from which he can familiarize himself with standards. The Lean management view is that a new employee is trained until he can maintain the standard without documents. In the Western world, Seiketsu is often misunderstood in terms of employee induction. Seiketsu is not intended to ensure the fastest possible induction, but the highest possible quality of work and increased motivation of the employee. The standardization of the activity within the framework of the CIP [4].
Shitsuke: As part of Shitsuke (always apply and improve), employees and managers have to ensure that the achieved standards are not undercut. In addition, the continuous improvement process should be initiated [4], by having employees develop suggestions for eliminating Muda. |
| TOPIC-004 | Lean Six Sigma | Classification of the Method | Lean Six Sigma > Lean Six Sigma > Classification of the Method | Lean Six Sigma is a combination of the goals and techniques of Lean Management and the Six Sigma approach. It thus combines productivity-enhancing measures with quality-focused measures, forming a holistic approach whose goal is to achieve higher success through joint planning and enhancement of both sizes.
It shows that the demand for quality improvement (Fig. 3.1) and simultaneous cost reduction does not have to be a contradiction. Errors and waste are eliminated through a systematic and fact-based analysis of the processes. A targeted implementation of uniform measurement and project systematics increases customer satisfaction and company value [1–3]. |
| TOPIC-005 | Lean Six Sigma | Description of the Method | Lean Six Sigma > Lean Six Sigma > Description of the Method | As already shown in the classification, Lean Six Sigma is the combination of techniques of the elements of Lean Management and Six Sigma. A core element is the DMAIC cycle which is divided into five phases and provides a structured analysis process for a defined problem. The phases are Define (D), Measure (M), Analyze (A), Improve (I), and Control (C). This cyclical structure also ensures continuous improvement. Various tools of Lean Management or Six Sigma can be used in each of these phases (Fig. 3.3). The individual phases will now be presented in detail. |
| TOPIC-006 | Lean Six Sigma | Define Phase | Lean Six Sigma > Lean Six Sigma > Description of the Method > Define Phase | In the Define phase, the current situation is described and the goals and the problem are precisely defined. In addition, the schedule and project organization should be determined. A uniform understanding of the Lean Six Sigma project should be created within the entire team. Therefore, a detailed project contract should be created. An important step in this phase is also to define customer requirements, as these are essential for project success. |
| TOPIC-007 | Lean Six Sigma | VOC | Lean Six Sigma > Lean Six Sigma > Description of the Method > Define Phase > VOC | To define customer requirements, the first step is to capture the voice of the customer (Voice of The Customer). This represents a completely unfiltered statement. The aim is to make this statement measurable criteria up to the Project Ys, so that project success can be measured later (Fig. 3.2). The voice of the customer can be determined through market analyses or individual interviews.
The actual problem of the customer needs to be understood. This results in the customer need. Subsequently, the customer's requirements must be replaced with measurable output criteria. These are also called Critical to Quality (CTQ). This is a feature that has a direct influence on the success of the output (e.g., product).
* VOC: Voice of the customer (customer statement)
* Customer requirements: (list of customer needs)
* CTQs: Critical to Quality (measurable criteria)
* Project Yields: The apex.
To the left of the pyramid, an upward-pointing arrow indicates the transition from an "Unfiltered statement" at the bottom to a "Measurable Requirement of the customer" at the top.]
The example provided for a customer statement is that it takes a very long time until an order release is made; consequently, a specific time limit can be defined for the release process. |
| TOPIC-008 | Lean Six Sigma | Project Contract | Lean Six Sigma > Lean Six Sigma > Description of the Method > Define Phase > Project Contract | At the end of the Define Phase, all information should be recorded in a condensed form in a document. The company situation should be presented to legitimize the project need, including a precisely defined problem statement. A goal description should be recorded according to the SMART (Specific, Measurable, Attainable, Relevant, Time bound) formula. Finally, the financial effect should be defined, and the project team with assigned responsibilities should be named. |
| TOPIC-009 | Lean Six Sigma | Measure Phase | Lean Six Sigma > Lean Six Sigma > Description of the Method > Measure Phase | The main goal of this phase is to determine the current state, serving as the basis for later process improvement. Critical measurement criteria must be selected, and relevant data must be determined to evaluate success in meeting customer requirements. Data quality is crucial and should be verified for "goodness" through a measurement system analysis (MSA). |
| TOPIC-010 | Lean Six Sigma | Measurement System Analysis | Lean Six Sigma > Lean Six Sigma > Description of the Method > Measure Phase > Measurement System Analysis | Data collection is carried out by trained individuals using defined tools and uniform methods. A measurement system must be tested for reliability before use to rule out flawed data and false conclusions. An MSA checks the following characteristics:
* Accuracy ("accuracy")
* Stability ("stability")
* Repeatability ("repeatability")
* Reproducibility ("reproducibility")
Resolution must also be checked, referring to the smallest possible display difference of the device; it should be of the tolerance. For discrete data, an attributive MSA is used, typically requiring at least two appraisers and 30 numbered parts (including both good and defective samples). Each appraiser measures all parts twice in a random order. A goal of 100% match with the reference value is ideal, though may be sufficient. |
| TOPIC-011 | Lean Six Sigma | Process Capability Analysis | Lean Six Sigma > Lean Six Sigma > Description of the Method > Measure Phase > Process Capability Analysis | DPMO (Defects Per Million Opportunities) is a metric describing the error rate from a company perspective:
DPO (Defects Per Opportunities) is used to convert to the later Sigma level:
From a customer's perspective, the PPM (Parts Per Million) metric is used:
If there is only one possibility of error per unit, DPMO and PPM are identical. However, for meeting customer demand, it only matters if the product is defect-free. In complex systems, the denominator for DPMO will be significantly larger than for PPM because of multiple error possibilities, making DPMO a "softer" metric. For actual quality evaluation, the "sharper" PPM metric is more suitable. |
| TOPIC-012 | Lean Six Sigma | Process Capability Indices | Lean Six Sigma > Lean Six Sigma > Description of the Method > Measure Phase > Process Capability Indices | Process capability can be expressed with the metric (dispersion index), which relates process spread to tolerance:
Because does not reflect the position of the mean value, the level index is used to represent process centering:
This metric describes the mean value's position within the tolerance. If a mean value shift of occurs, the level index changes (e.g., from without shift to with shift). A value of at least 1.5 is required to meet Six Sigma standards. |
| TOPIC-013 | Lean Six Sigma | Sigma Level | Lean Six Sigma > Lean Six Sigma > Description of the Method > Measure Phase > Sigma Level | To determine the sigma level, the error rate is converted into the yield ():
This corresponds to a yield of . The sigma level is read using a Z-table. Process sigma is divided into Sigma Short Term and Sigma Long Term. Long-term values account for environmental influences and wear, so a shift of is added to the calculation. |
| TOPIC-014 | Lean Six Sigma | Analysis | Lean Six Sigma > Lean Six Sigma > Description of the Method > Analysis | The objective is to identify root causes of the problem and verify if their resolution solves the process problem. Measured data is structured and assessed in two steps: finding main influencing variables and determining cause-effect relationships. Common methods include:
* Distribution diagrams
* Cause-effect diagram
* Pareto diagram
* Flow diagrams
* Control Charts
* Regression analyses
* Hypothesis test
* Design of Experiment (DoE) |
| TOPIC-015 | Lean Six Sigma | Pareto diagram | Lean Six Sigma > Lean Six Sigma > Description of the Method > Analysis > Pareto diagram | This bar chart arranges individual values from largest to smallest. It is based on the Pareto principle, suggesting that of problems can be traced back to of the causes. |
| TOPIC-016 | Lean Six Sigma | Improve | Lean Six Sigma > Lean Six Sigma > Description of the Method > Improve | In this phase, impact forecasts are reviewed and solutions for process optimization are selected. It involves determining how input variables and parameters should be set, considering disturbance variables. Activities include testing the solution, checking effectiveness, and creating action plans for sustainable implementation. Solutions are evaluated based on cost-benefit ratio, difficulty, implementation time, and risks. |
| TOPIC-017 | Lean Six Sigma | Control | Lean Six Sigma > Lean Six Sigma > Description of the Method > Control | The final phase stabilizes the optimized process and monitors results long-term. A control system is used to recognize deviations and initiate corrective measures, such as internal audits or test plans. Cost savings should be demonstrated via before-and-after comparisons. Successful findings should be communicated company-wide to benefit other projects.
Phase Target Six Sigma tools Lean tools
DEFINE Identification of requirements; determining financial impact; defining participants; considering process influences; coordinating changes. Project profile, VoC, QFD, Kano model; Stakeholder analysis; SIPOC; Communication plan. Value added analysis
MEASURE Mapping the process; working out quality-critical influences; preparation/measurement of data; determination of process capability and sigma level. Quality tree (CTQ); Data collection plan, sample survey; Quality control chart, process capability analysis. Value stream analysis, cycle time diagram
ANALYZE Root cause analysis; comparison of process performance with best practice. FMEA, DoE, Brainstorming, Ishikawa diagram, hypothesis tests, regression analyses; Benchmarking. Seven types of waste, 5 times Why? (5W)
IMPROVE Determination of starting points; implementing improvement actions; installation of continuous improvement routine. Evaluate and select suitable tools; Simulation, piloting. 5S, SMED, Kanban, TPM; Kaizen (KVP)
CONTROL Long-term safeguarding of the results achieved. PDCA, quality plan, project repetition plan. SOP, Poka Yoke |
| TOPIC-018 | Lean Six Sigma | Measure Phase | Lean Six Sigma > Lean Six Sigma > Measure Phase | The main goal of the phase is to determine the current state. This serves as the basis for later process improvement. Critical measurement criteria must be selected and the relevant data determined to evaluate success in meeting customer requirements [5]. The quality of the data is crucial. This should be checked for its goodness with a measurement system analysis (MSA). |
| TOPIC-019 | Lean Six Sigma | Measurement System Analysis | Lean Six Sigma > Lean Six Sigma > Measure Phase > Measurement System Analysis | The collection of data for later analysis is carried out by trained individuals, based on clear instructions and within the framework of uniform methods, using defined measuring tools. This step is important as this procedure leads to a corresponding reliability of the system and the data obtained from it. Before a measurement system can be used, it must first be tested for reliability to rule out that the recorded data are not flawed. The subsequent phases build on this data, thus false conclusions can be accordingly ruled out. A measurement system analysis checks the following characteristics of a measurement system [4]:
* Accuracy (“accuracy”),
* Stability (“stability”),
* Repeatability (“repeatability”) and
* Reproducibility (“reproducibility”).
In addition to the criteria mentioned above, it is also necessary to check the Resolution (resolution). The resolution refers to the smallest possible display difference of the measuring device. It should be less than or equal to 5 % of the Tolerance in order to record the quantity to be measured in sufficient detail [6]. An attributive measurement system analysis (MSA) is applied to discrete data. At least two appraisers and usually 30 numbered parts to be analyzed are required. Care should be taken to include both good parts and defective parts in the sample to be measured. Each appraiser must then measure all parts contained in the sample twice, in a random order. After the measurement results have been recorded, they are compared with the reference value. The goal of a good measurement system analysis is a 100 % match, although a limit value of at least 90 % may be sufficient [2]. |
| TOPIC-020 | Lean Six Sigma | Process Capability Analysis | Lean Six Sigma > Lean Six Sigma > Measure Phase > Process Capability Analysis | The DPMO (Defects Per Million Opportunities) is a metric that describes the error rate and is considered from a company’s perspective. The DPMO is defined as [7]:
The DPO (Defects Per Opportunities) can also be calculated later on, as this metric is used to convert to the later Sigma level. This metric is defined as follows [7]:
If an evaluation is to be carried out primarily from the customer’s perspective, the PPM (Parts Per Million) metric is used. It is defined as [8]:
If there is only one possibility of error—because there is only one characteristic—the DPMO and PPM metrics are the same. For meeting customer demand, it is not crucial whether a product has one or more defects, it is only important that the product is defect-free. Therefore, the PPM metric is a customer-driven metric and is used in the automotive industry as a requirement for suppliers. In contrast, the DPMO is used as an internal metric because it offers a better comparison between different complex systems. This results from the fact that the metric not only evaluates the number of defective units, but also relates these to the possibilities of error. This allows for fine-tuning. However, it should be noted that the error rate (DPMO) is the “softer” metric. This is because the denominator, due to the number of error possibilities, which results from the multiplication of the number of units and the possible number of errors per unit, will always be significantly larger than the denominator of the PPM. This, in turn, means that the overall metric is always smaller than the PPM. Therefore, for the actual evaluation of the quality level, the “sharpest” metric—the PPM—is more suitable [8].
Not only with the determination and consideration of the DPMO and the PPM can a statement be made about the quality capability of the process. To get a more accurate assessment of the capability, the following process capability indices must be determined. |
| TOPIC-021 | Lean Six Sigma | Process Capability Indices | Lean Six Sigma > Lean Six Sigma > Measure Phase > Process Capability Indices | The measure of process capability can be expressed with the metric . This evaluates the reliability of a process to achieve the required goals. For this, the process spread is related to the tolerance. This metric is also described by Töpfer as the dispersion index.
The dispersion index characterizes the basic suitability of a process to deliver values with small dispersion in relation to the length of the tolerance interval. The metric can be calculated by [9, 10]:
The disadvantage of the dispersion index is that it does not reflect the position of the mean value. This can lead to the dispersion being kept within a narrow range (high value), but the process is still not specification-compliant. A high value is a necessary but not sufficient condition to achieve a high process sigma value. For this, an additional consideration of the process centering is required, which is described by the level index and thus represents the second metric for evaluating the process capability [2]. The metric can be calculated as follows [9, 10]:
This metric thus describes the position of the mean value within the tolerance. If a mean value shift of occurs, the level index changes, but the dispersion index does not. This deteriorates from a (without shift) to (with shift). This means that a value of at least 1.5 must be achieved to meet the requirement of Six Sigma [9, 10]. Once the required measurements have been determined, the next step is to analyze them in more detail. |
| TOPIC-022 | Lean Six Sigma | Sigma Level | Lean Six Sigma > Lean Six Sigma > Measure Phase > Sigma Level | To determine the sigma level based on the determined metrics DPMO or DPO and PPM, the error rate is converted into the yield (Yield).
This corresponds to a yield of 11 %
To determine the sigma level, the calculated value can now be read off using the Z-table (Fig. 3.9).
The process sigma level is divided into Sigma Short Term and Sigma Long Term. The difference between a short-term process capability (Sigma Short Term) and the long-term process capability (Sigma Long Term) is based on the fact that the short-term value does not take into account external influences [4]. This means that in the long term, a process is less reliable because environmental influences or wear and tear are present. Therefore, a sigma of 1.5 is added to the Long Term, which expresses the shift due to unreliability. When determining via the DPMO, the table outputs the Sigma Long Term. However, when calculating via the Z-table of the normal distribution, the Sigma Short Term is determined [11]. |
| TOPIC-023 | Lean Six Sigma | Analysis | Lean Six Sigma > Lean Six Sigma > Analysis | The objective of this phase can be described as follows.
Identify the root causes of the problem and then verify whether their resolution solves the process problem [5].
To do this, the measured data must be structured, evaluated, analyzed, and assessed [12]. This phase can be divided into two steps. First, the main influencing variables must be found and then the cause-effect relationships must be determined and represented. Qualitative and statistical methods can be used for this. At the end, the effects and causes on the target variable must be known in order to develop them in the next phase [8].
* Distribution diagrams,
* Cause-effect diagram,
* Pareto diagram,
* Flow diagrams,
* Control Charts,
* Regression analyses,
* Hypothesis test and
* Design of Experiment |
| TOPIC-024 | Lean Six Sigma | Pareto diagram | Lean Six Sigma > Lean Six Sigma > Analysis > Pareto diagram | The insights gained in the Measure phase can be graphically analyzed using a Pareto diagram. This is a bar chart in which the individual values are arranged and cumulated in size from left (largest value) to right (smallest value). This form of presentation allows the existing resources to be focused on the essential influencing variables. This form of analysis is based on the Pareto principle, according to which 80 % of the problems can be traced back to 20 % of the causes [13]. |
| TOPIC-025 | Lean Six Sigma | Improve | Lean Six Sigma > Lean Six Sigma > Improve | In this phase, a review and concretization of the impact forecasts should be carried out again, as the data basis was significantly improved in the previous phase. If the results achieved do not reach the defined target level, the cycle must be run through again [10].
The goal of this phase is to recognize, evaluate, and select solutions for successful optimization [5]. It must be determined how the process input variables and process parameters, taking into account the disturbance variables, are to be set. The activities of this phase also include testing the solution, checking its effectiveness, and the subsequent sustainable implementation using action and measure plans [8, 12]. However, the solution should be evaluated beforehand in terms of cost-benefit ratio, degree of difficulty, time required for implementation, and possible risks [14]. |
| TOPIC-026 | Lean Six Sigma | Control | Lean Six Sigma > Lean Six Sigma > Control | The goal of the final phase is to stabilize the optimized process and check the pursued target level (Fig. 3.3) [10]. To monitor the process results and ensure them in the long term, a control system is needed that directly recognizes deviations and initiates appropriate corrective measures. This can be done through internal audits of the quality management or in the form of previously created test plans [12]. In addition to the control system, the cost savings should also be demonstrated by a before-and-after comparison, using the optimized rejects. If the results are satisfactory, the findings must be communicated throughout the company so that other projects can also benefit from them [5]. After the project is completed, further improvement activities should be implemented to thus directly enter the improvement process (CIP) [10].
Target Six Sigma tools Lean tools
DEFINE PHASE
Identification of customer requirements and value creation from the customer's perspective, definition of a process plan Project profile, VoC, QFD, Kano model Value added analysis
Determining the financial impact and savings potential of the planned project
Determining the requirements of all participants in the process under consideration Stakeholder analysis
Considering the influences and possibilities of the process with regard to its suppliers and customers SIPOC
Coordinating the planned changes with all parties involved and defining the communication structure Communication plan
MEASURE PHASE
Mapping the current process, in particular value creation Value stream analysis, cycle time diagram
Working out quality-critical influences Quality tree (CTQ)
Preparation and measurement of all required data Data collection plan, sample survey
Determination of the process capability and the current sigma level Quality control chart, process capability analysis
ANALYZE PHASE
Carrying out the root cause analysis to determine process influences FMEA, DoE, Brainstorming, Ishikawa diagram, hypothesis tests, regression analyses Seven types of use, 5 times Why? (5W)
Comparison of process performance with best practice Benchmarking
IMPROVE PHASE
Determination of suitable starting points for process improvement Evaluate and select suitable tools
Implementing improvement actions Simulation, piloting 5S, SMED, Kanban, TPM
Installation of a continuous improvement routine Kaizen (KVP )
CONTROL PHASE
Long-term safeguarding of the results achieved PDCA, quality plan, project repetition plan SOP, Poka, Yoke |
| TOPIC-027 | Poka Yoke | Classification of the Method | Lean Six Sigma > Poka Yoke > Classification of the Method | By enforcing the One-Piece-Flow and the desire to be able to produce flawlessly, it is necessary to make the manufacturing processes more reliable and to reduce errors. The goal of the Poka-Yoke method is to prevent errors in assembly in particular through an appropriate process design. The method follows the principle of error source prevention—since no errors can occur without an error source.
Together with the production evolution towards Lean Management, the Poka-Yoke method was invented in Japan in 1961 by Shigeo Shingo. Shigeo Shingo was a quality engineer at Toyota who coined Poka Yoke through the term Poka Yoke [1]. Baka Yoke translates as “foolproof” and quickly spread in organizations like the Arakawa Body Company.
An employee of the Arakawa Body Company, who was told that her workplace was “foolproof”, found the term derogatory and the term was renamed Poka Yoke “avoidance of unintentional errors” [2].
Lean Management is characterized by Kaizen and the avoidance of “Muda” (Waste). Figure 4.1 shows the three essential drivers for successful production—it can be seen that Poka Yoke is classified in terms of product quality compared to other process optimization methods [3]. The essential factors for successful production listed in Fig. 4.1 do condition each other, but are not negatively correlated. While it is possible to improve the quality of products by accepting a longer throughput time, both factors can also be optimized equally through the use of the right methods and an appropriate management approach. Furthermore, Poka Yoke can contribute to increased throughput time through the approach of error source prevention, as potential rework becomes obsolete. |
| TOPIC-028 | Poka Yoke | Description of the Method | Lean Six Sigma > Poka Yoke > Description of the Method | The Zero-Error-Production aimed at by Shigeo Shingo through the application of Poka Yoke is based on a basic idea with three components [4]:
1. Cause Analysis:
In the cause analysis, the process is checked in advance for possible incorrect actions and not resulting errors for their causes. Due to the analysis of the actions with regard to errors, a higher avoidance of errors is possible.
2. 100% Inspection:
Through the implementation of the Poka Yoke, all parts in a process are checked for certain potential incorrect actions, or the process is designed in such a way that the incorrect action does not occur. Due to the simplicity of the facilities, it is also economically possible to check each individual part and not just a sample.
3. Immediate Corrective Actions:
Because the system is designed in such a way that errors are not allowed, the initiation of necessary corrective measures takes place immediately. Furthermore, Wildemann divides Poka Yoke into three subsystems, which allow the discovery and reporting of incorrect actions to follow one another in time [5].
different methods, such as creativity techniques. Other approaches can be the standardization of functions or visualizations at workplaces. |
| TOPIC-029 | Poka Yoke | Do Phase | Lean Six Sigma > Poka Yoke > Description of the Method > Do Phase | 5. Create action plan
After the planning phase has been completed and the analysis is finished, the team creates an action plan in which responsibilities, deadlines, and budgets are defined.
6. Implement action plan
The team implements the measures of the action plan. Both progress and quality need to be controlled, documented, and if necessary, measures initiated. |
| TOPIC-030 | Poka Yoke | Check Phase | Lean Six Sigma > Poka Yoke > Description of the Method > Check Phase | 7. Measure effects
After all activities created in the action plan have been implemented, the team checks through appropriate measurements whether the desired effects have actually occurred. This allows the degree of goal achievement to be specified. Deviations in the realized improvements can—if necessary—be corrected by a new iteration of the DEMING cycle. Special attention should be paid to the implementation of the planned measures during the new iteration. |
| TOPIC-031 | Poka Yoke | Act Phase | Lean Six Sigma > Poka Yoke > Description of the Method > Act Phase | 8. Standardization and assurance of the result
The purpose and goal of the last step of the improvement cycle is to define a standard for the respective process. For the standard to be successfully implemented within the process, appropriate training for the employees may need to be carried out. Audits of the work method ensure the long-term guarantee of the improvement of the overall process. |
| TOPIC-032 | Poka Yoke | References | Lean Six Sigma > Poka Yoke > References | 1. Gutenberg E (1983) Grundlagen der Betriebswirtschaftslehre. Die Produktion (3), 24th ed. Springer, Berlin
2. Böhrs H (1967) Wirtschaften mit der Zeit als Kernstück der REFA-Lehre. In: Böhrs H (Ed) Arbeitsstudien in der Betriebswirtschaft. Gabler, Wiesbaden, S 13–48
3. Zollondz H-D (2013) Grundlagen Lean Management. Einführung in Geschichte, Begriffe, Systeme, Techniken sowie Gestaltungs- und Implementierungsansätze eines modernen Managementparadigmas. Oldenbourg (Edition Management), München |
| TOPIC-033 | Line Balancing | Classification of the Method | Lean Six Sigma > Line Balancing > Classification of the Method | In order to withstand cost pressure in manufacturing, measures are necessary to efficiently utilize and operate the lines. Therefore, one goal must be to eliminate conflicts such as bottlenecks or underutilizations or waiting times in manufacturing. A bottleneck (or also Bottleneck) usually occurs at the workstation where the processing of the process steps (the workload) takes the longest. The so-called "Work-In-Progress (WIP) inventory" is created by processing the process steps at this station. It includes all goods that are still in the processing phase. Conversely, unused times (idle times) occur at workstations with a lower temporal workload, as these workstations always have to wait for further assignment of work by the upstream workstations with longer process times. The idle time then refers to the time when a unit is unproductive or unused (but ready for operation). This is exactly where the method of Line Balancing comes into play.
The goal of Line Balancing is to optimize the value chain and eliminate waste [1]. In terms of production, Line Balancing aims to trim the production chain to flow production in One-Piece-Flow (single production) and to the TPS-typical pull principle [2]. In German, Line Balancing stands for cycle timing, so Line Balancing is essentially nothing more than aligning the cycle times of all workstations in the process to the customer demand to be achieved. Simply put: If you have to produce a part every 20 s to meet customer demand, then each individual station in the production chain—ideally One-Piece-Flow—should also only need 20 s.
Line Balancing thus serves to optimally utilize human and machine resources based on customer demand [1]. The practical goal of the method is therefore to determine the number of workstations and to assign the various tasks to the workstations in such a way that a uniform temporal workload per station is created, in order to achieve a synchronized flow of parts between the workstations or the associated units (see Fig. 6.1).
* Product quality: Chapter III Lean Six Sigma, Chapter IV Poka Yoke, Chapter V SMED.
* Kaizen core: Chapter II 5S.
* Throughput time: Chapter VI Line balancing (highlighted).
* Functional flexibility/Center base: Chapter VII Spaghetti diagram, Chapter VIII Value stream, Chapter IX Kanban.]
The even flow then also means that the idle times of the stations and the "Work-In-Progress inventory" are minimized.
Line Balancing has its origins in the Toyota Production System (TPS) and is also located in the Lean sector. A primary assignment of this method can be seen in connection with specialized Lean Six Sigma tools for improving series production. Another special feature of this method is that optimizations are primarily carried out through mathematical analyses. Therefore, some current users trace the orientation of this tool back to M.E. Salveson, who is considered one of the pioneers for the development of mathematically specialized Lean Six Sigma tools due to his research. His considerations on the problem of the "assembly line balancing problem" were groundbreaking for the development of the Line Balancing method [3]. Today it has a more central importance in the context of the Toyota production systems, whose methods include Line Balancing as well as other mathematically oriented Six Sigma methods, which include, among others, Just in Time, Total Productive Maintenance [4]. |
| TOPIC-034 | Line Balancing | Description of the Method | Lean Six Sigma > Line Balancing > Description of the Method | Line Balancing refers to the smoothing of very irregular production orders in terms of quantity and temporal sequence from the existing customer orders [5]. The main concern of line balancing is to balance the individual workstations in production so that no station becomes a bottleneck, leading to high Work-In-Progress inventory and increasing idle time. The following general procedure according to Fig. 6.2 is suggested.
Before starting with line balancing measures, it is necessary to capture the current, non-optimized production process (Step 1, actual analysis).
Only then will the two essential measures for line balancing begin. On the one hand, waste in the sense of the 7 (or 8) types of waste must be recognized and ideally eliminated. In addition, work redistribution (cycling) is then carried out to adapt all workstations to the required customer demand. In a final step, it is recommended to standardize the implemented improvements/changes to ensure the sustainability of the measures [1]. |
| TOPIC-035 | Line Balancing | Actual Analysis | Lean Six Sigma > Line Balancing > Description of the Method > Actual Analysis | To analyze the actual situation, it is necessary to analyze the value chain or process chain [6]. This includes the temporal recording of cycle times per activity, the number of activities at each workstation, and the number of workstations. The own Overall Equipment Effectiveness (OEE) must be known. In addition, customer demand is also absolutely necessary. These terms are explained in the following [1]. |
| TOPIC-036 | Line Balancing | Activities | Lean Six Sigma > Line Balancing > Description of the Method > Actual Analysis > Activities | Activities refer to all the steps an employee needs to perform his work. This includes active work, but also, for example, walking distances. Therefore, every single action must be recorded in terms of time. Accordingly, all activities are divided into three categories [7]:
* value-adding activities (e.g., turning, welding, screwing),
* necessary but non-value-adding activities (e.g., set-up, emptying containers),
* non-value-adding activities (e.g., waiting, searching, rework).
The correct time recording per activity is done per manufactured single piece. For example, a housing must be screwed for each finished product, and this activity takes 30 s. |
| TOPIC-037 | Line Balancing | Customer Cycle | Lean Six Sigma > Line Balancing > Description of the Method > Actual Analysis > Customer Cycle | The customer cycle is the ratio between the available production time and the customer order quantity. The customer cycle thus represents the time limit for each process. If the time is above the customer cycle, a bottleneck occurs. If the time is below the customer cycle, the opposite results. More is produced than the customer needs, leading to overproduction [1]. |
| TOPIC-038 | Line Balancing | OEE – Overall Equipment Effectiveness | Lean Six Sigma > Line Balancing > Description of the Method > Actual Analysis > OEE – Overall Equipment Effectiveness | The OEE reflects a key figure that combines the number of units, speed, production time, and quality. As a key figure, the OEE (Overall Equipment Effectiveness, Total Plant Effectiveness) provides information about the total losses and makes them visible to the employees. In order to work with the OEE, the optimum for the plant must be defined beforehand. This must run without interruption, must not lose any quality, and must always work at the highest possible speed. With this target value, the degree achieved by the real plant can be compared and thus the effectiveness can be determined [8]. |
| TOPIC-039 | Line Balancing | Cycle and Takt Time | Lean Six Sigma > Line Balancing > Description of the Method > Actual Analysis > Cycle and Takt Time | The actual analysis is particularly about the correct time recording of the individual cycle and takt times. Takt time is understood as the time for a single activity per part at a workstation. The cycle time describes the time in which a finished part leaves the work system or a workstation. It thus describes the complete run per part.
In Line Balancing, it is about determining the required cycle time. The required cycle time is the necessary customer takt to meet the customer demand, considering the own total plant effectiveness (OEE).
A customer takt of, for example, 100 s means that a finished part must leave the work system every 100 s in order to be able to meet the customer demand. In practice, however, no plant runs continuously without loss and at full effectiveness, so the OEE must be taken into account in the calculation to compensate for the "loss factors". In this way, the required cycle time can be determined in order to still be able to maintain the customer takt. To compensate for the losses over time, the actual required cycle time is always lower, since an OEE of 100% is almost impossible in the real environment and thus losses always have to be compensated [1]. |
| TOPIC-040 | Line Balancing | Work Distribution Diagram | Lean Six Sigma > Line Balancing > Description of the Method > Presentation of Analysis Results > Work Distribution Diagram | The work distribution diagram (AVD) is suitable for displaying the times of individual work processes at the workstations. A column with the individual tasks is displayed for each workstation. The tasks are then color-coded into value-adding (green), non-value-adding (red), necessary (yellow), and periodic tasks (blue). Figure 6.3 graphically illustrates the structure of a work distribution diagram.
In Fig. 6.3, the *upper dashed line* corresponds to the Customer Takt and the *lower line* to the required Cycle Time. It can be seen that some stations are significantly above the required times and some are even below. The goal of Line Balancing is to adjust the workload per station to the required cycle time, but at least below the customer takt. |
| TOPIC-041 | Line Balancing | Operation List | Lean Six Sigma > Line Balancing > Description of the Method > Presentation of Analysis Results > Operation List | The operation list is a tabular enumeration of operations of the entire work process [9]. It contains all operations listed in the Project Structure Plan. Each operation is assigned a letter. In addition, a predecessor is determined for each operation, i.e., the previous activity that is the prerequisite for the start of the respective operation must be determined. Furthermore, a duration is assigned to each operation. The operation list forms the basis of a network plan. It clarifies parallel work aspects and the overlap between work packages or time intervals [9]. The following Fig. 6.4 shows this graph.
Process Activity Time [min] Predecessor
A Process 1 4 -
B Process 2 8 A
C Process 3 10 A
D Process 4 2 A, B |
| TOPIC-042 | Line Balancing | Network Planning Technique | Lean Six Sigma > Line Balancing > Description of the Method > Presentation of Analysis Results > Network Planning Technique | After breaking down the manufacturing process into various process steps or operations and listing these operations in the Operation List, the network planning technique follows.
Here, *circles* are labeled with letters that are supposed to represent the operations. These are then connected with *arrows* depending on the order. A *rectangle* with the corresponding duration is then drawn on each *circle* or operation. The network planning technique describes the temporal and final chaining of actions. It illustrates the order and duration of these operations. Figure 6.5 shows a Network Plan. |
| TOPIC-043 | Spaghetti Diagram | Classification of the Method | Lean Six Sigma > Spaghetti Diagram > Classification of the Method | To analyze and illustrate waste (“Muda”) in an existing process, in addition to the value stream analysis, the so-called spaghetti diagram (also spaghetti chart) can be used. The spaghetti diagram is part of the tools for process analysis [1].
Thus, the diagram is used to represent material flows in order to eliminate the types of waste “transport” and “movement” and thus create a process that is as lean as possible. The method primarily supports the goal of reducing throughput times and thus increases the functional flexibility of the production system (Fig. 7.1). |
| TOPIC-044 | Spaghetti Diagram | Description of the Method | Lean Six Sigma > Spaghetti Diagram > Description of the Method | The starting point in process analysis using the spaghetti diagram is the layout of the work area. Therefore, it is important to define a clearly selected area for analysis. Once a sketch of the floor plan has been created, the process can be observed. Here too, a so-called “Gemba Walk”—a Japanese term meaning “the real place”—is suitable for capturing the process. The objects of observation can be the distances covered by the employees, but also the paths of the materials within the production process or even the flow of documents within a process. The application of this process analysis creates a high level of transparency within the existing process. This reveals efficiency losses due to the distances covered by the employees, but also losses caused by a suboptimal layout. The distances covered are drawn into the diagram by lines in the existing layout. The efficiency loss is thus usually made visible by very tangled lines in the diagram. These unproductive sequences must then be eliminated using various measures [1–3]. |
| TOPIC-045 | Spaghetti Diagram | Application of the Spaghetti Diagram | Lean Six Sigma > Spaghetti Diagram > Application of the Spaghetti Diagram | The following six steps are required to visualize the spaghetti diagram and efficiency losses (Fig. 7.2).
1. Definition of the local dimension—Define: In the first step, a work area to be analyzed should be defined. Care should be taken to ensure that the process to be considered has a clear start and end point and that this is ideally located in a clearly defined work area. If a slightly larger work area is chosen, which extends over several halls, for example, it makes sense to divide the diagram into two individual diagrams, as it otherwise becomes too complex. Once the work area is defined, the layout can be recorded. It is advisable to work as true to scale as possible. Existing drawings of the floor plans (e.g., factory layout) should be used for this. Furthermore, it is always necessary to conduct a walk-through on site (Gemba). Only here can the exact dimensions be checked and any changes that were not listed in the drawing be uncovered. The scale drawing allows not only the conclusion in which area the efficiency losses occur, but also allows an exact measurement [2].
2. Definition of the temporal dimension—Define: After the location has been defined, it is necessary to determine the temporal dimension. This should also be precisely defined in advance. The observation period must be chosen so that a clear statement about the process can be made in the analysis. If the observation period is too short, not enough information is recorded and therefore no reliable statement about the efficiency of the process is possible. Furthermore, in production companies that operate in shift work, it is necessary to extend the observation period to the various shifts. Different colors can be chosen to draw the lines, so that it is recognizable in the analysis which paths were taken by which shift. This opens up the possibility of comparing the two groups in the analysis, in order to eliminate possible efficiency losses between them [2].
3. Determination of the observation object—Define: Furthermore, in this step, the object to be analyzed must also be defined. For example, should a material be analyzed through the respective process steps or should the paths of the employees be recorded? The previous definition of the observation object is intended to reduce the later complexity.
4. Drawing of the process flow—Record: Once the temporal and spatial dimensions are defined, the layout is created and the observation object is defined, the drawing of the paths taken into the layout can begin. It is important to draw all the paths taken into the diagram exactly. Even if paths are taken twice, they must be recorded in the diagram. This may seem confusing, but it is essential for the later evaluation and uncovering of waste.
5. Evaluation of the spaghetti diagram—Analyze: The scale layout allows a qualitative as well as quantitative assessment of the current process flow and its efficiency in the evaluation. One sign of waste occurring within the process can be the distance traveled, which is determined by the quantitative analysis. For this, the distances drawn into the layout are read off due to the scale drawing. Another method to identify waste is the qualitative evaluation. This is done based on the lines drawn into the layout. An indicator is a high frequency of lines, long path lines, and frequent crossing of lines. If the visual evaluation shows a very tangled diagram, this is often a sign of a high degree of waste [2].
6. Define measures—Perform: After the diagram has been evaluated quantitatively and qualitatively, measures must be defined to free the process from waste and thus design a process that is as efficient as possible. A table can be used for this, in which the measures to be carried out are prioritized. It is often advisable to classify the measures according to their integration effort and to implement the so-called “quick-wins” directly. If changes to the layout are also planned, these should be implemented at a later point in time and possibly re-evaluated after a further analysis, after the “quick-wins” have been implemented.
7. Repetition—Iterate: The last step is to conduct another recording of the process to check the implemented measures. Even with this repeated process recording, it is advisable to record it to scale. This allows the measures taken to be evaluated quantitatively and the increase in efficiency to be clearly measured. The step of repeated recording is particularly important, as often an improvement of the process on one side can lead to a deterioration on the other side. |
| TOPIC-046 | Spaghetti Diagram | Advantages and Disadvantages of the Spaghetti Diagram | Lean Six Sigma > Spaghetti Diagram > Advantages and Disadvantages of the Spaghetti Diagram | The biggest advantage of the diagram is that no prior knowledge is required. The user can start recording immediately after drawing the layout. Furthermore, no prior knowledge is required for the evaluation. The diagram simply shows where waste occurs. This is also another major advantage of the diagram. It visualizes the process and, above all, its execution for the user in the best possible way. This way, waste can be eliminated directly in the process and, if necessary, faulty executions of the process (e.g., incorrect routes) can be eliminated. Another advantage that the Spaghetti Diagram offers is the focus on the two types of waste “Transport” and “Motion”. These two types of waste can be specifically eliminated. A major disadvantage of this diagram is the quickly occurring lack of clarity. If larger processes are analyzed or many routes have to be covered within the process, the diagram can often be difficult to evaluate. Therefore, the Define phase is a very important step to clearly delineate the process to be considered and its object of observation, thus reducing the lack of clarity to a minimum [3]. |
| TOPIC-047 | Value Stream Analysis | Classification of the Method | Lean Six Sigma > Value Stream Analysis > Classification of the Method | The value stream analysis is a method that has its roots in the Toyota Production System (TPS). The method means seeing the whole in order to improve the whole. The focus here is on the whole, meaning that analysis should also be carried out outside of production in order to gain a holistic understanding of the situation and opportunities for improvement. Thus, value stream analysis can enable a holistic transparent representation of the processes, with the aim of eliminating waste and thus significantly improving the responsiveness of production as well as increasing the profitability and efficiency [1–3].
Value stream analysis therefore primarily focuses on optimizing throughput times while simultaneously increasing the flexibility of the production system in the manufacture of different products according to customer specifications (Fig. 8.1). |
| TOPIC-048 | Value Stream Analysis | Description of the Method | Lean Six Sigma > Value Stream Analysis > Description of the Method | When creating a value stream analysis, it is necessary to start with a categorization of the prevailing products. If possible, a product or a product family should be chosen that needs to be analyzed in the production process. This should be followed by a customer demand analysis, which can be carried out based on the sales figures of the past fiscal year. In the next step, the actual value stream recording in production can begin, after which potential improvements can be analyzed (Fig. 8.2) [4]. |
| TOPIC-049 | Value Stream Analysis | Product Family Formation | Lean Six Sigma > Value Stream Analysis > Product Family Formation | Before starting with the value stream analysis, it must first be determined which product is to be analyzed. A value stream is always a link of the processes for exactly one product. If many different products, which take different paths through production, were drawn into a value stream analysis, this would lead to an overlay of connections in which nothing can be recognized anymore. To prevent this, the subdivision of the product spectrum according to production-relevant similar criteria must begin. This results in the product families. These are a segment that is separated from the factory and analyzed. To create such product families, the use of a product family matrix or the evaluation based on the production process/product family similarity is recommended [1]. |
| TOPIC-050 | Value Stream Analysis | Customer Needs Analysis | Lean Six Sigma > Value Stream Analysis > Customer Needs Analysis | The overarching goal of value stream analysis is to orient production towards the customer demand. For this, the customer perspective must be adopted in the analysis. This means that after defining the product families, the customer must be analyzed. The customer cycle helps in aligning the production rhythm and sales rhythm. The cycle brings the market feeling into production and makes the production rhythm transparent. The cycle time should always exactly match the customer cycle, as too high a time leads to non-fulfillment of customer demand and too short a time leads to overproduction. The customer cycle is the beat that is dictated by the market and with which production should work as best as possible [4]. The customer cycle can be calculated as follows [4]:
The calculated customer cycle and the resulting transparent production rhythm assume that there is not a high fluctuation in demand. If demand fluctuations occur, this places high demands on the flexibility of production. Flexibility can often only be achieved by decoupling production from the customer cycle by creating stocks. However, it is also possible to initiate upstream measures. For example, sales can influence ordering behavior through quantity and time-limited discounts [4]. |
| TOPIC-051 | Value Stream Analysis | Value Stream Recording | Lean Six Sigma > Value Stream Analysis > Value Stream Recording | The first step should be to start recording the material flow. The process is generally carried out upstream. Therefore, the recording starts with the customer and continues in the opposite direction to the actual material flow. The second step is to record the information flow. This should start at the customer order acceptance, as this represents the direct interface to the customer [5].
The recorded times are entered on the jump line, which is located under the drawing. This line consists of two levels. The upper level is used to describe the material flow using the storage range, and the lower level is used to describe the process using the processing time. At the end of the timeline, the total throughput time and the sum of the processing times are entered. The timeline allows an evaluation regarding the maximum achievable and the actual existing throughput time. A large distance from the actual to the theoretical throughput time leads to high inventories, which often cause problems with the logistical target specifications (delivery time, deadline compliance). If the throughput time is considered in relation to the processing time, a statement can be made about how much of the processing time the object under consideration has spent in the production system. This value serves as an assessment of the extent to which flow production has already been implemented [4, 6].
A second analysis, the cycle-oriented view, allows an assessment of the Degree of Coordination of the production units. The Cycle Coordination Diagram can be used as a tool here (Fig. 8.3) This allows the difference between the theoretical cycles and the actual cycle times to be represented. The Cycle Time of a process indicates the time requirement per piece and thus the capacitive performance of this process. The smaller the cycle time, the greater the capacity. Thus, the capacity offer can be represented by the cycle times, using a bar chart, over the entire Value Stream. In addition, the Customer Cycle can also be entered to visualize where capacities may be lacking and where they are sufficiently available. The largest bar in the diagram is the bottleneck of the line, as it determines the maximum possible output. The diagram results in a Capacity Profile of the value stream [4, 7]. |
| TOPIC-052 | Value Stream Analysis | Potential Analysis | Lean Six Sigma > Value Stream Analysis > Potential Analysis | In the potential analysis, waste in the value stream should be made visible and eliminated. Wastes are activities that do not contribute to the value enhancement of the product. From the Toyota Production System and according to Taiichi Ohno, wastes can be divided into seven categories. These are [8–10]:
* Waste due to overproduction: This means that the quantity produced exceeds the quantity demanded. Overproduction is one of the most serious wastes as it conditions the others. Overproduction can, for example, result from too high batch sizes.
* Waste due to inventories: High inventories lead to increased capital commitment and an increase in storage or parking space. Furthermore, high inventories conceal problems that are prevalent in production. This can, for example, be caused by a wrong production strategy or lack of overview/transparency within production and the associated poor control possibility.
* Waste due to transport: Transport often arises due to spatial separation of successive production steps or due to necessary intermediate storage due to downtimes. Causes include a poor layout, among other things.
* Waste due to movement: This is caused by unnecessary distances covered by the employee. This can be caused by poor ergonomics at the workplace and the associated frequent rotation of the body or by a secondary activity, such as placing a container.
* Waste due to waiting times: Waiting times often arise due to lack of material and machine downtimes. These often cause an uneven degree of utilization of employees in upstream or downstream process steps. A common reason is also poor takt time of the processes, which can be made visible in the takt alignment diagram.
* Waste due to the production process: These are wastes that can, for example, be caused by too long setup or travel distances. But also the setup time counts as non-value adding activities to the wastes within the production process.
* Waste due to errors: These are faulty parts that may have to be reworked in an additional step or completely removed from the production process. |
| TOPIC-053 | Kanban | Classification of the Method | Lean Six Sigma > Value Stream Analysis > Kanban > Classification of the Method | Muda describes any activity that consumes resources but does not create value, therefore the goal of any efficiency increase of a process is to minimize Muda. In manufacturing processes, the Just-In-Time manufacturing (JIT manufacturing) is desirable. This requires that the right parts in a flow process must be available at the right time, in the required quantity, at the right place [1]. This can be ensured with the help of a Kanban system (Fig. 9.1).
The system is now a globally used control method. The reason for this popularity lies in the reduction of complexity, low susceptibility to interference as well as decentralization and the associated reduced control effort within production [2]. It ensures that production runs smoothly in the sense of lean management with minimal throughput times and high production flexibility [3]. |
| TOPIC-054 | Kanban | Description of the Methodology | Lean Six Sigma > Value Stream Analysis > Kanban > Description of the Methodology | The Kanban system was developed by Ohno in 1950. It is the oldest principle of coordinated, self-regulating work systems. The Kanban system is often described in literature as the supermarket principle. As soon as a product is taken from the shelf, the resulting gap must be filled again. This view can also be transferred to production. If a part is consumed by a process, a gap is created. The upstream process must then ensure that the gap is filled as quickly as possible. This creates a clearly recognizable customer-supplier relationship [4].
The basic model of the Kanban control in parts production consists of a linear arrangement of workstations to a Kanban line. Each workstation has a buffer in the form of an outbound store. The information flow runs backwards along the Kanban line. When a customer order is received, this information is passed on to the first process where the raw material is located. The material flow, on the other hand, runs forward until the required product, demanded by the customer order, is completed. When an order is received, it can be served in the first step from the finished goods warehouse. The gap that arises there must be filled according to the supermarket principle and thus triggers a production order to the upstream workstation. The activities of generating and consuming the parts are continued until the first process of the chain [4].
The difference to the Push system is that in the Kanban (=Pull system) only the removed quantity is refilled. The Kanban cards serve the information flow between the individual control loops. The following two basic types of Kanban can be distinguished (Fig. 9.2):
* The Production Kanban circulates exclusively between the source and the Buffer storage. The cards contain data regarding the containers, the transport routes (from the source to the sink), the delivery time as well as the parts information [4]. They trigger production orders at the source [5].
* The Transport Kanban, on the other hand, circulates between the source and Buffer storage. It triggers a transport of parts to supply the consuming point from the buffer storage. If the supplier is also included in the Kanban system, the Kanban card takes over the function of the order form [5]. |
| TOPIC-055 | Kanban | 1-Card System | Lean Six Sigma > Value Stream Analysis > Kanban > 1-Card System | The basic model of the Kanban consists of a 1-card system. This is particularly suitable when the distance between two consecutive processing stations is so small that the output warehouse of the first process can be merged with the input warehouse of the following one. In the system, there is only one card that takes on two functions. On the one hand, transport and on the other hand, production. If a workstation removes a full container from the upstream buffer storage, the production kanban card attached to the container is passed on to the upstream process or placed in a collection box located in the buffer storage. The cards from the collection box must then be collected by an employee. The card triggers a production order and the removed quantity, with the corresponding card, is refilled in the buffer. This restores the initial state [6]. |
| TOPIC-056 | Kanban | 2-Card System | Lean Six Sigma > Value Stream Analysis > Kanban > 2-Card System | The 2-card system is mostly used when a container has to be fetched from a far-off place or when the transport quantity of containers differs from the quantity of the production order [4]. Here, the cards are differentiated into transport and production kanban (Fig. 9.3) [7].
If a place has consumed a container, it must be refilled from the preceding buffer storage. The starting point of consideration here is the consumer, the so-called sink. As soon as a container has been emptied, the employee removes a transport kanban from the designated collection box and goes with the empty container and the card to the buffer storage. There, he places the container in the designated place. In the next step, the employee removes a full container. Before the container can be transported to the sink, he must exchange the production kanban attached to the full container with the carried transport kanban and pay attention to the match of the information on both cards. The removed production kanban must now be placed in the collection box provided at the buffer storage. An employee of the source collects the cards from the collection box at short time intervals, which then triggers the production. The empty containers are transported to the source and are filled as a result of the production order and then provided in the buffer storage [5]. The transport kanban regulates the information flow and the production kanban the material flow [4]. |
| TOPIC-057 | Kanban | Conditions for a Kanban System | Lean Six Sigma > Value Stream Analysis > Kanban > Conditions for a Kanban System | For a manual Kanban System to work successfully, several aspects must be considered and adhered to. It is particularly important to define a high quality standard and to maintain this standard through suitable quality assurance measures, as it must be prevented that faulty parts enter the Kanban container and are transported to the next process. Another aspect that must be considered is that production may only be carried out due to a demand from the upstream process. This means that production should only be initiated by receiving a Kanban Card. In addition, only the exact quantity that is requested according to the card should be produced to avoid overproduction. The last important condition that should prevail for the system to work successfully is that the entire production must work in a standardized and stable manner. If there are frequent machine failures during production, this can result in the subsequent processes no longer being able to be supplied according to their needs. Thus, production can come to a complete standstill [3]. The prerequisites can be summarized as follows [8]:
* The material flow must correspond to the flow principle in order to avoid strong demand fluctuations. If these cannot be prevented, this leads to high demand peaks that cannot be covered by the Kanban containers and the material flow breaks off.
* In order to produce economically with a high variety of variants, short setup times are essential.
* A high level of quality control is necessary to avoid delivering faulty parts to the downstream process, so that no supply gaps occur due to the low stocks [4].
* It is recommended to produce variants or similar products that have a similar sequence of processing steps in order to keep the setup effort low [4]. |
| TOPIC-058 | Kanban | E-Kanban | Lean Six Sigma > Value Stream Analysis > Kanban > E-Kanban | It has already emerged that there are some deficiencies in traditional Kanban with regard to transparency, material booking and the lack of connection to the IT system [9]. The rapidly developing information and communication technology offers very good conditions for the Kanban System. Information can be transmitted digitally. For this purpose, physical Kanban Cards are still used, but they contain a barcode. By scanning this code, the data can be read out and transferred to the system for recording incoming and outgoing parts. The reproduction is controlled by the stock in the system [10]. In addition, the economic efficiency of the container sizes can be checked [11]. The principle is identical to the reorder point system known from procurement planning [10]. With an E-Kanban board, the information regarding the quantity of empty or full containers in circulation can be viewed digitally in the internal network through terminals located in the company. With the IT connection of the Kanban, a simpler supplier connection can also be implemented. As soon as a container in the system is set to the status empty, an order is sent. When a full container is accepted, it can be scanned and thus directly registered in the system. If the data is updated daily, this results in enormous advantages for the supplier. The supplier can use the data to precisely analyze consumer behavior, which in turn leads to shorter replenishment times [12]. The advantage of the E-Kanban system is a (almost) paperless and faster flow of information. By registering the current stocks in the system and the resulting accurate material consumption booking, Kanban orders can be better prioritized depending on the order situation. In addition, scanning the barcodes provides accurate documentation of the parts and therefore also a very good possibility of product tracking [9], which is becoming increasingly important in today’s times. The E-Kanban can be used using other techniques for automatic identification and data capture (Auto-ID) such as “Radio Frequency Identification” (RFID). |
| TOPIC-059 | Kanban | Signal Kanban—Kanban Board | Lean Six Sigma > Value Stream Analysis > Kanban > Signal Kanban—Kanban Board | A variant of the Kanban system is the formation of batch sizes and the resulting bundling of orders. The idea is not to trigger production as soon as an empty container arrives, but to wait until a critical amount of orders is reached. The most common way to implement this is the traffic light system. A board is divided into three different zones: a green, yellow, and red area. Each part gets a column, which starts with red at the bottom and ends with green at the top. Incoming Kanban cards are pinned to the board. When enough cards are collected to reach the green area, production begins. If the cards are only in the yellow area, in the middle, it is up to individual decision whether the order should be executed depending on the workload. It is important to note that a sufficient quantity of full containers must be kept in the buffer storage to serve the incoming orders. This in turn requires storage space equivalent to the bundled batches, and can therefore only be used if there is a small number of different end products. The advantage of the Kanban board is the visualization of the control impulses of the material flow and the transparency thus created [4]. |
| TOPIC-060 | Kanban | Visualization in the Kanban System | Lean Six Sigma > Value Stream Analysis > Kanban > Visualization in the Kanban System | Visualization in the production principle is an important component. It enables self-control and presents the services provided well for the employees. This allows them to directly identify with their performance. It serves as motivation to achieve the defined goals, as well as the process of continuous improvement (CIP) [13].
Increased transparency prevents *waste*, increases productivity, and enhances the competitiveness of the company.
The flow of information provided to the employee has a tremendous impact on job satisfaction. Visualization helps align the actions, thinking, and behavior of employees with the company's defined goals [13]. |
| TOPIC-061 | Kanban | Dimensioning | Lean Six Sigma > Value Stream Analysis > Kanban > Dimensioning | The central question for the design of a Kanban system is:
How many Kanbans, i.e., control elements, must be put into circulation to achieve reliable material availability? [14]
The number of cards depends on several parameters. There is the quantity of parts or the content per Kanban, and the replenishment quantity. It must be clearly defined whether a single production or a collection in batches takes place. Other aspects are the replenishment time and a necessary safety stock [14]. The inventory should be large at the introduction of the system and can then be reduced step by step, e.g., in the sense of Kaizen [4]. This increased inventory in the initial phase, however, ensures that the unproductivity of one’s own company and the suppliers can be compensated [3]. Then, a safety factor should be included in the design of the system. However, in the sense of the Lean concept, this is a waste and should be reduced to 1 as quickly as possible. The last parameter is the initial inventory. This represents the starting size and is always reached when production has not produced for a longer period of time [14]. The number of Kanbans can be calculated as follows [14]:
In case of fluctuating consumption, the average consumption should be replaced by a value for the maximum consumption to gain additional security in the design. Before the system can be introduced, it should be tested through a simulation [14].
Footnotes:
1. RT = Replenishment time; SS = Safety stock.
SF = Safety factor; PK = Parts per Kanban.
= Average consumption. |
| TOPIC-062 | Kanban | Summary | Lean Six Sigma > Value Stream Analysis > Kanban > Summary | In summary, it can be stated that the Kanban system and the resulting self-regulation of production significantly reduce planning and control effort. In addition, the responsiveness of production can be greatly increased [9]. A high supply security of the material can be guaranteed with minimal stocks. Furthermore, the Kanban system is a simple, easily understandable system that shows a high level of employee involvement [15]. If there is a disruption at the workplace or with the operating resources, this usually leads directly to a standstill in production. In addition, strong demand fluctuations cannot be compensated by the Kanban system [15]. |

## Fuente: Kb gn meyer org structure koda
### Manifest
#### Urn
urn:knowledge:gorenuble:core:gestion:meyer-org-structure:1.0.0
#### Title
Principle-based Organizational Structure
#### Federation
#### Visibility
internal
#### License
Institutional Use
#### Compatibility
#### Min consumer version
1.0.0
#### Breaking changes from
null
#### Resolution
#### Canonical url
file://knowledge/core/gestion/kb_gn_meyer_org_structure_koda.yml
#### Mirrors
#### Dependencies
#### Requires
| urn | reason |
| --- | --- |
| urn:knowledge:koda:core:spec:1.0.0 | KODA/Spec format compliance |
| urn:knowledge:koda:core:transform:1.0.0 | Transformation methodology reference |
#### Provenance
#### Created by
KODA-TRANSFORMER
#### Created at
2026-01-29
#### Last modified at
2026-01-29
#### Signature
null
### ID
MEYER-ORG-STRUCTURE-KODA-01
### Version
1.0.0
### Status
Draft
### Format
KODA/Spec
### Human Creator
S/D (fuente: meyer.md)
### Human Editor
FS
### Model Collaborator
GPT-5.2
### AI Remediator
KODA-TRANSFORMER
### Creation Date
2026-01-29
### Modification Date
2026-01-29
### Source
/Users/felixsanhueza/Developer/_workspaces/diagnostico_dgi/complement/meyer.md
### Ctx
Transformación KODA de alta densidad del documento "Principle-based Organizational Structure" (meyer.md).
### Warn
Contenido derivado de fuente potencialmente protegida por copyright; uso interno; verificar derechos antes de redistribuir.
### XRef Required
urn:knowledge:koda:core:spec:1.0.0
### XRef
urn:knowledge:koda:core:transform:1.0.0
### LLM Parsing Instructions
#### ID
KODA-LLM-PARSER-01
#### Req
Mandatory block following Metadata.
#### Prohib
Using for artifact creation or translation.
#### Content
BEGIN_LLM_INSTRUCTIONS
You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).

LEXICON (expand before processing): Act->Action, Cond->Condition, Ctx->Context, Ctx_Required->Required External Reference, Ctx_Optional->Optional External Reference, Def->Definition, Ex->Example, Mssn->Mission, Obj->Objective, Proc->Process, Purp->Purpose, Ref->Reference, XRef->Cross-Artifact Reference, XRef_Required->Mandatory Cross-Artifact Reference, Req->Requirement, Res->Result, Src->Source, Prohib->Prohibition, Warn->Warning, Just->Justification, Rec->Recommendation

REFERENCE POLICY: Ref: internal only—must point to existing ID within THIS document. XRef/XRef_Required: external only—must point to a URN (optionally with #ID fragment) in another artifact. External documents without specific ID use Ctx:, Ctx_Required:, or Ctx_Optional:.

LANGUAGE POLICY: Keywords in English, content in original language. Never translate content.
END_LLM_INSTRUCTIONS

### Metrics
#### Source Chars
230054
#### Artifact Chars
269846
#### CR
0.853
#### FS
100% (estructura preservada; contenido telegráfico preservado)
### Principle Based Organizational Structure
#### ID
MEYER-DOC-01
#### Title
Principle-based Organizational Structure
#### Sections
-
  #### ID
  MEYER-SEC-0001
  #### Title
  0. Document Overview
  #### Text
  Purp: Provide handbook for engineering entrepreneurial thinking and teamwork into organizations of any size.
Dest: Leaders, executives, managers responsible for organizational design.
Nat: Engineering science applied to organizational structure.
-
  #### ID
  MEYER-SEC-0002
  #### Title
  1. Core Thesis
  #### Text
  Mssn: Enable leaders to design high-performance organizational structures based on scientific principles.
Fnd: Organizational structure is engineering science with firm principles and constructs.
  #### Sections
  | ID | Title | Text |
  | --- | --- | --- |
  | MEYER-SEC-0003 | 1.1. Fundamental Premise | - Cpt: Organizational Machine.
  - Def: Organization as machine that either achieves vision or frustrates ambitions.
  - Src: Sergio Paiz observation: "Most managers focus on operating poorly designed machine, struggle with it, rather than stepping back and redesigning machine."
  - Ex: Google case.
    - Ctx: Bill Coughran, senior vice president of engineering, led group from 2003 to 2011 that built Google's "engine room".
    - Ctx: Knew Google File System (GFS) would have to be replaced within couple of years.
    - Obj: Build organization capable of innovating continually over time.
    - Fnd: Role of leader of innovation not to set vision and motivate others to follow it; to create community willing and able to generate new ideas.

- Cpt: Three Strategic Vectors.
  - Def: Great leaders pursue three parallel strategic vectors.
  - Cpt: Market Vector. Def: Alignment with customers.
  - Cpt: Technical Vector. Def: Product/service capabilities.
  - Cpt: Organizational Vector. Def: The machine itself.
  - Ctx: This document addresses organizational strategy. |
  | MEYER-SEC-0004 | 1.2. Power of Structure | Purp: Establish structure as most powerful element of organizational design.

- Cpt: Key Elements of Organizational Design.
  - Def: Structure, culture, resource-governance processes, methods, metrics.
  - Cpt: Structure Primacy. Def: Structure is most powerful of all elements.

- Cpt: Structure Definition.
  - Def: Organization chart defining everybody's domains, and processes combining those specialists on teams. |
-
  #### ID
  MEYER-SEC-0005
  #### Title
  2. Benefits and Symptoms
  #### Sections
  | ID | Title | Text |
  | --- | --- | --- |
  | MEYER-SEC-0006 | 2.1. Benefits of Healthy Structure | - Res: Individual accountabilities for results clear; people deliver results.
- Res: Staff focused on excellence in single profession; perform better.
- Res: Staff customer focused; relationships with clients improve; organization well aligned with clients' needs and strategies; synergies across clients' businesses discovered.
- Res: Teams form spontaneously; work well together in flexible, well-defined processes tailored to needs of specific projects and services.
- Res: Organization delivers commitments reliably, more quickly, with lower risk.
- Res: Costs competitive; redundancies eliminated; internal entrepreneurs accountable for offering best value.
- Res: Product quality increases; product line better integrated.
- Res: Staff creative and entrepreneurial; pace of innovation in every discipline improves.
- Res: Organization great place to work; staff empowered; conflicts of interests eliminated; jobs don't expect impossible.
- Res: Structure lasting; not designed around incumbent personalities; defines accountabilities for all domains (current and future); automatically evolves as strategies and technologies change.
- Res: Well-designed organizational structure contributes directly to shareholder value (mission of organization). |
  | MEYER-SEC-0007 | 2.2. Symptoms of Poor Structure | - Warn: Unclear individual accountabilities for results; staff task or process (rather than results) focused; confusion about who does what; redundant efforts; territorial disputes; internal competition.
- Warn: Poor performance; people going too many ways at once; jobs too big for most people to succeed; need for all "A players".
- Warn: Lack of customer focus; weak or strained relationships with clients; initiatives product or technology (rather than business) driven.
- Warn: Difficulties with cross-boundary teamwork; slow response to new challenges; organization of independent "silos".
- Warn: Slow or unreliable delivery.
- Warn: High costs; lack of concern for frugality; empire building.
- Warn: Poor quality; poorly integrated product line.
- Warn: Lack of entrepreneurial spirit; staff not creative; don't take initiatives to improve functions.
- Warn: Lagging in innovation; lack of accountability for planning and creating future.
- Warn: Low morale and motivation; disempowerment; dead-end jobs; cynicism; stress.
- Warn: Repeated restructurings, each fixing some problems and creating others.

- Res: Unhealthy structure not "supplier of choice" to customers (internal or external), nor "employer of choice" to staff.
- Res: Stressful place to work; tough organization to lead; takes lots of attention to keep running right; little time for strategic thinking. |
-
  #### ID
  MEYER-SEC-0008
  #### Title
  3. Science of Structure
  #### Text
  Fnd: Organizational structure is engineering science, not matter of personalities, politics, personal style.
  #### Sections
  | ID | Title | Text |
  | --- | --- | --- |
  | MEYER-SEC-0009 | 3.1. Definition of Science | Def: Observation, identification, description, experimental investigation, theoretical explanation of phenomena.
Src: American Heritage Dictionary.
Nat: Applied science with firm principles and constructs.
Ctx: Organizations are systems; present engineering challenge. |
  | MEYER-SEC-0010 | 3.2. Evolution of Science | Proc: Real-world empirical observations revealed patterns, generalized to principles and frameworks, tested over decades of actual implementation experiences.
Res: Principles now so clear that one can look at any organization chart and know who's fighting with whom, who's not making objectives, who has ulcers. |
  | MEYER-SEC-0011 | 3.3. Common Guidance Without Science | Ctx: When executives don't study science of structure, reorganizations guided by:

- Incumbents' personalities and careers; attempts to work around managers who don't do essential aspects of jobs.
- Overly simplistic models (like "build versus run") or industry fads (like matrix).
- Client pressures (such as groups dedicated to them).
- Today's work, priorities, strategies.
- Intuition.

Res: Structure evolves through series of incremental changes by different executives, each with own philosophies and exigencies; resembles patchwork quilt of mismatched pieces. |
  | MEYER-SEC-0012 | 3.4. Reasons to Study Science | - Cpt: Avoid Organization du Jour.
  - Def: Without guiding principles, each restructuring solves some problems while creating others.
  - Warn: Never-ending, painful, costly series of disruptions; staff endure endless stream of unsettling changes; little real difference in way things work; costs but few benefits.
  - Res: Science helps engineer organization charts systematically, making deliberate decisions about key trade-offs.
  - Res: Structure performs well at multitude of challenges; doesn't cause unintended consequences.
  - Res: Principle-based structure dynamically adapts to changes in world; lasting investment; repeated reorganizations not required.

- Cpt: Easier to Explain.
  - Res: Makes it easier to explain how things supposed to work.
  - Res: Easier for staff to understand; more likely to make it work as intended.
  - Res: With clear principles, executive can invite participation from leadership team without fear of endless haggling and parochial politics.
  - Res: Participation takes advantage of people's in-depth knowledge; builds deep understanding; engenders tremendous commitment.

- Cpt: Don't Blame People.
  - Fnd: Leaders have moral obligation to study science of structure.
  - Just: Critical to know difference between poorly performing person and good person in poorly designed job.
  - Ex: University case.
    - Ctx: Growing accredited university; Sondra hired to enhance corporate "outreach".
    - Obj: Encourage corporations to utilize University as part of professional development programs (sales function).
    - Obj: Build "School of Continuing Studies" to deliver continuing education to non-traditional students.
    - Res: Sondra good at sales; pulled together existing corporate-outreach staff; gave them sales training; developed sales objectives and dashboard; increased revenues by nearly $4 million in one year.
    - Warn: Sondra failed at second objective.
    - Ctx: President hoped she would sell University's current course offerings to new audiences, perhaps repackaging into smaller programs for badges or certificates, or defining new paths to existing degree offerings.
    - Req: To do this, Sondra would have to bring opportunities to rest of University (who already knew how to put together programs and deliver education) and coordinate enterprisewide initiatives.
    - Res: Instead, Sondra came up with own plan, as if setting up parallel school; plan inconsistent with University's processes; not feasible.
    - Cause: Coordinating enterprisewide initiatives is challenging job in own right, requiring competencies quite different from sales.
    - Cause: Sondra's failure not because she was poor performer (sales success proved this); because structure gave her two very different jobs; no one could be expected to excel at both.
    - Res: President studied science of structure; saw real problem before firing great sales leader.
  - Warn: Futile and cruel to blame people for poor performance when structure is root cause of problems.
  - Req: To know difference, need to understand science of structure.

- Cpt: New Levels of Performance.
  - Res: Principle-based structure can perform far better.
  - Src: Preston Simons, CIO at Aurora Health Care, former CIO at Abbott Laboratories.
  - Ctx: Led organizations ranging from hundreds of employees regionally to thousands globally; implemented these principles of structure in each case.
  - Res: Powerful, yet pragmatic approach consistently leads to improved role clarity; better teamwork; customer focus; entrepreneurship; improved performance; commitment.
  - Res: Uses principles as forensic tool for insights about inherited structure.
  - Res: Provides basis for participative change process allowing leadership team to contribute knowledge and build organization they truly understand and support. |
-
  #### ID
  MEYER-SEC-0013
  #### Title
  4. Insufficiency of Alternative Approaches
  #### Sections
  -
    #### ID
    MEYER-SEC-0014
    #### Title
    4.1. Great People Alone Not Enough
    #### Sections
    | ID | Title | Text |
    | --- | --- | --- |
    | MEYER-SEC-0015 | 4.1.1. Common Argument | - Cpt: Informal Organization Argument.
  - Def: Working relationships formed despite structure, creating "informal organization" that really determines how things get done.
  - Cpt: Conclusion. Def: Success depends simply on hiring and developing great people who work hard, work well together, "do what's right" for organization.
  - Res: Leads to designing organizational structures around unique talents or career needs of key executives. |
    | MEYER-SEC-0016 | 4.1.2. Problems with This Approach | - Cpt: Problem 1: Constant Restructuring.
  - Def: Must restructure organization whenever anyone changes jobs.
  - Cause: Successive managers, each with own unique talents, find carefully tailored jobs impossible to fill.
  - Res: Each restructuring disruptive and expensive; repeated reorganizations do little to improve effectiveness; reinforce belief that structure doesn't matter (self-fulfilling prophecy).

- Cpt: Problem 2: Fragility.
  - Def: Organizations depending only on great people require leadership teams that work so well together that structure doesn't matter.
  - Req: People look past own job descriptions and personal interests for good of organization.
  - Warn: Altruism not natural; not reliable process.
  - Res: Organizations fragile; require charismatic leader and tightly knit, dedicated leadership team; generally fall apart when executive who created team or key members leave (or get tired).

- Cpt: Problem 3: Impracticality.
  - Def: Organization depending on everyone being "great" is impractical.
  - Warn: Organization requiring everyone above average difficult to staff (can't always afford best, may not be available); limited in growth potential (can only hire so many super-achievers). |
    | MEYER-SEC-0017 | 4.1.3. Reality Check | - Cpt: Truth About Great People.
  - Def: Superior people who work well with peers, motivated by inspiring leader, willing to work long hours and set aside own best interests (and those of staff) to do what's best for organization, can overcome most structural dysfunctions.
  - Warn: If structure poorly designed, inordinate amount of leaders' time, energy, goodwill spent resolving confusion and friction rather than doing real work.
  - Rec: Rather have great people focus precious time and energies on achieving great things than dealing with self-imposed obstacles which can (and should) be fixed.

- Cpt: Structure as Powerful Force.
  - Ex: Large airline case.
    - Ctx: Large airline divided IT department into two computer centers: business systems and reservations system.
    - Ctx: Operations director tasked with keeping critical systems running efficiently, safely, reliably.
    - Ctx: Systems-engineering manager reported to operations director.
    - Res: Business systems group retained expensive old mainframe; systems-engineering manager failed to innovate; fired.
    - Res: Two years later, successor fired for same reason.
    - Res: Two years after that, another systems-engineering manager fired.
    - Ctx: All three managers bright, experienced people good at their professions; problem wasn't their lack of ability.
    - Cause: Operations director paid to keep things running efficiently, safely, reliably; rewarded for stability.
    - Cause: Innovation inevitably disrupts operational stability.
    - Res: Systems-engineering manager set up to fail.
  - Warn: No matter how good people may be, structure is powerful force.
  - Warn: If structure causing people to do wrong things, then "better" people will just do wrong things faster.

- Cpt: Conclusion.
  - Def: Great people in bad structure will fail, or at least not perform to potential.
  - Def: Normal bell-curve of people in healthy structure can succeed.
  - Def: Great organizations are, by design, those where average people can succeed, and super-achievers can super-succeed. |
  -
    #### ID
    MEYER-SEC-0018
    #### Title
    4.2. Great Processes Alone Not Enough
    #### Sections
    | ID | Title | Text |
    | --- | --- | --- |
    | MEYER-SEC-0019 | 4.2.1. Common Argument | - Cpt: Process Engineering Argument.
  - Def: Carefully engineered business processes are key to success.
  - Def: As long as everybody does their part in well-designed processes, organization will perform well. |
    | MEYER-SEC-0020 | 4.2.2. Problems with This Approach | - Cpt: Problem 1: Process Effectiveness Depends on Structure.
  - Def: If nobody specializes in given discipline, processes depending on that competency will fail.
  - Req: Organization chart must provide groups dedicated to every needed discipline.

- Cpt: Problem 2: Structure Can Override Processes.
  - Def: Sometimes processes ask people to do things at odds with job descriptions.
  - Cond: When staff caught between conflicting forces, they'll optimize performance appraisals, even if some processes fail.
  - Res: Always easy to blame others involved in process for failure.

- Cpt: Problem 3: Rigidity.
  - Cond: Predefined processes only make sense when work highly structured and routine.
  - Ctx: Most organizations require much more than people performing routine tasks on predefined assembly-line.
  - Cond: In functions where projects have unique requirements, where flexibility and innovation critical components of success, simply giving everybody clearly defined role in carefully engineered process makes organization more rigid and less creative. |
    | MEYER-SEC-0021 | 4.2.3. Conclusion | Def: Great people working with great processes can't perform well unless structure they live in is well designed. |
  -
    #### ID
    MEYER-SEC-0022
    #### Title
    4.3. Structure Drives Performance
    #### Text
    Fnd: Structure is foundation on which good people and processes thrive.

- Cpt: Performance Impacts.
  - Def: Structure is one of most powerful drivers of organization's performance: efficiency, effectiveness, agility, quality, creativity, innovation, competitiveness, customer satisfaction.

- Cpt: Staff Impacts.
  - Def: Structure is key element of staff's competence, job satisfaction, motivation, commitment, happiness, loyalty.
-
  #### ID
  MEYER-SEC-0023
  #### Title
  5. Seven Fundamental Principles
  #### Text
  Fnd: Seven Principles provide foundation for science of structure.
Ctx: Principles illustrated by case studies; IT organizations used as examples (largest and most complex internal support function, offers rich microcosm of companies as whole).

| Principle   | Statement                                                                                                                                       |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Principle 1 | Golden Rule: Authority and accountability must match.                                                                                           |
| Principle 2 | Specialization and Teamwork: You can only be world-class at one thing at a time; but you can't specialize if you can't team.                    |
| Principle 3 | Precise Domains: Define clear boundaries with no overlaps or gaps.                                                                              |
| Principle 4 | Basis for Substructure: Divide function into groups based on what it's supposed to be good at.                                                  |
| Principle 5 | Avoid Conflicts of Interests: Don't expect people to go in two opposing directions.                                                             |
| Principle 6 | Cluster by Professional Synergies: Cluster groups under common boss based on similar professions.                                               |
| Principle 7 | Business Within a Business: Every manager is entrepreneur whose job is to satisfy customers (internal and external) with products and services. |
  #### Sections
  | ID | Title | Text | Sections |
  | --- | --- | --- | --- |
  | MEYER-SEC-0024 | 5.1. Principle 1: Golden Rule - Authority and Accountability Must Match | Def: Authorities and accountabilities must match.
Nat: Most important principle; absolutely essential to success of every organization. | [{'ID': 'MEYER-SEC-0025', 'Title': '5.1.1. The Golden Rule Statement', 'Text': 'Req: Authorities and accountabilities must match.'}, {'ID': 'MEYER-SEC-0026', 'Title': '5.1.2. Consequences of Violation', 'Text': 'Cond: If authorities and accountabilities separated, serious problems inevitably arise.\n\n- Cpt: Authority Without Accountability.\n  - Def: Person with authorities but not matching accountabilities becomes unconstrained tyrant.\n  - Mech: Such people can make decisions without bearing consequences; can tell others what to do while others held accountable for results.\n  - Res: Little to stop them from issuing edicts that may not be practical, then letting others take blame when commands backfire.\n  - Res: Without checks and balances, they do as they please.\n\n- Cpt: Accountability Without Authority.\n  - Def: Those with accountabilities but insufficient authorities are disempowered and can\'t get jobs done.\n  - Fnd: People cannot be held accountable for results if they don\'t have resources and authorities necessary to achieve those results.\n  - Warn: Trying to hold staff accountable for things they can\'t control won\'t lead to good performance; only establishes scapegoat to blame when things go wrong.\n  - Res: Over time, disempowered people adopt helpless "victim" mentality, take no initiatives, spend time reading Dilbert and laughing about how futile it is to try to accomplish anything important.'}, {'ID': 'MEYER-SEC-0027', 'Title': '5.1.3. Case Studies', 'Text': '- Ex: Process Owners Case.\n  - Ctx: CIO appointed "process owners" at suggestion of process-improvement consultants.\n  - Ctx: Each assigned process engaging people from various parts of organization in producing specific service.\n  - Ctx: Process owners had authority over processes; had final say.\n  - Warn: Process owners didn\'t have matching accountability for effectiveness of processes (not always ones accountable for delivering services).\n  - Res: Process owners had authority without accountability; everybody else had accountability without authority.\n  - Res: If service-delivery groups failed, no way to know whether due to their own poor performance or due to bad process; nonetheless, they took blame.\n  - Res: Process owners implemented detailed, rigorous processes; succeeded at their mission.\n  - Res: Organization became bureaucratic, slow, inflexible.\n\n- Ex: CFO Mandates Others\' Budgets.\n  - Ctx: In many companies, budgets determined by Chief Financial Officer.\n  - Ctx: CFO held accountable for company\'s financial targets, but not for business results.\n  - Mech: To achieve goals, CFO cuts others\' budgets with little regard for impacts on business.\n  - Res: CFO rewarded for cost savings, not blamed for poor performance caused throughout rest of company.\n\n- Ex: Customer Service Held Accountable for Resolving Incidents.\n  - Ctx: Industrial products company.\n  - Ctx: Customer-service manager held accountable for resolving problems, not just coordinating resolution.\n  - Warn: Manager didn\'t have resources or authorities to solve many problems.\n  - Ctx: Those who created problems (production, shipping, billing, etc.) not held accountable for remediating them.\n  - Res: Resolution impeded; customers\' satisfaction suffered.'}, {'ID': 'MEYER-SEC-0028', 'Title': '5.1.4. Healthy Organization Model', 'Text': '- Req: Everybody is "process owner" for own products and services.\n- Req: Everybody accountable for frugality, not just CFO.\n- Req: Everybody accountable for resolving any problems they create, not just customer-service group.'}, {'ID': 'MEYER-SEC-0029', 'Title': '5.1.5. Empowerment', 'Text': "- Def: Empowerment means everybody accountable for own results, has authority over all information, resources, decisions needed to do jobs.\n- Prohib: Empowerment does not mean anarchy; not blank check whereby people can do whatever they please.\n- Def: With accountability comes equal measure of authority (and freedom).\n- Req: People must be given no more authorities than warranted by accountabilities.\n- Nat: Fixed-sum equation; if anyone has more authorities than accountabilities, somebody else has less (or they fight for control).\n- Just: Empowerment not just fad or nicety; absolute necessity in today's competitive business environment.\n- Just: Organizations can't afford to waste one iota of talents people have to offer; every bright mind has to be engaged in achieving success.\n- Just: Empowerment fundamental to employee motivation; people want to feel proud of work; hard to feel good if treated as child and told what to do all time."}, {'ID': 'MEYER-SEC-0030', 'Title': '5.1.6. Empowerment at Every Level', 'Text': '- Req: Empowerment not limited to senior managers; everyone (in every job, at every level, in every corner of organization) should be empowered to manage their piece of business, however large or small.\n- Cond: If subordinates inexperienced, not ready to take on very much on own.\n- Rec: Not to disempower them by telling them how to do jobs; rather, empower them in smaller chunks (series of small assignments, each within capabilities).\n- Res: Even relatively junior people can be empowered with authorities matching accountabilities; both equipped and motivated to succeed.'}, {'ID': 'MEYER-SEC-0031', 'Title': '5.1.7. Mandating "How" Instead of "What"', 'Text': '- Cpt: Implication of Golden Rule.\n  - Req: Organizations should hold people accountable for results, leave them free (within bounds) to decide how to attain those results.\n\n- Ex: SOx Compliance Waste.\n  - Ctx: Wallace, IT consultant, on last two projects (major ERP implementation programs in two different big companies).\n  - Src: Wallace claimed close to one-third of costs of these projects wasted in name of Sarbanes-Oxley (SOx) compliance.\n  - Def: 50 percent increase in project costs over what they otherwise would have been.\n  - Ctx: Not talking about costs of complying with SOx; saying companies could have complied to same degree at much lower cost.\n  - Ctx: One SOx requirement is documentation of IT\'s development and testing processes; additional work-products with cost.\n  - Cause: Waste resulted from requirement to do all IT documentation in specific way; both companies mandated use of specific documentation method (UML, Unified Modeling Language).\n  - Ctx: ERP systems well documented by vendors; documentation required by SOx would have been standard fare, much supplied by vendors.\n  - Warn: Vendors\' documentation doesn\'t fit neatly into required format; developing documentation in specific format extremely time consuming.\n  - Res: IT leadership drove costs sky-high when issued across-the-board edict dictating "how" as well as "what".\n\n- Ex: Project-Management Method.\n  - Def: Common example of disempowerment is requiring staff to use particular project-management method.\n  - Warn: Standard method may be too cumbersome for small, agile projects, or insufficiently robust for really complex projects.\n  - Res: If people perform poorly, unclear if their fault or fault of imposed method.\n\n- Cpt: Distinction.\n  - Def: Not disempowering to clearly define every aspect of "what," including artifacts like documentation and project status reports.\n  - Def: Is disempowering to require specific "how".'}, {'ID': 'MEYER-SEC-0032', 'Title': "5.1.8. Leader's Role in Empowered Organization", 'Text': '- Cpt: Golden Rule doesn\'t preclude managers from making decisions; they have authority because they have ultimate accountability for performance of their groups.\n\n- Cpt: Specific Authorities and Accountabilities of Leaders.\n  - Act: Decide rules of game (create organizational ecosystem: structure, resource-governance processes, culture).\n  - Act: Once right structure in place, adjust domains as needed, arbitrate boundary disputes, ensure teamwork occurring as it should.\n  - Act: Develop talent within group (recruiting, inspiring, coaching subordinates).\n    - Ctx: Coaching offered as advice which staff may or may not choose to follow.\n    - Cond: If staff forced to follow manager\'s "suggestions," then manager must share accountability for their results.\n  - Act: Manage performance (negotiating staff\'s objectives, giving frequent feedback, measuring results, deciding rewards, managing performance problems).\n  - Act: Manage commitments and resources (assigning work within group).\n  - Act: Coordinate shared decisions within group (decisions on common methods and tools, agreements on professional practices).\n  - Act: Make decisions where consensus cannot be reached.\n  - Act: Guide business and product (technology) strategies within group (recognizing that within group\'s overall strategies, entrepreneurs at next level empowered to determine own strategies).\n  - Act: Serve as diplomat, representing group to peers and superiors.\n\n- Cpt: Leader\'s Job Summary.\n  - Def: Create right environment, do everything possible to help subordinates succeed.\n\n- Cpt: Control in Empowered Organization.\n  - Def: Managing by results can give more, not less, control.\n  - Mech: Focus moves up from micro-managing subordinates to more leveraged level of orchestrating right results.\n  - Res: Instead of being cog in machine, leader becomes driver of machine.\n  - Res: Working at more strategic level good for organization and for career.'}, {'ID': 'MEYER-SEC-0033', 'Title': '5.1.9. Implications for Structure', 'Text': '- Req: Define jobs based on what people produce, not by how they do work (processes, methods, tools, tasks).\n- Req: Rather than language "responsible for doing" (tasks), job descriptions should be phrased in terms like "accountable for delivering".\n- Prohib: Never create job whose purpose is to disempower others.\n- Prohib: Don\'t create steering committees or process owners ("integrating managers") who constrain others\' prerogatives.\n- Rec: If concerned about teamwork, far better answer is to install systemic processes that align everybody\'s priorities and link them on teams without disempowerment.'}] |
  | MEYER-SEC-0034 | 5.2. Principle 2: Specialization and Teamwork | Def: You can only be world-class at one thing at a time; but you can't specialize if you can't team. | [{'ID': 'MEYER-SEC-0035', 'Title': '5.2.1. Case Study: Customer-centric Structure', 'Text': '- Ctx: CIO in large insurance company under pressure; business executives complaining about IT department\'s opacity, unresponsiveness, poor understanding of business strategies; frustrated couldn\'t control IT\'s priorities; didn\'t understand why many requests not being fulfilled.\n- Ctx: Trend toward decentralization; many business units started own little IT groups ("shadow IT"); groups existed because business units didn\'t want to do business with Corporate IT.\n- Act: CIO dedicated group to each client business unit; divided engineering staff among them; each group relatively self-sufficient, with all skills needed to deliver any applications requested by assigned business unit.\n- Ctx: Senior managers also served as primary liaisons to those business units.\n- Ctx: Structure: Janice (Sales and Marketing), Bill (Finance), Henry (HR and other Corporate functions), Eugene (Engineering and Manufacturing), IT infrastructure and operations.\n- Ctx: Client-aligned structure akin to decentralization, but with formal lines of reporting remaining within Corporate IT.\n\n- Cpt: Initial Success.\n  - Res: For while, structure seemed successful; Sales and Marketing clients felt IT more responsive to needs.\n  - Cause: Clients understood limits to resources (people in group) and could control priorities; more understanding when couldn\'t do everything.\n  - Res: Clients felt IT better understood their business; better partnership developed.\n  - Res: At first, clients happy and CIO felt less "heat" from executive peers.\n\n- Cpt: Problems Emerged.\n  - Warn: Client-liaison function part-time job; with big group to manage, didn\'t have much time to spend with clients; at best, provided point of contact; didn\'t add much value to clients\' strategic thinking.\n  - Warn: Faced conflict of interests; advice offered biased by capabilities of applications engineers in group; regardless of clients\' real needs, only delivered traditional applications.\n  - Warn: Engineering function sub-optimized; needed variety of technical specialists in group to satisfy clients\' needs; each technology sub-specialty scattered among various client-dedicated groups.\n  - Res: Limited professional exchange; when staff ran into technical challenges, might not have known someone in another group already figured out answer; even if heard of others\' work, peers busy with other priorities; costs rose and response times slowed as everybody reinvented solutions to common problems.\n  - Res: Little impetus for standards; people built systems optimal for specific clients, not for enterprise as whole; when company sought cost savings through consolidation ("rationalization") of applications, found it difficult; few existing applications could be used more broadly.\n  - Res: Structure reduced engineers\' ability to specialize; each group had to produce every type of application needed by clients; with reduced specialization, costs rose, quality suffered, response times slowed.\n  - Res: Pace of innovation slowed; couldn\'t hire expert in emerging technology when only enough demand for one person to be shared across whole enterprise; had to wait until demand grew to point where each business unit alone could justify headcount.\n  - Res: Business opportunities missed; didn\'t have specialists in web and mobile applications; missed opportunities to build customer loyalty.\n  - Res: Impacts extended beyond IT\'s performance; all clients needed information about money, customers, employees, products; over time, structure led to multiple general-ledger systems and multiple records for same customer; synergies lost.\n\n- Cpt: Conclusion.\n  - Res: Customer-aligned organization didn\'t deliver advantages of its size; performed no better than number of small decentralized groups.\n  - Res: Business unit executives demanded decentralization of applications engineering function, rightly pointing out little benefit to centralized reporting.\n  - Res: CIO failed to gain benefits of being one organization; organization didn\'t deserve to stay together because wasn\'t adding value.'}, {'ID': 'MEYER-SEC-0036', 'Title': '5.2.2. Why Organizations Exist', 'Text': '- Cpt: Fundamental Question.\n  - Def: Why would organization of 10, 100, or 1000 people perform any better than equal number of individuals scattered around enterprise or among small companies?\n\n- Cpt: Common Purpose Insufficient.\n  - Def: One obvious answer is people within organization work toward common purpose.\n  - Cond: For very simple tasks, might be enough; 100 individuals picking up trash along stretch of roadside may perform as well as 100-person organization; only have to agree on territories to avoid redundant work.\n  - Ex: 100 individuals, working independently, each trying to make cars; each would have to be expert in virtually every branch of design, engineering, manufacturing, etc.\n  - Warn: No one person can possibly know enough about all those professions to succeed.\n  - Res: Independent people agreeing to work toward common purpose solves problem of volume, but not of complexity.'}, {'ID': 'MEYER-SEC-0037', 'Title': '5.2.3. Cybernetic Variety', 'Text': '- Cpt: Human Mind Limitations.\n  - Cause: Reason found in limitations of human mind.\n  - Def: We can think only so many thoughts in day, read only so much, know only so much.\n  - Def: We have finite number of "brain cycles" each day.\n\n- Cpt: Cybernetics.\n  - Def: Study of dynamic systems (like thermostat that turns on heater when it gets too cold).\n  - Ctx: Organizations can be viewed as large, complex cybernetic systems.\n\n- Cpt: Variety Definition.\n  - Def: In cybernetics, term "variety" has special meaning.\n  - Def: Complexity inherent in system, multiplied by pace of activities (e.g., volume of work per day).\n  - Mdl: VARIETY = COMPLEXITY x PACE\n  - Def: Measure of throughput or bandwidth; amount and diversity of information confronting organization at any point in time.\n  - Res: As complexity increases, as volume increases, as time-frames shorten, variety goes up.\n\n- Cpt: Implication.\n  - Def: World around us swarming with immense variety, way too much for any one person to grasp.\n  - Def: We\'re all limited in our variety-processing abilities.'}, {'ID': 'MEYER-SEC-0038', 'Title': '5.2.4. Definition of Specialist', 'Text': '- Cpt: Three Choices for Finite Brain Cycles.\n  - Cpt: Choice 1: Generalist.\n    - Def: Know little bit about everything; proverbial "jack of all trades, and master of none".\n    - Res: Able to do many things, but none particularly well; never know enough about any one field to master it.\n    - Ctx: Describes many individuals working independently.\n  - Cpt: Choice 2: Extreme Specialist.\n    - Def: Focus all variety-processing abilities on one topic, learn virtually nothing about anything else.\n    - Res: Excel at that one thing; wouldn\'t be able to work well with others.\n    - Warn: This degree of specialization not practical.\n  - Cpt: Choice 3: T-shaped Specialist.\n    - Def: Focus on one profession, while still using some brain-cycles to know little about lots of things so as to be able to work well with others.\n    - Def: This "T-shaped" person is definition of practical specialist.\n\n- Cpt: Cybernetics Conclusion.\n  - Def: Cybernetics tells us people can only be world-class experts at one thing at a time.\n  - Ctx: May rotate among specialties in course of careers; but at any point in time, each must concentrate on single profession to master it.\n  - Def: Only T-shaped people can be really good at what they do.\n  - Src: Niels Bohr: "An expert is person who has made all mistakes that can be made in very narrow field".'}, {'ID': 'MEYER-SEC-0039', 'Title': '5.2.5. Why Organizations Exist - Answer', 'Text': '- Def: Organizations exist to allow people to specialize.\n- Mech: When T-shaped specialists in diverse range of fields work together, organization has both depth and breadth; can process more variety.\n- Warn: Organization of generalists performs no better than equal number of individuals.\n- Fnd: Whole point of forming organizations is to permit people to specialize.\n- Def: Within some practical limits, more that people specialize, better they (and their organizations) perform.'}, {'ID': 'MEYER-SEC-0040', 'Title': '5.2.6. Benefits of Specialization', 'Text': 'Src: Adam Smith described advantages of "division of labor" in 1776.\nFnd: By specializing, people gain deep knowledge of one discipline; study its ever-evolving methods and tools, stay abreast of innovations; by applying discipline many times in many different circumstances, specialists accumulate experience; get really good at what they do.\n\n- Res: Productivity: Specialists more efficient; increased productivity translates into cost savings.\n- Res: Speed: With all experience, specialists have ready answers; don\'t have to climb learning curve with each new challenge; know latest methods and technologies in field, which can leverage time; things get done faster.\n- Res: Quality: Specialists produce higher quality because they know how; products more usable, more capable, more maintainable, have lower life-cycle costs.\n- Res: Risk: People with more competence and experience deliver results more reliably, with fewer risks.\n- Res: Innovation: Specialists can keep up with literature; first to learn about emerging technologies and techniques; pace of innovation improves.\n- Res: Reduced stress: Specialists experience less stress; may be under pressure to produce lot, but confident of abilities; more productive, stable, happy.\n- Res: Motivation: With greater competence, easier to excel and rise up ranks in fields; specialists more valued in market than generalists; better career opportunities.\n\n- Cpt: Conclusion.\n  - Def: Specialists always outperform generalists.'}, {'ID': 'MEYER-SEC-0041', 'Title': '5.2.7. Concerns About Specialization', 'Text': '- Cpt: Practical Limits.\n  - Warn: Organizations can\'t afford to specialize to point of becoming "one deep" (dependent for critical services on just one individual).\n  - Warn: Person may become bottleneck; problems when takes vacation or leaves company.\n  - Rec: Sometimes cross-training can address this problem; in other cases, structure must define domains more broadly (sacrificing some specialization) to avoid groups of one.\n\n- Cpt: Job Narrowing Concern.\n  - Def: People do same thing, day after day (like on assembly line where people specialize in specific set of tasks).\n  - Warn: Narrow jobs disempowering, waste talent, demotivate staff.\n  - Def: Healthy specialization is not job narrowing.\n  - Def: Specialists do everything in their field of study: work with customers; deliver today\'s work; support past work; keep up with innovations; plan and develop future offerings; improve their processes.\n  - Res: As much job diversity in doing all that within one specialty as there is in doing little bit in many fields.\n\n- Cpt: Market Reality.\n  - Def: Market rewards specialists, not generalists.\n  - Warn: Some resist specialization to avoid accountability for excellence in any one thing; would be best suited to very small organizations, ideally "organizations" of one.'}, {'ID': 'MEYER-SEC-0042', 'Title': '5.2.8. Specialization Requires Teamwork', 'Text': '- Cpt: The Catch.\n  - Ex: Organization made of specialists, all very good at respective professions, but each acting independently without teamwork.\n  - Res: Would perform terribly; worse than collection of independent generalists.\n  - Cause: No one specialist sees big picture; collectively unlikely to get anything done.\n  - Def: More people specialize, more they become interdependent.\n  - Def: You can\'t specialize if you can\'t team.\n\n- Cpt: Gating Factor.\n  - Def: This often gating factor.\n  - Cond: If organization not good at cross-boundary teamwork (assembling just right mix of specialists onto teams, getting them to work well together), then must back away from specialization so groups are independent rather than interdependent.\n  - Res: Must sacrifice performance to avoid teamwork.\n  - Res: Leads to "silo" organization.'}, {'ID': 'MEYER-SEC-0043', 'Title': '5.2.9. The Silo Organization', 'Text': '- Cpt: Common Belief.\n  - Def: Some leaders believe only way to get people to work well together is to put them under common boss, who presumably will form teams and force staff to cooperate.\n  - Just: Citing Golden Rule, they add that to hold managers accountable for results, must give them authority over all needed resources.\n  - Res: Accept current, limited teaming capabilities of organizations; design structure to minimize interdependencies and "hand offs"; put all skills needed by function under its manager.\n\n- Cpt: Silo Definition.\n  - Def: Organization made up of groups that are self-sufficient and don\'t need to work together all that much (like bunch of vertical silos that never touch).\n\n- Cpt: Result of Silos.\n  - Def: Each profession scattered among various groups that need it.\n  - Res: Fragmentation reduces specialization; each member of that profession within each silo must cover entire profession.\n  - Res: Lower performance; benefits of specialization lost.\n\n- Cpt: Alternative.\n  - Def: Don\'t need to build silo structures to match authorities to accountabilities.\n  - Ex: Doing so like saying need to own own grocery store to control what you eat.\n  - Def: Just as managers have authority over external vendors, they can manage team-members in other groups who are assigned to them.\n  - Def: Antidote to silos is effective teamwork across boundaries.'}, {'ID': 'MEYER-SEC-0044', 'Title': '5.2.10. Implications for Structure', 'Text': "- Req: More people specialize, better they perform; don't design jobs for generalists, or expect people to be experts at too many things; jobs should be designed around well-focused specialties.\n- Req: Can't specialize if can't team well across boundaries; more willing to invest in cross-boundary teamwork, more can specialize (avoid silos of generalists) and better organization will perform.\n- Fnd: Organizations exist in order to allow people to specialize, which in turn depends on effective teamwork."}] |
  | MEYER-SEC-0045 | 5.3. Principle 3: Precise Domains | Def: Define clear boundaries with no overlaps or gaps. | [{'ID': 'MEYER-SEC-0046', 'Title': '5.3.1. Domain Definition', 'Text': '- Def: Organization chart determines everybody\'s "domains" (boundaries within which each group functions).\n- Warn: Sometimes group\'s domain defined only by few words in box; when different people interpret those words in different ways, three problems occur: overlaps, gaps, lack of focus.'}, {'ID': 'MEYER-SEC-0047', 'Title': '5.3.2. Case Study: Vague Domains', 'Text': '- Ctx: CIO put Rick in charge of "Infrastructure" group, Charlie managed "Enterprise Architecture" (EA).\n- Ctx: Charlie (Enterprise Architecture) believed his job was to design infrastructure; proposed cutting-edge technologies that weren\'t yet stable, but constituted elegant design.\n- Ctx: Rick fought that; looked bad when resisted innovation; but knew couldn\'t deliver reliable services with technologies not ready for production environment; ignored Charlie and designed own infrastructure.\n- Cause: Rick and Charlie didn\'t dislike one another; fought because they were paid to fight; both believed they had authority over design of infrastructure.'}, {'ID': 'MEYER-SEC-0048', 'Title': '5.3.3. Overlaps', 'Text': '- Def: Lack of clarity may cause multiple groups to think they\'re responsible for same function (overlapping domains).\n- Res: When domains overlap, staff fight and compete with one another.\n\n- Cpt: Intentional Internal Competition.\n  - Def: Some leaders create overlapping domains intentionally, thinking internal competition will elicit better performance.\n  - Def: Might argue it maximizes creativity, with different alternatives coming from various competing groups.\n  - Warn: Internal competition should never be needed.\n  - Just: Most companies face competition; in monopoly, not-for-profit, government organizations, external metrics (customer satisfaction, cost benchmarks) can keep people sharp.\n  - Just: For internal service providers, there\'s competition from vendors; nothing sacred; product development, manufacturing, sales, all support functions can be outsourced.\n  - Just: Another form of competition for internal service providers is decentralization (business units have own support functions rather than work with shared-services provider).\n  - Def: Don\'t need overlapping domains to motivate performance or creativity.\n  - Rec: If need for competitive performance not clear to staff, outsourcing or benchmarking study can serve as wake-up call, provide metrics of staff\'s competitiveness.\n\n- Cpt: Costs of Overlapping Domains.\n  - Warn: Reduced specialization: Splitting profession into multiple groups reduces specialization; costs include lower productivity, slower delivery, lower quality, greater risk, less innovation, more stress, lower motivation. Ref: ORG-STRUCT-PRINCIPLE2-BENEFITS-01.\n  - Warn: Redundant efforts: More than one group does same research, produces same kind of products; solutions reinvented rather than reused; wastes time and money, increasing costs.\n  - Warn: Less innovation: When two groups study same thing, something else that one might otherwise have explored is missed.\n  - Warn: Confusion: When two groups offer same service, customers don\'t know where to go for what; organization appears confused and inefficient.\n  - Warn: Product dis-integration: Multiple, incompatible versions of same product can undermine enterprise synergies; in engineering, overlaps may result in dozens of different fasteners (nuts and bolts) with essentially same purpose, increasing costs of manufacturing, inventories, support.\n  - Warn: Less teamwork: Internal competition may be friendly, limited to just part of staff\'s work; but inevitable friction undermines teamwork; no amount of team-building can overcome this force built into structure.\n  - Warn: Lack of entrepreneurship: Whenever single line of business fragmented, no one feels "ownership" as entrepreneur accountable for its performance, now and in future.\n\n- Cpt: Conclusion.\n  - Def: Whether by deliberately pitting people against one another or inadvertently leaving boundaries vague, internal competition is costly.\n  - Req: Good structure defines distinct domains, with no overlapping boundaries.'}, {'ID': 'MEYER-SEC-0049', 'Title': '5.3.4. Case Study: Gaps', 'Text': "- Ctx: In many fields, multiple layers of engineering, each building on lower layers.\n- Ctx: One IT department had applications development groups, but no groups dedicated to lower-layer technologies (other than infrastructure managed by Operations).\n- Ctx: Jim given responsibility for manufacturing and supply-chain systems; while working on just-in-time inventory management, studied electronic data interchange (EDI); as automated factory, learned lot about document management.\n- Ctx: Donna's financial applications group developed expertise in forecasting algorithms and reporting tools.\n- Ctx: Carey's customer applications group learned to quickly deliver small web applications and analyze masses of data company collected on customers.\n- Ctx: Structure: Jim (manufacturing and supply-chain applications plus EDI and document management), Donna (financial applications plus forecasting models and reporting tools), Carey (customer applications plus Agile development methods and big-data analytics), Operations.\n- Warn: Encouraged to share knowledge with one another; but rarely happened; managers allocated all resources to own projects; when Jim asked Donna for help with user-friendly reporting tool for inventory data, her staff too busy developing financial applications to work on his projects.\n- Res: Whenever needed technology missing (or just out of reach), people muddled through; multiple learning curves and replication of efforts costly; working outside one's expertise eroded performance, quality, reliable delivery.\n- Res: No single leader had job of ensuring comprehensive range of supporting technologies available; some critical new technologies ignored; business opportunities lost."}, {'ID': 'MEYER-SEC-0050', 'Title': '5.3.5. Gaps', 'Text': '- Def: When function is missing, gaps occur.\n\n- Cpt: Results of Gaps.\n  - Warn: Unreliable delivery: With no one thinking about function on daily basis, it\'s "catch as catch can" (done when need becomes urgent and obvious, or when people have spare time and happen to think of it); not reliable process.\n  - Warn: Reduced specialization: Staff filling gap outside their specialty aren\'t experts; don\'t have time to learn that other profession; costs described under Principle 2. Ref: ORG-STRUCT-PRINCIPLE2-BENEFITS-01.\n  - Warn: Overlaps: Gaps create overlaps; group that needs missing specialty fills gap, but only for itself since not its primary mission; in time, multiple groups fill same gap, creating overlaps.'}, {'ID': 'MEYER-SEC-0051', 'Title': '5.3.6. Focus', 'Text': "- Def: People naturally want to feel proud of their work.\n- Warn: When domains unclear, staff don't know what they're supposed to be good at; sense of direction becomes foggy; natural drive for excellence thwarted.\n- Res: May try to be good at too many things and become generalists; or may just follow personal interests, and gaps or overlaps occur unpredictably.\n\n- Cpt: Benefits of Clear Domains.\n  - Res: Give people focus they need to excel.\n  - Res: Tell people what literature, which conferences, which methods and technologies, what research to study.\n  - Res: Staff develop feeling of pride in their group's unique function; strive to do it well.\n  - Res: Clear domains basis for effective performance management; performance objectives and other metrics can be clearly defined only if jobs clearly defined.\n  - Res: Organization as whole requires clear domains to operate as planned; both customers and staff need to know where in organization to go for help they need.\n  - Res: Good structure provides crystal clear definitions of each group's domain; entire scope of organization divided among groups within it, with no gaps or overlaps, with clearly worded boundaries."}, {'ID': 'MEYER-SEC-0052', 'Title': '5.3.7. Case Study: Roles and Responsibilities', 'Text': '- Ctx: Traditional "roles and responsibilities" blur accountabilities and authorities.\n- Ctx: IT organization where applications-development process very confused.\n- Ctx: Aaron ran applications engineering group; "business analysts" in Mark\'s group worked with clients to define requirements and high-level designs; "project managers" reporting to Jay (PMO) responsible for large strategic projects.\n- Ctx: Structure: Aaron (applications engineering), Mark (business analysts), Jay (project management office PMO).\n- Ctx: Lot of friction; CIO instructed them to work out respective "roles and responsibilities".\n- Ctx: Answer: Aaron responsible for applications-development process; Jay decided project-management methods; promised they knew difference; Aaron defined projects for his group; Mark\'s analysts responsible for specifications and high-level designs; once specs and high-level designs done, Mark handed projects off to Jay\'s project managers (if big and "strategic") or to Aaron\'s group (for smaller projects); Jay and Aaron both responsible for project delivery; even for big projects Jay\'s PMO managed, Aaron had role (supplied engineers to do most of work); Aaron retained responsibility for maintenance and support of applications once deployed.\n- Res: CIO asked: "Who\'s responsible for project success?" Mark looked away; not his problem, even though analysts controlled critical step in process; both Aaron and Jay raised hands; if small project (enhancement to existing application), Aaron\'s group responsible; anything big deemed "strategic project" and Jay\'s PMO took over.\n- Warn: Delivery problems persisted; neither Jay nor Aaron could control resources needed to get job done; Jay pulled engineers out of Aaron\'s group to staff strategic initiatives; Aaron yanked engineers off Jay\'s projects to deal with urgent maintenance issues, putting Jay\'s projects in jeopardy.\n- Warn: Even small, urgent projects took long time; Mark chose requirements-planning method; Aaron chose meticulous development method which slowed projects; Jay decided project-management method (also slowed projects); three methods didn\'t mesh, required lots of paperwork for every hand-off; all three managers shared responsibility for overall process, but none had power to fix it.\n- Warn: Aaron\'s engineers, responsible for small projects, got little support from Jay\'s PMO staff who busy with big initiatives; project-management capabilities remained weak.\n- Warn: Aaron held accountable for long-term integrity of applications; but couldn\'t control all decisions that affected it; all made decisions that impacted quality of applications.\n- Res: All set up to fail, with overlapping accountabilities and without authorities needed to deliver results; even though divided up tasks, stepped on each other\'s toes and tensions rose.'}, {'ID': 'MEYER-SEC-0053', 'Title': '5.3.8. RACI Framework', 'Text': '- Def: RACI method sorts who has Responsibility for doing it, to whom they are Accountable, with whom they have to Consult, whom they\'re to keep Informed.\n\n- Cpt: RACI Problems.\n  - Warn: Responsibilities: Like simple roles and responsibilities, defines accountabilities for tasks and processes, not results.\n  - Warn: Accountable: Person with authority to make or approve decisions may or may not be customer; risks separating authorities from accountabilities.\n  - Warn: Consulted: RACI defines key contributors, but not their deliverables; they lack accountability for results; fixed list of contributors may not be right for every project.\n  - Warn: Informed: Fixed list may or may not be right stakeholders for every project; bureaucratic, not flexible and dynamic; people spend lot of time "consulting" and "informing," whether or not it adds value.'}, {'ID': 'MEYER-SEC-0054', 'Title': '5.3.9. Downside of Jobs Designed Around Tasks', 'Text': '- Warn: People execute tasks; not asked to think creatively about how to attain intended results; wastes insights of those in best position to know best way to get things done; tedious jobs lead to boredom and degrade morale.\n- Warn: Each group sub-optimizes (and perpetuates) its steps in current process; if tasks don\'t add up to intended results, not in position to fix it.\n- Warn: Boss who coordinates all tasks must plan every project in detail, monitor everyone\'s work, adjust tasks when things go wrong; busy managing tasks, doesn\'t have time to think about own challenges (building relationships, innovation, business strategies).\n- Warn: If project requires new task, may be nobody\'s job and hence task may not get done; puts ultimate deliverable in jeopardy.\n- Warn: When disempowered people interact with customers, both parties frustrated; customers ask for results that task-focused staff not able to offer; staff feel badly that can\'t satisfy customers.\n- Warn: People believe they\'ve done enough if put in required hours and completed tasks, whether or not job is done; go through motions, without caring (or even knowing) whether motions produce intended results.\n- Warn: When sorting tasks among groups, nothing to stop accidentally separating accountabilities and authorities.\n- Warn: Roles and responsibilities don\'t define accountabilities for leadership (improving methods and tools, sorting out processes and relationships with peers, exploring emerging technologies, selecting and managing vendors, developing strategies); doesn\'t appoint leaders responsible for managing today\'s business and planning tomorrow\'s.\n- Res: All adds up to unhappy customers and staff.\n- Def: Problem with "roles and responsibilities" is, can sort tasks in excruciating detail, and still won\'t know who\'s accountable for delivering organization\'s products and services.'}, {'ID': 'MEYER-SEC-0055', 'Title': '5.3.10. Domains Based on Results', 'Text': "- Def: Organizations don't make money by going through motions; make money by producing results.\n- Def: Key to good domains is bounding what people produce rather than what they do.\n- Res: Dividing up results actually lot easier than sorting tasks; list of organization's products and services far shorter than all tasks people do and roles they play.\n- Res: By defining who produces what, automatically know who does what.\n\n- Ex: Applications Manager Example.\n  - Ctx: Aaron is applications manager; accountable for entire portfolio of applications.\n  - Cond: If Aaron not clear about exactly what customer needs, may get help from Mark's business analysts; Mark's group produces requirements definitions, not product designs (not even at high level, since design is engineering task).\n  - Ctx: Once requirements clear, Aaron runs project; produces anything related to applications engineering (repair, enhancement, even major strategic initiatives); single point of accountability for all applications.\n  - Ctx: Jay is expert in project management, but that doesn't give him right to take over Aaron's projects; Jay sells Aaron project plans, training, project facilitation, project administration services; whether or not Aaron's engineers get help from Jay, still accountable for delivering projects, big and small.\n  - Ctx: Aaron's job to stay abreast of innovations in engineering methods; Mark continually refines requirements-planning methods; Jay runs consulting business and has to keep up with project-management methods and tools.\n  - Res: Since each group only produces results within its domain, boundaries clear; roles and responsibilities (and hand-offs) clear because everybody knows what they produce, for clients and for one another."}, {'ID': 'MEYER-SEC-0056', 'Title': '5.3.11. Implications for Structure', 'Text': '- Req: Provide every group with precisely worded boundaries.\n- Req: Ensure no overlaps; never create internal competition.\n- Req: Ensure no gaps; place every needed specialty within domain of one group.\n- Req: Domains should bound what people produce, not roles they play or tasks they\'re responsible for.\n- Req: Clear domains take more than few words in box on organization chart (vague phrases like "infrastructure" or "operations"); each box should be accompanied by carefully worded paragraph that clearly bounds what each group produces.\n- Res: Precise domains, defined by results, help people understand how structure supposed to work; clients know whom to call for what; staff better understand what\'s expected of them.\n- Res: Teamwork improves because everybody empowered to do what it takes to deliver their products and services; they know where to go for help when they need it.'}] |
  | MEYER-SEC-0057 | 5.4. Principle 4: Basis for Substructure | Def: Divide function into groups based on what it's supposed to be good at.
Ctx: Organization big enough to require multiple groups in essentially same profession; Principle 3 says domains defined by respective results; but how divide all various deliverables among those multiple groups? | [{'ID': 'MEYER-SEC-0058', 'Title': "5.4.1. Case Study: Structure by Clients' Business Processes", 'Text': '- Ctx: CIO viewed IT as means of supporting clients\' business processes; rather limited view; but at least wanted to focus staff on business rather than just technologies.\n- Act: Dedicated group to each of company\'s core processes; Gail given responsibility for corporate product-development process; Jerry looked after entire order-to-invoice process; Tom supported all company\'s financial and administrative processes.\n- Ctx: Structure: Gail (product-development process), Jerry (order-to-invoice process), Tom (financial and administrative processes).\n- Ctx: Each group expected to become familiar with workflows, design solutions that optimized these business processes.\n\n- Cpt: Problems in Practice.\n  - Warn: Redundant learning curves: Various processes all required many common skills; caused lot of parallel learning curves; under influence of innovative clients in R&D, Gail first to develop applications on then-new mobile devices; later, when Jerry embarked on sales-force automation project, his group had to research same technologies; while helped one another with advice, weren\'t able to flexibly deploy existing expertise to one another\'s project teams; staff still needed time for learning what others already knew; increased costs and delayed projects.\n  - Warn: Redundant work: Parallel efforts led to redundant work; both Gail and Jerry developed document-tracking modules; drove costs up further.\n  - Warn: Reduced specialization: Skills needed by multiple processes scattered among groups, reducing staff\'s ability to specialize; Gail and Jerry both needed expertise in product data; Jerry and Tom both worked on customer, sales, financial data; all three worked on human resources data; became specialists in clients\' business processes, but generalists with regard to own profession of engineering specific types of applications; performance naturally suffered.\n  - Warn: Product dis-integration: Each group independently developed own versions of financial, customer, product databases; fragmented data caused confusion when different reports gave clients conflicting views of "same" data; when did collaborate on few common applications and databases, other problems occurred; each enhanced same applications at various times; as result of "patch on patch," systems integrity deteriorated.\n  - Warn: Weak client relationships: CIO expected structure would bring IT closer to clients; however, not evident; most business units involved in numerous business processes; Manufacturing involved in both product development and production; thus, both Gail and Jerry served Manufacturing executives, focusing on different aspects of jobs; with no single point of contact for client like Manufacturing, appeared various IT groups competing for clients\' attention; IT appeared poorly coordinated; also meant clients had to determine which workflow wished to discuss before could know whom to call; IT\'s client liaisons not included in clients\' thinking early on, where real strategic discoveries made; furthermore, since processes touched multiple clients, IT managers couldn\'t focus on just one business unit; with more business units to cover, had less time to get to know people in each; also distanced IT from clients; finally, some clients weren\'t involved in any of core business processes; doesn\'t mean weren\'t important; top executives rarely engaged in routine business processes; clients such as president and executive vice president of planning and business development had no designated client liaisons, received poor service.\n  - Warn: Biased business diagnosis: Group dedicated to business process naturally biased in favor of automating that workflow; Gail, for example, paid to believe automating product-development process most important thing to do; however, corporate engineering function might have benefited far more from solutions that improve effectiveness of key individuals (e.g., engineering design tools) that have nothing to do with automating workflow; similarly, Manufacturing executive might be involved in critical decision, like consolidating plants, requiring decision support or collaboration tools (challenges that have nothing to do with any of chosen processes); due to bias for automating business processes built into structure, high-payoff opportunities missed.'}, {'ID': 'MEYER-SEC-0059', 'Title': '5.4.2. Basis for Substructure Definition', 'Text': "- Def: Way you divide domains among groups within profession is termed basis for substructure.\n- Def: Determines people's specialties (their bottom-of-the-T).\n\n- Cpt: Examples of Different Bases.\n  - Ex: If assign groups to clients' business processes, they'll become experts on those workflows, but generalists with regard to clients, their engineering disciplines, and services.\n  - Ex: If assign groups to clients (for internal service providers, business units; for companies, territories), they'll become very close to those clients while becoming generalists with regard to organization's products and services.\n  - Ex: If assign groups to technologies and disciplines (e.g., specific products), they'll become experts in those products while becoming generalists with regard to clients.\n  - Ex: If assign groups to services, they'll become experts in delivery of those services, while becoming generalists with regard to organization's clients and its products."}, {'ID': 'MEYER-SEC-0060', 'Title': '5.4.3. Consequences of Wrong Basis', 'Text': "- Warn: Reduced specialization: If basis for substructure anything other than function's expertise, then staff will specialize in something other than their primary mission; in case study, groups specialized in business processes, not in knowing clients or in their engineering profession; as another example, when Sales substructured by product lines (sales force within each business unit), specialization in clients' business reduced; since each Sales group must cover all clients, staff have less time with each client, get to know them less well; as per Principle 2, when specialization reduced, performance suffers: lower productivity, slower delivery, lower quality, greater risk, less innovation, more stress, lower motivation. Ref: ORG-STRUCT-PRINCIPLE2-BENEFITS-01.\n- Warn: Domain overlaps: At same time, inappropriate substructure often creates overlapping domains; if Engineers divided into client-dedicated groups, multiple groups deliver essentially same solutions to respective clients; often lot of reinvention; when Sales substructured by product line, clients confused by multiple points of contact, where have to call one person for some products and another for others; costs of overlaps described in Principle 3. Ref: ORG-STRUCT-PRINCIPLE3-OVERLAPS-01.\n- Warn: Inappropriate biases: Wrong basis for substructure can induce wrong biases; staff give poor advice, optimize wrong objectives; Sales force divided by product lines can't be trusted advisors to clients; recommendations always biased toward own product lines, not clients' real needs.\n- Warn: Disempowerment: Another problem occasionally resulting from inappropriate substructure is violation of Principle 1 (Golden Rule); two groups may fulfill essentially same function, one doing thinking (e.g., planning, or designing processes) while other does delivery; neither wholly responsible for results; costs of this disempowerment described under Principle 1. Ref: ORG-STRUCT-PRINCIPLE1-VIOLATIONS-01."}, {'ID': 'MEYER-SEC-0061', 'Title': '5.4.4. Implications for Structure', 'Text': '- Def: Organization chart defines everybody\'s specialties (their "bottom-of-the-T"); people concentrate on whatever their job\'s domain may be, become generalists at everything else.\n- Req: Use basis for substructure that exactly matches what people are supposed to be good at.\n- Ctx: There\'s no one right answer for entire organization; but for each specific function, specialty ("bottom of T"), and hence right basis for substructure, should be evident.\n- Ex: If want engineers to be good at designing things, define their domains by what they design; if job of Sales is to know clients, define their domains by clients they serve.'}] |
  | MEYER-SEC-0062 | 5.5. Principle 5: Avoid Conflicts of Interests | Def: Don't expect people to go in two opposing directions.
Ctx: To support empowerment, Principle 3 states groups' domains should be defined by results they produce; organization produces many different results; what goes best with what? What's right way to cluster set of results into group's domain? Two considerations: conflicts of interests (this Principle 5), and professional synergies (Principle 6). | [{'ID': 'MEYER-SEC-0063', 'Title': '5.5.1. Case Study: Governance and Client Liaison Group', 'Text': '- Ctx: IT organization found itself overwhelmed with unchecked demand coming from both clients and internal projects; needed to better manage process by which new work taken in; CIO also wanted to better align IT with clients\' business strategies by setting right priorities.\n- Act: Instead of addressing demand management and alignment through business-driven resource-governance processes, CIO put Martha in charge of "Governance" group; responsibilities included business relationship managers, demand management (deciding priorities among proposed projects), project portfolio management (PMO).\n- Ctx: Other groups responsible for project delivery and ongoing services.\n\n- Cpt: Martha\'s Conflicts of Interests.\n  - Warn: Had authority to decide project priorities; since not all benefits measured to point of calculating accurate returns (ROI), couldn\'t just go by numbers; had to judge merits of clients\' projects; conflicts with business relationship management role which attempts to be on clients\' side of table; will clients be open and trust people who will later judge merits of their requests?\n  - Warn: Similarly, judging internal projects proposed by peers undermines service orientation expected in project management function, which supposed to help peers deliver those projects.\n  - Warn: Since Martha\'s job was to limit demand to available resources, will business relationship managers be aggressive about seeking new high-payoff opportunities (which makes limiting demand more difficult)?\n  - Warn: Business relationship managers help some clients discover new opportunities; will projects that other clients define on own (without this group\'s help) get fair treatment when comes to setting project priorities?\n  - Warn: Will discovery process (which should be business driven and unbiased) recommend services as well as projects, despite bias toward projects coming from Martha\'s project-management function?\n  - Warn: Some high-payoff opportunities may be urgent; project-management function not going to like these disruptions to well-planned project schedule.'}, {'ID': 'MEYER-SEC-0064', 'Title': '5.5.2. Five Fundamental Conflicts of Interests', 'Text': 'Def: If put wrong deliverables together in single job, can inadvertently create conflicts of interests (two or more missions that are in some way opposed).\nDef: Five fundamental conflicts of interests inherent in all businesses, and in many organizations within enterprises.\n\n- Cpt: Conflict 1: Invention Versus Operations.\n  - Def: Invention (major innovations) versus operational stability.\n  - Def: Some managers find themselves responsible for both researching and developing new technologies (invention), and also for operating them; combining invention and operations may be attempt to give manager complete piece of business to run; however, misguided.\n  - Ex: George Case.\n    - Ctx: Manager given both infrastructure operations and infrastructure engineering responsibilities.\n    - Res: 6 months later, stabilized operations but holding up projects.\n    - Ctx: Working 60-hour weeks to document procedures; still had ways to go; hadn\'t started thinking about capacity planning, change control, disaster recovery, security administration; half day went into fire-fighting; last thing needed was another major application coming on-stream.\n    - Act: Decided once-a-month window for installing new applications would be more than ample; instituted lot more rigor around testing and quality control, even for small projects like enhancements.\n    - Res: Made great progress stabilizing operations, but innovation stopped.\n  - Ex: Telecommunications Cable Manufacturer.\n    - Ctx: Promising executive given responsibility for both business development (acquisitions) and operating acquired companies during transition into corporation.\n    - Res: After first major acquisition, CEO disappointed to find little done in way of new deals.\n    - Cause: Running and integrating acquired company required executive\'s full attention; after first big acquisition, had no time for new deals; by combining invention and operations, CEO left without business development function.\n  - Def: Term "invention" meant to imply creating entirely new things (developing new ideas, products, methods); special type of innovation, beyond marginal changes of continual improvement.\n  - Def: Invention is crux of this conflict of interests; any function can be innovative; but invention and operations antithetical.\n  - Cause: When one person asked to do both, not likely to find ideal balance; operational issues tend to take precedence; fire-fighting swamps invention; short-term problems take attention away from long-term opportunities; those who "keep things running" have little time for future-oriented invention.\n  - Cause: Not just matter of having time; invention not in their best interests; major changes threaten stability and efficiency of operations; operations staff will pursue innovation on margin (get better at what currently do); unlikely to pursue breakthroughs which inevitably disrupt operational stability.\n  - Ctx: Generally, conflict constrains invention; but cases where opposite true (under leader who prefers engineering, invention takes precedence; every new idea finds way into production, whether or not can be supported reliably; operations never stabilize).\n\n- Cpt: Conflict 2: Purpose-specific Solutions Versus Components.\n  - Def: Many organizations produce two different kinds of products: some purpose-specific, others components which may stand alone or be part of purpose-specific solutions (complete products versus parts that go into them).\n  - Ex: Construction industry: Some experts design buildings (architects), other experts design bridges (civil engineers); both draw on experts in common components (structural engineers, electrical engineers, traffic engineers).\n  - Ex: IT: Business applications purpose-specific; one team of developers may specialize in financial applications, another in customer applications; all different applications engineers draw on experts in component technologies (computing platforms, databases, middleware).\n  - Warn: If group expected to produce both purpose-specific solutions and component solutions, unhealthy bias built into organization chart; staff tend to put everything on familiar platforms.\n  - Res: Conversely, keeping them separate has advantages.\n  - Ex: PDC Bleach Operation.\n    - Ctx: PDC bought bleach operation with two factories; one factory produces hypochlorite (base chemical); sent to second factory which dilutes it and blends with fragrances to produce consumer bleach (application managed by Consumer Division).\n    - Res: Industrial Division quick to figure out hypochlorite used in several industrial applications like mining and agroindustry; distinguishing purpose-independent (base chemical) from purpose-specific (consumer bleach) products led to new source of revenues.\n\n- Cpt: Conflict 3: Enterprisewide Thinking Versus Focus of Specialist.\n  - Def: Some decisions (policies, plans, standards) are enterprisewide, affecting many different stakeholders.\n  - Warn: If these enterprisewide decisions assigned to any one of impacted domains, decisions will tend to be biased in favor of that one stakeholder; knowledge and interests of other affected groups may not be fairly represented.\n  - Ex: IT technology standards: Standards affect all IT applications and infrastructure domains, as well as operational services, customer support, in some cases even clients; if network standards decided by network engineers, may neglect interests of other engineers who must design systems compatible with network, and concerns of infrastructure services group accountable for running network.\n\n- Cpt: Conflict 4: Product Specialization Versus Unbiased Diagnosis of Clients\' Needs.\n  - Def: Technical excellence requires deep understanding of single domain (subset of organization\'s products and services).\n  - Def: Specialization brings quality, but also brings bias; bias not unhealthy, but rather natural outcome of dedicating career to particular specialty.\n  - Def: On other hand, when diagnosing clients\' needs, organization should be completely unbiased; must listen carefully to clients\' business challenges, prescribe most relevant subset of entire product line.\n  - Warn: If staff expected to do both, conflict of interests arises; as product specialists, should be biased; but when talking to clients, expected to provide unbiased, business-driven advice and "sell" whatever most needed.\n  - Warn: Impossible for people to be both biased and unbiased; as old saying goes, "Give child hammer, and everything looks like nail!" Despite best efforts to be objective, staff see only needs for their favored solutions; higher-payoff opportunities may be missed.\n\n- Cpt: Conflict 5: Service Orientation Versus Audit.\n  - Def: Primary mission of most functions is serving others (peers inside organization, clients throughout enterprise, or external customers); customer focus is key success factor.\n  - Def: May also be need for "audit" function which judges others, may even have veto-power over others\' decisions (e.g., auditors necessary to ensure compliance with financial laws, regulations, policies, ethics principles).\n  - Warn: Mixing audit functions with service functions creates conflict of interests; impossible to build relationship with customers while also judging them; just can\'t say, "I\'m from Internal Revenue Service; I\'m here to help!"\n  - Ex: IT example: Giving PC group power to decide whether users need new PC; clients wouldn\'t perceive them as service oriented, wouldn\'t openly discuss real needs.'}, {'ID': 'MEYER-SEC-0065', 'Title': '5.5.3. Consequences of Conflicts of Interests', 'Text': "Def: When structure tells individual to go in two (or more) opposing directions, adverse consequences both for organization and for individuals involved.\n\n- Warn: Gaps: Putting people in conflict-of-interests situations doesn't produce excellence at both missions; with finite brain cycles, people might be mediocre at both missions; more commonly, prefer one (based on predilections), and performance at other mission falls short; in George example, operations took precedence and infrastructure engineering (invention) became gap.\n- Warn: Unpredictable balance: Balance between conflicting missions not deliberate process, interplay among peers that analyzes trade-offs; people independently decide balance based on limited view of organization's needs, intuitions, personal preferences; as one manager leans one way and another in opposite direction, when decisions added up, statistics tells us tendency toward mean, regardless of needs of business at that time; meanwhile, organization's top executive has little control over balance; if organization needs to emphasize operational efficiencies to save money, or innovation to reap opportunities, top executive has no knob to turn; no explicit way to adjust balance on conflicting objectives.\n- Warn: Stress: More personal consequence is stress; when people expected to go in opposing directions, don't know what to do; typically fully aware of failure to succeed at both; highly stressful jobs lead to poor motivation, performance deficiencies, even health problems (like ulcers)."}, {'ID': 'MEYER-SEC-0066', 'Title': '5.5.4. Implications for Structure', 'Text': '- Def: Since organizations may face all these conflicts of interests, top executives inevitably must cope with these paradoxes and decide balance point on each.\n- Prohib: At lower levels, not healthy to combine functions with opposing objectives.\n- Req: Reserve conflicts of interests for highest possible level in organization chart, ideally for top executive alone.\n- Req: Healthy structure defines jobs that focus on only one side of each paradoxical dimension; gives staff clear, non-conflicting job objectives; allows executive to explicitly adjust balance by shifting resources between groups.'}] |
  | MEYER-SEC-0067 | 5.6. Principle 6: Cluster by Professional Synergies | Def: Cluster groups under common boss based on similar professions.
Ctx: As combine organization's many deliverables into domains, first consideration is avoiding conflicts of interests; second is professional synergies. | [{'ID': 'MEYER-SEC-0068', 'Title': '5.6.1. Case Study: Process-centric Groups', 'Text': '- Ctx: With some critical internal processes in need of attention, CIO tried process-centric structure; dedicated groups to each major process within IT to minimize "hand-offs".\n- Ctx: Structure included: Ruth (applications development process), Bob (infrastructure engineering process), Matt (incident management process), Art (operational service delivery process).\n- Ctx: Optimizing processes is good thing; but this structure created "silo" groups for each process, each containing various specialists it needed; scattered "campus" of similar professionals.\n\n- Cpt: Problems.\n  - Warn: With each group attempting to cover many engineering disciplines, all became less specialized, hence less effective; costs rose, quality suffered, pace of innovation slowed.\n  - Warn: Structure was disempowering; Art forced to operate whatever infrastructure Bob developed; accountable for service delivery, even though had only indirect control of own assets.\n  - Warn: Smaller, less-visible processes not represented in structure (business opportunity analyses, standards planning); since counting on organization chart to make processes work, these other critical processes languished.\n  - Warn: Structure sent wrong signals; staff focused on executing existing processes, not on running businesses and pursuing innovations in their professions.\n  - Warn: Technology experts scattered among various groups didn\'t coordinate professional practices (methods and tools); didn\'t share components; did poorly at product integration; both professional and enterprise synergies lost.\n\n- Cpt: Conclusion.\n  - Def: Structuring by internal processes extremely costly way to optimize workflows.\n  - Rec: If concerned about effectiveness of internal processes, process-facilitation function can help.\n  - Def: As long as willing to invest in processes and teamwork, no need to put diverse professions under common boss just to get them to work together.'}, {'ID': 'MEYER-SEC-0069', 'Title': '5.6.2. Clustering Similar Professions', 'Text': 'Fnd: If don\'t have to put people under common boss to get them to work together, then free to cluster staff by their professions.\nDef: Produces many kinds of synergies.\n\n- Cpt: Synergy 1: Professional Synergies.\n  - Def: Working together in same group encourages professional exchange (sharing experiences, discoveries, refinements of techniques, best practices).\n  - Res: Reduces redundant learning curves; everybody better informed; improves speed, quality, innovation; institutional knowledge better preserved by concentrating (rather than scattering) it.\n  - Res: Similar professionals can share work products; even if each project unique and solutions customized for each client, may be opportunities to reuse lower-level modules and designs; at minimum, staff can make use of others\' experiences.\n  - Res: Sharing in any of these forms saves time and money; common components may improve quality and maintainability of organization\'s products.\n  - Warn: Conversely, scattering profession destroys "campus effect"; people don\'t get together often enough to learn from one another; relearn and reinvent; wastes time and slows delivery; dampens pace of learning and innovation; reduces depth of expertise; result is lower productivity and quality, at higher cost.\n\n- Cpt: Synergy 2: Management Synergies.\n  - Def: Manager focused on set of similar professions better understands how to manage those specialists; better leader and mentor; can create sub-culture appropriate to profession.\n  - Warn: Conversely, when small group in one profession placed under manager of completely different profession, boss may not understand function well enough to lead it; mentoring weak; sub-culture may be inappropriate.\n  - Warn: With given profession reporting to multiple managers, less management control; harder to develop common methods and enforce professional standards.\n\n- Cpt: Synergy 3: Workload Synergies.\n  - Def: Larger pool of staff can better manage workloads; when one person or group becomes too busy, common manager can temporarily assign people from other closely related disciplines; since professional skills similar, reasonable chance loaned staff will be productive.\n  - Warn: When scattered about, little group of professionals under one manager finds it difficult to manage peak loads; hard to borrow people from group reporting to completely different manager.\n\n- Cpt: Synergy 4: Negotiating Power.\n  - Def: When profession consolidated, its manager has more buying power and can negotiate better deals from suppliers; group may also be able to save money by sharing tools (e.g., software licenses) and vendor services.\n  - Warn: When profession divided into multiple groups, each procuring own tools and services, buying power diminished.\n\n- Cpt: Synergy 5: Career Paths.\n  - Def: Single, larger group of all those in given profession offers better career opportunities; supervisory positions within that larger group may provide promotional opportunities for those excellent in profession.\n  - Warn: By contrast, when profession scattered into small groups under other functions, staff find it difficult to advance; positions at next level up may not benefit from their professional expertise; when look for career path, no place to go other than to leave their field of study behind.\n\n- Cpt: Synergy 6: Domain Adjudication.\n  - Def: Common manager overseeing collection of similar domains resolves boundary issues, ensures accountabilities for emerging technologies and disciplines assigned to one group; reduces chances of domain overlaps and gaps.\n  - Warn: If profession scattered around organization chart, groups may only meet at level of top executive; busy leader doesn\'t have time to personally adjudicate domains, or ensure every new sub-specialty covered somewhere, without overlapping domains; result typically domain overlaps and gaps; Principle 3 described problems. Ref: ORG-STRUCT-PRINCIPLE3-OVERLAPS-01.\n\n- Cpt: Synergy 7: Simplicity.\n  - Def: Putting similar professions in one place makes it easier for others to understand structure and find source of needed products and services.\n  - Warn: When profession scattered, harder to know where to go; creates confusion for clients as well as others in organization.\n\n- Cpt: Synergy 8: Product Synergies.\n  - Def: When similar professionals collaborate more, organization\'s products likely to be better integrated; can produce enterprise synergies (e.g., when clients collaborate better by using common tools and services).\n  - Ex: When all IT engineers who work on customer applications in one group, more likely to create systems that allow all enterprise\'s business units and functions to share holistic view of customers.\n  - Warn: Alternatively, if pieces of profession report to many different managers, tendency for each group to go own way; for lack of collaboration, organization\'s products don\'t fit well together (product dis-integration); silo structures tend to produce monolithic products, not modular, interoperable product line; increases costs and sacrifices enterprise synergies.'}, {'ID': 'MEYER-SEC-0070', 'Title': '5.6.3. Implications for Structure', 'Text': '- Req: Cluster domains based on professional synergies (not who works with whom).\n- Req: Put all staff who share common profession together under common boss.\n- Fnd: If trust that will build processes of cross-boundary teamwork, no need to cluster functions based on who works with whom.\n- Req: Cluster similar specialties to maximize professional synergies.'}] |
  | MEYER-SEC-0071 | 5.7. Principle 7: Business Within a Business | Def: Every manager is entrepreneur whose job is to satisfy customers (internal and external) with products and services.
Ctx: Seventh (and last) Principle speaks to way you think about domains, and staff's authorities and accountabilities.
Warn: Common mistake is to hold people accountable for implementing their specialties; may sound logical; but dangerous. | [{'ID': 'MEYER-SEC-0072', 'Title': '5.7.1. Case Study: Safety Group Accountable for Safety', 'Text': '- Ctx: Local water district serving nearly 10 million households employed staff in three shifts to operate and repair facilities.\n- Ctx: Separately, Safety and Environmental Compliance group did inspections, supervised handling of hazards, oversaw Operations staff while they did work (monitored oxygen in man-holes while workers inside, inspected welders\' equipment, oversaw excavations).\n- Ctx: Structure: Randy (operations and repairs), Barry (safety and environmental compliance).\n\n- Cpt: Problems.\n  - Warn: Safety was reduced: Work crews weren\'t trained in safety, since Safety group supposed to take care of that; but Safety staff couldn\'t oversee every detail; worse, sometimes work crews grew impatient waiting for Safety staff to show up, went ahead without them; mistakes made, number of safety incidents went up.\n  - Ctx: After paying large fine for environmental accident, Board hired respected consulting firm to benchmark water district against high-performing peers; study found they suffered incidents five to seven times average, incurred fines three to five times average.\n  - Warn: Costs increased: At that time, 80-person Safety group requesting additional 20 staff; however, same study found best practices were just 5 to 10 safety experts dedicated to establishing policies, training workers, collecting data.\n  - Res: Economics clear; Safety group held accountable for other people\'s behaviors was less effective and more expensive.\n\n- Cpt: Conclusion.\n  - Def: Safety is attribute of people\'s work, not product in itself; everybody must run safe businesses and produce safe products.\n  - Def: Safety group should have been in business of providing training and consulting to Operations, not "implementing safety".\n  - Fnd: Like in any function, success depends on understanding what business you\'re in.'}, {'ID': 'MEYER-SEC-0073', 'Title': '5.7.2. Why Entrepreneurs Love Their Jobs', 'Text': 'Def: Each group should be defined as business within business.\nCtx: Since 1980, advocate of managing groups within organizations as businesses within business; beliefs validated when met with highly successful entrepreneurs; each led profitable business, employing from dozens to thousands of people; clearly very smart and well-educated people who could have been top executives in global companies; instead, chose to build own small businesses; asked why; perhaps surprisingly, wasn\'t for money.\n\n- Cpt: What Entrepreneurs Said: Empowerment.\n  - "...owning my time, choosing which hours I work."\n  - "I work as I wish to, within my own sense of professionalism and ethics."\n  - "...control over decisions."\n  - "I\'m not good rule-follower; I like making my own rules."\n  - "...the creativity -- there\'s no limitations on my ideas."\n\n- Cpt: What Entrepreneurs Said: Identity with Results.\n  - "...make things happen."\n  - "...the adventure of starting something and getting it done."\n  - "...building and creating value."\n  - "...the sense of accomplishment."\n  - "...knowing that I\'ve added value."\n  - "...setting my own goals in life, and then reaching them."\n  - "I\'m an artist of necessities; I love filling society\'s needs."\n  - "I want to be game-changer."\n\n- Cpt: Conclusion.\n  - Def: No reason can\'t create these same motivational forces (empowerment, identity with results) inside large organizations, at every level.\n  - Def: This is goal of business-within-a-business paradigm.'}, {'ID': 'MEYER-SEC-0074', 'Title': '5.7.3. What It Means to Be a Business Within a Business', 'Text': '- Prohib: Business-within-a-business paradigm doesn\'t mean operating internal service functions as profit centers; doesn\'t require chargebacks, where managers actually pay one another for internal services; certainly doesn\'t imply arm\'s-length relationship where support staff don\'t care about well-being of enterprise.\n- Def: Simply means every manager thinks and acts like entrepreneur running his/her own little business.\n- Def: Regardless of size of organization, every group should understand its purpose is to "sell" its products and services to customers (whether or not money changes hands).\n- Def: As entrepreneurs, staff should define their catalog of products and services, know whom their customers are; customers may be peers within organization, clients throughout enterprise, or external customers.\n- Def: Most every business has competition; when speaking about company in competitive market, obvious; but same true of organizations inside enterprises; internal service providers compete with both outsourcing and decentralization.\n- Def: Even if seems to internal service providers as if clients must work through them, surest way to lose monopoly is to behave as monopolist; everyone should strive to earn customers\' business through performance, as supplier-of-choice in market that has right to go elsewhere (even if really can\'t).\n- Ctx: Other terms for business-within-a-business paradigm: shared services, "intrapreneurship"; all imply same thing: empowered, entrepreneurial organizations.'}, {'ID': 'MEYER-SEC-0075', 'Title': '5.7.4. Benefits of Business-Within-a-Business Paradigm', 'Text': 'Def: Business-within-a-business paradigm brings out best in people.\n\n- Res: Customer focus: "I understand those are my customers, not unruly children or helpless victims of my decisions; in many cases, they have right to choose what they buy from me."\n- Res: Results orientation: "It\'s my product line; I know I\'m accountable for delivering everything I promise."\n- Res: Quality: "I\'m proud of my work; it\'s my job to make it best."\n- Res: Efficiency and cost control: "I have to be best deal in town."\n- Res: Teamwork: "To stay competitive, I have to focus on my own domain; I get help from peers when I need other specialties."\n- Res: Judicious risk-taking: "I have no choice but to take some risks to keep up with my competition; but I do so thoughtfully."\n- Res: Use of vendors: "I manage business, not just resources I\'ve been given; if buying something more cost-effective than building it internally, or if I need more capacity, I\'ll be first to offer \'buy\' option alongside \'make\' approach."\n- Res: Innovation: "I\'ve got to stay ahead of (or at least keep up with) my competition; so I\'d better innovate."\n- Def: These all traits of successful entrepreneurs.\n\n- Cpt: What You Won\'t Hear.\n  - Warn: "My job is to get budget at beginning of year, make sure it\'s used up by year end."\n  - Warn: "We\'re in public service; we\'re not business; so I don\'t have to listen to any customers."\n  - Warn: "My customer is enterprise as whole; I know what\'s best for you."'}, {'ID': 'MEYER-SEC-0076', 'Title': '5.7.5. Why Not "Partners"', 'Text': '- Cpt: Opposition to Business-Within-a-Business.\n  - Def: Some oppose business-within-a-business paradigm because believe best way to encourage collaboration is to declare groups "partners" in shared goal.\n  - Ex: IT and clients they serve are "partners" in pursuing technology-enabled business strategies; as such, share authorities and accountabilities.\n  - Warn: May sound nice on surface; but what does it really mean?\n  - Def: Some interpretations of partnership induce behaviors that undermine relationships, not strengthen them.\n\n- Cpt: Dangerous Definition 1: We Share Everything.\n  - Def: Partnership means IT staff and clients are one team, decide everything jointly.\n  - Def: "All for one, one for all" notion of partnership sounds like should induce great collaboration.\n  - Warn: In practice, respective authorities and accountabilities unclear; each party has right to meddle in other\'s domain of expertise.\n  - Warn: IT staff feel have right to tell clients how to run businesses, may even claim authority to force changes on clients to make best use of technologies.\n  - Warn: Clients feel have right to tell IT staff how to manage technology projects.\n  - Res: Instead of each contributing unique competencies, decisions influenced by people who aren\'t fully qualified to make them.\n  - Warn: Shared accountability equivalent to no accountability; without clearly defined individual accountabilities, team members struggle for control and projects mire; when things go wrong, everybody takes cover under banner of "partnership".\n\n- Cpt: Dangerous Definition 2: We\'re the Experts.\n  - Def: "We are partners, and hence equals; and since we\'re IT experts in this partnership, we\'ll decide what technologies you get."\n  - Warn: This is opposite of customer focus; "we know what\'s best for you" attitude can only serve to erode relationships.\n  - Warn: This definition of partnership fundamentally disempowering and unproductive; would be unfair to hold clients accountable for business results if can\'t control means of production, including IT; that\'s Golden Rule. Ref: ORG-STRUCT-PRINCIPLE1-01.\n  - Res: Using concept of partnership to justify disempowering clients leads to resentment, disputes over authority, strained relationships; can also induce delays or inaction as two parties struggle to come to agreement.'}, {'ID': 'MEYER-SEC-0077', 'Title': '5.7.6. Better Form of Partnership: Customer-Supplier Relationships', 'Text': "- Def: Better answer found in business-within-a-business paradigm; effective partnerships built on customer-supplier relationships.\n\n- Cpt: Customer-Supplier Model.\n  - Def: Suppliers (like IT) respect customers' rights to make purchase decisions; present options and share what they know, then let customers decide what they'll buy.\n  - Def: Customers decide what they'll buy, then let suppliers figure out how to produce it; suppliers choose own methods and tools, manage their staff (including contractors) and vendors; empowered and proactive, without disempowering customers in any way.\n\n- Cpt: Matching Authorities and Accountabilities.\n  - Def: With authority comes accountability.\n  - Def: Customers have authority to decide what they'll buy, hence accountable for justifying utilization of internal services, paying all life-cycle costs, realizing benefits.\n  - Def: Suppliers have authority to decide how they'll produce those results; accountable for reliable delivery of products and services at competitive costs.\n\n- Cpt: Benefits.\n  - Def: Customer-supplier relationships clean and mutually respectful; match authorities and accountabilities.\n  - Def: They're synergistic; synergies only result from taking advantage of people's different strengths, assigning distinct authorities and accountabilities, without any loss of commitment to one another's success; mutually respectful customer-supplier relationships do exactly that."}, {'ID': 'MEYER-SEC-0078', 'Title': '5.7.7. Proactive Entrepreneurship', 'Text': 'Def: Entrepreneurs strive to please customers; but does not mean they\'re passive order-takers; proactive in many ways.\n\n- Act: Internal entrepreneurs market value of their products and services; not meant to be self-serving; to lift customers\' awareness of possibilities so as to engender more creative uses of offerings.\n- Act: Entrepreneurial organizations proactively schedule time to talk to customers about business challenges; "sales" in best sense of profession (not pushing products, but helping customers solve problems and achieve goals); result is opportunities closely aligned with customers\' objectives.\n- Act: In response to customers\' requirements, suppliers proactively offer alternative solutions (as in Chevrolet, BMW, Rolls-Royce); make customers aware of better ways to address needs without going so far as to choose for them.\n- Act: Internal entrepreneurs help customers analyze alternatives in context of customers\' values (not their own); not matter of making recommendation (form of "we know what\'s best for you" that takes on some accountability for customers\' success); rather, consultative process: "If speed most important to you, pick alternative A; but if costs more important, select B."\n- Ctx: If suppliers done good job of sharing all they know, likely customers will come to same conclusions as they did; but if customers select alternative other than one supplier would recommend, perhaps know something about business suppliers don\'t know; or perhaps applying own values to trade-offs; in any case, entrepreneurs respect customers\' purchase decisions.\n- Act: Entrepreneurial organizations can be proactive about facilitating enterprisewide decisions (policies and standards); decisions made by community of relevant stakeholders, not unilaterally by any one expert; but suppliers can put forward issues and coordinate stakeholders\' decisions on behalf of enterprise.\n- Act: Internal entrepreneurs proactively invest in own businesses (process improvements, technology innovation, new products) to remain competitive; decide own business strategies, research and professional-development priorities.\n- Act: Entrepreneurs proactively maintain and evolve infrastructure ("Infrastructure" means assets owned by organization for purpose of producing services); internal entrepreneurs don\'t ask customers\' permission before buy new manufacturing capacity; empowered to acquire whatever need to satisfy customers\' demands for services; decisions based on market needs in total (enterprise capacity plans), not demand from any single customer.\n- Act: Entrepreneurs don\'t wait for customers to tell them to offer new products and services; proactively evolve product lines (without forcing solutions on customers); put new products "on shelf" (making available to customers), but only take them "off shelf" (actually deploying) when customers agreed to buy them.\n- Act: Entrepreneurs proactively reduce costs and improve quality to remain competitive.\n\n- Cpt: Summary.\n  - Def: In business-within-a-business paradigm, everybody is "product manager"; some sell to external customers, generate profits for enterprise; others sell products and services internally, probably at breakeven; but all are entrepreneurs accountable for managing businesses.\n  - Def: As proactive as they are, there\'s line they don\'t cross; entrepreneurs respect that customers know businesses best, are accountable for business results; therefore, by Golden Rule, customers must have authority to decide what they "buy" from internal service providers. Ref: ORG-STRUCT-PRINCIPLE1-01.'}, {'ID': 'MEYER-SEC-0079', 'Title': '5.7.8. Implications for Structure', 'Text': '- Def: Business-within-a-business paradigm sends all right signals and rewards right behaviors; harnesses everybody\'s creativity; aligns work of customers and suppliers; builds highly effective partnerships.\n- Def: Organizational structure is key to achieving such entrepreneurial organization.\n- Req: Define groups as lines of business, bounded by products and services they produce (by what each "sells," not what it does); not suggesting money changes hands.\n- Def: Designing healthy structure is matter of dividing organization\'s various internal and external products and services among its groups, laying out mosaic of entrepreneurships.\n- Res: This capstone Principle creates empowered jobs, where staff customer focused, accountable for results, creative and entrepreneurial, highly motivated.'}] |
-
  #### ID
  MEYER-SEC-0080
  #### Title
  6. Building Blocks of Organization Charts
  #### Text
  Src: Socrates: "The beginning of wisdom is the definition of terms."
Def: Engineering science comprises both principles and components; Part 2 described seven Principles of structure; this Part describes components.
Def: Useful to think of these components as "Building Blocks" that can assemble into organization chart.
Fnd: Way Building Blocks defined is crucial; Principles guide us in how to do that (as well as in how to assemble them).
Def: Most salient to definition of Building Blocks is Principle 7 (business-within-a-business paradigm); tells us Building Blocks should be lines of business that exist within organizations; when assemble Building Blocks into organization chart, assured every job is empowered entrepreneurship.
Def: This Part defines all lines of business that exist within organizations.
  #### Sections
  -
    #### ID
    MEYER-SEC-0081
    #### Title
    6.1. Overview of Building Blocks
    #### Text
    - Def: Building Blocks are lines of business that exist within organizations.
- Ctx: Appear in every industry (corporations, not-for-profit organizations, higher education, governments, even clubs).
- Ctx: Same lines of business exist within departments inside enterprises; like whole companies, most internal service providers (IT, HR, Finance, Facilities) include operations functions that produce ongoing services (like manufacturing), gurus in disciplines (like engineering), customer service, even internal sales and marketing (relationship managers that link internal service provider to rest of enterprise).
- Ctx: Some departments may not include all Building Blocks; nonetheless, their work can be defined in this same language.
- Def: Building Blocks help avoid gaps (Principle 3); essentially checklist of all possible lines of business in any organization, so can be sure have all pieces needed somewhere in new organization chart. Ref: ORG-STRUCT-PRINCIPLE3-GAPS-01.
- Def: All Building Blocks important; some may be larger than others; some may be more strategic to future growth; some may serve clients, while others serve customers within organization itself (internal support services).
- Fnd: All are businesses, all should be creative, customer focused, entrepreneurial; all essential, should be treated with respect; any biases or discrimination can only serve to diminish effectiveness of victimized group, ultimately performance of entire organization; in healthy organization, there are no second-class citizens.
- Def: At high level, five Building Blocks (five types of businesses); each has sub-categories.

- Warn: Caution 1: This framework of Building Blocks not prescribed organization chart; no such thing as off-shelf organization chart right for everybody; rather, Building Blocks simply language you can use to describe organization charts.
- Warn: Too often, leaders get together to plan new organization chart; but each leaves meeting with somewhat different understanding of words like "engineering" and "operations"; Building Blocks provide clear, precise, common language for analyzing, discussing, designing organization charts.
- Res: Executives can use this common language to diagnose current structure; understand one another's proposals; make structural decisions in factual, analytic manner; establish common understanding of missions and boundaries.

- Warn: Caution 2: Some names of these Building Blocks may sound familiar; may have "Engineering" department today; but may, in fact, be combination of multiple Building Blocks; pieces of "Engineers" Building Block may be found in other departments.
- Warn: Don't confuse name of Building Block with name of group in current organization.
  -
    #### ID
    MEYER-SEC-0082
    #### Title
    6.2. Distinguishing Engineers and Service Providers
    #### Text
    - Def: By "line of business," don't mean industry; who's in business of airplanes? Boeing, all airlines, companies that clean planes, companies that cater food, local government organizations that run airports, federal government that controls air traffic and sets rules, and more.
- Def: Can't just say "airplanes" and know what business people in; similarly, within enterprise, can't just say "operations" or "infrastructure" and know what business staff in; framework of Building Blocks has to be more refined.
- Def: Consider difference between Boeing (sells airplanes) and airline (sells transportation service); or Ford and Hertz; or building contractor and hotel.
- Def: Pick any industry, see two very different kinds of businesses: Engineers design and produce products (assets), support those assets with design expertise; Service Providers buy those assets, own and operate them, use them to deliver service.
- Ex: For most any type of asset, see both; with regard to airplanes, Boeing is Engineer, airline is Service Provider; for cars, Ford is Engineer, Hertz is Service Provider.
- Def: Same split occurs in internal service providers; in IT, Engineers implement computers, storage devices, networks, applications; Service Providers own and operate those assets to deliver services (computer time, data storage, connectivity, applications hosting, software as service like email).
- Fnd: Engineers and Service Providers very different businesses (differing in competencies, business models, cultures, products and services); thus, separate Building Blocks.
  -
    #### ID
    MEYER-SEC-0083
    #### Title
    6.3. Building Block: Engineers
    #### Text
    Def: Engineers create organization's products; discipline or technology specialists, designers, gurus in those products.
    #### Sections
    | ID | Title | Text |
    | --- | --- | --- |
    | MEYER-SEC-0084 | 6.3.1. Engineers Definition and Services | - Def: Engineers maintain locus of expertise in specific engineering discipline, technology, or professional specialty; use expertise to design, build, install "solutions," perhaps utilizing vendors' products then adding value; solution may be physical asset, software, or design of intellectual property.
- Def: Also enhance, tune, repair, configure, support those solutions; definition does not distinguish those who design and build products from those who repair them; essentially same bottom-of-T required to do both.
- Def: Engineers sell anything requiring in-depth expertise in design of organization's products (knowledge of what's inside that "black box").

- Cpt: Services of Engineers (all based on in-depth product-design expertise).
  - Solutions (entirely new, or enhancements)
  - Repairs
  - Configuration tuning
  - Domain specific incident management (a.k.a., second-level support, as point of escalation for customer-service)
  - Documentation and training materials, and training
  - Expert time, studies, presentations, sales support

- Cpt: Examples Across Industries.
  - IT: applications developers, infrastructure systems engineers
  - HR: compensation and benefits design, performance-management systems design
  - Finance: tax law, investment financial analysis
  - Product manufacturers: product designers, manufacturing engineers
  - Health care: outcomes management, doctors
  - Education: schools and professors, curriculum and instructional design
  - Government: policy and program design, decisions on grants

- Def: Engineers don't own solutions they produce (other than work in progress); sell solutions to others, be they peers within organization (such as Service Providers) or external clients. |
    | MEYER-SEC-0085 | 6.3.2. Applications versus Base Engineers | - Def: In many functions and industries, multiple layers of Engineers; some design fully assembled products; others experts in components that go into various products.
- Ex: Automobile engineering: those who design cars, those who design trucks; both "applications" draw on "base" components like engines, transmissions, electrical systems.
- Ctx: In some fields, many layers of engineers; in IT, computer engineers, databases and middleware, applications; each layer draws on lower layers, supports next layer up.
- Def: Those who assemble components into complete products (top layer) called "Applications Engineers"; produce purpose-specific products tailored to various kinds of customers' needs.
- Def: All lower layers termed "Base Engineers"; design components that go into various applications; components purpose-independent in that serve multiple applications.
- Ex: Engineers who build cars and those who build trucks are Applications Engineers (specialize in different purposes); Base Engineers contribute parts and advice to both.
- Ex: At Boeing, Applications Engineers design different kinds of airplanes; employ Base Engineers who design engines, control systems, interiors, etc.
- Ex: Higher education: various schools are Applications Engineers; curriculum and instructional design experts are Base Engineers.
- Ex: IT: term "application" refers to data-object-specific software (systems designed to handle information about particular topic); Base Engineers sell and support data-object-independent technologies (computing platforms, database engines, middleware, telecommunications networks/infrastructure, end-user-computing and data-analysis tools, software-engineering tools and methods, models such as artificial intelligence). |
    | MEYER-SEC-0086 | 6.3.3. Engineers Competencies | - Def: Bottom-of-T: Specific domain of technology, field of science, professional discipline, or branch of engineering.
- Def: Significant top-of-T competency: Engineering methods and tools (e.g., for design and testing) as well as project management.
- Warn: If expected to produce anything other than solutions, depth in professional domain bound to suffer; if not given clear requirements for things to design, may have to learn about customers' businesses to help customers define requirements (product of different Building Block); any time spend studying customers' businesses is time away from real specialty.

- Mdl: Competencies Profile.
  - Bottom of T: Domain of technology, science, or discipline
  - Key methods: Design and testing, project management
  - Technical skill: High
  - Project management: High
  - Service management (operations): Low
  - Business of organization's customers: Low
  - Interpersonal skills: Low
  - People supervision: Medium |
    | MEYER-SEC-0087 | 6.3.4. Engineers Biases | Ctx: To avoid conflicts of interests (as per Principle 5), important to know biases of each Building Block. Ref: ORG-STRUCT-PRINCIPLE5-01.

- Def: Engineers love innovation, but quickly become bored (may get sloppy) when asked to do routine "keep it running" work.
- Def: Laser focused on domain of expertise, love to study nuances and leading-edge discoveries; count on other equally focused Engineers when other skills needed.
- Def: Engineers willing to produce anything customers need (from enterprisewide to highly customized solutions); but not experts in customers' businesses; cannot assess customers' needs in unbiased, business-driven manner, since paid to live and breathe own domain of solutions.

- Mdl: Biases Profile (Five Fundamental Conflicts).
  - Invention versus operational stability: Invention
  - Purpose-specific solutions versus components: Applications (purpose-specific), Base (components)
  - Enterprisewide thinking versus focus of specialist: Specialist
  - Technical specialization versus unbiased diagnosis of clients' needs: Technical specialization
  - Service oriented versus audit: Service oriented |
  -
    #### ID
    MEYER-SEC-0088
    #### Title
    6.4. Building Block: Service Providers
    #### Text
    Def: Service Providers deliver ongoing services; may buy products from Engineers, then use those assets to deliver service (like airline that buys airplanes and sells transportation service); or service may be delivered primarily by people.
    #### Sections
    | ID | Title | Text |
    | --- | --- | --- |
    | MEYER-SEC-0089 | 6.4.1. Service Providers Definition | - Def: Distinguishing attribute of Service Providers is ongoing nature of services; doesn't include stream of small, unique projects (like repairs Engineers sell); rather, essentially same routine service, day after day; think of services as water flowing from spigot.
- Def: Service Providers keep things running reliably, safely, efficiently.
- Ctx: Building Block includes manufacturing, customer service, range of support services. |
    | MEYER-SEC-0090 | 6.4.2. Asset-based Service Providers | - Def: Some services based on ownership of assets, where customers essentially buying use of those assets; termed "Asset-based Service Providers".
- Def: Business model: look for cases where customers can share use of asset; acquire those assets, termed "infrastructure," from organization's Engineers (or directly from vendors), use them to produce services.
- Ex: IT: may all own own PCs; but not possible for each to run own networks and data centers; Asset-based Service Providers see as business opportunity; acquire networks and shared-use computers, sell use of them to others.
- Ctx: Assets include information as well as tangible properties.

- Cpt: Examples Across Industries.
  - IT: computer time, data storage, connectivity
  - HR: benefits administration, employee data administration
  - Finance: accounting services, treasury
  - Product manufacturers: factories, warehouses, logistics
  - Health care: hospital rooms, clinics, labs
  - Education: classrooms, residence halls, library
  - Government: roads, parks, ports and airports, air traffic control (air space), welfare, data services

- Def: Asset-based Service Providers not technology specialists; rely on Engineers to build, document, upgrade, repair assets; know how to operate infrastructure; but real expertise is in providing services, and all that entails. |
    | MEYER-SEC-0091 | 6.4.3. People-based Service Providers | - Def: People-based Service Providers sell services produced by people rather than assets; equipment (such as computers) employed only to make people more productive at tasks conceivably could do manually; but use of asset not really what customers buying; buying "use" of people.

- Cpt: Examples Across Industries.
  - IT: service desk, field technicians, writers and trainers
  - HR: counseling, recruiting, onboarding, job grading
  - Finance: procurement, customer service
  - Product manufacturers: customer service, field technicians
  - Health care: admissions, nursing, non-medical services
  - Education: registrar, admissions processing, student counseling, business services
  - Government: social services, elections, weather forecasts

- Cpt: Three Types of People-based Service Providers.
  - Type 1: Product support: Services help customers get value from rest of organization's products and services; common example is customer service (help desk); another example is training in use of organization's products.
  - Type 2: Internal support: Services leverage time and enhance abilities of others within organization; example is project management office (PMO) which helps others manage projects, offering services (project plans/PERT charts/work-breakdown structures, project tracking and reporting); they don't manage projects; other examples are field technicians who follow instructions of other Building Blocks, technical writers who help others communicate knowledge.
  - Type 3: Business services: Services outside primary intent of organization; from CEO's perspective, Administration, IT, Finance, HR departments contain all Building Blocks but classed as People-Based Service Providers; similarly, when internal services decentralized (finance or administration function within IT department), classed as People-based Service Providers. |
    | MEYER-SEC-0092 | 6.4.4. Service Providers Competencies | - Def: Specialized expertise of both types of Service Providers is service management; includes assessing market and determining which services to offer; defining those services; acquiring and managing any needed assets, methods, vendor services; contracting with customers (service-level agreements); managing capacity; managing ongoing delivery of those services.

- Mdl: Competencies Profile.
  - Bottom of T: Specific services and how they're produced
  - Key methods: Service delivery and management
  - Technical skill: Medium
  - Project management: Low
  - Service management (operations): High
  - Business of organization's customers: Low
  - Interpersonal skills: Asset-based (Low), People-based (High)
  - People supervision: Asset-based (Medium), People-based (High) |
    | MEYER-SEC-0093 | 6.4.5. Service Providers Biases | - Def: Service Providers responsible for stability, responsiveness, reliability, security, low cost; readily solve problems in service delivery, continually improve existing services, offer new services when time right.
- Warn: Major innovations (inventions) inevitably disrupt smooth operations; Service Providers intentional damper on innovation, proceeding only when potential market demand justifies investment and technologies evolved to point of being ready to produce reliable, safe services; biased to favor stability over innovation; change only when safe.

- Mdl: Biases Profile (Five Fundamental Conflicts).
  - Invention versus operational stability: Operational stability
  - Purpose-specific solutions versus components: Agnostic
  - Enterprisewide thinking versus focus of specialist: Specialist
  - Technical specialization versus unbiased diagnosis of clients' needs: Unbiased
  - Service oriented versus audit: Service oriented |
  -
    #### ID
    MEYER-SEC-0094
    #### Title
    6.5. Building Block: Coordinators
    #### Text
    Def: Some things require consensus among stakeholders (people throughout organization, in some cases clients as well); Coordinators drive those shared decisions.
    #### Sections
    | ID | Title | Text |
    | --- | --- | --- |
    | MEYER-SEC-0095 | 6.5.1. Coordinators Definition | - Ex: Planning: Every internal entrepreneur responsible for planning own business within business (that's empowerment); but all plans must be coordinated to add up to organization's plan; furthermore, planning specialty in own right (methods and analytical skills require study); thus, role for "Planning Coordinator" whose job not to decide plan, but rather help everybody develop own plans in coordinated manner.
- Def: Coordinators help stakeholders (within organization and beyond) come to agreement on shared decisions (policies, plans, standards).
- Act: Establish processes for decision making; enable processes with methods and project plans; ensure right stakeholders involved; provide common information (assumptions and trends, templates and formats, conceptual frameworks, timeframes); help individuals with respective duties in process; facilitate collaboration on interdependencies, such that each group's plan fits into higher-order enterprisewide or organizationwide plan.
- Warn: You're not Coordinator if, like all other stakeholders, you participate in these decisions; only Coordinator if job is to facilitate decision process.
- Act: Coordinators also help people utilize resulting shared decisions; compile results and make them available; help others find, interpret, apply relevant policies, standards, plans.
- Prohib: Coordinators not accountable for content; participating stakeholders are; Coordinators just accountable for effective consensus-based decision-making processes.
- Warn: If stakeholders can't reach consensus, little Coordinator can do; would be mistake to give Coordinators authority to force decision; since not accountable for others' results, doing so would violate Golden Rule. Ref: ORG-STRUCT-PRINCIPLE1-01.
- Ctx: Perhaps premature to expect consensus; but if important to make decision now, Coordinators can help executives motivate stakeholders to want to agree. |
    | MEYER-SEC-0096 | 6.5.2. Types of Coordinators: Business-Oriented | Def: Numerous topics require coordination; each distinct line of business; some business oriented, others more technical and product specific; most common to all functions; few function-specific.

- Cpt: Strategy Planning Coordinator.
  - Def: Strategic plan answers questions: "What businesses do we want to be in? How will we get from here to there?" Answers based on continually changing environment, organization's strengths, weaknesses, opportunities, threats.
  - Ctx: Entrepreneurs at every level accountable for strategies of own groups; but individual strategies must fit together to achieve strategies at next level up; strategy planning science in own right; leaders need help with process as well as coordination.
  - Def: Expert in strategic planning methods, in business environment (including competitors) and how environment creates threats and opportunities; doesn't decide strategies, but helps everybody decide own respective strategies, in coordinated fashion.

- Cpt: Operational Planning Coordinator.
  - Def: Operating plan looks one or two years ahead, answers questions: "What do we plan to deliver in coming year? How will we fulfill that demand (including needed resources, such as budgets)?"
  - Def: Expert in business and budget planning methods (especially investment-based budgeting), in tools used to create operating plan and budget based on forecasted demand.

- Cpt: Research Coordinator.
  - Def: Within organizations, research means investigating new products, services, technologies, or disciplines; in manufacturing company, may develop new products or manufacturing techniques; in IT, example is investigation of new vendor products and services.
  - Prohib: Research Coordinator doesn't do any research; helps others do research, by sharing expertise in research methods and in how to develop research proposals; helps executive decide which research projects to fund, as portfolio of investments aligned with organization's strategies.
  - Ex: Akin to US National Science Foundation which distributes research grants to universities and corporations (who do actual research), but doesn't do any research itself.

- Cpt: Organizational Effectiveness Coordinator.
  - Def: Focus on how organization does business (not what business produces); scope includes: culture, structure, resource-governance processes ("internal economy"), shared methods and tools, metrics and rewards.
  - Def: Distinct from Human Resources in that engineers "organizational ecosystem," whereas HR focuses on employment relationship.
  - Def: Expert in principles of design of those organizational systems, in methods of change (not just generic change management, but methods specific to engineering organizational system).
  - Act: Leads transformation projects (including restructuring), then helps everybody work within organizational design; may also coordinate employee communications.

- Cpt: Audit Response Coordinator.
  - Prohib: Coordinators do not audit or judge people they're meant to serve; but external parties may audit organization; when happens, organization must provide point of contact, coordinated response.
  - Def: Helps everybody respond to auditors and provides point of contact, but content of audit response is responsibility of appropriate groups throughout organization.
  - Ctx: Response includes initial provision of information, as well as coordinated projects to remediate any problems revealed by audits.
  - Act: With knowledge of questions auditors ask, can offer "assessments" to help others prepare for audit; assessments voluntary service, not audit; results provided strictly to those being inspected.

- Cpt: Regulatory Compliance Coordinator.
  - Def: Everybody accountable for complying with laws and regulations; helps them do so by providing expertise in laws and regulations, in how they apply to organization.
  - Act: Provides point of contact for regulators, coordinates any compliance examinations and remediation projects.
  - Act: Like Audit Response Coordinator, may offer internal assessments to help others comply.

- Cpt: Business Continuity Coordinator.
  - Def: In case of disaster, organization must ensure staff safe, stabilize situation, bring business back to normal operations (disaster recovery); beyond that, business-continuity planning can mitigate damage done by disasters.
  - Act: Helps everybody develop own plans, coordinates interdependencies to optimize resilience of organization; coordinates tests of plan, and (if triggered by actual incident) execution of plan.

- Cpt: Security Coordinator.
  - Def: Security means minimizing risks of harm from espionage, theft, sabotage.
  - Def: In empowered organization, everybody responsible for own security, for providing safe, secure products and services to customers; Security Coordinator helps them do so.
  - Def: Expert in threats; helps everybody come to consensus on security policies; keeps people informed of threats and defense strategies; leads investigations of and responses to security incidents; coordinates recovery and mitigation projects done by appropriate managers.
  - Prohib: Not audit function; doesn't check up on everybody's compliance with policies; not Service Provider offering ongoing services like guards, building access control, or IT firewalls and identity management; works at higher, organizationwide level, as service to others accountable for own safety.
  - Ctx: In IT, titled Chief Information Security Officer (CISO). |
    | MEYER-SEC-0097 | 6.5.3. Types of Coordinators: Technical | - Cpt: Standards Coordinator.
  - Def: Organizations set product design standards to ensure interoperability and supportability of products.
  - Ex: In home, shape of electrical outlet example of standard; in manufacturing industries, simple example is constraints on variety of nuts and bolts used in products; in IT, standards are protocols, APIs, interfaces.
  - Def: Standards are conscious constraints on design (not preferred brands and models); permit evolutionary change without loss of integration and interoperability.
  - Ctx: Many stakeholders affected by standards (Engineers, Asset-based Service Providers, some People-based Service Providers, in some instances clients); all perspectives should be considered before standard decided; not only is knowledge valuable; involvement in decision encourages compliance.
  - Prohib: Standards Coordinator does not decide standards; creates framework; then, on ongoing basis, pulls together appropriate stakeholders to decide each "cell" within framework (specific standards), helps them come to consensus.
  - Act: Helps Engineers access and interpret agreed standards in course of designing solutions.

- Cpt: Design Patterns Coordinator.
  - Def: To optimize best interests of customers who buy multiple things from organization, various products and services should be designed to fit well together; involves agreements among various Engineers and Service Providers about "design patterns".
  - Def: Expert in "ripples" (how decisions about, or changes in, one domain affect others); facilitates consensus on design guidelines that affect all domains, helps individuals apply guidelines to decisions and understand ripples.
  - Ex: In community, city planning and zoning example, dictating which types of buildings belong in each area of city.
  - Ex: Distribution company: pricing, sales incentives, marketing promotions for one product line may affect company's ability to sell other product lines; impacts cross channels, product categories, services (distribution, sales, marketing); coordination of policies, of requests for variances, needed to reduce risk of optimizing one product while sabotaging sales of others.
  - Ex: Higher education: drives enterprise programs to enhance student success, helps multiple groups package offerings for different audiences (e.g., for non-traditional students).
  - Ex: IT: design patterns suggest where various functions fit in broader enterprise architecture (e.g., what software goes on personal devices/PCs/mobile devices versus on shared servers); maintains map of how existing systems interconnected and how data flows through them, to help Engineers anticipate how changes in one system will affect other systems.
  - Ctx: In IT, combination of Standards and Design Patterns Coordinators called "enterprise architect". |
    | MEYER-SEC-0098 | 6.5.4. Types of Coordinators: Function-Specific | - Cpt: Information Policy Coordinator (IT).
  - Def: In IT, need for coordination of policies with regard to how information handled; one example is retention policies (particularly complex given electronic records interdependent, so information that has to be retained may depend on availability of other data that should be destroyed).
  - Ctx: Other examples: how system-of-record determined; how data owners chosen, their accountabilities and authorities; what information to be shared (i.e., access-rights); how privacy maintained; what may and may not be said using enterprise resources (web sites, blogs, electronic mail).

- Cpt: Employment Policy Coordinator (HR).
  - Def: Employees hired with expectation they'll evolve in careers through multiple jobs within enterprise; staff considered employees of enterprise, not just group that initially hired them; thus, some decisions about employment relationship should be made by consensus, not by each department alone (or by HR).
  - Ex: Compensation must be coordinated to avoid inequities, so two people doing similar jobs in different places in enterprise paid roughly same; enterprise may collectively decide to pay above market to attract top talent, or below market to improve near-term margins; business decision, not strictly HR decision.
  - Def: Role: bring enterprise stakeholders to consensus on such policies. |
    | MEYER-SEC-0099 | 6.5.5. Coordinators Competencies | - Def: All Coordinators similar in that facilitate and coordinate shared decisions; experts in identifying stakeholders and in bringing teams to consensus.
- Def: In addition, each expert in structure of content they are coordinating; know enough about content to understand trade-offs in decisions; but cannot be expert in everybody's domains to point of deciding content, must not disempower others (even if do know lot about subject).
- Ex: Planning Coordinator knows what goes into good plan; but actual content of plan comes from participating managers.

- Mdl: Competencies Profile.
  - Bottom of T: Topic being coordinated
  - Key methods: Consensus building, information structuring
  - Technical skill: Low (business) to Medium (technical)
  - Project management: Medium
  - Service management (operations): Low
  - Business of organization's customers: Low
  - Interpersonal skills: High
  - People supervision: Low |
    | MEYER-SEC-0100 | 6.5.6. Coordinators Biases | Def: Critical that Coordinators are unbiased facilitators of shared decisions; but do have biases.

- Mdl: Biases Profile (Five Fundamental Conflicts).
  - Invention versus operational stability: Invention
  - Purpose-specific solutions versus components: Agnostic
  - Enterprisewide thinking versus focus of specialist: Enterprisewide (or organizationwide) decisions
  - Technical specialization versus unbiased diagnosis of clients' needs: Unbiased
  - Service oriented versus audit: Service oriented |
  -
    #### ID
    MEYER-SEC-0101
    #### Title
    6.6. Building Block: Sales and Marketing
    #### Text
    Def: Fourth of five Building Blocks; Sales and Marketing is client-facing part of organization; adds value in two ways: enhances organization's relationships with clients (not single point of contact, but default point of contact; facilitates effective communications between clients and everybody in organization); helps clients address challenges (problems and opportunities) using organization's products and services.
    #### Sections
    | ID | Title | Text |
    | --- | --- | --- |
    | MEYER-SEC-0102 | 6.6.1. Sales and Marketing Definition | - Def: Sales staff help clients acquire just right products and services from organization's entire catalog; align organization with clients' strategies and business needs; help clients discover high-payoff opportunities for organization's products and services.
- Warn: Word "sell" has two meanings: to provide product, or to help customers buy others' products; this Building Block does latter; brokers sales; not accountable for delivery of other groups' products and services. |
    | MEYER-SEC-0103 | 6.6.2. Internal Service Providers Need Sales | - Def: In companies, need for Sales and Marketing obvious; but Building Block equally essential to internal service providers; have tough competition from decentralization and outsourcing; despite monopolies in few areas, must earn "market share" by developing great relationships with clients.
- Def: Internal service provider must find ways to contribute value to clients' critical challenges and strategic opportunities; Sales provides linkage to clients and expertise to do that.
- Def: In companies, goal of Sales is maximize revenues; but for internal service providers, goal not to convince clients to spend more (expense to enterprise); rather, maximize organization's contributions to clients' success (i.e., generate right business that delivers most value).
- Ctx: Internal service providers may not want to call this function "sales"; term may offend some clients (because don't understand value); wouldn't want to imply out to get as much money as possible from internal clients; within internal service providers, Sales may be named "business relationship managers" or "consultancy"; "Chief Digital Officer" role, in best incarnations, is Sales role within IT. |
    | MEYER-SEC-0104 | 6.6.3. What Good Selling Is About | - Def: External or internal, whatever name, great salesmanship focuses on helping clients, not on helping organization "push" products and services; in sales literature, termed strategic selling, consultative selling, or partnership selling.
- Def: Great relationships built by recognizing what's unique about each client, understanding business challenges, connecting with right suppliers in organization; why Sales staff spend most time with clients.
- Def: Beyond relationship building, Sales helps clients discover creative, high-payoff uses of organization's products and services; linkage between clients' business and organization's deliverables sometimes called "strategic alignment".
- Def: Not matter of passive order-taking; Sales proactively meets with key clients to discover ways organization can help achieve goals; always works in business-driven manner, not pushing any particular products or services.
- Def: Purpose of internal Marketing not to aggrandize organization; to help clients understand organization's value, so make better use of, gain more benefit from, offerings; Marketing also helps internal service provider better understand clients' needs through market research. |
    | MEYER-SEC-0105 | 6.6.4. Decentralized Sales Functions | Def: Some internal service providers decentralize Sales function, having it report to clients rather than to shared-services organization.
Ctx: True that Sales staff must be very close to clients, spend most time with clients; may even be substructured by client business unit (dedicated to specific clients); but doesn't mean should report to clients.

- Cpt: Problems with Decentralization of Internal Sales.
  - Warn: When function decentralized, seems to devolve into full-service support function, rather than remain focused on just Sales Building Block for shared-services organization.
  - Warn: Decentralized Sales staff often treat centralized department as adversary, as if role is to defend business units against them, rather than facilitate great relationships between two organizations.
  - Warn: Makes hard to balance workloads (e.g., number of small business units share one Sales person while large business units may warrant team).
  - Warn: Generally difficulties introducing essential methods of Sales for lack of common boss.
  - Warn: Often miss cross-business-unit opportunities (e.g., when "consortium" of clients band together to share asset such as ERP software).
  - Warn: Decentralized Sales staff generally don't provide services to other Building Blocks within shared-services department (like briefings on business trends and client interactions).
  - Warn: Some believe better access to clients if part of clients' business units; but in practice, rank often gets in way; easier for shared-services person with "Director" title to attend meetings of business-unit Vice Presidents, than for Director within that business unit.
  - Fnd: For many reasons, decentralization of Sales function not advisable. |
    | MEYER-SEC-0106 | 6.6.5. Three Types of Sales | Def: Three distinct types of Sales (not counting Marketing).

- Cpt: Type 1: Account Sales.
  - Def: High-level account representatives responsible for entire client accounts, regardless of geography; in companies, might be called "named account managers," where accounts are one or more global companies; in internal service providers, might be "business relationship managers," where accounts are one or more business units.
  - Def: Responsible for relationship with entire account; in addition, proactively meet with selected client executives, produce stream of strategic projects by helping key clients discover high-payoff opportunities.
  - Def: Very senior function; Account Sales professionals can (and should) attend clients' executive-level meetings and credibly discuss business strategies and challenges (without descending into product discussions); kind of people clients would like to hire for senior management positions.
  - Ctx: While may not manage many people or big budget, strategic impact immense and job grade should be as high as most senior leaders in organization.

- Cpt: Type 2: Retail Sales.
  - Def: Not dedicated to any specific accounts; instead, territory is geographic; in companies, geographic sales force and any retail storefronts for walk-in customers; in internal service providers, default points of contact for clients' inquiries and concerns; may even manage showroom or demonstration center.
  - Ctx: May also include business analysts who convert high-level opportunities (discovered by Account Sales) into detailed requirements.
  - Def: To differentiate: Account Sales proactive, provide premium service to selected clients (top executives and key influencers of business strategies); Retail Sales reactive, available to anyone on demand.
  - Fnd: Both types of Sales staff more than just order takers; add value by helping clients understand what most need to buy from organization to address business challenges.

- Cpt: Type 3: Function Sales.
  - Def: Experts in clients' professions or specific business processes (disciplines relevant to multiple accounts, hence needed by multiple Account Sales staff).
  - Def: Don't have territory; "second-tier" salesforce called in by Account and Retail Sales to help make presentations and diagnose clients' needs.
  - Ex: Medical device manufacturer: Account Sales staff had responsibility for hospitals; when demonstrated device in hospital's hematology laboratory, brought in trained hematologist; when same Account Sales representative demonstrated same device in same hospital's immunology laboratory, brought in trained immunologist; second-tier Function Sales force shared by all Account Sales representatives.
  - Ex: IT: experts in "digital enterprise" (application of technology to enterprise's relationship with customers); expertise of "Chief Digital Officer" can be applied to many business units (hence, not Account Sales function); draws on many different technologies (hence, not Engineer function). |
    | MEYER-SEC-0107 | 6.6.6. Marketing | - Def: Marketing focuses on clients as whole (either all, or segments with similar needs and buying patterns); distinguishes it from Sales which works with clients individually.
- Def: Marketing includes two sub-specialties: Marketing Communications (one-to-many), and Market Research (many-to-one).

- Cpt: Marketing Communications.
  - Def: Helps others in organization communicate with clients; across all communications channels, Marketing coordinates organization's messages for consistency with strategies and brand, ensure various entrepreneurs within organization don't over-saturate channels.
  - Ctx: Includes branding and marketing communications strategies; publications (brochures, web sites, newsletters); advertising and direct communications; promotions; customer events.
  - Def: In companies, goal is generate demand; for internal service providers, encourage understanding of value of function and improve client satisfaction.

- Cpt: Market Research.
  - Def: Inbound communications channel, serving organization as window to entire client community (its market); answers questions about what clients think, want, need, will buy; ranges from simple customer-satisfaction surveys to complex buying-pattern analyses and market-demand forecasting models. |
    | MEYER-SEC-0108 | 6.6.7. Sales and Marketing Competencies | - Def: Takes right people to build effective Sales and Marketing function.
- Def: Great relationships and strategic value both depend on people who know clients, their businesses, their strategies; ideally, Sales staff have background much like clients, with similar education, experience in industry and in clients' jobs.
- Def: Additionally, Sales staff have deep understanding of linkage between organization and clients' businesses; understand how organization's products and services can enable clients' strategies.
- Def: Sales staff need excellent interpersonal skills; bottom-of-T also includes methods to identify clients' key concerns and needs; to discover high-payoff, strategic opportunities; to quantify benefits of proposed solutions (strategic as well as cost savings).
- Def: Marketing also customer facing; experts in communications and market-research methods, in way customers think about organization's products and services.

- Mdl: Competencies Profile.
  - Bottom of T: Clients, their business strategies, linkage to organization's products/services
  - Key methods Sales: opportunity identification and requirements planning, relationship management, benefits estimation, contract brokerage
  - Key methods Marketing: market communications, marketing strategy, market research
  - Technical skill: Low ("smart buyer's" knowledge of organization's entire product line)
  - Project management: Low
  - Service management (operations): Low
  - Business of organization's customers: High
  - Interpersonal skills: High
  - People supervision: Low |
    | MEYER-SEC-0109 | 6.6.8. Sales and Marketing Biases | - Def: To align with clients' business strategies, organization must be prepared to flexibly offer any subset of products and services in completely business-driven manner; Sales and Marketing function represents entire organization without any product bias.
- Def: But do have other biases.

- Mdl: Biases Profile (Five Fundamental Conflicts).
  - Invention versus operational stability: Agnostic
  - Purpose-specific solutions versus components: Agnostic
  - Enterprisewide thinking versus focus of specialist: Account (Specialist in clients), Others (Enterprisewide)
  - Technical specialization versus unbiased diagnosis of clients' needs: Unbiased!
  - Service oriented versus audit: Service oriented |
  -
    #### ID
    MEYER-SEC-0110
    #### Title
    6.7. Building Block: Audit
    #### Text
    Def: Audit Building Block includes more than traditional financial and compliance auditors; any function which inspects and judges others, and reports results to someone other than those being inspected, is considered Audit.
    #### Sections
    | ID | Title | Text |
    | --- | --- | --- |
    | MEYER-SEC-0111 | 6.7.1. Audit Definition | - Def: Audit may even have some authority to block others (veto requests or decisions); only Building Block with such power; all rest focus on serving, not judging, others.
- Def: Audit distinguished from service-oriented Building Blocks in that delivers findings to someone other than people being judged; while Auditors should be polite and treat everyone professionally, people they judge not their customers.
- Ex: Epic failure of Arthur Anderson example of misunderstanding this; financial crises in 2008 was, in part, caused by rating agencies paid by banks whose securities they judge.
- Def: Audit sells services to people other than those whom inspect (such as enterprise's Board or external entities).
- Ex: To illustrate difference, testing service not Audit (it's Service Provider); Engineers can voluntarily use it (or not), test results reported back to Engineers.
- Ex: Similarly, "assessment" distinct from Audit; assessment voluntary (requested by manager, perhaps to prepare for real audits); results reported back to those who were inspected.
- Def: By contrast, audit imposed; results reported to someone other than those being judged.
- Def: Audit's job: catch people not in compliance with rules (laws, regulations, policies, standards, codes of conduct, financial reporting), or stop people from making mistakes by vetoing decisions. |
    | MEYER-SEC-0112 | 6.7.2. Need for Audit | - Def: Audit often necessary, but should be considered control mechanism of last resort; far more expensive, less effective, than systemic controls.
- Def: When rules of game induce people to comply (i.e., when compliance in everyone's parochial self-interests), then control systemic and Audit unnecessary; don't have to force people to optimize performance appraisals, or inspect entrepreneurs to ensure producing profits.
- Def: When systemic controls not feasible, manual inspections and judgments required.
- Ex: Situation illustrating need: when customers can't perceive differences in product quality; if everyone had device that could identify contaminants in food, never another case of food poisoning; because consumers cannot know if item in grocery store contaminated, government (US: Food and Drug Administration) inspects food producers (Audit function); can't examine every piece of food; periodically inspect processes and test samples (expensive and imperfect control, but better than nothing).
- Ex: Another situation: when employees have ability to gain personally by sacrificing well-being of organization (e.g., where personal conflicts of interests might induce fraud); where occurs, if systemic checks-and-balances not practical, control such as Audit needed. |
    | MEYER-SEC-0113 | 6.7.3. Scope of Audit | - Def: Mission of Audit strictly to uncover problems.
- Prohib: Must not recommend corrective actions to those problems; Auditors' expertise in finding problems doesn't qualify them to design solutions (expertise of other Building Blocks).
- Warn: Furthermore, recommending solution would be exercising undue influence, conflict of interests; imagine Internal Revenue Service recommending solve compliance problem by buying particular brand of financial software!
- Warn: If Audit recommends solutions, would no longer be "arm's length"; might judge more harshly solution that complies but isn't what recommended, or overlook problems just because people followed recommendations.
- Prohib: Additionally, Auditors must not disempower managers by setting objectives or giving orders; to have legitimacy, order to comply with rules and policies must come through chain of command, as should directive to cooperate with Auditors. |
    | MEYER-SEC-0114 | 6.7.4. Audit Competencies | - Def: Auditors experts in policies, regulations, or rules they are judging; also experts in audit process (i.e., how to collect and analyze data needed to make judgments).

- Mdl: Competencies Profile.
  - Bottom of T: Topic being judged
  - Key methods: Audit process
  - Technical skill: High
  - Project management: Medium
  - Service management (operations): Low
  - Business of organization's customers: Low
  - Interpersonal skills: Medium
  - People supervision: Low |
    | MEYER-SEC-0115 | 6.7.5. Audit Biases | - Def: Audit biased in favor of compliance, regardless of needs of business.

- Mdl: Biases Profile (Five Fundamental Conflicts).
  - Invention versus operational stability: Operational stability
  - Purpose-specific solutions versus components: Agnostic
  - Enterprisewide decisions versus specialized expertise: Agnostic
  - Technical specialization versus unbiased diagnosis of clients' needs: Specialization in topic of audits
  - Service oriented versus audit: Audit

- Fnd: Audit not only distinct Building Block; to avoid conflicts of interests, must be kept entirely separate from all other service-oriented Building Blocks; if in service business, can't build open, collaborative relationship with customers while also judging them. |
-
  #### ID
  MEYER-SEC-0116
  #### Title
  7. Applying the Principles: Rainbow Analysis
  #### Text
  Src: Paul Cezanne: "We live in a rainbow of chaos."
Ctx: Now ready to look at any organization chart and anticipate where structure getting in way of people's performance.
Def: This Part introduces method (one which puts Principles and Building Blocks to work to diagnose organization chart).
  #### Sections
  | ID | Title | Sections |
  | --- | --- | --- |
  | MEYER-SEC-0117 | 7.1. Diagnosing an Organization Chart: The Rainbow Analysis | [{'ID': 'MEYER-SEC-0118', 'Title': '7.1.1. Rainbow Analysis Overview', 'Text': '- Def: First step in analyzing organization chart is applying Building Blocks to it.\n- Def: "Rainbow Analysis" does that, then guides through four questions to diagnose all problems designed into current organization chart; reveals strengths and weaknesses of current structure (who\'s set up to fight with whom, who\'s set up to fail).\n- Ctx: Rainbow Analysis can also be used to examine proposed organization chart before implemented; if about to announce new structure, will greatly improve odds of success; may even help avoid costly mistakes.\n- Warn: Identifying structural problems not meant to accuse organization of failing, or make people defensive; good people can overcome almost any structural dysfunction if work hard enough; Rainbow Analysis only predicts potential problems, not actual failures; highlights areas where structure making it harder for people to succeed.'}, {'ID': 'MEYER-SEC-0119', 'Title': '7.1.2. Rainbow Analysis Workshop', 'Text': "- Def: Rainbow Analysis is basis of highly interactive workshop in which leadership team diagnoses current organization chart; in workshop, can come to consensus on whether, and how much, change needed; experience helps understand more deeply science of structure.\n- Ctx: Facilitated Rainbow Analysis workshop for dozens of leadership teams, in corporate, government, not-for-profit enterprises; invariably, eye opener; participants see organizations and jobs in new ways; even if don't decide to restructure, understand where problems coming from and why people struggling.\n- Ctx: Can do same analysis on own; steps exactly same."}, {'ID': 'MEYER-SEC-0120', 'Title': '7.1.3. Data Collection', 'Text': '- Act: Process begins with organization chart (current structure or proposed new structure); if doing Rainbow Analysis in workshop, print organization chart in poster size and put up on wall.\n- Ctx: Typically, sufficient to examine just two tiers of organization chart; in large organizations, additional management layers may be needed.\n- Ctx: Need set of eight or more colored marker-pens.\n- Act: Considering one Building Block at time, revisit definition, interpret it in context of mission of organization.\n- Act: Each leader takes turn putting colored stripe under box on chart if performs that function; put red stripe under any box doing Sales work; blue stripe under Applications Engineers; purple under Base Engineers; and so on.\n- Def: Color-code organization chart, identifying which Building Blocks within each group (often augment colors by noting Building Block and its sub-domain).\n- Warn: If analyzing current organization, be honest and color-code based on what people actually do, regardless of what organization chart says supposed to do.\n- Res: In most organizations, result is very colorful chart; why called "Rainbow Analysis".\n- Res: Data-collection step helps build deeper understanding of definitions of Building Blocks, essential to learning and applying science of structure to organization.\n- Res: Provides data for analysis; once color coding (or labeling) done, four questions will tell where problems are.'}, {'ID': 'MEYER-SEC-0121', 'Title': '7.1.4. Question 1: Gaps', 'Text': "- Def: Gap is any color (line of business) that's missing, or is done part-time by people whose primary focus is another function (color spread around chart in combination with other colors); nobody's primary job.\n- Ctx: Color may be there but some sub-specialties within it may be missing; to find these gaps, look more closely at specific sub-domains within each group marked with given color.\n\n- Cpt: Consequences of Gaps.\n  - Warn: Unreliable delivery: With no one thinking about line of business on daily basis, unreliable process; organization misses opportunities (may not even know what missed). Ref: ORG-STRUCT-PRINCIPLE3-GAPS-01.\n  - Warn: Reduced specialization: Work done by people who don't specialize in that profession. Ref: ORG-STRUCT-PRINCIPLE2-BENEFITS-01.\n  - Res: As result of both problems, function unreliable and ineffective.\n  - Warn: Beyond that, gaps lead to overlaps when groups compete for control of missing domains (or just fill gaps for own needs).\n\n- Mdl: Summary of Gap Consequences.\n  - Unreliable processes [Principle 3]: unreliable product/service delivery\n  - Reduced specialization [Principle 2]: lower productivity, slower delivery (time to market), lower quality, greater risk, less innovation, more stress, lower motivation\n  - Overlaps [Principle 3]: reduced specialization, redundant efforts, less innovation, confusion, product dis-integration, territorial friction, lack of entrepreneurship"}, {'ID': 'MEYER-SEC-0122', 'Title': '7.1.5. Question 2: Rainbows', 'Text': '- Def: "Rainbows" easy to spot; groups marked with more than one color, delivering multiple Building Blocks.\n\n- Cpt: Problems Created by Rainbows.\n  - Warn: Reduced specialization: In rainbow groups, people expected to be experts at too many different things; thus, mediocre at many assignments, may neglect other duties altogether. Ref: ORG-STRUCT-PRINCIPLE2-BENEFITS-01.\n  - Warn: Conflicts of interests: More serious problem results from combination of incompatible Building Blocks. Ref: ORG-STRUCT-PRINCIPLE5-01.\n  - Ex: Staff may be expected to keep operations stable (Service Providers), and also to innovate (Engineers).\n  - Ex: May be expected to specialize in subset of organization\'s products or services (Engineers or Service Providers); at same time, may represent entire organization to clients (Sales) where supposed to be completely unbiased.\n  - Warn: Combination of Audit with any other Building Block is serious conflict of interests; cannot both judge people, and build service-oriented partnership with them.\n\n- Mdl: Summary of Rainbow Consequences.\n  - Reduced specialization [Principle 2]: lower productivity, slower delivery, lower quality, greater risk, less innovation, more stress, lower motivation\n  - Conflicts of interests [Principle 5]: domain gaps, unpredictable and uncontrollable balance of conflicting objectives, stress'}, {'ID': 'MEYER-SEC-0123', 'Title': '7.1.6. Question 3: Scattered Campuses', 'Text': '- Def: When color appears many different places on organization chart, that\'s "scattered campus"; in worst cases, all different sub-specialties within Building Block only come together at level of organization\'s top executive.\n\n- Cpt: Problems Created by Scattered Campuses.\n  - Warn: Reduces professional exchange of experiences, discoveries, techniques, work products; leads to higher costs, slower delivery times, product dis-integration. Ref: ORG-STRUCT-PRINCIPLE6-01.\n  - Warn: Reduces coordination of profession (weaker mentoring and management controls, less load balancing, limited career paths, confusion, missed enterprise synergies).\n  - Warn: If single line of business divided, no one may feel accountable for managing that business; worse, if one group\'s job to oversee or decide how another group does work, then neither is whole business and both disempowered. Ref: ORG-STRUCT-PRINCIPLE1-01, ORG-STRUCT-PRINCIPLE7-01.\n  - Warn: Over time, scattered campus often leads to gaps and overlaps, since no one manager (short of top executive) in position to adjudicate domains.\n\n- Mdl: Summary of Scattered Campus Consequences.\n  - Less professional exchange [Principle 6]: higher costs, slower delivery times, product dis-integration\n  - Less coordination [Principle 6]: weaker mentoring and management controls, less load balancing, limited career paths, confusion, missed enterprise synergies\n  - Domain overlaps [Principle 3]: reduced specialization, redundant efforts, less innovation, confusion, product dis-integration, territorial friction, lack of entrepreneurship\n  - Domain gaps [Principle 3]: unreliable delivery, reduced specialization\n  - Disempowerment [Principles 1, 7]: lack of customer focus and entrepreneurship, less business planning, disempowerment'}, {'ID': 'MEYER-SEC-0124', 'Title': '7.1.7. Question 4: Inappropriate Substructure', 'Text': "- Def: To analyze final question, look at both colors and words in boxes; color (Building Block) tells what group's specialty supposed to be; scan across organization chart to see how that domain subdivided; if basis for substructure anything other than what Building Block supposed to be good at, that's inappropriate substructure. Ref: ORG-STRUCT-PRINCIPLE4-01.\n- Ex: Might see Engineers divided into groups based on clients' organization chart, or business processes, rather than types of products they produce; or Service Providers divided up based on technologies they use rather than services they provide.\n\n- Mdl: Appropriate Bases for Substructure.\n  - Service Providers: Service\n  - Engineers, Application: Purpose (in IT, data object)\n  - Engineers, Base: Engineering discipline\n  - Coordinators: What they coordinate (broadly classed into business, technical)\n  - Sales, Account: Client territories (business units)\n  - Sales, Retail: Geography, venue\n  - Sales, Function: Client profession or business process\n  - Marketing communications: Communications channel, service\n  - Marketing research: Service (e.g., design, data collection, analysis)\n\n- Cpt: Problems Created by Inappropriate Substructure.\n  - Warn: Wrong basis for substructure reduces specialization; results in lower productivity, slower delivery, lower quality, more risk, less innovation, more stress, poor morale. Ref: ORG-STRUCT-PRINCIPLE2-BENEFITS-01.\n  - Warn: Generally creates overlapping domains; creates confusion, causes redundant efforts, undermines product integration, creates territorial friction, diminishes entrepreneurship. Ref: ORG-STRUCT-PRINCIPLE3-OVERLAPS-01.\n  - Warn: May induce inappropriate biases; Sales function divided by product line would give clients product-driven (rather than purely business-driven) recommendations; essentially, structure leads people to optimize wrong objectives. Ref: ORG-STRUCT-PRINCIPLE4-CONSEQUENCES-01.\n  - Warn: Worst of all, if groups divided by anything other than line of business (such as by tasks, or where one group's job to oversee another), serious consequences of disempowerment. Ref: ORG-STRUCT-PRINCIPLE1-01.\n\n- Mdl: Summary of Inappropriate Substructure Consequences.\n  - Reduced specialization [Principle 2]: lower productivity, slower delivery, lower quality, greater risk, less innovation, more stress, lower motivation\n  - Domain overlaps [Principle 3]: reduced specialization, redundant efforts, less innovation, confusion, product dis-integration, territorial friction, lack of entrepreneurship\n  - Inappropriate biases [Principle 4]: poor advice, optimizing wrong objectives\n  - Disempowerment [Principles 1, 7]: lack of customer focus and entrepreneurship, less business planning, disempowerment"}, {'ID': 'MEYER-SEC-0125', 'Title': '7.1.8. Interpreting the Rainbow Analysis', 'Text': '- Act: When facilitate leadership team workshops, as go through four questions, discuss each potential dysfunction, take notes of relevant problems (those which really seem to be affecting organization); list specific examples (exactly which sub-specialties missing, or where domains overlap).\n- Act: Then, considering list of relevant problems with existing structure, raise next question: Is change needed? If so, need just few small "tweaks" or "clean sheet of paper" approach?\n\n- Cpt: Choices at That Point.\n  - A. Do nothing\n  - B. Tweaks: few small changes to existing structure\n  - C. Clean sheet of paper: completely new structure\n\n- Warn: Be forewarned: Many small tweaks more difficult than Clean Sheet approach; typically less effective, lacking whole-system perspective; unless current structure very close to right, clean sheet of paper generally right way to go.\n- Rec: If doing this on own (rather than in workshop with leadership team), follow same steps; take notes as analyze each question, then assess how serious organization\'s problems are.'}] |
-
  #### ID
  MEYER-SEC-0126
  #### Title
  8. Structures Designed to Fail: Case Studies
  #### Text
  Src: Confucius: "Study the past if you would divine the future."
Def: Before start drawing boxes for own organization, useful to practice; this Part is series of case studies describing approaches to structure others have tried (some may find familiar); use Rainbow Analysis to analyze faults.
Ctx: Case studies give practice looking at organization charts and anticipating problems; warn about approaches that may be popular but have serious flaws, so won't risk repeating mistakes others made.
  #### Sections
  | ID | Title | Sections |
  | --- | --- | --- |
  | MEYER-SEC-0127 | 8.1. Strategy as Basis for Structure | [{'ID': 'MEYER-SEC-0128', 'Title': '8.1.1. Situation', 'Text': '- Ctx: In 1962, Alfred D. Chandler put forth well-known proposition that "structure follows strategy"; theorized organization\'s structure could be fine-tuned to accomplish well-defined strategy.\n- Ctx: Some still believe this; Satya Nadella, CEO Microsoft (June 17, 2015): "I\'m certain that matching our structure to our strategy will best position us to build products and services our customers love and ultimately drive new growth."\n- Def: On surface, may seem logical to organize around strategies; but serious flaws in this reasoning.'}, {'ID': 'MEYER-SEC-0129', 'Title': '8.1.2. Rainbow Analysis', 'Text': '- Warn: Gaps: "Strategy" rarely singular; enterprises pursue multiple strategies, each with many facets; not every strategy can be represented in structure; inevitably gaps; strategies ever changing; when new strategy, or variant of strategy, occurs, may be no group dedicated to it; with such gaps, some strategies either ignored or poorly executed.\n- Warn: Rainbows: Approach creates "silo" organization, where each strategy-centric group includes all professional specialties needs to achieve objectives; reduction in specialization hampers every strategy.\n- Warn: Scattered campus: Many strategies draw on same specialties; if organization divides talent into groups by strategy, specialties scattered around organization; overall enterprise strategy likely to become disjointed; economies of scale and synergies lost.\n- Warn: Inappropriate substructure: Staff encouraged (by nature of structure) to specialize in enterprise strategy, rather than in competencies supposed to contribute to that strategy; inappropriate basis for substructure; again, reduced specialization hampers performance.'}, {'ID': 'MEYER-SEC-0130', 'Title': '8.1.3. Common Sense Argument', 'Text': '- Def: Pace of business changed; in Chandler\'s day, business strategies may have been relatively stable and long-term; but no more! Strategies can, and do, shift quickly and continually; to remain competitive, organizations must learn to be flexible and responsive ("turn on dime").\n- Warn: If structure were to follow strategy, organizations would have to restructure on frequent basis; prohibitively disruptive, expensive, disconcerting to staff; would delay response to new strategies.\n- Warn: If don\'t continually restructure, organizations tuned to do excellent job of today\'s strategies destined to perform poorly at tomorrow\'s strategies.\n- Warn: Perhaps worse, organization structured around today\'s strategies will fail to discover tomorrow\'s strategies.'}, {'ID': 'MEYER-SEC-0131', 'Title': '8.1.4. Alternative', 'Text': '- Def: Well-designed organization chart, combined with effective teamwork, can handle any strategy.\n- Mech: Strategy translates into specific initiatives; for each initiative, clear domains identify one and only group that "sells" that product or service; becomes "prime contractor" for that strategic initiative; then, teamwork processes take over; prime contractor may get help from any other groups anywhere in organization, they in turn from still others.\n- Res: This way, each strategic initiative draws from existing structure all needed competencies; organization can quickly recombine talents on new teams to address unlimited number of strategies.\n- Res: Healthy structure responds effectively to continually changing mix of strategies; yet provides stability that allows people to focus on specialties, which cultivates excellence.\n- Res: In entrepreneurial organization, everybody continually develops own strategies as entrepreneurial businesses within business.\n- Fnd: Healthy organizations flexibly respond to diverse client strategies, while continually generating own strategies (reversing old adage that structure follows strategy).'}] |
  | MEYER-SEC-0132 | 8.2. Outsource Non-Core Competencies | [{'ID': 'MEYER-SEC-0133', 'Title': '8.2.1. Situation', 'Text': '- Ctx: Michael Treacy and Fred Wiersema posited three "competencies" organizations require: operational excellence, product/technology leadership, customer intimacy; explained why companies (or business units) must choose just one on which to base market reputation and strategies.\n- Ctx: Although cautioned against abandoning other two, some theorists recommend organizations optimize structure to focus on just one.\n- Ctx: Innumerable vendors and consultants suggest outsource everything not considered core competency, to point where axiom become common wisdom.'}, {'ID': 'MEYER-SEC-0134', 'Title': '8.2.2. Why Not Outsource', 'Text': '- Warn: Outsourcing entire functions not effective for many reasons.\n- Warn: Outsourcing less critical competencies doesn\'t magically strengthen remaining competency; doesn\'t leave any more people focused on chosen competency.\n- Warn: Managing vendors certainly not easier than managing staff; vendor contracts often difficult to exercise, distracting executives with complex legal negotiations.\n- Warn: Even in less critical (but still needed) competencies, outsourcing can damage performance; can reduce flexibility, since any unanticipated requirements generally must be negotiated, contracted, come at high price.\n- Warn: Vendors can never be as well aligned with business strategies as insiders; despite talk of partnership, vendors morally obliged to optimize best interests of their shareholders, not yours.\n- Warn: Even when vested interests aligned with yours, vendors don\'t contribute to strategies in same way; do as told (in contracts); despite talk of "partnership," never contribute to strategic thinking at same level as leaders within enterprise.\n- Warn: In many cases, outsourcing doesn\'t save money; in fact, just opposite; paying vendors profit to do what otherwise could do can turn out to be expensive.\n- Fnd: Ultimately, outsourcing entire function weakens it.'}, {'ID': 'MEYER-SEC-0135', 'Title': '8.2.3. Rainbow Analysis', 'Text': '- Warn: Gaps: Organization designed around single competency sacrifices effectiveness at other competencies; risky for two reasons: First, most strategies require mix of competencies; weakness in any competency can jeopardize strategy (e.g., strategy focused on customer intimacy requires operational excellence in points of customer interface like customer service and web applications; innovation strategies like product development require input from sales/marketing and manufacturing; operational efficiency strategies built on excellence in engineering). Second, business conditions volatile, so strategies must be dynamic; dip in economy may require shift in emphasis from innovation to operational efficiency, to be reversed when economy recovers; organization designed to pursue only one competency ill-equipped to respond when business imperatives require other strengths.\n- Fnd: No organization can afford to focus exclusively on just one competency, settle for mediocrity in others.'}, {'ID': 'MEYER-SEC-0136', 'Title': '8.2.4. Alternative', 'Text': "- Def: For each Building Block, one competency dominant: Sales/Marketing dedicated to customer intimacy; Engineering to innovation; Service Providers to operational efficiency.\n- Def: When diverse groups combined into organization, organization as whole can include all Building Blocks (and all competencies); no reason why organization can't excel at all competencies; in addition to enabling any strategies, ensures voice for each perspective in strategy-formulation process."}, {'ID': 'MEYER-SEC-0137', 'Title': '8.2.5. When to Use Outsourcing', 'Text': "- Def: Although outsourcing not good substitute for strong internal function, vendors can add lot of value; in some cases, may be cheaper, better, more flexible, responsive.\n- Def: External vendors more cost-effective when: Multiple corporations can share vendor's assets (only has value when economies of scale cross corporate boundaries, e.g., telecommunication networks); due to size, vendor can afford higher degree of specialization (particularly valuable in high-tech professions where only largest organizations can afford qualified individual); company requires more capital than available, willing to pay premium in operating expenses to use other companies' capital; business volumes vary widely, or grow more quickly than organization can hire staff and acquire resources (worth paying more to make costs variable rather than fixed)."}, {'ID': 'MEYER-SEC-0138', 'Title': '8.2.6. Extended Staffing', 'Text': '- Def: Appropriate way to take advantage of vendors without giving up internal competencies: Vendors should never be used as alternative to internal staff; instead, vendors hired by internal staff to extend productive capabilities or improve value proposition.\n- Def: Call this approach "extended staffing"; essentially, vendors part of staff of appropriate internal function, not independent service provider that works directly with other functions; clients get product or service from internal staff, who may use vendors as part of delivery capability.\n- Def: Should occur naturally in entrepreneurial organization; entrepreneurs don\'t focus on growing empires (costs and headcount); strive to be supplier-of-choice to customers; if more economic to "buy" than "make," first to propose it; that way, always offer best deal.\n- Prohib: Not "brokerage," as some proposed; brokerage implies just connecting buyer and seller, with no accountability for deliverables; instead, internal staff are "value-added resellers" of vendor services; people who know profession (and work for shareholders/taxpayers/donors) ones who make commitments to clients, manage vendors, retain accountability for results.\n- Def: Services internal entrepreneurs offer customers may not precisely match those vendors sell to them; staff may add value to vendor-services to better meet needs of internal customers (integration, security, business continuity, compliance, ongoing support); may assemble multiple vendor-services into more complete service; or may just repackage service, perhaps charge for it (distribute costs) in different way.\n- Res: Extended staffing promotes tight vendor integration; internal staff oversee vendors to ensure performance and compliance with internal policies, standards, plans; incorporate them in internal service-delivery processes.\n- Res: Internal staff incur costs in managing vendors (at least own time); but since specialists in professions, more effective and efficient for them to manage vendors than for consumers to do so.\n- Res: Another advantage: dynamic nature; when industry economics shift in either direction, staff can utilize vendors more or less; enterprise gets best balance between "make" and "buy" at any point in time.\n- Fnd: Extended staffing gives enterprises benefits of outsourcing, without forsaking internal competencies.'}] |
  | MEYER-SEC-0139 | 8.3. Managers as Client Liaisons | [{'ID': 'MEYER-SEC-0140', 'Title': '8.3.1. Situation', 'Text': '- Ctx: In one company, client executives complained Corporate IT didn\'t understand strategies, people, needs; when demanded single point of contact, CIO assigned set of business units to each senior leader; each leader had two roles: Role #1: Manage technology-engineering or service group, ostensibly available to all clients; Role #2: Serve as liaison to set of client business units, ostensibly representing entire IT department.\n- Ex: Phil headed group of IT applications developers for financial systems (general ledger, accounts payable, tax); assigned to Finance department (not just for own team\'s projects, but for all projects and services delivered to clients in Finance); considered "relationship manager" on behalf of all IT to CFO.\n- Ctx: Structure: Phil (financial applications + Finance clients), Sam (customer applications + Sales/Marketing clients), Bev (employee applications + HR clients).'}, {'ID': 'MEYER-SEC-0141', 'Title': '8.3.2. Rainbow Analysis', 'Text': "- Warn: Gaps: Clients rightly want IT liaisons readily available; Sales function should spend most time with clients; in terms of time commitment alone, full-time job; but Phil had big group to manage; couldn't spend sufficient time with clients (attending meetings; getting to know people and businesses; working to discover new opportunities; brokering clear agreements; delivering account reviews; resolving relationship issues); beyond that, Sales role requires specialized skills and methods, especially critical if function to do more than facilitate relationships and take orders; Phil knew to do function well would require study and experience; not matter of capability; confident if given proper time and training, could learn to perform client-liaison job well; but while did so, who would manage applications development group? Phil didn't have time to do both; even if had time, didn't have right background (IT expert, not finance professional; understood accounting processes; but didn't really understand business challenges and strategies); most time, Phil remained focused on original Engineering job (project pressures demanded it; technology first love and focus of career; people in group depended on guidance, coaching, leadership); thus, Sales function remained gap; senior managers provided point of contact which improved relations; but didn't do much to add value to clients' strategic challenges.\n- Warn: Rainbows: To extent Phil spent time with clients, most interactions with Accounting department (primary users of financial applications); couldn't help but notice traditional clients some of least influential of Finance department's senior management; saw Jane (manager of small Financial Planning group reporting to CFO) seemed to get more attention; Phil called Jane, told looking for high-payoff strategic IT projects, wondered if could serve; Jane invited Phil; when visited, found Jane analyzing staffing cost trends; what really needed was access to employee data, market data, data-analytics tools; but what did Phil recommend? Can't honestly expect manager of financial applications developers to prescribe anything other than extensions to general-ledger application!? Despite best intentions, technological bias crept in; project Phil suggested only of mild interest to Jane; structure put Phil in conflict-of-interests situation; as expert in set of technologies (financial applications), paid to be biased (natural bias of specialist); at same time, in client-liaison role, expected to be unbiased and represent entire IT product line; no matter how well-educated and well-intentioned, organizational forces working against him; wasn't that Phil made conscious decision to be parochial; honestly believed financial solutions to which dedicated greatest thing since sliced bread, just didn't see opportunities outside own specialty; rainbow of Sales and Engineering led to product-driven, rather than business-strategy-driven, recommendations; conflict of interests not lost on Jane; found difficult to trust objectivity of someone who also had responsibility for (hence vested interest in selling) one particular solution.\n- Warn: Inappropriate substructure: Jane persisted and got Phil to recognize need for solution other than financial systems; but then ran into another problem; other groups who supplied needed data and tools busy serving own clients; Jane needed employee data; but Bev's clients in HR set priorities for staff; Jane's Finance project didn't make list; Phil still had to find way to get job done; when couldn't get help from Bev, group developed small HR application (outside domain of expertise); similarly, clients outside Finance department had trouble getting help from Phil's group, since priorities set by CFO; result, multiple overlapping financial applications cropped up throughout company; structure led to costly replication of efforts and dis-integration of data; ultimately, structure devolved into client-dedicated Engineering groups; productivity and quality suffered; enterprisewide synergies lost."}, {'ID': 'MEYER-SEC-0142', 'Title': '8.3.3. Alternative', 'Text': '- Def: Mixture of clients and technologies was attempt to fill gap in structure: Account Sales function.\n- Def: Sales not part-time job for internal service provider\'s senior leaders, any more than engineering and manufacturing executives can serve as corporation\'s sales force in spare time; Sales should be separate group, within internal service providers as within companies.\n- Warn: Some may say organization can\'t afford it; but truth is, small, dedicated team of Sales professionals will perform far better than same number of person-hours spent on client-liaison work distributed among managers of other functions.\n- Warn: Some may say clients won\'t accept "sales" function in internal shared-services organization; okay, give different name; but in addition, define services Sales delivers to help clients understand value to them.\n- Fnd: Sales is profession in own right, warrants dedicated specialists.'}] |
  | MEYER-SEC-0143 | 8.4. Decentralization | [{'ID': 'MEYER-SEC-0144', 'Title': '8.4.1. Situation', 'Text': '- Def: Business unit leaders may prefer to have own support staff rather than work with enterprise shared-services department (i.e., choose decentralization).\n\n- Cpt: Allure Typically Comes Down to Five Things.\n  - Customer focus: Own staff will respect them and treat well; but shared-services providers may treat as nuisance rather than customer, ignore requests, attempt to control rather than serve.\n  - Understanding business: Own staff "closer to business" and understand unique needs, whereas some shared-services providers believe "one size fits all" and force solutions that don\'t fit needs.\n  - Control of priorities: Can control priorities of own decentralized groups; but some shared-services providers make wait in line, beg for attention, work through committees and bureaucratic hurdles to get what need.\n  - Control of costs: If shared-services providers allocate costs, business unit leaders can control expenses more easily when group reports to them.\n  - Accountability: Mistaken belief among some corporate executives that decentralization required to hold business-unit leaders fully accountable for results (as if doing business with vendor diminishes authority over, hence accountability for, business performance).'}, {'ID': 'MEYER-SEC-0145', 'Title': '8.4.2. Rainbow Analysis', 'Text': "- Ctx: Decentralization de facto substructures all Building Blocks by client.\n- Warn: Gaps: Managers of decentralized support groups still not effective at Account Sales function, being busy managing groups; rarely study methods needed to discover new strategic opportunities; result: less strategic value; decentralized groups do little to improve collaboration with shared-services providers; often see role as defending business unit against corporate function; result: strained relationships.\n- Warn: Scattered campus: Each specialty scattered among business units; small groups that have to cover many domains can't specialize to same degree as consolidated function; result: lower performance, less innovation, higher costs.\n- Warn: Inappropriate substructure: Every specialty substructured by client; each builds parochial solutions, undermining enterprise synergies; enterprise synergies can be found in every internal support function (shared information/IT, talent management/HR, space/Facilities, product standards and parts/Engineering, external customer touch-points/Marketing, production facilities/Manufacturing); all can create shared or compatible solutions that encourage collaboration across business units; decentralization undermines collaboration among business units."}, {'ID': 'MEYER-SEC-0146', 'Title': '8.4.3. Case Examples', 'Text': '- Ex: Heavy-Equipment Manufacturing: In spirit of autonomy, each division built own manufacturing plant; increased costs for reasons: Capacity sat idle in one plant while another pressured beyond capacity; ultimately, lots of excess capacity ("safety stock") built into system; one division had plant in country while another did not; instead of using local plant, other division shipped products from own plant in neighboring country, transportation costs rose; one division pioneered new manufacturing techniques, but other divisions didn\'t learn until much later when CEO intervened and commissioned corporatewide task-force to rationalize production capacity; while could have been significant economies if some plants designed around long, stable manufacturing runs while others designed for rapid re-tooling, none of divisions alone could afford to specialize to that degree.\n- Ex: Engineering Function: Each division had own design engineering function; with all reinvention, number of parts corporation had to make or buy skyrocketed; CEO-sponsored task-force found dozen different electric motors with roughly same specifications; costs of development, manufacturing, inventories, support all went up.\n- Ex: Insurance IT: Decentralization of IT function resulted in multiple customer databases; since customer-numbers varied, enterprise not able to spot customers who bought from multiple business units; Specialty Automotive business unit cancelled policy covering vintage sports car, saying no longer interested in that type of business; customer moved all insurance to another company (policies for other cars, home, personal liability umbrella, corporation); company never knew this; because customer databases fragmented among business units, knew customer as few discrete policies, not as one customer with diverse needs; decentralization undermines synergies across enterprise.\n\n- Fnd: Decentralization inevitably results in higher costs, slower delivery times, lower quality, less innovation, reduced career opportunities for staff, fragmented products and services which undermine enterprise synergies.\n- Warn: Only thing worse than decentralization is shared-services organization that\'s not customer focused; doesn\'t understand unique needs of each business unit; denies clients ability to control how much spend and what buy.'}, {'ID': 'MEYER-SEC-0147', 'Title': '8.4.4. Federated Model', 'Text': '- Def: In companies where decentralization prevalent, may be weak enterprise function for just obvious common services; all other services left to decentralized support groups; sometimes termed "federated" model.\n- Warn: Nice name doesn\'t solve any problems caused by decentralization; little more than truce, such that shared-services and decentralized functions not competing for territory.\n- Warn: Adopting federated model actually makes things worse; institutionalizes decentralization; ideally, shared-services providers should compete for business by offering business units better deal whenever possible; competition doesn\'t have to undermine local authority; shared-services providers can work through decentralized counterparts, as suppliers to them.'}, {'ID': 'MEYER-SEC-0148', 'Title': '8.4.5. Dotted Lines from Decentralized Groups', 'Text': '- Def: Some companies attempt to ameliorate problems caused by decentralization with "dotted line" drawn from decentralized groups up to leader of enterprise-level internal service provider.\n- Warn: From cynical perspective, might be attempt by top executives to make corporate executives accountable for behavior of people they cannot control, in spirit of holding one person accountable for entire function; violates Golden Rule: accountability without real authority. Ref: ORG-STRUCT-PRINCIPLE1-01.\n- Warn: In response, corporate leaders may try to claim degree of supervisory authority over decentralized staff; may grant business units can decide what to be done, but try to decide how work done (professional practices); some even attempt to manage career paths and contribute to performance appraisals; any attempts to exercise authority over people who don\'t report to you results in political struggles; real managers naturally fight any incursion on authorities; see use of dotted line as reducing ability to meet obligations; with close relationships with local business-unit executives, real (decentralized) managers generally win political battles; meanwhile, decentralized staff caught in middle; not fair to subject employee to potentially conflicting directions and priorities.\n- Fnd: Pragmatically, dotted line gives shared-services executives no real authority; decentralized staff get funding from business units, answer to business-unit leaders, quite willing to defend business units against corporate meddling; holding shared-services executive accountable for things cannot control just induces strained relationships, sets up executive to take blame when business units misbehave; to be effective, CEO must direct staff through legitimate lines of authority (through business-unit executives), not expect shared-services leaders to do "dirty work."'}, {'ID': 'MEYER-SEC-0149', 'Title': '8.4.6. Roles of Shared Services Amidst Decentralization', 'Text': '- Def: If have to tolerate decentralized (federated) environment, enterprise shared-services organizations can still fulfill five roles.\n  - Full-service provider to clients in corporate headquarters.\n  - Sole (monopoly) provider of short list of products and services where synergies and economies of scale widely accepted (often, services based on large, expensive assets like manufacturing plant or data center; or services that link everyone in enterprise like network); products and services on short list should be determined through consensus of business-unit leaders, not imposed by corporate executives, so as not to further strain relations.\n  - "Outsourcing" supplier whenever decentralized groups wish to buy from it; decision as to what shared-services provider will do for business unit completely at discretion of business unit; shared-services staff must earn business through excellent performance, value, relationships; by selling through (not around) decentralized counterparts, not disempowering autonomous business units in any way; yet as earn market share, can deliver some economies of scale and synergies.\n  - Sole provider of coordination services where decisions must be made that affect entire enterprise; Coordinators have no formal power; job to facilitate consensus among stakeholders on standards, policies, plans; can also facilitate collaboration among business units with common needs (shared vendor contracts/purchasing service, consortia where business units share product or service); both coordination and facilitation services just that (services); business units may or may not choose to participate; up to CEO and business-unit executives to motivate stakeholders to collaborate (demanding enterprisewide standards and policies, or common business processes); only then will decentralized staff choose to utilize these services.\n  - Spokesperson for profession, promoting best interests of all staff throughout enterprise; key: never speak for others or make commitments for others, or attempt to manage staff who report elsewhere; shared-services leader can further profession by encouraging collaboration (professional interest groups) and representing profession\'s interests in enterprise policy discussions.\n\n- Res: By accepting accountability only for these five roles, shared-services organization can contribute to enterprisewide objectives without threatening business unit autonomy, antagonizing potential customers, becoming scapegoat that takes blame for problems engendered by decentralization.\n- Res: By always treating decentralized counterparts in respectful, customer-focused manner, relationships improve and shared-services leaders find themselves with more, not less, actual influence; sometimes "soft" approach actually strong approach.\n- Warn: Despite these services, most costs of decentralization remain.'}, {'ID': 'MEYER-SEC-0150', 'Title': '8.4.7. Alternative: Shared Services', 'Text': '- Def: All patches only marginally effective; right answer is consolidation of shared services.\n- Def: "Shared services" refers to internal service provider that serves multiple clients; instead of each business unit owning own little group, clients buy products and services from central supplier.\n\n- Cpt: Benefits of Shared Services.\n  - Costs reduced when redundancies eliminated; can eliminate parallel training, product R&D, policy formulation, support functions.\n  - Shared services does not mean "one size fits all"; centralized (shared-services) team of specialists can tailor solutions to unique customers\' needs at lower cost and higher quality than small groups of decentralized generalists.\n  - Can spot opportunities for "consortia" where multiple clients share single solution; even if different business units require unique solutions, can at least reuse some components, certainly reuse knowledge and competencies.\n  - Consolidation offers economies of scale in both staff and infrastructure by better balancing workloads; one business unit\'s peak load may occur when other business units slow; total peak demand generally less than sum of each business unit\'s peak; centralization reduces need for "safety stocks."\n  - Consolidates buying power; vendor licenses may be shared at lower cost; bigger organization has more bargaining power and can drive better deal.\n  - Sheer size improves performance; larger organization can support broader, more diverse product line; can support products better globally, 24 by 7; can afford higher-caliber management.\n  - Substructuring staff in appropriate way (rather than by client) increases specialization, with performance improvements (lower cost, higher quality, more innovation).\n  - Greatest benefits from potential enterprisewide business synergies; as business units find themselves using same services, may collaborate more (and better) across boundaries; implications for enterprise performance as profound as reasons why business units under same corporate umbrella in first place.\n\n- Fnd: Well-designed and well-managed shared-services organization not only performs better, but can improve performance throughout enterprise.'}, {'ID': 'MEYER-SEC-0151', 'Title': '8.4.8. Prerequisites for Shared Services', 'Text': "- Def: Before business units give up decentralized groups, shared-services organization has to address reasons clients like decentralization; five problems that drive decentralization, all can be more effectively addressed in other ways.\n  - Customer focus: Matter of culture (habits and practices within organization); can be addressed by teaching staff specific behaviors that embody spirit of customer focus (including respect for customers' purchase decisions and willingness to tailor solutions to clients' unique needs); but first, structure has to clarify whom customers are.\n  - Understanding clients' businesses: Job of Account Sales function; answer is to dedicate Account Sales professional, not Engineers, to each client business unit.\n  - Control over priorities: Decentralization gives clients understanding of limits to resources, control over priorities; but better way to address resource-governance challenge; clients can be given control of spending power rather than dedicated staff.\n  - Control of costs: Costs of shared services should never be allocated to business units on any basis other than utilization; holding business-unit executives accountable for costs can't control is futile and unfair.\n  - Accountability: Business unit leaders must be held accountable for use of shared services, just as accountable for purchases from vendors; to support this, shared-services organizations must be able to portray costs by business unit, based on consumption; until can do so, shared-services costs must not be part of business units' cost structures.\n\n- Fnd: If meets these requirements, shared-services organization doesn't threaten business unit autonomy any more than buying from external vendors (which shared across corporations); should be no need for decentralization."}] |
-
  #### ID
  MEYER-SEC-0152
  #### Title
  9. Special Situations
  #### Text
  Def: This Part describes number of common challenges that, on surface, might seem to force deviation from ideal structure; but will see ways to approach challenges without compromising Principles.
Ctx: Special situations discussed: Self-managed groups, Shared people, Remote locations, Project management office, Compliance and governance.
  #### Sections
  -
    #### ID
    MEYER-SEC-0153
    #### Title
    9.1. Self-managed Groups
    #### Text
    - Def: What if line of business small, perhaps just few people, and no one person significantly more senior than others? Example: small group of "gurus" in distinct discipline (few experts in technology).
- Def: Could put staff under manager of related line of business; but may risk extending manager too far, or creating undesirable "rainbow".
- Def: Alternative: leave line of business as box on organization chart, but with no manager; termed "self-managed group"; group manages itself as if there were supervisor over it.

- Cpt: Advantages of Self-managed Groups.
  - Maintains focus on that line of business, rather than burying within another line of business.
  - Provides growth path for function that may someday warrant manager.
  - Useful when members need to be placed at higher level in structure to get political visibility needed to be effective (e.g., in internal service provider, few senior Account Sales staff may all report directly to organization's executive to attract high-level talent to critical function and make visible to internal client executives).
  - Helpful when members need to be placed at higher level to get job-grade (compensation) needed (e.g., when antiquated HR policies do not permit people to report to someone of same grade level).

- Def: People and line of business still need supervision; in self-managed group, staff share duties that boss otherwise would perform; how do so should be agreed by members of group and manager above them.

- Cpt: Choices for Sharing Supervisory Duties.
  - Boss (level up) does it.
  - "Lead" (perhaps on rotating basis) does it.
  - Any individual can do it independently.
  - Group collaborates on it (e.g., through consensus).

- Def: Sharing of supervisory duties should be reinforced with some degree of shared destiny to ensure collaboration; some portion of everyone's performance appraisal should be based on performance of whole group.
- Warn: Contrary to first impressions, self-managed groups do not save headcount; supervisory duties must still be fulfilled, even if shared by members of group; total supervisory workload may actually increase as result of transactions costs of rotating or sharing supervisory duties.

- Cpt: Disadvantages of Self-managed Groups.
  - Emanate from weaker leadership; may not be as coherent in business strategies and directions, nor as strong in representing views at next level up (e.g., competing for resources and influence).
  - May be slower to acquire new methods and tools; new lines of business tend to get off to slower start.
  - Require more attention from manager above them, at minimum to do individual performance management, coaching, career counseling; manager above must ensure supervisory duties being performed effectively by group.
  - While supposed to behave as single direct report, inevitably reduce feasible span of manager at next level up, which might cost additional layer of structure elsewhere in organization.

- Fnd: Self-managed groups not goal in themselves (although empowerment is); simply way of treating situations that warrant structural separation but not manager; approach should be used with caution; proper supervisory agreements and rewards must be cultivated to make them work.
  -
    #### ID
    MEYER-SEC-0154
    #### Title
    9.2. Shared People: Temporary Duty
    #### Text
    - Def: Sometimes appropriate for one manager to loan individual to another, part time or full time, temporarily or indefinitely; borrowing term from military, call this "temporary duty" (even though may be ongoing arrangement).

- Cpt: When Temporary Duty Needed.
  - Certain individuals have skills beyond domain of their group ("rainbow" people); not good to expand group's domain to encompass skills for three reasons: would create "rainbow" group, perhaps overlapping domains; would create anomalous structure that may outlive individual's tenure, causing difficulties for others who follow (or create need for another restructuring when individual moves on); would set precedent that acceptable to violate Principles; better to put person on loan to other group whose domain includes person's other skills.
  - Move portions of headcount from one group to another as workloads shift; "load balancing" particularly handy in smaller organizations.

- Def: Borrowing person not contract between two groups for delivery of service, since lending group cannot sell services outside domain; simply loan of person; all accountability for work remains with receiving group, which manages borrowed individual as if part-time employee; receiving managers may even pay individual's salary for that period of time.
- Def: If situation permanent, temporary duty equivalent to individual holding two part-time jobs, reporting to two different managers who individually supervise portions of time.
- Prohib: Not "dual reporting" where two managers supervise person doing single job; person works in two distinct domains, hence has two distinct part-time jobs.
- Def: Regardless of longevity of arrangement, two managers must be very clear about allocation of person's time, must agree on when that time available to each (e.g., may agree on 50/50 split, 2.5 days per week to each group; but one group may need person full-time for one week, in trade for no time another week).
- Def: In all cases, individual should have "home" group, reporting to one manager who administratively accountable; administrative manager is point of contact for human-resources issues.
- Def: While administrative manager takes lead responsibility for writing individual's performance appraisal, other manager who borrowed person should contribute to performance appraisal in proportion to amount of time spent working under direction.
  -
    #### ID
    MEYER-SEC-0155
    #### Title
    9.3. Remote Locations
    #### Text
    - Def: In geographically dispersed organizations, some remote locations may have very few staff; but organization still has to deliver all products and services to clients in that location.
- Def: Four ways to address remote locations.
    #### Sections
    | ID | Title | Text |
    | --- | --- | --- |
    | MEYER-SEC-0156 | 9.3.1. Option 1: Rainbow Groups | - Def: Create "rainbow" group that combines all Building Blocks; similar to decentralization, although shared-services executive still has supervisory authority.
- Res: Advantages: simplicity, since minimal teamwork across geographic distances required, everyone reports to one boss.
- Warn: Has all disadvantages of silo: reduces specialization, may create jobs in remote locations too broad for anyone to succeed at; remote people not part of core professional team, limited input to enterprise directions; explicit mechanisms must be established to coordinate research, product offerings, engineering standards, professional practices; despite efforts, remote people rarely receive sufficient technical direction from appropriate experts (busy with own projects); consistency at risk; dis-integration of organization's product line (due to rogue groups doing own thing) increases support costs and undermines enterprise synergies; establishing "rainbow" groups sends signal acceptable to violate Principles; sets bad precedent.
- Fnd: Generally, location-specific "rainbow" groups should be avoided; only necessary when collaboration between remote location and headquarters so difficult that location must be run autonomously, despite costs and risks; with internet and modern collaborative tools, rare in most businesses. |
    | MEYER-SEC-0157 | 9.3.2. Option 2: Site Coordinators | - Def: In larger remote groups where headcount sufficient to permit individuals to specialize in single function, each specialist can report to appropriate manager at central location.
- Res: Advantages: single boss, consistency in technical directions, remote staff participation in professional directions.
- Def: In this alternative, one of remote people (typically most senior) should be appointed "site coordinator" to deal with location-specific issues (personnel policies, dress codes, hours of operation); site-oriented issues should be clearly defined, to delineate responsibilities of site coordinators from those of managers; generally issues that affect all employees at location.
- Def: Additionally, site coordinators can serve as agent for remote staff's real managers; may help distant managers with generic (not domain-specific) supervisory duties; manager for each remote individual should clearly define which duties wishes to delegate to site coordinator.
- Def: Site coordinators should have input to remote staff's performance appraisals (done by real manager).
- Def: Site coordinator duties distinct from client-liaison function (i.e., Retail Sales for that location), although Retail Sales person may happen to be designated site coordinator.
- Def: Site-coordinator duties over-and-above person's normal functional responsibilities, though additional workload must be taken into account. |
    | MEYER-SEC-0158 | 9.3.3. Option 3: Technician Services | - Def: In small remote groups where staff work in multiple domains, remote group may be deemed "Technician Services" business (People-based Service Provider); technicians sell time to others within organization, acting as their agents ("eyes and hands in field"); all technical direction comes from subject-matter experts who hire them.
- Def: Technicians don't sell anything directly to clients; communicate directly with clients; but just agents of another group, accountability flows through appropriate function.
- Def: Technicians may report to supervisor in same location (if big enough), or to manager who supervises technicians in multiple locations.
- Warn: Doesn't work for Account Sales or Coordinators, where delegation to field technicians (requires clear documentation of what to do) not generally feasible; these functions should be delivered centrally, even to remote locations. |
    | MEYER-SEC-0159 | 9.3.4. Option 4: Temporary Duty | - Def: If predominant function in location and all staff there involved in that to some degree, manager and staff may report to that function; to fulfill other functions in location, any of staff (manager included) can be loaned to other groups as temporary duty. |
  -
    #### ID
    MEYER-SEC-0160
    #### Title
    9.4. Project Management Office
    #### Text
    - Def: Excellence in project management essential to reliable project delivery; on large, complex projects, particularly critical; what's best way to incorporate PMO in structure?
- Warn: Traditionally, project leader accountable for managing every aspect of project, including tasks assigned to every team member; but for large projects, few people have sufficient project-management skills; some leaders address by creating small group of "super project managers" for difficult projects; creates problems.
    #### Sections
    | ID | Title | Text |
    | --- | --- | --- |
    | MEYER-SEC-0161 | 9.4.1. Case Study: PMO that Manages Projects | - Ctx: Since Fred's applications engineers weak in project-management skills, CIO asked Kathy to form Project Management Office (PMO); Kathy wasn't there to help Fred manage projects; other way around; Kathy accountable for big or complex projects, Fred just "body shop" supplying people to work on Kathy's projects; led to numerous problems.
- Warn: Kathy's project managers experts in project management, not applications engineering; nonetheless, controlled who on project team and their assignments, schedules, key design decisions that affected delivery dates; with non-technical people calling shots, quality suffered.
- Warn: Exacerbating this, incentives biased against quality; Kathy not accountable for long-term applications support; but certainly accountable for on-time delivery; cut corners to get projects out on time.
- Warn: Meanwhile, Fred disempowered; couldn't control key design decisions; but still accountable for future support, maintenance, operational efficiency, integrations.
- Warn: Fred didn't really own line of business; with Kathy taking over delivery of products from time to time, wasn't empowered entrepreneur who could plan future, define products, optimize methods and costs, evolve capabilities.
- Warn: Fred's staff, being just body shop on all interesting projects, demoralized; had little incentive to improve project-management skills (root cause of problem).
- Res: As expected, Kathy and Fred at odds, not because didn't get along but because structure set them up to fight. |
    | MEYER-SEC-0162 | 9.4.2. Project Management as Service | - Def: Project-management experts important; PMO in itself not problem; in fact, great way to bring discipline and proficiency to project delivery.
- Def: Problems come from PMO that's accountable for projects, occasionally taking over delivery of other groups' products.
- Fnd: Effective PMO is People-based Service Provider, accountable for delivering project planning and facilitation services; helps everyone succeed at respective projects, without assuming project leadership or accountability for results. |
  -
    #### ID
    MEYER-SEC-0163
    #### Title
    9.5. Compliance and Governance
    #### Text
    - Def: "Compliance" processes ensure organizations follow rules, including own policies and standards, contractual obligations, myriad laws and regulations; how should compliance be represented in organization chart?
- Def: Compliance implemented through "governance," which means all processes that coordinate and control organization's resources and actions.
- Def: Governance not limited to oversight; controls can be embedded in organizational ecosystem (structure, culture, resource-management processes, metrics); but too often, executives assume "governance" means person or committee with authority to control others.
    #### Sections
    | ID | Title | Text |
    | --- | --- | --- |
    | MEYER-SEC-0164 | 9.5.1. Case Study: Chief Compliance Officer | - Ctx: Allison appointed Chief Compliance Officer in IT department of huge financial services company; enthusiastically told of importance of compliance in industry, hence stature of position as one person accountable for compliance of entire IT function; "CIO gave me authority to make that happen."
- Warn: Time and again, history proven this approach doesn't work; others have businesses to run, not going to let peer get in way; sure, comply when easy or when really have to (with big, visible initiatives); but on day-to-day basis, three factors working against: Allison accountable for compliance, not peers (won't put much effort into something not in own performance objectives); others accountable for business results, not going to compromise missions to help Allison with objectives (may have incentives to thwart if compliance gets in way); third factor is killer: others don't need to worry about compliance (Allison's problem); so if mess up and bad things happen, she'll take blame; may as well been given title "Chief Scapegoat".
- Fnd: All factors encourage Allison's peers to find ways around controls to get jobs done; ultimately, succeed. |
    | MEYER-SEC-0165 | 9.5.2. Who Decides Trade-offs | - Def: Realists know there are trade-offs; to illustrate extreme: if compliance means shutting down business for while, maybe right answer to wait to implement controls, hope nothing bad happens in meantime; on other hand, if risks of non-compliance huge (people getting hurt or very large fines), rational person would choose to shut down business to implement controls.
- Def: Trade-offs had to be made with full understanding of both risks and business impacts; somebody has to decide these trade-offs; no matter who, if something bad happens, whole organization suffers consequences; only question is, who should make decisions (compliance officer, or managers running business)?
- Def: Either compliance officer could study business and make decisions, or teach others risks and let those who know business decide.
- Warn: If compliance officer makes decisions, battle brewing (fighting to minimize risks, while managers fight to maintain operations); best decisions not going to come from internal fighting; far more effective if decisions collaborative. |
    | MEYER-SEC-0166 | 9.5.3. Everyone Must Be Accountable | - Def: Only one way to make managers want to collaborate: hold all accountable for own compliance.
- Def: Golden Rule: authority and accountability must match; if compliance officer makes decisions, has to be held accountable not just for compliance but for everybody's business results; otherwise, what's to stop from deciding in favor of too much compliance, sacrificing business results, letting others take blame when critical services fail? Ref: ORG-STRUCT-PRINCIPLE1-01.
- Fnd: Right approach: hold everybody accountable for own behaviors, including own compliance; then, willingly implement compliance initiatives to protect own hides; overall, success rate of compliance initiatives higher, not lower, when authority and accountability in right place. |
    | MEYER-SEC-0167 | 9.5.4. Compliance as Service | - Def: When everybody accountable for own compliance, organization doesn't need someone who forces others to comply; but still needs compliance officer.
- Def: Job of Compliance Officer: help others succeed with compliance accountabilities; service based on expertise in how regulations affect organization and its clients.
- Def: Compliance is Coordinator function; helps others succeed at accountabilities, including helping agree on shared decisions and processes.
- Def: If regulators request information or impose audit, can coordinate organization's response and serve as communications channel to regulator (single point of contact); but just accountable for coordination services, while everybody accountable for own portion of response.
- Def: Can help individual managers put together own policies and plans; at higher level, bring stakeholders to consensus on shared policies and plans, consolidate individual plans into integrated organizational plan.
- Def: Can help others agree on shared initiatives that improve compliance; then, help implement agreed changes, not as manager accountable for results but as facilitator and subject-matter expert.
- Def: As Coordinator, can manage tests of plans, while everybody remains accountable for own groups' responses.
- Def: Through all services, can teach others regulatory requirements, risks of non-compliance, kinds of changes required to mitigate risks; educating others equips them to better decide trade-offs. |
    | MEYER-SEC-0168 | 9.5.5. Oversight | - Def: May be need for oversight; but shouldn't be mixed with service role.
- Warn: Real auditors outside (regulators, hackers for security, Mother Nature for business continuity); if seen as auditor, doors close as approach, won't have much impact.
- Def: Remaining service oriented, can sell "compliance assessment studies" that help managers get ready for real external audit (or know how subordinates doing); describing this way keeps on their side of table, there to help them, not judge them; must maintain good relationships to implement meaningful change. |
    | MEYER-SEC-0169 | 9.5.6. Scapegoat Trap | - Warn: Many functions can fall into scapegoat trap by claiming authority over, hence accepting accountability for, others' behaviors.
- Ex: "Security" group thinks accountable for security, rather than helping everyone operate in secure manner.
- Ex: "Business continuity" group unilaterally designs plan.
- Ex: "Quality assurance" or "testing" group tries to take accountability for quality through inspection and control, rather than providing testing service to others accountable for producing quality products.
- Fnd: These all examples of familiar theme: Total Quality Management; quality, in all forms, is attribute of product or service, not separate deliverable; producing products, and quality of those products, not two distinct jobs; experiences in every industry prove same principle: responsibility for compliance, safety, security, every other aspect of quality should never be separated from responsibility for doing work.
- Fnd: In every case, better results achieved when everybody held accountable for own behaviors; Coordinators help others with accountabilities; if oversight (Audit) needed, must be kept arm's-length from service-oriented Coordinators. |
-
  #### ID
  MEYER-SEC-0170
  #### Title
  10. Workflows: Teamwork Processes
  #### Text
  Src: James A. Garfield: "Commerce links all mankind in one common brotherhood of mutual dependence and interests."
Def: To this point, focused on design of organization chart; now time to turn attention to processes of cross-boundary teamwork.
Def: Teamwork not luxury; essential aspect of organizational design; as per Principle 2, can't specialize if can't team. Ref: ORG-STRUCT-PRINCIPLE2-01.
Ctx: Indeed, word "structure" includes both organization charts and teamwork processes; Henry Mintzberg: "Structure of organization can be defined simply as sum total of ways in which labor divided into distinct tasks and... [how] coordination achieved among these tasks."
  #### Sections
  -
    #### ID
    MEYER-SEC-0171
    #### Title
    10.1. Importance of Teamwork
    #### Text
    - Def: Teamwork often gating factor in organizational design; organizations not very good at it deliberately create "silo" groups which can function relatively independently.
- Warn: In doing so, scatter profession among all groups that need it, hence reduce specialization; in other words, consciously give up some organizational performance to avoid having to invest in more effective teamwork processes.
- Warn: Even if self-sufficient silos not created deliberately, occur automatically if neglect teamwork processes; no matter what organization chart says, if can't get help from peers, forced to replicate skills and muddle through on own; without effective teamwork, groups inevitably evolve into silos of self-sufficient generalists.
- Fnd: Bottom-line: better organization is at cross-boundary teamwork, more can afford to specialize and, in doing so, optimize performance; if want to build high-performance structure, must be prepared to invest in mechanisms of teamwork.
- Def: By investing in teamwork, don't mean team-building; lot more to it than liking and trusting one another; effective cross-boundary teamwork depends on explicit mechanisms for forming and coordinating teams.
  -
    #### ID
    MEYER-SEC-0172
    #### Title
    10.2. What Not to Do to Improve Teamwork
    #### Sections
    | ID | Title | Text |
    | --- | --- | --- |
    | MEYER-SEC-0173 | 10.2.1. Case Study: Randy's Teamwork Challenges | - Ctx: When Randy hired as CIO, inherited seasoned executives technically qualified, generally liked by staff, nice people; one little detail: didn't team at all well; cordial with one another and cooperated on organizational decisions like policies and plans; but each ran group as independent silo with minimal collaboration on projects and services.
- Warn: Obviously costing company money; many skills replicated across groups, people spread thinly as tried to do too many things, hurt productivity; another problem: people managed functions didn't know much about (applications developers ran own development servers without much security, continuity planning, even back-ups; meanwhile, infrastructure group adept at running servers had own applications developers for billing system); each department had own support functions (budgeting, purchasing); two infrastructure control centers (one for computing, another for network); three different help desks (one for PCs and infrastructure, another for applications, still another for telecommunications networks); for lack of teamwork, hand-offs rough; when application ready for production, often delays due to poor coordination between developers and infrastructure staff; perhaps most embarrassing, each department had own client liaisons (Sales); organization looked foolish when clients got different, sometimes conflicting, answers from different "single points of contact," one hand didn't know what other hand doing. |
    | MEYER-SEC-0174 | 10.2.2. Failed Approach 1: Team-building | - Ctx: Randy hired consultant to do one-day seminar on teamwork; consultant taught leaders importance of teaming, team problem-solving techniques, effective communications skills; everyone agreed with everything said; but back on job, nothing changed.
- Ctx: Randy brought consultant back to do more extensive team-building process; leaders spent three days at resort playing games that required mutual trust, talking about how felt about one another and interdependencies, playing golf; got to know one another lot better, everyone had great time; but back on job, nothing changed. |
    | MEYER-SEC-0175 | 10.2.3. Failed Approach 2: Job Rotations | - Ctx: Getting frustrated, Randy tried job swapping; head of infrastructure group assigned to applications development; head of applications went to client support; head of client support moved to infrastructure group.
- Res: Leaders developed lot of empathy for one another; but still nothing changed; wasn't long before former head of infrastructure, now leading applications group, requesting money to upgrade development servers; meanwhile, new head of infrastructure fiercely defended need for own billing application developers.
- Res: Scheme lasted about three months, at which time Randy put everyone back (just moments before organization collapsed due to leaders who knew nothing about functions managed); cynics among staff got good laugh at this experiment. |
    | MEYER-SEC-0176 | 10.2.4. Failed Approach 3: Process Engineering | - Ctx: Randy's next attempt: define cross-boundary processes so people would know duties within teams; for service-management, hired consultant to train staff and implement ITIL "best practices" processes; for applications development, hired another consultant to implement "DevOps," including well-defined process (and tools to support) to move code from development into production; for other processes, chartered teams to document and redesign workflows that spanned organization, supported by another consultant who specialized in Lean-Six Sigma process engineering.
- Warn: Processes defined everybody's tasks; but no one accountable for results (delivery of services to customers); Randy designated "process owners" to oversee processes end-to-end.
- Warn: Introduced lot of strife into organization, since process owners violated Golden Rule by trying to tell others how to do jobs; many months (and dollars) later, few processes actually implemented; for those which were, additional headcount required to administer processes and coordinate hand-offs; organization became more bureaucratic, less flexible, less accountable. Ref: ORG-STRUCT-PRINCIPLE1-01.
- Res: Going in wrong direction! |
    | MEYER-SEC-0177 | 10.2.5. Failed Approach 4: Forced Consolidation | - Ctx: Randy gave up on participative style and mandated reorganization; consolidated three help desks, moved development server into computer center, set up single Client Liaison group reporting directly to him.
- Res: Resulted in utter chaos for while; after few months, things settled down: unified help desk did fine job of transferring calls to three "level-two" help desks; development servers moved into computer center, but applications developers insisted on managing themselves; reliability and security issues remained. |
-
  #### ID
  MEYER-SEC-0178
  #### Title
  11. Benefits and Cultural Transformation
  #### Text
  Src: Max De Pree: "First responsibility of leader is to define reality. Last is to say thank you. In between two, leader must become servant."
Def: Final Part helps executives think through role and plans with regard to structure of organizations.
  #### Sections
  -
    #### ID
    MEYER-SEC-0179
    #### Title
    11.1. Should I Do This? Benefits That Justify Costs
    #### Text
    - Def: Restructuring organization not easy; easy to simply draw boxes and assign names; but as most experienced, doing so does little to improve organization's effectiveness.
- Def: Reason executives take ineffective short-cuts: building high-performance organization takes meticulous planning; transformational, participative process adds to leaders' workloads; plus, process stressful (people worry about careers, status, power).
- Def: Benefits that justify costs: principle-based structure delivers both efficiencies and effectiveness; transforms organization's culture as well.
    #### Sections
    | ID | Title | Text |
    | --- | --- | --- |
    | MEYER-SEC-0180 | 11.1.1. Efficiencies | - Cpt: Sources of Efficiencies.
  - Overlaps eliminated: Time saved by eliminating redundant efforts, territorial disputes, time managers spend sorting out who does what.
  - Role clarity permits greater span: With clear domains, groups self-directed to far greater extent; permits flatter organization, reduces supervisory workloads.
  - Professional collaboration encouraged: Bringing together related specialties induces more professional exchange; precludes redundant research, accelerates organizational learning, improves productivity, enables more reusable components instead of reinvention.

- Warn: Be cautious about using efficiency gains to justify restructuring initiative; may lead to expectations of reduced budgets and headcount.
- Def: In practice, efficiencies often reinvested in doing more with same budget, not same with less budget; organizations catch up on critical sustainment tasks (training, innovation, planning, relationship building); improve quality of services and reduce risks; catch up on deferred maintenance; more responsive to customers, addressing backlogs and pent-up demand; find new opportunities to deliver more value by filling gaps.
- Warn: Promising cost savings from restructuring associates new organization with job losses; can set staff against change, making tough to realize potential benefits.
- Warn: Efficiencies develop gradually over time as new structure settles into place, not instantly upon announcement of new organization chart. |
    | MEYER-SEC-0181 | 11.1.2. Effectiveness | - Def: Effectiveness more important than efficiency, even in companies concerned about costs; efficiencies produce marginal cost savings, whereas improving effectiveness enhances organization's contribution to business (highly-leveraged benefit).
- Ex: Reducing headcount by one might save $100,000 per year; but if greater effectiveness means one more strategic project each year, benefits could be counted in millions.

- Cpt: Reasons Well-Designed Structure Improves Effectiveness.
  - Gaps eliminated: Assigning accountability for missing lines of business can deliver value not available from old organization (even if not full-time jobs); if Engineers or Service Providers missing, filling gaps delivers new products and services; creating new Sales function in internal service provider improves relationships and strategic alignment, should lead to ongoing stream of very high-payoff projects; if Coordinator functions missing, filling gaps improves product architecture and standardization, planning, policies, safety (security, compliance, risk).
  - Specialization increases: As scattered campuses consolidated, and by choosing right basis for substructure, impossibly diverse jobs replaced with well-focused specialties; staff become more competent, conflicts of interests eliminated; greater focus and specialization produces improved productivity, faster and more reliable delivery, higher quality, lower risk, more innovation, less stress, greater staff motivation.
  - Accountabilities for results clear: Groups defined as lines of business, accountable for delivering products and services; results-orientation delivers results; helps clients and internal customers, easy to know where to go for needs; precise domains facilitate performance management (easier to hold staff accountable for results-based metrics); people feel good about jobs when see value of work to customers.
  - Teamwork enhanced: Teamwork not limited to few visible projects where executives assemble teams; happens all time, whenever any group gets help from peers; better teamwork improves performance; instead of each group attempting to be self-sufficient, best talent from wide range of relevant specialties contributes to each project; produces far better results than generalists working alone.
  - Organization scalable: Healthy structure makes easier for organization to grow, take on new technologies and missions, integrate acquisitions and consolidations; not only clear where new opportunities fit, clear who's accountable for discovering them; for internal service providers, changes in clients' structure or strategies have minimal impact on organization's structure (outside of Account Sales); entirely possible to design structure that lasts lifetime, evolving naturally as new opportunities arise without need for another major restructuring.
  - Executive bottleneck eliminated: Empowered staff don't need to be micro-managed; executives can rise above day-to-day and focus on more strategic challenges. |
    | MEYER-SEC-0182 | 11.1.3. Cultural Transformation | - Def: In addition to improved efficiency and effectiveness, healthy structure has powerful impacts on organization's culture.

- Cpt: Empowerment.
  - Def: When jobs defined by what people "sell" (results), accountabilities well defined; staff can be empowered to produce results as see fit.
  - Res: Improves reliable delivery, since people have resources and authorities need to get job done.
  - Res: Encourages creativity and innovation, as staff think about best ways to accomplish results agreed to deliver.
  - Res: Encourages quality, since staff fully responsible for own results; people know have to maintain what sell; incentive to do things right first time, rather than wasting time and money correcting mistakes later; core principle of Total Quality Management embedded into fabric of organization.

- Cpt: Customer Focus.
  - Def: Running businesses within business, staff recognize funded (given budget) to serve customers, both within and outside organization.
  - Res: Focus on delivering products and services to customers, rather than on bureaucratic territories, procedures, tasks.
  - Res: Understand what customers want by listening, responding to customers' priorities (not own).
  - Res: Build effective working relationships with customers, pleasant to do business with.

- Cpt: Entrepreneurship.
  - Def: Since groups defined as lines of business, everybody is entrepreneur.
  - Res: Entrepreneurs know have to be reliable to stay in business; learn not to make commitments can't keep, to keep every commitment.
  - Res: Entrepreneurs continually seek new opportunities to add value; proactively discover ways to contribute to customers' success.
  - Res: Entrepreneurs optimize costs and methods; continually seek ways to deliver more value at lower cost.
  - Res: Entrepreneurs plan future of businesses; develop strategies, invest in capabilities, evolve product lines. |
  -
    #### ID
    MEYER-SEC-0183
    #### Title
    11.2. Key Takeaways
    #### Text
    - Fnd: Structure matters; affects every aspect of organizational performance (efficiency, effectiveness, culture).
- Fnd: Seven Principles provide scientific foundation for organizational design: Golden Rule (authority = accountability), Specialization and Teamwork, Precise Domains, Basis for Substructure, Avoid Conflicts of Interests, Cluster by Professional Synergies, Business Within Business.
- Fnd: Five Building Blocks (Engineers, Service Providers, Coordinators, Sales/Marketing, Audit) provide common language for analyzing and designing organizations.
- Fnd: Rainbow Analysis diagnostic method reveals structural problems: Gaps, Rainbows, Scattered Campuses, Inappropriate Substructure.
- Fnd: Teamwork processes essential complement to organization chart; can't specialize if can't team.
- Fnd: Special situations (self-managed groups, shared people, remote locations, PMO, compliance) can be addressed without compromising Principles.
- Fnd: Implementation requires participative process, careful planning, patience; benefits develop over time.
- Fnd: Well-designed structure lasts lifetime, evolving naturally without need for major restructuring.
-
  #### ID
  MEYER-SEC-0184
  #### Title
  12. Conclusion
  #### Text
  - Fnd: Organizational structure not just boxes on chart; comprehensive system encompassing organization chart, domains, teamwork processes, culture, resource-governance.
- Fnd: Science of structure based on timeless principles, not fads or fashions; principles apply across industries, functions, cultures, organization types.
- Fnd: Structure enables or constrains everything organization does; good people can overcome bad structure, but at great cost; well-designed structure multiplies effectiveness of every person.
- Fnd: Investment in getting structure right pays dividends forever; structure that embodies Principles becomes self-sustaining, self-correcting system.
- Rec: Leaders must become students of organizational science; understand principles, apply diagnostic methods, invest in proper design and implementation.
- Rec: Structure not one-time project; ongoing stewardship responsibility; leaders must continually reinforce principles, resist pressures to compromise, help organization evolve within framework.
- Fnd: Ultimate goal: organization where everyone empowered entrepreneur, running business within business, collaborating seamlessly across boundaries, continually discovering new ways to add value to customers.
