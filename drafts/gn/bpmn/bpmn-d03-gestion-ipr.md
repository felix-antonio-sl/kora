---
_manifest:
  urn: urn:gn:kb:bpmn-d03-gestion-ipr
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/04_habilitadores/arquitectura/bpmn/D03_gestion_ipr_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- bpmn
- ipr
- gestion-publica
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/04_habilitadores/arquitectura/bpmn/D03_gestion_ipr_koda.yml
    source_hashes:
      domains/gn/04_habilitadores/arquitectura/bpmn/D03_gestion_ipr_koda.yml: ad228323fcd3053399a1bea70e24f3a0d3ffdc1da1a6f46050562a2bbc463a88
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.24
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 28
    meat_count: 182
    fat_count: 0
    preserved_facts:
    - AI-Remediator=KODA-TRANSFORMER
    - Creation-Date=2025-12-22
    - 'Ctx=Especificación STS del dominio D03: Gestión de Intervenciones Públicas
      Regionales (IPR) del GORE Ñuble, modelado en BPMN.'
    - Format=KODA/Spec
    - Human-Creator=FS
    - Human-Editor=FS
    - ID=BPMN-GN-D03-GESTION-IPR-KODA
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
    - Mapa_General_Dominio.Cpt=Mapa general del ciclo de vida de las Intervenciones
      Públicas Regionales (IPR), incluyendo pre-fase y fases P1–P7.
    - Mapa_General_Dominio.ID=BPMN-GN-IPR-MAPA-01
    - "Mapa_General_Dominio.Mermaid=flowchart LR\n    subgraph PREFASE[\"\U0001F3AF\
      \ Pre-Fase\"]\n        P0[\"P0: Selector<br/>de Vías\"]\n    end\n\n    subgraph\
      \ CICLO_VIDA[\"\U0001F4CB Ciclo de Vida IPR\"]\n        P1[\"P1: Ingreso y<br/>Admisibilidad\"\
      ]\n        P2[\"P2: Evaluación<br/>Técnico-Económica\"]\n        P3[\"P3: Obtención\
      \ de<br/>Financiamiento\"]\n        P4[\"P4: Formalización\"]\n        P5[\"\
      P5: Ejecución y<br/>Supervisión\"]\n        P6[\"P6: Modificaciones<br/>en Ejecución\"\
      ]\n        P7[\"P7: Cierre y<br/>Evaluación Ex Post\"]\n    end\n\n    P0 -->\
      \ P1 --> P2 --> P3 --> P4 --> P5 --> P7\n    P5 <--> P6\n\n    style P0 fill:#FF9800,color:#fff\n\
      \    style P1 fill:#2196F3,color:#fff\n    style P2 fill:#9C27B0,color:#fff\n\
      \    style P3 fill:#4CAF50,color:#fff\n    style P4 fill:#00BCD4,color:#fff\n\
      \    style P5 fill:#E91E63,color:#fff\n    style P6 fill:#FFC107,color:#000\n\
      \    style P7 fill:#607D8B,color:#fff\n"
    - Metadatos_Dominio.Criticidad=🔴 Crítica
    - Metadatos_Dominio.Dueno=Jefatura DIPIR
    - Metadatos_Dominio.ID=DOM-IPR
    - Metadatos_Dominio.Procesos=9
    - Metadatos_Dominio.Ref_Fuente.Ctx_Required[0]=knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml
      L.1888-3727
    - Metadatos_Dominio.Subprocesos=~25
    - Model-Collaborator[0]=Cascade
    - Modification-Date=2025-12-22
    - Normativa_Aplicable.Filas[0].Alcance=Competencias GORE
    - Normativa_Aplicable.Filas[0].Norma=LOC 19.175
    - Normativa_Aplicable.Filas[1].Alcance=Glosa 06, 14, 16
    - Normativa_Aplicable.Filas[1].Norma=Ley de Presupuestos
    - Normativa_Aplicable.Filas[2].Alcance=Track C
    - Normativa_Aplicable.Filas[2].Norma=Instructivo SUBDERE FRIL
    - Normativa_Aplicable.Filas[3].Alcance=Track C
    - Normativa_Aplicable.Filas[3].Norma=Circular 33 MDSF
    - Normativa_Aplicable.Filas[4].Alcance=Rendiciones
    - Normativa_Aplicable.Filas[4].Norma=Resolución 30/2015 CGR
    - Normativa_Aplicable.Filas[5].Alcance=Track A
    - Normativa_Aplicable.Filas[5].Norma=Normas SNI/MDSF
    - Normativa_Aplicable.ID=BPMN-GN-IPR-NORMATIVA-01
    - "P0_Selector_de_Vias_de_Financiamiento_IPR.Diagrama_de_Flujo.Mermaid=flowchart\
      \ TD\n    A[(\"Iniciativa<br/>Identificada\")] --> B{\"¿Propósito<br/>Principal?\"\
      }\n\n    B -->|\"Activo Durable\"| C[\"\U0001F3D7️ PROYECTO\"]\n    B -->|\"\
      Servicio/Prestación\"| D[\"\U0001F4CA PROGRAMA\"]\n\n    C --> E{\"Evaluar<br/>Criterios\"\
      }\n    E -->|\"Municipio + <5.000 UTM\"| F[\"\U0001F3D8️ FRIL\"]\n    E -->|\"\
      Conservación/ANF/Estudio\"| G[\"\U0001F4DC Circular 33\"]\n    E -->|\"Foco\
      \ productivo\"| H[\"\U0001F680 FRPD\"]\n    E -->|\"Default\"| I[\"\U0001F4D0\
      \ SNI General\"]\n\n    D --> J{\"Tipo<br/>Ejecutor\"}\n    J -->|\"Privado\
      \ sin fines lucro\"| K[\"\U0001F381 8% FNDR\"]\n    J -->|\"GORE\"| L[\"\U0001F4CB\
      \ Glosa 06\"]\n    J -->|\"Entidad Pública\"| M[\"\U0001F504 Transferencia\"\
      ]\n    J -->|\"Foco productivo\"| N[\"\U0001F680 FRPD\"]\n\n    style A fill:#4CAF50,color:#fff\n\
      \    style F fill:#FF9800,color:#fff\n    style G fill:#9C27B0,color:#fff\n\
      \    style H fill:#E91E63,color:#fff\n    style I fill:#607D8B,color:#fff\n"
    - P0_Selector_de_Vias_de_Financiamiento_IPR.ID=BPMN-GN-IPR-SELECTOR-00
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[0].Condicion_Clave=Infraestructura
      menor
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[0].Ejecutor=Municipalidad
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[0].Monto=< 5.000
      UTM
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[0].Tipo=Proyecto
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[0].Via=FRIL
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[1].Condicion_Clave=Conservación,
      ANF, estudios
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[1].Ejecutor=Variable
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[1].Monto=Variable
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[1].Tipo=Proyecto
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[1].Via=Circular
      33
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[2].Condicion_Clave=Foco
      productivo/innovación
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[2].Ejecutor=Habilitado
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[2].Monto=Variable
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[2].Tipo=Ambos
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[2].Via=FRPD
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[3].Condicion_Clave=Default
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[3].Ejecutor=Variable
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[3].Monto=Variable
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[3].Tipo=Proyecto
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[3].Via=SNI General
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[4].Condicion_Clave=Concurso
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[4].Ejecutor=Privado
      s/f lucro
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[4].Monto=Variable
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[4].Tipo=Actividad
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[4].Via=8% FNDR
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[5].Condicion_Clave=Ejecución
      directa
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[5].Ejecutor=GORE
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[5].Monto=Variable
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[5].Tipo=Programa
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[5].Via=Glosa
      06
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[6].Condicion_Clave=ITF
      interno
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[6].Ejecutor=Entidad
      pública
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[6].Monto=Variable
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[6].Tipo=Programa
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.Filas[6].Via=Transferencia
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Matriz_Decision.ID=BPMN-GN-IPR-SELECTOR-MATRIZ-01
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Objetivo=Orientar selección de vía
      antes de formulación
    - P0_Selector_de_Vias_de_Financiamiento_IPR.Tipo=Pre-Fase (Decisión Estratégica)
    - "P1_Ingreso_Pertinencia_y_Admisibilidad.Diagrama_de_Flujo.Mermaid=flowchart\
      \ TD\n    subgraph EE[\"\U0001F3E2 Entidad Externa\"]\n        A[\"\U0001F4C4\
      \ Postulación<br/>preparada\"]\n    end\n\n    subgraph GORE[\"\U0001F3DB️ GORE\
      \ Ñuble\"]\n        B[\"\U0001F4EC Oficina Partes:<br/>Recepcionar y registrar\"\
      ]\n        C[\"\U0001F4CA DIPIR:<br/>Registrar en sistema\"]\n        D[\"\U0001F465\
      \ CDR:<br/>Evaluar pertinencia\"]\n        E{\"¿Pre-admisible?\"}\n        F[\"\
      ✅ PRE-ADMISIBLE\"]\n        G[\"❌ NO PRE-ADMISIBLE\"]\n        H[\"\U0001F50D\
      \ Analista:<br/>Revisión documental\"]\n        I{\"Estado<br/>admisibilidad\"\
      }\n        J[\"✅ ADMISIBLE\"]\n        K[\"⚠️ CON OBSERVACIONES\"]\n       \
      \ L[\"❌ INADMISIBLE\"]\n    end\n\n    subgraph SUBSANACION[\"\U0001F504 Subsanación\"\
      ]\n        M[\"Corregir en plazo\"]\n        N{\"¿OK?\"}\n    end\n\n    A -->\
      \ B --> C --> D --> E\n    E -->|\"Sí\"| F --> H --> I\n    E -->|\"No\"| G\n\
      \    I -->|\"OK\"| J\n    I -->|\"Observa\"| K --> M --> N\n    I -->|\"Rechaza\"\
      | L\n    N -->|\"Sí\"| J\n    N -->|\"No\"| L\n\n    style J fill:#4CAF50,color:#fff\n\
      \    style L fill:#f44336,color:#fff\n"
    - P1_Ingreso_Pertinencia_y_Admisibilidad.ID=BPMN-GN-IPR-FASE1-01
    - P1_Ingreso_Pertinencia_y_Admisibilidad.Roles_Involucrados.Filas[0].Responsabilidad=Recepcionar,
      registrar, derivar
    - P1_Ingreso_Pertinencia_y_Admisibilidad.Roles_Involucrados.Filas[0].Rol=Oficina
      de Partes
    - P1_Ingreso_Pertinencia_y_Admisibilidad.Roles_Involucrados.Filas[1].Responsabilidad=Registrar,
      convocar CDR
    - P1_Ingreso_Pertinencia_y_Admisibilidad.Roles_Involucrados.Filas[1].Rol=Jefatura
      DIPIR
    - P1_Ingreso_Pertinencia_y_Admisibilidad.Roles_Involucrados.Filas[2].Responsabilidad=Evaluar
      pertinencia estratégica
    - P1_Ingreso_Pertinencia_y_Admisibilidad.Roles_Involucrados.Filas[2].Rol=CDR
    - P1_Ingreso_Pertinencia_y_Admisibilidad.Roles_Involucrados.Filas[3].Responsabilidad=Revisión
      documental exhaustiva
    - P1_Ingreso_Pertinencia_y_Admisibilidad.Roles_Involucrados.Filas[3].Rol=Analista
      Preinversión
    - P1_Ingreso_Pertinencia_y_Admisibilidad.Subprocesos[0]=Recepción
    - P1_Ingreso_Pertinencia_y_Admisibilidad.Subprocesos[1]=CDR
    - P1_Ingreso_Pertinencia_y_Admisibilidad.Subprocesos[2]=Admisibilidad Documental
    - "P2_Evaluacion_Tecnico_Economica.Diagrama_de_Tracks.Mermaid=flowchart TD\n \
      \   A[\"IPR Admisible\"] --> B{\"Tipo de<br/>Iniciativa\"}\n\n    B -->|\"Proyecto\
      \ IDI\"| C[\"Track A:<br/>SNI/MDSF\"]\n    B -->|\"Programa GORE\"| D[\"Track\
      \ B:<br/>Glosa 06/DIPRES\"]\n    B -->|\"FRIL/FRPD/C33/8%\"| E[\"Track C:<br/>Vías\
      \ Simplificadas\"]\n    B -->|\"Transf. a Entidad Pública\"| F[\"Track D:<br/>ITF\
      \ Interno\"]\n\n    subgraph TRACK_A[\"Track A: SNI\"]\n        C --> C1[\"\
      Revisión RIS\"]\n        C1 --> C2[\"Envío a MDSF\"]\n        C2 --> C3[\"RATE:\
      \ RS/FI/OT\"]\n    end\n\n    subgraph TRACK_B[\"Track B: Glosa 06\"]\n    \
      \    D --> D1[\"Perfil MML\"]\n        D1 --> D2[\"Diseño MML\"]\n        D2\
      \ --> D3[\"DIPRES/SES evalúa\"]\n        D3 --> D4[\"RF/FI/OT\"]\n    end\n\n\
      \    subgraph TRACK_C[\"Track C: Simplificadas\"]\n        E --> E1[\"Requisitos\
      \ específicos\"]\n        E1 --> E2[\"Evaluación GORE\"]\n        E2 --> E3[\"\
      RS/FI/OT\"]\n    end\n\n    subgraph TRACK_D[\"Track D: Transferencias\"]\n\
      \        F --> F1[\"Postulación GESDOC\"]\n        F1 --> F2[\"Admisibilidad\
      \ DAE\"]\n        F2 --> F3[\"Eval. MML\"]\n        F3 --> F4[\"ITF Interno\"\
      ]\n    end\n\n    style C3 fill:#4CAF50,color:#fff\n    style D4 fill:#4CAF50,color:#fff\n\
      \    style E3 fill:#4CAF50,color:#fff\n    style F4 fill:#4CAF50,color:#fff\n"
    - P2_Evaluacion_Tecnico_Economica.ID=BPMN-GN-IPR-FASE2-01
    - "P2_Evaluacion_Tecnico_Economica.Track_A_SNI_MDSF.Mermaid=flowchart LR\n   \
      \ A[\"Revisión<br/>interna GORE\"] --> B[\"Verificar<br/>RIS aplicable\"]\n\
      \    B --> C[\"Cargar en<br/>BIP/Carpeta Digital\"]\n    C --> D[\"Oficio a\
      \ MDSF\"]\n    D --> E[\"MDSF evalúa<br/>(5+10 días)\"]\n    E --> F{\"RATE\"\
      }\n    F -->|\"RS\"| G[\"✅ Aprobado\"]\n    F -->|\"FI\"| H[\"Subsanar<br/>(60\
      \ días)\"]\n    F -->|\"OT\"| I[\"❌ Rechazado\"]\n    H --> E\n\n    style G\
      \ fill:#4CAF50,color:#fff\n    style I fill:#f44336,color:#fff\n"
    - "P2_Evaluacion_Tecnico_Economica.Track_C_Vias_Simplificadas.Mermaid=flowchart\
      \ TD\n    subgraph FRIL[\"FRIL\"]\n        F1[\"Postular<br/>GESDOC+BIP\"]\n\
      \        F2[\"Admisibilidad\"]\n        F3[\"Evaluación<br/>técnica\"]\n   \
      \     F4[\"RS (60 días)\"]\n        F1 --> F2 --> F3 --> F4\n    end\n\n   \
      \ subgraph FRPD[\"FRPD\"]\n        R1[\"Postular<br/>formulario online\"]\n\
      \        R2[\"Adm.<br/>Administrativa\"]\n        R3[\"Adm.<br/>Técnica/Ranking\"\
      ]\n        R4[\"Evaluación<br/>GORE\"]\n        R5[\"RS\"]\n        R1 --> R2\
      \ --> R3 --> R4 --> R5\n    end\n\n    subgraph C33[\"Circular 33\"]\n     \
      \   C1[\"Postular<br/>GESDOC+BIP\"]\n        C2[\"Admisibilidad\"]\n       \
      \ C3[\"Revisión<br/>técnica\"]\n        C4[\"RS/FI/OT\"]\n        C1 --> C2\
      \ --> C3 --> C4\n    end\n"
    - P2_Evaluacion_Tecnico_Economica.Tracks[0]=A (SNI)
    - P2_Evaluacion_Tecnico_Economica.Tracks[1]=B (Glosa 06)
    - P2_Evaluacion_Tecnico_Economica.Tracks[2]=C (Simplificadas)
    - P2_Evaluacion_Tecnico_Economica.Tracks[3]=D (Transferencias)
    - P3_Obtencion_de_Financiamiento.Criterios_para_Acuerdo_CORE.Filas[0].Condicion=Monto
      > 7.000 UTM
    - P3_Obtencion_de_Financiamiento.Criterios_para_Acuerdo_CORE.Filas[0].Requiere_CORE=✅
      Sí
    - P3_Obtencion_de_Financiamiento.Criterios_para_Acuerdo_CORE.Filas[1].Condicion=Nuevo
      programa/proyecto
    - P3_Obtencion_de_Financiamiento.Criterios_para_Acuerdo_CORE.Filas[1].Requiere_CORE=✅
      Sí
    - P3_Obtencion_de_Financiamiento.Criterios_para_Acuerdo_CORE.Filas[2].Condicion=Aumento
      costo <= 10% (tope 7.000 UTM)
    - P3_Obtencion_de_Financiamiento.Criterios_para_Acuerdo_CORE.Filas[2].Requiere_CORE=❌
      No
    - P3_Obtencion_de_Financiamiento.Criterios_para_Acuerdo_CORE.Filas[3].Condicion=Uso
      3% emergencia (Glosa 14)
    - P3_Obtencion_de_Financiamiento.Criterios_para_Acuerdo_CORE.Filas[3].Requiere_CORE=❌
      No
    - P3_Obtencion_de_Financiamiento.Criterios_para_Acuerdo_CORE.Filas[4].Condicion=Regularización
      de ingresos
    - P3_Obtencion_de_Financiamiento.Criterios_para_Acuerdo_CORE.Filas[4].Requiere_CORE=❌
      No
    - "P3_Obtencion_de_Financiamiento.Diagrama_de_Flujo.Mermaid=flowchart TD\n   \
      \ A[\"IPR con RS/RF\"] --> B{\"¿Requiere<br/>Acuerdo CORE?\"}\n\n    subgraph\
      \ RUTA_A[\"Ruta A: Sin CORE\"]\n        C[\"Solicitar CDP\"]\n        D[\"DAF\
      \ emite CDP\"]\n        E[\"Instrucción a<br/>Depto. Presupuesto\"]\n    end\n\
      \n    subgraph RUTA_B[\"Ruta B: Con CORE\"]\n        F[\"Preparar carpeta<br/>CORE\"\
      ]\n        G[\"Envío formal<br/>al CORE\"]\n        H[\"Votación CORE\"]\n \
      \       I{\"¿Aprobado?\"}\n        J[\"Certificado<br/>Acuerdo CORE\"]\n   \
      \     K[\"Solicitar creación<br/>presupuestaria\"]\n    end\n\n    B -->|\"\
      No\"| C --> D --> E\n    B -->|\"Sí\"| F --> G --> H --> I\n    I -->|\"✅\"\
      | J --> K\n    I -->|\"❌\"| L[\"Rechazado\"]\n\n    style E fill:#4CAF50,color:#fff\n\
      \    style K fill:#4CAF50,color:#fff\n    style L fill:#f44336,color:#fff\n"
    - P3_Obtencion_de_Financiamiento.ID=BPMN-GN-IPR-FASE3-01
    - P3_Obtencion_de_Financiamiento.Rutas[0]=A (Sin CORE)
    - P3_Obtencion_de_Financiamiento.Rutas[1]=B (Con CORE)
    - "P4_Formalizacion.Diagrama_de_Flujo.Mermaid=flowchart TD\n    A[\"Financiamiento<br/>aprobado\"\
      ] --> B{\"Tipo de<br/>modificación\"}\n\n    B -->|\"Interna\"| C[\"Resolución\
      \ GORE\"]\n    B -->|\"Afecta Partida 31\"| D[\"Solicitud a DIPRES\"]\n\n  \
      \  C & D --> E[\"Visaciones internas<br/>(DAF, DIPIR, Jurídica)\"]\n    E -->\
      \ F[\"Firma Gobernador/a\"]\n    F --> G[\"Control externo<br/>(DIPRES/CGR)\"\
      ]\n    G --> H[\"Elaborar Convenio<br/>de Transferencia\"]\n    H --> I[\"Revisión\
      \ Jurídica\"]\n    I --> J[\"Firma GORE +<br/>Entidad Receptora\"]\n    J -->\
      \ K[\"Resolución aprobatoria\"]\n    K --> L[\"Programar<br/>transferencias\"\
      ]\n\n    style L fill:#4CAF50,color:#fff\n"
    - P4_Formalizacion.ID=BPMN-GN-IPR-FASE4-01
    - P4_Formalizacion.Regla_de_Devengo.Filas[0].Momento_Devengo=Convenio tramitado
    - P4_Formalizacion.Regla_de_Devengo.Filas[0].Tipo_Receptor=Privados y Municipios
    - P4_Formalizacion.Regla_de_Devengo.Filas[1].Momento_Devengo=Al aprobar rendición
    - P4_Formalizacion.Regla_de_Devengo.Filas[1].Tipo_Receptor=Servicios Públicos
    - P4_Formalizacion.Subprocesos[0]=Actos
    - P4_Formalizacion.Subprocesos[1]=Convenio
    - P4_Formalizacion.Subprocesos[2]=Devengo
    - "P5_Ejecucion_y_Supervision.Diagrama_de_Flujo.Mermaid=flowchart TD\n    subgraph\
      \ INICIO[\"\U0001F680 Inicio\"]\n        A[\"Chequeo documentación<br/>técnica\"\
      ]\n        B[\"Reunión coordinación<br/>GORE-UT\"]\n        C[\"Carpeta de<br/>seguimiento\"\
      ]\n    end\n\n    subgraph LICITACION[\"\U0001F4CB Licitación (si aplica)\"\
      ]\n        D[\"Bases y publicación<br/>Mercado Público\"]\n        E[\"Adjudicación\"\
      ]\n        F[\"Contrato\"]\n        G[\"Entrega terreno/<br/>Orden inicio\"\
      ]\n    end\n\n    subgraph SEGUIMIENTO[\"\U0001F4CA Seguimiento\"]\n       \
      \ H[\"Visitas a terreno\"]\n        I[\"Revisión informes<br/>avance\"]\n  \
      \      J[\"Estados de Pago\"]\n        K[\"Actualizar BIP\"]\n        L[\"Monitoreo\
      \ financiero<br/>SIGFE\"]\n        M[\"Comité seguimiento\"]\n    end\n\n  \
      \  A --> B --> C --> D --> E --> F --> G\n    G --> H --> I --> J --> K\n  \
      \  L --> M\n\n    style K fill:#4CAF50,color:#fff\n"
    - P5_Ejecucion_y_Supervision.Hitos_de_Control.Filas[0].Hito=Inicio de obra
    - P5_Ejecucion_y_Supervision.Hitos_de_Control.Filas[0].Responsable=UT / ITO
    - P5_Ejecucion_y_Supervision.Hitos_de_Control.Filas[1].Hito=Avances periódicos
    - P5_Ejecucion_y_Supervision.Hitos_de_Control.Filas[1].Responsable=Supervisor
      GORE
    - P5_Ejecucion_y_Supervision.Hitos_de_Control.Filas[2].Hito=Recepción provisoria
    - P5_Ejecucion_y_Supervision.Hitos_de_Control.Filas[2].Responsable=UT
    - P5_Ejecucion_y_Supervision.Hitos_de_Control.Filas[3].Hito=Recepción definitiva
    - P5_Ejecucion_y_Supervision.Hitos_de_Control.Filas[3].Responsable=UT
    - P5_Ejecucion_y_Supervision.ID=BPMN-GN-IPR-FASE5-01
    - P5_Ejecucion_y_Supervision.Subprocesos[0]=Inicio
    - P5_Ejecucion_y_Supervision.Subprocesos[1]=Licitación
    - P5_Ejecucion_y_Supervision.Subprocesos[2]=Seguimiento
    - "P6_Modificaciones_en_Ejecucion.Diagrama_de_Flujo.Mermaid=flowchart TD\n   \
      \ A[\"Detectar necesidad<br/>de modificación\"] --> B[\"UT prepara<br/>informe\
      \ técnico\"]\n    B --> C[\"Oficio formal<br/>al GORE\"]\n    C --> D[\"Supervisor\
      \ GORE<br/>analiza\"]\n    D --> E{\"¿Altera<br/>objetivo?\"}\n    E -->|\"\
      Sí\"| F[\"❌ Rechazar\"]\n    E -->|\"No\"| G[\"Verificar<br/>umbrales\"]\n \
      \   G --> H{\"¿Requiere<br/>CORE/SNI?\"}\n    H -->|\"Sí\"| I[\"Tramitar como<br/>nueva\
      \ aprobación\"]\n    H -->|\"No\"| J[\"Aprobar<br/>internamente\"]\n    I &\
      \ J --> K[\"Convenio<br/>modificatorio\"]\n\n    style F fill:#f44336,color:#fff\n\
      \    style K fill:#4CAF50,color:#fff\n"
    - P6_Modificaciones_en_Ejecucion.ID=BPMN-GN-IPR-FASE6-01
    - P6_Modificaciones_en_Ejecucion.Subprocesos[0]=Solicitud
    - P6_Modificaciones_en_Ejecucion.Subprocesos[1]=Evaluación
    - P6_Modificaciones_en_Ejecucion.Subprocesos[2]=Tramitación
    - "P7_Cierre_Tecnico_Financiero_y_Evaluacion_Ex_Post.Diagrama_de_Flujo.Mermaid=flowchart\
      \ TD\n    subgraph CIERRE_TEC[\"\U0001F4CB Cierre Técnico\"]\n        A[\"Recepción\
      \ provisoria\"]\n        B[\"Período garantía\"]\n        C[\"Recepción definitiva\"\
      ]\n        D[\"Informe final<br/>técnico\"]\n    end\n\n    subgraph CIERRE_FIN[\"\
      \U0001F4B0 Cierre Financiero\"]\n        E[\"Rendición final<br/>SISREC\"]\n\
      \        F[\"Revisión DAF\"]\n        G{\"¿Saldos?\"}\n        H[\"Reintegro\"\
      ]\n        I[\"Resolución cierre<br/>convenio\"]\n        J[\"Devolución<br/>garantías\"\
      ]\n    end\n\n    subgraph EXPOST[\"\U0001F4CA Evaluación Ex Post\"]\n     \
      \   K[\"Selección muestra\"]\n        L[\"Estudio evaluativo\"]\n        M[\"\
      Lecciones aprendidas\"]\n    end\n\n    A --> B --> C --> D\n    D --> E -->\
      \ F --> G\n    G -->|\"Sí\"| H --> I\n    G -->|\"No\"| I\n    I --> J --> K\
      \ --> L --> M\n\n    style M fill:#9C27B0,color:#fff\n"
    - P7_Cierre_Tecnico_Financiero_y_Evaluacion_Ex_Post.ID=BPMN-GN-IPR-FASE7-01
    - P7_Cierre_Tecnico_Financiero_y_Evaluacion_Ex_Post.Subprocesos[0]=Cierre Técnico
    - P7_Cierre_Tecnico_Financiero_y_Evaluacion_Ex_Post.Subprocesos[1]=Cierre Financiero
    - P7_Cierre_Tecnico_Financiero_y_Evaluacion_Ex_Post.Subprocesos[2]=Evaluación
      Ex Post
    - Referencias_Cruzadas.Filas[0].Ctx_Optional[0]=file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D02_ciclo_presupuestario.md
    - Referencias_Cruzadas.Filas[0].Dominio_Relacionado=D02 Ciclo Presupuestario
    - Referencias_Cruzadas.Filas[0].Vinculo=CDP, modificaciones, SIGFE
    - Referencias_Cruzadas.Filas[1].Ctx_Optional[0]=file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D08_rendiciones.md
    - Referencias_Cruzadas.Filas[1].Dominio_Relacionado=D08 Rendiciones
    - Referencias_Cruzadas.Filas[1].Vinculo=Cierre financiero, SISREC
    - Referencias_Cruzadas.Filas[2].Ctx_Optional[0]=file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D01_actos_administrativos.md
    - Referencias_Cruzadas.Filas[2].Dominio_Relacionado=D01 Actos Administrativos
    - Referencias_Cruzadas.Filas[2].Vinculo=Resoluciones, Convenios
    - Referencias_Cruzadas.ID=BPMN-GN-IPR-REFERENCIAS-01
    - Sistemas_Involucrados.Filas[0].Fases_de_Uso=P1, P2, P5, P7
    - Sistemas_Involucrados.Filas[0].Sistema=SYS-BIP-SNI
    - Sistemas_Involucrados.Filas[1].Fases_de_Uso=P1, P2
    - Sistemas_Involucrados.Filas[1].Sistema=SYS-GESDOC
    - Sistemas_Involucrados.Filas[2].Fases_de_Uso=P3, P4, P5, P7
    - Sistemas_Involucrados.Filas[2].Sistema=SYS-SIGFE
    - Sistemas_Involucrados.Filas[3].Fases_de_Uso=P7
    - Sistemas_Involucrados.Filas[3].Sistema=SYS-SISREC
    - Sistemas_Involucrados.ID=BPMN-GN-IPR-SISTEMAS-01
    - Source.Ctx_Required[0]=knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml
    - Source.Primary-Source=sources/gn/arquitectura/bpmn/D03_gestion_ipr.md
    - Status=Draft
    - 'Ultima_Actualizacion.Cpt=Última actualización: 2025-12-16'
    - Ultima_Actualizacion.ID=BPMN-GN-IPR-ULT-ACT-01
    - Version=1.0.0
    - _manifest.compatibility.breaking_changes_from=null
    - _manifest.compatibility.min_consumer_version=1.0.0
    - _manifest.dependencies.requires[0].reason=KODA/Spec format compliance
    - _manifest.dependencies.requires[0].urn=urn:knowledge:koda:core:spec:1.0.0
    - _manifest.dependencies.requires[1].reason=Transformation methodology reference
    - _manifest.dependencies.requires[1].urn=urn:knowledge:koda:core:transform:1.0.0
    - _manifest.federation.license=Institutional Use
    - _manifest.federation.visibility=internal
    - _manifest.provenance.created_at=2025-12-22
    - _manifest.provenance.created_by=FS
    - _manifest.provenance.last_modified_at=2025-12-22
    - _manifest.provenance.model_collaborators[0]=Cascade
    - _manifest.provenance.model_collaborators[1]=KODA-TRANSFORMER
    - _manifest.resolution.canonical_url=file://knowledge/domains/gn/arquitectura/bpmn/D03_gestion_ipr_koda.yml
    - _manifest.urn=urn:knowledge:gorenuble:gn:bpmn-d03-gestion-ipr:1.0.0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
---

# BPMN D03: Gestión de Intervenciones Públicas Regionales (IPR)
## ID
BPMN-GN-D03-GESTION-IPR-KODA

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
Especificación STS del dominio D03: Gestión de Intervenciones Públicas Regionales (IPR) del GORE Ñuble, modelado en BPMN.

## Source
### Ctx Required
- knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml
### Primary Source
sources/gn/arquitectura/bpmn/D03_gestion_ipr.md

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
DOM-IPR
### Criticidad
🔴 Crítica
### Dueno
Jefatura DIPIR
### Procesos
9
### Subprocesos
~25
### Ref Fuente
#### Ctx Required
- knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml L.1888-3727

## Mapa General Dominio
### ID
BPMN-GN-IPR-MAPA-01
### Cpt
Mapa general del ciclo de vida de las Intervenciones Públicas Regionales (IPR), incluyendo pre-fase y fases P1–P7.
### Mermaid
flowchart LR
    subgraph PREFASE["🎯 Pre-Fase"]
        P0["P0: Selector<br/>de Vías"]
    end

    subgraph CICLO_VIDA["📋 Ciclo de Vida IPR"]
        P1["P1: Ingreso y<br/>Admisibilidad"]
        P2["P2: Evaluación<br/>Técnico-Económica"]
        P3["P3: Obtención de<br/>Financiamiento"]
        P4["P4: Formalización"]
        P5["P5: Ejecución y<br/>Supervisión"]
        P6["P6: Modificaciones<br/>en Ejecución"]
        P7["P7: Cierre y<br/>Evaluación Ex Post"]
    end

    P0 --> P1 --> P2 --> P3 --> P4 --> P5 --> P7
    P5 <--> P6

    style P0 fill:#FF9800,color:#fff
    style P1 fill:#2196F3,color:#fff
    style P2 fill:#9C27B0,color:#fff
    style P3 fill:#4CAF50,color:#fff
    style P4 fill:#00BCD4,color:#fff
    style P5 fill:#E91E63,color:#fff
    style P6 fill:#FFC107,color:#000
    style P7 fill:#607D8B,color:#fff


## P0 Selector de Vias de Financiamiento IPR
### ID
BPMN-GN-IPR-SELECTOR-00
### Tipo
Pre-Fase (Decisión Estratégica)
### Objetivo
Orientar selección de vía antes de formulación
### Diagrama de Flujo
#### Mermaid
flowchart TD
    A[("Iniciativa<br/>Identificada")] --> B{"¿Propósito<br/>Principal?"}

    B -->|"Activo Durable"| C["🏗️ PROYECTO"]
    B -->|"Servicio/Prestación"| D["📊 PROGRAMA"]

    C --> E{"Evaluar<br/>Criterios"}
    E -->|"Municipio + <5.000 UTM"| F["🏘️ FRIL"]
    E -->|"Conservación/ANF/Estudio"| G["📜 Circular 33"]
    E -->|"Foco productivo"| H["🚀 FRPD"]
    E -->|"Default"| I["📐 SNI General"]

    D --> J{"Tipo<br/>Ejecutor"}
    J -->|"Privado sin fines lucro"| K["🎁 8% FNDR"]
    J -->|"GORE"| L["📋 Glosa 06"]
    J -->|"Entidad Pública"| M["🔄 Transferencia"]
    J -->|"Foco productivo"| N["🚀 FRPD"]

    style A fill:#4CAF50,color:#fff
    style F fill:#FF9800,color:#fff
    style G fill:#9C27B0,color:#fff
    style H fill:#E91E63,color:#fff
    style I fill:#607D8B,color:#fff

### Matriz Decision
#### ID
BPMN-GN-IPR-SELECTOR-MATRIZ-01
#### Filas
| Via | Tipo | Ejecutor | Monto | Condicion_Clave |
| --- | --- | --- | --- | --- |
| FRIL | Proyecto | Municipalidad | < 5.000 UTM | Infraestructura menor |
| Circular 33 | Proyecto | Variable | Variable | Conservación, ANF, estudios |
| FRPD | Ambos | Habilitado | Variable | Foco productivo/innovación |
| SNI General | Proyecto | Variable | Variable | Default |
| 8% FNDR | Actividad | Privado s/f lucro | Variable | Concurso |
| Glosa 06 | Programa | GORE | Variable | Ejecución directa |
| Transferencia | Programa | Entidad pública | Variable | ITF interno |

## P1 Ingreso Pertinencia y Admisibilidad
### ID
BPMN-GN-IPR-FASE1-01
### Subprocesos
- Recepción
- CDR
- Admisibilidad Documental
### Diagrama de Flujo
#### Mermaid
flowchart TD
    subgraph EE["🏢 Entidad Externa"]
        A["📄 Postulación<br/>preparada"]
    end

    subgraph GORE["🏛️ GORE Ñuble"]
        B["📬 Oficina Partes:<br/>Recepcionar y registrar"]
        C["📊 DIPIR:<br/>Registrar en sistema"]
        D["👥 CDR:<br/>Evaluar pertinencia"]
        E{"¿Pre-admisible?"}
        F["✅ PRE-ADMISIBLE"]
        G["❌ NO PRE-ADMISIBLE"]
        H["🔍 Analista:<br/>Revisión documental"]
        I{"Estado<br/>admisibilidad"}
        J["✅ ADMISIBLE"]
        K["⚠️ CON OBSERVACIONES"]
        L["❌ INADMISIBLE"]
    end

    subgraph SUBSANACION["🔄 Subsanación"]
        M["Corregir en plazo"]
        N{"¿OK?"}
    end

    A --> B --> C --> D --> E
    E -->|"Sí"| F --> H --> I
    E -->|"No"| G
    I -->|"OK"| J
    I -->|"Observa"| K --> M --> N
    I -->|"Rechaza"| L
    N -->|"Sí"| J
    N -->|"No"| L

    style J fill:#4CAF50,color:#fff
    style L fill:#f44336,color:#fff

### Roles Involucrados
#### Filas
| Rol | Responsabilidad |
| --- | --- |
| Oficina de Partes | Recepcionar, registrar, derivar |
| Jefatura DIPIR | Registrar, convocar CDR |
| CDR | Evaluar pertinencia estratégica |
| Analista Preinversión | Revisión documental exhaustiva |

## P2 Evaluacion Tecnico Economica
### ID
BPMN-GN-IPR-FASE2-01
### Tracks
- A (SNI)
- B (Glosa 06)
- C (Simplificadas)
- D (Transferencias)
### Diagrama de Tracks
#### Mermaid
flowchart TD
    A["IPR Admisible"] --> B{"Tipo de<br/>Iniciativa"}

    B -->|"Proyecto IDI"| C["Track A:<br/>SNI/MDSF"]
    B -->|"Programa GORE"| D["Track B:<br/>Glosa 06/DIPRES"]
    B -->|"FRIL/FRPD/C33/8%"| E["Track C:<br/>Vías Simplificadas"]
    B -->|"Transf. a Entidad Pública"| F["Track D:<br/>ITF Interno"]

    subgraph TRACK_A["Track A: SNI"]
        C --> C1["Revisión RIS"]
        C1 --> C2["Envío a MDSF"]
        C2 --> C3["RATE: RS/FI/OT"]
    end

    subgraph TRACK_B["Track B: Glosa 06"]
        D --> D1["Perfil MML"]
        D1 --> D2["Diseño MML"]
        D2 --> D3["DIPRES/SES evalúa"]
        D3 --> D4["RF/FI/OT"]
    end

    subgraph TRACK_C["Track C: Simplificadas"]
        E --> E1["Requisitos específicos"]
        E1 --> E2["Evaluación GORE"]
        E2 --> E3["RS/FI/OT"]
    end

    subgraph TRACK_D["Track D: Transferencias"]
        F --> F1["Postulación GESDOC"]
        F1 --> F2["Admisibilidad DAE"]
        F2 --> F3["Eval. MML"]
        F3 --> F4["ITF Interno"]
    end

    style C3 fill:#4CAF50,color:#fff
    style D4 fill:#4CAF50,color:#fff
    style E3 fill:#4CAF50,color:#fff
    style F4 fill:#4CAF50,color:#fff

### Track A SNI MDSF
#### Mermaid
flowchart LR
    A["Revisión<br/>interna GORE"] --> B["Verificar<br/>RIS aplicable"]
    B --> C["Cargar en<br/>BIP/Carpeta Digital"]
    C --> D["Oficio a MDSF"]
    D --> E["MDSF evalúa<br/>(5+10 días)"]
    E --> F{"RATE"}
    F -->|"RS"| G["✅ Aprobado"]
    F -->|"FI"| H["Subsanar<br/>(60 días)"]
    F -->|"OT"| I["❌ Rechazado"]
    H --> E

    style G fill:#4CAF50,color:#fff
    style I fill:#f44336,color:#fff

### Track C Vias Simplificadas
#### Mermaid
flowchart TD
    subgraph FRIL["FRIL"]
        F1["Postular<br/>GESDOC+BIP"]
        F2["Admisibilidad"]
        F3["Evaluación<br/>técnica"]
        F4["RS (60 días)"]
        F1 --> F2 --> F3 --> F4
    end

    subgraph FRPD["FRPD"]
        R1["Postular<br/>formulario online"]
        R2["Adm.<br/>Administrativa"]
        R3["Adm.<br/>Técnica/Ranking"]
        R4["Evaluación<br/>GORE"]
        R5["RS"]
        R1 --> R2 --> R3 --> R4 --> R5
    end

    subgraph C33["Circular 33"]
        C1["Postular<br/>GESDOC+BIP"]
        C2["Admisibilidad"]
        C3["Revisión<br/>técnica"]
        C4["RS/FI/OT"]
        C1 --> C2 --> C3 --> C4
    end


## P3 Obtencion de Financiamiento
### ID
BPMN-GN-IPR-FASE3-01
### Rutas
- A (Sin CORE)
- B (Con CORE)
### Diagrama de Flujo
#### Mermaid
flowchart TD
    A["IPR con RS/RF"] --> B{"¿Requiere<br/>Acuerdo CORE?"}

    subgraph RUTA_A["Ruta A: Sin CORE"]
        C["Solicitar CDP"]
        D["DAF emite CDP"]
        E["Instrucción a<br/>Depto. Presupuesto"]
    end

    subgraph RUTA_B["Ruta B: Con CORE"]
        F["Preparar carpeta<br/>CORE"]
        G["Envío formal<br/>al CORE"]
        H["Votación CORE"]
        I{"¿Aprobado?"}
        J["Certificado<br/>Acuerdo CORE"]
        K["Solicitar creación<br/>presupuestaria"]
    end

    B -->|"No"| C --> D --> E
    B -->|"Sí"| F --> G --> H --> I
    I -->|"✅"| J --> K
    I -->|"❌"| L["Rechazado"]

    style E fill:#4CAF50,color:#fff
    style K fill:#4CAF50,color:#fff
    style L fill:#f44336,color:#fff

### Criterios para Acuerdo CORE
#### Filas
| Condicion | Requiere_CORE |
| --- | --- |
| Monto > 7.000 UTM | ✅ Sí |
| Nuevo programa/proyecto | ✅ Sí |
| Aumento costo <= 10% (tope 7.000 UTM) | ❌ No |
| Uso 3% emergencia (Glosa 14) | ❌ No |
| Regularización de ingresos | ❌ No |

## P4 Formalizacion
### ID
BPMN-GN-IPR-FASE4-01
### Subprocesos
- Actos
- Convenio
- Devengo
### Diagrama de Flujo
#### Mermaid
flowchart TD
    A["Financiamiento<br/>aprobado"] --> B{"Tipo de<br/>modificación"}

    B -->|"Interna"| C["Resolución GORE"]
    B -->|"Afecta Partida 31"| D["Solicitud a DIPRES"]

    C & D --> E["Visaciones internas<br/>(DAF, DIPIR, Jurídica)"]
    E --> F["Firma Gobernador/a"]
    F --> G["Control externo<br/>(DIPRES/CGR)"]
    G --> H["Elaborar Convenio<br/>de Transferencia"]
    H --> I["Revisión Jurídica"]
    I --> J["Firma GORE +<br/>Entidad Receptora"]
    J --> K["Resolución aprobatoria"]
    K --> L["Programar<br/>transferencias"]

    style L fill:#4CAF50,color:#fff

### Regla de Devengo
#### Filas
| Tipo_Receptor | Momento_Devengo |
| --- | --- |
| Privados y Municipios | Convenio tramitado |
| Servicios Públicos | Al aprobar rendición |

## P5 Ejecucion y Supervision
### ID
BPMN-GN-IPR-FASE5-01
### Subprocesos
- Inicio
- Licitación
- Seguimiento
### Diagrama de Flujo
#### Mermaid
flowchart TD
    subgraph INICIO["🚀 Inicio"]
        A["Chequeo documentación<br/>técnica"]
        B["Reunión coordinación<br/>GORE-UT"]
        C["Carpeta de<br/>seguimiento"]
    end

    subgraph LICITACION["📋 Licitación (si aplica)"]
        D["Bases y publicación<br/>Mercado Público"]
        E["Adjudicación"]
        F["Contrato"]
        G["Entrega terreno/<br/>Orden inicio"]
    end

    subgraph SEGUIMIENTO["📊 Seguimiento"]
        H["Visitas a terreno"]
        I["Revisión informes<br/>avance"]
        J["Estados de Pago"]
        K["Actualizar BIP"]
        L["Monitoreo financiero<br/>SIGFE"]
        M["Comité seguimiento"]
    end

    A --> B --> C --> D --> E --> F --> G
    G --> H --> I --> J --> K
    L --> M

    style K fill:#4CAF50,color:#fff

### Hitos de Control
#### Filas
| Hito | Responsable |
| --- | --- |
| Inicio de obra | UT / ITO |
| Avances periódicos | Supervisor GORE |
| Recepción provisoria | UT |
| Recepción definitiva | UT |

## P6 Modificaciones en Ejecucion
### ID
BPMN-GN-IPR-FASE6-01
### Subprocesos
- Solicitud
- Evaluación
- Tramitación
### Diagrama de Flujo
#### Mermaid
flowchart TD
    A["Detectar necesidad<br/>de modificación"] --> B["UT prepara<br/>informe técnico"]
    B --> C["Oficio formal<br/>al GORE"]
    C --> D["Supervisor GORE<br/>analiza"]
    D --> E{"¿Altera<br/>objetivo?"}
    E -->|"Sí"| F["❌ Rechazar"]
    E -->|"No"| G["Verificar<br/>umbrales"]
    G --> H{"¿Requiere<br/>CORE/SNI?"}
    H -->|"Sí"| I["Tramitar como<br/>nueva aprobación"]
    H -->|"No"| J["Aprobar<br/>internamente"]
    I & J --> K["Convenio<br/>modificatorio"]

    style F fill:#f44336,color:#fff
    style K fill:#4CAF50,color:#fff


## P7 Cierre Tecnico Financiero y Evaluacion Ex Post
### ID
BPMN-GN-IPR-FASE7-01
### Subprocesos
- Cierre Técnico
- Cierre Financiero
- Evaluación Ex Post
### Diagrama de Flujo
#### Mermaid
flowchart TD
    subgraph CIERRE_TEC["📋 Cierre Técnico"]
        A["Recepción provisoria"]
        B["Período garantía"]
        C["Recepción definitiva"]
        D["Informe final<br/>técnico"]
    end

    subgraph CIERRE_FIN["💰 Cierre Financiero"]
        E["Rendición final<br/>SISREC"]
        F["Revisión DAF"]
        G{"¿Saldos?"}
        H["Reintegro"]
        I["Resolución cierre<br/>convenio"]
        J["Devolución<br/>garantías"]
    end

    subgraph EXPOST["📊 Evaluación Ex Post"]
        K["Selección muestra"]
        L["Estudio evaluativo"]
        M["Lecciones aprendidas"]
    end

    A --> B --> C --> D
    D --> E --> F --> G
    G -->|"Sí"| H --> I
    G -->|"No"| I
    I --> J --> K --> L --> M

    style M fill:#9C27B0,color:#fff


## Sistemas Involucrados
### ID
BPMN-GN-IPR-SISTEMAS-01
### Filas
| Sistema | Fases_de_Uso |
| --- | --- |
| SYS-BIP-SNI | P1, P2, P5, P7 |
| SYS-GESDOC | P1, P2 |
| SYS-SIGFE | P3, P4, P5, P7 |
| SYS-SISREC | P7 |

## Normativa Aplicable
### ID
BPMN-GN-IPR-NORMATIVA-01
### Filas
| Norma | Alcance |
| --- | --- |
| LOC 19.175 | Competencias GORE |
| Ley de Presupuestos | Glosa 06, 14, 16 |
| Instructivo SUBDERE FRIL | Track C |
| Circular 33 MDSF | Track C |
| Resolución 30/2015 CGR | Rendiciones |
| Normas SNI/MDSF | Track A |

## Referencias Cruzadas
### ID
BPMN-GN-IPR-REFERENCIAS-01
### Filas
| Dominio_Relacionado | Ctx_Optional | Vinculo |
| --- | --- | --- |
| D02 Ciclo Presupuestario | ['file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D02_ciclo_presupuestario.md'] | CDP, modificaciones, SIGFE |
| D08 Rendiciones | ['file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D08_rendiciones.md'] | Cierre financiero, SISREC |
| D01 Actos Administrativos | ['file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/arquitectura/bpmn/D01_actos_administrativos.md'] | Resoluciones, Convenios |

## Ultima Actualizacion
### ID
BPMN-GN-IPR-ULT-ACT-01
### Cpt
Última actualización: 2025-12-16
