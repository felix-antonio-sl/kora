---
_manifest:
  urn: urn:ops:kb:deploy-agente-kora-en-openclaw-p03
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
    shard_index: 3
    shard_count: 4
    shard_root_urn: urn:ops:kb:deploy-agente-kora-en-openclaw
relations:
  cites:
  - urn:ops:kb:arquitectura-stack-kora
  - urn:ops:kb:federacion-kora-v2
---


# Tutorial: Desplegar un agente KORA en OpenClaw - Parte 03

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

**Fix:** Espaciar puertos base al menos 20. Ejemplo: korax=18789, steipete=18810, salubrista=18830, siguiente=18850. Ver `urn:ops:kb:arquitectura-stack-kora` para el inventario completo.

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

1. **openclaw.json5:** `identity` movido a `agents.list[0].identity`, `session.reset.mode` eliminado, `gateway.bind` cambiado de `"0.0.0.0"` a `"loopback"` (posteriormente actualizado a `"lan"` para federation cross-gateway — ver §11.1), `memorySearch.enabled: false` agregado
2. **docker-compose.yml:** `init: true` agregado, config bind mount reemplazado por named volume + copy, memory limit subido de 1G a 2G, `environment: HOME, TERM` agregados
3. **Volume init:** paso de pre-seed agregado (chown node:node, mkdir de subdirs requeridos)

### Verificacion post-deploy

```
$ docker compose ps
kora-pca kora-pca:latest Up (healthy) 8100/tcp
kora-personal kora-personal:latest Up (healthy) 127.0.0.1:18789->18789/tcp

$ docker compose logs kora-personal --tail 5
[gateway] agent model: anthropic/claude-opus-4-6
[gateway] listening on ws://127.0.0.1:18789
[telegram] [default] starting provider (@korax_kv_bot)

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
 bind: "lan", // CRITICO: "loopback" impide que otros containers alcancen este gateway
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
