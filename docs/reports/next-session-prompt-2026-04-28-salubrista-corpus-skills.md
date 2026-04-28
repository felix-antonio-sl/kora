---
_manifest:
  urn: "urn:kora:kb:next-session-prompt-2026-04-28-salubrista-corpus-skills"
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-28"
    source: "Prompt breve de continuacion posterior al cierre salubrista corpus fisico + skills."
version: "1.0.0"
status: publicado
tags: [next-session-prompt, salubrista, hospitalista, hodom, firs]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-28-salubrista-corpus-skills"
    - "urn:kora:kb:operational-memory-2026-04-28-salubrista-corpus-skills"
---

# Prompt de Continuacion

Copiar este bloque como mensaje inicial de la proxima sesion:

<prompt>
Trabaja sobre `/home/felix/kora` en `master`, continuando desde:

- `docs/reports/handoff-2026-04-28-salubrista-corpus-skills.md`
- `docs/reports/operational-memory-2026-04-28-salubrista-corpus-skills.md`

Primero verifica:

```bash
git status --short --branch
python3 toolchain/kora index
python3 toolchain/kora check --strict
python3 -m unittest tests.test_salubrista_hodom
python3 toolchain/kora kb-graph --json --orphans
```

Contrato esperado: `salubrista` compone las skills
`hospitalista`, `hospitalizacion-domiciliaria` y
`firs-razonamiento-sanitario`; el corpus fisico vive en
`artifacts/knowledge/salud/salubrista`; FIRS y perfiles deprecados no son KB
autorizada.

Siguiente linea razonable: transmutar `salubrista` a OpenClaw usando el clon
local de KORA como KB disponible, o limpiar de forma separada los restos de
staging `_FRAGUA/INBOX/salubrista`.
</prompt>
