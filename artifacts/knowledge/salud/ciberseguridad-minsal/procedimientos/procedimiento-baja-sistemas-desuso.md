---
_manifest:
  urn: urn:salud:kb:procedimiento-baja-sistemas-desuso
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-04'
    source: MINSAL Chile, SGSI Nivel Central. PROS-NC-008 v1
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- procedimiento
- baja-sistemas
- retiro
- disposicion
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:procedimiento-baja-sistemas-desuso
  salud:
    minsal_id: PROS-NC-008
    minsal_version: '1'
    fecha_aprobacion: '2024-01-15'
    clasificacion: Publica
    elaborador: Pablo Fabres / Jose Villa C.
    revisor: Catalina Arenas A. / Rodrigo Baeza
    aprobador: Jorge Herrera R. / Rodrigo Zamorano A.
relations:
  cites:
  - urn:salud:kb:instructivo-seguridad-informacion-ciberseguridad-sector-salud
---

# Procedimiento para Baja de Sistemas en Desuso — PROS-NC-008 v1

Sistema de Gestion de Seguridad de la Informacion — MINSAL Nivel Central. 15 de enero de 2024.

## Proposito y Alcance

Atender requerimientos de retiro o baja de sistemas publicados a internet por cese de prestacion de servicio o no uso en servidores o equipos del MINSAL. Objeto: garantizar seguridad de la informacion, cumplir estandares organizacionales y mitigar riesgos asociados a activos no utilizados.

| Ambito | Detalle |
|---|---|
| Cobertura | Sistemas publicados a internet bajo propiedad y/o gestion de MINSAL, Subsecretaria de Salud Publica y Subsecretaria de Redes Asistenciales |
| Controles ISO 27001:2022 | A.8.1.3 Uso aceptable de activos; A.12.1.2 Gestion de cambios; A.12.3.1 Respaldo de la informacion; A.18.1.2 Derechos de propiedad intelectual |

## Terminologia

**Sistema** — activos de informacion bajo alcance, en cualquier tecnologia: pagina/sistema/portal web, aplicativo, software, servicios web (SOAP, REST u otros), tokens o certificados de seguridad (SSL), API, servicio informatico.

**Baja de Sistema** — proceso de retirar un sistema de operacion activa. Implica desactivacion, interrupcion de servicios asociados y eliminacion de datos almacenados. Requiere actividades para proteger la seguridad de la informacion y garantizar el buen uso de los recursos.

## Marco Normativo

| Documento | Referencia |
|---|---|
| NCh-ISO 27001.Of2022 | Requisitos de seguridad de la informacion |
| Decreto 1/2015 SEGPRES | Norma tecnica sobre sistemas y sitios web de organos de administracion del Estado |
| Decreto 83/2004 SEGPRES | Norma tecnica sobre seguridad y confidencialidad de documentos electronicos |
| Decreto 7/2023 SEGPRES | Norma tecnica de seguridad de la informacion y ciberseguridad |

## Roles y Responsabilidades

| Rol | Responsabilidad |
|---|---|
| Nivel Directivo | Generar condiciones para ejecucion y comunicacion del procedimiento |
| Encargado de Seguridad de la Informacion / Ciberseguridad | Velar por aplicacion del procedimiento; asesorar en identificacion de amenazas por obsolescencia tecnologica, S.O. no soportados o vulnerabilidades reportadas; informar al Comite de Seguridad de la Informacion sobre sistemas en desuso o revocaciones tramitadas |
| Duenos de los sistemas | Aplicar el procedimiento; solicitar baja oportunamente cuando se requiera |
| Departamento de Tecnologias de Informacion y Comunicaciones | Control sobre dominios de sistemas ministeriales; reglas para seguridad y privacidad; baja de sistemas; custodia, administracion, desinstalacion y control; puede disponer baja si verifica que el sistema ya no esta en uso |
| Unidad de Operaciones | Actividades tecnicas de desactivacion y decomiso controlado y seguro; extraccion, custodia y eventual migracion de datos a nuevos sistemas; eliminacion segura de datos segun politicas de retencion |

## Criterios para Determinacion de Baja

### Criterios normativos y de uso

| Criterio | Condiciones |
|---|---|
| Inactividad Prolongada | Sistema inactivo >1 trimestre sin justificacion valida. Verificar: (i) al menos un trimestre sin uso; (ii) inexistencia de interoperabilidad o dependencia con otros sistemas — si existe, ejecutar desacople previo; (iii) baja en todos los ambientes tecnologicos donde resida; (iv) si prestaba servicio o tramite a usuarios via portal web, el dueno informa con debida anticipacion por medios institucionales la baja, motivos y reemplazo |
| Violacion de Seguridad | Baja inmediata si se detecta violacion que ponga en riesgo confidencialidad, integridad o disponibilidad de la informacion |
| Cambio en Estrategia Institucional | Revocacion segun planificacion establecida |
| Incumplimiento de Politicas y Normativas | Revocacion tras revision exhaustiva |
| Termino de Periodo de Vigencia | Baja al finalizar periodo para sistemas de apoyo a procesos temporales o transitorios (campanas estacionales, emergencia) |

### Criterios tecnicos

| Criterio | Descripcion |
|---|---|
| Obsolescencia tecnologica | Software reemplazado totalmente por nueva version; deja de soportar procesos de negocio; dificil integracion con nuevas soluciones de transformacion digital |
| Reemplazo o consolidacion | Nueva aplicacion reemplaza al sistema (reemplazo) o modulos de otra aplicacion cubren totalmente su funcionalidad (consolidacion) |
| Incompatibilidad con hardware | Nuevas versiones de equipos presentan problemas o incompatibilidad con software obsoleto; riesgo de fallas, suspension de soporte y garantia |
| Lentitud en ejecucion | Software obsoleto no asegura desempeno; aumenta carga laboral o genera tiempos muertos en procesos |
| Alta vulnerabilidad y falta de actualizaciones | Mayor antiguedad implica mas vulnerabilidades; parches solo en versiones actuales; S.O. obsoletos o no soportados aumentan superficie de riesgo sobre confidencialidad, integridad y disponibilidad |
| Perdida de soporte | Fabricantes terminan mantenimiento tecnico y generacion de parches de seguridad para versiones antiguas |

## Procedimiento de Baja

### Condiciones Generales

Origen de baja: monitoreo de no uso por Departamento TIC o solicitud directa de duenos de activos. El sistema solicitado debe estar registrado en el inventario de sistemas del Departamento TIC.

Software no autorizado: rige Procedimiento de Pantalla y Escritorio Limpio, punto 6.3 (Restricciones sobre uso de equipos e instalacion de software).

### Documentacion obligatoria de baja

Toda baja debe documentarse con al menos:

| Elemento | Contenido |
|---|---|
| Informacion del sistema | Nombre, numero en inventario de activos, fecha de registro, procesos en que se utiliza |
| Dueno del sistema | Unidad responsable, identidad de la persona que solicita la baja |
| Decision de baja | Fundamentos, fecha de decision, fecha prevista para desactivacion |
| Datos e informacion | Datos a custodiar, periodo de retencion, destino final (respaldo, migracion o eliminacion), responsable del proceso de extraccion y custodia |

### Flujo de baja

#### Solicitud de baja

El dueno del sistema solicita directamente la baja indicando la causal, via requerimiento a mesa de ayuda por correo institucional, que escala a la coordinacion del Departamento TIC correspondiente.

#### Verificacion previa

La Unidad de Operaciones:

- Determina el estado operativo del sistema y su infraestructura asociada
- Revisa los motivos documentados y los compara con los criterios tecnicos del presente procedimiento
- Elabora un informe y mantiene registros de resultados de evaluacion y acciones tomadas
- Realiza revision interna para confirmar validez de la decision y abordar implicaciones
- Informa resultados al director/a del Departamento TIC y al Encargado/a de Seguridad de la Informacion

#### Notificacion y revision

El director/a del Departamento TIC, en conjunto con el Encargado/a de Seguridad de la Informacion, notifica al dueno del activo la decision de aceptacion o rechazo de la baja y los pasos a seguir.

#### Comunicacion externa

El dueno del activo informa a los usuarios y partes interesadas sobre la baja de manera previa, transparente y clara.

#### Decomiso del sistema

El acceso al sistema se desactiva de manera controlada y segura. Las areas tecnologicas deben ajustarse al procedimiento de Gestion de Cambios en Ambientes Productivos (CAB) para aprobacion de la baja.

**Fases del decomiso:**

1. **Copias de Seguridad** — respaldo completo de datos criticos y configuraciones del sistema. Almacenamiento seguro en entorno controlado. Documentar ubicacion, fecha y contenido de cada respaldo.

2. **Identificacion de Recursos Sensibles** — catalogar datos de usuarios, informacion confidencial o propietaria almacenados. Asignar responsabilidades claras para gestion y proteccion durante la desactivacion.

3. **Respaldo y Retencion de Informacion** — respaldo de datos criticos antes de la baja. Verificar funcionalidad del respaldo. Almacenamiento seguro. Eliminacion en el sistema dado de baja segun politicas de retencion. Los datos respaldados se retienen segun politicas de retencion de la organizacion. Documentar la politica de retencion. Eliminacion segura de respaldos cuando ya no sean necesarios.

4. **Desactivacion Controlada** — coordinar via CAB con Unidad de Operaciones de TI, Explotacion e Infraestructura, Unidad de Proyectos y Unidad de Seguridad de la Informacion. Elaborar plan de desactivacion con pasos especificos para garantizar continuidad operativa y minimizar impacto negativo.

5. **Desconexion de Accesos Externos** — desconectar dominios, enlaces y servicios de red relacionados. Implementar medidas de seguridad adicionales: cortafuegos y restricciones de acceso para prevenir accesos no autorizados post-desactivacion.

6. **Desactivacion de Servicios Relacionados** — desactivar o retirar bases de datos, servidores de aplicaciones y servicios de alojamiento. Gestionar conexiones o integraciones con otros sistemas para evitar interrupciones no planificadas.

7. **Eliminacion de Contenido Sensible** — eliminar o proteger contenido sensible o critico almacenado antes de la desactivacion. Seguir procedimientos de eliminacion segura de datos para garantizar confidencialidad y cumplir politicas de privacidad.

8. **Verificacion de la Desactivacion** — verificacion exhaustiva de que todos los recursos relacionados se hayan desconectado y desactivado correctamente. Pruebas de seguridad para descartar brechas o riesgos de seguridad residuales.

9. **Baja del Inventario de Activos** — marcar como inactivo el sistema en el inventario de aplicaciones o de activos.

## Dominios: Creacion y Eliminacion

### Creacion de dominios

| Regla | Detalle |
|---|---|
| Dominio gob.cl | Obligatorio segun art. 13 Decreto Supremo N°1 SEGPRES. Registro previo ante Division de Informatica del Ministerio del Interior y Seguridad Publica via formulario en nic.gob.cl |
| Dominio minsal.cl | Gestionar incorporacion a traves del Departamento TIC |
| Prohibicion NIC Chile | Regla general: no registrar nombre de dominio para fines institucionales en el sistema de Nic Chile. Excepcion: si se registra, responsabilidad de custodia y mantencion recae en la jefatura de la unidad correspondiente |

Objeto: prevenir usurpacion de identidad, mal uso, abuso de prestigio y marca, y toda accion ajena al MINSAL.

### Eliminacion de dominios

| Caso | Procedimiento |
|---|---|
| Dominios .cl | Formalizar decision por parte del dueno; informar al Departamento TIC; tramitar eliminacion en NIC Chile. El titular que inscribio el dominio debe requerir a NIC Chile la eliminacion. Si no lo hace en 5 dias corridos desde expiracion, NIC Chile desactiva el dominio |
| Dominios minsal.cl, gob.cl, gov.cl | Proceder segun flujo de baja (§6.4) e incluir eliminacion del registro DNS asociado. Verificar eliminacion correcta de todos los registros DNS y que los nombres de dominio ya no esten activos en la infraestructura DNS |
| Dominio reclamado por tercero | Si un tercero registra el dominio eliminado y el dueno estima afectacion de derechos de MINSAL o fe publica, debe solicitar revocacion temprana o tardia ante NIC Chile, sujeto a la Politica de Resolucion de Controversias por Nombres de Dominio .cl. Requiere solicitud del dueno a NIC Chile por los medios dispuestos y pago de tarifa respectiva |

Responsabilidad del dueno: anunciar la baja, motivos y reemplazo del servicio por medios de comunicacion institucionales.

## Registros, Difusion y Revision

**Registros:**
- Catastro de Sistemas del MINSAL
- Registros de sistemas en decomiso
- Catastro de dominios inscritos en NIC Chile

**Difusion** — canales minimos:
- Publicacion en sitio web MINSAL: `http://www.minsal.cl/seguridad_de_la_informacion/`
- Publicacion en intranet MINSAL: `http://isalud.minsal.cl/`

**Revision** — minima cada un ano por el Comite de Seguridad de la Informacion, o ante necesidades de cambios para garantizar versionamiento.

## Control de Versiones

| Version | Fecha | Elaborador | Modificacion |
|---|---|---|---|
| 1.0 | 15.01.2024 | Pablo Fabres / Jose Villa C. | Creacion del documento |
