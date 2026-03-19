---
_manifest:
  urn: "urn:ops:kb:deploy-agente-kora-en-openclaw"
  provenance:
    created_by: "ops/clawstack"
    created_at: "2026-03-19"
    source: "Experiencia operacional desplegando korax v3.4.0 en Hetzner sobre OpenClaw + PCA sidecar"
version: "1.0.0"
status: published
tags: [deploy, openclaw, docker, tutorial, operaciones, korax, pca]
lang: es
---

# Tutorial: Desplegar un agente KORA en OpenClaw

Este tutorial documenta el proceso completo de tomar un agente del ecosistema KORA y desplegarlo como gateway OpenClaw en un servidor remoto. Usa como caso real el deploy de **korax v3.4.0** (exoesqueleto cognitivo) con **PCA v4.1** como sidecar HTTP en un servidor Hetzner.

El proceso es generalizable a cualquier agente KORA.

---

## 1. Entender las dos capas

Un agente KORA vive en el repositorio como un **workspace** — un directorio con archivos markdown que definen su comportamiento, personalidad, herramientas y skills. OpenClaw es el **runtime** que encarna ese workspace: le da un gateway HTTP, canales de comunicación (Telegram, Discord), persistencia de sesión, y acceso a modelos LLM.

```
KORA (especificacion)              OpenClaw (runtime)
─────────────────────              ──────────────────
AGENTS/korvo/korax/                ~/.openclaw/workspace/
├── AGENTS.md        ──strip──▶   ├── AGENTS.md
├── SOUL.md          ──strip──▶   ├── SOUL.md
├── TOOLS.md         ──strip──▶   ├── TOOLS.md
├── USER.md          ──strip──▶   ├── USER.md
├── IDENTITY.md      ──strip──▶   ├── IDENTITY.md
├── config.json      (no se copia, es metadata KORA)
└── skills/          ──strip──▶   └── skills/
```

**"strip"** significa remover el frontmatter YAML de KORA (`---\n_manifest:\n...\n---`) que OpenClaw no entiende. El contenido operacional queda intacto.

### 1.1 Que hace cada archivo

| Archivo | KORA | OpenClaw | Funcion |
|---------|------|----------|---------|
| **AGENTS.md** | Comportamiento formal (FSM, transiciones, invariantes, reglas de integridad) | Inyectado en cada turno (main + sub-agentes) | Define QUE hace el agente y COMO opera |
| **SOUL.md** | Identidad dialectica, paradigma cognitivo, tono | Inyectado solo en main | Define QUIEN es el agente |
| **TOOLS.md** | Interfaz semantica declarada con bindings | Inyectado en cada turno | Define CON QUE opera el agente |
| **USER.md** | Perfil del operador, preferencias | Inyectado solo en main | Define PARA QUIEN trabaja |
| **IDENTITY.md** | Nombre, emoji, vibe | Inyectado solo en main | Identidad publica del agente |
| **config.json** | Security envelope, allowed_kb, tools.allow | No se copia | Metadata de gobernanza KORA |
| **skills/** | Capacidades lazy-load (CM-*.md) | Cargados bajo demanda | Procedimientos especializados |

### 1.2 Limite critico: token economy

OpenClaw trunca silenciosamente archivos bootstrap a **20,000 caracteres** por archivo. Todo lo que exceda se pierde sin aviso. El total de bootstrap no debe exceder **150,000 caracteres**.

**Regla practica:** mantener AGENTS.md bajo 17K chars para margen de seguridad.

Tecnicas de compresion sin perder semantica:
- Remover notacion formal (coalgebras, fibraciones, transformaciones naturales) — el LLM no las necesita para operar correctamente
- Compactar tablas de sub-campos opcionales a una linea descriptiva
- Mover detalles derivables a skills lazy-load (se cargan solo cuando se invocan)

---

## 2. Decidir la arquitectura de servicios

Un agente KORA puede necesitar servicios externos. korax usa **PCA v4.1** (sistema de persistencia con SQLite). La pregunta clave: ¿donde corre ese servicio?

### Opcion A: Dentro del container (volume mount)

```
┌─────────────────────┐
│  OpenClaw + Python3  │
│  + PCA CLI mounted   │
└─────────────────────┘
```

- Requiere Dockerfile custom (agrega python3 a imagen Node.js)
- Se rompe en cada upgrade de OpenClaw
- Mezcla runtimes — viola principio de superficie minima

### Opcion B: Sidecar HTTP (recomendada)

```
┌─────────────────┐    ┌──────────────┐
│  OpenClaw        │───▶│  PCA HTTP     │
│  (imagen intacta)│HTTP│  (python3)    │
└─────────────────┘    └──────────────┘
```

- Imagen OpenClaw no se modifica — upgrades limpios
- PCA escala y se monitorea independientemente
- Requiere un wrapper HTTP sobre la API existente

**Elegimos opcion B.** El wrapper HTTP es trivial si la API del servicio ya esta bien estructurada.

### 2.1 Escribir el wrapper HTTP

Si el servicio tiene una API Python limpia (funciones que reciben parametros y devuelven datos), el wrapper es mecanico:

```python
#!/usr/bin/env python3
"""Wrapper HTTP stdlib puro sobre API existente."""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self._respond({"status": "ok"})
        elif self.path == "/api/estado":
            conn = get_db()
            self._respond(api.estado(conn))
            conn.close()
        # ... mapear cada endpoint

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        if self.path == "/api/captura":
            conn = get_db()
            result = api.captura(conn, body["texto"], body.get("fuente", "otro"))
            self._respond({"id": result.id, "texto": result.texto})
            conn.close()
        # ... mapear cada endpoint

    def _respond(self, data, code=200):
        body = json.dumps(data, ensure_ascii=False, default=str).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
```

**Clave:** usar solo stdlib (`http.server`, `json`). Cero dependencias externas = imagen Docker minima.

### 2.2 Actualizar los bindings en TOOLS.md

Los bindings del agente deben reflejar el protocolo real. Antes (CLI):

```
- **Binding:** `python3 $PCA_CLI captura "<texto>" [--fuente <f>]`
```

Despues (HTTP sidecar):

```
- **Binding:** `POST $PCA_API/captura` body: `{"texto": "<texto>", "fuente": "<f>"}`
```

El agente usara `curl` via code_execution para invocar el sidecar. `curl` esta disponible en la imagen base de OpenClaw.

---

## 3. Preparar el paquete de deploy (local)

Antes de tocar el servidor, preparar todo localmente.

### 3.1 Crear IDENTITY.md

OpenClaw requiere este archivo para la identidad publica del agente. Si no existe en el workspace KORA, crearlo:

```markdown
---
_manifest:
  urn: "urn:<namespace>:agent-bootstrap:<agent>-identity:<version>"
  type: "bootstrap_identity"
---

name: <NombreAgente>
emoji: <emoji>
vibe: <descripcion corta del agente>
```

### 3.2 Auditar tamaños de bootstrap

```bash
for f in AGENTS/<ns>/<agent>/*.md; do
    chars=$(wc -c < "$f")
    echo "$(basename $f): $chars chars"
done
```

Si algun archivo excede 17K, comprimir. Si el total excede 100K, evaluar mover contenido a skills lazy-load.

### 3.3 Verificar dependencias del servicio externo

```bash
# Si el servicio es Python, verificar que es stdlib puro
python3 -c "
import ast, sys
from pathlib import Path
stdlib = set(sys.stdlib_module_names)
# ... analizar imports
"
```

Si tiene dependencias externas, agregarlas al Dockerfile del sidecar.

### 3.4 Escribir los archivos de deploy

Se necesitan 4 archivos:

**a) Dockerfile del sidecar:**

```dockerfile
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
```

**b) docker-compose.yml:**

```yaml
services:
  gateway:
    image: gateway-agent:latest
    container_name: kora-<nombre>
    restart: unless-stopped
    init: true                          # CRITICO: PID 1 signal handling (patron canonico OpenClaw)
    env_file: .env
    environment:
      HOME: /home/node                  # Canonico OpenClaw
      TERM: xterm-256color
    ports:
      - "127.0.0.1:18789:18789"        # Loopback only — Telegram usa long-polling outbound
    volumes:
      - agent-data:/home/node/.openclaw                                     # Named volume para state (config, identity, sessions, credentials)
      # Config se copia al volume via init — NO bind mount de archivo individual
      # (OpenClaw usa atomic rename que falla sobre bind mounts de archivos)
      - ../workspaces/<gateway>/agents/<agent>:/home/node/.openclaw/workspace  # Bind mount — permite hot-reload
      - ../knowledge:/home/node/knowledge:ro                                   # KBs read-only
    networks:
      - kora-federation
    depends_on:
      sidecar:
        condition: service_healthy
    deploy:
      resources:
        limits:
          memory: 2G                    # OpenClaw necesita ~1.5G con skills discovery
          cpus: "2.0"
    healthcheck:
      test: ["CMD", "node", "-e", "fetch('http://localhost:18789/openclaw/health').then(r=>{if(!r.ok)process.exit(1)}).catch(()=>process.exit(1))"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 15s
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"

  sidecar:
    image: kora-sidecar:latest
    container_name: kora-sidecar
    restart: unless-stopped
    volumes:
      - sidecar-data:/app/data
    networks:
      - kora-federation
    deploy:
      resources:
        limits:
          memory: 128M
          cpus: "0.5"
    healthcheck:
      test: ["CMD", "python3", "-c", "from urllib.request import urlopen; urlopen('http://localhost:8100/health')"]
      interval: 15s
      timeout: 5s
      retries: 3
      start_period: 5s
    logging:
      driver: json-file
      options:
        max-size: "5m"
        max-file: "3"

networks:
  kora-federation:
    driver: bridge
    name: kora-federation

volumes:
  agent-data:
  sidecar-data:
```

> **Por que NO se bind-mountea el config directamente:** OpenClaw escribe su config via atomic rename (write-to-tmp + rename). Un bind mount de archivo individual causa `EBUSY` porque el filesystem del host no permite rename sobre el mount point. La solucion es usar un named volume para todo `/home/node/.openclaw/` y copiar el config al volume en un paso de init (ver seccion 6.5).

**c) openclaw.json5:**

```json5
{
  agents: {
    defaults: {
      workspace: "/home/node/.openclaw/workspace",
      model: { primary: "anthropic/claude-opus-4-6" },
      models: {
        "anthropic/claude-opus-4-6": {
          params: {
            cacheRetention: "long",  // cache de bootstrap ~1h
            // context1m: true,      // Solo con API key directa, NO con OAuth/setup-token
          },
        },
      },
      memorySearch: { enabled: false },  // desactivar si no hay embedding provider
    },
    list: [
      {
        id: "<agent-id>",
        default: true,
        identity: {                      // identity va DENTRO de agents.list[], NO top-level
          name: "<NombreAgente>",
          theme: "<descripcion>",
          emoji: "<emoji>",
        },
      }
    ],
  },
  session: { scope: "per-sender" },      // reset.mode solo acepta "daily"|"idle"
  gateway: {
    mode: "local",
    port: 18789,
    bind: "loopback",                    // valores validos: "auto"|"lan"|"loopback"|"custom"|"tailnet"
    controlUi: { enabled: true, basePath: "/openclaw" },
    auth: { mode: "token" },             // doctor genera el token automaticamente
  },
  channels: {
    telegram: {
      enabled: true,
      dmPolicy: "allowlist",
      allowFrom: [<TELEGRAM_USER_ID>],   // numerico (integer), de @userinfobot
      groupPolicy: "disabled",
      streaming: "partial",
      ackReaction: "<emoji>",
      reactionLevel: "minimal",
      linkPreview: false,
      textChunkLimit: 4000,
      chunkMode: "newline",
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

**d) .env:**

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
│   ├── docker-compose.yml
│   └── .env                    (chmod 600)
├── config/
│   └── <gateway>/
│       └── openclaw.json5
├── workspaces/
│   └── <gateway>/agents/<agent>/
│       ├── AGENTS.md           (sin frontmatter KORA)
│       ├── SOUL.md
│       ├── TOOLS.md
│       ├── USER.md
│       ├── IDENTITY.md
│       ├── skills/
│       └── memory/             (persistente)
├── knowledge/                  (rsync desde repo KORA, read-only)
├── comms/                      (buzones inter-cuadrilla, futuro)
├── scripts/
└── backups/
```

### 4.2 Strip de frontmatter KORA

OpenClaw no entiende el frontmatter `_manifest` de KORA. Hay que stripearlo al copiar:

```bash
strip_frontmatter() {
    local src="$1" dst="$2"
    python3 -c "
content = open('$src').read()
if content.startswith('---'):
    parts = content.split('---', 2)
    if len(parts) >= 3:
        open('$dst', 'w').write(parts[2].lstrip('\n'))
        return
open('$dst', 'w').write(content)
"
}

# Uso:
SRC=/home/felix/projects/kora/AGENTS/korvo/korax
DST=/srv/kora/workspaces/personal/agents/korax

for file in AGENTS.md SOUL.md TOOLS.md USER.md IDENTITY.md; do
    strip_frontmatter "$SRC/$file" "$DST/$file"
done

for skill in "$SRC"/skills/CM-*.md; do
    strip_frontmatter "$skill" "$DST/skills/$(basename $skill)"
done
```

### 4.3 Sync de Knowledge Base

Las KBs se copian (tambien sin frontmatter) como archivos de referencia que el agente puede leer bajo demanda via filesystem:

```bash
strip_frontmatter \
    /home/felix/projects/kora/KNOWLEDGE/korvo/manual-de-vida.md \
    /srv/kora/knowledge/korvo/manual-de-vida.md
```

**No van en el bootstrap** (serian 85K chars extra que explotarian la ventana). Van como archivos montados que el agente lee cuando los necesita.

### 4.4 Permisos

OpenClaw corre como uid 1000 (usuario `node`) dentro del container:

```bash
sudo chown -R 1000:1000 /srv/kora/workspaces/personal/agents/korax
chmod 600 /srv/kora/compose/.env
```

---

## 5. Build de imagenes Docker

### 5.1 Imagen base OpenClaw

Si tienes el source de OpenClaw:

```bash
cd /home/felix/projects/openclaw
docker build -t openclaw-local:latest .
```

### 5.2 Imagen del gateway

Si el agente no necesita nada extra (caso ideal con sidecar HTTP):

```bash
echo 'FROM openclaw-local:latest
ENV PCA_API=http://kora-pca:8100/api' | docker build -t kora-personal:latest -f - .
```

La imagen OpenClaw queda intacta. Solo se agrega un ENV para que el agente sepa donde esta el sidecar.

### 5.3 Imagen del sidecar

```bash
cd /home/felix/projects/pca
docker build -t kora-pca:latest -f /tmp/Dockerfile.pca .
```

---

## 6. Configuracion interactiva

Estos pasos requieren interaccion humana.

### 6.1 Crear bot de Telegram

1. Abrir Telegram, buscar **@BotFather**
2. Enviar `/newbot`
3. Elegir nombre y username
4. Copiar el token (formato: `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`)

### 6.2 Obtener tu Telegram user ID

1. Buscar **@userinfobot** en Telegram
2. Enviar cualquier mensaje
3. Copiar el numero (formato: `8734062810`)
4. Pegar en `openclaw.json5` → `channels.telegram.allowFrom`

### 6.3 Configurar autenticacion Anthropic

Para Claude Max (OAuth):

```bash
cd /srv/kora/compose
docker compose run --rm kora-personal openclaw models auth setup-token --provider anthropic
```

Sigue las instrucciones en pantalla para autorizar el acceso.

### 6.4 Rellenar .env

```bash
nano /srv/kora/compose/.env
# TELEGRAM_BOT_TOKEN=<token de paso 6.1>
# OPENCLAW_AUTH_TOKEN=<ya generado con openssl rand -hex 32>
```

### 6.5 Inicializar el volume del gateway

El named volume se crea como root. OpenClaw necesita que sea owned por uid 1000 (node). Ademas, hay que copiar el config al volume (no se puede bind-mountear — ver nota en seccion 3.4b).

```bash
cd /srv/kora/compose

# Paso 1: Pre-seed directorios con ownership correcta
docker compose run --rm --user root --no-deps --entrypoint sh kora-personal -c "
mkdir -p /home/node/.openclaw/agents/<agent>/sessions \
         /home/node/.openclaw/identity \
         /home/node/.openclaw/credentials \
         /home/node/.openclaw/logs &&
find /home/node/.openclaw -not -name openclaw.json -exec chown node:node {} + 2>/dev/null
chmod 700 /home/node/.openclaw
"

# Paso 2: Copiar config al volume
docker compose run --rm --user root --no-deps --entrypoint sh kora-personal -c "
cp /dev/stdin /home/node/.openclaw/openclaw.json &&
chown node:node /home/node/.openclaw/openclaw.json &&
chmod 600 /home/node/.openclaw/openclaw.json
" < ../config/personal/openclaw.json5
```

### 6.6 Validar config con doctor

```bash
docker compose run --rm kora-personal openclaw doctor
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
docker compose run --rm --user root --no-deps --entrypoint sh kora-personal -c \
  "cp /dev/stdin /home/node/.openclaw/openclaw.json && chown node:node /home/node/.openclaw/openclaw.json" \
  < ../config/personal/openclaw.json5
docker compose restart kora-personal
```

---

## 7. Deploy

```bash
cd /srv/kora/compose
docker compose up -d
```

Verificar:

```bash
# Estado de containers
docker compose ps

# Logs del gateway
docker compose logs -f kora-personal

# Logs del sidecar
docker compose logs -f kora-pca

# Health del sidecar
docker compose exec kora-pca python3 -c \
    "from urllib.request import urlopen; import json; print(json.dumps(json.loads(urlopen('http://localhost:8100/health').read()), indent=2))"
```

### 7.1 Pair de Telegram

1. Enviar cualquier DM al bot en Telegram
2. En el server:

```bash
docker compose exec kora-personal openclaw pairing list telegram
docker compose exec kora-personal openclaw pairing approve telegram <CODE>
```

### 7.2 Verificacion end-to-end

Enviar por Telegram:

```
/captura Probar que el agente funciona end-to-end via Telegram
```

Si el agente responde con un ID de candidato y confirma la captura, la cadena completa funciona:

```
Telegram → OpenClaw gateway → agente (bootstrap) → curl PCA HTTP → SQLite → respuesta → Telegram
```

---

## 8. Operaciones post-deploy

### 8.1 Re-sync del workspace

Cuando cambies el agente en el repo KORA:

```bash
cd /home/felix/projects/kora && git pull --ff-only
# Repetir strip_frontmatter para cada archivo cambiado
# Restart del gateway:
docker compose -f /srv/kora/compose/docker-compose.yml restart kora-personal
```

### 8.2 Backup de datos

```bash
# PCA DB
docker cp kora-pca:/app/data/pca.db /srv/kora/backups/pca-$(date +%Y%m%d).db

# Sesiones OpenClaw
docker cp kora-personal:/home/node/.openclaw/agents /srv/kora/backups/agents-$(date +%Y%m%d)
```

### 8.3 Monitoreo

```bash
# Estado del sistema PCA
docker compose exec kora-pca python3 -c \
    "from urllib.request import urlopen; import json; print(json.dumps(json.loads(urlopen('http://localhost:8100/api/estado').read()), indent=2))"

# Senales activas
docker compose exec kora-pca python3 -c \
    "from urllib.request import urlopen; import json; print(json.dumps(json.loads(urlopen('http://localhost:8100/api/signals').read()), indent=2))"
```

### 8.4 Troubleshooting

| Problema | Diagnostico | Solucion |
|----------|------------|----------|
| Gateway no arranca | `docker compose logs kora-personal` | Revisar syntax de openclaw.json5 |
| Sidecar unhealthy | `docker compose logs kora-pca` | Verificar puerto 8100 libre en red interna |
| Telegram no responde | Verificar `.env` tiene TELEGRAM_BOT_TOKEN | Verificar allowFrom tiene tu user ID numerico |
| "model not available" | `docker compose logs kora-personal \| grep auth` | Re-ejecutar setup-token |
| Respuestas truncadas | AGENTS.md > 20K chars | Comprimir bootstrap |
| PCA retorna 422 | Violacion de regla de integridad | Normal — el agente debe manejar el error |
| Container en restart loop | `docker compose logs --tail 50` | Verificar limites de memoria en compose |

---

## 9. Generalizacion: cualquier agente KORA

El proceso es identico para cualquier agente del ecosistema. Lo que cambia:

1. **Path del workspace:** `AGENTS/<namespace>/<agent>/`
2. **Servicios externos:** No todos los agentes necesitan sidecar. Si el agente es puramente conversacional (sin persistencia externa), no necesita sidecar ni Dockerfile custom
3. **allowed_kb:** Las KBs que necesita el agente (de `config.json`)
4. **Canal:** Puede ser Discord, HTTP webhook, u otro en vez de Telegram
5. **Modelo:** Puede ser otro provider (OpenAI, Gemini, etc.) con su propia auth

Lo que NO cambia:

- Strip de frontmatter KORA → workspace OpenClaw
- Estructura de directorios en `/srv/kora/`
- docker-compose con red kora-federation
- Flujo de provision → build → config → deploy → pair

---

## 10. Gotchas descubiertos en produccion

Lecciones del deploy real de korax v3.4.0 (2026-03-19). Cada una costo tiempo de troubleshooting.

### 10.1 Bind mount de archivo individual → EBUSY

**Sintoma:** `Error: EBUSY: resource busy or locked, rename '...openclaw.json.tmp' -> '...openclaw.json'`

**Causa:** OpenClaw usa escritura atomica (write-to-tmp + rename) para no corromper el config. Un bind mount de un archivo individual (`openclaw.json5:/home/node/.openclaw/openclaw.json`) no permite rename sobre el mount point.

**Fix:** Usar named volume para todo `/home/node/.openclaw/` y copiar el config al volume en un paso de init (seccion 6.5). Los bind mounts de **directorios** (workspace, knowledge) funcionan sin problema.

### 10.2 Schema de OpenClaw cambia entre versiones

**Sintoma:** `Config invalid` con mensajes como `identity was moved`, `Invalid input`.

**Causa:** OpenClaw 2026.2.27 movio `identity` de top-level a `agents.list[].identity`. Tambien cambio los valores validos de `session.reset.mode` y `gateway.bind`.

**Fix:** Siempre validar con `openclaw doctor` antes de `up`. Si hay migraciones pendientes, `openclaw doctor --fix` las aplica automaticamente. Mantener los templates de este tutorial actualizados con la version de OpenClaw en uso.

### 10.3 Named volume ownership = root

**Sintoma:** `Error: EACCES: permission denied, mkdir '/home/node/.openclaw/identity'`

**Causa:** Docker crea named volumes como root. OpenClaw corre como uid 1000 (node) y no puede escribir.

**Fix:** Pre-seed el volume con un container efimero `--user root` que crea los directorios y fija ownership (seccion 6.5). Esto se hace una sola vez.

### 10.4 Memory limit insuficiente para doctor

**Sintoma:** `FATAL ERROR: Reached heap limit Allocation failed - JavaScript heap out of memory` al correr `openclaw doctor`.

**Causa:** El memory limit de 1G no alcanza para skills discovery + plugin loading. La imagen OpenClaw tiene `NODE_OPTIONS=--max-old-space-size=2048` pero el cgroup limit del container lo mata antes.

**Fix:** Memory limit minimo de 2G para el gateway. Con 62Gi de RAM en el host, no es restriccion.

### 10.5 config.json de KORA tiene paths locales

**Sintoma:** `config.json` del workspace referencia paths macOS (`/Users/...`) que no existen en el server.

**Causa:** `config.json` es metadata de gobernanza KORA, no config de OpenClaw. Pero si se copia al workspace, el agente podria intentar usar esos paths.

**Fix:** Actualizar `config.json` del workspace (no del repo) para reflejar el binding HTTP:

```json
"pca": {
  "api_base": "http://kora-pca:8100/api",
  "mode": "http",
  "rationale": "En deploy Docker, PCA es sidecar HTTP. CLI path no aplica."
}
```

### 10.6 Telegram bot — verificar allowFrom es integer

**Sintoma:** Bot no responde a DMs aunque el token y user ID son correctos.

**Causa:** `allowFrom: ["7192195698"]` (string) no matchea contra el user ID numerico que Telegram envia como integer.

**Fix:** `allowFrom: [7192195698]` — sin comillas. JSON5 acepta trailing commas pero no perdona tipos incorrectos en runtime.

### 10.7 Healthcheck path depende de controlUi.basePath

**Sintoma:** Container queda `unhealthy` permanentemente aunque el gateway funciona y Telegram responde.

**Causa:** Si `controlUi.basePath` es `"/openclaw"`, el health endpoint se sirve en `/openclaw/health`, no en `/health`. Un healthcheck que apunta a `/health` recibe 404.

**Fix:** El healthcheck debe usar el basePath configurado:

```yaml
# Si basePath: "/openclaw"
healthcheck:
  test: ["CMD", "node", "-e", "fetch('http://localhost:PORT/openclaw/health').then(...)"]
```

### 10.8 context1m no funciona con OAuth token auth

**Sintoma:** Log warning: `ignoring context1m for OAuth token auth on anthropic/claude-opus-4-6; Anthropic rejects context-1m beta with OAuth auth`

**Causa:** El parametro `context1m: true` activa el beta de 1M tokens de Anthropic, pero este no es compatible con tokens OAuth (setup-token de Claude Max). Solo funciona con API keys directas (`sk-ant-api03-...`).

**Fix:** Remover `context1m: true` de los params del modelo si se usa OAuth. El contexto efectivo con OAuth es el default del modelo (~200K).

### 10.9 Multi-gateway: port spacing minimo 20

**Sintoma:** Conflictos potenciales de puerto entre gateways si se colocan en puertos consecutivos.

**Causa:** OpenClaw deriva puertos adicionales del base: browser control = base+2, CDP = base+9..+108. Dos gateways en 18789 y 18790 tendrian browser control en 18791 y 18792 — funciona, pero CDP podria colisionar.

**Fix:** Espaciar puertos base al menos 20. Ejemplo: korax=18789, steipete=18810, siguiente=18830.

---

## Apendice: Caso real — korax v3.4.0

### Metricas del deploy

| Metrica | Valor |
|---------|-------|
| Bootstrap total (sin frontmatter) | 34,886 chars (limit 150K) |
| Archivo mayor (AGENTS.md) | 16,378 chars (limit 20K) |
| Skills lazy-load | 12 (30,585 chars total) |
| KB montada | 84,258 chars (2 archivos, read-only) |
| Endpoints PCA HTTP | 22 (8 GET + 14 POST) |
| Dependencias PCA | 0 (stdlib puro) |
| Containers | 2 (gateway 2G/2cpu + sidecar 128M/0.5cpu) |
| Imagenes Docker | openclaw-local 4.4GB + kora-personal ~0B (thin layer) + kora-pca 181MB |
| Tiempo total deploy | ~2 horas (incluye troubleshooting de gotchas) |

### Optimizaciones aplicadas

1. **AGENTS.md:** 19,280 → 16,352 chars (-15%). Removida seccion coalgebraica (notacion formal que no afecta operacion), notas categoricas sobre fibraciones, tablas de sub-campos compactadas a una linea
2. **PCA como sidecar:** Imagen OpenClaw intacta, upgrades sin rebuild custom
3. **KB como archivos montados:** 85K chars que no entran en bootstrap van como referencia filesystem read-only
4. **Cache long:** Bootstrap de ~35K chars se cachea ~1h, reduciendo costo por turno

### Correciones aplicadas durante deploy

1. **openclaw.json5:** `identity` movido a `agents.list[0].identity`, `session.reset.mode` eliminado, `gateway.bind` cambiado de `"0.0.0.0"` a `"loopback"`, `memorySearch.enabled: false` agregado
2. **docker-compose.yml:** `init: true` agregado, config bind mount reemplazado por named volume + copy, memory limit subido de 1G a 2G, `environment: HOME, TERM` agregados
3. **config.json workspace:** paths macOS reemplazados por binding HTTP (`api_base: "http://kora-pca:8100/api"`)
4. **Volume init:** paso de pre-seed agregado (chown node:node, mkdir de subdirs requeridos)

### Validacion pre-deploy

```
41/41 workspaces KORA validos
0 URNs rotas
728 artefactos indexados
PCA HTTP: 22 endpoints testados e2e
Compose YAML: syntax valida
openclaw doctor: 0 errores de config
```

### Secuencia real de verificacion post-deploy

```
$ docker compose ps
kora-pca        kora-pca:latest        Up (healthy)     8100/tcp
kora-personal   kora-personal:latest   Up (healthy)     127.0.0.1:18789->18789/tcp

$ docker compose logs kora-personal --tail 5
[gateway]    agent model: anthropic/claude-opus-4-6
[gateway]    listening on ws://127.0.0.1:18789
[telegram]   [default] starting provider (@korax_kv_bot)

$ # Test end-to-end via Telegram:
$ # /captura Probar que korax funciona end-to-end via Telegram
$ # → "📥 Capturado → C-20260319013342918302"
```
