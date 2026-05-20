---
_manifest:
  urn: "urn:kora:kb:next-session-prompt-2026-04-28-openclaw-salubrista-urgenciologo"
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-28"
    source: "Prompt breve de continuacion posterior al handoff OpenClaw salubrista/urgenciologo."
version: "1.0.0"
status: publicado
tags: [next-session-prompt, openclaw, salubrista, urgenciologo, deploy]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-28-openclaw-salubrista-urgenciologo"
    - "urn:kora:kb:operational-memory-2026-04-27-openclaw-kora-live-kb"
---

# Prompt de Continuacion

Copiar este bloque como mensaje inicial de la proxima sesion:

<prompt>
Trabaja sobre `/home/felix/kora` en `master`, continuando desde
`docs/reports/handoff-2026-04-28-openclaw-salubrista-urgenciologo.md`.

Primero verifica:

```bash
git status --short --branch
python3 toolchain/kora index
python3 toolchain/kora check --strict
```

Contrato vigente: todo agente OpenClaw KORA asume `KORA_REPO` local actualizado,
montado read-only en `/home/node/repos/kora`; aliases de knowledge deben apuntar
a `artifacts/knowledge/**` dentro de ese clon.

Siguiente paso razonable: desplegar/verificar con OpenClaw real los builds
locales de `salud/salubrista` y `salud/urgenciologo`, correr `openclaw doctor`
y probar E2E por Telegram segun el handoff.
</prompt>
