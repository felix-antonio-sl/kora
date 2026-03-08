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
    preserved_facts:
    - AI-Remediator=KODA-TRANSFORMER
    - Creation-Date=2025-12-14
    - Ctx=Control de flujo de caja, ejecución de pagos y recaudación de ingresos del
      GORE Ñuble.
    - Definitions[0].Def=Funcionario responsable de la custodia de fondos, valores
      y administración de cuentas corrientes.
    - Definitions[0].ID=DEF-TESORERO
    - Definitions[1].Def=Programación Anual de Caja; herramienta de proyección de
      liquidez.
    - Definitions[1].ID=DEF-PAC
    - Definitions[2].Def=Cuenta Única Fiscal del Banco Estado.
    - Definitions[2].ID=DEF-CUF
    - Definitions[3].Def=Transferencia Electrónica de Fondos.
    - Definitions[3].ID=DEF-TEF
    - Format=KODA/Spec
    - Human-Creator=GORE Ñuble
    - ID=GN-MANUAL-TESORERIA-01
    - 'LLM_Parsing_Instructions.Content=BEGIN_LLM_INSTRUCTIONS

      Parse with absolute fidelity. Preserve meat (essential info) and skeleton (structure)
      with zero loss.

      LEXICON: Act->Action, Ctx->Context, Def->Definition, Obj->Objective, Proc->Process,
      Req->Requirement, Res->Result, Src->Source, Warn->Warning, Prohib->Prohibition.

      END_LLM_INSTRUCTIONS

      '
    - LLM_Parsing_Instructions.ID=KODA-LLM-PARSER-01
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.ID=GN-MANUAL-TESORERIA-ROOT-01
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Obj=Controlar el flujo de caja, la
      ejecución de pagos y la recaudación de ingresos, asegurando la disponibilidad
      financiera y el resguardo de los recursos regionales.
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_III_Proceso_de_Egresos_Pagos.6_Ciclo_de_Pago_a_Proveedores.Cond=Solo
      tras validación del Devengo.
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_III_Proceso_de_Egresos_Pagos.6_Ciclo_de_Pago_a_Proveedores.Escala_de_Aprobaciones[0].Rango=<
      100 UTM
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_III_Proceso_de_Egresos_Pagos.6_Ciclo_de_Pago_a_Proveedores.Escala_de_Aprobaciones[0].Resp=Jefe
      Finanzas + Tesorero
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_III_Proceso_de_Egresos_Pagos.6_Ciclo_de_Pago_a_Proveedores.Escala_de_Aprobaciones[1].Rango=100
      - 1.000 UTM
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_III_Proceso_de_Egresos_Pagos.6_Ciclo_de_Pago_a_Proveedores.Escala_de_Aprobaciones[1].Resp=Jefe
      DAF + Jefe Finanzas
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_III_Proceso_de_Egresos_Pagos.6_Ciclo_de_Pago_a_Proveedores.Escala_de_Aprobaciones[2].Rango=>
      1.000 UTM
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_III_Proceso_de_Egresos_Pagos.6_Ciclo_de_Pago_a_Proveedores.Escala_de_Aprobaciones[2].Resp=Requiere
      V°B° Administrador Regional
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_III_Proceso_de_Egresos_Pagos.6_Ciclo_de_Pago_a_Proveedores.ID=GN-MANUAL-TESORERIA-S3-PROV-01
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_III_Proceso_de_Egresos_Pagos.6_Ciclo_de_Pago_a_Proveedores.Reqs[0].Req=Recepción
      Conforme.
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_III_Proceso_de_Egresos_Pagos.6_Ciclo_de_Pago_a_Proveedores.Reqs[1].Req=Factura
      aceptada (8 días).
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_III_Proceso_de_Egresos_Pagos.6_Ciclo_de_Pago_a_Proveedores.Reqs[2].Req=OC
      y Resolución vigente.
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_III_Proceso_de_Egresos_Pagos.6_Ciclo_de_Pago_a_Proveedores.Reqs[3].Req=Imputación
      presupuestaria registrada.
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_III_Proceso_de_Egresos_Pagos.7_Medios_de_Pago.Excepcion=Cheques
      nominativos y cruzados (finiquitos, devoluciones menores).
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_III_Proceso_de_Egresos_Pagos.7_Medios_de_Pago.ID=GN-MANUAL-TESORERIA-S3-MEDIOS-01
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_III_Proceso_de_Egresos_Pagos.7_Medios_de_Pago.Preferente=Transferencia
      Electrónica (TEF Masiva) con doble apoderado.
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_III_Proceso_de_Egresos_Pagos.7_Medios_de_Pago.Ref=DEF-TEF
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_III_Proceso_de_Egresos_Pagos.8_Remuneraciones_y_Cotizaciones.ID=GN-MANUAL-TESORERIA-S3-REM-01
    - 'Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_III_Proceso_de_Egresos_Pagos.8_Remuneraciones_y_Cotizaciones.Reqs[0].Req=Confidencialidad:
      nómina encriptada.'
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_III_Proceso_de_Egresos_Pagos.8_Remuneraciones_y_Cotizaciones.Reqs[1].Req=Pago
      de Cotizaciones vía PREVIRED antes del día 10.
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_III_Proceso_de_Egresos_Pagos.ID=GN-MANUAL-TESORERIA-S3-01
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_II_Gestion_Bancaria_y_Programacion.4_Administracion_de_Cuentas_CUF.ID=GN-MANUAL-TESORERIA-S2-CUF-01
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_II_Gestion_Bancaria_y_Programacion.4_Administracion_de_Cuentas_CUF.Ref=DEF-CUF
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_II_Gestion_Bancaria_y_Programacion.4_Administracion_de_Cuentas_CUF.Req=Cierre/Apertura
      requiere Resolución + Autorización Hacienda.
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_II_Gestion_Bancaria_y_Programacion.4_Administracion_de_Cuentas_CUF.Tipos_Cuenta[0]=FNDR
      (Inversión)
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_II_Gestion_Bancaria_y_Programacion.4_Administracion_de_Cuentas_CUF.Tipos_Cuenta[1]=Funcionamiento
      (Gasto Administrativo)
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_II_Gestion_Bancaria_y_Programacion.4_Administracion_de_Cuentas_CUF.Tipos_Cuenta[2]=Fondos
      de Terceros (Custodia)
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_II_Gestion_Bancaria_y_Programacion.5_Programacion_de_Caja_PAC.ID=GN-MANUAL-TESORERIA-S2-PAC-01
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_II_Gestion_Bancaria_y_Programacion.5_Programacion_de_Caja_PAC.Proc[0].Act=Informa
      semanalmente disponibilidad real a DIPIR/DAF.
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_II_Gestion_Bancaria_y_Programacion.5_Programacion_de_Caja_PAC.Proc[1].Act=Solicita
      remesas a DIPRES vía SIGFE según devengo exigible.
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_II_Gestion_Bancaria_y_Programacion.5_Programacion_de_Caja_PAC.Ref=DEF-PAC
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_II_Gestion_Bancaria_y_Programacion.5_Programacion_de_Caja_PAC.Warn=Saldos
      no ejecutados al 31/12 deben reintegrarse a Rentas Generales (salvo SIC autorizado).
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_II_Gestion_Bancaria_y_Programacion.ID=GN-MANUAL-TESORERIA-S2-01
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_IV_Gestion_de_Ingresos_y_Garantias.10_Control_de_Garantias.ID=GN-MANUAL-TESORERIA-S4-GAR-01
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_IV_Gestion_de_Ingresos_y_Garantias.10_Control_de_Garantias.Proc[0].Act=Recepción
      de documento físico o certificado digital.
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_IV_Gestion_de_Ingresos_y_Garantias.10_Control_de_Garantias.Proc[1].Act=Registro
      detallado (Vencimiento, Monto, Aseguradora).
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_IV_Gestion_de_Ingresos_y_Garantias.10_Control_de_Garantias.Proc[2].Act=Alerta
      de Vencimiento (30 y 15 días de anticipación a Unidad Técnica).
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_IV_Gestion_de_Ingresos_y_Garantias.10_Control_de_Garantias.Proc[3].Act=Cobro
      inmediato ante resolución de incumplimiento.
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_IV_Gestion_de_Ingresos_y_Garantias.10_Control_de_Garantias.Req=Devolución
      exige Acta de Recepción Conforme Final.
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_IV_Gestion_de_Ingresos_y_Garantias.9_Percepcion_de_Ingresos.ID=GN-MANUAL-TESORERIA-S4-ING-01
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_IV_Gestion_de_Ingresos_y_Garantias.9_Percepcion_de_Ingresos.Tipos[0]=Transferencias
      DIPRES/SUBDERE.
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_IV_Gestion_de_Ingresos_y_Garantias.9_Percepcion_de_Ingresos.Tipos[1]=Ingresos
      Propios (Venta bases, activos).
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_IV_Gestion_de_Ingresos_y_Garantias.9_Percepcion_de_Ingresos.Tipos[2]=Recuperaciones
      (Licencias médicas SIL, viáticos).
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_IV_Gestion_de_Ingresos_y_Garantias.9_Percepcion_de_Ingresos.Tipos[3]=Multas
      a proveedores (descuento o pago directo).
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_IV_Gestion_de_Ingresos_y_Garantias.ID=GN-MANUAL-TESORERIA-S4-01
    - 'Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_I_Organizacion_y_Normas.1_Rol_del_Tesorero_Regional.Funciones[0].Act=Custodia
      de Fondos: Administración de cuentas corrientes.'
    - 'Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_I_Organizacion_y_Normas.1_Rol_del_Tesorero_Regional.Funciones[1].Act=Custodia
      de Valores: Resguardo de boletas de garantía, pólizas, vales vista.'
    - 'Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_I_Organizacion_y_Normas.1_Rol_del_Tesorero_Regional.Funciones[2].Act=Firma
      Conjunta: Autorización de pagos junto a Jefe DAF o Jefe Finanzas.'
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_I_Organizacion_y_Normas.1_Rol_del_Tesorero_Regional.ID=GN-MANUAL-TESORERIA-S1-ROL-01
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_I_Organizacion_y_Normas.1_Rol_del_Tesorero_Regional.Ref=DEF-TESORERO
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_I_Organizacion_y_Normas.2_Seguridad_de_Valores.ID=GN-MANUAL-TESORERIA-S1-SEG-01
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_I_Organizacion_y_Normas.2_Seguridad_de_Valores.Reqs[0].Act=Arqueo
      de Caja sorpresivo (realizado por Finanzas o Auditoría).
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_I_Organizacion_y_Normas.2_Seguridad_de_Valores.Reqs[1].Req=Uso
      de Caja Fuerte ignífuga con acceso restringido.
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_I_Organizacion_y_Normas.2_Seguridad_de_Valores.Reqs[2].Req=Póliza
      de Fidelidad Funcionaria para personal con manejo de fondos.
    - 'Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_I_Organizacion_y_Normas.3_Marco_Normativo.Fuentes[0].Src=DL
      1.263 (1975): Arts. 11, 12 (Anualidad) y 30 (CUF).'
    - 'Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_I_Organizacion_y_Normas.3_Marco_Normativo.Fuentes[1].Src=Ley
      21.180 (Transformación Digital): Expediente electrónico obligatorio.'
    - 'Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_I_Organizacion_y_Normas.3_Marco_Normativo.Fuentes[2].Src=Ley
      de Presupuestos (Partida 31): Glosas FNDR.'
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_I_Organizacion_y_Normas.3_Marco_Normativo.ID=GN-MANUAL-TESORERIA-S1-NORMA-01
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_I_Organizacion_y_Normas.ID=GN-MANUAL-TESORERIA-S1-01
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_V_Control_Diario.Act=Cuadratura
      de Caja diaria (Ingresos vs Egresos).
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_V_Control_Diario.ID=GN-MANUAL-TESORERIA-S5-01
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_V_Control_Diario.Prohib=Pasar
      diferencias al día siguiente sin aclarar.
    - Manual_1_3_Tesoreria_y_Gestión_de_Ingresos.Seccion_V_Control_Diario.Reporte=Informe
      Diario de Disponibilidades y Deuda Flotante Diaria.
    - Modification-Date=2025-12-18
    - Primary-Source=staging/brow_speculativo/manual_1_3_tesoreria.md
    - Referencias_Cruzadas.Ctx_Optional[0]=knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_1_presupuesto.yml
    - Referencias_Cruzadas.Ctx_Optional[1]=knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_2_contabilidad.yml
    - Referencias_Cruzadas.Ctx_Optional[2]=knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_1_compras_koda.yml
    - Referencias_Cruzadas.ID=GN-MANUAL-TESORERIA-XREF-01
    - Status=published
    - Version=1.0.0
    - _manifest.compatibility.breaking_changes_from=null
    - _manifest.compatibility.min_consumer_version=1.0.0
    - _manifest.dependencies.requires[0].reason=KODA/Spec format compliance
    - _manifest.dependencies.requires[0].urn=urn:knowledge:koda:core:spec:1.0.0
    - _manifest.federation.license=Institutional Use
    - _manifest.federation.visibility=internal
    - _manifest.provenance.created_at=2025-12-18
    - _manifest.provenance.created_by=KODA-TRANSFORMER
    - _manifest.provenance.last_modified_at=2025-12-18
    - _manifest.resolution.canonical_url=file://knowledge/domains/gn/gestion/kb_gn_045_manual_tesoreria_koda.yml
    - '_manifest.title=Manual 1.3: Tesorería y Gestión de Ingresos'
    - _manifest.urn=urn:knowledge:gorenuble:gn:manual-tesoreria:1.0.0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
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
