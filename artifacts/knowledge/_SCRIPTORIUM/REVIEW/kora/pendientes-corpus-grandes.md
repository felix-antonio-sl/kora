---
_manifest:
  urn: "urn:kora:kb:pendientes-corpus-grandes-inbox-2026-04-23"
  provenance:
    created_by: "FS"
    created_at: "2026-04-23"
    source: "Registro de corpus grandes en artifacts/knowledge/_SCRIPTORIUM/INBOX/ que requieren procesamiento con atomize u otro pipeline especializado; no procesables como koraficacion directa a un solo artefacto"
version: "1.0.0"
status: borrador
tags: [pendientes, corpus-grande, atomize, inbox, intake]
lang: es
extensions:
  kora:
    family: catalog
---

# Pendientes: Corpus Grandes en SCRIPTORIUM/INBOX

## Naturaleza del artefacto

Registro de materiales en `artifacts/knowledge/_SCRIPTORIUM/INBOX/` que por su tamano, formato o densidad semantica NO fueron procesables como koraficacion directa a un artefacto KORA/MD unico durante la ronda del 2026-04-23. Requieren procesamiento dedicado via `urn:kora:artefacto:atomize` u otro pipeline.

## Estado tras ronda 2026-04-24

### Procesado

- `Procrastination - Fuschia M. Sirois.txt` atomizado como bundle segmentado `urn:pro:kb:atomic-procrastination-sirois-*` en `artifacts/knowledge/_SCRIPTORIUM/REVIEW/pro/atomic/`.
- `curso-dov-dori/` atomizado por archivo como `urn:fxsl:kb:atomic-opm-curso-*` en `artifacts/knowledge/_SCRIPTORIUM/REVIEW/fxsl/atomic/`.
- `opm/transcripciones-videos-opcloud.txt` atomizado como `urn:fxsl:kb:atomic-opcloud-tutorials-*` en `artifacts/knowledge/_SCRIPTORIUM/REVIEW/fxsl/atomic/`.
- `opm-libro.txt` revisado contra `opm-libro-curado/`: duplica el libro ya curado, con portada/ruido adicional. No se atomizo de nuevo.
- `dankoe_articles_full.json` convertido a articulos MD en `artifacts/knowledge/_SCRIPTORIUM/REVIEW/korvo/dankoe/`.
- `seleccion-dan.json` convertido a catalogo curado en `artifacts/knowledge/_SCRIPTORIUM/REVIEW/korvo/dankoe-seleccion-curada.md`.
- `sii/documents.json` y `sii/questions.json` convertidos a datasets MD segmentados en `artifacts/knowledge/_SCRIPTORIUM/REVIEW/sii/datasets/`.
- `legal/15869-19 y 16821-19 ... IA.docx` convertido a `artifacts/knowledge/_SCRIPTORIUM/REVIEW/legal/ley-ia-chile-boletines-15869-19-16821-19.md`.
- `fxsl/gist/*.ttl` registrados como recursos crudos en `artifacts/agents/_FRAGUA/REVIEW/ontologista-gist/AGENT.md`.
- `*/local-machine-inventory-2026-04-22.md` eliminado de INBOX.

### Residuales

| Archivo o directorio | Estado | Plan |
|----------------------|--------|------|
| `salud/Oxford Handbook of Emergency Medicine ... libgen.li.pdf` | PDF externo/copyright | Mantener como referencia externa; no koraficar. |
| `salud/ARSENAL AFT EDITABLE_MAYO-24.pdf` | PDF | Decidir si es corpus interno convertible o referencia externa. |
| `salud/perfil-urgenciologo.md`, `salud/razo-urg.md`, `salud/toc_med-urg.md` | MD | Cubiertos por `salud/artefacto/urgenciologo`; no procesar salvo reemplazo explicito del agente productivo. |
| `wikiguias_corpus_tde/README.md` | README | Ampliar a knowledge note. |
| `pro/` | Directorio | Revisar si quedan fuentes no cubiertas por Procrastination. |
| Atomics nuevos | REVIEW | Requieren acceptance review antes de `kora promote`. |
| `opm-libro-curado/`, `fxsl/opm-methodology/` | REVIEW/indexado | Promover individualmente cuando la curacion sea estable. |

## Proximos pasos sugeridos

1. Revisar semanticamente los atomics generados y emitir acceptance reviews.
2. Decidir si `ARSENAL AFT EDITABLE_MAYO-24.pdf` es corpus interno convertible.
3. Ampliar `wikiguias_corpus_tde/README.md` a note KORA/MD.
4. Promover capitulos OPM de a uno si se considera estable la curacion.
