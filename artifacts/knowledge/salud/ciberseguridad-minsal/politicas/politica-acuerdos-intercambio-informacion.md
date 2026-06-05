---
_manifest:
  urn: urn:salud:kb:politica-acuerdos-intercambio-informacion
  provenance:
    created_by: Codex via koraficacion
    created_at: '2026-06-05'
    source: MINSAL Chile, SGSI Nivel Central. PS-NC-014 v03, Diciembre 2024
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
    shard_root_urn: urn:salud:kb:politica-acuerdos-intercambio-informacion
  salud:
    minsal_id: PS-NC-014
    minsal_version: '03'
relations:
  cites:
  - urn:salud:kb:politica-general-seguridad-informacion-ciberseguridad
---

# Politica de Acuerdos de Intercambio de Informacion

**PS-NC-014 v03, Diciembre 2024. TLP:BLANCO.**

## Proposito y alcance

Establece directrices para garantizar proteccion y seguridad en el intercambio de informacion sensible entre MINSAL y organizaciones externas. Cubre cuatro aspectos:

1. Servicios de red utilizados para transmision de informacion.
2. Procedimientos para la transferencia de datos entre las partes.
3. Contenido minimo de los acuerdos que regulan condiciones del intercambio.
4. Compromisos de confidencialidad que aseguren proteccion de datos sensibles.

Alcance:

- Informacion fisica y electronica en sistemas MINSAL Nivel Central (SSP y SRA) que requiera entrega a entidades externas.
- Modalidades: acuerdos de interoperabilidad entre sistemas; intercambio via correo, Internet, login a otros sistemas, medios magneticos, papel u otros medios.
- Aplica a todos los funcionarios (planta, contrata, reemplazos, suplencia), personal a honorarios y terceros (proveedores, servicios).

Dominios ISO 27001:2022 cubiertos:

| ID Control | Nombre del Control |
|---|---|
| A.08.21 | Seguridad de los servicios de red |
| A.05.14 | Transferencia de Informacion |
| A.06.06 | Acuerdos de confidencialidad o no divulgacion |

## Marco normativo y documentos relacionados

Normas base:

- NCh-ISO27001:2022 — Seguridad de la informacion, ciberseguridad y proteccion de la privacidad — Requisitos SGSI.
- Marco Juridico SSI publicado en portal CSIRT del Ministerio del Interior.
- Documentos SGSI disponibles en isalud.minsal.cl.

Leyes y decretos aplicables:

| Norma | Materia |
|---|---|
| DFL 1/2006 | Texto refundido DL 2.763/1979 y Leyes 18.933 y 18.469. |
| Ley 19.650 | Normas del area de la salud. |
| Ley 19.966 | Regimen de Garantias Explicitas en Salud (AUGE/GES). |
| Ley 19.628 | Proteccion de la vida privada. |
| Ley 20.285/2008 | Acceso a la informacion publica. |
| Ley 20.584/2012 | Derechos y deberes vinculados a atencion en salud. |
| Ley 20.120/2006 | Investigacion cientifica en ser humano. |
| Ley 21.180 | Transformacion Digital del Estado. |
| Ley 20.724/2014 | Regulacion de farmacias y medicamentos. |
| Ley 21.541/2023 | Telemedicina. |
| Ley 21.668 | Interoperabilidad de fichas clinicas. |
| Ley 21.459 | Delitos informaticos (deroga 19.223, adecua a Convenio de Budapest). |
| Ley 21.663 | Marco de Ciberseguridad (OIV). |
| Decreto 41/2012 | Reglamento sobre fichas clinicas. |
| Decreto 533/2015 | Marco regulatorio ciberseguridad para instituciones publicas. |
| Decreto 6/2021 | Atencion de salud realizada a distancia. |
| Decreto 273/2022 | Obligacion de reportar incidentes de ciberseguridad al CSIRT. |
| Decreto 285/2025 | Procedimiento de calificacion OIV (Ley 21.663). |
| Decreto 295/2025 | Reglamento de Reporte de Incidentes (Ley 21.663). |
| Decreto 7/2025 | Taxonomia de Incidentes de Ciberseguridad. |
| DFL 29/2005 | Estatuto Administrativo. |
| DFL 1/19653 | Bases Generales de la Administracion del Estado. |
| DS 7/2023 | Norma Tecnica de Seguridad de la Informacion y Ciberseguridad (Ley 21.180). |
| DE 51/2024 | Norma general tecnica N° 237 — Estandares de telemedicina. |
| RE 7/2025 | Taxonomia de incidentes (Agencia Nacional de Ciberseguridad). |
| RE 2/2025 | Publicidad de alertas tempranas y avisos de ciberseguridad. |
| Circular 711/2023 | Lineamientos sobre uso de IA en sector publico. |

## Roles y responsabilidades

| Rol | Responsabilidades |
|---|---|
| Departamento TIC | Definir y establecer mecanismos de control para entrega e intercambio de informacion electronica con entidades externas (confidencialidad, integridad, disponibilidad). Implementar tecnologias de seguridad (encriptacion, firma digital, VPNs) conforme a riesgos. Establecer acuerdos y protocolos de seguridad con terceros. |
| Encargado de Seguridad de la Informacion | Auditar cumplimiento de la politica (revisiones periodicas, analisis de riesgos). Gestionar incidentes de seguridad relacionados con intercambios. Velar por correcta aplicacion, revision y actualizacion de medidas de proteccion. |
| Propietario de la informacion | Autorizar o rechazar intercambios bajo su responsabilidad. Aplicar medidas de proteccion incluyendo clasificacion y etiquetado. Supervisar y revisar intercambios, tomar medidas correctivas. Mantener registros detallados de intercambios (trazabilidad y auditabilidad). Garantizar seguridad al termino de convenios: retorno o destruccion segura de datos en soportes originales o copias en sistemas del destinatario. |
| Usuarios | Cumplir con la politica usando herramientas y procedimientos seguros. Reportar incidentes por canales establecidos. No divulgar informacion sensible fuera de canales autorizados. Participar en formacion continua sobre seguridad e intercambio seguro. |

## Consideraciones generales

Todo intercambio de informacion MINSAL con terceros debe respaldarse con acuerdo de transferencia (Terminos y Condiciones Generales o Convenios de Cooperacion) que incluya clausula de confidencialidad y/o no divulgacion.

El intercambio puede originarse por necesidad del Ministerio o requerimiento externo. En todos los casos debe analizarse la autorizacion legal que faculte al Ministerio para comunicar la informacion y al requirente para tratarla.

Los terminos y condiciones deben elaborarse segun la normativa aplicable a cada tipo de informacion y competencias legales de emisor y receptor.

La operatividad del instrumento corresponde a los departamentos o areas tecnicas responsables del Ministerio.

## Seguridad de los servicios de red

En cualquier acuerdo sobre servicios de red, el Departamento TIC debe garantizar mecanismos de seguridad robustos que definan:

- Niveles de servicio.
- Requisitos de administracion.
- Acuerdos de confidencialidad.
- Derechos de auditoria.

Estos elementos deben monitorearse y verificarse periodicamente.

Controles tecnicos obligatorios:

- VPN para conexiones entre organizaciones.
- Firewalls que bloqueen intentos no autorizados.
- IDS/IPS para identificar y evitar ataques en tiempo real.
- Alineacion con estandares de seguridad MINSAL.
- Auditoria regular de cumplimiento.

## Acuerdos de transferencia de informacion — contenidos minimos

Contenidos minimos requeridos:

#### Licitud de la transferencia

| Elemento | Requisito |
|---|---|
| Competencias legales del emisor | Declarar normas que habilitan para generar y comunicar la informacion a terceros. |
| Atribuciones legales del receptor | Declarar atribuciones legales o interes legitimo para acceder a la informacion. |
| Finalidad | Usos o finalidad a la que se destinara la informacion. |
| Transferencia ulterior | Antecedentes que identifiquen destinatarios finales, si se preve transferencia a terceros. |

#### Detalles de la informacion transferida

| Elemento | Requisito |
|---|---|
| Tipo de informacion | Identificacion del tipo de datos objeto de transferencia. |
| Condiciones de seguridad | Especificacion por categoria para garantizar integridad, confidencialidad y disponibilidad. |
| Origen de los datos | Si proviene de fuente de acceso publico o privado. |

#### Responsabilidades de las partes

Definir si el receptor tendra caracter de mandatario/procesador de datos o si adquirira condicion de responsable del tratamiento al acceder a la informacion. Si el receptor es proveedor de servicios, consignar detalladamente las instrucciones de tratamiento de datos encargados.

#### Antecedentes asociados a los datos

| Elemento | Requisito |
|---|---|
| Tipo de datos | Especificar si es informacion publica o privada, datos personales o datos sensibles. |
| Datos sensibles y confidenciales | Prohibicion de uso fuera de la finalidad legitima acordada. Deber de no divulgacion. |
| Datos de terceros titulares | Verificar si las competencias legales del requirente habilitan tratamiento sin consentimiento del titular o, en caso contrario, exigir acreditacion de consentimiento. |
| Divulgacion post-vigencia | Especificar acciones y obligaciones para evitar divulgacion no autorizada durante y despues de la vigencia del acuerdo. |

#### Finalidad legitima informada

| Elemento | Requisito |
|---|---|
| Declaracion de finalidades | Finalidades legitimas y compromiso de uso consistente con dicha declaracion. |
| Condicion esencial | El cumplimiento de la finalidad es condicion esencial del acuerdo; su incumplimiento faculta al MINSAL para terminacion inmediata. |
| Datos sensibles | Detallar usos permitidos, sujetos autorizados. Prohibir cualquier uso no autorizado o ajeno a lo estipulado. Su incumplimiento se considera infraccion a condicion esencial. |

#### Calidad de datos y procesos

| Elemento | Requisito |
|---|---|
| Estandares de calidad | Definir y asignar responsabilidades por calidad de informacion transferida. |
| Desidentificacion | Consignar si datos se transferiran nominados o con desidentificacion (anonimizacion) o enmascaramiento (seudonimizacion). |
| Auditoria de anonimizacion/seudonimizacion | Prever mecanismos de auditoria de procesos que verifiquen el cumplimiento. |
| Trazabilidad | Estandares de calidad de procesos que garanticen trazabilidad de flujos durante todo el ciclo del dato, desde originadores hasta destinatarios finales, asegurando auditabilidad. |

#### Condiciones de seguridad de la informacion

Todo acuerdo debe incluir adhesion de los participantes al SGSI MINSAL vigente durante toda la vigencia del acuerdo, mas las siguientes condiciones minimas:

| Condicion | Detalle |
|---|---|
| Trazabilidad y no repudio | Procedimientos que permitan seguimiento detallado del proceso desde origen hasta destino, garantizando que ninguna parte pueda negar envio o recepcion. |
| Derecho de auditoria | MINSAL puede auditar y monitorear actividades relacionadas con manejo de informacion confidencial. |
| Etiquetado TLP | Sistema de etiquetado basado en Traffic Light Protocol para informacion sensible o critica. |
| Normas tecnicas de transmision | Empaquetado, cifrado y transmision de datos. Compresion y cifrado de bases de datos con AES-256. Protocolos HTTPS, SFTP, TCP/IP protegidos con TLS 1.2 o superior. |
| Autenticacion e integridad | Autenticacion mutua mediante certificados digitales. Verificacion de integridad via hash SHA-256 antes del procesamiento. |
| Notificacion de incidentes | Procedimientos especificos para notificacion e informe inmediato de accesos indebidos, divulgacion no autorizada o fuga de informacion. |
| Canal seguro para reidentificacion | Si la transferencia incluye datos seudonimizados, prever canal seguro para comunicacion que permita reidentificacion. |
| Cadena de custodia en transito | Garantias para almacenamiento y deposito durante la transferencia. Medios que aseguren cadena de custodia clara y trazable desde origen hasta destino. |
| Control de acceso en transferencia | SFTP, limitaciones de privilegios por roles, MFA, registro de actividades y tiempo determinado de disponibilidad de la informacion. |

#### Propiedad y retencion de la informacion

| Elemento | Requisito |
|---|---|
| Regimen de propiedad | Regular expresamente propiedad de la informacion y restricciones de divulgacion. Especificar si hay secretos comerciales, industriales o derechos de propiedad intelectual. |
| Productos derivados | Regular si los productos elaborados con la informacion estaran sujetos a regimen de propiedad especifico o arbitrio del receptor. |
| Finalizacion del acuerdo | Detallar medidas de devolucion o destruccion de informacion confidencial con eliminacion segura y verificable, o facultad de retencion si el receptor esta autorizado. |

#### Responsabilidad

| Elemento | Detalle |
|---|---|
| Resguardos especificos | Acciones correctivas, sanciones y medidas legales ante incumplimiento, incluyendo penalizaciones economicas o acciones judiciales. |
| Responsabilidad del originador | Calidad de los datos, procedimientos de acceso y calificacion sobre competencias legales del requirente. |
| Responsabilidad del receptor | Uso posterior de los datos y cumplimiento de obligaciones de confidencialidad. |

#### Revision de los acuerdos

Revision al menos anual para verificar adecuacion a normativa vigente y politicas de seguridad de la informacion del MINSAL.

## Politicas y procedimientos de transferencia

#### Directrices generales

| Regla | Detalle |
|---|---|
| Diversidad de canales | Correo electronico, llamadas de voz, videoconferencias y otras formas de intercambio electronico. |
| Estandares de seguridad | Cualquiera sea la modalidad, cumplir estandares para tratamiento de datos sensibles y proteccion de confidencialidad e integridad. |
| Proteccion anti-malware | Seguir directrices del Procedimiento contra codigo malicioso del MINSAL: verificaciones de seguridad previas, escaneo de virus y malware antes de transferencia. |
| Adhesion al SGSI | Todo servicio o acuerdo debe adherirse a terminos del SGSI MINSAL para trazabilidad, no repudio y proteccion contra interceptacion, acceso no autorizado, copia, modificacion, enrutamiento incorrecto, destruccion o denegacion de servicio. |
| Control de acceso | Implementar niveles adecuados para que solo personas autorizadas accedan durante la transferencia. |
| Conversaciones confidenciales | No realizarse en espacios publicos, oficinas abiertas o ambientes inseguros, ni por canales sin encriptacion o control de accesos. Usar plataformas seguras y comunicaciones cifradas. |

#### Intercambio Manual

| Regla | Detalle |
|---|---|
| Correo certificado | Usar solo servicios de correos autorizados en MINSAL, en forma certificada. |
| Entrega en mano | Personal al destinatario, en sobre sellado, con registro de entrega. |
| Soportes protegidos | Encriptacion o claves, con entrega de claves por medios seguros. |

#### Intercambio via correo electronico institucional

| Regla | Detalle |
|---|---|
| Responsabilidad del emisor | Verificar que el destinatario tenga atribuciones para acceder a la informacion. Incluir encriptacion o clave a archivos con informacion confidencial. |
| Entrega de claves | Por canal seguro, preferencia presencial o llamada telefonica cifrada (canal distinto al del envio del archivo). |
| Estandares de encriptacion | Cumplir con estandares de seguridad aprobados por el Ministerio. La encriptacion debe proteger tanto en transito como en recepcion. |
| Pie de pagina obligatorio | Todo correo enviado desde el Ministerio debe incluir advertencia sobre uso y autorizaciones necesarias para tratamiento. Informacion sensible: aplicar TLP. Especificar que la informacion es confidencial y solo para destinatario autorizado. |
| Responsabilidad del receptor | Proteccion y uso adecuado de la informacion recibida. |
| Prohibicion de reenvio automatico | No reenviar automaticamente correos a direcciones externas. |
| Reenvio manual | Solo con analisis previo de riesgos y cumpliendo politicas de seguridad y privacidad. |

#### Interoperacion entre sistemas

Requisitos para implementar interoperabilidad:

| Requisito | Detalle |
|---|---|
| Identificacion de sistemas | Especificar plataformas, aplicaciones y herramientas conectadas, asegurando infraestructura compatible con estandares de seguridad. |
| Procedimiento de intercambio | Definir procedimientos para transferencia, integridad y proteccion, incluyendo gestion de incidentes. |
| Costos | Asignar y distribuir costos de implementacion y mantenimiento. |
| Responsabilidades | Asignar claramente a cada parte sobre manejo de informacion y seguridad de sistemas. |
| Estandares de seguridad | Implementar y mantener durante la interoperacion, protegiendo contra accesos no autorizados, modificaciones o perdida de datos. |
| Normas tecnicas | Establecer para registro, almacenamiento y lectura de informacion o software, garantizando compatibilidad y seguridad. |

## Restricciones y prohibiciones

Prohibido el intercambio de informacion sensible a traves de telefonos o mensajeria electronica (incluyendo aplicaciones de mensajeria instantanea). Estos medios no proporcionan niveles adecuados de seguridad para proteger confidencialidad e integridad.

## Mecanismo de difusion

Contenido accesible y comprensible para todos los usuarios. Canales minimos:

- Publicacion en intranet: http://isalud.minsal.cl/
- Correo informativo.
- Publicacion en sitio web: http://www.minsal.cl/seguridad_de_la_informacion/

## Periodo de revision y excepciones

- Revision cada dos anos o cuando ocurran cambios significativos que afecten tecnologia, legislacion, estandares internacionales o mejores practicas.
- Excepciones: el Jefe de Departamento TIC, el CISO o el Comite de Seguridad de la Informacion pueden establecer condiciones especificas de excepcion que no infrinjan legislacion vigente ni comprometan la seguridad. Cada excepcion debe documentarse e iniciar proceso de revision de la politica.

## Historial de versiones

| Version | Fecha | Cambios |
|---|---|---|
| 00 | Agosto 2014 | Creacion del documento |
| 01 | Octubre 2016 | Actualizacion normativa, inclusion de controles |
| 02 | Julio 2020 | Actualizacion a normativa vigente |
| 03 | Diciembre 2024 | Actualizacion a ISO 27002:2022. Actualizacion de responsabilidades, leyes, decretos, directrices generales y periodo de revision |
