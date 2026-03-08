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
    preserved_facts:
    - AI-Remediator=KODA-TRANSFORMER
    - Creation-Date=2025-12-14
    - Ctx=Asegurar integridad contable bajo normativa NICSP y CGR; registro fidedigno,
      oportuno y trazable de hechos económicos del GORE Ñuble; operación diaria +
      procesos críticos de cierre financiero.
    - 'Definitions.Documentos_y_Registros[0].Def=Comprobante Contable: documento fuente
      único de registro (papel o digital firmado).'
    - Definitions.Documentos_y_Registros[0].ID=DEF-COMPROBANTE-CONTABLE
    - 'Definitions.Documentos_y_Registros[1].Def=Libro Banco: registro cronológico
      de movimientos bancarios; debe cuadrar diariamente con saldo contable de cuenta
      ''Banco''.'
    - Definitions.Documentos_y_Registros[1].ID=DEF-LIBRO-BANCO
    - 'Definitions.Documentos_y_Registros[2].Def=Libro de Honorarios Auxiliar: emisión
      mensual; más certificados de retención anuales (DJ 1879).'
    - Definitions.Documentos_y_Registros[2].ID=DEF-LIBRO-HONORARIOS-AUX
    - 'Definitions.Documentos_y_Registros[3].Def=Minuta explicativa: respaldo obligatorio
      para comprobantes manuales (ajustes/regularizaciones/depreciaciones/correcciones).'
    - Definitions.Documentos_y_Registros[3].ID=DEF-MINUTA-EXPLICATIVA
    - 'Definitions.Documentos_y_Registros[4].Def=Asiento Tipo: asiento contable pre-parametrizado
      en ERP para operaciones recurrentes.'
    - Definitions.Documentos_y_Registros[4].ID=DEF-ASIENTO-TIPO
    - 'Definitions.Documentos_y_Registros[5].Def=Matriz de Devengamiento: parametrización
      en ERP que asocia imputación presupuestaria (Subtítulo/Ítem/Asig) con asiento
      contable patrimonial.'
    - Definitions.Documentos_y_Registros[5].ID=DEF-MATRIZ-DEVENGAMIENTO
    - 'Definitions.Normas_y_Conceptos[0].Def=NICSP: Normas Internacionales de Contabilidad
      para el Sector Público; base del estándar contable chileno.'
    - Definitions.Normas_y_Conceptos[0].ID=DEF-NICSP
    - 'Definitions.Normas_y_Conceptos[1].Def=Devengo: reconocimiento de una obligación
      de pago o derecho de cobro, independiente de fecha efectiva de pago o recaudación.'
    - Definitions.Normas_y_Conceptos[1].ID=DEF-DEVENGO
    - 'Definitions.Normas_y_Conceptos[2].Def=Deuda Flotante: obligaciones devengadas
      y no pagadas al cierre del ejercicio.'
    - Definitions.Normas_y_Conceptos[2].ID=DEF-DEUDA-FLOTANTE
    - 'Definitions.Normas_y_Conceptos[3].Def=Interoperabilidad: capacidad de intercambiar
      información financiera automáticamente entre sistemas (ej.: ERP <-> Banco).'
    - Definitions.Normas_y_Conceptos[3].ID=DEF-INTEROPERABILIDAD
    - 'Definitions.Organos_y_Unidades[0].Def=CGR: Contraloría General de la República.'
    - Definitions.Organos_y_Unidades[0].ID=DEF-CGR
    - 'Definitions.Organos_y_Unidades[1].Def=DIPRES: Dirección de Presupuestos.'
    - Definitions.Organos_y_Unidades[1].ID=DEF-DIPRES
    - 'Definitions.Organos_y_Unidades[2].Def=DIPIR: División de Presupuesto e Inversión
      Regional.'
    - Definitions.Organos_y_Unidades[2].ID=DEF-DIPIR
    - 'Definitions.Organos_y_Unidades[3].Def=Jefe de Finanzas: responsable con atribución
      para crear nuevos modelos de asientos tipo.'
    - Definitions.Organos_y_Unidades[3].ID=DEF-JEFE-FINANZAS
    - 'Definitions.Organos_y_Unidades[4].Def=Tesorero: responsable de firma del Anexo
      CGR de Conciliación Bancaria (junto con Jefe de Finanzas).'
    - Definitions.Organos_y_Unidades[4].ID=DEF-TESORERO
    - 'Definitions.Sistemas_y_Modulos[0].Def=SIGFE: Sistema de Información para la
      Gestión Financiera del Estado (agregador central).'
    - Definitions.Sistemas_y_Modulos[0].ID=DEF-SIGFE
    - 'Definitions.Sistemas_y_Modulos[1].Def=ERP: sistema ERP financiero institucional;
      mantiene Matriz de Devengamiento y asientos patrimoniales.'
    - Definitions.Sistemas_y_Modulos[1].ID=DEF-ERP
    - 'Definitions.Sistemas_y_Modulos[2].Def=SIGPER: módulo/sistema de remuneraciones.'
    - Definitions.Sistemas_y_Modulos[2].ID=DEF-SIGPER
    - 'Definitions.Sistemas_y_Modulos[3].Def=SIGAS: módulo/sistema de activo fijo
      y existencias (bodega).'
    - Definitions.Sistemas_y_Modulos[3].ID=DEF-SIGAS
    - 'Definitions.Sistemas_y_Modulos[4].Def=SII: Servicio de Impuestos Internos (boletas
      electrónicas honorarios).'
    - Definitions.Sistemas_y_Modulos[4].ID=DEF-SII
    - 'Definitions.Sistemas_y_Modulos[5].Def=SISREC: Sistema de Rendición Electrónica
      de Cuentas de CGR.'
    - Definitions.Sistemas_y_Modulos[5].ID=DEF-SISREC
    - Format=KODA/Spec
    - Human-Creator=GORE Ñuble
    - Human-Editor=GORE Ñuble
    - ID=GN-MANUAL-CONTAB-CIERRE-01
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
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.ID=GN-MANUAL-CONTAB-ROOT-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Obj[0]=Asegurar integridad
      contable bajo normativa NICSP y CGR.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Obj[1]=Garantizar
      registro fidedigno, oportuno y trazable de hechos económicos del Gobierno Regional.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Centralizacion_Contable.Casos[0].Area=Remuneraciones
      (SIGPER)
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Centralizacion_Contable.Casos[0].ID=GN-MANUAL-CONTAB-S3-CENTRAL-REM-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Centralizacion_Contable.Casos[0].Proc[0]=Centralizar
      mensualmente tras cierre de sueldos.
    - 'Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Centralizacion_Contable.Casos[0].Proc[1]=Validar
      integridad total: Monto Bruto = Líquido + Leyes Sociales + Retenciones.'
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Centralizacion_Contable.Casos[0].Ref=DEF-SIGPER
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Centralizacion_Contable.Casos[1].Area=Activo
      Fijo y Existencias (SIGAS)
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Centralizacion_Contable.Casos[1].ID=GN-MANUAL-CONTAB-S3-CENTRAL-AF-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Centralizacion_Contable.Casos[1].Proc[0]=Entrada
      de bodega genera alta de activo/existencia + pasivo con proveedor (Facturas
      por Recibir).
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Centralizacion_Contable.Casos[1].Proc[1]=Consumo
      de bodega genera gasto patrimonial.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Centralizacion_Contable.Casos[1].Ref=DEF-SIGAS
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Centralizacion_Contable.Casos[2].Area=Interoperabilidad
      Externa
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Centralizacion_Contable.Casos[2].ID=GN-MANUAL-CONTAB-S3-CENTRAL-INTEROP-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Centralizacion_Contable.Casos[2].Proc[0]=Recepción
      automática de decretos de modificación presupuestaria desde DIPRES (si tecnología
      lo permite).
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Centralizacion_Contable.Casos[2].Proc[1]=Recepción
      de cartolas bancarias.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Centralizacion_Contable.Casos[2].Ref[0]=DEF-DIPRES
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Centralizacion_Contable.Casos[2].Ref[1]=DEF-INTEROPERABILIDAD
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Centralizacion_Contable.Def=Proceso
      crítico de integración de sistemas satélites al ERP Financiero.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Centralizacion_Contable.ID=GN-MANUAL-CONTAB-S3-CENTRALIZACION-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Comprobantes_Contables.Def=Comprobante
      Contable es documento fuente único de registro (papel o digital firmado).
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Comprobantes_Contables.ID=GN-MANUAL-CONTAB-S3-COMPROB-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Comprobantes_Contables.Ref=DEF-COMPROBANTE-CONTABLE
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Comprobantes_Contables.Tipos[0].Def=Se
      generan sin intervención humana directa al aprobarse hitos en módulos auxiliares.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Comprobantes_Contables.Tipos[0].Ex[0]=Recepción
      Conforme en Bodega genera el devengo.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Comprobantes_Contables.Tipos[0].ID=GN-MANUAL-CONTAB-S3-COMPROB-AUTO-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Comprobantes_Contables.Tipos[0].Tipo=Comprobantes
      Automáticos (Interfaz)
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Comprobantes_Contables.Tipos[1].ID=GN-MANUAL-CONTAB-S3-COMPROB-MAN-01
    - 'Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Comprobantes_Contables.Tipos[1].Prohib=Uso
      fuera de: ajustes, regularizaciones, depreciaciones manuales, correcciones de
      errores.'
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Comprobantes_Contables.Tipos[1].Ref=DEF-MINUTA-EXPLICATIVA
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Comprobantes_Contables.Tipos[1].Req[0]=V°B°
      de jefatura.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Comprobantes_Contables.Tipos[1].Req[1]=Adjuntar
      minuta explicativa.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Comprobantes_Contables.Tipos[1].Tipo=Comprobantes
      Manuales
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Comprobantes_Contables.Validaciones_Sistema.Ex[0]=Gasto
      presupuestario sin contrapartida patrimonial de gasto o activo.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Comprobantes_Contables.Validaciones_Sistema.ID=GN-MANUAL-CONTAB-S3-COMPROB-VAL-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Comprobantes_Contables.Validaciones_Sistema.Req[0]=Sistema
      bloquea comprobantes descuadrados.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Comprobantes_Contables.Validaciones_Sistema.Req[1]=Sistema
      bloquea comprobantes que rompan lógica Financiero-Económico.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.Anticipos.ID=GN-MANUAL-CONTAB-S3-DEUDA-ANT-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.Anticipos.Prohib=Nuevos
      anticipos a funcionarios/proveedores con rendiciones pendientes.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.Anticipos.Req=Control
      estricto de Fondos por Rendir y viáticos.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.Cuentas_por_Pagar.ID=GN-MANUAL-CONTAB-S3-DEUDA-CXP-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.Cuentas_por_Pagar.Proc[0]=Monitoreo
      de antigüedad de deuda (Aging).
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.Cuentas_por_Pagar.Ref=DEF-DEVENGO
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.Cuentas_por_Pagar.Req=Alerta
      obligatoria sobre facturas devengadas con más de 30 días de antigüedad (cumplimiento
      Ley Pago a 30 Días).
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.Def=Control
      de posición financiera.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.Deuda_Flotante.ID=GN-MANUAL-CONTAB-S3-DEUDA-DF-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.Deuda_Flotante.Ref[0]=DEF-DEUDA-FLOTANTE
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.Deuda_Flotante.Ref[1]=DEF-DEVENGO
    - 'Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.Deuda_Flotante.Req=Al
      cierre de año: segregación clara de compromisos devengados no pagados para imputación
      a caja del año siguiente.'
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.ID=GN-MANUAL-CONTAB-S3-DEUDA-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.Rendiciones_Cuentas_Externas_SISREC.ID=GN-MANUAL-CONTAB-S3-DEUDA-SISREC-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.Rendiciones_Cuentas_Externas_SISREC.Proc_Contable_GORE[0].Act=La
      UCR (Unidad de Control de Rendiciones) centraliza la recepción y deriva al Referente
      Técnico-Financiero (RTF).
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.Rendiciones_Cuentas_Externas_SISREC.Proc_Contable_GORE[0].Paso=1.
      Recepción y Derivación
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.Rendiciones_Cuentas_Externas_SISREC.Proc_Contable_GORE[1].Act=Revisión
      física y financiera en SISREC. Aprobación o devolución por observaciones.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.Rendiciones_Cuentas_Externas_SISREC.Proc_Contable_GORE[1].Paso=2.
      Revisión Técnica (Analista Otorgante)
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.Rendiciones_Cuentas_Externas_SISREC.Proc_Contable_GORE[2].Act=Firma
      del Informe de Aprobación por Jefatura DAF mediante Firma Electrónica Avanzada
      (FEA).
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.Rendiciones_Cuentas_Externas_SISREC.Proc_Contable_GORE[2].Paso=3.
      Firma y Aprobación (Encargado Otorgante)
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.Rendiciones_Cuentas_Externas_SISREC.Proc_Contable_GORE[3].Act=Descarga
      del informe aprobado y ejecución del asiento de rendición en SIGFE (Reverso
      de Anticipos / Reconocimiento de Gasto).
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.Rendiciones_Cuentas_Externas_SISREC.Proc_Contable_GORE[3].Dln=2
      días hábiles tras aprobación técnica.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.Rendiciones_Cuentas_Externas_SISREC.Proc_Contable_GORE[3].Paso=4.
      Contabilización SIGFE
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.Rendiciones_Cuentas_Externas_SISREC.Ref[0]=DEF-SISREC
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.Rendiciones_Cuentas_Externas_SISREC.Ref[1]=DEF-CGR
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.Rendiciones_Cuentas_Externas_SISREC.Ref[2]=DEF-SIGFE
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Deuda_Institucional.Rendiciones_Cuentas_Externas_SISREC.Req=Transferencias
      a terceros (Subtítulos 24 y 33) deben rendirse obligatoriamente vía SISREC (CGR)
      conforme a Res. Ex. N° 1.858/2023.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Honorarios.Def=Registro
      de prestaciones de servicios personales (boletas de honorarios).
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Honorarios.ID=GN-MANUAL-CONTAB-S3-HONOR-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Honorarios.Proc[0]=Importación
      de Boletas Electrónicas desde SII.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Honorarios.Proc[1]=Cálculo
      automático de retención (tasa vigente).
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Honorarios.Proc[2]=Generación
      de obligación de pago (Devengo) y cuentas por pagar.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Honorarios.Proc[3]=Emisión
      mensual Libro de Honorarios Auxiliar.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Honorarios.Proc[4]=Emisión
      certificados de retención anuales (DJ 1879).
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Honorarios.Ref[0]=DEF-SII
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Honorarios.Ref[1]=DEF-DEVENGO
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.Gestion_de_Honorarios.Ref[2]=DEF-LIBRO-HONORARIOS-AUX
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_III_Registro_y_Operacion_Contable.ID=GN-MANUAL-CONTAB-S3-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Biblioteca_de_Asientos_Contables_Memoria_Contable.Asientos_Tipo[0].Def=Automático
      desde módulo SIGPER.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Biblioteca_de_Asientos_Contables_Memoria_Contable.Asientos_Tipo[0].ID=GN-MANUAL-CONTAB-S2-ASIENTO-REM-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Biblioteca_de_Asientos_Contables_Memoria_Contable.Asientos_Tipo[0].Nombre=Devengo
      de Remuneraciones
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Biblioteca_de_Asientos_Contables_Memoria_Contable.Asientos_Tipo[0].Ref[0]=DEF-ASIENTO-TIPO
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Biblioteca_de_Asientos_Contables_Memoria_Contable.Asientos_Tipo[0].Ref[1]=DEF-SIGPER
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Biblioteca_de_Asientos_Contables_Memoria_Contable.Asientos_Tipo[1].Def=Automático
      desde módulo Adquisiciones/Activo Fijo.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Biblioteca_de_Asientos_Contables_Memoria_Contable.Asientos_Tipo[1].ID=GN-MANUAL-CONTAB-S2-ASIENTO-BYS-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Biblioteca_de_Asientos_Contables_Memoria_Contable.Asientos_Tipo[1].Nombre=Devengo
      de Bienes y Servicios
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Biblioteca_de_Asientos_Contables_Memoria_Contable.Asientos_Tipo[1].Ref=DEF-ASIENTO-TIPO
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Biblioteca_de_Asientos_Contables_Memoria_Contable.Asientos_Tipo[2].Def=Asiento
      tipo de recepción de aporte fiscal.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Biblioteca_de_Asientos_Contables_Memoria_Contable.Asientos_Tipo[2].ID=GN-MANUAL-CONTAB-S2-ASIENTO-ING-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Biblioteca_de_Asientos_Contables_Memoria_Contable.Asientos_Tipo[2].Nombre=Ingresos
      por Transferencia
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Biblioteca_de_Asientos_Contables_Memoria_Contable.Asientos_Tipo[2].Ref=DEF-ASIENTO-TIPO
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Biblioteca_de_Asientos_Contables_Memoria_Contable.Asientos_Tipo[3].Def=Asiento
      tipo para regularizar anticipos.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Biblioteca_de_Asientos_Contables_Memoria_Contable.Asientos_Tipo[3].ID=GN-MANUAL-CONTAB-S2-ASIENTO-REND-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Biblioteca_de_Asientos_Contables_Memoria_Contable.Asientos_Tipo[3].Nombre=Rendiciones
      de Cuentas
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Biblioteca_de_Asientos_Contables_Memoria_Contable.Asientos_Tipo[3].Ref=DEF-ASIENTO-TIPO
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Biblioteca_de_Asientos_Contables_Memoria_Contable.Creacion_de_Nuevos_Asientos.ID=GN-MANUAL-CONTAB-S2-ASIENTOS-CREA-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Biblioteca_de_Asientos_Contables_Memoria_Contable.Creacion_de_Nuevos_Asientos.Ref=DEF-JEFE-FINANZAS
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Biblioteca_de_Asientos_Contables_Memoria_Contable.Creacion_de_Nuevos_Asientos.Req=Solo
      Jefe de Finanzas tiene atribución para crear nuevos modelos de asientos.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Biblioteca_de_Asientos_Contables_Memoria_Contable.ID=GN-MANUAL-CONTAB-S2-ASIENTOS-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Biblioteca_de_Asientos_Contables_Memoria_Contable.Req=ERP
      opera con Asientos Tipo pre-parametrizados para evitar errores manuales en operaciones
      recurrentes.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Configuracion_del_Ambiente_Contable_Institucional.Asociacion_Contable_Presupuestaria.Ex[0]=Gastos
      en Personal -> Cuenta de Gasto Patrimonial + Pasivo Corriente.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Configuracion_del_Ambiente_Contable_Institucional.Asociacion_Contable_Presupuestaria.ID=GN-MANUAL-CONTAB-S2-ASOC-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Configuracion_del_Ambiente_Contable_Institucional.Asociacion_Contable_Presupuestaria.Mech[0]=Cada
      imputación presupuestaria (Subtítulo/Ítem/Asig) genera automáticamente asiento
      contable patrimonial correcto.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Configuracion_del_Ambiente_Contable_Institucional.Asociacion_Contable_Presupuestaria.Ref[0]=DEF-MATRIZ-DEVENGAMIENTO
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Configuracion_del_Ambiente_Contable_Institucional.Asociacion_Contable_Presupuestaria.Ref[1]=DEF-ERP
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Configuracion_del_Ambiente_Contable_Institucional.Asociacion_Contable_Presupuestaria.Req=Matriz
      de Devengamiento debe mantenerse actualizada en ERP.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Configuracion_del_Ambiente_Contable_Institucional.Centros_de_Costo.Def=Catálogo
      de centros de costo asociado a estructura organizacional (Divisiones/Departamentos)
      para imputar gastos operativos.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Configuracion_del_Ambiente_Contable_Institucional.Centros_de_Costo.ID=GN-MANUAL-CONTAB-S2-CCOSTO-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Configuracion_del_Ambiente_Contable_Institucional.Centros_de_Gestion_IPR.ID=GN-MANUAL-CONTAB-S2-CGESTION-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Configuracion_del_Ambiente_Contable_Institucional.Centros_de_Gestion_IPR.Req=Cada
      IDI funciona como centro de gestión contable; permite balances por proyecto.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Configuracion_del_Ambiente_Contable_Institucional.ID=GN-MANUAL-CONTAB-S2-AMBIENTE-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.ID=GN-MANUAL-CONTAB-S2-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Plan_de_Cuentas_Patrimonial_CGR.Cuentas_de_Orden.Def=Control
      de garantías (boletas, pólizas) y responsabilidades eventuales.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Plan_de_Cuentas_Patrimonial_CGR.Cuentas_de_Orden.ID=GN-MANUAL-CONTAB-S2-PLAN-ORDEN-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Plan_de_Cuentas_Patrimonial_CGR.Cuentas_de_Orden.Res=No
      afectan patrimonio directamente; sí responsabilidad administrativa.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Plan_de_Cuentas_Patrimonial_CGR.ID=GN-MANUAL-CONTAB-S2-PLAN-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Plan_de_Cuentas_Patrimonial_CGR.Niveles_Jerarquicos[0].Ex=Ej.
      1 ACTIVO
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Plan_de_Cuentas_Patrimonial_CGR.Niveles_Jerarquicos[0].Nivel=Título
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Plan_de_Cuentas_Patrimonial_CGR.Niveles_Jerarquicos[1].Ex=Ej.
      11 ACTIVOS CIRCULANTES
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Plan_de_Cuentas_Patrimonial_CGR.Niveles_Jerarquicos[1].Nivel=Grupo
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Plan_de_Cuentas_Patrimonial_CGR.Niveles_Jerarquicos[2].Ex=Ej.
      111 DISPONIBILIDADES
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Plan_de_Cuentas_Patrimonial_CGR.Niveles_Jerarquicos[2].Nivel=Subgrupo
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Plan_de_Cuentas_Patrimonial_CGR.Niveles_Jerarquicos[3].Ex=Ej.
      11101 BANCO ESTADO
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Plan_de_Cuentas_Patrimonial_CGR.Niveles_Jerarquicos[3].Nivel=Cuenta
      Nivel 1
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Plan_de_Cuentas_Patrimonial_CGR.Niveles_Jerarquicos[4].Ex=Ej.
      1110101 CUENTA ÚNICA FISCAL
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Plan_de_Cuentas_Patrimonial_CGR.Niveles_Jerarquicos[4].Nivel=Cuenta
      Nivel 2
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Plan_de_Cuentas_Patrimonial_CGR.Niveles_Jerarquicos[5].Def=Niveles
      adicionales para control de gestión.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Plan_de_Cuentas_Patrimonial_CGR.Niveles_Jerarquicos[5].Ex=Ej.
      auxiliar por Proyecto/IPR.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Plan_de_Cuentas_Patrimonial_CGR.Niveles_Jerarquicos[5].Nivel=Desagregados
      Institucionales
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Plan_de_Cuentas_Patrimonial_CGR.Ref=DEF-CGR
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_II_Plan_de_Cuentas_y_Estructura_Contable.Plan_de_Cuentas_Patrimonial_CGR.Req=GORE
      adopta integralmente Plan de Cuentas definido por CGR.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_IV_Integracion_Bancaria_y_Conciliacion_Contable.Administracion_de_Cuentas_Corrientes.ID=GN-MANUAL-CONTAB-S4-CC-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_IV_Integracion_Bancaria_y_Conciliacion_Contable.Administracion_de_Cuentas_Corrientes.Libro_Banco.ID=GN-MANUAL-CONTAB-S4-CC-LIBRO-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_IV_Integracion_Bancaria_y_Conciliacion_Contable.Administracion_de_Cuentas_Corrientes.Libro_Banco.Ref=DEF-LIBRO-BANCO
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_IV_Integracion_Bancaria_y_Conciliacion_Contable.Administracion_de_Cuentas_Corrientes.Libro_Banco.Req=Debe
      cuadrar diariamente con saldo contable de cuenta 'Banco'.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_IV_Integracion_Bancaria_y_Conciliacion_Contable.Administracion_de_Cuentas_Corrientes.Req=Registro
      único de todas las cuentas corrientes institucionales.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_IV_Integracion_Bancaria_y_Conciliacion_Contable.Administracion_de_Cuentas_Corrientes.Tipos_Cuenta[0]=FNDR
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_IV_Integracion_Bancaria_y_Conciliacion_Contable.Administracion_de_Cuentas_Corrientes.Tipos_Cuenta[1]=Operacionales
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_IV_Integracion_Bancaria_y_Conciliacion_Contable.Administracion_de_Cuentas_Corrientes.Tipos_Cuenta[2]=Fondos
      de Terceros
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_IV_Integracion_Bancaria_y_Conciliacion_Contable.Conciliacion_Bancaria.Def=Proceso
      de control interno para validar disponibilidad real de recursos.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_IV_Integracion_Bancaria_y_Conciliacion_Contable.Conciliacion_Bancaria.Frecuencia[0]=Diaria
      para gestión de caja.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_IV_Integracion_Bancaria_y_Conciliacion_Contable.Conciliacion_Bancaria.Frecuencia[1]=Mensual
      para cierre contable.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_IV_Integracion_Bancaria_y_Conciliacion_Contable.Conciliacion_Bancaria.ID=GN-MANUAL-CONTAB-S4-CONCIL-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_IV_Integracion_Bancaria_y_Conciliacion_Contable.Conciliacion_Bancaria.Informe.ID=GN-MANUAL-CONTAB-S4-CONCIL-INF-01
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_IV_Integracion_Bancaria_y_Conciliacion_Contable.Conciliacion_Bancaria.Informe.Ref[0]=DEF-CGR
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_IV_Integracion_Bancaria_y_Conciliacion_Contable.Conciliacion_Bancaria.Informe.Ref[1]=DEF-TESORERO
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_IV_Integracion_Bancaria_y_Conciliacion_Contable.Conciliacion_Bancaria.Informe.Ref[2]=DEF-JEFE-FINANZAS
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_IV_Integracion_Bancaria_y_Conciliacion_Contable.Conciliacion_Bancaria.Informe.Res=Generar
      Anexo CGR de Conciliación Bancaria firmado por Tesorero y Jefe de Finanzas.
    - Manual_1_2_Contabilidad_Gubernamental_y_Cierre_Financiero.Seccion_IV_Integracion_Bancaria_y_Conciliacion_Contable.Conciliacion_Bancaria.Metodo[0]=Carga
      electrónica de cartola bancaria (archivo del banco).
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
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
