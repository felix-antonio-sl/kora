---
_manifest:
  urn: "urn:agengai:kb:openclaw-skills-ops"
  provenance:
    created_by: kora/curator
    created_at: "2026-03-26"
    source: "openclaw/docs snapshot 2026-03: tools/skills.md, tools/creating-skills.md, tools/skills-config.md, tools/clawhub.md, cli/skills.md, platforms/mac/skills.md"
version: "1.0.0"
status: draft
tags: [openclaw, skills, lifecycle, clawhub, gating, configuracion, agentes]
lang: es
extensions:
  kora:
    family: note
    snapshot_date: "2026-03-26"
    disclaimer: "Snapshot versionado. Consultar documentacion oficial OpenClaw para info actualizada."
---

# Manual Operativo: Skills OpenClaw

## Anatomia de un skill

Un skill es un directorio que contiene un archivo `SKILL.md` con frontmatter YAML e instrucciones en markdown. Compatible con la spec [AgentSkills](https://agentskills.io).

Un skill NO es codigo ejecutable. Es texto instructivo que OpenClaw inyecta en el system prompt del agente. El agente decide cuando y como usar el skill basado en la descripcion e instrucciones.

Tres capas diferenciadas:

| Capa | Que es | Formato | Se ejecuta |
|------|--------|---------|------------|
| **Skill** | Instrucciones para el agente | `SKILL.md` (markdown) | No — texto inyectado en prompt |
| **Tool** | Funcion tipada invocable | JSON schema + handler | Si — llamada desde el agente |
| **Plugin** | Paquete Node.js extensible | NPM package + TypeScript | Si — codigo registrado en Gateway |

Los plugins pueden distribuir skills via `openclaw.plugin.json`. Los skills ensenan al agente a usar tools. Los tools ejecutan acciones.

## Metadata y frontmatter SKILL.md

El parser solo acepta keys de una linea. `metadata` es un JSON single-line.

### Campos del frontmatter

| Campo | Requerido | Tipo | Descripcion |
|-------|-----------|------|-------------|
| `name` | Si | string | Identificador unico (snake_case) |
| `description` | Si | string | Descripcion de una linea visible al agente |
| `homepage` | No | URL | Mostrada como "Website" en macOS Skills UI |
| `user-invocable` | No | bool (default: true) | Expone el skill como slash command del usuario |
| `disable-model-invocation` | No | bool (default: false) | Excluye del prompt del modelo (disponible via invocacion usuario) |
| `command-dispatch` | No | `tool` | Bypass del modelo: dispatch directo a tool |
| `command-tool` | Condicional | string | Tool a invocar (requerido si `command-dispatch: tool`) |
| `command-arg-mode` | No | `raw` (default) | Modo de argumentos para tool dispatch |
| `metadata` | No | JSON single-line | Metadata OpenClaw (gating, instaladores, UI) |

Cuando `command-dispatch: tool`, el tool recibe: `{ command: "<raw args>", commandName: "<slash command>", skillName: "<skill name>" }`.

Usar `{baseDir}` en instrucciones para referenciar la ruta del directorio del skill.

### Ejemplo minimal

```markdown
---
name: hello_world
description: A simple skill that says hello.
---

# Hello World Skill

When the user asks for a greeting, use the `echo` tool to say
"Hello from your custom skill!".
```

### Ejemplo con metadata completa

```markdown
---
name: image_lab
description: Generate or edit images via a provider-backed image workflow
homepage: https://example.com
metadata: { "openclaw": { "emoji": "🎨", "primaryEnv": "GEMINI_API_KEY", "os": ["darwin", "linux"], "requires": { "bins": ["uv"], "env": ["GEMINI_API_KEY"], "config": ["browser.enabled"] }, "install": [{ "id": "brew", "kind": "brew", "formula": "gemini-cli", "bins": ["gemini"], "label": "Install Gemini CLI (brew)" }] } }
---

# Image Lab

Instructions for the agent...
```

## Ubicaciones y precedencia

| Ubicacion | Ruta | Precedencia | Scope |
|-----------|------|-------------|-------|
| Workspace | `<workspace>/skills/` | Maxima | Per-agent |
| Managed/local | `~/.openclaw/skills/` | Media | Shared (todos los agentes) |
| Bundled | Shipped con instalacion OpenClaw | Baja | Global |
| Extra dirs | `skills.load.extraDirs` en config | Minima | Custom shared |

Si un skill name existe en mas de una ubicacion, prevalece la de mayor precedencia. El skill de workspace sobreescribe managed, que sobreescribe bundled.

Workspace skills son user-owned. `~/.openclaw/skills/` (managed) existe para local overrides: pinning o patching de un bundled skill sin modificar la copia bundled.

En setups multi-agente: cada agente tiene su propio workspace. Skills en `<workspace>/skills/` son exclusivos de ese agente. Skills en `~/.openclaw/skills/` son visibles para todos los agentes en la misma maquina.

## Gating: filtros de elegibilidad

OpenClaw filtra skills en tiempo de carga usando campos bajo `metadata.openclaw`.

### Campos de gating

| Campo | Tipo | Funcion |
|-------|------|---------|
| `always` | bool | Si `true`, skip todos los gates — siempre elegible |
| `os` | string[] | Filtro por plataforma: `darwin`, `linux`, `win32` |
| `requires.bins` | string[] | Cada binario debe existir en PATH |
| `requires.anyBins` | string[] | Al menos uno debe existir en PATH |
| `requires.env` | string[] | Variable de entorno debe existir o estar en config |
| `requires.config` | string[] | Rutas de `openclaw.json` que deben ser truthy |
| `primaryEnv` | string | Env var asociada a `skills.entries.<name>.apiKey` |
| `emoji` | string | Icono en macOS Skills UI |
| `homepage` | URL | "Website" en macOS Skills UI |
| `skillKey` | string | Key de config si difiere de `name` |

Si no existe `metadata.openclaw`, el skill es siempre elegible (salvo desactivacion por config o `allowBundled`).

### Logica de evaluacion

1. Si `always: true` → elegible (skip gates)
2. Si `os` definido y plataforma actual no esta en lista → no elegible
3. Si `requires.bins` definido → cada binario debe existir en PATH del host
4. Si `requires.anyBins` definido → al menos uno en PATH
5. Si `requires.env` definido → variable en `process.env` o provista en `skills.entries.<key>.env`
6. Si `requires.config` definido → cada ruta debe ser truthy en `openclaw.json`

### Sandbox: caveat bins

`requires.bins` se evalua en el **host** al cargar el skill. Si el agente corre en sandbox, el binario debe existir tambien **dentro del container**. Instalarlo via `agents.defaults.sandbox.docker.setupCommand` (o imagen custom). `setupCommand` ejecuta una vez post-creacion del container. Requiere egress de red, filesystem root writable y usuario root.

### Instaladores (macOS UI)

Array `install` bajo `metadata.openclaw`. Cada entrada define una opcion de instalacion:

| Kind | Campos | Notas |
|------|--------|-------|
| `brew` | `formula`, `bins`, `label`, `os` | Preferido en macOS por defecto |
| `node` | `package`, `bins` | Respeta `skills.install.nodeManager` (npm/pnpm/yarn/bun) |
| `go` | `path` | Si Go ausente y brew disponible, instala Go via Homebrew |
| `uv` | `package`, `bins` | Python package manager |
| `download` | `url`, `archive`, `extract`, `stripComponents`, `targetDir` | Descarga directa; `targetDir` default: `~/.openclaw/tools/<skillKey>` |

Si multiples instaladores listados, el gateway elige uno preferido (brew si disponible, luego node). Si todos son `download`, OpenClaw lista cada entrada.

Campos opcionales en instalador: `os` (filtro plataforma), `bins` (binarios que provee).

## Configuracion en openclaw.json

Toda configuracion de skills vive bajo `skills` en `~/.openclaw/openclaw.json`.

### Esquema completo

```json5
{
  skills: {
    allowBundled: ["gemini", "peekaboo"],      // Allowlist solo para bundled
    load: {
      extraDirs: ["~/skills-pack/skills"],     // Dirs adicionales (precedencia minima)
      watch: true,                             // Auto-refresh al cambiar SKILL.md
      watchDebounceMs: 250                     // Debounce del watcher (ms)
    },
    install: {
      preferBrew: true,                        // Preferir brew para instaladores
      nodeManager: "npm"                       // npm | pnpm | yarn | bun
    },
    entries: {
      "image-lab": {
        enabled: true,
        apiKey: { source: "env", provider: "default", id: "GEMINI_API_KEY" },
        env: { GEMINI_API_KEY: "sk-..." },
        config: { endpoint: "https://...", model: "nano-pro" }
      },
      peekaboo: { enabled: true },
      sag: { enabled: false }
    }
  }
}
```

### Campos globales

| Campo | Default | Descripcion |
|-------|---------|-------------|
| `allowBundled` | (sin filtro) | Allowlist para bundled skills. Si definido, solo los listados son elegibles. No afecta managed/workspace |
| `load.extraDirs` | [] | Directorios extra de skills (precedencia minima) |
| `load.watch` | true | Observar carpetas de skills y refrescar snapshot |
| `load.watchDebounceMs` | 250 | Debounce del watcher en milisegundos |
| `install.preferBrew` | true | Preferir brew al instalar dependencias |
| `install.nodeManager` | `npm` | Package manager para instalaciones node (npm/pnpm/yarn/bun). Solo afecta skill installs; el Gateway runtime debe ser Node (Bun no recomendado para WhatsApp/Telegram) |

### Campos por skill (`entries.<skillKey>`)

| Campo | Descripcion |
|-------|-------------|
| `enabled` | `false` desactiva el skill aunque este bundled/instalado |
| `env` | Variables de entorno inyectadas para el agent run (solo si no existen en `process.env`) |
| `apiKey` | Convenience para skills con `primaryEnv`. Acepta string plaintext o SecretRef `{ source, provider, id }` |
| `config` | Bag de campos custom por skill |

Keys bajo `entries` coinciden con `name` del skill por defecto. Si el skill define `metadata.openclaw.skillKey`, usar ese key.

Si el name contiene guiones, quotear el key (JSON5 soporta keys con comillas).

## Inyeccion de ambiente y secrets

Ciclo de inyeccion per agent run:

1. OpenClaw lee metadata de skills elegibles
2. Aplica `skills.entries.<key>.env` y `skills.entries.<key>.apiKey` a `process.env`
3. Construye system prompt con skills elegibles
4. Al terminar el run, restaura ambiente original

La inyeccion es **scoped al agent run**, no modifica el ambiente global del shell.

`env` solo aplica si la variable no existe ya en `process.env`. `apiKey` se resuelve al env var declarado en `primaryEnv`.

### Sandbox y secrets

En sesiones sandboxed, los procesos corren en Docker. El sandbox **no hereda** el `process.env` del host. `skills.entries.<key>.env` y `apiKey` aplican solo al host.

Alternativas para sandbox:
- `agents.defaults.sandbox.docker.env` (o per-agent `agents.list[].sandbox.docker.env`)
- Bake el env en imagen custom del sandbox


## Creacion de un skill

1. **Crear directorio del skill:**

```bash
mkdir -p ~/.openclaw/workspace/skills/mi-skill
```

Para skills compartidos entre agentes: `~/.openclaw/skills/mi-skill`

2. **Escribir SKILL.md** con frontmatter (name + description requeridos) e instrucciones markdown en el cuerpo.

3. **Agregar tools (opcional).** Definir schemas custom en frontmatter o instruir al agente a usar tools del sistema (`exec`, `browser`, etc.). Skills tambien pueden distribuirse dentro de plugins junto a los tools que documentan.

4. **Recargar sesion** para que OpenClaw detecte el skill:

```bash
# Desde chat
/new

# O reiniciar gateway
openclaw gateway restart
```

Si el watcher esta habilitado (`skills.load.watch: true`), cambios en `SKILL.md` se detectan automaticamente en el siguiente turno del agente sin reiniciar.

5. **Verificar carga:**

```bash
openclaw skills list
openclaw skills list --eligible
```

## Testing y verificacion

### Comandos de diagnostico

| Comando | Funcion |
|---------|---------|
| `openclaw skills list` | Listar todos los skills visibles |
| `openclaw skills list --eligible` | Solo skills que pasan gating |
| `openclaw skills info <name>` | Detalle de un skill (metadata, requisitos, estado) |
| `openclaw skills check` | Verificar requisitos (bins, env, config) de todos los skills |

### Test funcional

```bash
openclaw agent --message "prueba el skill mi-skill"
```

O interactuar directamente con el agente en chat y solicitar la funcionalidad del skill.

### Comportamiento del snapshot

OpenClaw toma snapshot de skills elegibles al iniciar sesion. Cambios en skills o config toman efecto:
- En la siguiente sesion nueva (sin watcher)
- En el siguiente turno del agente (con watcher habilitado)

## Publicacion en ClawHub

ClawHub es el registro publico de skills y plugins OpenClaw. Sitio: [clawhub.ai](https://clawhub.ai). Busqueda por embeddings (vector search), no solo keywords.

Ademas de skills, ClawHub soporta plugins:

```bash
openclaw plugins install clawhub:<package>
openclaw plugins update --all
```

Specs npm-safe de plugins se prueban contra ClawHub antes de npm. Los comandos nativos `openclaw` persisten source metadata para que `update` siga desde ClawHub en futuras actualizaciones.

### Requisitos de publicacion

- Cuenta GitHub con al menos 1 semana de antiguedad
- CLI `clawhub` instalada (`npm i -g clawhub` o `pnpm add -g clawhub`)
- Autenticacion: `clawhub login` (flujo browser) o `clawhub login --token <token>`

### Flujo de publicacion

Skill individual:

```bash
clawhub publish ./mi-skill \
  --slug mi-skill \
  --name "Mi Skill" \
  --version 1.0.0 \
  --changelog "Version inicial" \
  --tags latest
```

Scan y publicacion masiva:

```bash
clawhub sync --all
```

`clawhub sync` escanea el workdir actual. Si no encuentra skills, busca en ubicaciones legacy (`~/openclaw/skills`, `~/.openclaw/skills`).

### Instalacion por usuarios

```bash
openclaw skills install <skill-slug>
openclaw skills install <skill-slug> --version <version>
```

`openclaw skills install` instala en el directorio `skills/` del workspace activo. OpenClaw lo detecta en la siguiente sesion.

### Versionamiento en ClawHub

- Cada publish crea una nueva version **semver** (`SkillVersion`)
- Tags (`latest`, `stable`, etc.) apuntan a versiones; mover tags permite rollback
- Changelogs adjuntos por version (pueden estar vacios en sync)
- Content hash para comparar version local vs registry

### Lockfile y storage

- Skills instalados se registran en `.clawhub/lock.json` bajo el workdir
- Auth tokens almacenados en el config file de ClawHub CLI (override via `CLAWHUB_CONFIG_PATH`)

### Seguridad del registro

- Cualquier usuario autenticado puede reportar un skill
- Razones de reporte requeridas y registradas
- Maximo 20 reportes activos por usuario
- Skills con >3 reportes unicos se ocultan automaticamente
- Moderadores pueden ver, desocultar, eliminar skills o banear usuarios

### Variables de entorno ClawHub

| Variable | Funcion |
|----------|---------|
| `CLAWHUB_SITE` | Override URL del sitio |
| `CLAWHUB_REGISTRY` | Override URL de la API del registry |
| `CLAWHUB_CONFIG_PATH` | Override ruta de config/token CLI |
| `CLAWHUB_WORKDIR` | Override workdir por defecto |
| `CLAWHUB_DISABLE_TELEMETRY=1` | Desactivar telemetria en `sync` |

## Mantenimiento y hot reload

### Skills watcher

Por defecto, OpenClaw observa carpetas de skills y actualiza el snapshot cuando cambian archivos `SKILL.md`.

```json5
{
  skills: {
    load: {
      watch: true,          // default: true
      watchDebounceMs: 250  // default: 250
    }
  }
}
```

Cambios detectados se aplican en el siguiente turno del agente dentro de la misma sesion (hot reload).

### Session snapshot

OpenClaw toma snapshot de skills elegibles al iniciar sesion. Sin watcher, cambios requieren nueva sesion. Con watcher, el refresh es mid-session.

### Remote macOS nodes

Si el Gateway corre en Linux y un nodo macOS esta conectado con `system.run` permitido (Exec approvals security no en `deny`), OpenClaw trata skills macOS-only como elegibles si los binarios requeridos existen en ese nodo. El agente ejecuta esos skills via `nodes.run`.

Si el nodo macOS se desconecta, los skills permanecen visibles pero invocaciones pueden fallar hasta reconexion.

### Buenas practicas

- Instrucciones concisas: indicar al modelo *que* hacer, no como ser un AI
- Seguridad: si el skill usa `exec`, evitar command injection desde input no confiable
- Test local obligatorio antes de compartir: `openclaw agent --message "..."`

## Versionamiento y actualizacion

### Semver en ClawHub

Cada publish crea una nueva version semver. Tags como `latest` apuntan a versiones y permiten rollback.

### Actualizacion

| Comando | Funcion |
|---------|---------|
| `openclaw skills update <slug>` | Actualizar un skill |
| `openclaw skills update --all` | Actualizar todos los instalados |
| `clawhub update <slug>` | Actualizar via ClawHub CLI |
| `clawhub update --all` | Actualizar todos via ClawHub CLI |
| `clawhub update <slug> --version <v>` | Actualizar a version especifica |

### Conflictos locales

Updates comparan contenido local con versiones del registry usando content hash. Si archivos locales no coinciden con ninguna version publicada, el CLI pregunta antes de sobreescribir (o requiere `--force` en modo no interactivo).

## Skills dentro de plugins

Plugins pueden incluir skills listando directorios `skills` en `openclaw.plugin.json` (rutas relativas al root del plugin).

Skills de plugin se cargan cuando el plugin esta habilitado y participan en las reglas normales de precedencia. Gating posible via `metadata.openclaw.requires.config` en la entrada de config del plugin.

Para construccion de plugins: ver documentacion de Building Plugins.

## Impacto en tokens

Cuando hay skills elegibles, OpenClaw inyecta una lista XML compacta en el system prompt (`formatSkillsForPrompt`).

### Formula (caracteres)

```
total = 195 + Σ (97 + len(name_escaped) + len(description_escaped) + len(location_escaped))
```

- **Overhead base:** 195 caracteres (solo cuando >= 1 skill)
- **Por skill:** 97 caracteres + longitud de name, description y location con XML escaping
- XML escaping expande `& < > " '` a entidades (`&amp;`, `&lt;`, etc.), aumentando longitud
- Estimacion: ~4 caracteres/token (tokenizer estilo OpenAI), ~97 chars ≈ 24 tokens por skill mas longitudes reales de campos

## Seguridad

- Tratar skills de terceros como **codigo no confiable**. Leerlos antes de habilitar
- Preferir sandbox runs para inputs no confiables y tools riesgosos
- Workspace y extra-dir skill discovery solo aceptan realpath dentro del root configurado
- `skills.entries.*.env` y `skills.entries.*.apiKey` inyectan secrets en el **proceso host** para ese agent turn (no en sandbox). Mantener secrets fuera de prompts y logs
- `allowBundled` filtra solo bundled skills. Managed/workspace skills no se filtran por allowlist
- Para modelo de amenazas completo: consultar documentacion de Security de OpenClaw

## Deprecacion y remocion

| Accion | Metodo | Scope |
|--------|--------|-------|
| Desactivar un skill | `skills.entries.<key>.enabled: false` en config | Local (ese agente/host) |
| Filtrar bundled skills | `skills.allowBundled: [lista]` — solo los listados pasan | Solo bundled (managed/workspace no afectados) |
| Remover de disco | Eliminar directorio del skill | Local (detectado en siguiente snapshot) |
| Eliminar de ClawHub | `clawhub delete <slug> --yes` | Registry (global) |
| Restaurar en ClawHub | `clawhub undelete <slug> --yes` | Registry (global) |

## CLI: referencia de comandos

### openclaw skills

| Comando | Descripcion |
|---------|-------------|
| `openclaw skills search "query"` | Buscar skills en ClawHub |
| `openclaw skills install <slug>` | Instalar skill en workspace activo |
| `openclaw skills install <slug> --version <v>` | Instalar version especifica |
| `openclaw skills update <slug>` | Actualizar un skill |
| `openclaw skills update --all` | Actualizar todos los instalados |
| `openclaw skills list` | Listar skills visibles |
| `openclaw skills list --eligible` | Solo skills que pasan gating |
| `openclaw skills info <name>` | Detalle de un skill |
| `openclaw skills check` | Verificar requisitos de todos los skills |

`search`/`install`/`update` usan ClawHub e instalan en `skills/` del workspace activo. `list`/`info`/`check` inspeccionan skills locales del workspace y config actual.

### clawhub CLI

| Comando | Descripcion | Flags clave |
|---------|-------------|-------------|
| `clawhub login` | Autenticacion (browser flow) | `--token <t>`, `--label <l>`, `--no-browser` |
| `clawhub logout` | Cerrar sesion | |
| `clawhub whoami` | Usuario actual | |
| `clawhub search "query"` | Buscar en registry | `--limit <n>` |
| `clawhub install <slug>` | Instalar skill | `--version <v>`, `--force` |
| `clawhub update <slug>` | Actualizar skill | `--version <v>`, `--force`, `--all` |
| `clawhub list` | Listar instalados (lee `.clawhub/lock.json`) | |
| `clawhub publish <path>` | Publicar skill | `--slug`, `--name`, `--version`, `--changelog`, `--tags` |
| `clawhub sync` | Scan local + publish actualizaciones | `--root <dir>`, `--all`, `--dry-run`, `--bump <type>` (patch/minor/major, default: patch), `--changelog`, `--tags`, `--concurrency <n>` (default: 4) |
| `clawhub delete <slug>` | Eliminar del registry | `--yes` |
| `clawhub undelete <slug>` | Restaurar en registry | `--yes` |

Opciones globales: `--workdir <dir>`, `--dir <dir>`, `--site <url>`, `--registry <url>`, `--no-input`, `-V`.

## macOS: UI de Skills

La app macOS no parsea skills localmente — los obtiene del gateway via `skills.status`.

- **Data source:** `skills.status` (gateway) retorna todos los skills con elegibilidad y requisitos faltantes (incluyendo bloqueos por `allowBundled`). Requirements derivados de `metadata.openclaw.requires` en cada `SKILL.md`
- **Install actions:** `metadata.openclaw.install` define opciones. La app invoca `skills.install` en el gateway host. Solo un instalador preferido cuando hay multiples (brew > node)
- **Env/API keys:** Almacenados en `~/.openclaw/openclaw.json` bajo `skills.entries.<skillKey>`. Updates via `skills.update` (patchea `enabled`, `apiKey`, `env`)
- **Remote mode:** Install y config updates ejecutan en el gateway host, no en el Mac local
