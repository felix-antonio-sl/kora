---
_manifest:
  urn: urn:salud:kb:instructivo-seguridad-informacion-ciberseguridad-sector-salud
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-04'
    source: MINSAL Chile, Depto. TIC, Unidad de Seguridad de la Informacion y Ciberseguridad.
      ITS-NC-007 v2.0 (Abril 2025). Clasificacion TLP:BLANCO. Sucede a Res. Exenta
      N°785 (03-Nov-2021)
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- ciberseguridad
- minsal
- sgsi
- defensa-profundidad
- riesgos
- incidentes
- iot
- telemedicina
- ia
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 4
    shard_root_urn: urn:salud:kb:instructivo-seguridad-informacion-ciberseguridad-sector-salud
  salud:
    minsal_id: ITS-NC-007
    minsal_version: '2.0'
    fecha_aprobacion: Abril 2025
    clasificacion: TLP:BLANCO
    autores: Pablo Fabres F., Jose Villa C.
    aprobador: Jorge Herrera R., Jefe Depto. TIC
relations:
  cites:
  - urn:salud:kb:plan-ciberseguridad-sector-salud-2024-2025
  - urn:salud:kb:stack-tecnologico-seguridad-minsal
  - urn:salud:kb:clausulas-seguridad-contratos-ti-sector-salud
  - urn:salud:kb:arquitectura-referencia-desarrollo-sistemas-sector-salud
---

# Instructivo de Seguridad de la Informacion y Ciberseguridad para el Sector Salud


**ITS-NC-007 v2.0, Abril 2025. Caracter obligatorio. TLP:BLANCO.**

## Resumen

Actualizacion integral del Instructivo de Ciberseguridad aprobado por Res. Exenta N°785 (03-Nov-2021). Incorpora: Ley 21.663 Marco de Ciberseguridad, Ley 21.459 Delitos Informaticos, Ley 21.180 Transformacion Digital del Estado, Ley 21.541 Telemedicina, Ley 21.668 Interoperabilidad Fichas Clinicas, Ley 21.719 Proteccion de Datos Personales. Establece lineamientos, directrices y controles de seguridad obligatorios para todas las instituciones del ecosistema MINSAL (Seremis, Servicios de Salud, Hospitales, APS, Organismos Autonomos). Alineado con ISO/IEC 27001:2022, NIST SP 800-53, NIST CSF, CIS Controls v8, HIPAA.

---

## 2. Proposito

Establecer lineamientos, directrices y controles de seguridad obligatorios para las instituciones del ecosistema MINSAL: Ministerio de Salud, Subsecretarias de Salud Publica y Redes Asistenciales, SEREMIs, Servicios de Salud, Hospitales, APS, Organismos Autonomos y entidades externas que operen o administren sistemas de informacion en salud.

Marco normativo base: Ley 21.663 (Marco de Ciberseguridad), Ley 21.180 (Transformacion Digital del Estado), ISO/IEC 27001:2022, ISO/IEC 27002:2022, NIST SP 800-53, NIST CSF, CIS Controls v8, HIPAA. Alineado con Politica General de Seguridad de la Informacion y Ciberseguridad (Res. Exenta N°1465/2023).

Objetivo: reforzar confidencialidad, integridad, disponibilidad y trazabilidad de datos en cumplimiento de Ley 19.628 (Proteccion de la Vida Privada), Ley 21.719 (Proteccion de Datos Personales), Ley 20.584 (Derechos y Deberes de los Pacientes), Ley 21.541 (Telemedicina), Ley 21.668 (Interoperabilidad de Fichas Clinicas).

## 3. Alcance y Aplicabilidad

### 3.1. Alcance

| Institucion | Inclusion |
|---|---|
| Ministerio de Salud | Obligatorio |
| Subsecretarias de Salud Publica y Redes Asistenciales | Obligatorio |
| Seremis Regionales Ministeriales | Obligatorio |
| Servicios de Salud y establecimientos hospitalarios | Obligatorio |
| Centros de Atencion Primaria de Salud (APS) | Obligatorio |
| Organismos Autonomos de Salud | Obligatorio |
| Entidades externas que operen/administren sistemas de informacion en salud | Obligatorio |

### 3.2. Aplicabilidad

Ambito de aplicacion:
- **Infraestructura tecnologica**: redes, servidores, plataformas en la nube, dispositivos conectados
- **Sistemas de informacion**: software de gestion clinica, RCE, telemedicina, bases de datos
- **Gestion de accesos**: autenticacion, control de privilegios, monitoreo de actividad
- **Proteccion de datos sensibles**: cifrado, seudonimizacion, anonimizacion
- **Gestion de incidentes de ciberseguridad**: deteccion, respuesta, mitigacion

Todos los procesos de compra que realicen instituciones del sector deben contener la obligacion del proveedor de ceñirse a los lineamientos de este instructivo.

## 4. Elementos Claves para la Gestion de la Seguridad de la Informacion

### 4.1. Gobernanza

La Ley 21.663 establece que las instituciones publicas deben implementar una estructura de gobernanza para proteger sistemas criticos de informacion. La Ley 21.459 exige un marco de gobernanza que permita detectar, obtener evidencias y denunciar incidentes que pudieran revestir caracteres de delito. NIST CSF 2.0 destaca la funcion de gobierno para que la alta direccion comprenda y gestione los riesgos.

Las instituciones del sector salud deben:

| Directriz | Accion requerida |
|---|---|
| Responsable de ciberseguridad | Designar encargado de coordinar gestion de riesgos y cumplimiento normativo |
| Politicas y procedimientos | Implementar alineados con estandares nacionales e internacionales |
| Comites de Seguridad | Conformar Comite de Seguridad de la Informacion, Ciberseguridad y Proteccion de Datos Personales |
| Roles y responsabilidades | Establecer claramente con asignacion de funciones |
| Monitoreo continuo | Implementar estrategia con auditorias, capacitaciones y simulacros |

### 4.2. Compromiso del Nivel Directivo

La Ley 21.663 establece que "Autoridades y directivos de las instituciones tienen un rol fundamental en la gobernanza de la ciberseguridad, debiendo asumir un compromiso activo y vinculante". Implica:

| Compromiso | Descripcion |
|---|---|
| Incorporar ciberseguridad en estrategia institucional | Alineacion con objetivos organizacionales |
| Asignar recursos suficientes | Talento humano, tecnologias, capacitacion |
| Fomentar cultura organizacional de seguridad | Concienciacion, liderazgo visible, formacion continua |
| Supervisar y evaluar cumplimiento | Revision periodica de politicas y eficacia de controles |
| Enfoque integral ante incidentes | Prevencion, deteccion oportuna, mitigacion de impactos |

### 4.3. Estrategia de Seguridad y Plan Director de Seguridad

Estrategia de seguridad queda establecida en el **Plan Director de Seguridad de la Informacion y Ciberseguridad para el Sector Salud** (2024-2025, Res. Exenta N°969/2024 o vigente). Enfoque basado en riesgos y estandares de la industria.

Consideraciones clave:

| Requisito | Descripcion |
|---|---|
| Sponsor directivo | Representante de alta direccion con atribuciones para garantizar alineamiento estrategico |
| Recursos adecuados | Financieros, tecnologicos y humanos |
| Compromiso sectorial | Participacion activa de instituciones del sector |
| Plan Director institucional | Cada institucion debe desarrollar y mantener su propio plan adaptado a su realidad operativa |

## 5. Directrices para la Implementacion SGSI

Implementar un SGSI basado en principios de gobernanza, gestion de riesgos, cumplimiento normativo y mejora continua (ISO/IEC 27001:2022, Ley 21.663).

## 5.1. Gobernabilidad de la Seguridad de la Informacion y Ciberseguridad

| Elemento | Contenido requerido |
|---|---|
| Designacion formal de responsables | CISO, Comite de Seguridad de la Informacion, responsables locales |
| Integracion de la seguridad | Niveles estrategico, tactico y operativo |
| Politicas formales | Aprobadas por autoridad institucional |
| Rendicion de cuentas | Mecanismos de reporte hacia alta direccion |
| Coordinacion transversal | Areas clinicas, administrativas, TI y juridicas |

## 5.2. Roles y Responsabilidades

#### Alta Direccion Institucional / Direccion del Establecimiento de Salud

| Responsabilidad |
|---|
| Aprobar formalmente la politica de seguridad de la informacion |
| Proveer recursos necesarios (humanos, tecnologicos, financieros) para implementacion del SGSI |
| Asumir la responsabilidad final del tratamiento de riesgos institucionales |
| Participar en la revision de informes de impacto y presentacion de riesgos criticos |
| Aprobar planes de tratamiento y priorizacion de iniciativas |

#### Encargado de Seguridad de la Informacion y Ciberseguridad (CISO)

| Responsabilidad |
|---|
| Liderar implementacion, mantenimiento y mejora del SGSI a nivel institucional |
| Coordinar el Comite de Seguridad de la Informacion |
| Supervisar elaboracion del analisis de riesgos, plan de tratamiento y seguimiento de controles |
| Asegurar cumplimiento normativo y controles alineados a ISO/IEC 27001, NIST y legislacion nacional |
| Gestionar incidentes de seguridad y liderar respuesta ante ciberataques |
| Promover cultura de seguridad mediante capacitacion y concientizacion |

#### Comite de Seguridad de la Informacion

| Responsabilidad |
|---|
| Instancia transversal con representacion de areas clinicas, administrativas, legales y de TI |
| Analizar riesgos institucionales desde multiples perspectivas |
| Evaluar planes de tratamiento propuestos y sugerir prioridades |
| Apoyar integracion de seguridad en procesos estrategicos, operativos y clinicos |
| Monitorear cumplimiento de politicas y procedimientos internos |

#### Responsables Locales de Seguridad (en cada unidad o establecimiento)

| Responsabilidad |
|---|
| Implementar y mantener controles de seguridad en su area de responsabilidad |
| Coordinar con el CISO el levantamiento de activos, analisis de riesgos y respuesta a incidentes |
| Sensibilizar al personal sobre politicas y buenas practicas de seguridad |
| Participar en auditorias internas o revisiones de cumplimiento |

#### Encargado de Tecnologia / Jefe de Informatica

| Responsabilidad |
|---|
| Implementar controles tecnicos (firewalls, cifrado, autenticacion, etc.) conforme a lineamientos del SGSI |
| Garantizar alta disponibilidad, respaldo y continuidad operativa de los sistemas |
| Colaborar en levantamiento de activos tecnologicos e integracion de medidas de seguridad en nuevos proyectos |
| Aplicar pruebas de seguridad sobre APIs, plataformas y redes criticas |

#### Usuarios Finales / Funcionarios de Salud

| Responsabilidad |
|---|
| Cumplir con politicas, lineamientos y procedimientos institucionales de seguridad |
| Participar en capacitaciones obligatorias |
| Reportar oportunamente incidentes o eventos sospechosos |
| Proteger sus credenciales de acceso y manejar la informacion con responsabilidad |

#### Auditor Interno / Control Interno

| Responsabilidad |
|---|
| Evaluar periodicamente el nivel de cumplimiento del SGSI |
| Verificar la eficacia de los controles implementados |
| Emitir informes con hallazgos y recomendaciones a la alta direccion |
| Apoyar la preparacion de evidencias para fiscalizaciones externas |

## 5.3. Identificacion de los Activos de Informacion y su Orden de Criticidad

| Requisito | Descripcion |
|---|---|
| Inventario de Activos de Informacion | Digitales y fisicos |
| Clasificacion por criticidad | Alta, media, baja (impacto en confidencialidad, integridad, disponibilidad, trazabilidad) |
| Inclusion de activos tecnologicos | Sistemas HIS, servidores, dispositivos IoT, bases de datos |
| Inclusion de activos informacionales | Datos clinicos, administrativos, legales |
| Asignacion de responsables | Custodios por activo |
| Relacion activos-procesos | Para facilitar analisis de riesgos |

## 5.4. Gestion de Riesgos

Proceso metódico para identificar, analizar, evaluar y abordar riesgos. Razones criticas para el sector salud: proteccion de informacion del paciente, continuidad del negocio, cumplimiento legal, toma de decisiones informada, mejora de resiliencia, generacion de confianza.

### 5.4.1. Metodologias de Gestion de Riesgos

| Metodologia | Aplicacion |
|---|---|
| ISO 31000 | Gestion de Riesgos general |
| ISO/IEC 27005 | Gestion de Riesgos en Seguridad de la Informacion |
| NIST RMF | Marco de Gestion de Riesgos del NIST |
| MAGERIT | Metodologia de Analisis y Gestion de Riesgos (CSAE, Espana) |
| Politica de Gestion de Riesgos MINSAL | Complemento normativo nacional |

### 5.4.1.1. Flujo de Gestion de Riesgos

| Etapa | Actividades |
|---|---|
| **Establecimiento del Contexto** | Definir objetivos, alcance, criterios de riesgo, metodologia. Documentar. |
| **Identificacion de Riesgos** | Inventario de activos, identificacion de amenazas y vulnerabilidades, desarrollo de escenarios de riesgo |
| **Analisis de Riesgos** | Evaluar impacto y probabilidad, determinar nivel de riesgo (alto, medio, bajo) |
| **Evaluacion de Riesgos** | Comparar niveles con criterios de aceptacion, priorizar riesgos para tratamiento |
| **Tratamiento de Riesgos** | Elaborar e implementar Plan de Tratamiento: acciones, responsables, plazos, recursos. Opciones: mitigar, transferir, evitar, aceptar |
| **Monitoreo y Revision** | Seguimiento continuo de riesgos e implementacion de controles, revision periodica del proceso |

### 5.4.2. Plan de Tratamiento

Debe incluir: actividades concretas con responsables, justificacion tecnica y normativa, calendario de implementacion con fechas, criterios de validacion o cierre. Requiere aprobacion de autoridad correspondiente y monitoreo periodico por el Comite de Seguridad de la Informacion.

### 5.4.3. Informe de Impacto y Presentacion Directiva

El Informe de Impacto debe identificar: riesgos que afectan continuidad clinica/administrativa, vulnerabilidades de mayor impacto en sistemas criticos (HIS, bases de datos, redes internas), consecuencias ciudadanas, legales, operativas y reputacionales. Presentar a direccion del establecimiento. La retroalimentacion debe integrarse a mejora continua del SGSI.

### 5.4.4. Mejora Continua

Ciclo PDCA (Planificar - Hacer - Verificar - Actuar) conforme ISO 27001:

| Actividad |
|---|
| Revision periodica de politicas y controles |
| Evaluaciones de madurez y auditorias regulares |
| Actualizacion de analisis de riesgos |
| Reforzamiento de capacidades institucionales (formacion, sensibilizacion) |
| Retroalimentacion a partir de incidentes, brechas o hallazgos detectados |

## 5.5. Politica General, Especificas y Procedimientos

Cada institucion debe elaborar, formalizar, implementar y mantener una **Politica General de Seguridad de la Informacion y Ciberseguridad** como marco rector de alto nivel. Lenguaje accesible, alineado con leyes, decretos y estandares nacionales e internacionales vigentes.

### 5.5.1. Politicas Especificas

Areas criticas a cubrir:

| Politica Especifica |
|---|
| Accesos fisicos y logicos a activos de informacion |
| Relaciones con terceros y seguridad en cadena de suministro |
| Continuidad operativa (respaldo, DRP, BCP) |
| Clasificacion, etiquetado y manejo seguro de informacion por nivel de sensibilidad |
| Seguridad de activos de hardware y software |
| Comunicaciones seguras y proteccion contra malware |
| Gestion de incidentes de seguridad |
| Cumplimiento normativo especifico (proteccion de datos personales, seguridad de informacion de salud) |
| Uso aceptable de recursos informaticos |
| Seguridad en el desarrollo de software |

### 5.5.2. Procedimientos e Instructivos Operacionales

Procedimientos minimos recomendados a documentar y mantener (priorizar segun criterios):

| Procedimiento | Criterio de priorizacion |
|---|---|
| Gestion de ficha clinica electronica y en papel | Datos sensibles de salud |
| Gestion de agendas y programacion de atenciones | Afecta continuidad operativa |
| Gestion y control de inventarios de activos tecnologicos y clinicos | Sistemas informaticos criticos |
| Gestion de respaldos y recuperacion ante desastres | Afecta continuidad operativa |
| Control de accesos fisicos y logicos | Multiples unidades/actores externos |
| Tratamiento de incidentes de seguridad de la informacion | Datos sensibles de salud |
| Alta, modificacion y baja de usuarios | Sistemas informaticos criticos |
| Entrega de informacion a terceros | Multiples unidades/actores externos |

Criterios de priorizacion cuando no sea posible documentar todos:
1. Procesos con datos personales o sensibles de salud
2. Procesos que afecten continuidad operativa
3. Procesos con sistemas informaticos criticos (HIS, RIS, PACS, LIS)
4. Procesos con multiples unidades y/o actores externos
5. Procesos con incidentes, hallazgos de auditoria o vulnerabilidades previas

## 6. Directrices para una Arquitectura de la Seguridad de la Informacion y Ciberseguridad

Modelo de Seguridad por Capas / Defensa en Profundidad (DiD). Principio de seguridad y privacidad por defecto y desde el diseno (Ley 21.663, Ley 19.628, Ley 20.584). Controles tecnicos, fisicos y administrativos integrados.

## 6.1. Capas de Seguridad en Entornos de Salud

Modelo de defensa en profundidad con 8 capas de controles superpuestos: fisica, red, perimetral, aplicaciones, datos, endpoints, operaciones/monitoreo y nube.

## 6.1.1. Capa de Seguridad Fisica

Controles minimos:

| Control | Detalle |
|---|---|
| Control de acceso biometrico y tarjetas inteligentes | Lectores biometricos (huella, iris), tarjetas RFID personalizadas |
| Videovigilancia perimetral (CCTV) | Grabacion, monitoreo, analitica de video, alertas integradas |
| Zonificacion fisica y separacion de areas | Zonas de seguridad diferenciadas, barreras fisicas, jaulas de racks, salas blancas |
| Sistemas de deteccion de intrusos (IDS) fisicos | Alertar sobre accesos no autorizados |
| Sensores ambientales | Temperatura, humedad, alimentacion electrica (SAI/UPS, generadores) |
| Detectores de humo, humedad, temperatura y fallos electricos | Conectados a sistemas de gestion de instalaciones (BMS) |

## 6.1.2. Capa de Seguridad de Red

| Control | Detalle |
|---|---|
| Firewalls de ultima generacion (NGFW) | DPI, filtrado por aplicacion, geo-bloqueo, inspeccion SSL/TLS, IPS, sandboxing |
| IDS/IPS | Monitoreo de trafico, deteccion de actividad sospechosa, bloqueo/alertas |
| Listas de Control de Acceso (ACLs) | Control a nivel IP y puerto en enrutadores y switches |
| Segmentacion de Red | VLANs, subredes, arquitecturas Zero Trust, microsegmentacion para sistemas criticos, redes clinicas, administrativas, IoT y visitantes |
| VPNs seguras | Cifrado IPsec o SSL, autenticacion robusta, tuneles cifrados por usuario/dispositivo |
| Politicas de Filtrado de Contenido | Filtrado web y de correo electronico |
| Monitoreo del Trafico de Red | Continuo, deteccion de anomalias en tiempo real |

## 6.1.3. Capa de Seguridad del Perimetro

| Control | Detalle |
|---|---|
| WAF (Web Application Firewall) | Proteccion contra inyecciones SQL, XSS |
| Proteccion contra DDoS | Sistemas dedicados o servicios en la nube |
| Filtrado de Contenido Web | Bloqueo de sitios maliciosos y contenido inapropiado |
| Gestion de Amenazas Unificada (UTM) | Firewall, IPS, antivirus de gateway, filtrado web integrados |
| Politicas de Acceso Remoto Seguro | VPNs con autenticacion fuerte y cifrado |
| Monitoreo y Alertas | Integrados con SIEM |
