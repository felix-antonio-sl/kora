---
_manifest:
  urn: "urn:fxsl:kb:opm-ontologia"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-03-06"
    source: "opm_youtube.md + OPM version felix.md + ISO 19450"
version: "1.0.2"
status: published
tags: [opm, iso19450, objetos, procesos, enlaces, estados, opl, ontologia]
lang: es
---

# OPM — Ontologia Core: Objetos, Procesos, Estados y Enlaces

Primitivas de la ontologia minima OPM (ISO 19450). Tres elementos: Objeto + Proceso + Enlace.

---

## Objetos

Cosas que existen o podrian existir. Dos dimensiones clasificatorias:

**Por esencia:**
| Tipo | Representacion OPD | Descripcion |
|------|--------------------|-------------|
| Fisico | Rectangulo sombreado | Ocupa espacio fisico (maleta, persona, robot) |
| Informatico | Rectangulo plano (sin sombra) | No ocupa espacio fisico (peso, temperatura, codigo fuente) |

**Por perseverancia:**
| Tipo | Descripcion |
|------|-------------|
| Stateful | Tiene estados especificados. En todo momento esta en un estado o en transicion entre dos |
| Stateless | Sin estados especificados |

**Por afiliacion:**
| Tipo | Representacion OPD | Descripcion |
|------|--------------------|-------------|
| Sistemico | Contorno solido | Parte del sistema |
| Ambiental | Contorno discontinuo (dashed) | Externo al sistema, pero interactua con el |

**Atributos:** Objeto informatico que caracteriza otro thing. Valor = estado del atributo.
OPL: `Attribute of Object is value.`

**Operaciones:** Proceso que caracteriza un objeto (analogo a atributo pero dinamico).
OPL: `Object exhibits Operation.`

**Multiplicidad:** Sufijo `Set` para objetos inanimados plurales; sufijo `Group` para grupos humanos.

---

## Procesos

Cosas que transforman objetos (creando, consumiendo o cambiando su estado). Necesariamente asociados a objetos.

**Por esencia:** Fisicos (sombreados) o informaticos (sin sombra). Representacion OPD: rectangulo con borde azul.

**Por composicion:**
| Tipo | Descripcion | Mecanismo de refinamiento |
|------|-------------|--------------------------|
| Sincrono | Subprocesos en orden fijo y secuencial | In-zooming (orden temporal vertical) |
| Asincrono | Subprocesos sin orden predefinido, pueden ocurrir en paralelo | Unfolding (agregacion-participacion) |

**Operacion:** Proceso que caracteriza un objeto exhibidor. OPL: `Exhibitor exhibits Operation.`

---

## Estados de Objeto

Estado = situacion o posicion de objeto en momento dado. Solo objetos stateful.
Representacion OPD: rectangulo de esquinas redondeadas dentro del objeto (color marron dorado en OPL).

**Tipos especiales:**
| Tipo | Representacion | Descripcion |
|------|---------------|-------------|
| Inicial | Contorno grueso | Estado al crearse el objeto |
| Final | Doble contorno | Estado al fin del ciclo de vida; no puede cambiar |
| Default | Flecha diagonal abierta apuntando | Estado asumido por defecto |

**Pseudoestado:** Rectangulo con tres puntos `...` en esquina inferior derecha. Indica estados suprimidos para simplificar diagrama.

---

## OPL — Object Process Language

Representacion textual generada automaticamente por OPCloud al construir OPD. OPL es un subconjunto de ingles.
Equivalencia completa con OPD: todo lo grafico se expresa textualmente y viceversa.

**Colores semanticos en OPL:** Procesos = azul | Objetos = verde | Estados = marron dorado.

**Convenciones de nombre:**
- Objeto: negrita, capitalizacion cada palabra. Ej: `**Coffee Machine**`
- Proceso: negrita, capitalizacion cada palabra. Ej: `**Coffee Making**`
- Estado: negrita sin capitalizacion. Ej: `**hot**`

---

## Atributos Genericos de Things (ISO 19450)

Todo thing tiene tres atributos genericos:

| Atributo | Valores | Default |
|----------|---------|---------|
| Perseverance | Static / Dynamic | Segun contexto |
| Essence | Physical / Informatical | Segun esencia predominante del sistema |
| Affiliation | Systemic / Environmental | Systemic |

**Esencia del sistema:** Si mayoria de things son informaticos → sistema primariamente informatico; si mayoria son fisicos → sistema fisico.

---

## Principio de Unicidad del Enlace Procedimental

A cualquier nivel de abstraccion, un proceso y un objeto (o cualquiera de sus estados) se conectan con **exactamente un** enlace procedimental. Ese enlace determina unicamente el rol del objeto respecto al proceso.

---

## Enlaces de Transformacion (Procedurales)

Describen como un proceso transforma objetos. Tres tipos fundamentales:

### Enlace de Consumo (Consumption Link)
- Objeto deja de existir al inicio del proceso.
- OPD: flecha con punta cerrada desde objeto → proceso.
- OPL: `Processing consumes Consumee.`
- Variante con estado: `State-specified-Consumee triggers Processing, which consumes Consumee.`

### Enlace de Resultado (Result Link)
- Proceso crea objeto nuevo.
- OPD: flecha con punta cerrada desde proceso → objeto creado.
- OPL: `Processing yields Resultee.`
- Variante con estado resultado: `Processing yields qualified-state Object.`

### Enlace de Efecto (Effect Link)
- Proceso cambia estado de objeto sin especificar transicion (nivel de abstraccion alto).
- OPD: flecha bidireccional (dos puntas cerradas).
- OPL: `Processing affects Affectee.`

### Par de Enlaces Entrada/Salida (Input/Output Link Pair)
- Modela cambio de estado con estados especificados.
- Un enlace de entrada (estado-origen → proceso) + un enlace de salida (proceso → estado-destino).
- OPL: `Processing changes Object from input-state to output-state.`
- Variantes:
  - Solo entrada especificada: `Processing changes Object from input-state.`
  - Solo salida especificada: proceso cambia objeto a output-state desde cualquier estado.

---

## Enlaces de Habilitacion (Enabler Links)

Habilitador = objeto requerido para que proceso ocurra; **no es transformado** por el proceso.

### Enlace de Agente (Agent Link)
- Agente = humano o grupo humano con inteligencia natural orientado a objetivos.
- OPD: linea con circulo solido ("paleta negra") en extremo del proceso.
- OPL: `Agent handles Processing.`

### Enlace de Instrumento (Instrument Link)
- Instrumento = habilitador no humano (objeto inanimado o no decisor).
- OPD: linea con circulo vacio ("paleta blanca") en extremo del proceso.
- OPL: `Processing requires Instrument.`

### Variantes state-specified (habilitacion)
- State-specified agent: `Qualifying-state Agent handles Processing.`
- State-specified instrument: `Processing requires qualifying-state Instrument.`

---

## Comparacion: Transformee vs Enabler

| Aspecto | Transformee | Enabler |
|---------|-------------|---------|
| Rol | Consumido / creado / estado cambiado | Requerido pero no cambiado |
| Sin el objeto | Proceso no tiene sentido | Proceso no ocurre |
| Tipos | Consumee, Resultee, Affectee | Agent, Instrument |
| Punta OPD | Flecha | Circulo (solido=agente, vacio=instrumento) |

---

## Enlaces Estructurales

Relaciones estaticas, independientes del tiempo. Conectan things del mismo tipo (objeto-objeto o proceso-proceso), excepto Exhibition-Characterization.

### Agregacion-Participacion (Aggregation-Participation Link)
- Relacion todo-parte.
- OPD: linea con triangulo solido negro apuntando al todo.
- OPL: `Whole consists of Part1, Part2, and Part3.`
- Aplica a objetos (estructura) y a procesos (sincronos, via in-zooming).
- **Restriccion:** NO conecta objetos con procesos.

### Exhibicion-Caracterizacion (Exhibition-Characterization Link)
- Conecta exhibidor con su feature (atributo u operacion).
- **Unico enlace estructural que puede conectar objetos con procesos** (para modelar operaciones).
- OPD: triangulo negro pequeno dentro de triangulo grande vacio.
- OPL atributo: `Exhibitor exhibits Attribute.`
- OPL operacion: `Exhibitor exhibits Operation.`

### Generalizacion-Especializacion (Generalization-Specialization Link)
- Relacion tipo-subtipo con herencia.
- OPL: `Specialization is a General.`
- Herencia: elementos del general se asignan a especializaciones.
- Restriccion por discriminating attribute: subconjunto de valores heredados.

### Enlace Estructural Etiquetado (Tagged Structural Link)
- Para relaciones que no caben en las fundamentales.
- **Unidireccional etiquetado:** semantica definida por el modelador. OPL: `Source-thing tag Destination-thing.`
- **Unidireccional sin tag (null-tagged):** usa tag default del sistema; si no existe, el default es `relates to`.
- **Bidireccional etiquetado:** dos tags cuando ambos sentidos tienen significado propio no inverso. Produce dos sentencias OPL, una por direccion.
- **Reciproco:** un solo tag compartido en ambos sentidos. Si no hay tag, el default es `are related`.
- OPL reciproco sin tag: `Source-thing and Destination-thing are related.`

### Clasificacion-Instanciacion (Classification-Instantiation Link)
- Conecta clase (patron) con instancias (valores concretos de features).
- OPD: circulo negro pequeno dentro de triangulo vacio.
- OPL: `Instance-thing is an instance of Class-thing.`

---

## Cardinalidad y Multiplicidad

- Sin especificacion: exactamente una instancia por extremo.
- Multiplicidad puede aparecer en: tagged structural links, agregacion-participacion, relaciones procedurales.
- OPL con multiplicidad: objeto en plural precedido por expresion de multiplicidad.
- Restricciones de cardinalidad: expresiones aritmeticas (+, -, *, /) con operadores de comparacion (=, <, >, <=, >=) o conjuntos {}.
- Restricciones de valor de atributo: rangos enteros, reales, strings, enumerados.

---

## Enlace de Invocacion (Invocation Link)

Proceso invoca (reinicia) otro proceso. Modela iteracion y ciclicidad.
- **Invocacion implicita:** al terminar subproceso dentro de in-zoom, invoca el siguiente. Sin grafico; orden vertical implica secuencia.
- **Invocacion explicita:** flecha de proceso a proceso para indicar reinicio.
- **Auto-invocacion:** proceso se invoca a si mismo (ciclo).
