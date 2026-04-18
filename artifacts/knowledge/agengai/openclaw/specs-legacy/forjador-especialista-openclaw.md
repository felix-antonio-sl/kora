---
_manifest:
  urn: "urn:agengai:kb:forjador-especialista-openclaw"
  provenance:
    created_by: "MENTE-OMEGA"
    created_at: "2026-03-26"
    source: "SPEC: openclaw-manual-integral.md + manual-integral-skills-openclaw.md"
  version: "1.0.0"
  status: published
  tags: [openclaw, forjador, especialista, despliegue, ubuntu, host, skills, ciclo-de-vida]
  lang: "es"
  extensions:
    agengai:
      type: skill-agent
      embodies: forjador-especialista-openclaw
      class: CLASE-3
---

# FORJADOR ESPECIALISTA — Despliegue, Configuración y Mantención de Agentes OpenClaw en Ubuntu Host

## Identidad Encarnada

```
NOMBRE: Forjador Especialista
VIBE: ingeniero de agentes, artesano de cerebros artificiales
EMOJI: 🔧
SUSTANCIA: Despliega, configura y mantiene agentes OpenClaw en producción
ESPECIALIDAD: Ciclo de vida completo de skills + operación en Ubuntu host
DESTINATARIO: Operadores que necesitan equipos de agentes funcionando 24/7
```

---

## 1. Arquitectura de Despliegue en Ubuntu Host

### 1.1 Topología Nativa vs Docker

| Aspecto | Host Native | Docker Container |
|---------|-------------|-----------------|
| Rendimiento | Óptimo (sin overhead) | Overhead de container |
| Aislamiento | Compartido con sistema | Aislamiento completo |
| Persistencia | Directa en filesystem | Bind mounts necesarios |
| Actualizaciones | `npm update -g` | Nuevo contenedor o rebuild |
| Gestión de servicios | systemd nativo | Docker daemon |
| RAM disponible | Toda la del host | Limitada al container |
| Recomendación | **Productivo multi-agente** | Aislamiento alto o desarrollo |

**Para este servidor (62GB RAM, Ubuntu 24.04)**: Despliegue **host native** con systemd.

### 1.2 Estructura de Directorios en Host

```
~/.openclaw/
├── openclaw.json                    # Config global del gateway
├── credentials/                     # OAuth tokens, API keys
├── agents/                         # Agentes (workspaces + estado)
│   └── <agentId>/
│       ├── agent/
│       │   └── auth-profiles.json  # Perfil de autenticación propio
│       ├── sessions/
│       │   ├── sessions.json
│       │   └── <sessionId>.jsonl
│       └── sessions-legacy/
├── workspaces/                     # Workspaces de agentes
│   └── <workspaceId>/
│       ├── AGENTS.md
│       ├── SOUL.md
│       ├── USER.md
│       ├── IDENTITY.md
│       ├── TOOLS.md
│       ├── HEARTBEAT.md
│       ├── BOOT.md
│       ├── MEMORY.md
│       ├── memory/
│       │   └── YYYY-MM-DD.md
│       ├── skills/
│       │   └── <skill-name>/
│       │       └── SKILL.md
│       └── hooks/
│           └── <hook-name>/
│               ├── HOOK.md
│               └── handler.ts
├── skills/                         # Skills compartidos entre agentes
│   └── <shared-skill>/
│       └── SKILL.md
├── hooks/                          # Hooks globales
├── cron/
│   ├── jobs.json
│   └── runs/
├── nodes/
│   ├── paired.json
│   └── pending.json
├── tools/                          # Herramientas instaladas por skills
├── logs/
│   └── commands.log
├── backups/
└── tmp/
```

---

## 2. Instalación en Ubuntu Host

### 2.1 Requisitos del Sistema

| Recurso | Mínimo | Recomendado | Este Servidor |
|---------|--------|-------------|---------------|
| OS | Ubuntu 22.04+ | Ubuntu 24.04 LTS | **Ubuntu 24.04.4 LTS** ✓ |
| Node.js | 22.14+ | Node 24 | **v24.13.1** ✓ |
| RAM | 4GB | 16GB+ | **62GB** ✓ |
| Disk | 10GB | 50GB+ | **34GB libre** ✓ |
| User | sudo | sudo | **felix sudo** ✓ |

### 2.2 Flujo de Instalación Completo

```bash
# 1. Verificar prerrequisitos
node --version        # Debe ser 22+ (idealmente 24)
npm --version
python3 --version
sudo --version

# 2. Instalar OpenClaw (recomendado)
curl -fsSL https://openclaw.ai/install.sh | bash

# 3. Verificar instalación
openclaw --version
openclaw --version  # v2026.x.x

# 4. Ejecutar doctor para verificar estado
openclaw doctor

# 5. Configurar onboarding básico
openclaw onboard --install-daemon
# Sigue el wizard interactivo:
#   - Provider: anthropic
#   - API Key: sk-ant-...
#   - Gateway token: generado automáticamente
#   - Canal inicial: telegram (opcional)

# 6. Instalar como servicio systemd
openclaw gateway install

# 7. Verificar servicio
openclaw daemon status
sudo systemctl status openclaw-gateway

# 8. Verificar que el gateway escucha
openclaw gateway status
ss -ltnp | grep 18789
```

### 2.3 Configuración Post-Instalación

```bash
# Ver config generada
cat ~/.openclaw/openclaw.json

# Configurar modelo por defecto
openclaw config set agents.defaults.model.primary "anthropic/claude-sonnet-4-6"

# Configurar fallbacks
openclaw config set agents.defaults.model.fallbacks '["openai/gpt-5.2"]'

# Habilitar hot reload (default)
openclaw config set gateway.reload.mode "hybrid"

# Configurar timezone para cron
openclaw config set agents.defaults.timezone "America/Argentina/Buenos_Aires"
```

---

## 3. Gestión del Gateway como Daemon

### 3.1 Comandos del Daemon

```bash
# Instalación del servicio
openclaw daemon install

# Iniciar/Parar/Restart
openclaw daemon start
openclaw daemon stop
openclaw daemon restart

# Estado
openclaw daemon status

# Ver logs en tiempo real
openclaw logs --follow

# Reiniciar y ver logs
openclaw daemon restart && openclaw logs --follow

# Desinstalar servicio
openclaw daemon uninstall
```

### 3.2 Gestión via systemd (avanzado)

```bash
# Ver servicio
systemctl --user status openclaw-gateway

# Comandos
systemctl --user start openclaw-gateway
systemctl --user stop openclaw-gateway
systemctl --user restart openclaw-gateway
systemctl --user enable openclaw-gateway

# Logs de systemd
journalctl --user -u openclaw-gateway -f

# Verificar que está corriendo
ps aux | grep openclaw
```

### 3.3 Acceso Remoto

```bash
# SSH tunnel para acceso remoto
ssh -N -L 18789:127.0.0.1:18789 user@host

# Con tunnel activo, verificar conectividad
openclaw --host 127.0.0.1 --port 18789 health

# O configurar Tailscale (preferido para acceso permanente)
openclaw config set gateway.bind "tailnet"
openclaw config set gateway.tailscale.mode "serve"
```

---

## 4. Gestión Multi-Agente

### 4.1 Crear un Nuevo Agente

```bash
# Añadir agente
openclaw agents add <agent-id> --workspace ~/.openclaw/workspaces/<workspace-id>

# Configurar modelo
openclaw config set agents.list '[
  {"id": "omega-primary", "default": true, "workspace": "~/.openclaw/workspaces/primary"},
  {"id": "omega-dev", "workspace": "~/.openclaw/workspaces/dev"},
  {"id": "omega-ops", "workspace": "~/.openclaw/workspaces/ops"}
]'

# Listar agentes
openclaw agents list

# Eliminar agente
openclaw agents delete <agent-id>
```

### 4.2 Configurar Bindings (Routing)

```bash
# Routing por canal
openclaw config set bindings '[
  {"agentId": "omega-primary", "match": {"channel": "telegram", "accountId": "main"}},
  {"agentId": "omega-dev", "match": {"channel": "telegram", "accountId": "dev"}},
  {"agentId": "omega-ops", "match": {"channel": "discord", "guildId": "123456789"}}
]'

# Ver bindings actuales
openclaw config get bindings
```

### 4.3 Configuración de Workspace

```bash
# Estructura de workspace para nuevo agente
mkdir -p ~/.openclaw/workspaces/<workspace-id>
mkdir -p ~/.openclaw/workspaces/<workspace-id>/skills
mkdir -p ~/.openclaw/workspaces/<workspace-id>/memory
mkdir -p ~/.openclaw/workspaces/<workspace-id>/hooks

# Archivo IDENTITY.md
cat > ~/.openclaw/workspaces/<workspace-id>/IDENTITY.md << 'EOF'
# <Nombre del Agente>

**Rol**: <propósito breve>
**Emoji**: 🤖
**Vibe**: <personalidad>
EOF

# Archivo SOUL.md
cat > ~/.openclaw/workspaces/<workspace-id>/SOUL.md << 'EOF'
# Alma del Agente

## Quién es
<descripción extendida>

## Límites hard (nunca cruza)
- Nunca modifica archivos fuera de su workspace
- Nunca revela credenciales
- Nunca actúa sin confirmar con el usuario cuando es requerido

## Tono y registro
- Formal / Casual / Técnico
- Lenguaje: Español

## Valores
1. <valor 1>
2. <valor 2>
EOF

# Archivo AGENTS.md
cat > ~/.openclaw/workspaces/<workspace-id>/AGENTS.md << 'EOF'
# Instrucciones Operativas

## Rol
<descripción detallada>

## Responsabilidades
- <responsabilidad 1>
- <responsabilidad 2>

## Workflows
### Workflow principal
1. <paso>
2. <paso>
EOF
```

---

## 5. Ciclo de Vida Completo de Skills

### 5.1 Las 3 Capas de un Skill

```
┌─────────────────────────────────────────────────────────────┐
│  TIER 1: CATÁLOGO (~50-100 tokens por skill)            │
│  name + description (inyectado en system prompt al inicio)  │
└────────────────────────────┬────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────┐
│  TIER 2: INSTRUCCIONES (<5000 tokens, SKILL.md completo) │
│  Cargado cuando el skill se activa                         │
└────────────────────────────┬────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────┐
│  TIER 3: RECURSOS (bajo demanda)                         │
│  scripts/, references/, assets/                             │
└─────────────────────────────────────────────────────────────┘
```

### 5.2 Crear un Skill — Paso a Paso

```bash
# 1. Crear directorio
mkdir -p ~/.openclaw/workspaces/<workspace-id>/skills/<skill-name>

# 2. Escribir SKILL.md
cat > ~/.openclaw/workspaces/<workspace-id>/skills/<skill-name>/SKILL.md << 'EOF'
---
name: mi-skill
description: Make me a sandwich. Use whenever the user asks for a sandwich or needs lunch prepared.
---

# Mi Skill

## Cuándo usar
Este skill se activa cuando el usuario pide un sándwich o necesita preparar almuerzo.

## Cómo usarlo
1. Identificar el tipo de sándwich solicitado
2. Verificar ingredientes disponibles
3. Preparar el sándwich según preferencias del usuario
4. Confirmar la preparación

## Gotchas
- Siempre verificar allergies alimentarias antes de preparar
- Si no hay ingredientes, informar inmediatamente
EOF

# 3. Verificar que se carga
openclaw skills list
openclaw skills list --eligible

# 4. Probar invocación
openclaw agent --message "Make me a sandwich"

# 5. Si tiene scripts, crear directorio
mkdir -p ~/.openclaw/workspaces/<workspace-id>/skills/<skill-name>/scripts
```

### 5.3 Templates de SKILL.md

#### Template Básico
```markdown
---
name: nombre-del-skill
description: Breve descripción de qué hace y cuándo usarlo. Fraseo imperativo: "Use when..."
---

# Título del Skill

## Cuándo usar
<condiciones de activación>

## Procedimiento
1. <paso>
2. <paso>

## Gotchas
- <edge case 1>
- <edge case 2>

## Ejemplo
```
<ejemplo de uso>
```
```

#### Template con Scripts
```markdown
---
name: data-processor
description: Process and analyze CSV data files. Use when user needs to transform or extract insights from CSV data.
metadata: {"openclaw":{"requires":{"bins":["python3"]}}}
---

# Data Processor Skill

## Cuándo usar
- Usuario necesita analizar archivos CSV
- Solicita transformaciones de datos tabulares
- Necesita extraer estadísticas o patrones

## Scripts disponibles

### `scripts/analyze_csv.py`
Análisis básico de CSV:
```bash
python3 {baseDir}/scripts/analyze_csv.py --file <path> --operation <type>
```

### `scripts/transform.py`
Transformaciones:
```bash
python3 {baseDir}/scripts/transform.py --input <file> --output <file> --transform <type>
```

## Procedimiento
1. Recibir archivo CSV
2. Ejecutar `analyze_csv.py` para obtener estadísticas básicas
3. Si se requieren transformaciones, usar `transform.py`
4. Reportar resultados

## Gotchas
- El archivo debe tener extensión .csv
- La primera fila debe contener headers
- Si el archivo > 10MB, usar chunking
```

### 5.4 Gating — Control de Elegibilidad

```markdown
# Skill solo para Linux
---
name: linux-admin
description: Linux system administration tasks. Use when managing Ubuntu servers or workstations.
metadata: {"openclaw":{"os":["linux"]}}}
---

# Linux Admin Skill
```

```markdown
# Skill que requiere binario específico
---
name: docker-manager
description: Manage Docker containers and images. Use when user needs to deploy or monitor containers.
metadata: {"openclaw":{"requires":{"bins":["docker","docker-compose"]}}}
---

# Docker Manager Skill
```

```markdown
# Skill con requerimiento de config
---
name: web-server
description: Configure and manage web servers. Use when setting up nginx or apache.
metadata: {"openclaw":{"requires":{"config":["channels.telegram.enabled"]}}}
---

# Web Server Skill
```

### 5.5 Verificación y Debugging

```bash
# Listar todos los skills (locales + bundled)
openclaw skills list

# Listar solo skills elegibles (que pasan gating)
openclaw skills list --eligible

# Info detallada de un skill
openclaw skills info <skill-name>

# Diagnosticar problemas de un skill
openclaw skills check

# Ver en contexto del sistema
openclaw doctor

# Ver qué herramientas tiene disponibles
# (desde chat del agente)
/tools

# Ver tamaño del system prompt por skill
# (desde chat del agente)
/context detail
```

### 5.6 Actualización de Skills

```bash
# Actualizar un skill específico
openclaw skills update <skill-name>

# Actualizar todos los skills
openclaw skills update --all

# Reiniciar gateway para recargar
openclaw gateway restart

# O simplemente iniciar nueva sesión (hot reload)
/new
```

### 5.7 Deshabilitar/Eliminar Skills

```bash
# Deshabilitar sin eliminar (persiste en disco)
openclaw config set skills.entries.<skill-name>.enabled false

# Habilitar
openclaw config set skills.entries.<skill-name>.enabled true

# Eliminar skill
rm -rf ~/.openclaw/workspaces/<workspace-id>/skills/<skill-name>

# Verificar tras cambios
openclaw skills list
openclaw skills list --eligible
```

---

## 6. Hooks — Automatización Basada en Eventos

### 6.1 Tipos de Eventos

| Evento | Trigger |
|--------|---------|
| `command:new` | Usuario envía `/new` |
| `command:reset` | Usuario envía `/reset` |
| `command:stop` | Usuario envía `/stop` |
| `session:compact:before` | Antes de compactación |
| `session:compact:after` | Después de compactación |
| `agent:bootstrap` | Antes de inyectar bootstrap files |
| `gateway:startup` | Gateway inicia |
| `message:received` | Mensaje entrante |
| `message:sent` | Mensaje saliente |
| `message:preprocessed` | Post-enriquecimiento de mensaje |

### 6.2 Crear un Hook

```bash
# Crear directorio del hook
mkdir -p ~/.openclaw/workspaces/<workspace-id>/hooks/mi-hook

# HOOK.md
cat > ~/.openclaw/workspaces/<workspace-id>/hooks/mi-hook/HOOK.md << 'EOF'
---
emoji: "🔔"
events: ["gateway:startup", "command:new"]
export: "default"
---

# Mi Hook

Este hook ejecuta en gateway startup y comando /new.
EOF

# handler.ts (TypeScript)
cat > ~/.openclaw/workspaces/<workspace-id>/hooks/mi-hook/handler.ts << 'EOF'
import type { HookHandler } from 'openclaw/plugin-sdk/core'

export default {
  async default(params: { api: any }) {
    const { api } = params
    api.logger.info('Mi hook ejecutándose')
    
    // Lógica del hook
    return { handled: true }
  }
} satisfies HookHandler
EOF

# Habilitar el hook (requiere habilitación explícita para workspace hooks)
openclaw hooks enable mi-hook

# Ver hooks disponibles
openclaw hooks list

# Ver estado
openclaw hooks list --eligible
```

---

## 7. Configuración de Canales

### 7.1 Telegram (más rápido)

```bash
# Configurar Telegram
openclaw config set channels.telegram.enabled true
openclaw config set channels.telegram.botToken "123456:ABC-DEF..."

# Verificar
openclaw channels status telegram

# Grupos: requerir mention
openclaw config set channels.telegram.groups.policy "allowlist"
openclaw config set channels.telegram.groups.requireMention true
```

### 7.2 Discord

```bash
# Configurar Discord
openclaw config set channels.discord.enabled true
openclaw config set channels.discord.botToken "MTIz...=="

# Configurar intents requeridos
openclaw config set channels.discord.intents '["GUILD_MESSAGES","MESSAGE_CONTENT"]'

# Verificar
openclaw channels status discord
```

### 7.3 Slack

```bash
# Configurar Slack
openclaw config set channels.slack.enabled true
openclaw config set channels.slack.appToken "xapp-xxx"
openclaw config set channels.slack.botToken "xoxb-xxx"

# Modo Socket (default)
openclaw config set channels.slack.mode "socket"
```

---

## 8. Mantenimiento y Monitoreo

### 8.1 Health Checks

```bash
# Health check rápido
openclaw health

# Health check profundo
openclaw health --json

# Status detallado
openclaw status
openclaw status --deep

# Ver canales
openclaw channels status
openclaw channels status --probe
```

### 8.2 Logs

```bash
# Ver logs en tiempo real
openclaw logs --follow

# Ver últimas 100 líneas
openclaw logs | tail -100

# Logs de un canal específico
openclaw channels logs --channel telegram

# Guardar logs
openclaw logs > /tmp/openclaw-$(date +%Y%m%d).log
```

### 8.3 Session Management

```bash
# Ver sesiones activas
openclaw sessions list

# Ver detalle de sesión
openclaw sessions <session-id>

# Resetear sesión
# (desde chat del agente)
/new
/reset

# Maintenance mode
openclaw config set session.maintenance.mode "warn"
```

### 8.4 Cron Jobs

```bash
# Listar jobs
openclaw cron list

# Añadir job (diario a las 7am)
openclaw cron add \
  --name "Daily Report" \
  --cron "0 7 * * *" \
  --tz "America/Argentina/Buenos_Aires" \
  --session isolated \
  --message "Generar reporte diario" \
  --announce

# Ver runs
openclaw cron runs <job-id>

# Habilitar/Deshabilitar
openclaw cron enable <job-id>
openclaw cron disable <job-id>
```

### 8.5 Backup

```bash
# Crear backup
openclaw backup create

# Ver backups
openclaw backup list

# Verificar backup
openclaw backup verify <backup-id>

# Restaurar (si es necesario)
# openclaw backup restore <backup-id>
```

---

## 9. Seguridad — Hardening

### 9.1 Auditoría Rápida

```bash
# Auditoría de seguridad
openclaw security audit

# Auditoría profunda
openclaw security audit --deep

# Aplicar fixes automáticos
openclaw security audit --fix
```

### 9.2 Configuración Dura Recomendada

```bash
# DM scope para aislamiento
openclaw config set session.dmScope "per-channel-peer"

# Exec deny por defecto
openclaw config set tools.exec.security "deny"

# Sandbox para sesiones no-main
openclaw config set agents.defaults.sandbox.mode "non-main"

# Deshabilitar elevated por defecto
openclaw config set tools.elevated.enabled false
```

### 9.3 Gestión de Secrets

```bash
# Añadir API key como secret
openclaw config set agents.defaults.env.ANTHROPIC_API_KEY "sk-ant-..."

# Usar SecretRef (más seguro)
openclaw config set skills.entries.mi-skill.apiKey '{
  "source": "env",
  "provider": "default",
  "id": "MI_API_KEY"
}'

# Recargar secrets
openclaw secrets reload

# Audit de secrets
openclaw secrets audit
```

---

## 10. Troubleshooting

### 10.1 Gateway No Inicia

```bash
# Ver logs de systemd
journalctl --user -u openclaw-gateway -n 100

# Ver si hay error de puerto
ss -ltnp | grep 18789

# Ver config con validacion
openclaw config validate

# Doctor completo
openclaw doctor --repair --yes
```

### 10.2 Skills No Cargan

```bash
# Verificar que el directorio existe
ls -la ~/.openclaw/workspaces/*/skills/

# Ver skills elegibles
openclaw skills list --eligible

# Verificar SKILL.md
head -20 ~/.openclaw/workspaces/*/skills/*/SKILL.md

# Revisar logs
openclaw logs | grep -i skill

# Verificar gating (OS, bins, env)
openclaw skills check
```

### 10.3 Agente No Responde

```bash
# Ver estado del gateway
openclaw gateway status

# Ver sesiones
openclaw sessions list

# Resetear sesión manualmente
openclaw sessions <session-id> reset

# Ver cola
openclaw status

# Reiniciar gateway
openclaw daemon restart
```

### 10.4 Problemas de Memoria/Contexto

```bash
# Ver uso de contexto
# (desde chat del agente)
/context detail

# Forzar compactación
# (desde chat del agente)
/compact

# Reducir uso con modelos más pequeños
openclaw config set agents.defaults.model.primary "anthropic/claude-haiku-4-6"
```

---

## 11. Actualización y Migración

### 11.1 Actualizar OpenClaw

```bash
# Ver versión actual
openclaw --version

# Actualizar
npm update -g openclaw@latest

# O usar el comando built-in
openclaw update

# Reiniciar tras actualizar
openclaw daemon restart

# Verificar
openclaw doctor
```

### 11.2 Migración de Config Legacy

```bash
# Ejecutar doctor con migración
openclaw doctor --repair --yes

# Ver config normalizada
openclaw config get
```

### 11.3 Migrar a Nuevo Servidor

```bash
# 1. Backup en servidor viejo
openclaw backup create

# 2. Copiar archivos críticos
rsync -avz ~/.openclaw/ user@newserver:~/

# 3. Instalar OpenClaw en nuevo servidor
curl -fsSL https://openclaw.ai/install.sh | bash

# 4. Restaurar config (si no se copió todo)
openclaw backup restore <backup-id>

# 5. Verificar
openclaw doctor
openclaw gateway status
```

---

## 12. Workflows del Forjador

### 12.1 Workflow: Desplegar Nuevo Agente

```
┌──────────────────────────────────────────────────────────────────┐
│  1. ESPECIFICAR                                                     │
│     agentId, nombre, propósito, modelo, canales, skills           │
└────────────────────────────┬─────────────────────────────────────┘
                             ↓
┌──────────────────────────────────────────────────────────────────┐
│  2. CREAR WORKSPACE                                               │
│     mkdir + archivos bootstrap (IDENTITY, SOUL, AGENTS, USER)   │
└────────────────────────────┬─────────────────────────────────────┘
                             ↓
┌──────────────────────────────────────────────────────────────────┐
│  3. CONFIGURAR                                                    │
│     openclaw.json: agents.list + bindings                         │
└────────────────────────────┬─────────────────────────────────────┘
                             ↓
┌──────────────────────────────────────────────────────────────────┐
│  4. INSTALAR SKILLS                                               │
│     mkdir skills/<name> + SKILL.md + scripts                       │
└────────────────────────────┬─────────────────────────────────────┘
                             ↓
┌──────────────────────────────────────────────────────────────────┐
│  5. VERIFICAR                                                      │
│     openclaw agents list                                          │
│     openclaw skills list --eligible                              │
│     openclaw gateway restart                                      │
└────────────────────────────┬─────────────────────────────────────┘
                             ↓
┌──────────────────────────────────────────────────────────────────┐
│  6. PROBAR                                                        │
│     openclaw agent --message "Prueba de conectividad"             │
└──────────────────────────────────────────────────────────────────┘
```

### 12.2 Workflow: Crear y Deployar Skill

```
┌──────────────────────────────────────────────────────────────────┐
│  1. DISEÑAR                                                       │
│     Propósito, triggers, procedimientos, gotchas                    │
└────────────────────────────┬─────────────────────────────────────┘
                             ↓
┌──────────────────────────────────────────────────────────────────┐
│  2. CREAR DIRECTORIO                                              │
│     mkdir -p workspace/skills/<skill-name>/scripts,references     │
└────────────────────────────┬─────────────────────────────────────┘
                             ↓
┌──────────────────────────────────────────────────────────────────┐
│  3. ESCRIBIR SKILL.md                                             │
│     frontmatter + instrucciones + ejemplos                         │
└────────────────────────────┬─────────────────────────────────────┘
                             ↓
┌──────────────────────────────────────────────────────────────────┐
│  4. CREAR SCRIPTS (si aplica)                                    │
│     scripts/* + tests básicos                                      │
└────────────────────────────┬─────────────────────────────────────┘
                             ↓
┌──────────────────────────────────────────────────────────────────┐
│  5. VALIDAR                                                        │
│     skills-ref validate ./mi-skill                                 │
│     openclaw skills list                                          │
│     openclaw skills check                                        │
└────────────────────────────┬─────────────────────────────────────┘
                             ↓
┌──────────────────────────────────────────────────────────────────┐
│  6. PROBAR INVOCACIÓN                                             │
│     openclaw agent --message "Invocar skill"                    │
└────────────────────────────┬─────────────────────────────────────┘
                             ↓
┌──────────────────────────────────────────────────────────────────┐
│  7. ITERAR (si necesario)                                         │
│     Ajustar description → trigger rate                            │
│     Ajustar procedimientos → calidad output                        │
└──────────────────────────────────────────────────────────────────┘
```

---

## 13. Comandos de Referencia Rápida

### Gateway
```bash
openclaw gateway status
openclaw gateway restart
openclaw gateway install
openclaw daemon start|stop|restart|status
```

### Agentes
```bash
openclaw agents list
openclaw agents add <id> --workspace <path>
openclaw agents delete <id>
openclaw config set agents.list '[]'
```

### Skills
```bash
openclaw skills list
openclaw skills list --eligible
openclaw skills info <name>
openclaw skills check
openclaw skills update <name>
openclaw skills update --all
```

### Config
```bash
openclaw config get
openclaw config set <key> <value>
openclaw config validate
openclaw doctor --repair --yes
```

### Logs y Status
```bash
openclaw logs --follow
openclaw health
openclaw status
openclaw status --deep
openclaw channels status
```

### Seguridad
```bash
openclaw security audit
openclaw security audit --fix
openclaw secrets audit
openclaw secrets reload
```

---

*Forjador Especialista v1.0.0 — Creado por MENTE-OMEGA — OpenClaw 2026.3+*
