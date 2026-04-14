---
_manifest:
  urn: urn:fxsl:kb:opm-iso-19450-es
  provenance:
    created_by: kora/curator
    created_at: '2026-04-14'
    source: OPERATIONS/source/fxsl/opm-methodology/opm-iso.md
version: 1.4.0-es
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
    consolidado: true
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
| 3.84 | OPPL | **[Extensión no-ISO]** Capa de clasificación de oraciones sobre OPL usada para graduar la informatividad del modelo. Este término no forma parte de ISO/PAS 19450:2015; proviene de trabajo posterior de Dori. |

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

#### Modelos conceptuales vs modelos de ejecución (§6.2.6.1)

Quien modela debe distinguir entre el modelo conceptual y una ocurrencia operacional (en tiempo de ejecución) usada para evaluar el comportamiento del sistema. Un modelo OPM es un marco formal donde ocurrencias de objetos y procesos interactúan mediante enlaces. Quien modela puede simular el comportamiento creando instancias operacionales de cosas y siguiendo el flujo de control de ejecución definido por las conexiones y las reglas semánticas de OPM.

La presencia de ocurrencias de cosas traduce el modelo conceptual abstracto en una forma concreta de ejecución. El comportamiento del sistema modelado solo ocurre cuando existen instancias operacionales. Un enlace entre dos cosas no implica comportamiento hasta que existan instancias operacionales. La palabra "runtime" está implícita en toda declaración de especificación.

#### Realización del modelo (§6.2.6.2)

Un modelo que expresa detalle consistente es implementable como simulación capaz de realizar recursos, usar procesos para transformar objetos y producir valor funcional para un beneficiario. Esta es la capacidad de realización del modelo.

#### Navegación de OPD y composición de OPL (§6.2.6.3)

Los mecanismos de descomposición y despliegue de la §14 proveen las formas de enlazar diagramas OPD con el OPL correspondiente. La §14 no prescribe las etiquetas para identificar niveles jerárquicos sucesivos, ni la vinculación entre OPDs relacionados, ni los segmentos OPL correspondientes.

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

**Procesos persistentes (§7.2.1 NOTE 2):** existen procesos persistentes cuyo efecto es mantener el estado de un objeto, no cambiarlo. La semántica de un proceso persistente es mantener al objeto en su estado actual. Ejemplos: *Existir*, *Sostener*, *Mantener*, *Conservar*, *Permanecer*, *Esperar*, *Prolongar*, *Extender*, *Demorar*, *Ocupar*, *Persistir*, *Continuar*, *Soportar*, *Retener*. Para objetos biológicos, *Existir* implica *Vivir*.

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

## Estados de objeto

### Objetos con y sin estados

Un objeto con estados tiene un conjunto de estados permitidos. En cada instante, una instancia del objeto está en un estado o en transición entre estados. Un objeto sin estados no puede ser afectado; solo puede crearse o consumirse.

### Representación

El estado se representa como un rectángulo redondeado dentro del objeto. En OPL-ES la forma canónica es:

- `**Objeto** puede estar \`estado1\`, \`estado2\` o \`estado3\`.`
- `Estado \`estado\` de **Objeto** es inicial/final/por defecto.`

### Estados iniciales, por defecto y finales

| Designación | Marca gráfica | Significado |
|---|---|---|
| Inicial | borde grueso | estado en la creación del objeto |
| Final | doble borde | estado en el momento de ser consumido |
| Por defecto | indicador con flecha diagonal | estado más probable al inspeccionar aleatoriamente |

### Valores de atributos

Un atributo es un objeto que caracteriza una cosa. Sus valores son estados del atributo. Puede especificarse unidad de medida. La sintaxis canónica OPL-ES es:

- `**Atributo** de **Objeto** es valor.`
- `**Atributo** de **Objeto** varía de X a Y.`

---

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

| Enlace | Semántica | OPL-ES canónico | Dirección |
|---|---|---|---|
| Consumo | El proceso destruye o elimina el objeto | `*Proceso* consume **Consumido**.` | objeto → proceso |
| Resultado | El proceso crea o genera el objeto | `*Proceso* genera **Resultante**.` | proceso → objeto |
| Efecto | El proceso cambia el estado del objeto | `*Proceso* afecta **Afectado**.` | objeto ↔ proceso |

### Enlaces transformadores con estado especificado

| Enlace | OPL-ES canónico |
|---|---|
| Consumo con estado | `*Proceso* consume **Objeto** en \`estado\`.` |
| Resultado con estado | `*Proceso* genera **Objeto** en \`estado\`.` |
| Efecto entrada-salida | `*Proceso* cambia **Objeto** de \`estado-entrada\` a \`estado-salida\`.` |
| Efecto solo entrada | `*Proceso* cambia **Objeto** de \`estado-entrada\`.` |
| Efecto solo salida | `*Proceso* cambia **Objeto** a \`estado-salida\`.` |

Cuando el consumo ocurre a lo largo del tiempo, puede modelarse mediante una propiedad de tasa del enlace y un atributo de cantidad del consumido. Sin esas propiedades, el consumo se interpreta como inmediato al activarse el proceso.

**Resultado hacia un objeto con estado inicial:** el enlace de resultado debe conectarse al rectángulo del objeto o a un estado distinto del inicial, nunca al estado inicial directamente.

**Semántica de transición del afectado:** una vez que el proceso afectador comienza, el afectado sale del estado de entrada. Solo alcanza el estado de salida al completarse el proceso. Si el proceso se aborta antes, el estado del afectado queda indeterminado salvo que exista manejo de excepción.

**Resolución de salida en efecto con solo estado de entrada:** si no se especifica estado de salida, el destino es el estado por defecto del objeto. Si no existe estado por defecto, se usa la distribución de probabilidad de estados.

---

## Enlaces habilitadores

Los habilitadores son necesarios para que ocurra un proceso, pero no son transformados. Hay dos clases:

| Enlace | Tipo de habilitador | Símbolo OPD | OPL-ES canónico |
|---|---|---|---|
| Agente | Persona o grupo con toma de decisiones | círculo negro relleno | `**Agente** maneja *Proceso*.` |
| Instrumento | Objeto inanimado sin decisión propia | círculo blanco vacío | `*Proceso* requiere **Instrumento**.` |

Si un habilitador deja de existir durante la ejecución, el proceso se detiene y el estado del afectado queda indeterminado.

### Enlaces habilitadores con estado especificado

| Enlace | OPL-ES canónico |
|---|---|
| Agente con estado | `**Agente** en \`estado\` maneja *Proceso*.` |
| Instrumento con estado | `*Proceso* requiere **Instrumento** en \`estado\`.` |

El proceso ocurre si y solo si el habilitador está en el estado requerido.

---

## Enlaces de control: eventos

Los enlaces de evento anotan un enlace transformador o habilitador con `e`. Un evento dispara la evaluación de la precondición y luego se pierde, tanto si la precondición se satisface como si no.

### Enlaces de evento transformadores

| Enlace | OPL-ES canónico |
|---|---|
| Evento de consumo | `**Objeto** inicia *Proceso*, que consume **Objeto**.` |
| Evento de efecto | `**Objeto** inicia *Proceso*, que afecta **Objeto**.` |

### Enlaces de evento habilitadores

| Enlace | OPL-ES canónico |
|---|---|
| Evento de agente | `**Agente** inicia y maneja *Proceso*.` |
| Evento de instrumento | `**Instrumento** inicia *Proceso*, que requiere **Instrumento**.` |

### Enlaces de evento transformadores con estado especificado

| Enlace | OPL-ES canónico |
|---|---|
| Evento de consumo con estado | `**Objeto** en \`estado\` inicia *Proceso*, que consume **Objeto**.` |
| Evento de efecto entrada-salida | `**Objeto** en \`estado-entrada\` inicia *Proceso*, que cambia **Objeto** de \`estado-entrada\` a \`estado-salida\`.` |
| Evento de efecto solo entrada | `**Objeto** en \`estado-entrada\` inicia *Proceso*, que cambia **Objeto** de \`estado-entrada\`.` |
| Evento de efecto solo salida | `**Objeto** en cualquier estado inicia *Proceso*, que cambia **Objeto** a \`estado-destino\`.` |

### Enlaces de evento habilitadores con estado especificado

| Enlace | OPL-ES canónico |
|---|---|
| Evento de agente con estado | `**Agente** en \`estado\` inicia y maneja *Proceso*.` |
| Evento de instrumento con estado | `**Instrumento** en \`estado\` inicia *Proceso*, que requiere **Instrumento** en \`estado\`.` |

---

## Enlaces de control: condiciones y excepciones

### Enlaces de condición

Los enlaces de condición anotan un enlace con `c`. Introducen un **mecanismo de bypass**: si la precondición falla, el proceso se omite en vez de esperar.

### Enlaces transformadores condicionales

| Enlace | OPL-ES canónico |
|---|---|
| Consumo condicional | `*Proceso* ocurre si **Objeto** existe, en cuyo caso **Objeto** se consume, de lo contrario *Proceso* se omite.` |
| Efecto condicional | `*Proceso* ocurre si **Objeto** existe, en cuyo caso *Proceso* afecta **Objeto**, de lo contrario *Proceso* se omite.` |

### Enlaces habilitadores condicionales

| Enlace | OPL-ES canónico |
|---|---|
| Agente condicional | `**Agente** maneja *Proceso* si **Agente** existe; de lo contrario *Proceso* se omite.` |
| Instrumento condicional | `*Proceso* ocurre si **Instrumento** existe; de lo contrario *Proceso* se omite.` |

### Enlaces condicionales con estado especificado

Seis variantes donde el bypass verifica que el objeto esté en un estado concreto:

| Enlace | OPL-ES canónico |
|---|---|
| Consumo condicional con estado | `*Proceso* ocurre si **Objeto** está en \`estado\`, en cuyo caso **Objeto** se consume, de lo contrario *Proceso* se omite.` |
| Efecto entrada-salida condicional | `*Proceso* ocurre si **Objeto** está en \`estado-entrada\`, en cuyo caso *Proceso* cambia **Objeto** de \`estado-entrada\` a \`estado-salida\`, de lo contrario *Proceso* se omite.` |
| Efecto solo entrada condicional | `*Proceso* ocurre si **Objeto** está en \`estado-entrada\`, en cuyo caso *Proceso* cambia **Objeto** de \`estado-entrada\`, de lo contrario *Proceso* se omite.` |
| Efecto solo salida condicional | `*Proceso* ocurre si **Objeto** existe, en cuyo caso *Proceso* cambia **Objeto** a \`estado-salida\`, de lo contrario *Proceso* se omite.` |
| Agente condicional con estado | `**Agente** maneja *Proceso* si **Agente** está en \`estado\`, de lo contrario *Proceso* se omite.` |
| Instrumento condicional con estado | `*Proceso* ocurre si **Instrumento** está en \`estado\`, de lo contrario *Proceso* se omite.` |

Gráficamente, cada uno usa su símbolo base con anotación `c` cerca del proceso.

### Enlaces de excepción

Conectan un proceso fuente con un proceso de manejo según la duración observada.

| Enlace | Disparador | Símbolo OPD | OPL-ES canónico |
|---|---|---|---|
| Sobretiempo | La fuente excede su duración máxima | una barra oblicua | `*Manejo* ocurre si duración de *Fuente* excede máx-duración unidades-tiempo.` |
| Subtiempo | La fuente queda por debajo de su duración mínima | dos barras oblicuas paralelas | `*Manejo* ocurre si duración de *Fuente* es menor que mín-duración unidades-tiempo.` |

La duración de un proceso puede especializarse en mínima, esperada y máxima. La distribución de duración determina el valor efectivo por instancia.

---

## Enlaces de invocación

La invocación modela que un proceso inicia otro. Semánticamente puede verse como la creación de un objeto intermedio transitorio consumido de inmediato por el proceso destino.

| Enlace | Símbolo OPD | OPL-ES canónico |
|---|---|---|
| Invocación | línea quebrada tipo rayo | `*Proceso-invocador* invoca *Proceso-invocado*.` |
| Auto-invocación | par de invocaciones cerradas sobre sí mismas | `*Proceso-invocador* se invoca a sí mismo.` |

**Invocación implícita** dentro de un proceso descompuesto: la terminación de un subproceso invoca al que se encuentra inmediatamente debajo. No hay enlace explícito; la altura relativa determina el orden. Cuando dos o más subprocesos tienen la misma altura superior, comienzan en paralelo y el último en terminar inicia al siguiente.

**Invocación cíclica con bypass condicional:** los enlaces de invocación modelan comportamiento iterativo o cíclico. Después de cada ciclo, un nodo de decisión booleano evalúa si se vuelve a entrar o se continúa. En sistemas de refrigeración, por ejemplo, *Evaporar* invoca al proceso completo de refrigeración por compresión para expresar el ciclo continuo del refrigerante.

---

## Enlaces estructurales

### Enlaces estructurales etiquetados

La semántica la define quien modela mediante etiquetas textuales.

| Variante | OPD | OPL-ES canónico |
|---|---|---|
| Unidireccional etiquetado | flecha abierta + etiqueta | `**Origen** etiqueta **Destino**.` |
| Unidireccional sin etiqueta | flecha abierta, sin etiqueta | `**Origen** se relaciona con **Destino**.` |
| Bidireccional etiquetado | arpones en ambos extremos + dos etiquetas | Dos oraciones OPL, una por cada dirección |
| Recíproco etiquetado | arpones + una etiqueta | `**Origen** y **Destino** son etiqueta.` |
| Recíproco sin etiqueta | arpones, sin etiqueta | `**Origen** y **Destino** se relacionan.` |

### Relaciones estructurales fundamentales

| Relación | Refinable → refinador | Símbolo OPD | OPL-ES canónico |
|---|---|---|---|
| Agregación-participación | todo → partes | triángulo negro relleno | `**Todo** consta de **Parte1**, **Parte2** y **Parte3**.` |
| Exhibición-caracterización | exhibidor → rasgos | triángulo negro pequeño dentro de triángulo vacío | `**Exhibidor** exhibe **Atributo1** así como *Operación1*.` |
| Generalización-especialización | general → especializaciones | triángulo vacío | `**Especialización1** y **Especialización2** son **General**.` |
| Clasificación-instanciación | clase → instancias | círculo negro pequeño dentro de triángulo vacío | `**Instancia** es una instancia de **Clase**.` |

Las colecciones incompletas usan una barra horizontal bajo el triángulo y en OPL-ES se expresan con `y al menos otra parte`, `y al menos otro rasgo` o `y al menos otra especialización`.

**Restricción de perseverancia:** salvo en exhibición-caracterización, el refinable y los refinadores deben tener la misma perseverancia.

Exhibición-caracterización es el único enlace estructural que puede conectar objetos con procesos: el rasgo es atributo si es objeto y operación si es proceso.

**Clasificación-instanciación:** a diferencia de las otras tres relaciones fundamentales, no distingue entre colección completa e incompleta. El número de instancias puede variar durante la operación.

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

| Grupo | Unidireccional | Bidireccional | Recíproco |
|---|---|---|---|
| Estado especificado en el origen | `**Origen** en \`estado\` etiqueta **Destino**.` | `**Origen** en \`estado\` etiqueta-f **Destino**.` / `**Destino** etiqueta-b **Origen** en \`estado\`.` | `**Destino** y **Origen** en \`estado\` son etiqueta.` |
| Estado especificado en el destino | `**Origen** etiqueta **Destino** en \`estado\`.` | — | — |
| Estado especificado en origen y destino | `**Origen** en \`sa\` etiqueta **Destino** en \`sb\`.` | `**Origen** en \`sa\` etiqueta-f **Destino** en \`sb\`.` / `**Destino** en \`sb\` etiqueta-b **Origen** en \`sa\`.` | `**Origen** en \`sa\` y **Destino** en \`sb\` son etiqueta.` |

Las variantes bidireccionales y recíprocas no existen para el caso de estado solo en el destino.

---

## Cardinalidades de relación

### Multiplicidad de objetos

La multiplicidad restringe el número de instancias de objeto asociadas a un enlace. El valor por defecto es una instancia por extremo. Aplica a enlaces etiquetados, agregación-participación y enlaces procedimentales.

| Símbolo | Límites | Lectura OPL-ES |
|---|---|---|
| `?` | 0..1 | opcional |
| `*` | 0..* | opcional, de cero a muchos |
| sin símbolo | 1..1 | por defecto |
| `+` | 1..* | al menos uno |

La sintaxis de rango es `qmín..qmáx`. Pueden usarse varios rangos separados por comas y expresiones aritméticas con `+`, `-`, `*`, `/`, `(`, `)`. Las restricciones usan `=`, `≠`, `<`, `≤`, `≥`, llaves para conjuntos y el operador `∈`.

**Los nombres de parámetros deben ser únicos en todo el modelo.**

**Las restricciones de participación no aplican a procesos.** La repetición secuencial de un proceso se modela con un proceso recurrente y contador de iteración; la repetición paralela, con subprocesos síncronos o asíncronos dentro de una descomposición.

**Declaración de tipo:** un objeto puede declarar tipo computacional.

- `**Objeto** es de tipo tipo-id.`

Tipos comunes: `boolean`, `string`, `integer`, `float`, `double`, `short`, `long`, `enumerated`.

**Ejemplos de opcionalidad:**

- `**Auto** tiene **Sunroof** opcional.`
- `**Auto** está equipado con **Airbag** opcional.`
- `**Auto** es dirigido por **Volante**.` (valor 1..1 por defecto)
- `**Auto** lleva al menos un **Neumático de Repuesto**.`

**Ejemplo paramétrico** (reemplazo de paletas): un **Motor a Reacción** consta de `b` **Paletas Instaladas**. `k` (`k=2..4`) **Mecánicos de Motor de Aviación** manejan *Reemplazar Paletas* usando `k` **Herramientas de Fijación de Paletas**. `1..2` **Ingenieros Aeroespaciales** también manejan *Reemplazar Paletas*. *Reemplazar Paletas* consume `i` **Paletas Inspeccionadas** y `(b-i)` **Paletas Nuevas**, y genera `b` **Paletas Desmontadas**.

**Ejemplo multicondición** (avión): `**Avión** consta de **Fuselaje**, 2 **Alas** y `e` **Motores**, donde `e≥1` y `e=b+2*w`.` Cada ala tiene `w` motores (`0≤w≤3`). El fuselaje tiene `b` motores (`b∈{0,1}`).

---

## Operadores lógicos: AND, XOR, OR

### AND

AND se expresa con enlaces separados, del mismo tipo, sin tocarse entre sí. En OPL-ES suele materializarse en una sola oración con `y` o en varias oraciones independientes.

### XOR

Un abanico XOR usa un arco discontinuo simple. En OPL-ES se expresa con `exactamente uno de`.

### OR

Un abanico OR usa dos arcos discontinuos concéntricos. En OPL-ES se expresa con `al menos uno de`.

### Combinatoria de abanicos de enlaces

XOR y OR aplican a todas las familias de enlaces procedimentales. El extremo convergente es el extremo común; el divergente no lo es.

**Abanicos de consumo y resultado:**

| Tipo de abanico | Visual OPD | OPL-ES para XOR | OPL-ES para OR |
|---|---|---|---|
| Consumo convergente (objetos → proceso) | `A`, `B`, `C` apuntan con punta cerrada a `P`; arco en el extremo de `P` | `*P* consume exactamente uno de **A**, **B** o **C**.` | `*P* consume al menos uno de **A**, **B** o **C**.` |
| Consumo divergente (objeto → procesos) | `B` se abre hacia `P`, `Q`, `R`; arco en el extremo de `B` | `Exactamente uno de *P*, *Q* o *R* consume **B**.` | `Al menos uno de *P*, *Q* o *R* consume **B**.` |
| Resultado convergente (procesos → objeto) | `P`, `Q`, `R` convergen a `B` | `Exactamente uno de *P*, *Q* o *R* genera **B**.` | `Al menos uno de *P*, *Q* o *R* genera **B**.` |
| Resultado divergente (proceso → objetos) | `P` se abre hacia `A`, `B`, `C` | `*P* genera exactamente uno de **A**, **B** o **C**.` | `*P* genera al menos uno de **A**, **B** o **C**.` |

**Abanicos de efecto** (bidireccionales):

| Tipo de abanico | OPL-ES para XOR | OPL-ES para OR |
|---|---|---|
| Múltiples objetos | `*P* afecta exactamente uno de **A**, **B** o **C**.` | `*P* afecta al menos uno de **A**, **B** o **C**.` |
| Múltiples procesos | `Exactamente uno de *P*, *Q* o *R* afecta **B**.` | `Al menos uno de *P*, *Q* o *R* afecta **B**.` |

**Abanicos de habilitación**:

| Tipo de abanico | OPL-ES para XOR | OPL-ES para OR |
|---|---|---|
| Agentes | `**B** maneja exactamente uno de *P*, *Q* o *R*.` | `**B** maneja al menos uno de *P*, *Q* o *R*.` |
| Instrumentos | `Exactamente uno de *P*, *Q* o *R* requiere **B**.` | `Al menos uno de *P*, *Q* o *R* requiere **B**.` |

**Abanicos de invocación:**

| Tipo de abanico | OPL-ES para XOR | OPL-ES para OR |
|---|---|---|
| Divergente | `*P* invoca exactamente uno de *Q* o *R*.` | `*P* invoca al menos uno de *Q* o *R*.` |
| Convergente | `Exactamente uno de *P* o *Q* invoca *R*.` | `Al menos uno de *P* o *Q* invoca *R*.` |

### Ejemplos visuales de AND

AND requiere **enlaces que no se tocan** en el contorno del proceso. Tres ejemplos canónicos:

- **AND de agentes:** `**Propietario de Caja Fuerte A** maneja *Abrir Caja Fuerte*.` y `**Propietario de Caja Fuerte B** maneja *Abrir Caja Fuerte*.` Ambos deben estar presentes.
- **AND de instrumentos:** `*Abrir Caja Fuerte* requiere **Llave A**, **Llave B** y **Llave C**.` Las tres llaves son necesarias.
- **AND de resultados:** `*Preparar Comida* genera **Entrada**, **Plato Principal** y **Postre**.`
- **AND de efectos entrada-salida:** `*Subir Tasa de Interés* cambia simultáneamente varios objetos desde \`bajo\` hasta \`alto\`.` 

### Abanicos de enlaces con modificadores de control

Cada abanico XOR tiene variantes de evento y de condición:

| Abanico base | Variante evento OPD | OPL-ES de evento | Variante condición OPD | OPL-ES de condición |
|---|---|---|---|---|
| Efecto (múltiples procesos) | flechas bidireccionales con `e` | `**B** inicia exactamente uno de *P*, *Q* o *R*, que afecta **B**.` | igual con `c` | `Exactamente uno de *P*, *Q* o *R* ocurre si **B** existe; de lo contrario se omite.` |
| Consumo | flechas `B→P,Q,R` con `e` | `**B** en \`s2\` inicia exactamente uno de *P*, *Q* o *R*, que consume **B**.` | igual con `c` | `Exactamente uno de *P*, *Q* o *R* ocurre si **B** está en \`s2\`; de lo contrario se omite.` |
| Agente | enlaces de agente con `e` | `**B** en \`s2\` inicia y maneja exactamente uno de *P*, *Q* o *R*.` | igual con `c` | `**B** maneja exactamente uno de *P*, *Q* o *R* si **B** está en \`s2\`; de lo contrario se omite.` |
| Instrumento | enlaces de instrumento con `e` | `**B** en \`s2\` inicia exactamente uno de *P*, *Q* o *R*, que requiere **B** en \`s2\`.` | igual con `c` | `Exactamente uno de *P*, *Q* o *R* requiere **B** en \`s2\`; de lo contrario se omite.` |

Toda variante XOR tiene su contraparte OR reemplazando `exactamente` por `al menos` y el arco simple por arco doble.

### Abanicos probabilísticos

Cada enlace del abanico se anota con `Pr=p`, y las probabilidades suman 1.

**Ejemplo numérico:** un proceso `P` puede crear `B` en tres estados: `s1` (`Pr=0.32`), `s2` (`Pr=0.24`) y `s3` (`Pr=0.44`). Si no se anotan probabilidades, la probabilidad por defecto es `1/n`.

**Ejemplo mixto:** `*P* genera uno de **A**, **B** o **C** en `sc1`, con una probabilidad distinta por enlace. Algunos objetos fuente pueden tener estado especificado y otros no.

### Trayectorias de ejecución y etiquetas de ruta

Las etiquetas de ruta resuelven ambigüedad cuando existen varias opciones de salida. La regla es: al salir de un proceso, se sigue el enlace cuya etiqueta coincide con la etiqueta de entrada.

En OPL-ES:

- `Por ruta etiqueta, *Proceso* consume **Objeto**.`
- `Por ruta etiqueta, *Proceso* genera **Objeto**.`

Un **escenario** es un conjunto de una o más etiquetas de ruta que define una variante concreta de ejecución. En sistemas complejos, los escenarios evitan crear un OPD adicional por cada variante.

**Ejemplo** (*Preparar Alimento*):

- por ruta `carnívoro`: `*Preparar Alimento* consume **Carne**, genera **Estofado** y **Bistec**.`
- por ruta `herbívoro`: `*Preparar Alimento* consume **Pepino** y **Tomate**, genera **Ensalada**.`

---

## Gestión de contexto y refinamiento

### Completar el SD

El Diagrama de Sistema debe modelar:

- interesados, especialmente beneficiarios;
- el proceso que entrega valor;
- las cosas ambientales y sistémicas necesarias para producir un párrafo OPL breve y claro.

El SD debe contener solo las cosas centrales e indispensables. El valor funcional puede aparecer explícitamente como cambio de estado de un atributo del beneficiario o de forma implícita si el beneficiario es afectado.

### Mecanismos de refinamiento y abstracción

Tres pares principales:

| Mecanismo | Refinamiento | Abstracción |
|---|---|---|
| Estados | Expresión de estados | Supresión de estados |
| Estructura | Despliegue | Plegado |
| Comportamiento | Descomposición | Recomposición |

Hay cuatro pares de despliegue-plegado, uno por relación fundamental: agregación, exhibición, generalización y clasificación.

**Despliegue en el mismo diagrama:** refinable y refinadores comparten OPD.

**Despliegue en nuevo diagrama:** se crea OPD hijo; el refinable aparece con contorno grueso en ambos diagramas.

**Diagramas de vista (model views):** OPDs que reúnen hechos provenientes de múltiples OPDs para explicar un fenómeno o enfatizar un aspecto concreto. Las herramientas OPM deben soportar la creación de vistas que filtren por criterios específicos, como:

- el camino crítico para la duración mínima de ejecución del sistema;
- los agentes e instrumentos del sistema;
- todos los objetos y procesos vinculados por un tipo específico de enlace;
- la asignación de cosas de varios OPDs a módulos del sistema.

**Mapa del sistema (system map):** un árbol de procesos OPD que muestra explícitamente el contenido (cosas y enlaces) de cada OPD como nodo. Dado que el mapa puede volverse muy grande, los mecanismos de vista permiten acceder al contenido del modelo y a las asociaciones entre elementos.

---

## Árboles OPD y control implícito

**Árbol de procesos OPD:** raíz `SD`, y cada nodo corresponde a un OPD creado por descomposición de un proceso. Es el mecanismo principal de navegación. Etiquetas típicas: `SD`, `SD1`, `SD1.1`, `SD1.1.1`, etc.

**Árbol de objetos OPD:** raíz en un objeto, muestra su elaboración por refinamiento.

La línea temporal dentro de un proceso descompuesto fluye de arriba hacia abajo. Los subprocesos cuyos puntos de referencia superiores tienen la misma altura se ejecutan en paralelo.

### Resumen de enlaces de invocación implícitos

Dos formas gobiernan la ejecución implícita en descomposición síncrona:

| Forma | Semántica | Indicio estructural |
|---|---|---|
| Invocación implícita | Un subproceso invoca al subproceso inmediatamente inferior cuando termina | puntos superiores de elipses ordenados verticalmente |
| Conjunto de invocación implícita paralela | Varios subprocesos comienzan juntos cuando sus puntos superiores están alineados | mismas alturas en el contexto de descomposición |

---

## Distribución de enlaces a través del contexto

Los enlaces conectados al **contorno exterior** de un proceso descompuesto tienen semántica distributiva: se distribuyen a todos los subprocesos, de manera análoga a paréntesis algebraicos.

Restricciones críticas:

- los enlaces de **consumo** y **resultado** no deben conectarse al contorno exterior;
- al descomponer un proceso, todos los consumos y resultados migran **por defecto al primer subproceso**, y luego se reasignan;
- los enlaces de evento desde objetos o estados sistémicos no deben cruzar el límite de la descomposición para iniciar subprocesos;
- si un enlace de condición hace que un subproceso se omita y existe un siguiente subproceso en la secuencia, el control pasa al siguiente.

**Ejemplo válido e inválido:** si `P` se descompone en `P1`, `P2`, `P3`, es válido decir que `**Agente A** maneja *P*` o que `*P* requiere **Instrumento D**` porque esos enlaces se distribuyen. Pero `*P* consume **C**` o `*P* genera **B**` sobre el contorno exterior es inválido. Lo correcto es asignar `**C**` al subproceso que realmente lo consume y `**B**` al subproceso que realmente lo genera.

---

## Enlaces transformadores escindidos con estado especificado

Cuando un enlace de efecto entrada-salida del tipo `*P* cambia **A** de \`s1\` a \`s2\`` se descompone en varios subprocesos, el modelo puede quedar subespecificado: no se sabe qué subproceso saca a `A` de `s1` ni cuál la coloca en `s2`.

Procedimiento de resolución:

1. **Caso original:** `*P* cambia **A** de \`s1\` a \`s2\`.`
2. **Caso ambiguo tras descomposición:** `P` se descompone en `P1` y `P2`, pero el efecto completo sigue unido a `P`.
3. **Caso reparado:** se usa un par escindido.

Par escindido:

| Par | Significado | Fuente | Destino |
|---|---|---|---|
| Par de efecto entrada-salida escindido | El subproceso temprano saca el objeto del estado de entrada; el tardío lo coloca en el estado de salida | estado de entrada + subproceso tardío | subproceso temprano + estado de salida |

En OPL-ES:

- `*P1* cambia **A** de \`s1\`.`
- `*P2* cambia **A** a \`s2\`.`

Ese es el único mecanismo correcto para resolver la subespecificación de efectos en procesos descompuestos.

**Cambio de rol con la abstracción:** un objeto puede ser instrumento en un nivel abstracto y afectado en un nivel detallado. Esto es válido si a nivel abstracto sus estados inicial y final coinciden.

### Instancias operacionales del conjunto de objetos involucrados (§14.2.2.4.4)

Como consecuencia de la distribución de enlaces, las siguientes restricciones se aplican a las instancias operacionales de los transformados:

1. Cada instancia operacional de un **consumido** en el conjunto previo al proceso DEBE dejar de existir al inicio del subproceso más detallado que lo consume, y la instancia operacional no está en el conjunto posterior al proceso.
2. Cada instancia operacional de un **afectado** en el conjunto previo al proceso que cambia de estado DEBE salir de su estado de entrada al inicio del subproceso más detallado que cambia al afectado.
3. Cada instancia operacional de un **afectado** en el conjunto posterior al proceso que cambia de estado DEBE entrar en su estado de salida al completarse el subproceso más detallado que cambia al afectado.
4. Cada instancia operacional de un **resultante** en el conjunto posterior al proceso DEBE comenzar a existir al completarse el subproceso más detallado que lo genera, y la instancia operacional no está en el conjunto previo al proceso.

**Nota:** para un objeto con estados `B` cuya ejecución del proceso `P` tiene el efecto de cambiar su estado, `B` sale del estado de entrada al inicio del subproceso más detallado de `P` que cambia a `B`, y entra al estado de salida al final de ese mismo subproceso o de algún subproceso posterior. Durante la ejecución, el objeto `B` está en transición entre estados: ha dejado su estado de entrada pero aún no ha llegado a su estado de salida.

---

## Precedencia de enlaces durante la recomposición

Al recomponer, los enlaces procedimentales de subprocesos migran al proceso padre. **La fuerza semántica** determina cuál prevalece cuando dos enlaces compiten por el mismo par objeto-proceso.

Matriz de precedencia de enlaces transformadores:

| B↔P1 \ B↔P2 | Efecto | Resultado | Consumo |
|---|---|---|---|
| **Efecto** | Efecto | Resultado | Consumo |
| **Resultado** | Resultado | Inválido | Efecto |
| **Consumo** | Consumo | Efecto | Inválido |

Resultado + consumo sobre el mismo objeto es inválido porque el objeto no puede ser creado y destruido como el mismo hecho abstracto.

Orden principal de precedencia:

`consumo = resultado > efecto > agente > instrumento`

Los enlaces con estado especificado tienen mayor precedencia que los básicos. Dentro de cada clase, el orden secundario es:

`evento > sin control > condición`

### Orden completo de fuerza semántica (12 niveles)

Combinando precedencia primaria y secundaria, el orden completo de fuerza semántica de los enlaces procedimentales es:

| Nivel | Enlace | > que |
|---|---|---|
| 1 | evento de consumo | > consumo |
| 2 | consumo | = resultado |
| 3 | resultado | > condición de consumo |
| 4 | condición de consumo | > evento de efecto |
| 5 | evento de efecto | > efecto |
| 6 | efecto | > condición de efecto |
| 7 | condición de efecto | > evento de agente |
| 8 | evento de agente | > agente |
| 9 | agente | > condición de agente |
| 10 | condición de agente | > evento de instrumento |
| 11 | evento de instrumento | > instrumento |
| 12 | instrumento | > condición de instrumento |

Los símbolos `=` y `>` indican equivalencia y mayor fuerza respectivamente. Un enlace de evento es más fuerte que su enlace no-control correspondiente porque además de la semántica base tiene la capacidad de iniciar un proceso. Un enlace de condición es más débil porque el modificador de condición debilita los criterios de satisfacción de la precondición.

---

## Etiquetas OPD y navegación

**El SD contiene exactamente un proceso sistémico**, que expresa la función del sistema. Puede contener uno o más procesos ambientales.

Etiquetas típicas:

- `SD` para nivel 0;
- `SD1`, `SD2`, etc., para niveles descendientes.

**Etiquetas de aristas del árbol OPD:** cada arista del árbol de procesos usa un enlace estructural etiquetado unidireccional con una fórmula de refinamiento equivalente a `se refina por descomposición de NombreProceso en` o `se refina por despliegue de NombreCosa en`. En español canónico:

- `SD se refina por descomposición de *Proceso* en SD1.`
- `SD1 se refina por despliegue de **Cosa** en SD1.1.`

**Orden de especificación OPL:** la secuencia de párrafos OPL sigue en general orden en anchura, comenzando desde `SD`.

### OPL del sistema completo

El OPL del sistema completo es la especificación textual total obtenida al recorrer el árbol OPD y concatenar los párrafos OPL locales en orden de modelo. No describe solo el contexto actual, sino la totalidad del sistema.

Núcleo recuperable del ejemplo clásico de *Sistema de Lavado de Platos*:

- `**Usuario Doméstico** maneja *Lavar Platos*.`
- `*Lavar Platos* requiere **Lavavajillas**.`
- `*Lavar Platos* consume **Jabón**.`
- `*Lavar Platos* afecta **Conjunto de Platos**.`
- `SD se refina por descomposición de *Lavar Platos* en SD1.`
- `**Lavavajillas** consta de **Compartimento de Jabón** y otras partes.`
- `**Lavavajillas** puede estar \`vacío\` o \`cargado\`.`
- `Estado \`vacío\` de **Lavavajillas** es inicial y final.`
- `**Compartimento de Jabón** puede estar \`vacío\` o \`cargado\`.`
- `Estado \`vacío\` de **Compartimento de Jabón** es inicial.`
- `**Conjunto de Platos** exhibe **Limpieza**.`
- `**Limpieza** de **Conjunto de Platos** puede estar \`sucio\` o \`limpio\`.`
- `Estado \`sucio\` de **Limpieza** de **Conjunto de Platos** es inicial.`
- `Estado \`limpio\` de **Limpieza** de **Conjunto de Platos** es final.`
- `*Lavar Platos* se descompone en *Cargar Platos*, *Insertar Detergente*, *Lavar y Secar Platos* y *Descargar Platos*, en esa secuencia.`
- `*Cargar Platos* cambia **Lavavajillas** de \`vacío\` a \`cargado\`.`
- `*Insertar Detergente* requiere **Jabón**.`
- `*Insertar Detergente* cambia **Compartimento de Jabón** de \`vacío\` a \`cargado\`.`
- `*Lavar y Secar Platos* requiere **Lavavajillas**.`
- `*Lavar y Secar Platos* consume **Jabón**.`
- `*Lavar y Secar Platos* cambia **Limpieza** de **Conjunto de Platos** de \`sucio\` a \`limpio\`.`
- `*Descargar Platos* cambia **Lavavajillas** de \`cargado\` a \`vacío\`.`

**Simplificación de OPD:** la recomposición dentro del mismo diagrama y la descomposición en nuevo diagrama pueden simplificar un OPD sobrecargado. Restricción: un objeto no puede incorporarse al conjunto abstraído si eso crearía enlaces procedimentales directos entre procesos pares sin semántica OPM.

### Tabla 26 — Especificación OPL completa del Sistema de Lavado de Platos

| Especificación OPL del **Sistema de Lavado de Platos** |
|---|
| **SD: Sistema de Lavado de Platos** |
| `**Usuario Doméstico** maneja *Lavar Platos*.` |
| `*Lavar Platos* requiere **Lavavajillas**.` |
| `*Lavar Platos* consume **Jabón**.` |
| `*Lavar Platos* afecta **Conjunto de Platos**.` |
| `SD se refina por descomposición de *Lavar Platos* en SD1.` |
| **SD1: *Lavar Platos* descompuesto** |
| `**Lavavajillas** consta de **Compartimento de Jabón** y otras partes.` |
| `**Lavavajillas** puede estar \`vacío\` o \`cargado\`.` |
| `  Estado \`vacío\` de **Lavavajillas** es inicial y final.` |
| `**Compartimento de Jabón** puede estar \`vacío\` o \`cargado\`.` |
| `  Estado \`vacío\` de **Compartimento de Jabón** es inicial.` |
| `**Conjunto de Platos** exhibe **Limpieza**.` |
| `  **Limpieza** de **Conjunto de Platos** puede estar \`sucio\` o \`limpio\`.` |
| `  Estado \`sucio\` de **Limpieza** de **Conjunto de Platos** es inicial.` |
| `  Estado \`limpio\` de **Limpieza** de **Conjunto de Platos** es final.` |
| `**Usuario Doméstico** maneja *Lavar Platos*.` |
| `*Lavar Platos* se descompone en *Cargar Platos*, *Insertar Detergente*, *Lavar y Secar Platos* y *Descargar Platos*, en esa secuencia.` |
| `  *Cargar Platos* cambia **Lavavajillas** de \`vacío\` a \`cargado\`.` |
| `  *Insertar Detergente* requiere **Jabón**.` |
| `  *Insertar Detergente* cambia **Compartimento de Jabón** de \`vacío\` a \`cargado\`.` |
| `  *Lavar y Secar Platos* requiere **Lavavajillas**.` |
| `  *Lavar y Secar Platos* consume **Jabón**.` |
| `  *Lavar y Secar Platos* cambia **Limpieza** de **Conjunto de Platos** de \`sucio\` a \`limpio\`.` |
| `  *Descargar Platos* cambia **Lavavajillas** de \`cargado\` a \`vacío\`.` |
| Fin de especificación OPL del **Sistema de Lavado de Platos** |

### Principio de consistencia de hechos OPM

Si un hecho aparece en un OPD y contradice otro hecho del mismo modelo en otro OPD, el modelo es inconsistente y la herramienta debería detectarlo. Que un hecho sea refinamiento o abstracción de otro no constituye contradicción.

---

## Diagrama de sistema: procedimiento y componentes

El SD es el OPD de nivel 0 y proporciona una vista de alto nivel comprensible para cualquier interesado, incluso sin especialización técnica.

Cinco componentes para sistemas artificiales y sociotécnicos, y tres para sistemas naturales:

### 1. Propósito

Quién se beneficia y qué valor recibe. Suele expresarse como cambio de estado en un atributo del beneficiario, desde un estado problemático a uno satisfactorio. En sistemas naturales se habla más bien de **resultado** que de propósito.

### 2. Función principal

Combinación del proceso principal y el objeto operando. El nombre funcional puede formarse como objeto + proceso, por ejemplo `Pintar Auto`. El proceso principal transforma el operando mediante un enlace transformador.

### 3. Habilitadores

Objetos requeridos por el proceso pero no transformados por él.

- **Agentes:** personas o grupos; en sistemas naturales no hay agentes humanos.
- **Instrumentos:** objetos no humanos; el propio sistema suele ser el instrumento principal. El nombre por defecto del sistema es función + `Sistema`.

### 4. Entorno

Cosas fuera del sistema que afectan su operación. La afiliación sistémica o ambiental se determina por el atributo de afiliación.

### 5. Ocurrencia del problema

Imagen espejo de propósito y función. Un proceso ambiental provoca que el atributo del beneficiario se encuentre en el estado problemático. No aplica a sistemas naturales.

### Procedimiento de construcción del SD

Proceso guiado de nueve etapas:

1. **Proceso principal:** "¿Cuál es el proceso principal del sistema?"
2. **Beneficiario:** "¿Quién es el beneficiario?"
3. **Atributo del beneficiario:** "¿Qué atributo expresa el valor?"
4. **Agente:** "¿El beneficiario es también el agente?"
5. **Nombre del sistema:** "¿Cómo se llama el sistema?"
6. **Instrumentos:** "¿Qué instrumentos requiere?"
7. **Entradas:** "¿Cuáles son las entradas?"
8. **Salidas:** "¿Cuál es la salida?"
9. **Objetos ambientales:** "¿Qué objetos ambientales se asocian?"

### Jerarquía de detalle (SD1)

Cuando un OPD se vuelve demasiado complejo, se crea un OPD descendiente.

- **Refinamiento de proceso:** síncrono por descomposición o asíncrono por despliegue.
- **Refinamiento de objeto:** despliegue en partes y atributos.
- **Expresión de estados:** estados suprimidos en el SD aparecen en `SD1` enlazados a subprocesos.

**Regla normativa síncrono vs asíncrono (§14.2.2.5):** dado que la relación estructural fundamental de agregación-participación no prescribe ningún "orden parcial" de ejecución de procesos, el modelado de refinamiento síncrono de procesos DEBE usar descomposición (in-zooming). El modelado de refinamiento asíncrono de procesos DEBE usar el enlace estructural fundamental de agregación-participación, ya sea por despliegue de agregación en el mismo diagrama o en nuevo diagrama.

---

## Tipos de sistema y variaciones del SD

### Sistemas artificiales

Aplican los cinco componentes completos: propósito, función principal, habilitadores, entorno y ocurrencia del problema.

### Sistemas naturales

Aplican solo tres:

- función principal;
- instrumentos;
- entorno.

El propósito se reemplaza por **resultado**, beneficioso o perjudicial para grupos afectados. No existe "ocurrencia del problema" en sentido de diseño intencional.

### Sistemas sociales

Aplican los cinco componentes. Los agentes suelen ser el núcleo del modelo, y los instrumentos incluyen instalaciones y equipamiento.

### Sistemas sociotécnicos

Son sistemas complejos con muchos componentes que interactúan de múltiples formas y exigen coordinación entre especialistas de disciplinas distintas. OPM ofrece una especificación común que ayuda a evitar diseños desordenados, incompletos o poco claros.

---

## Nodos de decisión y comportamiento condicional

### Nodos de decisión

Un **nodo de decisión** es un objeto informacional que representa un punto de elección. La mejor práctica es nombrarlo como pregunta.

Un **objeto booleano** es un nodo de decisión con dos estados opuestos, típicamente `sí` y `no`.

### Enlace instrumental condicional vs no condicional

Diferencia crítica:

- **Instrumento condicional** (`c`): si el instrumento no existe o no está en el estado requerido, el proceso se **omite** y la ejecución continúa.
- **Instrumento no condicional**: si el instrumento falta, la ejecución **se detiene y espera**.

Esto define si el sistema falla de forma elegante o queda bloqueado.

### Subprocesos iterativos

La iteración se modela con nodos de decisión más enlaces de invocación. Después de cada ciclo, el nodo booleano decide si se vuelve atrás o se sigue. La invocación de retorno no debe violar el orden temporal de arriba hacia abajo dentro de una descomposición.

### Orden espacial en la descomposición de objetos

En la descomposición de objetos, la posición espacial de los objetos constituyentes tiene significado, a diferencia de la descomposición de procesos donde lo crítico es la línea temporal vertical. El orden espacial aplica tanto a objetos físicos como a objetos informacionales.

---

## Ingeniería de sistemas basada en modelos con OPM

### Visión general de MBSE

La Ingeniería de Sistemas Basada en Modelos (MBSE) usa modelos conceptuales para diseñar y desarrollar sistemas complejos. Los enfoques tradicionales basados en texto carecen de lenguaje estandarizado y de verificación o validación formales. OPM resuelve eso mediante especificación formal bimodal.

### Conceptos alternativos de solución

Procedimiento recomendado para generar alternativas:

1. crear al menos tres modelos conceptuales distintos;
2. aplicar pensamiento creativo holístico;
3. destilar el concepto central de cada uno;
4. explicitar los supuestos implícitos.

Un **concepto** es el principio físico o lógico central de una arquitectura. Los **conceptos alternativos de solución** son enfoques arquitectónicos distintos para un mismo problema.

### Revisión preliminar de diseño (PDR)

Una PDR estructurada incluye ocho secciones:

1. portada;
2. formulación del problema;
3. propósito y motivación;
4. supuestos y restricciones;
5. soluciones alternativas;
6. solución seleccionada con justificación;
7. costos de ciclo de vida y cronograma;
8. riesgos y mecanismos de mitigación.

### OPM como plano común

OPM sirve como especificación neutral entre disciplinas para el diseño detallado de sistemas complejos donde cada disciplina tiene su propio lenguaje. Los modelos detallados suelen abarcar entre **5 y 10 niveles de detalle** en el árbol de procesos OPD.

### Integración virtual

La integración virtual combina modelos conceptuales de hardware con módulos de software ejecutable real. El software controla virtualmente los modelos de hardware, lo que permite validar antes del prototipado físico.

---

## Sintaxis formal de OPL: EBNF central

La gramática formal de referencia en ISO/PAS 19450 usa terminales ingleses. En esta edición se ofrece la forma **canónica española**, alineada con `opm-opl-es.md`. Las reglas de producción se preservan; cambian los terminales léxicos y ciertas convenciones de superficie.

### Estructura del documento

```ebnf
parrafo_opl_es = oracion_opl_es, { salto_de_linea, oracion_opl_es } ;
oracion_opl_es = oracion_formal_opl_es, "." ;
oracion_formal_opl_es = oracion_de_descripcion_de_cosa
 | oracion_procedimental
 | oracion_estructural
 | oracion_de_gestion_de_contexto ;
```

### Declaraciones base

```ebnf
digito_no_cero = '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' ;
digito_decimal = '0' | digito_no_cero ;
entero_positivo = digito_no_cero, {digito_decimal} ;
nombre = letra, {caracter_de_cadena} ;
palabra_capitalizada = letra_mayuscula, {caracter_de_cadena} ;
palabra_no_capitalizada = letra_minuscula, {caracter_de_cadena} ;
identificador_de_tipo = "boolean" | "string" | tipo_numerico | "enumerated" ;
tipo_numerico = [prefijo], "integer" | "float" | "double" | "short" | "long" ;
restriccion_de_participacion = singular_inferior | singular_superior | plural_inferior | plural_superior
 | ( "0" | limite_de_participacion, [ " a ", limite_de_participacion ] ) ;
singular_inferior = "un" | "una" | "un opcional" | "una opcional" | "al menos un" | "al menos una" ;
clausula_de_rango = " es ", nombre_de_valor | " varía de ", nombre_de_valor, " a ", nombre_de_valor ;
```

### Identificadores

```ebnf
identificador_de_objeto = nombre_singular_de_objeto, [ " en ", unidad_de_medida ], [ clausula_de_rango ] ;
identificador_de_proceso = nombre_singular_de_proceso | nombre_singular_de_proceso, " proceso" ;
identificador_de_cosa = identificador_de_objeto | identificador_de_proceso ;
identificador_de_estado = palabra_no_capitalizada ;
expresion_de_etiqueta = frase_no_capitalizada ;
```

Convenciones:

- nombres de objeto: sintagmas nominales en singular, con mayúscula en palabras léxicas;
- nombres de proceso: infinitivo o nominalización técnica canónica del dominio;
- nombres de estado: en minúscula;
- etiquetas: frases breves en minúscula.

---

## Oraciones de descripción de cosas

```ebnf
oracion_de_propiedad_generica = identificador_de_cosa, " es ", [esencia], [afiliacion], [perseverancia] ;
oracion_de_enumeracion_de_estados = identificador_de_objeto, " puede estar ", lista_de_estados | "..., y otros estados" ;
oracion_de_estados_iniciales = "Estado ", identificador_de_estado, " de ", identificador_de_objeto, " es inicial" ;
oracion_de_estados_finales = "Estado ", identificador_de_estado, " de ", identificador_de_objeto, " es final" ;
oracion_de_estado_por_defecto = "Estado ", identificador_de_estado, " de ", identificador_de_objeto, " es por defecto" ;
```

Esencia: `Física` o `Informacional`. Afiliación: `Sistémica` o `Ambiental`. Perseverancia: `Persistente` o `Transitoria`.

## Oraciones procedimentales

```ebnf
oracion_procedimental = oracion_transformadora | oracion_habilitadora | oracion_de_control ;
oracion_transformadora = oracion_de_consumo | oracion_de_resultado | oracion_de_efecto | oracion_de_cambio ;

oracion_de_consumo = identificador_de_proceso, " consume ", objeto_con_opcion_de_estado ;
oracion_de_resultado = identificador_de_proceso, " genera ", objeto_con_opcion_de_estado ;
oracion_de_efecto = identificador_de_proceso, " afecta ", lista_de_objetos ;
oracion_de_cambio = oracion_de_cambio_entrada_salida | oracion_de_cambio_solo_entrada
 | oracion_de_cambio_solo_salida ;

frase_de_cambio_entrada_salida = identificador_de_objeto, " de ", estado_de_entrada, " a ", estado_de_salida ;
frase_de_cambio_solo_entrada = identificador_de_objeto, " de ", estado_de_entrada ;
frase_de_cambio_solo_salida = identificador_de_objeto, " a ", estado_de_salida ;

oracion_habilitadora = oracion_de_agente | oracion_de_instrumento ;
oracion_de_agente = objeto_con_opcion_de_estado, " maneja ", identificador_de_proceso ;
oracion_de_instrumento = identificador_de_proceso, " requiere ", objeto_con_opcion_de_estado ;

oracion_de_control = oracion_de_evento | oracion_de_condicion | oracion_de_invocacion | oracion_de_excepcion ;
oracion_de_evento_de_consumo = objeto_con_opcion_de_estado, " inicia ", identificador_de_proceso,
 ", que consume ", identificador_de_objeto ;
oracion_de_evento_de_efecto = identificador_de_objeto, " inicia ", identificador_de_proceso,
 ", que afecta ", identificador_de_objeto ;
oracion_de_evento_de_agente = objeto_con_opcion_de_estado, " inicia y maneja ", identificador_de_proceso ;
oracion_de_evento_de_instrumento = objeto_con_opcion_de_estado, " inicia ", identificador_de_proceso,
 ", que requiere ", objeto_con_opcion_de_estado ;

oracion_de_invocacion = identificador_de_proceso, " invoca ", lista_de_procesos
 | identificador_de_proceso, " se invoca a sí mismo" ;
oracion_de_excepcion_por_sobretiempo = identificador_de_proceso_activo,
 " ocurre si duración de ", identificador_de_proceso, " excede ", max_duracion_unidades_tiempo ;
oracion_de_excepcion_por_subtiempo = identificador_de_proceso_activo,
 " ocurre si duración de ", identificador_de_proceso, " es menor que ", min_duracion_unidades_tiempo ;
```

Las variantes XOR y OR usan `exactamente uno de` y `al menos uno de`. Las oraciones de condición siguen el patrón `ocurre si ... en cuyo caso ... de lo contrario ... se omite`.

### Oraciones de condición (EBNF completo)

```ebnf
oracion_de_condicion = oracion_transformadora_condicional | oracion_habilitadora_condicional ;

oracion_transformadora_condicional = oracion_de_consumo_condicional
 | oracion_de_consumo_condicional_con_estado
 | oracion_de_efecto_condicional ;

oracion_de_consumo_condicional = ( identificador_de_proceso, " ocurre si ", identificador_de_objeto,
 " existe, en cuyo caso ", identificador_de_objeto, " se consume, de lo contrario ",
 identificador_de_proceso, " se omite" )
 | ( "Si ", identificador_de_objeto, " existe entonces ", identificador_de_proceso,
 " ocurre y consume ", identificador_de_objeto, ", de lo contrario se omite ",
 identificador_de_proceso ) ;

oracion_de_consumo_condicional_con_estado = ( identificador_de_proceso, " ocurre si ",
 identificador_de_objeto, " está en ", estado_de_entrada, ", en cuyo caso ",
 identificador_de_objeto, " se consume, de lo contrario ", identificador_de_proceso, " se omite" ) ;

oracion_de_efecto_condicional = oracion_de_efecto_condicional_simple
 | oracion_de_efecto_entrada_salida_condicional
 | oracion_de_efecto_entrada_condicional
 | oracion_de_efecto_salida_condicional ;

oracion_de_efecto_condicional_simple = identificador_de_proceso, " ocurre si ",
 identificador_de_objeto, " existe, en cuyo caso ", identificador_de_proceso,
 " afecta ", identificador_de_objeto, ", de lo contrario ", identificador_de_proceso, " se omite" ;

oracion_de_efecto_entrada_salida_condicional = identificador_de_proceso, " ocurre si ",
 identificador_de_objeto, " está en ", estado_de_entrada, ", en cuyo caso ",
 identificador_de_proceso, " cambia ", identificador_de_objeto, " de ", estado_de_entrada,
 " a ", estado_de_salida, ", de lo contrario ", identificador_de_proceso, " se omite" ;

oracion_de_efecto_entrada_condicional = identificador_de_proceso, " ocurre si ",
 identificador_de_objeto, " está en ", estado_de_entrada, ", en cuyo caso ",
 identificador_de_proceso, " cambia ", identificador_de_objeto, " de ", estado_de_entrada,
 ", de lo contrario ", identificador_de_proceso, " se omite" ;

oracion_de_efecto_salida_condicional = identificador_de_proceso, " ocurre si ",
 identificador_de_objeto, " existe, en cuyo caso ", identificador_de_proceso,
 " cambia ", identificador_de_objeto, " a ", estado_de_salida,
 ", de lo contrario ", identificador_de_proceso, " se omite" ;

oracion_habilitadora_condicional = oracion_de_agente_condicional
 | oracion_de_instrumento_condicional ;

oracion_de_agente_condicional = ( objeto_con_opcion_de_estado, " maneja ",
 identificador_de_proceso, " si ", identificador_de_objeto, " existe; de lo contrario ",
 identificador_de_proceso, " se omite" )
 | ( objeto_con_opcion_de_estado, " maneja ", identificador_de_proceso, " si ",
 identificador_de_objeto, " está en ", identificador_de_estado, ", de lo contrario ",
 identificador_de_proceso, " se omite" ) ;

oracion_de_instrumento_condicional = ( identificador_de_proceso, " ocurre si ",
 identificador_de_objeto, " existe; de lo contrario ", identificador_de_proceso, " se omite" )
 | ( identificador_de_proceso, " ocurre si ", identificador_de_objeto, " está en ",
 identificador_de_estado, ", de lo contrario ", identificador_de_proceso, " se omite" ) ;
```

### Producciones adicionales: restricciones de expresión y listas con orden

```ebnf
(* --- Restricciones de expresión para multiplicidad --- *)

restriccion_de_expresion = "donde ", nombre, ( ( operacion_logica, nombre_de_valor )
 | ( inicio_conjunto, ( nombre | nombre_de_valor ),
 { ",", ( nombre | nombre_de_valor ) }, fin_conjunto ) ) ;

operacion_logica = "=" | "<" | ">" | "<=" | ">=" ;
inicio_conjunto = " en {" ;
fin_conjunto = "}" ;

(* --- Listas bifurcadas con orden --- *)

conjunto_de_cosas_objeto = cosa_objeto, [ { ", ", cosa_objeto } ],
 " y ", ( cosa_objeto | "más" ),
 [ ( ", ordenados por ", criterio_de_orden ) | ( ", en esa secuencia" ) ] ;

conjunto_de_cosas_proceso = cosa_proceso, [ { ", ", cosa_proceso } ],
 " y ", ( cosa_proceso | "más" ),
 [ ( ", ordenados por ", criterio_de_orden ) | ( ", en esa secuencia" ) ] ;

criterio_de_orden = nombre ;
cosa_objeto = [ restriccion_de_participacion, " " ], objeto_con_opcion_de_estado ;
cosa_proceso = [ restriccion_de_participacion, " " ], identificador_de_proceso ;

(* --- Especialización XOR y herencia múltiple --- *)

oracion_de_especializacion_xor_objeto = oracion_basica_xor_objeto
 | oracion_xor_objeto_separada_por_comas ;
oracion_basica_xor_objeto = objeto_especial, " puede ser ",
 identificador_de_objeto, " o ", identificador_de_objeto ;
oracion_xor_objeto_separada_por_comas = objeto_especial, " puede ser uno de ",
 identificador_de_objeto, { ", ", identificador_de_objeto }, " o ", identificador_de_objeto ;

oracion_de_herencia_multiple_objeto = objeto_especial, " es ",
 lista_de_objetos_generales ;
lista_de_objetos_generales = " un ", identificador_de_objeto,
 [ { " un ", identificador_de_objeto } ], " y un ", identificador_de_objeto ;
```

## Oraciones estructurales

```ebnf
oracion_estructural = oracion_de_enlace_estructural_etiquetado | oracion_de_agregacion
 | oracion_de_caracterizacion | oracion_de_exhibicion
 | oracion_de_especializacion | oracion_de_instanciacion ;

(* --- Oraciones de enlace estructural etiquetado --- *)

oracion_de_enlace_estructural_etiquetado = oracion_etiquetado_unidireccional
 | oracion_etiquetado_bidireccional ;

oracion_etiquetado_unidireccional = oracion_etiquetado_unidireccional_simple
 | oracion_etiquetado_bifurcada ;

oracion_etiquetado_unidireccional_simple =
 oracion_etiquetado_nullTag_objeto
 | oracion_etiquetado_nullTag_proceso
 | oracion_etiquetado_nonNullTag_objeto
 | oracion_etiquetado_nonNullTag_proceso ;

oracion_etiquetado_nullTag_objeto = [restriccion_participacion, " "],
 objeto_origen, etiqueta_nula_unidireccional, [restriccion_participacion, " "], objeto_destino ;
oracion_etiquetado_nullTag_proceso = [restriccion_participacion, " "],
 proceso_origen, etiqueta_nula_unidireccional, [restriccion_participacion, " "], proceso_destino ;
oracion_etiquetado_nonNullTag_objeto = [restriccion_participacion, " "],
 objeto_origen, " ", etiqueta_directa, " ", [restriccion_participacion, " "], objeto_destino,
 [", ", restriccion_de_expresion] ;
oracion_etiquetado_nonNullTag_proceso = [restriccion_participacion, " "],
 proceso_origen, " ", etiqueta_directa, " ", [restriccion_participacion, " "], proceso_destino ;

etiqueta_nula_unidireccional = " se relaciona con "
 | etiqueta_nula_definida_por_usuario ;

(* Variantes bifurcadas: listas de refinadores con orden o secuencia *)
oracion_etiquetado_bifurcada = oracion_bifurcada_nullTag_objeto
 | oracion_bifurcada_nullTag_proceso
 | oracion_bifurcada_nonNullTag_objeto
 | oracion_bifurcada_nonNullTag_proceso ;

oracion_bifurcada_nullTag_objeto = [restriccion_participacion, " "], objeto_origen,
 etiqueta_nula_unidireccional, conjunto_de_cosas_objeto ;
oracion_bifurcada_nullTag_proceso = [restriccion_participacion, " "], proceso_origen,
 etiqueta_nula_unidireccional, conjunto_de_cosas_proceso ;
oracion_bifurcada_nonNullTag_objeto = [restriccion_participacion, " "], objeto_origen,
 " ", etiqueta_directa, " ", conjunto_de_cosas_objeto ;
oracion_bifurcada_nonNullTag_proceso = [restriccion_participacion, " "], proceso_origen,
 " ", etiqueta_directa, " ", conjunto_de_cosas_proceso ;

conjunto_de_cosas_objeto = objeto_con_opcion, [ { ", ", objeto_con_opcion } ], " y ", ( objeto_con_opcion | "más" ),
 [ ( ", ordenados por ", criterio_de_orden ) | ( ", en esa secuencia" ) ] ;
conjunto_de_cosas_proceso = proceso_con_opcion, [ { ", ", proceso_con_opcion } ], " y ", ( proceso_con_opcion | "más" ),
 [ ( ", ordenados por ", criterio_de_orden ) | ( ", en esa secuencia" ) ] ;

(* Variantes bidireccionales *)
oracion_etiquetado_bidireccional = oracion_bidireccional_asimetrica_objeto
 | oracion_bidireccional_asimetrica_proceso
 | oracion_bidireccional_simetrica_objeto
 | oracion_bidireccional_simetrica_proceso ;

oracion_bidireccional_asimetrica_objeto = ( [restriccion_participacion, " "],
 objeto_origen, etiqueta_directa_bidireccional, [restriccion_participacion, " "], objeto_destino,
 [", ", restriccion_de_expresion] )
 | ( [restriccion_participacion, " "], objeto_destino, etiqueta_inversa_bidireccional,
 [restriccion_participacion, " "], objeto_origen, [", ", restriccion_de_expresion] ) ;
oracion_bidireccional_simetrica_objeto = ( [restriccion_participacion, " "],
 objeto_origen, " y ", [restriccion_participacion, " "], objeto_destino, " son ", etiqueta_simetrica )
 | ( [restriccion_participacion, " "], objeto_origen, " y ", [restriccion_participacion, " "],
 objeto_destino, " se relacionan" ) ;

etiqueta_simetrica = expresion_de_etiqueta ;
etiqueta_directa_bidireccional = expresion_de_etiqueta ;
etiqueta_inversa_bidireccional = expresion_de_etiqueta ;
etiqueta_nula_bidireccional = " se relacionan"
 | etiqueta_nula_definida_por_usuario ;

(* --- Oraciones de estructuras fundamentales --- *)

oracion_de_agregacion = oracion_de_agregacion_objeto | oracion_de_agregacion_proceso ;
oracion_de_agregacion_objeto = objeto_todo, " consta de ", lista_de_partes_objeto ;
oracion_de_agregacion_proceso = proceso_todo, " consta de ", lista_de_partes_proceso ;
lista_de_partes_objeto = parte_objeto, [ { ", ", parte_objeto } ], " y ", ( parte_objeto | "al menos otra parte" ) ;
lista_de_partes_proceso = parte_proceso, [ { ", ", parte_proceso } ], " y ", ( parte_proceso | "al menos otra parte" ) ;
parte_objeto = [restriccion_participacion, " "], identificador_de_objeto ;
parte_proceso = [restriccion_participacion, " "], identificador_de_proceso ;

oracion_de_caracterizacion = oracion_de_caract_objeto | oracion_de_caract_proceso ;
oracion_de_caract_objeto = identificador_de_objeto, " exhibe ",
 ( lista_de_atributos | lista_de_operadores
 | lista_de_atributos, ", así como ", lista_de_operadores ) ;
oracion_de_caract_proceso = identificador_de_proceso, " exhibe ",
 ( lista_de_operadores | lista_de_atributos
 | lista_de_operadores, ", así como ", lista_de_atributos ) ;

oracion_de_exhibicion = rasgo, " de ", identificador_de_objeto, ( clausula_de_rango | " es ", ",",
 ( ( lista_de_atributos | lista_de_operadores ) | ( lista_de_atributos, ", así como ", lista_de_operadores ) ) ) ;

oracion_de_especializacion = oracion_de_especializacion_objeto | oracion_de_especializacion_proceso
 | oracion_de_especializacion_estado ;
oracion_de_especializacion_objeto = lista_de_objetos_especiales, " son ", identificador_de_objeto ;
oracion_de_especializacion_proceso = lista_de_procesos_especiales, " son ", identificador_de_proceso ;
oracion_de_especializacion_estado = lista_de_objetos_con_estado, " son ", objeto_con_estado ;

oracion_de_instanciacion = oracion_de_instanciacion_objeto | oracion_de_instanciacion_proceso ;
oracion_de_instanciacion_objeto = identificador_de_objeto, " es una instancia de ", identificador_de_objeto
 | lista_de_objetos_instancia, " son instancias de ", identificador_de_objeto ;
oracion_de_instanciacion_proceso = identificador_de_proceso, " es una instancia de ", identificador_de_proceso
 | lista_de_procesos_instancia, " son instancias de ", identificador_de_proceso ;

atributo = identificador_de_objeto ;
operador = identificador_de_proceso ;
rasgo = atributo | operador ;
```

## Oraciones de gestión de contexto

```ebnf
oracion_de_gestion_de_contexto = oracion_de_despliegue | oracion_de_plegado
 | oracion_de_descomposicion | oracion_de_recomposicion ;

(* --- Oraciones de despliegue (unfolding) --- *)

oracion_de_despliegue = oracion_de_despliegue_objeto | oracion_de_despliegue_proceso ;

oracion_de_despliegue_objeto = oracion_de_despliegue_objeto_inespecificado
 | oracion_de_despliegue_objeto_todo
 | oracion_de_despliegue_objeto_general
 | oracion_de_despliegue_objeto_clase
 | oracion_de_despliegue_objeto_exhibidor ;

oracion_de_despliegue_objeto_inespecificado = identificador_de_objeto,
 " se despliega en ", lista_de_atributos, [", así como ", lista_de_operadores] ;
oracion_de_despliegue_objeto_todo = objeto_todo, " desde ", opd_padre,
 " se despliega por partes en ", opd_hijo, " en ", lista_de_partes_objeto ;
oracion_de_despliegue_objeto_general = objeto_general, " desde ", opd_padre,
 " se despliega por especialización en ", opd_hijo, " en ", lista_de_objetos_especiales ;
oracion_de_despliegue_objeto_clase = clase_de_objeto, " desde ", opd_padre,
 " se despliega por instanciación en ", opd_hijo, " en ", lista_de_objetos_instancia ;
oracion_de_despliegue_objeto_exhibidor = identificador_de_objeto, " desde ", opd_padre,
 " se despliega por rasgos en ", opd_hijo, " en ", lista_de_atributos, [", así como ", lista_de_operadores] ;

oracion_de_despliegue_proceso = oracion_de_despliegue_proceso_inespecificado
 | oracion_de_despliegue_proceso_todo
 | oracion_de_despliegue_proceso_general
 | oracion_de_despliegue_proceso_clase
 | oracion_de_despliegue_proceso_exhibidor ;

oracion_de_despliegue_proceso_inespecificado = identificador_de_proceso,
 " se despliega en ", lista_de_operadores, [", así como ", lista_de_atributos] ;
oracion_de_despliegue_proceso_todo = proceso_todo, " desde ", opd_padre,
 " se despliega por partes en ", opd_hijo, " en ", lista_de_partes_proceso ;
oracion_de_despliegue_proceso_general = proceso_general, " desde ", opd_padre,
 " se despliega por especialización en ", opd_hijo, " en ", lista_de_procesos_especiales ;
oracion_de_despliegue_proceso_clase = clase_de_proceso, " desde ", opd_padre,
 " se despliega por instanciación en ", opd_hijo, " en ", lista_de_procesos_instancia ;
oracion_de_despliegue_proceso_exhibidor = identificador_de_proceso, " desde ", opd_padre,
 " se despliega por rasgos en ", opd_hijo, " en ", lista_de_operadores, [", así como ", lista_de_atributos] ;

(* --- Oraciones de plegado (folding) --- *)

oracion_de_plegado = oracion_de_plegado_objeto | oracion_de_plegado_proceso ;
oracion_de_plegado_objeto = identificador_de_objeto, " se pliega en ", opd_hijo ;
oracion_de_plegado_proceso = identificador_de_proceso, " se pliega en ", opd_hijo ;

(* --- Oraciones de descomposición (in-zooming) --- *)

oracion_de_descomposicion = oracion_de_descomposicion_en_diagrama
 | oracion_de_descomposicion_en_nuevo_diagrama ;

oracion_de_descomposicion_en_diagrama = ( identificador_de_proceso, " se descompone en ",
 lista_de_procesos, ", en esa secuencia", [", así como ", lista_de_objetos_en_zoom] )
 | ( identificador_de_proceso, " se descompone en paralelo ", lista_de_procesos,
 [", así como ", lista_de_objetos_en_zoom] )
 | ( identificador_de_proceso, " se descompone en ", lista_de_procesos,
 " y en paralelo ", lista_de_procesos, ", en esa secuencia",
 [", así como ", lista_de_objetos_en_zoom] ) ;

oracion_de_descomposicion_en_nuevo_diagrama = ( identificador_de_proceso, " desde ", opd_padre,
 " se descompone en ", opd_hijo, " en ", lista_de_procesos, ", en esa secuencia",
 [", así como ", lista_de_objetos_en_zoom] )
 | ( identificador_de_proceso, " desde ", opd_padre,
 " se descompone en ", opd_hijo, " en paralelo ", lista_de_procesos,
 [", así como ", lista_de_objetos_en_zoom] )
 | ( identificador_de_proceso, " desde ", opd_padre,
 " se descompone en ", opd_hijo, " en ", lista_de_procesos,
 " y en paralelo ", lista_de_procesos, ", en esa secuencia",
 [", así como ", lista_de_objetos_en_zoom] ) ;

oracion_de_descomposicion_objeto_en_diagrama = ( identificador_de_objeto, " se descompone en ",
 lista_de_objetos, ", en esa secuencia", [", así como ", lista_de_procesos_en_zoom] ) ;

oracion_de_descomposicion_objeto_en_nuevo_diagrama = ( identificador_de_objeto, " desde ", opd_padre,
 " se descompone en ", opd_hijo, " en ", lista_de_objetos, ", en esa secuencia",
 [", así como ", lista_de_procesos_en_zoom] ) ;

lista_de_objetos_en_zoom = identificador_de_objeto, [ { ", ", identificador_de_objeto } ], " y ", identificador_de_objeto,
 ", en esa secuencia" ;
lista_de_procesos_en_zoom = identificador_de_proceso, [ { ", ", identificador_de_proceso } ] ;

(* --- Oraciones de recomposición (out-zooming) --- *)

oracion_de_recomposicion = oracion_de_recomposicion_proceso | oracion_de_recomposicion_objeto ;
oracion_de_recomposicion_proceso = identificador_de_proceso, " se recompone desde ", opd_hijo ;
oracion_de_recomposicion_objeto = identificador_de_objeto, " se recompone desde ", opd_hijo ;
```

Para subprocesos paralelos, la forma abreviada es:

- `*Proceso* se descompone en paralelo *A* y *B*.`

Para subprocesos mixtos (secuenciales y paralelos):

- `*Proceso* se descompone en *A*, paralelo *B* y *C*, y *D*, en esa secuencia.`

---

## Metamodelo OPM

La estructura del modelo OPM tiene dos jerarquías paralelas:

- **Modelo OPM** → conjunto de OPDs (gráfico) + especificación OPL (texto)
- **Conjunto de OPDs** → OPDs → constructos OPD → conjuntos de cosas + conjuntos de enlaces
- **Especificación OPL** → párrafos OPL → oraciones OPL → frases y nombres reservados

Un **constructo básico** contiene exactamente 2 cosas y 1 enlace. Los constructos compuestos incluyen abanicos de enlaces o más de dos refinadores.

## Modelo de enlace

Un enlace consta de:

- origen;
- destino;
- conector;
- línea;
- símbolo;
- etiqueta opcional;
- nombre de ruta opcional.

La multiplicidad tiene límites inferior y superior: `0..1`, `0..*`, `1..1`, `1..*`.

## Modelo de cosa

Una cosa es:

- **objeto**, o
- **proceso**.

Los objetos pueden ser sin estados o con estados. Los objetos con estados generan referencias a estados específicos.

**Objeto Específico de Estado (State-Specific Object).** Un objeto con estados que tiene `s` estados genera un conjunto de `s` **objetos específicos de estado**, cada uno de los cuales es una especialización sin estados del objeto original que "refiere a" un estado concreto. El concepto permite simplificar el modelo conceptual: cuando se necesita referenciar un objeto en un estado particular, se puede tratar como un objeto independiente sin estados. Por ejemplo, un **Producto** con estados `diseñado`, `fabricado`, `probado`, `comprado` y `usado` genera cinco especializaciones: **Producto Diseñado**, **Producto Fabricado**, etc. Cada una refiere al estado correspondiente de **Producto** mediante un enlace estructural etiquetado `refiere al estado de`.

- Un objeto sin estados tiene un conjunto de estados de cardinalidad `s=0`.
- Un objeto con estados tiene cardinalidad `s≥1`.
- El estado actual es una instancia de **Estado** dentro del **Conjunto de Estados** del objeto.
- Los estados se especializan en **Estado Inicial**, **Estado Final** y **Estado por Defecto**, cada uno con su designación y símbolo gráfico propio (rectángulo redondeado de borde grueso, doble borde, y señalador con flecha diagonal, respectivamente).

## Modelo de constructo estructural

Un constructo estructural básico = refinable + refinador + enlace estructural. Cinco variantes:

- agregación-participación;
- exhibición-caracterización;
- generalización-especialización;
- clasificación-instanciación;
- enlace estructural etiquetado.

## Modelo de constructo procedimental

Un constructo procedimental básico = objeto + proceso + enlace procedimental.

Las semánticas básicas son:

- transformación;
- habilitación;
- transformación con control;
- habilitación con control.

Los constructos transformadores se descomponen en:

- consumo;
- efecto;
- resultado.

Los habilitadores se descomponen en:

- agente;
- instrumento.

## Modelos de descomposición y recomposición en nuevo diagrama

El anexo C modela la descomposición y la recomposición en nuevo diagrama como procesos OPM de primera clase:

- **Descomposición en nuevo diagrama**: requiere `SDn`, realiza Mostrar Contenido y luego Refinar Enlaces, y genera `SDn+1`.
- **Recomposición en nuevo diagrama**: requiere `SDn+1`, realiza Abstraer Enlaces y luego Ocultar Contenido, y genera `SDn`.
- **OPD semidescompuesto**: objeto transitorio que existe solo dentro de esas transformaciones.

Las figuras del anexo muestran la migración de enlaces desde un proceso refinado `P` hacia subprocesos `P1`, `P2`, `P3`, reubicando consumidos, agentes, instrumentos y resultantes en el nivel detallado.

## Simplificación de un OPD

Un OPD sobrecargado puede simplificarse abstrayendo un conjunto acotado de procesos y objetos hacia un constructo de nivel superior, siempre que la abstracción no cree enlaces procedimentales ilegales entre procesos pares.

## Modelo de control del desempeño de procesos (Anexo C.6)

El anexo C.6 presenta un modelo autorreferencial completo que demuestra cómo OPM controla la ejecución de procesos en tiempo de simulación.

Jerarquía principal:

- `SD`
- `SD1`
- `SD1.1`
- `SD1.1.1`
- `SD1.1.1.1`
- `SD1.2`
- `SD1.2.1`
- `SD1.2.2`
- `SD1.2.3`

**SD: Control del Desempeño de Procesos**
Un *Proceso Ejecutable* invoca *Controlar Desempeño de Proceso*, que afecta el **Conjunto de Objetos Involucrados** y genera un **Mensaje de Éxito** o un **Mensaje de Falla**.

**SD1: Descomposición principal**
*Controlar Desempeño de Proceso* se descompone en *Iniciar Proceso* y *Ejecutar Proceso*, en esa secuencia. **Estado del Proceso** recorre `inactivo → iniciado(t=0) → operando(t<n) → completando(t=n) → completado(t=n)` o `abortado`. **Poscondición** pasa de `falsa` a `verdadera`.

**SD1.1: Iniciar Proceso**
Se descompone en *Evaluar Precondición* → (`Cancelar` | `Iniciar`). Si la precondición es falsa, *Cancelar* genera **Mensaje de Cancelación** y devuelve el estado a `inactivo`. Si es verdadera, *Iniciar* consume la precondición, genera poscondición falsa y cambia el estado del proceso a `iniciado(t=0)`.

**SD1.1.1: Evaluar Precondición**
Se descompone en *Verificar Habilitadores* → *Verificar Consumidos y Afectados* → (`Refutar Precondición` | `Confirmar Precondición`). Si alguna verificación falla, se refuta la precondición; si todas pasan, se confirma.

**SD1.2: Ejecutar Proceso**
Se descompone en *Ejecución Inicial* → *Ejecución Principal* → *Ejecución Final*.

- Inicial: en paralelo, *Salir de Estado de Entrada* + *Consumir Conjunto de Consumidos*.
- Principal: ciclo de *Comparar Tiempo y Duración* → *Verificar Habilitadores y Afectados* → *Ejecutar Proceso e Incrementar Tiempo*.
- Final: en paralelo, *Generar Resultantes* + *Entrar en Estado de Salida* + *Notificar Éxito*.

Ese modelo muestra:

- descomposición multinivel;
- transiciones de estado a través de la jerarquía;
- enlaces condicionales y bypass;
- manejo de excepciones;
- subprocesos paralelos;
- cambio de rol entre instrumento y afectado según el nivel de abstracción.

---

## Dinámica y simulación

### Ejecutabilidad

Un modelo OPM puede ser ejecutable: la simulación anima el sistema ejecutando el modelo en un entorno de software.

### Modos de transformación

| Modo | Significado |
|---|---|
| Construcción | El objeto es creado o generado |
| Efecto | El objeto cambia de estado y mantiene identidad |
| Consumo | El objeto es eliminado y deja de existir |

Construcción y consumo son transformaciones más profundas que efecto porque cambian existencia, no solo estado.

### Principio de línea de tiempo

La línea temporal por defecto en una descomposición fluye de arriba hacia abajo. Subprocesos a la misma altura se ejecutan en paralelo. Un proceso de salida por excepción puede provocar salida inmediata sin importar su posición gráfica.

### Eventos temporizados

Los eventos de estado pueden representar eventos temporales. Objetos tipo reloj o temporizador del sistema con valores concretos pueden iniciar procesos en instantes definidos.

### Diagrama de vida útil

Un diagrama de vida útil muestra, para cualquier instante:

- qué objetos existen;
- en qué estado está cada uno;
- qué procesos están activos.

Es útil para seguir transiciones a lo largo de la vida del sistema.

### Propiedades de duración de proceso

| Propiedad | Descripción |
|---|---|
| Duración | tiempo real transcurrido en ejecución |
| Duración mínima | tiempo mínimo permitido |
| Duración esperada | media estadística |
| Duración máxima | tiempo máximo permitido |
| Distribución de duración | función probabilística: normal, uniforme, exponencial, etc. |

La unidad temporal del sistema es la unidad por defecto para todos los procesos, salvo que se redefina.

**Ubicación gráfica:** los valores de duración se muestran **dentro de la elipse del proceso**, bajo el nombre del proceso y la unidad temporal. La mínima a la izquierda, la esperada al centro y la máxima a la derecha.

Ejemplo:

- `Procesar [min] (30.0, 45.6, 60.0)` con distribución `normal, media=45.6, desviación=7.3`.

### Ejemplos de duración

El anexo D aporta cuatro patrones recuperables:

1. **Metamodelo de duración de proceso:** una notación compacta puede codificar duración mínima, esperada y máxima junto con parámetros de distribución; la duración real sigue siendo propiedad de ejecución.
2. **Variantes de distribución:** un mismo proceso puede parametrizarse con distribuciones exponencial, normal o uniforme.
3. **Excepción por sobretiempo:** si la duración real supera la duración máxima, ocurre el proceso de manejo de sobretiempo.
4. **Excepción por subtiempo:** si la duración real cae por debajo de la mínima, ocurre el proceso de manejo de subtiempo.

Ejemplos canónicos:

- `Procesar [min] (30.0, 45.6, 60.0)` con `uniforme, a=5.0, b=70.0`, duración real `63.3`, instancia `1`, para el caso de sobretiempo.
- El mismo intervalo de duración, con duración real `23.4` e instancia `2`, corresponde al caso de subtiempo.

---

## Guía y convenciones de nombrado

### Buenas prácticas de OPD

- no más de una página o pantalla por OPD;
- máximo 20-25 cosas por OPD;
- no debe haber oclusión entre cosas;
- número de enlaces del mismo orden que el de cosas;
- minimizar cruces;
- los enlaces no deben atravesar áreas ocupadas por cosas.

### Principio de representación de elementos

Cualquier elemento del modelo puede aparecer en cualquier número de OPDs. Solo deben incluirse los elementos necesarios para comprender el aspecto que se quiere mostrar.

### Copias múltiples de una cosa

Para evitar enlaces largos y cruces, pueden aparecer símbolos duplicados de la misma cosa en un mismo OPD. Deben usarse con moderación.

### Reglas de nombrado

| Elemento | Convención | Ejemplos |
|---|---|---|
| Objeto | Sustantivo singular, capitalizado. Para plurales: `Conjunto` en inanimados y `Grupo` en humanos | `Conjunto de Ingredientes`, `Grupo de Clientes`, `Torta de Manzana` |
| Proceso | Infinitivo o nominalización técnica clara, capitalizada. Máximo 4 palabras | `Preparar`, `Preparar Torta`, `Responder Automáticamente a Choque`, `Verificación de Identidad` |
| Estado | Minúscula, forma descriptiva o pasiva del objeto | `pintado`, `inspeccionado`, `pre-cortado` |
| Etiqueta de enlace | Frase en minúscula | `sirve a`, `se relaciona con` |

**Patrones de nombrado de procesos.** La ISO define cuatro variantes de superficie para nombres de proceso (adaptadas a español):

| Patrón | Estructura | Ejemplo en español |
|---|---|---|
| Verbo | infinitivo | `Preparar`, `Responder` |
| Sustantivo-verbo | objeto + infinitivo | `Preparar Torta`, `Responder a Choque` |
| Adjetivo-verbo | calificativo + infinitivo | `Preparar Rápidamente`, `Responder Automáticamente` |
| Adjetivo-sustantivo-verbo | calificativo + objeto + infinitivo | `Preparar Rápidamente Torta`, `Responder Automáticamente a Choque` |

El adjetivo puede calificar tanto al proceso (el gerundio subyacente) como al objeto. Se recomienda la versión sustantivo-verbo cuando hay varias opciones.

**Reglas de unicidad de nombres de objetos.** Los nombres deben ser únicos dentro del modelo. Cuando un mismo concepto aparece como refinador de distintos refinables, se resuelve la ambiguedad mediante prefijo o sufijo con el nombre del refinable. Por ejemplo, si `Tamaño` es atributo de `Conjunto de Relojes` y de `Conjunto de Sombreros`, se usa `Tamaño de Conjunto de Relojes` y `Tamaño de Conjunto de Sombreros`, o bien `Tamaño del Reloj` y `Tamaño del Sombrero`.

**Convención de capitalización:** las palabras léxicas de nombres de cosas van en mayúscula inicial; estados y etiquetas no.

**Un estado no existe sin su objeto propietario.**

**El objeto consumido desaparece al inicio del proceso**, no al final.

**Unicidad de rol procedimental con doble rol de control:** un objeto puede además actuar como disparador (`e`) y/o como condicionante (`c`) sin perder su rol principal como transformado o habilitador.

### Principio de importancia de las cosas

La importancia relativa de una cosa suele ser proporcional al OPD más alto de la jerarquía en el que aparece.

---

## Ejemplos aplicados

Ejemplos canónicos de ISO/PAS 19450 y fuentes complementarias que muestran la notación OPM en uso.

### Mecanizado de barra de acero (enlaces con estado especificado)

Objetos: **Barra de Metal** con estados `pre-cortada`, `cortada`; **Pieza** con estados `pre-probada`, `probada`. Procesos: *Cortar* (ambiental), *Mecanizar* (físico), *Probar* (ambiental). Habilitadores: **Operario de Máquina** y **Refrigerante**.

Composición OPL-ES:

- `*Cortar* cambia **Barra de Metal** de \`pre-cortada\` a \`cortada\`.`
- `*Mecanizar* consume **Barra de Metal** en \`cortada\`.`
- `*Mecanizar* genera **Pieza** en \`pre-probada\`.`
- `**Operario de Máquina** maneja *Mecanizar*.`
- `*Mecanizar* requiere **Refrigerante**.`
- `*Probar* cambia **Pieza** de \`pre-probada\` a \`probada\`.`

### Pago con cheque (descomposición con transiciones de estado)

Objeto: **Cheque** con estados `en blanco → firmado → endosado → cobrado y cancelado`. Atributo: **Custodio** con estados `pagador → beneficiario → institución financiera`. Agentes: **Pagador**, **Beneficiario**, **Banco**.

`*Pagar con Cheque*` se descompone en:

1. `*Escribir y Firmar*`
2. `*Entregar y Aceptar*`
3. `*Endosar y Presentar*`
4. `*Cobrar y Cancelar*`

Ejemplos OPL-ES:

- `*Escribir y Firmar* cambia **Cheque** de \`en blanco\` a \`firmado\`.`
- `*Entregar y Aceptar* cambia **Custodio** de \`pagador\` a \`beneficiario\`.`
- `*Endosar y Presentar* cambia **Cheque** de \`firmado\` a \`endosado\`.`
- `*Cobrar y Cancelar* cambia **Cheque** de \`endosado\` a \`cobrado y cancelado\`.`

### Lavado de platos (cambio de rol según nivel de abstracción)

SD:

- `**Usuario Doméstico** maneja *Lavar Platos*.`
- `*Lavar Platos* requiere **Lavavajillas**.`
- `*Lavar Platos* consume **Jabón**.`
- `*Lavar Platos* afecta **Conjunto de Platos**.`

`SD1`:

- `*Lavar Platos* se descompone en *Cargar Platos*, *Insertar Detergente*, *Lavar y Secar Platos* y *Descargar Platos*, en esa secuencia.`
- `*Cargar Platos* cambia **Lavavajillas** de \`vacío\` a \`cargado\`.`
- `*Descargar Platos* cambia **Lavavajillas** de \`cargado\` a \`vacío\`.`

El punto clave es que **Lavavajillas** es instrumento en el nivel abstracto, pero afectado en el nivel detallado.

### Apertura de caja fuerte (operadores lógicos)

Ejemplos:

- XOR: exactamente uno entre **Propietario A** y **Propietario B** maneja *Abrir Caja Fuerte*.
- OR: al menos uno entre **Propietario A** y **Propietario B** maneja *Abrir Caja Fuerte*.
- AND: `*Abrir Caja Fuerte* requiere **Llave A**, **Llave B** y **Llave C**.`

### Especialización de vehículos (atributo discriminante)

- `**Vehículo** exhibe **Medio de Desplazamiento**.`
- `**Medio de Desplazamiento** puede estar \`tierra\`, \`aire\` o \`superficie acuática\`.`
- `**Auto**, **Aeronave** y **Barco** son **Vehículo**.`
- `**Auto** exhibe **Medio de Desplazamiento** en \`tierra\`.`
- `**Aeronave** exhibe **Medio de Desplazamiento** en \`aire\`.`
- `**Barco** exhibe **Medio de Desplazamiento** en \`superficie acuática\`.`

### Seguridad del hogar (proceso asincrónico)

`*Mantener Seguridad del Hogar*` consta de:

- *Atender Robo*;
- *Proteger contra Incendio*;
- *Alertar Terremoto*.

Como no se conoce el orden temporal, se usa despliegue por agregación-participación y no descomposición temporal.

### Preparación de café (estructura-comportamiento-función)

Estructura:

- `**Máquina de Café** consta de **Depósito de Agua**, **Espumador de Leche**, **Calentador de Agua**, **Compartimento de Cápsulas** y **Portataza**.`

Comportamiento:

- `*Preparar Café*` se descompone en *Calentar Agua*, *Espumar Leche*, *Preparar Café* y *Agregar Leche*.

Función:

- el beneficiario es **Persona que Bebe Café**;
- la función cambia **Satisfacción** de `insatisfecha` a `satisfecha`.

### Operación de auto eléctrico (componentes del SD)

Ejemplo de SD:

- propósito: mejorar **Éxito del Negocio** de **Grupo de Interesados de la Empresa**;
- función: `*Operar Auto Eléctrico*` cambia **Auto Eléctrico** de `detenido` a `en movimiento`;
- agente: **Conductor**;
- instrumento: **Sistema Operativo del Auto Eléctrico**;
- entorno: **Tipo de Terreno**, **Regulaciones**.

### Ejemplos sociales y sociotécnicos auxiliares

- **Control de Tráfico Aéreo:** **Piloto** y **Controlador Aéreo** son agentes; **Torre de Control** es instrumento.
- **Aprendizaje MOOC:** **Grupo de Estudiantes** actúa como agente; la plataforma MOOC como instrumento.
- **Gestión de Identidad Profesional en Línea:** el perfil en línea representa a la persona mediante enlace estructural etiquetado.
- **Transporte de Equipaje:** la función principal cambia la ubicación del equipaje del aeropuerto de origen al de destino.
- **Sistema de Conferencia:** **Organizador** y **Acomodadores** son agentes; instalaciones y equipamiento son instrumentos; el clima puede ser ambiental.

Para procedimientos específicos de OPCloud, flujos de interfaz y detalles de la herramienta, véase `urn:fxsl:kb:opcloud-tutorial-videos`.

---

## Notas para implementadores de herramientas

Las siguientes notas informativas del estándar están dirigidas a quienes desarrollan herramientas compatibles con OPM:

- Una herramienta puede rastrear el conjunto de refinadores de cada refinable y ajustar automáticamente el símbolo gráfico y las oraciones OPL correspondientes cuando quien modela cambia la colección de refinadores.
- Una herramienta puede ofrecer la opción de especificar la esencia primaria del sistema como medio para establecer el valor por defecto del atributo genérico de esencia.
- Una herramienta puede notificar a quien modela cuando se intenta incluir un objeto como refinador en más de un contexto, para que determine la pertinencia de la inclusión.
- Una herramienta puede establecer una sintaxis por defecto para resolver nombres de refinadores ambiguos.
- El OPL correspondiente a un OPD debe expresar solo los estados de los objetos tal como aparecen en ese OPD; la unión de estados de un objeto a través de todos los OPDs constituye el conjunto completo de estados de ese objeto.
- Cuando un enlace de evento desde un objeto o estado sistémico cruza el límite de un proceso descompuesto para iniciar un subproceso, la herramienta debería advertir que esto puede interferir con el orden temporal prescrito de la descomposición síncrona. Si el evento proviene de un objeto ambiental, la herramienta debería guiar a quien modela para definir cómo manejar la contingencia.
- Las herramientas de modelado OPM necesitan rastrear el número e identidades de las instancias operacionales de cada objeto y de cada proceso para poder realizar simulaciones.
