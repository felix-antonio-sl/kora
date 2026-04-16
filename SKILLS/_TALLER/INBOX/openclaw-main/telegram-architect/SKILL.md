---
name: telegram-architect
description: Disenar, configurar y auditar el canal Telegram para agentes OpenClaw. Usar cuando el usuario quiere configurar Telegram, definir politicas DM/grupo, streaming, reacciones, comandos, o diagnosticar problemas de conectividad.
---

## Alcance

Configuracion completa del canal Telegram para agentes OpenClaw.
Cubre: setup inicial, politicas DM/grupo, streaming, reacciones, comandos y diagnostico.

## Procedimiento: Diseno

### 1. Obtener bot token

Crear bot via @BotFather en Telegram. Guardar el token en archivo con permisos 600.

### 2. Definir politicas

| Parametro | Valores validos | Default recomendado |
|-----------|----------------|---------------------|
| `dmPolicy` | `pairing`, `allowlist`, `open`, `disabled` | `allowlist` |
| `groupPolicy` | `allowlist`, `open`, `disabled` | `disabled` |
| `requireMention` | `true`, `false` | `true` (en grupos) |
| `streaming` | `"partial"`, `"block"`, `"off"` | `"partial"` |
| `reactionLevel` | `"minimal"`, `"normal"`, `"off"` | `"normal"` |
| `ackReaction` | emoji string | `"👀"` |
| `silentErrorReplies` | `true`, `false` | `false` |
| `textChunkLimit` | numero de caracteres | 4096 |
| `chunkMode` | `"sentence"`, `"paragraph"`, `"none"` | `"sentence"` |

### 3. Emitir fragmento de config

```json
{
  "channels": {
    "telegram": {
      "accounts": {
        "main": {
          "tokenFile": "/home/felix/.openclaw/secrets/telegram-bot.token"
        }
      },
      "dmPolicy": "allowlist",
      "allowFrom": [7192195698],
      "groupPolicy": "disabled",
      "streaming": "partial",
      "reactionLevel": "normal",
      "ackReaction": "👀",
      "commands": ["/start", "/help", "/reset"]
    }
  }
}
```

### 4. Aplicar config

Usar `gateway → config.patch` con el fragmento anterior. No aplicar via `write`/`edit` sobre `openclaw.json`.

```bash
openclaw channels status     # verificar canal activo post-apply
```

## Procedimiento: Auditoria

```bash
openclaw channels status     # estado del canal Telegram
openclaw status --deep       # seccion channels del gateway
```

Verificar: canal conectado, politicas aplicadas, bot respondiendo.

## Procedimiento: Diagnostico

### Checklist Telegram

- [ ] Token valido: `curl https://api.telegram.org/bot<TOKEN>/getMe`
- [ ] Bot no bloqueado por usuario
- [ ] `allowFrom` incluye al usuario que reporta el problema
- [ ] `dmPolicy` no es `disabled` si se espera DM
- [ ] `groupPolicy` no es `disabled` si se espera respuesta en grupo
- [ ] Bot agregado al grupo con permisos de lectura de mensajes
- [ ] Gateway corriendo: `openclaw status`
- [ ] Canal conectado: `openclaw channels status`

## Notas

- El token va en archivo separado (`tokenFile`), nunca como string en `openclaw.json`.
- `streaming: "partial"` mejora la experiencia pero requiere conexion estable.
- `dmPolicy: "allowlist"` + `allowFrom` es la configuracion mas segura para agentes privados.
- `requireMention: true` evita que el agente responda a todos los mensajes de grupo.
