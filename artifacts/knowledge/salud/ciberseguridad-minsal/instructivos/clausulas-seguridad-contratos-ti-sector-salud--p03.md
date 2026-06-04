---
_manifest:
  urn: urn:salud:kb:clausulas-seguridad-contratos-ti-sector-salud-p03
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
    shard_index: 3
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

# Instructivo: Cláusulas de Protección de Datos y Seguridad de la Información para Contratos de Tecnologías del Sector Salud - Parte 03

## 9. Herramientas de Seguridad

En toda adquisición de soluciones tecnológicas, se exigirá cobertura integral en capa de telecomunicaciones, aplicaciones y sistemas de base.

| # | Herramienta | Función |
|---|-------------|---------|
| 1 | IDS/IPS | Prevención y detección de intrusiones ilegítimas |
| 2 | NGFW | Firewall de última generación para control de acceso y segmentación de red |
| 3 | WAF | Firewall de aplicaciones web para protección contra ataques dirigidos a aplicaciones |
| 4 | Escáner de vulnerabilidades | Sistemas operativos, software del servidor y componentes críticos |
| 5 | Análisis y escaneo de seguridad en aplicaciones | Detectar vulnerabilidades en código y configuraciones |
| 6 | DLP | Prevención de pérdida de datos para información confidencial y propiedad intelectual, en almacenamiento, uso y tránsito |
| 7 | EDR/XDR | Protección antimalware y antivirus de última generación para detección y respuesta ante amenazas avanzadas |
| 8 | Certificados digitales y MFA | Mecanismos de autenticación robustos para accesos críticos |
| 9 | IAM | Gestión de identidades y accesos para controlar y auditar privilegios |
| 10 | SIEM/SOAR | Monitorización y correlación de eventos de seguridad para respuesta eficaz ante incidentes |
| 11 | Seguridad en la nube | Cifrado, controles de acceso y auditoría en entornos cloud |
| 12 | Herramientas de conformidad | Cumplimiento normativo alineado con estándares de seguridad vigentes |

## 10. Infraestructura para Producción

**Datacenter:** Conforme al grado de criticidad de la información.

| Tipo de sistema | Infraestructura mínima |
|-----------------|----------------------|
| Registro clínico electrónico, exámenes de laboratorio e informes, recetas médicas, imágenes identificadas (información reservada) | **TIER III o superior** (preferiblemente TIER IV) para redundancia y tolerancia a fallos |
| Otros sistemas y aplicaciones | Requerimientos determinados caso a caso |

**Estándares de referencia:**
- ANSI/TIA-942 (Telecommunications Infrastructure Standard for Data Centers)
- RIC 11 de la normativa SEC (condiciones de continuidad de servicio para recintos de atención médica)

**Conectividad:** Red de Comunicaciones Privada de la institución contratante.

**Protección del tráfico:**

| Control |
|---------|
| Firewalls perimetrales y de aplicación (WAF) |
| Segmentación de redes |
| Monitoreo continuo del tráfico |
| Filtrado, inspección y restricción de acceso |
| IDS/IPS |
| Cifrado y autenticación de todo el tráfico |

## 11. Gestión de Datos Productivos

Directrices para el manejo de datos productivos en sistemas contratados: identificacion, calidad, migracion, cifrado, derechos del titular, supresion y trazabilidad.

## 11.1. Identificación de la Base de Datos

Todo sistema que trate datos personales debe contar con documento que señale:

| Elemento |
|----------|
| Responsable del tratamiento |
| Tipos/categorías de datos personales |
| Tiempos mínimos y máximos de retención |
| Procesos de negocio donde se utilizarán |
| Fuentes de datos personales |
| Destinatarios de la información |

## 11.2. Calidad de Datos

- El proveedor debe informar a la contraparte técnica cualquier cambio que afecte la calidad de datos productivos: detalle del cambio, origen (errores de ingreso o incidencias de sistemas), causas, trazabilidad (día, hora, usuarios, bases de datos, procesos).
- Verificación de calidad en todas las etapas del ciclo de tratamiento.
- Falencias imputables al proveedor: correcciones sin costo adicional para la Institución Contratante (parte de la garantía).

## 11.3. Procedimiento de Modificación o Restablecimiento de Datos

- El proveedor **no puede adoptar decisiones** sobre modificación o restablecimiento de datos.
- Procedimiento de solicitudes de análisis y calificación del cambio.
- Responsabilidad de la Contraparte institucional calificar la procedencia, escalar para autorizaciones; la autorización final solo la genera MINSAL.
- Si se autoriza: proveedor debe proporcionar antecedentes que aseguren el respaldo de la intervención.

## 11.4. Procedimiento de Notificación y Reporte

El proveedor reportará casos de sospecha de riesgo en datos de producción, con informe detallado de datos afectados y causas técnicas o de procesos.

## 11.5. Migración de Datos

- Resguardos para preservar calidad, integridad y disponibilidad.
- Respaldos para restablecimiento, copias de seguridad, procedimientos de gestión de cambio, garantía de continuidad de negocios.

## 11.6. Modelos de Datos

- Puesta a disposición de la contraparte técnica de los modelos de datos.
- Parte de los entregables obligatorios, cualquiera sea el modelo contractual.
- Al término del contrato: entrega de versiones actualizadas y vigentes.

## 11.7. Esquemas de Metadatos

Bases de datos con esquemas de metadatos aprobados por MINSAL.

## 11.8. Calidad de Tratamiento de Datos

- Los datos personales corresponden a sus titulares. Protección garantizada en Art. 19 Nos. 1 y 4 de la CPR.
- Debida diligencia en procesamiento y custodia. Responsabilidad por daños y quiebres de seguridad.
- Normativa aplicable: DFL N°1/2006 MINSAL, Ley 20.584, Ley 20.120, demás normativa complementaria del sector salud.
- Los datos de salud son sensibles: solo pueden tratarse en hipótesis legales o con consentimiento.

## 11.9. Ejercicio de Derechos del Titular de Datos

- MINSAL debe cumplir con derechos de acceso, rectificación, supresión/cancelación, bloqueo o portabilidad.
- El proveedor tiene carácter de procesador o mandatario.
- **Plazo de respuesta del proveedor: 8 horas hábiles** desde la comunicación de la contraparte técnica.

## 11.10. Mecanismos de Control y Seguimiento de Datos

| Mecanismo | Requisito |
|-----------|-----------|
| Acceso seguro | Privilegios por perfil de usuario o condiciones legales de acceso |
| Comunicación segura | Mecanismos de seguridad de nivel alto de protección para transferencia o comunicación |
| Registro auditable (log) | Identificación del usuario, descripción del contenido, motivo/propósito, destinatario — permanente a disposición del contratante |

## 11.11. Formatos de Salida

### 11.11.1. Reportes

| Requisito |
|-----------|
| Formatos confiables con protección de información y compatibilidad con cifrado |
| Datos sensibles o críticos: cifrado **AES-256** y acceso restringido según privilegios |
| Acceso con autenticación y autorización |
| Descarga con cifrado en tránsito (SSL/TLS) y mecanismos de verificación |

### 11.11.2. Descarga de Archivos

| Requisito |
|-----------|
| Formatos estructurados (CSV cifrado, JSON o XML con protección criptográfica) |
| Cifrado de nivel de campo o de base de datos |
| Controles de autenticación y autorización según perfil de acceso |

### 11.11.3. Medio de Transporte de Información

- Toda información transferida mediante dispositivos de almacenamiento móvil, correo electrónico o plataformas en nube: protegida con sistema de cifrado robusto.
- Solo el solicitante o receptor autorizado podrá descifrar los datos.
- **Prohibido el envío de información sensible a direcciones de correo no institucionales.**

## 11.12. Protección Criptográfica de Datos en Tránsito y Reposo

### 11.12.1. Cifrado de Datos Sensibles

Mecanismos criptográficos robustos para proteger acceso y almacenamiento de credenciales de usuario, bases de datos del sistema y transmisión de información sensible.

### 11.12.2. Seguridad en la Transmisión de Datos

| Requisito | Detalle |
|-----------|---------|
| HTTPS | Certificados emitidos por entidades acreditadas en el país |
| TLS | **TLS 1.2 o superior** como estándar mínimo |

### 11.12.3. Cifrado en Reposo

| Requisito | Detalle |
|-----------|---------|
| Algoritmos | **AES-256** o **RSA-4096**, u otros aprobados en política de uso de criptografía |
| Gestión de claves | Sistemas de gestión segura para generación, almacenamiento y rotación periódica |

### 11.12.4. Protección de Contraseñas

Almacenamiento con algoritmos diseñados para resistir ataques de fuerza bruta: **bcrypt, PBKDF2, Argon2**.

### 11.12.5. Monitoreo y Prevención de Vulneraciones

- Controles técnicos y administrativos para detección temprana de intentos de vulneración del sistema de cifrado.
- Sistemas configurados para seleccionar siempre la opción de cifrado más segura disponible.

### 11.12.6. Algoritmos No Permitidos

| Categoría | Algoritmo | Vulnerabilidad |
|-----------|-----------|----------------|
| Hashing inseguro (contraseñas) | **MD5** | Colisiones y ataques de fuerza bruta |
| Hashing inseguro (contraseñas) | **SHA-1** | Débil ante ataques de colisión y preimagen |
| Cifrado simétrico débil | **DES** (Data Encryption Standard) | Clave de 56 bits fácilmente rompible |
| Cifrado simétrico débil | **3DES** (Triple DES) | Claves efectivas de 112 bits inseguras ante ataques avanzados |
| Cifrado simétrico débil | **RC4** (Rivest Cipher 4) | Débil ante ataques de sesgo; inseguro para TLS |
| Protocolos obsoletos | **TLS 1.0 / TLS 1.1** | Inseguros y deshabilitados en sistemas modernos |
| Protocolos obsoletos | **SSL 2.0 / SSL 3.0** | Vulnerables a múltiples ataques |

## 11.13. Supresión, Cancelación o Destrucción de Datos

| Regla |
|-------|
| Toda modificación, cancelación o destrucción: según estándares aceptados, por instrucciones del mandante, con acta de operaciones |
| El proveedor responsable de la ejecución y de dejar constancia de pasos y resultados |
| Dispositivos digitales y magnéticos: formateo seguro antes de descarte |
| Procesos de digitalización: prohibido destruir o descartar originales sin autorización del mandante |
| Durante operación: cumplir políticas y procedimientos de gestión de incidentes, incluyendo registros y comunicación oportuna |

## 11.14. Política de Reemplazo de Medios Magnéticos

Borrado permanente de información almacenada una vez restaurada en su completitud y certificada su integridad por la contraparte de MINSAL.

## 11.15. Mecanismos de Control y Trazabilidad

| Aspecto a medir |
|-----------------|
| Cumplimiento de las medidas de seguridad acordadas |
| Cumplimiento de los niveles de servicio acordados |
| Cumplimiento de las políticas del prestador de servicios |
| Cumplimiento de medidas asociadas a destrucción de datos al final del contrato |

## 11.16. Tratamiento de los Datos Sensibles

Toda persona que desarrolle labores para el Sector Salud debe conocer las restricciones al tratamiento de datos según normativa general de salud, Ley 19.628 y normas sectoriales.

Obligación de guardar secreto sobre datos personales o sensibles provenientes de fuentes no accesibles al público (Artículo 7°, Ley 19.628). Protección y resguardo adecuado, garantizando razonablemente la privacidad mediante procedimientos y controles.

### 11.16.1. Privacidad por Defecto

- Acceso restringido a personas y usos predefinidos.
- Acción consciente y trazable para cambiar el modelo de acceso.
- Técnicas de anonimización, seudonimización o encriptación según requerimientos funcionales.

### 11.16.2. Seguridad en el Diseño

- Sistemas de verificación permanente de brechas de seguridad.
- Diseñados para adoptar medidas urgentes de resguardo de datos personales ante incidentes de seguridad.

### 11.16.3. Responsabilidad Demostrable

Trazabilidad de todas las operaciones de tratamiento de datos personales; verificación y demostración en cualquier momento. Registro de auditorías y logs de acceso.

### 11.16.4. Segregación de Datos y de Funciones

- Perfiles diferenciados por competencias; acceso solo a profesionales legalmente facultados.
- Procesamiento y almacenamiento segmentado en función de la clasificación de sensibilidad.

## 12. Arquitectura Referencial

Todo sistema desarrollado o implementado para MINSAL debe alinearse con la Arquitectura Referencial Ministerial.

| Directriz | Descripción |
|-----------|-------------|
| Alineación con la estrategia tecnológica | Diseño y desarrollo según visión y objetivos de la arquitectura de referencia |
| Estándares y tecnologías aprobadas | Plataformas, frameworks y patrones de diseño aprobados |
| Revisión y aprobación | Cambios significativos en arquitectura revisados y aprobados por Jefe TIC o gobernanza de arquitectura |
| Reutilización y modularidad | Diseño modular para escalabilidad, reducción de duplicación, optimización de recursos |
| Documentación y actualización continua | Documentar arquitecturas y modelos de datos, mantener actualizado en cada fase |

## 13. Interoperabilidad

| Directriz | Descripción |
|-----------|-------------|
| Estándares HL7 | Compatibilidad con HL7 v2.x y FHIR (R4 y posteriores) para intercambio de datos entre sistemas de información de salud (HCE, RIS, LIS, etc.) |
| Estándares de integración y protocolos | REST, GraphQL, JSON, XML, HTTPS, SFTP, TCP/IP |
| APIs documentadas y consistentes | Facilitar acceso e integración entre sistemas internos y de terceros |
| Compatibilidad con arquitectura empresarial | Alineación con lineamientos normativos y plataformas habilitadoras |
| Gestión de datos interoperables | Formatos estructurados y normalizados según directrices organizacionales y normativas |
| Pruebas de interoperabilidad | Durante el desarrollo: evaluar conectividad, rendimiento y seguridad en interacción con otras plataformas |

## 14. Uso de Inteligencia Artificial (IA)

| Obligación | Descripción |
|------------|-------------|
| Estándares | Más altos estándares éticos, legales y de seguridad |
| Auditabilidad y explicabilidad | Algoritmos auditables y explicables; detalles comprensibles sobre funcionamiento y toma de decisiones |
| Cumplimiento normativo | Ley N° 21.663 (Ciberseguridad), Ley N° 19.628 (Datos Personales), Ley N° 20.584 (Derechos y Deberes de los pacientes), y normas complementarias |
| Circular SEGPRES | Cumplimiento de Circular N° 711/2023 sobre Lineamientos para Uso de IA en el Sector Público |
| Protección de datos | Medidas adecuadas para confidencialidad e integridad de datos utilizados por IA |
| Evaluaciones periódicas de riesgos | Impactos sobre seguridad, privacidad y equidad; supervisión contra sesgos, discriminación y daños |
| Derechos de los usuarios | Mecanismos para cuestionar, corregir o revertir decisiones automatizadas; ejercicio de derechos ARCO |
| Regulaciones nacionales e internacionales | Cumplimiento de toda normativa sobre ética en IA en el ámbito de la salud |
| Responsabilidad del proveedor | Plena responsabilidad por uso y resultados de la IA, compromiso de corregir errores, vulnerabilidades o perjuicios, asegurando reparación o mitigación de daños |

## 15. Entrega de Sistemas y Datos al Término del Contrato

Como actividad de cierre de contrato, el Proveedor debe dejar operativos los aplicativos, bases de datos y software base en la plataforma del contratante.

**Actividades obligatorias:**

| Actividad |
|-----------|
| Entrega de la totalidad de la información pertinente que MINSAL o terceros determinados requieran para garantizar la continuidad operacional |
| Entrega de todos los datos tratados por el sistema en formato estructurado (relaciones entre tablas, datos maestros, librerías) para portabilidad; aplicaciones funcionando y envasadas con procedimientos de instalación garantizados |
| Entrega de todos los componentes para migración y almacenamiento histórico (modelo de datos, arquitectura, librerías, frameworks) |
| Especificación de cada componente del sistema, incluyendo diccionarios de datos |
| A solicitud de MINSAL: ambiente operativo funcionando con procedimientos de instalación garantizados, o ambiente operativo y aplicaciones/datos instalados en plataforma equivalente |
| Cualquier otro elemento necesario para mantener la continuidad operacional comparable al período de vigencia del contrato |
| Una vez recibidos los datos por MINSAL, la contraparte institucional da la orden de cancelación de datos en sistemas del proveedor, ejecutada sin dilaciones indebidas |
