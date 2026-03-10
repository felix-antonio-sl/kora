---
_manifest:
  urn: urn:gn:kb:bpmn-d02-ciclo-presupuestario
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-10'
    source: domains/gn/04_habilitadores/arquitectura/bpmn/D02_ciclo_presupuestario_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- presupuesto
- bpmn
- finanzas
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/04_habilitadores/arquitectura/bpmn/D02_ciclo_presupuestario_koda.yml
    source_hashes:
      domains/gn/04_habilitadores/arquitectura/bpmn/D02_ciclo_presupuestario_koda.yml: a0c587cb39904c946b6bf1f1c6dd57cd93abfb442ff13174afd931516b856578
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.64
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    document_family: generic
    publication_class: knowledge
    skeleton_count: 12
    meat_count: 92
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/bpmn__bpmn-d02-ciclo-presupuestario.md.json
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:gn:kb:bpmn-d02-ciclo-presupuestario
---

# BPMN D02: Ciclo Presupuestario Regional
- **Contexto requerido:** , 

## Metadatos Dominio
- **Criticidad:** 🔴 Crítica
- **Dueno:** DAF (Funcionamiento) / DIPIR (Inversión)
- **Procesos:** 5
- **Subprocesos:** ~15
### Referencias
- **Contexto requerido:** L.500-1886

## Mapa General Dominio
- **Cpt:** Mapa general del ciclo anual del presupuesto regional (P1–P5) y proceso transversal de modificaciones presupuestarias.
- **Mermaid:** flowchart LR
 subgraph CICLO["📅 Ciclo Anual"]
 P1["P1: Formulación; (May-Jun)"]
 P2["P2: Aprobación; (Sep-Nov)"]
 P3["P3: Distribución; (Dic-Ene)"]
 P4["P4: Ejecución; (Todo el año)"]
 P5["P5: Control y; Cierre (Dic-Ene)"]
 end

 subgraph TRANSVERSAL["🔄 Transversal"]
 PM["Modificaciones; Presupuestarias"]
 end

 P1 --> P2 --> P3 --> P4 --> P5
 P4 <--> PM
 P5 -.->|"Retroalimentación"| P1

 style P1 fill:#2196F3,color:#fff
 style P2 fill:#4CAF50,color:#fff
 style P3 fill:#FF9800,color:#fff
 style P4 fill:#9C27B0,color:#fff
 style P5 fill:#607D8B,color:#fff
 style PM fill:#E91E63,color:#fff

## P1 Formulacion del Presupuesto
- **Periodo:** Mayo-Junio (año anterior)
### Diagrama de Flujo
- **Mermaid:** flowchart TD
 A["📜 DIPRES emite; instructivo y clasificador"] --> B["Definir techos; preliminares"]

 subgraph INVERSION["💼 Inversión (DIPIR)"]
 C1["Propuesta marco; de inversión"]
 C2["Cartera proyectos; con RS vigente"]
 C3["Asignaciones por; fuente (FNDR/FRIL/FRPD)"]
 end

 subgraph FUNCIONAMIENTO["🏢 Funcionamiento (DAF)"]
 D1["Personal (Subt. 21)"]
 D2["Bienes/Servicios (Subt. 22)"]
 D3["Transferencias (Subt. 24)"]
 end

 B --> C1 & D1
 C1 --> C2 --> C3
 D1 --> D2 --> D3
 C3 & D3 --> E["Consolidación; propuesta"]
 E --> F["Presentación a; Gobernador/a"]
 F --> G["Ajustes según; prioridades ERD"]
 G --> H["📤 Envío a DIPRES"]

 style A fill:#2196F3,color:#fff
 style H fill:#4CAF50,color:#fff

### Estructura Presupuesto
#### Filas
| Subtitulo | Concepto | Responsable |
| --- | --- | --- |
| 21 | Personal | DAF |
| 22 | Bienes y Servicios | DAF |
| 24 | Transferencias Corrientes | DAF/DIPIR |
| 29 | Activos No Financieros | DAF |
| 31 | Inversión (Iniciativas) | DIPIR |
| 33 | Transferencias de Capital | DIPIR |

## P2 Aprobacion del Presupuesto
- **Cpt:** Proceso de aprobación del presupuesto regional (Gobernador, CORE, DIPRES, CGR).

## P3 Distribucion Inicial
- **Cpt:** Distribución inicial del presupuesto aprobado y carga en SIGFE.

## P4 Ejecucion Presupuestaria
- **Cpt:** Ejecución durante el año, con seguimiento de compromisos, devengos y pagos.

## P5 Control y Cierre de Ejercicio
- **Periodo:** Diciembre-Enero
### Diagrama de Flujo
- **Mermaid:** flowchart TD
 subgraph CONTROL["🔍 Control Durante el Año"]
 A["Control interno; (DAF, DIPIR, U. Control)"]
 B["Seguimiento DIPRES; (mensual)"]
 C["Sistema KPIs y; alertas tempranas"]
 end

 subgraph CIERRE["📅 Cierre 31/12"]
 D["Consolidar; información (DAF)"]
 E["Cerrar cuentas; en SIGFE"]
 F["Calcular deuda; flotante"]
 G["Regularizar; deuda flotante"]
 H["Informe cierre; a DIPRES/CGR"]
 end

 subgraph EVALUACION["📊 Evaluación"]
 I["Evaluar resultados; físicos y financieros"]
 J["Informe evaluación; ex post (DIPIR)"]
 end

 A & B & C --> D --> E --> F --> G --> H
 H --> I --> J

 style H fill:#607D8B,color:#fff
 style J fill:#9C27B0,color:#fff

### Deuda Flotante
- **Mermaid:** flowchart TD
 A["Obligaciones devengadas; al 31/12 pendientes; de pago"] --> B{"¿SIC; suficiente?"}
 B -->|"Sí"| C["Financiar con; SIC"]
 B -->|"No"| D["SIC + Mayor; aporte fiscal"]
 C & D --> E["Incorporar en; presupuesto año siguiente"]
 E --> F["Primera prioridad; de pago"]

 style F fill:#FF9800,color:#fff

### Reporteria Oficial
#### Filas
| Reporte | Frecuencia | Destinatario |
| --- | --- | --- |
| Informe Ejecución Mensual | Mensual | DIPRES, CORE |
| Informes por Glosas | Trimestral | Transparencia |
| Cartera de Proyectos | Mensual | Web institucional |
| Acuerdos CORE | 5 días hábiles | Web institucional |

## Sistemas Involucrados
### Filas
| Sistema | Funcion |
| --- | --- |
| SYS-SIGFE | Gestión financiera central |
| SYS-BIP-SNI | Inversión pública |
| SYS-TRANSPARENCIA | Publicación información |

## Normativa Aplicable
### Filas
| Norma | Alcance |
| --- | --- |
| LOC 19.175 Art. 72-73 | Competencias presupuestarias |
| Decreto 854/2004 Hacienda | Clasificador presupuestario |
| Ley de Presupuestos (anual) | Marco legal ejercicio |
| Glosa 14 Partida 31 | 3% emergencias |
| Glosa 16 Partida 31 | Transparencia |
| NICSP-CGR | Contabilidad gubernamental |
| Resolución 30/2015 CGR | Rendiciones |

## Referencias Cruzadas
### Filas
| Dominio_Relacionado | Ctx_Optional | Vinculo |
| --- | --- | --- |
| D03 Gestión IPR | | CDP, financiamiento proyectos |
| D08 Rendiciones | | Contabilización, SIGFE |
| D04 Compras | | Órdenes de compra, contratos |

## Ultima Actualizacion
- **Cpt:** Última actualización: 2025-12-16
