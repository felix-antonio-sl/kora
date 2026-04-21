---
_manifest:
  urn: "urn:kora:kb:next-session-prompt-2026-04-21-jointjs-skill-y-transmutacion-claude"
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-21"
    source: "Prompt breve de continuación posterior al cierre de la skill JointJS y su transmutación a Claude Code."
version: "1.0.0"
status: publicado
tags: [next-session-prompt, jointjs, skill, claude-code]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-21-jointjs-skill-y-transmutacion-claude"
    - "urn:kora:kb:operational-memory-2026-04-21-jointjs-skill-y-transmutacion-claude"
---

# Prompt de continuación

Copiar este bloque como mensaje inicial de la próxima sesión:

<prompt>
Trabaja sobre `/Users/felixsanhueza/Developer/kora` en `master`, posterior al cierre documentado en:

- `docs/reports/handoff-2026-04-21-jointjs-skill-y-transmutacion-claude.md`
- `docs/reports/operational-memory-2026-04-21-jointjs-skill-y-transmutacion-claude.md`

Verifica primero:

```bash
python3 toolchain/kora check --strict
python3 -m unittest discover -s tests
python3 toolchain/kora transmute --target claude-code --agent kora/jointjs-open-source
```

Contrato esperado:

- `18/18`
- `321 OK (skipped=2)`
- bundle skill en `artifacts/skills/kora/jointjs-open-source/_BUILD/claude-code/jointjs-open-source/SKILL.md`

Luego:

1. instalar el bundle en `~/.claude/skills/jointjs-open-source/`
2. probar uso real de la skill en Claude contra `https://docs.jointjs.com/`
3. verificar que el agente consulte docs oficiales también para preguntas simples
4. si eso cierra, abrir el gap siguiente: `skill -> codex`
</prompt>
