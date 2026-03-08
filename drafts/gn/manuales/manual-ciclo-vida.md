---
_manifest:
  urn: urn:gn:kb:manual-ciclo-vida
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/gestion/kb_gn_048_manual_ciclo_vida_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- ciclo-vida-funcionario
- gestion-personas
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/gestion/kb_gn_048_manual_ciclo_vida_koda.yml
    source_hashes:
      domains/gn/03_operacion/gestion/kb_gn_048_manual_ciclo_vida_koda.yml: 0a95c3718cf50db25b12eec303d32a07148c52053b672fcfde7c78632a08238c
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.14
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 19
    meat_count: 153
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/manuales__manual-ciclo-vida.md.json
---

# Manual 3.1: Ciclo de Vida del Funcionario
## ID
GN-MANUAL-CICLO-VIDA-KODA-01

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
MANUAL-CICLO-VIDA-01

## Primary Source
staging/brow_speculativo/manual_3_1_ciclo_vida.md

## Authoritative Source
### Path
staging/temp/brutos ordenados/01_gestion_personas/MANUAL GENERAL DE PROCEDIMIENTOS INTERNOS DE GDP.md
### Priority
1
### Type
Official-Manual-GDP
### Last Validated
2025-12-18

## Source Hierarchy
| Level | Description |
| --- | --- |
| 1 | Fuentes Brutas Ordenadas (staging/temp/brutos ordenados/*) |
| 2 | Pseudo-manuales KB (knowledge/domains/gn/gestion/pseudo_manuales_operativos/*) |
| 3 | Fuentes Especulativas (staging/brow_speculativo/*) |

## Ctx
Manual 3.1: Ciclo de Vida del Funcionario.

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


## Manual 3 1 Ciclo de Vida del Funcionario
### ID
GN-MANUAL-CICLO-VIDA-CONTENT-01
### Title
Manual 3.1: Ciclo de Vida del Funcionario
### Objetivo
#### ID
GN-MANUAL-CICLO-VIDA-OBJ-01
#### Obj
Regular los procesos administrativos asociados a la trayectoria laboral de los funcionarios del Gobierno Regional de Ñuble, desde su ingreso hasta su egreso, asegurando el cumplimiento de la normativa estatutaria y presupuestaria vigente.
### Seccion I Ingreso y Contratacion
#### ID
GN-MANUAL-CICLO-VIDA-SEC-I-01
#### Title
Sección I: Ingreso y Contratación
#### 1 Calidad Juridica y Dotacion
#### ID
GN-MANUAL-CICLO-VIDA-SEC-I-CALIDAD-01
#### Def
El ingreso al GORE se realiza bajo las siguientes modalidades, sujetas a la Dotación Máxima de Personal autorizada en la Ley de Presupuestos (Partida 31):
#### Modalidades
| Modalidad | Def |
| --- | --- |
| Planta | Cargos permanentes asignados a grados específicos. Ingreso por concurso público (salvo cargos de confianza). |
| Contrata | Empleos transitorios de duración anual (hasta el 31 de diciembre), renovables. |
| Honorarios | Contratación para labores accidentales o específicas no habituales (Suma Alzada). |
| Código del Trabajo | Casos excepcionales regulados por normas específicas. |
#### Restriccion de Dotacion Art 10 Ley Presupuestos 2026
#### ID
GN-MANUAL-CICLO-VIDA-SEC-I-RESTR-DOTACION-01
#### Req
Restricción de Dotación (Art. 10 Ley Presupuestos 2026)
No se puede aumentar la dotación máxima sin una compensación (disminución en otro servicio o cupos de honorarios).
La Tasa de Reemplazo para 2026 es de 1 por cada 3 vacantes producidas por retiro (jubilación/incentivo), requiriendo certificación de disponibilidad presupuestaria previa.

#### 2 Proceso de Reclutamiento y Seleccion
#### ID
GN-MANUAL-CICLO-VIDA-SEC-I-RECLUTAMIENTO-01
#### Proc
-
  #### Paso
  1. Levantamiento del Perfil
  #### Act
  Jefatura requirente define competencias y requisitos (DFL).
-
  #### Paso
  2. Autorización Presupuestaria
  #### Act
  División de Administración y Finanzas (DAF) certifica disponibilidad de cupo y recursos (Subtítulo 21).
-
  #### Paso
  3. Concurso Público (Planta)
  #### Proc
  - Publicación en Diario Oficial y sitio web.
  - Comité de Selección evalúa antecedentes y entrevistas.
  - Confección de terna y resolución del Gobernador(a).
-
  #### Paso
  4. Selección (Contrata/Honorarios)
  #### Proc
  - Publicación de oferta (Empleos Públicos / Web GORE).
  - Evaluación curricular y psicológica.
  - Entrevista técnica.
#### 3 Formalizacion del Ingreso
#### ID
GN-MANUAL-CICLO-VIDA-SEC-I-FORMALIZACION-01
#### Elementos
-
  #### Elemento
  Decreto de Nombramiento (Planta/Contrata)
  #### Def
  Registrado en SIAPER y tramitado ante Contraloría (Toma de Razón o Registro).
-
  #### Elemento
  Contrato de Honorarios
  #### Req
  Debe especificar labores, productos, monto y vigencia.
-
  #### Elemento
  Declaraciones Juradas
  #### Req
  Intereses, Patrimonio, Inhabilidades e Incompatibilidades (Art. 12 Ley 19.653).
-
  #### Elemento
  Obligación de Informar (Art. 14 Ley Presupuestos 2026)
  #### Req
  Informar trimestralmente a la CEMP y BCN la nómina de contrataciones (nombre, cargo, título).
### Seccion II Induccion e Integracion
#### ID
GN-MANUAL-CICLO-VIDA-SEC-II-01
#### Title
Sección II: Inducción e Integración
#### 4 Programa de Induccion
#### ID
GN-MANUAL-CICLO-VIDA-SEC-II-INDUCCION-01
#### Def
Todo funcionario nuevo debe participar en el proceso de inducción institucional, conforme al Manual de Inducción del GORE Ñuble (kb_gn_017_manual_induccion_gore_nuble_2025_koda.yml).
#### Responsable
Unidad de Desarrollo Organizacional (GDP).
#### Fases
- Fase 1: Bienvenida e Instalación (Día 1): Entrega de credencial, correo, puesto de trabajo.
- Fase 2: Inducción General (Semana 1): E-learning sobre Probidad, Estatuto, Estructura GORE.
- Fase 3: Inducción Específica (Mes 1): Acompañamiento en el puesto (Mentoring) por jefatura o par.
#### Plazo
Primer mes de ejercicio. Evaluación de inducción obligatoria al día 30.
#### Protocolos Ley Karin Art 14 Ley 18 575
#### ID
GN-MANUAL-CICLO-VIDA-SEC-II-PROTOCOLOS-01
#### Req
Prevención de Violencia y Acoso (Ley Karin)
Como parte de la inducción, se deben cumplir los siguientes hitos:
1. Difusión de Protocolos: Entrega de los protocolos institucionales de prevención de violencia en el trabajo, acoso laboral y acoso sexual.
2. Capacitación Preventiva: Módulo obligatorio sobre conductas prohibidas y canales de denuncia.
3. Acuse de Recibo: El funcionario debe firmar la recepción de los protocolos y del Reglamento Interno de Higiene y Seguridad.
4. Registro: Archivo de la firma en la carpeta personal del funcionario.

### Seccion III Movilidad y Desarrollo
#### ID
GN-MANUAL-CICLO-VIDA-SEC-III-01
#### Title
Sección III: Movilidad y Desarrollo
#### 5 Encasillamiento y Promocion
#### ID
GN-MANUAL-CICLO-VIDA-SEC-III-ENCASILLAMIENTO-01
#### Elementos
-
  #### Elemento
  Ascensos
  #### Def
  Movimiento a un cargo de grado superior en la planta, por concurso interno o promoción automática (según DFL).
-
  #### Elemento
  Traspaso Honorarios a Contrata (Art. 15 Ley Presupuestos 2026)
  #### Req
  - Autorización anual máxima de cupos a nivel nacional (6.500 para 2026).
  - Requisitos: Antigüedad, funciones habituales.
  - Proceso regulado por Decreto de Hacienda. No puede significar aumento del gasto líquido mensualizado.
#### 6 Suplencias y Reemplazos
#### ID
GN-MANUAL-CICLO-VIDA-SEC-III-SUPLENCIAS-01
#### Elementos
-
  #### Elemento
  Suplencia
  #### Def
  Reemplazo de un cargo titular vacante o por ausencia del titular.
-
  #### Elemento
  Reemplazos Temporales (Art. 11 Ley Presupuestos 2026)
  #### Req
  - Para ausencias > 30 días corridos.
  - Contrato máximo 6 meses.
  - Requiere Autorización Previa de DIPRES, salvo Licencias Maternales/Parentales (que solo deben informarse).
#### 7 Comisiones de Servicio y Cometidos
#### ID
GN-MANUAL-CICLO-VIDA-SEC-III-COMISIONES-01
#### Elementos
-
  #### Elemento
  Comisión de Servicio
  #### Def
  Destinación temporal a otra institución o lugar para funciones propias del cargo.
-
  #### Elemento
  Cometido Funcionario
  #### Def
  Desplazamiento transitorio para una tarea específica con derecho a pasajes y viáticos (ver Manual 3.2).
-
  #### Elemento
  Registro
  #### Req
  Obligatoriedad de Decreto Exento previo a la realización (salvo emergencias justificadas).
### Seccion IV Egreso y Desvinculacion
#### ID
GN-MANUAL-CICLO-VIDA-SEC-IV-01
#### Title
Sección IV: Egreso y Desvinculación
#### 8 Causales de Egreso
#### ID
GN-MANUAL-CICLO-VIDA-SEC-IV-CAUSALES-01
#### Causales
-
  #### Causal
  Renuncia Voluntaria
  #### Req
  Debe ser aceptada por la autoridad (plazo máximo 30 días para retener).
-
  #### Causal
  Jubilación
  #### Def
  Cumplimiento de edad y requisitos previsionales.
-
  #### Causal
  Vacancia del Cargo
  #### Def
  Por fallecimiento o inasistencia injustificada (>3 días seguidos).
-
  #### Causal
  Salud Incompatible
  #### Def
  - Declaración tras uso de licencias médicas por > 6 meses en 2 años (Art. 151 Estatuto Administrativo).
  - Nota: Al contratar reemplazos por licencias prolongadas, el Jefe de Servicio deberá considerar declarar la salud incompatible (Art 11 Ley Presupuestos 2026).
-
  #### Causal
  Calificación Deficiente
  #### Def
  Lista 3 (Condicional) dos veces consecutivas o Lista 4 (Eliminación).
-
  #### Causal
  Destitución
  #### Def
  Medida disciplinaria tras sumario administrativo.
-
  #### Causal
  Término de Contrata
  #### Def
  No renovación al 31 de diciembre (aviso previo, principio de confianza legítima CGR).
#### 9 Procedimiento de Cierre
#### ID
GN-MANUAL-CICLO-VIDA-SEC-IV-CIERRE-01
#### Proc
| Paso | Act |
| --- | --- |
| 1. Entrega del Cargo | Acta de traspaso de bienes (Manual 2.3), documentos y pendientes. |
| 2. Cierre de Accesos | Revocación de credenciales, accesos informáticos y firma electrónica. |
| 3. Certificado de Servicios | Emisión de relación de servicios para fines previsionales. |
| 4. Liquidación Final | Pago de haberes pendientes y feriado proporcional (si corresponde). |
| 5. Reporte de Desvinculación (Art. 14 Ley Presupuestos 2026) | Informar trimestralmente a la CEMP y BCN la nómina de funcionarios que cesan funciones (nombre, cargo, antigüedad, fecha y causal). |
### Nota de Cierre
#### ID
GN-MANUAL-CICLO-VIDA-NOTA-01
#### Ctx
Este manual se complementa con el Estatuto Administrativo (Ley 18.834), las instrucciones anuales de la Ley de Presupuestos y los protocolos de la Ley Karin (Ley 21.643). Los procesos aquí descritos se gestionan operativamente a través del sistema SIGPER.

## Referencias Cruzadas
### ID
GN-MANUAL-CICLO-VIDA-XREF-01
### Ctx Optional
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_2_remuneraciones.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_3_tiempo_ausentismo_koda.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_4_desarrollo_organizacional.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_5_bienestar_koda.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_1_presupuesto.yml
