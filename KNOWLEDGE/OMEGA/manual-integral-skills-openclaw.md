---
_manifest:
  urn: "urn:agengai:kb:openclaw-skills-manual"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-03-26"
    source: "KNOWLEDGE/agengai/openclaw/documentacion-oficial (tools/skills.md, tools/creating-skills.md, tools/skills-config.md, tools/clawhub.md, tools/slash-commands.md, cli/skills.md, platforms/mac/skills.md, tools/subagents.md, tools/exec-approvals.md, tools/loop-detection.md, tools/multi-agent-sandbox-tools.md, tools/elevated.md, gateway/sandboxing.md, gateway/secrets.md, gateway/security/index.md, security/THREAT-MODEL-ATLAS.md, concepts/agent.md, concepts/agent-workspace.md, concepts/system-prompt.md, plugins/building-plugins.md, plugins/manifest.md, help/testing.md; verificado contra mirror sync 2026-04-05 commit 2a39141) + fuente web externa: agentskills.io (spec overview, specification, quickstart, best-practices, optimizing-descriptions, evaluating-skills, using-scripts, client-implementation)"
version: "2.2.0"
status: draft
tags: [openclaw, skills, agentes-ia, llm, manual, ciclo-de-vida, seguridad, orquestacion, agentskills, interoperabilidad]
lang: es
extensions:
  agengai:
    family: guide
    scope: "Creacion, operacion y evolucion de skills en OpenClaw"
    dimensions: 15
    related: ["urn:agengai:kb:openclaw-manual-integral"]
---

# Manual Integral de Skills en OpenClaw

## 1. Resumen ejecutivo

OpenClaw usa carpetas de skills compatibles con el estandar abierto **AgentSkills** para ensenar al agente como usar herramientas. Cada skill es un directorio con un archivo `SKILL.md` que contiene frontmatter YAML e instrucciones Markdown.

AgentSkills fue desarrollado originalmente por Anthropic y liberado como formato abierto. Ha sido adoptado por mas de 30 productos: Claude Code, VS Code, Cursor, Gemini CLI, OpenAI Codex, GitHub Copilot, Junie (JetBrains), OpenHands, Roo Code, Goose, Amp, Letta, Firebender, Mux, OpenCode, Databricks, Spring AI, Kiro, Laravel Boost, TRAE, Factory, Piebald, Mistral Vibe, Command Code, Snowflake, Qodo, Ona, VT Code, Emdash y Agentman, entre otros.

Arquitectura, despliegue, seguridad y operacion general del Gateway: ver `urn:agengai:kb:openclaw-manual-integral`.

## 2. Definiciones

| Termino | Definicion |
| --- | --- |
| **Skill** | Directorio con `SKILL.md` que ensena al agente cuando y como usar herramientas |
| **SKILL.md** | Archivo con frontmatter YAML + instrucciones Markdown que define un skill |
| **AgentSkills** | Estandar abierto de formato de skills (`agentskills.io`), adoptado por 30+ productos |
| **Progressive disclosure** | Estrategia de carga en 3 tiers: catalogo (~100 tokens) -> instrucciones (<5K tokens) -> recursos (bajo demanda) |
| **Skill catalog** | Lista compacta de `name` + `description` de skills elegibles, inyectada en system prompt al inicio de sesion |
| **Skill activation** | Momento en que el agente carga el cuerpo completo de `SKILL.md` en contexto |
| **Skill resources** | Archivos auxiliares del skill: `scripts/`, `references/`, `assets/` — cargados bajo demanda |
| **Trigger rate** | Fraccion de ejecuciones donde un skill se activa correctamente ante un prompt dado |
| **Bundled skill** | Skill incluido en la distribucion de OpenClaw (npm o .app) |
| **Managed/local skill** | Skill en `~/.openclaw/skills`, visible para todos los agentes del nodo |
| **Workspace skill** | Skill en `<workspace>/skills/`, exclusivo del agente |
| **Gating** | Filtrado en tiempo de carga por binarios, env vars, config o plataforma |
| **ClawHub** | Registro publico de skills y plugins para OpenClaw |
| **Eligibility** | Estado booleano que determina si un skill se inyecta en el system prompt |
| **Session snapshot** | Lista congelada de skills elegibles al iniciar una sesion |
| **Skills watcher** | Observador de filesystem que refresca skills al detectar cambios en `SKILL.md` |
| **SecretRef** | Objeto `{ source, provider, id }` para inyeccion segura de API keys |
| **Sandbox** | Contenedor Docker donde se ejecutan procesos de skills aislados del host |
| **Elevated mode** | Modo que habilita ejecucion de herramientas restringidas (host shell) |

## 3. Diseno de skills

### 3.1 Estructura de directorio

Un skill es un directorio con, como minimo, un archivo `SKILL.md`:

```
mi-skill/
├── SKILL.md          # Requerido: metadata + instrucciones
├── scripts/          # Opcional: codigo ejecutable
├── references/       # Opcional: documentacion auxiliar
├── assets/           # Opcional: templates, recursos estaticos
└── ...               # Cualquier archivo o directorio adicional
```

Directorios opcionales:
- **`scripts/`** — Codigo ejecutable que el agente puede correr. Scripts deben ser autocontenidos o documentar dependencias explicitamente. Incluir mensajes de error utiles.
- **`references/`** — Documentacion adicional que el agente lee bajo demanda: `REFERENCE.md`, `FORMS.md`, archivos de dominio (`finance.md`, `legal.md`). Mantener archivos individuales enfocados para minimizar uso de contexto.
- **`assets/`** — Recursos estaticos: templates de documentos, imagenes, esquemas, tablas de lookup.

### 3.2 Formato SKILL.md

Estructura minima requerida:

```markdown
---
name: nombre-del-skill
description: Descripcion de que hace y cuando usarlo.
---

# Titulo del Skill

Instrucciones para el agente sobre cuando y como usar las herramientas.
```

Restricciones del parser de OpenClaw:
- Frontmatter solo acepta claves de **una sola linea**
- `metadata` debe ser un **objeto JSON en una sola linea**
- Usar `{baseDir}` en instrucciones para referenciar la ruta de la carpeta del skill

### 3.3 Claves de frontmatter

#### Campos del estandar AgentSkills

| Clave | Obligatoria | Restricciones |
| --- | --- | --- |
| `name` | Si | Max 64 chars. Spec AgentSkills: letras minusculas, numeros y guiones (ej: `pdf-processing`). OpenClaw tambien acepta snake_case (ej: `hello_world`). Debe coincidir con directorio padre |
| `description` | Si | Max 1024 chars. No vacio. Describir que hace el skill y cuando usarlo |
| `license` | No | Nombre de licencia o referencia a archivo de licencia incluido |
| `compatibility` | No | Max 500 chars. Requisitos de entorno (producto, paquetes, red) |
| `metadata` | No | Mapa de string a string para metadata adicional no definida por la spec |
| `allowed-tools` | No | Lista delimitada por espacios de herramientas pre-aprobadas (experimental) |

Validacion del campo `name`:
- Valido: `pdf-processing`, `data-analysis`, `code-review`, `hello_world`
- Invalido: `PDF-Processing` (mayusculas), `-pdf` (inicia con guion), `pdf--processing` (guiones consecutivos)

Validacion del campo `description`:
- Bueno: `Extract PDF text, fill forms, merge files. Use when handling PDFs.`
- Deficiente: `Helps with PDFs.`

#### Campos extendidos de OpenClaw

| Clave | Obligatoria | Descripcion |
| --- | --- | --- |
| `homepage` | No | URL mostrada como "Website" en la UI de macOS |
| `user-invocable` | No | `true` (default) o `false`. Expone el skill como slash command |
| `disable-model-invocation` | No | `true` o `false` (default). Excluye skill del prompt del modelo |
| `command-dispatch` | No | `tool` — despacho directo a herramienta, sin pasar por el modelo |
| `command-tool` | No | Nombre de la herramienta a invocar cuando `command-dispatch: tool` |
| `command-arg-mode` | No | `raw` (default). Reenvio de argumentos crudos a la herramienta |

Cuando `command-dispatch: tool`, la herramienta recibe: `{ command: "<args>", commandName: "<slash command>", skillName: "<nombre>" }`.

### 3.4 Gating (filtros en tiempo de carga — OpenClaw)

Campos bajo `metadata.openclaw` (JSON en una linea):

| Campo | Funcion |
| --- | --- |
| `always: true` | Siempre incluir (salta otros filtros) |
| `emoji` | Emoji para la UI de macOS |
| `os` | Lista de plataformas elegibles: `darwin`, `linux`, `win32` |
| `requires.bins` | Lista de binarios requeridos en PATH |
| `requires.anyBins` | Al menos uno de estos binarios en PATH |
| `requires.env` | Variables de entorno requeridas (o provistas en config) |
| `requires.config` | Rutas de `openclaw.json` que deben ser truthy |
| `primaryEnv` | Env var asociada a `skills.entries.<name>.apiKey` |
| `install` | Array de especificaciones de instalador (brew/node/go/uv/download) |

Ejemplo completo:

```markdown
---
name: image-lab
description: Generate or edit images via a provider-backed image workflow
metadata: {"openclaw":{"requires":{"bins":["uv"],"env":["GEMINI_API_KEY"],"config":["browser.enabled"]},"primaryEnv":"GEMINI_API_KEY"}}
---
```

Si no hay `metadata.openclaw`, el skill siempre es elegible (salvo deshabilitacion en config o bloqueo por `allowBundled`).

### 3.5 Especificaciones de instalador (OpenClaw)

Tipos soportados: `brew`, `node`, `go`, `uv`, `download`.

Reglas de seleccion:
- Si hay multiples instaladores, el gateway elige uno preferido (brew cuando disponible, sino node)
- Si todos son `download`, OpenClaw lista cada entrada
- Los instaladores aceptan `os: ["darwin"|"linux"|"win32"]` para filtrar por plataforma
- Instalaciones node respetan `skills.install.nodeManager` en `openclaw.json` (default: npm; opciones: npm/pnpm/yarn/bun)
- Instalaciones Go: si `go` falta y `brew` esta disponible, instala Go via Homebrew primero
- Descargas: `url` (requerido), `archive` (tar.gz/tar.bz2/zip), `extract`, `stripComponents`, `targetDir` (default: `~/.openclaw/tools/<skillKey>`)

### 3.6 Progressive disclosure

Skills se estructuran para uso eficiente del contexto en 3 tiers:

| Tier | Que se carga | Cuando | Costo en tokens |
| --- | --- | --- | --- |
| 1. Catalogo | `name` + `description` | Inicio de sesion | ~50-100 tokens por skill |
| 2. Instrucciones | Cuerpo completo de `SKILL.md` | Cuando el skill se activa | <5000 tokens (recomendado) |
| 3. Recursos | Scripts, references, assets | Cuando las instrucciones los referencian | Variable |

Reglas:
- Mantener `SKILL.md` bajo **500 lineas**
- Mover material de referencia detallado a archivos separados en `references/` o directorios similares
- Indicar al agente **cuando** cargar cada archivo: "Leer `references/api-errors.md` si el API retorna un status no-200" es mas util que "ver references/ para detalles"

### 3.7 Referencias a archivos

Usar rutas relativas desde la raiz del skill:

```markdown
Ver [la guia de referencia](references/REFERENCE.md) para detalles.

Ejecutar el script de extraccion:
scripts/extract.py
```

Mantener referencias a un nivel de profundidad desde `SKILL.md`. Evitar cadenas de referencias profundamente anidadas.

### 3.8 Principios de diseno y mejores practicas

#### Construir desde experiencia real

Riesgo principal: generar un skill con un LLM sin proveer contexto especifico del dominio. El resultado son procedimientos genericos en vez de los patrones, edge cases y convenciones del proyecto que hacen valioso al skill.

Dos estrategias:
- **Extraer de tarea real** — Completar una tarea con el agente, proveyendo correcciones y contexto. Luego extraer el patron reutilizable. Prestar atencion a: pasos que funcionaron, correcciones hechas, formatos de input/output, contexto provisto.
- **Sintetizar desde artefactos existentes** — Alimentar un LLM con material especifico del proyecto: documentacion interna, runbooks, specs de API, comentarios de code review, historial de version control, casos de falla reales.

#### Gastar contexto sabiamente

- **Agregar lo que el agente no sabe, omitir lo que ya sabe** — No explicar que es un PDF ni como funciona HTTP. Enfocarse en convenciones del proyecto, procedimientos de dominio, edge cases no obvios, herramientas o APIs especificas.
- **Disenar unidades coherentes** — Un skill debe encapsular una unidad coherente de trabajo. Scope demasiado estrecho: multiples skills para una sola tarea. Scope demasiado amplio: dificil de activar con precision.
- **Apuntar a detalle moderado** — Skills exhaustivos pueden perjudicar. Guia concisa y paso a paso con un ejemplo funcional supera a documentacion exhaustiva.

#### Calibrar el nivel de control

- **Dar libertad** cuando multiples enfoques son validos y la tarea tolera variacion. Explicar el *por que* puede ser mas efectivo que directivas rigidas.
- **Ser prescriptivo** cuando operaciones son fragiles, la consistencia importa, o una secuencia especifica debe seguirse.
- **Proveer defaults, no menus** — Elegir un default y mencionar alternativas brevemente en vez de presentar opciones iguales.
- **Favorecer procedimientos sobre declaraciones** — Ensenar al agente *como abordar* una clase de problemas, no *que producir* para una instancia especifica.

#### Refinar con ejecucion real

Ejecutar el skill contra tareas reales, alimentar los resultados (todos, no solo fallos) de vuelta al proceso de creacion. Incluso una sola pasada de ejecutar-y-revisar mejora notablemente la calidad.

## 4. Desarrollo de skills

### 4.1 Procedimiento de creacion

1. Crear directorio del skill:
   ```bash
   mkdir -p ~/.openclaw/workspace/skills/mi-skill
   ```
2. Escribir `SKILL.md` con frontmatter + instrucciones
3. (Opcional) Agregar `scripts/`, `references/`, `assets/` segun necesidad
4. (Opcional) Definir schemas de herramientas custom en frontmatter o usar herramientas existentes del sistema (`exec`, `browser`, etc.)
5. Cargar el skill iniciando nueva sesion:
   ```bash
   /new          # desde chat
   openclaw gateway restart  # o reiniciar gateway
   ```
6. Verificar carga:
   ```bash
   openclaw skills list
   ```
7. Probar con mensaje de prueba:
   ```bash
   openclaw agent --message "mensaje que active el skill"
   ```

### 4.2 Ubicaciones y precedencia

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

### 4.3 Skills per-agent vs compartidos

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
      skills: ["github", "weather"]  // baseline compartido
    },
    list: [
      { id: "writer" },                          // hereda defaults
      { id: "docs", skills: ["docs-search"] },   // reemplaza defaults (NO hereda)
      { id: "sandbox-agent", skills: [] },        // sin skills
    ]
  }
}
```

Reglas:
- `agents.defaults.skills` define baseline heredado por agentes sin override
- `agents.list[].skills` **reemplaza** el baseline completo (no se mezcla con defaults)
- Omitir `skills` en un agente = hereda defaults; `skills: []` = sin skills
- Si el allowlist efectivo cambia para una sesion activa, OpenClaw refresca el session snapshot

### 4.4 Skills en plugins

Plugins declaran skills en `openclaw.plugin.json` (rutas relativas a la raiz del plugin). Los skills del plugin se cargan cuando el plugin esta habilitado y participan en las reglas de precedencia normales. Gating via `metadata.openclaw.requires.config` en la entrada de configuracion del plugin.

### 4.5 Scripts en skills

#### Comandos one-off

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

#### Scripts autocontenidos con dependencias inline

Varios lenguajes soportan declaracion de dependencias inline:

- **Python (PEP 723)**: bloque TOML en `# ///` markers, ejecutar con `uv run scripts/extract.py`
- **Deno**: importaciones `npm:` y `jsr:` con version, ejecutar con `deno run scripts/extract.ts`
- **Bun**: auto-instala paquetes faltantes, ejecutar con `bun run scripts/extract.ts`
- **Ruby**: `bundler/inline` con bloque `gemfile`, ejecutar con `ruby scripts/extract.rb`

#### Diseno de scripts para uso agentico

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
openclaw skills search "query"       # buscar en ClawHub
openclaw skills install <slug>       # instalar en workspace activo
openclaw skills install <slug> --version <version>
openclaw skills update <slug>        # actualizar uno
openclaw skills update --all         # actualizar todos
openclaw skills list                 # listar skills locales
openclaw skills list --eligible      # solo elegibles
openclaw skills info <name>          # detalle de un skill
openclaw skills check                # diagnosticar binarios/env/config faltantes
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
      nodeManager: "npm"     // npm | pnpm | yarn | bun
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
      skills: ["github", "weather"]    // allowlist baseline (omitir = sin restriccion)
    },
    list: [
      { id: "writer" },                         // hereda defaults.skills
      { id: "docs", skills: ["docs-search"] },  // reemplaza (no hereda)
      { id: "sandbox", skills: [] },            // sin skills
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

## 7. Testing y depuracion

### 7.1 Testing basico de skills

Procedimiento:

1. Verificar carga: `openclaw skills list`
2. Verificar elegibilidad: `openclaw skills list --eligible`
3. Diagnosticar requisitos faltantes: `openclaw skills check`
4. Probar invocacion:
   ```bash
   openclaw agent --message "mensaje que active el skill"
   ```
5. Probar como slash command (si `user-invocable: true`):
   ```
   /nombre_del_skill [argumentos]
   ```

### 7.2 Depuracion de carga

Diagnostico detallado de problemas de carga: ver §17.7.

### 7.3 Recarga de skills

- Iniciar nueva sesion: `/new` o `openclaw gateway restart`
- Hot reload automatico si `skills.load.watch: true` — cambios en `SKILL.md` se reflejan en el siguiente agent turn
- El session snapshot se congela al inicio; hot reload actualiza para el siguiente turn

### 7.4 Debug de slash commands

Comandos utiles:
- `/tools` — ver herramientas disponibles al agente en la sesion actual
- `/tools verbose` — agregar descripciones
- `/context detail` — ver tamano per-skill en el system prompt
- `/verbose on` — habilitar texto detallado de fallos de herramientas (solo para debug)

### 7.5 Optimizacion de descripciones (trigger evals)

La `description` lleva toda la carga del triggering. Si la descripcion no comunica cuando el skill es util, el agente no lo activara.

#### Principios para descripciones efectivas

- **Fraseo imperativo** — "Use this skill when..." en vez de "This skill does..."
- **Foco en intent del usuario, no en implementacion** — Describir lo que el usuario intenta lograr
- **Errar hacia lo explicito** — Listar contextos donde aplica, incluyendo casos donde el usuario no nombra el dominio: "even if they don't explicitly mention 'CSV' or 'analysis'"
- **Mantener conciso** — Unas frases a un parrafo corto. Limite duro: 1024 caracteres

#### Disenar queries de evaluacion

Crear set de ~20 queries etiquetadas (`should_trigger: true/false`):

- **Should-trigger** (8-10): variar fraseo, explicitud, detalle, complejidad. Las mas utiles son donde el skill ayudaria pero la conexion no es obvia.
- **Should-not-trigger** (8-10): priorizar **near-misses** que comparten keywords pero necesitan algo diferente. "Write a fibonacci function" no testea nada; "write a python script that reads a CSV and uploads each row to postgres" si.

#### Calcular trigger rate

Ejecutar cada query multiples veces (minimo 3) y calcular fraccion de ejecuciones donde el skill se activo.
- Should-trigger pasa si trigger rate > 0.5
- Should-not-trigger pasa si trigger rate < 0.5

#### Loop de optimizacion

1. Evaluar descripcion actual en sets train (60%) y validation (40%)
2. Identificar fallos en train set
3. Revisar descripcion generalizando (no agregar keywords especificas de queries fallidas)
4. Re-evaluar ambos sets
5. Repetir hasta convergencia (5 iteraciones usualmente suficientes)
6. Seleccionar mejor iteracion por pass rate del validation set

El skill `skill-creator` (`github.com/anthropics/skills/tree/main/skills/skill-creator`) automatiza este loop end-to-end.

### 7.6 Evaluacion de calidad de output (evals)

#### Estructura de test cases

Cada test case tiene: **prompt** (mensaje realista), **expected_output** (descripcion de exito), **files** (opcionales).

```json
{
  "skill_name": "csv-analyzer",
  "evals": [
    {
      "id": 1,
      "prompt": "I have a CSV of monthly sales data in data/sales_2025.csv. Can you find the top 3 months by revenue and make a bar chart?",
      "expected_output": "A bar chart image showing the top 3 months by revenue, with labeled axes and values.",
      "files": ["evals/files/sales_2025.csv"],
      "assertions": [
        "The output includes a bar chart image file",
        "The chart shows exactly 3 months",
        "Both axes are labeled",
        "The chart title or caption mentions revenue"
      ]
    }
  ]
}
```

#### Ejecucion de evals

Patron: ejecutar cada test case **con skill** y **sin skill** (baseline). Estructura de workspace:

```
mi-skill-workspace/
└── iteration-1/
    ├── eval-caso-1/
    │   ├── with_skill/    (outputs/, timing.json, grading.json)
    │   └── without_skill/ (outputs/, timing.json, grading.json)
    └── benchmark.json     (estadisticas agregadas)
```

Cada run en contexto limpio (subagente o sesion separada). Capturar `total_tokens` y `duration_ms`.

#### Assertions y grading

Buenas assertions: verificables ("The output file is valid JSON"), especificas ("The bar chart has labeled axes"), contables ("The report includes at least 3 recommendations").

Malas assertions: vagas ("The output is good"), fragiles ("The output uses exactly the phrase 'Total Revenue: $X'").

Grading: evaluar cada assertion como PASS/FAIL con evidencia concreta que cite el output. Requerir evidencia para PASS; no dar beneficio de la duda.

#### Benchmark agregado

```json
{
  "run_summary": {
    "with_skill": { "pass_rate": { "mean": 0.83 }, "tokens": { "mean": 3800 } },
    "without_skill": { "pass_rate": { "mean": 0.33 }, "tokens": { "mean": 2100 } },
    "delta": { "pass_rate": 0.50, "tokens": 1700 }
  }
}
```

El delta muestra costo (mas tokens) vs beneficio (mejor pass rate).

#### Analisis de patrones

- Eliminar assertions que siempre pasan en ambas configuraciones (no discriminan)
- Investigar assertions que siempre fallan en ambas (assertion rota o test case demasiado dificil)
- Estudiar assertions que pasan con skill pero fallan sin el (valor agregado del skill)
- Endurecer instrucciones cuando resultados son inconsistentes entre runs

#### Loop de iteracion

1. Dar senales de eval + `SKILL.md` actual a un LLM para proponer mejoras
2. Revisar y aplicar cambios
3. Re-ejecutar todos los test cases en nuevo `iteration-<N+1>/`
4. Gradear y agregar resultados
5. Revisar con humano. Repetir hasta satisfaccion.

### 7.7 Patrones de instrucciones efectivas

#### Secciones de gotchas

Contenido de mayor valor: hechos del entorno que desafian suposiciones razonables. No consejos genericos ("handle errors appropriately") sino correcciones concretas:

```markdown
## Gotchas

- La tabla `users` usa soft deletes. Queries deben incluir
  `WHERE deleted_at IS NULL` o resultados incluiran cuentas desactivadas.
- El user ID es `user_id` en la DB, `uid` en el auth service,
  y `accountId` en el billing API. Los tres refieren al mismo valor.
```

Cuando el agente comete un error que debes corregir, agregar la correccion a gotchas.

#### Templates para formato de output

Proveer templates cuando se necesita output en formato especifico. Templates cortos inline en `SKILL.md`; largos o condicionales en `assets/`.

#### Checklists para workflows multi-paso

Lista explicita ayuda al agente a trackear progreso y no saltar pasos:

```markdown
## Workflow de procesamiento

- [ ] Paso 1: Analizar formulario (`scripts/analyze_form.py`)
- [ ] Paso 2: Crear mapping de campos (`fields.json`)
- [ ] Paso 3: Validar mapping (`scripts/validate_fields.py`)
- [ ] Paso 4: Llenar formulario (`scripts/fill_form.py`)
- [ ] Paso 5: Verificar output (`scripts/verify_output.py`)
```

#### Validation loops

Instruir al agente a validar su propio trabajo antes de avanzar: hacer el trabajo, ejecutar validador, corregir, repetir hasta que pase.

#### Plan-validate-execute

Para operaciones batch o destructivas: crear plan intermedio en formato estructurado, validar contra fuente de verdad, ejecutar solo cuando validacion pasa. El ingrediente clave es un script de validacion que verifica el plan contra la fuente de verdad.

### 7.8 Testing en SDK de plugins

Para plugins que incluyen skills:
- Usar `sdk-testing` del SDK de plugins OpenClaw
- Tests unitarios para herramientas del plugin
- Verificar que skills se cargan correctamente cuando el plugin esta habilitado

## 8. Validacion y aprobaciones

### 8.1 Validacion de elegibilidad

OpenClaw filtra skills en tiempo de carga evaluando secuencialmente:
1. `always: true` — salta todos los filtros
2. `os` — plataforma actual debe estar en la lista
3. `requires.bins` — todos deben existir en PATH del host
4. `requires.anyBins` — al menos uno debe existir
5. `requires.env` — variable debe existir en entorno o estar provista en config
6. `requires.config` — ruta en `openclaw.json` debe ser truthy
7. `enabled` en config — `false` descarta
8. `allowBundled` — si definido, solo bundled listados pasan

### 8.2 Aprobaciones de ejecucion (exec approvals)

Sistema de exec approvals general: ver manual integral §7.4. Cuando un skill invoca herramientas de ejecucion (`exec`), el sistema de aprobaciones controla el acceso:

| Nivel | Comportamiento |
| --- | --- |
| `deny` | Deniega toda ejecucion |
| `allowlist` | Solo comandos en la lista de aprobacion permitidos; nuevos requieren aprobacion |
| `full` | Permite toda ejecucion sin aprobacion |

Configuracion gateway: `tools.exec.security` en `openclaw.json` o `/exec security=<nivel>` en runtime.

**Policy host-local** — ademas de la config del gateway, existe una policy local persistida en `~/.openclaw/exec-approvals.json` que puede forzar prompts de aprobacion aunque la config del gateway diga `full`. La **politica mas estricta prevalece** entre gateway config y host-local policy.

Campos de la policy host-local:

| Campo | Descripcion |
| --- | --- |
| `security` | `deny` / `allowlist` / `full` |
| `ask` | `off` / `on-miss` / `always` — cuando solicitar aprobacion interactiva |
| `askFallback` | `deny` / `allowlist` / `full` — fallback si no hay operador para aprobar |
| `strictInlineEval` | Controla evaluacion de scripts inline |

Allowlists per-agent: patrones glob case-insensitive en la entry del agente. Shell chains se evaluan comando por comando. Skills instalados via `skills.install` auto-registran sus CLIs en el allowlist.

Aprobacion interactiva: `/approve <id> allow-once|allow-always|deny`. Aprobaciones se pueden reenviar a canales de chat.

### 8.3 Herramientas elevadas

Modo elevated general: ver manual integral §7.4. Modo elevated (`/elevated on|off|ask|full`) habilita herramientas restringidas. `full` salta aprobaciones de exec.

Configuracion de allowlists:
- `tools.elevated.allowPatterns` — patrones de comandos permitidos
- `tools.elevated.denyPatterns` — patrones denegados

### 8.4 Deteccion de loops

Deteccion de invocaciones ciclicas de herramientas:
- Monitoreo de patrones repetitivos en llamadas tool
- Interrupcion automatica al detectar ciclo
- Alerta al operador con detalle del loop

## 9. Observabilidad y metricas

### 9.1 Impacto en tokens del system prompt

Cuando hay skills elegibles, OpenClaw inyecta una lista XML compacta en el system prompt.

Formula de costo (caracteres):

```
total = 195 + SUM(97 + len(name_escaped) + len(description_escaped) + len(location_escaped))
```

- Base overhead (solo cuando hay >=1 skill): 195 caracteres
- Per skill: 97 caracteres + longitud de valores XML-escaped (`name`, `description`, `location`)
- XML escaping expande `& < > " '` en entidades, incrementando longitud
- Estimacion aprox. OpenAI-style: ~4 chars/token, asi que 97 chars ≈ 24 tokens per skill + campos

### 9.2 Inspeccion de contexto

| Comando | Informacion |
| --- | --- |
| `/context` | Vista general del contexto |
| `/context detail` | Tamano per-file, per-tool, per-skill y system prompt |
| `/context json` | Exportacion JSON estructurada |
| `/tools` | Herramientas disponibles para el agente ahora |
| `/tools verbose` | Herramientas con descripciones |

### 9.3 Metricas de uso

- `/usage tokens` — tokens por respuesta
- `/usage full` — tokens + desglose
- `/usage cost` — resumen de costos desde logs de sesion
- `/status` — incluye uso/cuota del provider actual cuando usage tracking esta habilitado

### 9.4 Logging

OpenClaw genera logs estructurados del gateway:
- `openclaw logs` — ver logs del gateway
- `openclaw logs --follow` — seguir logs en tiempo real
- Logs incluyen carga de skills, evaluacion de elegibilidad, inyeccion de prompt

### 9.5 Health checks

- `openclaw health` — estado general del sistema
- `openclaw doctor` — diagnostico detallado
- `openclaw skills check` — diagnostico especifico de skills (binarios, env, config)

## 10. Seguridad

### 10.1 Skills de terceros como codigo no confiable

Regla fundamental: tratar skills de terceros como **codigo no confiable**. Leer el contenido antes de habilitar.

Skills a nivel de proyecto provienen del repositorio siendo trabajado, que puede ser no confiable (ej: proyecto open-source recien clonado). Considerar gatear la carga de skills de proyecto con verificacion de confianza — solo cargar si el usuario ha marcado la carpeta como confiable.

### 10.2 Validacion de rutas

- Discovery de workspace y extra-dir solo acepta raices de skills y archivos `SKILL.md` cuya **realpath resuelta** queda dentro de la raiz configurada
- Previene symlink traversal y escapes de directorio

### 10.3 Inyeccion de secretos

- `skills.entries.<name>.env` y `skills.entries.<name>.apiKey` inyectan secretos en `process.env` del **host** para ese agent turn (no en el sandbox)
- Mantener secretos fuera de prompts y logs
- SecretRef soporta: string plano o objeto `{ source: "env", provider: "default", id: "VARIABLE" }`

### 10.4 Sandboxing

Cuando la sesion esta en sandbox (Docker), procesos de skills corren dentro del contenedor. El sandbox **no hereda** `process.env` del host. Binarios requeridos por `requires.bins` deben existir dentro del contenedor. Configuracion general de sandbox: ver manual integral `urn:agengai:kb:openclaw-manual-integral` §7.3.

### 10.5 Dangerous-code scanner

Las instalaciones de dependencias respaldadas por el Gateway (`skills.install`, onboarding, y la UI de Skills en macOS) ejecutan el **dangerous-code scanner** antes de ejecutar metadata de instaladores. Hallazgos `critical` bloquean por defecto salvo override explicito del caller; hallazgos `suspicious` solo advierten.

`openclaw skills install <slug>` (descarga desde ClawHub) es diferente: descarga la carpeta del skill al workspace y **no** usa el path de installer-metadata, por lo que no dispara el scanner.

### 10.6 Controles de ejecucion

- `tools.exec.security`: `deny`, `allowlist`, `full`
- `~/.openclaw/exec-approvals.json`: policy host-local que puede ser mas estricta que la config gateway (la mas estricta prevalece)
- `tools.elevated`: controla acceso a herramientas de shell del host
- Exec approvals interactivas: `/approve <id> allow-once|allow-always|deny`
- Allowlists con patrones para comandos permitidos/denegados

### 10.7 Modelo de amenazas para skills

Amenazas principales:
- **Inyeccion de prompt**: skill con instrucciones maliciosas que manipulan al agente
- **Inyeccion de comandos**: skill que usa `exec` sin sanitizar input del usuario
- **Exfiltracion de secretos**: skill que expone env vars en outputs o logs
- **Escalacion de privilegios**: skill que abusa de modo elevated
- **Symlink traversal**: skill con rutas que escapan de la raiz configurada

Mitigaciones:
- Leer skills antes de habilitar
- Sandbox para inputs no confiables
- Exec approvals con allowlists
- Validacion de realpath en discovery
- Secretos inyectados solo en host, no en sandbox

### 10.8 Seguridad en ClawHub

- Publicacion requiere cuenta GitHub con minimo una semana de antiguedad
- Cualquier usuario puede reportar un skill
- Skills con mas de 3 reportes unicos se ocultan automaticamente
- Moderadores pueden: ver ocultos, desocultar, eliminar, banear usuarios
- Abuso del sistema de reportes puede resultar en ban

## 11. Gobernanza y administracion

### 11.1 Control de acceso a comandos de skills

Autorizacion de slash commands (incluyendo skills):
- `commands.allowFrom` — allowlist per-provider para autorizacion de comandos
- `commands.useAccessGroups` (default: true) — usar allowlists/politicas de canal
- Senders no autorizados ven slash commands como texto plano

### 11.2 Skills como slash commands

Skills con `user-invocable: true` se exponen como slash commands:
- Nombres sanitizados a `a-z0-9_` (max 32 chars)
- Colisiones resueltas con sufijos numericos (`_2`)
- `/skill <name> [input]` para invocar por nombre (util cuando limites de comandos nativos impiden comandos per-skill)
- Registro nativo en Discord/Telegram (`commands.nativeSkills: "auto"`)

### 11.3 Allowlist de bundled skills

`skills.allowBundled` restringe skills bundled elegibles. Solo afecta bundled; managed/workspace no se filtran por esta lista.

### 11.4 Habilitacion/deshabilitacion por config

`skills.entries.<name>.enabled: false` deshabilita cualquier skill independientemente de su origen.

### 11.5 Administracion via macOS UI

La app macOS expone skills via el gateway (no parsea skills localmente):
- `skills.status` retorna todos los skills + elegibilidad + requisitos faltantes
- `skills.install` ejecuta instaladores en el host del gateway
- `skills.update` modifica `enabled`, `apiKey`, `env`
- En modo remoto, install + config ocurren en el host del gateway, no en el Mac local

### 11.6 Configuracion remota

- `/config set skills.entries.<name>.enabled=true` — habilitar via chat (requiere `commands.config: true`)
- `/config set skills.entries.<name>.apiKey="KEY"` — inyectar API key via chat
- `/debug set` — override runtime-only (no persiste a disco)

## 12. Optimizacion de rendimiento

### 12.1 Session snapshot

OpenClaw congela la lista de skills elegibles al iniciar sesion y la reutiliza en turns subsiguientes. Cambios en skills o config toman efecto en la siguiente sesion nueva.

Excepcion: si `skills.load.watch: true`, el hot reload actualiza la lista para el siguiente agent turn dentro de la misma sesion, nunca en el turno actual.

### 12.2 Minimizar impacto en tokens

Estrategias:
- Deshabilitar skills no necesarios: `skills.entries.<name>.enabled: false`
- Usar `allowBundled` para restringir bundled skills
- Escribir `name` y `description` cortos y precisos (max 1024 chars para description)
- Evitar caracteres que requieren XML escaping (`& < > " '`)
- Usar `disable-model-invocation: true` para skills que solo deben responder a slash commands
- Mantener `SKILL.md` bajo 500 lineas y 5000 tokens
- Mover material de referencia a `references/` para carga bajo demanda

### 12.3 Reducir latencia de carga

- `skills.load.watch: true` con `watchDebounceMs: 250` (default) evita recargas excesivas
- Mantener carpetas de skills limpias (menos archivos = escaneo mas rapido)
- `extraDirs` agrega overhead de escaneo; usar solo cuando necesario

### 12.4 Skills en nodos remotos macOS

Si el gateway corre en Linux pero un nodo macOS esta conectado con `system.run` permitido, OpenClaw puede tratar skills macOS-only como elegibles cuando los binarios requeridos estan presentes en ese nodo. El agente ejecuta esos skills via la herramienta `exec` con `host=node` (no `nodes.run`). Requisito: exec approvals security no puede estar en `deny`.

Advertencia: si el nodo macOS se desconecta, los skills pueden permanecer visibles en el catalogo, pero las invocaciones fallan hasta que el nodo reconecte.

## 13. Interoperabilidad

### 13.1 Estandar AgentSkills y ecosistema

AgentSkills es un formato abierto desarrollado originalmente por Anthropic. La especificacion define el formato de `SKILL.md`, campos de frontmatter y convenciones de directorio. El estandar esta abierto a contribuciones del ecosistema.

Productos que soportan AgentSkills: Claude Code, Claude, VS Code (GitHub Copilot), Cursor, OpenAI Codex, Gemini CLI, Junie (JetBrains), OpenHands, Roo Code, Goose (Block), Amp, Letta, Firebender, Mux (Coder), OpenCode, Databricks, Spring AI, Kiro (AWS), Laravel Boost, TRAE (ByteDance), Factory, Piebald, Mistral Vibe, Command Code, Snowflake, Qodo, Ona, VT Code, Emdash, Agentman.

Skills disenados para el estandar AgentSkills funcionan en cualquier cliente compatible. OpenClaw agrega extensiones propias via `metadata.openclaw` sin romper compatibilidad.

### 13.2 Convenciones cross-client de discovery

Convencion universal: skills a nivel de proyecto en `.agents/skills/` son descubiertos automaticamente por multiples clientes. OpenClaw tambien escanea `.claude/skills/` para compatibilidad pragmatica.

Directorios adicionales escaneados por algunas implementaciones: ancestros hasta raiz git (monorepos), directorios XDG, rutas configuradas por el usuario.

Precedencia universal: **skills de proyecto sobreescriben skills de usuario**.

Colision de nombres dentro del mismo scope: first-found o last-found (consistente). Registrar warning cuando ocurre shadowing.

### 13.3 Implementacion de soporte para skills (client guide)

#### Discovery

Escanear subdirectorios que contengan un archivo exactamente nombrado `SKILL.md`. Reglas practicas:
- Saltar `.git/`, `node_modules/`
- Opcionalmente respetar `.gitignore`
- Limites razonables (max profundidad 4-6, max 2000 directorios)

#### Parsing de SKILL.md

1. Encontrar `---` de apertura y cierre
2. Parsear bloque YAML entre ellos. Extraer `name` y `description` (requeridos) + campos opcionales
3. Todo despues del `---` de cierre, trimmed, es el cuerpo del skill

Validacion leniente:
- Name no coincide con directorio padre → warn, cargar igual
- Name excede 64 chars → warn, cargar igual
- Description faltante o vacia → saltar skill, logear error
- YAML completamente imparseable → saltar skill, logear error

Manejo de YAML malformado: considerar fallback que envuelva valores con colons sin quotear en comillas antes de re-parsear.

#### Disclosure al modelo

Construir catalogo compacto para system prompt:

```xml
<available_skills>
  <skill>
    <name>pdf-processing</name>
    <description>Extract PDF text, fill forms, merge files. Use when handling PDFs.</description>
    <location>/home/user/.agents/skills/pdf-processing/SKILL.md</location>
  </skill>
</available_skills>
```

Cada skill agrega ~50-100 tokens al catalogo. Si no hay skills, omitir catalogo e instrucciones completamente.

Skills filtrados (deshabilitados, sin permiso, `disable-model-invocation`) deben **ocultarse del catalogo**, no listarse y bloquear en activacion.

#### Activacion

Dos mecanismos:
- **File-read activation** — El modelo llama su herramienta de lectura de archivos con la ruta del `SKILL.md`. Sin infraestructura adicional.
- **Dedicated tool activation** — Herramienta `activate_skill` que toma nombre y retorna contenido. Ventajas: controlar contenido retornado, envolver en tags estructurados, listar recursos bundled, enforcer permisos, trackear activacion.

Activacion explicita por usuario: slash commands (`/skill-name`) interceptados por el harness.

#### Gestion de contexto de skills

- **Proteger de compaction** — Contenido de skills inyectado no debe podarse cuando la ventana de contexto se llena. Instrucciones de skill son guia conductual durable; perderlas degrada silenciosamente al agente.
- **Deduplicar activaciones** — Trackear skills activados en sesion actual; saltar re-inyeccion si ya esta en contexto.
- **Delegacion a subagente** (opcional) — En vez de inyectar en conversacion principal, ejecutar skill en sesion de subagente separada que retorna resumen.

### 13.4 Skills en plugins

Plugins declaran skills en `openclaw.plugin.json`:

```json
{
  "skills": ["skills/mi-skill"]
}
```

Rutas relativas a la raiz del plugin. Skills del plugin:
- Se cargan cuando el plugin esta habilitado
- Participan en reglas normales de precedencia
- Se pueden gatear via `metadata.openclaw.requires.config`

### 13.5 Skills y herramientas multi-canal

Herramientas que funcionan cross-channel:
- `exec` — ejecucion de comandos (host o sandbox)
- `browser` — navegacion web
- `web_fetch` — busqueda web
- Herramientas de canal (Telegram, Discord, Slack, WhatsApp, etc.)
- Herramientas de plugin (expandibles)

### 13.6 Slash commands nativos por canal

| Canal | Comandos nativos de skills | Config |
| --- | --- | --- |
| Discord | Auto | `channels.discord.commands.nativeSkills` |
| Telegram | Auto | `channels.telegram.commands.nativeSkills` |
| Slack | Off (requiere crear slash command por skill) | `channels.slack.commands.nativeSkills` |
| WhatsApp, Signal, iMessage | Solo texto | N/A (text commands siempre funcionan) |

### 13.7 Subagentes y skills

En arquitectura multi-agente:
- Cada subagente hereda la configuracion de skills del agente padre o define la propia
- Skills de workspace son per-agent (cada workspace tiene su directorio `skills/`)
- Skills compartidos (`~/.openclaw/skills/`) visibles para todos los agentes del nodo

### 13.8 Integracion MCP

Skills pueden coexistir con servidores MCP configurados en OpenClaw:
- `/mcp set` gestiona servidores MCP
- Skills y herramientas MCP son visibles simultaneamente al agente
- No hay conflicto de namespace: skills usan `name`, MCP usa identificadores de servidor

## 14. Orquestacion multi-agente

### 14.1 Skills per-agent vs compartidos

Ubicaciones, precedencia y alcance per-agent vs compartido: ver §4.2 y §4.3.

### 14.2 Sandboxing multi-agente

Para sesiones sandboxed con multiples agentes:
- Cada sesion puede tener su propio workspace bajo `agents.defaults.sandbox.workspaceRoot`
- Skills del workspace sandbox son independientes del workspace principal
- Herramientas sandbox incluyen: `exec`, `apply_patch`, `write`, `read` (adaptadas al entorno aislado)

### 14.3 Skills en cron y automatizacion

Skills estan disponibles en sesiones de cron jobs y automatizacion:
- `openclaw cron` gestiona tareas programadas
- Hooks permiten ejecutar logica pre/post en respuestas del agente
- Webhooks pueden disparar sesiones que usan skills
- Standing orders definen instrucciones persistentes que complementan skills

### 14.4 Delegacion entre agentes

Un agente puede delegar trabajo a subagentes que tienen sus propios skills:
- `/subagents spawn` — crear subagente con workspace independiente
- `/subagents steer` — redirigir subagente a nueva tarea
- Subagentes heredan elegibilidad de skills segun su workspace y config

Patron avanzado: en vez de inyectar instrucciones de skill en la conversacion principal, ejecutar el skill en un **subagente dedicado** que recibe las instrucciones, realiza la tarea, y retorna un resumen. Util cuando el workflow del skill es complejo y se beneficia de una sesion enfocada.

## 15. Documentacion de workspace para skills

### 15.1 Archivos de bootstrap del agente

Archivos en `agents.defaults.workspace` que contextualizan skills:

| Archivo | Funcion respecto a skills |
| --- | --- |
| `AGENTS.md` | Instrucciones operativas — puede referenciar skills disponibles |
| `SOUL.md` | Persona y limites — define como el agente usa skills |
| `TOOLS.md` | Notas de herramientas — documenta convenciones de uso de skills |
| `USER.md` | Perfil del usuario — informa preferencias que skills deben respetar |
| `IDENTITY.md` | Nombre/emoji/vibe del agente |
| `BOOTSTRAP.md` | Ritual de primera ejecucion (eliminado despues de completarse) |

Archivos inyectados en el contexto del agente en el primer turn de cada sesion. Archivos vacios se omiten; archivos grandes se truncan.

### 15.2 Documentacion del SKILL.md

Mejores practicas para instrucciones: ver §3.6 (progressive disclosure), §3.8 (principios de diseno) y §7.7 (patrones efectivos).

### 15.3 Templates de referencia

OpenClaw provee templates en `reference/templates/`:
- `AGENTS.md`, `AGENTS.dev.md` — instrucciones operativas
- `SOUL.md`, `SOUL.dev.md` — persona
- `TOOLS.md`, `TOOLS.dev.md` — notas de herramientas
- `USER.md`, `USER.dev.md` — perfil de usuario
- `IDENTITY.md`, `IDENTITY.dev.md` — identidad
- `BOOT.md`, `BOOTSTRAP.md`, `HEARTBEAT.md` — bootstrap y heartbeat

Estos templates orientan la documentacion que complementa los skills del agente.

## 16. Gestion del ciclo de vida

### 16.1 Ciclo de vida de un skill

```
Crear -> Cargar -> Probar -> Evaluar -> Publicar -> Actualizar -> Deprecar/Eliminar
```

| Fase | Accion | Comando/Metodo |
| --- | --- | --- |
| Crear | Escribir `SKILL.md` en directorio + scripts/references opcionales | Manual |
| Validar formato | Verificar conformidad con spec AgentSkills | `skills-ref validate ./mi-skill` |
| Cargar | Iniciar sesion o hot reload | `/new` o watcher automatico |
| Probar | Verificar eligibilidad + invocacion | `openclaw skills check` + `openclaw agent --message` |
| Evaluar triggering | Optimizar description con trigger evals | Script de trigger rate (§7.5) |
| Evaluar calidad | Test cases con assertions y grading | Eval framework (§7.6) |
| Publicar | Subir a ClawHub | `clawhub publish` o `clawhub sync` |
| Instalar | Descargar de ClawHub | `openclaw skills install` o `clawhub install` |
| Actualizar | Nueva version | `openclaw skills update` o `clawhub update` |
| Deshabilitar | Quitar de elegibilidad sin eliminar | `skills.entries.<name>.enabled: false` |
| Eliminar | Borrar directorio o `clawhub delete` | Manual o CLI |

### 16.2 Versionado

- Semver (`major.minor.patch`)
- Tags mutables (`latest`, custom) que apuntan a versiones
- Changelogs por version en ClawHub
- Deteccion de cambios via hash de contenido

### 16.3 Actualizaciones

```bash
openclaw skills update --all    # actualizar todos via OpenClaw
clawhub update --all            # actualizar todos via ClawHub CLI
```

Comportamiento:
- Compara hash local vs versiones del registro
- Si archivos locales no coinciden con ninguna version publicada, requiere `--force`
- Actualizaciones se reflejan en la siguiente sesion (o turn si watcher activo)

### 16.4 Migracion

Al migrar entre versiones de OpenClaw:
- Skills de workspace se preservan (residen en directorio del usuario)
- Skills bundled se actualizan con la distribucion
- Config en `openclaw.json` persiste; validar compatibilidad
- `.clawhub/lock.json` rastrea versiones instaladas

### 16.5 Backup y restauracion

- `openclaw backup` respalda configuracion y workspace (incluye skills)
- Publicar skills a ClawHub como backup distribuido
- `clawhub sync --all` sube skills locales al registro

## 17. Resiliencia y recuperacion

### 17.1 Tolerancia a fallos de skills

| Escenario | Comportamiento |
| --- | --- |
| Binario faltante | Skill no elegible; agente continua sin el skill |
| Env var faltante | Skill no elegible si esta en `requires.env` |
| Skill crashea en ejecucion | Agente recibe error de herramienta; puede reintentar o cambiar estrategia |
| Nodo remoto macOS se desconecta | Skills permanecen visibles; invocaciones fallan hasta reconexion |
| ClawHub no disponible | Skills locales funcionan normalmente; install/update fallan |

### 17.2 Hot reload

Hot reload refresca skills sin reiniciar gateway. Detalles: ver §7.3.

### 17.3 Session snapshot como proteccion

Session snapshot congela skills elegibles al inicio de sesion. Detalles: ver §12.1.

### 17.4 Proteccion de contexto contra compaction

Contenido de skills inyectado en el contexto conversacional no debe podarse cuando la ventana de contexto se llena:
- Instrucciones de skill son guia conductual durable
- Perder instrucciones mid-conversacion degrada silenciosamente al agente sin error visible
- Marcar outputs de herramienta de skill como protegidos para que el algoritmo de pruning los omita
- Usar tags estructurados para identificar contenido de skill durante compaction

### 17.5 Deduplicacion de activaciones

Trackear skills activados en la sesion actual. Si el modelo o usuario intenta cargar un skill ya en contexto, saltar la re-inyeccion para evitar instrucciones duplicadas.

### 17.6 Deteccion y prevencion de loops

Deteccion activa:
- OpenClaw detecta patrones repetitivos
- Interrumpe la ejecucion automaticamente
- Reporta detalle del loop al operador
- Previene consumo descontrolado de tokens y recursos

### 17.7 Diagnostico de fallos

Herramientas de diagnostico para skills:

| Herramienta | Uso |
| --- | --- |
| `openclaw skills check` | Verificar binarios, env vars, config para todos los skills |
| `openclaw skills list --eligible` | Confirmar que skills deseados son elegibles |
| `openclaw doctor` | Diagnostico general del sistema (incluye skills) |
| `/context detail` | Verificar que skills estan presentes en el system prompt |
| `/tools verbose` | Confirmar herramientas accesibles al agente |
| `openclaw logs --follow` | Revisar logs de carga y evaluacion de skills |
| `skills-ref validate ./mi-skill` | Validar formato contra spec AgentSkills |

### 17.8 Rollback de skills

Opciones de rollback:
- `clawhub install <slug> --version <version>` — instalar version especifica
- Mover tags en ClawHub para apuntar a version anterior
- Restaurar desde backup: `openclaw backup` preserva workspace con skills
- Deshabilitar temporalmente: `skills.entries.<name>.enabled: false`

## 18. Referencia rapida de comandos

### 18.1 CLI de OpenClaw

| Comando | Funcion |
| --- | --- |
| `openclaw skills search "query"` | Buscar en ClawHub |
| `openclaw skills install <slug>` | Instalar skill |
| `openclaw skills update --all` | Actualizar todos |
| `openclaw skills list` | Listar skills locales |
| `openclaw skills list --eligible` | Solo elegibles |
| `openclaw skills info <name>` | Detalle de un skill |
| `openclaw skills check` | Diagnosticar requisitos |

### 18.2 ClawHub CLI

| Comando | Funcion |
| --- | --- |
| `clawhub login` | Autenticar |
| `clawhub search "query"` | Buscar |
| `clawhub install <slug>` | Instalar |
| `clawhub update --all` | Actualizar todos |
| `clawhub list` | Listar instalados |
| `clawhub publish <path>` | Publicar skill |
| `clawhub sync --all` | Scan + publish |
| `clawhub delete <slug> --yes` | Eliminar |

### 18.3 Validacion y testing

| Comando | Funcion |
| --- | --- |
| `skills-ref validate ./mi-skill` | Validar formato AgentSkills |
| `openclaw agent --message "..."` | Probar invocacion de skill |
| Script trigger eval (§7.5) | Evaluar trigger rate de description |
| Eval framework (§7.6) | Evaluar calidad de output con assertions |

### 18.4 Slash commands en chat

| Comando | Funcion |
| --- | --- |
| `/skill <name> [input]` | Invocar skill por nombre |
| `/tools` | Ver herramientas disponibles |
| `/tools verbose` | Herramientas con descripciones |
| `/context detail` | Tamano per-skill en prompt |
| `/new` | Nueva sesion (recarga skills) |
| `/approve <id> allow-once` | Aprobar ejecucion |
| `/elevated on` | Habilitar herramientas elevadas |
| `/exec` | Ver/cambiar configuracion de ejecucion |

### 18.5 Configuracion clave

| Path en `openclaw.json` | Funcion |
| --- | --- |
| `skills.entries.<name>.enabled` | Habilitar/deshabilitar skill |
| `skills.entries.<name>.env` | Variables de entorno |
| `skills.entries.<name>.apiKey` | API key (string o SecretRef) |
| `skills.allowBundled` | Allowlist de bundled skills |
| `skills.load.extraDirs` | Directorios adicionales |
| `skills.load.watch` | Hot reload |
| `skills.install.nodeManager` | Gestor de paquetes |
