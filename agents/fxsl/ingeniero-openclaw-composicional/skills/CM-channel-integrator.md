---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:ingeniero-openclaw-composicional-cm-channel-integrator:1.1.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Integrar canales de mensajeria en OpenClaw. Lista dinamica — siempre verificar docs.openclaw.ai/channels.

## Input/Output

- **Input:** Canales requeridos desde S-REQUIREMENTS o S-CHANNEL-DESIGN
- **Output:** Seccion channels de openclaw.json con config por canal, seguridad, allowFrom

## Procedimiento

1. Identificar canales solicitados por usuario
2. Verificar soporte actual en docs.openclaw.ai/channels
3. Configurar cada canal con allowFrom, dmPolicy y seguridad
4. Configurar mention gating para grupos (requireMention: true default)
5. Generar seccion channels de openclaw.json

### Core Channels (verificar docs para estado actualizado)

| Canal | Library | Config Key | Doc |
|-------|---------|------------|-----|
| WhatsApp | Baileys | channels.whatsapp | docs.openclaw.ai/channels/whatsapp |
| Telegram | grammY | channels.telegram | docs.openclaw.ai/channels/telegram |
| Discord | discord.js | channels.discord | docs.openclaw.ai/channels/discord |
| Slack | Bolt SDK | channels.slack | docs.openclaw.ai/channels/slack |
| Signal | signal-cli | channels.signal | docs.openclaw.ai/channels/signal |
| IRC | IRC client nativo | channels.irc | docs.openclaw.ai/channels/irc |
| BlueBubbles | REST API macOS | channels.bluebubbles | docs.openclaw.ai/channels/bluebubbles |
| MS Teams | Bot Framework | channels.msteams | docs.openclaw.ai/channels/msteams |
| WebChat | Gateway WebSocket | webchat | docs.openclaw.ai/web/webchat |

### Plugin Channels

Matrix, LINE, Nostr NIP-04, Mattermost, Feishu/Lark, Google Chat, Nextcloud Talk, Tlon/Urbit, Twitch, Zalo.

### Security Defaults

- allowFrom: lista explicita de IDs permitidos
- dmPolicy: pairing (solicita pairing) o allowlist (lista explicita)
- groups: requireMention: true por defecto
- WhatsApp: numeros en formato E.164 (+15555550123)

## Signature Output

```json
{
  "channels": {
    "{canal}": {
      "allowFrom": ["..."],
      "groups": { "*": { "requireMention": true } }
    }
  }
}
```
