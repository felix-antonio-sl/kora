---
_manifest:
  urn: urn:gn:kb:manual-compras
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/gestion/kb_gn_046_manual_compras_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- compras-publicas
- chilecompra
- mercado-publico
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/gestion/kb_gn_046_manual_compras_koda.yml
    source_hashes:
      domains/gn/03_operacion/gestion/kb_gn_046_manual_compras_koda.yml: d8a0c38e5fb27d0017067ea4a3c0dd66fe3f89a0fcc7326e03e4ade56d084b96
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.14
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 18
    meat_count: 261
    fat_count: 0
    preserved_facts:
    - AI-Remediator=KODA-TRANSFORMER
    - Authoritative-Source.Last-Validated=2025-12-18
    - Authoritative-Source.Path=staging/temp/brutos ordenados/04_adquisiciones_activos/Manual-de-Adquisiciones-GORE_Ñuble_3R.md
    - Authoritative-Source.Priority=1
    - Authoritative-Source.Type=Official-Manual-DAF
    - Creation-Date=2025-12-14
    - 'Ctx=Manual: Compras Públicas y Contrataciones (GORE Ñuble).'
    - Format=KODA/Spec
    - Human-Creator=GORE Ñuble
    - Human-Editor=FS
    - ID=MANUAL-COMPRAS-CONTRATACIONES-01
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


      LANGUAGE POLICY: Keywords in English (and abbreviated forms as listed), content
      in original language (Spanish). Never translate content.

      END_LLM_INSTRUCTIONS

      '
    - LLM_Parsing_Instructions.ID=KODA-LLM-PARSER-01
    - LLM_Parsing_Instructions.Prohib=Using for artifact creation or translation.
    - LLM_Parsing_Instructions.Req=Mandatory block following Metadata.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.ID=MANUAL-COMPRAS-CONTRATACIONES-CONTENT-01
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Nota_Final.Ctx=Este manual establece
      los lineamientos para una gestión de compras eficiente, transparente y conforme
      a la normativa de contratación pública.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Obj=Normar la adquisición de bienes
      y servicios garantizando transparencia, eficiencia y cumplimiento de la Ley
      N° 19.886 de Compras Públicas y su Reglamento.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.10_Grandes_Compras_Licitaciones_mayores_a_5000_UTM.ID=MANUAL-COMPRAS-SEC-III-GRANDES-01
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.10_Grandes_Compras_Licitaciones_mayores_a_5000_UTM.Reqs[0].Req=Requieren
      visación previa de la División Jurídica sobre las bases.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.10_Grandes_Compras_Licitaciones_mayores_a_5000_UTM.Reqs[1].Req=Garantía
      de seriedad de la oferta obligatoria (generalmente 5% del presupuesto estimado).
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.10_Grandes_Compras_Licitaciones_mayores_a_5000_UTM.Reqs[2].Req=Plazo
      de ofertas mínimo 30 días corridos.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.10_Grandes_Compras_Licitaciones_mayores_a_5000_UTM.Reqs[3].Req=Evaluación
      técnica puede incluir visitas a terreno o demostraciones.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.7_Convenio_Marco_CM.Catalogo_ChileCompra.Ctx=Se
      accede vía tienda electrónica en www.mercadopublico.cl.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.7_Convenio_Marco_CM.Def=Modalidad
      preferente para bienes y servicios estandarizados.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.7_Convenio_Marco_CM.ID=MANUAL-COMPRAS-SEC-III-CM-01
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.7_Convenio_Marco_CM.Proceso.Proc[0].Act=Selección
      de producto
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.7_Convenio_Marco_CM.Proceso.Proc[1].Act=Emisión
      de OC
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.7_Convenio_Marco_CM.Proceso.Proc[2].Act=Aceptación
      proveedor
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.7_Convenio_Marco_CM.Proceso.Proc[3].Act=Despacho/Prestación
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.7_Convenio_Marco_CM.Restriccion.Prohib=No
      aplica para bienes o servicios no catalogados.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.7_Convenio_Marco_CM.Ventaja.Res=No
      requiere proceso licitatorio individual.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.8_Licitacion_Publica.Acta_de_Evaluacion.Req=Documento
      fundado que justifica la puntuación de cada oferente.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.8_Licitacion_Publica.Adjudicacion.Req=Por
      Resolución Exenta del Gobernador Regional, publicada en el portal.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.8_Licitacion_Publica.Bases_Administrativas.Ctx=Condiciones
      generales, plazos, garantías, causales de inadmisibilidad.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.8_Licitacion_Publica.Bases_Tecnicas.Ctx=Especificaciones
      del bien o servicio, criterios de evaluación técnica.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.8_Licitacion_Publica.Comision_Evaluadora.Reqs[0].Req=Mínimo
      3 integrantes designados por resolución.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.8_Licitacion_Publica.Comision_Evaluadora.Reqs[1].Req=Incluye
      al menos un funcionario del área técnica requirente.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.8_Licitacion_Publica.Criterios_de_Evaluacion.Req=Deben
      definirse en las bases con ponderaciones claras (Técnico, Económico, Plazos,
      etc.).
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.8_Licitacion_Publica.ID=MANUAL-COMPRAS-SEC-III-LP-01
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.8_Licitacion_Publica.Publicacion.Plazos[0]=Mínimo
      20 días corridos para ofertar (licitación normal).
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.8_Licitacion_Publica.Publicacion.Plazos[1]=10
      días (licitación abreviada por monto < 100 UTM).
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.8_Licitacion_Publica.Req=Obligatoria
      para compras de bienes, servicios y ejecución de proyectos de inversión (Subtítulo
      31) superiores a 1.000 UTM (salvo Convenio Marco).
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.9_Licitacion_Privada_y_Trato_Directo.Def=Modalidades
      excepcionales sujetas a causales legales taxativas.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.9_Licitacion_Privada_y_Trato_Directo.ID=MANUAL-COMPRAS-SEC-III-EXCEPCIONES-01
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.9_Licitacion_Privada_y_Trato_Directo.Trato_Directo_Art_8_Ley_19886.Causales[0].Causal=Proveedor
      único.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.9_Licitacion_Privada_y_Trato_Directo.Trato_Directo_Art_8_Ley_19886.Causales[1].Causal=Emergencias
      calificadas.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.9_Licitacion_Privada_y_Trato_Directo.Trato_Directo_Art_8_Ley_19886.Causales[2].Causal=Compras
      < 10 UTM.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.9_Licitacion_Privada_y_Trato_Directo.Trato_Directo_Art_8_Ley_19886.Causales[3].Causal=Contratos
      de prórroga por continuidad de servicio (máximo 12 meses).
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.9_Licitacion_Privada_y_Trato_Directo.Trato_Directo_Art_8_Ley_19886.ID=MANUAL-COMPRAS-SEC-III-TD-01
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.9_Licitacion_Privada_y_Trato_Directo.Trato_Directo_Art_8_Ley_19886.Requisitos[0].Req=Resolución
      fundada que invoque la causal específica.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.9_Licitacion_Privada_y_Trato_Directo.Trato_Directo_Art_8_Ley_19886.Requisitos[1].Req=Publicación
      en Mercado Público (salvo montos menores).
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.9_Licitacion_Privada_y_Trato_Directo.Trato_Directo_Art_8_Ley_19886.Requisitos[2].Req=Visación
      del Jefe DAF para montos > 100 UTM.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_III_Mecanismos_de_Compra.ID=MANUAL-COMPRAS-SEC-III-01
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.4_Plan_Anual_de_Compras_PAC.Aprobacion.Act=Aprueba
      el PAC consolidado
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.4_Plan_Anual_de_Compras_PAC.Aprobacion.Ctx=Mediante
      Resolución Exenta.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.4_Plan_Anual_de_Compras_PAC.Aprobacion.Responsable=Administrador
      Regional
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.4_Plan_Anual_de_Compras_PAC.Consolidacion.Act=Integra
      y prioriza las necesidades
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.4_Plan_Anual_de_Compras_PAC.Consolidacion.Criterios_de_Priorizacion[0].Criterio=Criticidad
      operativa.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.4_Plan_Anual_de_Compras_PAC.Consolidacion.Criterios_de_Priorizacion[1].Criterio=Disponibilidad
      presupuestaria.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.4_Plan_Anual_de_Compras_PAC.Consolidacion.Criterios_de_Priorizacion[2].Criterio=Alineamiento
      con metas institucionales.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.4_Plan_Anual_de_Compras_PAC.Consolidacion.Responsable=Unidad
      de Abastecimiento
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.4_Plan_Anual_de_Compras_PAC.Def=El
      PAC es el instrumento de planificación que articula necesidades con presupuesto
      disponible.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.4_Plan_Anual_de_Compras_PAC.Elaboracion.Act=Envía
      requerimientos a la Unidad de Abastecimiento
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.4_Plan_Anual_de_Compras_PAC.Elaboracion.Plazo=Antes
      del 15 de Noviembre del año anterior
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.4_Plan_Anual_de_Compras_PAC.Elaboracion.Responsable=Cada
      División/Departamento
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.4_Plan_Anual_de_Compras_PAC.ID=MANUAL-COMPRAS-SEC-II-PAC-01
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.4_Plan_Anual_de_Compras_PAC.Modificaciones.Cond=Durante
      el año
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.4_Plan_Anual_de_Compras_PAC.Modificaciones.Req=Permitidas
      mediante resolución fundada
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.4_Plan_Anual_de_Compras_PAC.Modificaciones.Req_Actualizacion[0].Req=Actualizar
      la publicación en el portal.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.4_Plan_Anual_de_Compras_PAC.Publicacion.Act=Publica
      en Mercado Público
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.4_Plan_Anual_de_Compras_PAC.Publicacion.Plazo=Dentro
      de los primeros 30 días del año calendario
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.4_Plan_Anual_de_Compras_PAC.Publicacion.Responsable=Unidad
      de Abastecimiento
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.5_Tipos_de_Requerimientos.ID=MANUAL-COMPRAS-SEC-II-REQS-01
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.5_Tipos_de_Requerimientos.Tipos[0].Def=Incluidos
      en la programación anual.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.5_Tipos_de_Requerimientos.Tipos[0].Tipo=Planificados
      (PAC)
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.5_Tipos_de_Requerimientos.Tipos[1].Def=Necesidades
      imprevistas que requieren justificación escrita del área solicitante y visación
      DAF.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.5_Tipos_de_Requerimientos.Tipos[1].Tipo=Extraordinarios
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.5_Tipos_de_Requerimientos.Tipos[2].Def=Situaciones
      de emergencia que permiten plazos abreviados según Reglamento (Art. 43).
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.5_Tipos_de_Requerimientos.Tipos[2].Tipo=Urgentes
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.6_Reserva_Presupuestaria_Previa.ID=MANUAL-COMPRAS-SEC-II-RESERVA-01
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.6_Reserva_Presupuestaria_Previa.Prohib=Ningún
      proceso de compra inicia sin CDP vigente.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.6_Reserva_Presupuestaria_Previa.Reqs[0].Req=El
      CDP debe emitirse desde el sistema financiero antes de la publicación del llamado
      o emisión de la OC.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.6_Reserva_Presupuestaria_Previa.Reqs[1].Req=La
      pre-afectación bloquea los recursos hasta la adjudicación o desistimiento.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_II_Planificacion_de_Compras.ID=MANUAL-COMPRAS-SEC-II-01
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.11_Generacion_de_la_OC.Contenido_Obligatorio[0].Req=Descripción
      detallada del bien/servicio.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.11_Generacion_de_la_OC.Contenido_Obligatorio[1].Req=Cantidad
      y precio unitario.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.11_Generacion_de_la_OC.Contenido_Obligatorio[2].Req=Plazo
      de entrega/ejecución.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.11_Generacion_de_la_OC.Contenido_Obligatorio[3].Req=Lugar
      de entrega.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.11_Generacion_de_la_OC.Contenido_Obligatorio[4].Req=Imputación
      presupuestaria (Subtítulo/Ítem/Asignación).
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.11_Generacion_de_la_OC.Def=La
      OC es el acto administrativo que formaliza el compromiso con el proveedor.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.11_Generacion_de_la_OC.ID=MANUAL-COMPRAS-SEC-IV-OC-01
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.11_Generacion_de_la_OC.Reqs[0].Req=Se
      emite en Mercado Público tras la adjudicación (licitaciones) o selección (CM/Trato
      Directo).
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.12_Aceptacion_y_Rechazo.ID=MANUAL-COMPRAS-SEC-IV-ACEPTACION-01
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.12_Aceptacion_y_Rechazo.Plazo=48
      horas hábiles
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.12_Aceptacion_y_Rechazo.Req=El
      proveedor tiene 48 horas hábiles para aceptar la OC en el portal (salvo indicación
      distinta en bases).
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.12_Aceptacion_y_Rechazo.Res=OC
      rechazada o no aceptada permite re-adjudicar al siguiente oferente mejor evaluado.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.13_Recepcion_Conforme.Bienes.Proc[0].Act=La
      bodega o área solicitante verifica cantidad, calidad y concordancia con OC.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.13_Recepcion_Conforme.Bienes.Proc[1].Act=Genera
      Acta de Recepción física o digital.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.13_Recepcion_Conforme.Def=Hito
      crítico que habilita el devengo y posterior pago.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.13_Recepcion_Conforme.ID=MANUAL-COMPRAS-SEC-IV-RECEPCION-01
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.13_Recepcion_Conforme.Integracion_Contable.Res=La
      recepción conforme genera automáticamente el devengo presupuestario y el pasivo
      contable (Cuentas por Pagar).
    - 'Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.13_Recepcion_Conforme.Nota_Recepcion_Fisica_Bienes.Ctx_Optional=Para
      el procedimiento detallado de recepción física de bienes, consulte el Manual
      2.2: Inventarios (./manual_2_2_inventarios.md) §7.'
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.13_Recepcion_Conforme.Pago_Electronico_Obligatorio.ID=MANUAL-COMPRAS-SEC-IV-PAGO-ELECTRONICO-01
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.13_Recepcion_Conforme.Pago_Electronico_Obligatorio.Prohib=Pago
      en efectivo o cheque, salvo excepciones legalmente autorizadas.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.13_Recepcion_Conforme.Pago_Electronico_Obligatorio.Req=Todos
      los pagos a proveedores deben realizarse exclusivamente mediante transferencia
      electrónica de fondos.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.13_Recepcion_Conforme.Pago_Electronico_Obligatorio.Src=Art.
      8 de la Ley de Presupuestos
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.13_Recepcion_Conforme.Servicios.Proc[0].Responsable=Administrador
      del contrato
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.13_Recepcion_Conforme.Servicios.Proc[1].Act=Certifica
      el cumplimiento mediante Informe de Conformidad.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.14_Devoluciones_y_Reclamos.ID=MANUAL-COMPRAS-SEC-IV-DEVOLUCIONES-01
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.14_Devoluciones_y_Reclamos.Plazo=8
      días corridos
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.14_Devoluciones_y_Reclamos.Reqs[0].Req=Plazo
      de 8 días corridos desde la recepción para reclamar la factura electrónica en
      el SII.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.14_Devoluciones_y_Reclamos.Reqs[1].Req=Devoluciones
      por no conformidad deben documentarse con Acta de Rechazo indicando las causales.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.14_Devoluciones_y_Reclamos.Reqs[2].Req=El
      proveedor tiene plazo según contrato/OC para subsanar o reemplazar.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_IV_Ejecucion_de_Ordenes_de_Compra.ID=MANUAL-COMPRAS-SEC-IV-01
    - 'Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.1_Fundamentos_Legales.Ctx=La
      gestión de compras del GORE se rige por:'
    - 'Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.1_Fundamentos_Legales.Fuentes[0].Src=Ley
      N° 19.886 y Modificación Ley 21.634 (Compras 2.0): Moderniza la gestión de compras
      públicas.'
    - 'Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.1_Fundamentos_Legales.Fuentes[1].Src=Decreto
      N° 661 (2024): Nuevo Reglamento de la Ley de Compras (vigencia 12/2024).'
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.1_Fundamentos_Legales.Fuentes[2].Src=Ley
      de Presupuestos (Partida 31).
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.1_Fundamentos_Legales.Fuentes[3].Src=Directivas
      ChileCompra.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.1_Fundamentos_Legales.Fuentes[4].Src=Ley
      21.180 (Transformación Digital).
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.1_Fundamentos_Legales.ID=MANUAL-COMPRAS-SEC-I-FUND-01
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.2_Principios_Rectores.ID=MANUAL-COMPRAS-SEC-I-PRINCIPIOS-01
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.2_Principios_Rectores.Principios[0].Principio=Libre
      Concurrencia
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.2_Principios_Rectores.Principios[0].Req=Garantizar
      la participación de todos los proveedores que cumplan requisitos.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.2_Principios_Rectores.Principios[1].Principio=Igualdad
      de Trato
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.2_Principios_Rectores.Principios[1].Req=No
      discriminar entre oferentes por razones ajenas al mérito técnico-económico.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.2_Principios_Rectores.Principios[2].Principio=Transparencia
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.2_Principios_Rectores.Principios[2].Req=Publicar
      bases, aclaraciones, evaluaciones y adjudicaciones en www.mercadopublico.cl.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.2_Principios_Rectores.Principios[3].Principio=Eficiencia
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.2_Principios_Rectores.Principios[3].Req=Optimizar
      la relación calidad-precio en las adquisiciones.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.2_Principios_Rectores.Principios[4].Principio=Probidad
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.2_Principios_Rectores.Principios[4].Req=Evitar
      conflictos de interés y declarar inhabilidades.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.3_Glosario_de_Terminos.ID=MANUAL-COMPRAS-SEC-I-GLOSARIO-01
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.3_Glosario_de_Terminos.Terminos[0].Def=Plan
      Anual de Compras.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.3_Glosario_de_Terminos.Terminos[0].ID=MANUAL-COMPRAS-GLOS-PAC
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.3_Glosario_de_Terminos.Terminos[0].Sigla=PAC
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.3_Glosario_de_Terminos.Terminos[1].Def=Orden
      de Compra emitida en Mercado Público.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.3_Glosario_de_Terminos.Terminos[1].ID=MANUAL-COMPRAS-GLOS-OC
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.3_Glosario_de_Terminos.Terminos[1].Sigla=OC
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.3_Glosario_de_Terminos.Terminos[2].Def=Acuerdo
      suscrito por ChileCompra con proveedores para compras directas a precios predefinidos.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.3_Glosario_de_Terminos.Terminos[2].ID=MANUAL-COMPRAS-GLOS-CONVENIO-MARCO
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.3_Glosario_de_Terminos.Terminos[2].Termino=Convenio
      Marco
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.3_Glosario_de_Terminos.Terminos[3].Def=Certificado
      de Disponibilidad Presupuestaria.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.3_Glosario_de_Terminos.Terminos[3].ID=MANUAL-COMPRAS-GLOS-CDP
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.3_Glosario_de_Terminos.Terminos[3].Sigla=CDP
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.3_Glosario_de_Terminos.Terminos[4].Def=Acto
      formal que valida la entrega satisfactoria del bien o servicio.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.3_Glosario_de_Terminos.Terminos[4].ID=MANUAL-COMPRAS-GLOS-RECEPCION-CONFORME
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.3_Glosario_de_Terminos.Terminos[4].Termino=Recepción
      Conforme
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.ID=MANUAL-COMPRAS-SEC-I-01
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.Nuevos_Umbrales_y_Modalidades
      (Decreto 661/2024).ID=MANUAL-COMPRAS-SEC-I-UMBRALES-01
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.Nuevos_Umbrales_y_Modalidades
      (Decreto 661/2024).Tabla_Maestra[0].Modalidad=Fondos Globales (Caja Chica) o
      Portal Mercado Público.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.Nuevos_Umbrales_y_Modalidades
      (Decreto 661/2024).Tabla_Maestra[0].Rango=< 3 UTM
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.Nuevos_Umbrales_y_Modalidades
      (Decreto 661/2024).Tabla_Maestra[1].Modalidad=Compra Ágil (Preferente). Mínimo
      3 cotizaciones en el sistema.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.Nuevos_Umbrales_y_Modalidades
      (Decreto 661/2024).Tabla_Maestra[1].Rango=3 a 100 UTM
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.Nuevos_Umbrales_y_Modalidades
      (Decreto 661/2024).Tabla_Maestra[2].Modalidad=Licitación Pública (Normas Simplificadas).
      Contrato opcional (puede formalizarse con OC).
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.Nuevos_Umbrales_y_Modalidades
      (Decreto 661/2024).Tabla_Maestra[2].Rango=100 a 1.000 UTM
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.Nuevos_Umbrales_y_Modalidades
      (Decreto 661/2024).Tabla_Maestra[3].Modalidad=Licitación Pública (Normas Generales).
      Contrato obligatorio y Garantía de Fiel Cumplimiento.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.Nuevos_Umbrales_y_Modalidades
      (Decreto 661/2024).Tabla_Maestra[3].Rango=> 1.000 UTM
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.Nuevos_Umbrales_y_Modalidades
      (Decreto 661/2024).Tabla_Maestra[4].Rango=> 5.000 UTM
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_I_Marco_Normativo_y_Principios_Rectores.Nuevos_Umbrales_y_Modalidades
      (Decreto 661/2024).Tabla_Maestra[4].Req=Garantía de Seriedad de la Oferta obligatoria
      (máximo 3% del monto).
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_VI_Control_Transparencia_y_Evaluacion.20_Interoperabilidad_con_Mercado_Publico.ID=MANUAL-COMPRAS-SEC-VI-INTEROP-01
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_VI_Control_Transparencia_y_Evaluacion.20_Interoperabilidad_con_Mercado_Publico.Reqs[0].Req=Toda
      operación debe reflejarse en www.mercadopublico.cl.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_VI_Control_Transparencia_y_Evaluacion.20_Interoperabilidad_con_Mercado_Publico.Reqs[1].Req=El
      sistema institucional (SIGAS o equivalente) debe sincronizar OC, estados de
      pago y recepciones.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_VI_Control_Transparencia_y_Evaluacion.20_Interoperabilidad_con_Mercado_Publico.Reqs[2].Req=Descarga
      automática de actas de adjudicación para trazabilidad.
    - 'Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_VI_Control_Transparencia_y_Evaluacion.21_Portal_de_Proveedores.Def=Herramienta
      de transparencia que permite a proveedores consultar:'
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_VI_Control_Transparencia_y_Evaluacion.21_Portal_de_Proveedores.Funcionalidades[0].Funcionalidad=Estado
      de sus órdenes de compra.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_VI_Control_Transparencia_y_Evaluacion.21_Portal_de_Proveedores.Funcionalidades[1].Funcionalidad=Estado
      de facturas y pagos.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_VI_Control_Transparencia_y_Evaluacion.21_Portal_de_Proveedores.Funcionalidades[2].Funcionalidad=Historial
      de transacciones.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_VI_Control_Transparencia_y_Evaluacion.21_Portal_de_Proveedores.ID=MANUAL-COMPRAS-SEC-VI-PORTAL-01
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_VI_Control_Transparencia_y_Evaluacion.22_Evaluacion_de_Proveedores.Consecuencias.Res=Proveedores
      con evaluación deficiente pueden ser excluidos de futuras licitaciones (según
      bases).
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_VI_Control_Transparencia_y_Evaluacion.22_Evaluacion_de_Proveedores.Criterios[0]=Cumplimiento
      de plazos
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_VI_Control_Transparencia_y_Evaluacion.22_Evaluacion_de_Proveedores.Criterios[1]=Calidad
      del producto/servicio
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_VI_Control_Transparencia_y_Evaluacion.22_Evaluacion_de_Proveedores.Criterios[2]=Respuesta
      ante incidencias
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_VI_Control_Transparencia_y_Evaluacion.22_Evaluacion_de_Proveedores.Frecuencia[0]=Al
      cierre de cada contrato
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_VI_Control_Transparencia_y_Evaluacion.22_Evaluacion_de_Proveedores.Frecuencia[1]=Anualmente
      para contratos de tracto sucesivo
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_VI_Control_Transparencia_y_Evaluacion.22_Evaluacion_de_Proveedores.ID=MANUAL-COMPRAS-SEC-VI-EVAL-01
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_VI_Control_Transparencia_y_Evaluacion.22_Evaluacion_de_Proveedores.Registro.Req=La
      calificación se incorpora al Historial de Proveedores institucional.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_VI_Control_Transparencia_y_Evaluacion.23_Reportes_y_Auditoria.ID=MANUAL-COMPRAS-SEC-VI-REPORTES-01
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_VI_Control_Transparencia_y_Evaluacion.23_Reportes_y_Auditoria.Indicadores_de_Gestion[0].Indicador=%
      de compras vía Convenio Marco.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_VI_Control_Transparencia_y_Evaluacion.23_Reportes_y_Auditoria.Indicadores_de_Gestion[1].Indicador=%
      de licitaciones declaradas desiertas.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_VI_Control_Transparencia_y_Evaluacion.23_Reportes_y_Auditoria.Indicadores_de_Gestion[2].Indicador=Tiempo
      promedio de adjudicación.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_VI_Control_Transparencia_y_Evaluacion.23_Reportes_y_Auditoria.Indicadores_de_Gestion[3].Indicador=Cumplimiento
      de plazos de pago a 30 días.
    - 'Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_VI_Control_Transparencia_y_Evaluacion.23_Reportes_y_Auditoria.Reportes[0]=Informe
      Mensual de Compras: Resumen de OC emitidas, montos, mecanismos utilizados.'
    - 'Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_VI_Control_Transparencia_y_Evaluacion.23_Reportes_y_Auditoria.Reportes[1]=Informe
      de Contratos Vigentes: Estado de avance, hitos pendientes, alertas de vencimiento.'
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_VI_Control_Transparencia_y_Evaluacion.ID=MANUAL-COMPRAS-SEC-VI-01
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_V_Gestion_de_Contratos.15_Formalizacion_de_Contratos.Casos[0].Caso=Licitaciones
      > 100 UTM.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_V_Gestion_de_Contratos.15_Formalizacion_de_Contratos.Casos[1].Caso=Servicios
      de tracto sucesivo.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_V_Gestion_de_Contratos.15_Formalizacion_de_Contratos.Casos[2].Caso=Obras
      civiles.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_V_Gestion_de_Contratos.15_Formalizacion_de_Contratos.Contenido_del_Contrato[0].Req=Identificación
      de las partes.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_V_Gestion_de_Contratos.15_Formalizacion_de_Contratos.Contenido_del_Contrato[1].Req=Objeto
      y alcance.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_V_Gestion_de_Contratos.15_Formalizacion_de_Contratos.Contenido_del_Contrato[2].Req=Precio
      y modalidad de pago (hitos, mensualidades, etc.).
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_V_Gestion_de_Contratos.15_Formalizacion_de_Contratos.Contenido_del_Contrato[3].Req=Plazos
      de ejecución.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_V_Gestion_de_Contratos.15_Formalizacion_de_Contratos.Contenido_del_Contrato[4].Req=Garantías
      exigidas.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_V_Gestion_de_Contratos.15_Formalizacion_de_Contratos.Contenido_del_Contrato[5].Req=Multas
      y sanciones.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_V_Gestion_de_Contratos.15_Formalizacion_de_Contratos.Contenido_del_Contrato[6].Req=Causales
      de término anticipado.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_V_Gestion_de_Contratos.15_Formalizacion_de_Contratos.ID=MANUAL-COMPRAS-SEC-V-FORMALIZACION-01
    - 'Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_V_Gestion_de_Contratos.15_Formalizacion_de_Contratos.Req=Obligatorio
      para:'
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_V_Gestion_de_Contratos.16_Administracion_del_Contrato.Administrador_del_Contrato.Req=Funcionario
      designado por resolución, responsable del seguimiento técnico y cumplimiento
      de hitos.
    - Manual_2_1_Compras_Publicas_y_Contrataciones.Seccion_V_Gestion_de_Contratos.16_Administracion_del_Contrato.Estados_de_Pago.Def=Documentos
      que certifican el avance para liberar pagos parciales según hitos.
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
---

# Manual 2.1: Compras Públicas y Contrataciones
## ID
MANUAL-COMPRAS-CONTRATACIONES-01

## Version
1.0.0

## Status
Draft

## Format
KODA/Spec

## Human Creator
GORE Ñuble

## Human Editor
FS

## Model Collaborator
IA-CASCADE

## AI Remediator
KODA-TRANSFORMER

## Creation Date
2025-12-14

## Modification Date
2025-12-16

## Primary Source
staging/brow_speculativo/manual_2_1_compras.md

## Ctx
Manual: Compras Públicas y Contrataciones (GORE Ñuble).

## Authoritative Source
### Path
staging/temp/brutos ordenados/04_adquisiciones_activos/Manual-de-Adquisiciones-GORE_Ñuble_3R.md
### Priority
1
### Type
Official-Manual-DAF
### Last Validated
2025-12-18

## Source Hierarchy
| Level | Description |
| --- | --- |
| 1 | Fuentes Brutas Ordenadas (staging/temp/brutos ordenados/*) |
| 2 | Pseudo-manuales KB (knowledge/domains/gn/gestion/pseudo_manuales_operativos/*) |
| 3 | Fuentes Especulativas (staging/brow_speculativo/*) |

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

LANGUAGE POLICY: Keywords in English (and abbreviated forms as listed), content in original language (Spanish). Never translate content.
END_LLM_INSTRUCTIONS


## Manual 2 1 Compras Publicas y Contrataciones
### ID
MANUAL-COMPRAS-CONTRATACIONES-CONTENT-01
### Obj
Normar la adquisición de bienes y servicios garantizando transparencia, eficiencia y cumplimiento de la Ley N° 19.886 de Compras Públicas y su Reglamento.
### Seccion I Marco Normativo y Principios Rectores
#### ID
MANUAL-COMPRAS-SEC-I-01
#### 1 Fundamentos Legales
#### ID
MANUAL-COMPRAS-SEC-I-FUND-01
#### Ctx
La gestión de compras del GORE se rige por:
#### Fuentes
| Src |
| --- |
| Ley N° 19.886 y Modificación Ley 21.634 (Compras 2.0): Moderniza la gestión de compras públicas. |
| Decreto N° 661 (2024): Nuevo Reglamento de la Ley de Compras (vigencia 12/2024). |
| Ley de Presupuestos (Partida 31). |
| Directivas ChileCompra. |
| Ley 21.180 (Transformación Digital). |
#### Nuevos Umbrales y Modalidades (Decreto 661/2024)
#### ID
MANUAL-COMPRAS-SEC-I-UMBRALES-01
#### Tabla Maestra
-
  #### Rango
  < 3 UTM
  #### Modalidad
  Fondos Globales (Caja Chica) o Portal Mercado Público.
-
  #### Rango
  3 a 100 UTM
  #### Modalidad
  Compra Ágil (Preferente). Mínimo 3 cotizaciones en el sistema.
-
  #### Rango
  100 a 1.000 UTM
  #### Modalidad
  Licitación Pública (Normas Simplificadas). Contrato opcional (puede formalizarse con OC).
-
  #### Rango
  > 1.000 UTM
  #### Modalidad
  Licitación Pública (Normas Generales). Contrato obligatorio y Garantía de Fiel Cumplimiento.
-
  #### Rango
  > 5.000 UTM
  #### Req
  Garantía de Seriedad de la Oferta obligatoria (máximo 3% del monto).
#### 2 Principios Rectores
#### ID
MANUAL-COMPRAS-SEC-I-PRINCIPIOS-01
#### Principios
| Principio | Req |
| --- | --- |
| Libre Concurrencia | Garantizar la participación de todos los proveedores que cumplan requisitos. |
| Igualdad de Trato | No discriminar entre oferentes por razones ajenas al mérito técnico-económico. |
| Transparencia | Publicar bases, aclaraciones, evaluaciones y adjudicaciones en www.mercadopublico.cl. |
| Eficiencia | Optimizar la relación calidad-precio en las adquisiciones. |
| Probidad | Evitar conflictos de interés y declarar inhabilidades. |
#### 3 Glosario de Terminos
#### ID
MANUAL-COMPRAS-SEC-I-GLOSARIO-01
#### Terminos
-
  #### ID
  MANUAL-COMPRAS-GLOS-PAC
  #### Sigla
  PAC
  #### Def
  Plan Anual de Compras.
-
  #### ID
  MANUAL-COMPRAS-GLOS-OC
  #### Sigla
  OC
  #### Def
  Orden de Compra emitida en Mercado Público.
-
  #### ID
  MANUAL-COMPRAS-GLOS-CONVENIO-MARCO
  #### Termino
  Convenio Marco
  #### Def
  Acuerdo suscrito por ChileCompra con proveedores para compras directas a precios predefinidos.
-
  #### ID
  MANUAL-COMPRAS-GLOS-CDP
  #### Sigla
  CDP
  #### Def
  Certificado de Disponibilidad Presupuestaria.
-
  #### ID
  MANUAL-COMPRAS-GLOS-RECEPCION-CONFORME
  #### Termino
  Recepción Conforme
  #### Def
  Acto formal que valida la entrega satisfactoria del bien o servicio.
### Seccion II Planificacion de Compras
#### ID
MANUAL-COMPRAS-SEC-II-01
#### 4 Plan Anual de Compras PAC
#### ID
MANUAL-COMPRAS-SEC-II-PAC-01
#### Def
El PAC es el instrumento de planificación que articula necesidades con presupuesto disponible.
#### Elaboracion
#### Responsable
Cada División/Departamento
#### Act
Envía requerimientos a la Unidad de Abastecimiento
#### Plazo
Antes del 15 de Noviembre del año anterior
#### Consolidacion
#### Responsable
Unidad de Abastecimiento
#### Act
Integra y prioriza las necesidades
#### Criterios de Priorizacion
| Criterio |
| --- |
| Criticidad operativa. |
| Disponibilidad presupuestaria. |
| Alineamiento con metas institucionales. |
#### Aprobacion
#### Responsable
Administrador Regional
#### Act
Aprueba el PAC consolidado
#### Ctx
Mediante Resolución Exenta.
#### Publicacion
#### Responsable
Unidad de Abastecimiento
#### Act
Publica en Mercado Público
#### Plazo
Dentro de los primeros 30 días del año calendario
#### Modificaciones
#### Cond
Durante el año
#### Req
Permitidas mediante resolución fundada
#### Req Actualizacion
| Req |
| --- |
| Actualizar la publicación en el portal. |
#### 5 Tipos de Requerimientos
#### ID
MANUAL-COMPRAS-SEC-II-REQS-01
#### Tipos
| Tipo | Def |
| --- | --- |
| Planificados (PAC) | Incluidos en la programación anual. |
| Extraordinarios | Necesidades imprevistas que requieren justificación escrita del área solicitante y visación DAF. |
| Urgentes | Situaciones de emergencia que permiten plazos abreviados según Reglamento (Art. 43). |
#### 6 Reserva Presupuestaria Previa
#### ID
MANUAL-COMPRAS-SEC-II-RESERVA-01
#### Prohib
Ningún proceso de compra inicia sin CDP vigente.
#### Reqs
| Req |
| --- |
| El CDP debe emitirse desde el sistema financiero antes de la publicación del llamado o emisión de la OC. |
| La pre-afectación bloquea los recursos hasta la adjudicación o desistimiento. |
### Seccion III Mecanismos de Compra
#### ID
MANUAL-COMPRAS-SEC-III-01
#### 7 Convenio Marco CM
#### ID
MANUAL-COMPRAS-SEC-III-CM-01
#### Def
Modalidad preferente para bienes y servicios estandarizados.
#### Catalogo ChileCompra
#### Ctx
Se accede vía tienda electrónica en www.mercadopublico.cl.
#### Proceso
#### Proc
| Act |
| --- |
| Selección de producto |
| Emisión de OC |
| Aceptación proveedor |
| Despacho/Prestación |
#### Ventaja
#### Res
No requiere proceso licitatorio individual.
#### Restriccion
#### Prohib
No aplica para bienes o servicios no catalogados.
#### 8 Licitacion Publica
#### ID
MANUAL-COMPRAS-SEC-III-LP-01
#### Req
Obligatoria para compras de bienes, servicios y ejecución de proyectos de inversión (Subtítulo 31) superiores a 1.000 UTM (salvo Convenio Marco).
#### Bases Administrativas
#### Ctx
Condiciones generales, plazos, garantías, causales de inadmisibilidad.
#### Bases Tecnicas
#### Ctx
Especificaciones del bien o servicio, criterios de evaluación técnica.
#### Publicacion
#### Plazos
- Mínimo 20 días corridos para ofertar (licitación normal).
- 10 días (licitación abreviada por monto < 100 UTM).
#### Criterios de Evaluacion
#### Req
Deben definirse en las bases con ponderaciones claras (Técnico, Económico, Plazos, etc.).
#### Comision Evaluadora
#### Reqs
| Req |
| --- |
| Mínimo 3 integrantes designados por resolución. |
| Incluye al menos un funcionario del área técnica requirente. |
#### Acta de Evaluacion
#### Req
Documento fundado que justifica la puntuación de cada oferente.
#### Adjudicacion
#### Req
Por Resolución Exenta del Gobernador Regional, publicada en el portal.
#### 9 Licitacion Privada y Trato Directo
#### ID
MANUAL-COMPRAS-SEC-III-EXCEPCIONES-01
#### Def
Modalidades excepcionales sujetas a causales legales taxativas.
#### Trato Directo Art 8 Ley 19886
#### ID
MANUAL-COMPRAS-SEC-III-TD-01
#### Causales
| Causal |
| --- |
| Proveedor único. |
| Emergencias calificadas. |
| Compras < 10 UTM. |
| Contratos de prórroga por continuidad de servicio (máximo 12 meses). |
#### Requisitos
| Req |
| --- |
| Resolución fundada que invoque la causal específica. |
| Publicación en Mercado Público (salvo montos menores). |
| Visación del Jefe DAF para montos > 100 UTM. |
#### 10 Grandes Compras Licitaciones mayores a 5000 UTM
#### ID
MANUAL-COMPRAS-SEC-III-GRANDES-01
#### Reqs
| Req |
| --- |
| Requieren visación previa de la División Jurídica sobre las bases. |
| Garantía de seriedad de la oferta obligatoria (generalmente 5% del presupuesto estimado). |
| Plazo de ofertas mínimo 30 días corridos. |
| Evaluación técnica puede incluir visitas a terreno o demostraciones. |
### Seccion IV Ejecucion de Ordenes de Compra
#### ID
MANUAL-COMPRAS-SEC-IV-01
#### 11 Generacion de la OC
#### ID
MANUAL-COMPRAS-SEC-IV-OC-01
#### Def
La OC es el acto administrativo que formaliza el compromiso con el proveedor.
#### Reqs
| Req |
| --- |
| Se emite en Mercado Público tras la adjudicación (licitaciones) o selección (CM/Trato Directo). |
#### Contenido Obligatorio
| Req |
| --- |
| Descripción detallada del bien/servicio. |
| Cantidad y precio unitario. |
| Plazo de entrega/ejecución. |
| Lugar de entrega. |
| Imputación presupuestaria (Subtítulo/Ítem/Asignación). |
#### 12 Aceptacion y Rechazo
#### ID
MANUAL-COMPRAS-SEC-IV-ACEPTACION-01
#### Plazo
48 horas hábiles
#### Req
El proveedor tiene 48 horas hábiles para aceptar la OC en el portal (salvo indicación distinta en bases).
#### Res
OC rechazada o no aceptada permite re-adjudicar al siguiente oferente mejor evaluado.
#### 13 Recepcion Conforme
#### ID
MANUAL-COMPRAS-SEC-IV-RECEPCION-01
#### Def
Hito crítico que habilita el devengo y posterior pago.
#### Bienes
#### Proc
| Act |
| --- |
| La bodega o área solicitante verifica cantidad, calidad y concordancia con OC. |
| Genera Acta de Recepción física o digital. |
#### Servicios
#### Proc
-
  #### Responsable
  Administrador del contrato
-
  #### Act
  Certifica el cumplimiento mediante Informe de Conformidad.
#### Integracion Contable
#### Res
La recepción conforme genera automáticamente el devengo presupuestario y el pasivo contable (Cuentas por Pagar).
#### Pago Electronico Obligatorio
#### ID
MANUAL-COMPRAS-SEC-IV-PAGO-ELECTRONICO-01
#### Src
Art. 8 de la Ley de Presupuestos
#### Req
Todos los pagos a proveedores deben realizarse exclusivamente mediante transferencia electrónica de fondos.
#### Prohib
Pago en efectivo o cheque, salvo excepciones legalmente autorizadas.
#### Nota Recepcion Fisica Bienes
#### Ctx Optional
Para el procedimiento detallado de recepción física de bienes, consulte el Manual 2.2: Inventarios (./manual_2_2_inventarios.md) §7.
#### 14 Devoluciones y Reclamos
#### ID
MANUAL-COMPRAS-SEC-IV-DEVOLUCIONES-01
#### Plazo
8 días corridos
#### Reqs
| Req |
| --- |
| Plazo de 8 días corridos desde la recepción para reclamar la factura electrónica en el SII. |
| Devoluciones por no conformidad deben documentarse con Acta de Rechazo indicando las causales. |
| El proveedor tiene plazo según contrato/OC para subsanar o reemplazar. |
### Seccion V Gestion de Contratos
#### ID
MANUAL-COMPRAS-SEC-V-01
#### 15 Formalizacion de Contratos
#### ID
MANUAL-COMPRAS-SEC-V-FORMALIZACION-01
#### Req
Obligatorio para:
#### Casos
| Caso |
| --- |
| Licitaciones > 100 UTM. |
| Servicios de tracto sucesivo. |
| Obras civiles. |
#### Contenido del Contrato
| Req |
| --- |
| Identificación de las partes. |
| Objeto y alcance. |
| Precio y modalidad de pago (hitos, mensualidades, etc.). |
| Plazos de ejecución. |
| Garantías exigidas. |
| Multas y sanciones. |
| Causales de término anticipado. |
#### 16 Administracion del Contrato
#### ID
MANUAL-COMPRAS-SEC-V-ADMIN-01
#### Administrador del Contrato
#### Req
Funcionario designado por resolución, responsable del seguimiento técnico y cumplimiento de hitos.
#### Libro de Obra Bitacora
#### Req
Registro de incidencias, instrucciones y acuerdos durante la ejecución (obligatorio en contratos de obra).
#### Estados de Pago
#### Def
Documentos que certifican el avance para liberar pagos parciales según hitos.
#### Modificaciones
#### Reqs
| Req |
| --- |
| Aumentos o disminuciones de hasta 30% del monto original requieren resolución fundada. |
| Sobre 30% requieren nueva licitación. |
#### 17 Garantias Contractuales
#### ID
MANUAL-COMPRAS-SEC-V-GARANTIAS-01
#### Tipos
| Tipo | Def |
| --- | --- |
| Seriedad de la Oferta | Devuelta tras adjudicación a oferentes no seleccionados. |
| Fiel Cumplimiento | Generalmente 5% del monto contratado, vigente hasta recepción final + plazo de responsabilidad. |
| Correcta Ejecución (Obras) | Puede exigirse por el plazo de responsabilidad post-recepción (típicamente 12 meses). |
#### Custodia
#### Ctx
Las garantías físicas (boletas, pólizas) se custodian en Tesorería. Las electrónicas se registran en el sistema de garantías.
#### 18 Multas y Sanciones
#### ID
MANUAL-COMPRAS-SEC-V-MULTAS-01
#### Reqs
| Req |
| --- |
| Deben estar contempladas en las bases y el contrato. |
| Causales típicas: Atraso en entrega, incumplimiento parcial, calidad deficiente. |
#### Procedimiento
#### Proc
-
  #### Act
  Informe del administrador
-
  #### Act
  Notificación al proveedor
-
  #### Plazo
  Plazo de descargos (5 días hábiles)
-
  #### Act
  Resolución que aplica o desestima la multa.
#### Cobro
#### Proc
| Act |
| --- |
| Descuento directo de estados de pago |
| Ejecución de garantía |
#### 19 Termino del Contrato
#### ID
MANUAL-COMPRAS-SEC-V-TERMINO-01
#### Tipos
| Tipo | Def |
| --- | --- |
| Término Natural | Cumplimiento del objeto en plazo. |
| Término Anticipado | Por incumplimiento grave, mutuo acuerdo, o causales de fuerza mayor. |
| Recepción Final | Acta que cierra el contrato y libera garantías (tras plazo de responsabilidad si aplica). |
### Seccion VI Control Transparencia y Evaluacion
#### ID
MANUAL-COMPRAS-SEC-VI-01
#### 20 Interoperabilidad con Mercado Publico
#### ID
MANUAL-COMPRAS-SEC-VI-INTEROP-01
#### Reqs
| Req |
| --- |
| Toda operación debe reflejarse en www.mercadopublico.cl. |
| El sistema institucional (SIGAS o equivalente) debe sincronizar OC, estados de pago y recepciones. |
| Descarga automática de actas de adjudicación para trazabilidad. |
#### 21 Portal de Proveedores
#### ID
MANUAL-COMPRAS-SEC-VI-PORTAL-01
#### Def
Herramienta de transparencia que permite a proveedores consultar:
#### Funcionalidades
| Funcionalidad |
| --- |
| Estado de sus órdenes de compra. |
| Estado de facturas y pagos. |
| Historial de transacciones. |
#### 22 Evaluacion de Proveedores
#### ID
MANUAL-COMPRAS-SEC-VI-EVAL-01
#### Frecuencia
- Al cierre de cada contrato
- Anualmente para contratos de tracto sucesivo
#### Criterios
- Cumplimiento de plazos
- Calidad del producto/servicio
- Respuesta ante incidencias
#### Registro
#### Req
La calificación se incorpora al Historial de Proveedores institucional.
#### Consecuencias
#### Res
Proveedores con evaluación deficiente pueden ser excluidos de futuras licitaciones (según bases).
#### 23 Reportes y Auditoria
#### ID
MANUAL-COMPRAS-SEC-VI-REPORTES-01
#### Reportes
- Informe Mensual de Compras: Resumen de OC emitidas, montos, mecanismos utilizados.
- Informe de Contratos Vigentes: Estado de avance, hitos pendientes, alertas de vencimiento.
#### Indicadores de Gestion
| Indicador |
| --- |
| % de compras vía Convenio Marco. |
| % de licitaciones declaradas desiertas. |
| Tiempo promedio de adjudicación. |
| Cumplimiento de plazos de pago a 30 días. |
### Nota Final
#### Ctx
Este manual establece los lineamientos para una gestión de compras eficiente, transparente y conforme a la normativa de contratación pública.

## Referencias Cruzadas
### ID
GN-MANUAL-COMPRAS-XREF-01
### Ctx Optional
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_1_presupuesto.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_2_contabilidad.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_3_tesoreria_koda.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_2_inventarios.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_2_remuneraciones.yml
