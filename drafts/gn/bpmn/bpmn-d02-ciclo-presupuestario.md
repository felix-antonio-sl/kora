---
_manifest:
  urn: urn:gn:kb:bpmn-d02-ciclo-presupuestario
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
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
    preserved_facts:
    - AI-Remediator=KODA-TRANSFORMER
    - Creation-Date=2025-12-22
    - 'Ctx=Especificación STS del dominio D02: Ciclo Presupuestario Regional del GORE
      Ñuble, modelado en BPMN.'
    - Format=KODA/Spec
    - Human-Creator=FS
    - Human-Editor=FS
    - ID=BPMN-GN-D02-CICLO-PRESUPUESTARIO-KODA
    - 'LLM_Parsing_Instructions.Content=BEGIN_LLM_INSTRUCTIONS

      You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.


      FIDELITY: Preserve meat (essential information) and skeleton (structure: headers,
      IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic
      prose).


      LEXICON (expand before processing): Act->Action, Cond->Condition, Cpt->Concept,
      Ctx->Context, Def->Definition, Fnd->Foundation, ID->ID, Mech->Mechanism, Mssn->Mission,
      Nat->Nature, Obj->Objective, Proc->Process, Prohib->Prohibition, Purp->Purpose,
      Ref->Reference, Req->Requirement, Res->Result, Resp->Responsible, Src->Source,
      Warn->Warning.


      REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS
      document. External documents and legal sources are mentioned as contextual information
      under Ctx: or Src:.


      LANGUAGE POLICY: Keywords in English (and abbreviated forms as listed), content
      in original language (Spanish). Never translate content.

      END_LLM_INSTRUCTIONS

      '
    - LLM_Parsing_Instructions.ID=KODA-LLM-PARSER-01
    - LLM_Parsing_Instructions.Prohib=Using for artifact creation or translation.
    - LLM_Parsing_Instructions.Req=Mandatory block following Metadata.
    - Mapa_General_Dominio.Cpt=Mapa general del ciclo anual del presupuesto regional
      (P1–P5) y proceso transversal de modificaciones presupuestarias.
    - Mapa_General_Dominio.ID=BPMN-GN-PRESUPUESTO-MAPA-01
    - "Mapa_General_Dominio.Mermaid=flowchart LR\n    subgraph CICLO[\"\U0001F4C5\
      \ Ciclo Anual\"]\n        P1[\"P1: Formulación<br/>(May-Jun)\"]\n        P2[\"\
      P2: Aprobación<br/>(Sep-Nov)\"]\n        P3[\"P3: Distribución<br/>(Dic-Ene)\"\
      ]\n        P4[\"P4: Ejecución<br/>(Todo el año)\"]\n        P5[\"P5: Control\
      \ y<br/>Cierre (Dic-Ene)\"]\n    end\n\n    subgraph TRANSVERSAL[\"\U0001F504\
      \ Transversal\"]\n        PM[\"Modificaciones<br/>Presupuestarias\"]\n    end\n\
      \n    P1 --> P2 --> P3 --> P4 --> P5\n    P4 <--> PM\n    P5 -.->|\"Retroalimentación\"\
      | P1\n\n    style P1 fill:#2196F3,color:#fff\n    style P2 fill:#4CAF50,color:#fff\n\
      \    style P3 fill:#FF9800,color:#fff\n    style P4 fill:#9C27B0,color:#fff\n\
      \    style P5 fill:#607D8B,color:#fff\n    style PM fill:#E91E63,color:#fff\n"
    - Metadatos_Dominio.Criticidad=🔴 Crítica
    - Metadatos_Dominio.Dueno=DAF (Funcionamiento) / DIPIR (Inversión)
    - Metadatos_Dominio.ID=DOM-PRESUPUESTO
    - Metadatos_Dominio.Procesos=5
    - Metadatos_Dominio.Ref_Fuente.Ctx_Required[0]=knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml
      L.500-1886
    - Metadatos_Dominio.Subprocesos=~15
    - Model-Collaborator[0]=Cascade
    - Modification-Date=2025-12-22
    - Normativa_Aplicable.Filas[0].Alcance=Competencias presupuestarias
    - Normativa_Aplicable.Filas[0].Norma=LOC 19.175 Art. 72-73
    - Normativa_Aplicable.Filas[1].Alcance=Clasificador presupuestario
    - Normativa_Aplicable.Filas[1].Norma=Decreto 854/2004 Hacienda
    - Normativa_Aplicable.Filas[2].Alcance=Marco legal ejercicio
    - Normativa_Aplicable.Filas[2].Norma=Ley de Presupuestos (anual)
    - Normativa_Aplicable.Filas[3].Alcance=3% emergencias
    - Normativa_Aplicable.Filas[3].Norma=Glosa 14 Partida 31
    - Normativa_Aplicable.Filas[4].Alcance=Transparencia
    - Normativa_Aplicable.Filas[4].Norma=Glosa 16 Partida 31
    - Normativa_Aplicable.Filas[5].Alcance=Contabilidad gubernamental
    - Normativa_Aplicable.Filas[5].Norma=NICSP-CGR
    - Normativa_Aplicable.Filas[6].Alcance=Rendiciones
    - Normativa_Aplicable.Filas[6].Norma=Resolución 30/2015 CGR
    - Normativa_Aplicable.ID=BPMN-GN-PRESUPUESTO-NORMATIVA-01
    - "P1_Formulacion_del_Presupuesto.Diagrama_de_Flujo.Mermaid=flowchart TD\n   \
      \ A[\"\U0001F4DC DIPRES emite<br/>instructivo y clasificador\"] --> B[\"Definir\
      \ techos<br/>preliminares\"]\n\n    subgraph INVERSION[\"\U0001F4BC Inversión\
      \ (DIPIR)\"]\n        C1[\"Propuesta marco<br/>de inversión\"]\n        C2[\"\
      Cartera proyectos<br/>con RS vigente\"]\n        C3[\"Asignaciones por<br/>fuente\
      \ (FNDR/FRIL/FRPD)\"]\n    end\n\n    subgraph FUNCIONAMIENTO[\"\U0001F3E2 Funcionamiento\
      \ (DAF)\"]\n        D1[\"Personal (Subt. 21)\"]\n        D2[\"Bienes/Servicios\
      \ (Subt. 22)\"]\n        D3[\"Transferencias (Subt. 24)\"]\n    end\n\n    B\
      \ --> C1 & D1\n    C1 --> C2 --> C3\n    D1 --> D2 --> D3\n    C3 & D3 --> E[\"\
      Consolidación<br/>propuesta\"]\n    E --> F[\"Presentación a<br/>Gobernador/a\"\
      ]\n    F --> G[\"Ajustes según<br/>prioridades ERD\"]\n    G --> H[\"\U0001F4E4\
      \ Envío a DIPRES\"]\n\n    style A fill:#2196F3,color:#fff\n    style H fill:#4CAF50,color:#fff\n"
    - P1_Formulacion_del_Presupuesto.Estructura_Presupuesto.Filas[0].Concepto=Personal
    - P1_Formulacion_del_Presupuesto.Estructura_Presupuesto.Filas[0].Responsable=DAF
    - P1_Formulacion_del_Presupuesto.Estructura_Presupuesto.Filas[0].Subtitulo=21
    - P1_Formulacion_del_Presupuesto.Estructura_Presupuesto.Filas[1].Concepto=Bienes
      y Servicios
    - P1_Formulacion_del_Presupuesto.Estructura_Presupuesto.Filas[1].Responsable=DAF
    - P1_Formulacion_del_Presupuesto.Estructura_Presupuesto.Filas[1].Subtitulo=22
    - P1_Formulacion_del_Presupuesto.Estructura_Presupuesto.Filas[2].Concepto=Transferencias
      Corrientes
    - P1_Formulacion_del_Presupuesto.Estructura_Presupuesto.Filas[2].Responsable=DAF/DIPIR
    - P1_Formulacion_del_Presupuesto.Estructura_Presupuesto.Filas[2].Subtitulo=24
    - P1_Formulacion_del_Presupuesto.Estructura_Presupuesto.Filas[3].Concepto=Activos
      No Financieros
    - P1_Formulacion_del_Presupuesto.Estructura_Presupuesto.Filas[3].Responsable=DAF
    - P1_Formulacion_del_Presupuesto.Estructura_Presupuesto.Filas[3].Subtitulo=29
    - P1_Formulacion_del_Presupuesto.Estructura_Presupuesto.Filas[4].Concepto=Inversión
      (Iniciativas)
    - P1_Formulacion_del_Presupuesto.Estructura_Presupuesto.Filas[4].Responsable=DIPIR
    - P1_Formulacion_del_Presupuesto.Estructura_Presupuesto.Filas[4].Subtitulo=31
    - P1_Formulacion_del_Presupuesto.Estructura_Presupuesto.Filas[5].Concepto=Transferencias
      de Capital
    - P1_Formulacion_del_Presupuesto.Estructura_Presupuesto.Filas[5].Responsable=DIPIR
    - P1_Formulacion_del_Presupuesto.Estructura_Presupuesto.Filas[5].Subtitulo=33
    - P1_Formulacion_del_Presupuesto.Estructura_Presupuesto.ID=BPMN-GN-PRESUPUESTO-ESTRUCTURA-01
    - P1_Formulacion_del_Presupuesto.ID=BPMN-GN-PRESUPUESTO-FORMULACION-01
    - P1_Formulacion_del_Presupuesto.Periodo=Mayo-Junio (año anterior)
    - P2_Aprobacion_del_Presupuesto.Cpt=Proceso de aprobación del presupuesto regional
      (Gobernador, CORE, DIPRES, CGR).
    - P2_Aprobacion_del_Presupuesto.ID=BPMN-GN-PRESUPUESTO-APROBACION-01
    - P3_Distribucion_Inicial.Cpt=Distribución inicial del presupuesto aprobado y
      carga en SIGFE.
    - P3_Distribucion_Inicial.ID=BPMN-GN-PRESUPUESTO-DISTRIBUCION-01
    - P4_Ejecucion_Presupuestaria.Cpt=Ejecución durante el año, con seguimiento de
      compromisos, devengos y pagos.
    - P4_Ejecucion_Presupuestaria.ID=BPMN-GN-PRESUPUESTO-EJECUCION-01
    - P5_Control_y_Cierre_de_Ejercicio.Deuda_Flotante.ID=BPMN-GN-PRESUPUESTO-DEUDA-FLOTANTE-01
    - "P5_Control_y_Cierre_de_Ejercicio.Deuda_Flotante.Mermaid=flowchart TD\n    A[\"\
      Obligaciones devengadas<br/>al 31/12 pendientes<br/>de pago\"] --> B{\"¿SIC<br/>suficiente?\"\
      }\n    B -->|\"Sí\"| C[\"Financiar con<br/>SIC\"]\n    B -->|\"No\"| D[\"SIC\
      \ + Mayor<br/>aporte fiscal\"]\n    C & D --> E[\"Incorporar en<br/>presupuesto\
      \ año siguiente\"]\n    E --> F[\"Primera prioridad<br/>de pago\"]\n\n    style\
      \ F fill:#FF9800,color:#fff\n"
    - "P5_Control_y_Cierre_de_Ejercicio.Diagrama_de_Flujo.Mermaid=flowchart TD\n \
      \   subgraph CONTROL[\"\U0001F50D Control Durante el Año\"]\n        A[\"Control\
      \ interno<br/>(DAF, DIPIR, U. Control)\"]\n        B[\"Seguimiento DIPRES<br/>(mensual)\"\
      ]\n        C[\"Sistema KPIs y<br/>alertas tempranas\"]\n    end\n\n    subgraph\
      \ CIERRE[\"\U0001F4C5 Cierre 31/12\"]\n        D[\"Consolidar<br/>información\
      \ (DAF)\"]\n        E[\"Cerrar cuentas<br/>en SIGFE\"]\n        F[\"Calcular\
      \ deuda<br/>flotante\"]\n        G[\"Regularizar<br/>deuda flotante\"]\n   \
      \     H[\"Informe cierre<br/>a DIPRES/CGR\"]\n    end\n\n    subgraph EVALUACION[\"\
      \U0001F4CA Evaluación\"]\n        I[\"Evaluar resultados<br/>físicos y financieros\"\
      ]\n        J[\"Informe evaluación<br/>ex post (DIPIR)\"]\n    end\n\n    A &\
      \ B & C --> D --> E --> F --> G --> H\n    H --> I --> J\n\n    style H fill:#607D8B,color:#fff\n\
      \    style J fill:#9C27B0,color:#fff\n"
    - P5_Control_y_Cierre_de_Ejercicio.ID=BPMN-GN-PRESUPUESTO-CIERRE-01
    - P5_Control_y_Cierre_de_Ejercicio.Periodo=Diciembre-Enero
    - P5_Control_y_Cierre_de_Ejercicio.Reporteria_Oficial.Filas[0].Destinatario=DIPRES,
      CORE
    - P5_Control_y_Cierre_de_Ejercicio.Reporteria_Oficial.Filas[0].Frecuencia=Mensual
    - P5_Control_y_Cierre_de_Ejercicio.Reporteria_Oficial.Filas[0].Reporte=Informe
      Ejecución Mensual
    - P5_Control_y_Cierre_de_Ejercicio.Reporteria_Oficial.Filas[1].Destinatario=Transparencia
    - P5_Control_y_Cierre_de_Ejercicio.Reporteria_Oficial.Filas[1].Frecuencia=Trimestral
    - P5_Control_y_Cierre_de_Ejercicio.Reporteria_Oficial.Filas[1].Reporte=Informes
      por Glosas
    - P5_Control_y_Cierre_de_Ejercicio.Reporteria_Oficial.Filas[2].Destinatario=Web
      institucional
    - P5_Control_y_Cierre_de_Ejercicio.Reporteria_Oficial.Filas[2].Frecuencia=Mensual
    - P5_Control_y_Cierre_de_Ejercicio.Reporteria_Oficial.Filas[2].Reporte=Cartera
      de Proyectos
    - P5_Control_y_Cierre_de_Ejercicio.Reporteria_Oficial.Filas[3].Destinatario=Web
      institucional
    - P5_Control_y_Cierre_de_Ejercicio.Reporteria_Oficial.Filas[3].Frecuencia=5 días
      hábiles
    - P5_Control_y_Cierre_de_Ejercicio.Reporteria_Oficial.Filas[3].Reporte=Acuerdos
      CORE
    - P5_Control_y_Cierre_de_Ejercicio.Reporteria_Oficial.ID=BPMN-GN-PRESUPUESTO-REPORTES-01
    - Referencias_Cruzadas.Filas[0].Ctx_Optional[0]=file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D03_gestion_ipr.md
    - Referencias_Cruzadas.Filas[0].Dominio_Relacionado=D03 Gestión IPR
    - Referencias_Cruzadas.Filas[0].Vinculo=CDP, financiamiento proyectos
    - Referencias_Cruzadas.Filas[1].Ctx_Optional[0]=file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D08_rendiciones.md
    - Referencias_Cruzadas.Filas[1].Dominio_Relacionado=D08 Rendiciones
    - Referencias_Cruzadas.Filas[1].Vinculo=Contabilización, SIGFE
    - Referencias_Cruzadas.Filas[2].Ctx_Optional[0]=file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D04_compras_contrataciones.md
    - Referencias_Cruzadas.Filas[2].Dominio_Relacionado=D04 Compras
    - Referencias_Cruzadas.Filas[2].Vinculo=Órdenes de compra, contratos
    - Referencias_Cruzadas.ID=BPMN-GN-PRESUPUESTO-REFERENCIAS-01
    - Sistemas_Involucrados.Filas[0].Funcion=Gestión financiera central
    - Sistemas_Involucrados.Filas[0].Sistema=SYS-SIGFE
    - Sistemas_Involucrados.Filas[1].Funcion=Inversión pública
    - Sistemas_Involucrados.Filas[1].Sistema=SYS-BIP-SNI
    - Sistemas_Involucrados.Filas[2].Funcion=Publicación información
    - Sistemas_Involucrados.Filas[2].Sistema=SYS-TRANSPARENCIA
    - Sistemas_Involucrados.ID=BPMN-GN-PRESUPUESTO-SISTEMAS-01
    - Source.Ctx_Required[0]=knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml
    - Source.Ctx_Required[1]=knowledge/domains/gn/presupuesto/kb_gn_018_gestion_prpto_koda.yml
    - Source.Primary-Source=sources/gn/arquitectura/bpmn/D02_ciclo_presupuestario.md
    - Status=Draft
    - 'Ultima_Actualizacion.Cpt=Última actualización: 2025-12-16'
    - Ultima_Actualizacion.ID=BPMN-GN-PRESUPUESTO-ULT-ACT-01
    - Version=1.0.0
    - _manifest.compatibility.breaking_changes_from=null
    - _manifest.compatibility.min_consumer_version=1.0.0
    - _manifest.dependencies.requires[0].reason=KODA/Spec format compliance
    - _manifest.dependencies.requires[0].urn=urn:knowledge:koda:core:spec:1.0.0
    - _manifest.dependencies.requires[1].reason=Transformation methodology reference
    - _manifest.dependencies.requires[1].urn=urn:knowledge:koda:core:transform:1.0.0
    - _manifest.dependencies.requires[2].reason=Guía integral de gestión presupuestaria
      regional
    - _manifest.dependencies.requires[2].urn=urn:knowledge:gorenuble:gn:gestion-prpto:1.0.0
    - _manifest.federation.license=Institutional Use
    - _manifest.federation.visibility=internal
    - _manifest.provenance.created_at=2025-12-22
    - _manifest.provenance.created_by=FS
    - _manifest.provenance.last_modified_at=2025-12-22
    - _manifest.provenance.model_collaborators[0]=Cascade
    - _manifest.provenance.model_collaborators[1]=KODA-TRANSFORMER
    - _manifest.resolution.canonical_url=file://knowledge/domains/gn/arquitectura/bpmn/D02_ciclo_presupuestario_koda.yml
    - _manifest.urn=urn:knowledge:gorenuble:gn:bpmn-d02-ciclo-presupuestario:1.0.0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
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
