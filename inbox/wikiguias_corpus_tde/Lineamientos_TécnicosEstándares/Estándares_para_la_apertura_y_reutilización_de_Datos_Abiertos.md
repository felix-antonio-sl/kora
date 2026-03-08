---
title: "Estándares para la apertura y reutilización de Datos Abiertos"
url: "https://wikiguias.digital.gob.cl/Est%C3%A1ndares/Datos-Abiertos"
category: "Lineamientos Técnicos/Estándares"
tags: [{'tag': 'datos', 'title': 'datos'}, {'tag': 'datos abiertos', 'title': 'datos abiertos'}, {'tag': 'open data', 'title': 'open data'}, {'tag': 'gobernanza', 'title': 'gobernanza'}]
description: "Guía para la estandarización estructura, una fácil comprensión y accesibilidad de los Datos Abiertos"
updated_at: "2025-10-07T21:05:54.773Z"
---

[¶](#estándares-para-la-apertura-y-reutilización-de-datos-abiertos) Estándares para la apertura y reutilización de Datos Abiertos
=================================================================================================================================

[¶](#introducción) INTRODUCCIÓN.
--------------------------------

El concepto de Datos Abiertos (Open Data) representa un compromiso global hacia la transparencia, el acceso a la información pública y la promoción de la competitividad y el desarrollo económico mediante la reutilización de información estatal. A través de iniciativas como [datos.gob.cl](http://datos.gob.cl), el Gobierno de Chile busca garantizar que todos los datos de carácter público generados por las instituciones estatales estén disponibles de forma abierta y accesible para todos los ciudadanos y entidades interesadas.

Los Datos Abiertos son publicados en formatos digitales estandarizados y estructurados para asegurar una fácil comprensión y accesibilidad, permitiendo que la información pueda ser utilizada no solo para generar informes y estadísticas, sino también para fomentar el beneficio social, generar investigación científica y crear oportunidades de negocio a través de su aplicación en diversas áreas como salud, seguridad, transporte, educación y medioambiente, entre otras.

Esta iniciativa se alinea con directrices internacionales y sigue ejemplos de países líderes en la materia, como Estados Unidos y el Reino Unido, quienes han avanzado significativamente en la publicación de datos abiertos desde el lanzamiento de iniciativas como la Open Government Directive y Opening up Government. Además, se reconoce el esfuerzo previo de la Unión Europea con la Directiva 2003/98/CE sobre la reutilización de la información del sector público.

> Director Peter R. Orszag, de la Oficina de Administración y Presupuesto, de la Oficina de Presidencia, de 8 de diciembre de 2009. Open Government Directive. Disponible en línea en: <https://obamawhitehouse.archives.gov/open/documents/open-government-directive>

> Gobierno de Reino Unido, 2010. [DATA.GOV.UK](http://DATA.GOV.UK): Opening Up Government. Disponible en línea en: <http://data.gov.uk/>

> Directiva 2003/98/CE del Parlamento Europeo y del Consejo, de 17 de noviembre de 2003, relativa a la reutilización de la información del sector público, Diario Oficial N° L 345 de 31 de diciembre de 2006, pp. 0090 – 0096. Disponible en línea en: <http://eurlex.europa.eu/LexUriServ/LexUriServ.do?uri=CELEX:32003L0098:ES:HTML>

El proyecto [datos.gob.cl](http://datos.gob.cl) es un pilar fundamental en la estrategia de Gobierno Digital de Chile, proporcionando datos que son financiados y recopilados con recursos públicos y que, por lo tanto, deben estar al servicio de la ciudadanía sin restricciones de uso y formatos adecuados. Este enfoque no solo busca potenciar la transparencia y el acceso a la información sino que también fomenta el desarrollo de nuevas tecnologías y la innovación, al permitir que terceros agreguen valor a los datos disponibles y generen nuevas soluciones y aplicaciones que beneficien a la sociedad en su conjunto.

[¶](#objetivo) OBJETIVO.
------------------------

La presente resolución tiene por objeto establecer los estándares y directrices técnicas para la apertura y reutilización de datos de los órganos de la Administración del Estado, con el propósito de facilitar su acceso, uso, reutilización y redistribución para cualquier fin.

[¶](#alcance-de-los-estándares-y-directrices-técnicas) ALCANCE DE LOS ESTÁNDARES Y DIRECTRICES TÉCNICAS
-------------------------------------------------------------------------------------------------------

Estos estándares y directrices técnicas son aplicables a los datos abiertos y conjuntos de datos abiertos publicados en el Portal de Datos Abiertos de la Secretaría de Gobierno Digital. Asimismo, se aplican a los portales o plataformas institucionales de datos abiertos de los órganos de la Administración del Estado, los cuales deberán garantizar que dichos datos estén referenciados y sincronizados en la plataforma de la SGD.

[¶](#conceptos-definiciones) CONCEPTOS - DEFINICIONES
-----------------------------------------------------

Para los efectos de la aplicación de las disposiciones establecidas por esta norma se entenderá por:

**Catálogo de datos abiertos:** repositorio que centraliza, almacena y disponibiliza conjuntos de datos abiertos estructurada y descrita por metadatos.  
**Conjunto de datos abiertos o datasets:** colección de datos representados, en su forma original, en formatos de uso común y conocidos y, si es posible, estructurados. Estos datos están relacionados entre sí y se encuentran descritos por sus metadatos.  
**Dato:** representación de un atributo o variable cuantitativa o cualitativa, por medio de una secuencia de letras, números o símbolos y que es posible capturar a través de la observación y/o medición de una o más personas, objetos, hechos, juicios o fenómenos.  
**DCAT:** estándar internacional relativo al vocabulario de catálogos de datos, diseñado para facilitar la interoperabilidad entre los catálogos de datos publicados en la red.  
**Dublin Core Metadata Element Set:** vocabulario genérico de 15 propiedades para describir recursos electrónicos auspiciado por la Dublin Core Metadata Initiative (DCMI)  
**Dato abierto:** dato digital con las características técnicas y jurídicas necesarias para que pueda ser usado, reutilizado y redistribuido libremente por cualquier persona y órgano de la Administración del Estado, en cualquier momento y lugar.  
**Datos genéricos:** datos de uso común que no requiere una aplicación especializada para ser utilizado.  
**Datos geográficos:** datos que implícita o explícitamente se refieren a una localización relativa a la Tierra. (Fuente: ISO/TC 211)  
**Diccionario de variables:** documento que detalla y define las variables incluidas en un conjunto de datos, describiendo su naturaleza, tipo y estructura.  
\*\*Documentación administrativa: \*\*documentos que respaldan la publicación de los datos abiertos, proporcionando contexto y justificación para su uso y comprensión.

[¶](#estándares-abiertos) ESTÁNDARES ABIERTOS.
----------------------------------------------

### [¶](#formato-abierto) Formato abierto.

Los datos abiertos de la Administración del Estado deben publicarse en formatos abiertos que aseguren su máxima reutilización y accesibilidad. Se requerirá que estos formatos cumplan con la clasificación de "tres estrellas o más" de Tim Berners-Lee, favoreciendo el uso de formatos no propietarios. Este criterio garantiza la legibilidad de los datos por máquinas sin la necesidad de herramientas costosas y facilita su integración en diversas aplicaciones.

> Tres estrellas o mas de Tim Berners-Lee: <https://5stardata.info/en/>

Conforme a la clasificación previamente establecida, se detallan a continuación algunos de los formatos abiertos que alcanzan un nivel de "tres estrellas o más". Estos formatos específicos son los que serán aceptados para la publicación de datos abiertos, adecuados a las distintas estructuras de datos y necesidades operativas implicadas:

### [¶](#datos-genéricos) Datos genéricos.

Los siguientes formatos abiertos se deberán utilizar para el manejo de datos genéricos, cada uno adecuado a diferentes estructuras de datos y necesidades operativas:

|  |  |
| --- | --- |
| **Nombre** | **Uso esperado** |
| CSV | Datos con estructura relacional (Tablas) |
| XML | Datos con estructura jerárquica (Árboles) |
| JSON | Datos con estructura jerárquica (Árboles) |
| RDF | Datos con cualquier estructura (Grafos) |
| TSV | Datos con estructura relacional (Tablas), utilizando tabulaciones como delimitadores entre elementos. |
| RAW | Datos en formato bruto o sin procesar que no siguen un esquema estructurado definido. |
| Parquet | Datos con estructura columnar optimizada para operaciones analíticas y de consulta en grandes volúmenes de datos. |

### [¶](#datos-geográficos) **Datos geográficos.**

Los datos geográficos son esenciales para una variedad de aplicaciones que requieren representaciones precisas de la superficie terrestre o de geometrías en el espacio geográfico. Para la publicación de estos datos, se deberán utilizar los siguientes formatos abiertos :

|  |  |
| --- | --- |
| **Nombre** | **Uso esperado** |
| GeoJSON | Datos geoespaciales basado en JSON |
| GML | Dato geográficos que proveen la información del servicio WFS |
| GeoPackage | Basado en SQLite para el almacenamiento y transferencia de datos geoespaciales y atributos, que soporta tanto datos vectoriales como de rasterización |

Para asegurar la accesibilidad y la utilización efectiva de los datos abiertos por una amplia variedad de aplicaciones y usuarios, es recomendable que los datos se proporcionen en múltiples formatos. Esto permite una mayor flexibilidad y adaptabilidad a las diferentes necesidades tecnológicas y de uso.

Además, se podrán publicar formatos adicionales para cada conjunto de datos para asegurar la mayor inclusión y entendimiento posible, por ejemplo: en el caso de datos tabulares hacer disponible la versión XLS o XLSX del archivo junto con el CSV.

### [¶](#documentación-administrativa) **Documentación administrativa.**

En casos donde los conjuntos de datos sean acompañados de documentación administrativa, dicha documentación debe cumplir con formatos específicos para asegurar su integridad y accesibilidad. La documentación administrativa abarca todos los documentos oficiales que respaldan, explican y contextualizan los conjuntos de datos abiertos publicados. Los formatos requeridos son los siguientes:

* PDF (Portable Document Format): Deberá utilizarse para toda documentación administrativa, garantizando que los documentos se presenten en un formato que preserve fielmente el contenido original y sea accesible para visualización en diversas plataformas tecnológicas
* ODT (Open Document Text): Para documentos que necesiten ser editables mientras se mantiene su accesibilidad y estandarización, se recomienda el uso de ODT, parte del estándar OpenDocument para procesadores de texto.

Esta documentación adjunta a los conjuntos de datos tiene como finalidad proporcionar detalles adicionales sobre la metodología y el origen de los datos, ofreciendo una mayor comprensión y contexto. Esta documentación no constituye un metadato, sino que complementa a los metadatos para enriquecer la transparencia y facilitar la interpretación de los datos publicados. Los órganos de la Administración del Estado deben adherirse a los formatos específicos al preparar esta documentación, que sirve exclusivamente para explicar el proceso de generación de los datos y no para describir el contenido de los datos en sí

### [¶](#archivos-de-gran-tamaño) **Archivos de Gran Tamaño.**

Se establece un límite máximo de tamaño de archivo en 200 megabytes. No obstante, en casos donde la naturaleza específica del conjunto de datos o una parte de estos justifique la necesidad de exceder este límite, la entidad correspondiente deberá particionar el archivo utilizando formatos comprimidos como ZIP o 7z. Esta partición debe garantizar la integridad y la accesibilidad total de los datos una vez descomprimidos.

[¶](#lenguaje-y-codificación) **Lenguaje y codificación.**
----------------------------------------------------------

El lenguaje que se debe utilizar para los datos y metadatos es Español-Chile (ES\_CL) y la codificación de caracteres debe ser UTF-8.

[¶](#metadatos) **Metadatos.**
------------------------------

Corresponde a cada Órgano de la Administración del Estado (OAE) publicar todos los conjuntos de datos abiertos junto con sus metadatos consistentes y en formatos legibles tanto para humanos como para máquinas, facilitando así la comprensión del origen, procesamiento y significado de los conjuntos y recursos de datos.

En conformidad con esta directriz, los metadatos requeridos para la publicación de datos abiertos se estructuran siguiendo el estándar DCAT, un marco diseñado para mejorar la interoperabilidad de los catálogos de datos abiertos en la red y complementado por elementos del Dublin Core, un estándar internacional para metadatos que facilitan la descripción general de recursos digitales. Ambos estándar fueron base para formular los metadatos realizando adiciones y modificaciones específicas para el contexto nacional y así incrementar la comprensión de los datos para los usuarios.

Los estándares de metadatos se organizan en cuatro niveles esenciales, cada uno con un propósito específico para mejorar la accesibilidad, facilitar la búsqueda e interpretación de los conjuntos de datos. Cada nivel define el grado de requerimiento del metadato, categorizado de la siguiente manera:

***Obligatorio:*** propiedad de uso obligatorio para el cumplimiento del perfil. Permite que todos los conjuntos de datos abiertos cuenten con una documentación básica homogénea.

***Recomendado*** propiedad que, si bien no es obligatoria, su uso es recomendado para una mayor calidad de documentación de los conjuntos de datos abiertos.

***Opcional:*** propiedad disponible para su uso en caso de que sea de utilidad para el organismo, pero que no necesariamente aplica para todos los casos.

A continuación, se muestran los metadatos solicitados por nivel, su descripción y el requerimiento:

### [¶](#metadatos-a-nivel-de-catálogo) **Metadatos a nivel de Catálogo:**

Proporcionan una visión general y comprensiva del catálogo de datos abiertos

|  |  |  |  |
| --- | --- | --- | --- |
| **Nombre del Metadato** | **Descripción** | **Requerimiento** | **Ejemplo** |
| Identificador del Catálogo | Código único asignado para identificar de manera inequívoca el catálogo | Obligatorio | cat\_001 |
| Título del Catálogo | Nombre dado al catálogo. Debe ser claro, breve y lo suficientemente abstracto como para abarcar la multiplicidad de conjuntos de datos abiertos que contiene. | Obligatorio | Catálogo de Datos Abiertos de la Ciudad de Santiago |
| Descripción del Catálogo | Descripción que detalla el contenido y el alcance del catálogo, incluyendo la naturaleza y tipos de datos que engloba. | Obligatorio | Conjunto de datos abiertos de la Municipalidad de Santiago, incluye información sobre demografía, transporte, obras públicas, etc. |
| OAE Asociado | Órgano de Administración del Estado al que pertenece el catálogo. De acuerdo al Gescode de Gobierno Digital. | Obligatorio | Municipalidad de Santiago |
| Código de OAE | Código asociado al Organo de Administración del Estado que pertenece el catálogo. De acuerdo al Gescode de Gobierno Digital. | Obligatorio | PE-MUN-00432 |
| Correo electrónico OAE | Correo electrónico de contacto de la OAE de la publicación del catálogo. | Obligatorio | [datos@municipalidad.gob.cl](mailto:datos@municipalidad.gob.cl) |
| Colección Categorías | Desagregación por categorías, lista de segundo nivel de acuerdo a las categorías que contenga el catálogo | Recomendado | Demografía, Transporte, Obras Públicas |
| Conjuntos de Datos | Contiene una lista de los conjuntos de datos abiertos que forman parte del catálogo. | Opcional | dataset\_1, dataset\_2, dataset\_3 |
| Fecha de creación | Fecha en que el catálogo fue creado oficialmente. | Obligatorio | 2023-01-01 |
| Fecha de última actualización/ modificación | Fecha de última actualización o modificación realizada al catálogo. | Recomendado | 2023-12-31 |
| Idioma(s) | Lenguaje utilizado para describir los metadatos y los conjuntos de datos abiertos en el catálogo. | Recomendado | Español, Inglés |
| Licencia | Indica la licencia bajo la cual los conjuntos de datos abiertos  y recursos del catálogo están disponibles. Un conjunto de datos abiertos o recurso que especifique una licencia diferente, sobreescribe a la licencia general del catálogo. | Recomendado | CC BY 4.0 |
| Página web del catálogo | Dirección web de acceso a la página principal del catálogo. | Opcional | <https://datos.gob.cl/> |
| Cobertura geográfica | Descripción del ámbito geográfico que abarcan los datos del catálogo, pudiendo especificar niveles:     - País   - Región   - Provincia   - Comuna | Recomendado | Chile, Región Metropolitana, Santiago |
| N° visitas | Número de visitas acumuladas por los usuarios al catálogo, reflejando el grado de interacción pública. | Recomendado | 1000 |

### [¶](#metadatos-a-nivel-de-conjunto-de-datos) Metadatos a nivel de Conjunto de Datos:

Detallan las características específicas de cada conjunto de datos abiertos.

|  |  |  |  |
| --- | --- | --- | --- |
| **Nombre del Metadato** | **Descripción** | **Requerimiento** | **Ejemplo** |
| Identificador del Conjunto de Datos | Identificador único asignado al conjunto de datos abiertos. | Obligatorio | dataset\_001 |
| Título del Conjunto de Datos | Nombre asignado al conjunto de datos tal como será publicado. Debe ser claro y lo suficientemente abstracto como para abarcar la multiplicidad de recursos que contiene. | Obligatorio | Datos abiertos de temperatura en Santiago |
| Descripción del Conjunto de Datos | Resumen detallado que explica el contenido y propósito del conjunto de datos abiertos, ofreciendo suficiente información para entender su relevancia y estructura. | Obligatorio | Conjunto de datos que contiene registros históricos de temperatura máxima y mínima diaria en estaciones meteorológicas de la ciudad de Santiago, desde 1980 hasta la actualidad. |
| Autor | Nombre del responsable de la publicación del conjunto de datos abiertos. | Obligatorio | Departamento de Meteorología, Municipalidad de Santiago |
| Correo electrónico de Contacto | Correo electrónico de contacto del responsable de la publicación del conjunto de datos abierto. | Obligatorio | [departamento@munidesantiago.gob.cl](mailto:departamento@munidesantiago.gob.cl) |
| OAE Asociado | Órgano de Administración del Estado al que pertenece el conjunto de datos abiertos. De acuerdo al Gescode de Gobierno Digital. | Obligatorio | Municipalidad de Santiago |
| Código de OAE | Código asociado al Organo de Administración del Estado que pertenece al conjunto de datos abiertos. De acuerdo al Gescode de Gobierno Digital. | Obligatorio | PE-MUN-00432 |
| Departamento de la OAE | Departamento encargado de la publicación del conjunto de datos abiertos. | Obligatorio | Departamento de Medio Ambiente |
| Recursos | Lista de recursos que pertenecen al conjunto de datos abiertos. | Obligatorio | archivo\_csv, archivo\_shp, metadata.json |
| Procedencia del conjunto de Datos | Indica los conjuntos de datos originales con que se conforman el conjunto de datos actual, especificando si es un subconjunto, una integración de varios conjuntos, o un producto de procesamiento. | Recomendado | Integración |
| Detalle de procedencia del conjunto de datos | Especifica los conjuntos de datos específicos del conjunto de datos original que fueron utilizadas para formar el nuevo conjunto de datos. | Recomendado | dataset\_1, dataset\_2, dataset\_3 |
| Categoría | Temática/s o categoría/s globales a la/s que se refiere el conjunto de datos abiertos al ser publicado. Un conjunto de datos abiertos puede pertenecer a más de una categoría global, de manera que el tipo de valor de este campo es una lista de categorías. | Obligatorio | Meteorología, Medio Ambiente, Urbanismo |
| Fecha de Creación | Fecha en la que el conjunto de datos de abierto fue creado | Obligatorio | 2023-01-01 |
| Fecha de publicación | Fecha de publicación del conjunto de datos abiertos en el portal de DDAA correspondiente | Obligatorio | 2023-02-15 |
| Fecha de última modificación | Fecha de última modificación del conjunto de datos abiertos (ya sea de sus datos o de sus metadatos) en el portal de DDAA correspondiente. | Recomendado | 2023-12-31 |
| Frecuencia de actualización | Frecuencia con la que se actualiza el conjunto de datos abiertos. | Recomendado | Mensual |
| Relación | Relación establecida entre el conjunto de datos abierto referenciado y el OAE. ( gestionador, autor institucional o custodia) | Opcional | autor institucional |
| Ubicación o Enlace Directo (URL) | URL de una página web a través de la cual se puede acceder al conjunto de datos abierto, sus recursos o información adicional sobre el mismo. | Recomendado | <https://datos.gob.cl/dataset/decima-encuesta-nacional-de-la-juventud> |
| Palabras Claves | Palabras que describen el título o el contenido del recurso. Etiquetas que colaboran en la búsqueda de los usuarios. Cuanto más amplia y uniforme sea la lista de tags mayor será su eficiencia. | Obligatorio | temperatura, Santiago, meteorología, clima |
| Periodo de referencia | Indica el lapso temporal al cual hacen referencia la información contenida en el conjunto de datos abiertos. | Obligatorio | 1980-2023 |
| Licencia | Detalles de la licencia bajo la cual se distribuye el conjunto de datos abiertos y todos sus recursos. | Obligatorio | CC BY 4.0 |
| Idioma(s) | Lenguaje  usado para describir el conjunto de datos abiertos y sus metadatos. | Recomendado | Español, Inglés |
| Cobertura geográfica | Descripción del ámbito geográfico que abarcan los datos del catálogo, pudiendo especificar niveles:    - País  - Región  - Provincia  - Comuna | Recomendado | Chile |
| Tamaño del Dataset | Volumen de datos que contiene el conjunto de datos abiertos. | Opcional | 10 MB |
| Visitas al dataset | Número total de visitas que el conjunto de datos abierto ha recibido. | Recomendado | 500 |
| Descargas | Cantidad de veces que el conjunto de datos abiertos ha sido descargado. | Recomendado | 200 |
| Versionamiento | Versión del conjunto de datos abierto citado. | Obligatorio | 1.0 |
| Fecha de la versión | Fecha de la edición de la versión. | Obligatorio | 2023-01-01 |
| Registro de Cambios | Describe de manera cronológica todas las modificaciones significativas que se han realizado en un conjunto de datos abiertos. | Recomendado | Versión 1.0: Datos iniciales. Versión 1.1: Se agregaron nuevas estaciones meteorológicas. |

### [¶](#metadatos-a-nivel-de-recurso) Metadatos a nivel de Recurso:

Se enfocan en describir los archivos individuales o recursos dentro de un conjunto de datos abiertos.

|  |  |  |  |
| --- | --- | --- | --- |
| **Nombre** | **Descripción** | **Requerido** | **Ejemplo** |
| Identificador | Identificador único del recurso, este identificador debe ser único para el recurso dentro del conjunto de datos abiertos. | Obligatorio | recurso\_001 |
| Título | Nombre asignado al recurso tal como será publicado. | Obligatorio | Datos de temperatura\_2023.csv |
| Descripción | Breve descripción del Recurso. Toda información adicional puede ser incluida en la descripción del conjunto de datos abiertos. | Obligatorio | Archivo CSV que contiene los registros de temperatura máxima y mínima diaria para el año 2023. |
| Diccionario de variables | Lista de campos que contiene un recurso tabular (no aplica para aquellas distribuciones que no sean tablas) | Obligatorio | fecha, estación, temperatura\_max, temperatura\_min |
| Fecha de última actualización/ modificación | Fecha de última actualización/modificación del Recurso. | Recomendado | 2023-12-31 |
| Ubicación o Enlace Directo (URL) | URL que permite el acceso al recurso del conjunto de datos abiertos. | Recomendado | <https://datos.gob.cl/dataset/10ma-encuesta-nacional-de-juventud/resource/b8579d7> |
| Tamaño del Archivo | Tamaño del Recurso en bytes. El tamaño puede ser aproximado cuando no se conozca el tamaño exacto. | Recomendado | 5 MB |
| Formato del recurso | Indica el formato del archivo del recurso | Recomendado | CSV |
| Visitas al recurso | Cantidad de visitas al recurso | Recomendado | 200 |
| Descargas | Cantidad de descargas del recurso | Recomendado | 100 |

Para datos geográficos, se recomienda utilizar la norma ISO 19115-1.

### [¶](#diccionario-de-variables) **Diccionario de Variables:**

Cada conjunto de datos abiertos deberá publicarse junto a su diccionario de variables, proporcionando una descripción detallada de las variables contenidas en los conjuntos de datos disponibles.

Los estándares establecidos para este diccionario definen tanto la estructura como la información específica que debe contenerse para cada variable, asegurando que los usuarios comprendan plenamente los datos y puedan utilizarlos eficazmente. El diccionario debe incluir la siguiente información para cada variable: Nombre, tipo, descripción, identificador, unidad de medida.

A continuación, se muestran la información que se requiere en el diccionario de variable junto con su descripción y el requerimiento:

|  |  |  |  |
| --- | --- | --- | --- |
| **Nombre** | **Descripción** | **Requerido** | **Ejemplo** |
| Nombre | El nombre del campo tal como se denomina en el encabezado del recurso. | Obligatorio | Edad |
| Tipo | El tipo de dato contenido en el campo | Obligatorio | Numérico |
| Descripción | La descripción de la información que contiene el campo. | Obligatorio | Edad de la persona encuestada |
| Identificador | El código identificador del campo. Debe ser único para todo el catálogo. Se utiliza cuando el campo requiere un identificador para ser utilizado en un sistema o aplicación. | Recomendado | edad |
| Unidad de medida | La descripción de la unidad de medida en la que están expresados los valores del campo. Sólo se utiliza para campos de tipo numérico. | Opcional | Años |

[¶](#licencia-para-la-apertura-y-publicación-de-datos) **LICENCIA PARA LA APERTURA Y PUBLICACIÓN DE DATOS**
-----------------------------------------------------------------------------------------------------------

Los datos y conjuntos de datos abiertos de los órganos de la Administración del Estado deberán ponerse a disposición de todas las personas, naturales o jurídicas, mediante licencias de dominio público.

A continuación se detallan las políticas específicas de licenciamiento que se aplicarán:

* **Licencia predeterminada:** En ausencia de asignación explícita, todos los conjuntos de datos emitidos por los órganos de la Administración del Estado se aperturarán bajo la licencia ***Creative Commons Zero (CC0 1.0)*****.**

|  |  |  |
| --- | --- | --- |
| **Licencia** | **Dominio** | **Descripción** |
| Creative Commons Zero (CC0 1.0) | Contenido, Datos | Renuncia a todos los derechos de autor y derechos conexos de una obra, permitiendo que sea utilizada por cualquier persona para cualquier propósito sin restricciones, situándose en el dominio público." |

* **Licencia para conjunto de datos:** Según las necesidades específicas y características de cada conjunto de datos, los órganos de la Administración del Estado podrán optar por licenciar los datos bajo cualquiera de las siguientes licencias alternativas, según se detalla en la lista predeterminada:

|  |  |  |
| --- | --- | --- |
| **Licencia** | **Dominio** | **Descripción** |
| Open Data Commons Public Domain Dedication and Licence (PDDL-1.0) | Datos | Permite a cualquier persona utilizar, modificar y distribuir los datos de manera libre y sin ninguna restricción. |
| Creative Commons Attribution 4.0 (CC-BY-4.0) | Contenido, Datos | Permite a terceros copiar, distribuir, exhibir y ejecutar obras derivadas con la condición de dar crédito al creador original de manera adecuada. |
| Open Data Commons Attribution License (ODC-By-1.0) | Datos | Permite la copia, distribución, y uso de los conjuntos de datos en nuevos productos o aplicaciones siempre que se de atribución al autor de los datos. |

Sin perjuicio de lo anterior, en aquellos casos en que atendida la naturaleza del conjunto de datos o de todo o parte de los datos que lo componen sea necesario utilizar una licencia diferente, la entidad correspondiente deberá solicitar y justificar esta situación a la Secretaría de Gobierno Digital.

[¶](#catálogos-de-datos-abiertos-institucionales) **CATÁLOGOS DE DATOS ABIERTOS INSTITUCIONALES**
-------------------------------------------------------------------------------------------------

Adicionalmente a los estantes y directrices técnicas establecidas anteriormente, los órganos de la Administración del Estado que dispongan de un portal o plataforma de datos abiertos institucional deberán:

* Asegurar que el acceso a los datos abiertos sea inmediato, sin requisitos adicionales de registro o identificación;
* Contener un listado completo, ordenado y clasificado de todos los conjuntos de datos abiertos disponibles.
* Facilitar la navegación, búsqueda y consulta efectiva dentro del repositorio, implementando todas las funcionalidades requeridas como navegación, búsqueda de texto y lenguaje de consulta.
* Mantener la operatividad del portal o plataforma, asegurando la disponibilidad continua y analizando las estadísticas de uso para mejorar el servicio.
* Proveer APIs que faciliten tanto la captura como la utilización de los conjuntos de datos abiertos por usuarios finales y su integración en el Portal Nacional de Datos Abiertos.