---
_manifest:
  urn: urn:agengai:kb:openclaw-skills-manual
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
    shard_index: 1
    shard_count: 5
    shard_root_urn: urn:agengai:kb:openclaw-skills-manual
relations:
  cites:
  - urn:agengai:kb:openclaw-manual-integral
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

## 3.1 Estructura de directorio

Un skill es un directorio con, como minimo, un archivo `SKILL.md`:

```
mi-skill/
├── SKILL.md # Requerido: metadata + instrucciones
├── scripts/ # Opcional: codigo ejecutable
├── references/ # Opcional: documentacion auxiliar
├── assets/ # Opcional: templates, recursos estaticos
└── ... # Cualquier archivo o directorio adicional
```

Directorios opcionales:
- **`scripts/`** — Codigo ejecutable que el agente puede correr. Scripts deben ser autocontenidos o documentar dependencias explicitamente. Incluir mensajes de error utiles.
- **`references/`** — Documentacion adicional que el agente lee bajo demanda: `REFERENCE.md`, `FORMS.md`, archivos de dominio (`finance.md`, `legal.md`). Mantener archivos individuales enfocados para minimizar uso de contexto.
- **`assets/`** — Recursos estaticos: templates de documentos, imagenes, esquemas, tablas de lookup.

## 3.2 Formato SKILL.md

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

## 3.3 Claves de frontmatter

### Campos del estandar AgentSkills

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

### Campos extendidos de OpenClaw

| Clave | Obligatoria | Descripcion |
| --- | --- | --- |
| `homepage` | No | URL mostrada como "Website" en la UI de macOS |
| `user-invocable` | No | `true` (default) o `false`. Expone el skill como slash command |
| `disable-model-invocation` | No | `true` o `false` (default). Excluye skill del prompt del modelo |
| `command-dispatch` | No | `tool` — despacho directo a herramienta, sin pasar por el modelo |
| `command-tool` | No | Nombre de la herramienta a invocar cuando `command-dispatch: tool` |
| `command-arg-mode` | No | `raw` (default). Reenvio de argumentos crudos a la herramienta |

Cuando `command-dispatch: tool`, la herramienta recibe: `{ command: "<args>", commandName: "<slash command>", skillName: "<nombre>" }`.

## 3.4 Gating (filtros en tiempo de carga — OpenClaw)

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

## 3.5 Especificaciones de instalador (OpenClaw)

Tipos soportados: `brew`, `node`, `go`, `uv`, `download`.

Reglas de seleccion:
- Si hay multiples instaladores, el gateway elige uno preferido (brew cuando disponible, sino node)
- Si todos son `download`, OpenClaw lista cada entrada
- Los instaladores aceptan `os: ["darwin"|"linux"|"win32"]` para filtrar por plataforma
- Instalaciones node respetan `skills.install.nodeManager` en `openclaw.json` (default: npm; opciones: npm/pnpm/yarn/bun)
- Instalaciones Go: si `go` falta y `brew` esta disponible, instala Go via Homebrew primero
- Descargas: `url` (requerido), `archive` (tar.gz/tar.bz2/zip), `extract`, `stripComponents`, `targetDir` (default: `~/.openclaw/tools/<skillKey>`)

## 3.6 Progressive disclosure

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

## 3.7 Referencias a archivos

Usar rutas relativas desde la raiz del skill:

```markdown
Ver [la guia de referencia](references/REFERENCE.md) para detalles.

Ejecutar el script de extraccion:
scripts/extract.py
```

Mantener referencias a un nivel de profundidad desde `SKILL.md`. Evitar cadenas de referencias profundamente anidadas.

## 3.8 Principios de diseno y mejores practicas

### Construir desde experiencia real

Riesgo principal: generar un skill con un LLM sin proveer contexto especifico del dominio. El resultado son procedimientos genericos en vez de los patrones, edge cases y convenciones del proyecto que hacen valioso al skill.

Dos estrategias:
- **Extraer de tarea real** — Completar una tarea con el agente, proveyendo correcciones y contexto. Luego extraer el patron reutilizable. Prestar atencion a: pasos que funcionaron, correcciones hechas, formatos de input/output, contexto provisto.
- **Sintetizar desde artefactos existentes** — Alimentar un LLM con material especifico del proyecto: documentacion interna, runbooks, specs de API, comentarios de code review, historial de version control, casos de falla reales.

### Gastar contexto sabiamente

- **Agregar lo que el agente no sabe, omitir lo que ya sabe** — No explicar que es un PDF ni como funciona HTTP. Enfocarse en convenciones del proyecto, procedimientos de dominio, edge cases no obvios, herramientas o APIs especificas.
- **Disenar unidades coherentes** — Un skill debe encapsular una unidad coherente de trabajo. Scope demasiado estrecho: multiples skills para una sola tarea. Scope demasiado amplio: dificil de activar con precision.
- **Apuntar a detalle moderado** — Skills exhaustivos pueden perjudicar. Guia concisa y paso a paso con un ejemplo funcional supera a documentacion exhaustiva.

### Calibrar el nivel de control

- **Dar libertad** cuando multiples enfoques son validos y la tarea tolera variacion. Explicar el *por que* puede ser mas efectivo que directivas rigidas.
- **Ser prescriptivo** cuando operaciones son fragiles, la consistencia importa, o una secuencia especifica debe seguirse.
- **Proveer defaults, no menus** — Elegir un default y mencionar alternativas brevemente en vez de presentar opciones iguales.
- **Favorecer procedimientos sobre declaraciones** — Ensenar al agente *como abordar* una clase de problemas, no *que producir* para una instancia especifica.

### Refinar con ejecucion real

Ejecutar el skill contra tareas reales, alimentar los resultados (todos, no solo fallos) de vuelta al proceso de creacion. Incluso una sola pasada de ejecutar-y-revisar mejora notablemente la calidad.
