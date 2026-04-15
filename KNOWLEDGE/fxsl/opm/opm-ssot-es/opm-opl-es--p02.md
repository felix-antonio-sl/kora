---
_manifest:
  urn: urn:fxsl:kb:opl-es-p02
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
    shard_index: 2
    shard_count: 5
    shard_root_urn: urn:fxsl:kb:opl-es
---

# OPL-ES — Lenguaje Objeto-Proceso en Español - Parte 02

## 7. Plantillas OPL-ES — Enlaces de Condición

### 7.1 Condición Transformadores

| ID | OPL-EN | OPL-ES |
|----|--------|--------|
| CT1 | Process occurs if Object exists, in which case Object is consumed, otherwise Process is skipped. | *Proceso* ocurre si **Objeto** existe, en cuyo caso **Objeto** se consume, de lo contrario *Proceso* se omite. |
| CT2 | Process occurs if Object exists, in which case Process affects Object, otherwise Process is skipped. | *Proceso* ocurre si **Objeto** existe, en cuyo caso *Proceso* afecta **Objeto**, de lo contrario *Proceso* se omite. |

### 7.2 Condición Habilitadores

| ID | OPL-EN | OPL-ES |
|----|--------|--------|
| CH1 | Agent handles Process if Agent exists, else Process is skipped. | **Agente** maneja *Proceso* si **Agente** existe, de lo contrario *Proceso* se omite. |
| CH2 | Process occurs if Instrument exists, else Process is skipped. | *Proceso* ocurre si **Instrumento** existe, de lo contrario *Proceso* se omite. |

### 7.3 Condición con Estado Especificado

| ID | OPL-EN | OPL-ES |
|----|--------|--------|
| CS1 | Process occurs if Object is specified-state, in which case Object is consumed, otherwise Process is skipped. | *Proceso* ocurre si **Objeto** está en `estado`, en cuyo caso **Objeto** se consume, de lo contrario *Proceso* se omite. |
| CS2 | Process occurs if Object is input-state, in which case Process changes Object from input-state to output-state, otherwise Process is skipped. | *Proceso* ocurre si **Objeto** está en `estado-entrada`, en cuyo caso *Proceso* cambia **Objeto** de `estado-entrada` a `estado-salida`, de lo contrario *Proceso* se omite. |
| CS3 | Process occurs if Object is input-state, in which case Process changes Object from input-state, otherwise Process is skipped. | *Proceso* ocurre si **Objeto** está en `estado-entrada`, en cuyo caso *Proceso* cambia **Objeto** de `estado-entrada`, de lo contrario *Proceso* se omite. |
| CS4 | Process occurs if Object exists, in which case Process changes Object to output-state, otherwise Process is skipped. | *Proceso* ocurre si **Objeto** existe, en cuyo caso *Proceso* cambia **Objeto** a `estado-salida`, de lo contrario *Proceso* se omite. |
| CS5 | Agent handles Process if Agent is specified-state, else Process is skipped. | **Agente** maneja *Proceso* si **Agente** está en `estado`, de lo contrario *Proceso* se omite. |
| CS6 | Process occurs if Instrument is specified-state, otherwise Process is skipped. | *Proceso* ocurre si **Instrumento** está en `estado`, de lo contrario *Proceso* se omite. |

---

## 8. Plantillas OPL-ES — Excepción e Invocación

### 8.1 Enlaces de Excepción

| ID | Tipo | OPL-EN | OPL-ES |
|----|------|--------|--------|
| EX1 | Overtime | Handling occurs if duration of Source exceeds max-duration time-units. | *Manejo* ocurre si duración de *Fuente* excede máx-duración unidades-tiempo. |
| EX2 | Undertime | Handling occurs if duration of Source falls short of min-duration time-units. | *Manejo* ocurre si duración de *Fuente* es menor que mín-duración unidades-tiempo. |

### 8.2 Enlaces de Invocación

| ID | Tipo | OPL-EN | OPL-ES |
|----|------|--------|--------|
| IV1 | Invocación | Invoking invokes Invoked. | *Invocador* invoca *Invocado*. |
| IV2 | Auto-invocación | Invoking invokes itself. | *Invocador* se invoca a sí mismo. |

---

## 9. Plantillas OPL-ES — Enlaces Estructurales

### 9.1 Etiquetados

| ID | Tipo | OPL-EN | OPL-ES |
|----|------|--------|--------|
| SE1 | Unidireccional etiquetado | Source tag Destination. | **Origen** etiqueta **Destino**. |
| SE2 | Unidireccional sin etiqueta | Source relates to Destination. | **Origen** se relaciona con **Destino**. |
| SE3 | Bidireccional etiquetado | Source f-tag Dest. / Dest b-tag Source. | **Origen** etiqueta-f **Destino**. / **Destino** etiqueta-b **Origen**. |
| SE4 | Recíproco etiquetado | Source and Destination are tag. | **Origen** y **Destino** son etiqueta. |
| SE5 | Recíproco sin etiqueta | Source and Destination are related. | **Origen** y **Destino** se relacionan. |

Nota: en SE1, SE3 y SE4, "etiqueta" es la forma definida por el modelador en español (ej. "emplea", "pertenece a", "supervisa"). La etiqueta actúa como verbo o predicado nominal de la oración.

### 9.2 Relaciones Estructurales Fundamentales

| ID | Relación | OPL-EN | OPL-ES |
|----|----------|--------|--------|
| RF1 | Agregación-participación | Whole consists of Part1, Part2 and Part3. | **Todo** consta de **Parte1**, **Parte2** y **Parte3**. |
| RF2 | Exhibición-caracterización (solo atributos) | Exhibitor exhibits Attribute1 and Attribute2. | **Exhibidor** exhibe **Atributo1** y **Atributo2**. |
| RF2b | Exhibición-caracterización (atributos + operaciones) | Exhibitor exhibits Attribute1 as well as Operation1. | **Exhibidor** exhibe **Atributo1** así como *Operación1*. |
| RF3 | Generalización-especialización (compuesto) | Specialization1 and Specialization2 are General. | **Especialización1** y **Especialización2** son **General**. |
| RF3b | Generalización-especialización (individual) | Specialization is a General. | **Especialización** es un **General**. |
| RF4 | Clasificación-instanciación | Instance is an instance of Class. | **Instancia** es una instancia de **Clase**. |

### 9.3 Colecciones Incompletas

| OPL-EN | OPL-ES |
|--------|--------|
| …and at least one other part. | …y al menos otra parte. |
| …and at least one other feature. | …y al menos otro rasgo. |
| …and at least one other specialization. | …y al menos otra especialización. |

### 9.4 Estructurales con Estado Especificado

| ID | Grupo | OPL-EN | OPL-ES |
|----|-------|--------|--------|
| SSE1 | Estado en origen (uni) | Specified-state Source tag Destination. | **Origen** en `estado` etiqueta **Destino**. |
| SSE2 | Estado en destino (uni) | Source tag specified-state Destination. | **Origen** etiqueta **Destino** en `estado`. |
| SSE3 | Estado en ambos (uni) | Sa Source tag Sb Destination. | **Origen** en `sa` etiqueta **Destino** en `sb`. |
| SSE4 | Estado en origen (bidi, f-tag) | Sa Source f-tag Destination. | **Origen** en `sa` etiqueta-f **Destino**. |
| SSE5 | Estado en origen (bidi, b-tag) | Destination b-tag Sa Source. | **Destino** etiqueta-b **Origen** en `sa`. |
| SSE6 | Estado en ambos (recíproco) | Sa Source and Sb Dest are tag. | **Origen** en `sa` y **Destino** en `sb` son etiqueta. |
| SSE7 | Estado en origen (recíproco) | Dest and Sa Source are tag. | **Destino** y **Origen** en `sa` son etiqueta. |

---

## 10. Plantillas OPL-ES — Gestión de Contexto

### 10.1 Descomposición (In-Zooming)

| ID | OPL-EN | OPL-ES |
|----|--------|--------|
| CX1 | Process zooms into P1, P2 and P3, in that sequence. | *Proceso* se descompone en *P1*, *P2* y *P3*, en esa secuencia. |
| CX2 | Process zooms into parallel P1 and P2. | *Proceso* se descompone en paralelo *P1* y *P2*. |

### 10.2 Despliegue (Unfolding)

| ID | OPL-EN | OPL-ES |
|----|--------|--------|
| CX3 | Thing unfolds in SD1 into T1, T2 and T3. | **Cosa** se despliega en SD1 en **T1**, **T2** y **T3**. |

### 10.3 Refinamiento entre OPDs

| ID | OPL-EN | OPL-ES |
|----|--------|--------|
| CX4 | SD is refined by in-zooming Process in SD1. | SD se refina por descomposición de *Proceso* en SD1. |

### 10.4 Plegado y Recomposición

| ID | OPL-EN | OPL-ES |
|----|--------|--------|
| CX5 | Process folds into parent OPD. | *Proceso* se pliega en el OPD padre. |
| CX6 | Object folds into parent OPD. | **Objeto** se pliega en el OPD padre. |
| CX7 | Process recomposes from diagram. | *Proceso* se recompone desde `diagrama`. |
| CX8 | Object recomposes from diagram. | **Objeto** se recompone desde `diagrama`. |

---

## 11. Operadores Lógicos

### 11.1 AND

AND se expresa implícitamente mediante sentencias OPL separadas para cada enlace. No hay operador explícito — cada enlace genera su propia oración. Gráficamente: enlaces separados (no se tocan) en el contorno del proceso.

Ejemplo AND de agentes:

- EN: `Safe Owner A handles Safe Opening.` / `Safe Owner B handles Safe Opening.`
- ES: **Dueño de Caja Fuerte A** maneja *Abrir Caja Fuerte*. / **Dueño de Caja Fuerte B** maneja *Abrir Caja Fuerte*.

### 11.2 XOR

Gráficamente: arco discontinuo simple. EN: "exactly one of". ES: "exactamente uno de".

| Familia | OPL-EN | OPL-ES |
|---------|--------|--------|
| Consumo conv. | P consumes exactly one of A, B, or C. | *P* consume exactamente uno de **A**, **B** o **C**. |
| Consumo div. | Exactly one of P, Q, or R consumes B. | Exactamente uno de *P*, *Q* o *R* consume **B**. |
| Resultado conv. | Exactly one of P, Q, or R yields B. | Exactamente uno de *P*, *Q* o *R* genera **B**. |
| Resultado div. | P yields exactly one of A, B, or C. | *P* genera exactamente uno de **A**, **B** o **C**. |
| Efecto (objetos) | P affects exactly one of A, B, or C. | *P* afecta exactamente uno de **A**, **B** o **C**. |
| Efecto (procesos) | Exactly one of P, Q, or R affects B. | Exactamente uno de *P*, *Q* o *R* afecta **B**. |
| Agente | B handles exactly one of P, Q, or R. | **B** maneja exactamente uno de *P*, *Q* o *R*. |
| Instrumento | Exactly one of P, Q, or R requires B. | Exactamente uno de *P*, *Q* o *R* requiere **B**. |
| Invocación div. | P invokes exactly one of Q or R. | *P* invoca exactamente uno de *Q* o *R*. |
| Invocación conv. | Exactly one of P or Q invokes R. | Exactamente uno de *P* o *Q* invoca *R*. |

### 11.3 OR

Misma estructura que XOR, reemplazando:

- EN: "exactly one of" → "at least one of"
- ES: "exactamente uno de" → "al menos uno de"

Gráficamente: arco doble (dos arcos concéntricos discontinuos).

### 11.4 XOR/OR con Modificadores de Control

Los abanicos XOR y OR se combinan con modificadores evento ("e") y condición ("c"). Regla de composición:

**Evento + XOR** — insertar "inicia" antes del verbo principal:

- EN: `B initiates exactly one of P, Q, or R, which affects B.`
- ES: **B** inicia exactamente uno de *P*, *Q* o *R*, que afecta **B**.

**Condición + XOR** — insertar "si … existe/está en estado … de lo contrario … se omite":

- EN: `Exactly one of P, Q, R occurs if B exists, otherwise skipped.`
- ES: Exactamente uno de *P*, *Q* o *R* ocurre si **B** existe, de lo contrario se omite.

Reemplazar "exactamente" por "al menos" para obtener la variante OR.

### 11.5 Probabilístico

Anotación `Pr=p` en cada enlace del abanico. Suma de probabilidades = 1. Notación numérica universal, sin cambio entre EN y ES.

---

## 12. Cardinalidad y Multiplicidad

| Símbolo | Rango | OPL-EN | OPL-ES |
|---------|-------|--------|--------|
| ? | 0..1 | an optional | un/una opcional |
| * | 0..* | optional (none to many) | opcional (cero o más) |
| (ninguno) | 1..1 | (default) | (por defecto) |
| + | 1..* | at least one | al menos un/una |

Rango parametrizado: `qmín..qmáx`. Restricciones con =, ≠, <, ≤, ≥, ∈. Sin cambio sintáctico entre EN y ES (notación matemática universal).

**Ejemplo de multiplicidad parametrizada**:

- EN: `Jet Engine consists of b Installed Blades.`
- ES: **Motor a Reacción** consta de b **Paletas Instaladas**.

### 12.1 Tipo

| OPL-EN | OPL-ES |
|--------|--------|
| Object is of type type-id. | **Objeto** es de tipo tipo-id. |

Tipos: boolean, string, integer, float, double, short, long, enumerated. Sin traducción (identificadores de tipo universales).

Producción formal: véase Apéndice A.4 (`oracion_de_tipo_de_dato`).

---

## 13. Etiquetas de Ruta

| OPL-EN | OPL-ES |
|--------|--------|
| Following path label, Process consumes Object. | Por ruta etiqueta, *Proceso* consume **Objeto**. |
| Following path label, Process yields Object. | Por ruta etiqueta, *Proceso* genera **Objeto**. |

"Por ruta" es la expresión fija. "etiqueta" es el nombre de la ruta definido por el modelador.

**Ejemplo (Preparar Alimento)**:

- EN: `Following path carnivore, Food Preparing consumes Meat, yields Stew and Steak.`
- ES: Por ruta carnívoro, *Preparar Alimento* consume **Carne**, genera **Estofado** y **Bistec**.

- EN: `Following path herbivore, Food Preparing consumes Cucumber and Tomato, yields Salad.`
- ES: Por ruta herbívoro, *Preparar Alimento* consume **Pepino** y **Tomate**, genera **Ensalada**.

---

## 14. Atributos y Valores

| OPL-EN | OPL-ES |
|--------|--------|
| Attribute of Object is value. | **Atributo** de **Objeto** es valor. |
| Attribute of Object ranges from X to Y. | **Atributo** de **Objeto** varía de X a Y. |
| Attribute of Object can be value1, value2, or value3. | **Atributo** de **Objeto** puede estar `valor1`, `valor2` o `valor3`. |

**Ejemplo**:

- EN: `Cleanliness of Dish Set can be dirty or clean.`
- ES: **Limpieza** de **Conjunto de Platos** puede estar `sucia` o `limpia`.

- EN: `State dirty of Cleanliness of Dish Set is initial.`
- ES: Estado `sucia` de **Limpieza** de **Conjunto de Platos** es inicial.

---

## 15. Reglas de Transformación Sistemática EN → ES

Para implementadores de herramientas. Reglas aplicadas en secuencia sobre una sentencia OPL-EN para producir OPL-ES:

| # | Regla | EN | ES |
|---|-------|----|----|
| R1 | Verbo principal | consumes, yields, affects, handles, requires, initiates, invokes, occurs, exists | consume, genera, afecta, maneja, requiere, inicia, invoca, ocurre, existe |
| R2 | State-specified: posición | `state Object` (estado antes del objeto) | **Objeto** en `estado` (estado después del objeto con "en") |
| R3 | Estado condicional | Object is state | **Objeto** está en `estado` |
| R4 | Declaración de estados | can be | puede estar |
| R5 | Conjunción copulativa | and | y (e ante i-/hi-) |
| R6 | Conjunción disyuntiva | or | o (u ante o-/ho-) |
| R7 | Preposición de origen | from | de |
| R8 | Preposición de destino | to | a |
| R9 | Preposición posesiva | of | de |
| R10 | Cuantificador XOR | exactly one of | exactamente uno de |
| R11 | Cuantificador OR | at least one of | al menos uno de |
| R12 | Condicional | if … exists | si … existe |
| R13 | Consecuencia | in which case | en cuyo caso |
| R14 | Alternativa | otherwise / else | de lo contrario |
| R15 | Pasiva refleja | is consumed / is skipped | se consume / se omite |
| R16 | Ruta | Following path | Por ruta |
| R17 | Artículo en instanciación | is an instance of | es una instancia de |
| R18 | Artículo en especialización (sg.) | is a | es un/una |
| R19 | Secuencia | in that sequence | en esa secuencia |
| R20 | Designación de estado | is initial / is final / is default | es inicial / es final / es por defecto |
| R21 | Nombres de entidad | (sin cambio — definidos por el modelador) | (sin cambio) |

**Nota para analizadores**: el verbo principal (R1) es el ancla léxica para detectar el idioma de la sentencia. Un analizador puede determinar EN vs ES verificando si el primer verbo conjugado pertenece al conjunto EN o ES.

---
