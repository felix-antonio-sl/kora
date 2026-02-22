---
_manifest:
  urn: "urn:kora:kb:md-spec"
  provenance:
    created_by: "FS"
    created_at: "2026-02-22"
    source: "KORA RAG-Native Standards"
version: "1.1.4"
status: published
tags: [spec, markdown, llm, knowledge, rag, koraficacion]
lang: es
---

# KORA/MD — Especificación de Artefactos de Conocimiento v1.1.4

## 1. Definición

**KORA/MD** es un dialecto restringido de Markdown optimizado exclusivamente para el almacenamiento, la vectorización y el consumo por parte de LLMs vía RAG.

> **Axioma de diseño:** Si un humano encuentra un artefacto KORA/MD agradable de leer, el artefacto tiene grasa.

### 1.1 Alcance y Audiencia

KORA/MD gobierna **únicamente** artefactos de conocimiento estático: bases de conocimiento, guías, manuales, leyes, procedimientos.

**Audiencia primaria:** LLMs que consumen estos artefactos vía recuperación aumentada (RAG). **Audiencia secundaria:** Humanos que redactan el conocimiento.

**Límite Duro:** Esta especificación **NO DEBE** usarse para gobernar agentes, catálogos, esquemas ni configuraciones de ejecución. Para la arquitectura de agentes, ver [KORA/Agent-Spec](urn:kora:kb:agent-spec-md).

> **Meta-Cláusula de Auto-Excepción:** Este documento (`md-spec.md`) ES un documento prescriptivo. Por consiguiente, su propia redacción **ESTÁ GOBERNADA** por el estándar superior [KORA/Spec-MD](urn:kora:kb:spec-md) y **NO DEBE** auto-aplicarse la prohibición de prosa impuesta en su Capa 2.

**Correcto:** `Usar esta especificación para una base de conocimiento normativa.`
**Incorrecto:** `Usar esta especificación para definir configuración de ejecución de un servicio.`

---

## 2. Definiciones

La tabla de esta sección **DEBE** incluir todo término clave con significado preciso dentro de KORA/MD:

**Correcto:** `El documento usa "RAG" y "URN"; ambos aparecen definidos en esta tabla.`
**Incorrecto:** `El documento usa "ACL" como término clave y no existe entrada para "ACL".`

| Término               | Definición                                                                                              |
| --------------------- | ------------------------------------------------------------------------------------------------------- |
| **Artefacto KORA/MD** | Archivo Markdown unitario gobernado por esta especificación, estructurado en frontmatter y cuerpo       |
| **Documento fuente**  | Archivo original escrito para humanos del cual se extrae el conocimiento                                |
| **Koraficación**      | Transformación de un documento humano a formato KORA/MD mediante el funtor F                            |
| **Telegrafización**   | Compresión de prosa a su forma canónica mínima sin pérdida de información normativa ni descriptiva      |
| **RAG**               | Sigla de recuperación aumentada; patrón donde un LLM responde con contexto recuperado                   |
| **LLM**               | Sigla de modelo de lenguaje de gran tamaño                                                              |
| **Chunk RAG**         | Unidad de texto delimitada por un encabezado `##`, independientemente recuperable por un sistema LLM    |
| **CLI**               | Sigla de interfaz de línea de comandos                                                                  |
| **SSOT**              | Sigla de fuente única de verdad; principio que dicta que un hecho debe existir en un solo lugar en KORA |
| **Funtor F**          | Función teórica que preserva estructura de verdad mientras elimina entropía comunicativa                |
| **URN**               | Identificador único de recurso con formato `urn:{namespace}:{type}:{id}`                                |
| **Namespace**         | Primer segmento lógico del URN; delimita el dominio (`gn`, `tde`, `kora`)                               |
| **Type (URN)**        | Segundo segmento del URN; en artefactos KORA/MD **DEBE** ser `kb`                                       |
| **ID (URN)**          | Tercer segmento del URN; identificador terminal en kebab-case                                           |
| **Frontmatter**       | Bloque YAML delimitado por `---` al inicio del archivo; contiene metadata de máquina                    |
| **SemVer**            | Esquema de versionamiento semántico `MAJOR.MINOR.PATCH`                                                 |
| **ISO 639-1**         | Estándar de código de idioma de dos letras usado en `lang`                                              |
| **IF/THEN**           | Estructura condicional tabular que expresa `Condición -> Resultado`                                     |

---

## 3. Anatomía del Documento

Todo artefacto KORA/MD **DEBE** constar de exactamente **2 capas** ontológicamente separadas:

```
┌─────────────────────────────────┐
│  CAPA 1: YAML Frontmatter      │  ← Manifiesto (metadata de máquina)
│  (---  ...  ---)                │
├─────────────────────────────────┤
│  CAPA 2: Cuerpo de Conocimiento│  ← Información pura (encabezados + contenido)
│  (# → ## → ### → contenido)    │
└─────────────────────────────────┘
```

**Correcto:** `Archivo con frontmatter YAML inicial + cuerpo Markdown posterior.`
**Incorrecto:** `Archivo con YAML intercalado en medio del cuerpo.`

### 3.1 Capa 1: YAML Frontmatter (Obligatorio)

Esta capa **DEBE** ser el único bloque YAML del archivo. **DEBE** incluir exactamente los campos del esquema mostrado (sin omitir obligatorios ni agregar extras). Este bloque pertenece al orquestador (indexador, catálogo, CLI); **NO DEBE** considerarse contexto para el LLM consumidor.

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
lang: "{código ISO 639-1 del contenido}"
---
```

**Reglas del Frontmatter:**

- `_manifest.urn` **DEBE** incluirse. El formato **DEBE** ser tripartito y atemporal: `urn:{namespace}:{type}:{id}`.
- Ninguna versión **DEBE** escribirse en el URN. Toda versión **DEBE** escribirse exclusivamente en el campo raíz `version`.
- El campo `tags` habilita filtrado en RAG. Cada frontmatter **DEBE** incluir un mínimo de 3 tags. Cada tag **DEBE** corresponder a un concepto presente explícitamente en el título, en un encabezado `##/###` o en una definición de §2.
- El campo `lang` **DEBE** declarar el idioma del contenido del cuerpo (ISO 639-1: `es`, `en`, `pt`, etc.).
- El campo `source` **DEBE** trazar el documento humano original del cual se extrajo el conocimiento.
- Todo campo no listado en este esquema **NO DEBE** incluirse. Todo frontmatter **NO DEBE** admitir extensiones arbitrarias.

**Correcto:**

```yaml
_manifest:
  urn: "urn:kora:kb:gestion-ipr"
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
  urn: "urn:kora:kb:gestion-ipr:1.2.0"
version: "1.2.0"
tags: [ipr]
lang: "es"
owner: "equipo-a"
```

### 3.2 Capa 2: Cuerpo de Conocimiento (El Artefacto)

Todo cuerpo de conocimiento **DEBE** organizar la información pura mediante la jerarquía estructural nativa de Markdown. Toda prosa **NO DEBE** usarse. Toda transición narrativa **NO DEBE** usarse. Toda retórica **NO DEBE** usarse. Toda interpretación semántica **DEBE** derivarse de encabezados, listas, tablas y referencias explícitas.

**Correcto:**
```markdown
## 4. Plazos

Plazo máximo: 60 días hábiles.
```

**Incorrecto:**
```markdown
## 4. Plazos

En esta sección veremos los plazos más importantes.
```

---

## 4. Topología de Direccionamiento (URNs)

### 4.1 Estructura Tripartita

Todo artefacto KORA/MD **DEBE** tener un URN con el formato `urn:{namespace}:{type}:{id}`.

| Componente    | Semántica                                                      | Ejemplos                                          |
| ------------- | -------------------------------------------------------------- | ------------------------------------------------- |
| **namespace** | Universo de discurso                                           | `gn`, `tde`, `fxsl`, `kora`                       |
| **type**      | Categoría ontológica (en artefactos KORA/MD **DEBE** ser `kb`) | `kb`                                              |
| **id**        | Objeto terminal (kebab-case, semánticamente expresivo)         | `gestion-ipr`, `ley-21180`, `protocolo-seguridad` |

**Correcto:** `urn:gn:kb:protocolo-seguridad`
**Incorrecto:** `urn:gn:kb:019`

### 4.2 Referencias A-Temporales

Toda referencia dentro del cuerpo **NO DEBE** incluir versión. Todo URN apunta al concepto, no a una instantánea temporal. Toda versión es un atributo mutable que reside exclusivamente en el frontmatter del documento destino.

**Correcto:** `Según [Guía de Implementación](urn:tde:kb:guia-implementacion)...`
**Incorrecto:** `...[Guía](urn:tde:kb:guia-implementacion:1.0.0)`

### 4.3 Tipos de Referencia

Toda referencia en KORA/MD **DEBE** utilizar la siguiente sintaxis estandarizada y **NO DEBE** desviarse:

| Tipo                      | Sintaxis                              | Uso                                       |
| ------------------------- | ------------------------------------- | ----------------------------------------- |
| Interna (mismo documento) | `[→ Nombre del H2 o H3]`              | Enlace a otra sección del mismo artefacto |
| A otro artefacto KORA     | `[Descripción](urn:{ns}:{type}:{id})` | Enlace semántico a otro artefacto         |
| Externa                   | `[Descripción](https://...)`          | Enlace a fuente web externa               |

**Correcto:** `Ver [Protocolo](urn:kora:kb:protocolo-seguridad) y [→ 5. Gramática Estructural].`
**Incorrecto:** `Ver protocolo-seguridad y sección cinco.`

---

## 5. Gramática Estructural

### 5.1 Jerarquía de Encabezados = Esqueleto Semántico

| Nivel  | Rol Semántico                            | Ejemplo                       |
| ------ | ---------------------------------------- | ----------------------------- |
| `#`    | Título del artefacto (único por archivo) | `# Gestión de IPR`            |
| `##`   | Tópico principal / sección de dominio    | `## 1. Fase de Formulación`   |
| `###`  | Subtópico / componente                   | `### 1.1 Requisitos BIP`      |
| `####` | Detalle atómico / nodo hoja              | `#### Excepciones Ley 19.175` |

**Reglas:**

- Cada encabezado **NO DEBE** exceder la profundidad de nivel 4 (`####`). Mayor profundidad señala necesidad de dividir el artefacto en dos.
- Cada `##` establece un límite duro de Chunk RAG: **DEBE** ser autosuficiente al extraerse de forma aislada (con sujeto, acción, condiciones y alcance explícitos).
- Cada encabezado **DEBE** ser telegráfico: sintagmas nominales, nunca oraciones completas.
- Un `###` **NO DEBE** existir sin estar subordinado a un `##`.

**Correcto:**
```markdown
## 4. Plazos FNDR

Plazo máximo: 60 días hábiles. Base: Res. CGR.
```

**Incorrecto:**
```markdown
## 4. Plazos FNDR

Como se explicó antes, se mantiene el mismo plazo.
```

**Correcto:**
```markdown
## 5. Gramática Estructural
### 5.1 Jerarquía de Encabezados
#### Excepciones de Fragmentación
```

**Incorrecto:**
```markdown
##### Detalle técnico
### Esta sección explica cómo estructurar encabezados
```

### 5.2 Elementos de Contenido

Cada elemento listado **PUEDE** usarse en KORA/MD conforme a su uso indicado, pero **NO DEBE** emplearse para su función prohibida:

| Elemento                 | Uso Permitido                                                                                                            | Función Prohibida                                       |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------- |
| **Negrita**              | Definición de término clave, primera mención                                                                             | Énfasis decorativo                                      |
| *Cursiva*                | Término extranjero, calificador técnico                                                                                  | Énfasis estilístico                                     |
| `código`                 | Identificadores, URNs, valores literales, comandos                                                                       | Resaltado general                                       |
| Lista no-ordenada (`-`)  | Enumeración sin orden inherente                                                                                          | Narrativa convertida a viñetas                          |
| Lista ordenada (`1.`)    | Pasos secuenciales, procedimientos                                                                                       | Prioridades sin secuencia real                          |
| Tabla                    | Comparación estructurada, datos matriciales, condiciones IF/THEN                                                         | Formato estético sin valor informativo                  |
| Blockquote (`>`)         | Cita textual literal de fuente normativa donde la literalidad importa (Nota: En Spec-MD su semántica paralela es Axioma) | Énfasis, recuadros editoriales, comentarios editoriales |
| Regla horizontal (`---`) | Separador entre secciones `##` principales                                                                               | Quiebres decorativos                                    |

### 5.3 Elementos Prohibidos (Grasa)

Cada elemento de la siguiente lista **NO DEBE** incluirse en ningún artefacto KORA/MD:

- Oraciones introductorias ("En este documento veremos...")
- Frases de transición ("A continuación", "Por otro lado", "Habiendo visto lo anterior")
- Hedging ("Podría ser que", "En general", "Suele ocurrir", "Probablemente")
- Preguntas retóricas
- Fórmulas de saludo o cierre
- Información repetida (viola SSOT)
- Tags HTML
- Notas al pie (usar referencias URN inline)
- Blockquotes anidados (`>>`)
- Emojis narrativos (solo permitidos como marcadores booleanos en tablas: ✅/❌)

### 5.4 Telegrafización (Compresión Informativa)

La escritura KORA/MD **DEBE** ser telegráfica: máxima densidad semántica, mínima cantidad de palabras. Toda oración larga **DEBE** ser comprimida a su forma canónica mínima.

| Fuente Humana (Grasa)                                                                                                                             | KORA/MD (Carne)                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| "El proceso de formulación de un proyecto de inversión pública regional consta de las siguientes etapas que deben ser seguidas por el formulador" | **Formulación IPR** — etapas obligatorias:               |
| "Es importante señalar que según lo establecido en la normativa vigente, específicamente la Ley 19.175"                                           | Según Ley 19.175:                                        |
| "A continuación se presenta una tabla que resume las principales diferencias entre los tipos de inversión"                                        | *(tabla directamente, sin preámbulo)*                    |
| "El concepto de rendición de cuentas se refiere al proceso mediante el cual..."                                                                   | **Rendición de cuentas** — proceso de verificación de... |
| "Cabe destacar que existen diversas excepciones contempladas en la normativa"                                                                     | Excepciones normativas:                                  |

**Patrones de Telegrafización obligatorios:**

- **Definiciones:** `**Término** — descripción telegráfica.`
- **Acciones:** `1. Verbo imperativo → resultado esperado.`
- **Condiciones:** Tabla con columnas `Condición | Resultado | Base Legal`.
- **Comparaciones:** Tabla matricial, nunca párrafos.

### 5.5 Preservación Isomórfica (Prueba Ácida)

La telegrafización **NO DEBE** sacrificar contenido informativo. Un artefacto KORA/MD **DEBE** ser isomórfico en verdad con su fuente original.

> Si al eliminar una palabra cambia el **tono** o la **fluidez** → **DEBE** eliminarse.
> Si al eliminar una palabra desaparece una **condición**, un **umbral**, una **excepción**, una **fecha**, una **cifra** o una **dependencia** → es pérdida de información crítica y **NO DEBE** eliminarse.

**Correcto:** `Plazo máximo: 60 días hábiles.`
**Incorrecto:** `Plazo máximo: 60 días.`

---

## 6. Koraficación

### 6.1 Entrada

Cualquier documento escrito originalmente para lectores humanos **PUEDE** usarse: PDF, Word, HTML, texto plano, wiki, memorándum.

### 6.2 El Funtor de Transformación

La koraficación es una transformación `F: DocHumano → KORA/MD`. **NO DEBE** tratarse como un flujo secuencial de fases; es un mapeo único que aplica simultáneamente:

- La gramática estructural definida en [→ 5. Gramática Estructural].
- Los invariantes definidos en [→ 7. Invariantes de KORA/MD].

**Propiedades del funtor:**

- **Fiel:** Toda relación de información en la fuente **DEBE** tener una representación en la salida. No se pierden relaciones.
- **Telegráfico:** Toda prosa **DEBE** comprimirse a su forma canónica mínima según los patrones de [→ 5.4 Telegrafización].
- **Promotor:** Cada estructura **DEBE** promoverse (prosa → tabla/lista) pero **NO DEBE** degradarse (tabla → prosa).
- **Normalizador:** El funtor **DEBE** reorganizar la jerarquía de encabezados para optimizar la fragmentación RAG. La normalización **DEBE** estar subordinada a la fidelidad (toda reorganización preserva la información).
- **Idioma-invariante:** El idioma de la salida **DEBE** ser idéntico al de la entrada.
- **Idempotente:** Toda aplicación recursiva `F(F(x))` **DEBE** resultar en `F(x)`.

La implementación concreta (un solo paso LLM, múltiples pasadas, trabajo manual) es irrelevante para esta especificación, siempre que el resultado cumpla la validación.

**Correcto:**

```markdown
Fuente:
- Requisitos de postulación y plazos por fondo (en párrafo).

Salida KORA/MD:
- Lista para requisitos.
- Tabla para plazos por fondo.
```

**Incorrecto:**

```markdown
Fuente:
| Fondo | Plazo   |
| ----- | ------- |
| FNDR  | 60 días |

Salida KORA/MD:
El fondo FNDR tiene un plazo de 60 días.
```

---

## 7. Invariantes de KORA/MD

### 7.1 Preservación de Idioma

Todo artefacto KORA/MD resultante **DEBE** estar en el mismo idioma que el documento fuente original. Toda koraficación transforma la estructura y la densidad, pero **NO DEBE** transformar el idioma.

- Todo documento fuente en español → artefacto KORA/MD resultante **DEBE** estar en español.
- Todo documento fuente en inglés → artefacto KORA/MD resultante **DEBE** estar en inglés.
- Todo campo `lang` del frontmatter **DEBE** reflejar el idioma del contenido original.

**Correcto:**
```yaml
lang: es
# Y el resto del cuerpo Markdown está íntegramente en español.
```

**Incorrecto:**
```yaml
lang: es
# Y el resto del cuerpo Markdown contiene encabezados en inglés sin justificación.
```

### 7.2 Independencia de Chunk RAG

Cada sección `##` **DEBE** sobrevivir a la extracción aislada por un sistema de *retrieval* y cumplir simultáneamente estos criterios:

- Toda referencia implícita ("como vimos arriba", "como veremos más adelante") **NO DEBE** usarse.
- Cada acrónimo **DEBE** definirse en primera mención dentro de **cada** `##`, o enlazarse vía URN.
- Cada `##` **DEBE** declarar sus propios términos clave.
- Cada `##` **DEBE** contener al menos una oración completa con sujeto, acción y condición/alcance cuando aplique.

**Correcto:**

```markdown
## 4. Plazos FNDR

Plazo máximo de rendición: 60 días hábiles desde la transferencia.
Base normativa: Res. CGR.
```

**Incorrecto:**

```markdown
## 4. Plazos FNDR

Como vimos arriba, se mantiene el plazo estándar.
```

### 7.3 Preservación de Verdad (Fidelidad Absoluta)

La koraficación elimina prosa, pero **NO DEBE** eliminar hechos. Todo contenido técnico, numérico, legal, temporal o condicional presente en el documento fuente **DEBE** estar representado en el artefacto resultante:

- Toda cifra, fecha, plazo y umbral del original **DEBE** aparecer en la salida.
- Toda excepción documentada en el original **DEBE** aparecer en la salida.
- Toda referencia legal o normativa del original **DEBE** aparecer en la salida.

**Correcto:** `FNDR: 60 días hábiles. Sectoriales: 30-90 días hábiles. Base: Res. CGR.`
**Incorrecto:** `Plazos variables según fondo.`

### 7.4 Preservación de Estructuras (Listas y Tablas)

Toda lista y tabla presente en el documento fuente es una estructura de información de alto valor semántico. Toda transformación de estas estructuras **DEBE** seguir reglas estrictas:

- Toda lista del original **DEBE** conservar todos sus ítems en la salida. Ningún ítem **DEBE** ser omitido ni fusionado con otro.
- Toda tabla del original **DEBE** conservar todas sus filas y columnas. Ninguna fila **DEBE** ser descartada ni colapsada.
- El contenido textual de cada ítem de lista o celda de tabla **DEBE** telegrafizarse, pero la estructura y la cardinalidad **DEBE** mantenerse intacta.
- Si el documento fuente describe información comparativa o matricial en prosa, esta **DEBE** ser promovida a tabla. La dirección de la transformación **DEBE** ser siempre prosa → estructura, y **NO DEBE** ser estructura → prosa.

**Correcto:**

```markdown
Fuente:
- Ítem A
- Ítem B

Salida KORA/MD:
- Ítem A
- Ítem B
```

**Incorrecto:**

```markdown
Fuente:
- Ítem A
- Ítem B

Salida KORA/MD:
- Ítem A y Ítem B
```

---

## 8. Validación

| Check                        | Criterio                                                                  | Acción si falla                                   |
| ---------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------- |
| Frontmatter válido           | Parsea sin error, sin campos prohibidos                                   | Corregir sintaxis, eliminar campos no autorizados |
| URN registrado               | `_manifest.urn` existe en catálogo                                        | Registrar vía `kora index`                        |
| URN sin versión              | Ni en `_manifest.urn` ni en referencias cruzadas del cuerpo               | Eliminar sufijo versional                         |
| Sin grasa                    | Cero introducciones, transiciones, hedging, retórica                      | Remover                                           |
| Idioma preservado            | `lang` coincide con idioma del documento fuente                           | Corregir `lang` o revertir traducciones           |
| Independencia de Chunk RAG   | Cada `##` cumple §7.2: sin anáfora, acrónimos definidos, oración completa | Agregar contexto explícito o enlaces URN          |
| Sin duplicación              | Cada hecho aparece exactamente una vez                                    | Deduplicar (SSOT)                                 |
| Referencias cruzadas válidas | Todo `(urn:...)` resuelve y carece de versión                             | Corregir o remover                                |
| Fidelidad                    | Toda cifra, fecha, excepción y condición del original presente            | Restaurar información perdida                     |
| Estructuras preservadas      | Toda lista conserva N ítems, toda tabla conserva M×K                      | Restaurar ítems/filas/columnas perdidas           |
| Tags                         | Mínimo 3 tags semánticos en frontmatter                                   | Agregar tags                                      |

---

## 9. Ejemplo de Transformación

### 9.1 Fuente (Documento Humano, español)

```text
La gestión de rendiciones de cuentas en el contexto del Gobierno Regional de Ñuble es un proceso fundamental que permite asegurar la correcta utilización de los recursos públicos transferidos a las distintas entidades beneficiarias. Este proceso se rige principalmente por las disposiciones de la Contraloría General de la República y se ejecuta a través del Sistema de Rendición Electrónica de Cuentas (SISREC).

Es importante señalar que existen distintos plazos según el tipo de fondos transferidos. Para los fondos FNDR, el plazo máximo es de 60 días hábiles. Para los fondos sectoriales, el plazo puede variar entre 30 y 90 días hábiles según lo establecido en el convenio respectivo.
```

### 9.2 Salida KORA/MD

```markdown
---
_manifest:
  urn: "urn:gn:kb:gestion-rendiciones"
  provenance:
    created_by: "FS"
    created_at: "2026-02-22"
    source: "Manual Rendiciones GORE Ñuble v3"
version: 2.0.0
status: published
tags: [rendiciones, sisrec, cgr, plazos, gore-nuble]
lang: es
---

# Gestión de Rendiciones de Cuentas

## Definición

**Rendición de cuentas** — proceso de verificación del uso de recursos públicos transferidos a entidades beneficiarias. Regulado por CGR. Ejecutado vía SISREC.

## Plazos por Tipo de Fondo

| Tipo de Fondo | Plazo              | Base Legal     |
| ------------- | ------------------ | -------------- |
| FNDR          | 60 días hábiles    | Res. CGR       |
| Sectoriales   | 30-90 días hábiles | Según convenio |
```
