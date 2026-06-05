---
_manifest:
  urn: urn:salud:kb:politica-respaldo-informacion-software
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-05'
    source: MINSAL Chile, SGSI Nivel Central. PS-NC-004 v5
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- politica
- respaldo
- backup
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:politica-respaldo-informacion-software
  salud:
    minsal_id: PS-NC-004
    minsal_version: '5'
relations:
  cites:
  - urn:salud:kb:politica-general-seguridad-informacion-ciberseguridad
---

# Politica de Respaldo de Informacion y Software -- PS-NC-004 v05

Sistema de Gestion de Seguridad de la Informacion -- MINSAL Nivel Central. Noviembre 2024.

## Proposito y alcance

Definir reglas para generacion, resguardo, mantenimiento y recuperacion de informacion almacenada en unidades de respaldo, para garantizar continuidad operativa ante contingencias o interrupciones del servicio de procesamiento.

Aplica a toda la informacion electronica en servidores, estaciones de trabajo y equipos comunicacionales que contengan datos, configuraciones, aplicativos y servicios criticos para MINSAL. Aplica a todos los funcionarios (planta, contrata, reemplazos, suplencia), personal a honorarios y terceros de la Subsecretaria de Salud Publica y Subsecretaria de Redes Asistenciales.

### Control ISO 27002:2022 asociado

| Control | Nombre |
|---|---|
| A.08.13 | Copias de Seguridad de la Informacion |

## Marco normativo

| Instrumento | Referencia |
|---|---|
| ISO 27001:2022 | Seguridad de la informacion, ciberseguridad y proteccion de la privacidad |
| Marco Juridico SSI | Portal CSIRT del Ministerio del Interior |
| Ley 21.663 | Marco de Ciberseguridad |
| Ley 20.285 | Acceso a la informacion publica |
| Ley 19.799 | Documentos electronicos, firma electronica y servicios de certificacion |
| Decreto 181 | Reglamento de la Ley 19.799 |
| Ley 19.628 | Proteccion de la vida privada (Ley 21.719 cambia nombre, vigente desde 01/12/2026) |
| Ley 19.880 | Bases de los procedimientos administrativos |
| Decreto 83, 2004 | Norma tecnica sobre seguridad y confidencialidad de documentos electronicos |
| Decreto 273, 2022 | Obligacion de reportar incidentes de ciberseguridad al CSIRT |
| Decreto Supremo N° 7 | Norma Tecnica de Seguridad de la Informacion y Ciberseguridad |

Documentos relacionados: Procedimiento para la eliminacion segura y reutilizacion de equipos. Documentos SGSI disponibles en `isalud.minsal.cl`.

## Roles

| Rol | Responsabilidad |
|---|---|
| Departamento TIC | Definir estandar de respaldo (software, aplicaciones, configuraciones, datos en Produccion, QA y Desarrollo); autorizar solicitudes de respaldo especiales; aprobar planes de respaldo y restauracion con la autoridad y el negocio |
| Operaciones TIC | Generar planes de respaldo y restauracion; coordinar, ejecutar y documentar cada proceso; realizar pruebas regulares de calidad; llevar registros de respaldos y pruebas; notificar problemas de calidad al negocio y Encargado de Seguridad |
| Encargado de Seguridad / Ciberseguridad | Definir tipo y periodicidad de respaldos para cada aplicacion o plataforma con el negocio |
| Auditoria Interna | Verificar cumplimiento de las disposiciones de la politica (generacion, almacenamiento, control periodico, recuperacion conforme a estandares) |
| Divisiones y Departamentos | Trabajar con TI, Seguridad y Legal para garantizar adopcion de practicas seguras |
| Usuarios | Adherirse a la politica; manejo seguro de datos; notificar incidentes de perdida o corrupcion de informacion |

## Materias que aborda

Respaldo de la informacion.

## Directrices

### Cumplimiento legislativo

Las medidas de control deben ser consistentes con la Normativa del SGSI.

### Consideraciones generales

| Regla | Detalle |
|---|---|
| Responsabilidad primaria | Departamento TIC: respaldo de servidores e infraestructura bajo su gestion. Otras areas: respaldar datos propios no centralizados en servidores TIC |
| Servidores externalizados | Departamento TIC verifica realizacion de respaldos; proveedor envia periodicamente jobs de respaldo y resultados |
| Clasificacion de importancia | Alta, Media, Baja. Mecanismo, periodicidad y tecnologia de respaldo depende de la importancia asignada |
| Registro de respaldos | Cada respaldo (manual o automatico) registrado en LOGS de servidores, informes de reporte diario o archivos electronicos. Servicio externo: registro de retiro de cintas |
| Medios removibles | Retirados del recinto de respaldo a otro que garantice catalogo, fiabilidad, seguridad y disponibilidad |
| Exclusiones | Claves de usuario NO se respaldan. Informacion no relevante para el quehacer institucional en servidores de archivo NO se respalda (utilidad determinada por el Comite de Seguridad) |
| Bitacora obligatoria | Ningun proceso de respaldo sin bitacora predefinida y aprobada |
| Horarios | Respaldos en horarios no laborales preferentemente para no afectar rendimiento |
| Depuracion | Depurar y/o restaurar informacion segun necesidades de informacion operativa en linea y rendimiento del equipo |
| Solicitudes especiales | Formalizadas via correo o memo por jefatura del area solicitante; dependiendo de la naturaleza, autorizacion adicional del Encargado de Seguridad |
| Rotulacion | Rotular copias con tipo de respaldo (archivos, aplicacion), ciclo (diario, mensual, etc.) y fecha de generacion |
| Modificaciones de SO | Respaldo previo a modificaciones significativas en sistemas operativos |
| Frecuencia minima estandar | Respaldo incremental diario de servidores de BD, aplicaciones, sitio web. Snapshots para maquinas virtuales. Instantaneas diarias para archivos compartidos |
| Post-respaldo | Retirar cinta magnetica de la unidad de cintas |

## Proteccion y mantenimiento de los medios de respaldo

| Regla | Detalle |
|---|---|
| Servidor de Respaldo | Respaldo de archivos, BD e informacion de sistemas centrales en Servidor de Respaldo dedicado, exclusivo para garantizar continuidad operativa |
| Prohibicion de contenido no institucional | Prohibido almacenar archivos de juegos, musica, reproductores, programas sin licencia o informacion ajena a la institucion |
| Vencimiento de medios | Traspasar informacion a otro medio de caracteristicas similares o superiores; eliminacion del medio original tras traspaso exitoso |
| Obsolescencia tecnologica | Ante cambio tecnologico en medios de respaldo, generar acciones de resguardo |
| Seguridad del sitio | Sitio de copias de respaldo con control de acceso y seguridad ambiental (conforme a Procedimiento de Seguridad Fisica) |
| Boveda fisica | Registrar fecha/hora/rotulo/responsable al ingreso y retiro de medios; eliminar informacion cuando el espacio este al limite de ocupacion aceptable, llevando control de lo borrado |
| Inventario | Inventario permanente de medios magneticos, contenido y ubicacion. Inventario anual (preferiblemente en verano) |
| Ubicacion externa | Ubicaciones externas alejadas de instalaciones de origen para copias criticas, conforme a Politica de Seguridad Fisica |
| Transporte externo | Frecuencia y forma de envio definida; medio de transporte seguro con proteccion fisica |
| Vida util | Control de vida util de medios de almacenamiento para no usar medios susceptibles de dano |
| Informe anual de antiguedad de dispositivos | Describe antiguedad de dispositivos fisicos (CD, cintas, cartridges, discos) en almacenamiento interno y externo; enfasis en los proximos a expirar; analizado por Jefe TIC |
| Informe de antiguedad de informacion | Informacion almacenada que segun entes reguladores ya no es necesario conservar; analizado con areas involucradas |

### Respaldo de servicios en nube

- Garantizar copias de seguridad de informacion, aplicaciones y sistemas alojados en el proveedor
- Frecuencia segun esta politica, alineada con requisitos operativos, legales y de seguridad
- Evaluar efectividad del servicio de respaldo del proveedor verificando SLA
- Pruebas periodicas de restauracion para confirmar recuperacion confiable ante contingencias

### Recuperacion de la informacion

| Regla | Detalle |
|---|---|
| Ejecucion | Departamento TIC (administra servicios tecnologicos bajo su gestion) |
| Documentacion | Documentar procesos y procedimientos de recuperacion; consignar cambios al entorno que pudieran incidir en recuperacion (modificaciones de software o procedimientos de BD) |
| Duplicacion previa | Duplicar el respaldo antes de restaurar para no danar originales ante problemas durante la recuperacion |
| Pruebas periodicas | Trimestrales (idealmente) para respaldos no requeridos frecuentemente en sistemas de aplicacion; pruebas muestrales a informacion respaldada por usuarios en red; documentar las pruebas |
| Tercerizacion | Si la funcion esta tercerizada, los contratos deben prever que se realice conforme a los procedimientos definidos |

### Comprobacion de integridad de la informacion

- Departamento TIC comprueba integridad y confiabilidad del sistema de respaldo (y verifica que el proveedor lo haga si los servidores estan externalizados)
- Restauraciones periodicas en escenario adecuado para verificar integridad de la informacion respaldada
- Configurar software de respaldo para almacenar bitacoras de cada evento

### Restauracion de la informacion

- Revisiones periodicas del estado de los respaldos para asegurar disponibilidad y recuperabilidad de informacion critica

Elementos para pruebas de restauracion:

| Requisito | Detalle |
|---|---|
| Plan de restauracion | Actividades, fechas estimadas, responsables, relevancia de la informacion |
| Log de restauracion | Conservar para validar ejecucion satisfactoria; si falla, analizar causas y re-ejecutar |
| Tiempo | Depende del tipo de conexion y cantidad de datos |
| Encriptacion | Informacion respaldada encriptada al momento de la generacion del backup |
| Pruebas periodicas | Seleccion aleatoria de carpetas/archivos a restaurar; ubicacion de restauracion definida (recomendado carpeta creada para tal fin) |
| Pruebas aleatorias | Pruebas de integridad y restauracion en ambientes controlados |
| Solicitudes | Solo los duenos de activos pueden solicitar recuperacion ante perdida total/parcial o pruebas controladas |

## Frecuencia y tipo de respaldo

#### Equipos asignados a funcionarios

- Cada usuario es responsable de la gestion adecuada de la informacion en su equipo computacional
- Respaldo directamente en nube corporativa via Microsoft 365 (OneDrive)
- Independiente de medidas tecnicas adicionales para usuarios criticos (autoridades, otros determinados)
- Periodicidad segun criticidad, necesidades operativas y requisitos normativos

#### Sistemas y bases de datos

Estandar minimo por unidad, cumpliendo retenciones requeridas. La organizacion define retencion segun criterios formales.

**Politica ambiente produccion:**

| Tipo | Retencion |
|---|---|
| Respaldo incremental diario | 60 dias |
| Respaldo full semanal | 365 dias |
| Respaldo full mensual | 2.190 dias |
| Respaldo full anual | 2.190 dias |

**Politica ambiente de pruebas (QA):**

| Tipo | Retencion |
|---|---|
| Respaldo semanal incremental | 60 dias |
| Respaldo full mensual | 365 dias |

**Politica ambiente desarrollo:**

| Tipo | Retencion |
|---|---|
| Respaldo semanal incremental | 60 dias |
| Respaldo full mensual | 365 dias |

El area de Operaciones TIC define los tipos de respaldo como estandar institucional: frecuencia, medios de almacenamiento, tipo de contenido, tiempo de almacenamiento y borrado.

Solicitudes especiales de respaldo protegido: autorizadas por Jefe del Departamento TIC y Encargado de Seguridad de la Informacion y Ciberseguridad.

### Proteccion de la informacion en medios de respaldo

Estrategia de seguridad de respaldo **3-2-1** para toda informacion critica:

| Principio | Detalle |
|---|---|
| 3 copias | Una original + dos copias adicionales de seguridad |
| 2 medios distintos | Al menos dos tipos de almacenamiento (ej. red + nube) |
| 1 copia externa | Una copia en ubicacion fisica o logica distinta de la institucion (centro de datos remoto o nube) |

Ajustable segun necesidades especificas (periodicidad, retencion, criticidad, requisitos legales/regulatorios).

- Informacion critica en respaldos externos trasladada con elementos de seguridad adecuados (encriptacion o prevencion de acceso fisico no autorizado)
- Operaciones TIC mantiene inventario actualizado de informacion almacenada externamente (proporcionado por el proveedor de resguardo)

### Proteccion de la informacion en medios magneticos (cintas)

Cuando el almacenamiento se realice mediante cintas con servicio especializado:

| Requisito | Detalle |
|---|---|
| Proteccion fisica y ambiental | Garantizar confidencialidad, integridad y disponibilidad de informacion, software y sistemas |
| Alcance | Todos los medios magneticos (historicos y vigentes) en dependencias del proveedor |
| Control de acceso | Solo personas autorizadas; registro de identidad, fecha, hora y bitacora de actividades |
| Seguridad ambiental | Controles de humedad, temperatura, detectores de incendio y condiciones que eviten deterioro |
| Controles periodicos | Procedimientos que aseguren integridad y disponibilidad del respaldo para recuperacion |
| Catalogo de software de respaldo | Actualizado, entregado periodicamente al Departamento TIC; registro de altas y bajas de cintas |
| Cinta principal + clone | Para todos los respaldos; cinta clone para traslado off-site |
| Intervenciones foraneas | Asegurar que no existan durante traslados por el proveedor |
| Consistencia de recuperacion | Recuperacion a estado consistente y conocido en caso de falla; consistencia de inventarios onsite |
| Verificacion de soportes | Comprobar que los respaldos son capaces de recuperar la informacion respaldada |
| Cifrado | Mecanismos de cifrado sobre medios portables |

### Vigencia, revision y retencion de respaldos

- Gestionados conforme a tiempos de retencion segun criticidad, requisitos operativos y normativas legales/regulatorias
- Al cumplir el periodo de retencion, eliminacion segura garantizando confidencialidad de los datos

### Respaldo de estaciones de trabajo

- Responsabilidad del usuario sobre la informacion en su computador asignado (incluye computadores portatiles)
- Necesidades de respaldo adicional: solicitud formal por Jefe del Departamento o Unidad al Jefe del Departamento TIC, justificando criticidad
- Jefe TIC evalua y resuelve la solicitud

### Borrado de la informacion

| Regla |
|---|
| Informacion en servidores centrales que no sea necesaria debe ser borrada |
| Informacion respaldada en medios magneticos que pierda vigencia debe ser borrada del medio |
| Servicio de respaldo externo debe certificar eliminacion y borrado correcto de medios |
| Equipo computacional o medio de almacenamiento dado de baja: examinado por Operaciones TIC para comprobar borrado de informacion |
| Destruccion de medios (cintas, CD/DVD) de forma que impida acceso, conforme al Procedimiento para la eliminacion segura y reutilizacion de equipos |

## Difusion

| Canal | Destino |
|---|---|
| Intranet MINSAL | `http://isalud.minsal.cl` |
| Correo informativo | Funcionarios |
| Sitio web MINSAL | `http://www.minsal.cl/seguridad_de_la_informacion/` |

## Periodo de revision

Cada **2 anos** o ante cambios significativos, verificando: adecuacion al proposito, reflejo de cambios tecnologicos, alineacion con legislacion vigente, estandares internacionales y mejores practicas.

## Excepciones

El Jefe de Depto. TIC, el CISO o el Comite de Seguridad evaluan y establecen condiciones especificas de excepcion, siempre que no infrinjan legislacion ni comprometan seguridad. Cada excepcion se documenta e inicia revision de la politica.

## Control de versiones

| Version | Fecha | Secciones | Motivo |
|---|---|---|---|
| 01 | Septiembre -- | Todas | Creacion del documento |
| 02 | Octubre -- | Todas | Aprobacion por resolucion |
| 03 | Octubre 2019 | Todas | Cambios en referencia normativa, formato, responsabilidades |
| 04 | Octubre 2021 | Todas | Vigencia y retencion de respaldos; incluye Recuperacion, Restauracion, Comprobacion de Integridad, Frecuencia y Tipo de respaldos, Proteccion en medios magneticos |
| 05 | Noviembre 2024 | Pag. 4, 6, 7, 9, 10 y roles | Actualizacion a ISO 27002:2022; leyes y decretos; roles y responsabilidades; consideraciones generales; proteccion de medios de respaldo; respaldo en nube; restauracion; frecuencia; proteccion de la informacion; vigencia de respaldos; periodo de revision; excepciones |
