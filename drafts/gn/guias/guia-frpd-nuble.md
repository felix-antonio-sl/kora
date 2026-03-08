---
_manifest:
  urn: urn:gn:kb:guia-frpd-nuble
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/ipr/kb_gn_027_guia_frpd_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- frpd
- fomento-productivo
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/ipr/kb_gn_027_guia_frpd_koda.yml
    source_hashes:
      domains/gn/03_operacion/ipr/kb_gn_027_guia_frpd_koda.yml: 4f4808ccddcb30b222213dde102ece5d7c782ef8a25540c58b78bba2c36eeff4
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
    meat_count: 801
    fat_count: 0
    preserved_facts:
    - AI-Remediator=KODA-TRANSFORMER
    - Creation-Date=2025-11-28
    - 'Ctx=Guía operativa para el concurso FRPD 2025 del Gobierno Regional de Ñuble.

      Regula requisitos, procesos, actores y restricciones para la asignación del

      Fondo Regional para la Productividad y el Desarrollo (FRPD) en la región.

      '
    - Format=KODA/Spec
    - Formulario_FRPD_Application_2025.Ctx[0]=Deriva directamente del bloque FORM-GN-FRPD-APPLICATION-2025-01
      del documento fuente.
    - Formulario_FRPD_Application_2025.ID=GN-FRPD-FORM-APPLICATION-2025-01
    - Formulario_FRPD_Application_2025.Purp=Definir los campos obligatorios y estructura
      del formulario de postulación FRPD 2025.
    - 'Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[0].Field-Constraint=Req:
      mandatory.'
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[0].Field-Label=Código
      BIP
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[0].Field-Type=Text
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[0].ID=GN-FRPD-FORM-COD-BIP
    - 'Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[1].Field-Constraint=Req:
      mandatory.'
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[1].Field-Label=Nombre
      del Programa
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[1].Field-Type=Text
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[1].ID=GN-FRPD-FORM-NOMBRE-PROGRAMA
    - 'Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[2].Field-Constraint=Req:
      mandatory. Min-Val: 0.'
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[2].Field-Label=Monto
      solicitado FNDR
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[2].Field-Type=Number
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[2].ID=GN-FRPD-FORM-MONTO-FNDR
    - 'Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[3].Field-Constraint=Req:
      mandatory. Min-Val: 0.'
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[3].Field-Label=Monto
      total del Programa
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[3].Field-Type=Number
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[3].ID=GN-FRPD-FORM-MONTO-TOTAL
    - 'Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[4].Field-Constraint=Req:
      mandatory. Min-Val: 1. Max-Val: 30.'
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[4].Field-Label=Plazo
      de ejecución (meses)
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[4].Field-Type=Number
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[4].ID=GN-FRPD-FORM-PLAZO-MESES
    - 'Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[5].Field-Constraint=Req:
      mandatory.'
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[5].Field-Label=Eje
      ERD
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[5].Field-Type=Text
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[5].ID=GN-FRPD-FORM-EJE-ERD
    - 'Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[6].Field-Constraint=Req:
      mandatory.'
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[6].Field-Label=Lineamiento
      ERD
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[6].Field-Type=Text
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[6].ID=GN-FRPD-FORM-LINEAMIENTO-ERD
    - 'Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[7].Field-Constraint=Req:
      mandatory.'
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[7].Field-Label=Objetivo
      ERD
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[7].Field-Type=Text
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[7].ID=GN-FRPD-FORM-OBJETIVO-ERD
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[8].Field-Instr=Marcar
      con X el lineamiento al que postula.
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[8].Field-Label=Lineamiento
      al que postula
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[8].Field-Options[0]=Social
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[8].Field-Options[1]=Asistencia
      técnica a municipalidades
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[8].Field-Options[2]=Cultural
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[8].Field-Options[3]=Salud
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[8].Field-Options[4]=Infancia
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[8].Field-Options[5]=Energía,
      transportes y telecomunicaciones
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[8].Field-Options[6]=Medioambiente
      y gestión de residuos
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[8].Field-Options[7]=Gestión
      de recursos hídricos
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[8].Field-Options[8]=Deportes
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[8].Field-Options[9]=Movilidad
      urbana
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[8].Field-Options[10]=Cuidados
      de adulto mayor
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[8].Field-Options[11]=Conectividad
      digital
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[8].Field-Options[12]=Emergencia
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[8].Field-Options[13]=Fomento
      productivo, emprendimiento, innovación
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[8].Field-Options[14]=Seguridad
      pública
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[8].Field-Options[15]=Atracción
      de inversiones
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[8].Field-Type=Checkbox-Group
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.Campos[8].ID=GN-FRPD-FORM-LINEAMIENTO-POSTULA
    - Formulario_FRPD_Application_2025.Seccion_1_Identificacion_Iniciativa.ID=GN-FRPD-FORM-SEC1-IDENT
    - 'Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[0].Field-Constraint=Req:
      mandatory.'
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[0].Field-Label=Institución
      o Servicio Postulante
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[0].Field-Type=Text
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[0].ID=GN-FRPD-FORM-INSTITUCION
    - 'Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[1].Field-Constraint=Req:
      mandatory.'
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[1].Field-Label=Representante
      Legal
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[1].Field-Type=Text
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[1].ID=GN-FRPD-FORM-REP-LEGAL
    - 'Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[2].Field-Constraint=Req:
      mandatory.'
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[2].Field-Label=Responsable
      de la formulación
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[2].Field-Type=Text
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[2].ID=GN-FRPD-FORM-RESP-FORMULACION
    - 'Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[3].Field-Constraint=Req:
      mandatory. Format: email.'
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[3].Field-Label=Correo
      y teléfono formulador
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[3].Field-Type=Text
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[3].ID=GN-FRPD-FORM-CONTACTO-FORMULADOR
    - 'Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[4].Field-Constraint=Req:
      mandatory.'
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[4].Field-Label=Antecedentes
      y Misión Institucional
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[4].Field-Type=TextArea
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[4].ID=GN-FRPD-FORM-ANTECEDENTES-MISION
    - 'Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[5].Field-Constraint=Req:
      mandatory.'
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[5].Field-Label=Nombre
      del instrumento o programa a utilizar
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[5].Field-Type=Text
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[5].ID=GN-FRPD-FORM-NOMBRE-INSTRUMENTO
    - 'Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[6].Field-Constraint=Req:
      mandatory.'
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[6].Field-Label=Descripción
      del instrumento o programa a utilizar
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[6].Field-Type=TextArea
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[6].ID=GN-FRPD-FORM-DESC-INSTRUMENTO
    - 'Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[7].Field-Constraint=Req:
      mandatory.'
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[7].Field-Label=Marco
      Legal para operar y realizar el programa
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[7].Field-Type=TextArea
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[7].ID=GN-FRPD-FORM-MARCO-LEGAL-PROGRAMA
    - 'Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[8].Field-Constraint=Req:
      mandatory.'
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[8].Field-Label=Fundamento
      de la solicitud de transferencia a la institución
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[8].Field-Type=TextArea
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[8].ID=GN-FRPD-FORM-FUNDAMENTO-TRANSFERENCIA
    - 'Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[9].Field-Constraint=Req:
      mandatory. Min-Val: 0.'
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[9].Field-Label=N°
      de programas en ejecución con Gobierno Regional
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[9].Field-Type=Number
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[9].ID=GN-FRPD-FORM-N-PROGRAMAS-EJEC
    - 'Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[10].Field-Constraint=Req:
      mandatory. Min-Val: 0.'
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[10].Field-Label=Saldo
      por rendir programas en ejecución (a la fecha de postulación)
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[10].Field-Type=Number
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.Campos[10].ID=GN-FRPD-FORM-SALDO-POR-RENDIR
    - Formulario_FRPD_Application_2025.Seccion_2_Institucion_Postulante.ID=GN-FRPD-FORM-SEC2-INSTITUCION
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[0].Field-Label=Análisis
      de los involucrados
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[0].Field-Type=Static-Text
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[0].ID=GN-FRPD-FORM-ANALISIS-INVOLUCRADOS
    - 'Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[1].Field-Constraint=Req:
      mandatory.'
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[1].Field-Instr=Identificar
      beneficiarios directos e indirectos en todos los niveles.
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[1].Field-Label=Descripción
      del grupo objetivo
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[1].Field-Type=TextArea
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[1].ID=GN-FRPD-FORM-DESC-GRUPO-OBJETIVO
    - 'Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[2].Field-Constraint=Req:
      mandatory.'
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[2].Field-Label=Territorio
      a intervenir
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[2].Field-Type=Text
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[2].ID=GN-FRPD-FORM-TERRITORIO-INTERVENIR
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[3].Field-Label=Identificación
      de proyectos o programas anteriores destinados al grupo objetivo (FNDR o Sectorial).
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[3].Field-Type=TextArea
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[3].ID=GN-FRPD-FORM-PROY-ANTERIORES
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[4].Field-Label=Análisis
      de los beneficiarios
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[4].Field-Type=Static-Text
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[4].ID=GN-FRPD-FORM-ANALISIS-BENEFICIARIOS
    - 'Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[5].Field-Constraint=Req:
      mandatory.'
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[5].Field-Label=Requisitos
      específicos para calificar como beneficiario
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[5].Field-Type=TextArea
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[5].ID=GN-FRPD-FORM-REQ-BENEFICIARIO
    - 'Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[6].Field-Constraint=Req:
      mandatory.'
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[6].Field-Label=Descripción
      del procedimiento de selección de beneficiarios
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[6].Field-Type=TextArea
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[6].ID=GN-FRPD-FORM-PROC-SELECCION-BENEF
    - 'Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[7].Field-Constraint=Req:
      mandatory.'
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[7].Field-Label=Beneficios
      a recibir por beneficiario individual
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[7].Field-Type=TextArea
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[7].ID=GN-FRPD-FORM-BENEFICIOS-INDIVIDUALES
    - 'Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[8].Field-Constraint=Req:
      mandatory.'
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[8].Field-Label=Numero
      estimado de beneficiarios (por grupo objetivo y género)
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[8].Field-Type=Text
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[8].ID=GN-FRPD-FORM-N-ESTIMADO-BENEF
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[9].Field-Label=Análisis
      del Problema
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[9].Field-Type=Static-Text
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[9].ID=GN-FRPD-FORM-ANALISIS-PROBLEMA
    - 'Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[10].Field-Constraint=Req:
      mandatory.'
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[10].Field-Label=Identificación
      del problema (problemas principales de la situación)
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[10].Field-Type=TextArea
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[10].ID=GN-FRPD-FORM-IDENTIFICACION-PROBLEMA
    - 'Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[11].Field-Constraint=Req:
      mandatory.'
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[11].Field-Label=Definición
      del problema central (aplicando prioridad y selectividad)
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[11].Field-Type=TextArea
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[11].ID=GN-FRPD-FORM-DEFINICION-PROBLEMA-CENTRAL
    - 'Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[12].Field-Constraint=Req:
      mandatory.'
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[12].Field-Label=Efectos
      del problema (definir los más importantes)
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[12].Field-Type=TextArea
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[12].ID=GN-FRPD-FORM-EFECTOS-PROBLEMA
    - 'Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[13].Field-Constraint=Req:
      mandatory.'
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[13].Field-Label=Causas
      del problema (elementos que lo provocan)
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[13].Field-Type=TextArea
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[13].ID=GN-FRPD-FORM-CAUSAS-PROBLEMA
    - 'Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[14].Field-Constraint=Req:
      mandatory.'
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[14].Field-Instr=Construir
      y presentar árbol de problemas. El árbol debe dar una imagen completa de la
      situación negativa. Verificar validez e integridad.
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[14].Field-Label=Árbol
      de problemas (diagrama Causa-Efecto)
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[14].Field-Type=File
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[14].ID=GN-FRPD-FORM-ARBOL-PROBLEMAS
    - 'Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[15].Field-Constraint=Req:
      mandatory.'
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[15].Field-Instr=Convertir
      condiciones negativas a positivas. Examinar relación medio-fin. Añadir nuevos
      objetivos si es necesario.
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[15].Field-Label=Diagrama
      de árbol de soluciones (medios y fines)
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[15].Field-Type=File
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.Campos[15].ID=GN-FRPD-FORM-ARBOL-OBJETIVOS
    - Formulario_FRPD_Application_2025.Seccion_3_Diagnostico.ID=GN-FRPD-FORM-SEC3-DIAGNOSTICO
    - Formulario_FRPD_Application_2025.Seccion_4_Identificacion_Programa.Campos[0].Field-Label=Estructura
      Analítica del Programa
    - Formulario_FRPD_Application_2025.Seccion_4_Identificacion_Programa.Campos[0].Field-Type=TextArea
    - Formulario_FRPD_Application_2025.Seccion_4_Identificacion_Programa.Campos[0].ID=GN-FRPD-FORM-ESTRUCTURA-ANALITICA
    - Formulario_FRPD_Application_2025.Seccion_4_Identificacion_Programa.Campos[1].Field-Label=Árbol
      de objetivos (seleccionados)
    - Formulario_FRPD_Application_2025.Seccion_4_Identificacion_Programa.Campos[1].Field-Type=File
    - Formulario_FRPD_Application_2025.Seccion_4_Identificacion_Programa.Campos[1].ID=GN-FRPD-FORM-ARBOL-OBJETIVOS-SEL
    - Formulario_FRPD_Application_2025.Seccion_4_Identificacion_Programa.Campos[2].Field-Label=Estructura
      del Programa
    - Formulario_FRPD_Application_2025.Seccion_4_Identificacion_Programa.Campos[2].Field-Type=TextArea
    - Formulario_FRPD_Application_2025.Seccion_4_Identificacion_Programa.Campos[2].ID=GN-FRPD-FORM-ESTRUCTURA-PROGRAMA
    - Formulario_FRPD_Application_2025.Seccion_4_Identificacion_Programa.Campos[3].Field-Label=Objetivo
      general del programa
    - Formulario_FRPD_Application_2025.Seccion_4_Identificacion_Programa.Campos[3].Field-Type=TextArea
    - Formulario_FRPD_Application_2025.Seccion_4_Identificacion_Programa.Campos[3].ID=GN-FRPD-FORM-OBJ-GENERAL
    - Formulario_FRPD_Application_2025.Seccion_4_Identificacion_Programa.Campos[4].Field-Label=Productos
      que se entregarán
    - Formulario_FRPD_Application_2025.Seccion_4_Identificacion_Programa.Campos[4].Field-Type=TextArea
    - Formulario_FRPD_Application_2025.Seccion_4_Identificacion_Programa.Campos[4].ID=GN-FRPD-FORM-PRODUCTOS-ENTREGAR
    - Formulario_FRPD_Application_2025.Seccion_4_Identificacion_Programa.Campos[5].Field-Label=Resultados
      esperados
    - Formulario_FRPD_Application_2025.Seccion_4_Identificacion_Programa.Campos[5].Field-Type=TextArea
    - Formulario_FRPD_Application_2025.Seccion_4_Identificacion_Programa.Campos[5].ID=GN-FRPD-FORM-RESULTADOS-ESPERADOS
    - Formulario_FRPD_Application_2025.Seccion_4_Identificacion_Programa.ID=GN-FRPD-FORM-SEC4-IDENT-PROGRAMA
    - 'Formulario_FRPD_Application_2025.Seccion_5_Matriz_Marco_Logico.Campos[0].Field-Instr=Completar
      la matriz para cada nivel: Fin, Propósito, Componentes y Actividades.'
    - Formulario_FRPD_Application_2025.Seccion_5_Matriz_Marco_Logico.Campos[0].Field-Label=Matriz
      de Marco Lógico
    - Formulario_FRPD_Application_2025.Seccion_5_Matriz_Marco_Logico.Campos[0].Field-Type=Repeater
    - Formulario_FRPD_Application_2025.Seccion_5_Matriz_Marco_Logico.Campos[0].ID=GN-FRPD-FORM-MATRIZ-MML
    - Formulario_FRPD_Application_2025.Seccion_5_Matriz_Marco_Logico.ID=GN-FRPD-FORM-SEC5-MML
    - 'Formulario_FRPD_Application_2025.Seccion_6_Operatividad_Programa.Campos[0].Field-Constraint=Req:
      mandatory.'
    - Formulario_FRPD_Application_2025.Seccion_6_Operatividad_Programa.Campos[0].Field-Instr=Incorporar
      carta Gantt de actividades y financiera.
    - Formulario_FRPD_Application_2025.Seccion_6_Operatividad_Programa.Campos[0].Field-Label=Etapa
      de Planificación y Control
    - Formulario_FRPD_Application_2025.Seccion_6_Operatividad_Programa.Campos[0].Field-Type=File
    - Formulario_FRPD_Application_2025.Seccion_6_Operatividad_Programa.Campos[0].ID=GN-FRPD-FORM-ETAPA-PLANIFICACION-CONTROL
    - Formulario_FRPD_Application_2025.Seccion_6_Operatividad_Programa.ID=GN-FRPD-FORM-SEC6-OPERATIVIDAD
    - Formulario_FRPD_Application_2025.Seccion_7_Presupuesto.Campos[0].Field-Label=Presupuesto
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
---

# Guía Operativa FRPD Ñuble 2025
## ID
GN-FRPD-GUIA-OPERATIVA-2025-01

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
IA-CASCADE

## AI Remediator
KODA-TRANSFORMER

## Creation Date
2025-11-28

## Modification Date
2025-11-28

## Ctx
Guía operativa para el concurso FRPD 2025 del Gobierno Regional de Ñuble.
Regula requisitos, procesos, actores y restricciones para la asignación del
Fondo Regional para la Productividad y el Desarrollo (FRPD) en la región.


## Source
### Primary Source
kb_gn_027_guia_frpd_sts.md
### Ctx Required
- Marco legal de Royalty Minero y FRPD (FIN-GORE-NORMATIVA-LEY-ROYALTY-01, FIN-GORE-NORMATIVA-GLOSA-13-01, FIN-GORE-NORMATIVA-FRPD-REGULACION-OPERATIVA-01).
- Glosa 06 de la Ley de Presupuestos y Circular N°22 de DIPRES.
- Resolución Exenta N°33 de la SUBCTCI (31-Ene-2024) sobre instituciones habilitadas.
- Guía de Proyectos SNI (kb_gn_024_guia_idi_sni_sts.md).
- Guía de Programas Públicos Regionales (kb_gn_025_guia_programas_sts.md).
- Guía Operativa del Departamento de Análisis y Evaluación del GORE Ñuble para obtención de RS.
### Ctx Optional
- Estrategia Regional de Desarrollo (ERD) Ñuble 2023-2030.
- Estrategia Regional de Ciencia, Tecnología, Conocimiento e Innovación (ER-CTCI) 2022-2030.
- Planes regionales y sectoriales de fomento productivo pertinentes.

## LLM Parsing Instructions
### ID
KODA-LLM-PARSER-GN-FRPD-ÑUBLE-2025-01
### Req
Mandatory block following Metadata.
### Prohib
Using for artifact creation or translation.
### Content
BEGIN_LLM_INSTRUCTIONS
You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

FIDELITY:
  - Preserve all meat (essential information) and skeleton (estructura:
    secciones, listas, tablas, jerarquías, relaciones) con cero pérdida.
  - Ignora fat (retórica, redundancias, frases de estilo).

LEXICON (expand before processing):
  Act->Action, Cond->Condition, Cpt->Concept, Ctx->Context,
  Def->Definition, Dest->Destination, Dln->Deadline,
  Ex->Example, Fnd->Foundation, ID->ID, Instr->Instruction,
  Just->Justification, Mech->Mechanism, Mssn->Mission, Mdl->Model,
  Nat->Nature, Obj->Objective, Proc->Process, Prohib->Prohibition,
  Purp->Purpose, Ref->Reference, Req->Requirement, Res->Result,
  Resp->Responsible, Src->Source, Warn->Warning.

REFERENCE POLICY:
  - Ref: es interno al documento; sólo puede apuntar a IDs definidos
    dentro de este mismo artefacto.
  - Documentos externos (leyes, resoluciones, oficios, formularios,
    guías complementarias, sitios web) se mencionan bajo Ctx:,
    Src:, Ctx_Required: o Ctx_Optional:, nunca bajo Ref:.

LANGUAGE POLICY:
  - Keywords en inglés (y abreviaturas como en este bloque).
  - Contenido descriptivo en español (es-CL). Nunca traduzcas el contenido.
END_LLM_INSTRUCTIONS


## Glosario FRPD
### ID
GN-FRPD-GLOSARIO-01
### Purp
Definir conceptos, siglas y normas clave recurrentes en la Guía Operativa FRPD Ñuble 2025.
### Terminos
| ID | Sigla | Cpt | Def |
| --- | --- | --- | --- |
| GN-FRPD-GLOS-FRPD | FRPD | Fondo Regional para la Productividad y el Desarrollo | Fondo regional asociado al Royalty Minero para financiar iniciativas de fomento productivo, innovación, ciencia, tecnología y desarrollo regional. |
| GN-FRPD-GLOS-FNDR | FNDR | Fondo Nacional de Desarrollo Regional | Principal fuente de financiamiento de proyectos y programas regionales, incluyendo recursos complementarios al FRPD. |
| GN-FRPD-GLOS-GORE | GORE | Gobierno Regional | Administración superior de la región, responsable del concurso FRPD y de la ejecución de iniciativas financiadas. |
| GN-FRPD-GLOS-CTCI | CTCI | Ciencia, Tecnología, Conocimiento e Innovación | Conjunto de actividades de generación y aplicación de conocimiento que el FRPD prioriza como motor de transformación y desarrollo regional. |
| GN-FRPD-GLOS-SISREC | SISREC | Sistema de Rendición de Cuentas | Plataforma electrónica obligatoria para la rendición de recursos FNDR/FRPD (Art. 24 Ley N° 21.796). |
| GN-FRPD-GLOS-RATE | RATE | Resultado de la Evaluación Técnica | Clasificaciones RS, FI, OT y NV que resumen el resultado de la evaluación técnica de una iniciativa. |
| GN-FRPD-GLOS-RS | RS | Recomendado Favorablemente | Calificación que indica aprobación técnica y habilita la obtención de RS para financiamiento. |

## Guia Operativa FRPD Ñuble 2025
### ID
GN-FRPD-GUIA-OPERATIVA-2025-01
### Titulo
Guía Operativa FRPD Ñuble 2025
### Purp
Regular el concurso FRPD 2025 para la asignación de recursos del Fondo
Regional para la Productividad y el Desarrollo en la Región de Ñuble,
definiendo reglas, criterios, plazos y responsabilidades para las
instituciones habilitadas.

### Destinatarios
- Instituciones públicas y entidades habilitadas por SUBCTCI para ejecutar programas y proyectos FRPD.
- Equipos técnicos del GORE Ñuble (DIPIR, Departamentos de Análisis y Evaluación, Presupuesto, etc.).
- Autoridades regionales y actores que participan en evaluación, seguimiento y supervisión de iniciativas FRPD.
### Alcance
- Aplica al concurso FRPD 2025 del GORE Ñuble.
- Cubre desde antecedentes generales, admisibilidad, evaluación técnica, ejecución, garantías y obligaciones de rendición.
### Estructura Secciones
| ID | Cpt |
| --- | --- |
| GN-FRPD-SEC-1-ANTECEDENTES | Antecedentes Generales del FRPD y propósito de la guía. |
| GN-FRPD-SEC-2-INTRO | Introducción, contexto regional y bifurcación del proceso de evaluación. |
| GN-FRPD-SEC-3-PILARES | Pilares estratégicos, sectores y focos prioritarios del concurso. |
| GN-FRPD-SEC-4-POSTULANTES | Instituciones habilitadas y prohibiciones para postular. |
| GN-FRPD-SEC-5-PRESENTACION | Presentación de postulaciones, plazos y mecanismos de consultas. |
| GN-FRPD-SEC-6-ADM-ADMIN | Admisibilidad administrativa y criterios obligatorios. |
| GN-FRPD-SEC-7-ADM-TEC | Admisibilidad técnica, variables de evaluación y ponderaciones. |
| GN-FRPD-SEC-8-EVAL-TEC | Evaluación técnica detallada, prioridades 2025, restricciones y antecedentes requeridos. |
| GN-FRPD-SEC-9-COMUNICACION | Comunicación oficial de resultados. |
| GN-FRPD-SEC-10-EJECUCION | Ejecución de iniciativas aprobadas, convenios, transferencias, seguimiento y reevaluaciones. |
| GN-FRPD-SEC-11-PROPIEDAD | Propiedad intelectual e industrial de los resultados. |
| GN-FRPD-SEC-12-COMPROMISO-GORE | Compromisos y condiciones suspensivas del GORE. |
| GN-FRPD-SEC-13-GARANTIAS | Garantías exigidas a instituciones privadas. |
| GN-FRPD-SEC-14-OTROS | Transparencia, rendiciones, SISREC, contrapartes, objeto social, supervisión y protección de datos. |
| GN-FRPD-FORM-APPLICATION-2025-01 | Formulario de postulación FRPD 2025 (campos obligatorios y especificaciones). |
### Sec 1 Antecedentes Generales
#### ID
GN-FRPD-SEC-1-ANTECEDENTES
#### Instrumento FRPD
#### ID
GN-FRPD-ANT-INSTRUMENTO-01
#### Cpt
Fondo Regional para la Productividad y el Desarrollo (FRPD).
#### Def
Fondo regional de inversión productiva asociado al Royalty Minero.
#### Purp
- Financiar inversión productiva a través de proyectos, planes o programas.
#### Req
- Considerar regulación operativa anual del FRPD en la Ley de Presupuestos (p.ej. provisión sin distribuir en Ítem 33.03 y transferencias directas cuando aplique).
#### Ctx
- Marco legal detallado en el Selector IPR (FIN-GORE-NORMATIVA-LEY-ROYALTY-01, FIN-GORE-NORMATIVA-GLOSA-13-01).
- kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-13
#### Tipos Iniciativa
#### ID
GN-FRPD-ANT-TIPOS-01
#### Tipos
| ID | Cpt | Def | Req | Ctx_Required |
| --- | --- | --- | --- | --- |
| GN-FRPD-TIPO-PROYECTO | Proyectos de inversión. | Iniciativas de inversión de capital. | ['Formulación según la guía del Sistema Nacional de Inversiones (SNI).'] | ['kb_gn_024_guia_idi_sni_sts.md.'] |
| GN-FRPD-TIPO-PROGRAMA | Programas. | Iniciativas de gasto corriente para entrega de servicios. | ['Formulación según la Guía de Programas Públicos Regionales.'] | ['kb_gn_025_guia_programas_sts.md.'] |
#### Ambitos Principales
#### ID
GN-FRPD-ANT-AMBITOS-01
#### Ambitos
- Fomento de actividades productivas.
- Desarrollo regional.
- Promoción de investigación científica, tecnológica, conocimiento e innovación (CTCI).
#### Alineacion Estrategica Obligatoria
#### ID
GN-FRPD-ANT-ALINEACION-01
#### Req
- Estrategia Regional de Desarrollo (ERD).
- Estrategia Regional de CTCI.
- Otras prioridades estratégicas regionales de fomento productivo.
#### Rol CTCI
#### ID
GN-FRPD-ANT-ROL-CTCI-01
#### Def
Los actores de CTCI son garantes de la transformación y el desarrollo regional.
#### Resultado Esperado
#### ID
GN-FRPD-ANT-RES-ESPERADO-01
#### Res
- Generar condiciones para apertura de empresas de base tecnológica con mayores y mejores empleos.
#### Proposito Guia Operativa
#### ID
GN-FRPD-ANT-PROP-GUIA-01
#### Purp
- Regular el concurso FRPD 2025 en Ñuble, dirigido a instituciones habilitadas.
#### Src
- Resolución Exenta N°33 de SUBCTCI (31-Ene-2024) con base de instituciones habilitadas.
### Sec 2 Introduccion
#### ID
GN-FRPD-SEC-2-INTRO
#### FRPD Como Herramienta
#### ID
GN-FRPD-INTRO-FRPD-01
#### Cpt
- FRPD como desafío y aporte al desarrollo económico, productivo y social regional.
- Ciencia y tecnología como herramienta clave para transformar y fortalecer la región.
#### Purp
- Promover e incentivar la asociatividad interinstitucional para la cooperación.
#### Res
- Contribuir a diversificar la matriz productiva y aumentar la competitividad regional.
#### Alineacion Estrategica
#### ID
GN-FRPD-INTRO-ALINEACION-01
#### Req
- Alinearse con pilares y prioridades de la ERD.
- Alinearse con la Estrategia Regional de CTCI 2022-2030.
#### Consideraciones Adicionales
- Responder a demandas sociales.
- Abordar necesidades territoriales de productividad y desarrollo.
#### Concurso 2025
#### ID
GN-FRPD-INTRO-CONCURSO-01
#### Proc
- Concurso FRPD año 2025 organizado por el GORE Ñuble.
#### Obj
- Resolver brechas en fomento y productividad regional.
#### Req Iniciativas
- Las iniciativas deben resolver problemáticas en sectores y focos prioritarios definidos en la guía.
#### Mecanismo Postulacion
#### Mech
Postulación mediante formulario online.
#### Act Postulante
- Completar todos los campos del formulario.
- Subir todos los anexos solicitados.
#### Alcance Bases
#### Cpt
Las bases determinan las iniciativas preseleccionadas para financiamiento.
#### Bifurcacion Post Seleccion
#### ID
GN-FRPD-INTRO-BIFURCACION-01
#### Warn
- Según Glosa 06 y Circular N°22 DIPRES, el camino posterior a la selección depende de la naturaleza de la iniciativa.
#### Casos
-
  #### ID
  GN-FRPD-CASO-1-CTCI
  #### Cpt
  Caso 1 – Innovación, CTCI.
  #### Def
  Iniciativas estrictamente enmarcadas en CTCI.
  #### Ctx
  - Exentas del proceso de evaluación ex ante DIPRES/SES.
  - La evaluación del concurso se considera final.
-
  #### ID
  GN-FRPD-CASO-2-FOMENTO
  #### Cpt
  Caso 2 – Fomento Productivo General.
  #### Def
  Iniciativas de fomento productivo que no califican como CTCI.
  #### Req
  - DEBEN ingresar al proceso de evaluación ex ante correspondiente.
  - Si son proyectos de inversión, seguir Guía SNI (kb_gn_024_guia_idi_sni_sts.md).
  - Si son programas de servicios, seguir Guía de Programas Públicos (kb_gn_025_guia_programas_sts.md).
### Sec 3 Pilares Estrategicos Concurso 2025
#### ID
GN-FRPD-SEC-3-PILARES
#### Referencias Legales Clave
#### ID
GN-FRPD-PILARES-REF-01
#### Ctx
- Ley de Royalty Minero (FIN-GORE-NORMATIVA-LEY-ROYALTY-01).
- Regulación operativa FRPD (FIN-GORE-NORMATIVA-FRPD-REGULACION-OPERATIVA-01).
#### Ambitos Accion
#### ID
GN-FRPD-PILARES-AMBITOS-01
#### Ambitos
#### Investigacion
#### Cpt
Investigación.
#### Subtipos
- Básica: esencial para formación de talento, innovación y solución de problemas.
- Aplicada: resuelve problemas relevantes específicos.
- Desarrollo experimental: crea o ensaya nuevas metodologías o tecnologías.
#### Innovacion
#### Cpt
Innovación.
#### Subtipos
- Base científico-tecnológica: clave para diversificación productiva.
- Productiva: introduce nuevos productos/servicios al mercado.
- Social: nuevos productos/servicios que satisfacen necesidades sociales.
- Pública: nuevas soluciones con valor público implementadas en el sector público.
#### Emprendimiento
#### Cpt
Emprendimiento (empresa).
#### Def
Actividades para solucionar problemas complejos y globales con potencial de crecimiento regional.
#### Difusion y Transferencia
#### Cpt
Divulgación, difusión y transferencia tecnológica.
#### Def
Programas que diseminan conocimiento, ciencia y tecnología hacia sociedad, industria y sector público.
#### Sectores Prioritarios
#### ID
GN-FRPD-PILARES-SECTORES-01
#### Lista Sectores
- Atracción de Inversiones para el Desarrollo Regional.
- Desarrollo Empresarial, Fomento Productivo e Inversión Productiva.
- Turismo y/o Medioambiente.
- Energía y/o Conectividad Digital.
#### Focos Prioritarios
#### ID
GN-FRPD-PILARES-FOCOS-01
#### Req
- Las iniciativas deben alinearse a los sectores prioritarios definidos para el concurso.
#### Ctx
- Marco estratégico validado por el Comité Regional de Ciencia.
#### Instrumentos Planificacion
- Estrategia de Desarrollo Regional al 2030.
- Estrategia Regional de CTCI.
#### Focos Principales
- Conocimiento, Ciencia, Tecnología e Innovación.
- Gestión, Competitividad, Capacitación Laboral e Innovación.
- Agroindustrial, Silvoagropecuario y/o Pesca.
- Emprendimiento, Turismo y Medioambiente.
### Sec 4 Postulantes Habilitados
#### ID
GN-FRPD-SEC-4-POSTULANTES
#### Criterio General
#### ID
GN-FRPD-POST-CRITERIO-01
#### Cpt
Cumplir con Resolución Exenta N°33 de SUBCTCI (31-Ene-2024) sobre instituciones habilitadas.
#### Lista Instituciones Habilitadas
#### ID
GN-FRPD-POST-LISTA-01
#### Cpt
Listado de instituciones habilitadas para postular al FRPD 2025.
#### Instituciones
- Agencia Nacional de Investigación y Desarrollo (ANID).
- CORFO (incluyendo Comité Innova Chile).
- Fundación para la Innovación Agraria (FIA).
- Servicio de Cooperación Técnica (SERCOTEC).
- Instituto de Desarrollo Agropecuario (INDAP).
- Subsecretaría de Economía y Empresas de Menor Tamaño (programas Desarrollo Productivo Sostenible).
- Subsecretaría de Ciencia, Tecnología, Conocimiento e Innovación.
- Servicio de Evaluación Ambiental.
- Servicio de Biodiversidad y Áreas Protegidas (SBAP).
- Servicio Nacional de Pesca y Acuicultura.
- Servicio Nacional de Turismo.
- Agencia de Promoción de la Inversión Extranjera (InvestChile).
- Instituto Nacional de Propiedad Industrial (INAPI).
- Servicio Nacional de Aduanas.
- Dirección General de Aguas (DGA).
- Comisión Nacional de Riego (CNR).
- Corporación Nacional Forestal (CONAF).
- Agencia de Sostenibilidad Energética (ASE).
- Servicio Agrícola y Ganadero (SAG).
- Instituto Nacional de Desarrollo Sustentable de la Pesca Artesanal y de la Acuicultura de Pequeña Escala (INDESPA).
- Agencia de Sustentabilidad y Cambio Climático (ASCC).
- Dirección General de Promoción de Exportaciones (PROCHILE).
- Centro de Información de Recursos Naturales (CIREN).
- Instituto Forestal (INFOR).
- Instituto de Fomento Pesquero (IFOP).
- Fundación Chile.
- Instituto para la Resiliencia ante Desastres (ITREND).
- Fundación Conecta Logística.
- Comités de Desarrollo Productivo Regional de CORFO.
- Centros Regionales de Desarrollo Científico y Tecnológico (Programa Regional ANID).
- Centros de Investigación en Áreas Prioritarias (FONDAP).
- Centros Tecnológicos de I+D de la ANID.
- Centros Científicos y Tecnológicos de Excelencia y Centros de Investigación Avanzada en Educación (PIA).
- Centros del Programa Iniciativa Científica Milenio.
- Centros Tecnológicos (Programa Fortalecimiento y Creación de Capacidades Tecnológicas Habilitantes).
- Centros e Institutos (Programa Fortalecimiento de Institutos Públicos).
- Entidades de Programas Tecnológicos y Consorcios Tecnológicos para la Innovación; Programas Estratégicos (Transforma).
- Centros de Excelencia Internacional.
- Centros de investigación y entidades I+D registradas en CORFO (Ley N° 20.241).
- Instituciones de educación superior (literales a, b, c art. 52 DFL N°2/2010 Mineduc), con acreditación institucional vigente Ley N° 20.129.
- Corporaciones regionales con participación del GORE (glosa 04, Partida 31, Capítulo 01, Programa 02, Ley de Presupuestos 2025).
#### Prohibiciones Postulacion
#### ID
GN-FRPD-POST-PROHIB-01
#### Prohib
- Instituciones cuyo objeto social no se relacione o sin experiencia comprobable en materias pertinentes.
- Instituciones con directivos o representantes con parentesco hasta 4° consanguinidad o 3° afinidad, o vínculo de cónyuge/conviviente civil/hijo en común, con Gobernador Regional, Consejeros Regionales, Jefes de División o funcionarios del GORE (incluyendo honorarios).
- Instituciones con directivos/representantes que hayan trabajado o prestado servicios (remunerados o no) en el GORE.
- Instituciones privadas con directivos/representantes que hayan sido autoridades o funcionarios del GORE en los 2 años previos al ejercicio de su cargo público actual.
### Sec 5 Presentacion Postulaciones
#### ID
GN-FRPD-SEC-5-PRESENTACION
#### Mecanismo
#### ID
GN-FRPD-PRES-MECANISMO-01
#### Mech
Postulación en línea mediante página web del GORE Ñuble.
#### Act
- Completar formulario de postulación.
#### Plazos Claves 2025
#### ID
GN-FRPD-PRES-PLAZOS-01
#### Cpt
Plazos clave del concurso 2025 (valores específicos se completan en cada convocatoria).
#### Fechas Placeholders
- Fecha-Publicacion
- Fecha-Inicio-Preguntas
- Fecha-Final-Preguntas
- Fecha-Publicacion-Respuestas
- Fecha-Cierre-Formulario
- Fecha-Revision-Adm
- Fecha-Resultados-Adm-Adm
- Fecha-Resultados-Adm-Tec
- Plazo-Max-Ingreso-Eval-Tec
- Plazo-Max-Obtener-RS
#### Consultas y Respuestas
#### ID
GN-FRPD-PRES-CONSULTAS-01
#### Proc Consultas
#### Mech
Correo electrónico.
#### Req
- Plazo de formulación: primeros 7 días corridos desde el día hábil siguiente a la publicación.
#### Dest
Página web del GORE Ñuble (publicación de preguntas).
#### Proc Respuestas
#### Mech
Mismo correo electrónico utilizado para consultas.
#### Req
- Plazo de respuesta máximo: 5 días hábiles, salvo complejidad.
#### Res
- Respuestas compiladas y publicadas en la web del GORE en los plazos establecidos.
### Sec 6 Admisibilidad Administrativa
#### ID
GN-FRPD-SEC-6-ADM-ADMIN
#### Evaluacion
#### ID
GN-FRPD-ADM-ADMIN-EVAL-01
#### Resp
- Comisión de profesionales del GORE Ñuble.
#### Res
- Clasificación de iniciativas como 'admisibles' o 'inadmisibles'.
#### Proximo Paso
- Iniciativas admisibles pasan a admisibilidad técnica.
#### Criterios Obligatorios
#### ID
GN-FRPD-ADM-ADMIN-CRITERIOS-01
#### Cpt
Criterios A–L de admisibilidad administrativa.
#### Req
- A. Registro en línea completo.
- B. Vinculación en el registro con pilar estratégico, sector y focos prioritarios (GUIDE-GN-FRPD-STRATEGIC-PILLARS-01, GUIDE-GN-FRPD-PRIORITY-SECTORS-01, GUIDE-GN-FRPD-PRIORITY-FOCUSES-01).
- C. Formulario de admisibilidad completo.
- D. Postulante perteneciente a categorías habilitadas (GUIDE-GN-FRPD-ELIGIBLE-APPLICANTS-01).
- E. Personalidad jurídica acreditada.
- F. Máximo 2 iniciativas por postulante (se consideran las 2 primeras ingresadas cronológicamente).
- G. Carta de patrocinio firmada por Rector, Director o Jefe de Servicio.
- H. Máximo 30% del monto total a remuneraciones con cargo al fondo regional.
- I. Plazo máximo de ejecución de 30 meses.
- J. Alcance regional (21 comunas) o justificación suficiente para un territorio particular (p.ej. Valle del Itata).
- K. Mínimo 1 profesional residente en Ñuble contratado (adjuntar certificado).
- L. Certificado que acredite que viáticos, alimentación, pasajes, peajes y estacionamiento son asumidos por la institución ejecutora.
#### Consecuencia Incumplimiento
#### Res
- La iniciativa se declara inadmisible.
### Sec 7 Admisibilidad Tecnica
#### ID
GN-FRPD-SEC-7-ADM-TEC
#### Proposito
#### ID
GN-FRPD-ADM-TEC-PROP-01
#### Purp
- Tomar la mejor decisión de inversión basada en la información presentada.
#### Obj
- Evaluar aplicación de las bases, pertinencia local y factibilidad técnica.
#### Comision Evaluadora
#### ID
GN-FRPD-ADM-TEC-COMISION-01
#### Composicion
- Máximo 11 representantes del territorio vinculados a fomento e innovación.
#### Quorum Minimo
6
#### Facultades
- Realizar observaciones a las iniciativas.
#### Variables Evaluacion
#### ID
GN-FRPD-ADM-TEC-VARIABLES-01
#### Variables
- A. Coherencia global de la iniciativa.
- B. Coherencia con objetivos de desarrollo regional.
- C. Coherencia entre componentes, propósito y actividades.
- D. Mérito innovador.
#### Criterios Puntuacion
#### ID
GN-FRPD-ADM-TEC-PUNTAJE-01
#### Escala
- 1 – Interés: Nulo.
- 3 – Interés: Bajo.
- 5 – Interés: Medio.
- 7 – Interés: Alto.
#### Ponderacion Variables
#### Tabla
- Coherencia global – 10%.
- Coherencia con objetivos de desarrollo regional – 30%.
- Coherencia componentes/propósito/actividades – 20%.
- Mérito innovador – 40%.
#### Calculo Puntaje Final
#### Cpt
Promedio ponderado de todos los evaluadores.
#### Puntaje Minimo Elegibilidad
5
#### Res
- Se construye un ranking de iniciativas 'Elegibles' de mayor a menor puntuación.
- Iniciativas 'Elegibles' pasan a Evaluación Técnica.
### Sec 8 Evaluacion Tecnica y Antecedentes
#### ID
GN-FRPD-SEC-8-EVAL-TEC
#### Alcance
#### ID
GN-FRPD-EVAL-ALCANCE-01
#### Obj
- Aplicar evaluación técnica a iniciativas declaradas 'Elegibles' en etapas anteriores.
#### Criterios
- Antecedentes presentados.
- Pertinencia.
- Ejecutabilidad.
- Uso eficiente de recursos fiscales.
#### Resp
- Unidad de Proyectos y Programas del Departamento de Análisis y Evaluación del GORE Ñuble.
#### Lineamientos y Prioridades 2025
#### ID
GN-FRPD-EVAL-LINEAMIENTOS-01
#### Req
- Considerar prioridades regionales año 2025 fijadas por Resolución Exenta.
#### Lista Prioridades 2025
- SOCIAL.
- ASISTENCIA TÉCNICA A MUNICIPALIDADES.
- CULTURA.
- SALUD.
- INFANCIA.
- ENERGÍA, TRANSPORTES Y TELECOMUNICACIONES.
- MEDIOAMBIENTE Y GESTIÓN DE RESIDUOS.
- GESTIÓN DE RECURSOS HÍDRICOS.
- DEPORTES.
- MOVILIDAD URBANA.
- CUIDADOS DE ADULTO MAYOR.
- CONECTIVIDAD DIGITAL.
- EMERGENCIA.
- FOMENTO PRODUCTIVO, EMPRENDIMIENTO E INNOVACIÓN.
- SEGURIDAD PÚBLICA.
- ATRACCIÓN DE INVERSIONES.
#### Focalizacion Inversion
#### Cpt
Reglas de foco y coherencia de la inversión.
#### Req
- Propósito: solucionar un problema regional definido, identificable, demostrable y con indicadores.
- Formulación: enfocada en disminuir brechas de un problema claramente definido.
- Cobertura: considerar dimensión regional del FNDR y magnitud del problema.
- Coherencia estratégica con ERD Ñuble 2023-2030, Plan de Gobierno Regional y/o Estrategia Regional de CTCI.
- Equidad: énfasis en equidad de acceso y pertinencia, con mecanismos de selección transparentes y probos.
- Gestión: capacidad óptima de gestión, maximizando eficiencia y eficacia.
#### Restricciones Postulacion
#### ID
GN-FRPD-EVAL-RESTRICCIONES-01
#### Instituciones Publicas
#### Cpt
Restricciones para instituciones públicas.
#### Req
- No postular a programas con objetivos distintos a su ley o decreto de creación.
- Acreditar objeto social coherente.
#### Convenios Vigentes
#### Req
- Si existen convenios vigentes con el GORE, adjuntar clarificación de saldos por rendir y cumplir con Res. N°30 de 2015 CGR.
#### Uso Prohibido Recursos FNDR
#### Prohib
- Otorgar préstamos.
- Financiar gastos de personal de entidades receptoras (salvo glosas específicas).
- Financiar gastos de bienes y servicios de consumo de entidades receptoras (salvo habilitación expresa).
- Constituir, aportar o comprar sociedades o empresas.
#### Limite Gastos Administrativos
#### Req
- Máximo 5% del total postulado (Art. 25 Ley N° 21.796).
#### Rendicion Cuentas
#### Req
- Rendir cuentas obligatoriamente vía SISREC (Art. 24 Ley N° 21.796).
#### Subcontratacion
#### Cpt
Reglas sobre subcontratación.
#### Req
- Permitida sólo para actividades que no son objeto principal del proyecto.
- Precisar en formulario, presupuesto y convenio.
#### Prohib
- No subcontratar con personas relacionadas (Art. 100 Ley N° 18.045), incluyendo matrices, coligantes, filiales, directores, gerentes y parientes hasta 2° consanguinidad vinculados al Gobernador, Consejeros o directivos del GORE.
#### Contratacion Personas
#### Prohib
- Contratar cónyuges, parejas, hijos o parientes hasta 3° consanguinidad del Gobernador, Consejeros, personal directivo GORE o Jefe de Servicio/directivos de la institución postulante.
#### Antecedentes Requeridos Postulacion
#### ID
GN-FRPD-EVAL-ANTECEDENTES-01
#### Mech Ingreso
#### Cpt
Mecanismos de ingreso de antecedentes.
#### Instituciones Privadas
#### Mech
Oficio al Gobernador Regional por Oficina de Partes.
#### Instituciones Publicas
#### Mech
DOC Digital del Estado de Chile.
#### Req
- Todos los antecedentes descritos deben estar cargados en el Banco Integrado de Proyectos (BIP) al momento de la postulación.
#### Lista Antecedentes
-
  #### ID
  GN-FRPD-ANT-OFICIO-CONDUCTOR
  #### Cpt
  Oficio Conductor.
  #### Req
  - Dirigido al Gobernador Regional, firmado y timbrado.
  - Debe indicar nombre de la iniciativa, código BIP y Eje/Lineamiento/Objetivo ERD asociado.
  #### Cond
  - Si no se cumple, la iniciativa es INADMISIBLE.
-
  #### ID
  GN-FRPD-ANT-FICHA-IDI
  #### Cpt
  Ficha IDI (año presupuestario 2025).
  #### Src
  - Se descarga desde BIP con código de proyecto.
  #### Ctx
  - Etapa de ejecución.
  #### Req
  - Cargar asignación presupuestaria completa.
  - Registrar cofinanciamiento y fuentes.
  - Monto total coherente con presupuesto y oficio.
  - Es el único antecedente impreso, pero también debe estar cargado en BIP.
-
  #### ID
  GN-FRPD-ANT-ANEXO-1-FORM
  #### Cpt
  Anexo 1 – Formulario de Postulación FRPD.
  #### Purp
  - Documento metodológico que fundamenta la iniciativa.
  #### Src
  - Disponible en página web del GORE Ñuble.
  #### Rec
  - Se sugiere usar Metodología de Marco Lógico.
  #### Ctx
  - Debe ubicarse en carpeta 'Estudio Preinversional' en BIP.
-
  #### ID
  GN-FRPD-ANT-ANEXO-2-PRESUPUESTO
  #### Cpt
  Anexo 2 – Presupuesto.
  #### Req
  - Formato PDF y Excel en BIP.
  - Desglose máximo coherente con MML, IVA incluido, sin gastos generales ni utilidades.
  #### Facultades GORE
  - El GORE puede solicitar análisis de precios unitarios (APU).
  #### Cond
  - Cofinanciamiento requiere V°B° de Unidad Financiera.
  #### Clasificador Presupuestario
  - Contratación de programa: actividades principales (RRHH, materiales, etc.), sugerido entre 70–95% del total.
  - Consultoras: externalización de servicios, no puede ser mayor a 'Contratación de Programas'.
  - Gastos administrativos: hasta 5% del total; incluye combustible, materiales de oficina y garantías (privados).
  #### Prohib
  - Cargar viáticos, alimentación, pasajes, peajes o estacionamiento al FRPD.
  #### Clasificacion SISREC
  - Inversión: adquisición de activos y otros sin contraprestación directa (asociado a contratación de programa).
  - Operación: gastos de bienes de consumo y otros para funcionamiento (asociados a gastos administrativos).
  - Recursos Humanos: remuneraciones (asociadas a consultorías).
  #### Imputacion Transferencia
  - Corriente: si gasto asimilable a subtítulos 21, 22, 24 > 50% del total.
  - De Capital: si gasto asimilable a subtítulos 29, 31, 33 > 50% del total.
-
  #### ID
  GN-FRPD-ANT-ANEXO-3-PERFILES
  #### Cpt
  Anexo 3 – Perfiles y descripción de cargo.
  #### Req
  - Describir perfiles, funciones, número de horas y formato de contratación.
  - Universidades estatales deben adjuntar declaración jurada simple del Rector con horas disponibles de académicos.
  - Adjuntar certificado de que personas a contratar no pertenecen a la institución (cuando corresponda).
-
  #### ID
  GN-FRPD-ANT-ANEXO-4-COTIZ-TDR
  #### Cpt
  Anexo 4 – Cotizaciones y/o Términos de Referencia (TDR).
  #### Req
  - Al menos 1 cotización por activo, con antigüedad ≤ 60 días, fecha, RUT del proveedor y precio.
  - TDR detallados para licitaciones (fechas, dimensiones, especificaciones técnicas).
  #### Ctx
  - Ubicación en BIP: carpeta 'Especificaciones Técnicas'.
-
  #### ID
  GN-FRPD-ANT-ANEXO-5-DECL-SIN-REND
  #### Cpt
  Anexo 5 – Declaración jurada simple (sin rendiciones pendientes).
  #### Src
  - Disponible en página web del GORE Ñuble.
  #### Req
  - Firma del representante legal.
-
  #### ID
  GN-FRPD-ANT-ANEXO-6-ESTATUTOS
  #### Cpt
  Anexo 6 – Decreto o Estatutos de creación del servicio.
  #### Purp
  - Acreditar que el objeto social se relaciona con el programa.
  #### Rec
  - Adjuntar aprobación técnica de SES o DIPRES si existe.
-
  #### ID
  GN-FRPD-ANT-ANEXO-7-PERSONERIA
  #### Cpt
  Anexo 7 – Personería del representante legal.
  #### Purp
  - Acreditar quién firmará el convenio.
-
  #### ID
  GN-FRPD-ANT-ANEXO-8-RESUMEN-EJEC
  #### Cpt
  Anexo 8 – Resumen Ejecutivo.
  #### Src
  - Disponible en página web del GORE Ñuble.
  #### Req
  - Apéndice con objetivos, descripción y montos.
  #### Ctx
  - Ubicación en BIP: carpeta 'Anexos'.
-
  #### ID
  GN-FRPD-ANT-OTROS-ANEXOS
  #### Cpt
  Otros anexos.
  #### Cond
  - Compromiso de financiamiento compartido: certificado de Dirección de Finanzas.
  - Postulación de Universidad Estatal: certificado de acreditación de la CNA.
  - Derechos de Autor: declaración jurada sobre plagio, si aplica.
#### Procedimiento Evaluacion Tecnica y RATE
#### ID
GN-FRPD-EVAL-PROCEDIMIENTO-01
#### Resp
- Unidad de Proyectos y Programas de la DIPIR-GORE Ñuble.
#### Func
- Revisión técnica y recomendación de iniciativas.
#### Res
- Acta de evaluación con asignación de RATE.
#### Tipos RATE
#### RS
#### ID
GN-FRPD-RATE-RS-01
#### Cpt
RS – Recomendado Favorablemente.
#### Res
- Otorga aprobación técnica.
#### Req
- Certificado RS, acta de evaluación, presupuesto final, ficha IDI y oficio conductor.
#### Contenido Certificado RS
- Listado de beneficiarios.
- Comuna o territorio.
- Monto FNDR y otros aportes.
- Antecedentes de la institución postulante.
- Producto esperado.
- Objetivo esperado.
- Coherencia con carácter regional del FNDR.
#### Vigencia
- Año de obtención + 2 años calendario siguientes, si no hay cambios sustantivos.
#### FI
#### ID
GN-FRPD-RATE-FI-01
#### Cpt
FI – Falta de Información.
#### Def
- Antecedentes insuficientes, errores o necesidad de actualización.
#### OT
#### ID
GN-FRPD-RATE-OT-01
#### Cpt
OT – Objetado técnicamente.
#### Def
- Iniciativa mal formulada o con problemas técnicos/administrativos/normativos insalvables.
#### NV
#### ID
GN-FRPD-RATE-NV-01
#### Cpt
NV – No Vigente.
#### Causa
- Incumplimiento de plazos para subsanar observaciones.
- Financiamiento por otra fuente.
- Desistimiento.
- Incompatibilidades normativas.
#### Res
- Término del proceso de evaluación para el año presupuestario.
### Sec 9 Comunicacion Resultados
#### ID
GN-FRPD-SEC-9-COMUNICACION
#### Canales
#### ID
GN-FRPD-COMUNICACION-CANALES-01
#### Medio Principal
- Publicación en página web del GORE Ñuble ([www.goredenuble.cl](www.goredenuble.cl)).
#### Medio Secundario
- Comunicación vía correo electrónico a coordinadores de iniciativas desde difoi.nuble@goredenuble.cl.
### Sec 10 Ejecucion Iniciativas
#### ID
GN-FRPD-SEC-10-EJECUCION
#### Solicitud Financiamiento
#### ID
GN-FRPD-EJEC-SOLICITUD-01
#### Act
- Departamento de Análisis y Evaluación emite reporte semanal al Gobernador y Jefe de División de Presupuesto con iniciativas aprobadas.
#### Proc Aprobacion
- > 7.000 UTM: aprobación del Consejo Regional.
- <= 7.000 UTM: toma de conocimiento del Consejo Regional.
#### Proc Post Aprobacion
- Departamento de Presupuesto elabora resolución y solicita creación presupuestaria a DIPRES.
#### Elaboracion Convenio
#### ID
GN-FRPD-EJEC-CONVENIO-01
#### Ctx
- Inicia una vez emitida la resolución de DIPRES.
#### Resp
- Departamento de Presupuestos del GORE.
#### Req
- Firma del representante legal del servicio beneficiado.
#### Transferencia Recursos
#### ID
GN-FRPD-EJEC-TRANSFERENCIAS-01
#### Cond
- Según Ley de Presupuestos, programación financiera y avance efectivo del programa.
#### Req
- Cuenta corriente exclusiva para recursos FNDR.
#### Seguimiento Iniciativa
#### ID
GN-FRPD-EJEC-SEGUIMIENTO-01
#### Resp
- División Patrocinante del GORE.
#### Obj
- Seguimiento técnico y financiero.
#### Reevaluaciones
#### ID
GN-FRPD-EJEC-REEVAL-01
#### Def
- Nuevo análisis frente a cambios significativos.
#### Ctx
- Aplica sólo a iniciativas con obras civiles.
#### Prohib
- No aplica a estudios ni programas.
#### Proc
- Modificaciones requieren ingreso de oficio al Gobernador para evaluación.
### Sec 11 Propiedad Intelectual
#### ID
GN-FRPD-SEC-11-PROPIEDAD
#### Reconocimiento
#### ID
GN-FRPD-PROPIEDAD-RECONOC-01
#### Cpt
- Propiedad intelectual de inventos e innovaciones según Ley 17.336 y 19.039.
#### Entidad Encargante
- El GORE Ñuble se considera quien encarga el servicio.
#### Compromiso GORE
- No perseguirá fines lucrativos con los resultados.
- No entregará información a terceros sin autorización expresa de la institución.
#### Propiedad Industrial
- Aplica el mismo régimen que para propiedad intelectual.
### Sec 12 Compromiso Gobierno Regional
#### ID
GN-FRPD-SEC-12-COMPROMISO-GORE
#### Compromiso
#### ID
GN-FRPD-COMPROMISO-01
#### Cpt
- Transferir recursos asignados según proyecto aprobado y programación financiera.
#### Condiciones Suspensivas
#### ID
GN-FRPD-COND-SUSPENSIVAS-01
#### Cond
- Existencia y disponibilidad de recursos en el presupuesto del GORE.
- No existencia de rebajas presupuestarias del Gobierno Central; en caso contrario, plazos y montos podrán modificarse.
### Sec 13 Garantias
#### ID
GN-FRPD-SEC-13-GARANTIAS
#### Ambito
#### ID
GN-FRPD-GARANTIAS-AMBITO-01
#### Ctx
- Aplica sólo a instituciones privadas.
#### Fnd
- Res. 30 CGR; Oficio Circular N°20 Ministerio de Hacienda; Dictamen N°15.978/10 CGR.
#### Reglas Garantias
#### ID
GN-FRPD-GARANTIAS-REGLAS-01
#### Req
- Obligatoria para transferencias > 1.000 UTM.
#### Purp
- Velar por el cumplimiento de obligaciones del convenio.
#### Instrumentos
- Boletas de garantía.
- Vales vista.
- Otros instrumentos de cobro inmediato.
#### Monto Minimo
- 5% del total transferido (Art. 25 Ley N° 21.796).
#### Financiamiento Garantia
- Puede cargarse al ítem de 'Gastos Administrativos'.
#### Vigencia
- Mínimo 90 días posteriores al término de la iniciativa; se extiende si hay ampliación de plazo.
### Sec 14 Otros Aspectos
#### ID
GN-FRPD-SEC-14-OTROS
#### Transparencia y Comunicaciones
#### ID
GN-FRPD-OTROS-TRANSP-01
#### Cpt
- Normas gráficas de la Unidad de Comunicaciones del GORE aplican a todas las iniciativas.
#### Act
- Publicación mensual en la web del GORE de la cartera de proyectos ingresados y con convenio.
#### Req Instituciones Privadas
- Al postular: sitio web con información de la institución, directorio y representante legal; publicar estados financieros, balance y memoria anual (especialmente si adjudica > 2.000 UTM).
- Durante ejecución: banner en web institucional con información de la iniciativa, convenio, avances, etc.
#### Rendiciones de Cuenta
#### ID
GN-FRPD-OTROS-RENDICIONES-01
#### Req
- Documentos originales para rendición.
- Listados de participación con firmas en fresco o digitales.
#### Uso SISREC
#### ID
GN-FRPD-OTROS-SISREC-01
#### Req
- Rendir cuentas vía SISREC (Art. 24 Ley N° 21.796).
#### Resp
- Órgano público que transfiere los fondos es responsable del uso de SISREC.
#### Obligacion Restituir Fondos
#### ID
GN-FRPD-OTROS-RESTITUCION-01
#### Causa
- Uso de recursos en finalidad distinta a la autorizada.
- Fondos no utilizados.
- Fondos observados por contraparte GORE o Unidad de Control.
#### Ctx
- La obligación de restituir es distinta de la garantía de fiel cumplimiento.
#### Contrapartes Tecnicas
#### ID
GN-FRPD-OTROS-CONTRAPARTES-01
#### Cpt
- Contraparte postulante: persona responsable de la iniciativa informada antes del convenio; si no existe, se debe presupuestar su contratación.
- Contraparte GORE: nombrada según Resolución Exenta N°162 del 15/02/2023.
#### Proc Coordinacion
- Se busca un flujo ágil; las instituciones deben canalizar la información mediante una contraparte.
- Para difusión, coordinar con Depto. de Comunicaciones o Gabinete del GORE.
#### Acreditar Objeto Social
#### ID
GN-FRPD-OTROS-OBJETO-SOCIAL-01
#### Req
- Los convenios deben mencionar expresamente el objeto social de la institución privada.
- Acreditar objeto social pertinente a la actividad mediante documentación adjunta.
#### Facultades Supervision
#### ID
GN-FRPD-OTROS-SUPERVISION-01
#### Cpt
- GORE y Consejo Regional pueden supervisar iniciativas en ejecución y ex post (Ley N°19.175).
#### Proc
- Dudas o interpretaciones sobre la guía serán resueltas por el GORE.
#### Contratacion Funcionarios Universidades
#### ID
GN-FRPD-OTROS-UNIVERSIDADES-01
#### Req
- Universidades deben adjuntar declaración jurada simple del Rector con detalle de horas disponibles de académicos/investigadores para I+D.
#### Cond
- Las horas no deben traslaparse con actividades y horarios regulares de la universidad.
#### Norma Supletoria
#### ID
GN-FRPD-OTROS-NORMA-SUPLETORIA-01
#### Cpt
- Aspectos no cubiertos en esta guía se rigen por Guía Base FNDR (Res. Ex. N°83/2024), Normas de Inversión Pública y normativa legal vigente.
#### Proteccion Datos Personales
#### ID
GN-FRPD-OTROS-DATOS-01
#### Fnd
- Ley N° 19.628 y sus modificaciones.
#### Req
- El postulante debe adoptar medidas técnicas y organizativas para asegurar confidencialidad, integridad y disponibilidad de datos personales.
#### Derechos Titulares
- Acceso, rectificación, supresión, oposición y portabilidad.
#### Normativa Especifica FRPD
#### ID
GN-FRPD-OTROS-NORMATIVA-ESPECIFICA-01
#### Cpt
- Regulación adicional podrá establecerse por decretos supremos del Ministerio de Hacienda (Ley N° 21.591).
#### Ctx
- Estas bases se entienden complementadas por dicha normativa una vez publicada.

## Formulario FRPD Application 2025
### ID
GN-FRPD-FORM-APPLICATION-2025-01
### Purp
Definir los campos obligatorios y estructura del formulario de postulación FRPD 2025.
### Ctx
- Deriva directamente del bloque FORM-GN-FRPD-APPLICATION-2025-01 del documento fuente.
### Seccion 1 Identificacion Iniciativa
#### ID
GN-FRPD-FORM-SEC1-IDENT
#### Campos
-
  #### ID
  GN-FRPD-FORM-COD-BIP
  #### Field Label
  Código BIP
  #### Field Type
  Text
  #### Field Constraint
  Req: mandatory.
-
  #### ID
  GN-FRPD-FORM-NOMBRE-PROGRAMA
  #### Field Label
  Nombre del Programa
  #### Field Type
  Text
  #### Field Constraint
  Req: mandatory.
-
  #### ID
  GN-FRPD-FORM-MONTO-FNDR
  #### Field Label
  Monto solicitado FNDR
  #### Field Type
  Number
  #### Field Constraint
  Req: mandatory. Min-Val: 0.
-
  #### ID
  GN-FRPD-FORM-MONTO-TOTAL
  #### Field Label
  Monto total del Programa
  #### Field Type
  Number
  #### Field Constraint
  Req: mandatory. Min-Val: 0.
-
  #### ID
  GN-FRPD-FORM-PLAZO-MESES
  #### Field Label
  Plazo de ejecución (meses)
  #### Field Type
  Number
  #### Field Constraint
  Req: mandatory. Min-Val: 1. Max-Val: 30.
-
  #### ID
  GN-FRPD-FORM-EJE-ERD
  #### Field Label
  Eje ERD
  #### Field Type
  Text
  #### Field Constraint
  Req: mandatory.
-
  #### ID
  GN-FRPD-FORM-LINEAMIENTO-ERD
  #### Field Label
  Lineamiento ERD
  #### Field Type
  Text
  #### Field Constraint
  Req: mandatory.
-
  #### ID
  GN-FRPD-FORM-OBJETIVO-ERD
  #### Field Label
  Objetivo ERD
  #### Field Type
  Text
  #### Field Constraint
  Req: mandatory.
-
  #### ID
  GN-FRPD-FORM-LINEAMIENTO-POSTULA
  #### Field Label
  Lineamiento al que postula
  #### Field Type
  Checkbox-Group
  #### Field Instr
  Marcar con X el lineamiento al que postula.
  #### Field Options
  - Social
  - Asistencia técnica a municipalidades
  - Cultural
  - Salud
  - Infancia
  - Energía, transportes y telecomunicaciones
  - Medioambiente y gestión de residuos
  - Gestión de recursos hídricos
  - Deportes
  - Movilidad urbana
  - Cuidados de adulto mayor
  - Conectividad digital
  - Emergencia
  - Fomento productivo, emprendimiento, innovación
  - Seguridad pública
  - Atracción de inversiones
### Seccion 2 Institucion Postulante
#### ID
GN-FRPD-FORM-SEC2-INSTITUCION
#### Campos
| ID | Field-Label | Field-Type | Field-Constraint |
| --- | --- | --- | --- |
| GN-FRPD-FORM-INSTITUCION | Institución o Servicio Postulante | Text | Req: mandatory. |
| GN-FRPD-FORM-REP-LEGAL | Representante Legal | Text | Req: mandatory. |
| GN-FRPD-FORM-RESP-FORMULACION | Responsable de la formulación | Text | Req: mandatory. |
| GN-FRPD-FORM-CONTACTO-FORMULADOR | Correo y teléfono formulador | Text | Req: mandatory. Format: email. |
| GN-FRPD-FORM-ANTECEDENTES-MISION | Antecedentes y Misión Institucional | TextArea | Req: mandatory. |
| GN-FRPD-FORM-NOMBRE-INSTRUMENTO | Nombre del instrumento o programa a utilizar | Text | Req: mandatory. |
| GN-FRPD-FORM-DESC-INSTRUMENTO | Descripción del instrumento o programa a utilizar | TextArea | Req: mandatory. |
| GN-FRPD-FORM-MARCO-LEGAL-PROGRAMA | Marco Legal para operar y realizar el programa | TextArea | Req: mandatory. |
| GN-FRPD-FORM-FUNDAMENTO-TRANSFERENCIA | Fundamento de la solicitud de transferencia a la institución | TextArea | Req: mandatory. |
| GN-FRPD-FORM-N-PROGRAMAS-EJEC | N° de programas en ejecución con Gobierno Regional | Number | Req: mandatory. Min-Val: 0. |
| GN-FRPD-FORM-SALDO-POR-RENDIR | Saldo por rendir programas en ejecución (a la fecha de postulación) | Number | Req: mandatory. Min-Val: 0. |
### Seccion 3 Diagnostico
#### ID
GN-FRPD-FORM-SEC3-DIAGNOSTICO
#### Campos
-
  #### ID
  GN-FRPD-FORM-ANALISIS-INVOLUCRADOS
  #### Field Label
  Análisis de los involucrados
  #### Field Type
  Static-Text
-
  #### ID
  GN-FRPD-FORM-DESC-GRUPO-OBJETIVO
  #### Field Label
  Descripción del grupo objetivo
  #### Field Type
  TextArea
  #### Field Instr
  Identificar beneficiarios directos e indirectos en todos los niveles.
  #### Field Constraint
  Req: mandatory.
-
  #### ID
  GN-FRPD-FORM-TERRITORIO-INTERVENIR
  #### Field Label
  Territorio a intervenir
  #### Field Type
  Text
  #### Field Constraint
  Req: mandatory.
-
  #### ID
  GN-FRPD-FORM-PROY-ANTERIORES
  #### Field Label
  Identificación de proyectos o programas anteriores destinados al grupo objetivo (FNDR o Sectorial).
  #### Field Type
  TextArea
-
  #### ID
  GN-FRPD-FORM-ANALISIS-BENEFICIARIOS
  #### Field Label
  Análisis de los beneficiarios
  #### Field Type
  Static-Text
-
  #### ID
  GN-FRPD-FORM-REQ-BENEFICIARIO
  #### Field Label
  Requisitos específicos para calificar como beneficiario
  #### Field Type
  TextArea
  #### Field Constraint
  Req: mandatory.
-
  #### ID
  GN-FRPD-FORM-PROC-SELECCION-BENEF
  #### Field Label
  Descripción del procedimiento de selección de beneficiarios
  #### Field Type
  TextArea
  #### Field Constraint
  Req: mandatory.
-
  #### ID
  GN-FRPD-FORM-BENEFICIOS-INDIVIDUALES
  #### Field Label
  Beneficios a recibir por beneficiario individual
  #### Field Type
  TextArea
  #### Field Constraint
  Req: mandatory.
-
  #### ID
  GN-FRPD-FORM-N-ESTIMADO-BENEF
  #### Field Label
  Numero estimado de beneficiarios (por grupo objetivo y género)
  #### Field Type
  Text
  #### Field Constraint
  Req: mandatory.
-
  #### ID
  GN-FRPD-FORM-ANALISIS-PROBLEMA
  #### Field Label
  Análisis del Problema
  #### Field Type
  Static-Text
-
  #### ID
  GN-FRPD-FORM-IDENTIFICACION-PROBLEMA
  #### Field Label
  Identificación del problema (problemas principales de la situación)
  #### Field Type
  TextArea
  #### Field Constraint
  Req: mandatory.
-
  #### ID
  GN-FRPD-FORM-DEFINICION-PROBLEMA-CENTRAL
  #### Field Label
  Definición del problema central (aplicando prioridad y selectividad)
  #### Field Type
  TextArea
  #### Field Constraint
  Req: mandatory.
-
  #### ID
  GN-FRPD-FORM-EFECTOS-PROBLEMA
  #### Field Label
  Efectos del problema (definir los más importantes)
  #### Field Type
  TextArea
  #### Field Constraint
  Req: mandatory.
-
  #### ID
  GN-FRPD-FORM-CAUSAS-PROBLEMA
  #### Field Label
  Causas del problema (elementos que lo provocan)
  #### Field Type
  TextArea
  #### Field Constraint
  Req: mandatory.
-
  #### ID
  GN-FRPD-FORM-ARBOL-PROBLEMAS
  #### Field Label
  Árbol de problemas (diagrama Causa-Efecto)
  #### Field Type
  File
  #### Field Instr
  Construir y presentar árbol de problemas. El árbol debe dar una imagen completa de la situación negativa. Verificar validez e integridad.
  #### Field Constraint
  Req: mandatory.
-
  #### ID
  GN-FRPD-FORM-ARBOL-OBJETIVOS
  #### Field Label
  Diagrama de árbol de soluciones (medios y fines)
  #### Field Type
  File
  #### Field Instr
  Convertir condiciones negativas a positivas. Examinar relación medio-fin. Añadir nuevos objetivos si es necesario.
  #### Field Constraint
  Req: mandatory.
### Seccion 4 Identificacion Programa
#### ID
GN-FRPD-FORM-SEC4-IDENT-PROGRAMA
#### Campos
| ID | Field-Label | Field-Type |
| --- | --- | --- |
| GN-FRPD-FORM-ESTRUCTURA-ANALITICA | Estructura Analítica del Programa | TextArea |
| GN-FRPD-FORM-ARBOL-OBJETIVOS-SEL | Árbol de objetivos (seleccionados) | File |
| GN-FRPD-FORM-ESTRUCTURA-PROGRAMA | Estructura del Programa | TextArea |
| GN-FRPD-FORM-OBJ-GENERAL | Objetivo general del programa | TextArea |
| GN-FRPD-FORM-PRODUCTOS-ENTREGAR | Productos que se entregarán | TextArea |
| GN-FRPD-FORM-RESULTADOS-ESPERADOS | Resultados esperados | TextArea |
### Seccion 5 Matriz Marco Logico
#### ID
GN-FRPD-FORM-SEC5-MML
#### Campos
| ID | Field-Label | Field-Type | Field-Instr |
| --- | --- | --- | --- |
| GN-FRPD-FORM-MATRIZ-MML | Matriz de Marco Lógico | Repeater | Completar la matriz para cada nivel: Fin, Propósito, Componentes y Actividades. |
### Seccion 6 Operatividad Programa
#### ID
GN-FRPD-FORM-SEC6-OPERATIVIDAD
#### Campos
| ID | Field-Label | Field-Type | Field-Instr | Field-Constraint |
| --- | --- | --- | --- | --- |
| GN-FRPD-FORM-ETAPA-PLANIFICACION-CONTROL | Etapa de Planificación y Control | File | Incorporar carta Gantt de actividades y financiera. | Req: mandatory. |
### Seccion 7 Presupuesto
#### ID
GN-FRPD-FORM-SEC7-PRESUPUESTO
#### Campos
-
  #### ID
  GN-FRPD-FORM-PRESUPUESTO-TITULO
  #### Field Label
  Presupuesto
  #### Field Type
  Static-Text
-
  #### ID
  GN-FRPD-FORM-PRESUPUESTO-DETALLADO
  #### Field Label
  Presupuesto Detallado
  #### Field Type
  Repeater
  #### Field Instr
  Añadir una fila por cada ítem del presupuesto.
-
  #### ID
  GN-FRPD-FORM-RESUMEN-PRESUP-CLASIF-PRESUP
  #### Field Label
  Resumen Presupuesto (por Clasificación Presupuestaria)
  #### Field Type
  Repeater
-
  #### ID
  GN-FRPD-FORM-RESUMEN-PRESUP-CLASIF-SISREC
  #### Field Label
  Resumen Presupuesto (por Clasificación SISREC)
  #### Field Type
  Repeater
-
  #### ID
  GN-FRPD-FORM-DETALLE-CONTRATACION-PERSONAS
  #### Field Label
  Detalle Contratación de Personas
  #### Field Type
  Repeater
-
  #### ID
  GN-FRPD-FORM-DETALLE-DIFUSION-HITOS
  #### Field Label
  Detalle actividades difusión e hitos comunicacionales
  #### Field Type
  Repeater
### Seccion 8 Resumen Programa
#### ID
GN-FRPD-FORM-SEC8-RESUMEN
#### Campos
-
  #### ID
  GN-FRPD-FORM-RESUMEN-PROGRAMA
  #### Field Label
  Resumen del Programa
  #### Field Type
  TextArea
  #### Field Constraint
  Req: mandatory. Max-Len: 3000.
  #### Field Instr
  ¾ de hoja máximo.
-
  #### ID
  GN-FRPD-FORM-FIRMA-FORMULADOR
  #### Field Label
  Nombre, firma y timbre del Formulador
  #### Field Type
  Signature
  #### Field Constraint
  Req: mandatory.
-
  #### ID
  GN-FRPD-FORM-FIRMA-REPRESENTANTE
  #### Field Label
  Nombre, firma y timbre del jefe de Servicio o Representante
  #### Field Type
  Signature
  #### Field Constraint
  Req: mandatory.
-
  #### ID
  GN-FRPD-FORM-CONTACTO-FORMULADOR-FINAL
  #### Field Label
  Fono y Mail del formulador
  #### Field Type
  Text
  #### Field Constraint
  Req: mandatory.
