---
_manifest:
  urn: urn:salud:kb:procedimiento-analisis-seguridad-sistemas-sitios
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-04'
    source: MINSAL Chile, SGSI Nivel Central. PROS-NC-009 v1.0
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- procedimiento
- analisis-seguridad
- pentesting
- vulnerabilidades
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:procedimiento-analisis-seguridad-sistemas-sitios
  salud:
    minsal_id: PROS-NC-009
    minsal_version: '1.0'
    fecha_aprobacion: '2024-02-20'
    clasificacion: Publica
    elaborador: Pablo Fabres / Jose Villa C.
relations:
  cites:
  - urn:salud:kb:instructivo-seguridad-informacion-ciberseguridad-sector-salud
---

# Procedimiento de Análisis de Seguridad para Sistemas y Sitios Web — PROS-NC-009 v1.0

Sistema de Gestión de Seguridad de la Información — MINSAL Nivel Central. Febrero 2024.

## 1. Propósito y alcance

Robustecer la seguridad y mecanismos de protección de los productos de software desarrollados para MINSAL, mitigando falencias detectadas y minimizando riesgos tecnológicos previo al paso a producción y exposición a Internet.

Aplica a todo producto de software expuesto a Internet — desarrollos propios o soluciones comerciales — para el Ministerio de Salud, Subsecretaría de Salud Pública y Subsecretaría de Redes Asistenciales.

### Controles ISO 27002:2013 abarcados

| Control | Descripción |
|---------|-------------|
| A.09.04.05 | Control de acceso al código fuente de los programas |
| A.14.01.01 | Análisis y especificación de requisitos de seguridad de la información |
| A.14.02.01 | Política de desarrollo seguro |
| A.14.02.02 | Procedimientos de control de cambios del sistema |
| A.14.02.06 | Entorno de desarrollo seguro |
| A.14.02.08 | Prueba de seguridad del sistema |
| A.14.02.09 | Prueba de aprobación del sistema |

## 2. Terminología

| Término | Definición |
|---------|------------|
| **Amenaza** | Evento o acción con potencial de comprometer la seguridad del sistema (ataque malicioso, fallo, desastre natural). |
| **Análisis de Riesgos** | Proceso de evaluar riesgos: identificación de vulnerabilidades y amenazas, determinación de probabilidad e impacto de explotación. |
| **Análisis de Vulnerabilidades** | Identificación y evaluación de debilidades en sistemas y redes explotables por amenazas. |
| **Análisis de Código Estático (SAST)** | Evaluación sin ejecución del programa sobre el código fuente para identificar vulnerabilidades, errores y prácticas inseguras. |
| **Análisis de Código Dinámico (DAST)** | Evaluación del comportamiento de una aplicación en ejecución mediante pruebas y monitoreo en tiempo real. |
| **Scanner de Seguridad** | Proceso automatizado que examina sistemas, redes o aplicaciones mediante herramientas especializadas y pruebas manuales contra vulnerabilidades conocidas y configuraciones incorrectas. |
| **Pen-Testing** | Evaluación activa de seguridad mediante simulación de ataques para identificar vulnerabilidades y evaluar medidas de seguridad existentes. |
| **Vulnerabilidad / Riesgo de Seguridad / Controles** | Debilidad explotable; probabilidad de que una amenaza explote una vulnerabilidad; y medidas implementadas para proteger activos (firewalls, cifrado, autenticación, políticas de acceso). |
| **Incidente de Seguridad** | Evento que indica violación de seguridad: acceso no autorizado, pérdida de datos o interrupción del servicio. |
| **Informe de Análisis de Vulnerabilidades** | Documento con resultados del análisis que identifica debilidades y riesgos que comprometan integridad, confidencialidad o disponibilidad, incluyendo recomendaciones de mitigación. |

## 3. Documentos aplicables

- **NCh-ISO 27001.Of2013** — Requisitos de seguridad de la información.
- **Decreto 1/2015**, Ministerio Secretaría General de la Presidencia — Norma técnica sobre sistemas y sitios web de los órganos de la administración del Estado.
- **Decreto 83/2004**, Ministerio Secretaría General de la Presidencia — Norma técnica sobre seguridad y confidencialidad de documentos electrónicos.
- **Decreto 7/2023**, Ministerio Secretaría General de la Presidencia — Norma técnica de seguridad de la información y ciberseguridad.

## 4. Roles y responsabilidades

### Encargado de Seguridad de la Información

- Velar por la aplicación del presente procedimiento.
- Asesorar en la identificación de amenazas a activos de información y vulnerabilidades que las propician.
- Informar al Comité de Seguridad de la Información sobre bajas o revocaciones de sistemas web.

### Dueños de activos de información

- Aplicar el presente procedimiento.
- Justificar formalmente cuando se requiera levantar una carta de riesgos.

### Usuarios (Jefe Proyecto TIC, Gestor TI, referentes de negocio)

- Solicitar el Análisis de Seguridad (vulnerabilidades) para productos de software expuestos a Internet.
- Entregar la información requerida por la Unidad de Seguridad de la Información y Ciberseguridad y realizar los respaldos según corresponda.
- Planificar los plazos de puesta en producción considerando los tiempos del procedimiento (análisis + emisión de informe).
- Gestionar la corrección de vulnerabilidades encontradas mediante el Plan de Remediación.
- Planificar los tiempos de solución de vulnerabilidades y etapas asociadas a Producción/Explotación.

### Unidad de Seguridad de la Información y Ciberseguridad MINSAL

- Agendar, programar y priorizar requerimientos de scanner de seguridad.
- Elaborar los Informes de Análisis de Vulnerabilidades.
- Informar vulnerabilidades encontradas por aplicativo.
- Emitir recomendaciones de mejora para cada vulnerabilidad detectada.

## 5. Procedimiento

### 5.1 Requisitos previos

El usuario debe proporcionar a través del **Formulario de Solicitud de Scanner de Seguridad** (Anexo 1, §8):

- Dirección IP donde se aloja el aplicativo.
- URL del sistema o sitio.
- Ambiente: Desarrollo / QA / Producción.
- Declaración de si contiene información sensible (Ley 19.628).
- Confirmación de respaldo del aplicativo y/o base de datos.
- Fechas tentativas para la realización del análisis.
- Credenciales de prueba de la aplicación o servidor.

### 5.2 Esquema de trabajo

```text
Usuario envía Formulario → Unidad programa análisis → Ejecución de scanner
→ Elaboración de Informe → Usuario recibe Informe
 ├─ Con vulnerabilidades: Plan de Remediación → Re-análisis → Cierre
 └─ Sin vulnerabilidades: Aprobación → Pase a producción → Cierre
```

#### Flujo operativo

1. **Solicitud**: El usuario envía correo a `mds@minsal.cl` con copia a `seguridadtic@minsal.cl`, adjuntando el Formulario de Solicitud de Scanner de Seguridad completo (Anexo 1).
2. **Validación**: Si el formulario está incompleto o incorrecto, se responde al usuario solicitando complementos y se cierra el ticket del requerimiento. Si está completo, se informa al usuario el inicio del análisis.
3. **Ejecución**: La Unidad de Seguridad de la Información y Ciberseguridad ejecuta el análisis de seguridad.
4. **Informe**: Se elabora el Informe de Análisis de Vulnerabilidades (Anexo 2, §9) con las vulnerabilidades detectadas y recomendaciones asociadas.
5. **Remediación** (si aplica): El usuario presenta un Plan de Remediación, programa fecha de re-análisis y reinicia el procedimiento.
6. **Aprobación**: Si no hay vulnerabilidades, se informa que no existen inconvenientes para el paso a producción.
7. **Cierre**: La Unidad envía el Informe al usuario y procede al cierre del requerimiento.

### 5.3 Planificación

**SLA: 48 horas hábiles** desde la recepción del requerimiento para ejecutar el análisis y elaborar el informe con vulnerabilidades identificadas y recomendaciones.

Se recomienda planificar el requerimiento en las fases iniciales del proyecto para absorber posibles ciclos de remediación sin retrasar la puesta en producción.

### 5.4 Realización del scanner de seguridad

Cada revisión consta de cuatro fases secuenciales:

| Fase | Actividad |
|------|-----------|
| 1. Recolección de información | Levantamiento de datos del activo objetivo. |
| 2. Tests | Herramientas automáticas + pruebas manuales. |
| 3. Revisión de resultados | Comprobación y validación de hallazgos de herramientas automáticas. |
| 4. Elaboración de informe | Documentación de resultados con acciones correctoras. |

#### Metodología

Basada en el estándar abierto **OWASP** (Open Web Application Security Project), incorporando:

- Búsqueda de causas de inseguridad en el software.
- Recomendación de soluciones a las amenazas descubiertas.
- Alineación con OWASP Top 10.

#### Consideraciones operativas

- Las pruebas automatizadas **pueden afectar la disponibilidad** de los servicios publicados (lentitud, reinicio, modificaciones en base de datos).
- El horario y calendario de pruebas deben acordarse y ser autorizados por el usuario.

### 5.5 Contenido del Informe de Análisis de Vulnerabilidades

El informe (plantilla en Anexo 2, §9) debe contener como mínimo:

#### Campos obligatorios

| Campo | Contenido |
|-------|-----------|
| **Descripción** | Identificación clara de activos analizados (URL, nombres de equipos, IPs). |
| **Alcance** | Aspectos revisados por activo (protocolos, puertos, vulnerabilidades conocidas). |
| **Resultados** | Vulnerabilidades encontradas, tipología, criticidad y sistemas afectados. |
| **Acciones recomendadas** | Método concreto para subsanar cada vulnerabilidad. |

#### Agrupación de resultados

Los resultados se agrupan por las siguientes categorías:

1. Número total de vulnerabilidades identificadas.
2. **Nivel de Severidad** — Clasificación según criticidad:
 - **Crítico** (CVSS 9.0–10.0): Explotación inminente, compromiso total del sistema.
 - **Alto** (CVSS 7.0–8.9): Riesgo significativo, requiere acción prioritaria.
 - **Medio** (CVSS 4.0–6.9): Riesgo moderado, requiere acción programada.
3. Vulnerabilidades de Sistemas Operativos.
4. Vulnerabilidades en Aplicaciones Propietarias y Aplicaciones Comerciales.
5. Vulnerabilidades en Autenticación y/o Control de Acceso.
6. Riesgo en el acceso a la Red (LAN).
7. Explotación de vulnerabilidades (pruebas de concepto).

### 5.6 Remediación

#### Gate de remediación

1. El usuario presenta un **Plan de Remediación** que aborde las deficiencias del Informe de Vulnerabilidades.
2. Una vez implementadas las correcciones y subsanadas las vulnerabilidades, se solicita un **nuevo análisis** siguiendo el procedimiento completo.
3. Si el re-análisis **no revela nuevas vulnerabilidades**, la Unidad de Seguridad de la Información y Ciberseguridad:
 - Aprueba el análisis mediante el Informe de Análisis de Vulnerabilidades.
 - Notifica al usuario por correo electrónico.
 - Procede al cierre del requerimiento.
4. Si el re-análisis **revela nuevas vulnerabilidades**, se reinicia el ciclo de remediación.

#### Gate de producción

La aprobación formal mediante el Informe de Análisis de Vulnerabilidades sin hallazgos es **requisito esencial** para avanzar a la fase de Producción del aplicativo.

El usuario debe ajustar la planificación del proyecto para absorber los tiempos de corrección de vulnerabilidades y las iteraciones de re-análisis necesarias.

## 6. Gobernanza documental

### Registros

- Formulario de Solicitud de Scanner de Seguridad (Anexo 1).
- Informe de Análisis de Vulnerabilidades (Anexo 2).

### Difusión

- Publicación en sistema web MINSAL: `http://www.minsal.cl/seguridad_de_la_informacion/`
- Publicación en intranet MINSAL: `http://isalud.minsal.cl/`

### Revisión y actualización

Revisión obligatoria del contenido **al menos cada 2 años** por el Comité de Seguridad de la Información, o antes si hay necesidades de cambio que requieran versionamiento.

### Control de versiones

| Versión | Fecha | Responsables | Alcance |
|---------|-------|-------------|---------|
| 1.0 | 20.02.2024 | Pablo Fabres / Jose Villa C. | Documento completo — versión inicial |

## 7. Anexo 1 — Formulario de Solicitud de Scanner de Seguridad

*Todos los campos son obligatorios.*

### Bloques A/B — Solicitante y responsable de autorización

Ambos bloques requieren los mismos campos: Nombre, Cargo, RUT, Establecimiento, Área/Departamento/Unidad, Teléfono, Email.

### Bloque C — Identificación del activo

| Campo | Valor |
|-------|-------|
| Nombre del activo | |
| Descripción de objetivos y alcance | |
| ¿Maneja datos sensibles? (Ley 19.628) | SI ☐ NO ☐ |
| ¿El activo se encuentra expuesto a Internet? | SI ☐ NO ☐ |
| ¿Será expuesto a Internet? | SI ☐ NO ☐ |
| URL(s) — enlace directo | |
| Dirección(es) IP — aplicativo y servidor | |
| Lenguaje(s) de programación | |
| Credenciales del aplicativo (prueba o lectura) | Usuario: / Clave: |
| Credenciales del servidor (prueba o lectura) | Usuario: / Clave: |

### Bloque D — Medidas de resguardo del activo

| Campo | Valor |
|-------|-------|
| ¿El activo se encuentra respaldado? | SI ☐ NO ☐ |
| ¿La base de datos se encuentra respaldada? | SI ☐ NO ☐ |
| Ambiente del activo | DESARROLLO ☐ QA ☐ PRODUCCIÓN ☐ |
| Fecha(s) solicitada(s) para el análisis | |
| Ventana horaria autorizada | |

### Bloque E — Aprobaciones

| Solicitante | Responsable de autorización |
|-------------|----------------------------|
| Nombre y firma | Nombre y firma |

### Notas

1. Los scanners a sitios web, servidores o endpoints pueden conllevar consecuencias negativas: lentitud, reinicio, modificaciones en base de datos, entre otros.
2. Si se solicita el scan sin los respaldos respectivos, la integridad de los activos es responsabilidad del solicitante.
3. El responsable de la solicitud lo es también para efectos de coordinación y toma de resguardos necesarios.

## 8. Anexo 2 — Plantilla de Informe de Análisis de Vulnerabilidades

```
INFORME DE ANÁLISIS DE VULNERABILIDADES

[Nombre del activo]
[Versión]

Departamento de Tecnologías de la Información y Comunicaciones
Unidad de Seguridad de la Información y Ciberseguridad
[Fecha]
```

### Secciones del informe

#### Descripción

Chequeos realizados sobre la plataforma y la solución del sitio/aplicativo `[nombre]` en busca de vulnerabilidades.

#### Alcances

- Revisión mediante sistemas de detección de vulnerabilidades (sin ingreso por consola).
- Revisión de vulnerabilidades a nivel servidor.
- Revisión de vulnerabilidades a nivel aplicativo.
- Nota: sin acceso al código fuente no es posible subsanar la totalidad del aplicativo.

#### Resultados

Tabla de hallazgos agrupados según severidad y categoría:

| Severidad | Ítem afectado | Descripción | Detalle | Acciones recomendadas |
|-----------|--------------|-------------|---------|----------------------|
| MEDIO / ALTO / CRÍTICO | Componente | Tipo de vulnerabilidad (ej. SQL Injection) | Descripción técnica del hallazgo | Método concreto de subsanación con URLs de referencia válidas |

#### Conclusiones

Síntesis de hallazgos y recomendación de mitigación con referencias a fuentes técnicas aplicables.

#### Aprobación

| Analista | Encargado |
|----------|-----------|
| Unidad de Ciberseguridad y Seguridad de la Información | Unidad de Ciberseguridad y Seguridad de la Información |
