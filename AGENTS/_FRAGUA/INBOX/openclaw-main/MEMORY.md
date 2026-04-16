# Memory

## Topologia vigente

- Gateway nativo systemd en hetzner2897261 (138.201.53.205). Node v24.x.
- 7 agentes: main (Clawforge), mente-omega, salubrista, steipete, gtd-integral, allan-kelly, fugaz.
- Config: `~/.openclaw/openclaw.json`. Usar `zsh -ic` para PATH correcto.
- Modelo primario: `openai-codex/gpt-5.4`. Fallback: `minimax/MiniMax-M2.7`.
- Regla dura: operar siempre sobre systemd nativo. No hay Docker para OpenClaw.

## VPS secundario

- clawdbot-hetzner (157.180.121.173): `ssh clawdbot@157.180.121.173` (clave ed25519).
- Para OpenClaw remoto: `ssh clawdbot@157.180.121.173 'export PATH="$HOME/.npm-global/bin:$PATH" && openclaw <cmd>'`

## Produccion documental

- Artefactos producidos en `output/`. Cross-agent via path absoluto.
- Doctrina: MANUAL.md seccion 14 (conocimiento, memoria e indexacion).

## Politica de memoria

- **MEMORY.md** se inyecta en cada turno. Solo anclas y reglas duras. Max ~1.5KB.
- **memory/*.md** no se inyecta. Acceso on-demand via `memory_search` / `memory_get`.

## Decisiones vigentes

- **2026-03-26**: SSOT config OpenClaw: `/home/felix/kora/KNOWLEDGE/OMEGA/openclaw-manual-integral.md` y `manual-integral-skills-openclaw.md`.
- **2026-04-10**: Federacion Docker (2a gen) eliminada completamente. Solo queda gateway nativo (3a gen).
- **2026-04-10**: Fallbacks simplificados: solo `minimax/MiniMax-M2.7`. Sin anthropic ni zai en cadena.

## Embedding de memoria

- Provider: `openai`, modelo: `text-embedding-3-small` (1536d)
- Hybrid search (0.7 vector + 0.3 text), MMR enabled.

## Campos removidos del schema

- `channels.telegram.humanDelay` — solo valido en `agents.defaults.humanDelay`
- `messages.tts.edge` — no existe; usar `provider: "microsoft"`

El validador es la autoridad. Si una fuente los menciona, ignorar.
