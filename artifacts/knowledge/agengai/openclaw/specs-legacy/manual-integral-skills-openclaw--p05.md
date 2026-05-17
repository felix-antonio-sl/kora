---
_manifest:
  urn: urn:agengai:kb:openclaw-skills-manual-p05
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
    family: guide
    scope: Creacion, operacion y evolucion de skills en OpenClaw
    dimensions: 15
    related:
    - urn:agengai:kb:openclaw-manual-integral
  kora:
    shard_index: 5
    shard_count: 5
    shard_root_urn: urn:agengai:kb:openclaw-skills-manual
relations:
  cites:
  - urn:agengai:kb:openclaw-manual-integral
---

# Manual Integral de Skills en OpenClaw - Parte 05

## 13.7 Subagentes y skills

En arquitectura multi-agente:
- Cada subagente hereda la configuracion de skills del agente padre o define la propia
- Skills de workspace son per-agent (cada workspace tiene su directorio `skills/`)
- Skills compartidos (`~/.openclaw/skills/`) visibles para todos los agentes del nodo

## 13.8 Integracion MCP

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
openclaw skills update --all # actualizar todos via OpenClaw
clawhub update --all # actualizar todos via ClawHub CLI
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
