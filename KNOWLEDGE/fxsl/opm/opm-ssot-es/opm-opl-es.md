---
_manifest:
  urn: urn:fxsl:kb:opl-es
version: 2.0.0
status: published
tags:
- opm
- opl
- spanish
- es
- grammar
- i18n
- bimodal
- localization
lang: es
extensions:
  kora:
    family: specification
    depends_on:
    - urn:fxsl:kb:opm-es
    shard_index: 1
    shard_count: 5
    shard_root_urn: urn:fxsl:kb:opl-es
relations:
  cites:
  - urn:fxsl:kb:manual-metodologico-opm-es
  - urn:fxsl:kb:opd-es
  - urn:fxsl:kb:opm-es
---


# OPL-ES — Lenguaje Objeto-Proceso en Español


Especificación completa de la gramática OPL en español, diseñada para que herramientas de modelado OPM generen y analicen sentencias OPL en español manteniendo equivalencia semántica total con la forma inglesa de referencia.

Referencia de núcleo: `urn:fxsl:kb:opm-es`.

---

## 0. Alcance y contrato editorial

Este documento es la **capa textual canónica** del corpus OPM en español. Su responsabilidad es:

- fijar la superficie léxica y sintáctica de OPL-ES;
- definir plantillas textuales canónicas para los hechos del modelo;
- preservar equivalencia semántica de ida y vuelta entre OPL-EN y OPL-ES.

Este documento **no** define:

- la semántica base de OPM, que pertenece a [OPM — Núcleo conceptual](urn:fxsl:kb:opm-es);
- la gramática gráfica del OPD, que pertenece a [OPD — Gramática visual de OPM](urn:fxsl:kb:opd-es);
- el procedimiento de construcción, refinamiento y gobernanza del modelo, que pertenece a [Manual metodológico de OPM](urn:fxsl:kb:manual-metodologico-opm-es).

Regla editorial: cuando este documento menciona enlaces, refinamientos, cardinalidades u operadores, lo hace **solo** para fijar su realización textual canónica en español. La semántica del hecho y su geometría visual se heredan del corpus base.

---

## 1. Decisiones de Diseño

### 1.1 Denominación de Procesos

En OPL-EN los procesos usan gerundio (-ing): "Cooking", "Driving", "Data Processing". En OPL-ES los procesos pueden usar **infinitivo** (-ar, -er, -ir): "Cocinar", "Conducir", "Procesar Datos", o una **nominalización verbal** encabezada por una primera palabra terminada en `-ción`: "Ampliación", "Verificación de Datos".

El infinitivo español es el equivalente funcional más directo del gerundio sustantivado inglés: funciona como sustantivo sujeto ("Cocinar consume..."). Sin embargo, en español técnico también es plenamente válida una forma nominal encabezada por `-ción`, cuando el dominio prefiera un nombre de acción en vez de un infinitivo.

**Validación de nombre**: un nombre de proceso OPL-ES válido cumple al menos una de estas condiciones:

1. La primera palabra está en infinitivo y termina en `-ar`, `-er` o `-ir`
2. La primera palabra termina en `-ción`
3. En dominios que lo justifiquen, la primera palabra termina en `-miento`

Ejemplos válidos: "Procesar Datos", "Preparar Empanadas", "Ampliación de Cobertura", "Verificación de Identidad", "Mantenimiento Preventivo".

**Patrones de nombre de proceso** (paralelos a EN):

| Patrón EN | Ejemplo EN | Patrón ES | Ejemplo ES |
|-----------|-----------|-----------|-----------|
| verb-ing | Making | Infinitivo o nominalización | Hacer / Fabricación |
| noun verb-ing | Cake Making | Infinitivo sustantivo o nominalización con complemento | Preparar Torta / Preparación de Torta |
| adj verb-ing | Automatic Responding | Infinitivo + adverbio o nominalización | Responder Automáticamente / Respuesta Automática |
| adj noun verb-ing | Automatic Crash Responding | Infinitivo complejo o nominalización encabezada por `-ción` | Responder a Colisión Automáticamente / Atención Automática de Colisión |

Preferentemente entre 2 y 4 palabras. Se aceptan nombres más largos cuando el dominio lo exige y no introducen ambigüedad. Se capitalizan las palabras léxicas; artículos y preposiciones breves PUEDEN permanecer en minúscula cuando mejora la naturalidad del español.

### 1.2 Denominación de Objetos

Sin cambio respecto a OPL-EN: sustantivo singular, con capitalización en las palabras léxicas del nombre.

Plurales: sufijo "Conjunto" para inanimados (EN: "Set"), "Grupo" para humanos (EN: "Group").

Ejemplos: **Ingrediente**, **Conjunto de Ingredientes**, **Grupo de Comensales**, **Torta de Manzana**.

### 1.3 Denominación de Estados

Sin cambio respecto a OPL-EN: minúsculas, forma pasiva o descriptiva del objeto que los contiene.

Ejemplos: `pintado`, `inspeccionado`, `pre-cortado`, `vacío`, `cargado`, `satisfecho`.

### 1.4 Género Gramatical

Las plantillas usan masculino como género por defecto. El modelador ajusta al género natural del sustantivo en instancias concretas. El género afecta artículos y participios pero no la estructura de la sentencia.

Ejemplo: "es un **Sistema**" (masc.) → "es una **Máquina**" (fem.).

### 1.5 Ser vs Estar

- **estar** para estados de objetos (condición temporal, mutable): "**Objeto** está en `estado`"
- **ser** para propiedades invariantes (tipo, clasificación, esencia): "**Objeto** es de tipo X", "**X** es un **Y**"

Justificación: los estados OPM son situaciones temporales de un objeto (estar), mientras que tipo, clasificación y esencia son propiedades permanentes del modelo (ser). Esta distinción gramatical del español se alinea con la semántica OPM.

### 1.6 Artículos y Preposiciones

OPL-ES omite artículos en las sentencias, siguiendo la convención de OPL-EN, excepto donde la gramática española los requiere:

- "es un/una" en clasificación-instanciación y generalización-especialización individual
- "de lo contrario" en condiciones
- "al menos" en operadores lógicos y cardinalidades

Preposición "a" personal: omitida para objetos directos, ya que las entidades OPM son típicamente inanimadas. Ejemplo: "*Cocinar* consume **Masa**" (no "consume a Masa").

### 1.7 Convenciones Tipográficas (Markdown OPL)

| Entidad | Convención | Ejemplo |
|---------|-----------|---------|
| Objeto | **negrita** | **Ingrediente** |
| Proceso | *cursiva* | *Cocinar* |
| Estado | `monoespaciado` | `crudo` |

Estas convenciones aplican a la representación textual en Markdown. Los colores, contornos, sombreados y demás atributos del OPD pertenecen a la capa visual y no forman parte del contrato de OPL-ES.

### 1.8 Orden Canónico

OPL-ES preserva el orden sujeto-verbo-complemento de cada plantilla OPL-EN. No se reordena la oración. Esto garantiza correspondencia estructural estable entre ambas superficies y simplifica el análisis sintáctico bidireccional.

### 1.9 Con Estado Especificado: Posición del Estado

En OPL-EN el estado precede al objeto como modificador: "`specified-state` Object". En OPL-ES el estado sigue al objeto con la preposición "en": "**Objeto** en `estado`".

- EN: `active User handles Processing.`
- ES: **Usuario** en `activo` maneja *Procesar*.

### 1.10 Voz Pasiva

OPL-ES usa la pasiva refleja ("se consume", "se omite") en lugar de la pasiva perifrástica ("es consumido"), por naturalidad y concisión.

---

## 2. Vocabulario de Verbos OPL-ES

Verbos fijos de la gramática, conjugados en tercera persona singular del presente indicativo.

| Función | EN | ES | Infinitivo ES |
|---------|----|----|--------------|
| Consumo | consumes | consume | consumir |
| Resultado | yields | genera | generar |
| Efecto | affects | afecta | afectar |
| Cambio de estado | changes … from … to | cambia … de … a | cambiar |
| Agente | handles | maneja | manejar |
| Instrumento | requires | requiere | requerir |
| Iniciación | initiates | inicia | iniciar |
| Invocación | invokes | invoca | invocar |
| Ocurrencia | occurs | ocurre | ocurrir |
| Existencia | exists | existe | existir |
| Omisión (pasiva) | is skipped | se omite | omitir |
| Consumo (pasiva) | is consumed | se consume | consumir |
| Agregación | consists of | consta de | constar |
| Exhibición | exhibits | exhibe | exhibir |
| Especialización (pl.) | are | son | ser |
| Especialización (sg.) | is a | es un/una | ser |
| Instanciación | is an instance of | es una instancia de | ser |
| Relación | relates to | se relaciona con | relacionar |
| Variación de rango | ranges from … to | varía de … a | variar |
| Tipo | is of type | es de tipo | ser |
| Declaración de estados | can be | puede estar | poder + estar |
| Descomposición | zooms into … in that sequence | se descompone en … en esa secuencia | descomponerse |
| Despliegue | unfolds into | se despliega en | desplegarse |
| Refinamiento | is refined by in-zooming … in | se refina por descomposición de … en | refinarse |

### Palabras Clave Fijas

| EN | ES |
|----|----|
| if | si |
| in which case | en cuyo caso |
| otherwise / else | de lo contrario |
| from | de |
| to | a |
| and | y (e ante i-, hi-) |
| or | o (u ante o-, ho-) |
| as well as | así como |
| exactly one of | exactamente uno de |
| at least one of | al menos uno de |
| at least one other | al menos otro/a |
| an optional | un/una opcional |
| at least one | al menos un/una |
| following path | por ruta |
| duration of | duración de |
| exceeds | excede |
| falls short of | es menor que |
| in that sequence | en esa secuencia |
| can be | puede estar |
| is initial | es inicial |
| is final | es final |
| is default | es por defecto |
| is initial and final | es inicial y final |

---

## 3. Plantillas OPL-ES — Descripción de Entidades

### 3.1 Propiedades Genéricas

| ID | OPL-EN | OPL-ES |
|----|--------|--------|
| D1 | Thing is Physical. | **Cosa** es física. |
| D2 | Thing is Informatical. | **Cosa** es informacional. |
| D3 | Thing is Environmental. | **Cosa** es ambiental. |
| D4 | Thing is Systemic. | **Cosa** es sistémica. |
| D11 | Thing is Persistent. | **Cosa** es persistente. |
| D12 | Thing is Transient. | **Cosa** es transitoria. |

### 3.2 Enumeración de Estados

| ID | OPL-EN | OPL-ES |
|----|--------|--------|
| D5 | Object can be state1, state2, or state3. | **Objeto** puede estar `estado1`, `estado2` o `estado3`. |
| D6 | Object can be state1, …, and other states. | **Objeto** puede estar `estado1`, …, y otros estados. |

### 3.3 Designación de Estados

| ID | OPL-EN | OPL-ES |
|----|--------|--------|
| D7 | State s of Object is initial. | Estado `s` de **Objeto** es inicial. |
| D8 | State s of Object is final. | Estado `s` de **Objeto** es final. |
| D9 | State s of Object is default. | Estado `s` de **Objeto** es por defecto. |
| D10 | State s of Object is initial and final. | Estado `s` de **Objeto** es inicial y final. |

### 3.4 Nota sobre procesos persistentes

Esta adaptación reconoce procesos que mantienen un estado o condición sin introducir cambio neto observable relevante. Ejemplos: *Existir*, *Sostener*, *Mantener*, *Conservar*.

Para mantener cerrada la superficie canónica, OPL-ES adopta la siguiente convención textual:

- cuando el proceso persistente permanece explícito en el modelo, su realización canónica es una oración de cambio con **estado de entrada = estado de salida**, por ejemplo: `*Mantener Presión* cambia **Tanque** de \`presurizado\` a \`presurizado\`.` Esta forma preserva el hecho del modelo sin introducir verbos especiales fuera de la gramática base;
- cuando la temporalidad sostenida no es semánticamente central, el modelo PUEDE simplificarse editorialmente mediante un enlace estructural etiquetado, según la política metodológica de `metodologia-opm-es` §9.1.

No existe una familia verbal adicional exclusiva para procesos persistentes: la canonicidad se obtiene reutilizando la plantilla transformadora ya existente con estado de entrada y salida coincidentes.

---

## 4. Plantillas OPL-ES — Enlaces Transformadores

### 4.1 Básicos

| ID | Tipo | OPL-EN | OPL-ES |
|----|------|--------|--------|
| T1 | Consumo | Processing consumes Consumee. | *Procesar* consume **Consumido**. |
| T2 | Resultado | Processing yields Resultee. | *Procesar* genera **Resultado**. |
| T3 | Efecto | Processing affects Affectee. | *Procesar* afecta **Afectado**. |

### 4.2 Con Estado Especificado

| ID | Tipo | OPL-EN | OPL-ES |
|----|------|--------|--------|
| TS1 | Consumo s-s | Process consumes specified-state Object. | *Proceso* consume **Objeto** en `estado`. |
| TS2 | Resultado s-s | Process yields specified-state Object. | *Proceso* genera **Objeto** en `estado`. |
| TS3 | Efecto entrada-salida | Process changes Object from input-state to output-state. | *Proceso* cambia **Objeto** de `estado-entrada` a `estado-salida`. |
| TS4 | Efecto solo entrada (enlace de entrada) | Process changes Object from input-state. | *Proceso* cambia **Objeto** de `estado-entrada`. |
| TS5 | Efecto solo salida (enlace de salida) | Process changes Object to output-state. | *Proceso* cambia **Objeto** a `estado-salida`. |

Nota: TS4 y TS5 son la **realización textual del enlace escindido**. Cuando un efecto entrada-salida (TS3) se distribuye a una descomposición, se escinde en un TS4 temprano (subproceso que saca del estado de entrada) y un TS5 tardío (subproceso que pone en el estado de salida). La geometría visual de esta escisión se define en `opm-visual-es` V-40.

---

## 5. Plantillas OPL-ES — Enlaces Habilitadores

### 5.1 Básicos

| ID | Tipo | OPL-EN | OPL-ES |
|----|------|--------|--------|
| H1 | Agente | Agent handles Processing. | **Agente** maneja *Proceso*. |
| H2 | Instrumento | Processing requires Instrument. | *Proceso* requiere **Instrumento**. |

### 5.2 Con Estado Especificado

| ID | Tipo | OPL-EN | OPL-ES |
|----|------|--------|--------|
| HS1 | Agente s-s | Specified-state Agent handles Processing. | **Agente** en `estado` maneja *Proceso*. |
| HS2 | Instrumento s-s | Processing requires specified-state Instrument. | *Proceso* requiere **Instrumento** en `estado`. |

---

## 6. Plantillas OPL-ES — Enlaces de Evento

### 6.1 Eventos Transformadores

| ID | Tipo | OPL-EN | OPL-ES |
|----|------|--------|--------|
| ET1 | Consumo evento | Object initiates Process, which consumes Object. | **Objeto** inicia *Proceso*, que consume **Objeto**. |
| ET2 | Efecto evento | Object initiates Process, which affects Object. | **Objeto** inicia *Proceso*, que afecta **Objeto**. |

### 6.2 Eventos Habilitadores

| ID | Tipo | OPL-EN | OPL-ES |
|----|------|--------|--------|
| EH1 | Agente evento | Agent initiates and handles Process. | **Agente** inicia y maneja *Proceso*. |
| EH2 | Instrumento evento | Instrument initiates Process, which requires Instrument. | **Instrumento** inicia *Proceso*, que requiere **Instrumento**. |

### 6.3 Eventos Transformadores con Estado Especificado

| ID | OPL-EN | OPL-ES |
|----|--------|--------|
| ETS1 | Specified-state Object initiates Process, which consumes Object. | **Objeto** en `estado` inicia *Proceso*, que consume **Objeto**. |
| ETS2 | Input-state Object initiates Process, which changes Object from input-state to output-state. | **Objeto** en `estado-entrada` inicia *Proceso*, que cambia **Objeto** de `estado-entrada` a `estado-salida`. |
| ETS3 | Input-state Object initiates Process, which changes Object from input-state. | **Objeto** en `estado-entrada` inicia *Proceso*, que cambia **Objeto** de `estado-entrada`. |
| ETS4 | Object in any state initiates Process, which changes Object to destination-state. | **Objeto** en cualquier estado inicia *Proceso*, que cambia **Objeto** a `estado-destino`. |

### 6.4 Eventos Habilitadores con Estado Especificado

| ID | OPL-EN | OPL-ES |
|----|--------|--------|
| EHS1 | Specified-state Agent initiates and handles Processing. | **Agente** en `estado` inicia y maneja *Proceso*. |
| EHS2 | Specified-state Instrument initiates Processing, which requires specified-state Instrument. | **Instrumento** en `estado` inicia *Proceso*, que requiere **Instrumento** en `estado`. |

---
