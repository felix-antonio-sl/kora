---
_manifest:
  urn: urn:salud:kb:clausulas-seguridad-contratos-ti-sector-salud
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
    shard_index: 1
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

# Instructivo: Cláusulas de Protección de Datos y Seguridad de la Información para Contratos de Tecnologías del Sector Salud


Sistema de Gestión de Seguridad de la Información — MINSAL
ITS-NC-006, Versión Oficial Actual v5.0, Marzo 2025
Clasificación de seguridad: Pública | TLP:BLANCO | 46 páginas

## 1. Preámbulo

| Amenaza | Consecuencias en Sector Salud |
|---------|-------------------------------|
| Ataques a cadena de suministro | Filtración de datos sensibles de pacientes, interrupción de servicios esenciales, compromiso de disponibilidad y confidencialidad de información sanitaria |
| SolarWinds (2020) | Infiltración en agencias gubernamentales de EE.UU. y empresas mundiales |
| Incidentes nacionales | SII, Poder Judicial, Dirección de Compras Públicas: vulnerabilidades en proveedores tecnológicos |

**Fundamento normativo:**

| Norma | Materia |
|-------|---------|
| Ley N° 21.663 | Ciberseguridad |
| Resolución Exenta N° 1465/2023 | Política General de Seguridad de la Información y Ciberseguridad MINSAL |
| Ley N° 19.628 | Protección de la Vida Privada |
| Ley N° 21.719 | Protección de Datos Personales (actualiza Ley N° 19.628) |
| Ley N° 20.584 | Derechos y Deberes de los pacientes |
| Ley N° 21.541 | Telemedicina |
| Ley N° 21.668 | Interoperabilidad de Fichas Clínicas |

**Propósito:** Proporcionar lineamientos para la inclusión de requisitos de seguridad en contratos tecnológicos del sector salud, garantizando que los proveedores adopten prácticas adecuadas en gestión de riesgos, protejan confidencialidad e integridad de la información, y contribuyan a la resiliencia digital.

## 2. Cumplimiento

- **Obligatoriedad:** Todos los proveedores tecnológicos que suscriban contratos con MINSAL y el Sector Salud.
- **Adhesión estricta** a las Políticas y Procedimientos de Seguridad de la Información vigentes del Ministerio.
- **Prohibición del proveedor como mandatario:** retener, utilizar o compartir información fuera del contrato.
- **Infracción grave:** Uso indebido, acceso no autorizado o retención de datos fuera del período estipulado. Sujeta a sanciones contractuales y legales.
- **Al finalizar el contrato:** Eliminar o devolver toda la información mediante mecanismos de eliminación certificados.

## 3. Definiciones

| # | Término | Definición |
|---|---------|-----------|
| 1 | Activos de información | Toda información o recurso para creación, almacenamiento, gestión o transmisión de información. Pueden ser materiales (RRHH especializados, aparatos, equipos, redes, instalaciones, soportes) o intangibles (datos, aplicaciones, sistemas operativos, bases de datos, imagen, reputación, marcas). |
| 2 | Activo informático | Toda información almacenada en una red y sistema informático que tenga valor para una persona u organización. |
| 3 | Autenticación | Propiedad de la información que da cuenta de su origen legítimo. |
| 4 | Anonimización | Procedimiento irreversible por el cual un dato personal no puede vincularse a una persona determinada ni permitir su identificación. Un dato anonimizado deja de ser dato personal. |
| 5 | Agencia (ANCI) | Agencia Nacional de Ciberseguridad. |
| 6 | Auditorías de seguridad | Procesos de control para revisar el cumplimiento de políticas y procedimientos del SGSI. |
| 7 | Seudonimización | Tratamiento de datos personales de manera que ya no puedan atribuirse a un titular sin información adicional de reidentificación, la cual debe constar en medios seguros, gestionados por separado y sujeta a medidas técnicas y organizativas. |
| 8 | Ciberespacio | Ambiente complejo soportado por hardware y redes de comunicaciones, con interacciones entre personas, software y servicios de Internet (ISO 27032). |
| 9 | Ciberataque | Acción para destruir, exponer, alterar, deshabilitar, exfiltrar u obtener acceso o uso no autorizado de un activo informático. |
| 10 | Ciberseguridad | Preservación de confidencialidad e integridad de la información y de la disponibilidad y resiliencia de redes y sistemas informáticos, protegiendo personas, sociedad, organizaciones o naciones de incidentes de ciberseguridad. |
| 11 | Incidente de ciberseguridad | Todo evento que perjudique o comprometa confidencialidad o integridad de la información, disponibilidad o resiliencia de redes y sistemas informáticos, o la autenticación de procesos. |
| 12 | Confidencialidad | Propiedad de que la información no es accedida o entregada a individuos, entidades o procesos no autorizados. |
| 13 | Continuidad de servicios | Capacidad de mantener disponibilidad de servicios, reduciendo riesgo de interrupción y propiciando recuperación del nivel normal de servicios TI en el menor tiempo posible. |
| 14 | Disponibilidad | Propiedad de que la información es accesible y utilizable cuando es requerida por un individuo, entidad o proceso autorizado. |
| 15 | Datos Personales | Datos relativos a cualquier información concerniente a personas naturales, identificadas o identificables, con independencia de su soporte. |
| 16 | Datos Sensibles | Datos personales sobre características físicas o morales, hechos o circunstancias de vida privada o intimidad: hábitos personales, origen racial, ideologías, opiniones políticas, creencias religiosas, estados de salud físicos o psíquicos, vida sexual. **Nota Ley 21.719 (vigencia 01-dic-2026):** Sustituye la definición incorporando: origen étnico o racial, afiliación política/sindical/gremial, situación socioeconómica, convicciones ideológicas/filosóficas, perfil biológico humano, datos biométricos, orientación sexual e identidad de género. |
| 17 | CSIRT | Centros multidisciplinarios para prevenir, detectar, gestionar y responder a incidentes de ciberseguridad o ciberataques de forma rápida y efectiva. |
| 18 | Gestión de incidentes | Procedimientos para detección, análisis, manejo, contención y resolución de un incidente de ciberseguridad. |
| 19 | Incidente | Evento inesperado o no deseado con consecuencias en detrimento de la seguridad de redes, equipos y sistemas de información (véase también ciberincidente). |
| 20 | Infraestructura crítica | Instalaciones, sistemas físicos o servicios esenciales cuya afectación cause grave daño a la salud, abastecimiento, actividad económica, medioambiente o seguridad del país. Incluye sistemas de asistencia sanitaria o de salud. |
| 21 | Integridad | Propiedad de que la información no ha sido modificada o destruida sin autorización. |
| 22 | Nube privada | Infraestructura de nube aprovisionada para uso exclusivo de una única organización. Puede ser propiedad, administrada y operada por la organización, un tercero o combinación, dentro o fuera de las instalaciones. |
| 23 | Nube pública | Infraestructura y recursos lógicos disponibles para el público en general a través de Internet. Propiedad de un Prestador de Servicios que gestiona la infraestructura y servicios ofrecidos. |
| 24 | Protección de los activos de información | Adopción de medidas que resguarden la seguridad física de los dispositivos y los accesos a éstos. |
| 25 | Red y sistema informático | Conjunto de dispositivos, cables, enlaces, enrutadores u otros equipos que almacenen, procesen o transmitan datos digitales. |
| 26 | Resiliencia | Capacidad de redes y sistemas informáticos para seguir operando luego de un incidente (aunque sea en estado degradado) y para recuperar sus funciones después de un incidente. |
| 27 | Riesgo | Posibilidad de ocurrencia de un incidente de ciberseguridad; cuantificado en probabilidad de ocurrencia e impacto de consecuencias. |
| 28 | Riesgo de Ciberseguridad | Circunstancia o hecho razonablemente identificable y previsible con posible efecto adverso en seguridad de redes, equipos y sistemas de información. |
| 29 | Seguridad de la información | Conjunto de medidas preventivas y reactivas para resguardar y proteger la información asegurando confidencialidad, integridad, autenticidad y disponibilidad de datos, continuidad de servicios y protección de activos de información. |
| 30 | Tratamiento de datos | Cualquier operación o conjunto de operaciones, automatizadas o no, que permitan recolectar, procesar, almacenar, comunicar, transmitir o utilizar datos personales. |
| 31 | Vulnerabilidad | Debilidad de un activo o control que puede ser explotado por una o más amenazas informáticas. |

## 4. Cumplimiento de las Políticas y Procedimientos Vigentes de Seguridad de la Información del Sector Salud

**Obligación base:** Conocer y cumplir las Políticas y Procedimientos publicados en `https://www.minsal.cl/seguridad_de_la_informacion/`.

### 4.1. Política General de Seguridad de la Información

- Toda persona que desarrolle labores para el Sector Salud (contratación directa o indirecta) debe dar estricto cumplimiento.
- Los proveedores e instituciones colaboradoras son responsables por incumplimientos, con independencia del régimen contractual o si el desempeño es a través de personal de su dependencia o subcontratación.
- En caso de incumplimiento, la institución se reserva:
 - Derecho de veto sobre el personal infractor.
 - Persecución de responsabilidades legales, administrativas y contractuales.
 - Solicitud de reemplazo de profesionales vetados por otros aprobados por el organismo contratante.

### 4.2. Políticas Específicas

Cumplimiento obligatorio de políticas específicas requeridas por la entidad contratante, especialmente:
- Control de accesos
- Desarrollo seguro de software
- Seguridad física y lógica

## 5. Gestión de Seguridad

Todo proveedor debe contar con un plan de gestión integral de seguridad, con auditorías internas y externas, validación de resultados y metodologías acordes a las Políticas y Procedimientos vigentes de MINSAL y normativa chilena publicada por la ANCI (`https://anci.gob.cl/`).

## 5.1. Gestión Ágil de Vulnerabilidades

| Componente | Descripción |
|------------|-------------|
| Monitoreo continuo | Amenazas y vulnerabilidades en sistemas, redes y aplicaciones |
| Corrección proactiva | Brechas de seguridad, siguiendo tiempos recomendados por estándares internacionales |
| Registro y documentación | Cada vulnerabilidad detectada, con trazabilidad de acciones correctivas |

## 5.2. Protocolo de Comunicación de Incidentes y Vulnerabilidades

- **Notificación:** Plazo máximo de **3 horas** desde detección a la jefatura designada o contraparte técnica.
- La contraparte técnica evalúa criticidad y notifica de inmediato al Encargado de Seguridad de la Información institucional.
- Reporte en portal de la ANCI conforme al Reglamento de Reporte de Incidentes (Decreto N° 295/2024, Ley 21.663).
- Proveedores de Servicios Esenciales: cumplimiento estricto del Artículo 5° de la Ley N° 21.663.

**Contenido del informe de incidente:**

| Elemento | Descripción |
|----------|-------------|
| Descripción técnica detallada | Vulnerabilidad detectada o incidente de seguridad |
| Impacto | Potencial o real sobre sistemas, datos e infraestructura crítica |
| Evidencia | Explotación o intento de explotación |
| Medidas | Mitigación y recuperación adoptadas o en curso, con plazos de resolución estimados |
| Revisión preventiva | Sistema completo en caso de vulnerabilidades críticas |

- Si el incidente es catalogado como **crítico**: revisión general del sistema para identificar otras vulnerabilidades explotadas.

## 5.3. Plan de Continuidad de Negocios (BCP) y Recuperación ante Desastres (DRP)

| Componente | Requisito |
|------------|-----------|
| Gestión de respaldos | Copias de seguridad periódicas en ubicaciones seguras |
| Pruebas funcionales | Regulares de recuperación de sistemas y datos |
| Redundancia y alta disponibilidad | Para servicios esenciales |
| Respuesta ante ransomware | Planes específicos |
| Otras medidas | Según estándares generalmente aceptados |

## 5.4. Auditorías de Seguridad y Evaluaciones Periódicas

**Periodicidad mínima: cada 3 meses.**

| Tipo de auditoría | Alcance |
|-------------------|---------|
| Escaneos de vulnerabilidades | Infraestructuras, plataformas y aplicaciones |
| Pruebas de penetración (pentesting) | Servicios críticos |
| Monitoreo de logs | Análisis forense de incidentes relevantes |
| Registro y documentación | Resultados, evidencias y acciones correctivas |

- Hallazgos reportados a la contraparte institucional.
- La institución contratante podrá requerir resultados de auditorías y/o realizar revisiones independientes.

## 5.5. Plan de Formación Continua en Seguridad de la Información

Capacitación obligatoria para colaboradores, proveedores y terceros:

| Área | Contenido |
|------|-----------|
| Concienciación | Ciberamenazas y prevención de riesgos |
| Buenas prácticas | Manejo seguro de la información y cumplimiento normativo |
| Usuarios privilegiados | Capacitación específica para administradores de sistemas |
| Simulacros | Respuesta ante incidentes y campañas de phishing controladas |

## 5.6. Gestión de Seguridad de Recursos Humanos

| Exigencia | Descripción |
|-----------|-------------|
| Acuerdos de confidencialidad | Firma obligatoria y compromiso de cumplimiento de políticas MINSAL |
| Validación de antecedentes | Antes de contratación de personal con acceso a infraestructuras críticas |
| Control de accesos | Principio de mínimos privilegios y segregación de funciones |

## 5.7. Gestión de Pruebas y Aceptación de Sistemas

### 5.7.1. Pruebas de Seguridad de los Sistemas

- Todos los productos de software deben someterse a pruebas y verificaciones de seguridad durante desarrollo y antes de implementación en producción, según criterios MINSAL.
- Las pruebas siguen el procedimiento definido para análisis de seguridad en aplicaciones.
- El proveedor debe abordar efectivamente las vulnerabilidades identificadas durante las revisiones, antes de exponer la versión en Internet.

### 5.7.2. Ambientes y Datos de Prueba

- Pruebas en ambientes diferenciados de los productivos.
- Los datos de prueba deben ser simulados (no operacionales, críticos, confidenciales ni sensibles).
- Si es indispensable usar datos reales (autorizado por la institución): aplicar técnicas de anonimización o seudonimización, con sistema seguro de almacenamiento de mecanismos de reidentificación.

### 5.7.3. Pruebas de Aseguramiento de Calidad

- Responsabilidad de la institución contratante garantizar la calidad del software antes del despliegue productivo.
- Proceso continuo durante todo el ciclo de vida del sistema, según Procedimiento de Aseguramiento de Calidad de Software vigente.
- Constancia en actas de: correspondencia entre requerimiento y estándares de calidad, seguridad y estabilidad.
- El Ministerio podrá validar el cumplimiento del procedimiento y la calidad del software desplegado.

### 5.7.4. Pruebas de Aceptación de los Sistemas

- Solo entran en producción sistemas que hayan superado las pruebas de aceptación definidas por MINSAL y el proveedor.
- Todo desarrollo o mantención debe incluir criterios de aceptación desde los términos de referencia.
- La corrección de errores de responsabilidad del proveedor no es mantención de cargo de la institución contratante. Las garantías tendrán vigencia desde la recepción conforme de la corrección.
- La certificación del hito solo se emite una vez aceptado el producto de software y la documentación correspondiente.

## 5.8. Gestión de Cambios

**Objetivos:**

- Minimizar impactos sobre disponibilidad del servicio y riesgos operacionales.
- Responder a requerimientos de cambios de negocio MINSAL.
- Reducir severidad e impacto de incidentes asociados a cambios.

**Clasificación de cambios:**

| Tipo | Origen |
|------|--------|
| Proactivos | Necesidades de negocio o técnicas para reducir costos, mejorar calidad, aumentar efectividad |
| Reactivos | Resolver errores o fallas, adaptaciones a requerimientos urgentes o cambios normativos |

**Responsabilidades del proveedor:**

| Tarea |
|-------|
| Participar activamente en la CAB (Change Advisory Board) |
| Evaluar, planificar, aportar antecedentes técnicos, aprobar o rechazar técnicamente el cambio |
| Interactuar con Change Coordinator |
| Recepción, registro, seguimiento y escalamiento |
| Evaluación de impacto y riesgo con la institución contratante |
| Categorización |
| Planificación con la institución contratante |
| Seguimiento y revisión |
| Reportes estadísticos y métricas del proceso |
| Proveer información de/para auditoría |

## 5.9. Desarrollo Seguro

- Adopción de estándares reconocidos: OWASP, NIST, SSDLC (Secure Software Development Lifecycle).

| Medida | Detalle |
|--------|---------|
| Prevención de inyección de código | SQL Injection, XSS, CSRF |
| Consultas a bases de datos | Procedimientos almacenados y consultas preparadas |
| Librerías y frameworks | De terceros reconocidos por fiabilidad y mecanismos de seguridad robustos |
| API REST | Autenticación con tokens (JWT u otros), certificados o llaves criptográficas |
| Licenciamiento | Todo desarrollo al interior del Estado debe estar licenciado acorde a necesidades de uso |

## 5.10. Mantenimiento de Parches y Actualización del Stack Tecnológico

| Obligación | Descripción |
|------------|-------------|
| Actualización continua | Framework y stack tecnológico exigido por MINSAL, software subyacente y todos los componentes, mediante parches de seguridad y actualizaciones críticas |
| Notificación de mantenimiento programado | Antelación a la institución contratante |
| Mantenimiento no programado | Deber de información tan pronto como sea posible (vulnerabilidades críticas) |
| Hardening | Todos los servidores web, de bases de datos y de aplicaciones configurados según mejores prácticas de seguridad |

## 6. Propiedad Intelectual

| Cláusula | Contenido |
|----------|-----------|
| **Titularidad y derechos** | Toda creación intelectual (software, bases de datos, código fuente, documentación, algoritmos, diseños, metodologías) es de propiedad exclusiva de la institución contratante, salvo que el contrato señale condición diferente. La institución podrá reconocer derechos morales si corresponde. |
| **Propiedad del código fuente** | Propiedad exclusiva de la institución contratante. Debe ser documentado, versionado y almacenado en repositorio centralizado y seguro, bajo control y acceso restringido. Garantiza derecho de uso, modificación, distribución y explotación sin limitaciones. |
| **Contratación de terceros** | Cláusula de cesión de derechos transfiriendo la totalidad de la propiedad intelectual a nombre del contratante. Código fuente y documentación técnica completa deben ser entregados a MINSAL. |
| **Licencias de terceros** | Revisar y aprobar condiciones de uso de software o componentes de terceros (código abierto o licencia comercial). Solo componentes cuya licencia permita integración sin comprometer titularidad. |
| **Confidencialidad y protección** | Toda información, especificación técnica, metodología o código generado durante el desarrollo es confidencial y propiedad de la contratante. Prohibida la divulgación, copia o uso no autorizado. |
| **Convenio de confidencialidad con personas naturales** | NDAs obligatorios para empleados de proveedor, personal a honorarios, estudiantes en práctica, convenios de colaboración. |
| **Derechos de uso en terminación de contratos** | La entidad contratante mantiene derecho exclusivo de uso y acceso a todos los materiales, código fuente y documentación. Transferencia inmediata de todos los derechos y activos digitales a MINSAL. |
| **SaaS: propiedad de modelos de datos** | El proveedor es titular de activos creados por la empresa (código fuente, software ejecutable, documentación). El contratante es propietario del modelo de datos y diseño de procesos facilitados para adaptaciones. Todo contrato SaaS debe incluir la entrega de documentos creados conjuntamente para arquitectura y diseño del servicio. |

## 7. Alojamiento de Datos en Servidores y Uso de Cloud Computing

**Lineamiento base:** Resolución Exenta N° 619-B de 26-nov-2018, Dirección de Compras y Contratación Pública (Directiva N° 32, "Recomendaciones para la contratación de servicios en la nube").

**Condiciones generales:**

| Condición | Descripción |
|-----------|-------------|
| Acceso remoto | Solo desde dentro de la Red de comunicaciones de la institución contratante, con canales seguros (usuario/contraseña segura o Clave Única) |
| Auditoría | Registros detallados y auditables: identificación del usuario, descripción del contenido, motivo/propósito del acceso, operaciones de tratamiento, destinatarios |
| Respaldos | Ejecución de respaldos para recuperación segura en tiempos razonables para procesos críticos |
| Seudonimización en nube | Datos sensibles seudonimizados antes de ingresar a sistemas en nube; datos de reidentificación se mantienen en servidores locales protegidos |
