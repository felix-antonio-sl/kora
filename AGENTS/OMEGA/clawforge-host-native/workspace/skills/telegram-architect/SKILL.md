---
name: telegram-architect
description: >-
  Design, configure, and audit the Telegram channel layer for OpenClaw agents.
  Use when the user wants to set up Telegram, configure DM or group policies,
  streaming, reactions, commands, or troubleshoot Telegram connectivity issues.
---

## Alcance

Configuracion completa del canal Telegram para agentes OpenClaw.
Cubre: setup inicial, politicas DM/grupo, streaming, reacciones, comandos y diagnostico.

## Procedimiento: Diseno

### 1. Obtener bot token

Crear bot via @BotFather en Telegram. Guardar el token.

### 2. Definir politicas

Decidir cada parametro segun el caso de uso:

| Parametro | Opciones | Default recomendado |
|-----------|----------|---------------------|
| `dmPolicy` | `all`, `allowlist`, `off` | `allowlist` |
| `groupPolicy` | `none`, `mention`, `reply`, `all` | `mention` |
| `streaming` | `true`, `false` | `true` |
| `reactions` | `true`, `false` | `true` |
| `allowFrom` | lista de user IDs o usernames | segun caso |

### 3. Emitir fragmento de config

```json
{
  "channels": {
    "telegram": {
      "botToken": "env:TELEGRAM_BOT_TOKEN",
      "dmPolicy": "allowlist",
      "allowFrom": ["username1", "username2"],
      "groupPolicy": "mention",
      "streaming": true,
      "reactions": true,
      "commands": ["/start", "/help", "/reset"]
    }
  }
}
```

### 4. Aplicar config

```bash
openclaw config set channels.telegram --from-json fragment.json
openclaw agent reload <name>
```

## Procedimiento: Auditoria

```bash
openclaw channel status --agent <name>
openclaw agent inspect <name>   # seccion channels
```

Verificar: canal conectado, politicas aplicadas, bot respondiendo.

## Procedimiento: Diagnostico

### Checklist Telegram

- [ ] Token valido: `curl https://api.telegram.org/bot<TOKEN>/getMe`
- [ ] Bot no bloqueado por usuario
- [ ] `allowFrom` incluye al usuario que reporta el problema
- [ ] `dmPolicy` no es `off` si se espera DM
- [ ] `groupPolicy` no es `none` si se espera respuesta en grupo
- [ ] Bot agregado al grupo con permisos de lectura de mensajes
- [ ] Gateway corriendo: `openclaw status`
- [ ] Canal conectado: `openclaw channel status --agent <name>`

## Notas

- Guardar el token en variable de entorno, nunca en config plano.
- `streaming: true` mejora la experiencia pero requiere conexion estable.
- Cambiar `dmPolicy` a `all` solo para agentes publicos; usar `allowlist` por defecto.
