---
_manifest:
  urn: urn:gn:kb:manual-bienestar
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/gestion/kb_gn_052_manual_bienestar_koda.yml
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- bienestar
- gestion-personas
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/gestion/kb_gn_052_manual_bienestar_koda.yml
    source_hashes:
      domains/gn/03_operacion/gestion/kb_gn_052_manual_bienestar_koda.yml: 50d5c9108caed0342e5598613db7f32524ca31b5ee24544305805d352759960c
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.18
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 17
    meat_count: 85
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/manuales__manual-bienestar.md.json
---

# Manual 3.5: Bienestar y Calidad de Vida
## ID
GN-MANUAL-BIENESTAR-KODA-01

## Version
1.0.0

## Status
Draft

## Format
KODA/Spec

## Human Creator
GORE Ñuble

## Human Editor
FS

## Model Collaborator
IA-CASCADE

## AI Remediator
KODA-TRANSFORMER

## Creation Date
2025-12-14

## Modification Date
2025-12-16

## Source ID
MANUAL-BIENESTAR-01

## Primary Source
staging/brow_speculativo/manual_3_5_bienestar.md

## Ctx
Gestionar beneficios y prestaciones sociales para mejorar calidad de vida de funcionarios y cargas familiares.

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

LEXICON (expand before processing): Act->Action, Cond->Condition, Ctx->Context, Ctx_Required->Required External Reference, Ctx_Optional->Optional External Reference, Def->Definition, Ex->Example, Mssn->Mission, Obj->Objective, Proc->Process, Purp->Purpose, Ref->Reference, XRef->Cross-Artifact Reference, XRef_Required->Mandatory Cross-Artifact Reference, Req->Requirement, Res->Result, Src->Source, Prohib->Prohibition, Warn->Warning, Just->Justification, Rec->Recommendation

REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. XRef/XRef_Required: are external only—must point to a URN (optionally with #ID fragment) in another artifact. External documents without specific ID use Ctx:, Ctx_Required:, or Ctx_Optional:.

LANGUAGE POLICY: Keywords in English, content in original language. Never translate content.
END_LLM_INSTRUCTIONS


## Manual 3 5 Bienestar y Calidad de Vida
### ID
GN-MANUAL-BIENESTAR-CONTENT-01
### Title
Manual 3.5: Bienestar y Calidad de Vida
### Objetivo
#### ID
GN-MANUAL-BIENESTAR-OBJ-01
#### Obj
Gestionar los beneficios y prestaciones sociales destinados a mejorar la calidad de vida de los funcionarios y sus cargas familiares.
### Seccion I Servicio de Bienestar
#### ID
GN-MANUAL-BIENESTAR-SEC-I-01
#### Title
Sección I: Servicio de Bienestar
#### 1 Afiliacion y Aportes
#### ID
GN-MANUAL-BIENESTAR-SEC-I-AFILIACION-01
#### Caracter
#### Def
La afiliación es voluntaria y la desafiliación es libre.
#### Socios
#### Req
Funcionarios de Planta y Contrata (y jubilados que deseen permanecer).
#### Financiamiento
| Fuente | Def |
| --- | --- |
| Aporte del Funcionario | Porcentaje de su remuneración imponible (descuento por planilla). |
| Aporte Institucional | Aporte anual definido en Ley de Presupuestos (Subtítulo 24). |
| Cuota de Incorporación | Pago único al ingresar. |
#### 2 Administracion
#### ID
GN-MANUAL-BIENESTAR-SEC-I-ADMIN-01
#### Organos
| Organo | Def |
| --- | --- |
| Consejo Administrativo | Órgano colegiado con representantes de la institución y de los socios (electos). Decide sobre presupuestos y beneficios. |
| Unidad de Bienestar | Ejecuta las decisiones del Consejo y administra los fondos. |
### Seccion II Beneficios y Prestaciones
#### ID
GN-MANUAL-BIENESTAR-SEC-II-01
#### Title
Sección II: Beneficios y Prestaciones
#### 3 Ayudas Medicas y Dentales
#### ID
GN-MANUAL-BIENESTAR-SEC-II-AYUDA-SALUD-01
#### Reembolso
#### Def
Bonificación de un porcentaje del copago (no cubierto por Isapre/FONASA y seguro complementario) en consultas, exámenes, medicamentos, óptica y prótesis.
#### Tope Anual
#### Req
Monto máximo de reembolso por socio/carga.
#### 4 Ayudas Economicas
#### ID
GN-MANUAL-BIENESTAR-SEC-II-AYUDA-ECO-01
#### Subsidios
#### Def
Asignaciones en dinero por eventos vitales (Nacimiento, Matrimonio/AUC, Fallecimiento).
#### Bonos Escolares
#### Def
Aporte anual por escolaridad de hijos (Pre-kinder a Universidad).
#### Becas de Excelencia
#### Def
Premio al rendimiento académico del funcionario o hijos.
#### 5 Prestamos
#### ID
GN-MANUAL-BIENESTAR-SEC-II-PRESTAMOS-01
#### Tipos
- Médico
- Auxilio (libre disposición)
- Escolar
- Habitacional
#### Condiciones
- Interés bajo
- Descuento por planilla en cuotas
- Requiere codeudor solidario (otro socio) según monto
#### 6 Convenios
#### ID
GN-MANUAL-BIENESTAR-SEC-II-CONVENIOS-01
#### Comerciales
#### Def
Descuentos en farmacias, gimnasios, ópticas, librerías, etc.
#### Institucionales
#### Def
Acuerdos con Cajas de Compensación (CCAF) para créditos sociales y turismo.
### Seccion III Calidad de Vida
#### ID
GN-MANUAL-BIENESTAR-SEC-III-01
#### Title
Sección III: Calidad de Vida
#### 7 Actividades Recreativas y Culturales
#### ID
GN-MANUAL-BIENESTAR-SEC-III-ACTIVIDADES-01
#### Act
- Organización de eventos de camaradería (Aniversario GORE, Fiestas Patrias, Navidad).
- Actividades deportivas y talleres.
#### 8 Prevencion de Riesgos
#### ID
GN-MANUAL-BIENESTAR-SEC-III-RIESGOS-01
#### Act
- Coordinación con Mutualidad (ACHS/IST) para evaluación de puestos de trabajo y prevención de enfermedades profesionales.
### Nota de Cierre
#### ID
GN-MANUAL-BIENESTAR-NOTA-01
#### Ctx
Este manual se rige por el Reglamento General de Servicios de Bienestar y el Reglamento Interno Específico del GORE Ñuble. Los procesos aquí descritos se gestionan operativamente a través del sistema SIGPER.

## Referencias Cruzadas
### ID
GN-MANUAL-BIENESTAR-XREF-01
### Ctx Optional
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_2_remuneraciones.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_1_ciclo_vida_koda.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_4_desarrollo_organizacional.yml
