# Quality Gates

No dar por cerrada una atomizacion solo porque el artefacto renderiza o el
lint pasa. Usar estos gates.

## Gate 1 — Estructura

Confirmar que el indice y los dominios reflejan la estructura real:

- aparecen los capitulos o secciones importantes
- no domina un titulo generico unico para todo el bundle
- la segmentacion sigue fronteras estructurales comprensibles

## Gate 2 — Contaminacion

Buscar ruido en el draft:

- `Table of Contents`
- running headers
- page numbers
- `Fig.` / `Figure`
- captions
- footnotes
- copyright / editorial

Si aparecen como proposiciones, rehacer.

## Gate 3 — Anclaje

Spot-check de fuentes:

- abrir varias citas del inicio, medio y final
- verificar que `Lx-Ly` apunte al original correcto
- confirmar que no haya desplazamiento sistematico de lineas

Si las citas no son confiables, el bundle no sirve.

## Gate 4 — Densidad semantica

Preguntas de control:

- el conteo total de proposiciones parece plausible para el tamaño del corpus
- no hay colapso grotesco de contenido sustantivo
- tampoco hay inflacion por partir frases triviales sin valor semantico

Si la densidad es implausible, rehacer.

## Gate 5 — Tipado

Muestrear proposiciones y verificar:

- `fact` no se esta usando como basurero por defecto
- restricciones numericas no quedaron como hechos neutros
- normas, permisos, exclusiones y plazos tienen tipo correcto
- contradicciones reales salen como `tension`

## Gate 6 — Integridad del bundle

Comprobar:

- `Pxxx` unicos globalmente
- `n_propositions` consistente
- indice y segmentos consistentes
- segmentos `100+` detectados correctamente

Usar:

```bash
python3 SKILLS/kora/atomize/scripts/check_atomic_bundle.py <index-o-segmento>
python3 SKILLS/kora/atomize/scripts/review_atomic_quality.py <index-o-segmento>
```

## Gate 7 — Muestreo comparativo

Comparar al menos:

- un bloque inicial del original vs un segmento inicial
- un bloque medio del original vs un segmento medio
- un bloque tardio del original vs un segmento tardio

Si el draft pierde estructura obvia o arrastra ruido claro, no cerrar.

## Gate 8 — Fidelidad semantica

Usar `semantic-fidelity-review.md` y preparar un packet de muestras:

```bash
python3 SKILLS/kora/atomize/scripts/prepare_atomic_fidelity_review.py <index-o-segmento>
```

Ese script no decide la fidelidad semantica. Solo prepara evidencia para que el
agente revise soporte, no-invencion, no-colapso y conservacion de condiciones.
Cuando haya `tension`, el packet debe priorizar esas proposiciones antes que el
muestreo posicional ordinario.

Rechazar si una muestra:

- no esta totalmente soportada por la fuente
- pierde negaciones, condiciones o excepciones
- cambia cantidades, fechas o nombres propios
- fusiona hechos distinguibles

## Gate 9 — Acceptance review persistente

Despues de pasar integridad, calidad editorial y muestreo semantico, escribir
una revision persistente junto al bundle:

```bash
python3 SKILLS/kora/atomize/scripts/review_atomic_acceptance.py <index-o-segmento> --decision accept --summary "Pasa los gates y mantiene fidelidad semantica en las muestras revisadas."
```

Eso genera `atomic-<slug>-review.md` en el mismo directorio del bundle.

Reglas:

- la review debe dejar `publish_ready: true`
- la review debe resumir `tension_count`, `multi_source_count` y otros riesgos
- cualquier edicion posterior del bundle invalida la review anterior
- `publish_atomic.py` debe negarse a promover si la review falta, rechaza o esta vieja

## Regla final

La atomizacion solo esta lista cuando pasa todos los gates y el resultado se
parece al documento recuperado semanticamente, no al texto roto de entrada.

Para fuentes tipo libro/OCR, comparar tambien contra
`golden-case-opm-libro.md`.

Para OCR corto/mediano, comparar tambien contra
`golden-case-ocr-procedure.md`.

Para corpus multiarchivo con repeticion entre documentos, comparar tambien
contra `golden-case-multifile-dedup.md`.

Para corpus multiarchivo con posiciones incompatibles, comparar tambien contra
`golden-case-multifile-tension.md`.

Publicacion canonica:

```bash
python3 SKILLS/kora/atomize/scripts/publish_atomic.py <index-o-segmento>
```
