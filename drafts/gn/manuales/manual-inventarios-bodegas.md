---
_manifest:
  urn: urn:gn:kb:manual-inventarios-bodegas
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-10'
    source: domains/gn/03_operacion/gestion/kb_gn_040_manual_inventarios_bodegas_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- inventarios
- bodegas
- nicsp
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/gestion/kb_gn_040_manual_inventarios_bodegas_koda.yml
    source_hashes:
      domains/gn/03_operacion/gestion/kb_gn_040_manual_inventarios_bodegas_koda.yml: 4eb84a392e7aafc83705fa4afd8644822e3b6cce38ffd9d7908e97cbb3d8fe9f
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 3.19
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    document_family: generic
    publication_class: knowledge
    skeleton_count: 2
    meat_count: 238
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/manuales__manual-inventarios-bodegas.md.json
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:gn:kb:manual-inventarios-bodegas
---

# Manual 2.2: Gestión de Inventarios y Bodegas
## Manual 2 2 Gestion de Inventarios y Bodegas
- **Definicion:** Manual 2.2: Gestión de Inventarios y Bodegas
## Objetivo
- **Objetivos:** Controlar el flujo físico de existencias y materiales, asegurando la disponibilidad oportuna de insumos para la operación institucional y el correcto registro contable de los movimientos.
## Seccion I Marco Normativo y Organizacion
### Fundamentos Legales
- **Contexto:** La gestión de inventarios se rige por:
- **Fuentes:** NICSP (Normas Internacionales de Contabilidad del Sector Público): Tratamiento contable de existencias y valorización., Resoluciones CGR: Normativa sobre control patrimonial y rendición de cuentas., Reglamento Interno de Bodegas: Documento institucional que define procedimientos operativos y responsabilidades., Ley 21.180 (Transformación Digital): Obligatoriedad del registro electrónico de movimientos.
### Estructura Organizacional de Bodegas
### Roles
| Rol | Def |
| --- | --- |
| Jefe de Bodega Central | Responsable de la administración general del sistema de bodegas. |
| Encargados de Bodega | Funcionarios designados para cada bodega, responsables de custodia y operación. |
| Usuarios Solicitantes | Funcionarios autorizados para generar pedidos de consumo. |
| Aprobadores | Jefaturas con atribución para autorizar despachos según monto y tipo de artículo. |
### Catalogo de Bodegas Institucionales
- **Contexto:** El GORE puede operar múltiples bodegas especializadas:
### Bodegas
| Bodega | Def |
| --- | --- |
| Bodega Central | Almacenamiento principal de insumos de consumo general. |
| Bodega de Economato | Materiales de oficina y papelería. |
| Bodega de Aseo | Productos de limpieza e higiene. |
| Bodega de Mantención | Repuestos, herramientas y materiales técnicos. |
| Bodega de Vestuario | Uniformes y elementos de seguridad personal (EPP). |
| Bodegas Satélite | Ubicaciones descentralizadas por edificio o servicio. |
## Seccion II Catalogo de Articulos
### Codificacion y Clasificacion
- **Requisitos:** Todo artículo debe estar registrado en el Catálogo Maestro antes de cualquier movimiento.
### Campos
| Campo | Def |
| --- | --- |
| Código Interno | Identificador único alfanumérico generado por el sistema. |
| Código de Barras | EAN-13 o Code-128 para lectura automática. |
| Clasificación Jerárquica | |
| Unidad de Medida | Unidad base de control (unidad, caja, resma, litro, etc.). |
| Conversiones | Tabla de equivalencias (ej. 1 caja = 12 unidades). |
### Atributos del Articulo
### Campos
| Campo | Def |
| --- | --- |
| Cuenta Contable | Asociación para generación automática de asientos. |
| Concepto de Gasto | Imputación presupuestaria (Subtítulo 22 generalmente). |
| Umbral de Capitalización | Bienes sobre 3 UTM se registran como Activo Fijo, no como existencias. |
| Control de Lote | Para artículos que requieren trazabilidad (medicamentos, alimentos). |
| Fecha de Vencimiento | |
| Imagen Referencial | Fotografía para identificación visual. |
| Stock Mínimo/Máximo | Parámetros para generación de alertas de reposición. |
### Proveedores Habituales
- **Contexto:** El sistema permite asociar proveedores frecuentes a cada artículo para facilitar:
- **Resultados:** Consulta de precios referenciales., Generación de requerimientos de reposición., Análisis histórico de compras.
## Seccion III Procesos de Ingreso
### Recepcion de Productos por Orden de Compra
- **Contexto:** Flujo estándar para ingresos desde proveedores externos.
### Pasos
| Paso | Act | Def |
| --- | --- | --- |
| 1 | Aviso de Entrega | El proveedor coordina fecha y hora de despacho. |
| 2 | Verificación Inicial | Contrastar guía de despacho con Orden de Compra. |
| 3 | Inspección Física | |
| 4 | Registro en Sistema | Ingresar cantidades recibidas, vinculando a OC. |
| 5 | Documento Tributario | Asociar factura electrónica o guía de despacho. |
| 6 | Ubicación | Asignar ubicación física dentro de la bodega. |
| 7 | Recepción Conforme | Firma del Encargado de Bodega que habilita el devengo. |
### Ctx Clasificacion Bienes
- **Contexto:** Los bienes recibidos deben clasificarse por tipología. Existencias (consumibles) van a Bodega según este manual; Activos Fijos (capitalizables) van al proceso de alta.
- **Contexto opcional:** Manual 2.3: Activo Fijo (./manual_2_3_activo_fijo.md).
### Recepcion con Capturador de Datos
- **Items:** Lectura de códigos de barras del proveedor o etiquetas institucionales., Validación automática contra OC (cantidad, artículo, precio)., Generación de alertas por discrepancias., Actualización inmediata de stock.
### Otros Tipos de Ingreso
### Tipos
| Tipo | Def |
| --- | --- |
| Devolución de Préstamo | Artículos retornados por otras bodegas o unidades. |
| Préstamo Recibido | Artículos temporales de otra institución o bodega. |
| Donación | Bienes recibidos sin costo (requiere resolución de aceptación). |
| Canje | Intercambio de artículos con proveedores. |
| Ajuste por Inventario | Regularización de diferencias positivas detectadas. |
| Devolución de Consumo | Artículos retornados por usuarios por no uso. |
## Seccion IV Procesos de Egreso
### Solicitud de Consumo
- **Contexto:** Mecanismo formal para retirar artículos de bodega.
### Proceso
| Paso | Def |
| --- | --- |
| Generación | Usuario solicitante crea pedido en sistema indicando artículos y cantidades. |
| Justificación | |
| Validación | El sistema verifica stock disponible antes de enviar a aprobación. |
| Flujo de Aprobación | Según monto o tipo de artículo, puede requerir V°B° de jefatura. |
### Despacho de Productos
### Proceso
| Paso | Def |
| --- | --- |
| Preparación (Picking) | El bodeguero reúne los artículos del pedido. |
| Verificación | Contrastar físico con digital antes de entregar. |
| Documento de Despacho | Guía interna firmada por el receptor. |
| Descuento de Stock | Actualización automática al confirmar entrega. |
| Valorización | El sistema aplica método de costeo (Precio Promedio Ponderado o FIFO). |
### Despacho con Capturador de Datos
- **Items:** Lectura de códigos de barras al momento de armar el pedido., Validación automática de artículos y cantidades., Generación de documento de despacho electrónico., Firma digital del receptor (si el dispositivo lo permite).
### Otros Tipos de Egreso
### Tipos
| Tipo | Def |
| --- | --- |
| Préstamo Otorgado | Entrega temporal a otra unidad o institución (con compromiso de devolución). |
| Merma | Pérdida por deterioro, vencimiento o rotura (requiere acta de baja). |
| Donación | Entrega gratuita a terceros (requiere resolución). |
| Devolución a Proveedor | Retorno por no conformidad o cambio. |
| Venta | Enajenación de excedentes (poco frecuente, requiere autorización especial). |
## Seccion V Control de Inventarios
### Toma de Inventario Fisico
- **Contexto:** Proceso obligatorio de verificación periódica.
### Frecuencia
| Tipo | Req | Def |
| --- | --- | --- |
| Inventario General | Al menos una vez al año (obligatorio al 31/12). | |
| Inventarios Parciales | | Por familia, ubicación o artículos críticos (mensual o trimestral). |
### Planificacion
- **Acciones:** Definir alcance, fechas, equipos de conteo y corte de operaciones.
### Ejecucion
- **Items:** Conteo ciego (sin ver saldos teóricos)., Segundo conteo para discrepancias., Registro en planillas o capturador de datos.
### Conciliacion
- **Acciones:** Comparar conteo físico vs. saldo en sistema.
### Ajustes
- **Acciones:** Generar movimientos de ajuste por diferencias (positivas o negativas).
### Ajuste de Inventario
### Tipos
| Tipo | Def |
| --- | --- |
| Ajuste Positivo (Sobrante) | Cuando el físico excede al teórico. |
| Ajuste Negativo (Faltante) | Cuando el teórico excede al físico. |
### Documentacion
- **Requisitos:** Acta de inventario firmada por comisión, con explicación de causas.
### Responsabilidad
- **Advertencias:** Faltantes injustificados pueden derivar en sumario administrativo.
### Contabilizacion
- **Resultados:** Generación automática de asiento contable por ajuste.
### Control de Vencimientos
- **Items:** El sistema emite alertas automáticas con 90/60/30 días de anticipación., Prioridad de despacho: FEFO (First Expired, First Out)., Artículos vencidos: Retiro inmediato, acta de baja, destrucción certificada si corresponde.
### Stock Critico y Reposicion
- **Proceso:** Alerta Automática: El sistema notifica a Abastecimiento cuando se alcanza el punto de reorden., Análisis de Consumo: Reportes históricos para ajustar parámetros de stock.
### Definiciones
| Termino | Def |
| --- | --- |
| Punto de Reorden | Nivel de stock que dispara la necesidad de reposición. |
| Stock de Seguridad | Margen para cubrir variaciones de demanda o atrasos de proveedor. |
## Seccion VI Valorizacion y Cierre Contable
### Metodos de Valorizacion
- **Contexto:** El GORE debe adoptar un método consistente según NICSP:
### Metodos
| Metodo | Def |
| --- | --- |
| Precio Promedio Ponderado (PPP) | Costo promedio recalculado con cada ingreso. |
| FIFO (First In, First Out) | Primeros ingresos se asignan a primeros egresos. |
| Costo Identificado | Para artículos de alto valor con trazabilidad individual. |
### Recosteo
- **Contexto:** Proceso para actualizar el costo de artículos ante cambios significativos.
- **Condiciones:** Aplicable cuando hay diferencias relevantes entre costo registrado y costo de reposición.
- **Resultados:** Genera comprobante contable de ajuste de valor.
### Cierre Mensual de Bodega
### Pasos
| Paso | Act | Req | Def |
| --- | --- | --- | --- |
| 1 | Corte de Movimientos | No ingresan ni egresan productos después del cierre. | |
| 2 | Valorización Final | | Cálculo del stock valorizado al último día del mes. |
| 3 | Generación de Comprobante | | Asiento contable que registra el costo de lo consumido. |
| 4 | Cuadratura | Stock valorizado debe coincidir con cuenta contable de Existencias. | |
### Cierre Anual
- **Requisitos:** Inventario físico obligatorio., Ajustes de inventario procesados antes del cierre.
- **Resultados:** Emisión de informe anual de existencias para CGR., Traspaso de saldos al ejercicio siguiente.
## Seccion VII Reporteria y Auditoria
### Reportes Estandar
- **Reportes:** Cartola de Artículos: Detalle de movimientos por artículo en un período., Stock Valorizado: Existencias actuales con su valor monetario., Consumos por Unidad: Análisis de uso por departamento/división., Artículos sin Movimiento: Identificación de obsolescencia., Vencimientos Próximos: Listado de artículos a vencer., Diferencias de Inventario: Resumen de ajustes realizados.
### Trazabilidad y Auditoria
- **Requisitos:** Cada movimiento registra: usuario, fecha, hora, documento de respaldo., Historial de eventos inalterable (log de auditoría)., Acceso restringido por perfil (bodeguero, supervisor, auditor)., Documentos de respaldo digitalizados y vinculados a cada transacción.
## Referencias y Alcance
- **Contexto:** Este manual complementa otros manuales de abastecimiento/patrimonio, enfocándose en la gestión física de existencias (consumibles) desde la recepción hasta el consumo.
- **Contexto opcional:** Manual 2.1: Compras Públicas (./manual_2_1_compras.md)., Manual 2.3: Activo Fijo (./manual_2_3_activo_fijo.md).

## Referencias Cruzadas
- **Contexto opcional:** , , ,
