---
_manifest:
  urn: "urn:ops:kb:deploy-agente-kora-en-openclaw"
  provenance:
    created_by: "ops/clawstack"
    created_at: "2026-03-19"
    updated_at: "2026-03-23"
    source: "Experiencia operacional desplegando korax v3.4.0, steipete v1.5.1 y salubrista-hah v1.0.0 en Hetzner sobre OpenClaw v2026.3.22"
version: "1.2.0"
status: published
tags: [deploy, openclaw, docker, tutorial, operaciones, transmutacion, federation, hooks, ux]
lang: es
---

# Tutorial: Desplegar un agente KORA en OpenClaw

Proceso completo para transmutar un agente del ecosistema KORA a un gateway OpenClaw corriendo en Docker sobre un servidor remoto. Generalizable a cualquier agente KORA — con o sin servicios externos.

El apendice documenta el caso real de korax v3.4.0 con PCA sidecar en Hetzner.

---

## 1. Entender las dos capas

Un agente KORA vive en el repositorio como un **workspace** — un directorio con archivos markdown que definen su comportamiento, personalidad, herramientas y skills. OpenClaw es el **runtime** que encarna ese workspace: le da un gateway HTTP, canales de comunicacion (Telegram, Discord, WhatsApp), persistencia de sesion, y acceso a modelos LLM.

```
KORA (especificacion)              OpenClaw (runtime)
─────────────────────              ──────────────────
AGENTS/<ns>/<agent>/               ~/.openclaw/workspace/
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
| **AGENTS.md** | Comportamiento formal (FSM, transiciones, invariantes, reglas) | Inyectado en cada turno (main + sub-agentes) | Define QUE hace el agente y COMO opera |
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

No todos los agentes KORA necesitan servicios externos. La decision depende de lo que declara `TOOLS.md`:

### Caso A: Agente puramente conversacional (sin sidecar)

Si el agente solo usa conversacion y tools nativos de OpenClaw (filesystem, code_execution, web), no necesita sidecar. Ejemplos: agentes consultivos, asesores, analistas.

```
┌─────────────────┐
│  OpenClaw        │
│  (imagen intacta)│
└─────────────────┘
```

Un solo container. Sin Dockerfile custom. Sin compose `depends_on`. La configuracion mas simple posible.

### Caso B: Agente con servicio externo (sidecar HTTP)

Si el agente invoca un servicio con estado propio (base de datos, API, daemon), ese servicio corre como sidecar en su propio container.

```
┌─────────────────┐    ┌──────────────┐
│  OpenClaw        │───▶│  Servicio     │
│  (imagen intacta)│HTTP│  (container)  │
└─────────────────┘    └──────────────┘
```

**Por que sidecar y no dentro del container:** Mezclar runtimes (Node.js + Python, por ejemplo) en un solo container requiere Dockerfile custom que se rompe en cada upgrade de OpenClaw. El sidecar mantiene la imagen OpenClaw intacta — upgrades son `docker pull` limpios.

### 2.1 Escribir el wrapper HTTP (solo caso B)

Si el servicio tiene una API limpia (funciones que reciben parametros y devuelven datos), el wrapper HTTP es mecanico. Usar solo stdlib para cero dependencias externas:

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
            self._respond(service.estado())
        # ... mapear cada endpoint de lectura

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        if self.path == "/api/accion":
            result = service.accion(body["param"])
            self._respond(result)
        # ... mapear cada endpoint de escritura

    def _respond(self, data, code=200):
        body = json.dumps(data, ensure_ascii=False, default=str).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
```

### 2.2 Actualizar los bindings en TOOLS.md

Los bindings del agente deben reflejar el protocolo real del deploy. Si el agente usaba CLI local:

```
- **Binding:** `python3 $CLI comando "<arg>"`
```

Cambiar a HTTP sidecar:

```
- **Binding:** `POST $API/comando` body: `{"arg": "<valor>"}`
```

El agente usara `curl` via code_execution para invocar el sidecar. `curl` esta disponible en la imagen base de OpenClaw.

---

## 3. Preparar el paquete de deploy (local)

Antes de tocar el servidor, preparar todo localmente. R5: observe before act.

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

### 3.2 Auditar tamanos de bootstrap

```bash
for f in AGENTS/<ns>/<agent>/*.md; do
    chars=$(wc -c < "$f")
    echo "$(basename $f): $chars chars"
done
```

Si algun archivo excede 17K, comprimir. Si el total excede 100K, evaluar mover contenido a skills lazy-load.

### 3.3 Verificar dependencias del servicio externo (solo caso B)

```bash
# Ejemplo para servicio Python: verificar que es stdlib puro
python3 -c "
import ast, sys
from pathlib import Path
stdlib = set(sys.stdlib_module_names)
external = set()
for f in Path('src').rglob('*.py'):
    for node in ast.walk(ast.parse(f.read_text())):
        if isinstance(node, ast.Import):
            for a in node.names:
                m = a.name.split('.')[0]
                if m not in stdlib and m not in {'mi_paquete'}:
                    external.add(m)
        elif isinstance(node, ast.ImportFrom) and node.module:
            m = node.module.split('.')[0]
            if m not in stdlib and m not in {'mi_paquete'}:
                external.add(m)
print(f'Externas: {external}' if external else 'CLEAN: stdlib puro')
"
```

Si tiene dependencias externas, agregarlas al Dockerfile del sidecar con `pip install`.

### 3.4 Escribir los archivos de deploy

#### a) Dockerfile del sidecar (solo caso B)

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

#### b) docker-compose.yml

**Caso A — agente sin sidecar:**

```yaml
services:
  gateway:
    image: openclaw-local:latest
    container_name: kora-<nombre>
    restart: unless-stopped
    init: true                          # CRITICO: PID 1 signal handling
    env_file: .env
    environment:
      HOME: /home/node
      TERM: xterm-256color
    ports:
      - "127.0.0.1:<puerto>:<puerto>"
    volumes:
      - agent-data:/home/node/.openclaw
      - ../workspaces/<gateway>/agents/<agent>:/home/node/.openclaw/workspace
      - ../knowledge:/home/node/knowledge:ro
    networks:
      - kora-federation
    deploy:
      resources:
        limits:
          memory: 2G                    # Minimo 2G para skills discovery
          cpus: "2.0"
    healthcheck:
      test: ["CMD", "node", "-e", "fetch('http://localhost:<puerto>/openclaw/health').then(r=>{if(!r.ok)process.exit(1)}).catch(()=>process.exit(1))"]
      # NOTA: el path /openclaw/health depende de controlUi.basePath (ver §10.7)
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 15s
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"

networks:
  kora-federation:
    driver: bridge
    name: kora-federation

volumes:
  agent-data:
```

**Caso B — agente con sidecar:** agregar el service sidecar y `depends_on`:

```yaml
services:
  gateway:
    # ... igual que caso A, mas:
    depends_on:
      sidecar:
        condition: service_healthy

  sidecar:
    image: kora-<servicio>:latest
    container_name: kora-<servicio>
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

volumes:
  agent-data:
  sidecar-data:
```

> **Por que NO se bind-mountea el config directamente:** OpenClaw escribe su config via atomic rename (write-to-tmp + rename). Un bind mount de archivo individual causa `EBUSY` porque el filesystem del host no permite rename sobre el mount point. La solucion es usar un named volume para todo `/home/node/.openclaw/` y copiar el config al volume en un paso de init (ver seccion 6.4). Los bind mounts de **directorios** (workspace, knowledge) funcionan sin problema.

#### c) openclaw.json5

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

#### d) .env

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
│   └── <namespace>/            (solo KBs que el agente necesita, per allowed_kb)
├── comms/                      (buzones inter-cuadrilla, futuro)
├── scripts/
└── backups/
```

```bash
# Crear estructura (reemplazar <gateway> y <agent>)
sudo mkdir -p /srv/kora/{compose,config/<gateway>,scripts,backups,comms}
sudo mkdir -p /srv/kora/workspaces/<gateway>/agents/<agent>/{skills,memory}
sudo mkdir -p /srv/kora/knowledge/<namespace>
sudo chown -R $(whoami):$(whoami) /srv/kora
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

# Reemplazar paths con los de tu agente:
KORA_REPO=/home/felix/projects/kora
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
# Ejemplo: urn:korvo:kb:manual-de-vida → KNOWLEDGE/korvo/manual-de-vida.md
strip_frontmatter \
    $KORA_REPO/KNOWLEDGE/<namespace>/<archivo>.md \
    /srv/kora/knowledge/<namespace>/<archivo>.md
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
docker compose logs -f gateway

# Logs del sidecar (caso B)
docker compose logs -f sidecar
```

### 7.1 Pair de Telegram

1. Enviar cualquier DM al bot en Telegram
2. En el server:

```bash
docker compose exec gateway openclaw pairing list telegram
docker compose exec gateway openclaw pairing approve telegram <CODE>
```

### 7.2 Verificacion end-to-end

Enviar cualquier mensaje al bot por Telegram. Si el agente responde coherentemente con su personalidad (SOUL.md) y comportamiento (AGENTS.md), la cadena completa funciona:

```
Telegram → OpenClaw gateway → agente (bootstrap) → respuesta → Telegram
```

Si el agente tiene sidecar, verificar que tambien accede al servicio externo (la respuesta debe incluir datos del sidecar, no solo texto conversacional).

---

## 8. Operaciones post-deploy

### 8.1 Re-sync del workspace

Cuando cambies el agente en el repo KORA:

```bash
cd /home/felix/projects/kora && git pull --ff-only

# Re-strip bootstrap files (§4.2)
SRC=$KORA_REPO/AGENTS/<namespace>/<agent>
DST=/srv/kora/workspaces/<gateway>/agents/<agent>
for file in AGENTS.md SOUL.md TOOLS.md USER.md IDENTITY.md; do
    [ -f "$SRC/$file" ] && strip_frontmatter "$SRC/$file" "$DST/$file"
done
for skill in "$SRC"/skills/CM-*.md; do
    [ -f "$skill" ] && strip_frontmatter "$skill" "$DST/skills/$(basename $skill)"
done

# Si cambio openclaw.json5, tambien re-sync al volume (§6.7)

# Restart
docker compose -f /srv/kora/compose/docker-compose.yml restart gateway
```

### 8.2 Backup de datos

```bash
# Sesiones OpenClaw
docker cp kora-<nombre>:/home/node/.openclaw/agents /srv/kora/backups/agents-$(date +%Y%m%d)

# Sidecar data (caso B)
docker cp kora-<servicio>:/app/data /srv/kora/backups/<servicio>-$(date +%Y%m%d)
```

### 8.3 Troubleshooting

| Problema | Diagnostico | Solucion |
|----------|------------|----------|
| Gateway no arranca | `docker compose logs gateway` | Revisar syntax de openclaw.json5 con `openclaw doctor` |
| Sidecar unhealthy | `docker compose logs sidecar` | Verificar puerto libre en red kora-federation |
| Telegram no responde | Verificar `.env` y `allowFrom` | allowFrom debe ser integer, no string |
| "model not available" | Logs del gateway, grep `auth` | Re-ejecutar setup-token (§6.5) |
| Respuestas truncadas | AGENTS.md > 20K chars | Comprimir bootstrap (§1.2) |
| Sidecar retorna 422 | Violacion de regla del servicio | Normal — el agente debe manejar el error |
| Container en restart loop | `docker compose logs --tail 50` | Verificar limites de memoria (minimo 2G gateway) |
| `EBUSY` al arrancar | Bind mount de archivo individual | Usar named volume + copy (§6.4) |
| `EACCES` permission denied | Volume owned by root | Pre-seed con `--user root` (§6.4) |
| `Config invalid` | Schema mismatch con version OpenClaw | `openclaw doctor --fix` para migrar (§10.2) |

---

## 9. Generalizacion: cualquier agente KORA

### Lo que cambia por agente

| Variable | Donde se define | Ejemplo |
|----------|----------------|---------|
| Path del workspace | `AGENTS/<namespace>/<agent>/` | `AGENTS/korvo/korax/` |
| Servicios externos | `TOOLS.md` bindings | PCA HTTP, API externa, DB |
| KBs requeridas | `config.json → allowed_kb` | `manual-de-vida.md` |
| Canal de entrada | Requisito operacional | Telegram, Discord, WhatsApp, HTTP |
| Modelo LLM | Requisito de capacidad | Opus 4.6, Sonnet 4.5, GPT-4o |
| Puerto gateway | Compose | 18789, 18790, ... |

### Lo que NO cambia

- Strip de frontmatter KORA → workspace OpenClaw
- Estructura de directorios en `/srv/kora/`
- Named volume para `/home/node/.openclaw/` (nunca bind mount de archivo)
- Pre-seed de volume con `--user root`
- `init: true` en compose
- `openclaw doctor` antes de `up`
- Red kora-federation para comunicacion inter-cuadrilla
- Flujo: provision → build → config → doctor → deploy → pair

### Arbol de decision rapido

```
¿El agente tiene TOOLS.md con bindings a servicios externos?
├── NO → Caso A: 1 container, imagen openclaw-local directa
└── SI → ¿El servicio tiene API limpia (funciones → datos)?
    ├── SI → Caso B: wrapper HTTP + sidecar container
    └── NO → Evaluar: adaptar API, o montar como volume con runtime extra
```

---

## 10. Gotchas descubiertos en produccion

Lecciones del deploy real de korax v3.4.0 (2026-03-19). Cada una costo tiempo de troubleshooting.

### 10.1 Bind mount de archivo individual → EBUSY

**Sintoma:** `Error: EBUSY: resource busy or locked, rename '...openclaw.json.tmp' -> '...openclaw.json'`

**Causa:** OpenClaw usa escritura atomica (write-to-tmp + rename) para no corromper el config. Un bind mount de un archivo individual (`openclaw.json5:/home/node/.openclaw/openclaw.json`) no permite rename sobre el mount point.

**Fix:** Usar named volume para todo `/home/node/.openclaw/` y copiar el config al volume en un paso de init (§6.4). Los bind mounts de **directorios** (workspace, knowledge) funcionan sin problema.

### 10.2 Schema de OpenClaw cambia entre versiones

**Sintoma:** `Config invalid` con mensajes como `identity was moved`, `Invalid input`.

**Causa:** OpenClaw 2026.2.27 movio `identity` de top-level a `agents.list[].identity`. Tambien cambio los valores validos de `session.reset.mode` y `gateway.bind`.

**Fix:** Siempre validar con `openclaw doctor` antes de `up`. Si hay migraciones pendientes, `openclaw doctor --fix` las aplica automaticamente. Mantener los templates de este tutorial actualizados con la version de OpenClaw en uso.

### 10.3 Named volume ownership = root

**Sintoma:** `Error: EACCES: permission denied, mkdir '/home/node/.openclaw/identity'`

**Causa:** Docker crea named volumes como root. OpenClaw corre como uid 1000 (node) y no puede escribir.

**Fix:** Pre-seed el volume con un container efimero `--user root` que crea los directorios y fija ownership (§6.4). Esto se hace una sola vez.

### 10.4 Memory limit insuficiente para doctor

**Sintoma:** `FATAL ERROR: Reached heap limit Allocation failed - JavaScript heap out of memory` al correr `openclaw doctor`.

**Causa:** El memory limit de 1G no alcanza para skills discovery + plugin loading. La imagen OpenClaw tiene `NODE_OPTIONS=--max-old-space-size=2048` pero el cgroup limit del container lo mata antes.

**Fix:** Memory limit minimo de 2G para el gateway.

### 10.5 config.json de KORA tiene paths locales

**Sintoma:** `config.json` del workspace referencia paths de la maquina de desarrollo (`/Users/...`) que no existen en el server.

**Causa:** `config.json` es metadata de gobernanza KORA, no config de OpenClaw. No debe copiarse al workspace. Pero si accidentalmente se copia, el agente podria intentar usar esos paths.

**Fix:** No copiar `config.json` al workspace (el `strip_frontmatter` loop de §4.2 ya lo excluye). Si el agente necesita saber la URL del sidecar, eso va en un ENV del container, no en config.json.

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

### Contexto

korax es un exoesqueleto cognitivo de productividad y bienestar (namespace korvo). Usa PCA v4.1 como sistema de persistencia (Candidato, UT, Proyecto, Objetivo, Contribucion) con 22 endpoints HTTP. Desplegado en Hetzner i7-7700 / 62GB RAM / Ubuntu 24.04 / Docker 29.3.0.

### Metricas del deploy

| Metrica | Valor |
|---------|-------|
| Bootstrap total (sin frontmatter) | 34,886 chars (limit 150K) |
| Archivo mayor (AGENTS.md) | 16,378 chars (limit 20K) |
| Skills lazy-load | 12 (30,585 chars total) |
| KB montada | 84,258 chars (2 archivos, read-only) |
| Endpoints sidecar | 22 (8 GET + 14 POST) |
| Dependencias sidecar | 0 (stdlib puro) |
| Containers | 2 (gateway 2G/2cpu + sidecar 128M/0.5cpu) |
| Imagenes Docker | openclaw-local 4.4GB + kora-personal ~0B (thin layer) + kora-pca 181MB |
| Tiempo total deploy | ~2 horas (incluye troubleshooting de gotchas) |

### Optimizaciones aplicadas

1. **AGENTS.md:** 19,280 → 16,352 chars (-15%). Removida seccion coalgebraica (notacion formal que no afecta operacion), notas categoricas sobre fibraciones, tablas de sub-campos compactadas a una linea
2. **PCA como sidecar:** Imagen OpenClaw intacta, upgrades sin rebuild custom
3. **KB como archivos montados:** 85K chars que no entran en bootstrap van como referencia filesystem read-only
4. **Cache long:** Bootstrap de ~35K chars se cachea ~1h, reduciendo costo por turno

### Correcciones aplicadas durante deploy

1. **openclaw.json5:** `identity` movido a `agents.list[0].identity`, `session.reset.mode` eliminado, `gateway.bind` cambiado de `"0.0.0.0"` a `"loopback"`, `memorySearch.enabled: false` agregado
2. **docker-compose.yml:** `init: true` agregado, config bind mount reemplazado por named volume + copy, memory limit subido de 1G a 2G, `environment: HOME, TERM` agregados
3. **Volume init:** paso de pre-seed agregado (chown node:node, mkdir de subdirs requeridos)

### Verificacion post-deploy

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

---

## 11. Post-deploy: integrar a la federación

Si el agente debe comunicarse con otros agentes desplegados, agregar al stack de federation (ver `urn:ops:kb:federacion-kora-v2`):

### 11.1 Hooks cross-gateway

Agregar a `openclaw.json5`:

```json5
hooks: {
  enabled: true,
  token: "{token compartido con otros gateways}",
}
gateway: {
  bind: "lan",  // CRITICO: "loopback" impide que otros containers alcancen este gateway
}
```

### 11.2 Storage compartido

Crear directorio propio y montar en compose:

```bash
mkdir -p /srv/kora/shared/{agent-id}
```

Agregar al `docker-compose.yml`:

```yaml
volumes:
  - ../shared/federation:/home/node/shared/federation:ro
  - ../shared/{agent-id}:/home/node/shared/{agent-id}
```

### 11.3 Instrucciones de derivación

Agregar sección `## Federacion kora` al TOOLS.md del workspace con: tabla de agentes, hook URLs, token, protocolo de derivación, referencia a `directorio-agentes.md`.

### 11.4 Actualizar directorio

Editar `/srv/kora/shared/federation/directorio-agentes.md` con el nuevo agente (dominio, acepta, rechaza, gateway, bot).

### 11.5 Registrar en panel

Agregar al `registry.json` del panel web (`~/projects/kora-panel/`).

---

## 12. Config UX del canal

Aplicar config UX óptima para el canal (ver `urn:ops:kb:ux-telegram-openclaw` para Telegram):

```json5
channels: {
  telegram: {
    chunkMode: "length",
    markdown: { tables: "bullets" },
    replyToMode: "first",
    silentErrorReplies: true,
    textChunkLimit: 4000,
    linkPreview: false,
    reactionLevel: "minimal",
  },
}
```

---

## Agentes desplegados con este tutorial

| Agente | Versión | Puerto | Arquitectura | Fecha |
|---|---|---|---|---|
| korax | v3.4.0 | 18789 | Caso B (+ sidecar PCA) | 2026-03-19 |
| steipete | v1.5.1 | 18810 | Caso A (puro, workers via exec) | 2026-03-19 |
| salubrista-hah | v1.0.0 | 18830 | Caso A (puro, 13 KBs salud) | 2026-03-23 |
