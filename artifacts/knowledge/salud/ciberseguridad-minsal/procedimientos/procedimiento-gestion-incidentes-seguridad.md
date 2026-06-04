---
_manifest:
  urn: urn:salud:kb:procedimiento-gestion-incidentes-seguridad
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-04'
    source: MINSAL Chile, SGSI Nivel Central. PROS-NC-007 v07, Noviembre 2024
  minsal_id: PROS-NC-007
  minsal_version: '07'
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- procedimiento
- incidentes
- respuesta
- csirt
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 2
    shard_root_urn: urn:salud:kb:procedimiento-gestion-incidentes-seguridad
relations:
  cites:
  - urn:salud:kb:instructivo-seguridad-informacion-ciberseguridad-sector-salud
  - urn:salud:kb:stack-tecnologico-seguridad-minsal
---

# Procedimiento Gestion de Incidentes de Seguridad de la Informacion


## Proposito y alcance

Deteccion oportuna y tratamiento de vulnerabilidades o eventos que comprometan activos de informacion institucionales. Respuesta rapida, eficaz y ordenada ante incidentes que afecten confidencialidad, integridad o disponibilidad.

Aplica a: funcionarios (planta, contrata, reemplazos, suplencia), personal a honorarios y terceros con acceso a informacion del MINSAL en ambas Subsecretarias (Salud Publica, Redes Asistenciales).

**Activos cubiertos**: bases de datos, documentos, equipos, expedientes, formularios, infraestructura fisica, personas, sistemas de informacion, software.

**Controles ISO 27001:2022 asociados**: A05.5 (Contacto con autoridades), A05.6 (Contacto con grupos de interes), A06.8 (Notificacion de eventos y puntos debiles), A05.09 (Inventario de informacion), A05.13 (Etiquetado), A05.24 (Planificacion), A05.26 (Respuesta a incidentes), A05.27 (Aprendizaje), A05.28 (Recopilacion de evidencias).

## Terminologia

**Amenaza** - Causa potencial de incidente que podria danar la organizacion o activos. Interna o externa, intencional o accidental.

**Ciberataque** - Actividad intencional que explota vulnerabilidades para acceder, modificar, interrumpir o destruir informacion, sistemas o servicios.

**Clasificacion de Incidentes** - Evaluacion segun severidad y priorizacion usando impacto operativo, alcance, activos afectados y probabilidad de recurrencia.

**CSIRT** - Grupo designado para coordinar y ejecutar respuesta a incidentes, compuesto por especialistas en seguridad, TI y representantes segun corresponda.

**Evento de Seguridad** - Ocurrencia identificada que indica posible incumplimiento de politica, falla de controles o situacion desconocida relevante para la seguridad.

**Gestion de Incidentes** - Proceso estructurado para identificar, analizar, responder y aprender de incidentes minimizando danos y previniendo recurrencia.

**Incidente de Seguridad** - Evento o serie de eventos no deseados con probabilidad significativa de comprometer operaciones y amenazar la seguridad de la informacion.

**Lecciones Aprendidas** - Analisis post-incidente que identifica oportunidades de mejora en procesos, controles y respuesta.

**Notificacion de Incidentes** - Comunicacion formal a partes interesadas sobre ocurrencia, impacto y medidas de mitigacion, conforme a requisitos legales y contractuales.

**Recuperacion** - Restauracion de operaciones normales de sistemas y servicios afectados, garantizando seguridad y estabilidad.

**Registro de Incidentes** - Documento o sistema para registrar, rastrear y gestionar incidentes (naturaleza, clasificacion, impacto, acciones).

**Resiliencia Cibernetica** - Capacidad de resistir, recuperarse y adaptarse frente a incidentes minimizando impacto operacional.

**Respuesta a Incidentes** - Acciones de contencion, mitigacion, investigacion y resolucion asegurando continuidad.

**Riesgo de Seguridad** - Combinacion de probabilidad de ocurrencia y consecuencias negativas.

**Vulnerabilidad** - Debilidad en sistema, proceso o configuracion explotable para comprometer seguridad.

## Marco normativo

- NCh ISO 27001:2022 — Seguridad de la informacion, ciberseguridad y proteccion de la privacidad
- Marco Juridico SSI publicado en portal CSIRT del Ministerio del Interior
- Decretos Supremos y Normas Internacionales de Seguridad de la Informacion
- Ley 18.845 (1989) — Sistema de microcopia o micrograbacion de documentos
- Ley 19.799 — Documentos y firmas electronicas
- Ley 19.880 — Bases de procedimientos administrativos
- Ley 20.584 — Derechos y deberes de los pacientes
- Ley 21.180 — Transformacion Digital del Estado
- Ley 21.663 — Marco de Ciberseguridad
- Ley 21.668 — Interoperabilidad de fichas clinicas
- Decreto 181 (2002) — Reglamento Ley 19.799
- DFL 1 (2005) — Ministerio de Salud
- Decreto 41 (2012) — Reglamento de ficha clinica
- DFL 725 (1968) — Codigo Sanitario
- Decreto 273 (2022) — Obligacion de reportar incidentes al CSIRT de Gobierno
- Decreto 533 — Marco regulatorio en ciberseguridad para instituciones publicas
- Decreto Supremo 7 — Norma Tecnica de Seguridad de la Informacion y Ciberseguridad

## Roles y responsabilidades

### Funcionarios

- Manejar, utilizar y proteger acceso a documentos institucionales garantizando integridad, disponibilidad y confidencialidad
- Informar oportunamente cualquier evento, debilidad o sospecha de incidente via canales oficiales

### Encargado de Seguridad de la Informacion y Ciberseguridad

- Disenar, actualizar y garantizar cumplimiento del procedimiento
- Supervisar acciones correctivas y preventivas
- Enlace principal entre alta direccion, partes interesadas y otras areas
- Informar a alta direccion sobre incidentes criticos y coordinar respuestas estrategicas
- Gestionar y priorizar eventos e incidentes, liderando medidas de mitigacion
- Informar a CSIRT de Gobierno segun Decreto 273 (2022) y Ley 21.180

### Departamento de Tecnologias

- Soporte tecnico en gestion de incidentes sobre sistemas e infraestructura TIC
- Identificar y remediar vulnerabilidades explotadas
- Proporcionar logs, configuraciones y datos tecnicos para analisis
- Coordinar unidades internas de Infraestructura, Operaciones, Desarrollo y Seguridad
- Implementar recuperacion y restauracion de servicios afectados

### Unidades responsables de los datos

- Cumplir politicas de seguridad y aplicar el procedimiento
- Representar intereses de areas afectadas y colaborar en gestion de impacto
- Informar incidentes detectados en sus areas
- Apoyar evaluacion de impacto en sus procesos
- Implementar recomendaciones para mitigar riesgos futuros

### Equipo de Respuesta de Incidentes

- Supervisar que equipos/areas resolutoras gestionen segun nivel de criticidad
- Gestionar incidentes de acuerdo con nivel de criticidad
- Coordinar respuesta de alto impacto con: Infraestructura Fisica, Operaciones TIC, RRHH, Unidad Juridica, Servicios Generales/Division de Administracion, Unidades responsables de datos

### Equipos/Areas resolutoras designadas

- Coordinar activacion de equipos de respuesta
- Identificar causa raiz y proponer medidas correctivas
- Generar y mantener reportes documentados
- Seguimiento de medidas de mitigacion hasta cierre
- Comunicacion activa con CSIRT de Gobierno

## Canales de notificacion

Todo el personal debe informar de manera inmediata cualquier debilidad, evento, incidente, amenaza o riesgo mediante canales unicos oficiales:

| Canal | Contacto |
|---|---|
| Telefonico | +562 800 123573 |
| Correo tecnico (requerimientos e incidencias) | md@minsal.cl |
| Correo seguridad (eventos, debilidades, incidentes, amenazas, riesgos) | seguridadtic@minsal.cl |

## Flujo de notificacion y gestion de incidentes

### Recepcion y analisis inicial

1. Personal detecta evento/vulnerabilidad y reporta via canales oficiales
2. Encargado de Seguridad contacta a quien reporta y jefatura del area en maximo **24 h** para recolectar antecedentes
3. Analisis de antecedentes con tres resultados posibles:
 - **No es amenaza**: cierre del registro, se informa a quien reporto
 - **Es vulnerabilidad**: gestion de mitigacion con duenos de activos, area competente o Comite de Seguridad
 - **Es incidente**: activacion del proceso de Gestion de Incidentes

### Identificacion de equipos resolutores

Asignacion documentada de equipos o areas resolutoras segun naturaleza del incidente:

| Activo afectado | Responsable de respuesta |
|---|---|
| Base de datos, Formulario, Infraestructura TIC, Sistema, Software | Departamento TIC |
| Documento, Expediente | Departamento donde se desarrolla el proceso |
| Otros equipos | Departamento Administracion y Servicios |
| Infraestructura fisica | Departamento Administracion y Servicios |
| Persona | Departamento RRHH |

### Niveles de escalamiento

Tres niveles segun impacto y severidad:

| Nivel | Descripcion | Responsable |
|---|---|---|
| Nivel 1 | Registro y clasificacion inicial | Mesa de ayuda, Resolutor Nivel 1, Encargado Seguridad |
| Nivel 2 | Evaluacion y respuesta inmediata | Evaluador Nivel 2, Encargado Seguridad |
| Nivel 3 | Crisis: incidente se agrava, afecta activos vitales, se prolonga | Comite de Crisis |

## Tipos de incidente

| Tipo | Ejemplos |
|---|---|
| **Informatico** | Denegacion de servicios, codigo malicioso, accesos no autorizados, incidentes que afecten continuidad de operaciones TIC |
| **No informatico** | Violaciones a confidencialidad/integridad/disponibilidad de documentos, filtracion de informacion reservada, incidentes por la naturaleza, acceso fisico no autorizado |

Clasificacion taxonomica segun referencia ENISA: https://www.enisa.europa.eu/publications/reference-incident-classification-taxonomy

## Nivel de criticidad

| Nivel | Impacto sobre activos |
|---|---|
| **Bajo** | Danos sin consecuencias relevantes |
| **Medio** | Consecuencias importantes |
| **Alto** | Consecuencias graves |
| **Muy Alto** | Consecuencias catastroficas |
| **Critico** | Consecuencias criticas sobre procesos de negocio institucionales |

## Procedimiento Nivel 1: Registro y clasificacion

- Mesa de ayuda o Resolutor Nivel 1 registra el incidente
- Clasificacion por: origen, tipo y nivel de criticidad
- Registro de: descripcion, responsables, analisis de ocurrencia, tiempo de respuesta, solucion, tipo/volumen/costo
- Si hay implicancias legales, poner antecedentes en conocimiento de Division Juridica y Jefe de Servicio
- **Obligaciones de registro**: recopilar evidencia tras verificacion, clasificar severidad, efectuar escalamiento Nivel 2 si pertinente, asegurar registro de todas las actividades de respuesta, comunicar a personas u organizaciones que deban ser informadas, manejar debilidades que causan o contribuyen al incidente

## Procedimiento Nivel 2: Analisis y respuesta inmediata

### Evaluacion Nivel 2

Actividades del evaluador cuando el incidente se considera relevante:

1. Analizar toda la informacion recopilada
2. Validar o reclasificar severidad
3. Gatillar respuesta inmediata
4. Iniciar cadena de custodia
5. Realizar analisis forense segun sea necesario
6. Ejecutar Plan de Comunicaciones Interna
7. Documentar el incidente

Todos los incidentes evaluados en Nivel 2 (incluyendo falsos positivos) deben ser revisados mediante analisis post-incidente para: identificar origen, implicancias, impacto, tendencias y mejora continua.

Si el incidente tiene severidad Nivel 3 o superior y **NO esta bajo control** pese al plan de respuesta inmediata, se activa el Proceso de Gestion de Crisis.

### Respuesta Inmediata

Responsable del activo designado para respuesta inmediata ejecuta:

| Accion | Descripcion |
|---|---|
| Contencion del dano | Evitar propagacion, coordinar actividades para disminuir probabilidad y consecuencia |
| Reclasificacion | Reclasificar si es necesario |
| Proteccion de evidencias | Resguardar evidencias recopiladas durante la gestion |
| Notificacion externa | Notificar a organismos externos cuando sea necesario (Carabineros, PDI, Bomberos, etc.) |
| Recuperacion de sistemas | Contactar administrador de sistemas para gestionar recuperacion |
| Escalamiento a proveedores | Contactar proveedores expertos en el activo vital para plan de accion |
| Documentacion | Recopilar todos los antecedentes del incidente |

## Procedimiento Nivel 3: Gestion de Crisis

Activacion cuando el incidente se agrava en severidad o impacto sobre personas, procesos, propiedad o infraestructura (Activos Ministeriales Vitales) y es probable que continue de forma prolongada.

### Comite de Crisis

Presidido por la figura maxima con capacidad de decision (responsable maximo del organismo o representante del Gabinete). Debe tener representacion y subrogante de:

| Area | Responsabilidades |
|---|---|
| **Direccion General / Presidente** | Inicia gestion de crisis, preside el comite, delega responsabilidades, se mantiene informado, actua como portavoz si las circunstancias lo exigen |
| **Encargado Seguridad / CISO** | Primero en conocer el incidente, determina nivel de criticidad (Impacto y Urgencia), decide si trasladar al Comite de Crisis, notifica al CSIRT de referencia, determina primeras acciones operativas de contencion, gestiona continuidad de servicios (respaldos, sitios de contingencia) |
| **TIC** | Revisa entorno comun de aplicaciones (comunicaciones, firewall, DNS), revisa entornos especificos por aplicacion, gestiona servidores virtuales si necesario, activa politica de copias de seguridad |
| **PMO / Encargado Proyecto** | Coordina con proveedores acciones de contencion, erradicacion y cierre |
| **Juridica** | Determina responsabilidades legales directas, da seguimiento a acciones segun leyes y normas aplicables, orienta sobre asuntos legales |
| **Comunicaciones** | Integra el comite con Manual de comunicaciones de crisis, decide mensajes clave/formato/canal segun grupos de interes, activa seguimiento de la crisis en medios y redes sociales, mantiene contacto con medios |
| **Administracion y Finanzas** | Analiza recursos necesarios para resolucion, recopila informacion y evalua hechos, plantea opciones, mantiene contacto con aseguradoras (si aplica) |
| **Infraestructura Fisica** | Portavoz ante funcionarios y representantes |
| **Recursos Humanos** | Gestiona acciones operativas en incidentes relacionados con personas, comunica con afectados, facilita informacion o asistencia basica, evalua animo de funcionarios y recomienda acciones |

### Declaracion de nivel de crisis

| Atributo | Bajo | Medio | Alto | Muy Alto | Critico |
|---|---|---|---|---|---|
| Declaracion de Crisis | NO | NO | OPCIONAL | SI | SI |
| Ambito de Gestion | Operativo | Operativo | Estrategico / Gobierno de crisis | Estrategico / Gobierno de crisis | Estrategico / Gobierno de crisis |
| Preside | Encargado Ciberseguridad | Encargado Ciberseguridad | Encargado Seguridad + TIC y Negocio | Encargado Seguridad | Representante Direccion |
| Procedimiento aplicable | Gestion de Incidentes | Gestion de Incidentes | Gestion de Crisis | Gestion de Crisis | Gestion de Crisis |

Niveles bajo y medio no requieren Comite de Crisis; los equipos tecnicos resuelven en nivel operativo bajo responsabilidad directa del Encargado de Ciberseguridad.

## Proceso disciplinario

Si el incidente es de mayor gravedad o se sospecha delito:

- El Comite de Seguridad, asesorado por Division Juridica, informa al Jefe Superior del Servicio
- De precisarse, se notifica a: Carabineros, Bomberos, Ambulancias, Ministerio Publico
- Si existen responsabilidades administrativas: el Comite solicita instruccion de procedimiento disciplinario segun Estatuto Administrativo
- Para personal a honorarios o terceros: se evalua termino anticipado del contrato o aplicacion de sancion contractual

## Continuidad de la Seguridad de la Informacion

Si el incidente no puede ser controlado y pone en riesgo operaciones y entrega de productos/servicios, el Comite de Seguridad evalua activacion de procesos de continuidad del negocio.

## Recoleccion de evidencia

Responsabilidad del responsable del activo involucrado, reportada al Encargado de Seguridad.

**Documentos en papel**:

- Levantar inventario
- Original en cadena de custodia, guardado de manera segura con registro de: quien encontro, donde, cuando, testigo del descubrimiento
- Asegurar que originales no sean alterados
- Usar copias numeradas de circulacion controlada para analisis

**Informacion en medios computacionales**:

- Generar imagen espejo en presencia de ministro de fe
- Levantar inventario e iniciar cadena de custodia
- Archivos originales y copias espejo guardados de manera segura e intactos (mecanismos de proteccion, encriptacion)
- Si no es factible aislar el original de produccion, la copia 1 se considera original siempre que se resguarde el procedimiento
- Imagenes o copias espejo de medios removibles, discos duros o memorias: numeradas y retenidas para asegurar disponibilidad
- De todas las operaciones de analisis: levantar acta identificando personas, detalle de operaciones, hallazgos o resultados
- Registro de todas las acciones durante el copiado; proceso ante testigos
- Trabajo forense solo sobre copias del material de evidencia
- Supervisar y registrar: cuando y donde se ejecuto el copiado, quien realizo las actividades, que herramientas y programas se utilizaron
- Si corresponde, evidencia entregada al Comite de Seguridad para evaluacion de procesos disciplinarios

## Comunicacion a los involucrados

Una vez contenido el incidente, el Encargado de Seguridad informa a los involucrados.

## Analisis de causa y cierre

Responsable del activo designado para resolucion:

1. Realizar analisis de causas del incidente
2. Si el incidente no esta cerrado: seleccionar e implementar plan de accion con plazo definido, dejando registro
3. Seguimiento del plan: responsabilidad del Encargado de Seguridad
4. Registrar cierre en informe de cierre de incidente

## Aprendizaje de incidentes

Al menos cada **6 meses**, el Encargado de Seguridad revisa los incidentes del periodo analizando:

- Posibles tendencias
- Eficacia de los tratamientos implementados
- Cuantificacion de tipos, volumenes y costos
- Incidentes recurrentes o de alto impacto
- Problemas subyacentes y medidas correctivas desarrolladas
- Necesidades de nuevos controles para limitar frecuencia, dano y costo futuro

Con estos antecedentes, propone al Comite de Seguridad medidas para prevenir recurrencia y promover aprendizajes.

## Plazos de notificacion de incidentes

Segun Ley 21.663 (Ley Marco de Ciberseguridad), todo incidente debe notificarse al CSIRT Nacional dentro de:

| Plazo | Accion requerida |
|---|---|
| **3 horas** | Alerta temprana desde que se conoce el incidente |
| **72 horas** | Actualizacion con evaluacion inicial, gravedad e impacto |
| **15 dias corridos** | Informe final con medidas adoptadas |

**Criterios de notificacion obligatoria al CSIRT Nacional**: incidentes que provoquen interrupcion de la continuidad de un servicio esencial, afecten la integridad fisica o salud de las personas, o afecten sistemas informaticos que contengan datos personales.

El incumplimiento de estos plazos se considera **falta grave**, derivable en acciones disciplinarias o contractuales.
