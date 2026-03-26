## exec

Ejecutar comandos en el host para diagnostico, configuracion y mantenimiento.

Comandos frecuentes:
- `systemctl status/start/stop/restart openclaw-gateway`
- `journalctl -u openclaw-gateway --since '30m ago'`
- `free -h`, `df -h /`, `uptime`, `ss -tlnp`
- `node --version`, `npm list -g openclaw`

## openclaw CLI

Superficie nativa para toda operacion del gateway. Preferir siempre sobre manipulacion manual.

Comandos frecuentes:
- `openclaw status` / `openclaw status --deep`
- `openclaw health --json`
- `openclaw doctor` / `openclaw doctor --fix`
- `openclaw config get <key>` / `openclaw config set <key> <value>`
- `openclaw config validate`
- `openclaw gateway status` / `openclaw gateway restart`
- `openclaw daemon status/start/stop/restart`
- `openclaw agents list`
- `openclaw channels status` / `openclaw channels logs <canal>`
- `openclaw skills list --eligible` / `openclaw skills check`
- `openclaw cron list` / `openclaw cron status`
- `openclaw security audit --deep`
- `openclaw logs --follow`

## read / write / edit

Para crear y mantener archivos del workspace: bootstrap, config, skills, memoria.

## memory_search / memory_get

Para recuperar decisiones previas, contratos activos, hallazgos.
Siempre verificar vigencia antes de operar sobre un recuerdo.

## web_fetch

Para buscar documentacion, changelogs, referencia de providers.
No como sustituto de contexto local bien mantenido.

## message

Para comunicar alertas y hallazgos al operador via canal.
Solo mensajes con contenido de valor. No spam operativo.
