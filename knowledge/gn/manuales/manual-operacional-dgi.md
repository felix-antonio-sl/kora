---
_manifest:
  urn: urn:gn:kb:manual-operacional-dgi
  provenance:
    created_by: FS
    created_at: '2026-01-29'
    source: "GORE Ñuble"
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- dgi
- gestion-institucional
- gn
lang: es
---

# Manual Operacional DGI

Siglas: DGI = Departamento de Gestión Institucional · AR = Administración Regional · TD = Transformación Digital · TDE = Transformación Digital del Estado (Ley 21.180) · KB = Knowledge Base / Base de Conocimiento · BPMN = Business Process Model and Notation · KPI = Key Performance Indicator · GORE = Gobierno Regional · ERD = Estrategia Regional de Desarrollo · DAF = División de Administración y Finanzas · DIPIR = División de Presupuesto e Inversión Regional · DIPLADE = División de Planificación y Desarrollo Regional · RPA = Robotic Process Automation · ADKAR = modelo de gestión del cambio (Awareness, Desire, Knowledge, Ability, Reinforcement).

## Disposiciones Generales

**Objeto:** Marco operativo del DGI del GORE Ñuble; define estructura, funciones, procesos y mecanismos de coordinación institucional.

**Alcance:** Todo el personal del DGI e interacciones con divisiones, unidades y actores externos relacionados con sus funciones.

**Marco normativo:**

| Norma | Contenido |
|-------|-----------|
| Ley 19.175 | Orgánica Constitucional sobre Gobierno y Administración Regional |
| Ley 21.180 | Transformación Digital del Estado |
| DS 14/2014 | Modelo de Gestión de Procesos |
| Resolución 22/2023 | Normas Técnicas de Interoperabilidad |
| PMG | Programa de Mejoramiento de la Gestión |

**Principios rectores:**

| ID | Principio | Descripción |
|----|-----------|-------------|
| PR-01 | Orientación al servicio | Foco en necesidades de usuarios internos y finales |
| PR-02 | Basado en datos | Decisiones sustentadas en información verificable |
| PR-03 | Mejora continua | Optimización sistemática de procesos |
| PR-04 | Colaboración | Trabajo conjunto con todas las divisiones |
| PR-05 | Transparencia | Información accesible y trazable |
| PR-06 | Innovación | Adopción de mejores prácticas y tecnologías |

## Estructura Organizacional

**Misión DGI:** Facilitar la gestión efectiva del GORE Ñuble mediante control de gestión, modernización de procesos, transformación digital y gestión del conocimiento, apoyando la toma de decisiones de la AR y la mejora continua de los servicios a la ciudadanía.

**Visión DGI:** Referente de gestión institucional en los Gobiernos Regionales de Chile, destacando por calidad de asesoría, innovación metodológica y uso efectivo de tecnologías.

**Áreas funcionales:**

| Área | Dominio |
|------|---------|
| Control de Gestión | Monitoreo de indicadores, dashboards, alertas, informes ejecutivos |
| Modernización de Procesos | Levantamiento BPMN, análisis de mejora, diseño de automatizaciones |
| Transformación Digital | Cumplimiento TDE, Comité TD, administración funcional de sistemas |
| Gestión del Conocimiento | Curación KB, administración agentes IA, capacitación y gestión del cambio |

**Perfiles de cargo:**

| Cargo | Dependencia | Funciones principales |
|-------|-------------|----------------------|
| Jefe(a) DGI | Administración Regional | Dirigir y coordinar equipo DGI; asesorar a AR; representar al DGI en instancias colegiadas; gestionar recursos; reportar estado de iniciativas |
| Especialista Procesos | Jefe DGI | Levantar y modelar BPMN; identificar oportunidades de mejora; diseñar automatizaciones; acompañar implementación; documentar procedimientos |
| Especialista TD | Jefe DGI | Monitorear cumplimiento TDE; secretaría técnica Comité TD; curar y mantener KB; administrar agentes IA; facilitar interoperabilidad |
| Especialista Control | Jefe DGI | Definir y monitorear indicadores; elaborar y mantener dashboards; detectar desviaciones; generar informes ejecutivos; proponer acciones correctivas |

**Matriz RACI:**

| Actividad | Jefe | Procesos | TD | Control | División | AR |
|-----------|:----:|:--------:|:--:|:-------:|:--------:|:--:|
| Diseñar indicadores | C | I | I | R | C | A |
| Levantar procesos | C | R | I | I | C | I |
| Gestionar KB | C | I | R | I | I | I |
| Administrar dashboards | C | I | I | R | I | I |
| Reportar a AR | R | C | C | C | I | A |
| Coordinar con divisiones | R | C | C | C | C | A |

R=Responsable, A=Aprueba, C=Consultado, I=Informado.

## Control de Gestión

**Proceso de monitoreo de indicadores:**

| Paso | Acciones |
|------|---------|
| 1. Definición | Identificar objetivos (ERD, Ñuble 250); definir indicadores SMART; establecer metas y umbrales; documentar ficha por indicador |
| 2. Recolección | Identificar fuentes de datos; establecer frecuencia de actualización; definir responsable de provisión; validar calidad |
| 3. Análisis | Aplicar fórmulas definidas; comparar con metas y períodos anteriores; identificar tendencias y desviaciones; documentar hallazgos |
| 4. Comunicación | Actualizar dashboard; generar alertas si corresponde; informar a responsables |

**Tipos de dashboard:**

| Tipo | Audiencia | Contenido | Frecuencia |
|------|-----------|-----------|-----------|
| Ejecutivo | AR, Gobernador | KPIs agregados, alertas críticas | Diaria |
| División | Jefe División | Indicadores de la división | Semanal |
| Operativo | Equipos | Detalle tareas y estados | Diaria |
| Temático | Comités | Foco específico (IPR, TD, etc.) | Según comité |

**Detección de cuellos de botella — señales de alerta:**
- Indicadores bajo umbral por más de 2 períodos.
- Acumulación de trabajo pendiente.
- Incremento en tiempos de ciclo.
- Reclamos o consultas recurrentes sobre mismo tema.
- Desviaciones presupuestarias significativas.

Proceso de investigación: Detección → Verificación (confirmar que el problema es real y significativo) → Análisis (causa raíz: 5 porqués o Ishikawa) → Propuesta (formular recomendación) → Comunicación (responsable y AR) → Seguimiento (verificar efectividad).

**Estructura Informe de Estado Situacional:**
1. Resumen Ejecutivo: estado general (semáforo), principales logros, alertas activas.
2. Indicadores Clave: tabla resumen con tendencia, gráficos de evolución.
3. Alertas y Riesgos: problemas detectados, acciones en curso, riesgos emergentes.
4. Avance de Iniciativas: estado de proyectos DGI, hitos cumplidos/pendientes.
5. Recomendaciones: decisiones requeridas, acciones sugeridas.
6. Próximo Período: prioridades, hitos esperados.

Frecuencia: semanal (resumen) / mensual (completo).

## Modernización de Procesos

**Levantamiento y modelado BPMN:**

| Fase | Acciones |
|------|---------|
| Preparación | Identificar proceso; definir alcance (inicio, fin, actores); programar sesiones; preparar materiales |
| Recolección | Entrevistas con ejecutores; observación en terreno; revisión de documentación existente; identificar variantes y excepciones |
| Modelado | Crear diagrama BPMN AS-IS; documentar roles y sistemas; documentar reglas de negocio; validar con participantes |
| Documentación | Completar ficha de proceso; registrar métricas actuales (tiempos, volúmenes); identificar puntos de dolor; almacenar en repositorio |

Elementos mínimos BPMN: eventos de inicio y fin · actividades con responsable · flujos de secuencia · compuertas de decisión · pools/lanes por actor · anotaciones explicativas.

**Análisis de oportunidades de mejora:**

| Dimensión | Pregunta |
|-----------|---------|
| Valor | ¿Cada actividad agrega valor al resultado? |
| Duplicación | ¿Hay actividades redundantes? |
| Esperas | ¿Dónde se acumula trabajo sin procesar? |
| Movimientos | ¿Hay traslados innecesarios de información? |
| Errores | ¿Dónde ocurren más errores o reprocesos? |
| Automatización | ¿Qué actividades son repetitivas y basadas en reglas? |

Priorización: Alto Impacto + Bajo Esfuerzo primero. Validar con División responsable e incorporar al plan de trabajo.

**Tipos de automatización:**

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| RPA | Automatización de tareas repetitivas | Carga de datos entre sistemas |
| Flujos de trabajo | Orquestación de aprobaciones | Circuito de visación |
| Notificaciones | Alertas automáticas | Vencimiento de convenio |
| Reportes | Generación programada | Informe semanal |
| Integraciones | Conexión entre sistemas | SIGFE ↔ Dashboard |

**Ciclo de implementación:**

| Fase | Acciones |
|------|---------|
| Preparación | Confirmar recursos; comunicar cambio a afectados; preparar capacitación; configurar ambiente |
| Piloto | Implementar en alcance reducido; monitorear intensivamente; recoger feedback; ajustar |
| Despliegue | Extender a alcance completo; capacitar usuarios; documentar nuevo procedimiento; comunicar |
| Estabilización | Monitorear indicadores; atender incidentes; refinar configuración; cerrar proyecto formalmente |
| Mejora continua | Medir resultados vs. línea base; identificar nuevas oportunidades; documentar lecciones aprendidas |

## Transformación Digital

**Coordinación cumplimiento Ley 21.180 — responsabilidades DGI:**
- Monitoreo: inventario de procesos y nivel de digitalización; identificar brechas respecto a requisitos TDE; reportar al Comité TD.
- Planificación: proponer roadmap de cumplimiento; priorizar procesos a digitalizar; estimar recursos requeridos.
- Facilitación: apoyar a divisiones en digitalización; coordinar aspectos técnicos con Unidad de Operaciones; gestionar dependencias.
- Verificación: validar que implementaciones cumplan normas técnicas; documentar evidencia; preparar información para auditorías.

**Checklist de cumplimiento por proceso:**
- Procedimiento documentado.
- Firma electrónica implementada.
- Notificaciones electrónicas habilitadas.
- Expediente electrónico configurado.
- Interoperabilidad especificada.
- Autenticación con ClaveÚnica (si aplica).

**Comité TD — gestión:** Secretaría técnica: preparar tabla y materiales → elaborar actas → dar seguimiento a acuerdos. Análisis de propuestas: presentar estado de avance TDE, proponer iniciativas, evaluar factibilidad. Frecuencia mínima: mensual.

**Matriz de responsabilidades — administración funcional de sistemas:**

| Función | DGI | TI |
|---------|:---:|:--:|
| Definir requisitos funcionales | R | C |
| Configurar reglas de negocio | R | I |
| Definir perfiles y roles | R | C |
| Habilitar cuentas y accesos | I | R |
| Mantener infraestructura/seguridad | I | R |
| Resolver incidentes de negocio | R | I |
| Resolver incidentes técnicos | C | R |
| Evolucionar plataforma | R | C |

**Gestión de datos e interoperabilidad:**
- Principios: Datos como activo estratégico · Fuente única de verdad (cada dato tiene una fuente autoritativa definida) · Interoperabilidad por diseño.
- Inventario: identificar conjuntos de datos críticos, documentar ubicación y formato, identificar dueño de datos.
- Calidad: definir estándares de calidad por conjunto, monitorear cumplimiento, gestionar correcciones.
- Integración: especificar necesidades de intercambio, diseñar interfaces (APIs, archivos), implementar y monitorear.

## Gestión del Conocimiento

**Proceso de curación de KB:**

| Fase | Acciones |
|------|---------|
| Identificación | Detectar conocimiento nuevo o actualizado; evaluar relevancia institucional; priorizar incorporación |
| Estructuración | Formatear según estándares KODA; asignar metadatos (URN, categorías); vincular con artefactos relacionados |
| Validación | Verificar exactitud del contenido; validar con expertos de dominio; aprobar publicación |
| Publicación | Incorporar al catálogo; actualizar índices y referencias; comunicar disponibilidad |
| Mantenimiento | Revisar vigencia periódicamente; actualizar ante cambios normativos; deprecar contenido obsoleto |

Criterios de priorización: frecuencia de consulta esperada · criticidad para operación · riesgo de información desactualizada · demanda explícita de usuarios.

**Ciclo de vida de agentes IA:**

| Fase | Acciones |
|------|---------|
| Diseño | Definir propósito y alcance; especificar fuentes de conocimiento; diseñar flujos de interacción; establecer límites de actuación |
| Desarrollo | Configurar agente según especificación; entrenar con conocimiento relevante; probar funcionamiento |
| Despliegue | Habilitar acceso a usuarios; capacitar en uso; monitorear adopción |
| Operación | Monitorear interacciones; detectar respuestas inadecuadas; refinar entrenamiento; actualizar conocimiento |
| Evolución | Evaluar efectividad; identificar mejoras; implementar versiones mejoradas |

**Gobernanza de IA:** Todo agente debe tener un dueño funcional. Las respuestas deben ser auditables. El conocimiento base debe estar documentado. Los usuarios deben saber que interactúan con IA.

**Capacitación y gestión del cambio:**
- Principios: Cambio centrado en personas (tecnología es medio, no fin) · Comunicación permanente (informar el "porqué" antes del "qué") · Participación (involucrar a afectados en diseño de soluciones) · Gradualidad (cambios incrementales sobre revoluciones).

| Fase | Acciones |
|------|---------|
| Preparación | Identificar stakeholders; evaluar impacto del cambio; diseñar estrategia de comunicación; identificar resistencias potenciales |
| Comunicación | Explicar el porqué del cambio; mostrar beneficios concretos; responder dudas; mantener comunicación constante |
| Capacitación | Diseñar programa según audiencia; ejecutar capacitaciones prácticas; proveer materiales de apoyo; evaluar aprendizaje |
| Acompañamiento | Proveer soporte durante transición; resolver problemas emergentes; celebrar éxitos tempranos; ajustar según feedback |
| Consolidación | Verificar adopción; reforzar nuevas prácticas; documentar lecciones aprendidas |

## Funciones Habilitadoras

**Gestión Arquitectural (Meyer):** Regla de Oro: Autoridad = Responsabilidad · Dominios Precisos: sin superposiciones · Sinergias: agrupación de especialistas.

**Dinámica de Producción (Lean/Kanban):** Visualización de flujo (Tableros) · Límites WIP (Work in Progress) · Métricas: Throughput (rendimiento) y Lead Time (tiempo ciclo).

**Navegación Social (ADKAR):** Rol de Lobbista Interno: facilitar, no imponer · Modelo ADKAR (Awareness, Desire, Knowledge, Ability, Reinforcement) · Influencia Ética: reciprocidad y prueba social.

## Coordinación Institucional

**Relación con AR:** Reunión semanal. Contenido: estado de iniciativas DGI, alertas y escalamientos, decisiones requeridas, prioridades para el próximo período. Escalamiento: temas que requieren decisión de AR → Informe Ejecutivo con opciones y recomendación.

**Matriz de interacción con divisiones:**

| División | Tipo de Interacción | Frecuencia |
|---------|---------------------|-----------|
| Gabinete | Agenda estratégica, comunicación política | Según necesidad |
| DAF | Indicadores presupuestarios, rendiciones | Semanal |
| DIPIR | Cartera IPR, estados de avance | Semanal |
| Jurídica | Convenios, resoluciones, cumplimiento | Quincenal |
| DIPLADE | Indicadores ERD, planificación | Mensual |
| Unidad Operaciones | Sistemas, interoperabilidad, infraestructura | Mensual (Mesa Técnica) |
| Auditoría Interna | Cumplimiento, control interno | Trimestral |

**Protocolo de escalamiento:**

| Nivel | Situación | Escalar a | Plazo |
|-------|-----------|-----------|-------|
| 1 | Incidente operativo | Jefe DGI | 4 horas |
| 2 | Bloqueo de proyecto | Administración Regional | 24 horas |
| 3 | Conflicto entre divisiones | Administración Regional | 48 horas |
| 4 | Decisión estratégica | Gobernador (vía AR) | Según urgencia |

Información requerida para escalar: descripción del problema · impacto si no se resuelve · opciones de solución · recomendación · plazo requerido para decisión · firma responsable del escalamiento.

**Participación en comités:**

| Comité | Rol DGI | Frecuencia |
|--------|---------|-----------|
| Comité de Transformación Digital | Secretaría técnica | Mensual |
| Comité de Coordinación Regional | Informante | Según convocatoria |
| Mesas de trabajo temáticas | Facilitador técnico | Según necesidad |
