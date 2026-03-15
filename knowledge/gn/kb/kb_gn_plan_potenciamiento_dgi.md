---
_manifest:
  urn: "urn:gn:kb:plan-potenciamiento-dgi"
  provenance:
    created_by: "felixsanhueza"
    created_at: "2026-03-15"
    source: "implementation_plan.md"
version: "1.0.0"
status: draft
tags: [dgi, plan-potenciamiento, meyer, lean-six-sigma, gestion-del-cambio]
lang: es
extensions:
  gn:
    family: "normative"
---

# Plan de Potenciamiento DGI

## Resumen

Modelo de integración para el potenciamiento del DGI del GORE Ñuble, articulando tres perspectivas: estructura organizacional (Meyer), mejora sistemática de procesos (Lean Six Sigma / DMAIC) y navegación social para gestión del cambio. Incluye catálogo de productos, mapas de stakeholders y modelos cognitivos para el AR Virtual.

---

## Síntesis de Perspectivas

### Perspectiva Meyer: Estructura como Ciencia

| Principio | Aplicación al DGI |
|-----------|-------------------|
| Regla de Oro | Autoridad y responsabilidad deben coincidir. El DGI asesora pero NO decide por las divisiones. |
| Especialización + Trabajo en Equipo | Cada rol del DGI debe ser experto de clase mundial en su dominio, colaborando con pares especializados. |
| Dominios Precisos | Límites claros entre Control de Gestión, Procesos y TD sin superposiciones ni brechas. |
| Base para Subestructura | Subdividir por especialidad técnica (qué producen), no por cliente o proceso interno. |
| Evitar Conflictos de Interés | No mezclar funciones de auditoría con servicios; no mezclar estabilidad con innovación. |
| Agrupar por Sinergias Profesionales | Mantener especialistas similares juntos para intercambio profesional y economías de escala. |
| Negocio Dentro del Negocio | Cada rol del DGI es un "emprendedor interno" que vende productos/servicios a clientes internos. |

### Perspectiva Lean Six Sigma: Mejora Sistemática

| Concepto | Aplicación al DGI |
|----------|-------------------|
| 5S | Organización visual del conocimiento institucional y flujos de trabajo |
| DMAIC | Ciclo sistemático para proyectos de mejora: Definir → Medir → Analizar → Mejorar → Controlar |
| Eliminación de Desperdicios | Identificar y reducir actividades que no agregan valor en procesos del GORE |
| Control Estadístico | Uso de datos para detectar desviaciones antes de que escalen |
| Kaizen | Cultura de mejora continua pequeña y constante vs. grandes revoluciones |

---

## Arquitectura de Integración

### Building Blocks (Meyer)

Organización del DGI según principios de especialización y dominios precisos, donde cada rol opera como un "negocio dentro del negocio".

| Block | Roles | Productos |
|-------|-------|-----------|
| Engineers (Base) | Especialista Procesos, Especialista TD | Modelos BPMN, diseños de automatización, especificaciones técnicas; configuraciones KB, agentes IA, arquitecturas de integración |
| Service Providers (Asset-based) | Especialista Control | Dashboards, informes periódicos, alertas operativas |
| Coordinators | Jefe DGI | Planificación estratégica, facilitación de consensos, gestión de prioridades |
| Sales & Marketing (Internal) | Navegador Institucional | Mapeo stakeholders, estrategia de influencia, acompañamiento en transiciones |

### Catálogo de Productos DGI

| Bloque | Productos |
|--------|-----------|
| Engineers - Procesos | Modelo BPMN proceso AS-IS; Diseño proceso TO-BE; Especificación de automatización; Análisis de causa raíz |
| Engineers - TD | Artefacto conocimiento estructurado; Agente IA configurado; Integración entre sistemas; Capacitación técnica |
| Service Providers - Control | Dashboard ejecutivo (diario); Informe estado situacional (semanal); Alerta de desviación (continuo); Métrica calculada y verificada |
| Coordinators - Jefatura | Plan de trabajo consensuado; Priorización de iniciativas; Resolución de conflictos; Comunicación con AR |

### Relaciones Cliente-Proveedor

**Paradigma:** Business Within a Business.

**Clientes internos:**
- Administración Regional: estrategia, prioridades
- Divisiones: mejoras operativas, cumplimiento TDE
- Comité TD: secretaría técnica

**Modelo de interacción:**
- Catálogo de servicios publicado
- Solicitudes canalizadas formalmente
- SLAs definidos por tipo de producto
- Feedback estructurado post-entrega

**Principio clave:** El DGI PROPONE y FACILITA; las divisiones DECIDEN y EJECUTAN. Autoridad para decidir = Responsabilidad por resultados.

---

## Marco DMAIC

### Marco operativo DMAIC para DGI

Cada proyecto de mejora del DGI sigue el ciclo DMAIC:

| Fase | Actividades |
|------|-------------|
| Define | Identificar problema/oportunidad; establecer alcance y objetivos SMART; definir stakeholders y sponsor; documentar caso de negocio |
| Measure | Establecer línea base con métricas actuales; recopilar datos del proceso AS-IS; validar sistema de medición; crear Value Stream Map si aplica |
| Analyze | Análisis de causa raíz (5 Porqués, Ishikawa); identificar cuellos de botella; cuantificar oportunidades; priorizar causas según impacto |
| Improve | Diseñar solución TO-BE; prototipar y pilotear; implementar cambios; capacitar usuarios |
| Control | Establecer controles estadísticos; documentar nuevo estándar; crear alertas automáticas; transferir a operación normal |

### Sistema 5S para Gestión del Conocimiento

| S | Concepto | Aplicación |
|---|----------|-----------|
| Seiri | Clasificar | Auditar artefactos, deprecar obsoletos, categorizar por utilidad |
| Seiton | Ordenar | URNs consistentes, catálogo maestro, taxonomía clara |
| Seiso | Limpiar | Revisión periódica de vigencia, corrección de errores |
| Seiketsu | Estandarizar | Plantillas KODA, procesos de curación, naming conventions |
| Shitsuke | Disciplina | Cultura de actualización, governance de KB, capacitación continua |

### Proyecto Piloto DMAIC Sugerido: Flujo de Visación de Actos Administrativos

| Fase | Entregable |
|------|-----------|
| Define | Charter: objetivo de reducir tiempo de visación en 30% |
| Measure | VSM actual, tiempos de ciclo por etapa, volumen mensual |
| Analyze | Identificación de esperas, reprocesos, cuellos de botella |
| Improve | Automatización de notificaciones, checklist digital, flujo en paralelo |
| Control | Dashboard de seguimiento, alertas de SLA, revisión mensual |

### Tablero Kanban para Gestión de Iniciativas

**Columnas:** BACKLOG → EN DISEÑO (DMAIC D-M-A) → EN IMPLEMENTACIÓN (DMAIC I) → EN VERIFICACIÓN (DMAIC C) → COMPLETADO.

**Límites WIP:**

| Columna | WIP Máximo |
|---------|-----------|
| En Diseño | 2 |
| En Implementación | 3 |
| En Verificación | 2 |

---

## Navegación Social y Gestión del Cambio

### El Rol del Navegador Institucional

**Block:** Sales & Marketing (Internal). También llamado: Gestor de Relaciones y Cambio.

**Definición:** Profesional que cultiva relaciones estratégicas con stakeholders clave, facilita la adopción de cambios y "vende" internamente el valor del DGI sin imponer ni auditar.

**Principio guía:** "No vendemos productos; ayudamos a las divisiones a descubrir cómo nuestros servicios pueden resolver sus dolores operativos."

**Productos:**
- Mapeo de stakeholders actualizado
- Diagnóstico de clima organizacional por división
- Estrategia de influencia por iniciativa
- Acompañamiento en transiciones
- Comunicación de éxitos y valor generado
- Feedback estructurado desde divisiones

### Mapa de Stakeholders GORE

| Nivel | Actor | Poder | Interés DGI | Estrategia |
|-------|-------|-------|------------|------------|
| Estratégico | Gobernador Regional | Alto | Variable (depende de agenda política) | Demostrar impacto en ERD y ciudadanía |
| Estratégico | Administrador/a Regional | Alto | Alto (sponsor natural) | Mantener informado, visibilizar quick wins |
| Táctico | Jefes de División | Medio-Alto | Variable (algunos resistentes) | Identificar campeones, resolver dolores primero, no amenazar autonomía |
| Táctico | Comité de Transformación Digital | Medio | Alto | Proveer secretaría técnica impecable |
| Operativo | Profesionales de divisiones | Bajo individual / Alto colectivo | Variable | Capacitación como servicio, celebrar adopciones, crear red de embajadores |

### Modelo ADKAR

| Fase | Pregunta | Acción |
|------|---------|--------|
| Awareness | ¿Por qué cambiar? | Comunicar el problema claramente, usar datos |
| Desire | ¿Qué gano yo? | Mostrar beneficios concretos para cada stakeholder |
| Knowledge | ¿Cómo lo hago? | Capacitar, proveer materiales, acompañar |
| Ability | ¿Puedo hacerlo? | Pilotear, ajustar, dar tiempo de práctica |
| Reinforcement | ¿Seguirá funcionando? | Celebrar éxitos, medir, reconocer |

### Tácticas de Influencia Ética

*El Navegador Institucional usa influencia, NO manipulación.*

| Táctica | Descripción | Ejemplo |
|---------|-------------|---------|
| Reciprocidad | Dar antes de pedir | Resolver un dolor pequeño de una división antes de proponer proyecto mayor |
| Prueba Social | Mostrar que otros ya adoptaron | "La División X ya usa el dashboard y redujo 30% sus consultas" |
| Autoridad | Citar fuentes creíbles | "Según la normativa TDE, esto debe implementarse para 2026" |
| Escasez | Crear urgencia legítima | "Si no priorizamos esto ahora, no cumpliremos el plazo del PMG" |
| Consistencia | Anclar a compromisos previos | "En la última reunión de Comité, se acordó avanzar en esta línea" |
| Simpatía | Construir relación genuina | Reuniones periódicas informales, conocer a las personas |

### Detección y manejo de resistencias

| Tipo | Síntomas | Respuesta |
|------|----------|-----------|
| Racional | Objeciones técnicas, preguntas sobre viabilidad | Escuchar, incorporar feedback, ajustar propuesta |
| Emocional | Frustración, comentarios sobre "otra moda más" | Empatizar, reconocer fatiga de cambios, ir gradual |
| Política | Sabotaje pasivo, demoras, "no es mi prioridad" | Identificar intereses, buscar win-win, escalar si es necesario |

**Protocolo:**
1. Escuchar genuinamente la objeción
2. Validar la preocupación legítima
3. Explorar intereses subyacentes
4. Buscar alternativa que satisfaga ambas partes
5. Documentar y ajustar enfoque
6. Si persiste: escalar a AR con propuesta de solución

### Métricas de éxito social

| Indicador | Meta | Medición |
|-----------|------|---------|
| NPS interno del DGI | > 50 | Encuesta trimestral a divisiones |
| Tasa de adopción voluntaria | > 70% | % de divisiones que solicitan servicios |
| Tiempo de respuesta a solicitudes | < 48h | Registro en sistema |
| Proyectos completados sin escalamiento | > 80% | Conteo de escalamientos a AR |
| Red de embajadores | 1 por división | Conteo de personas identificadas |

---

## Modelos Cognitivos para AR Virtual

| Modelo | Propósito | Dimensiones |
|--------|-----------|-------------|
| CM-LEAN-THINKING | Evaluar situaciones desde perspectiva de mejora continua | 7+1 mudas; ciclo PDCA; priorizar por impacto/esfuerzo; causa raíz antes de solucionar; mejoras pequeñas y constantes |
| CM-STRUCTURE-PRINCIPLES | Evaluar propuestas organizacionales según ciencia de Meyer | Coincidencia autoridad-responsabilidad; dominios precisos sin superposición; especialización vs. generalización; conflictos de interés; sinergias profesionales |
| CM-SOCIAL-NAVIGATION | Evaluar dimensión social de cambios organizacionales | Mapear stakeholders; ADKAR completo; táctica de influencia apropiada; tipo de resistencia; comunicación y acompañamiento |
| CM-DMAIC-EVALUATOR | Evaluar proyectos de mejora según metodología DMAIC | DEFINE: problema claro, alcance, sponsor; MEASURE: línea base, datos confiables; ANALYZE: causa raíz, priorización; IMPROVE: solución diseñada, pilotaje; CONTROL: controles, transferencia a operación |
