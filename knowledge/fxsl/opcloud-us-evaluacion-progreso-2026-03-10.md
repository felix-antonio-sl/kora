# Evaluacion de Historias de Usuario OPCloud

Fecha: 2026-03-10
Estado: evaluacion completa S1-S49, revision exhaustiva 183 frames (61 videos)
Alcance cubierto: S1-S49 evaluadas (543 HU en 91 epicas)

## Objetivo

Consolidar la evaluacion del documento de historias de usuario de OPCloud generado por ingenieria inversa, contrastandolo con:

- el marco metodologico OPM en `knowledge/fxsl/opm-methodology`
- la app `https://opcloud-sandbox.web.app/`
- la carpeta de frames extraidos de videos en `/Users/felixsanhueza/Downloads/youtube/frames`
- capturas manuales adicionales compartidas durante la sesion

## Fuentes usadas

### Documento base de historias

- `/Users/felixsanhueza/Downloads/historias-de-usuario-opcloud-consolidado.md`

### Marco metodologico

- `/Users/felixsanhueza/Developer/kora/knowledge/fxsl/opm-methodology/00-indice.md`
- `/Users/felixsanhueza/Developer/kora/knowledge/fxsl/opm-methodology/01-ontologia-opm.md`
- `/Users/felixsanhueza/Developer/kora/knowledge/fxsl/opm-methodology/02-diagrama-sistema.md`
- `/Users/felixsanhueza/Developer/kora/knowledge/fxsl/opm-methodology/03-comportamiento-control.md`

### Evidencia visual

- carpeta de frames: `/Users/felixsanhueza/Downloads/youtube/frames`
- cobertura final: 183 frames de 61 videos
- series: Intro 1-50 (49 videos) + Advance 1-9 (10 videos) + 2 adiciones tardias (Intro 49, Intro 50)
- patron: 3 capturas por video (`25pct`, `50pct`/`55pct`, `75pct`)

### Evidencia web

- acceso directo a `youtube.com` para validar disponibilidad de videos y metadatos
- inspeccion basica de `opcloud-sandbox.web.app` como SPA

## Modelo de evidencia usado

Para evitar sobreinferencias, cada HU se clasifica con uno de estos niveles:

- `frame-confirmada`: la capacidad es visible claramente en un frame
- `video-confirmada`: la capacidad parece real por el video o su narrativa, pero no queda fijada claramente en un frame
- `inferida`: deduccion razonable desde comportamiento o UI cercana, pero no observada de forma suficiente
- `sobreinferida`: la HU especifica reglas, restricciones o politicas no observables en la evidencia disponible
- `pendiente`: sin evidencia suficiente con las fuentes revisadas

## Hallazgos globales

### 1. El backlog esta sobrefragmentado

El consolidado resume `543` historias en `91` epicas. Eso funciona como inventario enciclopedico, pero no como backlog priorizable.

Patrones observados:

- una misma capacidad se divide en demasiadas HU micro-UI
- muchas HU deberian ser criterios de aceptacion o variantes de flujo
- hay epicas muy cargadas de detalle fino y otras que cubren capacidades mas nucleares con menos estructura

### 2. El documento mezcla backlog funcional con material tutorial

El caso mas claro es `EP-32`, que el propio documento declara como contexto del modelo OnStar y no como funcionalidad de producto.

Impacto:

- contamina metricas
- dificulta priorizacion
- mezcla evidencias de ejemplo con comportamiento real del sistema

### 3. Hay duplicaciones reales

Duplicaciones detectadas hasta ahora:

- `HU-0302` y `HU-0303`: misma interaccion de tabla de enlaces con preview OPL
- `HU-1008` y `HU-2802`: editar nombre de un thing desde OPL
- `HU-1009` y `HU-1010` reaparecen como `HU-5716` y `HU-5717`
- `HU-8705` (EP-87) duplica parcialmente `HU-9101` (EP-91): ambas describen anclar estereotipos
- `HU-8803` (EP-88) duplica parcialmente `HU-8703` (EP-87): ambas describen el IDE integrado

Impacto:

- riesgo de mantenimiento inconsistente
- discusiones sobre fuente de verdad
- inflacion artificial del backlog

### 4. El backlog esta sesgado hacia UI y menos hacia semantica OPM

Del marco OPM surgio una brecha importante:

- el sistema deberia reflejar estructura, comportamiento y funcion
- el `System Diagram` deberia cubrir proposito, beneficiario, funcion principal, habilitadores, entorno y ocurrencia del problema
- la equivalencia `OPD <-> OPL` es central

El backlog actual cubre muy bien modelado visual y mucha interaccion UI, pero mucho menos:

- arranque metodologico del SD
- funcion del sistema
- beneficiario y atributo beneficiario
- control semantico fuerte del modelo como sistema OPM

Nota: el frame de Intro 39 (Sub Models) muestra un **New Model Wizard** de 12 etapas que si cubre arranque del SD (Stage 10: Main Output, pregunta por output principal, si el output es tambien input, y la relacion del sistema con el output). Esto sugiere que OPCloud SI tiene soporte para arranque metodologico, pero las HU del consolidado NO lo capturan adecuadamente. EP-70 se centra en sub-models, no en el wizard.

### 5. La trazabilidad por sesiones se vuelve menos confiable en bloques avanzados

En los primeros bloques la correspondencia `S# -> feature` es relativamente legible. A partir de bloques intermedios y avanzados, la relacion entre:

- tag `Sxx`
- titulo del video
- evidencia visual disponible

deja de ser transparente. En la practica hubo que validar por feature, no por el numero del video.

### 6. Mismatches sistematicos entre session tags y contenido de video

La revision completa de frames revelo que varios session tags del consolidado no corresponden al contenido real del video:

- **S15** (EP-40 a EP-46 Settings): los frames muestran el canvas de modelado, no la pagina de Settings
- **S20** (EP-57 Link Properties): los frames muestran el modelo OnStar, no dialogo de link properties
- **S23** (EP-60/61 Ontology): los frames muestran Model Chat, no la interfaz de ontologia
- **S25** (EP-64 Resizing): Video 25 muestra Load Model con folders, no resizing (Video 31 muestra resizing)
- **S26** (EP-65 System Map): Video 26 muestra OPD tree arrangement, no System Map (Video 32 muestra System Map)
- **S30** (EP-69 Tabs): Video 30 muestra Folder Permissions dialog, no tabs (Video 38 muestra tabs)

Esto sugiere que los tags de sesion en el consolidado fueron asignados basandose en el contenido completo del video, mientras que los frames solo capturan 3 momentos (25%, 50%, 75%) que pueden no coincidir con el segmento relevante. El impacto es que la clasificacion heuristica basada en session strength sobreestimaba la evidencia para estas sesiones.

### 7. El bloque Advance muestra capacidades avanzadas bien diferenciadas

Los videos Advance 1-9 cubren un eje funcional distinto (simulacion, ejecucion, IoT, robótica) que esta mucho menos atomizado que los Intro. Sin embargo, las HU del consolidado para este bloque (EP-82 a EP-91) mantienen un nivel de detalle alto en reglas que no son visibles en frames estáticos.

## Resumen de avance por bloques

### Bloque S1-S10

Estado: evaluado

Cobertura observada:

- creacion de things
- nombrado y auto-format
- links basicos y tabla de enlaces
- halo e in-zoom
- estados
- panel izquierdo, OPD navigator y OPL
- styling de things
- OPL pane avanzado

Conclusiones del bloque:

- `S1`, `S4`, `S6`, `S7`, `S8` quedan bien respaldadas
- `S2` y `S9` presentan mas riesgo de sobreinferencia
- el bloque inicial describe bien modelado core, pero sigue excesivamente atomizado

Observaciones puntuales:

- el halo esta descrito como demasiadas HU separadas por icono
- varias capacidades del panel OPL se repiten luego en otras epicas
- varias reglas finas de links avanzados no quedan `frame-confirmadas`

### Bloque S11-S20

Estado: evaluado

Cobertura observada:

- OPD tree functions
- search de things
- permisos de modelos
- settings
- advanced loading/saving/versiones/archivados
- semi-fold
- links table avanzada
- link properties avanzadas

Conclusiones del bloque:

- `S12`, `S13`, `S15`, `S16`, `S18`, `S19`, `S20` quedan razonablemente fuertes
- `S17` esta claramente sobreespecificada respecto de la evidencia visual
- `S11` mezcla capacidades reales con reglas no demostradas por frame

Observaciones puntuales:

- exportacion y share tienen demasiado detalle fino para la evidencia disponible
- semi-fold si tiene evidencia visual buena, pero varias microreglas siguen inferidas
- properties de links estan bien probadas, pero duplican funcionalidades descritas antes desde OPL

### Bloque S21-S30

Estado: evaluado

Cobertura observada:

- OPD tree arrangement
- inner/outer things validation
- organization ontology
- templates
- manual/automatic resizing
- system map
- requirements views
- updated OPD tree navigation
- images in things
- create new model por tabs

Conclusiones del bloque:

- `S22`, `S23`, `S24`, `S26`, `S29` son los subbloques mejor anclados
- `S21`, `S25`, `S28`, `S30` contienen mas comportamiento inferido que comportamiento plenamente visible
- `S27` mezcla una capacidad visible real de requirement views con una capa mucho mas ambiciosa de metamodelo de requisitos

Observaciones puntuales:

- en `S22` si hay evidencia visual directa de la advertencia inner/outer
- en `S23` si se observa `Ontology Enforcement Level`
- en `S24` se confirma bien el manejo general de templates, pero no todas sus reglas
- en `S29` se confirma muy bien `Image by URL`, `Insert From Pool` y `Save to Pool`
- la politica de exportacion de imagenes por formato sigue inferida

### Bloque S31-S40

Estado: **evaluado** (cerrado)

#### S31 — Sub-Models (EP-70, 16 HU)

Frames: `39 - Intro 38 - Sub Models` (25%, 50%, 75%) + `40 - Intro 39 - Sub Models` (New Model Wizard)

**Evidencia visible en Video 39 (Intro 38)**:
- **25%**: "Main Model System" tab con sub-model icon. Canvas muestra Sub System 1 y Sub System 2 como objetos compartidos. OPL: "The selected things, Sub System 1 and Sub System 1 Output, and First Processing are refined in sub model Sub System 1 subsystem model view." Context menu con Remove/Expand All/Collapse All/Hide Names.
- **50%**: Dos tabs abiertos simultaneamente: "Main Model System" + "Sub System 1 of Main M...". OPD tree: SD1.1: Sub System 1 Subsystem Model View > SD1.1.1: First Processing in-zoomed **(read only)**. Canvas muestra First Processing con B/C/D Processing dentro.
- **75%**: Mismo dual-tab. OPL: **"SD1.1 is a view OPD, derived from SD1."** Sub System 1 Output con alias {ss1o}.

**Evidencia visible en Video 40 (Intro 39)**: New Model Wizard (Stage 10/12, "Main Output") — capacidad no documentada en EP-70.

Clasificacion por HU:

- HU-7001: `frame-confirmada` — OPL "refined in sub model" directamente visible
- HU-7002: `frame-confirmada` — sub-model nombrado en OPD tree + tab
- HU-7003: `video-confirmada` — icono verde en nodo SD1.1
- HU-7004: `frame-confirmada` — dos tabs abiertos simultaneamente
- HU-7005: `video-confirmada` — objetos compartidos visibles en SD
- HU-7006 a HU-7009: `inferida` — lazy loading, unload/reload, sync, restricciones son comportamientos runtime
- HU-7010: `frame-confirmada` — "(read only)" en SD1.1.1 en OPD tree
- HU-7011 a HU-7014: `inferida` — desconectar, no-reconectar, restricciones, export checkbox no visibles
- HU-7015: `video-confirmada` — jerarquia SD1.1 > SD1.1.1 confirma anidamiento
- HU-7016: `frame-confirmada` — OPL "SD1.1 is a view OPD, derived from SD1" + numeracion visible

Mejora respecto a evaluacion anterior: **5 frame-confirmada, 3 video-confirmada** (antes: 0 frame-confirmada, 12 sobreinferida)

#### S32 — Bring Connected (EP-71, 4 HU)

Frame: `41 - Intro 40 - Bring Connected_75pct.jpg`

Evidencia visible: pagina de Settings > OPCloud Settings mostrando "Default For Bring Connected Things" con dropdown multi-select de tipos de enlace (Procedural Enabling Links, Procedural Transforming Links, Fundamental Structural Links, Tagged Structural Links). Tambien visible: Time Precision, Spell Checking, Notes, Multi Deletion settings.

Clasificacion por HU:

- HU-7103 (configurar defaults en Settings): `frame-confirmada` — el dropdown con checkboxes es directamente visible
- HU-7101 (filtrar por tipo desde barra secundaria): `video-confirmada` — el frame muestra los settings, no la barra
- HU-7102 (usar defaults desde halo sin selector): `inferida` — razonable pero no visible
- HU-7104 (solo things directamente conectados): `inferida` — regla de negocio no observable

#### S33 — Grid (EP-72, 6 HU)

Frame: `42 - Intro 41 - Grid and alignment_75pct.jpg`

Evidencia visible: canvas con modelo in-zoomed (B Processing, C Processing, D Processing dentro de A Processing, Object 2 conectado). Arbol OPD visible, panel de things arrastrables, OPL. La grid como tal no se distingue claramente en el frame (puede estar desactivada o ser demasiado sutil para el screenshot).

Clasificacion por HU:

- HU-7201 (activar/desactivar grilla): `video-confirmada` — plausible por titulo del video, pero el frame no la muestra activa claramente
- HU-7202 a HU-7206 (configuracion de grid): `inferida` — los settings son plausibles pero no visibles en este frame

#### S34 — Move Models (EP-73, 4 HU)

Frame: `43 - Intro 42 - Move Models_75pct.jpg`

Evidencia visible: modal "Load Model" con busqueda, toggle "Show Versions" (activado), "Show Archived" (desactivado), "Include All Subfolders". Carpetas (Dest Folder, OnStar System To Move Versions, The Door Peephole System Versions). Modelos listados con descripcion, fecha, autor. Botones: Current Folder Permissions, Open, Remove Folder, Cancel. Seccion Recent Models con iconos.

Clasificacion por HU:

- HU-7301 (cortar modelo): `video-confirmada` — el modal muestra gestion de modelos, pero no se ve la accion de cortar en si
- HU-7302 (pegar modelo): `video-confirmada` — idem
- HU-7303 (cortar/pegar en vista lista): `video-confirmada` — la vista lista si es visible
- HU-7304 (mover carpetas completas): `video-confirmada` — las carpetas si son visibles

#### S35 — OPD Tree Management (EP-74, 8 HU)

Frame: `44 - Intro 43 - OPD tree managment_75pct.jpg`

Evidencia visible: modal "OPDs Tree Management" con arbol completo del sistema Automated Household Dish Caring. Jerarquia visible hasta 6 niveles de profundidad (SD1.2.1.1.1.1). Campo "Search OPD", toggle "Hide Names". Botones: Open, Cut, Remove, Rename, Close. Tooltip "Double-click to open". Indicadores de tipo (in-zoomed vs unfolded).

Clasificacion por HU:

- HU-7401 (abrir pantalla OPD Management): `frame-confirmada` — el modal completo es directamente visible
- HU-7402 (buscar por nombre): `frame-confirmada` — campo Search OPD visible
- HU-7403 (buscar por numero): `video-confirmada` — el campo existe, pero no se ve una busqueda por numero en accion
- HU-7404 (cortar y pegar OPDs): `frame-confirmada` — boton Cut visible
- HU-7405 (arrastrar y soltar): `inferida` — no visible en el frame estatico
- HU-7406 (eliminar OPD): `frame-confirmada` — boton Remove visible
- HU-7407 (renombrar OPD): `frame-confirmada` — boton Rename visible
- HU-7408 (abrir OPD): `frame-confirmada` — boton Open y tooltip "Double-click to open" visibles

#### S36 — Duplication, Bring Links, Methodology (EP-75, EP-76, EP-77, 10 HU)

Frames: `45 - Intro 44`, `46 - Intro 45`, `47 - Intro 46`

**Intro 44 — Duplication of Names:**
Evidencia visible: modelo con Object 7 unfolded en Object 8, 9, 10. Link estructural de agregacion. Menu contextual (tres puntos) visible cerca de Object 7. OPL confirmando unfold.

- HU-7501 (dialogo de duplicacion): `video-confirmada` — el titulo lo indica pero el frame muestra unfold, no el dialogo
- HU-7502 (usar thing existente): `video-confirmada`
- HU-7503 (restriccion tipos incompatibles): `inferida`

**Intro 45 — Bring Links Between:**
Evidencia visible: modelo OnStar con tooltip oscuro "Bring Links Between Selected Entities" visible. Driver con Danger Status (estados endangered/safe), Driver Rescuing, GPS, Cellular Network, VCIM, OnStar Console. Status "2 elements selected" visible.

- HU-7601 (traer enlaces entre seleccionados): `frame-confirmada` — el tooltip y la multi-seleccion son directamente visibles

**Intro 46 — Methodology Checking:**
Evidencia visible: modal "Invalid Things" con regla "A process must transform (create, consume or affect) at least one object." Tabla con Element/Containing OPD. Procesos invalidos listados: Another Processing, One Sub Processing, Two Sub Processing. Filtro "All Elements" con busqueda. Boton Close.

- HU-7705 (validar conectividad proceso-objeto): `frame-confirmada` — la regla exacta es visible en el modal
- HU-7706 (navegacion a thing problematico): `frame-confirmada` — la tabla muestra el OPD contenedor y la fila es clickeable
- HU-7701 (validar nombres gerundio): `video-confirmada` — el validador existe, pero esta regla especifica no se ve en el frame
- HU-7702 (validar nombres singular): `video-confirmada`
- HU-7703 (validar unfold > 1 parte): `video-confirmada`
- HU-7704 (validar in-zoom > 1 subproceso): `video-confirmada`

#### S37 — CSV Import (EP-78, 6 HU)

Frame: `48 - Intro 47 - Import CSV_75pct.jpg`

Evidencia visible: modelo con Object 1 exhibiendo Attribute1, Attribute2, Attribute3 (via exhibition links). Instance1 visible con Attribute1 mostrando valor "Value11". OPD Navigator minimap visible. OPL confirmando "Object 1 exhibits Attribute1, Attribute2, and Attribute3."

Clasificacion por HU:

- HU-7801 (importar desde CSV): `frame-confirmada` — el resultado de la importacion es directamente visible
- HU-7802 (preview): `video-confirmada` — el frame muestra el resultado, no la preview
- HU-7803 (opcion Ignore): `inferida` — regla de negocio no visible
- HU-7804 (atributos no-computacionales): `inferida`
- HU-7805 (auto-format al importar): `inferida`
- HU-7806 (re-importar): `inferida`

#### S38 — Generative AI Requirements (EP-79, 5 HU)

Frame: `49 - Intro 48 - Generative AI_75pct.jpg`

Evidencia visible: **Microsoft Excel** con archivo "OnStar System_requirements (1).xlsx" en Protected View. Columnas: ID (REQ-0001 a REQ-0023+), ParentID, Category (Structural, Interface, Functional, State), Priority, Risk, Status (Proposed), Statement (texto completo de requisitos), Rationale. Requisitos estructurados desde el modelo OnStar: composicion del sistema, interfaces, funciones, sub-procesos.

Clasificacion por HU:

- HU-7905 (descargar como Excel): `frame-confirmada` — el Excel con estructura completa es directamente visible
- HU-7902 (generar requisitos desde modelo): `frame-confirmada` — los requisitos generados son visibles con clasificacion
- HU-7901 (acceder al menu): `video-confirmada`
- HU-7903 (ver en panel scrollable): `video-confirmada`
- HU-7904 (copiar al portapapeles): `inferida`

#### S39 — Identification of Missing Knowledge (EP-80, 5 HU) — NUEVO

Frame: `66 - Intro 49 - Identification of Missing Knowledge_75pct.jpg`

Evidencia visible: pagina Settings > Analyze Model > Model Knowledge. Tab "Identification of Missing Knowledge" activo. Titulo "Identification of Missing Knowledge Using Machine Learning". Descripcion tecnica del metodo (Graph Neural Networks, DistMult, R-GCN). Tres botones: "DistMult Reasoning", "R-GCN Reasoning", "Download Suggestions (Excel)". Slider de confidence threshold (0.51). Tabla con 4 sugerencias: Source/Relation/Target/Confidence. Ejemplos: Data Base -> Aggregation -> Passenger System (0.524), Software -> Aggregation -> Passenger System (0.518).

Clasificacion por HU:

- HU-8001 (acceder a la seccion): `frame-confirmada` — la navegacion completa es visible
- HU-8002 (ejecutar analisis): `frame-confirmada` — los botones DistMult/R-GCN son visibles y los resultados estan en la tabla
- HU-8003 (ajustar umbral de confianza): `frame-confirmada` — el slider con valor 0.51 es directamente visible
- HU-8004 (descargar como Excel): `frame-confirmada` — boton "Download Suggestions (Excel)" visible
- HU-8005 (copiar al portapapeles): `inferida` — no se ve boton de copiar en el frame

Nota: el consolidado menciona "Pistol Reasoning" (HU-8002) pero el frame muestra "DistMult Reasoning" y "R-GCN Reasoning". La HU tiene un error de nombre.

#### S40 — Model Informativity Grading (EP-81, 5 HU) — NUEVO

Frame: `62 - Intro 50 - Model Informativity Grading_75pct.jpg`

Evidencia visible: pagina Settings > Analyze Model > Model Knowledge. Tab "Model Informativity Grading" activo. Botones "Run Model Grading" y "Download Grades (Excel)". Metricas en cards: TWINF 18.68, WINF 18.68, INF Avg 0.121, OPL Sentences 155. Tabla MFSP Distribution: Meta (0), Precedence (6/1.15), Procedural (43/8.44), Structural (17/1.58), ThingDef (89/7.52), Unknown (0). Seccion Sentence-Level Informativity con filtros por MFSP y Min INF. Tabla de sentencias con columnas #/OPL Sentence/MFSP/INF.

Clasificacion por HU:

- HU-8101 (acceder a Model Informatic Grading): `frame-confirmada` — la navegacion completa es visible
- HU-8102 (ejecutar calificacion): `frame-confirmada` — metricas TWINF, WINF, INF Avg, total OPL visibles, distribucion por categoria visible
- HU-8103 (ver tabla por sentencia): `frame-confirmada` — la tabla con sentencias, MFSP y scores INF es directamente visible
- HU-8104 (filtrar por categoria y score): `frame-confirmada` — dropdown MFSP y campo Min INF visibles
- HU-8105 (descargar como Excel): `frame-confirmada` — boton "Download Grades (Excel)" visible

Nota: esta es la epica con mayor ratio de confirmacion directa por frame de todo el consolidado (5/5 frame-confirmada).

### Bloque S41-S49

Estado: **evaluado** (nuevo)

#### S41 — Conexion ROS (EP-82, 7 HU)

Frame: `60 - Advance 9 - Using ROS with OPCloud_75pct.jpg`

Evidencia visible: modelo Spiral Drawing con TurtleSim. Sidebar muestra arbol profundo (SD1 > SD1.1 > SD1.1.1). Toolbar con botones de simulacion (Play, Stop, step, step counter "1", XLSX, speed slider, "Headless Runner" checkbox) y botones **#ROS** y **MQTT** visibles. A la derecha, ventana separada **TurtleSim** mostrando el simulador ROS con un turtle sprite en fondo azul. Objetos: Turtlesim OPCloud ROS Spiral System, ROS Master Server, Turtlesim Node, Drawing Ability (estados hard/easy). OPL visible.

Clasificacion por HU:

- HU-8202 (conectar/desconectar WebSocket ROS): `frame-confirmada` — boton #ROS visible en toolbar
- HU-8206 (simulacion con conexion ROS real): `frame-confirmada` — la ventana TurtleSim ejecutandose es evidencia directa
- HU-8203 (proceso computacional con opcion ROS): `video-confirmada` — el modelo ROS existe pero la configuracion del proceso no es visible
- HU-8204 (campos Topic/Data Type/Message): `inferida` — los campos de mensajeria no son visibles
- HU-8201 (configurar en Settings): `inferida` — la pagina de settings no es visible
- HU-8205 (descargar WebSocket server code): `inferida`
- HU-8207 (mezclar protocolos): `video-confirmada` — tanto #ROS como MQTT estan visibles en toolbar, sugiriendo soporte mixto

#### S42 — Conexion MQTT IoT (EP-83, 5 HU)

Frame: `58 - Advance 7 Part 6 - Using MQTT_75pct.jpg`

Evidencia visible: modelo IoT "Optimal Light Power Consumption Performing" con objetos fisicos: LDR Sensor, Microcontroller, LED Bulb, User. Objeto Digital Twin: "Room Surroundings Light Intensity_digitaltwin [lx] {rli}". Estados: Electrical Power Consumption Level (high/low). Toolbar con boton **MQTT** y **#ROS** visible. OPL mostrando "is the Digital Twin of". Headless Runner checkbox visible.

Clasificacion por HU:

- HU-8302 (conectar/desconectar MQTT): `frame-confirmada` — boton MQTT visible en toolbar
- HU-8303 (configurar Publish/Subscribe): `video-confirmada` — el modelo MQTT existe pero la configuracion no es visible
- HU-8304 (simulacion con MQTT real): `video-confirmada` — el modelo tiene la estructura pero el frame no muestra datos en tiempo real
- HU-8301 (configurar en Settings): `inferida`
- HU-8305 (detener simulacion): `frame-confirmada` — boton Stop visible en toolbar

Observacion: la capacidad de Digital Twin es significativa y no tiene su propia epica en el consolidado. El OPL muestra "is the Digital Twin of" como una relacion first-class.

#### S43 — Input de Usuario en Simulacion (EP-84, 4 HU)

Frame: `57 - Advance 7 Part 5 - Getting input_75pct.jpg`

Evidencia visible: modelo Spiral Drawing con agente "Turtlesim ROS User" conectado a proceso "Spiral Depth Selecting ()". Objeto "Spiral Depth [m] {sd}" con estado "value". Arbol profundo (SD1 > SD1.1 > SD1.1.1). Toolbar de simulacion con controles completos. OPL: "Turtlesim ROS User handles Spiral Depth Selecting."

Clasificacion por HU:

- HU-8401 (modelar input con agente): `frame-confirmada` — el agent link y la relacion "handles" son directamente visibles en el OPL
- HU-8402 (activar captura de input): `video-confirmada` — el toggle no es visible pero el modelo esta configurado
- HU-8403 (pop-up durante simulacion): `inferida` — el frame no muestra la simulacion ejecutandose
- HU-8404 (variable user input en IDE): `inferida`

#### S44 — Condiciones y Bucles (EP-85, 8 HU)

Frame: `56 - Advance 6 Part 4 - Conditions and loops_75pct.jpg`

Evidencia visible: modelo in-zoomed "A Processing" con: B Processing () (con codigo `return 'yes';` visible), Object 3 con estados "yes" y "no", C Processing y D Processing como ramas condicionales. Marcadores "c" en los links condicionales visibles. Object 1 como input y Object 2 como output.

Clasificacion por HU:

- HU-8501 (rama condicional con instrument condition link): `frame-confirmada` — las ramas con marcador "c" y los estados yes/no son directamente visibles
- HU-8505 (controlar estado via funcion): `frame-confirmada` — el codigo `return 'yes';` es visible en el proceso
- HU-8504 (fijar resultado a estado especifico): `video-confirmada` — plausible desde el modelo pero no demostrado en el frame
- HU-8502 (bucle con invocation link): `video-confirmada` — el titulo lo cubre pero el frame no muestra un bucle
- HU-8503 (seleccion aleatoria): `inferida`
- HU-8506 (update computation directly): `inferida`
- HU-8507 (advertencia bucle infinito): `inferida` — solo se ve boton Stop, no deteccion de bucle
- HU-8508 (probabilidades ponderadas): `inferida`

#### S45 — Validacion de Rangos (EP-86, 7 HU)

Frame: `55 - Advance 5 - Range Validation_75pct.jpg`

Evidencia visible: modelo con "Embedded Device Property Set" y atributos: Reliability [%] {se} con rango **[0..100]**, Cost [$] {c} con rango **(0..*)**, Power Consumption [mA] {pc} con rango **(0..*)**, Dimension Set, Material. Exhibition links conectando atributos al objeto padre. Nodo "stereotypes" visible. OPL mostrando "Reliability, se, is [0..100] %." y "Cost, c, is (0..*) $."

Clasificacion por HU:

- HU-8602 (definir rangos de valores): `frame-confirmada` — rangos [0..100] y (0..*) son directamente visibles tanto en OPD como en OPL
- HU-8601 (definir tipo de valor): `video-confirmada` — los tipos estan implicitos en las unidades pero la seleccion no es visible
- HU-8607 (sub-rangos dentro de estereotipos): `video-confirmada` — el estereotipo con rangos existe pero la interaccion de sub-rango no es visible
- HU-8603 (valor por defecto): `inferida`
- HU-8604 (indicadores de color): `inferida` — posiblemente visible en color pero no distinguible en el frame
- HU-8605 (modo soft vs hard): `inferida`
- HU-8606 (toggle Type): `inferida`

#### S46 — Calculos Avanzados y Aliases (EP-87, 5 HU)

Frame: `54 - Advance 4 Part 3 - User-defined Calculating_75pct.jpg`

Evidencia visible: modelo con estereotipos <<Point>> Point 1 {p1} y <<Point>> Point 2 {p2}. Atributos: X {x} (1, 5) y Y {y} (7, 19) visibles con valores. Proceso "Point Slope Calculating" conectado. Modal **"Function:"** abierto con codigo `return (p2.y-p1.y)/(` (formula de pendiente, parcialmente visible). Boton "Update". OPL mostrando "<<Point>> Point 1, p1, consists of X of Point 1, x, and Y of Point 1, y,."

Clasificacion por HU:

- HU-8703 (funcion definida por usuario): `frame-confirmada` — el IDE con codigo JavaScript es directamente visible
- HU-8701 (establecer alias): `frame-confirmada` — los aliases {p1}, {p2}, {x}, {y} son visibles en el modelo y usados en la funcion
- HU-8702 (acceder a sub-partes via alias): `frame-confirmada` — `p2.y` y `p1.y` en el codigo demuestran acceso a sub-partes via notacion de punto
- HU-8705 (anclar estereotipo): `frame-confirmada` — el nodo "stereotypes" con "Point" y la notacion <<Point>> son directamente visibles
- HU-8704 (ejecutar calculo): `video-confirmada` — los valores de entrada son visibles pero el resultado no se muestra en el frame

#### S47 — Objetos Computacionales y Simulacion (EP-88 + EP-89, 7 HU)

Frame: `53 - Advance 3 Part 2 - Simple Computational_75pct.jpg`

Evidencia visible: modelo simple con Object 1 [m] {o1}, Object 2 [m] {o2}, Object 3 [m] {o3}, cada uno con estado "value". Proceso "Calculating ()" con notacion "()" indicando proceso computacional. Links de consume/instrument desde Object 1 y 2, y result link hacia Object 3. Toolbar de simulacion visible. OPL: "Calculating requires Object 1, o1, and Object 2, o2," y "Calculating yields Object 3, o3,."

Clasificacion por HU:

- HU-8801 (convertir objeto a computacional): `frame-confirmada` — objetos con [m] (unidades), {alias} y "value" state son directamente visibles
- HU-8802 (funcion predefinida): `video-confirmada` — el proceso tiene "()" pero la seleccion de funcion no es visible
- HU-8803 (IDE integrado): `video-confirmada` — el IDE no es visible en este frame (si en Advance 4)
- HU-8901 (simulacion por objeto): `inferida`
- HU-8902 (numero de ejecuciones): `inferida`
- HU-8903 (descargar resultados Excel): `video-confirmada` — boton XLSX visible en toolbar
- HU-8904 (simulacion asincrona): `video-confirmada` — checkbox "Headless Runner" visible sugiere modo asincrono

#### S48 — Simulacion Conceptual (EP-90, 5 HU)

Frame: `52 - Advance 2 Part 1 - Conceptual Simulation_75pct.jpg`

Evidencia visible: modelo OnStar Driver Rescuing in-zoomed con subprocesos (Call Making, Vehicle Location Calculating, Call Transmitting, Call Handling). Objetos Call (estados requested/online), Danger Status (endangered/safe), Vehicle Location, OnStar Advisor. Objetos externos: OnStar Console, Cellular Network, GPS, VCIM. **Toolbar de simulacion completa**: Play, Stop, step-forward, step counter "1", XLSX, speed slider, "Headless Runner" checkbox, #ROS. OPL: "Driver Rescuing zooms in SD1 into Call Making, Vehicle Location Calculating, Call Transmitting, and Call Handling."

Clasificacion por HU:

- HU-9001 (abrir barra de simulacion): `frame-confirmada` — toolbar completa con Play, Stop, speed slider, sync controls directamente visible
- HU-9002 (simulacion conceptual sincronizada): `frame-confirmada` — el step counter en "1" indica que la simulacion esta activa/preparada
- HU-9003 (ajustar velocidad): `frame-confirmada` — speed slider directamente visible
- HU-9004 (detectar errores de orden): `video-confirmada` — plausible pero no demostrado en el frame
- HU-9005 (verificar orden en OPL): `frame-confirmada` — el OPL muestra el orden de subprocesos

#### S49 — Estereotipos OPM (EP-91, 7 HU)

Frame: `51 - Advance 1 - OPM Stereotypes Part 1_75pct.jpg`

Evidencia visible: modelo con "<<Embedded Device Property Set>> Object 1" (notacion guillemet de estereotipo visible). Proceso "A Processing". Sidebar con seccion "Stereotypes" mostrando "Embedded Device Property Set". Tooltip "Entities Extensions" visible en toolbar. OPD Navigator minimap.

Clasificacion por HU:

- HU-9101 (anclar estereotipo): `frame-confirmada` — la notacion <<...>> y el nodo Stereotypes son directamente visibles
- HU-9102 (distinguir organizacionales vs globales): `inferida` — no se ve icono "G" en el frame
- HU-9103 (ver contenido solo lectura): `video-confirmada` — el contenido del estereotipo no se ve expandido
- HU-9104 (desanclar manteniendo componentes): `inferida`
- HU-9105 (desanclar y eliminar todo): `inferida`
- HU-9106 (cambio de esencia al anclar): `inferida`
- HU-9107 (estereotipos anidados): `inferida`

## Evidencias funcionales ya confirmadas con fuerza

Capacidades con evidencia visual fuerte acumulada:

### Modelado Core
- creacion de objetos y procesos
- nombrado con auto-format
- panel `Draggable OPM Things`
- `OPD Navigator`
- panel `OPL`
- tabla de enlaces basica y avanzada
- halo contextual
- in-zoom
- objetos internos
- estados y atributos

### Navegacion y Gestion
- search de things en el modelo
- permisos de modelos
- settings OPL y settings generales
- versiones, archivados, search de modelos
- semi-fold
- templates
- ontology suggestion
- images in things
- system map
- requirement views
- OPD tree management (pantalla completa con Open/Cut/Remove/Rename)

### Validacion y Analisis
- methodology checking (regla "process must transform" visible)
- identification of missing knowledge (DistMult + R-GCN, confidence threshold, resultados en tabla)
- model informativity grading (TWINF, WINF, INF Avg, distribucion MFSP, sentencias con scores)
- bring links between selected entities (tooltip y multi-seleccion visibles)

### Import/Export e IA
- import CSV (atributos e instancias con valores visibles en modelo)
- generative AI requirements (Excel con REQ-ID, Category, Statement, Rationale)
- export XLSX de resultados de simulacion

### Simulacion y Ejecucion
- toolbar de simulacion completa (Play, Stop, step, speed slider, Headless Runner)
- simulacion conceptual con tokens
- condiciones y bucles (ramas con marcador "c", estados yes/no)
- objetos y procesos computacionales (notacion "()", aliases, unidades, valores)
- funciones definidas por usuario (IDE con JavaScript, notacion de punto para sub-partes)
- validacion de rangos ([0..100], (0..*) con notacion OPM)
- estereotipos OPM (notacion <<...>>, nodo Stereotypes)
- conexion ROS (boton #ROS, ventana TurtleSim ejecutandose)
- conexion MQTT (boton MQTT, Digital Twin "is the Digital Twin of")
- input de usuario en simulacion (agente "handles" proceso)
- configuracion de Bring Connected Things (defaults por tipo de enlace)

## Zonas de mayor sobreinferencia detectadas

Estas areas deberian degradarse a `video-confirmada`, `inferida` o `sobreinferida`:

### Criticas (sin evidencia directa)
- EP-70: 8 HU de sub-models siguen inferidas (lazy loading, sync polling, restricciones, desconexion, export) — pero las 5 core ya son frame-confirmada
- HU-8002: nombre incorrecto ("Pistol Reasoning" vs "DistMult Reasoning" real)

### Altas (politicas/reglas no visibles)
- reglas detalladas de exportacion PDF/OPL/share
- politicas de versionado y archivo
- comportamiento exacto de manual vs auto sizing
- reglas finas de images export por formato
- autosave por cambio de tab
- probabilidades ponderadas en simulacion (HU-8508)
- modo de validacion soft vs hard (HU-8605)
- configuracion detallada de mensajeria ROS (Topic/DataType/Message)
- pop-up de input durante simulacion (HU-8403)
- seleccion aleatoria de estado (HU-8503)

### Moderadas (plausibles pero no cerradas por frame)
- grid settings detallados (color, grosor, escala) — la grid como tal no se ve claramente activa en el frame
- operaciones de cortar/pegar modelo — el modal existe pero la accion en si no se ve
- dialogo de duplicacion de nombres — el video lo cubre pero el frame muestra unfold
- arrastrar OPDs en el arbol (HU-7405) — solo se ven botones, no drag-and-drop
- estereotipos organizacionales vs globales (HU-9102) — no se ve icono "G"
- desanclar estereotipos (HU-9104, 9105) — no visible

## Hallazgo no cubierto por el backlog

**New Model Wizard (12 etapas)**: el frame de Intro 39 muestra un wizard de creacion de modelos con:
- 12 etapas progresivas
- Stage 10: "Main Output" — pregunta por el output principal del sistema
- Pregunta si el output es tambien input
- Sentence builder: "The system [Select] the output"
- Botones Previous/Next/Cancel

Este wizard implementa el arranque metodologico del System Diagram que las HU NO cubren. Deberia tener su propia epica (EP propuesta: "Wizard de Creacion de Modelo SD") con ~12 HU (una por etapa). Esto cierra parcialmente la brecha del hallazgo global #4.

## Nuevas duplicaciones detectadas en bloques avanzados

| HU origen | HU destino | Solapamiento |
|-----------|-----------|-------------|
| HU-8705 (EP-87) | HU-9101 (EP-91) | anclar estereotipo — misma operacion descrita en dos epicas |
| HU-8803 (EP-88) | HU-8703 (EP-87) | IDE integrado — descrito en Objetos Computacionales y en Calculos Avanzados |
| HU-8305 (EP-83) | HU-8507 (EP-85) | boton Stop — descrito en MQTT y en Condiciones/Bucles |

## Matriz operativa por feature (S31-S49)

| Session | Feature | Epic | Total HU | frame-confirmada | video-confirmada | inferida | sobreinferida |
|---------|---------|------|----------|-----------------|-----------------|---------|---------------|
| S31 | Sub-Models | EP-70 | 16 | 5 | 3 | 8 | 0 |
| S32 | Bring Connected | EP-71 | 4 | 1 | 1 | 2 | 0 |
| S33 | Grid | EP-72 | 6 | 0 | 1 | 5 | 0 |
| S34 | Move Models | EP-73 | 4 | 0 | 4 | 0 | 0 |
| S35 | OPD Tree Mgmt | EP-74 | 8 | 6 | 1 | 1 | 0 |
| S36a | Duplication Names | EP-75 | 3 | 0 | 2 | 1 | 0 |
| S36b | Bring Links | EP-76 | 1 | 1 | 0 | 0 | 0 |
| S36c | Methodology Check | EP-77 | 6 | 2 | 4 | 0 | 0 |
| S37 | CSV Import | EP-78 | 6 | 1 | 1 | 4 | 0 |
| S38 | Gen AI Reqs | EP-79 | 5 | 2 | 2 | 1 | 0 |
| S39 | Missing Knowledge | EP-80 | 5 | 4 | 0 | 1 | 0 |
| S40 | Informativity | EP-81 | 5 | 5 | 0 | 0 | 0 |
| S41 | ROS | EP-82 | 7 | 2 | 2 | 3 | 0 |
| S42 | MQTT IoT | EP-83 | 5 | 2 | 2 | 1 | 0 |
| S43 | User Input | EP-84 | 4 | 1 | 1 | 2 | 0 |
| S44 | Conditions/Loops | EP-85 | 8 | 2 | 2 | 4 | 0 |
| S45 | Range Validation | EP-86 | 7 | 1 | 2 | 4 | 0 |
| S46 | Calc & Aliases | EP-87 | 5 | 4 | 1 | 0 | 0 |
| S47 | Computational | EP-88+89 | 7 | 1 | 3 | 3 | 0 |
| S48 | Conceptual Sim | EP-90 | 5 | 4 | 1 | 0 | 0 |
| S49 | Stereotypes | EP-91 | 7 | 1 | 1 | 5 | 0 |
| **TOTAL** | | | **122** | **45** | **34** | **43** | **0** |

### Distribucion S31-S49

- `frame-confirmada`: 45/122 (37%)
- `video-confirmada`: 34/122 (28%)
- `inferida`: 43/122 (35%)
- `sobreinferida`: 0/122 (0%) — eliminada tras revision Video 39

### Features mejor respaldadas por frame

1. EP-81 Model Informativity: 5/5 (100%)
2. EP-80 Missing Knowledge: 4/5 (80%)
3. EP-74 OPD Tree Management: 6/8 (75%)
4. EP-87 Calculos y Aliases: 4/5 (80%)
5. EP-90 Simulacion Conceptual: 4/5 (80%)

### Features mas debiles

1. EP-72 Grid: 0/6 frame-confirmada (0%)
2. EP-91 Stereotypes: 1/7 frame-confirmada (14%)
3. EP-86 Range Validation: 1/7 frame-confirmada (14%)
4. EP-70 Sub-Models: 5/16 frame-confirmada (31%) — mejorada significativamente

## Recomendaciones de normalizacion del backlog

### 1. Agregar metadatos de evidencia

Cada HU deberia incorporar:

- `fuente_principal`
- `video`
- `frame`
- `nivel_evidencia`
- `observado_o_inferido`

### 2. Separar capacidad de microinteraccion

Muchos items deberian consolidarse como:

- una HU principal por capacidad
- varios criterios de aceptacion por variante
- observaciones UX aparte

### 3. Separar funcionalidad de ejemplo/tutorial

Mantener fuera del backlog funcional:

- modelos ejemplo
- narrativas de tutorial
- contenidos del caso OnStar

### 4. Separar UI visible de regla de negocio

Especialmente en:

- permisos
- versionado
- ontologia
- requirements
- sub-models
- exportaciones

### 5. Reforzar backlog metodologico OPM

Faltan o estan poco visibles historias de nivel alto para:

- **wizard de creacion de System Diagram** (12 etapas, descubierto en frame de Intro 39)
- arranque del `System Diagram` (proposito, beneficiario, funcion)
- beneficiario
- atributo beneficiario
- funcion principal
- objeto principal
- habilitadores
- entorno
- consistencia semantica OPM

### 6. Crear epica para capacidad de Digital Twin

El frame de MQTT muestra una relacion OPL "is the Digital Twin of" que no tiene epica propia.

### 7. Reducir EP-70 (Sub-Models)

16 HU con 0 frame-confirmada es una señal clara. Propuesta:

- mantener 3-4 HU principales (crear, abrir, sincronizar, desconectar)
- mover las restricciones detalladas a criterios de aceptacion o a un documento de reglas de negocio
- verificar reglas contra la app real antes de mantenerlas

### 8. Corregir error factual

HU-8002 dice "Pistol Reasoning" — el nombre real visible en la app es "DistMult Reasoning".

## Matriz operativa maestra (543 HU)

Generada en: `/Users/felixsanhueza/Downloads/opcloud-matriz-operativa-maestra.csv`
Script generador: `/Users/felixsanhueza/Downloads/build_matrix.py`

### Revision completa de frames

La matriz fue recalibrada tras revision exhaustiva de los 183 frames (61 videos x 3 captures). Los 20 videos previamente no revisados (02, 03, 05, 11, 15, 17, 18, 20, 23, 25, 26, 30, 31, 32, 33, 35, 36, 37, 38, 39) fueron procesados frame por frame (25%, 50%, 75%), cruzando cada frame contra las HUs asignadas a esa sesion.

Cambios principales:
- EP-70 Sub-Models: 12 HU reclasificadas de `sobreinferida` a niveles reales (5 frame-confirmada, 3 video-confirmada, 8 inferida) gracias a Video 39 (Intro 38) que muestra dual-tab, OPL "SD1.1 is a view OPD, derived from SD1", "(read only)" en OPD tree
- S2 subio de weak a strong (main menu completo + Save Model dialog visible)
- S3 subio de moderate a strong (aggregation + tagged links visibles)
- S5 subio de moderate a strong (in-zoom con subprocesos paralelos)
- S15 bajo de strong a moderate (frames muestran canvas, no Settings UI)
- S20 bajo de strong a weak (frames muestran modelo, no link properties)
- S23 bajo de moderate a weak (frames muestran Model Chat, no ontologia)
- S25 subio de moderate a strong (Video 31 resize toolbar visible)
- S27 subio de moderate a strong (Video 34 requirements visibles)
- 60+ nuevos overrides especificos por HU con evidencia de frame

### Distribucion global por evidencia

| Nivel | Count | % |
|-------|-------|---|
| frame-confirmada | 255 | 47.0% |
| video-confirmada | 147 | 27.1% |
| inferida | 134 | 24.7% |
| sobreinferida | 0 | 0.0% |
| pendiente | 7 | 1.3% |

### Acciones recomendadas

| Accion | Count |
|--------|-------|
| mantener | 388 |
| agregar evidencia | 120 |
| verificar contra app o degradar | 14 |
| consolidar con HU duplicada | 11 |
| mover a artefacto tutorial | 7 |
| verificar contra app | 3 |

### HU con problemas detectados: 40

Tipos:
- 11 duplicaciones (5 pares + 1 parcial)
- 7 contaminacion tutorial (EP-32)
- 22 posible sobreinferencia de politica/regla

### Top 10 epicas con peor ratio frame-confirmada

| Epica | frame/total | ratio |
|-------|-------------|-------|
| EP-32 | 0/7 | 0% (tutorial, no funcional) |
| EP-40 | 0/4 | 0% (User Profile settings) |
| EP-51 | 0/3 | 0% (OPL export) |
| EP-52 | 0/4 | 0% (Image export) |
| EP-53 | 0/11 | 0% (PDF export) |
| EP-54 | 0/3 | 0% (Share link) |
| EP-60 | 0/7 | 0% (Ontology suggestions) |
| EP-61 | 0/6 | 0% (Ontology admin) |
| EP-72 | 0/6 | 0% (Grid) |
| EP-73 | 0/4 | 0% (Move models) |

### Columnas del CSV

- `HU`: identificador
- `Epica`: EP-xx
- `Epica_Titulo`: nombre descriptivo
- `Resumen`: titulo de la HU
- `Session`: tags Sxx del consolidado
- `Estado_Evidencia`: frame-confirmada / video-confirmada / inferida / sobreinferida / pendiente
- `Frame_Fuente`: nombre del frame que respalda la evidencia
- `Problema_Detectado`: duplicacion, contaminacion tutorial, sobreinferencia
- `Accion_Recomendada`: mantener / agregar evidencia / consolidar / degradar / verificar / mover

## Estado final

### Completo

- evaluacion global del documento
- resumen del marco OPM relevante
- evaluacion por bloques `S1-S10` (177 HU)
- evaluacion por bloques `S11-S20` (165 HU)
- evaluacion por bloques `S21-S30` (77 HU)
- evaluacion por bloques `S31-S40` (69 HU, cerrado)
- evaluacion por bloques `S41-S49` (55 HU, cerrado)
- matriz operativa por feature S31-S49
- **matriz operativa maestra completa** (543 HU, CSV generado)
- **revision exhaustiva de 183 frames** (61 videos x 3 captures, 20 videos revisados en detalle)
- **recalibracion de session strengths** basada en evidencia real (8 sesiones reclasificadas)
- **eliminacion de categoria sobreinferida** (EP-70 reclasificada con evidencia Video 39)

### Siguientes pasos recomendados

1. **Abrir la app** y verificar las 134 HU clasificadas como `inferida` — las que se confirmen suben a `frame-confirmada`, las que no se degradan o eliminan
2. **Consolidar las 11 HU duplicadas** eliminando la version redundante y manteniendo la mas completa
3. **Mover las 7 HU de EP-32** a un artefacto de tutorial separado
4. **Crear epica nueva para el New Model Wizard** (12 etapas, descubierto en frame Intro 39)
5. **Crear epica para Digital Twin** (relacion OPL "is the Digital Twin of", visible en MQTT)
6. **Reducir EP-70 Sub-Models** de 16 a ~8 principales, moviendo restricciones runtime (lazy loading, sync polling, restricciones) a criterios de aceptacion
7. **Reforzar backlog metodologico OPM** con historias de arranque del System Diagram usando el wizard como referencia
8. **Reconciliar mismatches session/video** documentados en hallazgo #6 — los tags S15, S20, S23, S25, S26, S30 no corresponden al contenido capturado en frames
9. **Agregar HU faltante para "Automatic Model Read Permission"** — feature visible en Video 30 sin HU en el consolidado
10. **Priorizar verificacion de EP-32, EP-40, EP-51-54, EP-60-61, EP-72, EP-73** — epicas con 0% de frame-confirmada que necesitan evidencia directa de la app
