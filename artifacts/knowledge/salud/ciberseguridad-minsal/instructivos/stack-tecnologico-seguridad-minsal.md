---
_manifest:
  urn: urn:salud:kb:stack-tecnologico-seguridad-minsal
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-04'
    source: MINSAL Chile, Depto. TIC, Unidad de Seguridad de la Informacion y Ciberseguridad.
      ITS-NC-004 v2.0 (Diciembre 2024)
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- ciberseguridad
- minsal
- stack-tecnologico
- versiones
- desarrollo
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:stack-tecnologico-seguridad-minsal
  salud:
    minsal_id: ITS-NC-004
    minsal_version: '2.0'
    fecha_aprobacion: Diciembre 2024
    clasificacion: TLP:BLANCO
relations:
  cites:
  - urn:salud:kb:instructivo-seguridad-informacion-ciberseguridad-sector-salud
  - urn:salud:kb:arquitectura-referencia-desarrollo-sistemas-sector-salud
---

## Objetivo del documento

Garantizar que los sistemas del Ministerio de Salud utilicen versiones aceptables y actualizadas de tecnologias base, para minimizar vulnerabilidades de seguridad, reducir riesgos de brechas en activos organizacionales y establecer infraestructura tecnologica robusta que salvaguarde informacion, sistemas y recursos digitales del Ministerio.

## Objetivo

Establecer un stack tecnologico de referencia — lenguajes de programacion, bases de datos, bibliotecas, frameworks y herramientas de desarrollo (frontend y backend) — aprobado por MINSAL. Todos los sistemas del Ministerio se desarrollaran e implementaran con las versiones mas seguras, estables y actualizadas de estas tecnologias.

## Stack Tecnologico

Las versiones minimas aceptables dependen de los componentes y herramientas especificas abajo detallados.

| Stack Tecnologico | Tipo | Version Minima | Version Recomendada | Ultima Version | Observacion |
| --- | --- | --- | --- | --- | --- |
| JBOSS | APP Server | 8.0 | | 8.0.4 | Version 8.0 tiene vulnerabilidades identificadas. En caso de utilizarla, es imprescindible aplicar todos los parches de seguridad disponibles para mitigar dichos riesgos. |
| Wordpress | CMS | 6.6 | | 6.7 | Se recomienda utilizar la version 6.6 como minimo, ya que ofrece mejoras y mayor robustez en seguridad. |
| ASP.NET (core) | Framework | 8.0.2 | | 9.0 | Ultima version LTS o superior. La version 8 cuenta con soporte de parches hasta la version 8.0.11. |
| Laravel | Framework | 10.0 | | 11.35.0 | Cada version cuenta con soporte de dos anos. Considerar fechas de End of Life (EOL). La version 10 tiene soporte para actualizaciones de seguridad hasta el 04 de febrero de 2025. |
| NodeJS | Framework | 22.12.0 | 22.12.0 | 23.4.0 | La version minima, 22.12.0, esta afectada por vulnerabilidad alta CVE-2024-36138. Sin embargo, se mantiene como version recomendada con su referencia de parche como solucion, ya que deberia ser suficiente para garantizar la compatibilidad con otras tecnologias y, ademas, aun cuenta con soporte. |
| React | Framework | 18.1 | | 19 | Version 18.1 o superior. |
| JAVA | Lenguaje | 21 | | 23 | Version 21 o superior. Ambas versiones (21 y 23) presentan vulnerabilidades conocidas; en caso de usarse deben aplicar el parche respectivo. |
| PHP | Lenguaje | 8.3.14 | | 8.4.1 | Version 8.3.14 o superior. |
| Python | Lenguaje | 3.11.4 | | 3.13.1 | Version 3.11.4 o superior. |
| Javascript | Lenguaje | es11 | | es14 | Version es11 o superior. |
| Typescript | Lenguaje | 5.3 | | 5.8.0 | Version 5.3 o superior. |
| Bootstrap | Libreria | 5.0.0 | | 5.3.3 | Version 5.0 o superior. |
| JQuery | Libreria | 3.6.0 | | 4.0.0 Beta | Version 3.6 o superior. |
| ReactJS | Biblioteca | 17.0 | | 19.0 | Version 17.0 o superior. |
| RedCAP | Software | 13.4.12 | | 14.0.12 | Version 13.4.12 o superior. |
| Apache HTTP | Web Server | 2.4.62 | | 2.4.62 | Version 2.4.62 o superior. |
| Apache Tomcat | Web Server | 10.1.34 | | 11.0.2 | Version 10.1.34 o superior. |
| IIS | Web Server | 10 | | 10 | Version 10.0 o superior. |
| NGINX | Web Server | 1.26.2 | | 1.27.3 | Version 1.26.2 o superior. |
| Uvicorn | Web Server | 0.30.1 | | 0.34.0 | Version 0.30.1 o superior. |
| Windows | OS | 10 | | 11 version 23h2 | Version 10 o superior. |
| Windows Server | OS | 2022 | | 2025 | Version 2022 o superior. Presenta vulnerabilidades conocidas. En caso de utilizarla, se debe aplicar los parches y actualizaciones correspondientes para garantizar la seguridad del sistema. |
| RHEL | OS | 9.3 | | 9.5 | Version 9.3 o superior. |
| Oracle Linux | OS | 9.1 | | 9.5 | Version 9.1 (version 2023.01.31) o superior. |
| CentOS | OS | 9 | | 10 | Version 9 o superior. |
| MySQL | DB | 8.4.3 | | 9.1.0 | Version 8.4.3 o superior. La version 9.0 no cuenta con soporte de seguridad; no se recomienda su uso. En su lugar, optar por versiones mas recientes con actualizaciones y soporte adecuado. |
| PostgreSQL | DB | 15.10 | | 17.2 | Version 15.10 o superior. |
| SQL Server | DB | 2017.0 | | 2022 | Version 16.0 o superior. Varias versiones del GDR mencionadas presentan vulnerabilidades conocidas. Si se opta por alguna de estas versiones, aplicar los parches de seguridad correspondientes. Se recomienda siempre usar la version mas actualizada disponible que este debidamente parchada. |
| MongoDB | DB | 7.0.16 | | 8.0.4 | Version 7.0.16 o superior. Recomendada como minima la ultima version de la serie 7.0. Las versiones 7.1.1, 7.2.2 y 7.3.4 no son recomendadas porque no cuentan con soporte de seguridad. Es crucial utilizar versiones con actualizaciones de seguridad activas. |
| Elasticsearch | DB | 8.11.1 | | 8.17 | Version 8.11.1 o superior. |
| Redis | DB | 7.2.6 | | 7.8.2 (7.4) community edition | Version 7.2.6 o superior. |
| Windows Server | OS | 2022 (20348.2966) | | 2025 | Version 2022 o superior. |
| docker.io/library/alpine | Imagen Base | 3.18 | | 3.21 | Version 3.18 o superior. Recomendada para asegurar compatibilidad con otras tecnologias y mantener actualizaciones de seguridad pertinentes. |
| registry.access.redhat.com/redhat/ubi9-minimal | Imagen Base | 9.2-latest | | 9.3-latest | Version 9.2 o superior. Recomendada para garantizar compatibilidad con otras tecnologias e implementar las ultimas actualizaciones de seguridad. |
| docker.io/library/ubuntu | Imagen Base | 22.04 | | 25.04 | Version 22.04 o superior. Generalmente usada como base para construccion de imagenes de contenedores. |
| Fastapi | Framework | 0.110.1 | | 0.115.6 | Version 0.110 o superior. Usado para el desarrollo de microservicios en Python. |
| Spring | Framework | 6.1.15 | | 6.2.1 | Version 6.1.15 o superior. Usado para aplicaciones JEE y microservicios. |
| Gitlab | Control de versiones | 17.5.4 | | 17.6.2 | Version 17.5.4 o superior. Esta version dejara de recibir soporte el 16 de enero de 2025. Las versiones desde la 17.6 hasta la anterior a la 17.6.2 presentan vulnerabilidades conocidas, por lo que es fundamental aplicar los parches de seguridad correspondientes. Se recomienda actualizar a una version mas reciente para mantener la seguridad y el soporte adecuado. |
| Nexus | Registro de artefactos | 3.73 | | 3.75 | Version 3.73 o superior. |
| Maven | Build Tools y gestionador de dependencias | 3.8.8 | | 4.0.0-rc-2 | Version 3.8.8 o superior. Herramienta para construccion de artefactos de software que cubre todo el ciclo (generacion de codigo, compilacion, pruebas, empaquetados, publicacion, etc.). |
| Gradle | Build Tools y gestionador de dependencias | 8.4 | | 8.11.1 | Version 8.4 o superior. Herramienta para construccion de artefactos de software que cubre todo el ciclo (generacion de codigo, compilacion, pruebas, empaquetados, publicacion, etc.). |
| Poetry | Gestionador de dependencias | 1.6 | | 1.8.0 | Version 1.6 o superior. Herramienta para el control de dependencias en aplicaciones Python. |
| Composer | Gestionador de dependencias | 2.8.0 | | 2.8.4 | Version 2.8.0 o superior. Herramienta para el control de dependencias en aplicaciones PHP. |
| yarn | Gestionador de dependencias | 4.4.0 | | 4.5.3 | Version 4.4.0 o superior. Herramienta para el control de dependencias en aplicaciones Javascript o Typescript. |
| RabbitMQ | Cola de Mensajeria | 3.13.1 | | 4.0.5 | Version 3.13.1 o superior. Utilizar ultima version estable. |
| Moodle | LMS | 4.4.5 | | 4.5.1 | Utilizar ultima version estable. |

## Actualizaciones

Monitorear regularmente las actualizaciones de seguridad y avisos de vulnerabilidades de los proveedores de soluciones de seguridad. Considerar compatibilidad entre herramientas del stack.

- **Sistemas Operativos**: Utilizar versiones mas recientes y compatibles de Windows Server, Linux o macOS. Mantener actualizaciones y parches de seguridad.

## Difusion

- Publicacion en sitio web MINSAL: `http://www.minsal.cl/seguridad_de_la_informacion/`
- Publicacion en intranet MINSAL: `http://isalud.minsal.cl/`
- Correo informativo Equipo TI.

## Revision

Revision anual minima por el Jefe de TIC, el CISO o el Comite de Seguridad de la Informacion, o ante necesidades de cambios de versionamiento.

## Control de Versiones

| Version | Fecha | Creado por | Pag. o Seccion modificada | Descripcion de la modificacion |
| --- | --- | --- | --- | --- |
| 1 | Enero 2024 | Jose Villa | Todo el documento | Creacion del documento |
| 2 | Diciembre 2024 | Equipo TIC | Pag 2 a la 6: Proposito, Objetivo y Tabla Stack | Actualizacion de versiones |
