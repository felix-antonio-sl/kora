---
_manifest:
  urn: urn:salud:kb:instructivo-seguridad-informacion-ciberseguridad-sector-salud-p03
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
    shard_index: 3
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

# Instructivo de Seguridad de la Informacion y Ciberseguridad para el Sector Salud - Parte 03

## 9. Respuesta ante Incidentes y Continuidad Operacional

### 9.1. Incidentes de Seguridad de la Informacion y Ciberseguridad

Todas las instituciones, publicas y privadas del Sector Salud, deben desarrollar, implementar y mantener un **Plan de Respuesta ante Incidentes (IRP)** conforme a Ley 21.663, Decreto N°295/2024 (Reglamento de Reporte de Incidentes) y estandares internacionales.

#### 9.1.1. Plan de Respuesta ante Incidentes (IRP)

| Etapa | Actividades |
|---|---|
| **Preparacion** | Definir roles y responsabilidades del equipo IR; realizar simulacros de incidentes ciberneticos; asegurar respaldos correctos de sistemas y datos criticos con procedimientos de restauracion listos |
| **Deteccion y Notificacion** | Mecanismos de monitoreo continuo (SIEM) para deteccion en tiempo real; procedimientos claros para que colaboradores reporten incidentes de inmediato con contactos de emergencia |
| **Evaluacion y Contencion** | Evaluar naturaleza y alcance del incidente (activos afectados, magnitud de la brecha); implementar medidas de contencion (desconectar sistemas comprometidos, revocar accesos) |
| **Erradicacion** | Eliminar amenazas y vulnerabilidades relacionadas con el incidente; limpiar sistemas afectados; aplicar parches o soluciones de seguridad |
| **Recuperacion** | Restaurar sistemas y servicios afectados siguiendo procedimientos establecidos; verificar que sistemas restaurados estén libres de amenazas y funcionen de manera segura |
| **Revision Post-Incidente** | Analisis post-incidente para lecciones aprendidas; actualizar procedimientos y mejorar controles; redactar informe detallado con causas, acciones tomadas, impacto y recomendaciones |

#### 9.1.2. Comunicacion en Caso de Incidente

| Nivel | Accion |
|---|---|
| Interna | Notificacion inmediata a responsables y equipos clave (TI, seguridad, gerencia) |
| Autoridades competentes | Reporte si el incidente involucra violacion de datos sensibles o existe obligacion legal |
| Publica y pacientes | Manejo de comunicacion si el incidente afecta los servicios que reciben |

#### 9.1.3. Reporte de Incidentes de Ciberseguridad: Procedimiento y Plazos

**Plataforma Oficial**: https://portal.anci.gob.cl/ (registro con Clave Unica)

**Canales de Contingencia**:
| Canal | Contacto |
|---|---|
| Telefono | 1510 |
| Correo Electronico | ayuda@anci.gob.cl |
| Telefono MINSAL | 800 123573 |
| Correo MINSAL | maso@minsal.cl |
| Correo Seguridad TIC | seguridadtic@minsal.cl |

**Etapas y Plazos de Reporte**:

| Etapa | Plazo | Contenido |
|---|---|---|
| **Alerta Temprana** | **3 horas** desde deteccion | Tipo de amenaza (malware, acceso no autorizado, DDoS); sistemas/datos afectados; gravedad estimada; acciones iniciales de contencion; impacto potencial en la institucion y servicios |
| **Segunda Notificacion** | **72 horas** desde confirmacion | Evolucion del incidente; medidas adoptadas para contencion y erradicacion; restauracion de sistemas y reanudacion de operacion; evaluacion del impacto real en confidencialidad, integridad y disponibilidad de datos; informe de cualquier brecha de seguridad o violacion de datos personales |
| **Informe Final** | **15 dias corridos** desde alerta temprana | Resumen completo del incidente desde deteccion hasta resolucion; detalle de causas y acciones de respuesta; evaluacion del impacto total y lecciones aprendidas; medidas preventivas adoptadas; recomendaciones para mejorar controles y protocolos de respuesta |

**Destinatarios**: ANCI, autoridades competentes, Comite de Seguridad de la Informacion de la institucion.

**Coordinacion Central**: Las instituciones pueden establecer coordinaciones estrategicas con el MINSAL a traves de su CISO o de la Unidad de Seguridad de la Informacion y Ciberseguridad del Depto. TIC, para articulacion conjunta con proveedores de red y fortalecimiento de postura de ciberseguridad, en coordinacion con el CSIRT Nacional.

**Informe de Lecciones Aprendidas**: Realizado por el equipo de respuesta tras la resolucion del incidente. Distribucion interna a todas las partes interesadas; presentacion a autoridades competentes si es necesario.

#### 9.1.4. Confidencialidad y Proteccion de la Informacion

Toda la informacion de alertas, reportes e informes sobre incidentes debe ser tratada con maxima confidencialidad. Las instituciones son responsables de asegurar que la informacion relacionada con incidentes se comparta unicamente con autoridades competentes y partes debidamente autorizadas (Ley 21.663).

### 9.2. Continuidad Operacional

#### 9.2.1. Plan de Continuidad Operacional (BCP) y Plan de Recuperacion ante Desastres (DRP)

Cada institucion debe desarrollar un BCP especifico para el sector salud integrado con un DRP:

| Elemento | Contenido |
|---|---|
| **Analisis de Impacto en el Negocio (BIA)** | Identificar funciones criticas que deben mantenerse operativas (acceso a registros medicos, administracion de tratamientos, operacion de dispositivos medicos); determinar RTO y RPO para cada servicio critico |
| **Estrategias de Respaldo y Recuperacion** | Respaldos regulares en ubicaciones seguras (nube o centros de datos redundantes); plan detallado de DRP que abarque restauracion de sistemas criticos, recuperacion de datos al RPO y reanudacion de servicios dentro del RTO |
| **Planes de Emergencia** | Planes especificos para desastres naturales, fallos en infraestructura o ciberataques; procedimientos claros para evacuacion de datos y reubicacion temporal de servicios en centros alternativos |

#### 9.2.2. Monitoreo de la Continuidad Operacional

| Actividad |
|---|
| Monitorear la salud de sistemas criticos en tiempo real con alertas automaticas ante fallos |
| Verificar periodicamente que los respaldos se realicen segun cronograma y que los procedimientos de recuperacion sean efectivos |
| Realizar simulacros regulares de respuesta ante incidentes y efectividad de los planes de recuperacion |

## 10. Ciberseguridad en Dispositivos Medicos IoT

### 10.1. Instrucciones de Seguridad para Dispositivos Medicos IoT

Los dispositivos IoT en salud abarcan: equipos medicos conectados (monitoreo de signos vitales, bombas de infusion, ventiladores, marcapasos), dispositivos portatiles de diagnostico, dispositivos implantables, equipos de imagenologia con telemetria, sensores corporales vestibles (wearables), sistemas de monitoreo remoto de pacientes, dispositivos inteligentes en entornos criticos (quirofanos, UCI, ambulancias), equipos de diagnostico avanzados con conectividad, infraestructura inteligente (camaras de seguridad, refrigeradores biomedicos, estaciones clinicas inteligentes).

| Instruccion | Especificacion |
|---|---|
| **Inventario y Gestion de Activos** | Inventario completo de todos los dispositivos IoT medicos con: ubicacion fisica, fabricante, modelo, version de firmware, personal responsable |
| **Segmentacion de Red y Accesos Controlados** | Arquitectura segmentada (VLANs + aislamiento fisico de puertos); ACLs y firewalls con reglas especificas limitando comunicacion a lo necesario |
| **Control de Acceso y Autenticacion Segura** | Mecanismos robustos; deshabilitar credenciales predeterminadas de fabrica inmediatamente; prohibir contrasenas debiles; MFA cuando el dispositivo lo permita |
| **Gestion de Vulnerabilidades y Actualizaciones** | Exigir a proveedores parches de seguridad y actualizaciones de firmware regulares con documentacion de pruebas de seguridad; planificar, probar e implementar actualizaciones manteniendo registro |
| **Monitoreo y Registro de Actividades** | Monitoreo continuo del comportamiento de dispositivos; deteccion de accesos no autorizados, modificaciones de configuracion, patrones de trafico anomalos e IoCs; logs detallados para auditorias y analisis forenses |
| **Cifrado de Datos y Comunicaciones** | Cifrado extremo a extremo; estandares criptograficos robustos (TLS 1.2+ para comunicaciones, AES-256 para datos en reposo) |
| **Pruebas de Seguridad y Evaluaciones de Riesgo** | Pentesting y evaluaciones de riesgo especificas antes de puesta en operacion; verificacion de interoperabilidad segura con otros sistemas clinicos/administrativos |
| **Cumplimiento Normativo y Contractual** | Clausulas explicitas de ciberseguridad en contratos con proveedores; concordancia con Ley 21.663, Ley 21.541 y politicas MINSAL |
| **Plan de Contingencia y Respuesta a Incidentes** | Integrar dispositivos IoT en planes de continuidad operativa y respuesta a incidentes; procedimientos especificos para identificacion, contencion, erradicacion y recuperacion de incidentes en estos dispositivos |

## 11. Seguridad en Telemedicina

Conforme a Ley 21.541 y Norma Tecnica N°237 del MINSAL.

### 11.1. Controles de Seguridad para la Telemedicina

| Control | Especificacion |
|---|---|
| **Autenticacion Robusta** | MFA para todos los usuarios (pacientes, profesionales, administrativos); estandares de seguridad ministerial; autenticacion biometrica cuando sea apropiado |
| **Autorizacion y Control de Acceso** | Politicas basadas en roles y privilegios minimos; gestion centralizada de cuentas (creacion, modificacion, revocacion); bloqueo automatico de sesion por inactividad |
| **Confidencialidad de la Informacion** | Cifrado extremo a extremo (TLS 1.2+); proteccion en reposo y transito; cumplimiento Ley 19.628 |
| **Integridad de la Informacion** | Mecanismos de verificacion de integridad de datos en transmision y almacenamiento; firmas digitales u otros mecanismos de autenticacion de origen; integridad de metadatos asociados |
| **Disponibilidad de los Servicios** | Redundancia y contingencia; DRP para minimizar tiempo de inactividad; monitoreo proactivo de rendimiento y disponibilidad |
| **Videoconferencia Segura** | Protocolos seguros de acceso de usuario; cifrado robusto de video y voz; verificacion de integridad de datos en comunicacion de video/voz; protocolos de identificacion de origen y destino en enrutamiento de mensajes; servicios de registro y custodia segura de videoconferencias |
| **Almacenamiento Seguro de Datos** | Repositorios seguros con controles de acceso estrictos y cifrado; politicas de retencion y eliminacion segun normativa; copias de seguridad periodicas en ubicaciones seguras |
| **Gestion de Incidentes** | Plan de respuesta especifico para telemedicina; roles y responsabilidades definidos; monitoreo y alerta temprana |
| **Auditoria y Trazabilidad** | Registros de auditoria detallados en plataformas de telemedicina; auditorias periodicas de cumplimiento; conservacion de registros segun normativa |
| **Cumplimiento Normativo** | Ley 21.541, Norma Tecnica N°237, Ley 19.628, Ley 21.663 y regulaciones aplicables; actualizacion ante cambios normativos |

## 12. Innovacion y Tendencias en Ciberseguridad

| Linea de Accion | Acciones Especificas |
|---|---|
| **Deteccion y Respuesta Avanzada con IA y Automatizacion** | Implementar EDR/XDR con IA (analisis de comportamiento); evaluar plataformas SOAR para automatizacion de flujos de respuesta; aplicar Machine Learning para optimizar deteccion y reducir falsos positivos |
| **Ciberinteligencia Predictiva y Tactica (TI/CTI)** | Analisis de tendencias de amenazas y reportes sectoriales; plataformas CTI integradas con Threat Hunting; monitoreo y correlacion de IoCs de diversas fuentes; intercambio de informacion con otros Servicios de Salud y entidades relevantes |
| **Blockchain** | Evaluar viabilidad para integridad, trazabilidad y transparencia de datos clinicos y consentimientos informados; pruebas piloto para intercambio seguro de historiales clinicos; asegurar interoperabilidad con sistemas existentes |
| **Prevencion de Suplantacion Digital (Deepfakes y Phishing Avanzado)** | Mitigar riesgos de fraude multimedia; validacion biometrica y soluciones antifraude avanzadas; sensibilizacion sobre nuevas tacticas de phishing visual y de voz; monitoreo de deepfakes e imagen institucional |
| **Ciberinteligencia en Gestion de Amenazas** | Integrar fuentes de Threat Intelligence en monitoreo y analisis de riesgos; participar en comunidades de intercambio sectorial (grupos WSSP del sector salud, foros nacionales) |
| **Identidad Digital y Autenticacion Avanzada** | Fortalecer IAM para control granular; autenticacion sin contrasenas y adaptativa; roles y privilegios temporales con trazabilidad; federacion de identidad (SSO) entre instituciones de salud |
| **Zero Trust Architecture (ZTA)** | Estrategia gradual de implementacion; microsegmentacion en redes clinicas y administrativas; verificacion continua de dispositivos; politicas de acceso basadas en identidad, rol, ubicacion, dispositivo y sensibilidad de datos |
| **Seguridad en Entornos Multicloud y SaaS** | Herramientas CSPM, CWPP y CASB; requisitos minimos de seguridad para proveedores cloud (Ley 21.663, HIPAA) |
| **Proteccion de Tecnologias Operacionales (OT) y Dispositivos IoMT** | Inventario actualizado de activos OT/IoMT; redes segmentadas y aisladas; sistemas de deteccion de amenazas especificos para entornos industriales y medicos; NAC e IDS adaptados a IoMT; restriccion de conexiones de red innecesarias |
| **Resiliencia Cibernetica Institucional** | BCP y DRP con escenarios de ciberataques complejos (ransomware, DDoS); respaldo inmutable de datos; mecanismos de recuperacion orquestada |

## 13. Capacitacion y Concientizacion en Ciberseguridad

### 13.1. Plan de Capacitacion Anual

Cubre totalidad del personal (planta, contrata, honorarios, proveedores externos con acceso a sistemas institucionales). Niveles diferenciados:

| Nivel | Audiencia | Contenido |
|---|---|---|
| **Basico** | Usuarios Generales | Identificacion de amenazas comunes, practicas seguras en uso diario de tecnologias institucionales |
| **Intermedio** | Personal Tecnico No Especializado | Conceptos de seguridad profundizados, herramientas practicas para proteccion de sistemas y datos bajo su responsabilidad |
| **Avanzado** | Personal Tecnico Especializado | Gestion de vulnerabilidades, seguridad cloud, hardening, criptografia, SIEM, procedimientos avanzados de gestion de incidentes |
| **Directivo** | Alta Direccion | Gobernanza de ciberseguridad, gestion de riesgos ciberneticos, cumplimiento normativo (Ley 21.663, Ley 21.719, HIPAA), toma de decisiones estrategicas ante incidentes de alto impacto |

### 13.2. Modulos Tematicos Minimos

| Modulo | Contenido |
|---|---|
| Fundamentos de Seguridad de la Informacion y Proteccion de Datos Personales | Confidencialidad, integridad, disponibilidad; principios y normativas de proteccion de datos personales (Ley 19.628, Ley 21.719) |
| Uso Seguro de Tecnologias y Redes Institucionales | Equipos de escritorio, portatiles, dispositivos moviles, correo electronico, navegacion web, redes inalambricas, acceso remoto seguro |
| Gestion de Contrasenas y Autenticacion Segura | Contrasenas robustas, rotacion periodica, MFA obligatorio para sistemas criticos |
| Prevencion de Phishing, Ingenieria Social y Malware | Reconocimiento de tecnicas, medidas preventivas contra virus, ransomware, spyware |
| Normativa Vigente en Ciberseguridad y Privacidad | Leyes, decretos, politicas internas y externas aplicables |
| Procedimientos de Respuesta ante Incidentes | Protocolos de identificacion, reporte y respuesta inicial; canales de comunicacion con ANCI |

### 13.3. Capacitacion Especializada

#### Equipos Tecnicos (Avanzada y Practica)

| Area |
|---|
| Gestion integral de vulnerabilidades (identificacion, evaluacion, priorizacion, remediacion) |
| Seguridad en la nube (configuracion segura, IAM cloud, cumplimiento) |
| Endurecimiento (hardening) de SO, servidores, aplicaciones y dispositivos de red |
| Implementacion y gestion de soluciones de cifrado (transito y reposo) |
| Implementacion, configuracion y analisis de SIEM |
| Procedimientos avanzados de gestion y respuesta a incidentes complejos |

#### Directivos

| Area |
|---|
| Gobernanza de la ciberseguridad y rol en estrategia institucional |
| Gestion de riesgos ciberneticos (impacto financiero y reputacional) |
| Cumplimiento normativo e implicaciones legales de incidentes |
| Toma de decisiones estrategicas y comunicacion en incidentes de alto impacto |

### 13.4. Simulacros y Ejercicios

| Requisito |
|---|
| Al menos un ejercicio o simulacro de respuesta a incidentes por año |
| Involucrar usuarios clave de diferentes areas, personal tecnico y responsables de continuidad operativa |
| Escenarios realistas y relevantes para el Sector Salud (ransomware, filtracion de datos, DDoS) |
| Documentacion exhaustiva de resultados, fortalezas y debilidades; acciones de mejora continua |

### 13.5. Evaluacion y Seguimiento

| Actividad |
|---|
| Evaluaciones diagnosticas al inicio y pruebas de conocimiento al finalizar cada modulo |
| Registro centralizado de participacion y cumplimiento (requisito obligatorio) |
| Indicadores de desempeño y madurez para evaluar cultura de ciberseguridad |

### 13.6. Materiales y Canales de Difusion

| Formato |
|---|
| Sesiones presenciales, modulos de e-learning interactivos, capsulas informativas, newsletters periodicas, videos explicativos |
| Canales digitales internos: intranet, plataformas de colaboracion, correo electronico institucional |

### 13.7. Obligatoriedad

La participacion en capacitacion en ciberseguridad es de caracter **obligatorio** para todo el personal como parte integral de sus obligaciones laborales. El incumplimiento podra tener las implicaciones que defina la normativa interna. Se implementara un sistema formal y centralizado de registro de todas las actividades de formacion y concientizacion, disponible para auditorias internas y externas.

## 14. Arquitectura Referencial

| Directriz | Especificacion |
|---|---|
| Alineacion con la Estrategia Tecnologica | Sistemas diseñados conforme a objetivos estrategicos y tecnologicos del MINSAL |
| Uso de Estandares y Tecnologias Aprobadas | Desarrollos segun tecnologias, plataformas, metodologias y patrones de diseno de la arquitectura referencial ministerial |
| Revision y Aprobacion Arquitectonica | Cambios o excepciones evaluados por equipo de gobernanza tecnologica institucional |
| Reutilizacion y Modularidad | Diseno modular, reutilizacion de componentes para reducir redundancias |
| Documentacion Tecnica Obligatoria | Documentacion arquitectonica actualizada (estructura del sistema, modelo de datos, diagramas de componentes, integraciones, configuraciones clave) |

## 15. Interoperabilidad

| Directriz | Especificacion |
|---|---|
| Cumplimiento de Estandares HL7 | HL7 v2.x y HL7 FHIR (R4 o superiores); interoperabilidad semantica y tecnica |
| Protocolos y Formatos de Intercambio Seguros | HTTPS, SFTP, REST, GraphQL; formatos JSON o XML |
| Desarrollo de APIs Documentadas | APIs bien documentadas y estandarizadas; integracion funcional consistente, trazable y escalable |
| Compatibilidad con la Arquitectura Empresarial | Respetar capas tecnologicas, dominios funcionales y plataformas habilitadoras |
| Gestion de Datos Normalizados | Datos estructurados y normalizados conforme a catalogos, codigos y estandares del sector salud |
| Pruebas de Interoperabilidad | Obligatorias durante el ciclo de desarrollo: pruebas funcionales, de seguridad y de rendimiento |

## 16. Uso de Inteligencia Artificial (IA)

### Directrices de Cumplimiento Obligatorio

| Directriz | Especificacion |
|---|---|
| Auditabilidad y Explicabilidad | Algoritmos auditables y explicables; garantizar comprension de decisiones automatizadas que afecten procesos clinicos o administrativos |
| Cumplimiento Normativo | Ley 21.663 (Ciberseguridad), Ley 21.719 (Proteccion de Datos Personales), Ley 21.541 (Telemedicina), Circular N°711/2023 de SEGPRES (uso de IA en sector publico) |
| Evaluacion y Gestion de Riesgos | Identificar y mitigar riesgos de seguridad, privacidad, equidad y sesgo algoritmico mediante evaluaciones periodicas de impacto |
| Supervision y Revision de Resultados | Supervision continua de sistemas de IA; garantizar que resultados no sean discriminatorios ni generen impactos adversos |
| Derechos de los Usuarios | Permitir cuestionar, corregir o apelar decisiones de IA; facilitar ejercicio de derechos ARCO (Acceso, Rectificacion, Cancelacion, Oposicion) |
| Responsabilidad y Remediacion | Proveedor responsable de resultados generados; corregir fallas, vulnerabilidades o impactos negativos; asegurar continuidad y confianza |

### 16.1. Casos de Uso de la IA y Riesgos Asociados

| Caso de Uso | Riesgos Asociados |
|---|---|
| IA para el Diagnostico | Sesgo en algoritmos (diagnosticos erroneos, falta de deteccion de condiciones); falta de transparencia en toma de decisiones |
| IA para el Tratamiento | Errores en recomendaciones por calidad deficiente de datos o falta de validacion clinica; riesgo para la seguridad del paciente; toda recomendacion debe ser validada por expertos medicos antes de implementarse |
| IA para la Gestion de la Salud Publica | Uso indebido de datos personales; preocupaciones sobre privacidad; diseno debe garantizar uso etico y legal de informacion de pacientes |

### 16.2. Consideraciones de Seguridad y Privacidad

| Consideracion | Especificacion |
|---|---|
| Seguridad de datos para entrenamiento | Almacenamiento y procesamiento con maximos estandares de seguridad; cifrado y proteccion contra accesos no autorizados; entornos seguros de procesamiento; controles de acceso estrictos |
| Transparencia y explicabilidad | Mecanismos de trazabilidad y auditabilidad de algoritmos; resultados explicables a profesionales de la salud y pacientes |
| Privacidad de pacientes | Anonimizacion y pseudonimizacion antes de entrenar algoritmos; politicas de consentimiento explicito |
| Consideraciones eticas y legales | Alineacion con principios eticos de dignidad y derechos humanos; cumplimiento de leyes de proteccion de datos y privacidad vigentes |

## 17. Auditoria y Cumplimiento del SGSI

### 17.1. Tipos de Auditorias Recomendadas

| Tipo | Descripcion |
|---|---|
| Auditorias Internas | Realizadas por personal de la institucion; evaluar efectividad de controles y detectar areas de mejora |
| Auditorias Externas | Auditores independientes para evaluacion imparcial del SGSI |
| Auditorias de Cumplimiento | Verificar cumplimiento con regulaciones especificas (Ley 21.663 y normativas locales e internacionales) |

### 17.2. Frecuencia y Criterios de Seleccion de Auditores

| Aspecto | Especificacion |
|---|---|
| Frecuencia auditorias internas | Al menos una vez al año |
| Frecuencia auditorias externas y de cumplimiento | Cada dos años o segun regulaciones pertinentes |
| Auditores internos | Conocimientos en seguridad de la informacion, imparcialidad, formacion en auditoria |
| Auditores externos | Profesionales independientes con experiencia en sector salud y certificaciones adecuadas |
| Auditores de cumplimiento | Especializados en normativas aplicables |

## 18. Indicadores de Seguridad de la Informacion y Ciberseguridad

KPI y KRI con definicion clara, unidad de medida, frecuencia de evaluacion y responsable. Resultados presentados periodicamente al Comite de Seguridad de la Informacion y a la Alta Direccion; informar a ANCI cuando sea necesario.

### 18.1. Indicadores Clave de Desempeño e Indicadores Clave de Riesgo (Ejemplo)

| Categoria/Area | Nombre del Indicador | Objetivo | Formula/Medicion | Frecuencia | Meta | Umbral de Alerta | Responsable |
|---|---|---|---|---|---|---|---|
| **Capa Fisica / Acceso** | % de cumplimiento de normas de acceso fisico | Evaluar el cumplimiento de politicas de acceso a zonas criticas | (% de areas con cumplimiento de acceso fisico / total) x 100 | Mensual | 100% | <95% | Encargado de Infraestructura |
| **Seguridad Fisica** | N° de eventos de seguridad fisica | Detectar accesos no autorizados, robos o vandalismo | N° de eventos registrados | Mensual | 0 | >2 | Seguridad Fisica |
| **Capa Red / Firewall Perimetral** | % de intentos de intrusion bloqueados | Medir la eficacia de las barreras perimetrales | (% intentos bloqueados / total intentos) x 100 | Semanal | 99.9% | <99.5% | Admin Red |
| **SOC / IDS/IPS** | N° de alertas criticas del IDS/IPS | Supervisar anomalias y amenazas externas | N° de alertas criticas generadas | Diario | <5 | >20 | Encargado de SOC |
| **Arquitectura de Red** | % de segmentacion implementada | Evaluar cobertura de segmentacion | % de segmentos implementados | Trimestral | 100% | <90% | Arquitecto de Red |
| **Seguridad Interna** | N° de accesos indebidos entre segmentos | Controlar accesos no autorizados entre segmentos de red | N° de accesos indebidos registrados | Mensual | 0 | >3 | Encargado de Seguridad |
| **Capa Endpoints** | % de endpoints con software de antivirus/EDR actualizado | Verificar cobertura | (% endpoints con software actualizado / total) x 100 | Semanal | 98% | <95% | Soporte Tecnico |
| **EDR / SOC** | Detecciones de malware en endpoints | Monitorear infecciones en equipos de usuario | N° de infecciones confirmadas | Semanal | 0 | >5 | SOC Admin |
| **Capa de Aplicacion** | Vulnerabilidades criticas sin corregir | Identificar riesgos graves en software | N° de vulnerabilidades criticas abiertas >30 dias | Mensual | 0 | >2 | Desarrollo / Seguridad App |
| **Desarrollo / QA** | % de pruebas de seguridad superadas | Verificar calidad de seguridad en sistemas criticos | % de sistemas criticos con pruebas SAST/DAST superadas | Trimestral | 90% | <85% | QA/DevSecOps |
| **Capa de Datos** | % de bases de datos cifradas | Asegurar confidencialidad de datos sensibles | (% bases/archivos criticos cifrados / total) x 100 | Trimestral | 95% | <90% | DBA / Seguridad |
| **Datos** | N° de incidentes de fuga de datos | Controlar exposicion de datos | N° de incidentes validados | Anual | 0 | >0 | Responsable de Datos |
| **Capa Administrativa** | % de personal capacitado en seguridad | Asegurar conocimiento basico de ciberseguridad | (% personal capacitado / total) x 100 | Anual | 95% | <90% | RRHH / CISO |
| **Normativas Internas** | Incumplimientos de politicas | Monitorear violaciones a normativas | N° de violaciones documentadas | Mensual | 0 | >3 | Comite de Seguridad |
| **Gestion de IAM** | Cuentas inactivas/obsoletas | Prevenir accesos indebidos por cuentas obsoletas | % de cuentas inactivas detectadas y deshabilitadas | Mensual | 100% | <95% | Administrador IAM |
| **Gestion de Vulnerabilidades** | Tasa de vulnerabilidades criticas sin mitigar | Reducir exposicion prolongada a riesgos graves | (vulnerabilidades criticas sin mitigar (>30 dias) / total criticas) x 100 | Mensual | 0% | >5% | Encargado de Infraestructura |
| **Respuesta a Incidentes** | Tiempo de respuesta | Mejorar eficiencia en contener amenazas | Tiempo de respuesta / N° incidentes | Trimestral | <8h | >12h | CSIRT local |
| **SOC/SIEM** | Tiempo de deteccion | Reducir latencia desde ocurrencia hasta deteccion | Tiempo desde deteccion / N° incidentes | Mensual | <1h | >4h | SOC/SIEM Admin |
| **Cumplimiento Normativo** | % de cumplimiento normativo | Asegurar alineacion con leyes y estandares | (% controles implementados / controles requeridos) x 100 | Anual | 100% | <90% | Oficial de Cumplimiento |

Consideraciones:
- Tabla es ejemplo; adaptar indicadores a necesidades, activos criticos y riesgos de cada institucion
- Los indicadores deben ser relevantes para los objetivos de seguridad y prioridades organizacionales
- Deben ser cuantificables y faciles de medir
- Los resultados deben permitir toma de decisiones informadas y acciones correctivas
- Revision y ajuste periodico
- Considerar herramientas de gestion de seguridad (SIEM, paneles de control) para recopilacion, analisis y visualizacion

## 19. Mecanismo de Difusion

| Canal | URL/Medio |
|---|---|
| Sitio web MINSAL | http://www.minsal.cl/seguridad_de_la_informacion/ |
| Intranet MINSAL | http://isalud.minsal.cl/ |
| Correo informativo | Distribucion por correo electronico institucional |
