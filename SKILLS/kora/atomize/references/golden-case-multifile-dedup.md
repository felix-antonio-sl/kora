# Golden Case — Multi-File Dedup

Usa este caso cuando la fuente sea un corpus pequeño de varias politicas o
procedimientos con enunciados repetidos entre archivos.

## Fuente

- fixture sintetico:
  `tests/fixtures/atomize/multifile-dedup/`

## Objetivo

Verificar que `atomize` no replique como proposiciones separadas un mismo
enunciado sustantivo cuando aparece en varios documentos.

## Resultado aceptable

La corrida aceptable sobre este fixture debe producir:

- `4` proposiciones unicas
- `3` fuentes en la proposicion fusionada:
  - `The operator must log each incident within 24 hours.`
- un solo enunciado consolidado con sublista multi-source
- el resto de las proposiciones conservadas por separado:
  - `The duty manager may approve a delayed entry.`
  - `The platform stores each log entry for 90 days.`
  - `The audit team may request the original attachments.`

## Qué rechazar

Rechazar la corrida si:

- el enunciado repetido aparece duplicado o triplicado
- se pierde la multiplicidad de fuentes al deduplicar
- se fusionan tambien proposiciones no equivalentes solo por compartir tema
- la proposicion consolidada toma wording hibrido no soportado por ninguna fuente

## Regla corta

Dedup correcto no es “quedar con menos proposiciones” sino “quedar con las
mismas afirmaciones unicas y todas sus fuentes”.
