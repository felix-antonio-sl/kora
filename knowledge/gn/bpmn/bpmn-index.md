---
_manifest:
  urn: urn:gn:kb:bpmn-index
  provenance:
    created_by: FS
    created_at: '2026-01-29'
    source: "GORE Ñuble"
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- bpmn
- arquitectura
- gn
lang: es
---

# Índice de Procesos BPMN — GORE Ñuble

## Contexto

Índice KORA/MD de los 10 dominios de proceso BPMN del GORE Ñuble (D01–D10).
Ruta raíz: `knowledge/gn/bpmn/`.

## Catálogo de Procesos

| ID | Título | URN KORA | Criticidad | Dueño | Procesos | Subprocesos |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| D01 | Actos Administrativos | `urn:gn:kb:bpmn-d01-actos-administrativos` | Alta | Unidad Jurídica | 2 | ~14 fases |
| D02 | Ciclo Presupuestario | `urn:gn:kb:bpmn-d02-ciclo-presupuestario` | Crítica | DAF / DIPIR | 5+transversal | ~15 |
| D03 | Gestión IPR | `urn:gn:kb:bpmn-d03-gestion-ipr` | Crítica | Jefatura DIPIR | 9 | ~25 |
| D04 | Compras y Contrataciones | `urn:gn:kb:bpmn-d04-compras-contrataciones` | Alta | Unidad Abastecimiento | 4 | ~12 |
| D05 | Inventarios y Activo Fijo | `urn:gn:kb:bpmn-d05-inventarios-activo-fijo` | Media | DAF | 2 | ~10 |
| D06 | Flota Vehicular | `urn:gn:kb:bpmn-d06-flota-vehicular` | Media | Jefe Servicios Generales | 1 | 6 |
| D07 | Gestión de Personas (RRHH) | `urn:gn:kb:bpmn-d07-rrhh` | Alta | Área Gestión de Personas | 7 | ~20 |
| D08 | Rendiciones de Cuentas | `urn:gn:kb:bpmn-d08-rendiciones` | Crítica | UCR/DAF | 3 | ~10 |
| D09 | CIES/SITIA (Seguridad Pública) | `urn:gn:kb:bpmn-d09-cies-sitia` | Alta | Supervisor CIES | 3 | ~8 |
| D10 | Geoespacial IDE/Geonodo | `urn:gn:kb:bpmn-d10-geoespacial-ide` | Media | Coordinador Regional IDE | 3 | ~10 |

## Sistemas Transversales

| Sistema | Dominios que lo usan |
| :--- | :--- |
| SYS-SIGFE | D02, D03, D04, D05, D07, D08 |
| SYS-BIP-SNI | D02, D03, D08 |
| SYS-SISREC | D03, D08 |
| SYS-DOCDIGITAL / SGD | D01, D04 |
| SYS-FIRMAGOB | D01, D08 |
| SYS-SIGPER / SIAPER | D07 |
| SYS-SIGAS | D05, D06 |
| SYS-GESDOC | D03 |
| ORG-CHILECOMPRA | D04 |
| SYS-HIKCENTRAL / SITIA | D09 |
| SYS-GEONODO / OGC | D10 |

## Mapa de Criticidad

| Criticidad | Dominios |
| :--- | :--- |
| Crítica | D02 Presupuesto, D03 IPR, D08 Rendiciones |
| Alta | D01 Actos Admin., D04 Compras, D07 RRHH, D09 CIES |
| Media | D05 Inventarios, D06 Flota, D10 Geoespacial |

## Matriz de Referencias Cruzadas

| Dominio | Referencias |
| :--- | :--- |
| D01 | D02, D03, D04, D08 |
| D02 | D01, D03, D04, D08 |
| D03 | D01, D02, D08 |
| D04 | D01, D02, D05 |
| D05 | D02, D04 |
| D06 | D04, D05 |
| D07 | D01, D02 |
| D08 | D02, D03 |
| D09 | D01 |
| D10 | D03, D09 |

## Dependencias Críticas

- Matriz de integración orgánica: `urn:gn:kb:matriz-integracion-organica`
- Modelo integrado BPMN+C4:
