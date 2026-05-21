---
_manifest:
  urn: urn:agengai:kb:openclaw-skills-manual-p02
  provenance:
    created_by: kora/curator
    created_at: '2026-03-26'
    source: 'KNOWLEDGE/agengai/openclaw/documentacion-oficial (tools/skills.md, tools/creating-skills.md,
      tools/skills-config.md, tools/clawhub.md, tools/slash-commands.md, cli/skills.md,
      platforms/mac/skills.md, tools/subagents.md, tools/exec-approvals.md, tools/loop-detection.md,
      tools/multi-agent-sandbox-tools.md, tools/elevated.md, gateway/sandboxing.md,
      gateway/secrets.md, gateway/security/index.md, security/THREAT-MODEL-ATLAS.md,
      concepts/agent.md, concepts/agent-workspace.md, concepts/system-prompt.md, plugins/building-plugins.md,
      plugins/manifest.md, help/testing.md; verificado contra mirror sync 2026-04-05
      commit 2a39141) + fuente web externa: agentskills.io (spec overview, specification,
      quickstart, best-practices, optimizing-descriptions, evaluating-skills, using-scripts,
      client-implementation)'
version: 2.2.0
status: publicado
tags:
- openclaw
- skills
- agentes-ia
- llm
- manual
- ciclo-de-vida
- seguridad
- orquestacion
- agentskills
- interoperabilidad
lang: es
extensions:
  agengai:
    family: note
    scope: Creacion, operacion y evolucion de skills en OpenClaw
    dimensions: 15
    related:
    - urn:agengai:kb:openclaw-manual-integral
  kora:
    shard_index: 2
    shard_count: 5
    shard_root_urn: urn:agengai:kb:openclaw-skills-manual
relations:
  cites:
  - urn:agengai:kb:openclaw-manual-integral
---

# Manual Integral de Skills en OpenClaw - Parte 02

## 4.1 Procedimiento de creacion

1. Crear directorio del skill:
 ```bash
 mkdir -p ~/.openclaw/workspace/skills/mi-skill
 ```
2. Escribir `SKILL.md` con frontmatter + instrucciones
3. (Opcional) Agregar `scripts/`, `references/`, `assets/` segun necesidad
4. (Opcional) Definir schemas de herramientas custom en frontmatter o usar herramientas existentes del sistema (`exec`, `browser`, etc.)
5. Cargar el skill iniciando nueva sesion:
 ```bash
 /new # desde chat
 openclaw gateway restart # o reiniciar gateway
 ```
6. Verificar carga:
 ```bash
 openclaw skills list
 ```
7. Probar con mensaje de prueba:
 ```bash
 openclaw agent --message "mensaje que active el skill"
 ```

## 4.2 Ubicaciones y precedencia

OpenClaw carga skills desde 6 raices nativas. Orden de precedencia en caso de conflicto de nombres (primera gana):

| Ubicacion | Precedencia | Alcance |
| --- | --- | --- |
| `<workspace>/skills/` | Maxima | Per-agent |
| `<workspace>/.agents/skills/` | Alta | Per-workspace agent (interoperable) |
| `~/.agents/skills/` | Media | Personal agent profile (interoperable) |
| `~/.openclaw/skills/` | Media | Compartido (todos los agentes) |
| Bundled (distribucion OpenClaw) | Baja | Global |
| `skills.load.extraDirs` | Minima | Carpetas compartidas custom |

Las rutas `.agents/skills/` son raices nativas de primera clase cargadas automaticamente por OpenClaw, no solo convenciones de interoperabilidad. Skills colocados ahi por otros clientes compatibles con el estandar AgentSkills (Claude Code, Cursor, Gemini CLI, etc.) son automaticamente visibles.

Convenciones adicionales de interoperabilidad:

| Scope | Ruta | Proposito |
| --- | --- | --- |
| Proyecto | `<proyecto>/.<tu-cliente>/skills/` | Ubicacion nativa de otro cliente |
| Usuario | `~/.<tu-cliente>/skills/` | Ubicacion nativa de otro cliente |

## 4.3 Skills per-agent vs compartidos

En setups multi-agente cada agente tiene su propio workspace:
- **Per-agent**: `<workspace>/skills/` — solo ese agente
- **Per-workspace agent**: `<workspace>/.agents/skills/` — compartido entre clientes del workspace
- **Personal agent**: `~/.agents/skills/` — compartido cross-workspace en la maquina
- **Compartidos**: `~/.openclaw/skills/` — visibles para todos los agentes del nodo
- **Carpetas compartidas**: via `skills.load.extraDirs` (precedencia minima)

**Agent skill allowlists** — en setups multi-agente, las ubicaciones determinan que copia de un skill gana (precedencia), pero las allowlists controlan que skills son **visibles** para cada agente. Son controles separados e independientes.

Configuracion:

```json5
{
 agents: {
 defaults: {
 skills: ["github", "weather"] // baseline compartido
 },
 list: [
 { id: "writer" }, // hereda defaults
 { id: "docs", skills: ["docs-search"] }, // reemplaza defaults (NO hereda)
 { id: "sandbox-agent", skills: [] }, // sin skills
 ]
 }
}
```

Reglas:
- `agents.defaults.skills` define baseline heredado por agentes sin override
- `agents.list[].skills` **reemplaza** el baseline completo (no se mezcla con defaults)
- Omitir `skills` en un agente = hereda defaults; `skills: []` = sin skills
- Si el allowlist efectivo cambia para una sesion activa, OpenClaw refresca el session snapshot

## 4.4 Skills en plugins

Plugins declaran skills en `openclaw.plugin.json` (rutas relativas a la raiz del plugin). Los skills del plugin se cargan cuando el plugin esta habilitado y participan en las reglas de precedencia normales. Gating via `metadata.openclaw.requires.config` en la entrada de configuracion del plugin.

## 4.5 Scripts en skills

### Comandos one-off

Cuando un paquete existente ya hace lo necesario, referenciarlo directamente en `SKILL.md` sin directorio `scripts/`:

| Herramienta | Ecosistema | Ejemplo |
| --- | --- | --- |
| `uvx` | Python (via uv) | `uvx ruff@0.8.0 check .` |
| `pipx` | Python | `pipx run 'black==24.10.0' .` |
| `npx` | Node.js (incluido con npm) | `npx eslint@9 --fix .` |
| `bunx` | Bun | `bunx eslint@9 --fix .` |
| `deno run` | Deno | `deno run npm:create-vite@6 my-app` |
| `go run` | Go | `go run golang.org/x/tools/cmd/goimports@v0.28.0 .` |

Reglas para comandos one-off:
- Fijar versiones (`npx eslint@9.0.0`) para reproducibilidad
- Declarar prerequisitos en `SKILL.md` (ej: "Requiere Node.js 18+") o usar el campo `compatibility`
- Cuando un comando crece en complejidad, moverlo a `scripts/`

### Scripts autocontenidos con dependencias inline

Varios lenguajes soportan declaracion de dependencias inline:

- **Python (PEP 723)**: bloque TOML en `# ///` markers, ejecutar con `uv run scripts/extract.py`
- **Deno**: importaciones `npm:` y `jsr:` con version, ejecutar con `deno run scripts/extract.ts`
- **Bun**: auto-instala paquetes faltantes, ejecutar con `bun run scripts/extract.ts`
- **Ruby**: `bundler/inline` con bloque `gemfile`, ejecutar con `ruby scripts/extract.rb`

### Diseno de scripts para uso agentico

| Principio | Detalle |
| --- | --- |
| Sin prompts interactivos | Agentes operan en shells no interactivos. Aceptar input via flags, env vars o stdin |
| `--help` documentado | Output de help es la interfaz primaria del agente. Incluir descripcion, flags, ejemplos |
| Mensajes de error utiles | Decir que fallo, que se esperaba, que intentar. No "Error: invalid input" |
| Output estructurado | Preferir JSON, CSV, TSV sobre texto libre. Datos a stdout, diagnosticos a stderr |
| Idempotencia | "Crear si no existe" es mas seguro que "crear y fallar si duplicado" |
| Soporte dry-run | `--dry-run` para operaciones destructivas o con estado |
| Exit codes significativos | Codigos distintos para tipos de fallo diferentes, documentados en `--help` |
| Defaults seguros | Operaciones destructivas requieren flags de confirmacion (`--confirm`, `--force`) |
| Output predecible en tamano | Muchos harnesses truncan output >10-30K chars. Defaultear a resumen; soportar `--offset` para paginacion |

Referenciar scripts desde `SKILL.md` con rutas relativas desde la raiz del skill:

```markdown

## Scripts disponibles

- **`scripts/validate.sh`** — Valida archivos de configuracion
- **`scripts/process.py`** — Procesa datos de entrada
```

## 5. Implementacion y despliegue

### 5.1 ClawHub — registro publico

ClawHub (`clawhub.ai`) es el registro publico de skills y plugins.

Flujos nativos de OpenClaw:

```bash
openclaw skills search "calendario"
openclaw skills install <slug>
openclaw skills update --all
```

ClawHub CLI (para publish/sync — requiere auth):

```bash
npm i -g clawhub
clawhub login
clawhub publish ./mi-skill --slug mi-skill --name "Mi Skill" --version 1.0.0 --tags latest
clawhub sync --all
```

### 5.2 CLI de skills

```bash
openclaw skills search "query" # buscar en ClawHub
openclaw skills install <slug> # instalar en workspace activo
openclaw skills install <slug> --version <version>
openclaw skills update <slug> # actualizar uno
openclaw skills update --all # actualizar todos
openclaw skills list # listar skills locales
openclaw skills list --eligible # solo elegibles
openclaw skills info <name> # detalle de un skill
openclaw skills check # diagnosticar binarios/env/config faltantes
```

`search`/`install`/`update` usan ClawHub e instalan en `<workspace>/skills/`. `list`/`info`/`check` inspeccionan skills locales visibles para el workspace y config actuales.

### 5.3 Comandos ClawHub CLI

| Comando | Funcion |
| --- | --- |
| `clawhub login` | Autenticacion via browser o `--token` |
| `clawhub logout` | Cerrar sesion |
| `clawhub whoami` | Identidad actual |
| `clawhub search "query"` | Buscar skills (busqueda semantica por embeddings) |
| `clawhub install <slug>` | Instalar version especifica o latest |
| `clawhub update <slug>` | Actualizar skill (o `--all`) |
| `clawhub list` | Listar instalados (lee `.clawhub/lock.json`) |
| `clawhub publish <path>` | Publicar skill con slug, name, version, changelog, tags |
| `clawhub delete <slug> --yes` | Eliminar skill (owner/admin) |
| `clawhub undelete <slug> --yes` | Restaurar skill eliminado |
| `clawhub sync` | Escanear + publicar skills nuevos/actualizados |

Opciones globales: `--workdir`, `--dir`, `--site`, `--registry`, `--no-input`, `-V`.

### 5.4 Validacion de formato AgentSkills

La libreria de referencia `skills-ref` valida que el frontmatter de `SKILL.md` cumple la especificacion y sigue todas las convenciones de nombrado:

```bash
skills-ref validate ./mi-skill
```

Repositorio: `github.com/agentskills/agentskills/tree/main/skills-ref`.

### 5.5 Versionado en ClawHub

- Cada publicacion crea una nueva version semver (`SkillVersion`)
- Tags (como `latest`) apuntan a una version; mover tags permite rollback
- Changelogs adjuntos por version
- Updates comparan contenido local vs versiones del registro usando hash de contenido

### 5.6 Almacenamiento local

- Skills instalados registrados en `.clawhub/lock.json`
- Tokens de auth en archivo de config de ClawHub CLI (override: `CLAWHUB_CONFIG_PATH`)

### 5.7 Variables de entorno ClawHub

| Variable | Funcion |
| --- | --- |
| `CLAWHUB_SITE` | Override URL del sitio |
| `CLAWHUB_REGISTRY` | Override URL del API del registro |
| `CLAWHUB_CONFIG_PATH` | Override ubicacion de config/token |
| `CLAWHUB_WORKDIR` | Override workdir por defecto |
| `CLAWHUB_DISABLE_TELEMETRY=1` | Deshabilitar telemetria en `sync` |

## 6. Configuracion

### 6.1 Schema completo (`~/.openclaw/openclaw.json`)

```json5
{
 skills: {
 allowBundled: ["gemini", "peekaboo"],
 load: {
 extraDirs: ["~/Projects/agent-scripts/skills"],
 watch: true,
 watchDebounceMs: 250
 },
 install: {
 preferBrew: true,
 nodeManager: "npm" // npm | pnpm | yarn | bun
 },
 entries: {
 "image-lab": {
 enabled: true,
 apiKey: { source: "env", provider: "default", id: "GEMINI_API_KEY" },
 env: { GEMINI_API_KEY: "KEY_VALUE" },
 config: { endpoint: "https://example.invalid", model: "nano-pro" }
 },
 "peekaboo": { enabled: true },
 "sag": { enabled: false }
 }
 },
 agents: {
 defaults: {
 skills: ["github", "weather"] // allowlist baseline (omitir = sin restriccion)
 },
 list: [
 { id: "writer" }, // hereda defaults.skills
 { id: "docs", skills: ["docs-search"] }, // reemplaza (no hereda)
 { id: "sandbox", skills: [] }, // sin skills
 ]
 }
}
```

### 6.2 Campos de configuracion global

| Campo | Default | Descripcion |
| --- | --- | --- |
| `skills.allowBundled` | (todos) | Allowlist para skills bundled. Si se define, solo los listados son elegibles |
| `skills.load.extraDirs` | [] | Directorios adicionales de skills (precedencia minima) |
| `skills.load.watch` | true | Observar carpetas de skills y refrescar al detectar cambios |
| `skills.load.watchDebounceMs` | 250 | Debounce del watcher en milisegundos |
| `skills.install.preferBrew` | true | Preferir instaladores brew cuando disponibles |
| `skills.install.nodeManager` | npm | Gestor de paquetes para instalacion: npm, pnpm, yarn, bun |

### 6.3 Campos por skill (`entries.<skillKey>`)

| Campo | Descripcion |
| --- | --- |
| `enabled` | `false` deshabilita el skill aunque este bundled/instalado |
| `env` | Variables de entorno inyectadas para el agent run (solo si no estan ya definidas) |
| `apiKey` | Convenience para skills con `primaryEnv`. String plano o SecretRef `{ source, provider, id }` |
| `config` | Bag de campos custom por skill |

Reglas:
- Claves bajo `entries` mapean al nombre del skill por defecto
- Si el skill define `metadata.openclaw.skillKey`, usar esa clave
- Cambios se reflejan en el siguiente agent turn si el watcher esta habilitado

### 6.4 Inyeccion de entorno por agent run

Secuencia al iniciar un agent run:
1. Leer metadata de skills
2. Aplicar `skills.entries.<key>.env` y `skills.entries.<key>.apiKey` a `process.env`
3. Construir system prompt con skills elegibles
4. Restaurar entorno original al terminar el run

Alcance: **scoped al agent run**, no es entorno global del shell.

### 6.5 Skills en entornos sandboxed

Cuando la sesion esta en sandbox (Docker), los procesos de skills corren dentro del contenedor. El sandbox **no hereda** `process.env` del host.

Opciones para inyectar variables:
- `agents.defaults.sandbox.docker.env` (o per-agent `agents.list[].sandbox.docker.env`)
- Incorporar env vars en imagen Docker custom

`env` global y `skills.entries.<skill>.env/apiKey` aplican **solo a ejecuciones en host**.

### 6.6 Binarios en sandbox

`requires.bins` se verifica en el **host** al cargar el skill. Si el agente esta en sandbox, el binario tambien debe existir **dentro del contenedor**.

Instalacion via:
- `agents.defaults.sandbox.docker.setupCommand` — ejecuta una vez despues de crear el contenedor
- Imagen Docker custom

`setupCommand` requiere: egreso de red, filesystem root escribible, usuario root en el sandbox.
