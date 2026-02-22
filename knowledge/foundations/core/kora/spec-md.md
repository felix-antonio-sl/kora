---
_manifest:
  urn: "urn:kora:kb:spec-md"
  provenance:
    created_by: "FS"
    created_at: "2026-02-22"
    source: "RFC 2119, Diátaxis Framework, KORA/MD"
version: "2.1.0"
status: published
tags: [spec, prescriptivo, formato, instrucciones, workflow]
lang: es
---

# KORA/Spec-MD — Especificación para Documentos Prescriptivos v2.1.0

## 1. Definición

**KORA/Spec-MD** es el formato para documentos prescriptivos dentro del ecosistema KORA: especificaciones, workflows, protocolos de agente, guías operativas y estándares.

KORA/MD gobierna conocimiento descriptivo (hechos). KORA/Spec-MD gobierna conocimiento prescriptivo (reglas).

| Eje                 | KORA/MD                                  | KORA/Spec-MD                                    |
| ------------------- | ---------------------------------------- | ----------------------------------------------- |
| Función             | Describir lo que ES                      | Definir lo que debe ser                         |
| Contenido           | Hechos, datos, procedimientos existentes | Reglas, formatos, restricciones, obligaciones   |
| Prosa               | Prohibida (telegráfico puro)             | Permitida cuando explica el porqué de una regla |
| Estructura          | Headings como `Chunk RAG`                | Headings como jerarquía normativa               |
| Validación          | Fidelidad al documento fuente            | Consistencia interna y ausencia de ambigüedad   |
| Consumidor primario | RAG / *Retrieval*                        | LLM en *Context Window* (*Skill*, *System Prompt*) |

### 1.1 Alcance y Audiencia

**Audiencia primaria:** LLMs que reciben documentos KORA/Spec-MD como skills o instrucciones de sistema. **Audiencia secundaria:** Humanos que diseñan, escriben o revisan especificaciones KORA.

Para optimizar su interpretación por la audiencia primaria, todo documento prescriptivo dentro de KORA **DEBE** redactarse conforme a esta especificación. Un documento KORA/Spec-MD **NO DEBE** utilizarse para registrar conocimiento descriptivo (ver [KORA/MD](urn:kora:kb:md-spec)).

**Correcto:** `Redactar un "Protocolo de Seguridad" usando el formato KORA/Spec-MD`
**Incorrecto:** `Usar KORA/Spec-MD para el "Historial de Incidentes" (es descriptivo, DEBE usar KORA/MD)`

En estándares fundacionales de formatos descriptivos, un documento **PUEDE** incluir una cláusula de auto-excepción para su propia redacción. Toda cláusula de auto-excepción **DEBE** referenciar explícitamente KORA/Spec-MD y delimitar de forma acotada qué regla local queda exceptuada.

**Correcto:** `Declarar una auto-excepción limitada a la prohibición de prosa e indicar referencia explícita a KORA/Spec-MD.`
**Incorrecto:** `Declarar una auto-excepción global sin alcance ni referencia normativa.`

### 1.2 Funtor de Cristalización

KORA/MD define un funtor de compresión `F: DocHumano → KORA/MD` que elimina grasa y preserva verdad. KORA/Spec-MD define un funtor de cristalización:

`G: {Decisiones ∪ Prácticas ∪ Restricciones} → KORA/Spec-MD`

El input no es un documento único sino un conjunto heterogéneo: decisiones de diseño (explícitas o tácitas), prácticas existentes (convenciones informales), y restricciones (técnicas, organizacionales, legales).

**Propiedades del funtor G:**

- **Cristalizador:** El funtor **DEBE** convertir decisiones implícitas y prácticas observadas en reglas explícitas con keywords RFC 2119.
- **Formalizador:** Cada convención informal **DEBE** materializarse como una regla con exactamente una lectura posible.
- **Desambiguador:** Donde la entrada admite múltiples interpretaciones, la salida **DEBE** forzar exactamente una.
- **Ejemplificador:** Toda regla con complejidad semántica o riesgo de ambigüedad **DEBE** acompañarse del par `Correcto:` / `Incorrecto:` para anclar la interpretación.

**Correcto:**
```markdown
- **Cristalizador:** (propiedad descrita con lenguaje normativo DEBE).
- **Ejemplificador:** ... (propiedad acompañada de este mismo bloque de Correcto/Incorrecto para evitar ambigüedad).
```

**Incorrecto:**
```markdown
- Cristalizador: Intenta escribir reglas claras cuando puedas.
```

---

## 2. Definiciones

La tabla de esta sección **DEBE** incluir todo término clave con significado preciso dentro de este documento:

**Correcto:** `El documento usa "RFC 2119" y "URN"; ambos aparecen definidos en esta tabla.`
**Incorrecto:** `El documento usa "ACL" como término clave y no existe entrada para "ACL".`

| Término                    | Definición                                                                                                                                                                |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Artefacto**              | Archivo Markdown unitario con frontmatter KORA y cuerpo de contenido                                                                                                      |
| **Documento prescriptivo** | Artefacto que establece cómo deben comportarse el sistema, los usuarios o los documentos (lo que debe ser)                                                                |
| **Documento descriptivo**  | Artefacto que registra hechos, datos o procedimientos existentes (lo que ES)                                                                                              |
| **Hedging**                | Lenguaje evasivo, condicional o probabilístico ("probablemente", "suele", "en general") que diluye o relativiza una obligación normativa.                                 |
| **Regla**                  | Unidad atómica de control: una oración con keyword RFC 2119 que impone una obligación, prohibición o permiso, opcionalmente acompañada de par `Correcto:` / `Incorrecto:` |
| **Chunk RAG**              | Unidad de texto independientemente recuperable por un sistema de retrieval                                                                                                |
| **Funtor**                 | Transformación que mapea objetos y relaciones de un dominio a otro preservando estructura                                                                                 |
| **Keyword RFC 2119**       | Palabra con significado normativo estandarizado (`DEBE`, `DEBERÍA`, `PUEDE` y sus negaciones)                                                                             |
| **SemVer**                 | Esquema de versionamiento semántico `MAJOR.MINOR.PATCH` usado para reflejar impacto de cambios normativos                                                                 |
| **Patch/Minor/Major**      | Tipos de incremento SemVer: Patch corrige erratas sin cambio normativo, Minor agrega reglas compatibles, Major introduce rupturas                                         |
| **ISO 639-1**              | Estándar de código de idioma de dos letras usado en el campo `lang`                                                                                                       |
| **ISO 8601 (fecha)**       | Estándar de fecha absoluta en formato `YYYY-MM-DD`                                                                                                                        |
| **URN**                    | Identificador único de recurso con formato `urn:{namespace}:{type}:{id}`                                                                                                  |
| **Namespace**              | Primer segmento lógico de un URN; delimita el dominio al que pertenece el recurso                                                                                         |
| **Frontmatter**            | Bloque YAML delimitado por `---` al inicio del archivo, contiene metadata de máquina                                                                                      |
| **Cuerpo Prescriptivo**    | Segunda capa del documento: contenido Markdown con reglas, definiciones y prosa normativa, separado del frontmatter                                                       |
| **Cláusula de auto-excepción** | Regla explícita y acotada que exceptúa una norma local del propio documento, con referencia a su estándar rector                                                   |
| **Cristalización**         | Proceso de convertir decisiones implícitas, prácticas informales y restricciones en reglas explícitas con keywords RFC 2119                                               |
| **Prosa explicativa**      | Texto dentro de un documento KORA/Spec-MD que cumple una función normativa: racionalizar, desambiguar, clarificar o contextualizar reglas                                 |
| **Fenced code block**      | Bloque Markdown delimitado por triple backtick; su contenido se trata como literal y no participa en validaciones de headings                                             |
| **Context Window**         | Ventana de contexto activa de un LLM donde se inyectan instrucciones, definiciones y evidencia relevante                                                                   |
| **Workflow**               | Secuencia prescriptiva de pasos operativos ejecutables por un agente humano o LLM                                                                                         |
| **Skill**                  | Habilidad o herramienta empaquetada que un LLM puede invocar en su *Context Window*                                                                                       |
| **System Prompt**          | Instrucción base fundacional inyectada a un LLM (Agente) antes de interactuar con el usuario                                                                              |
| **Retrieval**              | Mecanismo de búsqueda semántica para inyectar fragmentos de conocimiento en contextos de LLMs                                                                             |
| **Input / Output**         | Datos de entrada y salida, respectivamente, para una evaluación, función, agente o funtor                                                                                 |
| **Snapshot**               | Estado congelado de un objeto, abstracción o conocimiento en una versión específica temporal                                                                              |
| **Filler**                 | Texto de relleno carente de valor informativo o normativo (grasa comunicativa)                                                                                            |

---

## 3. Anatomía del Documento

Todo documento KORA/Spec-MD **DEBE** constar de exactamente **2 capas**:

```
┌─────────────────────────────────┐
│  CAPA 1: YAML Frontmatter      │  ← Manifiesto (metadata de máquina)
│  (---  ...  ---)                │
├─────────────────────────────────┤
│  CAPA 2: Cuerpo Prescriptivo   │  ← Reglas, definiciones, explicaciones
│  (# → ## → ### → contenido)    │
└─────────────────────────────────┘
```

**Correcto:** `Apertura de archivo con --- seguido del YAML de manifiesto`
**Incorrecto:** `Apertura de archivo con # Título seguido del YAML más abajo`

### 3.1 Capa 1: YAML Frontmatter

La Capa 1 **DEBE** ser un bloque YAML delimitado por `---` que precede a todo otro contenido, y **DEBE** cumplir estrictamente el siguiente esquema:

```yaml
---
_manifest:
  urn: "urn:{namespace}:{type}:{id}"
  provenance:
    created_by: "{autor}"
    created_at: "{YYYY-MM-DD}"
    source: "{referencias}"
version: "{semver}"
status: draft|published|deprecated
tags: [{tag_1}, {tag_2}, {tag_3}]
lang: "{ISO 639-1}"
---
```

### 3.2 Capa 2: Cuerpo Prescriptivo

El cuerpo prescriptivo **DEBE** estructurar su contenido en jerarquía de encabezados [→ 5. Gramática Estructural] y **NO DEBE** contener prosa que no cumpla una función normativa explícita [→ 5.4 Prosa Explicativa].

---

## 4. Lenguaje de Obligación

Todo documento KORA/Spec-MD **DEBE** adoptar las keywords de RFC 2119/8174 para expresar niveles de obligatoriedad. Cada keyword **DEBE** escribirse siempre en **negrita** para señalar su uso normativo:

| Keyword                     | Significado                                                   |
| --------------------------- | ------------------------------------------------------------- |
| **DEBE** (MUST)             | Requisito absoluto. No implementarlo viola la especificación. |
| **NO DEBE** (MUST NOT)      | Prohibición absoluta.                                         |
| **DEBERÍA** (SHOULD)        | Recomendado. Puede omitirse si hay razón documentada.         |
| **NO DEBERÍA** (SHOULD NOT) | Desaconsejado. Puede hacerse si hay razón documentada.        |
| **PUEDE** (MAY)             | Opcional. La implementación decide.                           |

**Reglas de uso:**
- Toda keyword **DEBE** usarse solo cuando la oración expresa una obligación, prohibición o permiso. **NO DEBE** usarse con valor normativo en oraciones puramente descriptivas o explicativas.
- La mención metalingüística de keywords RFC 2119 en definiciones, tablas de referencia o ejemplos didácticos **PUEDE** realizarse sin valor normativo; en esos casos **DEBERÍA** representarse en código inline (por ejemplo, `DEBE`) para evitar ambigüedad.
- En documentos en español, se **DEBE** usar la versión castellana. Cada equivalencia inglesa **PUEDE** incluirse entre paréntesis solo en la primera mención de su keyword y **NO DEBE** repetirse en menciones posteriores.
- En documentos en inglés, se **DEBE** usar la keyword RFC 2119 correspondiente en MAYÚSCULAS.

**Correcto:** `Primera mención: **DEBE** (equivalencia inglesa). Menciones posteriores: **DEBE** sin equivalencia inglesa.`
**Incorrecto:** `Incluir equivalencia inglesa en todas las apariciones de la misma keyword en un documento en español.`

---

## 5. Gramática Estructural

### 5.1 Jerarquía de Encabezados

| Nivel  | Rol en Spec                       | Ejemplo                                   |
| ------ | --------------------------------- | ----------------------------------------- |
| `#`    | Título del estándar               | `# KORA/Spec-MD — Especificación v2.0`    |
| `##`   | Sección normativa principal       | `## 4. Lenguaje de Obligación`            |
| `###`  | Subsección / componente de regla  | `### 5.1 Jerarquía de Encabezados`        |
| `####` | Detalle, caso especial, excepción | `#### Excepciones para prosa explicativa` |

**Reglas:**
- Cada encabezado **NO DEBE** exceder la profundidad de nivel 4 (`####`).
- Cada sección `##` **DEBE** estar numerada secuencialmente (`## 1.`, `## 2.`, ...) para referencias inequívocas dentro y fuera del documento. Todo heading dentro de fenced code blocks **NO DEBE** considerarse para esta validación.
- Cada encabezado **DEBE** ser descriptivo del contenido normativo, no genérico ("Otros", "Misceláneos").

**Correcto:** `## 4. Lenguaje de Obligación`
**Incorrecto:** `## Cosas Importantes`

**Correcto:** `#### Excepción para repositorios heredados`
**Incorrecto:** `##### Excepción para repositorios heredados`

**Correcto:** `## 1. Definición`, `## 2. Definiciones`, `## 3. Anatomía del Documento`
**Incorrecto:** `## 1. Definición`, `## 3. Anatomía del Documento` (salta `## 2.`)

### 5.2 Elementos de Contenido

Cada elemento de la siguiente tabla **PUEDE** incluirse en KORA/Spec-MD conforme a su uso permitido, pero **NO DEBE** emplearse para su función prohibida:

| Elemento                       | Uso Permitido en Specs                                            | Función Prohibida               |
| ------------------------------ | ----------------------------------------------------------------- | ------------------------------- |
| Prosa explicativa              | Contextualizar una regla, explicar el porqué, prevenir ambigüedad | Narración, transiciones, filler |
| Keywords RFC 2119 (en negrita) | Expresar niveles de obligación                                    | Énfasis genérico                |
| Blockquote (`>`)               | Principio o axioma fundamental del estándar                       | Citas de fuentes externas       |
| Bloque de código               | Ejemplos normativos, templates, formatos válidos                  | Decoración                      |

### 5.3 Elementos Prohibidos

Cada elemento de la siguiente lista **NO DEBE** incluirse en documentos KORA/Spec-MD:

- Hedging ("probablemente", "en general", "suele")
- Ambigüedad pronominal ("esto", "eso", "lo anterior" sin referente explícito)
- Frases de cortesía o trato informal
- Múltiples interpretaciones posibles de una regla (toda regla **DEBE** tener exactamente una lectura)
- Reglas sin ejemplo (toda regla con complejidad semántica o riesgo de ambigüedad **DEBE** incluir el par `Correcto:` / `Incorrecto:`)
- Secciones sin contenido normativo (si no prescribe ni define, no pertenece)

**Correcto:** `"El URN **DEBE** estar en minúsculas."`
**Incorrecto:** `"En general, sugerimos que el URN esté en minúsculas para evitar problemas."`

### 5.4 Prosa Explicativa

El cuerpo prescriptivo **PUEDE** incluir prosa explicativa únicamente si dicha prosa cumple al menos una de las siguientes funciones normativas:

1. **Explicar el porqué** de una regla (racionalización).
2. **Prevenir una interpretación errónea** (desambiguación).
3. **Clarificar un término** ya definido en [→ 2. Definiciones] cuando el contexto local requiere elaboración. Toda definición canónica **DEBE** residir en §2; la prosa inline solo contextualiza, no reemplaza.
4. **Contextualizar una restricción** que sin contexto parecería arbitraria.

Toda prosa **NO DEBE**:
- Introducir una sección ("En esta sección veremos...").
- Transicionar entre secciones ("Habiendo definido lo anterior...").
- Repetir información ya declarada en otra sección.
- Ser prescindible: si se elimina y las reglas siguen siendo igual de claras, la prosa era grasa y **DEBE** eliminarse.

**Correcto:**

```markdown
Todo artefacto KORA **DEBE** tener un URN tripartito.

La versión no forma parte del URN porque el URN identifica el concepto,
no un snapshot temporal.
```

La prosa explica el porqué (función 1). Sin ella, la regla se cumple pero el lector no entiende la decisión de diseño.

**Incorrecto:**

```markdown
En esta sección definiremos las reglas de URNs. Los URNs son muy
importantes para la organización del sistema.

Todo artefacto KORA **DEBE** tener un URN tripartito.
```

Violación: prosa introductoria ("En esta sección") y valorativa ("son muy importantes") sin función normativa.

---

## 6. Patrón Obligatorio: Regla + Ejemplo

Toda regla con complejidad semántica o riesgo de ambigüedad **DEBE** incluir el par `Correcto:` / `Incorrecto:` inmediatamente después de su enunciado.

El formato del bloque **DEBE** ser el siguiente, admitiendo sintaxis en línea o en bloque según la extensión del contenido:

````markdown
[Enunciado normativo con keyword RFC 2119].

**Correcto:** `[ejemplo breve en línea]`
**Incorrecto:** `[ejemplo breve en línea]`
````

O para ejemplos multilínea:

````markdown
[Enunciado normativo con keyword RFC 2119].

**Correcto:**
```[lenguaje]
[bloque de código extenso que cumple la regla]
```

**Incorrecto:**
```[lenguaje]
[bloque de código extenso que viola la regla]
```
````

Este patrón es la herramienta principal de desambiguación. Un LLM que recibe la spec como contexto usa los ejemplos para calibrar su interpretación de la regla.

---

## 7. Invariantes de KORA/Spec-MD

### 7.1 Consistencia Interna

Cada sección del documento **NO DEBE** contradecir a otra. Si dos reglas entran en conflicto, una de ellas **DEBE** incluir una cláusula de precedencia explícita.

**Correcto:** `"Excepción: En el namespace gn, esta regla prevalece sobre la regla 2.1."`
**Incorrecto:** `[Regla 1 prohíbe X, Regla 2 obliga X. Ninguna declara precedencia]`

### 7.2 Auto-Suficiencia

Cada documento KORA/Spec-MD **DEBE** poder comprenderse sin necesidad de leer otros documentos. Si depende de conceptos definidos externamente, **DEBE** definirlos brevemente inline o referenciarlos vía URN.

**Correcto:** `"...conforme al estándar base (ver [KORA/MD](urn:kora:kb:md-spec))."`
**Incorrecto:** `"...se usa el patrón P-44." (sin definir ni enlazar a su URN)`

### 7.3 Preservación de Idioma y Anglicismos

Todo documento **DEBE** estar escrito en un idioma consistente, el cual **DEBE** ser declarado en el campo `lang` del frontmatter.

Todo anglicismo técnico o término de la industria (ej. *chunk*, *frontmatter*, *workflow*) **PUEDE** utilizarse solo si cumple al menos una condición verificable: (a) tiene entrada en §2, (b) aparece en *cursiva* en su primera mención dentro de cada `##`, o (c) referencia una definición externa vía URN. Un anglicismo **NO DEBE** usarse sin cumplir al menos una de estas condiciones.

**Correcto:** `Frontmatter con lang: es y términos técnicos como Chunk RAG definidos formalmente en §2.`
**Incorrecto:** `Frontmatter con lang: es y secciones traducidas artificialmente usando "código frontal" en vez de "frontmatter".`

### 7.4 Versionamiento Semántico

Todo cambio en las reglas del documento **DEBE** reflejarse en el campo `version`:

| Tipo de cambio                                  | Acción                        |
| ----------------------------------------------- | ----------------------------- |
| Corrección de erratas sin cambio normativo      | Incrementar Patch (x.x.**X**) |
| Nueva regla, restricción o sección agregada     | Incrementar Minor (x.**X**.0) |
| Cambio que invalida implementaciones existentes | Incrementar Major (**X**.0.0) |

**Correcto:** `2.0.0 -> 2.0.1 para corregir redacción sin alterar reglas.`
**Incorrecto:** `2.0.0 -> 2.1.0 para una errata tipográfica sin cambio normativo.`

### 7.5 No-Circularidad

Ningún documento **DEBE** contener definiciones circulares (A se define en términos de B, y B en términos de A).

**Correcto:** `"URN": identificador único; "Namespace": primer segmento del URN.`
**Incorrecto:** `"URN": valor definido por namespace; "Namespace": valor definido por URN.`

---

## 8. Validación

| Check                        | Criterio                                                                                          | Acción si falla                                     |
| ---------------------------- | ------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| Frontmatter válido           | Parsea sin error, campos autorizados                                                              | Corregir YAML                                       |
| Numeración secuencial        | Secciones `##` numeradas 1, 2, 3... (excluye headings dentro de fenced code blocks)               | Renumerar                                           |
| Keywords RFC 2119 en negrita | Toda keyword normativa en **negrita**                                                             | Formatear                                           |
| Headings descriptivos        | Ningún heading genérico ("Otros", "Misceláneos")                                                  | Renombrar con contenido normativo                   |
| Sin ambigüedad               | Cada regla tiene exactamente una lectura                                                          | Reescribir o agregar ejemplo                        |
| Ejemplos presentes           | Toda regla con complejidad semántica o riesgo de ambigüedad tiene par `Correcto:` / `Incorrecto:` | Agregar ejemplos                                    |
| Sin prosa innecesaria        | Toda prosa cumple función normativa                                                               | Eliminar                                            |
| Consistencia interna         | Sin contradicciones no resueltas entre reglas                                                     | Resolver conflicto mediante cláusula de precedencia |
| No-circularidad              | Ningún término definido circularmente                                                             | Reescribir definiciones                             |
| Definiciones completas       | Todo término clave del documento tiene entrada en §2                                              | Agregar a §2 Definiciones                           |
| Anglicismos controlados      | Todo anglicismo cumple §7.3 (definido en §2, cursiva inicial o URN)                              | Definir, cursivar o referenciar                     |
| Referencias válidas          | Todo `(urn:...)` y `[→ Sección]` resuelve                                                         | Corregir                                            |
| Auto-suficiencia             | Conceptos externos definidos inline o referenciados                                               | Agregar definición                                  |

---

## 9. Ejemplo

### Regla bien formada (KORA/Spec-MD)

```markdown
### 4.2 Formato de Fechas

Toda fecha registrada o documentada en el sistema **DEBE** usar el estándar ISO 8601 absoluto (YYYY-MM-DD).

**Correcto:** `2026-02-22`
**Incorrecto:** `22 de Febrero`
```

### Regla mal formada (violaciones)

```markdown
### Fechas en el sistema

Consideramos que sería mejor que todas las fechas vayan en año, mes y día,
porque así es más fácil ordenarlas en la base de datos. 

Como veremos en la siguiente sección, la hora también es relevante.
```

Violaciones: heading descriptivo sin jerarquía numerada ("Fechas en el sistema"), hedging ("consideramos que sería mejor"), sin keyword RFC 2119 explícita ("vayan"), prosa irrelevante orientada a bases de datos en vez de gobernar el comportamiento humano, sintaxis no explícita del formato absoluto, transición narrativa a la sección siguiente, sin par `Correcto:`/`Incorrecto:`.

---

## 10. Template (Esqueleto Mínimo)

Todo documento KORA/Spec-MD **DEBE** seguir este esqueleto estructural:

```markdown
---
_manifest:
  urn: "urn:{namespace}:{type}:{id}"
  provenance:
    created_by: "{autor}"
    created_at: "{YYYY-MM-DD}"
    source: "{referencias}"
version: "{semver}"
status: draft|published|deprecated
tags: [{tag_1}, {tag_2}, {tag_3}]
lang: "{ISO 639-1}"
---

# {Nombre del Estándar} — {Título Descriptivo} v{X.Y.Z}

## 1. Definición

[Esta sección **DEBE** explicar qué es este estándar y qué gobierna, y **DEBE** delimitar explícitamente su alcance y audiencia.]

## 2. Definiciones

[La tabla **DEBE** incluir todos los términos con significado preciso dentro de este documento.]

## 3-N. Secciones Normativas

[Reglas organizadas por tópico. Cada regla **DEBE** incluir una keyword RFC 2119.
Toda regla con complejidad semántica o riesgo de ambigüedad **DEBE** incluir el par Correcto: / Incorrecto:.]

## N+1. Invariantes

[Propiedades que todo documento conforme **DEBE** cumplir.]

## N+2. Validación

[Esta sección **DEBE** contener una tabla de checks con criterio y acción si falla.]

## N+3. Ejemplo (opcional)

[Esta sección **PUEDE** incluir un bloque con un ejemplo bien formado y un bloque con un ejemplo mal formado con sus violaciones anotadas.]
```
