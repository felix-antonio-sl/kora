---
_manifest:
  urn: urn:salud:kb:procedimiento-desarrollo-seguro
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-04'
    source: MINSAL Chile, SGSI Nivel Central. PROS-NC-003 v1
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- procedimiento
- desarrollo-seguro
- ssdlc
- owasp
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 2
    shard_root_urn: urn:salud:kb:procedimiento-desarrollo-seguro
  salud:
    minsal_id: PROS-NC-003
    minsal_version: '1'
    fecha_aprobacion: Octubre 2019
    clasificacion: Publica
    elaborador: Rodrigo Vidal / Encargado PMG SSI
    revisor: José Villa / Área Seguridad de la Información (Representante Comité de
      Seguridad)
    aprobador: Gabriel Reveco / Encargado Ciberseguridad (Presidente Comité de Seguridad
      de la Información)
relations:
  cites:
    - urn:salud:kb:instructivo-seguridad-informacion-ciberseguridad-sector-salud
---

# Procedimiento de Desarrollo Seguro — PROS-NC-003 v1


Sistema de Gestión de Seguridad de la Información — MINSAL Nivel Central. Octubre 2019.

## Marco regulatorio

Marco regulatorio mínimo para el desarrollo de proyectos y aplicaciones tecnológicas de MINSAL, alineado con los procedimientos de seguridad de la información durante todo el ciclo de vida de los sistemas.

## Cobertura y alcance

| Cobertura | Detalle |
|-----------|---------|
| Áreas | Desarrollo y áreas usuarias de aplicaciones desarrolladas |
| Organismos | Subsecretarías de Salud Pública y Redes Asistenciales |
| Personal | Funcionarios (planta, contrata, reemplazos, suplencia), honorarios, terceros (proveedores, compra de servicios) con acceso a activos de información |
| Controles ISO 27001 | A.12.01.04 Separación de ambientes; A.12.02.01 Controles contra código malicioso; A.12.05.01 Instalación de software en operacionales; A.12.06.02 Restricciones sobre instalación de software; A.14.02.02 Procedimientos de control de cambios; A.14.02.06 Entorno de desarrollo seguro; A.14.02.08 Prueba de seguridad del sistema; A.14.02.09 Prueba de aprobación del sistema |

## Terminología y documentos aplicables

- **MINSAL** — Ministerio de Salud
- **SGSI** — Sistema de Gestión de Seguridad de Información
- **Documento aplicable**: NCh-ISO27001.Of2013 — Tecnología de la información, Técnicas de seguridad, Sistemas de gestión de la seguridad de la información, Requisitos

## Roles y responsabilidades

Responsables del cumplimiento: áreas de desarrollo de MINSAL, Usuarios, Custodios Físicos, Custodios de los Datos, contratistas, Administradores de Seguridad, Unidades de Informática, Gestión de Personas y Comité de Seguridad de la Información.

## Arquitectura de la plataforma de desarrollo

Aplicaciones a desarrollar deben considerar compatibilidad con el software base administrativo/institucional, aplicaciones existentes y características de las redes de datos vigentes.

## Metodología de desarrollo

### Cascada vs Ágil

| Dimensión | Modelo Cascada | Modelo Ágil |
|-----------|---------------|-------------|
| Flujo | Secuencial, lineal. Cada fase se completa antes de pasar a la siguiente (planificación → diseño → implementación → prueba) | Colaborativo, funcionalidad cruzada. Equipos pequeños manejan todas las etapas simultáneamente |
| Entregas | Actualizaciones grandes, complejas y poco frecuentes | Actualizaciones pequeñas, completas y frecuentes |
| Adecuación | Proyectos masivos segmentables en equipos más pequeños | Organizaciones pequeñas/medianas con equipos compactos |
| Riesgo | Retrasos en una fase repercuten en todo el ciclo | Mejora continua, adaptabilidad |

### Decisión metodológica

La decisión depende del tamaño del proyecto y del enfoque del equipo de desarrollo. El área de desarrollo elige la metodología.

## Controles proactivos en desarrollo de software

### Cuándo probar

Incluir seguridad en cada fase del SDLC. Pruebas recomendadas en etapas de Análisis, Diseño e Implementación — no solo en la etapa de Pruebas.

### Verificar seguridad desde el inicio

Las pruebas de seguridad deben ser parte integral de la práctica de ingeniería de software. No se puede "probar la seguridad" únicamente al final del proyecto. Verificación temprana y frecuente: pruebas manuales, pruebas automatizadas, escaneos.

Usar OWASP ASVS (Application Security Verification Standard) como guía para definir requisitos de seguridad y pruebas. Incluir protecciones de datos desde el inicio del desarrollo.

**Modelo de prueba:** Objetivos de seguridad → Revisar aplicación → Descomponer aplicación → Amenazas → Vulnerabilidades

## Pruebas de seguridad según OWASP — categorías y requisitos

### Recopilación de información

Primera fase: recoger máxima información sobre la aplicación objetivo.

- Spiders, Robots, Crawlers
- Reconocimiento mediante motores de búsqueda
- Identificación de puntos de entrada
- Pruebas de firmas de aplicaciones web
- Descubrimiento de aplicaciones
- Análisis de códigos de error

### Gestión de la configuración

Análisis de infraestructura y topología de arquitectura. Revela código fuente, métodos HTTP permitidos, funcionalidades administrativas, métodos de autenticación y configuraciones de infraestructura.

- Pruebas de SSL/TLS
- Pruebas del receptor de escucha de la BD
- Gestión de configuración de infraestructura y de aplicación
- Gestión de extensiones de archivo
- Archivos antiguos, copias de seguridad y sin referencias
- Interfaces de administración de infraestructura y aplicación
- Métodos HTTP y XST

### Lógica de negocio

Verificar fallas en lógica de negocio pensando en modos no convencionales (ej: saltar del paso 1 al 3 en un mecanismo de autenticación).

| Requisito | Descripción |
|-----------|-------------|
| Secuencialidad | Flujo lógico de negocio es secuencial y en orden |
| Límites | Detección y prevención de ataques automatizados (transferencias pequeñas continuas, transferencias masivas a múltiples usuarios) |
| Casos de abuso | Flujos de alto valor consideran actores maliciosos; protecciones contra engaño, manipulación, repudio, divulgación de información y elevación de privilegios |

### Autenticación

Verificar la identidad digital del remitente de una comunicación.

- Transmisión de credenciales a través de canal cifrado
- Enumeración de usuarios
- Pruebas de diccionario sobre cuentas de usuario o cuentas predeterminadas
- Pruebas de fuerza bruta
- Saltarse el sistema de autenticación
- Sistemas de recordatorio/restauración de contraseñas vulnerables
- Gestión del caché de navegación y salida de sesión
- Pruebas de CAPTCHA
- Múltiples factores de autenticación
- Pruebas por situaciones adversas

### Autorización

Permitir acceso a recursos solo a quienes tienen permiso. Entender el proceso de autorización y usar esa información para saltarse el mecanismo.

- Usuarios con acceso a recursos tienen credenciales válidas
- Control de acceso vía Active Directory para ingreso a sistemas (solo para validar que el usuario es válido; perfiles y roles de la aplicación pueden seguir siendo controlados por el sistema)
- Usuarios asociados a un conjunto bien definido de roles y privilegios
- Metadatos de roles y permisos protegidos contra reproducción o manipulación

### Gestión de sesiones

Cubre todos los controles sobre el usuario desde la autenticación hasta la salida de la aplicación.

- Sesiones únicas para cada individuo, no adivinables ni compartibles
- Sesiones invalidadas cuando ya no son necesarias y anuladas durante períodos de inactividad

### Validación de datos

La debilidad más común en seguridad de aplicaciones web es la falta de validación adecuada de entradas procedentes del cliente o del entorno. Conduce a inyecciones SQL sobre campos de control de acceso, ataques locale/Unicode, ataques sobre el sistema de archivos y desbordamientos de búfer.

- Todas las entradas validadas para ser utilizables para el propósito previsto
- Datos de entidad externa o cliente nunca son confiables y deben tratarse SIEMPRE como no confiables

### Denegación de servicio

Ataque DoS: usuario malicioso inunda con suficiente tráfico una máquina objetivo para hacerla incapaz de sostener el volumen de peticiones. DDoS: emplea gran número de máquinas para inundar una sola máquina objetivo.

### Servicios web

Los servicios web y SOA están expuestos a la red como cualquier otro servicio, pero pueden usarse sobre HTTP, FTP, SMTP u otros protocolos de transporte. Clientes típicamente son otros servidores, no frontales web. Vulnerabilidades similares a otras aplicaciones (inyección SQL, revelación de información) más vulnerabilidades específicas de XML.

### AJAX

Aplicaciones AJAX tienen mayor superficie de ataque que aplicaciones web convencionales. A veces desarrolladas centrándose más en qué se puede hacer que en qué se debería hacer. Procesamiento se realiza tanto en el lado del cliente como en el lado del servidor.

### Criptografía

- Módulos criptográficos fallan de forma segura; errores manejados correctamente
- Generador de números aleatorios adecuado cuando se requiera aleatoriedad
- Acceso a llaves criptográficas gestionado de forma segura

### Manejo de errores

Objetivo: proporcionar reacción útil al usuario, administradores y equipos de respuesta a incidentes. Producir registros de alta calidad, no cantidades masivas.

- No recopilar o registrar información confidencial si no se requiere específicamente
- Información registrada manejada de forma segura y protegida según clasificación de datos
- Si los registros contienen datos privados o confidenciales, se convierten en la información más sensible de la aplicación y resultan muy atractivos para atacantes

### Protección de datos

Tres elementos clave: Confidencialidad, Integridad y Disponibilidad (CID). Aplicaciones deben asumir que todos los dispositivos del usuario están comprometidos de alguna manera. Datos almacenados en dispositivos inseguros deben estar cifrados y no poder obtenerse, alterarse o divulgarse ilícitamente.

| Pilar | Requisito |
|-------|-----------|
| Confidencialidad | Datos protegidos de observación o divulgación no autorizada, en tránsito y almacenados |
| Integridad | Datos protegidos contra creación, alteración o borrado malicioso por atacantes no autorizados |
| Disponibilidad | Datos disponibles para usuarios autorizados según sea necesario |

### Código malicioso

- Actividad maliciosa potencial administrable de forma segura sin afectar al resto de la aplicación
- Sin malware activado por tiempo u otros ataques basados en factores temporales
- Sin llamadas a destinos maliciosos o no autorizados
- Sin puertas traseras (backdoors) o fallas lógicas controlables por un atacante
- Detección requiere acceso al código fuente, incluyendo bibliotecas de terceros. Revisión manual línea por línea

## Estándares de codificación SEI CERT

### Validar la entrada

Validar entrada de todas las fuentes de datos no confiables. La validación adecuada puede eliminar la gran mayoría de las vulnerabilidades de software. Sospechar de fuentes de datos externas: argumentos de línea de comandos, interfaces de red, variables de entorno, archivos controlados por el usuario.

### Prestar atención a las advertencias del compilador

Compilar con el nivel de advertencia más alto disponible. Eliminar las advertencias modificando el código. Usar herramientas de análisis estático y dinámico para detectar y eliminar fallas de seguridad adicionales.

### Arquitectura y diseño de políticas de seguridad

Crear arquitectura de software que implemente y haga cumplir políticas de seguridad. Si el sistema requiere diferentes privilegios en diferentes momentos, dividirlo en subsistemas de intercomunicación, cada uno con un conjunto de privilegios adecuado.

### Mantenlo simple

Mantener el diseño lo más simple y pequeño posible. Diseños complejos aumentan la probabilidad de errores en implementación, configuración y uso. El esfuerzo para lograr un nivel apropiado de seguridad aumenta dramáticamente con la complejidad.

### Por defecto denegar

Decisiones de acceso basadas en permiso, no en exclusión. Por defecto, el acceso está denegado y el esquema de protección identifica las condiciones bajo las cuales se permite el acceso.

### Privilegio mínimo

Cada proceso se ejecuta con el mínimo conjunto de privilegios necesarios. Acceso a permisos elevados solo durante el menor tiempo necesario para completar la tarea privilegiada. Reduce oportunidades de ejecutar código arbitrario con privilegios elevados.

### Sanitizar datos enviados a otros sistemas

Sanitizar todos los datos pasados a subsistemas complejos: shells de comando, bases de datos relacionales, componentes comerciales. Los atacantes pueden invocar funcionalidad no utilizada mediante SQL, comandos u otros ataques de inyección. El proceso de llamada comprende el contexto y es responsable de limpiar los datos antes de invocar el subsistema.

### Defensa en profundidad

Gestionar el riesgo con múltiples estrategias de defensa. Si una capa resulta inadecuada, otra capa puede evitar que una falla se convierta en vulnerabilidad explotable o limitar las consecuencias de una explotación exitosa.

### Técnicas efectivas de aseguramiento de la calidad

Buenas técnicas de QA identifican y eliminan vulnerabilidades. Incorporar pruebas de fuzz, pruebas de penetración y auditorías de código fuente como parte del programa de control de calidad. Revisiones de seguridad independientes aportan perspectiva externa.

### Adoptar una norma de codificación segura

Desarrollar o aplicar un estándar de codificación seguro para la plataforma y lenguaje de desarrollo de destino.

### Definir los requisitos de seguridad

Identificar y documentar los requisitos de seguridad al inicio del ciclo de vida del desarrollo. Asegurar que los artefactos de desarrollo subsiguientes se evalúen para cumplir con esos requisitos. Sin requisitos definidos, la seguridad del sistema no puede evaluarse efectivamente.

### Modelo de amenazas

Utilizar modelamiento de amenazas para anticipar amenazas al software. Proceso: identificar activos clave → descomponer la aplicación → identificar y categorizar amenazas por activo/componente → calificar amenazas según clasificación de riesgo → desarrollar estrategias de mitigación implementadas en diseños, códigos y casos de prueba.

## OWASP Proyecto de Ciclo de Vida de Desarrollo Seguro (S-SDLC)

Metodología de seguridad general para desarrolladores de aplicaciones y aplicaciones web. Objetivo: definir un ciclo de vida de desarrollo de software seguro estándar y guiar las mejores prácticas en cada fase (Diseño, Codificación, Mantenimiento, etc.).

La seguridad del software no es solo habilidades individuales sino también flujos de trabajo — el ciclo de vida de desarrollo de software. Participar en cada fase de un SDLC seguro es necesario para lograr seguridad.

Referencia: https://www.owasp.org/index.php/OWASP_Secure_Software_Development_Lifecycle_Project

## OWASP Top 10 — Amenazas

| # | Amenaza | Descripción |
|---|---------|-------------|
| 1 | **Inyección** | Fallas de inyección (SQL, NoSQL, OS, LDAP) cuando se envían datos no confiables a un intérprete como parte de un comando o consulta. Datos dañinos engañan al intérprete para ejecutar comandos involuntarios o acceder a datos sin autorización |
| 2 | **Pérdida de Autenticación** | Funciones de autenticación y gestión de sesiones implementadas incorrectamente. Permite comprometer contraseñas, tokens de sesiones o asumir identidad de otros usuarios |
| 3 | **Exposición de datos sensibles** | APIs y aplicaciones web no protegen adecuadamente datos sensibles (financieros, salud, PII). Requieren métodos de protección adicionales: cifrado en almacenamiento y tránsito |
| 4 | **Entidades Externas XML (XXE)** | Procesadores XML antiguos o mal configurados evalúan referencias a entidades externas. Permite revelar archivos internos, escanear puertos de LAN, ejecutar código remoto, ataques DoS |
| 5 | **Pérdida de Control de Acceso** | Restricciones sobre lo que usuarios autenticados pueden hacer no se aplican correctamente. Acceso no autorizado a funcionalidades/datos, cuentas de otros usuarios, modificación de datos, cambio de permisos |
| 6 | **Configuración de Seguridad Incorrecta** | Configuración manual, ad hoc o por omisión. S3 buckets abiertos, cabeceras HTTP mal configuradas, mensajes de error con contenido sensible, falta de parches, dependencias desactualizadas |
| 7 | **Cross-Site Scripting (XSS)** | Aplicación toma datos no confiables y los envía al navegador sin validación y codificación apropiada, o actualiza página existente con datos del usuario usando API que ejecuta JavaScript. Permite secuestrar sesión, modificar sitios, redirigir a sitios maliciosos |
| 8 | **Deserialización Insegura** | Aplicación recibe objetos serializados dañinos que pueden ser manipulados para ataques de repetición, inyecciones o elevación de privilegios. En el peor caso: ejecución remota de código en el servidor |
| 9 | **Componentes con vulnerabilidades conocidas** | Bibliotecas, frameworks y módulos se ejecutan con los mismos privilegios que la aplicación. Un componente vulnerable explotado puede provocar pérdida de datos o toma de control del servidor |
| 10 | **Registro y Monitoreo Insuficientes** | Falta de registro, monitoreo y respuesta ante incidentes permite mantener el ataque en el tiempo, pivotear a otros sistemas y manipular, extraer o destruir datos. Tiempo de detección de brecha típicamente >200 días, detectado por terceros |

Referencia: https://www.owasp.org/images/5/5e/OWASP-Top-10-2017-es.pdf

## Entornos de desarrollo separados de producción

Separar entornos de desarrollo, pruebas y operacionales para reducir riesgos de acceso o cambios no autorizados al entorno operacional.

### Reglas de transferencia

| Regla | Descripción |
|-------|-------------|
| Documentación de transferencia | Definir y documentar reglas de transferencia de software desde desarrollo al estado operacional |
| Sistemas separados | Software de desarrollo y operativo se ejecutan en distintos sistemas/procesadores, dominios y directorios |
| Pruebas previas | Cambios a sistemas operativos y aplicaciones se prueban en entorno de pruebas/etapas antes de aplicar a operacionales |
| No pruebas en producción | Salvo circunstancias excepcionales, no realizar pruebas en sistemas basados en ambientes productivos |
| Herramientas no accesibles | Compiladores, editores y otras herramientas de desarrollo no accesibles desde sistemas operacionales cuando no sea necesario |
| Perfiles distintos | Usuarios utilizan distintos perfiles para sistemas operacionales y de prueba; menús con mensajes de identificación adecuados para reducir riesgo de errores de conexión |
| Datos sensibles en pruebas | No copiar datos sensibles en el entorno de pruebas a menos que se entreguen controles equivalentes |

### Justificación

- Actividades de desarrollo y pruebas pueden provocar modificación no deseada de archivos o del entorno del sistema, o falla del sistema
- Necesidad de mantener un entorno conocido y estable para pruebas significativas
- Personal de desarrollo y pruebas con acceso al sistema operativo puede introducir código no autorizado o no probado, o alterar datos productivos (riesgo de fraude, código malicioso)
- Personal de desarrollo y pruebas representa amenaza a la confidencialidad de la información operacional

## Documentación requerida sobre desarrollos

### Modelo de datos

Cada desarrollo debe contar con información de tablas o estructuras de datos utilizadas, correctamente documentada. Requisitos mínimos:

- Identificación de llaves primarias y foráneas
- Descripción detallada (documentación en la tabla) de campos relevantes considerados especiales
- Nombres nemotécnicos de tablas y campos, autoexplicativos para evitar documentación adicional de cada uno

### Modelo entidad-relación

Cada desarrollo debe contar con un modelo o diagrama de entidad-relación que especifique cómo se relacionan las entidades del modelo de datos. Requisitos mínimos:

- Mostrar relaciones existentes a nivel de llave primaria y foránea
- Cardinalidad de las relaciones entre entidades

Vital para entender el alcance del desarrollo realizado.

### Documentación de sistemas (Diagrama de diseño lógico)

Enseña a quienes no están familiarizados con un sistema cómo se estructura, funciona y los motivos del diseño. Principales usuarios: futuros responsables del mantenimiento. El tiempo definido para el desarrollo debe considerar tiempo de documentación. Cada desarrollo debe documentarse mediante un Diagrama de Diseño Lógico de las principales funciones del sistema y sus interrelaciones con el modelo de datos.

### Documentación de requisitos básicos

Estándares mínimos para la correcta operación del desarrollo:

- Versión sistema operativo estación de trabajo
- Versión sistema operativo del servidor donde se aloja el aplicativo (si aplica)
- Versión sistema operativo del servidor de Base de Datos
- Versión de la Base de Datos
- Versión de Navegador Internet (si aplica)
- Espacios de almacenamiento requeridos mínimos y estimación promedio de crecimiento anual

### Manuales de usuarios

Cada desarrollo debe contar con manuales de uso con el funcionamiento detallado de cada función. Estructura mínima:

- Requerimientos Básicos
- Roles
- Descripción de pantallas y sus objetivos
- Control de Errores
- Contingencia y Soporte Técnico
