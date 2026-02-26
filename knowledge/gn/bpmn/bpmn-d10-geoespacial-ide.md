---
_manifest:
  urn: urn:gn:kb:bpmn-d10-geoespacial-ide
  provenance:
    created_by: FS
    created_at: '2026-01-29'
    source: "GORE Ñuble"
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- geoespacial
- ide
- bpmn
- gn
lang: es
---

# BPMN D10: Gestión de Información Geoespacial (IDE/Geonodo)

## Metadatos del Dominio

| Atributo | Valor |
| :--- | :--- |
| ID | DOM-GEO |
| Criticidad | Media |
| Dueño | Coordinador Regional IDE |
| Procesos | 3 (Ciclo de Vida, Publicación, Gobernanza) |
| Subprocesos | ~10 |

## Marco Estratégico

| Aspecto | Alineamiento |
| :--- | :--- |
| ERD Ñuble | Gestión territorial informada |
| IDE Chile | Interoperabilidad nacional |
| ISO/TC 211 | Estándares geoespaciales |
| OGC | Servicios web abiertos |

## P1: Ciclo de Vida de Datos Geoespaciales

**Fases:** 6. Ciclo con mejora continua: evaluación retroalimenta planificación.

### Fases y Responsables

| Fase | Actividades | Responsable |
| :--- | :--- | :--- |
| 1. Planificar | Definir necesidades (UN-IGIF), especificaciones (ISO 19131), catálogo objetos (ISO 19110) | Coord. Regional IDE |
| 2. Capturar/Integrar | Formularios/recolectores, ETL desde fuentes, control de versiones | UGIT / Equipo SIG |
| 3. Calidad | QA/QC (ISO 19157), validaciones automatizadas | UGIT / Equipo SIG |
| 4. Documentar | Metadatos (ISO 19115-1), URL descarga/servicios, licencias | UGIT / Equipo SIG |
| 5. Publicar | WMS/WFS/WCS, API endpoints, Geoportal, Registro CSW | UGIT / Equipo SIG |
| 6. Usar y Evaluar | Tableros/dashboards, indicadores uso/impacto, retroalimentación | Divisiones usuarias |

## P2: Publicación e Interoperabilidad

### Servicios OGC

| Servicio | Tipo de datos |
| :--- | :--- |
| WMS | Visualización de capas |
| WFS | Entidades vectoriales |
| WCS | Coberturas raster |

Formatos de exportación desde WFS: GeoJSON, GML, KML, Shapefile.

### API Institucional REST

| Endpoint | Función |
| :--- | :--- |
| /datasets | Listar conjuntos de datos |
| /datasets/{id} | Detalle del conjunto |
| /tiles/{z}/{x}/{y} | Teselas |
| /search | Búsqueda avanzada |

Respuesta: JSON.

### Geoportal

| Funcionalidad | Descripción |
| :--- | :--- |
| Búsqueda | Por tema, palabra clave, ubicación |
| Previsualización | Visor WMS integrado |
| Descarga | Múltiples formatos |
| Tutoriales | Guías por perfil de usuario |

## P3: Gobernanza de Datos Geoespaciales

### Roles de Gobernanza

| Rol | Nivel | Función |
| :--- | :--- | :--- |
| Gobernador/a | Estratégico | Patrocinio del Comité Geo Institucional |
| Coord. Regional IDE | Operativo | Liderazgo técnico |
| UGIT / Equipo SIG | Operativo | Operación técnica |
| Puntos Focales Sectoriales | Operativo | Representación por división |
| Jurídica | Soporte | Licencias |
| TI | Soporte | Infraestructura |
| Comunicaciones | Soporte | Difusión |

### Trazabilidad y Versionamiento

1. Cambio en capa → commit en GitHub institucional
2. Actualizar versión en metadatos
3. Notificar a consumidores

### Licenciamiento

| Tipo de Capa | Licencia recomendada |
| :--- | :--- |
| Datos abiertos | CC BY 4.0 |
| Bases de datos | ODbL |
| Datos restringidos | Acuerdo específico |

## Ética de Datos Geoespaciales

| Principio | Aplicación |
| :--- | :--- |
| Minimización | Evitar granularidad innecesaria |
| Anonimización | Cuando corresponda |
| Transparencia | Declarar origen y licencias |
| No estigmatización | Evitar visualizaciones dañinas |
| Calidad | Tratarla como deber público |

## Plan de Implementación (180 días)

| Fase | Período | Hitos |
| :--- | :--- | :--- |
| Fase 0 (0–30 días) | Enero 2025 | Comité Geo constituido; inventario y diagnóstico |
| Fase 1 (30–90 días) | Febrero–Marzo 2025 | Política y guía metadatos; Geonodo operativo; piloto 5 conjuntos |
| Fase 2 (90–150 días) | Abril 2025 | Geoportal y API; integración servicios externos |
| Fase 3 (150–180 días) | Mayo 2025 | Evaluación KPIs; capacitación y plan anual |

## Sistemas Involucrados

| Sistema | Función |
| :--- | :--- |
| SYS-GEONODO | Plataforma geoespacial |
| SYS-CSW | Catálogo de metadatos |
| SYS-OGC-SERVICES | WMS/WFS/WCS |
| SYS-GEO-PORTAL | Portal público |
| SYS-GEO-API | API REST |
| SYS-GITHUB-INSTITUCIONAL | Versionamiento de capas |

## Normativa Aplicable

| Norma | Alcance |
| :--- | :--- |
| ISO 19115-1 | Metadatos geoespaciales |
| ISO 19157 | Calidad de datos |
| ISO 19131 | Especificaciones de productos |
| Política IDE Chile | Interoperabilidad nacional |
| Ley 21.455 | Cambio climático (datos territoriales) |

## Referencias Cruzadas

| Dominio | Vínculo |
| :--- | :--- |
| D03 Gestión IPR | Georreferenciación de proyectos |
| D09 CIES/SITIA | Ubicación de cámaras |
