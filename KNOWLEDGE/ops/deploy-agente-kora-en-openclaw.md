---
_manifest:
  urn: urn:ops:kb:deploy-agente-kora-en-openclaw
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
    shard_index: 1
    shard_count: 4
    shard_root_urn: urn:ops:kb:deploy-agente-kora-en-openclaw
---

# Tutorial: Desplegar un agente KORA en OpenClaw


Proceso completo para transmutar un agente del ecosistema KORA a un gateway OpenClaw corriendo en Docker sobre un servidor remoto. Generalizable a cualquier agente KORA — con o sin servicios externos.

El apendice documenta el caso real de korax v3.4.0 con PCA sidecar en Hetzner.

---

## 1. Entender las dos capas

Un agente KORA vive en el repositorio como un **workspace** — un directorio con archivos markdown que definen su comportamiento, personalidad, herramientas y skills. OpenClaw es el **runtime** que encarna ese workspace: le da un gateway HTTP, canales de comunicacion (Telegram, Discord, WhatsApp), persistencia de sesion, y acceso a modelos LLM.

```
KORA (especificacion) OpenClaw (runtime)
───────────────────── ──────────────────
AGENTS/<ns>/<agent>/ ~/.openclaw/workspace/
├── AGENTS.md ──strip──▶ ├── AGENTS.md
├── SOUL.md ──strip──▶ ├── SOUL.md
├── TOOLS.md ──strip──▶ ├── TOOLS.md
├── USER.md ──strip──▶ ├── USER.md
├── IDENTITY.md ──strip──▶ ├── IDENTITY.md
├── config.json (no se copia, es metadata KORA)
└── skills/ ──strip──▶ └── skills/
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
│ OpenClaw │
│ (imagen intacta)│
└─────────────────┘
```

Un solo container. Sin Dockerfile custom. Sin compose `depends_on`. La configuracion mas simple posible.

### Caso B: Agente con servicio externo (sidecar HTTP)

Si el agente invoca un servicio con estado propio (base de datos, API, daemon), ese servicio corre como sidecar en su propio container.

```
┌─────────────────┐ ┌──────────────┐
│ OpenClaw │───▶│ Servicio │
│ (imagen intacta)│HTTP│ (container) │
└─────────────────┘ └──────────────┘
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
 self._respond(service.estado)
 # ... mapear cada endpoint de lectura

 def do_POST(self):
 body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
 if self.path == "/api/accion":
 result = service.accion(body["param"])
 self._respond(result)
 # ... mapear cada endpoint de escritura

 def _respond(self, data, code=200):
 body = json.dumps(data, ensure_ascii=False, default=str).encode
 self.send_response(code)
 self.send_header("Content-Type", "application/json")
 self.send_header("Content-Length", str(len(body)))
 self.end_headers
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

## 3.1 Crear IDENTITY.md

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

## 3.2 Auditar tamanos de bootstrap

```bash
for f in AGENTS/<ns>/<agent>/*.md; do
 chars=$(wc -c < "$f")
 echo "$(basename $f): $chars chars"
done
```

Si algun archivo excede 17K, comprimir. Si el total excede 100K, evaluar mover contenido a skills lazy-load.

## 3.3 Verificar dependencias del servicio externo (solo caso B)

```bash
# Ejemplo para servicio Python: verificar que es stdlib puro
python3 -c "
import ast, sys
from pathlib import Path
stdlib = set(sys.stdlib_module_names)
external = set
for f in Path('src').rglob('*.py'):
 for node in ast.walk(ast.parse(f.read_text)):
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

## a) Dockerfile del sidecar (solo caso B)

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

## b) docker-compose.yml

**Caso A — agente sin sidecar:**

```yaml
services:
 gateway:
 image: openclaw-local:latest
 container_name: kora-<nombre>
 restart: unless-stopped
 init: true # CRITICO: PID 1 signal handling
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
 memory: 2G # Minimo 2G para skills discovery
 cpus: "2.0"
 healthcheck:
 test: ["CMD", "node", "-e", "fetch('http://localhost:<puerto>/openclaw/health').then(r=>{if(!r.ok)process.exit(1)}).catch(=>process.exit(1))"]
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
