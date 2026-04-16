---
_manifest:
  urn: "urn:kora:kb:md-spec"
  provenance:
    created_by: "FS"
    created_at: "2026-03-09"
    source: "KORA categorical-foundations 05, KORA/Gobernanza v4.0.0, refactor del contrato de compresion y realizacion superficial; v7 agrega familia atomic con productor canonico atomize; v7.1 fusiona tipos de artefacto y familias documentales, acota reglas 7-8 por regimen, reformula regla 10"
version: "7.1.0"
status: published
tags: [spec, markdown, conocimiento, rag, koraficacion, fidelidad, atomic]
lang: es
extensions: {}
relations:
  cites:
    - "urn:kora:kb:gobernanza"
---

# KORA/MD v7.1.0

## 1. Definicion

KORA/MD es el formato de artefactos descriptivos del ecosistema KORA. Gobierna conocimiento, no workspaces, ni runtime, ni configuracion operativa.

KORA/MD optimiza almacenamiento, indexacion y recuperacion para humanos y LLMs via RAG sin sacrificar verdad factual.

### 1.1 Alcance y audiencia

Aplica a leyes, manuales, guias, corpus de conocimiento, notas tecnicas y cualquier artefacto cuyo objetivo sea describir hechos, procedimientos o referencias.

La audiencia primaria son runtimes y pipelines de recuperacion. La audiencia secundaria son humanos que curan el corpus.

## 2. Definiciones

| Termino                 | Definicion                                                                                                 |
| ----------------------- | ---------------------------------------------------------------------------------------------------------- |
| Artefacto KORA/MD       | Archivo Markdown con frontmatter KORA y cuerpo descriptivo                                                 |
| Koraficacion            | Transformacion `DocHumano -> KORA/MD` que preserva verdad y elimina entropia comunicativa                  |
| Chunk RAG               | Unidad primaria de recuperacion delimitada por `##`                                                        |
| Skeleton                | Estructura del documento: titulo, headings, tablas, listas, jerarquia                                      |
| Meat                    | Hechos atomicos que deben preservarse: cifras, fechas, condiciones, excepciones, referencias, dependencias |
| Fat                     | Retorica, hedging, transiciones y relleno editorial que debe eliminarse                                    |
| Realizacion superficial | Eleccion de la forma final visible del conocimiento: heading, prosa, lista o tabla                         |
| Labelese                | Salida que suena a serializacion de campos: `Asunto`, `Contenido`, `Tipo`, `Path`, etc.                    |
| FS                      | Fidelity Score. Porcentaje de hechos preservados o comprimidos sin perdida semantica                       |
| CR                      | Compression Ratio. Longitud fuente / longitud salida                                                       |
| SSOT                    | Un hecho, un lugar                                                                                         |
| Proposicion atomica     | Hecho verificable minimo autocontenido, con tipo, texto comprimido y ancla de fuente resoluble             |
| Productor canonico      | Herramienta autorizada para generar artefactos de una familia con garantia de invariantes                  |

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
status: draft|published|deprecated
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
7. Cuando el artefacto reside bajo `KNOWLEDGE/`, el namespace en el URN **DEBE** coincidir con el primer subdirectorio bajo `KNOWLEDGE/`. Enforcement: lint. Los artefactos que viven fuera de `KNOWLEDGE/` (specs en `specs/`, workspaces en `AGENTS/`, capacidades en `SKILLS/`, outputs en `BUILD/`) derivan su namespace de la topologia declarada por la spec canonica que los gobierna; para ellos esta regla no aplica.
8. El valor de `status` **DEBE** respetar el regimen de lifecycle correspondiente (`gobernanza §5`):
   - artefactos descriptivos (KORA/MD en `KNOWLEDGE/` y specs): `draft -> published -> deprecated`.
   - artefactos ejecutables (workspaces agente, skills, bootstrap): `draft -> active -> deprecated -> retired`.
   Las transiciones inversas son invalidas en ambos regimenes.
9. `KNOWLEDGE/` solo acepta artefactos con `status: published` o `status: deprecated`. Artefactos con `status: draft` **DEBEN** residir en `KNOWLEDGE/_SCRIPTORIUM/INBOX/` (material pre-categorial) o `KNOWLEDGE/_SCRIPTORIUM/REVIEW/` (drafts en revision). Enforcement: schema.
10. La transicion a `status: published` (o `status: active` para ejecutables) **DEBE** pasar por `kora promote` u otro procedimiento equivalente que verifique verificacion mecanica (§6.10), verificacion de fidelidad (§6.11) y ausencia de conflictos de namespace (regla 7).
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

Traces to: formal/05 §2.2 (Koraficacion Functor K)

Regla acida:

- si al eliminar texto cambia solo tono o fluidez, debe eliminarse
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
| `spec`       | Documenta reglas y contratos; precedencia declarada al inicio; URN `urn:{ns}:kb:{id}`; reside en `specs/`, no en `KNOWLEDGE/` |
| `guide`      | Manual o guia operativa; prosa tecnica controlada; ejemplos concretos vinculados a headings; `## Resumen` recomendado        |
| `normative`  | `##` con asunto semantico; condiciones, excepciones y matrices promovidas a listas/tablas; no dumps de numerales sin asunto |
| `glossary`   | Buckets recuperables; sin duplicados no resueltos; alias explicitos                                                          |
| `faq`        | `##` por pregunta; respuesta autocontenida; orden por frecuencia o tema                                                     |
| `catalog`    | Entradas tabuladas; columnas minimas `id | urn | titulo | resumen`; indexable por CLI                                        |
| `cq_catalog` | `## Resumen` obligatorio y no vacio; dominios como `##`; scaffold en idioma del documento; subperfil de `catalog`            |
| `inventory`  | Puede retener material operativo; si `publication_class=control`, queda fuera de KB publicada                               |
| `organigram` | Dependencias estructurales explicitas; no headings-campo para representar jerarquia                                         |
| `atomic`     | `## Indice de fuentes` obligatorio y no vacio; cada `##` agrupa proposiciones por dominio o source_file; cada proposicion tiene ID `Pxxx` unico, tipo del enum cerrado, texto comprimido y al menos una fuente resoluble; enum cerrado de tipos (`§5.6.1`); FS=100% sobre cifras/fechas/excepciones originales; dedup multi-source permitido; conflicto semantico entre fuentes -> tipo `tension`; limite operativo 5.000 palabras y 200 proposiciones por artefacto; si excede, segmentar y generar artefacto indice |
| `note`       | Nota tecnica compacta; al menos un `##` tematico; `## Resumen` opcional cuando el tamaño lo vuelve redundante                |

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
5. Si dos fuentes afirman el mismo hecho, se dedup en una sola proposicion con cita multiple.
6. Si dos fuentes se contradicen sobre el mismo hecho, **NO** se dedup: se emite una proposicion `tension` que nombra ambas posiciones.
7. Extensiones del frontmatter **DEBEN** declarar `extensions.kora.family: atomic` y, cuando aplique, `extensions.kora.atomic.source_corpus`, `extensions.kora.atomic.n_propositions` y `extensions.kora.atomic.producer`.

## 6. Koraficacion

### 6.1 Entrada

Cualquier documento originalmente escrito para humanos **PUEDE** usarse como entrada. Todo documento que ingrese al monorepo para koraficacion **DEBE** transitar por el pipeline descentralizado definido en `knowledge-spec §6`:

```
KNOWLEDGE/_SCRIPTORIUM/INBOX/  ->  KNOWLEDGE/_SCRIPTORIUM/REVIEW/  ->  KNOWLEDGE/{ns}/...
```

### 6.2 El proceso de koraficacion

La koraficacion es la transformacion `DocHumano -> KORA/MD`.

Traces to: formal/05 §2.2 (Koraficacion Functor K)

Propiedades:

- fiel
- comprimida
- promotora de estructura
- realizadora de superficie
- normalizadora
- idempotente
- invariante en idioma

### 6.3 Estrategia de ejecucion

La implementacion concreta puede usar trabajo manual, una o multiples pasadas LLM, siempre que el resultado satisfaga esta spec.

Cuando una familia tiene productor canonico declarado (`knowledge-spec §12`), la generacion de artefactos **DEBERIA** delegarse al productor; la edicion manual posterior **DEBE** marcarse explicitamente para inhibir sobreescrituras.

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

4. Si el artefacto atomic supera 5.000 palabras o 200 proposiciones, **DEBE** emitirse un artefacto `atomic-{slug}-index` y N artefactos `atomic-{slug}-{NN}`.
5. El indice **DEBE** contener tabla `Segmento | Rango Pxxx | Dominios` y resolver URNs a cada segmento.
6. Los IDs `Pxxx` **DEBEN** ser unicos a traves del indice + todos los segmentos (numeracion global).

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
7. Si `CR < 1.5`, debe reducirse redundancia restante o justificarse por alta densidad informacional.
8. Si la calidad de superficie falla, la koraficacion falla aunque `FS=100%`.

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
| Namespace-directorio      | Namespace URN coincide con subdirectorio bajo `KNOWLEDGE/`  | lint        | Migrar artefacto o corregir URN           |
| Status por directorio     | `KNOWLEDGE/` solo contiene `published` o `deprecated`       | schema      | Mover a `KNOWLEDGE/_SCRIPTORIUM/REVIEW/` o publicar |
| Lifecycle status          | Transicion de status cumple protocolo auditoria             | manual      | Completar auditoria antes de publicar     |
| Indice atomic             | `atomic` tiene `## Indice de fuentes` no vacio              | lint        | Completar indice                          |
| Proposiciones atomic      | Cada entry tiene ID Pxxx + tipo + texto + ≥1 fuente         | lint        | Reparar entry                             |
| Tipos atomic              | Cada tipo pertenece al enum cerrado (`§5.6.1`)              | schema      | Corregir tipo                             |
| Unicidad Pxxx             | IDs Pxxx unicos en artefacto y en conjunto segmentado       | lint        | Renumerar o consolidar                    |
| Segmentacion atomic       | Artefacto ≤5.000 palabras y ≤200 props o existe `-index`    | lint        | Segmentar o declarar indice               |
| Dedup atomic              | Multi-source solo si hechos equivalentes; conflicto -> `tension` | manual  | Reclasificar proposicion                  |

## 10. Migracion

Esta seccion se establece a partir de v6.3.0. Los breaking changes de major bumps anteriores no fueron documentados en seccion dedicada.

### 10.1 Contrato vigente v7

- Todo el contrato v6 se preserva sin quiebres.
- Se agrega familia documental `atomic` (§5.6) con invariantes y enum cerrado de tipos (§5.6.1).
- Se declara la figura de `productor canonico de familia`, referida a `knowledge-spec §12`.
- Se agregan checks de validacion para `atomic` (§9).
- Se agrega invariante de integridad de la familia `atomic` (§7.6).

Cambios v7.1:

- §3.1 regla 7 se acota a artefactos que residen bajo `KNOWLEDGE/`; artefactos en `specs/`, `AGENTS/`, `SKILLS/` o `BUILD/` derivan namespace de su spec canonica correspondiente.
- §3.1 regla 8 distingue lifecycle descriptivo (`draft -> published -> deprecated`) vs ejecutable (`draft -> active -> deprecated -> retired`) segun `gobernanza §5`.
- §3.1 regla 10 reapunta al procedimiento `kora promote` y verificaciones §6.10 + §6.11 + regla 7, eliminando referencia a "protocolo de auditoria" inexistente en gobernanza v4.
- §5.6 fusiona las taxonomias previas de `knowledge-spec §3` ("tipos de artefacto") y `md-spec §5.6` ("familias documentales") en una sola tabla. `knowledge-spec §3` pasa a referenciar esta tabla como autoridad.
- §5.6 agrega familias `spec`, `guide`, `faq`, `catalog`, `note` (antes tipos en `knowledge-spec`); renombra `inventory/control` a `inventory` con publication_class como discriminante; formaliza `cq_catalog` como subperfil de `catalog`.

### 10.2 Contrato v6

- URN conceptual tripartito, version fuera del URN (§4.1).
- Koraficacion como functor fiel, comprimido e idempotente (§6.2).
- Pipeline descentralizado en `_SCRIPTORIUM/{INBOX,REVIEW}/` -> `KNOWLEDGE/{ns}/...` (§6.1; detalle en `knowledge-spec §6`).
- Fidelidad absoluta `FS=100%` como criterio de cierre (§7.3).
- Compresion `CR>1.5` o justificacion explicita (§5.5).
- Telegrafizacion con reglas T1-T7 y realizacion superficial (§5.4).
- Familias documentales con invariantes propios (§5.6).
- Verificacion mecanica y de fidelidad obligatorias (§6.10, §6.11).
- Lifecycle `draft -> published -> deprecated` con auditoria para transitar (§3.1).

### 10.3 Que migrar desde v6

- Artefactos existentes que representan proposiciones atomicas **PUEDEN** reclasificarse como familia `atomic` en su frontmatter sin perder identidad URN.
- Los archivos en `atomize/raw/` permanecen pre-canonicos hasta ser re-procesados por el productor canonico de la familia `atomic`; su persistencia en ese estado es deuda declarada.
- Los outputs legacy de `atomize` con formato `_ATOMIC_GRAPH.md` plano **DEBEN** regenerarse con el productor canonico antes de ingresar a `KNOWLEDGE/`.

### 10.4 Que se depreca

- El formato plano `_ATOMIC_GRAPH.md` sin frontmatter queda deprecado como artefacto publicable. Se mantiene solo como salida operativa temporal dentro de `atomize/raw/atomize-out/`.

Toda futura transicion major **DEBE** documentar aqui: (1) que cambio, (2) que migrar, y (3) que se depreca.
