---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-builder:1.0.0
  type: lazy_load_endofunctor
---

# CM-OPENCLAW-BUILDER

## Proposito
Materializar el workspace KORA/OpenClaw-oriented respetando segregacion y baseline KORA.

## Input/Output
- **Input:** agent_path: string, blueprint: object
- **Output:** BuildReport

## Procedimiento
1. Crear o actualizar `AGENTS.md`, `SOUL.md`, `USER.md`, `TOOLS.md` y `config.json`.
2. Mantener la semantica OpenClaw-native en `AGENTS.md`, sin colapsar config o runtime state al bootstrap.
3. Crear skills solo cuando aporten fase o procedimiento reutilizable real.

## Signature Output
```yaml
build:
  files_written: 5
  skills_created: 0
```
