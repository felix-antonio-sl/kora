---
title: "Guía Técnica de Metadatos para Documentos y Expedientes Electrónicos"
url: "https://wikiguias.digital.gob.cl/guias/Metadatos_Expediente_Electr%C3%B3nico"
category: "Lineamientos Técnicos/Guías"
tags: [{'tag': 'expediente electrónico', 'title': 'expediente electrónico'}, {'tag': 'guía técnica', 'title': 'guía técnica'}, {'tag': 'metadatos', 'title': 'metadatos'}]
description: "Metadatos obligatorios, condicionales y sugeridos para la gestión e interoperabilidad de documentos y expedientes electrónicos de los órganos de la Administración del Estado."
updated_at: "2025-10-07T21:18:48.902Z"
---

> **Norma Técnica:** Documentos y Expedientes Electrónicos  
> **Versión BORRADOR**

[¶](#introducción) Introducción
-------------------------------

La ley N° 21.180 de Transformación Digital del Estado, del año 2019, modificó la ley N° 19.880 para incorporar la digitalización y transformación del ciclo de los procedimientos administrativos. La misma ley N° 21.180 encomendó a un reglamento la regulación de una serie de temas específicos, lo que se materializó mediante el decreto supremo N° 4. de 2020, del Ministerio Secretaría General de la Presidencia, que regula la forma en que los procedimientos administrativos deberán expresarse a través de medios electrónicos.

El reglamento dispuso la dictación de seis normas técnicas sobre interoperabilidad, seguridad de la información y ciberseguridad, documentos y expedientes electrónicos, notificaciones, calidad y funcionamiento, y de autenticación.

Con fecha 17 de agosto de 2023 se publicó el decreto supremo N° 10, del Ministerio Secretaría General de la Presidencia, que establece norma técnica de documentos y expedientes electrónicos para la gestión de procedimientos administrativos. Para efectos de facilitar su implementación, la presente guía técnica define los metadatos para los documentos y expedientes electrónicos gestionados por los organismos de la Administración del Estado para la tramitación de sus procedimientos administrativos.

Para la correcta interpretación de la presente guía técnica se debe seguir lo establecido en la Norma Técnica de Documentos y Expedientes Electrónicos para la Gestión de Procedimientos Administrativos. El artículo 2° de la Norma Técnica indica las definiciones correspondientes.

Este documento se basa en buenas prácticas internacionales, como la norma ISO 15.489 sobre gestión de documentos, e ISO 23.081 sobre metadatos para la gestión de documentos. Las normas ISO, en tanto marco de referencia para esta guía, sirven de fundamento para la definición, uso de los conceptos y desarrollo de la guía.

Se proyecta que versiones posteriores a la norma y a la presente guía se vayan incorporando en base al avance del cumplimiento de la Norma Técnica de Documentos y Expedientes electrónicos para la gestión de procedimientos administrativos.

[¶](#metadatos-para-la-gestión-documental-en-el-estado) Metadatos para la gestión documental en el Estado
---------------------------------------------------------------------------------------------------------

El uso de metadatos es fundamental para la descripción precisa y completa de documentos y expedientes electrónicos, permitiendo una correcta gestión y tramitación documental, favoreciendo la interoperabilidad y la eficiencia en los ciclos documentales de los procedimientos administrativos.

La descripción documental y los metadatos son elementos indivisibles de la identidad de los expedientes electrónicos y sus documentos. Estos elementos descriptivos, proporcionan información sobre la estructura, contenido y contexto de los documentos, lo que resulta de gran importancia para la accesibilidad, integridad y conservación de los expedientes. Además, los metadatos permiten la organización y búsqueda eficiente de la información contenida en los expedientes, lo que facilita la identificación precisa de los mismos y una gestión de la información más efectiva en los sistemas institucionales.

Todo documento y expediente electrónico requiere un conjunto de información que permita su descripción. Los metadatos hacen referencia tanto al documento en sí como a su contexto, abarcando las circunstancias en que se creó (como su autor, fecha y lugar), su estructura (protocolos de representación de datos e información para reconstruir el documento a partir de sus partes), y su contenido o partes. El objetivo que conlleva la utilización de metadatos es garantizar la disponibilidad, recuperación, accesibilidad, conservación e interoperabilidad del documento con otros sistemas de información.  
  
La presente definición de metadatos para la gestión documental del Estado se elaboró  en base al trabajo realizado por la mesa de expertos de diversas instituciones del Estado, que se conformó para la elaboración de la Norma Técnica de Documentos y Expedientes Electrónicos. En ella  se consideraron los siguientes estándares y normas ISO (*International Organization for Standardization*):

**1.ISO 15.489**[**[1]**](#_ftn1)**:** se enfoca en los ámbitos de información y gestión de documentos, y proporciona un marco de referencia para normalizar los procedimientos y prácticas de la gestión documental y archivos. El objetivo de la norma es asegurar la protección de los documentos y permitir una recuperación normalizada y eficaz de la información contenida en ellos.

**2. ISO 23.081**[**[2]**](#_ftn2)**:** establece las mejores prácticas para comprender, implementar y utilizar metadatos en el marco de la norma ISO 15.489. Esta norma establece un marco para la creación, gestión y uso de metadatos en la gestión de documentos, y proporciona orientación sobre los principios que deben regir en su implementación. Además, la norma proporciona elementos para la implantación y evaluación de los conjuntos de metadatos existentes, así como para sus futuras actualizaciones.

Durante el ciclo de gestión documental, a medida que el documento avanza por las diferentes etapas del procedimiento administrativo, se incorporan diferentes tipos de metadatos. Por ende, es fundamental incluirlos desde el momento de su creación y durante su gestión en las actividades de resguardo y preservación institucional, y en la preparación de su transferencia para su resguardo permanente, siguiendo las directrices del Archivo Nacional[[3]](#_ftn3).

[¶](#h-3-metadatos-de-expedientes-y-documentos-electrónicos) 3. Metadatos de expedientes y documentos electrónicos
------------------------------------------------------------------------------------------------------------------

En esta sección se presentan los metadatos obligatorios, condicionales y sugeridos, asociados a un expediente o un documento electrónico para la tramitación de un procedimiento administrativo.

Es importante destacar que los metadatos presentados son solo la base necesaria para asegurar su descripción e interoperabilidad, pero cada organismo podría evaluar la necesidad de incorporar información adicional relativa a procesos o políticas internas. Esto significa que, dependiendo de las necesidades específicas de cada institución, podrán incorporarse los metadatos sugeridos o algunos nuevos que cubran niveles descriptivos más amplios o específicos, de acuerdo con los procesos de cada organismo.

En esta sección se presenta el esquema completo de metadatos, identificando los obligatorios, condicionales y sugeridos. Los metadatos para expedientes se estructuran en ocho grupos, y los de documentos en diez.

![](/imagenes/grupo_de_metadatos.png)

Grupos de Metadatos

Esta estructura de metadatos considera varios de los conceptos utilizados por el Archivo Nacional de Australia (*Australian Government Recordkeeping Metadata Standard*) y el Esquema de Metadatos para la Gestión del Documento Electrónico (e-EMGDE) de España, a los cuales se le han incorporado adicionalmente los requerimientos que establece la Norma Técnica de Documentos y Expedientes Electrónicos y nuestra legislación vigente.

La estructura de metadatos presenta un modelo entidad-relación, considerando las siguientes entidades:

1. **Documento**
2. **Expediente**
3. **Actor**: institución, persona física o jurídica responsable o involucrada en la creación, producción, custodia o gestión de documentos.
4. **Relación**: asociación entre dos o más entidades que tiene relevancia en un contexto de gestión del documento o expediente.

Es por ello que se presentan opciones de secciones de metadatos múltiples, que permiten la incorporación de relaciones múltiples entre un expediente/documento y distintos actores.

Los organismos deben considerar que los metadatos están destinados a ser de registro permanente, en cuanto exista el expediente o documento electrónico en resguardo o custodia institucional y su posterior preservación a largo plazo en el Archivo Nacional. Esto significa que deben conservarse en las plataformas utilizadas para ese efecto, sin sobrescribirse, resguardados por el organismo responsable de su custodia.

Cada institución podrá disponer la forma en que implementará el registro de los metadatos. Por ejemplo, utilizando estructuras en repositorios documentales, bases de datos u otra solución que ofrezcan sus plataformas de gestión institucional. Sí es obligatoria la existencia de estos metadatos asociados a cada documento y expediente en resguardo institucional, y su generación en formato estandarizado cuando se interopere un documento o expediente.

El esquema de metadatos consta de 29 elementos para expedientes y 46 para documentos. Por tipo de incorporación, se dividen en:

1. **Obligatorios** (esenciales): 18 elementos para expedientes y 12 para documentos.
2. **Condicionales** (su uso depende del tipo de documento o expediente que se esté describiendo y su contexto): 5 elementos para expedientes y 16 para documentos.
3. **Sugeridos** (Pueden utilizarse bajo circunstancias en que se requiera una descripción más detallada): 6 elementos para expedientes y 18 elementos para documentos.

### [¶](#h-31-metadatos-para-expedientes-electrónicos) 3.1. Metadatos para expedientes electrónicos

La siguiente lista de metadatos contiene los campos para asociar a un expediente electrónico. Están agrupados por grupos de temática de los metadatos y se especifica una descripción básica para cada uno de ellos:

* **Codificación**: identificación estandarizada del metadato, requerida para la interoperabilidad de un expediente.
* **Numeral**: secuencia de metadato.
* **Grupo:**  agrupación de metadatos de acuerdo con su tipo.
* **Rótulo**: nombre del metadato específico.
* **Definición:** descripción del grupo o metadato específico.

Se marcan con el fondo de color los distintos tipos de metadatos:

* **Verde**: metadatos obligatorios, que deben incorporarse en toda creación del conjunto de metadatos asociados a un expediente.
* **Amarillo**: metadatos condicionales que deben incorporarse obligatoriamente siempre y cuando se cumpla una condición indicada en la ficha de especificaciones de cada metadato (ver [sección 3.3](https://docs.google.com/document/d/1kPbp3MJmIpnvgVSrBgea_aVuIb3Ssq6_/edit?pli=1#heading=h.6qte9o6xof5u)).
* **Blanco**: metadatos sugeridos. Son propuestas de uso de metadatos complementarios que permitan una completa clasificación y descripción del expediente. Cada organismo debe discernir si su uso es pertinente para la práctica institucional.

Al costado derecho se marcan explícitamente los metadatos con características específicas:

* **AN**: Metadato requerido obligatoriamente por parte del Archivo Nacional para el proceso de transferencia digital.
* **MU**: Metadato de carácter múltiple; pueden incorporarse múltiples registros de este campo, que irán describiendo relaciones o tipos con múltiples actores.

En la [sección 3.3](#_heading=h.6qte9o6xof5u)se presentan los cuadros descriptivos con especificaciones de cada metadato.

Tabla 1. Metadatos para expedientes electrónicos

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | **Codificación** | | **N°** | **Sub N°** | **Grupo/Rótulo** | **Definición** |  |  |
| **1** | **Identificación** | | | | | Información de identificación unívoca del documento. |
| 1 | MGDEE1\_1 | 1 | 1.1 | Identificador de expediente | Número único (ID) que se asigna automáticamente a un expediente registrado en un sistema de gestión documental. | **AN** |
| 2 | MGDEE1\_2 | 1 | 1.2 | Código serie | Código serie del cuadro de clasificación documental definido por el OAE. |  |
| 3 | MGDEE1\_3 | 1 | 1.3 | Número del expediente | Corresponde al número de orden interno dentro de una serie documental. |
| 4 | MGDEE1\_4 | 1 | 1.4 | Estado | Identifica el estado de generación del  expediente por parte del OAE productor. |
| 5 | MGDEE1\_5 | 1 | 1.5 | Título del expediente | Palabra, frase o grupo de caracteres que se utiliza para denominar el expediente con el que se está trabajando. Puede ser formal o atribuido. | **AN** |
| **2** | **Descripción** | | | | | Texto referencial asociado al contenido global del expediente. |  |
| 6 | MGDEE2\_1 | 2 | 2.1 | Resumen | Relato sintético que da cuenta del contenido global del expediente. |
| 7 | MGDEE2\_2 | 2 | 2.2 | Asunto del expediente | Materia o tema que trata una unidad documental y/o expediente, y que es reflejo de los fines u objetivos perseguidos con su conformación. | **AN** |
| **3** | **Temporalidad** | | | | | Atributos de temporalidad específicos asociados al expediente electrónico. |  |
| 8 | MGDEE3\_1 | 3 | 3.1 | Fecha de creación | Fecha en la que es generado el expediente. | **AN** |
| 9 | MGDEE3\_2 | 3 | 3.2 | Fecha de finalización | Fecha de finalización o cierre del expediente. | **AN** |
| **4** | **Caracterización documental** | | | | | Identificación específica por tipo de expediente. |  |
| 10 | MGDEE4\_1 | 4 | 4.1 | Mecanismo de incorporación de expediente | Identificación del mecanismo a través del cual se incorporó al sistema de gestión documental institucional. |
| 11 | MGDEE4\_2 | 4 | 4.2 | URI de expediente | Enlace a expediente almacenado en repositorio documental o plataforma estandarizada. |
| **5** | **Relaciones** | | | | | Identificación de las relaciones existentes de este expediente con OAE o personas. |
| **5.1** | OAE Asociado | | | | | Identificación de relaciones específicas del documento con OAE. |
| 12 | MGDEE51\_1 | 5 | 5.1.1 | Código de OAE productor | Identificación del OAE que, en el cumplimiento de sus funciones, genera el expediente. | **AN** |
| 13 | MGDEE51\_2 | 5 | 5.1.2 | Nombre OAE productor | Nombre institucional, en caso que el OAE productor no esté registrado en el codificador. |  |
| 14 | MGDEE51\_3 | 5 | 5.1.3 | Tipo Relación OAE | Relación establecida entre el expediente referenciado y el OAE. | **MU** |
| 15 | MGDEE51\_4 | 5 | 5.1.4 | Código de OAE relacionado | Identificación del OAE que, en el cumplimiento de sus funciones custodia, respalda o está involucrado. | **MU** |
| 16 | MGDEE51\_5 | 5 | 5.1.5 | Nombre OAE relacionado | Nombre institucional, en caso que sea el OAE productor que no esté registrado en el codificador. | **MU** |
| **5.2** | Otros actores | | | | | Identificación de relaciones del expediente con otros actores. |  |
| 17 | MGDEE52\_1 | 5 | 5.2.1 | Tipo de relación con otros actores | Identificación del tipo de relación existente con el actor y el expediente. | **MU** |
| 18 | MGDEE52\_2 | 5 | 5.2.2 | Tipo de actor relacionado | Identificación del tipo de actor relacionado que indicará la pertinencia del registro de identificación. | **MU** |
| 19 | MGDEE52\_3 | 5 | 5.2.3 | RUN/RUT relacionado | RUT (Rol Único Tributario) de la institución privada a la que está relacionado el presente expediente, o | **MU** |
| RUN (Número de Cédula de identidad)de la persona o Nro de pasaporte en caso de ser extranjero sin RUN. | **MU** |
| 20 | MGDEE52\_4 | 5 | 5.2.4 | Nombre del  actor relacionado | Nombre de la persona natural o jurídica sobre la que versa el expediente, si es que no se cuenta con la identificación(RUN/RUT) del actor relacionado. | **MU** |
| **5.3** | Índice de Documentos Asociados | | | | | Identificación de los expedientes o documentos asociados que forman parte del presente expediente. |  |
| 21 | MGDEE53\_1 | 5 | 5.3.1 | Identificador de Expediente/ Documento vinculado | Identificación del expediente o documento que conforma el presente expediente. | **AN** | **MU** |
| 22 | MGDEE53\_2 | 5 | 5.3.2 | Fecha de la  incorporación del expediente / documento | Se registra de forma automática, una vez que el expediente o documento se incorpora como parte del presente expediente. | **AN** | **MU** |
| **6** | **Seguridad** | | | | | Tipificación de niveles de seguridad requeridos para la gestión del expediente. |  |  |
| 23 | MGDEE6\_1 | 6 | 6.1 | Nivel de acceso | Indicación relativa al acceso y consulta del expediente. | **AN** |
| 24 | MGDEE6\_2 | 6 | 6.2 | Fecha fin restricción | Es la fecha que determina el desbloqueo del expediente. |  |
| 25 | MGDEE6\_3 | 6 | 6.3 | Texto Advertencia | Es el texto que se debe presentar en caso que un usuario quiera acceder a esta información. |
| 26 | MGDEE6\_4 | 6 | 6.4 | Información de carácter sensible y/o privada | Identificación sobre la información de carácter sensible contenida en el expediente. |
| **7** | **Procedimiento administrativo asociado** | | | | | Identificación del Procedimiento Administrativo y expediente electrónico. |
| 27 | MGDEE7\_1 | 7 | 7.1 | Código CPAT asociado | Código identificador  del procedimiento administrativo de CPAT |
| 28 | MGDEE7\_2 | 7 | 7.2 | Nombre de procedimiento administrativo asociado | Nombre del procedimiento administrativo, en caso de no encontrarse incorporado a CPAT. |
| **8** | **Versión** | | | | | Identificación de la versión. |
| 29 | MGDEE8\_1 | 8 | 8.1 | Versión MDGEE | Identifica la versión del esquema utilizado. |

### [¶](#h-32-metadatos-para-documentos-electrónicos) 3.2. Metadatos para documentos electrónicos

La siguiente lista de metadatos contiene los campos para asociar a un documento electrónico. Están agrupados por grupos de temática de los metadatos y se especifica una descripción básica para cada uno de ellos:

* **Codificación**: identificación estandarizada del metadato, requerida para la interoperabilidad de un expediente.
* **Numeral**: secuencia de metadato.
* **Grupo**: agrupación de metadatos de acuerdo con su tipo.
* **Rótulo**: nombre del metadato específico.
* **Definición**: descripción del grupo o metadato específico.

Se marcan con el fondo de color los distintos tipos de metadatos:

* **Verde**: metadatos obligatorios, que deben incorporarse en toda creación del conjunto de metadatos asociados a un expediente.
* **Amarillo**: metadatos condicionales que deben incorporarse obligatoriamente siempre y cuando se cumpla una condición indicada en la ficha de especificaciones de cada metadato (ver [sección 3.4](#_heading=h.26in1rg)).
* **Blanco**: metadatos sugeridos. Son propuestas de uso de metadatos complementarios que permitan una completa clasificación y descripción del expediente, pero que cada OAE debe discernir si son pertinentes su uso para la práctica institucional.

Al costado derecho se marcan explícitamente los metadatos con características específicas:

* **AN**: Metadato requerido obligatoriamente por parte del Archivo Nacional para un proceso de transferencia digital.
* **MU**: Metadato de carácter múltiple; pueden incorporarse múltiples registros de este campo, que irán describiendo relaciones o tipos con múltiples actores.

En la [sección 3.4](#_heading=h.26in1rg)se presentan los cuadros descriptivos de detalle de cada metadato.

Tabla 2. Metadatos para documentos electrónicos

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Codificación** | | | | **N°** | **Sub N°** | **Grupo/Rótulo** | **Definición** |  |  |
| **1** | | **Identificación** | | | | | Información de identificación unívoca del documento. |
| 1 | MGDDE1\_1 | 1 | 1.1 | Identificador | Código único que se debe asignar automáticamente a un documento registrado en el sistema. | **AN** |
| 2 | MGDDE1\_2 | 1 | 1.2 | Código serie | Código serie del documento,  considerando el cuadro de clasificación del OAE. | **AN** |
| 3 | MGDDE1\_3 | 1 | 1.3 | Número del documento | Corresponde al número de orden interno dentro de una serie documental. Este número de orden es recursivo y aplica tanto a documento como a expediente. |  |
| 4 | MGDDE1\_4 | 1 | 1.4 | Estado | Identifica el estado de generación del  documento por parte de la institución productora. |
| 5 | MGDDE1\_5 | 1 | 1.5 | Versión | Identificación del número de versión del documento. |
| 6 | MGDDE1\_6 | 1 | 1.6 | Título del documento | Consiste en una palabra, frase o grupo de caracteres que se utiliza para denominar el documento con el que se está trabajando y perteneciente al expediente. Puede ser formal o atribuido. | **AN** |
| 7 | MGDDE1\_7 | 1 | 1.7 | Resolución de captura | Nivel de resolución de la imagen, en caso de tratarse de una microforma. | **AN** |
| 8 | MGDDE1\_8 | 1 | 1.8 | Nombre archivo asociado | Nombre del archivo digital referenciado (documentos). |  |
| **2** | | **Características Técnicas** | | | | | Caracterización de documento. |
| 9 | MGDDE2\_1 | 2 | 2.1 | Tamaño | Volumen del documento estimado en Kb. |
| 10 | MGDDE2\_2 | 2 | 2.2 | Cantidad de páginas o extensión | Cantidad de páginas del documento o extensión del recurso digital. | **AN** |
| 11 | MGDDE2\_3 | 2 | 2.3 | Formato | Estructura utilizada para la transferencia, la conservación y la presentación de los datos. Corresponde a la extensión del archivo electrónico. |  |
| 12 | MGDDE2\_4 | 2 | 2.4 | Nombre y Versión del software | Identificación de la versión del programa informático que se utilizó para la generación del documento. |
| **3** | | **Descripción** | | | | | Texto referencial asociado al contenido del documento. |
| 13 | MGDDE3\_1 | 3 | 3.1 | Resumen | Relato sintético que da cuenta del contenido global del recurso. |
| 14 | MGDDE3\_2 | 3 | 3.2 | Palabras claves del documento | Materia o tema de que trata el documento y que son reflejo de los fines u objetivos perseguidos con su redacción. | **AN** |
| 15 | MGDDE3\_3 | 3 | 3.3 | Idioma | Identificación del idioma en que se encuentra generado el documento. |  |
| 16 | MGDDE3\_4 | 3 | 3.4 | Comunas | Identificación geográfica del origen/residencia del OAE que resguarda el documento. |
| **4** | | **Temporalidad** | | | | | Atributos de temporalidad específicos asociados a la creación del documento. |
| 17 | MGDDE4\_1 | 4 | 4.1 | Fecha de creación | Fecha en la que es generado el documento. | **AN** |
| 18 | MGDDE4\_2 | 4 | 4.2 | Fecha de modificación | Fecha de la última modificación del documento. |  |
| 19 | MGDDE4\_3 | 4 | 4.3 | Fecha de captura | Fecha en la cual el documento se incorpora al repositorio documental. Corresponde a aquellos documentos no generados internamente, ya sea que se reciben digitalmente, o que son digitalizados desde el formato físico (microforma). | **AN** |
| 20 | MGDDE4\_4 | 4 | 4.4 | Cobertura temporal | Tiempo (fechas) al que hace referencia el acto del documento. |  |
| **5** | | **Caracterización documental** | | | | | Identificación específica por tipo de documento. |
| 21 | MGDDE5\_1 | 5 | 5.1 | Tipo documental | Corresponde al nombre y/o código del tipo documental oficial  estandarizado. |
| 22 | MGDDE5\_2 | 5 | 5.2 | Origen del documento | Caracterización del origen de adopción del documento. | **AN** |
| 23 | MGDDE5\_3 | 5 | 5.3 | Mecanismo de incorporación | Expresa el mecanismo de incorporación al repositorio documental, ya sea manual, carga masiva mediante servicios web, mixto u otro. |  |
| 24 | MGDDE5\_4 | 5 | 5.4 | URI documento externo | Enlace a documento y/o recurso  residente en repositorio externo. |
| 25 | MGDDE5\_5 | 5 | 5.5 | Ubicación física del documento referenciado | Código almacenamiento físico en el archivo institucional, que permita identificar y obtener su ubicación en él (registro electrónico de documento físico) |
| 26 | MGDDE5\_6 | 5 | 5.6 | Estado de conservación microforma. | Descripción del estado del documento original a partir del cual se generó la microforma. | **AN** |
| 27 | MGDDE5\_7 | 5 | 5.7 | Disposición | Destino planificado del documento bajo una normativa o cuerpo legal, resolución u oficio, que es consecuencia del proceso de valoración documental. |  |
| **6** | | **Relaciones** | | | | | Identificación de las relaciones existentes de este documento con otros documentos, instituciones, ciudadanos o empresas. |  |
| **6.1** | | OAE Asociada | | | | | Identificación de relaciones específicas del documento con OAE. |  |
| 28 | MGDDE61\_1 | 6 | 6.1.1 | Código OAE | Identificación del OAE que, en el cumplimiento de sus funciones, genera, gestiona o custodia el documento. | **AN** | **MU** |
| 29 | MGDDE61\_2 | 6 | 6.1.2 | Nombre OAE | Nombre institucional, en caso que no se cuente con el código de identificación de la OAE relacionado |  | **MU** |
| 30 | MGDDE61\_3 | 6 | 6.1.3 | Tipo de relación entre documento y OAE | Relación establecida entre el documento referenciado y el OAE (gestionador, autor institucional o custodia) | **AN** | **MU** |
| **6.2** | | Otros actores | | | | | Identificación de relaciones del documento con otros actores (persona natural o jurídica). |  |  |
| 31 | MGDDE62\_1 | 6 | 6.2.1 | Tipo de relación con otros actores | Identificación del tipo de relación existente entre el actor y el documento. | **AN** | **MU** |
| 32 | MGDDE62\_2 | 6 | 6.2.2 | Tipo de actor relacionado | Identificación del tipo de actor relacionado que indicará la pertinencia del tipo de registro de la identificación. |  | **MU** |
| 33 | MGDDE62\_3 | 6 | 6.2.3 | Identificación de actor  relacionado | RUN (Número de Cédula de identidad) de la persona o RUT (Rol Único Tributario) de la institución privada o Nro. de pasaporte en caso de ser extranjero sin RUN. | **AN** | **MU** |
| 34 | MGDDE62\_4 | 6 | 6.2.4 | Nombre del actor relacionado | Nombre de la persona natural o jurídica sobre la que versa el documento, en caso de no contar con RUN respectivo. |  | **MU** |
| **7** | | **Seguridad** | | | | | Tipificación de niveles de seguridad requeridos para la gestión del documento. |  |
| 35 | MGDDE7\_1 | 7 | 7.1 | Nivel de Acceso | Indicación relativa al acceso y consulta de los documentos. | **AN** |
| 36 | MGDDE7\_2 | 7 | 7.2 | Fecha fin restricción | Es la fecha hasta cuando se debe presentar el texto de advertencia en caso que un usuario quiera acceder a esta documentación. |  |
| 37 | MGDD7\_3 | 7 | 7.3 | Texto Advertencia | Es el texto que se debe presentar en caso que un usuario quiera acceder a esta información. |
| 38 | MGDDE7\_4 | 7 | 7.4 | Información de carácter sensible | Identificación que el documento contiene información de carácter sensible |
| **8** | | **Firma** | | | | | Identificación del tipo de firma electrónica utilizada en la generación del documento. |
| 39 | MGDD8\_1 | 8 | 8.1 | Tipo Firma | Identificación del tipo de firma electrónica utilizada en la generación del documento (avanzada, simple). | **MU** |
| 40 | MGDD8\_2 | 8 | 8.2 | Proveedor | Identificación del proveedor del servicio de firma electrónica utilizado en el documento. | **MU** |
| 41 | MGDDE8\_3 | 8 | 8.3 | Firma Electrónica Avanzada | Se indica si el documento cuenta con firma electrónica avanzada. |  |
| **8.4** | | Firmantes | | | | |  |  |
| 42 | MGDDE84\_1 | 8 | 8.4.1 | Nombre/Cargo Representación | Identificación del nombre de la persona que firma y cargo asociado. | **MU** |
| 43 | MGDDE84\_2 | 8 | 8.4.2 | RUN firmante | Identificación de la persona que firma el documento. | **MU** |
| **9** | | **Procedimiento Administrativo Asociado** | | | | | Identificación del PAT asociado a la generación del presente documento. |  |
| 44 | MGDDE9\_1 | 9 | 9.1 | Código Procedimiento Administrativo asociado | Código identificador del procedimiento administrativo asociado a la creación del documento(CPAT). |
| 45 | MGDDE9\_2 | 9 | 9.2 | Nombre procedimiento administrativo asociado | Nombre del trámite asociado, en caso que no se cuente con el código CPAT |
| **10** | | **Versión** | | | | |  |
|  | 46 | | MGDDE10 | 10 | 10.1 | **Versión MGDDE** | Identifica la versión  del esquema utilizado. |
|  |  |  |  |  |  |  |  |  |  |

### [¶](#h-33-especificaciones-de-metadatos-para-expedientes-electrónicos) 3.3. Especificaciones de metadatos para expedientes electrónicos

A continuación se detallan los metadatos obligatorios, condicionales y sugeridos para los expedientes electrónicos. Cada ficha contiene información relevante, como el código de metadato, definición, obligatoriedad de uso, la forma de ingreso de la información, así como aspectos importantes para la correcta gestión, disponibilidad y preservación de los expedientes electrónicos.

#### [¶](#identificador) Identificador

| **1** | **Identificador de expediente** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE1\_1 | | | |
| N° Grupo | 1. Identificación | | | |
| Sub N° | 1.1 | | | |
| Definición | Código único (ID) institucional que se asigna automáticamente a un expediente registrado en un sistema de gestión documental o repositorio documental. | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Automático |
| Transferencia AN | SI | Repetible | | NO |
| Forma de ingreso | Se completa de forma automática por el sistema, que debe asignar a cada expediente creado un número único institucional que permitirá acceder al expediente específico cuando se requiera. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Alfanumérico | |
| Por defecto | |  | |
| Comentarios | Asegurar unicidad, persistencia y estandarización de la codificación. | | | |
| Ejemplo | EXP-20230925-001 | | | |
|  |  |  |  |  |

| **2** | **Código serie** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE1\_2 | | | |
| N° Grupo | 1. Identificación | | | |
| Sub N° | 1.2 | | | |
| Definición | Código de serie definido en el cuadro de clasificación documental del OAE. | | | |
| Obligación | **Sugerido** | Modo de ingreso | | Automático |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Se completa de forma automática por el sistema, que debe asignar a cada expediente creado un número. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Alfanumérico | |
| Por defecto | |  | |
| Comentarios |  | | | |
| Ejemplo |  | | | |
|  |  |  |  |  |

| **3** | **Número de expediente** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE1\_3 | | | |
| N° Grupo | 1. Identificación | | | |
| Sub N° | 1.3 | | | |
| Definición | Corresponde al número de orden interno dentro de una serie documental. | | | |
| Obligación | **Sugerido** | Modo de ingreso | | Automático |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Se completa de forma automática por el sistema, que debe asignar a cada expediente creado un número institucional que permitirá acceder al expediente específico cuando se requiera. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Alfanumérico | |
| Por defecto | |  | |
| Comentarios |  | | | |
| Ejemplo |  | | | |
|  |  |  |  |  |

| **4** | **Estado** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE1\_4 | | | |
| N° Grupo | 1. Identificación | | | |
| Sub N° | 1.1 | | | |
| Definición | Identifica el estado del proceso del expediente por parte del OAE productor, asociado a las fases del ciclo de vida de un expediente electrónico o de su gestión institucional. | | | |
| Obligación | **Sugerido** | Modo de ingreso | | Automático |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Puede generarse de forma automática y/o manual. | | | |
| Valores | Valor de ingreso | | - | |
| Tipo dato | | Alfanumérico | |
| Por defecto | | - | |
| Comentarios | El estado es un registro del proceso,puede referirse al estado de su creación o la fase de vida del expediente. | | | |
| Ejemplo |  | | | |
|  |  |  |  |  |

| **5** | **Título del Expediente** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE1\_5 | | | |
| N° Grupo | 1. Identificación | | | |
| Sub N° | 1.5 | | | |
| Definición | Palabra, frase o grupo de caracteres que se utiliza para denominar el expediente con el que se está trabajando. Puede ser formal o atribuido. | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Manual |
| Transferencia AN | SI | Repetible | | NO |
| Forma de ingreso | Puede generarse de forma automática y/o manual. El título formal es el título adjudicado por quien genera el expediente al momento de su creación. Este título puede ser automatizable al momento de creación del expediente asociado a un procedimiento administrativo. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Texto | |
| Por defecto | |  | |
| Comentarios | Destinar el uso de mayúsculas únicamente para el inicio del título y para nombres propios. | | | |
| Ejemplo | Asignación de presupuesto para compra de insumos. | | | |
|  |  |  |  |  |

| **6** | **Resumen** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE2\_1 | | | |
| N° Grupo | 2. Descripción | | | |
| Sub N° | 2.1 | | | |
| Definición | Relato sintético que da cuenta del contenido global del expediente. | | | |
| Obligación | **Sugerido** | Modo de ingreso | | Manual |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso |  | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Texto | |
| Por defecto | |  | |
| Comentarios |  | | | |
| Ejemplo |  | | | |
|  |  |  |  |  |

| **7** | **Asunto del expediente** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE2\_2 | | | |
| N° Grupo | 2. Descripción | | | |
| Sub N° | 2.2 | | | |
| Definición | Materia o tema de que trata el expediente, y que es reflejo de los fines u objetivos perseguidos con la tramitación asociada. | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Manual |
| Transferencia AN | SI | Repetible | | NO |
| Forma de ingreso | Se ingresa de forma manual y/o desde un vocabulario controlado. Se utiliza cuando la materia sobre la que versa el acto administrativo es relevante de destacar y esa información no puede ser extraída de los otros metadatos existentes en el registro (ya sea de esta lista o los propios de la gestión documental de cada OAE). | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Texto | |
| Por defecto | |  | |
| Comentarios | Este dato es un ámbito amplio que representa el contenido del expediente. | | | |
| Ejemplo | Compra de insumos tecnológicos para el año 2023. | | | |
|  |  |  |  |  |

| **8** | **Fecha de creación** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE3\_1 | | | |
| N° Grupo | 3. Temporalidad | | | |
| Sub N° | 3.1 | | | |
| Definición | Fecha en la que es generado el expediente. | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Automático |
| Transferencia AN | SI | Repetible | | NO |
| Forma de ingreso | Se genera automáticamente, según formato aaaa-mm-dd hh:mm:ss (ISO 8601). | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Formato aaaa-mm-dd hh:mm:ss (ISO 8601) | |
| Por defecto | | – | |
| Comentarios | Debe tener posibilidad de ser modificado, pero dicho cambio debe quedar registrado. | | | |
| Ejemplo | 2023-20-10:11:56:57 | | | |
|  |  |  |  |  |

| **9** | **Fecha de finalización** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE3\_2 | | | |
| N° Grupo | 3. Temporalidad | | | |
| Sub N° | 3.2 | | | |
| Definición | Fecha de finalización o cierre del expediente. | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Automático |
| Transferencia AN | SI | Repetible | | NO |
| Forma de ingreso | Se genera automáticamente, según formato aaaa-mm-dd hh:mm:ss (ISO 8601) | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Formato aaaa-mm-dd hh:mm:ss (ISO 8601) | |
| Por defecto | | – | |
| Comentarios | Debe tener posibilidad de ser modificado, pero dicho cambio debe quedar registrado. | | | |
| Ejemplo | 2023-20-11:16:56:57 | | | |
|  |  |  |  |  |

| **10** | **Mecanismos de incorporación del expediente** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE4\_1 | | | |
| N° | 4 | | | |
| Sub N° | 4.1 | | | |
| Definición | Expresa el mecanismo de incorporación de uno o más expedientes electrónicos al sistema de gestión documental institucional, ya sea manual, carga masiva mediante servicios web, mixto u otro. | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Automático/manual |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Lista MGDDE5\_3 | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Texto | |
| Por defecto | | 1 | |
| Comentarios | - | | | |
| Ejemplo | 1 (Incorporación manual) | | | |
|  |  |  |  |  |

| **11** | **URI de expediente** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE4\_2 | | | |
| N° Grupo | 4. Caracterización documental | | | |
| Sub N° | 4.2 | | | |
| Definición | Enlace a expediente almacenado en repositorio documental o plataforma estandarizada. | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Automático |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Se genera automáticamente por la plataforma. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | URI | |
| Por defecto | | – | |
| Comentarios | La institución podrá hacer uso de sus propios servicios de URIs persistentes y/o utilizar la plataforma de URIs persistente que el Estado disponga. | | | |
| Ejemplo | https://dominio-institución/servicio-persistente/20.500.13034/401 | | | |
|  |  |  |  |  |

| **12** | **Código de OAE productor** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE51\_1 | | | |
| N° Grupo | 5. Relaciones | OAE Asociado | | | |
| Sub N° | 5.1.1 | | | |
| Definición | Identificación del OAE que, en el cumplimiento de sus funciones, genera y/o gestiona los expedientes que son parte de su sistema de gestión de documentos y expedientes y formarán parte de su archivo. | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Automático |
| Transferencia AN | SI | Repetible | | NO |
| Forma de ingreso | Se genera automáticamente. Cada sistema debe incorporar el código y el nombre del productor. Este código debe corresponder a la codificación institucional proveída por el Gestor de Códigos (GESCODE). | | | |
| Valores | Valor de ingreso | | GESCODE | |
| Tipo dato | | Numérico | |
| Por defecto | | – | |
| Comentarios | La identificación del OAE generador es un valor requerido por AN. | | | |
| Ejemplo | 46 (Gobierno Regional de la Región de La Araucanía) | | | |
|  |  |  |  |  |

| **13** | **Nombre OAE productor** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE51\_2 | | | |
| N° Grupo | 5. Relaciones | OAE Asociado | | | |
| Sub N° | 5.1.2 | | | |
| Definición | Nombre institucional, en caso que el OAE productor no esté registrado en el codificador o la OAE decida almacenarlo para uso directo. | | | |
| Obligación | Condicional | Modo de ingreso | | Automático/manual |
| Transferencia AN | SI | Repetible | | NO |
| Forma de ingreso | Se genera manualmente en caso de no existir en el Gestor de Códigos (GESCODE) de SGD. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Texto | |
| Por defecto | |  | |
| Comentarios |  | | | |
| Ejemplo | Gobierno Regional de la Región de La Araucanía | | | |
|  |  |  |  |  |

| **14** | **Tipo de relación OAE** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE51\_3 | | | |
| N° Grupo | 5. Relaciones | OAE Asociado | | | |
| Sub N° | 5.1.3 | | | |
| Definición | Relación establecida entre el expediente referenciado y el OAE. | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Automático/manual |
| Transferencia AN | NO | Repetible | | SI |
| Forma de ingreso | Se genera automáticamente en base la lista predefinida de relaciones (ver [sección 4.](#_heading=h.1ksv4uv) lista N° 4). | | | |
| Valores | Valor de ingreso | | Servicio Codificador del Estado | |
| Tipo dato | | Numérico | |
| Por defecto | | 1 (custodia) | |
| Comentarios | Es obligatorio al menos identificar el OAE responsable de la custodia del expediente. | | | |
| Ejemplo | 1 (Custodia) | | | |
|  |  |  |  |  |

| **15** | **Código de OAE relacionado** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE51\_4 | | | |
| N° Grupo | 5. Relaciones | OAE Asociado | | | |
| Sub N° | 5.1.4 | | | |
| Definición | Identificación del OAE que, en el cumplimiento de sus funciones, custodia, gestiona o respalda el expediente. | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Automático/Manual |
| Transferencia AN | NO | Repetible | | SI |
| Forma de ingreso | Este código debe corresponder a la codificación institucional proveída por el Gestor de Códigos      (GESCODE). | | | |
| Valores | Valor de ingreso | | GESCODE | |
| Tipo dato | | Numérico | |
| Por defecto | | – | |
| Comentarios | Es obligatorio al menos identificar el OAE responsable de la custodia del expediente. | | | |
| Ejemplo | 46 (Gobierno Regional de la Región de La Araucanía) | | | |
|  |  |  |  |  |

| **16** | **Nombre de OAE relacionado** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE51\_5 | | | |
| N° Grupo | 5. Relaciones | OAE Asociado | | | |
| Sub N° | 5.1.5 | | | |
| Definición | Nombre institucional, en caso que el OAE productor no esté registrado en el Gestor de Códigos      (GESCODE). | | | |
| Obligación | Condicional | Modo de ingreso | | Automático/Manual |
| Transferencia AN | NO | Repetible | | SI |
| Forma de ingreso | Se debe registrar en caso de asociar a un OAE que no esté incorporado en el GESCODE. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Texto | |
| Por defecto | | – | |
| Comentarios |  | | | |
| Ejemplo | Gobierno Regional de la Región de La Araucanía | | | |
|  |  |  |  |  |

| **17** | **Tipo de relación con otros actores** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE52\_1 | | | |
| N° Grupo | 5. Relaciones | Otros actores | | | |
| Sub N° | 5.2.1 | | | |
| Definición | Identificación del tipo de relación existente con el actor (persona natural o jurídica) y el expediente.  Es obligatorio para la identificación de interesados. | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Automático/manual |
| Transferencia AN | NO | Repetible | | SI |
| Forma de ingreso | Se genera automáticamente/manual en base a una lista predefinida y el tipo de relación (ver [sección 4.](#_heading=h.1ksv4uv) lista N° 5). | | | |
| Valores | Valor de ingreso | | Servicio Codificador del Estado | |
| Tipo dato | | Numérico | |
| Por defecto | | 1 - Responsable | |
| Comentarios | Es obligatorio asignar al menor un funcionario responsable de la apertura del expediente. Al ser un campo múltiple es esperable que se incorporen los interesados u otros tipos de relaciones de personas naturales o jurídicas con el expediente. | | | |
| Ejemplo | 2 (Interesado) | | | |
|  |  |  |  |  |

| **18** | **Tipo de actor relacionado** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE52\_2 | | | |
| N° Grupo | 5. Relaciones | Otros actores | | | |
| Sub N° | 5.2.2 | | | |
| Definición | Identificación del actor relacionado (persona jurídica o natural). Es obligatorio para la identificación de interesados. | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Automático(manual) |
| Transferencia AN | NO | Repetible | | SI |
| Forma de ingreso | Identificación del tipo de actor relacionado que indicará la pertinencia del registro de identificación (ver [sección 4.](#_heading=h.1ksv4uv) lista N° 6). | | | |
| Valores | Valor de ingreso | | Servicio Codificador del Estado | |
| Tipo dato | | Numérico | |
| Por defecto | | 4 - Funcionario | |
| Comentarios | Al igual que el metadato anterior es obligatorio especificar el funcionario responsable inicial del expediente. | | | |
| Ejemplo | 1 (Ciudadano) | | | |
|  |  |  |  |  |

| **19** | **RUN/RUT Relacionado** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE52\_3 | | | |
| N° Grupo | 5. Relaciones | Otros actores | | | |
| Sub N° | 5.2.3 | | | |
| Definición | RUN (Número de Cédula de identidad) de la persona o RUT (Rol Único Tributario) de la institución privada a la que está relacionado el presente expediente o Nro Pasaporte en el caso de extranjeros.  Es obligatorio para la identificación de interesados. | | | |
| Obligación | Condicional | Modo de ingreso | | Automático/manual |
| Transferencia AN | NO | Repetible | | SI |
| Forma de ingreso | Se registra al momento de identificar al actor. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Alfanumérico | |
| Por defecto | | Formato RUN/RUT | |
| Comentarios | - | | | |
| Ejemplo | 60100003-2 | | | |
|  |  |  |  |  |

| **20** | **Nombre del    actor relacionado** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE52\_4 | | | |
| N° Grupo | 5. Relaciones | Otros actores | | | |
| Sub N° | 5.2.4 | | | |
| Definición | Nombre de la persona natural o jurídica sobre la que versa el expediente, si es que no se cuenta con la identificación del actor relacionado.  Es obligatorio para la identificación de interesados si no se cuenta con una identificación de tipo RUN/RUT. | | | |
| Obligación | Condicional | Modo de ingreso | | Automático/manual |
| Transferencia AN | NO | Repetible | | SI |
| Forma de ingreso | Se registra al momento de identificar al actor. Si es que no se cuenta con la opción de run/rut/ pasaporte se debe incorporar el nombre. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Texto | |
| Por defecto | | – | |
| Comentarios | - | | | |
| Ejemplos | Entel Chile  Julian Santelices Machuca | | | |
|  |  |  |  |  |

| **21** | **Identificación de expediente/documento vinculado** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE53\_1 | | | |
| N° Grupo | 5. Relaciones | Documentos asociados | | | |
| Sub N° | 5.3.1 | | | |
| Definición | Identificación del documento o el expediente relacionado (conformando el índice del expediente). | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Automático |
| Transferencia AN | SI | Repetible | | SI |
| Forma de ingreso | Se registra de forma automática, una vez que uno o más documentos/expedientes hayan sido incorporados al expediente. | | | |
| Valores | Valor de ingreso | | Lista controlada de identificadores de documentos/expedientes existentes en la plataforma/repositorio institucional o Uri del documento en caso de referencia a documentos/expedientes de otra OAE | |
| Tipo dato | | Alfanumérico | |
| Por defecto | | – | |
| Comentarios | Es requerido en caso que el documento forme parte de un expediente . | | | |
| Ejemplo | - | | | |
|  |  |  |  |  |

| **22** | **Fecha de la    incorporación del expediente / documento** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE53\_2 | | | |
| N° Grupo | 5. Relación | Documentos asociados | | | |
| Sub N° | 5.3.2 | | | |
| Definición | Fecha y hora de incorporación del documento o el expediente relacionado. | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Automático |
| Transferencia AN | SI | Repetible | | SI |
| Forma de ingreso | Se registra de forma automática, una vez que uno o más documentos/expedientes hayan sido incorporados al expediente. | | | |
| Valores | Valor de ingreso | | Fecha y hora en formato aaaa-mm-dd hh:mm:ss (ISO 8601) | |
| Tipo dato | | Alfanumérico | |
| Por defecto | | – | |
| Comentarios |  | | | |
| Ejemplo | 2023-20-11:16:56:57 | | | |
|  |  |  |  |  |

| **23** | **Nivel de acceso** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE6\_1 | | | |
| N° Grupo | 6. Seguridad | | | |
| Sub N° | 6.1 | | | |
| Definición | Indicación relativa al acceso y para consulta del expediente. | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Manual |
| Transferencia AN | SI | Repetible | | NO |
| Forma de ingreso | Se ingresa manualmente o también puede existir definición de asociación a un término cargado automáticamente, identificado explícitamente por tipo de expediente en la política de gestión documental institucional (ver [sección 4.](#_heading=h.1ksv4uv) lista N° 7). | | | |
| Valores | Valor de ingreso | | Servicio interoperabilidad Códigos (Gescode) | |
| Tipo dato | | Numérico | |
| Por defecto | | 1 - Público | |
| Comentarios | Codificación numérica y rótulo conocido. | | | |
| Ejemplo | 1 (acceso público) | | | |
|  |  |  |  |  |

| **24** | **Fecha fin restricción** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE6\_2 | | | |
| N° Grupo | 6. Seguridad | | | |
| Sub N° | 6.2 | | | |
| Definición | Es la fecha que determina el desbloqueo del expediente, en caso de existir. | | | |
| Obligación | Sugerido | Modo de ingreso | | Manual |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Se ingresa manualmente. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Fecha | |
| Por defecto | |  | |
| Comentarios |  | | | |
| Ejemplo |  | | | |
|  |  |  |  |  |

| **25** | **Texto de advertencia** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE6\_3 | | | |
| N° Grupo | 6. Seguridad | | | |
| Sub N° | 6.3 | | | |
| Definición | Es el texto que se debe presentar en caso que un usuario quiera acceder a esta información. | | | |
| Obligación | Sugerido | Modo de ingreso | | Manual |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Se ingresa manualmente. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Texto | |
| Por defecto | |  | |
| Comentarios |  | | | |
| Ejemplo |  | | | |
|  |  |  |  |  |

| **26** | **Información de carácter sensible y/o privado** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE6\_4 | | | |
| N° Grupo | 6. Seguridad | | | |
| Sub N° | 6.4 | | | |
| Definición | Identificación de que el expediente contiene información de carácter sensible o privada. | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Manual |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | La plataforma del OAE debe manejar un registro de marca de tipo de información sensible. | | | |
| Valores | Valor de ingreso | | Lista Controlada [1- SI  / 2 - NO] | |
| Tipo dato | | Numérico | |
| Por defecto | | 2 (NO) | |
| Comentarios | Una posibilidad que puede abordar cada OAE es identificar categorías controladas para información sensible y/o privada. | | | |
| Ejemplo | 2 | | | |
|  |  |  |  |  |

| **27** | **Código CPAT asociado** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE7\_1 | | | |
| N° Grupo | 7. Procedimiento administrativo asociado | | | |
| Sub N° | 7.1 | | | |
| Definición | Código identificador del procedimiento administrativo en el Catálogo de Procedimientos Administrativos y Tramitaciones (CPAT). | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Automático |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Código del procedimiento administrativo existente en el Catálogo de Procedimientos Administrativos y Tramitaciones del Estado (CPAT). | | | |
| Valores | Valor de ingreso | | GESCODE  Procedimientos Administrativos y Tramitaciones (CPAT) | |
| Tipo dato | | Alfanumérico | |
| Por defecto | | – | |
| Comentarios | Disponibilizado por el Catálogo de Procedimientos Administrativos y Tramitaciones (CPAT). | | | |
| Ejemplo | 5076 (PA-UNI00002-00001- Convalidación de Programa de Perfeccionamiento Académico ) | | | |
|  |  |  |  |  |

| **28** | **Nombre del procedimiento administrativo asociado** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE7\_2 | | | |
| N° Grupo | 7. Procedimiento administrativo asociado | | | |
| Sub N° | 7.2 | | | |
| Definición | Nombre del procedimiento administrativo asociado, en caso de no encontrarse incorporado al Catálogo de Procedimientos Administrativos y Tramitaciones (CPAT). | | | |
| Obligación | Condicional | Modo de ingreso | | Manual |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Nombre del procedimiento administrativo existente en el Catálogo   de Procedimientos y Tramitaciones (CPAT).  Es obligatorio en caso que el PA no se encuentre codificado en CPAT o el OAE decida registrarlo para referencia directa. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Alfanumérico | |
| Por defecto | | – | |
| Comentarios |  | | | |
| Ejemplos | Convalidación de Programa de Perfeccionamiento Académico | | | |
|  |  |  |  |  |

| **29** | **Versión MDGDEE** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDEE8\_1 | | | |
| N° | 8 | | | |
| Sub N° | 8.1 | | | |
| Definición | Identificación de la versión de la Guía Técnica de Metadatos utilizada, de acuerdo con las actualizaciones dispuestas por la Secretaría de Gobierno Digital. | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Automático |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Registro automático. | | | |
| Valores | Valor de ingreso | | Lista controlada de versiones de la guía de metadatos | |
| Tipo dato | | Numérico | |
| Por defecto | | 001 | |
| Comentarios | - | | | |
| Ejemplo | 001 | | | |
|  |  |  |  |  |

[¶](#h-34-especificaciones-de-metadatos-para-documentos-electrónicos) 3.4. Especificaciones de metadatos para documentos electrónicos
-------------------------------------------------------------------------------------------------------------------------------------

A continuación se detallan la especificación de cada uno de los metadatos obligatorios, condicionales y sugeridos para documentos electrónicos.

| **1** | **Identificador** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE1\_1 | | | |
| N° Grupo | 1. Identificación | | | |
| Sub N° | 1.1 | | | |
| Definición | Código único que se asigna automáticamente a un documento registrado en un sistema de gestión documental institucional. Este código identificador hace referencia al documento. | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Automático |
| Transferencia AN | SI | Repetible | | NO |
| Forma de ingreso | Se completa de forma automática por el sistema, que debe asignar a cada documento ingresado un código único que permitirá recuperar el documento específico cuando se requiera. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Alfanumérico | |
| Por defecto | |  | |
| Comentarios | Asegurar unicidad, persistencia y estandarización de la codificación. | | | |
| Ejemplo | DOCU-20230925-001-XYZ | | | |
|  |  |  |  |  |

| **2** | **Código de serie** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE1\_6 | | | |
| N° Grupo | 1. Identificación | | | |
| Sub N° | 1.2 | | | |
| Definición | Código serie del documento, considerando el cuadro de clasificación del OAE. | | | |
| Obligación | **Condicional** | Modo de ingreso | | Manual/automático |
| Transferencia AN | SI | Repetible | | NO |
| Forma de ingreso | Puede generarse de forma automática y/o manual.  Es obligatorio en caso de un proceso de transferencia al Archivo Nacional. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Alfanumérico | |
| Por defecto | |  | |
| Comentarios |  | | | |
| Ejemplo |  | | | |
|  |  |  |  |  |

| **3** | **Número de documento** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE1\_3 | | | |
| N° Grupo | 1. Identificación | | | |
| Sub N° | 1.3 | | | |
| Definición | Corresponde al número de orden interno dentro de una serie documental. Este número de orden es recursivo y aplica tanto a documento como a expediente. | | | |
| Obligación | Sugerido | Modo de ingreso | | Manual/automático |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Puede generarse de forma automática y/o manual. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Alfanumérico | |
| Por defecto | |  | |
| Comentarios |  | | | |
| Ejemplo |  | | | |
|  |  |  |  |  |

| **4** | **Estado** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE1\_4 | | | |
| N° Grupo | 1. Identificación | | | |
| Sub N° | 1.4 | | | |
| Definición | Identifica el estado de generación del documento por parte de la institución productora. | | | |
| Obligación | Sugerido | Modo de ingreso | | Manual/automático |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Puede generarse de forma automática y/o manual. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Alfanumérico | |
| Por defecto | |  | |
| Comentarios |  | | | |
| Ejemplo |  | | | |
|  |  |  |  |  |

| **5** | **Versión** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE1\_5 | | | |
| N° Grupo | 1. Identificación | | | |
| Sub N° | 1.5 | | | |
| Definición | Identificación del número de versión del documento. | | | |
| Obligación | Sugerido | Modo de ingreso | | Manual/automático |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Puede generarse de forma automática y/o manual. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Alfanumérico | |
| Por defecto | |  | |
| Comentarios |  | | | |
| Ejemplo | 1.1 | | | |
|  |  |  |  |  |

| **6** | **Título del documento** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE1\_6 | | | |
| N° Grupo | 1. Identificación | | | |
| Sub N° | 1.6 | | | |
| Definición | Consiste en una palabra, frase o grupo de caracteres que se utiliza para denominar el documento con el que se está trabajando. Puede ser formal o atribuido. | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Manual |
| Transferencia AN | SI | Repetible | | NO |
| Forma de ingreso | Puede generarse de forma automática y/o manual. El título formal es el título adjudicado por quien genera el documento al momento de su creación. Este título puede ser automatizable, dependiendo del tipo de documento. Cuando esto no es posible, dado que algunos tipos documentales no consideran el uso de un título (por ejemplo, una carta o correo electrónico), existen casos en que la persona responsable debe atribuir un título. Esto se realiza mediante el uso de texto libre. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Texto | |
| Por defecto | |  | |
| Comentarios | Destinar el uso de mayúsculas únicamente para el inicio del título y para nombres propios. | | | |
| Ejemplo | Resolución exenta asigna presupuesto para compra de insumos | | | |
|  |  |  |  |  |

| **7** | **Resolución de captura** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE1\_7 | | | |
| N° Grupo | 1. Identificación | | | |
| Sub N° | 1.7 | | | |
| Definición | Nivel de resolución de la imagen. | | | |
| Obligación | Condicional | Modo de ingreso | | Automático |
| Transferencia AN | SI | Repetible | | NO |
| Forma de ingreso | Se completa de forma automática. El sistema extrae la información desde los metadatos embebidos en el archivo.  Es obligatorio en caso de tratarse de un documento de tipo Microforma. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | |  | |
| Por defecto | |  | |
| Comentarios | Se refiere a la cantidad de píxeles que la imagen contiene, y se expresa como el número de píxeles en horizontal por el número de píxeles en vertical. Este metadato es obligatorio para Microformas. | | | |
| Ejemplo | 3000x2000 | | | |
|  |  |  |  |  |

| **8** | **Nombre archivo asociado** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE1\_8 | | | |
| N° Grupo | 1. Identificación | | | |
| Sub N° | 1.8 | | | |
| Definición | Nombre del archivo digital referenciado (documentos). | | | |
| Obligación | Sugerido | Modo de ingreso | | Automático |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Se completa de forma automática. El sistema extrae el nombre del archivo. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | |  | |
| Por defecto | |  | |
| Comentarios |  | | | |
| Ejemplo |  | | | |
|  |  |  |  |  |

| **9** | **Tamaño** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE2\_1 | | | |
| N° Grupo | 1. Identificación | | | |
| Sub N° | 2.1 | | | |
| Definición | Volumen del documento medido en Kb. | | | |
| Obligación | Sugerido | Modo de ingreso | | Automático |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Se completa de forma automática, el sistema extrae la información desde el archivo. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | |  | |
| Por defecto | |  | |
| Comentarios |  | | | |
| Ejemplo |  | | | |
|  |  |  |  |  |

| **10** | **Cantidad de páginas o extensión** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE2\_2 | | | |
| N° Grupo | 2. Características técnicas | | | |
| Sub N° | 2.2 | | | |
| Definición | Indica el número total de páginas que componen un documento, proporcionando información sobre la extensión del contenido. | | | |
| Obligación | **Condicional** | Modo de ingreso | | Automático |
| Transferencia AN | SI | Repetible | | NO |
| Forma de ingreso | Se completa de forma automática por el sistema, o puede ser ingresado de manera manual.  Es obligatorio en caso de tratarse de un documento de tipo Microforma. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Numérico | |
| Por defecto | |  | |
| Comentarios | - | | | |
| Ejemplo | 104 | | | |
|  |  |  |  |  |

| **11** | **Formato** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE2\_3 | | | |
| N° Grupo | 2. Características técnicas | | | |
| Sub N° | 2.3 | | | |
| Definición | Estructura utilizada para la transferencia, la conservación y la presentación de los datos. Corresponde a la extensión del archivo electrónico. | | | |
| Obligación | Sugerido | Modo de ingreso | | Automático |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Se completa de forma automática por el sistema. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Texto | |
| Por defecto | |  | |
| Comentarios | - | | | |
| Ejemplo | pdf | | | |
|  |  |  |  |  |

| **12** | **Nombre y versión del software** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE2\_4 | | | |
| N° Grupo | 2. Características técnicas | | | |
| Sub N° | 2.4 | | | |
| Definición | Identificación de la versión del programa informático que se utilizó para la generación del documento. | | | |
| Obligación | Sugerido | Modo de ingreso | | Automático |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Se completa de forma automática. El sistema extrae la información desde los metadatos embebidos en el archivo. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Texto | |
| Por defecto | |  | |
| Comentarios | - | | | |
| Ejemplo | pdf | | | |
|  |  |  |  |  |

| **13** | **Resumen** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE3\_1 | | | |
| N° Grupo | 3. Descripción | | | |
| Sub N° | 3.1 | | | |
| Definición | Relato sintético que da cuenta del contenido global del recurso. | | | |
| Obligación | Sugerido | Modo de ingreso | | Manual |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso |  | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Texto | |
| Por defecto | | – | |
| Comentarios | - | | | |
| Ejemplo |  | | | |
|  |  |  |  |  |

| **14** | **Palabras claves documento** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE3\_2 | | | |
| N° Grupo | 3. Descripción | | | |
| Sub N° | 3.2 | | | |
| Definición | Materias o temas de que trata una unidad documental, expresados a través de palabras representativas del documento y en contexto del expediente electrónico. | | | |
| Definición |  | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Manual |
| Transferencia AN | SI | Repetible | | NO |
| Forma de ingreso | Se ingresa de forma manual o mediante un selector de vocabulario controlado. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Texto | |
| Por defecto | |  | |
| Comentarios | Palabras cortas,  simples o compuestas en una frase breve, que expresen la información más relevante del contenido del documento. | | | |
| Ejemplo | Resolución de compra tecnológica - Adquisición de licencias de software | | | |
|  |  |  |  |  |

| **15** | **Idioma** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE3\_3 | | | |
| N° Grupo | 3. Descripción | | | |
| Sub N° | 3.3 | | | |
| Definición | Identificación del idioma en que se encuentra generado el documento. | | | |
| Obligación | Sugerido | Modo de ingreso | | Manual |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso |  | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Texto | |
| Por defecto | | – | |
| Comentarios | - | | | |
| Ejemplo |  | | | |
|  |  |  |  |  |

| **16** | **Comuna** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE3\_4 | | | |
| N° Grupo | 3. Descripción | | | |
| Sub N° | 3.4 | | | |
| Definición | Identificación geográfica del origen/residencia del resguardo del documento. | | | |
| Obligación | Sugerido | Modo de ingreso | | Automático |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso |  | | | |
| Valores | Valor de ingreso | | Código comuna sistema codificación. | |
| Tipo dato | | Numérico | |
| Por defecto | |  | |
| Comentarios |  | | | |
| Ejemplo |  | | | |
|  |  |  |  |  |

| **17** | **Fecha de creación** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE4\_1 | | | |
| N° Grupo | 4. Temporalidad | | | |
| Sub N° | 4.1 | | | |
| Definición | Fecha en la que es generado el documento. | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Automático |
| Transferencia AN | SI | Repetible | |  |
| Forma de ingreso | Se genera automáticamente, según formato aaaa-mm-dd hh:mm:ss (ISO 8601) | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Formato aaaa-mm-dd hh:mm:ss (ISO 8601) | |
| Por defecto | |  | |
| Comentarios | Metadato posible de ser modificado. Debe quedar registrado el historial de modificaciones. | | | |
| Ejemplo | 2023-20-11:16:56:57 | | | |
|  |  |  |  |  |

| **18** | **Fecha de modificación** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE4\_2 | | | |
| N° Grupo | 4. Temporalidad | | | |
| Sub N° | 4.2 | | | |
| Definición | Fecha de la última modificación del documento. | | | |
| Obligación | Obligatorio | Modo de ingreso | | Automático |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Se genera automáticamente, según formato aaaa-mm-dd hh:mm:ss (ISO 8601) en caso de una actualización en el repositorio. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Formato aaaa-mm-dd hh:mm:ss (ISO 8601). | |
| Por defecto | |  | |
| Comentarios | Metadato posible de ser modificado. Debe quedar registrado el historial de modificaciones. | | | |
| Ejemplo | 2023-20-11:16:56:57 | | | |
|  |  |  |  |  |

| **19** | **Fecha de captura** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE4\_3 | | | |
| N° Grupo | 4. Temporalidad | | | |
| Sub N° | 4.3 | | | |
| Definición | Fecha en la cual el documento se incorpora al repositorio documental. Corresponde a aquellos documentos no generados internamente, ya sea que se reciben digitalmente, o que son digitalizados desde el formato físico (microforma). | | | |
| Obligación | Condicional | Modo de ingreso | | Automático/manual |
| Transferencia AN | SI | Repetible | | NO |
| Forma de ingreso | Se genera automáticamente, según formato aaaa-mm-dd hh:mm:ss (ISO 8601).  En caso de tratarse de una Microforma es obligatorio. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Formato aaaa-mm-dd hh:mm:ss (ISO 8601). | |
| Por defecto | |  | |
| Comentarios |  | | | |
| Ejemplo | 2023-20-11:16:56:57 | | | |
|  |  |  |  |  |

| **20** | **Cobertura temporal** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE4\_4 | | | |
| N° Grupo | 4. Temporalidad | | | |
| Sub N° | 4.4 | | | |
| Definición | Indica el metadato descriptivo que registra el tiempo (fechas) al que hace referencia el acto del documento. | | | |
| Obligación | Sugerido | Modo de ingreso | | Automático/manual |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso |  | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Fecha | |
| Por defecto | |  | |
| Comentarios |  | | | |
| Ejemplo | 2023-20-11:16:56:57 | | | |
|  |  |  |  |  |

| **21** | **Tipo documental** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE5\_1 | | | |
| N° Grupo | 5. Caracterización documental | | | |
| Sub N° | 5.1 | | | |
| Definición | Corresponde al nombre y/o código del tipo documental oficial  estandarizado. | | | |
| Obligación | **Condicional** | Modo de ingreso | | Manual |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Se ingresa de forma manual o mediante la selección desde una lista o vocabulario controlado (ver [sección 4.](#_heading=h.1ksv4uv) lista N° 1).  Es obligatorio en caso de contar con la tipificación del documento. | | | |
| Valores | Valor de ingreso | | Gestor de Códigos (Gescode) | |
| Tipo dato | | Numérico | |
| Por defecto | | 3 (Antecedente) | |
| Comentarios | El valor a seleccionar desde lista controlada dependerá de un término genérico. | | | |
| Ejemplo | 30 (Oficio) | | | |
|  |  |  |  |  |

| **22** | **Origen del documento** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE5\_2 | | | |
| N° Grupo | 5. Caracterización documental | | | |
| Sub N° | 5.2 | | | |
| Definición | Caracterización del origen de incorporación del documento al repositorio institucional.  Es obligatorio en caso de tratarse de un documento de tipo Microforma. | | | |
| Obligación | Condicional | Modo de ingreso | | Automático |
| Transferencia AN | SI | Repetible | | NO |
| Forma de ingreso | Lista controlada de origen (ver [sección 4.](#_heading=h.1ksv4uv) lista N° 8). | | | |
| Valores | Valor de ingreso | | Gestor de Códigos      (Gescode) | |
| Tipo dato | | Numérico | |
| Por defecto | | 1 | |
| Comentarios |  | | | |
| Ejemplo | 1 (repositorio externo) | | | |
|  |  |  |  |  |

| **23** | **Mecanismo de incorporación del documento** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE5\_3 | | | |
| N° Grupo | 5. Caracterización documental | | | |
| Sub N° | 5.3 | | | |
| Definición | Expresa el mecanismo de incorporación al repositorio documental, ya sea físico, digitalización, digital  u otro. | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Automático |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Al momento de incorporar al repositorio automáticamente/manual. Se puede seleccionar desde una lista controlada ver ([sección 4.](#_heading=h.1ksv4uv) lista N° 2). | | | |
| Valores | Valor de ingreso | | Gestor de Códigos     (Gescode) | |
| Tipo dato | | Numérico | |
| Por defecto | | 2. Digital | |
| Comentarios | - | | | |
| Ejemplo | 2 (digital) | | | |
|  |  |  |  |  |

| **24** | **URI de documento externo** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE5\_4 | | | |
| N° Grupo | 5. Caracterización documental | | | |
| Sub N° | 5.4 | | | |
| Definición | Enlace a documento y/o recurso residente en repositorio externo. | | | |
| Obligación | Condicional | Modo de ingreso | | Automático |
| Transferencia AN | SI | Repetible | | NO |
| Forma de ingreso | Manual o consumo automático según corresponda.  Es obligatorio en caso de tratarse de un documento externo referenciado. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Alfanumérico | |
| Por defecto | | – | |
| Comentarios | En caso de tratarse de un repositorio externo se debe utilizar una URI persistente del documento. | | | |
| Ejemplos | URL: [https://dominio-institución/servicio-persistente/20.500.13034/401](/guias/Metadatos_Expediente_Electrónico/about:blank)  URI persistente: <http://bibliotecadigital.dipres.gob.cl/handle/11626/19183> | | | |
|  |  |  |  |  |

| **25** | **Ubicación física de documento referenciado** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE5\_5 | | | |
| N° Grupo | 5. Caracterización documental | | | |
| Sub N° | 5.5 | | | |
| Definición | Código de almacenamiento físico en el archivo institucional, que permita identificar y obtener su ubicación en él (registro electrónico de un documento físico). | | | |
| Obligación | Condicional | Modo de ingreso | | Automático |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Registro manual de la ubicación en el archivo institucional del documento físico que es referenciado en el documento electrónico.  Es obligatorio en caso de tratarse de un documento físico referenciado (expediente híbrido o una microforma realizada directamente). | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Alfanumérico | |
| Por defecto | | – | |
| Comentarios | Cada institución define sus políticas de codificación. | | | |
| Ejemplo | space\_40\_archivador\_20.5.10\_oae\_33706 | | | |
|  |  |  |  |  |

| **26** | **Estado de conservación microforma** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE5\_6 | | | |
| N° Grupo | 5. Caracterización documental | | | |
| Sub N° | 5.6 | | | |
| Definición | Descripción del estado del documento original a partir del cual se generó la microforma. | | | |
| Obligación | Condicional | Modo de ingreso | | Automático |
| Transferencia AN | SI | Repetible | | NO |
| Forma de ingreso | Es obligatorio en caso de tratarse de un documento tipo microforma. Su valor puede seleccionarse desde una lista controlada (ver [sección 4.](#_heading=h.1ksv4uv) lista N° 3). | | | |
| Valores | Valor de ingreso | | Gestor de Códigos (GESCODE) | |
| Tipo dato | | Numérico | |
| Por defecto | | 1 (Muy Bueno) | |
| Comentarios | Es requerido si se trata de un documento microforma | | | |
| Ejemplo | 1 (Muy Bueno) | | | |
|  |  |  |  |  |

| **27** | **Disposición** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE5\_7 | | | |
| N° Grupo | 5. Caracterización documental | | | |
| Sub N° | 5.7 | | | |
| Definición | Destino planificado del documento bajo una normativa o cuerpo legal, resolución u oficio, que es consecuencia del proceso de valoración documental. | | | |
| Obligación | Sugerido | Modo de ingreso | | Manual/automático |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso |  | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Texto | |
| Por defecto | |  | |
| Comentarios |  | | | |
| Ejemplo | Preservación Institucional | | | |
|  |  |  |  |  |

| **28** | **Código OAE** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE61\_1 | | | |
| N° Grupo | 6. Relaciones | OAE Asociada | | | |
| Sub N° | 6.1.1 | | | |
| Definición | Identificación del OAE que, en el cumplimiento de sus funciones, genera y/o gestiona los documentos y expedientes que son parte de su sistema de gestión documental y formarán parte de su archivo. | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Automático |
| Transferencia AN | SI | Repetible | | SI |
| Forma de ingreso | Se genera automáticamente. Cada sistema debe incorporar al menos  el código del OAE productor. | | | |
| Valores | Valor de ingreso | | Servicio codificación del Estado - OAE | |
| Tipo dato | | Numérico | |
| Por defecto | | – | |
| Comentarios |  | | | |
| Ejemplo | 46 (Gobierno Regional de la Región de La Araucanía) | | | |
|  |  |  |  |  |

| **29** | **Nombre OAE** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE61\_2 | | | |
| N° Grupo | 6. Relaciones | OAE Asociada | | | |
| Sub N° | 6.1.2 | | | |
| Definición | Nombre del OAE que, en el cumplimiento de sus funciones, genera y/o gestiona los documentos y expedientes que son parte de su sistema de gestión documental y formarán parte de su archivo. | | | |
| Obligación | Condicional | Modo de ingreso | | Automático/manual |
| Transferencia AN | SI | Repetible | | SI |
| Forma de ingreso | Se incorpora automáticamente/manual al incorporar una relación con una OAE con la que no se cuenta su código.   Es obligatorio en caso de no existir el código asociado o por resolución del OAE para su registro directo. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Alfanumérico | |
| Por defecto | | –- | |
| Comentarios | Sólo es obligatorio en caso que no se identifique por el código OAE | | | |
| Ejemplo | Gobierno Regional de la Región de La Araucanía | | | |
|  |  |  |  |  |

| **30** | **Tipo de relación entre documento y OAE** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE61\_3 | | | |
| N° Grupo | 6. Relaciones | Tipo de relación entre documento y OAE | | | |
| Sub N° | 6.1.3 | | | |
| Definición | Relación establecida entre el documento referenciado y el OAE (gestionador, autor institucional o custodia). | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Automático |
| Transferencia AN | SI | Repetible | | SI |
| Forma de ingreso | Se genera automáticamente por cada sistema al momento de incorporar el documento al repositorio. Al menos es obligatorio registrar autor institucional y custodia. Se puede seleccionar el valor desde una lista controlada (ver [sección 4.](#_heading=h.1ksv4uv) lista N° 4). | | | |
| Valores | Valor de ingreso | | Servicio codificación del Estado | |
| Tipo dato | | Numérico | |
| Por defecto | | 1(Autor institucional) | |
| Comentarios | Por lo menos debe incorporarse la relación con el autor institucional si corresponde. El productor y custodio del documento se obtendrá en los procesos de interoperabilidad a través de metadato del expediente al cual está relacionado. | | | |
| Ejemplo | 1 (Autor institucional) | | | |
|  |  |  |  |  |

| **31** | **Tipo de relación con otros actores** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE62\_1 | | | |
| N° Grupo | 6. Relaciones | Otros actores | | | |
| Sub N° | 6.2.1 | | | |
| Definición | Identificación del tipo de relación existente entre el actor (persona natural o jurídica) y el documento. | | | |
| Obligación | Condicional | Modo de ingreso | | Automático/manual |
| Transferencia AN | SI | Repetible | | SI |
| Forma de ingreso | Lista controlada (ver [sección 4.](#_heading=h.1ksv4uv) lista N° 5). Es obligatorio en caso de registrar una relación con el documento. | | | |
| Valores | Valor de ingreso | | Servicio codificación del Estado | |
| Tipo dato | | Numérico | |
| Por defecto | | 3 (Autor/creador) | |
| Comentarios | Al menos se debe registrar al autor(es)/creador(es) del documento. | | | |
| Ejemplo | 3 | | | |
|  |  |  |  |  |

| **32** | **Tipo de actor relacionado** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE62\_2 | | | |
| N° Grupo | 6. Relaciones | Otros actores | | | |
| Sub N° | 6.2.2 | | | |
| Definición | Identificación del tipo de actor relacionado, que indicará la pertinencia del registro de otro dato para identificar (RUT , RUN, Pasaporte). | | | |
| Obligación | Condicional | Modo de ingreso | | Automático |
| Transferencia AN | NO | Repetible | | SI |
| Forma de ingreso | Se especificará el tipo de persona relacionada para indicar el tipo de identificación requerida. Se puede usar una lista controlada (ver [sección 4.](#_heading=h.1ksv4uv) lista N° 6).  Es obligatorio en caso de registrar una relación con el documento. | | | |
| Valores | Valor de ingreso | | Servicio codificación del Estado | |
| Tipo dato | | Numérico | |
| Por defecto | | 1 (Ciudadano) | |
| Comentarios |  | | | |
| Ejemplo | 1 | | | |
|  |  |  |  |  |

| **33** | **Identificación de actor relacionado** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE62\_3 | | | |
| N° Grupo | 6. Relaciones | Otros actores | | | |
| Sub N° | 6.2.3 | | | |
| Definición | RUN (Número de Cédula de identidad) de la persona o RUT (Rol Único Tributario) de la institución privada o Nro de pasaporte en caso de ser extranjero. | | | |
| Obligación | Condicional | Modo de ingreso | | Automático/manual |
| Transferencia AN | SI | Repetible | | SI |
| Forma de ingreso | Es obligatorio en caso de registrar una relación con el documento. | | | |
| Valores | Valor de ingreso | | Formato RUN/RUT | |
| Tipo dato | | Alfanumérico | |
| Por defecto | | – | |
| Comentarios | - | | | |
| Ejemplo | 677368373-5 | | | |
|  |  |  |  |  |

| **34** | **Nombre del actor relacionado** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE62\_4 | | | |
| N° Grupo | 6. Relaciones | Otros actores | | | |
| Sub N° | 6.2.4 | | | |
| Definición | Nombre de la persona natural o jurídica relacionada con el documento. | | | |
| Obligación | Condicional | Modo de ingreso | | Manual |
| Transferencia AN | NO | Repetible | | SI |
| Forma de ingreso | Registro del nombre en caso de no contar con la identificación del actor relacionado. Es obligatorio en caso de registrar una relación con el documento. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Alfanumérico | |
| Por defecto | |  | |
| Comentarios | - | | | |
| Ejemplos | Entel Chile  Julian Santelices Machuca | | | |
|  |  |  |  |  |

| **35** | **Nivel de acceso** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE7\_1 | | | |
| N° Grupo | 7. Seguridad | | | |
| Sub N° | 7.1 | | | |
| Definición | Indicación relativa al acceso y consulta de los documentos. | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Manual |
| Transferencia AN | SI | Repetible | | NO |
| Forma de ingreso | Se ingresa manualmente, aunque el valor está basado en vocabulario controlado (ver [sección 4.](#_heading=h.1ksv4uv) lista N° 7). Debe quedar abierta la posibilidad de incorporar nuevos niveles, aunque siempre utilizando un vocabulario controlado. | | | |
| Valores | Valor de ingreso | | Servicio codificador del Estado | |
| Tipo dato | | Numérico | |
| Por defecto | | 1(Público) | |
| Comentarios | - | | | |
| Ejemplo | 1 | | | |
|  |  |  |  |  |

| **36** | **Fecha fin restricción** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE7\_2 | | | |
| N° Grupo | 7. Seguridad | | | |
| Sub N° | 7.2 | | | |
| Definición | Es la fecha hasta cuando se debe presentar el texto de advertencia en caso que un usuario quiera acceder a esta documentación. | | | |
| Obligación | Sugerido | Modo de ingreso | | Manual |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Se ingresa manualmente. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Fecha | |
| Por defecto | |  | |
| Comentarios | - | | | |
| Ejemplo |  | | | |
|  |  |  |  |  |

| **37** | **Texto Advertencia** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE7\_3 | | | |
| N° Grupo | 7. Seguridad | | | |
| Sub N° | 7.3 | | | |
| Definición | Es el texto que se debe presentar en caso que un usuario quiera acceder a esta información. | | | |
| Obligación | Sugerido | Modo de ingreso | | Manual |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Se ingresa manualmente. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Texto | |
| Por defecto | |  | |
| Comentarios | - | | | |
| Ejemplo |  | | | |
|  |  |  |  |  |

| **38** | **Información de carácter sensible** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE7\_4 | | | |
| N° Grupo | 7. Seguridad | | | |
| Sub N° | 7.4 | | | |
| Definición | Identificación de que el documento contiene información de carácter sensible | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Manual |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | La plataforma de repositorio debe manejar un registro de marca de tipo de información sensible. | | | |
| Valores | Valor de ingreso | | Lista Controlada [1 - SI / 2 - NO] | |
| Tipo dato | | Numérico | |
| Por defecto | | 2 (NO) | |
| Comentarios |  | | | |
| Ejemplo | 1 | | | |
|  |  |  |  |  |

| **39** | **Tipo Firma** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE8\_1 | | | |
| N° Grupo | 8. Firma | | | |
| Sub N° | 8.1 | | | |
| Definición | Identificación del tipo de firma electrónica utilizada en la generación del documento (avanzada, simple). | | | |
| Obligación | Sugerido | Modo de ingreso | | Automático |
| Transferencia AN | NO | Repetible | | SI |
| Forma de ingreso |  | | | |
| Valores | Valor de ingreso | | Lista controlada | |
| Tipo dato | | numérico | |
| Por defecto | | 1 (AVANZADA) | |
| Comentarios |  | | | |
| Ejemplo | 2 (SIMPLE) | | | |
|  |  |  |  |  |

| **40** | **Proveedor** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE8\_2 | | | |
| N° Grupo | 8. Firma | | | |
| Sub N° | 8.2 | | | |
| Definición | Identificación del proveedor del servicio de firma electrónica utilizado en el documento. | | | |
| Obligación | Sugerido | Modo de ingreso | | Automático |
| Transferencia AN | NO | Repetible | | SI |
| Forma de ingreso | Se completa en forma automática al detectar el proveedor de la firma. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Texto | |
| Por defecto | |  | |
| Comentarios |  | | | |
| Ejemplo |  | | | |
|  |  |  |  |  |

| **41** | **Firma electrónica avanzada** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE8\_3 | | | |
| N° Grupo | 8. Firma | | | |
| Sub N° | 8.3 | | | |
| Definición | Se indica si el documento cuenta con firma electrónica avanzada. | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Automático |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Se completa en forma automática al detectar si cuenta con FEA o no. | | | |
| Valores | Valor de ingreso | | Lista controlada [1 - SI / 2 - NO] | |
| Tipo dato | | Numérico | |
| Por defecto | | 2 (NO) | |
| Comentarios |  | | | |
| Ejemplo | 1 (SI) | | | |
|  |  |  |  |  |

| **42** | **Nombre/Cargo Representación** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE84\_1 | | | |
| N° Grupo | 8. Firma | Firmantes | | | |
| Sub N° | 8.4.1 | | | |
| Definición | Identificación del nombre de la persona que firma y cargo asociado. | | | |
| Obligación | Sugerido | Modo de ingreso | | Automático /manual |
| Transferencia AN | NO | Repetible | | SI |
| Forma de ingreso | Se completa en forma automática al detectar el firmante del archivo. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Texto | |
| Por defecto | |  | |
| Comentarios |  | | | |
| Ejemplo |  | | | |
|  |  |  |  |  |

| **43** | **RUN firmante** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE84\_2 | | | |
| N° Grupo | 8.4 Firma | Firmantes | | | |
| Sub N° | 8.4.2 | | | |
| Definición | Identificación de la persona que firma el documento. | | | |
| Obligación | Sugerido | Modo de ingreso | | Manual/Automático |
| Transferencia AN | NO | Repetible | | SI |
| Forma de ingreso | Se registra al momento de identificar al actor. | | | |
| Valores | Valor de ingreso | |  | |
| Tipo dato | | Numérico | |
| Por defecto | |  | |
| Comentarios |  | | | |
| Ejemplo |  | | | |
|  |  |  |  |  |

| **44** | **Código procedimiento administrativo asociado** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE9\_1 | | | |
| N° Grupo | 9, Procedimiento y Trámite asociado | | | |
| Sub N° | 9.1 | | | |
| Definición | Código identificador del procedimiento administrativo en el Catálogo de Procedimientos Administrativos y Tramitaciones (CPAT), asociado específicamente a la generación del documento. | | | |
| Obligación | Condicional | Modo de ingreso | | Automático/manual |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Código del procedimiento administrativo existente en el Catálogo de Procedimientos Administrativos y Tramitaciones del Estado (CPAT). Es obligatorio en caso de estar vinculado a un procedimiento administrativo específico. | | | |
| Valores | Valor de ingreso | | Servicio codificador del Estado CPAT | |
| Tipo dato | | Alfanumérico | |
| Por defecto | |  | |
| Comentarios | Disponibilidad por el Catálogo de procedimientos administrativos y trámites. | | | |
| Ejemplo | 5076   (Convalidación de Programa de Perfeccionamiento Académico - PA-UNI00002-00001) | | | |
|  |  |  |  |  |

| **45** | **Nombre procedimiento administrativo asociado** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MGDDE9\_2 | | | |
| N° Grupo | 9, Procedimiento y Trámite asociado | | | |
| Sub N° | 9.2 | | | |
| Definición | Nombre del trámite asociado, en caso que no se cuente con el código CPAT | | | |
| Obligación | Condicional | Modo de ingreso | | Manual |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Nombre del procedimiento administrativo no existente en el Catálogo de Procedimientos Administrativos y Tramitaciones del Estado (CPAT). Es obligatorio en caso de estar vinculado a un procedimiento administrativo específico y este no se encuentre creado en CPAT | | | |
| Valores | Valor de ingreso | | - | |
| Tipo dato | | Texto | |
| Por defecto | | - | |
| Comentarios | - | | | |
| Ejemplo | Convalidación de Programa de Perfeccionamiento Académico | | | |
|  |  |  |  |  |

| **46** | **Versión MDGD (esquema metadatos documentos)** | | | |
| --- | --- | --- | --- | --- |
| Código metadato | MDGDDE10 | | | |
| N° Grupo | 10. Versión MGD | | | |
| Sub N° | 10.1 | | | |
| Definición | Identificación de la versión de la Guía Técnica de Metadatos esquema de metadata utilizada, y de acuerdo con las actualizaciones dispuestas por la Secretaría de Gobierno Digital. | | | |
| Obligación | **Obligatorio** | Modo de ingreso | | Automático |
| Transferencia AN | NO | Repetible | | NO |
| Forma de ingreso | Registro automático. | | | |
| Valores | Valor de ingreso | | Lista controlada de versiones de la guía de metadatos | |
| Tipo dato | | Numérico | |
| Por defecto | | 1 | |
| Comentarios |  | | | |
| Ejemplo | 1 | | | |
|  |  |  |  |  |

[¶](#h-4-listas-controladas-de-metadatos-obligatorios-en-expedientes-y-documentos-electrónicos) 4. Listas controladas de Metadatos obligatorios en expedientes y documentos electrónicos
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

La siguiente sección incorpora listas controladas para los metadatos obligatorios de expedientes y documentos electrónicos.

Las listas controladas son listas de valores definidos previamente para un campo, de manera de estandarizar la forma en que se registra la información. Por ejemplo, para un campo referido a “división político-administrativa” la lista controlada contendría los valores “Región”, “Provincia", “Comuna”, por lo que los campos de información contendrían esos valores. Esto permite registrar de manera más consistente la información.

En el contexto de los metadatos para documentos y expedientes electrónicos, las listas controladas establecen valores pre-definidos y estandarizados para los metadatos. El uso de estas listas de valores permitirá mejorar los procesos de clasificación, búsqueda y recuperación de la información, contribuyendo así a la eficiencia y transparencia en la administración pública. Cada una de estas listas de valores para metadatos (lista controlada) estará disponible en el Gestor de Códigos (GESCODE)      para su uso por parte de los OAE.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **N°** | **Metadato** | Etiqueta | **Valores** | **Ejemplos** |
| **1** | **MGDDE5\_1** | Tipo Documental | 1. Acta | - Acta de Sesión |
| - Acta de evaluación |
| - Acta de consejo |
| - Acta de notificación |
| - Acta de observaciones |
| - Acta Consejo de |
| - Acta de Directorio |
| - Acta Junta |
| 2. Acuerdo | - Acuerdo de comité |
| - Acuerdo complementario |
| - Acuerdo de compromiso |
| 3. Antecedente | - Antecedentes legales |
| - Antecedentes personales |
| - Antecedentes profesionales |
| - Antecedentes societarios |
| - Antecedentes de vigencia |
| 4. Autorización | - Autorización de apertura |
| - Autorización de constitución |
| - Autorización de de inversión |
| - Autorización sanitaria |
| 5. Base | - Bases técnicas |
| - Bases de concurso |
| - Bases de licitación |
| 6. Boleta | - Boleta de garantía |
| - Boleta de honorarios |
| - Boleta de servicios |
| 7. Carta | - Carta circular |
| - Carta de compromiso |
| - Carta de recomendación |
| 8. Certificado | - Certificado de existencia |
| - Certificado de dominio |
| - Certificados de Vigencia |
| - Certificado de residencia |
| 9. Circular | - Circular interna |
| - Circular externa |
| - Circular administrativa |
| - Circular de convocatoria |
| - Circular de instrucciones |
| 10. Citación | - Citación administrativa |
| - Citación judicial |
| 11. Convenio | - Convenio de financiamiento |
| - Convenio de intercambio de información |
| - Convenio de transferencia de tecnología |
| 12. Constancia | - Constancia de estudios |
| -Constancia de trabajo |
| - Constancia de residencia |
| 13. Contrato | - Contrato de arrendamiento |
| - Contrato de concesión |
| - Contrato de trabajo |
| - Contrato de compraventa |
| - Contrato de obra pública |
| - Contrato de servicios |
| 14. Declaración | - Declaración de Impacto Ambiental |
| - Declaración Jurada |
| - Declaración pública |
| - Declaración sobre enajenación |
| 15. Decreto | - Decreto supremo |
| - Decreto Presidencial |
| - Decreto con fuerza de ley |
| - Decreto exento |
| - Decreto Municipal |
| - Decreto regional |
| - Decreto ley |
| - Decreto administrativo |
| - Decreto de emergencia |
| 16. Denuncia | - Denuncia penal |
| - Denuncia administrativa |
| - Denuncia laboral |
| - Denuncia ambiental |
| - Denuncia de maltrato o abuso |
| - Denuncia de violencia de género |
| 17. Dictamen | - Dictamen jurídico |
| - Dictamen técnico |
| - Dictamen contable |
| - Dictamen de auditoría |
| - Dictamen médico |
| - Dictamen de viabilidad |
| - Dictamen de impacto ambiental |
| - Dictamen de ética |
| 18. Estado de situación | - Estado de situación financiera |
| - Estado de situación patrimonial |
| - Estado de situación contable |
| - Estado de situación de recursos humanos |
| - Estado de situación de inventario |
| - Estado de situación de proyectos |
| - Estado de situación de cumplimiento normativo |
| - Estado de situación de gestión de riesgos |
| 19. Estudio | - Estudio de viabilidad |
| - Estudio de impacto ambiental |
| - Estudio de mercado |
| - Estudio de factibilidad técnica |
| - Estudio de riesgos |
| - Estudio de necesidades |
| - Estudio de impacto social |
| - Estudio de evaluación |
| 20. Expediente administrativo | - Expediente de persona |
| - Expediente de contratación |
| - Expediente de licitación |
| - Expediente de trámite |
| - Expediente de gestión financiera |
| - Expediente de proyecto |
| - Expediente de control y seguimiento |
| - Expediente de resolución de casos o reclamos |
| 21. Ficha | - Ficha de identificación |
| - Ficha de trámite |
| - Ficha de gestión de proyectos |
| - Ficha de participación ciudadana |
| - Ficha de atención ciudadana |
| - Ficha de capacitación |
| - Ficha de control de calidad |
| - Ficha de seguimiento normativo |
| 22. Informe | - Informe técnico |
| - Informe de gestión |
| - Informe financiero |
| - Informe de auditoría |
| - Informe de impacto ambiental |
| - Informe de investigación |
| - Informe de evaluación |
| - Informe de seguimiento |
| 23. Instructivo | - Instructivo de procedimientos |
| - Instructivo de seguridad |
| - Instructivo de capacitación |
| - Instructivo de mantenimiento |
| - Instructivo de - implementación |
| - Instructivo técnico |
| 24. Mandato | - Mandato legal- Mandato de representación |
| - Mandato de gestión |
| - Mandato de auditoría |
| - Mandato de comité o grupo de trabajo |
| - Mandato de negociación |
| - Mandato de investigación |
| - Mandato de supervisión |
| 25. Memorándum | - Memorándum interno |
| - Memorándum de coordinación |
| - Memorándum de información |
| - Memorándum de seguimiento |
| - Memorándum de respuesta |
| - Memorándum de acuerdo |
| - Memorándum de archivo |
| - Memorándum de autorización |
| 26. Minuta | - Minuta de reunión |
| - Minuta de seguimiento |
| - Minuta de planificación |
| - Minuta de presentación |
| - Minuta de visita |
| - Minuta de avance |
| - Minuta de gestión de riesgos |
| - Minuta de comité o grupo de trabajo |
| 27. Nomina | - Nómina de empleados |
| - Nómina de contratistas |
| - Nómina de pagos |
| - Nómina de beneficios |
| - Nómina de participantes |
| - Nómina de proveedores |
| - Nómina de beneficiarios |
| - Nómina de inscritos |
| 28. Nota | - Nota interna |
| - Nota de respuesta |
| - Nota de remisión |
| - Nota de atención |
| - Nota de agradecimiento |
| - Nota informativa |
| - Nota de archivo |
| - Nota de gestión |
| 29. Notificación | - Notificación de resolución |
| - Notificación de citación. |
| - Notificación de requerimiento |
| - Notificación de multa |
| - Notificación de cambio |
| - Notificación de incumplimiento |
| - Notificación de proceso administrativo |
| - Notificación de acuerdo |
| 30. Oficio | - Oficio de respuesta |
| - Oficio de remisión |
| - Oficio de notificación |
| - Oficio de solicitud |
| - Oficio de agradecimiento |
| - Oficio de gestión |
| - Oficio de informe |
| - Oficio de designación |
| - Oficio ordinario |
| - Oficio Circular |
| - Oficio Reservado |
| - Oficios Judiciales |
| 31. Ordenanza | - Ordenanza municipal |
| - Ordenanza interna |
| - Ordenanza de convivencia |
| - Ordenanza de tráfico |
| - Ordenanza de protección ambiental |
| - Ordenanza de seguridad |
| - Ordenanza de uso de instalaciones |
| - Ordenanza de contratación pública |
| 32. Prospecto | - Prospecto de información |
| - Prospecto de inversión |
| - Prospecto de capacitación |
| - Prospecto de promoción turística |
| - Prospecto de salud pública |
| - Prospecto de proyectos de infraestructura |
| - Prospecto de programas sociales |
| - Prospecto de eventos públicos |
| 33. Querella | - Querella criminal |
| - Querella laboral |
| - Querella administrativa |
| - Querella ambiental |
| - Querella de responsabilidad civil |
| - Querella de protección de derechos |
| - Querella de competencia desleal |
| - Querella de propiedad intelectual |
| 34. Reclamo | - Reclamo de servicios públicos |
| - Reclamo administrativo |
| - Reclamo laboral |
| - Reclamo de atención al cliente |
| - Reclamo de derechos ciudadanos |
| - Reclamo de defensa del consumidor |
| - Reclamo de seguridad pública |
| - Reclamo de servicios de salud |
| 35. Registro | - Registro de ingreso |
| - Registro de salida |
| - Registro de correspondencia |
| - Registro de proveedores |
| - Registro de inventario |
| - Registro de asistencia |
| - Registro de contratos |
| - Registro de incidentes |
| 36. Resolución | - Resolución administrativa |
| - Resolución judicial |
| - Resolución de recurso |
| - Resolución de contratación pública |
| - Resolución de reclamo |
| - Resolución de recurso de protección |
| - Resolución de auditoría |
| - Resolución de aprobación |
| - Resolución exenta |
| 37. Respuesta | - Respuesta a solicitud |
| - Respuesta a reclamo |
| - Respuesta a consulta |
| - Respuesta a recurso |
| - Respuesta a requerimiento |
| - Respuesta a notificación |
| - Respuesta a informe |
| - Respuesta a requerimiento de auditoría |
| 38. Retrocompra | - Contrato de retrocompra |
| - Solicitud de retrocompra |
| - Informe de evaluación para retrocompra |
| - Resolución de retrocompra |
| - Acta de retrocompra |
| - Certificado de retrocompra |
| - Informe de seguimiento de retrocompra |
| - Documento de registro de retrocompra |
| 39. Sentencia | - Sentencia judicial penal |
| - Sentencia judicial civil |
| - Sentencia judicial laboral |
| - Sentencia judicial administrativa |
| - Sentencia de tribunal arbitral |
| - Sentencia de tribunal disciplinario |
| - Sentencia de tribunal de ética |
| - Sentencia de tribunal de contratación pública |
| 40. Solicitud | - Solicitud de permiso |
| - Solicitud de licencia |
| - Solicitud de subsidio |
| - Solicitud de beneficio social |
| - Solicitud de información pública |
| - Solicitud de empleo |
| - Solicitud de cambio de domicilio |
| - Solicitud de trámite o servicio público |
| 41. Términos de referencia | - Términos de referencia para licitaciones |
| - Términos de referencia para proyectos |
| - Términos de referencia para estudios o investigaciones |
| - Términos de referencia para consultorías |
| - Términos de referencia para evaluaciones |
| - Términos de referencia para comités o grupos de trabajo |
| - Términos de referencia para auditorías o  revisiones internas |
| - Términos de referencia para contratos de  servicios profesionales |
| 42. Transcripción | - Transcripción de reuniones |
| - Transcripción de entrevistas |
| - Transcripción de audiencias |
| - Transcripción de conferencias |
| - Transcripción de discursos |
| - Transcripción de sesiones legislativas |
| - Transcripción de grabaciones de audio o video |
| - Transcripción de testimonios o declaraciones |
| **2** | **MGDDE5\_3** | Mecanismo de incorporación del documento | 1. Físico |  |
| 2. Digital |
| 3. Digitalización |
| **3** | **MGDDE5\_6** | Estado de conservación microforma | 1. Muy Bueno | - No presentan deterioros. |
| - Fácil manipulación. |
| 2. Bueno | - Deterioros menores que no comprometen la |
| información. |
| - Fácil manipulación |
| 3. Regular | - Hojas o cuadernillos sueltos. |
| - Manchas por humedad u otro que no compromete |
| la información. |
| - Rasgados menores en relación a superficie |
| total de documento. |
| - Restauraciones anteriores no especializadas. |
| - Deterioros de bordes (hasta 50% de las fojas). |
| - Manipular con cuidado |
| 4. Malo | - Rasgados y faltantes mayores (50 % o más). |
| - Tintas oxidadas con aureolas y roturas (50% |
| más) |
| - Daño biológico (manchas de hongos daño por |
| insectos) |
| - Aureolas por humedad y manchas significativas |
| (50% o más) |
| - Manipular con mucho cuidado |
| 5. Muy Malo | - Deterioros extremos. |
| - Volumen puede estar incompleto. |
| - Humedad, microorganismos activos, daños graves |
| por insectos (más del 50%) |
| - Oxidación de tintas se extiende a todo el |
| soporte en la mayoría de los documentos |
| - Muchos documentos con daños graves. |
| - Manipulación con extremo cuidado. |
| **4** | **MGDEE51\_3**  **MGDDE61\_3** | Tipo Relación OAE | 1. Autor institucional |  |
| 2. Destinatario |
| 3. Productor / generador |
| 4. Custodia |
| **5** | **MGDEE52\_1**  **MGDDE62\_1** | Tipo de relación con otros actores | 1. Responsable |  |
| 2. Interesado |
| 3. Autor/creador |
| 4. Referido |
| 5. Destinatario |
| 6. Ministro de Fe |
| **6** | **MGDEE52\_2**  **MGDDE62\_2** | Tipo de actor relacionado | 1. Ciudadano |  |
| 2. Extranjero |
| 3. Institución privada |
| 4. Funcionario |
| **7** | **MGDEE6\_1**  **MGDDE7\_1** | Nivel de acceso | 1. Público |  |
| 2. Restringido |
| 3. Secreto |
| 4. Reservado |
| **8** | **MGDDE5\_2** | Origen del documento | 1. Repositorio Externo |  |
| 2. Interoperabilidad |
| 3. Plataforma ciudadana |
| 4. Repositorio Ciudadano |

---

[[1]](#_ftnref1) Information and documentation - Records management - Part 1: General. <https://www.iso.org/standard/56639.html>

[[2]](#_ftnref2) Information and documentation -- Records management processes -- Metadata for records -- Part 1: Principles. Geneva, Switzerland: ISO.

[[3]](#_ftnref3)Archivo Nacional de Chile, Procedimiento para la Transferencia de Documentos en Soporte Papel al Archivo Nacional de Chile, versión 2021

<https://www.archivonacional.gob.cl/sites/www.archivonacional.gob.cl/files/2022-05/PROCEDIMIENTO%20TRANSFERENCIAS%20DOCUMENTALES%202022.pdf>