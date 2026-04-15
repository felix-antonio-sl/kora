---
_manifest:
  urn: urn:fxsl:kb:opcloud-tutorial-visual-observations-p02
  provenance:
    created_by: kora/curator
    created_at: '2026-04-14'
    source: OPCloud Tutorial Videos (61 videos, 183 frames @ 25%/50%/75%)
version: 1.0.0
status: published
tags:
- opm
- opcloud
- tutorial
- observaciones-visuales
- opd
- iso-19450
lang: es
extensions:
  kora:
    family: observation
    depends_on:
    - urn:fxsl:kb:opd-es
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:fxsl:kb:opcloud-tutorial-visual-observations
---

# Observaciones visuales de los tutoriales OPCloud - Parte 02

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
| OBS-4 | Link-kind dialog filtra opciones segun kind de | 01, 22 | UX, no normativo |
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
| Computational process `` | 53, 54, 60 | Procesos con codigo JavaScript embedded |
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
