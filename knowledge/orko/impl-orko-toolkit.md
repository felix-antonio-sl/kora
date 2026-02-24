---
_manifest:
  urn: "urn:orko:kb:impl-orko-toolkit"
  provenance:
    created_by: "FS"
    created_at: "2026-01-29"
    source: "ORKO framework documentation"
version: "2.0.0"
status: published
tags: [implementacion, toolkit, kits, playbooks, templates, diagnostico, ejecucion]
lang: es
---

# ORKO - Toolkit Implementación (Layer 4-5)

Compilación práctica de calculadoras, kits y templates para implementar ORKO v1.0.0. Herramientas consumibles por roles humanos (Excel, Markdown) y máquinas (YAML, JSON). Guía de uso del toolkit completo.

## Comience Aquí

### Paso 1: DIAGNOSTIQUE (1-2 horas)

1. Abra carpeta `01_DIAGNOSTICO`
2. Abra `1.1_Inventario_Maestro.xlsx` - Liste lo que su organización tiene hoy (personas, flujos, datos)
3. Abra `1.2_Calculadora_Salud.xlsx` - Use el WIZARD para transferir totales del inventario
4. Obtenga su **Health Score (H_org)** y su **Banda de Salud** (ej: G1-Crítico, G3-Aceptable)

### Paso 2: SELECCIONE SU RUTA

Use su `H_org` para decidir qué carpeta abrir en `02_EJECUCION`:

| H_org | Estado | Kit |
|-------|--------|-----|
| < 0.50 | Crítico | A_Kit_Survival |
| 0.50 - 0.70 | Estable | B_Kit_Minimal |
| > 0.70 | Saludable | C_Kit_Avanzado |

### Paso 3: EJECUTE (2-12 semanas)

Entre a la carpeta de su Kit y siga las instrucciones del `README` interno.

**Survival:** Foco en apagar incendios y recuperar capacidad operativa.

**Minimal:** Foco en construir cimientos y optimizar flujos clave.

**Avanzado:** Foco en escala, automatización y gobernanza de datos.

### Paso 4: MONITOREE

Cada 2 semanas, actualice su Inventario y recalcule su `H_org`.

- ↗️ Si mejora: Migre al siguiente Kit
- ↘️ Si empeora: Active los protocolos de escalamiento (ver `03_REFERENCIA`)

## Diagnóstico (01_DIAGNOSTICO)

### Propósito

Entender el terreno antes de cambiar nada. Debe saber exactamente qué tiene.

### Herramientas

#### 1.1_Inventario_Maestro.xlsx (EL MAPA)

**Qué es:** Un censo de capacidades (personas/bots), flujos de trabajo y activos de datos

**Acción:** Llene las pestañas P1, P2 y P3. Busque completitud al 80%, no perfección.

**Estructura:**
- P1 Tab: Capacidades (humans, algorithms, mechanical)
- P2 Tab: Flujos (processes, pipelines, workflows)
- P3 Tab: Información (data assets, documents, systems)

#### 1.2_Calculadora_Salud.xlsx (EL TERMÓMETRO)

**Qué es:** Algoritmo que convierte inventario en puntaje único: `H_org` (Health Score)

**Acción:** Use pestaña WIZARD para copiar datos del Inventario

**Resultado:** Número entre 0.00 y 1.00

**Componentes Medidos:**
- H1: Human wellbeing, engagement, development, autonomy
- H2: Architecture clarity, span of control, alignment
- H3: Flow efficiency, waste reduction, cycle time
- H4: Perception freshness, observability, detection latency
- H5: Decision velocity, portfolio balance, execution rate

#### 1.3_Matriz_Decision.xlsx (LA BRÚJULA)

**Qué es:** Herramienta para cruzar H_org con presupuesto y riesgo para confirmar trayectoria

**Acción:** (Opcional) Úsela si está en el límite entre dos trayectorias (ej: 0.49 vs 0.51)

**Parámetros:** H_org baseline, Budget available, Timeline, Risk tolerance, Org complexity

**Output:** Trajectory recommendation (Survival / Minimal / Avanzada)

### Próximo Paso

Una vez tenga su H_org, vaya a carpeta `02_EJECUCION` y seleccione el Kit correspondiente.

## Ejecución (02_EJECUCION)

### Propósito

Aquí ocurre la transformación. No intente hacer todo a la vez.

### A_Kit_Survival (H_org < 0.50)

**Para quién:** Organizaciones en caos, alta rotación, incidentes frecuentes, falta capacidad crítica

**Objetivo:** Estabilizar el barco. Detener el sangrado.

**Duración:** 2-4 semanas mínimo

**Contenido:**
- Playbooks: P01 (Low H_org Recovery), P02 (Handoff Reduction), P04 (Security Remediation)
- Templates: T10 (Incident Report)
- Métricas: F13 Health Monitoring, F14 Incident Response
- Goal: H_org > 60 en 7-14 días

**Tareas Inmediatas:**
1. Ejecute P01_Low_H_org_Recovery.md - Recuperar capacidad crítica (5 días)
2. Ejecute P02_Handoff_Reduction.md - Eliminar fricción en flujos críticos
3. Si brechas seguridad: P04_Security_Remediation.md
4. Use T10_Incident_Report.md para documentar y aprender

### B_Kit_Minimal (H_org 0.50 - 0.70)

**Para quién:** Organizaciones estables pero lentas, burocráticas, desconectadas estrategia

**Objetivo:** Construir cimientos sólidos. Conectar estrategia con ejecución.

**Duración:** 12-18 semanas

**Contenido:**
- Fases completas: F1-F18 (WSLC)
- Playbooks: P01-P15 (todas disponibles)
- Templates: T01-T15 (planning, execution, evolution)
- Énfasis: F4 (Capability), F5 (Flow), F7 (Purpose Cascade)

**Estructura típica:**
- Weeks 1-2: F1 Context Assessment
- Weeks 3-4: F2-F3 Vision + Trajectory
- Weeks 5-12: F4-F9 Design phases
- Weeks 13-16: F10-F12 Implementation
- Weeks 17-18: F13-F18 Operation & Evolution

### C_Kit_Avanzado (H_org > 0.70)

**Para quién:** Organizaciones de alto rendimiento buscando optimización, escala, gobernanza

**Objetivo:** Excelencia operativa. Innovación continua.

**Duración:** 18-36 semanas

**Contenido:**
- Todas las fases y playbooks
- Advanced playbooks: P05-P08 (Transformation focus)
- Énfasis: Autonomy design, Pilot→Scale patterns, Continuous optimization

---

**Nota:** Si tiene dudas, empiece por **Kit Minimal**. Es más fácil agregar complejidad después que quitarla.

## Referencia (03_REFERENCIA)

### Guía Uso Calculadoras

Instrucciones detalladas para cada calculadora:

- health_score_calculator.xlsx: Cálculo H_org, impacto componentes, trend analysis
- budget_parametric_allocator.xlsx: Estimación presupuesto y timeline por trayectoria
- roi_estimator.xlsx: Proyección ROI transformación y habilitación
- convergence_tracker.xlsx: Tracking convergencia E6_current vs E6_target

### Vocabulario Controlado

Definiciones canónicas de términos ORKO:

**Layer 0:** Axiomas (A1-A5), Primitivos (P1-P5), Invariantes (I1-I8)

**Layer 1:** Contratos (C1-C5), Dominios (D1-D4), Métricas (H_org, eta_org, ROI_Habilitacion)

**Layer 2:** Tejidos (TF1, TF2, TF3), Concerns transversales (Security, Purpose, Observability)

**Layer 3:** Fases (F1-F18), Playbooks (P01-P15), Trayectorias (Survival, Minimal, Avanzada), Health Gates (G1-G4)

**Layer 4:** Templates (T01-T15), Calculadoras, Developer tools

## Soporte (04_SOPORTE)

### Casos de Prueba

Validación de herramientas y templates contra escenarios reales:

- Caso 7 Validación: Organización de 500 personas, H_org = 0.62, transformación Minimal
  - Context assessment results
  - Health score calculation
  - Trajectory selection recommendation
  - Budget and timeline projections

## Integración con Metodología

### Mapeo Toolkit ← Fases WSLC

| Fase | Herramienta | Output |
|------|-----------|--------|
| F1 Context Assessment | T01_context_assessment.yaml | context_profile_36_params |
| F2 Vision Definition | T02_vision_statement.md | vision_statement.md |
| F3 Trajectory Selection | context_decision_matrix.xlsx | trajectory_selected |
| F4 Capability Mapping | T04_capacity_inventory.xlsx | p1_inventory.yaml |
| F5 Flow Design | T05_vsm_template.drawio | vsm_maps |
| F6 Information Architecture | T06_data_catalog.xlsx | data_catalog |
| F7 Purpose Cascade | T07_okr_cascade.xlsx | okr_cascade_L4_to_L1.yaml |
| F8 Limits Definition | regulatory_compliance_tracker.xlsx | limit_catalog.yaml |
| F13 Health Monitoring | health_score_calculator.xlsx | h_org_dashboard |
| F14 Incident Response | T10_incident_report.md | incident_reports |
| F15 Continuous Execution | T08_weekly_checkin.md | execution_log |
| F16 Learning Loops | T09_retrospective.md | learning_log |
| F17 Adaptation | T12_adr_template.md | ADRs |
| F18 Convergence Check | convergence_tracker.xlsx | convergence_report |

### Mapeo Playbooks ← Templates

| Playbook | Template | Artefacto |
|----------|----------|----------|
| P01 Low H_org Recovery | health_score_calculator.xlsx | h_org_recovery_plan.yaml |
| P03 OKR Alignment | T07_okr_cascade.xlsx | okr_alignment_plan.yaml |
| P06 Pilot Transformation | T05_vsm_template.drawio | pilot_transformation_plan.yaml |
| P10 Capacity Gap Resolution | T04_capacity_inventory.xlsx | capacity_gap_resolution_plan.yaml |
| P14 Client Expectation Mgmt | T02_vision_statement.md | communication_pack |

## Notas Implementación

### Validación Herramientas

- Calculadoras consistentes con fórmulas Layer 1 (H_org, ROI, eta_org)
- Templates cubren inputs/outputs de todas Fases F1-F18
- Trazabilidad completa: Tool → Phase → Primitive → Axioma

### Personalización

Cada organización puede:
- Ajustar pesos en health_score_calculator según contexto (PD36: 36 parámetros)
- Extender vocabulario_controlado.yaml con términos domain-específicos
- Crear templates adicionales para dominios especializados

### Governance

- Owner de toolkit: Layer 4 Implementation Lead
- Update frequency: Quarterly (con ciclos aprendizaje F16-F17)
- Version control: Git repository con schema validation

## Estado

**Validado:** ✅

**Última actualización:** 2026-02-19

**Próximo ciclo:** 2026-05-19 (aprendizajes de 5+ implementaciones Minimal)
