---
_manifest:
  urn: urn:gn:kb:ris-index
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_index_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- sni
- inversion-publica
- ris
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_index_koda.yml
    source_hashes:
      domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_index_koda.yml: 37bd32f03f5bf4b7480d8da3163c0303a73405a9c8cfcf32ee71d6508bae2b93
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.35
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 12
    meat_count: 69
    fat_count: 0
    preserved_facts:
    - Creation-Date=2025-11-28
    - Ctx=Índice maestro de Requisitos de Información Sectorial (RIS) del Sistema
      Nacional de Inversiones (SNI) relevantes para el GORE Ñuble.
    - Human-Creator=FS
    - Human-Editor=FS
    - ID=GN-RIS-INDEX-01
    - "LLM_Parsing_Instructions.Content=BEGIN_LLM_INSTRUCTIONS\nYou are an AI agent\
      \ consuming a KODA artifact. Parse with absolute fidelity.\n\nFIDELITY: Preserve\
      \ meat (essential information) and skeleton (structure: headers, IDs, lists,\
      \ tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).\n\
      \nLEXICON (expand before processing):\n  Act->Action, Cause->Cause, Cond->Condition,\
      \ Cpt->Concept, Ctx->Context,\n  Def->Definition, Dep->Dependency, Dest->Destination,\
      \ Dln->Deadline,\n  Ex->Example, Fnd->Foundation, ID->ID, Instr->Instruction,\n\
      \  Just->Justification, Mech->Mechanism, Mssn->Mission, Mdl->Model,\n  Nat->Nature,\
      \ Obj->Objective, Proc->Process, Prohib->Prohibition,\n  Purp->Purpose, Ref->Reference,\
      \ Req->Requirement, Res->Result,\n  Resp->Responsible, Src->Source, Warn->Warning.\n\
      \nREFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS\
      \ document. External documents and legal sources are mentioned as contextual\
      \ information under Ctx:, Ctx_Required:, Ctx_Optional: or Src:.\n\nLANGUAGE\
      \ POLICY: Keywords in English (and abbreviated forms as listed), content in\
      \ original language (Spanish). Never translate content.\nEND_LLM_INSTRUCTIONS\n"
    - LLM_Parsing_Instructions.ID=KODA-LLM-PARSER-GN-RIS-INDEX-01
    - LLM_Parsing_Instructions.Prohib=Using for artifact creation or translation.
    - LLM_Parsing_Instructions.Req=Mandatory block following Metadata.
    - Model-Collaborator=KODA-TRANSFORMER
    - Modification-Date=2025-11-28
    - RIS_Index.Entradas[0].Cpt=RIS Genéricas para Proyectos de Inversión (SNI 2023).
    - RIS_Index.Entradas[0].Estado=draft
    - RIS_Index.Entradas[0].Fuente-URL=https://sni.gob.cl/storage/docs/RIS_genericas_para_proyectos_de_inversion_2023.pdf
    - RIS_Index.Entradas[0].ID=RIS-PROYINV-2023
    - RIS_Index.Entradas[0].Urn=urn:knowledge:gorenuble:gn:ris-proyinv:1.0.0
    - RIS_Index.Entradas[1].Cpt=RIS para Programas de Inversión (Genérico, 2025).
    - RIS_Index.Entradas[1].Estado=draft
    - RIS_Index.Entradas[1].Fuente-URL=null
    - RIS_Index.Entradas[1].ID=RIS-PROGINV-2025
    - RIS_Index.Entradas[1].Urn=urn:knowledge:gorenuble:gn:ris-proginv:1.0.0
    - RIS_Index.Entradas[2].Cpt=RIS para Estudios y Proyectos de Empresas del Estado
      (2024).
    - RIS_Index.Entradas[2].Estado=draft
    - RIS_Index.Entradas[2].Fuente-URL=https://sni.gob.cl/storage/docs/RIS_-_Estudios_y_Proyectos_de_Empresas_del_Estado_2024.pdf
    - RIS_Index.Entradas[2].ID=RIS-EMPUB-2024
    - RIS_Index.Entradas[2].Urn=urn:knowledge:gorenuble:gn:ris-empub:1.0.0
    - RIS_Index.Entradas[3].Cpt=RIS para Estudios Básicos PMDT (Planes Maestros de
      Desarrollo Territorial, 2024).
    - RIS_Index.Entradas[3].Estado=draft
    - RIS_Index.Entradas[3].Fuente-URL=https://sni.gob.cl/storage/docs/RIS_-_Estudio_basico_PMDT_2024.pdf
    - RIS_Index.Entradas[3].ID=RIS-EB-PMDT-2024
    - RIS_Index.Entradas[3].Urn=urn:knowledge:gorenuble:gn:ris-pmdt:1.0.0
    - RIS_Index.Entradas[4].Cpt=RIS para Proyectos de Edificación Pública (2024).
    - RIS_Index.Entradas[4].Estado=draft
    - RIS_Index.Entradas[4].Fuente-URL=https://sni.gob.cl/storage/docs/RIS_-_Proyectos_de_Edificacion_publica_-_26-04-2024.pdf
    - RIS_Index.Entradas[4].ID=RIS-EDPUB-2024
    - RIS_Index.Entradas[4].Urn=urn:knowledge:gorenuble:gn:ris-edpub:1.0.0
    - RIS_Index.Entradas[5].Cpt=RIS para Proyectos de Arte y Cultura (2024).
    - RIS_Index.Entradas[5].Estado=draft
    - RIS_Index.Entradas[5].Fuente-URL=https://sni.gob.cl/storage/docs/RIS_Proyectos_Cultura_2024.pdf
    - RIS_Index.Entradas[5].ID=RIS-ARTCULT-2024
    - RIS_Index.Entradas[5].Urn=urn:knowledge:gorenuble:gn:ris-artcult:1.0.0
    - RIS_Index.Entradas[6].Cpt=RIS para Proyectos Patrimoniales (2024).
    - RIS_Index.Entradas[6].Estado=draft
    - RIS_Index.Entradas[6].Fuente-URL=https://sni.gob.cl/storage/docs/RIS_Proyectos_Inmuebles_Patrimoniales_2024.pdf
    - RIS_Index.Entradas[6].ID=RIS-PATRIMONIO-2024
    - RIS_Index.Entradas[6].Urn=urn:knowledge:gorenuble:gn:ris-patrimonio:1.0.0
    - RIS_Index.Entradas[7].Cpt=RIS para Proyectos de Infraestructura Deportiva (2024).
    - RIS_Index.Entradas[7].Estado=draft
    - RIS_Index.Entradas[7].Fuente-URL=https://sni.gob.cl/storage/docs/RIS__Proyectos_Deportes_2024.pdf
    - RIS_Index.Entradas[7].ID=RIS-DEPORTES-2024
    - RIS_Index.Entradas[7].Urn=urn:knowledge:gorenuble:gn:ris-deportes:1.0.0
    - RIS_Index.ID=GN-RIS-INDEX-01
    - RIS_Index.Purp=Servir como mapa de navegación para los diferentes RIS sectoriales
      utilizados por el GORE Ñuble.
    - Status=Draft
    - Version=1.0.0
    - _manifest.compatibility.breaking_changes_from=null
    - _manifest.compatibility.min_consumer_version=1.0.0
    - _manifest.dependencies.requires[0].reason=KODA/Spec format compliance
    - _manifest.dependencies.requires[0].urn=urn:knowledge:koda:core:spec:1.0.0
    - _manifest.dependencies.requires[1].reason=Transformation methodology reference
    - _manifest.dependencies.requires[1].urn=urn:knowledge:koda:core:transform:1.0.0
    - _manifest.federation.license=Institutional Use
    - _manifest.federation.visibility=internal
    - _manifest.provenance.created_at=2025-11-28
    - _manifest.provenance.created_by=FS
    - _manifest.provenance.last_modified_at=2025-11-28
    - _manifest.provenance.signature=null
    - _manifest.resolution.canonical_url=file://knowledge/domains/gn/kb_gn_010_ris_index_koda.yml
    - _manifest.urn=urn:knowledge:gorenuble:gn:ris-index:1.0.0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
---

# Índice RIS SNI — GORE Ñuble
## ID
GN-RIS-INDEX-01

## Version
1.0.0

## Status
Draft

## Human Creator
FS

## Human Editor
FS

## Model Collaborator
KODA-TRANSFORMER

## Creation Date
2025-11-28

## Modification Date
2025-11-28

## Ctx
Índice maestro de Requisitos de Información Sectorial (RIS) del Sistema Nacional de Inversiones (SNI) relevantes para el GORE Ñuble.

## LLM Parsing Instructions
### ID
KODA-LLM-PARSER-GN-RIS-INDEX-01
### Req
Mandatory block following Metadata.
### Prohib
Using for artifact creation or translation.
### Content
BEGIN_LLM_INSTRUCTIONS
You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).

LEXICON (expand before processing):
  Act->Action, Cause->Cause, Cond->Condition, Cpt->Concept, Ctx->Context,
  Def->Definition, Dep->Dependency, Dest->Destination, Dln->Deadline,
  Ex->Example, Fnd->Foundation, ID->ID, Instr->Instruction,
  Just->Justification, Mech->Mechanism, Mssn->Mission, Mdl->Model,
  Nat->Nature, Obj->Objective, Proc->Process, Prohib->Prohibition,
  Purp->Purpose, Ref->Reference, Req->Requirement, Res->Result,
  Resp->Responsible, Src->Source, Warn->Warning.

REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. External documents and legal sources are mentioned as contextual information under Ctx:, Ctx_Required:, Ctx_Optional: or Src:.

LANGUAGE POLICY: Keywords in English (and abbreviated forms as listed), content in original language (Spanish). Never translate content.
END_LLM_INSTRUCTIONS


## RIS Index
### ID
GN-RIS-INDEX-01
### Purp
Servir como mapa de navegación para los diferentes RIS sectoriales utilizados por el GORE Ñuble.
### Entradas
| ID | Cpt | Urn | Fuente-URL | Estado |
| --- | --- | --- | --- | --- |
| RIS-PROYINV-2023 | RIS Genéricas para Proyectos de Inversión (SNI 2023). | urn:knowledge:gorenuble:gn:ris-proyinv:1.0.0 | https://sni.gob.cl/storage/docs/RIS_genericas_para_proyectos_de_inversion_2023.pdf | draft |
| RIS-PROGINV-2025 | RIS para Programas de Inversión (Genérico, 2025). | urn:knowledge:gorenuble:gn:ris-proginv:1.0.0 | null | draft |
| RIS-EMPUB-2024 | RIS para Estudios y Proyectos de Empresas del Estado (2024). | urn:knowledge:gorenuble:gn:ris-empub:1.0.0 | https://sni.gob.cl/storage/docs/RIS_-_Estudios_y_Proyectos_de_Empresas_del_Estado_2024.pdf | draft |
| RIS-EB-PMDT-2024 | RIS para Estudios Básicos PMDT (Planes Maestros de Desarrollo Territorial, 2024). | urn:knowledge:gorenuble:gn:ris-pmdt:1.0.0 | https://sni.gob.cl/storage/docs/RIS_-_Estudio_basico_PMDT_2024.pdf | draft |
| RIS-EDPUB-2024 | RIS para Proyectos de Edificación Pública (2024). | urn:knowledge:gorenuble:gn:ris-edpub:1.0.0 | https://sni.gob.cl/storage/docs/RIS_-_Proyectos_de_Edificacion_publica_-_26-04-2024.pdf | draft |
| RIS-ARTCULT-2024 | RIS para Proyectos de Arte y Cultura (2024). | urn:knowledge:gorenuble:gn:ris-artcult:1.0.0 | https://sni.gob.cl/storage/docs/RIS_Proyectos_Cultura_2024.pdf | draft |
| RIS-PATRIMONIO-2024 | RIS para Proyectos Patrimoniales (2024). | urn:knowledge:gorenuble:gn:ris-patrimonio:1.0.0 | https://sni.gob.cl/storage/docs/RIS_Proyectos_Inmuebles_Patrimoniales_2024.pdf | draft |
| RIS-DEPORTES-2024 | RIS para Proyectos de Infraestructura Deportiva (2024). | urn:knowledge:gorenuble:gn:ris-deportes:1.0.0 | https://sni.gob.cl/storage/docs/RIS__Proyectos_Deportes_2024.pdf | draft |
