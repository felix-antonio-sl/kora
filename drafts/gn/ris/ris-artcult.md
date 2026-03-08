---
_manifest:
  urn: urn:gn:kb:ris-artcult
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_artcult_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- sni
- cultura
- proyectos-inversion
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_artcult_koda.yml
    source_hashes:
      domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_artcult_koda.yml: b81e6acc6c478e02e9d8ea146b172dec5893a516a96901e25d5416f63997d112
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
    meat_count: 83
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/ris__ris-artcult.md.json
---

# RIS Arte y Cultura (SNI 2024)
## ID
GN-RIS-ARTCULT-2024-01

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
Requisitos de información para proyectos de inversión cultural que ingresan al Sistema Nacional de Inversiones (SNI), versión 2024.

## Source
### Primary Source
kb_gn_010_ris.md (sección RIS-ARTCULT-2024)
### Ctx Required
- https://sni.gob.cl/storage/docs/RIS_Proyectos_Cultura_2024.pdf

## LLM Parsing Instructions
### ID
KODA-LLM-PARSER-GN-RIS-ARTCULT-2024-01
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


## RIS Arte Cultura 2024
### ID
RIS-ARTCULT-2024-META-01
### Fuente URL
https://sni.gob.cl/storage/docs/RIS_Proyectos_Cultura_2024.pdf
### Prop Doc
Establecer requisitos de información para proyectos de inversión cultural.
### Alcance
#### ID
RIS-ARTCULT-2024-ALCANCE-01
#### Aplicabilidad
Todas las iniciativas de inversión en proyectos culturales.
#### Foco
Necesidades culturales y artísticas.
#### Tipos Iniciativas
- Tipo-1-Nuevas: Construcción de bibliotecas, museos, centros culturales, centros de formación artística, etc.
- Tipo-2-Existentes: Reposición, normalización, reparaciones, mejoramientos o adecuaciones sin aumento de m².
### Lineas Inversion Orientaciones
#### ID
RIS-ARTCULT-2024-LINEAS-INV-01
#### Prop
Incrementar acceso a manifestaciones artísticas y culturales.
#### Prioridad
Sectores vulnerables y comunas con baja oferta cultural.
#### Acciones Clave
- Accion-1: Creación de nuevos recintos (centros culturales, bibliotecas, museos).
- Accion-2: Mejoramiento de infraestructuras existentes para optimizar y ampliar servicio cultural.
- Accion-3: Fomento de participación ciudadana en actividades culturales y programas educativos integradores.
#### Politicas Req
Incorporar diagnósticos que respondan a políticas sectoriales (nacionales, regionales, comunales).
### Consideraciones Transversales
#### ID
RIS-ARTCULT-2024-CONSIDERACIONES-TRANSV-01
#### Riesgo Desastres
#### Req Desde 2024
Aplicar "Metodología Complementaria para evaluación de Riesgo en infraestructura pública".
#### Enfoque Genero
#### Req
Integrar lineamientos y orientaciones específicas para asegurar equidad en formulación y ejecución.
### Ciclo Vida Requisitos
#### ID
RIS-ARTCULT-2024-CICLOVIDA-REQUISITOS-01
#### Etapa Prefactibilidad Factibilidad
#### ID
RIS-ARTCULT-2024-ETAPA-PREFACT-FACT-01
#### Estudio Preinversion Req
- Base: Elaborado según "Metodología General de Preparación y Evaluación de Proyectos".
- Cont: Incluir antecedentes técnicos y consideraciones específicas de edificaciones culturales.
#### Propiedad Terreno Req
Acreditar con documentación conforme a "Requisitos genéricos sobre las propiedades en que se proyectan edificaciones".
#### Programa Arq Req
Presentado en planilla Excel, firmado por profesional responsable.
#### TDR Req
Para contratación de la etapa.
#### Presupuesto Detallado Req
Incluir consultorías, asesorías, insumos y gastos administrativos (firmado).
#### Cronogramas Req
De actividades (Carta Gantt) y financiero.
#### Etapa Diseno
#### ID
RIS-ARTCULT-2024-ETAPA-DISEÑO-01
#### Actualizacion Estudio Preinv Req
Incluir ajustes basados en resultados de etapa anterior.
#### Propiedad Antecedentes Tec Req
Verificación y actualización conforme a normativas.
#### Programa Arq TDR Req
- Cont: Para contratación del diseño.
- Detalle: Debe incluir procesos de licitación, adjudicación y participación ciudadana.
#### Presupuesto Detallado Req
Considerar gastos de consultorías, asesorías y administrativos.
#### Cronogramas Req
De actividades (Carta Gantt) y financiero, integrando todos los procesos del diseño.
#### Etapa Ejecucion
#### ID
RIS-ARTCULT-2024-ETAPA-EJECUCION-01
#### Presentacion Proyecto Req
- Opcion-A: Con Estudio de Preinversión (perfil).
- Opcion-B: Con resumen ejecutivo si proviene de etapa de diseño.
- Entrega-Obligatoria: Diseño terminado.
#### Documentacion Tecnica Req
- Doc-1: Antecedentes técnicos requeridos para edificaciones.
- Doc-2: Certificación de aprobación del diseño.
#### TDR Ejecucion Req
Especificaciones técnicas detalladas.
#### Presupuesto Ejecucion Req
- Item-1: Obras civiles (planilla Excel detallada por partidas y niveles).
- Item-2: Equipos y equipamiento (incluir cotizaciones).
- Item-3: Asesorías/Consultorías (si corresponde).
- Item-4: Gastos administrativos.
#### Lista Equipos Req
Detallada y con respaldos de costos.
#### Cronogramas Req
- De-Actividades (Gantt): Contemplar licitación, adjudicación, tiempos de contrato y control de Unidad Técnica.
- Financiero: Concordante con Carta Gantt y ficha IDI.
#### Plan Contingencia Req
Especialmente para inmuebles existentes (abarcar funcionamiento, almacenaje, etc.).
### Aspectos Adicionales
#### ID
RIS-ARTCULT-2024-ADICIONALES-01
#### Firma Profesional
Todo documento de presupuesto debe estar firmado por profesional responsable.
#### Precios Sociales
Utilización obligatoria para evaluación social en todas las etapas.
#### Integracion Ficha IDI
Asegurar concordancia en tiempos y requerimientos establecidos.
#### Participacion Ciudadana
Incluir actividades específicas, especialmente en etapa de diseño.
