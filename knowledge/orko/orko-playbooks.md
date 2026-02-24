---
_manifest:
  urn: "urn:orko:kb:orko-playbooks"
  provenance:
    created_by: "FS"
    created_at: "2026-01-29"
    source: "ORKO framework documentation"
version: "2.0.0"
status: published
tags: [playbooks, recovery, transformation, operational, P01-P15]
lang: es
---

# ORKO - Catálogo Playbooks (P01-P15)

Catálogo de 15 procedimientos estandarizados para responder a eventos específicos de transformación organizacional, principalmente desviaciones en salud detectadas por Health Gates.

## Estructura General Playbook

Cada playbook define:

| Elemento | Descripción |
|----------|-------------|
| ID | P01-P15 |
| Tipo | Recovery, Transformation, Operational |
| Trigger | Condición activación |
| Fundamento | Layer 0 axiomas, Layer 1 dominios |
| Interfaz | Inputs, outputs, dependencies |
| Ejecución | Pasos, criterios éxito, RACI |
| Duración | Estimación de tiempo |

## Recovery Playbooks (P01-P04, P09, P12, P13)

Restauran H_org ante degradaciones críticas (G1/G2).

### P01 - Low H_org Recovery

**Trigger:** H_org < 60 (Critical) O G1/G2 activado

**Duración:** 1D

**Fundamento:**
- Layer 0: A1, A5, P1, P4, I3, I6
- Layer 1: D2, D4, E6
- Layer 2: TF1, TF2

**Pasos:**
1. Diagnóstico inmediato (2-4h): Identificar componentes H_org degradados (H1-H4)
2. Priorizar acciones (2h): Top-3 gaps críticos por impacto×urgencia
3. Plan recuperación (4h): Crear h_org_recovery_plan.yaml con timeline
4. Ejecutar quick wins (1-3 días): Acciones inmediatas (P10, P11, P12)
5. Monitorear recovery (continuo): Track H_org improvement vía F13

**Criterios Éxito:**
- H_org > 65 en 7-14 días
- Ningún componente H1-H4 < 50
- Recovery plan aprobado por Sponsor_L1_Human

**RACI:**
- Responsible: Role_HealthOwner, Role_Delivery_Lead
- Accountable: Sponsor_L1_Human
- Consulted: Role_Captain, TF1_Lead, TF2_Lead, TF3_Lead
- Informed: Board_Governance, All_Stakeholders

### P02 - Handoff Reduction

**Trigger:** H_org < 70 con handoffs altos en F5/F11 OR ROI_Habilitacion < 1.0

**Duración:** 2D

**Fundamento:**
- Layer 0: A1, A3, P2, I2, I3, I6
- Layer 1: D1, D4, E7
- Layer 2: TF2

**Pasos:**
1. Mapeo flujos (4-6h): Identificar handoffs críticos en TF2
2. Análisis impacto (2h): Cuantificar delay por handoff
3. Rediseño flujos (1 día): Reducir handoffs, aumentar bounded autonomy
4. Implementación (2-3 días): Ejecutar cambios flujo
5. Validación (continuo): Medir ROI_Habilitacion improvement

**Criterios Éxito:**
- Reducción > 30% handoffs críticos
- ROI_Habilitacion > 1.0
- H_org recovery

**RACI:**
- Responsible: Role_FlowOwner, TF2_Lead
- Accountable: Role_Captain
- Consulted: Role_Architect, Delivery_Lead
- Informed: Sponsor_L1_Human, Board_Governance

### P03 - OKR Alignment

**Trigger:** Desalineamiento OKR/propósito. H_org < target. eta_org < 0.60

**Duración:** 3D

**Pasos:**
1. Auditoría OKR (4h): Revisar cascade F7 vs resultados actuales
2. Gap analysis (4h): Identificar desconexión propósito-ejecución
3. Realinear OKRs (1 día): Ajustar o refinar OKRs con stakeholders
4. Communication plan (4h): Comunicar cambios a equipos
5. Tracking (continuo): Monitorear alineamiento post-ajuste

**Criterios Éxito:**
- 90% OKRs L4-L1 alineados
- H_org improvement > 5 puntos en 30 días
- Sponsor approval

### P04 - Security Remediation

**Trigger:** Incidente seguridad O gap cumplimiento que amenaza H_org/ROI_Habilitacion

**Duración:** 2D

**Pasos:**
1. Contención (inmediato): Mitigar riesgo security/compliance
2. Análisis impacto (4h): Evaluar impacto H_org y ROI_Habilitacion
3. Plan remediación (1 día): Definir acciones correctivas
4. Implementación (2-5 días): Ejecutar remediation plan
5. Post-mortem (4h): Documentar learnings y prevención

**Criterios Éxito:**
- Incident cerrado
- Compliance gap remediado
- H_org recovery
- Post-mortem publicado

### P09 - Drift Detection Response

**Trigger:** Degradación sostenida H_org/eta_org respecto a baseline. Drift E6_current vs E6_target

**Duración:** 3D

**Pasos:**
1. Detectar drift E6_current vs E6_target
2. Clasificar severidad
3. Plan corrección
4. Ejecutar
5. Validar convergencia

**RACI:**
- Responsible: Role_Architect, Role_HealthOwner
- Accountable: Role_Captain
- Consulted: TF1_Lead, TF2_Lead, TF3_Lead
- Informed: Sponsor_L1_Human

### P12 - Data Quality Recovery

**Trigger:** Problemas calidad datos en TF3/F6 impactando H_org/eta_org/ROI_Habilitacion

**Duración:** 2W

**Pasos:**
1. Auditar calidad datos TF3
2. Priorizar gaps críticos
3. Plan remediación
4. Ejecutar
5. Validar quality improvement

**RACI:**
- Responsible: Data_Quality_Owner, TF3_Lead
- Accountable: Role_Captain
- Consulted: Data_Engineers, Business_Analysts
- Informed: Sponsor_L1_Human, Data_Consumers

### P13 - Political Alignment

**Trigger:** Conflictos stakeholders O decisiones políticas degradan H_org sin causas técnicas

**Duración:** 2W

**Pasos:**
1. Identificar stakeholders clave
2. Mapear intereses y resistencias
3. Plan influencia
4. Ejecutar engagements
5. Validar alignment

**RACI:**
- Responsible: Role_Captain, Stakeholder_Manager
- Accountable: Sponsor_L1_Human
- Consulted: Communications, Change_Management
- Informed: Board_Governance, Key_Stakeholders

## Transformation Playbooks (P05-P08, P10-P11)

Cambios estructurales proactivos para mejorar eta_org y ROI.

### P05 - Bounded Autonomy (M6)

**Trigger:** H_org high + eta_org low (Stagnation) OR trayectoria Minimal→Avanzada

**Duración:** 4W

**Propósito:** Diseñar e implementar modelos de autonomía acotada (M6) para organizaciones con capacidad de supervisión suficiente

**Pasos:**
1. Diseñar modelo M6 autonomía
2. Pilotear con 1-2 equipos
3. Escalar
4. Monitorear eta_org

**RACI:**
- Responsible: Role_Architect, Transformation_Lead
- Accountable: Role_Captain
- Consulted: Team_Leads, TF1_Lead, TF2_Lead
- Informed: Sponsor_L1_Human, All_Teams

### P06 - Pilot Transformation

**Trigger:** Decisión ejecutar piloto transformación en dominio acotado

**Duración:** 4W

**Propósito:** Ejecutar piloto controlado para validar cambios antes de escalar

**Pasos:**
1. Seleccionar dominio piloto acotado
2. Diseñar intervención
3. Ejecutar piloto (2-4 semanas)
4. Evaluar resultados
5. Decidir escala

**Casos Típicos:**
- G4 activo + piloto limitado dominios críticos antes de escalar (P07)
- Recuperación eficiencia post-P10/P11 + validación multi-dominio
- Entrada nuevo mercado con bajo riesgo

### P07 - Scale Transformation

**Trigger:** Piloto (P06) exitoso con mejora sostenida en H_org/eta_org

**Duración:** 8W

**Propósito:** Escalar transformación piloto a más unidades/dominios

**Pasos:**
1. Validar piloto éxitoso
2. Planificar escala multi-dominio
3. Secuenciar rollout
4. Monitorear H_org durante escala
5. Ajustar según feedback

**Riesgos Mitigación:**
- Sobre-escala: Usar G1-G4 como frenos; si G2/G3, ralentizar
- Heterogeneidad contextos: Coordinar con E2 para validar patrones

### P08 - Optimization Sustain

**Trigger:** Transformación escalada; necesidad sostener/optimizar H_org/eta_org

**Duración:** 4W

**Propósito:** Mantener H_org/eta_org/ROI_Habilitacion evitando drift operativo

**Pasos:**
1. Identificar oportunidades optimización
2. Evaluar impacto global (ROI_Habilitacion)
3. Implementar mejoras
4. Monitorear sostenibilidad

**RACI:**
- Responsible: Continuous_Improvement_Lead, Operations_Lead
- Accountable: Role_Captain
- Consulted: Role_Architect, Role_HealthOwner
- Informed: Sponsor_L1_Human

### P10 - Capacity Gap Resolution

**Trigger:** Gaps críticos capacidad en F4/F10 explicando baja H_org/eta_org

**Duración:** 4W

**Propósito:** Diseñar y ejecutar plan cierre de gaps de capacidad (skills, FTE, plataformas)

**Pasos:**
1. Identificar gap capacidad (TF1)
2. Evaluar opciones (hire/buy/build/borrow)
3. Ejecutar adquisición
4. Onboard
5. Validar gap cerrado

**RACI:**
- Responsible: Role_CapacityOwner, TF1_Lead, HR
- Accountable: Role_Captain
- Consulted: Role_Architect, Finance
- Informed: Sponsor_L1_Human, Affected_Teams

### P11 - Flow Optimization

**Trigger:** Eficiencia flujos degradada. Cuellos de botella localizables en E7_FlowExecution

**Duración:** 3W

**Propósito:** Optimizar flujos cuando eta_org/ROI_Habilitacion degradados por cuellos de botella

**Pasos:**
1. Analizar flujos TF2
2. Identificar cuellos botella
3. Rediseñar
4. Implementar
5. Medir eta_org improvement

**RACI:**
- Responsible: Role_FlowOwner, TF2_Lead
- Accountable: Role_Captain
- Consulted: Role_Architect, Process_Owners
- Informed: Sponsor_L1_Human, All_Teams

## Operational Playbooks (P14-P15)

Ajustes tácticos durante operación continua.

### P14 - Client Expectation Management

**Trigger:** H4_Percepcion < 60 AND customer_feedback degraded OR stakeholder escalation

**Duración:** 3D-7D

**Propósito:** Mitigar brechas expectativas stakeholders y entregables que degradan H4_Percepcion

**Pasos:**
1. Confirmar gap con datos F13 + customer_feedback
2. Preparar runbook comunicación (interno/externo)
3. Alineamiento SAC/PO/Architecture
4. Priorizar acciones correctivas (P10/P11 técnico, P13 político)
5. Ejecutar plan + monitorear H4_Percepcion recovery

**RACI:**
- Responsible: Product_Owner, Delivery_Lead
- Accountable: Sponsor_L1_Human
- Consulted: Role_Architect, TF3_Lead, Communications
- Informed: Board_Governance

### P15 - Adaptive Cadence

**Trigger:** Volatilidad contexto aumenta. Velocidad disminuye. Crisis mode

**Duración:** 2W-8W

**Propósito:** Ajustar cadencias operativas ante shocks contextuales para mantener continuidad

**Modos Adaptación:**
- Crisis mode: Sprint 1→2 semanas, deploy diario→semanal
- Hypergrowth mode: Aumentar parallelismo pero con handoff control

**Pasos:**
1. Immediate cadence freeze: Reducir WIP 40% en 2 semanas
2. Triage: Identificar backlogs críticos continuidad
3. Capacity rebalancing: Invocar P10 si gaps capacidad
4. Communication plan: P14 si impacto clientes
5. Transition roadmap: 4-8 semanas a steady cadence

**RACI:**
- Responsible: Delivery_Lead, PMO
- Accountable: Sponsor_L1_Human
- Consulted: TF1_Lead, TF2_Lead, HR
- Informed: Board_Governance

## Matriz de Activación

| Health Gate | Playbooks |
|------------|-----------|
| G1 (H_org < 60) | P01, P02, P15 |
| G2 (60 ≤ H_org < 70) | P01 (focalizado), P09 |
| G3 (H_org ≥ 70, eta_org/ROI baja) | P10, P11, P03 |
| G4 (H_org ≥ 70, eta_org ≥ 0.70, ROI ≥ 1.2) | P05, P06, P07 |

## Validación

**Estado:** VALIDADO ✅

**Checklist:**
- Todos playbooks tienen trigger canónico
- RACI explícito en cada playbook
- Trazabilidad a Layer 0 (Axiomas, Primitivos)
- Integración con Health Gates G1-G4
- Estimaciones de duración realistas
- Criterios éxito medibles
