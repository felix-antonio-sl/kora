---
_manifest:
  urn: urn:salud:kb:politica-uso-criptografia
  provenance:
    created_by: Codex via koraficacion
    created_at: '2026-06-05'
    source: MINSAL Chile, SGSI Nivel Central. PS-NC-015 v1.0, Marzo 2023
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- politica
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:politica-uso-criptografia
  salud:
    minsal_id: PS-NC-015
    minsal_version: '01'
relations:
  cites:
  - urn:salud:kb:politica-general-seguridad-informacion-ciberseguridad
---

# Politica de Uso de Criptografia

**PS-NC-015 v1.0, Marzo 2023.**

## Proposito y alcance

Establece los requisitos para asegurar el uso adecuado y efectivo de la criptografia para proteger la confidencialidad, autenticidad e integridad de la informacion contra divulgacion no autorizada, alteracion o destruccion.

Alcance:

- Subsecretaria de Salud Publica y Subsecretaria de Redes Asistenciales.
- Aplica a todos los funcionarios (planta, contrata, reemplazos, suplencia), personal a honorarios y terceros (proveedores, servicios).
- Aplica a quienes traten informacion sensible, tengan derechos de acceso que puedan afectar activos de informacion, y al personal encargado de implementar controles de cifrado.

Dominios ISO 27001:2013 cubiertos:

| ID Control | Nombre del Control |
|---|---|
| A.10.1 | Controles criptograficos |
| A.10.1.1 | Politica de uso de los controles criptograficos |
| A.18.1.5 | Regulacion de los controles criptograficos |

## Terminologia

| Termino | Definicion |
|---|---|
| Cifrado | Escrito con letras, simbolos o numeros que solo pueden comprenderse con la llave criptografica necesaria para descifrarlos. |
| Cifrar | Procedimiento que usa un algoritmo de cifrado con clave para transformar informacion en incomprensible sin la clave secreta. |
| Controles criptograficos | Procedimientos y mecanismos utilizados para proteger la informacion mediante el cifrado y descifrado de los datos. |
| Datos personales | Datos relativos a cualquier informacion concerniente a personas naturales, identificadas o identificables. |
| Datos sensibles | Datos personales sobre caracteristicas fisicas o morales, habitos, origen racial, ideologias, creencias religiosas, estados de salud o vida sexual. |
| Datos en reposo | Datos almacenados no utilizandose activamente (discos duros, cintas, servidores, otros). |
| Datos en transito | Datos en movimiento entre dispositivos a traves de red o canal de comunicacion (internet, redes privadas, lineas telefonicas). |
| Tratamiento de datos | Cualquier operacion o procedimiento que permita recolectar, almacenar, grabar, organizar, elaborar, seleccionar, extraer, confrontar, interconectar, disociar, comunicar, ceder, transferir, transmitir o cancelar datos de caracter personal. |
| Llaves criptograficas | Secuencias de numeros o letras generadas automaticamente usadas en criptografia para transformar texto plano en texto cifrado, o viceversa. |
| Texto plano | Archivo informatico con caracteres legibles por humanos sin formato tipografico. |
| Nivel de clasificacion | Categorizacion de informacion en funcion de su nivel de confidencialidad. |

### Niveles de clasificacion de la informacion

| Nivel | Definicion |
|---|---|
| Secreto | Documentos e informaciones que requieren nivel elevado de proteccion y confidencialidad. No pueden ser divulgados, salvo situaciones especificamente autorizadas y registradas mediante actos o resoluciones. |
| Reservado | Informacion altamente sensible y de uso exclusivamente interno. Su divulgacion podria implicar impacto no deseado para MINSAL o vulnerar normativa vigente. Proteccion conforme a Ley 20.285. |
| Uso interno | Informacion sin datos sensibles, disponible para empleados y terceros seleccionados. Puede entregarse al publico sujeto a normativa vigente, previa consulta al propietario del activo. |
| Publico | Informacion generada, obtenida, adquirida o controlada por MINSAL de acceso publico. Sin requerimientos de confidencialidad. |

## Marco normativo y documentos relacionados

- NCh-ISO IEC 27001:2013 — Requisitos SGSI.
- NCh-ISO IEC 27002:2013 — Controles de seguridad de la informacion.
- Ley 19.628 — Proteccion de vida privada y datos personales.
- Ley 19.799 — Firmas y documentos electronicos.
- Ley 19.927 — Delitos de Pornografia Infantil.
- Ley 20.285 — Transparencia de la funcion publica y acceso a la informacion.
- Ley 21.180 — Transformacion Digital del Estado.
- Ley 21.459 — Delitos Informaticos (deroga 19.223, Convenio de Budapest).
- Decreto 83/2004 — Norma tecnica sobre seguridad y confidencialidad de documentos electronicos.
- Marco Juridico SSI en portal CSIRT del Ministerio del Interior.
- Politica de Seguridad para la clasificacion y manejo de informacion [1].
- Politica de Llaves Criptograficas del Ministerio de Salud.

## Roles y responsabilidades

| Rol | Responsabilidades |
|---|---|
| Departamento TIC | Garantizar que todo sistema de informacion que requiera transmision de informacion clasificada cuente con mecanismos de cifrado. Proveer los metodos de cifrado requeridos. |
| Encargado de Seguridad de la Informacion | Velar por el cumplimiento de la politica para que la informacion sea tratada segun nivel de confidencialidad al almacenarse o transmitirse. |
| Personal encargado de configuracion de encriptacion | Configurar y administrar el sistema de cifrado. Velar por el cumplimiento de la politica. Generar reportes requeridos. |
| Propietario de la informacion | Garantizar el cifrado de la informacion segun su clasificacion y nivel de confidencialidad en el desarrollo de sus actividades. |

## Directrices de la politica

### Disposiciones generales

MINSAL debe utilizar sistemas y tecnicas criptograficas para la proteccion de la informacion. El Departamento TIC evalua y actualiza periodicamente la seleccion de algoritmos segun cambios en estandares e implementa medidas de seguridad para proteger datos cifrados, incluyendo autenticacion de usuarios y gestion de acceso.

| Requisito | Detalle |
|---|---|
| Nivel de proteccion | Identificar nivel de proteccion requerido y clasificacion de la informacion; establecer tipo y calidad de algoritmos criptograficos en consecuencia. |
| Equipos de claves | Proteccion adecuada a equipos utilizados para generar, almacenar y archivar claves (considerarlos criticos o de alto riesgo). |
| Claves secretas y privadas | Proteger contra copia o modificacion no autorizada. |
| Cifrado por nivel de confidencialidad | Asegurar que la informacion se cifre segun nivel de confidencialidad al almacenarse o transmitirse por cualquier medio. |

### Directrices de seguridad para todo el personal

| N° | Directriz |
|---|---|
| i | Implementar controles criptograficos y cifrados seguros, proporcionales a la clasificacion de la informacion, en ubicaciones de datos en reposo y copias, incluidos servicios cloud. |
| ii | Usar tecnicas de encriptacion apropiadas para proteccion de informacion en dispositivos moviles, medios de almacenamiento y transmisiones hacia estos. |
| iii | Contrasenas de usuario y claves de acceso no podran almacenarse en texto plano; usar mecanismos criptograficos. |
| iv | Documentos cifrados y descifrados deben almacenarse y tratarse con medidas de seguridad conforme al nivel de clasificacion. |
| v | Identificar todo sistema que requiera transmision de informacion para garantizar que cuente con mecanismos de cifrado, segun su clasificacion. |
| vi | Cifrar discos duros de equipos computacionales que contengan informacion critica. |
| vii | En correo electronico: implementar y controlar datos confidenciales; mensaje y archivos adjuntos deben ser encriptados. |
| viii | Acuerdos de nivel de servicio o contratos con proveedores externos de servicios criptograficos (ej. autoridad de certificacion) deben abordar responsabilidad, confiabilidad y tiempos de respuesta. |
| ix | Manejo de llaves criptograficas segun Politica de Llaves Criptograficas del Ministerio de Salud. |

### Directrices para personal que trata informacion critica

| N° | Directriz |
|---|---|
| i | Cifrar documentos logicos que contengan informacion clasificada, en particular los importantes para las funciones y objetivos del MINSAL. |
| ii | Cifrar o aplicar claves a documentos (PDF, Excel, Word, BD, CSV, etc.) que contengan datos personales o datos sensibles. |
| iii | Entrega de clave del documento por medio diferente al del envio del archivo. |

### Cifrado por estado de los datos

Requisitos de cifrado segun estado de los datos, revisados y actualizados regularmente contra amenazas actuales.

#### Datos en reposo

- Seleccionar algoritmos de encriptacion seguros y reconocidos, adecuados segun disponibilidad de hardware/software, seguridad, estandarizacion y requisitos especificos.
- Aplica a discos duros, unidades flash USB y bases de datos.

**Algoritmos aceptados:**

| Algoritmo | Parametros |
|---|---|
| AES (Advanced Encryption Standard) | 128 bits o superior (192, 256). Cifrado simetrico. |
| SHA-2 o SHA-3 (Secure Hash Algorithm) | Familia SHA-2 o SHA-3. |

#### Datos en transito

Proteccion de datos enviados a traves de Internet o redes privadas.

**Protocolos requeridos:**

| Protocolo | Uso |
|---|---|
| SSL/TLS | Version mas reciente para comunicacion cliente-servidor. Cifrado de datos y autenticacion del servidor. Servidores web con conexiones seguras deben tener certificado SSL instalado. |
| IPSec | Seguridad en capa de red. Uso en VPNs y conexiones WAN. |
| SFTP, FTPS, SCP | Transporte de archivos confidenciales. Requieren cifrado para acceder a datos confidenciales desde cualquier dispositivo con interfaz web. |

#### Datos en uso

Software de encriptacion adecuado con clave de encriptacion segura. Seleccionar archivos a encriptar. Mantener clave protegida en lugar seguro.

**Software recomendado:**

| Software | Plataforma | Funcionalidad |
|---|---|---|
| Microsoft Office 365 (Proteger documento) | Multiplataforma | Encripta documentos Word, Excel, PowerPoint en uso. Desencripta automaticamente al guardar y cerrar. |
| BitLocker | Windows Pro/Enterprise/Education | Encriptacion de discos duros y almacenamiento externo. |
| GPG Suite | Mac | Encriptacion de correo y archivos. GPGServices para encriptar/desencriptar en tiempo real. |
| VeraCrypt | Multiplataforma | Encriptacion de datos en reposo y en uso. |
| AxCrypt | Windows | Encriptacion de archivos de codigo abierto. |

### Algoritmos no permitidos

| Algoritmo | Razon de exclusion |
|---|---|
| DES / IDEA | Obsoleto. Reemplazado desde 2002 por AES. |
| MD4, MD5 (hash) | No aprobado por NIST. |
| SHA-1 (hash) | Obsoleto. |
| 3DES | Obsoleto. |
| RC1, RC2, RC3, RC4 | Obsoletos. |
| CAST o CAST 128 | No aprobado. |
| Blowfish | No aprobado. |
| RSA o DSA con llaves ≤ 1024 bits | Llaves insuficientes. |
| Criptografia de curvas elipticas con llaves ≤ 160 bits | Llaves insuficientes. |
| TLS 1.0, TLS 1.1 | Versiones antiguas e inseguras. |
| Algoritmos no aprobados internacionalmente o implementaciones caseras locales | Sin respaldo de comunidad internacional. |

## Mecanismo de difusion

Contenido accesible y comprensible para todos los usuarios. Canales minimos:

- Publicacion en sitio web: http://www.minsal.cl/seguridad_de_la_informacion/
- Publicacion en intranet: http://isalud.minsal.cl/
- Correo informativo.

## Periodo de revision y cumplimiento

- Revision cada dos anos o cuando ocurran cambios significativos que afecten tecnologia, algoritmos o cifradores.
- Actualizacion cada vez que se produzcan colisiones criptograficas exitosas a los algoritmos validos.
- Alineacion con mejores practicas de la industria y cumplimiento normativo, contractual y legal continuo.
- Incumplimiento puede resultar en acciones disciplinarias, incluyendo terminacion del empleo o cancelacion de acceso a sistemas.

## Historial de versiones

| Version | Fecha | Cambios |
|---|---|---|
| 01 | 09.03.2023 | Creacion del documento |
