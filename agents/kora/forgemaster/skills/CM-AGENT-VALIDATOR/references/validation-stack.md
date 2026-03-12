---
title: Validation Stack
status: internal
lang: es
---

# Validation Stack

Recursos del repo que ya sostienen la validacion de workspaces KORA y que este Skill reutiliza:

- `specs/gobernanza.md`
- `specs/agent-spec-md.md`
- `specs/skill-spec-md.md`
- `specs/runtime-spec-md.md`
- `schemas/kora-agent-schema.json`
- `schemas/kora-agent-config-schema.json`
- `scripts/kora_lib/validation.py`
- `scripts/kora_lib/workspaces.py`
- `scripts/kora_lib/agent_audit.py`
- `tests/test_artifacts.py`
- `tests/test_semantic_validation.py`
- `tests/test_agent_audit.py`

Uso recomendado:

1. Fijar primero la spec rectora y las invariantes publicadas.
2. Ejecutar despues la verificacion mecanica reusable del repo.
3. Clasificar divergencias como `ERROR`, `WARNING` o `SKIP` sin relajar el baseline.
