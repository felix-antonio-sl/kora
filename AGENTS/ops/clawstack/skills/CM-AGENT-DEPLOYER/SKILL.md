---
_manifest:
  urn: urn:ops:skill:clawstack-agent-deployer:1.0.0
  type: lazy_load_endofunctor
extensions:
  ops:
    skill:
      form: extended
      allowed_tools:
        - host_exec
        - docker_exec
        - oc_cli
        - kb_route
      requires: []
      references:
        - references/deploy-phases-checklist.md
        - references/hetzner-audit-findings.md
      assets:
        - assets/strip-frontmatter.sh
---

# CM-AGENT-DEPLOYER

## Proposito

Ejecutar el pipeline completo de 16 fases para desplegar un agente KORA transmutado a un gateway OpenClaw corriendo en Docker sobre un servidor remoto. Automatiza las fases ejecutables y guia al operador a traves de las interactivas (bot creation, auth setup, pairing, e2e verification) con checkpoints de espera y reanudacion.

## Input/Output

- **Input:** transmutation_path: string (path a _transmutation.yml o directorio de artefactos transmutados), gateway_name: string, agent_id: string, kora_repo: string (default: /home/felix/kora)
- **Output:** DeployReport (ver Signature Output)

## Procedimiento

Consultar `references/deploy-phases-checklist.md` para verificacion y `references/hetzner-audit-findings.md` para gotchas conocidos. Consultar KB via `kb_route("deploy agentes")` → `urn:ops:kb:deploy-agente-kora-en-openclaw` para procedimiento detallado. Consultar KB via `kb_route("principios transmutacion")` → `urn:ops:kb:principios-transmutacion-kora-openclaw` para marco conceptual.

### Grupo A: Preparacion de infraestructura (automatizado)

**P01 — PROVISIONING.** Via `host_exec`: crear estructura `/srv/kora/{compose,config/{gateway},workspaces/{gateway}/agents/{agent}/{skills,memory},knowledge,scripts,backups}`. Fijar ownership `chown -R $(whoami):$(whoami) /srv/kora`. Verificar estructura con `ls -la`.

**P02 — STRIP AND COPY.** Leer _transmutation.yml para obtener lista de componentes fuente. Via `host_exec`: definir funcion strip_frontmatter (usar `assets/strip-frontmatter.sh` o inline Python del tutorial §4.2). Para cada archivo bootstrap (AGENTS.md, SOUL.md, TOOLS.md, USER.md, IDENTITY.md): strip frontmatter y copiar a workspace. Para skills degenerados (CM-*.md): strip y copiar. Para skills extendidos (CM-*/SKILL.md): strip SKILL.md y copiar directorio completo con fibras (scripts/, references/, assets/). Excluir config.json (metadata KORA, no workspace — principios P3). Verificar: conteo de archivos coincide con fuente.

**P03 — KB SYNC.** Leer `deployment_hints.kb_mounts` de _transmutation.yml. Para cada KB: resolver URN via catalogo, strip frontmatter, copiar a `/srv/kora/knowledge/{ns}/{file}`. Fijar permisos read-only. KBs NO van en bootstrap — son archivos montados que el agente lee on-demand (principios P8). Verificar: conteo y tamanos aproximados coinciden.

**P04 — DOCKER BUILD.** Via `docker_exec`: build imagen base OpenClaw (`docker build -t openclaw-local:latest .` desde repo OpenClaw). Si `deployment_hints.requires_sidecar == true`: build imagen sidecar. Si `deployment_hints.architecture == "caso-b"`: build overlay gateway con ENV del sidecar API. Verificar: `docker images` muestra tags esperados.

### Grupo B: Checkpoint interactivo — Bot creation (guiado)

**P06 — BOT CREATION.** Emitir instrucciones al operador:
1. "Abrir Telegram, buscar @BotFather, enviar /newbot"
2. "Elegir nombre y username para el bot del agente"
3. "Copiar el token (formato: 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11)"
4. "Buscar @userinfobot en Telegram, enviar cualquier mensaje, copiar user ID (INTEGER sin comillas)"
Requiere del operador: TELEGRAM_BOT_TOKEN, TELEGRAM_USER_ID. Almacenar para P07.

### Grupo C: Configuracion de entorno y volume (automatizado)

**P05 — CONFIG PARAMETRIZATION.** Leer config-snippet de _transmutation.yml. Parametrizar openclaw.json5: agent_id, gateway_name, puerto (spacing minimo 20 entre gateways — principios P7; detectar puertos existentes via `docker ps`), modelo, identity, sandbox, channels con datos de P06. Escribir a `/srv/kora/config/{gateway}/openclaw.json5`. Para kora-federation: detectar si ya existe (`docker network ls | grep kora-federation`); si existe usar `external: true`, si no crearla con `driver: bridge` (hallazgo H3). Si agente tiene bindings a proyectos dev (detectar de TOOLS.md): agregar mounts RW (hallazgo H5). Parametrizar docker-compose.yml: imagen, container name, puerto, volumes, red. Escribir a `/srv/kora/compose/docker-compose.yml`. Verificar: `docker compose config --quiet`.

**P07 — ENV GENERATION.** Via `host_exec`: generar OPENCLAW_AUTH_TOKEN (`openssl rand -hex 32`). Escribir .env con TELEGRAM_BOT_TOKEN (de P06), OPENCLAW_AUTH_TOKEN, NODE_ENV=production. Si sidecar: agregar SERVICE_API. `chmod 600 /srv/kora/compose/.env`. Actualizar openclaw.json5 con TELEGRAM_USER_ID (como integer) en `channels.telegram.allowFrom`. Verificar: .env existe con permisos correctos.

**P08 — VOLUME INIT.** Via `docker_exec`: pre-seed named volume con `docker compose run --rm --user root --no-deps --entrypoint sh gateway` para crear dirs y fijar ownership uid 1000 (node). Copiar config al volume. Verificar: dirs creados, config copiado, ownership correcta.

### Grupo D: Checkpoint interactivo — Auth setup (guiado)

**P09 — AUTH SETUP.** Emitir instrucciones al operador:
- "Ejecutar: `cd /srv/kora/compose && docker compose run --rm --no-deps gateway openclaw models auth setup-token --provider anthropic`"
- "Esto abre un flujo OAuth en tu browser. Completarlo y regresar aqui."
- Alternativa: si el operador tiene API key directa, agregar ANTHROPIC_API_KEY al .env y saltar OAuth.
Requiere confirmacion del operador.

### Grupo E: Validacion y deploy (automatizado)

**P10 — DOCTOR.** Via `docker_exec`: `docker compose run --rm --no-deps gateway openclaw doctor`. Parsear output. Esperado: cero errores de config. Warnings aceptables: gateway auth token missing, systemd unavailable, memory search disabled. Si errores: DETENER — no proceder a deploy. Reportar errores y sugerir fix.

**P11 — DEPLOY.** Via `docker_exec`: `docker compose up -d`. Verificar: `docker compose ps` muestra containers Up/healthy. Verificar: `docker compose logs --tail 20 gateway` contiene indicadores de arranque exitoso (agent model, listening on ws://, channel starting). Si containers en restart loop: detener y transicionar a S-TROUBLESHOOT.

### Grupo F: Checkpoints interactivos — Pairing y verificacion (guiado)

**P12 — PAIRING.** Emitir: "Enviar cualquier DM al bot en Telegram". Via `oc_cli`: `docker compose exec gateway openclaw pairing list telegram`. Mostrar codigos al operador. Preguntar cual aprobar. Via `oc_cli`: `docker compose exec gateway openclaw pairing approve telegram {CODE}`.

**P13 — E2E VERIFICATION.** Emitir: "Enviar un mensaje de test al bot por Telegram. El agente debe responder coherentemente con su personalidad (SOUL.md) y comportamiento (AGENTS.md)." Si sidecar: "Verificar que la respuesta incluye datos del servicio externo, no solo texto conversacional." Requiere confirmacion del operador.

### Grupo G: Lifecycle operacional (automatizado, on-demand)

**P14 — DRIFT MANAGEMENT.** Via `host_exec`: para cada archivo bootstrap, diff version stripped del repo vs version desplegada. Clasificar drift: regla emergente (backport candidate), residuo (limpiar), memory (normal, skip), HEARTBEAT.md (normal, skip). Reportar resumen con recomendaciones.

**P15 — BACKUP.** Via `docker_exec`: `docker cp kora-{name}:/home/node/.openclaw/agents /srv/kora/backups/agents-$(date +%Y%m%d)`. Si sidecar: `docker cp kora-{service}:/app/data /srv/kora/backups/{service}-$(date +%Y%m%d)`. Reportar paths y tamanos.

**P16 — RESYNC.** Cuando cambie el agente en el repo: re-ejecutar P02 para archivos cambiados. Si config cambio: usar sync-config.sh (hallazgo H7) o re-ejecutar P05 + copy al volume (§6.7 del tutorial). Via `docker_exec`: `docker compose restart gateway`. Verificar: containers healthy, logs limpios.

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
| proximos_pasos | string[] | Acciones pendientes |
