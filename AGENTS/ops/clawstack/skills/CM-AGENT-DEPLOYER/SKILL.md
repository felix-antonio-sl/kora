---
_manifest:
  urn: urn:ops:skill:clawstack-agent-deployer:1.2.0
  type: lazy_load_endofunctor
extensions:
  ops:
    skill:
      form: extended
      allowed_tools:
        - catalog_resolve
        - host_exec
        - docker_exec
        - oc_cli
        - kb_route
      requires: []
      references:
        - references/deploy-phases-checklist.md
        - references/hetzner-audit-findings.md
---

# CM-AGENT-DEPLOYER

## Proposito

Ejecutar el pipeline completo para desplegar un agente KORA transmutado a OpenClaw sobre un servidor remoto, consumiendo el contrato native-first emitido por forgemaster. Automatiza las fases ejecutables y guia al operador a traves de las interactivas (bot creation, auth setup, pairing, e2e verification) con checkpoints de espera y reanudacion. Incluye integracion con la federacion kora (shared storage, hooks cross-gateway, panel web, UX de canal).

## Input/Output

- **Input:** transmutation_path: string (path preferido a `_transmutation.yml`; tambien acepta directorio de staging que lo contenga), gateway_name: string, agent_id: string, kora_repo: string (default: /home/felix/kora)
- **Output:** DeployReport (ver Signature Output)

## Procedimiento

**Prerequisito**: normalizar `transmutation_path` asi:
1. Si apunta a `_transmutation.yml`, usar ese manifest y tomar su directorio padre como staging dir.
2. Si apunta a un directorio, exigir `{dir}/_transmutation.yml`.
3. Cargar el manifest y verificar ANTES de copiar nada:
   - que `target.artifacts` existe y lista artefactos emitidos por forgemaster;
   - que cada artefacto listado existe en staging;
   - que el hash real de cada artefacto coincide con el manifest;
   - que `platform_contract` existe;
   - que `platform_contract.config_projection`, `platform_contract.managed_installs` y `platform_contract.deployment_hints` existen.
Si falla cualquier check, ABORTAR: "Artefactos transmutados invalidos o adulterados. Re-transmutar con kora/forgemaster." Este skill NO transmuta ni recompone bootstrap desde el workspace KORA fuente — consume artefactos ya transmutados (R9: DEPLOY-FROM-TRANSMUTATION).

Consultar `references/deploy-phases-checklist.md` para verificacion y `references/hetzner-audit-findings.md` para gotchas conocidos. Consultar KB via `kb_route("deploy agentes")` → `urn:ops:kb:deploy-agente-kora-en-openclaw` para procedimiento detallado. Consultar KB via `kb_route("principios transmutacion")` → `urn:ops:kb:principios-transmutacion-kora-openclaw` para marco conceptual.

### Grupo A: Preparacion de infraestructura (automatizado)

**P01 — PROVISIONING.** Si `platform_contract.deployment_hints.topology.recommended == "single-gateway-multi-agent"` y ya existe un gateway compatible, reutilizarlo antes de crear uno aislado. Solo provisionar gateway/compose dedicados si el contrato exige `isolated-gateway` o el operador documenta la razon. Via `host_exec`: crear estructura `/srv/kora/{compose-{gateway},config/{gateway},workspaces/{gateway}/agents/{agent}/{skills,memory},knowledge,scripts,backups,shared/federation,shared/{agent}}` solo cuando aplique. Ajustar ownership solo sobre los paths creados para este deploy, no sobre todo `/srv/kora`. Verificar estructura con `ls -la`.

**P02 — COPY TRANSMUTED WORKSPACE.** Consumir el workspace ya emitido por forgemaster. Via `host_exec`:
- localizar `workspace/` y los artefactos declarados por `platform_contract` en el staging dir del manifest;
- copiar `workspace/` tal cual a `/srv/kora/workspaces/{gateway}/agents/{agent}/`;
- preservar nombres, skills adaptados, `IDENTITY.md` y cualquier frontmatter runtime ya generado para OpenClaw;
- NO re-strippear ni reconstruir bootstrap desde componentes KORA fuente.
Verificar: conteo de archivos y hashes de los artefactos copiados coinciden con `target.artifacts` del manifest.

**P03 — KB SYNC.** Leer `platform_contract.deployment_hints.kb_mounts` de _transmutation.yml. Para cada KB: resolver URN via `catalog_resolve`, strip frontmatter si la fuente lo requiere y copiar a `/srv/kora/knowledge/{ns}/{file}`. Fijar permisos read-only. KBs NO van en bootstrap — son archivos montados que el agente lee on-demand (principios P8). Verificar: conteo, rutas y tamanos aproximados coinciden.

**P04 — DOCKER BUILD.** Via `docker_exec`: desde el repo operativo de OpenClaw (`{openclaw_repo_path}` resuelto desde el contexto del host), build imagen base OpenClaw: `cd {openclaw_repo_path} && docker build -t openclaw-local:latest .`. Si `platform_contract.deployment_hints.requires_sidecar == true`: build imagen sidecar. Si `platform_contract.deployment_hints.architecture == "caso-b"`: build overlay gateway con ENV del sidecar API. Verificar: `docker images` muestra tags esperados.

### Grupo B: Checkpoint interactivo — Bot creation (guiado)

**P06 — BOT CREATION.** Emitir instrucciones al operador:
1. "Abrir Telegram, buscar @BotFather, enviar /newbot"
2. "Elegir nombre y username para el bot del agente"
3. "Copiar el token (formato: 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11)"
4. "Buscar @userinfobot en Telegram, enviar cualquier mensaje, copiar user ID (INTEGER sin comillas)"
Requiere del operador: TELEGRAM_BOT_TOKEN, TELEGRAM_USER_ID. Almacenar para P07.

### Grupo C: Configuracion de entorno y volume (automatizado)

**P05 — CONFIG PARAMETRIZATION.** Leer `platform_contract.config_projection` del staging dir o del manifest. Parametrizar openclaw.json5: agent_id, gateway_name, puerto (spacing minimo 20 entre gateways — principios P7; detectar puertos existentes via `docker ps`), modelo, identity, sandbox, channels con datos de P06 y cualquier override explicito del contrato. Escribir a `/srv/kora/config/{gateway}/openclaw.json5`. Para kora-federation: detectar si ya existe (`docker network ls | grep kora-federation`); si existe usar `external: true`, si no crearla con `driver: bridge` (hallazgo H3). Si existen mounts RW o requerimientos especiales, leerlos desde `platform_contract.deployment_hints.bind_mounts` o `manual_inputs_required`; **NO** inferirlos desde `TOOLS.md`. Parametrizar docker-compose.yml: imagen, container name, puerto, volumes, red. Escribir a `/srv/kora/compose-{gateway}/docker-compose.yml`. Verificar: `cd /srv/kora/compose-{gateway} && docker compose config --quiet`.

**P07 — ENV GENERATION.** Via `host_exec`: generar OPENCLAW_AUTH_TOKEN (`openssl rand -hex 32`). Escribir `.env` con TELEGRAM_BOT_TOKEN (de P06), OPENCLAW_AUTH_TOKEN, NODE_ENV=production. Si sidecar: agregar SERVICE_API. `chmod 600 /srv/kora/compose-{gateway}/.env`. Actualizar openclaw.json5 con TELEGRAM_USER_ID (como integer) en `channels.telegram.allowFrom`. Verificar: `.env` existe con permisos correctos.

**P08 — VOLUME INIT.** Via `docker_exec`: pre-seed named volume con `docker compose run --rm --user root --no-deps --entrypoint sh gateway` para crear dirs y fijar ownership uid 1000 (node). Copiar config al volume. Verificar: dirs creados, config copiado, ownership correcta.

**P08.5 — MANAGED INSTALLS.** Leer `platform_contract.managed_installs`. Para cada install nativo:
1. `skills`: ejecutar `openclaw skills install <slug> [--version <version>]` cuando `source != "workspace"`.
2. `plugins`: ejecutar `openclaw plugins install <locator>` respetando source/version/marketplace declarados.
3. `bundles`: instalar via `openclaw plugins install <locator>` o surface equivalente declarada por el contrato.
Verificar con `openclaw skills list`, `openclaw plugins list` o diagnostico equivalente. Ningun install gestionado **DEBE** quedar implícito.

### Grupo D: Checkpoint interactivo — Auth setup (guiado)

**P09 — AUTH SETUP.** Auth en OpenClaw es **per-agent** — cada agente almacena credenciales en `~/.openclaw/agents/{agent_id}/agent/auth-profiles.json` (no compartido entre agentes). Tres alternativas, en orden de preferencia:
1. **OAuth setup-token** (recomendado): "Ejecutar: `cd /srv/kora/compose-{gateway} && docker compose run --rm --no-deps gateway openclaw models auth setup-token --provider anthropic --agent {agent_id}`". Esto abre un flujo OAuth en el browser. Completarlo y regresar.
2. **Copiar auth de otro agente** (rapido, si ya hay un gateway con auth funcional): `docker exec {existing_container} cat /home/node/.openclaw/agents/{existing_agent}/agent/auth-profiles.json | docker exec -i {new_container} sh -c 'mkdir -p /home/node/.openclaw/agents/{new_agent}/agent && cat > /home/node/.openclaw/agents/{new_agent}/agent/auth-profiles.json && chmod 600 /home/node/.openclaw/agents/{new_agent}/agent/auth-profiles.json'`. Restart del gateway despues de copiar.
3. **API key directa**: agregar ANTHROPIC_API_KEY al .env. Requiere restart.
Verificar: enviar mensaje test al bot — si responde `No API key found for provider "anthropic"`, auth no esta configurada. Revisar logs con `docker logs {container} | grep "auth\|api.key\|anthropic"`.

### Grupo E: Validacion y deploy (automatizado)

**P10 — DOCTOR.** Via `docker_exec`: `cd /srv/kora/compose-{gateway} && docker compose run --rm --no-deps gateway openclaw doctor`. Parsear output. Esperado: cero errores de config. Warnings aceptables: gateway auth token missing, systemd unavailable, memory search disabled. Si errores: DETENER — no proceder a deploy. Reportar errores y sugerir fix.

**P11 — DEPLOY.** Via `docker_exec`: `cd /srv/kora/compose-{gateway} && docker compose up -d`. Verificar: `cd /srv/kora/compose-{gateway} && docker compose ps` muestra containers Up/healthy. Verificar: `cd /srv/kora/compose-{gateway} && docker compose logs --tail 20 gateway` contiene indicadores de arranque exitoso (agent model, listening on ws://, channel starting). Si containers en restart loop: detener y transicionar a S-TROUBLESHOOT.

### Grupo F: Checkpoints interactivos — Pairing y verificacion (guiado)

**P12 — PAIRING.** Emitir: "Enviar cualquier DM al bot en Telegram". Via `docker_exec`: `cd /srv/kora/compose-{gateway} && docker compose exec gateway openclaw pairing list telegram`. Mostrar codigos al operador. Preguntar cual aprobar. Via `docker_exec`: `cd /srv/kora/compose-{gateway} && docker compose exec gateway openclaw pairing approve telegram {CODE}`.

**P13 — E2E VERIFICATION.** Emitir: "Enviar un mensaje de test al bot por Telegram. El agente debe responder coherentemente con su personalidad (SOUL.md) y comportamiento (AGENTS.md)." Si sidecar: "Verificar que la respuesta incluye datos del servicio externo, no solo texto conversacional." Requiere confirmacion del operador.

### Grupo G: Lifecycle operacional (automatizado, on-demand)

**P14 — DRIFT MANAGEMENT.** Via `host_exec`: para cada archivo bootstrap, diff version stripped del repo vs version desplegada. Clasificar drift: regla emergente (backport candidate), residuo (limpiar), memory (normal, skip), HEARTBEAT.md (normal, skip). Reportar resumen con recomendaciones.

**P15 — BACKUP.** Via `docker_exec`: `cd /srv/kora/compose-{gateway} && docker compose cp gateway:/home/node/.openclaw/agents /srv/kora/backups/agents-{agent_id}-$(date +%Y%m%d)`. Si sidecar: `cd /srv/kora/compose-{gateway} && docker compose cp sidecar:/app/data /srv/kora/backups/sidecar-{agent_id}-$(date +%Y%m%d)`. Reportar paths y tamanos.

**P16 — RESYNC.** Cuando cambie el agente en el repo: re-ejecutar P02 para artefactos transmutados cambiados. Si config cambio: hacer merge declarativo del config; si existe `/srv/kora/scripts/sync-config.sh`, usarlo como helper, si no re-ejecutar P05 + copy al volume. Via `docker_exec`: `cd /srv/kora/compose-{gateway} && docker compose restart gateway`. Verificar: containers healthy, logs limpios.

### Grupo H: Integracion con la federacion (automatizado, post-deploy)

Consultar KB via `kb_route("federacion kora")` → `urn:ops:kb:federacion-kora-v2` para arquitectura y protocolo. Consultar KB via `kb_route("ux telegram")` → `urn:ops:kb:ux-telegram-openclaw` para configuracion de canal verificada.

**P17 — FEDERATION INTEGRATION.** Via `host_exec`:
1. Crear directorio shared del agente: `mkdir -p /srv/kora/shared/{agent_id}`.
2. Agregar bind mounts al docker-compose.yml del gateway: `../shared/federation:/home/node/shared/federation:ro` (siempre) y `../shared/{agent_id}:/home/node/shared/{agent_id}` (RW propio).
3. Configurar hooks en openclaw.json5: `hooks: { enabled: true, token: "{hooks_token}" }`. Token debe ser literal (OpenClaw no interpola env vars).
4. Configurar gateway bind: `gateway.bind: "lan"` (requerido para que otros containers en kora-federation alcancen el gateway; el port mapping Docker `127.0.0.1:{port}:{port}` sigue protegiendo del acceso externo).
5. NO duplicar el hooks token en `.env`, `TOOLS.md`, directorios compartidos ni outputs. Redactarlo siempre fuera de runtime config.
6. NO modificar `TOOLS.md` desplegado como overlay operacional. Publicar la metadata de federation en `/srv/kora/shared/federation/directorio-agentes.md` y en runtime config, sin convertir el workspace target en scratchpad operativo.
7. Actualizar `/srv/kora/shared/federation/directorio-agentes.md` con la nueva entrada del agente (dominio, gateway, hook URL, Telegram bot).
8. Verificar: `docker exec {container} cat /home/node/shared/federation/directorio-agentes.md` legible; `docker exec {container} touch /home/node/shared/{agent_id}/test` OK; hook test bidireccional con al menos un gateway existente via `curl POST /hooks/agent`.

**P18 — PANEL REGISTRATION.** Si panel web kora-panel esta desplegado:
1. Si el panel existe en un path operativo conocido, actualizar su `registry.json`: agregar entrada con gateway (container, host, port), compose path, config path, telegram bot, namespace, theme, emoji, shared dir.
2. Agregar visibilidad default en la matriz (`"none"` para todos los pares).
3. Rebuild y redeploy panel desde su path operativo real: `cd {kora_panel_path} && docker compose build && docker compose up -d`.
4. Verificar: `curl https://kora.sanixai.com/api/registry` muestra el nuevo agente.

**P19 — UX CHANNEL CONFIG.** Consultar KB `urn:ops:kb:ux-telegram-openclaw` para configuracion verificada. Aplicar al openclaw.json5 del gateway:
1. `channels.telegram.chunkMode: "length"` (no "newline" — fragmenta en 10+ burbujas).
2. `channels.telegram.markdown.tables: "bullets"` (no "code" — ilegible en movil).
3. `channels.telegram.replyToMode: "first"` (threading visual).
4. `channels.telegram.silentErrorReplies: true` (errores no suenan).
5. `channels.telegram.textChunkLimit: 4000` (maximo Telegram).
6. `channels.telegram.linkPreview: false` (evita previews distractores).
7. `agents.defaults.thinkingDefault: "adaptive"` (v2026.3.x — ajusta thinking a complejidad).
8. `session.reset`: segun perfil del agente — `mode: "idle", idleMinutes: 120` para agentes reactivos o `mode: "daily", atHour: 4` para agentes con sesiones de dia completo.
9. `session.maintenance: { pruneAfter: "30d", maxEntries: 500 }` para agentes con heartbeats o sesiones largas.
10. Aplicar via merge declarativo de config + restart; si existe `/srv/kora/scripts/sync-config.sh`, usarlo como helper. Verificar: `openclaw doctor` sin errores de schema.

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| agent_id | string | Agente desplegado |
| gateway_name | string | Nombre del gateway |
| architecture | enum | caso-a, caso-b |
| phases_completed | PhaseResult[] | {phase, status: ok/error/skipped/human-pending, detail} |
| human_checkpoints | HumanCheckpoint[] | {phase, instruction, data_collected} |
| deploy_status | enum | DEPLOYED, PARTIAL, FAILED |
| health | object | {doctor: PASS/FAIL, containers: healthy/unhealthy, e2e: confirmed/pending} |
| drift_summary | DriftEntry[] | Solo en P14: {file, type, recommendation} |
| federation | object | {shared_dir_created, hooks_configured, directorio_updated, panel_registered, ux_applied} |
| proximos_pasos | string[] | Acciones pendientes |
