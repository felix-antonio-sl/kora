# Telegram Ops Map

Fuentes oficiales prioritarias para arquitectura Telegram en OpenClaw.

## Fuente principal

- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/channels/telegram.md`

Usar para:

- `dmPolicy`, `allowFrom`, `groupPolicy`, `groupAllowFrom`
- groups, topics y `agentId` por topic
- `replyToMode`, `chunkMode`, `textChunkLimit`, `streaming`
- `silentErrorReplies`
- multi-account precedence
- `defaultAccount`
- webhook mode
- exec approvals Telegram

## Fuentes complementarias

- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/gateway/configuration-reference.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/cli/config.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/help/faq.md`

## Regla

1. ACL durable primero.
2. Pairing no sustituye config durable cuando OpenClaw expone `allowFrom`.
3. `chunkMode`, `replyToMode` y errores silenciosos son decisiones de UX y deben quedar en config nativa, no en folklore del deployer.
