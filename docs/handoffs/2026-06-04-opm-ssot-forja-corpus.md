---
_manifest:
  urn: "urn:kora:kb:handoff-opm-ssot-forja-corpus-2026-06-04"
  provenance:
    created_by: "Codex"
    created_at: "2026-06-04"
    source: "Cierre operativo de integracion del corpus OPM/Forja en artifacts/knowledge/fxsl/opm/opm-ssot-es."
version: "1.0.0"
status: publicado
tags: [handoff, opm, forja, ssot, knowledge, kora-md]
lang: es
extensions:
  kora:
    family: note
---

# Handoff 2026-06-04 - corpus OPM/Forja SSOT ES

## Estado Actual

El corpus OPM/Forja en español queda integrado como familia autocontenida de
cinco artefactos KORA/MD:

- `urn:fxsl:kb:reglas-opm-estrictas-es` v1.2.1.
- `urn:fxsl:kb:spec-forja-opl-es` v1.1.3.
- `urn:fxsl:kb:spec-forja-opd-es` v1.0.3.
- `urn:fxsl:kb:metodologia-forja-opm-es` v1.4.4.
- `urn:fxsl:kb:opm-categorial-es` v1.2.4.

La SSOT primaria operacional es `reglas-opm-estrictas-es`. Las specs OPD/OPL
definen frontera documental propia y remiten a la matriz de autoridad de reglas
para evitar duplicacion normativa. `metodologia-forja-es` queda como protocolo
de trabajo y `opm-categorial-es` como puente semantico/categorial no normativo
para el modelador.

## Decisiones

- `reglas-opm-estrictas-es` concentra las reglas formales, la matriz de familia
  Forja y la precedencia entre validez OPM, superficie OPD/OPL, metodo Forja y
  semantica categorial.
- `spec-forja-opl-es` no redefine OPM ni OPD: gobierna la superficie textual
  OPL, su gramatica, normalizacion, errores y roundtrip asociado.
- `spec-forja-opd-es` no redefine OPM ni OPL: gobierna la superficie grafica
  OPD y su contrato de equivalencia con OPL.
- `metodologia-forja-es` coordina uso humano-agente, fases de divergencia,
  evaluacion, consolidacion y chequeo sin duplicar reglas ejecutables.
- `opm-categorial-es` interpreta roles, fronteras, realizaciones y equivalencia
  como puente de razonamiento. No crea obligacion adicional para el checker.
- Opforja puede trabajar con realizaciones hermanas de una misma funcion; la
  equivalencia se decide por firma de frontera y el caso in-zoom/out-zoom queda
  como preservacion vertical complementaria.

## Artefactos Relevantes

- `artifacts/knowledge/fxsl/opm/opm-ssot-es/reglas-opm-estrictas-es.md`
- `artifacts/knowledge/fxsl/opm/opm-ssot-es/spec-forja-opl-es.md`
- `artifacts/knowledge/fxsl/opm/opm-ssot-es/spec-forja-opd-es.md`
- `artifacts/knowledge/fxsl/opm/opm-ssot-es/metodologia-forja-es.md`
- `artifacts/knowledge/fxsl/opm/opm-ssot-es/opm-categorial-es.md`

## Validacion Ejecutada

Gates finales sobre el repo KORA:

```bash
python3 toolchain/kora check --strict --path artifacts/knowledge/fxsl/opm/opm-ssot-es
python3 toolchain/kora lint-md artifacts/knowledge/fxsl/opm/opm-ssot-es
python3 toolchain/kora kb-graph --json --orphans
```

Resultado registrado: `check` 34/34 OK, `lint-md` 0 issues, `kb-graph` sin
orphans, broken edges ni ciclos en `depends`.

## Pendientes

- Mantener alineados los checks de `opforja` con las reglas finales de
  equivalencia horizontal de realizaciones hermanas y preservacion vertical
  in-zoom/out-zoom.
- Si se introduce una nueva regla ejecutable, agregarla primero a
  `reglas-opm-estrictas-es` y despues a specs o metodologia solo como remision.
- Si se agregan nuevos ejemplos OPD/OPL, validar que no dupliquen definiciones
  normativas ya concentradas en la matriz de familia.

## Supuestos

- El corpus objetivo es el subtree
  `artifacts/knowledge/fxsl/opm/opm-ssot-es`.
- Las versiones citadas son las vigentes al cierre del 2026-06-04.
- `docs/canon-opm/reglas-opm-estrictas.md` sigue siendo puente local derivado,
  no fuente primaria.

## Riesgos

- Riesgo de deriva si consumidores externos siguen citando paths locales en vez
  de URNs KORA.
- Riesgo de duplicacion futura si cambios en OPD/OPL intentan reabrir reglas
  formales ya gobernadas por `reglas-opm-estrictas-es`.
- Riesgo de mismatch operativo si `opforja` implementa equivalencia de frontera
  con nombres de roles pero no con la firma semantica declarada por el corpus.
