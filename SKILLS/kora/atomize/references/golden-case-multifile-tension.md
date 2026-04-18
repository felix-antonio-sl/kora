# Golden Case — Multi-File Tension

Usa este caso cuando dos o mas documentos sostienen posiciones incompatibles
sobre el mismo hecho y `atomize` debe preservar ambas posiciones mas una
proposicion `tension`.

## Fuente

- fixtures sinteticos:
  - `tests/fixtures/atomize/multifile-conflict/` — conflicto numerico (`24` vs `48` hours)
  - `tests/fixtures/atomize/multifile-negation-conflict/` — conflicto por negacion (`may` vs `may not`)
  - `tests/fixtures/atomize/multifile-exception-conflict/` — conflicto por excepcion explicita (`applies to all contractors` vs `... except temporary staff`)

## Resultado aceptable

La corrida aceptable sobre este fixture debe producir:

- `4` proposiciones
- `2` proposiciones originales incompatibles:
  - `The operator must log each incident within 24 hours.`
  - `The operator must log each incident within 48 hours.`
- `1` proposicion adicional de tipo `tension`
- `1` proposicion deduplicada compartida:
  - `The duty manager may approve a delayed entry.`
- la `tension` debe citar ambas fuentes
- la `tension` debe vivir en un bloque tipo:
  - `Tensiones entre fuentes · Incident Logging`

En variantes por negacion o excepcion, el principio es el mismo:

- preservar cada posicion original
- agregar `tension`
- no deduplicar como si fueran equivalentes

## Qué rechazar

Rechazar la corrida si:

- una de las dos posiciones desaparece
- las dos posiciones se deduplican como si fueran equivalentes
- se emiten solo las dos proposiciones incompatibles sin una `tension`
- la `tension` no nombra las dos posiciones enfrentadas

## Regla corta

Conflicto real entre fuentes no se resuelve eligiendo una version ni fusionando
la frase. Se preservan ambas y se agrega `tension`.
