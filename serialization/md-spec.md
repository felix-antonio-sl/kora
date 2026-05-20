---
_manifest:
  urn: "urn:kora:kb:md-spec"
  provenance:
    created_by: "FS"
    created_at: "2026-03-09"
    source: "KORA categorical-foundations 05, KORA/Gobernanza v4.3.0, refactor del contrato de compresion y realizacion superficial; v7 agrega familia atomic con productor canonico atomize; v7.1 fusiona tipos de artefacto y familias documentales; v8.0 absorbe el contrato prescriptivo de la retirada spec-md v5.2.0 como perfil normativo de la familia `spec`; v9.0 delega pipeline, lifecycle conceptual e identidad URN conceptual a knowledge-spec §3-§4, §8, §13, documenta las cuatro familias auxiliares que el toolchain usa (`bok`, `source`, `source-alias`, `generic`), y limpia la tabla de validacion para reflejar solo invariantes de formato; v10.0 retira familia atomic; v11.0 (KORA v9, HITL 2026-05-20): deshace la absorcion de v8.0 — el perfil prescriptivo migra a spec-md v1.0.0 (urn:kora:kb:spec-md regresa al canon). md-spec queda como spec del regimen descriptivo puro; la familia `spec` delega sus invariantes prescriptivos a spec-md."
version: "11.0.0"
status: publicado
tags: [markdown, conocimiento, rag, koraficacion, fidelidad, prescriptivo, cristalizacion, rfc2119, formato]
lang: es
extensions:
  kora:
    family: spec
relations:
  depends:
    - "urn:kora:kb:gobernanza"
  cites:
    - "urn:kora:kb:05-governance-lattice"
    - "urn:kora:kb:knowledge-spec"
---

# KORA/MD v11.0.0

## 1. Definicion

KORA/MD es el **formato base del regimen descriptivo** de artefactos
textuales del ecosistema KORA. Cubre todos los artefactos KORA/MD
descriptivos: knowledge, manuales, corpus, notas, glosarios, catalogos,
ADRs, etc.

El **regimen prescriptivo** (specs normativas) se define en
`urn:kora:kb:spec-md`, que extiende este envelope con los invariantes
adicionales (RFC 2119, `Traces to:`, cristalizacion, patron
regla+ejemplo+traza, invariantes prescriptivos, template, autoderecho
de precedencia). Los documentos de familia `spec` cumplen ambos
contratos.

Esta separacion (KORA v9, 2026-05-20) restaura la disciplina previa a
md-spec v8.0, que habia absorbido `spec-md v5.2.0`.

### 1.1 Alcance

KORA/MD optimiza almacenamiento, indexacion y recuperacion para humanos y
LLMs via RAG sin sacrificar verdad factual, y preserva la fuerza normativa
de las specs sin ambiguedad.

Esta spec es responsable de:

- envelope minimal (`_manifest` + body) para regimen descriptivo,
- gramatica estructural comun a ambos regimenes,
- familias documentales descriptivas y sus invariantes,
- koraficacion (`DocHumano -> KORA/MD`).

### 1.2 Lo que NO gobierna esta spec

- **Perfil prescriptivo `spec`**: gobernado por `urn:kora:kb:spec-md`
  (RFC 2119, `Traces to:`, cristalizacion, invariantes prescriptivos,
  template, auto-declaracion de precedencia).
- **URN conceptual y namespace-directorio**: gobernado por
  `knowledge-spec §3` (regimen `urn:{ns}:kb:{id}`).
- **Lifecycle descriptivo y status por directorio**: gobernado por
  `knowledge-spec §4`.
- **Pipeline de curacion** (`INBOX -> REVIEW -> productivo`): gobernado
  por `knowledge-spec §8`.
- **Productores canonicos de familia**: registrados en
  `knowledge-spec §9` (esta spec solo declara los invariantes de cada
  familia).
- **URN agentico** y shape `autoria-spec` de habilidades/agentes:
  gobernado por `autoria-spec` y `gobernanza §4.3`.

### 1.3 Audiencia

Audiencia primaria: runtimes, pipelines de recuperacion y agentes que
consumen ley operativa.

Audiencia secundaria: humanos que curan el corpus, diseñan, auditan o
evolucionan el ecosistema.

Todo documento `spec` de KORA **DEBE** redactarse conforme a esta
especificacion bajo el perfil `spec` (§5.6.2). Un documento descriptivo
**NO DEBE** gobernarse por los invariantes prescriptivos del perfil
`spec`.

## 2. Definiciones

| Termino | Definicion |
| --- | --- |
| Artefacto KORA/MD | Archivo Markdown con frontmatter KORA y cuerpo descriptivo o prescriptivo. |
| Koraficacion | Transformacion `DocHumano -> KORA/MD` que preserva verdad y elimina entropia comunicativa. |
| Chunk RAG | Unidad primaria de recuperacion delimitada por `##`. |
| Skeleton | Estructura del documento: titulo, headings, tablas, listas, jerarquia. |
| Meat | Hechos atomicos que deben preservarse: cifras, fechas, condiciones, excepciones, referencias, dependencias. |
| Fat | Retorica, hedging, transiciones y relleno editorial eliminable. |
| Realizacion superficial | Eleccion de la forma final visible del conocimiento: heading, prosa, lista o tabla. |
| Labelese | Salida que suena a serializacion de campos: `Asunto`, `Contenido`, `Tipo`, `Path`, etc. |
| FS | Fidelity Score. Porcentaje de hechos preservados o comprimidos sin perdida semantica. |
| CR | Compression Ratio. Longitud fuente / longitud salida. |
| SSOT | Un hecho, un lugar. |
| Proposicion atomica | Hecho verificable minimo autocontenido, con tipo, texto comprimido y ancla de fuente resoluble. |
| Productor canonico | Herramienta autorizada para generar artefactos de una familia con garantia de invariantes (`knowledge-spec §9`). |
| Documento `spec` | Artefacto de familia documental `spec`: define lo que debe ser (reglas, contratos, validaciones). |
| Keyword (RFC 2119) | Palabra reservada que fija fuerza normativa: DEBE, NO DEBE, DEBERIA, NO DEBERIA, PUEDE. Enum cerrado. |
| Regla | Oracion con keyword RFC 2119 y semantica operativa univoca. |
| Cristalizacion | Proceso `Decisiones + Practicas + Restricciones -> regla explicita con una sola lectura valida`. |
| Rationale | Explicacion auxiliar no normativa sobre motivacion; no introduce obligaciones. |
| Traces to | Puente entre una regla operacional y su justificacion en la Formal Layer oficial. |
| Auto-suficiencia | Propiedad de una regla que puede entenderse con su propio contexto local. |
| No-circularidad | Propiedad de una regla que no se justifica solo remitiendo a otra regla igual de opaca. |

## 3. Anatomia del documento

Todo artefacto KORA/MD **DEBE** constar de exactamente dos capas:

1. Frontmatter YAML base.
2. Cuerpo de conocimiento Markdown.

### 3.1 Capa 1: YAML Frontmatter

```yaml
---
_manifest:
  urn: "urn:{namespace}:{type}:{id}"
  provenance:
    created_by: "{autor}"
    created_at: "{YYYY-MM-DD}"
    source: "{referencia}"
version: "{semver}"
status: borrador|publicado|deprecado     # regimen descriptivo (knowledge-spec §4)
                                          # ejecutables agregan `activo` y `retirado` (autoria-spec §11)
tags: [{tag1}, {tag2}, {tag3}]
lang: "{iso-639-1}"
extensions: {}
---
```

Reglas del envelope:

1. El sobre base es **cerrado**; campos adicionales **DEBEN** residir en
   `extensions.{namespace}`.
2. `tags` **DEBE** contener al menos 3 tags semanticos.
3. `lang` describe el idioma del cuerpo (`iso-639-1`; default `es`).
4. `source` describe la procedencia humana o documental del conocimiento.
5. `version` se declara **fuera** del URN (`gobernanza §4.3`).
6. `status` se restringe a valores canonicos en español, con compatibilidad
   de aliases ingleses (`active`, `draft`, `published`, `deprecated`,
   `retired`) que el toolchain normaliza a su equivalente español
   (`toolchain/kora_lib/lifecycle.py`).
7. Cuando `source` referencia archivos del monorepo, la ruta **DEBERIA**
   ser resoluble desde la raiz del repo. Enforcement: manual.

Reglas que delegan a otras specs:

8. **URN tripartito y namespace-directorio**: gobernado por
   `knowledge-spec §3` (artefactos en `artifacts/knowledge/`) y por
   `autoria-spec §10` (artefactos agenticos).
9. **Status por directorio y lifecycle**: gobernado por
   `knowledge-spec §4` (descriptivo) y `autoria-spec §11` (agentico).
10. **Transicion `borrador -> publicado/activo`**: gobernada por
    `knowledge-spec §13` (`kora promote` para descriptivos) y por la
    misma CLI para habilidades (`autoria-spec §8.3`).

### 3.2 Capa 2: Cuerpo de conocimiento

El cuerpo **DEBE** privilegiar estructura recuperable sobre prosa
ornamental.

Permitido: headings, listas, tablas, definiciones, formulas, ejemplos
minimos.

Desaconsejado: transiciones narrativas, relleno editorial, referencias
vagas sin ancla.

### 3.3 Campo `relations`

El campo raiz `relations` esta **reservado por esta spec** para que
`knowledge-spec §6` defina su semantica (tipos `cites`, `depends`,
`supersedes`, `refines`, `traces_requirements`). Esta spec solo declara
que la clave es admisible en el envelope; los invariantes vivan en
`knowledge-spec`.

## 4. Topologia de direccionamiento

### 4.1 Estructura tripartita

Todo artefacto KORA/MD **DEBE** usar un URN `urn:{namespace}:{type}:{id}`.

Reglas:

1. La version **NO DEBE** incluirse en el URN.
2. Las referencias KORA **NO DEBEN** incluir version en artefactos
   conceptuales.
3. El filesystem con manifests es la fuente de verdad; el catalogo es una
   vista derivada.

Para el regimen concreto del componente `{type}` ver `gobernanza §4.3`:

- artefactos descriptivos (familias §5.6) usan `urn:{ns}:kb:{id}`;
- artefactos agenticos usan `urn:{ns}:artefacto:{id}`.

### 4.2 Tipos de referencia

Tipos permitidos:

- interna: `[-> Seccion]`
- KORA: `[Descripcion](urn:{ns}:{type}:{id})`
- externa: `[Descripcion](https://...)`

Reglas:

1. Las referencias internas **DEBEN** apuntar a headings o fragments
   resolubles.
2. Los fragments `#...` **DEBERIAN** usarse solo cuando aportan precision
   real.
3. El catalogo **DEBERIA** mantenerse completo y regenerable via
   `kora index`.

## 5. Gramatica estructural

### 5.1 Jerarquia de encabezados = esqueleto semantico

| Nivel | Rol semantico |
| --- | --- |
| `#` | Titulo del artefacto |
| `##` | Seccion primaria recuperable |
| `###` | Subtopico o componente |
| `####` | Detalle atomico |

Reglas:

1. La profundidad **NO DEBE** exceder `####`.
2. Cada `##` **DEBE** ser recuperable de forma casi aislada.
3. Los headings **DEBEN** ser compactos y semanticamente recuperables.
4. Un `###` **NO DEBE** existir sin un `##` padre.
5. Un heading **NO DEBE** terminar truncado con `...`.
6. Un heading primario **DEBE** expresar sujeto o alcance recuperable; el
   mero ordinal no basta.

### 5.2 Elementos de contenido

| Elemento | Uso permitido | Funcion prohibida |
| --- | --- | --- |
| Negrita | definiciones, terminos clave | enfasis decorativo |
| Cursiva | termino tecnico o extranjero | enfasis estilistico |
| `codigo` | URNs, ids, comandos, literales | resaltado general |
| Lista | enumeracion, procedimiento o desglose normativo | prosa fragmentada sin valor estructural |
| Tabla | comparacion, condiciones, matrices, catalogos | dumping decorativo o serializacion cruda |

### 5.3 Elementos prohibidos (grasa)

Cada elemento de la siguiente lista **NO DEBE** incluirse en KORA/MD:

- introducciones tipo "En este documento veremos..."
- transiciones tipo "A continuacion", "Por otro lado"
- hedging tipo "probablemente", "en general", "suele"
- preguntas retoricas
- saludos y cierres
- duplicacion de hechos

### 5.4 Telegrafizacion = compresion semantica estructural

La escritura KORA/MD **DEBE** ser telegrafica. La telegrafizacion no
significa reducir palabras por si mismas; significa eliminar redundancia y
promover la forma mas densa que preserve verdad y recuperacion.

Definicion operativa:

- comprimir relaciones redundantes
- eliminar verbos de enlace y marcadores discursivos innecesarios
- promover prosa comparativa o condicional a listas o tablas
- evitar repetir sujeto, alcance o contexto ya fijados por el heading
- preservar siempre `skeleton` y `meat`

Reglas de transformacion obligatorias:

| N° | Regla | Patron fuente | Transformacion |
| --- | --- | --- | --- |
| T1 | Eliminar perifrasis y verbos de enlace | "se podran traspasar recursos desde X" | "Traspaso permitido desde X" |
| T2 | Nominalizar acciones cuando mejore densidad | "deberan informar trimestralmente" | "Informe trimestral obligatorio" |
| T3 | Colapsar subordinadas condicionales a lista/tabla | "cuando el monto sea superior a X, se debera..." | Tabla `Condicion \| Resultado \| Base` |
| T4 | Eliminar marcadores discursivos | "asimismo", "a continuacion", "por otro lado", "cabe señalar" | Eliminar sin reemplazo |
| T5 | Comprimir enumeraciones embebidas en prosa a listas | "podran financiar A, B y C" | Lista con marcadores |
| T6 | Eliminar sujetos redundantes | "El Gobierno Regional debera... El Gobierno Regional podra..." | Sujeto una vez en heading, luego implicito |
| T7 | Promover comparaciones y condiciones a tablas | Parrafo con multiples "si X entonces Y" | Tabla `Condicion \| Resultado` |

Patrones estructurales obligatorios:

- Definiciones: `**Termino** - descripcion compacta`
- Condiciones: tabla `Condicion | Resultado | Base`
- Procedimientos: lista secuencial numerada
- Comparaciones: tabla, nunca parrafo si la relacion ya es matricial
- Enumeraciones: lista con marcadores, nunca embebidas en prosa

### 5.4.1 Contraejemplos normativos

Los siguientes pares muestran la transformacion esperada. El patron ✗
**NO DEBE** aparecer en KORA/MD; el patron ✓ **DEBE** usarse en su lugar.

**Contraejemplo 1: Prosa condicional -> lista de condiciones**

✗ Incorrecto:

> Se podran traspasar recursos desde cualquier Subtitulo e Item del presupuesto de inversion del Gobierno Regional respectivo a los Subtitulos 24, 26, 29, 31, 32.06, 33 y 34.07.

✓ Correcto:

> Traspaso permitido desde cualquier Subtitulo/Item de inversion regional a:
>
> - Subtitulos 24, 26, 29, 31, 33, 34.07
> - Subtitulo 32.06

**Contraejemplo 2: Oracion subordinada multiple -> compresion estructural**

✗ Incorrecto:

> Los gobiernos regionales podran realizar convenios de mandato con los municipios de acuerdo con el articulo 16 de la ley N°18.091, para el financiamiento de estudios definidos en el subtitulo 22 item 11.

✓ Correcto:

> Convenios de mandato con municipios permitidos (art. 16, Ley 18.091). Alcance: estudios (Subtitulo 22, Item 11).

**Contraejemplo 3: Parrafo con multiples condiciones -> tabla**

✗ Incorrecto:

> Se exceptuaran del proceso de evaluacion ex ante: a) los programas que hayan iniciado su ejecucion en años anteriores. b) las subvenciones asociadas al Concurso de Vinculacion con la Comunidad 8%. c) las transferencias a universidades, municipalidades, otras entidades publicas y gobierno central.

✓ Correcto:

> Excepciones evaluacion ex ante:
>
> | Tipo | Descripcion |
> | --- | --- |
> | Arrastres | Programas con ejecucion iniciada en años anteriores |
> | Subvenciones 8% | Concurso Vinculacion con la Comunidad |
> | Transferencias | A universidades, municipalidades, entidades publicas, gobierno central |

### 5.4.2 Realizacion superficial

La salida final **DEBE** sonar a conocimiento curado, no a dump comprimido.

Reglas:

1. Un heading puede ser compacto, pero **NO DEBE** quedar truncado con `...`.
2. Un heading primario **DEBE** expresar sujeto o alcance recuperable.
3. Una salida **NO DEBE** sonar a serializacion de campos (`Asunto`, `Contenido`, `Tipo`, `Path`, etc.), salvo que la familia documental lo exija de forma explicita.
4. Listas y tablas solo son validas si mejoran recuperacion o
   comparabilidad; si degradan legibilidad sin aportar estructura,
   **DEBE** preferirse prosa tecnica breve.
5. La nominalizacion es valida solo si no destruye naturalidad tecnica.
6. La compresion **NO DEBE** producir labelese, headings-campo, ni frases
   mecanicas.

Contraejemplos de mala realizacion superficial:

**Contraejemplo 4: Heading truncado**

✗ `## Glosa 03 - Los recursos de los presupuestos de inversion regional no podran...`

✓ `## Glosa 03 - Restriccion de uso de recursos de inversion regional`

**Contraejemplo 5: Heading-campo**

✗ `#### Titulo` / `#### Path` / `#### Artefactos`

✓ `### Introduccion y Fundamentos` + tabla con columnas
`id | urn | titulo | resumen`.

**Contraejemplo 6: Lista que reemplaza indebidamente una frase tecnica simple**

✗ Lista de tres bullets: "Convenios" / "con municipios" / "permitidos".

✓ Prosa: "Convenios de mandato con municipios permitidos."

**Contraejemplo 7: Tabla usada como pseudo-dump**

✗ Tabla `Campo | Valor` para serializar `Tipo`, `Path`, `Status`,
`Source_ID` sin valor recuperable.

✓ Tabla solo cuando exista comparacion, matriz, catalogo o conjunto de
registros.

### 5.5 Preservacion de verdad (prueba acida)

La compresion **NO DEBE** sacrificar contenido informativo.

Traces to: `urn:kora:kb:05-governance-lattice` §2.2 (Koraficacion Functor K)

Regla acida:

- si al eliminar texto cambia solo tono o fluidez, **DEBE** eliminarse
- si al eliminar texto desaparece una condicion, umbral, excepcion, fecha,
  cifra, dependencia o referencia, **NO DEBE** eliminarse

Metafora operativa:

- `skeleton`: preservar estructura
- `meat`: preservar siempre
- `fat`: eliminar siempre

Metricas:

- `FS=100%` es el objetivo obligatorio de fidelidad
- `CR>1.5` es el objetivo de compresion para koraficaciones normales
- `CR<1.5` solo es aceptable si `FS=100%`, no queda grasa eliminable y la
  realizacion superficial sigue siendo valida

### 5.6 Familias documentales

Una **familia documental** es un perfil del formato KORA/MD — no un
formato distinto. Todos los artefactos KORA/MD cumplen el contrato base
(§§1-5); cada familia agrega invariantes que su estructura de dominio
requiere. Esta lista es la **fuente unica** de clasificacion de artefactos
KORA/MD; `knowledge-spec §5` la cita como autoridad.

**Familias canonicas** (declarables via `extensions.{namespace}.family`):

| Familia | Invariantes |
| --- | --- |
| `spec` | Familia prescriptiva. Invariantes completos en §5.6.2 (cristalizacion, RFC 2119, `Traces to:`, patron regla+ejemplo+traza, consistencia interna, auto-suficiencia, no-circularidad, enforcement declarado). URN `urn:{ns}:kb:{id}`; reside en las capas normativas (`governance/`, `ontology/`, `serialization/`, `runtime/`), no en `artifacts/knowledge/`. |
| `guide` | Manual o guia operativa; prosa tecnica controlada; ejemplos concretos vinculados a headings; `## Resumen` recomendado. |
| `normative` | `##` con asunto semantico; condiciones, excepciones y matrices promovidas a listas/tablas; no dumps de numerales sin asunto. |
| `glossary` | Buckets recuperables; sin duplicados no resueltos; alias explicitos. |
| `faq` | `##` por pregunta; respuesta autocontenida; orden por frecuencia o tema. |
| `catalog` | Entradas tabuladas; columnas minimas `id \| urn \| titulo \| resumen`; indexable por CLI. |
| `cq_catalog` | `## Resumen` obligatorio y no vacio; dominios como `##`; scaffold en idioma del documento; subperfil de `catalog`. |
| `inventory` | Puede retener material operativo; si `publication_class=control`, queda fuera de KB publicada. |
| `organigram` | Dependencias estructurales explicitas; no headings-campo para representar jerarquia. |
| `note` | Nota tecnica compacta; al menos un `##` tematico; `## Resumen` opcional cuando el tamaño lo vuelve redundante. |
| `adr` | Architecture Decision Record. Subperfil de `note`. **Frontmatter extendido obligatorio**: `extensions.kora.adr.{contexto, alternativas, factorizacion_elegida, consecuencias, estado}`. Cuerpo con secciones fijas: `## Contexto`, `## Alternativas consideradas`, `## Decision`, `## Consecuencias`, `## Trazabilidad`. Decision se registra como factorizacion categorica: `decision = g ∘ f` donde `f` es la restriccion operativa y `g` el morfismo elegido entre alternativas. Estados: `propuesta -> aceptada -> (superseded \| deprecada \| retirada)`. Trazabilidad: `relations.cites` apunta a las alternativas consideradas aunque no se hayan adoptado. |

**Familias auxiliares** (clasificacion derivada por el toolchain, no se
declaran a mano):

| Familia | Origen | Semantica |
| --- | --- | --- |
| `bok` | `_extract_raw_family` cuando el URN contiene `:kb:bok-` o `tags` incluye `body-of-knowledge`/`bok` | Body of knowledge: corpus extendido, limites de chunk y archivo mas permisivos (1000 lineas por chunk, 1M total). |
| `source` | Convencion de directorio `fuentes/` o sufijo `.source.txt`/`.source.md` | Material fuente preservado para trazabilidad; chunks sin limite estricto. |
| `source-alias` | Subtipo de `source` que apunta a un canonico | No publicable como conocimiento independiente; valido solo como nodo de trazabilidad. |
| `generic` | Default cuando ningun mecanismo de clasificacion (§5.6 reglas de clasificacion) identifica una familia | Limites por defecto (120 lineas por chunk, 320 totales). |

Reglas de clasificacion (orden de precedencia):

1. `extensions.{namespace}.family` explicito en el frontmatter.
2. Convencion de directorio (e.g., `glossaries/`, `normative/`,
   `fuentes/`).
3. Heuristicas sobre URN y `tags` (origen de `bok`).
4. Clasificacion manual del curador durante koraficacion.
5. Productor canonico declarado (`knowledge-spec §9`): si existe, el
   productor fija la familia al emitir el artefacto.
6. Fallback: `generic`.

Una familia **PUEDE** heredar invariantes de otra declarando su relacion
como subperfil (ej. `cq_catalog` subperfil de `catalog`). La herencia es
estrictamente aditiva: el subperfil no puede relajar invariantes del
perfil base.

### 5.6.1 Perfil `spec`: invariantes prescriptivos (delegado)

La familia `spec` define el regimen prescriptivo del ecosistema KORA.
Todo documento `spec` **DEBE** cumplir los invariantes generales de
KORA/MD (esta spec) **mas** los invariantes prescriptivos definidos en
`urn:kora:kb:spec-md`.

Invariantes prescriptivos delegados a `spec-md`:

| Invariante | Ref |
|-----------|-----|
| Proceso de cristalizacion | `spec-md §3` |
| Lenguaje de obligacion RFC 2119 | `spec-md §4` |
| Convencion de trazabilidad (`Traces to:` / `Rationale:`) | `spec-md §5` |
| Elementos retoricos normativos | `spec-md §6` |
| Prosa explicativa admisible (4 funciones validas) | `spec-md §7` |
| Patron obligatorio regla + ejemplo + traza | `spec-md §8` |
| Invariantes prescriptivos (consistencia, auto-suficiencia, no-circularidad, idioma, enforcement) | `spec-md §9` |
| Template esqueleto minimo | `spec-md §10` |
| Invariante de auto-declaracion de precedencia | `spec-md §11` |
| Tabla de validacion prescriptiva (9 checks) | `spec-md §12` |

Esta separacion (KORA v9, 2026-05-20,
`urn:kora:kb:adr-kora-v9-separacion-descriptivo-prescriptivo-y-arnes`)
deshace la absorcion que `md-spec v8.0` habia hecho de
`spec-md v5.2.0`. El URN `urn:kora:kb:spec-md` regresa al canon como
nodo activo.

## 6. Koraficacion

### 6.1 Entrada

Cualquier documento originalmente escrito para humanos **PUEDE** usarse
como entrada. El **pipeline de curacion** que transita el material desde
crudo a publicado vive en `knowledge-spec §8`; esta seccion gobierna solo
el proceso de transformacion `DocHumano -> KORA/MD`, no la disciplina del
pipeline.

### 6.2 El proceso de koraficacion

La koraficacion es la transformacion `DocHumano -> KORA/MD`.

Traces to: `urn:kora:kb:05-governance-lattice` §2.2 (Koraficacion Functor K)

Propiedades:

- fiel
- comprimida
- promotora de estructura
- realizadora de superficie
- normalizadora
- idempotente
- invariante en idioma

### 6.3 Estrategia de ejecucion

La implementacion concreta **PUEDE** usar trabajo manual, una o
multiples pasadas LLM, siempre que el resultado satisfaga esta spec.

Cuando una familia tiene productor canonico declarado
(`knowledge-spec §9`), la generacion de artefactos **DEBE** delegarse al
productor; no existe una via alternativa soportada de emision para esa
familia. La edicion manual posterior **DEBE** marcarse explicitamente
para inhibir sobreescrituras.

### 6.4 Evaluacion del input

Antes de transformar, **DEBE** clasificarse el documento fuente segun:

- largo
- estructura existente
- densidad numerica
- presencia de tablas o listas
- idioma
- familia documental

Documentos grandes **DEBEN** segmentarse; documentos con alta carga
numerica **DEBEN** pasar verificacion mecanica fuerte.

### 6.5 Segmentacion

Para documentos grandes:

1. Los cortes **DEBEN** realizarse entre secciones naturales.
2. Cada segmento **DEBE** ser tematicamente coherente.
3. **NO DEBE** cortarse dentro de una tabla, lista o parrafo.

### 6.6 Transformacion

La transformacion **DEBE** ejecutarse en dos fases distintas:

1. Compresion semantica.
2. Realizacion superficial.

#### 6.6.1 Compresion semantica

Por cada segmento o documento completo:

1. Preservar toda cifra, fecha, plazo, condicion, excepcion y referencia
   legal.
2. Preservar el idioma del input.
3. Preservar toda lista y toda tabla sin perder items, filas o columnas.
4. Promover prosa comparativa o condicional a estructura.
5. Mantener orden semantico salvo que la normalizacion posterior mejore
   recuperacion sin perder verdad.
6. Eliminar grasa activa: introducciones, transiciones, hedging, saludos,
   retorica.
7. Aplicar las reglas T1-T7 de `§5.4`.

#### 6.6.2 Realizacion superficial

Antes de cerrar el artefacto:

1. Elegir forma final del contenido: prosa, lista o tabla.
2. Realizar headings finales recuperables y no truncados.
3. Verificar que la salida no suene a dump comprimido ni a serializacion
   de campos.
4. Reescribir headings o frases que queden mecanicos aunque la fidelidad
   sea correcta.
5. Aplicar invariantes de la familia documental correspondiente.

### 6.7 Ensamblaje

Si hubo segmentacion:

1. Los segmentos **DEBEN** concatenarse en orden.
2. El artefacto **DEBE** recibir un `#` unificado.
3. Las secciones primarias **DEBEN** quedar claras y recuperables.

### 6.8 Normalizacion

La normalizacion **PUEDE** reorganizar headings o fusionar secciones solo
si:

- mejora chunking y recuperacion
- elimina redundancia
- no agrega ni elimina informacion factual
- no degrada tablas o listas a prosa
- mejora realizacion superficial

### 6.9 Inyeccion de frontmatter

El frontmatter **DEBE** agregarse al final del proceso y cumplir `§3.1`.

### 6.10 Verificacion mecanica

Checks deterministas minimos:

- frontmatter valido
- URN formato correcto
- referencias validas
- idioma coherente
- cifras preservadas
- fechas preservadas
- listas y tablas preservadas
- tags minimo 3
- headings no truncados
- heading primario recuperable
- resumen obligatorio por familia cuando aplique
- ausencia de headings-campo prohibidos en KB publicada

### 6.11 Verificacion de fidelidad y calidad

Todo artefacto koraficado **DEBE** cerrar con verificacion de fidelidad y
calidad.

Proceso minimo:

1. Inventariar `skeleton/meat/fat`.
2. Enumerar hechos atomicos `N_hechos`.
3. Clasificar cada hecho como `preservado`, `comprimido`, `omitido` o
   `agregado`.
4. Calcular:
   - `FS = (preservados + comprimidos) / N_hechos * 100`
   - `CR = len(fuente) / len(salida)`
5. Auditar calidad de superficie:
   - headings recuperables
   - ausencia de labelese
   - ausencia de dumping estructural
   - naturalidad tecnica minima: la salida no incurre en ningun
     antipatron de `§5.4.2`.
6. Si `FS < 100%`, la koraficacion falla.
7. Si `CR < 1.5`, **DEBE** reducirse redundancia restante o justificarse
   por alta densidad informacional.
8. Si la calidad de superficie falla, la koraficacion falla aunque
   `FS=100%`.

### 6.12 Registro en catalogo

Todo artefacto nuevo o modificado **DEBE** quedar indexable por
`kora index`.

## 7. Invariantes

### 7.1 Preservacion de idioma

El idioma de salida **DEBE** coincidir con el idioma de la fuente salvo
que el artefacto explicite una traduccion como objetivo.

### 7.2 Independencia de chunk RAG

Cada `##` **DEBE** poder leerse con sujeto, alcance y dependencia
explicita cuando exista.

### 7.3 Preservacion de verdad (fidelidad absoluta)

`FS=100%` es el criterio de cierre de fidelidad.

### 7.4 Preservacion de estructuras y SSOT

Las estructuras existentes **NO DEBEN** degradarse y la duplicacion de
hechos **DEBE** eliminarse.

### 7.5 Calidad de superficie

La compresion maxima **NO DEBE** producir headings truncados, chunks
primarios pobres, labelese ni dumping estructural.

## 8. Versionado

- correccion editorial sin cambio semantico: patch
- adicion compatible de conocimiento o validacion: minor
- cambio incompatible del contrato de koraficacion, compresion o
  realizacion: major

## 9. Validacion

Esta tabla cubre solo invariantes de **formato** gobernados por esta
spec. Los invariantes de **tejido relacional** y **pipeline** viven en
`knowledge-spec §12`.

| Check | Criterio | Enforcement | Spec ref |
| --- | --- | --- | --- |
| Frontmatter valido | Cumple el envelope cerrado y usa `extensions` para metadata extra | schema | §3.1 |
| URN tripartito | `_manifest.urn` con regimen `urn:{ns}:{type}:{id}` y version fuera del URN | schema | §3.1, §4.1 |
| Referencias internas validas | URNs, headings y fragments resuelven | lint | §4.2 |
| Gramatica estructural | Jerarquia y chunks cumplen §5 | lint | §5.1-§5.4 |
| Sin grasa | No hay introducciones, transiciones ni hedging residual | manual | §5.3 |
| Fidelidad absoluta | `FS=100%` | manual | §5.5, §7.3 |
| Compresion razonable | `CR>1.5` o justificacion explicita | manual | §5.5 |
| Calidad de superficie | Sin headings truncados, labelese ni dumping | lint+manual | §5.4.2 |
| Heading recuperable | Cada `##` expresa sujeto o alcance recuperable | lint | §5.1 |
| Resumen obligatorio por familia | Familias que lo exigen incluyen `## Resumen` no vacio | lint | §5.6 |
| Headings-campo prohibidos | KB publicada no serializa campos como headings | lint | §5.4.2 |
| Estructuras preservadas | Tablas y listas no se degradan | manual | §7.4 |
| Catalogo derivado | El artefacto es indexable y regenerable por CLI | lint | §6.12 |

Checks de **tejido relacional** y **pipeline** (gobernados por
`knowledge-spec §12`): `urn-integrity`, `knowledge-zone`,
`kb-graph-cycles`, `supersedes-consistency`, `traces-requirements-semantics`.

Checks de **artefactos agenticos** (gobernados por `autoria-spec §14`):
`autoria-conformance`, `vector-laws`, `coalgebra-conformance`,
`fidelidad-agentskills`, `fidelidad-mastra`, `compromisos-eticos-no-todo`,
`skill-structure`.

## 10. Migracion

### 10.0 Contrato vigente v11

Cambios v10 → v11 (KORA v9, HITL 2026-05-20,
`urn:kora:kb:adr-kora-v9-separacion-descriptivo-prescriptivo-y-arnes`):

- **Regimen prescriptivo extraido**: §5.6.1.1-§5.6.1.9 (perfil `spec`
  con cristalizacion, RFC 2119, Traces to, elementos retoricos, prosa
  admisible, patron regla+ejemplo+traza, invariantes prescriptivos,
  template, auto-declaracion) migran a `urn:kora:kb:spec-md v1.0.0`.
- **§7.6** (integridad del perfil prescriptivo) migra a `spec-md §9 r6`.
- **§9 tabla de validacion**: 9 filas spec eliminadas (Keyword
  explicita, Trazabilidad oficial, Patron de regla, Consistencia
  interna, Auto-suficiencia, No-circularidad, Enforcement declarado,
  Template prescriptivo, Migracion en major). Migran a `spec-md §12`.
- **§1 Definicion** reformulada: md-spec gobierna solo el regimen
  descriptivo. La familia `spec` cumple ambos contratos: md-spec
  (envelope, gramatica, familias) + spec-md (invariantes prescriptivos).
- **§5.6.1** queda como subseccion **delegada**: la familia `spec`
  declara que sus invariantes prescriptivos viven en `spec-md`.
- **`urn:kora:kb:spec-md`** regresa al canon como nodo activo (estaba
  retirado/absorbido desde md-spec v8.0).

Que migrar:

- Refs cruzadas a `md-spec §5.6.1.X` (perfil spec) reapuntan a
  `spec-md §X` correspondiente.
- Refs a `md-spec §7.6` reapuntan a `spec-md §9 r6`.
- Refs a checks de validacion `Keyword explicita (spec)`, etc. usan
  ahora `spec-md §12`.

Que se preserva:

- Envelope, gramatica, telegrafizacion, fidelidad (§1-§5.5).
- Familias documentales descriptivas (§5.6 sin atomic ni perfil spec
  expandido).
- Koraficacion (§6).
- Invariantes generales (§7) y validacion descriptiva (§9).

### 10.0.1 Contrato vigente v10

Cambios v9 → v10 (retiro de familia `atomic` — directiva HITL del operador
2026-05-20, decision en `urn:kora:kb:adr-retiro-atomize-y-lecciones-koda`):

- **Familia `atomic` retirada** de §5.6: la fila desaparece de la tabla
  de familias canonicas.
- **§5.6.1 "Familia atomic: tipos y forma de proposicion"** eliminada
  (enum cerrado de 11 tipos de proposicion, forma minima de proposicion,
  9 reglas). El perfil prescriptivo `spec` que vivia en §5.6.2 ahora es
  §5.6.1.
- **§6.5 reglas 4-7** (segmentacion atomic blanda 15K chars / dura
  200 props / IDs Pxxx unicos globalmente) eliminadas.
- **§6.10 check ultimo** (atomic mechanical verification: Pxxx unicos,
  tipos enum cerrado, fuentes resolubles) eliminado.
- **§6.11 regla 9** (atomic dedup justification) eliminada.
- **§7.6 "Integridad de la familia atomic"** eliminada; el contenido de
  §7.7 ("Integridad del perfil prescriptivo spec") se renumera a §7.6.
- **§9 tabla validacion**: 6 filas atomic eliminadas (Indice atomic,
  Proposiciones atomic, Tipos atomic, Unicidad Pxxx, Segmentacion
  atomic, Dedup atomic).
- **Tag `atomic`** eliminado del frontmatter.

Que se preserva:

- El termino "Proposicion atomica" en §2 (definiciones) como termino del
  lexico KORA, no como invariante de familia.
- "Hechos atomicos" como adjetivo en §2 (Meat) y §6.11.
- El productor canonico `atomize` queda archivado en
  `governance/decisiones-archivadas/skills-retiradas/atomize/` con
  `status: retirado`. Su URN `urn:kora:artefacto:atomize` sigue
  resolviendo para trazabilidad.

### 10.0.1 Contrato vigente v9

- Todo el contrato semantico v8 se preserva sin quiebres.
- Las **reglas de pipeline** que vivian en `md-spec §3.1 r7-10` se
  movieron a `knowledge-spec §3-§4`. El envelope §3.1 r1-r7 (formato)
  permanece aqui; las nuevas reglas 8-10 declaran explicitamente la
  delegacion.
- Las **familias auxiliares** (`bok`, `source`, `source-alias`,
  `generic`) que el toolchain ya usaba en `validation.py` quedan
  documentadas en §5.6 como tabla separada de las canonicas; su origen
  es derivacion del toolchain, no declaracion editorial.
- La tabla §9 de validacion se reduce a invariantes de **formato**, y
  declara explicitamente que el resto vive en `knowledge-spec §12` y
  `autoria-spec §14`.
- `§6.1` se reduce a un puntero al pipeline gobernado por
  `knowledge-spec §8`.

### 10.1 Que migrar

- Artefactos KORA/MD existentes **no requieren** cambios de frontmatter,
  URN, lifecycle o status. La reorganizacion es doctrinal-doctrinal, no
  estructural.
- Referencias a `md-spec §3.1 r7` (namespace-directorio) se reapuntan a
  `knowledge-spec §3.2`.
- Referencias a `md-spec §3.1 r8-10` (lifecycle, status por directorio,
  procedimiento promote) se reapuntan a `knowledge-spec §4` y `§13`.
- Referencias a `md-spec §6.1` con detalle de pipeline se reapuntan a
  `knowledge-spec §8`.
- Checks de pipeline o tejido relacional que se citaran como `md-spec §9`
  se reapuntan a `knowledge-spec §12`.

### 10.2 Que se depreca

- Nada del contrato semantico de v8 se depreca.
- Las reglas absorbidas por `knowledge-spec` quedan **eliminadas** de
  esta spec para evitar duplicacion; la unica copia normativa es la de
  `knowledge-spec`.

### 10.3 Contrato vigente v8

(Resumen historico — el contrato vigente es v9; esto solo documenta el
salto v7 -> v8 absorbido y v8 -> v9 actual.)

- v8 absorbio el contrato prescriptivo de la retirada `spec-md v5.2.0`
  como perfil `spec` (§5.6.2).
- v8 agrego 7 invariantes prescriptivos (consistencia interna,
  auto-suficiencia, no-circularidad, idioma, enforcement declarado,
  template, auto-declaracion de precedencia).
- v8 agrego 9 checks especificos para el perfil `spec` en §9.

### 10.4 Contrato vigente v7

- URN conceptual tripartito, version fuera del URN.
- Koraficacion como functor fiel, comprimido e idempotente.
- Pipeline descentralizado en `_SCRIPTORIUM/{INBOX,REVIEW}/` ->
  `artifacts/knowledge/{ns}/...`.
- Fidelidad absoluta `FS=100%`.
- Compresion `CR>1.5` o justificacion explicita.
- Telegrafizacion con reglas T1-T7 y realizacion superficial.
- Familias documentales con invariantes propios.
- Verificacion mecanica y de fidelidad obligatorias.
- Lifecycle `borrador -> publicado -> deprecado`.

### 10.5 Que se preservo desde v6 y v7 hasta hoy

- URN conceptual tripartito sin version embebida.
- Reglas T1-T7 de compresion semantica.
- Familia `atomic` con productor canonico (`atomize`).
- Verificaciones §6.10 y §6.11 sin cambios.
- Perfil `spec` con todos sus invariantes §5.6.1.

Toda futura transicion major **DEBE** documentar aqui: (1) que cambio,
(2) que migrar, y (3) que se depreca.
