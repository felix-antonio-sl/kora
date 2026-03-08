---
_manifest:
  urn: urn:gn:kb:manual-flotas
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/gestion/kb_gn_047_manual_flotas_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- flotas
- vehiculos
- servicios-generales
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/gestion/kb_gn_047_manual_flotas_koda.yml
    source_hashes:
      domains/gn/03_operacion/gestion/kb_gn_047_manual_flotas_koda.yml: 1aafd1431cafe05ba214aaf313e7971f329c43013726f6b1c95fb710a0adc42f
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.2
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 17
    meat_count: 280
    fat_count: 0
    preserved_facts:
    - AI-Remediator=KODA-TRANSFORMER
    - Creation-Date=2025-12-14
    - Ctx=Operativizar servicios de soporte institucional y administrar flota vehicular
      del GORE.
    - Format=KODA/Spec
    - Human-Creator=GORE Ñuble
    - Human-Editor=FS
    - ID=GN-MANUAL-SERVICIOS-FLOTAS-KODA-01
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
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.ID=GN-MANUAL-SERV-FLOTAS-CONTENT-01
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Nota_de_Cierre.Def=Este manual
      establece los procedimientos para mantener la operatividad de los servicios
      de soporte institucional y la flota vehicular del GORE.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Nota_de_Cierre.ID=GN-MANUAL-SERV-FLOTAS-CIERRE-01
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Objetivo.ID=GN-MANUAL-SERV-FLOTAS-OBJ-01
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Objetivo.Obj=Operativizar
      los servicios de soporte institucional y administrar eficientemente la flota
      vehicular del GORE, garantizando disponibilidad, seguridad y control de costos.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.10_Solicitud_y_Asignacion_de_Vehiculos.Criterios_de_Prioridad[0]=Comisiones
      de servicio oficiales.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.10_Solicitud_y_Asignacion_de_Vehiculos.Criterios_de_Prioridad[1]=Actividades
      del Gobernador y autoridades.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.10_Solicitud_y_Asignacion_de_Vehiculos.Criterios_de_Prioridad[2]=Emergencias
      institucionales.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.10_Solicitud_y_Asignacion_de_Vehiculos.Criterios_de_Prioridad[3]=Traslados
      programados.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.10_Solicitud_y_Asignacion_de_Vehiculos.ID=GN-MANUAL-SERV-FLOTAS-SEC-III-SOL-ASIG-01
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.10_Solicitud_y_Asignacion_de_Vehiculos.Proc[0].Def=Funcionario
      requiere vehículo indicando fecha, hora, destino, propósito.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.10_Solicitud_y_Asignacion_de_Vehiculos.Proc[0].Paso=1.
      Solicitud
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.10_Solicitud_y_Asignacion_de_Vehiculos.Proc[1].Def=Jefatura
      del solicitante autoriza.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.10_Solicitud_y_Asignacion_de_Vehiculos.Proc[1].Paso=2.
      Aprobación
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.10_Solicitud_y_Asignacion_de_Vehiculos.Proc[2].Def=Encargado
      de Flota verifica disponibilidad y asigna vehículo + conductor.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.10_Solicitud_y_Asignacion_de_Vehiculos.Proc[2].Paso=3.
      Asignación
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.10_Solicitud_y_Asignacion_de_Vehiculos.Proc[3].Def=Notificación
      al solicitante y conductor.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.10_Solicitud_y_Asignacion_de_Vehiculos.Proc[3].Paso=4.
      Confirmación
    - 'Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.10_Solicitud_y_Asignacion_de_Vehiculos.Warn=Restricción
      de Uso (D.L. 799)

      Los vehículos estatales no pueden circular en días sábados, domingos ni festivos,
      salvo autorización expresa y fundada por razones de servicio impostergables.

      '
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.11_Bitacora_de_Uso.Campos[0]=Fecha
      y hora de salida/retorno.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.11_Bitacora_de_Uso.Campos[1]=Conductor.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.11_Bitacora_de_Uso.Campos[2]=Destino
      y propósito.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.11_Bitacora_de_Uso.Campos[3]=Kilometraje
      inicial y final.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.11_Bitacora_de_Uso.Campos[4]=Observaciones
      (estado del vehículo, incidentes).
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.11_Bitacora_de_Uso.ID=GN-MANUAL-SERV-FLOTAS-SEC-III-BITACORA-01
    - 'Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.11_Bitacora_de_Uso.Modalidad[0]=Digital:
      Registro en sistema o aplicación móvil.'
    - 'Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.11_Bitacora_de_Uso.Modalidad[1]=Física:
      Cuaderno en el vehículo (respaldo).'
    - 'Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.11_Bitacora_de_Uso.Req=Registro
      obligatorio de cada salida:'
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.12_Control_de_Combustible.Analisis_de_Rendimiento[0]=Km/litro
      por vehículo.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.12_Control_de_Combustible.Analisis_de_Rendimiento[1]=Comparación
      con estándar del fabricante.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.12_Control_de_Combustible.Analisis_de_Rendimiento[2]=Alertas
      por consumos anómalos.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.12_Control_de_Combustible.ID=GN-MANUAL-SERV-FLOTAS-SEC-III-COMBUST-01
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.12_Control_de_Combustible.Registro_de_Cargas[0]=Fecha
      y estación de servicio.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.12_Control_de_Combustible.Registro_de_Cargas[1]=Litros
      cargados.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.12_Control_de_Combustible.Registro_de_Cargas[2]=Monto.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.12_Control_de_Combustible.Registro_de_Cargas[3]=Kilometraje
      al momento de carga.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.12_Control_de_Combustible.Tarjeta_de_Combustible.Def=Asignada
      a cada vehículo (ej. ServiEstado, Copec).
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.13_Control_de_Kilometraje.ID=GN-MANUAL-SERV-FLOTAS-SEC-III-KM-01
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.13_Control_de_Kilometraje.Req[0]=Registro
      mensual del odómetro de cada vehículo.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.13_Control_de_Kilometraje.Req[1]=Proyección
      de mantenciones según kilometraje.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.13_Control_de_Kilometraje.Req[2]=Detección
      de usos no autorizados.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.8_Registro_de_Vehiculos.Datos_Administrativos[0]=Código
      de activo fijo (vinculación con Manual 2.3).
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.8_Registro_de_Vehiculos.Datos_Administrativos[1]=Fecha
      de adquisición y valor.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.8_Registro_de_Vehiculos.Datos_Administrativos[2]=Responsable
      asignado.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.8_Registro_de_Vehiculos.Datos_Administrativos[3]=Centro
      de costo.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.8_Registro_de_Vehiculos.Datos_de_Identificacion[0]=Patente.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.8_Registro_de_Vehiculos.Datos_de_Identificacion[1]=Marca,
      modelo, año.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.8_Registro_de_Vehiculos.Datos_de_Identificacion[2]=Número
      de chasis y motor.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.8_Registro_de_Vehiculos.Datos_de_Identificacion[3]=Color.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.8_Registro_de_Vehiculos.Datos_de_Identificacion[4]=Tipo
      (sedan, camioneta, minibús, etc.).
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.8_Registro_de_Vehiculos.Documentacion_Vigente[0]=Permiso
      de circulación.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.8_Registro_de_Vehiculos.Documentacion_Vigente[1]=Revisión
      técnica.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.8_Registro_de_Vehiculos.Documentacion_Vigente[2]=Seguro
      obligatorio (SOAP).
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.8_Registro_de_Vehiculos.Documentacion_Vigente[3]=Seguro
      automotriz voluntario.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.8_Registro_de_Vehiculos.Equipamiento[0]=Accesorios
      instalados (GPS, radio, botiquín, extintor).
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.8_Registro_de_Vehiculos.Equipamiento[1]=Kit
      de emergencia.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.8_Registro_de_Vehiculos.ID=GN-MANUAL-SERV-FLOTAS-SEC-III-REG-VEH-01
    - 'Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.8_Registro_de_Vehiculos.Req=Cada
      vehículo institucional debe tener ficha completa:'
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.9_Registro_de_Conductores.Actualizacion.Def=Control
      de vencimiento de licencias con alertas.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.9_Registro_de_Conductores.ID=GN-MANUAL-SERV-FLOTAS-SEC-III-REG-CONDUCT-01
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.9_Registro_de_Conductores.Req=Nómina
      de funcionarios autorizados para conducir vehículos institucionales.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.9_Registro_de_Conductores.Requisitos[0]=Licencia
      de conducir vigente (clase apropiada).
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.9_Registro_de_Conductores.Requisitos[1]=Hoja
      de vida sin infracciones graves.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.9_Registro_de_Conductores.Requisitos[2]=Autorización
      formal (resolución o memorando).
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.ID=GN-MANUAL-SERV-FLOTAS-SEC-III-01
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.Restricciones_Legales_Adquisicion.ID=GN-MANUAL-SERV-FLOTAS-SEC-III-RESTR-LEY-01
    - 'Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.Restricciones_Legales_Adquisicion.Req=Autorización
      Previa de DIPRES (Art. 12 Ley Presupuestos)

      La adquisición de vehículos motorizados, a cualquier título, requiere autorización
      previa de la Dirección de Presupuestos (DIPRES) cuando su precio supere el monto
      fijado por dicha dirección. Esta restricción aplica también a vehículos adquiridos
      vía proyectos de inversión.

      '
    - 'Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_III_Gestion_de_Flota_Vehicular.Title=Sección
      III: Gestión de Flota Vehicular'
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.4_Tipos_de_Mantencion.ID=GN-MANUAL-SERV-FLOTAS-SEC-II-TIPOS-01
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.4_Tipos_de_Mantencion.Tipos[0].Def=Programada
      para evitar fallas (revisiones periódicas).
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.4_Tipos_de_Mantencion.Tipos[0].Tipo=Preventiva
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.4_Tipos_de_Mantencion.Tipos[1].Def=Reparación
      de fallas o daños detectados.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.4_Tipos_de_Mantencion.Tipos[1].Tipo=Correctiva
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.4_Tipos_de_Mantencion.Tipos[2].Def=Atención
      inmediata ante situaciones críticas (filtraciones, cortes eléctricos).
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.4_Tipos_de_Mantencion.Tipos[2].Tipo=Emergencia
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.5_Plan_de_Mantencion_Preventiva.Contenido[0]=Listado
      de equipos e instalaciones a mantener.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.5_Plan_de_Mantencion_Preventiva.Contenido[1]=Frecuencia
      de intervención (mensual, trimestral, anual).
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.5_Plan_de_Mantencion_Preventiva.Contenido[2]=Responsable
      de ejecución (interno o contratista).
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.5_Plan_de_Mantencion_Preventiva.Contenido[3]=Presupuesto
      estimado.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.5_Plan_de_Mantencion_Preventiva.Elaboracion.Base=Inventario
      de instalaciones y equipos.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.5_Plan_de_Mantencion_Preventiva.Elaboracion.Frecuencia=Anual
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.5_Plan_de_Mantencion_Preventiva.ID=GN-MANUAL-SERV-FLOTAS-SEC-II-PLAN-PREV-01
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.5_Plan_de_Mantencion_Preventiva.Seguimiento.Def=Calendario
      de actividades con alertas automáticas.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.6_Ordenes_de_Trabajo.Asignacion[0]=A
      técnico interno
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.6_Ordenes_de_Trabajo.Asignacion[1]=Derivación
      a contratista
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.6_Ordenes_de_Trabajo.Cierre[0]=Validación
      por solicitante
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.6_Ordenes_de_Trabajo.Cierre[1]=Actualización
      de hoja de vida del equipo
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.6_Ordenes_de_Trabajo.Contenido[0]=Descripción
      del requerimiento.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.6_Ordenes_de_Trabajo.Contenido[1]=Ubicación
      y equipo afectado.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.6_Ordenes_de_Trabajo.Contenido[2]=Prioridad
      (alta, media, baja).
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.6_Ordenes_de_Trabajo.Contenido[3]=Fecha
      de solicitud.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.6_Ordenes_de_Trabajo.Def=Instrumento
      formal para solicitar y documentar intervenciones.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.6_Ordenes_de_Trabajo.Ejecucion[0]=Registro
      de trabajos realizados
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.6_Ordenes_de_Trabajo.Ejecucion[1]=Materiales
      usados
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.6_Ordenes_de_Trabajo.Ejecucion[2]=Horas
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.6_Ordenes_de_Trabajo.Generacion[0]=Por
      usuario (falla reportada)
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.6_Ordenes_de_Trabajo.Generacion[1]=Automática
      (plan preventivo)
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.6_Ordenes_de_Trabajo.ID=GN-MANUAL-SERV-FLOTAS-SEC-II-OT-01
    - 'Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.7_Control_de_Elementos_de_Seguridad.Elementos[0]=Extintores:
      Carga, vencimiento, ubicación, señalética.'
    - 'Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.7_Control_de_Elementos_de_Seguridad.Elementos[1]=Red
      húmeda y seca: Pruebas periódicas.'
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.7_Control_de_Elementos_de_Seguridad.Elementos[2]=Iluminación
      de emergencia.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.7_Control_de_Elementos_de_Seguridad.Elementos[3]=Señalética
      de evacuación.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.7_Control_de_Elementos_de_Seguridad.Elementos[4]=Detectores
      de humo y alarmas.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.7_Control_de_Elementos_de_Seguridad.ID=GN-MANUAL-SERV-FLOTAS-SEC-II-SEG-01
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.ID=GN-MANUAL-SERV-FLOTAS-SEC-II-01
    - 'Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_II_Mantencion_de_Infraestructura.Title=Sección
      II: Mantención de Infraestructura'
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.14_Plan_de_Mantencion_Vehicular.ID=GN-MANUAL-SERV-FLOTAS-SEC-IV-PLAN-01
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.14_Plan_de_Mantencion_Vehicular.Mantencion_Correctiva[0]=Reparación
      de fallas detectadas.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.14_Plan_de_Mantencion_Vehicular.Mantencion_Correctiva[1]=Prioridad
      según criticidad.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.14_Plan_de_Mantencion_Vehicular.Mantencion_Mayor[0]=Overhaul
      de motor, transmisión.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.14_Plan_de_Mantencion_Vehicular.Mantencion_Mayor[1]=Evaluación
      costo/beneficio vs. reemplazo del vehículo.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.14_Plan_de_Mantencion_Vehicular.Mantencion_Preventiva[0]=Según
      manual del fabricante y kilometraje.
    - 'Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.14_Plan_de_Mantencion_Vehicular.Mantencion_Preventiva[1]=Típico:
      Cada 5.000, 10.000, 20.000 km.'
    - 'Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.14_Plan_de_Mantencion_Vehicular.Mantencion_Preventiva[2]=Incluye:
      Cambio de aceite, filtros, revisión de frenos, neumáticos.'
    - 'Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.15_Ordenes_de_Trabajo_Vehicular.Def=Similar
      a mantención de infraestructura:'
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.15_Ordenes_de_Trabajo_Vehicular.ID=GN-MANUAL-SERV-FLOTAS-SEC-IV-OT-01
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.15_Ordenes_de_Trabajo_Vehicular.Proc[0]=Generación
      por plan o por reporte de falla.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.15_Ordenes_de_Trabajo_Vehicular.Proc[1]=Asignación
      a taller interno o externo (contratista autorizado).
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.15_Ordenes_de_Trabajo_Vehicular.Proc[2]=Registro
      de trabajos, repuestos, costos.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.15_Ordenes_de_Trabajo_Vehicular.Proc[3]=Actualización
      de hoja de vida del vehículo.
    - 'Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.16_Control_de_Documentacion.Def=Alertas
      automáticas para vencimientos:'
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.16_Control_de_Documentacion.ID=GN-MANUAL-SERV-FLOTAS-SEC-IV-DOC-01
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.16_Control_de_Documentacion.Table.Columns[0]=Documento
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.16_Control_de_Documentacion.Table.Columns[1]=Frecuencia
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.16_Control_de_Documentacion.Table.Columns[2]=Responsable
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.16_Control_de_Documentacion.Table.Rows[0].Documento=Permiso
      de Circulación
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.16_Control_de_Documentacion.Table.Rows[0].Frecuencia=Anual
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.16_Control_de_Documentacion.Table.Rows[0].Responsable=Encargado
      Flota
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.16_Control_de_Documentacion.Table.Rows[1].Documento=Revisión
      Técnica
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.16_Control_de_Documentacion.Table.Rows[1].Frecuencia=Semestral/Anual
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.16_Control_de_Documentacion.Table.Rows[1].Responsable=Encargado
      Flota
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.16_Control_de_Documentacion.Table.Rows[2].Documento=SOAP
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.16_Control_de_Documentacion.Table.Rows[2].Frecuencia=Anual
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.16_Control_de_Documentacion.Table.Rows[2].Responsable=Encargado
      Flota
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.16_Control_de_Documentacion.Table.Rows[3].Documento=Seguro
      Automotriz
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.16_Control_de_Documentacion.Table.Rows[3].Frecuencia=Anual
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.16_Control_de_Documentacion.Table.Rows[3].Responsable=Encargado
      Flota
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.16_Control_de_Documentacion.Table.Rows[4].Documento=Licencia
      Conductor
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.16_Control_de_Documentacion.Table.Rows[4].Frecuencia=Según
      vencimiento
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.16_Control_de_Documentacion.Table.Rows[4].Responsable=RRHH
      / Conductor
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.17_Siniestros_y_Accidentes.ID=GN-MANUAL-SERV-FLOTAS-SEC-IV-ACC-01
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.17_Siniestros_y_Accidentes.Proc[0]=1.
      Asegurar integridad de personas.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.17_Siniestros_y_Accidentes.Proc[1]=2.
      Notificar a Carabineros y compañía de seguros.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.17_Siniestros_y_Accidentes.Proc[2]=3.
      Documentar con fotografías y croquis.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.17_Siniestros_y_Accidentes.Proc[3]=4.
      Reportar a Encargado de Flota y jefatura.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.17_Siniestros_y_Accidentes.Proc[4]=5.
      Gestionar denuncia y reclamo al seguro.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.17_Siniestros_y_Accidentes.Proc[5]=6.
      Evaluar responsabilidad del conductor (posible sumario).
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.17_Siniestros_y_Accidentes.Proc[6]=7.
      Reparación o baja del vehículo según daño.
    - 'Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.17_Siniestros_y_Accidentes.Title=Procedimiento
      ante accidente:'
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.ID=GN-MANUAL-SERV-FLOTAS-SEC-IV-01
    - 'Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_IV_Mantencion_de_Vehiculos.Title=Sección
      IV: Mantención de Vehículos'
    - 'Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.1_Alcance_de_Servicios_Generales.Def=Servicios
      transversales de apoyo a la operación institucional:'
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.1_Alcance_de_Servicios_Generales.ID=GN-MANUAL-SERV-FLOTAS-SEC-I-ALCANCE-01
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.1_Alcance_de_Servicios_Generales.Servicios[0].Alcance=Edificios,
      instalaciones, sistemas eléctricos, sanitarios.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.1_Alcance_de_Servicios_Generales.Servicios[0].Servicio=Mantención
      de Infraestructura
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.1_Alcance_de_Servicios_Generales.Servicios[1].Alcance=Limpieza
      de oficinas, áreas comunes, jardines.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.1_Alcance_de_Servicios_Generales.Servicios[1].Servicio=Aseo
      y Ornato
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.1_Alcance_de_Servicios_Generales.Servicios[2].Alcance=Vigilancia,
      control de acceso, circuito cerrado.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.1_Alcance_de_Servicios_Generales.Servicios[2].Servicio=Seguridad
      Física
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.1_Alcance_de_Servicios_Generales.Servicios[3].Ctx=Si
      aplica.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.1_Alcance_de_Servicios_Generales.Servicios[3].Servicio=Cafetería
      y Servicios de Alimentación
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.1_Alcance_de_Servicios_Generales.Servicios[4].Alcance=Distribución
      interna y externa de correspondencia.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.1_Alcance_de_Servicios_Generales.Servicios[4].Servicio=Correo
      y Mensajería
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.1_Alcance_de_Servicios_Generales.Servicios[5].Alcance=Asignación
      y control de espacios.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.1_Alcance_de_Servicios_Generales.Servicios[5].Servicio=Gestión
      de Estacionamientos
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.2_Organizacion_del_Area.ID=GN-MANUAL-SERV-FLOTAS-SEC-I-ORG-01
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.2_Organizacion_del_Area.Roles[0].Def=Responsable
      de la coordinación integral.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.2_Organizacion_del_Area.Roles[0].Rol=Jefe
      de Servicios Generales
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.2_Organizacion_del_Area.Roles[1].Areas[0]=Mantención
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.2_Organizacion_del_Area.Roles[1].Areas[1]=Aseo
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.2_Organizacion_del_Area.Roles[1].Areas[2]=Seguridad
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.2_Organizacion_del_Area.Roles[1].Rol=Supervisores
      por Área
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.2_Organizacion_del_Area.Roles[2].Def=Funcionarios
      propios o empresas contratadas.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.2_Organizacion_del_Area.Roles[2].Rol=Personal
      Operativo
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.2_Organizacion_del_Area.Roles[3].Purp=Para
      contrataciones, pagos y control presupuestario.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.2_Organizacion_del_Area.Roles[3].Rol=Coordinación
      con DAF
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.3_Contratos_de_Servicios_Externalizados.Administracion_de_Contratos.Act[0]=Designación
      de Administrador del Contrato.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.3_Contratos_de_Servicios_Externalizados.Administracion_de_Contratos.Act[1]=Verificación
      de cumplimiento de dotaciones y horarios.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.3_Contratos_de_Servicios_Externalizados.Administracion_de_Contratos.Act[2]=Libro
      de novedades para registro de incidencias.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.3_Contratos_de_Servicios_Externalizados.Administracion_de_Contratos.Act[3]=Evaluación
      periódica del servicio.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.3_Contratos_de_Servicios_Externalizados.Administracion_de_Contratos.Act[4]=Aplicación
      de multas según bases contractuales.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.3_Contratos_de_Servicios_Externalizados.Administracion_de_Contratos.ID=GN-MANUAL-SERV-FLOTAS-SEC-I-ADMIN-CONTRATOS-01
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.3_Contratos_de_Servicios_Externalizados.Contratos[0].Def=Contrato
      de servicio con empresa especializada.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.3_Contratos_de_Servicios_Externalizados.Contratos[0].Servicio=Aseo
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.3_Contratos_de_Servicios_Externalizados.Contratos[1].Def=Contrato
      de vigilancia privada.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.3_Contratos_de_Servicios_Externalizados.Contratos[1].Servicio=Seguridad
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.3_Contratos_de_Servicios_Externalizados.Contratos[2].Def=Contrato
      de jardinería.
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.3_Contratos_de_Servicios_Externalizados.Contratos[2].Servicio=Mantención
      de Áreas Verdes
    - Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas.Seccion_I_Servicios_Generales.3_Contratos_de_Servicios_Externalizados.Contratos[3].Def=Contratos
      especializados.
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
---

# Manual 2.4: Servicios Generales y Gestión de Flotas
## ID
GN-MANUAL-SERVICIOS-FLOTAS-KODA-01

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

## Source ID
MANUAL-SERVICIOS-FLOTAS-01

## Primary Source
staging/brow_speculativo/manual_2_4_servicios_flotas.md

## Ctx
Operativizar servicios de soporte institucional y administrar flota vehicular del GORE.

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


## Manual 2 4 Servicios Generales y Gestion de Flotas
### ID
GN-MANUAL-SERV-FLOTAS-CONTENT-01
### Title
Manual 2.4: Servicios Generales y Gestión de Flotas
### Objetivo
#### ID
GN-MANUAL-SERV-FLOTAS-OBJ-01
#### Obj
Operativizar los servicios de soporte institucional y administrar eficientemente la flota vehicular del GORE, garantizando disponibilidad, seguridad y control de costos.
### Seccion I Servicios Generales
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-I-01
#### Title
Sección I: Servicios Generales
#### 1 Alcance de Servicios Generales
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-I-ALCANCE-01
#### Def
Servicios transversales de apoyo a la operación institucional:
#### Servicios
-
  #### Servicio
  Mantención de Infraestructura
  #### Alcance
  Edificios, instalaciones, sistemas eléctricos, sanitarios.
-
  #### Servicio
  Aseo y Ornato
  #### Alcance
  Limpieza de oficinas, áreas comunes, jardines.
-
  #### Servicio
  Seguridad Física
  #### Alcance
  Vigilancia, control de acceso, circuito cerrado.
-
  #### Servicio
  Cafetería y Servicios de Alimentación
  #### Ctx
  Si aplica.
-
  #### Servicio
  Correo y Mensajería
  #### Alcance
  Distribución interna y externa de correspondencia.
-
  #### Servicio
  Gestión de Estacionamientos
  #### Alcance
  Asignación y control de espacios.
#### 2 Organizacion del Area
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-I-ORG-01
#### Roles
-
  #### Rol
  Jefe de Servicios Generales
  #### Def
  Responsable de la coordinación integral.
-
  #### Rol
  Supervisores por Área
  #### Areas
  - Mantención
  - Aseo
  - Seguridad
-
  #### Rol
  Personal Operativo
  #### Def
  Funcionarios propios o empresas contratadas.
-
  #### Rol
  Coordinación con DAF
  #### Purp
  Para contrataciones, pagos y control presupuestario.
#### 3 Contratos de Servicios Externalizados
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-I-CONTRATOS-01
#### Def
La mayoría de servicios generales se ejecutan mediante contratos externos:
#### Contratos
| Servicio | Def |
| --- | --- |
| Aseo | Contrato de servicio con empresa especializada. |
| Seguridad | Contrato de vigilancia privada. |
| Mantención de Áreas Verdes | Contrato de jardinería. |
| Mantención de Ascensores/Equipos | Contratos especializados. |
#### Administracion de Contratos
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-I-ADMIN-CONTRATOS-01
#### Act
- Designación de Administrador del Contrato.
- Verificación de cumplimiento de dotaciones y horarios.
- Libro de novedades para registro de incidencias.
- Evaluación periódica del servicio.
- Aplicación de multas según bases contractuales.
### Seccion II Mantencion de Infraestructura
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-II-01
#### Title
Sección II: Mantención de Infraestructura
#### 4 Tipos de Mantencion
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-II-TIPOS-01
#### Tipos
| Tipo | Def |
| --- | --- |
| Preventiva | Programada para evitar fallas (revisiones periódicas). |
| Correctiva | Reparación de fallas o daños detectados. |
| Emergencia | Atención inmediata ante situaciones críticas (filtraciones, cortes eléctricos). |
#### 5 Plan de Mantencion Preventiva
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-II-PLAN-PREV-01
#### Elaboracion
#### Frecuencia
Anual
#### Base
Inventario de instalaciones y equipos.
#### Contenido
- Listado de equipos e instalaciones a mantener.
- Frecuencia de intervención (mensual, trimestral, anual).
- Responsable de ejecución (interno o contratista).
- Presupuesto estimado.
#### Seguimiento
#### Def
Calendario de actividades con alertas automáticas.
#### 6 Ordenes de Trabajo
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-II-OT-01
#### Def
Instrumento formal para solicitar y documentar intervenciones.
#### Generacion
- Por usuario (falla reportada)
- Automática (plan preventivo)
#### Contenido
- Descripción del requerimiento.
- Ubicación y equipo afectado.
- Prioridad (alta, media, baja).
- Fecha de solicitud.
#### Asignacion
- A técnico interno
- Derivación a contratista
#### Ejecucion
- Registro de trabajos realizados
- Materiales usados
- Horas
#### Cierre
- Validación por solicitante
- Actualización de hoja de vida del equipo
#### 7 Control de Elementos de Seguridad
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-II-SEG-01
#### Elementos
- Extintores: Carga, vencimiento, ubicación, señalética.
- Red húmeda y seca: Pruebas periódicas.
- Iluminación de emergencia.
- Señalética de evacuación.
- Detectores de humo y alarmas.
### Seccion III Gestion de Flota Vehicular
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-III-01
#### Title
Sección III: Gestión de Flota Vehicular
#### Restricciones Legales Adquisicion
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-III-RESTR-LEY-01
#### Req
Autorización Previa de DIPRES (Art. 12 Ley Presupuestos)
La adquisición de vehículos motorizados, a cualquier título, requiere autorización previa de la Dirección de Presupuestos (DIPRES) cuando su precio supere el monto fijado por dicha dirección. Esta restricción aplica también a vehículos adquiridos vía proyectos de inversión.

#### 8 Registro de Vehiculos
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-III-REG-VEH-01
#### Req
Cada vehículo institucional debe tener ficha completa:
#### Datos de Identificacion
- Patente.
- Marca, modelo, año.
- Número de chasis y motor.
- Color.
- Tipo (sedan, camioneta, minibús, etc.).
#### Datos Administrativos
- Código de activo fijo (vinculación con Manual 2.3).
- Fecha de adquisición y valor.
- Responsable asignado.
- Centro de costo.
#### Documentacion Vigente
- Permiso de circulación.
- Revisión técnica.
- Seguro obligatorio (SOAP).
- Seguro automotriz voluntario.
#### Equipamiento
- Accesorios instalados (GPS, radio, botiquín, extintor).
- Kit de emergencia.
#### 9 Registro de Conductores
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-III-REG-CONDUCT-01
#### Req
Nómina de funcionarios autorizados para conducir vehículos institucionales.
#### Requisitos
- Licencia de conducir vigente (clase apropiada).
- Hoja de vida sin infracciones graves.
- Autorización formal (resolución o memorando).
#### Actualizacion
#### Def
Control de vencimiento de licencias con alertas.
#### 10 Solicitud y Asignacion de Vehiculos
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-III-SOL-ASIG-01
#### Proc
| Paso | Def |
| --- | --- |
| 1. Solicitud | Funcionario requiere vehículo indicando fecha, hora, destino, propósito. |
| 2. Aprobación | Jefatura del solicitante autoriza. |
| 3. Asignación | Encargado de Flota verifica disponibilidad y asigna vehículo + conductor. |
| 4. Confirmación | Notificación al solicitante y conductor. |
#### Criterios de Prioridad
- Comisiones de servicio oficiales.
- Actividades del Gobernador y autoridades.
- Emergencias institucionales.
- Traslados programados.
#### Warn
Restricción de Uso (D.L. 799)
Los vehículos estatales no pueden circular en días sábados, domingos ni festivos, salvo autorización expresa y fundada por razones de servicio impostergables.

#### 11 Bitacora de Uso
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-III-BITACORA-01
#### Req
Registro obligatorio de cada salida:
#### Campos
- Fecha y hora de salida/retorno.
- Conductor.
- Destino y propósito.
- Kilometraje inicial y final.
- Observaciones (estado del vehículo, incidentes).
#### Modalidad
- Digital: Registro en sistema o aplicación móvil.
- Física: Cuaderno en el vehículo (respaldo).
#### 12 Control de Combustible
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-III-COMBUST-01
#### Tarjeta de Combustible
#### Def
Asignada a cada vehículo (ej. ServiEstado, Copec).
#### Registro de Cargas
- Fecha y estación de servicio.
- Litros cargados.
- Monto.
- Kilometraje al momento de carga.
#### Analisis de Rendimiento
- Km/litro por vehículo.
- Comparación con estándar del fabricante.
- Alertas por consumos anómalos.
#### 13 Control de Kilometraje
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-III-KM-01
#### Req
- Registro mensual del odómetro de cada vehículo.
- Proyección de mantenciones según kilometraje.
- Detección de usos no autorizados.
### Seccion IV Mantencion de Vehiculos
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-IV-01
#### Title
Sección IV: Mantención de Vehículos
#### 14 Plan de Mantencion Vehicular
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-IV-PLAN-01
#### Mantencion Preventiva
- Según manual del fabricante y kilometraje.
- Típico: Cada 5.000, 10.000, 20.000 km.
- Incluye: Cambio de aceite, filtros, revisión de frenos, neumáticos.
#### Mantencion Correctiva
- Reparación de fallas detectadas.
- Prioridad según criticidad.
#### Mantencion Mayor
- Overhaul de motor, transmisión.
- Evaluación costo/beneficio vs. reemplazo del vehículo.
#### 15 Ordenes de Trabajo Vehicular
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-IV-OT-01
#### Def
Similar a mantención de infraestructura:
#### Proc
- Generación por plan o por reporte de falla.
- Asignación a taller interno o externo (contratista autorizado).
- Registro de trabajos, repuestos, costos.
- Actualización de hoja de vida del vehículo.
#### 16 Control de Documentacion
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-IV-DOC-01
#### Def
Alertas automáticas para vencimientos:
#### Table
#### Columns
- Documento
- Frecuencia
- Responsable
#### Rows
| Documento | Frecuencia | Responsable |
| --- | --- | --- |
| Permiso de Circulación | Anual | Encargado Flota |
| Revisión Técnica | Semestral/Anual | Encargado Flota |
| SOAP | Anual | Encargado Flota |
| Seguro Automotriz | Anual | Encargado Flota |
| Licencia Conductor | Según vencimiento | RRHH / Conductor |
#### 17 Siniestros y Accidentes
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-IV-ACC-01
#### Title
Procedimiento ante accidente:
#### Proc
- 1. Asegurar integridad de personas.
- 2. Notificar a Carabineros y compañía de seguros.
- 3. Documentar con fotografías y croquis.
- 4. Reportar a Encargado de Flota y jefatura.
- 5. Gestionar denuncia y reclamo al seguro.
- 6. Evaluar responsabilidad del conductor (posible sumario).
- 7. Reparación o baja del vehículo según daño.
### Seccion V Control y Reporteria
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-V-01
#### Title
Sección V: Control y Reportería
#### 18 Indicadores de Gestion de Flota
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-V-IND-01
#### Indicadores
- Disponibilidad: % de tiempo operativo vs. mantenimiento.
- Utilización: % de uso efectivo vs. capacidad disponible.
- Costo por Kilómetro: (Combustible + Mantención + Seguros) / Km recorridos.
- Costo por Vehículo: Gastos totales mensuales/anuales.
- Incidentes: Número de accidentes, multas de tránsito.
#### 19 Reportes Periodicos
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-V-REP-01
#### Reportes
-
  #### Reporte
  Informe Mensual de Flota
  #### Contenido
  - Estado de cada vehículo.
  - Kilometraje recorrido.
  - Consumo de combustible.
  - Mantenciones realizadas.
  - Costos incurridos.
-
  #### Reporte
  Informe de Vencimientos
  #### Def
  Documentos próximos a vencer.
-
  #### Reporte
  Ranking de Conductores
  #### Def
  Por consumo, incidentes, multas.
#### 20 Auditoria de Uso
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-V-AUD-01
#### Act
- Verificación de coherencia entre bitácora, combustible y kilometraje.
- Detección de usos no autorizados o fuera de horario.
- Cruce con comisiones de servicio autorizadas.
### Seccion VI Disposiciones Especiales
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-VI-01
#### Title
Sección VI: Disposiciones Especiales
#### 21 Vehiculos en Comodato o Arriendo
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-VI-COMODATO-01
#### Tipos
| Tipo | Def |
| --- | --- |
| Comodato Recibido | Vehículos de otras instituciones en uso temporal. |
| Arriendo Operativo | Contratos de leasing o arriendo sin transferencia de propiedad. |
#### Control
#### Def
Mismo régimen de bitácora, combustible y mantención.
#### Contabilidad
#### Def
Registro como gasto de arriendo, no como activo fijo.
#### 22 Baja de Vehiculos
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-VI-BAJA-01
#### Ctx
Procedimiento según Manual 2.3 (Activo Fijo):
#### Proc
- Informe técnico de obsolescencia o siniestro.
- Resolución de baja.
- Destino: Remate, donación o destrucción.
- Trámites legales: Transferencia de dominio o baja registral.
#### 23 Responsabilidades
#### ID
GN-MANUAL-SERV-FLOTAS-SEC-VI-RESP-01
#### Roles
| Rol | Resp |
| --- | --- |
| Conductor | ['Uso correcto', 'Registro de bitácora', 'Reporte de fallas'] |
| Encargado de Flota | Planificación, asignación, control documental. |
| Jefe de Servicios Generales | Supervisión integral del área. |
| DAF | Control presupuestario y de contratos. |
### Nota de Cierre
#### ID
GN-MANUAL-SERV-FLOTAS-CIERRE-01
#### Def
Este manual establece los procedimientos para mantener la operatividad de los servicios de soporte institucional y la flota vehicular del GORE.

## Referencias Cruzadas
### ID
GN-MANUAL-SERV-FLOTAS-XREF-01
### Ctx Optional
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_3_activo_fijo.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_1_compras_koda.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_2_contabilidad.yml
