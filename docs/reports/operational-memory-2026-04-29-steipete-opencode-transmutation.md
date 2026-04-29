---
_manifest:
  urn: "urn:kora:kb:operational-memory-2026-04-29-steipete-opencode-transmutation"
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-29"
    source: "Memoria operativa compacta del cierre steipete/allan-kelly + transmutacion multi-runtime y soporte material de agentes Codex/OpenCode/OpenClaw."
version: "1.0.0"
status: publicado
tags: [operational-memory, steipete, allan-kelly, opencode, openclaw, transmutacion]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-29-steipete-opencode-transmutation"
    - "urn:dev:artefacto:steipete"
    - "urn:fxsl:artefacto:allan-kelly"
    - "urn:dev:artefacto:ship-discipline"
---

# Memoria Operativa - Steipete Multi-Runtime

## Snapshot

| Item | Estado |
|------|--------|
| Repo | `/home/felix/kora` |
| Rama | `master` |
| Agente dev | `artifacts/agents/dev/steipete/AGENT.md` |
| Agente fxsl | `artifacts/agents/fxsl/allan-kelly/AGENT.md` |
| Skill nuclear | `artifacts/skills/dev/ship-discipline/SKILL.md` |
| Toolchain principal | `toolchain/kora_lib/transmute.py` |
| Handoff rector | `docs/reports/handoff-2026-04-29-steipete-opencode-transmutation.md` |

## Hechos Durables

1. No usar lenguaje de clon para `steipete` ni `allan-kelly`; ambos son
   personas sinteticas inspiradas y no afiliadas a las personas reales.
2. Commit nunca es permiso implicito: `ship-discipline` y `steipete` cierran
   como patch listo salvo autorizacion explicita.
3. `opencode` forma parte del regimen de transmutacion y del schema de
   authoring KORA.
4. `kora transmute` para agentes debe emitir artefacto material, no solo
   `_transmutation.yml`, para:
   - `claude-code`: `{name}.md`
   - `codex`: `{name}.md`
   - `opencode`: `agents/{name}.md`
   - `openclaw`: `workspace/*.md`, `config/openclaw.json5`, `DEPLOY.md`
5. `kora transmute` para skills productivas soporta `openclaw` y emite
   `skills/{name}/SKILL.md`.
6. `review_atomic_acceptance.py` y `promote.py` comparten la regla: solo
   sufijos numericos cortos `-NN` o `-NNN` son segmentos atomic; sufijos
   numericos largos pueden ser parte del slug.

## Validacion Base

- `python3 toolchain/kora check --strict`: 30/30 OK.
- `python3 -m unittest discover -s tests`: 334 OK, 1 skipped.
- `git diff --check`: OK.

## Continuidad

Toda sesion posterior debe partir del handoff
`docs/reports/handoff-2026-04-29-steipete-opencode-transmutation.md`.

Invariante a conservar: cuando se agregue un nuevo runtime target a la CLI,
tambien debe quedar alineado en schema, specs, transmutation schema, emisores
materiales y tests de regresion.
