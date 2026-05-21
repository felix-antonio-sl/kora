---
_manifest:
  urn: "urn:fxsl:kb:opm-iso-19450-figuras"
  provenance:
    created_by: "FS"
    created_at: "2026-04-23"
    source: "artifacts/knowledge/_SCRIPTORIUM/INBOX/fxsl/opm-iso-19450-figuras.md — catalogo de figuras OPM ISO 19450 referenciadas"
version: "1.0.0"
status: borrador
tags: [opm, iso-19450, figuras, catalogo, fxsl]
lang: es
extensions:
  kora:
    family: note
---

# Descripciones textuales de figuras y tablas — ISO/PAS 19450

Representación puramente textual del contenido gráfico de la ISO/PAS 19450. Cada entrada describe con precisión los diagramas OPD, tablas y símbolos del estándar original, preservando toda la información semántica y topológica.

---

## Simbología OPM (Sección 4)

### Símbolos de entidad

**Objeto** (object): Rectángulo con borde verde continuo y esquinas rectas. Contiene el nombre de la entidad centrado. El borde tiene grosor estándar.

**Objeto físico** (physical object): Rectángulo con borde verde continuo y esquinas rectas, con una sombra gris proyectada hacia abajo y a la derecha, indicando materialidad física.

**Objeto ambiental** (environmental object): Rectángulo con borde verde discontinuo (línea punteada) y esquinas rectas. El borde punteado indica que el objeto pertenece al entorno del sistema, no al sistema mismo.

**Proceso** (process): Elipse con borde azul oscuro continuo. Contiene el nombre del proceso centrado.

**Proceso físico** (physical process): Elipse con borde azul oscuro continuo y sombra gris proyectada hacia abajo y a la derecha, indicando materialidad física.

**Proceso ambiental** (environmental process): Elipse con borde azul oscuro discontinuo (línea punteada). Indica que el proceso pertenece al entorno del sistema.

**Estado** (state): Rectángulo pequeño con esquinas redondeadas, borde verde oliva continuo, y fondo gris claro. Aparece siempre contenido dentro de un objeto, en la zona inferior del rectángulo del objeto.

### Símbolos de relaciones estructurales

**Agregación-participación**: Triángulo negro sólido (relleno completo) con vértice hacia arriba. Se coloca sobre el enlace estructural que conecta un todo con sus partes.

**Exhibición-caracterización**: Triángulo con borde negro y relleno blanco (hueco), con un pequeño triángulo negro sólido en su interior. Vértice hacia arriba.

**Generalización-especialización**: Triángulo con borde negro y relleno blanco (hueco), sin contenido interior. Vértice hacia arriba.

**Clasificación-instanciación**: Triángulo con borde negro y relleno blanco (hueco), con un pequeño círculo negro sólido en su interior. Vértice hacia arriba.

### Símbolos de enlaces estructurales etiquetados

**Enlace estructural etiquetado unidireccional**: Línea con punta de flecha abierta en el extremo destino. La etiqueta (tag) se escribe sobre la línea, con la fuente en itálica. Sin decoración especial en el extremo origen.

**Enlace estructural etiquetado bidireccional**: Línea con puntas tipo arpón (media punta de flecha) en lados opuestos de ambos extremos. Lleva dos etiquetas: una etiqueta de ida (forward tag) y una etiqueta de vuelta (reverse tag), escritas sobre la línea en itálica.

### Símbolos de enlaces procedimentales

**Enlace de agente** (agent link): Línea con un círculo negro sólido (relleno) en el extremo que toca el proceso. El otro extremo, conectado al agente (persona), tiene un corchete cuadrado abierto.

**Enlace de instrumento** (instrument link): Línea con un círculo blanco (hueco, solo borde) en el extremo que toca el proceso. El otro extremo tiene un corchete cuadrado abierto.

**Enlace de efecto** (effect link): Línea con dos puntas de flecha cerradas (rellenas), una en cada extremo, formando una flecha bidireccional. El objeto afectado está en un extremo y el proceso en el otro.

**Enlace de consumo** (consumption link): Línea con una punta de flecha cerrada (rellena) en el extremo del proceso. El objeto consumido está en el origen, sin decoración especial.

**Enlace de resultado** (result link): Línea con una punta de flecha cerrada (rellena) en el extremo del objeto resultante. El proceso está en el origen.

**Par de enlaces entrada-salida** (input-output link pair): Par de líneas paralelas o cercanas: una flecha desde el estado de entrada del objeto hacia el proceso (enlace de entrada), y otra flecha desde el proceso hacia el estado de salida del objeto (enlace de resultado con estado). Los estados de entrada y salida están explícitamente especificados.

**Enlace de evento de instrumento** (instrument event link): Similar al enlace de instrumento (círculo hueco en el extremo del proceso), pero con una letra pequeña `e` (evento) sobre la línea, indicando que el objeto inicia el proceso.

**Enlace de evento de consumo** (consumption event link): Similar al enlace de consumo (flecha hacia el proceso), pero con una letra pequeña `e` (evento) sobre la línea.

**Enlace condicional de instrumento** (instrumental condition link): Similar al enlace de instrumento, pero con una letra `c` sobre la línea, indicando condicionalidad.

**Enlace condicional de consumo** (consumption condition link): Similar al enlace de consumo, pero con una letra `c` sobre la línea.

**Enlace de evento de agente** (agent event link): Similar al enlace de agente (círculo negro en el extremo del proceso), pero con un símbolo `e` (evento) sobre la línea. El agente tanto inicia como habilita el proceso.

**Enlace de evento de efecto** (effect event link): Similar al enlace de efecto (flecha bidireccional), pero con un símbolo `e` sobre la línea. El objeto inicia el proceso que lo afecta.

**Enlace de excepción por sobretiempo** (overtime exception link): Línea con una barra simple (`/`) sobre el enlace, indicando excepción por exceder la duración máxima.

**Enlace de excepción por subtiempo** (undertime exception link): Línea con doble barra (`//`) sobre el enlace, indicando excepción por completar antes del tiempo esperado.

**Enlace de invocación** (invocation link): Flecha con forma de rayo/zigzag que conecta dos procesos. La punta de flecha indica el proceso invocado. El enlace de auto-invocación forma un bucle que sale y regresa al mismo proceso.

---

## Figura 1 — Panorama del metamodelo OPM

Diagrama OPD que muestra la jerarquía superior del metamodelo OPM.

**Estructura jerárquica (generalización-especialización)**:

- `OPM Element` es el nodo raíz, representado como rectángulo verde en la parte superior.
- `OPM Element` se especializa (triángulo hueco) en dos subtipos: `OPM Link` (rectángulo a la izquierda) y `OPM Thing` (rectángulo a la derecha).

**Relación etiquetada**:

- `OPM Link` se conecta a `OPM Thing` mediante un enlace etiquetado `connects` (flecha unidireccional de OPM Link hacia OPM Thing).

**Segunda capa de especialización**:

- `OPM Link` se especializa en `Structural Link` y `Procedural Link`.
- `OPM Thing` se especializa en `Process` (elipse azul) y `Object` (rectángulo verde).

**Conexiones de enlaces**:

- `Structural Link` tiene dos enlaces etiquetados `connects` que apuntan a `Object` (conecta dos objetos).
- `Procedural Link` tiene un enlace `connects` que apunta a `Process` y otro a `Object` (conecta un proceso con un objeto).

La topología muestra que todo elemento OPM es un enlace o una cosa; las cosas se dividen en procesos y objetos; los enlaces se dividen en estructurales (conectan objetos entre sí) y procedimentales (conectan procesos con objetos).

---

## Figura 2 — Notación gráfica de objeto

Rectángulo verde con borde continuo que contiene el texto `Vehicle Occupant Group` centrado. Es el símbolo canónico de un objeto OPM: forma rectangular, borde verde, sin sombra (informacional), sin línea punteada (sistémico).

---

## Figura 3 — Notación gráfica de proceso

Elipse azul oscuro con borde continuo que contiene el texto `Automatic Crash Responding` centrado en dos líneas. Es el símbolo canónico de un proceso OPM: forma elíptica, borde azul.

---

## Figura 4 — Combinaciones de atributos genéricos de cosas OPM

Diagrama con ocho símbolos organizados en una cuadrícula de 2 filas x 4 columnas, que muestra todas las combinaciones posibles de los tres atributos genéricos de las cosas OPM (perseverancia, esencia, afiliación):

**Fila superior (sistémicos, borde continuo)**:

1. `Informatical Systemic Process`: elipse con borde azul continuo, sin sombra. Proceso informacional y sistémico.
2. `Physical Systemic Process`: elipse con borde azul continuo y sombra gris. Proceso físico y sistémico.
3. `Informatical Systemic Object`: rectángulo con borde verde continuo, sin sombra. Objeto informacional y sistémico.
4. `Physical Systemic Object`: rectángulo con borde verde continuo y sombra gris. Objeto físico y sistémico.

**Fila inferior (ambientales, borde discontinuo)**:
5. `Informatical Environmental Process`: elipse con borde azul discontinuo, sin sombra.
6. `Physical Environmental Process`: elipse con borde azul discontinuo y sombra gris.
7. `Informatical Environmental Object`: rectángulo con borde verde discontinuo, sin sombra.
8. `Physical Environmental Object`: rectángulo con borde verde discontinuo y sombra gris.

Debajo del diagrama, ocho oraciones OPL confirman cada combinación:

- Informatical Systemic Process is an informatical and systemic process.
- Physical Systemic Process is a physical and systemic process.
- Informatical Systemic Object is an informatical and systemic object.
- Physical Systemic Object is a physical and systemic object.
- Informatical Environmental Process is an informatical and environmental process.
- Physical Environmental Process is a physical and environmental process.
- Informatical Environmental Object is an informatical and environmental object.
- Physical Environmental Object is a physical and environmental object.

---

## Figura 5 — Objeto con estados con dos estados

Rectángulo verde con borde continuo que contiene el nombre `Museum Visitor` en la parte superior. Dentro del rectángulo, en la zona inferior, hay dos rectángulos pequeños con esquinas redondeadas (estados) dispuestos horizontalmente:

- Estado izquierdo: `inside the museum`
- Estado derecho: `out of the museum`

OPL: Museum Visitor can be **inside the museum** or **out of the museum**.

---

## Figura 6 — Objeto con estados con estados inicial, por defecto y final

Rectángulo verde (`Specification`) con tres estados en su interior dispuestos horizontalmente:

- `preliminary` (izquierda): rectángulo con esquinas redondeadas y borde grueso simple (bold-contour), indicando que es **estado inicial**.
- `approved` (centro): rectángulo con esquinas redondeadas con una flecha abierta apuntando hacia él desde la izquierda, indicando que es **estado por defecto**.
- `cancelled` (derecha): rectángulo con esquinas redondeadas y doble borde concéntrico (double-contour), indicando que es **estado final**.

OPL:

- State **preliminary** of Specification is initial.
- State **approved** of Specification is default.
- State **cancelled** of Specification is final.

---

## Figura 7 — Enlaces transformadores: consumo, resultado, efecto

Tres diagramas OPD dispuestos horizontalmente, cada uno mostrando un tipo distinto de enlace transformador:

**Izquierda — Consumo**: Objeto `File` (rectángulo verde, arriba) conectado al proceso `Deleting` (elipse azul, abajo) mediante una flecha que va desde File hacia Deleting. La punta de flecha está en el extremo del proceso. OPL: Deleting consumes File.

**Centro — Resultado**: Proceso `Creating` (elipse, abajo) conectado al objeto `File` (rectángulo, arriba) mediante una flecha que va desde Creating hacia File. La punta de flecha está en el extremo del objeto. OPL: Creating yields File.

**Derecha — Efecto**: Objeto `File` (rectángulo, arriba) conectado al proceso `Editing` (elipse, abajo) mediante una flecha bidireccional (puntas de flecha en ambos extremos). OPL: Editing affects File.

---

## Tabla 1 — Resumen de enlaces transformadores básicos

| Nombre | Semántica | Ejemplo OPD y OPL | Origen | Destino |
|---|---|---|---|---|
| Enlace de consumo | El proceso consume el objeto. | OPD: `Food` (rectángulo) con flecha hacia `Eating` (elipse). OPL: Eating consumes **Food**. | Objeto consumido (consumed object) | Proceso que consume (consuming process) |
| Enlace de resultado | El proceso genera el objeto. | OPD: `Mining` (elipse) con flecha hacia `Copper` (rectángulo). OPL: Mining yields **Copper**. | Proceso que crea (creating process) | Objeto creado (created object) |
| Enlace de efecto | El proceso afecta al objeto cambiándolo de un estado a otro. | OPD: `Purifying` (elipse) con flecha bidireccional hacia `Copper` (rectángulo). OPL: Purifying affects **Copper**. | Objeto afectado y proceso afectante son ambos origen y destino (affected object and affecting process are both source and destination) |

---

## Figura 8 — Ejemplo de enlace de agente

Diagrama OPD con cinco elementos:

- `Welder` (rectángulo verde, arriba centro): agente humano.
- `Steel Part B` (rectángulo verde, izquierda media): objeto consumido.
- `Steel Part A` (rectángulo verde, izquierda abajo): objeto consumido.
- `Welding` (elipse azul, centro): proceso principal.
- `Steel Part AB` (rectángulo verde, derecha): objeto resultado.

**Enlaces**:

- `Welder` se conecta a `Welding` mediante un **enlace de agente** (línea con círculo negro sólido en el extremo del proceso). El agente habilita sin ser transformado.
- `Steel Part A` y `Steel Part B` se conectan a `Welding` mediante **enlaces de consumo** (flechas hacia el proceso).
- `Welding` se conecta a `Steel Part AB` mediante un **enlace de resultado** (flecha hacia el objeto).

OPL:

- Welder handles Welding.
- Welding consumes Steel Part A and Steel Part B.
- Welding yields Steel Part AB.

---

## Figura 9 — Ejemplo de enlace de instrumento

Diagrama OPD con tres elementos:

- `Insert Set` (rectángulo verde, arriba derecha): objeto con estados `pre-sintered` y `sintered`.
- `Sintering Oven` (rectángulo verde, izquierda): instrumento no humano.
- `Sintering` (elipse azul, abajo centro): proceso.

**Enlaces**:

- `Sintering Oven` se conecta a `Sintering` mediante un **enlace de instrumento** (línea con círculo hueco en el extremo del proceso).
- `Sintering` se conecta a `Insert Set` mediante un **par de enlaces entrada-salida** con estados especificados: flecha de entrada desde el estado `pre-sintered` hacia el proceso, y flecha de salida desde el proceso hacia el estado `sintered`.

OPL:

- Insert Set can be **pre-sintered** or **sintered**.
- Sintering requires Sintering Oven.
- Sintering changes Insert Set from **pre-sintered** to **sintered**.

---

## Tabla 2 — Resumen de enlaces habilitadores básicos

| Nombre | Semántica | Ejemplo OPD y OPL | Origen | Destino |
|---|---|---|---|---|
| Enlace de agente | El agente es un humano o grupo de humanos que habilita la ocurrencia del proceso al que está vinculado pero no es transformado por ese proceso. | OPD: `Welder` (rectángulo) conectado a `Welding` (elipse) con línea terminada en círculo negro sólido. OPL: Welder handles Welding. | Agente — el objeto habilitador (agent – the enabling object) | Proceso habilitado (enabled process) |
| Enlace de instrumento | El instrumento es un objeto inanimado que habilita la ocurrencia del proceso al que está vinculado pero no es transformado por ese proceso. | OPD: `Machine` (rectángulo) conectado a `Manufacturing` (elipse) con línea terminada en círculo hueco. OPL: Manufacturing requires Machine. | Instrumento — el objeto habilitador (instrument – the enabling object) | Proceso habilitado (enabled process) |

---

## Figura 10 — Enlace de resultado correcto (izq.) e incorrecto (der.) hacia objeto con estado inicial

**Diagrama izquierdo (CORRECTO)**: Proceso `P` (elipse azul, arriba) conectado mediante enlace de resultado (flecha) al objeto `A` (rectángulo verde, abajo). El objeto `A` contiene tres estados: `s1`, `s2`, `s3`. El estado `s2` está marcado como inicial (borde grueso, doble contorno). La flecha de resultado apunta al borde del objeto `A` en general, no a un estado específico. OPL: A can be s1, s2, or s3. S2 is initial. P yields A.

**Diagrama derecho (INCORRECTO)**: Misma configuración, pero la flecha de resultado apunta directamente al estado `s2` dentro del objeto `A`, lo cual es incorrecto porque eso significaría que P produce A en el estado s2 específicamente, no que simplemente crea A (cuyo estado inicial es s2 por definición). OPL: A can be s1, s2, or s3. S2 is initial. P yields **s2** A.

La diferencia semántica: cuando el enlace apunta al objeto, el resultado respeta el estado inicial definido; cuando apunta al estado, especifica explícitamente un estado de salida (lo cual es redundante e incorrecto si coincide con el inicial).

---

## Figura 11 — Enlaces de consumo y resultado con estado especificado

Diagrama OPD complejo que muestra un flujo de manufactura:

**Objetos**:

- `Raw Metal Bar` (rectángulo verde con sombra, físico): estados `pre-cut` y `cut`.
- `Machine Operator` (rectángulo verde con sombra, físico): agente humano.
- `Coolant` (rectángulo verde con sombra, físico): instrumento.
- `Part` (rectángulo verde con sombra, físico): estados `pre-tested` y `tested`.

**Procesos**:

- `Cutting` (elipse con borde discontinuo y sombra, ambiental y físico).
- `Machining` (elipse con sombra, físico).
- `Testing` (elipse con borde discontinuo y sombra, ambiental y físico).

**Enlaces**:

- `Cutting` cambia `Raw Metal Bar` de `pre-cut` a `cut` (par entrada-salida con estados especificados).
- `Machining` consume `cut Raw Metal Bar` (enlace de consumo con estado especificado: sale del estado `cut`).
- `Machine Operator` maneja `Machining` (enlace de agente, círculo negro).
- `Machining` requiere `Coolant` (enlace de instrumento, círculo hueco).
- `Machining` produce `pre-tested Part` (enlace de resultado con estado especificado: apunta al estado `pre-tested`).
- `Testing` cambia `Part` de `pre-tested` a `tested` (par entrada-salida).

OPL completo incluido debajo del diagrama.

---

## Tabla 3 — Resumen de enlaces transformadores con estado especificado

| Nombre | Semántica | Ejemplo OPD y OPL | Origen | Destino |
|---|---|---|---|---|
| Enlace de consumo con estado especificado | El proceso consume el objeto si y solo si el objeto está en el estado especificado. | OPD: `Food` con estados, flecha desde estado específico hacia `Eating`. OPL: Eating consumes edible Food. | Estado del consumido (consumee state) | Proceso que consume (consuming process) |
| Enlace de resultado con estado especificado | El proceso genera el objeto en el estado especificado. | OPD: `Mining` con flecha hacia estado específico de `Copper`. OPL: Mining yields raw Copper. | Proceso que crea | Estado del objeto creado |
| Par de enlaces de efecto entrada-salida especificados | El proceso cambia el objeto desde un estado (enlace de entrada) a otro estado (enlace de resultado) vía el par completo. | OPD: `Purifying` con flecha desde estado `raw` de `Copper` (entrada) y flecha hacia estado `pure` (salida). OPL: Purifying changes Copper from raw to pure. | Estado de entrada del afectado | Estado de salida del afectado |
| Par de enlaces de efecto entrada especificada | El proceso cambia el objeto desde un estado especificado a cualquiera de sus otros estados. | OPD: `Testing` con flecha desde estado `awaiting test` de `Sample`. OPL: Testing changes Sample from awaiting test. | Estado fuente del afectado | Proceso afectante / estado de destino |
| Par de enlaces de efecto salida especificada | El proceso cambia el objeto desde cualquier estado a un estado especificado de salida. | OPD: `Cleaning & Painting` con flecha hacia estado `painted` de `Engine Hood`. OPL: Cleaning & Painting changes Engine Hood to painted. | Afectado | Estado de salida del proceso afectante |

---

## Figura 12 — Enlace de instrumento (izq.) vs enlace de instrumento con estado especificado (der.)

**Diagrama izquierdo (sin estado especificado)**:

- `Moving Truck` (rectángulo con sombra, físico): estados `worn out` y `serviced`.
- `Servicing` (elipse con borde discontinuo y sombra, ambiental y físico): cambia Moving Truck de `worn out` a `serviced`.
- `Apartment Content Location` (rectángulo con sombra, físico): estados `old apartment` y `new apartment`.
- `Moving` (elipse con sombra, físico): requiere `Moving Truck` como instrumento (enlace de instrumento genérico, sin estado especificado). Moving cambia Apartment Content Location de `old apartment` a `new apartment`.

**Diagrama derecho (con estado especificado)**:

- Misma estructura, pero el enlace de instrumento de `Moving Truck` a `Moving` sale específicamente del estado `serviced`. El instrumento solo habilita el proceso si está en el estado `serviced`.

OPL diferencia: izquierda dice "Moving requires Moving Truck"; derecha dice "Moving requires **serviced** Moving Truck."

---

## Tabla 4 — Resumen de enlaces habilitadores con estado especificado

| Nombre | Semántica | Ejemplo OPD y OPL | Origen | Destino |
|---|---|---|---|---|
| Enlace de agente con estado especificado | El agente humano habilita el proceso siempre que esté en el estado especificado. | OPD: `Miner` con estados `sick` y `healthy`; enlace de agente sale del estado `healthy` hacia `Copper Mining`. OPL: Healthy Miner handles Copper Mining. | Estado del agente (agent state) | Proceso habilitado (enabled process) |
| Enlace de instrumento con estado especificado | El proceso requiere el instrumento en el estado especificado. | OPD: `Drill` con estados `faulty` y `operational`; enlace de instrumento sale del estado `operational` hacia `Copper Mining`. OPL: Copper Mining requires **operational** Drill. | Estado del instrumento (instrument state) | Proceso habilitado (enabled process) |

---

## Tabla 5 — Resumen de enlaces de evento transformadores

| Nombre | Semántica | Ejemplo OPD y OPL | Origen | Destino |
|---|---|---|---|---|
| Enlace de evento de consumo | El objeto inicia el proceso, el cual, si se ejecuta, consume el objeto. | OPD: `Food` (rectángulo) con flecha hacia `Eating` (elipse); la flecha lleva el símbolo `e` (evento) sobre la línea. Hay también una flecha de retorno desde el proceso hacia el objeto (consumo). OPL: Food initiates Eating, which consumes Food. | Consumido que inicia (initiating consumee) | Proceso iniciado, que consume al consumido que inicia (initiated process, which consumes the initiating consumee) |
| Enlace de evento de efecto | El objeto inicia el proceso, el cual, si se ejecuta, afecta al objeto. | OPD: `Copper` (rectángulo) con flecha-evento hacia `Purifying` (elipse); flecha bidireccional de efecto entre ambos. OPL: Copper initiates Purifying, which affects Copper. | Afectado que inicia (initiating affectee) | Proceso iniciado, que afecta al afectado (initiated process, which affects the initiating affectee) |

NOTA: El enlace de evento es el enlace desde el objeto hacia el proceso; el enlace desde el proceso hacia el objeto no es un enlace de evento.

---

## Tabla 6 — Resumen de enlaces de evento habilitadores

| Nombre | Semántica | Ejemplo OPD y OPL | Origen | Destino |
|---|---|---|---|---|
| Enlace de evento de agente | El agente (humano) tanto inicia como habilita el proceso. El agente necesita existir durante toda la duración del proceso. | OPD: `Miner` (rectángulo) conectado a `Copper Mining` (elipse) con línea que tiene tanto el símbolo `e` (evento) como el círculo negro (agente). OPL: Miner initiates and handles Copper Mining. | Agente que inicia (initiating agent) | Proceso iniciado (initiated process) |
| Enlace de evento de instrumento | El objeto inicia el proceso como instrumento, por lo que no cambia, pero necesita existir durante toda la duración del proceso. | OPD: `Drill` (rectángulo) conectado a `Copper Mining` (elipse) con línea que tiene tanto el símbolo `e` como el círculo hueco (instrumento). OPL: Drill initiates Copper Mining, which requires Drill. | Instrumento que inicia (initiating instrument) | Proceso iniciado (initiated process) |

---

## Tabla 7 — Resumen de enlaces de evento transformadores con estado especificado

| Nombre | Semántica | Ejemplo OPD y OPL | Origen | Destino |
|---|---|---|---|---|
| Enlace de evento de consumo con estado especificado | El objeto en el estado especificado inicia el proceso y es consumido por él. | OPD: `Food` con estados; flecha-evento desde estado específico hacia `Eating`. OPL: Edible Food initiates Eating, which consumes Food. | Estado del consumido (consumee state) | Proceso iniciado (initiated process) |
| Par de enlaces de evento de efecto entrada-salida especificados | El objeto en el estado especificado de entrada inicia el proceso y es transformado al estado de salida. | OPD: `Copper` con estados `raw` y `pure`; flecha-evento desde `raw` hacia `Purifying`, flecha de resultado hacia `pure`. OPL: Raw Copper initiates Purifying, which changes Copper from raw to pure. | Estado fuente del afectado | Proceso iniciado / estado destino del afectado |
| Par de enlaces de evento de efecto entrada especificada | El objeto en el estado especificado inicia el proceso y es cambiado a cualquiera de sus otros estados. | OPD: `Sample` con estados `awaiting test`, `passed`, `failed`; flecha-evento desde `awaiting test` hacia `Testing`. OPL: Awaiting test Sample initiates Testing, which changes Sample from awaiting test. | Estado fuente del afectado | Proceso iniciado |
| Par de enlaces de evento de efecto salida especificada | El objeto en cualquiera de sus estados inicia el proceso y es cambiado al estado de salida especificado. | OPD: `Engine Hood` con estados; flecha-evento desde Engine Hood hacia `Cleaning & Painting`, flecha de resultado hacia estado `painted`. OPL: Engine Hood initiates Cleaning & Painting, which changes Engine Hood to painted. | Afectado | Proceso iniciado / estado destino |

---

## Tabla 8 — Resumen de enlaces de evento habilitadores con estado especificado

| Nombre | Semántica | Ejemplo OPD y OPL | Origen | Destino |
|---|---|---|---|---|
| Enlace de evento de agente con estado especificado | El agente humano en el estado especificado tanto inicia como habilita el proceso. Debe permanecer en ese estado durante toda la duración del proceso. | OPD: `Miner` con estados `sick` y `healthy`; línea desde estado `healthy` hacia `Copper Mining` con símbolo `e` y círculo negro. OPL: Healthy Miner initiates and handles Copper Mining. | Estado del agente (agent state) | Proceso iniciado (initiated process) |
| Enlace de evento de instrumento con estado especificado | El objeto en el estado especificado inicia el proceso y actúa como instrumento. Debe permanecer en ese estado durante toda la duración. | OPD: `Drill` con estados `faulty` y `operational`; línea desde estado `operational` hacia `Copper Mining` con símbolo `e` y círculo hueco. OPL: Operational Drill initiates Copper Mining, which requires operational Drill. | Estado del instrumento (instrument state) | Proceso iniciado (initiated process) |

---

## Tabla 9 — Resumen de enlaces de invocación

| Nombre | Semántica | Ejemplo OPD y OPL | Origen | Destino |
|---|---|---|---|---|
| Enlace de invocación | Tan pronto como el proceso invocante termina, invoca el proceso señalado por el enlace de invocación. | OPD: `Product Finishing` (elipse) conectado a `Product Shipping` (elipse) mediante flecha en zigzag (rayo) que apunta hacia abajo. OPL: Product Finishing invokes Product Shipping. | Proceso que inicia (initiating process) | Otro proceso iniciado (another initiated process) |
| Enlace de auto-invocación | Al completarse el proceso, inmediatamente se invoca a sí mismo. | OPD: `Recurrent Processing` (elipse) con flecha en zigzag que sale y regresa al mismo proceso (bucle). OPL: Recurrent Processing invokes itself. | Proceso que inicia (initiating process) | El mismo proceso (the same process) |

---

## Tabla 10 — Resumen de enlaces transformadores condicionales

| Nombre | Semántica | Ejemplo OPD y OPL | Origen | Destino |
|---|---|---|---|---|
| Enlace de consumo condicional | Si existe una instancia operacional del objeto y el resto de la precondición del proceso se satisface, entonces el proceso se ejecuta y consume la instancia del objeto; de lo contrario, el control de ejecución avanza para iniciar el siguiente proceso. | OPD: `Object` (rectángulo) conectado a `Process` (elipse) con flecha que lleva la letra `c` sobre la línea. OPL: Process occurs if Object exists, in which case Process consumes Object, otherwise Process is skipped. | Objeto condicionante (conditioning object) | Proceso condicionado (conditioned process) |
| Enlace de efecto condicional | Si existe una instancia operacional del objeto y el resto de la precondición se satisface, el proceso se ejecuta y afecta la instancia del objeto; de lo contrario, el control avanza. | OPD: `Object` (rectángulo) conectado a `Process` (elipse) con flecha bidireccional que lleva la letra `c`. OPL: Process occurs if Object exists, in which case Process affects Object, otherwise Process is skipped. | Objeto condicionante | Proceso condicionado |

---

## Figura 13 — Enlace condicional de instrumento (con OPL parcial)

Diagrama OPD con seis elementos, todos ambientales (bordes discontinuos):

- `User` (rectángulo, arriba centro): agente.
- `Signal Booster` (rectángulo, izquierda): instrumento.
- `Cellular Network Signal` (rectángulo, derecha arriba): instrumento.
- `Nearby Mobile Device` (rectángulo, izquierda abajo): objeto condicional.
- `Cellular Network Signal Amplifying` (elipse, centro): proceso principal.
- `Calling Mobile Device` (rectángulo, derecha abajo): instrumento.

**Enlaces**:

- `User` maneja `Cellular Network Signal Amplifying` (enlace de agente, círculo negro).
- `Signal Booster` requiere el proceso (enlace de instrumento, círculo hueco).
- `Cellular Network Signal` requiere el proceso (enlace de instrumento).
- `Calling Mobile Device` requiere el proceso (enlace de instrumento).
- `Nearby Mobile Device` tiene un **enlace condicional de instrumento** hacia el proceso: línea con círculo hueco y letra `c` sobre ella.

OPL: Cellular Network Signal Amplifying occurs if Nearby Mobile Device exists, otherwise Cellular Network Signal Amplifying is skipped.

---

## Tabla 11 — Resumen de enlaces habilitadores condicionales básicos

| Nombre | Semántica | Ejemplo OPD y OPL | Origen | Destino |
|---|---|---|---|---|
| Enlace condicional de agente | El agente habilita el proceso si está presente; de lo contrario, el proceso se omite. | OPD: `Engineer` (rectángulo) con enlace de agente y `c` hacia `Part Designing` (elipse). OPL: Engineer handles Part Designing if Engineer is present, otherwise Part Designing is skipped. | Agente condicionante (conditioning agent) | Proceso condicionado (conditioned process) |
| Enlace condicional de instrumento | El instrumento habilita el proceso si existe; de lo contrario, el proceso se omite. | OPD: `LASER Meter` (rectángulo) con enlace de instrumento y `c` hacia `Precise Measuring` (elipse). OPL: Precise Measuring occurs if LASER Meter exists, otherwise Precise Measuring is skipped. | Instrumento condicionante (conditioning instrument) | Proceso condicionado (conditioned process) |

---

## Tabla 12 — Resumen de enlaces transformadores condicionales con estado especificado

| Nombre | Semántica | Ejemplo OPD y OPL | Origen | Destino |
|---|---|---|---|---|
| Enlace de consumo condicional con estado especificado | El proceso se ejecuta si el objeto está en el estado desde el cual el enlace se origina; de lo contrario, se omite. | OPD: `Raw Material Sample` con estados `pre-approved` y `approved`; enlace con `c` desde estado `pre-approved` hacia `Testing`. OPL: Testing occurs if Raw Material Sample is pre-approved, in which case Raw Material Sample is consumed, otherwise Testing is skipped. | Estado especificado condicionante del objeto (conditioning specified state of the object) | Proceso condicionado (conditioned process) |
| Enlace condicional de efecto entrada-salida especificado | El proceso se ejecuta si el objeto está en el estado de entrada (desde el cual el enlace se origina) y cambia el objeto al estado de salida; de lo contrario, se omite. | OPD: `Raw Material` con estados `pre-tested` y `tested`; enlace con `c` desde estado `pre-tested` hacia `Testing`, flecha de salida hacia `tested`. OPL: Testing occurs if Raw Material is pre-tested, in which case Testing changes Raw Material from pre-tested to tested, otherwise Testing is skipped. | Estado especificado de entrada del objeto | Proceso condicionado / estado destino |
| Enlace condicional de efecto entrada especificada | El proceso se ejecuta si el objeto está en el estado de entrada y lo cambia a cualquiera de sus otros estados. | OPD: `Message` con estados `created` y `delivered`; enlace con `c` desde estado `created` hacia `Delivery Attempting`. OPL: Delivery Attempting occurs if Message is created, in which case Delivery Attempting changes Message from created, otherwise Delivery Attempting is skipped. | Estado especificado de entrada | Proceso condicionado |
| Enlace condicional de efecto salida especificado | El proceso se ejecuta si el objeto existe y lo cambia desde su estado de entrada al estado de salida especificado; de lo contrario, se omite. | OPD: `Suspicious Component` con estados `pre-tested`, `tested`, `stress-tested`; enlace con `c` hacia `Stress Testing`, flecha hacia `stress-tested`. OPL: Stress Testing occurs if Suspicious Component exists, in which case Stress Testing changes Suspicious Component to stress-tested, otherwise Stress Testing is skipped. | Objeto condicionante | Proceso condicionado |

---

## Tabla 13 — Resumen de enlaces habilitadores condicionales con estado especificado

| Nombre | Semántica | Ejemplo OPD y OPL | Origen | Destino |
|---|---|---|---|---|
| Enlace condicional de agente con estado especificado | El agente habilita el proceso si está en el estado especificado; de lo contrario, el proceso se omite. | OPD: `Engineer` con estados `safety design authorized` y `safety design unauthorized`; enlace de agente con `c` desde estado `safety design authorized` hacia `Critical Part Designing`. OPL: Engineer handles Critical Part Designing if Engineer is safety design authorized, otherwise Critical Part Designing is skipped. | Estado especificado condicionante del agente | Proceso condicionado |
| Enlace condicional de instrumento con estado especificado | El instrumento habilita el proceso si está en el estado especificado; de lo contrario, el proceso se omite. | OPD: `LASER Meter` con estados `periodically calibrated` y `manufacturer calibrated`; enlace de instrumento con `c` desde estado `periodically calibrated` hacia `Ultra-Precision Measuring`. OPL: Ultra-Precision Measuring occurs if LASER Meter is periodically calibrated, otherwise Precise Measuring is skipped. | Estado especificado condicionante del instrumento | Proceso condicionado |

---

## Figura 14 — Dos tipos de enlaces estructurales etiquetados

Diagrama OPD con cuatro objetos:

- `Airport` (rectángulo, arriba izquierda).
- `Highway` (rectángulo, arriba derecha).
- `City` (rectángulo, abajo centro).
- `Underwater Tunnel` (rectángulo, abajo derecha).

**Enlaces etiquetados unidireccionales**:

- `Airport` → `City`: etiqueta `serves`. Flecha con punta abierta.
- `Highway` → `City`: etiqueta `surrounds`. Flecha con punta abierta.

**Enlace etiquetado bidireccional**:

- `Highway` ↔ `Underwater Tunnel`: etiqueta de ida `passes through`, etiqueta de vuelta `enables traffic flow in`. Dos flechas en sentidos opuestos.

OPL:

- Airport serves City.
- Highway surrounds City.
- Highway passes through Underwater Tunnel.
- Underwater Tunnel enables traffic flow in Highway.

---

## Figura 15 — Enlace etiquetado bidireccional (izq.) y su equivalente recíproco (der.)

**Diagrama izquierdo**: `Engine` (rectángulo, arriba) y `Gearbox` (rectángulo, abajo) conectados por un enlace bidireccional con dos etiquetas: `is attached to` en ambas direcciones. Son dos flechas separadas con la misma etiqueta.
OPL: Engine is attached to Gearbox. Gearbox is attached to Engine.

**Diagrama derecho**: `Engine` y `Gearbox` conectados por un enlace recíproco con una sola etiqueta `attached`. Una sola línea con la etiqueta recíproca.
OPL: Engine and Gearbox are attached.

Ambos diagramas son semánticamente equivalentes.

---

## Figura 16 — Enlace de relación agregación-participación

Diagrama OPD con un objeto compuesto:

- `Resource Description Framework Statement` (rectángulo, arriba): el todo.
- Conectado mediante un triángulo negro sólido (símbolo de agregación-participación) a tres partes debajo:
  - `Subject` (rectángulo, abajo izquierda)
  - `Predicate` (rectángulo, abajo centro)
  - `Object` (rectángulo, abajo derecha)

Las tres partes están conectadas al triángulo negro mediante líneas rectas. El triángulo tiene su vértice apuntando hacia arriba, hacia el todo.

OPL: Resource Description Framework Statement consists of Subject, Predicate and Object.

---

## Figura 17 — Ejemplo de agregación-participación con conjunto parcial de refinados

Diagrama OPD similar al anterior pero con solo dos partes visibles:

- `Resource Description Framework Statement` (rectángulo, arriba).
- Triángulo negro sólido de agregación, con una **barra horizontal corta** bajo la base del triángulo (indicando colección incompleta: existen refinadores no mostrados).
- Solo dos partes mostradas: `Subject` y `Predicate`.

La barra horizontal bajo el triángulo indica que hay más partes no mostradas en este diagrama.

OPL: Resource Description Framework Statement consists of Subject, Predicate and at least one other part.

---

## Figura 18 — Consumo parcial de agregación

**Diagrama izquierdo**: `Whole` (rectángulo, arriba) con triángulo negro (agregación) hacia cuatro partes: `Part A`, `Part B`, `Part C`, `Part D`. Todas las cuatro partes tienen enlaces de consumo (flechas) hacia el proceso `Consuming` (elipse). El todo y todas las partes participan en el consumo.

**Diagrama derecho**: `Whole` (rectángulo, arriba) con triángulo negro (con corte, parcial) hacia solo dos partes: `Part B` y `Part D`. Ambas conectadas por enlaces de consumo hacia `Consuming`. Muestra que solo algunas partes del todo son consumidas.

---

## Figura 19 — Las cuatro combinaciones de exhibición-caracterización de rasgos

Cuatro mini-diagramas OPD dispuestos en una cuadrícula 2x2:

**Arriba izquierda**: `Object Exhibitor` (rectángulo) con triángulo de exhibición (hueco con triángulo interior) hacia `Attribute` (rectángulo, debajo). Un objeto exhibe un atributo (que también es un objeto).

**Arriba derecha**: `Object Exhibitor` (rectángulo) con triángulo de exhibición hacia `Operation` (elipse, debajo). Un objeto exhibe una operación (que es un proceso).

**Abajo izquierda**: `Process Exhibitor` (elipse) con triángulo de exhibición hacia `Attribute` (rectángulo, debajo). Un proceso exhibe un atributo.

**Abajo derecha**: `Process Exhibitor` (elipse) con triángulo de exhibición hacia `Operation` (elipse, debajo). Un proceso exhibe una operación.

OPL:

- Object Exhibitor exhibits Attribute.
- Process Exhibitor exhibits Attribute.
- Object Exhibitor exhibits Operation.
- Process Exhibitor exhibits Operation.

---

## Figuras 20–23 — Ejemplos de exhibición por tipo

**Figura 20 — Ejemplos de atributos de objeto**: Cuatro pares objeto-atributo dispuestos horizontalmente. Cada par muestra un rectángulo (exhibidor) con triángulo de exhibición hacia un rectángulo inferior (atributo):

- `Material` exhibe `Specific Weight`.
- `Person` exhibe `Age`.
- `Chemical Element` exhibe `Atomic Weight`.
- `Laptop` exhibe `Manufacturer`.

**Figura 21 — Ejemplos de exhibidor de objeto con operación**: Cuatro pares:

- `Airplane` exhibe `Flying` (elipse).
- `Person` exhibe `Walking` (elipse).
- `Printer` exhibe `Printing` (elipse).
- `Dog` exhibe `Watching` (elipse).

**Figura 22 — Ejemplos de exhibidor de proceso con atributo**: Cuatro pares:

- `Diving` (elipse) exhibe `Depth` (rectángulo).
- `Commanding` (elipse) exhibe `Language` (rectángulo).
- `Printing` (elipse) exhibe `Printer` (rectángulo).
- `Striking` (elipse) exhibe `Duration` (rectángulo).

**Figura 23 — Ejemplos de exhibidor de proceso con operación**: Cuatro pares:

- `Moving` (elipse) exhibe `Accelerating` (elipse).
- `Fluctuating` (elipse) exhibe `Stabilizing` (elipse).
- `Transmitting` (elipse) exhibe `Delaying` (elipse).
- `Communicating` (elipse) exhibe `Interfering` (elipse).

---

## Figura 24 — Especializaciones singulares y plurales de objetos y procesos

Cuatro mini-diagramas:

**Arriba izquierda (especialización singular de objeto)**: `Camera` (rectángulo, arriba) con triángulo hueco de generalización y una línea hacia `Digital Camera` (rectángulo, abajo). OPL: Digital Camera is a Camera.

**Arriba derecha (especialización singular de proceso)**: `Food Gathering` (elipse, arriba) con triángulo hueco de generalización y una línea hacia `Hunting` (elipse, abajo). OPL: Hunting is Food Gathering.

**Abajo izquierda (especialización plural de objeto)**: `Camera` (rectángulo, arriba) con triángulo de generalización y dos líneas hacia `Analog Camera` y `Digital Camera` (rectángulos, abajo). OPL: Analog Camera and Digital Camera are Cameras.

**Abajo derecha (especialización plural de proceso)**: `Food Gathering` (elipse, arriba) con triángulo de generalización y dos líneas hacia `Hunting` y `Fishing` (elipses, abajo). OPL: Hunting and Fishing are Food Gathering.

---

## Figura 25 — El atributo discriminante Travelling Medium y sus especializaciones

Diagrama OPD jerárquico:

**Nivel superior**: `Vehicle` (rectángulo, arriba).

**Nivel de atributo**: `Vehicle` exhibe (triángulo de exhibición) `Travelling Medium` (rectángulo), que contiene tres estados: `ground`, `air`, `water surface`.

**Nivel de especialización**: `Vehicle` se generaliza (triángulo hueco) en tres especializaciones: `Car`, `Aircraft`, `Ship`.

**Nivel de atributos heredados**: Cada especialización exhibe su propia copia de `Travelling Medium`, pero con un solo estado (el valor discriminante correspondiente):

- `Car` exhibe `Travelling Medium` con estado `ground`.
- `Aircraft` exhibe `Travelling Medium` con estado `air`.
- `Ship` exhibe `Travelling Medium` con estado `water surface`.

OPL:

- Vehicle exhibits Travelling Medium.
- Travelling Medium of Vehicle can be ground, air, and water surface.
- Car, Aircraft, and Ship are Vehicles.
- Travelling Medium of Car is ground.
- Travelling Medium of Aircraft is air.
- Travelling Medium of Ship is water surface.

---

## Figura 26 — Clasificación-instanciación con rango de valores

**Diagrama izquierdo (clase)**: `Adult` (rectángulo, arriba) con triángulo de exhibición (hueco con triángulo interior) hacia tres atributos:

- `Gender` con estados `female` y `male`.
- `Height [cm]` con estado de rango `120..240`.
- `Weight [kg]` con estado de rango `40..240`.

**Diagrama derecho (instancia)**: `Adult` (rectángulo, arriba) con triángulo de clasificación (hueco con círculo) hacia `Jack Robinson : Adult` (rectángulo con nombre de instancia y clase). Esta instancia exhibe los mismos tres atributos, pero con valores concretos:

- `Gender`: estado `male`.
- `Height [cm]`: valor `185`.
- `Weight [kg]`: valor `88`.

OPL clase: Adult exhibits Gender, Height in cm, and Weight in kg. Gender of Adult can be female or male. Height in cm of Adult ranges from 120 to 240. Weight in kg of Adult ranges from 40 to 240.

OPL instancia: Jack Robinson is an instance of Adult. Gender of Jack Robinson is male. Height in cm of Jack Robinson is 185. Weight in kg of Jack Robinson is 88.

---

## Figura 27 — Estado de atributo como valor: modelos conceptual vs operacional

**Diagrama izquierdo (modelo conceptual/clase)**: `Metal Powder Mixture` (rectángulo, arriba) con triángulo de exhibición hacia `Specific Weight [gr/cm3]` (rectángulo), que contiene un estado de rango: `7.545..7.573`.

**Diagrama derecho (modelo operacional/instancia)**: `Mixture Lot #7545 : Metal Powder Mixture` (rectángulo, arriba) con triángulo de clasificación desde `Metal Powder Mixture`. Exhibe `Specific Weight [gr/cm3]` con un valor concreto: `7.555`.

OPL:

- Metal Powder Mixture exhibits Specific Weight in g/cm3.
- Specific Weight in g/cm3 of Metal Powder Mixture ranges from 7.545 to 7.573.
- Mixture Lot #7545 is an instance of Metal Powder Mixture.
- Specific Weight in g/cm3 of Mixture Lot #7545 is 7.555.

---

## Tabla 14 — Resumen de relaciones y enlaces estructurales

| Relación estructural (Forward-Reverse) | Símbolo OPD | OPL Forward (refineable-to-refinee) | OPL Reverse (refinee-to-refineable) |
|---|---|---|---|
| **Agregación**-Participación | Triángulo negro sólido. `Whole` arriba, `Part A` y `Part B` abajo. | Whole consists of Part A and Part B. | — |
| **Exhibición**-Caracterización | Triángulo hueco con triángulo interior. `Exhibitor` arriba, `Attribute A` y `Operation B` abajo. | Exhibitor exhibits Attribute A as well as Operation B. | — |
| **Generalización**-Especialización | Triángulo hueco vacío. `General Thing` arriba, `Specialization A` y `Specialization B` abajo. | — | Specialization A and Specialization B are General Thing. |
| **Clasificación**-Instanciación | Triángulo hueco con círculo interior. `Class` arriba, `Instance A` e `Instance B` abajo. | — | Instance A and Instance B are instances of Class. |
| Etiquetado unidireccional [Etiquetado nulo unidireccional] | Línea con etiqueta `tag-name` y flecha, de `Source` a `Destination`. | Source tag-name Destination. [Source relates to Destination.] | — |
| Etiquetado bidireccional | Línea con dos etiquetas: `a-to-b tag` y `b-to-a tag`, entre `A` y `B`. | A a-to-b tag B. B b-to-a tag A. | — |
| Etiquetado recíproco [Etiquetado nulo recíproco] | Línea con etiqueta `reciprocal tag` entre `A` y `B`. | A and B are reciprocal tag. [A and B are related.] | — |

---

## Figura 28 — Ejemplo de enlace de caracterización con estado especificado

Diagrama OPD jerárquico:

- `Vehicle` (rectángulo, arriba) exhibe `Travelling Medium` (rectángulo, abajo centro) con tres estados: `ground`, `air`, `water surface`.
- `Vehicle` se generaliza en `Car`, `Aircraft`, `Ship`.
- Cada especialización tiene un enlace de exhibición con estado especificado hacia `Travelling Medium`:
  - `Car` exhibe el estado `ground` de `Travelling Medium`.
  - `Aircraft` exhibe el estado `air`.
  - `Ship` exhibe el estado `water surface`.

La diferencia con la Figura 25 es que aquí cada especialización apunta directamente a un estado de un atributo compartido, en lugar de tener su propia copia del atributo.

---

## Tabla 15 — Resumen de relaciones y enlaces estructurales con estado especificado

Tabla con tres filas principales por direccionalidad (unidireccional, bidireccional, recíproco) y tres columnas por tipo de especificación de estado (source state-specified, destination state-specified, source-and-destination state-specified).

Cada celda muestra:

- Un mini-diagrama con objetos `A` y `B`, donde `A` tiene estado `s` y/o `B` tiene estado `s`/`sb`.
- La oración OPL correspondiente.

**Unidireccional**: S A tag-name B. | B tag-name s A. | Sa A tag-name sb B.
**Bidireccional**: S A f-tag-name B, B b-tag-name s A. | Sa A f-tag-name sb B, Sb B b-tag-name sa A.
**Recíproco**: B and s A are recip-tag-name. | Sa A and sb B are recip-tag-name.

---

## Figura 29 — Asociación de valores de atributo con objetos vía enlace estructural con estado especificado

Diagrama OPD complejo:

**Objeto principal**: `Check` (rectángulo, derecha) con cuatro estados verticales: `blank`, `signed`, `endorsed`, `cashed & cancelled`.

**Atributo exhibido**: `Check` exhibe `Keeper` (rectángulo). `Keeper` tiene tres estados: `payer`, `payee`, `financial institution`.

**Objetos asociados**: `Payer`, `Payee`, `Bank` (rectángulos).

**Enlaces estructurales con estado especificado**: Cada estado de `Keeper` se conecta a un objeto específico mediante enlace etiquetado unidireccional:

- Estado `payer` de `Keeper` → `Payer` (Payer Keeper relates to Payer)
- Estado `payee` de `Keeper` → `Payee` (Payee Keeper relates to Payee)
- Estado `financial institution` de `Keeper` → `Bank` (Financial institution Keeper relates to Bank)

**Proceso**: `Check-Based Paying` (elipse azul, centro derecha) está conectado al flujo.

---

## Figura 30 — Enlace estructural etiquetado con estado especificado en origen y destino

Diagrama OPD:

- `Water` (rectángulo, arriba) exhibe dos atributos:
  - `Phase` con estados: `solid`, `liquid`, `gas`.
  - `Temperature [Celsius]` con estados: `below zero`, `between zero and 100`, `above 100`.

- Tres enlaces etiquetados `exists for the range of` conectan estados de `Phase` con estados de `Temperature`:
  - `solid` → `below zero`
  - `liquid` → `between zero and 100`
  - `gas` → `above 100`

OPL:

- Water exhibits Phase and Temperature in Celsius.
- Phase of Water can be solid, liquid or gas.
- Temperature of Water in Celsius can be below zero, between zero and 100, or above 100.
- Solid Phase exists for the range of below zero Temperature in Celsius.
- Liquid Phase exists for the range of between zero and 100 Temperature in Celsius.
- Gas Phase exists for the range of above 100 Temperature in Celsius.

---

## Figura 31 — Ejemplos de multiplicidad de objetos

**Diagrama izquierdo (enlace etiquetado con multiplicidad)**: `Factory` (rectángulo) conectado a `Shopfloor` (rectángulo) mediante enlace etiquetado `comprises` con multiplicidad `3` sobre el extremo del destino. OPL: Factory comprises **3** Shopfloors.

**Diagrama derecho (agregación con multiplicidad)**: `Printer` (rectángulo, arriba) con triángulo negro de agregación (con corte, parcial) hacia dos partes:

- `Colour Cartridge` con multiplicidad `3` (tres unidades).
- `Black Cartridge` (sin multiplicidad explícita, una unidad).

OPL: Printer consists of **3** Colour Cartridges, Black Cartridge and other parts.

---

## Tabla 16 — Resumen de opcionalidad de enlaces

| Límites inferior y superior (q_min..q_max) | Símbolo de restricción de participación y frase OPL | Ejemplo OPD y OPL |
|---|---|---|
| 0..1 | `?` — an optional | OPD: `Car` → `Sunroof` con etiqueta `has` y símbolo `?`. OPL: Car has an optional Sunroof. |
| 0..* | `*` — optional (none to many) | OPD: `Car` → `Airbag` con etiqueta `is equipped with` y símbolo `*`. OPL: Car is equipped with optional Airbags. |
| 1..1 | (none) — sin símbolo | OPD: `Car` → `Steering Wheel` con etiqueta `is steered by`. OPL: Car is steered by Steering Wheel. |
| 1..* | `+` — at least one | OPD: `Car` → `Spare Tire` con etiqueta `carries` y símbolo `+`. OPL: Car carries at least one Spare Tire. |

---

## Figura 32 — Ejemplos de multiplicidad de objetos con rangos y parámetros

**Diagrama superior**: `Machine Center` (rectángulo) conectado a `Machine` (rectángulo) mediante enlace etiquetado `controls` con multiplicidad `3..5, 8..10`. OPL: Machine Center controls **3 to 5** or **8 to 10** Machines.

**Diagrama inferior**: `Machine Center` conectado a `Machine` mediante enlace etiquetado `controls` con multiplicidad `2, 3*n; n<=4`. OPL: Machine Center controls **2** or **3*n** Machines, where n<=4.

---

## Figura 33 — Multiplicidad de objetos: expresiones aritméticas y restricciones

Diagrama OPD complejo de mantenimiento aeronáutico:

**Objetos**:

- `Jet Engine` (rectángulo con sombra, físico): estados `used` y `refurbished`. Consiste de `b` Installed Blades.
- `Blade` (rectángulo con sombra, físico, con borde discontinuo, ambiental): estados `inspected` y `new`.
- `Installed Blade` (rectángulo con borde discontinuo): parte del Jet Engine.
- `Dismantled Blade` (rectángulo con sombra y borde discontinuo).
- `Aviation Engine Mechanic` (rectángulo): agente, multiplicidad `k=2..4`.
- `Blade Fastening Tool` (rectángulo): instrumento, multiplicidad `k`.
- `Aerospace Engineer` (rectángulo): agente, multiplicidad `1..2` y `0..1` (condicional).

**Procesos**:

- `Blade Replacing` (elipse con sombra, físico): proceso central.
- `Blade Inspecting` (elipse con sombra y borde discontinuo).
- `Purchasing` (elipse con borde discontinuo).

**Enlaces con multiplicidades aritméticas**:

- k=2 to 4 Aviation Engine Mechanics handle Blade Replacing.
- Blade Replacing requires k Blade Fastening Tools.
- Blade Replacing consumes b inspected Blades and b-1 new Blades.
- Blade Replacing yields b Dismantled Blades.
- Blade Inspecting consumes b, a<=b inspected Blades.
- Purchasing yields many new Blades.
- Restricción: a<=b.

---

## Figura 34 — Ejemplo de restricciones parametrizadas múltiples

Diagrama OPD:

- `Airplane` (rectángulo, arriba) con triángulo de agregación hacia tres partes:
  - `Body` (rectángulo): multiplicidad implícita 1.
  - `Wing` (rectángulo): multiplicidad `2`.
  - `Engine` (rectángulo): multiplicidad `e; e >= 1, e = b+2*w`.

- `Engine` está conectado a `Body` mediante enlace etiquetado `are attached to` con multiplicidad `b, b in {0, 1}`.
- `Engine` está conectado a `Wing` mediante enlace etiquetado `are attached to` con multiplicidad `w, 0 <= w <= 3`.

OPL:

- Airplane consists of Body, 2 Wings, and e Engines, where e >= 1, e = b+2*w.
- b Engines are attached to Body, where b in {0, 1}.
- w Engines are attached to Wing, where 0 <= w <= 3.

---

## Figura 35 — AND lógico para enlaces de agente e instrumento

**Diagrama izquierdo (AND de instrumentos)**: Tres objetos `Key A`, `Key B`, `Key C` (rectángulos) conectados cada uno mediante enlace de instrumento (círculo hueco) al proceso `Safe Opening` (elipse). `Safe` (rectángulo) con estados `closed` y `open` es afectado por el proceso. Todos los instrumentos son necesarios simultáneamente (AND implícito).

OPL: Safe can be closed or open. Safe Opening requires Key A, Key B, and Key C. Safe Opening changes Safe from closed to open.

**Diagrama derecho (AND de agentes)**: `Safe Owner A` y `Safe Owner B` (rectángulos) conectados cada uno mediante enlace de agente (círculo negro) al proceso `Safe Opening`. Ambos agentes son necesarios simultáneamente.

OPL: Safe can be closed or open. Safe Owner A and Safe Owner B handle Safe Opening. Safe Opening changes Safe from closed to open.

---

## Figura 36 — AND lógico para enlaces de resultado y consumo

**Diagrama izquierdo (AND de resultados)**: `Chef` (rectángulo) maneja `Meal Preparing` (elipse, enlace de agente). `Meal Preparing` produce tres resultados simultáneamente: `Starter`, `Entree`, `Dessert` (tres rectángulos, cada uno con enlace de resultado). OPL: Chef handles Meal Preparing. Meal Preparing yields Starter, Entree and Dessert.

**Diagrama derecho (AND de consumos)**: `Starter`, `Entree`, `Dessert` (tres rectángulos) son todos consumidos por `Meal Eating` (elipse). `Diner` (rectángulo) es afectado. Los tres son consumidos simultáneamente. OPL: Meal Eating affects Diner. Meal Eating consumes Dessert, Entree and Starter.

---

## Figura 37 — AND lógico para enlace de efecto y pares de enlaces entrada-salida

**Diagrama izquierdo (efecto sin estados)**: `Central Bank` (rectángulo) maneja `Interest Rate Changing` (elipse). El proceso afecta simultáneamente tres objetos: `Interest Rate`, `Price Index`, `Exchange Rate` (todos rectángulos, cada uno con enlace de efecto bidireccional). OPL: Central Bank handles Interest Rate Changing. Interest Rate Changing affects Exchange Rate, Price Index, and Interest Rate.

**Diagrama derecho (efecto con estados especificados)**: Misma estructura pero con estados. `Interest Rate` tiene estados `low` y `high`; `Price Index` tiene estados `low` y `high`; `Exchange Rate` tiene estados `low` y `high`. El proceso `Interest Rate Raising` cambia los tres simultáneamente:

- Exchange Rate de `low` a `high`.
- Price Index de `low` a `high`.
- Interest Rate de `low` a `high`.

---

## Figura 38 — OR lógico (izq.) y XOR lógico (der.) para enlace de agente

**Diagrama izquierdo (OR)**: `Safe Owner A` y `Safe Owner B` conectados a `Safe Opening` mediante enlaces de agente con un **arco de OR** (dos arcos discontinuos concéntricos) que une los dos enlaces en el extremo del proceso. El arco doble indica que al menos uno de los agentes participa.
OPL: At least one of Safe Owner A and Safe Owner B handles Safe Opening.

**Diagrama derecho (XOR)**: Misma configuración pero con un **arco de XOR** (arco discontinuo simple). Exactamente uno de los agentes participa.
OPL: Exactly one of Safe Owner A and Safe Owner B handles Safe Opening.

En ambos casos, `Safe` tiene estados `closed` y `open`, y el proceso cambia Safe de closed a open.

---

## Tabla 17 — Resumen de XOR y OR para abanicos convergentes de consumo y resultado

| Tipo | XOR | OR |
|---|---|---|
| **Abanico convergente de consumo** | OPD: Tres objetos `A`, `B`, `C` con flechas de consumo hacia proceso `P`, unidas por arco XOR (arco discontinuo simple). OPL: P consumes exactly one of A, B, or C. | OPD: Misma configuración con arco OR (dos arcos discontinuos concéntricos). OPL: P consumes at least one of A, B, or C. |
| **Abanico convergente de resultado** | OPD: Tres procesos `P`, `Q`, `R` con flechas de resultado hacia objeto `B`, unidas por arco XOR. OPL: Exactly one of P, Q, or R yields B. | OPD: Misma configuración con arco OR. OPL: At least one of P, Q, or R yields B. |

---

## Tabla 18 — Resumen de XOR y OR para abanicos divergentes de consumo y resultado

| Tipo | XOR | OR |
|---|---|---|
| **Abanico divergente de consumo** | OPD: Objeto `B` con flechas de consumo divergentes hacia procesos `P`, `Q`, `R`, unidas por arco XOR. OPL: Exactly one of P, Q, or R consumes B. | OPD: Misma configuración con arco OR. OPL: At least one of P, Q, or R consumes B. |
| **Abanico divergente de resultado** | OPD: Proceso `P` con flechas de resultado divergentes hacia objetos `A`, `B`, `C`, unidas por arco XOR. OPL: P yields exactly one of A, B, or C. | OPD: Misma configuración con arco OR. OPL: P yields at least one of A, B, or C. |

---

## Tabla 19 — Resumen de XOR y OR para abanicos de enlace de efecto

| Tipo | XOR | OR |
|---|---|---|
| **Abanico de efecto múltiples objetos** | OPD: Tres objetos `A`, `B`, `C` con flechas bidireccionales (efecto) hacia proceso `P`, unidas por arco XOR. OPL: P affects exactly one of A, B, or C. | OPD: Misma configuración con arco OR. OPL: P affects at least one of A, B, or C. |
| **Abanico de efecto múltiples procesos** | OPD: Tres procesos `P`, `Q`, `R` con flechas bidireccionales hacia objeto `B`, unidas por arco XOR. OPL: Exactly one of P, Q, or R affects B. | OPD: Misma configuración con arco OR. OPL: At least one of P, Q, or R affects B. |

---

## Tabla 20 — Resumen de abanicos de enlaces de agente e instrumento

| Tipo | XOR | OR |
|---|---|---|
| **Abanico de enlace de agente** | OPD: Objeto `B` (rectángulo) con enlaces de agente (círculos negros) hacia procesos `P`, `Q`, `R` (elipses), unidos por arco XOR. OPL: B handles exactly one of P, Q, or R. | OPD: Misma configuración con arco OR. OPL: B handles at least one of P, Q, or R. |
| **Abanico de enlace de instrumento** | OPD: Objeto `B` (rectángulo) con enlaces de instrumento (círculos huecos) hacia procesos `P`, `Q`, `R`, unidos por arco XOR. OPL: Exactly one of P, Q, or R requires B. | OPD: Misma configuración con arco OR. OPL: At least one of P, Q, or R requires B. |

---

## Tabla 21 — Resumen de abanicos de enlaces de invocación

| Tipo | XOR | OR |
|---|---|---|
| **Abanico divergente de invocación** | OPD: Proceso `P` con dos flechas zigzag (invocación) divergentes hacia `Q` y `R`, unidas por arco XOR. OPL: P invokes exactly one Q or R. | OPD: Misma configuración con arco OR. OPL: P invokes at least one of Q or R. |
| **Abanico convergente de invocación** | OPD: Procesos `P` y `Q` con flechas zigzag convergentes hacia `R`, unidas por arco XOR. OPL: Exactly one of P or Q invokes R. | OPD: Misma configuración con arco OR. OPL: At least one of P or Q invokes R. |

---

## Figura 39 — Ejemplos de enlaces XOR y OR con estado especificado

**Diagrama izquierdo (XOR con estado especificado en origen)**: Objeto `B` (rectángulo) con estados `s1`, `s2`. Tres procesos `P`, `Q`, `R`. Los enlaces de instrumento salen del estado `s2` de `B`, conectados por arco XOR. OPL: Exactly one of P, Q, or R requires **s2** B.

**Diagrama derecho (OR con estado especificado en destino)**: Proceso `P` (elipse) produce resultado hacia tres objetos/estados: estado `s3` de `A`, objeto `B`, y estado `s5` de `C`, conectados por arco OR. OPL: P yields at least one of **s3** A, B, or **s5** C.

---

## Tabla 22 — Abanicos de enlace de efecto con evento y condición

| Tipo | Evento | Condición |
|---|---|---|
| OPD | Objeto `B` con estados, flechas bidireccionales (efecto) con símbolo `e` hacia procesos `P`, `Q`, `R`, unidos por arco XOR. | Objeto `B`, flechas bidireccionales con símbolo `c` hacia procesos `P`, `Q`, `R`, unidos por arco XOR. |
| OPL (Evento) | B initiates exactly one of P, Q, or R, in which case the occurring process affects B. | — |
| OPL (Condición) | — | Exactly one of P, Q, or R occurs if B exists, in which case the occurring process affects B, otherwise these processes are skipped. |

---

## Tabla 23 — Abanicos de enlaces modificados por control con y sin estado especificado

Tabla que muestra combinaciones de:

- Tipos de enlace: consumo, agente, instrumento.
- Modificadores: evento (`e`), condición (`c`).
- Con y sin estado especificado.

Cada celda contiene un mini-OPD y la oración OPL correspondiente. El patrón general es que el modificador de evento (`e`) añade "initiates" y el modificador de condición (`c`) añade "occurs if ... exists, otherwise ... is skipped". El estado especificado prefija el nombre del estado al objeto.

---

## Figura 40 — Equivalencia entre enlace de resultado y conjunto de enlaces de resultado XOR con estado especificado

**Diagrama izquierdo**: Proceso `P` (elipse) con un solo enlace de resultado (flecha) hacia objeto `B` (rectángulo con estados `s1`, `s2`, `s3`). La flecha apunta al objeto en general, no a un estado específico. OPL: B can be s1, s2, or s3. P yields B.

**Diagrama derecho**: Proceso `P` con tres enlaces de resultado separados, cada uno apuntando a un estado distinto de `B` (`s1`, `s2`, `s3`), unidos por arco XOR (arco discontinuo simple). OPL: B can be s1, s2, or s3. P yields exactly one of s1 B, s2 B, or s3 B.

Ambos son semánticamente equivalentes: un enlace de resultado a un objeto con estados implica un XOR sobre todos los estados posibles.

---

## Figura 41 — Ejemplos de creación probabilística de objetos con estado especificado

**Diagrama izquierdo**: Proceso `P` con tres enlaces de resultado hacia estados de objeto `B`:

- Hacia `s1 B` con probabilidad `Pr=0.32`.
- Hacia `s2 B` con probabilidad `Pr=0.24`.
- Hacia `s3 B` con probabilidad `Pr=0.44`.
Las probabilidades suman 1.0. Arco XOR une los enlaces.

**Diagrama derecho**: Proceso `P` con tres enlaces de resultado:

- Hacia objeto `A` con probabilidad `Pr=0.3`.
- Hacia objeto `B` con probabilidad `Pr=q`.
- Hacia estado `sc1` de objeto `C` con probabilidad `Pr=0.7-q`.
Arco XOR. Las probabilidades también suman 1.0.

---

## Figura 42 — Objetos con y sin estados especificados como orígenes y destinos de abanico probabilístico

Tres diagramas:

**Diagrama superior**: Proceso `P` con cinco enlaces de resultado probabilísticos divergentes hacia:

- Objeto `A` con Pr=0.3
- Objeto `B` con Pr=0.2
- Estado `sc1` de `C` con Pr=0.1
- Estado `sd1` de `D` con Pr=0.25
- Estado `sd2` de `D` con Pr=0.15

**Diagrama medio**: Objeto `A` (sin estados) con tres enlaces de consumo divergentes hacia procesos `P`, `Q`, `R` con probabilidades `Pr=p`, `Pr=q`, `Pr=1-p-q` respectivamente. Arco XOR.
OPL: P with probability p, Q with probability q, or R with probability 1-p-q consumes A.

**Diagrama inferior**: Objeto `A` con estados `s1`, `s2`. Tres enlaces de consumo con estado especificado desde estado `s2` hacia procesos `P`, `Q`, `R` con probabilidades `Pr=p`, `Pr=q`, `Pr=1-p-q`. Arco XOR.
OPL: P with probability p, Q with probability q, or R with probability 1-p-q consumes s2 A.

---

## Figura 43 — Trayectorias de ejecución y etiquetas de ruta

**Diagrama izquierdo (sin ejecución visual)**: Objeto `Water` (rectángulo) con estados `ice`, `liquid`, `gas`. Proceso `Heating` (elipse, abajo). Seis enlaces de entrada-salida con etiquetas de ruta:

- `ice-to-liq`: entrada desde `ice`, salida hacia `liquid`.
- `ice-to-gas`: entrada desde `ice`, salida hacia `gas`.
- `liq-to-gas`: entrada desde `liquid`, salida hacia `gas`.
Y las inversas. Cada par de flechas (entrada y salida) lleva la misma etiqueta de ruta.

**Diagrama derecho (con indicación visual de ejecución)**: Mismo diagrama pero el proceso `Heating` está sombreado (azul sólido) indicando ejecución activa, y las trayectorias activas están resaltadas con puntos rojos.

OPL:

- Water can be ice, liquid, or gas.
- Following path ice-to-liq, Heating changes Water from ice to liquid.
- Following path liq-to-gas, Heating changes Water from liquid to gas.

---

## Figura 44 — Etiquetas de ruta en enlaces de consumo y resultado

Diagrama OPD:

- Tres objetos de entrada: `Tomato`, `Cucumber`, `Meat` (rectángulos).
- Proceso: `Food Preparing` (elipse, centro).
- Tres objetos de salida: `Salad`, `Stew`, `Steak` (rectángulos).

**Etiquetas de ruta**:

- Ruta `herbivore`: consume `Tomato` y `Cucumber`, produce `Salad`.
- Ruta `carnivore`: consume `Meat`, produce `Stew` y `Steak`.

Cada enlace de consumo y resultado lleva la etiqueta de la ruta correspondiente (`herbivore` o `carnivore`).

OPL:

- Following path carnivore, Food Preparing consumes Meat.
- Following path herbivore, Food Preparing consumes Cucumber and Tomato.
- Following path carnivore, Food Preparing yields Stew and Steak.
- Following path herbivore, Food Preparing yields Salad.

---

## Figura 45 — Objeto con estados con todos los estados expresados (izq.) y versión parcialmente suprimida (der.)

**Diagrama izquierdo**: Objeto `A` (rectángulo) con cinco estados visibles: `s1`, `s2`, `s3`, `s4`, `s5`. Proceso `P` (elipse) cambia A de `s1` a `s3` (par entrada-salida).
OPL: A can be s1, s2, s3, s4, or s5. P changes A from s1 to s3.

**Diagrama derecho**: Mismo objeto `A` pero solo mostrando los estados relevantes `s1` y `s3`, más una indicación visual (ellipsis o borde cortado) de que existen más estados. Proceso `P` cambia A de `s1` a `s3`.
OPL: A can be s1, s3, or other states. P changes A from s1 to s3.

Ambos son equivalentes; la versión derecha usa supresión de estados para simplificar el diagrama.

---

## Figura 46 — Ejemplo genérico de in-zooming en nuevo diagrama

**Diagrama izquierdo (SD)**: Proceso `Processing` (elipse) con cinco objetos conectados:

- `Agent` (rectángulo): maneja Processing (enlace de agente).
- `Instrument` (rectángulo): requerido por Processing (enlace de instrumento).
- `Consumee` (rectángulo): consumido por Processing.
- `Affectee` (rectángulo): afectado por Processing (enlace de efecto bidireccional).
- `Resultee` (rectángulo): producido por Processing (enlace de resultado).

**Diagrama derecho (SD1, in-zoomed)**: El proceso `Processing` se descompone (in-zoom) mostrando dos subprocesos dentro de la elipse ampliada:

- `A Subprocessing` (elipse interna, arriba).
- `B Subprocessing` (elipse interna, abajo).
Los subprocesos están en secuencia (A antes que B, por posición vertical).

Redistribución de enlaces:

- `Instrument` sigue conectado a `Processing` (nivel externo).
- `Agent` maneja `A Subprocessing`.
- `A Subprocessing` consume `Consumee`.
- `Processing` (nivel externo) afecta `Affectee`.
- `B Subprocessing` produce `Resultee`.

OPL SD: Agent handles Processing. Processing requires Instrument. Processing consumes Consumee. Processing affects Affectee. Processing yields Resultee.

OPL SD1: Processing requires Instrument. Processing affects Affectee. Processing zooms into A Subprocessing and B Subprocessing in that sequence. Agent handles A Subprocessing. A Subprocessing consumes Consumee. B Subprocessing yields Resultee.

---

## Figura 47 — Proceso Check-Based Paying con in-zooming exponiendo cuatro subprocesos secuenciales

Diagrama OPD complejo con dos niveles:

**Nivel SD**: `Check` exhibe `Keeper`. `Check` tiene estados `blank`, `signed`, `endorsed`, `cashed & cancelled`. `Keeper` tiene estados `payer`, `payee`, `financial institution`. Proceso principal: `Check-Based Paying`.

**Nivel SD1 (in-zoomed)**: `Check-Based Paying` descompuesto en cuatro subprocesos secuenciales (de arriba a abajo):

1. `Writing & Signing`: cambia Check de `blank` a `signed`. `Payer` maneja este subproceso.
2. `Delivering & Accepting`: cambia Keeper de `payer` a `payee`. `Payer` maneja.
3. `Endorsing & Submitting`: cambia Check de `signed` a `endorsed` y Keeper de `payee` a `financial institution`.
4. `Cashing & Cancelling`: cambia Check de `endorsed` a `cashed & cancelled` y Keeper de `financial institution` a `payer`. `Bank` maneja.

Incluye OPL extenso que describe toda la secuencia de transiciones de estado.

---

## Figura 48 — Enlace de invocación (izq.) y enlace de invocación implícita (der.)

**Diagrama izquierdo (invocación explícita)**: `Cleaning` (elipse) afecta `Product` (rectángulo, enlace de efecto bidireccional). `Cleaning` invoca `Coating` (elipse) mediante flecha zigzag. `Coating` también afecta `Product`.
OPL: Cleaning affects Product. Cleaning invokes Coating. Coating affects Product.

**Diagrama derecho (invocación implícita vía in-zooming)**: Proceso `Finishing` (elipse grande) que contiene dos subprocesos: `Cleaning` y `Coating`, en esa secuencia. `Product` está fuera, conectado por enlace de efecto. La secuencia vertical implica invocación: Cleaning termina e invoca implícitamente a Coating.
OPL: Finishing affects Product. Finishing zooms into Cleaning and Coating, in that sequence.

---

## Figura 49 — Orden parcial de subprocesos e invocación paralela implícita

Proceso `Processing` (elipse grande) que contiene siete subprocesos dispuestos en tres niveles verticales:

- **Nivel 1** (arriba): `A` (solo).
- **Nivel 2**: `B` y `C` (paralelos, al mismo nivel horizontal).
- **Nivel 3**: `D` (solo, secuencial después de B y C).
- **Nivel 4** (abajo): `E`, `F`, `G` (paralelos, al mismo nivel horizontal).

La posición vertical determina la secuencia; la posición horizontal al mismo nivel indica paralelismo.

OPL: Processing zooms into A, parallel B and C, D, and parallel E, F, and G, in that sequence.

---

## Tabla 24 — Resumen de enlaces de invocación implícitos

| Nombre | Semántica | Ejemplo OPD y OPL | Origen | Destino |
|---|---|---|---|---|
| **Enlace de invocación implícita** | Al completarse un subproceso dentro del contexto de un proceso in-zoomed, inmediatamente invoca el/los subprocesos debajo. | OPD: Proceso `Product Terminating` (elipse) contiene `Product Finishing` y `Product Shipping` en secuencia vertical. `Product` conectado externamente. OPL: Product Terminating zooms into Product Finishing and Product Shipping, in that sequence. | Proceso iniciante, cuyo punto superior de elipse está por encima del punto superior del proceso iniciado | Proceso iniciado, cuyo punto superior de elipse está por debajo del punto superior del proceso iniciante |
| **Conjunto de enlaces de invocación paralela implícita** | Subprocesos cuyas elipses tienen puntos superiores a la misma altura se inician en paralelo. | OPD superior: `Processing` contiene `A` y `B` al mismo nivel. OPL: Processing zooms into parallel A and B. OPD inferior: `Processing` contiene `A` (arriba) y `B`, `C` (mismo nivel, abajo). OPL: Processing zooms into A and parallel B and C, in that sequence. | Proceso iniciante | Conjunto de procesos iniciados al mismo nivel |

---

## Figura 50 — Distribución de enlaces en in-zooming

**Diagrama izquierdo (antes de distribución)**: Objeto `A` (rectángulo) maneja proceso `P` (elipse, enlace de agente). Objeto `B` (rectángulo) es instrumento de `P` (enlace de instrumento). Dentro de `P`: subprocesos `P1`, `P2`, `P3` en secuencia.
OPL: A handles P. P requires B. P zooms into P1, P2, and P3, in that sequence.

**Diagrama derecho (después de distribución)**: Los enlaces se distribuyen a los subprocesos:

- `A` maneja `P1`, `P2`, y `P3` (tres enlaces de agente separados).
- `P1`, `P2`, y `P3` requieren `B` (tres enlaces de instrumento separados).
OPL: P zooms into P1, P2, and P3, in that sequence. A handles P1, P2, and P3. P1, P2, and P3 require B.

---

## Figura 51 — Restricción de distribución para enlaces de consumo y resultado

**Diagrama izquierdo (INVÁLIDO)**: Objeto `A` maneja `P`. `P` contiene `P1`, `P2`, `P3`. Objeto `C` es consumido por `P` y objeto `B` es producido por `P`. Esto es inválido: los enlaces de consumo y resultado no pueden conectarse al proceso padre cuando tiene subprocesos; deben conectarse directamente a un subproceso específico.
OPL: A handles P. P requires D. P zooms into P1, P2, and P3. P consumes C – NOT VALID! P yields B – NOT VALID! P3 affects B.

**Diagrama derecho (VÁLIDO)**: Misma estructura pero:

- `P1` consume `C` (no P).
- `P2` produce `B` (no P).
- `P3` afecta `B`.
OPL: A handles P. P requires D. P zooms into P1, P2, and P3. P1 consumes C. P2 yields B. P3 affects B.

---

## Figura 52 — Escisión de enlace transformador con estado especificado para resolver subespecificación

Tres diagramas de izquierda a derecha:

**Diagrama 1 (SD)**: Objeto `A` con estados `s1`, `s2`. Proceso `P` cambia A de `s1` a `s2`.

**Diagrama 2 (in-zoomed, SUBESPECIFICADO)**: `P` descompuesto en `P1`, `P2`. Enlace de efecto (s1→s2) sigue conectado a `P` a nivel padre. No se especifica cuál subproceso realiza qué parte de la transición. Marcado como UNDERSPECIFIED.

**Diagrama 3 (in-zoomed, CORRECTO)**: `P` descompuesto en `P1`, `P2`. El enlace se escinde:

- `P1` cambia A de `s1` (enlace de entrada escindido).
- `P2` cambia A a `s2` (enlace de salida escindido).
OPL: A can be s1 or s2. P zooms into P1 and P2, in that sequence. P1 changes A from s1. P2 changes A to s2.

---

## Tabla 25 — Resumen de par de enlaces de efecto entrada-salida especificados escindidos

| Nombre | Semántica | Ejemplo OPD y OPL | Origen | Destino |
|---|---|---|---|---|
| Par de enlaces de efecto entrada-salida especificados escindidos | Un subproceso temprano de un proceso in-zoomed toma un objeto fuera de su estado de entrada. Un subproceso tardío del mismo proceso in-zoomed pone el objeto en su estado de salida. | OPD: Objeto `A` con estados `s1`, `s2`. Proceso `P` contiene `P1` y `P2`. `P1` cambia A desde s1. `P2` cambia A a s2. OPL: P1 changes A from s1. P2 changes A to s2. | **Flecha superior**: estado del afectado → subproceso temprano. **Flecha inferior**: subproceso tardío → estado de salida del afectado. |

NOTA 1: No hay versiones de control-link de los enlaces de efecto escindidos.
NOTA 2: Un objeto puede tener el rol de instrumento en un OPD abstracto y el de transformado en un descendiente más detallado.

---

## Figura 53 — Rol de la abstracción con enlaces transformadores escindidos

**Diagrama izquierdo (SD)**: `Household User` maneja `Dish Washing`. `Dish Washing` requiere `Dishwasher`. `Dish Washing` consume `Soap`. `Dish Washing` afecta `Dish Set`.

**Diagrama derecho (SD1, in-zoomed)**: `Dish Washing` se descompone en cuatro subprocesos secuenciales:

1. `Dish Loading`: cambia `Dishwasher` de `empty` a `loaded`.
2. `Detergent Inserting`: requiere `Soap`. Cambia `Soap Compartment` de `empty` a `loaded`.
3. `Dish Cleaning & Drying`: requiere `Dishwasher`. Consume `Soap`. Cambia `Cleanliness` de `Dish Set` de `dirty` a `clean`.
4. `Dish Unloading`: cambia `Dishwasher` de `loaded` a `empty`.

Objetos adicionales en SD1: `Soap Compartment` (parte de `Dish Washer`), `Cleanliness` (atributo de `Dish Set`).

Estados: `Dishwasher` puede ser `empty` o `loaded`. `Soap Compartment` puede ser `empty` o `loaded`. `Cleanliness` puede ser `dirty` o `clean`.

---

## Figura 54 — Home Safety Maintaining es un sistema asincrónico

Diagrama OPD:

- `Home Safety Maintaining` (elipse, arriba derecha) se descompone en tres subprocesos:
  - `Burglary Handling` (elipse)
  - `Fire Protecting` (elipse)
  - `Earthquake Alarming` (elipse)

Los tres son partes de `Home Safety Maintaining` (relación de agregación, triángulo negro sólido).

- `Detection Module` (rectángulo) exhibe `Detected Threat` (rectángulo) con tres estados: `burglary`, `fire`, `earthquake`.

- Cada estado de `Detected Threat` tiene un **enlace de evento** (`e`) hacia el subproceso correspondiente:
  - Estado `burglary` → `Burglary Handling` (enlace de evento de instrumento).
  - Estado `fire` → `Fire Protecting`.
  - Estado `earthquake` → `Earthquake Alarming`.

OPL:

- Home Safety Maintaining consists of Burglary Handling, Fire Protecting, and Earthquake Alarming.
- Detection Module exhibits Detected Threat.
- Detected Threat can be burglary, fire, or earthquake.
- Burglary Detected Threat initiates Burglary Handling, which requires burglary Detected Threat.
- Fire Detected Threat initiates Fire Protecting, which requires fire Detected Threat.
- Earthquake Detected Threat initiates Earthquake Alarming, which requires earthquake Detected Threat.

---

## Figura 55 — Abstracción de enlaces procedimentales

Diagrama que muestra la transición de un OPD detallado (SD1) a un OPD abstracto (SD) mediante out-zooming:

**SD1 (izquierda)**: Proceso `P` (elipse) contiene subprocesos `P1` y `P2`. Objeto `B` (rectángulo) tiene múltiples enlaces a los subprocesos.

**Proceso Out-zooming** (centro): Elipse con borde discontinuo representando el proceso de abstracción.

**SD (derecha)**: Solo muestra `B` y `P` como entidades compactas, con el enlace procedimental resumido (flecha bidireccional, efecto).

La flecha de out-zooming va de SD1 a SD, indicando la dirección de abstracción.

---

## Tabla 26

> **Nota**: La Tabla 26 no figura en el conjunto de imágenes extraídas del original. Puede tratarse de un salto en la numeración de la norma o de una imagen no capturada.

---

## Tabla 27 — Precedencia de enlaces transformadores: resolución de conflictos entre efecto, resultado y consumo

Tabla con cuatro filas y cuatro columnas. Cada celda contiene un mini-OPD mostrando el proceso P zoomed con subprocesos P1 y P2, y el objeto B.

La tabla cruza el tipo de enlace de B a P1 (efecto, resultado, consumo) con el tipo de enlace de B a P2 (efecto, resultado, consumo), y muestra si la combinación es **válida** o **inválida**.

**Reglas de precedencia**:

- Efecto + Efecto = Válido (enlace de efecto bidireccional en SD).
- Efecto + Resultado = Válido (enlace de efecto en SD).
- Resultado + Efecto = Válido (enlace de efecto en SD).
- Resultado + Consumo = Inválido.
- Consumo + Resultado = Inválido.
- Consumo + Efecto = Válido (enlace de consumo en SD).
- Efecto + Consumo = Válido (enlace de consumo en SD).
- Consumo + Consumo = Inválido.
- Resultado + Resultado = Inválido.

La lógica: consumo prevalece sobre efecto; efecto prevalece sobre resultado. Conflictos entre consumo-resultado o duplicados del mismo tipo extremo son inválidos.

---

## Figura 56 — Precedencia de enlaces para enlaces transformadores y habilitadores

**SD1 (izquierda)**: Proceso `P` contiene subprocesos `P1` y `P2`. Objeto `B` tiene:

- Enlace de instrumento (círculo hueco) hacia `P1`.
- Enlace de efecto (bidireccional) desde `P2`.

**SD (derecha, tras out-zooming)**: `B` tiene un **enlace de efecto** (bidireccional) hacia `P`. El enlace transformador (efecto) tiene precedencia sobre el habilitador (instrumento).

---

## Figura B.1 — Símbolos de objeto duplicado y proceso duplicado

Cuatro ejemplos de cómo se representan copias duplicadas:

**Objeto duplicado** (arriba izquierda): `Duplicate Object` (rectángulo) con una pequeña marca de duplicación en la esquina superior derecha (un pequeño rectángulo superpuesto, como una "oreja doblada").

**Proceso duplicado** (arriba derecha): `Copying` (elipse) con una pequeña marca de duplicación (un pequeño arco en la esquina superior derecha).

**Uso en contexto** (abajo izquierda): `Duplicate Object` (con marca) y `Copying` (con marca) conectados por relación de generalización (triángulo hueco), mostrando `Photocopying` como especialización.

**Uso en contexto** (abajo derecha): `Copying` (elipse) produce `Duplicate Object` (rectángulo con marca). Enlace de resultado.

---

## Figura C.1 — Estructura del modelo OPM (C.2 OPM model structure)

Diagrama OPD jerárquico del metamodelo OPM completo:

**Nivel superior**: `OPM Model` (rectángulo) con enlace etiquetado `specifies` hacia `System` (rectángulo).

**Descomposición de OPM Model** (agregación): consiste de `OPD Set` y `OPL Spec`.

- `OPD Set` y `OPL Spec` tienen enlaces bidireccionales etiquetados `graphically specifies` / `textually specifies`.

**OPD Set** consiste de uno o más `OPD` (multiplicidad `+`).
**OPL Spec** consiste de uno o más `OPL Paragraph` (multiplicidad `+`).

- `OPD` y `OPL Paragraph` tienen los mismos enlaces `graphically specifies` / `textually specifies`.

**OPD** consiste de uno o más `OPD Construct` (multiplicidad `+`).
**OPL Paragraph** consiste de uno o más `OPL Sentence` (multiplicidad `+`).

- `OPD Construct` y `OPL Sentence` tienen los mismos enlaces.

**OPD Construct** se descompone en `Link Set` y `Thing Set`.
**OPL Sentence** se descompone en `Punctuation Mark` (multiplicidad `+`), `Phrase` (multiplicidad `3..*`), que se generaliza en `Reserved Phrase` y `Word`.

En el nivel más bajo:

- `Link` y `Thing` forman el nivel atómico.
- `Link` tiene enlace `graphically specifies` / `textually specifies` con `Reserved Phrase`.
- `Thing` exhibe `Name` (multiplicidad `2..*`).
- Enlace etiquetado lateral `can be in-zoomed to create` conecta componentes.

---

## Figura C.2 — Modelo de OPD Construct y Basic Construct

Diagrama OPD:

- `OPD Construct` (rectángulo, arriba) consiste de `Thing Set` y `Link Set` (agregación).
- `Thing` y `Link` son `Elements` (generalización).
- `Thing Set` consiste de `2` o más `Things` (multiplicidad `2..*`).
- `Link Set` consiste de al menos uno `Link` (multiplicidad `+`).
- `Thing Set` exhibe `Size` con estados `2` y `>=3`.
- `Link Set` exhibe `Size` con estados `1` y `>=2`.
- `Basic Construct` es un `OPD Construct` (generalización).
- `Basic Construct` exhibe `1` Size de Link Set y `2` Size de Thing Set.

---

## Figura C.3 — Construcción de OPD Construct y Basic Construct

Similar a C.2 pero con proceso de construcción:

- `OPD Construct` exhibe `Connecting` (proceso).
- `Thing Set` tiene estados `disconnected` (inicial) y `connected` (final).
- `Connecting` requiere `Link Set` (instrumento) y cambia `Thing Set` de `disconnected` a `connected`.
- `Cardinality` reemplaza a `Size` como nombre del atributo.
- `Cardinality` de `Link Set` puede ser `1` o `>=2`.
- `Cardinality` de `Thing Set` puede ser `2` o `>=3`.

---

## Figura C.4 — Modelo OPM de OPM Element

Diagrama OPD:

- `Thing` y `Link` son `Elements` (generalización).
- `Link` conecta `2` `Things` (enlace etiquetado `connects`, multiplicidad `2`).
- `Link` consiste de `Source`, `Destination`, y `Connector` (agregación).
- `Source` y `Destination` son `Linked Things` (generalización).
- `Linked Thing` exhibe `Symbol` y `Multiplicity`.
- `Multiplicity` exhibe `Symbol` y `Lower&Upper Bound`.
- `Lower&Upper Bound` puede ser `0..1`, `0..*`, `1..1`, o `1..*`.
- `Lower&Upper Bound` por defecto es `1..1`.
- `Symbol` de `Multiplicity` puede ser `?`, `*`, `NONE`, o `+`.
- `?` denota 0..1, `*` denota 0..*, `NONE` denota 1..1, `+` denota 1..*.
- `Connector` consiste de `Line`, `Symbol`, un `Tag` opcional, y un `Path Label` opcional.
- `Tag` y `Path Label` son `Phrases` (generalización).

---

## Figura C.5 — Modelo OPM de Thing

Diagrama OPD:

- `Thing` se generaliza en `Process` y `Object`.
- `Object` exhibe `State Set`.
- `State Set` exhibe `Size` con estados `s=0` y `s>=1`.
- `State Set` consiste de `States` opcionales (multiplicidad `*`).
- `Stateless Object` y `Stateful Object` son `Objects` (generalización).
- `Stateless Object` exhibe `s=0` Size de State Set.
- `Stateful Object` exhibe `s>=1` Size de State Set.
- `Stateful Object` representa `s` `State-Specific Objects`.
- `State-Specific Object Set` consiste de `s` `State-Specific Objects`.
- `State-Specific Object` refiere a `State`.
- `Current State` es un `State` (indicado por enlace).

---

## Figura C.6 — Ejemplo de objeto específico de estado

Diagrama OPD:

- `Product` (rectángulo, derecha) con cinco estados verticales: `designed`, `manufactured`, `tested`, `purchased`, `used`.
- `State-Specific Product Set` (rectángulo, arriba izquierda) consiste de `5` `State-Specific Products`.
- `Product` deriva `State-Specific Product Set` (enlace etiquetado `derives`).
- Cinco especializaciones de `State-Specific Product`:
  - `Designed Product` refiere al estado `designed` de Product.
  - `Manufactured Product` refiere al estado `manufactured`.
  - `Tested Product` refiere al estado `tested`.
  - `Purchased Product` refiere al estado `purchased`.
  - `Used Product` refiere al estado `used`.

Cada State-Specific Product tiene un enlace etiquetado `refers to Product's state` hacia su estado correspondiente.

---

## Figura C.7 — Modelo OPM de objeto con estados y estado

Diagrama OPD:

- `Stateful Object` exhibe `State Set`.
- `State Set` consiste de al menos un `State`, opcionales `Initial States`, opcionales `Final States`, y un `Default State` opcional.
- `State` exhibe `Designation` y `Symbol`.
- `Designation` puede ser `initial`, `final`, o `default`.
- `Initial State`, `Final State`, y `Default State` son `States` (generalización).
- `Initial State` exhibe `initial` Designation y `bold-contour routableangle` Symbol.
- `Final State` exhibe `final` Designation y `double-contour routableangle` Symbol.
- `Default State` exhibe `default` Designation y `routableangle pointed to by open arrow` Symbol.
- `Symbol` puede ser: `routableangle`, `routableangle pointed to by open arrow`, `double-contour routableangle`, `bold-contour routableangle`.

---

## Figura C.8 — Modelo OPM de enlaces

Diagrama OPD jerárquico:

- `Element` se generaliza en `Thing` y `Link`.
- `Link` conecta `2` `Things` (multiplicidad `2`).
- `Link` se generaliza en `Structural Link` y `Procedural Link`.
- `Link` exhibe `Linked Pair`.
- `Linked Pair` consiste de `2` Things.
- `Linked Pair` puede ser: `object-object`, `object-state`, `state-state`, `process-object`, `process-state`, `process-process`.

**Subtipos de Structural Link**:

- `Object-Object Link` y `State-State Link`.
- `Object-State Link` es un `Object-Object Link` (subtipo).

**Subtipos de Procedural Link**:

- `Process-Object Link` y `Process-Process Link`.
- `Process-State Link` es un `Process-Object Link` (subtipo).

Cada subtipo exhibe el `Linked Pair` correspondiente.

---

## Figura C.9 — Modelo OPM de propiedades genéricas de Thing

Diagrama OPD:

- `Thing` se generaliza en `Process` y `Object`.
- `Thing` exhibe `Perseverance`, `Essence`, y `Affiliation`.
- `Perseverance` puede ser `transient` o `persistent`.
- `Essence` puede ser `physical` o `informatical`.
- `Affiliation` puede ser `systemic` o `environmental`.
- `Object` exhibe `persistent` Perseverance. `Process` exhibe `transient` Perseverance.
- Seis especializaciones cruzadas:
  - `Physical Process`, `Informatical Process`, `Systemic Process`, `Environmental Process` son Processes.
  - `Physical Object`, `Informatical Object`, `Systemic Object`, `Environmental Object` son Objects.
- `Physical Process` y `Physical Object` exhiben `physical` Essence.
- `Informatical Process` y `Informatical Object` exhiben `informatical` Essence.
- `Systemic Process` y `Systemic Object` exhiben `systemic` Affiliation.
- `Environmental Process` y `Environmental Object` exhiben `environmental` Affiliation.

---

## Figura C.10 — Modelo OPM de representación simbólica de Thing

Diagrama OPD:

- `Thing` exhibe `Symbol`.
- `Symbol` de `Thing` consiste de `Shape`, `Depth`, y `Contour`.
- `Process` y `Object` son `Things`.
- `Shape` puede ser `ellipse` o `rectangle`.
- `Depth` puede ser `shaded` o `flat`.
- `Contour` puede ser `solid` o `dashed`.
- `Process` exhibe `ellipse` Shape. `Object` exhibe `rectangle` Shape.
- `Physical Process` y `Physical Object` exhiben `shaded` Depth.
- `Informatical Process` y `Informatical Object` exhiben `flat` Depth.
- `Systemic Process` y `Systemic Object` exhiben `solid` Contour.
- `Environmental Process` y `Environmental Object` exhiben `dashed` Contour.

---

## Figura C.11 — Modelo OPM de las ocho representaciones simbólicas de Thing

Diagrama extenso que muestra las ocho combinaciones de Symbol (Shape x Depth x Contour) con sus representaciones visuales:

| Cosa | Shape | Depth | Contour | Visual |
|---|---|---|---|---|
| Physical Systemic Process | ellipse | shaded | solid | Elipse con borde continuo y sombra |
| Physical Environmental Process | ellipse | shaded | dashed | Elipse con borde punteado y sombra |
| Informatical Systemic Process | ellipse | flat | solid | Elipse con borde continuo, sin sombra |
| Informatical Environmental Process | ellipse | flat | dashed | Elipse con borde punteado, sin sombra |
| Physical Systemic Object | rectangle | shaded | solid | Rectángulo con borde continuo y sombra |
| Physical Environmental Object | rectangle | shaded | dashed | Rectángulo con borde punteado y sombra |
| Informatical Systemic Object | rectangle | flat | solid | Rectángulo con borde continuo, sin sombra |
| Informatical Environmental Object | rectangle | flat | dashed | Rectángulo con borde punteado, sin sombra |

Abajo se incluyen los ocho símbolos gráficos (PSP, PEP, ISP, IEP, PSO, PEO, ISO, IEO) con sus nombres abreviados.

---

## Figura C.12 — Elaboración de Basic Construct

Diagrama OPD:

- `Basic Construct` (arriba) consiste de `Link` y `2` `Things` (agregación).
- `Link` conecta `2` `Things`.
- `Structural Link` y `Procedural Link` son `Links` (generalización).
- `Basic Structural Construct` y `Basic Procedural Construct` son `Basic Constructs` (generalización).
- `Basic Structural Construct` consiste de `Structural Link` y `2` `Objects`.
- `Basic Procedural Construct` consiste de `Procedural Link`, `Object`, y `Process`.
- `Structural Link` conecta `2` Objects.
- `Procedural Link` conecta un `Process` y un `Object`.

---

## Figura C.13 — Modelo OPM de Basic Structural Construct

Diagrama OPD extenso:

- `Basic Structural Construct` consiste de `Refineable`, `Refinee`, y `Structural Link`.
- `Refineable` y `Refinee` son `Things`.
- `Structural Link` exhibe `Semantics`.
- `Semantics` puede ser: `aggregation-participation`, `exhibition-characterization`, `generalization-specialization`, `classification-instantiation`, o `user-defined`.
- Cinco subtipos de enlace (por semántica): `Aggregation-Participation Link`, `Exhibition-Characterization Link`, `Generalization-Specialization Link`, `Classification-Instantiation Link`, `Tagged Structural Link`.
- Cada subtipo exhibe su `Semantics` correspondiente.
- `Whole`, `Exhibitor`, `General`, y `Class` son `Refineables`.
- `Part`, `Feature`, `Specialization`, e `Instance` son `Refinées`.
- Cada Construct específico (Aggregation-Participation, Exhibition-Characterization, etc.) consiste de su Refineable, Refinee y Link correspondientes.

---

## Figura C.14 — Modelo OPM de Basic Procedural Construct

Diagrama OPD:

- `Basic Procedural Construct` consiste de `Object`, `Process`, y `Procedural Link`.
- `Procedural Link` exhibe `Semantics`.
- `Semantics` puede ser: `transformation`, `enablement`, `transformation & control`, y `enablement & control`.
- `Transformee` y `Enabler` son `Objects`.
- `Controlling Transformee` es un `Transformee`.
- `Controlling Enabler` es un `Enabler`.
- `Transforming Link` y `Enabling Link` son `Procedural Links`.
- `Transforming & Control Link` es un `Transforming Link`.
- `Enabling & Control Link` es un `Enabling Link`.
- `Transformation Construct` y `Enablement Construct` son `Basic Procedural Constructs`.
- `Transformation & Control Construct` es un `Transformation Construct`.
- `Enablement & Control Construct` es un `Enablement Construct`.

---

## Figura C.15 — Modelo OPM de Transformation Construct

Diagrama OPD:

- `Transformation Construct` consiste de `Transformee`, `Process`, y `Transforming Link`.
- `Transforming Link` exhibe `Symbol` y `Semantics`.
- `Symbol` puede ser: `unidirectional closed arrowhead` o `bidirectional closed arrowhead`.
- `Semantics` puede ser: `consumption`, `effect`, o `result`.
- `Consumee`, `Affectee`, y `Resultee` son `Transformees`.
- `Consumption Link`, `Effect Link`, y `Result Link` son `Transforming Links`.
- `Consumption Construct`, `Result Construct`, y `Effect Construct` son `Transformation Constructs`.
- `Consumption Construct` consiste de `Consumption Link`, `Process`, y `Consumee`.
- `Effect Construct` consiste de `Effect Link`, `Process`, y `Affectee`.
- `Result Construct` consiste de `Result Link`, `Process`, y `Resultee`.
- `State-Specified Consumption Construct` es un `Consumption Construct`.
- `State-Specified Result Construct` es un `Result Construct`.

---

## Figura C.16 — Modelo OPM de direccionalidad de enlaces de Transformation Construct

Diagrama OPD tabular que muestra la direccionalidad de conexión:

- `Transformation Construct` consiste de `Transformee`, `Transforming Link`, y `Process`.
- `Consumption Link`, `Effect Link`, y `Result Link` son `Transforming Links`.
- `Consumee`, `Affectee`, y `Resultee` son `Transformees`.

Direccionalidad:

- `Consumption Link` conecta **desde** `Consumee` **hacia** `Process`.
- `Effect Link` conecta `Affectee` **y** `Process` (bidireccional).
- `Result Link` conecta **desde** `Process` **hacia** `Resultee`.

---

## Figura C.17 — Modelo OPM de Basic Enablement Construct

Diagrama OPD:

- `Enablement Construct` consiste de `Enabler`, `Process`, y `Enabling Link`.
- `Enabling Link` exhibe `Semantics` y `Symbol`.
- `Enabling Link` conecta **desde** `Enabler` **hacia** `Process`.
- `Semantics` puede ser `Agent` o `Instrument`.
- `Symbol` puede ser `black lollipop` o `white lollipop`.
- `Agent` e `Instrument` son `Enablers`.
- `Agent Link` e `Instrument Link` son `Enabling Links`.
- `Agent Link` exhibe `agent` Semantics y `black lollipop` Symbol.
- `Instrument Link` exhibe `instrument` Semantics y `white lollipop` Symbol.
- `Agent Construct` e `Instrument Construct` son `Enablement Constructs`.
- `Agent Construct` consiste de `Agent`, `Process`, y `Agent Link`.
- `Instrument Construct` consiste de `Instrument`, `Process`, y `Instrument Link`.
- `State-Specified Agent Construct` es un `Agent Construct`.
- `State-Specified Instrument Construct` es un `Instrument Construct`.

---

## Figura C.18 — Modelo OPM de constructo de agente con estado especificado con ejemplo mapeado

**Parte superior (metamodelo)**:

- `State-Specified Agent Construct` (arriba derecha) consiste de `State-Specified Agent`, `Process`, y `Agent Link`.
- `State-Specified Agent` es un `State-Specified Enabler`.
- `State-Specified Enabler` es un `State-Specific Object`.
- `Agent Link` conecta `State-Specified Agent` y `Process`.

**Parte inferior (ejemplo mapeado)**: Flechas azules grandes conectan los elementos del metamodelo con un ejemplo concreto:

- `Administrator` (rectángulo) con estados `unauthorized` y `authorized` → mapea a `State-Specified Agent`.
- `Approving` (elipse) → mapea a `Process`.
- Enlace de agente con estado especificado desde `authorized` Administrator hacia `Approving` → mapea a `Agent Link`.

OPL ejemplo: Administrator can be unauthorized or authorized. Authorized Administrator handles Approving.

---

## Figura C.19 — Modelos de New-Diagram In-Zooming y New-Diagram Out-Zooming

**Diagrama izquierdo (modelo simple)**: `New-Diagram In-Zooming` (elipse) requiere `SDn` y produce `SDn+1`. `New-Diagram Out-Zooming` requiere `SDn+1`.

**Diagrama derecho (modelo descompuesto)**:

- `New-Diagram In-Zooming` se descompone en `Content Showing` y `Link Refining`, en esa secuencia, más `Semi-Zoomed OPD`.
  - `Content Showing` requiere `SDn` y produce `Semi-Zoomed OPD`.
  - `Link Refining` consume `Semi-Zoomed OPD` y produce `SDn+1`.

- `New-Diagram Out-Zooming` se descompone en `Link Abstracting` y `Content Hiding`, en esa secuencia, más `Semi-Zoomed OPD`.
  - `Link Abstracting` requiere `SDn+1` y produce `Semi-Zoomed OPD`.
  - `Content Hiding` consume `Semi-Zoomed OPD` y produce `SDn`.

---

## Figura C.20 — Elaboración de New-Diagram In-Zooming y Out-Zooming

Diagrama OPD complejo que muestra el flujo concreto entre SDn y SDn+1:

**SDn** contiene objetos `C`, `A`, `D` y proceso `P`, más objeto `B` fuera del proceso.

**Semi-Zoomed OPD** (estado intermedio): muestra `P` descompuesto con subprocesos `P1`, `P2`, `BP`, `P3`, más los objetos `C`, `A`, `D`. Los enlaces están parcialmente refinados.

**SDn+1**: versión completa con `P` descompuesto, todos los enlaces distribuidos a los subprocesos correctos, y objeto `B` conectado apropiadamente.

Las flechas entre las tres versiones muestran los pasos de Content Showing, Link Refining (in-zooming) y Link Abstracting, Content Hiding (out-zooming).

---

## Figura C.21 — Simplificación de un OPD

Diagrama en tres columnas:

**Columna 1 (Original)**: Tres OPDs (SD, SD1, SD1.1) con procesos y subprocesos cada vez más detallados. SD contiene objetos y proceso P. SD1 muestra P descompuesto en P1-P5. SD1.1 muestra P2 descompuesto en P21, P22.

**Columna 2 (Identificación)**: Se identifica el grupo P123 (P1, P2, P3 con fondo gris) como candidato para out-zooming.

**Columna 3 (Resultado simplificado)**: Cuatro OPDs renumerados:

- SD[new]: simplificado.
- SD1[new]: P123 como proceso compacto, más P4, P5, BK, B.
- SD1.1[new]: P123 descompuesto en P1, P2, P3.
- SD1.1.1[new]: P2 descompuesto en P21, P22.

---

## Figura C.22 — Process Performance Controlling — diagrama de sistema (SD)

Diagrama OPD del sistema de control de desempeño de procesos:

**Objetos**:

- `Involved Object Set` consiste de `Preprocess Object Set` y `Postprocess Object Set`.
- Cada uno exhibe `Size`: Preprocess `r+s>=0`, Postprocess `s>=0`, Involved `r+s>=0`.
- `Executable Process` (elipse con borde discontinuo, ambiental): el proceso a controlar.
- `Success Message`, `Failure Message`, `Cancel Message`, `Abort Message`: mensajes de resultado.
- `Abort Message` y `Cancel Message` son `Failure Messages` (generalización).

**Proceso principal**: `Process Performance Controlling` (elipse) afecta `Involved Object Set`. `Executable Process` invoca `Process Performance Controlling`. El proceso produce uno de `Success Message` o `Failure Message` (XOR).

---

## Figura C.23 — Process Performance Controlling in-zoomed en SD1

Diagrama OPD detallado:

- `Process Performance Controlling` se descompone en `Process Initiating` y `Process Performing`, en esa secuencia, más `Postcondition`.
- `Process Status` puede ser `idle`, `started (t=0)`, `aborted`, `completed (t=n)`, u otros estados.
- `Postcondition` puede ser `false` o `true`.
- `Process Initiating` cambia `Process Status` de `idle` a `started (t=0)` o `aborted`.
- `Process Initiating` produce `false Postcondition` y `Cancel Message`.
- `Process Performing` ocurre si `Enabler Set` existe (condicional), de lo contrario se omite.
- `Process Performing` cambia `Process Status` de `started (t=0)` a `aborted` o `completed (t=n)`.
- `Process Performing` afecta `Postcondition` y `Affectee Set`.
- `Process Performing` produce `Success Message` o `Abortion Message`.

---

## Figura C.24 — Process Initiating in-zoomed como SD1.1

Diagrama OPD:

- `Process Initiating` se descompone en `Precondition Evaluating` y paralelo `Cancelling` y `Starting`, más `Precondition`.
- `Precondition` puede ser `false` o `true`. Inicialmente `false`.
- `Executable Process` invoca `Precondition Evaluating`.
- `Precondition Evaluating` produce `Precondition`.
- `Precondition Evaluating` cambia `Process Status` de `idle` a otro estado.
- `Cancelling` ocurre si `Precondition` es `false` (condicional).
- `Cancelling` cambia `Process Status` a `idle` y produce `Cancel Message`.
- `Starting` ocurre si `Precondition` es `true` (condicional).
- `Starting` cambia `Process Status` a `started (t=0)` y produce `false Postcondition`.
- `Failure Time` exhibida por `Cancel Message`, con valor `t=0`.

---

## Figura C.25 — Precondition Evaluating in-zoomed — SD1.1

Diagrama OPD:

- `Precondition Evaluating` se descompone en `Enabler Set Checking`, `Consumee & Affectee Set Checking`, `Precondition Refuting`, y `Precondition Confirming`.
- `Enabler Set Check Result` puede ser `positive` o `negative`. Inicialmente `positive`.
- `Consumee & Affectee Set Check Result` puede ser `positive` o `negative`. Inicialmente `positive`.
- `Enabler Set Checking` requiere que `Enabler Set` exista (condicional).
- `Enabler Set Checking` afecta `Enabler Set Check Result`.
- `Consumee & Affectee Set Checking` ocurre si `Enabler Set Check Result` es `positive` (condicional).
- `Precondition Refuting` ocurre si algún check result es `negative`.
- `Precondition Confirming` ocurre si `Consumee & Affectee Set Check Result` es `positive`.
- `Precondition Confirming` cambia `Precondition` de `false` a `true` y `Process Status` a `started (t=0)`.

---

## Figura C.26 — Transformee Set Checking in-zoomed — SD1.1.1

Diagrama OPD aún más detallado:

- `Consumee & Affectee Set Checking` se descompone en `Consumee Set Checking`, `Affectee Set Checking`, y `Transformee Set Disqualifying`.
- `Consumee Set Check Results` y `Affectee Set Check Results` pueden ser `positive` o `negative`.
- `Consumee & Affectee Set` consiste de `Consumee Set` y `Affectee Set`.
- `Consumee Set Checking` ocurre si `Consumee Set` existe (condicional).
- `Affectee Set Checking` ocurre si `Consumee Set Check Results` es `positive` y `Affectee Set` existe.
- `Transformee Set Disqualifying` ocurre si algún resultado es `negative`.
- `Transformee Set Disqualifying` cambia `Consumee & Affectee Set Check Result` de `positive` a `negative`.

---

## Figura C.27 — Process Performing in-zoomed — SD1.2

Diagrama OPD:

- `Process Performing` se descompone en `Initial Process Performing`, `Main Process Performing`, y `Final Process Performing`, en esa secuencia.
- `Process Status` puede ser `idle`, `started (t=0)`, `operating (t=n)`, `completed (t=n)`, otros.
- `Postcondition` puede ser `false` o `true`. `Process Status` finalmente es `completed (t=n)`.
- `Affectee` puede ser `input state` o `output state`. Inicialmente `input state`, finalmente `output state`.
- `Initial Process Performing` cambia `Process Status` de `started (t=0)` a `operating (t=n)`.
- `Initial Process Performing` consume `Consumee Set`.
- `Main Process Performing` requiere `Enabler Set`. Produce `Abort Message` opcional.
- `Main Process Performing` cambia `Process Status` de `operating (t=n)` a `completing (t=n)` o `aborted`.
- `Final Process Performing` produce `Resultee Set` y `Success Message`.

---

## Figura C.28 — Initial Process Performing in-zoomed — SD1.2.1

Diagrama OPD:

- `Initial Process Performing` se descompone en paralelo `Input State Exiting` y `Consumee Set Consuming`.
- `Preprocess Object Set` consiste de `Enabler Set`, `Affectee Set`, y `Consumee Set`.
- `Affectee Set` consiste de `Affectees` opcionales.
- `Affectee` puede ser `input state` o `output state`. Inicialmente `input state`.
- `Input State Exiting` cambia `Affectee` desde `input state`.
- `Consumee Set Consuming` consume `Consumee Set`.
- Uno de los dos subprocesos cambia `Process Status` de `started (t=0)` a `operating (t=n)` y `Postcondition` desde `false`.

---

## Figura C.29 — Main Process Performing in-zoomed como SD1.2.2

Diagrama OPD extenso y complejo:

- `Main Process Performing` se descompone en `Elapsed Time & Duration Comparing`, `Enabler & Affectee Set Checking`, `Aborting & Notifying`, `Process Executing & Time Incrementing`, y `Finalizing`.
- `Elapsed Time` y `Duration` exhibidos por `Main Process Performing`, con `Time Unit`.
- `Time Comparison Result` puede ser `e<d`, `e=d`, `e>d`.
- `Elapsed Time & Duration Comparing` produce `Time Comparison Result` y cambia `Postcondition` a `true/false`.
- `Set Approval` puede ser `granted` o `denied`.
- `Process Executing & Time Incrementing` ocurre si `Set Approval` es `granted`.
- `Process Executing & Time Incrementing` consume `Executable Process Instruction Set`.
- `Aborting & Notifying` ocurre si `Set Approval` es `denied`.
- `Finalizing` ocurre si `Time Comparison Result` es `e=d`.
- `Overtime Exception Handling` consume `e>d Time Comparison Result`.

---

## Figura C.30 — Final Process Performing in-zoomed — SD1.2.3

Diagrama OPD:

- `Final Process Performing` se descompone en paralelo `Resultee Set Generating`, `Output State Entering`, y `Success Notifying`.
- `Postprocess Object Set` consiste de `Resultee Set` y `Affectee Set`.
- `Affectee Set` consiste de `Affectees` opcionales.
- `Affectee` puede ser `input state` o `output state`. Finalmente `output state`.
- `Process Status` puede ser `completed (t=n)` o `completing (t=n)`. Finalmente `completed (t=n)`.
- `Postcondition` puede ser `false` o `true`. Inicialmente `false`.
- `Resultee Set Generating` produce `Resultee Set`.
- `Output State Entering` cambia `Affectee` a `output state`.
- `Success Notifying` cambia `Postcondition` a `true` y produce `Success Message`.

---

## Figura D.1 — Modelo de sistema legal: cambio de menor a adulto a los 18 años

Diagrama OPD:

- `Person` (rectángulo con sombra, físico): estados `minor` y `adult`.
- `Birth` (elipse con borde discontinuo y sombra, ambiental y físico): produce `Person` (resultado). El resultado apunta al estado `minor`.
- `Growing` (elipse con borde discontinuo y sombra, ambiental y físico): proceso continuo.
- `Age [yr]` (rectángulo): atributo exhibido. Estados: `0`, `<18`, `>=18`.
- `Growing` cambia `Age` a través de múltiples transiciones (etiquetas de ruta `minor/minor`, `minor/adult`, `adult/adult`).
- `Legal Status Changing` (elipse): cambia `Person` de `minor` a `adult`.
- Enlace de evento (`e`) desde `Age` con estado `>=18` hacia `Legal Status Changing`: cuando Age alcanza >=18, se dispara el cambio de estado legal.

---

## Figura D.2 — El evento del System Clock iniciando Legal Status Changing

Diagrama OPD simplificado:

- `Birth` (elipse) produce `minor` `Person` (rectángulo con estados `minor`, `adult`).
- `System Clock [yr]` (rectángulo) con un solo estado: `18`.
- `System Clock` con estado `18` tiene un enlace de evento de instrumento (`e` con círculo hueco) hacia `Legal Status Changing` (elipse).
- `Legal Status Changing` cambia `Person` de `minor` a `adult`.

OPL implícito: Cuando el System Clock alcanza 18, dispara Legal Status Changing que cambia Person de minor a adult.

---

## Figura D.3 — Car Painting: cuatro diagramas de vida útil

Cuatro diagramas de vida útil (lifespan diagrams) apilados verticalmente que registran la historia del sistema de pintura de autos a medida que progresa el tiempo. Cada diagrama es una tabla con columnas `Name`, `Type`, y períodos de tiempo numerados (1-5).

**Diagrama 1 (solo período 1):**

| Name | Type | 1 |
|---|---|---|
| Painting | Process | not active (1) |
| Color | Object | white (0,0) [1] |
| Car | Object | exists (0,0) [1] |

**Diagrama 2 (períodos 1-3):**

| Name | Type | 1 | 2 | 3 |
|---|---|---|---|---|
| Painting | Process | not active | not active | active |
| Color | Object | white | white | — |
| Car | Object | exists | exists | exists |

**Diagrama 3 (períodos 1-4):**

| Name | Type | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Painting | Process | not active | not active | active | active |
| Color | Object | white | white | — | — |
| Car | Object | exists | exists | exists | exists |

**Diagrama 4 (períodos 1-5):**

| Name | Type | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Painting | Process | not active | not active | active | active | not active |
| Color | Object | white | white | — | — | red (0,...) |
| Car | Object | exists | exists | exists | exists | exists |

En el primer diagrama, solo se muestra el primer período: Painting no está activo, Car existe y Color es white. En el tercer período, Painting se activa y Color deja de ser white (está en transición). En el quinto período, Painting termina y Color es red.

---

## Figura D.4 — Ejecución del modelo OPM para Automatic Crash Responding

Tres instantáneas del mismo OPD mostrando el proceso de ejecución/simulación:

**Instantánea 1 (izquierda, antes)**: `Vehicle Occupants Group` (rectángulo) con estados `possibly injured` y `being helped`. Estado actual: `possibly injured` (resaltado). `Automatic Crash Responding` (elipse, sin ejecutar).

**Instantánea 2 (centro, durante)**: Mismo diagrama pero `Automatic Crash Responding` está en ejecución (elipse sombreada/rellena en azul sólido, indicando proceso activo).

**Instantánea 3 (derecha, después)**: Mismo diagrama pero el estado actual de `Vehicle Occupants Group` cambió a `being helped` (resaltado). `Automatic Crash Responding` terminó (elipse normal).

Las tres instantáneas muestran la progresión temporal de la simulación.

---

## Figura D.5 — Duración de Processing con valores de propiedades

**Diagrama izquierdo (modelo conceptual expandido)**:

- `Processing` (elipse) exhibe `Duration [min]` (rectángulo) con estado de valor `63.3`.
- `Duration [min]` tiene enlace etiquetado `determines` hacia `Duration Distribution` (rectángulo) con estado `normal, mean=45.6, sd=7.3`.
- `Duration [min]` se descompone (agregación) en tres atributos:
  - `Minimal Duration` con valor `30.0`.
  - `Expected Duration` con valor `45.6`.
  - `Maximal Duration` con valor `60.0`.
- Exhibe `Time Unit` con estados: `ms`, `sec`, `min`, `hour`, `day`, `week`, `month`, `year`.

**Diagrama derecho (notación compacta)**: `Processing` (elipse) con anotación interna:

```
Processing
[min]
{30.0, 45.6, 60.0}
{normal, mean=45.6, sd=7.3}
```

OPL: Processing exhibits 30.0, 45.6, and 60.0 min Minimal Duration, Expected Duration, and Maximal Duration, respectively and normal Duration Distribution with parameters mean=45.6 and sd=7.3.

---

## Figura D.6 — Ejemplos de duración de proceso

Tres procesos con diferentes configuraciones de duración en notación compacta:

**Proceso 1**: `Processing [hour] {8.0, 10.0} {exponential, lambda=5.6}` — Duración mínima 8.0 h y máxima 10.0 h, distribución exponencial con lambda=5.6.

**Proceso 2**: `Processing [ms] {normal, mean=1.63, sd=0.16}` — Solo distribución normal con mean=1.63 y sd=0.16 en milisegundos.

**Proceso 3**: `Processing [days] {uniform, a=3, b=5}` — Distribución uniforme con parámetros a=3 y b=5 en días.

---

## Figura D.7 — Ejemplo de excepción por sobretiempo (overtime)

Diagrama OPD:

- `Processing` (elipse) con duración `[min] {30.0, 45.6, 60.0} {uniform, a=5.0, b=70.0} {instance id=1}`.
- `Duration [min]` (rectángulo) exhibido con valor `63.3`.
- `Affectee` (rectángulo): objeto afectado.
- `Overtime Exception Handling` (elipse con borde discontinuo, ambiental): proceso de excepción.

**Enlace XOR**: O `Processing` o `Overtime Exception Handling` afecta `Affectee` (arco XOR con enlaces de efecto).

**Activación**: `Overtime Exception Handling` ocurre si la duración de `Processing` excede 60.0 min (la duración máxima). En este caso, la duración actual es 63.3, que excede el máximo.

OPL: Either Processing or Overtime Exception Handling affects Affectee. Overtime Exception Handling occurs if duration of Processing exceeds 60.0 min. Overtime Exception Handling affects Affectee.

---

## Figura D.8 — Ejemplo de excepción por subtiempo (undertime)

Diagrama OPD similar a D.7:

- `Processing` (elipse) con mismos parámetros de duración `{instance id=2}`.
- `Duration [min]` con valor `23.4` (menor que el mínimo de 30.0).
- `Affectee` (rectángulo).
- `Undertime Exception Handling` (elipse con borde discontinuo, ambiental): proceso de excepción.

**Enlace XOR**: O `Processing` o `Undertime Exception Handling` afecta `Affectee`.

**Activación**: `Undertime Exception Handling` ocurre si la duración de `Processing` queda por debajo de 60.0 min (la duración máxima). La duración actual es 23.4 min, lo que activa la excepción.

El símbolo del enlace de excepción por subtiempo usa `//` (doble barra diagonal) sobre el enlace, a diferencia de la barra simple del overtime.

OPL: Either Processing or Undertime Exception Handling affects Affectee. Undertime Exception Handling occurs if duration of Processing falls short of 60.0 min. Undertime Exception Handling affects Affectee.
