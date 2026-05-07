---
_manifest:
  urn: urn:salud:kb:hodom-operacional-indice
  provenance:
    created_by: FS
    created_at: '2026-05-07'
    source: Agente salubrista-hah operando en HODOM Hospital San Carlos (clawdbot).
      Consolidacion temporal INBOX/consolidacion_temp/
  version: 1.0.0
version: 1.0.0
status: publicado
family: catalog
tags:
- salud
- hodom
- operacional
- hospital-san-carlos
- iaas
- direccion-tecnica
- indicadores
lang: es
relations:
  cites:
  - urn:salud:kb:hodom-reglamento-ds1-2022
  - urn:salud:kb:hodom-direccion-tecnica
  - urn:salud:kb:salubrista
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:hodom-operacional-indice
---

# HODOM Operacional — Hospital San Carlos

Conocimiento derivado de la operacion real de la Unidad de Hospitalizacion
Domiciliaria del Hospital de San Carlos (SSNuble). El agente salubrista-hah
opera como copiloto del Director Tecnico.

## Fuentes operativas

- 726 ingresos, 747 altas en 14 meses (dic 2024 - ene 2026)
- 16 camas dotadas (20 desde sep 2025)
- Indice ocupacional promedio 89.8%
- Estadia promedio subio de 7.4 a 10.8 dias (+46%)

## Archivos derivados

- `urn:salud:kb:hodom-operacional-indicadores` — Indicadores de produccion 14m
