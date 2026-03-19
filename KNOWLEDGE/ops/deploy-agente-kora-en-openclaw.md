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
    env_file: .env
    ports:
      - "127.0.0.1:18789:18789"
    volumes:
      - ../config/<gateway>/openclaw.json5:/home/node/.openclaw/openclaw.json:ro
      - ../workspaces/<gateway>/agents/<agent>:/home/node/.openclaw/workspace
      - ../knowledge:/home/node/knowledge:ro
      - agent-data:/home/node/.openclaw/agents
    networks:
      - kora-federation
    depends_on:
      sidecar:
        condition: service_healthy

  sidecar:
    image: kora-sidecar:latest
    container_name: kora-sidecar
    restart: unless-stopped
    volumes:
      - sidecar-data:/app/data
    networks:
      - kora-federation

networks:
  kora-federation:
    driver: bridge

volumes:
  agent-data:
  sidecar-data:
```

**c) openclaw.json5:**

```json5
{
  identity: {
    name: "<NombreAgente>",
    theme: "<descripcion>",
    emoji: "<emoji>",
  },
  agents: {
    defaults: {
      workspace: "/home/node/.openclaw/workspace",
      model: {
        primary: "anthropic/claude-opus-4-6",
      },
      models: {
        "anthropic/claude-opus-4-6": {
          params: {
            context1m: true,         // 1M tokens de contexto
            cacheRetention: "long",  // cache de bootstrap ~1h
          },
        },
      },
    },
  },
  session: {
    scope: "per-sender",
    reset: { mode: "manual" },
  },
  gateway: {
    mode: "local",
    port: 18789,
    bind: "0.0.0.0",
    controlUi: { enabled: true, basePath: "/openclaw" },
    auth: { mode: "token" },
  },
  channels: {
    telegram: {
      enabled: true,
      dmPolicy: "allowlist",
      allowFrom: ["<TELEGRAM_USER_ID>"],  // numerico, de @userinfobot
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

## Apendice: Caso real — korax v3.4.0

### Metricas del deploy

| Metrica | Valor |
|---------|-------|
| Bootstrap total (sin frontmatter) | 34,886 chars (limit 150K) |
| Archivo mayor (AGENTS.md) | 16,352 chars (limit 20K) |
| Skills lazy-load | 12 (31,718 chars total) |
| KB montada | 85,170 chars (2 archivos, read-only) |
| Endpoints PCA HTTP | 22 (8 GET + 14 POST) |
| Dependencias PCA | 0 (stdlib puro) |
| Containers | 2 (gateway 1G/2cpu + sidecar 128M/0.5cpu) |
| Tiempo bootstrap → deploy | ~3 horas (incluye preparacion local) |

### Optimizaciones aplicadas

1. **AGENTS.md:** 19,280 → 16,352 chars (-15%). Removida seccion coalgebraica (notacion formal que no afecta operacion), notas categoricas sobre fibraciones, tablas de sub-campos compactadas a una linea
2. **PCA como sidecar:** Imagen OpenClaw intacta, upgrades sin rebuild custom
3. **KB como archivos montados:** 85K chars que no entran en bootstrap van como referencia filesystem read-only
4. **Cache long:** Bootstrap de ~35K chars se cachea ~1h, reduciendo costo por turno

### Validacion pre-deploy

```
41/41 workspaces KORA validos
0 URNs rotas
728 artefactos indexados
PCA HTTP: 22 endpoints testados e2e
Compose YAML: syntax valida
Preflight: 17/17 checks passed
```
