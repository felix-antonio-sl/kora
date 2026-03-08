---
_manifest:
  urn: urn:gn:kb:gestion-prpto-2026
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/presupuesto/kb_gn_018_gestion_prpto_2026_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- presupuesto-regional
- gestion-financiera
- ley-21796
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/presupuesto/kb_gn_018_gestion_prpto_2026_koda.yml
    source_hashes:
      domains/gn/03_operacion/presupuesto/kb_gn_018_gestion_prpto_2026_koda.yml: db858d287b9d9f249d02768786b20014521ff83e5d678bf3e6f3ff4f25932ba2
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.1
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 26
    meat_count: 902
    fat_count: 0
    preserved_facts:
    - AI-Remediator=KODA-TRANSFORMER
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Contenido_y_Requisitos.ID=GORE-FIN-APROB-CONTENIDO-01
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Contenido_y_Requisitos.Req_Acuerdo_CORE[0]=Voluntad
      del CORE debe ser clara en conceptos y montos y certificada por Secretario Ejecutivo.
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Contenido_y_Requisitos.Req_Generales[0]=Desagregación
      según clasificador presupuestario a nivel de Subtítulo e Ítem.
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Contenido_y_Requisitos.Req_Generales[1]=Transferencias
      desagregadas a nivel de Asignación (Subt. 24 y 33).
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Contenido_y_Requisitos.Req_Generales[2]=Clasificaciones
      coherentes con naturaleza del gasto y receptor (legalidad del gasto).
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Contenido_y_Requisitos.Req_Generales[3]=Equilibrio
      entre ingresos y gastos; montos coinciden con Ley de Presupuestos.
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Contenido_y_Requisitos.Req_Generales[4]=Coherencia
      entre propuesta Gobernador, acuerdo CORE y resoluciones DIPRES.
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Contenido_y_Requisitos.Req_Presupuesto_Funcionamiento[0]=Incluir
      glosas obligatorias (dotación, vehículos, viáticos, gasto CORE en el extranjero).
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Contenido_y_Requisitos.Req_Presupuesto_Funcionamiento[1]=Monto
      del Subtítulo 21 debe coincidir con lo autorizado en glosa específica.
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Contenido_y_Requisitos.Req_Presupuesto_Inversion[0]=Incluir
      arrastres de años anteriores conservando número de asignación y código BIP.
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Contenido_y_Requisitos.Req_Presupuesto_Inversion[1]=Incorporar
      nuevas iniciativas cumpliendo requisitos de glosas.
    - 'Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Contenido_y_Requisitos.Req_Presupuesto_Inversion[2]=Para
      nuevas transferencias a privados: acreditar selección por concurso o causal
      de excepción y personalidad jurídica vigente.'
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Contenido_y_Requisitos.Req_Presupuesto_Inversion[3]=Crear
      asignación para FRPD en ítem 33.03 y otras provisiones (FRIL, 8% FNDR).
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Contenido_y_Requisitos.Src=Instructivo
      CGR Aprobación Presupuesto Inicial (vigente).
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Procedimiento_Legal.Asunto=Procedimiento
      legal para aprobación de presupuesto inicial del GORE.
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Procedimiento_Legal.ID=GORE-FIN-APROB-PROCEDIMIENTO-01
    - 'Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Procedimiento_Legal.Proc_Fases_y_Plazos[0]=Propuesta
      del Gobernador: presenta distribución inicial al CORE (10 días desde publicación
      de la Ley).'
    - 'Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Procedimiento_Legal.Proc_Fases_y_Plazos[1]=Aprobación
      CORE: se pronuncia en 10 días desde recepción.'
    - 'Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Procedimiento_Legal.Proc_Fases_y_Plazos[2]=Envío
      a DIPRES: Gobernador remite acuerdo aprobado en 5 días.'
    - 'Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Procedimiento_Legal.Proc_Fases_y_Plazos[3]=Resoluciones
      DIPRES: elabora resoluciones de presupuesto de funcionamiento e inversión (10
      días).'
    - 'Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Procedimiento_Legal.Proc_Fases_y_Plazos[4]=Toma
      de Razón CGR: 15 días desde recepción (prorrogable por 15).'
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Procedimiento_Legal.Src=Glosa
      01 Partida 31 Ley 21.796; Instructivo CGR Aprobación Presupuesto Inicial (vigente).
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Rol_CORE_en_Aprobacion.Act=Propuesta
      de distribución se somete al CORE para aprobación, modificación o sustitución
      (Art. 25 LOC GORE).
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Rol_CORE_en_Aprobacion.Dln=10
      días corridos para pronunciarse.
    - 'Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Rol_CORE_en_Aprobacion.Fnd=Dictamen
      E548580/2024 CGR: decisiones informadas, razonadas y alineadas con intereses
      regionales.'
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Rol_CORE_en_Aprobacion.ID=GORE-FIN-APROB-ROL-CORE-01
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Rol_CORE_en_Aprobacion.Proc_Exposicion[0]=DIPIR
      expone presupuesto de inversiones.
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Rol_CORE_en_Aprobacion.Proc_Exposicion[1]=DAF
      expone presupuesto de funcionamiento.
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Rol_CORE_en_Aprobacion.Proc_Exposicion[2]=Ambas
      divisiones responden consultas y ajustan propuesta si corresponde.
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Tramite_DIPRES_y_CGR.Act=Gobernador
      remite distribución aprobada a DIPRES.
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Tramite_DIPRES_y_CGR.Act_DIPRES[0]=Revisar
      y elaborar resoluciones de presupuesto inicial (10 días).
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Tramite_DIPRES_y_CGR.Act_DIPRES[1]=Subsanar
      errores materiales y reclasificar ingresos y gastos informando a GORE y CGR.
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Tramite_DIPRES_y_CGR.Dln=5
      días desde aprobación CORE.
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Tramite_DIPRES_y_CGR.ID=GORE-FIN-APROB-TRAM-DIPRES-01
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Tramite_DIPRES_y_CGR.ID_Resolucion_CGR.Act=DIPRES
      remite resoluciones a CGR para Toma de Razón.
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Tramite_DIPRES_y_CGR.ID_Resolucion_CGR.Ctx[0]=CGR
      verifica clasificación presupuestaria, cumplimiento de glosas, conformidad normativa
      y coincidencia GORE-CORE-DIPRES.
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Tramite_DIPRES_y_CGR.ID_Resolucion_CGR.Ctx[1]=Toma
      de Razón deja acto vigente; Representa rechaza por ilegalidad o formula alcances.
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Tramite_DIPRES_y_CGR.ID_Resolucion_CGR.Dln=15
      días (prorrogable por 15).
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Tramite_DIPRES_y_CGR.ID_Resolucion_CGR.ID=GORE-FIN-APROB-TRAM-CGR-01
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Tramite_DIPRES_y_CGR.ID_Resolucion_CGR.Nat=Control
      previo obligatorio de legalidad.
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Tramite_DIPRES_y_CGR.ID_Resolucion_CGR.Res=DAF
      carga presupuesto en SIGFE (GORE-FIN-HERRAM-SIGFE-01).
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Tramite_DIPRES_y_CGR.Req_Documentos[0]=Oficio
      firmado por Gobernador titular o subrogante con acto de delegación.
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Tramite_DIPRES_y_CGR.Req_Documentos[1]=Contacto
      formal.
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Tramite_DIPRES_y_CGR.Req_Documentos[2]=Acuerdo
      CORE certificado.
    - Ciclo_Presupuestario.Aprobacion_y_Distribucion_Inicial.Tramite_DIPRES_y_CGR.Resp=DAF
      prepara oficio conductor y antecedentes.
    - Ciclo_Presupuestario.Cierre_Presupuestario.Compromisos_y_Cortes.Act=Definir
      fechas de corte para nuevos compromisos (usualmente diciembre) y comunicarlas.
    - Ciclo_Presupuestario.Cierre_Presupuestario.Compromisos_y_Cortes.ID=GORE-FIN-CIERRE-COMPROMISOS-01
    - Ciclo_Presupuestario.Cierre_Presupuestario.Compromisos_y_Cortes.Resp[0]=DAF
      comunica fechas límite.
    - Ciclo_Presupuestario.Cierre_Presupuestario.Compromisos_y_Cortes.Resp[1]=DIPIR
      verifica registro adecuado de compromisos.
    - Ciclo_Presupuestario.Cierre_Presupuestario.Deuda_Flotante.Cpt[0]=Si el Saldo
      Inicial de Caja (SIC) supera la deuda flotante, se financia 100% con SIC (solo
      Resolución GORE).
    - Ciclo_Presupuestario.Cierre_Presupuestario.Deuda_Flotante.Cpt[1]=Si SIC es insuficiente,
      se usa todo el SIC y la diferencia con mayor aporte fiscal (Resolución GORE
      + Decreto DIPRES).
    - Ciclo_Presupuestario.Cierre_Presupuestario.Deuda_Flotante.Def=Obligaciones devengadas
      en el año pero pendientes de pago al 31 de diciembre.
    - Ciclo_Presupuestario.Cierre_Presupuestario.Deuda_Flotante.Fnd=Art. 34 Ley 21.796
      permite exceder las sumas fijadas para este ítem.
    - Ciclo_Presupuestario.Cierre_Presupuestario.Deuda_Flotante.ID=GORE-FIN-CIERRE-DEUDA-FLOTANTE-01
    - Ciclo_Presupuestario.Cierre_Presupuestario.Deuda_Flotante.Resp=DAF calcula,
      registra y tramita su incorporación en el presupuesto del año siguiente mediante
      creación del ítem 34.07 Deuda Flotante.
    - Ciclo_Presupuestario.Cierre_Presupuestario.Deuda_Flotante.Warn=Priorizar pago
      de deuda flotante al inicio del nuevo ejercicio.
    - Ciclo_Presupuestario.Cierre_Presupuestario.Evaluacion_y_Cierre_Sistemas.Act[0]=DAF
      realiza ajustes contables, prepara Informe de Ejecución Anual y genera nuevo
      SIC.
    - Ciclo_Presupuestario.Cierre_Presupuestario.Evaluacion_y_Cierre_Sistemas.Act[1]=DIPIR
      evalúa ejecución física de proyectos, identifica logros, retrasos y cuellos
      de botella, retroalimentando la siguiente formulación.
    - Ciclo_Presupuestario.Cierre_Presupuestario.Evaluacion_y_Cierre_Sistemas.ID=GORE-FIN-CIERRE-EVALUACION-01
    - Ciclo_Presupuestario.Cierre_Presupuestario.Evaluacion_y_Cierre_Sistemas.ID_Cierre_Sistemas.Act=DAF
      realiza cierre en SIGFE y DIPIR actualiza estado final en BIP.
    - Ciclo_Presupuestario.Cierre_Presupuestario.Evaluacion_y_Cierre_Sistemas.ID_Cierre_Sistemas.ID=GORE-FIN-CIERRE-SISTEMAS-01
    - Ciclo_Presupuestario.Control_y_Seguimiento.Control_CGR.Cpt[0]=Control previo
      vía Toma de Razón de resoluciones y decretos presupuestarios.
    - Ciclo_Presupuestario.Control_y_Seguimiento.Control_CGR.Cpt[1]=Control posterior
      mediante auditorías e investigaciones especiales.
    - Ciclo_Presupuestario.Control_y_Seguimiento.Control_CGR.ID=GORE-FIN-CONTROL-LEGALIDAD-CGR-01
    - Ciclo_Presupuestario.Control_y_Seguimiento.Control_CGR.Req=DIPIR y DAF deben
      mantener antecedentes ordenados para fiscalizaciones.
    - Ciclo_Presupuestario.Control_y_Seguimiento.Control_CGR.Resp=Contraloría General
      de la República (CGR).
    - Ciclo_Presupuestario.Control_y_Seguimiento.Control_Interno_GORE.Act[0]=Revisar
      actos administrativos de contenido financiero (control ex-ante).
    - Ciclo_Presupuestario.Control_y_Seguimiento.Control_Interno_GORE.Act[1]=Visar
      resoluciones, verificar respaldos y revisar rendiciones.
    - Ciclo_Presupuestario.Control_y_Seguimiento.Control_Interno_GORE.ID=GORE-FIN-CONTROL-INTERNO-01
    - Ciclo_Presupuestario.Control_y_Seguimiento.Control_Interno_GORE.Req=DAF colabora
      para subsanar observaciones.
    - Ciclo_Presupuestario.Control_y_Seguimiento.Control_Interno_GORE.Resp=Unidad
      de Control o auditoría interna del GORE.
    - Ciclo_Presupuestario.Control_y_Seguimiento.Seguimiento_DIPRES.Act[0]=Monitorea
      ejecución presupuestaria mensual de los GORE mediante informes, reuniones y
      alertas de baja ejecución.
    - Ciclo_Presupuestario.Control_y_Seguimiento.Seguimiento_DIPRES.ID=GORE-FIN-CONTROL-SEGUIMIENTO-DIPRES-01
    - Ciclo_Presupuestario.Control_y_Seguimiento.Seguimiento_DIPRES.Req=GORE debe
      gestionar un calendario de hitos para asegurar cumplimiento.
    - Ciclo_Presupuestario.Control_y_Seguimiento.Seguimiento_DIPRES.Resp=Dirección
      de Presupuestos (DIPRES).
    - Ciclo_Presupuestario.Control_y_Seguimiento.Transparencia_y_Control_Social.Fnd=Ley
      N° 21.796 (Normas Generales) + Requerimientos de información Partida 31 (ver
      INFO-REQS-2026-GORES-01 en artefacto glosas GORES 2026).
    - Ciclo_Presupuestario.Control_y_Seguimiento.Transparencia_y_Control_Social.ID=GORE-FIN-CONTROL-TRANSPARENCIA-01
    - Ciclo_Presupuestario.Control_y_Seguimiento.Transparencia_y_Control_Social.Nat=Control
      social sobre inversión regional.
    - Ciclo_Presupuestario.Control_y_Seguimiento.Transparencia_y_Control_Social.Req[0]=Publicar
      mensualmente en sitio web del GORE la cartera de proyectos financiados con inversión
      regional.
    - Ciclo_Presupuestario.Control_y_Seguimiento.Transparencia_y_Control_Social.Req[1]=Publicar
      acuerdos del CORE en máximo 5 días hábiles.
    - 'Ciclo_Presupuestario.Control_y_Seguimiento.Transparencia_y_Control_Social.Req[2]=Informar
      trimestralmente el uso de recursos de inversión regional: listado de beneficiarios,
      comuna, instituciones receptoras, monto, productos del convenio y su aplicación
      a nivel regional.'
    - Ciclo_Presupuestario.Control_y_Seguimiento.Transparencia_y_Control_Social.Req[3]=Informar
      y publicar trimestralmente el destino de recursos FNDR a proyectos de desarrollo
      económico y los proyectos adjudicados por sectores según actividad económica.
    - Ciclo_Presupuestario.Control_y_Seguimiento.Transparencia_y_Control_Social.Req[4]=Publicar
      trimestralmente e informar a senadores y diputados de la región todos los proyectos
      adjudicados o contratados con cargo a Subt. 24 (oferta programática) y Subt.
      31 y 33, incluyendo nombre del proyecto, monto estimado, postulantes, pauta
      de evaluación, seleccionado, presupuesto aprobado y votación del CORE.
    - 'Ciclo_Presupuestario.Control_y_Seguimiento.Transparencia_y_Control_Social.Req[5]=Informar
      trimestralmente transferencias con cargo al Fondo de Vinculación con la Comunidad
      (8%): beneficiario, comuna, objeto del financiamiento, montos totales y fecha
      de cada transferencia.'
    - 'Ciclo_Presupuestario.Control_y_Seguimiento.Transparencia_y_Control_Social.Req[6]=Informar
      trimestralmente iniciativas y proyectos de inversión que superen 500 UTM: proyecto,
      antecedentes para aprobación, montos, plazo de ejecución e identidad del receptor
      de recursos.'
    - Ciclo_Presupuestario.Control_y_Seguimiento.Transparencia_y_Control_Social.Req[7]=Informar
      trimestralmente la disponibilidad presupuestaria para que universidades reconocidas
      por el Estado accedan a asignaciones directas de recursos FRPD y las solicitudes
      recibidas.
    - Ciclo_Presupuestario.Control_y_Seguimiento.Transparencia_y_Control_Social.Req[8]=Publicar
      acuerdos del CORE en máximo 5 días hábiles e información de corporaciones financiadas.
    - Ciclo_Presupuestario.Control_y_Seguimiento.Transparencia_y_Control_Social.Req[9]=Publicar
      información en formato digital legible y procesable, que no consista solamente
      en imágenes.
    - Ciclo_Presupuestario.Control_y_Seguimiento.Transparencia_y_Control_Social.Req[10]=Publicar
      en transparencia activa las actas de evaluación emitidas por comisiones evaluadoras
      de licitaciones y compras públicas (Ley N°19.886).
    - Ciclo_Presupuestario.Control_y_Seguimiento.Transparencia_y_Control_Social.Req[11]=Procurar
      lenguaje claro y vincular el presupuesto a orientaciones estratégicas, objetivos
      prioritarios y resultados esperados.
    - Ciclo_Presupuestario.Control_y_Seguimiento.Transparencia_y_Control_Social.Req[12]=Publicar
      de forma permanente en transparencia activa (literal k) art. 7 Ley N°20.285)
      los montos recibidos y ejecución presupuestaria del FRPD, incluyendo detalle
      de transferencias efectuadas.
    - Ciclo_Presupuestario.Control_y_Seguimiento.Transparencia_y_Control_Social.Resp=DIPIR
      compila información, DAF valida cifras.
    - Ciclo_Presupuestario.Ejecucion.Coordinacion_DAF_DIPIR.Ejemplos[0]=DIPIR informa
      a DAF proyectos retrasados para evaluar modificación presupuestaria.
    - Ciclo_Presupuestario.Ejecucion.Coordinacion_DAF_DIPIR.Ejemplos[1]=DAF alerta
      a DIPIR sobre partidas en agotamiento o riesgo de sobregiro.
    - Ciclo_Presupuestario.Ejecucion.Coordinacion_DAF_DIPIR.Fnd=Comunicación constante
      DAF-DIPIR es esencial para gestionar modificaciones y ejecución.
    - Ciclo_Presupuestario.Ejecucion.Coordinacion_DAF_DIPIR.ID=GORE-FIN-EJEC-COORDINACION-01
    - Ciclo_Presupuestario.Ejecucion.Programacion_Ejecucion_y_Caja.Asunto=Programación
      de ejecución y de caja.
    - Ciclo_Presupuestario.Ejecucion.Programacion_Ejecucion_y_Caja.Cpt[0]=DIPRES elabora
      programa de ejecución inicial mensualizado; GORE propone su programa.
    - Ciclo_Presupuestario.Ejecucion.Programacion_Ejecucion_y_Caja.Cpt[1]=GORE remite
      actualizaciones mensuales a más tardar el día 15, detallando aporte fiscal y
      fuentes.
    - Ciclo_Presupuestario.Ejecucion.Programacion_Ejecucion_y_Caja.Cpt[2]=Programa
      de Caja Mensual se basa en ejecución programada menos saldos disponibles para
      calcular necesidades de aporte fiscal y evitar recursos ociosos.
    - Ciclo_Presupuestario.Ejecucion.Programacion_Ejecucion_y_Caja.ID=GORE-FIN-EJEC-PROGRAMACION-01
    - Ciclo_Presupuestario.Ejecucion.Programacion_Ejecucion_y_Caja.Ref[0]=GN-PPTO-GLOS-GORE
    - Ciclo_Presupuestario.Ejecucion.Programacion_Ejecucion_y_Caja.Ref[1]=GN-PPTO-GLOS-DIPRES
    - Ciclo_Presupuestario.Ejecucion.Programacion_Ejecucion_y_Caja.Src=Instructivo
      DIPRES Ejecución Presupuestaria (vigente).
    - Ciclo_Presupuestario.Ejecucion.Regla_Devengo_Por_Tipo_Transferencia.Asunto=Reglas
      de devengo diferenciadas según tipo de transferencia.
    - 'Ciclo_Presupuestario.Ejecucion.Regla_Devengo_Por_Tipo_Transferencia.Casos[0]=Transferencias
      extrapresupuestarias (Subt. 24-03, 33-03) a instituciones de la Ley de Presupuestos:
      devengo al aprobarse la rendición (no al transferir).'
    - 'Ciclo_Presupuestario.Ejecucion.Regla_Devengo_Por_Tipo_Transferencia.Casos[1]=Transferencias
      presupuestarias consolidables o a municipios (Subt. 24-02, 33-02; 24-03, 33-03):
      regla general, devengo cuando la obligación es exigible (acto o convenio tramitado).'
    - 'Ciclo_Presupuestario.Ejecucion.Regla_Devengo_Por_Tipo_Transferencia.Casos[2]=Transferencias
      a entidades privadas (Subt. 24-01, 33-01): devengo cuando la obligación es exigible
      conforme al convenio/acto.'
    - Ciclo_Presupuestario.Ejecucion.Regla_Devengo_Por_Tipo_Transferencia.Fnd=Momento
      del devengo varía según receptor y modalidad; impacta metas de ejecución.
    - Ciclo_Presupuestario.Ejecucion.Regla_Devengo_Por_Tipo_Transferencia.ID=GORE-FIN-EJEC-DEVENGO-01
    - Ciclo_Presupuestario.Ejecucion.Regla_Devengo_Por_Tipo_Transferencia.Ref[0]=GN-PPTO-GLOS-CGR
    - Ciclo_Presupuestario.Ejecucion.Regla_Devengo_Por_Tipo_Transferencia.Src=Minuta
      CGR-AGORECHI-DIPRES marzo 2025; Dictamen CGR N°E583841/2024.
    - Ciclo_Presupuestario.Ejecucion.Rol_DAF_en_Ejecucion.Cpt_Control_Interno[0]=Resguardar
      respaldo legal de cada desembolso.
    - Ciclo_Presupuestario.Ejecucion.Rol_DAF_en_Ejecucion.Cpt_Control_Interno[1]=Asegurar
      respeto al destino de fondos según glosas.
    - Ciclo_Presupuestario.Ejecucion.Rol_DAF_en_Ejecucion.Cpt_Control_Interno[2]=Certificar
      disponibilidad presupuestaria y límites legales con coordinación de Unidad de
      Control.
    - Ciclo_Presupuestario.Ejecucion.Rol_DAF_en_Ejecucion.Cpt_Gestion_Financiera[0]=Garantizar
      gasto dentro de montos y clasificaciones autorizadas.
    - Ciclo_Presupuestario.Ejecucion.Rol_DAF_en_Ejecucion.Cpt_Gestion_Financiera[1]=Registrar
      preafectación, compromiso, devengo y pago en SIGFE.
    - Ciclo_Presupuestario.Ejecucion.Rol_DAF_en_Ejecucion.Cpt_Gestion_Financiera[2]=Supervisar
      programación de caja con DIPRES.
    - Ciclo_Presupuestario.Ejecucion.Rol_DAF_en_Ejecucion.Cpt_Pagos_y_Contabilidad[0]=Tramitar
      órdenes de compra, afectar gastos y realizar pagos (obligatoriamente vía transferencia
      electrónica, Art. 08 Ley 21.796).
    - Ciclo_Presupuestario.Ejecucion.Rol_DAF_en_Ejecucion.Cpt_Pagos_y_Contabilidad[1]=Cumplir
      normativa de compras públicas y rendición de cuentas.
    - Ciclo_Presupuestario.Ejecucion.Rol_DAF_en_Ejecucion.Cpt_Pagos_y_Contabilidad[2]=Elaborar
      informes financieros periódicos para DIPRES.
    - Ciclo_Presupuestario.Ejecucion.Rol_DAF_en_Ejecucion.Cpt_Pagos_y_Contabilidad[3]=Identificar
      mensualmente iniciativas de inversión (Subt. 31) por código BIP.
    - Ciclo_Presupuestario.Ejecucion.Rol_DAF_en_Ejecucion.ID=GORE-FIN-EJEC-ROL-DAF-01
    - Ciclo_Presupuestario.Ejecucion.Rol_DAF_en_Ejecucion.Ref[0]=GN-PPTO-GLOS-DAF
    - Ciclo_Presupuestario.Ejecucion.Rol_DAF_en_Ejecucion.Ref[1]=GN-PPTO-GLOS-SIGFE
    - Ciclo_Presupuestario.Ejecucion.Rol_DAF_en_Ejecucion.Ref[2]=GN-PPTO-GLOS-DIPRES
    - Ciclo_Presupuestario.Ejecucion.Rol_DAF_en_Ejecucion.Resp=DAF lidera administración
      financiera diaria.
    - Ciclo_Presupuestario.Ejecucion.Rol_DIPIR_en_Ejecucion.Cpt_Coord_Externa[0]=Articular
      con SEREMI, servicios públicos sectoriales y municipios beneficiarios.
    - Ciclo_Presupuestario.Ejecucion.Rol_DIPIR_en_Ejecucion.Cpt_Monitoreo_Proyectos[0]=Revisar
      avance físico de obras e iniciativas (Subt. 31 y 33).
    - Ciclo_Presupuestario.Ejecucion.Rol_DIPIR_en_Ejecucion.Cpt_Monitoreo_Proyectos[1]=Detectar
      atrasos o desviaciones y proponer acciones correctivas.
    - Ciclo_Presupuestario.Ejecucion.Rol_DIPIR_en_Ejecucion.Cpt_Monitoreo_Proyectos[2]=Evaluar
      cumplimiento de hitos de convenios (trimestral) y preparar informes para instancias
      externas.
    - Ciclo_Presupuestario.Ejecucion.Rol_DIPIR_en_Ejecucion.Cpt_Uso_Herramientas[0]=Actualizar
      estados en BIP y cargar ejecución físico-financiera (primeros 8 días del mes
      siguiente).
    - Ciclo_Presupuestario.Ejecucion.Rol_DIPIR_en_Ejecucion.Cpt_Uso_Herramientas[1]=Verificar
      vigencia técnica (RS) y usar SIGFE para seguimiento financiero.
    - 'Ciclo_Presupuestario.Ejecucion.Rol_DIPIR_en_Ejecucion.Cpt_Uso_Herramientas[2]=Referencias:
      GORE-FIN-HERRAM-BIP-01, GORE-FIN-HERRAM-SIGFE-01.'
    - Ciclo_Presupuestario.Ejecucion.Rol_DIPIR_en_Ejecucion.ID=GORE-FIN-EJEC-ROL-DIPIR-01
    - Ciclo_Presupuestario.Ejecucion.Rol_DIPIR_en_Ejecucion.Ref[0]=GN-PPTO-GLOS-DIPIR
    - Ciclo_Presupuestario.Ejecucion.Rol_DIPIR_en_Ejecucion.Ref[1]=GN-PPTO-GLOS-BIP
    - Ciclo_Presupuestario.Ejecucion.Rol_DIPIR_en_Ejecucion.Ref[2]=GN-PPTO-GLOS-SIGFE
    - Ciclo_Presupuestario.Ejecucion.Rol_DIPIR_en_Ejecucion.Ref[3]=GN-PPTO-GLOS-SNI
    - Ciclo_Presupuestario.Ejecucion.Rol_DIPIR_en_Ejecucion.Resp=DIPIR lidera seguimiento
      físico y presupuestario de la inversión.
    - 'Ciclo_Presupuestario.Etapas_Generales.Cpt[0]=Etapas: 1) Formulación, 2) Aprobación
      / Distribución Inicial, 3) Ejecución, 4) Modificaciones, 5) Control y Seguimiento,
      6) Cierre.'
    - 'Ciclo_Presupuestario.Etapas_Generales.Cpt[1]=Rol general DAF: financiero-administrativo.'
    - 'Ciclo_Presupuestario.Etapas_Generales.Cpt[2]=Rol general DIPIR: estratégico-programático
      de inversión (complementariedad de roles).'
    - Ciclo_Presupuestario.Etapas_Generales.ID=GORE-FIN-CICLO-ETAPAS-01
    - Ciclo_Presupuestario.Etapas_Generales.Purp=Describir las etapas del ciclo presupuestario
      y roles de DAF y DIPIR.
    - Ciclo_Presupuestario.Formulacion.Coordinacion_ARI_PROPIR.Asunto=Coordinación
      regional del gasto público vía ARI y PROPIR.
    - 'Ciclo_Presupuestario.Formulacion.Coordinacion_ARI_PROPIR.Def[0]=ARI: estimación
      de inversión de GORE, ministerios y servicios para el año siguiente.'
    - 'Ciclo_Presupuestario.Formulacion.Coordinacion_ARI_PROPIR.Def[1]=PROPIR: planificación
      y seguimiento del gasto público regional del año en curso.'
    - Ciclo_Presupuestario.Formulacion.Coordinacion_ARI_PROPIR.ID=GORE-FIN-FORM-ARI-PROPIR-01
    - Ciclo_Presupuestario.Formulacion.Coordinacion_ARI_PROPIR.Mech[0]=Ambos se gestionan
      en plataforma Chileindica (<www.chileindica.cl>).
    - Ciclo_Presupuestario.Formulacion.Coordinacion_ARI_PROPIR.Proc_Discrepancias[0]=Resolución
      en instancia regional.
    - Ciclo_Presupuestario.Formulacion.Coordinacion_ARI_PROPIR.Proc_Discrepancias[1]=Si
      persisten, tratamiento en comisiones técnicas de formulación presupuestaria
      a nivel central.
    - Ciclo_Presupuestario.Formulacion.Coordinacion_ARI_PROPIR.Ref[0]=GN-PPTO-GLOS-ARI
    - Ciclo_Presupuestario.Formulacion.Coordinacion_ARI_PROPIR.Ref[1]=GN-PPTO-GLOS-PROPIR
    - Ciclo_Presupuestario.Formulacion.Coordinacion_ARI_PROPIR.Resp_GORE[0]=Gobernador
      conduce el proceso (puede delegar en Jefe DIPLADE).
    - Ciclo_Presupuestario.Formulacion.Coordinacion_ARI_PROPIR.Resp_GORE[1]=DIPLADE
      lidera Secretaría Ejecutiva de la Coordinación Regional del Gasto Público (SEREMI
      y jefes de servicios).
    - Ciclo_Presupuestario.Formulacion.Coordinacion_ARI_PROPIR.Resp_GORE[2]=Admisión
      de iniciativas, fijación de plazos de postulación ARI (máx. primeros 4 meses).
    - Ciclo_Presupuestario.Formulacion.Coordinacion_ARI_PROPIR.Resp_GORE[3]=Informe
      trimestral PROPIR al CORE y envío ARI aprobado a ministerios.
    - Ciclo_Presupuestario.Formulacion.Coordinacion_ARI_PROPIR.Resp_Servicios_Publicos[0]=Ingresar
      iniciativas a Chileindica con desglose comunal, montos, fuente, beneficiarios
      y alineación con ERD.
    - Ciclo_Presupuestario.Formulacion.Coordinacion_ARI_PROPIR.Resp_Servicios_Publicos[1]=Informar
      ejecución financiera mensual PROPIR y comunicar ausencia de inversión cuando
      aplique.
    - Ciclo_Presupuestario.Formulacion.Coordinacion_ARI_PROPIR.Src=Instructivo Coordinación
      Gasto Público ARI 2026 y PROPIR (año en curso; versión 2025 no disponible en
      este corpus).
    - Ciclo_Presupuestario.Formulacion.Coordinacion_DIPIR_DAF.Cpt_Tareas_Glosas[0]=Identificar
      y explicitar glosas aplicables (dotaciones, vehículos, viáticos, etc.).
    - 'Ciclo_Presupuestario.Formulacion.Coordinacion_DIPIR_DAF.Cpt_Tareas_Glosas[1]=Ejemplo:
      glosas de la Partida 31 en Ley de Presupuestos 2026.'
    - Ciclo_Presupuestario.Formulacion.Coordinacion_DIPIR_DAF.Cpt_Tareas_Justificacion_Inversiones[0]=Justificar
      técnica y socialmente las inversiones propuestas.
    - Ciclo_Presupuestario.Formulacion.Coordinacion_DIPIR_DAF.Cpt_Tareas_Justificacion_Inversiones[1]=Obtener
      Recomendación Satisfactoria (RS) de MDSF para inclusión en presupuesto (salvo
      excepciones como FRIL).
    - Ciclo_Presupuestario.Formulacion.Coordinacion_DIPIR_DAF.Cpt_Tareas_Justificacion_Inversiones[2]=Mantener
      todos los proyectos en SNI con código BIP para formulación y seguimiento físico-financiero.
    - Ciclo_Presupuestario.Formulacion.Coordinacion_DIPIR_DAF.Cpt_Tareas_Provisiones[0]=Crear
      provisiones específicas (ej. FRPD en ítem 33.03, FRIL, provisiones 8% FNDR).
    - Ciclo_Presupuestario.Formulacion.Coordinacion_DIPIR_DAF.ID=GORE-FIN-FORM-COORDINACION-01
    - Ciclo_Presupuestario.Formulacion.Coordinacion_DIPIR_DAF.Ref[0]=GN-PPTO-GLOS-DIPIR
    - Ciclo_Presupuestario.Formulacion.Coordinacion_DIPIR_DAF.Ref[1]=GN-PPTO-GLOS-DAF
    - Ciclo_Presupuestario.Formulacion.Coordinacion_DIPIR_DAF.Ref[2]=GN-PPTO-GLOS-FNDR
    - Ciclo_Presupuestario.Formulacion.Coordinacion_DIPIR_DAF.Ref[3]=GN-PPTO-GLOS-FRIL
    - Ciclo_Presupuestario.Formulacion.Coordinacion_DIPIR_DAF.Ref[4]=GN-PPTO-GLOS-FRPD
    - Ciclo_Presupuestario.Formulacion.Coordinacion_DIPIR_DAF.Ref[5]=GN-PPTO-GLOS-SNI
    - Ciclo_Presupuestario.Formulacion.Coordinacion_DIPIR_DAF.Ref[6]=GN-PPTO-GLOS-BIP
    - Ciclo_Presupuestario.Formulacion.Coordinacion_DIPIR_DAF.Resp=Responsabilidad
      compartida entre DIPIR y DAF.
    - Ciclo_Presupuestario.Formulacion.Rol_DAF_Proyecciones_y_Clasificacion.Cpt_Tareas_Clasificacion[0]=Verificar
      correcta aplicación del clasificador presupuestario (Decreto N°854/2004).
    - Ciclo_Presupuestario.Formulacion.Rol_DAF_Proyecciones_y_Clasificacion.Cpt_Tareas_Clasificacion[1]=Asegurar
      nivel de detalle adecuado (Subtítulo, Ítem, Asignación), especialmente en transferencias
      (Subt. 24 y 33).
    - Ciclo_Presupuestario.Formulacion.Rol_DAF_Proyecciones_y_Clasificacion.Cpt_Tareas_Clasificacion[2]=Respetar
      principio de legalidad del gasto.
    - Ciclo_Presupuestario.Formulacion.Rol_DAF_Proyecciones_y_Clasificacion.Cpt_Tareas_Funcionamiento[0]=Proyectar
      gastos de funcionamiento (Subtítulos 21 y 22) con base en dotación vigente y
      gastos recurrentes.
    - Ciclo_Presupuestario.Formulacion.Rol_DAF_Proyecciones_y_Clasificacion.Cpt_Tareas_Funcionamiento[1]=Cumplir
      restricciones legales de gasto en personal y viáticos (ej. Art. 04 Ley 21.796).
    - Ciclo_Presupuestario.Formulacion.Rol_DAF_Proyecciones_y_Clasificacion.ID=GORE-FIN-FORM-ROL-DAF-01
    - Ciclo_Presupuestario.Formulacion.Rol_DAF_Proyecciones_y_Clasificacion.Ref[0]=GN-PPTO-GLOS-DAF
    - Ciclo_Presupuestario.Formulacion.Rol_DAF_Proyecciones_y_Clasificacion.Resp=DAF
      aporta información financiera y administrativa a la formulación.
    - Ciclo_Presupuestario.Formulacion.Rol_DIPIR_Oferta_Programatica.Cpt_Tareas[0]=Diseñar
      programas públicos ejecutados por el GORE usando Metodología de Marco Lógico.
    - Ciclo_Presupuestario.Formulacion.Rol_DIPIR_Oferta_Programatica.Cpt_Tareas[1]=Preparar
      antecedentes para evaluación ex-ante (DIPRES/MDSF) de programas Glosa 06.
    - Ciclo_Presupuestario.Formulacion.Rol_DIPIR_Oferta_Programatica.Cpt_Tareas[2]=Identificar
      programas nuevos o sustancialmente reformulados que requieren evaluación obligatoria.
    - Ciclo_Presupuestario.Formulacion.Rol_DIPIR_Oferta_Programatica.Cpt_Tareas[3]=Coordinar
      con DIPLADE y otras divisiones técnicas.
    - Ciclo_Presupuestario.Formulacion.Rol_DIPIR_Oferta_Programatica.Fnd=Glosa 06
      Partida 31 Ley 21.796, Oficio Circular N°22 DIPRES.
    - Ciclo_Presupuestario.Formulacion.Rol_DIPIR_Oferta_Programatica.ID=GORE-FIN-FORM-ROL-DIPIR-PROGRAMAS-01
    - Ciclo_Presupuestario.Formulacion.Rol_DIPIR_Oferta_Programatica.Ref[0]=GN-PPTO-GLOS-DIPIR
    - Ciclo_Presupuestario.Formulacion.Rol_DIPIR_Oferta_Programatica.Ref[1]=GN-PPTO-GLOS-DIPRES
    - Ciclo_Presupuestario.Formulacion.Rol_DIPIR_Oferta_Programatica.Ref[2]=GN-PPTO-GLOS-MDSF
    - Ciclo_Presupuestario.Formulacion.Rol_DIPIR_Proyecto_Presupuesto.Cpt_Tareas_Inversion[0]=Elaborar
      proyecto de presupuesto de inversiones.
    - Ciclo_Presupuestario.Formulacion.Rol_DIPIR_Proyecto_Presupuesto.Cpt_Tareas_Inversion[1]=Asesorar
      al Gobernador en selección de proyectos.
    - Ciclo_Presupuestario.Formulacion.Rol_DIPIR_Proyecto_Presupuesto.Cpt_Tareas_Inversion[2]=Coordinar
      ARI (Anteproyecto Regional de Inversiones) y PROPIR (Programa de Inversión Regional).
    - Ciclo_Presupuestario.Formulacion.Rol_DIPIR_Proyecto_Presupuesto.Cpt_Tareas_Inversion[3]=Recopilar
      iniciativas de servicios públicos (plataforma Chileindica).
    - Ciclo_Presupuestario.Formulacion.Rol_DIPIR_Proyecto_Presupuesto.Cpt_Tareas_Inversion[4]=Asegurar
      alineación con la Estrategia Regional de Desarrollo (ERD) y coordinar con DIPLADE.
    - Ciclo_Presupuestario.Formulacion.Rol_DIPIR_Proyecto_Presupuesto.Ctx=Foco en
      inversión regional y oferta programática.
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
---

# Gestión Financiera y Operativa del Presupuesto Regional 2026
## ID
GN-PPTO-GESTION-INTEGRAL-2026-01

## Version
1.0.0

## Status
Draft

## Format
KODA/Spec

## Human Creator
FS

## Human Editor
FS

## Model Collaborator
GPT-5.2

## AI Remediator
KODA-TRANSFORMER

## Creation Date
2026-01-02

## Modification Date
2026-01-02

## Ctx
Guía técnico-operativa 2026 para la gestión completa del presupuesto regional en Gobiernos Regionales (con foco en GORE Ñuble), alineada a Ley de Presupuestos 2026 (Ley N° 21.796) y glosas/reqs de información Partida 31.

## Primary Source
kb_gn_018_gestion_prpto.md

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

LEXICON (expand before processing): Act->Action, Cond->Condition, Cpt->Concept, Ctx->Context, Ctx_Required->Required External Reference, Ctx_Optional->Optional External Reference, Def->Definition, Ex->Example, Fnd->Foundation, ID->ID, Mech->Mechanism, Mssn->Mission, Nat->Nature, Obj->Objective, Proc->Process, Prohib->Prohibition, Purp->Purpose, Ref->Reference, Req->Requirement, Res->Result, Resp->Responsible, Src->Source, Warn->Warning, XRef->Cross-Artifact Reference, XRef_Required->Mandatory Cross-Artifact Reference.

REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. XRef/XRef_Required: are external only—must point to a URN (optionally with #ID fragment) in another artifact. External documents without specific ID use Ctx:, Ctx_Required:, Ctx_Optional:, or Src:.

LANGUAGE POLICY: Keywords in English (and abbreviated forms as listed), content in original language (Spanish). Never translate content.
END_LLM_INSTRUCTIONS


## Glosario PPTO Clave
### ID
GN-PPTO-GLOSARIO-01
### Purp
Definir conceptos y siglas presupuestarias clave utilizados en la guía.
### Terminos
| ID | Sigla | Nombre | Def |
| --- | --- | --- | --- |
| GN-PPTO-GLOS-GORE | GORE | Gobierno Regional | Entidad pública autónoma, con personalidad jurídica y patrimonio propio, encargada de la administración superior de la región. |
| GN-PPTO-GLOS-CORE | CORE | Consejo Regional | Órgano colegiado del GORE, con facultades normativas, resolutivas y fiscalizadoras. |
| GN-PPTO-GLOS-DAF | DAF | División de Administración y Finanzas | División responsable de la gestión administrativa interna, finanzas, presupuesto de funcionamiento y pagos del GORE. |
| GN-PPTO-GLOS-DIPIR | DIPIR | División de Presupuesto e Inversión Regional | División encargada del presupuesto de inversión, programación y seguimiento de iniciativas de inversión y programas regionales. |
| GN-PPTO-GLOS-DIPRES | DIPRES | Dirección de Presupuestos | Órgano técnico del Ministerio de Hacienda encargado de la formulación, ejecución y control del Presupuesto del Sector Público. |
| GN-PPTO-GLOS-CGR | CGR | Contraloría General de la República | Órgano de control que ejerce control de legalidad previo (Toma de Razón) y posterior sobre actos presupuestarios del GORE. |
| GN-PPTO-GLOS-MDSF | MDSF | Ministerio de Desarrollo Social y Familia | Organismo responsable de la evaluación técnico-económica de iniciativas de inversión en el SNI. |
| GN-PPTO-GLOS-SIGFE | SIGFE | Sistema de Información para la Gestión Financiera del Estado | Sistema contable-presupuestario oficial donde se registra la ejecución del presupuesto del GORE. |
| GN-PPTO-GLOS-BIP | BIP | Banco Integrado de Proyectos | Plataforma del SNI para el registro y seguimiento de iniciativas de inversión pública. |
| GN-PPTO-GLOS-SNI | SNI | Sistema Nacional de Inversiones | Marco y plataforma para la evaluación técnico-económica de proyectos de inversión pública. |
| GN-PPTO-GLOS-FNDR | FNDR | Fondo Nacional de Desarrollo Regional | Principal fuente de financiamiento de la inversión regional administrada por los GORE. |
| GN-PPTO-GLOS-FRIL | FRIL | Fondo Regional de Iniciativa Local | Fondo destinado a proyectos de infraestructura de menor escala, ejecutados principalmente por municipalidades. |
| GN-PPTO-GLOS-FRPD | FRPD | Fondo Regional para la Productividad y el Desarrollo | Fondo financiado con recursos del royalty minero para iniciativas de innovación, competitividad y desarrollo productivo. |
| GN-PPTO-GLOS-ARI | ARI | Anteproyecto Regional de Inversiones | Instrumento de planificación que estima la inversión pública en la región para el año siguiente. |
| GN-PPTO-GLOS-PROPIR | PROPIR | Programa Público de Inversión en la Región | Instrumento que organiza y monitorea el gasto público a ejecutar en la región en el año en curso. |
| GN-PPTO-GLOS-SISREC | SISREC | Sistema de Rendición Electrónica de Cuentas | Plataforma de la Contraloría General de la República para gestionar rendiciones de cuentas de transferencias. |

## Presentacion
### ID
GORE-FIN-PRESENTACION-01
### Asunto
Guía técnico-operativa para gestión completa de presupuesto en GORE.
### Purp
Proveer marco de referencia para la gestión presupuestaria regional en todas sus etapas (formulación -> cierre).
### Dest
- Jefaturas División Administración y Finanzas (DAF).
- Jefaturas División Presupuesto e Inversión Regional (DIPIR).
- Equipos técnicos GORE y actores regionales vinculados a la gestión presupuestaria.
### Ref
- GN-PPTO-GLOS-GORE
- GN-PPTO-GLOS-DAF
- GN-PPTO-GLOS-DIPIR

## Contexto y Marco Normativo
### ID
GORE-FIN-CTX-01
### Introduccion
#### ID
GORE-FIN-CTX-INTRO-01
#### Purp
Establecer propósito, alcance y marco normativo de la guía.
#### Req
Claridad operativa y precisión técnica para gestión diaria del presupuesto regional.
#### Cpt
Aborda el ciclo presupuestario completo (formulación, aprobación, ejecución, modificaciones, control, cierre).
#### Fnd
- D.F.L. N°1-19.175 (LOC GORE).
- D.L. N°1.263/1975 (Administración Financiera del Estado).
- Ley de Presupuestos del Sector Público (anual, ej. Ley 21.796 para 2026).
- Normas DIPRES (oficios circulares, instructivos de ejecución).
- Normas Contraloría General de la República (CGR) (resoluciones, instructivos).
- Jerarquía normativa: Ley > Decreto > Resolución > Oficio Circular > Instructivo.
#### Ref
- GN-PPTO-GLOS-GORE
- GN-PPTO-GLOS-DIPRES
- GN-PPTO-GLOS-CGR
- GN-PPTO-GLOS-MDSF
### Cambios Presupuestarios 2025
#### ID
GORE-FIN-CTX-CAMBIOS-2025-01
#### Asunto
Cambios estructurales en presupuesto GORE desde 2025 (vigentes en 2026).
#### Src
Oficio Circular N°11 DIPRES 2025 (última versión disponible en corpus).
#### Cpt
- Creación de 16 programas presupuestarios (uno por región) que integran funcionamiento e inversión.
- Creación de programa especial 'Asociatividad y Planes Especiales' para asociatividad regional, zonas extremas y territorios rezagados.
#### Cause
Profundización del proceso de descentralización fiscal.
#### Res
Requiere coordinación estrecha DAF-DIPIR para gestionar un solo programa integrado.
#### Ctx
- Mayor oferta programática regional (ejecución directa y transferencias), incluyendo 8% FNDR y programas Glosa 06.
- Dualidad de gestión: GORE debe administrar simultáneamente el Sistema Nacional de Inversiones (SNI) para proyectos de inversión y la evaluación ex-ante DIPRES/MDSF para programas.
### Ley Presupuestos 2026
#### ID
GORE-FIN-CTX-LEY-PPTO-2026-01
#### Purp
Referencia normativa base (KODA) para gestión presupuestaria 2026: normas generales + glosas y requerimientos de información de Partida 31.
#### Ley
#### Numero
21.796
#### Titulo
LEY DE PRESUPUESTOS DEL SECTOR PÚBLICO CORRESPONDIENTE AL AÑO 2026
#### Fuente
#### Src
DIARIO OFICIAL DE LA REPUBLICA DE CHILE
#### Fecha
Viernes 12 de Diciembre de 2025
#### CVE
2741100
#### XRef Required
- urn:knowledge:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-NORMAS-GENERALES-01
- urn:knowledge:gorenuble:presupuesto:glosas-gores-2026:1.0.0#GLOSAS-GORES-2026-01
- urn:knowledge:gorenuble:presupuesto:glosas-gores-2026:1.0.0#INFO-REQS-2026-GORES-01
#### Src
- knowledge/domains/gn/presupuesto/kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml
- knowledge/domains/gn/presupuesto/kb_gn_211_ley_presupuestos_2026_glosas_gores_2026_koda.yml

## Conceptos Presupuestarios Fundamentales
### ID
GORE-FIN-CONCEPTOS-FUNDAMENTALES-01
### Introduccion
#### ID
GORE-FIN-CONCEPTOS-INTRO-01
#### Purp
Establecer conceptos básicos del sistema presupuestario chileno que dan contexto a la gestión GORE.
#### Src
DL N°1.263/1975, Decreto N°854/2004 Hacienda y normativa presupuestaria general.
### Presupuesto Sector Publico
#### ID
GORE-FIN-CONCEPTOS-PUP-DEF-01
#### Def
Estimación financiera de ingresos y gastos del sector público para un año, que compatibiliza recursos disponibles con metas y objetivos preestablecidos.
#### Fnd
Art. 11, DL N°1.263/1975.
#### Nat
Instrumento de política fiscal que refleja prioridades de gobierno y gestión; conjuga dimensión jurídica (Ley), técnica (clasificadores) y contable (recursos financieros).
### Principios Presupuestarios
#### ID
GORE-FIN-CONCEPTOS-PUP-PRINCIPIOS-01
#### Asunto
Principios rectores del presupuesto público.
#### Cpt
- Principio de Universalidad: todos los ingresos y gastos del Estado deben reflejarse en el presupuesto (Art. 4°, DL N°1.263/1975).
- Principio de Anualidad: el ejercicio presupuestario coincide con el año calendario (Art. 12, DL N°1.263/1975).
### Clasificadores Presupuestarios
#### Clasificacion Institucional
#### ID
GORE-FIN-CONCEPTOS-CLAS-INST-01
#### Purp
Agrupar presupuestariamente los organismos incluidos en la Ley de Presupuestos.
#### Cpt
Estructura jerárquica: Partida → Capítulo → Programa.
#### Detalle
- Partida: nivel superior de agrupación (Presidencia, Congreso, Ministerios, Partida 50 Tesoro Público). Ejemplo: Partida 31 - Gobiernos Regionales.
- Capítulo: subdivisión de la Partida; corresponde a cada organismo con presupuesto directo en la Ley. Ejemplo: un capítulo por cada uno de los 16 GORE.
- Programa: división presupuestaria del Capítulo, asociada a funciones u objetivos específicos (ej. Programa 01 Funcionamiento, 02 Inversión Regional, 03 Asociatividad y Planes Especiales).
#### Clasificacion Por Objeto
#### ID
GORE-FIN-CONCEPTOS-CLAS-OBJ-01
#### Purp
Ordenar las transacciones según su origen (ingresos) o destino (gastos).
#### Cpt
Estructura jerárquica: Subtítulo → Ítem → Asignación → Sub-asignación.
#### Ejemplos
- Subtítulos de gasto: 21 Gastos en Personal, 22 Bienes y Servicios de Consumo, 33 Transferencias de Capital.
- Subtítulos de ingreso: 08 Otros Ingresos Corrientes, 09 Aporte Fiscal, 15 Saldo Inicial de Caja.
- Ítem: motivo significativo de ingreso o gasto (ej. Ítem 01 Personal de Planta).
- Asignación: motivo específico (ej. Asignación 22.04.001 Materiales de Oficina).
- Sub-asignación: desglose más particular (ej. 21.01.001-001 Sueldos Bases).
#### Clasificacion Por Grado Afectacion
#### ID
GORE-FIN-CONCEPTOS-CLAS-AFECT-01
#### Purp
Registrar y controlar instancias previas al devengo en la ejecución del presupuesto.
#### Obj
Conocer avance en la aplicación de los recursos y la calidad del compromiso fiscal.
#### Etapas
- Preafectación: intenciones de gasto sin obligación a terceros (llamados a licitación, cotizaciones).
- Afectación: obligación sujeta a perfeccionamiento (adjudicación, selección de proveedor).
- Compromiso Cierto: obligación recíproca formalizada (orden de compra, contrato, nombramiento).
- Compromiso Implícito: gasto y devengo ocurren simultáneamente (servicios básicos, peajes).

## Ciclo Presupuestario
### ID
GORE-FIN-CICLO-PRESUP-01
### Ref
- GN-PPTO-GLOS-GORE
- GN-PPTO-GLOS-DAF
- GN-PPTO-GLOS-DIPIR
- GN-PPTO-GLOS-CORE
### Etapas Generales
#### ID
GORE-FIN-CICLO-ETAPAS-01
#### Purp
Describir las etapas del ciclo presupuestario y roles de DAF y DIPIR.
#### Cpt
- Etapas: 1) Formulación, 2) Aprobación / Distribución Inicial, 3) Ejecución, 4) Modificaciones, 5) Control y Seguimiento, 6) Cierre.
- Rol general DAF: financiero-administrativo.
- Rol general DIPIR: estratégico-programático de inversión (complementariedad de roles).
### Formulacion
#### Rol DIPIR Proyecto Presupuesto
#### ID
GORE-FIN-FORM-ROL-DIPIR-01
#### Resp
DIPIR lidera elaboración del proyecto de presupuesto del GORE.
#### Ctx
Foco en inversión regional y oferta programática.
#### Cpt Tareas Inversion
- Elaborar proyecto de presupuesto de inversiones.
- Asesorar al Gobernador en selección de proyectos.
- Coordinar ARI (Anteproyecto Regional de Inversiones) y PROPIR (Programa de Inversión Regional).
- Recopilar iniciativas de servicios públicos (plataforma Chileindica).
- Asegurar alineación con la Estrategia Regional de Desarrollo (ERD) y coordinar con DIPLADE.
#### Ref
- GN-PPTO-GLOS-DIPIR
#### Rol DIPIR Oferta Programatica
#### ID
GORE-FIN-FORM-ROL-DIPIR-PROGRAMAS-01
#### Cpt Tareas
- Diseñar programas públicos ejecutados por el GORE usando Metodología de Marco Lógico.
- Preparar antecedentes para evaluación ex-ante (DIPRES/MDSF) de programas Glosa 06.
- Identificar programas nuevos o sustancialmente reformulados que requieren evaluación obligatoria.
- Coordinar con DIPLADE y otras divisiones técnicas.
#### Fnd
Glosa 06 Partida 31 Ley 21.796, Oficio Circular N°22 DIPRES.
#### Ref
- GN-PPTO-GLOS-DIPIR
- GN-PPTO-GLOS-DIPRES
- GN-PPTO-GLOS-MDSF
#### Rol DAF Proyecciones y Clasificacion
#### ID
GORE-FIN-FORM-ROL-DAF-01
#### Resp
DAF aporta información financiera y administrativa a la formulación.
#### Cpt Tareas Funcionamiento
- Proyectar gastos de funcionamiento (Subtítulos 21 y 22) con base en dotación vigente y gastos recurrentes.
- Cumplir restricciones legales de gasto en personal y viáticos (ej. Art. 04 Ley 21.796).
#### Cpt Tareas Clasificacion
- Verificar correcta aplicación del clasificador presupuestario (Decreto N°854/2004).
- Asegurar nivel de detalle adecuado (Subtítulo, Ítem, Asignación), especialmente en transferencias (Subt. 24 y 33).
- Respetar principio de legalidad del gasto.
#### Ref
- GN-PPTO-GLOS-DAF
#### Coordinacion DIPIR DAF
#### ID
GORE-FIN-FORM-COORDINACION-01
#### Resp
Responsabilidad compartida entre DIPIR y DAF.
#### Cpt Tareas Glosas
- Identificar y explicitar glosas aplicables (dotaciones, vehículos, viáticos, etc.).
- Ejemplo: glosas de la Partida 31 en Ley de Presupuestos 2026.
#### Cpt Tareas Provisiones
- Crear provisiones específicas (ej. FRPD en ítem 33.03, FRIL, provisiones 8% FNDR).
#### Cpt Tareas Justificacion Inversiones
- Justificar técnica y socialmente las inversiones propuestas.
- Obtener Recomendación Satisfactoria (RS) de MDSF para inclusión en presupuesto (salvo excepciones como FRIL).
- Mantener todos los proyectos en SNI con código BIP para formulación y seguimiento físico-financiero.
#### Ref
- GN-PPTO-GLOS-DIPIR
- GN-PPTO-GLOS-DAF
- GN-PPTO-GLOS-FNDR
- GN-PPTO-GLOS-FRIL
- GN-PPTO-GLOS-FRPD
- GN-PPTO-GLOS-SNI
- GN-PPTO-GLOS-BIP
#### Coordinacion ARI PROPIR
#### ID
GORE-FIN-FORM-ARI-PROPIR-01
#### Asunto
Coordinación regional del gasto público vía ARI y PROPIR.
#### Src
Instructivo Coordinación Gasto Público ARI 2026 y PROPIR (año en curso; versión 2025 no disponible en este corpus).
#### Def
- ARI: estimación de inversión de GORE, ministerios y servicios para el año siguiente.
- PROPIR: planificación y seguimiento del gasto público regional del año en curso.
#### Mech
- Ambos se gestionan en plataforma Chileindica (<www.chileindica.cl>).
#### Resp GORE
- Gobernador conduce el proceso (puede delegar en Jefe DIPLADE).
- DIPLADE lidera Secretaría Ejecutiva de la Coordinación Regional del Gasto Público (SEREMI y jefes de servicios).
- Admisión de iniciativas, fijación de plazos de postulación ARI (máx. primeros 4 meses).
- Informe trimestral PROPIR al CORE y envío ARI aprobado a ministerios.
#### Resp Servicios Publicos
- Ingresar iniciativas a Chileindica con desglose comunal, montos, fuente, beneficiarios y alineación con ERD.
- Informar ejecución financiera mensual PROPIR y comunicar ausencia de inversión cuando aplique.
#### Proc Discrepancias
- Resolución en instancia regional.
- Si persisten, tratamiento en comisiones técnicas de formulación presupuestaria a nivel central.
#### Ref
- GN-PPTO-GLOS-ARI
- GN-PPTO-GLOS-PROPIR
### Aprobacion y Distribucion Inicial
#### Procedimiento Legal
#### ID
GORE-FIN-APROB-PROCEDIMIENTO-01
#### Asunto
Procedimiento legal para aprobación de presupuesto inicial del GORE.
#### Src
Glosa 01 Partida 31 Ley 21.796; Instructivo CGR Aprobación Presupuesto Inicial (vigente).
#### Proc Fases y Plazos
- Propuesta del Gobernador: presenta distribución inicial al CORE (10 días desde publicación de la Ley).
- Aprobación CORE: se pronuncia en 10 días desde recepción.
- Envío a DIPRES: Gobernador remite acuerdo aprobado en 5 días.
- Resoluciones DIPRES: elabora resoluciones de presupuesto de funcionamiento e inversión (10 días).
- Toma de Razón CGR: 15 días desde recepción (prorrogable por 15).
#### Contenido y Requisitos
#### ID
GORE-FIN-APROB-CONTENIDO-01
#### Src
Instructivo CGR Aprobación Presupuesto Inicial (vigente).
#### Req Generales
- Desagregación según clasificador presupuestario a nivel de Subtítulo e Ítem.
- Transferencias desagregadas a nivel de Asignación (Subt. 24 y 33).
- Clasificaciones coherentes con naturaleza del gasto y receptor (legalidad del gasto).
- Equilibrio entre ingresos y gastos; montos coinciden con Ley de Presupuestos.
- Coherencia entre propuesta Gobernador, acuerdo CORE y resoluciones DIPRES.
#### Req Presupuesto Funcionamiento
- Incluir glosas obligatorias (dotación, vehículos, viáticos, gasto CORE en el extranjero).
- Monto del Subtítulo 21 debe coincidir con lo autorizado en glosa específica.
#### Req Presupuesto Inversion
- Incluir arrastres de años anteriores conservando número de asignación y código BIP.
- Incorporar nuevas iniciativas cumpliendo requisitos de glosas.
- Para nuevas transferencias a privados: acreditar selección por concurso o causal de excepción y personalidad jurídica vigente.
- Crear asignación para FRPD en ítem 33.03 y otras provisiones (FRIL, 8% FNDR).
#### Req Acuerdo CORE
- Voluntad del CORE debe ser clara en conceptos y montos y certificada por Secretario Ejecutivo.
#### Rol CORE en Aprobacion
#### ID
GORE-FIN-APROB-ROL-CORE-01
#### Act
Propuesta de distribución se somete al CORE para aprobación, modificación o sustitución (Art. 25 LOC GORE).
#### Dln
10 días corridos para pronunciarse.
#### Fnd
Dictamen E548580/2024 CGR: decisiones informadas, razonadas y alineadas con intereses regionales.
#### Proc Exposicion
- DIPIR expone presupuesto de inversiones.
- DAF expone presupuesto de funcionamiento.
- Ambas divisiones responden consultas y ajustan propuesta si corresponde.
#### Tramite DIPRES y CGR
#### ID
GORE-FIN-APROB-TRAM-DIPRES-01
#### Act
Gobernador remite distribución aprobada a DIPRES.
#### Dln
5 días desde aprobación CORE.
#### Resp
DAF prepara oficio conductor y antecedentes.
#### Req Documentos
- Oficio firmado por Gobernador titular o subrogante con acto de delegación.
- Contacto formal.
- Acuerdo CORE certificado.
#### Act DIPRES
- Revisar y elaborar resoluciones de presupuesto inicial (10 días).
- Subsanar errores materiales y reclasificar ingresos y gastos informando a GORE y CGR.
#### ID Resolucion CGR
#### ID
GORE-FIN-APROB-TRAM-CGR-01
#### Act
DIPRES remite resoluciones a CGR para Toma de Razón.
#### Nat
Control previo obligatorio de legalidad.
#### Dln
15 días (prorrogable por 15).
#### Ctx
- CGR verifica clasificación presupuestaria, cumplimiento de glosas, conformidad normativa y coincidencia GORE-CORE-DIPRES.
- Toma de Razón deja acto vigente; Representa rechaza por ilegalidad o formula alcances.
#### Res
DAF carga presupuesto en SIGFE (GORE-FIN-HERRAM-SIGFE-01).
### Ejecucion
#### Programacion Ejecucion y Caja
#### ID
GORE-FIN-EJEC-PROGRAMACION-01
#### Asunto
Programación de ejecución y de caja.
#### Src
Instructivo DIPRES Ejecución Presupuestaria (vigente).
#### Cpt
- DIPRES elabora programa de ejecución inicial mensualizado; GORE propone su programa.
- GORE remite actualizaciones mensuales a más tardar el día 15, detallando aporte fiscal y fuentes.
- Programa de Caja Mensual se basa en ejecución programada menos saldos disponibles para calcular necesidades de aporte fiscal y evitar recursos ociosos.
#### Ref
- GN-PPTO-GLOS-GORE
- GN-PPTO-GLOS-DIPRES
#### Rol DAF en Ejecucion
#### ID
GORE-FIN-EJEC-ROL-DAF-01
#### Resp
DAF lidera administración financiera diaria.
#### Cpt Gestion Financiera
- Garantizar gasto dentro de montos y clasificaciones autorizadas.
- Registrar preafectación, compromiso, devengo y pago en SIGFE.
- Supervisar programación de caja con DIPRES.
#### Cpt Pagos y Contabilidad
- Tramitar órdenes de compra, afectar gastos y realizar pagos (obligatoriamente vía transferencia electrónica, Art. 08 Ley 21.796).
- Cumplir normativa de compras públicas y rendición de cuentas.
- Elaborar informes financieros periódicos para DIPRES.
- Identificar mensualmente iniciativas de inversión (Subt. 31) por código BIP.
#### Cpt Control Interno
- Resguardar respaldo legal de cada desembolso.
- Asegurar respeto al destino de fondos según glosas.
- Certificar disponibilidad presupuestaria y límites legales con coordinación de Unidad de Control.
#### Ref
- GN-PPTO-GLOS-DAF
- GN-PPTO-GLOS-SIGFE
- GN-PPTO-GLOS-DIPRES
#### Rol DIPIR en Ejecucion
#### ID
GORE-FIN-EJEC-ROL-DIPIR-01
#### Resp
DIPIR lidera seguimiento físico y presupuestario de la inversión.
#### Cpt Monitoreo Proyectos
- Revisar avance físico de obras e iniciativas (Subt. 31 y 33).
- Detectar atrasos o desviaciones y proponer acciones correctivas.
- Evaluar cumplimiento de hitos de convenios (trimestral) y preparar informes para instancias externas.
#### Cpt Coord Externa
- Articular con SEREMI, servicios públicos sectoriales y municipios beneficiarios.
#### Cpt Uso Herramientas
- Actualizar estados en BIP y cargar ejecución físico-financiera (primeros 8 días del mes siguiente).
- Verificar vigencia técnica (RS) y usar SIGFE para seguimiento financiero.
- Referencias: GORE-FIN-HERRAM-BIP-01, GORE-FIN-HERRAM-SIGFE-01.
#### Ref
- GN-PPTO-GLOS-DIPIR
- GN-PPTO-GLOS-BIP
- GN-PPTO-GLOS-SIGFE
- GN-PPTO-GLOS-SNI
#### Regla Devengo Por Tipo Transferencia
#### ID
GORE-FIN-EJEC-DEVENGO-01
#### Asunto
Reglas de devengo diferenciadas según tipo de transferencia.
#### Src
Minuta CGR-AGORECHI-DIPRES marzo 2025; Dictamen CGR N°E583841/2024.
#### Fnd
Momento del devengo varía según receptor y modalidad; impacta metas de ejecución.
#### Casos
- Transferencias extrapresupuestarias (Subt. 24-03, 33-03) a instituciones de la Ley de Presupuestos: devengo al aprobarse la rendición (no al transferir).
- Transferencias presupuestarias consolidables o a municipios (Subt. 24-02, 33-02; 24-03, 33-03): regla general, devengo cuando la obligación es exigible (acto o convenio tramitado).
- Transferencias a entidades privadas (Subt. 24-01, 33-01): devengo cuando la obligación es exigible conforme al convenio/acto.
#### Ref
- GN-PPTO-GLOS-CGR
#### Coordinacion DAF DIPIR
#### ID
GORE-FIN-EJEC-COORDINACION-01
#### Fnd
Comunicación constante DAF-DIPIR es esencial para gestionar modificaciones y ejecución.
#### Ejemplos
- DIPIR informa a DAF proyectos retrasados para evaluar modificación presupuestaria.
- DAF alerta a DIPIR sobre partidas en agotamiento o riesgo de sobregiro.
### Modificaciones Presupuestarias
#### Motivaciones y Plazos
#### ID
GORE-FIN-MOD-INICIATIVA-01
#### Cause
Reubicar recursos, incorporar nuevos ingresos, ajustar costos o financiar imprevistos.
#### Dln
Solicitudes a DIPRES hasta 31 de octubre del año (según Instructivo DIPRES de ejecución).
#### Resp
- DIPIR lidera modificaciones de inversión (reasignar fondos de proyectos retrasados, usar ingresos adicionales).
- DAF lidera modificaciones de funcionamiento (suplementar partidas, incorporar Saldo Inicial de Caja).
#### Warn
Evitar solicitudes para regularizar hechos consumados, salvo excedibilidades legales.
#### Tipos de Modificacion y Actos
#### ID
GORE-FIN-MOD-TIPOS-ACTOS-01
#### Asunto
Tipología de modificaciones y actos administrativos requeridos.
#### Src
Oficio Circular N°11 DIPRES 2025 (última versión disponible en corpus).
#### Fnd
Naturaleza del acto depende si afecta presupuesto de la Partida 31 o solo el presupuesto interno del GORE.
#### Tipos
- Suplemento Presupuestario: aumenta presupuesto por mayor aporte fiscal; requiere Decreto Supremo DIPRES + Resolución GORE.
- Incorporación/Reducción de Ingresos Ley: distribución de fondos concursables o de contingencia; requiere Decreto Supremo DIPRES + Resolución GORE.
- Reasignación Presupuestaria Interna: movimientos entre subtítulos dentro del presupuesto del GORE; solo Resolución GORE.
- Transferencias a otros organismos (consolidable): reasignación desde FNDR en beneficio de un ministerio; Decreto Supremo DIPRES + Resolución GORE.
- Financiamiento de emergencias (3%): uso fondo de emergencia; Decreto Supremo DIPRES + Resolución GORE.
- Creación de iniciativas FRPD: uso de provisión en ítem 33.03; solo Resolución GORE.
- Incorporación Deuda Flotante: si se financia con SIC basta Resolución GORE; si requiere mayor aporte fiscal, se suma Decreto DIPRES.
#### Aprobacion Interna y Excepciones
#### ID
GORE-FIN-MOD-APROB-INTERNA-01
#### Req
Modificaciones que alteran presupuesto de inversión requieren acuerdo CORE, salvo excepciones explícitas.
#### Cpt
Glosa 01 y otros marcos definen casos sin acuerdo CORE (GORE-FIN-MOD-EXCEPCIONES-01).
#### Resp
- DIPIR prepara propuesta técnica de modificación para CORE.
- DAF provee respaldo financiero.
#### Tramite Externo DIPRES CGR
#### ID
GORE-FIN-MOD-TRAM-EXTERNA-01
#### Act
GORE emite resolución de modificación firmada por Gobernador y sujeta a visación DIPRES y Toma de Razón CGR.
#### Proc
- Visación DIPRES: verifica cumplimiento normativo y devuelve si hay errores.
- Toma de Razón CGR: revisa fundamento legal.
- Post-TDR: DAF ajusta presupuesto en SIGFE y DIPIR notifica a unidades ejecutoras.
#### Documentos Requeridos
#### ID
GORE-FIN-MOD-DOCS-REQUERIDOS-01
#### Src
Oficio Circular N°11 DIPRES 2025 (última versión disponible en corpus).
#### Cpt
- Certificado de acuerdo CORE cuando aplica.
- Minuta explicativa (justificación, origen/destino fondos, glosa habilitante).
- Informe favorable MDSF/DIPRES si financia programas directos nuevos.
- Otros documentos de respaldo (certificados de disponibilidad, convenios, etc.).
#### Excepciones sin Acuerdo CORE
#### ID
GORE-FIN-MOD-EXCEPCIONES-01
#### Asunto
Casos de modificaciones de inversión sin acuerdo CORE.
#### Src
Glosa 01 Partida 31 Ley 21.796; Oficio Circular N°11 DIPRES 2025 (última versión disponible en corpus).
#### Cpt Casos
- Aplicación de leyes generales (reajustes, sentencias, deuda flotante).
- Regularización de ingresos sin incidencia en gastos.
- Variaciones de tipo de cambio en activos no financieros.
- Uso del 3% para emergencias (Glosa 14).
- Aumento de costo de proyectos en ejecución hasta 10% del monto RS (tope 7.000 UTM).
- Adjudicación de licitaciones con variación hasta 10% sobre RS (tope 7.000 UTM).
#### Detalle Emergencias Glosa14 2026
#### ID
GORE-FIN-MOD-EMERG-GLO14-01
#### Fnd
Glosa 14 Partida 31 (GN-LEY-PPTO-2026-P31-GLO-14).
#### Cpt
- Se podrá traspasar hasta un 3% del presupuesto de inversión aprobado por el Congreso Nacional de cada GORE, a requerimiento de la Subsecretaría del Interior, a asignaciones 24.03.002 y/o 33.03.001 del presupuesto de dicha Subsecretaría para enfrentar situaciones de emergencia.
- Los GORE podrán destinar hasta un 2% del presupuesto de Inversión Regional aprobado por el Congreso Nacional para enfrentar situaciones de emergencia (todas sus etapas), definidas mediante resolución por el Ministro o Subsecretario del Interior, previa coordinación.
- La ejecución de estos recursos se podrá efectuar sin esperar la total tramitación del acto administrativo del GORE.
- Trimestralmente, los GORE informarán a la Comisión Especial Mixta de Presupuestos y a DIPRES sobre el uso de estos recursos.
#### Warn
Aunque no requieran CORE, sí exigen visación DIPRES, Toma de Razón CGR e información mensual al CORE.
#### Sintesis Roles en Modificaciones
#### ID
GORE-FIN-MOD-ROLES-SINTESIS-01
#### Resp
- DIPIR lidera modificaciones de inversión (racionalidad técnico-programática).
- DAF lidera modificaciones de funcionamiento (racionalidad financiero-legal).
#### Cpt
- Trabajo conjunto: DIPIR provee detalle de proyectos, DAF estructura modificación formal.
#### Warn
Antes de enviar, verificar que la modificación no vulnere normas (ej. prohibición de traspasar desde inversión a Subtítulo 22).
#### Limites y Flexibilidades TrasPasos
#### ID
GORE-FIN-MOD-LIMITES-01
#### Fnd
Fondos de inversión no deben utilizarse para financiar gastos corrientes de funcionamiento salvo habilitación legal expresa.
#### Src
DL N°1.263, Art. 04 Ley 21.796.
#### Reglas Claves Glosas
#### ID
GORE-FIN-MOD-LIMITES-GLOSAS-01
#### Cpt
- Glosa 03: prohíbe usar inversión para préstamos, gasto en personal o bienes y servicios de consumo de entidades receptoras.
- Glosa 04: permite traspasos entre subtítulos de inversión, excluyendo explícitamente al Subtítulo 22 como receptor.
- Glosa 01 de Ley de Reajuste: habilita excepcionalmente uso de fondos de inversión para gasto en personal cuando otra ley lo mande.
- Glosa 06: permite usar hasta 5% del monto del programa para gastos de administración del GORE (Subt. 21, 22, 29) y hasta 5% para honorarios de la entidad receptora.
- Art. 07 Ley 21.796: refuerza necesidad de habilitación legal expresa para financiar gastos operativos con recursos de transferencia.
#### Limites Incremento Gastos 2026
#### ID
GORE-FIN-MOD-LIMITES-ART04-01
#### Fnd
Art. 04 Ley 21.796.
#### Req Gastos Corrientes
- Se requiere autorización legal para incrementar la suma del valor neto de los gastos corrientes.
#### Excepciones Gastos Corrientes
- Ítems legalmente excedibles (art. 28 DL N°1.263/1975).
- Glosa 01 Programa Operaciones Complementarias.
- Mayores saldos iniciales de caja (excepto Partida Tesoro Público).
- Venta de activos financieros.
- Ingresos propios asignables.
- Recursos de fondos concursables de entes públicos.
- Art. 21 DL N°1.263/1975.
#### Req Gastos Capital
- Se requiere autorización legal para aumentar en más de 10% la suma aprobada en el Art. 1 de la Ley de Presupuestos para gastos de capital.
#### Excepciones Gastos Capital
- Reasignaciones presupuestarias desde gastos corrientes.
- Mayores saldos iniciales de caja (excepto Partida Tesoro Público).
- Venta de activos.
- Fondos concursables.
- Recuperación de anticipos.
#### Transferencias Consolidables
#### ID
GORE-FIN-MOD-CONSOL-01
#### Def
Transferencias desde un GORE a otras instituciones del Presupuesto del Sector Público para evitar doble contabilización del gasto.
#### Fnd
Oficio Circular N°11 DIPRES 2025 (última versión disponible en corpus), Glosa 01 Partida 31, Art. 26 Ley 21.796.
#### Proc
- GORE solicita formalmente a DIPRES la creación de la transferencia.
- GORE emite resolución interna con rebaja presupuestaria.
- Adjunta acuerdo CORE, justificación y aceptación del receptor.
- DIPRES elabora Decreto Supremo que modifica presupuesto GORE; pasa a CGR para Toma de Razón.
- Transferencias pueden efectuarse sin convenio formal si se cumple procedimiento presupuestario.
#### Ejemplo
#### ID
GORE-FIN-MOD-CONSOL-EJEMPLO-01
#### Asunto
Ejemplo de flujo para transferencia consolidable desde GORE X al Ministerio de Salud.
#### Ctx
- CORE aprueba; GORE envía oficio a DIPRES; emite resolución de rebaja. DIPRES emite Decreto que crea asignación y reasigna fondos, ajustando tanto presupuesto GORE como del ministerio.
### Control y Seguimiento
#### Control Interno GORE
#### ID
GORE-FIN-CONTROL-INTERNO-01
#### Resp
Unidad de Control o auditoría interna del GORE.
#### Act
- Revisar actos administrativos de contenido financiero (control ex-ante).
- Visar resoluciones, verificar respaldos y revisar rendiciones.
#### Req
DAF colabora para subsanar observaciones.
#### Control CGR
#### ID
GORE-FIN-CONTROL-LEGALIDAD-CGR-01
#### Resp
Contraloría General de la República (CGR).
#### Cpt
- Control previo vía Toma de Razón de resoluciones y decretos presupuestarios.
- Control posterior mediante auditorías e investigaciones especiales.
#### Req
DIPIR y DAF deben mantener antecedentes ordenados para fiscalizaciones.
#### Seguimiento DIPRES
#### ID
GORE-FIN-CONTROL-SEGUIMIENTO-DIPRES-01
#### Resp
Dirección de Presupuestos (DIPRES).
#### Act
- Monitorea ejecución presupuestaria mensual de los GORE mediante informes, reuniones y alertas de baja ejecución.
#### Req
GORE debe gestionar un calendario de hitos para asegurar cumplimiento.
#### Transparencia y Control Social
#### ID
GORE-FIN-CONTROL-TRANSPARENCIA-01
#### Nat
Control social sobre inversión regional.
#### Fnd
Ley N° 21.796 (Normas Generales) + Requerimientos de información Partida 31 (ver INFO-REQS-2026-GORES-01 en artefacto glosas GORES 2026).
#### Req
- Publicar mensualmente en sitio web del GORE la cartera de proyectos financiados con inversión regional.
- Publicar acuerdos del CORE en máximo 5 días hábiles.
- Informar trimestralmente el uso de recursos de inversión regional: listado de beneficiarios, comuna, instituciones receptoras, monto, productos del convenio y su aplicación a nivel regional.
- Informar y publicar trimestralmente el destino de recursos FNDR a proyectos de desarrollo económico y los proyectos adjudicados por sectores según actividad económica.
- Publicar trimestralmente e informar a senadores y diputados de la región todos los proyectos adjudicados o contratados con cargo a Subt. 24 (oferta programática) y Subt. 31 y 33, incluyendo nombre del proyecto, monto estimado, postulantes, pauta de evaluación, seleccionado, presupuesto aprobado y votación del CORE.
- Informar trimestralmente transferencias con cargo al Fondo de Vinculación con la Comunidad (8%): beneficiario, comuna, objeto del financiamiento, montos totales y fecha de cada transferencia.
- Informar trimestralmente iniciativas y proyectos de inversión que superen 500 UTM: proyecto, antecedentes para aprobación, montos, plazo de ejecución e identidad del receptor de recursos.
- Informar trimestralmente la disponibilidad presupuestaria para que universidades reconocidas por el Estado accedan a asignaciones directas de recursos FRPD y las solicitudes recibidas.
- Publicar acuerdos del CORE en máximo 5 días hábiles e información de corporaciones financiadas.
- Publicar información en formato digital legible y procesable, que no consista solamente en imágenes.
- Publicar en transparencia activa las actas de evaluación emitidas por comisiones evaluadoras de licitaciones y compras públicas (Ley N°19.886).
- Procurar lenguaje claro y vincular el presupuesto a orientaciones estratégicas, objetivos prioritarios y resultados esperados.
- Publicar de forma permanente en transparencia activa (literal k) art. 7 Ley N°20.285) los montos recibidos y ejecución presupuestaria del FRPD, incluyendo detalle de transferencias efectuadas.
#### Resp
DIPIR compila información, DAF valida cifras.
### Cierre Presupuestario
#### Compromisos y Cortes
#### ID
GORE-FIN-CIERRE-COMPROMISOS-01
#### Act
Definir fechas de corte para nuevos compromisos (usualmente diciembre) y comunicarlas.
#### Resp
- DAF comunica fechas límite.
- DIPIR verifica registro adecuado de compromisos.
#### Deuda Flotante
#### ID
GORE-FIN-CIERRE-DEUDA-FLOTANTE-01
#### Def
Obligaciones devengadas en el año pero pendientes de pago al 31 de diciembre.
#### Resp
DAF calcula, registra y tramita su incorporación en el presupuesto del año siguiente mediante creación del ítem 34.07 Deuda Flotante.
#### Fnd
Art. 34 Ley 21.796 permite exceder las sumas fijadas para este ítem.
#### Cpt
- Si el Saldo Inicial de Caja (SIC) supera la deuda flotante, se financia 100% con SIC (solo Resolución GORE).
- Si SIC es insuficiente, se usa todo el SIC y la diferencia con mayor aporte fiscal (Resolución GORE + Decreto DIPRES).
#### Warn
Priorizar pago de deuda flotante al inicio del nuevo ejercicio.
#### Evaluacion y Cierre Sistemas
#### ID
GORE-FIN-CIERRE-EVALUACION-01
#### Act
- DAF realiza ajustes contables, prepara Informe de Ejecución Anual y genera nuevo SIC.
- DIPIR evalúa ejecución física de proyectos, identifica logros, retrasos y cuellos de botella, retroalimentando la siguiente formulación.
#### ID Cierre Sistemas
#### ID
GORE-FIN-CIERRE-SISTEMAS-01
#### Act
DAF realiza cierre en SIGFE y DIPIR actualiza estado final en BIP.

## Gestion Subtitulos Presupuestarios
### ID
GORE-FIN-SUBTITULOS-01
### Introduccion
#### ID
GORE-FIN-SUB-INTRO-01
#### Purp
Describir subtítulos clave, su contenido y consideraciones operativas para la gestión regional.
#### Src
Chileindica y Ley de Presupuestos 2026.
#### Ctx
Subtítulos clave: 21, 22, 23, 24, 26, 29, 31, 33, 34.
### Ref
- GN-PPTO-GLOS-FNDR
- GN-PPTO-GLOS-FRIL
- GN-PPTO-GLOS-FRPD
### Subtitulo 21 Gastos en Personal
#### ID
GORE-FIN-SUB-21-PERS-01
#### Contenido
#### ID
GORE-FIN-SUB-21-CONTENIDO-01
#### Cpt
Remuneraciones y obligaciones del empleador del personal del GORE.
#### Resp
DAF.
#### Act
Asegurar que pagos respeten dotaciones, topes de glosas y normativa.
#### Ctx Flexibilidad 2026
- Glosa 01 Partida 31: sin límite de antigüedad para contratas; contratas pueden ejercer funciones directivas (hasta 20%); honorarios pueden actuar como agente público.
- Art. 05 Ley 21.796: suspensión de compatibilidad de cargo de planta con contrata.
#### Items Relevantes
#### ID
GORE-FIN-SUB-21-ITEMS-RELEVANTES-01
#### Asunto
Ítems del Subtítulo 21 relevantes para inversión regional.
#### Src
Documentos curados presupuesto/Chileindica.
#### Cpt
- Ítem 03 Otras Remuneraciones / Asignación 001 Honorarios a Suma Alzada: permite contratar profesionales para asesoría o ejecución en programas de inversión, clave para programas directos (Glosa 06).
### Subtitulo 22 Bienes y Servicios
#### ID
GORE-FIN-SUB-22-BS-01
#### Contenido
#### ID
GORE-FIN-SUB-22-CONTENIDO-01
#### Cpt
Gastos operativos (insumos, servicios básicos, arriendos, pasajes).
#### Resp
DAF.
#### Act
Gestionar adquisiciones vía Ley de Compras y buscar eficiencia.
#### Prohib
Prohibido reasignar recursos de inversión hacia Subtítulo 22 (Glosa 04 Partida 31).
#### Fnd
Incremento de Subtítulo 22 solo con ingresos propios o SIC.
#### Ctx
DIPIR interviene solo cuando programas directos (Glosa 06) destinan parte de su 5% a este subtítulo.
#### Items Relevantes
#### ID
GORE-FIN-SUB-22-ITEMS-RELEVANTES-01
#### Asunto
Ítems del Subtítulo 22 relevantes para la inversión regional.
#### Cpt
- Ítem 08 Servicios Generales / Asignación 007 Pasajes, Fletes y Bodegajes: algunos gastos de consumo se informan como inversión pública regional en Chileindica.
### Subtitulo 23 Prestaciones Seguridad Social
#### ID
GORE-FIN-SUB-23-PRESTSEC-01
#### Contenido
#### ID
GORE-FIN-SUB-23-CONTENIDO-01
#### Cpt
Gastos por prestaciones previsionales y de asistencia social; uso en GORE generalmente bajo.
#### Resp
DAF.
### Subtitulo 24 Transferencias Corrientes
#### ID
GORE-FIN-SUB-24-TRANSFCORR-01
#### Contenido
#### ID
GORE-FIN-SUB-24-CONTENIDO-01
#### Cpt
Recursos transferidos sin contraprestación directa para gastos corrientes de otras instituciones (funcionamiento e inversión asociados).
#### Nat
Doble componente (funcionamiento e inversión).
#### Fnd
Transferencias a privados deben ser por concurso público y convenio (Art. 23-27 Ley 21.796).
#### Reglas Transferencias Privados 2026
#### ID
GORE-FIN-SUB-24-PRIVADOS-ART23-27-01
#### Fnd
Art. 23-27 Ley 21.796.
#### Req General
- Transferencias corrientes y de capital a instituciones privadas deben ser resultado de concurso público abierto y transparente y materializarse mediante convenio.
- La asignación directa sin concurso procede sólo de forma excepcional y debe acreditarse mediante resolución fundada.
#### Causales Asignacion Directa Sin Concurso
- En concursos respectivos no se presentaron interesados.
- Sólo existe una persona jurídica como posible beneficiario o ejecutor.
- Emergencia, urgencia o imprevisto debidamente calificados.
#### Convenios Obligaciones y Prohibiciones
- El convenio debe indicar objeto social/fines del receptor y acreditar su pertinencia previamente a la suscripción.
- El convenio debe indicar actividades específicas y/o conceptos de gasto a financiar.
- No puede establecer compromisos financieros que excedan el ejercicio presupuestario sin autorización previa DIPRES.
- Debe condicionar la suscripción al cumplimiento íntegro de la Ley N°19.862.
- Rendiciones de cuentas deben realizarse vía Sistema de Rendición Electrónica de Cuentas (SISREC) CGR, según instrucciones CGR.
- Salvo plazo distinto en convenio, el organismo público tiene plazo máximo de 3 meses para pronunciarse fundadamente sobre la rendición.
- Debe exigir restitución si recursos se destinan a finalidad distinta, no se utilizan, no se rinden o son observados.
#### Reglas Ejecutoras Politica Publica
- Para instituciones privadas ejecutoras de políticas públicas: exigir al menos 2 años de antigüedad y experiencia acreditada.
- Exigir garantías cuando el total de recursos a transferir supere 1.000 UTM; garantía equivalente al 5% del monto total.
#### Inhabilidades Concursos y Convenios
- No podrán intervenir en procesos concursal/adjudicación/suscripción quienes tengan parentesco (hasta 4° consanguinidad/3° afinidad) con directivos o ejecutivos de institución participante.
- No podrán intervenir quienes hayan trabajado o desempeñado labores directivas en institución participante en los 2 años anteriores al cargo público.
- Debe dejarse constancia en actas de la nómina de funcionarias/os y personal a honorarios que intervino en el proceso.
#### Restituciones y Reintegros
- Los organismos públicos receptores que deban reintegrar recursos a rentas generales deben hacerlo a más tardar dentro del mes siguiente al cierre de la rendición.
- El proceso de rendición no podrá extenderse por más de 6 meses desde la finalización de la ejecución del convenio.
#### Items
#### ID
GORE-FIN-SUB-24-ITEMS-01
#### Cpt
- Ítem 01 Al Sector Privado.
- Ítem 03 A Otras Entidades Públicas.
- Ítem 04 A Empresas Públicas no Financieras.
- Ítem 05 A Empresas Públicas Financieras.
- Ítem 08 A Instituciones Privadas Ejecutoras de Políticas Públicas.
- Ítem 09 A Unidades o Programas del Servicio.
#### Transferencias Item09 Unidades Programas Servicio 2026
#### ID
GORE-FIN-SUB-24-ITEM09-ART07-01
#### Fnd
Art. 07 Ley 21.796.
#### Cond
Transferencias corrientes a Unidades o Programas del Servicio, ejecutados total o parcialmente por éste.
#### Req
- Desglose previo a la ejecución presupuestaria en conceptos de gasto, según visación DIPRES.
- Reporte mensual a DIPRES: avance de actividades e información de ejecución presupuestaria.
#### Res
- El desglose constituye autorización máxima de gasto por concepto; modificaciones por igual procedimiento.
- Personal contratado con cargo a dichos recursos no forma parte de la dotación del Servicio.
#### Prohib
- No incluir recursos para gastos en personal ni bienes y servicios de consumo, salvo autorización por norma expresa en el respectivo presupuesto.
#### Concurso 8pct FNDR
#### ID
GORE-FIN-SUB-24-CONCURSO-8FNDR-01
#### Asunto
Concurso de Vinculación con la Comunidad 8% FNDR.
#### Src
Glosa 07 Partida 31 Ley 21.796.
#### Cond
- Límite hasta 8% del total del presupuesto de inversión regional; mínimo 1% a cultura y patrimonio.
- Concursos exentos de evaluación ex-ante Glosa 06.
- Se podrá asignar hasta un 10% de los recursos del Concurso 8% para asignaciones directas asociadas con casos emblemáticos, excepcionales y emergentes, previo acuerdo del CORE y sujeto a la Resolución N°72 de 08.01.2025 DIPRES y sus modificaciones.
#### Ctx
- Actividades financiables: deportivas y del programa Elige Vivir Sano.
- Actividades financiables: seguridad ciudadana.
- Actividades financiables: participación de niños, niñas, adolescentes y jóvenes (Ley N°21.302, art. 6 letra p)).
- Actividades financiables: carácter social (discapacidad con dependencia severa, prevención y rehabilitación de drogas).
- Actividades financiables: atención de adultos mayores e integración y promoción del envejecimiento activo.
- Actividades financiables: protección del medioambiente y educación ambiental.
- Actividades financiables: adopción, rescate, atención y tratamiento veterinario, y gestión de residuos de animales.
- Actividades financiables: funcionamiento de establecimientos de larga estadía para adultos mayores, residencias familiares para niños/niñas/adolescentes/jóvenes, y dispositivos del Servicio de Reinserción Social Juvenil.
- Actividades financiables: funcionamiento de teatros municipales o regionales y/o monumentos históricos con atención a público.
- Actividades financiables: culturales y patrimoniales.
- Ejecutores: municipalidades, otras entidades públicas, instituciones privadas sin fines de lucro, organizaciones de la sociedad civil y organizaciones comunitarias sin fines de lucro.
#### Proc
- DIPIR elabora bases (aprueba CORE).
- Comisiones evalúan.
- CORE aprueba adjudicados.
- DAF formaliza y fiscaliza transferencias.
#### Programas y Transferencias Publicas
#### ID
GORE-FIN-SUB-24-PROGRAMAS-01
#### Asunto
Transferencias corrientes a entidades públicas y ejecución directa de programas.
#### Fnd
Glosa 06 Partida 31 Ley 21.796.
#### Cond
- Programas nuevos de ejecución directa requieren evaluación ex-ante DIPRES/MDSF.
- Prohibido usar inversión para financiar gastos permanentes de otros servicios (Glosa 03).
- Receptor público puede usar hasta 5% para honorarios de gestión.
- Glosa 06 habilita financiar áreas fuera de competencias LOC GORE en casos específicos.
#### Reglas Oferta Programatica Glosa06 2026
#### ID
GORE-FIN-SUB-24-PROGDIR-GLO06-01
#### Fnd
Glosa 06 Partida 31 (GN-LEY-PPTO-2026-P31-GLO-06).
#### Excepciones Evaluacion ExAnte
- Programas que hayan iniciado su ejecución en años anteriores.
- Subvenciones asociadas al Concurso de Vinculación con la Comunidad 8%.
- Transferencias a universidades, municipalidades, otras entidades públicas y gobierno central e instituciones privadas beneficiarias sin fines de lucro.
- Ayudas tempranas e iniciativas de fomento productivo vinculadas a emergencias y desastres naturales, en coordinación con el Ministerio del Interior.
#### Principios
- Coherencia con políticas públicas nacionales, coordinación, unidad de acción, eficiencia y eficacia.
- Evitar duplicidad o interferencia de funciones con otros órganos de la Administración del Estado.
#### Regla 5pct Administracion GORE
- Se podrá destinar hasta un 5% del monto total de la transferencia a gastos de administración en el GORE (personal, bienes y servicios de consumo y adquisición de activos no financieros) asociados a la ejecución del programa.
- El personal contratado a honorarios con cargo al 5% tendrá la calidad de agente público.
#### Regla 5pct Honorarios Receptor Publico
- En la entidad pública receptora se podrá contratar personal a honorarios con cargo a la transferencia; vínculo cesará de pleno derecho al finalizar el convenio.
- No podrá ser superior al 5% del total de la transferencia recibida.
#### Ambitos Adicionales Permitidos
- Emergencia: prevención/mitigación incendios forestales; labores preventivas por eventos climatológicos; gestión del riesgo de desastres (Ley N°21.364) y continuidad de servicios APR; sanitización y calefacción ante catástrofes; ayudas tempranas y reconstrucción (coordinación Subsecretaría del Interior); demolición de infraestructura en mal estado (certificada por municipalidad).
- Seguridad Pública: iniciativas de prevención y seguridad ciudadana.
- Salud: planes de resolución de lista de espera (coordinación MINSAL); cuidados de discapacidad en centros regionales de rehabilitación (instituciones privadas ejecutoras).
- Cuidados: adultos mayores (SENAMA), condominios tutelados, ELEAM, auxilio extraordinario a personas en situación de calle (MDSF), distribución medicamentos a domicilio (Servicio de Salud).
- Cambio Climático y Gestión de Residuos: protección ambiental/educación ambiental; mantención de parques/áreas verdes/jardines botánicos; operación tratamiento residuos/reciclaje/valorización; subsidios a municipalidades para disposición final residuos; gestión de residuos de animales.
- Energía, Transporte y Telecomunicaciones: autogeneración de energía; conectividad internet y radiocomunicaciones; subsidios Ley N°20.378; transporte escolar rural.
- Gestión Hídrica: funcionamiento/mantención/reparación sistemas APR y sanitarios rurales y/o desalinización; operación alcantarillado.
- Asistencia Técnica: asistencia técnica a municipalidades para fortalecer cartera de proyectos.
#### Ref
- GN-PPTO-GLOS-FNDR
- GN-PPTO-GLOS-FRIL
- GN-PPTO-GLOS-DIPRES
- GN-PPTO-GLOS-MDSF
### Subtitulo 26 Otros Gastos Corrientes
#### ID
GORE-FIN-SUB-26-OTROSCORR-01
#### Contenido
#### ID
GORE-FIN-SUB-26-CONTENIDO-01
#### Cpt
Devoluciones y compensaciones por daños a terceros (uso bajo pero posible).
#### Items
- Ítem 01 Devoluciones.
- Ítem 02 Compensaciones por Daños.
#### Resp
DAF.
### Subtitulo 29 Activos No Financieros
#### ID
GORE-FIN-SUB-29-ACTIVOS-01
#### Contenido
#### ID
GORE-FIN-SUB-29-CONTENIDO-01
#### Cpt
Adquisición de bienes de capital del GORE (equipos, vehículos, terrenos).
#### Purp
Financiar reposición de activos para otras instituciones públicas (Glosa 09 Partida 31).
#### Cond
- Activos nuevos requieren certificado de disponibilidad presupuestaria para los gastos recurrentes que generen dichos activos.
- El certificado debe ser emitido por el Ministerio o la Subsecretaría respectiva.
- Para Fuerzas de Orden y Seguridad Pública: certificado de pertinencia emitido por el Ministerio de Seguridad Pública.
- Para Cuerpos de Bomberos: certificado de pertinencia técnica emitido por la Junta Nacional de Bomberos de Chile.
- Compra de terrenos: coordinar con SERVIU de la región respectiva, cuando corresponda.
#### Resp
DIPIR identifica necesidades; DAF ejecuta adquisición.
#### Items
#### ID
GORE-FIN-SUB-29-ITEMS-01
#### Cpt
- Ítem 01 Terrenos.
- Ítem 02 Edificios.
- Ítem 03 Vehículos.
- Ítem 04 Mobiliario y Otros.
- Ítem 05 Máquinas y Equipos.
- Ítem 06 Equipos Informáticos.
- Ítem 07 Programas Informáticos.
- Ítem 99 Otros Activos no Financieros.
### Subtitulo 31 Iniciativas Inversion Directa
#### ID
GORE-FIN-SUB-31-INVDIR-01
#### Contenido
#### ID
GORE-FIN-SUB-31-CONTENIDO-01
#### Cpt
Inversión real ejecutada directamente por el GORE (unidad mandante).
#### Fnd
Glosa 10 Partida 31.
#### Req
- Respetar competencias GORE y someterse al SNI.
- Licitación pública obligatoria si proyectos/programas de inversión superan 1.000 UTM (Art. 06 Ley 21.796).
- Licitación pública obligatoria si estudios básicos superan 500 UTM (Art. 06 Ley 21.796).
- Identificaciones presupuestarias de iniciativas contratadas en años anteriores en ejecución y aquellas creadas en el mismo año no requerirán nueva aprobación del CORE si los montos totales o resultantes son iguales o menores al 10% de los costos totales ya aprobados por el Consejo Regional, reajustados a la moneda del año en curso.
#### Alcances Glosa10 2026
#### ID
GORE-FIN-SUB-31-GLO10-ALCANCE-01
#### Fnd
Glosa 10 Partida 31 (GN-LEY-PPTO-2026-P31-GLO-10).
#### Cpt
- Iniciativas adicionales permitidas: infraestructura pública (construcción, conservación y mejoramiento) en coordinación con ministerio sectorial.
- Iniciativas adicionales permitidas: transporte (coordinación MTT) en marco Ley N°20.378.
- Iniciativas adicionales permitidas: electrificación, gas, energía, conectividad digital, telefonía celular y comunicaciones (incluye conexiones domiciliarias).
- Iniciativas adicionales permitidas: agua potable y alcantarillado; proyectos sanitarios en áreas de concesión de empresas del sector público; APR y mitigación/reparación por cambio climático (pequeños productores y habitantes rurales).
- Regla especial 2026: saneamiento rural o proyectos en territorios insulares (SSR) pueden definir como Unidad Técnica a empresa pública o privada que opere en la región, mediante resolución fundada.
- DOH y Subdirección de Servicios Sanitarios Rurales informan a Gobiernos Regionales y Contraloría Regional regiones sin especialistas (20 enero y 30 junio).
- Huellas y caminos vecinales privados de uso público: administración directa/contrato/compra servicio; requiere compromiso formal de transferencia de faja y visto bueno Dirección Regional de Vialidad.
- Personal a honorarios para ejecución de proyectos tendrá calidad de agente público.
#### Proc
GORE actúa como unidad mandante; DAF gestiona licitación y contratación.
#### Items
#### ID
GORE-FIN-SUB-31-ITEMS-01
#### Cpt
- Ítem 01 Estudios Básicos.
- Ítem 02 Proyectos (estudios preinversionales y ejecución).
- Ítem 03 Programas de Inversión.
### Subtitulo 33 Transferencias Capital
#### ID
GORE-FIN-SUB-33-TRANSFCAP-01
#### Contenido
#### ID
GORE-FIN-SUB-33-CONTENIDO-01
#### Cpt
Transferencia de recursos a terceros para ejecutar proyectos de inversión; subtítulo de mayor peso.
#### Resp
Municipalidades, servicios públicos, corporaciones, etc.
#### Fnd
Glosa 11 Partida 31 y normativa complementaria.
#### Req
- Cada transferencia debe formalizarse en un convenio con definición de objeto, monto, plazos, obligaciones, seguimiento y garantías.
#### Alcances Glosa11 2026
#### ID
GORE-FIN-SUB-33-GLO11-ALCANCE-01
#### Fnd
Glosa 11 Partida 31 (GN-LEY-PPTO-2026-P31-GLO-11).
#### Cpt
- Iniciativas adicionales permitidas: PMU/PMB en coordinación con SUBDERE.
- Iniciativas adicionales permitidas: infraestructura social/deportiva en inmuebles con calidades jurídicas específicas y en inmuebles fiscales en tuición de organizaciones privadas sin fines de lucro con fines sociales.
- Iniciativas adicionales permitidas: caminos comunitarios en territorios Ley N°19.253 o de comunidades agrícolas.
- Iniciativas adicionales permitidas: fachadas de inmuebles privados con protección patrimonial.
- Iniciativas adicionales permitidas: protección/puesta en valor de Monumentos Nacionales, Inmuebles de Conservación Histórica, zonas de conservación, UNESCO y Lista Tentativa (incluye ejecución con sector privado).
- Iniciativas adicionales permitidas: subsidios a empresas (públicas o privadas) para inversión social (electrificación, gas, energía, telefonía/comunicaciones), evaluadas como iniciativa de inversión por MDSF.
- APR/sanitarios rurales/desalinización: transferencia por resolución fundada del Gobernador Regional con efectos sin esperar total tramitación; requiere pronunciamiento técnico favorable Subdirección SSR.
- Transferencias a municipalidades y empresas sanitarias para monitoreo, mantenciones, diseño de soluciones y trabajos preventivos ante filtraciones de redes agua potable/alcantarillado; incluye pavimentación post recambio de redes; previa visación del órgano competente regional.
- Para proyectos de Construcción de Infraestructura Sanitaria financiados por GORE, rige límite de costo del art. 8° DS N°829/1998 del Ministerio del Interior y sus modificaciones.
#### Ref
- GN-PPTO-GLOS-FNDR
- GN-PPTO-GLOS-FRIL
- GN-PPTO-GLOS-FRPD
#### Items
#### ID
GORE-FIN-SUB-33-ITEMS-01
#### Cpt
- Ítem 01 Al Sector Privado.
- Ítem 03 A Otras Entidades Públicas (ítem principal de inversión GORE).
- Ítem 04 A Empresas Públicas no Financieras.
- Ítem 05 A Empresas Públicas Financieras.
- Ítem 06 A Gobiernos Extranjeros.
- Ítem 07 A Organismos Internacionales.
#### Casos Especiales
#### ID
GORE-FIN-SUB-33-CASOS-ESPECIALES-01
#### Cpt
- FRIL: fondo para proyectos municipales de menor escala; seguir Guía Operativa FRIL SUBDERE (Resolución Exenta N°15.051 de 29 de diciembre de 2023).
- FRIL: proyectos municipales con costo total por proyecto inferior a 5.000 UTM (valorizadas al 1 de enero del ejercicio presupuestario vigente) no requieren informe favorable MDSF; se debe ingresar al SNI la información necesaria según Oficio Ordinario N°2 de 26 de enero de 2024 e instructivo asociado.
- FRIL: GORE puede aprobar por resolución instructivos o bases (metodología distribución entre comunas, procedimientos de ejecución, entrega de recursos, rendición y otros).
- FRIL: una vez aprobados los montos por municipio, el compromiso de financiamiento debe informarse mediante oficio dirigido al municipio respectivo.
- Emergencia hídrica: permite transferir a municipios y sanitarias para reparar redes de agua con visación de órgano técnico competente.
#### Roles
#### ID
GORE-FIN-SUB-33-ROLES-01
#### Resp
- DIPIR articula cartera de proyectos, coordina RS, prioriza y coordina convenios y seguimiento técnico.
- DAF elabora aspectos financieros de convenios, ejecuta transferencias y revisa rendiciones.
### Subtitulo 34 Servicio de Deuda
#### ID
GORE-FIN-SUB-34-DEUDA-01
#### Contenido
#### ID
GORE-FIN-SUB-34-CONTENIDO-01
#### Cpt
Pagos asociados principalmente a la Deuda Flotante del año anterior.
#### Prohib
GORE no puede endeudarse sin ley especial.
#### Purp
Registrar y pagar la Deuda Flotante; uso de Ítem 34.07.
#### Warn
Alto nivel de deuda flotante recurrente indica gestión deficiente.

## Glosas Relevantes y Fondos
### ID
GORE-FIN-GLOSAS-01
### Ref
- GN-PPTO-GLOS-FNDR
- GN-PPTO-GLOS-FRPD
### FNDR
#### ID
GORE-FIN-GLOSAS-FNDR-01
#### Asunto
Fondo Nacional de Desarrollo Regional.
#### Def
Principal fuente de financiamiento de inversión regional.
#### Ctx
- Distribución (referencial): 90% asignado por ley, 10% gestionado por SUBDERE/DIPRES.
- DIPIR programa cartera para ejecutar 90%; DAF vigila uso autorizado de giros.
#### Req
Ley de Presupuestos 2026 (Partida 31) establece requerimientos de información y publicación asociados a ejecución FNDR (ver INFO-REQS-2026-GORES-01).
### FRPD
#### ID
GORE-FIN-GLOSAS-FRPD-01
#### Asunto
Fondo Regional para la Productividad y el Desarrollo (FRPD).
#### Def
Fondo que reemplaza al FIC, orientado a innovación, competitividad, ciencia y tecnología.
#### Fnd
- Glosa 13 Partida 31 Ley 21.796.
- Art. 13 Ley 21.591 (Royalty Minero) y reglamento específico.
- Glosa 13 Partida 31 (GN-LEY-PPTO-2026-P31-GLO-13): Decreto N°1699 de 6 de diciembre de 2025 MH; Resolución Exenta N°33/2024 MinCiencia; Resolución Exenta N°08/2025 Subsecretaría de Economía y sus modificaciones.
#### Proc
- Crear provisión FRPD en Ítem 33.03 del presupuesto inicial.
- Reasignar durante el año a iniciativas específicas vía modificaciones presupuestarias.
#### Cpt
- Evita doble concursabilidad.
- Tipología Innovación y Competitividad (Res. Ex. N°33 Subdere 2024) exenta de evaluación ex-ante Glosa 06; otras tipologías se rigen por normativa general.
- Se podrán transferir directamente recursos a iniciativas seleccionadas mediante concurso convocado por CORFO o ANID, cuyas instituciones ejecutoras estén incluidas en Resolución Exenta N°33/2024 MinCiencia y sus modificaciones.
- Se podrán efectuar creaciones y modificaciones de asignaciones para el pago de compromisos de arrastre de iniciativas ejecutadas por instituciones elegibles del Fondo de Innovación y Competitividad.
- Se podrá participar del financiamiento de iniciativas de Programas de Desarrollo Productivo Sostenible (Ministerio de Economía) y del Programa de Financiamiento Estructural I+D+i Universitario (Ministerio de Ciencia).
- DIPIR gestiona fondo; DAF maneja provisión y control financiero.
### Equidad y Territorios Rezagados
#### ID
GORE-FIN-GLOSAS-EQUIDAD-01
#### Asunto
Fondos para corregir desigualdades territoriales.
#### Cpt
- Fondo de Equidad Interregional, integrado al programa de inversión.
- Planes de Zonas Extremas y Territorios Rezagados, financiados con programa especial de Asociatividad y Planes Especiales.
### Subvenciones 8pct
#### ID
GORE-FIN-GLOSAS-SUBV8-01
#### Asunto
Subvenciones concursables 8% FNDR.
#### Fnd
Glosa 07 Partida 31 Ley 21.796; vinculado a GORE-FIN-SUB-24-CONCURSO-8FNDR-01.
#### Req
- Proceso de asignación transparente mediante concursos.
- Rendición de cuentas vía SISREC CGR (Art. 24 Ley 21.796).
### Asociatividad Regional
#### ID
GORE-FIN-GLOSAS-ASOC-01
#### Asunto
Asociatividad regional y participación en personas jurídicas.
#### Mech
GORE puede participar en corporaciones y fundaciones.
#### Fnd
Art. 101 LOC GORE; programa especial de asociatividad; Glosa 08 Partida 31 Ley 21.796.
#### Cond
- Aporte máximo GORE: 5% del presupuesto de inversión.
- Aportes para funcionamiento son anuales; no proceden convenios plurianuales.
- Cofinanciamiento máximo 50% con recursos GORE.
- Aportes privados pueden ser no pecuniarios, valorizados en convenio.
#### Req
- Informar y publicar periódicamente sobre corporaciones financiadas.
- Al término del primer trimestre: informar a DIPRES y publicar en webs del GORE y corporación: razón social; misión/objetivos/productos; directorio; organigrama; instituciones que financian; vínculo con objetivos del GORE; planificación anual con resultados esperados.
- Trimestralmente (dentro de 30 días): número de profesionales, remuneración y perfil; concursos de contratación; recursos transferidos/ejecutados (período y acumulado); indicadores de gestión (avance físico y financiero de iniciativas).
- Dar cuenta pública anual; mantener estados financieros publicados; regirse por Ley N°20.285 en lo aplicable.
### Universidades Regionales
#### ID
GORE-FIN-GLOSAS-UNIV-01
#### Asunto
Transferencias a universidades regionales.
#### Fnd
Glosa 05 Partida 31 Ley 21.796.
#### Cpt
- Habilita transferencias a universidades del DFL N°4 de 1981 con casa central en la región.
- Fines deben estar dentro de competencia universitaria y sujetarse a reglas de concursabilidad cuando aplique.
- Ejecución y uso: sólo para fines dentro del ámbito de competencia del establecimiento adjudicatario.
- Ejecución preferente por universidades con sede en la región respectiva.
- Ejecución íntegra por la propia universidad.
- Estas transferencias se podrán exceptuar del mecanismo de concursabilidad establecido en el articulado de la ley.
### Region Nuble Programa 19 2026
#### ID
GORE-FIN-REG-NUB-PPTO-2026-01
#### Fnd
Glosas específicas Gobierno Regional Región de Ñuble (Programa 19) Partida 31 Ley 21.796: GN-LEY-PPTO-2026-P31-REG-NUB-PROG-19.
#### Funcionamiento Regional
#### ID
GORE-FIN-REG-NUB-FUNC-2026-01
#### Fnd
GN-LEY-PPTO-2026-P31-REG-NUB-PROG-19.
#### Cpt
- Dotación máxima de vehículos: 5 (GN-LEY-PPTO-2026-P31-REG-NUB-PROG-19-GLO-01).
- Gastos en personal: 4.222.003 miles (GN-LEY-PPTO-2026-P31-REG-NUB-PROG-19-GLO-02).
- Incluye dotación máxima de personal 101, horas extraordinarias (Miles de $9.928), viáticos territorio nacional (Miles de $19.802) y exterior (Miles de $17.100), convenios con personas naturales (N°3; Miles de $115.294), funciones críticas (N°2; Miles de $23.242) (GN-LEY-PPTO-2026-P31-REG-NUB-PROG-19-GLO-03).
- Monto máximo para gastos en el ítem de publicidad: 84.272 miles (GN-LEY-PPTO-2026-P31-REG-NUB-PROG-19-GLO-05).
#### Informes Especificos 2026
#### ID
GORE-FIN-REG-NUB-INF-2026-01
#### Cpt
- Informar trimestralmente a la Comisión Especial Mixta de Presupuestos sobre convenios y montos para compra y distribución de agua vía camiones aljibe u otros medios, comunas, población beneficiada y acciones para incentivar competencia (GN-LEY-PPTO-2026-P31-REG-NUB-PROG-19-GLO-06).
- Informar trimestralmente a Comisiones de Economía del Senado y de la Cámara sobre proyectos de inversión a implementarse en Ñuble y efecto en generación de empleo regional (GN-LEY-PPTO-2026-P31-REG-NUB-PROG-19-GLO-07).

## Control Externo y Documentacion
### ID
GORE-FIN-CONTROL-EXT-01
### Toma de Razon y Control CGR
#### ID
GORE-FIN-CTRL-TDR-01
#### Asunto
Toma de Razón y control de legalidad por CGR.
#### Cpt Hitos
- Resolución de presupuesto inicial.
- Resoluciones de modificaciones presupuestarias (previa visación DIPRES).
- Decretos Supremos.
- Convenios relevantes.
#### Rec
- Planificar tiempos, asegurar calidad documental y archivar actos tramitados para futuras revisiones.
#### Ref
- GN-PPTO-GLOS-CGR
### Documentacion DIPRES
#### ID
GORE-FIN-CTRL-DOC-DIPRES-01
#### Asunto
Preparación de antecedentes para DIPRES.
#### Cpt Reportes
- Programa de ejecución y caja mensual.
- Ejecución presupuestaria mensual.
- Reporte trimestral de transferencias.
- Ejecución de inversión Subt. 31 por código BIP.
- Informe mensual de dotación de personal.
#### Requerimientos de Informacion Partida 31 2026
#### ID
GORE-FIN-CTRL-DOC-INFO-REQ-2026-01
#### Purp
Checklist operacional de requerimientos de información/publicación asociados a Ley de Presupuestos 2026 (Partida 31: Gobiernos Regionales).
#### Src
kb_gn_211_ley_presupuestos_2026_glosas_gores_2026_koda.yml#INFO-REQS-2026-GORES-01
#### XRef Required
- urn:knowledge:gorenuble:presupuesto:glosas-gores-2026:1.0.0#INFO-REQS-2026-GORES-01
#### Req
- INFO-REQ-01 (Semestral) SUBDERE → CEMP: Informará los montos destinados regionalmente para proyectos de conectividad digital, que incluyan servicios de telecomunicaciones y cobertura digital, de zonas rezagadas que no sean cubiertas por el Fondo de Desarrollo para las Telecomunicaciones.
- INFO-REQ-02 (Mensual + 5 días hábiles) GORES: Publicar mensualmente en sus respectivas páginas web la cartera de proyectos financiada con cargo a los presupuestos de inversión de los gobiernos regionales; y publicar los acuerdos adoptados por los respectivos consejos regionales dentro de los 5 días hábiles siguientes, contados desde la adopción del respectivo acuerdo.
- INFO-REQ-03 (Trimestral) GORES → CEMP + Comisión de Gobierno Interior, Nacionalidad, Ciudadanía y Regionalización de la Cámara de Diputados + SUBDERE: Informar: a) el uso de los recursos con cargo a los presupuestos de inversión (beneficiarios, comuna, instituciones receptoras, monto, productos del convenio y aplicación regional); b) el destino de recursos FNDR a proyectos de desarrollo económico y proyectos adjudicados por sectores según actividad económica; esta información deberá publicarse en los mismos plazos en la página web de los gobiernos regionales, y un consolidado en la página web de SUBDERE.
- INFO-REQ-04 (Trimestral) GORES: Informarán acerca de la disponibilidad presupuestaria para que las universidades reconocidas por el Estado accedan a asignaciones directas de recursos provenientes del Fondo Regional para la Productividad y el Desarrollo, específicamente destinados a proyectos de ciencia, investigación, tecnología e innovación; e informarán sobre solicitudes de asignación directa recibidas para fomentar I+D, innovación y actividades relacionadas con desarrollo científico y aeroespacial a nivel nacional.
- INFO-REQ-05 (Trimestral) Cada Gobierno Regional: Publicar en su página web e informar a senadores y diputados de la respectiva región de todos los proyectos adjudicados o contratados con cargo a: oferta programática Subtítulo 24 y proyectos/contratos/convenios con cargo a Subtítulos 31 y 33; identificar, al menos: nombre del proyecto, monto estimado, postulantes, pauta de evaluación, postulante seleccionado y presupuesto aprobado, y votación del CORE en comisiones y en el Consejo Regional.
- INFO-REQ-06 (Trimestral) SUBDERE: Publicará trimestralmente en su página web la distribución de los recursos entre regiones, los criterios que fundan dicha distribución, la cartera de proyectos que con ellos se financie, individualizando el costo de cada uno de dichos proyectos y la ejecución presupuestaria del Plan Especial de Zonas Extremas por región.
- INFO-REQ-07 (A más tardar 30-04-2026) DIPRES → CEMP + Comisión de Gobierno Interior, Nacionalidad, Ciudadanía y Regionalización de la Cámara + Comisión de Gobierno, Descentralización y Regionalización del Senado: Informará los saldos iniciales de caja incorporados al presupuesto de cada Gobierno Regional a dicha fecha (programa de funcionamiento e inversión).
- INFO-REQ-08 (Semestral) GORES → CEMP + Comisión de Vivienda, Desarrollo Urbano y Bienes Nacionales de la Cámara de Diputados: Informar sobre los avances en la compra de terrenos para viviendas sociales.
- INFO-REQ-09 (Publicación permanente) Cada gobierno regional beneficiario FRPD: Publicar en Transparencia Activa, de forma permanente, completa y actualizada, montos recibidos e informes de ejecución presupuestaria, incluyendo detalle de transferencias efectuadas, conforme a ley N° 20.285; omisión o falta de actualización reclamable según artículo 8° de dicha ley.
- INFO-REQ-10 (Antes del 30-09-2026) DIPRES → CEMP + GORES: Informará criterios aplicados para asignación de recursos adicionales dentro de Partida 31, indicando expresamente nivel de ejecución presupuestaria considerado por región y decisiones de distribución adoptadas.
- INFO-REQ-11 (Trimestral) SUBDERE → Gobierno Regional del Maule + CEMP: Informará estado de implementación del Fondo de Apoyo al Transporte Público y la Conectividad Regional en la región, señalando la aplicación de reglas sectoriales vigentes y evaluaciones sobre alternativas de flexibilidad dentro del marco normativo aplicable para financiar iniciativas de interés regional.
- INFO-REQ-12 (Trimestral) Gobierno Regional → Comisiones de Gobierno, Descentralización y Regionalización y de Hacienda del Senado + Comisiones de Gobierno Interior, Nacionalidad, Ciudadanía y Regionalización y de Hacienda de la Cámara de Diputados: Informar todas las iniciativas y proyectos de inversión que superen 500 UTM, individualizando: proyecto, antecedentes tenidos a la vista para su aprobación, montos, plazo de ejecución e identidad a quien se entregarán los recursos.
- INFO-REQ-12B (Hasta último día hábil de marzo 2026) Gobierno Regional → Comisiones de Hacienda de ambas Cámaras: Informar el nombre y cargo del responsable de evacuar esta información, así como del funcionario que lo subrogará en caso de ausencia.
- INFO-REQ-13 (Trimestral) Gobernador regional → Comisiones de Gobierno, Descentralización y Regionalización y de Hacienda del Senado + Comisiones de Gobierno Interior, Nacionalidad, Ciudadanía y Regionalización y de Hacienda de la Cámara de Diputados: Informar toda transferencia con cargo al Fondo de Vinculación con la Comunidad: beneficiario, comuna, objeto del financiamiento, montos totales transferidos y fecha de cada transferencia.
- INFO-REQ-13B (Hasta último día hábil de marzo 2026) Gobierno Regional → Comisiones de Hacienda de ambas Cámaras: Informar el nombre y cargo de la persona responsable de evacuar la información solicitada y de quien le subrogará en su ausencia.
- INFO-REQ-14 (Semestral) GORES → CEMP: Informar, a través de informe consolidado, respecto de la ejecución presupuestaria e información sobre el avance de las iniciativas financiadas a través de los Planes Especiales de Zonas Extremas.
- INFO-REQ-15 (Anual) GORES → CEMP: Informarán los recursos destinados a abastecimiento mediante camiones aljibe en situaciones de emergencia hídrica.
- INFO-REQ-16 (Anual) Gobierno Regional → CEMP: Informará las acciones de coordinación con la Dirección de Obras Hidráulicas para atender emergencias APR, detallando tiempos de respuesta y mecanismos de seguimiento.
#### Rec
Ante dudas, solicitar dictamen a DIPRES o CGR antes de ejecutar.
#### Ref
- GN-PPTO-GLOS-DIPRES
- GN-PPTO-GLOS-CGR
### Formatos y Anexos DIPRES
#### ID
GORE-FIN-CTRL-DOC-DIPRES-FORMATOS-01
#### Asunto
Formatos y anexos requeridos por DIPRES.
#### Src
Oficio Circular N°11 DIPRES 2025 (última versión disponible en corpus).
#### Purp
Estandarizar información remitida.
#### Cpt Anexos
- Anexo 1: Certificado de Acuerdo CORE.
- Anexo 2: Reporte Mensual de Ejecución.
- Anexo 3: Reporte Trimestral de Transferencias.

## Instrumentos de Ejecucion
### ID
GORE-FIN-INSTRUMENTOS-01
### Convenios y Transferencias
#### ID
GORE-FIN-INSTR-CONVENIOS-01
#### Cpt
El convenio de transferencia es la herramienta jurídica central para materializar transferencias Subt. 24 y 33.
#### Purp
Formalizar relaciones entre GORE y receptor, definir obligaciones y asegurar rendición.
#### Fnd
Art. 23-27 Ley 21.796 para transferencias a privados y normativa complementaria para entidades públicas.
#### Req Contenido Minimo
- Partes, objeto, monto, plazos y productos.
- Obligaciones de ejecución y seguimiento.
- Reglas de rendición de cuentas, reintegro de saldos y garantías.
#### Proc
#### ID
GORE-FIN-INSTR-CONV-PROCESO-01
#### Secuencia
- Elaboración de borrador.
- Suscripción por las partes.
- Entrega de garantías cuando corresponda.
- Toma de Razón si aplica.
- Ejecución (pago y monitoreo).
- Rendición (SISREC).
- Cierre (aprobación rendición y reintegro de saldos).
#### Ref
- GN-PPTO-GLOS-CGR
- GN-PPTO-GLOS-DIPRES
- GN-PPTO-GLOS-SIGFE
- GN-PPTO-GLOS-SISREC
### Programas Directos GORE
#### ID
GORE-FIN-INSTR-PROGDIR-01
#### Marco
#### ID
GORE-FIN-INSTR-PROGDIR-MARCO-01
#### Asunto
Programas ejecutados directamente por el GORE (oferta programática adicional).
#### Fnd
Art. 20 letra k) LOC GORE; Glosa 06 Partida 31 Ley 21.796.
#### Mech
- GORE desarrolla programas con cargo a presupuesto de inversión, ejecutados directamente o vía privados a través de concursos.
#### Evaluacion ExAnte
#### ID
GORE-FIN-INSTR-PROGDIR-EVAL-EXANTE-01
#### Req
- Programas nuevos ejecutados directamente por GORE deben someterse a evaluación ex-ante de diseño por MDSF/DIPRES (Glosa 06).
#### Src
Oficio Circular N°22 DIPRES.
#### Proc
- GORE nomina contraparte.
- Presenta perfil de programa.
- Completa Formulario de Diseño Ex-Ante.
- SES/DIPRES revisan y emiten certificado.
#### Res
Recomendado Favorablemente (RF) es requisito para financiar el programa.
#### Cond Excepciones
- Continuidad de programas existentes.
- Concursos 8% FNDR.
- Transferencias a entidades públicas.
- Emergencias.
- Programas con RF previo o FRPD según Res. 33/2024.
#### Gastos Administracion Programas
#### ID
GORE-FIN-INSTR-PROGDIR-GASTOS-ADM-01
#### Cpt Regla Clave
- GORE puede destinar hasta 5% del monto de cada programa a gastos de administración propios.
- Receptor público puede usar hasta 5% para contratar honorarios de gestión.

## Cumplimiento Hitos y KPIs
### ID
GORE-FIN-CUMPLIMIENTO-01
### Sistema Seguimiento Hitos
#### ID
GORE-FIN-CUMPL-PLAN-01
#### Purp
Instaurar sistema interno de seguimiento de hitos de ejecución física y financiera.
#### Proc
- Planificación anual: DIPIR y DAF definen hitos y cronograma maestro.
- Monitoreo periódico: reuniones técnicas mensuales y directivas trimestrales.
- Coordinación interinstitucional con unidades técnicas.
- Alertas tempranas para detectar problemas y reaccionar oportunamente.
#### Ref
- GN-PPTO-GLOS-DIPIR
- GN-PPTO-GLOS-DAF
### Indicadores Desempeno
#### ID
GORE-FIN-CUMPL-KPIS-01
#### Asunto
Indicadores clave para monitoreo de desempeño.
#### Src
Indicadores GORE Ñuble en Ley de Presupuestos (vigente).
#### Ctx
La Ley fija indicadores de eficacia, eficiencia, calidad y economía para cada GORE.
#### Ejemplos Nuble
- % de proyectos Subt. 31 y 33 (incluyendo FRIL) con visita en terreno.
- % de iniciativas FNDR del PROPIR georreferenciadas y pertinentes.
- % de iniciativas de fomento productivo que benefician a mujeres.
#### Obj
Lograr gestión por resultados evitando ejecución apresurada de fin de año ('dicembreo').
#### Ref
- GN-PPTO-GLOS-FNDR
- GN-PPTO-GLOS-FRIL
- GN-PPTO-GLOS-PROPIR

## Herramientas de Soporte
### ID
GORE-FIN-HERRAMIENTAS-01
### SIGFE
#### ID
GORE-FIN-HERRAM-SIGFE-01
#### Def
Sistema de Información para la Gestión Financiera del Estado, contable-presupuestario y transaccional.
#### Resp
DAF.
#### Purp
- Control presupuestario en línea.
- Generación de reportes para DIPRES.
- Gestión de pagos y registro de todas las etapas del gasto.
#### Rec
DIPIR debiera contar con usuarios de consulta para seguimiento de ejecución por iniciativa.
#### Ref
- GN-PPTO-GLOS-SIGFE
### BIP
#### ID
GORE-FIN-HERRAM-BIP-01
#### Def
Banco Integrado de Proyectos, plataforma del SNI para registro y seguimiento de iniciativas de inversión.
#### Nat
Registro único nacional de proyectos con código BIP.
#### Resp
DIPIR.
#### Purp
- Evaluación ex-ante y obtención de RS/AD.
- Seguimiento físico y planificación multianual (ARI).
#### Warn
Interoperabilidad limitada con SIGFE; requiere conciliaciones manuales.
#### Ref
- GN-PPTO-GLOS-BIP
- GN-PPTO-GLOS-SNI
### Chileindica
#### ID
GORE-FIN-HERRAM-CHILEINDICA-01
#### Asunto
Plataforma Chileindica.
#### Src
Guías Chileindica e instructivo de coordinación ARI-PROPIR.
#### Def
Plataforma para coordinación y seguimiento de inversión pública regional (ARI y PROPIR).
#### Ctx
URL: <www.chileindica.cl>.
#### Purp
- Formulación y aprobación de ARI y PROPIR.
- Seguimiento de ejecución del PROPIR.
#### Resp
SEREMI y servicios públicos regionales, en coordinación con GORE.
#### Ref
- GN-PPTO-GLOS-ARI
- GN-PPTO-GLOS-PROPIR
- GN-PPTO-GLOS-GORE

## Conclusion General
### ID
GORE-FIN-CONCLUSION-01
### Sintesis
#### ID
GORE-FIN-CONCLUSION-SINTESIS-01
#### Cpt
- La gestión presupuestaria GORE es un proceso complejo que exige trabajo colaborativo entre DAF y DIPIR.
- DAF aporta rigor financiero, cumplimiento normativo y control de fondos.
- DIPIR aporta visión de desarrollo, priorización de inversiones y seguimiento de resultados.
- Objetivo cuantitativo: ejecutar 100% del presupuesto.
- Objetivo cualitativo: ejecutar con eficiencia, legalidad y pertinencia territorial.
- Claves del éxito: dominar el ciclo presupuestario, aplicar correctamente clasificador y glosas, documentar actos y someterse a controles, usando esta guía como referencia.
#### Res
Una gestión presupuestaria sólida y confiable respalda los objetivos de desarrollo regional y la legitimidad del GORE frente a la ciudadanía y los órganos de control.
#### Ref
- GN-PPTO-GLOS-GORE
- GN-PPTO-GLOS-DAF
- GN-PPTO-GLOS-DIPIR
