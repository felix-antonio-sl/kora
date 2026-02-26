---
_manifest:
  urn: "urn:tde:kb:guia-estandares-datos-abiertos"
  provenance:
    created_by: FS
    created_at: '2026-02-26'
    source: "https://wikiguias.digital.gob.cl/Est%C3%A1ndares/Datos-Abiertos"
version: 1.0.0
status: published
tags: [datos-abiertos, open-data, estandares, metadatos, dcat, licencias, tde, guia]
lang: es
---

# Estándares para apertura y reutilización de Datos Abiertos

## Objetivo

Establecer estándares y directrices técnicas para apertura y reutilización de datos de OAE, facilitando acceso, uso, reutilización y redistribución para cualquier fin.

## Alcance

Aplicable a datos abiertos publicados en Portal de Datos Abiertos de SGD (datos.gob.cl). También a portales institucionales de OAE, que deben garantizar datos referenciados y sincronizados en plataforma SGD.

## Definiciones

| Término | Definición |
|---------|-----------|
| Catálogo de datos abiertos | Repositorio que centraliza, almacena y disponibiliza conjuntos de datos descritos por metadatos |
| Conjunto de datos (dataset) | Colección de datos en formatos de uso común, relacionados entre sí, descritos por metadatos |
| Dato | Representación de atributo/variable cuantitativa o cualitativa mediante secuencia de letras, números o símbolos |
| DCAT | Estándar de vocabulario de catálogos de datos para interoperabilidad |
| Dublin Core | Vocabulario genérico de 15 propiedades para describir recursos electrónicos (DCMI) |
| Dato abierto | Dato digital con características técnicas y jurídicas para ser usado, reutilizado y redistribuido libremente |
| Datos genéricos | Datos de uso común sin aplicación especializada |
| Datos geográficos | Datos referidos implícita/explícitamente a localización relativa a la Tierra (ISO/TC 211) |
| Diccionario de variables | Documento que detalla y define variables de un conjunto de datos |
| Documentación administrativa | Documentos que respaldan la publicación, proporcionando contexto y justificación |

## Estándares abiertos

### Formato abierto

Datos deben publicarse en formatos abiertos con clasificación "3 estrellas o más" de Tim Berners-Lee (https://5stardata.info/en/). Formatos no propietarios, legibles por máquinas.

### Formatos para datos genéricos

| Formato | Uso |
|---------|-----|
| CSV | Estructura relacional (tablas) |
| XML | Estructura jerárquica (árboles) |
| JSON | Estructura jerárquica (árboles) |
| RDF | Cualquier estructura (grafos) |
| TSV | Estructura relacional, tabulaciones como delimitadores |
| RAW | Datos brutos sin esquema definido |
| Parquet | Estructura columnar optimizada para analítica en grandes volúmenes |

### Formatos para datos geográficos

| Formato | Uso |
|---------|-----|
| GeoJSON | Datos geoespaciales basado en JSON |
| GML | Datos geográficos para WFS |
| GeoPackage | Basado en SQLite, soporta vectoriales y rasterización |

Se recomienda publicar en múltiples formatos. Se pueden añadir formatos adicionales (ej. XLS/XLSX junto a CSV).

### Documentación administrativa

- **PDF**: toda documentación administrativa (preserva contenido, accesible multiplataforma)
- **ODT**: documentos editables estandarizados (OpenDocument)

Complementa metadatos (no los sustituye). Explica proceso de generación, no contenido de datos.

### Archivos de gran tamaño

Límite máximo: **200 MB**. Si se excede → particionar con ZIP o 7z, garantizando integridad y accesibilidad al descomprimir.

## Lenguaje y codificación

- Idioma: **ES_CL** (datos y metadatos)
- Codificación: **UTF-8**

## Metadatos

Basados en estándar DCAT + Dublin Core, con adiciones para contexto nacional.

**Niveles de requerimiento**:
- **Obligatorio**: cumplimiento del perfil, documentación básica homogénea
- **Recomendado**: mayor calidad de documentación
- **Opcional**: útil según organismo, no aplica universalmente

### Metadatos de catálogo

| Metadato | Requerimiento |
|----------|--------------|
| Identificador del catálogo | Obligatorio |
| Título del catálogo | Obligatorio |
| Descripción del catálogo | Obligatorio |
| OAE asociado (según Gescode) | Obligatorio |
| Código de OAE (según Gescode) | Obligatorio |
| Correo electrónico OAE | Obligatorio |
| Fecha de creación | Obligatorio |
| Colección categorías | Recomendado |
| Conjuntos de datos | Opcional |
| Fecha última actualización | Recomendado |
| Idioma(s) | Recomendado |
| Licencia | Recomendado |
| Página web del catálogo | Opcional |
| Cobertura geográfica (país/región/provincia/comuna) | Recomendado |
| N° visitas | Recomendado |

### Metadatos de conjunto de datos

| Metadato | Requerimiento |
|----------|--------------|
| Identificador | Obligatorio |
| Título | Obligatorio |
| Descripción | Obligatorio |
| Autor | Obligatorio |
| Correo electrónico contacto | Obligatorio |
| OAE asociado (Gescode) | Obligatorio |
| Código OAE (Gescode) | Obligatorio |
| Departamento OAE | Obligatorio |
| Recursos | Obligatorio |
| Categoría | Obligatorio |
| Fecha de creación | Obligatorio |
| Fecha de publicación | Obligatorio |
| Palabras clave | Obligatorio |
| Período de referencia | Obligatorio |
| Licencia | Obligatorio |
| Versionamiento | Obligatorio |
| Fecha de la versión | Obligatorio |
| Procedencia | Recomendado |
| Detalle de procedencia | Recomendado |
| Fecha última modificación | Recomendado |
| Frecuencia de actualización | Recomendado |
| URL de acceso | Recomendado |
| Idioma(s) | Recomendado |
| Cobertura geográfica | Recomendado |
| Visitas | Recomendado |
| Descargas | Recomendado |
| Registro de cambios | Recomendado |
| Relación (gestionador/autor/custodia) | Opcional |
| Tamaño del dataset | Opcional |

### Metadatos de recurso

| Metadato | Requerimiento |
|----------|--------------|
| Identificador | Obligatorio |
| Título | Obligatorio |
| Descripción | Obligatorio |
| Diccionario de variables | Obligatorio |
| Fecha última actualización | Recomendado |
| URL de acceso | Recomendado |
| Tamaño del archivo | Recomendado |
| Formato del recurso | Recomendado |
| Visitas | Recomendado |
| Descargas | Recomendado |

Para datos geográficos → norma ISO 19115-1.

### Diccionario de variables

Cada dataset debe publicarse con diccionario de variables:

| Campo | Requerimiento |
|-------|--------------|
| Nombre (encabezado del recurso) | Obligatorio |
| Tipo de dato | Obligatorio |
| Descripción | Obligatorio |
| Identificador (único en catálogo) | Recomendado |
| Unidad de medida (sólo numéricos) | Opcional |

## Licencias

### Licencia predeterminada

En ausencia de asignación explícita → **Creative Commons Zero (CC0 1.0)**: renuncia a derechos de autor, dominio público.

### Licencias alternativas permitidas

| Licencia | Dominio | Descripción |
|----------|---------|-------------|
| PDDL-1.0 (Open Data Commons) | Datos | Uso, modificación y distribución libre sin restricción |
| CC-BY-4.0 (Creative Commons Attribution) | Contenido, Datos | Copiar, distribuir, obras derivadas con crédito al creador |
| ODC-By-1.0 (Open Data Commons Attribution) | Datos | Copia, distribución, uso con atribución al autor |

Licencia distinta a las listadas → solicitar y justificar ante SGD.

## Catálogos institucionales de datos abiertos

OAE con portal/plataforma propia deben:
- Acceso inmediato sin registro ni identificación
- Listado completo, ordenado y clasificado de datasets
- Funcionalidades de navegación, búsqueda de texto y lenguaje de consulta
- Operatividad continua del portal + análisis de estadísticas de uso
- APIs para captura y utilización de datasets + integración con Portal Nacional
