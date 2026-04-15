---
_manifest:
  urn: urn:fxsl:kb:opm-es-p03
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
    shard_index: 3
    shard_count: 5
    shard_root_urn: urn:fxsl:kb:opm-es
relations:
  cites:
  - urn:fxsl:kb:manual-metodologico-opm-es
  - urn:fxsl:kb:opd-es
  - urn:fxsl:kb:opl-es
---


# OPM — Núcleo conceptual - Parte 03

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

**Descomposición síncrona (*in-zooming*) vs asíncrona (*unfolding*):** la descomposición de un proceso (in-zooming) es síncrona — el proceso padre espera a que todos los subprocesos completen antes de devolver control. En cambio, el despliegue (unfolding) de una relación estructural es asíncrono respecto del flujo de control del proceso: revela estructura estática sin implicar secuenciación temporal. Esta distinción es relevante al decidir si un refinamiento debe modelarse como descomposición (comportamiento secuenciado) o como despliegue (estructura revelada).

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

Los enlaces conectados al **contorno exterior** de un proceso descompuesto tienen semántica distributiva. La especificación formal completa de las reglas de distribución — tipos de enlace, restricciones de frontera, distribución por posición de subproceso, excepciones para eventos ambientales y reglas de escisión — vive en [OPD — Gramática visual de OPM](urn:fxsl:kb:opd-es) §11 y §12.

Invariantes semánticos que esta capa conserva:

- los enlaces de **consumo** y **resultado** no deben conectarse al contorno exterior de un proceso descompuesto;
- los enlaces de agente e instrumento se distribuyen a todos los subprocesos;
- los enlaces de evento desde objetos sistémicos no deben cruzar el límite de la descomposición para iniciar subprocesos — **excepción:** los enlaces de evento desde objetos **ambientales** pueden cruzar este límite; en tal caso la herramienta debería guiar a quien modela para definir cómo manejar la contingencia (véase §12 de la especificación visual);
- si un enlace de condición hace que un subproceso se omita, el control pasa al siguiente.

---

## Enlaces transformadores escindidos con estado especificado

Cuando un enlace de efecto entrada-salida se descompone en subprocesos, el modelo queda subespecificado. La escisión del enlace en un par (entrada al subproceso temprano, salida al subproceso tardío) es el único mecanismo correcto para resolver esa subespecificación.

La especificación formal de los pares escindidos, su tabla de geometría y sus restricciones vive en [OPD — Gramática visual de OPM](urn:fxsl:kb:opd-es) §12.

La realización textual de los enlaces escindidos vive en [OPL-ES](urn:fxsl:kb:opl-es) §4 y §7.

**Cambio de rol con la abstracción:** un objeto puede ser instrumento en un nivel abstracto y afectado en un nivel detallado. Esto es válido si a nivel abstracto sus estados inicial y final coinciden.

### Instancias operacionales del conjunto de objetos involucrados

Como consecuencia de la distribución de enlaces, las siguientes restricciones se aplican a las instancias operacionales de los transformados:

1. Cada instancia operacional de un **consumido** en el conjunto previo al proceso DEBE dejar de existir al inicio del subproceso más detallado que lo consume, y la instancia operacional no está en el conjunto posterior al proceso.
2. Cada instancia operacional de un **afectado** en el conjunto previo al proceso que cambia de estado DEBE salir de su estado de entrada al inicio del subproceso más detallado que cambia al afectado.
3. Cada instancia operacional de un **afectado** en el conjunto posterior al proceso que cambia de estado DEBE entrar en su estado de salida al completarse el subproceso más detallado que cambia al afectado.
4. Cada instancia operacional de un **resultante** en el conjunto posterior al proceso DEBE comenzar a existir al completarse el subproceso más detallado que lo genera, y la instancia operacional no está en el conjunto previo al proceso.

---

## Precedencia de enlaces durante la recomposición

Al recomponer, los enlaces procedimentales de subprocesos migran al proceso padre. La **fuerza semántica** determina cuál prevalece cuando dos enlaces compiten por el mismo par objeto-proceso.

La especificación formal de la jerarquía completa de precedencia, incluyendo la matriz transformadora, el orden principal `consumo = resultado > efecto > agente > instrumento`, la precedencia secundaria por modificador de control y el orden completo de **12 niveles** de fuerza semántica, vive en [OPD — Gramática visual de OPM](urn:fxsl:kb:opd-es) §13.

Los invariantes semánticos que gobiernan la precedencia se formalizan en `opm-visual-es` §13. Esta capa no los re-enuncia para evitar duplicación con divergencia.

---

## Etiquetas OPD y navegación

**El SD contiene exactamente un proceso sistémico**, que expresa la función del sistema. Puede contener uno o más procesos ambientales.

Etiquetas típicas:

- `SD` para nivel 0;
- `SD1`, `SD2`, etc., para niveles descendientes.

**Etiquetas de aristas del árbol OPD:** cada arista del árbol de procesos usa un enlace estructural etiquetado unidireccional con una fórmula de refinamiento equivalente a `se refina por descomposición de NombreProceso en` o `se refina por despliegue de NombreCosa en`. La realización textual canónica de estas sentencias pertenece a [OPL-ES](urn:fxsl:kb:opl-es) §10.

**Orden de especificación OPL:** la secuencia de párrafos OPL sigue en general orden en anchura, comenzando desde `SD`. El procedimiento operativo de recorrido pertenece a [Manual metodológico de OPM](urn:fxsl:kb:manual-metodologico-opm-es).

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

### Principio de consistencia de hechos OPM

Si un hecho aparece en un OPD y contradice otro hecho del mismo modelo en otro OPD, el modelo es inconsistente y la herramienta debería detectarlo. Que un hecho sea refinamiento o abstracción de otro no constituye contradicción.

---

## Diagrama de sistema: procedimiento y componentes

El SD es el OPD de nivel 0 y proporciona una vista de alto nivel comprensible para cualquier interesado, incluso sin especialización técnica. En la capa base solo interesa su función semántica: expresar la función del sistema y su contexto de máximo nivel.

La construcción detallada del SD, sus variantes por tipo de sistema, la secuencia de preguntas, la jerarquía de detalle, los nodos de decisión y las reglas de praxis asociadas pertenecen a [Manual metodológico de OPM](urn:fxsl:kb:manual-metodologico-opm-es).

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

## Sintaxis formal de OPL: delegación editorial

La gramática formal completa de OPL-ES deja de vivir en esta capa para eliminar solapamiento con la capa textual canónica. La EBNF española completa, incluyendo producción base, oraciones procedimentales, estructurales, condicionales y de gestión de contexto, vive ahora exclusivamente en [OPL-ES](urn:fxsl:kb:opl-es), Apéndice A.

> **Nota:** El Apéndice A de OPL-ES forma parte vinculante de la capa textual canónica. Las producciones EBNF definidas allí son parte de la especificación del corpus.

Este documento conserva solo el contrato semántico que la gramática textual debe preservar:

- la dualidad OPD–OPL;
- la correspondencia entre familia semántica de enlace y plantilla textual;
- la trazabilidad entre refinamiento del modelo y composición textual;
- la equivalencia semántica entre la formulación inglesa de referencia y la formulación canónica española.

---

## Metamodelo OPM

La estructura del modelo OPM tiene dos jerarquías paralelas:

- **Modelo OPM** → conjunto de OPDs (gráfico) + especificación OPL (texto)
- **Conjunto de OPDs** → OPDs → constructos OPD → conjuntos de cosas + conjuntos de enlaces
- **Especificación OPL** → párrafos OPL → oraciones OPL → frases y nombres reservados

Un **constructo básico** contiene exactamente 2 cosas y 1 enlace. Los constructos compuestos incluyen abanicos de enlaces o más de dos refinadores.
