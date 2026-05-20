---
_manifest:
  urn: "urn:kora:kb:operational-memory-2026-04-19-h-menores-resueltas"
  provenance:
    created_by: "OpenAI Codex (encarnando cat-thinking)"
    created_at: "2026-04-19"
    source: "Memoria operativa compacta del cierre de H9 H17 H20 H22."
version: "1.0.0"
status: publicado
tags: [operational-memory, h9, h17, h20, h22, snapshot]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-19-h-menores-resueltas"
---

# Memoria operativa — H9 H17 H20 H22 resueltas

## Snapshot numerico

| Metrica | Valor | Comando |
|---------|-------|---------|
| Checks registry | 17 | `python3 toolchain/kora check --strict` |
| Suite unittest | 302 (`skipped=2`) | `python3 -m unittest discover -s tests` |
| Nodos KB | 525 | `python3 toolchain/kora kb-graph --json --orphans` |
| Aristas KB | 668 | `python3 toolchain/kora kb-graph --json --orphans` |
| Huerfanos reales KB | 0 | `python3 toolchain/kora kb-graph --json --orphans` |
| Aristas rotas KB | 0 | `python3 toolchain/kora kb-graph --json --orphans` |
| `traces_requirements` en KB graph | 1 | `python3 toolchain/kora kb-graph --json --orphans` |
| Wiring docs generados | 2 | `docs/generated/agent-wiring.{json,md}` |

## Artefactos nuevos

### Knowledge

- `artifacts/knowledge/kora/sys/requirement-traceability-model.md`
- `artifacts/knowledge/kora/sys/req-knowledge-graph-must-materialize-traces.md`
- `artifacts/knowledge/kora/sys/catalogo-patrones-skills.md`
- `artifacts/knowledge/kora/sys/modelo-organizacional-kora.md`

### Toolchain

- `toolchain/kora_lib/reports.py`
- `toolchain/kora_lib/graph.py`
- `toolchain/kora_lib/kb_graph.py`
- `toolchain/kora_lib/promote.py`

### Generated docs

- `docs/generated/agent-wiring.json`
- `docs/generated/agent-wiring-mermaid.md`

## Decisiones operativas

### H9

- `requirement` se cierra como nodo direccionable + edge de traza, no como
  comentario en prose.
- La relacion nueva es `relations.traces_requirements`.
- La proyeccion en el grafo es `TracesRequirement`.

### H17

- El catalogo de patrones acepta como evidencia:
  - skill productiva
  - staging activo de skills
  - staging activo de agentes si contienen skills embebidas relevantes

### H20

- Se reutiliza el `repo-graph` como source of truth.
- No se introduce un DSL nuevo para handoffs.
- La salida oficial es Mermaid materializado en `docs/generated/`.

### H22

- El modelo organizacional vive como artefacto de conocimiento publicado, no
  como extension constitucional.

## Higiene de trabajo

1. Los cambios de `docs/generated/*` forman parte legitima de esta tanda:
   reflejan `TracesRequirement`, wiring Mermaid y el aumento de nodos/aristas.
2. `AGENTS.md` en la raiz sigue local/no-trackeado; no fue absorbido al commit.
3. El backup local del residual `AGENTS/` permanece fuera del repo en:
   `/Users/felixsanhueza/Developer/_backups/kora-local-residuals/AGENTS-20260418-192108`

## Siguiente bloque recomendado

1. `H2-artifacts` — clasificacion de `168 CM-*`
2. Promocion de staging (`_FRAGUA`, `_TALLER`)
