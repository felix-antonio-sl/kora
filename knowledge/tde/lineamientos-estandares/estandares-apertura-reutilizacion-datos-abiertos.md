---
_manifest:
  urn: "urn:tde:kb:estandares-apertura-reutilizacion-datos-abiertos"
  provenance: "https://wikiguias.digital.gob.cl/Est%C3%A1ndares/Datos-Abiertos"
version: 1.0.0
status: published
tags: [tde, lineamientos-estandares, datos-abiertos, open-data, datos, gobernanza]
lang: es
---

# Estándares para la apertura y reutilización de Datos Abiertos

> **Portal de referencia:** [datos.gob.cl](http://datos.gob.cl) — Secretaría de Gobierno Digital
> **Objeto:** Establecer estándares y directrices técnicas para la apertura y reutilización de datos de los órganos de la Administración del Estado, facilitando su acceso, uso, reutilización y redistribución para cualquier fin.
> **Alcance:** Datos abiertos y conjuntos de datos publicados en el Portal de Datos Abiertos de la Secretaría de Gobierno Digital y en portales o plataformas institucionales de los órganos de la Administración del Estado (estos últimos deben garantizar que sus datos estén referenciados y sincronizados en la plataforma de la SGD).

---

## Conceptos y Definiciones

| Término | Definición |
|---------|------------|
| **Catálogo de datos abiertos** | Repositorio que centraliza, almacena y disponibiliza conjuntos de datos abiertos estructurados y descritos por metadatos |
| **Conjunto de datos abiertos (dataset)** | Colección de datos representados en formatos de uso común y conocidos (si es posible, estructurados), relacionados entre sí y descritos por sus metadatos |
| **Dato** | Representación de un atributo o variable cuantitativa o cualitativa mediante letras, números o símbolos, capturable por observación y/o medición |
| **DCAT** | Estándar internacional de vocabulario de catálogos de datos, diseñado para facilitar la interoperabilidad entre catálogos de datos en la red |
| **Dublin Core Metadata Element Set** | Vocabulario genérico de 15 propiedades para describir recursos electrónicos (DCMI) |
| **Dato abierto** | Dato digital con las características técnicas y jurídicas para ser usado, reutilizado y redistribuido libremente por cualquier persona y órgano, en cualquier momento y lugar |
| **Datos genéricos** | Datos de uso común que no requieren una aplicación especializada para ser utilizados |
| **Datos geográficos** | Datos que implícita o explícitamente se refieren a una localización relativa a la Tierra (ISO/TC 211) |
| **Diccionario de variables** | Documento que detalla y define las variables de un conjunto de datos, describiendo su naturaleza, tipo y estructura |
| **Documentación administrativa** | Documentos que respaldan la publicación de datos abiertos, proporcionando contexto y justificación para su uso y comprensión |

---

## Estándares Abiertos

### Formato abierto

Los datos abiertos deben publicarse en formatos abiertos que aseguren su máxima reutilización y accesibilidad, cumpliendo con la clasificación de **"tres estrellas o más"** de Tim Berners-Lee, favoreciendo el uso de formatos no propietarios.

### Datos genéricos

| Nombre | Uso esperado |
|--------|-------------|
| **CSV** | Datos con estructura relacional (Tablas) |
| **XML** | Datos con estructura jerárquica (Árboles) |
| **JSON** | Datos con estructura jerárquica (Árboles) |
| **RDF** | Datos con cualquier estructura (Grafos) |
| **TSV** | Datos con estructura relacional (Tablas), usando tabulaciones como delimitadores |
| **RAW** | Datos en formato bruto o sin procesar, sin esquema estructurado definido |
| **Parquet** | Datos con estructura columnar optimizada para operaciones analíticas en grandes volúmenes |

### Datos geográficos

| Nombre | Uso esperado |
|--------|-------------|
| **GeoJSON** | Datos geoespaciales basados en JSON |
| **GML** | Datos geográficos que proveen información del servicio WFS |
| **GeoPackage** | Basado en SQLite para almacenamiento y transferencia de datos geoespaciales; soporta datos vectoriales y de rasterización |

Para datos geográficos a nivel de recurso, se recomienda utilizar la norma **ISO 19115-1**.

Se recomienda proporcionar los datos en **múltiples formatos** para mayor flexibilidad. Se pueden publicar formatos adicionales (ej.: versión XLS o XLSX junto con el CSV para datos tabulares).

### Documentación administrativa

| Formato | Uso |
|---------|-----|
| **PDF** | Toda documentación administrativa (preserva fielmente el contenido original, accesible en diversas plataformas) |
| **ODT** | Documentos que necesiten ser editables manteniendo accesibilidad y estandarización (estándar OpenDocument) |

La documentación administrativa no constituye un metadato; complementa a los metadatos para enriquecer la transparencia y facilitar la interpretación. Su propósito es explicar el proceso de generación de los datos, no describir el contenido de los datos en sí.

### Archivos de Gran Tamaño

Límite máximo de tamaño de archivo: **200 megabytes**. Si la naturaleza del conjunto de datos justifica exceder este límite, la entidad debe particionar el archivo usando formatos comprimidos como **ZIP o 7z**, garantizando la integridad y accesibilidad total de los datos una vez descomprimidos.

---

## Lenguaje y Codificación

- **Lenguaje:** Español-Chile (ES_CL)
- **Codificación de caracteres:** UTF-8

---

## Metadatos

Cada Órgano de la Administración del Estado (OAE) debe publicar todos los conjuntos de datos abiertos junto con sus metadatos, consistentes y en formatos legibles tanto para humanos como para máquinas.

Los metadatos se estructuran siguiendo el estándar **DCAT**, complementado por elementos del **Dublin Core**, con adiciones y modificaciones para el contexto nacional.

**Niveles de requerimiento:**

| Nivel | Descripción |
|-------|-------------|
| **Obligatorio** | Uso obligatorio para el cumplimiento del perfil; asegura documentación básica homogénea para todos los conjuntos de datos |
| **Recomendado** | No obligatorio, pero su uso mejora la calidad de la documentación |
| **Opcional** | Disponible si es de utilidad para el organismo; no necesariamente aplica para todos los casos |

### Metadatos a nivel de Catálogo

| Nombre del Metadato | Descripción | Requerimiento |
|--------------------|-------------|---------------|
| Identificador del Catálogo | Código único para identificar inequívocamente el catálogo | Obligatorio |
| Título del Catálogo | Nombre claro, breve y suficientemente abstracto para abarcar la multiplicidad de conjuntos de datos | Obligatorio |
| Descripción del Catálogo | Detalla el contenido y alcance del catálogo, incluyendo la naturaleza y tipos de datos | Obligatorio |
| OAE Asociado | Órgano de Administración del Estado al que pertenece (según Gescode de Gobierno Digital) | Obligatorio |
| Código de OAE | Código del OAE (según Gescode de Gobierno Digital) | Obligatorio |
| Correo electrónico OAE | Correo de contacto del OAE que publica el catálogo | Obligatorio |
| Fecha de creación | Fecha en que el catálogo fue creado oficialmente | Obligatorio |
| Colección Categorías | Desagregación por categorías (lista de segundo nivel) | Recomendado |
| Fecha de última actualización/modificación | Fecha de última actualización o modificación del catálogo | Recomendado |
| Idioma(s) | Lenguaje utilizado para describir metadatos y conjuntos de datos | Recomendado |
| Licencia | Licencia bajo la cual los conjuntos de datos y recursos están disponibles (una licencia específica del dataset la sobreescribe) | Recomendado |
| Cobertura geográfica | Ámbito geográfico de los datos (País, Región, Provincia, Comuna) | Recomendado |
| N° visitas | Número de visitas acumuladas al catálogo | Recomendado |
| Conjuntos de Datos | Lista de los conjuntos de datos que forman parte del catálogo | Opcional |
| Página web del catálogo | URL de acceso a la página principal del catálogo | Opcional |

### Metadatos a nivel de Conjunto de Datos

| Nombre del Metadato | Descripción | Requerimiento |
|--------------------|-------------|---------------|
| Identificador del Conjunto de Datos | Identificador único del conjunto de datos | Obligatorio |
| Título del Conjunto de Datos | Nombre claro y suficientemente abstracto para abarcar la multiplicidad de recursos que contiene | Obligatorio |
| Descripción del Conjunto de Datos | Resumen detallado del contenido y propósito del conjunto de datos | Obligatorio |
| Autor | Nombre del responsable de la publicación | Obligatorio |
| Correo electrónico de Contacto | Correo del responsable de la publicación | Obligatorio |
| OAE Asociado | Órgano de Administración del Estado al que pertenece (Gescode) | Obligatorio |
| Código de OAE | Código del OAE (Gescode) | Obligatorio |
| Departamento de la OAE | Departamento encargado de la publicación | Obligatorio |
| Recursos | Lista de recursos que pertenecen al conjunto de datos | Obligatorio |
| Categoría | Temática(s) o categoría(s) globales del conjunto de datos (puede pertenecer a más de una) | Obligatorio |
| Fecha de Creación | Fecha en que el conjunto de datos fue creado | Obligatorio |
| Fecha de publicación | Fecha de publicación en el portal de datos abiertos | Obligatorio |
| Palabras Claves | Etiquetas que colaboran en la búsqueda de los usuarios | Obligatorio |
| Periodo de referencia | Lapso temporal al que hace referencia la información | Obligatorio |
| Licencia | Licencia bajo la cual se distribuye el conjunto de datos y todos sus recursos | Obligatorio |
| Versionamiento | Versión del conjunto de datos citado | Obligatorio |
| Fecha de la versión | Fecha de la edición de la versión | Obligatorio |
| Procedencia del conjunto de datos | Indica si es un subconjunto, integración de varios conjuntos o producto de procesamiento | Recomendado |
| Detalle de procedencia | Especifica los conjuntos de datos originales utilizados para formar el nuevo conjunto | Recomendado |
| Fecha de última modificación | Fecha de última modificación del conjunto de datos o sus metadatos | Recomendado |
| Frecuencia de actualización | Frecuencia con que se actualiza el conjunto de datos | Recomendado |
| Ubicación o Enlace Directo (URL) | URL de acceso al conjunto de datos o información adicional | Recomendado |
| Idioma(s) | Lenguaje usado para describir el conjunto de datos y sus metadatos | Recomendado |
| Cobertura geográfica | Ámbito geográfico de los datos (País, Región, Provincia, Comuna) | Recomendado |
| Visitas al dataset | Número total de visitas recibidas | Recomendado |
| Descargas | Cantidad de veces descargado | Recomendado |
| Registro de Cambios | Descripción cronológica de modificaciones significativas | Recomendado |
| Relación | Relación entre el conjunto de datos y el OAE (gestionador, autor institucional o custodia) | Opcional |
| Tamaño del Dataset | Volumen de datos del conjunto | Opcional |

### Metadatos a nivel de Recurso

| Nombre | Descripción | Requerido |
|--------|-------------|-----------|
| Identificador | Identificador único del recurso dentro del conjunto de datos | Obligatorio |
| Título | Nombre del recurso tal como será publicado | Obligatorio |
| Descripción | Breve descripción del recurso | Obligatorio |
| Diccionario de variables | Lista de campos del recurso tabular (no aplica para no-tablas) | Obligatorio |
| Fecha de última actualización/modificación | Fecha de última actualización o modificación del recurso | Recomendado |
| Ubicación o Enlace Directo (URL) | URL de acceso al recurso | Recomendado |
| Tamaño del Archivo | Tamaño en bytes (puede ser aproximado) | Recomendado |
| Formato del recurso | Formato del archivo | Recomendado |
| Visitas al recurso | Cantidad de visitas al recurso | Recomendado |
| Descargas | Cantidad de descargas del recurso | Recomendado |

---

## Diccionario de Variables

Cada conjunto de datos abiertos debe publicarse con su **diccionario de variables**, que debe incluir la siguiente información para cada variable:

| Nombre | Descripción | Requerido |
|--------|-------------|-----------|
| Nombre | Nombre del campo tal como se denomina en el encabezado del recurso | Obligatorio |
| Tipo | Tipo de dato contenido en el campo | Obligatorio |
| Descripción | Descripción de la información que contiene el campo | Obligatorio |
| Identificador | Código identificador único del campo en todo el catálogo (cuando se requiere para un sistema o aplicación) | Recomendado |
| Unidad de medida | Descripción de la unidad de medida de los valores del campo (solo para campos numéricos) | Opcional |

---

## Licencia para la apertura y publicación de datos

Los datos y conjuntos de datos abiertos de los órganos de la Administración del Estado deben ponerse a disposición de todas las personas mediante **licencias de dominio público**.

**Licencia predeterminada:** En ausencia de asignación explícita, todos los conjuntos de datos se abrirán bajo la licencia **Creative Commons Zero (CC0 1.0)**.

| Licencia | Dominio | Descripción |
|----------|---------|-------------|
| Creative Commons Zero (CC0 1.0) | Contenido, Datos | Renuncia a todos los derechos de autor y derechos conexos; permite cualquier uso sin restricciones, situándose en el dominio público |

**Licencias alternativas** para conjuntos de datos según sus características:

| Licencia | Dominio | Descripción |
|----------|---------|-------------|
| Open Data Commons Public Domain Dedication and Licence (PDDL-1.0) | Datos | Permite usar, modificar y distribuir libremente los datos sin ninguna restricción |
| Creative Commons Attribution 4.0 (CC-BY-4.0) | Contenido, Datos | Permite copiar, distribuir, exhibir y ejecutar obras derivadas con la condición de dar crédito al creador original |
| Open Data Commons Attribution License (ODC-By-1.0) | Datos | Permite copia, distribución y uso en nuevos productos o aplicaciones, siempre que se dé atribución al autor |

Si la naturaleza del conjunto de datos hace necesario utilizar una licencia diferente, la entidad deberá **solicitar y justificar** esta situación a la Secretaría de Gobierno Digital.

---

## Catálogos de Datos Abiertos Institucionales

Los órganos de la Administración del Estado que dispongan de un portal o plataforma de datos abiertos institucional deben:

- **Acceso inmediato:** Asegurar que el acceso sea inmediato, sin requisitos adicionales de registro o identificación
- **Listado completo:** Contener un listado completo, ordenado y clasificado de todos los conjuntos de datos disponibles
- **Navegabilidad:** Facilitar la navegación, búsqueda y consulta efectiva dentro del repositorio, implementando funcionalidades de navegación, búsqueda de texto y lenguaje de consulta
- **Operatividad continua:** Mantener la operatividad del portal, asegurando disponibilidad continua y analizando estadísticas de uso para mejorar el servicio
- **APIs:** Proveer APIs que faciliten la captura y utilización de los conjuntos de datos por usuarios finales y su integración en el Portal Nacional de Datos Abiertos
