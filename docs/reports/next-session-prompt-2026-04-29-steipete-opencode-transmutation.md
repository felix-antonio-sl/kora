---
_manifest:
  urn: "urn:kora:kb:next-session-prompt-2026-04-29-steipete-opencode-transmutation"
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-29"
    source: "Prompt breve de continuacion posterior al cierre steipete multi-runtime."
version: "1.0.0"
status: publicado
tags: [next-session-prompt, steipete, opencode, openclaw, transmutacion]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-29-steipete-opencode-transmutation"
    - "urn:kora:kb:operational-memory-2026-04-29-steipete-opencode-transmutation"
---

# Prompt de continuacion

Copiar este bloque como mensaje inicial de la proxima sesion:

<prompt>
Trabaja sobre `/home/felix/kora` en `master`, partiendo del cierre documentado
en:

- `docs/reports/handoff-2026-04-29-steipete-opencode-transmutation.md`
- `docs/reports/operational-memory-2026-04-29-steipete-opencode-transmutation.md`

Primero verifica:

```bash
python3 toolchain/kora check --strict
python3 -m unittest discover -s tests
```

Contrato esperado: `30/30 OK` y suite completa verde.

Luego continua con la validacion runtime real de `dev/steipete` y
`fxsl/allan-kelly`:

1. revisar/instalar `artifacts/agents/dev/steipete/_BUILD/claude-code/steipete.md`
2. probar `artifacts/agents/dev/steipete/_BUILD/codex/steipete.md`
3. cargar `artifacts/agents/dev/steipete/_BUILD/opencode/agents/steipete.md`
4. sincronizar `artifacts/agents/dev/steipete/_BUILD/openclaw/workspace/` en OpenClaw y correr doctor
5. repetir el mismo flujo con `artifacts/agents/fxsl/allan-kelly/_BUILD/`
6. reportar cualquier drift entre runtime real y `_transmutation.yml`
</prompt>
