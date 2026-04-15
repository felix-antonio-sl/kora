---
_manifest:
  urn: urn:fxsl:kb:opm-es-p02
version: 2.0.0
status: published
tags:
- opm
- fundamentos
- ingenieria-de-sistemas
- modelado-conceptual
- representacion-bimodal
- mbse
- opl-es
lang: es
extensions:
  kora:
    family: specification
    consolidado: true
    shard_index: 2
    shard_count: 5
    shard_root_urn: urn:fxsl:kb:opm-es
relations:
  cites:
  - urn:fxsl:kb:opl-es
---


# OPM — Núcleo conceptual - Parte 02

## Panorama de enlaces

### Enlaces procedimentales

Existen tres clases:

- **enlaces transformadores**: conectan proceso con transformado (consumo, resultado o efecto);
- **enlaces habilitadores**: conectan habilitador con proceso (agente o instrumento);
- **enlaces de control**: enlaces procedimentales con modificador `e` o `c`.

**Principio de unicidad del enlace procedimental:** un objeto o estado tiene exactamente un rol respecto de un proceso enlazado: transformado o habilitador.

**Enlaces procedimentales con estado especificado:** conectan el proceso con un estado específico de un objeto, no con el objeto completo.

### Enlaces estructurales

Hay dos clases:

- **etiquetados**, cuya semántica la define quien modela;
- **fundamentales**, con semántica fija: agregación-participación, exhibición-caracterización, generalización-especialización y clasificación-instanciación.

Los enlaces estructurales conectan objetos con objetos o procesos con procesos, excepto exhibición-caracterización, que también puede conectar objetos con procesos.

### Control evento-condición-acción

La ejecución de un proceso comienza cuando:

1. ocurre el evento iniciador, si existe;
2. y se satisface la precondición.

Los eventos se pierden tras la evaluación, incluso si la precondición falla.

- **Conjunto previo al proceso**: consumidos + afectados + habilitadores necesarios antes de iniciar el proceso.
- **Conjunto posterior al proceso**: resultantes + objetos afectados después de completar el proceso.

---

## Enlaces transformadores

Tres tipos básicos:

| Enlace | Semántica | Dirección abstracta |
|---|---|---|
| Consumo | El proceso destruye o elimina el objeto. | objeto → proceso |
| Resultado | El proceso crea o genera el objeto. | proceso → objeto |
| Efecto | El proceso cambia el estado del objeto. | objeto ↔ proceso |

**Restricción sobre modificadores de control del enlace de resultado:** no existen las variantes "evento de resultado" ni "condición de resultado". La razón es que el resultado no existe antes del proceso, pues es creado por él, por lo que no puede ser precondición (`c`) ni disparador (`e`). El consumo sí admite ambos modificadores porque el objeto consumido existe en el conjunto previo al proceso. Esta asimetría entre consumo y resultado es inherente a la ontología OPM: el consumo opera sobre el conjunto previo; el resultado opera sobre el conjunto posterior.

> **Nota de capa base:** el conjunto posterior al proceso no admite precondiciones, por lo que los modificadores `c` y `e` no aplican a enlaces de resultado. Esta restricción es absoluta y no admite excepciones.

### Enlaces transformadores con estado especificado

Los enlaces transformadores pueden restringirse a estados concretos del objeto: consumo con estado, resultado con estado, efecto entrada-salida, efecto solo entrada y efecto solo salida.

La realización textual canónica de estas variantes vive en `opm-opl-es` §4. La realización gráfica vive en `opm-visual-es` §3.

Cuando el consumo ocurre a lo largo del tiempo, puede modelarse mediante una propiedad de tasa del enlace y un atributo de cantidad del consumido. Sin esas propiedades, el consumo se interpreta como inmediato al activarse el proceso.

**Resultado hacia un objeto con estado inicial:** el enlace de resultado debe conectarse al rectángulo del objeto o a un estado distinto del inicial, nunca al estado inicial directamente.

**Semántica de transición del afectado:** una vez que el proceso afectador comienza, el afectado sale del estado de entrada. Solo alcanza el estado de salida al completarse el proceso. Si el proceso se aborta antes, el estado del afectado queda indeterminado salvo que exista manejo de excepción.

**Resolución de salida en efecto con solo estado de entrada:** si no se especifica estado de salida, el destino es el estado por defecto del objeto. Si no existe estado por defecto, se usa la distribución de probabilidad de estados.

---

## Enlaces habilitadores

Los habilitadores son necesarios para que ocurra un proceso, pero no son transformados. Hay dos clases:

| Enlace | Tipo de habilitador |
|---|---|
| Agente | Persona o grupo con toma de decisiones. |
| Instrumento | Objeto inanimado sin decisión propia. |

Si un habilitador deja de existir durante la ejecución, el proceso se detiene y el estado del afectado queda indeterminado.

### Enlaces habilitadores con estado especificado

Los habilitadores también pueden restringirse a un estado específico. El proceso ocurre si y solo si el habilitador está en el estado requerido.

La realización textual canónica de estas variantes vive en `opm-opl-es` §5. La realización gráfica vive en `opm-visual-es` §3.

---

## Enlaces de control: eventos

Los enlaces de evento anotan un enlace transformador o habilitador con `e`. Un evento dispara la evaluación de la precondición y luego se pierde, tanto si la precondición se satisface como si no.

### Enlaces de evento transformadores

Las variantes transformadoras incluyen evento de consumo y evento de efecto, con o sin estado especificado.

### Enlaces de evento habilitadores

Las variantes habilitadoras incluyen evento de agente y evento de instrumento, con o sin estado especificado.

La realización textual canónica de todos los eventos vive en `opm-opl-es` §6. La realización gráfica vive en `opm-visual-es` §4.

---

## Enlaces de control: condiciones y excepciones

### Enlaces de condición

Los enlaces de condición anotan un enlace con `c`. Introducen un **mecanismo de omisión condicional** (*bypass*): si la precondición falla, el proceso se omite en vez de esperar.

### Enlaces transformadores condicionales

Los transformadores condicionales introducen omisión condicional: si falla la precondición, el proceso se omite en vez de esperar. Existen variantes de consumo y efecto, con y sin estado especificado.

### Enlaces habilitadores condicionales

Los habilitadores condicionales aplican el mismo patrón a agentes e instrumentos.

### Enlaces condicionales con estado especificado

Las variantes con estado especificado heredan la misma semántica de omisión condicional, restringida a un estado concreto.

La realización textual canónica de todas las condiciones vive en `opm-opl-es` §7. La realización gráfica vive en `opm-visual-es` §4.

### Enlaces de excepción

Conectan un proceso fuente con un proceso de manejo según la duración observada.

| Enlace | Disparador |
|---|---|
| Sobretiempo | La fuente excede su duración máxima. |
| Subtiempo | La fuente queda por debajo de su duración mínima. |

La duración de un proceso puede especializarse en mínima, esperada y máxima. La distribución de duración determina el valor efectivo por instancia.

La realización textual canónica vive en `opm-opl-es` §8.1. La realización gráfica de los enlaces de excepción vive en `opm-visual-es` §4.4; las propiedades de duración que los disparan viven en `opm-visual-es` §14.

---

## Enlaces de invocación

La invocación modela que un proceso inicia otro. Semánticamente puede verse como la creación de un objeto intermedio transitorio consumido de inmediato por el proceso destino.

| Enlace | Semántica |
|---|---|
| Invocación | Un proceso inicia otro proceso. |
| Auto-invocación | Un proceso se reinicia o se reitera a sí mismo. |

**Invocación implícita** dentro de un proceso descompuesto: la terminación de un subproceso invoca al que se encuentra inmediatamente debajo. No hay enlace explícito; la altura relativa determina el orden. Cuando dos o más subprocesos tienen la misma altura superior, comienzan en paralelo y el último en terminar inicia al siguiente.

**Invocación cíclica con omisión condicional:** los enlaces de invocación modelan comportamiento iterativo o cíclico. Después de cada ciclo, un nodo de decisión booleano evalúa si se vuelve a entrar o se continúa. En sistemas de refrigeración, por ejemplo, *Evaporar* invoca al proceso completo de refrigeración por compresión para expresar el ciclo continuo del refrigerante.

La realización textual canónica vive en `opm-opl-es` §8.2. La realización gráfica vive en `opm-visual-es` §9.

---

## Enlaces estructurales

### Enlaces estructurales etiquetados

Los **enlaces estructurales etiquetados** permiten expresar relaciones semánticas definidas por quien modela, no predefinidas por la ontología OPM. Se distinguen cuatro variantes:

- **Unidireccional**: lleva una etiqueta textual que describe la relación desde la fuente al destino.
- **Unidireccional sin etiqueta (null-tagged)**: la etiqueta por defecto es `se relaciona con` (*relates to*). Se usa cuando la relación existe pero no requiere calificación explícita.
- **Bidireccional**: lleva etiquetas independientes en cada dirección.
- **Recíproco**: la misma semántica aplica en ambas direcciones.

### Relaciones estructurales fundamentales

| Relación | Refinable → refinador |
|---|---|
| Agregación-participación | todo → partes |
| Exhibición-caracterización | exhibidor → rasgos |
| Generalización-especialización | general → especializaciones |
| Clasificación-instanciación | clase → instancias |

Las colecciones incompletas usan una barra horizontal bajo el triángulo. Su realización textual canónica pertenece a [OPL-ES](urn:fxsl:kb:opl-es) §9.

**Restricción de perseverancia:** salvo en exhibición-caracterización, el refinable y los refinadores deben tener la misma perseverancia.

Exhibición-caracterización es el único enlace estructural que puede conectar objetos con procesos: el rasgo es atributo si es objeto y operación si es proceso.

**Clasificación-instanciación:** a diferencia de las otras tres relaciones fundamentales, no distingue entre colección completa e incompleta. El número de instancias puede variar durante la operación.

La realización textual canónica de enlaces estructurales y sus variantes básicas vive en `opm-opl-es` §9. La realización gráfica vive en `opm-visual-es` §8.

### Herencia

Las especializaciones heredan del general:

- todas las partes;
- todos los rasgos;
- todos los enlaces estructurales etiquetados;
- todos los enlaces procedimentales.

Se permite herencia múltiple. Un atributo discriminante restringe los valores válidos para las especializaciones. El máximo número de especializaciones con varios atributos discriminantes es el producto cartesiano de sus valores posibles.

**Mecanismo de sobreescritura:** quien modela puede reemplazar un participante heredado especificando una especialización de ese participante con otro nombre y otro conjunto de estados.

**Regla de existencia en ejecución:** una instancia especializada no existe en ausencia de la instancia más general de la que hereda.

**Procedimiento para crear un general a partir de especializaciones existentes:**

1. identificar rasgos y participantes comunes;
2. crear una nueva cosa general con esos elementos;
3. conectarla con sus especializaciones mediante generalización-especialización;
4. eliminar de las especializaciones lo ahora heredado;
5. migrar al general los enlaces procedimentales y estructurales comunes.

### Enlaces estructurales con estado especificado

Estos enlaces asocian objetos especializados con valores concretos de atributos.

Siete clases se agrupan en tres familias:

- estado especificado en el origen;
- estado especificado en el destino;
- estado especificado en origen y destino.

Las variantes bidireccionales y recíprocas no existen para el caso de estado solo en el destino.

La realización textual canónica de estas variantes vive en `opm-opl-es` §9.4. La realización gráfica vive en `opm-visual-es` §8.5.

---

## Cardinalidades de relación

### Multiplicidad de objetos

La multiplicidad restringe el número de instancias de objeto asociadas a un enlace. El valor por defecto es una instancia por extremo. Aplica a enlaces etiquetados, agregación-participación y enlaces procedimentales.

| Símbolo | Límites |
|---|---|
| `?` | 0..1 |
| `*` | 0..* |
| sin símbolo | 1..1 |
| `+` | 1..* |

La sintaxis de rango es `qmín..qmáx`. Pueden usarse varios rangos separados por comas y expresiones aritméticas con `+`, `-`, `*`, `/`, `(`, `)`. Las restricciones usan `=`, `≠`, `<`, `≤`, `≥`, llaves para conjuntos y el operador `∈`.

**Los nombres de parámetros deben ser únicos en todo el modelo.**

**Las restricciones de participación no aplican a procesos.** La repetición secuencial de un proceso se modela con un proceso recurrente y contador de iteración; la repetición paralela, con subprocesos síncronos o asíncronos dentro de una descomposición.

**Declaración de tipo:** un objeto puede declarar tipo computacional. Los tipos comunes incluyen `boolean`, `string`, `integer`, `float`, `double`, `short`, `long` y `enumerated`.

La realización textual canónica de multiplicidades, restricciones y tipos vive en `opm-opl-es` §12.

---

## Operadores lógicos: AND, XOR, OR

### AND

AND se expresa con enlaces separados, del mismo tipo, sin tocarse entre sí.

### XOR

Un abanico XOR exige exclusión mutua: exactamente una ruta del abanico queda habilitada.

### OR

Un abanico OR exige inclusión: al menos una ruta del abanico queda habilitada.

### Combinatoria de abanicos de enlaces

XOR y OR aplican a todas las familias de enlaces procedimentales. El extremo convergente es el extremo común; el divergente no lo es.
La realización visual de estos abanicos vive en `opm-visual-es` §5. La realización textual canónica vive en `opm-opl-es` §11.

### Abanicos de enlaces con modificadores de control

Los abanicos XOR y OR pueden combinarse con modificadores de evento y condición. La semántica sigue siendo la de selección exclusiva o inclusiva, enriquecida respectivamente con iniciación o omisión condicional.

### Abanicos probabilísticos

Cada enlace del abanico se anota con `Pr=p`, y las probabilidades suman 1. Si no se anotan probabilidades explícitas, la distribución por defecto es uniforme.

### Trayectorias de ejecución y etiquetas de ruta

Las etiquetas de ruta resuelven ambigüedad cuando existen varias opciones de salida. La regla es: al salir de un proceso, se sigue el enlace cuya etiqueta coincide con la etiqueta de entrada.

La realización textual canónica de etiquetas de ruta y escenarios pertenece a [OPL-ES](urn:fxsl:kb:opl-es) §13.

Un **escenario** es un conjunto de una o más etiquetas de ruta que define una variante concreta de ejecución. En sistemas complejos, los escenarios evitan crear un OPD adicional por cada variante.

---
