---
_manifest:
  urn: urn:gn:kb:bpmn-d02-ciclo-presupuestario
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
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
    cr: 1.65
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 12
    meat_count: 92
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/bpmn__bpmn-d02-ciclo-presupuestario.md.json
---

# BPMN D02: Ciclo Presupuestario Regional
## Source
### Ctx Required
- knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml
- knowledge/domains/gn/presupuesto/kb_gn_018_gestion_prpto_koda.yml

## Metadatos Dominio
### Criticidad
🔴 Crítica
### Dueno
DAF (Funcionamiento) / DIPIR (Inversión)
### Procesos
5
### Subprocesos
~15
### Ref Fuente
#### Ctx Required
- knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml L.500-1886

## Mapa General Dominio
### Cpt
Mapa general del ciclo anual del presupuesto regional (P1–P5) y proceso transversal de modificaciones presupuestarias.
### Mermaid
flowchart LR
    subgraph CICLO["📅 Ciclo Anual"]
        P1["P1: Formulación<br/>(May-Jun)"]
        P2["P2: Aprobación<br/>(Sep-Nov)"]
        P3["P3: Distribución<br/>(Dic-Ene)"]
        P4["P4: Ejecución<br/>(Todo el año)"]
        P5["P5: Control y<br/>Cierre (Dic-Ene)"]
    end

    subgraph TRANSVERSAL["🔄 Transversal"]
        PM["Modificaciones<br/>Presupuestarias"]
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
### Periodo
Mayo-Junio (año anterior)
### Diagrama de Flujo
#### Mermaid
flowchart TD
    A["📜 DIPRES emite<br/>instructivo y clasificador"] --> B["Definir techos<br/>preliminares"]

    subgraph INVERSION["💼 Inversión (DIPIR)"]
        C1["Propuesta marco<br/>de inversión"]
        C2["Cartera proyectos<br/>con RS vigente"]
        C3["Asignaciones por<br/>fuente (FNDR/FRIL/FRPD)"]
    end

    subgraph FUNCIONAMIENTO["🏢 Funcionamiento (DAF)"]
        D1["Personal (Subt. 21)"]
        D2["Bienes/Servicios (Subt. 22)"]
        D3["Transferencias (Subt. 24)"]
    end

    B --> C1 & D1
    C1 --> C2 --> C3
    D1 --> D2 --> D3
    C3 & D3 --> E["Consolidación<br/>propuesta"]
    E --> F["Presentación a<br/>Gobernador/a"]
    F --> G["Ajustes según<br/>prioridades ERD"]
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
### Cpt
Proceso de aprobación del presupuesto regional (Gobernador, CORE, DIPRES, CGR).

## P3 Distribucion Inicial
### Cpt
Distribución inicial del presupuesto aprobado y carga en SIGFE.

## P4 Ejecucion Presupuestaria
### Cpt
Ejecución durante el año, con seguimiento de compromisos, devengos y pagos.

## P5 Control y Cierre de Ejercicio
### Periodo
Diciembre-Enero
### Diagrama de Flujo
#### Mermaid
flowchart TD
    subgraph CONTROL["🔍 Control Durante el Año"]
        A["Control interno<br/>(DAF, DIPIR, U. Control)"]
        B["Seguimiento DIPRES<br/>(mensual)"]
        C["Sistema KPIs y<br/>alertas tempranas"]
    end

    subgraph CIERRE["📅 Cierre 31/12"]
        D["Consolidar<br/>información (DAF)"]
        E["Cerrar cuentas<br/>en SIGFE"]
        F["Calcular deuda<br/>flotante"]
        G["Regularizar<br/>deuda flotante"]
        H["Informe cierre<br/>a DIPRES/CGR"]
    end

    subgraph EVALUACION["📊 Evaluación"]
        I["Evaluar resultados<br/>físicos y financieros"]
        J["Informe evaluación<br/>ex post (DIPIR)"]
    end

    A & B & C --> D --> E --> F --> G --> H
    H --> I --> J

    style H fill:#607D8B,color:#fff
    style J fill:#9C27B0,color:#fff

### Deuda Flotante
#### Mermaid
flowchart TD
    A["Obligaciones devengadas<br/>al 31/12 pendientes<br/>de pago"] --> B{"¿SIC<br/>suficiente?"}
    B -->|"Sí"| C["Financiar con<br/>SIC"]
    B -->|"No"| D["SIC + Mayor<br/>aporte fiscal"]
    C & D --> E["Incorporar en<br/>presupuesto año siguiente"]
    E --> F["Primera prioridad<br/>de pago"]

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
| D03 Gestión IPR | ['file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D03_gestion_ipr.md'] | CDP, financiamiento proyectos |
| D08 Rendiciones | ['file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D08_rendiciones.md'] | Contabilización, SIGFE |
| D04 Compras | ['file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D04_compras_contrataciones.md'] | Órdenes de compra, contratos |

## Ultima Actualizacion
### Cpt
Última actualización: 2025-12-16
