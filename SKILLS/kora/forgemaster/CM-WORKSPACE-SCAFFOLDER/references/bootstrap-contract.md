---
title: Bootstrap Contract
status: internal
lang: es
---

# Bootstrap Contract

Fuentes del repo que fijan la forma canonica del scaffolding de agentes:

- `specs/gobernanza.md`
- `specs/agent-spec-md.md`
- `specs/skill-spec-md.md`
- `schemas/kora-agent-schema.json`
- `schemas/kora-agent-config-schema.json`
- `tests/fixtures/valid-agent-bootstrap.md`
- `tests/fixtures/valid-config.json`
- `tests/fixtures/extended-skill/SKILL.md`

Uso recomendado:

1. Tomar `agent-spec-md` y `gobernanza.md` como contrato rector.
2. Usar los schemas para validar la forma de `config.json` y bootstrap frontmatter.
3. Usar las fixtures como ejemplos minimos de parseo y carga valida, no como plantillas literales de produccion.
