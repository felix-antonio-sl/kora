---
_manifest:
  urn: urn:salud:kb:arquitectura-referencia-desarrollo-sistemas-sector-salud-p02
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
    shard_index: 2
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

# Documento Tecnico: Arquitectura de Referencia para Sector Salud - Parte 02

## Stack tecnologico

#### Lenguajes de programacion

| Lenguaje | Directriz |
|---|---|
| Java | Usar versiones con soporte a largo plazo (LTS) y actualizaciones de seguridad activas. |
| Python | Usar versiones LTS con actualizaciones de seguridad activas. |
| PHP | Usar versiones LTS con actualizaciones de seguridad activas. |

Las versiones recomendadas se encuentran en el documento de Stack Tecnologico.

#### Frameworks

| Lenguaje | Framework | Version |
|---|---|---|
| Java | SpringBoot | Ultima version |
| Python | Django | Ultima version |
| Python | Flask | Ultima version |
| PHP | Laravel | Ultima version |
| PHP | CodeIgniter | Ultima version |

Crucial considerar versiones con actualizaciones de seguridad activas y ciclo de vida de soporte adecuado.

#### Bases de datos

| Tipo | Motor | Version minima |
|---|---|---|
| Relacional | PostgreSQL | 9+ |
| Relacional | MySQL | 5.7+ |
| Relacional | Oracle | Ultima version |
| No relacional | MongoDB | 4+ |
| No relacional | Redis | 5+ |
| No relacional | Elasticsearch | 5.5+ |

#### Librerias

| Categoria | Libreria | Version |
|---|---|---|
| Bibliotecas graficas | Bootstrap | 5.x+ |
| Scripts | ReactJS | 18.x+ |
| Scripts | jQuery | 3.x+ |

Criterio de seleccion: frecuencia de actualizaciones de seguridad y nivel de soporte de la comunidad. Librerias bien mantenidas son menos propensas a tener vulnerabilidades sin parchar.

#### Plataformas en la nube

Plataformas como AWS, Azure, GCP ofrecen servicios y recursos para hospedar, desplegar y escalar aplicaciones. La definicion de herramientas sobre ambientes cloud debe evaluarse particularmente para cada solucion.

**Principio**: El Ministerio prefiere desarrollos agnosticos a la marca; no recomienda el uso de tecnologias nativas de cada nube.

**Seguridad desde el diseno en cloud**:
- Gestion de identidades y accesos (IAM) robusta con principio de minimo privilegio.
- Configuracion segura de recursos cloud (instancias, almacenamiento, bases de datos, redes).
- Cifrado en transito y en reposo para proteger la confidencialidad de los datos.
- Segmentacion de red y firewalls virtuales para controlar el trafico.
- Monitorizacion y registro centralizado de eventos de seguridad para deteccion temprana de incidentes.
- Mecanismos de respuesta a incidentes especificos para la nube.

Las herramientas de seguridad seleccionadas deben, en lo posible, ser servicios nativos de la nube configurables de manera segura o herramientas de terceros interoperables, evitando dependencia de tecnologias propietarias que dificulten la portabilidad entre proveedores cloud.

#### Herramientas de desarrollo y gestion

Existe una lista de herramientas actuales en el Stack Tecnologico del Ministerio: herramientas para encolamiento, servidores de aplicaciones, registro de eventos, servidores web, entre otros. Consultar la Guia de Implementacion de SW para el listado completo.

## Marcos de trabajo y lineamientos para diseno de arquitectura de soluciones

Conjunto estructurado de enfoques, principios y directrices que guian el proceso de diseno y construccion de soluciones tecnologicas.

## Principios arquitectonicos

| # | Principio | Descripcion |
|---|---|---|
| 1 | Modularidad | Division del sistema en modulos independientes y autonomos. Cada modulo se encarga de una funcionalidad especifica y puede ser desarrollado, probado y mantenido de manera independiente. Facilita escalabilidad, mantenimiento y reutilizacion de componentes. |
| 2 | Reutilizacion | Creacion de componentes y servicios que puedan ser utilizados en multiples partes del sistema o en diferentes proyectos. Reduce duplicacion de esfuerzos, acelera el desarrollo y mejora consistencia y calidad del codigo. |
| 3 | Separacion de Responsabilidades | Asignacion clara de tareas y responsabilidades a diferentes componentes del sistema. Cada componente realiza una funcion especifica sin conocimiento profundo de las operaciones de otros. Mejora mantenibilidad y facilita cambios y actualizaciones. |
| 4 | Escalabilidad | Arquitectura capaz de crecer en respuesta a la demanda sin comprometer el rendimiento. Escalabilidad horizontal (agregando mas instancias del mismo componente) o vertical (mejorando los recursos de un componente existente). |
| 5 | Desacoplamiento | Los componentes del sistema deben tener la menor dependencia posible entre si. Permite cambios en uno sin afectar a otros. Mejora flexibilidad y facilita la evolucion y colaboracion entre equipos de desarrollo. |
| 6 | Abstraccion | Creacion de interfaces que oculten los detalles internos y presenten solo la funcionalidad esencial. Permite cambios internos sin afectar a los usuarios o a otros componentes. |
| 7 | Coherencia y Consistencia | Mantener una estructura coherente y una logica consistente en todo el sistema. Facilita la comprension y reduce la complejidad. |
| 8 | Flexibilidad | Arquitectura flexible para adaptarse a cambios en los requisitos y tecnologias. Se logra mediante el uso de patrones de diseno que permiten cambios graduales y extensiones sin rehacer toda la estructura. |
| 9 | Eficiencia | Los principios arquitectonicos deben contribuir a la eficiencia del sistema en terminos de recursos de hardware, rendimiento y consumo energetico. |
| 10 | Seguridad | La seguridad debe ser un principio fundamental, asegurando que los sistemas y las comunicaciones esten protegidos contra amenazas y vulnerabilidades. |

## Patrones de diseno

Soluciones probadas y documentadas para problemas recurrentes en el diseno de software y sistemas. Ofrecen un lenguaje comun y una guia efectiva. Se debera ajustar el uso de patrones a la solucion requerida, manteniendo la simpleza y la estandarizacion como premisa. El uso de cada tipo de patron debera ser justificado en cada caso.

## Metodologias de desarrollo

Enfoques sistematicos y estructurados para planificar, disenar, construir, probar y entregar software y sistemas. La recomendacion es ajustar la metodologia a la naturaleza de lo que se busca solucionar.

## Lineamientos de seguridad

Los lineamientos de seguridad establecen una base solida de ciberseguridad para la proteccion de activos y datos, mitigacion de riesgos y mantenimiento de la integridad, confidencialidad y disponibilidad de la informacion.

**Principio fundamental**: Modelo de Seguridad por Capas fundamentado en el principio de **seguridad y privacidad por defecto y desde el diseno**, establecido en la Ley 21.663 (Marco de Ciberseguridad). Todos los sistemas informaticos, aplicaciones y tecnologias de la informacion deben concebirse, implementarse y gestionarse tomando como base la seguridad y la privacidad de los datos personales que procesan desde su inicio.

#### Proteccion de Datos

| Dimensión | Descripcion | Implementacion |
|---|---|---|
| Confidencialidad | Informacion solo disponible para personas autorizadas. | Controles de acceso RBAC y ABAC. Cifrado robusto (AES-256 o superior) en reposo y en transito (TLS 1.2 o superior). Minimizacion de datos y anonimizacion/seudonimizacion. |
| Integridad | Datos no alterados por personas no autorizadas; cambios registrados y rastreados. | Mecanismos de control de versiones, sumas de verificacion (checksums), firmas digitales. Registros de auditoria (logs) detallados e inmutables. Validaciones de entrada y controles de integridad referencial a nivel de base de datos y aplicacion. |
| Disponibilidad | Datos y sistemas disponibles cuando sean necesarios. | Arquitecturas resilientes y tolerantes a fallos: redundancia de componentes, balanceo de carga, mecanismos de conmutacion por error (failover). Estrategias de backup y restauracion periodicas y probadas. Planes de continuidad del negocio (BCP) y recuperacion ante desastres (DRP). |

#### Control de Acceso

| Componente | Descripcion | Implementacion |
|---|---|---|
| Autenticacion | Verificar identidad de usuarios antes de otorgar acceso. | Mecanismos robustos: autenticacion multifactor (MFA), contrasenas complejas y politicas de rotacion, autenticacion basada en certificados o biometria. Protocolos seguros: OAuth 2.0, SAML 2.0. |
| Autorizacion | Definir que recursos y datos pueden acceder los usuarios autorizados. | Implementacion de listas de control de acceso (ACLs), RBAC y ABAC, aplicadas consistentemente en capa de aplicacion e infraestructura. |
| Auditoria | Registrar actividades de usuarios y eventos del sistema para revision posterior. | Herramientas de gestion de logs (SIEM) para analisis, correlacion y alerta de eventos sospechosos. |

#### Gestion de Riesgos

| Componente | Descripcion | Implementacion |
|---|---|---|
| Evaluacion de Riesgos | Identificar y evaluar amenazas y vulnerabilidades para determinar riesgos potenciales. | Pruebas de penetracion (pentesting) periodicas, analisis de vulnerabilidades automatizados, revisiones de seguridad del codigo fuente (SAST/DAST). |
| Mitigacion de Riesgos | Implementar medidas de seguridad para reducir los riesgos a un nivel aceptable. | Sistemas de prevencion de intrusiones (IPS), firewalls de ultima generacion (NGFW), herramientas de deteccion y respuesta de endpoints (EDR), aplicacion de parches de seguridad de manera oportuna. |

#### Seguridad en la Infraestructura

| Componente | Implementacion |
|---|---|
| Firewalls | Firewalls perimetrales e internos con reglas estrictas de filtrado de trafico basadas en el principio de minimo privilegio. Listas blancas (whitelisting) y listas negras (blacklisting) de direcciones IP y puertos, inspeccion profunda de paquetes (DPI). |
| Antivirus y Antimalware | Soluciones antivirus/antimalware actualizadas en todos los endpoints y servidores. Analisis en tiempo real y programados, actualizaciones automaticas de firmas. |
| Actualizaciones y Parches | Proceso robusto de gestion de parches para identificar, probar e implementar actualizaciones de seguridad para todos los sistemas operativos, aplicaciones y librerias de manera oportuna. Herramientas de gestion de parches automatizadas. |

#### Criptografia

| Componente | Implementacion |
|---|---|
| Cifrado | Algoritmos de cifrado fuertes y estandares de la industria: **AES-256** para datos en reposo, **TLS 1.2 o superior** para datos en transito. Gestion de claves criptograficas segura. |
| Firmas Digitales | Criptografia de clave publica para verificar autenticidad e integridad de los datos, asegurando el no repudio. Uso de certificados digitales validos y confiables. |

#### Gestion de Incidentes de Seguridad

| Fase | Acciones |
|---|---|
| Preparacion | Establecer planes de respuesta a incidentes (IRP): roles y responsabilidades, procedimientos de comunicacion, pasos de contencion, erradicacion y recuperacion. |
| Deteccion | Monitoreo continuo de seguridad (SIEM, IDS/IPS, EDR) para identificar actividades anomalas y posibles incidentes en tiempo real. |
| Respuesta | Ejecucion coordinada y eficiente de los planes de respuesta: contener la amenaza, erradicar la causa raiz, recuperar los sistemas afectados y aprender de la experiencia. Herramientas forenses y de analisis de malware cuando sea necesario. |

#### Sensibilizacion y Formacion

| Componente | Implementacion |
|---|---|
| Conciencia en Seguridad | Programa continuo de concienciacion en seguridad para todos los funcionarios: mejores practicas, riesgos ciberneticos comunes (phishing, malware, ingenieria social) y responsabilidades en la proteccion de la informacion. Plataformas de aprendizaje en linea y simulaciones de ataques. |

#### Cumplimiento Normativo

| Componente | Implementacion |
|---|---|
| Regulaciones | Controles especificos para cumplir con normativas: Ley de Proteccion de Datos Personales, Ley Marco de Ciberseguridad, Ley de Derechos y Deberes de los Pacientes, entre otras. |

## Lineamientos de cumplimiento

#### Regulaciones y Normativas

| Componente | Descripcion |
|---|---|
| Cumplimiento Legal | Asegurar que la organizacion cumpla con leyes y regulaciones aplicables al sector salud y gobierno, ademas de las regulaciones existentes en el territorio nacional y en el pais donde se aloje la infraestructura (cloud). |
| Normativas de la Industria | Estandares y regulaciones especificos del sector salud. |

#### Politicas Internas

| Componente | Descripcion |
|---|---|
| Politicas de la Organizacion | Normas internas y expectativas en areas como uso de tecnologia, seguridad de la informacion y comportamiento etico. |
| Politicas de Privacidad | Como se manejan y protegen los datos personales de pacientes, empleados y otros. |

#### Proteccion de Datos

| Componente | Descripcion |
|---|---|
| Privacidad de Datos | Como se recopilan, almacenan y utilizan los datos personales, en cumplimiento con regulaciones de proteccion de datos. |

#### Seguridad de la Informacion

| Componente | Descripcion |
|---|---|
| Gestion de Riesgos de Seguridad | Implementar medidas de seguridad adecuadas para proteger la informacion sensible y prevenir brechas de seguridad. |

#### Informes y Auditorias

| Componente | Descripcion |
|---|---|
| Documentacion | Mantener registros y documentacion que demuestren el cumplimiento de las regulaciones y politicas. |
| Auditorias Internas y Externas | Permitir evaluar y verificar el cumplimiento y la efectividad de las medidas de cumplimiento. |

#### Adaptacion y Actualizacion

| Componente | Descripcion |
|---|---|
| Cambio en Regulaciones | Los Lineamientos de Cumplimiento deben ser revisados durante el periodo de construccion de cualquier solucion, permitiendo estar al dia con el cumplimiento de cada hito. |

## Lineamientos de rendimiento

| # | Lineamiento | Descripcion |
|---|---|---|
| 1 | Establecimiento de Objetivos | Definir metas de rendimiento especificas para los sistemas y aplicaciones: tiempos de respuesta, velocidad de procesamiento y capacidad de usuarios concurrentes. |
| 2 | Diseno Eficiente | Desarrollar sistemas y aplicaciones utilizando principios de diseno que minimicen la sobrecarga y optimicen los recursos: minimizacion de consultas de bases de datos y reduccion de llamadas de red. |
| 3 | Optimizacion de Codigo | Identificar areas de codigo que puedan ralentizar el rendimiento y optimizar los algoritmos y procesos para lograr ejecuciones mas rapidas. |
| 4 | Gestion de Carga | Implementar estrategias para manejar momentos de alta demanda: escalabilidad automatica en la nube o distribucion de la carga de trabajo en servidores. |
| 5 | Monitorizacion y Analisis | Supervisar constantemente el rendimiento de los sistemas y aplicaciones para identificar cuellos de botella y puntos problematicos. |
| 6 | Ajuste y Optimizacion Continua | Realizar ajustes regulares en funcion de los datos de monitorizacion y las pruebas de rendimiento para mantener y mejorar el rendimiento. |
| 7 | Almacenamiento y Memoria | Optimizar el uso de recursos de almacenamiento y memoria para minimizar la latencia y mejorar el rendimiento de lectura y escritura. |
| 8 | Redes y Comunicacion | Minimizar la latencia y mejora el rendimiento de las comunicaciones utilizando tecnicas como la compresion de datos y la cache de contenidos. |
| 9 | Tiempos de Respuesta | Asegurar que los sistemas y las aplicaciones respondan a las solicitudes de los usuarios en un tiempo aceptable. |
| 10 | Pruebas de Rendimiento | Realizar pruebas rigurosas para evaluar el rendimiento en diferentes escenarios: cargas de trabajo pesadas y picos de demanda. |
| 11 | Optimizacion de Base de Datos | Asegurar que las bases de datos esten optimizadas para consultas rapidas y eficientes, mediante indices y optimizacion de consultas. |

## Lineamientos de integracion

| # | Lineamiento | Descripcion |
|---|---|---|
| 1 | Estandarizacion | Establecer y ajustarse a los estandares y protocolos para la comunicacion y el intercambio de datos entre sistemas. |
| 2 | Interfaces Claras | Definir interfaces bien documentadas y robustas que especifican como los sistemas interactuan entre si. |
| 3 | APIs y Servicios Web | Utilizar APIs y servicios web para permitir la comunicacion y la integracion entre sistemas heterogeneos. |
| 4 | Formatos de Datos | Establecer formatos de datos estandar para asegurar que la informacion se pueda intercambiar y comprender de manera consistente. |
| 5 | Middleware | Utilizar el middleware proporcionado para simplificar la comunicacion entre aplicaciones: sistemas de mensajeria y buses de servicios. |
| 6 | Integracion en Tiempo Real | Permitir la integracion de datos y procesos en tiempo real, asegurando que la informacion este actualizada y precisa en todos los sistemas. |
| 7 | Automatizacion | Utilizar herramientas y soluciones de automatizacion aprobadas por TIC para facilitar la configuracion y gestion de la integracion entre sistemas. |
| 8 | Gestion de Identidad | Asegurar que los sistemas puedan compartir y verificar la identidad de los usuarios de manera segura, mediante soluciones de autenticacion y autorizacion. |
| 9 | Sincronizacion y Migracion de Datos | Definir procesos y estrategias para sincronizar y migrar datos entre sistemas, manteniendo la coherencia, integridad y ajustandose a los estandares definidos. |
| 10 | Pruebas de Integracion | Realizar pruebas rigurosas para garantizar que la integracion entre sistemas funcione segun lo previsto y que los datos se transfieran correctamente. |
| 11 | Monitorizacion y Mantenimiento | Supervisar constantemente la salud y el rendimiento de las integraciones, incluyendo health checks para identificar problemas y realizar ajustes. |

## Consideraciones de infraestructura

| # | Consideracion | Descripcion |
|---|---|---|
| 1 | Escalabilidad | Disenar las soluciones para poder crecer o reducirse segun las demandas cambiantes de la organizacion. |
| 2 | Rendimiento | Optimizar la solucion para ofrecer un rendimiento adecuado, asegurando que los recursos sean aprovechados de la mejor manera posible. |
| 3 | Seguridad | No modificar innecesariamente las medidas de seguridad existentes en la infraestructura. Proteger los activos y datos contra amenazas ciberneticas y acceso no autorizado. |
| 4 | Cumplimiento | Asegurar que se cumpla con las regulaciones que el area de infraestructura provea. |
| 5 | Almacenamiento | Disenar una estrategia de almacenamiento que permita un acceso rapido y seguro a los datos, al mismo tiempo que garantiza su respaldo y recuperacion. |
| 6 | Redes | Disenar el intercambio de informacion para que se ajuste a los requerimientos de red definidos, asi como a los protocolos establecidos. |

## Evaluacion de tecnologias

| # | Fase | Descripcion |
|---|---|---|
| 1 | Identificacion de Requisitos | Comprender claramente los requisitos y las necesidades de la solucion para determinar que caracteristicas y funcionalidades son esenciales en la tecnologia a evaluar. |
| 2 | Consideraciones de Costos | Evaluar los costos asociados con la adquisicion, implementacion, capacitacion y mantenimiento de la tecnologia a lo largo de su ciclo de vida, considerando licencias. |
| 3 | Evaluacion de Riesgos | Evaluar los riesgos potenciales asociados con la tecnologia: problemas de seguridad, falta de soporte o dificultades de integracion. |
| 4 | Demos y Presentaciones | Generar demos y presentaciones de la tecnologia para obtener una comprension mas profunda de como se adapta a las necesidades. |
| 5 | Analisis de Costo-Beneficio | Evaluar los beneficios potenciales en relacion con los costos y los riesgos. Considerar el impacto positivo en el negocio y requerimientos adicionales. |

Es posible incorporar el uso de nuevas tecnologias al stack tecnologico del Ministerio, siempre que se justifique el uso de cualquiera que no se encuentre ya definido previamente.

## Recomendaciones para la actualizacion del documento

| # | Recomendacion | Descripcion |
|---|---|---|
| 1 | Evaluacion de Nuevas Tecnologias | Evaluar nuevas tecnologias y soluciones emergentes para determinar si se alinean con la vision y los objetivos del Ministerio, y si pueden aportar valor a la arquitectura existente. |
| 2 | Retroalimentacion de Usuarios | Recoger comentarios y retroalimentacion de los usuarios y partes interesadas sobre el rendimiento y la eficacia de la arquitectura actual para identificar areas que necesitan mejoras. |
| 3 | Revision de Requisitos | Actualizar los requisitos de negocio y tecnologicos para asegurar que la arquitectura este alineada con los cambios en la estrategia y las necesidades de la organizacion. |
| 4 | Adaptacion a Cambios en el Negocio | Ajustar la arquitectura para reflejar cambios en la estructura organizativa, nuevos productos o servicios, y cambios en la direccion estrategica. |
| 5 | Actualizacion de Estandares y Lineamientos | Revisar y actualizar los estandares y lineamientos para reflejar las mejores practicas actuales y garantizar la coherencia en el diseno y la implementacion de soluciones. |
| 6 | Revision por Pares y Auditorias | Realizar revisiones por pares y auditorias periodicas para garantizar la calidad y la efectividad de los ajustes realizados. |

## Referencias

### Estandares internacionales (resumen)

| Estandar | Aplicacion |
|---|---|
| ISO/IEC 42010 | Descripcion estandarizada de arquitecturas de sistemas. |
| TOGAF | Marco para desarrollo de arquitecturas empresariales; gobernanza institucional, interoperabilidad y alineamiento estrategico. |
| Archimate | Lenguaje de modelado para representar arquitecturas; relaciones entre procesos, aplicaciones y componentes tecnologicos. |
| COBIT | Gobernanza y gestion de TI alineada con objetivos organizacionales; control y trazabilidad de decisiones arquitectonicas y cumplimiento normativo. |
| NIST SP 800-160 Vol. 1 y 2 | Ingenieria de sistemas seguros; integra ciberseguridad desde el diseno en infraestructuras criticas. |
| Well-Architected Framework (AWS/Azure/GCP) | Buenas practicas para arquitecturas en la nube; evaluacion y mejora continua. |
| ISO/IEC 25010 | Modelo de calidad de productos de software: seguridad, mantenibilidad, eficiencia. |
| ISO/IEC/IEEE 42030 | Evaluacion formal de arquitecturas; calidad y desempeno. |
| HL7/FHIR | Estandares de interoperabilidad entre sistemas clinicos y de salud. |
