---
_manifest:
  urn: urn:orko:kb:orko-fundamentos
  provenance:
    created_by: FS
    created_at: '2026-01-29'
    source: ORKO framework documentation
version: 2.0.0
status: published
tags:
- axiomas
- primitivos
- invariantes
- fundamentos
- teoria
- knowledge
lang: es
---

# ORKO - Fundamentos Teóricos (Layer 0)

- Base axiomática irreducible del sistema ORKO.
- Contiene axiomas, primitivos, invariantes y teoremas.


## Axiomas Irreducibles (A1-A5)

- Verdades fundamentales no derivables.
- Genoma ontológico.


### A1 - Transformación

- Todo sistema organizacional existe para transformar estados (S1 → S2).


| Atributo | Valor |
|----------|-------|
| Enunciado formal | ∀ org: ∃ T \| T: S_in → S_out |
| Irreducibilidad | Sin T, sistema es estático (inerte). No derivable. |
| Derivaciones | P2 Flujo (Estructura de T). Duración, Costo, Calidad. |

### A2 - Capacidad

- Existe capacidad que efectúa la transformación.
- No ocurre espontáneamente.


| Atributo | Valor |
|----------|-------|
| Enunciado formal | ∀ T: ∃ C \| C executes T |
| Irreducibilidad | T requiere agente causal. C es el potencial de actuar. |
| Derivaciones | P1 Capacidad (Agente transformador). Actor vs Sustrato. |

### A3 - Información

- Existe estructura portadora de significado que coordina transformaciones.


| Atributo | Valor |
|----------|-------|
| Enunciado formal | ∀ T: ∃ I_in, I_out \| T(I_in) = I_out |
| Irreducibilidad | Sin I, no hay coordinación ni memoria. Caos. |
| Derivaciones | P3 Información (Estructura, Lineage). Dato + Señal + Estado. |

### A4 - Restricción

- No todo es posible.
- Existen restricciones que acotan el espacio de posibilidades.


| Atributo | Valor |
|----------|-------|
| Enunciado formal | ∀ T: T ⊆ Espacio_Factible(L) |
| Irreducibilidad | Sin L, espacio infinito no operable. Física/Regulación exigen L. |
| Derivaciones | P4 Límite. Tipos: Físico, Regulatorio, Org, Económico, Técnico. |

### A5 - Intencionalidad

- Transformación tiene propósito direccional (outcome deseado).


| Atributo | Valor |
|----------|-------|
| Enunciado formal | ∀ T: ∃ P \| P directs T |
| Irreducibilidad | Sin P, movimiento es browniano (ruido). Teleología distingue Org de Caos. |
| Derivaciones | P5 Propósito (Outcome, OKR). Valor derivado de P. |

- **Validación:** A1-A5 cubren Acción, Agente, Medio, Límite, Fin.
- Ortogonales pares a pares.


## Primitivos (P1-P5) - Constructos Operacionales

- Mínima estructura necesaria para operacionalizar A1-A5.


### P1 - Capacidad

- Potencial de ejecutar transformación.
- Unifica Actor y Agente.


- **Dimensiones Ortogonales:**


| Dimensión | Nivel | Descripción |
|-----------|-------|-------------|
| Sustrato | Humano | Juicio, ética, creatividad (C0-C3) |
| | Algorítmico | Escala, velocidad (C0-C2) |
| | Mecánico | Fuerza, precisión (C0) |
| | Mixto | HITL (Human-in-the-loop) |
| Cognición | C0_Ejecutar | Determinístico. Sin decisión. (RPA, Sensor) |
| | C1_Decidir | Selección opciones. (ML, Rule Engine) |
| | C2_Reflexionar | Metacognición proceso. (Manager, Planner) |
| | C3_Meta-Reflexionar | Reflexión sobre reflexión. (Estratega, Humano) |
| Rol Valor | Producción | Directo a cliente. Genera Revenue. |
| | Habilitación | Amplifica prod interna. Indirecto. |

- **Resolución Actor-Agente:** Actor y Agente NO son primitivos.
- Son Vistas de P1.
- Actor = Vista filtrada por Sustrato.
- Agente = Vista filtrada por Cognición (Capacity ≥ C1).


### P2 - Flujo

- Secuencia estructurada de transformaciones (DAG).


| Componente | Descripción |
|-----------|-------------|
| Steps | Nodos atómicos (ordenados) |
| Dependencies | Edges (flujo info) |
| Handoffs | Cambio de Capacidad (Costos fricción) |
| Métricas | Cycle Time, Throughput, Handoff Ratio |

### P3 - Información

- Contenido estructurado + Propiedades Temporales + Lineage.


| Tipo | Validez | Notas |
|-----|---------|-------|
| Persistente | Datos estables (Docs, Records). Validity ∞ |  |
| Transitoria | Eventos/Señales. Validity corta (TTL) |  |
| Agregada | Estado derivado (Dashboards). Validity composita |  |

- **Propiedades:** Lineage (Trazabilidad origen:
- Producer Flow/Cap).
- Freshness (Age vs Validity).


### P4 - Límite

- Constraint que acota espacio posibilidades.


| Tipo | Características |
|-----|-----------------|
| Físico | Inmutable (Leyes naturales) |
| Regulatorio | Hard constraint externo (Ley, Compliance) |
| Organizacional | Soft constraint interno (Policy, RACI) |
| Económico | Resource constraint (Budget) |
| Técnico | Capacity constraint (Rate limit) |

- **Enforcement:** Preventivo (Bloqueo ante-facto, Critical).
- Detectivo (Alerta post-facto, Error/Warning).
- Correctivo (Compensación auto).


### P5 - Propósito

- Outcome deseado con métricas y jerarquía.


| Componente | Descripción |
|-----------|-------------|
| Objective | Cualitativo, inspiracional |
| Key_Results | Cuantitativos (Metric, Target, Current) |
| Hierarchy | Org → Unit → Team → Individual |
| Owner | Humano Accountable (Mandatory) |

## Invariantes (I1-I8) - Restricciones del Sistema

- Propiedades que DEBEN preservarse en todo estado válido.


### I1 - Minimalidad

- Sistema usa conjunto mínimo necesario (P1-P5).
- Nada sobra.


### I2 - Ortogonalidad

- P1-P5 mutuamente independientes.
- Cambiar uno no rompe otro.


### I3 - Trazabilidad

- Todo artefacto tiene Lineage, Owner, Timestamp.


### I4 - Clasificación

- Todo elemento es Producción o Habilitación (contextual).


### I5 - HAIC (Primacía Humana)

- Human-AI Collaboration.
- AI tiene autonomía acotada, accountability humana intransferible.


- **Niveles de Delegación AI:**


| Modo | Descripción |
|------|-------------|
| M1_Monitorear | AI observa. Humano decide. |
| M2_Informar | AI sugiere. Humano decide. |
| M3_Habilitar | Humano invoca. AI ejecuta supervisada. |
| M4_Controlar | AI decide (reglas). Humano handles exceptions. |
| M5_Coproducir | Humano + AI colaboran par-a-par. |
| M6_Ejecutar | AI autónoma (bounded). Humano supervisa/override. |

- **Constraints:** Accountability moral siempre es Humana.
- Override mechanism siempre disponible (M4-M6).
- Explainability obligatoria (M3+).


### I6 - Trayectoria

- Capacidad Algorítmica evoluciona con historial (Logs → Mejora).


### I7 - Emergencia

- Prácticas emergen en niveles complejidad (L0-L5).
- No over-engineering.


### I8 - Adaptación

- Separación Genoma (Rígido) vs Fenotipo (Flexible).


## Ciclos Fundamentales

### SDA - Sense, Decide, Act

- Ciclo canónico de transformación operativa.


| Fase | Descripción | Inputs |
|------|-------------|--------|
| Sense | Capturar estado (D2) | Sensores, Observables |
| Decide | Seleccionar acción (D3) | Info, Propósito, Límites |
| Act | Ejecutar transformación (D4) | Capacidad, Acción |

- **Latencias Comparativas:**

- Humano: Sense(s) → Decide(min/h) → Act(min)
- Algoritmo: Sense(ms) → Decide(ms) → Act(ms) [1000x faster]

- **Propiedad:** Recursivo (Fractal).


### WSLC - Work System Life Cycle

- Ciclo de vida evolutivo del sistema mismo.


| Fase | Descripción |
|------|-------------|
| W1_Initiation | Concepción, Business Case |
| W2_Development | Construcción, Diseño |
| W3_Implementation | Despliegue, Cutover |
| W4_Operation | Ejecución continua (contiene SDAs) |
| W5_Retirement | Decommission, Learning |

- **Relación SDA:** WSLC evoluciona el sistema que ejecuta SDAs.


## Dominios (D1-D4) - Concerns Ortogonales

- Separación de responsabilidades ortogonales para manejo complejidad.


### D1 - Arquitectura

- **Pregunta:** ¿Quién hace qué?
- (Estructura)


- **Responsabilidades:** Diseño Estructural, Autoridad (RACI), Límites.


- **Métrica:** A_Score (Claridad, Span, Alignment).


### D2 - Percepción

- **Pregunta:** ¿Qué pasa?
- (Observabilidad)


- **Responsabilidades:** Instrumentación 16 Observables (EX1-8 Externos, IN1-8 Internos).


- **Métrica:** P_Score (Coverage, Freshness, Accuracy).


### D3 - Decisión

- **Pregunta:** ¿Qué hacer?
- (Estrategia)


- **Responsabilidades:** Propósitos (OKRs), Priorización (RICE), Portfolio Mgmt.


- **Métrica:** D_Score (Alignment, Quality, Velocity).


### D4 - Operación

- **Pregunta:** ¿Cómo ejecutar?
- (Delivery)


- **Responsabilidades:** Ejecución Flujos, Optimización, Incident Mgmt.


- **Métrica:** O_Score (Throughput, Reliability, Efficiency).


## Ecuación Maestra & Métricas

### V_org - Valor Organizacional

```
V_org(t) = Σ Outcomes(t) - Σ Costos(t)

Outcome = Volume × f_evaluate(Quality, Purpose)
Costo = Producción + Habilitación (Total Cost of Capacity)
```

### Integración AOC (Arquitectura Organizacional Cuántica)

```
AOC = w1·Coherencia + w2·Resonancia + w3·Flujo
Impacto: Mejor arquitectura = Mayor Quality multiplier
```

### H_org - Health Score Organizacional

```
H_org = 0.25·A + 0.20·P + 0.25·D + 0.30·O

Threshold: H_min = 70
Si H < 70, sistema entra en deuda/degradación
```

## Teoremas

| Teorema | Enunciado |
|---------|-----------|
| T1_Completitud | P1-P5 suficientes para expresar todo concepto org |
| T2_Ortogonalidad | P1-P5 dimensión independiente comprobada |
| T3_Minimalidad | Remover cualquier Pi rompe el sistema (Axioma violado) |
| T5_Emergencia | Prácticas solo válidas si Nivel_Complexity ≥ Nivel_Práctica |

## Modelo Relacional

| Entidad | Descripción |
|---------|-------------|
| E1(Cap) | Capacidad |
| E2(Flu) | Flujo |
| E3(Inf) | Información |
| E4(Lim) | Límite |
| E5(Prop) | Propósito |

- **Relaciones Clave:**

- R1: Capacidad ejecuta Flujo (N:M)
- R2: Flujo produce Información (1:N)
- R6: Límite restringe Capacidad/Flujo (N:M)
- R9: Propósito direcciona Flujo (1:N)
- R13: Capacidad(Human) delega Capacidad(Algo) [HAIC Base]

- **Constraints:**

- Acyclicity en DAGs (Lineage, Flujos)
- Mandatory Owner para Propósito
- Mandatory Human Accountable para AI
