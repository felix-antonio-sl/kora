# Memory — fugaz

## Produccion documental

- Artefactos producidos en `output/` si aplica. Cross-agent via path absoluto.


## Identidad operativa

- fugaz es un agente independiente. Opera sesion propia con contexto propio.
- Si hay herencia del workspace original de steipete, tratarla como contexto adoptado, no como historia propia.

## Fuentes de referencia

- `reference/legacy-steipete/general/` — legado estrategico general (heredado del workspace steipete)
- `reference/legacy-steipete/opmodel/` — artefactos preservados de opmodel
- `/home/felix/projects/opmodel` — fuente viva actual del proyecto opmodel
- `/home/felix/kora/KNOWLEDGE/fxsl/opm/` — fuente de verdad teorica/metodologica OPM/ISO

## Politica de CLIs de coding

- **Claude Code CLI prohibido** — no despachar `claude` como agente de coding desde fugaz
- **Autorizados a destajo:** Codex (`codex`), OpenCode (`opencode`), Gemini CLI (`gemini`)

### Forma canonica: ACP via `sessions_spawn`

```
sessions_spawn(runtime: "acp", agentId: "codex", task: "tu tarea")
sessions_spawn(runtime: "acp", agentId: "opencode", task: "tu tarea")
sessions_spawn(runtime: "acp", agentId: "gemini", task: "tu tarea")
```

Harness disponibles: claude, codex, opencode, gemini, copilot, cursor, droid, iflow, kilocode, kimi, kiro, openclaw, pi, qwen.

Reglas:
- **Siempre `runtime: "acp"`** para coding agents. No usar `exec` con CLIs directo.
- Nunca en `~/.openclaw` ni `~/clawd`
- Usar `cwd` para setear working directory del proyecto
- Permisos ya configurados globalmente: `approve-all`
- Resultados se anuncian automaticamente de vuelta al requester
- `/acp doctor` para diagnosticar problemas
- Doc oficial: `docs/tools/acp-agents.md`

## Skills canonicos locales

- `/home/felix/openclaw-fleet/workspaces/fugaz/skills/opm-modeler/` — skill canonica para tareas de modelado OPM/ISO 19450: OPM, OPD, OPL, SD, SD1, refinamiento, validacion metodologica y modelamiento conceptual.
- `/home/felix/openclaw-fleet/workspaces/fugaz/skills/opmodel-knowledge/` — skill canonica para conocimiento operativo y continuidad sobre OPModel.
- `/home/felix/openclaw-fleet/workspaces/fugaz/skills/arquitecto-categorico/` — disponible para formalizacion fuerte de arquitecturas de datos, APIs y estructuras categoricas cuando aplique.
- Para trabajo OPM/OPModel, no tratar estas tareas como genericas si una de esas skills aplica.
