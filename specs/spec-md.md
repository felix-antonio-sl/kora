---
_manifest:
  urn: "urn:kora:kb:spec-md"
  provenance:
    created_by: "FS"
    created_at: "2026-02-26"
    source: "RFC 2119, Diataxis Framework, KORA/MD, KORA categorical-foundations 05"
version: "3.0.0"
status: published
tags: [spec, prescriptivo, formato, instrucciones, workflow, crystallization, traceability]
lang: es
---

# KORA/Spec-MD — Especificacion para Documentos Prescriptivos v3.0.0

## 1. Definicion

**KORA/Spec-MD** es el formato para documentos prescriptivos dentro del ecosistema KORA: especificaciones, workflows, protocolos de agente, guias operativas y estandares.

KORA/MD gobierna conocimiento descriptivo (hechos). KORA/Spec-MD gobierna conocimiento prescriptivo (reglas).

| Eje | KORA/MD | KORA/Spec-MD |
| --- | --- | --- |
| Funcion | Describir lo que ES | Definir lo que debe ser |
| Contenido | Hechos, datos, procedimientos existentes | Reglas, formatos, restricciones, obligaciones |
| Prosa | Prohibida (telegrafico puro) | Permitida cuando explica el porque de una regla |
| Estructura | Headings como `Chunk RAG` | Headings como jerarquia normativa |
| Validacion | Fidelidad al documento fuente | Consistencia interna y ausencia de ambiguedad |
| Consumidor primario | RAG / *Retrieval* | LLM en *Context Window* (*Skill*, *System Prompt*) |

### 1.1 Alcance y Audiencia

**Audiencia primaria:** LLMs que reciben documentos KORA/Spec-MD como skills o instrucciones de sistema. **Audiencia secundaria:** Humanos que disenan, escriben o revisan especificaciones KORA.

Para optimizar su interpretacion por la audiencia primaria, todo documento prescriptivo dentro de KORA **DEBE** redactarse conforme a esta especificacion. Un documento KORA/Spec-MD **NO DEBE** utilizarse para registrar conocimiento descriptivo (ver [KORA/MD](urn:kora:kb:md-spec)).

**Correcto:** `Redactar un "Protocolo de Seguridad" usando el formato KORA/Spec-MD`
**Incorrecto:** `Usar KORA/Spec-MD para el "Historial de Incidentes" (es descriptivo, DEBE usar KORA/MD)`

En estandares fundacionales de formatos descriptivos, un documento **PUEDE** incluir una clausula de auto-excepcion para su propia redaccion. Toda clausula de auto-excepcion **DEBE** referenciar explicitamente KORA/Spec-MD y delimitar de forma acotada que regla local queda exceptuada.

**Correcto:** `Declarar una auto-excepcion limitada a la prohibicion de prosa e indicar referencia explicita a KORA/Spec-MD.`
**Incorrecto:** `Declarar una auto-excepcion global sin alcance ni referencia normativa.`

### 1.2 Proceso de Cristalizacion

KORA/MD transforma documentos humanos en conocimiento optimizado para RAG (ver [md-spec](urn:kora:kb:md-spec) §6). KORA/Spec-MD define un proceso analogo para reglas: la **cristalizacion**.

La cristalizacion toma un conjunto heterogeneo de inputs — decisiones de diseno (explicitas o tacitas), practicas existentes (convenciones informales), y restricciones (tecnicas, organizacionales, legales) — y produce un documento prescriptivo con reglas explicitas:

```python
# Crystallization process C: Decisions -> KORA/Spec-MD
def crystallize(inputs: set[Decision | Practice | Restriction]) -> SpecDocument:
    """
    Transform implicit decisions and informal practices
    into explicit rules with RFC 2119 keywords.
    """
    rules = []
    for item in inputs:
        rule = make_explicit(item)          # Crystallizer: implicit -> explicit
        rule = force_single_reading(rule)    # Formalizer: one reading only
        rule = disambiguate(rule)            # Disambiguator: force one interpretation
        if rule.is_complex or rule.is_ambiguous:
            rule.add_examples()              # Exemplifier: Correcto/Incorrecto
        rules.append(rule)
    return assemble_spec(rules)
```

Todo documento que ingrese al monorepo para cristalizacion **DEBE** transitar por el pipeline de ingesta definido en [Pipeline de Ingesta](urn:kora:kb:pipeline-ingesta): `inbox/` -> `source/` -> `drafts/` -> `knowledge/`.

Traces to: formal/05 §2.3 (Crystallization Functor C)

**Propiedades del proceso de cristalizacion:**

- **Cristalizador:** El proceso **DEBE** convertir decisiones implicitas y practicas observadas en reglas explicitas con keywords RFC 2119.
- **Formalizador:** Cada convencion informal **DEBE** materializarse como una regla con exactamente una lectura posible.
- **Desambiguador:** Donde la entrada admite multiples interpretaciones, la salida **DEBE** forzar exactamente una.
- **Ejemplificador:** Toda regla con complejidad semantica o riesgo de ambiguedad **DEBE** acompanarse del par `Correcto:` / `Incorrecto:` para anclar la interpretacion.

**Correcto:**
```markdown
- **Cristalizador:** (propiedad descrita con lenguaje normativo DEBE).
- **Ejemplificador:** ... (propiedad acompanada de este mismo bloque de Correcto/Incorrecto para evitar ambiguedad).
```

**Incorrecto:**
```markdown
- Cristalizador: Intenta escribir reglas claras cuando puedas.
```

### 1.3 Convencion de Trazabilidad

Toda regla operacional en un documento KORA/Spec-MD que tenga justificacion formal en la Formal Layer (documentos `knowledge/kora/categorical-foundations/00-05`) **DEBERIA** incluir una linea de trazabilidad inmediatamente despues del enunciado de la regla:

```markdown
Todo agente DEBE descomponerse en exactamente 5 componentes.
Traces to: formal/01 §7 (Segregation is Necessary theorem)
```

**Formato:** `Traces to: formal/{numero} §{seccion} ({nombre del teorema o propiedad})`

**Semantica:**

- **Con traza:** la regla tiene respaldo matematico. Modificarla requiere verificar contra el teorema formal referenciado.
- **Sin traza:** la regla es pragmatica (token budgets, naming, SemVer). Puede modificarse sin verificacion formal.

La presencia o ausencia de traza **NO DEBE** afectar la fuerza normativa de la regla. Una regla con **DEBE** sigue siendo obligatoria independientemente de si tiene traza formal o no.

**Correcto:** `"Todo CM es un Skill valido. Traces to: formal/02 §2.3 (eta isomorphism)"`
**Incorrecto:** `"Skills DEBEN tener <=5000 tokens. Traces to: ..." (regla pragmatica sin teorema formal; no debe tener traza)`

---

## 2. Definiciones

La tabla de esta seccion **DEBE** incluir todo termino clave con significado preciso dentro de este documento:

**Correcto:** `El documento usa "RFC 2119" y "URN"; ambos aparecen definidos en esta tabla.`
**Incorrecto:** `El documento usa "ACL" como termino clave y no existe entrada para "ACL".`

| Termino | Definicion |
| --- | --- |
| **Artefacto** | Archivo Markdown unitario con frontmatter KORA y cuerpo de contenido |
| **Documento prescriptivo** | Artefacto que establece como deben comportarse el sistema, los usuarios o los documentos (lo que debe ser) |
| **Documento descriptivo** | Artefacto que registra hechos, datos o procedimientos existentes (lo que ES) |
| **Hedging** | Lenguaje evasivo, condicional o probabilistico ("probablemente", "suele", "en general") que diluye o relativiza una obligacion normativa |
| **Regla** | Unidad atomica de control: una oracion con keyword RFC 2119 que impone una obligacion, prohibicion o permiso, opcionalmente acompanada de par `Correcto:` / `Incorrecto:` |
| **Chunk RAG** | Unidad de texto independientemente recuperable por un sistema de retrieval |
| **Cristalizacion** | Proceso de convertir decisiones implicitas, practicas informales y restricciones en reglas explicitas con keywords RFC 2119 |
| **Traces to** | Convencion de trazabilidad (§1.3) que conecta una regla operacional con su justificacion en la Formal Layer |
| **Formal Layer** | Capa de conocimiento categorico-matematico que provee justificacion formal a las reglas operacionales |
| **Keyword RFC 2119** | Palabra con significado normativo estandarizado (`DEBE`, `DEBERIA`, `PUEDE` y sus negaciones) |
| **SemVer** | Esquema de versionamiento semantico `MAJOR.MINOR.PATCH` usado para reflejar impacto de cambios normativos |
| **Patch/Minor/Major** | Tipos de incremento SemVer: Patch corrige erratas sin cambio normativo, Minor agrega reglas compatibles, Major introduce rupturas |
| **ISO 639-1** | Estandar de codigo de idioma de dos letras usado en el campo `lang` |
| **ISO 8601 (fecha)** | Estandar de fecha absoluta en formato `YYYY-MM-DD` |
| **URN** | Identificador unico de recurso con formato `urn:{namespace}:{type}:{id}` |
| **Namespace** | Primer segmento logico de un URN; delimita el dominio al que pertenece el recurso |
| **Frontmatter** | Bloque YAML delimitado por `---` al inicio del archivo, contiene metadata de maquina |
| **Cuerpo Prescriptivo** | Segunda capa del documento: contenido Markdown con reglas, definiciones y prosa normativa, separado del frontmatter |
| **Clausula de auto-excepcion** | Regla explicita y acotada que exceptua una norma local del propio documento, con referencia a su estandar rector |
| **Prosa explicativa** | Texto dentro de un documento KORA/Spec-MD que cumple una funcion normativa: racionalizar, desambiguar, clarificar o contextualizar reglas |
| **Fenced code block** | Bloque Markdown delimitado por triple backtick; su contenido se trata como literal y no participa en validaciones de headings |
| **Context Window** | Ventana de contexto activa de un LLM donde se inyectan instrucciones, definiciones y evidencia relevante |
| **Workflow** | Secuencia prescriptiva de pasos operativos ejecutables por un agente humano o LLM |
| **Skill** | Habilidad o herramienta empaquetada que un LLM puede invocar en su *Context Window* |
| **System Prompt** | Instruccion base fundacional inyectada a un LLM (Agente) antes de interactuar con el usuario |
| **Retrieval** | Mecanismo de busqueda semantica para inyectar fragmentos de conocimiento en contextos de LLMs |
| **Input / Output** | Datos de entrada y salida, respectivamente, para una evaluacion, funcion, agente o proceso |
| **Snapshot** | Estado congelado de un objeto, abstraccion o conocimiento en una version especifica temporal |
| **Filler** | Texto de relleno carente de valor informativo o normativo (grasa comunicativa) |

---

## 3. Anatomia del Documento

Todo documento KORA/Spec-MD **DEBE** constar de exactamente **2 capas**:

```
+---------------------------------+
|  CAPA 1: YAML Frontmatter      |  <- Manifiesto (metadata de maquina)
|  (---  ...  ---)                |
+---------------------------------+
|  CAPA 2: Cuerpo Prescriptivo   |  <- Reglas, definiciones, explicaciones
|  (# -> ## -> ### -> contenido)  |
+---------------------------------+
```

**Correcto:** `Apertura de archivo con --- seguido del YAML de manifiesto`
**Incorrecto:** `Apertura de archivo con # Titulo seguido del YAML mas abajo`

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

El cuerpo prescriptivo **DEBE** estructurar su contenido en jerarquia de encabezados [-> 5. Gramatica Estructural] y **NO DEBE** contener prosa que no cumpla una funcion normativa explicita [-> 5.4 Prosa Explicativa].

---

## 4. Lenguaje de Obligacion

Todo documento KORA/Spec-MD **DEBE** adoptar las keywords de RFC 2119/8174 para expresar niveles de obligatoriedad. Cada keyword **DEBE** escribirse siempre en **negrita** para senalar su uso normativo:

| Keyword | Significado |
| --- | --- |
| **DEBE** (MUST) | Requisito absoluto. No implementarlo viola la especificacion. |
| **NO DEBE** (MUST NOT) | Prohibicion absoluta. |
| **DEBERIA** (SHOULD) | Recomendado. Puede omitirse si hay razon documentada. |
| **NO DEBERIA** (SHOULD NOT) | Desaconsejado. Puede hacerse si hay razon documentada. |
| **PUEDE** (MAY) | Opcional. La implementacion decide. |

**Reglas de uso:**
- Toda keyword **DEBE** usarse solo cuando la oracion expresa una obligacion, prohibicion o permiso. **NO DEBE** usarse con valor normativo en oraciones puramente descriptivas o explicativas.
- La mencion metalinguistica de keywords RFC 2119 en definiciones, tablas de referencia o ejemplos didacticos **PUEDE** realizarse sin valor normativo; en esos casos **DEBERIA** representarse en codigo inline (por ejemplo, `DEBE`) para evitar ambiguedad.
- En documentos en espanol, se **DEBE** usar la version castellana. Cada equivalencia inglesa **PUEDE** incluirse entre parentesis solo en la primera mencion de su keyword y **NO DEBE** repetirse en menciones posteriores.
- En documentos en ingles, se **DEBE** usar la keyword RFC 2119 correspondiente en MAYUSCULAS.

**Correcto:** `Primera mencion: **DEBE** (equivalencia inglesa). Menciones posteriores: **DEBE** sin equivalencia inglesa.`
**Incorrecto:** `Incluir equivalencia inglesa en todas las apariciones de la misma keyword en un documento en espanol.`

---

## 5. Gramatica Estructural

### 5.1 Jerarquia de Encabezados

| Nivel | Rol en Spec | Ejemplo |
| --- | --- | --- |
| `#` | Titulo del estandar | `# KORA/Spec-MD — Especificacion v3.0` |
| `##` | Seccion normativa principal | `## 4. Lenguaje de Obligacion` |
| `###` | Subseccion / componente de regla | `### 5.1 Jerarquia de Encabezados` |
| `####` | Detalle, caso especial, excepcion | `#### Excepciones para prosa explicativa` |

**Reglas:**
- Cada encabezado **NO DEBE** exceder la profundidad de nivel 4 (`####`).
- Cada seccion `##` **DEBE** estar numerada secuencialmente (`## 1.`, `## 2.`, ...) para referencias inequivocas dentro y fuera del documento. Todo heading dentro de fenced code blocks **NO DEBE** considerarse para esta validacion.
- Cada encabezado **DEBE** ser descriptivo del contenido normativo, no generico ("Otros", "Miscelaneos").

**Correcto:** `## 4. Lenguaje de Obligacion`
**Incorrecto:** `## Cosas Importantes`

**Correcto:** `#### Excepcion para repositorios heredados`
**Incorrecto:** `##### Excepcion para repositorios heredados`

**Correcto:** `## 1. Definicion`, `## 2. Definiciones`, `## 3. Anatomia del Documento`
**Incorrecto:** `## 1. Definicion`, `## 3. Anatomia del Documento` (salta `## 2.`)

### 5.2 Elementos de Contenido

Cada elemento de la siguiente tabla **PUEDE** incluirse en KORA/Spec-MD conforme a su uso permitido, pero **NO DEBE** emplearse para su funcion prohibida:

| Elemento | Uso Permitido en Specs | Funcion Prohibida |
| --- | --- | --- |
| Prosa explicativa | Contextualizar una regla, explicar el porque, prevenir ambiguedad | Narracion, transiciones, filler |
| Keywords RFC 2119 (en negrita) | Expresar niveles de obligacion | Enfasis generico |
| Blockquote (`>`) | Principio o axioma fundamental del estandar | Citas de fuentes externas |
| Bloque de codigo | Ejemplos normativos, templates, formatos validos | Decoracion |

### 5.3 Elementos Prohibidos

Cada elemento de la siguiente lista **NO DEBE** incluirse en documentos KORA/Spec-MD:

- Hedging ("probablemente", "en general", "suele")
- Ambiguedad pronominal ("esto", "eso", "lo anterior" sin referente explicito)
- Frases de cortesia o trato informal
- Multiples interpretaciones posibles de una regla (toda regla **DEBE** tener exactamente una lectura)
- Reglas sin ejemplo (toda regla con complejidad semantica o riesgo de ambiguedad **DEBE** incluir el par `Correcto:` / `Incorrecto:`)
- Secciones sin contenido normativo (si no prescribe ni define, no pertenece)

**Correcto:** `"El URN **DEBE** estar en minusculas."`
**Incorrecto:** `"En general, sugerimos que el URN este en minusculas para evitar problemas."`

### 5.4 Prosa Explicativa

El cuerpo prescriptivo **PUEDE** incluir prosa explicativa unicamente si dicha prosa cumple al menos una de las siguientes funciones normativas:

1. **Explicar el porque** de una regla (racionalizacion).
2. **Prevenir una interpretacion erronea** (desambiguacion).
3. **Clarificar un termino** ya definido en [-> 2. Definiciones] cuando el contexto local requiere elaboracion. Toda definicion canonica **DEBE** residir en §2; la prosa inline solo contextualiza, no reemplaza.
4. **Contextualizar una restriccion** que sin contexto pareceria arbitraria.

Toda prosa **NO DEBE**:
- Introducir una seccion ("En esta seccion veremos...").
- Transicionar entre secciones ("Habiendo definido lo anterior...").
- Repetir informacion ya declarada en otra seccion.
- Ser prescindible: si se elimina y las reglas siguen siendo igual de claras, la prosa era grasa y **DEBE** eliminarse.

**Correcto:**

```markdown
Todo artefacto KORA **DEBE** tener un URN tripartito.

La version no forma parte del URN porque el URN identifica el concepto,
no un snapshot temporal.
```

La prosa explica el porque (funcion 1). Sin ella, la regla se cumple pero el lector no entiende la decision de diseno.

**Incorrecto:**

```markdown
En esta seccion definiremos las reglas de URNs. Los URNs son muy
importantes para la organizacion del sistema.

Todo artefacto KORA **DEBE** tener un URN tripartito.
```

Violacion: prosa introductoria ("En esta seccion") y valorativa ("son muy importantes") sin funcion normativa.

---

## 6. Patron Obligatorio: Regla + Ejemplo + Traza

Toda regla con complejidad semantica o riesgo de ambiguedad **DEBE** incluir el par `Correcto:` / `Incorrecto:` inmediatamente despues de su enunciado.

Si la regla tiene justificacion en la Formal Layer, **DEBERIA** incluir ademas una linea `Traces to:` inmediatamente despues del enunciado y antes de los ejemplos.

El formato del bloque **DEBE** ser el siguiente:

````markdown
[Enunciado normativo con keyword RFC 2119].
Traces to: formal/{doc} §{seccion} ({nombre del teorema})

**Correcto:** `[ejemplo breve en linea]`
**Incorrecto:** `[ejemplo breve en linea]`
````

O sin traza (regla pragmatica):

````markdown
[Enunciado normativo con keyword RFC 2119].

**Correcto:** `[ejemplo breve en linea]`
**Incorrecto:** `[ejemplo breve en linea]`
````

Para ejemplos multilinea:

````markdown
[Enunciado normativo con keyword RFC 2119].
Traces to: formal/{doc} §{seccion} ({nombre})

**Correcto:**
```[lenguaje]
[bloque de codigo extenso que cumple la regla]
```

**Incorrecto:**
```[lenguaje]
[bloque de codigo extenso que viola la regla]
```
````

Este patron es la herramienta principal de desambiguacion. Un LLM que recibe la spec como contexto usa los ejemplos para calibrar su interpretacion de la regla.

---

## 7. Invariantes de KORA/Spec-MD

### 7.1 Consistencia Interna

Cada seccion del documento **NO DEBE** contradecir a otra. Si dos reglas entran en conflicto, una de ellas **DEBE** incluir una clausula de precedencia explicita.

**Correcto:** `"Excepcion: En el namespace gn, esta regla prevalece sobre la regla 2.1."`
**Incorrecto:** `[Regla 1 prohibe X, Regla 2 obliga X. Ninguna declara precedencia]`

### 7.2 Auto-Suficiencia

Cada documento KORA/Spec-MD **DEBE** poder comprenderse sin necesidad de leer otros documentos. Si depende de conceptos definidos externamente, **DEBE** definirlos brevemente inline o referenciarlos via URN.

**Correcto:** `"...conforme al estandar base (ver [KORA/MD](urn:kora:kb:md-spec))."`
**Incorrecto:** `"...se usa el patron P-44." (sin definir ni enlazar a su URN)`

### 7.3 Preservacion de Idioma y Anglicismos

Todo documento **DEBE** estar escrito en un idioma consistente, el cual **DEBE** ser declarado en el campo `lang` del frontmatter.

Todo anglicismo tecnico o termino de la industria (ej. *chunk*, *frontmatter*, *workflow*) **PUEDE** utilizarse solo si cumple al menos una condicion verificable: (a) tiene entrada en §2, (b) aparece en *cursiva* en su primera mencion dentro de cada `##`, o (c) referencia una definicion externa via URN. Un anglicismo **NO DEBE** usarse sin cumplir al menos una de estas condiciones.

**Correcto:** `Frontmatter con lang: es y terminos tecnicos como Chunk RAG definidos formalmente en §2.`
**Incorrecto:** `Frontmatter con lang: es y secciones traducidas artificialmente usando "codigo frontal" en vez de "frontmatter".`

### 7.4 Versionamiento Semantico

Todo cambio en las reglas del documento **DEBE** reflejarse en el campo `version`:

| Tipo de cambio | Accion |
| --- | --- |
| Correccion de erratas sin cambio normativo | Incrementar Patch (x.x.**X**) |
| Nueva regla, restriccion o seccion agregada | Incrementar Minor (x.**X**.0) |
| Cambio que invalida implementaciones existentes | Incrementar Major (**X**.0.0) |

**Correcto:** `2.0.0 -> 2.0.1 para corregir redaccion sin alterar reglas.`
**Incorrecto:** `2.0.0 -> 2.1.0 para una errata tipografica sin cambio normativo.`

### 7.5 No-Circularidad

Ningun documento **DEBE** contener definiciones circulares (A se define en terminos de B, y B en terminos de A).

**Correcto:** `"URN": identificador unico; "Namespace": primer segmento del URN.`
**Incorrecto:** `"URN": valor definido por namespace; "Namespace": valor definido por URN.`

---

## 8. Validacion

| Check | Criterio | Accion si falla |
| --- | --- | --- |
| Frontmatter valido | Parsea sin error, campos autorizados | Corregir YAML |
| Numeracion secuencial | Secciones `##` numeradas 1, 2, 3... (excluye headings dentro de fenced code blocks) | Renumerar |
| Keywords RFC 2119 en negrita | Toda keyword normativa en **negrita** | Formatear |
| Headings descriptivos | Ningun heading generico ("Otros", "Miscelaneos") | Renombrar con contenido normativo |
| Sin ambiguedad | Cada regla tiene exactamente una lectura | Reescribir o agregar ejemplo |
| Ejemplos presentes | Toda regla con complejidad semantica o riesgo de ambiguedad tiene par `Correcto:` / `Incorrecto:` | Agregar ejemplos |
| Sin prosa innecesaria | Toda prosa cumple funcion normativa | Eliminar |
| Consistencia interna | Sin contradicciones no resueltas entre reglas | Resolver conflicto mediante clausula de precedencia |
| No-circularidad | Ningun termino definido circularmente | Reescribir definiciones |
| Definiciones completas | Todo termino clave del documento tiene entrada en §2 | Agregar a §2 Definiciones |
| Anglicismos controlados | Todo anglicismo cumple §7.3 (definido en §2, cursiva inicial o URN) | Definir, cursivar o referenciar |
| Referencias validas | Todo `(urn:...)` y `[-> Seccion]` resuelve | Corregir |
| Auto-suficiencia | Conceptos externos definidos inline o referenciados | Agregar definicion |
| Trazabilidad valida | Toda linea `Traces to:` referencia un documento y seccion existentes en la Formal Layer | Corregir referencia o eliminar traza |

---

## 9. Ejemplo

### Regla bien formada (KORA/Spec-MD)

```markdown
### 4.2 Formato de Fechas

Toda fecha registrada o documentada en el sistema **DEBE** usar el estandar ISO 8601 absoluto (YYYY-MM-DD).

**Correcto:** `2026-02-22`
**Incorrecto:** `22 de Febrero`
```

### Regla bien formada con traza

```markdown
### 3.1 Segregacion de Componentes

La logica de transicion (AGENTS.md) **NO DEBE** mezclarse con la personalidad (SOUL.md).
Traces to: formal/01 §2.2 (Fiber Independence theorem)

**Correcto:** `AGENTS.md contiene solo FSM. SOUL.md contiene solo tono y arquetipo.`
**Incorrecto:** `AGENTS.md contiene "Soy un analista apasionado" seguido de la FSM.`
```

### Regla mal formada (violaciones)

```markdown
### Fechas en el sistema

Consideramos que seria mejor que todas las fechas vayan en ano, mes y dia,
porque asi es mas facil ordenarlas en la base de datos.

Como veremos en la siguiente seccion, la hora tambien es relevante.
```

Violaciones: heading descriptivo sin jerarquia numerada ("Fechas en el sistema"), hedging ("consideramos que seria mejor"), sin keyword RFC 2119 explicita ("vayan"), prosa irrelevante orientada a bases de datos en vez de gobernar el comportamiento humano, sintaxis no explicita del formato absoluto, transicion narrativa a la seccion siguiente, sin par `Correcto:`/`Incorrecto:`.

---

## 10. Template (Esqueleto Minimo)

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

# {Nombre del Estandar} — {Titulo Descriptivo} v{X.Y.Z}

## 1. Definicion

[Esta seccion **DEBE** explicar que es este estandar y que gobierna, y **DEBE** delimitar explicitamente su alcance y audiencia.]

## 2. Definiciones

[La tabla **DEBE** incluir todos los terminos con significado preciso dentro de este documento.]

## 3-N. Secciones Normativas

[Reglas organizadas por topico. Cada regla **DEBE** incluir una keyword RFC 2119.
Toda regla con complejidad semantica o riesgo de ambiguedad **DEBE** incluir el par Correcto: / Incorrecto:.
Reglas con justificacion formal **DEBERIAN** incluir Traces to:]

## N+1. Invariantes

[Propiedades que todo documento conforme **DEBE** cumplir.]

## N+2. Validacion

[Esta seccion **DEBE** contener una tabla de checks con criterio y accion si falla.]

## N+3. Ejemplo (opcional)

[Esta seccion **PUEDE** incluir un bloque con un ejemplo bien formado y un bloque con un ejemplo mal formado con sus violaciones anotadas.]
```
