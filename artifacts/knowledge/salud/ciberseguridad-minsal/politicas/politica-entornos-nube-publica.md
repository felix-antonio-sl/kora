---
_manifest:
  urn: urn:salud:kb:politica-entornos-nube-publica
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-05'
    source: MINSAL Chile, SGSI Nivel Central. PS-NC-022 v1, Junio 2023
  minsal_id: PS-NC-022
  minsal_version: '1'
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- politica
- nube-publica
- cloud
- aws
- azure
- gcp
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:politica-entornos-nube-publica
relations:
  cites:
  - urn:salud:kb:politica-general-seguridad-informacion-ciberseguridad
---

# Politica de Seguridad para Entornos de Nube Publica

## Proposito y alcance

Establecer lineamientos y requisitos de seguridad para la gestion y proteccion de los entornos de nube publica utilizados por el MINSAL. Define controles y practicas para asegurar confidencialidad, integridad y disponibilidad de la informacion critica almacenada y procesada en la nube, minimizando riesgos y garantizando resiliencia operativa.

Aplica a todos los recursos, aplicaciones, servicios, datos y usuarios que interactuan con entornos de nube publica del MINSAL, incluyendo servicios de AWS, Azure y GCP. Aplica a proveedores, funcionarios o personal con acceso a estos entornos.

**Controles ISO 27001:2022 asociados**:

| Estandar | ID | Control |
| --- | --- | --- |
| ISO 27001:2022 - Organizacionales | 5.16 | Gestion de Identidad |
| | 5.17 | Informacion de Autenticacion |
| | 5.18 | Autenticacion de usuarios |
| | 5.19 | Gestion de acceso privilegiado |
| ISO 27001:2022 - Tecnologia | 8.5 | Autenticacion Segura |
| | 8.6 | Gestion de accesos a la red |
| | 8.7 | Gestion de accesos a sistemas operativos |
| | 8.8 | Gestion de accesos a aplicaciones |

## Definiciones

**Modelo de Responsabilidad Compartida** — Division de responsabilidades entre el proveedor de servicios en la nube y el cliente.

**SaaS** — Software as a Service: aplicaciones completas accesibles via internet sin instalacion ni mantenimiento por parte del cliente.

**PaaS** — Platform as a Service: plataforma para desarrollar, ejecutar y gestionar aplicaciones sin gestionar infraestructura subyacente.

**IaaS** — Infrastructure as a Service: recursos virtualizados (maquinas, almacenamiento, redes) con gestion del cliente sobre aplicaciones y configuraciones.

**Nube Publica** — Infraestructura compartida por multiples organizaciones gestionada por un proveedor externo (AWS, Azure, GCP).

**Nube Privada** — Infraestructura utilizada exclusivamente por una organizacion, gestionada internamente o por un tercero.

**Nube Hibrida** — Modelo que combina nubes publicas y privadas permitiendo transferencia de datos y aplicaciones entre ellas.

**Proveedor de Servicios en la Nube (CSP)** — Entidad que ofrece servicios en la nube como almacenamiento, plataformas o infraestructura.

**Cloud Computing** — Modelo de acceso a recursos tecnologicos via internet sin gestionar infraestructura fisica local.

## Marco normativo y documentos relacionados

**Normas tecnicas**:
- NCh ISO27001:2022 — Seguridad de la informacion, ciberseguridad y proteccion de la privacidad
- ISO/IEC 27017 — Controles y asesoramiento para proveedores de servicios en la nube
- Marco Juridico SSI, CSIRT del Ministerio del Interior

**Leyes y decretos aplicables**:

| Norma | Materia |
| --- | --- |
| Ley 19.628 | Proteccion de vida privada y datos personales (modificada por Ley 21.719, vigencia 01-12-2026) |
| Ley 20.285, 2008 | Acceso a la informacion publica |
| Ley 20.584, 2012 | Derechos y deberes vinculados a la atencion en salud |
| Ley 21.459 | Normas sobre delitos informaticos (deroga Ley 19.223, adecua al Convenio de Budapest) |
| Ley 21.180 | Transformacion Digital del Estado |
| Ley 21.541 | Autoriza telemedicina |
| Ley 21.663 | Marco de Ciberseguridad |
| Ley 21.668 | Interoperabilidad de fichas clinicas |
| Ley 19.886 | Compras y contratacion publica |
| Decreto 41, 2012 | Reglamento sobre fichas clinicas |
| Decreto 273, 2022 | Obligacion de reportar incidentes de ciberseguridad al CSIRT |
| Decreto 6, 2021 | Reglamento sobre atencion de salud a distancia |
| Decreto 40, 2012 | Reglamentos internos de prestadores institucionales |
| Decreto 38, 2012 | Derechos y deberes vinculados a la atencion de salud |
| Decreto 7, 2019 | Reglamento sobre notificacion de enfermedades de declaracion obligatoria |
| Decreto 533, 2015 | Crea Comite Interministerial sobre Ciberseguridad |
| Decreto 20 | Aprueba Politica Nacional de Inteligencia Artificial |
| Decreto Supremo 7 | Norma Tecnica de Seguridad de la Informacion y Ciberseguridad |
| Resolucion Exenta 342, 2018 | Aprueba Programa Nacional de Telesalud |
| Circular 711 | Lineamientos sobre uso de herramientas de IA en el sector publico |

## Roles y responsabilidades

**CISO (Responsable de Seguridad de la Informacion)** — Define y revisa la implementacion de la politica. Supervisa procesos de auditoria y cumplimiento.

**Unidad de Arquitectura** — Diseña y define lineamientos tecnicos, estandares y metodologias para configuracion coherente y segura de entornos de nube. Selecciona herramientas, tecnologias y enfoques para integracion de servicios cloud. Asegura escalabilidad, interoperabilidad y cumplimiento normativo.

**Administradores de la nube (Accesos Privilegiados)** — Gestionan accesos, configuracion y seguridad de los entornos de nube. Abarcan todos los entornos asociados a areas o unidades con responsabilidad de gestion total por contratacion directa.

**Ingeniero Cloud** — Ejecuta acciones y configuraciones siguiendo diseños de la Unidad de Arquitectura. Implementa soluciones aprobadas por el CISO.

**Funcionarios MINSAL (Usuarios)** — Cumplir politicas de acceso, uso seguro de datos y notificar inmediatamente incidentes de seguridad.

**Proveedor de la nube (AWS, Azure, GCP)** — Cumplir acuerdos de nivel de servicio y permitir auditorias para verificar conformidad con requisitos de seguridad.

## Materias que aborda

- Arquitectura de Seguridad en la Nube (AWS, Azure, GCP)
- Gestion de Identidades y Accesos (IAM)
- Proteccion de Datos
- Resiliencia y Continuidad
- Monitoreo y Deteccion de Amenazas
- Pruebas de Seguridad y Auditoria

## Arquitectura de seguridad

Disenar la arquitectura siguiendo la triada CIA (confidencialidad, integridad, disponibilidad). Incorporar principios de seguridad desde la fase de diseño. Emplear segmentacion de red y aislamiento de cargas de trabajo.

**Resource Management** — Gestion eficiente de recursos en nube:
- Control de asignacion para evitar aprovisionamiento excesivo y minimizar riesgos de exposicion
- Monitoreo y administracion continua para detectar y mitigar actividades sospechosas
- Politicas de uso eficiente para reducir costos y asegurar disponibilidad
- Restriccion de accesos y permisos basada en minimo privilegio

## Modelo de Confianza Zero (Zero Trust)

Ninguna entidad (usuario, dispositivo o aplicacion) es confiable por defecto. Toda interaccion requiere autenticacion, autorizacion y verificacion continua.

- Autenticacion multifactor (MFA) y autorizacion basada en contexto para toda comunicacion
- Segmentacion de red y microsegmentacion para dividir el entorno en zonas menores
- Aislamiento de datos criticos y aplicaciones en segmentos con control estricto de acceso y trafico

## Seguridad desde el Diseño (Security by Design)

Controles de seguridad integrados desde la fase de diseño en cada fase de desarrollo e implementacion. Alineacion con ISO 27001, 27017 y 27018. Capas de seguridad en cada nivel de la arquitectura: control de acceso, almacenamiento y procesamiento de datos.

## Segmentacion de Redes y Microsegmentacion

Division de redes en segmentos mas pequeños mediante VLANs para reducir superficie de ataque. Control estricto de trafico entre segmentos con politicas que permitan solo trafico autorizado. Uso de firewalls y WAF perimetrales y de aplicaciones para monitoreo y restriccion de trafico entre segmentos.

## Gestion de Identidad y Acceso (IAM)

**Principio de Minimo Privilegio** — Cada usuario, dispositivo o sistema cuenta unicamente con los permisos necesarios para sus tareas especificas. Sin privilegios excesivos explotables en caso de brecha.

**MFA obligatorio** — Autenticacion multifactor para acceso a recursos y datos sensibles por parte de todos los usuarios y administradores. Segundo factor de autenticacion (ej. codigo enviado a dispositivo registrado).

**Roles en lugar de credenciales estaticas** — Eliminar credenciales o claves API permanentes. Uso de roles y permisos temporales:

| Proveedor | Mecanismo |
| --- | --- |
| AWS | IAM Roles: permisos temporales y especificos a usuarios y servicios |
| Azure | Managed Identities: credenciales automaticas y rotativas, sin gestion manual |
| GCP | Service Accounts: permisos especificos y temporales para aplicaciones y servicios |

## Gestion de claves y tokenizacion

**Cifrado obligatorio** — Todos los datos sensibles cifrados en reposo y en transito. Sin acceso sin claves de descifrado correspondientes.

**Gestion centralizada de claves**:

| Proveedor | Servicio | Capacidades |
| --- | --- | --- |
| AWS | AWS KMS | Rotacion automatica, registro detallado de actividades, control de acceso IAM |
| Azure | Azure Key Vault | Politicas de acceso, rotacion automatica, registros de auditoria |
| GCP | Google Cloud KMS | Controles avanzados de rotacion y gestion, politicas de control de acceso |

**Tokenizacion y enmascaramiento** — Para datos altamente sensibles (salud, confidenciales): sustitucion de datos reales por identificadores o versiones enmascaradas sin valor fuera del sistema autorizado.

## Geolocalizacion y proteccion de datos sensibles

- Recopilacion y uso de datos de geolocalizacion limitado a lo estrictamente necesario para competencias legales del organismo
- Si los datos se almacenan o procesan fuera de Chile, el proveedor debe cumplir con estandares aceptables de proteccion de datos personales (paises con proteccion equivalente o contratos especificos)
- Cifrado en transito y reposo, controles de acceso restringido
- Derecho de titulares a acceder, rectificar, solicitar eliminacion y revocar consentimiento. Procedimientos efectivos para ejercicio de estos derechos
- Registro detallado de tratamientos, accesos y modificaciones para trazabilidad y verificacion de cumplimiento
- Auditorias periodicas para verificar cumplimiento y acceso restringido a personal autorizado

## Alta disponibilidad y recuperacion ante desastres

**Multi-AZ y multi-region** — Alta disponibilidad mediante multiples zonas de disponibilidad y regiones para reducir puntos unicos de falla.

| Proveedor | Estrategia |
| --- | --- |
| AWS | RDS Multi-AZ: replicacion de bases de datos con conmutacion por error automatica |
| Azure | Azure SQL Database Failover Groups: conmutacion entre bases de datos en diferentes regiones |
| GCP | Google Cloud Spanner: replicacion global y recuperacion ante desastres con failover automatico |

**Replicacion** — Aplicaciones criticas y bases de datos replicadas en tiempo real con pruebas regulares de capacidad de recuperacion rapida.

**Automatizacion de failover y backups** — Scripts y servicios gestionados para recuperacion rapida sin intervencion manual. Backups automaticos regulares en ubicaciones seguras con copias en diferentes regiones. Pruebas periodicas de restauracion.

## Administracion de informacion de autenticacion secreta

Monitoreo y deteccion de amenazas para deteccion temprana y respuesta rapida del equipo de seguridad mediante:

- **SIEM** — Centralizacion y correlacion de eventos en tiempo real para detectar amenazas unificando datos de multiples fuentes y patrones anomalos
- **UEBA** — Analisis basado en IA y aprendizaje automatico para identificar patrones de comportamiento normal y detectar anomalias. Especialmente util para amenazas internas
- **Monitoreo proactivo** — Identificacion temprana de amenazas y respuestas automaticas mediante politicas predefinidas que minimizan tiempo de reaccion

## Gestion de vulnerabilidades y actualizacion de seguridad

**Evaluacion y remediacion** — Evaluaciones periodicas de vulnerabilidades en sistemas, aplicaciones y redes. Aplicacion oportuna de parches de seguridad.

**Automatizacion** — Herramientas automatizadas de gestion de parches para detectar, priorizar y aplicar actualizaciones. Alertas proactivas para vulnerabilidades no gestionadas o criticas.

**Ciclo de mejora continua** — Revision regular de seguridad alineada con CIS y NIST. Documentacion y auditoria de procesos para cumplimiento normativo y mejora de resiliencia.

## Almacenamiento en nube

**Reglas por criticidad de la informacion**:

| Clasificacion | Condicion |
| --- | --- |
| Operacional | Permitido solo para datos necesarios en plataformas autorizadas por MINSAL |
| Sensible (pacientes, registros clinicos, estrategicos) | Solo si el proveedor cumple normativas de seguridad vigentes |
| Critico | Solo en servicios con configuraciones avanzadas de seguridad |

**Proveedores aprobados** — AWS, Azure y GCP con contratos vigentes que incluyan clausulas de seguridad y cumplimiento normativo. Prohibidos servicios de almacenamiento personales (Google Drive, Dropbox personal).

**Acceso y comparticion** — Acceso limitado a personal autorizado. Comparticion de datos y documentos mediante metodos seguros que limiten exposicion a usuarios no autorizados.

**Cifrado de datos** — AES-256 en transito y reposo. Claves de cifrado gestionadas de manera segura y restringidas a usuarios con roles especificos.

**Gestion de identidad y acceso** — MFA para acceder a servicios en la nube. Permisos basados en roles (RBAC) limitados a los datos necesarios para sus funciones.

**Clasificacion de informacion** — Clasificar la informacion segun politicas internas del MINSAL (confidencial, sensible, publica) antes de almacenar en nube. Evaluar y gestionar riesgos por categoria.

**Backup y recuperacion** — Copias de seguridad automaticas replicadas en multiples regiones. Pruebas regulares de restauracion para verificar integridad de datos respaldados.

**Procedimientos obligatorios para funcionarios** — Cumplimiento estricto de politicas. Capacitacion periodica en buenas practicas. Reporte inmediato de incidentes (accesos no autorizados, perdida de datos) al area de TI o al CISO.

## Pruebas de seguridad y auditoria

**Pruebas de penetracion** — Periodicas para identificar vulnerabilidades simulando ataques que evaluan la resistencia de sistemas y aplicaciones.

**Auditorias externas** — Organizaciones independientes validan conformidad con ISO 27001, 27017 y 27018.

**Red Team y Ethical Hacking** — Metodologias definidas y aprobadas por MINSAL junto con Ciberseguridad y Arquitectura. Objetivo: fortalecer inteligencia de amenazas mediante ejercicios avanzados (analisis de vulnerabilidades, Pentest, simulaciones de ataques reales). Frecuencia minima: Red Teaming/Pentest anual, analisis de vulnerabilidades cada 3 meses.

**Revisiones de arquitectura** — Periodicas para identificar y corregir debilidades en controles. Uso de herramientas de asesoria (AWS Trusted Advisor, Azure Advisor) para recomendaciones de mejores practicas.

## Servicios de almacenamiento en nube publica

**Criterios de uso** — Nubes publicas exclusivamente para informacion no critica ni confidencial (reportes estadisticos no sensibles, documentacion administrativa de soporte). Prohibido almacenar datos personales, confidenciales o sensibles en nubes publicas no autorizadas.

**Servicios permitidos**:

| Proveedor | Servicios |
| --- | --- |
| AWS | S3, RDS, Glacier |
| Microsoft Azure | Azure Blob Storage, Azure Files |
| Google Cloud Platform (GCP) | Google Cloud Storage, Filestore |

**Restricciones** — Prohibidos servicios no corporativos (Dropbox, Google Drive personal, similares no gestionados por TI). Acceso solo desde dispositivos gestionados por TI con controles actualizados. Evaluacion anual de proveedores para verificar conformidad con estandares de seguridad.

## Proceso de eliminacion de informacion

- **Politicas de retencion** claras para toda informacion en nube. Eliminacion cuando ya no sea necesaria para operaciones o cumplimiento normativo
- **Metodos de eliminacion segura** — Herramientas nativas del proveedor (AWS S3 Object Lock, borrado criptografico en Azure y GCP). Confirmacion mediante auditorias y reportes automaticos
- **Registro de eliminacion** — Fecha, hora, usuario responsable y confirmacion de eliminacion exitosa

## Copias de seguridad en la nube

- **Automatizacion** — Todos los sistemas criticos cuentan con copias de seguridad automatizadas
- **Distribucion**:
 - Almacenamiento en multiples regiones dentro del territorio de Chile para resiliencia y cumplimiento de leyes de proteccion de datos y ciberseguridad
 - Si el proveedor no cuenta con infraestructura en Chile: politica de no replicacion fuera de Chile o control estricto de replicacion hacia otros paises
 - Si solo existe una region: uso de zonas de disponibilidad separadas dentro de la misma infraestructura
 - Enfoque hibrido recomendado: copia primaria en infraestructura propia y copia secundaria en nube publica
 - Servicios de alta disponibilidad (AWS Glacier, Azure Backup)
- **Pruebas de restauracion** regulares para verificar integridad de datos y capacidad de recuperacion

## Contratacion de servicios en nube

**Medidas organizativas** — Verificar que el proveedor cuente con certificaciones de seguridad (ISO 27001, SOC 2). Evaluar politicas de seguridad del proveedor incluyendo gestion de incidentes y continuidad. Establecer acuerdos de nivel de servicio (SLA) con metricas claras de disponibilidad y respuesta.

**Medidas tecnicas** — Verificar cifrado de datos, controles de acceso y segmentacion. Evaluar capacidad de integracion con herramientas de monitoreo del MINSAL.

**Resguardos de legalidad** — Clausulas contractuales que aseguren cumplimiento de legislacion chilena de proteccion de datos, jurisdiccion aplicable y auditoria.

## Propiedad intelectual en entornos cloud

Los derechos de propiedad intelectual sobre datos, aplicaciones y desarrollos realizados por o para el MINSAL permanecen bajo titularidad del MINSAL, independientemente de la infraestructura cloud utilizada. Los contratos con proveedores deben incluir clausulas explicitas de propiedad intelectual y confidencialidad.

## Difusion

- Publicacion en intranet MINSAL: http://isalud.minsal.cl/
- Correo informativo

## Revision

Revision al menos cada dos años, o ante necesidades de cambios para garantizar idoneidad, adecuacion y efectividad.

## Excepciones

El Comite de Seguridad de la Informacion evaluara y podra establecer condiciones puntuales de excepcion, siempre que no se infrinja la legislacion vigente. Toda excepcion debe documentarse y generar un proceso de revision de la politica.

## Historial y control de versiones

| Version | Fecha | Creado por | Descripcion |
| --- | --- | --- | --- |
| 1.0 | Junio 2023 | MINSAL SGSI Nivel Central | Creacion del documento |

## Anexo: Comparacion de seguridad cloud (AWS vs Azure vs GCP)

Los tres proveedores ofrecen capacidades equivalentes en controles fundamentales de seguridad: cifrado en reposo y transito, gestion de identidad con MFA, RBAC, KMS con rotacion automatica, SIEM nativo, segmentacion de red (VPC/VNet), y certificaciones ISO 27001. Las diferencias estan en la implementacion especifica de cada servicio; esta politica exige que la Unidad de Arquitectura mantenga una matriz de equivalencia actualizada para cada servicio contratado.
