---
_manifest:
  urn: urn:salud:kb:management-engineering-ext-indice
  provenance:
    created_by: FS
    created_at: '2026-05-07'
    source: Healthcare Management Engineering (Kolker, Springer 2012). INBOX/salud/
  version: 1.0.0
version: 1.0.0
status: publicado
family: note
tags:
- salud
- management-engineering
- operaciones
- capacidad
- colas
- simulacion
lang: es
relations:
  cites:
  - urn:salud:kb:salubrista
  - urn:salud:kb:salubrista-fuente-management-engineering
  - urn:salud:kb:gestion-redes-general
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:management-engineering-ext-indice
---

# Healthcare Management Engineering — Indice

Fuente: Healthcare Management Engineering: What Does This Fancy Term Really Mean?
(Kolker, Springer 2012). 8 capitulos, ~50,000 palabras.

Complementa la fuente management-engineering-sanitario existente con metodos
cuantitativos adicionales.

## Capitulos de la fuente

1. Traditional Management and Management Engineering
2. Dynamic Supply and Demand Balance Problems
3. Linear and Probabilistic Resource Optimization and Allocation Problems
4. Forecasting Time Series
5. Business Intelligence and Data Mining
6. The Use of Game Theory
7. Summary of Fundamental Management Engineering Principles
8. Concluding Remarks

## Metodos clave

| Metodo | Aplicacion en salud |
|--------|-------------------|
| Discrete Event Simulation | Flujo de pacientes, capacidad de urgencias, ocupacion UCI |
| Queuing Theory | Tiempos de espera, optimizacion de throughput |
| Linear Optimization | Asignacion de recursos, rentabilidad de servicio |
| Time Series Forecasting | Prediccion de volumenes y estacionalidad |
| Game Theory (Shapley) | Distribucion justa de ahorros entre proveedores |
| Principal Component Analysis | Analisis de margen de contribucion |

## Archivos derivados

- `urn:salud:kb:management-engineering-ext-capacidad` — Capacidad, colas y flujo
