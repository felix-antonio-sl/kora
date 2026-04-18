# Atomic Output Contract

## Artefacto unico

- Path canonico:
  `KNOWLEDGE/_SCRIPTORIUM/REVIEW/kora/atomic/atomic-{slug}.md`
- `status: draft`
- `extensions.kora.family: atomic`
- `extensions.kora.atomic.producer: urn:kora:artefacto:atomize`

## Bundle segmentado

- Indice:
  `atomic-{slug}-index.md`
- Segmentos:
  `atomic-{slug}-01.md`, `atomic-{slug}-02.md`, ...
- La unicidad de `Pxxx` es global a todo el bundle.
- La tabla del indice usa el contrato de `md-spec`:
  `| Segmento | Rango Pxxx | Dominios |`
  y el segmento resuelve su URN desde la propia celda `Segmento`.

## Secciones obligatorias

- `# <titulo>`
- `## Resumen`
- `## Indice de fuentes`
- uno o mas `##` tematicos con proposiciones

## Forma de proposicion

```md
- **P042** · `requirement` · Texto autocontenido y verificable. · [src:S01:L10-L12](./fuente.md#L10-L12)
```

## Invariantes

- cada `Pxxx` es unico
- el tipo pertenece al enum cerrado
- cada proposicion tiene al menos una fuente resoluble
- `FS=100%` aplica tambien a la particion semantica relevante: no fusionar
  hechos distinguibles del cuerpo sustantivo para bajar conteo
- quitar paratexto irrelevante si; borrar o colapsar contenido sustantivo no
- dedup multi-source solo para hechos equivalentes
- contradicciones reales se expresan como `tension`
- segmentacion cerca de `15.000` caracteres, pero con corte estructural
  coherente
- maximo duro de `200` proposiciones por artefacto que no sea indice
- no debe filtrarse paratexto recurrente como TOC, running headers, page
  numbers, captions, epigrafes o footnotes editoriales
- las citas `Lx-Ly` deben anclar al original real, no a una version
  normalizada con lineas desplazadas
