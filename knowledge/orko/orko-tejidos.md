---
_manifest:
  urn: urn:orko:kb:orko-tejidos
  provenance:
    created_by: FS
    created_at: '2026-01-29'
    source: ORKO framework documentation
version: 2.0.0
status: published
tags:
- tejidos
- tf1
- tf2
- tf3
- tecnologia
- operacionalizacion
- knowledge
lang: es
---

# ORKO - Tejidos Tecnológicos (Layer 2)

- Operacionalización que transforma contratos arquitectónicos abstractos en implementaciones tecnológicas concretas.
- Genoma (Abstracciones Universales) / Fenotipo (Implementaciones Concretas).


## Principio de Derivación

- Cada primitivo fundamental (P1, P2, P3) genera UN tejido tecnológico.
- Transversales (P4, P5) son concerns cross-cutting.


## TF1 - Tejido de Capacidad

- **Primitivo:** P1_Capacidad | **Axioma:** A2_Existencia_Capacidad


- **Scope:** Diseño, desarrollo, despliegue, gestión capacidades organizacionales


- **Sustratos:** Humano, Algorítmico, Mecánico, Mixto


- **Dominios Técnicos:** BAD (Business Architecture Design), OCE (Org Change Eng), Infrastructure


### Schema CapacityAsset

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | UUID | Identificador único |
| capacity_type | {C0, C1, C2, C3} | Nivel cognitivo |
| substrate | {Humano, Algorítmico, Mecánico, Mixto} |  |
| role | {Producción, Habilitación} |  |
| accountable_id | UUID (Humano\|Mixto) | Obligatorio (I5_HAIC) |
| delegated_from | UUID | Si substrate=Algorítmico |
| delegation_mode | {M1..M6} | Modelo delegación |
| override_enabled | Boolean | Circuit breaker |
| lifecycle | State | {Planning, Development, Active, Idle, Deprecated, Retired} |
| utilization_avg | Float[0..1] | Promedio utilización |

- **Métricas de Trayectoria (Algorítmico):**

- total_executions
- drift_detected
- last_retrain_date
- performance_trend

### Patrones de Desarrollo

| Sustrato | Ciclo | Herramientas |
|----------|-------|-------------|
| Humano | Define_Role → Hire/Upskill → Onboard → Monitor → Optimize | HR platforms, LMS, Perf mgmt |
| Algorítmico ML | Define_Problem → Data_Prep → Train → Evaluate → Serve → Monitor/Retrain | MLflow, Kubeflow, SageMaker |
| Algorítmico Agent | Define_Role → Prompt_Eng → Tool_Integration → Guardrails → HITL → Deploy | LangChain, vLLM, LangGraph |
| Mecánico | Hardware_Selection → Procurement → Configuration → Maintenance | CMMS, IoT platforms |

### Score TF1

```
TF1_Score = weighted_avg(Coverage×25%, Quality×30%, Availability×25%, Governance×10%, Efficiency×10%)
Threshold: >= 70
```

- **Invariantes:**

- INV_TF1.1: accountable_id.substrate ∈ {Humano, Mixto}
- INV_TF1.2: substrate=Algorítmico → delegated_from NOT NULL
- INV_TF1.3: delegation_mode=M6 → guardrails comprehensive

## TF2 - Tejido de Flujo

- **Primitivo:** P2_Flujo + P1_Capacidad(ejecutores) | **Axioma:** A1_Transformación


- **Scope:** Orquestación, automatización, ejecución flujos organizacionales


- **Espectro Cognitivo:** C0_Mechanical, C1_Decisional, C2_Cognitive


- **Dominios Técnicos:** BPA (Business Process Automation), OCE, CI/CD


### Schema FlowAsset

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | UUID |  |
| flow_type | {Process, Pipeline, Orchestration, Workflow} |  |
| cognitive_level | {C0, C1, C2, Mixed} |  |
| role | {Producción, Habilitación} |  |
| steps | DAG<Step> | Estructura acíclica |
| dependencies | Edges | Flujo información |
| coordinator_capacity_id | UUID | Si cognitive_level >= C1 |
| agents | List<AgentRole> | Para C2 multi-agent |
| delegation_mode | {M1..M6} | Autonomía |
| hitl_checkpoints | List | Human-in-the-loop |
| override_mechanism | Boolean | Circuit breaker |
| guardrails | {operational, quality, scope} |  |

- **Propiedades de Step:**

- capacity_id
- input_schema / output_schema
- timeout_seconds
- retry_policy

### Patrones de Orquestación

| Nivel Cognitivo | Patrones | Herramientas |
|-----------------|----------|-------------|
| C0_Mechanical | RPA_UI_Automation, Scheduled_Job | UiPath, Airflow, dbt |
| C1_Decisional | ML_Based_Routing, Business_Rules_Engine | Scikit-learn, Drools |
| C2_Cognitive | Single_Agent_Task, Multi_Agent_Orchestration | LangGraph, CrewAI, AutoGen |

### Score TF2

```
TF2_Score = weighted_avg(Coverage×20%, Reliability×30%, Efficiency×25%, Safety×15%, STP_Rate×10%)
Threshold: >= 70
```

- **Invariantes:**

- INV_TF2.1: ∀ step: step.output_schema compatible next_step.input_schema
- INV_TF2.2: cognitive_level=C2 ∧ orchestration.pattern=Multi_Agent → agents.length ≥ 2
- INV_TF2.3: handoff_ratio > 0.30 → Warning (Meyer Rule)

## TF3 - Tejido de Información

- **Primitivo:** P3_Información | **Axioma:** A3_Existencia_Información


- **Scope:** Ciclo vida completa información (Ingestion→Storage→Processing→Analytics→Semantics)


- **Sub-Dominios:** Foundation, Analytics, Semantic


- **Arquitectura:** Lakehouse Unificado (Bronze → Silver → Gold → Semantic)


- **Dominios Técnicos:** Data, Analytics, Knowledge Management


### Schema InformationAsset

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | UUID |  |
| information_type | {Persistente, Transitoria, Agregada} |  |
| structure | {Structured, Semi_Structured, Unstructured} |  |
| sub_domain | {Foundation, Analytics, Semantic} |  |
| format | String | YAML, JSON, Parquet, etc |
| schema_definition | Schema | Format specification |
| timestamp | ISO8601 |  |
| validity_period_seconds | Int | TTL |
| freshness_sla_seconds | Int | SLA freshness |
| origin | {Internal, External} |  |
| produced_by_flow | UUID |  |
| produced_by_capacity | UUID |  |
| source_ref | String | Si external |
| parent_assets | List<UUID> | Lineage |
| access_control | RBAC | Security |
| contains_pii | Boolean |  |
| masking_rules | List | Si PII |
| compliance | List | Regulatory |
| encryption | Boolean |  |

### Arquitectura Lakehouse

| Layer | Características |
|-------|-----------------|
| Bronze | Raw ingestion, original format, no validation |
| Silver | Cleaned, validated, normalized, deduplicated |
| Gold | Business-ready, aggregated, high quality |
| Semantic | Unstructured indexed (Vector+Keyword), Knowledge Graph, RAG-ready |

### Score TF3

```
TF3_Score = weighted_avg(Coverage×20%, Quality×30%, Freshness×20%, Governance×15%, Adoption×15%)
Threshold: >= 70
```

- **Invariantes:**

- INV_TF3.1: origin=Internal ⇒ (produced_by_flow OR produced_by_capacity NOT NULL)
- INV_TF3.2: contains_pii=true → masking_rules NOT NULL
- INV_TF3.3: sub_domain=Semantic ∧ rag_config NOT NULL → indexing.vector_indexed=true

## Concerns Transversales

### Security (P4 - Límite)

- **Aplicación a Tejidos:**


| Tejido | Implementación |
|-------|-----------------|
| TF1 | IAM (Least privilege), Guardrails (Input/Output validation), Audit trails |
| TF2 | Execution permissions, Bounded Autonomy (M1-M6), Circuit Breakers |
| TF3 | Row/Column Security, PII Masking/Encryption, Compliance retention |

```
Security_Score = weighted_avg(IAM×25%, Encryption×20%, Compliance×25%, Incidents×20%, Audit×10%)
Gating_Rule: Security_Score < 70 → Bloquear cambios críticos
```

### Purpose (P5 - Propósito)

- **Definición:** Mecanismo de Governance que vincula tejidos con Objetivos de Negocio (OKRs)


| Tejido | Aplicación |
|-------|-----------|
| TF1 | Capacity.purpose → Linked OKRs (Contribution: Velocity/Quality) |
| TF2 | Flow.purpose → Linked OKRs (Contribution: Efficiency/Safety) |
| TF3 | Information.purpose → Linked OKRs (Contribution: Decision/Insight) |

```
Purpose_Alignment = (Σ OKR.progress × asset_contribution) / Total_OKRs
```

### Interface Layer UX/UI

- **Design System Unificado:**


| Nivel | Elementos |
|-------|-----------|
| Foundation | Tokens, Grid, Typography, Colors |
| Components | Atomic Design (Atoms, Molecules, Organisms) |

- **Aplicación Tejidos:**

- TF1_UIs: Capacity Registry, Agent Designer, Performance Dashboard
- TF2_UIs: Flow Designer (DAG), Execution Monitor, HITL Queue
- TF3_UIs: Data Catalog, Dashboard Builder, RAG Search UI

- **Standards:** WCAG 2.1 AA, Core Web Vitals


### Observability

- **Pillars:** Logs, Metrics, Traces, Alerts


| Tejido | Logs | Metrics | Traces |
|-------|------|---------|--------|
| TF1 | Lifecycle logs | Utilization metrics | Drift traces |
| TF2 | Execution steps | STP rates | End-to-end traces |
| TF3 | Data quality scores | Lineage DAGs | Access logs |

## Entidades Compuestas

### E7 - Flow Execution

- **Ubicación:** Integrado en TF2.execution_history


- **Concepto:** Instancia concreta de ejecución de Flow (Runtime tracking)


- **Key Fields:**

- id, flow_id, trigger
- status, current_step_id
- outputs_produced
- metrics(DORA)

### E6 - Architectural State

- **Ubicación:** Concern Transversal (Meta-arquitectónico)


- **Concepto:** Snapshot completo del sistema en momento dado


- **Tipos:** Current, Target, Intermediate, Historical


- **Operaciones:**

- capture_current_state()
- define_target_state()
- plan_intermediate_states()
- calculate_convergence()
- transition_to_state()

- **Métricas:**

- consistency_validated: Boolean
- convergence_pct: Float
- health_score: Aggregated(TF1, TF2, TF3, Security)

## Integración de Tejidos

### Principios

- Loose Coupling (Contratos)
- High Cohesion
- Explicit Dependencies
- Event Driven
- Idempotency

### Patrones de Integración

| Patrón | Descripción |
|--------|-------------|
| TF1_executes_TF2 | Flow steps asignados a Capacities |
| TF2_triggered_by_TF3 | Cambios en Info Assets disparan flujos |
| TF2_produces_TF3 | Ejecución genera/transforma assets |
| TF3_feeds_TF1 | Training data para ML, Context para RAG |

### Casos Uso End-to-End

- **RAG Pipeline:**

- Components: TF1(LLM) + TF2(Orchestration) + TF3(Semantic)
- Trace: Query → TF2 → TF1(Embed) → TF3(Retrieve) → TF1(Generate) → TF3(Log)

- **CI/CD Pipeline:**

- Components: TF1(Build/Test) + TF2(Pipeline) + TF3(Repo/Logs)
- Trace: Commit → TF2 → TF1s → HITL → Deploy → Monitor

- **Multi-Agent Research:**

- Components: TF1(Agents) + TF2(Hierarchical Loop) + TF3(Sources)
- Trace: Task → TF1(Manager) → TF2(Loop) → TF1(Workers) → TF3(Report)

## Validación

### Invariantes I1-I8

| Invariante | Status |
|-----------|--------|
| I1_Minimalidad | 3 tejidos irreducibles, cobertura completa P1-P5 |
| I2_Ortogonalidad | 0% overlap entre tejidos |
| I3_Trazabilidad | 100% rastreable vertical (Axiomas) y horizontal |
| I4_Clasificacion | Roles Producción/Habilitación explícitos |
| I5_HAIC | Accountability y Bounded Autonomy transversales |
| I6_Trajectory | Drift detection y Learning loops activos |
| I7_Emergencia | Niveles cognitivos C0-C3 soportados |
| I8_Adaptacion | Trayectorias Minimal y Avanzada soportadas |

- **Estado:** VALIDADO ✅

