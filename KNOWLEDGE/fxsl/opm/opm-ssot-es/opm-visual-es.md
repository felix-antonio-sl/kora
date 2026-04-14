---
_manifest:
  urn: "urn:fxsl:kb:opm-visual-es"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-04-14"
    source: "urn:fxsl:kb:opm-iso-19450-es (consolidado v1.4.0-es)"
version: "1.1.0"
status: published
tags: [opm, iso-19450, especificacion-visual, gramatica-grafica, opd]
lang: es
extensions:
  kora:
    family: specification
    depends_on:
      - "urn:fxsl:kb:opm-iso-19450-es"
---

# Especificación formal de la gramática visual OPM

Reglas completas para construir y evaluar cualquier OPD (Object-Process Diagram) conforme a ISO/PAS 19450. Este documento opera a nivel de **tipo**, no de instancia: define las primitivas, composiciones válidas, restricciones y reglas de precedencia que gobiernan la capa gráfica de OPM.

Fuente normativa: `opm-iso-19450-consolidado.md` (v1.4.0-es).

---

## 1. Primitivas gráficas

La capa visual de OPM se construye con un vocabulario cerrado de formas, contornos, sombreados, decoraciones de extremo y marcas textuales. Ningún elemento fuera de este vocabulario es válido en un OPD conforme.

### 1.1 Formas cerradas (cosas)

| Forma | Entidad que representa |
|---|---|
| Rectángulo | Objeto |
| Elipse | Proceso |
| Rectángulo redondeado (routableangle) | Estado (siempre contenido dentro de un objeto) |

### 1.1b Esquema de colores canónico (informativo)

Los colores no son normativos en ISO/PAS 19450 (la semántica se codifica por forma, contorno y sombreado), pero el esquema de referencia del estándar es:

| Elemento | Color de borde | Color de fondo |
|---|---|---|
| Objeto | Verde | Transparente (informacional) o blanco |
| Proceso | Azul oscuro | Transparente (informacional) o blanco |
| Estado | Verde oliva | Gris claro |
| Enlace estructural | Negro | — |
| Enlace procedimental | Negro | — |

**Regla V-63**: Los colores son informativos, no normativos. Una implementación conforme puede usar un esquema de colores diferente siempre que la distinción entre forma, contorno y sombreado sea legible. El esquema verde/azul es el de referencia.

### 1.2 Atributos de contorno

| Contorno | Codifica |
|---|---|
| Continuo (sólido) | Afiliación sistémica — la cosa pertenece al sistema |
| Discontinuo (punteado) | Afiliación ambiental — la cosa pertenece al entorno |

### 1.3 Atributos de profundidad (sombreado)

| Profundidad | Codifica |
|---|---|
| Sombreado (sombra gris desplazada abajo-derecha) | Esencia física |
| Plano (sin sombra) | Esencia informacional (valor por defecto) |

### 1.4 Producto cartesiano: las ocho representaciones de cosa

Toda cosa OPM se renderiza como Forma x Contorno x Profundidad:

| # | Forma | Contorno | Profundidad | Cosa resultante |
|---|---|---|---|---|
| 1 | Rectángulo | sólido | sombreado | Objeto físico sistémico |
| 2 | Rectángulo | sólido | plano | Objeto informacional sistémico |
| 3 | Rectángulo | discontinuo | sombreado | Objeto físico ambiental |
| 4 | Rectángulo | discontinuo | plano | Objeto informacional ambiental |
| 5 | Elipse | sólido | sombreado | Proceso físico sistémico |
| 6 | Elipse | sólido | plano | Proceso informacional sistémico |
| 7 | Elipse | discontinuo | sombreado | Proceso físico ambiental |
| 8 | Elipse | discontinuo | plano | Proceso informacional ambiental |

**Regla V-1**: Los valores por defecto son informacional (sin sombra) y sistémico (borde continuo). Si no se especifica, toda cosa es informacional y sistémica.

**Regla V-2**: La perseverancia no es visual — se infiere del tipo: los objetos son persistentes, los procesos son transitorios.

### 1.5 Decoraciones de extremo de enlace

| Decoración | Nombre | Uso |
|---|---|---|
| Punta de flecha cerrada | arrowhead | Enlaces transformadores (consumo, resultado, efecto) |
| Círculo negro relleno | black lollipop | Enlace de agente (extremo proceso) |
| Círculo blanco vacío | white lollipop | Enlace de instrumento (extremo proceso) |
| Corchete cuadrado abierto | open bracket | Extremo origen de enlaces procedimentales (agente, instrumento, consumo) |
| Línea en zigzag con punta | lightning bolt | Enlace de invocación |
| Punta de flecha abierta | open arrowhead | Enlaces estructurales etiquetados unidireccionales |
| Arpón (media punta) | harpoon | Enlaces estructurales etiquetados bidireccionales |

### 1.6 Marcas textuales sobre enlaces

| Marca | Significado |
|---|---|
| `e` | Modificador de evento — el objeto inicia el proceso |
| `c` | Modificador de condición — el proceso se omite si la precondición falla |
| `/` | Excepción por sobretiempo (overtime) |
| `//` | Excepción por subtiempo (undertime) |
| `Pr=p` | Probabilidad del enlace dentro de un abanico probabilístico |
| Texto itálico sobre el eje | Etiqueta (tag) de enlace estructural |
| Texto sobre enlace procedimental | Etiqueta de ruta (path label) |

### 1.7 Símbolos triangulares (relaciones estructurales fundamentales)

| Símbolo | Relación |
|---|---|
| Triángulo negro sólido (relleno completo) | Agregación-participación |
| Triángulo vacío con triángulo negro interior | Exhibición-caracterización |
| Triángulo vacío (sin contenido) | Generalización-especialización |
| Triángulo vacío con círculo negro interior | Clasificación-instanciación |

**Regla V-3**: El vértice del triángulo siempre apunta hacia el refinable (todo, exhibidor, general, clase). La base conecta con los refinadores (partes, rasgos, especializaciones, instancias).

### 1.8 Indicadores auxiliares

| Indicador | Representación | Significado |
|---|---|---|
| Colección incompleta | Barra horizontal corta bajo el triángulo | Existen refinadores no mostrados |
| Cosa duplicada | Silueta desplazada detrás del símbolo | Copia visual de la misma cosa en el mismo OPD |
| Supresión de estados | Rectángulo redondeado con `...` en esquina inferior derecha del objeto | El objeto tiene más estados que los mostrados |
| Multiplicidad | Número o expresión junto al extremo del enlace | Cardinalidad de la relación |

### 1.9 Estructura atómica del OPD

**Regla V-60**: Todo OPD se compone de OPD Constructs. Un OPD Construct consiste de un Thing Set (2 o más cosas) y un Link Set (1 o más enlaces). El átomo mínimo es el Basic Construct: exactamente 1 enlace conectando exactamente 2 cosas. Un Basic Structural Construct conecta 2 objetos mediante 1 enlace estructural. Un Basic Procedural Construct conecta 1 proceso y 1 objeto mediante 1 enlace procedimental.

### 1.10 Anatomía formal de un enlace

**Regla V-61**: Todo enlace consiste de tres componentes: Source (cosa o estado de origen), Destination (cosa o estado de destino), y Connector. El Connector se compone de: Line (la línea visible), Symbol (decoración de extremo: arrowhead, lollipop, etc.), y opcionalmente Tag (etiqueta textual) y Path Label (etiqueta de ruta). Source y Destination son Linked Things; cada uno exhibe Symbol (decoración visual) y Multiplicity (cardinalidad).

---

## 2. Estados de objeto

### 2.1 Representación

Los estados se representan como rectángulos redondeados (routableangles) contenidos dentro del rectángulo del objeto propietario, dispuestos horizontalmente en la zona inferior.

**Regla V-4**: Un estado no existe fuera de su objeto propietario. No hay estados flotantes.

**Regla V-5**: Un objeto sin estados no puede ser afectado; solo puede ser creado (resultado) o destruido (consumo).

### 2.2 Marcadores de designación de estado

| Designación | Marca gráfica | Significado |
|---|---|---|
| Inicial | Borde grueso simple (bold-contour) | Estado en la creación del objeto |
| Final | Doble borde concéntrico (double-contour) | Estado en el momento de ser consumido |
| Por defecto | Flecha diagonal abierta apuntando al estado | Estado más probable al inspeccionar aleatoriamente |
| Normal | Borde estándar | Estado sin designación especial |

**Regla V-6**: Un objeto puede tener cero o más estados iniciales, cero o más estados finales, y como máximo un estado por defecto.

### 2.3 Valores de atributo como estados

Los valores de un atributo son estados del objeto-atributo. Pueden expresarse como:
- Valores discretos: `sólido`, `líquido`, `gas`.
- Rangos numéricos: `120..240`.
- Valor concreto (en instancias): `185`.

---

## 3. Taxonomía completa de enlaces procedimentales

### 3.1 Enlaces transformadores

| Enlace | Dirección gráfica | Decoración fuente | Decoración destino | Semántica |
|---|---|---|---|---|
| Consumo | objeto → proceso | (ninguna) | punta cerrada | El proceso destruye el objeto |
| Resultado | proceso → objeto | (ninguna) | punta cerrada | El proceso crea el objeto |
| Efecto | objeto ↔ proceso | punta cerrada | punta cerrada | El proceso cambia el estado del objeto |

**Regla V-7**: Un enlace de efecto requiere que el objeto tenga al menos un estado definido.

**Regla V-8**: Un enlace de resultado hacia un objeto con estado inicial debe conectar al rectángulo del objeto, nunca directamente al estado inicial.

### 3.2 Enlaces transformadores con estado especificado

Cuando un enlace parte de o llega a un estado específico dentro del objeto:

| Variante | Geometría |
|---|---|
| Consumo con estado | Flecha desde el estado específico del objeto hacia el proceso |
| Resultado con estado | Flecha desde el proceso hacia el estado específico del objeto |
| Efecto entrada-salida | Flecha de entrada desde el estado-origen hacia el proceso + flecha de salida desde el proceso hacia el estado-destino |
| Efecto solo entrada | Flecha desde el estado-origen hacia el proceso (sin flecha de salida especificada) |
| Efecto solo salida | Flecha desde el proceso hacia el estado-destino (sin flecha de entrada especificada) |

**Regla V-9**: En un efecto solo-entrada sin estado de salida especificado, el destino es el estado por defecto del objeto, o la distribución de probabilidad de estados si no hay defecto.

### 3.3 Enlaces habilitadores

| Enlace | Dirección gráfica | Decoración proceso | Semántica |
|---|---|---|---|
| Agente | agente → proceso | Círculo negro relleno (black lollipop) | Persona que habilita sin ser transformada |
| Instrumento | instrumento → proceso | Círculo blanco vacío (white lollipop) | Objeto inanimado que habilita sin ser transformado |

**Regla V-10**: Si un habilitador deja de existir durante la ejecución, el proceso se detiene y el estado del afectado queda indeterminado.

### 3.4 Enlaces habilitadores con estado especificado

El enlace parte del estado específico del agente/instrumento hacia el proceso. El habilitador solo habilita si está en ese estado.

### 3.5 Principio de unicidad del enlace procedimental

**Regla V-11**: Un objeto o estado tiene exactamente un rol respecto de un proceso enlazado: es transformado O habilitador, nunca ambos simultáneamente para el mismo enlace.

---

## 4. Modificadores de control

### 4.1 Evento (`e`)

El modificador `e` se coloca sobre cualquier enlace transformador o habilitador, cerca del extremo del proceso. Semántica: el objeto (o su estado) **inicia** la evaluación de la precondición del proceso.

| Enlace base | + evento = | Geometría adicional |
|---|---|---|
| Consumo | Evento de consumo | Marca `e` sobre el enlace, cerca del proceso |
| Efecto | Evento de efecto | Marca `e` sobre el enlace bidireccional, cerca del proceso |
| Agente | Evento de agente | Marca `e` sobre el enlace con lollipop negro |
| Instrumento | Evento de instrumento | Marca `e` sobre el enlace con lollipop blanco |

**Regla V-12**: El enlace de evento es el segmento desde el objeto/estado hacia el proceso. El segmento desde el proceso hacia el objeto (consumo, efecto) NO es un enlace de evento.

**Regla V-13**: Un evento se pierde tras la evaluación, incluso si la precondición falla.

### 4.2 Condición (`c`)

El modificador `c` introduce un mecanismo de bypass: si la precondición falla, el proceso se omite y el control pasa al siguiente.

| Enlace base | + condición = | Geometría adicional |
|---|---|---|
| Consumo | Consumo condicional | Marca `c` sobre el enlace |
| Efecto | Efecto condicional | Marca `c` sobre el enlace bidireccional |
| Agente | Agente condicional | Marca `c` sobre el enlace con lollipop negro |
| Instrumento | Instrumento condicional | Marca `c` sobre el enlace con lollipop blanco |

### 4.3 Composición: estado especificado + modificador de control

Los modificadores `e` y `c` se combinan con estado especificado. La geometría resultante: el enlace parte del estado concreto del objeto y lleva la marca `e` o `c` sobre la línea.

### 4.4 Excepción temporal

| Enlace | Marca | Dispara cuando |
|---|---|---|
| Excepción por sobretiempo | `/` (una barra oblicua) | Duración real > duración máxima |
| Excepción por subtiempo | `//` (dos barras oblicuas) | Duración real < duración mínima |

Estos enlaces conectan un proceso fuente con un proceso de manejo de excepción. El proceso de manejo es ambiental (borde discontinuo).

---

## 5. Operadores lógicos

### 5.1 AND (conjunción)

**Representación**: Enlaces separados del mismo tipo que no se tocan entre sí. No hay símbolo explícito de AND.

**Regla V-14**: AND es el operador por defecto. Múltiples enlaces del mismo tipo sin arco conector implican AND.

### 5.2 XOR (disyunción exclusiva)

**Representación**: Un arco discontinuo simple sobre el abanico de enlaces, con foco en el extremo convergente.

**Semántica**: Exactamente uno de los enlaces participantes se activa.

### 5.3 OR (disyunción inclusiva)

**Representación**: Dos arcos discontinuos concéntricos sobre el abanico de enlaces.

**Semántica**: Al menos uno de los enlaces participantes se activa.

### 5.4 Reglas de aplicación

**Regla V-15**: XOR y OR aplican a todas las familias de enlaces procedimentales: consumo, resultado, efecto, agente, instrumento e invocación.

**Regla V-16**: El arco se posiciona en el extremo convergente del abanico (el extremo compartido por todos los enlaces).

**Regla V-17**: Un abanico puede ser convergente (múltiples fuentes → un destino) o divergente (una fuente → múltiples destinos).

### 5.5 Combinatoria completa de abanicos

| Familia de enlace | Convergente | Divergente |
|---|---|---|
| Consumo | N objetos → 1 proceso | 1 objeto → N procesos |
| Resultado | N procesos → 1 objeto | 1 proceso → N objetos |
| Efecto | N objetos ↔ 1 proceso | N procesos ↔ 1 objeto |
| Agente | (no aplica) | 1 agente → N procesos |
| Instrumento | (no aplica) | 1 instrumento → N procesos |
| Invocación | N procesos → 1 proceso | 1 proceso → N procesos |

### 5.6 Abanicos con modificadores de control

Cada abanico XOR/OR admite variantes con `e` (evento) y `c` (condición). La marca se coloca sobre cada enlace individual del abanico. La contraparte OR de cualquier XOR se obtiene reemplazando el arco simple por arco doble y la semántica de "exactamente" por "al menos".

### 5.7 Abanicos con estado especificado

Los enlaces del abanico pueden partir de o llegar a estados específicos de los objetos. Cada enlace individual del abanico puede tener o no estado especificado independientemente.

### 5.8 Abanicos probabilísticos

Cada enlace del abanico se anota con `Pr=p`. Las probabilidades de todos los enlaces del abanico deben sumar 1.0. Si no se anotan probabilidades, la probabilidad por defecto es `1/n` donde n es el número de enlaces.

**Regla V-18**: Un abanico probabilístico es siempre XOR — exactamente un enlace se activa por ejecución.

### 5.9 Equivalencia resultado-XOR

**Regla V-19**: Un enlace de resultado simple hacia un objeto con estados es semánticamente equivalente a un abanico XOR de enlaces de resultado con estado especificado, uno por cada estado posible del objeto.

---

## 6. Trayectorias de ejecución y etiquetas de ruta

### 6.1 Definición

Una etiqueta de ruta (path label) es texto colocado sobre un enlace procedimental. Resuelve la ambigüedad cuando un proceso tiene múltiples combinaciones posibles de entrada/salida.

### 6.2 Regla de coincidencia

**Regla V-20**: Al ejecutarse un proceso, se sigue la trayectoria cuya etiqueta de ruta de entrada coincide con la etiqueta de ruta de salida. Todos los enlaces de consumo/resultado con la misma etiqueta forman una trayectoria.

### 6.3 Escenarios

Un escenario es un conjunto de etiquetas de ruta que define una variante concreta de ejecución. Evita crear un OPD adicional por cada variante.

---

## 7. Multiplicidad y cardinalidad

### 7.1 Símbolos de opcionalidad

| Símbolo | Límites | Significado |
|---|---|---|
| `?` | 0..1 | Opcional (cero o una instancia) |
| `*` | 0..* | Opcional, cero a muchos |
| (sin símbolo) | 1..1 | Exactamente uno (por defecto) |
| `+` | 1..* | Al menos uno |

### 7.2 Rangos y expresiones

La multiplicidad soporta:
- Rangos: `3..5`, `8..10`.
- Rangos múltiples separados por coma: `3..5, 8..10`.
- Expresiones aritméticas: `2`, `3*n`.
- Restricciones: `n<=4`, `e >= 1`, `b in {0, 1}`.
- Operadores de restricción: `=`, `!=`, `<`, `<=`, `>=`, `in {conjunto}`.

**Regla V-21**: Los nombres de parámetros de multiplicidad deben ser únicos en todo el modelo.

**Regla V-22**: La multiplicidad se coloca como anotación junto al extremo del enlace o cerca del refinador en relaciones estructurales.

### 7.3 Restricciones de aplicación

**Regla V-23**: La multiplicidad aplica a enlaces etiquetados, agregación-participación y enlaces procedimentales. No aplica a procesos directamente.

---

## 8. Enlaces estructurales

### 8.1 Enlaces etiquetados

| Variante | Geometría | Decoración |
|---|---|---|
| Unidireccional | Línea con punta abierta en destino | Etiqueta itálica sobre la línea |
| Unidireccional sin etiqueta | Línea con punta abierta | Sin etiqueta (semántica: "se relaciona con") |
| Bidireccional | Línea con arpones en ambos extremos | Dos etiquetas (ida y vuelta) |
| Recíproco | Línea con arpones | Una sola etiqueta o sin etiqueta |

**Regla V-56**: Un enlace bidireccional cuyos dos tags son idénticos es semánticamente equivalente a un enlace recíproco con ese mismo tag. Ambas representaciones son intercambiables.

### 8.2 Relaciones estructurales fundamentales

| Relación | Símbolo | Dirección vértice→base | Refinable | Refinadores |
|---|---|---|---|---|
| Agregación-participación | Triángulo negro sólido | Todo → Partes | Whole | Parts |
| Exhibición-caracterización | Triángulo vacío + triángulo negro interior | Exhibidor → Rasgos | Exhibitor | Features |
| Generalización-especialización | Triángulo vacío | General → Especializaciones | General | Specializations |
| Clasificación-instanciación | Triángulo vacío + círculo negro interior | Clase → Instancias | Class | Instances |

### 8.3 Reglas de las relaciones fundamentales

**Regla V-24**: Salvo en exhibición-caracterización, el refinable y los refinadores deben tener la misma perseverancia (ambos objetos o ambos procesos).

**Regla V-25**: Exhibición-caracterización es la única relación estructural que puede conectar objetos con procesos. El rasgo es atributo si es objeto y operación si es proceso.

**Regla V-26**: Las cuatro combinaciones exhibidor-rasgo son válidas: objeto exhibe atributo, objeto exhibe operación, proceso exhibe atributo, proceso exhibe operación.

**Regla V-27**: Clasificación-instanciación no distingue entre colección completa e incompleta (el número de instancias varía en operación).

**Regla V-57**: Las partes de una agregación pueden ser consumidas, afectadas o producidas de forma independiente sin que el todo sea consumido, afectado o producido. Los enlaces transformadores pueden conectar subprocesos con partes individuales del todo.

### 8.4 Herencia

Las especializaciones heredan del general: todas las partes, todos los rasgos, todos los enlaces estructurales etiquetados, todos los enlaces procedimentales.

**Regla V-28**: Se permite herencia múltiple.

**Regla V-29**: Un atributo discriminante restringe los valores válidos de un atributo para cada especialización. Cada especialización exhibe exactamente un valor del atributo discriminante.

**Regla V-58**: En clasificación-instanciación, la clase muestra atributos con rangos de valores (estados de rango como `120..240`); la instancia muestra los mismos atributos con valores concretos (estados de valor como `185`). La instancia se nombra con el formato `NombreInstancia : NombreClase`.

### 8.5 Enlaces estructurales con estado especificado

Tres familias por posición de la especificación de estado:

| Posición | Geometría |
|---|---|
| Estado en origen | El enlace parte de un estado específico del objeto origen |
| Estado en destino | El enlace llega a un estado específico del objeto destino |
| Estado en origen y destino | Ambos extremos conectan a estados específicos |

**Regla V-30**: Las variantes bidireccional y recíproco NO existen para el caso de estado solo en destino.

---

## 9. Enlaces de invocación

### 9.1 Tipos

| Enlace | Geometría | Semántica |
|---|---|---|
| Invocación | Línea en zigzag (rayo) con punta, proceso → proceso | Al terminar, el proceso invocante inicia el invocado |
| Auto-invocación | Zigzag que sale y regresa al mismo proceso (bucle) | El proceso se invoca a sí mismo al terminar |

### 9.2 Invocación implícita

Dentro de un proceso descompuesto, la invocación se determina por posición vertical:

**Regla V-31**: La terminación de un subproceso invoca al subproceso inmediatamente inferior (cuyo punto superior de elipse está debajo). No hay enlace explícito.

**Regla V-32**: Subprocesos cuyos puntos superiores de elipse están a la misma altura se ejecutan en paralelo. El último en terminar inicia al siguiente nivel.

### 9.3 Activación asincrónica por eventos

**Regla V-59**: Cuando subprocesos dentro de una descomposición son activados individualmente por enlaces de evento desde estados distintos de un objeto, se ejecutan de forma asincrónica e independiente. No hay orden secuencial ni paralelo entre ellos: cada subproceso se activa exclusivamente cuando ocurre su evento correspondiente. Este patrón modela sistemas reactivos donde los subprocesos compiten por activación según el estado del entorno.

---

## 10. Gestión de contexto y refinamiento

### 10.1 Mecanismos de refinamiento y abstracción

| Par | Refinamiento | Abstracción |
|---|---|---|
| Estados | Expresión de estados | Supresión de estados |
| Estructura | Despliegue (unfolding) | Plegado (folding) |
| Comportamiento | Descomposición | Recomposición |

### 10.2 Despliegue en el mismo diagrama

El refinable y los refinadores comparten OPD, unidos por enlaces estructurales fundamentales.

### 10.3 Despliegue en nuevo diagrama (in-zooming)

**Regla V-33**: El refinable aparece con contorno grueso tanto en el OPD padre como en el OPD hijo.

**Regla V-62**: El in-zooming se ejecuta en dos fases: (1) Content Showing — muestra el contenido interno del refinable, produciendo un Semi-Zoomed OPD; (2) Link Refining — refina los enlaces del OPD padre distribuyéndolos a los subprocesos, produciendo el OPD hijo (SDn+1). El out-zooming es el inverso: (1) Link Abstracting — abstrae los enlaces de los subprocesos; (2) Content Hiding — oculta el contenido interno, restaurando el OPD padre (SDn).

### 10.4 Descomposición de proceso

**Regla V-34**: La elipse del proceso refinable se agranda para contener los subprocesos como elipses menores.

**Regla V-35**: La línea temporal fluye de arriba hacia abajo. La posición vertical determina la secuencia de ejecución.

### 10.5 Descomposición de objeto

El rectángulo del objeto refinable se agranda para mostrar objetos constituyentes.

### 10.6 Supresión de estados

Para simplificar un OPD, se pueden ocultar estados no relevantes. Se indica con el símbolo de supresión (`...` en un rectángulo redondeado en la esquina inferior derecha del objeto).

### 10.7 Simplificación de OPD

Un subconjunto de subprocesos puede reagruparse en un nuevo proceso compacto mediante out-zooming, generando un OPD simplificado con menos niveles.

---

## 11. Distribución de enlaces

### 11.1 Regla general

**Regla V-36**: Los enlaces conectados al contorno exterior de un proceso descompuesto se distribuyen a todos los subprocesos. Los enlaces de agente e instrumento conectados al proceso padre aplican a todos los subprocesos.

### 11.2 Restricciones de distribución

**Regla V-37**: Los enlaces de consumo y resultado NO deben conectarse al contorno exterior de un proceso descompuesto. Deben conectarse directamente al subproceso específico que consume o produce.

**Regla V-38**: Los enlaces de evento desde objetos sistémicos no deben cruzar el límite de la descomposición para iniciar subprocesos.

**Regla V-39**: Si un enlace de condición causa que un subproceso se omita, el control pasa al siguiente subproceso en la secuencia.

---

## 12. Enlaces transformadores escindidos

### 12.1 Problema

Cuando un enlace de efecto entrada-salida (`P cambia A de s1 a s2`) se descompone en subprocesos, queda subespecificado: no se sabe qué subproceso saca al objeto del estado de entrada ni cuál lo coloca en el de salida.

### 12.2 Solución: par escindido

**Regla V-40**: El enlace se escinde en dos:
- El subproceso **temprano** recibe la flecha de entrada (saca al objeto de s1).
- El subproceso **tardío** recibe la flecha de salida (coloca al objeto en s2).

**Regla V-41**: No existen versiones con modificador de control de los enlaces escindidos.

### 12.3 Cambio de rol con la abstracción

**Regla V-42**: Un objeto puede ser instrumento en un nivel abstracto y afectado en un nivel detallado. Esto es válido si a nivel abstracto los estados inicial y final del objeto coinciden.

---

## 13. Precedencia de enlaces durante la recomposición

### 13.1 Matriz de precedencia transformadora

Al recomponer subprocesos en un proceso padre, si dos subprocesos tienen enlaces distintos hacia el mismo objeto, la fuerza semántica determina cuál prevalece:

| B↔P1 \ B↔P2 | Efecto | Resultado | Consumo |
|---|---|---|---|
| **Efecto** | Efecto | Resultado | Consumo |
| **Resultado** | Resultado | **Inválido** | Efecto |
| **Consumo** | Consumo | Efecto | **Inválido** |

**Regla V-43**: Resultado + consumo sobre el mismo objeto es inválido (no se puede crear y destruir como el mismo hecho abstracto). Resultado + resultado y consumo + consumo también son inválidos.

### 13.2 Precedencia entre transformadores y habilitadores

**Regla V-44**: Un enlace transformador siempre prevalece sobre un enlace habilitador al recomponer.

### 13.3 Orden principal de precedencia

```
consumo = resultado > efecto > agente > instrumento
```

### 13.4 Precedencia secundaria por modificador de control

Dentro de cada clase de enlace:

```
evento > sin control > condición
```

### 13.5 Orden completo de fuerza semántica (12 niveles)

| Nivel | Enlace |
|---|---|
| 1 | Evento de consumo |
| 2 | Consumo (= Resultado) |
| 3 | Resultado (= Consumo) |
| 4 | Condición de consumo |
| 5 | Evento de efecto |
| 6 | Efecto |
| 7 | Condición de efecto |
| 8 | Evento de agente |
| 9 | Agente |
| 10 | Condición de agente |
| 11 | Evento de instrumento |
| 12 | Instrumento |

La condición debilita; el evento fortalece.

---

## 14. Propiedades de duración de proceso

### 14.1 Propiedades

| Propiedad | Descripción |
|---|---|
| Duración | Tiempo real transcurrido en ejecución |
| Duración mínima | Tiempo mínimo permitido |
| Duración esperada | Media estadística |
| Duración máxima | Tiempo máximo permitido |
| Distribución de duración | Función probabilística: normal, uniforme, exponencial, etc. |

### 14.2 Representación gráfica

**Regla V-45**: Los valores de duración se muestran dentro de la elipse del proceso, bajo el nombre y la unidad temporal. Formato: `[unidad] {min, esperada, max} {distribución, parámetros}`.

### 14.3 Unidades temporales válidas

`ms`, `sec`, `min`, `hour`, `day`, `week`, `month`, `year`.

---

## 15. Etiquetas OPD y navegación

### 15.1 Etiquetado del árbol de procesos

**Regla V-46**: El SD (System Diagram) contiene exactamente un proceso sistémico. Puede contener procesos ambientales.

Convención de etiquetas: `SD` → `SD1` → `SD1.1` → `SD1.1.1`, etc.

### 15.2 Árbol de procesos OPD

Raíz en `SD`. Cada nodo corresponde a un OPD creado por descomposición de un proceso. Es el mecanismo principal de navegación del modelo.

### 15.3 Árbol de objetos OPD

Raíz en un objeto. Muestra su elaboración por refinamiento (exhibición, agregación, etc.).

---

## 16. Convenciones de nombrado y buenas prácticas

### 16.1 Reglas de nombrado

| Elemento | Convención |
|---|---|
| Objeto | Sustantivo singular, palabras con mayúscula inicial. Plurales: `Conjunto` (inanimados), `Grupo` (humanos) |
| Proceso | Infinitivo o nominalización técnica, capitalizado. Máximo 4 palabras |
| Estado | Minúscula, forma descriptiva o participio pasivo |
| Etiqueta de enlace | Frase en minúscula |

**Regla V-47**: Los nombres de objetos deben ser únicos en todo el modelo. Cuando hay ambigüedad, se añade el nombre del refinable como sufijo.

**Regla V-48**: Un estado no existe sin su objeto propietario.

**Regla V-49**: El objeto consumido desaparece al inicio del proceso, no al final.

### 16.2 Límites de complejidad por OPD

**Regla V-50**: No más de una página/pantalla por OPD. Máximo 20-25 cosas por OPD.

**Regla V-51**: No debe haber oclusión entre cosas. Los enlaces no deben atravesar áreas ocupadas por cosas. Minimizar cruces.

### 16.3 Principio de representación

**Regla V-52**: Cualquier elemento del modelo puede aparecer en cualquier número de OPDs. Solo deben incluirse los elementos necesarios para el aspecto que se muestra.

---

## 17. Ejecución y simulación

### 17.1 Visualización de ejecución

**Regla V-53**: Durante la simulación, un proceso en ejecución se muestra con su elipse rellena en color sólido (sombreada completamente).

**Regla V-54**: El estado actual de un objeto se muestra resaltado (borde más grueso o color diferencial) respecto a los estados inactivos.

### 17.2 Principio de línea de tiempo

**Regla V-55**: El tiempo fluye de arriba hacia abajo dentro de la descomposición de un proceso. Las posiciones verticales de los subprocesos determinan el orden temporal.

---

## 18. Estructura del metamodelo OPM (Anexo C)

Esta sección formaliza la estructura reflexiva del metamodelo OPM tal como aparece en el Anexo C normativo de ISO/PAS 19450. Define cómo se compone un modelo OPM, la dualidad gráfico-textual, y los conceptos de objeto específico de estado.

### 18.1 Composición del modelo OPM

**Regla V-64**: Un OPM Model especifica un System. Se compone de un OPD Set y un OPL Spec. El OPD Set contiene uno o más OPDs (multiplicidad 1..*). El OPL Spec contiene uno o más OPL Paragraphs (multiplicidad 1..*). OPD Set y OPL Spec son duales: el OPD Set especifica gráficamente lo que el OPL Spec especifica textualmente, y viceversa.

### 18.2 Dualidad OPD–OPL

**Regla V-65**: Cada OPD tiene su contraparte en un OPL Paragraph. Cada OPD Construct tiene su contraparte en una o más OPL Sentences. La dualidad es bidireccional: toda afirmación en un OPD debe ser reproducible como OPL, y toda oración OPL debe ser representable como OPD Construct.

### 18.3 Construcción del OPD Construct

**Regla V-66**: La construcción de un OPD Construct es el proceso Connecting, que toma un Thing Set en estado `disconnected` y un Link Set como instrumento, y produce un Thing Set en estado `connected`. La cardinalidad del Link Set puede ser `1` (Basic Construct) o `≥ 2` (Compound Construct). La cardinalidad del Thing Set puede ser `2` (Basic) o `≥ 3` (Compound).

### 18.4 Objetos con y sin estados

**Regla V-67**: Todo objeto exhibe un State Set. Si el tamaño del State Set es `s = 0`, el objeto es Stateless (sin estados). Si `s ≥ 1`, el objeto es Stateful (con estados). Un Stateful Object con `s` estados deriva un State-Specific Object Set que contiene exactamente `s` State-Specific Objects. Cada State-Specific Object refiere a exactamente un estado del objeto original.

### 18.5 Naming de instancias State-Specific

**Regla V-68**: Un State-Specific Object se nombra concatenando el nombre del estado con el nombre del objeto original (e.g., `Designed Product` para el estado `designed` de `Product`). Este patrón permite referenciar un objeto restringido a un estado particular como entidad independiente en OPL y en enlaces procedimentales.

### 18.6 Nota sobre Tabla 26 de ISO/PAS 19450

> La Tabla 26 del estándar original no fue capturada en la extracción de imágenes disponible. Dada su posición entre la Tabla 25 (enlaces escindidos) y la Tabla 27 (precedencia de transformadores), probablemente contenía un resumen de precedencia transformador-habilitador, cuyo contenido ya está formalizado en las reglas V-43 y V-44 de la sección 13.

---

## Índice de reglas

| Regla | Resumen |
|---|---|
| V-1 | Valores por defecto: informacional y sistémico |
| V-2 | Perseverancia no es visual, se infiere del tipo |
| V-3 | Vértice del triángulo apunta al refinable |
| V-4 | Los estados no existen fuera de su objeto |
| V-5 | Objeto sin estados: solo creado o destruido |
| V-6 | Máximo un estado por defecto; múltiples iniciales/finales permitidos |
| V-7 | Efecto requiere objeto con al menos un estado |
| V-8 | Resultado no conecta directamente al estado inicial |
| V-9 | Efecto solo-entrada sin salida: destino es estado por defecto |
| V-10 | Habilitador desaparece: proceso se detiene |
| V-11 | Unicidad de rol: transformado XOR habilitador |
| V-12 | Evento es solo el segmento objeto→proceso |
| V-13 | Evento se pierde tras evaluación |
| V-14 | AND es el operador por defecto (sin arco) |
| V-15 | XOR/OR aplican a todas las familias procedimentales |
| V-16 | Arco en extremo convergente del abanico |
| V-17 | Abanicos: convergente o divergente |
| V-18 | Probabilístico es siempre XOR |
| V-19 | Resultado simple equivale a XOR de resultados con estado |
| V-20 | Coincidencia de etiquetas de ruta fija trayectoria |
| V-21 | Parámetros de multiplicidad: nombres únicos |
| V-22 | Multiplicidad: anotación junto al extremo del enlace |
| V-23 | Multiplicidad no aplica a procesos directamente |
| V-24 | Misma perseverancia en refinable y refinadores (excepto exhibición) |
| V-25 | Exhibición puede conectar objetos con procesos |
| V-26 | Cuatro combinaciones exhibidor-rasgo válidas |
| V-27 | Clasificación no distingue colección completa/incompleta |
| V-28 | Herencia múltiple permitida |
| V-29 | Atributo discriminante: un valor por especialización |
| V-30 | Bidireccional/recíproco no existen con estado solo en destino |
| V-31 | Invocación implícita: posición vertical determina secuencia |
| V-32 | Misma altura = ejecución paralela |
| V-33 | In-zooming: contorno grueso en padre e hijo |
| V-34 | Descomposición: elipse agrandada contiene subprocesos |
| V-35 | Línea temporal: arriba → abajo |
| V-36 | Agente/instrumento en contorno exterior se distribuyen |
| V-37 | Consumo/resultado NO en contorno exterior de descomposición |
| V-38 | Eventos sistémicos no cruzan límite de descomposición |
| V-39 | Condición omite subproceso: control pasa al siguiente |
| V-40 | Enlace escindido: temprano saca de s1, tardío pone en s2 |
| V-41 | No hay enlaces escindidos con modificador de control |
| V-42 | Cambio de rol instrumento→afectado válido si estados coinciden |
| V-43 | Resultado + consumo sobre mismo objeto = inválido |
| V-44 | Transformador prevalece sobre habilitador |
| V-45 | Duración dentro de la elipse: {min, esp, max} |
| V-46 | SD contiene exactamente un proceso sistémico |
| V-47 | Nombres de objetos únicos en el modelo |
| V-48 | Estado no existe sin su objeto |
| V-49 | Consumido desaparece al inicio del proceso |
| V-50 | Máximo 20-25 cosas por OPD |
| V-51 | Sin oclusión, minimizar cruces |
| V-52 | Un elemento puede aparecer en cualquier número de OPDs |
| V-53 | Ejecución: elipse rellena en color sólido |
| V-54 | Estado actual: resaltado |
| V-55 | Tiempo fluye arriba → abajo en descomposición |
| V-56 | Bidireccional con tags iguales equivale a recíproco |
| V-57 | Partes de agregación pueden transformarse independientemente del todo |
| V-58 | Instancias muestran valores concretos; clases muestran rangos |
| V-59 | Activación asincrónica por eventos: subprocesos independientes |
| V-60 | Átomo del OPD: Basic Construct = 1 Link + 2 Things |
| V-61 | Anatomía de enlace: Source + Destination + Connector (Line + Symbol + Tag? + PathLabel?) |
| V-62 | In-zooming en dos fases: Content Showing + Link Refining |
| V-63 | Colores informativos, no normativos; esquema verde/azul es referencia |
| V-64 | OPM Model = OPD Set + OPL Spec; especifica un System |
| V-65 | Dualidad OPD ↔ OPL: toda afirmación gráfica es reproducible como texto y viceversa |
| V-66 | Connecting: Thing Set (disconnected→connected) con Link Set como instrumento |
| V-67 | Stateless (s=0) vs Stateful (s≥1); Stateful deriva State-Specific Object Set |
| V-68 | State-Specific Object: nombre = estado + nombre del objeto original |
