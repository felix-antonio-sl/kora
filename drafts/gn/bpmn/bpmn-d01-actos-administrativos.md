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
    preserved_facts:
    - AI-Remediator=KODA-TRANSFORMER
    - Creation-Date=2025-12-22
    - 'Ctx=Especificación STS del dominio D01: Tramitación de Actos Administrativos
      del GORE Ñuble, modelado en BPMN.'
    - "Expediente_Electronico_Ley_21180.Estructura_Expediente.Mermaid=flowchart TD\n\
      \    subgraph EXPEDIENTE[\"\U0001F4C1 Expediente Electrónico\"]\n        A[\"\
      Metadatos:<br/>• ID único<br/>• Fecha creación<br/>• Tipo acto\"]\n        B[\"\
      Documentos:<br/>• Borrador<br/>• Antecedentes<br/>• Visaciones\"]\n        C[\"\
      Firmas:<br/>• FEA funcionarios<br/>• FEA autoridad\"]\n        D[\"Trazabilidad:<br/>•\
      \ Log de acciones<br/>• Fechas/horas\"]\n    end\n\n    A --> B --> C --> D\n\
      \n    style C fill:#2196F3,color:#fff\n"
    - Expediente_Electronico_Ley_21180.ID=BPMN-GN-ACTOS-EXPEDIENTE-01
    - Expediente_Electronico_Ley_21180.Principios_TDE.Filas[0].Aplicacion=Documento
      digital = papel
    - Expediente_Electronico_Ley_21180.Principios_TDE.Filas[0].Principio=Equivalencia
      funcional
    - Expediente_Electronico_Ley_21180.Principios_TDE.Filas[1].Aplicacion=Sin dependencia
      de proveedor
    - Expediente_Electronico_Ley_21180.Principios_TDE.Filas[1].Principio=Neutralidad
      tecnológica
    - Expediente_Electronico_Ley_21180.Principios_TDE.Filas[2].Aplicacion=Comunicación
      entre sistemas
    - Expediente_Electronico_Ley_21180.Principios_TDE.Filas[2].Principio=Interoperabilidad
    - Expediente_Electronico_Ley_21180.Principios_TDE.Filas[3].Aplicacion=Integridad,
      autenticidad, no repudio
    - Expediente_Electronico_Ley_21180.Principios_TDE.Filas[3].Principio=Seguridad
    - Expediente_Electronico_Ley_21180.Principios_TDE.ID=BPMN-GN-ACTOS-TDE-PRINCIPIOS-01
    - Format=KODA/Spec
    - Human-Creator=FS
    - Human-Editor=FS
    - ID=BPMN-GN-D01-ACTOS-ADMIN-KODA
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
    - Mapa_General_Dominio.Cpt=Mapa general de los procesos de actos administrativos
      (resoluciones exentas y convenios/transferencias) y elementos transversales.
    - Mapa_General_Dominio.ID=BPMN-GN-ACTOS-ADMIN-MAPA-01
    - "Mapa_General_Dominio.Mermaid=flowchart LR\n    subgraph PROCESOS[\"\U0001F4CB\
      \ Procesos de Actos Administrativos\"]\n        P1[\"P1: Resoluciones<br/>Exentas\"\
      ]\n        P2[\"P2: Convenios y<br/>Transferencias\"]\n    end\n\n    subgraph\
      \ TRANSVERSAL[\"\U0001F527 Elementos Transversales\"]\n        T1[\"Expediente<br/>Electrónico\"\
      ]\n        T2[\"Firma Electrónica<br/>Avanzada\"]\n        T3[\"Toma de Razón<br/>(cuando\
      \ aplica)\"]\n    end\n\n    P1 --> T1 & T2\n    P2 --> T1 & T2 & T3\n\n   \
      \ style P1 fill:#2196F3,color:#fff\n    style P2 fill:#4CAF50,color:#fff\n"
    - Metadatos_Dominio.Criticidad=🟠 Alta
    - Metadatos_Dominio.Dueno=Unidad Jurídica
    - Metadatos_Dominio.ID=DOM-ACTOS-ADMIN
    - Metadatos_Dominio.Procesos=2
    - Metadatos_Dominio.Ref_Fuente.Ctx_Required[0]=knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml
      L.100-499
    - Metadatos_Dominio.Subprocesos=~14 fases
    - Model-Collaborator[0]=Cascade
    - Modification-Date=2025-12-22
    - Normativa_Aplicable.Filas[0].Alcance=Procedimiento administrativo
    - Normativa_Aplicable.Filas[0].Norma=Ley 19.880 LBPA
    - Normativa_Aplicable.Filas[1].Alcance=Expediente electrónico
    - Normativa_Aplicable.Filas[1].Norma=Ley 21.180 TDE
    - Normativa_Aplicable.Filas[2].Alcance=Firma electrónica
    - Normativa_Aplicable.Filas[2].Norma=Ley 19.799
    - Normativa_Aplicable.Filas[3].Alcance=Rendiciones
    - Normativa_Aplicable.Filas[3].Norma=Resolución 30/2015 CGR
    - Normativa_Aplicable.Filas[4].Alcance=Contratación pública
    - Normativa_Aplicable.Filas[4].Norma=Ley 19.886
    - Normativa_Aplicable.ID=BPMN-GN-ACTOS-NORMATIVA-01
    - "P1_Flujo_Resoluciones_Exentas.Diagrama_de_Flujo_Completo.Mermaid=flowchart\
      \ TD\n    subgraph FASE1[\"1️⃣ Iniciación\"]\n        A[\"Área Requirente:<br/>Elaborar\
      \ borrador\"]\n        B[\"Adjuntar<br/>antecedentes\"]\n        C[\"Ingresar\
      \ al SGD\"]\n    end\n\n    subgraph FASE2[\"2️⃣ Revisión Jurídica\"]\n    \
      \    D[\"Jurídica recibe<br/>expediente\"]\n        E[\"Verificar legalidad<br/>y\
      \ forma\"]\n        F{\"¿OK?\"}\n        G[\"✅ V°B° Jurídico\"]\n        H[\"\
      ❌ Observar\"]\n    end\n\n    subgraph FASE3[\"3️⃣ Gestión\"]\n        I[\"\
      Centro Gestión:<br/>Asignar N° resolución\"]\n        J[\"Completar<br/>formalidades\"\
      ]\n    end\n\n    subgraph FASE4[\"4️⃣ Control\"]\n        K[\"Unidad Control:<br/>Verificar\
      \ procedencia\"]\n        L{\"¿Conforme?\"}\n        M[\"✅ V°B° Control\"]\n\
      \        N[\"❌ Reparar\"]\n    end\n\n    subgraph FASE5[\"5️⃣ V°B° Administrador/a\"\
      ]\n        O[\"Administrador/a Regional:<br/>Revisar y visar\"]\n    end\n\n\
      \    subgraph FASE6[\"6️⃣ Firma\"]\n        P[\"Gobernador/a:<br/>Firma con\
      \ FEA\"]\n    end\n\n    subgraph FASE7[\"7️⃣ Notificación y Archivo\"]\n  \
      \      Q[\"Oficina Partes:<br/>Numerar y fechar\"]\n        R[\"Notificar a<br/>interesados\"\
      ]\n        S[\"Publicar si<br/>corresponde\"]\n        T[\"Archivar expediente\"\
      ]\n    end\n\n    A --> B --> C --> D --> E --> F\n    F -->|\"Sí\"| G --> I\
      \ --> J --> K --> L\n    F -->|\"No\"| H --> A\n    L -->|\"Sí\"| M --> O -->\
      \ P --> Q --> R --> S --> T\n    L -->|\"No\"| N --> A\n\n    style P fill:#4CAF50,color:#fff\n\
      \    style T fill:#607D8B,color:#fff\n"
    - P1_Flujo_Resoluciones_Exentas.Fases=7
    - P1_Flujo_Resoluciones_Exentas.ID=BPMN-GN-RES-EXENTAS-FLUJO-01
    - P1_Flujo_Resoluciones_Exentas.Roles_por_Fase.Filas[0].Fase=Iniciación
    - P1_Flujo_Resoluciones_Exentas.Roles_por_Fase.Filas[0].Responsable=Área Requirente
    - P1_Flujo_Resoluciones_Exentas.Roles_por_Fase.Filas[1].Fase=Revisión Jurídica
    - P1_Flujo_Resoluciones_Exentas.Roles_por_Fase.Filas[1].Responsable=Unidad Jurídica
    - P1_Flujo_Resoluciones_Exentas.Roles_por_Fase.Filas[2].Fase=Gestión
    - P1_Flujo_Resoluciones_Exentas.Roles_por_Fase.Filas[2].Responsable=Centro de
      Gestión
    - P1_Flujo_Resoluciones_Exentas.Roles_por_Fase.Filas[3].Fase=Control
    - P1_Flujo_Resoluciones_Exentas.Roles_por_Fase.Filas[3].Responsable=Unidad de
      Control
    - P1_Flujo_Resoluciones_Exentas.Roles_por_Fase.Filas[4].Fase=V°B° Administrador/a
    - P1_Flujo_Resoluciones_Exentas.Roles_por_Fase.Filas[4].Responsable=Administrador/a
      Regional
    - P1_Flujo_Resoluciones_Exentas.Roles_por_Fase.Filas[5].Fase=Firma
    - P1_Flujo_Resoluciones_Exentas.Roles_por_Fase.Filas[5].Responsable=Gobernador/a
      Regional
    - P1_Flujo_Resoluciones_Exentas.Roles_por_Fase.Filas[6].Fase=Notificación y Archivo
    - P1_Flujo_Resoluciones_Exentas.Roles_por_Fase.Filas[6].Responsable=Oficina de
      Partes
    - P1_Flujo_Resoluciones_Exentas.Roles_por_Fase.ID=BPMN-GN-RES-EXENTAS-ROLES-01
    - P1_Flujo_Resoluciones_Exentas.SLA=15 días hábiles
    - P2_Convenios_y_Transferencias.Contenido_Minimo_Convenio.Filas[0].Descripcion=GORE
      + Entidad receptora
    - P2_Convenios_y_Transferencias.Contenido_Minimo_Convenio.Filas[0].Elemento=Partes
    - P2_Convenios_y_Transferencias.Contenido_Minimo_Convenio.Filas[1].Descripcion=Descripción
      del programa/proyecto
    - P2_Convenios_y_Transferencias.Contenido_Minimo_Convenio.Filas[1].Elemento=Objeto
    - P2_Convenios_y_Transferencias.Contenido_Minimo_Convenio.Filas[2].Descripcion=Valor
      total y calendario
    - P2_Convenios_y_Transferencias.Contenido_Minimo_Convenio.Filas[2].Elemento=Monto
    - P2_Convenios_y_Transferencias.Contenido_Minimo_Convenio.Filas[3].Descripcion=Duración
      y fechas clave
    - P2_Convenios_y_Transferencias.Contenido_Minimo_Convenio.Filas[3].Elemento=Plazos
    - P2_Convenios_y_Transferencias.Contenido_Minimo_Convenio.Filas[4].Descripcion=Deberes
      de cada parte
    - P2_Convenios_y_Transferencias.Contenido_Minimo_Convenio.Filas[4].Elemento=Obligaciones
    - P2_Convenios_y_Transferencias.Contenido_Minimo_Convenio.Filas[5].Descripcion=Modalidad,
      plazos, SISREC
    - P2_Convenios_y_Transferencias.Contenido_Minimo_Convenio.Filas[5].Elemento=Rendicion
    - P2_Convenios_y_Transferencias.Contenido_Minimo_Convenio.Filas[6].Descripcion=Condiciones
      de devolución
    - P2_Convenios_y_Transferencias.Contenido_Minimo_Convenio.Filas[6].Elemento=Restitucion
    - P2_Convenios_y_Transferencias.Contenido_Minimo_Convenio.Filas[7].Descripcion=Cláusulas
      anticorrupción
    - P2_Convenios_y_Transferencias.Contenido_Minimo_Convenio.Filas[7].Elemento=Probidad
    - P2_Convenios_y_Transferencias.Contenido_Minimo_Convenio.ID=BPMN-GN-CONVENIOS-CONTENIDO-01
    - P2_Convenios_y_Transferencias.Cpt=Proceso para la tramitación de convenios y
      transferencias asociadas a actos administrativos.
    - P2_Convenios_y_Transferencias.Criterios_Toma_de_Razon.ID=BPMN-GN-CONVENIOS-TOMA-RAZON-01
    - "P2_Convenios_y_Transferencias.Criterios_Toma_de_Razon.Mermaid=flowchart TD\n\
      \    A[\"Convenio<br/>firmado\"] --> B{\"Monto y<br/>naturaleza\"}\n    B -->|\"\
      Supera umbral<br/>CGR\"| C[\"Requiere<br/>Toma de Razón\"]\n    B -->|\"Bajo\
      \ umbral\"| D[\"Exento\"]\n    B -->|\"Normativa<br/>específica\"| E[\"Consultar<br/>Res.\
      \ CGR\"]\n\n    style C fill:#f44336,color:#fff\n    style D fill:#4CAF50,color:#fff\n"
    - "P2_Convenios_y_Transferencias.Diagrama_de_Flujo.Mermaid=flowchart TD\n    A[\"\
      Área requirente<br/>propone convenio\"] --> B[\"Elaborar borrador<br/>de convenio\"\
      ]\n    B --> C[\"Revisión Jurídica\"]\n    C --> D{\"¿Ajustes?\"}\n    D -->|\"\
      Sí\"| B\n    D -->|\"No\"| E[\"Resolución que<br/>aprueba convenio\"]\n    E\
      \ --> F[\"Toma de Razón<br/>si corresponde\"]\n    F --> G[\"Firma de partes\"\
      ]\n    G --> H[\"Ejecución y<br/>seguimiento\"]\n"
    - P2_Convenios_y_Transferencias.ID=BPMN-GN-CONVENIOS-TRANSFERENCIAS-01
    - Referencias_Cruzadas.Filas[0].Ctx_Optional[0]=file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D03_gestion_ipr.md
    - Referencias_Cruzadas.Filas[0].Dominio_Relacionado=D03 Gestión IPR
    - Referencias_Cruzadas.Filas[0].Vinculo=Fase 4 Formalización
    - Referencias_Cruzadas.Filas[1].Ctx_Optional[0]=file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D02_ciclo_presupuestario.md
    - Referencias_Cruzadas.Filas[1].Dominio_Relacionado=D02 Ciclo Presupuestario
    - Referencias_Cruzadas.Filas[1].Vinculo=Modificaciones, resoluciones
    - Referencias_Cruzadas.Filas[2].Ctx_Optional[0]=file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D08_rendiciones.md
    - Referencias_Cruzadas.Filas[2].Dominio_Relacionado=D08 Rendiciones
    - Referencias_Cruzadas.Filas[2].Vinculo=Convenios de transferencia
    - Referencias_Cruzadas.ID=BPMN-GN-ACTOS-REFERENCIAS-01
    - Sistemas_Involucrados.Filas[0].Funcion=Gestión documental, expediente
    - Sistemas_Involucrados.Filas[0].Sistema=SYS-DOCDIGITAL
    - Sistemas_Involucrados.Filas[1].Funcion=Firma Electrónica Avanzada
    - Sistemas_Involucrados.Filas[1].Sistema=SYS-FIRMAGOB
    - Sistemas_Involucrados.Filas[2].Funcion=Registro de compromisos
    - Sistemas_Involucrados.Filas[2].Sistema=SYS-SIGFE
    - Sistemas_Involucrados.Filas[3].Funcion=Publicación
    - Sistemas_Involucrados.Filas[3].Sistema=SYS-TRANSPARENCIA
    - Sistemas_Involucrados.ID=BPMN-GN-ACTOS-SISTEMAS-01
    - Source.Ctx_Required[0]=knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml
    - Source.Primary-Source=sources/gn/arquitectura/bpmn/D01_actos_administrativos.md
    - Status=Draft
    - 'Ultima_Actualizacion.Cpt=Última actualización: 2025-12-16'
    - Ultima_Actualizacion.ID=BPMN-GN-ACTOS-ULT-ACT-01
    - Version=1.0.0
    - _manifest.compatibility.breaking_changes_from=null
    - _manifest.compatibility.min_consumer_version=1.0.0
    - _manifest.dependencies.requires[0].reason=KODA/Spec format compliance
    - _manifest.dependencies.requires[0].urn=urn:knowledge:koda:core:spec:1.0.0
    - _manifest.dependencies.requires[1].reason=Transformation methodology reference
    - _manifest.dependencies.requires[1].urn=urn:knowledge:koda:core:transform:1.0.0
    - _manifest.dependencies.requires[2].reason=Marco integrado de procesos BPMN y
      arquitectura C4
    - _manifest.dependencies.requires[2].urn=urn:knowledge:gorenuble:gn:bpmn-c4:1.0.0
    - _manifest.federation.license=Institutional Use
    - _manifest.federation.visibility=internal
    - _manifest.provenance.created_at=2025-12-22
    - _manifest.provenance.created_by=FS
    - _manifest.provenance.last_modified_at=2025-12-22
    - _manifest.provenance.model_collaborators[0]=Cascade
    - _manifest.provenance.model_collaborators[1]=KODA-TRANSFORMER
    - _manifest.resolution.canonical_url=file://knowledge/domains/gn/arquitectura/bpmn/D01_actos_administrativos_koda.yml
    - _manifest.urn=urn:knowledge:gorenuble:gn:bpmn-d01-actos-administrativos:1.0.0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
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
