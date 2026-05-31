# GEMINI.md

KORA — repositorio, catalogo y sistema de produccion y mantenimiento de
artefactos para sistemas LLM. Gobernado por specs.

KORA gestiona **tres tipos de artefacto, y solo tres**:

- **conocimiento** — archivos `.md` en estandar KORA/MD para *consumo* de
  sistemas LLM (se leen como contexto, no se ejecutan);
- **agentes** (`AGENT.md`) y **skills** (`SKILL.md`) — actores y capacidades que
  se *proyectan a runtimes* (claude-code, codex, openclaw, hermes) via
  transmutacion.

Las **specs** (`governance/`, `ontology/`, `serialization/`, `runtime/`) son la
ley, no artefactos. "Conocimiento" es un tipo especifico, no paraguas de los
otros dos. La ecuacion `PMI × LFS + autoria + transmutacion funtorial` es la
garantia formal, no la definicion. La fuente de verdad es el filesystem con
manifests validos; `docs/generated/` es derivado.

La inteligencia operativa vive en `governance/`, `ontology/`, `serialization/`,
`runtime/`, `artifacts/` y `toolchain/`.

Lee la guia operativa canonica antes de hacer nada: `CLAUDE.md` (top-level) y
luego `governance/gobernanza.md`. Para arrancar una sesion, `docs/start-prompt.md`.
