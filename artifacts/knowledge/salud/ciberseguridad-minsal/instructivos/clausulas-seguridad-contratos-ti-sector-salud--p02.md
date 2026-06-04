---
_manifest:
  urn: urn:salud:kb:clausulas-seguridad-contratos-ti-sector-salud-p02
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-04'
    source: MINSAL Chile, SGSI Nivel Central. ITS-NC-006 v5.0 (Marzo 2025). Clasificación
      TLP:BLANCO
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- ciberseguridad
- minsal
- contratos-ti
- proteccion-datos
- clausulas
- saas
- cloud
lang: es
extensions:
  kora:
    family: note
    shard_index: 2
    shard_count: 4
    shard_root_urn: urn:salud:kb:clausulas-seguridad-contratos-ti-sector-salud
  salud:
    minsal_id: ITS-NC-006
    minsal_version: '5.0'
    fecha_aprobacion: Marzo 2025
    clasificacion: TLP:BLANCO
relations:
  cites:
  - urn:salud:kb:instructivo-seguridad-informacion-ciberseguridad-sector-salud
  - urn:salud:kb:stack-tecnologico-seguridad-minsal
  - urn:salud:kb:arquitectura-referencia-desarrollo-sistemas-sector-salud
---

# Instructivo: Cláusulas de Protección de Datos y Seguridad de la Información para Contratos de Tecnologías del Sector Salud - Parte 02

## 7.1. Medidas Organizativas

### 7.1.1. Prohibición de Uso de la Información

Toda persona que entre en contacto con la información tiene calidad de mero procesador o mandatario. Puede utilizarla solo en cumplimiento de obligaciones contractuales. Proscrito el uso para fines distintos de los expresamente autorizados.

### 7.1.2. Acceso Restringido

Prohibido utilizar servicios de almacenamiento en nube o cualquier servicio de nube pública no autorizado previamente por el área de TI o el comité de ciberseguridad.

### 7.1.3. Auditorías Externas de Seguridad

| Elemento | Requisito |
|----------|-----------|
| Capacidad de auditar | Accesos, modificaciones, eliminaciones de datos; movimientos entre regiones de almacenamiento |
| Período de retención de logs | Mínimo **5 años**, accesibles para inspecciones internas o regulatorias |
| Herramientas automáticas | Supervisar actividades en la nube y generar reportes periódicos |

### 7.1.4. Notificación de Incidentes

- Notificar al Oficial de Seguridad de la Información en plazo máximo de **3 horas**.
- Resguardar evidencias iniciando cadena de custodia.
- Proveer detalles del incidente, medidas adoptadas y planes de mitigación.
- Los funcionarios deben reportar inmediatamente cualquier anomalía al equipo de TI o al CISO del MINSAL.
- Reporte en portal ANCI conforme al Decreto N° 295/2024.
- Proveedores de Servicios Esenciales: cumplimiento del Artículo 5° de la Ley N° 21.663.

### 7.1.5. Monitoreo y Cumplimiento

| Medida | Descripción |
|--------|-------------|
| Herramientas automáticas | Supervisar actividades en la nube, generar reportes periódicos |
| Alcance contractual | Definir claramente servicios prestados y márgenes de crecimiento/elasticidad |
| **SLA** | Disponibilidad mínima **99.98%** del servicio y soporte técnico **24/7** |
| Diferenciación SLA | Tiempo de respuesta vs. tiempo de resolución |
| Sanciones | Definidas para incumplimiento |

### 7.1.6. Medidas frente a Incumplimientos Contractuales

| Medida | Descripción |
|--------|-------------|
| Penalidades económicas | Proporcionales al impacto del incumplimiento |
| Rescisión anticipada | Frente a incumplimientos graves, sin costos adicionales para el contratante |
| Compromisos de mitigación | Plan de acción correctiva inmediato ante incidentes o fallas |
| Mantenimiento normativo | Para reformas normativas que impacten el diseño, desarrollo o implementación |
| Devolución y eliminación de datos | Condiciones claras al término del contrato, garantizando que no queden copias residuales |

### 7.1.7. Resguardos de Legalidad de las Cláusulas — Cláusulas Prohibidas

| Materia | Cláusulas prohibidas |
|---------|----------------------|
| Resolución de controversias | Prórroga de competencia a tribunales extranjeros; cláusulas de arbitraje ante árbitros arbitradores |
| Responsabilidad | Renuncia a las responsabilidades del proveedor, sus partners o dependientes |
| Garantías | Renuncia a garantías; condiciones de vigencia de garantía sobre entregas parciales que extingan o limiten la garantía del producto final |
| Cesiones de datos | Aceptación de cláusulas que representen cesiones de datos sensibles o datos personales en hipótesis no autorizadas por la ley |

### 7.1.8. Propiedad Intelectual en Entornos Cloud

- Toda propiedad intelectual generada en entornos de nube pública es propiedad exclusiva de MINSAL (software, código fuente, algoritmos, documentos, diseños, bases de datos).
- Acceso restringido a personas autorizadas, con revisión periódica de derechos y privilegios.
- Medidas de protección: encriptación, controles de acceso y autenticación, monitoreo continuo.
- Los proveedores no obtendrán derechos sobre obras protegidas ni sobre los datos.
- Los proveedores solo usarán material protegido bajo condiciones acordadas y en la medida necesaria para la prestación del servicio.

## 7.2. Medidas Técnicas

### 7.2.1. Certificaciones de Seguridad

| Estándar | Materia |
|----------|---------|
| ISO/IEC 27001 | Gestión de la seguridad de la información |
| ISO/IEC 27017 | Controles de seguridad específicos para servicios en la nube |
| ISO/IEC 27018 | Protección de datos personales en servicios en la nube |

Cumplimiento adicional con regulaciones nacionales: Ley de Protección de Datos Personales, Ley Marco de Ciberseguridad, Ley de Delitos Informáticos.

### 7.2.2. Encriptación de Datos

Datos confidenciales y sensibles deben aplicarse técnicas de encriptación que aseguren que no serán accedidos ilegítimamente.

### 7.2.3. Seudonimización

- Información sensible de personas naturales: técnicas de seudonimización, manteniendo en servidor local los códigos de reidentificación.
- Técnicas recomendadas: tokenización y enmascaramiento.
- Las claves de seudonimización deben gestionarse en sistemas separados y seguros.

### 7.2.4. Elasticidad

- Servicios en la nube con capacidad de aumentar o reducir automáticamente los recursos.
- Presupuestos deben prever elasticidad con márgenes para imprevistos.

### 7.2.5. Garantía de Disponibilidad

- Esquemas de alta disponibilidad (HA) con recursos en múltiples regiones o zonas de disponibilidad.
- Mecanismos para rápida restauración de operaciones (BCP/DRP).

### 7.2.6. Geolocalización y Protección de Datos Sensibles

- Recopilación limitada a lo estrictamente necesario.
- Si los datos se almacenan/procesan fuera de Chile: garantizar estándares aceptables de protección en el país de destino.
- Cifrado en tránsito y en reposo, controles de acceso restringido.
- Titulares tienen derecho de acceso. Rectificación, supresión o cancelación se evalúan caso a caso.
- Registro detallado de tratamientos, accesos y modificaciones de datos de geolocalización.
- Auditorías periódicas.

### 7.2.7. Automatización de Respaldos y Pruebas de Restauración

- Copias de seguridad automatizadas para sistemas críticos.
- Pruebas regulares de restauración.

### 7.2.8. Distribución de Copias

- Almacenamiento en múltiples regiones.
- Almacenamiento exclusivamente en nubes públicas con infraestructura accesible desde Chile por medios seguros.
- Si el proveedor tiene infraestructura en Chile y fuera: política de no replicación fuera de Chile o control estricto de replicación.
- Enfoque híbrido recomendado: copia primaria en infraestructura propia (local o nube privada) y copia secundaria en nube pública.

### 7.2.9. Monitoreo y Registro de Eventos

| Elemento auditado | Detalle |
|-------------------|---------|
| Gestión automatizada de parches | Detectar, priorizar y aplicar actualizaciones de seguridad |
| Alertas proactivas | Vulnerabilidades no gestionadas o críticas |
| Monitoreo proactivo | Identificar amenazas en etapas iniciales, activar respuestas automáticas |
| Registros de autenticación y acceso | Fallidos y exitosos en sistemas críticos y plataformas cloud |
| Eventos de red | Tráfico sospechoso, IPs no autorizadas, patrones anómalos |
| Modificaciones de configuración | Infraestructura, aplicaciones y bases de datos |
| Accesos a datos sensibles | Conforme al principio de minimización de datos |

### 7.2.10. Protección contra Amenazas

**Arquitectura de seguridad en capas con controles mínimos:**

| Control | Función |
|---------|---------|
| Web Application Firewall (WAF) | Protección de aplicaciones web |
| Protección DDoS | Mitigación de ataques de denegación de servicio |
| Segmentación de red y Zero Trust | Aislamiento y control de acceso |
| Threat Intelligence | Análisis de Indicadores de Compromiso (IoCs) |

## 7.3. Seguridad en Nube — Principios para Prestadores de Servicios

| Principio | Requisito |
|-----------|-----------|
| Controles de acceso, identidad y autenticación | Restringidos a personas autenticadas y autorizadas |
| Protección de activos | Centros de datos bajo estándares reconocidos; criterios claros sobre controles criptográficos y política de respaldo/retención/eliminación |
| Seguridad operacional, del personal y proveedores | Procesos para garantizar seguridad en la operación; posibilidad de vetar personal o proveedores con incumplimiento histórico |
| Gestión segura de clientes | Separación lógica o física de clientes; delimitación clara de responsabilidades |
| Información de auditorías a clientes | Registros de auditoría de accesos, sesiones y datos; atribución de la institución de realizar comprobaciones |
| Marco de gobernanza | Coordinación y dirección en la gestión del servicio y la información |
| Reporte de incidentes | Información detallada y oportuna sobre incidentes que afecten el servicio contratado |

## 8. Obligaciones de Seguridad para Soluciones de Software como Servicio (SaaS)

Obligaciones tecnicas y normativas para proveedores SaaS que operen con datos del sector salud: cumplimiento normativo, soberania de datos, controles tecnicos avanzados, gestion de datos no productivos, interoperabilidad, y entrega al termino del contrato.

## 8.1. Cumplimiento Normativo y Regulatorio

| Norma | Obligación SaaS |
|-------|-----------------|
| Ley N° 19.628 | Medidas técnicas y organizativas para confidencialidad, integridad y disponibilidad de datos personales; consentimiento informado, derechos de titulares, notificación de brechas |
| Ley N° 21.663 | Marco de ciberseguridad integral: identificación, protección, detección, respuesta y recuperación |
| Política de Seguridad del Sector Salud | Adopción de controles de seguridad definidos en políticas secundarias y documentos relacionados |

## 8.2. Resguardo de Datos, Soberanía y Continuidad Operacional

- Infraestructura según punto 7. Priorizar servicios con infraestructura accesible desde Chile o en jurisdicciones con protección equivalente.
- Controles técnicos y organizativos en todas las etapas (recopilación, procesamiento, almacenamiento, transmisión, eliminación): confidencialidad, integridad, disponibilidad.
- Estrategia integral de respaldo: copias periódicas, seguras (cifradas, ubicaciones separadas), verificables, con retenciones definidas.

## 8.3. Controles Técnicos de Seguridad Avanzados

#### Autenticación y Gestión de Credenciales

| Control | Requisito |
|---------|-----------|
| **MFA** | Obligatorio para todos los accesos (usuarios finales y administradores), mínimo 2 factores |
| Captcha/ReCaptcha | En formularios de inicio de sesión y recuperación de contraseñas |
| Control de intentos fallidos | Restricción del número de intentos antes de mitigación |
| Bloqueo por intentos fallidos | Período de bloqueo temporal |
| Gestión de sesiones | Tiempo de expiración para sesiones inactivas con cierre automático |
| Longitud de contraseñas | Mínimo 8 a 12 caracteres |
| Listas de contraseñas prohibidas | Prevención de credenciales vulnerables |
| Historial de contraseñas | Últimas 5 contraseñas, restricción de reutilización |
| Restablecimiento seguro | Enlaces de un solo uso con expiración; validación adicional con 2FA |

#### Cifrado

| Ámbito | Requisito |
|--------|-----------|
| Cifrado en tránsito | TLS/SSL con certificados digitales válidos de autoridades certificadoras confiables |
| Cifrado en reposo | AES-256 o superior (base de datos, almacenamiento de archivos) |

#### Detección y Prevención

| Control | Función |
|---------|---------|
| IDS/IPS | Detección y prevención de intrusiones |
| NGFW | Firewalls de última generación |
| Anti-malware avanzado | Soluciones anti-malware y análisis de comportamiento anómalo |
| WAF | Protección de aplicaciones web |

#### Monitoreo Continuo

Sistema de monitoreo de seguridad **24/7** con registro de eventos, alertas en tiempo real y capacidad de análisis forense.

#### Control de Acceso

- RBAC granular con privilegio mínimo.
- Gestión de identidades con validación unívoca de pacientes, proveedores y establecimientos.

#### Alta Disponibilidad y Tolerancia a Fallos

| Requisito | Detalle |
|-----------|---------|
| Disponibilidad de sistemas críticos | **99.98%** |
| Arquitectura | Alta disponibilidad, balanceo de carga, redundancia |
| Respaldo | Periódico de datos clínicos |

#### Protección contra Vulnerabilidades y Actualizaciones

| Obligación |
|------------|
| Actualizaciones y parches de seguridad regulares |
| Mantener actualizado software subyacente y componentes |
| Notificar mantenimiento programado con antelación a MINSAL |
| Mantenimiento no programado por vulnerabilidades críticas: informar tan pronto como sea posible |
| Responsabilidad total del proveedor por aplicación de parches y gestión del impacto |

#### Respuesta a Incidentes

| Plazo | Acción |
|-------|--------|
| **3 horas** | Notificación desde la detección a partes afectadas y autoridades competentes |
| **72 horas** (3 días) | Informe preliminar de evaluación del incidente |
| **15 días corridos** | Informe detallado de causas y medidas de mitigación y control |

- Incidente crítico o alto: informar inmediatamente al Encargado de Seguridad del MINSAL, quien califica criticidad y notifica a través del portal ANCI.
- Proveedores de Servicios Esenciales: cumplimiento del Artículo 5° de la Ley 21.663.

#### Revisiones y Auditorías de Seguridad

MINSAL podrá realizar auditorías periódicas por sí o por terceros independientes.

#### Recuperación ante Desastres (DRP)

- Desarrollar, implementar y mantener un DRP integral y eficaz.
- Entregar a la contraparte técnica de MINSAL.
- Evidencias de pruebas regulares y ejercicios de recuperación.

#### Respaldo y Recuperación

| Requisito | Detalle |
|-----------|---------|
| Frecuencia de respaldos | Según Políticas del Ministerio |
| Pruebas de restauración | Regulares |
| Restauración de datos | Plazo máximo de **2 horas** tras la detección del incidente |

#### Monitoreo y Auditoría

| Requisito |
|-----------|
| Sistemas de monitorización continua (SIEM) y auditoría detallada con trazabilidad de todas las transacciones |
| Monitoreo **24/7** de todos los servicios |
| Análisis regular de logs para identificar brechas de seguridad o anomalías |
| Sistemas de detección de intrusos en tiempo real |

## 8.3.11. Supresión, Cancelación o Destrucción de Datos

| Regla | Plazo/Condición |
|-------|-----------------|
| Mecanismos de supresión/ destrucción definitiva | Cuando los datos ya no sean necesarios |
| Eliminación segura, irreversible y verificable | Imposibilidad de recuperación posterior |
| **Cancelación de servicios, terminación de contrato o solicitud de MINSAL** | Eliminación total en plazo máximo de **15 días corridos**, con certificado de destrucción segura auditado |
| Alcance de la supresión | Producción, respaldo, contingencia, desarrollo y prueba |
| Conservación por mandato legal | Preservación segura, acceso restringido y trazabilidad completa hasta destrucción final |

#### Gestión de Configuraciones Seguras

| Requisito |
|-----------|
| Documentación completa de arquitectura de seguridad, configuraciones y procedimientos |
| Configuraciones seguras (hardening) para todos los componentes |
| Configuraciones auditables y no modificables sin notificación previa a MINSAL |

#### Seguridad en APIs

- Principios de "security by design".
- Autenticación robusta (OAuth 2.0), autorización granular, cifrado TLS 1.3.
- Protección contra OWASP API Top 10.
- Validación de entradas, limitación de tasas de consumo, trazabilidad completa de accesos, documentación actualizada.

## 8.4. Gestión Segura de Datos Productivos en Entornos No Productivos

Uso de datos reales en entornos no productivos: solo con autorización expresa del organismo contratante, según punto 11.

## 8.5. Interoperabilidad, Adherencia a la Arquitectura Referencial y Uso de IA

- Alineación con puntos 12 (Arquitectura Referencial) y 13 (Interoperabilidad).
- Estándares: HL7, FHIR, REST, GraphQL, JSON, XML, HTTPS con TLS.
- Especificar mecanismos de integración (protocolos, APIs, estándares, medidas de seguridad en transferencia).
- Si incluye IA: declarar uso conforme al punto 14 (transparencia, trazabilidad, explicabilidad).

## 8.6. Entrega Segura de Información y Eliminación al Término del Contrato

- Entrega completa, organizada y en formatos interoperables (documentación técnica, bases de datos, código fuente si aplica).
- Eliminación segura e irreversible de todos los datos del contratante (borrado seguro, destrucción física de medios), con evidencia documentada.
