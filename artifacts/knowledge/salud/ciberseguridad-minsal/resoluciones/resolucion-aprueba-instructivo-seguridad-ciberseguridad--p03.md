---
_manifest:
  urn: urn:salud:kb:resolucion-aprueba-instructivo-seguridad-ciberseguridad-p03
  provenance:
    created_by: Codex
    created_at: '2026-06-05'
    source: Resolucion Exenta RES_853, MINSAL, 23 JUL 2025
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- resolucion
- acto-administrativo
lang: es
extensions:
  kora:
    family: note
    shard_index: 3
    shard_count: 4
    shard_root_urn: urn:salud:kb:resolucion-aprueba-instructivo-seguridad-ciberseguridad
relations:
  cites:
  - urn:salud:kb:politica-general-seguridad-informacion-ciberseguridad
---

# Resolucion Exenta RES_853 - Aprueba Instructivo de Seguridad de la Informacion y Ciberseguridad para el Sector Salud ITS-NC-007-V.2.0, Abril 2025 - Parte 03

## Ciberseguridad en Dispositivos Medicos loT

### Instrucciones de Seguridad para Dispositivos Medicos loT

| Instruccion | Especificacion |
| --- | --- |
| Inventario y gestion de activos | Inventario actualizado de todos los dispositivos loT conectados: ubicacion, fabricante, modelo, version de firmware, responsable |
| Segmentacion de red | VLANs y aislamiento fisico. ACLs y firewalls con reglas restrictivas. |
| Control de acceso y autenticacion | Mecanismos robustos. Deshabilitar credenciales de fabrica. Prohibir contrasenas debiles. MFA cuando sea posible. |
| Gestion de vulnerabilidades y actualizaciones | Proveedores deben entregar parches regulares y documentacion de pruebas de seguridad. Planificacion y prueba en entornos no productivos. Registro detallado. |
| Monitoreo y registro de actividades | Monitoreo continuo de comportamiento: accesos no autorizados, modificaciones de configuracion, trafico anomalo, IoCs. Logs detallados. |
| Cifrado de datos y comunicaciones | Extremo a extremo. TLS 1.2+ para comunicaciones, AES-256 para datos en reposo. |
| Pruebas de seguridad y evaluaciones de riesgo | Pentesting y evaluaciones antes de la puesta en operacion. Verificacion de interoperabilidad segura. |
| Cumplimiento normativo y contractual | Clausulas explicitas de ciberseguridad en contratos con proveedores. Concordancia con Ley N°21.663, Ley N°21.541. |
| Plan de contingencia y respuesta | Integracion de dispositivos loT en IRP y BCP/DRP. Procedimientos especificos para incidentes que afecten estos dispositivos. |

## Seguridad en Telemedicina

Conforme a Ley N°21.541 y Norma Tecnica N°237 del MINSAL.

### Controles de Seguridad para Telemedicina

| Control | Especificacion |
| --- | --- |
| Autenticacion robusta | MFA para todos los usuarios. Autenticacion biometrica cuando sea factible. |
| Autorizacion y control de acceso | RBAC y privilegios minimos. Gestion centralizada de cuentas. Bloqueo automatico por inactividad. |
| Confidencialidad | Cifrado extremo a extremo (TLS 1.2+). Proteccion en reposo y transito. Cumplimiento Ley N°19.628. |
| Integridad | Verificacion de integridad de datos. Firmas digitales. Integridad de metadatos. |
| Disponibilidad | Redundancia y contingencia. DRP. Monitoreo de rendimiento. |
| Videoconferencia segura | Protocolos seguros de acceso. Cifrado robusto de video/voz. Protocolos de identificacion de origen/destino. Registro y custodia segura de grabaciones. |
| Almacenamiento seguro | Repositorios seguros con control de acceso y cifrado. Politicas de retencion y eliminacion. Backups periodicos. |
| Gestion de incidentes | IRP especifico para telemedicina. Monitoreo y alerta temprana. |
| Auditoria y trazabilidad | Registros de auditoria detallados. Auditorias periodicas. Conservacion segun normativa. |
| Cumplimiento normativo | Ley N°21.541, Norma Tecnica N°237, Ley N°19.628, Ley N°21.663. |

## Innovacion y Tendencias en Ciberseguridad

Lineas de accion para fortalecimiento institucional:

| Linea de accion | Medidas |
| --- | --- |
| IA y automatizacion | EDR/XDR con IA, SOAR para automatizacion de flujos de respuesta, Machine Learning para optimizar deteccion |
| Ciberinteligencia predictiva (TI/CTI) | Analisis de tendencias, plataformas CTI para Threat Hunting, monitoreo y correlacion de IoCs, intercambio de informacion entre Servicios de Salud |
| Blockchain | Evaluar para integridad, trazabilidad y transparencia de datos clinicos y consentimientos. Pruebas piloto. Interoperabilidad segura. |
| Prevencion de suplantacion digital | Mitigacion de deepfakes, validacion biometrica y antifraude, sensibilizacion sobre phishing visual/voz, monitoreo de imagen institucional |
| Identidad digital y autenticacion avanzada | IAM fortalecido, autenticacion sin contrasenas y adaptativa, roles y privilegios temporales, SSO entre instituciones |
| Zero Trust Architecture (ZTA) | Estrategia gradual, microsegmentacion, monitoreo continuo, control de acceso basado en identidad y contexto |
| Seguridad multicloud y SaaS | CSPM, CWPP, CASB. Requisitos minimos de seguridad para proveedores cloud. |
| Proteccion OT y loMT | Inventario y segmentacion, deteccion de amenazas especifica, NAC e IDS para loMT, restriccion de conexiones innecesarias |
| Resiliencia cibernetica | BCP/DRP probados para ciberataques (ransomware, DDoS), respaldo inmutable, recuperacion orquestada |

## Capacitacion y Concientizacion en Ciberseguridad

### Plan de Capacitacion Anual

El Area de Seguridad de la Informacion, en colaboracion con la Direccion y RRHH, elaborara un Plan Anual de Capacitacion en Ciberseguridad para todo el personal (planta, contrata, honorarios) y proveedores externos con acceso a sistemas institucionales.

**Niveles de profundidad**:

| Nivel | Audiencia | Contenido |
| --- | --- | --- |
| Basico | Usuarios generales | Amenazas comunes, practicas seguras diarias |
| Intermedio | Personal tecnico no especializado | Conceptos de seguridad, herramientas practicas de proteccion |
| Avanzado | Personal tecnico especializado | Gestion de vulnerabilidades, seguridad cloud, hardening, criptografia, SIEM, gestion avanzada de incidentes |
| Directivo | Alta direccion | Gobierno de ciberseguridad, gestion de riesgos, cumplimiento normativo, toma de decisiones ante incidentes |

### Modulos Tematicos Minimos

1. Fundamentos de Seguridad de la Informacion y Proteccion de Datos Personales (Ley N°19.628 y Ley N°21.719).
2. Uso Seguro de Tecnologias y Redes Institucionales.
3. Gestion de Contrasenas y Autenticacion Segura (MFA obligatorio para sistemas criticos).
4. Prevencion de Phishing, Ingenieria Social y Malware.
5. Normativa Vigente en Ciberseguridad y Privacidad.
6. Procedimientos de Respuesta ante Incidentes (incluyendo canales ANCI).

### Capacitacion Especializada

**Equipos tecnicos**: gestion de vulnerabilidades, seguridad cloud, hardening, cifrado, SIEM, respuesta avanzada a incidentes.

**Directivos**: gobernanza, gestion de riesgos, cumplimiento normativo, toma de decisiones estrategicas ante incidentes de alto impacto.

### Simulacros y Ejercicios

- Al menos un ejercicio o simulacro de respuesta a incidentes por ano.
- Involucrar usuarios clave, personal tecnico y responsables de continuidad operativa.
- Escenarios realistas para el Sector Salud (ransomware, filtracion de datos, DDoS).
- Documentacion exhaustiva y acciones de mejora continua.

### Evaluacion y Seguimiento

- Evaluaciones pre y post capacitacion.
- Registro centralizado de participacion. Cumplimiento obligatorio.
- Indicadores de desempeno y madurez de cultura de ciberseguridad.

### Materiales y Difusion

Formatos diversos: sesiones presenciales, e-learning, capsulas informativas, newsletters, videos. Canales: intranet, plataformas de colaboracion, correo institucional.

### Obligatoriedad

Participacion obligatoria para todo el personal. Incumplimiento con implicaciones segun normativa interna. Sistema formal de registro disponible para auditorias.

## Arquitectura Referencial

Todo sistema del Sector Salud debe alinearse con la Arquitectura Referencial Ministerial:

- Alineacion con la estrategia tecnologica del MINSAL.
- Uso de estandares, tecnologias, metodologias y patrones de diseno aprobados.
- Revision y aprobacion arquitectonica para cambios o excepciones.
- Diseno modular y reutilizacion de componentes.
- Documentacion tecnica obligatoria actualizada (estructura, modelo de datos, diagramas, integraciones).

## Interoperabilidad

- Cumplimiento de estandares HL7: HL7 v2.x y HL7 FHIR (R4 o superiores).
- Protocolos estandarizados: HTTPS, SFTP, REST, GraphQL. Formatos: JSON, XML.
- APIs bien documentadas y estandarizadas.
- Compatibilidad con la arquitectura empresarial institucional.
- Datos normalizados conforme a catalogos, codigos y estandares del sector.
- Pruebas de interoperabilidad obligatorias (funcionales, de seguridad, de rendimiento).

## Uso de Inteligencia Artificial (IA)

### Directrices obligatorias

| Directriz | Especificacion |
| --- | --- |
| Auditabilidad y explicabilidad | Algoritmos auditables y explicables. Decisiones automatizadas comprensibles ante requerimiento. |
| Cumplimiento normativo | Ley N°21.663, Ley N°21.719, Ley N°21.541, Circular N°711/2023 SEGPRES. |
| Evaluacion y gestion de riesgos | Identificar y mitigar riesgos de seguridad, privacidad, equidad y sesgo algoritmico. Evaluaciones periodicas de impacto. |
| Supervision de resultados | Mecanismos de supervision continua. Resultados no discriminatorios ni adversos. |
| Derechos de los usuarios | Cuestionar, corregir o apelar decisiones automatizadas. Ejercicio de derechos ARCO. |
| Responsabilidad y remediacion | Proveedor responsable de resultados. Correccion de fallas, vulnerabilidades e impactos negativos. |

### Casos de uso y riesgos

| Caso de uso | Riesgos |
| --- | --- |
| IA para diagnostico | Sesgo algoritmico, falta de transparencia |
| IA para tratamiento | Errores por datos deficientes, falta de validacion clinica |
| IA para gestion de salud publica | Uso indebido de datos personales, privacidad |

### Seguridad y privacidad en IA

- Datos de entrenamiento con cifrado y control de acceso estricto.
- Mecanismos de trazabilidad y auditabilidad de algoritmos.
- Anonimizacion y seudonimizacion de datos de pacientes.
- Alineacion con principios eticos y legales de proteccion de datos.

## Auditoria y Cumplimiento del SGSI

### Tipos de Auditorias

| Tipo | Descripcion |
| --- | --- |
| Auditorias internas | Personal de la institucion. Evaluar efectividad de controles y areas de mejora. |
| Auditorias externas | Auditores independientes. Evaluacion imparcial del SGSI. |
| Auditorias de cumplimiento | Verificar cumplimiento con Ley N°21.663 y otras normativas. |

### Frecuencia y Seleccion

- Auditorias internas: al menos una vez al ano.
- Auditorias externas y de cumplimiento: cada dos anos o segun regulaciones.
- Auditores internos: conocimiento en seguridad de la informacion, imparcialidad, formacion en auditoria.
- Auditores externos: independientes, experiencia en sector salud, certificaciones adecuadas.
- Auditores de cumplimiento: especializados en normativas aplicables.

## Indicadores de Seguridad (KPI/KRI)

Cada institucion debe establecer KPI y KRI con: definicion clara, unidad de medida, frecuencia de evaluacion y responsable. Resultados presentados al Comite de Seguridad y a la Alta Direccion. Cuando corresponda, informar a la ANCI.

Areas de indicadores (ejemplos en Anexo 21.6):
- Seguridad fisica, red, endpoints, aplicacion, datos, administrativa.
- Gestion de vulnerabilidades, respuesta a incidentes.
- Cumplimiento normativo.

## Mecanismo de Difusion

- Sitio web MINSAL: http://www.minsal.cl/seguridad_de_la_informacion/
- Intranet MINSAL: http://isalud.minsal.cl/
- Correo informativo.

## Control de Versiones

| Version | Fecha | Cambios |
| --- | --- | --- |
| 2.0 | Abril 2025 | Adaptacion normativa nacional e internacional en materia de Seguridad de la Informacion y Ciberseguridad |

## Anexos

### Definiciones y Terminos Clave

- **Activos de informacion**: toda informacion o recurso para su creacion, almacenamiento, gestion o transmision. Materiales (RRHH, equipos, redes, instalaciones) o intangibles (datos, aplicaciones, sistemas operativos, imagen, reputacion).
- **Activo informatico**: informacion almacenada en red y sistema informatico con valor para una persona u organizacion.
- **Autenticacion**: propiedad que da cuenta del origen legitimo de la informacion.
- **Anonimizacion**: procedimiento irreversible que impide vincular un dato personal a una persona determinada.
- **ANCI**: Agencia Nacional de Ciberseguridad.
- **Auditorias de seguridad**: procesos de control para revisar cumplimiento de politicas y procedimientos del SGSI.
- **Seudonimizacion**: tratamiento de datos personales que impide su atribucion sin informacion adicional de reidentificacion, almacenada separadamente.
- **Ciberespacio**: ambiente complejo soportado por hardware y redes de comunicaciones (ISO 27032).
- **Ciberataque**: accion para destruir, exponer, alterar, deshabilitar, exfiltrar u obtener acceso no autorizado a un activo informatico.
- **Ciberseguridad**: preservacion de confidencialidad, integridad, disponibilidad y resiliencia de redes y sistemas informaticos.
- **Incidente de ciberseguridad**: evento que perjudique o comprometa la confidencialidad, integridad, disponibilidad o resiliencia de redes y sistemas, o la autenticacion de procesos.
- **Confidencialidad**: la informacion no es accedida por individuos, entidades o procesos no autorizados.
- **Continuidad de servicios**: capacidad de mantener disponibilidad de servicios, reduciendo riesgo de interrupcion y propiciando recuperacion.
- **Disponibilidad**: la informacion es accesible y utilizable cuando es requerida por una entidad autorizada.
- **Datos personales**: informacion concerniente a personas naturales, identificadas o identificables.
- **Datos sensibles**: datos sobre caracteristicas fisicas o morales, vida privada o intimidad. La Ley N°21.719 (vigente 01-DIC-2026) redefine: origen etnico/racial, afiliacion politica/sindical/gremial, situacion socioeconomica, convicciones ideologicas/filosoficas, creencias religiosas, datos de salud, perfil biologico, datos biometricos, vida sexual, orientacion sexual e identidad de genero.
- **CSIRT**: centros multidisciplinarios para prevenir, detectar, gestionar y responder a incidentes de ciberseguridad.
- **Gestion de incidentes**: procedimientos para deteccion, analisis, manejo, contencion y resolucion de un incidente.
- **Incidente**: evento inesperado con consecuencias en detrimento de la seguridad de redes, equipos y sistemas de informacion.
- **Infraestructura critica**: instalaciones, sistemas, redes y servicios cuya afectacion cause grave dano a la salud, abastecimiento, actividad economica, medioambiente o seguridad del pais.
- **Integridad**: la informacion no ha sido modificada o destruida sin autorizacion.
- **Nube privada**: infraestructura de nube para uso exclusivo de una unica organizacion.
- **Nube publica**: infraestructura disponible al publico general a traves de Internet.
- **Proteccion de activos de informacion**: medidas que resguarden la seguridad fisica de dispositivos y accesos.
- **Red y sistema informatico**: dispositivos, cables, enlaces, enrutadores u otros equipos que almacenen, procesen o transmitan datos digitales.
- **Resiliencia**: capacidad de redes y sistemas para seguir operando tras un incidente y recuperar sus funciones.
- **Riesgo**: posibilidad de ocurrencia de un incidente. Magnitud cuantificada por probabilidad e impacto.
- **Seguridad de la informacion**: medidas preventivas y reactivas para resguardar y proteger la informacion, asegurando confidencialidad, integridad, autenticidad y disponibilidad, continuidad de servicios y proteccion de activos.
- **Tratamiento de datos**: cualquier operacion automatizada o no que permita recolectar, procesar, almacenar, comunicar, transmitir o utilizar datos personales.
- **Vulnerabilidad**: debilidad de un activo o control explotable por amenazas.

## Normativa sobre Seguridad de la Informacion

#### Normativa del Sector Salud

- DFL N°1/2005 MINSAL: texto refundido DL N°2763/1979 + Leyes N°18.933 y N°18.469.
- DFL N°725 MINSAL: Codigo Sanitario.
- Ley N°19.966/2004: regimen de garantias de salud (AUGE/GES).
- Ley N°19.650: perfecciona normas del area de la salud.
- Ley N°20.120/2006: investigacion cientifica en ser humano, genoma, prohibicion de clonacion humana.
- Ley N°20.584: Deberes y Derechos de las Personas en Atencion de Salud.
- Ley N°20.724/2014: modifica Codigo Sanitario en regulacion de medicamentos.
- Ley N°20.850/2016: sistema de proteccion financiera para diagnosticos y tratamientos de alto costo (Ley Ricarte Soto).
- Ley N°21.258/2020: Ley Nacional del Cancer (Ley Claudio Mora).
- Ley N°21.541/2023: autoriza atenciones mediante telemedicina.
- Decreto N°41/2012 MINSAL: Reglamento de Ficha Clinica.
- Decreto N°31/2012 MINSAL: Reglamento sobre entrega de informacion y consentimiento informado.
- Decreto N°38/2005 MINSAL: Reglamento Organico de establecimientos de salud de menor complejidad y de autogestion.
- Decreto N°38/2012 MINSAL: Reglamento sobre derechos y deberes de las personas en atencion de salud.
- Decreto N°38/2013 MINSAL: modifica Reglamento de Farmacias, Droguerias, etc.
- Decreto N°6/2021 MINSAL: Reglamento sobre acciones de atencion de salud a distancia.
- Decreto N°820/2011 MINSAL.

#### Normativa de Documentos Electronicos

- Ley N°19.880/2003: bases de los procedimientos administrativos.
- Ley N°21.180: Transformacion Digital del Estado.
- Ley N°19.799/2002: firmas y documentos electronicos.
- Decreto N°181: Reglamento de Ley N°19.799.
- DS N°83/2005 SEGPRES. Decreto N°14/2014 SEGPRES. Decreto N°1/2015 SEGPRES.
- Decreto N°4/2021 SEGPRES: Reglamento de procedimientos administrativos por medios electronicos (Ley N°21.180).
- Decreto N°24/2019 Economia: norma tecnica para servicio de certificacion de firma electronica avanzada.
- Decreto N°1/2015 SEGPRES: norma tecnica sobre sistemas y sitios web de los organos de la administracion del Estado.

#### Normativa de Seguridad de la Informacion

- Ley N°21.663: Marco de Ciberseguridad.
- Decreto N°295/2024 Interior: Reglamento de Reporte de Incidentes de Ciberseguridad.
- Decreto N°483/2024 Interior: Estructura Interna de la ANCI.
- Decreto N°164/2023 Interior: Politica Nacional de Ciberseguridad 2023-2028.
- DS N°7/2023 SEGPRES: Norma Tecnica de Seguridad de la Informacion y Ciberseguridad (Ley N°21.180).
- DS N°83/2005 SEGPRES: Norma Tecnica sobre seguridad y confidencialidad de documentos electronicos.
- Decreto N°273/2022 Interior: obligacion de reportar incidentes de ciberseguridad.
- Circular N°711/2023 SEGPRES: lineamientos sobre uso de IA en el sector publico.
- RE N°372/2025 y Oficio N°7286/2025: Recomendaciones del Consejo para la Transparencia sobre Transparencia Algoritmica.

#### Normativa de Proteccion de Datos Personales

- Art. 19 N°1 y N°4 Constitucion Politica.
- Ley N°19.628/1999: Proteccion de la Vida Privada. Define dato personal, dato sensible y condiciones de tratamiento.
- Ley N°21.719/2024: modifica Ley N°19.628. Nuevo nombre: "Ley de Proteccion de Datos Personales". Vigente 01-DIC-2026.
- Ley N°20.575: principio de finalidad en tratamiento de datos personales.
- Decreto N°779/2000: Reglamento del Registro de Bancos de Datos Personales de organismos publicos.
- RE N°489/2022 Consejo para la Transparencia: procedimiento para ejercicio de derechos Ley N°19.628.

#### Normativa de Delitos Informaticos

- Ley N°21.459/2022: delitos informaticos, deroga Ley N°19.223, adecua al Convenio de Budapest.
- Ley N°20.009: clonacion de tarjetas de credito.
- Decreto N°83/2017: promulga Convenio de Budapest en Chile.

#### Normativa de Propiedad Intelectual

- Ley N°19.039: Propiedad Industrial.
- Ley N°17.336: Propiedad Intelectual. Proteccion de programas computacionales.

#### Normas de Aplicacion General

- Ley N°21.542: modificacion constitucional para proteccion de infraestructura critica por FFAA.
- Ley N°21.180: Transformacion Digital del Estado.
- Ley N°19.880: bases de procedimientos administrativos.
- Ley N°20.285: transparencia y acceso a la informacion publica.
- Ley N°19.886: compras publicas.
- Decreto N°661: Reglamento de Ley N°19.886.
- RE N°619-B/2018 Direccion de Compras y Contratacion Publica.
