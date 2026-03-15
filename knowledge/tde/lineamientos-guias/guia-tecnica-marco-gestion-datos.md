---
_manifest:
  urn: "urn:kora:kb:tde:lineamientos-guias:guia-tecnica-marco-gestion-datos:1.0.0"
  provenance: "https://wikiguias.digital.gob.cl/guias/Guía_MGDE"
version: 1.0.0
status: draft
tags: [tde, lineamientos-guias, datos, guia-tecnica, dama, mgde, organos-administracion-estado]
lang: es
---

# Guía Técnica: aplicación del Marco de Referencia de Gestión de Datos del Estado (MGDE)

**Última actualización:** 29/11/2024 — **Autor:** Secretaría de Gobierno Digital

---

## 1. Contexto y objetivos

La guía orienta a los órganos de la Administración del Estado (OAE) en la adopción de buenas prácticas de gestión de datos usando el MGDE.

Está asociada a la **Ley N° 21.658** que crea la SGD, responsable de coordinar, asesorar y apoyar el uso estratégico de tecnologías digitales, datos e información pública.

Dos de las seis dimensiones del marco de políticas de Gobierno Digital de la OCDE son especialmente relevantes:

- **Impulsado por los datos:** valora los datos como activo estratégico y establece mecanismos de gobernanza, acceso, intercambio y reutilización.
- **Abierto por defecto:** pone a disposición pública los datos del gobierno y procesos de formulación de políticas, dentro de los límites legales y en equilibrio con el interés nacional.

### Beneficios de un marco de referencia de gestión de datos

- Alinea objetivos de datos con objetivos estratégicos institucionales.
- Mejora la calidad del servicio y la eficiencia de los procesos.
- Disminuye el tiempo de diseño y desarrollo de servicios.
- Optimiza costos de planificación, diseño, operación y mejora continua.
- Define mejor roles y responsabilidades en procesos de gestión de datos.
- Facilita sinergias entre personas, procesos, información y tecnología.
- Homogeniza la comprensión de la gestión de datos entre instituciones del Estado.

---

## 2. Normativa relacionada

**Ley N° 21.658** — crea la Secretaría de Gobierno Digital.
**Ley N° 18.575** — Orgánica constitucional de bases generales de la Administración del Estado (define OAEs).

---

## 3. Marco de Referencia de Gestión de Datos del Estado (MGDE)

El MGDE es una **adaptación del marco DAMA** (DAMA Management Body of Knowledge, DMBoK®) a la realidad chilena. Simplifica DAMA para permitir que OAE de distintas capacidades incorporen la gobernanza de datos, y complementa el modelo con dimensiones específicas a la realidad del servicio público chileno y la Ley 21.180.

### Principios orientadores (10)

Los OAE deben suscribir estos principios literalmente o adaptados a sus necesidades, e incluirlos en la política de gobernanza de datos:

1. La gestión de datos debe servir para **mejorar los servicios** a las personas.
2. Los datos internos y externos se tratan como **activos estratégicos**.
3. Todo activo de datos será **catalogado y documentado** con metadatos.
4. Todo activo de datos tendrá asignada una **persona responsable** (administrador o custodio).
5. Se promoverá la **digitalización, uso analítico y trabajo colaborativo** en torno a los datos.
6. Se promoverá la **evaluación de la calidad** de los datos.
7. Se promoverá la **interoperabilidad** de los datos, interna y externa.
8. Se procurará un **uso ético** de datos en cumplimiento de la normativa vigente.
9. Toda tarea de acceso a datos requiere **definición de roles y responsabilidades** en el contexto de las definiciones de seguridad institucionales.
10. La gestión de datos se planificará, implementará, evaluará y mejorará **de manera integral y continua** a lo largo del ciclo de vida de los datos.

**Ciclo de vida de los datos (8 etapas):** Generación → Recolección/captura → Procesamiento → Almacenamiento → Administración → Análisis → Visualización → Interpretación.

---

## 4. Dimensiones y criterios del MGDE

El MGDE está organizado en **12 dimensiones**, evaluadas según criterios que corresponden a los conceptos clave de cada dimensión. En total: **52 preguntas**.

| Dimensión | N° criterios | N° preguntas |
|-----------|-------------|-------------|
| Visión estratégica | 7 | 7 |
| Gobernanza de datos | 7 | 7 |
| Arquitectura, diseño y documentación | 4 | 6 |
| Almacenamiento y operación | 1 | 1 |
| Seguridad y ciberseguridad de datos | 4 | 6 |
| Integración e interoperabilidad | 2 | 4 |
| Documentos y contenidos | 4 | 4 |
| Datos maestros y de referencia | 3 | 3 |
| Analítica e inteligencia de negocios | 3 | 3 |
| Calidad de datos | 2 | 2 |
| Datos abiertos | 3 | 7 |
| Aspectos legales y normativos | 2 | 2 |

### Descripción de dimensiones

**Visión estratégica** — genera el compromiso de la institución con la gestión de datos, asegurando su alineación con objetivos institucionales para un mandato de largo plazo. Criterios: Visión, Estrategia, Presupuesto y recursos, Capacidades, Gestión del cambio, Alianzas y colaboraciones, Medición y seguimiento.

**Gobernanza de datos** — define visión, políticas y estrategias alineadas a objetivos institucionales para potenciar los datos como activos organizacionales. Criterios: Política de gobernanza, Organización, Implementación, Herramientas, Capacitación, Gestión de riesgos, Gestión ética de datos.

**Arquitectura, diseño y documentación** — establece modelos, documentos y metadatos que describen estructuras y conjuntos de datos. Criterios: Arquitectura Institucional, Catálogo de datos, Modelos y Documentación, Metadatos. Herramientas de catálogo: CKAN (open source), Magda (open source, federado).

**Almacenamiento y operación** — implementación y operación de plataformas de gestión de datos. Criterios: Gestión de la operación y almacenamiento.

**Seguridad y ciberseguridad de datos** — privacidad, confidencialidad y acceso apropiado a los datos. Criterios: Seguridad, Ciberseguridad, Protección de Datos Personales, Recuperación ante desastres.

**Integración e interoperabilidad** — mecanismos para integración y transferencia de datos al interior y exterior de la organización. Criterios: Integración, Interoperabilidad.

**Documentos y contenidos** — políticas y herramientas para datos no estructurados. Criterios: Definiciones, Metadatos, Expediente Electrónico, Repositorio Documental.

**Datos maestros y de referencia** — estandarización de codificaciones y centralización de información relevante para la institución y el sector. Criterios: Datos referenciales, Datos maestros, Herramientas.

**Analítica e inteligencia de negocios** — análisis de datos (descriptivo, diagnóstico, predictivo, prescriptivo) como apoyo a la toma de decisiones. Herramientas: data mart, data lake, data warehouse. Criterios: Toma de decisiones basada en información, Información de gestión, Herramientas.

**Calidad de datos** — metodologías y herramientas para definir, controlar y mejorar la calidad de los datos. Criterios: Definición, Metodología y Herramientas.

**Datos abiertos** — procedimientos y herramientas para publicación de datos abiertos en base a la Carta Internacional de Datos Abiertos (Open Data Charter, 6 principios). Criterios: Definiciones, Publicación, Mecanismos de acceso/formato/documentación/condiciones de uso.

**Aspectos legales y normativos** — exigencias para el área jurídica en definición de políticas, procedimientos y planes de cumplimiento normativo. Criterios: Participación del área jurídica, Cumplimiento aspectos legales y normativos.

---

## 5. Modelo de madurez del MGDE

Cuatro niveles de madurez adaptables a distintos tipos de instituciones:

| Nivel | Descripción |
|-------|-------------|
| **Insuficiente** | No se cumplen los mínimos deseables. |
| **Básico** | Se cumplen los mínimos. Orientado a OAE que requieren lo básico para la gestión de datos. |
| **Medio** | Profundización en cada dimensión. Orientado a OAE que requieren mayor desarrollo. |
| **Avanzado** | Aborda a cabalidad cada dimensión. Orientado a OAE con alto nivel de desarrollo requerido. |

Un OAE puede combinar distintos niveles por dimensión según sus prioridades y capacidades.

---

## 6. Método de autoevaluación

La autoevaluación opera mediante la **Matriz de evaluación del nivel de madurez**, con preguntas de 4 respuestas posibles (insuficiente, básico, medio, avanzado), o 2 respuestas dicotómicas (Sí/No) donde la primera equivale a insuficiente y la segunda a avanzado.

**Puntajes por nivel:** 0 = Insuficiente, 2 = Básico, 4 = Medio, 6 = Avanzado.

### Cálculo del puntaje por dimensión

**Pje(D) = ∑Pje(Pi)**

Donde Pje(Pi) es el puntaje de la pregunta i.

Ejemplo: dimensión de 7 preguntas con respuestas {2, 0, 2, 4, 2, 0, 2} → Pje(D) = 12.

### Nivel de madurez por dimensión

**% Pje(D) = Pje(D) / (6 × NP(D))**

Donde NP(D) es el número de preguntas de la dimensión.

Ejemplo: 12/42 = 28,6% → nivel **Insuficiente**.

**Intervalos:**
- [0%, 40%) → Insuficiente
- [40%, 60%) → Básico
- [60%, 80%) → Medio
- [80%, 100%] → Avanzado

### Puntaje global del OAE

**Pje(OAE) = ∑Pje(Dj) × P(Dj)**

Ponderador igual para cada dimensión: 1/12 = 8,3% (modificable por el OAE según sus necesidades).

**Puntaje máximo global:** 312. Puntaje ponderado máximo: 260.

### Ejemplo de resultados de autoevaluación

| Dimensión | Puntaje | % Puntaje/Avanzado | Nivel Madurez | Ponderación |
|-----------|---------|-------------------|---------------|-------------|
| Visión estratégica | 12 | 29% | Insuficiente | 8,3% |
| Gobernanza de datos | 12 | 29% | Insuficiente | 8,3% |
| Arquitectura, diseño y documentación | 4 | 11% | Insuficiente | 8,3% |
| Almacenamiento y operación | 4 | 67% | Medio | 8,3% |
| Seguridad y ciberseguridad de datos | 4 | 11% | Insuficiente | 8,3% |
| Integración e interoperabilidad | 12 | 50% | Básico | 8,3% |
| Documentos y contenidos | 4 | 17% | Insuficiente | 8,3% |
| Datos maestros y de referencia | 10 | 56% | Básico | 8,3% |
| Analítica e inteligencia de negocios | 6 | 33% | Insuficiente | 8,3% |
| Calidad de datos | 0 | 0% | Insuficiente | 8,3% |
| Datos abiertos | 22 | 52% | Básico | 8,3% |
| Aspectos legales y normativos | 0 | 0% | Insuficiente | 8,3% |
| **Institución X (total)** | **90** (pond. 75) | **28,8%** | **Insuficiente** | — |

---

## 7. Hoja de ruta

Plan de acción para alcanzar el nivel de madurez esperado, elaborado **por dimensión** a partir del nivel actual y el nivel esperado definido por la institución.

- Se deben proponer acciones por criterio usando la matriz de evaluación.
- Se debe justificar el nivel esperado por dimensión y la priorización de prácticas.
- Combinar estrategias **top-down** (formalización de políticas directivas) y **bottom-up** (mejoras operativas por equipos).

---

## 8. Consideraciones para la implementación

- El MGDE debe ser aplicado por un equipo especializado con mix de competencias apropiadas.
- El Gobierno de Datos debe alinearse con la estrategia organizacional.
- Debe integrarse con otros marcos de trabajo: Gestión de Procesos, Calidad, TIC, Transformación Digital, Gestión Documental, Arquitectura Empresarial.
- La **gestión del cambio** debe incluirse de forma alineada con la estrategia y planes de Transformación Digital.

### Gestión del cambio

Implementar un modo distinto de hacer las cosas y producir cambios de conducta. Inicia a alto nivel mediante decisiones basadas en evidencia. Los OAE deben desplegar procesos formales de gestión del cambio según tamaño y complejidad, manteniendo un documento que describa las acciones y cómo se comunican al personal.

---

## 9. Plan de implementación del MGDE

Proceso gradual que puede requerir entre **24 y 48 meses** (en ocasiones más), con variaciones según capacidades organizacionales y liderazgo directivo.

### Etapas del plan

| Duración referencial | Etapa | Descripción |
|---------------------|-------|-------------|
| 4–8 meses | **Etapa 1:** Diagnóstico y definiciones estratégicas | Autoevaluación, definición del nivel de madurez esperado y elaboración de hoja de ruta. |
| 8–12 meses | **Etapa 2:** Implementación básica | Implementación de elementos básicos en dimensiones priorizadas (máximo 3). |
| 12–28 meses | **Etapa 3:** Implementación avanzada | Consolidación de gobernanza y cumplimiento del nivel básico en todas las dimensiones. |

### Actividades por etapa

**Etapa 1:**
- Establecimiento de visión estratégica
- Concientización de equipos directivos
- Formación de equipo(s) y capacitación inicial
- Redacción de Política de Gestión de Información
- Definiciones de gobernanza y gestión del cambio
- Autoevaluación y generación de hoja de ruta

**Etapa 2:**
- Difusión y gestión del cambio
- Implementación de gobernanza (inicial)
- Capacitación en prácticas
- Definición e implementación de prácticas priorizadas
- Productos iniciales y proyectos piloto
- Evaluación y generación de hoja de ruta para la siguiente etapa

**Etapa 3:**
- Difusión (profundizar) y gestión del cambio
- Consolidación de la gobernanza
- Implementación de mejores prácticas
- Revisión/actualización de políticas
- Productos y proyectos
- Evaluación y planes de acción para mejora continua

### Estructura organizacional

Tres esquemas posibles:

- **Equipos compartidos (descentralizado):** responsabilidades distribuidas en líneas de negocio y TIC; coordinación por comités, sin dueño único.
- **Equipo dedicado (centralizado):** unidad organizacional única responsable; involucrados reportan a un líder de gestión de datos.
- **Esquema mixto:** modelo de red con responsabilidades delimitadas mediante matriz RACI (responsable, accountable, consultado, informado).

### Instancias de trabajo

**Comité Directivo** (jefaturas de áreas funcionales vinculadas a producción y consumo de información):
- Encargado de coordinación institucional para impulso de la gestión de datos.
- Provee direccionamiento al Comité Ejecutivo.
- Aprueba estrategia, planes y presupuestos.

**Comité Ejecutivo** (jefaturas o profesionales de Planificación, Control de Gestión y TIC):
- Propone políticas y estrategias.
- Establece planes y requiere presupuesto.
- Coordina la implementación de la gestión de datos.

**Mesa(s) de trabajo** (profesionales de áreas funcionales vinculadas a producción y consumo de información):
- Ejecutan la planificación.
- Desarrollan la gobernanza y las prácticas.

### Roles para la gestión de datos

**Director/a de Datos (CDO):** responsable integral de estrategia y ejecución. Responsabilidades: estrategia organizacional de datos; estándares, políticas y procedimientos de gobernanza; alineación de requerimientos de datos con recursos TI; asesoramiento en BI, analítica y calidad de datos; supervisión del cumplimiento.

**Administrador/a o Custodio/a de datos (Data Steward):** expertos funcionales con responsabilidad por conocimiento (metadatos, reglas de negocio) y calidad de los datos. Pertenecen a las líneas de negocio.

**Analista de Datos (Data Analyst):** expertos funcionales en uso y análisis de datos. Pertenecen a las líneas de negocio.

**Arquitecto de Datos (Data Architect):** diseña planos para la gestión de datos. Responsabilidades: traducir requisitos de datos en modelos y bases de datos; garantizar exactitud y accesibilidad; definir marco de arquitectura de datos (seguridad, metadatos, datos maestros); crear procesos de gestión de datos; diseñar estrategias y modelos conceptuales.

### Ciclo de mejora continua

**Planificación:** el Comité Ejecutivo propone anualmente un Plan Anual de Gestión de Datos al Comité Directivo (objetivos, alcance, recursos). Informa avances al menos semestralmente.

**Implementación:** el Comité Ejecutivo conforma Mesas de Trabajo organizadas por temas y/o dimensiones; dan cuenta periódicamente al Comité Ejecutivo.

**Evaluación:** anualmente, evaluar el avance del plan recogiendo experiencias y oportunidades de mejora.

**Evolución:** políticas, definiciones y procesos se revisan y mejoran periódicamente adoptando metodologías, marcos y buenas prácticas nacionales e internacionales.

---

## Herramienta de autoevaluación automática MGDE

La SGD pone a disposición una herramienta en Google Workspace que:
- Permite completar un formulario en las 12 dimensiones del MGDE.
- Determina el nivel de madurez actual del OAE.
- Genera automáticamente una propuesta de hoja de ruta al seleccionar el nivel deseado.
- Almacena resultados en la SGD para control y monitoreo de avances.

**Componentes:**
1. **Formulario de ingreso:** G Forms con preguntas distribuidas en 14 secciones.
2. **Código:** Apps Script que registra respuestas y genera/envía la planilla de resultados.
3. **Reporte de resultados:** Google Sheets con (a) resultados globales y por dimensión con gráfico de radar, (b) comparación con niveles Avanzado/Medio/Básico, (c) hoja de ruta sugerida.

**Acceso:** [Completar formulario de autoevaluación](https://forms.gle/b2LRbJJcFheEGBnn9)
