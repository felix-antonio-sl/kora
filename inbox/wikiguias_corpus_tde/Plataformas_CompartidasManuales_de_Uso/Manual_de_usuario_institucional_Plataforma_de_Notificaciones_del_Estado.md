---
title: "Manual de usuario institucional: Plataforma de Notificaciones del Estado"
url: "https://wikiguias.digital.gob.cl/Manuales/instituciones-plataforma-de-notificaciones"
category: "Plataformas Compartidas/Manuales de Uso"
tags: []
description: "Describe el uso, principales funcionalidades, configuración de roles y perfiles de usuarios de la Plataforma de Notificaciones del Estado, CasillaÚnica."
updated_at: "2025-10-07T23:05:11.844Z"
---

[¶](#manual-de-usuario-institucional-plataforma-de-notificaciones-del-estado) Manual de usuario institucional: Plataforma de Notificaciones del Estado
======================================================================================================================================================

[¶](#introducción)  Introducción
--------------------------------

El objetivo de este documento es describir el uso de la Plataforma de Notificaciones del Estado, CasillaÚnica,  para las instituciones públicas.

Este sistema estará a disposición de  los funcionarios habilitados, quienes encontrarán funcionalidades que les permitirán: enviar notificaciones electrónicas a los participantes de los procedimientos administrativos que la institución haya subido a la plataforma, ver estadísticas, opciones de administración de usuarios, así como realizar  configuraciones de a  la institución, tales como registro de firmas y logotipo.

Este manual explica el funcionamiento de la Plataforma de Notificaciones, y está focalizado en aquellas funcionalidades de administración del sistema y de acceso a funcionarios de los distintos Órganos de la Administración del Estado, en adelante OAE,  que se integren a la plataforma. Se describe cada uno de los módulos que la plataforma ofrece, los diferentes roles con que se  puede ingresar y opciones del menú disponibles para cada uno.

> En el contenido del documento contratará link en los módulos/temas específicos, **podrá hacer click para ver más  información de un módulo en particular**; se abrirá un nuevo documento con la información detallada y pantallas que describen el funcionamiento de esa sección.

[¶](#descripción-general) Descripción general
---------------------------------------------

### [¶](#plataforma-de-notificaciones) **Plataforma de notificaciones**

La **plataforma de notificaciones**  constituye el canal a través del cual los OAE remitirán las notificaciones electrónicas de los procedimientos administrativos al Domicilio Digital Único de las personas. Está conformada por dos ambientes destinados a:

* **Ciudadanos,** que tendrán acceso a las notificaciones electrónicas y dónde podrán configurar su Domicilio Digital Único, en adelante DDU, y acceder a los mensajes enviados por las instituciones.
* **Instituciones,** donde los funcionarios con permiso de acceso , podrán practicar en forma electrónica las notificaciones de los procedimientos administrativos que llevan adelante, así como la gestión de sus usuarios.
* **API,** es una extensión del ambiente institucional. En él, las instituciones pueden enviar mensajes de forma automática a través de la API, activado desde cualquier sistema dentro de la OAE que gestione los procedimientos administrativos que llevan adelante. Para ver mas detalle sobre el envío de notificación por parte del OAE desde la API, haga click en el enlace: [API-notificaciones](https://docs.google.com/document/d/1YS3ZtH2X2tuQD1lrnaEqRffBjITWjpLGE5Gk6kh-fC8/edit?tab=t.0#heading=h.78o1ffcgsbay)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdgBRMBpcOi0F34qkSFsV9Cbs4KF8OmA8o1Y44GvjREBXWH4qYHmZAGOh8G3gYQ4y7XoQPUCsFw0r-hz9qFbdl8wzlgSbbLAFA4dh1KKFRE41zbpUBN5sCjrEwgnYP3lvOClHeBjRmsVA4UTGIyVSJOIboK?key=iVFjPJUemyGU7tRH3lqfAw)


*Figura 1. Estructura general de la plataforma de notificaciones*

**El ambiente institucional**, es un sitio web para funcionarios, que le  permitirá desde la Plataforma de Notificaciones, CasillaÚnica, enviar mensajes a los ciudadanos personas naturales y jurídicas, que figuren como interesados en los distintos procedimientos administrativos que se inician en los Órganos de la Administración del Estado (OAE). Además, permitirá la configuración y permisos de acceso de los roles de gestión de los OAE, además disponer de un conjunto de estadísticas de uso de la plataforma y de configuración del Domicilio Digital Único, DDU.

> El funcionario podrá pre-visualizar un mensaje enviado como lo vería un ciudadano. Cabe señalar que, por manejar información de carácter confidencial, todas **las** **acciones que realice el funcionario dentro de la plataforma, serán almacenadas en caso de ser necesaria una auditoría**.

### [¶](#módulos-del-ambiente-institucional) Módulos del ambiente institucional

El ambiente institucional consta de módulos que permiten a los usuarios realizar las siguientes acciones:

* [**Configuración**](https://docs.google.com/document/d/16zNugOkhh_4UBHSLYKB7iEfZptOxRMyaNIiZDvnBfMA/edit?usp=sharing)**:** en esta sección se podrá configurar el logotipo, firma y procedimiento administrativo de la institución; estas configuraciones deben ser creadas por el administrador de la institución, previo al envío de los mensajes.
  + El funcionario seleccionará y subirá en la plataforma  una imagen que identificará la institución en todos los mensajes enviados por esta (el sistema solo admite formato PNG y JPG para el logo).
  + También se puede configurar la firma que tendrán los mensajes al final de su contenido, una institución puede tener más de una firma y debe elegir una al enviar un mensaje.
* **Crear mensajes:** en esta sección el funcionario puede crear mensajes para ser enviados a nombre de una institución. Los mensajes estarán identificados con el logo y la firma que se han configurado en la sección anterior y relacionados a un procedimiento administrativo. Se pueden enviar mensajes [simple](https://docs.google.com/document/d/16lZcjk--3Whqf9FkEUnYvPqRedUYAZY-WPtggqByvbA/edit?usp=sharing) y [múltiples](https://docs.google.com/document/d/1zHHz6KeHe7FSsRQbskVNwFaoP_1MGGaDvP6gdYGU8lo/edit?usp=sharing), en la interfaz web y también a través de la API. Para ver mas detalle sobre el envío de notificación por parte del OAE desde la API, haga click en el enlace => [API-notificaciones](https://docs.google.com/document/d/1YS3ZtH2X2tuQD1lrnaEqRffBjITWjpLGE5Gk6kh-fC8/edit?tab=t.0#heading=h.78o1ffcgsbay)
* [**Mensajes enviados**](https://docs.google.com/document/d/1QVpUMyR5iOu-RCswMQMk61IZdyCfMdMuiSEbji8t-Z4/edit?usp=sharing)**:** muestra  un listado  de los mensajes que se han enviado por la institución, ordenado por fecha y hora de envío, muestra datos relevantes del mensaje que se ha enviado. Se puede acceder al detalle de cada mensaje para ver más información y descargar el comprobante o certificado de envío.
* [**Borradores**](https://docs.google.com/document/d/1XWao88gWBHOxKtz5tZPOCV5bbBuPxPdwcDl54P3FN7A/edit?usp=sharing)**:** los borradores son mensajes que se iniciaron pero no se enviaron, se pueden crear desde el módulo de creación de mensajes y se podrá continuar con el envío en cualquier momento. Para recuperar un borrador debe ingresar en esta opción y seleccionar el que necesite de la lista, de esta forma se podrá continuar editando el mensaje y finalmente ser enviado.
* [**Solicitud de excepción**](https://docs.google.com/document/d/1DXPsBV7qwwWstnqpD1_nCZMy5MeZNnAQrzV1oDrU3NM/edit?tab=t.0)**:** En esta opción la institución, previa solicitud de una persona, a través de un funcionario institucional habilitado para tales fines, podrá ingresar un registro de excepción.  Esta acción exceptúa a la persona solicitante de ser notificada por medios electrónicos, en conformidad a lo expresado en el Título V del Reglamento de la Ley N° 21.180, de Transformación Digital del Estado. En este módulo el funcionario realiza la  excepción, a través del registro en un formulario con los datos del solicitante, en este registro se debe indicar los motivos de excepción y dejar un documento que justifique el motivo.
* [**Plantillas**](https://docs.google.com/document/d/1ibXvy-zijC4Vnw4Rk7p1Xj1GOySOjHgom0-q8qH6PEM/edit?usp=sharing)**:** en esta opción una institución puede crear plantillas para los mensajes que envía regularmente.  De esta forma, al crear un mensaje ya se tiene una base, que se puede modificar antes de ser enviado.
* Administración: permite [**administrar usuarios**](https://docs.google.com/document/d/1QGhLaU0-cauPhu7GZCIskghKIIWLpjXu2IJMkyvktTo/edit?usp=sharing), el administrador institucional creará a los funcionarios que podrán realizar envío de mensajes.
* [**Procedimiento administrativo**](https://docs.google.com/document/d/1y0Dfsl5GNUEopxKFpLgkrbelqn6LFdyKJi6GGiUN4O8/edit?tab=t.0#heading=h.b4h7e4y4s0nk): en esta sección se debe seleccionar el /los procedimientos administrativos que la institución tiene planificado notificar. Es importante elegir el procedimiento administrativo que va notificar la institución, uno o varios,  los cuales son tomados del listado que haya cargado en CPAT (Catálogo de Procedimientos Administrativos y Tramitaciones).
* Estadísticas: Módulo donde se puede ver la gestión de envío de mensajes por la institución, tiene varias opciones:
  + [**Estadísticas de mensajes agrupados**](https://docs.google.com/document/d/1nm3oufeIiAoyo79bOkgFKJOWwj74GSRILPVIuerYXvo/edit?usp=sharing)**:** permite visualizar la cantidad de mensajes enviados por la institución en un determinado periodo, se puede filtrar por: rango de  fecha, tipo del mensaje y estado de envío.
  + [**Estadísticas de  Mensajes a destinatarios**](https://docs.google.com/document/d/16VGy0Pif2DB5dpx-dk7Nc8gS6kdwoeqDQnizPqtI2WA/edit?usp=sharing)**:** permite visualizar el detalle de los mensajes enviados a destinatarios en un determinado periodo de tiempo.
    - Se puede filtrar por: rango de fecha, tipo de mensaje, estado o id de envío;
    - Se puede ver la tipificación de envíos de acuerdo a la configuración de DDU de los destinatarios, estado de los mensajes enviados a DDU-casilla y según tipo de mensaje, tipo de configuración de DDU,  tipo de ciudadano y estado del mensaje.
    - También se informa si el mensaje fue leído o no (solo en caso que su DDU esté configurado como casilla).
  + [**Estadísticas de Consulta de mensajes**](https://docs.google.com/document/d/1VarnWcJQzrp-zK5xFZHIzHX1Mrh-trHu8vbVt9yspaE/edit?usp=sharing)**:** permite visualizar el detalle de los mensajes enviados a un ciudadano en particular, ofreciendo una búsqueda por RUT/RUN.

### [¶](#perfil-de-usuario-y-ámbito-de-información) Perfil de usuario y ámbito de información

La SGD podrá definir diferentes roles para la operación de la plataforma de notificaciones. Hasta el momento, se tienen definidos solo dos: administrador de instituciones y administrador de mensajes:

* **Administrador de Instituciones:** El usuario administrador de instituciones, puede configurar y visualizar información de la institución a la que pertenece. Cada institución debe tener al menos un administrador institucional.
* **Administrador de Mensajes:** El usuario administrador de mensajes, es aquel que tiene como función principal el envío de mensajes en la plataforma. Cada institución puede tener más de un administrador de mensajes.

La aplicación cuenta con varios módulos, que serán habilitados según el tipo de usuario que ingrese a la plataforma en el ambiente institucional. Además de los roles que le permiten tener acceso a los diferentes módulos, cada institución solo podrá ver los datos asociados a ella.  A continuación se indican los permisos asignados según el tipo de usuario:

|  |  |  |
| --- | --- | --- |
| **Módulos/secciones de la aplicación** | **Adm. Instituciones** | **Adm de mensajes** |
| Configuración (logo y firma) | Si | No |
| Inicio | Si | Si |
| Crear mensajes | No | SI |
| Mensajes enviados | No | Si |
| Borradores | No | Si |
| Solicitud de excepción | Si | No |
| Plantillas | Si | Si |
| **Administración** |  |  |
| Usuarios | Si | No |
| Procedimientos administrativos | Si | No |
| **Estadísticas** |  |  |
| Mensajes agrupados | Si | Si |
| Mensajes a destinatarios | Si | Si |
| Consulta de mensajes | Si | Si |

*Tabla 1. Roles y permisos*

[¶](#elementos-generales-de-la-aplicación) **Elementos generales de la aplicación**
-----------------------------------------------------------------------------------

### [¶](#ingreso-a-la-aplicación) Ingreso a la aplicación

Para acceder al ambiente institucional de la plataforma de notificaciones, debe colocar en su navegador web la siguiente dirección:

[***https://institucion.casillaunica.gob.cl/***](https://institucion.devel.casillaunica.gob.cl/l)

|  |
| --- |
|  |
| *Figura 2. Pantalla de inicio del ambiente institucional* |

**Para ingresar, el usuario debe estar autenticado y autorizado,** el usuario debe tener un rol dentro de la aplicación.

> La autenticación para el ingreso a la plataforma se realiza mediante ClaveÚnica.

|  |
| --- |
|  |
| *Figura 3. Autenticación de un usuario en el ambiente institucional* |

### [¶](#estructura-y-secciones-de-la-pantalla) **Estructura y secciones de la pantalla**

Al ingresar visualizará una pantalla como se muestra en la figura 4, la cual contiene  una cabecera, un menú lateral, zona de contenido y pie de página, cada una con información y elementos que permitirá navegar por la aplicación.

|  |
| --- |
|  |
| *Figura 4. Estructura de la pantalla* |

### [¶](#cabecera) **Cabecera**

Se ubica en la parte superior de la pantalla y muestra el logo que identifica al producto, nombre de la institución  y un botón para el  cierre  de sesión.

|  |
| --- |
|  |
| *Figura 5. Cabecera* |

### [¶](#barra-lateral) **Barra Lateral**

En esta zona, está disponible el menú del sistema según las opciones que tenga habilitadas el tipo de usuario que ingrese, y permitirá ir a los diferentes módulos; también se identifica al  usuario conectado.

|  |
| --- |
|  |
| *Figura 6. barra lateral* |

### [¶](#zona-de-contenido) **Zona de contenido**

Se desplegará por defecto la página de inicio al ingresar al ambiente institucional, de acuerdo al perfil de usuario que se conecte. En la parte superior izquierda  se podrá observar la ruta de la opción que se esté desplegando en esta zona y el contenido de la opción que solicite en el menú.

|  |
| --- |
|  |
| *Figura 7. Zona de contenido* |

### [¶](#pie-de-página-footer) **Pie de página (Footer)**

Se ubica en la parte inferior de la pantalla y señala la información de horarios de atención de mesa de servicios y un enlace al sitio web de la mesa en caso que quiera resolver alguna inquietud y/o crear un ticket.

|  |
| --- |
|  |
| *Figura 8. pie de página* |

### [¶](#levantar-ticket-a-mesa-de-servicios) **Levantar ticket a mesa de servicios**

En el pie de página de la aplicación se podrá acceder a levantar tickets a mesa de ayuda, además del horario de atención respectivo. Al seleccionar este vínculo ingresará al sitio de la mesa de servicios y si lo desea puede crear una solicitud accediendo a  un  formulario que permitirá enviar sus consultas para ser resueltas por el área respectiva.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcvNLXxReH3WI6vAK9Qd8-7U9G5ILMVpPlXAizpNo2RwmUYbFdio8eRSG3kjaNPRU-0Kf56CelNkbzMN3p2Y7cWJZiI8OQQ_HuyuiB9VOeOZh94zTXaqxgIYdDZm0VnA4tx3oFATw?key=iVFjPJUemyGU7tRH3lqfAw)

### [¶](#cerrar-sesión) **Cerrar sesión**

Una vez que el usuario ha terminado de realizar sus actividades en la plataforma, puede cerrar la sesión haciendo click en el botón ***Cerrar sesión***. Posteriormente,será redirigido a la página principal de la plataforma Institucional.

**Si se detectan 10 minutos de inactividad en la plataforma,** se mostrará una ventana modal informando que se cerrará la sesión, si la inactividad continúa por 2 minutos más y no hay respuesta del usuario, se cerrará la sesión automáticamente y se mostrará una pantalla explicando  lo ocurrido**,** si desea volver a ingresar debe autenticarse nuevamente.

|  |
| --- |
|  |
| *Figura 10. Cierre de sesión por inactividad* |

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdZ80fbBmGORLwKf42dkt7hltbVocW4uXxCM7_xYif9KKixkRm9kqFKw6OAaSKPqjvoSTxJS4E4bml-KCNuFSGso_f6mTEkANU03pMmsFnvmNa8L5eHy1tQybgQ08vT4XP3QeLMrQ?key=iVFjPJUemyGU7tRH3lqfAw)

[¶](#módulossecciones-de-la-aplicación) **Módulos/secciones de la aplicación**
------------------------------------------------------------------------------

### [¶](#configuración) **Configuración**

El menú de configuración se encuentra ubicado en la cabecera y sólo el administrador de la institución tiene acceso a esta funcionalidad.

A través de esta opción  se configura el logotipo y la firma de la institución; ambas configuraciones deben ser creadas previo al envío de los mensajes.

|  |
| --- |
|  |
| *Figura 12. Menú de configuración* |

Cada institución debe tener configurado una imagen o logo que la identifique, para ver más detalle de la opción  Configuración puede hacer click en el enlace => [Configuración](https://docs.google.com/document/d/16zNugOkhh_4UBHSLYKB7iEfZptOxRMyaNIiZDvnBfMA/edit?usp=sharing)

### [¶](#inicio) **Inicio**

Es la página  que se muestra por defecto al ingresar al aplicativo y varía ligeramente de acuerdo al perfil de usuario que ingrese; la página muestra: un saludo con identificación del rol, opción más usada para el rol que ingresó,  datos relevantes relacionados con el envío de mensajes y acceso a los términos y condiciones.

Los accesos directos dependen del perfil:

**Para administrador de institución:** muestra la opción de administración de usuarios, estadísticas y términos y condiciones.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdlAGeK75_E6Nsem5v97pUyhwo76d8K9zXAaLSOaIFucdPq1mGrLMoNKoEMR2dgoTOpXrhLjVLY2V1OTvDDqCia27z3oDgTJ9_zAil9EHc6e7JMBULNjYQZKz92tOLEff3ZxqU4Lg?key=iVFjPJUemyGU7tRH3lqfAw)


*Figura 13. Página de inicio para el administrador de institución*

* **Para el administrador de mensajes**: muestra la opción para crear,  consultar mensajes, consultar configuración de DDU  y términos y condiciones.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXex7OKRMAM99DIKaHzKZyNs4UIIDQ_8GfEkaYLaUagwqG3pEcPVTAKy6VpXLKy4WULFSjmHblbT9UDFAydGW-j2BCpbJcFYzPmzsQe4WJnVSkTit-hTrNZyHv5CXmFiRfyZWrUt?key=iVFjPJUemyGU7tRH3lqfAw)


*Figura 14. Página de inicio para el administrador de mensajes*

La opción **Consulta de configuración DDU**, disponible en la página de inicio del administrador de mensajes, permite saber qué configuración tiene un determinado RUN. Es importante saber que un DDU puede tener alguno de los valores: No configurado, Excepcionado o Casilla.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdYfxaS9tTj9jHEl3IzvwqvcjVzGL0Iw7afxxUo0YoUX9EYhETbHDLlOLCBw6cEMe_J_JMnVdPBG0rldv-K2FjhDmfbm2Cmb8sJmd2UwZlh4QtKg0iiquLcAxKDmP6NSuadrNVIDw?key=iVFjPJUemyGU7tRH3lqfAw)


*Figura 15. Consulta de configuración de DDU*

### [¶](#crear-mensajes) **Crear mensajes**

En esta opción se puede enviar mensajes utilizando el  RUN/RUT del destinatario. La plataforma web ofrece dos opciones para el envío de mensajes:

Mensajes simples, en los cuales un  mismo contenido y adjunto se envía a los mismos destinatarios y  mensajes múltiples, en los cuales un mismo contenido con diferentes adjuntos se envía a distintos grupos de destinatarios.  Puede encontrar  más detalle sobre estos flujos de envío de  mensajes en los enlaces:  [mensaje simple](https://docs.google.com/document/d/16lZcjk--3Whqf9FkEUnYvPqRedUYAZY-WPtggqByvbA/edit?usp=sharing) y/o [mensaje múltiple](https://docs.google.com/document/d/1zHHz6KeHe7FSsRQbskVNwFaoP_1MGGaDvP6gdYGU8lo/edit?usp=sharing)

**Cabe señalar que**

* Un envío puede tener uno o varios destinatarios, que están identificados por su RUT/RUN.
* Un envío puede combinar destinatarios que sean personas naturales y jurídicas.
* El ingreso de destinatarios de un mensaje se puede hacer manual o a través de un listado cargado en un archivo .csv.
* Se pueden adjuntar archivos en un mensaje, deben cumplir con lo siguiente:
  + Límite de tamaño por archivo individual: 20MB
  + Límite de tamaño total de archivos adjuntos: 20MB
  + Los tipos de adjuntos soportados son: pdf, jpg, png, word (doc. docx), excel(xls, xlsx); los pdf con firma electrónica serán validados.
* Los mensajes enviados por defecto serán de tipo  Notificaciones y están asociados a un procedimiento administrativo.

> **Los mensajes simples**, envían a un mismo grupo de destinatarios, un mismo mensaje y archivos adjuntos.
>
> **Los mensajes múltiples**, diferentes grupos de destinatarios comparten el mismo contenido del mensaje y se pueden tener adjuntos por cada grupo.

### [¶](#mensajes-enviados) **Mensajes enviados**

Es un listado de mensajes enviados por la institución,  desde la interfaz web y también desde la API, ordenado de forma descendente por fecha y hora de envío.

**En él se podrá**

* Ver los envíos de mensajes enviados desde la opción: simple, múltiple y desde la API.
* Cambiar la dirección del orden de la lista (ascendente/descendente).
* Realizar búsqueda dentro de la lista.
* Navegar por diferentes páginas de la lista.
* Acceder al  detalle de los mensajes
* Realizar búsquedas

**Además podrá ver**

* Información resumida de cada mensaje: Fecha, hora de envío, asunto, estado de envío, tipo de mensaje, cantidad de destinatarios y adjuntos, si tiene, y el medio de envío, el cual puede ser, WEB o API.
* Acceder a ver más detalle del mensaje haciendo click en el mensaje que desee.

Para revisar más detalles sobre esta opción  puedes ingresar a la documentación de [Mensajes enviados](https://docs.google.com/document/d/1QVpUMyR5iOu-RCswMQMk61IZdyCfMdMuiSEbji8t-Z4/edit?usp=sharing).

### [¶](#borradores) Borradores

Es una bandeja con el listado de los borradores que ha creado la institución, ordenado por fecha y hora, mostrando al inicio los más recientes.

**En esta lista podrá**

* Cambiar la dirección del orden de la lista.
* Realizar búsqueda dentro de la lista.
* Navegar por diferentes páginas de la lista.
* Ver información de los borradores en la lista: fecha y hora de envío, asunto, parte del mensaje, cantidad de destinatarios, si tiene adjuntos.
* Crear un mensaje iniciando con los datos que contiene el borrador.

Para revisar más detalles sobre esta opción puedes ingresar a la documentación de [Borradores](https://docs.google.com/document/d/1XWao88gWBHOxKtz5tZPOCV5bbBuPxPdwcDl54P3FN7A/edit?usp=sharing)

### [¶](#solicitud-de-excepción) **Solicitud de excepción**

En esta opción, la institución- previa solicitud de un ciudadano- podrá  inhabilitar su RUN para que este reciba notificaciones a través de la plataforma. Esto debido a ciertas condiciones que le impiden a la persona solicitante acceder a la plataforma de notificaciones. Si se necesita enviar mensajes a una persona que se encuentra excepcionada, la institución debe habilitar otro mecanismo de comunicación para poder enviar la notificación.

Para revisar más detalles sobre este contenido puedes ingresar a la documentación de [Solicitud de excepción](https://docs.google.com/document/d/1DXPsBV7qwwWstnqpD1_nCZMy5MeZNnAQrzV1oDrU3NM/edit?usp=share_link).

### [¶](#plantillas) Plantillas

En esta sección, se pueden crear, editar, eliminar, duplicar y previsualizar plantillas. El usuario tendrá acceso a cada una de las opciones mencionadas anteriormente de acuerdo a los permisos que tengan asignados, como: Administrador de Institución o Administrador de Mensajes.

Al ingresar a la sección de Plantillas, el sistema muestra la siguiente pantalla.

|  |
| --- |
|  |
| *Figura 16. Listado de plantillas* |

**En la sección de Plantillas podrá:**

* Crear plantilla.
* Buscar dentro de la lista por el autor o editor de la plantilla.
* Realizar filtros,ofrece la opción de filtrar las plantillas por un rango o una fecha específica, a través de los campos Fecha Desde y Fecha Hasta.
* Navegar por diferentes páginas de la lista.
* Editar, previsualizar, duplicar y eliminar las plantillas creadas, en caso de que el usuario/a cuente con los permisos asignados para ello.

Para revisar más detalles sobre este contenido puedes ingresar a la documentación de [Plantillas](https://docs.google.com/document/d/1ibXvy-zijC4Vnw4Rk7p1Xj1GOySOjHgom0-q8qH6PEM/edit?usp=sharing).

### [¶](#administración) **Administración**

Esta sección ofrece la funcionalidad para la administración de Usuarios. A través de ella, el usuario institucional tendrá acceso a  crear nuevos usuarios con el rol de administrador de mensajes, dentro de su institución, y modificar/eliminar.

#### [¶](#usuarios) **Usuarios**

Permite la administración y creación de los usuarios que podrán enviar mensajes dentro de la institución.

Para revisar más detalles sobre este contenido puedes ingresar a la documentación de [Administración de usuarios](https://docs.google.com/document/d/1QGhLaU0-cauPhu7GZCIskghKIIWLpjXu2IJMkyvktTo/edit?usp=sharing)

#### [¶](#procedimiento-administrativo) **Procedimiento administrativo**

Permite a la institución seleccionar, desde los procedimientos administrativos (PA) que la institución cargó en CPAT, los PA que la institución va a notificar.

|  |
| --- |
|  |
| *Figura 17. Listado de procedimientos administrativos cargados en notificador* |

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcPrkCohN8-SsAOOF-T6uZvnhoF1MMdCShHsyn093EFVPHlBeMLXRgXS-t_MZZ4ZZYSIC1xOoc-6_AesXyuVYJHdCRT8SNOe7Czg-9BMjA1qiDL15_SIdHjTUn2SoTnPPcOR5DE5Q?key=iVFjPJUemyGU7tRH3lqfAw)


Figura 18. *Listado de procedimientos cargados por una institución en CPAT*

### [¶](#estadísticas) **Estadísticas**

En este módulo la institución podrá visualizar los envíos de mensajes que han realizado, están organizados de acuerdo a: cantidad de mensajes que se han enviado, destinatarios de esos mensajes y mensajes que ha recibido un RUT/RUN en particular.

#### [¶](#mensajes-agrupados) **Mensajes agrupados**

Permite visualizar la cantidad de mensajes enviados por la institución en un determinado periodo. Para revisar más detalles sobre este contenido puedes ingresar a la documentación de [Mensaje agrupados](https://docs.google.com/document/d/1nm3oufeIiAoyo79bOkgFKJOWwj74GSRILPVIuerYXvo/edit?usp=sharing).

#### [¶](#mensajes-a-destinatarios) **Mensajes a destinatarios**

Permite visualizar el detalle de envío de los mensajes a sus destinatarios en un determinado periodo de tiempo por: tipo de configuración de DDU, tipo de ciudadano y por estado del mensaje. También se informa si el mensaje fue leído , solo en caso que su DDU esté configurado como casilla. Para revisar más detalles sobre este contenido puedes ingresar a la documentación de [Mensajes a destinatarios](https://docs.google.com/document/d/16VGy0Pif2DB5dpx-dk7Nc8gS6kdwoeqDQnizPqtI2WA/edit?usp=sharing).

#### [¶](#consulta-de-mensajes) **Consulta de mensajes**

Permite visualizar el detalle de los mensajes recibidos por un ciudadano en particular, ofreciendo una búsqueda por RUT/RUN.  Para revisar más detalles sobre este contenido puedes ingresar a la documentación de [Consulta mensajes](https://docs.google.com/document/d/1VarnWcJQzrp-zK5xFZHIzHX1Mrh-trHu8vbVt9yspaE/edit?usp=sharing).

[¶](#glosario) Glosario
-----------------------

* **Domicilio Digital Único , también podrá referenciarse como “DDU:** El Domicilio Digital Único (DDU) es un medio electrónico que designas para recibir notificaciones electrónicas de parte del Estado. En este domicilio recibirás las comunicaciones oficiales de las instituciones de manera centralizada.
* **Expediente electrónico:** Es un expediente con registro electrónico del conjunto de documentos, datos, vínculos y metadatos estandarizados, que corresponden al registro de actuaciones y resoluciones asociadas a un procedimiento administrativo, en el contexto de este manual, su identificación está asociada a un ID compuesto por un código alfanumérico.
* **Firma:** En el contexto de este manual, corresponde a un texto que identifica a la institución que envía un mensaje, y que se incluye como pie de firma. Esta firma debe ser configurada por administradores de cada institución.
* **Instituciones:** Corresponde a los Órganos de la Administración del Estado., como son ministerios, secretarías, servicios, gobernaciones, municipalidades, etc.
* **Logo:** En el contexto de este manual, corresponde a una imagen que identifica a la institución que envía un mensaje, y que se incluye en el encabezado del mensaje. Este logo debe ser configurado por administradores de cada institución.
* **Mensaje:** Para efectos de la Plataforma de Notificaciones son las comunicaciones que puede recibir el usuario desde un órgano de la Administración del Estado, sean estas comunicaciones institucionales, comunicaciones personales, a notificaciones de actos administrativos de carácter resolutivo.
* **Notificación:** Comunicación formal a un destinatario de una resolución administrativa.
* **Notificación electrónica:** en el contexto de este manual, se refiere a notificación, y comunicado personal.
* **OAE:** Órganos de la Administración del Estado.
* **Persona Jurídica:** Persona Jurídica que se conecta al notificador para consultar mensajes y notificaciones oficiales que le llegan desde instituciones del Estado de Chile, Ministerios, Municipalidades o cualquier otro organismo del estado.
* **Persona Natural:** Persona Natural que se conecta al notificador para configurar DDU, consultar mensajes y notificaciones oficiales que le llegan desde instituciones del estado de Chile, Ministerios, Municipalidades o cualquier otro organismo del estado.
* **Plataforma de notificaciones:** La Plataforma de Notificaciones Electrónicas es el canal oficial a través del cual los Órganos de la Administración del Estado (OAE) enviarán notificaciones electrónicas al Domicilio Digital Único (DDU) de las personas.
* **Procedimiento administrativo:** El procedimiento administrativo es una sucesión de actos trámites vinculados entre sí, emanados de la Administración y, en su caso, de particulares interesados, que tiene por finalidad producir un acto administrativo terminal.
* **Usuario Persona:** Son las personas naturales, jurídicas, entes y agrupaciones sin personalidad jurídica que actúan como interesados, apoderados, funcionarios o asesores a honorarios que acceden a procedimientos administrativos y los correspondientes expedientes electrónicos en las plataformas electrónicas que les dan soporte.
* **Usuario Institucional:** Son todos los funcionarios pertenecientes a algún OAE que interactúan con la plataforma de notificaciones y que tendrán un rol funcional de acuerdo a la descripción de roles y perfiles presentes en este documento.