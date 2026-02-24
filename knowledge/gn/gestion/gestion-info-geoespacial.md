---
_manifest:
  urn: "urn:gn:kb:gestion-info-geoespacial"
  provenance:
    created_by: "FS"
    created_at: "2026-01-29"
    source: "GORE Ñuble"
version: "2.0.0"
status: published
tags: [gore-nuble, gobierno-regional, geoespacial, ide, geonodo]
lang: es
---

# Gestión de Información Geoespacial en GORE Ñuble

## Glosario Geoespacial Clave

| Concepto | Descripción |
| :--- | :--- |
| **IDE Chile / SNIT** | Infraestructura de Datos Geoespaciales y Sistema Nacional de Información Territorial; coordinación interinstitucional. |
| **Geonodo** | Plataforma web open source; eje tecnológico para publicación, catálogo y servicios territoriales. |
| **ISO 19115-1** | Norma internacional para esquema de metadatos geográficos y servicios. |
| **ISO 19157** | Norma de calidad de datos geográficos (medidas, descriptores y reportes). |
| **CSW** | Catalog Service for the Web; estándar OGC para descubrimiento y cosecha de metadatos. |
| **WMS/WFS/WCS** | Servicios OGC: Visualización (WMS), Entidades vectoriales (WFS), Coberturas ráster (WCS). |
| **GeoJSON / GML / KML** | Formatos estandarizados de intercambio de información geoespacial. |
| **LAMPv2** | Perfil de metadatos de referencia (campos mínimos y plantillas). |
| **UN-IGIF** | Marco estratégico internacional para gobernanza y datos geoespaciales. |
| **QA/QC** | Aseguramiento y Control de Calidad aplicado a datos y metadatos. |
| **Metadatos** | Descriptores estructurados (identificación, calidad, distribución, responsabilidad). |
| **ISO 19110** | Catálogo de objetos: clases, atributos, relaciones y reglas. |

## Propósito y Alcance

- **Propósito:** Unificar y operacionalizar lineamientos geoespaciales en GORE Ñuble.
- **Integración:** Recomendaciones IDE Chile, estándares ISO/TC 211, OGC y lineamientos éticos.
- **Alcance:** Todo el ciclo de vida de datos producidos, gestionados o publicados por GORE Ñuble y contratistas.
- **Eje Tecnológico:** Plataforma Geonodo.
- **Objetivo:** Asegurar interoperabilidad, trazabilidad y valor público de datos territoriales.
- **Resultado:** Soporte a decisiones de política pública, planificación y gestión de riesgo.

## Marco Normativo y Gobernanza

### Sistema Nacional y Roles
- **Coordinación:** SNIT/IDE Chile coordina gestión de información territorial pública.
- **Secretaría Ejecutiva:** Coordinación operativa nacional.
- **Consejo de Ministros:** Conducción superior del sistema.
- **Coordinación Regional IDE:** Articulación interinstitucional, conducción técnica regional y vínculo con nivel central.

### Obligaciones Institucionales
- Publicar características de información territorial en catálogos oficiales.
- Cumplir normas y estándares de interoperabilidad.
- Fomentar manejo de datos en red y en línea.
- Promover acuerdos para modernización de gestión de datos.

### Estructura Operativa GORE
- **Gobernador/a:** Patrocinio político y validación de política de datos.
- **Coordinador/a Regional IDE:** Liderazgo operativo y hoja de ruta.
- **UGIT / Equipo SIG:** Operación técnica, QA/QC, soporte Geonodo.
- **Puntos Focales Sectoriales:** Dominio temático y control de calidad de contenidos.
- **Asesoría Jurídica:** Términos de uso, licencias y resguardo de datos sensibles.

### Matriz RACI de Actividades Críticas

| Actividad | R (Responsable) | A (Accountable) | C (Consultado) | I (Informado) |
| :--- | :--- | :--- | :--- | :--- |
| Política de publicación | Coord. Regional IDE | Gobernador/a | Jurídica, UGIT | Sectores |
| Modelado semántico | UGIT | Coord. Regional IDE | Puntos Focales | Comunicaciones |
| Metadatos (LAMPv2) | UGIT | Coord. Regional IDE | Puntos Focales | Ciudadanía |
| Licenciamiento | Jurídica | Coord. Regional IDE | UGIT, Comunicaciones | Sectores |
| Servicios OGC/API | UGIT | Coord. Regional IDE | Equipo TI | Sectores |

## Enfoque Estratégico UN-IGIF

| Vía Estratégica | Aplicación GORE Ñuble |
| :--- | :--- |
| **Gobernanza** | Roles definidos, comité interdisciplinario, manual de procesos e IDE institucional. |
| **Política y Legal** | Regulación de acceso, seguridad, apertura y estándares; revisiones periódicas. |
| **Finanzas** | Plan plurianual, fuentes externas, criterios de costo-eficiencia y valor público. |
| **Datos** | Modelo semántico institucional, capas priorizadas, políticas de calidad. |
| **Innovación** | Cloud services, CI/CD de datos, tableros y captura móvil. |
| **Estándares** | Uso sistemático de normas ISO/TC 211 y OGC en ciclo de vida del dato. |

## Estándares, Perfiles y Calidad

### Gestión de Metadatos
- **Núcleo:** ISO 19115-1.
- **Imágenes/Teledetección:** ISO 19115-2.
- **Codificación XML:** ISO 19139.
- **Perfiles de Referencia:** LAMPv2 y Perfil Chileno.
- **Cosecha:** Implementación de CSW para federación entre nodos IDE.

### Campos Mínimos de Metadatos
- **Identificación:** Título, resumen, temas, palabras clave, alcance espacial.
- **Calidad:** Linaje, precisión (posicional/temporal), completitud, consistencia.
- **Distribución:** Formatos, URL descarga/servicios, licencias.
- **Responsabilidad:** Contacto, fechas de publicación y mantenimiento.

### Calidad y Modelado
- **Referencia Calidad:** ISO 19157 (medidas e informes registrados en metadatos).
- **Especificaciones:** ISO 19131 para productos geoespaciales.
- **Semántica:** ISO 19110 para catálogo de objetos (clases, atributos, relaciones).

## Publicación, Acceso e Interoperabilidad

### Servicios y Formatos
- **Servicios:** WMS, WFS y WCS para visualización y acceso a datos.
- **Intercambio:** GeoJSON, GML, KML y Shapefile.

### API Institucional
- **Endpoints:** `/datasets`, `/datasets/{id}`, `/tiles/{z}/{x}/{y}`.
- **Funcionalidad:** Métodos HTTP, paginación, filtros y autenticación para capas restringidas.
- **Documentación:** OpenAPI/Swagger interactivo.

### Usabilidad
- Geoportal intuitivo para usuarios no expertos.
- Búsqueda avanzada por tema y ubicación.
- Previsualización mediante visores WMS.
- Tutoriales y guías de uso diferenciadas por perfil.

## Plataforma Tecnológica Geonodo

- **Naturaleza:** Software libre, modular y alineado a estándares OGC/ISO.
- **Función:** Soporte integral al ciclo de vida del dato territorial.
- **Ciclo en Geonodo:**
    1. **Planificación:** Formularios y catálogo ISO 19110.
    2. **Producción:** Capas vectoriales, rasters, captura móvil.
    3. **Publicación:** Servicios WMS/WFS, visores y dashboards.
    4. **Difusión:** Páginas temáticas e historias con datos.
- **Administración:** Gestión por roles (superadmin, admin, usuario) y servicios externos.
- **Ventaja:** Integración nativa de metadatos (LAMPv2) y federación vía CSW.

## Desarrollo y Seguridad Institucional

- **Estándares:** Uso de OGC/ISO en adquisición y modelado.
- **Software Libre:** Principio de reducción de costos y sostenibilidad.
- **GitHub Institucional:** Control de versiones, CI/CD de datos y metadatos.
- **Mantenimiento:** Plan de servicio, monitoreo y respaldo.
- **Seguridad:** Clasificación de datos, hardening, gestión de secretos y auditorías.

## Licenciamiento y Ética

### Licencias y Términos
- **Datos Abiertos:** Creative Commons (CC BY 4.0) para capas; ODbL para bases de datos.
- **Términos:** Definición de atribución, límites de responsabilidad y restricciones sensibles.
- **Trazabilidad:** Plantilla de licencias con revisión jurídica.

### Ética de Datos
- **Privacidad:** Minimización y anonimización de datos personales.
- **Transparencia:** Declaración de origen, finalidad y restricciones en metadatos.
- **Equidad:** Evaluación de sesgos; evitar visualizaciones estigmatizantes.
- **Profesionalismo:** Exactitud y calidad como deber público.

## Modelo Operativo y Trazabilidad

### Flujo Institucional
1. **Planificar:** Definir necesidades (UN-IGIF) y especificaciones (ISO 19131/19110).
2. **Capturar:** Formularios, ETL y control de versiones.
3. **Calidad:** QA/QC (ISO 19157) y validaciones automatizadas.
4. **Documentar:** Metadatos (ISO 19115-1) y licencias.
5. **Publicar:** Servicios OGC, API y registros CSW.
6. **Evaluar:** Tableros de impacto y feedback.

### Trazabilidad
- Identificadores persistentes de capas.
- Control de cambios en GitHub.
- Historial de versiones de metadatos.

## Plan de Implementación (180 Días)

| Fase | Duración | Acciones Clave |
| :--- | :--- | :--- |
| **0: Preparación** | 0-30 días | Constitución Comité Geo, designación de roles, diagnóstico madurez. |
| **1: Cimiento** | 30-90 días | Política metadatos (LAMPv2), Geonodo base, piloto 5 capas críticas. |
| **2: Expansión** | 90-150 días | Lanzamiento Geoportal y API, integración servicios externos, política licencias. |
| **3: Consolidación** | 150-180 días | Evaluación KPI, capacitación continua, plan anual actualización. |

### Indicadores de Desempeño (KPI)
- % capas con metadatos completos.
- % capas con licencia explícita.
- Tiempo de actualización por tipo de dato.
- Disponibilidad de servicios y tráfico API.
- Satisfacción usuaria del geoportal.

## Anexos Operativos

- **Checklist Metadatos:** Título, resumen, palabras clave, fechas, responsable, contacto, extensión (espacial/temporal), linaje, precisión, URL servicios, licencia.
- **Endpoints API Ejemplo:**
    - `GET /datasets` (listado).
    - `GET /datasets/{id}` (detalle).
    - `GET /tiles/{z}/{x}/{y}` (teselas).
    - `GET /search?q=...` (filtros bbox, tema, fecha).
- **Modelo Catálogo Objetos:** Clase (ej. Infraestructura Vial) → Atributos (id, tipo, jerarquía) → Relaciones (pertenece_a) → Reglas (dominios).

## Gobierno del Documento

- **Propietario:** Coordinación Regional IDE GORE Ñuble.
- **Mantenimiento:** Revisión semestral o ante cambios normativos/tecnológicos.
- **Control de Cambios:** Registro en GitHub institucional; actualización de versión en metadatos.
