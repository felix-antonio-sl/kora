---
_manifest:
  urn: urn:gn:kb:ris-empub
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_empub_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- sni
- empresas-publicas
- inversion
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_empub_koda.yml
    source_hashes:
      domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_empub_koda.yml: 2f7d6ea2883d0c6c42e1eaf9143929c29bd001d5218a038f75ea8070f3b9bb19
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.17
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 13
    meat_count: 84
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/ris__ris-empub.md.json
---

# RIS Estudios y Proyectos de Empresas del Estado (SNI 2024)
## ID
GN-RIS-EMPUB-2024-01

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
Requisitos de información para estudios y proyectos de Empresas del Estado que ingresan al Sistema Nacional de Inversiones (SNI), versión 2024.

## Source
### Primary Source
kb_gn_010_ris.md (sección RIS-EMPUB-2024)
### Ctx Required
- https://sni.gob.cl/storage/docs/RIS_-_Estudios_y_Proyectos_de_Empresas_del_Estado_2024.pdf

## LLM Parsing Instructions
### ID
KODA-LLM-PARSER-GN-RIS-EMPUB-2024-01
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


## RIS Empresas Publicas 2024
### ID
RIS-EMPUB-2024-META-01
### Fuente URL
https://sni.gob.cl/storage/docs/RIS_-_Estudios_y_Proyectos_de_Empresas_del_Estado_2024.pdf
### Prop Doc
Establecer requisitos para estudios y proyectos de empresas del Estado que ingresan al Sistema Nacional de Inversiones (SNI).
### Alcance
#### ID
RIS-EMPUB-2024-ALCANCE-01
#### Normativa Base
Art. 25 Ley 20.530.
#### Req Norma
Exige informe de evaluación a empresas con ≥50% capital estatal.
#### Evaluacion Foco
Técnico-económica centrada en rentabilidad.
#### Instituciones Evaluadoras
- MDSF (Ministerio de Desarrollo Social y Familia).
- SEP (Sistema de Empresas Públicas).
- COCHILCO o Ministerio de Energía (según corresponda).
#### Aplicacion
Empresas que ingresan al SNI.
#### Prevalencia
Si existen RIS sectoriales, sus definiciones priman sobre este documento.
### Clasificacion Sectorial Empresas
#### ID
RIS-EMPUB-2024-CLASIFICACION-01
#### Empresas Portuarias
- Arica, Iquique, Antofagasta, Coquimbo, Valparaíso, San Antonio, Talcahuano-San Vicente, Puerto Montt, Chacabuco, Austral.
#### Transporte
- Metro S.A.
- Ferrocarriles del Estado (EFE).
#### Servicios
- COTRISA, Correos de Chile, Polla Chilena, Casa de Moneda, SASIPA, ZOFRI, ECONSSA, Fondo de Infraestructura (Desarrollo País).
#### Mineria
- ENAMI, CODELCO-CHILE, ENAP (y filiales como SIPETROL).
### Orientaciones Sectoriales
#### ID
RIS-EMPUB-2024-ORIENTACIONES-01
#### Evaluacion Privada
- Req-Tasa-Desc: Utilizar tasa de descuento del SEP.
- Cond-Sin-Tasa-SEP: Usar tasa determinada por la empresa, con fundamentación.
#### Evaluacion Social
- Req: Obligatoria si existen beneficios/costos externos o externalidades.
- Instr: Usar precios sociales y tasa de descuento social del SNI.
#### Antecedentes Tecnicos
- Req: Documentación de diseños, estudios (suelo, vial, etc.), impacto, financieros, operacionales, jurídicos y administrativos.
#### Responsabilidad
Veracidad de antecedentes es de la institución patrocinante del proyecto.
#### Metodologia
Formulación debe desarrollarse con metodología respectiva (General o Específica).
### Etapas Postulacion Proyectos
#### ID
RIS-EMPUB-2024-ETAPAS-POSTULACION-01
#### Etapa Preinversion
#### ID
RIS-EMPUB-2024-ETAPA-PREINVERSION-01
#### Estudio Preinversion Req
- Base: "Metodología General de Preparación y Evaluación de Proyectos" o metodología específica.
- Cont: Informe, planillas de Evaluación Privada y, si aplica, Evaluación Social y/o Riesgo de Desastres.
#### Terreno Req
Acreditar propiedad o, en su defecto, requisitos para nuevo terreno.
#### Contratacion Req
- TDR para contratación de estudios (prefactibilidad/factibilidad).
- Presupuesto detallado (incluye participación ciudadana si aplica), firmado por profesional competente.
#### Cronograma Req
Carta Gantt de actividades y cronograma financiero.
#### Plan Estrategico Req
Demostrar consistencia entre inversión y objetivos estratégicos de la empresa.
#### Etapa Diseno
#### ID
RIS-EMPUB-2024-ETAPA-DISEÑO-01
#### Documentacion Req
- Cond-Desde-Perfil: Adjuntar estudio de preinversión.
- Cond-Desde-Prefact/Fact: Adjuntar entregables y resumen de etapa previa.
#### Terreno Req
Documento acreditativo, según requisitos genéricos.
#### Contratacion Presupuesto Req
- TDR para contratación del diseño (incluye participación ciudadana si aplica).
- Presupuesto detallado y firmado.
#### Cronograma Req
Carta Gantt y cronograma financiero.
#### Plan Estrategico Req
Aprobado y alineado con objetivos de la empresa.
#### Etapa Ejecucion
#### ID
RIS-EMPUB-2024-ETAPA-EJECUCION-01
#### Presentacion Proyecto Modalidades
- Modalidad-A (Directo-a-Ejecucion): Estudio de preinversión a nivel de perfil, con variables clave actualizadas.
- Modalidad-B (Desde-Diseño): Resumen ejecutivo y diseño completo (terminado, aprobado, visado).
#### Aprobacion Tecnica Req
Certificación y firma de responsable técnico.
#### Terreno Req
Documento de propiedad o justificación para nuevo terreno.
#### Cronograma Req
Carta Gantt de ejecución y cronograma financiero.
#### Aprobaciones Req
Incluir aprobaciones sectoriales y técnicas pertinentes.
#### Plan Contingencia Req
Para inmuebles existentes, con detalle de costos.
#### Plan Estrategico Req
Alternativamente, demostrar consistencia con objetivos estratégicos.
#### Presupuesto Obras Req
Detallado y firmado. Considerar presupuesto de plan de contingencia.
#### RCA Req
Verificar ingreso al SEIA y acreditar aprobación de Resolución de Calificación Ambiental.
#### Puesta en Marcha Req
Definir alcance, rendimientos, costos y plazos.
