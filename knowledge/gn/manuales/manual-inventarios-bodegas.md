---
_manifest:
  urn: urn:gn:kb:manual-inventarios-bodegas
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: "GORE Ñuble"
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- inventarios
- bodegas
- nicsp
- gn
lang: es
---

# Manual 2.2: Gestión de Inventarios y Bodegas

Objetivo: Controlar el flujo físico de existencias y materiales, asegurando la disponibilidad oportuna de insumos para la operación institucional y el correcto registro contable de los movimientos.

Siglas: NICSP = Normas Internacionales de Contabilidad del Sector Público · CGR = Contraloría General de la República · SIGAS = sistema de activo fijo y existencias · OC = Orden de Compra · PPP = Precio Promedio Ponderado · FIFO = First In First Out · FEFO = First Expired First Out.

## Marco Normativo y Organización

| Fuente | Contenido |
|--------|-----------|
| NICSP | Tratamiento contable de existencias y valorización |
| Resoluciones CGR | Control patrimonial y rendición de cuentas |
| Reglamento Interno de Bodegas | Procedimientos operativos y responsabilidades institucionales |
| Ley 21.180 | Obligatoriedad del registro electrónico de movimientos |

**Roles:**

| Rol | Responsabilidad |
|-----|----------------|
| Jefe de Bodega Central | Administración general del sistema de bodegas |
| Encargados de Bodega | Custodia y operación de cada bodega; designados formalmente |
| Usuarios Solicitantes | Funcionarios autorizados para generar pedidos de consumo |
| Aprobadores | Jefaturas con atribución para autorizar despachos según monto y tipo |

**Bodegas institucionales:**

| Bodega | Contenido |
|--------|-----------|
| Bodega Central | Insumos de consumo general |
| Bodega de Economato | Materiales de oficina y papelería |
| Bodega de Aseo | Productos de limpieza e higiene |
| Bodega de Mantención | Repuestos, herramientas y materiales técnicos |
| Bodega de Vestuario | Uniformes y elementos de seguridad personal (EPP) |
| Bodegas Satélite | Ubicaciones descentralizadas por edificio o servicio |

## Catálogo de Artículos

**Codificación:** Todo artículo debe estar en el Catálogo Maestro antes de cualquier movimiento.

| Campo | Descripción |
|-------|-------------|
| Código Interno | Identificador único alfanumérico generado por el sistema |
| Código de Barras | EAN-13 o Code-128 para lectura automática |
| Clasificación jerárquica | Familia → Línea → Grupo (ej. Insumos de Oficina → Papelería → Cuadernos) |
| Unidad de Medida | Unidad base de control (unidad, caja, resma, litro, etc.) |
| Conversiones | Tabla de equivalencias (ej. 1 caja = 12 unidades) |
| Cuenta Contable | Asociación para generación automática de asientos |
| Concepto de Gasto | Imputación presupuestaria (Subtítulo 22 generalmente) |
| Umbral de Capitalización | Bienes sobre 3 UTM → Activo Fijo, no existencias (ver Manual 2.3) |
| Control de Lote | Para artículos que requieren trazabilidad (medicamentos, alimentos) |
| Fecha de Vencimiento | Obligatorio para artículos perecibles |
| Stock Mínimo/Máximo | Parámetros para alertas de reposición |

## Procesos de Ingreso

**Recepción por Orden de Compra (flujo estándar):**

| Paso | Acción |
|------|--------|
| 1. Aviso de entrega | Proveedor coordina fecha y hora de despacho |
| 2. Verificación inicial | Contrastar guía de despacho con OC |
| 3. Inspección física | Contar unidades, verificar estado y calidad, controlar lotes y vencimientos |
| 4. Registro en sistema | Ingresar cantidades recibidas, vinculando a OC |
| 5. Documento tributario | Asociar factura electrónica o guía de despacho |
| 6. Ubicación | Asignar ubicación física dentro de la bodega |
| 7. Recepción Conforme | Firma del Encargado de Bodega que habilita el devengo |

Bienes recibidos se clasifican: existencias (consumibles) → Bodega según este manual; activos fijos (capitalizables) → proceso de alta (Manual 2.3).

**Recepción con capturador de datos:** Lectura de códigos de barras del proveedor o etiquetas institucionales · validación automática contra OC (cantidad, artículo, precio) · alertas por discrepancias · actualización inmediata de stock.

**Otros tipos de ingreso:**

| Tipo | Descripción |
|------|-------------|
| Devolución de Préstamo | Artículos retornados por otras bodegas o unidades |
| Préstamo Recibido | Artículos temporales de otra institución o bodega |
| Donación | Bienes recibidos sin costo (requiere resolución de aceptación) |
| Canje | Intercambio de artículos con proveedores |
| Ajuste por Inventario | Regularización de diferencias positivas detectadas |
| Devolución de Consumo | Artículos retornados por usuarios por no uso |

## Procesos de Egreso

**Solicitud de consumo:**
1. Usuario solicitante crea pedido en sistema indicando artículos y cantidades.
2. Justificación: campo obligatorio que describe el uso previsto.
3. Validación: el sistema verifica stock disponible antes de enviar a aprobación.
4. Flujo de aprobación: según monto o tipo de artículo, puede requerir V°B° de jefatura.

**Despacho de productos:**

| Paso | Descripción |
|------|-------------|
| Preparación (Picking) | Bodeguero reúne los artículos del pedido |
| Verificación | Contrastar físico con digital antes de entregar |
| Documento de Despacho | Guía interna firmada por el receptor |
| Descuento de Stock | Actualización automática al confirmar entrega |
| Valorización | Sistema aplica método de costeo (PPP o FIFO) |

**Despacho con capturador:** Lectura de códigos de barras al armar el pedido · validación automática de artículos y cantidades · documento de despacho electrónico · firma digital del receptor (si el dispositivo lo permite).

**Otros tipos de egreso:**

| Tipo | Descripción |
|------|-------------|
| Préstamo Otorgado | Entrega temporal a otra unidad o institución; compromiso de devolución |
| Merma | Pérdida por deterioro, vencimiento o rotura (requiere acta de baja) |
| Donación | Entrega gratuita a terceros (requiere resolución) |
| Devolución a Proveedor | Retorno por no conformidad o cambio |
| Venta | Enajenación de excedentes (poco frecuente; requiere autorización especial) |

## Control de Inventarios

**Toma de inventario físico:**

| Tipo | Frecuencia | Descripción |
|------|-----------|-------------|
| Inventario General | Al menos anual (obligatorio al 31/12) | Totalidad de bienes |
| Inventarios Parciales | Mensual o trimestral | Por familia, ubicación o artículos críticos |

Ejecución: conteo ciego (sin ver saldos teóricos) · segundo conteo para discrepancias · registro en planillas o capturador · conciliación físico vs. saldo en sistema · ajustes por diferencias.

**Ajuste de inventario:**

| Tipo | Descripción |
|------|-------------|
| Positivo (Sobrante) | Físico excede al teórico; regularizar con alta |
| Negativo (Faltante) | Teórico excede al físico; investigar causa |

Documentación: acta de inventario firmada por comisión con explicación de causas. Faltantes injustificados pueden derivar en sumario administrativo. Ajuste genera asiento contable automático.

**Control de vencimientos:** Alertas automáticas a 90/60/30 días de anticipación. Prioridad de despacho: FEFO. Artículos vencidos: retiro inmediato + acta de baja + destrucción certificada si corresponde.

**Stock crítico y reposición:**
- Punto de Reorden: nivel de stock que dispara la necesidad de reposición.
- Stock de Seguridad: margen para cubrir variaciones de demanda o atrasos de proveedor.
- Alerta automática al sistema de Abastecimiento al alcanzar el punto de reorden.

## Valorización y Cierre Contable

**Métodos de valorización (NICSP):**

| Método | Descripción |
|--------|-------------|
| PPP — Precio Promedio Ponderado | Costo promedio recalculado con cada ingreso |
| FIFO — First In, First Out | Primeros ingresos se asignan a primeros egresos |
| Costo Identificado | Para artículos de alto valor con trazabilidad individual |

**Cierre mensual de bodega:**

| Paso | Acción |
|------|--------|
| 1. Corte de Movimientos | No ingresan ni egresan productos después del cierre |
| 2. Valorización Final | Cálculo del stock valorizado al último día del mes |
| 3. Generación de Comprobante | Asiento contable que registra el costo de lo consumido |
| 4. Cuadratura | Stock valorizado = cuenta contable de Existencias |

**Cierre anual:** Inventario físico obligatorio · ajustes procesados antes del cierre · emisión de informe anual de existencias para CGR · traspaso de saldos al ejercicio siguiente.

## Reportería y Auditoría

**Reportes estándar:**

| Reporte | Contenido |
|---------|-----------|
| Cartola de Artículos | Detalle de movimientos por artículo en un período |
| Stock Valorizado | Existencias actuales con su valor monetario |
| Consumos por Unidad | Análisis de uso por departamento/división |
| Artículos sin Movimiento | Identificación de obsolescencia |
| Vencimientos Próximos | Listado de artículos a vencer |
| Diferencias de Inventario | Resumen de ajustes realizados |

**Trazabilidad:** Cada movimiento registra usuario, fecha, hora, documento de respaldo. Historial de eventos inalterable (log de auditoría). Acceso restringido por perfil (bodeguero, supervisor, auditor). Documentos de respaldo digitalizados y vinculados a cada transacción.
