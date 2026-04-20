---
_manifest:
  urn: "urn:kora:kb:operational-memory-2026-04-20-hitl-fase2-cierre-y-knowledge-contract"
  provenance:
    created_by: "Codex GPT-5 (encarnando steipete)"
    created_at: "2026-04-20"
    source: "Memoria operativa compacta del cierre HITL, Fase 2 y knowledge contract explícito."
version: "1.0.0"
status: publicado
tags: [operational-memory, hitl, fase-2, urgenciologo, knowledge-contract]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-20-hitl-fase2-cierre-y-knowledge-contract"
    - "urn:kora:kb:next-session-prompt-2026-04-20-hitl-fase2-cierre-y-knowledge-contract"
---

# Memoria operativa — cierre HITL, Fase 2 y knowledge contract

## Snapshot numérico

| Métrica | Valor |
|--------|-------|
| Checks registry | 18 |
| `check --strict` | 18/18 verde |
| Suite unittest | 320 OK (`skipped=2`) |
| Deploy status Claude | 1 ok / 7 missing / 0 stale |
| Runtime vivo probado | `claude-code` |
| Agente canario | `salud/urgenciologo` |
| KB foco | `urn:salud:kb:me-dolor-toracico` |

## Invariantes que deben seguir verdaderos

1. `bundle-coherence` existe en el registry.
2. `deploy-status` existe como subcomando CLI.
3. `record-invocation` existe como subcomando CLI.
4. `urgenciologo` en Claude expone `## Knowledge Contract`.
5. `_transmutation.yml` expone `knowledge_contract`.
6. `dolor-toracico.md` mantiene `verified_at`.

## Paths importantes

- Handoff: [handoff-2026-04-20-hitl-fase2-cierre-y-knowledge-contract.md](/Users/felixsanhueza/Developer/kora/docs/reports/handoff-2026-04-20-hitl-fase2-cierre-y-knowledge-contract.md)
- Prompt siguiente: [next-session-prompt-2026-04-20-hitl-fase2-cierre-y-knowledge-contract.md](/Users/felixsanhueza/Developer/kora/docs/reports/next-session-prompt-2026-04-20-hitl-fase2-cierre-y-knowledge-contract.md)
- KB foco: [dolor-toracico.md](/Users/felixsanhueza/Developer/kora/artifacts/knowledge/salud/med-emergencia/dolor-toracico.md)
- Agente: [artifacts/agents/salud/urgenciologo/AGENT.md](/Users/felixsanhueza/Developer/kora/artifacts/agents/salud/urgenciologo/AGENT.md)
- Bundle Claude: [urgenciologo.md](/Users/felixsanhueza/Developer/kora/artifacts/agents/salud/urgenciologo/_BUILD/claude-code/urgenciologo.md)
- Manifest transmutación: [_transmutation.yml](/Users/felixsanhueza/Developer/kora/artifacts/agents/salud/urgenciologo/_BUILD/claude-code/_transmutation.yml)

## Consolidación de memoria

La memoria global de Codex en este entorno es de solo lectura. Por eso la consolidación se dejó en esta memoria operativa del repo, no en `~/.codex/memories/`.

## Riesgos resumidos

- `deploy-status` no endurece `missing`
- JSONL de telemetría no deduplicado
- knowledge contract visible hoy solo en bundle Claude

## Próximo frente recomendado

Abrir **Fase 3** por `P3.2`: mismo componente, segundo runtime.

Objetivo recomendado: `salud/urgenciologo` en `codex`.
