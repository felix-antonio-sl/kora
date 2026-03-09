---
_manifest:
  urn: urn:gn:kb:manual-inventarios-bodegas
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/gestion/kb_gn_040_manual_inventarios_bodegas_koda.yml
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
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/gestion/kb_gn_040_manual_inventarios_bodegas_koda.yml
    source_hashes:
      domains/gn/03_operacion/gestion/kb_gn_040_manual_inventarios_bodegas_koda.yml: 4eb84a392e7aafc83705fa4afd8644822e3b6cce38ffd9d7908e97cbb3d8fe9f
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
    skeleton_count: 16
    meat_count: 268
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/manuales__manual-inventarios-bodegas.md.json
---

# Manual 2.2: Gestión de Inventarios y Bodegas
## ID
KB-GN-040-MANUAL-INVENTARIOS-BODEGAS-01

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

## Primary Source
staging/brow_speculativo/manual_2_2_inventarios.md

## Ctx
Manual 2.2: Gestión de Inventarios y Bodegas.

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


## Manual 2 2 Gestion de Inventarios y Bodegas
### ID
GN-MANUAL-INVENTARIOS-BODEGAS-01
### Titulo
#### Def
Manual 2.2: Gestión de Inventarios y Bodegas
### Objetivo
#### Obj
Controlar el flujo físico de existencias y materiales, asegurando la disponibilidad oportuna de insumos para la operación institucional y el correcto registro contable de los movimientos.
### Seccion I Marco Normativo y Organizacion
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S01
#### Fundamentos Legales
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S01-01
#### Ctx
La gestión de inventarios se rige por:
#### Src
- NICSP (Normas Internacionales de Contabilidad del Sector Público): Tratamiento contable de existencias y valorización.
- Resoluciones CGR: Normativa sobre control patrimonial y rendición de cuentas.
- Reglamento Interno de Bodegas: Documento institucional que define procedimientos operativos y responsabilidades.
- Ley 21.180 (Transformación Digital): Obligatoriedad del registro electrónico de movimientos.
#### Estructura Organizacional de Bodegas
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S01-02
#### Roles
| Rol | Def |
| --- | --- |
| Jefe de Bodega Central | Responsable de la administración general del sistema de bodegas. |
| Encargados de Bodega | Funcionarios designados para cada bodega, responsables de custodia y operación. |
| Usuarios Solicitantes | Funcionarios autorizados para generar pedidos de consumo. |
| Aprobadores | Jefaturas con atribución para autorizar despachos según monto y tipo de artículo. |
#### Catalogo de Bodegas Institucionales
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S01-03
#### Ctx
El GORE puede operar múltiples bodegas especializadas:
#### Bodegas
| Bodega | Def |
| --- | --- |
| Bodega Central | Almacenamiento principal de insumos de consumo general. |
| Bodega de Economato | Materiales de oficina y papelería. |
| Bodega de Aseo | Productos de limpieza e higiene. |
| Bodega de Mantención | Repuestos, herramientas y materiales técnicos. |
| Bodega de Vestuario | Uniformes y elementos de seguridad personal (EPP). |
| Bodegas Satélite | Ubicaciones descentralizadas por edificio o servicio. |
### Seccion II Catalogo de Articulos
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S02
#### Codificacion y Clasificacion
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S02-01
#### Req
Todo artículo debe estar registrado en el Catálogo Maestro antes de cualquier movimiento.
#### Campos
-
  #### Campo
  Código Interno
  #### Def
  Identificador único alfanumérico generado por el sistema.
-
  #### Campo
  Código de Barras
  #### Def
  EAN-13 o Code-128 para lectura automática.
-
  #### Campo
  Clasificación Jerárquica
  #### Items
  - Familia (ej. Insumos de Oficina).
  - Línea (ej. Papelería).
  - Grupo (ej. Cuadernos).
-
  #### Campo
  Unidad de Medida
  #### Def
  Unidad base de control (unidad, caja, resma, litro, etc.).
-
  #### Campo
  Conversiones
  #### Def
  Tabla de equivalencias (ej. 1 caja = 12 unidades).
#### Atributos del Articulo
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S02-02
#### Campos
-
  #### Campo
  Cuenta Contable
  #### Def
  Asociación para generación automática de asientos.
-
  #### Campo
  Concepto de Gasto
  #### Def
  Imputación presupuestaria (Subtítulo 22 generalmente).
-
  #### Campo
  Umbral de Capitalización
  #### Def
  Bienes sobre 3 UTM se registran como Activo Fijo, no como existencias.
  #### Ctx Optional
  Manual 2.3: Activo Fijo (./manual_2_3_activo_fijo.md).
-
  #### Campo
  Control de Lote
  #### Def
  Para artículos que requieren trazabilidad (medicamentos, alimentos).
-
  #### Campo
  Fecha de Vencimiento
  #### Req
  Obligatorio para artículos perecibles.
-
  #### Campo
  Imagen Referencial
  #### Def
  Fotografía para identificación visual.
-
  #### Campo
  Stock Mínimo/Máximo
  #### Def
  Parámetros para generación de alertas de reposición.
#### Proveedores Habituales
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S02-03
#### Ctx
El sistema permite asociar proveedores frecuentes a cada artículo para facilitar:
#### Res
- Consulta de precios referenciales.
- Generación de requerimientos de reposición.
- Análisis histórico de compras.
### Seccion III Procesos de Ingreso
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S03
#### Recepcion de Productos por Orden de Compra
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S03-01
#### Ctx
Flujo estándar para ingresos desde proveedores externos.
#### Pasos
-
  #### Paso
  1
  #### Act
  Aviso de Entrega
  #### Def
  El proveedor coordina fecha y hora de despacho.
-
  #### Paso
  2
  #### Act
  Verificación Inicial
  #### Def
  Contrastar guía de despacho con Orden de Compra.
-
  #### Paso
  3
  #### Act
  Inspección Física
  #### Items
  - Contar unidades.
  - Verificar estado y calidad.
  - Controlar lotes y vencimientos (si aplica).
-
  #### Paso
  4
  #### Act
  Registro en Sistema
  #### Def
  Ingresar cantidades recibidas, vinculando a OC.
-
  #### Paso
  5
  #### Act
  Documento Tributario
  #### Def
  Asociar factura electrónica o guía de despacho.
-
  #### Paso
  6
  #### Act
  Ubicación
  #### Def
  Asignar ubicación física dentro de la bodega.
-
  #### Paso
  7
  #### Act
  Recepción Conforme
  #### Def
  Firma del Encargado de Bodega que habilita el devengo.
#### Ctx Clasificacion Bienes
#### Ctx
Los bienes recibidos deben clasificarse por tipología. Existencias (consumibles) van a Bodega según este manual; Activos Fijos (capitalizables) van al proceso de alta.
#### Ctx Optional
Manual 2.3: Activo Fijo (./manual_2_3_activo_fijo.md).
#### Recepcion con Capturador de Datos
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S03-02
#### Items
- Lectura de códigos de barras del proveedor o etiquetas institucionales.
- Validación automática contra OC (cantidad, artículo, precio).
- Generación de alertas por discrepancias.
- Actualización inmediata de stock.
#### Otros Tipos de Ingreso
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S03-03
#### Tipos
| Tipo | Def |
| --- | --- |
| Devolución de Préstamo | Artículos retornados por otras bodegas o unidades. |
| Préstamo Recibido | Artículos temporales de otra institución o bodega. |
| Donación | Bienes recibidos sin costo (requiere resolución de aceptación). |
| Canje | Intercambio de artículos con proveedores. |
| Ajuste por Inventario | Regularización de diferencias positivas detectadas. |
| Devolución de Consumo | Artículos retornados por usuarios por no uso. |
### Seccion IV Procesos de Egreso
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S04
#### Solicitud de Consumo
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S04-01
#### Ctx
Mecanismo formal para retirar artículos de bodega.
#### Proc
-
  #### Paso
  Generación
  #### Def
  Usuario solicitante crea pedido en sistema indicando artículos y cantidades.
-
  #### Paso
  Justificación
  #### Req
  Campo obligatorio que describe el uso previsto.
-
  #### Paso
  Validación
  #### Def
  El sistema verifica stock disponible antes de enviar a aprobación.
-
  #### Paso
  Flujo de Aprobación
  #### Def
  Según monto o tipo de artículo, puede requerir V°B° de jefatura.
#### Despacho de Productos
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S04-02
#### Proc
| Paso | Def |
| --- | --- |
| Preparación (Picking) | El bodeguero reúne los artículos del pedido. |
| Verificación | Contrastar físico con digital antes de entregar. |
| Documento de Despacho | Guía interna firmada por el receptor. |
| Descuento de Stock | Actualización automática al confirmar entrega. |
| Valorización | El sistema aplica método de costeo (Precio Promedio Ponderado o FIFO). |
#### Despacho con Capturador de Datos
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S04-03
#### Items
- Lectura de códigos de barras al momento de armar el pedido.
- Validación automática de artículos y cantidades.
- Generación de documento de despacho electrónico.
- Firma digital del receptor (si el dispositivo lo permite).
#### Otros Tipos de Egreso
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S04-04
#### Tipos
| Tipo | Def |
| --- | --- |
| Préstamo Otorgado | Entrega temporal a otra unidad o institución (con compromiso de devolución). |
| Merma | Pérdida por deterioro, vencimiento o rotura (requiere acta de baja). |
| Donación | Entrega gratuita a terceros (requiere resolución). |
| Devolución a Proveedor | Retorno por no conformidad o cambio. |
| Venta | Enajenación de excedentes (poco frecuente, requiere autorización especial). |
### Seccion V Control de Inventarios
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S05
#### Toma de Inventario Fisico
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S05-01
#### Ctx
Proceso obligatorio de verificación periódica.
#### Frecuencia
-
  #### Tipo
  Inventario General
  #### Req
  Al menos una vez al año (obligatorio al 31/12).
-
  #### Tipo
  Inventarios Parciales
  #### Def
  Por familia, ubicación o artículos críticos (mensual o trimestral).
#### Planificacion
#### Act
Definir alcance, fechas, equipos de conteo y corte de operaciones.
#### Ejecucion
#### Items
- Conteo ciego (sin ver saldos teóricos).
- Segundo conteo para discrepancias.
- Registro en planillas o capturador de datos.
#### Conciliacion
#### Act
Comparar conteo físico vs. saldo en sistema.
#### Ajustes
#### Act
Generar movimientos de ajuste por diferencias (positivas o negativas).
#### Ajuste de Inventario
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S05-02
#### Tipos
| Tipo | Def |
| --- | --- |
| Ajuste Positivo (Sobrante) | Cuando el físico excede al teórico. |
| Ajuste Negativo (Faltante) | Cuando el teórico excede al físico. |
#### Documentacion
#### Req
Acta de inventario firmada por comisión, con explicación de causas.
#### Responsabilidad
#### Warn
Faltantes injustificados pueden derivar en sumario administrativo.
#### Contabilizacion
#### Res
Generación automática de asiento contable por ajuste.
#### Control de Vencimientos
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S05-03
#### Items
- El sistema emite alertas automáticas con 90/60/30 días de anticipación.
- Prioridad de despacho: FEFO (First Expired, First Out).
- Artículos vencidos: Retiro inmediato, acta de baja, destrucción certificada si corresponde.
#### Stock Critico y Reposicion
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S05-04
#### Definiciones
| Termino | Def |
| --- | --- |
| Punto de Reorden | Nivel de stock que dispara la necesidad de reposición. |
| Stock de Seguridad | Margen para cubrir variaciones de demanda o atrasos de proveedor. |
#### Proc
- Alerta Automática: El sistema notifica a Abastecimiento cuando se alcanza el punto de reorden.
- Análisis de Consumo: Reportes históricos para ajustar parámetros de stock.
### Seccion VI Valorizacion y Cierre Contable
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S06
#### Metodos de Valorizacion
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S06-01
#### Ctx
El GORE debe adoptar un método consistente según NICSP:
#### Metodos
| Metodo | Def |
| --- | --- |
| Precio Promedio Ponderado (PPP) | Costo promedio recalculado con cada ingreso. |
| FIFO (First In, First Out) | Primeros ingresos se asignan a primeros egresos. |
| Costo Identificado | Para artículos de alto valor con trazabilidad individual. |
#### Recosteo
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S06-02
#### Ctx
Proceso para actualizar el costo de artículos ante cambios significativos.
#### Cond
- Aplicable cuando hay diferencias relevantes entre costo registrado y costo de reposición.
#### Res
- Genera comprobante contable de ajuste de valor.
#### Cierre Mensual de Bodega
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S06-03
#### Pasos
-
  #### Paso
  1
  #### Act
  Corte de Movimientos
  #### Req
  No ingresan ni egresan productos después del cierre.
-
  #### Paso
  2
  #### Act
  Valorización Final
  #### Def
  Cálculo del stock valorizado al último día del mes.
-
  #### Paso
  3
  #### Act
  Generación de Comprobante
  #### Def
  Asiento contable que registra el costo de lo consumido.
-
  #### Paso
  4
  #### Act
  Cuadratura
  #### Req
  Stock valorizado debe coincidir con cuenta contable de Existencias.
#### Cierre Anual
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S06-04
#### Req
- Inventario físico obligatorio.
- Ajustes de inventario procesados antes del cierre.
#### Res
- Emisión de informe anual de existencias para CGR.
- Traspaso de saldos al ejercicio siguiente.
### Seccion VII Reporteria y Auditoria
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S07
#### Reportes Estandar
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S07-01
#### Reportes
- Cartola de Artículos: Detalle de movimientos por artículo en un período.
- Stock Valorizado: Existencias actuales con su valor monetario.
- Consumos por Unidad: Análisis de uso por departamento/división.
- Artículos sin Movimiento: Identificación de obsolescencia.
- Vencimientos Próximos: Listado de artículos a vencer.
- Diferencias de Inventario: Resumen de ajustes realizados.
#### Trazabilidad y Auditoria
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-S07-02
#### Req
- Cada movimiento registra: usuario, fecha, hora, documento de respaldo.
- Historial de eventos inalterable (log de auditoría).
- Acceso restringido por perfil (bodeguero, supervisor, auditor).
- Documentos de respaldo digitalizados y vinculados a cada transacción.
### Referencias y Alcance
#### ID
GN-MANUAL-INVENTARIOS-BODEGAS-REF-01
#### Ctx
Este manual complementa otros manuales de abastecimiento/patrimonio, enfocándose en la gestión física de existencias (consumibles) desde la recepción hasta el consumo.
#### Ctx Optional
- Manual 2.1: Compras Públicas (./manual_2_1_compras.md).
- Manual 2.3: Activo Fijo (./manual_2_3_activo_fijo.md).

## Referencias Cruzadas
### ID
GN-MANUAL-INVENTARIOS-XREF-01
### Ctx Optional
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_1_compras_koda.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_3_activo_fijo.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_2_contabilidad.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_1_presupuesto.yml
