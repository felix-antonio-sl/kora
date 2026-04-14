---
_manifest:
  urn: "urn:fxsl:kb:metodologia-modelamiento-opm"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-04-14"
    source: "synthesis:opm-iso-19450-es,opm-opl-es,opcloud-tutorial-videos,opm-applied-system-modeling,opm-canonical-example"
version: "3.7.0"
status: published
tags: [opm, methodology, system-modeling, sd-construction, refinement, complexity-management, modeling-protocol, patrones, antipatterns, control-flow, error-handling, quantitative, simulation, executable-modeling, opcloud]
lang: es
extensions:
  kora:
    family: specification
    depends_on:
      - "urn:fxsl:kb:opm-iso-19450-es"
      - "urn:fxsl:kb:opm-opl-es"
---

# Metodología de Modelamiento OPM — Protocolo de Modelamiento Conceptual de Sistemas

## 1 Definición

Esta especificación define la metodología para construir modelos conceptuales de sistemas usando Object-Process Methodology (OPM). Consolida reglas normativas desde [OPM ISO/PAS 19450](urn:fxsl:kb:opm-iso-19450-es) y [OPL-ES](urn:fxsl:kb:opm-opl-es), e incorpora directamente la guía operativa de uso de herramienta previamente dispersa en artefactos hoy deprecados. Para la especificación formal del lenguaje OPM, ver [OPM ISO/PAS 19450](urn:fxsl:kb:opm-iso-19450-es). Para la realización textual en español, ver [OPL-ES](urn:fxsl:kb:opm-opl-es).

### 1.1 Alcance y Precedencia del Corpus

Este artefacto es una **guía derivada**. No reemplaza la base normativa del corpus.

Orden de precedencia:

1. **ISO 19450** gobierna semántica OPM, notación, relaciones y procedimiento base de construcción del SD.
2. **OPL-ES** gobierna la realización textual en español sin alterar la semántica OPM.
3. **Esta metodología** integra las capas normativas anteriores y explicita reglas operativas para ciclo de vida, simulación, gobernanza del modelo y uso de herramienta.

Regla de resolución:

- Si una regla de **semántica OPM** entra en conflicto con una regla de herramienta, prevalece ISO 19450.
- Si un artefacto en `lang: es` define **realización OPL en español** como parte de su contrato, prevalece OPL-ES. Un artefacto expositivo en `lang: es` PUEDE mantener sentencias OPL canónicas en inglés para preservar roundtrip con ISO/OPCloud, siempre que lo declare explícitamente y no presente esas sentencias como OPL-ES.
- Las capacidades de OPCloud NO redefinen por sí solas la semántica de OPM; solo operacionalizan su uso en la herramienta.
- Los artefactos deprecados del directorio NO participan en precedencia; solo sirven como enrutamiento histórico.

## 2 Definiciones

| Término | Definición |
|---------|-----------|
| SD (Diagrama de Sistema) | OPD raíz que muestra la función del sistema y su contexto de nivel superior (§3.75) |
| SD1 | OPD descendiente de SD donde el proceso principal se refina exponiendo subprocesos. [Extensión no-ISO: convención de etiquetado derivada] |
| OPD (Object-Process Diagram) | Representación gráfica OPM de un modelo o parte de un modelo (§3.41) |
| OPL (Object-Process Language) | Representación textual de OPM; en esta edición, OPL-ES es la forma canónica (§3.42) |
| Beneficiario | Interesado que recibe valor funcional de la operación del sistema (§3.6) |
| Transformado | Objeto afectado por un proceso (§3.78) |
| Afectado | Transformado cuyo estado cambia por acción de un proceso; debe ser un objeto con estados (§3.2) |
| Consumido | Transformado que un proceso consume o elimina (§3.10) |
| Resultante | Transformado que un proceso crea (§3.64) |
| Agente | Habilitador que es una persona o un grupo de personas (§3.3) |
| Instrumento | Habilitador no humano (§3.30) |
| Función | Proceso que entrega valor funcional a un beneficiario (§3.23) |
| Arquitectura | Combinación de estructura + comportamiento que habilita la función y produce emergencia. [Extensión no-ISO: síntesis conceptual] |
| Emergencia | Capacidad del sistema completo que ninguna parte individual exhibe. [Extensión no-ISO: concepto de ingeniería de sistemas] |
| Proceso persistente | Proceso cuyo efecto es mantener el estado de un objeto, no cambiarlo (§7.2.1 NOTE 2) |
| Objeto transiente | Objeto de vida corta creado y consumido inmediatamente entre dos procesos. [Extensión no-ISO: conveniencia de modelado] |
| Fuerza semántica | Precedencia de un enlace procedimental que determina cuál prevalece en conflictos. [Extensión no-ISO: derivada de la tabla de precedencia §14 de ISO 19450] |
| Principio del Nombre Singular | Los nombres de cosas en OPM DEBEN ser singulares. En inglés, colecciones humanas usan "Group" y las inanimadas "Set". En español, los equivalentes son "Grupo" y "Conjunto". [Extensión no-ISO: nombre asignado por esta metodología a una convención de ISO 19450] |

## 3 Fundamentos Ontológicos

Los fundamentos ontológicos de OPM están formulados en el trabajo de Dori (*Model-Based Systems Engineering with OPM and SysML*) y subyacen a ISO/PAS 19450 sin que la norma los nombre individualmente como principios, teoremas o aserciones. Las formulaciones de esta sección provienen del textbook de referencia, no del texto normativo de ISO/PAS 19450.

### 3.1 Principio de Ontología Mínima [Textbook de Dori]

> Si un sistema puede especificarse al mismo nivel de precisión y detalle con dos lenguajes de diferentes tamaños ontológicos, el lenguaje con ontología menor es preferible, siempre que la comprensibilidad sea comparable.

OPM usa dos clases de elementos: **cosas** (objetos y procesos) y **enlaces** (procedimentales y estructurales), que expresan relaciones entre cosas (cfr. ISO 19450 §3.16, §3.36, §3.76).

### 3.2 Teorema Objeto-Proceso [Textbook de Dori]

> Objetos, procesos y relaciones entre ellos constituyen una ontología universal mínima.

Demostrado por necesidad (especificar estructura requiere objetos; especificar comportamiento requiere procesos) y suficiencia (las cosas existen o suceden; solo se asocian mediante relaciones). Los objetos pueden ser con estados (con estados explícitos, transformables vía efecto) o sin estados (solo creables/consumibles). La distinción con estados / sin estados es posterior a la base ontológica.

### 3.3 Aserción Objeto-Proceso [Textbook de Dori]

> Usando objetos, procesos, relaciones, y mecanismos de refinamiento (descomposición y despliegue), se puede modelar conceptualmente cualquier sistema en cualquier dominio y nivel de complejidad.

## 4 Principios de Modelamiento

ISO/PAS 19450 define seis principios de modelado OPM. Todo modelamiento DEBE respetarlos. A continuación se reproducen fielmente; después se listan reglas complementarias derivadas del estándar y del textbook de Dori.

### 4.1 Principios ISO/PAS 19450

**Principio 1 — Actividad al servicio de un propósito.** La función del sistema y el propósito del modelado definen el alcance y el nivel de detalle. Diferentes interesados requieren diferentes vistas del mismo sistema.

**Principio 2 — Unificación de función, estructura y comportamiento.** Estructura más comportamiento producen función. La estructura reúne objetos físicos e informacionales y sus relaciones estructurales. El comportamiento reúne procesos que transforman objetos a lo largo del tiempo.

**Principio 3 — Identificación del valor funcional.** El proceso que entrega valor expresa la función tal como la percibe el beneficiario principal. Identificar y nombrar ese proceso es el paso crítico inicial.

**Principio 4 — Función vs comportamiento.** La función es el valor para el beneficiario; el comportamiento es cómo opera el sistema. La misma función puede implementarse con estructuras y comportamientos distintos.

**Principio 5 — Definición del límite del sistema.** El entorno es el conjunto de cosas fuera del sistema que pueden interactuar con él. Las cosas sistémicas tienen contorno sólido; las ambientales, contorno discontinuo.

**Principio 6 — Equilibrio entre claridad y completitud.** Los sistemas reales contienen demasiado detalle para una sola vista. La comprensión requiere balancear claridad y completitud mediante una jerarquía de OPDs.

### 4.2 Reglas complementarias derivadas

Las siguientes reglas no son los seis principios de modelado de ISO/PAS 19450, sino restricciones derivadas de otras secciones del estándar y del textbook de Dori. También DEBEN respetarse.

**Function-as-a-Seed [Textbook de Dori].** El modelamiento de un sistema DEBE comenzar definiendo, nombrando y representando la función del sistema, que es su proceso de nivel superior. La función es la semilla de la que evoluciona el modelo. Comenzar por la forma (objetos) en vez de la función (proceso) es un error común. (Operacionaliza los principios ISO 1 y 3.)

**Importancia de Cosa [Textbook de Dori].** La importancia de una cosa T en un modelo OPM es directamente proporcional al OPD más alto en la jerarquía donde T aparece. Objetos y procesos tienen igual estatus; ninguno tiene supremacía sobre el otro.

**Transformación de Objeto por Proceso [derivada de ISO §3.58, §3.77].** En un modelo OPM completo, cada proceso DEBE estar conectado a al menos un objeto que el proceso transforma o a un estado de ese objeto. Un proceso sin enlace transformador no tiene significado. Un proceso PUEDE tener múltiples transformados.

**Unicidad de Enlace Procedimental [derivada de ISO §10].** A cualquier nivel de detalle, un objeto y un proceso PUEDEN estar conectados con a lo sumo un enlace procedimental, que determina unívocamente el rol del objeto respecto al proceso. *Resolución de colisión de roles:* Cuando un objeto es simultáneamente habilitador (agente o instrumento) y transformado (afectado) del mismo proceso, el enlace transformador DEBE prevalecer por mayor fuerza semántica. El modelador PUEDE agregar un stick-figure para preservar la identidad humana del agente desplazado. Alternativa: hacer descomposición al proceso y asignar enlace de agente a un subproceso y enlace de efecto a otro.

**Representación de Hechos del Modelo [derivada de ISO §3.38].** Todo hecho del modelo DEBE aparecer en al menos un OPD del set de OPDs del modelo. No todo hecho necesita repetirse en cada OPD. Suficiente con que aparezca al menos una vez.

**Equivalencia Gráfico-Texto [derivada de ISO §3.41, §3.42].** Todo modelo OPM DEBE expresarse en modalidades gráficas (OPD) y textuales (OPL) semánticamente equivalentes. Cada OPD tiene un párrafo OPL correspondiente. La redundancia aprovecha canales cognitivos duales (visual + verbal).

**Jerarquía de Detalle [operacionaliza Principio ISO 6].** Cuando un OPD se vuelve difícil de comprender por exceso de detalle, se DEBE crear un nuevo OPD descendiente. Heurística: un OPD NO DEBERÍA exceder 20-25 entidades ni una pantalla/página.

**Trade-off Completitud-Claridad [operacionaliza Principio ISO 6].** El detalle abrumador de sistemas reales DEBE balancearse distribuyendo la especificación completa a través del set de OPDs, manteniendo cada OPD individual claro y comprensible.

## 5 Clasificación del Sistema

Antes de construir el SD, el modelador DEBE clasificar el sistema. La clasificación determina qué componentes del SD aplican.

Reglas prescriptivas por categoría:

- **Artificial**: DEBE modelarse con los 5 componentes completos
- **Natural**: NO DEBE modelarse propósito (usar "resultado"). NO DEBE modelarse ocurrencia del problema. NO hay agentes humanos — solo instrumentos. Componentes aplicables del SD: función principal (sí), habilitadores del proceso (sí, solo instrumentos), entorno (sí), propósito (no → resultado), ocurrencia del problema (no)
- **Social**: DEBE modelarse con los 5 componentes completos. Se PUEDE usar enlaces habilitadores con estado especificado para condiciones ambientales
- **Socio-técnico**: DEBE modelarse con los 5 componentes completos. Se PUEDE usar enlaces estructurales etiquetados para relaciones no fundamentales

### 5.1 Patrones de Referencia por Categoría [Textbook de Dori]

Los siguientes patrones sintetizan ejemplos pedagógicos del textbook de referencia de Dori, no de ISO/PAS 19450. Son útiles para clasificar el sistema antes de construir el SD:

| Categoría | Patrón de referencia | Lección operativa |
|-----------|----------------------|-------------------|
| Artificial | `Airplane Flying`, `Battery Charging` | Hay propósito explícito, ocurrencia del problema, agentes humanos y un objeto proveedor de beneficio claramente identificable |
| Natural | `Fetus Developing`, `Rain Storm Forming` | Se modela resultado en vez de propósito; el resultado puede ser beneficioso o perjudicial; no hay agentes humanos |
| Social | `Conference Occurring` | Las condiciones ambientales PUEDEN expresarse con enlaces habilitadores con estado especificado, por ejemplo `good Weather` |
| Socio-técnico | `Online Professional Identity Managing` | Los enlaces estructurales etiquetados suelen ser necesarios para relaciones no fundamentales, por ejemplo `Profile represents User` |
| Físico con partes informacionales | `Baggage Transporting` | Un sistema con seguimiento o software auxiliar SIGUE clasificándose como físico si la transformación dominante es física |

## 6 Construcción del SD — Nivel 0

El SD DEBE ser simple y claro, con mínimos detalles técnicos. Todos los interesados DEBEN poder comprender el SD sin pericia técnica.

### 6.0 Asistente Agnóstico de Construcción del SD [Extensión no-ISO]

El asistente del SD es un **protocolo de interacción** agnóstico de herramienta. No presupone OPCloud, formularios, UI gráfica ni asistente LLM. Cualquier implementación válida DEBE guiar al modelador por una secuencia ordenada de puntos de control y producir, al final, un SD semánticamente completo. ISO/PAS 19450 define un procedimiento guiado de nueve preguntas para la construcción del SD. Este asistente extiende ese procedimiento con etapas adicionales de clasificación (etapa 0), resolución de agencia (etapa 5) y verificación formal (etapa 11).

**Implementaciones válidas:** entrevista guiada, formulario estructurado, lista de verificación operativa, asistente conversacional, plugin de modelado o flujo de trabajo humano moderado.

**Regla central:** cada etapa del asistente DEBE cerrar con un hecho del modelo explicitado y listo para representarse en OPD/OPL. El asistente NO termina cuando el usuario "entiende" el sistema; termina cuando los hechos mínimos del SD quedaron decididos.

**Pre-etapa obligatoria:** antes de iniciar el asistente, el modelador DEBE clasificar el sistema según §5. La clasificación determina si se habla de propósito o resultado y si la `Ocurrencia del Problema` aplica.

| Etapa | Objetivo | Salida mínima obligatoria | Mapeo metodológico |
|-------|----------|---------------------------|---------------------|
| 0 | Clasificar sistema | Tipo: artificial / natural / social / socio-técnico | §5 |
| 1 | Fijar proceso principal | Nombre canónico del proceso principal | §6.1 |
| 2 | Identificar interesado primario | Grupo beneficiario o afectado equivalente | §6.2 |
| 3 | Fijar valor a transformar | Atributo del beneficiario/resultado + estados de entrada/salida | §6.3 |
| 4 | Fijar función principal | Objeto proveedor de beneficio + atributo funcional, si aplica | §6.4 |
| 5 | Resolver agencia humana | Conjunto de agentes válido o declaración explícita de ausencia | §6.5 |
| 6 | Delimitar el sistema | Nombre del sistema + exhibición del proceso principal | §6.6 |
| 7 | Identificar habilitadores no humanos | Conjunto de instrumentos | §6.7 |
| 8 | Fijar transformados y resultados | Entradas, afectados y salidas | §6.8 |
| 9 | Delimitar contexto externo | Objetos/procesos del entorno | §6.9 |
| 10 | Modelar problema inicial, si aplica | Ocurrencia del problema o decisión explícita de no-aplicación | §6.10 |
| 11 | Cerrar con compuerta de consistencia | Lista de verificación SD `PASA/FALLA` | §6.11 |

**Semántica de cierre por etapa:**

- Si una etapa no puede cerrarse, el wizard DEBE retroceder a la etapa anterior que bloquea la decisión.
- Si el sistema es **natural**, la etapa 10 DEBE cerrarse como `NO APLICA`, no como omisión silenciosa.
- Si el sistema transforma múltiples objetos, la etapa 4 DEBE dejar explicitado cuál es el `Objeto Proveedor de Beneficio`.
- Si no existen agentes humanos, la etapa 5 DEBE registrar `sin agentes humanos` en vez de forzar un marcador de posición.

**Contrato de salida del asistente:** un asistente agnóstico correcto entrega, como mínimo, un paquete de decisiones equivalente a:

1. tipo de sistema
2. proceso principal
3. beneficiario/afectado
4. atributo de valor + transición de estados
5. función principal
6. agentes
7. sistema + exhibición
8. instrumentos
9. conjunto de entradas/salidas
10. entorno
11. ocurrencia del problema o no-aplicación
12. verificación SD

Una herramienta PUEDE dividir o fusionar etapas por conveniencia UX, pero NO DEBE perder ninguna de estas salidas semánticamente necesarias.

### 6.1 Paso 1: Identificación del Proceso Principal

La forma del nombre depende del idioma de realización:

- En artefactos y modelos en **inglés**, el nombre del proceso DEBE terminar con verbo en forma gerundio (sufijo "-ing"), conforme a [OPM ISO/PAS 19450](urn:fxsl:kb:opm-iso-19450-es).
- En artefactos y modelos en **español**, el nombre del proceso DEBE encabezarse con infinitivo (-ar, -er, -ir) o con una nominalización verbal cuya primera palabra termine en `-ción`, conforme a [OPL-ES](urn:fxsl:kb:opm-opl-es) §1.1. La forma en `-miento` TAMBIÉN PUEDE aceptarse cuando el dominio la exija.

**Correcto:** `Battery Charging`, `Airplane Flying`

**Incorrecto:** `Charge Battery`, `Fly Airplane`

En inglés, el nombre DEBERÍA combinar el transformado seguido del verbo gerundio. En español, DEBERÍA mantener la misma función nominal usando infinitivo o, cuando mejore la naturalidad terminológica del dominio, una forma encabezada por `-ción`.

### 6.2 Paso 2: Grupo Beneficiario

El nombre DEBE ser singular según el Principio del Nombre Singular de OPM:

- En inglés: sufijo "Group" para humanos y "Set" para inanimados
- En español: sufijo "Grupo" para humanos y "Conjunto" para inanimados

El grupo beneficiario DEBE representarse como objeto físico.

### 6.3 Paso 3: Atributo del Beneficiario y Estados

El modelador DEBE definir un atributo informacional del beneficiario con exactamente dos estados:

- **Estado de entrada** (actual/problemático)
- **Estado de salida** (deseado/mejorado)

OPL-ES: `*Proceso Principal* cambia **Atributo del Beneficiario** de **Grupo Beneficiario** de \`entrada\` a \`salida\`.`

### 6.4 Paso 4: Función Principal

El modelador DEBE identificar el transformado principal (objeto proveedor de beneficio). DEBERÍA agregar un atributo proveedor de beneficio cuyo valor cambia de problemático a satisfactorio.

Cuando el proceso transforma múltiples transformados, solo el objeto proveedor de beneficio define la función. Otros transformados (consumidos/producidos) DEBEN modelarse pero NO son parte de la función.

### 6.5 Paso 5: Identificación de Agentes

El término "agente" y el enlace de agente (círculo negro relleno) DEBEN usarse exclusivamente para humanos o grupos humanos. Robots, agentes de software y sistemas IA DEBEN usar enlace de instrumento. Un robot PUEDE describirse como "agente de software embebido" en prosa, pero en el modelo DEBE usar enlace de instrumento.

Cuando el beneficiario es también agente del proceso, el modelador DEBE elegir el enlace según la regla de colisión de roles (§4.4): si el beneficiario es transformado, el enlace de efecto prevalece; la figura humana preserva la identidad humana.

OPL-ES: `**Agente** maneja *Proceso Principal*.`

**Doble rol en procesos distintos:** Un objeto PUEDE ser agente de un proceso y transformado de otro proceso distinto simultáneamente. Ejemplo: Learner es agente de MOOC Learning pero también transformado (Knowledge Level cambia). Esto es distinto de la colisión agente-afectado del §4.4, que aplica al mismo proceso.

### 6.6 Paso 6: Nombre del Sistema y Exhibición

El nombre por defecto DEBERÍA ser el nombre del proceso + "Sistema". El modelador PUEDE usar un nombre aceptado en su lugar.

El proceso principal DEBE modelarse como operación del sistema via exhibición-caracterización.

### 6.7 Paso 7: Identificación de Instrumentos

El modelador DEBE identificar habilitadores no humanos requeridos durante toda la duración del proceso. Cada instrumento DEBE conectarse via enlace de instrumento (círculo blanco vacío).

**Reclasificación por desgaste:** Cuando el desgaste, degradación o amortización de un instrumento es relevante al alcance del sistema, el modelador DEBE reclasificarlo como afectado, agregando un atributo (ej: Amortization Level) que el proceso cambia. Se DEBE modelar un proceso de mantenimiento separado.

**Correcto:** Machine es afectado de Metal Cutting (Amortization Level cambia); Machine Maintaining es proceso separado.

**Incorrecto:** Machine es instrumento de Metal Cutting cuando su desgaste es relevante al sistema (el mantenimiento queda oculto).

### 6.8 Paso 8: Objetos de Entrada/Salida

Cada objeto consumido DEBE conectarse via enlace de consumo. Cada objeto creado DEBE conectarse via enlace de resultado. Si un objeto es afectado (no consumido), DEBE conectarse via par entrada-salida especificando la transición de estados.

### 6.9 Paso 9: Objetos Ambientales

Los objetos ambientales DEBEN representarse con contorno discontinuo. Un mismo objeto PUEDE ser sistémico en un modelo y ambiental en otro.

### 6.10 Paso 10: Ocurrencia del Problema

Para sistemas artificiales y sociales, el modelador DEBE modelar la ocurrencia del problema — imagen espejo del propósito. Se DEBE agregar un proceso ambiental que causa el estado problemático.

Para sistemas naturales, la ocurrencia del problema NO DEBE modelarse.

### 6.11 Verificación del SD

| Verificación | Condición | Severidad |
|--------------|-----------|----------|
| Propósito definido | Beneficiario + atributo + transición de estados | CRÍTICA |
| Función definida | Proceso principal + transformado principal | CRÍTICA |
| Habilitadores presentes | ≥1 agente o instrumento | ALTA |
| Entorno identificado | ≥1 objeto ambiental | MEDIA |
| Ocurrencia del problema (si aplica) | Proceso ambiental causa estado negativo | MEDIA |
| OPL legible | Sentencias OPL correctas | ALTA |
| Nombres conformes | Infinitivo/nominalización + singular + Conjunto/Grupo | ALTA |
| Exhibición | Sistema exhibe proceso como operación | ALTA |
| Agentes = humanos | Ningún instrumento con enlace de agente | ALTA |

## 7 Construcción de SD1 — Refinamiento Nivel 1

SD1 refina el SD exponiendo subprocesos y objetos asociados.

### 7.1 Refinamiento de Proceso Síncrono (Descomposición)

Aplica cuando los subprocesos tienen un orden fijo y predefinido.

**Procedimiento:**

1. Crear nuevo OPD etiquetado SD1
2. Inflar el proceso principal en el centro
3. Agregar subprocesos verticalmente según **Principio de Línea de Tiempo de OPM** (primero arriba, último abajo)
4. Cada subproceso DEBE estar conectado a al menos un transformado
5. Verificar agregación-participación implícita por contención gráfica

**In-diagram vs new-diagram (acercamiento en el mismo diagrama vs en diagrama nuevo):**

| Variante | Descripción | Usar cuando |
|----------|-------------|-------------|
| En el mismo diagrama | El refinable aparece descompuesto en el mismo OPD (no se crea OPD nuevo) | OPD tiene espacio suficiente; pocos subprocesos |
| En diagrama nuevo | Nuevo OPD descendiente; refinable con contorno grueso en ambos OPDs | Caso prevalente; el acercamiento requiere espacio sustancial |

**Identidad semántica de la descomposición:** Cuando un proceso se descompone, sus subprocesos = partes (agregación-participación + ordenabilidad positiva), y los objetos que el proceso exhibe (vía exhibición-caracterización) = atributos del proceso. Objetos que ingresan al contexto por migración de enlaces mantienen su identidad independiente y NO son atributos del proceso. Simétricamente, cuando un objeto se descompone: objetos internos = partes, procesos internos = operaciones del objeto.

**Paralelismo implícito:** Cuando dos o más subprocesos tienen el borde superior de sus elipses a la misma altura, DEBEN interpretarse como ejecutándose en paralelo. El siguiente subproceso inicia cuando el último de los paralelos termina. OPL usa la palabra clave `en paralelo` para expresar concurrencia.

**Correcto:** Subprocesos de arriba hacia abajo; paralelos a la misma altura.

**Incorrecto:** Subprocesos fuera del proceso inflado; paralelos a alturas distintas sin intención de secuencia.

### 7.2 Refinamiento de Proceso Asíncrono (Despliegue)

Aplica cuando los subprocesos son independientes y PUEDEN ocurrir en cualquier orden.

**Cuatro pares de despliegue-plegado** (cada una corresponde a una relación estructural fundamental):

| Relación | Despliegue | Plegado |
|----------|------------|---------|
| Agregación-participación | Exponer partes del todo | Ocultar partes |
| Exhibición-caracterización | Exponer rasgos del exhibidor | Ocultar rasgos |
| Generalización-especialización | Exponer especializaciones del general | Ocultar especializaciones |
| Clasificación-instanciación | Exponer instancias de la clase | Ocultar instancias |

**Despliegue parcial:** Cuando no todos los refinadores se muestran, el símbolo de colección incompleta indica que el despliegue es incompleto.

**Caso de uso del despliegue de proceso:** Sistemas orientados a servicios y de tiempo real con funciones paralelas o auxiliares independientes de la función principal DEBERÍAN usar despliegue en vez de descomposición para refinamiento de proceso.

**Regla de decisión — Agregación vs Generalización:**

| Pregunta | Si → | No → |
|----------|------|------|
| ¿Cada subproceso es una variante/tipo del mismo patrón de transformación? | Generalización-especialización | Agregación-participación |
| ¿El todo necesita todas las partes para funcionar? | Agregación-participación | Generalización-especialización |

**Correcto:** Road Danger Warning → Vehicle Crash Alerting, Pedestrian Crash Alerting, Lane Deviation Alerting (son *tipos* de alerta → generalización).

**Incorrecto:** Usar agregación para tipos/variantes (implica que el todo necesita todas las partes simultáneamente).

### 7.3 Refinamiento de Objetos

Los objetos se refinan vía descomposición (composición espacial/estructural) y despliegue (taxonomías, rasgos, instancias). La descomposición de objetos expone partes y operaciones (§7.1); el despliegue expone refinadores vía las cuatro relaciones estructurales (§7.2). La posición espacial de constituyentes en una descomposición de objeto PUEDE tener significado semántico (disposición física, orden lógico).

**Alcance de objeto interior vs exterior:** Un objeto creado dentro de un proceso descompuesto (objeto interior) existe solo en el alcance de ese proceso y se elimina si el proceso padre se elimina. Un objeto creado a nivel SD (objeto exterior) existe independientemente y es referenciable entre múltiples OPDs. El modelador DEBE decidir el alcance basándose en si la existencia del objeto depende del proceso (interior) o es independiente (exterior). Mover un objeto exterior dentro de un proceso inflado NO lo convierte en interior — el objeto retorna a su alcance original al reposicionarlo (envolvimiento visual, no semántico).

### 7.4 Distribución y Migración de Enlaces

| Tipo de enlace | Contorno exterior | Migración por defecto |
|-------------|---------------|-------------------|
| Enlace de agente | PERMITIDO (distribuye a todos) | — |
| Enlace de instrumento | PERMITIDO (distribuye a todos) | — |
| Enlace de consumo | PROHIBIDO | Migra al primer subproceso; reasignar |
| Enlace de resultado | PROHIBIDO | Migra al primer subproceso; reasignar |
| Enlace de evento sistémico | PROHIBIDO | — |

**Procedimiento de migración de enlaces** (al hacer descomposición):

1. Al dibujar el primer subproceso P1 dentro del proceso descompuesto P, la herramienta DEBE mover automáticamente todos los enlaces procedimentales y de control de P a P1
2. Al agregar subprocesos subsiguientes, el modelador DEBE migrar enlaces transformadores de vuelta a P o al subproceso apropiado
3. Los enlaces habilitadores DEBEN migrarse a los subprocesos específicos donde el habilitador es necesario
4. Los enlaces que aplican a todos los subprocesos DEBEN permanecer en el contorno del proceso padre

**Enlaces de invocación implícitos** (no visibles gráficamente, implícitos por disposición vertical):

| Tipo | Semántica |
|------|-----------|
| Proceso → primer(os) subproceso(s) | Control transferido al subproceso superior al entrar al contexto descompuesto |
| Subproceso → siguiente(s) subproceso(s) | La terminación del origen inicia el siguiente |
| Último subproceso → proceso contenedor | Control retorna al proceso descompuesto tras la terminación del último subproceso |

Cuando dos o más subprocesos tienen sus bordes superiores a la misma altura, inician en paralelo; sincronización: el último en terminar inicia el siguiente.

**Antipatrón — Evento a subproceso no-primero:** El modelador NO DEBERÍA conectar un enlace de evento a un subproceso que no sea el primero (superior) dentro de una descomposición, excepto si ha verificado que todos los subprocesos anteriores pueden omitirse sin dejar precondiciones insatisfechas. Conectar a un subproceso intermedio salta los anteriores, potencialmente dejando el sistema en estado inconsistente.

**Escisión de enlaces transformadores con estado especificado:** Cuando `*P* cambia **A** de \`s1\` a \`s2\`` se descompone en P1 y P2, el modelo queda subespecificado. Resolución:

1. `*P1* cambia **A** de \`s1\`.` (escisión de entrada — saca A de s1)
2. `*P2* cambia **A** a \`s2\`.` (escisión de salida — pone A en s2)

Los enlaces escindidos con modificador de control NO están permitidos (saltear un subproceso de una escisión distorsionaría la semántica del efecto).

### 7.5 Expresión y Supresión de Estados

Los estados DEBERÍAN suprimirse en el SD cuando no están conectados a ningún proceso. Los estados DEBERÍAN expresarse en SD1 donde se conectan a subprocesos.

**Estado indeterminado durante proceso activo:** Mientras un proceso que afecta está activo, el afectado está "en transición" entre estado de entrada y estado de salida. Su estado es indeterminado y NO disponible para uso por otros procesos. Si el proceso se detiene prematuramente, el afectado permanece en estado indeterminado a menos que un manejador de excepciones lo resuelva.

### 7.6 Verificación de SD1

| Check | Condición | Severidad |
|-------|-----------|----------|
| Subprocesos transforman | Cada subproceso ≥ 1 transformado | CRÍTICA |
| Refinamiento correcto | Síncrono → descomposición; asíncrono → despliegue | ALTA |
| Enlaces distribuidos | Consumo/resultado NO en contorno exterior | CRÍTICA |
| Sin event a no-primero | Enlace de eventos solo al primer subproceso (o justificacion explícita) | ALTA |
| Enlaces escindidos resueltos | Ningún enlace de efecto underspecified en descomposición con múltiples subprocesos | ALTA |
| Estados expresados | Estados relevantes visibles y conectados | ALTA |
| Sin redundancia | Sin duplicación innecesaria de hechos del SD | MEDIA |

## 8 Gestión de Complejidad — Niveles 2+

### 8.1 Cuatro Mecanismos de Refinamiento-Abstraccion

| Mecanismo | Refinamiento | Abstraccion | Uso principal |
|-----------|-------------|-------------|---------------|
| Descomposición / Recomposición | Expone contenido interno | Oculta contenido interno | Procesos sincrónicos; objetos con partes espaciales |
| Despliegue / Plegado | Expone refinadores via relación estructural | Oculta refinadores | Procesos asincrónicos; taxonomías; rasgos |
| State Expression / Suppression | Muestra estados | Oculta estados irrelevantes | Simplificacion contextual |
| Creación / Eliminación de Vistas | Ensambla hechos de varios OPDs | Elimina una vista | Vistas transversales |

**Decisión descomposición vs despliegue para procesos sincrónicos:** Descomposición DEBERÍA preferirse porque: (a) requiere menos símbolos, (b) genera OPL más corto, (c) reemplaza event/enlaces de invocación explícitos con invocación implícita del timeline. Despliegue de procesos sincrónicos es semánticamente equivalente pero más verboso.

**Port Plegado [OPCloud]:** Especialización de plegado donde la operación (proceso feature) se desplaza al contorno del exhibitor (objeto). Útil cuando el modelador quiere que los rectángulos de objetos representen disposición físico y tamaños relativos. OPL: keyword "as ports" al final de la sentencia de exhibición. Port plegado también aplica a atributos de procesos.

**Semi-Plegado [OPCloud]:** Tecnica intermedia entre fold completo y unfold completo. Muestra nombres de partes dentro del container del objeto sin crear un OPD hijo. Un indicador numerico ("2 more") senala partes ocultas. El modelador DEBERÍA usar semi-plegado para inspección rapida de estructura sin proliferación de OPDs.

Reglas adicionales:

- Views NO DEBEN editarse; la edicion ocurre en OPDs no-view
- El set completo de estados de un objeto es la union de estados en todos los OPDs

### 8.2 Organización del Árbol OPD y Forest

Convention de etiquetado: SD, SD1, SD1.1, SD1.2, SD2, etc. El **Mapa del Sistema** muestra todos los cosas sin enlaces, sirviendo como índice navegable.

**Regla de integridad del arbol [OPCloud]:** Solo OPDs leaf (hojas terminales) PUEDEN eliminarse. OPDs internos estan protegidos para mantener la integridad del arbol de refinamiento. Intentar eliminar un nodo interno DEBE generar error.

**Mapa del Sistema:** árbol OPD elaborado donde cada nodo es un icono miniaturizado del OPD, con flechas gruesas indicando refinamiento. Esencial para navegación en modelos complejos (>10 OPDs). El modelador DEBERÍA generar el mapa del sistema para cualquier modelo con más de un nivel de detalle.

**OPD Último [Textbook de Dori]:** Representación flat obtenida por flattening recursivo del árbol OPD de abajo hacia arriba. No apta para consumo humano excepto en modelos muy pequenos; util para uso automatizado (gestión de conocimiento, querying).

**Whole System Specification [ISO]** — tres constructos complementarios:

| Constructo | Contenido |
|-----------|-----------|
| OPD model specification | Coleccion de OPDs sucesivos en orden en anchura |
| OPL model specification | Coleccion de paragrafos OPL correspondientes, con sentencias duplicadas eliminadas |
| OPM model specification | Presentacion side-by-side: cada OPD con su párrafo OPL a la derecha |

**Sub-Models para trabajo concurrente [OPCloud]:** Cuando múltiples modeladores trabajan en subsistemas simultáneamente, el modelador DEBERÍA separar subsistemas en sub-models. Las conexiónes entre el modelo principal y los sub-models DEBEN mantenerse mínimas para reducir acoplamiento y conflictos de edicion concurrente.

### 8.3 Creacion de Vistas

Tipos: process tree, object tree, allocation view, simulation-motivated view.

### 8.4 Precedencia de Enlaces durante Recomposición

| B↔P1 \ B↔P2 | Effect | Result | Consumption |
|-------------|--------|--------|-------------|
| **Effect** | Effect | Result | Consumption |
| **Result** | Result | Invalido | Effect |
| **Consumption** | Consumption | Effect | Invalido |

**Orden de precedencia primario:** consumption = result > effect > agent > instrumento.

**Orden completo (12 niveles, de mayor a menor fuerza semántica):**

1. consumption event
2. consumption = result (sin modifier)
3. result > consumption condition
4. consumption condition > effect event
5. effect event > effect (sin modifier)
6. effect > effect condition
7. effect condition > agent event
8. agent event > agent (sin modifier)
9. agent > agent condition
10. agent condition > instrumento event
11. instrumento event > instrumento (sin modifier)
12. instrumento > instrumento condition

**Secondary precedence** (dentro de cada kind): event > non-control > condition. Enlace de eventos llevan semántica del enlace sin modificador + process initiation. Condition modifiers debilitan criterios de satisfacción de precondición. Enlaces con estado especificado tienen precedencia sobre enlaces básicos del mismo tipo.

### 8.5 Práctica Middle-Out y Simplificacion [Textbook de Dori]

Las prácticas de esta subsección provienen del textbook de referencia y de la experiencia pedagógica, no del texto normativo de ISO/PAS 19450.

**Desde el nivel medio**: el modelador comienza por el nivel que mejor entiende y refina/abstrae en ambas direcciones.

**Procedimiento de simplificacion de OPD sobrecargado:**

1. Identificar conjunto TO de cosas a extraer
2. Nombrar un nuevo proceso interino que los contenga
3. Ejecutar in-diagram recomposición (abstracción de enlaces + ocultamiento de contenido)
4. Crear nuevo OPD descendiente con los hechos extraidos
5. Renumerar OPDs hijos afectados

Reduccion neta: procesos_removidos + objetos_removidos + links_removidos - 1 (el proceso interino agregado).

**Depth-first traversal para documentos complejos:** Al modelar estandares, regulaciones o documentos extensos, el modelador DEBERÍA seguir una estrategia en profundidad: profundizar completamente en una seccion/clausula antes de avanzar a la siguiente. Esto contrasta con en anchura y permite descubrir inconsistencias locales más rapidamente.

**Object-process disconnect bridging:** Documentos y estandares frecuentemente separan la descripción de objetos (estructura) de la descripción de procesos (comportamiento) en clausulas independientes sin integración. El modelador DEBE conectar ambas vistas usando OPM, enlazando cada proceso con los objetos que transforma. Esta integración revela gaps y objetos implícitos que el texto omite.

### 8.6 Emergencia como Criterio de Validación Arquitectural [Extensión no-ISO]

El concepto de emergencia proviene de la ingeniería de sistemas general, no de ISO/PAS 19450.

El modelador DEBE verificar que la arquitectura del sistema (structure + behavior) produce al menos una capacidad emergente — una funcionalidad que el sistema completo exhibe pero ninguna parte individual posee. Si no existe emergencia, la colección de partes no constituye un sistema en el sentido MBSE.

### 8.7 Gobernanza del Modelo [OPCloud / Textbook de Dori]

Las capacidades de gobernanza de esta subsección corresponden a funcionalidades de OPCloud y al trabajo post-ISO de Dori. OPPL no forma parte de ISO/PAS 19450:2015 (cfr. término 3.84 del glosario ISO).

**Ontology Enforcement:** Para consistencia terminológica en equipos, el modelador DEBERÍA configurar enforcement de ontología organizacional en tres niveles:

| Nivel | Comportamiento |
|-------|---------------|
| None | Sin restricción terminológica |
| Suggest | Sugiere término estandar; el modelador puede ignorar |
| Enforce | Impide terminos no estandarizados |

**Model Informativeness Grading:** Las sentencias OPPL se clasifican en: Definition, Structural, Procedural, Meta, Unknown. Métricas: nivel informativo, puntaje ponderado, INF average, total OPPL sentences. El modelador DEBERÍA ejecutar grading periódicamente para identificar enlaces de precedencia faltantes y procesos sin entradas/salidas.

**Version Comparison:** El modelador DEBERÍA comparar versiones del modelo para seguimiento de mejoras y detección de regresiónes. El diff entre versiones revela hechos agregados, modificados o eliminados.

**Name Coherency:** Ante nombres duplicados, el modelador DEBE resolver con una de tres opciones: (1) usar existing cosa — crea visual instance (mismo cosa, diferente vista en otro OPD), (2) renombrar con nombre único, (3) descartar. La opcion "close" sin resolver NO DEBERÍA usarse. Visual instances solo PUEDEN crearse entre elementos del mismo tipo (object→object, process→process).

### 8.8 Operaciones de Gestión del Modelo en OPCloud [OPCloud]

Las siguientes capacidades son relevantes para el ciclo de vida del modelo, pero no alteran la semántica OPM:

- **Persistencia:** el modelador DEBERÍA tratar Save/Load como operaciones regulares de punto de control durante sesión. Share expone el modelo a otros usuarios con permisos read o edit.
- **Permisos:** el owner/admin PUEDE compartir con usuarios o grupos completos, pero NO entre organizaciones distintas. Read precede a write. El modelador DEBERÍA verificar permisos antes de colaboración concurrente.
- **Exportacion:** OPL puede exportarse con o sin numeracion. Los OPDs pueden exportarse como imagen o PDF, ya sea para el OPD actual, el arbol completo o solo el SD. Los exports DEBEN tratarse como snapshots publicables, no como SSOT del modelo.
- **Templates:** OPCloud soporta templates Private, Organizational y Global. Insertar un template crea una copia local; las actualizaciones posteriores del template fuente NO se propagan a las inserciones ya hechas.
- **Reubicacion del modelo:** mover modelos via cut/paste conserva auto-save e historial de versiones. El modelador DEBERÍA revisar versiones antes y despues de mover o fusionar trabajo.
- **Búsqueda y navegación asistida:** operaciones como search, bring connected y filtered bring DEBERÍAN usarse para inspección localizada de un subgrafo antes de editar, especialmente en modelos con alta densidad de enlaces.

## 9 Heurísticas de Modelamiento Avanzado [Textbook de Dori / OPCloud]

Las heurísticas de esta sección integran prácticas del textbook de referencia de Dori, experiencia pedagógica y patrones observados en OPCloud. No provienen del texto normativo de ISO/PAS 19450, pero son consistentes con su semántica.

### 9.1 Proceso Persistente → Tagged Structural Link

Cuando un proceso mantiene un objeto en su estado actual sin transformarlo (Supporting, Holding, Maintaining, Keeping, Storing, Containing, Connecting), el modelador DEBERÍA reemplazarlo con un enlace estructural etiquetado.

**Justificación:** Los procesos state-preserving violan la definición fundamental de proceso como "cosa que transforma un objeto". El enlace estructural etiquetado es más compacto y expresa la naturaleza time-invariant de la relación.

**Correcto:** `Foundation supports House.` (enlace estructural etiquetado, una sentencia OPL)

**Incorrecto:** Supporting como proceso explícito con Foundation como instrumento y House como afectado (múltiples enlaces, OPL más complejo, contradice definición de proceso)

**Excepcion:** Si mantener el estado requiere esfuerzo no trivial (ej: helicopter hovering requiere propulsión activa), el modelador DEBE modelar el proceso explícitamente.

### 9.2 Objeto Transiente → Invocation Link

Cuando un proceso crea un objeto que el siguiente proceso consume inmediatamente sin intervencion, el modelador DEBERÍA suprimir el objeto transiente y reemplazar la creation-consumption pair con un enlace de invocación (forma de rayo).

**Correcto:** `Object Detecting invokes Threat Assessing.` (enlace de invocación, Spark suprimido)

**Incorrecto:** Mantener Detection Signal como objeto explícito cuando nunca es observado ni transformado por otro proceso.

### 9.3 Dualidad Estructural

Los patrones §9.1 y §9.2 son duales: enlaces estructurales etiquetados suprimen procesos state-preserving innecesarios; enlaces de invocación suprimen objetos transientes innecesarios. El modelador DEBE aplicar ambos consistentemente.

### 9.4 Cambio de Rol entre Niveles de Detalle

Un objeto PUEDE ser instrumento en un nivel abstracto (ej: SD) y afectado en un nivel detallado (ej: SD1), siempre que el estado inicial y final sean iguales en el nivel abstracto (cambio neto = cero).

**Correcto:** Dishwasher es instrumento de Dish Washing en SD. En SD1: Loading cambia Dishwasher de empty a loaded; Unloading cambia de loaded a empty (neto = sin cambio → instrumento válido en SD).

**Incorrecto:** Declarar un objeto como instrumento en SD cuando su estado neto cambia en SD1 (debe ser afectado en ambos niveles).

### 9.5 Arbol de Decisión de Propiedades de Atributos

Al definir un atributo, el modelador DEBERÍA clasificarlo en cuatro dimensiónes binarias:

| Dimensión | Valores | Criterio |
|-----------|---------|----------|
| Explicitness | explicit (por defecto) / implicit | ¿Es un objeto separado? |
| Mode | qualitative (por defecto) / quantitative | ¿Valores numéricos? |
| Touch | hard (por defecto) / soft | ¿Computable desde otros atributos? |
| Emergence | inherent (por defecto) / emergent | ¿Al menos una parte lo exhibe? |

Atributos soft son derivables → PUEDEN no requerir seguimiento independiente. Atributos emergent existen solo a nivel del todo → definen la arquitectura del sistema.

### 9.6 Homogeneidad de Enlaces

Enlaces estructurales DEBEN ser homogéneos (object↔object o process↔process). Enlaces procedimentales DEBEN ser non-homogeneous (object↔process). Unica excepción: exhibición-caracterización permite las 4 combinaciones de perseverance (object exhibe attribute-object, object exhibe operation-process, process exhibe attribute-object, process exhibe operation-process).

### 9.7 Enlaces Estructurales Etiquetados con Estado Especificado

Cuando un estado de un objeto corresponde o se asocia con otro objeto, el modelador DEBERÍA usar un state-specified enlace estructural etiquetado (conectando el estado al objeto asociado) en vez de crear procesos o objetos intermedios.

### 9.8 Atributos Discriminantes y Caracterización con Estado Especificado

Cuando las especializaciónes se distinguen por un valor de atributo, el modelador DEBERÍA usar un discriminating attribute con state-specified enlaces de caracterización. Esto produce un OPD significativamente más compacto que repetir el atributo para cada especialización.

### 9.9 Alcance de Herencia OPM

Cada especialización DEBE heredar del general: (1) todas las partes (aggregation), (2) todos los rasgos (exhibición), (3) todos los enlaces estructurales etiquetados, (4) todos los enlaces procedimentales. Los estados también se heredan. Una especialización PUEDE sobreescribir estados heredados especificando estados propios.

### 9.10 Relatividad de Instancia e Instancias Visuales vs Lógicas [OPCloud]

"Instance" es relativo al sistema de discurso. Lo que es instancia en un sistema (ej: "Taurus 2015" en comparacion de autos) PUEDE ser clase con especializaciónes en otro sistema (ej: autos individuales con VIN en un concesionario).

**Visual Instance vs Logical Instance:** Una visual instance es el mismo cosa representado en diferentes OPDs (misma identidad, diferente vista). Una lógical instance es una relación clasificación-instanciación (clase → instancia). El modelador NO DEBE confundir ambas. Visual instances solo PUEDEN crearse entre elementos del mismo perseverance (object↔object, process↔process; object→process prohibido).

### 9.11 Clasificación de Essence para Things Mixtos

Cuando un cosa tiene partes físico e informacional, el modelador DEBE clasificarlo como **físico**. La esencia dominante del componente tangible prevalece. Ejemplo: Baggage Transporting system tiene componentes informaticales (location seguimiento) pero se clasifica como físico porque el proceso involucra transporte físico.

### 9.12 Estados Directos vs Atributo + Valores (Simplificacion)

Cuando un objeto tiene un solo atributo relevante, el modelador PUEDE simplificar el modelo asignando los valores del atributo como **estados directos del objeto**, eliminando el atributo intermedio.

**Correcto (simplificado):** `Fetus can be embryo or baby.` (estados directos del objeto)

**Correcto (completo):** `Fetus exhibits Developmental Stage. Developmental Stage of Fetus can be embryo or baby.` (atributo + valores)

**Decisión rule:** Usar la forma simplificada cuando el objeto tiene un solo atributo relevante al alcance del modelo y la legibilidad mejora. Usar la forma completa cuando el objeto tiene múltiples atributos o cuando el nombre del atributo agrega información semántica no obvia.

### 9.13 Generalización como Abstracción del SD

Cuando múltiples objetos específicos del SD1 compartirían el mismo tipo de relación con el proceso principal en el SD, el modelador DEBERÍA crear un objeto general que los englobe y agregar solo ese objeto al SD, manteniendo los específicos en SD1.

**Correcto:** Road Danger Representation (general) en SD; Vehicle-in-Front Representation, Pedestrian-in-Front Representation, Lane Set Representation (específicos) en SD1 conectados via generalización-especialización.

**Incorrecto:** Las tres representaciones específicas en SD (overcrowding del diagrama top-level).

### 9.14 Hacer Explícitos los Objetos Implícitos

Al modelar sistemas a partir de texto (standards, regulaciones, especificaciones), el modelador DEBE identificar y modelar explícitamente los objetos que el texto menciona implícitamente. En documentos process-oriented, los objetos transformados por los procesos frecuentemente no se nombran. El acto de forzar la pregunta "¿qué objeto transforma este proceso?" revela entidades críticas omitidas por el autor del texto.

### 9.15 Detección de Sinónimos/Homónimos mediante Modelamiento Formal

OPM fuerza un mapping 1:1 entre cosas y nombres. El modelador DEBE usar este formalismo para detectar: (a) **sinonimos** — múltiples palabras para el mismo concepto (ej: "propósito" vs "stated propósito" en ISO 15288), y (b) **homonimos** — misma palabra para conceptos distintos (ej: "environment" vs "operational environment"). Cada sinonimo detectado DEBE resolverse eligiendo un término canónico. Cada homonimo DEBE resolverse creando cosas separados con nombres distintos.

### 9.16 Detección de Inconsistencias Texto-Diagrama

El modelamiento OPM de un documento existente produce como subproducto la detección de inconsistencias entre el texto principal y sus diagramas. El modelador DEBERÍA documentar estas inconsistencias como hallazgos de calidad. Ejemplo: en ISO 15288, boxes representan "systems" en un diagrama y "processes" en otro, sin justificacion. El modelo OPM resuelve estas ambiguedades asignando perseverance correcto (object vs process) a cada cosa.

### 9.17 Etiquetado de OPD por Cláusula de Referencia

Al modelar documentos normativos, el modelador DEBERÍA etiquetar los OPDs con las clausulas del documento fuente (ej: `[5.2.2] System`, `[6.1] Acquisition`). Esto permite trazabilidad directa entre el modelo y el texto fuente, facilita revision por pares, y soporta validación de cobertura.

## 10 Control de Flujo Avanzado

### 10.1 Esperar vs Omitir — Enlaces Condicionales vs No Condicionales

| Tipo de enlace | Si el objeto/estado está ausente | Uso |
|-------------|----------------------------------|-----|
| Non-condition (sin `c`) | Proceso ESPERA indefinidamente | Proceso obligatorio — el sistema se detiene |
| Condition (con `c`) | Proceso se SALTA | Proceso opcional — la ejecución avanza |

**Regla de decisión:** Usar enlace de condición cuando el proceso es opcional; usar non-enlace de condición cuando es obligatorio. Error común: usar non-enlace de condición para un recurso que puede no aparecer → deadlock.

### 10.2 Precedencia de Omisión sobre Espera

Cuando el preprocess object set contiene tanto enlaces de condición como non-enlaces de condición, omisión DEBE tener precedencia sobre espera. Si cualquier condition-linked object/estado está ausente, el proceso se salta independientemente de la satisfacción de los non-enlaces de condición.

### 10.3 Semántica de Enlaces de Evento (OR) vs Enlaces de Condición (AND/OR)

- **Multiples enlace de eventos** al mismo proceso: semántica OR (cualquier evento individual basta para trigger)
- **Multiples enlaces de condición** al mismo proceso: semántica AND para ejecución (todos deben cumplirse) pero semántica OR para omisión (falla de cualquiera causa omisión)

### 10.4 Abanicos de Enlaces XOR vs OR

| Fan | Simbolo | Semántica | Uso |
|-----|---------|-----------|-----|
| XOR | Arco dashed simple | Exactamente uno de los paths | Decisiones mutuamente excluyentes |
| OR | Arco dashed doble | Al menos uno de los paths | Concurrencia condicional |

Para fan size f=2: XOR usa "either...or"; para f>2: "exactly one of." OR siempre usa "at least one of."

### 10.5 XOR/OR Combinatorial (m-de-f) [Textbook de Dori]

Para f > 2, el modelador PUEDE generalizar: "exactly m of f" (XOR combinatorial) o "at least m of f" (OR combinatorial), donde m < f. El número m se registra junto al arco en el OPD. Modela escenarios como "2 de 3 key holders deben estar presentes."

### 10.6 NOT mediante Existente/No-Existente [Textbook de Dori]

OPM no tiene símbolo NOT dedicado. Para modelar "proceso P ejecuta solo cuando objeto S está ausente," el modelador DEBERÍA crear estados implícitos `existent` y `non-existent` para S, y conectar `non-existent` a P con enlace de instrumento o condition enlace de instrumento.

### 10.7 Etiquetas de Ruta para Desambiguación de Escenarios

Cuando un proceso tiene múltiples enlaces procedurales entrantes y salientes y se necesita especificar cuál entrada mapea a cuál salida, el modelador DEBE usar path labels. El enlace seguido a la salida es el que tiene el mismo label que el enlace de entrada. Path labels proveen memoria entre entrada y salida y eliminan el requisito AND para preprocess objects: solo objetos con el mismo label deben coexistir.

### 10.8 Patrones de Iteración

**Patrón Set-Member:** Adjuntar dos enlaces procedimentales del mismo tipo a un proceso — uno a un set de n miembros y otro a un miembro — produce iteración automatica n veces.

**Patrón Bucle:** Un enlace de invocación desde el último subproceso hacia el proceso padre descompuesto crea un bucle. Para intervalos entre iteraciones, insertar un proceso Waiting con restricciones de tiempo.

**Patrón Decisión-Node:** Para iteración con condición de terminación, usar un boolean decisión node que evalua despues de cada ciclo; si "No," enlace de invocación loopea; si "Yes," la ejecución avanza al siguiente subproceso.

### 10.9 Semántica Temporal de Enlaces Transformadores

| Tipo | Temporalidad de la transformación |
|------|----------------------------------|
| Consumo | Inmediata al inicio del proceso. El consumido deja de existir tan pronto el proceso se activa. Si el consumido no existe, el proceso espera |
| Resultado | Creación solo al término del proceso. Durante la ejecución, ni consumido (ya consumido) ni resultante (aún no creado) existen |
| Efecto | El afectado sale del estado de entrada al inicio del subproceso que lo afecta; entra al estado de salida al completarse ese subproceso. Entre ambos puntos, el objeto está "en transición" — estado indeterminado |

Esta semántica temporal es crítica para simulación y para entender la disponibilidad de objetos entre subprocesos.

### 10.10 Objetos Booleanos y Ramificación

Un **Boolean object** es un objeto informacional dual-state generado por un proceso de decisión. Sus estados forman un par Boolean (yes/no, true/false, pass/fail, approved/denied, `geq-x`/`lt-x`). Cada estado se conecta via enlaces de condición a procesos alternativos subsiguientes, implementando control if-then-else.

**Generalización:** Cualquier objeto con n estados funciona como un case statement — cada estado PUEDE servir como source de condition o enlace de instrumento para un proceso subsiguiente distinto.

### 10.11 Escenarios y Repertorio de Comportamiento

Un **scenario** (thread of execution) es un path específico a través de la jerarquía de procesos del sistema, trazado siguiendo el estado de cada objeto. En cada branching point (Boolean object, enlaces de condición, XOR fan), exactamente un path se materializa. El conjunto completo de scenarios constituye el **behavioral repertoire** del sistema — la totalidad de comportamientos posibles.

### 10.12 Enlaces Transformadores Condicionales (Taxonomía Completa)

| Enlace | Semántica | OPL-ES |
|--------|-----------|--------|
| Consumo condicional | Si consumido existe, proceso lo consume; si no, se omite | `*Proceso* ocurre si **Objeto** existe, en cuyo caso **Objeto** se consume, de lo contrario *Proceso* se omite.` |
| Efecto condicional | Si afectado existe, proceso lo afecta; si no, se omite | `*Proceso* ocurre si **Objeto** existe, en cuyo caso *Proceso* afecta **Objeto**, de lo contrario *Proceso* se omite.` |
| Agente condicional | Si agente existe, proceso opera con agente; si no, se omite | `**Agente** maneja *Proceso* si **Agente** existe; de lo contrario *Proceso* se omite.` |
| Instrumento condicional | Si instrumento existe, proceso opera; si no, se omite | `*Proceso* ocurre si **Instrumento** existe; de lo contrario *Proceso* se omite.` |

Cada uno de estos TIENE versión con estado especificado (proceso opera si objeto está en estado específico; si no, se omite).

### 10.13 Enlaces Procedimentales con Valor Especificado

| Enlace | Semántica |
|--------|-----------|
| Enlace de establecimiento de valor | Unidirectional; establece valor de atributo independiente del valor previo |
| Value enlace de efecto | Bidirectional; cambia valor de atributo de uno no específicado a otro |
| In-out-specified value enlace de efecto pair | Cambia valor de atributo de entrada value específico a salida value específico |

Estos enlaces aplican a **values** (estados de atributos), no a estados de objetos no-atributo.

### 10.14 Abanicos Probabilísticos

En un XOR diverging fan probabilistico, cada enlace DEBE anotarse con una probabilidad. La suma de todas las probabilidades DEBE ser exactamente 1. Por defecto sin fan: si un proceso crea un objeto con n estados, cada estado tiene probabilidad 1/n.

## 11 Manejo de Errores Temporales

### 11.1 Enlaces de Excepción por Sobretiempo

Cuando un proceso tiene Maximal Duration, el modelador DEBERÍA adjuntar un enlace de excepción por sobretiempo a un proceso de manejo de overtime. Si el proceso excede su tiempo máximo, el manejador de excepciones se activa y resuelve los objetos en transición a estados permisibles.

### 11.2 Enlaces de Excepción por Subtiempo

Cuando un proceso tiene Minimal Duration, el modelador DEBERÍA adjuntar un enlace de excepción por subtiempo. Si el proceso se completa antes del mínimo (o es omitido, duración = 0), el undertime handler se activa.

**Patrón — Undertime como detector de omisión:** Un enlace de excepción por subtiempo en un proceso con duración mínima detecta cuando el proceso no se ejecutó (duración efectiva = 0 < mínimo positivo), activando lógica de recuperación. Esto provee un mecanismo formal para "proceso no ejecutado."

### 11.3 Resolución de Estado Indeterminado

Todo afectado en transición durante un proceso activo permanece en estado indeterminado si el proceso falla. Los manejador de excepcioness (overtime/undertime) DEBEN resolver el objeto a un estado permisible. Sin manejo de excepciones, el objeto queda indefinido y el modelo es incompleto para simulación.

## 12 Modelamiento Cuantitativo y Simulación [Textbook de Dori / OPCloud]

ISO/PAS 19450 define propiedades cuantitativas (tasa, duración, multiplicidad) pero no prescribe flujos de trabajo computacionales ni de simulación específicos. Las secciones §12.4-12.6 y §12.9 son específicas de OPCloud.

### 12.1 Tasa de Transformación

Cuando consumo, creación, o cambio de estado ocurre como flujo continuo o operación multi-unidad en el tiempo, el modelador DEBERÍA asignar una propiedad Transformation Rate al enlace procedimental relevante. Tres especializaciónes: consumption rate, yield rate, effect rate.

### 12.2 Computación con OPM — Claridad de Roles de Operandos

Cuando se modelan operaciones aritméticas no conmutativas (Dividing, Subtracting), el modelador DEBE designar explícitamente los roles de operandos (Dividend vs Divisor, Minuend vs Subtrahend). OPM embebe formulas en nombres de proceso (ej: `Residue Computing (residue=il-u)`) para concisión.

### 12.3 Distribución de Duración para Simulación Estocástica

El modelador PUEDE especificar una Duration Distribution en la propiedad Duration de un proceso, identificando una función de distribución de probabilidad. En runtime, cada instancia del proceso muestrea su duración independientemente. Sin Duration Distribution, todas las instancias ejecutan en exactamente la Expected Duration (irrealista para sistemas reales).

### 12.4 Flujo de Trabajo Computacional en OPCloud [OPCloud]

Cuando se implemente el modelo en OPCloud, el modelador DEBE seguir este patrón de 5 pasos:

1. **Definir objetos** con atributos computacionales (tipo: integer, float, string, character, boolean)
2. **Asignar alias** a cada atributo computacional (ej: "x1", "y1") para uso en formulas
3. **Crear proceso de calculo** — representado con braces `{}` en el OPD, indicando naturaleza computacional
4. **Definir formula** usando los aliases (ej: `slope = (y2-y1)/(x2-x1)`)
5. **Conectar proceso** a objetos via consumption/enlace de efectos para flujo de datos

**Stereotypes en OPCloud:** Templates de parámetros reutilizables para patrones computacionales comunes. La herramienta distingue niveles Global y Organizational. Al remover un stereotype de un cosa, el modelador DEBE elegir entre unlink (conservar componentes) o unlink-and-remove (eliminar componentes agregados).

### 12.5 Validación de Rangos [OPCloud]

El modelador DEBERÍA asignar rangos a atributos computacionales para enforcement durante simulación. Sintaxis: `[inclusive`, `(exclusive`. Multiples rangos: `[1,10][20,30]`. El sistema válida automáticamente que los valores permanezcan en rangos validos.

### 12.6 Flujo de Simulación con Entrada de Usuario [OPCloud]

Para simulación con entrada de usuario en OPCloud, el modelador DEBE seguir estos 6 pasos:

1. Crear usuario como objeto físico
2. Conectar usuario al proceso via **enlace de agente**
3. Marcar proceso para recibir user entrada durante simulación
4. Crear objeto entrada computacional para recibir valores
5. Conectar proceso al objeto entrada via **enlace de efecto** (requerido para actualizar objetos computacionales con valores de usuario)
6. En la computación, usar función **User Entrada** del API predefinido

Sin los pasos 5-6, el objeto entrada no recibira valores durante simulación.

### 12.7 Semántica Operacional en Contextos Descompuestos

Ejecutar un proceso con contexto descompuesto transfiere control recursivamente al subproceso superior del nivel más profundo. El control retorna al proceso descompuesto tras terminación del último subproceso.

**Transformaciones del conjunto de objetos involucrados por instancia:**

| Tipo de transformado | Temporalidad de la transformación |
|---------------------|----------------------------------|
| Consumido | Deja de existir al inicio del subproceso más detallado que lo consume |
| Afectado | Sale del estado de entrada al inicio del subproceso más detallado que lo cambia; entra al estado de salida al completarse ese (o subsiguiente) subproceso |
| Resultante | Creado al completarse el subproceso más detallado que lo genera |

Un objeto con estados en transición: ha dejado su estado de entrada pero aún no ha llegado al estado de salida (duración positiva). Durante este periodo, el objeto es indisponible para otros procesos.

### 12.8 Espacio de Estados Compuesto y Precondiciones Compuestas

El state space de un objeto es el producto cartesiano de los sets de estados de todos sus atributos y partes stateful. El modelador DEBE reconocer que no todos los puntos del state space son factibles; los compound states infeasibles DEBERÍAN identificarse mediante process modeling. Para precondiciones compuestas que abarcan múltiples atributos, el modelador DEBE usar multiple condition clause OPL sentences con clausulas X-OR numeradas conectadas por AND lógico.

### 12.9 Integración Externa e Ingesta de Datos en OPCloud [OPCloud]

Cuando el modelo deja de ser solo conceptual y debe intercambiar datos con entorno externo, el modelador PUEDE usar las siguientes capacidades:

- **MQTT:** adecuado para sensores/actuadores IoT con topicos publish/subscribe. Requiere configurar raw server y MQTT server. El modelador DEBERÍA usarlo para acoplar variables computacionales a telemetria o comandos ligeros.
- **ROS:** adecuado para robots y sistemas con ROS master. El flujo de trabajo mínimo DEBE incluir definición de mensaje, publicacion, suscripcion y manejo del feedback bucle via condiciones/iteración.
- **CSV Import para atributos:** util para carga masiva de instancias y valores de atributos. Restricción: el objeto target NO DEBE ser una instancia conectada via clasificación-instanciación. El modelador DEBERÍA previsualizar el import y decidir si ignora existentes o crea atributos faltantes.

## 13 Modelamiento de Requisitos en OPCloud [OPCloud]

En este corpus, el modelamiento de requirements se trata como una capacidad de OPCloud, no como una extension normativa independiente de OPM. Por lo tanto, las siguientes reglas aplican solo cuando el modelo se implementa en OPCloud.

### 13.1 Operaciones Disponibles

OPCloud permite agregar, remover y visualizar requirements sobre elementos, enlaces o diagramas completos. Las relaciones recuperables en el tutorial son:

- Exhibición
- Characterization
- Aggregation Participation

### 13.2 Convención de Trazabilidad

Cuando se use trazabilidad de requirements en OPCloud, el enlace estructural etiquetado con tag **"satisfies"** DEBERÍA usarse como convención de trazabilidad entre artefacto y requirement.

**Correcto:** `Seat satisfies RQ1 Driver Seat.`

**Incorrecto:** Conectar requirements a artifacts via enlaces procedimentales (los requirements no transforman ni habilitan procesos; la relación es estructural).

### 13.3 Ejemplo Mínimo

Ejemplo recuperable desde el tutorial:

- Door-Peephole: peephole como parte de door
- Restricciones dimensionales: 56-64 inches
- Componentes: lens + sleeves
- Componente opcional: peephole cover
- Función: one-way view for seeing visitors

### 13.4 Analisis de Gaps y Generacion Asistida [OPCloud]

OPCloud ofrece capacidades auxiliares que el modelador PUEDE usar para detectar vacios y acelerar derivación de requirements:

- **Identification of Missing Knowledge:** DEBERÍA usarse como heurística de detección de gaps, no como verdad del modelo. `Pistol` sirve para filtrado rapido; `RGCN`, cuando este disponible, ofrece mayor precisión. El umbral de confianza DEBERÍA ajustarse explícitamente antes de aceptar sugerencias.
- **AI Requirements Generation:** toma OPPL como insumo y genera texto de requirement, verification type, acceptance criteria y model triplets. La salida DEBE revisarse manualmente antes de integrarla al corpus o al modelo.
- **Version comparison:** el modelador DEBERÍA comparar resultados del analisis entre versiones sucesivas para distinguir mejoras reales de ruido introducido por cambios de disposición o renaming.

## 14 Simulación y Ejecución del Modelo [Textbook de Dori / OPCloud]

### 14.1 Recorrido en Profundidad del Árbol OPD para Ejecución

La ejecución animada del modelo OPM sigue un recorrido **en profundidad** del árbol OPD. Los tokens fluyen a lo largo de los links: al llegar a un proceso descompuesto, el control se transfiere recursivamente al subproceso más profundo (superior del nivel más bajo). El control retorna al nivel padre tras completar el último subproceso.

Los tokens se visualizan como valores que se pasan entre objetos y procesos: consumed (eliminado del source), instrumento (read-only, permanece), resultante (creado en destination). Tokens computacionales llevan valores numéricos.

### 14.2 Transición Conceptual → Computacional

El modelador DEBE reconocer el punto en el árbol OPD donde la transición de modelamiento conceptual puro a modelamiento computacional es necesaria. Indicadores:

- Los valores numéricos específicos se vuelven necesarios para decisión de diseno
- Trade-off studies requieren parámetros cuantitativos
- El proceso físico tiene una formula matematica subyacente (ej: V = V0 - (F/m)*t)

En este punto, el modelador DEBE convertir procesos conceptuales a procesos computacionales y usar la realización soportada por la herramienta. En OPCloud, la senal visual recuperable es el uso de `{}` en el OPD.

### 14.3 Simulación Conceptual vs Ejecución Computacional en OPCloud [OPCloud]

El modelador DEBE distinguir entre:

- **Simulación conceptual:** animacion visual del flujo de tokens para validar orden, precondiciones y cobertura del comportamiento
- **Ejecución computacional:** corrida efectiva de formulas, atributos computacionales y actualizacion de valores

Reglas operativas:

- La velocidad de animacion DEBERÍA ajustarse para hacer visibles procesos rapidos o loops
- Si el orden observado no coincide con el esperado, el modelador DEBE revisar altura relativa de subprocesos, enlaces de control y condiciones
- Los tokens computacionales transportan valores; los conceptuales solo evidencian disponibilidad, consumo, creación o cambio de estado

## 15 Invariantes

Los invariantes se verifican operativamente en §16, donde se organizan por nivel con severidad asignada. La columna **Fuente** distingue el origen de cada invariante: **ISO** para reglas directamente trazables a ISO/PAS 19450, **Dori** para reglas del textbook, **OPCloud** para reglas de herramienta, y **Ext** para extensiones de esta metodología.

| Invariante | Enforcement | Fuente |
|-----------|-------------|--------|
| Nombre del proceso principal termina en gerundio (EN) o se encabeza por infinitivo / `-ción` / `-miento` válido (ES) | lint | ISO / OPL-ES |
| Todos los nombres de cosas son singulares | lint | ISO |
| Grupo beneficiario es objeto físico | lint | ISO |
| Atributo del beneficiario es objeto informacional | lint | ISO |
| Exactamente un proceso principal por SD | schema | ISO |
| Enlace de agentes solo conectan a humanos (exclusividad) | manual | ISO |
| Enlace de instrumentos solo conectan a no humanos | manual | ISO |
| Todo habilitador persiste sin cambio neto tras el proceso | manual | ISO |
| Objetos ambientales tienen contorno discontinuo | lint | ISO |
| Sistema exhibe proceso principal via exhibición-caracterización | manual | ISO |
| Consumption/enlace de resultados NO en contorno exterior de proceso descompuesto | lint | ISO |
| Todo subproceso conectado a al menos un transformado | lint | ISO |
| Modelo bimodal: todo OPD tiene párrafo OPL equivalente | schema | ISO |
| Un hecho del modelo aparece en al menos un OPD | schema | ISO |
| Enlaces estructurales son homogéneos (excepción: exhibición-caracterización) | lint | ISO |
| Habilitadores y afectados pertenecen a Pre(P) ∩ Post(P); consumidos solo a Pre(P); resultantes solo a Post(P) | manual | ISO |
| Probabilidades en fan XOR suman exactamente 1 | lint | ISO |
| Subprocesos paralelos tienen borde superior de elipse a la misma altura | manual | ISO |
| Enlaces escindidos control-modified NO están permitidos | lint | Ext |
| Arquitectura del sistema produce al menos una capacidad emergente | manual | Ext |
| Links NO DEBEN cruzar areas ocupadas por cosas | manual | Dori |
| Things NO DEBEN ocultarse mutuamente (excepción: port plegado) | manual | Dori |
| Minimizar número de enlaces y cruces de enlaces en cada OPD | manual | Dori |
| Si se usan requirements en OPCloud, la trazabilidad usa enlaces estructurales y la convención "satisfies" | manual | OPCloud |
| En OPCloud, procesos computacionales se distinguen visualmente con `{}` en el OPD | lint | OPCloud |
| Sinonimos resueltos: un cosa = un nombre canónico | manual | Dori |

## 16 Lista de verificación de Validación

Todos los invariantes de §15 DEBEN verificarse en el nivel aplicable. Esta tabla lista checks operativos adicionales organizados por nivel. La columna **Fuente** usa las mismas claves que §15: **ISO**, **Dori**, **OPCloud**, **Ext**.

| Nivel | Check | Condición | Severidad | Fuente |
|-------|-------|-----------|----------|--------|
| SD | Sistema clasificado | Tipo determinado (artificial/natural/social/socio-técnico) | CRÍTICA | ISO |
| SD | Propósito/resultado definido | Beneficiario + atributo + transición estados | CRÍTICA | ISO |
| SD | Función definida | Proceso principal + transformado principal | CRÍTICA | ISO |
| SD | Habilitadores presentes | ≥1 agente o instrumento | ALTA | ISO |
| SD | Entorno identificado | ≥1 objeto ambiental | MEDIA | ISO |
| SD | Ocurrencia del problema (si aplica) | Proceso ambiental causa estado negativo | MEDIA | ISO |
| SD | Reclasificación de instrumentos | Instrumentos con desgaste relevante reclasificados a afectado | MEDIA | Dori |
| SD1 | Refinamiento correcto | Síncrono → descomposición; asíncrono → despliegue | ALTA | ISO |
| SD1 | Sin evento a no-primero | Enlaces de evento no a subprocesos intermedios (o justificación) | ALTA | Ext |
| SD1 | Enlaces escindidos resueltos | Ningún enlace de efecto underspecified en descomposición multi-subprocess | ALTA | ISO |
| SD1 | Estados expresados | Estados relevantes visibles y conectados | ALTA | ISO |
| SD1 | Tipo asíncrono correcto | Agregación para partes; generalización para tipos | ALTA | ISO |
| SD1 | Sin redundancia | Sin duplicación innecesaria de hechos del SD | MEDIA | Dori |
| SD2+ | Precedencia de enlaces | Recomposición aplica matriz de precedencia | ALTA | ISO |
| SD2+ | Árbol OPD válido | Etiquetado secuencial correcto | MEDIA | ISO |
| SD2+ | Coherencia de cambio de rol | Instrumento en abstract = afectado en detail solo si cambio neto = 0 | ALTA | Dori |
| Quant | Operandos explícitos | Operaciones no conmutativas con roles designados | MEDIA | Dori |
| Quant | Flujo computacional | Atributos computacionales con tipo, alias y formula | MEDIA | OPCloud |
| Quant | Validación de rangos | Rangos definidos para atributos con dominio acotado | MEDIA | OPCloud |
| Error | Manejo de excepciones | Procesos con límites de tiempo tienen enlaces de excepción por sobretiempo/subtiempo | MEDIA | ISO |
| Error | Resolución de estado indeterminado | Afectados en transición resueltos por manejador de excepciones | MEDIA | ISO |
| Global | Claridad | Ningún OPD excede 20-25 entidades | MEDIA | Dori |
| Global | Alcance interior/exterior | Objetos inner solo existen en alcance de su proceso padre | MEDIA | ISO |
| Global | Coherencia de nombres | Sin nombres duplicados no resueltos | ALTA | Dori |
| Global | Enforcement de ontología | Nivel configurado para organización (Suggest o Enforce) | MEDIA | OPCloud |
| Global | Informatividad del modelo | Grading ejecutado; sin enlaces de precedencia faltantes críticos | MEDIA | OPCloud |
| Global | Mapa del sistema | Generado para modelos con >10 OPDs | MEDIA | Dori |
| Global | Constructos de especificación | OPD + OPL + OPM spec completos en orden en anchura | MEDIA | ISO |
| Global | Port plegado | Usado donde disposición física de componentes es relevante | BAJA | OPCloud |
| Global | Objetos implícitos | Objetos implícitos en texto fuente identificados y modelados explícitamente | ALTA | Dori |
| Req | Trazabilidad estructural | Si se usan requirements en OPCloud, se ocupan enlaces estructurales y convención "satisfies" | MEDIA | OPCloud |
