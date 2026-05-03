# LLM-First Workflow

Usa este skill cuando el trabajo principal es **curacion semantica**, no solo
reescritura mecanica.

## Cuando aplicar este flujo

- Documento unico o carpeta con varios documentos.
- Fuente humana, incompleta o mal formateada.
- Necesidad de reconstruir estructura, no solo copiarla.
- Necesidad de dedup semantico o deteccion de tensiones.

## Regla de oro

El LLM es el motor de atomizacion. Los scripts del repo son enforcement
posterior: lint, promotion, index y chequeos de integridad.

## Secuencia recomendada

1. Hacer triage de la fuente antes de escribir:
   - markdown limpio
   - texto plano / OCR / libro exportado
   - politica o procedimiento
   - corpus multiarchivo
2. Leer toda la fuente relevante antes de escribir.
3. Inferir la estructura semantica real:
   - titulos implicitos
   - definiciones
   - reglas operativas
   - exclusiones
   - plazos
   - restricciones numericas
4. Si la fuente es `.txt` u OCR, cargar `plaintext-book-recovery.md` y fijar
   explicitamente que ruido debe excluirse.
   - si es libro exportado, contrastar con `golden-case-opm-libro.md`
   - si es OCR procedimental corto, contrastar con `golden-case-ocr-procedure.md`
5. Extraer proposiciones minimas y autocontenidas.
6. Tipar cada proposicion con el enum cerrado de `atomic`.
7. Deduplicar por equivalencia de significado, no por igualdad textual.
8. Si dos fuentes sostienen cosas incompatibles, no deduplicar:
   - emitir `tension`
   - nombrar ambas posiciones
   - si el corpus es multiarchivo con repeticion real, contrastar con
     `golden-case-multifile-dedup.md`
   - si el corpus es multiarchivo con conflicto real, contrastar con
     `golden-case-multifile-tension.md`
9. Ordenar el artefacto por bloques tematicos o por source-file si conviene.
10. Segmentar cerca de `15.000` caracteres solo en fronteras estructurales
   coherentes.
11. Muestrear el draft antes de cerrarlo:
   - inicio
   - medio
   - final
   - indice del bundle
12. Pasar `quality-gates.md`.
13. Pasar `semantic-fidelity-review.md` con un packet de muestras.
14. Escribir los drafts directamente en
   `artifacts/knowledge/_SCRIPTORIUM/REVIEW/kora/atomic/`.
15. Escribir una acceptance review persistente:
   - `python3 artifacts/skills/kora/atomize/scripts/review_atomic_acceptance.py <path> --decision accept --summary "..."`
   - esto debe dejar `atomic-<slug>-review.md` junto al bundle
16. Ejecutar validacion mecanica al final:
   - `python3 toolchain/kora lint-md <path-o-dir>`
   - `python3 artifacts/skills/kora/atomize/scripts/publish_atomic.py <draft-o-index>`

## Heuristicas de calidad

- Preservar cifras, fechas, nombres propios y referencias normativas.
- No comprimir de forma destructiva.
- No dejar proposiciones ambiguas que dependan del parrafo anterior.
- No partir una misma regla en varias proposiciones salvo que gane claridad
  real.
- No usar el tipo `fact` por defecto si la proposicion es normativa.
- No aceptar como bueno un draft que todavia contenga TOC, headers, footers,
  captions, epigrafes o footnotes como proposiciones.
- No confiar solo en `lint OK`; el cierre requiere pasar gates editoriales.
- No confiar solo en el conteo o en el shape del indice; la fidelidad se
  comprueba comparando muestras contra la fuente.
- No promover un bundle editado despues de la acceptance review; la review debe
  rehacerse para el estado actual del draft.

## Sobre `atomize`

`atomize` es el productor canonico de la familia `atomic` y la unica ruta
soportada para emitir nuevos artefactos de esa familia.

- `python3 toolchain/kora atomize ...` es la superficie mecanica del mismo
  productor canonico.
- `artifacts/skills/kora/atomize/scripts/atomize.py` es el wrapper portable del skill
  para esa misma superficie.
- Ninguna de esas superficies constituye un modo degradado alternativo.

Si una corrida no logra `FS=100%` o colapsa hechos distinguibles, el problema
no se resuelve cambiando de “modo”: se corrige la atomizacion dentro del mismo
productor canonico.
