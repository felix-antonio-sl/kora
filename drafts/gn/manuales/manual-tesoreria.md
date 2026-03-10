---
_manifest:
  urn: urn:gn:kb:manual-tesoreria
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-10'
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
    cr: 2.64
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    document_family: generic
    publication_class: knowledge
    skeleton_count: 3
    meat_count: 76
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/manuales__manual-tesoreria.md.json
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:gn:kb:manual-tesoreria
---

# Manual 1.3: Tesorería y Gestión de Ingresos
## Definiciones
| ID | Def |
| --- | --- |
| DEF-TESORERO | Funcionario responsable de la custodia de fondos, valores y administración de cuentas corrientes. |
| DEF-PAC | Programación Anual de Caja; herramienta de proyección de liquidez. |
| DEF-CUF | Cuenta Única Fiscal del Banco Estado. |
| DEF-TEF | Transferencia Electrónica de Fondos. |

## Manual 1 3 Tesoreria y Gestión de Ingresos
- **Objetivos:** Controlar el flujo de caja, la ejecución de pagos y la recaudación de ingresos, asegurando la disponibilidad financiera y el resguardo de los recursos regionales.
### Seccion I Organizacion y Normas
#### 1 Rol del Tesorero Regional
- **Referencias:** DEF-TESORERO
#### Funciones
| Act |
| --- |
| Custodia de Fondos: Administración de cuentas corrientes. |
| Custodia de Valores: Resguardo de boletas de garantía, pólizas, vales vista. |
| Firma Conjunta: Autorización de pagos junto a Jefe DAF o Jefe Finanzas. |
#### 2 Seguridad de Valores
#### Reqs
| Req |
| --- |
| |
| Uso de Caja Fuerte ignífuga con acceso restringido. |
| Póliza de Fidelidad Funcionaria para personal con manejo de fondos. |
#### 3 Marco Normativo
#### Fuentes
| Src |
| --- |
| DL 1.263 (1975): Arts. 11, 12 (Anualidad) y 30 (CUF). |
| Ley 21.180 (Transformación Digital): Expediente electrónico obligatorio. |
| Ley de Presupuestos (Partida 31): Glosas FNDR. |
### Seccion II Gestion Bancaria y Programacion
#### 4 Administracion de Cuentas CUF
- **Referencias:** DEF-CUF
- **Tipos Cuenta:** FNDR (Inversión), Funcionamiento (Gasto Administrativo), Fondos de Terceros (Custodia)
- **Requisitos:** Cierre/Apertura requiere Resolución + Autorización Hacienda.
#### 5 Programacion de Caja PAC
- **Referencias:** DEF-PAC
- **Advertencias:** Saldos no ejecutados al 31/12 deben reintegrarse a Rentas Generales (salvo SIC autorizado).
#### Proceso
| Act |
| --- |
| Informa semanalmente disponibilidad real a DIPIR/DAF. |
| Solicita remesas a DIPRES vía SIGFE según devengo exigible. |
### Seccion III Proceso de Egresos Pagos
#### 6 Ciclo de Pago a Proveedores
- **Condiciones:** Solo tras validación del Devengo.
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
- **Referencias:** DEF-TEF
- **Preferente:** Transferencia Electrónica (TEF Masiva) con doble apoderado.
- **Excepcion:** Cheques nominativos y cruzados (finiquitos, devoluciones menores).
#### 8 Remuneraciones y Cotizaciones
#### Reqs
| Req |
| --- |
| Confidencialidad: nómina encriptada. |
| Pago de Cotizaciones vía PREVIRED antes del día 10. |
### Seccion IV Gestion de Ingresos y Garantias
#### 9 Percepcion de Ingresos
- **Tipos:** Transferencias DIPRES/SUBDERE., Ingresos Propios (Venta bases, activos)., Recuperaciones (Licencias médicas SIL, viáticos)., Multas a proveedores (descuento o pago directo).
#### 10 Control de Garantias
- **Requisitos:** Devolución exige Acta de Recepción Conforme Final.
#### Proceso
| Act |
| --- |
| Recepción de documento físico o certificado digital. |
| Registro detallado (Vencimiento, Monto, Aseguradora). |
| Alerta de Vencimiento (30 y 15 días de anticipación a Unidad Técnica). |
| Cobro inmediato ante resolución de incumplimiento. |
### Seccion V Control Diario
- **Acciones:** Cuadratura de Caja diaria (Ingresos vs Egresos).
- **Prohibiciones:** Pasar diferencias al día siguiente sin aclarar.
- **Reporte:** Informe Diario de Disponibilidades y Deuda Flotante Diaria.

## Referencias Cruzadas
- **Contexto opcional:** , ,
