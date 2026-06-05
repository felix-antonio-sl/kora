---
_manifest:
  urn: urn:salud:kb:resolucion-aprueba-politicas-seguridad-263
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-05'
    source: MINSAL Chile. Resolución Exenta N°263 (MAR-2022). Aprueba Política de
      Respaldo de Información y Software del Ministerio de Salud.
  extensions:
    kora:
      family: note
    salud:
      minsal_id: RES_263
      fecha: 2022-03
      signatario: Ministro de Salud
      documento_aprobado: PS-NC-004
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- resolucion
- acto-administrativo
lang: es
relations:
  cites:
  - urn:salud:kb:politica-general-seguridad-informacion-ciberseguridad
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:resolucion-aprueba-politicas-seguridad-263
---

# Resolución Exenta N°263 — Aprueba Política de Respaldo de Información y Software

**Santiago, MAR 2022. Aprueba la política PS-NC-004, Versión Oficial v04, Octubre 2021.**

## Vistos

| Norma | Detalle |
| --- | --- |
| Ley N°21.289 | Presupuestos del Sector Público año 2021 |
| DFL N°1/2005, MINSAL | Texto refundido DL N°2.763/1979 y Leyes N°18.933 y N°18.469 |
| DFL N°1/19653/2000, SEGPRES | Texto refundido Ley N°18.575, Orgánica Constitucional de Bases Generales de la Administración del Estado |
| Resolución Exenta N°889/2019, MINSAL | Aprueba Política General de Seguridad de la Información |
| Memorándum A22 N°110 (12-abr-2021) y N°126 (27-abr-2021) | Jefe Depto. TIC |
| Recado interno (06-may-2021) | Encargado de Seguridad MINSAL |
| Resolución N°07/2019, CGR | Exención del trámite de toma de razón |

## Considerando

1. Las TIC son insumos esenciales en los procesos institucionales del sector salud. La Ley 19.880 prevé procedimientos administrativos en expedientes físicos o electrónicos.
2. Art. 6 de la Ley 19.799 sobre documentos electrónicos, firma electrónica y servicios de certificación.
3. Decreto N°83/2005, SEGPRES: norma técnica sobre seguridad de la información de documentos electrónicos en la Administración del Estado.
4. Art. 5 letra p) del Decreto N°83: define Política de Seguridad como "conjunto de normas o buenas prácticas para disminuir el nivel de riesgo". Art. 11: la Política debe fijar directrices generales de seguridad institucional.
5. El MINSAL aprobó la "Política General de Seguridad de la Información" por Resolución Exenta N°889/2019. Se requiere aprobar instrumentos complementarios.
6. Al MINSAL compete ejercer la rectoría del sector salud, comprendiendo dirección y orientación de todas las actividades relativas a la provisión de acciones de salud.

## Resuelvo

### 1. Apruébase

La **Política de Respaldo de Información y Software** para el Ministerio de Salud, PS-NC-004, Versión Oficial v04, Octubre 2021, cuyo texto íntegro se transcribe a continuación.

---

## Política de Respaldo de Información y Software — PS-NC-004

**Versión 1.3, Agosto 2021. Sistema de Gestión de Seguridad de la Información — Nivel Central.**

**Versión Oficial Actual v04 — Octubre 2021.**

| Rol | Persona | Fecha |
| --- | --- | --- |
| Elaborado | Rodrigo Vidal, Unidad de Seguridad | Octubre 2021 |
| Revisado | Eduardo Albornoz / Andrés Muñoz, Unidad Operaciones | Noviembre 2021 |
| Revisado | José Villa, Encargado Ciberseguridad | Noviembre 2021 |
| Aprobado | Gino Paolo Peirano Alvarado, Jefe Depto. TIC | Noviembre 2021 |

## 1. Propósito

Definir reglas que aseguren adecuada generación, resguardo, mantenimiento y recuperación de la información almacenada en unidades de respaldo, para proveer continuidad a la operación en caso de contingencias o interrupciones del servicio de procesamiento.

## 2. Alcance o Ámbito de Aplicación

Aplica a toda la información electrónica contenida en servidores, estaciones de trabajo y equipos comunicacionales con datos, configuraciones, aplicativos y servicios críticos para el MINSAL.

Aplicable a todos los funcionarios (planta, contrata, reemplazos y suplencia), personal a honorarios y terceros (proveedores, compra de servicios) que presten servicios para la Subsecretaría de Salud Pública y Subsecretaría de Redes Asistenciales.

**Alcance de Dominios y Controles (NCh-ISO 27001:2013):**

| Dominio | ID Control | Nombre del Control |
| --- | --- | --- |
| Seguridad de las operaciones | A.12.03.01 | Respaldo de la información |

## 3. Marco Normativo y Documentos Relacionados

**Marco Normativo:**

- NCh-ISO 27001:2013: Sistemas de gestión de la seguridad de la información — Requisitos
- Ley 19.799 sobre firma y documentos electrónicos y su normativa complementaria
- Marco Jurídico de SSI, publicado en portal CSIRT del Ministerio del Interior
- Decretos Supremos y Normas Internacionales de Seguridad y Ciberseguridad: `https://www.csirt.gob.cl/decretos/`
- Leyes relacionadas: `https://www.csirt.gob.cl/leyes/`
- Circular 28.704 (ago-1981), CGR: Disposiciones sobre eliminación de documentos
- Decreto N°83/2004, SEGPRES: norma técnica sobre seguridad y confidencialidad de documentos electrónicos

**Documentos Relacionados:**

- Documentos del SGSI disponibles en `isalud.minsal.cl`
- Procedimiento para la eliminación segura y reutilización de equipos

## 4. Roles y Responsabilidades

**Departamento TIC:**

- Definir el estándar de respaldo de servidores centrales y equipos de hardware (software básico, aplicaciones, configuraciones de servicios y datos en ambientes de Producción, QA y Desarrollo)
- Autorizar solicitudes de respaldo especiales

**Departamento TIC — Operaciones TIC:**

- Generar planes de respaldos y restauración
- Coordinar, ejecutar y probar en intervalos definidos en la frecuencia y tipos de respaldo
- Llevar registros de respaldos y pruebas

**Encargado de Seguridad / Encargado de Ciberseguridad:**

- Definir con el negocio el tipo y periodicidad de respaldos para cada aplicación o plataforma
- Autorizar solicitudes especiales de respaldo protegido

**Usuarios:**

- Cumplir con lo establecido en esta política

## 5. Materias que Aborda

- Respaldo de la información
- Restauración de la información

## 6. Directrices de la Política

Cumplimiento de la legislación: las medidas de control de acceso deben cumplir y ser consistentes con la Normativa del SGSI.

## 6.1 Respaldo de información en servidores centrales

El Depto. TIC es responsable del respaldo de información en servidores centrales. Las demás áreas son responsables del respaldo de sus datos cuando no residan en servidor centralizado.

Si los servidores centrales están externalizados con proveedor, el Depto. TIC verifica que los respaldos se realicen. El proveedor debe enviar diariamente los "job's" de respaldo generados y sus resultados, según procedimiento definido con la contraparte institucional.

## 6.2 Clasificación de la información

MINSAL mantiene información de distintos tipos de criticidad (Alta, Media, Baja). El mecanismo, periodicidad y tecnología de respaldo depende de la criticidad asignada.

## 6.3 Información que no se respalda

- Claves de usuario: **NO** serán respaldadas.
- Información no relevante para el quehacer institucional en servidores de archivo: **NO** será respaldada. La utilidad de la información la determina el Comité de Seguridad de la Información del Nivel Central.

## 6.4 Procedimiento y gestión de dispositivos de respaldos

**Reglas generales:**

- Toda solicitud de respaldo adicional debe ser formalizada por correo o memo de la Jefatura del área solicitante; según naturaleza, también autorizada por el Encargado de Seguridad.
- No ejecutar procesos de resguardo no materializados en bitácora predefinida y aprobada.
- Efectuar copias en horarios que no afecten el rendimiento de servidores, preferentemente fuera de horario laboral.
- Realizar depuración/restauración según necesidades de información operativa en línea.
- Efectuar respaldo de servidores previo a modificaciones significativas en Sistemas Operativos.
- Respaldo incremental diario de Servidores de Bases de Datos, Aplicaciones y Sitio Web.
- Para máquinas virtuales: Snapshots.
- Para recursos de archivos compartidos: instantáneas diarias, minimizando uso de cintas magnéticas y garantizando pronta restauración.

**a) Registro de los respaldos:**

- Cada respaldo (manual o automático) debe quedar registrado en LOGS de servidores, informes de reporte diario de la plataforma de respaldo o archivos electrónicos.
- Si existe servicio externo para resguardo de cintas magnéticas: llevar registro de retiro de cintas.
- Rotular copias de respaldo con: tipo de respaldo (archivos de datos, aplicación), ciclo (diario, mensual) y fecha de generación.
- Retirar cinta magnética de la unidad de cintas después del respaldo.

**b) Protección y mantención de los medios de respaldo:**

- Almacenar nivel mínimo de información crítica de respaldo en ubicación remota, a distancia que escape de daños por desastre en sitio principal. El nivel mínimo lo define el Comité de Seguridad de la Información del Nivel Central.
- Mantener registros exactos y completos de copias y procedimientos documentados de restablecimiento.
- Para ámbitos críticos: almacenar al menos tres generaciones o ciclos de información de respaldo.
- La información crítica almacenada fuera de la Institución debe trasladarse con seguridad adecuada (encriptación o métodos para prevenir acceso físico no autorizado).
- Operaciones TIC mantiene inventario actualizado de información almacenada externamente (proporcionado por el proveedor de resguardo).
- Todos los archivos, bases de datos e información de sistemas centrales deben respaldarse en un Servidor de Respaldo.
- Uso del Servidor de Respaldo: exclusivo para funciones institucionales.
- Prohibido almacenar en el Servidor de Respaldo: archivos de juegos, música, reproductores, videos, programas sin licencia, o información ajena a la Institución.
- Si el medio magnético u óptico está próximo a vencimiento: traspasar información a otro medio de características similares o superiores; luego, eliminación segura del medio original.
- Ante cambio tecnológico que genere obsolescencia de medios de respaldo: generar acciones necesarias de resguardo.
- El sitio de copias de respaldo debe cumplir con reglas de control de acceso y seguridad ambiental definidas en el procedimiento de Seguridad Física.
- Los medios de respaldo removibles deben retirarse del recinto de respaldo y llevarse a otro que garantice catálogo, fiabilidad, seguridad y disponibilidad.
- Si no hay bóveda de almacenamiento electrónico y sí físico:
 - Registrar en planilla: fecha, hora, rótulo del medio, responsable de transporte a custodia, y registro de retiro cuando alguien autorizado solicite unidades para prueba o recuperación.
 - Eliminar información (verificando que no requiere restauración) cuando el espacio esté al límite aceptable, llevando control de lo borrado y procurando al menos una copia recuperable mientras no se cumpla el acápite de eliminación.
 - Mantener inventario permanente de medios magnéticos: contenido y ubicación.
 - Realizar inventario anual de medios magnéticos, preferentemente en verano.
 - Fijar ubicaciones externas alejadas para copias de respaldo de información crítica, cumpliendo la Política de Seguridad Física.
 - Establecer frecuencia y forma de envío a ubicación externa por medio de transporte seguro con protección física.
 - Llevar control de vida útil de medios de almacenamiento.
 - Emitir anualmente informe de antigüedad de dispositivos físicos (CD, cintas, cartridges, discos) en almacenamiento interno y externo, con énfasis en los próximos a expirar según especificaciones del fabricante. Visado por el Jefe del Depto. TIC.
 - Emitir anualmente informe de antigüedad de información almacenada, especialmente la que según entes reguladores ya no requiere conservación. Aprobado con áreas involucradas.
 - Realizar pruebas periódicas en respaldos no requeridos frecuentemente (trimestral para datos de sistemas de aplicación) para asegurar disponibilidad. Pruebas muestrales a información respaldada por usuarios en la red. Documentar las pruebas.
 - Realizar pruebas aleatorias de integridad de respaldos y pruebas de restauración sobre ambientes controlados para validar efectividad.

**c) Protección de la información en medios magnéticos (cintas):**

- Garantizar custodia y almacenamiento de medios magnéticos a través de servicio especializado; el proveedor es responsable del resguardo del respaldo.
- Las cintas de respaldo deben tener protección física y ambiental adecuada para mantener confidencialidad, integridad y disponibilidad.
- Velar por custodia física de todos los medios magnéticos (históricos y vigentes) almacenados en dependencias del proveedor.
- Acceso al lugar de almacenamiento restringido a personas autorizadas.
- El respaldo de datos y software críticos debe almacenarse en lugar protegido con acceso controlado.
- Mantener catálogo actualizado del software de respaldo, entregado periódicamente en copia al Depto. TIC, incluyendo registro de altas y bajas de cintas.
- Disponer de cinta principal y cinta clone para todos los respaldos; cinta clone para traslado off-site.
- Asegurar que no existan intervenciones foráneas en los respaldos durante traslados por el proveedor.
- Asegurar recuperación de información a estado consistente y conocido en caso de falla del sistema; mantener consistencia de inventarios de medios magnéticos onsite.
- Verificar estado de soportes físicos que contienen copias de seguridad, comprobando que los respaldos puedan recuperar la información.
- Disponer mecanismos de cifrado sobre medios portables.
- El referente técnico del contrato es responsable de velar por el cumplimiento de los puntos anteriores.

## 6.5 Frecuencia y Tipo de Respaldo

**Equipos de funcionarios críticos:** al menos 1 respaldo anual.

**Sistemas y bases de datos:** cumplir estándar mínimo de retenciones. La Organización define la retención según criterios formalmente establecidos.

**Política ambiente de producción:**

| Tipo | Retención |
| --- | --- |
| Respaldos incrementales diarios | 60 días |
| Respaldos full semanal | 365 días |
| Respaldo full mensual | 2.190 días |
| Respaldo full anual | 2.190 días |

**Política ambiente de pruebas (QA):**

| Tipo | Retención |
| --- | --- |
| 1 respaldo semanal incremental | 60 días |
| Respaldo full mensual | 365 días |

**Política ambiente Desarrollo:**

| Tipo | Retención |
| --- | --- |
| 1 respaldo semanal incremental | 60 días |
| Respaldo full mensual | 365 días |

**Respaldo de estaciones de trabajo:** responsabilidad del usuario; también aplica para computadores portátiles.

El área de Operaciones TIC define los tipos de respaldo estándar: frecuencia, medios de almacenamiento, tipo de contenido, tiempo de almacenamiento y borrado.

**Solicitudes especiales de respaldo protegido:**

- Autorizadas por el Jefe del Depto. TIC y los Encargados de Seguridad/Ciberseguridad.
- Cualquier necesidad de respaldo debe ser solicitada formalmente por el Jefe del Depto. o Unidad respectiva, justificando la criticidad, dirigida al Jefe del Depto. TIC.

## 6.6 Vigencia y Retención de los Respaldos

La obligación de realizar respaldos se rige por el Decreto 83/2004 de Minsegpres sobre seguridad de la información. La conservación de información relativa a procesos y documentos se rige por la ley y normas reglamentarias de cada caso concreto.

## 6.7 Borrado de la Información

- La información no necesaria en servidores centrales debe ser borrada.
- La información respaldada en medios magnéticos que pierda vigencia debe ser borrada. El servicio de respaldo externo debe certificar la correcta eliminación.
- Todo equipo computacional o medio de almacenamiento dado de baja debe ser examinado por Operaciones TIC para comprobar que la información ha sido borrada.
- La destrucción de medios de almacenamiento (cintas, CD/DVD) con información debe impedir el acceso al medio, según el Procedimiento para la eliminación segura y reutilización de equipos.
- La calificación de la información como innecesaria es responsabilidad de la unidad dueña de la información.

## 6.8 Recuperación de la Información

- Ejecutada por el Depto. TIC.
- Documentar el proceso y procedimientos de recuperación, incluyendo cambios al entorno que pudiesen incidir en la recuperación (modificaciones al software, procedimientos de administración de bases de datos o sistemas).
- Duplicar el respaldo antes de restaurar, para no dañar los originales si surge algún problema.
- Si la función de respaldo y recuperación está tercerizada, las Unidades de Informática deben prever en los contratos que dichas funciones se realicen conforme a los Procedimientos definidos.

**Comprobación de integridad de la información:**

- El Depto. TIC comprueba integridad y confiabilidad del sistema de respaldos. Si los servidores están externalizados, verifica que esto ocurra.
- Realizar periódicamente restauraciones de información en escenario adecuado para verificar integridad.
- Configurar el software de respaldo para almacenar bitácoras de cada evento.

**Restauración de la información:**

- Los dueños de los activos son los únicos autorizados para solicitar recuperación de información. En ausencia o cese del dueño, la responsabilidad recae en quien lo subrogue o reemplace.
- Depto. TIC elabora anualmente plan de pruebas de restauración (actividades, fechas, responsables, relevancia de la información).
- Conservar log de restauración para validar ejecución satisfactoria. Si falla, analizar causas y reejecutar.
- El tiempo de restauración depende del tipo de conexión y tamaño de la información.
- La información respaldada debe quedar encriptada al momento de la generación del backup.
- La clave de desencriptación se mantiene en archivos a cargo del dueño de la información. TIC Minsal mantiene copia de respaldo de la clave, utilizable solo en ausencia del dueño.
- Las pruebas de restauración deben ser periódicas según el plan. Carpetas/archivos a restaurar se seleccionan aleatoriamente. La restauración puede ser en ubicación original (información eliminada por usuario) o en carpeta creada para tal fin (recomendado para no sobrescribir archivos modificados por usuario).

## 7. Mecanismo de Difusión

La comunicación se efectuará de forma accesible y comprensible mediante:

- Publicación en intranet Minsal: `http://isalud.minsal.cl/`
- Correo informativo

## 8. Período de Revisión

Revisión al menos cada dos años por el Comité de Seguridad de la Información, o cuando se requiera por necesidades de cambio para garantizar idoneidad, adecuación y efectividad.

## 9. Excepciones al Cumplimiento de la Política

El Comité de Seguridad de la Información podrá establecer condiciones puntuales de excepción siempre que no infrinja la legislación vigente. Toda excepción debe ser documentada y generar un proceso de revisión de la política.

## 10. Historial y Control de Versiones

| Versión | Fecha | Sección | Cambio |
| --- | --- | --- | --- |
| 01 | Septiembre 2014 | Todas | Creación del documento |
| 02 | Octubre 2019 | Ninguna | Aprobación por resolución; cambios en referencia normativa; formato de documento; responsabilidades |
| 03 | Octubre 2021 | Todas | Modifica: consideraciones generales, vigencia y retención de respaldos, recuperación de respaldos, restauración de la información, comprobación de integridad, frecuencia, protección de información en medios |

---

### 2. Publíquese

El contenido del archivo computacional correspondiente junto con la presente resolución, por el Depto. TIC, en `https://www.minsal.cl/seguridad_de_la_informacion/` y en el Banner de transparencia del MINSAL.

### 3. Remítase

Un ejemplar del instructivo a los funcionarios que corresponda, vía correo electrónico.

### 4. Anótese y comuníquese

## Distribución

- Gabinete Ministro de Salud
- Gabinete Subsecretaría de Salud Pública
- Gabinete Subsecretaría de Redes Asistenciales
- Depto. de Tecnologías de la Información y Comunicaciones
- Depto. de Salud Digital
- Archivo División Jurídica
- Archivo
