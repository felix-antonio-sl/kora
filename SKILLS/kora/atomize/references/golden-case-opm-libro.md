# Golden Case — `opm-libro`

Usa este caso como patron cuando la fuente se parece a un libro exportado,
OCR, PDF convertido a `.txt` o documento largo con paginacion incrustada.

## Fuente

- original:
  `/home/felix/kora/KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro.txt`
- bundle malo inicial:
  `KNOWLEDGE/_SCRIPTORIUM/REVIEW/kora/atomic/atomic-opm-libro-*`
- bundle aceptable de referencia:
  `KNOWLEDGE/_SCRIPTORIUM/REVIEW/kora/atomic/atomic-opm-libro-rebuilt-*`

## Sintomas de corrida mala

La primera corrida mala tenia señales evidentes:

- `138` proposiciones para `~825k` caracteres
- `32` segmentos con muchos de `1-4` proposiciones
- dominios genericos como `opm libro (Parte 01)` en vez de capitulos reales
- contenido de portada, TOC y prefacio mezclado sin jerarquia confiable
- citas formalmente validas pero no suficientemente controladas editorialmente

Ejemplos de olor malo:

- el indice no mostraba capitulos reales
- el primer segmento contenia ruido de portada
- habia segmentos minusculos pese al tamaño del corpus

## Sintomas de corrida aceptable

La corrida reconstruida de referencia muestra el minimo que deberia verse:

- `4199` proposiciones
- `81` segmentos
- capitulos y secciones reales en el indice:
  - `Chapter 1 Ready to Start Modeling?`
  - `1.1 The Automatic Crash Response System`
  - `Chapter 21 Complexity Management: Refinement and Abstraction`
- anchors `Lx-Ly` alineados con el `.txt` original
- `check_atomic_bundle.py` en verde
- `review_atomic_quality.py` ya no marca densidad baja ni microsegmentos

No significa que el bundle rebuilt sea perfecto. Todavia puede arrastrar
residuos como captions o frases de borde. Pero esta claramente del lado
correcto de la comparacion.

## Regla de comparacion

Si la corrida nueva se parece mas al bundle malo que al rebuilt, rechazar.

Preguntas de control:

- el conteo total esta en el orden correcto de magnitud
- aparecen capitulos y secciones reales del libro
- desaparecen TOC, page numbers y running headers
- no hay docenas de segmentos diminutos
- el inicio del bundle ya es cuerpo sustantivo o prefacio real, no portada

## Uso practico

Cuando la fuente tenga esta forma:

1. leer `plaintext-book-recovery.md`
2. usar este caso como baseline editorial
3. correr:

```bash
python3 SKILLS/kora/atomize/scripts/check_atomic_bundle.py <index>
python3 SKILLS/kora/atomize/scripts/review_atomic_quality.py <index>
```

4. muestrear:
   - un segmento inicial
   - un segmento medio
   - un segmento tardio
5. comparar contra este baseline antes de cerrar

## Regla corta

Para fuentes tipo libro/OCR, una corrida con pocas decenas o pocos cientos de
proposiciones para cientos de miles de caracteres casi seguro esta mal.
