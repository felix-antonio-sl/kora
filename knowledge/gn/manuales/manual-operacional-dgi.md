---
_manifest:
  urn: "urn:gn:kb:manual-operacional-dgi"
  provenance:
    created_by: "FS"
    created_at: "2026-01-29"
    source: "GORE Ñuble"
version: "2.0.0"
status: published
tags: [gore-nuble, gobierno-regional, dgi, gestion-institucional]
lang: es
---

# Manual Operacional DGI

## Disposiciones Generales

- **Objeto**: Marco operativo del Departamento de Gestión Institucional (DGI) del GORE Ñuble; define estructura, funciones, procesos y coordinación.
- **Alcance**: Personal DGI e interacciones con divisiones, unidades y actores externos.

### Definiciones Operacionales

| Término | Definición |
| :--- | :--- |
| DGI | Departamento de Gestión Institucional |
| AR | Administración Regional |
| TD | Transformación Digital |
| TDE | Transformación Digital del Estado (Ley 21.180) |
| KB | Knowledge Base / Base de Conocimiento |
| BPMN | Business Process Model and Notation |
| KPI | Key Performance Indicator |
| GORE | Gobierno Regional |
| ERD | Estrategia Regional de Desarrollo |

### Marco Normativo y Principios

- **Normativa**: Ley 19.175 (Gobierno Regional), Ley 21.180 (Transformación Digital), DS 14/2014 (Gestión Procesos), Res. 22/2023 (Interoperabilidad), PMG.
- **Principios**:
  - Orientación al servicio (usuarios internos/finales).
  - Basado en datos (información verificable).
  - Mejora continua (optimización sistemática).
  - Colaboración, Transparencia e Innovación.

## Estructura Organizacional

### Misión y Visión DGI

- **Misión**: Facilitar gestión efectiva vía control, modernización, transformación digital y gestión del conocimiento para toma de decisiones AR.
- **Visión**: Referente de gestión en GOREs Chile por calidad, innovación y tecnología.

### Áreas y Perfiles

- **Dominios Funcionales**:
  - **Control de Gestión**: Monitoreo, dashboards, alertas, informes.
  - **Modernización de Procesos**: Levantamiento BPMN, mejoras, automatización.
  - **Transformación Digital**: Cumplimiento TDE, Comité TD, sistemas.
  - **Gestión del Conocimiento**: Curación KB, agentes IA, capacitación.

- **Cargos y Funciones**:
  - **Jefe DGI**: Depende de AR. Dirige equipo, asesora a AR, reporta estado de iniciativas.
  - **Especialista Procesos**: Levanta/modela BPMN, diseña automatizaciones, documenta procedimientos.
  - **Especialista TD**: Monitorea TDE, secretaría Comité TD, cura base de conocimiento, administra IA.
  - **Especialista Control**: Define/monitorea indicadores, mantiene dashboards, genera informes ejecutivos.

### Matriz RACI Operativa

| Actividad | Jefe | Procesos | TD | Control | División | AR |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Diseñar indicadores | C | I | I | R | C | A |
| Levantar procesos | C | R | I | I | C | I |
| Gestionar KB | C | I | R | I | I | I |
| Administrar dashboards | C | I | I | R | I | I |
| Reportar a AR | R | C | C | C | I | A |

## Control de Gestión

### Proceso de Monitoreo

1. **Definición**: Identificar objetivos (ERD, Ñuble 250), definir indicadores SMART, metas y umbrales.
2. **Recolección**: Fuentes de datos, frecuencia actualización, responsables provisión, validación calidad.
3. **Análisis**: Aplicar fórmulas, comparar metas/periodos, identificar tendencias y hallazgos.
4. **Comunicación**: Actualizar dashboard, generar alertas e informar responsables.

### Instrumentos de Control

- **Tipos de Dashboard**:
  - **Ejecutivo**: Para AR/Gobernador. KPIs agregados y alertas críticas (Diario).
  - **División**: Para Jefe División. Indicadores específicos (Semanal).
  - **Operativo**: Para equipos. Detalle tareas y estados (Diario).
  - **Temático**: Para Comités (IPR, TD). Foco específico (Según comité).

- **Gestión de Alertas**:
  - **Señales**: Indicadores < umbral (>2 períodos), acumulación pendientes, ↑ tiempos ciclo, reclamos recurrentes, desviaciones presupuestarias.
  - **Acción**: Detección → Verificación → Análisis (5 porqués/Ishikawa) → Propuesta → Comunicación → Seguimiento.

### Informe de Estado Situacional

- **Estructura**:
  1. Resumen ejecutivo (semáforo, logros, alertas).
  2. Tabla indicadores clave (tendencia, gráficos).
  3. Detalle alertas y riesgos.
  4. Avance iniciativas DGI.
  5. Recomendaciones y decisiones requeridas.
  6. Prioridades próximo período.
- **Frecuencia**: Semanal (resumen) / Mensual (completo).

## Modernización de Procesos

### Levantamiento y Modelado BPMN

- **Fases**:
  1. **Preparación**: Identificar alcance (inicio/fin), actores y programar sesiones.
  2. **Recolección**: Entrevistas, observación terreno, revisión documentación, variantes/excepciones.
  3. **Modelado**: Diagrama AS-IS, roles/sistemas, reglas de negocio, validación.
  4. **Documentación**: Ficha proceso, métricas (tiempos/volumen), registro en repositorio.
- **Elementos Mínimos**: Eventos inicio/fin, actividades con responsable, flujos, compuertas, pools/lanes, anotaciones.

### Análisis y Mejora

- **Dimensiones de Análisis**: Valor agregado, duplicación, esperas, movimientos, errores/reprocesos, potencial automatización.
- **Priorización**: Primero iniciativas de **Alto Impacto + Bajo Esfuerzo**.
- **Tipos de Automatización**:
  - RPA (tareas repetitivas, carga datos).
  - Flujos (orquestación aprobaciones, visación).
  - Notificaciones (alertas vencimiento).
  - Reportes (generación programada).
  - Integraciones (SIGFE - Dashboards).

### Ciclo de Implementación

- **Preparación**: Recursos, comunicación, capacitación, ambiente.
- **Piloto**: Alcance reducido, monitoreo intensivo, feedback, ajuste.
- **Despliegue**: Alcance completo, capacitación usuarios, documentación nueva.
- **Estabilización**: Monitoreo KPIs, incidentes, refinamiento.
- **Mejora Continua**: Medición vs línea base, lecciones aprendidas.

## Transformación Digital

### Cumplimiento Ley 21.180 (TDE)

- **Responsabilidades DGI**:
  - Inventario procesos y nivel digitalización.
  - Roadmap cumplimiento y priorización.
  - Soporte a divisiones en digitalización.
  - Verificación cumplimiento normas técnicas y evidencia para auditoría.
- **Checklist Cumplimiento**:
  - Procedimiento documentado.
  - Firma electrónica y Notificaciones electrónicas.
  - Expediente electrónico.
  - Interoperabilidad especificada.
  - Autenticación ClaveÚnica.

### Gobernanza y Sistemas

- **Comité TD**: Secretaría técnica, actas, seguimiento acuerdos, análisis factibilidad iniciativas. Frecuencia mensual.
- **Administración Funcional**:
  - **DGI (Responsable)**: Requisitos funcionales, reglas de negocio, perfiles/roles, incidentes de negocio, evolución plataforma.
  - **TI**: Cuentas/accesos, infraestructura, seguridad, incidentes técnicos.

### Gestión de Datos e Interoperabilidad

- **Principios**: Datos como activo estratégico, Fuente única de verdad, Interoperabilidad por diseño.
- **Proceso**:
  - **Inventario**: Conjuntos críticos, ubicación, formato, dueño.
  - **Calidad**: Estándares, monitoreo y correcciones.
  - **Integración**: APIs, archivos, monitoreo intercambio.

## Gestión del Conocimiento

### Curación de KB e IA

- **Proceso Curación (KODA)**: Identificación → Estructuración (URN/Metadatos) → Validación (Expertos) → Publicación (Catálogo) → Mantenimiento (Revisión vigencia).
- **Criterios Priorización**: Frecuencia consulta, criticidad operación, riesgo desactualización, demanda usuarios.
- **Ciclo Vida Agentes IA**: Diseño (propósito/fuentes) → Desarrollo (entrenamiento/pruebas) → Despliegue (capacitación) → Operación (monitoreo/refinamiento) → Evolución.

### Gobernanza IA y Cambio

- **Gobernanza**: Dueño funcional obligatorio, respuestas auditables, conocimiento documentado, transparencia sobre uso de IA.
- **Principios Gestión Cambio**: Foco en personas, comunicación permanente (el "porqué"), participación afectados, gradualidad.
- **Fases Proceso**: Preparación (stakeholders/impacto) → Comunicación (beneficios/dudas) → Capacitación (práctica) → Acompañamiento (soporte transición) → Consolidación (refuerzo/lecciones).

## Funciones Habilitadoras

- **Gestión Arquitectural (Meyer)**:
  - Regla de Oro: Autoridad = Responsabilidad.
  - Dominios Precisos: Sin superposiciones.
  - Sinergias: Agrupación efectiva de especialistas.
- **Dinámica de Producción (Lean/Kanban)**:
  - Visualización flujo (Tableros).
  - Límites de Trabajo en Curso (WIP).
  - Métricas: Throughput (rendimiento), Lead Time (tiempo ciclo).
- **Navegación Social (ADKAR)**:
  - Rol de Lobbista Interno: Facilitar consensos.
  - Modelo ADKAR: Awareness, Desire, Knowledge, Ability, Reinforcement.
  - Influencia Ética: Reciprocidad y prueba social.

## Coordinación Institucional

### Relación AR y Divisiones

- **Administración Regional**: Reunión semanal. Reporte iniciativas, alertas, decisiones y prioridades. Escalamiento mediante Informe Ejecutivo con opciones/recomendación.
- **Matriz de Interacción**:
  - **Gabinete**: Agenda estratégica (Según necesidad).
  - **DAF**: Indicadores presupuestarios y rendiciones (Semanal).
  - **DIPIR**: Cartera IPR y estados avance (Semanal).
  - **Jurídica**: Convenios, resoluciones y cumplimiento (Quincenal).
  - **DIPLADE**: Indicadores ERD y planificación (Mensual).
  - **Operaciones**: Mesa Técnica sistemas/infraestructura (Mensual).
  - **Auditoría**: Cumplimiento y control interno (Trimestral).

### Protocolo de Escalamiento

| Nivel | Situación | Escalar a | Plazo Máximo |
| :--- | :--- | :--- | :--- |
| 1 | Incidente operativo | Jefe DGI | 4 horas |
| 2 | Bloqueo de proyecto | Adm. Regional | 24 horas |
| 3 | Conflicto divisiones | Adm. Regional | 48 horas |
| 4 | Decisión estratégica | Gobernador (vía AR) | Según urgencia |

- **Requisitos**: Descripción problema, impacto, opciones, recomendación, plazo decisión y firma responsable.

### Participación en Comités

- **Comité TD**: Secretaría técnica (Mensual).
- **Comité Coordinación Regional**: Informante (Según convocatoria).
- **Mesas Temáticas**: Facilitador técnico (Según necesidad).
