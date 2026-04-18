---
_manifest:
  urn: urn:ops:kb:deploy-agente-kora-en-openclaw-p02
  provenance:
    created_by: ops/clawstack
    created_at: '2026-03-19'
    updated_at: '2026-03-23'
    source: Experiencia operacional desplegando korax v3.4.0, steipete v1.5.1 y salubrista-hah
      v1.0.0 en Hetzner sobre OpenClaw v2026.3.22
version: 1.2.0
status: published
tags:
- deploy
- openclaw
- docker
- tutorial
- operaciones
- transmutacion
- federation
- hooks
- ux
lang: es
extensions:
  kora:
    shard_index: 2
    shard_count: 4
    shard_root_urn: urn:ops:kb:deploy-agente-kora-en-openclaw
relations:
  cites:
  - urn:korvo:kb:manual-de-vida
  - urn:ops:kb:ux-telegram-openclaw
---


# Tutorial: Desplegar un agente KORA en OpenClaw - Parte 02

## c) openclaw.json5

```json5
{
 agents: {
 defaults: {
 workspace: "/home/node/.openclaw/workspace",
 model: { primary: "anthropic/claude-opus-4-6" },
 models: {
 "anthropic/claude-opus-4-6": {
 params: {
 cacheRetention: "long", // cache de bootstrap ~1h
 // context1m: true, // Solo con API key directa, NO con OAuth/setup-token
 },
 },
 },
 memorySearch: { enabled: false }, // desactivar si no hay embedding provider
 },
 list: [
 {
 id: "<agent-id>",
 default: true,
 identity: { // identity va DENTRO de agents.list[], NO top-level
 name: "<NombreAgente>",
 theme: "<descripcion>",
 emoji: "<emoji>",
 },
 }
 ],
 },
 session: { scope: "per-sender" }, // reset.mode solo acepta "daily"|"idle"
 gateway: {
 mode: "local",
 port: 18789,
 bind: "lan", // "lan" obligatorio en Docker para hooks cross-gateway (P15)
 controlUi: { enabled: true, basePath: "/openclaw" },
 auth: { mode: "token" }, // doctor genera el token automaticamente
 },
 channels: {
 telegram: {
 enabled: true,
 dmPolicy: "allowlist",
 allowFrom: [<TELEGRAM_USER_ID>], // numerico (integer), de @userinfobot
 groupPolicy: "disabled",
 streaming: "partial",
 chunkMode: "length", // NO "newline" — fragmenta por párrafo (ver urn:ops:kb:ux-telegram-openclaw)
 markdown: { tables: "bullets" }, // tablas legibles en móvil
 replyToMode: "first", // threading visual
 silentErrorReplies: true, // errores no suenan
 ackReaction: "<emoji>",
 reactionLevel: "minimal",
 linkPreview: false,
 textChunkLimit: 4000,
 },
 },
}
```

> **Errores comunes en openclaw.json5** (todos causan `Config invalid` al arrancar):
>
> | Error | Sintoma | Fix |
> |-------|---------|-----|
> | `identity` como key top-level | `identity was moved; use agents.list[].identity` | Mover a `agents.list[0].identity` |
> | `session.reset.mode: "manual"` | `Invalid input` | Usar `"daily"` o `"idle"`, o no incluir `reset` |
> | `gateway.bind: "0.0.0.0"` | `Invalid input` | Usar `"loopback"` (o `"lan"` si necesitas acceso LAN) |
> | `allowFrom: ["123"]` | String en vez de number | Usar `allowFrom: [123]` (integer sin comillas) |

## d) .env

```bash
TELEGRAM_BOT_TOKEN=<token de @BotFather>
OPENCLAW_AUTH_TOKEN=<openssl rand -hex 32>
NODE_ENV=production
```

---

## 4. Preparar el servidor

### 4.1 Estructura de directorios

```
/srv/kora/
├── compose/
│ ├── docker-compose.yml
│ └── .env (chmod 600)
├── config/
│ └── <gateway>/
│ └── openclaw.json5
├── workspaces/
│ └── <gateway>/agents/<agent>/
│ ├── AGENTS.md (sin frontmatter KORA)
│ ├── SOUL.md
│ ├── TOOLS.md
│ ├── USER.md
│ ├── IDENTITY.md
│ ├── skills/
│ └── memory/ (persistente)
├── knowledge/ (rsync desde repo KORA, read-only)
│ └── <namespace>/ (solo KBs que el agente necesita, per allowed_kb)
├── comms/ (buzones inter-cuadrilla, futuro)
├── scripts/
└── backups/
```

```bash
# Crear estructura (reemplazar <gateway> y <agent>)
sudo mkdir -p /srv/kora/{compose,config/<gateway>,scripts,backups,comms}
sudo mkdir -p /srv/kora/workspaces/<gateway>/agents/<agent>/{skills,memory}
sudo mkdir -p /srv/kora/
sudo chown -R $(whoami):$(whoami) /srv/kora
```

### 4.2 Strip de frontmatter KORA

OpenClaw no entiende el frontmatter `_manifest` de KORA. Hay que stripearlo al copiar:

```bash
strip_frontmatter {
 local src="$1" dst="$2"
 python3 -c "
content = open('$src').read
if content.startswith('---'):
 parts = content.split('---', 2)
 if len(parts) >= 3:
 open('$dst', 'w').write(parts[2].lstrip('\n'))
 return
open('$dst', 'w').write(content)
"
}

# Reemplazar paths con los de tu agente:
KORA_REPO=/home/felix/kora
SRC=$KORA_REPO/AGENTS/<namespace>/<agent>
DST=/srv/kora/workspaces/<gateway>/agents/<agent>

for file in AGENTS.md SOUL.md TOOLS.md USER.md IDENTITY.md; do
 [ -f "$SRC/$file" ] && strip_frontmatter "$SRC/$file" "$DST/$file"
done

for skill in "$SRC"/skills/CM-*.md; do
 [ -f "$skill" ] && strip_frontmatter "$skill" "$DST/skills/$(basename $skill)"
done
```

### 4.3 Sync de Knowledge Base

Copiar solo las KBs declaradas en `config.json → allowed_kb`. Tambien sin frontmatter:

```bash
# Por cada KB en allowed_kb, resolver path y copiar
# Ejemplo: urn:korvo:kb:manual-de-vida → 
strip_frontmatter \
 $KORA_REPO/ \
 /srv/kora/
```

**Las KBs no van en el bootstrap** (pueden ser decenas de KB extra que explotarian la ventana). Van como archivos montados read-only que el agente lee bajo demanda via filesystem.

### 4.4 Permisos

OpenClaw corre como uid 1000 (usuario `node`) dentro del container:

```bash
sudo chown -R 1000:1000 /srv/kora/workspaces/<gateway>/agents/<agent>
chmod 600 /srv/kora/compose/.env
```

---

## 5. Build de imagenes Docker

### 5.1 Imagen base OpenClaw

```bash
cd /home/felix/projects/openclaw
docker build -t openclaw-local:latest .
```

### 5.2 Imagen del gateway

**Caso A (sin sidecar):** usar directamente `openclaw-local:latest` en el compose. No se necesita build custom.

**Caso B (con sidecar):** agregar solo el ENV que indica donde esta el sidecar:

```bash
cd /home/felix/projects/openclaw
echo 'FROM openclaw-local:latest
ENV SERVICE_API=http://kora-<servicio>:8100/api' | docker build -t kora-<gateway>:latest -f - .
```

### 5.3 Imagen del sidecar (solo caso B)

Escribir el Dockerfile a disco y buildear:

```bash
cd /home/felix/projects/<servicio>

cat > /tmp/Dockerfile.sidecar << 'EOF'
FROM python:3.13-slim-bookworm
RUN useradd -r -s /usr/sbin/nologin app
WORKDIR /app
COPY server.py ./
COPY src/ ./src/
RUN mkdir -p /app/data && chown app:app /app/data
USER app
ENV PYTHONUNBUFFERED=1
EXPOSE 8100
HEALTHCHECK --interval=15s --timeout=5s --retries=3 \
 CMD python3 -c "from urllib.request import urlopen; urlopen('http://localhost:8100/health')"
CMD ["python3", "server.py"]
EOF

docker build -t kora-<servicio>:latest -f /tmp/Dockerfile.sidecar .
rm /tmp/Dockerfile.sidecar
```

---

## 6. Configuracion

Estos pasos se ejecutan en orden. Los primeros son interactivos (requieren datos humanos), los siguientes son mecanicos.

### 6.1 Crear bot de Telegram

1. Abrir Telegram, buscar **@BotFather**
2. Enviar `/newbot`
3. Elegir nombre y username
4. Copiar el token (formato: `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`)

### 6.2 Obtener tu Telegram user ID

1. Buscar **@userinfobot** en Telegram
2. Enviar cualquier mensaje
3. Copiar el numero (formato: `8734062810`)
4. Pegar en `openclaw.json5` → `channels.telegram.allowFrom` **como integer, sin comillas**

### 6.3 Rellenar .env y openclaw.json5

```bash
# Generar token de gateway
GATEWAY_TOKEN=$(openssl rand -hex 32)

# Escribir .env
cat > /srv/kora/compose/.env << EOF
TELEGRAM_BOT_TOKEN=<token de paso 6.1>
OPENCLAW_AUTH_TOKEN=$GATEWAY_TOKEN
NODE_ENV=production
EOF
chmod 600 /srv/kora/compose/.env

# Editar openclaw.json5 con tu Telegram user ID (integer)
nano /srv/kora/config/<gateway>/openclaw.json5
```

### 6.4 Inicializar el volume del gateway

El named volume se crea como root. OpenClaw necesita que sea owned por uid 1000 (node). Ademas, hay que copiar el config al volume (no se puede bind-mountear — ver nota en §3.4b).

```bash
cd /srv/kora/compose

# Paso 1: Pre-seed directorios con ownership correcta
docker compose run --rm --user root --no-deps --entrypoint sh gateway -c "
mkdir -p /home/node/.openclaw/agents /home/node/.openclaw/identity \
 /home/node/.openclaw/credentials /home/node/.openclaw/logs &&
find /home/node/.openclaw -exec chown node:node {} + 2>/dev/null
chmod 700 /home/node/.openclaw
"

# Paso 2: Copiar config al volume
docker compose run --rm --user root --no-deps --entrypoint sh gateway -c \
 "cp /dev/stdin /home/node/.openclaw/openclaw.json && chown node:node /home/node/.openclaw/openclaw.json && chmod 600 /home/node/.openclaw/openclaw.json" \
 < ../config/<gateway>/openclaw.json5
```

### 6.5 Configurar autenticacion del modelo

Para Anthropic con Claude Max (OAuth):

```bash
cd /srv/kora/compose
docker compose run --rm --no-deps gateway openclaw models auth setup-token --provider anthropic
```

`--no-deps` evita intentar levantar el sidecar durante el setup interactivo.

Para API key (sin OAuth): agregar `ANTHROPIC_API_KEY=sk-ant-...` al `.env`.

### 6.6 Validar config con doctor

```bash
docker compose run --rm --no-deps gateway openclaw doctor
```

Doctor debe reportar **cero errores de config**. Warnings aceptables:

| Warning | Evaluacion |
|---------|-----------|
| `Gateway auth token missing` | Se genera automaticamente al primer `up` |
| `Config file world-readable` | Dentro del volume, aislado por container |
| `systemd unavailable` | Normal en container — docker compose es el supervisor |
| `Memory search disabled` | Correcto si no hay embedding provider |

Si doctor reporta `Config invalid`, corregir antes de continuar. **No ignorar errores de validacion.**

### 6.7 Re-sync de config al volume

Cuando modifiques `openclaw.json5` en el host despues del deploy inicial:

```bash
cd /srv/kora/compose
docker compose run --rm --user root --no-deps --entrypoint sh gateway -c \
 "cp /dev/stdin /home/node/.openclaw/openclaw.json && chown node:node /home/node/.openclaw/openclaw.json" \
 < ../config/<gateway>/openclaw.json5
docker compose restart gateway
```

---
