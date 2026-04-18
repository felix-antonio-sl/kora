---
_manifest:
  urn: "urn:kora:skill:atomize:1.0.0"
  type: lazy_load_endofunctor
name: atomize
description: >-
  Productor canonico y unica via soportada de emision para la familia
  documental `atomic` (md-spec v7.1 §5.6, knowledge-spec §12). Skill
  runtime-agnostic para Claude Code y Codex: transforma uno o varios
  documentos humanos en artefactos KORA/MD de familia `atomic`. El LLM hace la
  extraccion semantica, tipado, dedup, deteccion de tensiones y reparacion
  estructural; los scripts del repo quedan como capa de enforcement posterior.
  Output canonico:
  `KNOWLEDGE/_SCRIPTORIUM/REVIEW/kora/atomic/atomic-{slug}.md`.
allowed-tools: Read Glob Write Bash
extensions:
  kora:
    # Vector ontologico PMI × LFS (harness-spec v1.0)
    harness_vector:
      pi: 2              # plan ramificado (7 pasos + segmentacion + dedup)
      mu: 0              # sin materia propia (ejecutor externo)
      xi: 1              # interaccion atomica (invocacion → output)
      lambda: 0          # individual
      phi: 1             # instrumental
      sigma: [1, 1, 3, 1, 0]  # safety: 1, fairness: 1, transparency: 3, accountability: 1, sustainability: 0
    presentation: state-primary
    skill_freedom: medium
    atlas:
      harness_name: disciplina
      form: skill-standard
      hcai_metaphor: supertool
metadata:
  kora:
    urn: "urn:kora:skill:atomize:1.0.0"
    lifecycle:
      status: active
      created: "2026-04-16"
      updated: "2026-04-18"
    tools: ["Read", "Glob", "Write", "Bash"]
    knowledge:
      - "urn:kora:kb:md-spec"
      - "urn:kora:kb:knowledge-spec"
    composable_with: []
    domain: ["knowledge", "atomic", "koraficacion"]
    level: L1
---

# Atomize — Productor canonico de la familia `atomic`

## Purpose

Transforma uno o varios documentos humanos en un artefacto KORA/MD de familia
`atomic`, conformado a `md-spec §5.6` y al registro de productores canonicos
de `knowledge-spec §12`. La semantica fuerte vive en el modelo: extraer
proposiciones, reparar estructura implicita, clasificar tipos, deduplicar por
equivalencia y detectar tensiones entre fuentes. El resultado se emite como
artefacto direccionable por LLMs, util para Claude Code y Codex.

Este skill es el **productor canonico de la familia `atomic`**: es la unica
herramienta autorizada para generar artefactos de esa familia cumpliendo sus
invariantes.

Regla operativa: no confiar en la forma superficial del input. Una fuente
`.txt`, OCR o export roto puede contener la estructura correcta mezclada con
TOC, running headers, page numbers, captions, epigrafes o notas al pie. El
trabajo del skill es recuperar la estructura y excluir el ruido, no copiarlo.

## Input / Output

**Input:**
- Path a una carpeta con documentos (.md, .txt, .rst) hasta 3 niveles de
  profundidad.
- Tambien puede ser un **solo documento**; no requiere corpus multiarchivo.
- Flags opcionales: `--slug`, `--output`.

**Output canonico (pipeline descentralizado v8):**
- `KNOWLEDGE/_SCRIPTORIUM/REVIEW/kora/atomic/atomic-{slug}.md` si el corpus
  cabe en un artefacto coherente sin superar el maximo duro de 200
  proposiciones.
- `KNOWLEDGE/_SCRIPTORIUM/REVIEW/kora/atomic/atomic-{slug}-index.md` + N
  segmentos `atomic-{slug}-{NN}.md` si se requiere segmentacion.

La referencia de segmentacion es `~15.000` caracteres por artefacto, pero no
es un limite fijo: el corte debe hacerse lo mas cerca posible de ese tamaño
sin romper la estructura del contenido.

Al promover via `kora promote`, el artefacto migra a `KNOWLEDGE/kora/atomic/`
con `status: published`.

**Modo unico de operacion:**
- `atomize` es el unico productor soportado para emitir artefactos `atomic`.
- El skill y `python3 scripts/kora atomize ...` son dos superficies del mismo
  productor canonico; no son modos semanticos alternativos.
- Ningun scaffold, wrapper auxiliar o salida degradada cuenta como opcion
  equivalente para publicar familia `atomic`.

**Criterio de cierre semantico:**
- `atomic` cierra solo con `FS=100%` segun `md-spec §6.11` y `§7.3`.
- Una corrida de `atomize` **NO** autoriza publicar un artefacto si colapsa
  hechos distinguibles del cuerpo sustantivo o si reduce conteo por fusion
  editorial en vez de dedup real.
- Quitar paratexto irrelevante (blurbs, copyright, TOC, boilerplate) es
  correcto; comprimir contenido sustantivo fusionando afirmaciones distintas no
  lo es.
- Regla corta: si una corrida `colapsa hechos distinguibles`, no cerro la
  atomizacion; vuelvo a curar semanticamente.

**URNs asignados** (templates, no URNs resolubles):

```
# artefacto unico
urn:kora:kb:atomic-<slug>

# corpus segmentado
urn:kora:kb:atomic-<slug>-index
urn:kora:kb:atomic-<slug>-<NN>
```

**Frontmatter emitido:**
- `status: draft` (pasa por `kora promote` para publicar).
- `extensions.kora.family: atomic`
- `extensions.kora.atomic.producer: "urn:kora:skill:atomize:1.0.0"`
- `extensions.kora.atomic.source_corpus`, `n_propositions`, `segmented`,
  `segment_index`, `segment_count`, `hand_edited`.

## Procedimiento

1. **Triage de fuente** — identificar si la entrada es:
   - markdown limpio o semiestructurado
   - texto plano libro/OCR/export
   - politica/procedimiento con listas/tablas
   - corpus multiarchivo
2. **Inventario de estructura y ruido** — detectar antes de escribir:
   - cortes reales: partes, capitulos, secciones
   - ruido recurrente: TOC, page numbers, running headers, captions,
     footnotes, copyright, urls sueltas, ejercicios
3. **Reconstruir el esquema del contenido** — headings implicitos, listas,
   tablas, definiciones, reglas, plazos, exclusiones y excepciones.
4. **Extraer proposiciones atomicas** — cada una autocontenida, verificable y
   con al menos una ancla de fuente resoluble al original.
5. **Clasificar semanticamente** — usar el enum cerrado de `atomic`; no tipar
   por heuristica superficial si el contexto semantico dice otra cosa.
6. **Deduplicar por equivalencia** — fusionar hechos iguales aunque cambie la
   redaccion. Si hay contradiccion real entre fuentes, emitir `tension`. No
   fusionar hechos distinguibles del mismo parrafo solo para reducir conteo.
7. **Segmentar con criterio estructural** — referencia blanda `~15.000`
   caracteres, limite duro `200` proposiciones, sin cortar listas/tablas/
   parrafos en puntos arbitrarios.
8. **Muestrear el resultado antes de cerrarlo**:
   - un segmento inicial
   - un segmento medio
   - un segmento tardio
   - el indice del bundle si existe
9. **Escribir drafts canonicos** en
   `KNOWLEDGE/_SCRIPTORIUM/REVIEW/kora/atomic/`.
10. **Validar y publicar** — usar `kora lint-md`, `kora promote` y `kora index`
    como enforcement mecanico posterior.

## Modo de recuperacion obligatoria

Cuando la fuente sea `.txt`, OCR, libro exportado o documento claramente mal
formateado:

- cargar `references/plaintext-book-recovery.md`
- cargar `references/golden-case-opm-libro.md` si la fuente se parece a un
  libro exportado o a un `.txt` largo con paginacion incrustada
- muestrear el original antes de atomizar:
  - primeras 150-250 lineas
  - primer capitulo real
  - una zona media
  - una zona tardia
- fijar explicitamente:
  - donde empieza el cuerpo sustantivo
  - cuales son los verdaderos cortes de capitulo/seccion
  - que clases de ruido deben excluirse
- no cerrar la corrida hasta pasar `references/quality-gates.md`

No basta con que el lint pase. Una corrida puede ser formalmente valida y a la
vez semanticamente mala.

## Criterios de rechazo

Rechazar y rehacer la atomizacion si ocurre cualquiera de estos casos:

- el conteo de proposiciones es implausiblemente bajo para el tamaño y densidad
  del corpus
- el indice muestra dominios genericos o muchos segmentos diminutos sin razon
  editorial clara
- se filtraron TOC, running headers, page numbers, captions, epigrafes o notas
  al pie como proposiciones
- las fuentes apuntan a lineas desplazadas o no verificables en el original
- se perdieron capitulos o subsecciones obvias del documento
- se fusionaron hechos distinguibles para bajar conteo
- la segmentacion corta en puntos arbitrarios y no en fronteras estructurales

Regla corta: `lint OK` no equivale a `atomizacion buena`.

## Resources

### Scripts
- `scripts/atomize.py` — invoca el productor canonico `kora atomize` desde el
  bundle portable del skill; no es un modo alternativo.
- `scripts/validate_atomic.py` — corre `kora lint-md` sobre drafts o
  artefactos `atomic` ya emitidos.
- `scripts/check_atomic_bundle.py` — inspecciona un bundle `atomic`,
  resume roles/cantidades y detecta fallas de integridad o IDs duplicados.
- `scripts/review_atomic_quality.py` — corre una pasada editorial sobre un
  bundle: contaminacion por paratexto, microsegmentos y anclajes sospechosos.
- `scripts/prepare_atomic_fidelity_review.py` — prepara un packet de evidencia
  para revisar fidelidad semantica con muestras de proposiciones y excerpts del
  original; no dicta el juicio semantico por si solo.
- `scripts/review_atomic_acceptance.py` — escribe un artefacto persistente
  `atomic-<slug>-review.md` con gates, packet de fidelidad y veredicto
  explicito `accept` o `reject`.
- `scripts/publish_atomic.py` — ejecuta `kora promote` solo si existe una
  review aceptada y fresca para el bundle; luego reconstruye el catalogo con
  `kora index`.

### References
- `references/llm-first-workflow.md` — playbook runtime-agnostic para Claude
  Code y Codex; define como usar el LLM como motor semantico principal.
- `references/atomic-output-contract.md` — contrato compacto del artefacto
  final: frontmatter, forma de proposicion, bundle segmentado e invariantes de
  validacion.
- `references/plaintext-book-recovery.md` — protocolo de recuperacion para
  `.txt`, OCR y libros exportados: triage, exclusion de ruido y reconstruccion
  estructural.
- `references/golden-case-opm-libro.md` — caso patron real de comparacion:
  corrida mala vs corrida aceptable para un libro exportado a `.txt`.
- `references/golden-case-ocr-procedure.md` — fixture corto de OCR/procedimiento
  con running headers, captions y guiones partidos; baseline de recuperacion.
- `references/golden-case-multifile-dedup.md` — fixture multiarchivo para
  validar dedup real sin perder multiplicidad de fuentes.
- `references/golden-case-multifile-tension.md` — fixture multiarchivo para
  conflicto real entre fuentes: preservar ambas posiciones y agregar `tension`.
- `references/quality-gates.md` — gates de calidad para decidir si una
  atomizacion debe aceptarse o rehacerse.
- `references/semantic-fidelity-review.md` — protocolo de revision semantica:
  soporte, no-invencion, no-colapso y conservacion de condiciones.

## Signature Output

- Artefactos conformes a `md-spec §5.6` familia `atomic`.
- `## Indice de fuentes` obligatorio.
- Proposiciones con formato `- **Pxxx** · \`tipo\` · texto · [src](...)` o con
  sublista de fuentes en dedup multi-source.
- FS=100% sobre cifras, fechas, excepciones, nombres propios y referencias
  legales, y sobre la particion semantica relevante del cuerpo sustantivo.
- IDs `Pxxx` unicos (globalmente en conjunto segmentado).
- `status: draft` en `KNOWLEDGE/_SCRIPTORIUM/REVIEW/kora/atomic/`.

## Retrocompatibilidad

El CLI integrado del repo **NO** expone un modo `--legacy`. El formato plano
`_ATOMIC_GRAPH.md` sigue deprecado por `md-spec §10.4` y queda fuera del flujo
canonico soportado por `scripts/kora`.

## Relacion con otros artefactos

- Citado por: `specs/knowledge-spec.md §12.2` como productor canonico de
  familia `atomic`.
- Consume invariantes de: `specs/md-spec.md §5.6` y `§5.6.1`.
- Pipeline de publicacion: atomize -> `KNOWLEDGE/_SCRIPTORIUM/REVIEW/kora/atomic/`
  -> `kora check` -> `kora promote` -> `KNOWLEDGE/kora/atomic/`.
- Compatible con runtimes tipo skills/agentskills.io y uso directo en Claude
  Code y Codex sin cambiar el contrato del output.
