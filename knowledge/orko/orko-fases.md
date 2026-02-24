---
_manifest:
  urn: "urn:orko:kb:orko-fases"
  provenance:
    created_by: "FS"
    created_at: "2026-01-29"
    source: "ORKO framework documentation"
version: "2.0.0"
status: published
tags: [fases, WSLC, workflow, ciclos, transformacion]
lang: es
---

# ORKO - Fases Metodología WSLC (Layer 3)

Metodología de 18 fases (F1-F18) que operacionaliza las transformaciones organizacionales. Contratos de decisión con trayectorias, health gates y protocolo de convergencia F2↔F3.

## Introducción Metodología

**Definición:** Sistema operativo organizacional adaptable y formal para guiar transformaciones complejas.

**Core Concept:** Work-System Lifecycle (WSLC) de 18 fases + Catálogo de 15 Playbooks activados por Health Gates.

**Filosofía:** Minimalidad, Ortogonalidad, Accountability Humana (HAIC), Adaptación basada en Datos.

## Mapeo Dominios (D1-D4) a Fases

Las 18 fases operacionalizan los 4 dominios arquitectónicos:

| Fase | D1_Arq | D2_Perc | D3_Dec | D4_Oper | Primitivos |
|------|--------|---------|--------|---------|-----------|
| F1 Context Assessment | ◐ | ●●● | ◐ | ○ | P1-P5 (scan) |
| F2 Vision Definition | ◐ | ◐ | ●● | ○ | P5 (propósito) |
| F3 Trajectory Selection | ○ | ◐ | ●●● | ○ | Decision |
| F4 Capability Mapping | ●● | ◐ | ○ | ○ | P1 |
| F5 Flow Design | ●● | ◐ | ○ | ○ | P2 |
| F6 Information Architecture | ●●● | ◐ | ○ | ○ | P3 |
| F7 Purpose Cascade | ● | ○ | ○ | ○ | P5 |
| F8 Limits Definition | ● | ◐ | ●● | ○ | P4 |
| F9 Target State Design | ●●● | ○ | ●● | ○ | E6 target |
| F10 Quick Wins | ○ | ○ | ● | ●● | Delivery |
| F11 Fabric Deployment | ●● | ○ | ● | ●● | TF1-TF3 |
| F12 State Transition | ○ | ● | ● | ●● | E6 evolve |
| F13 Health Monitoring | ○ | ●●● | ○ | ●● | H_org sensing |
| F14 Incident Response | ○ | ●● | ●● | ●●● | Remediation |
| F15 Continuous Execution | ○ | ◐ | ● | ●●● | Xanpan |
| F16 Learning Loops | ○ | ●● | ● | ● | Retrospectives |
| F17 Adaptation | ◐ | ●● | ●●● | ○ | I6 trajectory |
| F18 Convergence Check | ○ | ●● | ● | ○ | E6 validation |

**Leyenda:** ●●● Primario (75-100%) | ●● Secundario (40-70%) | ● Terciario (15-35%) | ◐ Implícito (<15%) | ○ No aplica

## Trayectorias Soportadas

### Trayectoria Survival (6-12 meses)

**Para:** Organizaciones en crisis (H_org < 50)

**Objetivo:** Estabilizar el barco. Detener el sangrado.

**Fases Mínimas:** F1, F2, F3, F13, F14, P01-P04

**No incluye:** Diseño arquitectónico completo, transformación profunda

### Trayectoria Minimal (12-18 meses)

**Para:** Organizaciones estables pero lentas (H_org 50-70)

**Objetivo:** Construir cimientos sólidos. Conectar estrategia con ejecución.

**Fases Completas:** F1-F18

**Énfasis:** Capability mapping, Flow design, Purpose cascade

**Playbooks:** P01-P15 (todas disponibles)

### Trayectoria Avanzada (18-36 meses)

**Para:** Organizaciones de alto rendimiento (H_org > 70)

**Objetivo:** Excelencia operativa. Innovación continua.

**Fases Completas:** F1-F18 + iteraciones profundas

**Énfasis:** Advanced autonomy (M6), Pilot→Scale transformations

**Playbooks:** P05-P08 prioritarios (transformation focus)

## Protocolos Especiales

### F2-F3 Convergence Protocol

**Naturaleza:** Circular dependency entre Vision Definition (F2) y Trajectory Selection (F3)

**Problema Resuelto:**
- F2 requiere trayectoria para definir visión (input)
- F3 requiere visión para seleccionar trayectoria (input)

**Solución:**
1. F1 completa (context_profile_36_params)
2. F3 propone trajectory_baseline basada en H_org + budget
3. F2 define vision_draft compatible con trayectoria
4. F3 valida/ajusta trayectoria vs vision_refined
5. Iteran hasta convergencia (típicamente 2-3 ciclos)

**Ownership:** Role_Captain + Sponsor_L1_Human (Semanal)

## Health Gates (G1-G4)

### G1 - H_org Crítico

**Condición:** H_org < 60

**Nivel:** RED

**Fases:** F13, F14

**Playbooks Trigger:** P01, P02, P15

**Trayectoria:** Survival

**Acción:** Activación respuesta inmediata. Incident response (F14).

### G2 - H_org Bajo Riesgo

**Condición:** 60 ≤ H_org < 70

**Nivel:** YELLOW

**Fases:** F13, F16, F17

**Playbooks Trigger:** P01 (focalizado), P09

**Trayectoria:** Minimal

**Acción:** Recuperación estructurada. Análisis drift. Adaptación (F17).

### G3 - H_org Bueno, Eficiencia Baja

**Condición:** H_org ≥ 70 AND (eta_org < 0.60 OR ROI_Habilitacion < 1.0)

**Nivel:** YELLOW

**Fases:** F13, F4, F5

**Playbooks Trigger:** P10, P11, P03

**Trayectoria:** Minimal

**Acción:** Optimización capacidades y flujos. Gap resolution.

### G4 - Ready for Avanzada

**Condición:** H_org ≥ 70 AND eta_org ≥ 0.70 AND ROI_Habilitacion ≥ 1.2

**Nivel:** GREEN

**Fases:** F13, F17, F3

**Playbooks Trigger:** P05, P06, P07

**Trayectoria:** Avanzada

**Acción:** Escalamiento autonomía. Pilotos. Transformaciones controladas.

## Governance de Fases

### Roles Clave

| Rol | Responsabilidad |
|-----|-----------------|
| Role_Captain | Orquestación metodológica. Accountable F1-F3, F7, F16 |
| Role_Architect | Integridad técnica (D1). Accountable F4-F9, F18 |
| Role_HealthOwner | Salud org (D2). Accountable F13, playbook triggers |
| Role_Delivery_Lead | Ejecución (D4). Accountable F10-F11, F15 |
| Sponsor_L1_Human | Decisiones estratégicas, presupuesto, trade-offs |

### Rituales

| Ritual | Frecuencia | Owner | Propósito |
|--------|-----------|-------|----------|
| Phase Planning | Semanal (desarrollo), Bi-weekly (ops) | Role_Captain | Secuenciar phases, asignar capacity |
| Health Check | Semanal | Role_HealthOwner | Revisar H_org, activar playbooks |
| Steering | Mensual | Role_Captain + Sponsor | Evaluar trayectoria, pivots |
| Learning Review | Trimestral | Role_Captain | F16 deep retrospectives |

## Estimaciones de Duración

| Fase | Duración Typical | Variación |
|------|-----------------|-----------|
| F1 Context Assessment | 2-4 semanas | Org complexity |
| F2 Vision Definition | 2-3 semanas | Alignment cycles |
| F3 Trajectory Selection | 1-2 semanas | Sponsor availability |
| F4 Capability Mapping | 3-4 semanas | Inventory accuracy |
| F5 Flow Design | 4-6 semanas | Current state complexity |
| F6 Information Architecture | 4-6 semanas | Data landscape |
| F7 Purpose Cascade | 2-3 semanas | Org hierarchy depth |
| F8 Limits Definition | 2-3 semanas | Compliance complexity |
| F9 Target State Design | 3-4 semanas | Synthesis effort |
| F10 Quick Wins | 2-4 semanas | Number of wins |
| F11 Fabric Deployment | 4-8 semanas | TF1-TF3 scope |
| F12 State Transition | 2-4 weeks | Migration risk |
| F13 Health Monitoring | Continuous | Cadence 2-week |
| F14 Incident Response | 1-7 days | Incident severity |
| F15 Continuous Execution | Continuous | Sprint cadence |
| F16 Learning Loops | 4 hours/month | Review frequency |
| F17 Adaptation | 1-2 weeks | Pivot magnitude |
| F18 Convergence Check | 1 day | Analysis effort |

## Validación

**Invariantes Cumplidas:**
- I1_Minimalidad: 18 fases necesarias y suficientes
- I3_Trazabilidad: Todo artefacto traza a Primitivos P1-P5
- I5_HAIC: Todo role/ownership explícitamente humano
- I6_Trajectory: 3 trayectorias diferenciadas (Survival, Minimal, Avanzada)
- I8_Adaptacion: F16/F17 garantizan evolución

**Estado:** VALIDADO ✅
