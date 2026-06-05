---
_manifest:
  urn: urn:salud:kb:politica-general-seguridad-informacion-ciberseguridad
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-05'
    source: 'MINSAL Chile, SGSI Nivel Central. PS-NC-005 v5, mayo 2025. Elaborado:
      Pablo Fabres F., Jose Villa C. Revisado: Jose Villa C. Aprobado: Jorge Herrera
      R., Jefe Depto. TIC.'
  extensions:
    kora:
      family: note
    salud:
      minsal_id: PS-NC-005
      minsal_version: '5'
      fecha_aprobacion: mayo 2025
      paginas: 20
      ambito: Nivel Central, Subsecretarias de Salud Publica y Redes Asistenciales
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- ciberseguridad
- minsal
- sgsi
- politica-general
- iso-27001
- gobernanza
- incidentes
- continuidad
- ia-transparencia
lang: es
relations:
  cites:
  - urn:salud:kb:instructivo-seguridad-informacion-ciberseguridad-sector-salud
extensions:
  kora:
    shard_index: 1
    shard_count: 2
    shard_root_urn: urn:salud:kb:politica-general-seguridad-informacion-ciberseguridad
---

# Politica General de Seguridad de la Informacion y Ciberseguridad del Ministerio de Salud


**PS-NC-005 v5, mayo 2025. Nivel Central MINSAL.**

## Marco y Ambito

Establece el marco de referencia y directrices para proteger la informacion y sistemas del MINSAL, salvaguardando confidencialidad, integridad y disponibilidad de activos de informacion y mitigando riesgos de ciberseguridad.

Ambito: integral y transversal sobre todas las operaciones, sistemas, recursos y procesos de gestion de la informacion y ciberseguridad del MINSAL. Aplica a:

| Grupo | Inclusion |
|---|---|
| Funcionarios (planta, contrata, reemplazos, suplencia) | Obligatorio |
| Personal a honorarios | Obligatorio |
| Terceros (proveedores, compra de servicios, externalizados) | Obligatorio |
| Ambito geografico | Nivel Central: Subsecretarias de Salud Publica y Redes Asistenciales |

Requerimientos de seguridad hacia terceros y honorarios deben constar en TDR, bases de licitacion y contratos.

Controles ISO 27001:2022 cubiertos:

| Control | Descripcion |
|---|---|
| A.05-5.1 | Politicas para la seguridad de la informacion |
| A.05-5.2 | Roles y responsabilidades en seguridad de la informacion |
| A.05-5.36 | Cumplimiento de politicas, reglas y normas de seguridad de la informacion |

Materias que aborda: politicas de seguridad, revision de politicas, roles y responsabilidades, revision independiente de seguridad.

## Declaracion Institucional y Principios

MINSAL se compromete a gestion continua de seguridad de la informacion y ciberseguridad conforme a normativa gubernamental vigente. Implementa plan de mejora continua basado en NCh-ISO 27001:2022 (SGSI), complementado con estandares nacionales e internacionales adaptados al sector salud. Alineado con Ley 21.663 Marco de Ciberseguridad.

Trece principios institucionales:

| N° | Principio |
|---|---|
| i | Informacion como recurso esencial en salud: valor estrategico, rol fundamental en toma de decisiones |
| ii | Proteger privacidad y confidencialidad de toda informacion sensible o personal, cualquier formato o medio |
| iii | Preservar integridad de los datos: exactitud y actualizacion pueden ser vitales |
| iv | Garantizar acceso a informacion critica solo para usuarios autorizados y en momentos pertinentes |
| v | Implementar modelo de gestion de riesgos para identificar y mitigar riesgos relevantes con controles apropiados |
| vi | Cumplir marco normativo de seguridad de la informacion en sector salud e institucional mediante controles definidos |
| vii | Respaldos seguros con proteccion de informacion del sector salud; definir responsabilidades y frecuencia de pruebas de restauracion para sistemas criticos |
| viii | Identificar, analizar, notificar, responder y aprender de debilidades e incidentes para mitigacion y prevencion |
| ix | Programas educativos para personal del sector salud en seguridad de la informacion y ciberseguridad |
| x | Plataforma de intercambio reciproco de experiencias y aprendizaje en seguridad de la informacion del sector Salud |
| xi | Responsabilidades frente a la seguridad definidas, compartidas, publicadas y aceptadas por cada funcionario, proveedor o tercero |
| xii | Lineamientos de interoperabilidad para proteccion cohesiva y robusta de sistemas y datos |
| xiii | Desarrollo e implementacion de sistemas de IA de forma etica, segura y centrada en las personas |

## Objetivos de la Gestion

### Objetivo General

Establecer vision estrategica de seguridad de la informacion y ciberseguridad con marco integral que promueva entorno seguro y consciente, garantizando proteccion, confidencialidad, integridad y disponibilidad de activos de informacion y mitigacion de riesgos ciberneticos. Proposito: salvaguardar intereses publicos, asegurar cumplimiento de obligaciones legales y normativas, fortalecer confianza ciudadana en gestion de datos y servicios electronicos.

La politica establece directrices generales para mantener niveles aceptables de seguridad en componentes de software, hardware, sistemas informaticos y datos que gestionan, almacenan, procesan e interoperan.

### Objetivos Especificos

| # | Objetivo |
|---|---|
| 1 | Identificar y registrar activos de informacion relevantes (directos e indirectos) en procesos institucionales criticos y de soporte |
| 2 | Establecer roles y responsabilidades para esquema de gobernanza consistente con necesidades institucionales y riesgos de avances tecnologicos |
| 3 | Implementar modelo de gestion de riesgos de seguridad de la informacion y ciberseguridad para comprension precisa de amenazas, identificacion y mitigacion con controles apropiados |
| 4 | Garantizar proteccion integral en procesamiento, conservacion y transmision: prevenir acceso no autorizado, revelaciones accidentales, errores, fraudes, sabotajes, violaciones de privacidad |
| 5 | Establecer protocolos claros de gestion de incidentes: detectar, notificar, responder y recuperarse eficientemente |
| 6 | Utilizar y mantener efectivamente la estructura de estandares, politicas y procedimientos de seguridad |
| 7 | Minimizar probabilidad de eventos contingentes que interrumpan operacion normal; reducir impacto de danos a instalaciones, almacenamiento, equipos de procesamiento y comunicacion |
| 8 | Aplicar planes de continuidad operacional ante situaciones contingentes |
| 9 | Sensibilizar y capacitar a funcionarios sobre responsabilidad en seguridad; crear cultura organizacional que integre seguridad como aspecto fundamental |

## Roles y Responsabilidades

### Comite de Seguridad de la Informacion y Ciberseguridad

| Funcion |
|---|
| Desarrollar y revisar politicas, directrices y procedimientos de seguridad de la informacion y ciberseguridad; definir estandares y mejores practicas |
| Supervisar implementacion de la estructura documental del SGSI |
| Proponer estrategias o soluciones para implementar o controlar componentes de la estructura documental del SGSI |
| Arbitrar conflictos en materia de seguridad de la informacion y riesgos asociados; proponer soluciones |
| Revisar y monitorear incidentes de seguridad; establecer acciones preventivas y correctivas |
| Coordinarse con el Comite de Riesgos de la Institucion para estrategias comunes de gestion |
| Revisar elementos del SGSI y proponer mejoras a traves del Encargado de Seguridad y Ciberseguridad |
| Difundir componentes de la estructura documental del SGSI via Intranet y medios de comunicacion institucionales |
| Monitorear cambios significativos que pudieran variar los riesgos |
| Establecer acciones y proponer iniciativas para mejorar la seguridad de la informacion y ciberseguridad |
| Supervisar auditorias de Seguridad de la Informacion y Ciberseguridad internas o externas |

### Encargado de Seguridad de la Informacion y Ciberseguridad (CISO)

Responsable institucional: velar por la seguridad de la informacion y ciberseguridad, asegurar desarrollo, cumplimiento y actualizacion de la Politica, gestionar la administracion de la seguridad.

| Funcion |
|---|
| Actuar como contraparte frente al Ministerio del Interior en materias relativas a Ciberseguridad para el nivel central del MINSAL |
| Alinear esfuerzos de las distintas areas en proteccion de sistemas tecnologicos e informacion segun criterios de Ciberseguridad |
| Gestionar internamente el tratamiento de incidentes vinculados a activos de informacion, identificados/reportados por Min. Interior o instancias internas, efectuando reportabilidad y seguimiento |
| Apoyar el proceso de Sensibilizacion en Materias de Ciberseguridad al Interior de la Institucion |
| Presidir el comite encargado de actualizar politicas de Ciberseguridad y Seguridad de la Informacion |
| Coordinar acciones para resguardar y asegurar la continuidad del negocio frente a incidentes de Ciberseguridad |
| Resguardar que se informe adecuadamente a todas las personas con acceso a activos de informacion sobre las Politicas vigentes y obligaciones en gestion de incidentes |
| Comunicar al CSIRT Nacional los incidentes de ciberseguridad via https://portal.anci.gob.cl, en representacion del Subsecretario de Salud Publica o de Redes Asistenciales, en sus calidades de jefes de servicio |

### Encargado de los Activos de Informacion

Responsable de identificacion y clasificacion de activos, gestion del riesgo y niveles de seguridad asociados. Esta funcion **no puede ser externalizada bajo ninguna forma**.

### Usuarios Finales

Todos quienes deben acatar las politicas y normativas definidas, independiente de otros roles nominados. Incluye: funcionarios (planta, contrata, reemplazos, suplencia), personal a honorarios, terceros (proveedores, compra de servicios, tratamiento por encargo, externalizados).

Responsabilidades principales:

| Responsabilidad |
|---|
| Utilizar la informacion solo para el proposito autorizado |
| Conocer las politicas y procedimientos de seguridad de la informacion institucionalizados |
| Cumplir los controles establecidos en politicas y procedimientos del SGSI de ambas Subsecretarias |
| Tomar medidas adecuadas para evitar divulgacion o uso no autorizado de informacion |
| Comunicar los incidentes relativos a la seguridad de la informacion |
| Responder por el uso de cualquier recurso de procesamiento de la informacion bajo su responsabilidad |

## Gobernanza y Estructura Organizacional

Ley 21.663 establece estructura de gobernanza para ciberseguridad en Chile. DS N°7/2023 establece Norma Tecnica de Seguridad de la Informacion y Ciberseguridad (en linea con Ley 21.180 sobre Transformacion Digital del Estado) exigiendo roles especificos: responsable institucional de seguridad de la informacion y ciberseguridad, y encargado de activos de informacion. NIST Cybersecurity Framework resalta la gobernanza como funcion que permite a la alta direccion entender y gestionar riesgos, alineandolos con estrategia organizacional.

Estructura de gobernanza MINSAL:

| Componente | Descripcion |
|---|---|
| Unidad de Seguridad de la Informacion y Ciberseguridad | Define, impulsa y controla politicas y estrategias. Depende funcionalmente del Depto. TIC, con independencia respecto a responsables operativos de sistemas de informacion. Cuenta con recursos humanos y materiales necesarios |
| Encargado de Seguridad de la Informacion y Ciberseguridad (CISO) | Profesional con competencias adecuadas para liderar la unidad, capacidad de decision e influencia en la organizacion, reporta directamente al mas alto nivel institucional |
| Comite de Seguridad de la Informacion y Ciberseguridad | Incluye representantes de areas ministeriales relevantes. Supervisa ejecucion de estrategias de seguridad y respuesta ante incidentes |

## Despliegue Organizacional y Proteccion de Recursos

### Estrategia y Plan Director de Seguridad

Plan Director que detalla iniciativas para salvaguardar activos digitales y procesos tecnologicos esenciales. Fundamentado en gestion de riesgos y estandares nacionales e internacionales. Permite planificar, ejecutar y supervisar medidas de proteccion asegurando continuidad operativa, respuesta ante incidentes y resiliencia digital.

Requisitos para implementacion efectiva:

| Requisito | Descripcion |
|---|---|
| Sponsor directivo | Representante de alta direccion que asegure compatibilidad de objetivos de politica con estrategia institucional; garantizar asignacion y comunicacion clara de responsabilidades y autoridades |
| Recursos adecuados | Alta direccion debe asignar recursos financieros, tecnologicos y humanos necesarios |
| Compromiso sectorial | Participacion y compromiso activo de instituciones del sector para eficacia del SGSI a nivel sectorial y nacional |

### Gestion Transversal

La Gestion de Seguridad de la Informacion y Ciberseguridad se implementa de manera transversal en toda la Institucion, no limitada al Depto. TIC. Aborda procesos interdepartamentales con participacion de sus responsables.

### Seguridad de Recursos Humanos

Informar y educar a todos los empleados y terceros sobre lo esperado en materia de seguridad de la informacion, tanto en red local como en conexiones externas.

### Gestion de Activos

Prioridad primordial: gestion y proteccion efectiva de activos segun clasificacion por nivel de importancia. Abarca hardware, software, dispositivos de comunicacion, elementos de apoyo, informacion y datos en todas sus formas y formatos.

Clasificacion considera: confidencialidad, integridad, disponibilidad de datos, funciones que los activos respaldan y normativa vigente aplicable.

### Autenticacion, Autorizacion y Control de Acceso

Acceso de usuarios debidamente autorizado; prevencion de acceso no autorizado a sistemas de informacion. Procedimientos formales de control en asignacion de derechos de acceso cubriendo todo el ciclo de vida del usuario (registro inicial hasta desvinculacion).

Atencion especial para evitar asignacion de privilegios que permitan eludir controles del sistema. Medidas complementarias:

- Politica de escritorio y pantalla limpios
- Procedimiento de habilitacion y deshabilitacion de perfiles y derechos de acceso segun necesidades institucionales

### Seguridad Fisica y Ambiental

Identificar riesgos vinculados al acceso fisico a instalaciones e infraestructura tecnologica, tanto de funcionarios como de terceros. Objetivo: prevenir acceso no autorizado, danos e interferencias en instalaciones y en la informacion resguardada.

## Controles Tecnicos, Operativos y de Cumplimiento

### Seguridad Operativa

Implementar mecanismos de gestion y monitoreo para salvaguardar infraestructura de TI ante amenazas fisicas y tecnologicas. Proposito: optimizar operacion de plataformas tecnologicas garantizando procesamiento preciso y seguro de la informacion.

### Adquisicion, Desarrollo y Mantenimiento de Sistemas

Abarca sistemas operativos, infraestructura, aplicaciones empresariales y aplicaciones desarrolladas internamente. Identificar y acordar requisitos de seguridad antes del desarrollo y/o implementacion; deben justificarse, acordarse y documentarse como parte integral de los procedimientos.

En desarrollos internos o contratados a terceros: seguridad como componente integral desde la especificacion del software y durante todo el ciclo de vida. Ciberseguridad integrada en cada etapa para proteccion de confidencialidad, integridad y disponibilidad.

### Interoperabilidad

| Elemento | Requerimiento |
|---|---|
| Estandares y protocolos compartidos | Asegurar interaccion segura y eficiente entre diferentes sistemas y tecnologias |
| Cifrado y autenticacion en comunicaciones | Prevenir accesos no autorizados, asegurar confidencialidad de datos transmitidos |
| Procedimientos seguros de intercambio de datos | Mecanismos de validacion de integridad para prevenir alteraciones no autorizadas |
| Planes de contingencia y recuperacion | Considerar interoperabilidad en recuperacion ante fallos para no comprometer la seguridad global |

### Ciberseguridad Operacional

Conjunto integral de practicas y politicas para proteger sistemas, redes y datos contra amenazas ciberneticas:

- Autenticacion solida
- Encriptacion para confidencialidad
- Actualizacion constante de software y sistemas para mitigar vulnerabilidades
- Capacitacion periodica del personal en concienciacion sobre seguridad
- Monitorizacion constante de actividad sospechosa
- Planes de respuesta ante incidentes

Objetivo: mantener integridad, disponibilidad y privacidad de activos digitales de manera efectiva y continua.

### Gestion de Incidentes

Comunicacion oportuna de debilidades, problemas y eventos de seguridad; procedimiento formal para informar eventos y gestionar respuesta. Proceso de escalado con acciones definidas al recibir un informe de evento; ampliamente difundido.

**Reportabilidad obligatoria segun Decreto N°295/2025 del Min. del Interior y Seguridad Publica**:

| Plazo | Accion |
|---|---|
| Max. 3 horas desde deteccion | Alerta temprana al CSIRT Nacional via https://portal.anci.gob.cl |
| Max. 72 horas siguientes | Informe de actualizacion |
| Max. 15 dias corridos | Informe final |
| Max. 7 dias corridos desde deteccion | Plan de accion (operadores de importancia vital) |

Registro actualizado de todos los incidentes: deteccion, analisis, respuesta y resolucion. Permite identificar tendencias, evaluar efectividad de medidas e implementar mejora continua.

Programas de capacitacion y concienciacion para todos los funcionarios: fomentar cultura de seguridad, preparacion para identificar y reportar incidentes oportunamente.

### Continuidad del Negocio

Pilar fundamental para proteger estabilidad de operaciones y salvaguardar activos criticos. Medidas preventivas y de mitigacion para evitar y reducir al minimo impactos de incidentes de seguridad que afecten integridad de redes, equipos y sistemas esenciales.

Desarrollar, implementar, poner en practica y evaluar plan de respuesta integral alineado con estandares internacionales o nacionales de amplio reconocimiento. Centrado en preservar integridad, disponibilidad y confidencialidad de la informacion desde la perspectiva de los clientes.

### Cumplimiento y Auditoria

Anualmente: generacion de procedimientos de auditoria para prevenir incumplimiento de leyes, estatutos, regulaciones, obligaciones contractuales y requisitos de seguridad que afecten el diseno, operacion, uso y gestion de sistemas ministeriales.

Seguimiento y atencion efectiva de recomendaciones para asegurar conformidad con regulaciones en constante evolucion.

### Arquitectura de Referencia

Sistemas tecnologicos se desarrollan e implementan conforme a la Arquitectura de Referencia del MINSAL. Los proyectos deben integrar principios arquitectonicos: seguridad y privacidad de la informacion, interoperabilidad, gestion de datos, infraestructura y usuarios. Ademas: patrones de diseno, metodologias de desarrollo y directrices clave en seguridad, cumplimiento normativo y rendimiento.

Aplicable a todas las iniciativas de desarrollo de sistemas en el sector salud.

### Uso de IA y Transparencia Algoritmica

Uso de sistemas de IA en salud: seguro, etico y transparente, con resultados auditables y cumplimiento de legislacion vigente. Alicacion en sector publico alineada con proteccion de derechos, transparencia y seguridad de la informacion.

Lineamientos:

| Principio | Requerimiento |
|---|---|
| Datos en entornos seguros | Cifrado y controles de acceso rigurosos; anonimizacion o pseudonimizacion para salvaguardar privacidad de pacientes |
| Trazabilidad y auditabilidad | Documentacion adecuada de algoritmos; capacidad de explicar decisiones automatizadas cuando sea necesario |
| Consentimiento informado | Obligatorio antes de usar datos personales para finalidades distintas de las prestaciones de salud. Documentos comprensibles que incluyan: tipo de datos, proposito y alcance, destinatarios, y si se anonimizaran o seudonimizaran |
| Principios eticos | Alineacion con dignidad y derechos humanos de pacientes; cumplimiento de leyes de proteccion de datos y privacidad |
| Supervision humana | Mecanismos de intervencion humana en situaciones donde la IA pueda impactar significativamente la salud o derechos de los pacientes |

## Gestion Documental del SGSI

La documentacion aplicable a las Subsecretarias de Salud Publica y de Redes Asistenciales debe asegurar:

| Requisito |
|---|
| Integracion del modelo de seguridad de la informacion con metodologias y politicas existentes para ambas subsecretarias |
| Cumplimiento de normas legales y reglamentarias de seguridad de la informacion y ciberseguridad, para la informacion y los medios que la contienen |
| Niveles de autorizacion y responsabilidad para utilizacion, divulgacion, administracion, seguimiento y custodia de la informacion |
| Proteccion de la informacion, sus medios de procesamiento, conservacion y transmision contra uso no autorizado, revelaciones accidentales, errores, fraudes, sabotajes, espionaje, violacion de privacidad |
| Medidas de proteccion fisica en medios de procesamiento, conservacion y comunicacion que eviten acceso y/o utilizacion indebida por personal no autorizado |
| Derechos de propiedad sobre la informacion y sistemas establecidos |
| Mecanismos de proteccion de integridad, disponibilidad y confidencialidad en comunicaciones internas y externas |
| Delimitacion de ambitos fisicos de accion de las politicas de seguridad segun distintos niveles de riesgo |
| Acceso a servicios de ambas subsecretarias (medios internos o externos) segun atribuciones de las personas o entidades |
| Monitoreo de actividades y uso de recursos criticos con informacion oportuna para los niveles correspondientes |

## Gestion de Riesgos

A lo menos cada dos anos, el Comite de Seguridad de la Informacion Nivel Central debe gestionar la actualizacion de los riesgos de seguridad, construida a partir del analisis de amenazas y vulnerabilidades a las que estan expuestos los activos de informacion relevantes.

Metodologia enfocada en procesos de provision institucional, sus actividades, actores y activos. Referentes:

- NCh-ISO 31000:2018 (directrices para la gestion de riesgos)
- NCh-ISO/IEC 27005:2020 (gestion del riesgo de seguridad de la informacion)
- Politica General de Seguridad de la Informacion del MINSAL
- Procedimiento de Riesgos de Seguridad de la Informacion del MINSAL

## Indicadores

| Area | Indicador | Descripcion |
|---|---|---|
| Cobertura ISO 27001 | Numero de Controles implementados | Controles de seguridad ISO 27001 implementados en la organizacion |
| Cobertura ISO 27001 | Nivel de Documentacion de Politicas y Procedimientos | Politicas y procedimientos de seguridad documentados segun ISO 27001 |
| Niveles de madurez | Medicion del Nivel de madurez (modelo PMI) | Madurez en procesos operativos y de gestion de seguridad segun ISO 27001 |
| Gestion de incidentes | Tasa de Incidentes de Seguridad | Cantidad de incidentes reportados en un periodo (intrusion, phishing, malware, etc.) |
| Gestion de incidentes | Tiempo de Resolucion de Incidentes | Tiempo desde deteccion hasta cierre del incidente |
| Analisis de vulnerabilidades | Vulnerabilidades Criticas por Aplicacion | Cantidad de vulnerabilidades criticas (alto riesgo) por aplicacion |
| Analisis de vulnerabilidades | Tiempo Promedio de Resolucion de Vulnerabilidades | Tiempo desde descubrimiento hasta resolucion completa |
| Capacitacion | Capacitacion en Seguridad | Porcentaje de funcionarios capacitados en seguridad de la informacion segun ISO 27001 |

## Revision y Medicion

A lo menos una vez al ano, el Comite de Seguridad de la Informacion MINSAL evalua el estado del SGSI e informa al nivel directivo. Considera cambios que puedan afectar el enfoque de gestion de seguridad:

| Aspecto a evaluar |
|---|
| Retroalimentacion de las partes interesadas |
| Resultados de revisiones efectuadas por terceras partes |
| Estado de acciones preventivas y correctivas |
| Cambios en procesos institucionales, nueva legislacion, tecnologia |
| Alertas ante amenazas y vulnerabilidades |
| Informacion relacionada a incidentes de seguridad |
| Recomendaciones provistas por autoridades relevantes |
| Medicion de los indicadores del Sistema |
