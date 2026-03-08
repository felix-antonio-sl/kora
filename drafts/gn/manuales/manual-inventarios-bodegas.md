---
_manifest:
  urn: urn:gn:kb:manual-inventarios-bodegas
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
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
    preserved_facts:
    - AI-Remediator=KODA-TRANSFORMER
    - Creation-Date=2025-12-14
    - 'Ctx=Manual 2.2: Gestión de Inventarios y Bodegas.'
    - Format=KODA/Spec
    - Human-Creator=GORE Ñuble
    - Human-Editor=GORE Ñuble
    - ID=KB-GN-040-MANUAL-INVENTARIOS-BODEGAS-01
    - 'LLM_Parsing_Instructions.Content=BEGIN_LLM_INSTRUCTIONS

      You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.


      FIDELITY: Preserve meat (essential information) and skeleton (structure: headers,
      IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic
      prose).


      LEXICON (expand before processing): Act->Action, Cond->Condition, Ctx->Context,
      Ctx_Required->Required External Reference, Ctx_Optional->Optional External Reference,
      Def->Definition, Ex->Example, Mssn->Mission, Obj->Objective, Proc->Process,
      Purp->Purpose, Ref->Reference, XRef->Cross-Artifact Reference, XRef_Required->Mandatory
      Cross-Artifact Reference, Req->Requirement, Res->Result, Src->Source, Prohib->Prohibition,
      Warn->Warning, Just->Justification, Rec->Recommendation


      REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS
      document. XRef/XRef_Required: are external only—must point to a URN (optionally
      with #ID fragment) in another artifact. External documents without specific
      ID use Ctx:, Ctx_Required:, or Ctx_Optional:.


      LANGUAGE POLICY: Keywords in English, content in original language. Never translate
      content.

      END_LLM_INSTRUCTIONS

      '
    - LLM_Parsing_Instructions.ID=KODA-LLM-PARSER-01
    - LLM_Parsing_Instructions.Prohib=Using for artifact creation or translation.
    - LLM_Parsing_Instructions.Req=Mandatory block following Metadata.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.ID=GN-MANUAL-INVENTARIOS-BODEGAS-01
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Objetivo.Obj=Controlar el flujo
      físico de existencias y materiales, asegurando la disponibilidad oportuna de
      insumos para la operación institucional y el correcto registro contable de los
      movimientos.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Referencias_y_Alcance.Ctx=Este manual
      complementa otros manuales de abastecimiento/patrimonio, enfocándose en la gestión
      física de existencias (consumibles) desde la recepción hasta el consumo.
    - 'Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Referencias_y_Alcance.Ctx_Optional[0]=Manual
      2.1: Compras Públicas (./manual_2_1_compras.md).'
    - 'Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Referencias_y_Alcance.Ctx_Optional[1]=Manual
      2.3: Activo Fijo (./manual_2_3_activo_fijo.md).'
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Referencias_y_Alcance.ID=GN-MANUAL-INVENTARIOS-BODEGAS-REF-01
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.ID=GN-MANUAL-INVENTARIOS-BODEGAS-S03
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Otros_Tipos_de_Ingreso.ID=GN-MANUAL-INVENTARIOS-BODEGAS-S03-03
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Otros_Tipos_de_Ingreso.Tipos[0].Def=Artículos
      retornados por otras bodegas o unidades.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Otros_Tipos_de_Ingreso.Tipos[0].Tipo=Devolución
      de Préstamo
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Otros_Tipos_de_Ingreso.Tipos[1].Def=Artículos
      temporales de otra institución o bodega.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Otros_Tipos_de_Ingreso.Tipos[1].Tipo=Préstamo
      Recibido
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Otros_Tipos_de_Ingreso.Tipos[2].Def=Bienes
      recibidos sin costo (requiere resolución de aceptación).
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Otros_Tipos_de_Ingreso.Tipos[2].Tipo=Donación
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Otros_Tipos_de_Ingreso.Tipos[3].Def=Intercambio
      de artículos con proveedores.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Otros_Tipos_de_Ingreso.Tipos[3].Tipo=Canje
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Otros_Tipos_de_Ingreso.Tipos[4].Def=Regularización
      de diferencias positivas detectadas.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Otros_Tipos_de_Ingreso.Tipos[4].Tipo=Ajuste
      por Inventario
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Otros_Tipos_de_Ingreso.Tipos[5].Def=Artículos
      retornados por usuarios por no uso.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Otros_Tipos_de_Ingreso.Tipos[5].Tipo=Devolución
      de Consumo
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_con_Capturador_de_Datos.ID=GN-MANUAL-INVENTARIOS-BODEGAS-S03-02
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_con_Capturador_de_Datos.Items[0]=Lectura
      de códigos de barras del proveedor o etiquetas institucionales.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_con_Capturador_de_Datos.Items[1]=Validación
      automática contra OC (cantidad, artículo, precio).
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_con_Capturador_de_Datos.Items[2]=Generación
      de alertas por discrepancias.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_con_Capturador_de_Datos.Items[3]=Actualización
      inmediata de stock.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.Ctx=Flujo
      estándar para ingresos desde proveedores externos.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.Ctx_Clasificacion_Bienes.Ctx=Los
      bienes recibidos deben clasificarse por tipología. Existencias (consumibles)
      van a Bodega según este manual; Activos Fijos (capitalizables) van al proceso
      de alta.
    - 'Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.Ctx_Clasificacion_Bienes.Ctx_Optional=Manual
      2.3: Activo Fijo (./manual_2_3_activo_fijo.md).'
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.ID=GN-MANUAL-INVENTARIOS-BODEGAS-S03-01
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.Pasos[0].Act=Aviso
      de Entrega
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.Pasos[0].Def=El
      proveedor coordina fecha y hora de despacho.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.Pasos[0].Paso=1
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.Pasos[1].Act=Verificación
      Inicial
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.Pasos[1].Def=Contrastar
      guía de despacho con Orden de Compra.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.Pasos[1].Paso=2
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.Pasos[2].Act=Inspección
      Física
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.Pasos[2].Items[0]=Contar
      unidades.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.Pasos[2].Items[1]=Verificar
      estado y calidad.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.Pasos[2].Items[2]=Controlar
      lotes y vencimientos (si aplica).
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.Pasos[2].Paso=3
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.Pasos[3].Act=Registro
      en Sistema
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.Pasos[3].Def=Ingresar
      cantidades recibidas, vinculando a OC.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.Pasos[3].Paso=4
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.Pasos[4].Act=Documento
      Tributario
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.Pasos[4].Def=Asociar
      factura electrónica o guía de despacho.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.Pasos[4].Paso=5
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.Pasos[5].Act=Ubicación
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.Pasos[5].Def=Asignar
      ubicación física dentro de la bodega.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.Pasos[5].Paso=6
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.Pasos[6].Act=Recepción
      Conforme
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.Pasos[6].Def=Firma
      del Encargado de Bodega que habilita el devengo.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_III_Procesos_de_Ingreso.Recepcion_de_Productos_por_Orden_de_Compra.Pasos[6].Paso=7
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Atributos_del_Articulo.Campos[0].Campo=Cuenta
      Contable
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Atributos_del_Articulo.Campos[0].Def=Asociación
      para generación automática de asientos.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Atributos_del_Articulo.Campos[1].Campo=Concepto
      de Gasto
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Atributos_del_Articulo.Campos[1].Def=Imputación
      presupuestaria (Subtítulo 22 generalmente).
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Atributos_del_Articulo.Campos[2].Campo=Umbral
      de Capitalización
    - 'Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Atributos_del_Articulo.Campos[2].Ctx_Optional=Manual
      2.3: Activo Fijo (./manual_2_3_activo_fijo.md).'
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Atributos_del_Articulo.Campos[2].Def=Bienes
      sobre 3 UTM se registran como Activo Fijo, no como existencias.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Atributos_del_Articulo.Campos[3].Campo=Control
      de Lote
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Atributos_del_Articulo.Campos[3].Def=Para
      artículos que requieren trazabilidad (medicamentos, alimentos).
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Atributos_del_Articulo.Campos[4].Campo=Fecha
      de Vencimiento
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Atributos_del_Articulo.Campos[4].Req=Obligatorio
      para artículos perecibles.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Atributos_del_Articulo.Campos[5].Campo=Imagen
      Referencial
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Atributos_del_Articulo.Campos[5].Def=Fotografía
      para identificación visual.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Atributos_del_Articulo.Campos[6].Campo=Stock
      Mínimo/Máximo
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Atributos_del_Articulo.Campos[6].Def=Parámetros
      para generación de alertas de reposición.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Atributos_del_Articulo.ID=GN-MANUAL-INVENTARIOS-BODEGAS-S02-02
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Codificacion_y_Clasificacion.Campos[0].Campo=Código
      Interno
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Codificacion_y_Clasificacion.Campos[0].Def=Identificador
      único alfanumérico generado por el sistema.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Codificacion_y_Clasificacion.Campos[1].Campo=Código
      de Barras
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Codificacion_y_Clasificacion.Campos[1].Def=EAN-13
      o Code-128 para lectura automática.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Codificacion_y_Clasificacion.Campos[2].Campo=Clasificación
      Jerárquica
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Codificacion_y_Clasificacion.Campos[2].Items[0]=Familia
      (ej. Insumos de Oficina).
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Codificacion_y_Clasificacion.Campos[2].Items[1]=Línea
      (ej. Papelería).
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Codificacion_y_Clasificacion.Campos[2].Items[2]=Grupo
      (ej. Cuadernos).
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Codificacion_y_Clasificacion.Campos[3].Campo=Unidad
      de Medida
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Codificacion_y_Clasificacion.Campos[3].Def=Unidad
      base de control (unidad, caja, resma, litro, etc.).
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Codificacion_y_Clasificacion.Campos[4].Campo=Conversiones
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Codificacion_y_Clasificacion.Campos[4].Def=Tabla
      de equivalencias (ej. 1 caja = 12 unidades).
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Codificacion_y_Clasificacion.ID=GN-MANUAL-INVENTARIOS-BODEGAS-S02-01
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Codificacion_y_Clasificacion.Req=Todo
      artículo debe estar registrado en el Catálogo Maestro antes de cualquier movimiento.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.ID=GN-MANUAL-INVENTARIOS-BODEGAS-S02
    - 'Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Proveedores_Habituales.Ctx=El
      sistema permite asociar proveedores frecuentes a cada artículo para facilitar:'
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Proveedores_Habituales.ID=GN-MANUAL-INVENTARIOS-BODEGAS-S02-03
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Proveedores_Habituales.Res[0]=Consulta
      de precios referenciales.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Proveedores_Habituales.Res[1]=Generación
      de requerimientos de reposición.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_II_Catalogo_de_Articulos.Proveedores_Habituales.Res[2]=Análisis
      histórico de compras.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Despacho_con_Capturador_de_Datos.ID=GN-MANUAL-INVENTARIOS-BODEGAS-S04-03
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Despacho_con_Capturador_de_Datos.Items[0]=Lectura
      de códigos de barras al momento de armar el pedido.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Despacho_con_Capturador_de_Datos.Items[1]=Validación
      automática de artículos y cantidades.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Despacho_con_Capturador_de_Datos.Items[2]=Generación
      de documento de despacho electrónico.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Despacho_con_Capturador_de_Datos.Items[3]=Firma
      digital del receptor (si el dispositivo lo permite).
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Despacho_de_Productos.ID=GN-MANUAL-INVENTARIOS-BODEGAS-S04-02
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Despacho_de_Productos.Proc[0].Def=El
      bodeguero reúne los artículos del pedido.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Despacho_de_Productos.Proc[0].Paso=Preparación
      (Picking)
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Despacho_de_Productos.Proc[1].Def=Contrastar
      físico con digital antes de entregar.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Despacho_de_Productos.Proc[1].Paso=Verificación
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Despacho_de_Productos.Proc[2].Def=Guía
      interna firmada por el receptor.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Despacho_de_Productos.Proc[2].Paso=Documento
      de Despacho
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Despacho_de_Productos.Proc[3].Def=Actualización
      automática al confirmar entrega.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Despacho_de_Productos.Proc[3].Paso=Descuento
      de Stock
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Despacho_de_Productos.Proc[4].Def=El
      sistema aplica método de costeo (Precio Promedio Ponderado o FIFO).
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Despacho_de_Productos.Proc[4].Paso=Valorización
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.ID=GN-MANUAL-INVENTARIOS-BODEGAS-S04
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Otros_Tipos_de_Egreso.ID=GN-MANUAL-INVENTARIOS-BODEGAS-S04-04
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Otros_Tipos_de_Egreso.Tipos[0].Def=Entrega
      temporal a otra unidad o institución (con compromiso de devolución).
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Otros_Tipos_de_Egreso.Tipos[0].Tipo=Préstamo
      Otorgado
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Otros_Tipos_de_Egreso.Tipos[1].Def=Pérdida
      por deterioro, vencimiento o rotura (requiere acta de baja).
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Otros_Tipos_de_Egreso.Tipos[1].Tipo=Merma
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Otros_Tipos_de_Egreso.Tipos[2].Def=Entrega
      gratuita a terceros (requiere resolución).
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Otros_Tipos_de_Egreso.Tipos[2].Tipo=Donación
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Otros_Tipos_de_Egreso.Tipos[3].Def=Retorno
      por no conformidad o cambio.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Otros_Tipos_de_Egreso.Tipos[3].Tipo=Devolución
      a Proveedor
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Otros_Tipos_de_Egreso.Tipos[4].Def=Enajenación
      de excedentes (poco frecuente, requiere autorización especial).
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Otros_Tipos_de_Egreso.Tipos[4].Tipo=Venta
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Solicitud_de_Consumo.Ctx=Mecanismo
      formal para retirar artículos de bodega.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Solicitud_de_Consumo.ID=GN-MANUAL-INVENTARIOS-BODEGAS-S04-01
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Solicitud_de_Consumo.Proc[0].Def=Usuario
      solicitante crea pedido en sistema indicando artículos y cantidades.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Solicitud_de_Consumo.Proc[0].Paso=Generación
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Solicitud_de_Consumo.Proc[1].Paso=Justificación
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Solicitud_de_Consumo.Proc[1].Req=Campo
      obligatorio que describe el uso previsto.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Solicitud_de_Consumo.Proc[2].Def=El
      sistema verifica stock disponible antes de enviar a aprobación.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Solicitud_de_Consumo.Proc[2].Paso=Validación
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Solicitud_de_Consumo.Proc[3].Def=Según
      monto o tipo de artículo, puede requerir V°B° de jefatura.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_IV_Procesos_de_Egreso.Solicitud_de_Consumo.Proc[3].Paso=Flujo
      de Aprobación
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Catalogo_de_Bodegas_Institucionales.Bodegas[0].Bodega=Bodega
      Central
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Catalogo_de_Bodegas_Institucionales.Bodegas[0].Def=Almacenamiento
      principal de insumos de consumo general.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Catalogo_de_Bodegas_Institucionales.Bodegas[1].Bodega=Bodega
      de Economato
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Catalogo_de_Bodegas_Institucionales.Bodegas[1].Def=Materiales
      de oficina y papelería.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Catalogo_de_Bodegas_Institucionales.Bodegas[2].Bodega=Bodega
      de Aseo
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Catalogo_de_Bodegas_Institucionales.Bodegas[2].Def=Productos
      de limpieza e higiene.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Catalogo_de_Bodegas_Institucionales.Bodegas[3].Bodega=Bodega
      de Mantención
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Catalogo_de_Bodegas_Institucionales.Bodegas[3].Def=Repuestos,
      herramientas y materiales técnicos.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Catalogo_de_Bodegas_Institucionales.Bodegas[4].Bodega=Bodega
      de Vestuario
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Catalogo_de_Bodegas_Institucionales.Bodegas[4].Def=Uniformes
      y elementos de seguridad personal (EPP).
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Catalogo_de_Bodegas_Institucionales.Bodegas[5].Bodega=Bodegas
      Satélite
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Catalogo_de_Bodegas_Institucionales.Bodegas[5].Def=Ubicaciones
      descentralizadas por edificio o servicio.
    - 'Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Catalogo_de_Bodegas_Institucionales.Ctx=El
      GORE puede operar múltiples bodegas especializadas:'
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Catalogo_de_Bodegas_Institucionales.ID=GN-MANUAL-INVENTARIOS-BODEGAS-S01-03
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Estructura_Organizacional_de_Bodegas.ID=GN-MANUAL-INVENTARIOS-BODEGAS-S01-02
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Estructura_Organizacional_de_Bodegas.Roles[0].Def=Responsable
      de la administración general del sistema de bodegas.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Estructura_Organizacional_de_Bodegas.Roles[0].Rol=Jefe
      de Bodega Central
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Estructura_Organizacional_de_Bodegas.Roles[1].Def=Funcionarios
      designados para cada bodega, responsables de custodia y operación.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Estructura_Organizacional_de_Bodegas.Roles[1].Rol=Encargados
      de Bodega
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Estructura_Organizacional_de_Bodegas.Roles[2].Def=Funcionarios
      autorizados para generar pedidos de consumo.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Estructura_Organizacional_de_Bodegas.Roles[2].Rol=Usuarios
      Solicitantes
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Estructura_Organizacional_de_Bodegas.Roles[3].Def=Jefaturas
      con atribución para autorizar despachos según monto y tipo de artículo.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Estructura_Organizacional_de_Bodegas.Roles[3].Rol=Aprobadores
    - 'Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Fundamentos_Legales.Ctx=La
      gestión de inventarios se rige por:'
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Fundamentos_Legales.ID=GN-MANUAL-INVENTARIOS-BODEGAS-S01-01
    - 'Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Fundamentos_Legales.Src[0]=NICSP
      (Normas Internacionales de Contabilidad del Sector Público): Tratamiento contable
      de existencias y valorización.'
    - 'Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Fundamentos_Legales.Src[1]=Resoluciones
      CGR: Normativa sobre control patrimonial y rendición de cuentas.'
    - 'Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Fundamentos_Legales.Src[2]=Reglamento
      Interno de Bodegas: Documento institucional que define procedimientos operativos
      y responsabilidades.'
    - 'Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.Fundamentos_Legales.Src[3]=Ley
      21.180 (Transformación Digital): Obligatoriedad del registro electrónico de
      movimientos.'
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_I_Marco_Normativo_y_Organizacion.ID=GN-MANUAL-INVENTARIOS-BODEGAS-S01
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VII_Reporteria_y_Auditoria.ID=GN-MANUAL-INVENTARIOS-BODEGAS-S07
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VII_Reporteria_y_Auditoria.Reportes_Estandar.ID=GN-MANUAL-INVENTARIOS-BODEGAS-S07-01
    - 'Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VII_Reporteria_y_Auditoria.Reportes_Estandar.Reportes[0]=Cartola
      de Artículos: Detalle de movimientos por artículo en un período.'
    - 'Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VII_Reporteria_y_Auditoria.Reportes_Estandar.Reportes[1]=Stock
      Valorizado: Existencias actuales con su valor monetario.'
    - 'Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VII_Reporteria_y_Auditoria.Reportes_Estandar.Reportes[2]=Consumos
      por Unidad: Análisis de uso por departamento/división.'
    - 'Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VII_Reporteria_y_Auditoria.Reportes_Estandar.Reportes[3]=Artículos
      sin Movimiento: Identificación de obsolescencia.'
    - 'Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VII_Reporteria_y_Auditoria.Reportes_Estandar.Reportes[4]=Vencimientos
      Próximos: Listado de artículos a vencer.'
    - 'Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VII_Reporteria_y_Auditoria.Reportes_Estandar.Reportes[5]=Diferencias
      de Inventario: Resumen de ajustes realizados.'
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VII_Reporteria_y_Auditoria.Trazabilidad_y_Auditoria.ID=GN-MANUAL-INVENTARIOS-BODEGAS-S07-02
    - 'Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VII_Reporteria_y_Auditoria.Trazabilidad_y_Auditoria.Req[0]=Cada
      movimiento registra: usuario, fecha, hora, documento de respaldo.'
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VII_Reporteria_y_Auditoria.Trazabilidad_y_Auditoria.Req[1]=Historial
      de eventos inalterable (log de auditoría).
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VII_Reporteria_y_Auditoria.Trazabilidad_y_Auditoria.Req[2]=Acceso
      restringido por perfil (bodeguero, supervisor, auditor).
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VII_Reporteria_y_Auditoria.Trazabilidad_y_Auditoria.Req[3]=Documentos
      de respaldo digitalizados y vinculados a cada transacción.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VI_Valorizacion_y_Cierre_Contable.Cierre_Anual.ID=GN-MANUAL-INVENTARIOS-BODEGAS-S06-04
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VI_Valorizacion_y_Cierre_Contable.Cierre_Anual.Req[0]=Inventario
      físico obligatorio.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VI_Valorizacion_y_Cierre_Contable.Cierre_Anual.Req[1]=Ajustes
      de inventario procesados antes del cierre.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VI_Valorizacion_y_Cierre_Contable.Cierre_Anual.Res[0]=Emisión
      de informe anual de existencias para CGR.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VI_Valorizacion_y_Cierre_Contable.Cierre_Anual.Res[1]=Traspaso
      de saldos al ejercicio siguiente.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VI_Valorizacion_y_Cierre_Contable.Cierre_Mensual_de_Bodega.ID=GN-MANUAL-INVENTARIOS-BODEGAS-S06-03
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VI_Valorizacion_y_Cierre_Contable.Cierre_Mensual_de_Bodega.Pasos[0].Act=Corte
      de Movimientos
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VI_Valorizacion_y_Cierre_Contable.Cierre_Mensual_de_Bodega.Pasos[0].Paso=1
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VI_Valorizacion_y_Cierre_Contable.Cierre_Mensual_de_Bodega.Pasos[0].Req=No
      ingresan ni egresan productos después del cierre.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VI_Valorizacion_y_Cierre_Contable.Cierre_Mensual_de_Bodega.Pasos[1].Act=Valorización
      Final
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VI_Valorizacion_y_Cierre_Contable.Cierre_Mensual_de_Bodega.Pasos[1].Def=Cálculo
      del stock valorizado al último día del mes.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VI_Valorizacion_y_Cierre_Contable.Cierre_Mensual_de_Bodega.Pasos[1].Paso=2
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VI_Valorizacion_y_Cierre_Contable.Cierre_Mensual_de_Bodega.Pasos[2].Act=Generación
      de Comprobante
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VI_Valorizacion_y_Cierre_Contable.Cierre_Mensual_de_Bodega.Pasos[2].Def=Asiento
      contable que registra el costo de lo consumido.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VI_Valorizacion_y_Cierre_Contable.Cierre_Mensual_de_Bodega.Pasos[2].Paso=3
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VI_Valorizacion_y_Cierre_Contable.Cierre_Mensual_de_Bodega.Pasos[3].Act=Cuadratura
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VI_Valorizacion_y_Cierre_Contable.Cierre_Mensual_de_Bodega.Pasos[3].Paso=4
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VI_Valorizacion_y_Cierre_Contable.Cierre_Mensual_de_Bodega.Pasos[3].Req=Stock
      valorizado debe coincidir con cuenta contable de Existencias.
    - Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VI_Valorizacion_y_Cierre_Contable.ID=GN-MANUAL-INVENTARIOS-BODEGAS-S06
    - 'Manual_2_2_Gestion_de_Inventarios_y_Bodegas.Seccion_VI_Valorizacion_y_Cierre_Contable.Metodos_de_Valorizacion.Ctx=El
      GORE debe adoptar un método consistente según NICSP:'
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
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
