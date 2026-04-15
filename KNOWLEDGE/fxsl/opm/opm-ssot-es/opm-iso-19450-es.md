---
_manifest:
  urn: urn:fxsl:kb:opm-es
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
    shard_index: 1
    shard_count: 5
    shard_root_urn: urn:fxsl:kb:opm-es
relations:
  cites:
  - urn:fxsl:kb:manual-metodologico-opm-es
  - urn:fxsl:kb:opd-es
  - urn:fxsl:kb:opl-es
---


# OPM — Núcleo conceptual


Lenguaje conceptual compacto y metodología para modelar sistemas y representar conocimiento. Esta edición presenta una adaptación canónica en español técnico natural de OPM y adopta **OPL-ES** como forma textual canónica del corpus.

OPM ofrece dos modalidades semánticamente equivalentes:

- **gráfica**, mediante un conjunto de OPDs;
- **textual**, mediante párrafos de OPL-ES.

La meta sigue siendo la misma: permitir que las personas expertas de dominio comprendan el modelo sin perder precisión formal, unificando función, estructura y comportamiento dentro de un único formalismo.

## Contrato editorial del corpus

Este documento es la **capa semántica y ontológica canónica** del corpus OPM en español. Su responsabilidad es:

- fijar definiciones, clases de elementos y clases de relaciones;
- establecer principios de modelado, conformidad y criterio semántico;
- delimitar qué hechos del modelo existen independientemente de su representación textual o gráfica.

Este documento **no** es la fuente canónica de:

- la realización textual en español, que pertenece a [OPL-ES](urn:fxsl:kb:opl-es);
- la gramática gráfica exhaustiva del OPD, que pertenece a [OPD — Gramática visual de OPM](urn:fxsl:kb:opd-es);
- el procedimiento de construcción, refinamiento y gobernanza del modelo, que pertenece a [Manual metodológico de OPM](urn:fxsl:kb:manual-metodologico-opm-es).

Regla editorial: este documento puede nombrar esas capas para ubicar la semántica, pero no debe duplicar sus tablas canónicas ni su casuística operativa.

---

## Alcance y conformidad

OPM se especifica con suficiente detalle como para que quienes modelan puedan producir modelos conceptuales con distintos niveles de profundidad y quienes construyen herramientas puedan implementar software compatible.

**Convención de referencias §:** las referencias `§N` sin prefijo de documento en esta capa remiten a secciones de este mismo documento. Las referencias a otras capas del corpus incluyen el documento destino.

Tres niveles de conformidad:

| Nivel | Requisitos |
|---|---|
| Parcial (simbólico) | Uso exclusivo de símbolos OPM y de elementos con semántica asignada |
| Completo | Parcial + aplicación consistente de principios, contexto y refinamiento |
| Herramienta | Parcial + soporte para conformidad completa + soporte textual OPL según EBNF |

No hay referencias normativas externas.

---

## Glosario

La tabla siguiente consolida el glosario operativo de esta capa. Los términos base conservan su numeración histórica para mantener estabilidad editorial; cualquier adición fuera de esa numeración se marca explícitamente.

| ID | Término | Definición |
|---|---|---|
| 3.1 | Abstracción | Disminución del grado de detalle y de la completitud del modelo del sistema (3.8) para mejorar la comprensión |
| 3.2 | Afectado | Transformado cuyo estado cambia por acción de un proceso; debe ser un objeto con estados |
| 3.3 | Agente | Habilitador que es una persona o un grupo de personas |
| 3.4 | Atributo | Objeto que caracteriza una cosa distinta de sí mismo |
| 3.5 | Comportamiento | Transformación de objetos (3.39) resultante de la ejecución de un modelo OPM compuesto por una colección de cosas (3.76) y enlaces (3.36) |
| 3.6 | Beneficiario | Interesado (3.65) que recibe valor funcional de la operación (3.46) del sistema |
| 3.7 | Clase | Colección de cosas (3.76) con los mismos valores de perseverancia (3.50), esencia y afiliación, y el mismo conjunto de rasgos (3.21) y estados (3.69) |
| 3.8 | Completitud | Grado en que todos los detalles del sistema están especificados |
| 3.9 | Enlace de condición | Enlace procedimental desde objeto o estado hacia proceso que expresa una restricción procedimental |
| 3.10 | Consumido | Transformado que un proceso consume o elimina |
| 3.11 | Contexto | Porción del modelo OPM representada por un OPD y su párrafo OPL correspondiente |
| 3.12 | Enlace de control | Enlace procedimental con semántica adicional de control |
| 3.13 | Modificador de control | Símbolo sobre un enlace que agrega semántica de control: `e` o `c` |
| 3.14 | Atributo discriminante | Atributo cuyos valores identifican especializaciones |
| 3.15 | Efecto | Cambio de estado de un objeto o de un valor de atributo; solo aplica a objetos con estados |
| 3.16 | Elemento | Cosa o enlace |
| 3.17 | Habilitador | 〈proceso〉 Objeto (3.39) que permite un proceso (3.58) sin ser transformado por este |
| 3.18 | Evento | 〈OPM〉 Instante de creación (o aparición) de un objeto (3.39), o entrada de un objeto a un estado (3.68) particular, cualquiera de los cuales puede iniciar la evaluación de una precondición (3.53) del proceso |
| 3.19 | Enlace de evento | Enlace de control que representa un evento desde objeto o estado hacia proceso |
| 3.20 | Exhibidor | Cosa caracterizada por un rasgo mediante exhibición-caracterización |
| 3.21 | Rasgo | Atributo u operación |
| 3.22 | Plegado | Abstracción que oculta refinadores de un refinable desplegado |
| 3.23 | Función | Proceso que entrega valor funcional a un beneficiario |
| 3.24 | General | Refinable con especializaciones |
| 3.25 | Informacional | Relativo a datos, información o conocimiento |
| 3.26 | Herencia | Asignación de elementos OPM desde un general a sus especializaciones |
| 3.27 | Enlace de entrada | Enlace desde un objeto o estado fuente hacia un proceso transformador |
| 3.28 | Instancia de modelo | Objeto o proceso que actúa como instancia en clasificación-instanciación |
| 3.29 | Instancia operacional | Cosa identificable de forma única durante la operación o simulación |
| 3.30 | Instrumento | Habilitador no humano |
| 3.31 | Invocación | Inicio de un proceso por otro proceso |
| 3.32 | Conjunto de objetos involucrados | Unión del conjunto previo al proceso y del conjunto posterior al proceso |
| 3.33 | Contexto de descomposición | Cosas y enlaces dentro del límite de una cosa descompuesta |
| 3.34 | Descomposición de objeto | Despliegue por partes que muestra el orden espacial de objetos constituyentes |
| 3.35 | Descomposición de proceso | Despliegue por partes que muestra el orden temporal parcial de procesos constituyentes |
| 3.36 | Enlace | Expresión gráfica de una relación estructural o procedimental |
| 3.37 | Metamodelo | Modelo de un lenguaje de modelado |
| 3.38 | Hecho de modelo | Relación entre dos cosas OPM o entre estados |
| 3.39 | Objeto | Elemento del modelo que representa una cosa con existencia física o informacional potencial |
| 3.40 | Clase de objeto | Patrón para objetos con la misma estructura y el mismo patrón de transformación |
| 3.41 | OPD | Representación gráfica OPM de un modelo o parte de un modelo |
| 3.42 | OPL | Representación textual de OPM; en esta edición, OPL-ES es la forma canónica |
| 3.43 | OPM | Lenguaje formal bimodal, gráfico y textual, para especificar sistemas complejos y multidisciplinarios |
| 3.44 | Árbol de objetos OPD | Árbol que muestra la elaboración de un objeto a través del refinamiento |
| 3.45 | Árbol de procesos OPD | Árbol generado desde el SD por descomposición de procesos; principal mecanismo de navegación |
| 3.46 | Operación | Proceso que caracteriza una cosa, es decir, lo que esa cosa hace |
| 3.47 | Enlace de salida (output link) | Enlace desde un proceso transformador hacia el estado de destino (salida) de un objeto. Forma parte del par de efecto con estado especificado junto con el enlace de entrada (3.27) |
| 3.48 | Recomposición de objeto | Inverso de la descomposición de objeto |
| 3.49 | Recomposición de proceso | Inverso de la descomposición de proceso |
| 3.50 | Perseverancia | Propiedad: estática para objeto, dinámica para proceso |
| 3.51 | Poscondición | Condición que resulta de la finalización exitosa de un proceso |
| 3.52 | Conjunto posterior al proceso | Objetos que permanecen o resultan tras completar un proceso |
| 3.53 | Precondición | Condición para iniciar un proceso |
| 3.54 | Conjunto previo al proceso | Objetos evaluados antes de iniciar un proceso |
| 3.55 | Esencia primaria | Esencia mayoritaria, informacional o física, de las cosas del sistema |
| 3.56 | Enlace procedimental | Notación gráfica de una relación procedimental |
| 3.57 | Relación procedimental | Conexión dependiente del tiempo o de condiciones entre objeto o estado y proceso |
| 3.58 | Proceso | Transformación de uno o más objetos |
| 3.59 | Clase de proceso | Patrón para procesos con el mismo patrón de transformación |
| 3.60 | Propiedad | Anotación de modelado que distingue elementos: cardinalidades, etiquetas y etiquetas de ruta |
| 3.61 | Refinable | Cosa susceptible de refinamiento: todo, exhibidor, general o clase |
| 3.62 | Refinador | Cosa que refina a un refinable: parte, rasgo, especialización o instancia |
| 3.63 | Refinamiento | Elaboración que incrementa detalle y completitud |
| 3.64 | Resultante | Transformado que un proceso crea |
| 3.65 | Interesado | Persona u organización con interés en el sistema |
| 3.66 | Objeto con estados | Objeto con estados especificados |
| 3.67 | Objeto sin estados | Objeto sin estados especificados |
| 3.68 | Estado de objeto | Situación o posición posible de un objeto |
| 3.69 | Estado de sistema | Instantánea del modelo del sistema en un momento dado |
| 3.70 | Expresión de estados | Refinamiento que revela un subconjunto de estados de un objeto |
| 3.71 | Supresión de estados | Abstracción que oculta un subconjunto de estados de un objeto |
| 3.72 | Enlace estructural | Notación gráfica de una relación estructural |
| 3.73 | Relación estructural | Conexión operacionalmente invariante entre cosas |
| 3.74 | Estructura | Objetos y relaciones no transitorias del modelo |
| 3.75 | Diagrama de Sistema (SD) | OPD raíz que muestra la función del sistema y su contexto de nivel superior |
| 3.76 | Cosa | Objeto o proceso |
| 3.77 | Transformación | Creación, consumo o cambio de estado de un objeto |
| 3.78 | Transformado | Objeto afectado por un proceso |
| 3.79 | Enlace transformador | Enlace de consumo, efecto o resultado |
| 3.80 | Despliegue | Refinamiento que agrega detalle a refinadores |
| 3.81 | Valor de atributo | Estado de un atributo |
| 3.82 | Valor funcional | Beneficio derivado de la función de un sistema |
| 3.83 | Todo | Agregado |
| E1 | OPPL | Capa de clasificación de oraciones sobre OPL usada para graduar la informatividad del modelo. |

Notas normativas clave:

- **Propiedad vs atributo (3.60):** a diferencia de un atributo, el valor de una propiedad no cambia durante la simulación ni en la implementación operacional. Cardinalidades, etiquetas y etiquetas de ruta son propiedades.
- **No hay estados de proceso (3.68):** OPM no usa estados de proceso como "iniciado", "en proceso" o "terminado". En su lugar se modelan subprocesos como *Iniciar*, *Procesar* o *Finalizar*.
- **Toda cosa implica instancias (3.28/3.29):** al crear una cosa en el modelo conceptual, quien modela implica que al menos una instancia operacional de esa cosa, o de una especialización suya, puede existir durante la operación del sistema.

---

## Principios de modelado

Seis principios gobiernan el modelado OPM:

1. **Actividad al servicio de un propósito.** La función del sistema y el propósito del modelado definen el alcance y el nivel de detalle. Diferentes interesados requieren diferentes vistas del mismo sistema.
2. **Unificación de función, estructura y comportamiento.** Estructura más comportamiento producen función. La estructura reúne objetos físicos e informacionales y sus relaciones estructurales. El comportamiento reúne procesos que transforman objetos a lo largo del tiempo.
3. **Identificación del valor funcional.** El proceso que entrega valor expresa la función tal como la percibe el beneficiario principal. Identificar y nombrar ese proceso es el paso crítico inicial.
4. **Función vs comportamiento.** La función es el valor para el beneficiario; el comportamiento es cómo opera el sistema. La misma función puede implementarse con estructuras y comportamientos distintos.
5. **Definición del límite del sistema.** El entorno es el conjunto de cosas fuera del sistema que pueden interactuar con él. Las cosas sistémicas tienen contorno sólido; las ambientales, contorno discontinuo.
6. **Equilibrio entre claridad y completitud.** Los sistemas reales contienen demasiado detalle para una sola vista. La comprensión requiere balancear claridad y completitud mediante una jerarquía de OPDs.

---

## Conceptos fundamentales

### Representación bimodal

Todo modelo OPM se expresa en dos formas equivalentes:

- **OPD**, la representación gráfica;
- **OPL-ES**, la representación textual canónica en español.

Cada OPD tiene un párrafo OPL correspondiente. La redundancia entre la representación gráfica y la textual aprovecha los dos canales cognitivos, visual y verbal.

### Elementos de modelado

Existen dos clases de elementos:

- **cosas**: objetos y procesos;
- **enlaces**: procedimentales y estructurales.

### Gestión de contexto

El OPD es la unidad fundamental para representar un contexto. Los mecanismos principales para gestionar su alcance son:

- expresión y supresión de estados;
- despliegue y plegado;
- descomposición y recomposición.

#### Tabla de equivalencia terminológica (mecanismos de refinamiento)

El corpus usa términos en español como forma canónica. Los términos en inglés se conservan como equivalentes de referencia:

| Español (canónico) | Inglés de referencia | Mecanismo |
|---|---|---|
| Descomposición | In-zooming | Exponer contenido interno de una cosa en un OPD hijo |
| Recomposición | Out-zooming | Ocultar contenido interno, restaurando el OPD padre |
| Despliegue | Unfolding | Exponer refinadores vía relación estructural fundamental |
| Plegado | Folding | Ocultar refinadores de un refinable desplegado |
| Expresión de estados | State expression | Revelar un subconjunto de estados de un objeto |
| Supresión de estados | State suppression | Ocultar un subconjunto de estados de un objeto |
| Contenedor | Container | Cosa refinada agrandada en el OPD hijo |
| Proceso inflado | Inflated process | Elipse del proceso agrandada para contener subprocesos |
| Semi-plegado | Semi-fold | Compresión parcial de refinadores |

### Modelos conceptuales y de ejecución

Los modelos conceptuales describen patrones de estructura y comportamiento. Los modelos de ejecución representan instancias operacionales durante una simulación. Un modelo con un nivel consistente de detalle es implementable como simulación capaz de activar recursos y producir valor funcional; ese es el criterio formal de completitud.

#### Modelos conceptuales vs modelos de ejecución (§6.2.6.1)

Quien modela debe distinguir entre el modelo conceptual y una ocurrencia operacional (en tiempo de ejecución) usada para evaluar el comportamiento del sistema. Un modelo OPM es un marco formal donde ocurrencias de objetos y procesos interactúan mediante enlaces. Quien modela puede simular el comportamiento creando instancias operacionales de cosas y siguiendo el flujo de control de ejecución definido por las conexiones y las reglas semánticas de OPM.

La presencia de ocurrencias de cosas traduce el modelo conceptual abstracto en una forma concreta de ejecución. El comportamiento del sistema modelado solo ocurre cuando existen instancias operacionales. Un enlace entre dos cosas no implica comportamiento hasta que existan instancias operacionales. La noción de tiempo de ejecución está implícita en toda declaración de especificación.

#### Realización del modelo (§6.2.6.2)

Un modelo que expresa detalle consistente es implementable como simulación capaz de realizar recursos, usar procesos para transformar objetos y producir valor funcional para un beneficiario. Esta es la capacidad de realización del modelo.

#### Navegación de OPD y composición de OPL (§6.2.6.3)

Los mecanismos de descomposición y despliegue de esta capa proveen las formas de enlazar diagramas OPD con el OPL correspondiente. Esta capa no prescribe las etiquetas para identificar niveles jerárquicos sucesivos, ni la vinculación entre OPDs relacionados, ni los segmentos OPL correspondientes.

---

## Especificación de la notación visual

La capa gráfica de OPM usa un conjunto mínimo de formas, contornos, sombreados y marcas. En la capa base basta distinguir tres familias:

- **cosas**: objetos, procesos y estados;
- **enlaces procedimentales**: transformadores, habilitadores y de control;
- **enlaces estructurales**: etiquetados y fundamentales.

La semántica de cada familia pertenece a esta capa base; su geometría, decoración, composición, comportamiento visual entre OPDs e índices de reglas pertenecen a [OPD — Gramática visual de OPM](urn:fxsl:kb:opd-es).

Regla editorial:

- este documento solo necesita afirmar que un hecho del modelo tiene representación gráfica obligatoria;
- la tabla exhaustiva de símbolos, variantes, adornos, arcos, contornos y marcas vive exclusivamente en `opm-visual-es`;
- la realización textual de esos mismos hechos vive exclusivamente en `opm-opl-es`.

---

## Cosas: objetos y procesos

### Objetos

Un objeto es una cosa que existe o puede existir física o informacionalmente. Su persistencia se asume por defecto hasta que un proceso actúe sobre él. Se representa con un rectángulo.

### Procesos

Un proceso transforma uno o más objetos creándolos, afectándolos o consumiéndolos. Tiene duración positiva. Se representa con una elipse.

**Procesos persistentes:** esta adaptación reconoce casos límite en los que un proceso explícito mantiene un estado o condición relevante en el tiempo en vez de introducir un cambio neto observable. Estos casos no invalidan la ontología general de OPM, pero tampoco convierten el mantenimiento de estado en patrón por defecto. Deben reservarse para situaciones en que la temporalidad, el esfuerzo sostenido o la condición mantenida formen parte del hecho del modelo. Ejemplos: *Existir*, *Sostener*, *Mantener*, *Conservar*, *Permanecer*, *Esperar*, *Prolongar*, *Extender*, *Demorar*, *Ocupar*, *Persistir*, *Continuar*, *Soportar*, *Retener*. Para objetos biológicos, *Existir* implica *Vivir*.

### Prueba Objeto-Proceso

Tres criterios distinguen proceso de objeto:

- asociación con el tiempo: el proceso ocurre a lo largo del tiempo;
- asociación verbal: el nombre del proceso expresa acción;
- transformación: el proceso debe transformar al menos un objeto.

La política léxica y sintáctica de nombrado en español no se fija en esta capa. La realización textual canónica de nombres de proceso vive exclusivamente en [OPL-ES](urn:fxsl:kb:opl-es) §1.1. Esta capa base solo exige que el nombre denote una acción o transformación identificable del dominio.

### Propiedades genéricas

Todas las cosas tienen tres propiedades genéricas:

| Propiedad | Valores | Convención |
|---|---|---|
| Perseverancia | estática (objeto) / dinámica (proceso) | determinada por el tipo |
| Esencia | física / informacional | la informacional es el valor por defecto |
| Afiliación | sistémica / ambiental | la sistémica es el valor por defecto |

**Herencia de afiliación:** los atributos de objetos ambientales son ambientales. Los procesos ejecutados por entidades ambientales son procesos ambientales.

---

## Estados de objeto

### Objetos con y sin estados

Un objeto con estados tiene un conjunto de estados permitidos. En cada instante, una instancia del objeto está en un estado o en transición entre estados. Un objeto sin estados no puede ser afectado; solo puede crearse o consumirse.

### Representación

El estado se representa como un rectángulo redondeado dentro del objeto. Su realización textual canónica pertenece a [OPL-ES](urn:fxsl:kb:opl-es) §3.2 y §14.

### Estados iniciales, por defecto y finales

Tres designaciones califican estados: **inicial** (estado al crearse el objeto), **final** (estado al consumirse) y **por defecto** (estado más probable al inspeccionar aleatoriamente). Un objeto puede tener cero o más estados iniciales, cero o más finales, y como máximo uno por defecto. La realización gráfica de cada designación (contorno grueso, doble borde, flecha diagonal) vive en [OPD — Gramática visual de OPM](urn:fxsl:kb:opd-es) §2.2.

### Valores de atributos

Un atributo es un objeto que caracteriza una cosa. Sus valores son estados del atributo. Puede especificarse unidad de medida. Su realización textual canónica pertenece a [OPL-ES](urn:fxsl:kb:opl-es) §14.

---
