---
_manifest:
  urn: urn:gn:kb:bpmn-d02-ciclo-presupuestario
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/04_habilitadores/arquitectura/bpmn/D02_ciclo_presupuestario_koda.yml
version: 2.0.0
status: published
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
    cr: 1.28
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 25
    meat_count: 124
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/bpmn__bpmn-d02-ciclo-presupuestario.md.json
---

# BPMN D02: Ciclo Presupuestario Regional
## ID
BPMN-GN-D02-CICLO-PRESUPUESTARIO-KODA

## Version
1.0.0

## Status
Draft

## Format
KODA/Spec

## Human Creator
FS

## Human Editor
FS

## Model Collaborator
- Cascade

## AI Remediator
KODA-TRANSFORMER

## Creation Date
2025-12-22

## Modification Date
2025-12-22

## Ctx
Especificación STS del dominio D02: Ciclo Presupuestario Regional del GORE Ñuble, modelado en BPMN.

## Source
### Ctx Required
- knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml
- knowledge/domains/gn/presupuesto/kb_gn_018_gestion_prpto_koda.yml
### Primary Source
sources/gn/arquitectura/bpmn/D02_ciclo_presupuestario.md

## LLM Parsing Instructions
### ID
KODA-LLM-PARSER-01
### Req
Mandatory block following Metadata.
### Prohib
Using for artifact creation or translation.
### Content
BEGIN_LLM_INSTRUCTIONS
You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).

LEXICON (expand before processing): Act->Action, Cond->Condition, Cpt->Concept, Ctx->Context, Def->Definition, Fnd->Foundation, ID->ID, Mech->Mechanism, Mssn->Mission, Nat->Nature, Obj->Objective, Proc->Process, Prohib->Prohibition, Purp->Purpose, Ref->Reference, Req->Requirement, Res->Result, Resp->Responsible, Src->Source, Warn->Warning.

REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. External documents and legal sources are mentioned as contextual information under Ctx: or Src:.

LANGUAGE POLICY: Keywords in English (and abbreviated forms as listed), content in original language (Spanish). Never translate content.
END_LLM_INSTRUCTIONS


## Metadatos Dominio
### ID
DOM-PRESUPUESTO
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
### ID
BPMN-GN-PRESUPUESTO-MAPA-01
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
### ID
BPMN-GN-PRESUPUESTO-FORMULACION-01
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
#### ID
BPMN-GN-PRESUPUESTO-ESTRUCTURA-01
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
### ID
BPMN-GN-PRESUPUESTO-APROBACION-01
### Cpt
Proceso de aprobación del presupuesto regional (Gobernador, CORE, DIPRES, CGR).

## P3 Distribucion Inicial
### ID
BPMN-GN-PRESUPUESTO-DISTRIBUCION-01
### Cpt
Distribución inicial del presupuesto aprobado y carga en SIGFE.

## P4 Ejecucion Presupuestaria
### ID
BPMN-GN-PRESUPUESTO-EJECUCION-01
### Cpt
Ejecución durante el año, con seguimiento de compromisos, devengos y pagos.

## P5 Control y Cierre de Ejercicio
### ID
BPMN-GN-PRESUPUESTO-CIERRE-01
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
#### ID
BPMN-GN-PRESUPUESTO-DEUDA-FLOTANTE-01
#### Mermaid
flowchart TD
    A["Obligaciones devengadas<br/>al 31/12 pendientes<br/>de pago"] --> B{"¿SIC<br/>suficiente?"}
    B -->|"Sí"| C["Financiar con<br/>SIC"]
    B -->|"No"| D["SIC + Mayor<br/>aporte fiscal"]
    C & D --> E["Incorporar en<br/>presupuesto año siguiente"]
    E --> F["Primera prioridad<br/>de pago"]

    style F fill:#FF9800,color:#fff

### Reporteria Oficial
#### ID
BPMN-GN-PRESUPUESTO-REPORTES-01
#### Filas
| Reporte | Frecuencia | Destinatario |
| --- | --- | --- |
| Informe Ejecución Mensual | Mensual | DIPRES, CORE |
| Informes por Glosas | Trimestral | Transparencia |
| Cartera de Proyectos | Mensual | Web institucional |
| Acuerdos CORE | 5 días hábiles | Web institucional |

## Sistemas Involucrados
### ID
BPMN-GN-PRESUPUESTO-SISTEMAS-01
### Filas
| Sistema | Funcion |
| --- | --- |
| SYS-SIGFE | Gestión financiera central |
| SYS-BIP-SNI | Inversión pública |
| SYS-TRANSPARENCIA | Publicación información |

## Normativa Aplicable
### ID
BPMN-GN-PRESUPUESTO-NORMATIVA-01
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
### ID
BPMN-GN-PRESUPUESTO-REFERENCIAS-01
### Filas
| Dominio_Relacionado | Ctx_Optional | Vinculo |
| --- | --- | --- |
| D03 Gestión IPR | ['file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D03_gestion_ipr.md'] | CDP, financiamiento proyectos |
| D08 Rendiciones | ['file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D08_rendiciones.md'] | Contabilización, SIGFE |
| D04 Compras | ['file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D04_compras_contrataciones.md'] | Órdenes de compra, contratos |

## Ultima Actualizacion
### ID
BPMN-GN-PRESUPUESTO-ULT-ACT-01
### Cpt
Última actualización: 2025-12-16
