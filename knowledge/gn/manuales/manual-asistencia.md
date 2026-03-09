---
_manifest:
  urn: urn:gn:kb:manual-asistencia
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/gestion/kb_gn_051_manual_asistencia_koda.yml
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- asistencia
- ausentismo
- gestion-personas
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/gestion/kb_gn_051_manual_asistencia_koda.yml
    source_hashes:
      domains/gn/03_operacion/gestion/kb_gn_051_manual_asistencia_koda.yml: 932eac1d1b8589c949c56f3aec4f1643c8d791657e2839bd57fa73f0286afb0d
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.15
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 19
    meat_count: 107
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/manuales__manual-asistencia.md.json
---

# Manual 3.3: Gestión del Tiempo y Ausentismo
## ID
GN-MANUAL-TIEMPO-AUSENTISMO-KODA-01

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
MANUAL-TIEMPO-AUSENTISMO-01

## Primary Source
staging/brow_speculativo/manual_3_3_tiempo_ausentismo.md

## Authoritative Source
### Path
staging/temp/brutos ordenados/01_gestion_personas/MANUAL GENERAL DE PROCEDIMIENTOS INTERNOS DE GDP.md
### Priority
1
### Type
Official-Manual-GDP
### Section
Autorización Trabajo Extraordinario, Descanso Compensatorio
### Last Validated
2025-12-18

## Source Hierarchy
| Level | Description |
| --- | --- |
| 1 | Fuentes Brutas Ordenadas (staging/temp/brutos ordenados/*) |
| 2 | Pseudo-manuales KB (knowledge/domains/gn/gestion/pseudo_manuales_operativos/*) |
| 3 | Fuentes Especulativas (staging/brow_speculativo/*) |

## Ctx
Manual: Gestión del Tiempo y Ausentismo (GORE Ñuble).

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

LEXICON (expand before processing): Act->Action, Cond->Condition, Cpt->Concept, Ctx->Context, Ctx_Required->Required External Reference, Ctx_Optional->Optional External Reference, Def->Definition, Dln->Deadline, Ex->Example, ID->ID, Just->Justification, Mssn->Mission, Obj->Objective, Proc->Process, Prohib->Prohibition, Purp->Purpose, Rec->Recommendation, Ref->Reference, Req->Requirement, Res->Result, Src->Source, Warn->Warning, XRef->Cross-Artifact Reference, XRef_Required->Mandatory Cross-Artifact Reference.

REFERENCE POLICY: Ref: internal only—must point to existing ID within THIS document. XRef/XRef_Required: external only—must point to a URN (optionally with #ID fragment) in another artifact. Other external mentions use Ctx:, Ctx_Required:, Ctx_Optional:, or Src:.

LANGUAGE POLICY: Keywords in English (and abbreviated forms as listed), content in original language (Spanish). Never translate content.
END_LLM_INSTRUCTIONS


## Manual 3 3 Gestion del Tiempo y Ausentismo
### ID
MANUAL-TIEMPO-AUSENTISMO-CONTENT-01
### Obj
Regular el control de asistencia, el cumplimiento de la jornada laboral y la gestión de permisos y licencias del personal, garantizando la continuidad operativa del GORE.
### Seccion I Jornada y Asistencia
#### ID
MANUAL-TIEMPO-SEC-I-01
#### 1 Jornada Laboral
#### ID
MANUAL-TIEMPO-SEC-I-JORNADA-01
#### Src
Estatuto Administrativo (Ley 18.834)
#### Componentes
-
  #### Jornada Ordinaria
  44 horas semanales, distribuidas de lunes a viernes.
-
  #### Horarios
  Fijos o flexibles (según reglamento interno), garantizando presencia en horario núcleo (ej. 09:30 - 16:00).
-
  #### Colacion
  Mínimo 30 minutos, no imputables a la jornada de trabajo.
#### 2 Control de Asistencia
#### ID
MANUAL-TIEMPO-SEC-I-ASISTENCIA-01
#### Sistema
#### Ctx
Registro biométrico (huella/facial) o tarjeta magnética.
#### Obligatoriedad
#### Req
Todo funcionario debe registrar entrada y salida.
#### Excepciones
#### Ctx
Cargos directivos y Jefes de División (art. 22 del Código del Trabajo por analogía/exención de marcar).
#### Atrasos y Tiempos Menores
#### ID
MANUAL-TIEMPO-SEC-I-ATRASOS-01
#### Regla
#### Cond
Suma de atrasos y tiempos menores de jornada en el periodo mensual.
#### Req
Si el total acumulado supera los 59 minutos, genera descuento proporcional en las remuneraciones del funcionario (PR-DAF-0004).
### Seccion II Gestion de Derechos Estatutarios Ausencias Planificadas
#### ID
MANUAL-TIEMPO-SEC-II-01
#### Title
Sección II: Gestión de Derechos Estatutarios
#### 3 Feriado Legal Vacaciones
#### ID
MANUAL-TIEMPO-SEC-II-FERIADO-01
#### Derecho
#### Ctx
15 días hábiles con goce de sueldo tras 1 año de servicio (aumenta a 20 y 25 días según antigüedad).
#### Solicitud
#### Proc
-
  #### Act
  Vía sistema interno (workflow SIGPER).
-
  #### Req
  Aprobada por Jefatura Directa.
#### Acumulacion
#### Req
- Posible acumular hasta 2 períodos (requiere resolución fundada).
#### Warn
Días no utilizados fuera de los períodos autorizados caducan automáticamente.
#### 4 Permisos Administrativos
#### ID
MANUAL-TIEMPO-SEC-II-PERMISOS-01
#### Dias Administrativos
#### Ctx
6 días anuales con goce de sueldo para fines particulares.
#### Fraccionamiento
#### Req
Pueden tomarse por días completos o medios días (mañana/tarde).
#### 5 Compensacion de Horas
#### ID
MANUAL-TIEMPO-SEC-II-COMPENSACION-01
#### Ctx
Devolución de tiempo por trabajos extraordinarios realizados en horario nocturno, festivo o fines de semana, autorizada previamente por Resolución.
### Seccion III Licencias Medicas Ausencias No Planificadas
#### ID
MANUAL-TIEMPO-SEC-III-01
#### Title
Sección III: Gestión de Licencias Médicas (LME)
#### 6 Flujo de Tramitacion LME
#### ID
MANUAL-TIEMPO-SEC-III-LME-01
#### Proc
-
  #### Paso
  1. Recepción y Validación
  #### Act
  El funcionario presenta LME (electrónica vía portal I-MED o manual en papel).
  #### Dln
  Max 3 días hábiles desde inicio del reposo.
-
  #### Paso
  2. Registro y Certificación
  #### Act
  GDP registra en SIGPER y emite Certificado de Remuneraciones (últimos 3 meses).
-
  #### Paso
  3. Tramitación Externa
  #### Proc
  | Cond | Act |
  | --- | --- |
  | Afiliado FONASA con Caja Compensación (CCAF). | Envío a CCAF dentro de 3 días hábiles. |
  | Afiliado FONASA sin CCAF. | Envío a COMPIN dentro de 3 días hábiles. |
  | Afiliado ISAPRE. | Envío a la Isapre respectiva dentro de 3 días hábiles. |
-
  #### Paso
  4. Resolución y Ajuste
  #### Proc
  - Recepción de Resolución (Aprobad/Rechazada/Reducida).
  - Cálculo de SIL (Subsidio por Incapacidad Laboral) para recuperación.
  - En caso de Rechazo/Reducción: Generar descuento o reintegro inmediato tras notificación (Manual 3.2).
#### 7 Mantencion de Ingresos
#### ID
MANUAL-TIEMPO-SEC-III-REMUNERACIONES-01
#### Req
El GORE garantiza el pago íntegro de la remuneración líquida mientras el funcionario mantenga el vínculo.
#### Recuperacion
GDP tramita ante el ente pagador (Caja/Compin/Isapre) la devolución del subsidio correspondiente al empleador.
### Seccion IV Responsabilidades
#### ID
MANUAL-TIEMPO-SEC-IV-01
#### Title
Sección IV: Responsabilidades
#### Funcionario
#### Req
Cuidar su asistencia, registrar marcas biométricas, solicitar permisos a tiempo y justificar ausencias en plataforma de control.
#### Jefatura Directa
#### Req
- Autorizar permisos garantizando cobertura de funciones críticas del servicio.
- Validar cumplimiento de turnos y evitar acumulación excesiva de compensatorios.
#### Gestion de Personas (GDP)
#### Req
- Administración técnica del sistema de control y SIGPER.
- Reportar semanalmente atrasos a Remuneraciones para corte mensual.
- Liderar la recuperación de subsidios por licencias médicas.
### Nota de Cierre
#### ID
GN-MANUAL-TIEMPO-NOTA-01
#### Ctx
Este manual se complementa con el Reglamento Interno de Higiene y Seguridad del GORE Ñuble. Los procesos de LME se rigen por el D.S. N° 3 de 1984 del Minsal.

## Referencias Cruzadas
### ID
GN-MANUAL-TIEMPO-XREF-01
### Ctx Optional
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_1_ciclo_vida_koda.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_2_remuneraciones.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_5_bienestar_koda.yml
