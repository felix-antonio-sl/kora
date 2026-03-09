---
_manifest:
  urn: urn:gn:kb:gestion-info-geoespacial
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
    source: domains/gn/04_habilitadores/arquitectura/kb_gn_090_gestion_informacion_geoespacial_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- geoespacial
- ide
- geonodo
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/04_habilitadores/arquitectura/kb_gn_090_gestion_informacion_geoespacial_koda.yml
    source_hashes:
      domains/gn/04_habilitadores/arquitectura/kb_gn_090_gestion_informacion_geoespacial_koda.yml: 2f10bceb00446a20526d688bcf0b28453a1180763af4490b68cbe90502fb7eb0
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.81
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 15
    meat_count: 287
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/gestion__gestion-info-geoespacial.md.json
---

# Gestión de Información Geoespacial en GORE Ñuble
## Source
### Ctx Required
- staging/gn/Kb_gn_090_gestion_informacion_geoespacial.md

## Glosario Geoespacial Clave
### Proposito
Definir conceptos y siglas clave recurrentes en la gestión de información geoespacial del GORE.
### Terminos
| ID | Cpt | Def |
| --- | --- | --- |
| GN-GEO-GLOS-IDE-CHILE | IDE Chile / SNIT | Infraestructura de Datos Geoespaciales de Chile y Sistema Nacional de Información Territorial, marco de coordinación interinstitucional para información territorial pública. |
| GN-GEO-GLOS-GEONODO | Geonodo | Plataforma web geoespacial de código abierto utilizada como eje tecnológico institucional para publicación, catálogo y servicios de datos territoriales. |
| GN-GEO-GLOS-ISO-19115 | ISO 19115-1 | Norma internacional que define el esquema de metadatos para describir información geográfica y servicios. |
| GN-GEO-GLOS-ISO-19157 | ISO 19157 | Norma de calidad de datos geográficos que establece medidas, descriptores y formas de reportar calidad. |
| GN-GEO-GLOS-CSW | CSW (Catalog Service for the Web) | Estándar OGC para servicios de catálogo que permiten descubrir, consultar y cosechar metadatos entre nodos. |
| GN-GEO-GLOS-WMS | WMS/WFS/WCS | Servicios OGC para visualización de mapas (WMS), acceso a entidades vectoriales (WFS) y coberturas ráster (WCS). |
| GN-GEO-GLOS-GEOJSON | GeoJSON / GML / KML / Shapefile | Formatos estandarizados de intercambio de información geoespacial. |
| GN-GEO-GLOS-LAMPV2 | LAMPv2 | Perfil de metadatos de referencia usado junto al Perfil Chileno en la definición de campos mínimos y plantillas. |
| GN-GEO-GLOS-UN-IGIF | UN-IGIF | Marco estratégico internacional considerado como referencia para el enfoque de gobernanza y datos geoespaciales. |
| GN-GEO-GLOS-QA-QC | QA/QC | Abreviatura para aseguramiento y control de calidad aplicado a datos geoespaciales y sus metadatos. |
| GN-GEO-GLOS-METADATOS | Metadatos geoespaciales | Conjunto estructurado de descriptores de un recurso geoespacial, incluyendo identificación, calidad, distribución y responsabilidad. |
| GN-GEO-GLOS-CATALOGO-OBJETOS | Catálogo de Objetos (ISO 19110) | Catálogo que define clases, atributos, relaciones y reglas de los objetos geográficos institucionales. |

## Proposito y Alcance
### Proposito
Unificar, armonizar y operacionalizar lineamientos para la gestión de información geoespacial del GORE Ñuble.
### Contexto
- Integra recomendaciones IDE Chile, estándares ISO/TC 211 y OGC, buenas prácticas, y lineamientos de licenciamiento y ética.
- Alcance aplica a todo el ciclo de vida de datos geoespaciales producidos, gestionados o publicados por GORE Ñuble y sus unidades/contratos asociados.
### Fundamento
Usa la plataforma Geonodo como eje tecnológico.
### Objetivos
- Asegurar consistencia semántica, interoperabilidad, trazabilidad y valor público de los datos territoriales.
### Resultados
- Habilitar decisiones de política pública, planificación y gestión del riesgo.

## Marco Normativo y Gobernanza
### Sistema Nacional y Roles Clave
#### Referencias
- GN-GEO-GLOS-IDE-CHILE
#### Cpt
SNIT/IDE Chile
#### Definicion
Mecanismo de coordinación interinstitucional para la gestión de información territorial pública.
#### Contexto
- Concepto operativo actual es IDE Chile.
#### Responsables
- Secretaría Ejecutiva coordina operativamente las instancias públicas.
#### Roles Clave
| Cpt | Resp |
| --- | --- |
| Consejo de Ministros / Secretaría Ejecutiva | ['Conducción superior del Sistema (Consejo).', 'Coordinación operativa (Secretaría Ejecutiva).'] |
| Cpt | Def | Resp |
| --- | --- | --- |
| Coordinación Regional IDE | Función delegada por la autoridad regional para articular, conducir técnicamente y vincular al territorio con IDE Chile. | ['Articulación interinstitucional.', 'Conducción técnica de la IDE regional.', 'Vinculación permanente con Secretaría Ejecutiva IDE Chile.'] |
### Obligaciones Institucionales
#### Requisitos
- Publicar y mantener características de la información territorial en catálogos y portales oficiales.
- Construir información territorial conforme a normas y estándares propuestos para interoperabilidad.
- Fomentar manejo del dato en red y en línea.
- Promover acuerdos institucionales para modernización continua de la gestión de datos geoespaciales.
### Estructura Operativa GORE
#### Cpt Roles
| Cpt | Resp |
| --- | --- |
| Gobernador/a Regional | Patrocinio político y validación de la política de datos territoriales. |
| Coordinador/a Regional IDE | Liderazgo operativo, definición de hoja de ruta y vínculo con Secretaría Ejecutiva IDE Chile. |
| UGIT / Equipo SIG institucional | Operación técnica: modelado, QA/QC, publicación y soporte de Geonodo. |
| Puntos Focales Sectoriales | Dominio temático y control de calidad de contenidos y metadatos en cada área. |
| Asesoría Jurídica | Definir términos de uso, licencias y resguardo de datos sensibles. |
### Matriz RACI Clave
#### Tabla RACI
#### Encabezado
- Actividad
- R (Responsible)
- A (Accountable)
- C (Consulted)
- I (Informed)
#### Filas
| Actividad | R | A | C | I |
| --- | --- | --- | --- | --- |
| Definir política de publicación geoespacial | Coordinación Regional IDE | Gobernador/a Regional | Asesoría Jurídica, UGIT | Servicios sectoriales |
| Modelado semántico / ISO 19110 | UGIT | Coordinación Regional IDE | Puntos Focales Sectoriales | Comunicaciones |
| Metadatos ISO 19115-1 / Perfil LAMPv2 | UGIT | Coordinación Regional IDE | Puntos Focales Sectoriales | Ciudadanía |
| Licenciamiento de datos geoespaciales | Asesoría Jurídica | Coordinación Regional IDE | UGIT, Comunicaciones | Servicios sectoriales |
| Publicación de servicios OGC/API | UGIT | Coordinación Regional IDE | Equipo TI | Servicios sectoriales, Comunicaciones |

## Enfoque Estrategico UN IGIF
### Contexto
Aplicación interna de las vías estratégicas de UN-IGIF al GORE Ñuble.
### Referencias
- GN-GEO-GLOS-UN-IGIF
### Vias
| Cpt | Def |
| --- | --- |
| Gobernanza e instituciones | Roles definidos, comité interdisciplinario, manual de procesos y plataforma IDE institucional como base organizacional. |
| Política y legal | Política interna de información geoespacial que regula acceso, seguridad, apertura y estándares, con revisiones periódicas. |
| Finanzas | Plan plurianual de financiamiento, identificación de fuentes externas y criterios de costo-eficiencia y valor público. |
| Datos | Modelo semántico institucional con capas base y temáticas priorizadas, políticas de calidad y actualización. |
| Innovación | Adopción de servicios en la nube, CI/CD de datos, tableros y captura móvil para acelerar entrega de valor. |
| Estándares | Uso sistemático de normas ISO/TC 211 y OGC en todo el ciclo de vida de datos geoespaciales. |

## Estandares Perfiles y Calidad
### Metadatos
#### Referencias
- GN-GEO-GLOS-ISO-19115
- GN-GEO-GLOS-LAMPV2
- GN-GEO-GLOS-METADATOS
#### Estandares
| Def |
| --- |
| ISO 19115-1 como núcleo de metadatos. |
| ISO 19115-2 como extensión para imágenes y teledetección. |
| ISO 19139 como norma de codificación XML. |
#### Rec
- Usar Perfil LAMPv2 y/o Perfil Chileno como referencia principal.
#### Mecanismo
- Implementar CSW para catálogo y cosecha (harvesting) entre nodos de IDE.
#### Campo Minimo Metadatos
#### Cpt
- Identificación del recurso: título, resumen, tema/palabras clave, alcance/espacial.
- Calidad: linaje, precisión posicional/temporal, completitud y consistencia lógica.
- Distribución: formatos, URL de descarga/servicios, términos de uso/licencia.
- Responsabilidad: responsable, contacto, fechas de publicación/actualización y mantenimiento.
### Calidad de Datos
#### Referencias
- GN-GEO-GLOS-ISO-19157
- GN-GEO-GLOS-QA-QC
#### Fundamento
- ISO 19157 como referencia de medidas e informes de calidad.
#### Requisitos
- Registrar QA/QC en metadatos, incluyendo linaje, exactitud y consistencia.
### Especificaciones y Modelos
#### Referencias
- GN-GEO-GLOS-CATALOGO-OBJETOS
#### Cpt
- Especificaciones de productos geoespaciales (capas/series) basadas en ISO 19131.
- Catálogo de objetos geográficos basado en ISO 19110 para lograr consistencia semántica (clases, atributos, relaciones).
### Evolucion Normativa
#### Requisitos
- Monitorear normas en estudio (por ejemplo, API Tiles).
- Actualizar continuamente la arquitectura de publicación y los perfiles usados.

## Publicacion Acceso e Interoperabilidad
### Servicios y Formatos
#### Referencias
- GN-GEO-GLOS-WMS
- GN-GEO-GLOS-GEOJSON
#### Cpt Servicios
| Def |
| --- |
| WMS/WFS/WCS como servicios principales para visualización, acceso a entidades y coberturas. |
#### Cpt Formatos
| Def |
| --- |
| Uso de GeoJSON, GML, KML y Shapefile como formatos de intercambio soportados. |
### API Institucional
#### Requisitos
- Definir endpoints claros (por ejemplo, `/datasets`, `/datasets/{id}`, `/tiles/{z}/{x}/{y}`) con métodos HTTP, paginación y filtros.
- Implementar autenticación/autorización para capas restringidas.
- Gestionar versionamiento y monitoreo de la API.
- Publicar documentación interactiva (OpenAPI/Swagger) con ejemplos de solicitudes y códigos de respuesta.
### Usabilidad y Accesibilidad
#### Requisitos
- Disponer de geoportal intuitivo orientado a usuarios no expertos.
#### Mecanismo
- Búsqueda avanzada por tema, palabra clave y ubicación.
- Previsualización mediante visores basados en WMS.
- Descargas en múltiples formatos.
- Tutoriales y guías de uso para distintos perfiles de usuario.

## Plataforma Tecnologica Geonodo
### Rol de Geonodo
#### Referencias
- GN-GEO-GLOS-GEONODO
#### Definicion
Plataforma web de código abierto, modular y alineada a estándares para gestión de datos geoespaciales.
#### Proposito
Soportar el ciclo de vida completo de datos territoriales.
#### Ciclo Vida Datos
| Cpt | Def |
| --- | --- |
| Planificación | Formularios, catálogo ISO 19110 y definición de capas. |
| Producción y Almacenamiento | Capas vectoriales, rasters, recolector móvil y datos tabulares. |
| Publicación | Catálogo, servicios WMS/WFS y visores y cuadros de mando. |
| Difusión | Páginas web temáticas para comunicar datos e historias. |
#### Mecanismo
- Gestión por instancias y roles (superadmin, admin, usuario).
- Administración de servicios externos (WMS/WFS) y geocodificación.
#### Ventaja Clave
#### Definicion
Integración nativa de metadatos (LAMPv2/Perfil Chileno) y CSW para cosecha y federación de catálogos.

## Desarrollo Tecnologico Institucional
### Requisitos
- Usar estándares abiertos (OGC/ISO) en adquisición, modelado y publicación de datos.
- Usar software libre como principio para reducir costos, aumentar sostenibilidad y aprovechar comunidad.
### Cpt
| Cpt | Def |
| --- | --- |
| GitHub institucional | Repositorio para control de versiones, automatización (CI/CD de datos y metadatos) y política de contribución. |
| Soporte y mantenimiento | Plan de servicio, monitoreo y respaldo de la plataforma geoespacial. |
| Seguridad y privacidad | Clasificación de datos, segregación de ambientes, gestión de secretos, hardening y auditorías periódicas. |

## Licenciamiento y Terminos de Uso
### Cpt
| Cpt | Rec |
| --- | --- |
| Datos abiertos | ['Aplicar licencias Creative Commons (por ejemplo, CC BY 4.0) para capas abiertas.', 'Aplicar ODbL para bases de datos cuando corresponda.'] |
| Cpt | Req |
| --- | --- |
| Términos de uso | ['Definir con claridad atribución, limitaciones de responsabilidad, ausencia de garantías y restricciones sobre datos sensibles.'] |
| Cpt | Def |
| --- | --- |
| Política institucional de licenciamiento | Plantilla de licencias, revisión jurídica y trazabilidad de decisiones. |

## Etica de Datos Geoespaciales
### Cpt
| Cpt | Req |
| --- | --- |
| Privacidad y proporcionalidad | ['Minimizar datos personales y granularidad cuando no sea necesaria.', 'Aplicar anonimización cuando corresponda.'] |
| Cpt | Req |
| --- | --- |
| Consentimiento y transparencia | ['Declarar origen, finalidad, licencias y restricciones en metadatos y geoportal.'] |
| Cpt | Req |
| --- | --- |
| Equidad y no daño | ['Evaluar impactos y sesgos potenciales.', 'Evitar visualizaciones que estigmaticen comunidades.'] |
| Cpt | Def | Req |
| --- | --- | --- |
| Profesionalidad | Responsabilidad con la sociedad en la gestión de datos geoespaciales. | ['Tratar exactitud y calidad como deber público.'] |

## Modelo Operativo y Trazabilidad
### Flujo Institucional
#### Proceso
- Planificar: definir necesidades (UN-IGIF), especificaciones (ISO 19131) y catálogo de objetos (ISO 19110).
- Capturar/Integrar: usar formularios/recolectores, ETL y control de versiones.
- Calidad: realizar QA/QC (ISO 19157) y validaciones automatizadas.
- Documentar: crear metadatos (ISO 19115-1), URL de descarga/servicios y licencias.
- Publicar: usar WMS/WFS/WCS, API, geoportal y registros CSW.
- Usar y evaluar: implementar tableros, indicadores de uso/impacto y mecanismos de retroalimentación.
### Trazabilidad
#### Mecanismo
| Cpt |
| --- |
| Identificadores persistentes de capas/series. |
| Control de cambios en GitHub institucional. |
| Registro de versiones de metadatos. |

## Plan de Implementacion 180 Dias
### Fase 0 0 30 Dias
#### Acciones
- Constitución del Comité Geo institucional y designación formal de roles.
- Inventario de datos y diagnóstico de madurez (gobernanza, datos, tecnología, capacidades).
### Fase 1 30 90 Dias
#### Acciones
- Definición de política interna y guías de metadatos (plantilla ISO 19115-1/LAMPv2).
- Puesta en marcha de Geonodo (instancia, roles, seguridad básica) y catálogo CSW.
- Piloto de 5 conjuntos priorizados (capas base + temáticas) con metadatos y WMS/WFS.
### Fase 2 90 150 Dias
#### Acciones
- Publicación de geoportal y API (OpenAPI + páginas de datos).
- Integración con servicios externos (WMS/WFS) y tableros de mando.
- Adopción de política de licenciamiento y términos de uso.
### Fase 3 150 180 Dias
#### Acciones
- Evaluación de calidad y uso (KPIs).
- Capacitación continua y plan anual de actualización.
### Indicadores Minimos
#### Cpt
- Porcentaje de capas con metadatos completos.
- Porcentaje de capas con licencia explícita.
- Tiempo de actualización por tipo de dato.
- Disponibilidad de servicios.
- Consumo de API (tráfico, usuarios, aplicaciones integradas).
- Satisfacción usuaria respecto del geoportal y servicios de datos.

## Anexos Operativos
### Checklist Metadatos Nucleo
#### Cpt
Checklist de metadatos núcleo sugerido.
#### Requisitos
- Título, resumen, palabras clave, temática, fechas, responsable, contacto.
- Extensión espacial/temporal, referencia geodésica/proyección.
- Linaje, precisión, completitud, consistencia.
- Formatos, URL de servicios/descarga, licencia/uso, frecuencia de mantenimiento.
### Plantilla Licencias Terminos Uso
#### Cpt
Plantilla de licencias y términos de uso.
#### Definicion
- Uso de CC BY 4.0 (atribución requerida) y ODbL (bases de datos), con cláusulas institucionales asociadas.
### Lista Endpoints API Ejemplo
#### Cpt
Lista de endpoints API de ejemplo.
#### Ex
- `/datasets` (GET, POST)
- `/datasets/{id}` (GET, PUT, DELETE)
- `/tiles/{z}/{x}/{y}` (GET) – capa/base de teselas.
- `/search` (GET) – filtros por tema, bbox, fecha; paginación `limit/offset`.
### Plantilla Catalogo Objetos
#### Mdl
Clase → Atributos, Relaciones, Reglas.
#### Ex
- "Infraestructura_Vial" → (id_via, tipo, jerarquía, estado), (conexión, pertenece_a), (dominios de valores, obligatoriedad).
### Referencia RACI Completa
#### Contexto
Matriz RACI completa disponible en documento separado.
#### Referencias
GEO-GORE-GOBERNA-RACI-01
### Glosario Extendido
#### Cpt
Glosario extendido de términos IDE, SNIT, CSW, WMS, WFS, WCS, LAMPv2, UN-IGIF, QA/QC, Metadatos y Catálogo de Objetos.
#### Referencias
- GN-GEO-GLOS-IDE-CHILE
- GN-GEO-GLOS-CSW
- GN-GEO-GLOS-WMS
- GN-GEO-GLOS-LAMPV2
- GN-GEO-GLOS-UN-IGIF
- GN-GEO-GLOS-QA-QC
- GN-GEO-GLOS-METADATOS
- GN-GEO-GLOS-CATALOGO-OBJETOS

## Gobierno de Documento
### Responsables
| Cpt | Def |
| --- | --- |
| Propietario del documento | Coordinación Regional IDE GORE Ñuble. |
### Proceso
| Cpt | Def |
| --- | --- |
| Mantenimiento | Revisión semestral o ante cambios normativos/tecnológicos relevantes. |
| Control de cambios | Registro en repositorio institucional (GitHub/GitLab) y actualización de versión en metadatos. |
