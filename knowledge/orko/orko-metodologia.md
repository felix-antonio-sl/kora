---
_manifest:
  urn: "urn:orko:kb:orko-metodologia"
  provenance:
    created_by: "FS"
    created_at: "2026-01-29"
    source: "ORKO framework documentation"
version: "2.0.0"
status: published
tags: [metodologia, WSLC, fases, playbooks, governance]
lang: es
---

# ORKO - Metodología (Layer 3)

Sistema operativo organizacional adaptable y formal para guiar transformaciones complejas. Work-System Lifecycle (WSLC) de 18 fases + Catálogo de 15 Playbooks activados por Health Gates.

## Filosofía

Minimalidad, Ortogonalidad, Accountability Humana (HAIC), Adaptación basada en Datos.

## WSLC - Fases (F1-F18)

### Initiation (F1-F3)

#### F1 - Context Assessment

**Propósito:** Capturar estado organizacional actual (E6_current), H_org baseline y perfil de contexto (36 params)

**Inputs:** Stakeholder Interviews, Org Docs, Regulatory Context

**Outputs:**
- context_profile_36_params
- h_org_baseline
- context_classification

**Owner:** Role_Captain

#### F2 - Vision Definition

**Propósito:** Definir visión, ambición y North Star alineada con restricciones del contexto

**Inputs:** F1.context_profile, F3.trajectory_selected

**Outputs:** vision_statement.md, okr_L4, vision_constraints

**Owner:** Role_Captain + Sponsor_L1_Human

**Protocolo:** F2_F3_convergence (circular dependency)

#### F3 - Trajectory Selection

**Propósito:** Seleccionar trayectoria óptima (Survival, Minimal, Avanzada) basada en decisión matrix formal

**Inputs:** F1.h_org_baseline, Budget/Runway

**Outputs:** trajectory_selected, timeline_commitment, budget_allocation

**Owner:** Role_Captain + Sponsor_L1_Human

### Development (F4-F9)

#### F4 - Capability Mapping

**Propósito:** Inventariar y mapear capacidades (P1) humanas, algorítmicas y mixtas

**Inputs:** F2.vision, F3.trajectory

**Outputs:** p1_inventory.yaml, skills_matrix, capacity_gaps

**Owner:** Role_Architect

#### F5 - Flow Design

**Propósito:** Diseñar flujos de valor (P2) y optimizar handoffs

**Inputs:** F4.p1_inventory, F7.okr_cascade

**Outputs:** vsm_maps, handoff_ratio_metrics, flow_optimization_plan

**Owner:** Role_Architect

#### F6 - Information Architecture

**Propósito:** Diseñar arquitectura de información (P3), dominios de datos y governance

**Inputs:** F1.context, F7.okrs

**Outputs:** data_catalog, architecture_blueprint, information_governance

**Owner:** Role_Architect (Data)

#### F7 - Purpose Cascade

**Propósito:** Cascadear OKRs (P5) desde L4 (Org) hasta L3/L2/L1 según trayectoria, asignando accountability humana

**Inputs:** F2.okr_L4, F3.trajectory

**Outputs:** okr_cascade_L4_to_L1.yaml, purpose_policy, alignment_matrix

**Owner:** Role_Captain + Leaders

**Invariant:** I5_HAIC: Every OKR must have a Human Owner

#### F8 - Limits Definition

**Propósito:** Formalizar límites (P4) regulatorios, técnicos y presupuestarios

**Inputs:** F1.regulatory_constraints, F3.budget

**Outputs:** limit_catalog.yaml, compliance_framework_refs

**Owner:** Role_Architect (Governance)

#### F9 - Target State Design

**Propósito:** Sintetizar diseños F4-F8 en un Estado Arquitectónico Objetivo (E6_target)

**Inputs:** F4-F8 outputs, F3.trajectory

**Outputs:** e6_target.yaml, target_diagrams, gap_analysis_current_target

**Owner:** Role_Architect

### Implementation (F10-F12)

#### F10 - Quick Wins

**Propósito:** Ejecutar acciones de alto impacto y bajo esfuerzo para ganar momentum y mejorar H_org temprano

**Inputs:** F9.gap_analysis, F5.vsm_maps

**Outputs:** quick_wins_backlog, execution_log, h_org_early_impact

**Owner:** Role_Delivery_Lead

#### F11 - Fabric Deployment

**Propósito:** Desplegar cambios estructurales en Tejidos (TF1, TF2, TF3)

**Inputs:** F9.target_schemas, F9.e6_target

**Outputs:** fabric_deployment_plan, tf1/tf2/tf3_status

**Owner:** Role_Delivery_Lead

#### F12 - State Transition

**Propósito:** Orquestar la transición formal de E6_current a E6_target (migraciones, reorgs)

**Inputs:** F9.e6_target, F11.fabric_status

**Outputs:** state_transition_plan, e6_intermediate_states

**Owner:** Role_Architect + Delivery

### Operation (F13-F15)

#### F13 - Health Monitoring

**Propósito:** Monitoreo continuo de métricas canónicas (H_org, eta_org) y activación de Health Gates

**Inputs:** Live Signals TF1/TF2/TF3

**Outputs:** h_org_dashboard, health_gate_status (G1-G4), playbook_triggers

**Owner:** Role_HealthOwner

#### F14 - Incident Response

**Propósito:** Gestión reactiva de incidentes y degradaciones de salud detectadas por F13

**Inputs:** F13.alerts, playbook_triggers

**Outputs:** incident_reports, recovery_actions, post_mortems

**Owner:** Role_IncidentLead

#### F15 - Continuous Execution

**Propósito:** Operación regular del sistema de trabajo (Sprints, BAU, Cadencia)

**Inputs:** Backlog F10/F11, F7.okrs

**Outputs:** execution_log, sprint_reports, cadence_adjustments

**Owner:** Role_Delivery_Lead

### Evolution (F16-F18)

#### F16 - Learning Loops

**Propósito:** Cerrar ciclos de aprendizaje, analizando correlación entre acciones y métricas

**Inputs:** F13.trends, F14.post_mortems, F15.reports

**Outputs:** learning_log, playbook_improvement_backlog, trajectory_recommendations

**Owner:** Role_Captain

#### F17 - Adaptation

**Propósito:** Formalizar decisiones de cambio de rumbo (Pivots, Trajectory Adjustments) vía ADRs

**Inputs:** F16.learnings, F13.trends

**Outputs:** trajectory_adjustment, adaptation_plan, okr_refinement

**Owner:** Role_SteeringCommittee

#### F18 - Convergence Check

**Propósito:** Validación final de convergencia hacia E6_target al cierre de ciclo

**Inputs:** F9.e6_target, F12.e6_current_post

**Outputs:** convergence_report, convergence_score, gap_analysis_residual

**Owner:** Role_Architect

## Playbooks (P01-P15)

### Recovery (P01-P04, P09, P12, P13)

**Propósito:** Restaurar H_org ante degradaciones críticas (G1/G2)

| Playbook | Trigger | Duración |
|----------|---------|----------|
| P01_Low_H_org_Recovery | H_org < 60 (Critical) | 1D |
| P02_Handoff_Reduction | Handoff Ratio > 30% (High Friction) | 2D |
| P03_OKR_Alignment | OKR Alignment Score < 0.6 (Strategic Drift) | 3D |
| P04_Security_Remediation | P4 Limit Breach / Security Incident | 2D |
| P09_Drift_Detection | Drift relevant E6_current vs target | 3D |
| P12_Data_Quality_Recovery | Data quality issues impacting H_org | 2W |
| P13_Political_Alignment | Stakeholder conflicts / political barriers | 2W |

### Transformation (P05-P08, P10-P11)

**Propósito:** Cambios estructurales proactivos para mejorar eta_org y ROI

| Playbook | Trigger | Duración |
|----------|---------|----------|
| P05_Bounded_Autonomy_M6 | H_org high + eta_org low (Stagnation) | 4W |
| P06_Pilot_Transformation | Trajectory Milestone / New Innovation | 4W |
| P07_Scale_Transformation | Pilot Success confirmed by F16 | 8W |
| P08_Optimization_Sustain | Post-Transformation Stabilization | 4W |
| P10_Capacity_Gap_Resolution | Missing Skills / Capacity Bottleneck | 4W |
| P11_Flow_Optimization | Cycle Time degradation | 3W |

### Operational (P14-P15)

**Propósito:** Ajustes tácticos durante operación continua

| Playbook | Trigger | Duración |
|----------|---------|----------|
| P14_Client_Expectation_Mgmt | NPS Drop / Client Churn risk | 3D-7D |
| P15_Adaptive_Cadence | Volatility up / Velocity down | 2W-8W |

## Governance

### Roles

| Rol | Responsabilidades |
|-----|-------------------|
| Role_Captain | Orquestador metodológico general. Accountable F1-F3, F7, F16 |
| Role_Architect | Guardián integridad técnica (D1). Accountable F4, F5, F6, F8, F9, F18 |
| Role_HealthOwner | Guardián H_org (D2). Accountable F13 y activación Playbooks |
| Role_Delivery_Lead | Líder ejecución (D4). Accountable F10, F11, F15 |
| Role_IncidentLead | Líder efímero para F14 |
| Sponsor_L1_Human | Ejecutivo responsable decisiones estratégicas y presupuesto |

### Rituales

| Ritual | Frecuencia | Propósito |
|--------|-----------|----------|
| Health_Check_Weekly | Semanal | Revisión F13 H_org y health gates |
| Steering_Committee_Monthly | Mensual | Revisión F17 trayectoria y adaptación |
| Learning_Review_Quarterly | Trimestral | Sesión F16 aprendizaje profundo |

## Validación

### Invariantes I1-I8

| Invariante | Status |
|-----------|--------|
| I1_Minimalidad | Fases necesarias y suficientes. Playbooks ortogonales |
| I2_Ortogonalidad | Mapeo D1-D4 a Fases limpio sin overlap |
| I3_Trazabilidad | Todo artefacto traza a Primitivos P1-P5 |
| I5_HAIC | Todo rol y ownership explícitamente humano |
| I6_Trajectory | Metodología soporta 3 trayectorias diferenciadas |
| I8_Adaptacion | F16/F17 garantizan evolución del sistema |

**Estado:** VALIDADO ✅
