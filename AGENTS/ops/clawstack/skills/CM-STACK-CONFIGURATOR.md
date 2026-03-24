---
_manifest:
  urn: urn:ops:skill:clawstack-stack-configurator:1.1.0
  type: lazy_load_endofunctor
---

# CM-STACK-CONFIGURATOR

## Proposito
Configura cualquier capa del stack o cross-layer, aplicando cambios declarativos con verificacion post-aplicacion.

## Input/Output
- **Input:** scope: string (host|docker|openclaw|cross-layer), cambios: ConfigChange[]
- **Output:** ConfigReport (ver Signature Output)

## Procedimiento
1. Identificar scope y capa(s) afectada(s).
2. Segun scope:
   - **host**: networking (netplan), firewall (ufw), servicios (systemd units), packages (apt), SSH config.
   - **docker**: compose files, daemon.json, images, volumes, networks, cgroups limits.
   - **openclaw**: gateway (port, auth, mode, bind), channels (whatsapp, telegram, discord, slack, signal), agents (list, workspace, model, identity), sandbox (mode, scope, docker config), automation (heartbeats, cron, hooks), memory (flush, search, compaction), skills (entries, gating), models (providers, fallbacks, aliases), federation (hooks token, shared mounts, directorio-agentes). Incluye dos patrones compuestos:
     - *Patron UX Telegram* (consultar `urn:ops:kb:ux-telegram-openclaw`): chunkMode="length", markdown.tables="bullets", replyToMode="first", silentErrorReplies=true, thinkingDefault="adaptive", session.reset, session.maintenance. Aplicar via merge declarativo de config + restart; si existe `/srv/kora/scripts/sync-config.sh`, usarlo como helper, no como dependencia implicita. Trampas: streaming "full" no existe; tools.profile "minimal" solo da session_status; group:memory no existe en v2026.3.22; config no interpola ${ENV_VAR}.
     - *Patron Federation* (consultar `urn:ops:kb:federacion-kora-v2`): hooks.enabled=true con token literal en config runtime, gateway.bind="lan" (no "loopback" para Docker bridge), shared mounts en compose, seccion derivacion en TOOLS.md del agente sin secretos, entrada en directorio-agentes.md.
   - **cross-layer**: cambios que afectan multiples capas (ej: abrir puerto en UFW + configurar canal en OpenClaw).
3. Para cada cambio: leer config actual, proponer diff, confirmar con usuario.
4. Aplicar cambio con herramienta apropiada (host_exec | docker_exec | oc_cli).
5. Verificar post-aplicacion: restart si necesario, test funcional, doctor/status.
6. Si error: rollback al estado anterior, reportar causa.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| scope | string | Capa(s) configurada(s) |
| cambios_aplicados | ConfigChange[] | Lista de cambios con diff before/after |
| verificacion | PASS|FAIL | Estado post-aplicacion |
| restart_required | bool | Si algun servicio requiere restart |
