---
_manifest:
  urn: urn:salud:kb:procedimiento-gestion-medios-removibles
  provenance:
    created_by: Codex via koraficacion
    created_at: '2026-06-04'
    source: MINSAL Chile, SGSI Nivel Central. PROS-NC-006 v1
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- procedimiento
- medios-removibles
- usb
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:procedimiento-gestion-medios-removibles
  salud:
    minsal_id: PROS-NC-006
    minsal_version: '1'
    fecha_aprobacion: Octubre 2019
    clasificacion: TLP:BLANCO
    autores:
    - Rodrigo Vidal, Encargado PMG SSI
    - Jose Villa, Area Seguridad de la Informacion
    aprobador: Gabriel Reveco, Encargado Ciberseguridad
relations:
  cites:
  - urn:salud:kb:instructivo-seguridad-informacion-ciberseguridad-sector-salud
---

# Procedimiento Gestion de Medios Removibles

**PROS-NC-006 v1, Octubre 2019. TLP:BLANCO.**

## 1. Proposito

Proteger datos en medios de almacenamiento removibles contra divulgacion no autorizada, modificacion, borrado, destruccion o interrupcion de actividades del negocio.

## 2. Alcance

| Dimension | Detalle |
|---|---|
| Medios cubiertos | Discos externos, pendrives, CDs, DVDs |
| Ambito organizacional | Subsecretaria de Salud Publica y Subsecretaria de Redes Asistenciales |
| Personal aplicable | Funcionarios (planta, contrata, reemplazos, suplencia), personal a honorarios, terceros (proveedores, servicios) con derechos de acceso a informacion |
| Control ISO | A.08.03.01 Administracion de medios extrables (NCh-ISO 27001.Of2013) |

## 3. Terminologia

- **MINSAL** — Ministerio de Salud
- **SGSI** — Sistema de Gestion de Seguridad de Informacion
- **CSIRT** — Equipo de respuesta ante Incidentes

## 4. Documentos Aplicables

- NCh-ISO27001.Of2013 — Requisitos SGSI
- Procedimiento Gestion de Incidentes de Seguridad de la Informacion
- Procedimiento Gestion de Derechos de Acceso y Devolucion de Activos

## 5. Roles y Responsabilidades

| Rol | Responsabilidad |
|---|---|
| Funcionario | Resguardar informacion en medios removibles; usarlos segun este procedimiento; informar deterioro oportuno; gestionar uso, eliminacion de datos, almacenamiento y destruccion del medio |
| Jefatura directa / Coordinador administrativo | Solicitar asignacion de medios removibles para su personal; informar a Unidad de Soporte TIC |
| Departamento de Tecnologias y Comunicaciones | Definir estandares; evaluar y autorizar uso; proponer configuraciones de seguridad; aplicar medidas de proteccion; formatear medios externos y pendrives a solicitud del usuario |

## 6. Procedimiento

### Consideraciones generales

1. Los medios removibles **no son alternativa de respaldo**. La informacion debe mantenerse en los servidores destinados para ello.
2. Los medios removibles se usan **unicamente como medio de transporte** de informacion, no como almacenamiento primario.
3. **Escaneo antivirus obligatorio** cada vez que un medio removible se conecte a un equipo de la red MINSAL.
4. La informacion sensible en medios removibles requiere **cifrado obligatorio**. Las claves de cifrado se resguardan segun el Procedimiento de Gestion de Derechos de Acceso y Devolucion de Activos.
5. Informacion caduca en medio removible: **formatear o destruir** el medio.
6. Almacenar medios removibles en **ambiente seguro** segun especificaciones del fabricante.
7. Informacion que requiera disponibilidad mas alla de la vida util del medio debe **transferirse** a otro medio para evitar perdida.

### Manejo de medios removibles

- Responsabilidad exclusiva del funcionario: almacenamiento y resguardo del medio para evitar acceso no autorizado, dano, perdida o extravio.
- Ante acceso no autorizado, dano, perdida o extravio: **notificar a CSIRT** (`csirt@minsal.cl`) segun Procedimiento de Gestion de Incidentes de Seguridad.
- Medio con informacion caduca: **formatear**. Si el formateo no es posible: **destruir**.

## 7. Registros

- Solicitud para creacion de accesos
- Entrega de credenciales y claves de acceso
- Planilla de registro de eliminacion de accesos
- Registros de entrega y devolucion de equipamiento

## 8. Difusion

Canales minimos obligatorios:

- Publicacion en intranet MINSAL (`http://isalud.minsal.cl`)
- Correo informativo

## 9. Revision y Medicion

Revision minima cada **dos anos** o ante cambios significativos, para asegurar idoneidad, eficiencia y efectividad continua.

## 10. Control de Versiones

| Version | Fecha | Motivo | Secciones |
|---|---|---|---|
| 01 | Octubre 2019 | Creacion del documento | Todas |
