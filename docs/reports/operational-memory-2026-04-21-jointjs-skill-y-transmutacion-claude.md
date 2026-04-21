---
_manifest:
  urn: "urn:kora:kb:operational-memory-2026-04-21-jointjs-skill-y-transmutacion-claude"
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-21"
    source: "Memoria operativa compacta del cierre de la skill JointJS y su transmutación a Claude Code."
version: "1.0.0"
status: publicado
tags: [operational-memory, jointjs, skill, claude-code, transmutacion]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-21-jointjs-skill-y-transmutacion-claude"
    - "urn:kora:kb:next-session-prompt-2026-04-21-jointjs-skill-y-transmutacion-claude"
---

# Memoria operativa — JointJS skill y transmutación Claude

## Snapshot numérico

| Métrica | Valor |
|--------|-------|
| Checks registry | 18 |
| `check --strict` | 18/18 |
| Suite unittest | 321 OK (`skipped=2`) |
| Skill nueva | `kora/jointjs-open-source` |
| Runtime skill soportado nuevo | `claude-code` |

## Invariantes que deben seguir verdaderos

1. `artifacts/skills/kora/jointjs-open-source/SKILL.md` existe y es skill productiva KORA.
2. `transmute --target claude-code --agent kora/jointjs-open-source` funciona.
3. El bundle target queda en `_BUILD/claude-code/<skill-name>/SKILL.md`.
4. `_transmutation.yml` se emite también para la skill transmutada.

## Decisiones compactas

- no se usa `agents/openai.yaml` dentro del repo para esta skill
- la docs oficial de JointJS vive fuera del repo y es SSOT
- la transmutación a Claude usa shape oficial de skills, no subagente

## Próximo frente recomendado

1. Instalar el bundle en `~/.claude/skills/jointjs-open-source/`
2. Probar invocación real en Claude
3. Si funciona, abrir `skill -> codex`
