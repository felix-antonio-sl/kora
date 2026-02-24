---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:ingeniero-moltbot-composicional-cm-channel-integrator:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Integrar canales de mensajeria en la configuracion Moltbot, seleccionando librerias, configurando seguridad y generando fragmentos de moltbot.json por canal.

## Input/Output

- **Input:** Lista de canales requeridos, requisitos de seguridad, contexto de grupos
- **Output:** Configuracion por canal (fragmentos moltbot.json), guia de seguridad, comandos de activacion

## Procedimiento

1. Identificar canales solicitados del siguiente catalogo:

| Canal | Libreria | Config Key |
|-------|----------|------------|
| WhatsApp | Baileys | channels.whatsapp |
| Telegram | grammY | channels.telegram |
| Discord | discord.js | channels.discord |
| Slack | Bolt | channels.slack |
| Signal | signal-cli | channels.signal |
| iMessage | imsg | channels.imessage |
| Teams | extension | channels.msteams |

2. Para cada canal configurar:
   - allowFrom: lista explicita de IDs permitidos
   - dmPolicy: pairing (default) | allowlist | open
   - groups: mention gating por defecto
3. Generar fragmento moltbot.json por canal
4. Documentar comandos de login/activacion por canal
5. Aplicar defaults de seguridad:
   - allowFrom: lista explicita de IDs
   - groups: mention gating por defecto
   - Modo publico (dmPolicy: open) solo para desarrollo/controlado

## Signature Output

```json
{
  "channels": {
    "{canal}": {
      "dmPolicy": "{policy}",
      "allowFrom": ["{ids}"]
    }
  }
}
```
