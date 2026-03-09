---
_manifest:
  urn: urn:gn:kb:manual-desarrollo-organizacional
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/gestion/kb_gn_042_manual_desarrollo_organizacional_koda.yml
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- desarrollo-organizacional
- capacitacion
- gestion-personas
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/gestion/kb_gn_042_manual_desarrollo_organizacional_koda.yml
    source_hashes:
      domains/gn/03_operacion/gestion/kb_gn_042_manual_desarrollo_organizacional_koda.yml: 3263702921c6f5b970f42c120665e927fc6490c6f80daff6548ee571f120dc41
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
    skeleton_count: 20
    meat_count: 105
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/manuales__manual-desarrollo-organizacional.md.json
---

# Manual 3.4: Desarrollo Organizacional y Capacitación
## ID
GN-MANUAL-DESARROLLO-ORGANIZACIONAL-KODA-01

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
MANUAL-DESARROLLO-ORG-01

## Primary Source
staging/brow_speculativo/manual_3_4_desarrollo_organizacional.md

## Authoritative Sources
| Path | Type | Priority |
| --- | --- | --- |
| staging/temp/brutos ordenados/01_gestion_personas/res_exta_132_designa_encargado_y_referentes_tecnicos_cdc_2025_koda.yml | CDC-Resolution | 1 |
| staging/temp/brutos ordenados/01_gestion_personas/res_exta_817_define_equipos_trabajo_cdc_2025_koda.yml | CDC-Teams-Resolution | 1 |

## Last Validated
2025-12-18

## Source Hierarchy
| Level | Description |
| --- | --- |
| 1 | Fuentes Brutas Ordenadas (staging/temp/brutos ordenados/*) |
| 2 | Pseudo-manuales KB (knowledge/domains/gn/gestion/pseudo_manuales_operativos/*) |
| 3 | Fuentes Especulativas (staging/brow_speculativo/*) |

## Ctx
Manual 3.4: Desarrollo Organizacional y Capacitación (GORE Ñuble).

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

LEXICON (expand before processing): Act->Action, Cond->Condition, Ctx->Context, Ctx_Required->Required External Reference, Ctx_Optional->Optional External Reference, Def->Definition, Ex->Example, ID->ID, Just->Justification, Mssn->Mission, Obj->Objective, Proc->Process, Prohib->Prohibition, Purp->Purpose, Rec->Recommendation, Ref->Reference, Req->Requirement, Res->Result, Src->Source, Warn->Warning, XRef->Cross-Artifact Reference, XRef_Required->Mandatory Cross-Artifact Reference.

REFERENCE POLICY: Ref: internal only—must point to existing ID within THIS document. XRef/XRef_Required: external only—must point to a URN (optionally with #ID fragment) in another artifact. Other external mentions use Ctx:, Ctx_Required:, Ctx_Optional:, or Src:.

LANGUAGE POLICY: Keywords in English, content in original language. Never translate content.
END_LLM_INSTRUCTIONS


## Manual 3 4 Desarrollo Organizacional y Capacitacion
### ID
MANUAL-DESARROLLO-ORG-CONTENT-01
### Title
Manual 3.4: Desarrollo Organizacional y Capacitación
### Objetivo
#### ID
MANUAL-DESARROLLO-ORG-OBJ-01
#### Obj
Potenciar las competencias de los funcionarios y promover un ambiente laboral positivo, alineado con los objetivos estratégicos del GORE Ñuble.
### Seccion I Capacitacion y Formacion
#### ID
MANUAL-DESARROLLO-ORG-SEC-I-01
#### Title
Sección I: Capacitación y Formación
#### 1 Sistema de Capacitacion
#### ID
MANUAL-DESARROLLO-ORG-SEC-I-SISTEMA-01
#### Ctx
Regido por el Estatuto Administrativo y normas del Servicio Civil, busca perfeccionar los conocimientos y habilidades.
#### 2 Deteccion de Necesidades de Capacitacion DNC
#### ID
MANUAL-DESARROLLO-ORG-SEC-I-DNC-01
#### Proc
| Act | Def |
| --- | --- |
| Proceso Anual | Consulta a jefaturas y funcionarios sobre brechas de competencias. |
#### Fuentes de Informacion
- Evaluación del desempeño.
- Nuevas normativas o sistemas (ej. SIGFE, Transformación Digital).
- Objetivos estratégicos regionales (ERD).
#### 3 Plan Anual de Capacitacion PAC
#### ID
MANUAL-DESARROLLO-ORG-SEC-I-PAC-01
#### Elaboracion
#### Resp
Área de Gestión de Personas
#### Act
Consolida el DNC.
#### Comite Bipartito de Capacitacion
#### Def
Instancia consultiva con representantes de la asociación de funcionarios y la administración. Revisa y sugiere acciones.
#### Aprobacion
#### Req
Resolución Exenta del Gobernador(a).
#### Ejecucion
#### Proc
- Cursos internos
- Cursos externos
- e-learning
#### Compromiso
#### Req
- Funcionario capacitado debe replicar conocimientos o aplicarlos.
- Renuncias post-curso pueden implicar devolución de costos (según reglamento).
#### Rec Prioridad en Competencias Digitales Estrategia TDE
#### ID
MANUAL-DESARROLLO-ORG-SEC-I-TIP-DIGITAL-01
#### Rec
Se priorizarán acciones formativas en competencias digitales (uso de plataformas, firma electrónica, seguridad de la información), conforme a la Estrategia de Capacitación de la Transformación Digital del Estado.
### Seccion II Gestion del Desempeno
#### ID
MANUAL-DESARROLLO-ORG-SEC-II-01
#### Title
Sección II: Gestión del Desempeño
#### 4 Sistema de Calificaciones
#### ID
MANUAL-DESARROLLO-ORG-SEC-II-CALIFICACIONES-01
#### Def
Instrumento formal para evaluar el desempeño funcionario.
#### Periodo
#### Req
Anual (1 de septiembre al 31 de agosto).
#### Etapas
-
  #### Etapa
  1. Precalificación
  #### Resp
  Jefe Directo
  #### Def
  Evalúa factores cualitativos y cuantitativos.
-
  #### Etapa
  2. Junta Calificadora
  #### Def
  Comité colegiado que revisa las precalificaciones y asigna la nota final y Lista (1: Distinción, 2: Buena, 3: Condicional, 4: Eliminación).
-
  #### Etapa
  3. Apelación
  #### Proc
  - Funcionario puede apelar ante la Junta
  - En segunda instancia, ante la Contraloría (por vicios de legalidad).
#### 5 Metas y Compromisos PMG
#### ID
MANUAL-DESARROLLO-ORG-SEC-II-PMG-01
#### Metas de Gestion Institucional
#### Def
Definidas anualmente (ej. eficiencia presupuestaria, atención usuarios).
#### Metas de Desempeno Colectivo
#### Def
Definidas por equipo/división.
#### Evaluacion
#### Res
El cumplimiento determina el pago del Componente de Desempeño de la Asignación de Modernización (pagado trimestralmente).
### Seccion III Desarrollo Organizacional
#### ID
MANUAL-DESARROLLO-ORG-SEC-III-01
#### Title
Sección III: Desarrollo Organizacional
#### 6 Clima Laboral
#### ID
MANUAL-DESARROLLO-ORG-SEC-III-CLIMA-01
#### Medicion
#### Req
Aplicación bianual de encuestas de clima laboral (ej. ISTAS 21).
#### Intervencion
#### Proc
- Planes de acción para abordar brechas (liderazgo, comunicación, condiciones físicas).
#### 7 Conciliacion Trabajo Vida
#### ID
MANUAL-DESARROLLO-ORG-SEC-III-CONCILIACION-01
#### Politicas
#### Rec
- Promoción de corresponsabilidad parental
- Respeto de horarios
- Derecho a desconexión
#### Teletrabajo
#### Cond
Modalidad sujeta a factibilidad técnica y normativa específica (Ley de Presupuestos / Reglamento Interno), priorizando tareas que permitan medición por objetivos.
### Nota Final
#### ID
MANUAL-DESARROLLO-ORG-NOTA-01
#### Ctx
Este manual fomenta la carrera funcionaria y la profesionalización del capital humano regional. Los procesos aquí descritos se gestionan operativamente a través del sistema SIGPER.

## Referencias Cruzadas
### ID
GN-MANUAL-DESARROLLO-ORG-XREF-01
### Ctx Optional
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_1_ciclo_vida_koda.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_2_remuneraciones.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_3_tiempo_ausentismo_koda.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_5_bienestar_koda.yml
