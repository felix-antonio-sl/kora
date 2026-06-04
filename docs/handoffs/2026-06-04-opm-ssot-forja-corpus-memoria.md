---
_manifest:
  urn: "urn:kora:kb:memoria-opm-ssot-forja-corpus-2026-06-04"
  provenance:
    created_by: "Codex"
    created_at: "2026-06-04"
    source: "Memoria operativa derivada del handoff 2026-06-04 opm-ssot-forja-corpus."
version: "1.0.0"
status: publicado
tags: [memoria, opm, forja, ssot, knowledge]
lang: es
extensions:
  kora:
    family: note
---

# Memoria 2026-06-04 - corpus OPM/Forja SSOT ES

- Handoff completo:
  `docs/handoffs/2026-06-04-opm-ssot-forja-corpus.md`.
- Corpus cerrado: reglas v1.2.1, OPL v1.1.3, OPD v1.0.3, metodologia v1.4.4,
  categorial v1.2.4.
- `reglas-opm-estrictas-es` es SSOT primaria y contiene la matriz de autoridad
  de la familia Forja.
- OPL y OPD tienen frontera documental propia; no deben redefinir validez OPM
  ni metodologia.
- `metodologia-forja-es` coordina el proceso de forja, no la ley formal.
- `opm-categorial-es` es puente semantico/categorial no normativo para el
  modelador.
- Opforja permite realizaciones hermanas: la equivalencia horizontal se decide
  por firma de frontera; in-zoom/out-zoom es preservacion vertical
  complementaria.
- Gates finales registrados: `check` 34/34 OK, `lint-md` 0 issues,
  `kb-graph` sin orphans, broken edges ni ciclos en `depends`.
