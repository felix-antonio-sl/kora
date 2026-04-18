# Golden Case — OCR Procedure

Usa este caso cuando la fuente se parece a un procedimiento corto o mediano
extraido por OCR: headers repetidos, page numbers, captions, cortes por guion y
saltos de pagina.

## Fuente

- fixture sintetico:
  `tests/fixtures/atomize/ocr-dirty-procedure.txt`

## Señales de entrada

La fuente incluye a proposito:

- page numbers (`12`, `13`, `14`)
- running header repetido (`OPERATIONS MANUAL 2024`)
- caption (`Figure 1 Incident Flow`)
- corte OCR por guion (`Respon- / se`, `proce- / dure`)
- ruido de paginacion (`Continued on next page`)
- URL suelta

## Resultado aceptable

Una corrida aceptable debe recuperar algo cercano a esto:

- `7` proposiciones
- heading recuperado:
  - `Incident Response Procedure / 1. Scope`
- palabras recompuestas:
  - `Incident Response Procedure`
  - `This procedure applies to all contracted operators.`
- ruido excluido:
  - no aparece `OPERATIONS MANUAL 2024`
  - no aparece `Figure 1 Incident Flow`
  - no aparece `Continued on next page`
- tipado esperable en las primeras muestras:
  - `scope` para `This procedure applies to all contracted operators.`
  - `requirement` para `Operators must log each incident within 24 hours.`
  - `permission` para `Exceptions are permitted only when the duty manager approves the delay.`

## Qué rechazar

Rechazar la corrida si:

- el titulo OCR queda como proposicion en vez de estructura
- las palabras partidas por guion quedan rotas en la proposicion final
- los running headers se mezclan con cuerpo sustantivo
- varias reglas operativas quedan colapsadas en una sola proposicion larga

## Uso práctico

1. cargar `plaintext-book-recovery.md`
2. comparar contra este fixture
3. confirmar que el draft final se parece al resultado aceptable, no al OCR sucio
