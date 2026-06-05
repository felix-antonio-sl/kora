---
_manifest:
  urn: urn:salud:kb:resolucion-aprueba-politicas-seguridad-264
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-05'
    source: MINSAL Chile. Resolución Exenta N°264 (MAR-2022). Aprueba Procedimiento
      para Gestión de Cambios en Ambiente Productivo.
  extensions:
    kora:
      family: note
    salud:
      minsal_id: RES_264
      fecha: 2022-03
      signatario: Ministro de Salud
      documento_aprobado: PROT-NC-003
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- resolucion
- acto-administrativo
lang: es
relations:
  cites:
  - urn:salud:kb:politica-general-seguridad-informacion-ciberseguridad
extensions:
  kora:
    shard_index: 1
    shard_count: 2
    shard_root_urn: urn:salud:kb:resolucion-aprueba-politicas-seguridad-264
---

# Resolución Exenta N°264 — Aprueba Procedimiento para Gestión de Cambios en Ambiente Productivo


**Santiago, MAR 2022. Aprueba PROT-NC-003, Versión Oficial Actual v02, Marzo 2021.**

## Vistos

| Norma | Detalle |
| --- | --- |
| Ley N°21.289 | Presupuestos del Sector Público año 2021 |
| DFL N°1/2005, MINSAL | Texto refundido DL N°2.763/1979 y Leyes N°18.933 y N°18.469 |
| DFL N°1/19653/2000, SEGPRES | Texto refundido Ley N°18.575, Orgánica Constitucional de Bases Generales de la Administración del Estado |
| Resolución Exenta N°889/2019, MINSAL | Aprueba Política General de Seguridad de la Información |
| Memorándum A22 N°110 (12-abr-2021) y N°126 (27-abr-2021) | Jefe Depto. TIC |
| Recado interno (06-may-2021) | Encargado de Seguridad MINSAL |
| Resolución N°07/2019, CGR | Exención del trámite de toma de razón |

## Considerando

1. Las TIC son insumos esenciales en los procesos institucionales del sector salud. La Ley 19.880 prevé procedimientos administrativos en expedientes físicos o electrónicos.
2. Art. 6 de la Ley 19.799: los órganos del Estado podrán ejecutar actos, celebrar contratos y expedir documentos suscribiéndolos con firma electrónica.
3. Decreto N°83/2005, SEGPRES: norma técnica sobre seguridad de documentos electrónicos en la Administración del Estado.
4. Art. 5 letra p) del Decreto N°83: define Política de Seguridad como "conjunto de normas o buenas prácticas para disminuir el nivel de riesgo". Art. 11: debe fijar directrices generales de seguridad institucional.
5. El MINSAL aprobó la "Política General de Seguridad de la Información" por Resolución Exenta N°889/2019. Se requiere aprobar instrumentos complementarios.
6. Al MINSAL compete ejercer la rectoría del sector salud.

## Resuelvo

### 1. Apruébase

El **Procedimiento para Gestión de Cambios en Ambiente Productivo** para el Ministerio de Salud, PROT-NC-003, cuyo texto íntegro se transcribe a continuación.

---

## Procedimiento para Gestión de Cambios en Ambiente Productivo — PROT-NC-003

**Versión 1.3, Agosto 2021. Depto. TIC — Nivel Central. Versión Oficial Actual v02 — Marzo 2021.**

| Rol | Persona | Fecha |
| --- | --- | --- |
| Elaborado | José Villa, Encargado Ciberseguridad (Representante Comité de Seguridad) | Marzo 2021 |
| Revisado | Andrés Muñoz, Infraestructura Tecnológica y Continuidad Operativa | Marzo 2021 |
| Aprobado | Gino Peirano, Jefe Depto. TIC | Marzo 2021 |

## 1. Propósito

Preservar la disponibilidad de los servicios soportados por la infraestructura tecnológica del MINSAL, evaluando y planificando anticipadamente las actividades de puesta en producción y pre-producción de cambios, asegurando eficiencia, calidad, continuidad operacional y éxito de la implementación.

Define la planificación, coordinación, monitoreo y comunicación de cambios que afectan a recursos tecnológicos y sistemas de información para minimizar el impacto sobre los niveles de servicio en ambiente de producción.

## 2. Alcance

Aplicable a todos los cambios en hardware, infraestructura de comunicaciones, software, aplicaciones, sitios web y bases de datos (CDP) de las Subsecretarías de Salud Pública y de Redes Asistenciales.

Describe el flujo de actividades del proceso de Gestión de Cambios: roles, herramientas, métricas e indicadores.

**Controles NCh-ISO 27001:2013:**

| ID Control | Nombre |
| --- | --- |
| A.14.02.02 | Procedimientos de control de cambios del sistema |

## 3. Terminología

- **Cambio** - cualquier acción deliberada que altera o impacta la infraestructura TI: adición, eliminación, modificación o movimiento de uno o más Elementos de Configuración.
- **Gestión de Cambios** - proceso dentro de la Gestión de Servicios TI, responsable del control y tratamiento de cambios en la Infraestructura TI para promover beneficio al negocio minimizando el riesgo de interrupción de servicios.
- **Solicitud de Cambio (RFC)** - requerimiento formal de cambio en espera de ser implementado; incluye detalles del cambio propuesto, en formato electrónico o papel.
- **Impacto del cambio** - medida del efecto sobre el negocio que el cambio tiene o podría tener; se relaciona con el grado de posible violación de acuerdos de niveles de servicio.
- **Urgencia del cambio** - medida de criticidad para la atención de un cambio, en función de tiempos límite pactados con el negocio. Relacionada con el tiempo disponible para ejecución antes de violar acuerdos de niveles de servicio.
- **Buenas prácticas para la gestión del cambio** - mínimo estándar basado en experiencia y conocimientos previos, usado en diseño, ejecución y documentación de un cambio.

## 4. Documentos Aplicables

- NCh-ISO 27001:2013: Tecnología de la información — Técnicas de seguridad — SGSI — Requisitos
- Políticas y procedimientos de Seguridad de la Información del Minsal: disponibles en `isalud.minsal.cl`
- Procedimiento Control de Cambios en los Medios y Sistemas de Procesamiento de Información (PROS-NC-002)
- Política Desarrollo de Sistemas (PS-NC-002)
- Políticas y procedimientos del Depto. TIC: disponibles en `isalud.minsal.cl`

## 5. Roles y Responsabilidades

**a) Solicitante o peticionario:**

- Inicia el proceso de cambio a partir de una necesidad detectada en su ámbito de responsabilidad; remite RFC al procedimiento de Gestión de Cambios.
- Describe y define el cambio, lista de componentes, secuencia y horario de implementación.
- Define la estrategia de Rollback.
- Coordina con el usuario final la aceptación del horario y ejecución de la prueba.
- Certifica el resultado de la implementación en conjunto con el usuario (certificación técnica y funcional).
- Asegura coherencia y completitud de actividades registradas en la RFC.
- Informa el resultado del cambio (tiempo, recursos, objetivo).
- Coordina con el área de operaciones la Estrategia de Paso a Producción.
- Entrega manuales de despliegue e instalación en español.
- Gestiona y asegura que toda versión de software sea controlada mediante GitLab (herramienta oficial Minsal).
- Informa todos los cambios en ambientes de testing o QA a la mesa de CAB en detalle.
- Genera los tickets necesarios para ejecución de actividades descritas en la RFC.
- Asegura que solo el área de producción Operaciones tenga acceso a ambientes de QA (testing) y Producción.

**b) Gestor del Cambio:**

- Responsable de la operación del proceso de Gestión de Cambios.
- Recibe y procesa las Peticiones de Cambio; aprueba dentro de su nivel de autorización.
- Asigna prioridad y categoría a las peticiones, consultando al responsable del proceso si es necesario.
- Revisa características de riesgo/impacto de las peticiones.
- Revisa el plan de trabajo y planifica los cambios menores.
- Coordina la asignación de miembros con el perfil del proceso.
- Notifica el cambio a las partes implicadas.
- Supervisa y coordina la operativa de tratamiento de los cambios.

**c) Comité de Cambios (CAB):**

Presidido por el Gestor del Cambio. Integrantes según naturaleza de los cambios:

- **Jefe de Arquitectura, Desarrollo y Procesos** - aprueba diseño de cambios según definiciones existentes.
- **Encargado de Ciberseguridad y Seguridad de la Información** - verifica cumplimiento de estándares de seguridad.
- **Jefe Infraestructura Tecnológica y Continuidad Operativa** - gestiona documentación y requerimientos, acompaña instalación, cierra actividad en ambiente productivo.
- **Jefe Calidad de SW** - revisa, autoriza y asegura calidad del cambio en producción.
- **Jefe de Oficina de Proyectos** - coordina instancias de análisis del proyecto, gestiona documentación, acompaña instalación y aprueba paso a producción.
- **Gestor del Cambio** - operación del proceso.
- **Responsable del Cambio** (ocasional) - titular del proceso de Negocio.
- **Clientes afectados o sus representantes** (ocasional).

**Responsabilidades del CAB:**

- Evaluar y asesorar aprobación de cambios (complejos, alto impacto).
- Asistir en asignación de prioridad de cambios.
- Proponer calendario de implantación.
- Proponer modificaciones de procedimientos de cambio.
- Verificar cumplimiento de planificación y planes de calidad.
- Evaluar el proceso de Gestión de Cambios para corregir desviaciones y proponer mejoras.

**d) Implementador del cambio:**

- Asignado por el dueño del cambio o solicitante responsable.
- Implementa/ejecuta cambio según instrucciones del solicitante.
- Obtiene información adicional para la implementación.
- Adjunta evidencia de realización de la actividad.

## 6. Procedimiento

#### 6.1 Condiciones Generales

- Solo el área de producción Operaciones TIC accede a ambientes de QA (testing) y Producción.
- Utilizar métodos y procedimientos estándares para manejar eficiente y rápidamente todos los cambios.
- Minimizar el impacto de incidencias relacionadas con cambios sobre la calidad del servicio.
- Priorizar implantación de cambios según compromisos de servicio.
- Colaborar en identificación proactiva de mejoras y modificaciones beneficiosas.
- Mejorar utilización de recursos, incrementando eficiencia.

**Tratamiento estructurado:**

- Registrar de forma centralizada todas las RFC.
- Analizar impacto en el entorno de producción.
- Evaluar, aprobar, planificar y coordinar implantación.
- Verificar resultado efectivo del cambio realizado.

Salvo circunstancias excepcionales, no realizar cambios o pruebas directamente en sistemas productivos. Excepciones requieren aprobación del Encargado de Seguridad/Ciberseguridad y el Jefe del Depto. TIC, previa justificación y análisis de riesgo (ver Política Desarrollo de Sistemas PC-NC-002).

#### 6.2 Proceso

**6.2.1 Descripción del proceso:**

El proceso de Gestión de Cambios gestiona simultáneamente el ciclo de vida y el estado de los distintos cambios de sistemas. Las actividades de Gestión de Cambios se diferencian de las actividades de Gestión de Programas/Proyectos.

Distinción clave: Gestión de Cambios = proceso global; Control de Cambios = procedimiento concreto sobre un cambio específico.

**6.2.2 Priorización:**

La prioridad (RFC) indica importancia relativa para asignación de recursos y determina el intervalo de tiempo requerido para la acción. Depende de impacto y urgencia.

- **Impacto**: valorado según criticidad del servicio afectado, número de usuarios afectados e importancia relativa en la entidad.
- **Urgencia**: estimada por tiempo necesario para resolución, según tiempos de respuesta del acuerdo de niveles de servicio.

Criterios de impacto y urgencia se establecen en coordinación con responsables del negocio y se formalizan en acuerdos de niveles de servicio.

**6.2.3 Tipos de Cambios:**

| Tipo | Descripción |
| --- | --- |
| Estándar | Procedimientos establecidos y conocidos; presentado una única vez al CAB |
| Menor | Impactos y riesgos bajos y controlados; no hay indisponibilidad de servicios; grupo de trabajo con experiencia; SLA no está en riesgo |
| Mayor | Riesgos e impactos altos; indisponibilidad de servicio durante actividades; uno o varios grupos de trabajo; riesgo de comprometer SLA |
| Excepcionado | No entró al flujo normal del CAB; requiere aprobación del Jefe de TIC o Jefe de Operaciones responsable de continuidad operacional |
| Emergencia | Implementación inmediata fuera de procedimientos usuales (CAB), por pérdida súbita de servicios o falla imprevista. Requiere aprobación de jefatura del Depto. TIC y, si es urgencia del negocio, del responsable del área respectiva |

Para incidentes cuya solución requiera cambio urgente: no se exige aprobación del CAB, pero en un plazo menor a `8` horas hábiles debe documentarse el cambio según formato RFC y enviarse formulario PIR evaluando el cambio. Debe informarse al CAB previo a la ejecución y contar con aprobación según punto 6.2.7.

**6.2.4 Convocatoria del Comité de Cambios:**

- Realizada por el Gestor del Cambio, previa validación de las RFCs.
- No requiere reuniones cara a cara; los flujos de notificación pueden ser por medios electrónicos, herramientas web o e-mail.
- Solo en casos muy complejos, de alto riesgo o impacto se requiere reunión formal.
- Reuniones periódicas definidas por el CAB, con agenda previa.

**Agenda estándar del CAB:**

- Revisión de Peticiones de Cambio pendientes.
- Revisión de cambios realizados desde la última reunión.
- Evaluación de eficacia y eficiencia del proceso.
- Priorización y calendarización de cambios pendientes.

En el CAB no se coordinan actividades de paso a producción; estas deben ser coordinadas previamente por el líder técnico o Jefe de Proyecto con las áreas respectivas.

**6.2.5 Requisitos para convocar al CAB:**

a) **Solicitud de Cambio (RFC)** - requisición formal con detalles del cambio propuesto.
b) **Presentación con detalles del cambio** - contiene: descripción del proyecto o servicio, detalle de requerimientos y aprobaciones previas al CAB, plan de actividades con tickets asociados, diagrama de arquitectura tecnológica y comunicaciones, diagrama de flujo del proceso, y toda información para contextualizar el cambio.

**6.2.6 Recepción de RFC:**

- El Gestor de Cambios recibe las RFC, comprueba completitud y corrección, y filtra las totalmente impracticables.
- Las RFC deben enviarse al CAB hasta las `15:00` horas del día anterior a la realización del CAB.
- Si una RFC es rechazada, se presenta en la próxima sesión y se reprograma la actividad.
- La convocatoria a CAB puede ser de martes y jueves, previa validación del RFC y envío oportuno al Gestor del Cambio.

**6.2.7 Aprobación del cambio:**

| Tipo de Cambio | Aprobación requerida |
| --- | --- |
| Cambios normales (Estándar, Menor, Mayor) | Comité de Cambios (CAB) |
| Cambios Excepcionados | VB del Jefe Depto. TIC |

**6.2.8 Autorizar Implementación del Cambio:**

El Gestor de Cambios comprueba la correcta implantación consultando al personal involucrado (Administradores, Especialistas Técnicos, equipo de desarrollo).

**6.2.9 Revisión de la Implementación y Cierre del Cambio (RFC):**

Después de un período preestablecido tras la implementación (o marcha atrás), se realiza una revisión técnica post-implementación.

**6.2.10 Gestión y Mejora del Proceso:**

Actividades de mejora continua:

- Registro detallado de cambios presentados.
- Seguimiento de cada cambio y su efectividad.
- Informe del estado de cambios: cerrados, en desarrollo y pendientes.
- Retroalimentación de actividades como parte de la agenda del CAB.

**6.2.11 Repositorios del proceso de Cambios:**

Todos los cambios que han pasado por Control de Cambios son revisables. En la carpeta Plantilla se encuentran:

- RFC Vigente (sacar copia, no escribir sobre él).
- Solicitud de Cambio RFC (Request for Change).
- Archivos y antecedentes para planificación del cambio.
- Registros Minuta CAB (Aprobación o Rechazo).
- Aprobación del cambio Excepcionado con VB Jefe TIC.

## 7. Matriz de Responsabilidades

| Actividad | Solicitante | Gestor del Cambio | CAB | Especialistas | Responsable del Servicio |
| --- | --- | --- | --- | --- | --- |
| Registrar y filtrar RFC | R | R | | | |
| Evaluar y aprobar cambio | R | R | R | | |
| Planificar (Estrategia de Paso a Producción) | A/R | R | R | A/R | C |
| Coordinar desarrollo y pruebas | A/R | R | | C | |
| Coordinar implementación | A/R | R | R | | |
| Verificar y analizar implantación | A/R | R | | C | |
| Coordinar restauración del estado inicial | A/R | R | | | |
| Revisar cambio (PIR) | R | A | R | | C |
| Cerrar cambio / RFC | | A | R | | |
| Supervisar y comunicar | A | R | | | |
| Informes y métricas | | A/R | | | |
| Evaluación y mejora del proceso | | A/R | | | |

Leyenda: **R** = Responsable directo de realizar/ejecutar. **A** = Responsable último o indirecto (puede delegar, debe supervisar). **C** = Consultar antes de hacer. **I** = Informar después de hacer.

## 8. Métricas e Informes

El Responsable de Gestión de Cambios asegura la recolección de métricas que permitan valorar la calidad del proceso, con seguimiento de KPIs y ejecución de acciones correctivas.

**8.1 Indicadores:**

- Cantidad de cambios solicitados.
- Cantidad de cambios realizados.
- Cantidad de cambios solicitados — rechazados = Cambios normales, emergencia y excepcionados.

## 9. Registros

- Solicitud de Cambio RFC (Request for Change).
- Archivos y antecedentes para planificación del cambio (Estrategia de PAP).
- Registros Minuta CAB (Aprobación o Rechazo).
- Aprobación del cambio Excepcionado con VB Jefe TIC.
- Registros de auditoría de cambios.
- Actualización de inventarios: Infraestructura de Comunicaciones, Hardware, Aplicaciones, Usuarios (cuando aplica).

## 10. Difusión

La comunicación se efectuará de forma accesible y comprensible mediante:

- Publicación en intranet Minsal: `http://isalud.minsal.cl/`
- Correo informativo

## 11. Revisión y Medición

El procedimiento debe revisarse al menos una vez al año o cuando ocurran cambios significativos, para asegurar su continua idoneidad, eficiencia y efectividad.

## 12. Control de Versiones

| Versión | Fecha | Motivo | Secciones Modificadas |
| --- | --- | --- | --- |
| 01 | Marzo 2021 | Creación del documento | Todas |
| 02 | Noviembre 2021 | Ajustes de procedimientos | Se agregan: Estrategias de paso a producción, Acceso a ambientes de Testing y Producción, Entregables para pasos a producción, Fuente oficial de versionamiento de software MINSAL |

## 13. Anexos

N/A

---

### 2. Publíquese

El contenido del archivo computacional correspondiente junto con la presente resolución, por el Depto. TIC, en `https://www.minsal.cl/seguridad_de_la_informacion/` y en el Banner de transparencia del MINSAL.

### 3. Remítase

Un ejemplar del instructivo a los funcionarios que corresponda, vía correo electrónico.

### 4. Anótese y comuníquese
