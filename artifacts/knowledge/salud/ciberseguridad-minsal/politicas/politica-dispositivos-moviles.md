---
_manifest:
  urn: urn:salud:kb:politica-dispositivos-moviles
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-05'
    source: MINSAL Chile, SGSI Nivel Central. PS-NC-017 v1
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
    shard_root_urn: urn:salud:kb:politica-dispositivos-moviles
  salud:
    minsal_id: PS-NC-017
    minsal_version: '1'
    fecha_aprobacion: Marzo 2023
    elaborador: Jose Villa
    revisor: Jose Villa (Encargado Seguridad de la Informacion), Carlos Maldonado
      (Encargado Operaciones), Rodrigo Zamorano (Encargado Proyectos)
    aprobador: Jorge Herrera (Jefe Departamento TIC)
    clasificacion: Publica
relations:
  cites:
  - urn:salud:kb:politica-general-seguridad-informacion-ciberseguridad
---

# Politica de Dispositivos Moviles — PS-NC-017 v1

Sistema de Gestion de Seguridad de la Informacion — MINSAL Nivel Central. Marzo 2023.

## Definicion y ambito de aplicacion

Establecer normas y responsabilidades para el uso correcto, seguro y apropiado de dispositivos moviles de propiedad institucional o utilizados en nombre del MINSAL.

| Cobertura | Detalle |
|-----------|---------|
| Organismos | Subsecretaria de Salud Publica, Subsecretaria de Redes Asistenciales |
| Personal | Funcionarios (planta, contrata, reemplazos, suplencia), honorarios, terceros (proveedores, compra de servicios) que utilicen dispositivos moviles para actividades laborales |
| Control ISO 27001 | 8.1 Politica de dispositivos moviles (NCh-ISO IEC 27002:2022) |

## Marco normativo y documentos relacionados

**Normas tecnicas:**
- NCh-ISO 27001:2013 — Tecnologia de la informacion, Tecnicas de seguridad, SGSI, Requisitos
- NCh-ISO IEC 27002:2013 — Seguridad de la informacion, ciberseguridad y proteccion de la privacidad, Controles de seguridad de la informacion

**Leyes:**
- Ley 19.628 — Proteccion de vida privada y datos personales
- Ley 19.799 — Firmas y documentos electronicos
- Ley 19.927 — Delitos de Pornografia Infantil
- Ley 20.285 — Transparencia de la funcion publica y acceso a la informacion
- Ley 21.180 — Transformacion Digital del Estado
- Ley 21.459 — Delitos Informaticos (adecua Convenio de Budapest)

**Decretos:**
- Decreto 83/2004 (Min. Secretaria General de la Presidencia) — Norma tecnica sobre seguridad y confidencialidad de documentos electronicos
- Decreto 273/2022 (Min. Interior y Seguridad Publica) — Obligacion de reportar incidentes de ciberseguridad

**Marco adicional:** Marco Juridico referido a los SSI, publicado en el portal CSIRT del Ministerio del Interior.

**Documentos relacionados:**
- Politica de Seguridad para la clasificacion y manejo de informacion
- Politica de Seguridad en la Red

## Terminologia

| Termino | Definicion |
|---------|------------|
| Dispositivo movil | Elemento electronico de tamano pequeno con capacidades de procesamiento de datos, conexion a Internet y memoria. Ejemplos: smartphones, tabletas, computadores portatiles |
| Informacion | Conjunto de datos que organizados en un contexto tienen significado |
| Ingenieria social | Practica de obtener informacion confidencial mediante manipulacion de usuarios legitimos. Tecnica para obtener datos, acceso o privilegios a sistemas que permite ejecutar acciones maliciosas contra la informacion e infraestructura tecnologica |

### Niveles de clasificacion

| Nivel | Definicion |
|-------|------------|
| Secreto | Documentos que requieren proteccion y confidencialidad elevadas. No divulgables salvo en situaciones autorizadas y registradas |
| Reservado | Informacion altamente sensible de uso exclusivamente interno. Su divulgacion podria implicar impacto no deseado para MINSAL o vulnerar normativa. Debe declararse como reservada segun Ley 20.285 |
| Publica | Informacion de acceso publico, sin requerimientos de confidencialidad |
| Uso interno | Informacion sin datos sensibles, disponible para empleados y terceros seleccionados. Entregable al publico sujeta a normativa vigente previa consulta al propietario del activo |

## Roles y responsabilidades

| Rol | Responsabilidad |
|-----|-----------------|
| Division de Administracion y Finanzas / Depto. TIC | Proporcionar dispositivos moviles seguros y actualizados. Mantener registro de dispositivos asignados (equipo y persona). Mantenimiento restringido al departamento responsable |
| Funcionarios | Proteger y mantener dispositivos moviles entregados por MINSAL. Informar inmediatamente cualquier perdida, robo, dano o incidente de seguridad a Jefatura directa y Depto. TIC |
| Encargado de Seguridad de la Informacion | Velar por el cumplimiento de la politica y gestion adecuada de dispositivos moviles |

## Directrices de la politica

### Uso autorizado

| Regla | Detalle |
|-------|---------|
| Responsabilidad del usuario | El usuario garantiza la seguridad del equipo y de la informacion que contiene fuera de las instalaciones |
| Uso laboral exclusivo | Prohibido uso personal |
| Acceso a datos | Solo datos institucionales necesarios para tareas laborales autorizadas |
| Comparticion | Prohibido compartir dispositivos moviles institucionales sin autorizacion expresa |
| Exposicion termica | No exponer el equipo a altas temperaturas que puedan danar sus componentes |
| Proteccion de acceso | Adoptar medidas para evitar acceso no autorizado por terceros a la informacion almacenada |
| Custodia fisica | No descuidar ni dejar el dispositivo visible o facilmente accesible en el automovil. En lugares sin custodia garantizada: anclar con candado de seguridad o guardar en armario seguro |

### Seguridad de los dispositivos moviles

| Requisito | Detalle |
|-----------|---------|
| Contrasenas seguras | Proteccion obligatoria |
| Software de seguridad actualizado | Proteccion obligatoria |
| Prohibicion de jailbreak/rooteo | No intervenir para eliminar restricciones del desarrollador (jailbreaking en iOS, rooteo en Android). Compromete seguridad, estabilidad y viola terminos del fabricante |
| Conexiones a redes externas | Seguir normas de la politica de seguridad de la red |
| Cifrado | Dispositivos moviles deben estar cifrados para proteger datos institucionales |
| Reporte de incidentes | Informar inmediatamente cualquier sospecha de vulnerabilidad o incidente. Ante sospecha de virus/malware, notificar a la mayor brevedad al personal tecnico responsable |
| Integridad del equipo | Prohibido modificar hardware, instalar software o cambiar configuracion sin autorizacion del departamento competente |
| Copias de seguridad | Asegurar copias de seguridad de la informacion almacenada, protegidas y almacenadas adecuadamente |
| Eliminacion de datos | Eliminar datos cuando ya no sean necesarios, de manera segura y efectiva |

### Perdida, robo o dano

| Obligacion | Detalle |
|------------|---------|
| Reporte inmediato | Informar cualquier perdida, robo o dano |
| Proteccion de datos | Tomar medidas para proteger datos institucionales ante perdida o presunta sustraccion |
| Borrado remoto | MINSAL se reserva el derecho de borrar datos de dispositivos perdidos o robados |

### Tratamiento de informacion confidencial

- Toda informacion confidencial debe almacenarse cifrada
- Antes de devolucion del dispositivo: eliminar informacion de forma segura o solicitar eliminacion al tecnico responsable
- No almacenar informacion institucional no estrictamente necesaria para las tareas del usuario
- Si se accede a la informacion desde varios dispositivos: mantener sincronizada para evitar duplicidades y errores de version

## Mecanismo de difusion

Canales minimos:
- Publicacion en sitio web https://www.minsal.cl/seguridad_de_la_informacion/
- Publicacion en intranet http://isalud.minsal.cl/
- Correo informativo

## Periodo de revision

Revision minima cada dos anos o ante cambios significativos para garantizar:
- Adecuacion al proposito y precision
- Reflejo de cambios en las tecnologias
- Alineacion con las mejores practicas de la industria

## Cumplimiento

El incumplimiento puede resultar en acciones disciplinarias, incluyendo terminacion del empleo o cancelacion del acceso a sistemas de informacion.

## Historial y control de versiones

| Version | Fecha | Creado por | Descripcion |
|---------|-------|------------|-------------|
| 1.0 | 20.03.2023 | Jose Villa C. | Creacion del documento |
