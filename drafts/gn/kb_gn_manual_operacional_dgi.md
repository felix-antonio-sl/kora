---
_manifest:
  urn: "urn:gn:kb:manual-operacional-dgi"
  provenance:
    created_by: "felixsanhueza"
    created_at: "2026-03-15"
    source: "manual_operacional_dgi.md"
version: "1.0.0"
status: draft
tags: [dgi, manual-operacional, gestion-institucional, gore-nuble, transformacion-digital]
lang: es
extensions:
  gn:
    family: "manual"
---

# Manual Operacional del Departamento de Gestión Institucional

## Resumen

Marco operativo del DGI del GORE Ñuble: estructura organizacional, funciones de las 4 áreas (Control de Gestión, Modernización de Procesos, Transformación Digital, Gestión del Conocimiento) y mecanismos de coordinación institucional. Normativa base: Ley N° 19.175, Ley N° 21.180, DS 14/2014, Resolución N° 22/2023.

---

## Disposiciones Generales

**Objeto:** Establece el marco operativo del DGI del GORE Ñuble, definiendo estructura, funciones, procesos y mecanismos de coordinación institucional.

**Alcance:** Aplicable a todo el personal del DGI y a las interacciones con divisiones, unidades y actores externos relacionados con sus funciones.

### Definiciones operacionales

| Sigla | Definición |
|-------|------------|
| DGI | Departamento de Gestión Institucional |
| AR | Administración Regional |
| TD | Transformación Digital |
| TDE | Transformación Digital del Estado (Ley N° 21.180) |
| KB | Knowledge Base / Base de Conocimiento |
| BPMN | Business Process Model and Notation |
| KPI | Key Performance Indicator |
| GORE | Gobierno Regional |
| ERD | Estrategia Regional de Desarrollo |

### Marco Normativo

- Ley N° 19.175: Orgánica Constitucional sobre Gobierno y Administración Regional
- Ley N° 21.180: Transformación Digital del Estado
- DS 14/2014: Modelo de Gestión de Procesos
- Resolución N° 22/2023: Normas Técnicas de Interoperabilidad
- PMG: Programa de Mejoramiento de la Gestión

### Principios Rectores

| Principio | Descripción |
|-----------|-------------|
| Orientación al servicio | Foco en necesidades de usuarios internos y finales |
| Basado en datos | Decisiones sustentadas en información verificable |
| Mejora continua | Optimización sistemática de procesos |
| Colaboración | Trabajo conjunto con todas las divisiones |
| Transparencia | Información accesible y trazable |
| Innovación | Adopción de mejores prácticas y tecnologías |

---

## Estructura Organizacional

**Misión DGI:** Facilitar la gestión efectiva del GORE Ñuble mediante control de gestión, modernización de procesos, transformación digital y gestión del conocimiento, apoyando la toma de decisiones de la Administración Regional y la mejora continua de los servicios a la ciudadanía.

**Visión DGI:** Ser referente de gestión institucional en los Gobiernos Regionales de Chile, destacando por la calidad de su asesoría, innovación metodológica y uso efectivo de tecnologías para la gestión pública.

### Áreas funcionales

| ID | Área | Descripción |
|----|------|-------------|
| DOM-CG | Control de Gestión | Monitoreo de indicadores, dashboards, alertas, informes ejecutivos |
| DOM-MP | Modernización de Procesos | Levantamiento BPMN, análisis de mejora, diseño de automatizaciones |
| DOM-TD | Transformación Digital | Cumplimiento TDE, Comité TD, administración funcional de sistemas |
| DOM-KC | Gestión del Conocimiento | Curación KB, administración agentes IA, capacitación y gestión del cambio |

### Perfiles de cargo

**Jefe(a) DGI** (dependencia: Administración Regional)
- Dirigir y coordinar el equipo DGI
- Asesorar a AR en materias de gestión institucional
- Representar al DGI en instancias colegiadas
- Gestionar recursos del departamento
- Reportar estado de iniciativas a AR

**Especialista en Modernización de Procesos** (dependencia: Jefe DGI)
- Levantar y modelar procesos BPMN
- Identificar oportunidades de mejora
- Diseñar automatizaciones
- Acompañar implementación de cambios
- Documentar procedimientos optimizados

**Especialista en Transformación Digital** (dependencia: Jefe DGI)
- Monitorear cumplimiento TDE
- Gestionar secretaría técnica Comité TD
- Curar y mantener base de conocimiento
- Administrar agentes IA institucionales
- Facilitar interoperabilidad de sistemas

**Especialista en Control de Gestión** (dependencia: Jefe DGI)
- Definir y monitorear indicadores
- Elaborar y mantener dashboards
- Detectar y analizar desviaciones
- Generar informes ejecutivos
- Proponer acciones correctivas

### Matriz RACI

| Actividad | Jefe | Procesos | TD | Control | División | AR |
|-----------|------|----------|----|---------|----------|----|
| Diseñar indicadores | C | I | I | R | C | A |
| Levantar procesos | C | R | I | I | C | I |
| Gestionar KB | C | I | R | I | I | I |
| Administrar dashboards | C | I | I | R | I | I |
| Reportar a AR | R | C | C | C | I | A |
| Coordinar con divisiones | R | C | C | C | C | A |

*R=Responsable, A=Aprueba, C=Consultado, I=Informado*

---

## Control de Gestión

### Monitoreo de indicadores institucionales

**Objetivo:** Mantener visibilidad permanente sobre el estado de gestión del GORE.

1. **Definición de indicadores:** Identificar objetivos estratégicos (ERD, Ñuble 250) → definir indicadores SMART → establecer metas y umbrales de alerta → documentar ficha por indicador.
2. **Recolección de datos:** Identificar fuentes por indicador → establecer frecuencia → definir responsable de provisión → validar calidad.
3. **Cálculo y análisis:** Aplicar fórmulas → comparar con metas y períodos anteriores → identificar tendencias y desviaciones → documentar hallazgos.
4. **Comunicación:** Actualizar dashboard → generar alertas si corresponde → informar a responsables.

### Tipos de Dashboard

| Tipo | Audiencia | Contenido | Frecuencia |
|------|-----------|-----------|------------|
| Ejecutivo | AR, Gobernador | KPIs agregados, alertas críticas | Diaria |
| División | Jefe División | Indicadores de la división | Semanal |
| Operativo | Equipos | Detalle de tareas y estados | Diario |
| Temático | Comités | Foco específico (IPR, TD, etc.) | Según comité |

### Detección de cuellos de botella

**Señales de alerta:**
- Indicadores bajo umbral por más de 2 períodos
- Acumulación de trabajo pendiente
- Incremento en tiempos de ciclo
- Reclamos o consultas recurrentes sobre mismo tema
- Desviaciones presupuestarias significativas

**Proceso de investigación:**
1. Detección: Sistema de alertas o reporte de división
2. Verificación: Confirmar que el problema es real y significativo
3. Análisis: Identificar causa raíz (5 porqués, Ishikawa)
4. Propuesta: Formular recomendación de solución
5. Comunicación: Informar a responsable y AR
6. Seguimiento: Verificar implementación y efectividad

### Estructura Informe Estado Situacional

| Sección | Contenido |
|---------|-----------|
| 1. Resumen Ejecutivo | Estado general (semáforo), principales logros, alertas activas |
| 2. Indicadores Clave | Tabla resumen con tendencia, gráficos de evolución |
| 3. Alertas y Riesgos | Problemas detectados, acciones en curso, riesgos emergentes |
| 4. Avance de Iniciativas | Estado de proyectos DGI, hitos cumplidos/pendientes |
| 5. Recomendaciones | Decisiones requeridas, acciones sugeridas |
| 6. Próximo Período | Prioridades, hitos esperados |

**Frecuencia:** Semanal (resumen) / Mensual (completo).

---

## Modernización de Procesos

### Levantamiento y modelado BPMN

**Fases:**

| Fase | Actividades |
|------|-------------|
| Preparación | Identificar proceso a levantar; definir alcance (inicio, fin, actores); programar sesiones; preparar materiales |
| Recolección | Entrevistas con ejecutores; observación en terreno; revisar documentación; identificar variantes y excepciones |
| Modelado | Diagrama BPMN AS-IS; identificar roles y sistemas; documentar reglas de negocio; validar con participantes |
| Documentación | Completar ficha de proceso; registrar métricas actuales (tiempos, volúmenes); identificar puntos de dolor; almacenar en repositorio |

**Elementos BPMN mínimos requeridos:**
- Eventos de inicio y fin
- Actividades con responsable
- Flujos de secuencia
- Compuertas de decisión
- Pools/lanes por actor
- Anotaciones explicativas

### Análisis de oportunidades de mejora

| Dimensión | Pregunta |
|-----------|---------|
| Valor | ¿Cada actividad agrega valor al resultado? |
| Duplicación | ¿Hay actividades redundantes? |
| Esperas | ¿Dónde se acumula trabajo sin procesar? |
| Movimientos | ¿Hay traslados innecesarios de información? |
| Errores | ¿Dónde ocurren más errores o reprocesos? |
| Automatización | ¿Qué actividades son repetitivas y basadas en reglas? |

**Priorización:** Alto impacto + Bajo esfuerzo primero. Validar con División responsable.

### Tipos de automatización

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| RPA | Automatización de tareas repetitivas | Carga de datos entre sistemas |
| Flujos de trabajo | Orquestación de aprobaciones | Circuito de visación |
| Notificaciones | Alertas automáticas | Vencimiento de convenio |
| Reportes | Generación programada | Informe semanal |
| Integraciones | Conexión entre sistemas | SIGFE – Dashboard |

### Proceso de implementación

| Fase | Actividades |
|------|-------------|
| Preparación | Confirmar recursos; comunicar cambio; preparar materiales de capacitación; configurar ambiente |
| Piloto | Implementar en alcance reducido; monitorear intensivamente; recoger feedback; ajustar |
| Despliegue | Extender a alcance completo; capacitar usuarios; documentar procedimiento actualizado; comunicar |
| Estabilización | Monitorear indicadores; atender incidentes; refinar configuración; cerrar proyecto formal |
| Mejora continua | Medir resultados vs. línea base; identificar nuevas oportunidades; documentar lecciones aprendidas |

---

## Transformación Digital

### Coordinación cumplimiento Ley N° 21.180

**Responsabilidades:**

| Función | Actividades |
|---------|-------------|
| Monitoreo | Inventario de procesos y nivel de digitalización; identificar brechas TDE; reportar al Comité TD |
| Planificación | Proponer roadmap de cumplimiento; priorizar procesos a digitalizar; estimar recursos |
| Facilitación | Apoyar a divisiones; coordinar aspectos técnicos con Unidad de Operaciones; gestionar dependencias |
| Verificación | Validar que implementaciones cumplan normas técnicas; documentar evidencia; preparar auditorías |

**Checklist de cumplimiento TDE:**
- Procedimiento documentado
- Firma electrónica implementada
- Notificaciones electrónicas habilitadas
- Expediente electrónico configurado
- Interoperabilidad especificada
- Autenticación con ClaveÚnica (si aplica)

### Gestión del Comité de TD

**Frecuencia:** Mínimo mensual.

| Función | Actividades |
|---------|-------------|
| Secretaría Técnica | Preparar tabla y materiales; elaborar actas; dar seguimiento a acuerdos |
| Análisis de Propuestas | Presentar estado de avance TDE; proponer iniciativas para decisión; evaluar factibilidad |
| Coordinación | Articular divisiones en temas transversales; gestionar dependencias; escalar impedimentos |

### Administración funcional de sistemas

| Función | DGI | TI |
|---------|-----|-----|
| Definir requisitos funcionales | R | C |
| Configurar reglas de negocio | R | I |
| Definir perfiles y roles | R | C |
| Habilitar cuentas y accesos | I | R |
| Mantener infraestructura/seguridad | I | R |
| Resolver incidentes de negocio | R | I |
| Resolver incidentes técnicos | C | R |
| Evolucionar plataforma | R | C |

### Interoperabilidad y datos

**Principios:**
- Datos como activo: Los datos institucionales son un activo estratégico.
- Fuente única de verdad: Cada dato tiene una fuente autoritativa definida.
- Interoperabilidad por diseño: Los sistemas deben poder intercambiar datos.

---

## Gestión del Conocimiento

### Curación y actualización de KB

| Fase | Actividades |
|------|-------------|
| Identificación | Detectar conocimiento nuevo/actualizado; evaluar relevancia; priorizar incorporación |
| Estructuración | Formatear según estándares; asignar metadatos (URN, categorías); vincular con artefactos relacionados |
| Validación | Verificar exactitud; validar con expertos de dominio; aprobar publicación |
| Publicación | Incorporar al catálogo; actualizar índices y referencias; comunicar disponibilidad |
| Mantenimiento | Revisar vigencia periódicamente; actualizar ante cambios normativos; deprecar contenido obsoleto |

**Criterios de priorización:**
- Frecuencia de consulta esperada
- Criticidad para operación
- Riesgo de información desactualizada
- Demanda explícita de usuarios

### Administración de agentes IA

| Fase | Actividades |
|------|-------------|
| Diseño | Definir propósito y alcance; especificar fuentes de conocimiento; diseñar flujos; establecer límites |
| Desarrollo | Configurar según especificación; entrenar con conocimiento relevante; probar |
| Despliegue | Habilitar acceso; capacitar en uso; monitorear adopción |
| Operación | Monitorear interacciones; detectar respuestas inadecuadas; refinar entrenamiento; actualizar conocimiento |
| Evolución | Evaluar efectividad; identificar mejoras; implementar versiones mejoradas |

**Gobernanza de IA:**
- Todo agente debe tener un dueño funcional.
- Las respuestas deben ser auditables.
- El conocimiento base debe estar documentado.
- Los usuarios deben saber que interactúan con IA.

### Capacitación y gestión del cambio

**Principios:** Cambio centrado en personas. Comunicación permanente del *porqué* antes del *qué*. Participación de afectados en diseño de soluciones. Gradualidad: cambios incrementales sobre revoluciones.

| Fase | Actividades |
|------|-------------|
| Preparación | Identificar stakeholders; evaluar impacto; diseñar estrategia de comunicación; identificar resistencias |
| Comunicación | Explicar el porqué; mostrar beneficios concretos; responder dudas; mantener comunicación constante |
| Capacitación | Diseñar programa según audiencia; ejecutar capacitaciones prácticas; proveer materiales; evaluar aprendizaje |
| Acompañamiento | Proveer soporte durante transición; resolver problemas emergentes; celebrar éxitos tempranos; ajustar |
| Consolidación | Verificar adopción; reforzar nuevas prácticas; documentar lecciones aprendidas |

---

## Funciones Habilitadoras

| Función | Propósito | Conceptos Clave |
|---------|-----------|----------------|
| Gestión Arquitectural | Diseñar estructura organizacional saludable (Meyer) | Golden Rule: Autoridad = Responsabilidad; Dominios precisos sin superposiciones; Sinergias |
| Dinámica de Producción | Gestionar flujo de trabajo (Lean/Kanban) | Visualización de flujo; Límites WIP; Throughput, Lead Time |
| Navegación Social | Gestión del cambio y relaciones (ADKAR) | Lobbista interno: facilitar, no imponer; Modelo ADKAR; Influencia ética |

---

## Coordinación Institucional

### Relación con Administración Regional

- **Canal:** Reunión semanal de coordinación.
- **Contenidos:** Estado de iniciativas DGI, alertas y escalamientos, decisiones requeridas, prioridades para próximo período.
- **Escalamiento:** Temas que requieren decisión de AR se escalan mediante Informe Ejecutivo con opciones y recomendación.

### Matriz de interacción con divisiones

| División | Tipo de Interacción | Frecuencia |
|----------|--------------------|-----------:|
| Gabinete | Agenda estratégica, comunicación política | Según necesidad |
| DAF | Indicadores presupuestarios, rendiciones | Semanal |
| DIPIR | Cartera IPR, estados de avance | Semanal |
| Jurídica | Convenios, resoluciones, cumplimiento | Quincenal |
| DIPLADE | Indicadores ERD, planificación | Mensual |
| Unidad Operaciones | Sistemas, interoperabilidad, infraestructura | Mensual (Mesa Técnica) |
| Auditoría Interna | Cumplimiento, control interno | Trimestral |

### Protocolo de escalamiento

| Nivel | Situación | Escalar a | Plazo |
|-------|-----------|-----------|-------|
| 1 | Incidente operativo | Jefe DGI | 4 horas |
| 2 | Bloqueo de proyecto | Administración Regional | 24 horas |
| 3 | Conflicto entre divisiones | Administración Regional | 48 horas |
| 4 | Decisión estratégica | Gobernador (vía AR) | Según urgencia |

**Información requerida en escalamiento:** Descripción del problema; impacto si no se resuelve; opciones de solución; recomendación; plazo requerido para decisión; firma responsable del escalamiento.

### Participación en comités

| Comité | Rol DGI | Frecuencia |
|--------|---------|------------|
| Comité de Transformación Digital | Secretaría técnica | Mensual |
| Comité de Coordinación Regional | Informante | Según convocatoria |
| Mesas de trabajo temáticas | Facilitador técnico | Según necesidad |
