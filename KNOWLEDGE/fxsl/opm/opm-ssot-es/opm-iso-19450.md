---
_manifest:
  urn: urn:fxsl:kb:opm-iso-19450-es
  provenance:
    created_by: kora/curator
    created_at: '2026-04-14'
    source: OPERATIONS/source/fxsl/opm-methodology/opm-iso.md
version: 1.3.0-es
status: published
tags:
- opm
- iso-19450
- ingenieria-de-sistemas
- modelado-conceptual
- representacion-bimodal
- mbse
- opcloud
- opl-es
lang: es
extensions:
  kora:
    family: specification
    depends_on:
    - urn:fxsl:kb:opm-opl-es
    shard_index: 1
    shard_count: 6
    shard_root_urn: urn:fxsl:kb:opm-iso-19450-es
---

# OPM ISO/PAS 19450 — Metodología Objeto‑Proceso


Lenguaje conceptual compacto y metodología para modelar sistemas de automatización y representar conocimiento. Esta edición canoniza el contenido de ISO/PAS 19450 en español técnico natural y adopta **OPL-ES** como forma textual canónica, en lugar de limitarse a traducir literalmente el inglés.

OPM ofrece dos modalidades semánticamente equivalentes:

- **gráfica**, mediante un conjunto de OPDs;
- **textual**, mediante párrafos de OPL-ES.

La meta sigue siendo la misma: permitir que las personas expertas de dominio comprendan el modelo sin perder precisión formal, unificando función, estructura y comportamiento dentro de un único formalismo.

---

## Alcance y conformidad

OPM se especifica con suficiente detalle como para que quienes modelan puedan producir modelos conceptuales con distintos niveles de profundidad y quienes construyen herramientas puedan implementar software compatible.

Tres niveles de conformidad:

| Nivel | Requisitos |
|---|---|
| Parcial (simbólico) | Uso exclusivo de símbolos OPM (§4) y de elementos (§7-12) con semántica asignada |
| Completo | Parcial + enfoque de modelado según §6 y §14 |
| Herramienta | Parcial + soporte para conformidad completa + soporte textual OPL según EBNF |

No hay referencias normativas externas.

---

## Glosario

La ISO/PAS 19450 define 84 términos formales. A continuación se presentan en español técnico natural, manteniendo la semántica de la norma.

| # | Término | Definición |
|---|---|---|
| 3.1 | Abstracción | Disminución de detalle y completitud para mejorar la comprensión |
| 3.2 | Afectado | Transformado cuyo estado cambia por acción de un proceso; debe ser un objeto con estados |
| 3.3 | Agente | Habilitador que es una persona o un grupo de personas |
| 3.4 | Atributo | Objeto que caracteriza una cosa distinta de sí mismo |
| 3.5 | Comportamiento | Transformación de objetos durante la ejecución del modelo |
| 3.6 | Beneficiario | Interesado que recibe valor funcional de la operación del sistema |
| 3.7 | Clase | Colección de cosas con la misma perseverancia, esencia, afiliación, rasgos y estados |
| 3.8 | Completitud | Grado en que todos los detalles del sistema están especificados |
| 3.9 | Enlace de condición | Enlace procedimental desde objeto o estado hacia proceso que expresa una restricción procedimental |
| 3.10 | Consumido | Transformado que un proceso consume o elimina |
| 3.11 | Contexto | Porción del modelo OPM representada por un OPD y su párrafo OPL correspondiente |
| 3.12 | Enlace de control | Enlace procedimental con semántica adicional de control |
| 3.13 | Modificador de control | Símbolo sobre un enlace que agrega semántica de control: `e` o `c` |
| 3.14 | Atributo discriminante | Atributo cuyos valores identifican especializaciones |
| 3.15 | Efecto | Cambio de estado de un objeto o de un valor de atributo; solo aplica a objetos con estados |
| 3.16 | Elemento | Cosa o enlace |
| 3.17 | Habilitador | Objeto que permite un proceso sin ser transformado |
| 3.18 | Evento | Instante de creación, aparición o entrada en estado de un objeto; puede iniciar evaluación de precondición |
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
| 3.47 | Enlace de resultado | Enlace desde un proceso transformador hacia el estado de salida de un objeto |
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
| 3.60 | Propiedad | Anotación de modelado que distingue elementos: cardinalidades, etiquetas y nombres de ruta |
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
| 3.84 | OPPL | Capa de clasificación de oraciones sobre OPL usada para graduar la informatividad del modelo |

Notas normativas clave:

- **Propiedad vs atributo (3.60):** a diferencia de un atributo, el valor de una propiedad no cambia durante la simulación ni en la implementación operacional. Cardinalidades, etiquetas y nombres de ruta son propiedades.
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

### Modelos conceptuales y de ejecución

Los modelos conceptuales describen patrones de estructura y comportamiento. Los modelos de ejecución representan instancias operacionales durante una simulación. Un modelo con un nivel consistente de detalle es implementable como simulación capaz de activar recursos y producir valor funcional; ese es el criterio formal de completitud.

---

## Especificación de la notación visual

La capa gráfica de OPM usa un conjunto mínimo de formas, contornos, sombreados y marcas. Cada elemento visual tiene una especificación fija.

### Símbolos de entidad

Las entidades son formas cerradas. Las cosas y sus estados son los bloques básicos del diagrama.

| Entidad | Forma | Variantes de contorno | Variantes de sombreado | Etiqueta |
|---|---|---|---|---|
| Objeto | Rectángulo | sólido (sistémico), discontinuo (ambiental) | sombreado (físico), plano (informacional) | nombre del objeto, palabras con mayúscula inicial |
| Proceso | Elipse | sólido (sistémico), discontinuo (ambiental) | sombreado (físico), plano (informacional) | nombre del proceso |
| Estado | Rectángulo redondeado dentro del objeto | normal, grueso (inicial), doble (final), con flecha diagonal abierta (por defecto) | sin sombreado | nombre del estado, en minúscula |

Las ocho combinaciones de símbolo de cosa surgen del producto cartesiano Forma × Sombreado × Contorno:

| Símbolo | Descripción | Significado |
|---|---|---|
| Rectángulo sólido sombreado | Objeto físico sistémico | Objeto tangible dentro del límite del sistema |
| Rectángulo discontinuo sombreado | Objeto físico ambiental | Objeto tangible fuera del sistema |
| Rectángulo sólido plano | Objeto informacional sistémico | Objeto de datos o información dentro del sistema |
| Rectángulo discontinuo plano | Objeto informacional ambiental | Objeto de datos o información fuera del sistema |
| Elipse sólida sombreada | Proceso físico sistémico | Proceso físico dentro del sistema |
| Elipse discontinua sombreada | Proceso físico ambiental | Proceso físico fuera del sistema |
| Elipse sólida plana | Proceso informacional sistémico | Proceso informacional dentro del sistema |
| Elipse discontinua plana | Proceso informacional ambiental | Proceso informacional fuera del sistema |

### Símbolos de enlaces procedimentales

Los enlaces procedimentales conectan objetos o estados con procesos. Cada tipo tiene un símbolo propio.

| Enlace | Fuente | Destino | Especificación gráfica |
|---|---|---|---|
| Consumo | objeto | proceso | Flecha con **punta cerrada** desde el consumido hacia el proceso |
| Resultado | proceso | objeto | Flecha con **punta cerrada** desde el proceso creador hacia el resultante |
| Efecto | objeto ↔ proceso | bidireccional | **Flecha bidireccional con dos puntas cerradas**, una en cada extremo |
| Par efecto entrada-salida | estado → proceso → estado | par direccional | Flecha con punta cerrada desde el **estado de entrada** al proceso y otra desde el proceso al **estado de salida** del mismo objeto |
| Agente | agente | proceso | Línea con **círculo negro relleno** en el extremo hacia el proceso |
| Instrumento | instrumento | proceso | Línea con **círculo blanco vacío** en el extremo hacia el proceso |
| Evento de consumo | objeto | proceso | Enlace de consumo con letra pequeña **`e`** cerca de la punta |
| Evento de efecto | objeto ↔ proceso | bidireccional | Enlace de efecto con letra pequeña **`e`** cerca del extremo del proceso |
| Evento de agente | agente | proceso | Enlace de agente con letra pequeña **`e`** cerca del proceso |
| Evento de instrumento | instrumento | proceso | Enlace de instrumento con letra pequeña **`e`** cerca del proceso |
| Condición de consumo | objeto | proceso | Enlace de consumo con letra pequeña **`c`** cerca de la punta |
| Condición de efecto | objeto ↔ proceso | bidireccional | Enlace de efecto con letra pequeña **`c`** cerca del proceso |
| Condición de agente | agente | proceso | Enlace de agente con letra pequeña **`c`** cerca del proceso |
| Condición de instrumento | instrumento | proceso | Enlace de instrumento con letra pequeña **`c`** cerca del proceso |
| Invocación | proceso | proceso | Línea quebrada tipo **rayo** con punta cerrada |
| Auto-invocación | proceso | mismo proceso | **Par de enlaces de invocación** unidos cabeza con cola y cerrando sobre el mismo origen |
| Excepción por sobretiempo | proceso | proceso de manejo | **Una barra oblicua corta** sobre la línea cerca del proceso destino |
| Excepción por subtiempo | proceso | proceso de manejo | **Dos barras oblicuas paralelas** sobre la línea cerca del proceso destino |

Las variantes con estado especificado parten de un **estado concreto** dentro del objeto y no del objeto completo. La posición de la anotación `e` o `c` se mantiene.

### Símbolos de enlaces estructurales

| Enlace | Especificación gráfica |
|---|---|
| Agregación-participación | **Triángulo negro relleno** cuyo vértice conecta con el todo y cuya base conecta con las partes |
| Exhibición-caracterización | **Pequeño triángulo negro dentro de un triángulo vacío mayor**; el vértice del mayor conecta con el exhibidor |
| Generalización-especialización | **Triángulo vacío**; el vértice conecta con el general |
| Clasificación-instanciación | **Pequeño círculo negro dentro de un triángulo vacío** |
| Indicador de colección incompleta | **Barra horizontal corta** bajo el símbolo triangular |
| Etiquetado unidireccional | Flecha con **punta abierta** y etiqueta textual cerca del eje |
| Etiquetado bidireccional | Línea con **puntas tipo arpón** en lados opuestos de ambos extremos |
| Etiquetado recíproco | Igual al bidireccional, con una sola etiqueta o sin etiqueta |

### Símbolos de operadores lógicos

| Operador | Especificación gráfica |
|---|---|
| AND | Enlaces separados de la misma clase, **sin tocarse** |
| XOR | **Arco discontinuo** sobre el abanico de enlaces, con el foco en el extremo convergente |
| OR | **Dos arcos discontinuos concéntricos** sobre el abanico |
| Probabilístico | Anotación **`Pr=p`** sobre cada enlace del abanico; las probabilidades suman 1 |

### Símbolos de gestión de contexto

| Mecanismo | Especificación gráfica |
|---|---|
| Indicador de supresión de estados | **Pequeño rectángulo redondeado con `...`** en la esquina inferior derecha del objeto |
| Despliegue dentro del mismo diagrama | Refinable y refinadores en el mismo OPD, unidos por enlaces estructurales fundamentales |
| Despliegue o descomposición en nuevo diagrama | El refinable tiene **contorno grueso** en el OPD padre y en el hijo |
| Descomposición de proceso | La elipse del refinable **se agranda** para contener subprocesos; la línea temporal fluye de **arriba hacia abajo** |
| Descomposición de objeto | El rectángulo del refinable **se agranda** para mostrar objetos constituyentes |
| Invocación implícita | **No tiene símbolo explícito**; el orden vertical dentro de la descomposición fija la secuencia |
| Invocación implícita paralela | Subprocesos con los puntos superiores a **la misma altura** empiezan al mismo tiempo |
| Cosa duplicada | **Pequeña silueta desplazada detrás** del símbolo repetido |
| Etiqueta de ruta | **Texto sobre el enlace procedimental**; la coincidencia entre etiquetas de entrada y salida fija la trayectoria |

### Composición visual de la descomposición

La descomposición de procesos crea jerarquía visual. En el SD, un proceso `P` aparece como una elipse simple enlazada a objetos. En `SD1`, la elipse de `P` se agranda y contiene sus subprocesos `P1`, `P2`, `P3` como elipses menores ordenadas verticalmente.

Los objetos del SD se enlazan a los subprocesos concretos que les corresponden. Los enlaces conectados al **contorno exterior** de un proceso descompuesto se distribuyen a todos los subprocesos solo en los casos permitidos. Los enlaces de consumo y resultado **no deben** quedar en el contorno exterior porque eso rompería la lógica temporal.

La descomposición de objetos funciona de forma análoga, aunque sin transferir control de ejecución.

---

## Cosas: objetos y procesos

### Objetos

Un objeto es una cosa que existe o puede existir física o informacionalmente. Su persistencia se asume por defecto hasta que un proceso actúe sobre él. Se representa con un rectángulo.

### Procesos

Un proceso transforma uno o más objetos creándolos, afectándolos o consumiéndolos. Tiene duración positiva. Se representa con una elipse.

### Prueba Objeto-Proceso

Tres criterios distinguen proceso de objeto:

- asociación con el tiempo: el proceso ocurre a lo largo del tiempo;
- asociación verbal: el nombre del proceso expresa acción;
- transformación: el proceso debe transformar al menos un objeto.

En español canónico, la superficie recomendada para procesos en OPL-ES es:

- infinitivo: `Procesar Datos`, `Preparar Café`;
- o nominalización natural del dominio encabezada por `-ción`: `Verificación de Identidad`, `Preparación de Café`.

### Propiedades genéricas

Todas las cosas tienen tres propiedades genéricas:

| Propiedad | Valores | Convención |
|---|---|---|
| Perseverancia | estática (objeto) / dinámica (proceso) | determinada por el tipo |
| Esencia | física / informacional | la informacional es el valor por defecto |
| Afiliación | sistémica / ambiental | la sistémica es el valor por defecto |

**Herencia de afiliación:** los atributos de objetos ambientales son ambientales. Los procesos ejecutados por entidades ambientales son procesos ambientales.

---
