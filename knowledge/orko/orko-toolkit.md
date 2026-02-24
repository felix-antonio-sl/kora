---
_manifest:
  urn: urn:orko:kb:orko-toolkit
  provenance:
    created_by: FS
    created_at: '2026-01-29'
    source: ORKO framework documentation
version: 2.0.0
status: published
tags:
- toolkit
- implementacion
- calculadoras
- templates
- herramientas
- knowledge
lang: es
---

# ORKO - Toolkit de Implementación (Layer 4)

- Conjunto de herramientas prácticas (templates y calculadoras) para implementar la metodología.
- Artefactos consumibles por roles humanos (Excel, Markdown) y máquinas (JSON, YAML).


- **Scope:** Layer 4-5 (Implementación)


- **Developer Mode:** Las calculadoras se generan programáticamente desde dev_specs (Python)


## Calculadoras Principales

### Health Score Calculator

- **Archivo:** health_score_calculator.xlsx


- **Propósito:** Cálculo formal de H_org y componentes (H1-H5)


- **Inputs:**

- Métricas Layer 1 (metric_id, value)
- Pesos contextuales

- **Outputs:**

- H_org score (0-100)
- Radar chart
- Health Gate status

- **Fases:** F1, F13, F18


### Budget Parametric Allocator

- **Archivo:** budget_parametric_allocator.xlsx


- **Propósito:** Estimación paramétrica de presupuesto y timeline según trayectoria


- **Inputs:**

- Trajectory (Survival/Minimal/Avanzada)
- Headcount
- Rates

- **Outputs:**

- Budget total
- Allocation por Fase
- Timeline estimado

- **Fases:** F3, F8


### ROI Estimator

- **Archivo:** roi_estimator.xlsx


- **Propósito:** Proyección de retorno de inversión de transformación y habilitación


- **Inputs:**

- Cost of Delay
- Efficiency gains (%)
- Implementation cost

- **Outputs:**

- ROI_Habilitacion
- Payback period
- NPV

- **Fases:** F3, F15, P05


### Context Decision Matrix

- **Archivo:** context_decision_matrix.xlsx


- **Propósito:** Matriz de decisión para selección de trayectoria basada en 36 parámetros


- **Fases:** F1, F3


### Convergence Tracker

- **Archivo:** convergence_tracker.xlsx


- **Propósito:** Tracking de convergencia arquitectónica E6_current vs E6_target


- **Fases:** F12, F18


### Regulatory Compliance Tracker

- **Archivo:** regulatory_compliance_tracker.xlsx


- **Propósito:** Seguimiento de cumplimiento normativo (P4 Límite)


- **Fases:** F8, P04


## Templates

### Assessment

| ID | Nombre | Fase | Formato | Path |
|----|--------|------|---------|------|
| T01 | Context Assessment | F1 | YAML → Excel | 01_assessment/T01_context_assessment.yaml |
| T02 | Vision Statement | F2 | Markdown | 01_assessment/T02_vision_statement.md |
| T03 | Stakeholder Matrix | F1 | CSV | 01_assessment/T03_stakeholder_matrix.csv |

### Planning

| ID | Nombre | Fase | Formato | Path |
|----|--------|------|---------|------|
| T04 | Capacity Inventory | F4 | Excel | 02_planning/T04_capacity_inventory.xlsx |
| T05 | VSM Template | F5 | Draw.io | 02_planning/T05_vsm_template.drawio |
| T06 | Data Catalog | F6 | Excel | 02_planning/T06_data_catalog.xlsx |
| T07 | OKR Cascade | F7 | Excel | 02_planning/T07_okr_cascade.xlsx |

### Execution

| ID | Nombre | Fase | Formato | Path |
|----|--------|------|---------|------|
| T08 | Weekly Check-in | F15 | Markdown | 03_execution/T08_weekly_checkin.md |
| T09 | Retrospective | F16 | Markdown | 03_execution/T09_retrospective.md |
| T10 | Incident Report | F14 | Markdown | 03_execution/T10_incident_report.md |
| T11 | Xanpan Board | F15 | Image | 03_execution/T11_xanpan_board.png |

### Evolution

| ID | Nombre | Fase | Formato | Path |
|----|--------|------|---------|------|
| T12 | ADR Template | F9/F17 | Markdown | 04_evolution/T12_adr_template.md |
| T13 | User Story | F4 | Markdown | 04_evolution/T13_user_story.md |
| T14 | Planning Poker | F4 | Excel | 04_evolution/T14_planning_poker.xlsx |
| T15 | DORA Dashboard | F13 | JSON | 04_evolution/T15_dora_dashboard.json |

## Developer Tools

### Scripts

| ID | Path | Descripción |
|----|------|-------------|
| generate_calculadoras | dev_specs/scripts/generate_calculadoras_cap22.py | Script maestro Python para regenerar archivos Excel desde specs |

### Specs

| Path | Descripción |
|------|-------------|
| dev_specs/specs/ | Archivos YAML/JSON que definen la lógica de cálculo |

## Validación

- **Estado:** VALIDADO ✅


- **Checklist:**

- Calculadoras consistentes con fórmulas Layer 1 (H_org, ROI)
- Templates cubren inputs/outputs de Fases F1-F18
- Trazabilidad completa: Tool → Phase → Primitive
