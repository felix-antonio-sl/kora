---
_manifest:
  urn: urn:gn:kb:ris-patrimonio
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_patrimonio_koda.yml
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- patrimonio
- sni
- inversion-publica
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_patrimonio_koda.yml
    source_hashes:
      domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_patrimonio_koda.yml: ee94c5bc9568dc06e21ab69a6febc9140ea6e9f1ee22534630b7b24a5e28f889
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.16
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 13
    meat_count: 74
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/ris__ris-patrimonio.md.json
---

# RIS Proyectos Patrimoniales (SNI 2024)
## ID
GN-RIS-PATRIMONIO-2024-01

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
Requisitos de información para proyectos de inversión en inmuebles patrimoniales que ingresan al Sistema Nacional de Inversiones (SNI), versión 2024.

## Source
### Primary Source
kb_gn_010_ris.md (sección RIS-PATRIMONIO-2024)
### Ctx Required
- https://sni.gob.cl/storage/docs/RIS_Proyectos_Inmuebles_Patrimoniales_2024.pdf

## LLM Parsing Instructions
### ID
KODA-LLM-PARSER-GN-RIS-PATRIMONIO-2024-01
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


## RIS Patrimonio 2024
### ID
RIS-PATRIMONIO-2024-META-01
### Fuente URL
https://sni.gob.cl/storage/docs/RIS_Proyectos_Inmuebles_Patrimoniales_2024.pdf
### Prop Doc
Establecer requisitos de información para proyectos de inversión en inmuebles patrimoniales.
### Alcance
#### ID
RIS-PATRIMONIO-2024-ALCANCE-01
#### Prop
Preservar e incrementar patrimonio cultural nacional a través de inversiones en inmuebles patrimoniales.
#### Tipos Inmuebles
Monumentos históricos, paleontológicos, arqueológicos, inmuebles de conservación histórica, zonas de conservación.
#### Beneficios
Recuperación de infraestructura, integración en educación formal, reconocimiento de diversidad cultural.
### Orientaciones Sectoriales
#### ID
RIS-PATRIMONIO-2024-ORIENTACIONES-SECTORIALES-01
#### Planes Infraestructura
- Origen: Generados por Ministerio de las Culturas, las Artes y el Patrimonio.
- Prop-Plan: Poner en valor inmuebles patrimoniales y asegurar condiciones para bienes muebles protegidos.
#### Enfoque Integral
- Fomenta patrimonio como bien público, factor de desarrollo humano y sostenibilidad territorial.
- Considera diversidad de expresiones culturales (más allá de lo monumental).
#### Req Transversales
- Req-A-Riesgo-Desastres: Aplicar Metodología Complementaria (desde 2024) para instalaciones turísticas.
- Req-B-Enfoque-Genero: Incorporar lineamientos específicos en la formulación de proyectos.
### Postulacion Por Etapas
#### ID
RIS-PATRIMONIO-2024-POSTULACION-ETAPAS-01
#### Etapa Prefactibilidad Factibilidad
#### ID
RIS-PATRIMONIO-2024-ETAPA-PREFACT-FACT-01
#### Formulacion Proyecto Req
- Base-Metodologica: "Metodología para la formulación y evaluación socioeconómica de proyectos de patrimonio cultural inmueble".
- Precios-Sociales: Aplicar en la evaluación.
#### Documentacion Legal Req
Copia de Resolución o Decreto Oficial que avale la protección (emitido por CMN o MINVU).
#### Propiedad Terreno Req
Acreditar propiedad según "Requisitos genéricos sobre las propiedades en que se proyectan edificaciones".
#### Presupuesto Etapa Req
- Detalle: Consultorías, actividades (nombre, costo hora/hombre, insumos, gastos administrativos).
- Firma: Profesional responsable.
#### Aprobacion Intervencion Req
Documento de aprobación del proyecto de intervención por CMN o MINVU, conforme a declaratoria original.
#### TDR Consultoria Req
Detallar requerimientos de profesionales especializados.
#### Cronogramas Req
Financiero y de actividades (Carta Gantt).
#### Etapa Diseno
#### ID
RIS-PATRIMONIO-2024-ETAPA-DISEÑO-01
#### Continuidad Formulacion Req
Actualizar perfil usando misma Metodología, integrando resultados de etapa anterior.
#### Documentacion Legal Req
Copia de Resolución o Decreto Oficial de protección legal.
#### Informes Tecnicos Opcional
Estado actual y de conservación, características especiales del terreno, etc. (si es necesario).
#### Planos Emplazamiento Req
Incluir deslindes, cotas y concordancia con Carta Gantt y ficha IDI.
#### Presupuesto Detallado Req
Incluir consultorías, gastos administrativos, permisos vigentes e informes de revisores independientes si aplica.
#### TDR Diseño Req
Programa arquitectónico y modelo de gestión aprobado por unidad técnica y propietarios.
#### Cronogramas Req
Carta Gantt (con procesos de licitación, adjudicación, contrato, control UT) y cronograma financiero.
#### Etapa Ejecucion
#### ID
RIS-PATRIMONIO-2024-ETAPA-EJECUCION-01
#### Formulacion Proyecto Req
- Opcion-A (Directo-a-Ejecucion): Estudio de preinversión a nivel de perfil (con Metodología) y entrega de diseño terminado.
- Opcion-B (Desde-Diseño): Resumen ejecutivo y entrega del diseño final.
#### Aprobacion Diseño Req
Diseño de arquitectura aprobado por CMN o SEREMI MINVU (según corresponda).
#### Equipamiento Req
Lista detallada de ítems, cantidad, especificaciones técnicas, costo unitario y total (si aplica).
#### Presupuesto Detallado Req
Obras civiles (ítems, cantidad, costos), equipos/equipamiento, consultorías/asesorías especiales, gastos administrativos.
#### Documentacion Adicional Req
Entrega de documentos requeridos para proyectos con edificación.
#### TDR Especificaciones Tec Req
- Cont: Requerimientos de obras, experiencia de oferentes, equipamiento y equipos.
- TDR específico para asesorías o consultorías especializadas.
#### Cronogramas Req
- De-Actividades (Gantt): Incluir todos los procesos (licitación, adjudicación, contrato, adquisiciones).
- Financiero: Acorde a Carta Gantt y ficha IDI.
#### Plan Contingencia Req
Especialmente si se retiran elementos patrimoniales; debe detallar almacenamiento y condiciones de preservación durante la ejecución.
