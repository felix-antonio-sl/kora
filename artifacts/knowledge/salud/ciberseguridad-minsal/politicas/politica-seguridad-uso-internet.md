---
_manifest:
  urn: urn:salud:kb:politica-seguridad-uso-internet
  provenance:
    created_by: Codex via koraficacion
    created_at: '2026-06-05'
    source: MINSAL Chile, SGSI Nivel Central. PS-NC-012 v02, Julio 2020
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- politica
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:politica-seguridad-uso-internet
  salud:
    minsal_id: PS-NC-012
    minsal_version: '02'
relations:
  cites:
  - urn:salud:kb:politica-general-seguridad-informacion-ciberseguridad
---

# Politica de Seguridad en el Uso de Internet

**PS-NC-012 v02, Julio 2020.**

## Proposito y alcance

Define restricciones de acceso a Internet para usuarios de MINSAL y Areas dependientes, evitando navegacion a sitios riesgosos para estaciones de trabajo y red de datos.

Alcance:

- Aplica a todos los recursos computacionales con acceso a Internet donde se implemente esta politica.
- Cubre toda informacion electronica en servidores centrales, estaciones de trabajo y equipos comunicacionales con datos, configuraciones, aplicativos y servicios criticos.
- Aplica a todos los funcionarios (planta, contrata, reemplazos, suplencia), personal a honorarios y terceros (proveedores, servicios).

Dominios ISO 27001:2013 cubiertos: A.08.01.03 (Uso aceptable de activos) y A.08.02.03 (Manejo de activos).

## Marco normativo y documentos relacionados

- NCh-ISO27001:2013 — Requisitos SGSI.
- Marco Juridico SSI publicado en portal CSIRT del Ministerio del Interior.
- Decretos Supremos y Normas Internacionales de Seguridad de la Informacion y Ciberseguridad.
- Leyes relacionadas.
- Documentos SGSI disponibles en isalud.minsal.cl.

## Roles y responsabilidades

| Rol | Responsabilidades |
|---|---|
| Encargado de Seguridad de la Informacion / Ciberseguridad | Revisar categorias de navegacion y excepciones. Auditar integridad de categorias de permiso. Controlar navegacion. Informar al Comite de Seguridad situaciones anomalas. Enviar avisos por violacion a normas, politicas, procedimientos y estandares. |
| Departamento TIC | Implementar filtros y reglas definidas en esta politica. |
| Usuarios | Cumplir lo establecido en esta politica. |

## Directrices generales

- Permisos de uso de Internet limitados por necesidad funcional de cada usuario.
- Servicio de Internet disponible para todos los usuarios segun perfil asignado.
- Asignacion de perfiles por IP de equipo, realizada por Departamento TIC.

## Uso aceptable de Internet

| Regla | Detalle |
|---|---|
| Conexion institucional como primera opcion | Usar medios dispuestos por la Institucion. |
| Conexion alternativa | Ante falla de la principal, se permite acceso via proveedores externos con firewall institucional, antivirus actualizado, firewall de equipo, antimalware y parches de seguridad. |
| Uso ocasional personal | Permitido si no interfiere con funciones ni causa conflictos con actividad institucional. |
| Redes sociales | Permitidas solo si la funcion del usuario lo requiere. |
| Portales cautivos para visitas | Redes inalambricas deben contar con portales cautivos para visitas que necesiten conexion, aislando la red de trabajo institucional. |
| Contrasenas en navegadores | No almacenar. |

## Restricciones en el uso de Internet

Prohibiciones absolutas:

| Categoria | Detalle |
|---|---|
| Descarga de material ilegal | Material que infrinja Ordenamiento Juridico Nacional, Reglamento Interno, Codigo de Etica o normativa institucional. |
| Redes sociales y entretenimiento sin autorizacion | Streaming, chats, foros, blogs y sitios de entretenimiento requieren autorizacion formal de Jefatura, Jefe TIC y Encargado de Seguridad. |
| Pornografia | Ingreso a paginas con contenido pornografico no permitido. |
| Uso comercial o politico | Conexion Minsal no puede usarse para propostios comerciales o politicos. |
| Infraccion a propiedad intelectual | No transgredir copyright, secreto comercial, patentes u otras regulaciones. No instalar ni distribuir software sin licencia apropiada. |
| Interferencia o denegacion de servicios | Prohibido interferir o denegar servicios informaticos mediante programas, scripts, comandos u otros metodos, interna o externamente. |
| Sitios de hacking e inseguros | Sin permiso, no acceder a sitios de hacking o inseguros que pongan en riesgo integridad y confidencialidad. |
| Publicacion no autorizada | No publicar informacion Minsal en sitios personales sin autorizacion del propietario de la informacion. |

Obligaciones de abstencion del usuario:

| Prohibicion | Alcance |
|---|---|
| Causar dano grave e inminente | A la calidad o estabilidad del servicio informatico o de redes. |
| Transgredir derechos de propiedad intelectual | Copyright, secreto comercial, patentes, instalacion o distribucion de software sin licencia institucional. |
| Exportar software ilegalmente | Software, informacion tecnica, tecnologia o encriptacion que viole legislacion nacional o internacional de control de exportaciones. |
| Actividades ilicitas | Utilizacion de activos computacionales para actividades ilicitas. |
| Programas maliciosos | Introducir troyanos, virus, malware u otros a la red o servidores. |
| Ofertas fraudulentas | Productos o servicios fraudulentos usando activos institucionales. |
| Infracciones de seguridad e interrupcion de servicios | Acceso no autorizado a informacion, conexion a servidores o cuentas sin autorizacion. Inspeccion de trafico, ping flood, falsificacion de paquetes, denegacion de servicios, falsificacion de ruteo con fines maliciosos. |
| Escaneo o monitoreo no autorizado | Escaneo o monitoreo de redes o seguridad sin notificacion de unidad de seguridad o fuera de actividad laboral. |
| Eludir autenticacion | Bypass de autenticacion de usuario o seguridad de cualquier dispositivo, red o cuenta. |
| Proveer informacion institucional a externos | Sin autorizacion formal. |
| Contenido ilegal | Hechos delictivos, terrorismo, pirateria, infraccion a derecho de autor, pornografia infantil, estafas y otros. |

## Monitoreo

Toda informacion entrante o saliente a Internet sera monitoreada y registrada. Puede ser revisada y auditada sin previo aviso si las autoridades lo consideran necesario.

## Filtro de contenido — niveles y asignacion

Se establecen grupos de acceso segun perfiles de usuario, basados en categorias estandar de industria (referencia: filtros WSA de CISCO). Tres niveles de acceso:

1. Acceso Completo (Filtro Etico)
2. Acceso General
3. Acceso Restringido

El Filtro Etico es la asignacion minima: nadie en la organizacion tendra acceso a las paginas bloqueadas en este filtro. La asignacion de usuarios a cada nivel es responsabilidad del Encargado de Seguridad de la Informacion.

## Filtro de Acceso Completo

Solo restringido por Filtro Etico de la Red de Conectividad del Estado. Sin otras restricciones.

| Categoria WSA | Descripcion | Bloqueo |
|---|---|---|
| Adult | Contenido para Adultos | X |
| Child Abuse Content | Contenido de Abuso Infantil | X |
| Dating | Sitio de Citas | X |
| Extreme | Contenido Extremo | X |
| Filter Avoidance | Sorteo de medidas de seguridad via proxy | X |
| Freeware and Shareware | Descarga ilegal de software | X |
| Gambling | Casinos y apuestas en linea | X |
| Games | Juegos en linea | X |
| Hacking | Contenido de Hacking | X |
| Illegal Activities | Actividades Ilegales | X |
| Illegal Downloads | Descargas Ilegales | X |
| Illegal Drugs | Drogas Ilegales | X |
| Parked Domains | Dominios web con problemas | X |
| Pornography | Pornografia | X |
| Weapons | Armas | X |

## Filtro de Acceso General

Restricciones del Filtro Etico mas categorias adicionales.

| Categoria WSA | Descripcion | Bloqueo |
|---|---|---|
| Adult | Contenido para Adultos | X |
| Child Abuse Content | Contenido de Abuso Infantil | X |
| Dating | Sitio de Citas | X |
| Extreme | Contenido Extremo | X |
| Filter Avoidance | Sorteo de seguridad via proxy | X |
| Freeware and Shareware | Descarga ilegal de software | X |
| Gambling | Casinos y apuestas en linea | X |
| Games | Juegos en linea | X |
| Hacking | Contenido de Hacking | X |
| Illegal Activities | Actividades Ilegales | X |
| Illegal Downloads | Descargas Ilegales | X |
| Illegal Drugs | Drogas Ilegales | X |
| Parked Domains | Dominios web con problemas | X |
| Pornography | Pornografia | X |
| Weapons | Armas | X |
| Advertisements | Anuncios Comerciales | X |
| Alcohol | Bebidas alcoholicas | X |
| Astrology | Astrologia, Horoscopo, Tarot | X |
| Dynamic and Residential | Redes domesticas residenciales | X |
| Entertainment | Entretenimiento (peliculas, videos, musicales, fans) | X |
| Internet Telephony | Telefonia por internet | X |
| Lingerie and Swimsuits | Lenceria y trajes de bano | X |
| Non-sexual Nudity | Desnudos no sexuales | X |
| Peer File Transfer | Transferencia de archivos | X |
| SaaS and B2B | Reuniones y ventas en linea | X |
| Safe for Kids | Educacion y animacion infantil | X |
| Sex Education | Educacion sexual, embarazos | X |
| Software Updates | Parches informaticos | X |
| Web Hosting | Entrega de informacion de sitios web | X |
| Uncategorized | No categorizados (de 78 grupos) | X |

## Filtro de Acceso Restringido

Restricciones del Filtro General mas categorias adicionales.

Ademas de todas las del Filtro General, agrega:

| Categoria WSA | Descripcion | Bloqueo |
|---|---|---|
| Chat and Instant Messaging | Chat y mensajeria instantanea | X |
| Online Communities | Grupos de interes y sociedades | X |
| Online Storage and Backup | Almacenamiento en la nube | X |
| Social Networking | Redes sociales | X |
| Streaming Audio | Transmision de audio en vivo | X |
| Streaming Video | Transmision de video en vivo (TV, Youtube) | X |

## Acceso a sitios web sin restricciones

Categorias no sujetas a restriccion en ningun nivel:

| Categoria WSA | Descripcion |
|---|---|
| Real Estate | Arriendos, ventas, remates de propiedades |
| Sports and Recreation | Deportes, reglas, normas, estadisticas |
| Digital Postcards | Tarjetas y saludos digitales |
| Arts | Arte, museos, galerias |
| Auctions | Subastas en linea |
| Business and Industry | Marketing, Comercio, Negocios |
| Cheating and Plagiarism | Trabajos escritos, plagio |
| Computer Security | Seguridad tecnologica |
| Computers and Internet | Informacion tecnica (Software y Hardware) |
| Dining and Drinking | Restaurantes y bares |
| Education | Educacion |
| Fashion | Confeccion y moda |
| File Transfer Services | Transmision de datos |
| Finance | Informacion Financiera |
| Government and Law | Informacion legal |
| Hate Speech | Discursos mal intencionados |
| Health and Nutrition | Nutricion y Salud |
| Humor | Humor |
| Infrastructure and Content Deliv. Net. | Infraestructura y Redes |
| Job Search | Trabajos |
| Lotteries | Juegos de azar |
| Mobile Phones | Telefonia celular |
| Nature | Naturaleza |
| News | Noticias |
| Non-governmental Organizations | ONGs |
| Online Trading | Venta en linea (ebay) |
| Organizational Email | Correo organizacional |
| Personal Sites | Sitios personales |
| Photo Search and Images | Fotografia e imagenes |
| Politics | Politica |
| Professional Networking | Profesionales de Redes |
| Reference | Referencias |
| Religion | Religion |
| Science and Technology | Ciencia y Tecnologia |
| Search Engines and Portals | Motores de busqueda y portales |
| Shopping | Compras |
| Social Science | Ciencias sociales |
| Society and Culture | Sociedades y cultura |
| Tobacco | Tabaco |
| Transportation | Transporte |
| Travel | Viajes |
| Web Page Translation | Traduccion web |
| Web-based Email | Correo basado en web |

## Incidentes de seguridad

Usuarios que identifiquen, perciban o sospechen de algun problema de seguridad deben contactar inmediatamente al Encargado de Seguridad de Sistemas de Informacion de la Institucion.

## Mecanismo de difusion

Contenido accesible y comprensible para todos los usuarios. Canales minimos:

- Publicacion en intranet Minsal: http://isalud.minsal.cl/
- Correo informativo.

## Periodo de revision y excepciones

- Revision cada dos anos por el Comite de Seguridad de la Informacion, o ante necesidades de cambios.
- Casos especiales: el Comite evalua y puede establecer condiciones puntuales de excepcion que no infrinjan legislacion vigente. Toda excepcion debe documentarse y generar proceso de revision.

## Historial de versiones

| Version | Fecha | Cambios |
|---|---|---|
| 01 | Agosto 2013 | Creacion del documento |
| 02 | Julio 2020 | Actualizacion del documento |
