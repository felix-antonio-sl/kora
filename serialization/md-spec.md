---
_manifest:
  urn: "urn:kora:kb:md-spec"
  provenance:
    created_by: "FS"
    created_at: "2026-03-09"
    source: "KORA categorical-foundations 05, KORA/Gobernanza v4.3.0, refactor del contrato de compresion y realizacion superficial; v7 agrega familia atomic con productor canonico atomize; v7.1 fusiona tipos de artefacto y familias documentales; v8.0 absorbe el contrato prescriptivo de la retirada spec-md v5.2.0 como perfil normativo de la familia `spec`, restaurando cristalizacion, RFC 2119, Traces to, patron regla+ejemplo+traza e invariantes de consistencia interna, auto-suficiencia y no-circularidad"
version: "8.1.0"
status: publicado
tags: [markdown, conocimiento, rag, koraficacion, fidelidad, atomic, prescriptivo, cristalizacion, rfc2119]
lang: es
extensions:
  kora:
    family: spec
relations:
  depends:
    - "urn:kora:kb:gobernanza"
  cites:
    - "urn:kora:kb:05-governance-lattice"
---

# KORA/MD v8.1.0

## 1. Definicion

KORA/MD es el formato base de artefactos textuales del ecosistema KORA. Gobierna dos regimenes pragmaticos sobre un mismo envelope:

- **Descriptivo** — artefactos que describen hechos, procedimientos o referencias (conocimiento, manuales, corpus, notas).
- **Prescriptivo** — artefactos que gobiernan comportamientos, contratos y validaciones (specs, protocolos, workflows normativos).

Ambos regimenes comparten frontmatter (§3.1), gramatica estructural (§5.1-§5.4), topologia de direccionamiento (§4), preservacion de verdad (§5.5) y ciclo de koraficacion (§6). El regimen se declara via `familia documental` (§5.6); el perfil `spec` agrega invariantes prescriptivos especificos (§5.6.2).

KORA/MD optimiza almacenamiento, indexacion y recuperacion para humanos y LLMs via RAG sin sacrificar verdad factual, y preserva la fuerza normativa de las specs sin ambiguedad.

### 1.1 Alcance y audiencia

Regimen **descriptivo**: leyes (como corpus de referencia), manuales, guias, corpus de conocimiento, notas tecnicas, catalogos.

Regimen **prescriptivo**: specs constitucionales, protocolos, workflows normativos, contratos de API, politicas.

La audiencia primaria son runtimes, pipelines de recuperacion y agentes que consumen ley operativa. La audiencia secundaria son humanos que curan el corpus, diseñan, auditan o evolucionan el ecosistema.

Todo documento `spec` de KORA **DEBE** redactarse conforme a esta especificacion bajo el perfil `spec` (§5.6.2). Un documento descriptivo **NO DEBE** gobernarse por los invariantes prescriptivos del perfil `spec`.

## 2. Definiciones

| Termino                 | Definicion                                                                                                 |
| ----------------------- | ---------------------------------------------------------------------------------------------------------- |
| Artefacto KORA/MD       | Archivo Markdown con frontmatter KORA y cuerpo descriptivo                                                 |
| Koraficacion            | Transformacion `DocHumano -> KORA/MD` que preserva verdad y elimina entropia comunicativa                  |
| Chunk RAG               | Unidad primaria de recuperacion delimitada por `##`                                                        |
| Skeleton                | Estructura del documento: titulo, headings, tablas, listas, jerarquia                                      |
| Meat                    | Hechos atomicos que deben preservarse: cifras, fechas, condiciones, excepciones, referencias, dependencias |
| Fat                     | Retorica, hedging, transiciones y relleno editorial eliminable                                             |
| Realizacion superficial | Eleccion de la forma final visible del conocimiento: heading, prosa, lista o tabla                         |
| Labelese                | Salida que suena a serializacion de campos: `Asunto`, `Contenido`, `Tipo`, `Path`, etc.                    |
| FS                      | Fidelity Score. Porcentaje de hechos preservados o comprimidos sin perdida semantica                       |
| CR                      | Compression Ratio. Longitud fuente / longitud salida                                                       |
| SSOT                    | Un hecho, un lugar                                                                                         |
| Proposicion atomica     | Hecho verificable minimo autocontenido, con tipo, texto comprimido y ancla de fuente resoluble             |
| Productor canonico      | Herramienta autorizada para generar artefactos de una familia con garantia de invariantes                  |
| Documento `spec`        | Artefacto agentico de familia documental `spec`: define lo que debe ser (reglas, contratos, validaciones). Alias historico: "documento prescriptivo". |
| Keyword (RFC 2119)      | Palabra reservada que fija fuerza normativa: DEBE, NO DEBE, DEBERIA, NO DEBERIA, PUEDE. Enum cerrado.      |
| Regla                   | Oracion con keyword RFC 2119 y semantica operativa univoca                                                 |
| Cristalizacion          | Proceso `Decisiones + Practicas + Restricciones -> regla explicita con una sola lectura valida`            |
| Rationale               | Explicacion auxiliar no normativa sobre motivacion; no introduce obligaciones                              |
| Traces to               | Puente entre una regla operacional y su justificacion en la Formal Layer oficial                           |
| Auto-suficiencia        | Propiedad de una regla que puede entenderse con su propio contexto local, sin lectura telepatica del repo  |
| No-circularidad         | Propiedad de una regla que no se justifica solo remitiendo a otra regla igual de opaca                     |

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
status: borrador|publicado|deprecado  # valores en espanol; ejecutables agregan `activo` y `retirado`
tags: [{tag1}, {tag2}, {tag3}]
lang: "{iso-639-1}"
extensions: {}
---
```

Reglas:

1. El regimen de identidad es conceptual: URN tripartito + version fuera del URN.
2. El sobre base es cerrado.
3. Metadata adicional **DEBE** residir en `extensions.{namespace}`.
4. `tags` **DEBE** contener al menos 3 tags semanticos.
5. `lang` describe el idioma del cuerpo.
6. `source` describe la procedencia humana o documental del conocimiento.
7. Cuando el artefacto reside bajo `artifacts/knowledge/`, el namespace en el URN **DEBE** coincidir con el primer subdirectorio bajo `artifacts/knowledge/`. Enforcement: lint. Los artefactos que viven fuera de `artifacts/knowledge/` (specs en `governance/`, `ontology/`, `serialization/` o `runtime/`; workspaces en `artifacts/agents/`; habilidades en `artifacts/skills/`; outputs en `BUILD/`) derivan su namespace de la topologia declarada por la spec canonica que los gobierna; para ellos esta regla no aplica.
8. El valor de `status` **DEBE** respetar el regimen de lifecycle correspondiente (`gobernanza §5`), declarado en idioma español:
   - artefactos descriptivos (KORA/MD en `artifacts/knowledge/` y specs): `borrador -> publicado -> deprecado`.
   - artefactos agenticos productivos (toda `forma_material` de `autoria-spec`: habilidad, subagente, agente-propiamente-tal, agente-plataforma): `borrador -> activo -> deprecado -> retirado`.
   Las transiciones inversas son invalidas en ambos regimenes.
9. `artifacts/knowledge/` solo acepta artefactos con `status: publicado` o `status: deprecado`. Artefactos con `status: borrador` **DEBEN** residir en `artifacts/knowledge/_SCRIPTORIUM/INBOX/` (material pre-categorial) o `artifacts/knowledge/_SCRIPTORIUM/REVIEW/` (drafts en revision). Enforcement: schema.
10. La transicion a `status: publicado` (o `status: activo` para ejecutables) **DEBE** pasar por `kora promote` u otro procedimiento equivalente que verifique verificacion mecanica (§6.10), verificacion de fidelidad (§6.11) y ausencia de conflictos de namespace (regla 7).
11. Cuando `source` referencia archivos del monorepo, la ruta **DEBERIA** ser resoluble desde la raiz del repo. Enforcement: manual.

### 3.2 Capa 2: Cuerpo de conocimiento

El cuerpo **DEBE** privilegiar estructura recuperable sobre prosa ornamental.

Permitido:

- headings
- listas
- tablas
- definiciones
- formulas
- ejemplos minimos

Desaconsejado:

- transiciones narrativas
- relleno editorial
- referencias vagas sin ancla

## 4. Topologia de direccionamiento

### 4.1 Estructura tripartita

Todo artefacto KORA/MD **DEBE** usar un URN `urn:{namespace}:{type}:{id}`.

Reglas:

1. La version **NO DEBE** incluirse en el URN.
2. Las referencias KORA **NO DEBEN** incluir version en artefactos conceptuales.
3. El filesystem con manifests es la fuente de verdad; el catalogo es una vista derivada.

### 4.2 Tipos de referencia

Tipos permitidos:

- interna: `[-> Seccion]`
- KORA: `[Descripcion](urn:{ns}:{type}:{id})`
- externa: `[Descripcion](https://...)`

Reglas:

1. Las referencias internas **DEBEN** apuntar a headings o fragments resolubles.
2. Los fragments `#...` **DEBERIAN** usarse solo cuando aportan precision real.
3. El catalogo **DEBERIA** mantenerse completo y regenerable via `kora index`.

## 5. Gramatica estructural

### 5.1 Jerarquia de encabezados = esqueleto semantico

| Nivel  | Rol semantico                |
| ------ | ---------------------------- |
| `#`    | Titulo del artefacto         |
| `##`   | Seccion primaria recuperable |
| `###`  | Subtopico o componente       |
| `####` | Detalle atomico              |

Reglas:

1. La profundidad **NO DEBE** exceder `####`.
2. Cada `##` **DEBE** ser recuperable de forma casi aislada.
3. Los headings **DEBEN** ser compactos y semanticamente recuperables.
4. Un `###` **NO DEBE** existir sin un `##` padre.
5. Un heading **NO DEBE** terminar truncado con `...`.
6. Un heading primario **DEBE** expresar sujeto o alcance recuperable; el mero ordinal no basta.

### 5.2 Elementos de contenido

| Elemento | Uso permitido                                   | Funcion prohibida                        |
| -------- | ----------------------------------------------- | ---------------------------------------- |
| Negrita  | definiciones, terminos clave                    | enfasis decorativo                       |
| Cursiva  | termino tecnico o extranjero                    | enfasis estilistico                      |
| `codigo` | URNs, ids, comandos, literales                  | resaltado general                        |
| Lista    | enumeracion, procedimiento o desglose normativo | prosa fragmentada sin valor estructural  |
| Tabla    | comparacion, condiciones, matrices, catalogos   | dumping decorativo o serializacion cruda |

### 5.3 Elementos prohibidos (grasa)

Cada elemento de la siguiente lista **NO DEBE** incluirse en KORA/MD:

- introducciones tipo "En este documento veremos..."
- transiciones tipo "A continuacion", "Por otro lado"
- hedging tipo "probablemente", "en general", "suele"
- preguntas retoricas
- saludos y cierres
- duplicacion de hechos

### 5.4 Telegrafizacion = compresion semantica estructural

La escritura KORA/MD **DEBE** ser telegrafica. La telegrafizacion no significa reducir palabras por si mismas; significa eliminar redundancia y promover la forma mas densa que preserve verdad y recuperacion.

Definicion operativa:

- comprimir relaciones redundantes
- eliminar verbos de enlace y marcadores discursivos innecesarios
- promover prosa comparativa o condicional a listas o tablas
- evitar repetir sujeto, alcance o contexto ya fijados por el heading
- preservar siempre `skeleton` y `meat`

Reglas de transformacion obligatorias:

| N°  | Regla                                               | Patron fuente                                                  | Transformacion                             |
| --- | --------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------ |
| T1  | Eliminar perifrasis y verbos de enlace              | "se podran traspasar recursos desde X"                         | "Traspaso permitido desde X"               |
| T2  | Nominalizar acciones cuando mejore densidad         | "deberan informar trimestralmente"                             | "Informe trimestral obligatorio"           |
| T3  | Colapsar subordinadas condicionales a lista/tabla   | "cuando el monto sea superior a X, se debera..."               | Tabla `Condicion \| Resultado \| Base`     |
| T4  | Eliminar marcadores discursivos                     | "asimismo", "a continuacion", "por otro lado", "cabe señalar"  | Eliminar sin reemplazo                     |
| T5  | Comprimir enumeraciones embebidas en prosa a listas | "podran financiar A, B y C"                                    | Lista con marcadores                       |
| T6  | Eliminar sujetos redundantes                        | "El Gobierno Regional debera... El Gobierno Regional podra..." | Sujeto una vez en heading, luego implicito |
| T7  | Promover comparaciones y condiciones a tablas       | Parrafo con multiples "si X entonces Y"                        | Tabla `Condicion \| Resultado`             |

Patrones estructurales obligatorios:

- Definiciones: `**Termino** - descripcion compacta`
- Condiciones: tabla `Condicion | Resultado | Base`
- Procedimientos: lista secuencial numerada
- Comparaciones: tabla, nunca parrafo si la relacion ya es matricial
- Enumeraciones: lista con marcadores, nunca embebidas en prosa

### 5.4.1 Contraejemplos normativos

Los siguientes pares muestran la transformacion esperada. El patron ✗ **NO DEBE** aparecer en KORA/MD; el patron ✓ **DEBE** usarse en su lugar.

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
2. Un heading primario **DEBE** expresar sujeto o alcance recuperable, aunque no sea un sintagma nominal puro.
3. Una salida **NO DEBE** sonar a serializacion de campos (`Asunto`, `Contenido`, `Tipo`, `Path`, `Artefactos`, etc.), salvo que la familia documental lo exija de forma explicita.
4. Listas y tablas solo son validas si mejoran recuperacion o comparabilidad; si degradan legibilidad sin aportar estructura, **DEBE** preferirse prosa tecnica breve.
5. La nominalizacion es valida solo si no destruye naturalidad tecnica.
6. La compresion **NO DEBE** producir labelese, headings-campo, ni frases mecanicas.

Contraejemplos de mala realizacion superficial:

**Contraejemplo 4: Heading truncado**

✗ Incorrecto:

> `## Glosa 03 - Los recursos de los presupuestos de inversion regional no podran...`

✓ Correcto:

> `## Glosa 03 - Restriccion de uso de recursos de inversion regional`

**Contraejemplo 5: Heading-campo**

✗ Incorrecto:

> `#### Titulo`
>
> `#### Path`
>
> `#### Artefactos`

✓ Correcto:

> `### Introduccion y Fundamentos`
>
> Tabla de artefactos con columnas `id | urn | titulo | resumen`

**Contraejemplo 6: Lista que reemplaza indebidamente una frase tecnica simple**

✗ Incorrecto:

> `#### Alcance`
>
> - Convenios
> - con municipios
> - permitidos

✓ Correcto:

> `#### Alcance`
>
> Convenios de mandato con municipios permitidos.

**Contraejemplo 7: Tabla usada como pseudo-dump**

✗ Incorrecto:

> Tabla `Campo | Valor` para serializar `Tipo`, `Path`, `Status`, `Source_ID` sin valor recuperable.

✓ Correcto:

> Tabla solo cuando exista comparacion, matriz, catalogo o conjunto de registros.

### 5.5 Preservacion de verdad (prueba acida)

La compresion **NO DEBE** sacrificar contenido informativo.

Traces to: `urn:kora:kb:05-governance-lattice` §2.2 (Koraficacion Functor K)

Regla acida:

- si al eliminar texto cambia solo tono o fluidez, **DEBE** eliminarse
- si al eliminar texto desaparece una condicion, umbral, excepcion, fecha, cifra, dependencia o referencia, **NO DEBE** eliminarse

Metafora operativa:

- `skeleton`: preservar estructura
- `meat`: preservar siempre
- `fat`: eliminar siempre

Metricas:

- `FS=100%` es el objetivo obligatorio de fidelidad
- `CR>1.5` es el objetivo de compresion para koraficaciones normales
- `CR<1.5` solo es aceptable si `FS=100%`, no queda grasa eliminable y la realizacion superficial sigue siendo valida

### 5.6 Familias documentales

Una **familia documental** es un perfil del formato KORA/MD — no un formato
distinto. Todos los artefactos KORA/MD cumplen el contrato base (§§1-5); cada
familia agrega invariantes que su estructura de dominio requiere. Esta lista
es la **fuente unica** de clasificacion de artefactos KORA/MD, reemplazando
la dualidad anterior "tipos" (en `knowledge-spec`) vs "familias" (en esta
spec). `knowledge-spec §3` referencia esta tabla como autoridad.

| Familia      | Invariantes                                                                                                                 |
| ------------ | --------------------------------------------------------------------------------------------------------------------------- |
| `spec`       | Familia prescriptiva. Invariantes completos en §5.6.2 (cristalizacion, RFC 2119, `Traces to:`, patron regla+ejemplo+traza, consistencia interna, auto-suficiencia, no-circularidad, enforcement declarado). URN `urn:{ns}:kb:{id}`; reside en las capas normativas (`governance/`, `ontology/`, `serialization/`, `runtime/`), no en `artifacts/knowledge/`. |
| `guide`      | Manual o guia operativa; prosa tecnica controlada; ejemplos concretos vinculados a headings; `## Resumen` recomendado        |
| `normative`  | `##` con asunto semantico; condiciones, excepciones y matrices promovidas a listas/tablas; no dumps de numerales sin asunto |
| `glossary`   | Buckets recuperables; sin duplicados no resueltos; alias explicitos                                                          |
| `faq`        | `##` por pregunta; respuesta autocontenida; orden por frecuencia o tema                                                     |
| `catalog`    | Entradas tabuladas; columnas minimas `id | urn | titulo | resumen`; indexable por CLI                                        |
| `cq_catalog` | `## Resumen` obligatorio y no vacio; dominios como `##`; scaffold en idioma del documento; subperfil de `catalog`            |
| `inventory`  | Puede retener material operativo; si `publication_class=control`, queda fuera de KB publicada                               |
| `organigram` | Dependencias estructurales explicitas; no headings-campo para representar jerarquia                                         |
| `atomic`     | `## Indice de fuentes` obligatorio y no vacio; cada `##` agrupa proposiciones por dominio o source_file; cada proposicion tiene ID `Pxxx` unico, tipo del enum cerrado, texto comprimido y al menos una fuente resoluble; enum cerrado de tipos (`§5.6.1`); FS=100% sobre cifras/fechas/excepciones originales **y sobre la particion semantica relevante del documento**: no se permite colapsar hechos distinguibles en una proposicion mas general solo para bajar conteo; dedup multi-source permitido solo para equivalencia semantica real; conflicto semantico entre fuentes -> tipo `tension`; referencia operativa de ~15.000 caracteres por artefacto y maximo duro de 200 proposiciones; si el corte estructural lo exige, se permite quedar levemente por debajo o por encima de la referencia |
| `note`       | Nota tecnica compacta; al menos un `##` tematico; `## Resumen` opcional cuando el tamaño lo vuelve redundante                |
| `adr`        | Architecture Decision Record. Subperfil de `note`. **Frontmatter extendido obligatorio**: `extensions.kora.adr.{contexto, alternativas, factorizacion_elegida, consecuencias, estado}`. Cuerpo con secciones fijas: `## Contexto`, `## Alternativas consideradas`, `## Decision`, `## Consecuencias`, `## Trazabilidad`. Decision se registra como factorizacion categorica: `decision = g ∘ f` donde `f` es la restriccion operativa y `g` el morfismo elegido entre alternativas. Estados: `propuesta -> aceptada -> (superseded|deprecada|retirada)`. Trazabilidad: `relations.cites` apunta a las alternativas consideradas aunque no se hayan adoptado. |

Clasificacion de familia:

La familia de un artefacto **DEBE** identificarse por uno de estos mecanismos, en orden de precedencia:

1. `extensions.{namespace}.family` explicito en el frontmatter.
2. Convencion de directorio (e.g., `glossaries/`, `normative/`, `atomic/`).
3. Clasificacion manual del curador durante koraficacion.
4. Productor canonico declarado (ver `knowledge-spec §12`): si existe, el productor fija la familia al emitir el artefacto.

Una familia **PUEDE** heredar invariantes de otra declarando su relacion como
subperfil (ej. `cq_catalog` subperfil de `catalog`). La herencia es estrictamente
aditiva: el subperfil no puede relajar invariantes del perfil base.

### 5.6.1 Familia `atomic`: tipos y forma de proposicion

La familia `atomic` tiene enum cerrado de tipos de proposicion:

| Tipo          | Semantica                                         |
| ------------- | ------------------------------------------------- |
| `requirement` | algo que se debe cumplir                          |
| `definition`  | que es algo                                       |
| `rule`        | como funciona algo                                |
| `exclusion`   | que no aplica o esta prohibido                    |
| `constraint`  | limite numerico o temporal                        |
| `obligation`  | accion que alguien debe realizar                  |
| `permission`  | algo que esta permitido                           |
| `deadline`    | plazo especifico                                  |
| `tension`     | contradiccion o ambiguedad entre fuentes          |
| `fact`        | dato verificable sin carga normativa              |
| `scope`       | alcance o ambito de aplicacion                    |

Forma minima de proposicion (dentro de un `##` de la familia):

- una fuente:
  ```
  - **P042** · `exclusion` · texto atomico verificable · [src](urn:...#loc)
  ```
- varias fuentes (dedup aplicado):
  ```
  - **P042** · `exclusion` · texto atomico verificable
    - [src-a](urn:...#loc)
    - [src-b](urn:...#loc)
  ```

Reglas:

1. El ID `Pxxx` **DEBE** ser unico en el artefacto; en artefactos segmentados, el `indice` **DEBE** mantener la unicidad global.
2. El tipo **DEBE** pertenecer al enum cerrado.
3. El texto **DEBE** ser autocontenido y preservar cifras, fechas, nombres propios, leyes y decretos sin compresion destructiva.
4. Cada proposicion **DEBE** tener al menos una fuente resoluble.
5. La compresion **NO DEBE** fusionar afirmaciones semanticamente distintas aunque pertenezcan al mismo parrafo, ejemplo o argumento. Si una fuente contiene varios hechos distinguibles y reutilizables, **DEBEN** emitirse como proposiciones separadas.
6. Eliminar paratexto irrelevante (blurbs, copyright, TOC, boilerplate editorial) **ES OBLIGATORIO**, pero esa eliminacion **NO CUENTA** como licencia para comprimir el contenido sustantivo del cuerpo del documento.
7. Si dos fuentes afirman el mismo hecho, se dedup en una sola proposicion con cita multiple.
8. Si dos fuentes se contradicen sobre el mismo hecho, **NO** se dedup: se emite una proposicion `tension` que nombra ambas posiciones.
9. Extensiones del frontmatter **DEBEN** declarar `extensions.kora.family: atomic` y, cuando aplique, `extensions.kora.atomic.source_corpus`, `extensions.kora.atomic.n_propositions` y `extensions.kora.atomic.producer`.

### 5.6.2 Perfil `spec`: invariantes prescriptivos

La familia `spec` absorbe el contrato prescriptivo del ecosistema KORA. Todo documento `spec` **DEBE** cumplir, ademas del contrato base de KORA/MD, los invariantes de esta seccion.

#### 5.6.2.1 Proceso de cristalizacion

La cristalizacion transforma decisiones, practicas y restricciones implicitas en reglas explicitas con una sola lectura valida.

Traces to: `urn:kora:kb:05-governance-lattice` §2.3 (Crystallization Functor C)

Entrada:

- decisiones de diseño
- practicas existentes
- restricciones tecnicas, organizacionales o legales

Salida:

- documento prescriptivo con reglas explicitas, rationale y validacion

Propiedades del funtor de cristalizacion:

1. **Cristalizador** — lo implicito se vuelve regla explicita.
2. **Formalizador** — cada regla queda con una lectura operativa univoca.
3. **Desambiguador** — el hedging y la vaguedad se eliminan.
4. **Ejemplificador** — las reglas complejas se anclan con `Correcto:` / `Incorrecto:`.

#### 5.6.2.2 Lenguaje de obligacion (RFC 2119)

Keywords normativas permitidas (enum cerrado):

- **DEBE**
- **NO DEBE**
- **DEBERIA**
- **NO DEBERIA**
- **PUEDE**

Reglas:

1. Toda obligacion importante en un documento `spec` **DEBE** usar una keyword RFC 2119.
2. El hedging normativo ("probablemente", "seria bueno", "idealmente") **NO DEBE** reemplazar una keyword.
3. Las keywords en español **DEBEN** escribirse en mayusculas.
4. La equivalencia inglesa (MUST, MUST NOT, SHOULD, SHOULD NOT, MAY) **PUEDE** aparecer en la primera mencion, no en todas.

#### 5.6.2.3 Convencion de trazabilidad

Una regla con justificacion formal oficial **DEBERIA** incluir una linea:

```markdown
Traces to: `urn:kora:kb:{slug}` §{seccion} ({teorema})
```

Reglas:

1. `Traces to:` **DEBE** apuntar solo a la Formal Layer oficial (`artifacts/knowledge/kora/categorical-foundations/`), usando el URN canonico del artefacto formal (`urn:kora:kb:{slug}`) seguido del numero de seccion y, opcionalmente, el nombre del teorema.
2. No se admite path relativo (`formal/05`) ni alias no resolubles: la identidad del artefacto formal se expresa por URN (`gobernanza §4.3`).
3. Una regla pragmatica **NO DEBE** fingir respaldo formal: si la justificacion es pragmatica, se usa `Rationale:`.
4. `Rationale:` **PUEDE** explicar motivos conceptuales o pragmaticos, pero **NO DEBE** introducir obligaciones nuevas.
5. La ausencia de `Traces to:` no debilita la fuerza normativa de una regla.

Traces to: `urn:kora:kb:05-governance-lattice` §3.2 (Traceability Functor)

Rationale: el URN canonico es identidad estable (Yoneda); los paths relativos mezclan identidad con ubicacion fisica y se rompen al reorganizar la Formal Layer.

#### 5.6.2.4 Elementos retoricos normativos

El perfil `spec` admite tres elementos retoricos normativos adicionales a los tipograficos de §5.2:

| Elemento                    | Uso permitido                             | Funcion prohibida               |
| --------------------------- | ----------------------------------------- | ------------------------------- |
| `Correcto:` / `Incorrecto:` | anclar la interpretacion de una regla     | decoracion                      |
| `Rationale:`                | registrar motivacion no normativa         | introducir deberes nuevos       |
| Tabla de validacion         | checks y enforcement declarativo          | listado estetico sin criterio   |

#### 5.6.2.5 Prosa explicativa admisible

La prosa explicativa en un documento `spec` **PUEDE** existir solo cuando cumple una de estas cuatro funciones normativas (lista exhaustiva):

1. justificar una regla
2. prevenir ambiguedad
3. contextualizar una restriccion
4. advertir un limite del enforcement

Prosa que no satisface ninguna de estas cuatro funciones es grasa y **DEBE** eliminarse conforme a §5.3.

#### 5.6.2.6 Patron obligatorio: regla + ejemplo + traza

Toda regla con mas de una condicion, alcance no obvio, o riesgo de interpretacion divergente **DEBE** seguir este patron:

1. Regla normativa con keyword RFC 2119.
2. `Correcto:` / `Incorrecto:` cuando la regla admita mala lectura.
3. `Traces to:` si la regla tiene respaldo formal oficial; `Rationale:` si la justificacion es pragmatica.

Reglas:

1. La ausencia de `Traces to:` no debilita la fuerza normativa.
2. `Rationale:` **NO DEBE** introducir obligaciones nuevas.
3. Un ejemplo **NO DEBE** reemplazar la regla; la ancla.

Ejemplo:

```markdown
Toda regla pragmatica **DEBE** declararse con keyword explicita.

Correcto: `La herramienta declara su nivel de enforcement en tabla de validacion.`
Incorrecto: `Seria bueno indicar como se verifica.`
Rationale: La auditabilidad requiere distinguir schema, lint, runtime y manual.
```

#### 5.6.2.7 Invariantes prescriptivos

Ademas de los invariantes generales de §7, un documento `spec` **DEBE** cumplir:

1. **Consistencia interna** — no contiene reglas incompatibles entre si sin una clausula de precedencia o excepcion explicita.
2. **Auto-suficiencia de la regla** — toda regla importante puede entenderse con su propio contexto local, sin depender de una lectura telepatica del repositorio. (Esta invariante es a nivel de *regla*; §7.2 es a nivel de *chunk `##`*.)
3. **No-circularidad** — una regla **NO DEBE** justificarse solo remitiendo a otra regla igual de opaca. Si depende de otra, la dependencia **DEBE** aclarar que agrega o restringe.
4. **Preservacion de idioma y anglicismos** — el documento mantiene idioma consistente. Los anglicismos **PUEDEN** usarse si nombran terminos tecnicos inevitables, pero **NO DEBEN** reemplazar una regla ya expresable en español.
5. **Enforcement declarado** — toda tabla de validacion **DEBE** incluir columna `Enforcement` con valor de `gobernanza §7` (`schema`, `lint`, `runtime`, `eval`, `manual`).

#### 5.6.2.8 Template esqueleto minimo

Todo documento `spec` nuevo **DEBERIA** arrancar desde este esqueleto. Las sub-reglas marcadas con **DEBE** dentro del esqueleto son obligatorias independientemente del caracter recomendatorio del template:

1. `## 1. Definicion` (incluye alcance y audiencia).
2. `## 2. Definiciones` de terminos usados normativamente.
3. `## 3-N. Secciones normativas` numeradas secuencialmente.
4. `## N+1. Invariantes`.
5. `## N+2. Validacion` (tabla con `Enforcement` obligatoria).
6. `## N+3. Ejemplos` (opcional).
7. `## N+4. Migracion` — **DEBE** incluirse en major bumps; opcional en minor/patch. En major bumps documenta: (1) que cambio, (2) que migrar, (3) que se depreca.

#### 5.6.2.9 Invariante de auto-declaracion

El propio documento `spec` **DEBE** declarar al inicio su **precedencia** en la jerarquia de specs, conforme a `gobernanza §3.4` (regla de especializacion). La declaracion **PUEDE** ser el frontmatter `relations.depends` o una seccion `## Precedencia` explicita.

## 6. Koraficacion

### 6.1 Entrada

Cualquier documento originalmente escrito para humanos **PUEDE** usarse como entrada. Todo documento que ingrese al monorepo para koraficacion **DEBE** transitar por el pipeline descentralizado definido en `knowledge-spec §6`:

```
artifacts/knowledge/_SCRIPTORIUM/INBOX/  ->  artifacts/knowledge/_SCRIPTORIUM/REVIEW/  ->  artifacts/knowledge/{ns}/...
```

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

La implementacion concreta **PUEDE** usar trabajo manual, una o multiples pasadas LLM, siempre que el resultado satisfaga esta spec.

Cuando una familia tiene productor canonico declarado (`knowledge-spec §12`), la generacion de artefactos **DEBE** delegarse al productor; no existe una via alternativa soportada de emision para esa familia. La edicion manual posterior **DEBE** marcarse explicitamente para inhibir sobreescrituras.

### 6.4 Evaluacion del input

Antes de transformar, **DEBE** clasificarse el documento fuente segun:

- largo
- estructura existente
- densidad numerica
- presencia de tablas o listas
- idioma
- familia documental

Documentos grandes **DEBEN** segmentarse; documentos con alta carga numerica **DEBEN** pasar verificacion mecanica fuerte.

### 6.5 Segmentacion

Para documentos grandes:

1. Los cortes **DEBEN** realizarse entre secciones naturales.
2. Cada segmento **DEBE** ser tematicamente coherente.
3. **NO DEBE** cortarse dentro de una tabla, lista o parrafo.

Para familia `atomic`, segmentacion operativa:

4. Si el artefacto atomic supera 200 proposiciones, **DEBE** emitirse un artefacto `atomic-{slug}-index` y N artefactos `atomic-{slug}-{NN}`.
5. La referencia de segmentacion para familia `atomic` es ~15.000 caracteres por artefacto, pero **NO** es un limite rigido: el corte **DEBE** hacerse en la frontera estructural mas cercana que preserve coherencia tematica.
6. El indice **DEBE** contener tabla `Segmento | Rango Pxxx | Dominios` y resolver URNs a cada segmento.
7. Los IDs `Pxxx` **DEBEN** ser unicos a traves del indice + todos los segmentos (numeracion global).

### 6.6 Transformacion

La transformacion **DEBE** ejecutarse en dos fases distintas:

1. Compresion semantica.
2. Realizacion superficial.

#### 6.6.1 Compresion semantica

Por cada segmento o documento completo:

1. Preservar toda cifra, fecha, plazo, condicion, excepcion y referencia legal.
2. Preservar el idioma del input.
3. Preservar toda lista y toda tabla sin perder items, filas o columnas.
4. Promover prosa comparativa o condicional a estructura.
5. Mantener orden semantico salvo que la normalizacion posterior mejore recuperacion sin perder verdad.
6. Eliminar grasa activa: introducciones, transiciones, hedging, saludos, retorica.
7. Aplicar las reglas T1-T7 de `§5.4`.

#### 6.6.2 Realizacion superficial

Antes de cerrar el artefacto:

1. Elegir forma final del contenido: prosa, lista o tabla.
2. Realizar headings finales recuperables y no truncados.
3. Verificar que la salida no suene a dump comprimido ni a serializacion de campos.
4. Reescribir headings o frases que queden mecanicos aunque la fidelidad sea correcta.
5. Aplicar invariantes de la familia documental correspondiente.

### 6.7 Ensamblaje

Si hubo segmentacion:

1. Los segmentos **DEBEN** concatenarse en orden.
2. El artefacto **DEBE** recibir un `#` unificado.
3. Las secciones primarias **DEBEN** quedar claras y recuperables.

### 6.8 Normalizacion

La normalizacion **PUEDE** reorganizar headings o fusionar secciones solo si:

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
- para familia `atomic`: IDs Pxxx unicos, tipos dentro del enum cerrado, cada proposicion con ≥1 fuente resoluble

### 6.11 Verificacion de fidelidad y calidad

Todo artefacto koraficado **DEBE** cerrar con verificacion de fidelidad y calidad.

Proceso minimo:

1. Inventariar `skeleton/meat/fat`.
2. Enumerar hechos atomicos `N_hechos`.
3. Clasificar cada hecho como `preservado`, `comprimido`, `omitido` o `agregado`.
4. Calcular:
   - `FS = (preservados + comprimidos) / N_hechos * 100`
   - `CR = len(fuente) / len(salida)`
5. Auditar calidad de superficie:
   - headings recuperables
   - ausencia de labelese
   - ausencia de dumping estructural
   - naturalidad tecnica minima: la salida no incurre en ningun antipatron de `§5.4.2` (heading truncado, heading-campo, lista que reemplaza frase simple, tabla como pseudo-dump)
6. Si `FS < 100%`, la koraficacion falla.
7. Si `CR < 1.5`, **DEBE** reducirse redundancia restante o justificarse por alta densidad informacional.
8. Si la calidad de superficie falla, la koraficacion falla aunque `FS=100%`.
9. En familia `atomic`, una reduccion fuerte del numero de proposiciones respecto del inventario inicial de hechos **DEBE** justificarse mediante dedup real o descarte de paratexto; no es valida si proviene de fusionar hechos distinguibles.

### 6.12 Registro en catalogo

Todo artefacto nuevo o modificado **DEBE** quedar indexable por `kora index`.

## 7. Invariantes

### 7.1 Preservacion de idioma

El idioma de salida **DEBE** coincidir con el idioma de la fuente salvo que el artefacto explicite una traduccion como objetivo.

### 7.2 Independencia de chunk RAG

Cada `##` **DEBE** poder leerse con sujeto, alcance y dependencia explicita cuando exista.

### 7.3 Preservacion de verdad (fidelidad absoluta)

`FS=100%` es el criterio de cierre de fidelidad.

### 7.4 Preservacion de estructuras y SSOT

Las estructuras existentes **NO DEBEN** degradarse y la duplicacion de hechos **DEBE** eliminarse.

### 7.5 Calidad de superficie

La compresion maxima **NO DEBE** producir headings truncados, chunks primarios pobres, labelese ni dumping estructural.

### 7.6 Integridad de la familia `atomic`

En artefactos `atomic`, la unicidad global de IDs y la resolubilidad de fuentes son invariantes; violarlos invalida la familia.

### 7.7 Integridad del perfil prescriptivo `spec`

En artefactos `spec`, los invariantes de §5.6.2.7 (consistencia interna, auto-suficiencia de regla, no-circularidad, preservacion de idioma, enforcement declarado) son constitutivos del perfil; violarlos invalida el caracter prescriptivo del documento.

## 8. Versionado

- correccion editorial sin cambio semantico: patch
- adicion compatible de conocimiento o validacion: minor
- cambio incompatible del contrato de koraficacion, compresion o realizacion: major

## 9. Validacion

| Check                     | Criterio                                                    | Enforcement | Accion si falla                           |
| ------------------------- | ----------------------------------------------------------- | ----------- | ----------------------------------------- |
| Frontmatter valido        | Cumple el sobre base y usa `extensions` para metadata extra | schema      | Corregir frontmatter                      |
| Regimen de identidad      | URN tripartito y version fuera del URN                      | schema      | Migrar identidad                          |
| Referencias validas       | URNs, headings y fragments resuelven                        | lint        | Corregir referencias                      |
| Gramatica estructural     | Jerarquia y chunks cumplen `§5`                             | lint        | Reescribir seccion                        |
| Sin grasa                 | No hay introducciones, transiciones ni hedging residual     | manual      | Re-comprimir                              |
| Fidelidad absoluta        | `FS=100%`                                                   | manual      | Restaurar hechos omitidos                 |
| Compresion razonable      | `CR>1.5` o justificacion explicita                          | manual      | Reducir redundancia o documentar densidad |
| Calidad de superficie     | Sin headings truncados, labelese ni dumping                 | lint+manual | Re-realizar superficie                    |
| Heading recuperable       | Cada `##` expresa sujeto o alcance recuperable              | lint        | Renombrar heading                         |
| Resumen obligatorio       | Familias que lo exigen incluyen `## Resumen` no vacio       | lint        | Agregar o completar resumen               |
| Headings-campo prohibidos | KB publicada no serializa campos como headings              | lint        | Reestructurar seccion                     |
| Estructuras preservadas   | Tablas y listas no se degradan                              | manual      | Restaurar estructura                      |
| Catalogo derivado         | El artefacto es indexable y regenerable por CLI             | lint        | Corregir manifest o indexador             |
| Namespace-directorio      | Namespace URN coincide con subdirectorio bajo `artifacts/knowledge/`  | lint        | Migrar artefacto o corregir URN           |
| Status por directorio     | `artifacts/knowledge/` solo contiene `published` o `deprecated`       | schema      | Mover a `artifacts/knowledge/_SCRIPTORIUM/REVIEW/` o publicar |
| Lifecycle status          | Transicion de status pasa por `kora promote` y verificaciones §3.1 regla 10 | manual | Ejecutar `kora promote` con verificaciones §6.10 y §6.11 |
| Indice atomic             | `atomic` tiene `## Indice de fuentes` no vacio              | lint        | Completar indice                          |
| Proposiciones atomic      | Cada entry tiene ID Pxxx + tipo + texto + ≥1 fuente         | lint        | Reparar entry                             |
| Tipos atomic              | Cada tipo pertenece al enum cerrado (`§5.6.1`)              | schema      | Corregir tipo                             |
| Unicidad Pxxx             | IDs Pxxx unicos en artefacto y en conjunto segmentado       | lint        | Renumerar o consolidar                    |
| Segmentacion atomic       | Maximo duro de 200 props; referencia blanda ~15.000 caracteres con corte estructural coherente | lint/manual | Segmentar o declarar indice si corresponde |
| Dedup atomic              | Multi-source solo si hechos equivalentes; conflicto -> `tension` | manual  | Reclasificar proposicion                  |
| Keyword explicita (spec)  | Familia `spec`: toda obligacion importante usa keyword RFC 2119 | lint        | Reescribir regla con keyword              |
| Trazabilidad oficial (spec) | `Traces to:` referencia solo Formal Layer oficial         | lint        | Corregir o degradar a `Rationale:`        |
| Patron de regla (spec)    | Reglas complejas que admitan mala lectura incluyen `Correcto:/Incorrecto:`; toda regla con justificacion disponible incluye `Traces to:` (si es formal) o `Rationale:` (si es pragmatica) | manual | Completar regla conforme §5.6.2.6 |
| Consistencia interna (spec) | No hay contradicciones no resueltas                       | manual      | Reescribir o introducir precedencia       |
| Auto-suficiencia de regla (spec) | Reglas se entienden sin contexto omitido critico     | manual      | Reescribir regla                          |
| No-circularidad (spec)    | Referencias normativas no forman bucles opacos              | manual      | Aclarar dependencia                       |
| Enforcement declarado (spec) | Toda tabla de validacion incluye columna `Enforcement`   | lint        | Completar tabla                           |
| Template prescriptivo (spec) | Documento sigue esqueleto §5.6.2.8                       | manual      | Reestructurar secciones                   |
| Migracion en major (spec) | Major bumps incluyen seccion `## Migracion`                 | lint        | Agregar seccion                           |

## 10. Migracion

Esta seccion se establece a partir de v6.3.0. Los breaking changes de major bumps anteriores no fueron documentados en seccion dedicada.

### 10.0 Contrato vigente v8

- Todo el contrato v7.1 se preserva sin quiebres en el regimen descriptivo.
- md-spec admite regimen dual: **descriptivo** y **prescriptivo**. Ambos comparten envelope, gramatica y koraficacion; el perfil `spec` (§5.6.2) agrega invariantes prescriptivos.
- Absorbe organicamente el contrato de la retirada `spec-md v5.2.0`:
  - §5.6.2.1 proceso de cristalizacion (funtor C) con Traces to formal/05 §2.3.
  - §5.6.2.2 keywords RFC 2119 como enum cerrado + obligatoriedad.
  - §5.6.2.3 convencion `Traces to:` / `Rationale:` formalizada.
  - §5.6.2.4 elementos retoricos normativos (`Correcto:/Incorrecto:`, `Rationale:`, tabla de validacion).
  - §5.6.2.5 cuatro funciones validas para prosa explicativa en spec.
  - §5.6.2.6 patron obligatorio regla + ejemplo + traza.
  - §5.6.2.7 invariantes prescriptivos (consistencia interna, auto-suficiencia de regla, no-circularidad, idioma, enforcement declarado).
  - §5.6.2.8 template esqueleto minimo con seccion Migracion obligatoria en major bumps.
  - §5.6.2.9 auto-declaracion de precedencia.
- §2 agrega siete terminos prescriptivos (documento prescriptivo, regla, cristalizacion, rationale, traces to, auto-suficiencia, no-circularidad).
- §7 agrega §7.7 integridad del perfil prescriptivo.
- §9 agrega 9 checks especificos para perfil `spec`.

### 10.1 Contrato vigente v7

- Todo el contrato v6 se preserva sin quiebres.
- Se agrega familia documental `atomic` (§5.6) con invariantes y enum cerrado de tipos (§5.6.1).
- Se declara la figura de `productor canonico de familia`, referida a `knowledge-spec §12`.
- Se agregan checks de validacion para `atomic` (§9).
- Se agrega invariante de integridad de la familia `atomic` (§7.6).

Cambios v7.1:

- §3.1 regla 7 se acota a artefactos que residen bajo `artifacts/knowledge/`; artefactos en las capas normativas (`governance/`, `ontology/`, `serialization/`, `runtime/`), `artifacts/agents/`, `artifacts/skills/` o `BUILD/` derivan namespace de su spec canonica correspondiente.
- §3.1 regla 8 distingue lifecycle descriptivo (`draft -> published -> deprecated`) vs ejecutable (`draft -> active -> deprecated -> retired`) segun `gobernanza §5`.
- §3.1 regla 10 reapunta al procedimiento `kora promote` y verificaciones §6.10 + §6.11 + regla 7, eliminando referencia a "protocolo de auditoria" inexistente en gobernanza v4.
- §5.6 fusiona las taxonomias previas de `knowledge-spec §3` ("tipos de artefacto") y `md-spec §5.6` ("familias documentales") en una sola tabla. `knowledge-spec §3` pasa a referenciar esta tabla como autoridad.
- §5.6 agrega familias `spec`, `guide`, `faq`, `catalog`, `note` (antes tipos en `knowledge-spec`); renombra `inventory/control` a `inventory` con publication_class como discriminante; formaliza `cq_catalog` como subperfil de `catalog`.

### 10.2 Contrato v6

- URN conceptual tripartito, version fuera del URN (§4.1).
- Koraficacion como functor fiel, comprimido e idempotente (§6.2).
- Pipeline descentralizado en `_SCRIPTORIUM/{INBOX,REVIEW}/` -> `artifacts/knowledge/{ns}/...` (§6.1; detalle en `knowledge-spec §6`).
- Fidelidad absoluta `FS=100%` como criterio de cierre (§7.3).
- Compresion `CR>1.5` o justificacion explicita (§5.5).
- Telegrafizacion con reglas T1-T7 y realizacion superficial (§5.4).
- Familias documentales con invariantes propios (§5.6).
- Verificacion mecanica y de fidelidad obligatorias (§6.10, §6.11).
- Lifecycle `draft -> published -> deprecated` con auditoria para transitar (§3.1).

### 10.3 Que migrar desde v6

- Artefactos existentes que representan proposiciones atomicas **PUEDEN** reclasificarse como familia `atomic` en su frontmatter sin perder identidad URN.
- Los archivos en `atomize/raw/` permanecen pre-canonicos hasta ser re-procesados por el productor canonico de la familia `atomic`; su persistencia en ese estado es deuda declarada.
- Los outputs legacy de `atomize` con formato `_ATOMIC_GRAPH.md` plano **DEBEN** regenerarse con el productor canonico antes de ingresar a `artifacts/knowledge/`.

### 10.4 Que se depreca (v6 → v7)

- El formato plano `_ATOMIC_GRAPH.md` sin frontmatter queda deprecado como artefacto publicable. Se mantiene solo como salida operativa temporal dentro de `atomize/raw/atomize-out/`.

### 10.5 Que migrar desde v7.1 (a v8.0)

- Artefactos existentes en la topologia legacy `specs/` se reclasifican al perfil `spec` (§5.6.2) y se ubican en la capa normativa vigente que corresponda (`governance/`, `ontology/`, `serialization/` o `runtime/`). No cambia URN ni version del artefacto (cambia version de md-spec, no de la spec consumidora).
- Specs que contenian reglas sin keyword RFC 2119 o sin el patron regla+ejemplo+traza **DEBEN** auditarse. El check `Patron de regla (spec)` es `manual`; el check `Keyword explicita (spec)` es `lint`.
- Specs que usaban `Traces to:` hacia paths relativos o hacia artefactos fuera de la Formal Layer oficial **DEBEN** corregirse a URN de Formal Layer oficial o degradarse a `Rationale:`.
- Specs sin columna `Enforcement` en tablas de validacion **DEBEN** completarla.
- Las referencias colgadas a `urn:kora:kb:spec-md` (retirada) se migran a `urn:kora:kb:md-spec` en una sola pasada; el contrato prescriptivo ahora vive aqui.

### 10.6 Que se depreca (v7.1 → v8.0)

- Nada del regimen descriptivo se depreca; el contrato v7.1 se preserva integro.
- La spec `spec-md v5.2.0` (retirada en el commit `4c35d31`, 2026-04-16) queda formalmente absorbida. Su URN `urn:kora:kb:spec-md` **NO DEBE** usarse; referencias residuales se migran a `urn:kora:kb:md-spec`.

Toda futura transicion major **DEBE** documentar aqui: (1) que cambio, (2) que migrar, y (3) que se depreca.
