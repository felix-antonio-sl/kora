---
_manifest:
  urn: urn:gn:kb:manual-contabilidad
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: "GORE Ñuble"
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
---

# Manual 1.2: Contabilidad Gubernamental y Cierre Financiero

Objetivo: Asegurar integridad contable bajo normativa NICSP y CGR; garantizar registro fidedigno, oportuno y trazable de hechos económicos del GORE Ñuble en operación diaria y procesos críticos de cierre financiero.

Siglas: CGR = Contraloría General de la República · DIPRES = Dirección de Presupuestos · DIPIR = División de Presupuesto e Inversión Regional · NICSP = Normas Internacionales de Contabilidad del Sector Público · SIGFE = Sistema de Información para la Gestión Financiera del Estado · ERP = sistema ERP financiero institucional · SIGPER = sistema de remuneraciones · SIGAS = sistema de activo fijo y existencias · SII = Servicio de Impuestos Internos · SISREC = Sistema de Rendición Electrónica de Cuentas CGR · DAF = División de Administración y Finanzas · UCR = Unidad de Control de Rendiciones · RTF = Referente Técnico-Financiero · FEA = Firma Electrónica Avanzada.

## Marco Normativo

| Fuente | Contenido |
|--------|-----------|
| DL N° 1.263 (1975) | Ley Orgánica de Administración Financiera del Estado |
| Resolución N° 16 (2015) CGR | Aprueba normativa Sistema de Contabilidad General de la Nación (NICSP-CGR) |
| Resolución N° 30 (2015) CGR | Normas sobre rendición de cuentas |
| Oficios Circulares CGR | Instrucciones anuales sobre cierres contables y apertura de ejercicio |
| Instrucciones DIPRES | Clasificador Presupuestario y manuales operativos SIGFE |

**Conceptos clave:**
- Devengo: reconocimiento de obligación de pago o derecho de cobro, independiente de fecha efectiva de pago o recaudación.
- Deuda Flotante: obligaciones devengadas y no pagadas al cierre del ejercicio.
- Matriz de Devengamiento: parametrización en ERP que asocia imputación presupuestaria (Subtítulo/Ítem/Asig) con asiento contable patrimonial.
- Asiento Tipo: asiento contable pre-parametrizado en ERP para operaciones recurrentes.
- Comprobante Contable: documento fuente único de registro (papel o digital firmado).
- Libro Banco: registro cronológico de movimientos bancarios; debe cuadrar diariamente con saldo contable de cuenta "Banco".

## Plan de Cuentas y Estructura Contable

**Plan de Cuentas CGR (adoptado integralmente por el GORE):**

| Nivel | Ejemplo |
|-------|---------|
| Título | 1 ACTIVO |
| Grupo | 11 ACTIVOS CIRCULANTES |
| Subgrupo | 111 DISPONIBILIDADES |
| Cuenta Nivel 1 | 11101 BANCO ESTADO |
| Cuenta Nivel 2 | 1110101 CUENTA ÚNICA FISCAL |
| Desagregados institucionales | Auxiliar por Proyecto/IPR |

Cuentas de Orden: control de garantías (boletas, pólizas) y responsabilidades eventuales; no afectan patrimonio directamente; sí responsabilidad administrativa.

**Configuración del ambiente contable:**
- Centros de costo: catálogo asociado a estructura organizacional (Divisiones/Departamentos) para imputar gastos operativos.
- Centros de gestión IPR: cada IDI funciona como centro de gestión contable; permite balances por proyecto.
- Asociación contable-presupuestaria: Matriz de Devengamiento actualizada en ERP; cada imputación presupuestaria genera automáticamente asiento contable patrimonial correcto.

**Asientos Tipo pre-parametrizados:**

| Asiento | Fuente |
|---------|--------|
| Devengo de Remuneraciones | Automático desde módulo SIGPER |
| Devengo de Bienes y Servicios | Automático desde módulo Adquisiciones/Activo Fijo |
| Ingresos por Transferencia | Asiento tipo de recepción de aporte fiscal |
| Rendiciones de Cuentas | Asiento tipo para regularizar anticipos |

Creación de nuevos asientos: solo Jefe de Finanzas tiene atribución.

## Registro y Operación Contable

**Comprobantes contables:**
- Automáticos (Interfaz): se generan sin intervención humana directa al aprobarse hitos en módulos auxiliares (ej. Recepción Conforme en Bodega genera el devengo).
- Manuales: solo para ajustes, regularizaciones, depreciaciones manuales y correcciones de errores. Requieren V°B° de jefatura y minuta explicativa adjunta.
- Validaciones del sistema: bloquea comprobantes descuadrados y bloquea lógica Financiero-Económico (ej. gasto presupuestario sin contrapartida patrimonial).

**Centralización contable** (integración de sistemas satélites al ERP Financiero):

| Área | Procedimiento |
|------|--------------|
| Remuneraciones (SIGPER) | Centralizar mensualmente tras cierre de sueldos; validar integridad total: Monto Bruto = Líquido + Leyes Sociales + Retenciones |
| Activo Fijo y Existencias (SIGAS) | Entrada de bodega genera alta de activo/existencia + pasivo con proveedor (Facturas por Recibir); consumo de bodega genera gasto patrimonial |
| Interoperabilidad Externa | Recepción automática de decretos de modificación presupuestaria desde DIPRES; recepción de cartolas bancarias |

**Gestión de honorarios:** Importación de Boletas Electrónicas desde SII → cálculo automático de retención (tasa vigente) → generación de obligación de pago (Devengo) y cuentas por pagar → emisión mensual Libro de Honorarios Auxiliar → emisión certificados de retención anuales (DJ 1879).

**Gestión de deuda institucional:**
- Cuentas por Pagar: monitoreo de antigüedad (Aging); alerta obligatoria sobre facturas devengadas con más de 30 días de antigüedad (Ley Pago a 30 Días).
- Deuda Flotante: al cierre de año, segregación clara de compromisos devengados no pagados para imputación a caja del año siguiente.
- Anticipos: control estricto de Fondos por Rendir y viáticos; prohibido nuevos anticipos a funcionarios/proveedores con rendiciones pendientes.

**Rendiciones externas (SISREC):** Transferencias a terceros (Subtítulos 24 y 33) deben rendirse vía SISREC (CGR), conforme a Res. Ex. N° 1.858/2023.

| Paso | Responsable | Acción |
|------|-------------|--------|
| 1. Recepción y Derivación | UCR | Centraliza la recepción y deriva al RTF |
| 2. Revisión Técnica | Analista Otorgante | Revisión física y financiera en SISREC; aprobación o devolución por observaciones |
| 3. Firma y Aprobación | Encargado Otorgante (Jefatura DAF) | Firma del Informe de Aprobación mediante FEA |
| 4. Contabilización SIGFE | Analista | Descarga del informe aprobado; ejecución del asiento de rendición en SIGFE (Reverso de Anticipos / Reconocimiento de Gasto) — plazo: 2 días hábiles tras aprobación técnica |

## Integración Bancaria y Conciliación

**Administración de cuentas corrientes:** Registro único de todas las cuentas (FNDR, Operacionales, Fondos de Terceros). Libro Banco debe cuadrar diariamente con saldo contable de cuenta "Banco".

**Conciliación bancaria:**
- Frecuencia: diaria (gestión de caja) y mensual (cierre contable).
- Método: carga electrónica de cartola bancaria → cruce automático (matcheo) por monto y número de documento.
- Partidas conciliatorias: analizar y depurar mensualmente (cheques girados no cobrados, depósitos no reconocidos, cargos bancarios no contabilizados).
- Resultado: Anexo CGR de Conciliación Bancaria firmado por Tesorero y Jefe de Finanzas.

## Procesos de Cierre

**Cierre mensual** (cronograma estricto, ej. día 10 del mes siguiente):

| Paso | Acción |
|------|--------|
| 1. Cierre de Módulos Auxiliares | Bodega, Activo Fijo, Remuneraciones, Tesorería |
| 2. Centralización | Ejecutar interfaces pendientes |
| 3. Análisis de Cuentas | Revisar saldos anómalos (ej. activo con saldo acreedor) |
| 4. Cuadratura Inter-sistémica | Saldo Presupuestario vs. Contabilidad Patrimonial |
| 5. Generación de Reportes | Balance de Comprobación y de Saldos; Informe de Ejecución Presupuestaria |
| 6. Envío SIGFE | Generación y transmisión de XML/API a Contraloría/DIPRES |

**Cierre anual:**
- Períodos 13 y 14: uso de períodos de ajuste y cierre según instrucciones CGR.
- Devengo total: asegurar devengo de bienes y servicios recibidos al 31/12, aunque factura llegue después.
- Ajustes: depreciación anual · corrección monetaria (si aplica) · provisiones de vacaciones · castigos de deuda incobrable.
- Asiento de apertura: generado automáticamente por el sistema; cuentas de resultado se refunden en "Resultados Acumulados".

**Reportería legal obligatoria:** Balance de 8 Columnas · Estado de Situación Financiera (Balance General Clasificado) · Estado de Resultados · Estado de Flujo de Efectivo (Método Directo) · Estado de Cambios en el Patrimonio Neto · Informe de Pasivos Contingentes.

## Auditoría y Control

**Pista de auditoría:** Principio "Quién, Qué, Cuándo". Cada comprobante registra usuario creador, usuario aprobador, fecha y hora exacta. Comprobante Aprobado/Mayorizado no se edita — se reversa con comprobante contrario. Log de cambios para datos maestros (ej. cambio de cuenta bancaria de proveedor).

**Segregación de funciones:** Quien solicita gasto no debe aprobar. Quien gira pago no debe conciliar el banco. Credenciales únicas e intransferibles.

Documento vivo: actualizar ante cambios en normativa NICSP-CGR o en sistemas de información del GORE.
