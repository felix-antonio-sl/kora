---
_manifest:
  urn: urn:salud:kb:arquitectura-referencia-desarrollo-sistemas-sector-salud
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-04'
    source: MINSAL Chile, Depto. TIC, Unidad de Arquitectura, Desarrollo y Calidad.
      AR-NC-001 v1.0 (Mayo 2025). Incluye Documento Tecnico Arquitectura de Referencia
      v1.0
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- arquitectura-software
- desarrollo-sistemas
- interoperabilidad
- microservicios
- fhir
- cloud
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 2
    shard_root_urn: urn:salud:kb:arquitectura-referencia-desarrollo-sistemas-sector-salud
  salud:
    minsal_id: AR-NC-001
    minsal_version: '1.0'
    fecha_aprobacion: Mayo 2025
    clasificacion: Publica
    autores: Rodrigo Baeza G. (Unidad de Arquitectura, Desarrollo y Calidad)
    revisor_seguridad: Jose Villa C.
    revisor_tecnico: Catalina Arenas A.
    aprobador: Jorge Herrera R., Jefe Depto. TIC
relations:
  cites:
  - urn:salud:kb:instructivo-seguridad-informacion-ciberseguridad-sector-salud
  - urn:salud:kb:stack-tecnologico-seguridad-minsal
  - urn:salud:kb:clausulas-seguridad-contratos-ti-sector-salud
---

# Documento Tecnico: Arquitectura de Referencia para Sector Salud


Version 1.0, 2025

## Objetivos

### Objetivo general

Ofrecer una guia integral para planificacion, diseno y despliegue de infraestructura tecnologica moderna, eficiente y segura. Establece pilares solidos para la construccion de software a medida. Optimiza la gestion interna, fortalece la colaboracion interinstitucional y mejora la comprension de los equipos de desarrollo mediante implementacion de estandares de seguridad y escalabilidad.

### Objetivos especificos

1. Definir una arquitectura modular y escalable que permita la adaptacion agil a las cambiantes necesidades tecnologicas.
2. Establecer lineamientos precisos para implementacion de estandares abiertos y protocolos de interoperabilidad, facilitando la integracion de sistemas internos y colaboracion con otras instituciones gubernamentales.
3. Disenar mecanismos de seguridad robustos que salvaguarden la integridad y confidencialidad de los datos (segmentacion de red, encriptacion de comunicaciones, sistemas avanzados de deteccion y respuesta ante amenazas ciberneticas).
4. Definir interfaces de usuario intuitivas y modernas que mejoren la experiencia de los ciudadanos.
5. Proporcionar pautas detalladas para implementacion de soluciones tecnologicas que respalden la toma de decisiones basada en datos.
6. Establecer criterios de sostenibilidad y mantenimiento a largo plazo, garantizando la continuidad operativa.
7. Fomentar la cultura de innovacion tecnologica y capacitacion continua del personal.
8. Evaluar periodicamente la implementacion de la arquitectura de referencia y realizar ajustes necesarios para garantizar alineacion con objetivos estrategicos y avances tecnologicos.
9. Facilitar la generacion de informes y metricas para medir el impacto de la implementacion en terminos de eficiencia, seguridad y satisfaccion ciudadana.

## Destinatarios

- **Profesionales TIC**: Arquitectos, ingenieros, desarrolladores, administradores de sistemas. Orientacion detallada sobre como disenar, implementar y gestionar soluciones en linea con las mejores practicas y estandares.
- **Equipos de Seguridad de la Informacion y Ciberseguridad**: Directrices y enfoques detallados para garantizar la proteccion de datos y sistemas contra amenazas ciberneticas.
- **Personal de Gestion de Proyectos**: Informacion util para planificar y ejecutar proyectos TIC de manera efectiva, asegurando alineacion con los objetivos estrategicos.
- **Instituciones del Sector Salud**: Servicios de Salud, Establecimientos, Seremis, Organismos Autonomos y otras instituciones gubernamentales. Comprender como la arquitectura de referencia promueve la interoperabilidad y la cooperacion efectiva.

## Arquitectura de referencia: componentes clave

| Componente | Descripcion |
|---|---|
| Infraestructura Tecnologica | Servidores, redes y sistemas de almacenamiento distribuidos. Virtualizacion y nube para escalabilidad y disponibilidad. |
| Plataforma de Servicios | Servicios compartidos: autenticacion, autorizacion, gestion de identidades y servicios de mensajeria. Estandares abiertos. |
| Integracion de Datos | Mecanismos de integracion para consolidacion e intercambio de informacion entre sistemas internos y externos. Protocolos API REST y SOAP. |
| Seguridad y Privacidad | Modelo de seguridad por diseno. Cifrado robusto en transito y reposo, MFA, RBAC, monitoreo continuo con SIEM, EDR/XDR, gestion activa de vulnerabilidades, cumplimiento normativo (Ley 19.628, Ley 21.663), planes de continuidad operativa, respaldos cifrados, respuesta ante incidentes. |
| Analitica de Datos | Herramientas de analisis de datos para toma de decisiones informadas. Tecnicas de analisis de big data y visualizacion. |
| Gestion de Procesos | Capa de gestion de procesos para automatizar flujos de trabajo internos y la interaccion con ciudadanos. |
| Interoperabilidad y Colaboracion | Interfaces y protocolos estandarizados para colaboracion con otras instituciones gubernamentales, facilitando el intercambio seguro de datos. |
| Escalabilidad y Resiliencia | Escalabilidad horizontal, estrategias de respaldo y recuperacion para continuidad de servicios. |
| Mantenimiento y Actualizacion | Procesos y procedimientos para mantenimiento continuo, asegurando soluciones actualizadas y seguras. |

## Arquitectura de referencia: abstraccion empresarial

El siguiente diagrama describe la arquitectura de referencia desde un punto de vista empresarial:

```text
 CIUDADANIA GOBIERNO PRIVADO
 | | |
 +---------+------------+-----------+---------+
 | CANALES DE COMUNICACION |
 | BOTS | CHAT | MENSAJERIA | CORREO |
 | PORTALES | APPS |
 +-------------------+------------------------+
 |
 +-------------------+------------------------+
 | PROCESOS DE NEGOCIO |
 +-------------------+------------------------+
 |
 +-----------------------------+------------------------------+
 | MICROSERVICIOS / WEB SERVICES |
 +-----------------------------+------------------------------+
 | INTEGRACION DE SISTEMAS (ESB) |
 +-----------------------------+------------------------------+
 | BASES DE DATOS |
 +-----------------------------+------------------------------+
 | IaaS | PaaS | SaaS (CLOUD) |
 +------------------------------------------------------------+
```

La arquitectura de referencia empresarial esta compuesta por 9 zonas:

## Zona 1: Gestion y gobierno de arquitectura empresarial

| Sub-componente | Descripcion |
|---|---|
| Gobernanza de Arquitectura | Principios, politicas y procesos para supervisar y gestionar la evolucion de la arquitectura. Asegura que todas las decisiones de diseno sean coherentes con los objetivos estrategicos y directrices organizacionales. |
| Planificacion Estrategica | Metas a largo plazo de la organizacion y como la arquitectura tecnologica apoya y potencia estos objetivos. Identificacion de oportunidades y desafios tecnologicos clave. |
| Gestion de Cambios | Procedimientos para administrar cambios y actualizaciones en la arquitectura de manera controlada y con minimo impacto en la operacion actual. Evita interrupciones innecesarias y garantiza continuidad del servicio. |
| Control de Calidad | Mecanismos para evaluar la calidad y eficacia de la arquitectura implementada: revisiones periodicas, evaluaciones de riesgos, aseguramiento de conformidad con estandares y regulaciones. |
| Colaboracion y Comunicacion | Canales de comunicacion efectivos entre equipos de arquitectura, lideres y stakeholders clave. Fomenta la colaboracion y el intercambio de conocimiento. |
| Gestion de Recursos | Determinacion de recursos necesarios (personal especializado, herramientas de software, presupuesto) para implementar y mantener la arquitectura. |

## Zona 2: Modelo de seguridad y privacidad de la informacion

| Sub-componente | Descripcion |
|---|---|
| Seguridad en Capas | Controles tecnicos y administrativos desde la capa de red hasta la aplicacion: firewalls de proxima generacion (NGFW), WAF, segmentacion de redes, monitoreo continuo mediante SIEM, sistemas de deteccion y respuesta (EDR/XDR). |
| Gestion de Identidad y Acceso | Autenticacion y autorizacion de usuarios y sistemas. Autenticacion multifactor (MFA), control de accesos basado en roles (RBAC), principios de minimo privilegio, politicas de acceso dinamico. |
| Control de Acceso Granular | Politicas y tecnologias para controlar el acceso a datos y sistemas, asignando niveles de privilegio especificos segun roles y responsabilidades de los usuarios. |
| Cifrado de Datos | Cifrado robusto de datos en reposo y en transito mediante algoritmos criptograficos fuertes (AES-256, TLS 1.2 o superior). Adecuada gestion de claves y certificados. |
| Gestion de Amenazas y Vulnerabilidades | Sistemas de deteccion y prevencion de intrusiones para identificar actividades maliciosas o anomalas en tiempo real. Medidas proactivas para mitigar riesgos potenciales. |
| Gestion Integral de Actualizaciones | Diseno de servicios y plataformas para facilitar la recepcion e implementacion oportuna de actualizaciones y parches de seguridad. Proteccion continua contra vulnerabilidades conocidas y emergentes. |
| Continuidad Operacional y Recuperacion ante Incidentes | Integracion de estrategias de continuidad del negocio y planes de recuperacion ante desastres ciberneticos. Respaldos cifrados, planes de respuesta a incidentes, simulacros periodicos. |
| Cumplimiento Normativo | Aseguramiento de que la arquitectura cumpla con las leyes, regulaciones y estandares de seguridad y privacidad relevantes para el sector salud y las normativas gubernamentales vigentes. |
| Auditoria y Monitoreo | Registros detallados de actividades para permitir la revision y el analisis de eventos en caso de incidentes de seguridad, garantizando trazabilidad y rendicion de cuentas. |
| Gestion de Incidentes | Procedimientos claros y eficientes para respuesta, contencion, erradicacion y recuperacion ante incidentes de seguridad, minimizando el impacto y restaurando la operatividad normal. |
| Privacidad de los Datos | Politicas y practicas para proteger la privacidad de datos personales, asegurando recopilacion, almacenamiento y procesamiento conforme a las leyes de privacidad aplicables. |
| Seguridad en la Comunicacion Web | Todos los accesos a sitios web institucionales y comunicaciones cliente-servidor protegidos mediante HTTPS/TLS. Certificados digitales gestionados y actualizados conforme a las mejores practicas. Tokens de sesion unicos, seguros y de corta duracion, con mecanismos de rotacion y cifrado para prevenir secuestro de sesion. Mensajes de error genericos, sin exposicion de informacion sensible. Contrasenas almacenadas con funciones de hash seguras (bcrypt, Argon2 o scrypt), utilizando salting y stretching. |
| Seguridad por Diseno en APIs | APIs internas y externas desarrolladas bajo principios de seguridad por diseno: autenticacion robusta (OAuth 2.0), autorizacion granular, cifrado TLS 1.3, protecciones contra OWASP API Top 10. Validacion de entradas, limitacion de tasas de consumo, trazabilidad completa de los accesos, documentacion actualizada. Para exposicion de servicios API REST: autenticacion mediante tokens (JWT), certificados o llaves criptograficas. |
| Educacion y Concienciacion | Formacion continua y sensibilizacion sobre cuestiones de seguridad entre el personal, reduciendo los riesgos asociados con errores humanos. |

## Zona 3: Usuarios

| Sub-componente | Descripcion |
|---|---|
| Identificacion de Grupos de Interes | Identificar y clasificar los diferentes grupos de usuarios y stakeholders: ciudadanos, funcionarios, entidades gubernamentales colaboradoras. |
| Analisis de Requerimientos | Recopilar y analizar los requerimientos y expectativas de cada grupo de interes en terminos de funcionalidad, usabilidad y experiencia general. |
| Segmentacion de Usuarios | Segmentar usuarios en categorias basadas en roles, responsabilidades y necesidades especificas para personalizacion efectiva. |
| Diseno Centrado en el Usuario | Utilizar informacion recopilada para disenar interfaces y funcionalidades intuitivas y relevantes para cada grupo de usuarios. |
| Feedback Continuo | Establecer canales para recopilar comentarios y sugerencias de los usuarios, facilitando la mejora constante. |
| Pruebas de Usuario | Realizar pruebas de usuario para validar el diseno y la funcionalidad de los sistemas antes de su implementacion. |
| Capacitacion y Soporte | Implementar programas de capacitacion y proporcionar soporte continuo para ayudar a los usuarios a utilizar eficazmente los sistemas. |
| Medicion de la Experiencia del Usuario | Recopilar metricas para evaluar la satisfaccion y la experiencia general de los usuarios, permitiendo ajustes basados en datos. |
| Comunicacion con Stakeholders | Establecer canales de comunicacion efectivos con los stakeholders, manteniendolos informados sobre actualizaciones y mejoras. |

## Zona 4: Canales

| Sub-componente | Descripcion |
|---|---|
| Canal de Comunicacion | Canales a traves de los cuales el Ministerio interactua con ciudadanos, otros organismos gubernamentales y personal interno: sitios web, aplicaciones moviles, correos electronicos, lineas de atencion telefonica, redes sociales. |
| Multicanalidad | Integracion coherente de los diferentes canales, permitiendo a los usuarios acceder a los mismos servicios y recursos independientemente del canal. |
| Personalizacion | Adaptar la experiencia del usuario segun sus preferencias y necesidades a traves de diversos canales. |
| Accesibilidad | Garantizar que los canales sean accesibles para personas con discapacidades conforme a estandares de accesibilidad web. |
| Interaccion en Tiempo Real | Caracteristicas que permiten la interaccion en tiempo real con los usuarios, como chats en linea y respuestas automaticas. |
| Notificaciones y Alertas | Mecanismos para enviar notificaciones y alertas a los usuarios sobre actualizaciones, cambios o eventos relevantes a traves de diferentes canales. |
| Analisis de Datos de Uso | Recopilar y analizar informacion sobre como los usuarios interactuan con los diferentes canales para identificar areas de mejora. |
| Seguridad en la Comunicacion | Medidas de seguridad para proteger la informacion transmitida a traves de los canales: encriptacion de datos y autenticacion. |
| Integracion con Sistemas Internos | Conexion de los canales con los sistemas internos del Ministerio para una gestion eficiente y experiencia de usuario coherente. |
| Monitoreo y Mejora Continua | Procesos para monitorear el rendimiento de los canales y recopilar retroalimentacion de usuarios para realizar ajustes y mejoras. |

## Zona 5: Procesos de negocio

| Sub-componente | Descripcion |
|---|---|
| Identificacion de Procesos Clave | Identificar los procesos centrales y criticos para el funcionamiento del Ministerio, desde la gestion interna hasta la interaccion con ciudadanos y otras entidades. |
| Modelado de Procesos | Representacion visual de los flujos de trabajo, destacando actividades, actores involucrados y sus interacciones. |
| Optimizacion y Automatizacion | Analizar procesos existentes para identificar oportunidades de optimizacion y automatizacion, mejorando eficiencia y reduciendo errores. |
| Flujos de Trabajo Digitales | Transicion de procesos tradicionales a flujos de trabajo digitales, aprovechando herramientas y tecnologias para facilitar la colaboracion y toma de decisiones. |
| Integracion de Sistemas | Conexiones entre sistemas internos y externos necesarios para llevar a cabo los procesos de manera fluida, garantizando transferencia de datos y sincronizacion de informacion. |
| Gestion de Casos | Estructura para gestionar casos complejos que involucran multiples etapas y partes interesadas, asegurando resolucion eficiente y coherente. |
| Monitorizacion y Reportes | Seguimiento constante de los procesos para recopilar datos y generar informes que permitan evaluar el rendimiento y eficacia de las operaciones. |
| Mejora Continua | Mecanismos para recopilar retroalimentacion de los usuarios y realizar ajustes en los procesos en funcion de los resultados y necesidades cambiantes. |
| Cumplimiento Regulatorio | Asegurar que los procesos esten en conformidad con regulaciones y normativas relevantes, respetando estandares legales y eticos. |
| Capacitacion y Adopcion | Capacitacion a los usuarios para garantizar la correcta ejecucion de los procesos y promover la adopcion exitosa de nuevas formas de trabajar. |

## Zona 6: Integracion e interoperabilidad

| Sub-componente | Descripcion |
|---|---|
| Cumplimiento de Estandares HL7 | Compatibilidad con HL7 en sus versiones vigentes: HL7 v2.x y FHIR (R4 y posteriores). Asegura intercambio de datos entre sistemas de informacion de salud con consistencia y precision clinica. Interoperabilidad eficaz entre sistemas de historia clinica electronica (HCE), sistemas de apoyo clinico (RIS, LIS) y otras aplicaciones de salud. |
| Estandares de Integracion y Protocolos | Utilizar estandares ampliamente aceptados (REST, GraphQL, JSON, XML) y protocolos de comunicacion seguros (HTTPS, SFTP, TCP/IP) para transmision de datos confiable y segura. |
| Gestion de Datos Interoperables | Datos en formatos estructurados y normalizados segun directrices organizacionales y normativas vigentes, permitiendo intercambio y procesamiento sin perdida de consistencia o integridad. |
| Plataforma de Integracion | Establecer una plataforma que actue como intermediario entre los sistemas, facilitando la comunicacion y el flujo de datos de manera estandarizada. |
| Interfaces y Protocolos Estandar | Definir interfaces y protocolos de comunicacion estandarizados para intercambio de datos coherente y uniforme. |
| Orquestacion de Procesos | Capacidad de orquestar procesos complejos que involucran varios sistemas, garantizando ejecucion fluida y secuencial. |
| Transformacion de Datos | Permitir la transformacion de datos para asegurar que la informacion se ajuste a los formatos requeridos por los sistemas de destino. |
| Adaptadores y Conectores | Desarrollar adaptadores y conectores especificos para conectarse con sistemas externos, asegurando una integracion efectiva. |
| Gestion de Mensajes | Sistema de gestion de mensajes para asegurar la entrega y el enrutamiento adecuado de la informacion entre sistemas. |
| Seguridad en la Integracion | Medidas de seguridad para proteger la informacion durante la transferencia entre sistemas: encriptacion y autenticacion. |
| Monitorizacion y Trafico de Datos | Mecanismo para monitorear el trafico de datos y verificar el estado de la integracion en tiempo real. |
| Integracion de Terceros | Integracion con sistemas y servicios de terceros, como proveedores externos o agencias gubernamentales, para una colaboracion mas amplia. |
| Pruebas de Integracion | Pruebas exhaustivas de la integracion para asegurar que los sistemas interactuen de manera efectiva y sin problemas. |
| APIs Documentadas y Consistentes | Desarrollo obligatorio de APIs documentadas y consistentes que faciliten el acceso y la integracion de funcionalidades y datos entre diferentes sistemas de salud, tanto internos como de terceros. |

## Zona 7: Servicios de informacion

| Sub-componente | Descripcion |
|---|---|
| Inventario de Aplicaciones | Inventario completo de las aplicaciones utilizadas, identificando proposito, funcionalidades y relacion con los procesos de negocio. |
| Diseno de Aplicaciones | Especificaciones tecnicas y funcionales de las aplicaciones, asegurando adaptacion optima a requerimientos de usuarios y objetivos organizacionales. |
| Desarrollo de Software | Metodologias de desarrollo agil y buenas practicas para construir, mantener y mejorar las aplicaciones. |
| Integracion de Sistemas | Conexiones entre diferentes aplicaciones y sistemas para permitir el flujo de datos y la interoperabilidad, evitando duplicacion de esfuerzos. |
| Implementacion y Despliegue | Estrategia y proceso para implementar y desplegar nuevas aplicaciones y actualizaciones en entorno controlado, minimizando el impacto en la operacion. |
| Mantenimiento y Soporte | Procedimientos para el mantenimiento y soporte continuo de las aplicaciones: correccion de errores, actualizaciones de seguridad y mejoras funcionales. |
| Arquitectura de Aplicaciones | Estructura y diseno general de las aplicaciones: modularidad, escalabilidad y reutilizacion de componentes. |
| Seguridad de Aplicaciones | Medidas de seguridad a nivel de aplicaciones: autenticacion, autorizacion, pruebas de seguridad. Estandares reconocidos de desarrollo seguro (OWASP, NIST). Secure Software Development Lifecycle (SSDLC). Prevencion de ataques de inyeccion de codigo: SQL Injection, XSS, CSRF. Consultas a bases de datos mediante procedimientos almacenados y consultas preparadas. Librerias y frameworks de terceros reconocidos por su fiabilidad y mecanismos de seguridad robustos. |
| Gestion de Versiones | Proceso para gestionar las versiones de las aplicaciones, facilitando control de cambios e implementacion ordenada de nuevas funcionalidades. |
| API Strategy | Estrategia de API que permite a las aplicaciones interactuar de manera coherente y eficiente, fomentando interoperabilidad e integracion. |

## Zona 8: Datos e informacion

| Sub-componente | Descripcion |
|---|---|
| Gestion de Datos Maestros | Fuentes confiables y unicas de datos maestros (registros de ciudadanos, empleados, activos) para garantizar integridad y coherencia de la informacion. |
| Almacenamiento de Datos | Tecnologias y estrategias para el almacenamiento eficiente y seguro de los datos: bases de datos, sistemas de archivos y almacenamiento en la nube. |
| Modelado de Datos | Definir modelos de datos que representen la estructura y relaciones entre los diferentes tipos de informacion. |
| Integracion de Datos | Mecanismos para la integracion de datos entre sistemas y aplicaciones, garantizando consistencia y disponibilidad de la informacion. |
| Calidad de Datos | Practicas para asegurar la calidad de los datos: limpieza, normalizacion y validacion. |
| Acceso y Privacidad | Politicas de acceso a los datos, asegurando que solo los usuarios autorizados puedan acceder a la informacion relevante y se respete la privacidad de datos personales. |
| Gobierno de Datos | Procesos y responsabilidades para la gestion y control de datos: definicion de roles y responsabilidades de administracion de datos. |
| Analisis de Datos | Capacidad de analizar datos para extraer conocimientos y patrones que respalden la toma de decisiones informadas. |
| Visualizacion de Datos | Herramientas de visualizacion de datos para representar la informacion de manera comprensible y facil de interpretar. |
| Respaldo y Recuperacion | Estrategias de respaldo y recuperacion de datos para asegurar la continuidad operativa en caso de fallos o perdidas de informacion. |

## Zona 9: Servicios de infraestructura

| Sub-componente | Descripcion |
|---|---|
| Virtualizacion y Cloud | Tecnologias de virtualizacion y servicios en la nube para crear infraestructura flexible y escalable. |
| Servidores y Almacenamiento | Servidores y sistemas de almacenamiento que satisfagan las necesidades de procesamiento y capacidad de datos requeridas por las aplicaciones. |
| Redes y Comunicaciones | Red robusta y segura que permita la comunicacion eficiente entre sistemas y usuarios internos y externos. |
| Balanceo de Carga | Mecanismos de balanceo de carga para distribuir equitativamente la carga de trabajo entre servidores, mejorando disponibilidad y rendimiento. |
| Seguridad de la Infraestructura | Medidas de seguridad para proteger la infraestructura tecnologica: cortafuegos, deteccion de intrusiones, soluciones de seguridad en red. |
| Respaldo y Recuperacion | Estrategia de respaldo y recuperacion de la infraestructura para garantizar la continuidad de los servicios en caso de fallas o desastres. |
| Monitoreo y Gestion | Herramientas y procesos para monitorear el rendimiento de la infraestructura y abordar proactivamente problemas potenciales. |
| Escalabilidad Automatizada | Sistemas para escalar automaticamente los recursos segun las demandas cambiantes, garantizando el rendimiento en momentos de alta carga. |
| Gestion de Configuracion | Practicas de gestion de configuracion para asegurar que la infraestructura este correctamente configurada y documentada. |
| Eficiencia Energetica | Practicas de eficiencia energetica en el diseno y operacion de la infraestructura, minimizando el consumo de recursos. |

## Arquitectura de referencia: abstraccion tecnica

El siguiente diagrama muestra la arquitectura tecnica orientada a microservicios propuesta:

```text
 RED
 |
 +-----------+-----------+
 | K8s Cluster |
 | Angular Node.js |
 | React |
 +-----------+-----------+
 | (Frontend)
 |
 +-----------+-----------+
 | API Gateway (Apigee) |
 +-----------+-----------+
 |
 +--------------+--------------+
 | K8s Cluster | K8s Cluster
 | OpenHIM (HL7 Bus) | Server
 | |
 | APIs | Colas | ETLs |
 +--------------+--------------+
 | (Backend)
 +--------------+--------------+
 | K8s Cluster | K8s Cluster
 | Node.js Java .NET Core |
 | RabbitMQ Python |
 +--------------+--------------+
 |
 +--------------+--------------+
 | K8s Cluster |
 | PostgreSQL | MongoDB |
 +----------------------------+
 | (Datos)
```

La arquitectura orientada a microservicios cuenta con:

- **Capa frontend**: Desarrollo en cluster (K8s), recomendacion de dockerizacion, posibilidad de maquinas virtuales. Tecnologias: Angular, Node.js, React.
- **API Gateway (Apigee)**: Gobernanza de APIs e interoperabilidad de todos los sistemas con los servicios, y del front con el back.
- **Capa backend**: Segun el sistema, herramientas como OpenHIM (bus de integracion HL7). Incluye APIs, colas, ETLs. Tecnologias: Node.js, Java, .NET Core, RabbitMQ, Python.
- **Capa de datos**: MongoDB para bases de datos no relacionales; PostgreSQL para bases de datos relacionales.

## Enfoque monolitico

| Caracteristica | Descripcion |
|---|---|
| Simplicidad Inicial | Desarrollos mas simples en arquitectura y estructura, facilitan implementacion inicial. |
| Despliegue Unificado | Todo en un solo componente; despliegue y actualizacion como una unidad. |
| Comunicacion Interna Facil | Debido a la estrecha integracion, comunicaciones internas entre componentes son mas directas. |
| Escalabilidad Limitada | Dificil escalar solo una parte del sistema sin afectar el sistema en su conjunto. |
| Acoplamiento Fuerte | Cambios en una parte pueden afectar otras partes debido al acoplamiento estrecho. |
| Dificultad en Mantenimiento | A medida que el sistema crece, puede volverse complicado de mantener y evolucionar. |

**Recomendado en escenarios**: Aplicaciones pequenas y simples; equipos con recursos limitados; prototipos y MVPs; aplicaciones con pocos cambios futuros; tiempo de lanzamiento rapido; aplicaciones internas; proyectos de aprendizaje.

## Enfoque de microservicios

| Caracteristica | Descripcion |
|---|---|
| Desacoplamiento | Microservicios independientes entre si; cambios y actualizaciones sin afectar otros componentes. |
| Escalabilidad Granular | Escalar solo los microservicios que requieren mas recursos. |
| Flexibilidad Tecnologica | Diferentes microservicios pueden estar desarrollados con diferentes tecnologias segun su mejor adecuacion. |
| Facilita la Innovacion | Mas facil experimentar con nuevas tecnologias o enfoques en componentes especificos. |
| Complejidad de Gestion | Coordinar multiples microservicios puede ser complicado en despliegue, monitoreo y gestion. |
| Comunicacion Distribuida | La comunicacion entre microservicios a traves de la red puede aumentar la latencia. |
| Mayor Inversion Inicial | El desarrollo inicial puede requerir mas esfuerzo por la necesidad de disenar, implementar y gestionar varios microservicios. |

**Recomendado en escenarios**: Donde la flexibilidad, escalabilidad y modularidad son esenciales para el exito de la aplicacion.
