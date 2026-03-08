---
_manifest:
  urn: urn:gn:kb:ris-proyinv
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_proyinv_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- sni
- inversiones
- proyectos-inversion
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_proyinv_koda.yml
    source_hashes:
      domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_proyinv_koda.yml: 2ff418c2537e09c49caf194bbbe8fbc0320a4f95c3b5a1ab0f146a993f46e33f
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
    meat_count: 115
    fat_count: 0
    preserved_facts:
    - Creation-Date=2025-11-28
    - Ctx=Requisitos de información sectorial genéricos para Proyectos de Inversión
      que ingresan al Sistema Nacional de Inversiones (SNI), versión 2023.
    - Human-Creator=FS
    - Human-Editor=FS
    - ID=GN-RIS-PROYINV-2023-01
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
    - LLM_Parsing_Instructions.ID=KODA-LLM-PARSER-GN-RIS-PROYINV-2023-01
    - LLM_Parsing_Instructions.Prohib=Using for artifact creation or translation.
    - LLM_Parsing_Instructions.Req=Mandatory block following Metadata.
    - Model-Collaborator=KODA-TRANSFORMER
    - Modification-Date=2025-11-28
    - 'RIS_Proyectos_Inversion_2023.Ciclo_Vida_Proyecto.Estados[0]=Estado-1-Preinversion:
      Preparación y evaluación para determinar viabilidad.'
    - 'RIS_Proyectos_Inversion_2023.Ciclo_Vida_Proyecto.Estados[1]=Estado-2-Inversion:
      Diseño y ejecución de obras.'
    - 'RIS_Proyectos_Inversion_2023.Ciclo_Vida_Proyecto.Estados[2]=Estado-3-Operacion:
      Puesta en marcha (marcha blanca) y operación en régimen.'
    - RIS_Proyectos_Inversion_2023.Ciclo_Vida_Proyecto.Etapas_Inversion[0]=Etapa-1-Diseño
    - RIS_Proyectos_Inversion_2023.Ciclo_Vida_Proyecto.Etapas_Inversion[1]=Etapa-2-Ejecucion
    - RIS_Proyectos_Inversion_2023.Ciclo_Vida_Proyecto.Etapas_Operacion[0]=Etapa-1-Puesta-en-marcha
    - RIS_Proyectos_Inversion_2023.Ciclo_Vida_Proyecto.Etapas_Operacion[1]=Etapa-2-Operacion-en-regimen
    - RIS_Proyectos_Inversion_2023.Ciclo_Vida_Proyecto.Etapas_Preinversion[0]=Etapa-1-Perfil
    - RIS_Proyectos_Inversion_2023.Ciclo_Vida_Proyecto.Etapas_Preinversion[1]=Etapa-2-Prefactibilidad
    - RIS_Proyectos_Inversion_2023.Ciclo_Vida_Proyecto.Etapas_Preinversion[2]=Etapa-3-Factibilidad
    - RIS_Proyectos_Inversion_2023.Ciclo_Vida_Proyecto.ID=RIS-PROYINV-2023-CICLOVIDA-01
    - 'RIS_Proyectos_Inversion_2023.Documentos_Apoyo.Fuentes-URL[0]=Fuente-1-RIS:
      https://sni.gob.cl/requisitos-de-informacion-por-sector'
    - 'RIS_Proyectos_Inversion_2023.Documentos_Apoyo.Fuentes-URL[1]=Fuente-2-Herramientas:
      https://sni.gob.cl/herramientas-de-apoyo-para-la-formulacion'
    - 'RIS_Proyectos_Inversion_2023.Documentos_Apoyo.Fuentes-URL[2]=Fuente-3-Metodologias:
      https://sni.gob.cl/metodologias-por-sector'
    - RIS_Proyectos_Inversion_2023.Documentos_Apoyo.ID=RIS-PROYINV-2023-APOYO-01
    - 'RIS_Proyectos_Inversion_2023.Documentos_Apoyo.Req-Especificos[0].Enunciado=Req-1:
      Requisitos genéricos sobre propiedades en edificaciones.'
    - RIS_Proyectos_Inversion_2023.Documentos_Apoyo.Req-Especificos[0].ID=Req-1
    - 'RIS_Proyectos_Inversion_2023.Documentos_Apoyo.Req-Especificos[1].Enunciado=Req-2:
      Antecedentes técnicos para proyectos con edificación.'
    - RIS_Proyectos_Inversion_2023.Documentos_Apoyo.Req-Especificos[1].ID=Req-2
    - 'RIS_Proyectos_Inversion_2023.Documentos_Apoyo.Req-Especificos[2].Enunciado=Req-3:
      Instructivo para proyectos que postulan a Pago Contra Recepción.'
    - RIS_Proyectos_Inversion_2023.Documentos_Apoyo.Req-Especificos[2].ID=Req-3
    - RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Diseno.Calendario-Inv-Req=Detalle
      por asignaciones (incluir monto para terreno si aplica).
    - RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Diseno.Cronograma-Req=Carta
      Gantt con duración en meses.
    - 'RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Diseno.Docs-Base-Req[0]=Doc-1:
      Estudio preinversional (perfil, prefactibilidad o factibilidad).'
    - 'RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Diseno.Docs-Base-Req[1]=Doc-2:
      Programa arquitectónico (según especificaciones sectoriales).'
    - 'RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Diseno.Docs-Base-Req[2]=Doc-3:
      Plano de emplazamiento y de zona (incluye áreas de influencia y servicios).'
    - RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Diseno.ID=RIS-PROYINV-2023-INVERSION-DISEÑO-01
    - 'RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Diseno.Presupuesto-Detallado-Req.Desglose-Asignaciones[0]=Gastos-Administrativos:
      Consultorías (incluye personal desagregado por nivel y otros gastos: materiales,
      insumos, difusión).'
    - 'RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Diseno.Presupuesto-Detallado-Req.Desglose-Asignaciones[1]=Gastos-Administrativos:
      Revisores independientes (según normativa).'
    - 'RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Diseno.Presupuesto-Detallado-Req.Obs-Req[0]=Unidades
      de medida: horas (RRHH) o unidades globales (otros).'
    - RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Diseno.Presupuesto-Detallado-Req.Obs-Req[1]=Incluir
      impuestos.
    - RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Diseno.TDR-Consultoria-Req=Para
      contratación de especialistas (arquitectura, ingeniería, especialidades).
    - RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Ejecucion.Cronograma-Act-Req=Detallado
      por actividad, con estimaciones de tiempo y fuentes de financiamiento.
    - 'RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Ejecucion.Docs-Req[0]=Doc-1:
      Estudio preinversional actualizado con resultados de etapa de diseño.'
    - 'RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Ejecucion.Docs-Req[1]=Doc-2:
      Resultados completos de diseño (planos, especificaciones técnicas, presupuestos
      visados).'
    - RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Ejecucion.ID=RIS-PROYINV-2023-INVERSION-EJECUCION-01
    - RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Ejecucion.Presupuesto-Proyecto-Req.Desglose-Asignaciones[0]=Gastos-Administrativos
    - RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Ejecucion.Presupuesto-Proyecto-Req.Desglose-Asignaciones[1]=Consultorias
    - RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Ejecucion.Presupuesto-Proyecto-Req.Desglose-Asignaciones[2]=Terrenos
      (incluye expropiación o adquisición)
    - RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Ejecucion.Presupuesto-Proyecto-Req.Desglose-Asignaciones[3]=Obras-Civiles
      (incluye servidumbres, redes, etc.)
    - RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Ejecucion.Presupuesto-Proyecto-Req.Desglose-Asignaciones[4]=Equipamiento
      (mobiliario integrado al proyecto)
    - RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Ejecucion.Presupuesto-Proyecto-Req.Desglose-Asignaciones[5]=Equipos
      (máquinas, hardware, software)
    - RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Ejecucion.Presupuesto-Proyecto-Req.Desglose-Asignaciones[6]=Vehiculos
      (si forman parte del proyecto)
    - RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Ejecucion.Presupuesto-Proyecto-Req.Desglose-Asignaciones[7]=Otros-Gastos
      (gastos adicionales no contemplados)
    - RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Ejecucion.Presupuesto-Proyecto-Req.Fichas-Registros-Req[0]=Coherencia
      con antecedentes de respaldo y fichas del IDI.
    - RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Ejecucion.Presupuesto-Proyecto-Req.Obs-Req[0]=Unidades
      de medida varían (horas, m², N° unidades, global, etc.).
    - RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Ejecucion.Presupuesto-Proyecto-Req.Obs-Req[1]=Costo
      total debe incluir impuestos.
    - RIS_Proyectos_Inversion_2023.Fase_Inversion.Etapa_Ejecucion.Soportes-Req=Cotizaciones
      para equipos y equipamiento.
    - RIS_Proyectos_Inversion_2023.Fase_Inversion.ID=RIS-PROYINV-2023-INVERSION-01
    - RIS_Proyectos_Inversion_2023.Fase_Preinversion.Cronograma_Actividades.Detalle-Req=Fuentes
      de financiamiento, especificación de jornada (completa, parcial, etc.).
    - RIS_Proyectos_Inversion_2023.Fase_Preinversion.Cronograma_Actividades.Formato=Carta
      Gantt.
    - RIS_Proyectos_Inversion_2023.Fase_Preinversion.Cronograma_Actividades.ID=RIS-PROYINV-2023-PREINVERSION-CRONOGRAMA-01
    - 'RIS_Proyectos_Inversion_2023.Fase_Preinversion.Estudio_Preinversional.Cont-Req[0]=Item-1:
      Perfil del proyecto (cuando se postula a prefactibilidad).'
    - 'RIS_Proyectos_Inversion_2023.Fase_Preinversion.Estudio_Preinversional.Cont-Req[1]=Item-2:
      Respaldo con metodología aplicable (general o específica).'
    - RIS_Proyectos_Inversion_2023.Fase_Preinversion.Estudio_Preinversional.ID=RIS-PROYINV-2023-PREINVERSION-ESTUDIO-01
    - RIS_Proyectos_Inversion_2023.Fase_Preinversion.ID=RIS-PROYINV-2023-PREINVERSION-01
    - RIS_Proyectos_Inversion_2023.Fase_Preinversion.Implicancias_Ambientales.ID=RIS-PROYINV-2023-PREINVERSION-AMBIENTAL-01
    - RIS_Proyectos_Inversion_2023.Fase_Preinversion.Implicancias_Ambientales.Req=Evaluación
      de impactos ambientales del proyecto.
    - 'RIS_Proyectos_Inversion_2023.Fase_Preinversion.Presupuesto_Detallado.Cont-Req[0]=Asig-Gastos-Administrativos/Item-1:
      Consultorías, personal (profesionales, técnicos, administrativos).'
    - 'RIS_Proyectos_Inversion_2023.Fase_Preinversion.Presupuesto_Detallado.Cont-Req[1]=Asig-Gastos-Administrativos/Item-2:
      Otros gastos administrativos, gastos generales, utilidades.'
    - 'RIS_Proyectos_Inversion_2023.Fase_Preinversion.Presupuesto_Detallado.Cont-Req[2]=Asig-Consultorias/Item-1:
      Costo total, desagregando perfiles y unidades de medida (horas o unidades).'
    - RIS_Proyectos_Inversion_2023.Fase_Preinversion.Presupuesto_Detallado.Formato=Desglose
      por asignaciones.
    - RIS_Proyectos_Inversion_2023.Fase_Preinversion.Presupuesto_Detallado.ID=RIS-PROYINV-2023-PREINVERSION-PRESUPUESTO-01
    - 'RIS_Proyectos_Inversion_2023.Fase_Preinversion.Presupuesto_Detallado.Obs-Req[0]=Obs-1:
      Incluir costos de estudios ambientales (EIA, DIA) si corresponde.'
    - 'RIS_Proyectos_Inversion_2023.Fase_Preinversion.Presupuesto_Detallado.Obs-Req[1]=Obs-2:
      Costo total debe incluir impuestos.'
    - 'RIS_Proyectos_Inversion_2023.Fase_Preinversion.Presupuesto_Detallado.Obs-Req[2]=Obs-3:
      Alinear a Clasificador Presupuestario (ficha IDI).'
    - RIS_Proyectos_Inversion_2023.Fase_Preinversion.Resultados_Esperados.Enfoque=Vinculados
      directamente a contenidos y objetivos del estudio.
    - RIS_Proyectos_Inversion_2023.Fase_Preinversion.Resultados_Esperados.ID=RIS-PROYINV-2023-PREINVERSION-RESULTADOS-01
    - 'RIS_Proyectos_Inversion_2023.Fase_Preinversion.TDR_Estudio.Cont-Req[0]=Antecedentes-Generales/Item-1:
      Estudios previos (nombre, consultora, año, resumen, versión más reciente).'
    - 'RIS_Proyectos_Inversion_2023.Fase_Preinversion.TDR_Estudio.Cont-Req[1]=Antecedentes-Generales/Item-2:
      Estimación de costos de inversión.'
    - 'RIS_Proyectos_Inversion_2023.Fase_Preinversion.TDR_Estudio.Cont-Req[2]=Identificacion-Problema:
      Definición del problema.'
    - 'RIS_Proyectos_Inversion_2023.Fase_Preinversion.TDR_Estudio.Cont-Req[3]=Objetivos:
      Generales y específicos.'
    - 'RIS_Proyectos_Inversion_2023.Fase_Preinversion.TDR_Estudio.Cont-Req[4]=Diag-1:
      Diagnóstico situación actual.'
    - 'RIS_Proyectos_Inversion_2023.Fase_Preinversion.TDR_Estudio.Cont-Req[5]=Var-1:
      Definición y análisis de variables (oferta, demanda, proyecciones, brechas).'
    - 'RIS_Proyectos_Inversion_2023.Fase_Preinversion.TDR_Estudio.Cont-Req[6]=Sol-1:
      Análisis de alternativas de solución.'
    - 'RIS_Proyectos_Inversion_2023.Fase_Preinversion.TDR_Estudio.Cont-Req[7]=Opt-1:
      Análisis de tamaño óptimo, localización y momento de inversión.'
    - 'RIS_Proyectos_Inversion_2023.Fase_Preinversion.TDR_Estudio.Cont-Req[8]=Cost-Ben-1:
      Identificación y valorización de costos y beneficios (directos e indirectos).'
    - 'RIS_Proyectos_Inversion_2023.Fase_Preinversion.TDR_Estudio.Cont-Req[9]=Eval-1:
      Evaluación técnico-económica de cada alternativa.'
    - 'RIS_Proyectos_Inversion_2023.Fase_Preinversion.TDR_Estudio.Cont-Req[10]=Sel-1:
      Selección mejor alternativa (con profundización en etapa de factibilidad).'
    - 'RIS_Proyectos_Inversion_2023.Fase_Preinversion.TDR_Estudio.Cont-Req[11]=Res-1:
      Resumen y conclusiones.'
    - RIS_Proyectos_Inversion_2023.Fase_Preinversion.TDR_Estudio.ID=RIS-PROYINV-2023-PREINVERSION-TDR-01
    - RIS_Proyectos_Inversion_2023.Fase_Preinversion.TDR_Estudio.Prop=Definir información
      básica y actividades del estudio.
    - RIS_Proyectos_Inversion_2023.Fuente-URL=https://sni.gob.cl/storage/docs/RIS_genericas_para_proyectos_de_inversion_2023.pdf
    - RIS_Proyectos_Inversion_2023.ID=RIS-PROYINV-2023-META-01
    - RIS_Proyectos_Inversion_2023.Prop-Doc=Establecer requisitos de información para
      la formulación y presentación de Proyectos de Inversión en sus distintas fases
      y etapas.
    - Source.Ctx_Required[0]=https://sni.gob.cl/storage/docs/RIS_genericas_para_proyectos_de_inversion_2023.pdf
    - Source.Ctx_Required[1]=https://sni.gob.cl/requisitos-de-informacion-por-sector
    - Source.Primary-Source=kb_gn_010_ris.md (sección RIS-PROYINV-2023)
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
    - _manifest.resolution.canonical_url=file://knowledge/domains/gn/kb_gn_010_ris_proyinv_koda.yml
    - _manifest.urn=urn:knowledge:gorenuble:gn:ris-proyinv:1.0.0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
---

# RIS Genéricas — Proyectos de Inversión (SNI 2023)
## ID
GN-RIS-PROYINV-2023-01

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
Requisitos de información sectorial genéricos para Proyectos de Inversión que ingresan al Sistema Nacional de Inversiones (SNI), versión 2023.

## Source
### Primary Source
kb_gn_010_ris.md (sección RIS-PROYINV-2023)
### Ctx Required
- https://sni.gob.cl/storage/docs/RIS_genericas_para_proyectos_de_inversion_2023.pdf
- https://sni.gob.cl/requisitos-de-informacion-por-sector

## LLM Parsing Instructions
### ID
KODA-LLM-PARSER-GN-RIS-PROYINV-2023-01
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


## RIS Proyectos Inversion 2023
### ID
RIS-PROYINV-2023-META-01
### Fuente URL
https://sni.gob.cl/storage/docs/RIS_genericas_para_proyectos_de_inversion_2023.pdf
### Prop Doc
Establecer requisitos de información para la formulación y presentación de Proyectos de Inversión en sus distintas fases y etapas.
### Ciclo Vida Proyecto
#### ID
RIS-PROYINV-2023-CICLOVIDA-01
#### Estados
- Estado-1-Preinversion: Preparación y evaluación para determinar viabilidad.
- Estado-2-Inversion: Diseño y ejecución de obras.
- Estado-3-Operacion: Puesta en marcha (marcha blanca) y operación en régimen.
#### Etapas Preinversion
- Etapa-1-Perfil
- Etapa-2-Prefactibilidad
- Etapa-3-Factibilidad
#### Etapas Inversion
- Etapa-1-Diseño
- Etapa-2-Ejecucion
#### Etapas Operacion
- Etapa-1-Puesta-en-marcha
- Etapa-2-Operacion-en-regimen
### Fase Preinversion
#### ID
RIS-PROYINV-2023-PREINVERSION-01
#### Estudio Preinversional
#### ID
RIS-PROYINV-2023-PREINVERSION-ESTUDIO-01
#### Cont Req
- Item-1: Perfil del proyecto (cuando se postula a prefactibilidad).
- Item-2: Respaldo con metodología aplicable (general o específica).
#### TDR Estudio
#### ID
RIS-PROYINV-2023-PREINVERSION-TDR-01
#### Prop
Definir información básica y actividades del estudio.
#### Cont Req
- Antecedentes-Generales/Item-1: Estudios previos (nombre, consultora, año, resumen, versión más reciente).
- Antecedentes-Generales/Item-2: Estimación de costos de inversión.
- Identificacion-Problema: Definición del problema.
- Objetivos: Generales y específicos.
- Diag-1: Diagnóstico situación actual.
- Var-1: Definición y análisis de variables (oferta, demanda, proyecciones, brechas).
- Sol-1: Análisis de alternativas de solución.
- Opt-1: Análisis de tamaño óptimo, localización y momento de inversión.
- Cost-Ben-1: Identificación y valorización de costos y beneficios (directos e indirectos).
- Eval-1: Evaluación técnico-económica de cada alternativa.
- Sel-1: Selección mejor alternativa (con profundización en etapa de factibilidad).
- Res-1: Resumen y conclusiones.
#### Cronograma Actividades
#### ID
RIS-PROYINV-2023-PREINVERSION-CRONOGRAMA-01
#### Formato
Carta Gantt.
#### Detalle Req
Fuentes de financiamiento, especificación de jornada (completa, parcial, etc.).
#### Resultados Esperados
#### ID
RIS-PROYINV-2023-PREINVERSION-RESULTADOS-01
#### Enfoque
Vinculados directamente a contenidos y objetivos del estudio.
#### Implicancias Ambientales
#### ID
RIS-PROYINV-2023-PREINVERSION-AMBIENTAL-01
#### Req
Evaluación de impactos ambientales del proyecto.
#### Presupuesto Detallado
#### ID
RIS-PROYINV-2023-PREINVERSION-PRESUPUESTO-01
#### Formato
Desglose por asignaciones.
#### Cont Req
- Asig-Gastos-Administrativos/Item-1: Consultorías, personal (profesionales, técnicos, administrativos).
- Asig-Gastos-Administrativos/Item-2: Otros gastos administrativos, gastos generales, utilidades.
- Asig-Consultorias/Item-1: Costo total, desagregando perfiles y unidades de medida (horas o unidades).
#### Obs Req
- Obs-1: Incluir costos de estudios ambientales (EIA, DIA) si corresponde.
- Obs-2: Costo total debe incluir impuestos.
- Obs-3: Alinear a Clasificador Presupuestario (ficha IDI).
### Fase Inversion
#### ID
RIS-PROYINV-2023-INVERSION-01
#### Etapa Diseno
#### ID
RIS-PROYINV-2023-INVERSION-DISEÑO-01
#### Docs Base Req
- Doc-1: Estudio preinversional (perfil, prefactibilidad o factibilidad).
- Doc-2: Programa arquitectónico (según especificaciones sectoriales).
- Doc-3: Plano de emplazamiento y de zona (incluye áreas de influencia y servicios).
#### Cronograma Req
Carta Gantt con duración en meses.
#### Calendario Inv Req
Detalle por asignaciones (incluir monto para terreno si aplica).
#### TDR Consultoria Req
Para contratación de especialistas (arquitectura, ingeniería, especialidades).
#### Presupuesto Detallado Req
#### Desglose Asignaciones
- Gastos-Administrativos: Consultorías (incluye personal desagregado por nivel y otros gastos: materiales, insumos, difusión).
- Gastos-Administrativos: Revisores independientes (según normativa).
#### Obs Req
- Unidades de medida: horas (RRHH) o unidades globales (otros).
- Incluir impuestos.
#### Etapa Ejecucion
#### ID
RIS-PROYINV-2023-INVERSION-EJECUCION-01
#### Docs Req
- Doc-1: Estudio preinversional actualizado con resultados de etapa de diseño.
- Doc-2: Resultados completos de diseño (planos, especificaciones técnicas, presupuestos visados).
#### Soportes Req
Cotizaciones para equipos y equipamiento.
#### Cronograma Act Req
Detallado por actividad, con estimaciones de tiempo y fuentes de financiamiento.
#### Presupuesto Proyecto Req
#### Desglose Asignaciones
- Gastos-Administrativos
- Consultorias
- Terrenos (incluye expropiación o adquisición)
- Obras-Civiles (incluye servidumbres, redes, etc.)
- Equipamiento (mobiliario integrado al proyecto)
- Equipos (máquinas, hardware, software)
- Vehiculos (si forman parte del proyecto)
- Otros-Gastos (gastos adicionales no contemplados)
#### Obs Req
- Unidades de medida varían (horas, m², N° unidades, global, etc.).
- Costo total debe incluir impuestos.
#### Fichas Registros Req
- Coherencia con antecedentes de respaldo y fichas del IDI.
### Documentos Apoyo
#### ID
RIS-PROYINV-2023-APOYO-01
#### Req Especificos
| ID | Enunciado |
| --- | --- |
| Req-1 | Req-1: Requisitos genéricos sobre propiedades en edificaciones. |
| Req-2 | Req-2: Antecedentes técnicos para proyectos con edificación. |
| Req-3 | Req-3: Instructivo para proyectos que postulan a Pago Contra Recepción. |
#### Fuentes URL
- Fuente-1-RIS: https://sni.gob.cl/requisitos-de-informacion-por-sector
- Fuente-2-Herramientas: https://sni.gob.cl/herramientas-de-apoyo-para-la-formulacion
- Fuente-3-Metodologias: https://sni.gob.cl/metodologias-por-sector
