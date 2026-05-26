---
_manifest:
  urn: urn:tde:kb:orientaciones-basicas-gestion-tic
  provenance:
    source: https://wikiguias.digital.gob.cl/guias/orientaciones-TIC
version: 1.0.0
status: published
tags:
- tde
- lineamientos-guias
- tic
- guias
- institucionalidad
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:tde:kb:orientaciones-basicas-gestion-tic
---

# Orientaciones Básicas para la Gestión de las TIC

**Objetivo:** orientar la implementación y el inicio del funcionamiento de nuevas instituciones públicas en materia de gestión de sistemas de información y datos.

---

## Marco institucional para el Gobierno Digital

### Institucionalidad

La **Secretaría de Gobierno Digital (SGD)**, creada por Ley N°21.658 en la Subsecretaría de Hacienda, es el órgano rector de la transformación digital de la Administración del Estado desde el 1 de marzo de 2024. Continuadora legal de la ex División de Gobierno Digital (SEGPRES).

**Funciones de la SGD:**
- Proponer al Ministro de Hacienda la Estrategia de Gobierno Digital
- Coordinar la implementación de la Estrategia de Gobierno Digital con enfoque integrado de gobierno
- Coordinar, asesorar y apoyar intersectorialmente el uso estratégico de tecnologías digitales, datos e información pública
- Desarrollar y operar plataformas y servicios compartidos (mínimo: interoperabilidad e identidad digital)

El reglamento de la SGD regulará los mecanismos de implementación de la Estrategia, el monitoreo y seguimiento de medidas, la solicitud de información necesaria y toda otra materia para el adecuado ejercicio de sus competencias.

### Ley de Transformación Digital del Estado (LTDE)

La **Ley N°21.180** obliga a los órganos del Estado (excepto empresas públicas) a interoperar y gestionar trámites electrónicos antes de **diciembre de 2027**, mediante un régimen gradual de 7 fases definido en el DFL N°1 de 2020, aplicado según la madurez digital de cada grupo institucional.

Marco reglamentario de la LTDE:
- **Decreto Supremo N°4 de 2020, SEGPRES:** regula tramitación electrónica de procedimientos administrativos (excepciones, notificaciones y estándares tecnológicos)
- **6 normas técnicas:** interoperabilidad, seguridad, documentos electrónicos, notificaciones, calidad y autenticación

---

## Desafíos TIC de las nuevas instituciones

Los principales desafíos TIC son:
- Lograr que la tecnología agregue valor a los objetivos estratégicos y facilite la entrega de servicios
- Asegurar cumplimiento de normativa y estándares técnicos
- Definir estrategia TIC alineada con objetivos institucionales
- Implementar infraestructura tecnológica adecuada (on premise o nube)
- Gestionar datos con políticas y gobernanza claras
- Contar con personal calificado y asegurar interoperabilidad con otras entidades del Estado

---

## Estrategia TIC

Definir una Estrategia TIC permite alinear la tecnología con los objetivos institucionales, planificar, evaluar servicios y aplicar indicadores para medir avances.

**Elementos esenciales de la Estrategia TIC:**

1. **Objetivos estratégicos de TIC** — objetivos de largo plazo, relación con objetivos institucionales y contribución de los proyectos
2. **Modelo de arquitectura institucional** — arquitectura de referencia; CMDB (si existe); estructura de HW, SW y redes (on premise, cloud, IaaS, PaaS, SaaS)
3. **Modelo de planificación de TIC** — cómo se identifican, priorizan y gestionan los proyectos TIC; existencia, composición y funcionamiento del Comité TIC
4. **Evaluación de los servicios de TIC** — KPIs de servicios TIC; existencia de proceso de mejora continua

---

## Estructura organizacional

### Roles clave recomendados

1. **Comité TIC** — gestiona temas TIC estratégicos por la alta dirección. En instituciones pequeñas, puede ser el Comité de Calidad, Experiencia Usuaria y Transformación Digital (conforme a Guía Metodológica del PMG de Transformación Digital)

2. **Coordinador/a de Transformación Digital (CTD)** — enlace institucional con la SGD; lidera la transformación digital. Debe ser nombrado formalmente por la máxima autoridad del servicio. Registrar junto a su subrogante en https://gobdigital.cerofilas.gob.cl/

3. **Jefatura TIC** — lidera estrategias y proyectos tecnológicos. Perfil requerido: profesional en ingeniería o informática con conocimientos en gestión de proyectos, arquitectura de información y nube

4. **Equipo responsable de TIC** — según estrategia (desarrollo externo, SaaS, on premise o cloud):
 - Infraestructura: ingenieros/as en nube, operaciones, redes, telecomunicaciones y seguridad
 - Desarrollo propio: desarrolladores, administradores de BD, diseñadores UX/UI, especialistas QA
 - Analítica: analistas, científicos e ingenieros de datos; expertos en SIG para datos georreferenciados

5. **Oficial de Seguridad de la Información y Ciberseguridad** — define políticas, gestiona riesgos, atiende incidentes y cumple regulaciones; actúa en coordinación con la Agencia Nacional de Ciberseguridad (ANCI)

6. **Encargado/a de Protección de Datos (DPO)** — garantiza cumplimiento normativo, asesora, capacita, supervisa y actúa como enlace con autoridades

7. **Otras contrapartes importantes:**
 - Abogado/a experto/a en datos personales, tecnología y transformación digital
 - Especialista en compras TIC para gestionar inversiones y compras coordinando con áreas técnicas y legales

---

## Infraestructura digital básica

**Sistemas y servicios mínimos para cubrir objetivos documentales, transaccionales y de gestión:**

1. **Infraestructura de nube** (almacenamiento, procesamiento y otros servicios) para escalabilidad, redundancia y disponibilidad. Incluir un **SIEM** (Sistema de monitoreo y alertas de seguridad)

2. **Solución de ofimática** (Google Workspace, Microsoft Office 365 u equivalente) para procesadores de texto, planillas, etc.

3. **Herramienta de gestión documental** que garantice trazabilidad de trámites. Elegir entre SaaS o soluciones públicas según urgencia, recursos y complejidad. Consultar la [Pauta de evaluación de sistemas de gestión documental y expedientes electrónicos en el Estado](https://digital.gob.cl/transformacion-digital/estandares-y-guias/pauta-de-evaluacion-de-sistemas-de-gestion-documental-y-de-expedientes-electronicos-en-el-estado/)

4. **Sistema de información para gestión transaccional de personas** (idealmente SaaS): remuneraciones, asistencias, permisos, viáticos, vacaciones

5. **Servicios normativos de la Biblioteca del Congreso Nacional** (Ley Chile) para organizar y consultar regulación sectorial: https://www.bibliotecanacionaldigital.gob.cl/bnd/612/w3-propertyvalue-761831.html

6. **Gestor colaborativo de proyectos y tareas** (recomendado): ASANA, JIRA, Redmine u otro

7. **Diseño de sitios web y servicios digitales** conforme a lineamientos SGD: [Guía de uso Instrumento de evaluación de calidad en sitios webs y servicios digitales del Estado](/guias/Guia_Web)

8. **Sistemas CRM** para cumplir exigencias del Sistema de Información y Atención Ciudadana (SIAC)

---

## Integración con plataformas transversales SGD

Integrarse con las plataformas estatales es obligatorio para cumplir normas, estandarizar procesos, asegurar validez e interoperabilidad.

### Pasos de integración

1. **Completar el CPAT** (Catálogo de Procedimientos Administrativos y Otras Tramitaciones) — herramienta oficial de identificación y caracterización de procedimientos administrativos. Consultar guía rápida CPAT para cumplir la fase de preparación

2. **Usar plataformas transversales de la SGD:**

| Plataforma | Uso |
|-----------|-----|
| **ClaveÚnica** | Habilitar plataformas y sistemas que requieran verificar identidad digital de personas usuarias |
| **FirmaGob** | Firma de documentos con firma electrónica avanzada por funcionarias/os |
| **DocDigital** | Comunicaciones oficiales con otros OAE (conecta oficinas de partes) |
| **SIMPLE** | Digitalización de procesos orientados a las personas |
| **PISEE** | Interoperabilidad de datos y documentos entre OAE (evita solicitar información que el Estado ya posee) |
| **Notificador** | Plataforma oficial de notificaciones a personas usuarias a un domicilio digital único |

Mesa de servicios SGD: https://gobdigitalcl.freshdesk.com/support/home

---

## Gestión de proyectos TIC

La SGD entrega:
- Asesoría en formulación de proyectos para el proceso EVALTIC: https://wikiguias.digital.gob.cl/guias/guias/guia_evaltic
- Guía para gestión de proyectos TIC: https://wikiguias.digital.gob.cl/es/guias/Gestion_de_proyectos_TIC

---

## Gestión de temas avanzados TIC

1. **Estrategia de datos** — definir modelo, infraestructura, tecnología, estructura organizacional, datos críticos, maestros, interoperabilidad, calidad y gestión del dato. Seguir el [marco de referencia SGD para la gestión de datos](/guias/Guía_MGDE). Para tareas de anonimización, consultar [guía introductoria de anonimización de datos](/guias/Guia_anonimizacion)

2. **Analítica de datos, big data e inteligencia de negocios** — usar el [repositorio de algoritmos públicos](https://www.algoritmospublicos.cl/repositorio) para análisis de línea base

3. **Inteligencia Artificial** — toda iniciativa debe enmarcarse en la [Política Nacional de Inteligencia Artificial](https://www.minciencia.gob.cl/areas/inteligencia-artificial/politica-nacional-de-inteligencia-artificial/) y el plan de acciones para cumplir los ejes: 1) Factores Habilitantes, 2) Desarrollo y Adopción, 3) Gobernanza y Ética

4. **Portal de datos abiertos** — publicar todos los datos que puedan ser requeridos por transparencia; reduce solicitudes bajo Ley de Transparencia y fomenta investigación académica

5. **Plan de continuidad operacional (BCP) y plan de recuperación de desastres (DRP)** — garantizan continuidad y recuperación de servicios TIC

6. **Paneles o dashboards interactivos** — con indicadores clave y visualización dinámica de información

---

## Ruta de implementación y priorización

**Criterios de priorización:**

- **Cumplimiento legal primero** — priorizar acciones que aseguren cumplimiento de la Ley N°21.180 y otras normativas obligatorias
- **Seguridad y ciberseguridad** — proteger plataformas y servicios para asegurar continuidad operacional y protección de datos
- **Riesgos operativos** — atender primero las brechas que puedan poner en riesgo la continuidad de los servicios
- **Capacidades internas** — avanzar según disponibilidad y competencias del equipo; solicitar apoyo externo cuando sea necesario
- **Flexibilidad** — adaptar la ruta según el contexto, urgencia y necesidades particulares de la institución
