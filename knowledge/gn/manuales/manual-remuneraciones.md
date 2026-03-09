---
_manifest:
  urn: urn:gn:kb:manual-remuneraciones
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/gestion/kb_gn_049_manual_remuneraciones_koda.yml
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- remuneraciones
- sigper
- gestion-personas
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/gestion/kb_gn_049_manual_remuneraciones_koda.yml
    source_hashes:
      domains/gn/03_operacion/gestion/kb_gn_049_manual_remuneraciones_koda.yml: ec913a9bf78844e5a92b580b05439afdb477e766fc384ca10ab58be2d7207ee6
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
    skeleton_count: 18
    meat_count: 108
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/manuales__manual-remuneraciones.md.json
---

# Manual 3.2: Remuneraciones y Compensaciones
## ID
GN-MANUAL-REMUNERACIONES-01

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

## Ctx
Manual 3.2: Remuneraciones y Compensaciones.

## Primary Source
staging/brow_speculativo/manual_3_2_remuneraciones.md

## Authoritative Source
### Path
staging/temp/brutos ordenados/01_gestion_personas/PROCEDIMIENTO DE SOLICITUD, CÁLCULO Y PAGO DE REMUNERACIONES.md
### Priority
1
### Type
Official-Procedure-GDP
### Last Validated
2025-12-18

## Source Hierarchy
| Level | Description |
| --- | --- |
| 1 | Fuentes Brutas Ordenadas (staging/temp/brutos ordenados/*) |
| 2 | Pseudo-manuales KB (knowledge/domains/gn/gestion/pseudo_manuales_operativos/*) |
| 3 | Fuentes Especulativas (staging/brow_speculativo/*) |

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


## Manual 3 2 Remuneraciones y Compensaciones
### ID
GN-MANUAL-REM-ROOT-01
### Obj
Regular el proceso de cálculo, validación y pago de las remuneraciones del personal del GORE Ñuble, asegurando exactitud, oportunidad y cumplimiento legal.
### Seccion I Estructura de Remuneraciones
#### ID
GN-MANUAL-REM-S1-01
#### Escala de Sueldos y Haberes
#### ID
GN-MANUAL-REM-S1-EUS-01
#### Req
Estructura rige por EUS y leyes especiales de reajuste Sector Público.
#### Componentes
#### Sueldo Base
#### ID
GN-MANUAL-REM-S1-SB-01
#### Def
Asignado según grado EUS.
#### Asignaciones Permanentes
#### ID
GN-MANUAL-REM-S1-AP-01
#### Items
- Antigüedad (Bienios).
- Profesional / Directiva / Jefatura.
- Zona (según localidad).
- Modernización (Ley 19.553): Componente Base y por Desempeño Institucional/Colectivo.
#### Asignaciones Transitorias
#### ID
GN-MANUAL-REM-S1-AT-01
#### Items
- Viáticos (Comisiones de Servicio).
- Horas Extraordinarias (Trabajo fuera de jornada).
#### Honorarios
#### ID
GN-MANUAL-REM-S1-HON-01
#### Condiciones
| Req |
| --- |
| Monto definido en contrato a Suma Alzada. |
| No perciben asignaciones de escala EUS (zona, antigüedad, etc.). |
| Sujeto a boleta de honorarios mensual (electrónica). |
### Seccion II Proceso de Calculo y Pago
#### ID
GN-MANUAL-REM-S2-01
#### Ciclo Mensual de Remuneraciones
#### ID
GN-MANUAL-REM-S2-CICLO-01
#### Proc
-
  #### Paso
  1. Recopilación y Apertura (Días 01 - 14)
  #### Act
  Cierre de recepción de novedades (licencias, horas extra visadas, nuevos contratos).
  #### Input
  Formularios GDP firmados y Decretos tramitados.
-
  #### Paso
  2. Proceso y Cálculo (Días 15 - 17)
  #### Act
  Ingreso al sistema, cálculo de brutos, descuentos y líquidos.
-
  #### Paso
  3. Validación y VB (Día 18)
  #### Act
  Revisión de nóminas preliminares por Jefatura GDP y Control.
-
  #### Paso
  4. Pago (Fecha Legal)
  #### Req
  Día 19 del mes (o hábil anterior). Transferencia efectiva a cuentas funcionarios.
-
  #### Paso
  5. Reliquidaciones y Planilla Suplementaria (Días 19 - 25)
  #### Act
  Pagos rechazados o ajustes de última hora.
-
  #### Paso
  6. Pago Cotizaciones (Día 20-30)
  #### Act
  Declaración y pago PREVIRED.
#### Horas Extraordinarias y Viaticos
#### ID
GN-MANUAL-REM-S2-HEV-01
#### Horas Extras
#### ID
GN-MANUAL-REM-S2-HE-01
#### Topes Institucionales Ref PR DAF 0005
- Diurnas: Máximo 20 horas mensuales.
- Nocturnas/Festivas: Máximo 16 horas mensuales.
- Total Máximo: 40 horas (solo casos criticos excepcionales autorizados por Gobernador).
#### Req
- Resolución previa.
- Sistema de control horario biométrico debe respaldar la solicitud.
#### Viaticos
#### ID
GN-MANUAL-REM-S2-VIAT-01
#### Cond
- Pago anticipado o devengado.
#### Reglas
- Escala según grado y destino (nacional/internacional).
- Rendición de cometido requerida para cierre administrativo.
### Seccion III Obligaciones y Control
#### ID
GN-MANUAL-REM-S3-01
#### Descuentos Legales y Voluntarios
#### ID
GN-MANUAL-REM-S3-DESC-01
#### Obligatorios
#### Def
Impuesto Único de Segunda Categoría, AFP/IPS, FONASA/Isapre, Seguro de Cesantía (Código del Trabajo).
#### Voluntarios
#### Def
Ahorro previsional, asociaciones de funcionarios, convenios de bienestar (hasta tope legal del 15% o 25% de remuneración líquida).
#### Obligaciones de Informacion Ley de Presupuestos
#### ID
GN-MANUAL-REM-S3-INF-01
#### Src
Art. 14 N°10 Ley Presupuestos 2026.
#### Req
Remitir semestralmente a Comisión de Hacienda de la Cámara de Diputados:
#### Entregables
- Gastos asociados a remuneraciones.
- Calidad jurídica de contratos.
- Porcentajes por estamento y género.
- Duración media de contratos y re-contrataciones.
#### Transparencia Activa
#### ID
GN-MANUAL-REM-S3-TA-01
#### Src
Ley 20.285.
#### Req
Publicación mensual en sitio web de dotación de planta, contrata y honorarios con remuneraciones brutas y líquidas.
### Complementos y Sistema Operativo
#### ID
GN-MANUAL-REM-CTX-01
#### Ctx
Este manual se complementa con el Manual 3.1 (Ciclo de Vida) para la fuente del dato (personas) y Manual 1.3 (Tesorería) para la ejecución del gasto. Los procesos aquí descritos se gestionan operativamente a través del sistema SIGPER.

## Referencias Cruzadas
### ID
GN-MANUAL-REM-XREF-01
### Ctx Optional
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_1_ciclo_vida_koda.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_3_tiempo_ausentismo_koda.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_1_presupuesto.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_2_contabilidad.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_3_tesoreria_koda.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_5_bienestar_koda.yml
