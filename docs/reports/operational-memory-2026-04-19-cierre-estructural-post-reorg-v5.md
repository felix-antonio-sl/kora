---
_manifest:
  urn: "urn:kora:kb:operational-memory-2026-04-19-cierre-estructural-post-reorg-v5"
  provenance:
    created_by: "OpenAI Codex (encarnando arquitecto-categorico)"
    created_at: "2026-04-19"
    source: "Memoria operativa compacta del cierre estructural posterior al reorg v5."
version: "1.0.0"
status: publicado
tags: [operational-memory, snapshot, structural-closeout, qa, multiagente, mastra]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-19-cierre-estructural-post-reorg-v5"
    - "urn:kora:kb:next-session-prompt-2026-04-19-cierre-estructural-post-reorg-v5"
---

# Memoria operativa — cierre estructural post-reorg v5

Snapshot operativo al cierre de la sesion `2026-04-19`.

## Snapshot numerico

| Metrica | Valor | Comando |
|---------|-------|---------|
| Checks registry | 16 | `python3 toolchain/kora check --strict` |
| Suite unittest | 299 (`skipped=2`) | `python3 -m unittest discover -s tests` |
| Nodos KB | 521 | `python3 toolchain/kora kb-graph --json --orphans` |
| Aristas KB | 654 | `python3 toolchain/kora kb-graph --json --orphans` |
| Huerfanos reales KB | 0 | `python3 toolchain/kora kb-graph --json --orphans` |
| Aristas rotas KB | 0 | `python3 toolchain/kora kb-graph --json --orphans` |
| Runtime targets de transmutacion | 5 (`claude-code`, `codex`, `gemini`, `mastra`, `openclaw`) | `python3 toolchain/kora transmute --help` |
| Specs nuevas de esta sesion | 4 | `qa-spec`, `procesos-spec`, `risk-register-spec`, `multiagente-spec` |
| Runtime extensions nuevas de esta sesion | 1 | `mastra-runtime-extension` |
| Namespace maps de curacion | 10 | `artifacts/knowledge/*/namespace-curation-map.md` |

## Contrato vigente

### Canon constitucional

- `gobernanza v4.4.0`
- `harness-spec v1.1.0`
- `qa-spec v1.0.0`
- `procesos-spec v1.0.0`
- `risk-register-spec v1.0.0`
- `runtime-spec-md v3.8.0`
- `transmutation-spec v1.1.0`
- `multiagente-spec v1.0.0`
- `openclaw-runtime-extension v1.2.0`
- `mastra-runtime-extension v1.0.0`
- `autoria-spec v1.2.0`

### Checks nuevos o ampliados

- `fidelidad-mastra` existe y es obligatorio en `check --strict`.
- `tests/test_cli_smoke.py` exige 5 targets de transmutacion.
- `tests/test_artifacts.py` cubre `qa-spec`, `mastra-runtime-extension` y la
  materializacion de `procesos-spec` / `risk-register-spec` / `multiagente-spec`.

## Invariantes duras

1. `Sigma` discreto vive en `harness-spec`; su lectura enriched vive en
   `qa-spec`.
2. `risk_register` es efecto acumulativo, no lista ornamental.
3. Todo protocolo multiagente debe propagar `session_id`, `protocol_id`,
   ticket de procedencia y piso de calidad.
4. `mastra` es target de transmutacion, no fuente de `ingest`.
5. El grafo KB no debe volver a tener huerfanos reales como estado basal.

## Higiene de trabajo

1. El worktree actual tiene cambios ajenos en
   `artifacts/knowledge/fxsl/opm/opm-ssot-es/*`; no tocarlos ni mezclarlos con
   commits de toolchain/specs.
2. `docs/generated/*` se regeneraron para verificar el estado, pero deben
   commitearse solo en una pasada limpia donde no haya derivaciones de cambios
   ajenos.
3. Si se vuelve a tocar `docs/generated/*`, correr siempre:

```bash
python3 toolchain/kora index
python3 toolchain/kora kb-graph --json --orphans
python3 toolchain/kora check --strict
python3 -m unittest discover -s tests
```

## Siguiente bloque recomendado

1. `168 CM-*` embebidos en productivos (`promover / absorber / descartar`).
2. Promotion backlog en `_FRAGUA/INBOX/` y `_TALLER/INBOX/`.
3. Solo despues de eso: `H9`, `H17`, `H20`, `H22`.
