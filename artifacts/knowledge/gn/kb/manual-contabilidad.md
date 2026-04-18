---
_manifest:
  urn: urn:gn:kb:manual-contabilidad
  provenance:
    created_by: FS
    created_at: '2026-03-15'
    source: Manual 1.2 Contabilidad Gubernamental y Cierre Financiero GORE Ñuble
version: 1.0.0
status: published
tags:
- contabilidad
- cierre-financiero
- gore-nuble
- nicsp
- sigfe
lang: es
extensions:
  gn:
    family: guide
relations:
  cites:
  - urn:gn:kb:gestion-rendiciones
---


# Contabilidad Gubernamental y Cierre Financiero — GORE Ñuble

## Visión General

Manual operativo de contabilidad gubernamental del GORE Ñuble. Estandariza los procedimientos contables para asegurar el registro fidedigno, oportuno y trazable de todos los hechos económicos del Gobierno Regional, bajo normativa NICSP y CGR. Cubre el plan de cuentas patrimonial, configuración contable institucional, registro y operación diaria, integración bancaria, procesos de cierre mensual y anual, reportería legal y controles de auditoría.

**Destinatarios:** analistas contables, tesoreros, jefaturas y DIPIR (División de Presupuesto e Inversión Regional).

## Glosario

| Término | Definición |
| :--- | :--- |
| CGR | Contraloría General de la República |
| DIPRES | Dirección de Presupuestos |
| DIPIR | División de Presupuesto e Inversión Regional |
| NICSP | Normas Internacionales de Contabilidad para el Sector Público; base del estándar contable chileno |
| SIGFE | Sistema de Información para la Gestión Financiera del Estado (agregador central) |
| ERP | Sistema ERP financiero institucional; mantiene Matriz de Devengamiento y asientos patrimoniales |
| SIGPER | Módulo/sistema de remuneraciones |
| SIGAS | Módulo/sistema de activo fijo y existencias (bodega) |
| SII | Servicio de Impuestos Internos (boletas electrónicas de honorarios) |
| SISREC | Sistema de Rendición Electrónica de Cuentas de CGR |
| Devengo | Reconocimiento de una obligación de pago o derecho de cobro, independiente de la fecha efectiva de pago o recaudación |
| Deuda Flotante | Obligaciones devengadas y no pagadas al cierre del ejercicio |
| Interoperabilidad | Capacidad de intercambiar información financiera automáticamente entre sistemas (ej.: ERP <-> Banco) |
| Comprobante Contable | Documento fuente único de registro (papel o digital firmado) |
| Libro Banco | Registro cronológico de movimientos bancarios; debe cuadrar diariamente con saldo contable de cuenta "Banco" |
| Libro de Honorarios Auxiliar | Emisión mensual; incluye certificados de retención anuales (DJ 1879) |
| Minuta Explicativa | Respaldo obligatorio para comprobantes manuales (ajustes, regularizaciones, depreciaciones, correcciones) |
| Asiento Tipo | Asiento contable pre-parametrizado en ERP para operaciones recurrentes |
| Matriz de Devengamiento | Parametrización en ERP que asocia imputación presupuestaria (Subtítulo/Ítem/Asig) con asiento contable patrimonial |

## Marco Normativo

La gestión contable del GORE se rige estrictamente por la siguiente normativa:

| Norma | Alcance |
| :--- | :--- |
| Decreto Ley N°1.263 (1975) | Ley Orgánica de Administración Financiera del Estado |
| Resolución N°16 (2015) CGR | Aprueba normativa del Sistema de Contabilidad General de la Nación (NICSP-CGR) |
| Resolución N°30 (2015) CGR | Fija normas sobre rendición de cuentas |
| Oficios Circulares CGR | Instrucciones anuales sobre cierres contables y apertura de ejercicio |
| Instrucciones DIPRES | Clasificador Presupuestario y manuales operativos SIGFE |

## Plan de Cuentas Patrimonial

El GORE adopta integralmente el Plan de Cuentas definido por CGR. La estructura jerárquica tiene 6 niveles:

| Nivel | Nombre | Ejemplo |
| :--- | :--- | :--- |
| 1 | Título | 1 ACTIVO |
| 2 | Grupo | 11 ACTIVOS CIRCULANTES |
| 3 | Subgrupo | 111 DISPONIBILIDADES |
| 4 | Cuenta Nivel 1 | 11101 BANCO ESTADO |
| 5 | Cuenta Nivel 2 | 1110101 CUENTA ÚNICA FISCAL |
| 6 | Desagregados Institucionales | Auxiliar por Proyecto/IPR (niveles adicionales para control de gestión) |

### Cuentas de Orden

Control de garantías (boletas, pólizas) y responsabilidades eventuales. No afectan patrimonio directamente, pero sí generan responsabilidad administrativa.

## Configuración Contable Institucional

### Centros de costo

Catálogo de centros de costo asociado a la estructura organizacional (Divisiones/Departamentos) para imputar gastos operativos.

### Centros de gestión IPR

Cada IDI funciona como centro de gestión contable, lo que permite generar balances por proyecto.

### Asociación contable-presupuestaria (Matriz de Devengamiento)

La Matriz de Devengamiento debe mantenerse actualizada en el ERP. Cada imputación presupuestaria (Subtítulo/Ítem/Asig) genera automáticamente el asiento contable patrimonial correcto.

**Ejemplo:** Gastos en Personal genera Cuenta de Gasto Patrimonial + Pasivo Corriente.

## Biblioteca de Asientos Tipo

El ERP opera con Asientos Tipo pre-parametrizados para evitar errores manuales en operaciones recurrentes.

| Asiento Tipo | Descripción |
| :--- | :--- |
| Devengo de Remuneraciones | Automático desde módulo SIGPER |
| Devengo de Bienes y Servicios | Automático desde módulo Adquisiciones/Activo Fijo |
| Ingresos por Transferencia | Asiento tipo de recepción de aporte fiscal |
| Rendiciones de Cuentas | Asiento tipo para regularizar anticipos |

### Creación de nuevos asientos tipo

Solo el Jefe de Finanzas tiene atribución para crear nuevos modelos de asientos tipo.

## Registro y Operación Contable

### Comprobantes contables

El Comprobante Contable es el documento fuente único de registro (papel o digital firmado).

**Comprobantes automáticos (interfaz):** se generan sin intervención humana directa al aprobarse hitos en módulos auxiliares. Ejemplo: Recepción Conforme en Bodega genera el devengo.

**Comprobantes manuales:** uso restringido exclusivamente a ajustes, regularizaciones, depreciaciones manuales y correcciones de errores. Requisitos:

- V°B° de jefatura.
- Adjuntar minuta explicativa.

**Validaciones del sistema:**

- El sistema bloquea comprobantes descuadrados.
- El sistema bloquea comprobantes que rompan lógica Financiero-Económico (ej.: gasto presupuestario sin contrapartida patrimonial de gasto o activo).

### Centralización contable

Proceso crítico de integración de sistemas satélites al ERP Financiero.

**Remuneraciones (SIGPER):**

- Centralizar mensualmente tras cierre de sueldos.
- Validar integridad total: Monto Bruto = Líquido + Leyes Sociales + Retenciones.

**Activo Fijo y Existencias (SIGAS):**

- Entrada de bodega genera alta de activo/existencia + pasivo con proveedor (Facturas por Recibir).
- Consumo de bodega genera gasto patrimonial.

**Interoperabilidad externa:**

- Recepción automática de decretos de modificación presupuestaria desde DIPRES (si la tecnología lo permite).
- Recepción de cartolas bancarias.

### Gestión de honorarios

Registro de prestaciones de servicios personales (boletas de honorarios). Procedimiento:

1. Importación de boletas electrónicas desde SII.
2. Cálculo automático de retención (tasa vigente).
3. Generación de obligación de pago (devengo) y cuentas por pagar.
4. Emisión mensual del Libro de Honorarios Auxiliar.
5. Emisión de certificados de retención anuales (DJ 1879).

## Gestión de Deuda Institucional

Control de posición financiera del GORE.

### Cuentas por pagar

- Monitoreo de antigüedad de deuda (Aging).
- **Alerta obligatoria** sobre facturas devengadas con más de 30 días de antigüedad (cumplimiento Ley Pago a 30 Días).

### Deuda flotante

Al cierre de año: segregación clara de compromisos devengados no pagados para imputación a caja del año siguiente.

### Anticipos

Control estricto de Fondos por Rendir y viáticos. **Prohibición:** no se otorgan nuevos anticipos a funcionarios o proveedores con rendiciones pendientes.

### Tratamiento contable de rendiciones SISREC

Las transferencias a terceros (Subtítulos 24 y 33) deben rendirse obligatoriamente vía SISREC (CGR) conforme a Res. Ex. N°1.858/2023. Para el flujo completo del proceso de rendición (roles, SLAs, tipología de fondos, documentación), ver [urn:gn:kb:gestion-rendiciones](urn:gn:kb:gestion-rendiciones).

Esta sección describe exclusivamente el tratamiento contable que ejecuta la DAF al recibir una rendición aprobada:

Proceso contable GORE:

| Paso | Actividad | Plazo |
| :--- | :--- | :--- |
| 1. Recepción y Derivación | La UCR (Unidad de Control de Rendiciones) centraliza la recepción y deriva al Referente Técnico-Financiero (RTF) | — |
| 2. Revisión Técnica | Analista Otorgante realiza revisión física y financiera en SISREC; aprobación o devolución por observaciones | — |
| 3. Firma y Aprobación | Jefatura DAF firma el Informe de Aprobación mediante Firma Electrónica Avanzada (FEA) | — |
| 4. Contabilización SIGFE | Descarga del informe aprobado y ejecución del asiento de rendición en SIGFE (reverso de anticipos / reconocimiento de gasto) | 2 días hábiles tras aprobación técnica |

## Integración Bancaria y Conciliación

### Administración de cuentas corrientes

Registro único de todas las cuentas corrientes institucionales. Tipos de cuenta:

- FNDR
- Operacionales
- Fondos de Terceros

**Libro Banco:** registro cronológico de movimientos bancarios. Debe cuadrar diariamente con el saldo contable de la cuenta "Banco".

### Conciliación bancaria

Proceso de control interno para validar la disponibilidad real de recursos.

**Frecuencia:**

- Diaria para gestión de caja.
- Mensual para cierre contable.

**Método:**

1. Carga electrónica de cartola bancaria (archivo del banco).
2. Cruce automático (matcheo) por monto y número de documento.

**Partidas conciliatorias** — se analizan y depuran mensualmente:

- Cheques girados y no cobrados (validar caducidad).
- Depósitos no reconocidos (investigar origen inmediato).
- Cargos bancarios no contabilizados.

**Informe:** generar Anexo CGR de Conciliación Bancaria firmado por Tesorero y Jefe de Finanzas.

## Procesos de Cierre

### Cierre mensual

Cronograma estricto para asegurar reportes oportunos (ej.: día 10 del mes siguiente).

| Paso | Actividad |
| :--- | :--- |
| 1 | **Cierre de módulos auxiliares:** Bodega, Activo Fijo, Remuneraciones, Tesorería (no más cheques con fecha del mes) |
| 2 | **Centralización:** ejecutar interfaces pendientes |
| 3 | **Análisis de cuentas:** revisar saldos anómalos (ej.: cuentas de activo con saldo acreedor) |
| 4 | **Cuadratura inter-sistémica:** Saldo Presupuestario vs. Contabilidad Patrimonial |
| 5 | **Generación de reportes:** Balance de Comprobación y de Saldos; Informe de Ejecución Presupuestaria |
| 6 | **Envío SIGFE:** generación y transmisión de XML/API a CGR/DIPRES |

### Cierre anual y apertura

Proceso de fin de ejercicio.

**Períodos 13 y 14:** uso de períodos de ajuste y cierre según instrucciones CGR.

**Devengo total:** asegurar devengo de bienes y servicios recibidos al 31/12, aunque la factura llegue después.

**Ajustes de cierre:**

- Depreciación anual.
- Corrección monetaria (si aplica).
- Provisiones de vacaciones.
- Castigos de deuda incobrable.

**Asiento de apertura:** el sistema genera automáticamente el asiento de apertura del año siguiente (Saldos 31/12 Año X -> Saldos 01/01 Año X+1). Las cuentas de resultado se refunden en "Resultados Acumulados". Se debe garantizar la continuidad de saldos patrimoniales.

## Reportería Legal

El sistema emite nativamente los siguientes formatos exigidos:

1. Balance de 8 Columnas.
2. Estado de Situación Financiera (Balance General Clasificado).
3. Estado de Resultados.
4. Estado de Flujo de Efectivo (Método Directo).
5. Estado de Cambios en el Patrimonio Neto.
6. Informe de Pasivos Contingentes.

## Auditoría y Control

### Pista de auditoría

Principio "Quién, Qué, Cuándo": cada comprobante registra usuario creador, usuario aprobador, fecha y hora exacta.

**Inmutabilidad:** un Comprobante Aprobado/Mayorizado no se edita. Si requiere corrección, se reversa con otro comprobante contrario.

**Log de cambios:** registro obligatorio para modificaciones en datos maestros (ej.: cambio de cuenta bancaria de proveedor).

### Seguridad

**Segregación de funciones:**

- Quien solicita gasto no debe ser quien lo aprueba.
- Quien gira pago no debe ser quien concilia el banco.

**Credenciales:** claves únicas e intransferibles.

---

> Documento vivo: debe actualizarse ante cambios en normativa NICSP-CGR o en sistemas de información del GORE.
