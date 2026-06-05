---
_manifest:
  urn: urn:salud:kb:politica-identificacion-autenticacion-usuarios
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-05'
    source: MINSAL Chile, SGSI Nivel Central. PS-NC-003 v3
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- politica
- identificacion
- autenticacion
- contrasenas
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:politica-identificacion-autenticacion-usuarios
  salud:
    minsal_id: PS-NC-003
    minsal_version: '3'
relations:
  cites:
  - urn:salud:kb:politica-general-seguridad-informacion-ciberseguridad
---

# Politica de Identificacion y Autenticacion de Usuarios -- PS-NC-003 v03

Sistema de Gestion de Seguridad de la Informacion -- MINSAL Nivel Central. Octubre 2019.

## Proposito y alcance

Garantizar que solo personal debidamente autorizado accede a la informacion mediante sistemas de identificacion y autenticacion con claves seguras.

Define estandares y controles para acceso a recursos y sistemas computacionales de MINSAL Nivel Central: identificacion y autenticacion de usuarios, uso de nombres de usuario y contrasenas, solicitudes y administracion.

Aplica a todos los recursos computacionales de MINSAL Nivel Central y a todos los funcionarios (planta, contrata, reemplazos, suplencia), personal a honorarios y terceros de la Subsecretaria de Salud Publica y Subsecretaria de Redes Asistenciales.

### Controles ISO 27001:2013 asociados

| Control | Nombre |
|---|---|
| A.09.02.01 | Registro y cancelacion de registro de usuario |
| A.09.03.01 | Uso de informacion de autenticacion secreta |
| A.09.04.03 | Sistema de gestion de contrasenas |

## Marco normativo

| Instrumento | Referencia |
|---|---|
| NCh-ISO 27001:2013 | Sistemas de gestion de la seguridad de la informacion -- Requisitos |
| Marco Juridico SSI | Publicado en portal CSIRT del Ministerio del Interior |

Documentos relacionados: Politica de proteccion de datos y privacidad, Procedimiento de gestion de derechos de acceso y proteccion de activos, Procedimiento de gestion de incidentes de seguridad.

## Roles

| Rol | Responsabilidad |
|---|---|
| Operaciones TIC | Establecer mecanismos para supervision de actividad de cuenta y alertas de actividades inusuales; proponer controles de claves; velar por cumplimiento de politicas de identificacion y autenticacion |
| Operaciones TIC (Desarrollo/Soporte) / Areas con equipos de desarrollo | Gestionar accesos a aplicaciones; resguardar contrasenas de administracion; mantener registro de reasignaciones; autorizar asignacion de usuarios y contrasenas para personal externo; aprobar controles de claves con privilegios |
| Administrador de Sistemas | Gestionar accesos en aplicaciones donde tiene derechos de administracion; resguardar contrasenas de administracion |
| Encargado de Seguridad / Ciberseguridad | Gestionar resolucion de incidencias en manejo de cuentas de usuarios |
| Jefes de Division, Departamento, Subdepartamento | Solicitar formalmente a Division TIC cambios en perfil de privilegios; informar a TIC y RRHH cambios de funciones o alejamiento de personal a su cargo |
| Departamento de Gestion de Personas | Coordinar con Division TIC notificaciones de altas, bajas y traslados de personal |
| Funcionarios MINSAL | Cuenta de usuario unica (usuario y contrasena) para acceso a recursos y activos; responsabilidad personal sobre uso de su credencial |

## Materias que aborda

- Registro y cancelacion de registro de usuario
- Uso de informacion de autenticacion secreta
- Sistema de gestion de contrasenas

## Definiciones

**Programa de utilidad (rutina de servicios)** -- aplicacion de software para resolucion de problemas y diagnostico de fallas. Puede escanear sistemas, encontrar errores, realizar copias de seguridad, comprimir archivos, desinstalar programas. Disenados para analizar, configurar, optimizar y mantener equipos (hardware, SO, software de aplicaciones, almacenamiento). Ejemplos: antivirus, restaurador del SO, defragmentador, particionador de disco, programas de respaldo, limpiadores de registro, administrador de archivos, testeador de memoria, protectores de pantalla.

## Directrices

### Cumplimiento legislativo

Las medidas de control de acceso deben ser consistentes con la Normativa del SGSI.

### Registro y cancelacion de registro de usuarios

- Todo acceso debe ser solicitado y autorizado por la Jefatura correspondiente al Departamento TIC
- Mecanismo de identificacion (cuenta de usuario) y autenticacion (clave de acceso) individual
- Prohibido usar nombre de usuario ajeno o facilitar usuario y contrasena personal a un tercero
- Al abandono de la organizacion, el Departamento de Gestion de Personas notifica al Departamento TIC para deshabilitar o eliminar la cuenta
- La Jefatura notifica por escrito al Departamento TIC sobre ingreso, salida o traslado para crear, inhabilitar, modificar o eliminar privilegios en plataformas, dominios y dispositivos
- Administracion de accesos conforme al procedimiento de gestion de derechos de acceso

### Administracion de informacion de autenticacion secreta

Conforme al procedimiento de gestion de derechos de acceso.

## Uso de informacion de autenticacion secreta

Obligaciones de todos los usuarios:

- Mantener la informacion de autenticacion como confidencial; no divulgar a ninguna parte, incluidas personas con autoridad
- Evitar mantener registro fisico (papel, archivo, dispositivo) de la informacion de autenticacion, salvo almacenamiento seguro aprobado (boveda de contrasenas)
- Cambiar la informacion de autenticacion ante indicacion de posible vulneracion
- No compartir informacion de autenticacion secreta de usuario
- No usar la misma informacion de autenticacion para fines ajenos a MINSAL (redes sociales, bancos, etc.)
- Usar contrasenas con longitud minima suficiente y las caracteristicas definidas en 6.5.1

#### Caracteristicas de contrasenas

| Requisito | Detalle |
|---|---|
| Contrasenas temporales | Entrega segura; prohibido usar correo electronico de terceros o no protegido |
| Robustez | Dificiles de adivinar; solo de conocimiento personal; prohibida su divulgacion y anotacion en lugar visible |
| Validacion de robustez | Los sistemas de informacion deben validar la robustez de las contrasenas |
| Historico encriptado | Archivo historico para impedir reutilizacion de claves recientes |
| Almacenamiento protegido | Nunca almacenar de forma desprotegida (navegador, post-it, cuadernos) |
| Contrasenas de fabrica | Toda contrasena predeterminada por el vendedor debe cambiarse tras instalacion |
| Unicidad | Unicas para cada funcionario |

Requisitos minimos de la contrasena:

| Categoria | Ejemplo |
|---|---|
| Longitud | Minimo 8 caracteres |
| Prohibiciones | No debe contener nombres/apellidos del funcionario, username, nombre de la institucion o unidad, palabras completas |
| Letras mayusculas | A, B, C |
| Letras minusculas | a, b, c |
| Numeros | 0-9 |
| Composicion | Al menos un caracter de cada categoria |

Ejemplo: `A23J77c31`

#### Cambio de contrasenas

| Regla |
|---|
| Contrasena temporal se crea expirada para forzar cambio en primer acceso |
| Cambio periodico segun frecuencia establecida por Departamento TIC (Soporte TIC) |
| No reutilizar contrasenas en el tiempo ni en distintos sistemas |
| No construir contrasenas identicas o similares a las ultimas utilizadas |
| Archivos de contrasenas historicas siempre encriptados (donde sea factible) |

#### Almacenamiento de contrasenas

| Prohibicion |
|---|
| No incorporar contrasenas en codigo fuente de aplicaciones |
| No mantener listados de contrasenas en archivos de texto plano (deben estar encriptados) |
| Contrasenas de administracion resguardadas por el responsable del aplicativo y/o Departamento TIC |
| Archivo historico de contrasenas encriptado para impedir reutilizacion |

La cantidad de contrasenas historicas a almacenar esta definida en el estandar del Departamento TIC (Soporte TIC).

#### Contrasenas en dispositivos de red

- Routers, firewalls, switches deben tener contrasenas unicas u otro mecanismo de control de acceso
- Si un dispositivo no posee contrasena de acceso, impedir administracion remota (solo conexion local por personal autorizado)

#### Contrasena por omision

Toda contrasena por omision provista por el fabricante debe ser reemplazada.

#### Recordatorios de contrasenas

- Prohibido anotar contrasenas en lugares publicos
- Contrasenas encontradas en medios publicos seran informadas y podran ser motivo de sancion disciplinaria (Estatuto Administrativo y Politica General de Seguridad)

#### Asignacion de contrasenas expiradas y reasignacion

- Usuario que olvide/extravie su contrasena debe solicitarla al Departamento TIC (Soporte TIC) e identificarse como propietario
- Toda reasignacion se registra en bitacora del sistema y se notifica al usuario a su casilla de correo registrada (para detectar suplantacion)
- El Departamento TIC debe disponer herramientas que eviten tacticas de suplantacion de identidad (ingenieria social)

## Procedimientos de inicio de sesion seguro

| Medida |
|---|
| Acceso controlado mediante IDs unicos y contrasenas robustas |
| Metodos alternativos para autenticacion alta: medios criptograficos, tarjetas inteligentes, tokens, medios biometricos |
| No divulgar informacion del sistema que asista a usuarios no autorizados |
| No proporcionar mensajes de ayuda durante el inicio de sesion |
| Validar datos de inicio de sesion solo al completar todos los campos; no indicar cual parte es correcta/incorrecta |
| Proteger contra intentos de inicio de sesion forzados |
| No mostrar la contrasena ingresada |
| No transmitir contrasenas en texto sin cifrar a traves de la red |
| Terminar sesiones activas tras periodo de inactividad (especialmente en areas publicas, externas o dispositivos moviles) |
| Restringir tiempos de conexion para aplicaciones de alto riesgo |

### Uso de programas de utilidad privilegiados

- Restringido al personal del Departamento TIC, Administradores de Sistemas y funcionarios que por naturaleza de sus funciones requieran acceso
- Se requiere autorizacion del Encargado de Seguridad / Ciberseguridad
- Solo estos funcionarios tienen permisos de administrador en los equipos

Al habilitar equipamiento para usuarios revisar:

- Segregacion de programas de utilidad de software de aplicaciones
- Autorizacion para programas de utilidad ad hoc
- Eliminacion o deshabilitacion de programas de utilidad innecesarios
- No dejar programas de utilidad disponibles a usuarios con acceso a aplicaciones donde se requiere segregacion de deberes

### Intentos fallidos

- Numero de intentos erroneos limitado segun estandar del Departamento TIC (Soporte TIC)
- Al alcanzar el limite, la cuenta queda bloqueada
- Solo el Departamento TIC (Soporte TIC) autorizado para desbloqueo
- Desbloqueo solicitado por jefe directo o propietario de la cuenta
- Reasignacion de contrasena solicitada por jefe directo del usuario titular
- Usuarios externos: reactivacion solo con consentimiento del contacto establecido al crear la cuenta

### Acceso a informacion sensible

- Contrasenas robustas (segun punto 6.5.1)
- La contrasena nunca se comparte; el usuario que la presta es responsable de todas las acciones realizadas con ella

### Vulnerabilidades detectadas

- Ante compromiso del sistema por uso indebido de cuentas con privilegios, reemplazar todas las contrasenas de cuentas con privilegios del sistema
- Usuarios o administradores deben informar eventos anomalos o vulnerabilidades a sus superiores, al Departamento, Encargado de Seguridad y Encargado de Ciberseguridad, conforme al Procedimiento de Gestion de Incidentes de Seguridad

## Difusion

| Canal | Destino |
|---|---|
| Intranet MINSAL | `http://isalud.minsal.cl` |
| Correo informativo | Funcionarios |

## Periodo de revision

Minimo cada **2 anos** por el Comite de Seguridad de la Informacion, o ante necesidades de cambio que requieran garantizar idoneidad, adecuacion y efectividad.

## Excepciones

El Comite de Seguridad de la Informacion evalua y establece condiciones puntuales de excepcion, siempre que no infrinjan legislacion vigente. Toda excepcion debe documentarse e iniciar revision de la politica para determinar directrices adicionales o modificaciones.

## Control de versiones

| Version | Fecha | Secciones | Motivo |
|---|---|---|---|
| 01 | Agosto 2014 | Todas | Creacion del Documento |
| 02 | Octubre 2016 | Puntos 1 al 4, 5.1 al 5.7, 7, 8 | Actualizacion de normativa de referencia; inclusion de puntos 7 y 8 |
| 03 | Octubre 2019 | Todas | Cambio de formato; actualizacion de referencias normativas; actualizacion de todos los puntos |
