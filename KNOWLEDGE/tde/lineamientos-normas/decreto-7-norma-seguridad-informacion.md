---
_manifest:
  urn: urn:tde:kb:decreto-7-norma-seguridad-informacion
  provenance: https://wikiguias.digital.gob.cl/Normas/Decreto7
version: 1.0.0
status: published
tags:
- tde
- lineamientos-normas
- decreto
- norma-tecnica
- seguridad-de-la-informacion
- ciberseguridad
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:tde:kb:decreto-7-norma-seguridad-informacion
---

# Decreto 7 — Norma Técnica de Seguridad de la Información y Ciberseguridad

> Promulgación: 19-MAY-2023 | Publicación: 17-AGO-2023 | Versión: Única

> Nota: ver también [Guía Técnica de Ciberseguridad](/guias/GU-CIBER-001)

## Encabezado

**Bases legales:**

| Instrumento | Materia |
|-------------|---------|
| DS Nº 100/2005 SEGPRES (CPR arts. 32 Nº6 y 35) | Constitución Política |
| Ley Nº 19.880 | Bases procedimientos administrativos |
| Ley Nº 18.993 | Crea MINSEGPRES |
| Ley Nº 21.180 | Transformación Digital del Estado |
| DFL Nº 1/2020 MINSEGPRES | Gradualidad implementación ley 21.180 |
| DS Nº 4/2020 MINSEGPRES | Reglamento medios electrónicos (en adelante "el Reglamento") |
| DS Nº 83/2004 MINSEGPRES | Norma técnica seguridad y confidencialidad documentos electrónicos |
| Instructivo Presidencial Nº 8/2018 | Instrucciones ciberseguridad órganos del Estado |
| Resolución Nº 7/2019 CGR | Exención toma de razón |

**Considerando (síntesis):** Ley 21.180 mandató dictar 6 normas técnicas (interoperabilidad, seguridad, documentos, notificaciones, calidad, autenticación) vía DS del MINSEGPRES. Mesa Técnica de Seguridad integrada por CSIRT-Interior, Defensa, SUBTEL, DIPRES, Hacienda, CPLT, CORFO y SII, con base en estándares internacionales. [→ Artículo 12]

---

## Disposiciones generales

### Artículo 1 — Objeto

Definir estándares y directrices técnicas de seguridad de la información y ciberseguridad que deben cumplir los órganos de la Administración del Estado para resguardar la **confidencialidad, integridad y disponibilidad** de la información y la infraestructura informática de las plataformas que sustentan procedimientos administrativos.

### Artículo 2 — Definiciones

| Término | Definición |
|---------|-----------|
| **Activo** | Elemento lógico o físico (hardware, software, sistema) que permite generar, almacenar, enviar o intercambiar información. |
| **Activo de Información** | Datos cuyo tratamiento es esencial para el funcionamiento del órgano; deben protegerse en confidencialidad, integridad y disponibilidad. |
| **Ciberseguridad y Seguridad de la Información** | Conjunto de acciones, políticas y medidas preventivas/reactivas para prevenir, mitigar y responder ante incidentes de seguridad, protegiendo activos y continuidad de servicios. |
| **Confidencialidad** | Acceso exclusivo a quienes están autorizados. |
| **Control de Seguridad** | Estándares, buenas prácticas y normativas para gestión de riesgos TI. |
| **Disponibilidad** | Accesibilidad y utilización del activo a requerimiento autorizado. |
| **Gestión de Riesgo** | Proceso estructurado de identificación, evaluación, control y tratamiento de riesgos. |
| **Incidente de Seguridad** | Evento indeseado que compromete disponibilidad, autenticidad, integridad o confidencialidad de sistemas, activos o servicios. |
| **Integridad** | Exactitud, autenticidad y completitud de los activos de información. |
| **Plataforma Electrónica** | Software, datos e infraestructura tecnológica que sustenta procesos o procedimientos. |
| **Reglamento** | DS Nº 4/2020 MINSEGPRES. |
| **Riesgo** | Efecto de incertidumbre sobre activos, expresado en consecuencias de un incidente y su probabilidad. |
| **Servidor** | Equipo virtual o físico que entrega servicios de red, bases de datos, sistemas informáticos o recursos a usuarios. |
| **Sistema Informático** | Conjunto de componentes lógicos y físicos que realizan la función para la cual fueron diseñados. |
| **Usuarios(as)** | Interesados(as) en un procedimiento administrativo y funcionarios(as) que acceden a plataformas que lo soportan. |

### Artículo 3 — Marco para la seguridad de la información y ciberseguridad

Los órganos estructurarán su trabajo a partir del diagnóstico inicial (→ Artículo 4), definiendo funciones y categorías (→ Título Tercero), junto con la elaboración e implementación de la Política (→ Artículo 5).

### Artículo 4 — Diagnóstico inicial

Cada órgano deberá realizar un **diagnóstico inicial** del estado de ciberseguridad de sus plataformas, conforme a las guías técnicas del Artículo 12. El resultado deberá incluirse en el Catálogo de Plataformas de la Norma Técnica de Calidad y Funcionamiento (art. 57 del Reglamento).

---

## De la Política de Seguridad de la Información y Ciberseguridad

### Artículo 5 — Política de Seguridad de la Información y Ciberseguridad

Cada órgano deberá elaborar una **Política**, aprobada por acto administrativo del Jefe(a) Superior de Servicio. La Política debe:

1. Establecer objetivos generales y específicos.
2. Identificar y delimitar el alcance (activos, roles, plataformas de procedimientos administrativos).
3. Señalar la legislación y normativa vigente aplicable.
4. Especificar roles y designar:
 - Un(a) **responsable institucional de seguridad de la información y ciberseguridad**: vela por la seguridad, desarrollo, cumplimiento y actualización de la Política. **No puede ser externalizado.**
 - Un(a) **responsable de los activos de información**: identifica, clasifica y gestiona los riesgos. **No puede ser externalizado.**
 - Cada órgano determinará si estos roles se unifican o no en una sola persona.
 - Los órganos que ya designaron encargado(a) de ciberseguridad conforme al Instructivo Nº 8/2018 se entienden cumplidos en este requisito, salvo que opten por designar uno nuevo.

La Política también deberá velar por la preservación, confidencialidad, integridad y disponibilidad de la información, incorporando seguridad y privacidad desde el diseño. Las guías técnicas del Artículo 12 complementarán los detalles operativos.

---

## Funciones y categorías

### Artículo 6 — Funciones y categorías

Para implementar la Política, cada órgano deberá atender las funciones y categorías del presente título, que se especificarán en las guías técnicas del Artículo 12.

### Artículo 7 — Función de identificación

Actividades para identificar y administrar los **riesgos de seguridad** asociados a procesos, personas y plataformas. Comprende las categorías de:
- Contexto o entorno del órgano
- Gobernanza
- Gestión de activos de información
- Gestión de riesgos
- Contratación y gestión de proveedores de servicios en la nube

### Artículo 8 — Función de protección

Procesos y actividades para garantizar medidas de seguridad que permitan la entrega de servicios en forma adecuada, oportuna y segura. Comprende las categorías de:
- Gestión de servidores, redes, autenticación y control de acceso
- Concienciación y formación de funcionarios
- Seguridad de los datos
- Procesos de protección de la información
- Registro de eventos

### Artículo 9 — Función de detección

Procesos para la **detección oportuna** de incidentes de seguridad. Comprende:
- Análisis de eventos para identificar anomalías o fallas
- Monitoreo continuo de seguridad (protección contra código malicioso)
- Proceso de detección de eventos

### Artículo 10 — Función de respuesta

Procesos y actividades para **adoptar medidas técnicas y organizativas** ante incidentes detectados. Comprende:
- Planificación de respuesta ante incidentes
- Comunicación de acciones de respuesta
- Análisis de incidentes
- Mitigación de incidentes
- Mejoras a la planificación y procesos de respuesta

### Artículo 11 — Función de recuperación

Procesos para **restablecer capacidades** afectadas por un incidente (plataformas, servidores, redes, servicios). Comprende:
- Planificación de la recuperación
- Mejoras a la planificación y procesos de recuperación
- Comunicación del estado de recuperación

---

## Disposiciones finales

### Artículo 12 — Guía técnica

La División de Gobierno Digital del MINSEGPRES dictará una o más guías técnicas con los aspectos operativos y procesos de implementación de esta norma.

### Artículo 13 — Gradualidad

La aplicación es acorde a la gradualidad del DFL Nº 1/2020 MINSEGPRES. La División de Gobierno Digital definirá los lineamientos y formato de cumplimiento para los órganos obligados.

### Artículo 14 — Revisión y actualización de la norma

Revisión y actualización **al menos cada dos años**, contados desde la entrada en vigencia. Las actualizaciones considerarán aprendizajes y dificultades reportados por los órganos, impulsando buenas prácticas y minimizando efectos de prácticas incorrectas.
