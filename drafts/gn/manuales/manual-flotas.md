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
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/manuales__manual-flotas.md.json
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
