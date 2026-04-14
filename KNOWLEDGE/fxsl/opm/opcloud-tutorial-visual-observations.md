---
_manifest:
  urn: "urn:fxsl:kb:opcloud-tutorial-visual-observations"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-04-14"
    source: "OPCloud Tutorial Videos (61 videos, 183 frames @ 25%/50%/75%)"
version: "1.0.0"
status: published
tags: [opm, opcloud, tutorial, observaciones-visuales, opd, iso-19450]
lang: es
extensions:
  kora:
    family: observation
    depends_on:
      - "urn:fxsl:kb:opm-visual-es"
---

# Observaciones visuales de los tutoriales OPCloud

Descripcion sistematica de los diagramas OPM visibles en los 61 videos tutoriales oficiales de OPCloud (Technion). Cada video fue analizado en 3 frames (25%, 50%, 75% del timeline). El objetivo es extraer comportamientos visuales confirmados, reglas OPM demostradas, y observaciones nuevas no cubiertas por la gramatica visual existente.

Fuente: `/home/felix/_TEMP_BORRAR/frames-videos-opcloud/` (183 JPG frames).

---

## 1. Inventario de videos y contenido OPD

### 1.1 Videos con contenido OPD rico

| # | Video | Modelo | Niveles OPD | Features clave |
|---|---|---|---|---|
| 01 | Creating Things | Model (nuevo) | SD | Creacion de things, link-kind dialog |
| 03 | Basic Modeling | OnStar Example | SD | Agregacion, agent, instrument, effect, tagged link |
| 04 | Inzooming | OnStar Example | SD1 | Process in-zoom, thick contour, subprocesos placeholder |
| 05 | Inzooming Part 2 | OnStar Example | SD1 | Renombrado subprocesos, objetos internos |
| 06 | States | OnStar Example | SD1 | Estados en objeto, parallelismo, co-agents |
| 07 | Navigating | OnStar Example | SD, SD1 | Danger Status con estados, exhibition |
| 09 | Advanced Links | Model (nuevo) | SD | Gen-spec, XOR consumption, state-tagged links |
| 10 | OPL Pane Advanced | Turbojet Engine | SD1 | Alias, cardinality, exhibition elision |
| 15 | Objects Advanced | Turbojet Engine | SD, SD1, SD2 | In-zoom + unfold simultaneos, thick contour |
| 17 | Importing OPCAT | Schilling 23 | SD, SD1 | Modelo importado, range attributes |
| 18 | Key Shortcuts | OnStar Example | SD, SD1 | Navegacion in-zoom via teclado |
| 19 | OPD Tree Functions | Reverse Sensing | SD (4 niveles) | Multiplicity en agregacion, arbol profundo |
| 21 | Semi-Folding | Model (nuevo) | SD, SD1 | Semi-fold, "lists...as parts" vs "consists of" |
| 22 | Links Table | Model (nuevo) | SD | Link-kind dialogs, split input link pair |
| 24 | Links Properties | Model (nuevo) | SD | Multiplicity parametrica, probability, path, rate |
| 26 | OPD Tree Arrangement | Model (nuevo) | SD1 | Orden temporal automatico |
| 27 | Inner/Outer Validation | Model (nuevo) | SD1 | Validacion de frontera in-zoom |
| 28 | Organization Ontology | Model (nuevo) | SD | Ontologia organizacional, enforcement level |
| 29 | Templates | Model (nuevo) | SD, SD1 | Templates Private/Org/Global |
| 34 | OPM Requirements | Door Peephole | SD, SD1 | Requirements modeling, Reqt views |
| 36 | OPD Tree Navigation | Dishwasher | SD, SD1, SD2 | Environmental process, deep hierarchy |
| 37 | Images in Things | Model (nuevo) | SD | Imagenes embebidas, image pool |
| 39 | Sub Models | Main System | SD1, SD1.1 | View OPDs, sub-system model, read-only |
| 41 | Bring Connected | Model (nuevo) | SD1 | Filtro por tipo de link |
| 44 | OPD Tree Management | Dishwasher | Multiple | 6 niveles de profundidad |
| 45 | Name Duplication | Model (nuevo) | SD, SD2 | Chequeo de nombres duplicados |
| 46 | Bring Links Selected | OnStar Example | SD, SD1 | Links entre entidades seleccionadas |
| 47 | Methodology Checking | Methodology Check | SD, SD1 | Regla gerundio, regla transformacion |
| 48 | CSV Import | Model (nuevo) | SD | Exhibition, gen-spec desde CSV |
| 49 | AI Requirements | OnStar Example | SD1 | Gemini genera requirements desde OPL |
| 51 | OPM Stereotypes | Model (nuevo) | SD | Stereotypes con guillemets |
| 52 | Simulation Part 1 | OnStar Example | SD, SD1 | Simulacion conceptual |
| 53 | Simulation Part 2 | Model (nuevo) | SD | Simulacion computacional simple (5+10=15) |
| 54 | Simulation Part 3 | Model (nuevo) | SD | User-defined function, slope formula |
| 55 | Range Validation | Model (nuevo) | SD | Rangos [1..10], tipos, stereotype attributes |
| 56 | Simulation Part 4 | Model (nuevo) | SD1 | Condiciones (yes/no), loops, branching |
| 57 | Simulation Part 5 | Model (nuevo) | SD | User input durante simulacion |
| 58 | Simulation Part 6 | Light Power | SD1 | MQTT IoT, digital twin |
| 59 | Simulation Part 7 | Name Guessing | SD-SD1.2.1 | External URL API (nationalize.io) |
| 60 | Simulation Part 8 | Turtlesim ROS | SD-SD1.1.1 | ROS integration, robot control |
| 62 | Informativity Grading | N/A | N/A | MIL/MIA scoring, TWINF |
| 66 | Missing Knowledge | N/A | N/A | GNN/R-GCN link prediction |

### 1.2 Videos UI-only (sin OPD sustantivo)

| # | Video | Contenido |
|---|---|---|
| 02 | Main Menu | Menu hamburguesa, Save dialog |
| 08 | Styling and Text | Formateo visual, "State safe is final" |
| 11 | Exporting | OPL export, PDF preview |
| 12 | Permissions | Dialog de permisos por modelo |
| 13 | Advanced Loading | Load Model browser |
| 14 | OPCloud Settings | Pagina de configuracion |
| 16 | Things Searching | Dialog de busqueda cross-OPD |
| 20 | Tutorial Mode | Modo tutorial sobre OnStar SD |
| 23 | Model Chat | Chat colaborativo en tiempo real |
| 25 | Folders Handling | Navegacion de carpetas |
| 30 | Auto Permissions | Permisos automaticos por carpeta |
| 31 | Things Resizing | Resize manual/automatico |
| 32 | System Map | Thumbnails de OPD hierarchy |
| 33 | Export SVG | Export JPEG/SVG, scope OPD/Tree/SD |
| 35 | Export PDF | Export PDF con opciones avanzadas |
| 38 | Create New Model | Tabs multiples, modelo nuevo |
| 40 | New Model Wizard | Wizard de 12 pasos para SD canonico |
| 42 | Grid and Alignment | Grid snap, configuracion visual |
| 43 | Move Models | Mover modelos entre carpetas |

---

## 2. Modelos recurrentes

Cuatro modelos aparecen repetidamente como ejemplos canonicos:

### 2.1 OnStar Example (Driver Rescuing)

Modelo mas frecuente (videos 01-07, 11, 18, 20, 30, 46, 49, 52). SD + SD1.

**SD**: Driver (environmental, dashed) — Driver Rescuing (process) — OnStar System (aggregation: GPS, Cellular Network, VCIM, OnStar Console) — OnStar Advisor (agent) — Danger Status (states: endangered, safe).

**SD1 (Driver Rescuing in-zoomed)**: Subprocesos Call Making, Call Transmitting, Vehicle Location Calculating, Call Handling. Objetos internos: Call (states: requested, online), Vehicle Location. Externos: Driver, OnStar Advisor, GPS, Cellular Network, OnStar Console, VCIM.

### 2.2 Turbojet Engine System (MIT)

Videos 10, 15, 16. SD + SD1 (in-zoom) + SD2 (unfold).

Demuestra in-zoom y unfold simultaneos como siblings bajo SD. Alias extensivos (tes, hpt, hpc). Parametros computacionales con unidades (kPa, kJ). Autor: Hanan Kohen, MIT.

### 2.3 Automated Household Dish Caring (Dishwasher)

Videos 35, 36, 44. Jerarquia mas profunda: 6 niveles (SD → SD1 → SD1.1 → SD1.1.1 → SD1.2.1.1 → SD1.2.1.1.1 → SD1.2.1.1.1.1). Environmental process (Dishwasher Lifecycle Managing, dashed ellipse). Final state (Dish Set: clean unloaded is final).

### 2.4 Reverse Sensing System

Videos 19, 32. SD con 4 niveles de OPD tree. Environmental object (Object, dashed). Multiplicity "2" en triangulo de agregacion.

---

## 3. Observaciones detalladas por tema — primitivas y estados

### 3.1 Primitivas graficas y esencia

| Observacion | Videos | Regla V- confirmada |
|---|---|---|
| Objeto = rectangulo, proceso = elipse, estado = rountangle | 01, 03 | V-1 (implicita) |
| Contorno dashed = environmental (Driver, Object) | 03, 07, 19, 32, 46 | V-71 |
| Physical = sombra 3D desplazada (GPS, Cellular Network) | 03, 09, 23 | §1.3 |
| Informational = sin sombra (Danger Status, Call) | 05, 08 | §1.3 |
| Colores: verde (objeto), azul (proceso), no normativos | 01, 03, 52 | V-63 |

### 3.2 Estados de objeto

| Observacion | Videos | Regla V- confirmada |
|---|---|---|
| Estados como rountangles dentro del rectangulo del objeto | 06, 07, 09 | §2.1 |
| Final state (Dish Set: "clean unloaded is final") | 36 | V-6 |
| Initial state (OPL: "State safe is final") | 08 | V-6 |
| Valores numericos como estados (Temperature: value, Object 1: 5) | 10, 53 | §2.3 |
| Rangos como estados ([0..100], [1..10],[20..30], {0..*}) | 55 | §2.3 |
| Tipo de dato como estado enumerado (int, float, string, char, boolean) | 55 | §2.3 extension |

## 3b. Observaciones detalladas — enlaces

### 3.3 Enlaces procedimentales

| Observacion | Videos | Regla V- confirmada |
|---|---|---|
| Effect link bidireccional (Driver Rescuing affects Driver) | 02, 03 | §3.1 |
| Agent link con lollipop negro (OnStar Advisor handles) | 03, 04, 19 | §3.3 |
| Instrument link (Driver Rescuing requires OnStar System) | 03, 10 | §3.3 |
| Consumption link (Salad Making consumes Tomato) | 09, 42 | §3.1 |
| Result link (A Processing yields Object 2) | 09, 42, 53 | §3.1 |
| Co-agents (Driver AND OnStar Advisor handle Call Handling) | 06 | V-14 (AND implicito) |
| XOR consumption (Salad Making consumes exactly one of...) | 09 | §5.2 |
| State-tagged links (Driving "to garden", "to work") | 09 | §3.2 |
| Split Input Link Pair (en link-kind dialog) | 22 | V-40 |
| Event modifier "e" y condition modifier "c" | 56 | §4.1, §4.2 |
| Invocation link (zigzag) no observado directamente | — | §9.1 |

### 3.4 Enlaces estructurales

| Observacion | Videos | Regla V- confirmada |
|---|---|---|
| Agregacion-participacion (triangulo negro solido) | 03, 10, 19, 45 | §8.2 |
| Exhibition-caracterizacion (Driver exhibits Danger Status) | 07, 08, 48 | §8.2 |
| Generalizacion-especializacion (Car → Porsche, SUV) | 09 | §8.2 |
| Clasificacion-instanciacion (CSV import crea instancias) | 48 | §8.2 |
| Tagged structural link ("communicates via", "controls") | 03, 07, 24 | §8.1 |
| Multiplicidad en agregacion ("2" junto al triangulo) | 10, 19 | V-22 |
| Multiplicidad parametrica ("2..3*(n=4)" en tagged link) | 24 | §7.2 |
| Herencia multiple no observada directamente | — | V-28 |

## 3c. Observaciones detalladas — refinamiento y contexto

### 3.5 Refinamiento: In-zooming

| Observacion | Videos | Regla V- confirmada |
|---|---|---|
| Thick contour en proceso refinado (elipse agrandada) | 04, 15, 18 | V-33, V-34 |
| Thick contour en objeto refinado (unfold) | 15 | V-33, V-69 |
| Subprocesos placeholder (B Processing, C Processing, D Processing) | 04 | R-OC-1 |
| Orden temporal top-to-bottom (OPL: "time sequence") | 04, 05, 26 | V-31, V-35 |
| Parallelismo por misma Y (OPL: "parallel C Processing and D Processing") | 06 | V-32 |
| Objetos internos ("as well as Call and Vehicle Location") | 04, 05 | R-OC-2 |
| Externos copiados en OPD hijo (Driver, OnStar System en SD1) | 04, 46 | V-80, V-81 |
| Environmental persiste en hijo (Driver dashed en SD1) | 04, 18, 46 | V-71 |
| Agent link al contorno del container (OnStar Advisor → Driver Rescuing) | 04, 52 | V-36 |
| Instrument link al contorno del container | 04, 52 | V-36 |

### 3.6 Refinamiento: Unfolding

| Observacion | Videos | Regla V- confirmada |
|---|---|---|
| Thick contour en objeto unfolded (Turbojet Engine System en SD2) | 15 | V-33, V-69 |
| Unfold revela partes via agregacion | 15, 21, 45 | §10.2 |
| In-zoom y unfold como siblings bajo SD (SD1+SD2 en Turbojet) | 15 | Confirmado |
| Part-unfolding OPL: "from SD part-unfolds in SD1 into..." | 41, 45 | Extension OPL |
| Specialization-unfolding OPL: "from SD specializes in..." | 41 | Extension OPL |

### 3.7 Semi-Folding

| Observacion | Videos | Regla V- confirmada |
|---|---|---|
| Semi-fold: triangulos pequeños con nombre dentro del rectangulo parent | 21 | R-SF-1 |
| OPL: "lists X and Y as parts" para semi-folded | 21 | R-SF-5 |
| OPL: "consists of Z and two more parts" para extraidos | 21 | R-SF-5 |
| Indicador numerico "2" = parts ocultos, no total | 21 | R-SF-7 |
| Links procedimentales apuntan a parts semi-folded dentro del parent | 21 (75%) | R-SF-6, R-SF-9 |
| Semi-fold parcial: algunos parts dentro, otros fuera | 21 (50%) | R-SF-8 |

### 3.8 Container / Internal-External

| Observacion | Videos | Regla V- confirmada |
|---|---|---|
| Validacion: "external thing should not overlap in-zoomed thing" | 27 | V-83 |
| Insertar interno: arrastrar desde Draggable OPM Things panel | 27 | V-79 |
| Externos mantienen propiedades (contorno, esencia) en OPD hijo | 04, 18, 46 | V-80 |
| Objetos internos creados dentro de in-zoom (Call, Vehicle Location) | 04, 05 | V-84 |
| Remove dialog: "remove appearance" vs "remove from entire model" | 06 | Appearance vs existence |

### 3.9 OPD Tree y navegacion

| Observacion | Videos | Regla V- confirmada |
|---|---|---|
| Etiquetado SD → SD1 → SD1.1 → SD1.1.1 | 04, 15, 19, 44 | V-46 |
| Jerarquia mas profunda observada: 6 niveles (Dishwasher) | 44 | §15 |
| In-zoom y unfold producen siblings (SD1 + SD2) | 15 | V-113, V-114 |
| View OPDs (Sub System Model View, "derived from SD1") | 39 | V-114 |
| Read-only OPDs dentro de sub-model views | 39 | Extension OPCloud |
| System Map: thumbnails de toda la jerarquia con flechas | 32 | Extension OPCloud |
| OPD Tree Management: Cut, Remove, Rename de nodos | 44 | V-113 |
| "OPD Tree Processes Arrangement: Automatic" en settings | 26 | Extension OPCloud |

## 3d. Observaciones detalladas — simulacion, validacion y extensiones

### 3.10 Simulacion y ejecucion

| Observacion | Videos | Regla V- confirmada |
|---|---|---|
| Toolbar de simulacion: play, step, XLSX, headless | 52, 53 | V-53 (implicita) |
| Proceso computacional: notacion "()" despues del nombre | 53, 54, 60 | Extension OPCloud |
| Valores numericos en estados durante simulacion (5, 10, 15) | 53 | V-54 |
| User-defined function: JavaScript en editor (return formula) | 54, 57 | Extension OPCloud |
| Alias en formulas: dot notation (p1.x, p2.y) | 54 | Extension OPCloud |
| Condicion booleana: Object con estados yes/no → branching | 56 | V-39 |
| User input durante simulacion: variable userInput en JS | 57 | Extension OPCloud |
| MQTT connection: IoT sensor → simulacion | 58 | Extension OPCloud |
| External URL: HTTP API call (nationalize.io) durante simulacion | 59 | Extension OPCloud |
| ROS integration: control de robot via OPM simulation | 60 | Extension OPCloud |
| Digital Twin: OPL "is the Digital Twin of" | 58 | Extension OPCloud |
| aliasArr JSON structure: binding de aliases a variables JS | 59 | Extension OPCloud |

### 3.11 Validacion y metodologia

| Observacion | Videos | Regla V- confirmada |
|---|---|---|
| Regla gerundio: "process should end with -ing" | 47 | V-47 (naming) |
| Regla transformacion: "process must transform at least one object" | 47 | V-5, V-7 (implicita) |
| Organization Ontology: enforcement level Suggest/Enforce | 28 | Extension OPCloud |
| Name duplication check: impide nombres duplicados | 45 | V-47 |
| Model Informativity Grading (MIL/MIA): TWINF score | 62 | Extension OPCloud |
| Missing Knowledge: GNN/R-GCN link prediction | 66 | Extension OPCloud |

### 3.12 Stereotypes y templates

| Observacion | Videos | Regla V- confirmada |
|---|---|---|
| Stereotype: notacion guillemet como prefijo en nombre | 51, 54, 55 | Extension OPCloud |
| Stereotype agrega atributos automaticamente (Cost, Dimension Set) | 51, 55 | Extension OPCloud |
| Templates: scope Private/Organizational/Global | 29 | Extension OPCloud |
| Images Pool: imagenes embebidas en things | 37 | Extension OPCloud |

---

## 4. Reglas visuales confirmadas (cross-ref a opm-visual-es.md v1.2.0)

### 4.1 Primitivas (§1)

| Regla | Confirmacion |
|---|---|
| V-1 (defaults informacional+sistemico) | Videos 01, 31 ("informatical and systemic") |
| V-3 (vertice triangulo → refinable) | Videos 03, 10, 19, 45 |
| V-63 (colores informativos) | Verde=objeto, azul=proceso en todos los videos |
| V-69 (thick contour in-zoom Y unfold) | Video 15: SD1 (in-zoom) y SD2 (unfold) ambos thick |
| V-70 (in-diagram no thick) | Video 21: unfold en mismo OPD no produce thick |
| V-71 (contorno persiste cross-nivel) | Videos 04, 18, 46: Driver dashed en SD y SD1 |

### 4.2 Estados (§2)

| Regla | Confirmacion |
|---|---|
| V-4 (estado no existe fuera de objeto) | Todos los videos: estados siempre dentro |
| V-6 (max 1 default, multiples initial/final) | Video 36: "State clean unloaded is final" |

### 4.3 Enlaces procedimentales (§3)

| Regla | Confirmacion |
|---|---|
| V-7 (effect requiere objeto con estado) | Video 03: Driver Rescuing affects Driver (Danger Status tiene estados) |
| V-11 (unicidad de rol) | Nunca se observo un objeto como transformado Y habilitador simultaneamente |
| V-14 (AND implicito) | Video 06: co-agents sin arco conector |

### 4.4 Operadores logicos (§5)

| Regla | Confirmacion |
|---|---|
| V-15 (XOR/OR a todas las familias) | Video 09: XOR en consumption |
| V-18 (probabilistico = XOR) | No observado |

### 4.5 Multiplicidad (§7)

| Regla | Confirmacion |
|---|---|
| V-21 (parametros unicos) | Video 24: n=4 en formula de multiplicidad |
| V-22 (anotacion junto al extremo) | Videos 10, 19: "2" junto al triangulo |

### 4.6 Herencia (§8.4)

| Regla | Confirmacion |
|---|---|
| V-28 (herencia multiple) | No observada |
| V-29 (atributo discriminante) | No observado |

### 4.7 Invocacion (§9)

| Regla | Confirmacion |
|---|---|
| V-31 (posicion vertical = secuencia) | Videos 04, 05, 06, 26, 36 |
| V-32 (misma altura = paralelo) | Video 06: "parallel Call Transmitting and Vehicle Location Calculating" |
| V-77 (solo process in-zoom) | Videos 15, 21: object in-zoom/unfold sin orden temporal |
| V-59 (activacion asincronica) | No observada |

### 4.8 Refinamiento (§10)

| Regla | Confirmacion |
|---|---|
| V-33 (thick contour padre e hijo) | Videos 04, 15, 18 |
| V-34 (elipse agrandada) | Videos 04, 05, 06 |
| V-62 (in-zoom en dos fases) | Observacion implicita |
| V-79 (container en OPD hijo) | Videos 04, 27 |
| V-80 (externos copiados) | Videos 04, 46 |
| V-83 (no refinar externo) | Video 27: validacion explicita |
| V-87 (supresion solo in-zoom) | No observable directamente |
| V-95-97 (invariantes cross-nivel) | Driver mantiene nombre/esencia en todos los niveles |
| V-100 (ciclo prohibido) | No observable (prevencion silenciosa) |

### 4.9 Distribucion de enlaces (§11)

| Regla | Confirmacion |
|---|---|
| V-36 (agent/instrument al contorno se distribuyen) | Videos 04, 52 |
| V-37 (consumption/result NO al contorno) | Consistente: nunca observado |
| V-107 (distribucion solo in-zoom) | Consistente: unfold no muestra distribucion |

### 4.10 Precedencia (§13)

| Regla | Confirmacion |
|---|---|
| V-43 (result+consumption invalido) | No testeado explicitamente |
| V-44 (transformador > habilitador) | Consistente |

### 4.11 OPD Tree (§15)

| Regla | Confirmacion |
|---|---|
| V-46 (SD contiene 1 proceso sistemico) | Todos los modelos |
| V-113 (solo hojas eliminables) | Video 44: OPD Tree Management |
| V-114 (View OPDs) | Video 39: "SD1.1 is a view OPD, derived from SD1" |

---

## 5. Observaciones nuevas (no cubiertas en opm-visual-es.md v1.2.0)

### 5.1 Comportamientos OPCloud confirmados

| ID | Observacion | Video | Impacto |
|---|---|---|---|
| OBS-1 | In-zoom auto-crea 3 subprocesos placeholder con nombres genericos (B/C/D Processing) | 04 | UX, no normativo |
| OBS-2 | OPL in-zoom sentence incluye objetos internos: "as well as [objects]" | 04, 05 | Confirmacion de R-OC-2 |
| OBS-3 | OPL parallelismo por Y: "parallel X and Y" | 06 | Confirmacion de R-OC-7 |
| OBS-4 | Link-kind dialog filtra opciones segun kind de source/target | 01, 22 | UX, no normativo |
| OBS-5 | "Remove appearance" vs "remove from entire model" distingue existencia de vista | 06 | Confirma V-52, V-101 |
| OBS-6 | Validacion de frontera: "external thing should not overlap in-zoomed thing" | 27 | Confirma V-83 |
| OBS-7 | Semi-fold OPL: "lists...as parts" vs "consists of...and N more parts" | 21 | Confirma R-SF-5 |
| OBS-8 | Links procedimentales pueden apuntar a parts semi-folded dentro del parent | 21 (75%) | Confirma R-SF-6 |
| OBS-9 | View OPDs explicitamente declarados en OPL: "SD1.1 is a view OPD, derived from SD1" | 39 | Confirma V-114, extiende con sintaxis OPL |
| OBS-10 | Read-only OPDs dentro de sub-model views | 39 | Extension no cubierta |
| OBS-11 | Part-unfolding syntax: "from SD part-unfolds in SD1 into..." | 41, 45 | Extension OPL no cubierta |
| OBS-12 | Specialization-unfolding syntax: "from SD specializes in..." | 41 | Extension OPL no cubierta |

### 5.2 Features OPCloud sin base ISO 19450

| Feature | Video | Descripcion |
|---|---|---|
| Stereotypes (notacion guillemet) | 51, 54, 55 | Templates de propiedades reutilizables con prefijo en nombre |
| Computational process `()` | 53, 54, 60 | Procesos con codigo JavaScript embedded |
| Digital Twin relationship | 58 | OPL: "is the Digital Twin of" |
| Generative AI requirements | 49 | Gemini genera requirements "shall" desde OPL |
| MIL/MIA Informativity | 62 | Scoring de informatividad del modelo |
| GNN Missing Knowledge | 66 | R-GCN link prediction en knowledge graph |
| MQTT/ROS/URL integration | 58, 59, 60 | Simulacion conectada a sistemas externos |
| Organization Ontology | 28 | Vocabulario controlado organizacional |
| System Map | 32 | Vista panoramica de jerarquia OPD |
| Model Chat | 23 | Colaboracion en tiempo real |
| Methodology Checking | 47 | Validacion de reglas OPM |

### 5.3 Patrones de modelado observados

| Patron | Ejemplo | Videos |
|---|---|---|
| SD canonico (System, Handler, Tool Set, Process, I/O, Beneficiary) | OPM Example Model template | 33, 40, 47 |
| In-zoom + unfold como siblings (SD1 + SD2) | Turbojet Engine | 15 |
| Environmental process (dashed ellipse) | Dishwasher Lifecycle Managing | 36 |
| Parametric objects con alias y unidades | Turbojet Engine ([kPa], [kJ]) | 10, 15 |
| Condition branching via boolean object (yes/no states) | Simulacion Part 4 | 56 |
| Co-agents (multiple agents handle same process) | OnStar: Driver AND OnStar Advisor | 06 |
| Attribute values via classification-instantiation | CSV import | 48 |

---

## 6. Cobertura de modelos por niveles de refinamiento

| Profundidad | Modelo | Videos |
|---|---|---|
| 1 nivel (SD only) | Model nuevo, OnStar SD | 01, 02, 03, 09, 53 |
| 2 niveles (SD + SD1) | OnStar, Model nuevo | 04-06, 18, 21, 26, 52 |
| 3 niveles (SD + SD1 + SD1.1) | Turbojet, Reverse Sensing | 10, 15, 19, 59 |
| 4 niveles | Name Guessing, Turtlesim ROS | 59, 60 |
| 5 niveles | Dishwasher | 36, 44 |
| 6 niveles | Dishwasher (SD1.2.1.1.1.1) | 44 |

---

## 7. Resumen estadistico

| Metrica | Valor |
|---|---|
| Videos analizados | 61 |
| Frames procesados | 183 |
| Videos con OPD sustantivo | 42 |
| Videos UI-only | 19 |
| Modelos unicos observados | ~15 |
| Profundidad maxima OPD | 6 niveles |
| Reglas V- confirmadas | 38/114 |
| Observaciones nuevas | 12 |
| Features OPCloud sin base ISO | 11 |
