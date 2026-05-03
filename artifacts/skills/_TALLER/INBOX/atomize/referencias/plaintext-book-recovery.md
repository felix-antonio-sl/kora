# Plaintext / OCR Recovery

Usa este protocolo cuando la fuente sea un `.txt`, OCR, libro exportado,
documento con paginacion incrustada o texto claramente mal formateado.

## Objetivo

Recuperar la estructura semantica real del documento y excluir el paratexto
repetitivo antes de atomizar.

## Preflight minimo

Muestrea siempre cuatro zonas del original:

- primeras `150-250` lineas
- comienzo del primer capitulo o seccion real
- una zona media
- una zona tardia

Determina con ese muestreo:

- donde empieza el cuerpo sustantivo
- como se marcan partes, capitulos y secciones
- que ruido se repite en cada pagina o bloque

## Ruido tipico a excluir

Excluir por defecto salvo que el usuario pida lo contrario:

- portada, blurbs, copyright, ISBN, DOI y creditos editoriales
- `Table of Contents` e indices
- running headers y running footers
- page numbers sueltos
- captions de figura cuando no aportan contenido sustantivo
- urls sueltas y restos de OCR
- epigrafes de apertura de capitulo
- ejercicios y problemas
- notas al pie puramente bibliograficas o editoriales

## Contenido que no se debe perder

No excluir:

- definiciones y teoremas
- reglas operativas y restricciones
- excepciones y exclusiones
- plazos, cifras y cantidades
- ejemplos explicativos que introducen hechos o reglas
- subtitulos reales del cuerpo del capitulo

## Politica de reconstruccion

1. Marcar primero los cortes de `Parte`, `Capitulo` y seccion numerada.
2. Tratar el TOC como ruido aunque use nombres iguales a los capitulos reales.
3. Tomar como cuerpo real el primer bloque donde ya hay prosa continua del
   capitulo, no la portada ni el TOC.
4. Si una nota al pie se parte por salto de pagina, excluirla completa salvo
   que introduzca contenido normativo o conceptual sustantivo.
5. Si una linea parece heading pero en realidad es un running header, excluirla
   y no promoverla a estructura.

## Red flags

Si ves cualquiera de estas señales en el draft atomizado, la corrida sigue
mal:

- el primer segmento contiene la portada o el titulo repetido del libro
- aparece `Table of Contents` como dominio o proposicion
- un heading real desaparece y se reemplaza por dominios genericos
- una proposicion contiene texto de dos paginas pegadas por una nota al pie
- aparecen captions tipo `Fig. 3.2 ...` como hechos autonomos

## Sanity check rapido

Antes de cerrar, comparar:

- un bloque del original del inicio vs el primer segmento util
- un bloque medio vs un segmento medio
- un bloque tardio vs un segmento tardio

La pregunta no es solo si "hay salida", sino si el bundle refleja la
arquitectura real del documento.

Si la fuente se parece a `opm-libro.txt`, usar ademas
`golden-case-opm-libro.md` como baseline concreto de comparacion.

Si la fuente es un procedimiento OCR corto o mediano con headers repetidos,
captions y palabras partidas, comparar tambien contra
`golden-case-ocr-procedure.md`.
