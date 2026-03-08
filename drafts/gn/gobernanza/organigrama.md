---
_manifest:
  urn: urn:gn:kb:organigrama
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/01_fundamentos/intro/kb_gn_002_organigrama_koda.yml; ontologies/onto_gorenuble/goreNubleOrgData.ttl
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- organigrama
- institucional
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/01_fundamentos/intro/kb_gn_002_organigrama_koda.yml
    - ontologies/onto_gorenuble/goreNubleOrgData.ttl
    source_hashes:
      domains/gn/01_fundamentos/intro/kb_gn_002_organigrama_koda.yml: 7b2c3c0ca3bf951a0d091021bfc7b8a4561e2cd99b10d89982535a8cf29f3435
      ontologies/onto_gorenuble/goreNubleOrgData.ttl: f15a877cfd6af0118b1cdb93aafd1391f4b8d956e7f001eb74f5b1dd09019cf1
    source_type: mixed
    transformation_mode: korafy_composite
    fs: 100
    cr: 1.47
    run_id: gn-smoke
    review_gate: manual
    scope_statement: Organigrama operativo y estructura organica observables en la
      fuente KODA y el slice TTL organizacional.
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 15
    meat_count: 795
    fat_count: 0
    preserved_facts:
    - Creation-Date=2026-01-26
    - Ctx=Organigrama institucional del Gobierno Regional de Ñuble (versión 2026).
    - Human-Creator=FSA
    - Human-Editor=FSA
    - ID=KB-GN-002-ORGANIGRAMA-01
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
    - Model-Collaborator=GPT-5.2
    - Modification-Date=2026-01-26
    - Organigrama_Institucional_GORE_Nuble.Ctx[0]=Contenido redactado como descripciones
      funcionales (no incluye dotación/cargos específicos).
    - Organigrama_Institucional_GORE_Nuble.Ctx[1]=Orden de unidades preserva el orden
      del documento fuente.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Act[0]=Supervisar
      elaboración y ejecución del presupuesto.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Act[1]=Gestionar
      registro contable y elaboración de estados financieros.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Act[2]=Analizar
      situación económica para toma de decisiones.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Act[3]=Implementar
      políticas de control para seguridad de activos.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Act[4]=Optimizar
      uso de recursos.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.ID=GN-ORG-DEP-FINANZAS-01
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Purp=Revisión
      y control de información presupuestaria, contable y financiera.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Res=Garante
      de salud financiera y transparencia institucional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Adquisiciones.Act[0]=Ejecutar
      procesos de adquisiciones de bienes y servicios necesarios para funcionamiento
      institucional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Adquisiciones.Act[1]=Publicar
      y monitorear contrataciones especialmente encomendadas provenientes del programa
      de inversiones, junto a unidad técnica designada.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Adquisiciones.ID=GN-ORG-UNID-ADQ-01
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Adquisiciones.Obj[0]=Eficiencia.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Adquisiciones.Obj[1]=Transparencia.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Adquisiciones.Obj[2]=Probidad.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Adquisiciones.Purp=Procesos
      de compras de bienes y servicios.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Adquisiciones.Req[0]=Apego
      a Ley de Compras Públicas y su reglamento.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Contabilidad_y_Finanzas.Act[0]=Registrar,
      controlar y analizar información contable y presupuestaria.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Contabilidad_y_Finanzas.Act[1]=Resguardar
      integridad de datos financieros y contables.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Contabilidad_y_Finanzas.ID=GN-ORG-UNID-CONTAB-FIN-01
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Contabilidad_y_Finanzas.Purp=Registro,
      control y análisis de información contable y presupuestaria.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Contabilidad_y_Finanzas.Res[0]=Permite
      gestión alineada con normativas vigentes y buenas prácticas del sector público.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Control_de_Rendiciones.Act[0]=Seguimiento,
      monitoreo, control y contabilización de rendiciones de cuentas ingresadas al
      Gobierno Regional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Control_de_Rendiciones.Act[1]=Asegurar
      uso de recursos conforme a normativa vigente, de forma eficiente, transparente
      y oportuna.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Control_de_Rendiciones.ID=GN-ORG-UNID-RENDICIONES-01
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Control_de_Rendiciones.Purp=Seguimiento
      y control de rendiciones de cuentas.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Control_de_Rendiciones.Res[0]=Resguarda
      correcta administración de fondos públicos.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Operaciones.Act[0]=Gestionar
      infraestructura física (edificios e instalaciones) y flota de vehículos institucionales.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Operaciones.Act[1]=Coordinar
      mantenimiento preventivo, correctivo y respuesta a emergencias.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Operaciones.Act[2]=Asegurar
      operatividad, funcionalidad y seguridad de recursos físicos institucionales.
    - 'Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Operaciones.Act[3]=Gestionar
      y mantener infraestructura TI: red, servidores, hardware, software, sistemas
      de información.'
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Operaciones.Act[4]=Gestionar
      políticas de seguridad informática y protección de datos institucionales.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Operaciones.Act[5]=Desarrollar
      soluciones tecnológicas alineadas con objetivos estratégicos del Gobierno Regional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Operaciones.ID=GN-ORG-UNID-OPERACIONES-01
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Operaciones.Purp=Infraestructura
      física, flota vehicular y tecnologías de la información.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Operaciones.Src[0]=Ley
      de Transformación Digital.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Tesoreria.Act[0]=Administrar,
      controlar y custodiar ingresos y egresos del Gobierno Regional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Tesoreria.Act[1]=Gestionar
      fondos institucionales, pagos y flujo de caja.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Tesoreria.Act[2]=Velar
      por liquidez y estabilidad financiera.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Tesoreria.ID=GN-ORG-UNID-TESORERIA-01
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Tesoreria.Purp=Administración
      y custodia de ingresos y egresos; pagos y flujo de caja.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Tesoreria.Res[0]=Asegura
      cumplimiento de obligaciones financieras.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Finanzas.Unidades_Dependientes.Unidad_de_Tesoreria.Res[1]=Asegura
      eficiencia en ejecución presupuestaria.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Gestion_y_Desarrollo_de_Personas.Act[0]=Definir,
      elaborar e implementar estrategias, políticas y procesos institucionales de
      gestión de personas.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Gestion_y_Desarrollo_de_Personas.Act[1]=Asegurar
      equipo humano competente, motivado y alineado con objetivos de desarrollo regional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Gestion_y_Desarrollo_de_Personas.ID=GN-ORG-DEP-GDP-01
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Gestion_y_Desarrollo_de_Personas.Purp=Estrategias,
      políticas y procesos del ciclo de vida laboral del personal.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Gestion_y_Desarrollo_de_Personas.Req[0]=Concordancia
      con lineamientos de la autoridad regional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Gestion_y_Desarrollo_de_Personas.Req[1]=Concordancia
      con normativa vigente aplicable al sector público.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Departamento_de_Gestion_y_Desarrollo_de_Personas.Req[2]=Concordancia
      con instrumentos de gestión de personas del Estado.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Oficina_de_Partes.Act[0]=Recepción,
      distribución, archivo, registro y despacho de documentación de entrada y salida
      de servicios administrativos del Gobierno Regional de Ñuble.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Oficina_de_Partes.Act[1]=Gestión
      de otras materias propias de su naturaleza y/o encomendadas o delegadas.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Oficina_de_Partes.ID=GN-ORG-OF-PARTES-01
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Componentes.Oficina_de_Partes.Purp=Gestión
      documental institucional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.ID=GN-ORG-DIV-ADAF-01
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Purp=Gestión
      administrativa y financiera; presupuesto de funcionamiento; servicios generales;
      personal.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Res=Sustenta
      funcionamiento eficiente y transparente del Gobierno Regional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Src[0]=Ley
      N.º 19.175.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Administracion_y_Finanzas.Src[1]=Ley
      N.º 18.834.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Desarrollo_Social_y_Humano.Act[0]=Definir
      e implementar lineamientos estratégicos de inversión social.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Desarrollo_Social_y_Humano.Act[1]=Diseñar,
      ejecutar y dar seguimiento a políticas regionales, programas y proyectos sociales.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Desarrollo_Social_y_Humano.Componentes.Departamento_de_Fondos_Concursables_y_Programas_Sociales.Act[0]=Planificar,
      coordinar, gestionar y supervisar inversión social mediante fondos concursables
      y programas sociales.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Desarrollo_Social_y_Humano.Componentes.Departamento_de_Fondos_Concursables_y_Programas_Sociales.Act[1]=Asegurar
      asignación eficiente, transparente y pertinente de recursos públicos.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Desarrollo_Social_y_Humano.Componentes.Departamento_de_Fondos_Concursables_y_Programas_Sociales.Act[2]=Promover
      iniciativas con impacto social, pertinencia territorial y enfoque de derechos.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Desarrollo_Social_y_Humano.Componentes.Departamento_de_Fondos_Concursables_y_Programas_Sociales.Act[3]=Articular
      trabajo con municipios, servicios públicos, organizaciones de la sociedad civil
      y otras entidades ejecutoras.
    - 'Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Desarrollo_Social_y_Humano.Componentes.Departamento_de_Fondos_Concursables_y_Programas_Sociales.Act[4]=Velar
      por ciclo de vida de iniciativas: diseño, evaluación, ejecución, seguimiento
      y cierre.'
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Desarrollo_Social_y_Humano.Componentes.Departamento_de_Fondos_Concursables_y_Programas_Sociales.ID=GN-ORG-DEP-FCPS-01
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Desarrollo_Social_y_Humano.Componentes.Departamento_de_Fondos_Concursables_y_Programas_Sociales.Purp=Gestión
      de fondos concursables y programas sociales.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Desarrollo_Social_y_Humano.Componentes.Departamento_de_Fondos_Concursables_y_Programas_Sociales.Req[0]=Coherencia
      con Estrategia Regional de Desarrollo, políticas públicas vigentes y prioridades
      definidas por el Gobierno Regional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Desarrollo_Social_y_Humano.Componentes.Departamento_de_Gestion_Territorial.Act[0]=Actuar
      como nexo de vinculación estratégica entre el Gobierno Regional de Ñuble y las
      personas de la región.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Desarrollo_Social_y_Humano.Componentes.Departamento_de_Gestion_Territorial.Act[1]=Fortalecer
      desarrollo social y comunitario.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Desarrollo_Social_y_Humano.Componentes.Departamento_de_Gestion_Territorial.Act[2]=Asegurar
      pertinencia territorial de actividades.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Desarrollo_Social_y_Humano.Componentes.Departamento_de_Gestion_Territorial.Act[3]=Contribuir
      a priorización de inversión regional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Desarrollo_Social_y_Humano.Componentes.Departamento_de_Gestion_Territorial.Act[4]=Realizar
      seguimiento técnico de cartera de inversión social de la división.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Desarrollo_Social_y_Humano.Componentes.Departamento_de_Gestion_Territorial.ID=GN-ORG-DEP-GT-01
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Desarrollo_Social_y_Humano.Componentes.Departamento_de_Gestion_Territorial.Purp=Operativización
      y despliegue territorial de oferta programática.
    - 'Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Desarrollo_Social_y_Humano.Ctx[0]=Ámbitos:
      pobreza, educación, salud, género, neurodiversidad, vivienda, entre otros.'
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Desarrollo_Social_y_Humano.Def=Eje
      de la inversión social del Gobierno Regional de Ñuble.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Desarrollo_Social_y_Humano.ID=GN-ORG-DIV-DSH-01
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Desarrollo_Social_y_Humano.Obj[0]=Promover
      equidad territorial.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Desarrollo_Social_y_Humano.Obj[1]=Promover
      inclusión social.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Desarrollo_Social_y_Humano.Obj[2]=Resguardar
      dignidad humana.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Desarrollo_Social_y_Humano.Purp=Fortalecer
      desarrollo humano y reducir brechas estructurales.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Desarrollo_Social_y_Humano.Res[0]=Complementa
      y fortalece acción del Estado en la región.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Fomento_e_Industria.Act[0]=Proponer,
      promover y ejecutar planes y programas regionales para estimular desarrollo
      de ciencia, tecnología e innovación y nuevas capacidades empresariales.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Fomento_e_Industria.Act[1]=Facilitar
      incorporación de nuevas tecnologías de la información para favorecer crecimiento
      sostenido, integrado y sustentable.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Fomento_e_Industria.Act[2]=Proponer
      y promover instrumentos de fomento productivo.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Fomento_e_Industria.Componentes.Departamento_de_Ciencia_Tecnologia_e_Innovacion.Act[0]=Planificar,
      diseñar e implementar estrategias de CTI.
    - 'Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Fomento_e_Industria.Componentes.Departamento_de_Ciencia_Tecnologia_e_Innovacion.Act[1]=Coordinar
      y articular actores relevantes: sector público, academia y ámbito privado.'
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Fomento_e_Industria.Componentes.Departamento_de_Ciencia_Tecnologia_e_Innovacion.Act[2]=Contribuir
      a creación de políticas públicas.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Fomento_e_Industria.Componentes.Departamento_de_Ciencia_Tecnologia_e_Innovacion.Act[3]=Fortalecer
      ecosistema regional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Fomento_e_Industria.Componentes.Departamento_de_Ciencia_Tecnologia_e_Innovacion.ID=GN-ORG-DEP-CTI-01
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Fomento_e_Industria.Componentes.Departamento_de_Ciencia_Tecnologia_e_Innovacion.Obj=Sostenibilidad
      y crecimiento económico.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Fomento_e_Industria.Componentes.Departamento_de_Ciencia_Tecnologia_e_Innovacion.Purp=Fomento
      del conocimiento, investigación y desarrollo tecnológico regional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Fomento_e_Industria.Componentes.Departamento_de_Fomento_y_Desarrollo_Productivo.Act[0]=Promover
      emprendimiento.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Fomento_e_Industria.Componentes.Departamento_de_Fomento_y_Desarrollo_Productivo.Act[1]=Diseñar
      políticas regionales de fomento y desarrollo productivo.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Fomento_e_Industria.Componentes.Departamento_de_Fomento_y_Desarrollo_Productivo.Act[2]=Ejecutar
      planes, programas e instrumentos de fomento productivo.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Fomento_e_Industria.Componentes.Departamento_de_Fomento_y_Desarrollo_Productivo.Act[3]=Lograr
      crecimiento sostenible, integrado y articulado con actores relevantes de la
      región.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Fomento_e_Industria.Componentes.Departamento_de_Fomento_y_Desarrollo_Productivo.ID=GN-ORG-DEP-FDP-01
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Fomento_e_Industria.Componentes.Departamento_de_Fomento_y_Desarrollo_Productivo.Purp=Impulso
      a economía regional y emprendimiento.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Fomento_e_Industria.ID=GN-ORG-DIV-FOMENTO-01
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Fomento_e_Industria.Purp=Fomento
      productivo, ciencia, tecnología e innovación.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Infraestructura_y_Transportes.Act[0]=Proponer,
      promover y ejecutar planes y programas regionales en infraestructura, equipamiento
      regional y transportes.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Infraestructura_y_Transportes.Componentes.Departamento_de_Ejecucion_y_Supervision_de_Proyectos_de_Inversion.Act[0]=Supervisar
      gestión eficiente de inversión regional mediante control riguroso de ejecución
      de proyectos asignados.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Infraestructura_y_Transportes.Componentes.Departamento_de_Ejecucion_y_Supervision_de_Proyectos_de_Inversion.Act[1]=Fiscalización
      técnica (física) y presupuestaria (financiera) para resguardar integridad del
      proceso.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Infraestructura_y_Transportes.Componentes.Departamento_de_Ejecucion_y_Supervision_de_Proyectos_de_Inversion.Act[2]=Coordinar
      con Contrapartes Técnicas para asegurar cumplimiento de objetivos institucionales.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Infraestructura_y_Transportes.Componentes.Departamento_de_Ejecucion_y_Supervision_de_Proyectos_de_Inversion.Act[3]=Ejecutar
      de manera directa iniciativas de inversión que le sean encomendadas (responsabilidad
      técnica y administrativa).
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Infraestructura_y_Transportes.Componentes.Departamento_de_Ejecucion_y_Supervision_de_Proyectos_de_Inversion.ID=GN-ORG-DEP-ESP-01
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Infraestructura_y_Transportes.Componentes.Departamento_de_Ejecucion_y_Supervision_de_Proyectos_de_Inversion.Purp=Supervisión
      de ejecución de proyectos de inversión regional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Infraestructura_y_Transportes.Componentes.Departamento_de_Infraestructura_y_Conectividad.Act[0]=Proponer
      y promover planes, estudios y programas regionales en coordinación con servicios
      públicos regionales.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Infraestructura_y_Transportes.Componentes.Departamento_de_Infraestructura_y_Conectividad.Act[1]=Analizar
      e identificar brechas existentes en infraestructura, transporte, movilidad y
      conectividad en distintas escalas territoriales.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Infraestructura_y_Transportes.Componentes.Departamento_de_Infraestructura_y_Conectividad.Act[2]=Entregar
      directrices para oferta de programas y servicios de conectividad.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Infraestructura_y_Transportes.Componentes.Departamento_de_Infraestructura_y_Conectividad.Act[3]=Promover
      y coordinar iniciativas para ampliar cobertura y calidad del transporte colectivo.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Infraestructura_y_Transportes.Componentes.Departamento_de_Infraestructura_y_Conectividad.Act[4]=Proponer
      iniciativas para intermovilidad segura mediante programas y obras.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Infraestructura_y_Transportes.Componentes.Departamento_de_Infraestructura_y_Conectividad.Act[5]=Evaluar
      y coordinar con otras instituciones planes de inversiones en movilidad.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Infraestructura_y_Transportes.Componentes.Departamento_de_Infraestructura_y_Conectividad.Act[6]=Estudiar
      y proponer sistemas de Transporte Inteligente.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Infraestructura_y_Transportes.Componentes.Departamento_de_Infraestructura_y_Conectividad.ID=GN-ORG-DEP-INFRA-CONECT-01
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Infraestructura_y_Transportes.Componentes.Departamento_de_Infraestructura_y_Conectividad.Purp=Infraestructura,
      transporte, movilidad y conectividad (vial y digital).
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Infraestructura_y_Transportes.ID=GN-ORG-DIV-INFRA-TRANS-01
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Infraestructura_y_Transportes.Purp=Obras
      de infraestructura y equipamiento regional; gestión en transportes.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Act[0]=Elaborar
      y proponer estrategias, políticas, planes, programas y proyectos para desarrollo
      armónico del territorio (incluye Plan Regional de Ordenamiento Territorial).
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Act[1]=Basar
      procesos en insumos técnicos y participativos, conforme a prioridades definidas
      por el gobierno regional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Act[2]=Apoyar
      al Gobernador Regional en evaluación de cumplimiento de políticas, planes, programas,
      proyectos y presupuestos de carácter regional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Act[3]=Prestar
      asistencia técnica a municipalidades y otros organismos de la administración
      que lo requieran.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Comite_de_Pertinencia_y_Vinculacion_Estrategica.Act[0]=Asesorar
      integralmente a la autoridad.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Comite_de_Pertinencia_y_Vinculacion_Estrategica.Act[1]=Analizar
      admisibilidad de proyectos postulados.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Comite_de_Pertinencia_y_Vinculacion_Estrategica.Act[2]=Analizar
      pertinencia regional con base en instrumentos de planificación regional y competencias
      determinadas en la Ley Orgánica de Gobierno y Administración Regional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Comite_de_Pertinencia_y_Vinculacion_Estrategica.Def=Instancia
      formal de asesoría y análisis de proyectos.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Comite_de_Pertinencia_y_Vinculacion_Estrategica.ID=GN-ORG-COMITE-PERTINENCIA-01
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Comite_de_Pertinencia_y_Vinculacion_Estrategica.Integrantes[0]=Administrador(a)
      Regional.
    - 'Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Comite_de_Pertinencia_y_Vinculacion_Estrategica.Integrantes[1]=Jefaturas
      de Divisiones: Planificación y Desarrollo Regional (Presidente del Comité),
      Presupuesto e Inversión Regional, Fomento e Industria, Desarrollo Social y Humano,
      Infraestructura y Transporte.'
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Departamento_Zonas_en_Desarrollo.Act[0]=Promover
      inversión pública focalizada.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Departamento_Zonas_en_Desarrollo.Act[1]=Fortalecer
      descentralización.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Departamento_Zonas_en_Desarrollo.Act[2]=Promover
      participación de actores de la sociedad.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Departamento_Zonas_en_Desarrollo.Act[3]=Promover
      desarrollo territorial integral y equilibrado con base en especificidades regionales.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Departamento_Zonas_en_Desarrollo.Ctx[0]=Enfoque
      de derechos.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Departamento_Zonas_en_Desarrollo.ID=GN-ORG-DEP-ZED-01
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Departamento_Zonas_en_Desarrollo.Purp=Acceso
      equitativo al desarrollo y fortalecimiento de descentralización.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Departamento_de_Desarrollo_de_Proyectos_Estrategicos.Act[0]=Seleccionar,
      planificar y supervisar iniciativas de alto impacto.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Departamento_de_Desarrollo_de_Proyectos_Estrategicos.Act[1]=Alinear
      operación diaria con visión de largo plazo del Gobierno Regional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Departamento_de_Desarrollo_de_Proyectos_Estrategicos.Act[2]=Facilitar
      vínculo entre visión de la autoridad regional, su Consejo y directivos.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Departamento_de_Desarrollo_de_Proyectos_Estrategicos.Act[3]=Asegurar
      contribución de proyectos a competitividad, innovación y crecimiento territorial.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Departamento_de_Desarrollo_de_Proyectos_Estrategicos.ID=GN-ORG-DEP-DPE-01
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Departamento_de_Desarrollo_de_Proyectos_Estrategicos.Purp=Gestión
      de iniciativas de alto impacto alineadas con visión regional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Departamento_de_Desarrollo_de_Proyectos_Estrategicos.Req[0]=Alineación
      con Estrategia Regional de Desarrollo.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Departamento_de_Planificacion_Estrategica_y_Ordenamiento_Territorial.Act[0]=Elaborar
      y proponer planes de desarrollo local que integren necesidades de la comunidad
      con análisis de restricciones ambientales y particularidades geofísicas del
      territorio.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Departamento_de_Planificacion_Estrategica_y_Ordenamiento_Territorial.Act[1]=Considerar
      vocación productiva distintiva de cada comuna, infraestructura existente y proyecciones
      de crecimiento futuro.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Departamento_de_Planificacion_Estrategica_y_Ordenamiento_Territorial.Act[2]=Coordinar
      formulación y seguimiento del Anteproyecto Regional de Inversión (ARI).
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Departamento_de_Planificacion_Estrategica_y_Ordenamiento_Territorial.Act[3]=Coordinar
      formulación y seguimiento del Programa Público de Inversión Regional (PROPIR).
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Departamento_de_Planificacion_Estrategica_y_Ordenamiento_Territorial.ID=GN-ORG-DEP-PEOT-01
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Departamento_de_Planificacion_Estrategica_y_Ordenamiento_Territorial.Mssn=Impulsar
      desarrollo armónico y sostenible.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Componentes.Departamento_de_Planificacion_Estrategica_y_Ordenamiento_Territorial.Purp=Planificación
      estratégica y ordenamiento territorial regional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.ID=GN-ORG-DIV-PLAN-01
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Planificacion_y_Desarrollo_Regional.Purp=Planificación
      territorial y apoyo a evaluación de políticas regionales.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Act[0]=Elaborar
      proyectos de presupuestos de inversión del gobierno regional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Act[1]=Ejecutar
      y controlar presupuesto de inversión y programas administrados por el gobierno
      regional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Act[2]=Asesorar
      al Gobernador Regional en definición de proyectos de inversión a desarrollar
      o financiar según lineamientos y prioridades de instrumentos de planificación
      regional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Analisis_y_Evaluacion.Act[0]=Evaluar
      pertinencia con lineamientos regionales.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Analisis_y_Evaluacion.Act[1]=Asesorar
      en determinación de proyectos a desarrollar.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Analisis_y_Evaluacion.Act[2]=Proporcionar
      proyectos con RS coordinando el Comité de Pertinencia y Vinculación Estratégica
      para análisis y priorización.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Analisis_y_Evaluacion.Act[3]=Establecer
      metodologías y analizar normativa técnica y presupuestaria para postulación
      a financiamiento.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Analisis_y_Evaluacion.Act[4]=Controlar
      solicitudes de financiamiento de inversión regional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Analisis_y_Evaluacion.Act[5]=Apoyar
      formulación de proyectos y programas regionales.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Analisis_y_Evaluacion.Act[6]=Coordinar
      asesoría técnica a municipalidades y otros servicios para cumplimiento del desarrollo
      regional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Analisis_y_Evaluacion.Ctx[0]=Postulación
      a financiamiento FNDR.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Analisis_y_Evaluacion.ID=GN-ORG-DEP-AE-01
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Analisis_y_Evaluacion.Purp=Revisión
      y evaluación técnica de proyectos/programas postulados.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Analisis_y_Evaluacion.Unidades_Dependientes.Unidad_de_Municipalidades_y_Conservaciones.Act[0]=Evaluar
      técnica y administrativamente proyectos de inversión local.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Analisis_y_Evaluacion.Unidades_Dependientes.Unidad_de_Municipalidades_y_Conservaciones.Act[1]=Asegurar
      viabilidad normativa y financiera.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Analisis_y_Evaluacion.Unidades_Dependientes.Unidad_de_Municipalidades_y_Conservaciones.Act[2]=Fortalecer
      gestión comunal mediante asesoría directa y capacitación externa para optimizar
      formulación de iniciativas territoriales.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Analisis_y_Evaluacion.Unidades_Dependientes.Unidad_de_Municipalidades_y_Conservaciones.Act[3]=Tramitar
      convenios, resoluciones y registro en plataformas oficiales del Estado.
    - 'Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Analisis_y_Evaluacion.Unidades_Dependientes.Unidad_de_Municipalidades_y_Conservaciones.Ctx[0]=Tipos:
      FRIL, Circular 33, PMU-PMB.'
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Analisis_y_Evaluacion.Unidades_Dependientes.Unidad_de_Municipalidades_y_Conservaciones.Def=Unidad
      dependiente del Departamento de Análisis y Evaluación.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Analisis_y_Evaluacion.Unidades_Dependientes.Unidad_de_Municipalidades_y_Conservaciones.ID=GN-ORG-UNID-MUNIC-CONS-01
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Analisis_y_Evaluacion.Unidades_Dependientes.Unidad_de_Municipalidades_y_Conservaciones.Purp=Evaluación
      de proyectos de inversión local.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Analisis_y_Evaluacion.Unidades_Dependientes.Unidad_de_Proyectos_y_Programas.Act[0]=Evaluar
      técnica y administrativamente iniciativas FNDR, programas públicos y concursos.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Analisis_y_Evaluacion.Unidades_Dependientes.Unidad_de_Proyectos_y_Programas.Act[1]=Gestionar
      admisibilidad y visación ante el Ministerio de Desarrollo Social cuando corresponda.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Analisis_y_Evaluacion.Unidades_Dependientes.Unidad_de_Proyectos_y_Programas.Act[2]=Asesorar
      a divisiones regionales, servicios, universidades y organizaciones privadas
      para correcta formulación de proyectos.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Analisis_y_Evaluacion.Unidades_Dependientes.Unidad_de_Proyectos_y_Programas.Act[3]=Ejecutar
      planes de capacitación externa.
    - 'Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Analisis_y_Evaluacion.Unidades_Dependientes.Unidad_de_Proyectos_y_Programas.Ctx[0]=Concursos:
      8%, FRPD, otros; activos no financieros.'
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Analisis_y_Evaluacion.Unidades_Dependientes.Unidad_de_Proyectos_y_Programas.ID=GN-ORG-UNID-PP-01
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Analisis_y_Evaluacion.Unidades_Dependientes.Unidad_de_Proyectos_y_Programas.Purp=Evaluación
      de iniciativas FNDR, programas y concursos asociados al programa de inversión
      regional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Presupuesto.Act[0]=Gestionar
      presupuesto desde identificación presupuestaria hasta control y seguimiento.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Presupuesto.Act[1]=Elaborar
      resoluciones.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Presupuesto.Act[2]=Gestionar
      caja.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Presupuesto.Act[3]=Coordinar
      internamente con divisiones del Gobierno Regional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Presupuesto.Act[4]=Coordinar
      externamente con Dirección de Presupuestos (DIPRES), SUBDERE y Contraloría Regional.
    - Organigrama_Institucional_GORE_Nuble.Divisiones.Division_de_Presupuesto_e_Inversion_Regional.Componentes.Departamento_de_Presupuesto.ID=GN-ORG-DEP-PRESUPUESTO-01
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
---

# Organigrama Institucional GORE Ñuble

## Alcance
Organigrama operativo y estructura organica observables en la fuente KODA y el slice TTL organizacional.

## Fuente: Kb gn 002 organigrama koda
### Manifest
#### Urn
urn:knowledge:gorenuble:gn:organigrama:1.0.0
#### Federation
#### Visibility
internal
#### License
Institutional Use
#### Compatibility
#### Min consumer version
1.0.0
#### Breaking changes from
null
#### Resolution
#### Canonical url
file://knowledge/domains/gn/01_fundamentos/intro/kb_gn_002_organigrama_koda.yml
#### Mirrors
#### Dependencies
#### Requires
| urn | reason |
| --- | --- |
| urn:knowledge:koda:core:spec:1.0.0 | KODA/Spec format compliance |
| urn:knowledge:koda:core:transform:1.0.0 | Transformation methodology reference |
#### Provenance
#### Created by
KODA-TRANSFORMER
#### Created at
2026-01-27
#### Last modified at
2026-01-27
#### Signature
null
### ID
KB-GN-002-ORGANIGRAMA-01
### Version
1.0.0
### Status
Published
### Human Creator
FSA
### Human Editor
FSA
### Model Collaborator
GPT-5.2
### Creation Date
2026-01-26
### Modification Date
2026-01-26
### Primary Source
staging/organigrama_gore_2026.md
### Ctx
Organigrama institucional del Gobierno Regional de Ñuble (versión 2026).
### LLM Parsing Instructions
#### ID
KODA-LLM-PARSER-01
#### Req
Mandatory block following Metadata.
#### Prohib
Using for artifact creation or translation.
#### Content
BEGIN_LLM_INSTRUCTIONS
You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).

LEXICON (expand before processing): Act->Action, Cond->Condition, Ctx->Context, Ctx_Required->Required External Reference, Ctx_Optional->Optional External Reference, Def->Definition, Ex->Example, Mssn->Mission, Obj->Objective, Proc->Process, Purp->Purpose, Ref->Reference, XRef->Cross-Artifact Reference, XRef_Required->Mandatory Cross-Artifact Reference, Req->Requirement, Res->Result, Src->Source, Prohib->Prohibition, Warn->Warning, Just->Justification, Rec->Recommendation

REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. XRef/XRef_Required: are external only—must point to a URN (optionally with #ID fragment) in another artifact. External documents without specific ID use Ctx:, Ctx_Required:, or Ctx_Optional:.

LANGUAGE POLICY: Keywords in English, content in original language. Never translate content.
END_LLM_INSTRUCTIONS

### Organigrama Institucional GORE Nuble
#### ID
GN-ORG-2026-01
#### Purp
Describir estructura organizacional y funciones generales por unidad.
#### Ctx
- Contenido redactado como descripciones funcionales (no incluye dotación/cargos específicos).
- Orden de unidades preserva el orden del documento fuente.
#### Maxima Autoridad
#### Gobernador Regional
#### ID
GN-ORG-GOBERNADOR-01
#### Def
Máxima autoridad ejecutiva del Gobierno Regional; dirige la administración del Gobierno Regional.
#### Src
- Ley Orgánica Constitucional de Gobierno y Administración Regional (LOCGAR), Ley N°19.175.
- Constitución Política de la República.
#### Act
- Gestionar administración del Gobierno Regional.
- Ejecutar funciones propias del servicio.
- Coordinar trabajo de las divisiones del Gobierno Regional.
- Presidir el Consejo Regional.
#### Req
- Ejercer funciones con estricto apego a la Constitución Política de la República.
#### Unidades y Organos
#### Unidad de Gabinete y Participacion Social
#### ID
GN-ORG-GABINETE-01
#### Purp
Asesoría al Gobernador Regional y al equipo directivo; coordinación institucional.
#### Act
- Asesorar al Gobernador Regional y equipo directivo en materias específicas (principalmente administrativas y de gestión).
- Coordinar agenda institucional, despliegue territorial y audiencias.
- Preparar información de respaldo para actividades institucionales.
- Contribuir a articulación con actores del sector público y privado.
#### Departamento de Comunicaciones
#### ID
GN-ORG-COMUNICACIONES-01
#### Purp
Comunicación externa e interna del Gobierno Regional.
#### Act
- Diseñar, planificar y ejecutar estrategias de comunicación para mantener a la ciudadanía informada del quehacer, planes y objetivos del Gobierno Regional y su Consejo.
- Gestionar vinculación con actores relacionados con la institución.
- Gestionar relación formal con medios de comunicación e imagen institucional.
- Fortalecer confianza en la información entregada y transparencia de acciones.
- Promover comunicación clara y cercana a la ciudadanía.
- Fortalecer flujos de información interna para alinear equipos, fomentar cultura organizacional y mejorar compromiso con objetivos estratégicos.
#### Unidad de Control
#### ID
GN-ORG-CONTROL-01
#### Purp
Auditoría operativa interna; control de legalidad y ejecución financiera/presupuestaria.
#### Dependencia
Gobernador Regional.
#### Relacion
- Colabora directamente con el Consejo Regional en su función de fiscalización.
#### Act
- Realizar auditoría operativa interna institucional.
- Fiscalizar legalidad de actos del Gobierno Regional.
- Controlar ejecución financiera y presupuestaria.
- Emitir informes trimestrales al Consejo Regional.
- Responder consultas del Consejo Regional.
- Informar sobre reclamaciones.
- Representar al Gobernador Regional actos que se estimen ilegales.
- Asesoría técnica permanente al Gobernador Regional y al Consejo Regional en cumplimiento normativo, auditoría interna y control de gestión.
- Identificar, evaluar y mitigar riesgos institucionales.
- Resguardar uso eficiente, eficaz y conforme a derecho de recursos públicos regionales.
- Seguimiento sistemático de ejecución presupuestaria.
- Informar trimestralmente al Consejo Regional sobre avance financiero, procesos de contratación pública, licitaciones y materias relevantes para toma de decisiones.
#### Consejo de la Sociedad Civil COSOC
#### ID
GN-ORG-COSOC-01
#### Def
Órgano colegiado y autónomo.
#### Obj
- Promover y fortalecer participación ciudadana en gestión del Gobierno Regional.
- Fiscalizar cumplimiento de normas de participación civil.
#### Ctx
- Con representación de organizaciones de la sociedad civil de la Región de Ñuble vinculadas a competencias del Gobierno Regional.
#### Res
- Contribuye a transparencia, eficacia y legitimidad de la acción gubernamental a nivel regional.
#### Consejo Regional de Nuble CORE
#### ID
GN-ORG-CORE-01
#### Def
Órgano normativo, fiscalizador y decisorio del Gobierno Regional.
#### Purp
Hacer efectiva la participación de la comunidad regional en el gobierno regional.
#### Ctx
- Compuesto por 16 Consejeras y Consejeros Regionales.
- Elegidos democráticamente para representar provincias: Diguillín, Punilla e Itata.
- Presidido por el Gobernador Regional.
#### Src
- Ley 19.175 Orgánica Constitucional sobre Gobierno y Administración Regional.
#### Secretaria Ejecutiva del Consejo Regional
#### ID
GN-ORG-SEC-CORE-01
#### Def
Unidad administrativa, técnica y operativa que facilita y coordina funcionamiento del CORE.
#### Act
- Asegurar cumplimiento de acuerdos y resoluciones del Consejo.
- Servir de enlace entre CORE, Gobernador Regional, unidades del Gobierno Regional y comunidad.
- Coordinar, colaborar y asesorar desempeño de funciones del Consejo Regional.
- Apoyar planificación anual.
- Registrar acuerdos.
- Elaborar actas de cada sesión.
#### Administracion Regional
#### ID
GN-ORG-ADMIN-REGIONAL-01
#### Purp
Gestión administrativa integral y coordinación del accionar de jefaturas de divisiones.
#### Act
- Coordinar accionar de jefes/as de cada una de las divisiones.
- Ejecutar materias propias del servicio.
- Ejercer subrogancia del Gobernador Regional en caso de ausencia.
#### Ctx
- Desempeño del cargo bajo exclusiva confianza del Gobernador Regional.
#### Corporacion Regional de Desarrollo
#### ID
GN-ORG-CORP-DESARROLLO-01
#### Mssn
Entidad asesora del Gobierno Regional de Ñuble en planificación, gestión y desarrollo de políticas públicas.
#### Obj
Promover desarrollo integral y articulado público-privado en áreas de interés de la región.
#### Act
- Contribuir a promoción, posicionamiento y avance de la región a nivel nacional e internacional.
- Implementar iniciativas para disminuir desigualdades socio-territoriales.
#### Ctx
- Núcleo de intervención: provincias y comunas de la región.
#### Auditoria Interna
#### ID
GN-ORG-AUD-INTERNA-01
#### Def
Unidad de monitoreo independiente y objetivo del sistema de control interno del Gobierno Regional.
#### Act
- Evaluación objetiva e independiente de gestión y desempeño del Gobierno Regional.
- Examinar y analizar procesos administrativos, financieros y operativos para asegurar conformidad normativa y uso eficiente de recursos.
- Realizar auditoría operativa interna del GORE.
- Velar por transparencia activa según ley de acceso a la información pública.
- Asesorar al Gobernador Regional y jefaturas en asuntos de funcionamiento (excepto procesos disciplinarios).
- Coordinar seguimiento de recomendaciones de la Contraloría General de la República.
#### Departamento Juridico
#### ID
GN-ORG-JURIDICO-01
#### Purp
Asesoría legal interna; resguardo de legalidad institucional.
#### Act
- Asesorar en materias legales a distintas áreas del servicio.
- Elaborar y supervisar actos administrativos.
- Representación judicial y extrajudicial del Gobierno Regional.
- Entregar lineamientos legales a la autoridad y unidades.
- Mantener informados estamentos sobre normas legales y reglamentarias pertinentes.
#### Departamento de Gestion Institucional
#### ID
GN-ORG-GESTION-INST-01
#### Purp
Planificación institucional y control de gestión para toma de decisiones.
#### Act
- Desarrollar sistema de planificación y control de gestión.
- Formular, monitorear y dar seguimiento a indicadores de desempeño institucional.
- Planificar, organizar y controlar procesos administrativos y estratégicos para asegurar cumplimiento de objetivos.
- Optimizar recursos y lograr objetivos de calidad y eficiencia.
- Implementar políticas y mejora continua para asegurar buen funcionamiento administrativo y organizacional.
#### Unidades Dependientes
#### Oficina OIRS
#### ID
GN-ORG-OIRS-01
#### Def
Oficina de Informaciones, Reclamos y Sugerencias (OIRS).
#### Purp
Facilitar vínculo ciudadanía–Gobierno Regional.
#### Act
- Generar espacios de atención y participación ciudadana.
- Facilitar interacción con la ciudadanía.
- Garantizar derecho de acceso a la información pública.
- Gestionar y canalizar reclamos, sugerencias y felicitaciones recibidos en la institución.
- Asegurar atención oportuna.
- Retroalimentar administración con base en necesidades y sugerencias de la comunidad.
#### Departamento Nuble 250
#### ID
GN-ORG-NUBLE-250-01
#### Purp
Articulación técnica y seguimiento de proyectos estratégicos priorizados (Agenda Ñuble 250).
#### Ctx
- Agenda Ñuble 250: hoja de ruta regional hacia 2028; concordante con el primer decenio de creación de la Región de Ñuble.
#### Act
- Articular técnicamente, coordinar, controlar y dar seguimiento a la gestión de proyectos estratégicos de la cartera de inversión priorizada.
- Favorecer trabajo coordinado entre reparticiones públicas y divisiones del Gobierno Regional.
- Fortalecer gobernanza territorial y coherencia de acción estatal en la región.
#### Req
- Alineación con objetivos de la Estrategia de Desarrollo Regional.
#### Unidad Regional de Asuntos Internacionales URAI
#### ID
GN-ORG-URAI-01
#### Purp
Gestión de internacionalización de la región.
#### Act
- Propiciar cooperación internacional.
- Impulsar paradiplomacia.
- Coordinar con entidades nacionales e internacionales.
- Promover desarrollo regional y participación comunitaria en ámbito exterior.
- Complementar funciones del gobierno central.
#### Res
- Contribuye a participación activa de la Región de Ñuble en escena internacional.
#### Departamento Coordinacion Integral de Emergencia y Seguridad
#### ID
GN-ORG-EMERG-SEG-01
#### Purp
Mejorar respuesta oportuna y coordinada ante emergencias y seguridad pública.
#### Mech
- Integración de sistemas de comunicaciones, información, televigilancia y medios logísticos.
- Colaboración entre distintas instituciones.
#### Act
- Formular, diseñar y evaluar políticas y estrategias en seguridad pública y gestión de riesgo de desastres.
- Gestionar cartera de proyectos GORE en seguridad y gestión de riesgo de desastres.
- Mantener coordinación permanente con municipalidades e instituciones de la región en estas materias.
#### Divisiones
#### Division de Planificacion y Desarrollo Regional
#### ID
GN-ORG-DIV-PLAN-01
#### Purp
Planificación territorial y apoyo a evaluación de políticas regionales.
#### Act
- Elaborar y proponer estrategias, políticas, planes, programas y proyectos para desarrollo armónico del territorio (incluye Plan Regional de Ordenamiento Territorial).
- Basar procesos en insumos técnicos y participativos, conforme a prioridades definidas por el gobierno regional.
- Apoyar al Gobernador Regional en evaluación de cumplimiento de políticas, planes, programas, proyectos y presupuestos de carácter regional.
- Prestar asistencia técnica a municipalidades y otros organismos de la administración que lo requieran.
#### Componentes
#### Comite de Pertinencia y Vinculacion Estrategica
#### ID
GN-ORG-COMITE-PERTINENCIA-01
#### Def
Instancia formal de asesoría y análisis de proyectos.
#### Integrantes
- Administrador(a) Regional.
- Jefaturas de Divisiones: Planificación y Desarrollo Regional (Presidente del Comité), Presupuesto e Inversión Regional, Fomento e Industria, Desarrollo Social y Humano, Infraestructura y Transporte.
#### Act
- Asesorar integralmente a la autoridad.
- Analizar admisibilidad de proyectos postulados.
- Analizar pertinencia regional con base en instrumentos de planificación regional y competencias determinadas en la Ley Orgánica de Gobierno y Administración Regional.
#### Departamento de Planificacion Estrategica y Ordenamiento Territorial
#### ID
GN-ORG-DEP-PEOT-01
#### Purp
Planificación estratégica y ordenamiento territorial regional.
#### Mssn
Impulsar desarrollo armónico y sostenible.
#### Act
- Elaborar y proponer planes de desarrollo local que integren necesidades de la comunidad con análisis de restricciones ambientales y particularidades geofísicas del territorio.
- Considerar vocación productiva distintiva de cada comuna, infraestructura existente y proyecciones de crecimiento futuro.
- Coordinar formulación y seguimiento del Anteproyecto Regional de Inversión (ARI).
- Coordinar formulación y seguimiento del Programa Público de Inversión Regional (PROPIR).
#### Departamento de Desarrollo de Proyectos Estrategicos
#### ID
GN-ORG-DEP-DPE-01
#### Purp
Gestión de iniciativas de alto impacto alineadas con visión regional.
#### Act
- Seleccionar, planificar y supervisar iniciativas de alto impacto.
- Alinear operación diaria con visión de largo plazo del Gobierno Regional.
- Facilitar vínculo entre visión de la autoridad regional, su Consejo y directivos.
- Asegurar contribución de proyectos a competitividad, innovación y crecimiento territorial.
#### Req
- Alineación con Estrategia Regional de Desarrollo.
#### Departamento Zonas en Desarrollo
#### ID
GN-ORG-DEP-ZED-01
#### Purp
Acceso equitativo al desarrollo y fortalecimiento de descentralización.
#### Ctx
- Enfoque de derechos.
#### Act
- Promover inversión pública focalizada.
- Fortalecer descentralización.
- Promover participación de actores de la sociedad.
- Promover desarrollo territorial integral y equilibrado con base en especificidades regionales.
#### Division de Presupuesto e Inversion Regional
#### ID
GN-ORG-DIV-PRESUPUESTO-INVERSION-01
#### Purp
Presupuesto de inversión regional; ejecución, control y asesoría al Gobernador.
#### Act
- Elaborar proyectos de presupuestos de inversión del gobierno regional.
- Ejecutar y controlar presupuesto de inversión y programas administrados por el gobierno regional.
- Asesorar al Gobernador Regional en definición de proyectos de inversión a desarrollar o financiar según lineamientos y prioridades de instrumentos de planificación regional.
#### Componentes
#### Departamento de Analisis y Evaluacion
#### ID
GN-ORG-DEP-AE-01
#### Purp
Revisión y evaluación técnica de proyectos/programas postulados.
#### Ctx
- Postulación a financiamiento FNDR.
#### Act
- Evaluar pertinencia con lineamientos regionales.
- Asesorar en determinación de proyectos a desarrollar.
- Proporcionar proyectos con RS coordinando el Comité de Pertinencia y Vinculación Estratégica para análisis y priorización.
- Establecer metodologías y analizar normativa técnica y presupuestaria para postulación a financiamiento.
- Controlar solicitudes de financiamiento de inversión regional.
- Apoyar formulación de proyectos y programas regionales.
- Coordinar asesoría técnica a municipalidades y otros servicios para cumplimiento del desarrollo regional.
#### Unidades Dependientes
#### Unidad de Municipalidades y Conservaciones
#### ID
GN-ORG-UNID-MUNIC-CONS-01
#### Def
Unidad dependiente del Departamento de Análisis y Evaluación.
#### Purp
Evaluación de proyectos de inversión local.
#### Ctx
- Tipos: FRIL, Circular 33, PMU-PMB.
#### Act
- Evaluar técnica y administrativamente proyectos de inversión local.
- Asegurar viabilidad normativa y financiera.
- Fortalecer gestión comunal mediante asesoría directa y capacitación externa para optimizar formulación de iniciativas territoriales.
- Tramitar convenios, resoluciones y registro en plataformas oficiales del Estado.
#### Unidad de Proyectos y Programas
#### ID
GN-ORG-UNID-PP-01
#### Purp
Evaluación de iniciativas FNDR, programas y concursos asociados al programa de inversión regional.
#### Ctx
- Concursos: 8%, FRPD, otros; activos no financieros.
#### Act
- Evaluar técnica y administrativamente iniciativas FNDR, programas públicos y concursos.
- Gestionar admisibilidad y visación ante el Ministerio de Desarrollo Social cuando corresponda.
- Asesorar a divisiones regionales, servicios, universidades y organizaciones privadas para correcta formulación de proyectos.
- Ejecutar planes de capacitación externa.
#### Departamento de Presupuesto
#### ID
GN-ORG-DEP-PRESUPUESTO-01
#### Purp
Gestión integral del presupuesto de inversión.
#### Act
- Gestionar presupuesto desde identificación presupuestaria hasta control y seguimiento.
- Elaborar resoluciones.
- Gestionar caja.
- Coordinar internamente con divisiones del Gobierno Regional.
- Coordinar externamente con Dirección de Presupuestos (DIPRES), SUBDERE y Contraloría Regional.
#### Division de Desarrollo Social y Humano
#### ID
GN-ORG-DIV-DSH-01
#### Def
Eje de la inversión social del Gobierno Regional de Ñuble.
#### Purp
Fortalecer desarrollo humano y reducir brechas estructurales.
#### Act
- Definir e implementar lineamientos estratégicos de inversión social.
- Diseñar, ejecutar y dar seguimiento a políticas regionales, programas y proyectos sociales.
#### Ctx
- Ámbitos: pobreza, educación, salud, género, neurodiversidad, vivienda, entre otros.
#### Obj
- Promover equidad territorial.
- Promover inclusión social.
- Resguardar dignidad humana.
#### Res
- Complementa y fortalece acción del Estado en la región.
#### Componentes
#### Departamento de Fondos Concursables y Programas Sociales
#### ID
GN-ORG-DEP-FCPS-01
#### Purp
Gestión de fondos concursables y programas sociales.
#### Act
- Planificar, coordinar, gestionar y supervisar inversión social mediante fondos concursables y programas sociales.
- Asegurar asignación eficiente, transparente y pertinente de recursos públicos.
- Promover iniciativas con impacto social, pertinencia territorial y enfoque de derechos.
- Articular trabajo con municipios, servicios públicos, organizaciones de la sociedad civil y otras entidades ejecutoras.
- Velar por ciclo de vida de iniciativas: diseño, evaluación, ejecución, seguimiento y cierre.
#### Req
- Coherencia con Estrategia Regional de Desarrollo, políticas públicas vigentes y prioridades definidas por el Gobierno Regional.
#### Departamento de Gestion Territorial
#### ID
GN-ORG-DEP-GT-01
#### Purp
Operativización y despliegue territorial de oferta programática.
#### Act
- Actuar como nexo de vinculación estratégica entre el Gobierno Regional de Ñuble y las personas de la región.
- Fortalecer desarrollo social y comunitario.
- Asegurar pertinencia territorial de actividades.
- Contribuir a priorización de inversión regional.
- Realizar seguimiento técnico de cartera de inversión social de la división.
#### Division de Fomento e Industria
#### ID
GN-ORG-DIV-FOMENTO-01
#### Purp
Fomento productivo, ciencia, tecnología e innovación.
#### Act
- Proponer, promover y ejecutar planes y programas regionales para estimular desarrollo de ciencia, tecnología e innovación y nuevas capacidades empresariales.
- Facilitar incorporación de nuevas tecnologías de la información para favorecer crecimiento sostenido, integrado y sustentable.
- Proponer y promover instrumentos de fomento productivo.
#### Componentes
#### Departamento de Fomento y Desarrollo Productivo
#### ID
GN-ORG-DEP-FDP-01
#### Purp
Impulso a economía regional y emprendimiento.
#### Act
- Promover emprendimiento.
- Diseñar políticas regionales de fomento y desarrollo productivo.
- Ejecutar planes, programas e instrumentos de fomento productivo.
- Lograr crecimiento sostenible, integrado y articulado con actores relevantes de la región.
#### Departamento de Ciencia Tecnologia e Innovacion
#### ID
GN-ORG-DEP-CTI-01
#### Purp
Fomento del conocimiento, investigación y desarrollo tecnológico regional.
#### Obj
Sostenibilidad y crecimiento económico.
#### Act
- Planificar, diseñar e implementar estrategias de CTI.
- Coordinar y articular actores relevantes: sector público, academia y ámbito privado.
- Contribuir a creación de políticas públicas.
- Fortalecer ecosistema regional.
#### Division de Infraestructura y Transportes
#### ID
GN-ORG-DIV-INFRA-TRANS-01
#### Purp
Obras de infraestructura y equipamiento regional; gestión en transportes.
#### Act
- Proponer, promover y ejecutar planes y programas regionales en infraestructura, equipamiento regional y transportes.
#### Componentes
#### Departamento de Infraestructura y Conectividad
#### ID
GN-ORG-DEP-INFRA-CONECT-01
#### Purp
Infraestructura, transporte, movilidad y conectividad (vial y digital).
#### Act
- Proponer y promover planes, estudios y programas regionales en coordinación con servicios públicos regionales.
- Analizar e identificar brechas existentes en infraestructura, transporte, movilidad y conectividad en distintas escalas territoriales.
- Entregar directrices para oferta de programas y servicios de conectividad.
- Promover y coordinar iniciativas para ampliar cobertura y calidad del transporte colectivo.
- Proponer iniciativas para intermovilidad segura mediante programas y obras.
- Evaluar y coordinar con otras instituciones planes de inversiones en movilidad.
- Estudiar y proponer sistemas de Transporte Inteligente.
#### Departamento de Ejecucion y Supervision de Proyectos de Inversion
#### ID
GN-ORG-DEP-ESP-01
#### Purp
Supervisión de ejecución de proyectos de inversión regional.
#### Act
- Supervisar gestión eficiente de inversión regional mediante control riguroso de ejecución de proyectos asignados.
- Fiscalización técnica (física) y presupuestaria (financiera) para resguardar integridad del proceso.
- Coordinar con Contrapartes Técnicas para asegurar cumplimiento de objetivos institucionales.
- Ejecutar de manera directa iniciativas de inversión que le sean encomendadas (responsabilidad técnica y administrativa).
#### Division de Administracion y Finanzas
#### ID
GN-ORG-DIV-ADAF-01
#### Purp
Gestión administrativa y financiera; presupuesto de funcionamiento; servicios generales; personal.
#### Src
- Ley N.º 19.175.
- Ley N.º 18.834.
#### Res
Sustenta funcionamiento eficiente y transparente del Gobierno Regional.
#### Componentes
#### Oficina de Partes
#### ID
GN-ORG-OF-PARTES-01
#### Purp
Gestión documental institucional.
#### Act
- Recepción, distribución, archivo, registro y despacho de documentación de entrada y salida de servicios administrativos del Gobierno Regional de Ñuble.
- Gestión de otras materias propias de su naturaleza y/o encomendadas o delegadas.
#### Departamento de Gestion y Desarrollo de Personas
#### ID
GN-ORG-DEP-GDP-01
#### Purp
Estrategias, políticas y procesos del ciclo de vida laboral del personal.
#### Act
- Definir, elaborar e implementar estrategias, políticas y procesos institucionales de gestión de personas.
- Asegurar equipo humano competente, motivado y alineado con objetivos de desarrollo regional.
#### Req
- Concordancia con lineamientos de la autoridad regional.
- Concordancia con normativa vigente aplicable al sector público.
- Concordancia con instrumentos de gestión de personas del Estado.
#### Departamento de Finanzas
#### ID
GN-ORG-DEP-FINANZAS-01
#### Purp
Revisión y control de información presupuestaria, contable y financiera.
#### Act
- Supervisar elaboración y ejecución del presupuesto.
- Gestionar registro contable y elaboración de estados financieros.
- Analizar situación económica para toma de decisiones.
- Implementar políticas de control para seguridad de activos.
- Optimizar uso de recursos.
#### Res
Garante de salud financiera y transparencia institucional.
#### Unidades Dependientes
#### Unidad de Tesoreria
#### ID
GN-ORG-UNID-TESORERIA-01
#### Purp
Administración y custodia de ingresos y egresos; pagos y flujo de caja.
#### Act
- Administrar, controlar y custodiar ingresos y egresos del Gobierno Regional.
- Gestionar fondos institucionales, pagos y flujo de caja.
- Velar por liquidez y estabilidad financiera.
#### Res
- Asegura cumplimiento de obligaciones financieras.
- Asegura eficiencia en ejecución presupuestaria.
#### Unidad de Contabilidad y Finanzas
#### ID
GN-ORG-UNID-CONTAB-FIN-01
#### Purp
Registro, control y análisis de información contable y presupuestaria.
#### Act
- Registrar, controlar y analizar información contable y presupuestaria.
- Resguardar integridad de datos financieros y contables.
#### Res
- Permite gestión alineada con normativas vigentes y buenas prácticas del sector público.
#### Unidad de Control de Rendiciones
#### ID
GN-ORG-UNID-RENDICIONES-01
#### Purp
Seguimiento y control de rendiciones de cuentas.
#### Act
- Seguimiento, monitoreo, control y contabilización de rendiciones de cuentas ingresadas al Gobierno Regional.
- Asegurar uso de recursos conforme a normativa vigente, de forma eficiente, transparente y oportuna.
#### Res
- Resguarda correcta administración de fondos públicos.
#### Unidad de Adquisiciones
#### ID
GN-ORG-UNID-ADQ-01
#### Purp
Procesos de compras de bienes y servicios.
#### Req
- Apego a Ley de Compras Públicas y su reglamento.
#### Act
- Ejecutar procesos de adquisiciones de bienes y servicios necesarios para funcionamiento institucional.
- Publicar y monitorear contrataciones especialmente encomendadas provenientes del programa de inversiones, junto a unidad técnica designada.
#### Obj
- Eficiencia.
- Transparencia.
- Probidad.
#### Unidad de Operaciones
#### ID
GN-ORG-UNID-OPERACIONES-01
#### Purp
Infraestructura física, flota vehicular y tecnologías de la información.
#### Act
- Gestionar infraestructura física (edificios e instalaciones) y flota de vehículos institucionales.
- Coordinar mantenimiento preventivo, correctivo y respuesta a emergencias.
- Asegurar operatividad, funcionalidad y seguridad de recursos físicos institucionales.
- Gestionar y mantener infraestructura TI: red, servidores, hardware, software, sistemas de información.
- Gestionar políticas de seguridad informática y protección de datos institucionales.
- Desarrollar soluciones tecnológicas alineadas con objetivos estratégicos del Gobierno Regional.
#### Src
- Ley de Transformación Digital.

## Fuente: GoreNubleOrgData
- <https://gorenuble.gob.cl/data/goreNubleOrgData>
- @prefix gist: <https://w3id.org/semanticarts/ns/ontology/gist/> .
- @prefix gnub: <https://gorenuble.gob.cl/ns/ontology/> .
- @prefix gnubd: <https://gorenuble.gob.cl/ns/data/> .
- @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
- a gist:Assignment ;
- a gist:GovernmentOrganization ;
- a gnub:AdvisoryBody ;
- a gnub:Department ;
- a gnub:OrganizationalUnitType ;
- a gnub:PositionType ;
- a owl:Ontology ;
- gist:isAssignmentOf gnubd:_Person_AlejandroAguilera ;
- gist:isAssignmentOf gnubd:_Person_OscarCrisostomo ;
- gist:isAssignmentTo gnubd:_Advisory_COSOC ;
- gist:isAssignmentTo gnubd:_Advisory_ComiteCTCI ;
- gist:isAssignmentTo gnubd:_Div_DAF ;
- gist:isAssignmentTo gnubd:_Div_DIDESO ;
- gist:isAssignmentTo gnubd:_Div_DIFOI ;
- gist:isAssignmentTo gnubd:_Div_DIINF ;
- gist:isAssignmentTo gnubd:_Div_DIPIR ;
- gist:isAssignmentTo gnubd:_Div_DIPLADE ;
- gist:isAssignmentTo gnubd:_Org_GORE_Nuble ;
- gist:isAssignmentTo gnubd:_Staff_Auditoria ;
- gist:isAssignmentTo gnubd:_Staff_Comunicaciones ;
- gist:isAssignmentTo gnubd:_Staff_Control ;
- gist:isAssignmentTo gnubd:_Staff_Corporacion ;
- gist:isAssignmentTo gnubd:_Staff_DGI ;
- gist:isAssignmentTo gnubd:_Staff_EmergenciaSeguridad ;
- gist:isAssignmentTo gnubd:_Staff_Gabinete ;
- gist:isAssignmentTo gnubd:_Staff_Juridica ;
- gist:isAssignmentTo gnubd:_Staff_Nuble250 ;
- gist:isAssignmentTo gnubd:_Staff_URAI ;
- gist:isAssignmentTo gnubd:_Unit_DAF_OficinaPartes ;
- gist:isCategorizedBy gnubd:_PositionType_AdministradorRegional ;
- gist:isCategorizedBy gnubd:_PositionType_Gobernador ;
- gist:isCategorizedBy gnubd:_PositionType_JefeDivision ;
- gist:isDirectPartOf gnubd:_Div_DIPLADE ;
- gist:isDirectPartOf gnubd:_Province_Punilla ;
- gist:isGovernedBy gnubd:_Org_GORE_Nuble ;
- gnub:containsGeoRegion gnubd:_Province_Diguillin, gnubd:_Province_Itata, gnubd:_Province_Punilla ;
- gnub:isCapitalOf gnubd:_Province_Punilla ;
- gnubd:_Advisory_CDR
- gnubd:_Advisory_COSOC
- gnubd:_Advisory_COSOC gist:isMemberOf gnubd:_Collection_ORGANOS_ESPECIALES .
- gnubd:_Advisory_ComiteCTCI
- gnubd:_Advisory_ComiteCTCI gist:isMemberOf gnubd:_Collection_ORGANOS_ESPECIALES .
- gnubd:_Assignment_AdministradorRegional
- gnubd:_Assignment_AdministradorRegional gnub:supervises gnubd:_Assignment_JefeDIPLADE, gnubd:_Assignment_JefeDIPIR, gnubd:_Assignment_JefeDIDESO, gnubd:_Assignment_JefeDIFOI, gnubd:_Assignment_JefeDIINF, gnubd:_Assignment_JefeDAF .
- gnubd:_Assignment_AdministradorRegional gnub:supervises gnubd:_Assignment_JefeJuridica, gnubd:_Assignment_JefeAuditoria, gnubd:_Assignment_JefeDGI, gnubd:_Assignment_JefeNuble250, gnubd:_Assignment_JefeURAI, gnubd:_Assignment_JefeEmergenciaSeguridad, gnubd:_Assignment_JefeCorporacion .
- gnubd:_Assignment_Gobernador
- gnubd:_Assignment_Gobernador gnub:chairs gnubd:_Org_CORE_Nuble .
- gnubd:_Assignment_Gobernador gnub:nominatesCandidatesFor gnubd:_Collection_SEREMIAS .
- gnubd:_Assignment_Gobernador gnub:nominatesCandidatesFor gnubd:_Org_SEREMI_Educacion, gnubd:_Org_SEREMI_Salud, gnubd:_Org_SEREMI_Vivienda, gnubd:_Org_SEREMI_ObrasPublicas, gnubd:_Org_SEREMI_Agricultura, gnubd:_Org_SEREMI_Transportes, gnubd:_Org_SEREMI_Economia, gnubd:_Org_SEREMI_Trabajo, gnubd:_Org_SEREMI_MedioAmbiente .
- gnubd:_Assignment_Gobernador gnub:supervises gnubd:_Assignment_AdministradorRegional .
- gnubd:_Assignment_Gobernador gnub:supervises gnubd:_Assignment_JefeGabinete, gnubd:_Assignment_JefeComunicaciones, gnubd:_Assignment_JefeControl .
- gnubd:_Assignment_Gobernador gnub:supervises gnubd:_Assignment_PresidenteCOSOC, gnubd:_Assignment_PresidenteCTCI .
- gnubd:_Assignment_JefeAuditoria
- gnubd:_Assignment_JefeComunicaciones
- gnubd:_Assignment_JefeControl
- gnubd:_Assignment_JefeCorporacion
- gnubd:_Assignment_JefeDAF
- gnubd:_Assignment_JefeDGI
- gnubd:_Assignment_JefeDIDESO
- gnubd:_Assignment_JefeDIFOI
- gnubd:_Assignment_JefeDIINF
- gnubd:_Assignment_JefeDIPIR
- gnubd:_Assignment_JefeDIPLADE
- gnubd:_Assignment_JefeEmergenciaSeguridad
- gnubd:_Assignment_JefeGabinete
- gnubd:_Assignment_JefeJuridica
- gnubd:_Assignment_JefeNuble250
- gnubd:_Assignment_JefeOficinaPartes
- gnubd:_Assignment_JefeURAI
- gnubd:_Assignment_PresidenteCOSOC
- gnubd:_Assignment_PresidenteCTCI
- gnubd:_Collection_DIVISIONES_ORGANICAS
- gnubd:_Collection_NIVEL_CENTRAL
- gnubd:_Collection_STAFF_APOYO
- gnubd:_Commune_Chillan
- gnubd:_Commune_ChillanViejo
- gnubd:_Commune_Coelemu
- gnubd:_Commune_ElCarmen
- gnubd:_Commune_Niquen
- gnubd:_Commune_Portezuelo
- gnubd:_Commune_SanNicolas
- gnubd:_Commune_Yungay
- gnubd:_Dept_DIFOI_FomentoDesarrolloProductivo
- gnubd:_Dept_DIINF_InfraestructuraConectividad
- gnubd:_Dept_DIPLADE_PlanificacionEstrategica
- gnubd:_Dept_DIPLADE_ProyectosEstrategicos
- gnubd:_Dept_DIPLADE_ZonasDesarrollo
- gnubd:_Div_DAF gist:isMemberOf gnubd:_Collection_DIVISIONES_ORGANICAS .
- gnubd:_Div_DIDESO gist:isMemberOf gnubd:_Collection_DIVISIONES_ORGANICAS .
- gnubd:_Div_DIDESO gnub:deliversSocialProgramsIn gnubd:_GeoRegion_Nuble .
- gnubd:_Div_DIFOI gist:isMemberOf gnubd:_Collection_DIVISIONES_ORGANICAS .
- gnubd:_Div_DIFOI gnub:coordinatesProductivelyWith gnubd:_Collection_SERVICIOS_PUBLICOS_REGIONALES .
- gnubd:_Div_DIFOI gnub:coordinatesProductivelyWith gnubd:_Org_ServicioSaludNuble, gnubd:_Org_INE_Regional, gnubd:_Org_SAG_Regional, gnubd:_Org_SII_Regional, gnubd:_Org_SERNATUR_Nuble, gnubd:_Org_CORFO_Regional, gnubd:_Org_INDAP_Regional, gnubd:_Org_SERCOTEC_Regional .
- gnubd:_Div_DIFOI gnub:promotesProductiveDevelopmentIn gnubd:_GeoRegion_Nuble .
- gnubd:_Div_DIINF gist:isMemberOf gnubd:_Collection_DIVISIONES_ORGANICAS .
- gnubd:_Div_DIINF gnub:deliversPublicWorksIn gnubd:_GeoRegion_Nuble .
- gnubd:_Div_DIPIR gist:isMemberOf gnubd:_Collection_DIVISIONES_ORGANICAS .
- gnubd:_Div_DIPLADE
- gnubd:_Div_DIPLADE gist:isMemberOf gnubd:_Collection_DIVISIONES_ORGANICAS .
- gnubd:_Div_DIPLADE gnub:coordinatesPlansWith gnubd:_Collection_SEREMIAS .
- gnubd:_Div_DIPLADE gnub:coordinatesPlansWith gnubd:_Org_SEREMI_Educacion, gnubd:_Org_SEREMI_Salud, gnubd:_Org_SEREMI_Vivienda, gnubd:_Org_SEREMI_ObrasPublicas, gnubd:_Org_SEREMI_Agricultura, gnubd:_Org_SEREMI_Transportes, gnubd:_Org_SEREMI_Economia, gnubd:_Org_SEREMI_Trabajo, gnubd:_Org_SEREMI_MedioAmbiente .
- gnubd:_OrgType_GobiernoRegional
- gnubd:_OrgType_Municipalidad
- gnubd:_OrgType_ONG
- gnubd:_OrgType_ServicioPublico
- gnubd:_OrgType_Universidad
- gnubd:_Org_CGR gist:isMemberOf gnubd:_Collection_NIVEL_CENTRAL .
- gnubd:_Org_CORE_Nuble gnub:audits gnubd:_Assignment_AdministradorRegional .
- gnubd:_Org_DIPRES gist:isMemberOf gnubd:_Collection_NIVEL_CENTRAL .
- gnubd:_Org_DPP_Diguillin gnub:exercisesInteriorGovernmentOver gnubd:_Province_Diguillin .
- gnubd:_Org_DPP_Itata gnub:exercisesInteriorGovernmentOver gnubd:_Province_Itata .
- gnubd:_Org_DPP_Punilla
- gnubd:_Org_DPP_Punilla gist:isMemberOf gnubd:_Collection_GOBIERNO_INTERIOR .
- gnubd:_Org_DPP_Punilla gnub:exercisesInteriorGovernmentOver gnubd:_Province_Punilla .
- gnubd:_Org_MDSF gist:isMemberOf gnubd:_Collection_NIVEL_CENTRAL .
- gnubd:_Org_MinisterioInterior gist:isMemberOf gnubd:_Collection_NIVEL_CENTRAL .
- gnubd:_Org_MinisterioInterior gnub:hasTutelaOver gnubd:_Org_DPR_Nuble .
- gnubd:_Org_MinisterioSeguridadPublica gist:isMemberOf gnubd:_Collection_NIVEL_CENTRAL .
- gnubd:_Org_Presidencia
- gnubd:_Org_Presidencia gist:isMemberOf gnubd:_Collection_NIVEL_CENTRAL .
- gnubd:_Org_Presidencia gnub:designates gnubd:_Org_DPR_Nuble .
- gnubd:_Org_SEREMI_MedioAmbiente
- gnubd:_Org_SEREMI_MedioAmbiente gist:isMemberOf gnubd:_Collection_SEREMIAS .
- gnubd:_Org_SEREMI_Vivienda
- gnubd:_Org_SEREMI_Vivienda gist:isMemberOf gnubd:_Collection_SEREMIAS .
- gnubd:_Org_SUBDERE gist:isMemberOf gnubd:_Collection_NIVEL_CENTRAL .
- gnubd:_Org_SUBDERE gnub:regulates gnubd:_Org_GORE_Nuble .
- gnubd:_Person_TamaraValenzuela
- gnubd:_PositionType_AdministradorRegional
- gnubd:_PositionType_ConsejeroRegional
- gnubd:_PositionType_Gobernador
- gnubd:_PositionType_JefeDepartamento
- gnubd:_PositionType_JefeDivision
- gnubd:_PositionType_JefeUnidad
- gnubd:_PositionType_RTF
- gnubd:_PositionType_SecretarioEjecutivo
- gnubd:_Province_Punilla
- gnubd:_Staff_Auditoria gist:isMemberOf gnubd:_Collection_STAFF_APOYO .
- gnubd:_Staff_Comunicaciones gist:isMemberOf gnubd:_Collection_STAFF_APOYO .
- gnubd:_Staff_Control gist:isMemberOf gnubd:_Collection_STAFF_APOYO .
- gnubd:_Staff_Corporacion gist:isMemberOf gnubd:_Collection_STAFF_APOYO .
- gnubd:_Staff_DGI gist:isMemberOf gnubd:_Collection_STAFF_APOYO .
- gnubd:_Staff_EmergenciaSeguridad
- gnubd:_Staff_EmergenciaSeguridad gist:isMemberOf gnubd:_Collection_ORGANOS_ESPECIALES .
- gnubd:_Staff_Gabinete gist:isMemberOf gnubd:_Collection_STAFF_APOYO .
- gnubd:_Staff_Juridica gist:isMemberOf gnubd:_Collection_STAFF_APOYO .
- gnubd:_Staff_Nuble250 gist:isMemberOf gnubd:_Collection_STAFF_APOYO .
- gnubd:_Staff_URAI gist:isMemberOf gnubd:_Collection_STAFF_APOYO .
- gnubd:_Unit_DAF_ControlRendiciones
- gnubd:_Unit_DIPIR_ProyectosProgramas
- gnubd:_Unit_DIPLADE_ComitePertinencia
- gnubd:_Unit_Percentage
- owl:imports <https://gorenuble.gob.cl/ontology/goreNubleOntology> ;
- skos:altLabel "$"@es ;
- skos:altLabel "%" ;
- skos:altLabel "Auditoría"@es ;
- skos:altLabel "CDR"@es ;
- skos:altLabel "CGR"@es ;
- skos:altLabel "CIES"@es ;
- skos:altLabel "CLP"@es ;
- skos:altLabel "CONSEJO REGIONAL 16 Consejeros Electos"@es ;
- skos:altLabel "CORE Ñuble"@es ;
- skos:altLabel "CORFO Ñuble"@es ;
- skos:altLabel "COSOC"@es ;
- skos:altLabel "CTI"@es ;
- skos:altLabel "Centro Integral de Emergencia y Seguridad"@es ;
- skos:altLabel "Comité CTCI"@es ;
- skos:altLabel "Comité CTI"@es ;
- skos:altLabel "Comité Pertinencia y Vinculación Estratégica"@es ;
- skos:altLabel "Comunicaciones"@es ;
- skos:altLabel "Corporación"@es ;
- skos:altLabel "DAF"@es ;
- skos:altLabel "DGI"@es ;
- skos:altLabel "DIDESO"@es ;
- skos:altLabel "DIFOI"@es ;
- skos:altLabel "DIPIR"@es ;
- skos:altLabel "DIPLADE"@es ;
- skos:altLabel "DIPRES"@es ;
- skos:altLabel "DIT"@es ;
- skos:altLabel "DPP Diguillín"@es ;
- skos:altLabel "DPP Itata"@es ;
- skos:altLabel "DPP Punilla"@es ;
- skos:altLabel "DPR Ñuble"@es ;
- skos:altLabel "Delegado Presidencial Regional"@es ;
- skos:altLabel "Departamento de Zonas en Desarrollo"@es ;
- skos:altLabel "Depto. Análisis y Evaluación"@es ;
- skos:altLabel "Depto. Ciencia, Tecnología e Innovación"@es ;
- skos:altLabel "Depto. Desarrollo Proyectos Estratégicos"@es ;
- skos:altLabel "Depto. Ejecución y Supervisión de Proyectos de Inversión"@es ;
- skos:altLabel "Depto. Finanzas"@es ;
- skos:altLabel "Depto. Fomento y Desarrollo Productivo"@es ;
- skos:altLabel "Depto. Fondos Concursables y Programas Sociales"@es ;
- skos:altLabel "Depto. Gestión Territorial"@es ;
- skos:altLabel "Depto. Gestión y Desarrollo de Personas"@es ;
- skos:altLabel "Depto. Infraestructura y Conectividad"@es ;
- skos:altLabel "Depto. Planificación Estratégica y Ordenamiento Territorial"@es ;
- skos:altLabel "Depto. Presupuesto"@es ;
- skos:altLabel "Depto. Zonas en Desarrollo"@es ;
- skos:altLabel "Divisiones Orgánicas"@es ;
- skos:altLabel "División Administración y Finanzas"@es ;
- skos:altLabel "División Desarrollo Social y Humano"@es ;
- skos:altLabel "División Fomento e Industria"@es ;
- skos:altLabel "División Infraestructura y Transportes"@es ;
- skos:altLabel "División Planificación y Desarrollo Regional"@es ;
- skos:altLabel "División Presupuesto e Inversión Regional"@es ;
- skos:altLabel "GORE Ñuble"@es ;
- skos:altLabel "Gabinete del Gobernador"@es ;
- skos:altLabel "Gabinete"@es ;
- skos:altLabel "INDAP Ñuble"@es ;
- skos:altLabel "INE Ñuble"@es ;
- skos:altLabel "Jurídica"@es ;
- skos:altLabel "MDSF"@es ;
- skos:altLabel "OIRS"@es ;
- skos:altLabel "ONG"@es ;
- skos:altLabel "Oficina Partes"@es ;
- skos:altLabel "Presidente de la República"@es ;
- skos:altLabel "Provincia Diguillín (Capital: Bulnes)"@es ;
- skos:altLabel "Provincia Itata (Capital: Quirihue)"@es ;
- skos:altLabel "Provincia Punilla (Capital: San Carlos)"@es ;
- skos:altLabel "RTF"@es ;
- skos:altLabel "SAG Ñuble"@es ;
- skos:altLabel "SERCOTEC Ñuble"@es ;
- skos:altLabel "SEREMIAS"@es ;
- skos:altLabel "SERVICIOS"@es ;
- skos:altLabel "SII Ñuble"@es ;
- skos:altLabel "SS Ñuble"@es ;
- skos:altLabel "SUBDERE"@es ;
- skos:altLabel "Secretaría Ejecutiva CORE"@es ;
- skos:altLabel "Staff de Apoyo"@es ;
- skos:altLabel "TIC"@es ;
- skos:altLabel "UCR"@es ;
- skos:altLabel "URAI"@es ;
- skos:altLabel "UTM"@es ;
- skos:altLabel "Unidad Adquisiciones"@es ;
- skos:altLabel "Unidad Contabilidad y Finanzas"@es ;
- skos:altLabel "Unidad Control Rendiciones"@es ;
- skos:altLabel "Unidad Control"@es ;
- skos:altLabel "Unidad Municipalidades y Conservaciones"@es ;
- skos:altLabel "Unidad Operaciones"@es ;
- skos:altLabel "Unidad Proyectos y Programas"@es ;
- skos:altLabel "Unidad Regional de Asuntos Institucionales (URAI)"@es ;
- skos:altLabel "Unidad Tesorería"@es ;
- skos:altLabel "XVI Región"@es ;
- skos:altLabel "Ñuble 250"@es ;
- skos:altLabel "Órganos Especiales"@es ;
- skos:altLabel "⚙️ SERVICIOS PÚBLICOS REGIONALES"@es ;
- skos:altLabel "🏛️ NIVEL CENTRAL (Estado)"@es ;
- skos:altLabel "📋 SECRETARÍAS REGIONALES MINISTERIALES"@es ;
- skos:altLabel "🗺️ TERRITORIO: 3 PROVINCIAS, 21 COMUNAS"@es ;
- skos:altLabel "🛡️ GOBIERNO INTERIOR"@es ;
- skos:definition "Administrador Regional del GORE Ñuble."@es ;
- skos:definition "Asignación del cargo de Administrador/a Regional."@es ;
- skos:definition "Asignación del cargo de Gobernador/a Regional de Ñuble."@es ;
- skos:definition "Aspecto que mide el porcentaje máximo permitido para gastos administrativos."@es ;
- skos:definition "Capital regional de Ñuble. Principal centro urbano."@es ;
- skos:definition "Cargo de confianza del Gobernador, responsable de la gestión administrativa interna."@es ;
- skos:definition "Cargo de responsabilidad sobre una División del GORE, depende del Administrador Regional."@es ;
- skos:definition "Componente de la base de conocimientos (ABox) que contiene las instancias concretas de la estructura orgánica, la división territorial de la Región de Ñuble, el personal institucional, y elementos compartidos (UoM, Aspects)."@es ;
- skos:definition "División encargada de formular instrumentos de planificación y coordinar la estrategia de desarrollo regional."@es ;
- skos:definition "División encargada de planificación, priorización, evaluación técnica y seguimiento físico de inversión regional."@es ;
- skos:definition "División encargada de políticas y programas de fomento productivo, ciencia, tecnología e innovación."@es ;
- skos:definition "División encargada de programas e iniciativas orientadas a cohesión social, inclusión y acceso a servicios."@es ;
- skos:definition "División encargada de proponer, promover y ejecutar planes y programas regionales en infraestructura, equipamiento regional y gestión en transportes."@es ;
- skos:definition "División responsable de la gestión administrativa y financiera, formulación y ejecución presupuestaria del presupuesto de funcionamiento, provisión de servicios generales y administración del personal."@es ;
- skos:definition "Entidad administradora del SNI y responsable de la evaluación socioeconómica."@es ;
- skos:definition "Instancia político-técnica de filtro de pertinencia estratégica de IPR antes de evaluación técnica."@es ;
- skos:definition "Institución pública encargada de la administración superior de la Región de Ñuble."@es ;
- skos:definition "Miembro electo del Consejo Regional (CORE)."@es ;
- skos:definition "Ministro de fe del CORE, responsable de asesoría técnica y administrativa."@es ;
- skos:definition "Máxima autoridad ejecutiva del Gobierno Regional, electa por sufragio universal."@es ;
- skos:definition "Organismo rector del sistema presupuestario, encargado de la asignación de recursos y evaluación de programas (Glosa 06)."@es ;
- skos:definition "Profesional técnico (DIPIR, DIDESO, DIFOI) responsable de la revisión técnica y financiera de rendiciones."@es ;
- skos:definition "Provincia cordillerana oriente de Ñuble. 5 comunas. Capital: San Carlos."@es ;
- skos:definition "Provincia costera e interior central de Ñuble. 9 comunas. Capital: Bulnes."@es ;
- skos:definition "Representante del Presidente en la región, a cargo del gobierno interior y coordinación de servicios públicos nacionales."@es ;
- skos:definition "Responsable de un Departamento dentro de una División."@es ;
- skos:definition "Responsable de una Unidad dentro de un Departamento o División."@es ;
- skos:definition "Unidad de tiempo equivalente a un doceavo de año."@es ;
- skos:definition "Unidad económica tributaria utilizada en Chile, ajustada mensualmente por inflación."@es ;
- skos:definition "Unidad encargada de fiscalizar legalidad y ejecución financiera/presupuestaria; depende del Gobernador Regional y colabora con el CORE."@es ;
- skos:definition "Unidad especializada en DAF encargada del control y contabilización de rendiciones (SISREC)."@es ;
- skos:definition "XVI Región de Chile, creada por Ley 21.033. Capital: Chillán. 3 provincias, 21 comunas."@es ;
- skos:definition "Órgano colegiado del GORE con facultades normativas, resolutivas y fiscalizadoras."@es ;
- skos:definition "Órgano desconcentrado del DPR que ejerce gobierno interior en la Provincia de Diguillín."@es ;
- skos:definition "Órgano desconcentrado del DPR que ejerce gobierno interior en la Provincia de Itata."@es ;
- skos:definition "Órgano desconcentrado del DPR que ejerce gobierno interior en la Provincia de Punilla."@es ;
- skos:prefLabel "Administrador/a Regional de Ñuble"@es ;
- skos:prefLabel "Administrador/a Regional"@es ;
- skos:prefLabel "Alejandro Aguilera"@es ;
- skos:prefLabel "Alicia Contreras Vielma"@es ;
- skos:prefLabel "Antonieta Soto Trombert"@es ;
- skos:prefLabel "Auditoría Interna"@es ;
- skos:prefLabel "Bulnes"@es ;
- skos:prefLabel "CORFO Regional"@es ;
- skos:prefLabel "Chillán Viejo"@es ;
- skos:prefLabel "Chillán"@es ;
- skos:prefLabel "Cobquecura"@es ;
- skos:prefLabel "Coelemu"@es ;
- skos:prefLabel "Coihueco"@es ;
- skos:prefLabel "Comité Directivo Regional"@es ;
- skos:prefLabel "Comité de Ciencia, Tecnología, Conocimiento e Innovación"@es ;
- skos:prefLabel "Comité de Pertinencia y Vinculación Estratégica"@es ;
- skos:prefLabel "Consejero/a Regional"@es ;
- skos:prefLabel "Consejo Regional de Ñuble"@es ;
- skos:prefLabel "Consejo de la Sociedad Civil"@es ;
- skos:prefLabel "Contraloría General de la República"@es ;
- skos:prefLabel "Corporación Regional de Desarrollo"@es ;
- skos:prefLabel "Cristián Quiroz Reyes"@es ;
- skos:prefLabel "Datos Organizacionales GORE Ñuble"@es ;
- skos:prefLabel "Delegación Presidencial Provincial de Diguillín"@es ;
- skos:prefLabel "Delegación Presidencial Provincial de Itata"@es ;
- skos:prefLabel "Delegación Presidencial Provincial de Punilla"@es ;
- skos:prefLabel "Delegación Presidencial Regional de Ñuble"@es ;
- skos:prefLabel "Departamento Coordinación Integral de Emergencia y Seguridad"@es ;
- skos:prefLabel "Departamento Jurídico"@es ;
- skos:prefLabel "Departamento Zonas en Desarrollo"@es ;
- skos:prefLabel "Departamento de Análisis y Evaluación"@es ;
- skos:prefLabel "Departamento de Ciencia, Tecnología e Innovación"@es ;
- skos:prefLabel "Departamento de Comunicaciones"@es ;
- skos:prefLabel "Departamento de Desarrollo de Proyectos Estratégicos"@es ;
- skos:prefLabel "Departamento de Ejecución y Supervisión de Proyectos de Inversión"@es ;
- skos:prefLabel "Departamento de Finanzas"@es ;
- skos:prefLabel "Departamento de Fomento y Desarrollo Productivo"@es ;
- skos:prefLabel "Departamento de Fondos Concursables y Programas Sociales"@es ;
- skos:prefLabel "Departamento de Gestión Institucional"@es ;
- skos:prefLabel "Departamento de Gestión Territorial"@es ;
- skos:prefLabel "Departamento de Gestión y Desarrollo de Personas"@es ;
- skos:prefLabel "Departamento de Infraestructura y Conectividad"@es ;
- skos:prefLabel "Departamento de Planificación Estratégica y Ordenamiento Territorial"@es ;
- skos:prefLabel "Departamento de Presupuesto"@es ;
- skos:prefLabel "Departamento Ñuble 250"@es ;
- skos:prefLabel "Dirección de Presupuestos"@es ;
- skos:prefLabel "Divisiones del GORE Ñuble"@es ;
- skos:prefLabel "División de Administración y Finanzas"@es ;
- skos:prefLabel "División de Desarrollo Social y Humano"@es ;
- skos:prefLabel "División de Fomento e Industria"@es ;
- skos:prefLabel "División de Infraestructura y Transportes"@es ;
- skos:prefLabel "División de Planificación y Desarrollo Regional"@es ;
- skos:prefLabel "División de Presupuesto e Inversión Regional"@es ;
- skos:prefLabel "El Carmen"@es ;
- skos:prefLabel "Erick Solo de Zaldivar"@es ;
- skos:prefLabel "Gobernador Regional de Ñuble"@es ;
- skos:prefLabel "Gobernador/a Regional"@es ;
- skos:prefLabel "Gobierno Interior (Ñuble)"@es ;
- skos:prefLabel "Gobierno Regional de Ñuble"@es ;
- skos:prefLabel "Gobierno Regional"@es ;
- skos:prefLabel "INDAP Regional"@es ;
- skos:prefLabel "INE Regional"@es ;
- skos:prefLabel "Jefe/a Auditoría Interna"@es ;
- skos:prefLabel "Jefe/a Corporación Regional de Desarrollo"@es ;
- skos:prefLabel "Jefe/a Departamento Coordinación Integral de Emergencia y Seguridad"@es ;
- skos:prefLabel "Jefe/a Departamento Jurídico"@es ;
- skos:prefLabel "Jefe/a Departamento de Comunicaciones"@es ;
- skos:prefLabel "Jefe/a Departamento de Gestión Institucional (DGI)"@es ;
- skos:prefLabel "Jefe/a Departamento Ñuble 250"@es ;
- skos:prefLabel "Jefe/a División DAF"@es ;
- skos:prefLabel "Jefe/a División DIDESO"@es ;
- skos:prefLabel "Jefe/a División DIFOI"@es ;
- skos:prefLabel "Jefe/a División DIINF"@es ;
- skos:prefLabel "Jefe/a División DIPIR"@es ;
- skos:prefLabel "Jefe/a División DIPLADE"@es ;
- skos:prefLabel "Jefe/a Oficina de Partes"@es ;
- skos:prefLabel "Jefe/a URAI"@es ;
- skos:prefLabel "Jefe/a Unidad de Control"@es ;
- skos:prefLabel "Jefe/a Unidad de Gabinete y Participación Social"@es ;
- skos:prefLabel "Jefe/a de Departamento"@es ;
- skos:prefLabel "Jefe/a de División"@es ;
- skos:prefLabel "Jefe/a de Unidad"@es ;
- skos:prefLabel "Juan Parada González"@es ;
- skos:prefLabel "Mes"@es ;
- skos:prefLabel "Ministerio de Desarrollo Social y Familia"@es ;
- skos:prefLabel "Ministerio de Seguridad Pública"@es ;
- skos:prefLabel "Ministerio del Interior"@es ;
- skos:prefLabel "Municipalidad"@es ;
- skos:prefLabel "Ninhue"@es ;
- skos:prefLabel "Nivel Central del Estado (Chile)"@es ;
- skos:prefLabel "Oficina de Informaciones, Reclamos y Sugerencias (OIRS)"@es ;
- skos:prefLabel "Oficina de Partes"@es ;
- skos:prefLabel "Organización Privada Sin Fines de Lucro"@es ;
- skos:prefLabel "Pemuco"@es ;
- skos:prefLabel "Peso Chileno"@es ;
- skos:prefLabel "Pinto"@es ;
- skos:prefLabel "Porcentaje"@es ;
- skos:prefLabel "Portezuelo"@es ;
- skos:prefLabel "Presidencia de la República de Chile"@es ;
- skos:prefLabel "Presidente/a COSOC"@es ;
- skos:prefLabel "Presidente/a Comité CTCI"@es ;
- skos:prefLabel "Provincia de Diguillín"@es ;
- skos:prefLabel "Provincia de Itata"@es ;
- skos:prefLabel "Provincia de Punilla"@es ;
- skos:prefLabel "Quillón"@es ;
- skos:prefLabel "Quirihue"@es ;
- skos:prefLabel "Raúl Súnico Galdames"@es ;
- skos:prefLabel "Referente Técnico Financiero"@es ;
- skos:prefLabel "Región de Ñuble"@es ;
- skos:prefLabel "Ránquil"@es ;
- skos:prefLabel "SAG Regional"@es ;
- skos:prefLabel "SERCOTEC Regional"@es ;
- skos:prefLabel "SEREMI Agricultura"@es ;
- skos:prefLabel "SEREMI Economía"@es ;
- skos:prefLabel "SEREMI Educación"@es ;
- skos:prefLabel "SEREMI Medio Ambiente"@es ;
- skos:prefLabel "SEREMI Obras Públicas"@es ;
- skos:prefLabel "SEREMI Salud"@es ;
- skos:prefLabel "SEREMI Seguridad Pública"@es ;
- skos:prefLabel "SEREMI Trabajo"@es ;
- skos:prefLabel "SEREMI Transportes"@es ;
- skos:prefLabel "SEREMI Vivienda"@es ;
- skos:prefLabel "SEREMIs (Ñuble)"@es ;
- skos:prefLabel "SERNATUR Ñuble"@es ;
- skos:prefLabel "SII Regional"@es ;
- skos:prefLabel "San Carlos"@es ;
- skos:prefLabel "San Fabián"@es ;
- skos:prefLabel "San Ignacio"@es ;
- skos:prefLabel "San Nicolás"@es ;
- skos:prefLabel "Secretario/a Ejecutivo/a"@es ;
- skos:prefLabel "Secretaría Ejecutiva del CORE"@es ;
- skos:prefLabel "Servicio Público"@es ;
- skos:prefLabel "Servicio de Salud Ñuble"@es ;
- skos:prefLabel "Servicios Públicos Regionales (Ñuble)"@es ;
- skos:prefLabel "Staff de Apoyo del GORE Ñuble"@es ;
- skos:prefLabel "Subsecretaría de Desarrollo Regional y Administrativo"@es ;
- skos:prefLabel "Tamara Valenzuela Fuentealba"@es ;
- skos:prefLabel "Tope Gastos Administración"@es ;
- skos:prefLabel "Treguaco"@es ;
- skos:prefLabel "Unidad Regional de Asuntos Internacionales (URAI)"@es ;
- skos:prefLabel "Unidad Tributaria Mensual"@es ;
- skos:prefLabel "Unidad de Adquisiciones"@es ;
- skos:prefLabel "Unidad de Contabilidad y Finanzas"@es ;
- skos:prefLabel "Unidad de Control de Rendiciones"@es ;
- skos:prefLabel "Unidad de Control"@es ;
- skos:prefLabel "Unidad de Gabinete y Participación Social"@es ;
- skos:prefLabel "Unidad de Municipalidades y Conservaciones"@es ;
- skos:prefLabel "Unidad de Operaciones"@es ;
- skos:prefLabel "Unidad de Proyectos y Programas"@es ;
- skos:prefLabel "Unidad de Tesorería"@es ;
- skos:prefLabel "Universidad"@es ;
- skos:prefLabel "Yungay"@es ;
- skos:prefLabel "Álvaro Rivas Rivera"@es ;
- skos:prefLabel "Ñiquén"@es ;
- skos:prefLabel "Órganos Especiales del GORE Ñuble"@es ;
- skos:prefLabel "Óscar Crisóstomo Llanos"@es ;
- skos:scopeNote "Primer gate del flujo de admisibilidad: emite PRE-ADMISIBLE CDR o NO PRE-ADMISIBLE CDR. Ver instancias AdmissibilityState en IPRData."@es ;
