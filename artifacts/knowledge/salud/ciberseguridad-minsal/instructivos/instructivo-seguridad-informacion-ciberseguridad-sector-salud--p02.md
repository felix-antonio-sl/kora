---
_manifest:
  urn: urn:salud:kb:instructivo-seguridad-informacion-ciberseguridad-sector-salud-p02
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
    shard_index: 2
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

# Instructivo de Seguridad de la Informacion y Ciberseguridad para el Sector Salud - Parte 02

## 6.1.4. Capa de Aplicacion

| Control | Detalle |
|---|---|
| Ciclo de Vida de Desarrollo de Software Seguro (SSDLC) | OWASP, NIST; autenticacion, autorizacion, pruebas de seguridad |
| Validacion de Entradas | Prevencion de SQL Injection, XSS, CSRF; procedimientos almacenados y consultas preparadas |
| Codificacion Segura | Guias OWASP Top Ten |
| Control de Acceso a la Aplicacion | Basado en roles (RBAC) |
| Gestion Segura de Sesiones | Identificadores robustos, proteccion contra secuestro, invalidacion al cierre |
| Pruebas de seguridad | SAST (estaticas) y DAST (dinamicas), pentesting especifico |
| Manejo Seguro de Errores y Excepciones | Sin divulgacion de informacion sensible |
| Cifrado de datos sensibles en la aplicacion | Logs de auditoria detallados |
| Proteccion de Datos Sensibles | Cifrado en transito y reposo, anonimizacion/seudonimizacion, enmascaramiento en entornos no productivos |
| Gestion segura de APIs | OAuth 2.0, autorizacion granular, TLS 1.2+, OWASP API Top 10, validacion de entradas, limitacion de tasas, trazabilidad |
| APIs REST | Autenticacion via tokens (JWT), certificados, llaves criptograficas |

## 6.1.5. Capa de Seguridad de los Datos

| Control | Detalle |
|---|---|
| Autenticacion Fuerte | MFA obligatorio cuando sea posible |
| Cifrado de Datos en Reposo | AES-256, gestion segura de claves criptograficas |
| Cifrado de Datos en Transito | TLS 1.2 o superior |
| Firmas Digitales | Criptografia de clave publica; instrumentos publicos requieren Firma Electronica Avanzada |
| Prevencion de Perdida de Datos (DLP) | Monitoreo y control de movimiento de informacion sensible |
| Anonimizacion y Seudonimizacion | Segun aplique legalmente |
| Politicas de Retencion y Eliminacion Segura | Segun requisitos legales, procedimientos seguros |
| Auditoria de Acceso a Datos | Registro de accesos, modificaciones y eliminaciones |
| Clasificacion y etiquetado de informacion | Etiquetas automatizadas y manuales |
| Autenticacion | OAuth 2.0, SAML 2.0 para federacion de identidades |
| Autorizacion | ACLs, RBAC, ABAC consistentes en aplicacion e infraestructura |
| DLP | Prevencion de fuga via correo, USB, impresion o nube |
| Sistemas de respaldo automatizados | Copias locales y en nube, pruebas regulares de recuperacion (DRP/BIA) |

## 6.1.6. Capa de Seguridad de Dispositivos y Endpoints

| Control | Detalle |
|---|---|
| Antimalware Avanzado | Deteccion en tiempo real, analisis heuristico, NGAV con deteccion basada en comportamiento |
| EDR / XDR | Monitoreo continuo, deteccion temprana, respuesta automatizada, integracion con SIEM |
| Firewall Personal | Control de trafico entrante y saliente a nivel endpoint |
| Gestion Centralizada de Dispositivos Moviles (MDM/UEM) | Politicas de seguridad, configuracion, inventario, control de apps, borrado remoto |
| Control de Acceso al Dispositivo | Contrasenas complejas, PINs, biometria, bloqueo automatico por inactividad |
| Cifrado de Disco Completo | En portatiles y dispositivos con informacion sensible |
| Gestion de Parches y Actualizaciones | Proceso centralizado y automatizado para SO, aplicaciones y firmware |
| Control de Aplicaciones | Solo software autorizado, bloqueo de aplicaciones riesgosas |
| DLP en el Endpoint | Monitoreo y control de transferencia de informacion sensible |
| Control de dispositivos extraibles | Restriccion de USB no autorizados, registro de eventos, cifrado; puertos USB deshabilitados por defecto |
| Politicas de Uso Seguro de Dispositivos | Restricciones de software no autorizado, redes no seguras, informacion sensible en dispositivos personales |

## 6.1.7. Capa de Seguridad Operacional y de Monitoreo

| Control | Detalle |
|---|---|
| SOC o Funciones Equivalentes | Monitoreo continuo, analisis de alertas, gestion de incidentes |
| SIEM | Recopilacion, correlacion y analisis de logs de todas las fuentes |
| Monitoreo Continuo de Infraestructura | Salud, rendimiento y seguridad de red, servidores, aplicaciones y bases de datos |
| Alertas y Notificaciones en Tiempo Real | Personal de seguridad notificado inmediatamente |
| Procesos de Gestion de Incidentes Definidos | Identificacion, analisis, contencion, erradicacion, recuperacion, lecciones aprendidas |
| Equipos de Respuesta a Incidentes (IRT) | Roles y responsabilidades definidos |
| Inteligencia de Amenazas (Threat Intelligence) | Integracion en monitoreo y analisis para anticipar ataques |
| Analisis Forense | Investigacion de incidentes, causa raiz, alcance, evidencia |
| Ejercicios y Simulacros | Periodicos de respuesta a incidentes |
| Comunicacion de Incidentes | Protocolos para alta direccion y ANCI |
| CTI (Cyber Threat Intelligence) | Informacion contextualizada para anticipar campañas y vectores |
| Pruebas de seguridad | Evaluaciones periodicas de vulnerabilidades, pentesting, SAST/DAST, auditorias, simulacros |

## 6.1.8. Capa de Seguridad en la Nube

| Control | Detalle |
|---|---|
| IAM en la Nube | AWS IAM, Azure AD, Google Cloud IAM; principio de minimo privilegio; MFA obligatorio para cuentas privilegiadas |
| CSPM | Monitoreo continuo de configuracion, alertas automaticas, flujos de remediacion |
| Seguridad de la Red en la Nube | VPC/VNet, subredes, firewalls virtuales, segmentacion logica, VPN/Direct Connect para conectividad hibrida |
| Proteccion de Datos en la Nube | Cifrado con AWS KMS, Azure Key Vault, Google Cloud KMS; TLS/SSL 1.2+; politicas de retencion y eliminacion; DLP |
| Monitorizacion y Registro en la Nube | AWS CloudWatch, Azure Monitor, Google Cloud Logging; integracion con SIEM centralizado |
| Seguridad de Cargas de Trabajo | Hardening de SO, EDR/XDR cloud-optimizado, escaneo de vulnerabilidades en contenedores, politicas de seguridad en orquestacion, minimo privilegio en FaaS |
| Cumplimiento y Gobernanza en la Nube | Ley 21.663, Ley 19.628, HIPAA; auditorias periodicas; herramientas de cumplimiento del proveedor |

Consideraciones adicionales:
- **Modelo de Responsabilidad Compartida**: entender responsabilidades propias vs. proveedor
- **Seleccion del Proveedor**: cumplir con estandares y regulaciones del sector salud
- **Evaluacion Continua**: evaluaciones de seguridad regulares en entorno cloud

## 6.1.9. Tabla de Cumplimiento por Capas (Defensa en Profundidad)

| Capa | Objetivo Principal | Controles Claves | Estandares de Referencia |
|---|---|---|---|
| **Fisica** | Restringir acceso fisico a instalaciones y areas criticas | Control biometrico, tarjetas inteligentes, CCTV y analitica de video, zonificacion, barreras fisicas, sensores ambientales (disponibilidad) | ISO 27001 A.11; NIST SP 800-53 PE; HIPAA §164.310; Ley 21.663 Art. 3-4; Ley 19.628 |
| **Red** | Prevenir accesos no autorizados y segmentar la red | NGFW, filtrado de paquetes, IDS/IPS, VLANs y microsegmentacion, VPN seguras | ISO 27001 A.13; NIST SP 800-53 SC; HIPAA §164.312(e); Ley 21.663 Art. 7; Ley 19.628 |
| **Perimetro** | Proteger los puntos de entrada a la red institucional | WAF, Proteccion DDoS, Proxy inversos, Gateway remoto seguro | ISO 27001 A.13; NIST SP 800-53 SC-5; HIPAA §164.312(b); Ley 21.663 Art. 7; OWASP Top 10 |
| **Aplicacion** | Desarrollar y mantener aplicaciones seguras | SSDLC (OWASP/NIST), SAST/DAST, pentesting, Gestion segura de APIs (OAuth2, TLS 1.2+), Controles frontend (XSS, CSRF, validacion, HTTPS) | ISO 27001 A.14; NIST SP 800-218 (SSDF); HIPAA §164.312(c); Ley 21.663 Art. 8; Ley 19.628 Art. 4 |
| **Datos** | Proteger informacion en reposo y en transito | Cifrado AES-256, TLS 1.2+, Firmas digitales, Clasificacion de datos, MFA, OAuth2, SAML, DLP, backups seguros | ISO 27001 A.8, A.10, A.18; NIST SP 800-57/111/88; HIPAA §164.312(a-c); Ley 21.663 Art. 3-4; Ley 19.628 |
| **Endpoints** | Proteger dispositivos que acceden a la red y datos | Antivirus/Antimalware, EDR/XDR, Gestion de parches, Control de USB, MDM/UEM | ISO 27001 A.12, A.13; NIST SP 800-171; HIPAA §164.310(d); Ley 21.663 Art. 9 |
| **Operacional y Monitoreo** | Detectar y responder a amenazas en tiempo real | Monitoreo continuo, SIEM, SOC 24/7, CTI (Cyber Threat Intelligence), Pentesting, auditorias, DRP | ISO 27001 A.16, A.12.4, A.17; NIST SP 800-137; HIPAA §164.308(a)(6); Ley 21.663 Art. 10-11 |
| **Nube** | Asegurar la proteccion de recursos en entornos cloud | IAM, CSPM, Cifrado en transito y reposo, SLA con proveedores, Monitoreo de uso y amenazas en la nube, Cumplimiento y gobernanza | ISO 27001 A.5.19, A.5.23, A.5.30; NIST SP 800-144; NIST SP 800-53 AC, SC, AU; CIS Controls v8; Ley 21.663; Ley 19.628 Art. 8 |

## 6.1.10. Amenazas Ciberneticas en el Sector Salud

| Tipo de Ataque | Impactos Potenciales | Controles Clave para Mitigacion |
|---|---|---|
| **Ransomware** | Interrupcion de servicios clinicos criticos (HIS, PACS, LIS); Perdida de acceso a datos esenciales para atencion medica; Costos financieros por rescate, recuperacion y multas regulatorias; Daño reputacional significativo | Copias de datos cifradas y segregadas (ISO 27001 A.12.3); EDR/XDR con capacidad de contencion automatica; Segmentacion de red y control de trafico lateral (NIST SP 800-207); Plan de respuesta ante incidentes (ISO 27035); Parches y actualizaciones periodicas |
| **Ataques a la Cadena de Suministro** | Introduccion de malware en sistemas de mision critica; Compromiso de datos sensibles; Impacto indirecto en la confiabilidad de la atencion medica | Evaluacion continua de proveedores (ISO 27001 A.15); Requisitos de seguridad en contratos (Ley 21.663, CIS v8 Control 15.1); Gestion de riesgos de terceros (NIST SP 800-161); Control de acceso minimo necesario; Aislamiento de entornos criticos |
| **Robo de Datos de Pacientes** | Multas severas por incumplimiento de normativas de privacidad; Litigios legales; Perdida de confianza de los pacientes y del publico | Cifrado en reposo y en transito (ISO 27001 A.10); Gestion de identidad y acceso (IAM) robusta; DLP (prevencion de fuga de datos); Auditoria y monitoreo continuo (SIEM); Concientizacion y capacitacion en privacidad |
| **Ataques a Dispositivos Medicos (IoT/IoMT)** | Riesgo directo para la seguridad y la vida de los pacientes; Interrupciones en procedimientos medicos criticos; Potencial de litigios legales graves | Gestion de inventario de activos medicos (ISO 27001 A.8); Segmentacion de red para dispositivos IoMT; Control de firmware y actualizaciones seguras; Evaluaciones de seguridad periodicas; Supervision continua del comportamiento de dispositivos |
| **Ingenieria Social (Phishing y Spear Phishing)** | Acceso no autorizado a sistemas clinicos; Instalacion de ransomware o spyware; Compromiso de redes internas y bases de datos sensibles | Programas de concientizacion y simulacros de phishing; Autenticacion multifactor (MFA); Filtros de correo y sandboxing; Politica de minimo privilegio; Monitoreo de accesos |
| **Ataques de Denegacion de Servicio (DDoS)** | Caida de plataformas de telemedicina, urgencias o sistemas administrativos; Afectacion directa a la calidad de la atencion medica; Perdida de ingresos y deterioro de la imagen institucional | Servicios de mitigacion DDoS (WAF y CDN con capacidad de absorcion); Alta disponibilidad y redundancia (ISO 27001 A.17); Plan de continuidad operativa y DRP; Monitorizacion de trafico en tiempo real |

## 7. Proteccion de los Activos Criticos

Los activos criticos son aquellos elementos clave cuya afectacion puede impactar gravemente la calidad de los servicios de salud, la seguridad de los pacientes y la continuidad de operaciones.

### 7.1. Identificacion de Activos Criticos

| Categoria | Ejemplos |
|---|---|
| Datos sensibles | Informacion personal de pacientes, registros medicos, diagnosticos, tratamientos |
| Sistemas y plataformas | Sistemas de gestion hospitalaria, EMR, plataformas de administracion de citas |
| Infraestructura tecnologica | Servidores, bases de datos, redes, dispositivos de almacenamiento, sistemas de respaldo |
| Dispositivos medicos conectados | Respiradores, monitores cardiacos, dispositivos de imagenes, bombas de infusion, marcapasos |

### 7.2. Clasificacion de Activos y Niveles de Criticidad

| Nivel | Descripcion | Ejemplos |
|---|---|---|
| **Critico (C1)** | Su indisponibilidad, alteracion o fuga paraliza la operacion institucional, afecta gravemente la atencion clinica o expone datos personales sensibles | Historia Clinica Electronica, Core HIS, Sistema de Imagenologia (RIS/PACS), ERP institucional, plataformas de telemedicina, bases de datos maestras, sistemas de administracion de medicamentos |
| **Alto (C2)** | Su indisponibilidad afecta significativamente procesos operativos o de soporte | Sistemas de agenda, laboratorio (LIS), gestion documental, correo institucional, portales ciudadanos |
| **Medio (C3)** | Su indisponibilidad es tolerable por tiempos definidos sin afectar la seguridad o integridad del paciente o la institucion | Portales informativos, intranet, sistemas de apoyo no criticos |
| **Bajo (C4)** | No afecta procesos misionales y su uso es complementario | Sistemas de capacitacion, encuestas internas, aplicativos no sensibles |

### 7.3. Controles para la Proteccion de los Activos Criticos

#### 7.3.1. Control de Acceso

| Control | Especificacion |
|---|---|
| Autenticacion Multifactor (MFA) | Obligatorio para sistemas y activos criticos; al menos dos metodos de verificacion; integrado con IAM centralizado |
| Autorizacion Basada en Roles (RBAC) | Permisos asignados por roles; principio de minimo privilegio; ACLs detalladas a nivel de sistemas, aplicaciones y bases de datos |
| Gestion de Cuentas y Credenciales | Contrasenas complejas con rotacion; gestores de contrasenas empresariales; bloqueo automatico tras intentos fallidos; monitoreo de cuentas privilegiadas |
| Control de Acceso a la Red | Segmentacion con VLANs y microsegmentacion; firewalls internos con reglas especificas; listas blancas de IPs y puertos |
| Seguridad en Dispositivos Medicos | Autenticacion y control de acceso propios; VLANs dedicadas o firewalls restrictivos |
| Gestion de Vulnerabilidades | Proceso continuo de identificacion, clasificacion y correccion; herramientas automatizadas de escaneo; parches proactivos |

#### 7.3.2. Proteccion de Datos

| Control | Especificacion |
|---|---|
| Cifrado de Datos | AES-256 o superior; gestion segura de claves (HSM); TLS 1.2+ para trafico web y transferencia de datos; certificados digitales configurados correctamente |
| Prevencion de Perdida de Datos (DLP) | Herramientas de software DLP; politicas basadas en clasificacion de informacion; monitoreo de transferencia de archivos, correo y otros canales |
| Integridad de los Datos | Checksums, hashes criptograficos, firmas digitales; sistema de control de versiones; registros de auditoria de todas las modificaciones |
| Monitoreo Continuo | Supervision en tiempo real de actividad de sistemas y red; alertas para identificar y responder rapidamente |
| Analisis de Logs | SIEM centralizado; correlacion de eventos; deteccion de patrones anomalos; alertas tempranas |
| Pruebas de Penetracion | Periodicas en sistemas e infraestructura que soportan activos criticos; simulacion de ataques reales |

#### 7.3.3. Seguridad de la Infraestructura

| Control | Especificacion |
|---|---|
| Fortalecimiento (Hardening) | Configuracion segura de SO y aplicaciones; desactivar servicios y funcionalidades no esenciales; permisos correctos de archivos y directorios |
| Gestion de Parches y Vulnerabilidades | Proceso robusto; herramientas automatizadas; escaneos periodicos |
| Proteccion Antimalware Avanzada | Deteccion basada en comportamiento; sandboxing; analisis en tiempo real en endpoints y servidores |
| Registros y Monitoreo (Logging y SIEM) | Registro detallado de actividad; centralizacion en SIEM; deteccion de comportamientos anomalos; alertas automaticas |

#### 7.3.4. Resiliencia y Recuperacion

| Control | Especificacion |
|---|---|
| Respaldos Regulares (Backups) | Automaticos y periodicos; almacenamiento en ubicaciones separadas geograficamente; regla 3-2-1 (3 copias, 2 medios, 1 fuera del sitio); pruebas de restauracion automaticas |
| Planes de Recuperacion ante Desastres (DRP) | Identificacion de activos esenciales; definicion de RTO y RPO; sitios de respaldo (frio, tibio, caliente) segun criticidad; simulacros periodicos; actualizacion ante cambios |
| Plan de Respuesta ante Incidentes | Procedimientos claros para identificacion, contencion, erradicacion y recuperacion de activos criticos; roles y responsabilidades definidos; equipo capacitado |

#### 7.3.5. Seguridad en la Nube

| Control | Especificacion |
|---|---|
| Configuracion Segura de Servicios Cloud | Directrices de seguridad del proveedor; IAM especifico para cloud; reglas de firewall y grupos de seguridad; opciones de cifrado del proveedor |
| Monitorizacion de la Seguridad en la Nube | Herramientas nativas del proveedor; alertas para eventos de seguridad; integracion de registros con SIEM centralizado |

### 7.4. Matriz de Controles por Nivel de Criticidad de Activos

| Control/Requisito | Tipo | C1 (Critico) | C2 (Alto) | C3 (Medio) | C4 (Bajo) |
|---|---|---|---|---|---|
| Autenticacion Multifactor (MFA) | Acceso | Obligatorio | Obligatorio | Recomendado | Opcional |
| Autorizacion Basada en Roles y Atributos (RBAC) | Acceso | Obligatorio | Obligatorio | Recomendado | Opcional |
| Gestion de Cuentas y Credenciales | Acceso | Obligatorio | Obligatorio | Recomendado | Opcional |
| Control de Acceso a la Red (Segmentacion) | Red | Obligatorio | Obligatorio | Recomendado | Opcional |
| Seguridad en Dispositivos Medicos | Dispositivo | Obligatorio | Obligatorio | Recomendado | Opcional |
| Gestion de Parches y Vulnerabilidades | General | Obligatorio | Obligatorio | Recomendado | Opcional |
| Cifrado en transito y reposo (TLS 1.2+/AES-256) | Datos | Obligatorio | Obligatorio | Recomendado | Opcional |
| Prevencion de Perdida de Datos (DLP) | Datos | Obligatorio | Recomendado | Opcional | Opcional |
| Integridad de los Datos (Checksums, hashes, Firmas, Auditoria) | Datos | Obligatorio | Obligatorio | Recomendado | Opcional |
| Monitoreo Continuo | Seguridad | Obligatorio | Obligatorio | Recomendado | Opcional |
| Analisis de Logs (SIEM) | Seguridad | Obligatorio | Obligatorio | Recomendado | Opcional |
| Pruebas de Penetracion Periodicas | Seguridad | Obligatorio | Recomendado | Opcional | Opcional |
| Fortalecimiento de Sistemas y Aplicaciones (Hardening) | Sistemas | Obligatorio | Obligatorio | Recomendado | Opcional |
| Gestion de Parches y Vulnerabilidades | Sistemas | Obligatorio | Obligatorio | Recomendado | Opcional |
| Antimalware Avanzada | Servidores | Obligatorio | Obligatorio | Recomendado | Opcional |
| Registros y Monitoreo de Seguridad (Logging y SIEM) | Seguridad | Obligatorio | Obligatorio | Recomendado | Opcional |
| Copias de respaldo con prueba de restauracion | Respaldo | Obligatorio | Obligatorio | Recomendado | Opcional |
| Planes de Recuperacion ante Desastres (DRP) | Respaldo | Obligatorio | Obligatorio | Recomendado | Opcional |
| Plan de Respuesta ante Incidentes | Respaldo | Obligatorio | Obligatorio | Recomendado | Opcional |
| Configuracion Segura de Servicios Cloud | Nube | Obligatorio | Recomendado | Recomendado | Opcional |
| Monitorizacion de la Seguridad en la Nube | Nube | Obligatorio | Recomendado | Recomendado | Opcional |
| Revision anual de contratos y clausulas de seguridad | Contratos | Obligatorio | Obligatorio | Recomendado | Opcional |
| Evaluacion de codigo seguro (OWASP, SAST/DAST) | Seguridad | Obligatorio | Recomendado | Opcional | Opcional |

## 8. Proteccion de Informacion

### 8.1. Clasificacion de la Informacion

Categorias minimas de clasificacion:

| Categoria | Descripcion |
|---|---|
| Publica | Informacion de acceso libre |
| Uso Interno | Informacion de circulacion restringida al personal institucional |
| Confidencial | Informacion cuyo acceso no autorizado puede causar daño significativo |
| Informacion Sensible de Salud | Datos clinicos y de salud protegidos por ley |

Debe estar documentada, difundida y aplicada transversalmente.

### 8.2. Control de Acceso a la Informacion

| Directriz | Especificacion |
|---|---|
| Principio de privilegio minimo | Cada usuario accede unicamente a la informacion necesaria para sus funciones |
| Autenticacion fuerte | MFA obligatorio en sistemas con informacion critica o sensible |
| Registro y monitoreo | Todos los accesos deben ser registrados, monitoreados y auditados de forma continua |

### 8.3. Proteccion en Transito y en Reposo

| Control | Especificacion |
|---|---|
| Cifrado en reposo | AES-256 o RSA-4096, u otros algoritmos aprobados en politica de criptografia |
| Cifrado en transito | TLS 1.2 o superior como estandar minimo; HTTPS con certificados de entidades acreditadas en el pais |
| Prohibicion de canales inseguros | Correos electronicos sin cifrado, dispositivos de almacenamiento portatiles sin proteccion |
| Proteccion de contrasenas | Almacenamiento con bcrypt, PBKDF2, Argon2 |
| Monitoreo de vulneraciones | Controles tecnicos y administrativos para deteccion temprana de intentos de vulneracion del sistema de cifrado; sistemas configurados para seleccionar siempre la opcion de cifrado mas segura |
| Gestion de claves criptograficas | Sistemas seguros para generacion, almacenamiento y rotacion periodica |

### 8.4. Almacenamiento y Resguardo

| Directriz |
|---|
| Almacenar unicamente en infraestructuras autorizadas por MINSAL, con estandares de seguridad y ubicacion geografica bajo jurisdiccion nacional (salvo autorizacion expresa) |
| Sistemas de respaldo deben garantizar recuperacion segura e integra ante incidentes o fallas |

### 8.5. Eliminacion y Destruccion Segura

| Directriz | Especificacion |
|---|---|
| Prohibicion de borrado sin autorizacion | Informacion clinica en ficha clinica, resultados de examenes, recetas, licencias medicas no pueden ser borrados sin autorizacion expresa y por escrito de la direccion medica del establecimiento |
| Metodos de borrado seguro | Sobre escritura multiple con herramientas certificadas (borrado logico); trituracion, desmagnetizacion o incineracion (destruccion fisica); conforme NIST SP 800-88 Rev. 1, ISO/IEC 27040 |
| Registro obligatorio | Actas o bitacoras especificando tipo de datos, metodo, responsables y fecha; conservar segun politica de retencion documental |
| Instruccion explicita del mandante | Toda modificacion, cancelacion o destruccion requiere instruccion explicita del mandante, documentada y vinculada al acta |
| Terceros procesadores | Responsables de ejecutar eliminacion conforme a lineamientos contractuales y regulatorios, con constancia formal de cada etapa |
| Dispositivos descartados | Formateo o sanitizacion segura obligatoria; prohibido reutilizar equipos con datos sensibles sin limpieza certificada |
| Proyectos de digitalizacion | Prohibido que proveedores eliminen o destruyan documentos originales sin autorizacion formal del mandante, debidamente documentada |

### 8.6. Proteccion en Entornos de Nube

| Directriz | Especificacion |
|---|---|
| Cláusulas contractuales | Obligatorias: confidencialidad, integridad, disponibilidad; cumplimiento Ley 21.719, Ley 21.663; alineadas con Instructivo sobre Cláusulas de Proteccion de Datos y Seguridad del MINSAL |
| Encriptacion de Datos | AES-256 en reposo; TLS 1.3 en transito; claves criptograficas en HSM; MFA para acceso a claves y sistemas con datos cifrados |
| Seudonimizacion | Datos personales sensibles: conservar codigos de reidentificacion en servidores locales; tokenizacion y enmascaramiento recomendados; claves de seudonimizacion en sistemas separados |
| Elasticidad | Servicios contratados elasticos con escalado automatico; contratos con margenes de crecimiento sin nuevas licitaciones |
| Garantia de Disponibilidad | Alta disponibilidad (HA) con recursos en multiples regiones/zonas; planes BCP/DRP alineados con estandares internacionales |
| Geolocalizacion y Proteccion | Tratamiento de datos de geolocalizacion limitado a lo estrictamente necesario; cifrado en transito y reposo; controles de acceso restringido; trazabilidad mediante registros de tratamiento y accesos; auditorias periodicas |
| Automatizacion de Respaldos | Respaldos automatizados en nube con pruebas regulares de restauracion |
| Distribucion de Copias | Multiples regiones, al menos una en infraestructura ubicada en Chile; evitar replicacion automatica fuera del pais o controlarla estrictamente; enfoque hibrido recomendado: copia primaria en infraestructura propia + secundaria en nube publica |
| Monitoreo y Registro de Eventos | Logs detallados en todas las capas; herramientas de gestion de parches; alertas de vulnerabilidades criticas; auditar: autenticaciones, eventos de red sospechosos, modificaciones en configuraciones y permisos, accesos a datos sensibles |
| WAF | Delante de aplicaciones web expuestas; inspeccion HTTP/HTTPS; reglas contra XSS, SQLi, RFI; personalizacion de reglas; integracion con SIEM |
| Proteccion DDoS | Infraestructura protegida contra saturacion; servicios de mitigacion con identificacion de patrones anomalos y redireccion de ataques; proteccion a nivel de red y aplicacion |
| Inteligencia de Amenazas e IoCs | Integracion de fuentes de Threat Intelligence con SIEM/XDR; respuestas automatizadas ante detecciones criticas |
| Politicas IAM (Minimos Privilegios) | Permisos minimos necesarios; roles agrupados por responsabilidades laborales; auditorias periodicas de politicas IAM |
| ZTNA (Zero Trust Network Access) | Verificacion rigurosa basada en identidad, contexto (ubicacion, hora, dispositivo) y cumplimiento de politicas; microsegmentacion |
| MFA | Obligatorio para acceso a consola de administracion, servicios cloud y recursos sensibles; al menos dos factores (TOTP, hardware token, biometria) |
| SASE | Evaluar e implementar: integracion de seguridad cloud con SD-WAN; FWaaS, SWG, CASB, ZTNA |
