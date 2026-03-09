---
_manifest:
  urn: "urn:kora:kb:md-spec"
  provenance:
    created_by: "FS"
    created_at: "2026-03-09"
    source: "KORA categorical-foundations 05, KORA/Gobernanza v3.0.0, refactor del contrato de compresion y realizacion superficial"
version: "6.1.0"
status: published
tags: [spec, markdown, conocimiento, rag, koraficacion, fidelidad]
lang: es
---

# KORA/MD v6.1.0

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

La spec general **DEBE** complementarse con invariantes por familia documental cuando la estructura del dominio lo requiera.

Familias minimas:

| Familia             | Invariantes                                                                                                                 |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `normative`         | `##` con asunto semantico; condiciones, excepciones y matrices promovidas a listas/tablas; no dumps de numerales sin asunto |
| `glossary`          | buckets recuperables; sin duplicados no resueltos; alias explicitos                                                         |
| `organigram`        | dependencias estructurales explicitas; no headings-campo para representar jerarquia                                         |
| `cq_catalog`        | `## Resumen` obligatorio y no vacio; dominios como `##`; scaffold en idioma del documento                                   |
| `inventory/control` | puede retener material operativo; si `publication_class=control`, queda fuera de KB publicada                               |

Clasificacion de familia:

La familia de un artefacto **DEBE** identificarse por uno de estos mecanismos, en orden de precedencia:

1. `extensions.{namespace}.family` explicito en el frontmatter.
2. Convencion de directorio (e.g., `glossaries/`, `normative/`).
3. Clasificacion manual del curador durante koraficacion.

## 6. Koraficacion

### 6.1 Entrada

Cualquier documento originalmente escrito para humanos **PUEDE** usarse como entrada. Todo documento que ingrese al monorepo para koraficacion **DEBE** transitar por el pipeline `inbox/ -> source/ -> drafts/ -> knowledge/`.

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
   - naturalidad tecnica minima
6. Si `FS < 100%`, la koraficacion falla.
7. Si `CR < 1.5`, debe reducirse redundancia restante o justificarse por alta densidad informacional.
8. Si la calidad de superficie falla, la koraficacion falla aunque `FS=100%`.

### 6.12 Registro en catalogo

Todo artefacto nuevo o modificado **DEBE** quedar indexable por `kora index`.

## 7. Invariantes de KORA/MD

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
