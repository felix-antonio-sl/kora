---
title: "Guía Técnica de Seguridad de la Información y Ciberseguridad"
url: "https://wikiguias.digital.gob.cl/guias/GU-CIBER-001"
category: "Lineamientos Técnicos/Guías"
tags: [{'tag': 'seguridad de la información', 'title': 'seguridad de la información'}, {'tag': 'ciberseguridad', 'title': 'ciberseguridad'}, {'tag': 'datos', 'title': 'datos'}, {'tag': 'guía técnica', 'title': 'guía técnica'}]
description: "Guía técnica de apoyo a la norma técniva de Seguridad de la Información y Ciberseguridad de la ley N°21.180, ley de Transformción Digital"
updated_at: "2025-10-07T22:50:39.295Z"
---

[¶](#guía-técnica) **GUÍA TÉCNICA**
-----------------------------------

**Guía Técnica  Seguridad de la Información y Ciberseguridad**

[¶](#introducción) **Introducción**
-----------------------------------

En cumplimiento del artículo 12 de la [Norma Técnica de Seguridad de la Información y Ciberseguridad](/Normas/Decreto7),  la presente guía técnica entrega lineamientos para implementar controles de seguridad de la información y ciberseguridad en los órganos de la Administración del Estado, y para la aplicación de políticas, buenas prácticas y estándares apropiados en la protección de sus activos de información y servicios.

Tanto los términos establecidos en esta guía técnica, así como la forma de implementación de la misma, deberán interpretarse según lo establecido en la Norma Técnica de Seguridad de la Información y Ciberseguridad, salvo aquellas definiciones que se incorporen únicamente en esta guía para facilitar su entendimiento y aplicación.

La Norma Técnica está basada en buenas prácticas internacionales, en la familia de normas NCH-ISO 27000, y el marco NIST, así como el Decreto N° 83, del año 2015, del Ministerio Secretaría General de la Presidencia. En consecuencia, el marco de trabajo que presenta esta guía técnica puede ser complementado con dicha familia de normas y con el marco NIST, para su mejor entendimiento.

Sin embargo, los órganos podrán establecer o utilizar otras técnicas o estándares para la implementación de esta guía técnica, siempre que sean consistentes con la normativa señalada en el párrafo anterior, así como con las directrices y lineamientos establecidos en la [*Política Nacional de Ciberseguridad*](https://www.diariooficial.interior.gob.cl/publicaciones/2023/12/04/43717/01/2415658.pdf), la [*Ley Marco de Ciberseguridad*](https://www.diariooficial.interior.gob.cl/publicaciones/2024/04/08/43820/01/2475674.pdf) o por la Secretaría de Gobierno Digital del Ministerio de Hacienda. Se entenderá que serán consistentes cuando tengan, a lo menos, efectos equivalentes.

---

[¶](#definiciones) **Definiciones**
-----------------------------------

Las definiciones que a continuación se presentan son complementarias a las que ya están establecidas en la Norma Técnica de Seguridad de la Información y Ciberseguridad, que se aplican a esta guía técnica también.

**Apetito al riesgo**: es la cantidad de riesgo que una organización está dispuesta a asumir para alcanzar sus objetivos estratégicos.

**Ataque día cero**: (*zero day attack*) es un ataque basado en una vulnerabilidad de software o hardware que los atacantes descubrieron antes de que el proveedor sepa siquiera de su existencia. Debido a que los proveedores desconocen este problema, no existen parches para vulnerabilidades o medidas de mitigación de día cero, por lo cual es muy probable que los ataques tengan éxito.

**Custodio**: es el encargado de otorgar y supervisar los accesos a los activos de información bajo su custodia.

**Dueño de activo de información**: es el encargado de velar porque los activos se encuentren debidamente inventariados, clasificados y actualizados de acuerdo con el esquema de clasificación y priorización establecido por cada OAE.

**Evento precursor**: es un indicio de que puede ocurrir un incidente en el futuro, el que puede o no materializarse en un evento de seguridad.

**Plan de continuidad operativa y contingencia**: plan que contiene los lineamientos para mantener la continuidad operativa de las plataformas electrónicas del servicio, para los casos en que éstas o sus sistemas de información fallen.

**Planes de recuperación**: planes que disponen, para cada plataforma, las acciones para restaurar la normalidad en su funcionamiento después de una disrupción, de manera que vuelvan a operar en su estado funcional en el menor tiempo posible.

**Planes de respuesta**: planes que establecen, para cada plataforma, los procedimientos para enfrentar inmediatamente un incidente una vez que ha ocurrido. Los planes de respuesta deben activarse una vez confirmado un incidente y, en consecuencia, hayan sido afectadas alguna de las plataformas electrónicas o cualquiera de sus componentes.

**Redundancia**: duplicación de los componentes de software o hardware de un sistema, de manera de asegurar su disponibilidad en caso de fallas.

**Tolerancia al riesgo**: se relaciona con la cantidad de riesgo del entorno, como la volatilidad o los altibajos, que una institución puede tolerar.

---

[¶](#política-de-seguridad-de-la-información-y-ciberseguridad) **Política de Seguridad de la Información y Ciberseguridad**
---------------------------------------------------------------------------------------------------------------------------

Cada órgano de la Administración del Estado (OAE) deberá elaborar una Política de Seguridad de la Información y Ciberseguridad (ver artículo N°5 de la [Norma Técnica de Seguridad de la Información y Ciberseguridad](https://www.diariooficial.interior.gob.cl/publicaciones/2023/08/17/43629/01/2361371.pdf)), que tendrá como objetivo establecer las directrices generales en materia de seguridad de la información y ciberseguridad dentro del órgano, además de velar por la seguridad de los componentes de software, hardware y sistemas informáticos, así como de los datos que almacenan, procesan e interoperan. Igualmente, deberá contener la visión estratégica del OAE con respecto a la seguridad de la información y ciberseguridad, y los lineamientos para alcanzar los objetivos propuestos.

Para la elaboración de su Política, los OAEs deberán realizar un diagnóstico del estado actual de sus sistemas, activos de información, procesos y procedimientos, con el objetivo de generar una línea base del estado actual de la institución en los temas relacionados con el contenido de la Norma Técnica. Con este levantamiento se facilitará la identificación de necesidades y su clasificación, de acuerdo con su grado de urgencia. Adicionalmente este levantamiento será la base de lo definido en el capítulo  **Función de identificación** de esta guía.

La Política deberá ser aprobada por el(la) Jefe(a) de Servicio respectivo, con el propósito de lograr un efectivo compromiso del estamento directivo con su cumplimiento y aplicación. Esta Política deberá, además, indicar explícitamente su procedimiento y frecuencia de actualización (idealmente anual), que dé cuenta de los cambios de entorno, nuevas hipótesis de escenario y todo otro factor que pueda incidir en su aplicabilidad y resguardos.

La Política deberá velar por el resguardo, confidencialidad, integridad y disponibilidad de la información, propiciando métodos para el desarrollo seguro, de manera que también se establezcan lineamientos para que los OAEs realicen o contraten desarrollos considerando estándares de seguridad de la información y la privacidad desde el diseño inicial. Para todo lo anterior, deberá identificar y desarrollar a lo menos lo siguiente:

**Objetivos generales y específicos**

Contendrá los objetivos esenciales que persigue el OAE en la materia y los indicadores con los cuales medirá el cumplimiento de la política.

Para tener como referencia al momento de elaborar la Política, y sólo de modo ilustrativo, se pueden definir objetivos similares a:

|  |
| --- |
| Ejemplo de objetivos generales |
| Asegurar la confidencialidad, integridad y disponibilidad de los activos de información a través de la ejecución de políticas, gestión de riesgos y aseguramiento informático de las plataformas de tecnologías de la información.  Reflejar el compromiso, apoyo, interés, fomento y desarrollo de una cultura de seguridad informática y de seguridad de Ia información institucional. |

|  |
| --- |
| Ejemplo de objetivos específicos |
| Gestionar de manera adecuada acciones para el tratamiento de incidentes de seguridad de la información.  Generar iniciativas de capacitación y sensibilización de la seguridad de la información para los funcionarios de la institución. |

### [¶](#identificación-y-determinación-del-alcance-de-la-política) **Identificación y determinación del alcance de la Política**

De acuerdo con la Norma Técnica de Seguridad de la Información y Ciberseguridad, los activos de información corresponden a «datos o información cuyo tratamiento es esencial para el funcionamiento y desarrollo del órgano de la Administración del Estado que lo utiliza, genera, almacena, envía o intercambia, y que deben ser protegidos en su confidencialidad, integridad, disponibilidad u otros factores de importancia». En este contexto, todos los activos de información deberán ser identificados, descritos y clasificados, asignándoles un dueño y un custodio (véase **Dueños de los activos de información** y **Custodios** de esta guía) , cumpliendo con los lineamientos de seguridad definidos por la institución. La política establecerá los roles y las acciones que los OAE deben implementar para alcanzar estándares de seguridad apropiados.

### [¶](#indicación-de-la-legislación-y-normas-específicas-y-vigentes-que-resulten-aplicables) **Indicación de la legislación y normas** **específicas y vigentes que resulten aplicables**

Incluirá la identificación, definición y comprensión del contexto regulatorio actual y previsto aplicable al OAE, sus competencias, facultades, funciones y misiones principales con respecto a la seguridad de la información y ciberseguridad, sin perjuicio del cumplimiento de toda [otra normativa que resulte aplicable](https://anci.gob.cl/normativa).

### [¶](#especificación-de-los-roles-institucionales-y-definición-de-responsabilidades) **Especificación de los roles institucionales y definición de responsabilidades**

Deberán considerarse y coordinarse los roles del responsable institucional de seguridad de la información y ciberseguridad, y del responsable de los activos de información.

RESPONSABLE INSTITUCIONAL DE SEGURIDAD DE LA INFORMACIÓN Y CIBERSEGURIDAD

Será el encargado de velar por la seguridad de la información y ciberseguridad en el OAE respectivo, además de asegurar el desarrollo, cumplimiento y actualización de la Política y de gestionar la administración de la seguridad de la información y/o ciberseguridad.

Nota :

Las distintas normas asignan denominaciones diferentes para esta figura. Sin embargo, se trata de roles equivalentes, independientemente de la denominación asignada en cada fuente legal.

* Instructivo Presidencial N° 8, de 2018, sobre Ciberseguridad.
* Decreto N° 7, año 2023, del Ministerio Secretaría General de la Presidencia,  establece Norma Técnica de Seguridad de la Información y Ciberseguridad6.
* Ley N° 21.663: Ley Marco de Ciberseguridad.

RESPONSABLE DE LOS ACTIVOS DE INFORMACIÓN

Deberá realizar la identificación, clasificación y priorización de los activos de información, y gestionar el riesgo y niveles de seguridad asociados. Adicionalmente, para la gestión de cada activo de información, considerado individualmente, se deberán designar los roles correspondientes (véase **Dueños de los activos de información** y **Custodios** de esta guía).

Cada órgano de la Administración del Estado deberá determinar si el rol de responsable institucional de seguridad de la información, y el de responsable de los activos de información se unifican o no en una sola persona. Con todo, es preferible que éstos roles dependan directamente del Jefe de Servicio, antes que ser parte de las áreas de tecnología y/o informática, ya que cumplirán funciones de auditoría y entrega de directrices en todos las materias referentes a seguridad de la información y ciberseguridad del OAE, tanto a las áreas de tecnología como al resto del órgano. El desempeño de estas funciones no podrá ser externalizado bajo ninguna forma (vea Art. 5, inc. 3°, numeral 4 de la Norma Técnica de Seguridad de la Información y Ciberseguridad).

### [¶](#clasificación-de-la-información-tratamiento-y-criticidad) **Clasificación de la información, tratamiento y criticidad**

Contendrá los métodos para identificar el nivel de criticidad de cada activo de información, de manera que pueda proveerse la seguridad de la información y restricción de acceso necesaria, haciéndola concordante con el punto  **Control de acceso de esta guía**. La clasificación de la información deberá vincularse al nivel de sensibilidad y criticidad quecada activo represente para el OAE.

**Gestión de riesgos**

Deberá considerar los aspectos generales que tendrá a la vista el OAE para la evaluación y tratamiento de los riesgos. En ese sentido, deberá indicar los objetivos del órgano, la forma en que se rendirá cuenta y la manera en la que será medido el proceso de gestión.

**Gestión de vulnerabilidades técnicas**

Contendrá todas las medidas adecuadas y oportunas para la identificación de vulnerabilidades de orden técnico. Además, deberá contener las directrices que permitan determinar las funciones y responsabilidades al interior del OAE para la gestión de vulnerabilidades técnicas, incluyendo su monitoreo, evaluación de riesgos de la vulnerabilidad, tratamiento y cualquier otra actividad necesaria para su gestión.

**Control de acceso**

Regulará los procedimientos de acceso y distribución de identidades, cuya administración y gestión reduzca los riesgos de suplantación y accesos no autorizados. Asimismo, se deberá procurar que queden definidas las responsabilidades que cada funcionario o asesor a honorarios deba cumplir en relación con los accesos. Deberá también indicar el procedimiento de recuperación del control del sistema de identidad y las credenciales de acceso, por niveles escalonados y privilegios, en caso de compromiso de una o más credenciales del sistema.

**Respaldos de información**

Deberá indicar los mecanismos, procesos y requisitos para la realización de copias de seguridad de la información, programas y configuraciones, y debe incluir el proceso de restauración de software de relevancia para el OAE. Una vez realizados los respaldos, se deberá chequear su consistencia en función de asegurar el acceso y la calidad de la información protegida para su posterior uso en un eventual proceso de restauración. Este chequeo deberá hacerse de manera periódica y programada, dejando registro de ellos.

De la misma manera, la Política deberá contener las definiciones del proceso de restauración de dichos respaldos, como respuesta frente a la ocurrencia de un incidente de seguridad. Este procedimiento deberá ceñirse a lo indicado en los puntos  **Controles criptográficos** y **Eliminación** de esta guía.

**Continuidad**

Se definirán lineamientos y alcances para construir el plan de continuidad operativa y contingencia9, elaborado para mantener la continuidad en la operación de las plataformas electrónicas del servicio, para los casos en que estas o sus sistemas de información fallen. Este plan deberá contener lo mínimo indispensable para actuar frente a un incidente de seguridad. Así, contendrá desde la identificación de los funcionarios o asesores que responderán al incidente, hasta el desarrollo y aprobación de los planes de recuperación y respuesta que la institución deberá desplegar ante un incidente. Se deberán establecer los planes necesarios que permitan asegurar una continuidad en la prestación de los servicios que cada institución presta.

Nota :

De acuerdo con el art. 8°, literal c) de la Ley N° 21.663, Ley Marco de Ciberseguridad, aquellos  organismos que sean calificados como operadores de importancia vital deberán elaborar e implementar planes de continuidad operacional. De acuerdo con los artículos 39 y 40 de la misma norma, el incumplimiento de este deber implica infracción y su correspondiente sanción. 10. Art. 11 de la Norma Técnica de Seguridad de la Información y Ciberseguridad.

**Controles criptográficos**

Deberá incluir directrices para garantizar el uso eficiente y adecuado de los mecanismos criptográficos, la protección de la confidencialidad e integridad, no-repudio y autenticación. Por cada activo de información, su dueño respectivo deberá definir el nivel de protección necesario, tomando en cuenta sus características y su nivel de riesgo. Además, deberá contener directrices para el uso adecuado y eficaz de la criptografía en el ciclo de vida de la información, desde su transporte (por ejemplo, uso de certificados SSL para comunicación web) hasta el almacenamiento (por ejemplo, respaldos cifrados o bien cifrar determinados campos en una base de datos).

**Privacidad y protección de la información**

Establecerá los lineamientos que permitan adoptar, desde el diseño, los resguardos debidos y necesarios para la protección de los datos personales que se transmitan, interoperen y se almacenen en las plataformas, de acuerdo con la normativa vigente de protección de datos.

**Eliminación**

Deberá disponer los procesos formales para la eliminación segura de los diferentes elementos cuando ya no sean de utilidad para el OAE, o por exigencias legales, o del dueño de la información, respetando los requerimientos de retención de información que imponga la legislación aplicable al organismo respectivo. Asimismo, deberá considerar los mecanismos de registro de cada una de las eliminaciones.

Adicionalmente, este proceso deberá considerar e implementar las directrices específicas para la eliminación de documentos y expedientes electrónicos, entregadas por la Norma Técnica de Documentos y Expedientes Electrónicos, en lo referente a registro de trazabilidad del proceso (Art. 11, del [Decreto N° 10 de 2023](https://www.diariooficial.interior.gob.cl/publicaciones/2023/08/17/43629/01/2361374.pdf), establece Norma Técnica de Documentos y Expedientes Electrónicos para la Gestión de Expedientes Administrativos) e incorporación en la política de gestión documental de cada OAE.

---

**Funciones, Categorías y Subcategorías**

Para la generación e implementación de la Política, los organismos deben atender las funciones y categorías indicadas en la Norma Técnica de Seguridad de la Información y Ciberseguridad. Adicionalmente, se establecen subcategorías, cuyo propósito es disponer de un conjunto de actividades tendientes al logro de resultados específicos.

Las funciones, categorías y subcategorías apuntan a resguardar la confidencialidad, integridad y disponibilidad de la información, documentos, expedientes electrónicos y las comunicaciones oficiales de los órganos del Estado, además de proteger la infraestructura informática que aloja las plataformas relacionadas y las comunicaciones necesarias para su correcta operación. Asimismo, el marco otorga orientación para la creación de entornos y estrategias necesarias para una adecuada administración de la seguridad de la información y ciberseguridad, de acuerdo con los objetivos de cada OAE, la normativa legal vigente y los estándares internacionales pertinentes.

Este marco de trabajo se basa principalmente en la estructura de dominios de NIST. Sin perjuicio de ello, es necesario considerar que ese mismo estándar toma como referencia a otros estándares, tales como CIS, COBIT 5 o ISO, por lo que se consideran además elementos de otras normas, en particular ISO 27.001 y 27.002 y sus respectivas versiones NCH entregadas por el INN (Instituto de Normalización Nacional).

**Función de Identificación**

Corresponde a las acciones, procesos y procedimientos desarrollados por un OAE para lograr un acabado entendimiento organizacional que permita identificar y administrar adecuadamente los riesgos de seguridad de la información y ciberseguridad para procesos, personas y tecnología.

Lo anterior considera la realización de un diagnóstico inicial basado en una auditoría interna, entrevistas u otro medio de valoración definido por cada órgano, que podrá incluir el desarrollo de una plantilla de evaluación preliminar que permita a cada OAE conocer la base desde donde debe dar comienzo al proceso de implementación de la Norma Técnica.

Nota:

Para cumplir con lo requerido en esta función es muy importante que se realice el análisis o levantamiento diagnóstico preliminar, ya que con esto se establecerá la línea base con la cual los OAEs deberán comenzar la implementación de la Norma Técnica y lo detallado en esta guía técnica. Para esto, los OAEs pueden basarse en diferentes herramientas o frameworks, como [MITRE ATT&CK Enterprise](https://attack.mitre.org/), [NIST CSF](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1271es.pdf), [CIS Controls15](https://www.cisecurity.org/controls/v8), ISO/IEC 27001, etc.

**Contexto de la institución o entorno de la institución**

Para una mejor comprensión de sus procesos internos, así como de su entorno, cada OAE deberá analizar, evaluar y comunicar aquellos aspectos de carácter interno y externo que afecten o puedan afectar el desempeño de sus actividades o que, por su alcance, puedan potencialmente afectar a otros OAEs en términos de la seguridad de la información y ciberseguridad.

Asimismo, los OAE deberán considerar las necesidades y misiones relevantes de cada actor que se vincule a ellos en materias de seguridad de la información y ciberseguridad. Para esto, el análisis deberá contener las relaciones y funciones fundamentales, para lo que habrán de detallarse los aspectos legales y regulatorios aplicables, así como las obligaciones contractuales relevantes, las definiciones estratégicas internas -tales como misión, visión, directrices y buenas prácticas-, además de las interdependencias e interconexiones de cada actor vinculado, a través de un diagrama de entorno y una identificación de actores relevantes.

**Gobernanza**

Para efectos de una adecuada gestión de riesgos, que permita mantener un ambiente controlado mediante los respectivos controles, la gobernanza deberá permitir identificar cómo los actores que participan en la materia interactúan y se relacionan, según sus atribuciones y funciones. De este modo, el establecimiento de una gobernanza permitirá comprender las políticas, procedimientos y procesos necesarios para monitorear y gestionar los requisitos regulatorios y legales, e identificar los riesgos operativos y del entorno del OAE. Esto permitirá establecer una adecuada gestión, considerando el desarrollo, ejecución y supervisión de planes, políticas, programas, procedimientos y prácticas que recopilen, controlen, protejan e incrementen el valor de los datos y activos de información.

**Gestión de activos de la información**

Para una adecuada gestión de los activos de información se vuelve necesario identificar y definir roles y responsabilidades para su protección. Por ello, deberán aplicarse todas las medidas necesarias de manera responsable y coordinada, con el objetivo de establecer el nivel de protección requerido.

Para ello, se deberán considerar, al menos, las siguientes subcategorías:

INVENTARIO DE ACTIVOS

Los OAEs deben inventariar los activos de información, tales como dispositivos y sistemas físicos, plataformas de software, sitios web, bases de datos, aplicaciones u otros, que resulten relevantes para la consecución de sus objetivos en el marco de los procedimientos administrativos electrónicos, plataformas de gestión de expedientes electrónicos, comunicaciones oficiales, notificaciones y plataformas relacionadas que estén bajo su competencia. Estos activos deben documentarse y etiquetarse de manera detallada en un inventario de activos de información, cuya actualización debe ser periódica. Para estos efectos los OAEs pueden apoyarse en las definiciones de [ITIL v4 para un CMDB16](https://wiki.es.it-processmaps.com/index.php/Lista_de_control_CMS_CMDB).

DUEÑOS DE LOS ACTIVOS DE INFORMACIÓN

Cada uno de los activos que contenga el inventario antes descrito deberá tener un dueño, quien será el encargado de velar por que los activos bajo su supervisión se encuentren debidamente inventariados, clasificados y actualizados, de acuerdo con el esquema de clasificación y priorización establecido por el responsable de los activos de información para el correspondiente OAE (véase **Responsable de los activos de información** de esta guía).

En el ejercicio de sus funciones deberá:

* Procurar que sean clasificados según su nivel de sensibilidad o criticidad.
* Establecer mecanismos de definición y revisión periódica de las restricciones de acceso a los activos y, en general, asegurar una adecuada gestión de ellos durante todo su ciclo de vida, según lo definido en los lineamientos de control de acceso.
* Tomar los resguardos necesarios para la eliminación de los activos, según lo dispuesto en los lineamientos para eliminación.

Con todo, se recomienda catalogar ciertas características adicionales de los activos ya inventariados, tales como ubicación, tamaño y unidades, departamentos o divisiones que intervienen en su gestión, o quién es su responsable.

CUSTODIOS

Son los responsables de custodiar los accesos a cada uno de los activos de información que la organización utiliza o almacena en sus sistemas de información, ocupándose de los aspectos técnicos y de seguridad para permitir únicamente accesos autorizados a los datos, garantizando así su integridad, disponibilidad y confidencialidad.

CLASIFICACIÓN DE ACTIVOS DE INFORMACIÓN

Cada OAE, a través del responsable de los activos de información, deberá elaborar un esquema de clasificación y priorización de activos de información en función de la criticidad y sensibilidad de su revelación o modificación no autorizada, considerando además su valor comercial, la normativa vigente y obligaciones contractuales aplicables.

Cada activo deberá ser clasificado por su respectivo dueño, de acuerdo a este esquema, y de manera tal que el resultado sea de aplicación transversal al órgano y consistente con el contexto de sus plataformas y activos de información.

A continuación, se presenta un ejemplo de esquema de clasificación y priorización en función de la confidencialidad de la información, según lo descrito en la Norma NCH 27.002, en que la clasificación se realiza según el impacto que tendría la revelación de la información, el nivel de riesgo del activo de información y el potencial perjuicio para la organización. Se consideran los siguientes niveles:

* La revelación de la información no conlleva ningún daño.
* La revelación conlleva un perjuicio menor para las actividades de la institución.
* La revelación tiene un impacto significativo a corto plazo sobre objetivos tácticos u operaciones de la institución.
* La revelación tiene un impacto serio en la institución y conlleva sanciones administrativas, civiles o penales.

Otra forma de clasificar la información podrá realizarse, por ejemplo, en base a la confidencialidad de la misma y el impacto para el OAE en caso de pérdida o robo, en conformidad con los criterios establecidos en el Decreto Supremo N° 83, de 2005, del Ministerio Secretaría General de la Presidencia, que aprueba Norma Técnica para los órganos de la Administración del Estado sobre Seguridad y Confidencialidad de los documentos electrónicos, clasificándolos de la siguiente forma:

* Documentos públicos: aquellos documentos que no son ni reservados ni secretos.
* Documentos reservados: aquellos documentos cuyo conocimiento está circunscrito al ámbito de la respectiva unidad del órgano a que sean remitidos, en virtud de una ley o de una norma administrativa dictada en conformidad a ella, que les confiere tal carácter.
* Documentos secretos: los documentos que tienen tal carácter de conformidad a la legislación vigente, teniendo en especial consideración el artículo 22 de la Ley N° 20.285, sobre Acceso a la Información Pública.

De acuerdo al artículo 23 de la Ley de Transparencia, los órganos de la Administración del Estado deberán mantener un índice actualizado de los actos y documentos calificados como secretos o reservados de conformidad a dicha ley. Para la correcta publicación de dicho índice, los OAEs deberán cumplir con lo establecido en la nueva Instrucción General del Consejo para la Transparencia, sobre Transparencia Activa ([Res. Ex. N° 500](https://www.consejotransparencia.cl/wp-content/uploads/instruccion/2023/01/IG-TA.pdf), año 2022, Instrucción General sobre Transparencia Activa, del Consejo para la Transparencia).

MAPEO DE LA COMUNICACIÓN ORGANIZACIONAL Y EL FLUJO DE DATOS

Se deberán desarrollar e implementar mecanismos y procedimientos adecuados para el monitoreo y control de la comunicación y flujo de datos, de acuerdo con el esquema de clasificación y priorización de activos de información, con el objeto de mitigar los riesgos de una revelación y/o modificación no autorizada o no deseada de información. Para ello, habrá que mantener registro de todos los emisores y receptores de información, sus privilegios y generar los debidos controles y respaldos.

[¶](#gestión-de-riesgos) **Gestión de riesgos**
-----------------------------------------------

Una vez analizado el contexto, y para una adecuada gestión de riesgos, los OAEs deben, en primer lugar, comprender cuáles son las vulnerabilidades que afectan a sus activos junto a los riesgos de seguridad de la información y ciberseguridad que puedan afectarles en el ejercicio de sus funciones. Luego, deben establecerse los procesos de gestión en función de sus prioridades, restricciones y tolerancias, para poder respaldar de mejor manera sus decisiones de riesgo operacionales. Se sugiere el uso -como herramienta de apoyo para la identificación de riesgos- del [Documento Técnico N° 70](https://www.auditoriainternadegobierno.gob.cl/wp-content/upLoads/2022/06/DOCUMENTO-TE%CC%81CNICO-N-70-V03-IMPLANTACIO%CC%81N-MANTENCIO%CC%81N-Y-ACTUALIZACIO%CC%81N-DEL-PROCESO-DE-RIESGOS.pdf): Implantación, Mantención y Actualización del Proceso de Gestión de Riesgos en el Sector Público, elaborado por el Consejo de Auditoría Interna General de Gobierno.

Nota:

Para el análisis de riesgos los organismos se pueden apoyar en diversas herramientas o toolkits que están disponibles, ya sea de pago o gratuitos, como el provisto por [OWASP.ORG](https://owasp-risk-rating.com/) y la plantilla provista por [AGESIC](https://www.gub.uy/agencia-gobierno-electronico-sociedad-informacion-conocimiento/sites/agencia-gobierno-electronico-sociedad-informacion-conocimiento/files/documentos/publicaciones/Guia%20-%20Implantacion%20SGSI%20-%20Inventario%20activos%20y%20Evaluacion%20riesgos_3.xlsx) de Uruguay entre otros que pueden estar disponibles.

En la elaboración de procedimientos para la gestión del riesgo deberán considerarse a lo menos los siguientes puntos:

CONTEXTO DEL RIESGO

El contexto de gestión de riesgos deberá establecerse a partir de la evaluación y comprensión de los ámbitos internos y externos en que se desenvuelve la institución. A partir de este análisis deberán plantearse los objetivos, alcances, prioridades y restricciones del OAE en materias de gestión de riesgos.

DEFINICIÓN Y COMUNICACIÓN DEL NIVEL DE TOLERANCIA Y APETITO FRENTE AL RIESGO

Se deberán determinar y comunicar claramente los criterios de tolerancia y apetito al riesgo del OAE. Una vez identificados los riesgos y definidos su tolerancia y apetito al riesgo, cada OAE deberá establecer las medidas de mitigación basándose en esos criterios.

Por ejemplo, si una plataforma particular se encontrase fuera de servicio por más de una hora, aquello podría considerarse como un nivel de riesgo inaceptable, o no, dependiendo de cómo haya sido definida la tolerancia o apetito al riesgo por parte del OAE afectado, y el eventual impacto en terceros u otros OAEs que dicha indisponibilidad pueda tener.

IDENTIFICACIÓN DEL RIESGO

Se deberán definir y documentar todos los riesgos que pueden conllevar una pérdida potencial para el OAE, además de detallar cómo, dónde y por qué podría ocurrir la pérdida. Para ello, primero se deberán tener identificados los activos de información (véase **Gestión de activos de información** de esta guía), procesos, amenazas de seguridad, controles existentes, vulnerabilidades y las consecuencias que podrían ocurrir si algún activo sufre una pérdida de confidencialidad, integridad y disponibilidad.

La identificación debe incluir los riesgos independientemente de que su fuente esté o no bajo el control de la organización y aunque la fuente o causa del riesgo no sea evidente. Por tanto, la identificación de riesgos debiese incluir aquellos riesgos asociados con servicios de información o datos administrados por otros OAEs, o por terceros, pero que son críticos para el cumplimiento de la misión de la institución, de manera que el organismo considere aquella dependencia y los riesgos correspondientes, y en consecuencia defina medidas de mitigación.

La identificación de los riesgos debe ser consistente con la clasificación y priorización de los activos de información.

ANÁLISIS DE RIESGO

Se deberá determinar el impacto de una pérdida potencial. La estimación del impacto deberá contener un análisis de distintos escenarios, considerando las probabilidades y consecuencias potenciales frente a la materialización de un riesgo sobre los activos y procesos del OAE. Esto se podrá realizar mediante metodologías cualitativas o cuantitativas, por ejemplo, estimando el riesgo a partir de multiplicar la probabilidad de que una amenaza explote una vulnerabilidad por el impacto potencial de que esa vulnerabilidad sea explotada.

EVALUACIÓN DEL RIESGO

Después de realizar el análisis de riesgo, se deberán contrastar las estimaciones de riesgo resultantes con los niveles de tolerancia previamente establecidos (véase subcategoría **Definición y comunicación del nivel de tolerancia y apetito institucional frente al riesgo** de esta guía). En base a esta evaluación, cada OAE deberá tomar las decisiones correspondientes para tratar el riesgo evaluado, según se describe en la siguiente sección.

TRATAMIENTO DEL RIESGO

El OAE deberá identificar y priorizar la mejor opción para abordar el riesgo. Para esto se considerarán las siguientes opciones:

* Tolerar o aceptar el riesgo.
* Mitigar el riesgo, mediante un procedimiento o control.
* Transferir el riesgo, por ejemplo, a un tercero que lo mitigue o acepte.
* Evitar el riesgo, por ejemplo, eliminando la fuente que origina el riesgo.

En todo caso, aquellos activos que se consideren como de alto riesgo siempre deberán ser calificados como tal, independientemente de su tratamiento, conforme al grado de exposición en caso de que sean filtrados.

Se deberán justificar las opciones abordadas para el tratamiento de los riesgos. En caso de la aceptación del riesgo, se deberán explicar y documentar claramente las razones, siendo previamente aprobadas por el responsable de activos de información.

COMUNICACIÓN, MONITOREO Y REVISIÓN DE LOS RIESGOS

Se deberá hacer seguimiento y mantener un registro actualizado de todos los riesgos, procurando comunicar a todos los interesados cuando la situación de un riesgo haya cambiado. El responsable de los activos de información deberá procurar que se realicen o se lleven a cabo las opciones de tratamiento para los riesgos identificados.

Asimismo, se deberá mantener un registro actualizado y permanente de los riesgos, en donde se identifiquen las amenazas y vulnerabilidades de las plataformas y su probabilidad de ocurrencia y la estimación de su impacto potencial. En este registro se especificará claramente el tratamiento o resolución que se brindará a estos riesgos. En caso de que un riesgo sea considerado como aceptado y su tratamiento no sea realizado, se deberá documentar como «riesgo aceptado» en un documento formal que deberá contar con la aprobación del responsable de los activos de información.

### [¶](#relación-con-proveedores) **Relación con proveedores**

Los contratos que la institución mantiene con proveedores para el diseño, desarrollo, operación y mantención de las plataformas o activos de información, u otros servicios que le presten al órgano, deberán alinearse al cumplimiento de la Política de Seguridad de la Información y Ciberseguridad y los atributos de confidencialidad, integridad y disponibilidad dispuestos en la presente guía técnica y toda otra normativa pertinente.

Adicionalmente, los OAEs deberán implementar políticas de gestión de estos contratos, las cuales deberán considerar el desarrollo de un inventario de los mismos, donde estén claramente identificados los proveedores con la individualización de sus respectivas contrapartes técnicas, permitiendo tener el contacto tanto comercial como de soporte con los proveedores, además de información actualizada de los servicios prestados, los plazos contratados y fechas de inicio y vencimiento o renovación en caso de que proceda.

El OAE deberá identificar los riesgos de la cadena de suministro cibernética, y en consecuencia, evaluar y establecer los procesos de gestión de riesgo pertinentes. En ese sentido deberá identificar a los proveedores de servicios informáticos, priorizarlos y evaluarlos mediante un proceso de evaluación de riesgos.

Adicionalmente, el OAE deberá establecer procesos de gestión del servicio con los proveedores, con el objetivo de monitorear, revisar y auditar regularmente la provisión de servicios por parte de éstos, lo que será medido a través de los distintos indicadores que sean acordados contractualmente, por ejemplo, incidentes detectados y la respuesta efectiva, identificación de vulnerabilidades y sus medidas de mitigación, y otros acuerdos de niveles de servicio (SLA) que se hayan establecido.

CONTRATACIÓN DE SERVICIOS EN LA NUBE

Cuando se contrate un servicio en la nube, se deberá especificar la definición de roles y responsabilidades relacionados a dicho servicio, lo que deberá estar detallado dentro de un acuerdo de servicio. Dicho acuerdo puede incluir los siguientes procesos:

* Asegurar la protección de la información frente al término del contrato con el proveedor.
* Realizar revisiones periódicas de cumplimiento técnico.
* Realizar pruebas periódicas de seguridad de la información, cuyos resultados deben ser informados cuando se materialice la resolución de las eventuales brechas de seguridad detectadas.
* Definir auditorías periódicas, cuyos resultados deben ser comunicados a los OAEs.
* Asegurar la recolección, mantención y protección de evidencia, incluyendo logs y hallazgos de auditoría.

El proveedor de un servicio en la nube debe especificar de manera clara y precisa en el contrato o acuerdo complementario, toda la información respecto a las medidas de seguridad de la información que implementará para garantizar el servicio. Esta información variará dependiendo del tipo de servicio en la nube que el cliente está contratando.

La convención que se celebre entre el OAE y el proveedor particular de Nube deberá además indicar claramente el Modelo de Responsabilidades Compartidas, conforme a lo estipulado en el respectivo Convenio Marco, Bases Tipo o Bases de Licitación respectivas, haciendo explícitos los roles y responsabilidad incluidos en dicho modelo para las distintas capas y niveles de servicio.

### [¶](#función-de-protección) **Función de protección**

Son las acciones, procesos y procedimientos llevados a cabo por un OAE con el objeto de desarrollar e implementar medidas de seguridad adecuadas para garantizar la entrega de sus servicios.

**Gestión de servidores, redes, identidad, autenticación y control de acceso a plataformas electrónicas**

El acceso a los activos de información físicos y lógicos y a todas las instalaciones donde se almacenen deberá restringirse a los usuarios, procesos y dispositivos previamente autorizados. Para ello, deberá cumplirse al menos con lo siguiente:

GESTIÓN DE SERVIDORES

Para el resguardo de la seguridad de los servidores, cualquiera sea la ubicación y naturaleza de éstos, como mínimo se deberán abordar los siguientes aspectos:

* I. Administración

Deberán ser administrados por usuarios con roles y responsabilidades definidos paratales efectos y/o dispositivos autorizados. Estos privilegios podrán asignarse y revocarsemediante protocolos que deben ser definidos por la organización.

* II. Registro

Deberá mantenerse registro de los eventos identificados durante las autenticaciones de los usuarios autorizados, operación de las plataformas y de las acciones realizadas dentro de los servidores. Este registro deberá mantenerse por un período mínimo de 12 meses o lo que la regulación propia de cada OAE obligue.

* III. Separación de entornos

Deberá mantenerse la separación de los distintos entornos (producción, pruebas, preproducción y desarrollo), en donde se trabaje de manera independiente y aislada uno del otro.

* IV. Acceso a servidores

El acceso a los servidores deberá estar habilitado sólo mediante redes seguras, por ejemplo, VPN, y favoreciendo el uso de llaves criptográficas (por ejemplo, SSH en servidores Linux y Windows).

* V. Configuración de servidores

La configuración de los servidores no deberá ser la configuración que trae por defecto el sistema, sino que deberá ser adecuada a las necesidades de uso de la institución, y deberá estar formalmente documentada. Esta documentación deberá ceñirse a los lineamientos de  **Procedimientos de control de cambios** de esta  guía.

* VI. Sincronización horaria

Los relojes de los servidores, así como las bases de datos y las aplicaciones relacionadas a las plataformas deberán estar en sincronización con la hora y fecha oficial chilena, que es administrada por el Servicio Hidrográfico y Oceanográfico de la Armada, según lo dispuesto en el DS N°25 de 1966 del Ministerio de Defensa Nacional.

* VII. Gestión de capacidad de software y hardware

Se deberán tener en consideración las capacidades de los servidores, tanto en sus recursos de hardware como de software, incluidos los sistemas operativos, aplicativos y bases de datos, para responder adecuadamente a los requerimientos de las plataformas, resguardar la continuidad operacional y asegurar la calidad del servicio. Estas capacidades del equipamiento deben ser continuamente revisadas, evaluadas y mejoradas cuando corresponda.

* VIII. Redundancia

Los servidores deben contar con redundancia para garantizar la disponibilidad y así mantener el nivel de servicio esperado frente a algún evento disruptivo que ponga en peligro la continuidad operativa. Para ello, al considerar mecanismos redundantes se deberá tener especial cuidado con la integridad y confidencialidad de la información. Estos mecanismos se deben probar con frecuencia para garantizar su efectividad.

* IX. Control de uso y actualización de aplicaciones

Las aplicaciones que contengan los servidores deberán estar restringidas y su utilización debidamente justificada. Además, deberán contar con actualizaciones y parches vigentes, así como licenciamiento vigente, en el caso que corresponda. Se deberá establecer una política o protocolo de actualizaciones y aplicación de parches adecuada para asegurar el cumplimiento.

* X. Mantenimiento

El equipamiento deberá mantenerse en condiciones óptimas, con el objeto de preservar la disponibilidad e integridad continua de las plataformas y sus componentes. De la misma manera, deberán tomarse los resguardos para conservar la confidencialidad de la información contenida en el equipamiento durante el proceso de mantenimiento.

Adicionalmente

• Las mantenciones y/o actualizaciones se deberán realizar sólo por personal autorizado para ello. Si este proceso es realizado en forma remota, se deberán tomar los resguardos correspondientes, como el uso de VPN, llaves de acceso, dispositivos dongle, entre otros.

• Cada mantenimiento preventivo, correctivo o eventuales reportes de fallas deberán ser registrados, de acuerdo con lo indicado en los procedimientos de control de cambios.

* XI. Actualización de software

Se deberán mantener los sistemas operativos actualizados, así como también los aplicativos. Dichas actualizaciones deberán realizarse de acuerdo con las últimas recomendaciones de los fabricantes, y para cada actualización se deberán tener en cuenta los siguientes controles.

• Serán procedentes sólo aquellas actualizaciones que hayan sido autorizadas por el responsable de los activos de información, y que se encuentren debidamente probadas.

• La ejecución de estas actualizaciones estará a cargo de un usuario autorizado y con las correspondientes competencias técnicas.

• Se deberá mantener y actualizar un plan de vuelta atrás, el que deberá ser aplicado en caso de fallas al realizar una actualización o modificación en el sistema.

GESTIÓN DE LAS REDES

Los OAE deberán realizar una adecuada gestión de las redes, de manera de resguardar la confidencialidad, integridad y disponibilidad de los servicios de las plataformas. Para ello se deberá considerar lo siguiente:

* I. Administración

Es necesaria una correcta administración de las redes, cualquiera sea su naturaleza, manteniendo siempre una separación entre entornos.

* II. Monitoreo de eventos

Se debe realizar una adecuada monitorización de eventos y anomalías, de manera tal que permita identificar si corresponde o no a un incidente de seguridad de la información y así mejorar la toma decisiones. Si este fuere el caso, deberá ceñirse a lo indicado en esta guía sobre la gestión de incidentes (ver **Gestión de Incidentes de Seguridad de la Información y Ciberseguridad** de esta guía).

* III. Control de accesos

Los accesos a las redes internas deben ser monitoreados y sólo se debe permitir el acceso a personal autorizado, ya sean funcionarios o asesores a honorarios, que presten soporte o mantención a las plataformas cuya autorización se haya formalizado con anterioridad. En especial, para sistemas o funciones considerados como críticos, los mecanismos de control de acceso deberán orientarse hacia modelos multifactor (2FA, o similares).

* IV. Uso de VPN

Cada OAE deberá utilizar servicios de red privada virtual (VPN) para conexiones desde otras redes hacia las redes internas donde se encuentren las plataformas. Además, se recomienda que este servicio de VPN cuente con una segunda validación de autenticación, por ejemplo, un código OTP.

* V. Monitoreo de puertos

Se deberá administrar y monitorear continuamente el uso operacional de puertos, protocolos y servicios, tanto en dispositivos de red como en servidores y plataformas, para minimizar los riesgos de seguridad.

* VI. Uso, actualización y configuración de cortafuegos (firewall)

La administración de la red deberá complementarse con un sistema de cortafuegos actualizado. La configuración del cortafuego y otros dispositivos, nunca deberá ser la configuración de fábrica de los dispositivos, sino que se debe adaptar a los requerimientos específicos de cada OAE. Además el cortafuegos debe ser monitoreado para prevenir posibles eventos de seguridad.

GESTIÓN DE CREDENCIALES, PRIVILEGIOS Y CONTRASEÑAS

Los OAEs deberán implementar todos los medios necesarios para distribuir y otorgar las autorizaciones de ingreso a las plataformas, de manera restringida, con un mínimo de privilegios y de acuerdo con el rol de cada funcionario o asesor a honorarios, incluyendo niveles agregados de privilegios.

* I. Gestión de credenciales y privilegios

Los OAE deberán contar con procedimientos internos que detallen las acciones a realizar para los siguientes casos:

• Otorgamiento de acceso cuando así lo requieran las funciones correspondientes al cargo.

• Revocamiento de acceso en caso de cese de funciones, renuncia o abandono del cargo.

• Para el caso de otorgamiento de los accesos cuya asignación corresponda a privilegios elevados, se deberá mantener un registro de estos accesos y se deberá revisar continuamente.

• El registro de actividades y acciones sobre las plataformas y/o servidores, cualquiera que sea el tipo, deberá obedecer a lo señalado en la presente guía.

• Para todo otorgamiento de accesos, se deberá contar con un proceso formal de entrega, privilegiando un mecanismo de entrega individual y seguro.

• El procedimiento de control de acceso deberá especificar los mecanismos y frecuencias específicas para la mantención y actualización de llaves y contraseñas de acceso a los activos de la institución.

• La gestión de privilegios deberá tender a un modelo de roles, asignando los privilegios a dichos roles y posteriormente asignando usuarios específicos a uno o más roles. Se deberá evitar la asignación directa de privilegios o accesos a usuarios individuales.

* II. Mecanismos de autenticación y gestión de contraseñas

Los OAEs deberán implementar los mecanismos de autenticación necesarios para asegurar la correcta identificación para acceder a sus plataformas, aplicando las mejores prácticas recomendadas por las normas internacionales vigentes y la [evidencia científica](https://cups.cs.cmu.edu/passwords.html). Entre las consideraciones deberán estar los siguientes aspectos.

a. El diseño de un sistema de autenticación debe tener en cuenta si se privilegiará la protección de las claves contra ataques en línea (online attacks) o fuera de línea (offline attacks). Esta decisión debería estar basada en la naturaleza del sistema de autenticación y en un análisis de riesgos.

b. El diseño de un sistema de autenticación debería tener en cuenta la confidencialidad de la información que ofrece al usuario, y debería forzar una política de contraseñas concordante con ese nivel de confidencialidad  (Véase, por ejemplo, la norma de [NIST sobre niveles de autenticación.](https://pages.nist.gov/800-63-3/sp800-63b.html)  Por ejemplo, si el sistema de autenticación protege el acceso a información personal identificable (PII) del ciudadano, la política de contraseñas del usuario deberá ser más estricta que si la información no es personal o no es identificable.

c. Las políticas de contraseñas deberán tender a requerir claves largas, de 10 caracteres o más. Alternativamente, pueden prohibir contraseñas contenidas en diccionarios de claves comunes o que han sido encontradas en brechas públicas.

d. Las contraseñas siempre deberán almacenarse en forma cifrada, nunca en texto legible, idealmente mediante modelos OneWay Function que impidan el acceso o recuperación de la clave original, en caso de compromiso de lectura de la base de datos de credenciales.

e. Dependiendo de la confidencialidad de la información contenida en los sistemas, se recomienda evaluar la implementación de múltiples factores de identificación.

f. No requerir ni forzar el cambio periódico de contraseñas, a menos que se sospeche que ha habido accesos no autorizados a una o más cuentas.

g. En el proceso de autenticación con terceros nunca se deben almacenar temporalmente las contraseñas o usuarios. En caso de requerir autorizaciones de terceros, se debe utilizar estándares como OAuth2.

h. La comunicación para administrar autenticaciones y contraseñas siempre debe hacerse usando comunicación encriptada, y además las credenciales deben ir encriptadas.

i. Al crear un nuevo usuario, las credenciales nunca deben ser entregadas por edios de comunicación inseguros, como son los mensajes de texto o correos electrónicos, por ejemplo. Nunca se deben entregar juntos el identificador de usuario y la contraseña asignada, y de preferencia se debe forzar el cambio al primer uso de la contraseña asignada.

### [¶](#concienciación-y-formación) **Concienciación y formación**

Será responsabilidad de cada OAE el procurar la capacitación a sus funcionarios y asesores a honorarios, incluidos los cargos superiores y los encargados de la seguridad lógica y cibernética, de acuerdo con su rol y responsabilidades, y con apego a lo descrito en esta Guía Técnica de Seguridad de la Información y Ciberseguridad.

Cada OAE deberá desarrollar y mantener un plan de capacitación anual en seguridad de la información y ciberseguridad, que brinde conocimientos sobre la materia a sus funcionarios y asesores a honorarios.

El plan deberá contar con:

a. El detalle de campañas, recordatorios, folletos o afiches en torno a la seguridad de la información y ciberseguridad. Deberá mantenerse registro de estas actividades, así como también de las capacitaciones realizadas a los funcionarios.

b. Detalles y alcance de las responsabilidades y compromisos asociados a la seguridad de sus plataformas electrónicas, según lo dispuesto en esta guía, y de acuerdo con el rol que se ha definido y que le corresponda a cada funcionario y asesor a honorarios.

c. Declarar explícitamente el impacto potencial, que tendría una falla en la seguridad de la información o en la ciberseguridad.

d. Los mecanismos necesarios para que cada funcionario y asesor a honorarios conozca y refuerce los procedimientos y políticas internas de cada OAE. Para ello habrá que:

* Detallar la metodología de manejo y reporte de los incidentes.
* Difundir buenas prácticas en el resguardo y conservación de la información, de acuerdo con su clasificación.
* Difundir buenas prácticas en el resguardo y protección de las contraseñas y credenciales de accesos, entregadas para acceder a las plataformas del organismo, así como en el buen manejo de equipos personales que interactúen con las plataformas.
* Detallar los mecanismos de comunicación y datos de contacto de funcionarios y asesores a honorarios responsables ante alguna situaciónvimprevista.

El plan deberá revisarse de manera anual. En tanto, su efectividad deberá ser evaluada frecuentemente, de modo que se permita a los OAEs una mejora progresiva en sus propios procesos de concientización y sensibilización en estas materias. Asimismo, el plan deberá activarse ante la llegada de un nuevo funcionario, asesor a honorarios o si se realiza un cambio de funciones que involucre a las plataformas mencionadas.

[¶](#seguridad-de-los-datos) **Seguridad de los datos**
-------------------------------------------------------

Se deberán tomar los resguardos necesarios para salvaguardar y preservar la confidencialidad, integridad y disponibilidad de los datos que el organismo genere, maneje, administre o almacene, de acuerdo con la propia estrategia de riesgos en torno a sus plataformas.

Los lineamientos técnicos contenidos en esta sección serán aplicables a todos los datos de un OAE, tengan o no el carácter de personales, sin perjuicio de que, en este último caso, los OAEs también deberán cumplir con la Ley N° 19.628 sobre protección la vida privada, o aquella que la reemplace.

ENCRIPTACIÓN Y CRIPTOGRAFÍA

La criptografía deberá utilizarse para alcanzar los siguientes objetivos de seguridad:

* Confidencialidad: utilizar cifrado para proteger la información sensible o crítica, en cualquier estado en que se encuentre, así como respaldos de información, cualquiera sea el tipo.
* Integridad/autenticidad: uso de firmas electrónicas o códigos de autenticación de mensajes para verificar la autenticidad o integridad de información sensible o crítica, ya sea en tránsito o almacenada.
* Uso de técnicas criptográficas para resguardar el proceso de autenticación de usuarios o de parte de sistemas que interactúen accediendo o realizando transacciones con usuarios, órganos y recursos del sistema.

Ejemplos de estándares de encriptación utilizados frecuentemente:

* AES (Advanced Encryption Standard): corresponde a un sistema de cifrado simétrico, con lo que tanto el emisor como el receptor cuentan con la misma llave. AES trabaja con llaves de 128, 192, y 256 bits para encriptar, y con bloques de 128 bits para desencriptar. Sin embargo, AES no proporciona un método para compartir las llaves de forma segura; para esto, se puede recurrir a otros métodos de intercambio de claves.
* RSA (Rivest-Shamir-Adleman): corresponde a un sistema de cifrado asimétrico, que comprende el uso de una llave pública y una privada; mientras la llave pública se usa para la encriptación, la privada se utiliza para la desencriptación.
* SHA (Secure Hash Algorithm): un valor hash es un valor único generado a partir de los datos de entrada; lo que se genera es una cadena de caracteres alfanuméricos de longitud fija, permitiendo mayor eficiencia en el procesamiento. SHA se utiliza principalmente para proteger contraseñas, evitando tener que almacenarlas en texto claro. Se recomienda no usar algoritmos de la familia SHA-1, sino que algoritmos posteriores de la familia SHA-2 o SHA-3.

La utilización de los distintos estándares criptográficos implica diferencias en la complejidad de los cálculos, y por tanto del uso de memoria. La elección de uno u otro debiera considerar el costo asociado con los requerimientos de procesamiento, así como los usos en que se implementará la encriptación.

MECANISMOS DE ELIMINACIÓN DE DATOS

Para eliminar de manera segura elementos que ya no sean necesarios, los OAEs deberán adoptar procedimientos formales, de manera de preservar la confidencialidad hasta el momento de su eliminación y reducir el riesgo de filtración de información confidencial a terceros no autorizados. Del mismo modo, deberá tenerse en cuenta el tiempo reglamentario de mantención de estos elementos, ya sea por fines de auditorías internas, legales u otro semejante que impida el borrado.

MECANISMOS DE INTEROPERABILIDAD, INTERCAMBIO Y TRANSFERENCIA DE DATOS

Al respecto, las plataformas deberán:

a. Resguardar la información transferida de cualquier interceptación, modificación o copia no autorizada, errores de ruta o destrucción accidental; lo anterior, para resguardar que se garantice el no repudio de la información transferida.

b. Los OAEs deberán implementar procedimientos formales para intercambiar información, estableciendo las responsabilidades de cada parte con ella. Estos procedimientos deberán incluir:

* Las responsabilidades involucradas sobre los envíos, recepciones y transmisiones. Cada OAE que interopera debe ser responsable de la información disponibilizada y debe procurar que esta esté libre de código malicioso.
* Niveles de acceso y protocolos de comunicación y transporte.
* Funciones, roles y responsabilidades.

c. Interoperar a través de un medio seguro, cuyo cifrado sea de punto a punto, procurando usar un protocolo que no esté obsoleto ni que sea de baja seguridad, de conformidad con la Norma Técnica de Interoperabilidad y las directrices que dicte la Secretaría de Gobierno Digital en la materia.

d. Autenticar de manera segura a nodos y servicios que se conectan al sistema de interoperabilidad, de conformidad con la Norma Técnica de Interoperabilidad.

e. La información personal y sensible debe interoperar bajo un nivel de cifrado alto, cuyo método de control criptográfico debe estar alineado con el acápite sobre controles criptográficos y la Norma Técnica de Interoperabilidad.

f. Toda otra consideración que contenga la Norma Técnica de Interoperabilidad o dictamine la Secretaría de Gobierno Digital.

### [¶](#procesos-y-procedimientos-para-proteger-la-información) **Procesos y procedimientos para proteger la información**

Los OAEs deberán implementar políticas de seguridad, procesos y procedimientos que estén orientados a la protección de los activos y sistemas de información. Para ello deben considerarse al menos las siguientes acciones:

PROCEDIMIENTOS PARA EL DESARROLLO SEGURO DE LAS PLATAFORMAS

Los OAE deberán implementar procesos que involucren la seguridad de la información y ciberseguridad en todo el ciclo de vida de desarrollo de las plataformas, tales como:

* Procurar que el personal de desarrollo de software mantenga un entorno de desarrollo seguro y sea capacitado periódicamente en temas de seguridad.
* Mantener ambientes separados para el desarrollo, testing y producción; a la vez, asegurar que el equipo de desarrollo no tenga acceso a los ambientes de producción, o tenga acceso controlado y en forma temporal. En el mismo sentido, se deberá mantener registro de cada uno de los accesos que éstos realicen a las plataformas de producción.
* Implementar mecanismos de seguridad en los repositorios donde se almacene el código fuente y versionamiento de las plataformas.
* Considerar las pautas de codificación recomendadas para cada lenguaje de programación, framework y servidores, así como elementos de seguridad para las plataformas y la infraestructura que las soporta (con metodologías de desarrollo seguro, como por ejemplo, OWASP).
* Al comienzo del ciclo de desarrollo se deben considerar los requisitos mínimos de seguridad, según las características y tratamiento de la información de las plataformas.
* En las fases posteriores del ciclo desarrollo se deberá contemplar el cumplimiento periódico de hitos de seguridad, tales como análisis ético de vulnerabilidades (ethical hacking), análisis de vulnerabilidades automatizados, pruebas y revisiones de código. Dichas acciones deberán ser efectuadas antes del pase a operación o producción.
* El OAE deberá propender a contar con herramientas de análisis de código automatizadas, de manera de poder detectar, previo al paso a producción, debilidades o vulnerabilidades en el código fuente.

PROCEDIMIENTOS DE CONTROL DE CAMBIOS

Todos los cambios que se realicen sobre las plataformas deberán ser registrados. Del mismo modo, la implantación de estos cambios deberá ser planificada y comunicada a las áreas interesadas, teniendo en cuenta los efectos que esta acción pueda tener sobre la normal operación del servicio. El procedimiento deberá contener como mínimo lo siguiente:

* Revisión para asegurar que el cambio sea pertinente, haya sido autorizado y debidamente probado (por ejemplo, mediante pull requests aprobados y la correcta ejecución de tests unitarios).
* Registro de las actividades ejecutadas durante el cambio.
* Evaluación del riesgo eventual para la seguridad de la información debido a la realización de estos cambios (por ejemplo, mediante herramientas de análisis de código).
* Planes de vuelta atrás (rollback).
* Proceso de solución rápida (hotfix) para gestionar un error, una vulnerabilidad o falla de seguridad que requiera de un cambio de manera rápida o urgente.
* Respaldar el desarrollo mediante gestores de versionamiento que permitan recuperar cualquier estado anterior a la última versión en producción.

PROCEDIMIENTO DE GESTIÓN DE RESPALDOS

Se deberán realizar respaldos de la información contenida en bases de datos, así como de las aplicaciones, de acuerdo al acápite 2.9. Respaldos de información. Se deberá tener en cuenta lo siguiente:

* Los respaldos deben tener una frecuencia de ejecución definida, la que debe ser debidamente documentada y deberá obedecer a lo indicado en el plan de continuidad de la institución.
* Realización de pruebas de integridad de cada respaldo realizado, para asegurar la inexistencia de fallas en la información contenida. Estas pruebas deben incluir verificaciones al medio en donde se almacenan los respaldos, de modo de garantizar que, en la eventualidad de su uso, se pueda ejecutar un procedimiento de restauración de manera efectiva.
* Se debe contar con un procedimiento de restauración de información, desde un respaldo realizado con anterioridad. La ejecución del proceso de restauración debe estar debidamente documentada. Luego de una restauración exitosa de información desde un respaldo, se debe verificar la integridad de los datos recuperados.
* Los respaldos deben almacenarse siempre en una locación geográfica distinta a la ubicación del servidor de la operación.
* Para los respaldos, se debe contar con las mismas medidas de protección indicadas para el servidor, o los servidores, en términos de protección a nivel físico y/o lógico.
* Los respaldos deberán ser cifrados de acuerdo con el acápite sobre controles criptográficos.

PROCEDIMIENTO DE GESTIÓN DE VULNERABILIDADES TÉCNICAS

Se deberá procurar resolver las vulnerabilidades técnicas detectadas de manera oportuna, identificando los riesgos asociados y las medidas efectivas para afrontar dichas vulnerabilidades. Se definirá un procedimiento asociado para su resolución, que categorice las vulnerabilidades según su nivel de riesgo. Para la definición del procedimiento se deberá contemplar lo siguiente:

* Definir líneas de acción en base a roles y tiempos para reaccionar y responder frente a la detección y posterior remediación de las vulnerabilidades, de acuerdo al nivel de criticidad de la vulnerabilidad.
* Gestionar las vulnerabilidades de manera que, una vez detectados los riesgos asociados, sea posible aplicar las correspondientes medidas correctivas, desde la instalación de parches a los sistemas, hasta la aplicación de controles.
* Aplicación de medidas para afrontar las vulnerabilidades detectadas y debidamente gestionadas, de acuerdo con la urgencia de la vulnerabilidad y su resolución. Esta resolución estará enmarcada en la aplicación de controles  relacionados al procedimiento de gestión de cambios o, si fuere el caso, de acuerdo con los procedimientos definidos para responder frente a un incidente de seguridad.

PLAN DE CONTINUIDAD

Con el objeto de asegurar la disponibilidad de los servicios brindados por las plataformas, los OAEs deberán procurar identificar las amenazas y riesgos potenciales para la continuidad de las operaciones. Cada OAE deberá considerar lo siguiente:

* Definir una estructura de trabajo interna, que permita actuar en caso de ocurrencia de un incidente o evento disruptivo que interrumpa la continuidad de las plataformas y la disponibilidad de los servicios que se entregan, o bien afecte su confidencialidad, integridad o disponibilidad (por ejemplo, exfiltración de datos o exposición de información). Dicho equipo se denominará “Equipo de Respuesta a Incidentes de Seguridad Informática”(Art. 24, literal d, de la Ley Marco de Ciberseguridad). La definición de esta estructura deberá adecuarse al esquema de roles y responsabilidades, indicado en la presente guía técnica (véase 2.4. Especificación de roles institucionales).
* En caso de tratarse de un incidente de seguridad, deberá estarse a lo indicado en el punto sobre Gestión de Incidentes de Seguridad de la Información y Ciberseguridad.
* Conocer el nivel de riesgos tolerables por las plataformas y el tiempo máximo de recuperación frente a este tipo de eventos.
* Desarrollar o actualizar planes de respuesta y recuperación por plataforma frente a la ocurrencia de un incidente o cualquier evento disruptivo, los que serán activados para mitigar los efectos negativos producidos por dichos eventos sobre la continuidad operativa de las plataformas.
* Desarrollar planes de prueba que den una seguridad razonable frente a la disrupción de los servicios definidos como esenciales.

Al ejecutar las acciones mencionadas frente a la ocurrencia de un incidente, se asegura la vuelta a la normalidad de operación de las plataformas y recuperación de la disponibilidad del servicio que se brinda.

PROCESOS DE RECURSOS HUMANOS

Los OAEs deberán establecer cláusulas de seguridad en los nombramientos de los funcionarios, en los convenios celebrados con asesores a honorarios o en los actos administrativos correspondientes, considerando los siguientes elementos:

* Compromiso y responsabilidades de confidencialidad y no divulgación ni revelación para el manejo eventual de datos personales o sensibles.
* Las responsabilidades y restricciones legales sobre el tratamiento de datos personales o asuntos de propiedad intelectual.
* La responsabilidad sobre la clasificación de la información de acuerdo a los esquemas de la institución, así como la gestión de la información u otros activos.
* La responsabilidad con el manejo de información recibida desde las partes externas.
* Las acciones o sanciones bajo el escenario de omisión de requisitos de seguridad de la información establecidos por la institución.

Estas cláusulas deberán mantenerse vigentes mientras los contratos o convenios entre las partes permanezcan vigentes, salvo que por ley deban extenderse ciertas obligaciones de confidencialidad más allá del período de duración de aquellos.

Asimismo, en caso de requerirse, podrán extenderse otras obligaciones por un periodo mayor luego del término del contrato o convenio correspondiente, según el grado de confidencialidad de la información manejada y la definición de riesgos establecidas por el OAE de acuerdo con la legislación aplicable.

[¶](#registro-de-eventos) **Registro de eventos**
-------------------------------------------------

Se deberá registrar de manera regular la actividad de los usuarios administradores de los servidores y plataformas, además de las excepciones, fallas u otros eventos de seguridad de la información. Estos registros deberán contener al menos la siguiente información, cuando esta aplique al evento en cuestión:

* Identificación del usuario que accedió, y su origen (por ejemplo, dirección IP, nombre usuario).
* Registro horario del acceso.
* Números de intentos de acceso fallidos y exitosos.
* Todas las acciones y transacciones realizadas sobre los servidores, servicios y/o las plataformas realizadas en el periodo que duró el acceso.
* Información a la cual se accedió.

### [¶](#función-de-detección) **Función de Detección**

Los OAEs deberán desarrollar e implementar las acciones, procesos y procedimientos necesarios para la detección oportuna de la ocurrencia de eventos de seguridad de la información o ciberseguridad. Esto implica aplicar las acciones de monitoreo que sean necesarias para poder cumplir con lo requerido.

### [¶](#análisis-de-eventos) **Análisis de eventos**

Este monitoreo deberá incluir, al menos, el análisis de los eventos registrados, del entorno físico/lógico, actividades asociadas al personal y a proveedores, detección de código malicioso y amenazas y vulnerabilidades de las plataformas o sus componentes.

Se deberán analizar los eventos de seguridad registrados con el objeto de identificar posibles anomalías, fallas o eventos precursores que pudieran derivar en un incidente de seguridad. Este análisis deberá contener a lo menos:

* Identificación de la causal de origen.
* Identificación del posible motivo del evento.
* Posible correlación con eventos anteriores.
* Determinación del impacto potencial del evento para las plataformas y así poder estimar el nivel de riesgo del evento analizado.
* Disponer de herramientas de correlación de logs y envío de alertas tempranas.
* Las instituciones deberán generar un mecanismo para separar aquellos eventos que no suponen un riesgo de seguridad, o bien que están dentro de su nivel de riesgo tolerable, de aquellos eventos que suponen un riesgo para las plataformas y por ende deben seguir siendo analizados en mayor profundidad.

### [¶](#monitoreo-continuo-de-la-seguridad) **Monitoreo continuo de la seguridad**

GESTIÓN DEL CÓDIGO MALICIOSO

Los servidores y las plataformas deben contar con medidas adecuadas para la protección contra código malicioso, entre ellas:

* Instalar y actualizar de manera frecuente y automática mecanismos de protección de código malicioso.
* Realizar revisiones rutinarias y frecuentes a las plataformas, en búsqueda de cualquier evidencia de archivos o modificaciones sin autorización. Estas revisiones deberán incluir a la red de datos donde se encuentren los componentes de las plataformas.
* Incorporar dentro del plan de continuidad operativa las actividades necesarias para recuperar las funciones después de un evento de código malicioso, incluyendo los datos de respaldo de las plataformas.
* Analizar las características y el comportamiento del código malicioso en caso de detectarse.
* Contemplar todas las acciones necesarias para detectar la ejecución de comandos por usuarios no autorizados.

MONITOREO DE LA RED

Se deberá administrar, supervisar y controlar las redes para proteger la información y las plataformas y así garantizar su seguridad. Para ello se deberán considerar los siguientes elementos:

* Solo pueden acceder a las redes los funcionarios, asesores a honorarios, proveedores expresamente autorizados y plataformas cuya autorización se haya formalizado con anterioridad.
* La administración de la red deberá complementarse con un sistema de cortafuegos. La configuración de este y otros dispositivos nunca deberá ser la configuración de fábrica de los dispositivos.
* Se deberá contar con mecanismos de registro y monitoreo del tráfico de la red que permitan la identificación del uso normal versus posibles eventos de seguridad.
* Se deberá administrar y monitorear continuamente el uso operacional de puertos, protocolos y servicios en dispositivos en red, servidores y plataformas para minimizar los riesgos de seguridad.
* Se deberán mantener todos los puertos cerrados; sólo cuando sea estrictamente necesario se podrán mantener puertos abiertos, ya sea para mantener la operación o comunicación, o bien por alguna necesidad puntual, debiendo ser controlados y cerrados en cuanto la necesidad haya finalizado.
* Se deben definir criterios para la segregación de las redes en los dominios y el nivel de acceso permitido, según lo indicado en la política de control de accesos, en los requisitos de acceso de las plataformas, y según el valor y la clasificación de la información procesada.

### [¶](#proceso-de-detección) **Proceso de detección**

Cada OAE deberá establecer en sus procesos de detección las actividades que le permitan:

* Establecer los roles y responsabilidades en la detección, comunicación y clasificación de eventos.
* Cumplir, en cada actividad relacionada a los eventos, con los requisitos de seguridad establecidos en la Política de Seguridad de la Información y Ciberseguridad y en el análisis de riesgos.
* Comunicar los eventos detectados y que todos los interesados puedan conocer la información y gestionarla debidamente.
* Contar con mediciones continuas de efectividad del proceso de detección, permitiendo realizar una mejora continua de estos procesos.

### [¶](#función-de-respuesta) **Función de Respuesta**

Los OAEs deberán desarrollar e implementar todas aquellos procesos, procedimientos y acciones, para tomar medidas técnicas y organizativas con respecto a un incidente de seguridad de la información y/o ciberseguridad detectado.

### [¶](#planes-de-respuesta-ante-incidentes) **Planes de respuesta ante incidentes**

Los OAE dentro de su política deberán contar con planes de respuesta inmediata ante incidentes y posterior recuperación. Estos instrumentos deberán contar con lo siguiente:

I. El plan de respuesta ante incidentes debe activarse una vez confirmado un incidente y en consecuencia hayan sido afectadas alguna de las plataformas o cualquiera de sus componentes.

El plan de respuesta debe abordar, al menos, los siguientes elementos:

* Notificar del incidente ala ANCi y al regulador cuando corresponda.
* Identificación de activos, controles, roles y responsabilidades involucradas en el incidente. Para esto, se debe:

• Establecer procedimientos para evaluar el impacto del incidente.

• Establecer procedimientos para evaluar si la red ha sido interceptada o ha sido comprometida con la presencia de un ataque conocido o de día cero y de amenazas persistentes activas o inactivas.

• Establecer procedimientos para determinar si algún dato sensible ha sido comprometido, secuestrado, robado o corrupto y, de ser así, cuál podría ser el riesgo potencial para los titulares de tales datos y las plataformas.

• Establecer procedimientos para evaluar el daño a los servidores.

* Acciones de mitigación: el objetivo es contener de manera inmediata las afectaciones a sistemas, redes, bases de datos y dispositivos para minimizar la amplitud del incidente y aislarlo de la posibilidad de causar daños generalizados.
* Acciones para el restablecimiento de la operación normal:

• Erradicar el riesgo de seguridad para garantizar que el atacante no pueda recuperar el acceso y así repetir el ataque.

• Actualizar sistemas de parches, blindar la infraestructura.

• Cerrar los accesos a la red.

• Modificar contraseñas de cuentas comprometidas.

• Erradicar los archivos infectados y, si es necesario, reconfigurar o reemplazar el hardware (virtual o físico).

• Restaurar el nivel de servicio al estado anterior al incidente.

• Comprobar si hubo exfiltración o pérdida de datos una vez que se ha recuperado la integridad, disponibilidad y confidencialidad de las plataformas y que el servicio ha vuelto a la normalidad.

* Definir los canales de comunicación adecuados durante la mitigación y recuperación del incidente y la aplicación de este plan.
* Preparar y publicar declaraciones internas y públicas tan pronto como sea posible. En dichas declaraciones se debe describir con la mayor precisión posible la naturaleza de la vulneración, las causas de fondo, el alcance del ataque, los pasos a seguir para remediarlo y un resumen de las actualizaciones futuras.
* Asegurar la obtención de las evidencias necesarias para un análisis forense posterior. Por ejemplo, preservar todos los artefactos y detalles de la vulneración para un análisis más profundo del origen, impacto e intenciones.
* Registro y seguimiento del incidente.
* Mantener registro completo del incidente y de la respuesta, incluyendo la hora, los datos, el tipo de incidente, quien lo descubrió, ubicación y alcance del daño causado por el ataque.
* Realizar un informe de respuesta a incidentes que incluya todos los componentes que se vieron afectadas por el incidente.
* Realizar una mejora continua en base a las lecciones aprendidas. Durante el paso de erradicación, se deberá identificar la causa raíz para ayudar a determinar la ruta de ataque utilizada, de modo que se puedan mejorar los controles de seguridad para prevenir ciberataques en el futuro.
* En el caso de existir un compromiso del personal o los roles definidos en el incidente, activar los protocolos de reemplazo necesarios.

### [¶](#análisis-forense) **Análisis forense**

Posteriormente a un incidente y a la aplicación de los planes de respuesta, se deberá realizar un análisis forense, cuyo propósito es el siguiente:

* Recopilar información y evidencia de lo acontecido. Se debe mantener resguardo de la integridad de la evidencia recopilada, procurando su inalterabilidad y resguardo en la cadena de custodia.
* Resolver la debilidad o vulnerabilidad en caso de que estas hayan sido la causa del incidente.
* Actualizar los procedimientos de respuesta ante incidentes en caso de ser necesario, utilizando las lecciones aprendidas durante el incidente y su posterior recuperación.

### [¶](#función-de-recuperación) **Función de Recuperación**

Los OAEs deberán desarrollar e implementar todas las acciones, procesos y procedimientos para mantener los planes de recuperación y restablecer cualquier capacidad, plataforma, sistema, servidor, red o servicio en general que se haya visto afectado debido a un incidente de seguridad de la información y/o ciberseguridad.

**Gestión de incidentes de Seguridad de la Información y Ciberseguridad**

Se deberán implementar las medidas necesarias para gestionar los incidentes de seguridad de manera rápida y eficiente, con un orden claro, consensuado, coordinado y documentado previamente. Para ello se deberá definir y ejecutar un proceso de gestión de incidentes, que contenga al menos las siguientes etapas:

* Se deberá utilizar la escala de la Guía de Notificación de Incidentes de ANCi.
* Determinación del o los activos involucrados y el impacto sobre los servicios b. brindados por las plataformas.
* Descripción de forma e inicio de la ejecución de planes de respuesta ante incidentes y si así correspondiera, la activación del plan de continuidad operativa y contingencia.
* Notificación del incidente al Equipo de Respuesta a Incidentes de Seguridad Informática (“CSIRT de Gobierno”), según la Guía de Notificación de Incidentes.

---

[¶](#revisión-y-actualización-de-la-guía) **Revisión y actualización de la Guía**
---------------------------------------------------------------------------------

La presente guía deberá ser revisada, al menos, cada año a fin de determinar si requiere o no de actualización. Las actualizaciones de esta guía deberán tomar en consideración los aprendizajes y las dificultades de aplicación transversales, así como impulsar las buenas prácticas y minimizar las incorrectas que se pudieren haber presentado.

Se deberá dejar registro de todas las versiones y adecuaciones que se le hayan realizado a la presente guía.

Control de versiones

|  |  |  |
| --- | --- | --- |
| Versión | Fecha | Descripción |
| 1.0 | 24/03/2025 | Versión inicial |