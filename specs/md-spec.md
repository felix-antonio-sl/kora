---
_manifest:
  urn: "urn:kora:kb:md-spec"
  provenance:
    created_by: "FS"
    created_at: "2026-03-08"
    source: "KORA categorical-foundations 05, KORA/Gobernanza v3.0.0, repair of koraficacion contract"
version: "5.0.0"
status: published
tags: [spec, markdown, conocimiento, rag, koraficacion, fidelidad]
lang: es
---

# KORA/MD v5.0.0

## 1. Definicion

KORA/MD es el formato de artefactos descriptivos del ecosistema KORA. Gobierna conocimiento, no workspaces, ni runtime, ni configuracion operativa.

KORA/MD optimiza almacenamiento, indexacion y recuperacion para humanos y LLMs via RAG sin sacrificar verdad factual.

### 1.1 Alcance y audiencia

Aplica a leyes, manuales, guias, corpus de conocimiento, notas tecnicas y cualquier artefacto cuyo objetivo sea describir hechos, procedimientos o referencias.

La audiencia primaria son runtimes y pipelines de recuperacion. La audiencia secundaria son humanos que curan el corpus.

## 2. Definiciones

| Termino | Definicion |
| --- | --- |
| Artefacto KORA/MD | Archivo Markdown con frontmatter KORA y cuerpo descriptivo |
| Koraficacion | Transformacion `DocHumano -> KORA/MD` que preserva verdad y elimina entropia comunicativa |
| Chunk RAG | Unidad primaria de recuperacion delimitada por `##` |
| Skeleton | Estructura del documento: titulo, headings, tablas, listas, jerarquia |
| Meat | Hechos atomicos que deben preservarse: cifras, fechas, condiciones, excepciones, referencias, dependencias |
| Fat | Retorica, hedging, transiciones y relleno editorial que debe eliminarse |
| FS | Fidelity Score. Porcentaje de hechos preservados o comprimidos sin perdida semantica |
| CR | Compression Ratio. Longitud fuente / longitud salida |
| SSOT | Un hecho, un lugar |

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

| Nivel | Rol semantico |
| --- | --- |
| `#` | Titulo del artefacto |
| `##` | Seccion primaria recuperable |
| `###` | Subtopico o componente |
| `####` | Detalle atomico |

Reglas:

1. La profundidad **NO DEBE** exceder `####`.
2. Cada `##` **DEBE** ser recuperable de forma casi aislada.
3. Los headings **DEBEN** ser telegraficos: sintagmas nominales, no oraciones.
4. Un `###` **NO DEBE** existir sin un `##` padre.

### 5.2 Elementos de contenido

| Elemento | Uso permitido | Funcion prohibida |
| --- | --- | --- |
| Negrita | definiciones, terminos clave | enfasis decorativo |
| Cursiva | termino tecnico o extranjero | enfasis estilistico |
| `codigo` | URNs, ids, comandos, literales | resaltado general |
| Lista | enumeracion o procedimiento | prosa fragmentada sin estructura |
| Tabla | comparacion, condiciones, matrices | decoracion sin valor informativo |

### 5.3 Elementos prohibidos (grasa)

Cada elemento de la siguiente lista **NO DEBE** incluirse en KORA/MD:

- introducciones tipo "En este documento veremos..."
- transiciones tipo "A continuacion", "Por otro lado"
- hedging tipo "probablemente", "en general", "suele"
- preguntas retoricas
- saludos y cierres
- duplicacion de hechos

### 5.4 Telegrafizacion (compresion informativa)

La escritura KORA/MD **DEBE** ser telegrafica: maxima densidad semantica, minima cantidad de palabras.

Patrones obligatorios:

- Definiciones: `**Termino** - descripcion telegrafica`
- Condiciones: tabla `Condicion | Resultado | Base`
- Procedimientos: lista secuencial
- Comparaciones: tabla, nunca parrafo si la relacion ya es matricial

### 5.5 Preservacion de verdad (prueba acida)

La telegrafizacion **NO DEBE** sacrificar contenido informativo.

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
- `CR<1.5` solo es aceptable si `FS=100%` y no queda grasa eliminable

## 6. Koraficacion

### 6.1 Entrada

Cualquier documento originalmente escrito para humanos **PUEDE** usarse como entrada. Todo documento que ingrese al monorepo para koraficacion **DEBE** transitar por el pipeline `inbox/ -> source/ -> drafts/ -> knowledge/`.

### 6.2 El proceso de koraficacion

La koraficacion es la transformacion `DocHumano -> KORA/MD`.

Traces to: formal/05 §2.2 (Koraficacion Functor K)

Propiedades:

- fiel
- telegrafica
- promotora de estructura
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

Documentos grandes **DEBEN** segmentarse; documentos con alta carga numerica **DEBEN** pasar verificacion mecanica fuerte.

### 6.5 Segmentacion

Para documentos grandes:

1. Los cortes **DEBEN** realizarse entre secciones naturales.
2. Cada segmento **DEBE** ser tematicamente coherente.
3. **NO DEBE** cortarse dentro de una tabla, lista o parrafo.

### 6.6 Telegrafizacion fiel

Por cada segmento o documento completo:

1. Preservar toda cifra, fecha, plazo, condicion, excepcion y referencia legal.
2. Preservar el idioma del input.
3. Preservar toda lista y toda tabla sin perder items, filas o columnas.
4. Promover prosa comparativa o condicional a estructura.
5. Mantener orden semantico salvo que la normalizacion posterior mejore recuperacion sin perder verdad.
6. Eliminar grasa activa: introducciones, transiciones, hedging, saludos, retorica.

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

### 6.11 Verificacion de fidelidad

Todo artefacto koraficado **DEBE** cerrar con verificacion de fidelidad.

Proceso minimo:

1. Inventariar `skeleton/meat/fat`.
2. Enumerar hechos atomicos `N_hechos`.
3. Clasificar cada hecho como `preservado`, `comprimido`, `omitido` o `agregado`.
4. Calcular:
   - `FS = (preservados + comprimidos) / N_hechos * 100`
   - `CR = len(fuente) / len(salida)`
5. Si `FS < 100%`, la koraficacion falla.
6. Si `CR < 1.5`, debe justificarse por alta densidad informacional o reintentarse la telegrafizacion.

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

## 8. Versionado

- correccion editorial sin cambio semantico: patch
- adicion compatible de conocimiento o validacion: minor
- cambio incompatible del contrato de koraficacion o fidelidad: major

## 9. Validacion

| Check | Criterio | Enforcement | Accion si falla |
| --- | --- | --- | --- |
| Frontmatter valido | Cumple el sobre base y usa `extensions` para metadata extra | schema | Corregir frontmatter |
| Regimen de identidad | URN tripartito y version fuera del URN | schema | Migrar identidad |
| Referencias validas | URNs, headings y fragments resuelven | lint | Corregir referencias |
| Gramatica estructural | Jerarquia y chunks cumplen `§5` | lint | Reescribir seccion |
| Sin grasa | No hay introducciones, transiciones ni hedging residual | manual | Re-telegrafizar |
| Fidelidad absoluta | `FS=100%` | manual | Restaurar hechos omitidos |
| Compresion razonable | `CR>1.5` o justificacion explicita | manual | Re-telegrafizar o documentar densidad |
| Estructuras preservadas | Tablas y listas no se degradan | manual | Restaurar estructura |
| Catalogo derivado | El artefacto es indexable y regenerable por CLI | lint | Corregir manifest o indexador |
