---
_manifest:
  urn: urn:gn:kb:gestion-info-geoespacial
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
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
    cr: 1.13
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 28
    meat_count: 316
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/gestion__gestion-info-geoespacial.md.json
---

# Gestión de Información Geoespacial en GORE Ñuble
## ID
GN-GEO-GESTION-INFORMACION-01

## Version
1.0.0

## Status
Draft

## Format
KODA/Spec

## Human Creator
FS

## Human Editor
FS

## Model Collaborator
Cascade

## AI Remediator
KODA-TRANSFORMER

## Creation Date
2025-11-27

## Modification Date
2025-11-27

## Ctx
Marco integrado de gestión de información geoespacial para el GORE Ñuble, alineado a IDE Chile, ISO/TC 211 y OGC, con Geonodo como eje.

## Source
### Primary Source
Kb_gn_090_gestion_informacion_geoespacial.md
### Ctx Required
- staging/gn/Kb_gn_090_gestion_informacion_geoespacial.md

## LLM Parsing Instructions
### ID
KODA-LLM-PARSER-GN-GEO-INFO-01
### Req
Mandatory block following Metadata.
### Prohib
Using for artifact creation or translation.
### Content
BEGIN_LLM_INSTRUCTIONS
You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).

LEXICON (expand before processing):
  Act->Action, Cause->Cause, Cond->Condition, Cpt->Concept, Ctx->Context,
  Def->Definition, Dep->Dependency, Dest->Destination, Dln->Deadline,
  Ex->Example, Fnd->Foundation, ID->ID, Instr->Instruction,
  Just->Justification, Mech->Mechanism, Mssn->Mission, Mdl->Model,
  Nat->Nature, Obj->Objective, Proc->Process, Prohib->Prohibition,
  Purp->Purpose, Ref->Reference, Req->Requirement, Res->Result,
  Resp->Responsible, Src->Source, Warn->Warning.

REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. External documents and legal sources are mentioned as contextual information under Ctx:, Ctx_Required:, Ctx_Optional: or Src:.

LANGUAGE POLICY: Keywords in English (and abbreviated forms as listed), content in original language (Spanish). Never translate content.
END_LLM_INSTRUCTIONS


## Glosario Geoespacial Clave
### ID
GN-GEO-GLOSARIO-01
### Purp
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
### ID
GEO-GORE-PROPOSITO-01
### Purp
Unificar, armonizar y operacionalizar lineamientos para la gestión de información geoespacial del GORE Ñuble.
### Ctx
- Integra recomendaciones IDE Chile, estándares ISO/TC 211 y OGC, buenas prácticas, y lineamientos de licenciamiento y ética.
- Alcance aplica a todo el ciclo de vida de datos geoespaciales producidos, gestionados o publicados por GORE Ñuble y sus unidades/contratos asociados.
### Fnd
Usa la plataforma Geonodo como eje tecnológico.
### Obj
- Asegurar consistencia semántica, interoperabilidad, trazabilidad y valor público de los datos territoriales.
### Res
- Habilitar decisiones de política pública, planificación y gestión del riesgo.

## Marco Normativo y Gobernanza
### ID
GEO-GORE-GOBERNA-01
### Sistema Nacional y Roles Clave
#### ID
GEO-GORE-GOBERNA-SISTEMA-01
#### Ref
- GN-GEO-GLOS-IDE-CHILE
#### Cpt
SNIT/IDE Chile
#### Def
Mecanismo de coordinación interinstitucional para la gestión de información territorial pública.
#### Ctx
- Concepto operativo actual es IDE Chile.
#### Resp
- Secretaría Ejecutiva coordina operativamente las instancias públicas.
#### Roles Clave
-
  #### Cpt
  Consejo de Ministros / Secretaría Ejecutiva
  #### Resp
  - Conducción superior del Sistema (Consejo).
  - Coordinación operativa (Secretaría Ejecutiva).
-
  #### Cpt
  Coordinación Regional IDE
  #### Def
  Función delegada por la autoridad regional para articular, conducir técnicamente y vincular al territorio con IDE Chile.
  #### Resp
  - Articulación interinstitucional.
  - Conducción técnica de la IDE regional.
  - Vinculación permanente con Secretaría Ejecutiva IDE Chile.
### Obligaciones Institucionales
#### ID
GEO-GORE-GOBERNA-OBLIGA-01
#### Req
- Publicar y mantener características de la información territorial en catálogos y portales oficiales.
- Construir información territorial conforme a normas y estándares propuestos para interoperabilidad.
- Fomentar manejo del dato en red y en línea.
- Promover acuerdos institucionales para modernización continua de la gestión de datos geoespaciales.
### Estructura Operativa GORE
#### ID
GEO-GORE-GOBERNA-ESTRUCTURA-01
#### Cpt Roles
| Cpt | Resp |
| --- | --- |
| Gobernador/a Regional | Patrocinio político y validación de la política de datos territoriales. |
| Coordinador/a Regional IDE | Liderazgo operativo, definición de hoja de ruta y vínculo con Secretaría Ejecutiva IDE Chile. |
| UGIT / Equipo SIG institucional | Operación técnica: modelado, QA/QC, publicación y soporte de Geonodo. |
| Puntos Focales Sectoriales | Dominio temático y control de calidad de contenidos y metadatos en cada área. |
| Asesoría Jurídica | Definir términos de uso, licencias y resguardo de datos sensibles. |
### Matriz RACI Clave
#### ID
GEO-GORE-GOBERNA-RACI-01
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
### ID
GEO-GORE-ESTRATEGIA-01
### Ctx
Aplicación interna de las vías estratégicas de UN-IGIF al GORE Ñuble.
### Ref
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
### ID
GEO-GORE-ESTANDARES-01
### Metadatos
#### ID
GEO-GORE-ESTANDARES-METADATOS-01
#### Ref
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
#### Mech
- Implementar CSW para catálogo y cosecha (harvesting) entre nodos de IDE.
#### Campo Minimo Metadatos
#### ID
GEO-GORE-ESTANDARES-METADATOS-MINIMOS-01
#### Cpt
- Identificación del recurso: título, resumen, tema/palabras clave, alcance/espacial.
- Calidad: linaje, precisión posicional/temporal, completitud y consistencia lógica.
- Distribución: formatos, URL de descarga/servicios, términos de uso/licencia.
- Responsabilidad: responsable, contacto, fechas de publicación/actualización y mantenimiento.
### Calidad de Datos
#### ID
GEO-GORE-ESTANDARES-CALIDAD-01
#### Ref
- GN-GEO-GLOS-ISO-19157
- GN-GEO-GLOS-QA-QC
#### Fnd
- ISO 19157 como referencia de medidas e informes de calidad.
#### Req
- Registrar QA/QC en metadatos, incluyendo linaje, exactitud y consistencia.
### Especificaciones y Modelos
#### ID
GEO-GORE-ESTANDARES-MODELOS-01
#### Ref
- GN-GEO-GLOS-CATALOGO-OBJETOS
#### Cpt
- Especificaciones de productos geoespaciales (capas/series) basadas en ISO 19131.
- Catálogo de objetos geográficos basado en ISO 19110 para lograr consistencia semántica (clases, atributos, relaciones).
### Evolucion Normativa
#### ID
GEO-GORE-ESTANDARES-EVOLUCION-01
#### Req
- Monitorear normas en estudio (por ejemplo, API Tiles).
- Actualizar continuamente la arquitectura de publicación y los perfiles usados.

## Publicacion Acceso e Interoperabilidad
### ID
GEO-GORE-PUBLICACION-01
### Servicios y Formatos
#### ID
GEO-GORE-PUBLICACION-SERVICIOS-01
#### Ref
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
#### ID
GEO-GORE-PUBLICACION-API-01
#### Req
- Definir endpoints claros (por ejemplo, `/datasets`, `/datasets/{id}`, `/tiles/{z}/{x}/{y}`) con métodos HTTP, paginación y filtros.
- Implementar autenticación/autorización para capas restringidas.
- Gestionar versionamiento y monitoreo de la API.
- Publicar documentación interactiva (OpenAPI/Swagger) con ejemplos de solicitudes y códigos de respuesta.
### Usabilidad y Accesibilidad
#### ID
GEO-GORE-PUBLICACION-USABILIDAD-01
#### Req
- Disponer de geoportal intuitivo orientado a usuarios no expertos.
#### Mech
- Búsqueda avanzada por tema, palabra clave y ubicación.
- Previsualización mediante visores basados en WMS.
- Descargas en múltiples formatos.
- Tutoriales y guías de uso para distintos perfiles de usuario.

## Plataforma Tecnologica Geonodo
### ID
GEO-GORE-PLATAFORMA-01
### Rol de Geonodo
#### ID
GEO-GORE-PLATAFORMA-ROL-01
#### Ref
- GN-GEO-GLOS-GEONODO
#### Def
Plataforma web de código abierto, modular y alineada a estándares para gestión de datos geoespaciales.
#### Purp
Soportar el ciclo de vida completo de datos territoriales.
#### Ciclo Vida Datos
| Cpt | Def |
| --- | --- |
| Planificación | Formularios, catálogo ISO 19110 y definición de capas. |
| Producción y Almacenamiento | Capas vectoriales, rasters, recolector móvil y datos tabulares. |
| Publicación | Catálogo, servicios WMS/WFS y visores y cuadros de mando. |
| Difusión | Páginas web temáticas para comunicar datos e historias. |
#### Mech
- Gestión por instancias y roles (superadmin, admin, usuario).
- Administración de servicios externos (WMS/WFS) y geocodificación.
#### Ventaja Clave
#### ID
GEO-GORE-PLATAFORMA-VENTAJA-01
#### Def
Integración nativa de metadatos (LAMPv2/Perfil Chileno) y CSW para cosecha y federación de catálogos.

## Desarrollo Tecnologico Institucional
### ID
GEO-GORE-DESARROLLO-01
### Req
- Usar estándares abiertos (OGC/ISO) en adquisición, modelado y publicación de datos.
- Usar software libre como principio para reducir costos, aumentar sostenibilidad y aprovechar comunidad.
### Cpt
| Cpt | Def |
| --- | --- |
| GitHub institucional | Repositorio para control de versiones, automatización (CI/CD de datos y metadatos) y política de contribución. |
| Soporte y mantenimiento | Plan de servicio, monitoreo y respaldo de la plataforma geoespacial. |
| Seguridad y privacidad | Clasificación de datos, segregación de ambientes, gestión de secretos, hardening y auditorías periódicas. |

## Licenciamiento y Terminos de Uso
### ID
GEO-GORE-LICENCIAS-01
### Cpt
-
  #### Cpt
  Datos abiertos
  #### Rec
  - Aplicar licencias Creative Commons (por ejemplo, CC BY 4.0) para capas abiertas.
  - Aplicar ODbL para bases de datos cuando corresponda.
-
  #### Cpt
  Términos de uso
  #### Req
  - Definir con claridad atribución, limitaciones de responsabilidad, ausencia de garantías y restricciones sobre datos sensibles.
-
  #### Cpt
  Política institucional de licenciamiento
  #### Def
  Plantilla de licencias, revisión jurídica y trazabilidad de decisiones.

## Etica de Datos Geoespaciales
### ID
GEO-GORE-ETICA-01
### Cpt
-
  #### Cpt
  Privacidad y proporcionalidad
  #### Req
  - Minimizar datos personales y granularidad cuando no sea necesaria.
  - Aplicar anonimización cuando corresponda.
-
  #### Cpt
  Consentimiento y transparencia
  #### Req
  - Declarar origen, finalidad, licencias y restricciones en metadatos y geoportal.
-
  #### Cpt
  Equidad y no daño
  #### Req
  - Evaluar impactos y sesgos potenciales.
  - Evitar visualizaciones que estigmaticen comunidades.
-
  #### Cpt
  Profesionalidad
  #### Def
  Responsabilidad con la sociedad en la gestión de datos geoespaciales.
  #### Req
  - Tratar exactitud y calidad como deber público.

## Modelo Operativo y Trazabilidad
### ID
GEO-GORE-OPERATIVO-01
### Flujo Institucional
#### ID
GEO-GORE-OPERATIVO-FLUJO-01
#### Proc
- Planificar: definir necesidades (UN-IGIF), especificaciones (ISO 19131) y catálogo de objetos (ISO 19110).
- Capturar/Integrar: usar formularios/recolectores, ETL y control de versiones.
- Calidad: realizar QA/QC (ISO 19157) y validaciones automatizadas.
- Documentar: crear metadatos (ISO 19115-1), URL de descarga/servicios y licencias.
- Publicar: usar WMS/WFS/WCS, API, geoportal y registros CSW.
- Usar y evaluar: implementar tableros, indicadores de uso/impacto y mecanismos de retroalimentación.
### Trazabilidad
#### ID
GEO-GORE-OPERATIVO-TRAZABILIDAD-01
#### Mech
| Cpt |
| --- |
| Identificadores persistentes de capas/series. |
| Control de cambios en GitHub institucional. |
| Registro de versiones de metadatos. |

## Plan de Implementacion 180 Dias
### ID
GEO-GORE-IMPLEMENTACION-01
### Fase 0 0 30 Dias
#### ID
GEO-GORE-IMPLEMENTACION-FASE0-01
#### Act
- Constitución del Comité Geo institucional y designación formal de roles.
- Inventario de datos y diagnóstico de madurez (gobernanza, datos, tecnología, capacidades).
### Fase 1 30 90 Dias
#### ID
GEO-GORE-IMPLEMENTACION-FASE1-01
#### Act
- Definición de política interna y guías de metadatos (plantilla ISO 19115-1/LAMPv2).
- Puesta en marcha de Geonodo (instancia, roles, seguridad básica) y catálogo CSW.
- Piloto de 5 conjuntos priorizados (capas base + temáticas) con metadatos y WMS/WFS.
### Fase 2 90 150 Dias
#### ID
GEO-GORE-IMPLEMENTACION-FASE2-01
#### Act
- Publicación de geoportal y API (OpenAPI + páginas de datos).
- Integración con servicios externos (WMS/WFS) y tableros de mando.
- Adopción de política de licenciamiento y términos de uso.
### Fase 3 150 180 Dias
#### ID
GEO-GORE-IMPLEMENTACION-FASE3-01
#### Act
- Evaluación de calidad y uso (KPIs).
- Capacitación continua y plan anual de actualización.
### Indicadores Minimos
#### ID
GEO-GORE-IMPLEMENTACION-KPIS-01
#### Cpt
- Porcentaje de capas con metadatos completos.
- Porcentaje de capas con licencia explícita.
- Tiempo de actualización por tipo de dato.
- Disponibilidad de servicios.
- Consumo de API (tráfico, usuarios, aplicaciones integradas).
- Satisfacción usuaria respecto del geoportal y servicios de datos.

## Anexos Operativos
### ID
GEO-GORE-ANEXOS-01
### Checklist Metadatos Nucleo
#### ID
GEO-GORE-ANEXOS-CHECKLIST-01
#### Cpt
Checklist de metadatos núcleo sugerido.
#### Req
- Título, resumen, palabras clave, temática, fechas, responsable, contacto.
- Extensión espacial/temporal, referencia geodésica/proyección.
- Linaje, precisión, completitud, consistencia.
- Formatos, URL de servicios/descarga, licencia/uso, frecuencia de mantenimiento.
### Plantilla Licencias Terminos Uso
#### ID
GEO-GORE-ANEXOS-LICENCIAS-01
#### Cpt
Plantilla de licencias y términos de uso.
#### Def
- Uso de CC BY 4.0 (atribución requerida) y ODbL (bases de datos), con cláusulas institucionales asociadas.
### Lista Endpoints API Ejemplo
#### ID
GEO-GORE-ANEXOS-API-01
#### Cpt
Lista de endpoints API de ejemplo.
#### Ex
- `/datasets` (GET, POST)
- `/datasets/{id}` (GET, PUT, DELETE)
- `/tiles/{z}/{x}/{y}` (GET) – capa/base de teselas.
- `/search` (GET) – filtros por tema, bbox, fecha; paginación `limit/offset`.
### Plantilla Catalogo Objetos
#### ID
GEO-GORE-ANEXOS-CATALOGO-01
#### Mdl
Clase → Atributos, Relaciones, Reglas.
#### Ex
- "Infraestructura_Vial" → (id_via, tipo, jerarquía, estado), (conexión, pertenece_a), (dominios de valores, obligatoriedad).
### Referencia RACI Completa
#### ID
GEO-GORE-ANEXOS-RACI-01
#### Ctx
Matriz RACI completa disponible en documento separado.
#### Ref
GEO-GORE-GOBERNA-RACI-01
### Glosario Extendido
#### ID
GEO-GORE-ANEXOS-GLOSARIO-01
#### Cpt
Glosario extendido de términos IDE, SNIT, CSW, WMS, WFS, WCS, LAMPv2, UN-IGIF, QA/QC, Metadatos y Catálogo de Objetos.
#### Ref
- GN-GEO-GLOS-IDE-CHILE
- GN-GEO-GLOS-CSW
- GN-GEO-GLOS-WMS
- GN-GEO-GLOS-LAMPV2
- GN-GEO-GLOS-UN-IGIF
- GN-GEO-GLOS-QA-QC
- GN-GEO-GLOS-METADATOS
- GN-GEO-GLOS-CATALOGO-OBJETOS

## Gobierno de Documento
### ID
GEO-GORE-DOC-GOBIERNO-01
### Resp
| Cpt | Def |
| --- | --- |
| Propietario del documento | Coordinación Regional IDE GORE Ñuble. |
### Proc
| Cpt | Def |
| --- | --- |
| Mantenimiento | Revisión semestral o ante cambios normativos/tecnológicos relevantes. |
| Control de cambios | Registro en repositorio institucional (GitHub/GitLab) y actualización de versión en metadatos. |
