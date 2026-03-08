---
_manifest:
  urn: urn:gn:kb:manual-contabilidad
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/gestion/kb_gn_044_manual_contabilidad_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- contabilidad
- sigfe
- nicsp
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/gestion/kb_gn_044_manual_contabilidad_koda.yml
    source_hashes:
      domains/gn/03_operacion/gestion/kb_gn_044_manual_contabilidad_koda.yml: e213a67f06aa9e3579701b12b3a73536efd26e221a3a11177008549bab99ff87
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
    skeleton_count: 17
    meat_count: 326
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/manuales__manual-contabilidad.md.json
---

# Manual 1.2: Contabilidad Gubernamental y Cierre Financiero
## ID
GN-MANUAL-CONTAB-CIERRE-01

## Version
1.0.0

## Status
Draft

## Format
KODA/Spec

## Human Creator
GORE Ñuble

## Human Editor
GORE Ñuble

## Model Collaborator
CASCADE

## AI Remediator
KODA-TRANSFORMER

## Creation Date
2025-12-14

## Modification Date
2025-12-16

## Ctx
Asegurar integridad contable bajo normativa NICSP y CGR; registro fidedigno, oportuno y trazable de hechos económicos del GORE Ñuble; operación diaria + procesos críticos de cierre financiero.

## Primary Source
staging/brow_speculativo/manual_1_2_contabilidad.md

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


## Definitions
### Organos y Unidades
| ID | Def |
| --- | --- |
| DEF-CGR | CGR: Contraloría General de la República. |
| DEF-DIPRES | DIPRES: Dirección de Presupuestos. |
| DEF-DIPIR | DIPIR: División de Presupuesto e Inversión Regional. |
| DEF-JEFE-FINANZAS | Jefe de Finanzas: responsable con atribución para crear nuevos modelos de asientos tipo. |
| DEF-TESORERO | Tesorero: responsable de firma del Anexo CGR de Conciliación Bancaria (junto con Jefe de Finanzas). |
### Normas y Conceptos
| ID | Def |
| --- | --- |
| DEF-NICSP | NICSP: Normas Internacionales de Contabilidad para el Sector Público; base del estándar contable chileno. |
| DEF-DEVENGO | Devengo: reconocimiento de una obligación de pago o derecho de cobro, independiente de fecha efectiva de pago o recaudación. |
| DEF-DEUDA-FLOTANTE | Deuda Flotante: obligaciones devengadas y no pagadas al cierre del ejercicio. |
| DEF-INTEROPERABILIDAD | Interoperabilidad: capacidad de intercambiar información financiera automáticamente entre sistemas (ej.: ERP <-> Banco). |
### Sistemas y Modulos
| ID | Def |
| --- | --- |
| DEF-SIGFE | SIGFE: Sistema de Información para la Gestión Financiera del Estado (agregador central). |
| DEF-ERP | ERP: sistema ERP financiero institucional; mantiene Matriz de Devengamiento y asientos patrimoniales. |
| DEF-SIGPER | SIGPER: módulo/sistema de remuneraciones. |
| DEF-SIGAS | SIGAS: módulo/sistema de activo fijo y existencias (bodega). |
| DEF-SII | SII: Servicio de Impuestos Internos (boletas electrónicas honorarios). |
| DEF-SISREC | SISREC: Sistema de Rendición Electrónica de Cuentas de CGR. |
### Documentos y Registros
| ID | Def |
| --- | --- |
| DEF-COMPROBANTE-CONTABLE | Comprobante Contable: documento fuente único de registro (papel o digital firmado). |
| DEF-LIBRO-BANCO | Libro Banco: registro cronológico de movimientos bancarios; debe cuadrar diariamente con saldo contable de cuenta 'Banco'. |
| DEF-LIBRO-HONORARIOS-AUX | Libro de Honorarios Auxiliar: emisión mensual; más certificados de retención anuales (DJ 1879). |
| DEF-MINUTA-EXPLICATIVA | Minuta explicativa: respaldo obligatorio para comprobantes manuales (ajustes/regularizaciones/depreciaciones/correcciones). |
| DEF-ASIENTO-TIPO | Asiento Tipo: asiento contable pre-parametrizado en ERP para operaciones recurrentes. |
| DEF-MATRIZ-DEVENGAMIENTO | Matriz de Devengamiento: parametrización en ERP que asocia imputación presupuestaria (Subtítulo/Ítem/Asig) con asiento contable patrimonial. |

## Manual 1 2 Contabilidad Gubernamental y Cierre Financiero
### ID
GN-MANUAL-CONTAB-ROOT-01
### Obj
- Asegurar integridad contable bajo normativa NICSP y CGR.
- Garantizar registro fidedigno, oportuno y trazable de hechos económicos del Gobierno Regional.
### Seccion I Fundamentos y Marco Normativo
#### ID
GN-MANUAL-CONTAB-S1-01
#### Introduccion y Proposito
#### ID
GN-MANUAL-CONTAB-S1-INTRO-01
#### Purp
- Estandarizar y normar procedimientos contables del Gobierno Regional de Ñuble.
- Asegurar registro de cada transacción financiera según principios de contabilidad sector público y normativa legal vigente.
#### Dest
- Analistas contables.
- Tesoreros.
- Jefaturas.
- DIPIR.
#### Ctx
Guía para operación diaria y procesos críticos de cierre financiero.
#### Ref
DEF-DIPIR
#### Marco Legal Aplicable
#### ID
GN-MANUAL-CONTAB-S1-MARCO-01
#### Req
Gestión contable GORE se rige estrictamente por normativa y regulaciones listadas.
#### Fuentes
-
  #### Src
  Decreto Ley N° 1.263 (1975): Ley Orgánica de Administración Financiera del Estado.
-
  #### Src
  Resolución N° 16 (2015) CGR: aprueba normativa Sistema de Contabilidad General de la Nación (NICSP-CGR).
  #### Ref
  - DEF-CGR
  - DEF-NICSP
-
  #### Src
  Resolución N° 30 (2015) CGR: fija normas sobre rendición de cuentas.
  #### Ref
  DEF-CGR
-
  #### Src
  Oficios Circulares CGR: instrucciones anuales sobre cierres contables y apertura de ejercicio.
  #### Ref
  DEF-CGR
-
  #### Src
  Instrucciones DIPRES: Clasificador Presupuestario y manuales operativos SIGFE.
  #### Ref
  - DEF-DIPRES
  - DEF-SIGFE
#### Glosario de Terminos Contables Clave
#### ID
GN-MANUAL-CONTAB-S1-GLOSARIO-01
#### Terminos
| Ref |
| --- |
| DEF-DEVENGO |
| DEF-NICSP |
| DEF-SIGFE |
| DEF-DEUDA-FLOTANTE |
| DEF-INTEROPERABILIDAD |
### Seccion II Plan de Cuentas y Estructura Contable
#### ID
GN-MANUAL-CONTAB-S2-01
#### Plan de Cuentas Patrimonial CGR
#### ID
GN-MANUAL-CONTAB-S2-PLAN-01
#### Req
GORE adopta integralmente Plan de Cuentas definido por CGR.
#### Ref
DEF-CGR
#### Niveles Jerarquicos
-
  #### Nivel
  Título
  #### Ex
  Ej. 1 ACTIVO
-
  #### Nivel
  Grupo
  #### Ex
  Ej. 11 ACTIVOS CIRCULANTES
-
  #### Nivel
  Subgrupo
  #### Ex
  Ej. 111 DISPONIBILIDADES
-
  #### Nivel
  Cuenta Nivel 1
  #### Ex
  Ej. 11101 BANCO ESTADO
-
  #### Nivel
  Cuenta Nivel 2
  #### Ex
  Ej. 1110101 CUENTA ÚNICA FISCAL
-
  #### Nivel
  Desagregados Institucionales
  #### Def
  Niveles adicionales para control de gestión.
  #### Ex
  Ej. auxiliar por Proyecto/IPR.
#### Cuentas de Orden
#### ID
GN-MANUAL-CONTAB-S2-PLAN-ORDEN-01
#### Def
Control de garantías (boletas, pólizas) y responsabilidades eventuales.
#### Res
No afectan patrimonio directamente; sí responsabilidad administrativa.
#### Configuracion del Ambiente Contable Institucional
#### ID
GN-MANUAL-CONTAB-S2-AMBIENTE-01
#### Centros de Costo
#### ID
GN-MANUAL-CONTAB-S2-CCOSTO-01
#### Def
Catálogo de centros de costo asociado a estructura organizacional (Divisiones/Departamentos) para imputar gastos operativos.
#### Centros de Gestion IPR
#### ID
GN-MANUAL-CONTAB-S2-CGESTION-01
#### Req
Cada IDI funciona como centro de gestión contable; permite balances por proyecto.
#### Asociacion Contable Presupuestaria
#### ID
GN-MANUAL-CONTAB-S2-ASOC-01
#### Req
Matriz de Devengamiento debe mantenerse actualizada en ERP.
#### Mech
- Cada imputación presupuestaria (Subtítulo/Ítem/Asig) genera automáticamente asiento contable patrimonial correcto.
#### Ex
- Gastos en Personal -> Cuenta de Gasto Patrimonial + Pasivo Corriente.
#### Ref
- DEF-MATRIZ-DEVENGAMIENTO
- DEF-ERP
#### Biblioteca de Asientos Contables Memoria Contable
#### ID
GN-MANUAL-CONTAB-S2-ASIENTOS-01
#### Req
ERP opera con Asientos Tipo pre-parametrizados para evitar errores manuales en operaciones recurrentes.
#### Asientos Tipo
| ID | Nombre | Def | Ref |
| --- | --- | --- | --- |
| GN-MANUAL-CONTAB-S2-ASIENTO-REM-01 | Devengo de Remuneraciones | Automático desde módulo SIGPER. | ['DEF-ASIENTO-TIPO', 'DEF-SIGPER'] |
| GN-MANUAL-CONTAB-S2-ASIENTO-BYS-01 | Devengo de Bienes y Servicios | Automático desde módulo Adquisiciones/Activo Fijo. | DEF-ASIENTO-TIPO |
| GN-MANUAL-CONTAB-S2-ASIENTO-ING-01 | Ingresos por Transferencia | Asiento tipo de recepción de aporte fiscal. | DEF-ASIENTO-TIPO |
| GN-MANUAL-CONTAB-S2-ASIENTO-REND-01 | Rendiciones de Cuentas | Asiento tipo para regularizar anticipos. | DEF-ASIENTO-TIPO |
#### Creacion de Nuevos Asientos
#### ID
GN-MANUAL-CONTAB-S2-ASIENTOS-CREA-01
#### Req
Solo Jefe de Finanzas tiene atribución para crear nuevos modelos de asientos.
#### Ref
DEF-JEFE-FINANZAS
### Seccion III Registro y Operacion Contable
#### ID
GN-MANUAL-CONTAB-S3-01
#### Comprobantes Contables
#### ID
GN-MANUAL-CONTAB-S3-COMPROB-01
#### Def
Comprobante Contable es documento fuente único de registro (papel o digital firmado).
#### Ref
DEF-COMPROBANTE-CONTABLE
#### Tipos
-
  #### ID
  GN-MANUAL-CONTAB-S3-COMPROB-AUTO-01
  #### Tipo
  Comprobantes Automáticos (Interfaz)
  #### Def
  Se generan sin intervención humana directa al aprobarse hitos en módulos auxiliares.
  #### Ex
  - Recepción Conforme en Bodega genera el devengo.
-
  #### ID
  GN-MANUAL-CONTAB-S3-COMPROB-MAN-01
  #### Tipo
  Comprobantes Manuales
  #### Prohib
  Uso fuera de: ajustes, regularizaciones, depreciaciones manuales, correcciones de errores.
  #### Req
  - V°B° de jefatura.
  - Adjuntar minuta explicativa.
  #### Ref
  DEF-MINUTA-EXPLICATIVA
#### Validaciones Sistema
#### ID
GN-MANUAL-CONTAB-S3-COMPROB-VAL-01
#### Req
- Sistema bloquea comprobantes descuadrados.
- Sistema bloquea comprobantes que rompan lógica Financiero-Económico.
#### Ex
- Gasto presupuestario sin contrapartida patrimonial de gasto o activo.
#### Centralizacion Contable
#### ID
GN-MANUAL-CONTAB-S3-CENTRALIZACION-01
#### Def
Proceso crítico de integración de sistemas satélites al ERP Financiero.
#### Casos
| ID | Area | Proc | Ref |
| --- | --- | --- | --- |
| GN-MANUAL-CONTAB-S3-CENTRAL-REM-01 | Remuneraciones (SIGPER) | ['Centralizar mensualmente tras cierre de sueldos.', 'Validar integridad total: Monto Bruto = Líquido + Leyes Sociales + Retenciones.'] | DEF-SIGPER |
| GN-MANUAL-CONTAB-S3-CENTRAL-AF-01 | Activo Fijo y Existencias (SIGAS) | ['Entrada de bodega genera alta de activo/existencia + pasivo con proveedor (Facturas por Recibir).', 'Consumo de bodega genera gasto patrimonial.'] | DEF-SIGAS |
| GN-MANUAL-CONTAB-S3-CENTRAL-INTEROP-01 | Interoperabilidad Externa | ['Recepción automática de decretos de modificación presupuestaria desde DIPRES (si tecnología lo permite).', 'Recepción de cartolas bancarias.'] | ['DEF-DIPRES', 'DEF-INTEROPERABILIDAD'] |
#### Gestion de Honorarios
#### ID
GN-MANUAL-CONTAB-S3-HONOR-01
#### Def
Registro de prestaciones de servicios personales (boletas de honorarios).
#### Proc
- Importación de Boletas Electrónicas desde SII.
- Cálculo automático de retención (tasa vigente).
- Generación de obligación de pago (Devengo) y cuentas por pagar.
- Emisión mensual Libro de Honorarios Auxiliar.
- Emisión certificados de retención anuales (DJ 1879).
#### Ref
- DEF-SII
- DEF-DEVENGO
- DEF-LIBRO-HONORARIOS-AUX
#### Gestion de Deuda Institucional
#### ID
GN-MANUAL-CONTAB-S3-DEUDA-01
#### Def
Control de posición financiera.
#### Cuentas por Pagar
#### ID
GN-MANUAL-CONTAB-S3-DEUDA-CXP-01
#### Proc
- Monitoreo de antigüedad de deuda (Aging).
#### Req
Alerta obligatoria sobre facturas devengadas con más de 30 días de antigüedad (cumplimiento Ley Pago a 30 Días).
#### Ref
DEF-DEVENGO
#### Deuda Flotante
#### ID
GN-MANUAL-CONTAB-S3-DEUDA-DF-01
#### Req
Al cierre de año: segregación clara de compromisos devengados no pagados para imputación a caja del año siguiente.
#### Ref
- DEF-DEUDA-FLOTANTE
- DEF-DEVENGO
#### Anticipos
#### ID
GN-MANUAL-CONTAB-S3-DEUDA-ANT-01
#### Req
Control estricto de Fondos por Rendir y viáticos.
#### Prohib
Nuevos anticipos a funcionarios/proveedores con rendiciones pendientes.
#### Rendiciones Cuentas Externas SISREC
#### ID
GN-MANUAL-CONTAB-S3-DEUDA-SISREC-01
#### Req
Transferencias a terceros (Subtítulos 24 y 33) deben rendirse obligatoriamente vía SISREC (CGR) conforme a Res. Ex. N° 1.858/2023.
#### Proc Contable GORE
-
  #### Paso
  1. Recepción y Derivación
  #### Act
  La UCR (Unidad de Control de Rendiciones) centraliza la recepción y deriva al Referente Técnico-Financiero (RTF).
-
  #### Paso
  2. Revisión Técnica (Analista Otorgante)
  #### Act
  Revisión física y financiera en SISREC. Aprobación o devolución por observaciones.
-
  #### Paso
  3. Firma y Aprobación (Encargado Otorgante)
  #### Act
  Firma del Informe de Aprobación por Jefatura DAF mediante Firma Electrónica Avanzada (FEA).
-
  #### Paso
  4. Contabilización SIGFE
  #### Act
  Descarga del informe aprobado y ejecución del asiento de rendición en SIGFE (Reverso de Anticipos / Reconocimiento de Gasto).
  #### Dln
  2 días hábiles tras aprobación técnica.
#### Ref
- DEF-SISREC
- DEF-CGR
- DEF-SIGFE
### Seccion IV Integracion Bancaria y Conciliacion Contable
#### ID
GN-MANUAL-CONTAB-S4-01
#### Ctx Optional
Procedimientos operativos Tesorería (pagos, ingresos, garantías): Manual 1.3: Tesorería y Gestión de Ingresos (./manual_1_3_tesoreria.md).
#### Administracion de Cuentas Corrientes
#### ID
GN-MANUAL-CONTAB-S4-CC-01
#### Req
Registro único de todas las cuentas corrientes institucionales.
#### Tipos Cuenta
- FNDR
- Operacionales
- Fondos de Terceros
#### Libro Banco
#### ID
GN-MANUAL-CONTAB-S4-CC-LIBRO-01
#### Ref
DEF-LIBRO-BANCO
#### Req
Debe cuadrar diariamente con saldo contable de cuenta 'Banco'.
#### Conciliacion Bancaria
#### ID
GN-MANUAL-CONTAB-S4-CONCIL-01
#### Def
Proceso de control interno para validar disponibilidad real de recursos.
#### Frecuencia
- Diaria para gestión de caja.
- Mensual para cierre contable.
#### Metodo
- Carga electrónica de cartola bancaria (archivo del banco).
- Cruce automático (matcheo) por monto y número de documento.
#### Partidas Conciliatorias
#### Req
Analizar y depurar mensualmente.
#### Casos
- Cheques girados y no cobrados (validar caducidad).
- Depósitos no reconocidos (investigar origen inmediato).
- Cargos bancarios no contabilizados.
#### Informe
#### ID
GN-MANUAL-CONTAB-S4-CONCIL-INF-01
#### Res
Generar Anexo CGR de Conciliación Bancaria firmado por Tesorero y Jefe de Finanzas.
#### Ref
- DEF-CGR
- DEF-TESORERO
- DEF-JEFE-FINANZAS
### Seccion V Procesos de Cierre
#### ID
GN-MANUAL-CONTAB-S5-01
#### Cierre Mensual
#### ID
GN-MANUAL-CONTAB-S5-CM-01
#### Req
Cronograma estricto para asegurar reportes oportunos (ej.: día 10 del mes siguiente).
#### Proc
-
  #### Paso
  1. Cierre de Módulos Auxiliares
  #### Act
  Bodega, Activo Fijo, Remuneraciones, Tesorería (no más cheques con fecha del mes).
-
  #### Paso
  2. Centralización
  #### Act
  Ejecutar interfaces pendientes.
-
  #### Paso
  3. Análisis de Cuentas
  #### Act
  Revisar saldos anómalos (ej.: cuentas de activo con saldo acreedor).
-
  #### Paso
  4. Cuadratura Inter-sistémica
  #### Act
  Saldo Presupuestario vs. Contabilidad Patrimonial.
-
  #### Paso
  5. Generación de Reportes
  #### Res
  - Balance de Comprobación y de Saldos.
  - Informe de Ejecución Presupuestaria.
-
  #### Paso
  6. Envío SIGFE
  #### Act
  Generación y transmisión de XML/API a Contraloría/DIPRES.
  #### Ref
  - DEF-SIGFE
  - DEF-CGR
  - DEF-DIPRES
#### Cierre Anual y Apertura
#### ID
GN-MANUAL-CONTAB-S5-CA-01
#### Def
Proceso de fin de ejercicio.
#### Periodo 13 14
#### ID
GN-MANUAL-CONTAB-S5-CA-P1314-01
#### Req
Uso de períodos de ajuste y cierre según instrucciones CGR.
#### Ref
DEF-CGR
#### Devengo Total
#### ID
GN-MANUAL-CONTAB-S5-CA-DEV-01
#### Req
Asegurar devengo de bienes y servicios recibidos al 31/12, aunque factura llegue después.
#### Ref
DEF-DEVENGO
#### Ajustes
#### ID
GN-MANUAL-CONTAB-S5-CA-AJUSTES-01
#### Items
- Depreciación anual.
- Corrección monetaria (si aplica).
- Provisiones de vacaciones.
- Castigos de deuda incobrable.
#### Asiento de Apertura
#### ID
GN-MANUAL-CONTAB-S5-CA-APERTURA-01
#### Req
Sistema genera automáticamente asiento de apertura del año siguiente (Saldos 31/12 Año X -> Saldos 01/01 Año X+1).
#### Req Continuidad
Garantizar continuidad de saldos patrimoniales.
#### Res
Cuentas de resultado se refunden en 'Resultados Acumulados'.
#### Reporteria Legal
#### ID
GN-MANUAL-CONTAB-S5-REPORT-01
#### Req
Sistema emite nativamente formatos exigidos.
#### Reportes
- Balance de 8 Columnas.
- Estado de Situación Financiera (Balance General Clasificado).
- Estado de Resultados.
- Estado de Flujo de Efectivo (Método Directo).
- Estado de Cambios en el Patrimonio Neto.
- Informe de Pasivos Contingentes.
### Seccion VI Auditoria y Control
#### ID
GN-MANUAL-CONTAB-S6-01
#### Auditoria 360 Pista de Auditoria
#### ID
GN-MANUAL-CONTAB-S6-AUD-01
#### Purp
Principio de 'Quién, Qué, Cuándo'.
#### Req
- Cada comprobante registra usuario creador, usuario aprobador, fecha y hora exacta.
#### Inmutabilidad
#### ID
GN-MANUAL-CONTAB-S6-AUD-INM-01
#### Req
Comprobante Aprobado/Mayorizado NO se edita.
#### Act
Se reversa con otro comprobante contrario.
#### Log de Cambios
#### ID
GN-MANUAL-CONTAB-S6-AUD-LOG-01
#### Req
Log de cambios para datos maestros.
#### Ex
- Cambio de cuenta bancaria de proveedor.
#### Ref
DEF-COMPROBANTE-CONTABLE
#### Seguridad
#### ID
GN-MANUAL-CONTAB-S6-SEG-01
#### Segregacion de Funciones
#### ID
GN-MANUAL-CONTAB-S6-SEG-SF-01
#### Req
- Quien solicita gasto no debe ser quien lo aprueba.
- Quien gira pago no debe ser quien concilia el banco.
#### Credenciales
#### ID
GN-MANUAL-CONTAB-S6-SEG-CRED-01
#### Req
Claves únicas e intransferibles.
### Warn
#### ID
GN-MANUAL-CONTAB-WARN-VIVO-01
#### Warn
Documento vivo: debe actualizarse ante cambios en normativa NICSP-CGR o en sistemas de información del GORE.
#### Ref
- DEF-NICSP
- DEF-CGR

## Referencias Cruzadas
### ID
GN-MANUAL-CONTAB-XREF-01
### Ctx Optional
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_1_presupuesto.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_3_tesoreria_koda.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_2_inventarios.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_3_activo_fijo.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_2_remuneraciones.yml
