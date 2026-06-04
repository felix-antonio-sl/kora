---
_manifest:
  urn: urn:salud:kb:procedimiento-monitoreo-uso-medios-procesamiento
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-04'
    source: MINSAL Chile, SGSI Nivel Central. PROS-NC-005 v4
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- procedimiento
- monitoreo
- uso-aceptable
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:procedimiento-monitoreo-uso-medios-procesamiento
  salud:
    minsal_id: PROS-NC-005
    minsal_version: '4'
    fecha_aprobacion: Octubre 2019
    clasificacion: TLP:BLANCO
relations:
  cites:
  - urn:salud:kb:procedimiento-gestion-incidentes-seguridad
  - urn:salud:kb:procedimiento-desarrollo-seguro
---

## Proposito y alcance

Define las actividades de monitoreo del uso de las instalaciones de procesamiento de informacion de Minsal en el Nivel Central.

Aplica a todos los funcionarios (planta, contrata, reemplazos, suplencia), personal a honorarios y terceros (proveedores, compra de servicios) con derechos de acceso a activos de informacion del Ministerio de Salud.

Controles NCh-ISO 27001.Of2013 cubiertos:

| Control | Descripcion |
| --- | --- |
| A.12.04.01 | Registro de evento |
| A.12.04.03 | Registros del administrador y del operador |
| A.12.04.04 | Sincronizacion de relojes |
| A.12.06.01 | Gestion de las vulnerabilidades tecnicas |
| A.18.02.03 | Verificacion del cumplimiento tecnico |

## Responsable

**Operaciones TIC**: monitoreo de capacidad de servidores, servicios, aplicaciones en produccion y equipos de comunicacion.

## Monitoreo de servidores

Frecuencia: al menos **semanal**. Registros electronicos conservados minimo **2 años**.

Variables minimas a monitorear:

- Porcentaje de uso de CPU
- Espacio disponible en disco duro
- Memoria RAM

| Condicion | Accion |
| --- | --- |
| Cualquier variable > 80% capacidad | Evaluar aumento de capacidad o reduccion de demanda usando historico del servidor |

Medidas de reduccion de demanda:

1. Eliminacion de datos obsoletos (espacio en disco)
2. Retiro de servicio de aplicaciones, sistemas, bases de datos o entornos
3. Eliminacion de procesos y programaciones de parches
4. Optimizacion de consultas de logicas de aplicaciones o bases de datos
5. Alternativas de almacenamiento externo (Hosting, VPS)

## Monitoreo de servicios y aplicaciones

Frecuencia: al menos **semanal**. Registros electronicos conservados minimo **2 años**.

Servicios minimos a monitorear:

- DNS
- Videoconferencia
- Internet
- Telefonia
- Wireless
- Firewall
- Aplicativos criticos

## Monitoreo de vulnerabilidades y cumplimiento tecnico

Frecuencia: **aleatoria**. Registros electronicos conservados minimo **2 años**.

Pruebas de seguridad sobre infraestructura y aplicativos, con herramientas especializadas o manuales.

Entregable: informe detallado con resultados, analisis de implicaciones de seguridad y recomendaciones de solucion.

## Gestion de eventos e incidentes de seguridad

Eventos que ponen en riesgo la seguridad deben reportarse segun el Procedimiento de gestion de incidentes de seguridad de la informacion.

### Eventos que requieren investigacion adicional

| Categoria | Eventos |
| --- | --- |
| Perdida | Servicio, equipos o instalaciones |
| Mal funcionamiento | Sobrecargas del sistema, software o hardware |
| Errores humanos | No cumplimiento de politicas o pautas |
| Cambios no controlados | Modificaciones de sistema sin autorizacion |
| Acceso | Violaciones, exposicion de informacion sensible |

### Elementos investigables por categoria

**Acceso no autorizado**: ID de usuario, fecha/hora de eventos clave, tipos de eventos, archivos accedidos, programa/utilidad usado.

**Operaciones privilegiadas**: uso de cuentas privilegiadas (supervisor, root, administrador), arranque/apagado de sistema, conexion/desconexion de dispositivos I/O.

**Intentos de acceso no autorizado**: acciones de usuario fallidas o rechazadas, acciones fallidas sobre datos/recursos, violaciones de politica de acceso en gateway y firewall, alertas de sistemas de deteccion de intrusion.

**Alertas o fallas del sistema**: alarmas/mensajes de consola, excepciones de registro del sistema, alarmas de red, alarmas de control de acceso.

**Otros indicadores**: cambios o intentos de cambio en configuraciones/controles de seguridad, descargas masivas de informacion, barrido de puertos, accesos fuera de horario habitual, accesos con derechos de administrador, frecuencias anormales de uso, envio de informacion a servidores externos, trafico cifrado, descargas desde servidores externos.

## Registros de administrador y operador

Usuarios con privilegios pueden manipular registros bajo su control directo. Estas cuentas deben revisarse al menos cada **12 meses** mediante:

- Auditorias internas
- Auditorias externas
- Revision del Encargado de Seguridad de la Informacion / Ciberseguridad
- Revision del Area de Operaciones TIC (Seguridad TIC)

## Sincronizacion de relojes

Responsable: Operaciones TIC.

Herramientas:

| Herramienta | Aplica a |
| --- | --- |
| Parche de hora de Microsoft | Sistemas Windows |
| Active Directory | Sistemas en dominio |
| Manual | Equipos con otro sistema operativo |

Hora de referencia: Servicio Hidrografico y Oceanografico de la Armada (SHOA).

## Registros

- Registros de monitoreo de servidores
- Registros de monitoreo del estado de servicios y aplicaciones
- Registros de monitoreo de vulnerabilidades

## Difusion

Canales minimos:

- Publicacion en intranet Minsal (http://isalud.minsal.cl/)
- Correo informativo

## Revision y control de versiones

Revision: al menos cada **2 años** o ante cambios significativos.

| Version | Fecha | Motivo | Secciones |
| --- | --- | --- | --- |
| 01 | Diciembre 2013 | Creacion | Todas |
| 02 | Octubre 2014 | Actualizacion de roles y responsabilidades | 6.1, 6.2 |
| 03 | Noviembre 2016 | Actualizacion normativa; inclusion de registros de administrador y sincronizacion de relojes | 6.1, 6.2, 6.3 |
| 04 | Octubre 2019 | Actualizacion integral | Todas |
