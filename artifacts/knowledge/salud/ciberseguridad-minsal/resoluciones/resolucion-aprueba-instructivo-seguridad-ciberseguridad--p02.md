---
_manifest:
  urn: urn:salud:kb:resolucion-aprueba-instructivo-seguridad-ciberseguridad-p02
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
    shard_index: 2
    shard_count: 4
    shard_root_urn: urn:salud:kb:resolucion-aprueba-instructivo-seguridad-ciberseguridad
relations:
  cites:
  - urn:salud:kb:politica-general-seguridad-informacion-ciberseguridad
---

# Resolucion Exenta RES_853 - Aprueba Instructivo de Seguridad de la Informacion y Ciberseguridad para el Sector Salud ITS-NC-007-V.2.0, Abril 2025 - Parte 02

## Arquitectura de Seguridad de la Informacion y Ciberseguridad

Cada institucion debe implementar un Modelo de Seguridad por Capas (Defensa en Profundidad), basado en el principio de seguridad y privacidad por defecto y desde el diseno (Ley N°21.663, Ley N°19.628, Ley N°20.584).

#### Capa de Seguridad Fisica

| Control | Especificacion |
| --- | --- |
| Control de acceso biometrico y tarjetas inteligentes | Lectores biometricos (huella, iris), tarjetas RFID personalizadas |
| Videovigilancia (CCTV) | Perimetral y en zonas criticas, con grabacion, analitica de video y alertas |
| Zonificacion fisica | Zonas de seguridad diferenciadas, barreras fisicas, jaulas de racks, salas blancas para TI |
| IDS fisicos | Deteccion de intrusos para alertar accesos no autorizados |
| Sensores ambientales | Control de temperatura, humedad y alimentacion electrica (SAI/UPS, generadores) |
| Detectores | Humo, humedad, temperatura y fallos electricos conectados a BMS |

#### Capa de Seguridad de Red

| Control | Especificacion |
| --- | --- |
| Firewalls de ultima generacion (NGFW) | Inspeccion profunda de paquetes (DPI), filtrado por aplicacion, geo-bloqueo, listas blancas/negras IP |
| Proteccion avanzada | Analisis de trafico cifrado (SSL/TLS), IPS, sandboxing para malware desconocido |
| IDS/IPS | Monitoreo de trafico, deteccion de actividades sospechosas, bloqueo/alertas |
| ACLs | En enrutadores y switches, restriccion de comunicaciones entre segmentos |
| Segmentacion de red | VLANs, subredes, arquitecturas Zero Trust, microsegmentacion para aislar sistemas criticos, redes clinicas, administrativas, loT y visitantes |
| VPNs seguras | Cifrado IPsec o SSL, autenticacion robusta, tuneles cifrados por usuario/dispositivo |
| Filtrado de contenido | Politicas de filtrado web y correo electronico |
| Monitoreo de trafico | Continuo, deteccion de anomalias en tiempo real |

#### Capa de Seguridad del Perimetro

| Control | Especificacion |
| --- | --- |
| WAF | Proteccion de aplicaciones web contra SQL injection, XSS |
| Proteccion DDoS | Sistemas dedicados o servicios cloud para mitigar ataques |
| Filtrado de contenido web | Bloqueo de sitios maliciosos y categorias inapropiadas |
| UTM | Integracion de firewall, IPS, antivirus gateway, filtrado web |
| Acceso remoto seguro | VPNs con autenticacion fuerte y cifrado, control de origen |
| Monitoreo y alertas | Integracion con SIEM |

#### Capa de Aplicacion

| Control | Especificacion |
| --- | --- |
| Ciclo de Vida de Desarrollo Seguro (SSDLC) | Autenticacion, autorizacion, pruebas de seguridad. Estandares OWASP, NIST. |
| Validacion de entradas | Prevencion de SQL Injection, XSS, CSRF. Uso de procedimientos almacenados y consultas preparadas. |
| Codificacion segura | Guias OWASP Top Ten |
| Control de acceso | Autenticacion y autorizacion basada en roles (RBAC) |
| Gestion segura de sesiones | Identificadores robustos, proteccion anti-secuestro, invalidacion al cierre |
| Pruebas de seguridad | Pentesting, SAST (analisis estatico), DAST (analisis dinamico) |
| Manejo seguro de errores | Sin divulgacion de informacion sensible o detalles internos |
| Cifrado de datos sensibles | Dentro de la aplicacion |
| Registros de auditoria | Logs detallados de actividad |
| Proteccion de datos sensibles | Cifrado en transito y reposo, anonimizacion/seudonimizacion, enmascaramiento en entornos no productivos |
| Gestion segura de APIs | OAuth 2.0, autorizacion granular, TLS 1.2+, proteccion OWASP API Top 10, validacion de entradas, rate limiting, trazabilidad completa |
| APIs REST | Autenticacion privada mediante tokens (JWT), certificados, llaves criptograficas |

#### Capa de Seguridad de los Datos

| Control | Especificacion |
| --- | --- |
| Autenticacion fuerte | MFA cuando sea posible |
| Cifrado en reposo | AES-256, gestion segura de claves criptograficas |
| Cifrado en transito | TLS 1.2 o superior |
| Firmas digitales | Criptografia de clave publica. Instrumentos publicos con Firma Electronica Avanzada. |
| DLP | Monitoreo y control de movimiento de informacion sensible |
| Anonimizacion y seudonimizacion | Tecnicas para reducir riesgo de identificacion directa |
| Politicas de retencion y eliminacion | Segun requisitos legales y de negocio, con procedimientos seguros |
| Auditoria de acceso a datos | Registro de accesos, modificaciones y eliminaciones |
| Clasificacion y etiquetado | Etiquetas automatizadas y manuales para categorizar y aplicar politicas |
| Autorizacion | ACLs, RBAC y ABAC consistentes en aplicacion e infraestructura |
| Sistemas de respaldo automatizados | Backups periodicos locales y cloud, pruebas regulares de recuperacion (DRP/BIA) |

#### Capa de Seguridad de Dispositivos y Endpoints

| Control | Especificacion |
| --- | --- |
| Antimalware avanzado (NGAV) | Deteccion en tiempo real, analisis heuristico, proteccion contra amenazas emergentes, deteccion basada en comportamiento |
| EDR/XDR | Monitoreo continuo de endpoints, deteccion temprana, respuesta automatizada. Integracion con SIEM. |
| Firewall personal | En todos los dispositivos |
| MDM/UEM | Politicas de seguridad, configuracion, inventario, control de apps/datos, borrado remoto |
| Control de acceso al dispositivo | Autenticacion fuerte, bloqueo automatico por inactividad |
| Cifrado de disco completo | En portatiles y dispositivos con informacion sensible |
| Gestion de parches | Centralizada y automatizada para SO, aplicaciones y firmware |
| Control de aplicaciones | Solo software autorizado |
| DLP en endpoint | Monitoreo y control de transferencia de informacion sensible |
| Control de dispositivos extraibles | Restriccion de USB no autorizados, registro de conexion, cifrado en dispositivos permitidos. Puertos USB deshabilitados por defecto. |
| BYOD | MDM/UEM obligatorio para dispositivos personales autorizados |

#### Capa de Seguridad Operacional y de Monitoreo

| Control | Especificacion |
| --- | --- |
| SOC o funciones equivalentes | Monitoreo continuo, analisis de alertas, gestion de incidentes |
| SIEM | Recopilacion, correlacion y analisis de logs de todas las fuentes |
| Monitoreo continuo | Salud, rendimiento y seguridad de infraestructura, red, servidores, aplicaciones, bases de datos |
| Alertas en tiempo real | Notificacion inmediata al personal de seguridad |
| Procesos de gestion de incidentes | Documentados: identificacion, analisis, contencion, erradicacion, recuperacion, lecciones aprendidas |
| IRT (Equipo de Respuesta a Incidentes) | Roles y responsabilidades definidos |
| Inteligencia de amenazas (CTI) | Integrada en monitoreo y analisis |
| Analisis forense | Capacidades para investigar incidentes, causas raiz, alcance, evidencias |
| Ejercicios y simulacros | Periodicos de respuesta a incidentes |
| Comunicacion de incidentes | Protocolos hacia alta direccion y ANCI |
| Pruebas de seguridad | Evaluaciones periodicas de vulnerabilidades, pentesting, SAST/DAST, auditorias, simulacros |

#### Capa de Seguridad en la Nube

Para instituciones que utilicen servicios cloud (IaaS, PaaS, SaaS), considerando el modelo de responsabilidad compartida:

| Control | Especificacion |
| --- | --- |
| IAM en la nube | Gestion centralizada de identidades, roles y permisos (AWS IAM, Azure AD, Google Cloud IAM). Principio de minimo privilegio. MFA obligatorio para cuentas con privilegios. |
| CSPM | Monitoreo continuo de configuracion, alertas automaticas ante configuraciones inseguras, flujos de remediacion. |
| Seguridad de red cloud | VPC/VNet, subredes logicas, firewalls virtuales (Grupos de Seguridad, ACLs), segmentacion robusta, conectividad hibrida con VPN/Direct Connect. |
| Proteccion de datos cloud | Cifrado en reposo (KMS) y en transito (TLS 1.2+), politicas de retencion y eliminacion conforme Ley N°19.628, DLP. |
| Monitorizacion y registro cloud | AWS CloudWatch, Azure Monitor, Google Cloud Logging, integracion con SIEM centralizado. |
| Seguridad de cargas de trabajo | Hardening de SO en instancias, EDR/XDR cloud, escaneo de vulnerabilidades en contenedores, politicas de seguridad en Kubernetes, SDLC seguro para FaaS. |
| Cumplimiento y gobernanza cloud | Politicas para cumplir Ley N°21.663 y Ley N°19.628, auditorias periodicas, herramientas de compliance automatizadas. |
| Consideraciones adicionales | Comprender modelo de responsabilidad compartida, seleccion de proveedores con cumplimiento sectorial, evaluacion continua. |

## Tabla de cumplimiento por capas (referencias)

| Capa | Referencias principales |
| --- | --- |
| Fisica | ISO 27001 A.11; NIST SP 800-53 PE; HIPAA 164.310; Ley 21.663 Art. 9; Ley 19.628 |
| Red | ISO 27001 A.13; NIST SP 800-53 SC; HIPAA 164.312(e); Ley 21.663 Art. 7; Ley 19.628 |
| Perimetro | ISO 27001 A.13; NIST SP 800-53 SC-5; HIPAA 164.312(b); Ley 21.663 Art. 7; OWASP Top 10 |
| Aplicacion | ISO 27001 A.14; NIST SP 800-218 (SSDF); HIPAA 164.312(c); Ley 21.663 Art. 8; Ley 19.628 Art. 4 |
| Datos | ISO 27001 A.8, A.10, A.18; NIST SP 800-57/111/88; HIPAA 164.312(a-c); Ley 21.663 Art. 3-4; Ley 19.628 Art. 7-8 |
| Endpoints | ISO 27001 A.12, A.13; NIST SP 800-171; HIPAA 164.310(d); Ley 21.663 Art. 9 |
| Operacional y Monitoreo | ISO 27001 A.16, A.12.4, A.17; NIST SP 800-137; HIPAA 164.308(a)(6); Ley 21.663 Art. 10-11 |
| Nube | ISO 27001 A.5.19, A.5.23, A.5.30; NIST SP 800-144; NIST SP 800-53 AC, SC, AU; CIS Controls v8; Ley 21.663 Art. 7; Ley 19.628 Art. 8 |

## Amenazas Ciberneticas en el Sector Salud

| Tipo de Ataque | Impactos Potenciales | Controles Clave |
| --- | --- | --- |
| Ransomware | Interrupcion de servicios clinicos criticos, perdida de acceso a datos, costos financieros, dano reputacional | Copias de datos cifradas y segregadas, EDR/XDR, segmentacion de red, IRP, parches periodicos |
| Ataques a la Cadena de Suministro | Introduccion de malware en sistemas criticos, compromiso de datos sensibles | Evaluacion continua de proveedores, requisitos de seguridad en contratos, gestion de riesgos de terceros, control de acceso minimo, aislamiento de entornos criticos |
| Robo de Datos de Pacientes | Multas por incumplimiento de privacidad, litigios, perdida de confianza | Cifrado en reposo y transito, IAM robusta, DLP, auditoria continua (SIEM), capacitacion en privacidad |
| Ataques a Dispositivos Medicos | Riesgo directo a seguridad y vida de pacientes, interrupcion de procedimientos, litigios | Inventario de activos medicos, segmentacion de red para loMT, control de firmware, evaluaciones periodicas, supervision continua |
| Ingenieria Social (Phishing/Spear Phishing) | Acceso no autorizado, instalacion de ransomware/spyware, compromiso de redes y bases de datos | Programas de concientizacion, simulacros de phishing, MFA, filtros de correo/sandboxing, politica de minimo privilegio, monitoreo de accesos inusuales |
| DDoS | Caida de plataformas de telemedicina/urgencias, afectacion a la atencion, perdida de ingresos, deterioro de imagen | Servicios de mitigacion DDoS (WAF y CDN), alta disponibilidad y redundancia, DRP, monitorizacion en tiempo real |

## Proteccion de los Activos Criticos

### Identificacion de Activos Criticos

Activos criticos incluyen:
- **Datos sensibles**: informacion personal de pacientes, historiales medicos, diagnosticos, tratamientos.
- **Sistemas y plataformas**: sistemas de gestion hospitalaria, EMR, plataformas de administracion de citas.
- **Infraestructura tecnologica**: servidores, bases de datos, redes, almacenamiento, sistemas de respaldo.
- **Dispositivos medicos conectados**: respiradores, monitores cardiacos, dispositivos de imagenes.

### Clasificacion de Activos por Nivel de Criticidad

| Nivel | Descripcion | Ejemplos |
| --- | --- | --- |
| Critico (C1) | Su compromiso interrumpe la operacion o expone datos personales sensibles | Historia Clinica Electronica, Core HIS |
| Alto (C2) | Su fallo tiene impacto relevante en procesos operativos o de soporte | Sistemas de agenda, LIS, gestion documental, correo institucional, portales ciudadanos |
| Medio (C3) | Su indisponibilidad es tolerable por tiempos definidos sin afectar seguridad del paciente o la institucion | Portales informativos, intranet, sistemas de apoyo no criticos |
| Bajo (C4) | No afecta procesos misionales, uso complementario | Sistemas de capacitacion, encuestas internas, aplicativos no sensibles |

### Matriz de Controles por Nivel de Criticidad

| Control/Requisito | Tipo | C1 (Critico) | C2 (Alto) | C3 (Medio) | C4 (Bajo) |
| --- | --- | --- | --- | --- | --- |
| MFA | Acceso | Obligatorio | Obligatorio | Recomendado | Opcional |
| RBAC | Acceso | Obligatorio | Obligatorio | Obligatorio | Opcional |
| Gestion de cuentas y credenciales | Acceso | Obligatorio | Obligatorio | Recomendado | Opcional |
| Control de acceso a red (segmentacion) | Red | Obligatorio | Obligatorio | Obligatorio | Opcional |
| Seguridad en dispositivos medicos | Dispositivo | Obligatorio | Obligatorio | Opcional | Opcional |
| Gestion de parches y vulnerabilidades | General | Obligatorio | Obligatorio | Obligatorio | Opcional |
| Cifrado en transito y reposo (TLS 1.2+/AES-256) | Datos | Obligatorio | Obligatorio | Obligatorio | Opcional |
| DLP | Datos | Obligatorio | Recomendado | Opcional | Opcional |
| Integridad de datos (checksums, hashes, firmas, auditoria) | Datos | Obligatorio | Obligatorio | Recomendado | Opcional |
| Monitoreo continuo | Monitoreo | Obligatorio | Obligatorio | Recomendado | Opcional |
| SIEM | Monitoreo | Obligatorio | Recomendado | Opcional | Opcional |
| Pruebas de penetracion periodicas | Seguridad | Obligatorio | Recomendado | Opcional | Opcional |
| Hardening (SO y aplicaciones) | Sistemas | Obligatorio | Obligatorio | Recomendado | Opcional |
| Antimalware avanzada | Endpoints/Servidores | Obligatorio | Obligatorio | Obligatorio | Obligatorio |
| Backups con prueba de restauracion | Respaldo | Obligatorio | Obligatorio | Obligatorio | Opcional |
| DRP | Respaldo | Obligatorio | Recomendado | Opcional | Opcional |
| IRP | Respuesta | Obligatorio | Obligatorio | Obligatorio | Opcional |
| Configuracion segura cloud | Nube | Obligatorio | Obligatorio | Recomendado | Opcional |
| Monitorizacion cloud | Nube | Obligatorio | Obligatorio | Recomendado | Opcional |
| Revision anual de contratos y clausulas | Contratos | Obligatorio | Obligatorio | Recomendado | Opcional |
| Evaluacion de codigo seguro (OWASP, SAST/DAST) | Seguridad | Obligatorio | Obligatorio | Recomendado | Opcional |

## Proteccion de Informacion

### Clasificacion de la Informacion

Categorias minimas: Publica, Uso Interno, Confidencial, Informacion Sensible de Salud. Documentada, difundida y aplicada transversalmente.

### Control de Acceso a la Informacion

- Principio de privilegio minimo.
- Autenticacion fuerte obligatoria (MFA) en sistemas con informacion critica o sensible.
- Todos los accesos registrados, monitoreados y auditados.

### Proteccion en Transito y en Reposo

- Informacion cifrada en reposo y en transito con algoritmos aprobados (NIST, ISO/IEC).
- Proteccion criptografica de credenciales, bases de datos y transmision de informacion sensible.
- Prohibido el uso de canales inseguros para informacion sensible (correos sin cifrado, dispositivos portatiles sin proteccion).
- HTTPS con certificados de entidades acreditadas para todos los sitios y sistemas web.
- TLS 1.2 o superior como estandar minimo.
- Cifrado en reposo: AES-256 o RSA-4096. Gestion segura de claves criptograficas.
- Almacenamiento de contrasenas: bcrypt, PBKDF2, Argon2.
- Controles para deteccion temprana de intentos de vulneracion del cifrado.

### Almacenamiento y Resguardo

- Solo en infraestructuras autorizadas por MINSAL, con estandares de seguridad y ubicacion geografica bajo jurisdiccion nacional (salvo autorizacion expresa).
- Sistemas de respaldo que garanticen recuperacion segura e integra.

### Eliminacion y Destruccion Segura

- Bajo estandares estrictos, con trazabilidad, auditabilidad y cumplimiento de Ley N°21.719, Ley N°21.663, Ley N°20.584 y Decreto N°41 (Reglamento de Ficha Clinica).
- Informacion clinica de ficha clinica no podra ser borrada sin autorizacion expresa y por escrito de la direccion medica.
- Metodos seguros de borrado logico (sobreescritura multiple certificada) y destruccion fisica (trituracion, desmagnetizacion, incineracion) segun NIST SP 800-88 Rev. 1 e ISO/IEC 27040.
- Registro mediante actas o bitacoras: tipo de datos, metodo, responsables, fecha.
- Modificacion, cancelacion o destruccion solo bajo instruccion explicita del mandante documentada.
- Terceros (procesadores de datos) responsables de ejecutar eliminacion conforme a lineamientos contractuales y regulatorios.
- Dispositivos descartados deben someterse a formateo o sanitizacion segura. Prohibido reutilizar equipos con datos sensibles sin limpieza certificada.
- Prohibido que proveedores eliminen o destruyan originales sin autorizacion formal documentada.

### Proteccion en Entornos de Nube

- Exigir al proveedor niveles de seguridad equivalentes o superiores a la normativa nacional.
- Clausulas contractuales obligatorias sobre confidencialidad, integridad y disponibilidad, cumpliendo Ley N°21.719, Ley N°21.663 y alineadas con el Instructivo de Clausulas de Proteccion de Datos y Seguridad del MINSAL.
- Cifrado: AES-256 para datos en reposo, TLS 1.3 para datos en transito, claves en HSM, MFA para acceso a claves.
- Seudonimizacion: recomendada para datos personales sensibles, con codigos de reidentificacion en servidores locales. Tecnicas: tokenizacion, enmascaramiento. Claves de seudonimizacion en sistemas separados.
- Elasticidad: planificacion anticipada de capacidad, escalabilidad automatica, contratos con margenes de crecimiento.
- Alta disponibilidad (HA): recursos en multiples regiones/zonas, mecanismos de restauracion rapida (BCP/DRP).
- Geolocalizacion: tratamiento limitado a lo necesario. Si se procesa fuera de Chile, proteccion equivalente. Cifrado y controles de acceso restringido. Trazabilidad y auditorias periodicas.
- Respaldos automatizados con pruebas regulares de restauracion. Copias en multiples regiones (al menos una en Chile). Enfoque hibrido recomendado.
- Monitoreo y registro de eventos en todas las capas. Auditoria de: autenticaciones, eventos de red, modificaciones de configuracion, accesos a datos sensibles.
- Proteccion contra amenazas:
 - WAF delante de aplicaciones web, con reglas contra XSS, SQLI, RFI.
 - Proteccion DDoS a nivel de red y aplicacion con servicios de mitigacion.
 - Inteligencia de amenazas (Threat Intelligence) e IoCs integrados con SIEM/XDR, con respuestas automatizadas.
 - Politicas IAM de minimos privilegios y roles, con revision periodica.
 - ZTNA: verificacion rigurosa por identidad, contexto y cumplimiento de politicas de dispositivo. Microsegmentacion.
 - MFA obligatorio para consola de administracion cloud y recursos sensibles.
 - SASE: integracion de seguridad cloud con SD-WAN (FWaaS, SWG, CASB, ZTNA).

## Respuesta ante Incidentes y Continuidad Operacional

### Plan de Respuesta ante Incidentes (IRP)

Todas las instituciones del Sector Salud, publicas y privadas, obligadas a desarrollar, implementar y mantener un IRP conforme a Ley N°21.663, Decreto N°295/2024 y estandares internacionales. Debe coordinarse con la ANCI.

Etapas fundamentales del IRP:

| Etapa | Actividades |
| --- | --- |
| Preparacion | Definir roles y responsabilidades del equipo de respuesta. Realizar simulacros. Asegurar respaldo de sistemas y datos criticos. |
| Deteccion y notificacion | Monitoreo continuo con SIEM. Procedimientos para reporte inmediato de colaboradores. |
| Evaluacion y contencion | Evaluar naturaleza y alcance. Implementar medidas de contencion (desconexion de sistemas, revocacion de accesos). |
| Erradicacion | Eliminar amenazas y vulnerabilidades. Limpiar sistemas afectados. Aplicar parches. |
| Recuperacion | Restaurar sistemas segun procedimientos. Verificar que esten libres de amenazas. |
| Revision post-incidente | Analisis de lecciones aprendidas. Actualizar procedimientos. Informe detallado con causas, acciones, impacto y recomendaciones. |

### Comunicacion en Caso de Incidente

- Notificacion inmediata a responsables y equipos clave (TI, seguridad, gerencia).
- Comunicacion con autoridades competentes cuando haya violacion de datos sensibles u obligacion legal de reporte.
- Manejo de comunicacion con el publico y pacientes si el incidente afecta servicios.

### Reporte de Incidentes de Ciberseguridad

**Obligatoriedad** (Art. 3° Decreto N°295/2024): todos los organismos del Sector Salud que presten servicios esenciales deben reportar incidentes de impacto significativo a la ANCI.

**Plataforma oficial**: https://portal.anci.gob.cl/

**Canales alternativos de contingencia**: Telefono 1510, Correo ayuda@anci.gob.cl

**Procedimiento de reporte** (3 etapas secuenciales):

| Etapa | Plazo | Contenido |
| --- | --- | --- |
| Alerta Temprana | 3 horas desde deteccion | Informacion preliminar: naturaleza, alcance, impacto potencial |
| Segunda Notificacion | 72 horas desde confirmacion | Reporte detallado: evolucion, medidas de contencion/erradicacion, restauracion, impacto real, brechas de seguridad |
| Informe Final | 15 dias corridos desde alerta temprana | Resumen completo, causas, acciones, impacto total, lecciones aprendidas, medidas preventivas, recomendaciones |

**Coordinacion central**: las instituciones pueden coordinarse con el MINSAL a traves del CISO o de la Unidad de Seguridad de la Informacion y Ciberseguridad. Canales ministeriales: telefono 800 123 573, correo mas@minsal.cl, correo seguridadtic@minsal.cl.

### Confidencialidad de la Informacion de Incidentes

Toda la informacion en alertas, reportes e informes debe tratarse con maxima confidencialidad (Ley N°21.663). Se comparte unicamente con autoridades competentes y partes autorizadas.

### Continuidad Operacional

Cada institucion debe desarrollar un Plan de Continuidad de Negocio (BCP) integrado con un Plan de Recuperacion ante Desastres (DRP).

**Analisis de Impacto en el Negocio (BIA)**:
- Identificar funciones criticas que deben mantenerse operativas.
- Determinar RTO (Recovery Time Objective) y RPO (Recovery Point Objective) para cada servicio critico.

**Estrategias de respaldo y recuperacion**:
- Respaldos regulares en ubicaciones seguras (cloud o centros de datos redundantes).
- DRP detallado con restauracion de sistemas criticos, recuperacion de datos al RPO y reanudacion de servicios dentro del RTO.

**Planes de emergencia**: para desastres naturales, fallos de infraestructura, ciberataques. Procedimientos de evacuacion de datos y reubicacion temporal de servicios.

**Monitoreo de la continuidad**:
- Monitoreo en tiempo real de salud de sistemas criticos con alertas automaticas.
- Verificacion periodica de respaldos y procedimientos de recuperacion.
- Simulacros regulares.
