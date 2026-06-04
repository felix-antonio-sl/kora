---
_manifest:
  urn: urn:salud:kb:procedimiento-contra-codigo-malicioso
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-04'
    source: MINSAL Chile, SGSI Nivel Central. PROS-NC-001 v1
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- procedimiento
- codigo-malicioso
- malware
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:procedimiento-contra-codigo-malicioso
  salud:
    minsal_id: PROS-NC-001
    minsal_version: '1'
relations:
  cites:
  - urn:salud:kb:instructivo-seguridad-informacion-ciberseguridad-sector-salud
---

# Procedimiento Contra Codigo Malicioso

**PROS-NC-001 v1, Octubre 2019.**

Prevenir, detectar y corregir corrupcion de informacion por malware en ambientes de procesamiento.

| Dimension | Detalle |
|---|---|
| Equipos | Computadores de escritorio y moviles en red MINSAL, propios o de terceros |
| Organizacion | Subsecretaria de Salud Publica, Subsecretaria de Redes Asistenciales |
| Personal | Funcionarios (planta, contrata, reemplazos, suplencia), honorarios, terceros con acceso a activos de informacion |
| Controles ISO | NCh-ISO 27001.Of2013: A.12.02.01 Controles contra codigo malicioso, A.12.06.02 Restricciones sobre instalacion de software |
| Firmas | Elaboro: Rodrigo Vidal / Encargado PMG SSI. Reviso: Jose Villa / Area Seguridad de la Informacion (Representante Comite de Seguridad). Aprobo: Gabriel Reveco / Encargado Ciberseguridad (Presidente Comite de Seguridad de la Informacion). Octubre 2019 |

"Funcionario" abarca: planta, contrata, reemplazos, suplencia, honorarios y terceros (proveedores, compra de servicios).

## Terminologia

- **MINSAL** — Ministerio de Salud
- **SGSI** — Sistema de Gestion de Seguridad de Informacion
- **Malware** — programa o codigo malicioso danino para los sistemas

## Documentos Aplicables

- NCh-ISO27001.Of2013 — Tecnologia de la informacion, Tecnicas de seguridad, SGSI — Requisitos
- Procedimiento para el control de software operacional
- Politica de pantallas y escritorios limpios
- Procedimiento Gestion de Incidentes de Seguridad de la Informacion

## Roles y Responsabilidades

Cumplimiento obligatorio para: todos los usuarios, Administradores de Seguridad, Custodio de los Datos, Unidades de Informatica, Jefe de Servicio, Directores, Jefes de Division, Jefes de Departamento y Gestion de Personas.

## Procedimiento

#### Programa de control de malware

Sistema antivirus automatico, estandarizado y residente en equipos centralizados y estaciones de trabajo, activo durante todo el uso; cubre estaciones, servidores y archivos entrantes/salientes por correo electronico.

- Actualizacion remota o manual con periodicidad del proveedor; mantener version mas actualizada en todos los equipos. Encargado de Seguridad de la Informacion / Ciberseguridad verifica vigencia aleatoriamente. Recomendado: servidor local de actualizaciones.
- Escaneo AntiMalware completo semanal programado por personal TIC de cada unidad.
- Monitorear vigencia del contrato con proveedor AntiMalware.
- Facilitar extension de licencias AntiMalware a PC domesticos de usuarios identificados.
- Empresas externas que requieran conexion a red MINSAL: exigir AntiMalware actualizado; conectarse en red segmentada (zona de recursos limitados), aislada de equipos internos. Si no requieren equipo propio, proveer uno con medidas de seguridad definidas.

#### Tratamiento de dispositivos de almacenamiento o informacion externa dudosa

CD, pen drive, tarjetas de memoria o informacion externa dudosa (ej. de empresas afectadas por malware): remitir al Departamento TIC para revision. Bloquear en firewalls contenido riesgoso, especialmente archivos ejecutables.

#### Recuperacion de danos por malware

- Mantener plan de recuperacion: copias de respaldo de datos operativos + reinstalacion de software base y aplicativo.
- Departamento TIC analiza: magnitud del dano, cantidad de equipos afectados, alcance del virus, consecuencias posteriores, fecha de ocurrencia.
- Evaluar integridad de archivos/programas post-eliminacion. Encargado de Seguridad de la Informacion / Ciberseguridad genera plan detallado de prueba; Administrador de Seguridad en la unidad ejecuta.
- Imprimir archivo de log del software AntiMalware.
- Contaminacion masiva: comunicar inmediatamente estado y acciones al Encargado de Seguridad de la Informacion / Ciberseguridad para coordinar respuesta.
- Perdida de informacion durante eliminacion: Administrador de Seguridad solicita copia de seguridad de archivos danados al custodio.
- Reinstalacion de sistemas aplicativos, software base y copias de seguridad: solicitud al Custodio Fisico de respaldos con firma de autorizacion del Encargado de Seguridad de la Informacion / Ciberseguridad.
- Todo incidente de malware: investigacion segun Procedimiento de Gestion de Incidentes de Seguridad de la Informacion para determinar responsables y aplicar sanciones.
- Evaluar contaminacion reiterada por usuario para adoptar medidas anti-reincidencia.

#### Sensibilizacion de usuarios

Sensibilizar sobre riesgos de perdida de informacion por malware y comunicar metodologia de combate.

- Escaneo de discos: periodico, al recibir archivos de sitios externos, al bajar de Internet, al usar dispositivos de terceros.
- No divulgar ni considerar informacion de malware de fuente distinta al Administrador de Sistemas. Ante alerta externa: contactar Soporte TIC para evaluacion de veracidad y acciones.
- Prohibido: trasgredir o sabotear medidas de seguridad, evadir controles, interceptar o decodificar contrasenas, acceder a informacion no autorizada.

| Conducta inapropiada |
|---|
| Desinstalacion o inhabilitacion consciente de aplicaciones de seguridad (ej. antivirus) |
| Instalacion de software no autorizado por Departamento TIC |
| Cesion, prestamo o utilizacion del equipo por terceros (amigos, parientes, conocidos) |
| Modificacion de configuracion del sistema operativo o aplicaciones del software operativo basico |
| Apertura del equipo o cambio de hardware/dispositivos |
| Utilizacion no autorizada de acceso a paginas Web |

## Registros

- Inventario de software antimalware
- Registro de instalacion de software antimalware
- Solicitud para creacion de accesos
- Entrega de credenciales y claves de acceso
- Registro de incidencias de malware en la red interna
- Tickets de revision de equipo por ataque de malware

## Difusion

Publicacion en intranet MINSAL (`http://isalud.minsal.cl`) y correo informativo.

## Revision y Medicion

Revision minima cada dos anos o ante cambios significativos, para asegurar idoneidad, eficiencia y efectividad continua.

## Control de Versiones

| Version | Fecha de Aprobacion | Motivo del cambio | Secciones modificadas |
|---|---|---|---|
| 01 | Octubre 2019 | Creacion del documento | Todas |
