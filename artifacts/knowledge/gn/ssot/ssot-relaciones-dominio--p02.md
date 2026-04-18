---
_manifest:
  urn: urn:gn:kb:ssot-relaciones-dominio-p02
  provenance:
    created_by: FS
    created_at: '2026-03-10'
    source: goreNubleOntology.ttl (TBox), goreNubleDipirOntology.ttl, GORE_OS/CLAUDE.md
version: 2.0.0
status: published
tags:
- ssot
- relaciones
- dominio
- ipr
- convenio
- resolucion
- morfismos
- categorico
lang: es
extensions:
  gn:
    family: ssot
    bundle: urn:gn:kb:ssot-master
  kora:
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:gn:kb:ssot-relaciones-dominio
---

# SSOT — Relaciones de dominio - Parte 02

## Budget mediator chain

El presupuesto conecta estructura organizacional con inversión vía una cadena de 3 objetos:

```
Organization (División)
 ↑ ownedBy (N:1)
BudgetProgram ──classifiedBy──→ {Subtitle, Item, Allocation, ProgramType, ProgramCode, FundingSource}
 ↑ belongsToProgram (N:1)
BudgetCommitment (CDP)
 ├── linkedToIPR (N:1, opcional) ──→ IPR
 └── linkedToAgreement (N:1, opcional) ──→ GOREAgreement
```

### Path equation PE-7: Validación CDP

`amount(CDP) ≤ current_amount(BudgetProgram) - committed_amount(BudgetProgram)`

El CDP es válido solo si el monto no excede el saldo disponible del programa presupuestario. Advisory lock `pg_advisory_xact_lock` serializa emisiones concurrentes.

### Cadena de ejecución por programa

Cada BudgetProgram tiene 5 aspectos de magnitud que forman un orden parcial:

`initial ≤ current` (post-modificaciones)
`committed ≤ current` (CDPs no pueden exceder vigente)
`accrued ≤ committed` (no se devenga sin compromiso previo)
`paid ≤ accrued` (no se paga sin devengo previo)

### Carryover como morfismo temporal

`BudgetCarryover: BudgetProgram(año T) → BudgetProgram(año T+1)`

Arrastre = saldo no ejecutado que se incorpora al siguiente año fiscal vía SIC (Saldo Inicial de Caja).

[impl: `core.budget_program` (25.761), `core.budget_commitment` (4.617), `core.budget_carryover` (13.378). `POST /api/presupuesto/{id}/cdps`. CLAUDE.md §Rules 25, 28]

## DGI cartera — colímite computado

La señal de salud de cada IPR en la cartera DGI es un colímite de 5 observaciones cruzadas:

```
health_signal = _compute_health_signal(
 cuotas_vencidas: Agreement.installments WHERE due_date < NOW
 alertas_criticas: Alert WHERE subject_type='core.ipr' AND severity=CRITICO
 brecha_avance: IPR.physical_progress - IPR.planned_progress
 staleness: NOW - MAX(ProgressReport.created_at)
 compromisos_vencidos: OperationalCommitment WHERE status=PENDIENTE AND due_date < NOW
)
```

| Señal | Condición |
|-------|-----------|
| ROJO | Cualquier componente en estado crítico |
| AMARILLO | Al menos un componente requiere atención |
| VERDE | Todos los componentes normales |

Es la única relación en el dominio que agrega datos de 5 entidades distintas en un solo valor. Cockpit drill-down: `/cartera?health_signal=ROJO`.

[impl: `dgi_cartera.py`. `_compute_health_signal`. 3 endpoints: cartera, resumen, cuotas-vencidas. CLAUDE.md §DGI Layer]

## User → Role → Population fibración

El par (role, division) determina completamente el contexto operativo de un usuario:

```
User ──hasRole──→ SystemRole (ref.category, 13 roles)
 | |
 | determines → Population {operativa, dgi}
 | |
 └──belongsTo──→ Organization (División)
 |
 determines → sidebar, dashboard, filtrado
```

### Fibración por population

| Population | Roles | Sidebar | Dashboard |
|-----------|-------|---------|-----------|
| operativa | ADMIN_SISTEMA, ADMIN_REGIONAL, JEFE_DIVISION, ENCARGADO, GOBERNADOR, SECRETARIO_EJECUTIVO, CONSEJERO_REGIONAL, JEFE_DEPARTAMENTO, JEFE_UNIDAD | 10 ítems operativos + role-specific | dashboard + ejecutivo / mi-división / mis-compromisos |
| dgi | JEFE_DGI, ESP_CONTROL_GESTION, ESP_PROCESOS, ESP_TD | 7 ítems DGI | cockpit DGI |

### Path equation PE-8: Routing determinístico

`sidebar(user) = population(role(user))`
`dashboard(user) = population(role(user)) × role_level(role(user))`

El routing es un funtor `F: User → UIContext` completamente determinado por el role. No hay ambigüedad.

[impl: `lib/auth.tsx` → `useAuth`. `User.population` drives routing. `components/sidebar.tsx` → `operationalNav` vs `dgiNav`. CLAUDE.md §Rules 11, 23]
