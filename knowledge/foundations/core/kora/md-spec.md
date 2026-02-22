---
_manifest:
  urn: "urn:kora:kb:md-spec"
  provenance:
    created_by: "FS"
    created_at: "2026-02-22"
    source: "KORA RAG-Native Standards"
version: 1.0.0
status: published
tags: [spec, markdown, llm, knowledge, rag, koraficacion]
lang: es
---

# KORA/MD — Especificación de Artefactos de Conocimiento v1.0

## 1. Definición

**KORA/MD** es un dialecto restringido de Markdown optimizado exclusivamente para el almacenamiento, la vectorización y el consumo por parte de LLMs vía RAG.

**Axioma de diseño**: Si un humano encuentra un artefacto KORA/MD agradable de leer, probablemente tiene demasiada grasa.

### 1.1 Alcance y Audiencia

KORA/MD gobierna **únicamente** artefactos de conocimiento estático: bases de conocimiento, guías, manuales, leyes, procedimientos.

**Audiencia primaria:** LLMs que consumen estos artefactos vía Retrieval-Augmented Generation (RAG). **Audiencia secundaria:** Humanos que redactan el conocimiento.

**Límite Duro:** Esta especificación **NO DEBE** usarse para gobernar agentes, catálogos, schemas ni configuraciones de runtime.

---

## 2. Definiciones

Los siguientes términos tienen significado preciso dentro de KORA/MD:

| Término               | Definición                                                                                                |
| --------------------- | --------------------------------------------------------------------------------------------------------- |
| **Artefacto KORA/MD** | Archivo Markdown unitario gobernado por esta especificación, estructurado en frontmatter y cuerpo         |
| **Documento fuente**  | Archivo original escrito para humanos del cual se extrae el conocimiento                                  |
| **Koraficación**      | Transformación de un documento humano a formato KORA/MD mediante el funtor F                              |
| **Telegrafización**   | Compresión de prosa a su forma canónica mínima sin pérdida de información normativa ni descriptiva        |
| **Chunk RAG**         | Unidad de texto delimitada por un encabezado `##`, independientemente recuperable por un sistema LLM      |
| **SSOT**              | Single Source of Truth; principio que dicta que un hecho debe existir en un solo lugar dentro de KORA     |
| **Funtor F**          | Función matemática teórica que preserva la estructura de verdad mientras elimina la entropía comunicativa |

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

### Capa 1: YAML Frontmatter (Obligatorio)

Esta capa **DEBE** ser el único bloque YAML del archivo. **DEBE** contener la mínima metadata viable para indexación y trazabilidad. Este bloque pertenece al orquestador (indexador, catálogo, CLI); **NO DEBE** considerarse contexto para el LLM consumidor.

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
- La versión **NO DEBE** escribirse en el URN. **DEBE** escribirse exclusivamente en el campo raíz `version`.
- `tags` habilita filtrado en RAG. **DEBEN** incluirse un mínimo de 3 tags semánticamente relevantes al dominio.
- `lang` **DEBE** declarar el idioma del contenido del cuerpo (ISO 639-1: `es`, `en`, `pt`, etc.).
- `source` **DEBE** trazar el documento humano original del cual se extrajo el conocimiento.
- Todo campo no listado en este esquema **NO DEBE** incluirse. El frontmatter **NO DEBE** admitir extensiones arbitrarias.

### Capa 2: Cuerpo de Conocimiento (El Artefacto)

El cuerpo de conocimiento **DEBE** organizar la información pura mediante la jerarquía estructural nativa de Markdown. La prosa **NO DEBE** usarse. Las transiciones **NO DEBEN** usarse. La retórica **NO DEBE** usarse. El LLM infiere la semántica directamente de la estructura del documento.

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
**Incorrecto:** `urn:gn:kb:019` (el ID numérico no aporta semántica al motor de retrieval)

### 4.2 Referencias A-Temporales

Las referencias dentro del cuerpo **NO DEBEN** incluir versión. El URN apunta al concepto, no a un snapshot temporal. La versión es un atributo mutable que reside exclusivamente en el frontmatter del documento destino.

**Correcto:** `Según [Guía de Implementación](urn:tde:kb:guia-implementacion)...`
**Incorrecto:** `...[Guía](urn:tde:kb:guia-implementacion:1.0.0)`

### 4.3 Tipos de Referencia

Las referencias en KORA/MD **DEBEN** utilizar la siguiente sintaxis estandarizada y **NO DEBEN** desviarse:

| Tipo                      | Sintaxis                              | Uso                                       |
| ------------------------- | ------------------------------------- | ----------------------------------------- |
| Interna (mismo documento) | `[→ Nombre del H2 o H3]`              | Enlace a otra sección del mismo artefacto |
| A otro artefacto KORA     | `[Descripción](urn:{ns}:{type}:{id})` | Enlace semántico a otro artefacto         |
| Externa                   | `[Descripción](https://...)`          | Enlace a fuente web externa               |

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

- Los encabezados **NO DEBEN** exceder la profundidad de nivel 4 (`####`). Mayor profundidad señala necesidad de dividir el artefacto en dos.
- Cada `##` establece un límite duro de chunk RAG: **DEBE** ser independientemente recuperable y comprensible sin contexto de los otros `##`.
- Los encabezados **DEBEN** ser telegráficos: sintagmas nominales, nunca oraciones completas.
- Un `###` **NO DEBE** existir sin estar subordinado a un `##`.

### 5.2 Elementos de Contenido

Los siguientes elementos **PUEDEN** usarse en KORA/MD conforme a su uso indicado, pero **NO DEBEN** emplearse para su función prohibida:

| Elemento                 | Uso Permitido                                                                 | Función Prohibida                          |
| ------------------------ | ----------------------------------------------------------------------------- | ------------------------------------------ |
| **Negrita**              | Definición de término clave, primera mención                                  | Énfasis decorativo                         |
| *Cursiva*                | Término extranjero, calificador técnico                                       | Énfasis estilístico                        |
| `código`                 | Identificadores, URNs, valores literales, comandos                            | Resaltado general                          |
| Lista no-ordenada (`-`)  | Enumeración sin orden inherente                                               | Narrativa convertida a viñetas             |
| Lista ordenada (`1.`)    | Pasos secuenciales, procedimientos                                            | Prioridades sin secuencia real             |
| Tabla                    | Comparación estructurada, datos matriciales, condiciones IF/THEN              | Formato estético sin valor informativo     |
| Blockquote (`>`)         | Cita textual literal de fuente normativa o legal donde la literalidad importa | Énfasis, callouts, comentarios editoriales |
| Regla horizontal (`---`) | Separador entre secciones `##` principales                                    | Quiebres decorativos                       |

### 5.3 Elementos Prohibidos (Grasa)

Los siguientes elementos **NO DEBEN** incluirse en ningún artefacto KORA/MD:

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

---

## 6. Koraficación

### 6.1 Input

Cualquier documento escrito originalmente para lectores humanos **PUEDE** usarse: PDF, Word, HTML, texto plano, wiki, memorándum.

### 6.2 El Funtor de Transformación

La koraficación es una transformación `F: DocHumano → KORA/MD`. **NO DEBE** tratarse como un pipeline secuencial de fases — es un mapping único que aplica simultáneamente:

- La gramática estructural definida en [→ 5. Gramática Estructural].
- Los invariantes definidos en [→ 7. Invariantes de KORA/MD].

**Propiedades del funtor:**

- **Fiel:** Toda relación de información en la fuente **DEBE** tener una representación en el output. No se pierden relaciones.
- **Telegráfico:** Toda prosa **DEBE** comprimirse a su forma canónica mínima según los patrones de [→ 5.4 Telegrafización].
- **Promotor:** Las estructuras **DEBEN** promoverse (prosa → tabla/lista) pero **NO DEBEN** degradarse (tabla → prosa).
- **Normalizador:** El funtor **DEBE** reorganizar la jerarquía de encabezados para optimizar el chunking RAG. La normalización **DEBE** estar subordinada a la fidelidad (toda reorganización preserva la información).
- **Idioma-invariante:** El idioma del output **DEBE** ser idéntico al del input.
- **Idempotente:** `F(F(x)) = F(x)`.

La implementación concreta (un solo paso LLM, múltiples pasadas, trabajo manual) es irrelevante para esta especificación, siempre que el resultado cumpla la validación.

---

## 7. Invariantes de KORA/MD

### 7.1 Preservación de Idioma

El idioma del artefacto KORA/MD resultante **DEBE** ser idéntico al idioma del documento fuente original. La koraficación transforma la estructura y la densidad, pero **NO DEBE** transformar el idioma.

- Documento fuente en español → artefacto KORA/MD **DEBE** estar en español.
- Documento fuente en inglés → artefacto KORA/MD **DEBE** estar en inglés.
- El campo `lang` del frontmatter **DEBE** reflejar el idioma del contenido original.

### 7.2 Independencia de Chunk

Cada sección `##` **DEBE** sobrevivir a la extracción aislada por un sistema RAG y seguir siendo 100% inteligible:

- Las referencias implícitas ("como vimos arriba", "como veremos más adelante") **NO DEBEN** usarse.
- Los acrónimos **DEBEN** definirse en primera mención dentro de **cada** `##`, o enlazarse vía URN.
- Cada `##` **DEBE** declarar sus propios términos clave.

### 7.3 Preservación de Verdad (Fidelidad Absoluta)

La koraficación elimina prosa, pero **NO DEBE** eliminar hechos. Todo contenido técnico, numérico, legal, temporal o condicional presente en el documento fuente **DEBE** estar representado en el artefacto resultante:

- Toda cifra, fecha, plazo y umbral del original **DEBE** aparecer en el output.
- Toda excepción documentada en el original **DEBE** aparecer en el output.
- Toda referencia legal o normativa del original **DEBE** aparecer en el output.

### 7.4 Preservación de Estructuras (Listas y Tablas)

Las listas y tablas presentes en el documento fuente son estructuras de información de alto valor semántico. Su transformación **DEBE** seguir reglas estrictas:

- Toda lista del original **DEBE** conservar todos sus ítems en el output. Ningún ítem **DEBE** ser omitido, fusionado con otro ni resumido superficialmente.
- Toda tabla del original **DEBE** conservar todas sus filas y columnas. Ninguna fila **DEBE** ser descartada ni colapsada.
- El contenido textual de cada ítem de lista o celda de tabla **DEBE** telegrafizarse, pero la estructura y la cardinalidad **DEBEN** mantenerse intactas.
- Si el documento fuente describe información comparativa o matricial en prosa, esta **DEBE** ser promovida a tabla. La dirección de la transformación **DEBE** ser siempre prosa → estructura, y **NO DEBE** ser estructura → prosa.

---

## 8. Validación

| Check                   | Criterio                                                       | Acción si falla                                   |
| ----------------------- | -------------------------------------------------------------- | ------------------------------------------------- |
| Frontmatter válido      | Parsea sin error, sin campos prohibidos                        | Corregir sintaxis, eliminar campos no autorizados |
| URN registrado          | `_manifest.urn` existe en catálogo                             | Registrar vía `kora index`                        |
| URN sin versión         | Ni en `_manifest.urn` ni en cross-refs del cuerpo              | Eliminar sufijo versional                         |
| Sin grasa               | Cero introducciones, transiciones, hedging, retórica           | Remover                                           |
| Idioma preservado       | `lang` coincide con idioma del documento fuente                | Corregir `lang` o revertir traducciones           |
| Independencia de chunk  | Cada `##` recuperable y comprensible aislado                   | Agregar contexto faltante o enlaces `[→]`         |
| Sin duplicación         | Cada hecho aparece exactamente una vez                         | Deduplicar (SSOT)                                 |
| Cross-refs válidos      | Todo `(urn:...)` resuelve y carece de versión                  | Corregir o remover                                |
| Fidelidad               | Toda cifra, fecha, excepción y condición del original presente | Restaurar información perdida                     |
| Estructuras preservadas | Toda lista conserva N ítems, toda tabla conserva M×K           | Restaurar ítems/filas/columnas perdidas           |
| Tags                    | Mínimo 3 tags semánticos en frontmatter                        | Agregar tags                                      |

---

## 9. Ejemplo de Transformación

### Fuente (Documento Humano, español)

> La gestión de rendiciones de cuentas en el contexto del Gobierno Regional de Ñuble es un proceso fundamental que permite asegurar la correcta utilización de los recursos públicos transferidos a las distintas entidades beneficiarias. Este proceso se rige principalmente por las disposiciones de la Contraloría General de la República y se ejecuta a través del Sistema de Rendición Electrónica de Cuentas (SISREC).
>
> Es importante señalar que existen distintos plazos según el tipo de fondos transferidos. Para los fondos FNDR, el plazo máximo es de 60 días hábiles. Para los fondos sectoriales, el plazo puede variar entre 30 y 90 días hábiles según lo establecido en el convenio respectivo.

### Output KORA/MD

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

