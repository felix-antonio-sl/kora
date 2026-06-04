---
_manifest:
  urn: urn:salud:kb:procedimiento-gestion-identidad-derechos-acceso
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
    shard_index: 1
    shard_count: 2
    shard_root_urn: urn:salud:kb:procedimiento-gestion-identidad-derechos-acceso
  salud:
    minsal_id: PROS-NC-004
    minsal_version: '07'
    fecha_aprobacion: Noviembre 2024
    clasificacion: Uso Interno
relations:
  cites:
    - urn:salud:kb:instructivo-seguridad-informacion-ciberseguridad-sector-salud
---

# Procedimiento para la Gestión de Identidad y Derechos de Acceso


**PROS-NC-004 v07, Noviembre 2024. Clasificación: Uso Interno. Documento Controlado.**

## 1. Disposiciones Generales

### 1.1 Propósito

Establecer las actividades para la gestión de identidades y derechos de acceso a la información, asegurando una adecuada administración de las autorizaciones y claves de acceso de los usuarios a los activos tecnológicos de la organización. Administrar el ciclo de vida de los usuarios: creación de cuentas, roles y permisos hasta su inhabilitación, a partir de requerimientos del Departamento de Gestión de Personas y/o Jefatura directa.

### 1.2 Alcance

Aplicable a todos los funcionarios (planta, contrata, reemplazos y suplencia), personal a honorarios y terceros (proveedores, compra de servicios) que presten servicios para las Subsecretarías de Salud Pública y de Redes Asistenciales y que tengan derechos de acceso a la información que puedan afectar los activos de información del Ministerio de Salud.

#### Controles ISO 27001:2022 asociados

| ID | Control |
|-------|---------|
| 5.11 | Devolución de Activos |
| 5.15 | Control de Acceso |
| 5.16 | Gestión de Identidad |
| 5.17 | Información de Autenticación |
| 5.18 | Derechos de Acceso |
| 6.5 | Responsabilidades en la desvinculación o cambio de empleo |
| 8.2 | Gestión de Privilegios de Acceso |

### 1.3 Terminología

- **Privilegios de Acceso**: Conjunto de permisos otorgados a un usuario para interactuar con recursos o información (lectura, escritura, ejecución, modificación, eliminación) según nivel de autorización.
- **Derechos de Acceso**: Permisos específicos que determinan qué recursos o información puede ser accedida por un usuario y en qué condiciones, de acuerdo con su rol y clasificación de la información. Incluyen: Acceso Total, Acceso Restringido, Acceso de Solo Lectura, Acceso Condicional.
- **Principio de Necesidad de Saber**: Solo se otorgarán derechos de acceso en función de la necesidad de cada usuario para desempeñar su función.
- **Principio de Menor Privilegio**: Los usuarios recibirán únicamente los privilegios mínimos necesarios para realizar sus tareas específicas.

### 1.4 Marco Normativo

- **NCh ISO 27001:2022** y **NCh ISO 27002:2022**: Controles de seguridad de la información.
- **Marco Jurídico SSI**: Publicado en portal CSIRT del Ministerio del Interior.
- **Ley 20.285**: Transparencia de la función pública y derecho de acceso a la información.
- **Ley 19.628**: Protección de datos personales.
- **Ley 19.880**: Bases de los procedimientos administrativos.
- **Ley 20.584**: Derechos y deberes de los pacientes.
- **Ley 21.180**: Transformación Digital del Estado.
- **Ley 21.459**: Delitos Informáticos (deroga Ley 19.223, adecúa al Convenio de Budapest).
- **Ley 21.663**: Marco de Ciberseguridad.
- **Ley 21.668**: Interoperabilidad de fichas clínicas.
- **Decreto 273/2022**: Obligación de reportar incidentes de ciberseguridad al CSIRT de Gobierno.
- **Decreto 41/2012**: Reglamento de Ficha Clínica.
- **Decreto Supremo 7**: Norma Técnica de Seguridad de la Información y Ciberseguridad.
- **Decreto Exento 51**: Norma General Técnica 237 (telemedicina).
- **Decreto 533**: Marco regulatorio en ciberseguridad para instituciones públicas.
- **Decreto 73/2022**: Ministerio del Interior.

**Documentos relacionados**:
- Política de seguridad en la identificación y autenticación de usuarios.
- Política de Seguridad para el control de acceso.
- Política de Seguridad para las relaciones con los proveedores.

### 1.5 Ámbito de Aplicación

Todos los usuarios y sistemas de control de accesos de la organización y unidades dependientes para: Datos, Sistemas Operativos, Sistemas de Aplicación, Bases de Datos, Otros Recursos Informáticos.

## 2. Roles y Responsabilidades

### 2.1 Jefatura de Unidad, Departamento o División (Dueños de Activos)

- Autorizar y garantizar que los accesos de los usuarios a los aplicativos tecnológicos bajo su gestión estén alineados con las necesidades del cargo y las políticas de seguridad Ministeriales.
- Aprobar y notificar formalmente el ingreso de nuevos funcionarios, asegurando asignación de derechos de acceso adecuados a sus funciones.
- Solicitar oportunamente la creación, modificación o eliminación de accesos conforme a cambios en roles o funciones.
- Comunicar oportunamente cualquier desvinculación, traslado o modificación en las responsabilidades de los funcionarios para actualizar o revocar sus derechos de acceso.
- Asegurar que los usuarios de cada unidad cumplan con las normativas del procedimiento.

### 2.2 Coordinador Administrativo o funcionario designado

- Gestionar las solicitudes de acceso a los sistemas de información, asegurando que estén directamente relacionadas con las funciones autorizadas por la Jefatura.
- Comunicar de manera inmediata al Departamento de Gestión de Personas cualquier desvinculación para proceder con la revocación o ajuste de derechos de acceso.
- Recopilar, validar y mantener los antecedentes mínimos necesarios para la tramitación del ingreso de nuevos usuarios, incluyendo asignación de derechos de acceso provisionales cuando corresponda.

### 2.3 Departamento TIC (Unidad de Operaciones)

- Configurar los accesos iniciales a los sistemas de información bajo su administración para nuevos funcionarios, según autorizaciones aprobadas por la Jefatura.
- Revocar de manera oportuna los accesos de los funcionarios desvinculados, asegurando que no queden cuentas activas asociadas a usuarios no autorizados.
- Coordinar la recuperación de los activos de información y cuentas asociadas a los funcionarios desvinculados.
- Mantener un registro actualizado de todas las acciones realizadas sobre accesos y permisos, facilitando auditorías internas o externas.

### 2.4 Departamento Administración y Servicios

- Recuperar los activos asignados a los funcionarios que se desvinculan.

### 2.5 Administradores de Sistemas

- Gestionar y ser responsables de los accesos de usuarios a las aplicaciones en las que tienen derechos de administración; resguardar las contraseñas de administración.
- Administrar y supervisar los accesos de los usuarios asegurando que se cumplan los principios de autorización y privilegios mínimos.
- Realizar revisiones regulares de los permisos asignados para detectar y corregir accesos indebidos o desactualizados.
- Asegurar que las configuraciones de acceso y seguridad cumplan con las normativas establecidas.
- Informar oportunamente al Departamento TIC sobre cualquier irregularidad, incidente de seguridad o necesidad de ajuste en los accesos.

### 2.6 Departamento de Gestión de Personas

- Proveer al Departamento TIC un listado actualizado de ingresos y desvinculaciones de funcionarios, con periodicidad mínima trimestral.
- Asegurar la comunicación efectiva con las jefaturas responsables para verificar y validar la información de movimientos de personal.

### 2.7 Encargado de Seguridad de la Información

- Coordinar y supervisar periódicamente la revisión de la gestión de identidad y los derechos de acceso, asegurando que sean acordes a las funciones asignadas y a los principios de mínimo privilegio.
- Supervisar que las cuentas de usuario, especialmente aquellas con privilegios administrativos, sean deshabilitadas o eliminadas de manera oportuna, en colaboración con el Departamento TIC y Departamento de Gestión de Personas.
- Asegurar que las acciones realizadas en la gestión de identidad y acceso cumplan con normativas legales, políticas institucionales y estándares de seguridad vigentes.

### 2.8 Departamento de Auditoría Interna

- Evaluar el cumplimiento de este procedimiento, proponiendo mejoras para asegurar la conformidad con normativas legales y estándares internos.

### 2.9 Funcionarios

- Mantener la confidencialidad de las contraseñas y claves secretas asociadas a su acceso a las plataformas tecnológicas del MINSAL.
- Cumplir con las Políticas y Procedimientos del SGSI en todas las acciones relacionadas con su rol y responsabilidades.
- Evitar la divulgación de información sensible o confidencial relacionada con MINSAL, tanto dentro como fuera del ámbito laboral.
- Asumir la responsabilidad sobre el uso y protección de la información institucional, incluso fuera de las dependencias de trabajo y del horario laboral habitual.
- Garantizar la transferencia ordenada y completa de la información perteneciente a MINSAL en caso de cese de funciones, cambio de puesto o responsabilidades.
- Familiarizarse y cumplir con las Políticas de Seguridad de la Información del Ministerio, independientemente de su condición de funcionario o tercero autorizado.

## 3. Registro y Creación de Usuarios

### 3.1 Consideraciones generales del registro

La asignación y control de privilegios y derechos de acceso serán gestionados de acuerdo con el rol del usuario, la clasificación de la información y las necesidades operativas. Los accesos serán revisados periódicamente para garantizar que se ajusten a las políticas de seguridad vigentes.

Se deben utilizar registros únicos para permitir a los usuarios vincularse y ser responsables de sus acciones. Los Administradores de Sistemas deben mantener un registro formal de todas las personas autorizadas, asignándoles un ID único. Este registro debe incluir los derechos de acceso a la información y activos asociados y actualizarse cada vez que ocurran cambios en los derechos de acceso lógico y físico para asegurar trazabilidad.

### 3.2 Creación de accesos para funcionarios nuevos

La solicitud de accesos debe ser entregada por la unidad solicitante con al menos **2 días hábiles** de anticipación. No incluye el proceso de compra de equipos o licenciamiento. Debe contar con la aprobación del departamento de personal.

Previa creación, se realizará validación de la identidad de la persona para asegurar que no tiene otro usuario asignado y que la nueva identidad en los sistemas sea asignada a una única persona.

La Jefatura contratante deberá coordinar los recursos específicos a los cuales el usuario requiere acceder:
- Red de la unidad contratante
- Equipo de procesamiento (PC)
- Aplicaciones específicas
- Bases de datos requeridas
- Servicios (impresoras, telefonía, etc.)
- Sistemas y menús/funcionalidades específicas
- Carpetas compartidas
- Objetos, grupos y dominios
- Otros recursos identificados puntualmente

Debe existir una adecuada segregación de funciones, de acuerdo con la función administrativa del usuario, la criticidad de los datos y la oposición de intereses. Se podrán conceder derechos de acceso **temporales** por un periodo de tiempo limitado y revocarlos en la fecha de expiración, en particular para personal temporal o personal que requiere acceso temporal a activos de información a los que no tiene acceso regular.

### 3.3 Solicitud de acceso para funcionarios activos

En caso de traspasos de cargos, se debe evaluar si los permisos otorgados con anterioridad deben o no continuar vigentes. Si se deben habilitar más permisos, se deberá contar con el requerimiento del Jefe de Departamento respectivo.

### 3.4 Solicitud de acceso para funcionarios con conectividad remota

Para usuarios en modalidad de trabajo remoto (teletrabajo), se deben evaluar los permisos y herramientas requeridas según los accesos solicitados, los cuales serán configurados en el equipo asignado. Estos permisos deben ser autorizados por el Jefe de Departamento respectivo.

### 3.5 Acceso a los recursos de cada uno de los equipos

El acceso a los recursos de los equipos debe ser autorizado por el Jefe de Unidad o supervisor directo con autorización del Jefe de Departamento o Jefe de Divisiones. La asignación de permisos debe ser revisada por el Administrador de Sistemas y deberá contar con las aprobaciones necesarias antes de su implementación. Las aprobaciones requieren alineación con: la Política de Clasificación y Manejo de la Información, la Política de Identificación y Autenticación de Usuarios, y los requisitos de seguridad del perímetro físico.

**Principio general**: El usuario sólo debe tener acceso a los recursos mínimos indispensables para realizar su tarea. Se le prohibirá el acceso a todos los recursos de información salvo a aquellos que se le permitan expresamente.

### 3.6 Flujo de creación de accesos básicos

1. La Jefatura solicita mediante correo `mds@minsal.cl` los accesos básicos usando el **Formulario de solicitud para creación/eliminación de accesos**.
2. El área de Soporte del Departamento TIC crea los accesos básicos: correo electrónico, usuario en Active Directory, habilitación de estación de trabajo.
3. La entrega de contraseñas temporales se realiza mediante el **Registro de Entrega de Claves de Acceso**, firmado por el funcionario que recibe. Queda una copia en Soporte y otra en poder del funcionario.
4. En el registro se proporciona un enunciado con las responsabilidades del uso de los sistemas.

**Condiciones de uso notificadas al usuario**: cambiar clave inicial programada por TIC, mantener confidenciales las claves secretas, cumplir con las Políticas y Procedimientos del SGSI, entender la responsabilidad funcionaria incluso fuera de dependencias y horario de trabajo.

### 3.7 Aspectos mínimos para la incorporación

- Completar correctamente ficha de personal.
- Firma conforme de acuerdo de confidencialidad por parte del usuario.
- Revisar disponibilidad o validar adquisición de recursos técnicos requeridos (PC, Notebook, Celular, Licencias).
- Crear usuario en Active Directory.
- Crear cuentas VPN de ser requerida.
- Dar accesos a carpetas compartidas.
- Dar accesos a todos los sistemas.
- Incorporar nuevo usuario a grupos de trabajo comúnmente usados (teléfono).
- Asignar cuenta de Correo.
- Asignar usuario de grupos de correo.
- Crear usuario en impresoras.
- Sistema operativo cliente debidamente licenciado y aprobado.
- Drivers internos y de periféricos utilizados en la organización.

### 3.8 Registro de usuarios en los sistemas de información

Flujo para creación o eliminación de accesos a sistemas de información:
1. La Jefatura solicita mediante correo electrónico la creación/eliminación de accesos usando el **Formulario de solicitud de creación/eliminación de accesos** firmado.
2. En el formulario se debe indicar: usuario (nombre.apellido), RUT, detalle de sistemas a los cuales accederá, detalle del perfil de usuario para cada sistema.
3. En caso necesario, se debe solicitar la autorización de acceso al propietario del sistema.

### 3.9 Administración de cuentas especiales

Cuando un usuario requiera una cuenta especial con altos privilegios (acceso a sistemas de información, sistema operativo o sistema de administración de bases de datos), el control estará a cargo del Departamento TIC. La creación deberá ser autorizada por la Unidad de Operaciones y/o el Encargado de Seguridad.

Los permisos serán asignados bajo el principio de mínimo privilegio y en función de los roles o funciones, conforme a la Política de Control de Acceso. Se deberán identificar las cuentas de usuarios con mayor riesgo en cada uno de los sistemas para garantizar un control adecuado sobre los accesos críticos.

Las contraseñas de acceso con altos privilegios deben ser gestionadas de manera estricta, en particular en el caso de servidores internos (no externalizados). La responsabilidad de la administración recae directamente en el Departamento TIC.

### 3.10 Solicitud de creación, eliminación o ajustes de derechos de acceso

Para solicitar accesos o eliminación al sistema y a los datos, la Jefatura respectiva deberá enviar un correo electrónico a Mesa de Servicio (`mds@minsal.cl`). Este correo, una vez validado, será utilizado como parte de la solicitud que se enviará al Administrador del Sistema. El sistema debe poseer: mecanismos de protección de accesos, identificación del usuario que genera el pedido, y conservación del documento de respaldo.

La Jefatura informará las incorporaciones nuevas a `mds@minsal.cl` lo antes posible una vez conocida la fecha de incorporación. El Departamento de Gestión de Personas debe comunicar **trimestralmente** por correo electrónico al Encargado de Seguridad y/o Jefe Depto. TIC el nombre de los usuarios incorporados, para control efectivo de los usuarios habilitados.

## 4. Eliminación de Accesos y Recuperación de Activos

### 4.1 Eliminación o ajuste de los derechos de acceso

La Jefatura de Unidad/Departamento/División o Coordinador Administrativo deberá solicitar al Departamento de Gestión de Personas la eliminación de accesos respectivos, informando la baja de usuarios que ya no presten servicios, mediante correo electrónico dirigido a la Jefatura de Personal. Ésta informará oportunamente a la Jefatura del Departamento TIC y/o Encargado de Seguridad, apenas se determine la fecha de desvinculación o cambio de cargo.

#### Aspectos mínimos para bajas de usuarios (Unidad de Operaciones y Soporte)

- Eliminar usuario en Active Directory.
- Eliminar cuentas VPN.
- Eliminar accesos a todos los sistemas.
- Eliminar accesos a carpetas compartidas.
- Eliminar cuenta de Correo.
- Eliminar usuario de grupos de correo.
- Eliminar usuario de las impresoras.
- Respaldar información de carpetas compartidas.
- Respaldar cuenta de correo (si el usuario lo solicita).
- Respaldar PC del usuario según lo solicitado por Jefe Unidad responsable.
- Formatear PC del usuario (cuando sea requerido).

### 4.2 Consideraciones generales sobre devolución de activos

Todo funcionario es responsable de **devolver todos los activos** pertenecientes a la organización al finalizar su relación laboral, contrato o acuerdo.

- **Equipos personales**: Si un funcionario utiliza equipos propios, tiene la obligación de transferir toda la información pertinente a MINSAL y eliminarla de cualquier soporte que posea. De ser necesario, el Departamento TIC podrá tener acceso a los equipos para asegurar la transferencia.
- **Conocimiento desarrollado**: Si un funcionario posee conocimiento perteneciente a MINSAL desarrollado dentro del marco de sus labores y que es importante para las operaciones en curso, debe documentarlo y transferirlo al Servicio.
- **Información personal en equipos MINSAL**: Se debe consignar en una carpeta denominada "información personal". Toda la información no incluida en esta carpeta se considerará laboral y podrá ser revisada y respaldada por MINSAL.

### 4.3 Eliminación de accesos a funcionarios con accesos críticos o privilegiados

Para funcionarios con accesos críticos o privilegiados (permisos por encima de los atribuidos a cuentas normales en sistemas de información, sistema operativo, sistema de administración de base de datos, o que implican acceso a información sensible o privilegiada), se debe proceder al bloqueo inmediato tras la notificación de desvinculación o renuncia:

1. Bloquear los accesos a los sistemas de información.
2. Bloquear casilla(s) de correo y configurar mensaje automático de aviso para correos entrantes.
3. Bloquear cuentas (VPN, Videoconferencia, almacenamiento en la nube, etc.).
4. Avisar a los proveedores relacionados de la desvinculación.
5. Recuperar los activos asignados al funcionario.
6. Identificar y respaldar la información laboral contenida en los dispositivos (la información personal o privada no podrá ser revisada, solo eliminada), a solicitud del Jefe directo.
7. Eliminar de los grupos de mensajería instantánea relacionados a sus funciones.
8. Una vez recuperada la información, revocar las cuentas respectivas.

La Jefatura solicitará al Departamento de Gestión de Personas la eliminación de accesos mediante correo a la Jefatura de Personal, quien informará oportunamente al Jefe del Departamento TIC y/o Encargado de Seguridad, quien procederá **de inmediato** con las acciones anteriores, además de avisar a proveedores relacionados. Cualquier acción sobre los accesos y activos debe ser comunicada al funcionario. Se le debe otorgar la oportunidad de respaldar su información personal.

### 4.4 Recuperación de activos y eliminación de derechos de acceso

La Jefatura debe informar cualquier desvinculación mediante correo `mds@minsal.cl` con el **Formulario de solicitud para creación/eliminación de accesos**. La notificación debe ser enviada **simultáneamente** a: (1) Departamento de Gestión y Desarrollo de Personas, (2) Departamento de Administración y Servicios, (3) Departamento TIC.

**Departamento de Administración y Servicios**: Gestiona la recuperación de activos físicos asignados (documentos corporativos, equipamiento, teléfonos móviles, tarjetas de acceso, manuales). Los activos recuperados se registran en el Sistema de Inventario, documentando: dispositivos finales de usuario, dispositivos de almacenamiento portátiles, equipos especializados, claves físicas (tarjetas RFID, MFA físicos), copias físicas de información.

**Jefe directo**: Responsable de coordinar la recuperación de la información corporativa contenida en activos digitales asignados (computadores, discos duros externos), garantizando protección de la información institucional, respaldo de datos críticos y correcta transferencia o eliminación, conforme a políticas y estándares MINSAL, en colaboración con el Departamento TIC.

**Departamento TIC**: Responsable de bloquear los derechos de acceso a los sistemas de información (cambio de contraseñas, eliminación de usuario) y recuperar activos tecnológicos de información (discos duros, CD/DVD de respaldos, software, manuales, cualquier información almacenada en medios electrónicos).

Una vez transcurridos **30 días** desde el bloqueo de los derechos de acceso, estos deben ser **eliminados**. En caso de que no se devuelvan todos los equipos asignados o sean devueltos con desperfectos, se debe informar al Departamento de Administración y Servicios para que se tomen las medidas correspondientes.

### 4.5 Responsabilidades en la desvinculación o cambio de empleo

**Personal externo**: Debe conocer y aplicar los lineamientos de la Política General de Seguridad de la Información, resguardando la confidencialidad de toda la información a la que tenga acceso. Todas las obligaciones del SGSI **continuarán vigentes** tras la finalización de las actividades.

**Personal a honorarios**: Debe dar cumplimiento a las políticas de Seguridad de la Información, la política de privacidad y protección de datos personales, resguardando la confidencialidad de toda la información. Las obligaciones del SGSI **continuarán vigentes** tras la finalización de las actividades.

**Funcionarios (planta, contrata, reemplazos y suplencia)**: Todas las obligaciones de protección de datos y confidencialidad de la información definidas en el SGSI **continuarán vigentes** tras la finalización de las actividades.

## 5. Accesos Privilegiados, Revisión y Perfiles

### 5.1 Gestión de derechos de acceso privilegiados

La asignación, modificación y eliminación de derechos de acceso privilegiados a sistemas de información, sistemas operativos y sistemas de administración de bases de datos está bajo la responsabilidad del Departamento TIC, que mantendrá un registro actualizado y auditable de los accesos privilegiados.

Los derechos de acceso privilegiados serán asignados **únicamente** a usuarios cuya función o rol lo requiera estrictamente, siguiendo el principio de mínimos privilegios, conforme a la Política de Control de Acceso. Se llevará a cabo una **revisión regular** de los derechos de acceso privilegiados para asegurar su vigencia y adecuación a las responsabilidades actuales. Cualquier acceso innecesario o desactualizado deberá ser **revocado inmediatamente**.

#### Acceso privilegiado en sistemas no administrados por el Departamento TIC

Los derechos de acceso privilegiados en sistemas no administrados directamente por el Departamento TIC (sistemas en la nube o infraestructuras externas) deberán gestionarse según las políticas de acceso específicas de esos entornos, cumpliendo los mismos principios de mínimos privilegios. Es responsabilidad del dueño del activo asegurar que los proveedores ofrezcan mecanismos para la auditoría y control adecuado.

Deberán establecerse procedimientos claros para la asignación, modificación y revocación de accesos privilegiados en sistemas externos, manteniendo consistencia con la Política de Control de Acceso. Si un acceso privilegiado ya no es necesario (cambio de rol o finalización de relación con la organización), será **revocado inmediatamente, sin excepción**.

### 5.2 Revisión de los derechos de acceso de usuario

Los Dueños de los Activos de Información revisarán e informarán al Jefe del Departamento TIC o al Departamento de Gestión de Personas sobre cualquier cambio en las funciones o roles del personal que implique modificación de los derechos de acceso.

Los derechos de acceso de los usuarios deberán revisarse **al menos cada seis meses**, asegurando consistencia con las funciones actuales del personal. Se debe chequear la asignación de privilegios para asegurar que no se hayan obtenido privilegios no autorizados. Los ID de usuario y cuentas que ya no sean necesarias deberán ser **identificados y eliminados** para prevenir accesos indebidos.

### 5.3 Perfiles de acceso de los usuarios

Los perfiles de acceso son el conjunto de atribuciones y privilegios a los cuales tiene acceso una cuenta de usuario o grupo de usuarios. Las Jefaturas de Unidad, Departamento o División —responsables de la custodia de los datos de sus procesos— deben revisar en forma periódica los perfiles de usuario del personal vigente y actualizarlos cada vez que ocurra un cambio en la definición de funciones.

La administración de perfiles radica en el Gestor de Identidades y las Jefaturas de Unidad/Departamento/División. La responsabilidad de asignar un perfil a un usuario corresponderá al Jefe de Departamento solicitante, velando porque sus atribuciones correspondan a la descripción de cargo y responsabilidades funcionales.

**Requisitos para perfiles**: análisis constante de las funciones del personal; perfil solicitado formalmente por el jefe directo; perfiles acordes a las funciones de cada rol; no asignar mayores privilegios que los descritos por función; cualquier cambio en los perfiles debe ser aprobado por el Jefe del área.

### 5.4 Niveles de autorización

| Requerimiento | Responsable de autorizar |
|---|---|
| Accesos de usuarios a equipos de procesamiento y recursos (servicios, aplicaciones, datos) | Jefe de Departamento, Gestor de Identidad y Gestión de Personas (RRHH) |
| Accesos de cuentas de usuario especiales | Jefe de Informática y Encargado de Seguridad |
| Bajas de usuarios en equipos de procesamiento | Jefe de Departamento y Gestión de Personas (RRHH) |
