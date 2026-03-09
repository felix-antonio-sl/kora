---
_manifest:
  urn: urn:gn:kb:plan-potenciamiento-dgi
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
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
    cr: 104.35
    run_id: gn-smoke
    review_gate: auto
    scope_statement: Plan DGI con dependencias core declaradas.
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 21
    meat_count: 1170
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/gobernanza__plan-potenciamiento-dgi.md.json
---

# Plan de Potenciamiento DGI

## Alcance
Plan DGI con dependencias core declaradas.
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
| ID | Title | XRef |
| --- | --- | --- |
| POT-SYN-01 | Perspectiva Meyer: Estructura como Ciencia | urn:mgmt:kb:meyer-org-structure |
| POT-SYN-02 | Perspectiva Lean Six Sigma: Mejora Sistemática | urn:mgmt:kb:lean6 |

## IntegrationArchitecture
| ID | Title |
| --- | --- |
| POT-ARQ-01 | Arquitectura de Building Blocks (Meyer) |
| POT-ARQ-02 | Catálogo de Productos DGI |
| POT-ARQ-03 | Relaciones Cliente-Proveedor |

## DMAICFramework
| ID | Title |
| --- | --- |
| POT-DMAIC-01 | Marco Operativo DMAIC para DGI |
| POT-DMAIC-02 | Sistema 5S para Gestión del Conocimiento |
| POT-DMAIC-03 | Proyecto Piloto DMAIC Sugerido |
| POT-DMAIC-04 | Tablero Kanban para Gestión de Iniciativas |

## SocialNavigation
| ID | Title |
| --- | --- |
| POT-SOC-01 | El Rol del Navegador Institucional |
| POT-SOC-02 | Mapa de Stakeholders GORE |
| POT-SOC-03 | Modelo ADKAR para Gestión del Cambio |
| POT-SOC-04 | Tácticas de Influencia Ética |
| POT-SOC-05 | Detección y Manejo de Resistencias |
| POT-SOC-06 | Métricas de Éxito Social |

## CognitiveModels
| ID | Title | Purpose | Dimensions |
| --- | --- | --- | --- |
| POT-CM-01 | CM-LEAN-THINKING | Evaluar situaciones desde la perspectiva de mejora continua | Identificar desperdicios (7+1 mudas): sobreproducción, esperas, transporte, sobreproceso, inventario, movimiento, defectos, talento subutilizado, Aplicar ciclo PDCA: Plan-Do-Check-Act, Priorizar por impacto/esfuerzo, Buscar causa raíz antes de solucionar, Preferir mejoras pequeñas y constantes |
| POT-CM-02 | CM-STRUCTURE-PRINCIPLES | Evaluar propuestas organizacionales según ciencia de Meyer | Verificar coincidencia autoridad-responsabilidad, Confirmar dominios precisos sin superposición, Evaluar especialización vs. generalización, Detectar conflictos de interés potenciales, Validar agrupación por sinergias profesionales, Aplicar paradigma 'negocio dentro del negocio' |
| POT-CM-03 | CM-SOCIAL-NAVIGATION | Evaluar dimensión social de cambios organizacionales | Mapear stakeholders y sus intereses, Aplicar ADKAR: ¿Tiene awareness, desire, knowledge, ability, reinforcement?, Seleccionar táctica de influencia apropiada, Detectar tipo de resistencia (racional, emocional, política), Planificar comunicación y acompañamiento |
| POT-CM-04 | CM-DMAIC-EVALUATOR | Evaluar proyectos de mejora según metodología DMAIC | DEFINE: ¿Problema claro? ¿Alcance definido? ¿Sponsor identificado?, MEASURE: ¿Línea base establecida? ¿Datos confiables?, ANALYZE: ¿Causa raíz identificada? ¿Priorización por impacto?, IMPROVE: ¿Solución diseñada? ¿Pilotaje realizado?, CONTROL: ¿Controles establecidos? ¿Transferencia a operación? |

## Fuentes derivadas
### Kb gn lean6 core koda
- Fuente: `core/gestion/kb_gn_lean6_core_koda.yml`
- Tipo: estructurado
- Claves: Source, Warn, XRef_Required, Scope, Metrics, Topics
### Kb gn meyer org structure koda
- Fuente: `core/gestion/kb_gn_meyer_org_structure_koda.yml`
- Tipo: estructurado
- Claves: Source, Warn, XRef_Required, XRef, Metrics, Principle_Based_Organizational_Structure
