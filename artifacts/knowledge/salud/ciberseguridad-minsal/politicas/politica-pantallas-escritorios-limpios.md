---
_manifest:
  urn: urn:salud:kb:politica-pantallas-escritorios-limpios
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-05'
    source: MINSAL Chile, SGSI Nivel Central. PS-NC-007 v05, Octubre 2019
  minsal_id: PS-NC-007 v5
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
    shard_root_urn: urn:salud:kb:politica-pantallas-escritorios-limpios
relations:
  cites:
  - urn:salud:kb:politica-general-seguridad-informacion-ciberseguridad
---

# Politica de Pantallas y Escritorios Limpios

## Proposito y alcance

Define reglas de uso y control para reducir riesgos de acceso no autorizado, perdida o dano a la informacion durante y fuera de las horas normales de trabajo.

Aplica a: funcionarios (planta, contrata, reemplazos, suplencia), personal a honorarios y terceros (proveedores, compra de servicios) que presten servicios para Subsecretaria de Salud Publica y Subsecretaria de Redes Asistenciales.

Aplica a: informacion en pantalla de estacion de trabajo, informacion impresa o escrita expuesta en escritorios, muebles o medios de almacenamiento removibles.

**Controles ISO 27001:2013 asociados**:

| Dominio | ID Control | Control |
| --- | --- | --- |
| Seguridad fisica y ambiental | A.11.02.01 | Ubicacion y proteccion del equipamiento |
| Seguridad fisica y ambiental | A.11.02.08 | Equipo de usuario desatendido |
| Seguridad fisica y ambiental | A.11.02.09 | Politica de escritorio y pantalla limpios |
| Seguridad de las operaciones | A.12.06.02 | Restricciones sobre la instalacion de software |

## Marco normativo y documentos relacionados

- Documentos del SGSI de MINSAL, disponibles en isalud.minsal.cl
- Politica Nacional de Ciberseguridad (PNCS)
- Marco Juridico referido a los SSI, publicado en portal CSIRT del Ministerio del Interior
- Decretos Supremos y Normas Internacionales de Seguridad de la Informacion y Ciberseguridad
- Leyes relacionadas

## Roles y responsabilidades

**Comite de Seguridad de la Informacion** — Define directrices para tratamiento de informacion en escritorios y pantallas de funcionarios y externos.

**Jefe Departamento de Tecnologias de Informacion** — Implementa directrices de seguridad definidas en esta politica para manejo y proteccion de la informacion.

**Encargado(s) de Seguridad de la Informacion** — Determina requisitos de seguridad para tratamiento de informacion y vela por correcta aplicacion de la politica.

**Usuario** — Protege articulos personales y de la Subsecretaria, y toda informacion institucional que depende de el y/o utiliza.

## Materias que aborda

- Ubicacion y proteccion del equipamiento
- Equipamiento desatendido por el usuario
- Escritorios y pantallas limpias
- Proteccion de seguridad para impresoras
- Salas y pizarras limpias
- Restricciones sobre el uso de equipos y la instalacion de software

## Directrices

### Ubicacion y proteccion del equipamiento

Areas de trabajo de usuarios deben localizarse preferentemente en ubicaciones no expuestas a acceso de personas externas (ver Politica de perimetros de seguridad fisica y proteccion del equipamiento).

Equipos ubicados cerca de zonas de atencion o transito de publico deben situarse con pantallas no visibles por personas no autorizadas y aseguradas, en lo posible, mediante candado de seguridad u otro medio anti-sustraccion.

No ingerir alimentos o bebidas cerca de equipos o dispositivos de procesamiento de informacion, ni colocar o manipular liquidos en su cercania.

### Equipamiento desatendido por el usuario

Al ausentarse del puesto de trabajo, el usuario debe bloquear la estacion de trabajo para proteger acceso a aplicaciones y servicios.

Estaciones de trabajo y equipos portatiles deben tener aplicado el protector de pantalla definido por el Encargado de Seguridad de la Informacion, activable ante tiempo sin uso.

La pantalla de autenticacion a la red institucional debe requerir solo identificacion de cuenta y clave; no entregar ni solicitar otra informacion.

La autenticacion de usuario debe requerirse cada vez que el equipamiento se encienda, reinicie, bloquee o despues de activarse el protector de pantalla.

### Escritorios y pantallas limpias

Al ausentarse del puesto, junto con bloquear la estacion, el usuario debe guardar en lugar seguro documentos, medios magneticos u opticos removibles con informacion confidencial.

Al finalizar la jornada, guardar en lugar seguro documentos y medios con informacion confidencial o de uso interno, y desconectarse de computadores centrales, servidores y estaciones de trabajo al cerrar sesion (no apagar solo el monitor).

**Lugar seguro**: aquel que protege el activo de informacion de accesos no autorizados, evita alteracion de contenido y permite recuperacion oportuna por personas autorizadas (ej. caja fuerte, archivador, mueble seguro, oficina con llave).

En zonas de atencion de publico, al ausentarse guardar tambien documentos y medios con informacion de uso interno.

Equipos de reproduccion de informacion (impresoras, fotocopiadoras) deben ubicarse en lugares con acceso controlado. Documentacion confidencial o sensible debe retirarse inmediatamente del equipo.

### Proteccion de seguridad para impresoras

Impresoras en atencion o transito de publico deben quedar protegidas de acceso no autorizado.

Informacion impresa debe ser retirada de la impresora en forma inmediata para evitar acceso por personas no autorizadas.

Cuando sea posible y se trate de informacion sensible, implementar control de impresion con clave por usuario.

### Salas y pizarras limpias

Salas o areas de reuniones y capacitacion deben quedar limpias de todo material utilizado.

Pizarras deben quedar limpias de informacion expuesta despues de cada reunion.

Si se utiliza estacion de trabajo de uso comun para presentaciones, eliminar la informacion presentada al terminar.

### Restricciones sobre el uso de equipos y la instalacion de software

Usuarios no deben intentar transgredir o sabotear medidas de seguridad de los sistemas, ni utilizar herramientas, programas o dispositivos para evadir controles, interceptar o decodificar contrasenas o acceder a informacion no autorizada.

Conductas inapropiadas:

- Utilizar el computador en actividades ajenas al ambito de trabajo
- Usar equipos de la Organizacion en actividades de lucro personal
- Desinstalar o inhabilitar aplicaciones de seguridad del computador institucional (ej. antivirus)
- Instalar software no autorizado por el Departamento TIC
- Ceder, prestar o permitir el uso del equipo por terceras personas
- Modificar configuracion del sistema operativo u otras aplicaciones del software operativo basico
- Abrir el equipo y/o cambiar hardware o dispositivos que lo componen
- Utilizacion no autorizada de acceso a paginas Web

## Mecanismo de difusion

- Publicacion en intranet MINSAL http://isalud.minsal.cl/
- Correo informativo

## Periodo de revision

Revision a lo menos cada dos anos por el Comite de Seguridad de la Informacion, o segun necesidades de cambio para garantizar idoneidad, adecuacion y efectividad.

## Excepciones

El Comite de Seguridad de la Informacion evaluara y podra establecer condiciones puntuales de excepcion, siempre que no infrinja la legislacion vigente. Toda excepcion debe documentarse y generar un proceso de revision que determine si se deben agregar directrices particulares.

## Historial de versiones

| Version | Fecha | Cambios |
| --- | --- | --- |
| 1 | Octubre 2011 | Creacion del documento |
| 2 | Agosto 2013 | Alineacion con nueva estructura del SGSI declarada en politica general. Inclusion de Encargado de Seguridad y Usuario en responsabilidades. Inclusion de explicacion de "lugar seguro". Inclusion de equipos de reproduccion de informacion. Inclusion de definicion de pantalla y escritorio limpio |
| 3 | Octubre 2014 | Inclusion de controles A.11.3.2 y A.9.2.1 de NCh-ISO 27001.Of2009 |
| 4 | Octubre 2017 | Actualizacion referencia normativa a version 2013 de ISO 27001. Actualizacion referencias normativas. Ajuste formato y codigo. Ajuste de contenidos a nuevos requisitos de la norma |
| 5 | Octubre 2019 | Inclusion de control A.12.06.02. Actualizacion de mecanismos de difusion a politica para el Nivel Central |
