## Envelope de permisos

Clawforge opera con acceso completo al host y al gateway: filesystem sin restriccion, exec sin allowlist, superficies nativas de OpenClaw.

---

## exec

Ejecucion sin restriccion de comandos (`security: full`).

Comandos frecuentes:
- `systemctl --user status/start/stop/restart openclaw-gateway`
- `journalctl --user -u openclaw-gateway --since '30m ago'`
- `free -h`, `df -h /`, `uptime`, `ss -tlnp`
- `node --version`, `npm list -g openclaw`
- `openclaw --version`, `openclaw update`
- `nginx -t`, `certbot renew`

## openclaw CLI

Superficie nativa para toda operacion del gateway. Preferir siempre sobre manipulacion manual.

Comandos frecuentes:
- `openclaw status` / `openclaw status --deep`
- `openclaw health --json`
- `openclaw doctor` / `openclaw doctor --fix`
- `openclaw config get <key>` / `openclaw config set <key> <value>`
- `openclaw config validate`
- `openclaw gateway status` / `openclaw gateway restart`
- `openclaw agents list`
- `openclaw channels status` / `openclaw channels logs <canal>`
- `openclaw skills list --eligible` / `openclaw skills check`
- `openclaw cron list` / `openclaw cron status`
- `openclaw security audit --deep`
- `openclaw logs --follow`
- `openclaw models status` / `openclaw models auth login`

## read / write / edit / apply_patch

Acceso completo al filesystem del host. Puede leer y escribir en cualquier ruta:
- `~/.openclaw/workspace*/` — workspaces de todos los agentes
- `~/.openclaw/secrets/` — token files (leer para auditar, escribir con chmod 600)
- `/etc/nginx/`, `/etc/systemd/system/` — config de servicios del host
- Cualquier otra ruta necesaria para operar, configurar o reparar el stack

Para modificar `~/.openclaw/openclaw.json`: usar `gateway -> config.patch` o `openclaw config set`. No usar `write`/`edit` directamente sobre ese archivo.

## memory_search / memory_get

Para recuperar decisiones previas, contratos activos, hallazgos.
Siempre verificar vigencia antes de operar sobre un recuerdo.

## web_fetch / web_search

Para buscar documentacion, changelogs, referencia de providers.
No como sustituto de contexto local bien mantenido.

## message

Para comunicar alertas y hallazgos al operador via canal.
Solo mensajes con contenido de valor. No spam operativo.

## sessions_list / sessions_history / sessions_send / session_status / sessions_spawn

Comunicacion y coordinacion cross-agent. Ver seccion de coordinacion en AGENTS.md.

## gateway

Acceso a la API interna del gateway. Expone operaciones RPC de control-plane, incluyendo:

- **`config.patch`** — merge parcial sobre `openclaw.json`. Valida en memoria **antes** de escribir al disco.
  Es el mecanismo canonico para cambios de config complejos (multiples campos, estructuras anidadas).
  Si el campo no existe en el schema, el gateway rechaza el patch sin tocar el archivo.
- **`config.apply`** — reemplazo completo del config. Misma garantia de validacion previa.
- **`update.run`** — lanza el flujo de actualizacion de version de OpenClaw.

**Regla de uso:** Para cualquier modificacion de `openclaw.json` con multiples campos o estructuras complejas, usar siempre `gateway -> config.patch`. Para campos individuales, `openclaw config set <key> <value>` via CLI.
Nunca usar `write`/`edit` directamente sobre `openclaw.json`: no tienen checkpoint de validacion previo al escritura.

## cron

Para programar tareas de mantenimiento, health checks y auditorias periodicas.

## Coding agents (ACP — forma nativa y canonica)

OpenClaw tiene ACP (Agent Client Protocol) habilitado con backend `acpx`. Esto es la superficie nativa para spawnear coding agents.

### Forma canonica: `sessions_spawn` con `runtime: "acp"`

```
sessions_spawn(runtime: "acp", agentId: "codex", task: "tu tarea")
```

Harness disponibles (agentId): claude, codex, opencode, gemini, copilot, cursor, droid, iflow, kilocode, kimi, kiro, openclaw, pi, qwen.

### Patrones

| Caso | Llamada |
|------|--------|
| One-shot (ejecuta y vuelve) | `sessions_spawn(runtime: "acp", agentId: "codex", task: "...")` |
| Thread-bound persistente (Discord/Telegram) | `sessions_spawn(runtime: "acp", agentId: "codex", thread: true, mode: "session", task: "...")` |
| Desde chat (operador) | `/acp spawn codex --bind here` o `/acp spawn codex --thread auto` |
| Steer en sesion activa | `/acp steer --session <key> "instruccion"` |

### Reglas duras

- **Siempre `runtime: "acp"`** para coding agents. No usar `exec` con CLIs directo.
- **Nunca en `~/.openclaw` ni `~/clawd`.** Usar `cwd` para setear working directory.
- `cwd` debe ser un **git repo** (requirement de varios harness). Sin git repo, Codex falla con `acpx exited with code 1`.
- Permisos ya configurados: `permissionMode: approve-all`, `nonInteractivePermissions: deny`.
- Resultados se anuncian automaticamente de vuelta al requester.
- `/acp doctor` para diagnosticar problemas.
- `/acp status` para ver sesiones activas.

### Doc oficial

- `docs/tools/acp-agents.md` — referencia completa
- `docs/tools/subagents.md` — sub-agentes nativos (no ACP)
