---
_manifest:
  urn: urn:salud:kb:procedimiento-desarrollo-seguro-p02
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
    shard_index: 2
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
    - urn:salud:kb:procedimiento-desarrollo-seguro
---

# Procedimiento de Desarrollo Seguro — PROS-NC-003 v1 - Parte 02

## Desarrollos adquiridos a terceros

Adquisiciones o recepción de software no desarrollado internamente deben cumplir:

- Requisitos de compatibilidad según arquitectura de la plataforma de desarrollo
- Documentación de sistema según lo especificado en secciones de documentación

En caso de incumplimiento, coordinar previamente con el proveedor la implementación de dicha compatibilidad.

## Paso a producción

Cualquier desarrollo interno o sistema adquirido que requiera instalación en ambiente productivo debe cumplir:

| # | Requisito | Responsable |
|---|-----------|-------------|
| 1 | Testeado y certificado por QA. QA implementa el mejor método o estrategia de prueba. Pruebas documentadas y entregadas a desarrollo y operaciones con resultados. QA certifica el correcto funcionamiento | Área de QA |
| 2 | Testeado y aprobado por Seguridad, quien realiza pruebas para identificar posibles vulnerabilidades | Área de Seguridad |
| 3 | Entregado con toda la documentación completa del sistema | Desarrollo |
| 4 | Entregada toda la documentación legal en caso de adquisición (factura de compra, licenciamiento, etc.) | Proveedor / Desarrollo |
| 5 | Entregada la versión actualizada de su código fuente y su correspondiente documentación para almacenamiento digital | Desarrollo |

## Registros y difusión

**Registros:**

- Documentos de desarrollo: Modelo de Datos, Modelo Entidad-Relación, Documentación de Sistemas (Diagrama de diseño Lógico), Documentación de Requisitos Básicos, Manuales de Usuarios
- Registros de pruebas de aceptación de sistemas

**Difusión** — canales mínimos:

- Publicación en la intranet de MINSAL (http://isalud.minsal.cl/)
- Correo informativo

## Revisión y control de versiones

**Revisión:** obligatoria al menos cada dos años o cuando ocurran cambios significativos, para asegurar continua idoneidad, eficiencia y efectividad.

**Control de versiones:**

| Versión | Fecha de Aprobación | Motivo del cambio | Secciones modificadas |
|---------|---------------------|-------------------|----------------------|
| 01 | Octubre 2019 | Creación del documento | Todas |

## Anexo: Directrices ISO 27001 a cumplir

| Control | Descripción |
|---------|-------------|
| 7.1.1 | Selección |
| 12.1.1 | Procedimientos operativos documentados |
| 12.1.2 | Administración de cambios |
| 12.1.4 | Separación de entornos de desarrollo, pruebas y operacionales |
| 12.6.1 | Administración de vulnerabilidades técnicas |
| 14.1.1 | Análisis y especificación de los requisitos de seguridad de la información |
| 14.1.2 | Protección de servicios de aplicación en redes públicas |
| 14.1.3 | Protección de transacciones de servicios de aplicación |
| 14.2.1 | Política de desarrollo seguro |
| 14.2.2 | Procedimientos de control de cambios del sistema |
| 14.2.3 | Revisión técnica de las aplicaciones después de los cambios en la plataforma operativa |
| 14.2.4 | Restricciones a los cambios de paquetes de software |
| 14.2.5 | Principios de ingeniería segura del sistema |
| 14.2.6 | Entorno de desarrollo seguro |
| 14.2.7 | Desarrollo externalizado |
| 14.2.8 | Pruebas de seguridad del sistema |
| 14.3.1 | Protección de los datos de pruebas |
| 18.1.2 | Derechos de propiedad intelectual |
| 18.1.5 | Regulación de controles criptográficos |

Complementarios: ISO 27036 — Information security for supplier relationships (four parts); ISO 29101 — Privacy architecture framework

## Anexo: Herramientas para test de aplicaciones

| # | Herramienta | Propósito |
|---|-------------|-----------|
| 1 | Selenium | Web Application Testing. Framework para probar aplicaciones web (interfaz web y pruebas funcionales). Incluye Selenium IDE, RC, WebDriver y Grid |
| 2 | Appium | Mobile Testing. Framework para probar aplicaciones web nativas, híbridas y móviles en iOS, Android y Windows (dispositivos reales y simuladores). Multiplataforma, misma API |
| 3 | JMeter | Load Testing. Herramienta Java para cargar comportamiento de aplicación y medir rendimiento. Prueba recursos estáticos y dinámicos (SOAP/REST, HTTP/HTTPS, BD, FTP) |
| 4 | Jenkins | Continuous Testing. Integración continua vía automatización. Administra cambios de código, pruebas y ciclo de vida del despliegue. +1200 plugins |
| 5 | TestLink | Test Management. Herramienta web para administrar casos de prueba, conjuntos de pruebas, documentos de prueba y proyectos. Integrable con Mantis, JIRA, Bugzilla, FogBugz |
| 6 | Mantis | Bug-Tracking & Project Management. Seguimiento de errores, gestión de proyectos y administración de problemas. Colaboración entre equipos y clientes |
| 7 | Postman | API Testing. Extensión de Chrome o producto cloud para desarrollar, probar y documentar APIs. Historial de solicitudes HTTP, scripts personalizados, autocompletar URL |
| 8 | Firebug / Firepath | Online Debugging. Extensión de navegador para depuración, edición y supervisión de CSS, HTML y JavaScript. Firepath identifica XPath de cualquier elemento |
| 9 | GitHub | Project & Source Code Hosting. Repositorio web para alojar y administrar proyectos, versiones y código fuente. Edición online, ticketing, seguimiento de errores, administración de tareas |
| 10 | Bugzilla | Defect Tracking & Collaboration. Seguimiento de defectos con sistema integrado de email, gerencia avanzada de preguntas, sistema de permisos, informes incorporados, perfiles editables |
| 11 | RazorSQL | Database Query Tool. Editor SQL y base de datos para Windows, Mac OS y Linux. Importar, exportar y convertir BD en MySQL, Oracle, DB2, PostgreSQL, SQLite, MS SQL Server, MS Access |
| 12 | PhantomJS | Headless Browser. Navegador headless para automatizar interacciones de página. Habilita navegación y comportamiento de usuario sin cargar GUI |
| 13 | UIAutomator | Android Testing Framework. Pruebas de UI funcional para aplicaciones Android. Casos de prueba en múltiples dispositivos con diferentes resoluciones. Prueba apps preinstaladas y de terceros |
| 14 | Notepad++ | Source Code Editor. Editor de texto para 27 lenguajes de programación en Windows. Resaltado de sintaxis, plegado, ediciones sincronizadas, vistas múltiples, macros |
| 15 | FileZilla | FTP Solution. Aplicación FTP multiplataforma cliente/servidor. Transferencias en FTP, SFTP, FTPS. Administrador de sitio con detalles de conexión |
| 16 | AutoIT | Language Automation. Automatización de GUI de Windows y secuencias de comandos (pulsaciones de teclas, movimiento del ratón, manipulación de ventana/control) |

Referencias: [Selenium](http://www.seleniumhq.org/projects/webdriver/), [Appium](http://appium.io), [JMeter](http://jmeter.apache.org), [Jenkins](https://jenkins.io), [TestLink](http://testlink.org), [Mantis](https://www.mantisbt.org), [Postman](https://www.getpostman.com), [Firebug](http://getfirebug.com), [GitHub](https://github.com), [Bugzilla](https://www.bugzilla.org), [RazorSQL](https://razorsql.com), [PhantomJS](http://phantomjs.org), [UIAutomator](https://google.github.io/android-testing-support-library/docs/uiautomator/), [Notepad++](https://notepad-plus-plus.org), [FileZilla](https://filezilla-project.org), [AutoIT](https://es.m.wikipedia.org/wiki/AutoIt)
