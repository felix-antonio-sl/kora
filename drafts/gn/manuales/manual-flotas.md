---
_manifest:
  urn: urn:gn:kb:manual-flotas
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
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
    cr: 3.81
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    document_family: generic
    publication_class: knowledge
    skeleton_count: 2
    meat_count: 248
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/manuales__manual-flotas.md.json
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:gn:kb:manual-flotas
---

# Manual 2.4: Servicios Generales y Gestión de Flotas
## Manual 2 4 Servicios Generales y Gestion de Flotas
- **Titulo:** Manual 2.4: Servicios Generales y Gestión de Flotas
## Objetivo
- **Objetivos:** Operativizar los servicios de soporte institucional y administrar eficientemente la flota vehicular del GORE, garantizando disponibilidad, seguridad y control de costos.
## Seccion I Servicios Generales
- **Titulo:** Sección I: Servicios Generales
### 1 Alcance de Servicios Generales
- **Definicion:** Servicios transversales de apoyo a la operación institucional:
### Servicios
| Servicio | Alcance |
| --- | --- |
| Mantención de Infraestructura | Edificios, instalaciones, sistemas eléctricos, sanitarios. |
| Aseo y Ornato | Limpieza de oficinas, áreas comunes, jardines. |
| Seguridad Física | Vigilancia, control de acceso, circuito cerrado. |
| Cafetería y Servicios de Alimentación | |
| Correo y Mensajería | Distribución interna y externa de correspondencia. |
| Gestión de Estacionamientos | Asignación y control de espacios. |
### 2 Organizacion del Area
### Roles
| Rol | Def |
| --- | --- |
| Jefe de Servicios Generales | Responsable de la coordinación integral. |
| Supervisores por Área | |
| Personal Operativo | Funcionarios propios o empresas contratadas. |
| Coordinación con DAF | |
### 3 Contratos de Servicios Externalizados
- **Definicion:** La mayoría de servicios generales se ejecutan mediante contratos externos:
### Contratos
| Servicio | Def |
| --- | --- |
| Aseo | Contrato de servicio con empresa especializada. |
| Seguridad | Contrato de vigilancia privada. |
| Mantención de Áreas Verdes | Contrato de jardinería. |
| Mantención de Ascensores/Equipos | Contratos especializados. |
### Administracion de Contratos
- **Acciones:** Designación de Administrador del Contrato., Verificación de cumplimiento de dotaciones y horarios., Libro de novedades para registro de incidencias., Evaluación periódica del servicio., Aplicación de multas según bases contractuales.
## Seccion II Mantencion de Infraestructura
- **Titulo:** Sección II: Mantención de Infraestructura
### 4 Tipos de Mantencion
### Tipos
| Tipo | Def |
| --- | --- |
| Preventiva | Programada para evitar fallas (revisiones periódicas). |
| Correctiva | Reparación de fallas o daños detectados. |
| Emergencia | Atención inmediata ante situaciones críticas (filtraciones, cortes eléctricos). |
### 5 Plan de Mantencion Preventiva
- **Contenido:** Listado de equipos e instalaciones a mantener., Frecuencia de intervención (mensual, trimestral, anual)., Responsable de ejecución (interno o contratista)., Presupuesto estimado.
### Elaboracion
- **Frecuencia:** Anual
- **Base:** Inventario de instalaciones y equipos.
### Seguimiento
- **Definicion:** Calendario de actividades con alertas automáticas.
### 6 Ordenes de Trabajo
- **Definicion:** Instrumento formal para solicitar y documentar intervenciones.
- **Generacion:** Por usuario (falla reportada), Automática (plan preventivo)
- **Contenido:** Descripción del requerimiento., Ubicación y equipo afectado., Prioridad (alta, media, baja)., Fecha de solicitud.
- **Asignacion:** A técnico interno, Derivación a contratista
- **Ejecucion:** Registro de trabajos realizados, Materiales usados, Horas
- **Cierre:** Validación por solicitante, Actualización de hoja de vida del equipo
### 7 Control de Elementos de Seguridad
- **Elementos:** Extintores: Carga, vencimiento, ubicación, señalética., Red húmeda y seca: Pruebas periódicas., Iluminación de emergencia., Señalética de evacuación., Detectores de humo y alarmas.
## Seccion III Gestion de Flota Vehicular
- **Titulo:** Sección III: Gestión de Flota Vehicular
### Restricciones Legales Adquisicion
- **Requisitos:** Autorización Previa de DIPRES (Art. 12 Ley Presupuestos)
La adquisición de vehículos motorizados, a cualquier título, requiere autorización previa de la Dirección de Presupuestos (DIPRES) cuando su precio supere el monto fijado por dicha dirección. Esta restricción aplica también a vehículos adquiridos vía proyectos de inversión.

### 8 Registro de Vehiculos
- **Requisitos:** Cada vehículo institucional debe tener ficha completa:
- **Datos de Identificacion:** Patente., Marca, modelo, año., Número de chasis y motor., Color., Tipo (sedan, camioneta, minibús, etc.).
- **Datos Administrativos:** Código de activo fijo (vinculación con Manual 2.3)., Fecha de adquisición y valor., Responsable asignado., Centro de costo.
- **Documentacion Vigente:** Permiso de circulación., Revisión técnica., Seguro obligatorio (SOAP)., Seguro automotriz voluntario.
- **Equipamiento:** Accesorios instalados (GPS, radio, botiquín, extintor)., Kit de emergencia.
### 9 Registro de Conductores
- **Requisitos:** Nómina de funcionarios autorizados para conducir vehículos institucionales.
- **Requisitos:** Licencia de conducir vigente (clase apropiada)., Hoja de vida sin infracciones graves., Autorización formal (resolución o memorando).
### Actualizacion
- **Definicion:** Control de vencimiento de licencias con alertas.
### 10 Solicitud y Asignacion de Vehiculos
- **Criterios de Prioridad:** Comisiones de servicio oficiales., Actividades del Gobernador y autoridades., Emergencias institucionales., Traslados programados.
- **Advertencias:** Restricción de Uso (D.L. 799)
Los vehículos estatales no pueden circular en días sábados, domingos ni festivos, salvo autorización expresa y fundada por razones de servicio impostergables.

### Proceso
| Paso | Def |
| --- | --- |
| 1. Solicitud | Funcionario requiere vehículo indicando fecha, hora, destino, propósito. |
| 2. Aprobación | Jefatura del solicitante autoriza. |
| 3. Asignación | Encargado de Flota verifica disponibilidad y asigna vehículo + conductor. |
| 4. Confirmación | Notificación al solicitante y conductor. |
### 11 Bitacora de Uso
- **Requisitos:** Registro obligatorio de cada salida:
- **Campos:** Fecha y hora de salida/retorno., Conductor., Destino y propósito., Kilometraje inicial y final., Observaciones (estado del vehículo, incidentes).
- **Modalidad:** Digital: Registro en sistema o aplicación móvil., Física: Cuaderno en el vehículo (respaldo).
### 12 Control de Combustible
- **Registro de Cargas:** Fecha y estación de servicio., Litros cargados., Monto., Kilometraje al momento de carga.
- **Analisis de Rendimiento:** Km/litro por vehículo., Comparación con estándar del fabricante., Alertas por consumos anómalos.
### Tarjeta de Combustible
- **Definicion:** Asignada a cada vehículo (ej. ServiEstado, Copec).
### 13 Control de Kilometraje
- **Requisitos:** Registro mensual del odómetro de cada vehículo., Proyección de mantenciones según kilometraje., Detección de usos no autorizados.
## Seccion IV Mantencion de Vehiculos
- **Titulo:** Sección IV: Mantención de Vehículos
### 14 Plan de Mantencion Vehicular
- **Mantencion Preventiva:** Según manual del fabricante y kilometraje., Típico: Cada 5.000, 10.000, 20.000 km., Incluye: Cambio de aceite, filtros, revisión de frenos, neumáticos.
- **Mantencion Correctiva:** Reparación de fallas detectadas., Prioridad según criticidad.
- **Mantencion Mayor:** Overhaul de motor, transmisión., Evaluación costo/beneficio vs. reemplazo del vehículo.
### 15 Ordenes de Trabajo Vehicular
- **Definicion:** Similar a mantención de infraestructura:
- **Proceso:** Generación por plan o por reporte de falla., Asignación a taller interno o externo (contratista autorizado)., Registro de trabajos, repuestos, costos., Actualización de hoja de vida del vehículo.
### 16 Control de Documentacion
- **Definicion:** Alertas automáticas para vencimientos:
### Table
| Documento | Frecuencia | Responsable |
| --- | --- | --- |
### 17 Siniestros y Accidentes
- **Titulo:** Procedimiento ante accidente:
- **Proceso:** 1. Asegurar integridad de personas., 2. Notificar a Carabineros y compañía de seguros., 3. Documentar con fotografías y croquis., 4. Reportar a Encargado de Flota y jefatura., 5. Gestionar denuncia y reclamo al seguro., 6. Evaluar responsabilidad del conductor (posible sumario)., 7. Reparación o baja del vehículo según daño.
## Seccion V Control y Reporteria
- **Titulo:** Sección V: Control y Reportería
### 18 Indicadores de Gestion de Flota
- **Indicadores:** Disponibilidad: % de tiempo operativo vs. mantenimiento., Utilización: % de uso efectivo vs. capacidad disponible., Costo por Kilómetro: (Combustible + Mantención + Seguros) / Km recorridos., Costo por Vehículo: Gastos totales mensuales/anuales., Incidentes: Número de accidentes, multas de tránsito.
### 19 Reportes Periodicos
### Reportes
| Reporte | Def |
| --- | --- |
| Informe Mensual de Flota | |
| Informe de Vencimientos | Documentos próximos a vencer. |
| Ranking de Conductores | Por consumo, incidentes, multas. |
### 20 Auditoria de Uso
- **Acciones:** Verificación de coherencia entre bitácora, combustible y kilometraje., Detección de usos no autorizados o fuera de horario., Cruce con comisiones de servicio autorizadas.
## Seccion VI Disposiciones Especiales
- **Titulo:** Sección VI: Disposiciones Especiales
### 21 Vehiculos en Comodato o Arriendo
### Tipos
| Tipo | Def |
| --- | --- |
| Comodato Recibido | Vehículos de otras instituciones en uso temporal. |
| Arriendo Operativo | Contratos de leasing o arriendo sin transferencia de propiedad. |
### Control
- **Definicion:** Mismo régimen de bitácora, combustible y mantención.
### Contabilidad
- **Definicion:** Registro como gasto de arriendo, no como activo fijo.
### 22 Baja de Vehiculos
- **Contexto:** Procedimiento según Manual 2.3 (Activo Fijo):
- **Proceso:** Informe técnico de obsolescencia o siniestro., Resolución de baja., Destino: Remate, donación o destrucción., Trámites legales: Transferencia de dominio o baja registral.
### 23 Responsabilidades
### Roles
| Rol | Resp |
| --- | --- |
| Conductor | Uso correcto, Registro de bitácora, Reporte de fallas |
| Encargado de Flota | Planificación, asignación, control documental. |
| Jefe de Servicios Generales | Supervisión integral del área. |
| DAF | Control presupuestario y de contratos. |
## Nota de Cierre
- **Definicion:** Este manual establece los procedimientos para mantener la operatividad de los servicios de soporte institucional y la flota vehicular del GORE.

## Referencias Cruzadas
- **Contexto opcional:** knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_3_activo_fijo.yml, knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_1_compras_koda.yml, knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_2_contabilidad.yml
