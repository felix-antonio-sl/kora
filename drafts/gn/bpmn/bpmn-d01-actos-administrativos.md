---
_manifest:
  urn: urn:gn:kb:bpmn-d01-actos-administrativos
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/04_habilitadores/arquitectura/bpmn/D01_actos_administrativos_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- bpmn
- actos-administrativos
- ley-19880
- ley-21180
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/04_habilitadores/arquitectura/bpmn/D01_actos_administrativos_koda.yml
    source_hashes:
      domains/gn/04_habilitadores/arquitectura/bpmn/D01_actos_administrativos_koda.yml: b0cfd30ba3085e4149285f535c9083cf50f7abcc622a77edf76c80b1d324c84e
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
    skeleton_count: 23
    meat_count: 127
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/bpmn__bpmn-d01-actos-administrativos.md.json
---

# BPMN D01: Tramitación de Actos Administrativos
## ID
BPMN-GN-D01-ACTOS-ADMIN-KODA

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
Especificación STS del dominio D01: Tramitación de Actos Administrativos del GORE Ñuble, modelado en BPMN.

## Source
### Ctx Required
- knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml
### Primary Source
sources/gn/arquitectura/bpmn/D01_actos_administrativos.md

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
DOM-ACTOS-ADMIN
### Criticidad
🟠 Alta
### Dueno
Unidad Jurídica
### Procesos
2
### Subprocesos
~14 fases
### Ref Fuente
#### Ctx Required
- knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml L.100-499

## Mapa General Dominio
### ID
BPMN-GN-ACTOS-ADMIN-MAPA-01
### Cpt
Mapa general de los procesos de actos administrativos (resoluciones exentas y convenios/transferencias) y elementos transversales.
### Mermaid
flowchart LR
    subgraph PROCESOS["📋 Procesos de Actos Administrativos"]
        P1["P1: Resoluciones<br/>Exentas"]
        P2["P2: Convenios y<br/>Transferencias"]
    end

    subgraph TRANSVERSAL["🔧 Elementos Transversales"]
        T1["Expediente<br/>Electrónico"]
        T2["Firma Electrónica<br/>Avanzada"]
        T3["Toma de Razón<br/>(cuando aplica)"]
    end

    P1 --> T1 & T2
    P2 --> T1 & T2 & T3

    style P1 fill:#2196F3,color:#fff
    style P2 fill:#4CAF50,color:#fff


## P1 Flujo Resoluciones Exentas
### ID
BPMN-GN-RES-EXENTAS-FLUJO-01
### Fases
7
### SLA
15 días hábiles
### Diagrama de Flujo Completo
#### Mermaid
flowchart TD
    subgraph FASE1["1️⃣ Iniciación"]
        A["Área Requirente:<br/>Elaborar borrador"]
        B["Adjuntar<br/>antecedentes"]
        C["Ingresar al SGD"]
    end

    subgraph FASE2["2️⃣ Revisión Jurídica"]
        D["Jurídica recibe<br/>expediente"]
        E["Verificar legalidad<br/>y forma"]
        F{"¿OK?"}
        G["✅ V°B° Jurídico"]
        H["❌ Observar"]
    end

    subgraph FASE3["3️⃣ Gestión"]
        I["Centro Gestión:<br/>Asignar N° resolución"]
        J["Completar<br/>formalidades"]
    end

    subgraph FASE4["4️⃣ Control"]
        K["Unidad Control:<br/>Verificar procedencia"]
        L{"¿Conforme?"}
        M["✅ V°B° Control"]
        N["❌ Reparar"]
    end

    subgraph FASE5["5️⃣ V°B° Administrador/a"]
        O["Administrador/a Regional:<br/>Revisar y visar"]
    end

    subgraph FASE6["6️⃣ Firma"]
        P["Gobernador/a:<br/>Firma con FEA"]
    end

    subgraph FASE7["7️⃣ Notificación y Archivo"]
        Q["Oficina Partes:<br/>Numerar y fechar"]
        R["Notificar a<br/>interesados"]
        S["Publicar si<br/>corresponde"]
        T["Archivar expediente"]
    end

    A --> B --> C --> D --> E --> F
    F -->|"Sí"| G --> I --> J --> K --> L
    F -->|"No"| H --> A
    L -->|"Sí"| M --> O --> P --> Q --> R --> S --> T
    L -->|"No"| N --> A

    style P fill:#4CAF50,color:#fff
    style T fill:#607D8B,color:#fff

### Roles por Fase
#### ID
BPMN-GN-RES-EXENTAS-ROLES-01
#### Filas
| Fase | Responsable |
| --- | --- |
| Iniciación | Área Requirente |
| Revisión Jurídica | Unidad Jurídica |
| Gestión | Centro de Gestión |
| Control | Unidad de Control |
| V°B° Administrador/a | Administrador/a Regional |
| Firma | Gobernador/a Regional |
| Notificación y Archivo | Oficina de Partes |

## P2 Convenios y Transferencias
### ID
BPMN-GN-CONVENIOS-TRANSFERENCIAS-01
### Cpt
Proceso para la tramitación de convenios y transferencias asociadas a actos administrativos.
### Diagrama de Flujo
#### Mermaid
flowchart TD
    A["Área requirente<br/>propone convenio"] --> B["Elaborar borrador<br/>de convenio"]
    B --> C["Revisión Jurídica"]
    C --> D{"¿Ajustes?"}
    D -->|"Sí"| B
    D -->|"No"| E["Resolución que<br/>aprueba convenio"]
    E --> F["Toma de Razón<br/>si corresponde"]
    F --> G["Firma de partes"]
    G --> H["Ejecución y<br/>seguimiento"]

### Contenido Minimo Convenio
#### ID
BPMN-GN-CONVENIOS-CONTENIDO-01
#### Filas
| Elemento | Descripcion |
| --- | --- |
| Partes | GORE + Entidad receptora |
| Objeto | Descripción del programa/proyecto |
| Monto | Valor total y calendario |
| Plazos | Duración y fechas clave |
| Obligaciones | Deberes de cada parte |
| Rendicion | Modalidad, plazos, SISREC |
| Restitucion | Condiciones de devolución |
| Probidad | Cláusulas anticorrupción |
### Criterios Toma de Razon
#### ID
BPMN-GN-CONVENIOS-TOMA-RAZON-01
#### Mermaid
flowchart TD
    A["Convenio<br/>firmado"] --> B{"Monto y<br/>naturaleza"}
    B -->|"Supera umbral<br/>CGR"| C["Requiere<br/>Toma de Razón"]
    B -->|"Bajo umbral"| D["Exento"]
    B -->|"Normativa<br/>específica"| E["Consultar<br/>Res. CGR"]

    style C fill:#f44336,color:#fff
    style D fill:#4CAF50,color:#fff


## Expediente Electronico Ley 21180
### ID
BPMN-GN-ACTOS-EXPEDIENTE-01
### Estructura Expediente
#### Mermaid
flowchart TD
    subgraph EXPEDIENTE["📁 Expediente Electrónico"]
        A["Metadatos:<br/>• ID único<br/>• Fecha creación<br/>• Tipo acto"]
        B["Documentos:<br/>• Borrador<br/>• Antecedentes<br/>• Visaciones"]
        C["Firmas:<br/>• FEA funcionarios<br/>• FEA autoridad"]
        D["Trazabilidad:<br/>• Log de acciones<br/>• Fechas/horas"]
    end

    A --> B --> C --> D

    style C fill:#2196F3,color:#fff

### Principios TDE
#### ID
BPMN-GN-ACTOS-TDE-PRINCIPIOS-01
#### Filas
| Principio | Aplicacion |
| --- | --- |
| Equivalencia funcional | Documento digital = papel |
| Neutralidad tecnológica | Sin dependencia de proveedor |
| Interoperabilidad | Comunicación entre sistemas |
| Seguridad | Integridad, autenticidad, no repudio |

## Sistemas Involucrados
### ID
BPMN-GN-ACTOS-SISTEMAS-01
### Filas
| Sistema | Funcion |
| --- | --- |
| SYS-DOCDIGITAL | Gestión documental, expediente |
| SYS-FIRMAGOB | Firma Electrónica Avanzada |
| SYS-SIGFE | Registro de compromisos |
| SYS-TRANSPARENCIA | Publicación |

## Normativa Aplicable
### ID
BPMN-GN-ACTOS-NORMATIVA-01
### Filas
| Norma | Alcance |
| --- | --- |
| Ley 19.880 LBPA | Procedimiento administrativo |
| Ley 21.180 TDE | Expediente electrónico |
| Ley 19.799 | Firma electrónica |
| Resolución 30/2015 CGR | Rendiciones |
| Ley 19.886 | Contratación pública |

## Referencias Cruzadas
### ID
BPMN-GN-ACTOS-REFERENCIAS-01
### Filas
| Dominio_Relacionado | Ctx_Optional | Vinculo |
| --- | --- | --- |
| D03 Gestión IPR | ['file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D03_gestion_ipr.md'] | Fase 4 Formalización |
| D02 Ciclo Presupuestario | ['file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D02_ciclo_presupuestario.md'] | Modificaciones, resoluciones |
| D08 Rendiciones | ['file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D08_rendiciones.md'] | Convenios de transferencia |

## Ultima Actualizacion
### ID
BPMN-GN-ACTOS-ULT-ACT-01
### Cpt
Última actualización: 2025-12-16
