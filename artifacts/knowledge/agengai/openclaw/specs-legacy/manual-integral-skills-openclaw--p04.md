---
_manifest:
  urn: urn:agengai:kb:openclaw-skills-manual-p04
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
    shard_index: 4
    shard_count: 5
    shard_root_urn: urn:agengai:kb:openclaw-skills-manual
relations:
  cites:
  - urn:agengai:kb:openclaw-manual-integral
---

# Manual Integral de Skills en OpenClaw - Parte 04

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

## 13.1 Estandar AgentSkills y ecosistema

AgentSkills es un formato abierto desarrollado originalmente por Anthropic. La especificacion define el formato de `SKILL.md`, campos de frontmatter y convenciones de directorio. El estandar esta abierto a contribuciones del ecosistema.

Productos que soportan AgentSkills: Claude Code, Claude, VS Code (GitHub Copilot), Cursor, OpenAI Codex, Gemini CLI, Junie (JetBrains), OpenHands, Roo Code, Goose (Block), Amp, Letta, Firebender, Mux (Coder), OpenCode, Databricks, Spring AI, Kiro (AWS), Laravel Boost, TRAE (ByteDance), Factory, Piebald, Mistral Vibe, Command Code, Snowflake, Qodo, Ona, VT Code, Emdash, Agentman.

Skills disenados para el estandar AgentSkills funcionan en cualquier cliente compatible. OpenClaw agrega extensiones propias via `metadata.openclaw` sin romper compatibilidad.

## 13.2 Convenciones cross-client de discovery

Convencion universal: skills a nivel de proyecto en `.agents/skills/` son descubiertos automaticamente por multiples clientes. OpenClaw tambien escanea `.claude/skills/` para compatibilidad pragmatica.

Directorios adicionales escaneados por algunas implementaciones: ancestros hasta raiz git (monorepos), directorios XDG, rutas configuradas por el usuario.

Precedencia universal: **skills de proyecto sobreescriben skills de usuario**.

Colision de nombres dentro del mismo scope: first-found o last-found (consistente). Registrar warning cuando ocurre shadowing.

## 13.3 Implementacion de soporte para skills (client guide)

### Discovery

Escanear subdirectorios que contengan un archivo exactamente nombrado `SKILL.md`. Reglas practicas:
- Saltar `.git/`, `node_modules/`
- Opcionalmente respetar `.gitignore`
- Limites razonables (max profundidad 4-6, max 2000 directorios)

### Parsing de SKILL.md

1. Encontrar `---` de apertura y cierre
2. Parsear bloque YAML entre ellos. Extraer `name` y `description` (requeridos) + campos opcionales
3. Todo despues del `---` de cierre, trimmed, es el cuerpo del skill

Validacion leniente:
- Name no coincide con directorio padre → warn, cargar igual
- Name excede 64 chars → warn, cargar igual
- Description faltante o vacia → saltar skill, logear error
- YAML completamente imparseable → saltar skill, logear error

Manejo de YAML malformado: considerar fallback que envuelva valores con colons sin quotear en comillas antes de re-parsear.

### Disclosure al modelo

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

### Activacion

Dos mecanismos:
- **File-read activation** — El modelo llama su herramienta de lectura de archivos con la ruta del `SKILL.md`. Sin infraestructura adicional.
- **Dedicated tool activation** — Herramienta `activate_skill` que toma nombre y retorna contenido. Ventajas: controlar contenido retornado, envolver en tags estructurados, listar recursos bundled, enforcer permisos, trackear activacion.

Activacion explicita por usuario: slash commands (`/skill-name`) interceptados por el harness.

### Gestion de contexto de skills

- **Proteger de compaction** — Contenido de skills inyectado no debe podarse cuando la ventana de contexto se llena. Instrucciones de skill son guia conductual durable; perderlas degrada silenciosamente al agente.
- **Deduplicar activaciones** — Trackear skills activados en sesion actual; saltar re-inyeccion si ya esta en contexto.
- **Delegacion a subagente** (opcional) — En vez de inyectar en conversacion principal, ejecutar skill en sesion de subagente separada que retorna resumen.

## 13.4 Skills en plugins

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

## 13.5 Skills y herramientas multi-canal

Herramientas que funcionan cross-channel:
- `exec` — ejecucion de comandos (host o sandbox)
- `browser` — navegacion web
- `web_fetch` — busqueda web
- Herramientas de canal (Telegram, Discord, Slack, WhatsApp, etc.)
- Herramientas de plugin (expandibles)

## 13.6 Slash commands nativos por canal

| Canal | Comandos nativos de skills | Config |
| --- | --- | --- |
| Discord | Auto | `channels.discord.commands.nativeSkills` |
| Telegram | Auto | `channels.telegram.commands.nativeSkills` |
| Slack | Off (requiere crear slash command por skill) | `channels.slack.commands.nativeSkills` |
| WhatsApp, Signal, iMessage | Solo texto | N/A (text commands siempre funcionan) |
