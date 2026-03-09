---
_manifest:
  urn: urn:gn:kb:manual-contabilidad
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
    source: domains/gn/03_operacion/gestion/kb_gn_044_manual_contabilidad_koda.yml
version: 2.0.0
status: published
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
    cr: 3.36
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 3
    meat_count: 296
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/manuales__manual-contabilidad.md.json
---

# Manual 1.2: Contabilidad Gubernamental y Cierre Financiero
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
### Objetivos
- Asegurar integridad contable bajo normativa NICSP y CGR.
- Garantizar registro fidedigno, oportuno y trazable de hechos económicos del Gobierno Regional.
### Seccion I Fundamentos y Marco Normativo
#### Introduccion y Proposito
#### Proposito
- Estandarizar y normar procedimientos contables del Gobierno Regional de Ñuble.
- Asegurar registro de cada transacción financiera según principios de contabilidad sector público y normativa legal vigente.
#### Dest
- Analistas contables.
- Tesoreros.
- Jefaturas.
- DIPIR.
#### Contexto
Guía para operación diaria y procesos críticos de cierre financiero.
#### Referencias
DEF-DIPIR
#### Marco Legal Aplicable
#### Requisitos
Gestión contable GORE se rige estrictamente por normativa y regulaciones listadas.
#### Fuentes
| Src | Ref |
| --- | --- |
| Decreto Ley N° 1.263 (1975): Ley Orgánica de Administración Financiera del Estado. |  |
| Resolución N° 16 (2015) CGR: aprueba normativa Sistema de Contabilidad General de la Nación (NICSP-CGR). | DEF-CGR, DEF-NICSP |
| Resolución N° 30 (2015) CGR: fija normas sobre rendición de cuentas. | DEF-CGR |
| Oficios Circulares CGR: instrucciones anuales sobre cierres contables y apertura de ejercicio. | DEF-CGR |
| Instrucciones DIPRES: Clasificador Presupuestario y manuales operativos SIGFE. | DEF-DIPRES, DEF-SIGFE |
#### Glosario de Terminos Contables Clave
#### Terminos
| Ref |
| --- |
| DEF-DEVENGO |
| DEF-NICSP |
| DEF-SIGFE |
| DEF-DEUDA-FLOTANTE |
| DEF-INTEROPERABILIDAD |
### Seccion II Plan de Cuentas y Estructura Contable
#### Plan de Cuentas Patrimonial CGR
#### Requisitos
GORE adopta integralmente Plan de Cuentas definido por CGR.
#### Referencias
DEF-CGR
#### Niveles Jerarquicos
| Nivel | Ex |
| --- | --- |
| Título | Ej. 1 ACTIVO |
| Grupo | Ej. 11 ACTIVOS CIRCULANTES |
| Subgrupo | Ej. 111 DISPONIBILIDADES |
| Cuenta Nivel 1 | Ej. 11101 BANCO ESTADO |
| Cuenta Nivel 2 | Ej. 1110101 CUENTA ÚNICA FISCAL |
| Desagregados Institucionales | Ej. auxiliar por Proyecto/IPR. |
#### Cuentas de Orden
#### Definicion
Control de garantías (boletas, pólizas) y responsabilidades eventuales.
#### Resultados
No afectan patrimonio directamente; sí responsabilidad administrativa.
#### Configuracion del Ambiente Contable Institucional
#### Centros de Costo
#### Definicion
Catálogo de centros de costo asociado a estructura organizacional (Divisiones/Departamentos) para imputar gastos operativos.
#### Centros de Gestion IPR
#### Requisitos
Cada IDI funciona como centro de gestión contable; permite balances por proyecto.
#### Asociacion Contable Presupuestaria
#### Requisitos
Matriz de Devengamiento debe mantenerse actualizada en ERP.
#### Mecanismo
- Cada imputación presupuestaria (Subtítulo/Ítem/Asig) genera automáticamente asiento contable patrimonial correcto.
#### Ex
- Gastos en Personal -> Cuenta de Gasto Patrimonial + Pasivo Corriente.
#### Referencias
- DEF-MATRIZ-DEVENGAMIENTO
- DEF-ERP
#### Biblioteca de Asientos Contables Memoria Contable
#### Requisitos
ERP opera con Asientos Tipo pre-parametrizados para evitar errores manuales en operaciones recurrentes.
#### Asientos Tipo
| ID | Nombre | Def | Ref |
| --- | --- | --- | --- |
| GN-MANUAL-CONTAB-S2-ASIENTO-REM-01 | Devengo de Remuneraciones | Automático desde módulo SIGPER. | DEF-ASIENTO-TIPO, DEF-SIGPER |
| GN-MANUAL-CONTAB-S2-ASIENTO-BYS-01 | Devengo de Bienes y Servicios | Automático desde módulo Adquisiciones/Activo Fijo. | DEF-ASIENTO-TIPO |
| GN-MANUAL-CONTAB-S2-ASIENTO-ING-01 | Ingresos por Transferencia | Asiento tipo de recepción de aporte fiscal. | DEF-ASIENTO-TIPO |
| GN-MANUAL-CONTAB-S2-ASIENTO-REND-01 | Rendiciones de Cuentas | Asiento tipo para regularizar anticipos. | DEF-ASIENTO-TIPO |
#### Creacion de Nuevos Asientos
#### Requisitos
Solo Jefe de Finanzas tiene atribución para crear nuevos modelos de asientos.
#### Referencias
DEF-JEFE-FINANZAS
### Seccion III Registro y Operacion Contable
#### Comprobantes Contables
#### Definicion
Comprobante Contable es documento fuente único de registro (papel o digital firmado).
#### Referencias
DEF-COMPROBANTE-CONTABLE
#### Tipos
| ID | Tipo | Def | Ex | Prohib | Req | Ref |
| --- | --- | --- | --- | --- | --- | --- |
| GN-MANUAL-CONTAB-S3-COMPROB-AUTO-01 | Comprobantes Automáticos (Interfaz) | Se generan sin intervención humana directa al aprobarse hitos en módulos auxiliares. | Recepción Conforme en Bodega genera el devengo. |  |  |  |
| GN-MANUAL-CONTAB-S3-COMPROB-MAN-01 | Comprobantes Manuales |  |  | Uso fuera de: ajustes, regularizaciones, depreciaciones manuales, correcciones de errores. | V°B° de jefatura., Adjuntar minuta explicativa. | DEF-MINUTA-EXPLICATIVA |
#### Validaciones Sistema
#### Requisitos
- Sistema bloquea comprobantes descuadrados.
- Sistema bloquea comprobantes que rompan lógica Financiero-Económico.
#### Ex
- Gasto presupuestario sin contrapartida patrimonial de gasto o activo.
#### Centralizacion Contable
#### Definicion
Proceso crítico de integración de sistemas satélites al ERP Financiero.
#### Casos
| ID | Area | Proc | Ref |
| --- | --- | --- | --- |
| GN-MANUAL-CONTAB-S3-CENTRAL-REM-01 | Remuneraciones (SIGPER) | Centralizar mensualmente tras cierre de sueldos., Validar integridad total: Monto Bruto = Líquido + Leyes Sociales + Retenciones. | DEF-SIGPER |
| GN-MANUAL-CONTAB-S3-CENTRAL-AF-01 | Activo Fijo y Existencias (SIGAS) | Entrada de bodega genera alta de activo/existencia + pasivo con proveedor (Facturas por Recibir)., Consumo de bodega genera gasto patrimonial. | DEF-SIGAS |
| GN-MANUAL-CONTAB-S3-CENTRAL-INTEROP-01 | Interoperabilidad Externa | Recepción automática de decretos de modificación presupuestaria desde DIPRES (si tecnología lo permite)., Recepción de cartolas bancarias. | DEF-DIPRES, DEF-INTEROPERABILIDAD |
#### Gestion de Honorarios
#### Definicion
Registro de prestaciones de servicios personales (boletas de honorarios).
#### Proceso
- Importación de Boletas Electrónicas desde SII.
- Cálculo automático de retención (tasa vigente).
- Generación de obligación de pago (Devengo) y cuentas por pagar.
- Emisión mensual Libro de Honorarios Auxiliar.
- Emisión certificados de retención anuales (DJ 1879).
#### Referencias
- DEF-SII
- DEF-DEVENGO
- DEF-LIBRO-HONORARIOS-AUX
#### Gestion de Deuda Institucional
#### Definicion
Control de posición financiera.
#### Cuentas por Pagar
#### Proceso
- Monitoreo de antigüedad de deuda (Aging).
#### Requisitos
Alerta obligatoria sobre facturas devengadas con más de 30 días de antigüedad (cumplimiento Ley Pago a 30 Días).
#### Referencias
DEF-DEVENGO
#### Deuda Flotante
#### Requisitos
Al cierre de año: segregación clara de compromisos devengados no pagados para imputación a caja del año siguiente.
#### Referencias
- DEF-DEUDA-FLOTANTE
- DEF-DEVENGO
#### Anticipos
#### Requisitos
Control estricto de Fondos por Rendir y viáticos.
#### Prohibiciones
Nuevos anticipos a funcionarios/proveedores con rendiciones pendientes.
#### Rendiciones Cuentas Externas SISREC
#### Requisitos
Transferencias a terceros (Subtítulos 24 y 33) deben rendirse obligatoriamente vía SISREC (CGR) conforme a Res. Ex. N° 1.858/2023.
#### Proc Contable GORE
| Paso | Act |
| --- | --- |
| 1. Recepción y Derivación | La UCR (Unidad de Control de Rendiciones) centraliza la recepción y deriva al Referente Técnico-Financiero (RTF). |
| 2. Revisión Técnica (Analista Otorgante) | Revisión física y financiera en SISREC. Aprobación o devolución por observaciones. |
| 3. Firma y Aprobación (Encargado Otorgante) | Firma del Informe de Aprobación por Jefatura DAF mediante Firma Electrónica Avanzada (FEA). |
| 4. Contabilización SIGFE | Descarga del informe aprobado y ejecución del asiento de rendición en SIGFE (Reverso de Anticipos / Reconocimiento de Gasto). |
#### Referencias
- DEF-SISREC
- DEF-CGR
- DEF-SIGFE
### Seccion IV Integracion Bancaria y Conciliacion Contable
#### Contexto opcional
Procedimientos operativos Tesorería (pagos, ingresos, garantías): Manual 1.3: Tesorería y Gestión de Ingresos (./manual_1_3_tesoreria.md).
#### Administracion de Cuentas Corrientes
#### Requisitos
Registro único de todas las cuentas corrientes institucionales.
#### Tipos Cuenta
- FNDR
- Operacionales
- Fondos de Terceros
#### Libro Banco
#### Referencias
DEF-LIBRO-BANCO
#### Requisitos
Debe cuadrar diariamente con saldo contable de cuenta 'Banco'.
#### Conciliacion Bancaria
#### Definicion
Proceso de control interno para validar disponibilidad real de recursos.
#### Frecuencia
- Diaria para gestión de caja.
- Mensual para cierre contable.
#### Metodo
- Carga electrónica de cartola bancaria (archivo del banco).
- Cruce automático (matcheo) por monto y número de documento.
#### Partidas Conciliatorias
#### Requisitos
Analizar y depurar mensualmente.
#### Casos
- Cheques girados y no cobrados (validar caducidad).
- Depósitos no reconocidos (investigar origen inmediato).
- Cargos bancarios no contabilizados.
#### Informe
#### Resultados
Generar Anexo CGR de Conciliación Bancaria firmado por Tesorero y Jefe de Finanzas.
#### Referencias
- DEF-CGR
- DEF-TESORERO
- DEF-JEFE-FINANZAS
### Seccion V Procesos de Cierre
#### Cierre Mensual
#### Requisitos
Cronograma estricto para asegurar reportes oportunos (ej.: día 10 del mes siguiente).
#### Proceso
| Paso | Act |
| --- | --- |
| 1. Cierre de Módulos Auxiliares | Bodega, Activo Fijo, Remuneraciones, Tesorería (no más cheques con fecha del mes). |
| 2. Centralización | Ejecutar interfaces pendientes. |
| 3. Análisis de Cuentas | Revisar saldos anómalos (ej.: cuentas de activo con saldo acreedor). |
| 4. Cuadratura Inter-sistémica | Saldo Presupuestario vs. Contabilidad Patrimonial. |
| 5. Generación de Reportes |  |
| 6. Envío SIGFE | Generación y transmisión de XML/API a Contraloría/DIPRES. |
#### Cierre Anual y Apertura
#### Definicion
Proceso de fin de ejercicio.
#### Periodo 13 14
#### Requisitos
Uso de períodos de ajuste y cierre según instrucciones CGR.
#### Referencias
DEF-CGR
#### Devengo Total
#### Requisitos
Asegurar devengo de bienes y servicios recibidos al 31/12, aunque factura llegue después.
#### Referencias
DEF-DEVENGO
#### Ajustes
#### Items
- Depreciación anual.
- Corrección monetaria (si aplica).
- Provisiones de vacaciones.
- Castigos de deuda incobrable.
#### Asiento de Apertura
#### Requisitos
Sistema genera automáticamente asiento de apertura del año siguiente (Saldos 31/12 Año X -> Saldos 01/01 Año X+1).
#### Req Continuidad
Garantizar continuidad de saldos patrimoniales.
#### Resultados
Cuentas de resultado se refunden en 'Resultados Acumulados'.
#### Reporteria Legal
#### Requisitos
Sistema emite nativamente formatos exigidos.
#### Reportes
- Balance de 8 Columnas.
- Estado de Situación Financiera (Balance General Clasificado).
- Estado de Resultados.
- Estado de Flujo de Efectivo (Método Directo).
- Estado de Cambios en el Patrimonio Neto.
- Informe de Pasivos Contingentes.
### Seccion VI Auditoria y Control
#### Auditoria 360 Pista de Auditoria
#### Proposito
Principio de 'Quién, Qué, Cuándo'.
#### Requisitos
- Cada comprobante registra usuario creador, usuario aprobador, fecha y hora exacta.
#### Inmutabilidad
#### Requisitos
Comprobante Aprobado/Mayorizado NO se edita.
#### Acciones
Se reversa con otro comprobante contrario.
#### Log de Cambios
#### Requisitos
Log de cambios para datos maestros.
#### Ex
- Cambio de cuenta bancaria de proveedor.
#### Referencias
DEF-COMPROBANTE-CONTABLE
#### Seguridad
#### Segregacion de Funciones
#### Requisitos
- Quien solicita gasto no debe ser quien lo aprueba.
- Quien gira pago no debe ser quien concilia el banco.
#### Credenciales
#### Requisitos
Claves únicas e intransferibles.
### Advertencias
#### Advertencias
Documento vivo: debe actualizarse ante cambios en normativa NICSP-CGR o en sistemas de información del GORE.
#### Referencias
- DEF-NICSP
- DEF-CGR

## Referencias Cruzadas
### Contexto opcional
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_1_presupuesto.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_3_tesoreria_koda.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_2_inventarios.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_3_activo_fijo.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_2_remuneraciones.yml
