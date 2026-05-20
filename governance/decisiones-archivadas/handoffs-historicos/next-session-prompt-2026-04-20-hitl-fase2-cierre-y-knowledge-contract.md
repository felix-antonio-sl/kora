---
_manifest:
  urn: "urn:kora:kb:next-session-prompt-2026-04-20-hitl-fase2-cierre-y-knowledge-contract"
  provenance:
    created_by: "Codex GPT-5 (encarnando steipete)"
    created_at: "2026-04-20"
    source: "Prompt breve de continuación posterior al cierre HITL, Fase 2 y knowledge contract explícito."
version: "1.0.0"
status: publicado
tags: [next-session-prompt, hitl, fase-3, urgenciologo, codex-runtime]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-20-hitl-fase2-cierre-y-knowledge-contract"
    - "urn:kora:kb:operational-memory-2026-04-20-hitl-fase2-cierre-y-knowledge-contract"
---

# Prompt de continuación

Copiar el bloque como mensaje inicial de la próxima sesión en este repo.

<prompt>
Trabaja sobre `/Users/felixsanhueza/Developer/kora` en `master`, posterior al cierre documentado en:

- `docs/reports/handoff-2026-04-20-hitl-fase2-cierre-y-knowledge-contract.md`
- `docs/reports/operational-memory-2026-04-20-hitl-fase2-cierre-y-knowledge-contract.md`

Estado esperado al arrancar:

- `python3 toolchain/kora check --strict` => 18/18 verde
- `python3 -m unittest discover -s tests` => 320 OK (`skipped=2`)
- `python3 toolchain/kora deploy-status` => `salud/urgenciologo` en Claude = ok; resto missing; 0 stale

Hecho ya:

- Fase 0 cerrada en lo reversible
- Fase 1 cerrada con `salud/urgenciologo` + `me-dolor-toracico` + `claude-code`
- Fase 2 cerrada con `invocations/retrieval/lead-time/verified_at/deploy-status/bundle-coherence`
- `knowledge_contract` explícito en `_transmutation.yml` y visible en el bundle Claude

Siguiente paso recomendado:

- Abrir Fase 3 por `P3.2`: correr el mismo componente `salud/urgenciologo` en un segundo runtime, idealmente `codex`
- Si el runtime no proyecta bundle utilizable, cerrar primero ese gap manteniendo visible el `knowledge_contract`

Reglas:

- no reabrir Hermes
- respetar freeze formal de `harness-spec`, `autoria-spec`, `transmutation-spec`
- no degradar el `knowledge_contract` a implícito
- no ejecutar checks/tests en paralelo con `kora index` cuando necesites evidencia limpia
</prompt>
