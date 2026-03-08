---
_manifest:
  urn: urn:gn:kb:manual-tesoreria
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/gestion/kb_gn_045_manual_tesoreria_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- tesoreria
- finanzas
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/gestion/kb_gn_045_manual_tesoreria_koda.yml
    source_hashes:
      domains/gn/03_operacion/gestion/kb_gn_045_manual_tesoreria_koda.yml: 764bfd77fdf2c5d3e8421de25ddea6186bb127d0a5d4dc2ddf4296d3b267d32e
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
    skeleton_count: 15
    meat_count: 100
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/manuales__manual-tesoreria.md.json
---

# Manual 1.3: Tesorería y Gestión de Ingresos
## ID
GN-MANUAL-TESORERIA-01

## Version
1.0.0

## Status
published

## Format
KODA/Spec

## Human Creator
GORE Ñuble

## AI Remediator
KODA-TRANSFORMER

## Creation Date
2025-12-14

## Modification Date
2025-12-18

## Primary Source
staging/brow_speculativo/manual_1_3_tesoreria.md

## Ctx
Control de flujo de caja, ejecución de pagos y recaudación de ingresos del GORE Ñuble.

## LLM Parsing Instructions
### ID
KODA-LLM-PARSER-01
### Content
BEGIN_LLM_INSTRUCTIONS
Parse with absolute fidelity. Preserve meat (essential info) and skeleton (structure) with zero loss.
LEXICON: Act->Action, Ctx->Context, Def->Definition, Obj->Objective, Proc->Process, Req->Requirement, Res->Result, Src->Source, Warn->Warning, Prohib->Prohibition.
END_LLM_INSTRUCTIONS


## Definitions
| ID | Def |
| --- | --- |
| DEF-TESORERO | Funcionario responsable de la custodia de fondos, valores y administración de cuentas corrientes. |
| DEF-PAC | Programación Anual de Caja; herramienta de proyección de liquidez. |
| DEF-CUF | Cuenta Única Fiscal del Banco Estado. |
| DEF-TEF | Transferencia Electrónica de Fondos. |

## Manual 1 3 Tesoreria y Gestión de Ingresos
### ID
GN-MANUAL-TESORERIA-ROOT-01
### Obj
Controlar el flujo de caja, la ejecución de pagos y la recaudación de ingresos, asegurando la disponibilidad financiera y el resguardo de los recursos regionales.
### Seccion I Organizacion y Normas
#### ID
GN-MANUAL-TESORERIA-S1-01
#### 1 Rol del Tesorero Regional
#### ID
GN-MANUAL-TESORERIA-S1-ROL-01
#### Ref
DEF-TESORERO
#### Funciones
| Act |
| --- |
| Custodia de Fondos: Administración de cuentas corrientes. |
| Custodia de Valores: Resguardo de boletas de garantía, pólizas, vales vista. |
| Firma Conjunta: Autorización de pagos junto a Jefe DAF o Jefe Finanzas. |
#### 2 Seguridad de Valores
#### ID
GN-MANUAL-TESORERIA-S1-SEG-01
#### Reqs
-
  #### Act
  Arqueo de Caja sorpresivo (realizado por Finanzas o Auditoría).
-
  #### Req
  Uso de Caja Fuerte ignífuga con acceso restringido.
-
  #### Req
  Póliza de Fidelidad Funcionaria para personal con manejo de fondos.
#### 3 Marco Normativo
#### ID
GN-MANUAL-TESORERIA-S1-NORMA-01
#### Fuentes
| Src |
| --- |
| DL 1.263 (1975): Arts. 11, 12 (Anualidad) y 30 (CUF). |
| Ley 21.180 (Transformación Digital): Expediente electrónico obligatorio. |
| Ley de Presupuestos (Partida 31): Glosas FNDR. |
### Seccion II Gestion Bancaria y Programacion
#### ID
GN-MANUAL-TESORERIA-S2-01
#### 4 Administracion de Cuentas CUF
#### ID
GN-MANUAL-TESORERIA-S2-CUF-01
#### Ref
DEF-CUF
#### Tipos Cuenta
- FNDR (Inversión)
- Funcionamiento (Gasto Administrativo)
- Fondos de Terceros (Custodia)
#### Req
Cierre/Apertura requiere Resolución + Autorización Hacienda.
#### 5 Programacion de Caja PAC
#### ID
GN-MANUAL-TESORERIA-S2-PAC-01
#### Ref
DEF-PAC
#### Proc
| Act |
| --- |
| Informa semanalmente disponibilidad real a DIPIR/DAF. |
| Solicita remesas a DIPRES vía SIGFE según devengo exigible. |
#### Warn
Saldos no ejecutados al 31/12 deben reintegrarse a Rentas Generales (salvo SIC autorizado).
### Seccion III Proceso de Egresos Pagos
#### ID
GN-MANUAL-TESORERIA-S3-01
#### 6 Ciclo de Pago a Proveedores
#### ID
GN-MANUAL-TESORERIA-S3-PROV-01
#### Cond
Solo tras validación del Devengo.
#### Reqs
| Req |
| --- |
| Recepción Conforme. |
| Factura aceptada (8 días). |
| OC y Resolución vigente. |
| Imputación presupuestaria registrada. |
#### Escala de Aprobaciones
| Rango | Resp |
| --- | --- |
| < 100 UTM | Jefe Finanzas + Tesorero |
| 100 - 1.000 UTM | Jefe DAF + Jefe Finanzas |
| > 1.000 UTM | Requiere V°B° Administrador Regional |
#### 7 Medios de Pago
#### ID
GN-MANUAL-TESORERIA-S3-MEDIOS-01
#### Ref
DEF-TEF
#### Preferente
Transferencia Electrónica (TEF Masiva) con doble apoderado.
#### Excepcion
Cheques nominativos y cruzados (finiquitos, devoluciones menores).
#### 8 Remuneraciones y Cotizaciones
#### ID
GN-MANUAL-TESORERIA-S3-REM-01
#### Reqs
| Req |
| --- |
| Confidencialidad: nómina encriptada. |
| Pago de Cotizaciones vía PREVIRED antes del día 10. |
### Seccion IV Gestion de Ingresos y Garantias
#### ID
GN-MANUAL-TESORERIA-S4-01
#### 9 Percepcion de Ingresos
#### ID
GN-MANUAL-TESORERIA-S4-ING-01
#### Tipos
- Transferencias DIPRES/SUBDERE.
- Ingresos Propios (Venta bases, activos).
- Recuperaciones (Licencias médicas SIL, viáticos).
- Multas a proveedores (descuento o pago directo).
#### 10 Control de Garantias
#### ID
GN-MANUAL-TESORERIA-S4-GAR-01
#### Proc
| Act |
| --- |
| Recepción de documento físico o certificado digital. |
| Registro detallado (Vencimiento, Monto, Aseguradora). |
| Alerta de Vencimiento (30 y 15 días de anticipación a Unidad Técnica). |
| Cobro inmediato ante resolución de incumplimiento. |
#### Req
Devolución exige Acta de Recepción Conforme Final.
### Seccion V Control Diario
#### ID
GN-MANUAL-TESORERIA-S5-01
#### Act
Cuadratura de Caja diaria (Ingresos vs Egresos).
#### Prohib
Pasar diferencias al día siguiente sin aclarar.
#### Reporte
Informe Diario de Disponibilidades y Deuda Flotante Diaria.

## Referencias Cruzadas
### ID
GN-MANUAL-TESORERIA-XREF-01
### Ctx Optional
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_1_presupuesto.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_2_contabilidad.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_1_compras_koda.yml
