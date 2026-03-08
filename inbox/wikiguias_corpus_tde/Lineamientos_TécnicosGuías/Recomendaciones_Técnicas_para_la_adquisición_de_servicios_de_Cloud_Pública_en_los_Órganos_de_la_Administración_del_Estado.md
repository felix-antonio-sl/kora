---
title: "Recomendaciones Técnicas para la adquisición de servicios de Cloud Pública en los Órganos de la Administración del Estado. "
url: "https://wikiguias.digital.gob.cl/guias/guias/recomendaciones_cloud"
category: "Lineamientos Técnicos/Guías"
tags: [{'tag': 'guía técnica', 'title': 'guía técnica'}, {'tag': 'cloud', 'title': 'cloud'}]
description: "Documento con recomendaciones técnicas para la adquisición de servicios de Cloud Pública por parte de los órganos de la Administración del Estado de Chile"
updated_at: "2025-10-07T22:54:40.625Z"
---

[¶](#recomendaciones-técnicas-para-la-adquisición-de-servicios-de-cloud-pública-en-los-órganos-de-la-administración-del-estado) Recomendaciones técnicas para la adquisición de servicios de *Cloud* Pública en los órganos de la Administración del Estado
===========================================================================================================================================================================================================================================================

[¶](#objetivo)   Objetivo
-------------------------

Este documento, elaborado por la Secretaría de Gobierno Digital (SGD), tiene como objetivo entregar un conjunto de recomendaciones técnicas para la adquisición de servicios de *Cloud* Pública por parte de los órganos de la Administración del Estado de Chile (OAE), particularmente para los profesionales TI involucrados en la etapa de precompra[1] de dichos servicios. Además, se contemplan algunas consideraciones generales para la elección del proveedor *Cloud* más adecuado y algunos elementos necesarios para definir los *SLA*[2].

[¶](#alcance) Alcance
---------------------

 El presente documento, de carácter consultivo, se limita a orientar la toma de decisiones en la definición del requerimiento técnico para la adquisición de servicios en la Nube Pública, contribuyendo también a la formulación de proyectos en el marco del proceso EvalTI[3], no pretendiendo resolver problemáticas ajenas a dicho alcance (tales como preservación digital, seguridad de la información o determinación de mecanismos de compra).

[¶](#agradecimientos) Agradecimientos
-------------------------------------

 La Secretaría de Gobierno Digital agradece los valiosos aportes de los integrantes del Consejo de Política de Suministro TI y los comentarios y sugerencias de la industria tecnológica nacional, agrupada a través de sus asociaciones gremiales ChileTec y  ACTI A.G.

[¶](#consideraciones)  Consideraciones
--------------------------------------

 Este documento está en permanente revisión, siendo esta su segunda versión, la cual incorpora nuevos temas, sugerencias y comentarios. Su contenido se actualiza periódicamente en función de su uso por los profesionales, reformas normativas o disponibilidad de nuevas tecnologías. Para esto, la SGD ejecuta diversos mecanismos de consulta, de manera de incluir a los órganos de la Administración del Estado, expertos, sociedad civil y a la industria en la actualización de su contenido.

[¶](#capítulo-1-árbol-de-decisiones-para-la-compra) Capítulo 1: árbol de decisiones para la compra.
===================================================================================================

[¶](#conceptos)   **Conceptos**
-------------------------------

* ***Cloud Computing*****:** modelo que permite el acceso bajo demanda y a través de la red, a un conjunto de recursos compartidos y configurables (redes, servidores, capacidad de almacenamiento, aplicaciones y servicios) que tienen la gran ventaja de ser asignados y liberados con una mínima gestión por parte del proveedor del servicio (Citado en Nigro, 2022; NIST, 2011)[4].
* **Nube Primero (Cloud First):** este principio apunta a que los órganos públicos evalúen el uso preferente de servicios en la nube para el diseño e implementación de sus arquitecturas tecnológicas, con mayor prioridad que el uso de infraestructuras propias o administradas por la institución (OnPremise, housing o similares), observando principios de eficiencia, legalidad, neutralidad tecnológica y seguridad[5].
* **Nube Inteligente (Cloud Smart):** este principio apunta a que los órganos públicos deben considerar sus objetivos estratégicos, modelos de operación, consideraciones financieras y  protección a los datos al momento de adoptar y operar sus soluciones en la nube.  Este concepto puede armonizarse con Cloud First para crear una estrategia gradual, integral y efectiva de adopción de la nube.
* **Territorialidad de los datos:** la utilización de *Cloud* Pública lleva implícita la conexión vía internet, lo cual no reconoce territorialidad. En dicho sentido, la normativa chilena, por regla general, no exige que los datos deban estar ubicados dentro de las fronteras nacionales. Lo anterior permite el uso de este modelo tecnológico por parte de los OAE, salvo que exista alguna normativa sectorial o interna que disponga que la ubicación de los datos deba mantenerse dentro del territorio nacional.

[¶](#criterios-generales-para-el-uso-de-cloud-pública) **Criterios generales para el uso de Cloud Pública**
-----------------------------------------------------------------------------------------------------------

La decisión de mover cargas tecnológicas hacia el *Cloud* Público (utilizar *Cloud*) es más que una determinación institucional de contratar servicios externos de infraestructura, puesto que la decisión requiere un diseño estratégico mínimo y el cumplimiento de diversas etapas y actividades, lo cual incluye, a lo menos:

* Una evaluación de las reales necesidades.
* Definición de expectativas.
* Disponibilidad de capacidades profesionales (internas y/o externas).
* Una planificación detallada y
* El diseño de un nuevo modelo de operación.

 El modelo *Cloud* Público promueve la disponibilidad y se compone de cinco características esenciales:

* Autoservicio bajo demanda.
* Amplio acceso a la red.
* Agrupación de recursos.
* Elasticidad rápida y
* Servicio medido [6].

 Conforme a ello, la utilización correcta de servicios de *Cloud* Pública ofrece múltiples oportunidades para las organizaciones en diversos ámbitos:

* Actualización tecnológica permanente.
* Disminución de personal dedicado a la operación.
* Respaldos.
* Gestión permanente de seguridad.
* Flexibilidad.
* Escalabilidad.
* Continuidad operacional.
* Menores montos de inversión.

 El uso de *Cloud* Pública requiere de personas con conocimientos más específicos en diversos temas, lo cual exige un diseño con mayor detalle del plan de migración y la cobertura de los múltiples roles requeridos.

 Desde un punto de vista financiero, al ser un modelo basado en *OPEX* (gastos de operación) versus *CAPEX* (inversión), también facilita la asignación de recursos para servicios *Cloud*.

 Respecto a la propiedad de los datos se debe verificar, para la contratación de servicios de Nube Pública y especialmente servicios SaaS, que los términos de servicio sean explícitos en indicar que los datos son propiedad del OAE contratante y que no se transfiere en ningún momento la propiedad o el derecho a uso de dichos datos hacia el proveedor del servicio. Así también, los datos (y metadata asociada) pueden ser solicitados por el OAE en cualquier momento, usando formatos estándar para transferencia de información y de ser requerido, el detalle explicativo de la data recibida. Estos criterios requieren en particular una estricta observación al término del contrato de servicios.

[¶](#preguntas-clave-para-decidir-utilizar-servicios-en-el-cloud) **Preguntas clave para decidir utilizar servicios en el** ***Cloud*****:**
--------------------------------------------------------------------------------------------------------------------------------------------

 Este conjunto de preguntas tiene por objeto ayudar a un proceso interno de decisión y diseño de la compra, que de respuestas precisas para una migración o uso de servicios *Cloud* Público, sobre la base de experiencia y recomendaciones de buenas prácticas.

 A continuación se sugiere seguir este breve cuestionario compuesto de un grupo de preguntas de respuesta simple: Sí o No, las que verifican la preparación y madurez necesaria en la Institución para implementar un proyecto exitoso de adopción del *Cloud*. La principal recomendación es que para asegurar un proyecto de adopción exitoso de Cloud Pública, deben cumplirse las condiciones que aseguren un Si a estas preguntas.

 Cabe mencionar que  son de carácter higiénico y contemplan aspectos específicos que se espera estén resueltos, ya sea mediante recursos internos o externos.

 Terminadas las preguntas y si el resultado ha sido exitoso, puede pasar al siguiente capítulo que indica «qué comprar».

**Árbol de decisiones:**

**1.- ¿Cuenta con un equipo de trabajo de al menos dos profesionales, internos o externos, con experiencia en control y gestión de** ***Cloud*** **y que sean Administradores de Sistemas,** ***Devops*** **y/o** ***SREs*****?**

**Si su respuesta es SÍ, vaya a la pregunta 2.**

Si su respuesta es NO, la recomendación es que diseñe un mecanismo que permita contar con al menos 2 profesionales idóneos (ya sea de manera interna o externa) y pase a la pregunta 2.

**2. ¿Tiene sistemas productivos** ***legacy*** **que son críticos y que no puede migrar aún hacia tecnologías más modernas?**

 Si su respuesta es SÍ, pero requiere con urgencia migrar sus sistemas por obsolescencia tecnológica de la infraestructura base u otras condiciones de seguridad y operación, evalúe la migración a través de procesos “*lift and shift*” hacia la Nube, como una medida **temporal y parcial** hasta lograr la actualización y pase a la pregunta 3.

**Si su respuesta es NO, continúe con la pregunta 3.**

**3. ¿Los sistemas que usted administra deben escalar de manera repentina y muchas veces no predecible?** (el concepto **“*****escalar”*** se refiere a que su capacidad de cómputo o de almacenamiento está sujeto a crecimientos temporales y bruscos o bien a un crecimiento sostenido y sin horizonte, predecible en el tiempo).

**Si su respuesta es SÍ, continúe con la pregunta 4.**

Si su respuesta es NO, la recomendación es que evalúe *Cloud* Pública contemplando sólo las capacidades que utiliza actualmente, considerando a lo más el crecimiento vegetativo de su plataforma o bien opciones de *housing/hosting* que le permitan un crecimiento moderado y predecible en el tiempo. Una vez determinados esos parámetros, pase a la pregunta 4.

**4. ¿Tiene documentadas sus aplicaciones, infraestructura y sistemas?**

En particular, con los siguientes instrumentos:

1. Diagrama de infraestructura.
2. *CMDB* (base de datos de configuración).
3. Diagramas de despliegue o equivalentes.
4. Demanda de transacciones por unidad de tiempo (segundo, minuto).
5. *RTO y RPO* para sistemas críticos.
6. Mapa de procesos y su vinculación con sistemas.

**Si su respuesta es SÍ para los 6 instrumentos señalados, continúe con la pregunta 5.**

Si su respuesta es NO a alguno de esos puntos, la recomendación es que establezca un Proyecto de Migración que incluya una estrategia y un plan de actividades que responda a las preguntas previas (antes del inicio de la adopción de *Cloud* en la Institución) y que permita tener esos instrumentos bien definidos y documentados. Una vez documentados estos puntos, pase a la pregunta 5.

**5. ¿Tiene conocido y planificado (por ejemplo, Gantt) las actividades y el tiempo que le tomará migrar sus sistemas al** ***Cloud*****, con recursos propios o externalizados?**

**Si su respuesta es SÍ, continúe con la pregunta 6.**

Si su respuesta es **NO**, la recomendación es que establezca una planificación y documente su plan de migración con los recursos y tiempos adecuados, incluyendo la gestión del cambio necesaria. En este ámbito, proveedores especializados en la adopción de *Cloud* pueden apoyarlo. Pero en cualquier caso, para una buena planificación de la migración, debe tener resueltos los puntos indicados previamente. Una vez resuelta la planificación, pase a la pregunta 6.

**6. ¿Posee un área de ciberseguridad y un** ***CISO*****, con recursos propios o externalizados?**

**Si su respuesta es SÍ, continúe con el siguiente capítulo de este documento.**

Si su respuesta es NO, la recomendación es que identifique de qué forma resolverá estas funciones, tanto durante el proceso de adopción como en la operación con el Cloud Público. El rol de *CISO* institucional debe ser un rol interno, aún cuando las labores técnicas y operativas de apoyo pueden ser resueltas mediante apoyo externo. Una vez cubiertas estas funciones, continúe con el siguiente capítulo de este documento.

[¶](#capítulo-2-qué-comprar) Capítulo 2: ¿Qué comprar?
======================================================

 Si su institución cuenta con capacidades de gestión técnica limitadas y requiere un software para una necesidad específica ofrecido por algún proveedor, el cual sólo requiere configuración para ser utilizado (por ejemplo, *ERP, CRM, KMS, CMS,* etc.), la recomendación es que **prefiera soluciones** ***Cloud*** **en una modalidad** ***SaaS*** **o** ***Software as a Service***, por sus siglas en inglés. No se recomienda la compra de *Cloud* Pública para instalar aplicaciones desde cero, ya que se requieren capacidades técnicas de administración y operación similares al *On Premises, lo cual no le permitirá gozar de todos los beneficios de la Cloud Pública*. Para el caso de *SaaS*, utilice servicios que los proveedores ofrezcan listos para su uso. Un ejemplo claro son las plataformas de ofimática *Cloud* como *Google Workspace*, *Office* 365, *Zimbra* u otros.

 Si usted quiere gestionar aplicaciones propias o de terceros que requieren escalar y que usted puede gestionar, modificar, desarrollar, migrar, asignar dinámicamente espacio dedicado (espacios de disco), bases de datos, balanceo de carga y otros similares, además de disponer los recursos profesionales adecuados, **entonces está en condiciones de una compra de infraestructura («capacidades básicas») y de plataformas (base de datos, sistemas operativos, etc) en el** ***Cloud*** **Público, conocido como** ***IaaS*** **(infraestructura como servicio) y** ***PaaS*** **(plataforma como servicio)**.

 Los servicios *Cloud* requieren una cantidad de dinero mensual variable (pues los proveedores cobran por uso) que le permitirá, de manera gestionada y autónoma (vía paneles de control y gestión que los mismos proveedores proveen y que usted debe exigir) adquirir dinámicamente los servicios.

**Algunos servicios que se pueden adquirir en** ***Cloud*** **son:**

1. **Capacidad de cómputo (máquinas y servidores virtuales).**
2. **Gestores y plataformas para contenedores.**
3. ***Network*** **(redes virtuales).**
4. **Bases de datos y** ***big data*****.**
5. **Almacenamiento (espacio en disco).**
6. **Herramientas para seguridad (*****firewalls*** **virtuales, sistemas de detección de amenazas, etc.).**
7. **Entornos de desarrollo.**
8. **Sistemas de gestión de identidad y acceso.**

 Cada proveedor utiliza diferentes nombres y categorías para los servicios antes descritos y un conjunto de soluciones propias y específicas que deberán ser evaluados y seleccionados para cada requerimiento.

 El modelo de compra comúnmente adoptado corresponde a que el proveedor ofrece una cantidad de «créditos» que equivalen a una suma de dinero para la adquisición de servicios *Cloud*. En ocasiones, este monto puede incluir servicios de soporte proporcionados por el proveedor, lo cual también deberá considerarse al realizar la compra.

 La compra debe explicitar los distintos servicios en que serán utilizados los créditos. **En forma no excluyente, puede considerar los siguientes servicios cloud, ya sea en modalidad** ***IaaS, PaaS, BaaS, CaaS y SaaS*****:**

-   Máquina virtual.

-   Repositorios de almacenamiento.

-   Sistema de archivos distribuidos.

-   Servicio de *Kubernetes* elástico.

-   Servicio de balanceo de tráfico.

-   Servicio de bases datos relacional.

-   Servicio de *DNS*.

-   Servicio de red de distribución de contenidos estáticos.

-   Servicio de correos.

-   Monitoreo de infraestructura.

-   Servicio de *WAF*.

-   Servicio de bases datos no relacional (ejemplo *Mongo Atlas*).

-   Servicio de encolamiento.

-   Servicios de *ETL*.

-   Servicio de *data streams*.

-   Servicio de *Datawarehouse*.

-   Servicio de detección de amenazas.

-   Servicio automático de evaluación de seguridad Inspector.

-   Bases de datos como servicio.

-   Inteligencia artificial como servicio.

-   Plataforma de desarrollo de aplicaciones móviles como servicio (*MBaaS).*

-   Servicio de gestión de *API*

-   Servicio de identidad y acceso como servicio.

[¶](#capítulo-3-consideraciones-para-la-elección-del-proveedor-adecuado) Capítulo 3: consideraciones para la elección del  proveedor adecuado.
==============================================================================================================================================

[¶](#características-de-proveedores-cloud) **Características de proveedores** ***Cloud*****.**
----------------------------------------------------------------------------------------------

 Existen diversos tipos de proveedores de servicios *Cloud*, con distintos tipos de capacidades, experiencias, alcances y servicios.

 Una caracterización preliminar tiene relación con el tamaño, alcance y cobertura de la empresa y de sus servicios. En la escala más amplia, se encuentran los ***Hyperscalers***, que son proveedores de servicios *Cloud* globales y generalmente asociados a corporaciones globales de tecnología. En una escala media, **proveedores regionales** (que cubren un continente), generalmente asociados a empresas de servicios tecnológicos y empresas de telecomunicaciones. Y a **nivel local**, empresas nacionales que cubren generalmente un país y ofrecen un modelo de servicios tecnológicos a demanda, más específicos o de alcance más local.

 No existe *a priori* una respuesta de qué tipo de proveedor *Cloud* es mejor para una institución pública. La selección del proveedor adecuado para una necesidad particular de una institución pública dependerá de qué tan específicos son los servicios solicitados, el nivel de disponibilidad (*SLA*) requerido, la capacidad y conocimiento de la institución para realizar la administración de los servicios y los recursos financieros disponibles, entre otros factores.

[¶](#consideraciones-para-la-elección-del-proveedor-adecuado) **Consideraciones para la elección del proveedor adecuado.**
--------------------------------------------------------------------------------------------------------------------------

 Sin ser una lista exhaustiva, hay cinco características clave que cualquier institución pública debería considerar al evaluar proveedores de servicios *Cloud* y que deberían ser contemplados en los requerimientos técnicos respectivos:

1. **Fiabilidad y disponibilidad:**
   1. *Uptime*: se requiere un nivel de disponibilidad adecuado a los niveles de servicio que la institución requiere (que se especifica en un *SLA* que incorpora diversos elementos de servicio). Esto incluye respaldar tanto la infraestructura física como las capacidades de administración y operación.
   2. Centros de datos redundantes: busca garantizar la continuidad del servicio en caso de fallas en un centro de datos. Esta capacidad se aprovecha implementando procedimientos de continuidad operacional que tengan mínimo impacto para los requerimientos de la institución.
2. **Seguridad:**
   1. Cumplimiento normativo: para asegurar el cumplimiento con estándares y regulaciones de seguridad definidos por la normativa.
   2. Gestión de identidad y acceso: se requieren mecanismos y servicios robustos de gestión de identidad y acceso para proteger los recursos *Cloud*, además de procedimientos claros de coordinación con la institución para asegurar los accesos correctos.
   3. Determinación de responsabilidades: debe existir un modelo claro de responsabilidades entre el prestador de servicios *Cloud* y la institución que utiliza sus servicios.
3. **Escalabilidad y flexibilidad:**
   1. Escalabilidad automática: debe permitir un fácil escalamiento de recursos arriba o abajo según las necesidades, siendo en algunos casos fundamental la capacidad de escalabilidad automática para manejar cargas de trabajo variables.
   2. Variedad de servicios: debe ofrecer una amplia gama de servicios para satisfacer diversas necesidades, desde almacenamiento básico hasta servicios de inteligencia artificial.
4. **Rendimiento:**
   1. Redes de Entrega de Contenidos (en inglés *CDN*): la presencia de *CDN* puede mejorar el rendimiento de entrega de contenido. Si la institución lo requiere, es importante verificar si el proveedor ofrece servicios de *CDN* para acelerar la carga de datos y aplicaciones.
   2. Localización de Centros de Datos: la proximidad geográfica de los centros de datos puede influir en el rendimiento. Un proveedor con centros de datos cerca de los usuarios puede ofrecer menores tiempos de latencia.
5. **Soporte y servicio al cliente:**
   1. Niveles de soporte: es crucial realizar una evaluación de los distintos niveles de soporte ofrecidos por el proveedor ante situaciones adversas o incidencias de operación.
   2. Recursos de ayuda y documentación: la disponibilidad de recursos de ayuda, documentación detallada y una comunidad activa puede facilitar la gestión y solución de problemas.

 Antes de tomar una decisión es importante evaluar cómo estas características específicas se alinean con los requisitos y objetivos de la institución. Además, se deben considerar aspectos como costos y términos contractuales al evaluar proveedores de servicios *Cloud*.

[¶](#el-rol-de-los-partners-o-socios-de-negocios-en-el-modelo-de-provisión) **El rol de los Partners o Socios de Negocios en el modelo de provisión**
-----------------------------------------------------------------------------------------------------------------------------------------------------

 En la provisión de servicios de *Cloud* Pública, no siempre se establece una relación directa (tanto técnica como comercial) entre la Institución Pública y el proveedor base de los servicios. En muchos casos, la provisión de los servicios se realiza en modo indirecto a través de un *reseller, partner, socio comercial o distribuidor*, quien es el que realiza la oferta al cliente del sector público, firma el contrato y mantiene la relación técnico comercial permanente. Esto aplica por ejemplo a casi todos los *Hyperscalers* o empresas regionales que operan en Chile.

 Es importante considerar que cada marca de Nube Pública tiene condiciones o restricciones específicas tanto técnicas como comerciales (por ejemplo, capacidades, certificaciones, volumen de negocios) para seleccionar sus partners o socios comerciales (los proveedores de las entidades públicas), en forma complementaria a las condiciones requeridas para que esos proveedores estén habilitados en Mercado Público. Esto puede tener un impacto en la definición del requerimiento, selección del instrumento de compra y el proceso de habilitación en la Nube Pública; conforme a ello, y en concordancia con lo dispuesto en el artículo 35 bis, de la ley N°19.886[7], al tratarse de una contratación compleja, se deberán utilizar los mecanismos de análisis técnico, financiero, de ciclo de vida útil y otros que correspondan, además de los procedimientos de consulta al mercado y otros existentes.

 Esta característica del modelo comercial (marca) y de provisión de Nube Pública (reseller) explica, por ejemplo, que en muchos casos el “consumo” que se puede visualizar en la consola de uso de servicios de Nube Pública, tenga diferencias con el monto final a pagar, ya que se deben incluir márgenes de comercialización, impuestos, conversión de monedas y otros, que impactarán procesos posteriores de presupuesto, facturación y pago. De igual forma, servicios de soporte técnico de primer nivel, generalmente serán provistos por el partner o socio comercial, siendo escalados en caso de ser necesario, al proveedor global.

 La Nube Pública es un modelo de servicios permanentes y recurrentes, en el cual, al momento de formular los requerimientos técnicos y comerciales, se debe establecer con la mayor precisión posible los roles, responsabilidades y funciones que deberá desarrollar cada parte. Lo anterior cobra especial relevancia, puesto que dichas condiciones serán parte del contenido de la relación contractual de las partes.

 Por ello, debe considerarse en la construcción de los requerimientos de compra:

1. Las expectativas técnicas y comerciales que la Institución tiene respecto al modelo de operación de los servicios de *Cloud* Pública.
2. El modelo comercial, que incluye tasas adicionales, modalidad de precios, cobros, impuestos aplicables, que puede variar dependiendo del instrumento de compra que se aplique.
3. El modelo de servicios, que debe incluir:
   1. Responsabilidades y funciones propias de la institución
   2. Responsabilidades y funciones del socio comercial
   3. Responsabilidades y funciones del proveedor de Nube Pública.
   4. El modelo de control de la consola de servicios y la distribución de las responsabilidades en su administración.

[¶](#capítulo-4-consideraciones-de-servicio) Capítulo 4: consideraciones de servicio.
=====================================================================================

[¶](#acuerdos-de-nivel-de-servicio-slas)  **Acuerdos de Nivel de Servicio (*****SLAs*****)**
--------------------------------------------------------------------------------------------

### [¶](#concepto-de-sla)   **Concepto de** ***SLA*****:**

 El Acuerdo de Nivel de Servicio (*SLA*, por sus siglas en inglés) en el contexto de servicios *Cloud*, forma parte de la relación contractual entre un proveedor de servicios y los clientes, que establece los términos y condiciones que rigen la calidad, disponibilidad y rendimiento de los servicios ofrecidos. Este acuerdo define métricas específicas, como tiempo de actividad, tiempos de respuesta y capacidad de almacenamiento, proporcionando un marco para evaluar el rendimiento del proveedor de servicios. Los *SLA* son esenciales para establecer expectativas claras y garantizar la transparencia en la prestación de servicios *Cloud*, permitiendo a los usuarios entender y medir la eficiencia y confiabilidad del proveedor. También proporciona una base objetiva para la resolución de problemas y compensaciones en caso de incumplimientos. La elaboración y el cumplimiento riguroso de los *SLA* son fundamentales para establecer una relación sólida entre los proveedores de servicios *Cloud* y sus clientes.

 Es fundamental que la institución defina SLAs acordes a su misión, visión, objetivos institucionales y el tipo de servicios que va a implementar a través del uso de *Cloud*, para tener una operación más eficiente y optimizar el uso de los recursos comprometidos.

 Ejemplo de valores de *SLAs* en *Cloud* Pública:

* Un servicio de carácter crítico, cuyo uso se realiza mayoritariamente durante horario hábil, podría estar asociado a un *SLA* más estricto durante dicho horario (por ejemplo, si las razones de servicio lo justifican, sería razonable un 99.5% de disponibilidad de las plataformas tecnológicas y media hora de tiempo de respuesta de los equipos de soporte).
* Para el mismo servicio, pero fuera del horario hábil, se podría definir un *SLA* más permisivo (por ejemplo, un 97% de disponibilidad y 4 horas de respuesta de los equipos de soporte frente a incidentes.

### [¶](#elementos-de-un-sla) **Elementos de un** ***SLA***

Un listado no taxativo de elementos que pueden ser incluidos en un *SLA* para servicios *Cloud*, corresponde a:

* **Disponibilidad o Tiempo de actividad (*****uptime*****)**: indica el porcentaje de tiempo que los servicios *Cloud* estarán disponibles para los usuarios. Por lo general, se expresa en términos de «nueves» (por ejemplo, 99.9% de disponibilidad), donde un mayor número de nueves implica mayor confiabilidad (y exigencia).
* **Rendimiento**: indica el compromiso de desempeño (límites y capacidades) de los recursos contratados (capacidad de almacenamiento, potencia de procesamiento, transacciones por segundo procesadas, número de operaciones de I/O por segundo de almacenamiento, rendimiento de la red). Por lo general, se expresa en cantidades esperadas de capacidad por cada componente del servicio.
* **Tiempo de respuesta**: define el período máximo en el que el proveedor de servicios se compromete a responder a una solicitud o incidencia. Este componente es crucial para medir la capacidad de respuesta y eficiencia del proveedor.
* **Mantenimiento programado:** especifica los períodos durante los cuales el servicio puede estar fuera de línea, debido a mantenimiento planificado. Proporciona transparencia sobre posibles interrupciones de los servicios y permite a la institución anticiparlas.
* **Compensación por incumplimiento**: establece las medidas correctivas o compensaciones que el proveedor debe ofrecer en caso de no cumplir con los niveles de servicio acordados. Puede incluir créditos de servicio o extensiones de contrato.
* **Seguridad y cumplimiento normativo**: detalla las medidas de seguridad implementadas por el proveedor para proteger los datos, así como los estándares y regulaciones de cumplimiento que el proveedor debe seguir.
* **Escalación y resolución de problemas**: define los procedimientos para informar y resolver problemas. Esto incluye el proceso de escalación, los plazos para la resolución de problemas y las responsabilidades de ambas partes.
* **Backup y recuperación de datos**: detalla las políticas de copia de seguridad, frecuencia de respaldo y los procedimientos de recuperación de datos en caso de pérdida o corrupción. Asegura la integridad y disponibilidad de la información.

### [¶](#establecimiento-e-implementación-de-slas)  **Establecimiento e Implementación de** ***SLAs*****:**

Es crucial establecer un Acuerdo de Nivel de Servicio (*SLA*) claro en el requerimiento técnico por parte de la Institución Pública y posteriormente controlar su implementación de manera efectiva con el proveedor de servicios *Cloud*. Esto asegurará expectativas claras y garantizará un rendimiento confiable de los servicios.

Algunos pasos y consideraciones para ayudar al establecimiento del SLA:

* **Objetivos y requisitos claros:** definir claramente los objetivos institucionales y los requisitos específicos para el servicio a contratar. Esto incluye identificar los servicios críticos, necesidades de rendimiento y cualquier requisito de seguridad o cumplimiento normativo.
* **Establecer expectativas claras:** definir claramente los objetivos y las expectativas que tiene para el *SLA*. Asegurar que cada métrica y condición esté bien definida y sea comprensible para ambas partes. La transparencia y comprensión detallada desde el principio es esencial.
* **Personalización del** ***SLA*****:** buscar la posibilidad de personalizar el *SLA* según las necesidades específicas de su organización. No todos los servicios son iguales, y un *SLA* adaptado puede garantizar que sus requisitos únicos estén debidamente abordados.
* **Negociación proactiva:** proporcionar métricas y datos específicos sobre el uso proyectado y las expectativas de rendimiento. Esto puede ayudar a fundamentar las solicitudes y facilitar una discusión más informada.
* **Establecer multas y compensaciones claras:** definir claramente las multas por incumplimiento y las compensaciones ofrecidas. Asegurar que estas sean proporcionales al impacto que un incumplimiento podría tener en sus operaciones.
* **Incluir cláusulas de revisión:** integrar cláusulas de revisión periódica en el contrato. La tecnología y las necesidades de servicio cambian con el tiempo, por lo cual es crucial tener flexibilidad para ajustar el *SLA* según sea necesario.
* **Considerar la escalabilidad:** anticipar las necesidades futuras de escalabilidad y asegurar que el *SLA* sea flexible para adaptarse a cambios en el volumen de uso, expansión geográfica u otras expansiones.
* **Mantenimiento de una relación de colaboración:** fomentar una relación de colaboración permanente con el proveedor. Un enfoque de trabajo conjunto puede ayudar a resolver problemas de manera más efectiva y garantizar una comunicación abierta y continua. Una buena práctica es definir reuniones periódicas de revisión del servicio, cumplimiento de los *SLAs* y adaptaciones necesarias.

### [¶](#seguimiento-y-cumplimiento)  **Seguimiento y Cumplimiento**

 Para realizar un seguimiento efectivo y garantizar el cumplimiento de un Acuerdo de Nivel de Servicio en servicios *Cloud*, considere las siguientes recomendaciones:

* **Establecer un equipo de gestión:** definir un equipo dedicado para gestionar y supervisar el cumplimiento del *SLA*, idealmente con representantes de las áreas técnica, legal y de gestión.
* **Definir métricas de monitoreo:** identificar las métricas clave que se deben monitorear para evaluar el rendimiento del proveedor de servicios *Cloud*.
* **Implementar herramientas de monitoreo:** utilizar herramientas de monitoreo y gestión de servicios *Cloud* para realizar un seguimiento en tiempo real del rendimiento y la disponibilidad de los servicios. Estas herramientas pueden alertar sobre posibles problemas antes de que afecten significativamente a los usuarios.
* **Programar revisiones periódicas:** programar revisiones regulares del *SLA* con el proveedor, mediante reuniones periódicas. Estas revisiones deben incluir un análisis detallado de las métricas de rendimiento, la discusión de problemas pasados y la planificación para futuras mejoras.
* **Automatizar informes de cumplimiento:** implementar sistemas de generación automática de informes que muestren el cumplimiento del *SLA*. Es importante que los informes sean claros, detallados y accesibles para todas las partes involucradas.
* **Establecer auditorías periódicas:** realizar auditorías periódicas para evaluar el cumplimiento del *SLA* en profundidad. Estas auditorías pueden ser realizadas por equipos internos o externos y garantizan la conformidad con los términos del acuerdo.
* **Gestión proactiva de problemas:** desarrollar un proceso de gestión proactiva de problemas, identificando desviaciones recurrentes de las condiciones de servicio.
* **Establecer un sistema de seguimiento de incidentes:** implementar un sistema de seguimiento de incidentes que registre y clasifique cualquier interrupción del servicio, que idealmente permite un análisis posterior y ayuda a identificar patrones y áreas de mejora.
* **Revisar y actualizar el** ***SLA*** **según sea necesario:** mantener el *SLA* actualizado y revisar regularmente si las métricas y condiciones establecidas siguen siendo adecuadas para las necesidades cambiantes, realizando ajustes según se considere necesario.
* **Fomentar la comunicación abierta:** establecer canales de comunicación efectivos con el proveedor. La comunicación abierta facilita la resolución rápida de problemas y garantiza que ambas partes estén informadas de cambios en los requisitos o expectativas.

---

[1] Entendido como el proceso de preparación de la contratación administrativa.

[2] Acuerdos de niveles de servicios.

[3] Proceso dirigido a las Instituciones Públicas  con el fin de promover el buen uso de los recursos asignados por el Estado a Tecnología, fomentar proyectos que sean un aporte tanto para la gestión interna de las instituciones como de cara a las personas, e impulsar el uso de tecnologías emergentes, eficiencia en el gasto y transparencia.

[4] [1] NIST. Cloud computing. https: //www.nist.gov/. 2011.CLOUD COMPUTING: RETOS Y OPORTUNIDADES Cloud computing: Challenges and opportunities HECTOR NIGRO 1. Rev. Ingeniería, Matemáticas y Ciencias de la Información Vol. 9 / Núm. 18 / julio-diciembre de 2022;11-16 Link:https://www.proquest.com/openview/d626c4162b23f7a962f05c311303ee2e/1?pq-origsite=gscholar&cbl=3747991

[5] Instructivo Presidencial No. 1 que entrega directrices sobre la evaluación y adopción preferente de servicios en la nube por parte de los órganos de la Administración Central del Estado, 2018

[6] Author: Amini, Mahyar and Jahanbakhsh Javid, Negar, A Multi-Perspective Framework Established on Diffusion of Innovation (DOI) Theory and Technology, Organization and Environment (TOE) Framework Toward Supply Chain Management System Based on Cloud Computing Technology for Small and Medium Enterprises (January 2023). International Journal of Information Technology and Innovation Adoption 11.8 (2023): 1217-1234 Available at SSRN: https://ssrn.com/abstract=4340207.

[7] Art. 35 bis, incisos 4, 5 y 6, ley N° 19.886, que señala “En las adquisiciones y contrataciones complejas y en aquellas por sobre los montos que determine el reglamento, los organismos del Estado deberán previamente obtener y analizar información acerca de las características técnicas de los bienes o servicios requeridos, de sus precios, de los costos asociados, considerando el ciclo de vida útil del bien a adquirir, o de cualquiera otra característica relevante que requieran.

Si para ello es indispensable hacer consultas a terceros ajenos a los organismos del Estado, éstas deberán efectuarse mediante una consulta pública a través del Sistema de Información y Gestión de Compras y Contrataciones del Estado. Excepcionalmente, y en caso de que no se obtenga la información necesaria para efectuar la contratación por medio del sistema correspondiente, las entidades contratantes podrán obtener directamente sus cotizaciones a través de correos electrónicos, sitios web, catálogos electrónicos, listas o comparadores de precios por internet, u otros medios similares, de lo que deberá quedar registro en el Sistema de Información y Gestión de Compras y Contrataciones del Estado.

Sólo cuando sea imprescindible, en consideración al tipo de bien o servicio por adquirir, podrán realizarse reuniones presenciales o virtuales entre funcionarios de un organismo comprador y los potenciales proveedores, con el fin de obtener información sobre dicho bien o servicio. De todas las actuaciones señaladas en este inciso deberá quedar registro en el Sistema de Información y Gestión de Compras y Contrataciones del Estado. En dicho caso, se deberá cumplir con lo dispuesto en la ley N° 20.730, que regula el lobby y las gestiones que representen intereses particulares ante las autoridades y funcionarios”.