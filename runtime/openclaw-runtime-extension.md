---
_manifest:
  urn: "urn:agengai:kb:openclaw-runtime-extension"
  provenance:
    created_by: "OpenAI"
    created_at: "2026-03-23"
    source: "runtime-spec-md v3.8.0, OpenClaw baseline; v1.0.1 agrega relations estandarizadas; v1.1.0 alinea con transmutation-spec v1.0 y harness-spec v1.0 — incorpora matriz de preservacion por eje, dominio de soporte, ACP como meta-runtime; v1.2.0 se ancla a multiagente-spec como ley de coreografia; v1.2.1 fija acceso a KB via clon local vivo de KORA para despliegues OpenClaw KORA."
version: "1.2.1"
status: publicado
tags: [spec, runtime, openclaw, extension, transmutacion, deploy, acp]
lang: es
extensions:
  agengai:
    family: spec
    extends:
      - "urn:kora:kb:runtime-spec-md"
    precedence_tier: 4
    platform: "openclaw"
    baseline_docs_release: "2026.4.9"
relations:
  depends:
    - "urn:kora:kb:runtime-spec-md"
    - "urn:kora:kb:transmutation-spec"
    - "urn:kora:kb:multiagente-spec"
  cites:
    - "urn:kora:kb:harness-spec"
    - "urn:kora:kb:gobernanza"
---

# AGENGAI/OpenClaw-Runtime-Extension v1.2.1

## 1. Definicion

Esta extension especializa `runtime-spec-md` para el target **OpenClaw**.
Fija dominio de soporte, matriz de fidelidad de proyeccion, principio
native-first y encaje runtime-especifico.

### 1.1 Alcance

Gobierna:

1. Proyeccion `T_{openclaw}: KORA_IR → OpenClaw` segun `transmutation-spec`.
2. Principio `native-first` para OpenClaw.
3. Topologia de output `artifacts/agents/{ns}/{agent}/_BUILD/openclaw/`.
4. Frontera entre artefactos derivados y estado operativo mutable.
5. Encaje con ACP (OpenClaw como meta-runtime multi-backend).
6. Acceso read-only al repo KORA local actualizado como fuente de conocimiento.

### 1.2 Rol distintivo de OpenClaw

A diferencia de Claude Code, Codex y Gemini — que son runtimes individuales
— OpenClaw es un **meta-runtime** via ACP (Agent Client Protocol) con
15 backends permitidos: `claude, codex, copilot, cursor, droid, gemini,
iflow, kilocode, kimi, kiro, openclaw, opencode, pi, qwen, ...`.

Esto lo hace soportar el **dominio mas amplio** de los 5 runtimes target,
incluyendo el unico soporte nativo a **arnés Servicio** (Μ=3 ambiental,
always-on).

## 2. Formas materiales soportadas

| Forma material (atlas B) | Ubicacion runtime | Estructura |
|----------------------------|----------------------|--------------|
| Workspace de agente | `openclaw-fleet/workspaces/{agentId}/` | 8+ archivos canónicos (AGENTS.md, SOUL.md, IDENTITY.md, USER.md, TOOLS.md, HEARTBEAT.md, BOOT.md, MEMORY.md) + `memory/`, `skills/`, `reference/` |
| Skill embebido | `workspaces/{agentId}/skills/{name}/SKILL.md` | conforme agentskills.io + overlay KORA |
| Bot 24/7 | workspace + Telegram account + systemd service | `~/.openclaw/openclaw.json` config |
| ACP backend delegado | invocacion via `acp.defaultAgent` o `acp.dispatch` | protocolo ACP |

## 3. Matriz de preservacion por eje

OpenClaw soporta el dominio mas amplio de los 5 runtimes target.

### 3.1 Eje Π (plan)

```yaml
pi:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full }
  "2": { projected: 2, fidelity: full }
  "3": { projected: 3, fidelity: full, comment: "OpenClaw soporta delegacion jerarquica recursiva via ACP dispatch y sub-agentes" }
```

### 3.2 Eje Μ (materia)

```yaml
mu:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full, comment: "scratchpad intra-session" }
  "2": { projected: 2, fidelity: full, comment: "MEMORY.md (~1.5KB inyectado cada turno) + memory/*.md (declarative)" }
  "3": { projected: 3, fidelity: full, comment: "always-on via systemd + Telegram bots; unico runtime con Μ=3 full" }
```

### 3.3 Eje Ξ (interaccion)

```yaml
xi:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full }
  "2": { projected: 2, fidelity: full }
  "3": { projected: 3, fidelity: full, comment: "protocolos multi-fase via session types de ACP + handoffs entre agentes" }
  "4": { projected: 4, fidelity: full, comment: "operad dinamica: Org^#_m via ACP dispatch + agentToAgent + forgemaster-como-orquestador" }
```

### 3.4 Eje Λ (nivel sociotecnico)

```yaml
lambda:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full, comment: "organizacional via fleet + workspaces compartidos" }
  "2": { projected: 2, fidelity: full, comment: "ecosystem via ACP multi-backend federado" }
  "3": { projected: 3, fidelity: partial, loss: "society-in-the-loop requiere gobernanza externa no modelada en runtime; parcialmente soportado via audit trails y compliance" }
```

### 3.5 Eje Φ (acoplamiento humano-AI)

```yaml
phi:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full, comment: "tool metaphor via Telegram chat" }
  "2": { projected: 2, fidelity: full, comment: "collaborative con liderazgo humano" }
  "3": { projected: 3, fidelity: partial, loss: "hybrid cognition parcial; OpenClaw tiene human-in-the-loop pero no HAJCS completo" }
  "4": { projected: null, fidelity: none, loss: "co-evolutivo requiere aprendizaje continuo que OpenClaw no modela" }
```

### 3.6 Eje Σ (vector etico)

```yaml
sigma:
  safety_norm:
    max_supported: 3
    enforcement: "hard_rules en AGENTS.md + approval gates + policy enforcement en gateway"
  fairness:
    max_supported: 3
    enforcement: "declarative + bias audits manuales; no enforcement runtime automatico"
  transparency:
    max_supported: 3
    enforcement: "conversation history persistente + logs + audit trails por sesion"
  accountability:
    max_supported: 3
    enforcement: "git log en openclaw-fleet repo + logs_2.sqlite por session + Telegram accountability natural"
  sustainability:
    max_supported: 2
    enforcement: "model routing + budget tracking; sustainability environmental no medida directamente"
```

## 4. Principio native-first

Cuando OpenClaw ofrece superficie nativa para config, permisos, bundles o
instalacion, la transmutacion **DEBE** usar esa superficie antes que un
wrapper textual improvisado.

Superficies nativas:

- Config: `~/.openclaw/openclaw.json` (no texto embebido en body).
- Permisos: `tools.agentToAgent.allow` + `acp.allowedAgents`.
- Bundles: workspace `skills/` directory + `_meta.json`.
- Instalacion: `openclaw` CLI comandos (`config set`, `gateway restart`).
- Telegram channels: `channels.telegram.accounts` con `tokenFile` en
  `~/.openclaw/secrets/`.
- Model routing: `agents.defaults.model.primary` + `fallbacks[]`.

## 5. Topologia target

La salida derivada **DEBE** vivir bajo:

```
artifacts/agents/{namespace}/{agent}/_BUILD/openclaw/
```

Dentro de ese contenedor:

- Artefactos del agente compilados (workspace files).
- Config nativa OpenClaw.
- `_transmutation.yml` (obligatorio).
- Skill bundles si aplican.

El **workspace productivo** de OpenClaw vive en
`~/openclaw-fleet/workspaces/{agentId}/` — es **runtime**, no IR. El build
KORA produce los blueprints que se sincronizan al workspace runtime.

## 6. Runtime state boundary

Quedan **fuera** de la fuente canonica (no en `_BUILD/`, ni versionados):

- Credenciales (`~/.openclaw/secrets/`).
- Pairing stores.
- Caches.
- Sessions.
- Volumenes operativos.
- `.openclaw/` workspace state (gitignored en openclaw-fleet).
- `.clawhub/` lock files.

Estos se resuelven en runtime, no en transmutacion.

## 7. Metadata de encaje runtime

```yaml
extensions:
  openclaw:
    # Workspace
    agent_id: "salubrista"
    workspace_path: "workspaces/salubrista/"
    # Bot
    bot_handler: telegram
    bot_account: "@vector_kv_bot"
    token_file: "secrets/telegram-salubrista.token"
    # Model
    model_primary: "openai-codex/gpt-5.4"
    model_fallbacks: ["minimax/MiniMax-M2.7"]
    compaction_model: "openai-codex/gpt-5.4"
    responses_server_compaction: true
    runtime_context_cap: 272000  # tokens
    # ACP
    acp_compliant: true
    acp_backend: "openclaw"
    acp_default_delegate: "codex"  # backend para delegar
    # Reload
    reload_mode: "hybrid"  # hot-reload de workspace files
    # Heartbeat
    heartbeat_enabled: true
    stuck_session_warn_ms: 300000
    # KORA live clone
    kora_repo_required: true
    kora_repo_env: "KORA_REPO"
    kora_repo_default: "/home/felix/kora"
    kora_repo_mount: "/home/node/repos/kora"
    knowledge_mount_strategy: "bind_mount_live_kora_clone"
    knowledge_mount_mode: "ro"
```

## 8. ACP como meta-runtime

OpenClaw es **meta-runtime** via ACP: puede delegar a 15 backends distintos.
Un artefacto KORA desplegado en OpenClaw puede configurar:

- `acp.defaultAgent: codex` — backend principal de inferencia.
- `acp.allowedAgents[]` — backends permitidos para dispatch dinamico.
- `acp.dispatch.enabled: true` — permite cambio dinamico de backend por
  tarea.
- `acp.maxConcurrentSessions: 8` — backpressure.

Esto significa que un artefacto KORA en OpenClaw puede correr su plan con
Claude, Codex, Gemini, Pi, o cualquier backend ACP — OpenClaw orquesta.

**Consecuencia**: OpenClaw es el **unico target con acceso a toda la
fibra ACP**. Artefactos que requieren multi-backend inherentemente
(p. ej. que delegan tareas creativas a Claude y tareas de codigo a Codex)
viven nativamente en OpenClaw.

La validez de esos handoffs ya no queda implicita: desde `multiagente-spec
v1.0.0`, ACP debe leerse como realizacion de una coreografia con `protocol_id`,
`session_id` y budget propagados.

## 9. Dominio de invocacion

| Modo | Trigger | Vector tipico |
|------|---------|----------------|
| Conversation Telegram | Mensaje de usuario al bot | Π=2, Μ=3, Ξ=3, Λ=1-2, Φ=1-2 |
| ACP dispatch | `acp.dispatch` a backend especifico | Π=2, Μ=2, Ξ=2-3, varies |
| agentToAgent | Un agente invoca a otro en la fleet | Π=2-3, Μ=3, Ξ=4, Λ=1 |
| Proactive (cron/webhook) | Trigger externo al bot | Π=2, Μ=3, Ξ=3, Φ=1, always-on |
| Skill invocation | Skill dentro de workspace | Π=1-2, Μ=0-1, Ξ=1 |

## 10. Reglas de transmutacion

Obligatorias:

1. `_transmutation.yml` emitido conforme `transmutation-spec §6`.
2. Output vive en `artifacts/agents/{ns}/{agent}/_BUILD/openclaw/`.
3. Native-first: usar superficies nativas antes que wrappers textuales.
4. Runtime state NO se materializa en output canonico.
5. Secrets nunca se embeben en artefactos versionados.
6. Las 8 leyes estructurales de `transmutation-spec §3.2` se preservan.
7. Si el vector IR declara Μ=3 (ambiental), OpenClaw lo realiza; no requiere
   pérdida.
8. En despliegues KORA, el host DEBE tener un clon local actualizado de KORA y
   montarlo read-only en `/home/node/repos/kora`; los corpus de
   `artifacts/knowledge/**` se leen desde ese clon, no desde copias sueltas.

### 10.1 Contrato de repo KORA vivo

Todo agente KORA transmutado a OpenClaw asume:

```yaml
kora_repo_access:
  required: true
  host_env: KORA_REPO
  default_host_path: /home/felix/kora
  container_mount: /home/node/repos/kora
  mode: ro
  sync_strategy: bind_mount_live_kora_clone
  knowledge_root: artifacts/knowledge
```

El deploy puede exponer aliases ergonomicos como
`/home/node/knowledge/{namespace}/{corpus}`, pero esos aliases deben apuntar al
mismo clon KORA. Si no existe clon local actualizado, el `platform_contract`
debe declararlo como fallback o freeze auditado; no es el modo normal.

## 11. Ingesta inversa (`Lift_{openclaw}`)

Workspaces OpenClaw elevables a IR KORA:

```bash
kora ingest --from openclaw --workspace ~/openclaw-fleet/workspaces/mente-omega
```

Mapeo:

| Archivo Workspace | Destino KORA IR |
|-------------------|-------------------|
| `AGENTS.md` | `agent.plan` + `agent.interface` |
| `SOUL.md` | `agent.profile.identity` + atlas descriptivo |
| `IDENTITY.md` | metadata de presentacion |
| `USER.md` | `agent.context.operator_profile` |
| `TOOLS.md` | `agent.interface.allowed_tools` |
| `HEARTBEAT.md` | `extensions.openclaw.heartbeat_enabled: true` |
| `BOOT.md` | `agent.plan.initial_state` (derivado) |
| `MEMORY.md` + `memory/` | proyecta a `vector_ontologico.mu: 2-3` segun size/frequency |
| `skills/` | `agent.composition.sub_skills[]` + cada skill ingestado separadamente |

Default `vector_ontologico` para workspaces OpenClaw ingestados:
`(Π=2, Μ=3, Ξ=3, Λ=1, Φ=2, Σ=[2,2,2,2,1])`. El autor ajusta.

## 12. Validacion

| Check | Condicion | Enforcement |
|-------|-----------|-------------|
| Native-first | No wrapper textual cuando hay superficie nativa | manual/lint |
| Output ordenado | La salida vive bajo topologia declarada | lint |
| `_transmutation.yml` presente | Conforme transmutation-spec §6 | lint |
| Estado excluido | No se serializan credenciales ni caches | lint/manual |
| ACP metadata | Si artefacto es ACP-compliant, `acp_backend` declarado | lint |
| Matriz coherente | Valor de matriz coincide con version OpenClaw runtime | manual |
| Vector dentro del dominio | Vector IR ∈ `D_{openclaw}` (maximo dominio de los 5) | lint |
| Repo KORA vivo | `KORA_REPO` clonado y actualizado, montado RO en `/home/node/repos/kora` | preflight |

## 13. Trace fidelity

```yaml
trace_fidelity:
  level: pendiente
  capture_mechanism: "journalctl --user + session jsonl por especificar"
  notes: "no cerrar verificacion estricta de trazabilidad hasta completar mecanismo estable"
```

## 14. Contrato vigente v1.2.1

- OpenClaw soporta **todos** los arneses: {Utilidad, Disciplina, Delegado,
  Persona, Orquestador, Servicio}.
- **Unico target** con soporte nativo a arnés Servicio (Μ=3).
- Soporta ACP como meta-runtime multi-backend (15 backends).
- Dominio completo: Π ≤ 3, Μ ≤ 3, Ξ ≤ 4, Λ ≤ 3 (Λ=3 parcial), Φ ≤ 3.
- Integracion con Telegram, systemd, ACP dispatch.
- Hot-reload de workspace files via `gateway.reload.mode: hybrid`.
- Agentes KORA desplegados en OpenClaw leen `artifacts/knowledge/**` desde un
  clon local vivo y actualizado de KORA montado read-only.

## 15. Migracion

### 15.1 Cambios v1.0.1 → v1.1.0

- Adopta formato de `transmutation-spec v1.0` (matriz de preservacion por
  eje).
- Declara dominio de soporte explicito en harness-spec PMI × LFS.
- Formaliza rol de meta-runtime via ACP.
- Agrega mapeo `Lift_{openclaw}` para ingesta inversa.
- Alinea metadata runtime con campos estandar.
- Documenta campos nuevos: `acp_*`, `reload_mode`, `runtime_context_cap`.

### 15.2 Compatibilidad

Las reglas v1.0.1 (native-first, topologia, runtime state boundary) se
mantienen. La nueva estructura agrega explicitud; no rompe transmutaciones
existentes.

### 15.3 Cambios v1.2.0 → v1.2.1

- Generaliza el patron aprendido en `salud/urgenciologo`: los agentes OpenClaw
  KORA se despliegan con `KORA_REPO` local actualizado.
- El conocimiento autorizado se resuelve desde
  `$KORA_REPO/artifacts/knowledge/**` mediante bind mount read-only.
- `_transmutation.yml` puede declarar `kora_repo_access` como contrato de
  preflight para despliegue.
