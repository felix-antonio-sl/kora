---
_manifest:
  urn: urn:fxsl:kb:metodologia-modelamiento-opm-p03
  provenance:
    created_by: kora/curator
    created_at: '2026-03-25'
    source: synthesis:opm-iso-19450,opm-opl-es,opcloud-tutorial-videos,opm-applied-system-modeling,opm-canonical-example
version: 3.5.1
status: published
tags:
- opm
- methodology
- system-modeling
- sd-construction
- refinement
- complexity-management
- modeling-protocol
- patterns
- antipatterns
- control-flow
- error-handling
- quantitative
- simulation
- executable-modeling
- opcloud
lang: es
extensions:
  kora:
    family: specification
    depends_on:
    - urn:fxsl:kb:opm-iso-19450
    - urn:fxsl:kb:opl-es
    shard_index: 3
    shard_count: 4
    shard_root_urn: urn:fxsl:kb:metodologia-modelamiento-opm
---

# Metodologia de Modelamiento OPM — Protocolo de Modelamiento Conceptual de Sistemas - Parte 03

## 9 Heuristicas de Modelamiento Avanzado

### 9.1 State-Preserving Process → Tagged Structural Link

Cuando un proceso mantiene un objeto en su estado actual sin transformarlo (Supporting, Holding, Maintaining, Keeping, Storing, Containing, Connecting), el modelador DEBERIA reemplazarlo con un tagged structural link.

**Rationale:** Los procesos state-preserving violan la definicion fundamental de proceso como "thing que transforma un objeto". El tagged structural link es mas compacto y expresa la naturaleza time-invariant de la relacion.

**Correcto:** `Foundation supports House.` (tagged structural link, una sentencia OPL)

**Incorrecto:** Supporting como proceso explicito con Foundation como instrument y House como affectee (multiples links, OPL mas complejo, contradice definicion de proceso)

**Excepcion:** Si mantener el estado requiere esfuerzo no trivial (ej: helicopter hovering requiere propulsion activa), el modelador DEBE modelar el proceso explicitamente.

### 9.2 Transient Object → Invocation Link

Cuando un proceso crea un objeto que el siguiente proceso consume inmediatamente sin intervencion, el modelador DEBERIA suprimir el objeto transiente y reemplazar la creation-consumption pair con un invocation link (forma de rayo).

**Correcto:** `Object Detecting invokes Threat Assessing.` (invocation link, Spark suprimido)

**Incorrecto:** Mantener Detection Signal como objeto explicito cuando nunca es observado ni transformado por otro proceso.

### 9.3 Dualidad Estructural

Los patterns §9.1 y §9.2 son duales: tagged structural links suprimen procesos state-preserving innecesarios; invocation links suprimen objetos transientes innecesarios. El modelador DEBE aplicar ambos consistentemente.

### 9.4 Role Shift entre Niveles de Detalle

Un objeto PUEDE ser instrument en un nivel abstracto (ej: SD) y affectee en un nivel detallado (ej: SD1), siempre que el estado inicial y final sean iguales en el nivel abstracto (cambio neto = cero).

**Correcto:** Dishwasher es instrument de Dish Washing en SD. En SD1: Loading cambia Dishwasher de empty a loaded; Unloading cambia de loaded a empty (neto = sin cambio → instrument valido en SD).

**Incorrecto:** Declarar un objeto como instrument en SD cuando su estado neto cambia en SD1 (debe ser affectee en ambos niveles).

### 9.5 Arbol de Decision de Propiedades de Atributos

Al definir un atributo, el modelador DEBERIA clasificarlo en cuatro dimensiones binarias:

| Dimension | Valores | Criterio |
|-----------|---------|----------|
| Explicitness | explicit (default) / implicit | ¿Es un objeto separado? |
| Mode | qualitative (default) / quantitative | ¿Valores numericos? |
| Touch | hard (default) / soft | ¿Computable desde otros atributos? |
| Emergence | inherent (default) / emergent | ¿Al menos una parte lo exhibe? |

Atributos soft son derivables → PUEDEN no requerir tracking independiente. Atributos emergent existen solo a nivel del todo → definen la arquitectura del sistema.

### 9.6 Link Homogeneity

Structural links DEBEN ser homogeneos (object↔object o process↔process). Procedural links DEBEN ser non-homogeneous (object↔process). Unica excepcion: exhibition-characterization permite las 4 combinaciones de perseverance (object exhibe attribute-object, object exhibe operation-process, process exhibe attribute-object, process exhibe operation-process).

### 9.7 State-Specified Tagged Structural Links

Cuando un estado de un objeto corresponde o se asocia con otro objeto, el modelador DEBERIA usar un state-specified tagged structural link (conectando el estado al objeto asociado) en vez de crear procesos o objetos intermedios.

### 9.8 Discriminating Attributes y State-Specified Characterization

Cuando las especializaciones se distinguen por un valor de atributo, el modelador DEBERIA usar un discriminating attribute con state-specified characterization links. Esto produce un OPD significativamente mas compacto que repetir el atributo para cada especializacion.

### 9.9 Alcance de Herencia OPM

Cada especializacion DEBE heredar del general: (1) todas las partes (aggregation), (2) todos los features (exhibition), (3) todos los tagged structural links, (4) todos los procedural links. Los estados tambien se heredan. Una especializacion PUEDE override estados heredados especificando estados propios.

### 9.10 Relatividad de Instancia y Visual vs Logical Instances

"Instance" es relativo al sistema de discurso. Lo que es instancia en un sistema (ej: "Taurus 2015" en comparacion de autos) PUEDE ser clase con especializaciones en otro sistema (ej: autos individuales con VIN en un concesionario).

**Visual Instance vs Logical Instance:** Una visual instance es el mismo thing representado en diferentes OPDs (misma identidad, diferente vista). Una logical instance es una relacion classification-instantiation (clase → instancia). El modelador NO DEBE confundir ambas. Visual instances solo PUEDEN crearse entre elementos del mismo perseverance (object↔object, process↔process; object→process prohibido).

### 9.11 Clasificacion de Essence para Things Mixtos

Cuando un thing tiene partes physical e informatical, el modelador DEBE clasificarlo como **physical**. La esencia dominante del componente tangible prevalece. Ejemplo: Baggage Transporting system tiene componentes informaticales (location tracking) pero se clasifica como physical porque el proceso involucra transporte fisico.

### 9.12 Direct States vs Attribute + Values (Simplificacion)

Cuando un objeto tiene un solo atributo relevante, el modelador PUEDE simplificar el modelo asignando los valores del atributo como **estados directos del objeto**, eliminando el atributo intermedio.

**Correcto (simplificado):** `Fetus can be embryo or baby.` (estados directos del objeto)

**Correcto (completo):** `Fetus exhibits Developmental Stage. Developmental Stage of Fetus can be embryo or baby.` (atributo + valores)

**Decision rule:** Usar la forma simplificada cuando el objeto tiene un solo atributo relevante al scope del modelo y la legibilidad mejora. Usar la forma completa cuando el objeto tiene multiples atributos o cuando el nombre del atributo agrega informacion semantica no obvia.

### 9.13 Generalizacion como Abstraccion del SD

Cuando multiples objetos especificos del SD1 compartirían el mismo tipo de relacion con el proceso principal en el SD, el modelador DEBERIA crear un objeto general que los englobe y agregar solo ese objeto al SD, manteniendo los especificos en SD1.

**Correcto:** Road Danger Representation (general) en SD; Vehicle-in-Front Representation, Pedestrian-in-Front Representation, Lane Set Representation (especificos) en SD1 conectados via generalization-specialization.

**Incorrecto:** Las tres representaciones especificas en SD (overcrowding del diagrama top-level).

### 9.14 Making Implicit Objects Explicit

Al modelar sistemas a partir de texto (standards, regulaciones, especificaciones), el modelador DEBE identificar y modelar explicitamente los objetos que el texto menciona implicitamente. En documentos process-oriented, los objetos transformados por los procesos frecuentemente no se nombran. El acto de forzar la pregunta "¿que objeto transforma este proceso?" revela entidades criticas omitidas por el autor del texto.

### 9.15 Synonym/Homonym Detection via Modelamiento Formal

OPM fuerza un mapping 1:1 entre things y nombres. El modelador DEBE usar este formalismo para detectar: (a) **sinonimos** — multiples palabras para el mismo concepto (ej: "purpose" vs "stated purpose" en ISO 15288), y (b) **homonimos** — misma palabra para conceptos distintos (ej: "environment" vs "operational environment"). Cada sinonimo detectado DEBE resolverse eligiendo un termino canonico. Cada homonimo DEBE resolverse creando things separados con nombres distintos.

### 9.16 Text-Diagram Inconsistency Detection

El modelamiento OPM de un documento existente produce como byproduct la deteccion de inconsistencias entre el texto principal y sus diagramas. El modelador DEBERIA documentar estas inconsistencias como hallazgos de calidad. Ejemplo: en ISO 15288, boxes representan "systems" en un diagrama y "processes" en otro, sin justificacion. El modelo OPM resuelve estas ambiguedades asignando perseverance correcto (object vs process) a cada thing.

### 9.17 Clause-Referenced OPD Naming

Al modelar documentos normativos, el modelador DEBERIA etiquetar los OPDs con las clausulas del documento fuente (ej: `[5.2.2] System`, `[6.1] Acquisition`). Esto permite trazabilidad directa entre el modelo y el texto fuente, facilita revision por pares, y soporta validacion de cobertura.

## 10 Control de Flujo Avanzado

### 10.1 Wait vs Skip — Condition vs Non-Condition Links

| Tipo de link | Si el objeto/estado esta ausente | Uso |
|-------------|----------------------------------|-----|
| Non-condition (sin `c`) | Proceso ESPERA indefinidamente | Proceso obligatorio — el sistema se detiene |
| Condition (con `c`) | Proceso se SALTA | Proceso opcional — la ejecucion avanza |

**Regla de decision:** Usar condition link cuando el proceso es opcional; usar non-condition link cuando es obligatorio. Error comun: usar non-condition link para un recurso que puede no aparecer → deadlock.

### 10.2 Precedencia de Skip sobre Wait

Cuando el preprocess object set contiene tanto condition links como non-condition links, skip DEBE tener precedencia sobre wait. Si cualquier condition-linked object/estado esta ausente, el proceso se salta independientemente de la satisfaccion de los non-condition links.

### 10.3 Semantica de Event Links (OR) vs Condition Links (AND/OR)

- **Multiples event links** al mismo proceso: semantica OR (cualquier evento individual basta para trigger)
- **Multiples condition links** al mismo proceso: semantica AND para ejecucion (todos deben cumplirse) pero semantica OR para skip (falla de cualquiera causa skip)

### 10.4 XOR vs OR Link Fans

| Fan | Simbolo | Semantica | Uso |
|-----|---------|-----------|-----|
| XOR | Arco dashed simple | Exactamente uno de los paths | Decisiones mutuamente excluyentes |
| OR | Arco dashed doble | Al menos uno de los paths | Concurrencia condicional |

Para fan size f=2: XOR usa "either...or"; para f>2: "exactly one of." OR siempre usa "at least one of."

### 10.5 XOR/OR Combinatorial (m-de-f)

Para f > 2, el modelador PUEDE generalizar: "exactly m of f" (XOR combinatorial) o "at least m of f" (OR combinatorial), donde m < f. El numero m se registra junto al arco en el OPD. Modela escenarios como "2 de 3 key holders deben estar presentes."

### 10.6 NOT via Existent/Non-Existent

OPM no tiene simbolo NOT dedicado. Para modelar "proceso P ejecuta solo cuando objeto S esta ausente," el modelador DEBERIA crear estados implicitos `existent` y `non-existent` para S, y conectar `non-existent` a P con instrument link o condition instrument link.

### 10.7 Path Labels para Disambiguation de Escenarios

Cuando un proceso tiene multiples links procedurales entrantes y salientes y se necesita especificar cual input mapea a cual output, el modelador DEBE usar path labels. El link seguido a la salida es el que tiene el mismo label que el link de entrada. Path labels proveen memoria entre input y output y eliminan el requisito AND para preprocess objects: solo objetos con el mismo label deben coexistir.

### 10.8 Patrones de Iteracion

**Patron Set-Member:** Adjuntar dos procedural links del mismo tipo a un proceso — uno a un set de n miembros y otro a un miembro — produce iteracion automatica n veces.

**Patron Loop:** Un invocation link desde el ultimo subproceso hacia el proceso padre in-zoomed crea un loop. Para intervalos entre iteraciones, insertar un proceso Waiting con time constraints.

**Patron Decision-Node:** Para iteracion con condicion de terminacion, usar un boolean decision node que evalua despues de cada ciclo; si "No," invocation link loopea; si "Yes," la ejecucion avanza al siguiente subproceso.

### 10.9 Semantica Temporal de Transforming Links

| Tipo | Timing de transformacion |
|------|-------------------------|
| Consumption | Inmediata al inicio del proceso. Consumee deja de existir tan pronto el proceso se activa. Si el consumee no existe, el proceso espera |
| Result | Creacion solo al termino del proceso. Durante la ejecucion, ni consumee (ya consumido) ni resultee (aun no creado) existen |
| Effect | Affectee sale del input state al inicio del subprocess que lo afecta; entra al output state al completion de ese subprocess. Entre ambos puntos, el objeto esta "en transicion" — estado indeterminado |

Esta semantica temporal es critica para simulacion y para entender la disponibilidad de objetos entre subprocesos.

### 10.10 Boolean Objects y Branching

Un **Boolean object** es un objeto informatical dual-state generado por un proceso de decision. Sus estados forman un par Boolean (yes/no, true/false, pass/fail, approved/denied, `geq-x`/`lt-x`). Cada estado se conecta via condition links a procesos alternativos subsiguientes, implementando control if-then-else.

**Generalizacion:** Cualquier objeto con n estados funciona como un case statement — cada estado PUEDE servir como source de condition o instrument link para un proceso subsiguiente distinto.

### 10.11 Scenarios y Behavioral Repertoire

Un **scenario** (thread of execution) es un path especifico a traves de la jerarquia de procesos del sistema, trazado siguiendo el estado de cada objeto. En cada branching point (Boolean object, condition links, XOR fan), exactamente un path se materializa. El conjunto completo de scenarios constituye el **behavioral repertoire** del sistema — la totalidad de comportamientos posibles.

### 10.12 Condition Transforming Links (Taxonomy Completa)

| Link | Semantica | OPL |
|------|-----------|-----|
| Condition consumption | Si consumee existe, proceso lo consume; si no, skip | `Process occurs if Object exists, in which case Process consumes Object, otherwise Process is skipped` |
| Condition effect | Si affectee existe, proceso lo afecta; si no, skip | `Process occurs if Object exists, in which case Process affects Object, otherwise Process is skipped` |
| Condition agent | Si agent existe, proceso opera con agent; si no, skip | `Agent handles Process if Agent exists, otherwise Process is skipped` |
| Condition instrument | Si instrument existe, proceso opera; si no, skip | `Process occurs if Instrument exists, else Process is skipped` |

Cada uno de estos TIENE version state-specified (proceso opera si objeto esta en estado especifico; si no, skip).

### 10.13 Value-Specified Procedural Links

| Link | Semantica |
|------|-----------|
| Value setting link | Unidirectional; establece valor de atributo independiente del valor previo |
| Value effect link | Bidirectional; cambia valor de atributo de uno no especificado a otro |
| In-out-specified value effect link pair | Cambia valor de atributo de input value especifico a output value especifico |

Estos links aplican a **values** (estados de atributos), no a estados de objetos no-atributo.

### 10.14 Probabilistic Fans

En un XOR diverging fan probabilistico, cada link DEBE anotarse con una probabilidad. La suma de todas las probabilidades DEBE ser exactamente 1. Default sin fan: si un proceso crea un objeto con n estados, cada estado tiene probabilidad 1/n.

## 11 Manejo de Errores Temporales

### 11.1 Overtime Exception Links

Cuando un proceso tiene Maximal Duration, el modelador DEBERIA adjuntar un overtime exception link a un proceso de manejo de overtime. Si el proceso excede su tiempo maximo, el exception handler se activa y resuelve los objetos en transicion a estados permisibles.

### 11.2 Undertime Exception Links

Cuando un proceso tiene Minimal Duration, el modelador DEBERIA adjuntar un undertime exception link. Si el proceso se completa antes del minimo (o es skipped, duracion = 0), el undertime handler se activa.

**Pattern — Undertime como detector de skip:** Un undertime exception link en un proceso con duracion minima detecta cuando el proceso no se ejecuto (duracion efectiva = 0 < minimo positivo), activando recovery logic. Esto provee un mecanismo formal para "proceso no ejecutado."

### 11.3 Resolucion de Estado Indeterminado

Todo affectee en transicion durante un proceso activo permanece en estado indeterminado si el proceso falla. Los exception handlers (overtime/undertime) DEBEN resolver el objeto a un estado permisible. Sin exception handling, el objeto queda indefinido y el modelo es incompleto para simulacion.

## 12 Modelamiento Cuantitativo y Simulacion

### 12.1 Transformation Rate

Cuando consumo, creacion, o cambio de estado ocurre como flujo continuo o operacion multi-unidad en el tiempo, el modelador DEBERIA asignar una propiedad Transformation Rate al procedural link relevante. Tres especializaciones: consumption rate, yield rate, effect rate.

### 12.2 Computing with OPM — Claridad de Roles de Operandos

Cuando se modelan operaciones aritmeticas no conmutativas (Dividing, Subtracting), el modelador DEBE designar explicitamente los roles de operandos (Dividend vs Divisor, Minuend vs Subtrahend). OPM embebe formulas en nombres de proceso (ej: `Residue Computing (residue=il-u)`) para compactness.

### 12.3 Duration Distribution para Simulacion Estocastica

El modelador PUEDE especificar una Duration Distribution en la propiedad Duration de un proceso, identificando una funcion de distribucion de probabilidad. En runtime, cada instancia del proceso muestrea su duracion independientemente. Sin Duration Distribution, todas las instancias ejecutan en exactamente la Expected Duration (irrealista para sistemas reales).

### 12.4 Workflow Computacional en OPCloud

Cuando se implemente el modelo en OPCloud, el modelador DEBE seguir este patron de 5 pasos:

1. **Definir objetos** con atributos computacionales (tipo: integer, float, string, character, boolean)
2. **Asignar alias** a cada atributo computacional (ej: "x1", "y1") para uso en formulas
3. **Crear proceso de calculo** — representado con braces `{}` en el OPD, indicando naturaleza computacional
4. **Definir formula** usando los aliases (ej: `slope = (y2-y1)/(x2-x1)`)
5. **Conectar proceso** a objetos via consumption/effect links para flujo de datos

**Stereotypes en OPCloud:** Templates de parametros reutilizables para patrones computacionales comunes. La herramienta distingue niveles Global y Organizational. Al remover un stereotype de un thing, el modelador DEBE elegir entre unlink (conservar componentes) o unlink-and-remove (eliminar componentes agregados).

### 12.5 Range Validation

El modelador DEBERIA asignar rangos a atributos computacionales para enforcement durante simulacion. Sintaxis: `[inclusive`, `(exclusive`. Multiples rangos: `[1,10][20,30]`. El sistema valida automaticamente que los valores permanezcan en rangos validos.

### 12.6 User Input Simulation Workflow

Para simulacion con entrada de usuario en OPCloud, el modelador DEBE seguir estos 6 pasos:

1. Crear usuario como objeto fisico
2. Conectar usuario al proceso via **agent link**
3. Marcar proceso para recibir user input durante simulacion
4. Crear objeto input computacional para recibir valores
5. Conectar proceso al objeto input via **effect link** (requerido para actualizar objetos computacionales con valores de usuario)
6. En la computacion, usar funcion **User Input** del API predefinido

Sin los pasos 5-6, el objeto input no recibira valores durante simulacion.

### 12.7 Operational Semantics en Contextos In-Zoomed

Ejecutar un proceso con contexto in-zoomed transfiere control recursivamente al subproceso topmost del nivel mas profundo. El control retorna al proceso in-zoomed tras completion del ultimo subproceso.

**Transformaciones del Involved Object Set por instancia:**

| Tipo de transformee | Timing de transformacion |
|---------------------|-------------------------|
| Consumee | Deja de existir al inicio del deepest subprocess que lo consume |
| Affectee | Sale del input state al inicio del deepest subprocess que lo cambia; entra al output state al completion de ese (o subsiguiente) subprocess |
| Resultee | Creado al completion del deepest subprocess que lo genera |

Un objeto stateful en transicion: ha dejado su input state pero aun no ha llegado al output state (duracion positiva). Durante este periodo, el objeto es indisponible para otros procesos.

### 12.8 Compound State Space y Precondiciones Compuestas

El state space de un objeto es el producto cartesiano de los sets de estados de todos sus atributos y partes stateful. El modelador DEBE reconocer que no todos los puntos del state space son factibles; los compound states infeasibles DEBERIAN identificarse mediante process modeling. Para precondiciones compuestas que abarcan multiples atributos, el modelador DEBE usar multiple condition clause OPL sentences con clausulas X-OR numeradas conectadas por AND logico.

### 12.9 Integracion Externa e Ingesta de Datos en OPCloud

Cuando el modelo deja de ser solo conceptual y debe intercambiar datos con entorno externo, el modelador PUEDE usar las siguientes capacidades:

- **MQTT:** adecuado para sensores/actuadores IoT con topicos publish/subscribe. Requiere configurar raw server y MQTT server. El modelador DEBERIA usarlo para acoplar variables computacionales a telemetria o comandos ligeros.
- **ROS:** adecuado para robots y sistemas con ROS master. El workflow minimo DEBE incluir definicion de mensaje, publicacion, suscripcion y manejo del feedback loop via condiciones/iteracion.
- **CSV Import para atributos:** util para carga masiva de instancias y valores de atributos. Restriccion: el objeto target NO DEBE ser una instancia conectada via classification-instantiation. El modelador DEBERIA previsualizar el import y decidir si ignora existentes o crea atributos faltantes.
