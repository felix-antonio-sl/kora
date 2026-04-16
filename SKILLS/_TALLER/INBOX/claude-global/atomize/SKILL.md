---
name: atomize
description: Extrae proposiciones atómicas de carpetas de documentos y emite artefactos KORA/MD de familia `atomic` conformes a md-spec v7. Productor canónico de la familia `atomic` (knowledge-spec §12). Alternativa a RAG para corpus densos.
trigger: /atomize
---

# /atomize

Extrae proposiciones atómicas de una carpeta de documentos y emite artefactos KORA/MD de familia `atomic` conformes a `md-spec v7`. Este skill es el **productor canónico** de la familia `atomic` declarado por `knowledge-spec §12`.

## Uso

```
/atomize                                    # carpeta actual → contexto KORA autodetectado
/atomize <path>                             # carpeta específica
/atomize <path> --slug <slug>               # override del slug del artefacto
/atomize <path> --output <dir>              # override del directorio de salida
/atomize <path> --legacy                    # fallback formato plano `_ATOMIC_GRAPH.md` (no canónico)
```

## Output canónico

Por defecto, si el input está dentro de o cerca de un repo KORA (detectado por ancestor con `OPERATIONS/` + `KNOWLEDGE/` + `specs/`), el skill emite:

```
<repo-root>/OPERATIONS/drafts/kora/atomic-{slug}.md        # ≤ 5.000 palabras y ≤ 200 props
```

Si el corpus supera los umbrales, segmenta:

```
<repo-root>/OPERATIONS/drafts/kora/atomic-{slug}-index.md  # índice
<repo-root>/OPERATIONS/drafts/kora/atomic-{slug}-01.md     # segmentos
<repo-root>/OPERATIONS/drafts/kora/atomic-{slug}-02.md
...
```

URNs asignados: `urn:kora:kb:atomic-{slug}` (único) o `urn:kora:kb:atomic-{slug}-index` + `urn:kora:kb:atomic-{slug}-NN`.

Si no detecta contexto KORA y no se pasó `--output`, el skill emite el artefacto canónico en `<input>/atomize-out/atomic-{slug}.md` y avisa que el artefacto es portable pero no está enganchado a ningún repo KORA.

Si se pasa `--legacy`, produce el formato plano `_ATOMIC_GRAPH.md` sin frontmatter. Este modo queda deprecado por `md-spec §10.4` y solo existe para compat.

## Qué es una proposición atómica

El hecho verificable más pequeño que es autocontenido — se entiende sin contexto externo. Una oración compuesta con dos hechos independientes debe dividirse en dos proposiciones.

Cada proposición tiene: ID (`P###`), texto comprimido, tipo, ≥1 fuente resoluble, y entidades mencionadas.

## Tipos válidos (enum cerrado, md-spec §5.6.1)

| Tipo          | Semántica                                         | Ejemplo |
|---------------|---------------------------------------------------|---------|
| `requirement` | algo que se debe cumplir                          | "enfermero clínico requiere ≥2 años experiencia clínica" |
| `definition`  | qué es algo                                       | "HD: modalidad alternativa a hospitalización cerrada para agudos/crónicos reagudizados" |
| `rule`        | cómo funciona algo                                | "SEREMI otorga autorización sanitaria según domicilio dependencias administrativas" |
| `exclusion`   | qué no aplica o está prohibido                    | "HD excluye pacientes con salud mental descompensada" |
| `constraint`  | límite numérico o temporal                        | "autorización sanitaria vigencia 3 años, prórroga automática" |
| `obligation`  | acción que alguien debe realizar                  | "trabajador social debe verificar disponibilidad cuidador/tutor legal" |
| `permission`  | algo que está permitido                           | "médico atención directa puede usar TIC para diagnóstico y tratamiento" |
| `deadline`    | plazo específico                                  | "establecimientos existentes: 6 meses para ajustar procedimientos" |
| `tension`     | contradicción o ambigüedad entre fuentes          | "Decreto 31 exige IAAS 80h coordinación pero tabla asigna RCP 3h" |
| `fact`        | dato verificable sin carga normativa              | "Decreto 31 firmado 05-jun-2024 por Ministra Ximena Aguilera" |
| `scope`       | alcance o ámbito de aplicación                    | "reglamento rige establecimientos atención cerrada públicos/privados con HD" |

Usar solo tipos de este enum. El conformance check de `md-spec §9` lo valida.

## What You Must Do When Invoked

Si no se pasa path, usar `.` (directorio actual). No preguntar al usuario por el path.

Parsear flags: `--slug`, `--output`, `--legacy`.

Seguir los pasos en orden. No saltar pasos.

### Step 0 — Detectar contexto KORA y decidir output path

Buscar hacia arriba desde el input path un directorio ancestro que contenga simultáneamente `OPERATIONS/`, `KNOWLEDGE/` y `specs/`. Si se encuentra, ese es el `repo-root` de KORA y el output canónico va a `<repo-root>/OPERATIONS/drafts/kora/`.

```bash
# Pseudocódigo del algoritmo:
# D = abspath(INPUT_PATH)
# while D != "/":
#   if -d D/OPERATIONS && -d D/KNOWLEDGE && -d D/specs: break
#   D = dirname(D)
# if D == "/": KORA_REPO = null
# else: KORA_REPO = D
```

Decidir `OUTPUT_DIR`:

1. Si se pasó `--output <dir>`, usar ese directorio.
2. Si no, y hay contexto KORA, usar `<repo-root>/OPERATIONS/drafts/kora/`.
3. Si no, usar `<input>/atomize-out/` y avisar al usuario.

Crear el directorio si no existe:

```bash
mkdir -p OUTPUT_DIR
```

### Step 1 — Detectar archivos

Ejecutar:

```bash
find INPUT_PATH -maxdepth 3 -type f \( -name "*.md" -o -name "*.txt" -o -name "*.rst" \) | head -25 | sort
```

Contar archivos y estimar palabras:

```bash
find INPUT_PATH -maxdepth 3 -type f \( -name "*.md" -o -name "*.txt" -o -name "*.rst" \) | head -25 | xargs wc -w 2>/dev/null | tail -1
```

Presentar un resumen limpio:

```
Corpus: N archivos · ~M palabras
```

Actuar:

- Si 0 archivos: detener con "No se encontraron archivos soportados en [path]."
- Si > 20 archivos: advertir "⚠ Corpus grande (N archivos). Sin subagentes, la extracción puede ser incompleta. ¿Continuar con los primeros 20, o elegir subcarpeta?" Esperar respuesta.
- Si no: proceder a Step 1.5.

### Step 1.5 — Chunking de archivos grandes para procesamiento

Para cada archivo detectado, estimar word count:

```bash
wc -w "FILEPATH" | awk '{print $1}'
```

- Si ≤ 5.000 palabras: leer el archivo completo en Step 2.
- Si > 5.000 palabras: partir por H2 headers. Cada sección H2 es un chunk independiente. Contenido antes del primer H2 → chunk "Preface".
- Si un H2 sigue excediendo 5.000 palabras: partir por H3.
- Si no hay H2/H3: partir por bloques de párrafos ~3.000 palabras en blanks.

Para procesar chunks: usar Read con `offset`/`limit`. Extraer proposiciones chunk por chunk. Mantener IDs `Pxxx` consecutivos a través de chunks.

### Step 2 — Extraer proposiciones atómicas

Leer cada archivo (o cada chunk) con Read. Para cada:

1. Si tiene frontmatter YAML, extraer `_manifest.urn`, `tags`, `status`, `version` (una vez por archivo).
2. Parsear estructura: identificar H1, H2, H3.
3. Para cada sección con contenido, descomponer en proposiciones atómicas.

**Reglas de descomposición:**

- Cada proposición = el hecho verificable más pequeño autocontenido.
- Oración compuesta con dos hechos independientes → dos proposiciones.
- Tablas y listas: cada fila/item que alguien pueda consultar independientemente es una proposición; si el sentido sólo existe como grupo, preservar la lista como una sola proposición.
- Cada proposición tiene exactamente un tipo del enum cerrado.
- Extraer entidades: roles nombrados, instituciones, instrumentos legales, conceptos, valores de constraint.
- Si una sección tiene tabla, extraer cada fila independiente como proposición separada.
- Si la fuente se contradice consigo misma, crear proposición `tension` nombrando ambas posiciones.

**IDs:** `P001`, `P002`, ... secuenciales **globalmente** a través de todos los archivos y segmentos. No reiniciar por archivo.

**Tracking por proposición:**

- `id`: P### (sequential)
- `text`: texto comprimido (ver Step 3)
- `text_original`: texto original completo (para verificación de fidelidad)
- `type`: uno de los 11 tipos válidos
- `sources`: lista de objetos `{file, location, urn_hint}`
  - `file`: ruta relativa al input
  - `location`: header H2/H3, número de artículo, o sección
  - `urn_hint`: si el archivo tenía frontmatter con URN, guardarlo para anclaje
- `entities`: lista de entidades nombradas

Mantener todas las proposiciones en memoria. No emitir output aún.

### Step 3 — Comprimir proposiciones

Para cada proposición, reescribir `text` con el mínimo de caracteres posible manteniéndola autocontenida (comprensible sin leer `type`).

**Reglas de compresión:**

1. Eliminar artículos, preposiciones redundantes, verbos auxiliares cuando el sentido se preserva.
2. Usar abreviaturas de dominio estándar: HD, IAAS, RCP, SEREMI, CGR, MINSAL, FNDR, SNI, DIPRES, TIC, etc.
3. Usar símbolos cuando reemplazan palabras sin ambigüedad: `≥`, `≤`, `→`, `=`, `/`.
4. Mantener: sujeto + verbo semántico + objeto + constraint.
5. **No** comprimir nombres propios, números, fechas, identificadores legales (números de artículo, ley, decreto).
6. El resultado debe ser entendible por un profesional de dominio sin contexto adicional.

**Validación:** después de comprimir, verificar que el texto comprimido aún contiene todas las entidades de `entities` (o sus abreviaturas estándar). Si falta una entidad, la compresión perdió información — rehacerla.

### Step 4 — Dedup multi-source y detección de conflictos

Este paso es nuevo respecto al formato legacy. Implementa SSOT de `md-spec §7.4`.

Para cada par de proposiciones `(P_a, P_b)`:

1. Si tienen el mismo tipo + mismas entidades clave + predicado semánticamente equivalente:
   - Consolidar en una sola proposición.
   - Fusionar `sources` de ambas.
   - Mantener el `Pxxx` más bajo; re-mapear referencias al ID consolidado.

2. Si tienen entidades clave iguales pero predicados que se contradicen (una afirma X, otra afirma ¬X):
   - **NO** dedup.
   - Emitir proposición adicional de tipo `tension` que nombra ambas posiciones con sus fuentes respectivas.
   - Mantener ambas proposiciones originales preservadas.

3. Si el solapamiento es parcial (mismo tipo, entidades similares pero no idénticas):
   - Conservador: mantener separadas.
   - Anotar la relación como cross-reference en Step 5.

Criterio de equivalencia semántica: mismo tipo + mismo conjunto de entidades clave + mismo predicado modulo variación superficial. En duda, mantener separadas y anotar.

Después del dedup, renumerar IDs para que queden contiguos (sin huecos).

### Step 5 — Construir la jerarquía del artefacto

Determinar la raíz del artefacto:

1. Si los archivos tienen frontmatter con `_manifest.urn`, extraer el segmento compartido (e.g., `urn:salud:kb:hodom-*` → raíz "HODOM").
2. Si la mayoría de archivos comparten el mismo H1, usar ese H1.
3. Si el directorio tiene nombre significativo (no `raw`, `docs`, `src`, `.`), usarlo.
4. Si nada, sintetizar título de 2-5 palabras del H1 + primer párrafo de cada archivo.

Computar `{slug}`: kebab-case de la raíz, sin acentos, sin caracteres no-ASCII. Máximo 40 caracteres.

Si se pasó `--slug`, usar ese valor (normalizado).

**Dominios (secciones H2 del artefacto):** derivar de `source_location` + agrupación semántica de las proposiciones. Un dominio H2 agrupa proposiciones temáticamente coherentes.

### Step 5.5 — Decidir segmentación

Contar `N_props` (proposiciones finales tras dedup) y estimar `W_total` (palabras totales del artefacto con frontmatter + índice + proposiciones).

- Si `N_props ≤ 200` **y** `W_total ≤ 5000`: emitir un único artefacto `atomic-{slug}.md`.
- Si excede uno de los dos: segmentar por dominio (H2) en artefactos `atomic-{slug}-NN.md` cada uno ≤ 5.000 palabras y ≤ 200 props, más un artefacto `atomic-{slug}-index.md` con tabla maestra.

Reglas de corte:

1. Nunca cortar dentro de un dominio H2 (todos los P### de un dominio viven en el mismo segmento).
2. Si un solo dominio excede los umbrales, subdividirlo por subdominios H3 en segmentos separados.
3. Balancear segmentos: preferir ~150 props / ~4.000 palabras por segmento para dejar margen.

### Step 6 — Emitir artefactos KORA/MD

Para cada artefacto a emitir (índice + N segmentos, o artefacto único), generar este contenido:

#### 6.1 Frontmatter obligatorio

```yaml
---
_manifest:
  urn: "urn:kora:kb:atomic-{slug}"           # o -index / -NN
  provenance:
    created_by: "atomize"
    created_at: "{YYYY-MM-DD}"               # fecha actual
    source: "{input-path-absoluto-o-relativo-a-repo}"
version: "1.0.0"
status: draft
tags: [atomic, {ns-semantico-del-corpus}, {dominio-principal}]
lang: "{iso-639-1-del-corpus}"
extensions:
  kora:
    family: atomic
    atomic:
      source_corpus: "{ruta o urn del corpus fuente}"
      n_propositions: {conteo-global-o-del-segmento}
      n_sources: {numero-de-archivos-fuente}
      producer: "urn:kora:skill:atomize"
      segmented: true|false
      segment_index: null | NN                 # solo en segmentos
      total_segments: null | N                 # solo en segmentos y en el índice
      hand_edited: false
---
```

Reglas del frontmatter:

- `tags` tiene mínimo 3. Siempre incluir `atomic` + uno semántico del corpus + uno del dominio principal.
- `lang` coincide con el idioma mayoritario de las fuentes.
- En el **índice** de un corpus segmentado: `n_propositions` es el total global; `segmented: true`, `segment_index: null`, `total_segments: N`.
- En un **segmento**: `n_propositions` es el conteo local; `segmented: true`, `segment_index: NN`, `total_segments: N`.
- En artefacto único (no segmentado): `segmented: false`, `segment_index: null`, `total_segments: null`.

#### 6.2 Cuerpo del artefacto único

```markdown
# Atomic: {Root label}

## Resumen

{K} archivos · {N} proposiciones · {M} entidades · compresión promedio ~{X}%.

## Indice de fuentes

| Fuente | Archivo | URN hint | Rango Pxxx |
| ------ | ------- | -------- | ---------- |
| F01    | decreto-31.md | urn:salud:kb:corpus-decreto31 | P001–P042 |
| F02    | manual-hd.md  | —                             | P043–P087 |

## {Dominio A}

- **P001** · `definition` · texto comprimido · [F01](urn:...#art-1)
- **P002** · `requirement` · texto comprimido
  - [F01](urn:...#art-3)
  - [F02](path/manual-hd.md#cap-2)
- **P003** · `tension` · texto de la contradicción · fuentes divergentes
  - [F01](urn:...#art-12)
  - [F02](path/manual-hd.md#cap-4)

## {Dominio B}

- **P004** · `constraint` · ...
  ...

## Entidades

_(opcional, solo si N ≥ 50 props)_

| Entidad | Menciones | Proposiciones |
| ------- | --------- | ------------- |
| SEREMI  | 8         | P003, P011, P019, ... |
```

#### 6.3 Cuerpo del índice (corpus segmentado)

```markdown
# Atomic: {Root label} — Índice

## Resumen

Corpus segmentado en {N} partes · {Total} proposiciones globales · {K} archivos fuente.

## Indice de fuentes

_(tabla como en §6.2, global)_

## Segmentos

| Segmento | Dominios                     | Rango Pxxx | Props | Artefacto |
| -------- | ---------------------------- | ---------- | ----- | --------- |
| 01       | Definiciones, Alcance        | P001–P132  | 132   | [atomic-{slug}-01](urn:kora:kb:atomic-{slug}-01) |
| 02       | Requisitos, Procedimientos   | P133–P287  | 155   | [atomic-{slug}-02](urn:kora:kb:atomic-{slug}-02) |
| 03       | Excepciones, Plazos, Sanciones | P288–P412 | 125   | [atomic-{slug}-03](urn:kora:kb:atomic-{slug}-03) |
```

#### 6.4 Cuerpo de un segmento

Estructura idéntica a §6.2, con la diferencia de que el `# H1` menciona el número de segmento: `# Atomic: {Root label} — Segmento {NN}`.

### Step 7 — Verificación pre-escritura (md-spec §6.10 + §6.11)

Antes de escribir cualquier artefacto, correr estos checks:

1. **Frontmatter válido**: YAML parseable, `_manifest.urn` con formato `urn:kora:kb:atomic-{slug}[-...]`, `status: draft`, `tags` ≥ 3, `lang` presente.
2. **Enum cerrado de tipos**: cada proposición usa un tipo válido.
3. **IDs únicos**: no hay Pxxx duplicados en un mismo artefacto. En conjunto segmentado, no hay duplicados globales.
4. **Fuentes resolubles**: cada proposición tiene ≥1 fuente; las URNs citadas tienen formato válido.
5. **Headings no truncados**: ningún heading termina con `...`.
6. **Chunk primario recuperable**: cada `##` expresa sujeto o alcance semántico, no ordinal.
7. **FS=100%**: cada proposición tiene `text_original` preservado en memoria; verificar que el texto comprimido preserva cifras, fechas, nombres propios y términos legales del original.
8. **CR**: calcular `CR = len(texto_original_total) / len(texto_comprimido_total)`. Si `CR < 1.5`, imprimir advertencia pero no bloquear.
9. **Segmentación correcta**: cada segmento ≤ 5.000 palabras y ≤ 200 props; el índice suma exactamente los rangos declarados.
10. **Ausencia de labelese**: ningún heading como `#### Tipo`, `#### Path`, `#### Valor`.

Si algún check falla, **no escribir**. Imprimir el diagnóstico y detener.

### Step 8 — Escribir y reportar

Si los checks pasaron, escribir los artefactos con `Write`.

Si `OUTPUT_DIR/atomic-{slug}.md` ya existe:

1. Leer su frontmatter.
2. Si tiene `extensions.kora.atomic.hand_edited: true`, **abortar** con mensaje: "⚠ El artefacto existente fue editado a mano. Use `--output <otro-dir>` o libere `hand_edited: false` manualmente."
3. En otro caso, preguntar: "⚠ `atomic-{slug}.md` ya existe y no está hand-edited. ¿Sobreescribir? (s/n)". Esperar respuesta.

Tras escribir, imprimir:

```
Atomización completa · familia: atomic · productor: urn:kora:skill:atomize

  Artefactos emitidos:
    - OPERATIONS/drafts/kora/atomic-{slug}.md        (N props · W palabras)
    [o la lista de índice + segmentos]

  Estadísticas:
    N proposiciones globales · M entidades · K archivos fuente
    Dedup: X proposiciones consolidadas · Y tensions detectadas
    Compresión promedio: ~Z%

  Siguiente paso:
    kora index
    kora check --strict
    kora promote OPERATIONS/drafts/kora/atomic-{slug}.md
```

Luego mostrar las 3 proposiciones más destacables — priorizar `tension` primero, luego `exclusion`, luego `deadline`. Si no hay, mostrar las 3 con más entidades.

## Honesty Rules

- Nunca inventar una proposición. Si el contenido es ambiguo, usar tipo `tension` y describir ambas interpretaciones.
- Nunca fusionar dos hechos independientes para reducir conteo.
- Nunca omitir una proposición por parecer trivial — si es un hecho distinto, incluirlo.
- Nunca comprimir tan agresivamente que un profesional de dominio no pueda reconstruir el significado.
- Si una fila de tabla contiene un hecho, extraerlo — no resumir la tabla como una proposición.
- Dedup **sólo** cuando dos proposiciones son semánticamente equivalentes; si hay duda, mantener separadas.
- Siempre mostrar el conteo total de proposiciones, `CR` y el número de tensions.

## Edge Cases

- **Archivo sin headers:** tratar todo el archivo como una sección. Usar el filename como label.
- **Archivo con sólo H1:** todo el contenido va bajo una sección con ese H1 como label.
- **Archivo vacío o sólo frontmatter:** saltear, no contar en el total.
- **Archivo en otro idioma:** extraer y comprimir en el idioma fuente. `lang` en el frontmatter del output refleja el mayoritario; si mezcla, usar el dominante y documentar en `source`.
- **Archivo muy largo (> 5.000 palabras):** manejo automático por Step 1.5.
- **Archivos binarios:** ignorar silenciosamente.
- **Directorios anidados:** escanear hasta 3 niveles (Step 1).
- **Corpus sin contexto KORA:** emitir artefacto canónico en `<input>/atomize-out/atomic-{slug}.md` con aviso de que no está enganchado a un repo. El artefacto es portable: puede copiarse a `OPERATIONS/drafts/kora/` de cualquier repo KORA después.
- **Re-ejecución sobre corpus ya atomizado:** si el output existe sin `hand_edited: true`, sobreescribir tras confirmación. Mantener los mismos Pxxx cuando sea posible (estabilidad de IDs para referencias externas); si el contenido cambió demasiado, reinicializar numeración y advertir.

## Integración con KORA

- **Productor canónico de la familia `atomic`** declarado en `specs/knowledge-spec.md §12`.
- **Invariantes del output** definidos en `specs/md-spec.md §5.6` + `§5.6.1`.
- **Pipeline de publicación:** `atomize` → `OPERATIONS/drafts/kora/` → `kora check` → `kora promote` → `KNOWLEDGE/kora/atomic/`.
- **Retrocompatibilidad:** el flag `--legacy` produce el formato plano `_ATOMIC_GRAPH.md`; formato deprecado por `md-spec §10.4`.
