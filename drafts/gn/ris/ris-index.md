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
    cr: 1.42
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 12
    meat_count: 69
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/ris__ris-index.md.json
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
| RIS-PROYINV-2023 | RIS Genéricas para Proyectos de Inversión (SNI 2023). | urn:gn:kb:ris-proyinv | https://sni.gob.cl/storage/docs/RIS_genericas_para_proyectos_de_inversion_2023.pdf | draft |
| RIS-PROGINV-2025 | RIS para Programas de Inversión (Genérico, 2025). | urn:gn:kb:ris-proginv | null | draft |
| RIS-EMPUB-2024 | RIS para Estudios y Proyectos de Empresas del Estado (2024). | urn:gn:kb:ris-empub | https://sni.gob.cl/storage/docs/RIS_-_Estudios_y_Proyectos_de_Empresas_del_Estado_2024.pdf | draft |
| RIS-EB-PMDT-2024 | RIS para Estudios Básicos PMDT (Planes Maestros de Desarrollo Territorial, 2024). | urn:gn:kb:ris-pmdt | https://sni.gob.cl/storage/docs/RIS_-_Estudio_basico_PMDT_2024.pdf | draft |
| RIS-EDPUB-2024 | RIS para Proyectos de Edificación Pública (2024). | urn:gn:kb:ris-edpub | https://sni.gob.cl/storage/docs/RIS_-_Proyectos_de_Edificacion_publica_-_26-04-2024.pdf | draft |
| RIS-ARTCULT-2024 | RIS para Proyectos de Arte y Cultura (2024). | urn:gn:kb:ris-artcult | https://sni.gob.cl/storage/docs/RIS_Proyectos_Cultura_2024.pdf | draft |
| RIS-PATRIMONIO-2024 | RIS para Proyectos Patrimoniales (2024). | urn:gn:kb:ris-patrimonio | https://sni.gob.cl/storage/docs/RIS_Proyectos_Inmuebles_Patrimoniales_2024.pdf | draft |
| RIS-DEPORTES-2024 | RIS para Proyectos de Infraestructura Deportiva (2024). | urn:gn:kb:ris-deportes | https://sni.gob.cl/storage/docs/RIS__Proyectos_Deportes_2024.pdf | draft |
