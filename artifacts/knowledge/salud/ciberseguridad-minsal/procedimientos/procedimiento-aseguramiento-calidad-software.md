---
_manifest:
  urn: urn:salud:kb:procedimiento-aseguramiento-calidad-software
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-04'
    source: MINSAL Chile, SGSI Nivel Central. PROS-NC-011 v1
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- procedimiento
- calidad-software
- qa
- testing
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:procedimiento-aseguramiento-calidad-software
  salud:
    minsal_id: PROS-NC-011
    minsal_version: '1'
    fecha_aprobacion: Julio 2021
    clasificacion: Publica
    elaborador: Encargado Aseguramiento de Calidad TIC MINSAL
    revisor: José Villa Catalán / Encargado de Ciberseguridad
    aprobador: Gino Paolo Peirano Alvarado / Jefe Departamento Tecnologías de la Información
      y Comunicaciones
relations:
  cites:
  - urn:salud:kb:instructivo-seguridad-informacion-ciberseguridad-sector-salud
---

# Procedimiento para el Aseguramiento de Calidad de Software — PROS-NC-011 v1

Sistema de Gestión de Seguridad de la Información — MINSAL Nivel Central. Julio 2021.

## Objetivo del procedimiento

Establecer un marco regulatorio mínimo para el Aseguramiento de Calidad de Software de MINSAL, de modo que los desarrollos y mantenciones estén alineados con los procedimientos de seguridad de la información definidos para el desarrollo de sistemas.

## Cobertura y alcance

| Cobertura | Detalle |
|-----------|---------|
| Áreas | Desarrollo y áreas usuarias de aplicaciones desarrolladas |
| Organismos | Subsecretarías de Salud Pública y Redes Asistenciales |
| Personal | Funcionarios (planta, contrata, reemplazos, suplencia), honorarios, terceros (proveedores, compra de servicios) con acceso a activos de información |
| Controles ISO 27001 | A.14.02.01 Política de desarrollo seguro; A.14.02.02 Procedimientos de control de cambios del sistema; A.14.02.03 Revisión técnica de las aplicaciones después de los cambios en la plataforma de operación; A.14.02.09 Prueba de aprobación del sistema |

## Terminología y documentos aplicables

- **MINSAL** — Ministerio de Salud
- **SGSI** — Sistema de Gestión de Seguridad de Información
- **Documentos aplicables**: NCh-ISO27001.Of2013; Marco Jurídico referido a los SSI (portal CSIRT del Ministerio del Interior); Decretos Supremos y Normas Internacionales de Seguridad de la Información y Ciberseguridad; documentos del SGSI disponibles en http://isalud.minsal.cl

## Roles y responsabilidades

Responsables del cumplimiento: áreas de desarrollo de MINSAL, Usuarios, Custodios Físicos, Custodios de los Datos, contratistas, Administradores de Seguridad, Unidades de Informática, Gestión de Personas y Comité de Seguridad de la Información.

## Solicitud de Aseguramiento de Calidad de Software

Los líderes de proyectos de desarrollo o mantención deben formalizar la necesidad de QA mediante el formulario **Solicitud de Aseguramiento de Calidad de Software**, como parte de la planificación del proyecto, entregándolo al encargado del servicio en TIC MINSAL.

Debe adjuntarse: metodología de desarrollo/mantención, documentación de requerimientos de negocio, manuales de usuario y toda documentación relevante para el proceso de QA.

El encargado del servicio de QA registra la solicitud en el **Catastro de Solicitudes de Aseguramiento de Calidad de Software**, asignando un código de identificación que se entrega al requirente.

## Alcances del proceso de QA

El encargado de QA en TIC MINSAL analiza y evalúa el alcance y estrategia propuestos para el proceso y los formaliza al requirente.

## Planificación del proceso de QA

El encargado de QA estima los recursos y plazos asociados y los comunica al requirente, quien incorpora dichas actividades y plazos en el plan principal del proyecto. El plan ajustado se comparte con el encargado de QA para coordinación y seguimiento de hitos.

## Ambiente para el proceso de QA

El requirente coordina la preparación y habilitación de todos los ambientes o requisitos tecnológicos e informa al encargado de QA cuando estén disponibles. Debe entregar las credenciales necesarias según los roles definidos.

**Inmutabilidad del ambiente**: El requirente debe garantizar que el ambiente no sufrirá cambios durante cada ciclo de QA. Cualquier intervención requerida debe coordinarse con el encargado de QA. El incumplimiento puede invalidar el proceso de QA en curso, requiriendo uno nuevo cuando las condiciones sean adecuadas.

## Data para el proceso de QA

La data de prueba es provista por el requirente, salvo que el equipo de QA esté en condiciones de prepararla por sí mismo.

## Versionamiento del software a certificar

El requirente debe garantizar que las fuentes y/o binarios estén versionados en la plataforma de versionamiento de MINSAL. El sistema debe contar con un número de versión que permita identificación y trazabilidad respecto a versiones anteriores. El proceso de QA es válido solo para la versión especificada.

## Seguimiento al proceso de QA

El encargado de QA entrega periódicamente un avance que incluye: estadísticas, hallazgos detectados y evidencias de los hallazgos.

## Aseguramiento de Calidad de Software Funcional

### Criterios de aceptación

El servicio de QA funcional define los siguientes criterios de aceptación, informados al requirente al inicio del proceso:

| Condición de Aceptación | Umbral |
|-------------------------|--------|
| Casos de prueba ejecutados | 100% de los definidos |
| Hallazgos Invalidantes pendientes | 0 |
| Hallazgos Graves pendientes | 0 |
| Hallazgos Medios pendientes | Impacta hasta 1% de los casos de prueba |
| Hallazgos Leves pendientes | Impacta hasta 5% de los casos de prueba |

### Análisis y diseño de casos de prueba

El equipo de QA analiza la documentación de requerimientos funcionales y diseña los casos de prueba. El encargado de QA los envía al requirente para revisión, confirmación o ajuste por el negocio. La versión validada por el negocio es devuelta al encargado de QA, quien deja registro de los casos de prueba a utilizar.

### Ciclo de ejecución de casos de prueba

El proceso contempla hasta **3 ciclos de QA**. Después de cada ciclo, el encargado informa el resultado al requirente y se evalúa contra los criterios de aceptación. Si al término del tercer ciclo los criterios no se cumplen, el proceso de QA es **rechazado**. Se deja registro del resultado de cada ciclo.

### Hallazgos detectados

Al término de cada ciclo se entregan al requirente: hallazgos detectados, evidencias asociadas y estadísticas del proceso. El requirente coordina la revisión de hallazgos con el negocio para definir el curso a seguir con cada uno, y comparte la decisión con el equipo de QA. Se deja registro de los hallazgos, evidencias y decisión del negocio.

### Término del proceso de QA funcional

Cuando los criterios de aceptación determinan el resultado, el encargado confirma el resultado al requirente y prepara el **Informe de Término del Proceso de Aseguramiento de Calidad**. El proceso puede ser **cancelado** por mutuo acuerdo entre requirente y encargado. Se deja registro del resultado final en el Catastro de Solicitudes y del Informe Final.

## Pruebas de Carga y Estrés

### Equipo, roles y responsabilidades

Se conforma un equipo multidisciplinario con representantes de: Negocio, Proveedores, Proyectos TIC MINSAL, Arquitectura TIC MINSAL, PMO TIC MINSAL, Operaciones TIC MINSAL, Seguridad de la Información TIC MINSAL y Aseguramiento de Calidad de Software TIC MINSAL. Se definen roles y responsabilidades para cada integrante.

### Estadísticas y métricas actuales y futuras

El negocio informa las estadísticas y métricas actuales del sistema y las proyecciones esperadas para un período futuro.

### Flujos de negocio a considerar

El negocio define los flujos más representativos de su servicio para ser utilizados en las pruebas.

### Niveles de servicio esperados

El negocio define los niveles de servicio actuales y esperados, que sirven como referencia para las pruebas de carga y estrés.

### Modelo a utilizar

El encargado de QA coordina con el equipo la definición del modelo de pruebas de carga y estrés.

### Monitoreo, métricas y evidencias

El encargado de QA coordina la definición del monitoreo de infraestructura, comunicaciones y aplicaciones, y las métricas y evidencias a obtener durante la ejecución. Se definen responsables de preparación y ejecución del monitoreo y de la entrega de métricas y evidencias.

### Automatización

El encargado de QA coordina la definición de herramientas y equipamiento de automatización para simular los flujos de negocio representativos. El encargado de negocio coordina el desarrollo de las automatizaciones y la preparación para la ejecución.

### Estrategia de pruebas de carga y estrés

El encargado de QA coordina la elaboración de la estrategia mediante el documento **Estrategia de Pruebas de Carga y Stress**, del cual se deja registro.

### Ciclo de ejecución

Las pruebas se realizan en base a ciclos de ejecución, hasta que los resultados sean aceptados por el equipo asignado.

### Recopilación de métricas y evidencias

El encargado de QA coordina la recopilación, documenta y comparte métricas y evidencias con el equipo para el análisis del ciclo. Se deja registro.

### Análisis de resultados de cada ciclo

El encargado de QA coordina el análisis de resultados. El equipo define las actividades siguientes: cambios en infraestructura, cambios en comunicaciones, cambios a configuraciones de software básico, ajustes a aplicativos o componentes, o cierre del proceso.

### Aplicación de mejoras, ajustes o modificaciones

Cada responsable aplica las acciones acordadas e informa al equipo del resultado. Finalizadas las actividades, el encargado de QA coordina un nuevo ciclo de pruebas.

### Término del proceso de pruebas de carga y estrés

Al finalizar, el encargado de QA prepara y comparte el **Informe de Término del Proceso de Pruebas de Carga y Stress** con todos los antecedentes. Se deja registro del resultado final y del Informe Final.

## Análisis de código fuente

El software desarrollado o modificado es analizado en su código fuente para detectar vulnerabilidades de seguridad o de calidad. El encargado coordina este análisis y entrega el informe con resultados al solicitante para que coordine la resolución de vulnerabilidades. Se deja registro del proceso y sus resultados.

## Registros

| Proceso | Registro |
|---------|----------|
| QA Funcional | Solicitud de Aseguramiento de Calidad de Software |
| QA Funcional | Catastro de Solicitudes de Aseguramiento de Calidad de Software |
| QA Funcional | Casos de prueba diseñados |
| QA Funcional | Casos de prueba ejecutados por ciclo |
| QA Funcional | Hallazgos detectados en el proceso |
| QA Funcional | Evidencias generadas en el proceso |
| QA Funcional | Métricas del proceso |
| QA Funcional | Informe de Término del Proceso de Aseguramiento de Calidad |
| Pruebas de Carga y Estrés | Estrategia de Pruebas de Carga y Stress |
| Pruebas de Carga y Estrés | Métricas y Evidencias generadas durante el proceso |
| Pruebas de Carga y Estrés | Informe de Término del proceso de Pruebas de Carga y Stress |

## Difusión

La comunicación del procedimiento se efectúa mediante: publicación en la intranet http://isalud.minsal.cl y correo informativo, de modo que el contenido sea accesible y comprensible para todos los usuarios.

## Revisión y medición

El procedimiento se revisa al menos cada **dos años** o cuando ocurran cambios significativos, para asegurar su continua idoneidad, eficiencia y efectividad.

## Control de versiones

| Versión | Fecha | Motivo | Secciones |
|---------|-------|--------|-----------|
| v1 | Julio 2021 | Creación del documento | Todas |
