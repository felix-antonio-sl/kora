---
_manifest:
  urn: "urn:kora:kb:md-spec"
  provenance:
    created_by: "FS"
    created_at: "2026-02-26"
    source: "KORA RAG-Native Standards, KORA categorical-foundations 05"
version: "3.0.0"
status: published
tags: [spec, markdown, llm, knowledge, rag, koraficacion, workflow, verificacion, fidelidad, traceability]
lang: es
---

# KORA/MD — Especificacion de Artefactos de Conocimiento v3.0.0

## 1. Definicion

**KORA/MD** es un dialecto restringido de Markdown optimizado exclusivamente para el almacenamiento, la vectorizacion y el consumo por parte de LLMs via RAG.

> **Axioma de diseno:** Si un humano encuentra un artefacto KORA/MD agradable de leer, el artefacto tiene grasa.

### 1.1 Alcance y Audiencia

KORA/MD gobierna **unicamente** artefactos de conocimiento estatico: bases de conocimiento, guias, manuales, leyes, procedimientos.

**Audiencia primaria:** LLMs que consumen estos artefactos via recuperacion aumentada (RAG). **Audiencia secundaria:** Humanos que redactan el conocimiento.

**Limite Duro:** Esta especificacion **NO DEBE** usarse para gobernar agentes, catalogos, esquemas ni configuraciones de ejecucion. Para la arquitectura de agentes, ver [KORA/Agent-Spec](urn:kora:kb:agent-spec-md).

> **Meta-Clausula de Auto-Excepcion:** Este documento (`md-spec.md`) ES un documento prescriptivo. Por consiguiente, su propia redaccion **ESTA GOBERNADA** por el estandar superior [KORA/Spec-MD](urn:kora:kb:spec-md) y **NO DEBE** auto-aplicarse la prohibicion de prosa impuesta en su Capa 2.

**Correcto:** `Usar esta especificacion para una base de conocimiento normativa.`
**Incorrecto:** `Usar esta especificacion para definir configuracion de ejecucion de un servicio.`

---

## 2. Definiciones

La tabla de esta seccion **DEBE** incluir todo termino clave con significado preciso dentro de KORA/MD:

**Correcto:** `El documento usa "RAG" y "URN"; ambos aparecen definidos en esta tabla.`
**Incorrecto:** `El documento usa "ACL" como termino clave y no existe entrada para "ACL".`

| Termino | Definicion |
| --- | --- |
| **Artefacto KORA/MD** | Archivo Markdown unitario gobernado por esta especificacion, estructurado en frontmatter y cuerpo |
| **Documento fuente** | Archivo original escrito para humanos del cual se extrae el conocimiento |
| **Koraficacion** | Proceso de transformar un documento humano a formato KORA/MD. Preserva toda informacion eliminando entropia comunicativa |
| **Telegrafizacion** | Compresion de prosa a su forma canonica minima sin perdida de informacion normativa ni descriptiva |
| **RAG** | Sigla de recuperacion aumentada; patron donde un LLM responde con contexto recuperado |
| **LLM** | Sigla de modelo de lenguaje de gran tamano |
| **Chunk RAG** | Unidad de texto delimitada por un encabezado `##`, independientemente recuperable por un sistema LLM |
| **CLI** | Sigla de interfaz de linea de comandos |
| **SSOT** | Sigla de fuente unica de verdad; principio que dicta que un hecho debe existir en un solo lugar en KORA |
| **Koraficacion transform** | Proceso que preserva toda informacion factual mientras elimina entropia comunicativa. Se aplica como un mapeo unico, no como fases secuenciales |
| **URN** | Identificador unico de recurso con formato `urn:{namespace}:{type}:{id}` |
| **Namespace** | Primer segmento logico del URN; delimita el dominio (`gn`, `tde`, `kora`) |
| **Type (URN)** | Segundo segmento del URN; en artefactos KORA/MD **DEBE** ser `kb` |
| **ID (URN)** | Tercer segmento del URN; identificador terminal en kebab-case |
| **Frontmatter** | Bloque YAML delimitado por `---` al inicio del archivo; contiene metadata de maquina |
| **SemVer** | Esquema de versionamiento semantico `MAJOR.MINOR.PATCH` |
| **ISO 639-1** | Estandar de codigo de idioma de dos letras usado en `lang` |
| **IF/THEN** | Estructura condicional tabular que expresa `Condicion -> Resultado` |
| **Segmento** | Porcion tematicamente coherente de un documento fuente, delimitada para procesamiento independiente (~3-5K tokens) |
| **Verificacion Adversarial** | Evaluacion por un LLM distinto al transformador que identifica omisiones comparando fuente contra output |
| **Verificacion Mecanica** | Conjunto de checks deterministicos (no LLM) que validan fidelidad estructural y numerica |
| **Fidelidad** | Propiedad del output que garantiza que toda informacion del documento fuente esta representada |
| **Normalizacion** | Reorganizacion opcional de la jerarquia de encabezados para optimizar fragmentacion RAG sin perdida de informacion |

---

## 3. Anatomia del Documento

Todo artefacto KORA/MD **DEBE** constar de exactamente **2 capas** ontologicamente separadas:

```
+---------------------------------+
|  CAPA 1: YAML Frontmatter      |  <- Manifiesto (metadata de maquina)
|  (---  ...  ---)                |
+---------------------------------+
|  CAPA 2: Cuerpo de Conocimiento|  <- Informacion pura (encabezados + contenido)
|  (# -> ## -> ### -> contenido)  |
+---------------------------------+
```

**Correcto:** `Archivo con frontmatter YAML inicial + cuerpo Markdown posterior.`
**Incorrecto:** `Archivo con YAML intercalado en medio del cuerpo.`

### 3.1 Capa 1: YAML Frontmatter (Obligatorio)

Esta capa **DEBE** ser el unico bloque YAML del archivo. **DEBE** incluir exactamente los campos del esquema mostrado (sin omitir obligatorios ni agregar extras). Este bloque pertenece al orquestador (indexador, catalogo, CLI); **NO DEBE** considerarse contexto para el LLM consumidor.

```yaml
---
_manifest:
  urn: "urn:{namespace}:{type}:{id}"
  provenance:
    created_by: "{autor}"
    created_at: "{YYYY-MM-DD}"
    source: "{URL o referencia del documento original}"
version: "{semver}"
status: draft|published|deprecated
tags: [{tag_1}, {tag_2}, {tag_3}]
lang: "{codigo ISO 639-1 del contenido}"
---
```

**Reglas del Frontmatter:**

- `_manifest.urn` **DEBE** incluirse. El formato **DEBE** ser tripartito y atemporal: `urn:{namespace}:{type}:{id}`.
- Ninguna version **DEBE** escribirse en el URN. Toda version **DEBE** escribirse exclusivamente en el campo raiz `version`.
- El campo `tags` habilita filtrado en RAG. Cada frontmatter **DEBE** incluir un minimo de 3 tags. Cada tag **DEBE** corresponder a un concepto presente explicitamente en el titulo, en un encabezado `##/###` o en una definicion de §2.
- El campo `lang` **DEBE** declarar el idioma del contenido del cuerpo (ISO 639-1: `es`, `en`, `pt`, etc.).
- El campo `source` **DEBE** trazar el documento humano original del cual se extrajo el conocimiento.
- Todo campo no listado en este esquema **NO DEBE** incluirse. Todo frontmatter **NO DEBE** admitir extensiones arbitrarias.

**Correcto:**

```yaml
_manifest:
  urn: "urn:gn:kb:gestion-ipr"
  provenance:
    created_by: "autor"
    created_at: "2026-02-22"
    source: "manual-ipr-vigente"
version: "1.2.0"
status: published
tags: [inversion, ipr, normativa]
lang: "es"
```

**Incorrecto:**

```yaml
_manifest:
  urn: "urn:gn:kb:gestion-ipr"
version: "1.2.0"
tags: [ipr]
lang: "es"
owner: "equipo-a"
```

### 3.2 Capa 2: Cuerpo de Conocimiento (El Artefacto)

Todo cuerpo de conocimiento **DEBE** organizar la informacion pura mediante la jerarquia estructural nativa de Markdown. Toda prosa **NO DEBE** usarse. Toda transicion narrativa **NO DEBE** usarse. Toda retorica **NO DEBE** usarse. Toda interpretacion semantica **DEBE** derivarse de encabezados, listas, tablas y referencias explicitas.

**Correcto:**
```markdown
## 4. Plazos

Plazo maximo: 60 dias habiles.
```

**Incorrecto:**
```markdown
## 4. Plazos

En esta seccion veremos los plazos mas importantes.
```

---

## 4. Topologia de Direccionamiento (URNs)

### 4.1 Estructura Tripartita

Todo artefacto KORA/MD **DEBE** tener un URN con el formato `urn:{namespace}:{type}:{id}`.

| Componente | Semantica | Ejemplos |
| --- | --- | --- |
| **namespace** | Universo de discurso | `gn`, `tde`, `fxsl`, `kora` |
| **type** | Categoria ontologica (en artefactos KORA/MD **DEBE** ser `kb`) | `kb` |
| **id** | Objeto terminal (kebab-case, semanticamente expresivo) | `gestion-ipr`, `ley-21180`, `protocolo-seguridad` |

**Correcto:** `urn:gn:kb:gestion-ipr`
**Incorrecto:** `urn:gn:kb:019`

### 4.2 Referencias A-Temporales

Toda referencia dentro del cuerpo **NO DEBE** incluir version. Todo URN apunta al concepto, no a una instantanea temporal. Toda version es un atributo mutable que reside exclusivamente en el frontmatter del documento destino.

**Correcto:** `Segun [Guia de Implementacion](urn:tde:kb:sistema-tde-2025)...`
**Incorrecto:** `...[Guia](urn:tde:kb:sistema-tde-2025)`

### 4.3 Tipos de Referencia

Toda referencia en KORA/MD **DEBE** utilizar la siguiente sintaxis estandarizada y **NO DEBE** desviarse:

| Tipo | Sintaxis | Uso |
| --- | --- | --- |
| Interna (mismo documento) | `[-> Nombre del H2 o H3]` | Enlace a otra seccion del mismo artefacto |
| A otro artefacto KORA | `[Descripcion](urn:{ns}:{type}:{id})` | Enlace semantico a otro artefacto |
| Externa | `[Descripcion](https://...)` | Enlace a fuente web externa |

**Correcto:** `Ver [Agent Spec](urn:kora:kb:agent-spec-md) y [-> 5. Gramatica Estructural].`
**Incorrecto:** `Ver protocolo-seguridad y seccion cinco.`

---

## 5. Gramatica Estructural

### 5.1 Jerarquia de Encabezados = Esqueleto Semantico

| Nivel | Rol Semantico | Ejemplo |
| --- | --- | --- |
| `#` | Titulo del artefacto (unico por archivo) | `# Gestion de IPR` |
| `##` | Topico principal / seccion de dominio | `## 1. Fase de Formulacion` |
| `###` | Subtopico / componente | `### 1.1 Requisitos BIP` |
| `####` | Detalle atomico / nodo hoja | `#### Excepciones Ley 19.175` |

**Reglas:**

- Cada encabezado **NO DEBE** exceder la profundidad de nivel 4 (`####`). Mayor profundidad senala necesidad de dividir el artefacto en dos.
- Cada `##` establece un limite duro de Chunk RAG: **DEBE** ser autosuficiente al extraerse de forma aislada (con sujeto, accion, condiciones y alcance explicitos).
- Cada encabezado **DEBE** ser telegrafico: sintagmas nominales, nunca oraciones completas.
- Un `###` **NO DEBE** existir sin estar subordinado a un `##`.

**Correcto:**
```markdown
## 4. Plazos FNDR

Plazo maximo: 60 dias habiles. Base: Res. CGR.
```

**Incorrecto:**
```markdown
## 4. Plazos FNDR

Como se explico antes, se mantiene el mismo plazo.
```

**Correcto:**
```markdown
## 5. Gramatica Estructural
### 5.1 Jerarquia de Encabezados
#### Excepciones de Fragmentacion
```

**Incorrecto:**
```markdown
##### Detalle tecnico
### Esta seccion explica como estructurar encabezados
```

### 5.2 Elementos de Contenido

Cada elemento listado **PUEDE** usarse en KORA/MD conforme a su uso indicado, pero **NO DEBE** emplearse para su funcion prohibida:

| Elemento | Uso Permitido | Funcion Prohibida |
| --- | --- | --- |
| **Negrita** | Definicion de termino clave, primera mencion | Enfasis decorativo |
| *Cursiva* | Termino extranjero, calificador tecnico | Enfasis estilistico |
| `codigo` | Identificadores, URNs, valores literales, comandos | Resaltado general |
| Lista no-ordenada (`-`) | Enumeracion sin orden inherente | Narrativa convertida a vinetas |
| Lista ordenada (`1.`) | Pasos secuenciales, procedimientos | Prioridades sin secuencia real |
| Tabla | Comparacion estructurada, datos matriciales, condiciones IF/THEN | Formato estetico sin valor informativo |
| Blockquote (`>`) | Cita textual literal de fuente normativa donde la literalidad importa (Nota: En Spec-MD su semantica paralela es Axioma) | Enfasis, recuadros editoriales, comentarios editoriales |
| Regla horizontal (`---`) | Separador entre secciones `##` principales | Quiebres decorativos |

### 5.3 Elementos Prohibidos (Grasa)

Cada elemento de la siguiente lista **NO DEBE** incluirse en ningun artefacto KORA/MD:

- Oraciones introductorias ("En este documento veremos...")
- Frases de transicion ("A continuacion", "Por otro lado", "Habiendo visto lo anterior")
- Hedging ("Podria ser que", "En general", "Suele ocurrir", "Probablemente")
- Preguntas retoricas
- Formulas de saludo o cierre
- Informacion repetida (viola SSOT)
- Tags HTML
- Notas al pie (usar referencias URN inline)
- Blockquotes anidados (`>>`)
- Emojis narrativos (solo permitidos como marcadores booleanos en tablas)

### 5.4 Telegrafizacion (Compresion Informativa)

La escritura KORA/MD **DEBE** ser telegrafica: maxima densidad semantica, minima cantidad de palabras. Toda oracion larga **DEBE** ser comprimida a su forma canonica minima.

| Fuente Humana (Grasa) | KORA/MD (Carne) |
| --- | --- |
| "El proceso de formulacion de un proyecto de inversion publica regional consta de las siguientes etapas que deben ser seguidas por el formulador" | **Formulacion IPR** — etapas obligatorias: |
| "Es importante senalar que segun lo establecido en la normativa vigente, especificamente la Ley 19.175" | Segun Ley 19.175: |
| "A continuacion se presenta una tabla que resume las principales diferencias entre los tipos de inversion" | *(tabla directamente, sin preambulo)* |
| "El concepto de rendicion de cuentas se refiere al proceso mediante el cual..." | **Rendicion de cuentas** — proceso de verificacion de... |
| "Cabe destacar que existen diversas excepciones contempladas en la normativa" | Excepciones normativas: |

**Patrones de Telegrafizacion obligatorios:**

- **Definiciones:** `**Termino** — descripcion telegrafica.`
- **Acciones:** `1. Verbo imperativo -> resultado esperado.`
- **Condiciones:** Tabla con columnas `Condicion | Resultado | Base Legal`.
- **Comparaciones:** Tabla matricial, nunca parrafos.

### 5.5 Preservacion de Verdad (Prueba Acida)

La telegrafizacion **NO DEBE** sacrificar contenido informativo. Un artefacto KORA/MD **DEBE** preservar toda la verdad factual de su fuente original.

Traces to: formal/05 §2.2 (Koraficacion Functor K — Faithful property)

> Si al eliminar una palabra cambia el **tono** o la **fluidez** -> **DEBE** eliminarse.
> Si al eliminar una palabra desaparece una **condicion**, un **umbral**, una **excepcion**, una **fecha**, una **cifra** o una **dependencia** -> es perdida de informacion critica y **NO DEBE** eliminarse.

**Correcto:** `Plazo maximo: 60 dias habiles.`
**Incorrecto:** `Plazo maximo: 60 dias.`

---

## 6. Koraficacion

### 6.1 Entrada

Cualquier documento escrito originalmente para lectores humanos **PUEDE** usarse: PDF, Word, HTML, texto plano, wiki, memorandum. Todo documento que ingrese al monorepo para koraficacion **DEBE** transitar por el pipeline de ingesta definido en [Pipeline de Ingesta](urn:kora:kb:pipeline-ingesta): `inbox/` -> `source/` -> `drafts/` -> `knowledge/`.

### 6.2 El Proceso de Koraficacion

La koraficacion es un proceso de transformacion que convierte documentos humanos en artefactos KORA/MD. **NO DEBE** tratarse como un flujo secuencial de fases; es un mapeo unico que aplica simultaneamente:

- La gramatica estructural definida en [-> 5. Gramatica Estructural].
- Los invariantes definidos en [-> 7. Invariantes de KORA/MD].

Traces to: formal/05 §2.2 (Koraficacion Functor K)

**Propiedades del proceso:**

```python
# Koraficacion transform K: DocHumano -> KORA/MD
def koraficate(source: HumanDocument) -> KoraArtifact:
    """
    Transform a human document into a KORA/MD artifact.
    All 6 properties apply simultaneously, not sequentially.
    """
    output = KoraArtifact(lang=source.lang)

    # Property 1: Faithful — every fact in source appears in output
    for fact in source.extract_facts():
        output.include(fact)

    # Property 2: Telegraphic — compress to canonical minimum
    output.telegraphize()  # removes communicative entropy

    # Property 3: Promoter — prose -> structured (never the reverse)
    output.promote_structures()  # prose -> tables, lists, code

    # Property 4: Normalizer — optimize heading hierarchy for RAG
    output.normalize_headings()  # subordinate to fidelity

    # Property 5: Idempotent — K(K(x)) == K(x)
    assert koraficate(output) == output

    # Property 6: Language-invariant — output lang == source lang
    assert output.lang == source.lang

    return output
```

- **Fiel:** Toda relacion de informacion en la fuente **DEBE** tener una representacion en la salida. No se pierden relaciones.
- **Telegrafico:** Toda prosa **DEBE** comprimirse a su forma canonica minima segun los patrones de [-> 5.4 Telegrafizacion].
- **Promotor:** Cada estructura **DEBE** promoverse (prosa -> tabla/lista) pero **NO DEBE** degradarse (tabla -> prosa).
- **Normalizador:** El proceso **DEBE** reorganizar la jerarquia de encabezados para optimizar la fragmentacion RAG. La normalizacion **DEBE** estar subordinada a la fidelidad (toda reorganizacion preserva la informacion).
- **Idioma-invariante:** El idioma de la salida **DEBE** ser identico al de la entrada.
- **Idempotente:** Toda aplicacion recursiva `K(K(x))` **DEBE** resultar en `K(x)`.

La implementacion concreta (un solo paso LLM, multiples pasadas, trabajo manual) es irrelevante para esta especificacion, siempre que el resultado cumpla la validacion. Para una estrategia de ejecucion concreta, ver [-> 6.3 Estrategia de Ejecucion].

**Correcto:**

```markdown
Fuente:
- Requisitos de postulacion y plazos por fondo (en parrafo).

Salida KORA/MD:
- Lista para requisitos.
- Tabla para plazos por fondo.
```

**Incorrecto:**

```markdown
Fuente:
| Fondo | Plazo   |
| ----- | ------- |
| FNDR  | 60 dias |

Salida KORA/MD:
El fondo FNDR tiene un plazo de 60 dias.
```

### 6.3 Estrategia de Ejecucion

La koraficacion como proceso es declarativa (§6.2), pero su ejecucion mediante LLMs requiere una estrategia que mitigue limitaciones probabilisticas. Esta subseccion define el COMO: segmentacion, separacion de concerns y verificacion mecanica.

### 6.4 Evaluacion del Input

Antes de transformar, **DEBE** clasificarse el documento fuente:

| Criterio | Valor | Implicacion |
| --- | --- | --- |
| Largo del documento | <5K tokens | Koraficacion directa (un solo paso) |
| Largo del documento | 5K-15K tokens | Koraficacion segmentada (por secciones naturales) |
| Largo del documento | >15K tokens | Koraficacion segmentada + verificacion adversarial obligatoria |
| Estructura existente | Tiene headings claros | Segmentar por headings del original |
| Estructura existente | Prosa monolitica sin headings | Segmentar por parrafos tematicos (~1-2K tokens/segmento) |
| Contenido numerico | Alto (tablas, cifras, leyes, plazos) | Verificacion mecanica de fidelidad obligatoria |
| Contenido numerico | Bajo (prosa conceptual) | Verificacion mecanica opcional |

### 6.5 Segmentacion

Para documentos >5K tokens:

1. **DEBEN** identificarse los puntos de corte naturales del documento (titulos, capitulos, secciones).
2. Cada segmento **DEBE** ser tematicamente coherente y caber dentro de ~3-5K tokens.
3. Los segmentos **DEBEN** numerarse para trazabilidad: `[Seg-1]`, `[Seg-2]`, ... `[Seg-N]`.

**NO DEBE** cortarse dentro de una tabla, lista o parrafo. El corte **DEBE** realizarse siempre entre secciones.

**Correcto:** `Cortar entre ## Seccion A y ## Seccion B, generando [Seg-1] y [Seg-2] independientes.`
**Incorrecto:** `Cortar una tabla de 20 filas a la mitad para que cada segmento contenga 10 filas.`

### 6.6 Telegrafizacion Fiel (Primer Paso LLM)

Para cada segmento (o el documento completo si es <5K), **DEBE** aplicarse la siguiente instruccion al LLM:

```
Transforma el siguiente documento a formato KORA/MD aplicando estas reglas:
- Telegrafizar: comprimir toda prosa a su forma minima sin perder informacion.
- Preservar: toda cifra, fecha, plazo, excepcion, condicion y referencia legal.
- Preservar idioma: el output debe estar en el mismo idioma del input.
- Preservar estructuras: toda lista conserva todos sus items. Toda tabla conserva todas sus filas y columnas.
- Promover: convertir prosa comparativa/condicional a tablas o listas.
- NO reorganizar la estructura de secciones. Mantener el orden del original.
- Usar headings telegraficos (sintagmas nominales, no oraciones).
- Prohibido: introducciones, transiciones, hedging, saludos, retorica.

Documento fuente:
[contenido del segmento]
```

La instruccion **NO DEBE** modificarse para agregar directivas que contradigan esta especificacion. El output **DEBE** ser un segmento koraficado con estructura fiel al original.

**Correcto:**

```markdown
Instruccion: "Telegrafizar preservando toda cifra y estructura."
Output: tabla con todas las filas del original, texto comprimido.
```

**Incorrecto:**

```markdown
Instruccion: "Resume el documento en 3 parrafos."
Output: parrafos que omiten cifras y colapsan tablas.
```

### 6.7 Ensamblaje

Si el documento fue segmentado:

1. Los segmentos koraficados **DEBEN** concatenarse en orden.
2. **DEBE** agregarse el `#` (H1) como titulo unificado del artefacto.
3. **DEBEN** agregarse separadores `---` entre secciones `##`.

### 6.8 Normalizacion (Segundo Paso LLM — Opcional)

**DEBERIA** aplicarse solo si el documento original tiene redundancia evidente o estructura suboptima.

**Instruccion al LLM:**

```
El siguiente es un artefacto KORA/MD ya telegrafizado. Tu tarea es UNICAMENTE reorganizar la estructura de encabezados para optimizarla:
- Fusionar secciones que tratan el mismo tema.
- Dividir secciones excesivamente largas.
- Eliminar informacion duplicada (conservar la instancia mas completa).
- NO modificar el texto de las celdas, items de lista ni definiciones.
- NO agregar ni eliminar informacion factual.

Artefacto:
[contenido ensamblado]
```

La normalizacion **NO DEBE** agregar ni eliminar informacion factual. El output **DEBE** ser un artefacto normalizado.

### 6.9 Inyeccion de Frontmatter

**DEBE** agregarse el bloque YAML frontmatter al inicio del artefacto:

```yaml
---
_manifest:
  urn: "urn:{namespace}:kb:{id}"
  provenance:
    created_by: "{autor}"
    created_at: "{YYYY-MM-DD}"
    source: "{referencia del documento original}"
version: "1.0.0"
status: draft
tags: [{tag1}, {tag2}, {tag3}]
lang: {codigo ISO 639-1 del contenido}
---
```

El frontmatter **DEBE** cumplir el schema definido en [-> 3.1 Capa 1: YAML Frontmatter].

**Correcto:**

```yaml
version: "1.0.0"
lang: "es"
```

**Incorrecto:**

```yaml
version: 1.0.0
lang: es
owner: "equipo-a"
```

### 6.10 Verificacion Mecanica

Checks deterministicos (no dependen de LLM). Cada check **DEBE** ejecutarse antes de considerar el artefacto como valido:

| Check | Metodo | Criterio de falla |
| --- | --- | --- |
| Conteo de items de lista | `grep -c "^- " source` vs `grep -c "^- " output` | Diferencia > 0 |
| Conteo de filas de tabla | `grep -c "^\|" source` vs `grep -c "^\|" output` | output < source (descontando headers) |
| Cifras preservadas | Extraer `\d+[\.,]?\d*` del source, verificar presencia en output | Cifra ausente |
| Fechas preservadas | Extraer patrones de fecha del source, verificar en output | Fecha ausente |
| Frontmatter valido | Parsear YAML entre `---` delimitadores | Error de parseo |
| URN sin version | Buscar `urn:.*:.*:.*:` (4+ segmentos) en cuerpo | Match encontrado |
| Lang coherente | Campo `lang` vs idioma detectado del contenido | Divergencia |

### 6.11 Verificacion Adversarial

Para documentos >15K tokens o con alto contenido numerico, **DEBE** ejecutarse verificacion adversarial.

**Instruccion al LLM verificador (distinto al transformador):**

```
Compara el documento original con el artefacto KORA/MD generado.
Identifica TODA informacion presente en el original que NO este representada en el output.
Lista cada omision como:
- [LINEA/SECCION del original]: [informacion faltante]

Si no hay omisiones, responde: "FIDELIDAD: COMPLETA"

Original:
[documento fuente]

KORA/MD generado:
[artefacto]
```

Si se detectan omisiones -> **DEBE** volverse a [-> 6.6 Telegrafizacion Fiel] para los segmentos afectados.

### 6.12 Registro en Catalogo

1. **DEBE** ejecutarse `kora index` para registrar el URN en el catalogo.
2. **DEBE** cambiarse `status: draft` a `status: published` una vez verificado.
3. **DEBE** realizarse commit al monorepo.

---

## 7. Invariantes de KORA/MD

### 7.1 Preservacion de Idioma

Todo artefacto KORA/MD resultante **DEBE** estar en el mismo idioma que el documento fuente original. Toda koraficacion transforma la estructura y la densidad, pero **NO DEBE** transformar el idioma.

- Todo documento fuente en espanol -> artefacto KORA/MD resultante **DEBE** estar en espanol.
- Todo documento fuente en ingles -> artefacto KORA/MD resultante **DEBE** estar en ingles.
- Todo campo `lang` del frontmatter **DEBE** reflejar el idioma del contenido original.

**Correcto:**
```yaml
lang: es
# Y el resto del cuerpo Markdown esta integramente en espanol.
```

**Incorrecto:**
```yaml
lang: es
# Y el resto del cuerpo Markdown contiene encabezados en ingles sin justificacion.
```

### 7.2 Independencia de Chunk RAG

Cada seccion `##` **DEBE** sobrevivir a la extraccion aislada por un sistema de *retrieval* y cumplir simultaneamente estos criterios:

- Toda referencia implicita ("como vimos arriba", "como veremos mas adelante") **NO DEBE** usarse.
- Cada acronimo **DEBE** definirse en primera mencion dentro de **cada** `##`, o enlazarse via URN.
- Cada `##` **DEBE** declarar sus propios terminos clave.
- Cada `##` **DEBE** contener al menos una oracion completa con sujeto, accion y condicion/alcance cuando aplique.

**Correcto:**

```markdown
## 4. Plazos FNDR

Plazo maximo de rendicion: 60 dias habiles desde la transferencia.
Base normativa: Res. CGR.
```

**Incorrecto:**

```markdown
## 4. Plazos FNDR

Como vimos arriba, se mantiene el plazo estandar.
```

### 7.3 Preservacion de Verdad (Fidelidad Absoluta)

La koraficacion elimina prosa, pero **NO DEBE** eliminar hechos. Todo contenido tecnico, numerico, legal, temporal o condicional presente en el documento fuente **DEBE** estar representado en el artefacto resultante:

Traces to: formal/05 §2.2 (Koraficacion Functor K — Faithful property)

- Toda cifra, fecha, plazo y umbral del original **DEBE** aparecer en la salida.
- Toda excepcion documentada en el original **DEBE** aparecer en la salida.
- Toda referencia legal o normativa del original **DEBE** aparecer en la salida.

**Correcto:** `FNDR: 60 dias habiles. Sectoriales: 30-90 dias habiles. Base: Res. CGR.`
**Incorrecto:** `Plazos variables segun fondo.`

### 7.4 Preservacion de Estructuras (Listas y Tablas)

Toda lista y tabla presente en el documento fuente es una estructura de informacion de alto valor semantico. Toda transformacion de estas estructuras **DEBE** seguir reglas estrictas:

- Toda lista del original **DEBE** conservar todos sus items en la salida. Ningun item **DEBE** ser omitido ni fusionado con otro.
- Toda tabla del original **DEBE** conservar todas sus filas y columnas. Ninguna fila **DEBE** ser descartada ni colapsada.
- El contenido textual de cada item de lista o celda de tabla **DEBE** telegrafizarse, pero la estructura y la cardinalidad **DEBE** mantenerse intacta.
- Si el documento fuente describe informacion comparativa o matricial en prosa, esta **DEBE** ser promovida a tabla. La direccion de la transformacion **DEBE** ser siempre prosa -> estructura, y **NO DEBE** ser estructura -> prosa.

**Correcto:**

```markdown
Fuente:
- Item A
- Item B

Salida KORA/MD:
- Item A
- Item B
```

**Incorrecto:**

```markdown
Fuente:
- Item A
- Item B

Salida KORA/MD:
- Item A y Item B
```

---

## 8. Validacion

| Check | Criterio | Accion si falla |
| --- | --- | --- |
| Frontmatter valido | Parsea sin error, sin campos prohibidos | Corregir sintaxis, eliminar campos no autorizados |
| URN registrado | `_manifest.urn` existe en catalogo | Registrar via `kora index` |
| URN sin version | Ni en `_manifest.urn` ni en referencias cruzadas del cuerpo | Eliminar sufijo versional |
| Sin grasa | Cero introducciones, transiciones, hedging, retorica | Remover |
| Idioma preservado | `lang` coincide con idioma del documento fuente | Corregir `lang` o revertir traducciones |
| Independencia de Chunk RAG | Cada `##` cumple §7.2: sin anafora, acronimos definidos, oracion completa | Agregar contexto explicito o enlaces URN |
| Sin duplicacion | Cada hecho aparece exactamente una vez | Deduplicar (SSOT) |
| Referencias cruzadas validas | Todo `(urn:...)` resuelve y carece de version | Corregir o remover |
| Fidelidad | Toda cifra, fecha, excepcion y condicion del original presente | Restaurar informacion perdida |
| Estructuras preservadas | Toda lista conserva N items, toda tabla conserva MxK | Restaurar items/filas/columnas perdidas |
| Tags | Minimo 3 tags semanticos en frontmatter | Agregar tags |

---

## 9. Ejemplo de Transformacion

### 9.1 Fuente (Documento Humano, espanol)

```text
La gestion de rendiciones de cuentas en el contexto del Gobierno Regional de Nuble es un proceso fundamental que permite asegurar la correcta utilizacion de los recursos publicos transferidos a las distintas entidades beneficiarias. Este proceso se rige principalmente por las disposiciones de la Contraloria General de la Republica y se ejecuta a traves del Sistema de Rendicion Electronica de Cuentas (SISREC).

Es importante senalar que existen distintos plazos segun el tipo de fondos transferidos. Para los fondos FNDR, el plazo maximo es de 60 dias habiles. Para los fondos sectoriales, el plazo puede variar entre 30 y 90 dias habiles segun lo establecido en el convenio respectivo.
```

### 9.2 Salida KORA/MD

```markdown
---
_manifest:
  urn: "urn:gn:kb:gestion-rendiciones"
  provenance:
    created_by: "FS"
    created_at: "2026-02-22"
    source: "Manual Rendiciones GORE Nuble v3"
version: "2.0.0"
status: published
tags: [rendiciones, sisrec, cgr, plazos, gore-nuble]
lang: es
---

# Gestion de Rendiciones de Cuentas

## Definicion

**Rendicion de cuentas** — proceso de verificacion del uso de recursos publicos transferidos a entidades beneficiarias. Regulado por CGR. Ejecutado via SISREC.

## Plazos por Tipo de Fondo

| Tipo de Fondo | Plazo              | Base Legal     |
| ------------- | ------------------ | -------------- |
| FNDR          | 60 dias habiles    | Res. CGR       |
| Sectoriales   | 30-90 dias habiles | Segun convenio |
```
