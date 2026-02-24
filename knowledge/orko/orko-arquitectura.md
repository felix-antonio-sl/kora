---
_manifest:
  urn: urn:orko:kb:orko-arquitectura
  provenance:
    created_by: FS
    created_at: '2026-01-29'
    source: ORKO framework documentation
version: 2.0.0
status: published
tags:
- arquitectura
- contratos
- dise-o
- principios
- entidades
- knowledge
lang: es
---

# ORKO - Arquitectura Organizacional (Layer 1)

- Operacionalización de los fundamentos teóricos en estructuras, contratos y modelos ejecutables.
- Contratos canónicos y principios de diseño que operacionalizan el Genoma.


## Contratos Canónicos (Primitivos Operables)

- Especificación OPERABLE de Primitivos P1–P5.
- Schemas abstractos (Genoma) implementables en tecnología (Fenotipo).


### C1 - Capacidad

- **ID:** ORKO-CON-C1 | **Primitivo Base:** P1


- **Schema:**


| Campo | Tipo | Restricción |
|-------|------|-------------|
| id | UUID | Immutable |
| substrate | {Humano, Algorítmico, Mecánico, Mixto} |  |
| capacity_type | {C0_Ejecutar, C1_Decidir, C2_Reflexionar, C3_Meta_Reflexionar} |  |
| role | {Producción, Habilitación} |  |
| role_context | String |  |
| accountable_id | UUID (Humano/Mixto) | INV_C1 |
| delegated_from | UUID \| null | INV_C2 si Algorítmico |
| delegation_mode | {M1..M6} |  |
| lifecycle | {Planning, Development, Active, Idle, Deprecated, Retired} |  |

- **Invariantes:**

- INV_C1: accountable_id.substrate ∈ {Humano, Mixto} (HAIC)
- INV_C2: Algorítmico → delegated_from NOT NULL
- INV_C3: Mixto → composition has ≥1 Humano

- **Resolución:** Actor y Agente son VISTAS de Capacidad, no entidades separadas.


### C2 - Flujo

- **ID:** ORKO-CON-C2 | **Primitivo Base:** P2


- **Schema:**


| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | UUID |  |
| type | {Producción, Habilitación} |  |
| steps | List<{step_id, capacity_required, input, output, automation_level}> | DAG |
| dependencies | DAG structure | Acyclic |
| metrics | {cycle_time, throughput, handoff_ratio, flow_efficiency} |  |
| owner_capacity_id | UUID |  |
| purpose_id | UUID | Required |

- **Invariantes:**

- INV_F1: Acyclic DAG
- INV_F4: All flows serve a Purpose (A5)

### C3 - Información

- **ID:** ORKO-CON-C3 | **Primitivo Base:** P3


- **Schema:**


| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | UUID |  |
| information_type | {Persistente, Transitoria, Agregada} |  |
| lineage | {produced_by_flow/capacity, parent_ids, origin} | DAG |
| temporal | {valid_from, valid_until, retention} |  |
| quality | {completeness, accuracy, timeliness} |  |
| observable_id | {EX1..EX8, IN1..IN8} \| null |  |

- **Invariantes:**

- INV_I3: Lineage forms DAG
- Lineage_Policy: Internal origin MUST have producer; External MUST have source_ref

### C4 - Límite

- **ID:** ORKO-CON-C4 | **Primitivo Base:** P4


- **Schema:**


| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | UUID |  |
| limit_type | {Físico, Regulatorio, Organizacional, Económico, Técnico} |  |
| constraint | {target, expression, enforcement={Preventive\|Detective}} |  |
| compliance | {violations_summary, severity_score} |  |

- **Invariantes:**

- INV_L3: Regulatorio requires Authority Source

### C5 - Propósito

- **ID:** ORKO-CON-C5 | **Primitivo Base:** P5


- **Schema:**


| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | UUID |  |
| objective | String | Qualitativo |
| key_results | List<{current, target, achievement_type}> |  |
| hierarchy | {parent_purpose_id, children_ids, alignment_score} | Tree |
| ownership | {owner_capacity_id (Humano/Mixto)} |  |

- **Invariantes:**

- INV_P5: Hierarchy forms Tree (Child end_date ≤ Parent end_date)
- INV_P3: Owner MUST be Human/Mixto

### Entidades Compuestas

- **E7 - Ejecución de Flujo**

- Descripción: Instancia concreta de un Flujo
- Schema: {flow_id, executed_by, start/end_time, status, outputs, failure_reason}
- Rol: Base para DORA metrics y audit trails

- **E6 - Estado Arquitectónico**

- Descripción: Snapshot consistente del sistema (Capacidades + Flujos + Propósitos)
- Schema: {state_type={Current\|Target}, snapshot_data, validity}

## Principios de Diseño (PD1-PD76)

- Reglas operativas derivadas de invariantes teóricos (I1-I8).
- Total:
- 76 principios.


### Minimalidad (I1)

- PD1_Justificación: Nueva entidad requiere business case irreducibilidad
- PD2_Composición: Preferir componer existentes (C1⊕C2) sobre crear nuevas
- PD3_Eliminación_Redundancia: Sunset entidades subutilizadas

### Ortogonalidad (I2)

- PD6_Separación_Concerns: Responsabilidad única por entidad
- PD7_Relaciones_Explícitas: No embedding oculto

### Trazabilidad (I3)

- PD10_Metadata: created_by, version mandatory
- PD11_Lineage: Cadena proveniencia completa
- PD13_Decision_Records: ADRs obligatorios para decisiones Type-1

### HAIC (I5)

- PD18_Accountability_Transversal: Humano accountable siempre
- PD19_Delegación_Explícita: Algoritmos operan bajo modos M1-M6
- PD20_Override_Universal: Humano siempre puede intervenir (circuit breakers)
- PD21_Explainability: AI debe explicar decisiones a humano

### Trayectoria (I6)

- PD23_Progresión_Gradual: Autonomía (M1→M6) ganada con historial éxito
- PD24_Drift_Detection: Downgrade autonomía si performance degrada

### Métricas AOC-Kelly (PD41-46)

- PD41_Coherencia: Value/Energy > threshold
- PD44_Small_Batches: 80% work in small units
- PD45_Flow_Gate: Lead time constraint contextual
- PD46_Quality_Speed: Velocidad no puede sacrificar calidad (Index)

### Contexto (I8, PD36-40)

- PD36_Context_Schema: 36 parámetros obligatorios para adaptar framework
- PD37_Genotype_Phenotype: Separación estricta (Teoría inmutable vs Práctica adaptable)

## Modelo Relacional

- **Entidades Core:** E1_Cap, E2_Flu, E3_Inf, E4_Lim, E5_Prop


### Relaciones Fundamentales

| ID | Relación | Tipo |
|----|----------|------|
| R1 | Capacidad ejecuta Flujo | 1..* ↔ 0..* |
| R2 | Flujo produce Información | 1 → 1..* |
| R3 | Capacidad produce Información | 1 → 0..* |
| R4 | Capacidad consume Información | 0..* ← 0..* |
| R5 | Información deriva Información | 0..* ↔ 0..* DAG |
| R6 | Límite restringe {Cap, Flu, Inf} | N:M |
| R9 | Propósito direcciona Flujo | 1 ← 1..* |
| R10 | Propósito asigna Capacidad | 0..* ← 1 |
| R11 | Propósito jerarquía | Tree |
| R12 | Capacidad composición | Recursive, Acyclic |

- **R13 - Delegación HAIC:**

- Def: Capacidad(Alg) [1] ↔delegada_por↔ [1] Capacidad(Hum/Mix)
- Constraint: Mandatory for all Algo capacities

- **R14-R15:**

- R14_State_Transitions: Estado → Transición → Estado (Evolution)
- R15_Transition_Flow: Transición ejecutada por Flujos (Design-Run Link)

## Vistas Arquitectónicas (Dominios)

- Proyecciones del modelo para concerns específicos.


### D1 - Arquitectura

- **Concern:** Estructura & Límites


- **Artefactos:**

- D1.1 Org Chart (Capacidades + R12)
- D1.2 RACI Matrix (Rights management)
- D1.3 Purpose Cascade (Alignment tree)

- **Métrica:** A_Score (Claridad Autoridad, Span of Control, Alignment)


### D2 - Percepción

- **Concern:** Observabilidad & Estado


- **Artefactos:**

- D2.1 Dashboard 16 Observables (8 EXT + 8 INT)
  - EXT: Demanda, Competidores, Regulación, Tech, Feedback, Disrupt, Social, Econ
  - INT: Velocidad, Salud Cap, Eficiencia, Calidad, Utilización, Alineación, Violaciones, Debt
- D2.2 Anomaly/Compliance Logs

- **Métrica:** P_Score (Coverage, Freshness, Latencia Detección)


### D3 - Decisión

- **Concern:** Estrategia & Priorización


- **Artefactos:**

- D3.1 OKR Canvas (Planning)
- D3.2 Portfolio Board (RICE scoring, WIP limits)
- D3.3 Decision Audit Trail (Accountability log)

- **Métrica:** D_Score (Velocity, Portfolio Balance, Execution Rate)


### D4 - Operación

- **Concern:** Ejecución & Entrega Valor


- **Artefactos:**

- D4.1 Value Stream Map (Flow analysis)
- D4.2 DORA Dashboard (Deploy freq, Lead time, CFR, MTTR)
- D4.3 Incident Log

- **Métrica:** O_Score (Flow efficiency, Cycle time, Availability)


## H_org - Health Score Organizacional

- **Definición:** Métrica integrada de salud organizacional


```
H_org = 0.30·H1(Humano) + 0.25·H2(Arq) + 0.20·H3(Flujo) + 0.15·H4(Perc) + 0.10·H5(Dec)

Constraint: H_org < 70 → Bloquear transformaciones (Recovery Mode)
```

- **Dimensiones H:**

- H1_Humano: Bienestar, Engagement, Desarrollo, Autonomía
- H2_Arquitectura: A_Score revisado
- H3_Flujo: O_Score revisado (Focus on waste reduction)

## Patrones y Anti-Patrones

### Patrones Clave

| Patrón | Descripción |
|--------|-------------|
| D1.1_Team_Topology_Aligned | Estructura refleja flujos (Conway). Stream-aligned teams |
| D1.2_Delegation_Ladder | Delegación progresiva M1→M6 basada en confianza |
| D1.3_Purpose_Cascade | Link explícito L4(Org)→L1(Indiv) |
| D2.1_Observable_Instrumentation | Priorizar 16 observables por tiers |
| D3.1_RICE_Prioritization | Scoring objetivo (Reach×Impact×Conf/Effort) |
| D3.2_WIP_Limit | Stop starting, start finishing |
| D4.1_Continuous_Deployment | Pipeline automatizado con automated rollback |
| D4.2_Observability_Triad | Logs + Metrics + Traces integrados |

### Anti-Patrones Clave

| Anti-Patrón | Descripción |
|-----------|-------------|
| AP1_Conway_Ignored | Estructura funcional vs Flujos cruzados. Handoff hell |
| AP2_Automation_Blindness | M6 prematuro, sin supervisión. Riesgo crítico |
| AP3_Orphan_OKRs | Objetivos sin padre. Esfuerzo desperdiciado |
| AP13_Rainbow_Groups | Mezcla arquetipos incompatibles (Innovación + Ops) |
| AP14_Activity_Based_Teams | Equipos por función (Frontend dept) vs valor |
