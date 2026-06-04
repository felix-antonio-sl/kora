---
_manifest:
  urn: urn:fxsl:kb:manual-opforja-es
  provenance:
    created_by: deep-opm-pro/codex + custodio KORA
    created_at: '2026-06-04'
    source: Manual operativo derivado del corpus OPM/Forja SSOT ES vigente. Parte
      desde reglas-opm-estrictas-es v1.2.1, metodologia-forja-es v1.4.4, spec-forja-opd-es
      v1.0.3, spec-forja-opl-es v1.1.3, opm-categorial-es v1.2.4 y modelamiento-opm
      v1.5.0. Iniciado en REVIEW y promovido a productivo como manual v0.1.0 con
      secciones de estabilidad editorial explícita porque la implementación de opforja/deep-opm-pro
      sigue evolucionando.
version: 0.1.0
status: publicado
source_base: reglas-opm-estrictas-es.md v1.2.1; metodologia-forja-es.md v1.4.4; spec-forja-opd-es.md
  v1.0.3; spec-forja-opl-es.md v1.1.3; opm-categorial-es.md v1.2.4; modelamiento-opm
  v1.5.0.
derived_from:
- urn:fxsl:kb:reglas-opm-estrictas-es
- urn:fxsl:kb:metodologia-forja-opm-es
- urn:fxsl:kb:spec-forja-opd-es
- urn:fxsl:kb:spec-forja-opl-es
- urn:fxsl:kb:opm-categorial-es
scope: Manual operativo de uso de opforja para modeladores, agentes y mantenedores.
  Enseña flujo, criterio, lectura de OPD/OPL, validación y uso práctico sin duplicar
  el canon prescriptivo ni las specs modales. Las secciones dependientes de interfaz
  se tratan como borrador vivo hasta estabilizar la app.
tags:
- opm
- opforja
- manual
- guia-operativa
- modelamiento
- opd
- opl
- deep-opm-pro
- ssot-forja
lang: es
extensions:
  kora:
    family: note
    lifecycle_note: publicado v0.1.0; mantener secciones dependientes de interfaz como vivo o pendiente de evidencia hasta sincronización con la app.
    shard_index: 1
    shard_count: 2
    shard_root_urn: urn:fxsl:kb:manual-opforja-es
relations:
  depends:
  - urn:fxsl:kb:reglas-opm-estrictas-es
  - urn:fxsl:kb:metodologia-forja-opm-es
  - urn:fxsl:kb:spec-forja-opd-es
  - urn:fxsl:kb:spec-forja-opl-es
  cites:
  - urn:fxsl:kb:opm-categorial-es
  - urn:fxsl:kb:opm-es
  - urn:fxsl:kb:opd-es
  - urn:fxsl:kb:opl-es
  - urn:fxsl:kb:manual-metodologico-opm-es
---

# Manual de opforja


Manual operativo para modelar con OPM en opforja/deep-opm-pro.

## Estado editorial

Este manual está publicado como **v0.1.0 operativo** porque el criterio de uso
ya está estabilizado por el corpus Forja. Las partes dependientes de interfaz se
mantienen marcadas como `vivo` o `pendiente de evidencia` mientras opforja siga
cambiando.

| Estado | Significado | Uso en este manual |
| --- | --- | --- |
| `estable` | Deriva de corpus Forja publicado y no depende de chrome ni gestos de UI. | Puede enseñarse como conducta esperada. |
| `vivo` | Depende de implementación opforja vigente o de comportamiento observado en app. | Se redacta como disciplina operativa, no como promesa permanente de UI. |
| `pendiente de evidencia` | Requiere screenshot, fixture, checker, ley o caso end-to-end antes de publicarse. | Se conserva como ranura editorial, no como regla. |

## Contrato del manual

Este manual **enseña a usar opforja**. No reemplaza la autoridad normativa del
corpus. Cuando una decisión sea normativa, debe citar su artefacto propietario:

| Plano | Artefacto propietario | Qué decide |
| --- | --- | --- |
| Validez y severidad | `urn:fxsl:kb:reglas-opm-estrictas-es` | Si un hecho OPD/OPL es válido, condicionado, advertido, no canonizado o prohibido. |
| Método | `urn:fxsl:kb:metodologia-forja-opm-es` | En qué orden modelar, cuándo detenerse, cómo refinar y cómo validar utilidad. |
| OPD | `urn:fxsl:kb:spec-forja-opd-es` | Cómo se realiza visualmente un hecho OPM en opforja. |
| OPL | `urn:fxsl:kb:spec-forja-opl-es` | Cómo se genera, lee, parsea, edita y sincroniza OPL-ES. |
| Formal | `urn:fxsl:kb:opm-categorial-es` | Qué lectura estructural explica equivalencia, composición y refinamiento bajo la superficie. |

Regla editorial: el manual resume criterio y procedimiento; **no copia matrices
de reglas, glifos completos, EBNF ni catálogos exhaustivos**. Si una explicación
necesita ese detalle, remite al artefacto propietario.

## Tabla de contenidos

0. Qué es opforja
1. Modelo mental mínimo
2. Flujo de modelamiento Forja
3. Trabajar en la interfaz opforja
4. Construir un modelo desde cero
5. Refinar sin romper el modelo
6. Reglas prácticas de OPD
7. Reglas prácticas de OPL
8. Validación y diagnóstico
9. Patrones de modelado
10. Ejemplo end-to-end
11. Apéndices

## 0. Qué es opforja

**Estado:** estable para el concepto; vivo para detalles de app.

opforja es la realización de OPM en deep-opm-pro: una mesa de trabajo para
construir, leer, validar y serializar modelos OPM bimodales, con OPD como
superficie visual y OPL-ES como superficie textual.

OPM aporta la ontología mínima: objetos, procesos, estados y enlaces. Forja
añade una disciplina operativa para usar esa ontología en una herramienta viva:
reglas estrictas, método de modelado, realización visual, realización textual,
roundtrip, validación y criterios de corrección.

opforja no es un dibujador genérico. Una figura en el canvas vale solo si porta
un hecho OPM válido y si ese hecho puede expresarse en OPL. Tampoco es un motor
que descubre la verdad del dominio: el operador aporta qué hace el sistema en el
mundo; opforja y sus agentes custodian que esa verdad se exprese con primitivas
OPM correctas.

### 0.1 Audiencia

- Modeladores que necesitan construir un sistema OPM desde cero.
- Agentes que guían, validan o serializan modelos OPM.
- Mantenedores de deep-opm-pro que implementan canvas, OPL, validadores,
 exportadores o simulación.
- Revisores que necesitan distinguir errores de modelo, errores de herramienta
 y deuda documental.

### 0.2 Precedencia de lectura

Para aprender uso práctico, leer este manual. Para decidir una controversia,
leer el artefacto propietario:

1. Validez: `reglas-opm-estrictas-es`.
2. Camino de modelado: `metodologia-forja-es`.
3. Superficie visual: `spec-forja-opd-es`.
4. Superficie textual: `spec-forja-opl-es`.
5. Explicación formal: `opm-categorial-es`.

Las capas base (`opm-es`, `opd-es`, `opl-es`, `manual-metodologico-opm-es`) son
procedencia OPM general. En opforja se consultan bajo la precedencia Forja.

## 1. Modelo mental mínimo

**Estado:** estable.

### 1.1 Función antes que forma

Todo modelo opforja empieza por una pregunta: **qué transformación entrega valor
y para quién**. La forma cuesta; la función entrega valor. Si el modelo empieza
por objetos sin proceso central, todavía no es un modelo OPM útil.

Una función debe ser suficientemente neutral respecto de la solución. "Cruzar el
río" puede realizarse con puente, ferry o túnel; "construir puente" ya escogió
una forma. Mientras haya alternativas vivas, mantener separadas intención,
función y forma.

### 1.2 Objetos, procesos y estados

Un **objeto** existe. Un **proceso** transforma. Un **estado** es una situación
posible de un objeto. La pregunta fundacional es siempre: esto que acabo de
nombrar, ¿existe o sucede?

Los nombres no son cosmética: un objeto debe nombrar una cosa; un proceso debe
nombrar una transformación. Palabras como "gestión", "módulo", "sistema",
"procesar" o "manejar" suelen esconder barro si no dicen qué cambia.

### 1.3 Transformees, agentes e instrumentos

No toda cosa conectada a un proceso cumple el mismo rol:

- **Transformee:** la cosa que el proceso consume, produce, crea, destruye o
 cambia.
- **Agente:** una entidad humana u organizacional que maneja o ejecuta con
 responsabilidad.
- **Instrumento:** una herramienta, sistema, recurso o dispositivo requerido por
 el proceso pero no transformado por él.

Confundir transformee con enabler es un error ontológico, no un detalle visual.
Si el proceso no cambia nada, probablemente no es el proceso central o no se ha
identificado aún el objeto que cambia.

### 1.4 OPD y OPL son dos caras del mismo hecho

Cada hecho modelado debe poder verse en OPD y leerse en OPL. Si el OPL no se lee
como lenguaje natural controlado, el OPD está mal o incompleto. Si una oración
OPL no puede volver a un hecho inequívoco, el texto está fuera del roundtrip.

La bimodalidad no es exportación tardía: es una forma de pensar. El modelador
lee el diagrama en voz alta para detectar ambigüedad, mezcla de roles, nombres
pobres y relaciones tácitas.

### 1.5 Refinamiento

El refinamiento distribuye complejidad sin fragmentar la verdad del modelo:

- **In-zoom:** descompone un proceso en subprocesos internos.
- **Out-zoom:** recompone una descomposición hacia su proceso abstracto.
- **Unfold:** despliega estructura interna de una cosa.
- **Fold:** vuelve a plegar detalle.

Una descomposición válida conserva la firma de frontera del proceso abstracto.
Si agrega o quita roles netos de frontera, ya no realiza la misma función. Si
dos realizaciones hermanas tienen la misma firma de frontera, pueden compararse
como alternativas funcionalmente equivalentes.

### 1.6 Barro ontológico

Barro es cualquier ambigüedad que vuelve caro o falso el siguiente paso:

- nombre pobre,
- proceso sin transformee,
- agente confundido con instrumento,
- esencia física/informacional no declarada,
- frontera de sistema implícita,
- refinamiento sin motivo,
- supuesto disfrazado de hecho.

La conducta correcta no es adivinar. La conducta correcta es detenerse, nombrar
el barro, citar la regla o criterio en juego y hacer una pregunta concreta.

## 2. Flujo de modelamiento Forja

**Estado:** estable.

El flujo Forja organiza el trabajo para que el modelo nazca desde función y no
desde dibujo.

### 2.1 A0: antes de la semilla

Antes del SD, generar alternativas. El modelador debería explorar al menos tres
conceptos de solución cuando la arquitectura no está decidida. Cada concepto
debe declarar su intención, función, forma y supuestos.

La equivalencia funcional se evalúa por firma de frontera: mismos roles netos
sobre entidades de frontera, interior posiblemente distinto.

### 2.2 A1: clasificación del sistema

Clasificar el sistema como artificial, natural, social o sociotécnico. La
clasificación cambia cómo se pregunta por propósito, beneficiario, outcome,
agencia humana y problem occurrence.

### 2.3 A2: construcción del SD

El System Diagram debe fijar, en orden:

1. propósito u outcome,
2. proceso central,
3. beneficiario o affectee,
4. atributo de valor y estados relevantes,
5. transformees,
6. agentes humanos si existen,
7. sistema y frontera,
8. instrumentos,
9. contexto externo,
10. problem occurrence cuando aplique,
11. lectura OPL inicial.

El SD no busca completitud total; busca una semilla honesta y trazable.

### 2.4 A3: primer refinamiento

El primer refinamiento debe responder una pregunta real del modelo. No se
in-zoomea por decoración. Si al abrir el proceso central aparecen cinco o más
subprocesos principales, revisar si la altitud está bien elegida.

### 2.5 A4: gestión de complejidad

La complejidad se distribuye por OPDs conectados, no por vistas desconectadas.
Cada OPD debe ser legible y tener un foco claro. Si una vista se congestiona, se
refina, se pliega o se separa por una frontera justificada.

### 2.6 A5: heurísticas de modelado

Heurísticas Forja de uso frecuente:

- modelar primero el cambio de valor,
- preferir nombres que digan qué transforma o qué es,
- no introducir estados sin atributo,
- no introducir interfaz crítica como nota externa si explica comportamiento,
- conservar intermediarios cuando explican arquitectura,
- registrar supuestos explícitamente.

### 2.7 A6: control de flujo

Eventos, condiciones, excepciones, invocación y autoinvocación existen para
explicar cuándo un proceso ocurre, se omite, se desvía o llama a otro proceso.
No son adornos. Un control mal puesto cambia la semántica del modelo.

### 2.8 A7: requisitos, errores, simulación y cuantitativo

Un requisito inferido no es una norma ni un hecho demostrado. Debe marcarse como
inferencia, hipótesis o requisito declarado. Lo cuantitativo debe conservar
polaridad, unidad, fórmula y procedencia de datos cuando afecte decisiones.

### 2.9 A8: validación tripartita

Validar no es solo pasar checks:

- **Bien formado:** cumple reglas.
- **Representa:** el operador confirma que el modelo dice lo que ocurre.
- **Sirve:** responde al propósito declarado con suficiente profundidad.

Un modelo puede ser conforme pero malo. Ese es el territorio del método.

## 3. Trabajar en la interfaz opforja

**Estado:** vivo.

La interfaz de opforja debe tratarse como mesa de trabajo, no como autoridad
semántica. Si la UI permite una operación que contradice el corpus, manda el
corpus. Si la UI todavía no implementa una capacidad canonizada, el manual debe
registrarlo como brecha de herramienta y no enseñar un atajo falso.

### 3.1 Canvas OPD

El canvas permite componer hechos visuales. Cada forma, enlace, marcador,
estado, sombra, contorno, triángulo o badge debe leerse como portador de
semántica OPM o como UI transitoria claramente separada.

### 3.2 Panel OPL

El panel OPL permite leer el modelo como lenguaje natural controlado. Su uso
principal para el modelador es detectar si el OPD expresa lo que se quiso decir.
Editar OPL solo es seguro cuando la oración pertenece al vocabulario y a las
plantillas que el parser reconoce.

### 3.3 Selección, edición y navegación

La navegación debe preservar identidad: seleccionar una cosa, su OPL o su
aparición en otro OPD no crea cosas nuevas. Si una operación cambia solo la
apariencia local, no debe cambiar el hecho canónico.

### 3.4 Exportación y persistencia

La exportación útil conserva hechos, identidad, OPDs, OPL y trazas suficientes
para rehidratar o auditar el modelo. Una imagen sola sirve para comunicación,
pero no sustituye el bundle canónico.

## 4. Construir un modelo desde cero

**Estado:** estable.

1. Declarar propósito en una oración verbo-objeto.
2. Verificar que la función sea transformadora.
3. Nombrar el proceso central sin elegir arquitectura prematura.
4. Identificar beneficiario o affectee.
5. Declarar qué atributo de valor cambia.
6. Identificar transformees y sus estados relevantes.
7. Añadir agentes e instrumentos solo si cumplen su rol.
8. Declarar esencia y afiliación de cada cosa.
9. Leer el OPL inicial y corregir nombres o roles ambiguos.
10. Cerrar el SD con supuestos explícitos y brechas visibles.

Si cualquiera de esos pasos no puede contestarse, el resultado correcto es una
pregunta de aclaración, no un diagrama plausible.
