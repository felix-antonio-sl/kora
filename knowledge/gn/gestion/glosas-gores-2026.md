---
_manifest:
  urn: urn:gn:kb:glosas-gores-2026
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
    source: domains/gn/03_operacion/presupuesto/kb_gn_211_ley_presupuestos_2026_glosas_gores_2026_koda.yml
version: 2.0.0
status: published
tags:
- gore
- presupuesto-2026
- glosas
- inversion-regional
- gestion-publica
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/presupuesto/kb_gn_211_ley_presupuestos_2026_glosas_gores_2026_koda.yml
    source_hashes:
      domains/gn/03_operacion/presupuesto/kb_gn_211_ley_presupuestos_2026_glosas_gores_2026_koda.yml: ed0903e022f2ea9f6e21be87dca3a1f1043b7bb83e09be34aeef38e2261d05eb
    source_type: koda_yaml
    transformation_mode: korafy_koda_hybrid
    fs: 100
    cr: 1.79
    run_id: gn-smoke
    review_gate: auto
    scope_statement: Glosas GORE 2026 y su uso operativo; revisar ubicacion semantica
      final.
    dependencies: []
    expected_sections:
    - Contenido
    document_family: generic
    publication_class: knowledge
    skeleton_count: 6
    meat_count: 698
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/gestion__glosas-gores-2026.md.json
---

# Glosas y Requerimientos de Información GORES 2026

## Proposito
Transformación KODA de glosas y requerimientos de información de la Ley de Presupuestos Año 2026 (Partida: Financiamiento Gobiernos Regionales).

## Objetivos

### Objetivos
- FS=100%: preservar contenido normativo + estructura (tablas, numerales, listas).
- Deduplicación: usar Ref para entidades recurrentes.
- Estructura RAG: secciones, actores, restricciones, montos, reporting.

## Definiciones

### Definiciones
| ID | Def |
| --- | --- |
| ACTOR-GORES | gobiernos regionales |
| ENTITY-GORE | Gobierno Regional |
| BODY-CONSEJO-REGIONAL | Consejo Regional |
| BODY-CEMP | Comisión Especial Mixta de Presupuestos |
| ORG-DIPRES | Dirección de Presupuestos |
| ORG-SUBDERE | Subsecretaría de Desarrollo Regional y Administrativo |
| ORG-MDSF | Ministerio de Desarrollo Social y Familia |
| ORG-MTT | Ministerio de Transportes y Telecomunicaciones |
| ORG-SUBINTERIOR | Subsecretaría del Interior |
| LAW-DFL-1-19175 | D.F.L N°1-19.175 |
| LAW-20378 | Ley N°20.378 (Fondo de Apoyo al Transporte Público y la Conectividad Regional) |
| LAW-18091 | ley N°18.091 |
| LAW-20285 | Ley N°20.285 (acceso a la información pública) |
| SUBTITULO-24 | Subtítulo 24 |
| ITEM-3303 | Ítem 33.03 |
| RES-EX-33-2024-MCTCI | Resolución Exenta N° 33, de 2024 (Ministerio de Ciencias, Tecnología, Conocimiento e Innovación) |

## LEY DE PRESUPUESTOS AÑO 2026

### Partida
Financiamiento Gobiernos Regionales

### Units
Miles de $

### Economic Classification Incomes Expenses

#### Table
| Sub-Título | Clasificación Económica | Gobiernos Regionales (01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16) |
| --- | --- | --- |
| INGRESOS |  | 1.900.047.503 |
| 05 | Transferencias Corrientes | 17.827.479 |
| 09 | Aporte Fiscal | 1.124.303.237 |
| 13 | Transferencias para Gastos de Capital | 757.916.787 |
| GASTOS |  | 1.900.047.503 |
| 24 | Transferencias Corrientes | 128.872.343 |
| 33 | Transferencias de Capital | 1.771.175.160 |

### Glosses
| ID | Title |
| --- | --- |
| GLOSA-01-FUNCIONAMIENTO-REGIONAL | 01 Aplicable a Funcionamiento Regional |
| GLOSA-02-INVERSION-REGIONAL | 02 Aplicable a Inversión Regional |
| GLOSA-03-RESTRICCIONES-FINANCIAMIENTO | 03 Restricciones de Financiamiento |
| GLOSA-04-TRASPASO-RECURSOS | 04 Traspaso de Recursos |
| GLOSA-05-TRANSFERENCIAS-UNIVERSIDADES | 05 Transferencias a Universidades |
| GLOSA-06-OFERTA-PROGRAMATICA-INVERSION-S24 | 06 Oferta Programática e Inversión Regional (Subtítulo 24) |
| GLOSA-07-S24-CONCURSO-VINCULACION-COMUNIDAD-8 | 07 Aplicable al Subtítulo 24 de los presupuestos de inversión de los gobiernos regionales |
| GLOSA-08-INFORMACION-CORPORACIONES | 08 Información sobre Corporaciones |
| GLOSA-09-S29-ACTIVOS-NO-FINANCIEROS | 09 Aplica a Subtítulo 29 (presupuesto de inversión regional) |
| GLOSA-10-S31-INVERSION-PUBLICA | 10 Aplica a Subtítulo 31 (presupuesto de inversión) |
| GLOSA-11-S33-TRANSFERENCIAS-CAPITAL | 11 Transferencias de Capital (Subtítulo 33) |

### Information Requirements

#### Items
| ID |
| --- |
| INFO-REQ-01 |
| INFO-REQ-02 |
| INFO-REQ-03 |
| INFO-REQ-04 |
| INFO-REQ-05 |
| INFO-REQ-06 |
| INFO-REQ-07 |
| INFO-REQ-08 |
| INFO-REQ-09 |
| INFO-REQ-10 |
| INFO-REQ-11 |
| INFO-REQ-12 |
| INFO-REQ-12B |
| INFO-REQ-13 |
| INFO-REQ-13B |
| INFO-REQ-14 |
| INFO-REQ-15 |
| INFO-REQ-16 |

## Validation Report

### Syntax

#### Resultados
YAML parse OK (ruby psych).

### Metrics

#### TER Approx

#### Formula
(source_tokens - artifact_tokens) / source_tokens

#### Method
Heurística chars/4; misma regla en ambos.

#### Resultados
TER ≈ -2,9%: artefacto > fuente (fuente legal ya es densa; overhead YAML/metadata/estructura semántica aumenta tamaño).

#### RD

#### Formula
Ref_usages / total_definitions

#### Ref Usages
65

#### Definiciones
16

#### RD
4.06

#### FS

#### Formula
(preserved_facts / source_facts) * 100

#### Method
Revisión manual/estructural (sin extracción automática de hechos).

#### Target
100

#### FS
100

#### Advertencias
FS=100 declarado por revisión manual; si necesitas auditoría estricta, hacemos diff factual (CM-DIFF-ENGINE) con checklist.
