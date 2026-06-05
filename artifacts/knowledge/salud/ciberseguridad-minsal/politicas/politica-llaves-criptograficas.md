---
_manifest:
  urn: urn:salud:kb:politica-llaves-criptograficas
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-05'
    source: MINSAL Chile, SGSI Nivel Central. PS-NC-019 v1
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
    shard_root_urn: urn:salud:kb:politica-llaves-criptograficas
  salud:
    minsal_id: PS-NC-019
    minsal_version: '1'
    fecha_aprobacion: Marzo 2023
    elaborador: José Villa Catalan / Luciano Rojas
    revisor: José Villa (Encargado Seguridad de la Información), Carlos Maldonado
      (Encargado Operaciones), Rodrigo Zamorano (Encargado Proyectos)
    aprobador: Jorge Herrera (Jefe Departamento TIC)
    clasificacion: Publica
relations:
  cites:
  - urn:salud:kb:politica-general-seguridad-informacion-ciberseguridad
---

# Politica de Llaves Criptograficas — PS-NC-019 v1

Sistema de Gestion de Seguridad de la Informacion — MINSAL Nivel Central. Marzo 2023.

## Definicion y ambito de aplicacion

Definir reglas para el uso de claves criptograficas que protejan confidencialidad, integridad, autenticidad e integridad de la informacion cifrada en MINSAL.

| Cobertura | Detalle |
|-----------|---------|
| Organismos | Subsecretaria de Salud Publica, Subsecretaria de Redes Asistenciales |
| Personal | Funcionarios (planta, contrata, reemplazos, suplencia), honorarios, terceros (proveedores, compra de servicios) que traten informacion sensible |
| Control ISO 27001 | 8.24 Uso de criptografia (NCh-ISO IEC 27002:2022) |

Aplica a quienes tengan autorizacion de acceso a informacion que pueda afectar los activos de informacion, incluyendo personal autorizado y encargados de implementar controles de cifrado en servicios de red y sistemas de informacion.

## Marco normativo y documentos relacionados

**Normas tecnicas:**
- NCh-ISO 27001:2013 — Tecnologia de la informacion, Tecnicas de seguridad, SGSI, Requisitos

**Leyes:**
- Ley 19.628 — Proteccion de vida privada y datos personales
- Ley 19.799 — Firmas y documentos electronicos
- Ley 19.927 — Delitos de Pornografia Infantil
- Ley 20.285 — Transparencia de la funcion publica y acceso a la informacion
- Ley 21.180 — Transformacion Digital del Estado
- Ley 21.459 — Delitos Informaticos (adecua Convenio de Budapest)

**Decretos:**
- Decreto 83/2004 (Min. Secretaria General de la Presidencia) — Norma tecnica sobre seguridad y confidencialidad de documentos electronicos
- Decreto Supremo 1/2015 (Min. Secretaria General de la Presidencia) — Norma tecnica sobre sistemas y sitios web
- Decreto 273/2022 (Min. Interior y Seguridad Publica) — Obligacion de reportar incidentes de ciberseguridad

**Documentos relacionados:** Politica de Seguridad para la clasificacion y manejo de informacion.

## Terminologia

| Termino | Definicion |
|---------|------------|
| Cifrado | Texto escrito con letras, simbolos o numeros que solo se comprende con la llave criptografica necesaria para descifrarlo |
| Cifrar | Procedimiento que usa un algoritmo de cifrado con clave para transformar informacion haciendola incomprensible para quien no tenga la clave secreta |
| Controles criptograficos | Procedimientos y mecanismos para proteger la informacion mediante cifrado y descifrado de datos |
| Datos personales | Informacion concerniente a personas naturales identificadas o identificables, con independencia de su soporte |
| Datos sensibles | Datos personales sobre caracteristicas fisicas o morales, hechos o circunstancias de la vida privada o intimidad (habitos personales, origen racial, ideologias, creencias religiosas, estados de salud, vida sexual) |
| Datos en reposo | Datos almacenados no utilizados activamente (discos duros, cintas magneticas, servidores) |
| Datos en transito | Datos en movimiento entre dispositivos o lugares a traves de redes o canales de comunicacion |
| Tratamiento de datos | Operaciones automatizadas o no que permitan recolectar, almacenar, grabar, organizar, elaborar, seleccionar, extraer, confrontar, interconectar, disociar, comunicar, ceder, transferir, transmitir o cancelar datos de caracter personal |
| Llaves criptograficas | Codigos (algoritmos) generados automaticamente, almacenados en directorio especial durante la instalacion. Secuencia de numeros o letras que especifica la transformacion de texto plano en texto cifrado y viceversa |
| Texto plano | Archivo informatico con texto legible por humanos, sin formato tipografico |

### Niveles de clasificacion de informacion

| Nivel | Definicion |
|-------|------------|
| Secreto | Documentos e informaciones que requieren nivel elevado de proteccion y confidencialidad. No pueden divulgarse salvo en situaciones autorizadas y registradas mediante actos o resoluciones de clasificacion |
| Reservado | Informacion altamente sensible y de uso exclusivamente interno. Su divulgacion podria implicar impacto no deseado para MINSAL o vulnerar normativa vigente. Debe declararse como reservada segun Ley 20.285 |
| Publica | Informacion de acceso publico generada, obtenida, adquirida o controlada por MINSAL. Sin requerimientos de confidencialidad |
| Uso interno | Informacion sin datos sensibles, en proceso de construccion, disponible para empleados y terceros seleccionados. Puede entregarse al publico previa consulta al propietario del activo |

## Roles y responsabilidades

| Rol | Responsabilidad |
|-----|-----------------|
| Departamento TIC | Disponer recursos necesarios para la adecuada administracion de llaves criptograficas |
| Encargado de Seguridad de la Informacion | Velar por el cumplimiento de la politica y gestion adecuada de llaves criptograficas |
| Dueno del activo (Propietario de la informacion) | Custodiar las llaves criptograficas asignadas |
| Administrador del Sistema | Activar, recibir y distribuir llaves criptograficas a usuarios autorizados |

## Directrices de la politica

### Principios generales

- La informacion clasificada segun nivel de confidencialidad debe cifrarse al almacenarse y transmitirse por cualquier medio
- Los sistemas que actualmente cuenten con mecanismos de cifrado deben cumplir esta politica
- El administrador del sistema activa, recibe y distribuye llaves criptograficas a usuarios autorizados, asegurando vigencia durante el periodo establecido
- Las llaves criptograficas deben almacenarse de forma segura, con acceso restringido solo a usuarios autorizados
- Debe almacenarse copia de seguridad de llaves en lugar seguro para recuperacion en caso de extravio

### Cambio, actualizacion y revocacion

- El cambio o actualizacion de llaves debe ser solicitado por el personal responsable o usuarios de estas
- Las claves secretas y privadas deben protegerse contra copia o modificacion no autorizada
- Las llaves seran revocadas por el oficial de seguridad de la informacion o persona delegada cuando:
 - Exista sospecha de acceso por persona no autorizada
 - El colaborador finalice su relacion con la Institucion
- Se mantendra registro de todas las actividades de administracion, gestion y eliminacion de llaves criptograficas

## Gestion de claves

### Ciclo de vida

Implementar gestion de claves con procesos seguros para generar, almacenar, archivar, recuperar, distribuir, retirar y destruir claves criptograficas, basada en normas, procedimientos y metodos preestablecidos.

### Proteccion

| Requisito | Detalle |
|-----------|---------|
| Integridad | Todas las claves criptograficas deben estar protegidas contra modificaciones y perdidas |
| Confidencialidad | Claves secretas y privadas deben contar con proteccion contra uso no autorizado y divulgacion |
| Proteccion fisica | El equipo utilizado para generar, almacenar y archivar claves debe estar protegido fisicamente |
| Autenticidad | Garantizar autenticidad de claves publicas |
| Revocacion | Mecanismos para retirar o desactivar claves comprometidas o cuando el usuario deja la organizacion |

## Mecanismo de difusion

Canales minimos:
- Publicacion en sitio web http://www.minsal.cl/seguridad_de_la_informacion/
- Publicacion en intranet http://isalud.minsal.cl/
- Correo informativo

## Periodo de revision

Revision minima cada dos anos o ante cambios significativos que garanticen:
- Adecuacion al proposito
- Reflejo de cambios en tecnologias, algoritmos y cifradores
- Alineacion con mejores practicas de la industria
- Respaldo del cumplimiento normativo, contractual y legal continuo

Actualizaciones adicionales ante colisiones criptograficas exitosas a algoritmos validos.

## Cumplimiento

El incumplimiento puede resultar en acciones disciplinarias, incluyendo terminacion del empleo o cancelacion del acceso a sistemas de informacion.

## Historial y control de versiones

| Version | Fecha | Creado por | Descripcion |
|---------|-------|------------|-------------|
| 1.0 | 20.03.2023 | Jose Villa C. | Creacion del documento |
