---
_manifest:
  urn: urn:gn:kb:ris-pmdt
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_pmdt_koda.yml
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- sni
- pmdt
- inversiones
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_pmdt_koda.yml
    source_hashes:
      domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_pmdt_koda.yml: f8f48675034e2613ee5cf2eaed0964d2211ddf442245e0fcb558b013a966c058
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.19
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 13
    meat_count: 57
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/ris__ris-pmdt.md.json
---

# RIS Estudio Básico PMDT (SNI 2024)
## ID
GN-RIS-EB-PMDT-2024-01

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
Requisitos de información para estudios básicos de Planes Maestros de Desarrollo Territorial (PMDT) que ingresan al Sistema Nacional de Inversiones (SNI), versión 2024.

## Source
### Primary Source
kb_gn_010_ris.md (sección RIS-EB-PMDT-2024)
### Ctx Required
- https://sni.gob.cl/storage/docs/RIS_-_Estudio_basico_PMDT_2024.pdf

## LLM Parsing Instructions
### ID
KODA-LLM-PARSER-GN-RIS-EB-PMDT-2024-01
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


## RIS EB PMDT 2024
### ID
RIS-EB-PMDT-2024-META-01
### Fuente URL
https://sni.gob.cl/storage/docs/RIS_-_Estudio_basico_PMDT_2024.pdf
### Prop Doc
Instruir postulación a SNI de estudios básicos para elaboración de Planes Maestros de Desarrollo Territorial (PMDT).
### Emisor
División de Evaluación Social de Inversiones – MDSF, 2024.
### Alcance Documento
#### ID
RIS-EB-PMDT-2024-ALCANCE-01
#### Prop
Establecer instrucciones para postular al SNI la ejecución de estudios básicos para elaborar un PMDT.
### Orientaciones Transversales
#### ID
RIS-EB-PMDT-2024-ORIENTACIONES-TRANSV-01
#### Enfoque Genero
#### Req
Obligatorio en toda iniciativa de inversión.
#### Guia
Seguir lineamientos del documento "Orientaciones para la incorporación de Enfoque de Género."
#### Riesgo Desastres
#### Aplicabilidad
Infraestructuras en zonas con riesgo (tsunami, erupción volcánica, remoción en masa, incendios forestales).
#### Req
Uso complementario del "Instructivo para la Evaluación de Riesgo de Desastres" dentro del análisis técnico-económico.
### Orientaciones Sectoriales
#### ID
RIS-EB-PMDT-2024-ORIENTACIONES-SECTORIAL-01
#### Naturaleza PMDT
Instrumento de planificación territorial enfocado en inversiones para desarrollo de ejes productivos.
#### Base Enfoque
Participativo con actores comunitarios, públicos y privados.
#### Origen Programa
Programa de Infraestructura Rural para el Desarrollo Territorial (PIRDT) de SUBDERE.
#### Extension Actual
Se extiende a otras instituciones formuladoras y financieras para levantar cartera de inversión en sector rural.
#### Participacion Institucional
- Posible convocatoria a SEREMI de Desarrollo Social y Familia y otros actores técnicos.
- Al cierre del estudio, levantar acta de aprobación firmada por toda la contraparte técnica.
### Requerimientos Info Etapa Ejecucion
#### ID
RIS-EB-PMDT-2024-REQ-INFO-EJECUCION-01
#### Req 1 Informe Seleccion
#### Cont
Informe de Selección de Territorio y Subterritorio.
#### Base Metodologica
Metodología "Formulación y Evaluación del PMDT", Capítulo II "Fase previa a la Elaboración de un PMDT."
#### Req 2 Informe Validacion
#### Cont
Informe de Validación del Subterritorio.
#### Aprobacion
Consejo Regional del Gobierno Regional, según misma metodología.
#### Req 3 TDR Estudio
#### Req
Deben estar alineados con la "Metodología para la Formulación y Evaluación del PMDT".
#### Req 4 Presupuesto Detallado
#### Desglose Req
Horas profesionales, precio unitario/hora, gastos de traslado (viáticos, pasajes, peajes), actividades de participación, gastos generales, utilidades.
#### Firma Req
Profesional responsable de la Unidad Técnica, con indicación de fecha y moneda.
#### Req 5 Plazo Ejecucion
#### Formato
Cronograma en semanas o meses.
#### Cont Extra
Incluir número de informes de avance previstos.
