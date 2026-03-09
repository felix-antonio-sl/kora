---
_manifest:
  urn: urn:gn:kb:ris-proginv
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_proginv_koda.yml
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- sni
- inversion-publica
- mdsf
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_proginv_koda.yml
    source_hashes:
      domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_proginv_koda.yml: 6918a72cf7ef99090c9c7d3ade29ba26502c46b691595f7e9114936205443188
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.2
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 13
    meat_count: 85
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/ris__ris-proginv.md.json
---

# RIS Genéricas — Programas de Inversión (SNI 2025)
## ID
GN-RIS-PROGINV-2025-01

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
Requisitos de información sectorial genéricos para Programas de Inversión que ingresan al Sistema Nacional de Inversiones (SNI), versión 2025.

## Source
### Primary Source
kb_gn_010_ris.md (sección RIS-PROGINV-2025)

## LLM Parsing Instructions
### ID
KODA-LLM-PARSER-GN-RIS-PROGINV-2025-01
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


## RIS Programas Inversion 2025
### ID
RIS-PROGINV-2025-META-01
### Prop Doc
Establecer requisitos de información para la formulación y presentación de Programas de Inversión en el Sistema Nacional de Inversiones (SNI).
### Concepto General
#### ID
RIS-PROGINV-2025-CONCEPTO-01
#### Prop
Formular iniciativas de inversión con duración definida y finita para lograr un propósito específico en una población objetivo.
#### Plataforma
Presentación en Sistema Nacional de Inversiones (BIP) con código asignado.
#### Evaluacion
Revisión por Ministerio de Desarrollo Social y Familia (MDSF), nivel central o regional.
### Etapas Programa
#### ID
RIS-PROGINV-2025-ETAPAS-01
#### Etapa 1 Perfil
Estudio preliminar. Base para postulación.
#### Etapa 2 Diseño
Planificación detallada de actividades y recursos.
#### Etapa 3 Ejecucion
Implementación con presupuesto integral y seguimiento.
### Antecedentes Transicion Etapas
#### ID
RIS-PROGINV-2025-ANTECEDENTES-01
#### Trans Perfil Diseno
| ID | Enunciado |
| --- | --- |
| Req-1 | Req-1: Estudio de perfil (según documento guía). |
| Req-2 | Req-2: Términos de Referencia (TDR) para el diseño. |
| Req-3 | Req-3: Presupuesto detallado para etapa Diseño. |
#### Trans PerfilDiseno Ejecucion
| ID | Enunciado |
| --- | --- |
| Req-1 | Req-1: Estudio de perfil (según metodología vigente). |
| Req-2 | Req-2: Diseño definitivo del programa. |
| Req-3 | Req-3: Presupuesto detallado para etapa Ejecución. |
### TDR Programa
#### ID
RIS-PROGINV-2025-TDR-01
#### Cont 1 Diagnostico
Situación actual, problema y caracterización de la población.
#### Cont 2 Objetivos
Generales y específicos.
#### Cont 3 Localizacion
Cobertura geográfica del estudio.
#### Cont 4 Variables
Identificación, medición y análisis (cuantitativo y/o cualitativo).
#### Cont 5 Actividades
Descripción y detalle de cada acción prevista.
#### Cont 6 Metodologia
Herramientas y técnicas (talleres, e-learning, presenciales).
#### Cont 7 Cronograma
Carta Gantt en semanas o meses.
#### Cont 8 Resultados
Indicadores y evaluación de impacto en la población.
#### Cont 9 Informes
Número, tipo, contenido y resultados esperados.
### Presupuesto Detallado
#### ID
RIS-PROGINV-2025-PRESUPUESTO-01
#### Etapa Diseno
#### ID
RIS-PROGINV-2025-PRESUPUESTO-DISEÑO-01
#### Req Ficha IDI
Incluir asignaciones "Consultorías" y "Gastos Administrativos" si corresponde.
#### Desglose Req
- Item-Personal: Profesionales, Técnicos, Administrativos con perfiles detallados.
- Item-Otros-Gastos: Materiales, insumos, pasajes, difusión.
- Item-Generales-Utilidades: Gastos generales y utilidades.
#### Instr Unidad Medida
Horas o unidades. Costo total incluye impuestos.
#### Etapa Ejecucion
#### ID
RIS-PROGINV-2025-PRESUPUESTO-EJECUCION-01
#### Modo Contratacion Programa
| ID | Enunciado |
| --- | --- |
| Req-1 | Req-1: Incluir todos los gastos de la empresa ejecutora. |
| Req-2 | Req-2: Presupuesto anualizado. |
| Opcion-1 | Opcion-1: Posible asignación de "Consultorías" para contraparte técnica. |
#### Desglose Req
- Item-Personal: Detallado por tipo y nivel.
- Item-Otros-Gastos: Materiales, insumos, pasajes, difusión.
#### Instr Separacion
Separar gastos de licitación vs. gastos de seguimiento.
#### Instr Unidad Medida
Horas o unidades. Considerar impuestos.
#### Clasificador Presupuestario
#### ID
RIS-PROGINV-2025-PRESUPUESTO-CLASIFICADOR-01
#### Req 1
Incluir valores actualizados.
#### Req 2
Desglosar según conceptos establecidos en clasificador.
### Registro Ficha IDI
#### ID
RIS-PROGINV-2025-FICHA-IDI-01
#### Req 1 Coherencia
Información ingresada debe reflejar fielmente los antecedentes (TDR).
#### Req 2 Asignaciones
Estudios Básicos se registran en "Gastos Administrativos" y "Consultoría y Contratación del Programa".
