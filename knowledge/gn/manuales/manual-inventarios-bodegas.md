---
_manifest:
  urn: "urn:gn:kb:manual-inventarios-bodegas"
  provenance:
    created_by: "FS"
    created_at: "2026-01-29"
    source: "GORE Ñuble"
version: "2.0.0"
status: published
tags: [gore-nuble, gobierno-regional, inventarios, bodegas, contabilidad]
lang: es
---

# Manual 2.2: Gestión de Inventarios y Bodegas

## Marco Normativo y Organización
- **Objetivo**: Controlar flujo físico de existencias, asegurar disponibilidad de insumos y garantizar registro contable de movimientos.
- **Fundamentos Legales**:
  | Norma | Aplicación |
  | :--- | :--- |
  | NICSP | Tratamiento contable de existencias y valorización. |
  | Resoluciones CGR | Normativa sobre control patrimonial y rendición de cuentas. |
  | Reglamento Interno | Definición de procedimientos operativos y responsabilidades. |
  | Ley 21.180 | Obligatoriedad de registro electrónico (Transformación Digital). |
- **Roles y Atribuciones**:
  - **Jefe de Bodega Central**: Administrador general del sistema de bodegas.
  - **Encargados de Bodega**: Custodia y operación por recinto designado.
  - **Usuarios Solicitantes**: Generación de pedidos de consumo autorizados.
  - **Aprobadores**: Jefaturas con facultad de autorizar despachos según monto/artículo.
- **Catálogo de Bodegas**:
  - Central (consumo general), Economato (papelería/oficina), Aseo (limpieza), Mantención (herramientas/técnico), Vestuario (EPP), Satélites (descentralizadas).

## Catálogo de Artículos
- **Requisito**: Inscripción obligatoria en Catálogo Maestro previo a cualquier movimiento.
- **Codificación y Clasificación**:
  - Código Interno: Alfanumérico único del sistema.
  - Código de Barras: Estándares EAN-13 o Code-128.
  - Jerarquía: Familia > Línea > Grupo.
  - Control por Unidad de Medida base y tablas de conversión (ej. Caja a Unidades).
- **Atributos Técnicos**:
  - **Contable**: Asociación a Cuenta Contable y Concepto de Gasto (Subtítulo 22).
  - **Capitalización**: Bienes > 3 UTM se derivan a Activo Fijo (no existencias).
  - **Trazabilidad**: Control de Lote y Fecha de Vencimiento (obligatorio para perecibles).
  - **Reposición**: Parámetros de Stock Mínimo y Máximo.
- **Proveedores**: Registro de proveedores frecuentes para análisis histórico y reposición.

## Procesos de Ingreso
- **Recepción por Orden de Compra (OC)**:
  1. Aviso de Entrega: Coordinación con proveedor.
  2. Verificación: Contrastar Guía de Despacho vs OC.
  3. Inspección: Conteo físico, estado de calidad y control de lotes.
  4. Registro: Ingreso en sistema vinculado a OC.
  5. Documentación: Asociación de factura electrónica o guía.
  6. Ubicación: Asignación física en estantería/bodega.
  7. Recepción Conforme: Firma de encargado que habilita el devengo presupuestario.
- **Ingreso Digital**: Uso de capturadores de datos para validación automática contra OC.
- **Otros Tipos de Ingreso**:
  - Devolución de préstamo, donaciones (con resolución de aceptación), canjes, ajustes por inventario (sobrantes) y devoluciones de usuarios.

## Procesos de Egreso
- **Solicitud de Consumo**:
  - Creación de pedido en sistema por usuario solicitante.
  - Justificación obligatoria del uso previsto.
  - Validación de stock disponible previa a la aprobación.
  - Flujo de firmas según jerarquía y tipo de bien.
- **Operación de Despacho**:
  - Picking: Preparación física de artículos.
  - Verificación: Cruce físico vs digital.
  - Despacho: Emisión de guía interna y firma del receptor.
  - Actualización: Descuento automático de stock y valorización (PPP o FIFO).
- **Otros Tipos de Egreso**:
  - Préstamo otorgado, merma (requiere acta de baja por deterioro/vencimiento), donaciones (con resolución), devolución a proveedor y venta de excedentes.

## Control de Inventarios
- **Toma de Inventario Físico**:
  - **General**: Obligatorio anualmente al 31 de diciembre.
  - **Parcial**: Mensual o trimestral para artículos críticos o familias específicas.
  - **Metodología**: Conteo ciego, segundo conteo ante discrepancias y conciliación sistémica.
- **Ajustes de Inventario**:
  - Sobrantes (Positivos) y Faltantes (Negativos).
  - Documentación: Acta firmada por comisión con justificación técnica.
  - Sanción: Faltantes injustificados pueden derivar en sumario administrativo.
- **Gestión de Expiración**:
  - Alertas sistémicas a 90, 60 y 30 días del vencimiento.
  - Despacho bajo lógica FEFO (First Expired, First Out).
- **Reposición**:
  - Punto de Reorden: Nivel de stock que activa alerta a Abastecimiento.
  - Stock de Seguridad: Margen para cubrir variaciones de demanda.

## Valorización y Cierre Contable
- **Métodos de Valorización (NICSP)**:
  - Precio Promedio Ponderado (PPP): Recalculado con cada nuevo ingreso.
  - FIFO (First In, First Out): Asignación de costo por antigüedad de ingreso.
  - Costo Identificado: Para bienes de alto valor unitario.
- **Cierre Mensual de Bodega**:
  1. Corte de movimientos (bloqueo transaccional).
  2. Valorización de existencias al último día del mes.
  3. Generación de comprobante contable de consumo mensual.
  4. Cuadratura entre stock valorizado y cuenta contable de Existencias.
- **Cierre Anual**: Requiere inventario físico total y procesamiento de ajustes previo a la emisión del informe para CGR.

## Reportería y Auditoría
- **Reportes Estándar**:
  - Cartola de movimientos por artículo.
  - Listado de stock valorizado.
  - Consumos por unidad administrativa.
  - Análisis de obsolescencia (artículos sin movimiento).
  - Reporte de vencimientos próximos.
- **Trazabilidad y Seguridad**:
  - Log de auditoría inalterable (usuario, fecha, hora, documento).
  - Acceso restringido mediante perfiles (Bodeguero, Supervisor, Auditor).
  - Soporte documental digitalizado vinculado a cada transacción.
