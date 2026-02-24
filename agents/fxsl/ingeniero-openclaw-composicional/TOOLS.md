---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:ingeniero-openclaw-composicional-tools:1.1.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string → path: string
- **Cuando usar:** Resolver URNs KODA core via catalogo. No existen URNs locales de OpenClaw.
- **Cuando NO usar:** Para temas OpenClaw — usar web_search_openclaw en su lugar.
- **Notas:** catalog_master_*.yml = SOURCE_OF_TRUTH.

## web_search_openclaw

- **Firma:** query: string, scope: "docs.openclaw.ai" → results: SearchResult[]
- **Cuando usar:** SIEMPRE antes de responder sobre OpenClaw. Documentacion es DINAMICA. Buscar en docs.openclaw.ai con scope restringido.
- **Cuando NO usar:** Nunca omitir para temas OpenClaw. Si no se encuentra info → DECLARE_UNCERTAINTY.
- **Routing Map:**

| Topic | URL |
|-------|-----|
| instalacion, install, onboard, wizard, setup, quickstart | docs.openclaw.ai/start/quickstart |
| arquitectura, gateway, components, WebSocket, daemon | docs.openclaw.ai/concepts/architecture |
| configuracion, openclaw.json, hot reload, config | docs.openclaw.ai/gateway/configuration |
| configuracion ejemplos, templates | docs.openclaw.ai/gateway/configuration-examples |
| seguridad, tokens, allowFrom, dmPolicy, sandbox | docs.openclaw.ai/gateway/security |
| tailscale, remote access, SSH, tunnel | docs.openclaw.ai/gateway/tailscale |
| multi-agent, routing, agents.list, workspace aislado | docs.openclaw.ai/concepts/multi-agent |
| canales, channels, supported channels | docs.openclaw.ai/channels |
| WhatsApp, Baileys, QR, pairing, groups | docs.openclaw.ai/channels/whatsapp |
| Telegram, grammY, bot API | docs.openclaw.ai/channels/telegram |
| Discord, bot, servers, DMs | docs.openclaw.ai/channels/discord |
| Slack, Bolt SDK | docs.openclaw.ai/channels/slack |
| Signal, signal-cli | docs.openclaw.ai/channels/signal |
| IRC | docs.openclaw.ai/channels/irc |
| iMessage, BlueBubbles | docs.openclaw.ai/channels/bluebubbles |
| Teams, Microsoft | docs.openclaw.ai/channels/msteams |
| Matrix | docs.openclaw.ai/channels/matrix |
| Nostr, NIP-04 | docs.openclaw.ai/channels/nostr |
| LINE | docs.openclaw.ai/channels/line |
| pairing, trust, DM approval | docs.openclaw.ai/channels/pairing |
| tools, apply_patch, exec, browser, canvas, cron, sessions | docs.openclaw.ai/tools |
| tool profiles, minimal, coding, messaging, full | docs.openclaw.ai/tools |
| providers, modelos, venice, anthropic, openai, ollama | docs.openclaw.ai/providers |
| nodos, nodes, iOS, Android, headless | docs.openclaw.ai/nodes |
| plataformas, macOS, Linux, Windows, Docker | docs.openclaw.ai/platforms |
| Docker | docs.openclaw.ai/install/docker |
| Nix | docs.openclaw.ai/install/nix |
| CLI, comandos, referencia | docs.openclaw.ai/cli |
| features, capacidades | docs.openclaw.ai/concepts/features |
| troubleshooting, errores, doctor | docs.openclaw.ai/gateway/troubleshooting |
| environment variables | docs.openclaw.ai/help/environment |
| workspace, bootstrap files, AGENTS.md, SOUL.md | docs.openclaw.ai/start/hubs |

## web_search

- **Firma:** query: string → results: SearchResult[]
- **Cuando usar:** Informacion complementaria no disponible en docs.openclaw.ai.
- **Cuando NO usar:** Para temas OpenClaw — usar web_search_openclaw primero.
