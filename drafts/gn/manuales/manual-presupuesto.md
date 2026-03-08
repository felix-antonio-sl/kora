---
_manifest:
  urn: urn:gn:kb:manual-presupuesto
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/gestion/kb_gn_043_manual_presupuesto_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- presupuesto
- sigfe
- fndr
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/gestion/kb_gn_043_manual_presupuesto_koda.yml
    source_hashes:
      domains/gn/03_operacion/gestion/kb_gn_043_manual_presupuesto_koda.yml: 2fd27082c96bc49473323ed93d8e54394b1e1d5a9fac13e69880c9abeec64e86
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.13
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 19
    meat_count: 290
    fat_count: 0
    preserved_facts:
    - AI-Remediator=KODA-TRANSFORMER
    - Authoritative-Source.Last-Validated=2025-12-18
    - Authoritative-Source.Path=staging/temp/brutos ordenados/02_finanzas_control/OF
      CIRCULAR 11 (038FF)_30.01_INSTRUCCIONES APLICACIÓN GLOSAS GORES.koda.yml
    - Authoritative-Source.Priority=1
    - Authoritative-Source.Type=Official-Circular-DIPRES
    - Creation-Date=2025-12-14
    - 'Ctx=Estandarizar ciclo de vida de recursos financieros regionales: planificación
      -> formulación -> aprobación -> ejecución -> control -> cierre; cumplimiento
      Ley de Presupuestos y SAF del Estado.'
    - 'Definitions.Cadena_Presupuestaria[0].Def=CDP (Certificado de Disponibilidad
      Presupuestaria): Documento previo obligatorio que certifica saldo; ningún proceso
      de compra o convenio inicia sin CDP.'
    - Definitions.Cadena_Presupuestaria[0].ID=DEF-CDP
    - 'Definitions.Cadena_Presupuestaria[1].Def=Compromiso: Acto administrativo (OC/Contrato/Resolución
      Convenio) que afecta el presupuesto; reserva recursos definitivamente para un
      tercero.'
    - Definitions.Cadena_Presupuestaria[1].ID=DEF-COMPROMISO
    - 'Definitions.Cadena_Presupuestaria[2].Def=Devengo: Hito de recepción conforme;
      genera obligación de pago y pasivo contable; debe ser simultáneo a recepción
      de factura/bien.'
    - Definitions.Cadena_Presupuestaria[2].ID=DEF-DEVENGO
    - 'Definitions.Cadena_Presupuestaria[3].Def=Pago: Egreso efectivo de fondos que
      extingue la obligación.'
    - Definitions.Cadena_Presupuestaria[3].ID=DEF-PAGO
    - 'Definitions.Cierre[0].Def=SIC: Saldo Inicial de Caja.'
    - Definitions.Cierre[0].ID=DEF-SIC
    - 'Definitions.Cierre[1].Def=Deuda Flotante: Obligaciones devengadas al 31/12
      pendientes de pago.'
    - Definitions.Cierre[1].ID=DEF-DEUDA-FLOTANTE
    - 'Definitions.Cierre[2].Def=Ítem 34.07 ''Deuda Flotante'': se crea en presupuesto
      del año siguiente para registrar financiamiento.'
    - Definitions.Cierre[2].ID=DEF-ITEM-DEUDA-FLOTANTE
    - 'Definitions.Instrumentos_y_Fondos[0].Def=FNDR: Principal fuente de recursos
      para inversiones; se subdivide en asignaciones regionales (decisión GORE) y
      provisiones (decisión central/mixta).'
    - Definitions.Instrumentos_y_Fondos[0].ID=DEF-FNDR
    - 'Definitions.Instrumentos_y_Fondos[1].Def=FRPD: Recursos destinados a fomento
      productivo, ciencia e innovación.'
    - Definitions.Instrumentos_y_Fondos[1].ID=DEF-FRPD
    - 'Definitions.Instrumentos_y_Fondos[2].Def=PAC (Programación Anual de Caja):
      Proyecta flujo de ingresos y egresos para asegurar liquidez para cumplir obligaciones.'
    - Definitions.Instrumentos_y_Fondos[2].ID=DEF-PAC
    - 'Definitions.Organos_y_Unidades[0].Def=DIPRES (Dirección de Presupuestos): Ente
      rector que define instrucciones, techos y autoriza modificaciones mayores.'
    - Definitions.Organos_y_Unidades[0].ID=DEF-DIPRES
    - 'Definitions.Organos_y_Unidades[1].Def=Gobernador Regional: Responsable de proponer
      el presupuesto al CORE y ejecutarlo.'
    - Definitions.Organos_y_Unidades[1].ID=DEF-GOBERNADOR-REGIONAL
    - 'Definitions.Organos_y_Unidades[2].Def=Consejo Regional (CORE): Aprueba presupuesto
      inicial y modificaciones mayores; fiscaliza la ejecución.'
    - Definitions.Organos_y_Unidades[2].ID=DEF-CORE
    - 'Definitions.Organos_y_Unidades[3].Def=División de Presupuesto e Inversión Regional
      (DIPIR): Unidad técnica responsable de gestión diaria del presupuesto, control
      de saldos y visación de gastos.'
    - Definitions.Organos_y_Unidades[3].ID=DEF-DIPIR
    - 'Definitions.Sistemas_y_Codigos[0].Def=SIGFE: Sistema central (módulo formulación
      y registro ejecución) para gestión financiera del Estado.'
    - Definitions.Sistemas_y_Codigos[0].ID=DEF-SIGFE
    - 'Definitions.Sistemas_y_Codigos[1].Def=BIP: Banco Integrado de Proyectos; código
      requerido para proyectos de inversión.'
    - Definitions.Sistemas_y_Codigos[1].ID=DEF-BIP
    - 'Definitions.Sistemas_y_Codigos[2].Def=IDI: Iniciativa (proyecto) de inversión;
      se controla por código (BIP) y no se mezclan fondos entre proyectos.'
    - Definitions.Sistemas_y_Codigos[2].ID=DEF-IDI
    - Format=KODA/Spec
    - Human-Creator=GORE Ñuble
    - Human-Editor=GORE Ñuble
    - ID=GN-MANUAL-PPTO-FORM-EJEC-01
    - Just=Manual orientado a disciplina fiscal y cumplimiento de metas de ejecución
      del Gobierno Regional.
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
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Ctx_Related_Knowledge.Ctx_Optional[0]=knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_2_contabilidad.yml
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Ctx_Related_Knowledge.Ctx_Optional[1]=knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_3_tesoreria_koda.yml
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Ctx_Related_Knowledge.Ctx_Optional[2]=knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_1_compras_koda.yml
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Ctx_Related_Knowledge.Ctx_Optional[3]=knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_2_remuneraciones.yml
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Ctx_Related_Knowledge.ID=GN-MANUAL-PPTO-XREF-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Ctx_Related_Knowledge.XRef[0]=urn:knowledge:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Ctx_Related_Knowledge.XRef[1]=urn:knowledge:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Ctx_Related_Knowledge.XRef[2]=urn:knowledge:gorenuble:gn:gestion-prpto:1.0.0
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.ID=GN-MANUAL-PPTO-ROOT-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Obj[0]=Estandarizar ciclo
      de vida de recursos financieros regionales.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Obj[1]=Asegurar cumplimiento
      Ley de Presupuestos del Sector Público y normativa SAF del Estado.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Distribucion_Inicial.ID=GN-MANUAL-PPTO-S3-F7-01
    - 'Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Distribucion_Inicial.Proc[0]=Promulgada
      la Ley: emitir Decreto de Identificación Presupuestaria.'
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Distribucion_Inicial.Proc[1]=Desagregar
      montos globales en asignaciones específicas e Iniciativas de Inversión (códigos
      BIP).
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Distribucion_Inicial.Ref=DEF-BIP
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.ID=GN-MANUAL-PPTO-S3-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.Excepciones_Sin_Acuerdo_CORE_Glosa_01.Casos[0]=Incorporación
      de Mayores Ingresos Propios percibidos.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.Excepciones_Sin_Acuerdo_CORE_Glosa_01.Casos[1]=Distribución
      de Saldos Iniciales de Caja (SIC) para Deuda Flotante.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.Excepciones_Sin_Acuerdo_CORE_Glosa_01.Casos[2]=Reasignaciones
      por aplicación de leyes de Reajuste.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.Excepciones_Sin_Acuerdo_CORE_Glosa_01.Casos[3]=Cumplimiento
      de sentencias ejecutoriadas.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.Excepciones_Sin_Acuerdo_CORE_Glosa_01.Casos[4]=Desagregación
      de recursos para Transferencias Consolidadas.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.Excepciones_Sin_Acuerdo_CORE_Glosa_01.Casos[5]=Distribución
      de Provisiones de la Partida Tesoro Público.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.Excepciones_Sin_Acuerdo_CORE_Glosa_01.Ctx=Modificaciones
      que el Gobernador puede autorizar vía Resolución sin acuerdo CORE (Glosa 01,
      Circular 11).
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.Excepciones_Sin_Acuerdo_CORE_Glosa_01.ID=GN-MANUAL-PPTO-S3-F9-EXCEP-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.ID=GN-MANUAL-PPTO-S3-F9-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.Niveles[0].Alcance=Reasignaciones
      entre ítems del mismo subtítulo (con restricciones).
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.Niveles[0].Aprobacion=Gobernador.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.Niveles[0].Nivel=1
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.Niveles[0].Nombre=Resolución
      GORE
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.Niveles[1].Alcance=Reasignaciones
      entre subtítulos de misma naturaleza.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.Niveles[1].Nivel=2
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.Niveles[1].Nombre=Resolución
      GORE con Toma de Razón
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.Niveles[2].Alcance[0]=Suplementos
      de fondos.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.Niveles[2].Alcance[1]=Transferencias
      entre programas.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.Niveles[2].Alcance[2]=Creación
      de asignaciones.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.Niveles[2].Nivel=3
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.Niveles[2].Nombre=Decreto
      de Hacienda
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.Niveles[2].Req=Trámite
      en DIPRES.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.Ref=DEF-DIPRES
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.Rol_CORE.ID=GN-MANUAL-PPTO-S3-F9-CORE-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.Rol_CORE.Ref=DEF-CORE
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.Rol_CORE.Req=CORE
      debe aprobar modificaciones que impliquen cambios en distribución de inversión
      o creación de nuevos programas.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Modificaciones_Presupuestarias.Rol_CORE.Src=Ley
      19.175.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Niveles_de_Ejecucion_y_Grados_de_Afectacion.Cadena_Estandar[0].Def=Reserva
      preventiva de recursos al iniciar un proceso de compra o solicitud de gasto
      (interno).
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Niveles_de_Ejecucion_y_Grados_de_Afectacion.Cadena_Estandar[0].Etapa=0.
      Pre-afectación
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Niveles_de_Ejecucion_y_Grados_de_Afectacion.Cadena_Estandar[1].Act=Emisión
      del certificado que bloquea el saldo presupuestario.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Niveles_de_Ejecucion_y_Grados_de_Afectacion.Cadena_Estandar[1].Etapa=1.
      CDP
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Niveles_de_Ejecucion_y_Grados_de_Afectacion.Cadena_Estandar[1].Ref=DEF-CDP
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Niveles_de_Ejecucion_y_Grados_de_Afectacion.Cadena_Estandar[2].Act=Registro
      del acto administrativo (OC, Contrato, Resolución) que formaliza la obligación
      con un tercero.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Niveles_de_Ejecucion_y_Grados_de_Afectacion.Cadena_Estandar[2].Etapa=2.
      Compromiso
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Niveles_de_Ejecucion_y_Grados_de_Afectacion.Cadena_Estandar[2].Ref=DEF-COMPROMISO
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Niveles_de_Ejecucion_y_Grados_de_Afectacion.Cadena_Estandar[3].Act=Reconocimiento
      de la obligación exigible tras recepción conforme o cumplimiento de hito.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Niveles_de_Ejecucion_y_Grados_de_Afectacion.Cadena_Estandar[3].Etapa=3.
      Devengo
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Niveles_de_Ejecucion_y_Grados_de_Afectacion.Cadena_Estandar[3].Ref=DEF-DEVENGO
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Niveles_de_Ejecucion_y_Grados_de_Afectacion.Cadena_Estandar[4].Act=Extinción
      de la obligación mediante transferencia electrónica.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Niveles_de_Ejecucion_y_Grados_de_Afectacion.Cadena_Estandar[4].Etapa=4.
      Pago
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Niveles_de_Ejecucion_y_Grados_de_Afectacion.Cadena_Estandar[4].Ref=DEF-PAGO
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Niveles_de_Ejecucion_y_Grados_de_Afectacion.ID=GN-MANUAL-PPTO-S3-F8-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Niveles_de_Ejecucion_y_Grados_de_Afectacion.Req=Todo
      gasto debe seguir estrictamente la cadena de afectación en SIGFE para asegurar
      trazabilidad y control financiero.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Reglas_Especificas_de_Devengo_para_Transferencias.Casos[0].Caso=Transferencias
      Extrapresupuestarias (Subt. 24.03, 33.03) a Instituciones Ley Ppto
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Reglas_Especificas_de_Devengo_para_Transferencias.Casos[0].Regla=El
      devengo ocurre al aprobarse técnicamente la rendición de cuentas, no al momento
      de la transferencia.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Reglas_Especificas_de_Devengo_para_Transferencias.Casos[1].Caso=Transferencias
      a Municipios y Otros Servicios (Consolidables)
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Reglas_Especificas_de_Devengo_para_Transferencias.Casos[1].Regla=El
      devengo ocurre cuando la obligación es exigible según el acto administrativo
      o convenio tramitado.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Reglas_Especificas_de_Devengo_para_Transferencias.Casos[2].Caso=Transferencias
      a Entidades Privadas (Subt. 24.01, 33.01)
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Reglas_Especificas_de_Devengo_para_Transferencias.Casos[2].Regla=El
      devengo ocurre al cumplirse las condiciones de exigibilidad pactadas en el convenio
      formal.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Reglas_Especificas_de_Devengo_para_Transferencias.ID=GN-MANUAL-PPTO-S3-F8-REGLAS-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Reglas_Especificas_de_Devengo_para_Transferencias.Ref=DEF-SIGFE
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_III_Ejecucion_y_Control_Presupuestario.Reglas_Especificas_de_Devengo_para_Transferencias.Src=Minuta
      CGR-AGORECHI-DIPRES marzo 2025; Dictamen CGR N°E583841/2024.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Discusion_y_Aprobacion.ID=GN-MANUAL-PPTO-S2-F6-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Discusion_y_Aprobacion.Proc[0].Act=DIPIR
      presenta propuesta consolidada a Gobernador y Administrador Regional.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Discusion_y_Aprobacion.Proc[0].Etapa=1.
      Interna
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Discusion_y_Aprobacion.Proc[1].Act=Gobernador
      presenta proyecto al CORE (comisión y aprobación en pleno).
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Discusion_y_Aprobacion.Proc[1].Etapa=2.
      CORE
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Discusion_y_Aprobacion.Proc[2].Etapa=3.
      DIPRES/Congreso
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Discusion_y_Aprobacion.Proc[2].Proc=Discusión
      técnica con analistas DIPRES; trámite legislativo (Septiembre-Noviembre).
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Discusion_y_Aprobacion.Proc[3].Etapa=4.
      Promulgación
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Discusion_y_Aprobacion.Proc[3].Res=Publicación
      Ley de Presupuestos (Diciembre).
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Discusion_y_Aprobacion.Ref[0]=DEF-DIPIR
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Discusion_y_Aprobacion.Ref[1]=DEF-GOBERNADOR-REGIONAL
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Discusion_y_Aprobacion.Ref[2]=DEF-CORE
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Discusion_y_Aprobacion.Ref[3]=DEF-DIPRES
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Fase_Exploratoria_Marco_Presupuestario.Actividad=DIPRES
      comunica 'Marco Exploratorio' (techo global estimado).
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Fase_Exploratoria_Marco_Presupuestario.Analisis_Interno[0].Act=Proyectar
      'Arrastres' (compromisos de años anteriores a pagar en año t+1).
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Fase_Exploratoria_Marco_Presupuestario.Analisis_Interno[0].Resp=DIPIR
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Fase_Exploratoria_Marco_Presupuestario.Analisis_Interno[1].Res=Determinar
      'Espacio Presupuestario' para nuevas iniciativas.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Fase_Exploratoria_Marco_Presupuestario.Analisis_Interno[1].Resp=DIPIR
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Fase_Exploratoria_Marco_Presupuestario.Calendario=Mayo-Junio
      del año anterior.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Fase_Exploratoria_Marco_Presupuestario.ID=GN-MANUAL-PPTO-S2-F4-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Fase_Exploratoria_Marco_Presupuestario.Ref[0]=DEF-DIPRES
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Fase_Exploratoria_Marco_Presupuestario.Ref[1]=DEF-DIPIR
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Formulacion_del_Proyecto_de_Presupuesto.ID=GN-MANUAL-PPTO-S2-F5-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Formulacion_del_Proyecto_de_Presupuesto.Ingreso_SIGFE.Act=Cargar
      formulación en módulo de formulación del sistema central.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Formulacion_del_Proyecto_de_Presupuesto.Ingreso_SIGFE.ID=GN-MANUAL-PPTO-S2-F5-SIGFE-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Formulacion_del_Proyecto_de_Presupuesto.Ingreso_SIGFE.Ref=DEF-SIGFE
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Formulacion_del_Proyecto_de_Presupuesto.Programa_01_Funcionamiento.ID=GN-MANUAL-PPTO-S2-F5-P01-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Formulacion_del_Proyecto_de_Presupuesto.Programa_01_Funcionamiento.Proc[0]=Formular
      en base a dotación efectiva (remuneraciones).
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Formulacion_del_Proyecto_de_Presupuesto.Programa_01_Funcionamiento.Proc[1]=Formular
      en base a contratos de servicios vigentes (luz, agua, seguridad, aseo).
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Formulacion_del_Proyecto_de_Presupuesto.Programa_02_Inversion.ID=GN-MANUAL-PPTO-S2-F5-P02-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Formulacion_del_Proyecto_de_Presupuesto.Programa_02_Inversion.Prioridades[0].Prioridad=1.
      Continuidad (Arrastre).
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Formulacion_del_Proyecto_de_Presupuesto.Programa_02_Inversion.Prioridades[0].Req=Asegurar
      financiamiento de obras en ejecución.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Formulacion_del_Proyecto_de_Presupuesto.Programa_02_Inversion.Prioridades[1].Prioridad=2.
      Nuevas Iniciativas.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Formulacion_del_Proyecto_de_Presupuesto.Programa_02_Inversion.Prioridades[1].Req[0]=Seleccionar
      proyectos con recomendación técnica favorable (RS).
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.Formulacion_del_Proyecto_de_Presupuesto.Programa_02_Inversion.Prioridades[1].Req[1]=Alinear
      con Estrategia Regional de Desarrollo (ERD).
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_II_Ciclo_de_Formulacion_Presupuestaria.ID=GN-MANUAL-PPTO-S2-01
    - 'Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Gestion_de_Convenios_de_Transferencia.Ctx[0]=Unidades
      técnicas posibles: MOP, SERVIU, Municipalidad.'
    - 'Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Gestion_de_Convenios_de_Transferencia.Ctx[1]=Estados
      de Pago: transferencia contra avance.'
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Gestion_de_Convenios_de_Transferencia.Def=Mecanismo
      principal para ejecutar proyectos donde GORE no es unidad técnica.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Gestion_de_Convenios_de_Transferencia.ID=GN-MANUAL-PPTO-S4-F11-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Gestion_de_Convenios_de_Transferencia.Tipos[0].Def=GORE
      encarga ejecución a tercero (MOP, SERVIU, Municipalidad); transfiere recursos
      contra avance (Estados de Pago).
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Gestion_de_Convenios_de_Transferencia.Tipos[0].Tipo=Convenio
      Mandato
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Gestion_de_Convenios_de_Transferencia.Tipos[1].Def=Entrega
      recursos para ejecución directa del beneficiario (subvenciones, fondos concursables).
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Gestion_de_Convenios_de_Transferencia.Tipos[1].Req=Rendición
      estricta (SISREC/Contraloría).
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Gestion_de_Convenios_de_Transferencia.Tipos[1].Tipo=Convenio
      de Transferencia
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.ID=GN-MANUAL-PPTO-S4-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Identificacion_de_Iniciativas_IDI.Apertura_IDI.Act=Crear
      'ficha IDI' en sistema presupuestario; cargar presupuesto anual y total.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Identificacion_de_Iniciativas_IDI.Apertura_IDI.ID=GN-MANUAL-PPTO-S4-F10-APERTURA-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Identificacion_de_Iniciativas_IDI.Apertura_IDI.Ref[0]=DEF-DIPIR
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Identificacion_de_Iniciativas_IDI.Apertura_IDI.Ref[1]=DEF-IDI
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Identificacion_de_Iniciativas_IDI.Apertura_IDI.Resp=DIPIR
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Identificacion_de_Iniciativas_IDI.Control_por_Codigo.ID=GN-MANUAL-PPTO-S4-F10-CONTROL-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Identificacion_de_Iniciativas_IDI.Control_por_Codigo.Ref=DEF-IDI
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Identificacion_de_Iniciativas_IDI.Control_por_Codigo.Req=Ejecución
      se controla a nivel de IDI; no usar fondos de proyecto A para pagar proyecto
      B.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Identificacion_de_Iniciativas_IDI.ID=GN-MANUAL-PPTO-S4-F10-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Identificacion_de_Iniciativas_IDI.Req=Cada
      proyecto de inversión debe tener código BIP.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Programacion_Financiera.Coordinacion=DIPIR-Tesorería.
    - 'Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Programacion_Financiera.Ctx_Optional=Para
      detalle operativo PAC y gestión de caja: Manual 1.3: Tesorería y Gestión de
      Ingresos (./manual_1_3_tesoreria.md).'
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Programacion_Financiera.Devengamiento_Oportuno.ID=GN-MANUAL-PPTO-S4-F13-DEVOP-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Programacion_Financiera.Devengamiento_Oportuno.Req[0]=Evitar
      devengamiento masivo en diciembre.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Programacion_Financiera.Devengamiento_Oportuno.Req[1]=Procesar
      estados de pago mensualmente para reflejar ejecución real.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Programacion_Financiera.ID=GN-MANUAL-PPTO-S4-F13-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Programacion_Financiera.PAC_de_Inversiones.Def=PAC
      vinculada a avance físico de obras.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Programacion_Financiera.PAC_de_Inversiones.ID=GN-MANUAL-PPTO-S4-F13-PACINV-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Programacion_Financiera.PAC_de_Inversiones.Ref=DEF-PAC
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Programas_Directos_Glosa_06.Def=Oferta
      programática ejecutada directamente por el GORE.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Programas_Directos_Glosa_06.Evaluacion_Ex_Ante.ID=GN-MANUAL-PPTO-S4-F12-EXANTE-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Programas_Directos_Glosa_06.Evaluacion_Ex_Ante.Ref=DEF-DIPRES
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Programas_Directos_Glosa_06.Evaluacion_Ex_Ante.Req=Programas
      nuevos o sustancialmente reformulados requieren evaluación favorable DIPRES/MDSF
      antes de financiamiento.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Programas_Directos_Glosa_06.Exencion.ID=GN-MANUAL-PPTO-S4-F12-EXENCION-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Programas_Directos_Glosa_06.Exencion.Ref[0]=DEF-FNDR
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Programas_Directos_Glosa_06.Exencion.Ref[1]=DEF-FRPD
    - 'Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Programas_Directos_Glosa_06.Exencion.Req=Exentos
      de evaluación ex-ante: programas 8% FNDR (Glosa 07) y tipologías FRPD de Innovación.'
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Programas_Directos_Glosa_06.Gasto_Administrativo.ID=GN-MANUAL-PPTO-S4-F12-GA-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Programas_Directos_Glosa_06.Gasto_Administrativo.Req=Hasta
      5% del monto del programa para gastos de administración del GORE (Subtítulos
      21, 22, 29).
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Programas_Directos_Glosa_06.ID=GN-MANUAL-PPTO-S4-F12-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Programas_Directos_Glosa_06.Metodologia_Marco_Logico.ID=GN-MANUAL-PPTO-S4-F12-ML-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Programas_Directos_Glosa_06.Metodologia_Marco_Logico.Req=Diseñar
      programas con objetivos, componentes, actividades e indicadores verificables.
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Ref=DEF-FNDR
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Restricciones_Glosas_2025.ID=GN-MANUAL-PPTO-S4-GLOSAS-01
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Restricciones_Glosas_2025.Normas[0].Glosa=03
      (Gastos en Personal)
    - Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria.Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR.Restricciones_Glosas_2025.Normas[0].Prohib=No
      se puede imputar a inversión (Subtítulo 31) gastos en personal (Subtítulo 21),
      salvo contratación de inspección técnica de obras.
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
---

# Manual 1.1: Formulación y Ejecución Presupuestaria
## ID
GN-MANUAL-PPTO-FORM-EJEC-01

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
Estandarizar ciclo de vida de recursos financieros regionales: planificación -> formulación -> aprobación -> ejecución -> control -> cierre; cumplimiento Ley de Presupuestos y SAF del Estado.

## Primary Source
staging/brow_speculativo/manual_1_1_presupuesto.md

## Authoritative Source
### Path
staging/temp/brutos ordenados/02_finanzas_control/OF CIRCULAR 11 (038FF)_30.01_INSTRUCCIONES APLICACIÓN GLOSAS GORES.koda.yml
### Priority
1
### Type
Official-Circular-DIPRES
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

LANGUAGE POLICY: Keywords in English, content in original language. Never translate content.
END_LLM_INSTRUCTIONS


## Definitions
### Organos y Unidades
| ID | Def |
| --- | --- |
| DEF-DIPRES | DIPRES (Dirección de Presupuestos): Ente rector que define instrucciones, techos y autoriza modificaciones mayores. |
| DEF-GOBERNADOR-REGIONAL | Gobernador Regional: Responsable de proponer el presupuesto al CORE y ejecutarlo. |
| DEF-CORE | Consejo Regional (CORE): Aprueba presupuesto inicial y modificaciones mayores; fiscaliza la ejecución. |
| DEF-DIPIR | División de Presupuesto e Inversión Regional (DIPIR): Unidad técnica responsable de gestión diaria del presupuesto, control de saldos y visación de gastos. |
### Sistemas y Codigos
| ID | Def |
| --- | --- |
| DEF-SIGFE | SIGFE: Sistema central (módulo formulación y registro ejecución) para gestión financiera del Estado. |
| DEF-BIP | BIP: Banco Integrado de Proyectos; código requerido para proyectos de inversión. |
| DEF-IDI | IDI: Iniciativa (proyecto) de inversión; se controla por código (BIP) y no se mezclan fondos entre proyectos. |
### Instrumentos y Fondos
| ID | Def |
| --- | --- |
| DEF-FNDR | FNDR: Principal fuente de recursos para inversiones; se subdivide en asignaciones regionales (decisión GORE) y provisiones (decisión central/mixta). |
| DEF-FRPD | FRPD: Recursos destinados a fomento productivo, ciencia e innovación. |
| DEF-PAC | PAC (Programación Anual de Caja): Proyecta flujo de ingresos y egresos para asegurar liquidez para cumplir obligaciones. |
### Cadena Presupuestaria
| ID | Def |
| --- | --- |
| DEF-CDP | CDP (Certificado de Disponibilidad Presupuestaria): Documento previo obligatorio que certifica saldo; ningún proceso de compra o convenio inicia sin CDP. |
| DEF-COMPROMISO | Compromiso: Acto administrativo (OC/Contrato/Resolución Convenio) que afecta el presupuesto; reserva recursos definitivamente para un tercero. |
| DEF-DEVENGO | Devengo: Hito de recepción conforme; genera obligación de pago y pasivo contable; debe ser simultáneo a recepción de factura/bien. |
| DEF-PAGO | Pago: Egreso efectivo de fondos que extingue la obligación. |
### Cierre
| ID | Def |
| --- | --- |
| DEF-SIC | SIC: Saldo Inicial de Caja. |
| DEF-DEUDA-FLOTANTE | Deuda Flotante: Obligaciones devengadas al 31/12 pendientes de pago. |
| DEF-ITEM-DEUDA-FLOTANTE | Ítem 34.07 'Deuda Flotante': se crea en presupuesto del año siguiente para registrar financiamiento. |

## Manual 1 1 Formulacion y Ejecucion Presupuestaria
### ID
GN-MANUAL-PPTO-ROOT-01
### Obj
- Estandarizar ciclo de vida de recursos financieros regionales.
- Asegurar cumplimiento Ley de Presupuestos del Sector Público y normativa SAF del Estado.
### Seccion I Marco Conceptual y Estructura
#### ID
GN-MANUAL-PPTO-S1-01
#### Clasificador Presupuestario
#### ID
GN-MANUAL-PPTO-S1-CLASIF-01
#### Src
Decreto N° 854 (2004) de Hacienda.
#### Ctx
Estructura presupuestaria GORE Ñuble.
#### Estructura
#### Partida
| Partida | Def |
| --- | --- |
| 31 | Identifica a los Gobiernos Regionales. |
#### Capitulos
| Capitulo | Def |
| --- | --- |
| 01 Gobierno Regional | Ejecución administrativa y operativa. |
| 02 Consejo Regional | Gastos funcionamiento CORE (dietas, viáticos, asesorías). |
#### Programas
| Programa | Def |
| --- | --- |
| 01 Funcionamiento | Gastos administrativos (Personal; Bienes y Servicios). |
| 02 Inversión Regional | Ejecución FNDR y otros fondos de capital. |
#### Subtitulos Relevantes
- 21 Gastos en Personal.
- 22 Bienes y Servicios de Consumo.
- 24 Transferencias Corrientes.
- 29 Adquisición de Activos No Financieros.
- 31 Iniciativas de Inversión.
- 33 Transferencias de Capital.
#### Fuentes de Financiamiento
#### ID
GN-MANUAL-PPTO-S1-FUENTES-01
#### Fuentes
-
  #### Ref
  DEF-FNDR
-
  #### Ref
  DEF-FRPD
-
  #### Fuente
  Ingresos Propios
  #### Def
  Recursos generados por venta de bienes, multas o servicios.
-
  #### Ref
  DEF-PAC
#### Roles Presupuestarios
#### ID
GN-MANUAL-PPTO-S1-ROLES-01
#### Roles
| Ref |
| --- |
| DEF-DIPRES |
| DEF-GOBERNADOR-REGIONAL |
| DEF-CORE |
| DEF-DIPIR |
### Seccion II Ciclo de Formulacion Presupuestaria
#### ID
GN-MANUAL-PPTO-S2-01
#### Fase Exploratoria Marco Presupuestario
#### ID
GN-MANUAL-PPTO-S2-F4-01
#### Calendario
Mayo-Junio del año anterior.
#### Actividad
DIPRES comunica 'Marco Exploratorio' (techo global estimado).
#### Analisis Interno
-
  #### Resp
  DIPIR
  #### Act
  Proyectar 'Arrastres' (compromisos de años anteriores a pagar en año t+1).
-
  #### Resp
  DIPIR
  #### Res
  Determinar 'Espacio Presupuestario' para nuevas iniciativas.
#### Ref
- DEF-DIPRES
- DEF-DIPIR
#### Formulacion del Proyecto de Presupuesto
#### ID
GN-MANUAL-PPTO-S2-F5-01
#### Programa 01 Funcionamiento
#### ID
GN-MANUAL-PPTO-S2-F5-P01-01
#### Proc
- Formular en base a dotación efectiva (remuneraciones).
- Formular en base a contratos de servicios vigentes (luz, agua, seguridad, aseo).
#### Programa 02 Inversion
#### ID
GN-MANUAL-PPTO-S2-F5-P02-01
#### Prioridades
| Prioridad | Req |
| --- | --- |
| 1. Continuidad (Arrastre). | Asegurar financiamiento de obras en ejecución. |
| 2. Nuevas Iniciativas. | ['Seleccionar proyectos con recomendación técnica favorable (RS).', 'Alinear con Estrategia Regional de Desarrollo (ERD).'] |
#### Ingreso SIGFE
#### ID
GN-MANUAL-PPTO-S2-F5-SIGFE-01
#### Act
Cargar formulación en módulo de formulación del sistema central.
#### Ref
DEF-SIGFE
#### Discusion y Aprobacion
#### ID
GN-MANUAL-PPTO-S2-F6-01
#### Proc
-
  #### Etapa
  1. Interna
  #### Act
  DIPIR presenta propuesta consolidada a Gobernador y Administrador Regional.
-
  #### Etapa
  2. CORE
  #### Act
  Gobernador presenta proyecto al CORE (comisión y aprobación en pleno).
-
  #### Etapa
  3. DIPRES/Congreso
  #### Proc
  Discusión técnica con analistas DIPRES; trámite legislativo (Septiembre-Noviembre).
-
  #### Etapa
  4. Promulgación
  #### Res
  Publicación Ley de Presupuestos (Diciembre).
#### Ref
- DEF-DIPIR
- DEF-GOBERNADOR-REGIONAL
- DEF-CORE
- DEF-DIPRES
### Seccion III Ejecucion y Control Presupuestario
#### ID
GN-MANUAL-PPTO-S3-01
#### Distribucion Inicial
#### ID
GN-MANUAL-PPTO-S3-F7-01
#### Proc
- Promulgada la Ley: emitir Decreto de Identificación Presupuestaria.
- Desagregar montos globales en asignaciones específicas e Iniciativas de Inversión (códigos BIP).
#### Ref
DEF-BIP
#### Niveles de Ejecucion y Grados de Afectacion
#### ID
GN-MANUAL-PPTO-S3-F8-01
#### Req
Todo gasto debe seguir estrictamente la cadena de afectación en SIGFE para asegurar trazabilidad y control financiero.
#### Cadena Estandar
-
  #### Etapa
  0. Pre-afectación
  #### Def
  Reserva preventiva de recursos al iniciar un proceso de compra o solicitud de gasto (interno).
-
  #### Etapa
  1. CDP
  #### Ref
  DEF-CDP
  #### Act
  Emisión del certificado que bloquea el saldo presupuestario.
-
  #### Etapa
  2. Compromiso
  #### Ref
  DEF-COMPROMISO
  #### Act
  Registro del acto administrativo (OC, Contrato, Resolución) que formaliza la obligación con un tercero.
-
  #### Etapa
  3. Devengo
  #### Ref
  DEF-DEVENGO
  #### Act
  Reconocimiento de la obligación exigible tras recepción conforme o cumplimiento de hito.
-
  #### Etapa
  4. Pago
  #### Ref
  DEF-PAGO
  #### Act
  Extinción de la obligación mediante transferencia electrónica.
#### Reglas Especificas de Devengo para Transferencias
#### ID
GN-MANUAL-PPTO-S3-F8-REGLAS-01
#### Src
Minuta CGR-AGORECHI-DIPRES marzo 2025; Dictamen CGR N°E583841/2024.
#### Casos
| Caso | Regla |
| --- | --- |
| Transferencias Extrapresupuestarias (Subt. 24.03, 33.03) a Instituciones Ley Ppto | El devengo ocurre al aprobarse técnicamente la rendición de cuentas, no al momento de la transferencia. |
| Transferencias a Municipios y Otros Servicios (Consolidables) | El devengo ocurre cuando la obligación es exigible según el acto administrativo o convenio tramitado. |
| Transferencias a Entidades Privadas (Subt. 24.01, 33.01) | El devengo ocurre al cumplirse las condiciones de exigibilidad pactadas en el convenio formal. |
#### Ref
DEF-SIGFE
#### Modificaciones Presupuestarias
#### ID
GN-MANUAL-PPTO-S3-F9-01
#### Niveles
-
  #### Nivel
  1
  #### Nombre
  Resolución GORE
  #### Alcance
  Reasignaciones entre ítems del mismo subtítulo (con restricciones).
  #### Aprobacion
  Gobernador.
-
  #### Nivel
  2
  #### Nombre
  Resolución GORE con Toma de Razón
  #### Alcance
  Reasignaciones entre subtítulos de misma naturaleza.
-
  #### Nivel
  3
  #### Nombre
  Decreto de Hacienda
  #### Alcance
  - Suplementos de fondos.
  - Transferencias entre programas.
  - Creación de asignaciones.
  #### Req
  Trámite en DIPRES.
#### Excepciones Sin Acuerdo CORE Glosa 01
#### ID
GN-MANUAL-PPTO-S3-F9-EXCEP-01
#### Ctx
Modificaciones que el Gobernador puede autorizar vía Resolución sin acuerdo CORE (Glosa 01, Circular 11).
#### Casos
- Incorporación de Mayores Ingresos Propios percibidos.
- Distribución de Saldos Iniciales de Caja (SIC) para Deuda Flotante.
- Reasignaciones por aplicación de leyes de Reajuste.
- Cumplimiento de sentencias ejecutoriadas.
- Desagregación de recursos para Transferencias Consolidadas.
- Distribución de Provisiones de la Partida Tesoro Público.
#### Rol CORE
#### ID
GN-MANUAL-PPTO-S3-F9-CORE-01
#### Src
Ley 19.175.
#### Req
CORE debe aprobar modificaciones que impliquen cambios en distribución de inversión o creación de nuevos programas.
#### Ref
DEF-CORE
#### Ref
DEF-DIPRES
### Seccion IV Gestion de la Inversion Regional FNDR
#### ID
GN-MANUAL-PPTO-S4-01
#### Ref
DEF-FNDR
#### Identificacion de Iniciativas IDI
#### ID
GN-MANUAL-PPTO-S4-F10-01
#### Req
Cada proyecto de inversión debe tener código BIP.
#### Apertura IDI
#### ID
GN-MANUAL-PPTO-S4-F10-APERTURA-01
#### Resp
DIPIR
#### Act
Crear 'ficha IDI' en sistema presupuestario; cargar presupuesto anual y total.
#### Ref
- DEF-DIPIR
- DEF-IDI
#### Control por Codigo
#### ID
GN-MANUAL-PPTO-S4-F10-CONTROL-01
#### Req
Ejecución se controla a nivel de IDI; no usar fondos de proyecto A para pagar proyecto B.
#### Ref
DEF-IDI
#### Gestion de Convenios de Transferencia
#### ID
GN-MANUAL-PPTO-S4-F11-01
#### Def
Mecanismo principal para ejecutar proyectos donde GORE no es unidad técnica.
#### Tipos
-
  #### Tipo
  Convenio Mandato
  #### Def
  GORE encarga ejecución a tercero (MOP, SERVIU, Municipalidad); transfiere recursos contra avance (Estados de Pago).
-
  #### Tipo
  Convenio de Transferencia
  #### Def
  Entrega recursos para ejecución directa del beneficiario (subvenciones, fondos concursables).
  #### Req
  Rendición estricta (SISREC/Contraloría).
#### Ctx
- Unidades técnicas posibles: MOP, SERVIU, Municipalidad.
- Estados de Pago: transferencia contra avance.
#### Programas Directos Glosa 06
#### ID
GN-MANUAL-PPTO-S4-F12-01
#### Def
Oferta programática ejecutada directamente por el GORE.
#### Evaluacion Ex Ante
#### ID
GN-MANUAL-PPTO-S4-F12-EXANTE-01
#### Req
Programas nuevos o sustancialmente reformulados requieren evaluación favorable DIPRES/MDSF antes de financiamiento.
#### Ref
DEF-DIPRES
#### Metodologia Marco Logico
#### ID
GN-MANUAL-PPTO-S4-F12-ML-01
#### Req
Diseñar programas con objetivos, componentes, actividades e indicadores verificables.
#### Gasto Administrativo
#### ID
GN-MANUAL-PPTO-S4-F12-GA-01
#### Req
Hasta 5% del monto del programa para gastos de administración del GORE (Subtítulos 21, 22, 29).
#### Exencion
#### ID
GN-MANUAL-PPTO-S4-F12-EXENCION-01
#### Req
Exentos de evaluación ex-ante: programas 8% FNDR (Glosa 07) y tipologías FRPD de Innovación.
#### Ref
- DEF-FNDR
- DEF-FRPD
#### Restricciones Glosas 2025
#### ID
GN-MANUAL-PPTO-S4-GLOSAS-01
#### Src
Circular 11 DIPRES - Instrucciones Glosas GORES.
#### Normas
-
  #### Glosa
  03 (Gastos en Personal)
  #### Prohib
  No se puede imputar a inversión (Subtítulo 31) gastos en personal (Subtítulo 21), salvo contratación de inspección técnica de obras.
-
  #### Glosa
  06 (Programas GORE)
  #### Req
  Ejecución directa requiere unidad técnica interna competente y resolución fundada.
-
  #### Glosa
  07 (Subvenciones 8%)
  #### Req
  Máximo 8% del presupuesto inversional. Asignación directa solo a entidades públicas o privadas sin fines de lucro, con justificación fundada.
-
  #### Glosa
  12 (FRIL)
  #### Req
  Proyectos menores a 5.000 UTM exentos de evaluación MDSyF (solo requieren elegibilidad técnica regional).
#### Programacion Financiera
#### ID
GN-MANUAL-PPTO-S4-F13-01
#### Coordinacion
DIPIR-Tesorería.
#### PAC de Inversiones
#### ID
GN-MANUAL-PPTO-S4-F13-PACINV-01
#### Def
PAC vinculada a avance físico de obras.
#### Ref
DEF-PAC
#### Devengamiento Oportuno
#### ID
GN-MANUAL-PPTO-S4-F13-DEVOP-01
#### Req
- Evitar devengamiento masivo en diciembre.
- Procesar estados de pago mensualmente para reflejar ejecución real.
#### Ctx Optional
Para detalle operativo PAC y gestión de caja: Manual 1.3: Tesorería y Gestión de Ingresos (./manual_1_3_tesoreria.md).
### Seccion V Informes y Evaluacion
#### ID
GN-MANUAL-PPTO-S5-01
#### Reporteria Oficial
#### ID
GN-MANUAL-PPTO-S5-F14-01
#### Informe de Ejecucion Mensual
#### ID
GN-MANUAL-PPTO-S5-F14-MENSUAL-01
#### Proc
- Enviar a DIPRES y CORE dentro de primeros días del mes siguiente.
- Mostrar presupuesto vigente vs devengado.
#### Ref
- DEF-DIPRES
- DEF-CORE
#### Informes Trimestrales Glosas
#### ID
GN-MANUAL-PPTO-S5-F14-TRIM-01
#### Def
Reportes exigidos por Ley de Presupuestos (ej.: gastos en publicidad, viáticos, convenios directos).
#### Proc
- Enviar al Congreso.
- Publicar en transparencia activa.
#### Cierre Presupuestario
#### ID
GN-MANUAL-PPTO-S5-F15-01
#### Regla 31 Diciembre
#### ID
GN-MANUAL-PPTO-S5-F15-REG31-01
#### Req
- Presupuesto expira al 31/12.
- Saldos no comprometidos no se acumulan para el año siguiente (salvo norma expresa de saldo inicial de caja).
#### Deuda Flotante
#### ID
GN-MANUAL-PPTO-S5-F15-DF-01
#### Ref
DEF-DEUDA-FLOTANTE
#### Financiamiento
| Cond | Res |
| --- | --- |
| SIC suficiente | Financiar íntegramente con SIC (solo Resolución GORE). |
| SIC insuficiente | Usar todo SIC disponible + diferencia con mayor aporte fiscal (Resolución GORE + Decreto DIPRES). |
#### Prioridad
#### ID
GN-MANUAL-PPTO-S5-F15-DF-PRIOR-01
#### Req
Pago Deuda Flotante es primera prioridad al inicio del nuevo ejercicio.
#### Registro
#### ID
GN-MANUAL-PPTO-S5-F15-DF-REG-01
#### Act
Crear Ítem 34.07 'Deuda Flotante' en presupuesto del año siguiente.
#### Ref
DEF-ITEM-DEUDA-FLOTANTE
#### Ref
DEF-SIC
### Ctx Related Knowledge
#### ID
GN-MANUAL-PPTO-XREF-01
#### XRef
- urn:knowledge:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0
- urn:knowledge:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0
- urn:knowledge:gorenuble:gn:gestion-prpto:1.0.0
#### Ctx Optional
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_2_contabilidad.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_3_tesoreria_koda.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_1_compras_koda.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_2_remuneraciones.yml

## Just
Manual orientado a disciplina fiscal y cumplimiento de metas de ejecución del Gobierno Regional.
