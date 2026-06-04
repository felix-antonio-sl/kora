---
_manifest:
  urn: urn:salud:kb:procedimiento-gestion-identidad-derechos-acceso-p02
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-04'
    source: 'MINSAL Chile, SGSI Nivel Central. PROS-NC-004 v07 (Noviembre 2024). Clasificación:
      Uso Interno.'
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- procedimiento
- iam
- control-acceso
- identidad
lang: es
extensions:
  kora:
    family: note
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:salud:kb:procedimiento-gestion-identidad-derechos-acceso
  salud:
    minsal_id: PROS-NC-004
    minsal_version: '07'
    fecha_aprobacion: Noviembre 2024
    clasificacion: Uso Interno
relations:
  cites:
    - urn:salud:kb:procedimiento-gestion-identidad-derechos-acceso
---

# Procedimiento para la Gestión de Identidad y Derechos de Acceso - Parte 02

## 6. Administración de Cuentas y Contraseñas

### 6.1 Administración de claves de acceso

Todos los sistemas computacionales que permitan acceder a la información administrada por MINSAL deben contar con un sistema de identificación y autenticación de usuarios que garantice que sólo personal debidamente autorizado tiene acceso, considerando además el acceso a través de claves seguras.

### 6.2 Cuentas de usuario

Requerimientos:
- Cada persona debe tener una **única** identificación de cuenta personal en todos los sistemas/equipos de la unidad.
- La identificación de la cuenta personal debe corresponder a una nomenclatura estándar predefinida de **mínimo 12 caracteres**. Debe contener letras mayúsculas, minúsculas y números.
- La identificación de cuentas especiales también debe tener **mínimo 12 caracteres**: los primeros dos caracteres corresponden al código del sistema/aplicación; los restantes identifican el tipo de permiso otorgado.
- Para aplicaciones donde el control de acceso es realizado fuera del Active Directory, la clave de acceso será según lo estipulado por el proveedor sin especificación de largo.

### 6.3 Utilización de las cuentas de usuario

Se **prohíbe** a los usuarios: la utilización de cuentas genéricas y compartir su cuenta con otros usuarios.

### 6.4 Datos a incluir en las cuentas de usuario

En la descripción de cada cuenta personal se debe incluir: RUN o número único de identificación, nombre y apellido completo del responsable, nombre a visualizar, área o unidad a la que pertenece, email, anexo, cargo, Jefe Unidad o Supervisor Directo. En las cuentas especiales, adicionalmente debe figurar la función para la que fue creada.

### 6.5 Administración de contraseñas de cada usuario

- Toda cuenta de usuario debe tener asociada obligatoriamente una **contraseña**.
- Al crear un usuario, se debe definir una contraseña única y robusta, de carácter personal. Debe ser cambiada **obligatoriamente en el primer acceso**.
- Las contraseñas deben: permanecer encriptadas y residir en archivos ocultos y protegidos; no ser visibles por pantalla al ingresarlas; tener longitud **mínima de 12 posiciones**; contener letras y números (alfanumérica); no ser en blanco; no ser genéricas o de fácil detección.
- La contraseña no debe ser igual a la identificación personal (User_ID) ni demasiado obvia.
- El Gestor de Identidades comunica la contraseña al usuario cuando se le otorga por primera vez. Si lo cree conveniente, debe utilizar procedimientos de llamado y re-llamado para asegurar la identidad del usuario.

**Requisitos para cambio de contraseñas**:
- Cambio automático obligatorio en el primer ingreso al sistema.
- Cambio automático obligatorio al menos cada **90 días** (puede ser menor).
- Ser distinta de por lo menos las últimas **6 contraseñas** anteriores.
- Permitir ser cambiada toda vez que el usuario lo requiera.

### 6.6 Bloqueo de cuentas

Al cumplirse el número de intentos fallidos establecido, la cuenta debe quedar **bloqueada**. Los únicos autorizados para su desbloqueo son el Departamento TIC; podrá ser habilitada por Soporte TI. Para las cuentas especiales de mayor riesgo, la reconexión debe ser **documentada y comunicada** al Encargado de Seguridad.

Se podrá bloquear la cuenta de usuario durante permisos o ausencias prolongadas. Para ello, el usuario o su Jefe directo deberá informar mediante correo electrónico las fechas de ausencia. El bloqueo se mantendrá hasta la efectiva comunicación con el usuario responsable.

### 6.7 Otras claves de sistemas

Existen servicios propios de las unidades que, dada su criticidad e importancia estratégica, el conocimiento, administración y uso de estas claves radican sólo en dicha unidad, excluyendo al área de Informática. Ejemplos: claves de cuentas bancarias de la organización, usuario y contraseña para Facturación Electrónica, otros.

## 7. Gobernanza del Procedimiento

### 7.1 Registros

- Solicitud para creación de accesos.
- Entrega de credenciales y claves de acceso.
- Planilla de registro de eliminación de accesos.
- Registros de entrega y devolución de equipamiento.

Período de mantención de los registros: **2 años**.

### 7.2 Mecanismo de Difusión

La comunicación del procedimiento se efectuará al menos mediante los siguientes canales:
- Publicación en la intranet de MINSAL: `http://isalud.minsal.cl/`
- Correo informativo.
- Publicación en el sitio web MINSAL: `http://www.minsal.cl/seguridad_de_la_informacion/`

### 7.3 Período de Revisión

El procedimiento deberá ser revisado cada **2 años** o cuando ocurran cambios significativos, para garantizar que: sigue siendo adecuado para su propósito y preciso, refleja los cambios en las tecnologías, y está alineado con la legislación vigente, los estándares internacionales y las mejores prácticas.

### 7.4 Excepciones al Cumplimiento del Procedimiento

En situaciones excepcionales, el Jefe de Departamento TIC, el CISO o el Comité de Seguridad de la Información tendrán la facultad de evaluar y establecer condiciones específicas para la excepción al cumplimiento de este procedimiento, siempre que tales excepciones **no infrinjan la legislación vigente ni comprometan la seguridad de la información**.

Cada excepción deberá ser **debidamente documentada**, y se deberá iniciar un proceso de revisión del procedimiento en el que se determinará si es necesario realizar modificaciones específicas.

### 7.5 Control de Versiones (resumen)

| Versión | Fecha | Modificaciones clave |
|---|---|---|
| 01 | Dic 2013 | Creación del documento. Registro de usuarios. |
| 02 | Jul 2014 | Eliminación de derechos de acceso. Flujos del proceso. Se eliminó sección de normativa 2013 de gestión de contraseñas (incluidas en política de identificación de usuarios). |
| 03 | Nov 2016 | Incluye control A.07.03.01 (Responsabilidades en desvinculación o cambio de empleo) y A.09.04.03. Se actualizan documentos aplicables. División TIC → Departamento TIC. RRHH → Gestión y Desarrollo de Personas. |
| 04 | Oct 2019 | Actualización flujos 6.1.2, 6.1.3 y 6.2.2. Responsabilidad de revisar accesos pasa a los Encargados de Seguridad. Se actualizan registros de operación. Se actualizan vías de difusión. |
| 05 | Mar 2021 | Incluye punto 6.2.2. Revisión y eliminación de accesos a funcionarios con accesos críticos o privilegiados. |
| 06 | Ago 2021 | Incluye Gestión de Identidad e Identificación y Autenticación de usuarios. |
| 07 | Nov 2024 | Actualización integral: normativa ISO 27002:2022 e ISO 27001:2022. Terminología. Leyes y decretos. Roles y responsabilidades. Registro de usuarios. Gestión de derechos privilegiados. Vigencia de respaldos. Período de revisión. Excepciones. |
