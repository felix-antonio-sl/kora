---
_manifest:
  urn: urn:salud:kb:procedimiento-control-cambios-medios-procesamiento
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-04'
    source: MINSAL Chile, SGSI Nivel Central. PROS-NC-002 v3
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- procedimiento
- control-cambios
- change-management
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:procedimiento-control-cambios-medios-procesamiento
  salud:
    minsal_id: PROS-NC-002
    minsal_version: '3'
relations:
  cites:
  - urn:salud:kb:instructivo-seguridad-informacion-ciberseguridad-sector-salud
---

# PROS-NC-002 — Control de Cambios en Medios y Sistemas de Procesamiento de Información

Directrices para regular cambios de infraestructura de comunicaciones, hardware y software en MINSAL. Aplica a todo cambio en hardware, infraestructura de comunicaciones, software, aplicaciones, sitios web y bases de datos de las Subsecretarías de Salud Pública y de Redes Asistenciales. Obligatorio para funcionarios (planta, contrata, reemplazos, suplencia), personal a honorarios y terceros (proveedores, compra de servicios) con derechos de acceso a activos de información del Ministerio.

**Controles NCh-ISO 27001.Of2013 cubiertos**: A.12.05.01 Instalación del software en sistemas operacionales, A.12.06.02 Instalación del software en sistemas operacionales, A.14.02.02 Procedimientos de control de cambios del sistema.

## Definiciones y Documentos de Referencia

- **MINSAL**: Ministerio de Salud.
- **SGSI**: Sistema de Gestión de Seguridad de Información.
- **NCh-ISO27001.Of2013**: Tecnología de la información — Técnicas de seguridad — SGSI — Requisitos.
- **Procedimiento de desarrollo seguro**: complementa las pruebas y criterios de cambios en aplicaciones.

## Roles Operacionales

**Operaciones TIC (Sistemas / Infraestructura) / Equipos de desarrollo TIC**:

- Planificar, coordinar y ejecutar cambios en aplicaciones, infraestructura de comunicaciones, hardware y software básico.
- Instalar nuevos sistemas aplicativos o actualizaciones de los existentes.
- Controlar aprobaciones del usuario antes de ejecutar cambios solicitados.
- Atender solicitudes y requerimientos de usuarios ante incidentes y cambios mayores.
- Controlar a terceros (proveedores) cuando participen en la gestión de un cambio.

## Gestión de Cambios: Requisitos Generales

Todo cambio en infraestructura de comunicaciones, hardware, software básico o aplicaciones debe cumplir tres fases.

### Planificación previa al cambio

Registro obligatorio de planificación detallada:

| Dimensión | Elementos requeridos |
|---|---|
| Objetivo y alcance | Objetivo del cambio; clientes, aplicaciones y hardware/software afectados |
| Operación | Recursos necesarios; cronograma; respaldos previos; pruebas pre/post instalación; capacitación de usuarios; plan de vuelta atrás; riesgos |
| Aceptación | Criterios de éxito o aceptación; registro de rechazo |
| Plazos | Fechas de entrega; previsión de incidencias futuras |

Requisitos adicionales:

- Coordinar el cambio con áreas involucradas o propietarios de sistemas afectados, ejecutándolo en períodos de baja carga de trabajo.
- Solicitar autorización previa.

### Durante el cambio

- Mantener contacto directo con fabricantes o empresas de soporte del software y equipamiento.
- Generar y conservar registros de auditoría del cambio.

### Posterior al cambio

Actualizar inventarios según corresponda:

- Inventario de Infraestructura de Comunicaciones.
- Inventario de Hardware.
- Inventario de Aplicaciones.

## Cambios en Infraestructura de Comunicaciones, Hardware y Software Básico

**Infraestructura de comunicaciones y hardware**: Operaciones TIC planifica internamente o con terceros los cambios por mejoras o reparaciones ante fallas. Terceros deben ser controlados por Operaciones TIC.

**Software básico**:

- Programar cambios preferentemente en fines de semana, días no hábiles o fuera del horario de oficina.
- Verificar autenticidad, integridad y posible impacto en aplicaciones antes de instalar actualizaciones.
- Instalar la actualización en ambiente separado de prueba para verificar funcionamiento.

## Cambios en Aplicaciones

### Cambios generales

- Control de versiones obligatorio.
- El Jefe de Proyecto define y solicita con el equipo de desarrollo los criterios de cambio de versión o releases.
- Análisis y prueba en ambiente de Testing.
- Para sistemas nuevos y de función crítica: pruebas de volumen, estrés, rendimiento, almacenamiento, integración, seguridad y recuperación ante errores (según procedimiento de desarrollo seguro).
- Aprobación del dueño de la aplicación.
- Documentación necesaria para entrega del cambio a producción.
- Documentación detallada de cambios para facilitar capacitación a usuarios.
- Capacitación tan cercana a la salida a producción como sea posible.
- En desarrollos externos: apoyo del personal de la empresa desarrolladora cuando sea posible.

### Cambios mayores

Cambios transversales que afectan a la institución requieren:

- Equipo dedicado para registrar y documentar diferencias a nivel de perfiles, datos, programas e interfaces usuarias entre sistema antiguo y nuevo.
- Capacitación planificada y ejecutada al personal impactado.
- Apoyo a la salida a producción mediante mesa de ayuda (incorporación o constitución de mesa especial).

### Cambios de emergencia

Proceso definido y controlado, con registro post-modificación de la información asociada y aprobación correspondiente.

## Registros Obligatorios

- Registros de planificación de cambios.
- Registros de auditoría de cambios.
- Actualización de inventarios cuando corresponda: Infraestructura de Comunicaciones, Hardware, Aplicaciones.

## Difusión y Revisión

**Difusión**: publicación en la intranet de MINSAL (http://isalud.minsal.cl/) y correo informativo. El contenido debe ser accesible y comprensible para todos los usuarios.

**Revisión**: cada dos años o ante cambios significativos, para asegurar idoneidad, eficiencia y efectividad continuas.

**Control de versiones**:

| Versión | Fecha de Aprobación | Motivo |
|---|---|---|
| 02 | Agosto 2014 | Actualización del documento |
| 03 | Octubre 2019 | Actualización de referencias normativas, responsabilidades y registros de operación |
