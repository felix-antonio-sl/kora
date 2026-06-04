---
_manifest:
  urn: urn:salud:kb:instructivo-seguridad-informacion-ciberseguridad-sector-salud-p04
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
    shard_index: 4
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

# Instructivo de Seguridad de la Informacion y Ciberseguridad para el Sector Salud - Parte 04

## 20. Control de Versiones

| Version | Fecha | Pag/Seccion Modificada | Motivo del Cambio |
|---|---|---|---|
| 1.0 | Nov 2021 | Todas | Creacion del documento (Res. Exenta N°785) |
| 2.0 | Abril 2025 | Todas | Adaptacion normativa nacional y estandares internacionales en materia de Seguridad de la Informacion y Ciberseguridad |

## 21. Anexos

Material complementario: definiciones, compendio normativo, estandares internacionales, matriz de riesgos, estructura de politicas e indicadores KPI/KRI.

## 21.1. Definiciones y Terminos Claves

| Termino | Definicion |
|---|---|
| **Activos de informacion** | Toda informacion o recurso relacionado para la creacion, almacenamiento, gestion o transmision de dicha informacion. Pueden ser materiales (RRHH especializados, aparatos, equipos, redes, instalaciones, soportes y sistemas de almacenamiento) o intangibles (datos, aplicaciones, sistemas operativos, bases de datos, imagen, reputacion, marcas) |
| **Activo informatico** | Toda informacion almacenada en una red y sistema informatico que tenga valor para una persona u organizacion |
| **Autenticacion** | Propiedad de la informacion que da cuenta de su origen legitimo |
| **Anonimizacion** | Procedimiento irreversible en virtud del cual un dato personal no puede vincularse o asociarse a una persona determinada, ni permitir su identificacion, por haberse destruido o eliminado el nexo con la informacion que vincula, asocia o identifica a esa persona. Un dato anonimizado deja de ser un dato personal |
| **Agencia (ANCI)** | La Agencia Nacional de Ciberseguridad |
| **Auditorias de seguridad** | Procesos de control destinados a revisar el cumplimiento de las politicas y procedimientos que se derivan del SGSI |
| **Seudonimizacion** | Tratamiento de datos personales que se efectua de manera tal que ya no puedan atribuirse a un titular sin utilizar informacion adicional que permita la reidentificacion, la cual debe constar en medios seguros, gestionados por separado, y estar sujeta a medidas tecnicas y organizativas |
| **Ciberespacio** | Ambiente complejo, soportado por hardware y las redes de comunicaciones, en el cual constan interacciones entre personas, software y servicios de Internet, destinados a la distribucion mundial de informacion y comunicacion (ISO 27032) |
| **Ciberataque** | Accion realizada con la finalidad de destruir, exponer, alterar, deshabilitar, o exfiltrar u obtener acceso o hacer uso no autorizado de un activo informatico |
| **Ciberseguridad** | Preservacion de la confidencialidad e integridad de la informacion y de la disponibilidad y resiliencia de las redes y sistemas informaticos, con el objetivo de proteger a las personas, la sociedad, las organizaciones o las naciones de incidentes de ciberseguridad |
| **Incidente de ciberseguridad** | Todo evento que perjudique o comprometa la confidencialidad o integridad de la informacion, la disponibilidad o resiliencia de las redes y sistemas informaticos, o la autenticacion de los procesos ejecutados o implementados en las redes y sistemas informaticos |
| **Confidencialidad** | Propiedad que consiste en que la informacion no es accedida o entregada a individuos, entidades o procesos no autorizados |
| **Continuidad de servicios** | Capacidad de una organizacion para mantener la disponibilidad de sus servicios, reduciendo el riesgo de eventos que puedan dar lugar a una interrupcion o inestabilidad en las operaciones |
| **Disponibilidad** | Propiedad que consiste en que la informacion es accesible y utilizable cuando es requerida por un individuo, entidad o proceso autorizado |
| **Datos Personales** | Los datos relativos a cualquier informacion concerniente a personas naturales, identificadas o identificables, con independencia de su soporte |
| **Datos Sensibles** | Datos personales que se refieren a caracteristicas fisicas o morales de las personas o a hechos o circunstancias de su vida privada o intimidad. [Nota: Ley 21.719 (vigencia 01-dic-2026) sustituye: "Datos personales sensibles: aquellos datos personales que se refieren a las caracteristicas fisicas o morales de las personas o a hechos o circunstancias de su vida privada o intimidad, que revelen el origen etnico o racial, la afiliacion politica, sindical o gremial, la situacion socioeconomica, las convicciones ideologicas o filosoficas, las creencias religiosas, los datos relativos a la salud, al perfil biologico humano, los datos biometricos, y la informacion relativa a la vida sexual, a la orientacion sexual y a la identidad de genero de una persona natural"] |
| **CSIRT** | Centros multidisciplinarios que tienen por objeto prevenir, detectar, gestionar y responder a incidentes de ciberseguridad o ciberataques, en forma rapida y efectiva, conforme a procedimientos y politicas predefinidas |
| **Gestion de incidentes** | Procedimientos para la deteccion, analisis, manejo, contencion y resolucion de un incidente de ciberseguridad |
| **Incidente** | Evento inesperado o no deseado con consecuencias en detrimento de la seguridad de las redes, equipos y sistemas de informacion |
| **Infraestructura critica** | Las instalaciones, sistemas fisicos o servicios esenciales y de utilidad publica, redes, servicios y equipos fisicos y de tecnologia de la informacion cuya afectacion, degradacion, denegacion, interrupcion o destruccion cause un grave daño a la salud o al abastecimiento de la poblacion, a la actividad economica esencial, al medioambiente o a la seguridad del pais. Incluye sistemas de asistencia sanitaria o de salud |
| **Integridad** | Propiedad que consiste en que la informacion no ha sido modificada o destruida sin autorizacion |
| **Nube privada** | Infraestructura de la nube aprovisionada para uso exclusivo de una unica organizacion, propia o de terceros, dentro o fuera de las instalaciones |
| **Nube publica** | Infraestructura y recursos logicos disponibles para el publico en general a traves de Internet, propiedad de un Prestador de Servicios |
| **Proteccion de los activos de informacion** | Adopcion de las medidas que resguarden la seguridad fisica de los dispositivos, asi como los accesos a estos |
| **Red y sistema informatico** | Conjunto de dispositivos, cables, enlaces, enrutadores u otros equipos de comunicaciones o sistemas que almacenen, procesen o transmitan datos digitales |
| **Resiliencia** | Capacidad de las redes y sistemas informaticos para seguir operando luego de un incidente de ciberseguridad, aunque sea en un estado degradado, debilitado o segmentado, y la capacidad para recuperar sus funciones despues de un incidente |
| **Riesgo** | Posibilidad de ocurrencia de un incidente de ciberseguridad; la magnitud se cuantifica en terminos de la probabilidad de ocurrencia y del impacto de las consecuencias |
| **Riesgo de Ciberseguridad** | Toda circunstancia o hecho razonablemente identificable y previsible, que tenga un posible efecto adverso en la seguridad de las redes, equipos y sistemas de informacion |
| **Seguridad de la informacion** | Conjunto de medidas preventivas y reactivas que tienen por objeto resguardar y proteger la informacion, asegurando la confidencialidad, integridad, autenticidad y disponibilidad de los datos, continuidad de servicios y proteccion de activos de informacion |
| **Tratamiento de datos** | Cualquier operacion o conjunto de operaciones o procedimientos tecnicos, de caracter automatizado o no, que permitan de cualquier forma recolectar, procesar, almacenar, comunicar, transmitir o utilizar datos personales o conjuntos de datos personales |
| **Vulnerabilidad** | Debilidad de un activo o control que puede ser explotado por una o mas amenazas informaticas |

## 21.2. Normativa sobre Seguridad de la Informacion

### 21.2.1. Normativa del Sector Salud

| Norma | Descripcion |
|---|---|
| DFL N°1, 24-abr-2006 | Texto refundido, coordinado y sistematizado del DL N°2.763/1979 y leyes N°18.933 y 18.469 |
| DFL N°725 | Codigo Sanitario |
| Ley N°19.966/2004 | Regimen de garantias de salud |
| Ley N°19.650 | Perfecciona normas del area de la salud |
| Ley N°20.120/2006 | Investigacion cientifica en el ser humano, su genoma, prohibe la clonacion humana |
| Ley N°20.584 | Deberes y Derechos de las Personas en Atencion de Salud |
| Ley N°20.724/2014 | Modifica Codigo Sanitario en regulacion de medicamentos |
| Ley N°20.850/2016 | Sistema de proteccion financiera para diagnosticos y tratamientos de alto costo (Ley Ricarte Soto) |
| Ley N°21.258/2020 | Ley nacional del cancer (Ley Claudio Mora) |
| Ley 21.541/2023 | Autoriza atenciones mediante telemedicina |
| Decreto N°41/2012 | Reglamento de Ficha Clinica |
| Decreto N°31/2012 | Reglamento sobre entrega de informacion y consentimiento informado |
| Decreto N°38/2005 | Reglamento Organico de establecimientos de salud de menor complejidad y de autogestion en red |
| Decreto N°38/2012 | Reglamento sobre derechos y deberes de las personas en atencion de salud |
| Decreto N°38/2013 | Modifica Decreto N°466/1984, Reglamento de Farmacias, Droguerias, etc. |
| Decreto N°6/2021 | Reglamento sobre acciones de atencion de salud realizadas a distancia |
| Decreto N°820/2011 | Ministerio de Salud |

### 21.2.2. En Materia de Documentos Electronicos

| Norma | Descripcion |
|---|---|
| Ley N°19.880/2003 | Bases de los procedimientos administrativos |
| Ley N°21.180 | Transformacion digital del Estado |
| Ley N°19.799/2002 | Firmas y documentos electronicos |
| Decreto N°181 | Reglamento Ley N°19.799 sobre documentos electronicos, firma electronica y certificacion |
| Decreto N°83/2005 | SEGPRES |
| Decreto N°14/2014 | SEGPRES |
| Decreto N°1/2015 | SEGPRES |
| Decreto N°4/2021 | SEGPRES, Reglamento de procedimientos administrativos por medios electronicos (Ley 21.180) |
| Decreto N°24/2019 | Min. Economia, Norma tecnica para servicio de certificacion de firma electronica avanzada |
| Decreto N°1/2015 | SEGPRES, Norma tecnica sobre sistemas y sitios web de los organos de la administracion del Estado |

### 21.2.3. En Materia de Seguridad de la Informacion

| Norma | Descripcion |
|---|---|
| Ley N°21.663 | Marco de Ciberseguridad |
| Decreto N°295/2024 | Reglamento de reporte de incidentes de ciberseguridad (Ley 21.663) |
| Decreto N°483/2024 | Estructura interna de la Agencia Nacional de Ciberseguridad (ANCI) |
| Decreto N°164/2023 | Politica Nacional de Ciberseguridad 2023-2028 |
| Decreto Supremo N°7/2023 | SEGPRES, Norma Tecnica de Seguridad de la Informacion y Ciberseguridad (Ley 21.180) |
| Decreto Supremo N°83/2005 | Norma tecnica sobre seguridad y confidencialidad de los documentos electronicos |
| Decreto N°273/2022 | Obligacion de reportar incidentes de ciberseguridad |
| Circular N°711/2023 | Lineamientos sobre uso de IA en el sector publico (SEGPRES) |
| Res. Exenta N°372/2025 | Recomendaciones del Consejo para la Transparencia sobre Transparencia Algoritmica |
| Oficio N°7286/2025 | Guia del Consejo para la Transparencia para adopcion de Recomendaciones sobre Transparencia Algoritmica |

### 21.2.4. En Materia de Proteccion de Datos Personales

| Norma | Descripcion |
|---|---|
| Art. 19 Nos. 1 y 4 CPR | Constitucion Politica de la Republica |
| Ley N°19.628/1999 | Sobre proteccion de la vida privada |
| Ley N°21.719/2024 | Modifica Ley N°19.628, sustituyendo nombre por "Ley de Proteccion de Datos Personales" (vigencia: 01-dic-2026) |
| Ley N°20.575 | Principio de finalidad en el tratamiento de datos personales |
| Decreto N°779/2000 | Reglamento del Registro de Bancos de Datos Personales a cargo de organismos publicos |
| Res. Exenta N°489/2022 | Consejo para la Transparencia, Procedimiento para tramitacion de solicitudes de ejercicio de derechos Ley N°19.628 |

### 21.2.5. En Materia de Delitos Informaticos

| Norma | Descripcion |
|---|---|
| Ley N°21.459/2022 | Normas sobre delitos informaticos, deroga Ley N°19.223, adecua al Convenio de Budapest |
| Ley N°20.009 | Sobre clonacion de tarjetas de credito |
| Decreto N°83/2017 | Promulga el Convenio de Budapest en Chile |

### 21.2.6. En Materia de Propiedad Intelectual

| Norma | Descripcion |
|---|---|
| Ley N°19.039 | Propiedad Industrial |
| Ley N°17.336 | Propiedad Intelectual (proteccion de programas computacionales) |

### 21.2.7. Normas de Aplicacion General

| Norma | Descripcion |
|---|---|
| Ley 21.542 | Modifica Constitucion para proteccion de infraestructura critica por FF.AA. |
| Ley N°21.180 | Transformacion digital del Estado |
| Ley N°19.880 | Bases de los procedimientos administrativos |
| Ley N°20.285 | Transparencia y acceso a la informacion publica |
| Ley N°19.886 | Compras publicas |
| Decreto N°661 | Reglamento de Ley N°19.886 sobre contratos administrativos |
| Res. Exenta N°619-B/2018 | Direccion de Compras y Contratacion Publica |

## 21.3. Estandares Internacionales y Normativa Nacional

| Tema | Nombre | Descripcion |
|---|---|---|
| Gestion de Seguridad de la Informacion | **ISO 27001:2022** | Requisitos para establecer, implementar, mantener y mejorar un SGSI |
| Controles de Seguridad | **ISO 27002:2022** | Guia de buenas practicas para controles de seguridad de la informacion |
| Controles de Seguridad | **NIST SP 800-53** | Catalogo de controles de privacidad y seguridad para sistemas de informacion |
| Seguridad en Salud | **ISO/IEC 27799:2016** | Aplica principios de ISO/IEC 27002 al ambito de la salud |
| Gestion de Riesgos | **ISO 31000** | Principios y directrices para gestion de riesgos |
| Continuidad del Negocio | **ISO 22301** | Requisitos para sistema de gestion de continuidad del negocio |
| Proteccion de Datos de Salud (EE.UU.) | **HIPAA** | Health Insurance Portability and Accountability Act |
| Proteccion de Datos (UE) | **GDPR - UE 2016/679** | Reglamento General de Proteccion de Datos |
| Intercambio de Registros de Salud (UE) | **Electronic Health Record Exchange Format** | Marco para intercambio de registros electronicos de salud con interoperabilidad y seguridad |
| Proteccion de Datos (Chile) | **Ley N°19.628** | Ley chilena sobre Proteccion de la Vida Privada |
| Proteccion de Datos (Chile) | **Ley N°21.719** | Modifica Ley 19.628 incorporando estandares modernos de proteccion de datos personales |
| Gobernanza de Datos (UE) | **European Data Governance Act (DGA)** | Marco para intercambio seguro de datos dentro de la UE |
| Ciberseguridad | **NIST Cybersecurity Framework** | Marco basado en 5 funciones: Identificar, Proteger, Detectar, Responder, Recuperar |
| Ciberseguridad | **CIS Controls v8** | Controles priorizados para defensa contra amenazas ciberneticas comunes |
| Gestion de Incidentes | **ISO/IEC 27035** | Guias para gestion de incidentes de seguridad de la informacion |
| Ciberseguridad (UE) | **Directiva NIS 2 - UE 2022/2555** | Requisitos de ciberseguridad para sectores criticos, incluyendo salud |
| Ciberseguridad (UE) | **ENISA** | Buenas practicas, marcos y herramientas para ciberseguridad a nivel europeo |
| Ciberseguridad (Chile) | **Ley N°21.663** | Ley Marco de Ciberseguridad de Chile |
| Seguridad de Redes | **ISO/IEC 27033** | Guias detalladas para seguridad en redes |
| Salud Digital (Chile) | **Ley N°21.541** | Regula atencion medica por medios digitales (telemedicina) con requisitos de ciberseguridad |
| Etica de IA (Chile) | **Circular N°711/2023** | Lineamientos para uso etico y seguro de IA en organismos publicos de Chile |
| Etica de IA (UE) | **EU AI Act** | Marco legal propuesto por la Comision Europea para regular sistemas de IA |
| Transparencia Algoritmica (Chile) | **Res. Exenta N°372/2025** y **Oficio N°7286/2025** | Recomendaciones del Consejo para la Transparencia sobre Transparencia Algoritmica y SDA |

## 21.4. Matriz de Riesgos de Seguridad de la Informacion (Ejemplo)

| Amenaza | Vulnerabilidad | Impacto Potencial | Control Preventivo | Control Correctivo |
|---|---|---|---|---|
| **Ataques de ransomware** | Sistemas desactualizados, falta de parches de seguridad | Inaccesibilidad a datos clinicos criticos, interrupcion de servicios de salud | Actualizacion periodica de software, EDR y antivirus de nueva generacion, segmentacion de redes criticas | Plan de recuperacion ante incidentes (IRP), Restauracion desde respaldos verificados |
| **Perdida o robo de dispositivos moviles** | Falta de cifrado de dispositivos, ausencia de MDM | Fuga de datos sensibles de pacientes | Cifrado completo de dispositivos moviles, Gestion de dispositivos moviles (MDM), Autenticacion multifactor | Borrado remoto, Investigacion de incidente y notificacion a la autoridad |
| **Acceso no autorizado a sistemas clinicos** | Politicas de acceso debiles, cuentas compartidas o no robustas | Modificacion o exfiltracion de datos de pacientes, daño reputacional | Politicas de control de acceso basadas en roles (RBAC), Autenticacion multifactor (MFA), Revisiones periodicas de cuentas y permisos | Bloqueo inmediato de cuentas comprometidas, Analisis forense y remediacion de brechas |
| **Phishing dirigido a personal administrativo o clinico** | Falta de capacitacion en ciberseguridad, filtros de correo inadecuados | Compromiso de credenciales, infeccion de malware | Programas de concienciacion en ciberseguridad, Filtros avanzados de correo (antiphishing, antispam) | Restablecimiento inmediato de credenciales, Analisis de dispositivos y contencion de malware |
| **Fallas en alta disponibilidad y sistemas criticos (HIS, PACS, LIS)** | Ausencia de alta disponibilidad y respaldo de sistemas | Interrupcion en diagnosticos, tratamientos, procedimientos clinicos | Implementacion de arquitecturas de alta disponibilidad (HA), Sistemas de respaldo en caliente y pruebas de recuperacion | Activacion de procedimientos de continuidad operativa, Recuperacion desde entornos alternativos |

## 21.5. Estructura de Politicas y Procedimientos (Ejemplo, 13 Politicas Mapeadas a ISO 27001:2022)

| Politica / Procedimiento | Proposito | Categoria ISO/IEC 27001:2022 | Procedimientos Asociados |
|---|---|---|---|
| **Politica General de Seguridad de la Informacion** | Establece el marco general de gestion de la seguridad de la informacion y el compromiso institucional | Politicas de Seguridad de la Informacion (A.5) | Procedimiento de revision y aprobacion de politicas, Procedimiento de difusion institucional |
| **Politica de Control de Accesos** | Regula el acceso fisico y logico a los sistemas y la informacion | Organizacion de la Seguridad de la Informacion | Procedimiento de gestion de cuentas de usuario, Procedimiento de revision periodica de accesos |
| **Politica de Uso Aceptable de Recursos** | Establece normas para el uso correcto de los recursos tecnologicos institucionales | Politicas de Seguridad de la Informacion | Procedimiento de monitoreo del uso de recursos, Procedimiento de sancion por mal uso |
| **Politica de Gestion de Activos** | Define como identificar, clasificar y proteger los activos de informacion | Gestion de Activos (A.5, A.8) | Procedimiento de inventario, Procedimiento de clasificacion y etiquetado |
| **Politica de Clasificacion y Manejo de la Informacion** | Establece criterios para el uso y proteccion de la informacion segun su sensibilidad | Gestion de Activos (A.5, A.8) | Procedimiento de clasificacion, Procedimiento de destruccion segura |
| **Politica de Respaldo y Recuperacion** | Establece directrices para respaldar y restaurar informacion critica | Operacion (A.12) | Procedimiento de respaldos, Procedimiento de prueba de restauracion |
| **Politica de Continuidad Operacional y DRP** | Asegura la continuidad del negocio frente a interrupciones | Seguridad de la Continuidad (A.17) | Procedimiento de activacion del plan, Procedimiento de pruebas periodicas |
| **Politica de Seguridad Fisica y Ambiental** | Controla acceso fisico y proteccion del entorno | Seguridad Fisica (A.11) | Procedimiento de control de accesos fisicos, Procedimiento de contingencias ambientales |
| **Politica de Seguridad en el Ciclo de Vida de los Sistemas** | Integra seguridad desde el diseno hasta el retiro de sistemas | Adquisicion, desarrollo y mantenimiento de sistemas (A.14) | Procedimiento de desarrollo seguro, Pruebas de aceptacion |
| **Politica de Relacion con Proveedores** | Establece requisitos de seguridad para terceros y contratistas | Relacion con Proveedores (A.15) | Evaluacion de seguridad de proveedores, Acuerdos de confidencialidad |
| **Politica de Gestion de Incidentes** | Define como responder y aprender de incidentes de seguridad | Gestion de Incidentes (A.16) | Procedimiento de deteccion, Procedimiento de notificacion, Analisis post-incidente |
| **Politica de Proteccion de Datos Personales** | Garantiza cumplimiento de Ley 19.628 en tratamiento de datos | Cumplimiento (A.5.34, A.18) | Procedimiento de gestion de consentimientos, Procedimiento de anonimizacion |
| **Politica de Correos Electronicos** | Normas de uso seguro y profesional del correo institucional | Comunicaciones (A.13) | Prevencion de phishing, Cifrado de correos |
| **Politica de Uso de Criptografia** | Determina mecanismos de cifrado aceptados para proteger la informacion | Criptografia (A.10) | Procedimiento de cifrado, Gestion de llaves |
| **Procedimientos e Instructivos Tecnicos** | Instrumentos que detallan como implementar los controles definidos por las politicas | Transversal | Revision de cumplimiento tecnico, Auditorias internas |
