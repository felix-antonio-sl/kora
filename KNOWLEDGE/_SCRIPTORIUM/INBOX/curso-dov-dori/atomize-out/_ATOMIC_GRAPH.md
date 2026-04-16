# MBSE con OPM — Curso Dov Dori
<!-- /atomize · 152 proposiciones · 118 entidades · 5 archivos · 2026-04-06 -->
<!-- Consultar: buscar por [P###], por tipo (REQUISITO, DEFINICIÓN, REGLA...), o por entidad -->

## Parte 1 — Fundamentos OPM

### Introducción y contexto (01-02)
- [P001] **DEFINICIÓN** — MBSE: metodología moderna donde modelos conceptuales formales son referencia autoritativa para ingeniería de sistemas complejos
- [P002] **DEFINICIÓN** — OPM: metodología y lenguaje de modelado conceptual para MBSE, reconocido como → `ISO 19450`
- [P003] **HECHO** — OPM inventado por Dov Dori, profesor en → `Technion` y → `MIT`
- [P004] **HECHO** — empresas que usan OPM: Whirlpool (diseño electrodomésticos), fabricantes aeronaves, industria automotriz, robótica ISS, seguros, biología molecular
- [P005] **REGLA** — modelo conceptual es paso temprano necesario para desarrollar cualquier sistema complejo
- [P006] **DEFINICIÓN** — OPM usa mínimo de elementos: 2 tipos de things (objects/processes) + links para conectarlos

### Objects (03)
- [P007] **DEFINICIÓN** — object: thing que existe o puede existir física o informaticalmente
- [P008] **REGLA** — objects representados por rectángulos con borde verde
- [P009] **REGLA** — physical objects = rectángulo sombreado; informatical objects = rectángulo plano sin sombreado
- [P010] **REGLA** — personas también clasificadas como objects en OPM
- [P011] **REGLA** — information items clasificados como informatical objects

### Processes (04)
- [P012] **DEFINICIÓN** — process: thing que transforma objects creándolos, consumiéndolos o cambiando su estado
- [P013] **REGLA** — processes representados por elipses con borde azul
- [P014] **REGLA** — physical processes = elipse sombreada; informatical processes = elipse plana

### States (05)
- [P015] **DEFINICIÓN** — state: situación o posición posible en que un object puede estar por algún tiempo
- [P016] **REGLA** — states representados por "roundtangles" (rectángulos esquinas redondeadas) dentro del object
- [P017] **REGLA** — state solo existe gráficamente dentro del object box; sin significado fuera
- [P018] **REGLA** — object stateful puede estar en ≤1 state a la vez; si process lo transforma, está en transición entre input state y output state
- [P019] **REGLA** — modelar object como stateful/stateless depende del contexto del sistema

### Relations between Things (06)
- [P020] **DEFINICIÓN** — aggregation-participation (whole-part): relación estructural donde whole agrega ≥1 parts
- [P021] **REGLA** — aggregation-participation link = línea con triángulo negro; conecta objects con objects O processes con processes
- [P022] **EXCLUSIÓN** — aggregation-participation no conecta objects con processes; object no puede componerse de processes ni viceversa
- [P023] **HECHO** — OPCloud: software cloud dedicado para construir modelos OPM colaborativamente

### Object creation and consumption (07)
- [P024] **DEFINICIÓN** — transformation: lo que un process hace a un object; 3 tipos: consumption, creation, change (state transition)
- [P025] **REGLA** — consumption link = flecha desde consumed object → process
- [P026] **REGLA** — result link = flecha desde creating process → resulting object
- [P027] **REGLA** — effect link = flechas bidireccionales entre affecting process y affected object (cambio de estado)

### State transition (08)
- [P028] **DEFINICIÓN** — input-output link pair: par de links desde input state → process y desde process → output state
- [P029] **REGLA** — state transition modela cambio de estado de object mediante process conectado con in-out link pair

### System aspects (09)
- [P030] **DEFINICIÓN** — structure (what): colección de components y relaciones estáticas time-independent entre ellos
- [P031] **DEFINICIÓN** — behavior (how): dinámica del sistema; processes/sub-processes y relaciones time-dependent con objects transformados
- [P032] **DEFINICIÓN** — function (what for/why): combinación de main object + main process; en sistemas artificiales provee beneficio al beneficiary
- [P033] **DEFINICIÓN** — main object (operand/transformee): object transformado por el sistema
- [P034] **DEFINICIÓN** — main process: process que transforma el main object
- [P035] **REGLA** — system architecture = combinación de structure + behavior que hace posible la function

### Object-Process Language (10)
- [P036] **DEFINICIÓN** — OPD (Object-Process Diagram): modalidad gráfica de OPM
- [P037] **DEFINICIÓN** — OPL (Object-Process Language): modalidad textual de OPM; subconjunto de inglés natural
- [P038] **REGLA** — Graphics-Text Equivalence Principle: todo hecho modelado en OPD se expresa también en OPL y viceversa
- [P039] **REGLA** — en OPD: processes = texto azul; objects = texto verde; states = color gold-brown
- [P040] **HECHO** — redundancia visual/verbal beneficiosa: humanos procesan información verbal y visual por canales separados con capacidad limitada (multimedia learning)

### Resumen Parte 1 (11)
- [P041] **REGLA** — OPM domain-independent: puede modelar sistemas de cualquier dominio
- [P042] **REGLA** — links aprendidos Parte 1: aggregation-participation (structural) + transforming links (consumption, creation, state change)
- [P043] **REGLA** — every system tiene 3 aspectos: structure, behavior, function; combination structure+behavior = function

## Parte 2 — System Diagram (SD)

### Top level of model
- [P044] **DEFINICIÓN** — SD (System Diagram): primer OPD; vista top-level bird's-eye del sistema
- [P045] **REQUISITO** — SD debe ser simple/claro con mínimos detalles técnicos
- [P046] **REGLA** — SD tiene 5 componentes: purpose, function, enablers, environment, problem occurrence

### System purpose
- [P047] **DEFINICIÓN** — system purpose: beneficio clave que sistema artificial provee a sus beneficiaries
- [P048] **DEFINICIÓN** — beneficiary: stakeholder que extrae valor y beneficio del sistema
- [P049] **DEFINICIÓN** — beneficiary attribute: atributo informatical del beneficiary group cuyo valor cambia beneficiándolo
- [P050] **DEFINICIÓN** — exhibition-characterization link: relación estructural entre thing y su attribute; línea con triángulo blanco-negro
- [P051] **REGLA** — en sistemas naturales: outcome reemplaza purpose (no diseñados por humanos)
- [P052] **REGLA** — OPM convention: object names deben ser singular; humanos → agregar "Group"; inanimados → agregar "Set"

### Main function of System
- [P053] **DEFINICIÓN** — system function = par {transformee + process que lo transforma}; function entrega purpose a beneficiaries
- [P054] **DEFINICIÓN** — transformee (operand): object que sufre transformación
- [P055] **DEFINICIÓN** — benefit-providing object: main object afectado por main process directa/indirectamente via atributos
- [P056] **DEFINICIÓN** — benefit-providing attribute: atributo del benefit-providing object transformado por main process
- [P057] **REGLA** — function name = object name + process name (ej: "Airplane Flying")
- [P058] **REGLA** — main process puede conectarse a >1 transformee; function incluye solo benefit-providing object

### Process enablers
- [P059] **DEFINICIÓN** — enabler: object requerido para que process ocurra; no transformado por el process
- [P060] **DEFINICIÓN** — agent: enabler humano; goal-oriented con inteligencia natural
- [P061] **DEFINICIÓN** — instrument: enabler no-humano, usualmente inanimado
- [P062] **REGLA** — agent link = línea con círculo negro al extremo del process ("black lollipop")
- [P063] **REGLA** — instrument link = línea con círculo vacío al extremo del process ("white lollipop")
- [P064] **REGLA** — instrument default del sistema = nombre de function/main process + "System"
- [P065] **REGLA** — enablers no son transformados por el process que habilitan

### System boundary and environment
- [P066] **DEFINICIÓN** — thing affiliation: atributo que especifica si thing es systemic (parte del sistema) o environmental
- [P067] **DEFINICIÓN** — system boundary: borde imaginario que separa things systemic de environmental
- [P068] **REGLA** — systemic things = contorno sólido; environmental things = contorno punteado (dashed)
- [P069] **REGLA** — environmental things afectan operación del sistema pero están fuera del control del diseñador

### Problem occurrence
- [P070] **REGLA** — problem occurrence = imagen espejo de system purpose + main function
- [P071] **REGLA** — process ambiental causa que beneficiary attribute esté en estado negativo y benefit-providing attribute en estado problemático

## Parte 3 — Refinamiento SD1

### Process refinement
- [P072] **DEFINICIÓN** — SD1: OPD descendiente de SD donde main process se refina exponiendo sub-processes y objects asociados
- [P073] **DEFINICIÓN** — synchronous process: process cuyos sub-processes ocurren en orden fijo predefinido
- [P074] **DEFINICIÓN** — asynchronous process: process cuyos sub-processes no tienen orden fijo; pueden ocurrir en paralelo/cualquier secuencia
- [P075] **REGLA** — Detail Hierarchy OPM Principle: cuando OPD se vuelve difícil de comprender por exceso de detalle, crear nuevo OPD descendiente

### Synchronous process refinement
- [P076] **REGLA** — refinamiento synchronous = in-zooming: process inflado con sub-processes ordenados verticalmente dentro
- [P077] **REGLA** — Timeline OPM Principle: dentro de in-zoomed process, timeline va de arriba (primero) a abajo (último)
- [P078] **REGLA** — aggregation-participation en in-zoom se expresa por containment (sub-processes dentro del process), no por link explícito

### Modelling principles
- [P079] **REGLA** — Procedural Link Uniqueness Principle: en cualquier nivel de detalle, process y object/state conectados por ≤1 procedural link único
- [P080] **REGLA** — evitar modelar mismo model fact en >1 OPD salvo que agregue comprensión
- [P081] **REGLA** — en SD usar effect link cuando SD1 ya detalla state transitions específicos

### Asynchronous process refinement
- [P082] **REGLA** — refinamiento asynchronous = unfolding: sub-processes fuera del main process, conectados con structural links
- [P083] **DEFINICIÓN** — generalization-specialization: relación entre thing general y sus sub-types (ej: vehicle → car, truck)
- [P084] **REGLA** — generalization-specialization link = línea con triángulo hueco apuntando al general
- [P085] **REGLA** — usar aggregation-participation si sub-processes son parts del whole; generalization-specialization si son tipos/especializaciones

### Object refinement
- [P086] **REGLA** — objects se refinan por unfolding mostrando parts y attributes en OPD separado ("object tree")
- [P087] **REGLA** — state suppression: ocultar states no vinculados a ningún process en un OPD; pseudo-state (3 dots) indica states ocultos
- [P088] **DEFINICIÓN** — emergence: aparición de capacidad/funcionalidad que caracteriza al sistema completo pero no a ninguna de sus partes individualmente
- [P089] **REGLA** — system architecture = combinación structure+behavior que da origen a emergence → `function`

### Objects y processes como features
- [P090] **DEFINICIÓN** — feature: thing que caracteriza otro thing (el exhibitor); generaliza attribute y operation
- [P091] **DEFINICIÓN** — attribute: feature que es object (informatical, describe al exhibitor)
- [P092] **DEFINICIÓN** — operation: feature que es process (lo que el object hace/puede hacer); equivalente a "method" en programación
- [P093] **REGLA** — exhibition-characterization es el único structural link que conecta objects con processes
- [P094] **REGLA** — attributes siempre informatical; operations pueden ser physical o informatical

## Parte 4 — Sistemas naturales, sociales y recapitulación

### SD de sistema natural — Rainstorm (SD1)
- [P095] **REGLA** — SD sistema natural comparte 3 componentes con artificial: function, enablers, environment; pero purpose/problem occurrence usualmente no aplican
- [P096] **REGLA** — en sistema natural: outcome reemplaza purpose; puede ser beneficioso o detrimental
- [P097] **REGLA** — sistemas naturales sin participación humana no tienen agents
- [P098] **REGLA** — thing systemic puede ser part de thing environmental

### SD de sistema social — Conference (SD2)
- [P099] **REGLA** — sistema social es artificial como tecnológico; SD involucra mismos 5 componentes
- [P100] **DEFINICIÓN** — stakeholder/stakeholder group: individuo, organización o grupo con interés en o afectado por un sistema

### SD de sistema socio-técnico — Social Network (SD3)
- [P101] **DEFINICIÓN** — socio-technical system: sistema artificial que integra aspectos tecnológicos y sociales
- [P102] **DEFINICIÓN** — tagged structural link: link estructural con tag describiendo naturaleza de la relación; OPL = concatenación source + tag + destination
- [P103] **REGLA** — tagged structural link se usa cuando ninguna relación estructural fundamental es apropiada

### Recapitulación curso
- [P104] **HECHO** — Dov Dori = inventor OPM, profesor → `Technion` e → `MIT`
- [P105] **HECHO** — equipo curso: Dr. Rea Lavi (diseño instruccional), Kave Shafran (media), Dr. Niva Wengrowicz y Dr. Ahmad Jbara (versiones hebreo/árabe)
- [P106] **REGLA** — OPM altamente expresivo pero compacto; facilita comunicación entre todos stakeholders

## Guía de Implementación OPM (Wizard)

### Workflow del wizard SD
- [P107] **REGLA** — paso 1 wizard: determinar main process (nombre en gerundio "-ing")
- [P108] **REGLA** — paso 2: identificar beneficiary group (singular + "Group" para humanos)
- [P109] **REGLA** — paso 3: definir beneficiary attribute con input state (current) y output state (desired)
- [P110] **REGLA** — paso 4: determinar si beneficiary = agent del main process
- [P111] **REGLA** — paso 5: nombrar system (default = main process name + "System")
- [P112] **REGLA** — paso 6: identificar instruments requeridos (singular; "Set" para inanimados)
- [P113] **REGLA** — paso 7: definir inputs (objects consumed por process)
- [P114] **REGLA** — paso 8: definir outputs (objects created/affected/changed)
- [P115] **REGLA** — paso 9: marcar environmental objects (externos al sistema)

### Taxonomía OPM completa (resumen transversal)

#### Things
- [P116] **DEFINICIÓN** — thing: elemento fundamental OPM; specializes en object y process
- [P117] **DEFINICIÓN** — object: thing que existe; puede ser physical (sombreado) o informatical (plano)
- [P118] **DEFINICIÓN** — process: thing que transforma objects; physical (sombreado) o informatical (plano)
- [P119] **DEFINICIÓN** — state: situación posible de object; representado como roundtangle dentro del object
- [P120] **DEFINICIÓN** — feature: thing que caracteriza otro thing; specializes en attribute (object) y operation (process)

#### Structural links
- [P121] **DEFINICIÓN** — aggregation-participation: whole-part; triángulo negro; objects↔objects O processes↔processes
- [P122] **DEFINICIÓN** — exhibition-characterization: thing↔feature; triángulo blanco-negro; único structural link object↔process
- [P123] **DEFINICIÓN** — generalization-specialization: general↔sub-types; triángulo hueco
- [P124] **DEFINICIÓN** — tagged structural link: relación user-defined con tag textual

#### Procedural links (transforming)
- [P125] **DEFINICIÓN** — consumption link: flecha object → process (consumee → consumer)
- [P126] **DEFINICIÓN** — result link: flecha process → object (creator → resultee)
- [P127] **DEFINICIÓN** — effect link: flechas bidireccionales process ↔ object (cambio estado sin detallar)
- [P128] **DEFINICIÓN** — input-output link pair: input state → process + process → output state

#### Procedural links (enabling)
- [P129] **DEFINICIÓN** — agent link: "black lollipop"; human enabler → process
- [P130] **DEFINICIÓN** — instrument link: "white lollipop"; non-human enabler → process

#### Diagrams y principios
- [P131] **DEFINICIÓN** — OPD: Object-Process Diagram; modalidad gráfica
- [P132] **DEFINICIÓN** — OPL: Object-Process Language; modalidad textual (subconjunto inglés natural)
- [P133] **DEFINICIÓN** — SD: System Diagram; top-level OPD con 5 componentes
- [P134] **DEFINICIÓN** — SD1: primer nivel detalle; refina main process en sub-processes
- [P135] **REGLA** — Graphics-Text Equivalence: OPD ↔ OPL biyección completa
- [P136] **REGLA** — Timeline Principle: sub-processes synchronous ordenados top→bottom en in-zoom
- [P137] **REGLA** — Detail Hierarchy: crear OPD descendiente cuando exceso detalle
- [P138] **REGLA** — Procedural Link Uniqueness: ≤1 procedural link entre process y object/state en cualquier nivel

#### System aspects
- [P139] **DEFINICIÓN** — structure: "what" del sistema; components + relaciones estáticas
- [P140] **DEFINICIÓN** — behavior: "how" del sistema; processes + relaciones dinámicas
- [P141] **DEFINICIÓN** — function: "why" del sistema; main object + main process → beneficio
- [P142] **DEFINICIÓN** — emergence: capacidad del sistema completo ausente en sus partes individuales
- [P143] **DEFINICIÓN** — system architecture: structure + behavior → emergence → function

#### SD components
- [P144] **DEFINICIÓN** — purpose: beneficio clave para beneficiaries (artificial) / outcome (natural)
- [P145] **DEFINICIÓN** — enablers: agents (humanos) + instruments (no-humanos); no transformados
- [P146] **DEFINICIÓN** — environment: things fuera del sistema que afectan operación; contorno dashed
- [P147] **DEFINICIÓN** — problem occurrence: espejo de purpose; process ambiental causa estado problemático
- [P148] **DEFINICIÓN** — affiliation: systemic (sólido) vs environmental (dashed)

#### Refinamiento
- [P149] **REGLA** — synchronous → in-zooming (sub-processes dentro, ordenados verticalmente)
- [P150] **REGLA** — asynchronous → unfolding (sub-processes fuera, conectados por structural links)
- [P151] **REGLA** — objects → unfolding en object tree (parts + attributes)
- [P152] **REGLA** — state suppression: ocultar states irrelevantes en OPD dado; pseudo-state indica existencia
