---
_manifest:
  urn: urn:salud:kb:procedimiento-gestion-crisis-incidentes
  provenance:
    source: MINSAL Chile, SGSI Nivel Central. PROS-NC-012 v01
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- procedimiento
- crisis
- incidentes-criticos
- bcp
- drp
lang: es
extensions:
  kora:
    family: note
    minsal_id: PROS-NC-012
    minsal_version: '01'
    shard_index: 1
    shard_count: 2
    shard_root_urn: urn:salud:kb:procedimiento-gestion-crisis-incidentes
relations:
  cites:
  - urn:salud:kb:instructivo-seguridad-informacion-ciberseguridad-sector-salud
---

# Procedimiento Gestión de Crisis por Incidentes de Seguridad


## Propósito y alcance

Tratamiento de incidencias mayores que requieran Comité de Crisis para su gestión en las Subsecretarías de Salud Pública y de Redes Asistenciales.

**Afectación a activos de información**: bases de datos, documentos, equipos, expedientes, formularios, infraestructura física, personas, sistemas de información, software.

**Dimensiones cubiertas**:

| Dimensión | Afectación |
|-----------|------------|
| Confidencialidad | Acceso no autorizado a la información |
| Integridad | Modificación no autorizada, destrucción o pérdida de información |
| Disponibilidad | Inaccesibilidad a la información |

**Sujetos obligados**: funcionarios (planta, contrata, reemplazos y suplencia), personal a honorarios y terceros (proveedores, compra de servicios) con derechos de acceso a información que puedan afectar los activos de información del MINSAL.

**Controles ISO 27001:2013 cubiertos**: A.06.01.03 (Contacto con autoridades), A.06.01.04 (Contacto con grupos especiales de interés), A.16.01.01 (Responsabilidades y procedimientos), A.16.01.02 (Informe de eventos), A.16.01.03 (Informe de debilidades), A.16.01.04 (Evaluación y decisión sobre eventos), A.16.01.05 (Respuesta ante incidentes), A.16.01.06 (Aprendizaje de incidentes), A.16.01.07 (Recolección de evidencia).

## Terminología

- **MINSAL**: Ministerio de Salud.
- **SGSI**: Sistema de Gestión de Seguridad de Información.
- **CSIRT**: Equipo de Respuesta ante Emergencias Informáticas.

## Documentos aplicables

- Documentos del SGSI de MINSAL.
- Política Nacional de Ciberseguridad (PNCS).
- Marco Jurídico SSI, publicado en portal CSIRT del Ministerio del Interior: decretos supremos y normas internacionales ([csirt.gob.cl/decretos](https://www.csirt.gob.cl/decretos)), leyes relacionadas ([csirt.gob.cl/leyes](https://www.csirt.gob.cl/leyes)).

## Roles y responsabilidades

**Miembros del Comité de Crisis y subrogantes**: responsabilidades detalladas en §6.1.

**Funcionarios**: informar cualquier evento o debilidad que pueda afectar la seguridad de la información.

## Flujo general de gestión de incidentes críticos

Respuesta a incidentes a través de instancias técnicas coordinadas con el Equipo de Respuesta a Incidentes y el Comité de Crisis, según impacto sobre activos vitales de la organización.

La gestión de incidentes de seguridad recae en el Encargado de Seguridad de la Información y Ciberseguridad y/o quien asigne el Jefe del Departamento TIC, con apoyo del equipo de respuesta a incidentes y del Comité de Crisis, resguardando los principios de la Política General y leyes vigentes.

El Encargado de Seguridad mantiene contactos con autoridades, grupos de interés externos y foros que manejen incidentes de seguridad de la información.

**Incidentes judicializados**: convocar a expertos policiales para acceso a la información necesaria para la investigación, con cuidados especiales.

## Comité de Crisis

### Composición y responsabilidades

Responsable de la gestión de incidentes. Debe estar previamente definido. Presidido por la figura máxima con capacidad de decisión (responsable máximo del organismo y/o representante del Gabinete de Ministro o Subsecretarías).

**Áreas con representación y subrogante obligatorias**: Encargado de Ciberseguridad, Infraestructura Física, TIC (Operaciones, Infraestructura, Desarrollo, Explotación), Dueños de los Procesos, Recursos Humanos, Finanzas, Jurídica y Comunicaciones.

La gestión de crisis no es exclusiva del equipo de seguridad o tecnología: implica a toda la organización.

**Facultades del presidente**: declarar crisis, definir nivel de criticidad, establecer medidas, asignar responsabilidades desde lo operativo (contención y resolución) hasta la política de comunicación (imagen institucional, comunicados, canales).

#### Tabla de actores y responsabilidades

| Actor | Responsabilidades |
|-------|-------------------|
| CEO / Director General (Presidente) | Inicia la gestión de crisis y preside el comité. Delega responsabilidades. Se mantiene permanentemente informado. Actúa como portavoz si las circunstancias lo exigen. |
| Encargado de Ciberseguridad / Seguridad de la Información (TIC) | Primero en conocer el incidente. Determina nivel de criticidad (Impacto y Urgencia). Traslada al Comité de Crisis si procede. Notifica al CSIRT de referencia. Determina primeras acciones operativas de contención. Gestiona continuidad de servicios (respaldos, sitios de contingencia). Revisa entorno común (comunicaciones, firewall, DNS, etc.) y específicos por aplicación. Gestiona servidores virtuales rápidos si es necesario. Activa política de copias de seguridad. Activa infraestructura de contingencia. |
| PMO / Encargado del Proyecto | Coordina con proveedores todas las acciones de contención, erradicación y cierre. |
| Jurídica | Determina responsabilidades legales directas provocadas por el incidente. Da seguimiento a acciones según leyes y normas aplicables. Orienta sobre todos los asuntos legales. |
| Comunicaciones | Integra el Comité de Crisis. Adopta el Manual de Comunicaciones de Crisis previamente elaborado. Decide mensajes clave, formato y canal más adecuado según grupos de interés. Activa seguimiento y percusión de la crisis en medios de comunicación y redes sociales. Mantiene contacto con los medios. |
| Administración y Finanzas | Analiza recursos necesarios para la resolución de la crisis. Recopila información, evalúa hechos y plantea opciones. Mantiene comunicación con compañías aseguradoras (si aplica). |
| Infraestructura Física | (integrada con Administración y Finanzas) |
| Recursos Humanos | Portavoz ante los funcionarios y representantes. Gestiona acciones operativas en caso de incidentes relacionados con personas. Comunica con afectados y facilita información o asistencia básica (ej. lesión de un funcionario). Evalúa ánimo de los funcionarios y recomienda acciones para evitar decaimiento. |

### Declaración de crisis y niveles de criticidad

#### Niveles

| Nivel | Criticidad | Declaración de Crisis | Comité requerido | Ámbito de decisión | Preside |
|-------|------------|-----------------------|-----------------|-------------------|---------|
| Bajo | Baja | No | No requiere | Operativo | Encargado del área TI y responsable de activos afectados |
| Medio | Media | No | No requiere (opcional) | Operativo | Encargado de Ciberseguridad y/o quien asigne Jefe DTI |
| Alto | Alta | Sí | Requiere Comité de Crisis (Nivel 2-3, sin CEO) | Táctico | Encargado de Ciberseguridad y/o quien asigne Jefe DTI |
| Muy Alto | Muy Alta | Sí | Requiere Comité de Crisis + Gobierno de Crisis | Estratégico | Representante de Dirección / CEO |

**Regla**: incidentes con peligrosidad baja y media no requieren convocatoria de Comité de Crisis. Los equipos técnicos tienen el conocimiento para solución a nivel operativo, bajo responsabilidad directa del Encargado de Ciberseguridad y/o quien asigne el Jefe DTI.

#### Escalamiento

Si en cualquier fase el Comité de Crisis determina que el alcance del incidente es mayor a lo definido inicialmente, el presidente debe escalar al Comité Superior de Gestión de Incidencias.

## Preparación

Herramientas y recursos disponibles antes de cualquier incidente, mantenidas y actualizadas por el representante que preside el Comité según nivel de criticidad.

### Instalaciones y comunicación

**Información de contacto**: registro de partes interesadas dentro y fuera de la organización (titular y subrogante): Equipo de Respuesta ante Incidentes, Autoridades, Comunicaciones, Jurídica, Recursos Humanos, Administración y Servicios. Debe incluir números de teléfono y correos electrónicos.

**Canales únicos de reporte de incidentes**:

| Canal | Destino |
|-------|---------|
| Teléfono | CA +(562) 800 123 573 |
| Correo técnico (requerimientos, incidencias) | mdas@minsal.cl |
| Correo seguridad (eventos, debilidades, incidentes, amenazas, riesgos) | seguridadtic@minsal.cl |

**Sistema de registro de incidentes**: para monitoreo y seguimiento del estado.

**Teléfonos móviles**: para personal asignado a gestión de incidentes en terreno o fuera de dependencias principales.

**Software de encriptación de comunicaciones**: para comunicaciones sensibles entre miembros del equipo de respuesta, partes internas y externas, PDI, Ministerio del Interior, etc.

**Sala de Crisis**: sala fija o temporal para centralización de comunicaciones y coordinación.

**Almacenamiento seguro**: para custodia de evidencia u otro material sensible.

### Hardware y software

- Estaciones de trabajo para actividades forenses y dispositivos de respaldo (imágenes, logs, datos relevantes).
- Notebooks para análisis de datos, paquetes y redacción de reportes.
- Estaciones de trabajo, servidores y equipamiento de red extra (físico o virtualizado) para restaurar respaldos o gestionar malware.
- Medios extraíbles en blanco (pendrive, discos duros).
- Impresora.
- Analizadores de tráfico para capturar y analizar tráfico de red.
- Software de análisis forense para imágenes de disco.
- Medios extraíbles con versiones confiables de programas para obtención de evidencia.
- Accesorios para recopilar evidencias: notebooks, cámaras digitales, grabadoras de audio, formularios de cadena de custodia, etiquetas y bolsas de custodia, cinta adhesiva de custodia.

### Recursos para el análisis

- Listado de puertos, incluidos los usados comúnmente por troyanos.
- Documentación de sistemas operativos, aplicaciones, protocolos y manuales de antivirus.
- Diagrama de red y listado de activos críticos (aplicaciones, bases de datos, servidores, etc.).
- Línea base de red, sistema y actividades de las aplicaciones.
- Arquitectura del sistema afectado.

### Software para mitigación

Acceso a imágenes de sistemas operativos y aplicaciones para recuperación y restauración.

## Identificación

Si se determina incidente que requiere Comité de Crisis:

1. Aviso inmediato a sus miembros.
2. El Encargado del Comité según nivel coordina acciones de contención y erradicación.
3. Registro de todas las actividades y comunicaciones, respondiendo: ¿quién?, ¿qué?, ¿dónde?, ¿por qué?, ¿cómo?
4. Activación de comunicación interna y con terceras partes según tipo y nivel del incidente.
5. Una vez determinado el alcance, activado el comité y registrado lo ocurrido, avanzar a contención.

## Contención

El Comité de Crisis coordina la contención para minimizar daños. Responsables de contención varían según tipo de incidencia (ver §Comité de Crisis).

### Acciones inmediatas de contención

Detener de inmediato el incidente y contener los daños. Ejemplos: aislación de segmento de red con estaciones infectadas, sacar de producción servidores comprometidos, apagar switch. No son soluciones definitivas: solo limitan la escalación.

### Respaldo de la información

Respaldos de activos afectados para preservar evidencia para análisis forense y acciones legales.

### Acciones de contención para restablecer operaciones

Remediación para restablecer operaciones: levantar respaldos, activar sites de contingencia, activar procesos manuales, remover cuentas comprometidas y puertas traseras, instalar parches de seguridad, y toda acción destinada a evitar escalación.

## Plan de comunicación

### Criterio

Nivel de peligrosidad asignado al incidente como referencia. Si a lo largo del desarrollo, mitigación o resolución se categoriza con un nivel que requiera plan de comunicaciones, activarlo para actores involucrados (equipos de trabajo, árbol de llamadas, clientes, proveedores).

El Encargado de Seguridad de la Información y Ciberseguridad informa al Jefe del Departamento de Tecnologías los incidentes con nivel de severidad Rojo.

### Cadena de escalamiento de comunicación

```
Encargado de Seguridad de la Información y Ciberseguridad
 → Jefe del Departamento de Tecnologías
 → Jefe Gabinete Ministro
 → Jefe Gabinete SRA (Subsecretaría de Redes Asistenciales)
 → Jefe Gabinete SSP (Subsecretaría de Salud Pública)
 → Director Operativo CSIRT
 → Director General CSIRT
 → Consejo Nacional de Ciberseguridad (CNC)
 → Subsecretario del Interior
 → Ministro de Interior y Seguridad Pública
 → Presidente de la República
```

**Comunicación preventiva al SOC**: según nivel de severidad, informar al Coordinador SOC, quien informa en detalle al Director Operativo y General de CSIRT.

**Comunicación oficial a medios públicos**: coordinar con el Jefe del Departamento de Comunicaciones, quien visa el texto a publicar y los medios a utilizar.

## Erradicación

El Comité de Crisis gestiona la restauración de activos afectados:

1. Ejecutar todas las acciones para remover cualquier contenido malicioso o ilícito.
2. Asegurar que los sistemas o procesos están "limpios".
3. Implementar todas las protecciones para evitar recurrencia, basado en lo aprendido (ej. instalación de parches, actualización de sistemas, compra de equipamiento).

## Recuperación

El Comité de Crisis gestiona la recuperación de procesos una vez erradicadas las vulnerabilidades, con testeo, monitoreo y validación de efectividad.

**Definiciones requeridas**:
- Fecha y hora de restauración de las operaciones.
- Metodología de testeo para verificar que los activos afectados no son vulnerables y son completamente funcionales.
- Duración del monitoreo para verificar comportamiento anómalo.
- Herramientas para monitoreo y validación del comportamiento de los activos afectados.

## Lecciones aprendidas

El presidente del Comité de Crisis gestiona la documentación completa de todas las actividades realizadas, más cualquier información beneficiosa para futuros incidentes.

**Plazo máximo del informe**: dos semanas para confección y aprobación.

**Campos mínimos del informe**:
- Cuándo fue detectado el problema y por quién.
- Alcance de la incidencia.
- Cómo fue contenido y erradicado.
- Trabajos realizados durante la recuperación.
- Áreas en donde el Comité fue efectivo.
- Áreas en los que se necesita mejorar.
- Recomendaciones de mejora para la gestión de incidencias.

## Registros

- Informe de gestión de la incidencia.
- Evidencia recopilada durante el proceso.
- Registros de las actividades ejecutadas durante la gestión de la incidencia.

## Difusión

Al menos mediante los siguientes canales:
- Publicación en la intranet de MINSAL: [isalud.minsal.cl](http://isalud.minsal.cl/).
- Correo informativo.

El contenido debe ser accesible y comprensible para todos los usuarios.

## Revisión y medición

Revisión cada dos años o cuando ocurran cambios significativos para asegurar continua idoneidad, eficiencia y efectividad.

## Excepciones

El Comité de Seguridad de la Información evalúa casos especiales. Puede establecer condiciones puntuales de excepción siempre que no infrinja las políticas internas existentes.

Toda excepción debe ser documentada y generar un proceso de revisión del procedimiento que determine si se deben agregar condiciones de operación particulares.

## Control de versiones

| Versión | Fecha | Motivo del cambio |
|---------|-------|-------------------|
| 01 | Diciembre (sin año especificado) | Creación del documento |

## Anexo A: Checklist de gestión de incidencias

### Preparación

- Todos los miembros conocen las políticas de seguridad.
- Todos los miembros tienen claro a quién contactar en caso de incidentes.
- Todos los miembros tienen acceso a herramientas, equipamiento y registros para el proceso.
- Todos los miembros tienen experiencia o han realizado simulacros de incidentes.

### Identificación

- Dónde ocurrió el incidente.
- Quién reportó o descubrió el incidente.
- Cómo fue descubierto.
- Más de un área comprometida: cuáles y cuándo fue descubierto.
- Impacto del incidente.
- Fuentes del incidente identificadas (dónde, cuándo y cuáles).

### Contención

**Acciones inmediatas**:
- ¿El problema puede ser aislado? Si sí, aislar. Si no, gestionar con dueños y encargados de activos y terceras partes relevantes para determinar acciones de contención.
- ¿Todos los activos comprometidos están aislados de los no comprometidos? Si sí, continuar. Si no, continuar aislando para evitar escalamiento.

**Respaldo de la información**:
- ¿Copias forenses de activos afectados creadas y resguardadas para futuros análisis?
- ¿Todos los comandos y documentación relevante desde que ocurrió el incidente se mantiene actualizada? Si no, documentar todas las acciones lo antes posible para retener evidencia para análisis futuros (técnicos y legales) y lecciones aprendidas.
- ¿Copias forenses almacenadas en lugares seguros? Si no, resguardarlas en lugar seguro para prevenir pérdida o manipulación indebida.

**Restablecimiento de operaciones**:
- Si el activo puede ser aislado del proceso y continuar operaciones, proceder a erradicación.
- Si el activo debe continuar en el proceso, restablecer operaciones removiendo cualquier vulnerabilidad (remover malware, hardening, etc.).

### Erradicación

- ¿Los activos afectados pueden ser rediseñados o fortalecidos (hardening, parches, contramedidas) para reducir riesgo de ataques? Si no, responder por qué.
- ¿Todas las vulnerabilidades y artefactos utilizados por el atacante han sido removidos y los activos fortalecidos contra esas vulnerabilidades? Si no, responder por qué.

### Recuperación

- ¿Todos los activos afectados han sido parchados y fortalecidos frente al ataque reciente? ¿Existen posibilidades de un ataque futuro?
- Fecha y hora en que los procesos pueden ser restablecidos.
- ¿Qué herramientas se utilizarán para testear, monitorear y verificar que los procesos han sido restablecidos y no son vulnerables a los mismos métodos de ataque?
- ¿Durante cuánto tiempo se monitorearán los procesos restablecidos?
- ¿Existen indicadores que permitan definir una línea base para medir el grado de cumplimiento de los procesos restaurados?

### Lecciones aprendidas

- ¿Existe toda la documentación del incidente? Si sí, generar el Informe de Incidente. Si no, generarla lo antes posible antes de que la información se olvide o pierda.
- ¿El informe de gestión de incidentes responde a: ¿qué?, ¿dónde?, ¿por qué?, ¿cómo?
- ¿Es posible generar el informe dentro de las dos semanas posteriores al incidente? Si no, explicar por qué y cuándo estará disponible.
- Reunión de lecciones aprendidas: analizar el proceso de respuesta con todos los miembros del comité. ¿Existen áreas en las que sea necesario mejorar? Si no existen, explicar por qué.
