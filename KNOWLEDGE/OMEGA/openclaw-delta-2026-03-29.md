---
_manifest:
  urn: "urn:agengai:kb:openclaw-delta-2026-03-29"
  provenance:
    created_by: "forjador-especialista-openclaw"
    created_at: "2026-03-29"
    source: "KNOWLEDGE/agengai/openclaw/documentacion-oficial (modificaciones 29-Mar-2026 vs compilacion 26-Mar-2026)"
  version: "1.0.0"
  status: published
  tags: [openclaw, delta, actualizacion, hooks, cli-backends, autenticacion, canales, skills, modelos-locales]
  lang: es
  extensions:
    agengai:
      family: delta
      scope: "Cambios en OpenClaw documentacion-oficial posteriores a 2026-03-26"
      complements:
        - "urn:agengai:kb:openclaw-manual-integral"
        - "urn:agengai:kb:openclaw-skills-manual"
---

# Delta OpenClaw — 2026-03-29

Complemento de actualizacion para `urn:agengai:kb:openclaw-manual-integral` (v1.0.0) y
`urn:agengai:kb:openclaw-skills-manual` (v2.0.0). Cubre cambios en la documentacion oficial
ocurridos el 29-Mar-2026, tres dias despues de la compilacion de los manuales base.

Leer en paralelo con los manuales base. Este documento NO reemplaza — extiende.

---

## 1. Hooks — Sistema Completo

> Reemplaza seccion 2.4 de `openclaw-manual-integral.md` (que era incompleta).
> Agrega contexto relevante a skills en `manual-integral-skills-openclaw.md`.

### 1.1 Eventos disponibles

| Evento | Trigger |
| --- | --- |
| `command:new` | Usuario envia `/new` |
| `command:reset` | Usuario envia `/reset` |
| `command:stop` | Usuario envia `/stop` |
| `session:compact:before` | Antes de compactacion |
| `session:compact:after` | Despues de compactacion |
| `session:patch` | Actualizacion de propiedades de sesion (solo clientes privilegiados) |
| `agent:bootstrap` | Antes de inyectar archivos bootstrap al workspace |
| `gateway:startup` | Despues de iniciar channels y cargar hooks |
| `message:received` | Mensaje entrante |
| `message:sent` | Mensaje saliente |
| `message:transcribed` | Post-transcripcion audio — incluye campo `transcript` |
| `message:preprocessed` | Post-enriquecimiento completo (media + links) |
| `tool_result_persist` | Transformar resultados de tool antes de persistir (sincrono, via plugin API) |
| `before_compaction` | Lifecycle de compactacion (plugin hook runner) |
| `after_compaction` | Lifecycle de compactacion (plugin hook runner) |

### 1.2 Context shapes de eventos de mensaje

El contexto completo disponible en handlers `message:*`:

```typescript
{
  from?: string
  to?: string
  body?: string
  bodyForAgent?: string
  transcript?: string        // Solo en message:transcribed
  timestamp?: number
  channelId: string
  conversationId?: string
  messageId?: string
  senderId?: string
  senderName?: string
  senderUsername?: string
  provider?: string
  surface?: string
  mediaPath?: string
  mediaType?: string
}
```

### 1.3 Plugin hook API — semantica de decision

**`before_tool_call`**:
- `{ block: true }` — terminal: detiene handlers de menor prioridad y bloquea la llamada
- `{ block: false }` — sin decision: no limpia bloqueo previo
- `{ requireApproval: { timeoutMs, onTimeout: "allow" | "deny" } }` — solicita aprobacion interactiva

**`message_sending`**:
- `{ cancel: true }` — terminal: cancela el envio del mensaje
- `{ cancel: false }` — sin decision

### 1.4 Bundled hooks

| Hook | Eventos | Funcion |
| --- | --- | --- |
| `session-memory` | `command:new`, `command:reset` | Guarda contexto de sesion en `<workspace>/memory/` |
| `bootstrap-extra-files` | `agent:bootstrap` | Inyecta archivos bootstrap adicionales segun globs |
| `command-logger` | comandos | Log audit en JSONL a `~/.openclaw/logs/commands.log` |
| `boot-md` | `gateway:startup` | Ejecuta `BOOT.md` del workspace al iniciar |

### 1.5 Trust boundary y discovery

Precedencia de discovery (menor a mayor override):
bundled → plugin → managed (`~/.openclaw/hooks/` + `extraDirs`) → workspace (`<workspace>/hooks/`)

**Regla critica**: workspace hooks NO pueden sobreescribir hooks con el mismo nombre de otras fuentes
(bundled, plugin, managed). Son aditivos, no sustitutivos.

Los workspace hooks requieren habilitacion explicita antes de cargarse:

```bash
openclaw hooks enable <nombre-del-hook>
```

### 1.6 Hook packs

Paquetes npm con campo `openclaw.hooks` en `package.json`. Instalacion:

```bash
openclaw plugins install <spec>
```

Dependencias instaladas con `npm install --ignore-scripts`.

### 1.7 Metadata en HOOK.md

| Campo | Descripcion |
| --- | --- |
| `emoji` | Emoji para la UI |
| `events` | Array de eventos que disparan el hook |
| `export` | Named export del handler (default: `"default"`) |
| `os` | Filtro de plataforma |
| `requires` | `bins`, `anyBins`, `env`, `config` |
| `always` | Bypass de eligibilidad |
| `install` | Especificaciones de instalador |

### 1.8 Configuracion

```json5
{
  hooks: {
    internal: {
      enabled: true,
      entries: {
        "session-memory": { enabled: true },
        "command-logger": { enabled: false },
        "boot-md": { enabled: true }
      },
      load: { extraDirs: ["/path/to/more/hooks"] }
    }
  }
}
```

### 1.9 CLI

```bash
openclaw hooks list [--eligible] [--verbose] [--json]
openclaw hooks info <nombre>
openclaw hooks check
openclaw hooks enable <nombre>
openclaw hooks disable <nombre>
```

---

## 2. CLI Backends — Fallback de Texto via CLIs Locales

> Completamente nuevo. Ausente en ambos manuales base.

### 2.1 Concepto

Superficie de fallback de texto puro cuando providers API fallan o no estan disponibles.
Sin tools (texto in → texto out). Sesiones soportadas para coherencia en follow-ups.

Los backends CLI son declarados por plugins (anthropic, openai, google) como proveedores de fallback.
OpenClaw los trata como un provider mas en la cadena de fallbacks.

### 2.2 Quick start

```bash
openclaw agent --message "hola" --model claude-cli/opus-4-6
openclaw agent --message "hola" --model codex-cli/gpt-5.4
```

### 2.3 Configuracion como fallback

```json5
agents: {
  defaults: {
    model: {
      primary: "anthropic/claude-opus-4-6",
      fallbacks: ["claude-cli/opus-4-6", "claude-cli/opus-4.5"]
    }
  }
}
```

### 2.4 Campos de configuracion de CLI backend

| Campo | Descripcion |
| --- | --- |
| `sessionArg` / `sessionArgs` | Pasar session ID al CLI |
| `sessionMode` | `"always"` \| `"existing"` \| `"none"` |
| `resumeArgs` | Flags diferentes para resume (distinto de first-run) |
| `imageArg` | Pasar imagenes por ruta al CLI |
| `imageMode` | `"repeat"` — como inyectar multiples imagenes |
| `systemPromptArg` | Argumento para system prompt customizado |
| `systemPromptWhen` | `"first"` — solo inyectar en el primer turno |

### 2.5 Backends registrados por plugins

| Plugin | Backend ID | Notas |
| --- | --- | --- |
| anthropic | `claude-cli` | Args especificos de claude CLI |
| openai | `codex-cli` | Resume support, output JSONL |
| google | `google-gemini-cli` | Session support |

### 2.6 Limitaciones

- Sin OpenClaw tools (conservative)
- Sin streaming (output recolectado al final)
- Structured outputs dependen del CLI subyacente
- Codex resume es texto plano, no JSONL

---

## 3. Autenticacion — Ampliaciones

> Extiende seccion §4.2 de `openclaw-manual-integral.md`.

### 3.1 Claude CLI migration (nuevo metodo)

```bash
# Cambiar autenticacion a CLI
openclaw models auth login --provider anthropic --method cli --set-default

# Shortcut via onboard
openclaw onboard --auth-choice anthropic-cli
```

El perfil legacy se mantiene; solo cambia el default a `claude-cli/...`.

### 3.2 Auth profiles con referencias estaticas

```json5
{
  // En auth-profiles.json o config
  "keyRef": { "source": "env", "provider": "default", "id": "ANTHROPIC_API_KEY" }
  // equivalente con token
  "tokenRef": { "source": "env", "provider": "default", "id": "MY_TOKEN" }
}
```

### 3.3 API key rotation — jerarquia completa

Para providers con soporte de rotacion:

| Variable | Prioridad | Descripcion |
| --- | --- | --- |
| `OPENCLAW_LIVE_<PROVIDER>_KEY` | Maxima (nueva) | Override unico, sin rotacion |
| `<PROVIDER>_API_KEYS` | Alta | Lista CSV/semicolons de keys |
| `<PROVIDER>_API_KEY` | Media | Key primaria |
| `<PROVIDER>_API_KEY_*` | Minima | Keys numeradas |

Reintentos solo en rate-limit (429). Fallos no-rate-limit fallan inmediatamente.

### 3.4 Seleccion de credencial per-session

```
# Pinear credencial especifica para esta sesion
/model <alias-o-id>@<profileId>

# Ver candidatos y proximo auth profile
/model status
```

### 3.5 Override de auth order per-agent

```bash
openclaw models auth order get --provider anthropic
openclaw models auth order set --provider anthropic
openclaw models auth order clear --provider anthropic
```

El override persiste en `~/.openclaw/agents/<agentId>/agent/auth-profiles.json`.

---

## 4. Modelos Locales

> Completamente nuevo. Ausente en ambos manuales base.

### 4.1 Requisitos de hardware

Minimo recomendado: hardware equivalente a 2+ Mac Studios maxeados (~$30k+ en GPUs).
Una sola GPU de 24 GB funciona solo para prompts ligeros.
Usar el variant mas grande disponible del modelo local.

### 4.2 Stack recomendado

- LM Studio + modelo local grande (Qwen, DeepSeek, Llama)
- Responses API para separacion de reasoning
- Endpoint default: `http://127.0.0.1:1234/v1`

### 4.3 Configuracion ejemplo (LM Studio)

```json5
{
  agents: {
    defaults: {
      model: { primary: "lmstudio/my-local-model" }
    }
  },
  models: {
    mode: "merge",
    providers: {
      lmstudio: {
        baseUrl: "http://127.0.0.1:1234/v1",
        apiKey: "lmstudio",
        api: "openai-responses",
        models: [{
          id: "my-local-model",
          reasoning: false,
          contextWindow: 196608,
          maxTokens: 8192,
          cost: { input: 0, output: 0 }
        }]
      }
    }
  }
}
```

### 4.4 Config hybrid (local + hosted como fallback)

```json5
{
  agents: {
    defaults: {
      model: {
        primary: "anthropic/claude-sonnet-4-6",
        fallbacks: ["lmstudio/my-local-model", "anthropic/claude-opus-4-6"]
      }
    }
  },
  models: { mode: "merge" }  // Mantiene proveedores hosted en el catalogo
}
```

### 4.5 Otros proxies OpenAI-compatibles

vLLM, LiteLLM, OAI-proxy y gateways custom siguen el mismo patron:
cambiar `baseUrl` al endpoint correspondiente.

### 4.6 Troubleshooting

```bash
# Verificar conectividad del gateway local
curl http://127.0.0.1:1234/v1/models
```

- **Hanging en inicio**: LM Studio pudo haber descargado el modelo — cold start es causa comun
- **Context errors**: reducir `contextWindow` en config o subir el limite del servidor
- **Safety**: modelos locales omiten filtros del provider; mantener agentes con scope estrecho

---

## 5. Canales — Configuracion Ampliada

> Extiende seccion §4.3 de `openclaw-manual-integral.md`.

### 5.1 Channel defaults (nuevo)

```json5
{
  channels: {
    defaults: {
      groupPolicy: "allowlist",   // open | allowlist | disabled
      heartbeat: {
        showOk: false,            // incluir canales saludables en heartbeat output
        showAlerts: true,         // incluir estados degradados/error
        useIndicator: true        // renderizar compact indicator-style output
      }
    }
  }
}
```

`channels.defaults.groupPolicy` es el fallback cuando no hay `groupPolicy` a nivel de provider.

### 5.2 Model por canal (nuevo)

Fijar un modelo especifico a un canal, grupo, o topic:

```json5
{
  channels: {
    modelByChannel: {
      discord: {
        "123456789012345678": "anthropic/claude-opus-4-6"
      },
      slack: {
        "C1234567890": "openai/gpt-4.1"
      },
      telegram: {
        "-1001234567890": "openai/gpt-4.1-mini",
        "-1001234567890:topic:99": "anthropic/claude-sonnet-4-6"
      }
    }
  }
}
```

El mapeo aplica cuando la sesion no tiene un model override previo (ej: seteado via `/model`).
Acepta `provider/model` o aliases configurados.

### 5.3 Telegram — campos nuevos

```json5
{
  channels: {
    telegram: {
      retry: {
        attempts: 3,
        minDelayMs: 400,
        maxDelayMs: 30000,
        jitter: 0.1
      },
      network: {
        autoSelectFamily: true,
        dnsResultOrder: "ipv4first"
      },
      proxy: "socks5://localhost:9050",
      webhookUrl: "https://example.com/telegram-webhook",
      webhookSecret: "secret",
      webhookPath: "/telegram-webhook"
    }
  }
}
```

- `tokenFile` rechaza symlinks (solo archivos regulares)
- `TELEGRAM_BOT_TOKEN` sigue siendo fallback para cuenta default
- En setups multi-cuenta (2+ account ids): definir `defaultAccount` explicito; `openclaw doctor` advierte cuando falta

### 5.4 Discord — thread bindings y voz

```json5
{
  channels: {
    discord: {
      threadBindings: {
        enabled: true,
        idleHours: 24,         // auto-unfocus por inactividad (0 = deshabilitado)
        maxAgeHours: 0,        // hard max age (0 = deshabilitado)
        spawnSubagentSessions: false  // opt-in para sessions_spawn({ thread: true })
      },
      voice: {
        enabled: true,
        autoJoin: [
          { guildId: "123456789012345678", channelId: "234567890123456789" }
        ],
        daveEncryption: true,
        decryptionFailureTolerance: 24,
        tts: {
          provider: "openai",
          openai: { voice: "alloy" }
        }
      },
      ui: {
        components: {
          accentColor: "#5865F2"
        }
      }
    }
  }
}
```

**Thread bindings**: habilita `/focus`, `/unfocus`, `/agents`, `/session idle`, `/session max-age`
y bound delivery/routing por thread de Discord.

**Voice**: OpenClaw intenta recovery de voice dejando/reuniendose a la sesion tras repeated
decrypt failures. `daveEncryption` y `decryptionFailureTolerance` pasan a `@discordjs/voice`.

### 5.5 WhatsApp — multi-account

```json5
{
  channels: {
    whatsapp: {
      accounts: {
        default: {},
        personal: {},
        biz: {}
      },
      defaultAccount: "default"
    }
  }
}
```

- Outbound defaultea a cuenta `default`; si no existe, usa el primer account id (sorted)
- `defaultAccount` override ese fallback cuando coincide con un account id configurado
- Per-account overrides: `sendReadReceipts`, `dmPolicy`, `allowFrom`
- Legacy single-account Baileys auth dir migrado automaticamente por `openclaw doctor` a `whatsapp/default`

---

## 6. Skills — Actualizaciones

> Extiende seccion §3 y §12 de `manual-integral-skills-openclaw.md`.

### 6.1 Skills watcher (auto-refresh)

```json5
{
  skills: {
    load: {
      watch: true,
      watchDebounceMs: 250
    }
  }
}
```

Cambios en `SKILL.md` disparan refresh automatico. El session snapshot se actualiza
en el siguiente agent turn (no en el turno actual). Comportamiento:

- Session snapshot congelado al inicio de sesion
- Si `watch: true`: snapshot bumped en el siguiente turn cuando hay cambios
- Si nuevo remote node conecta: snapshot puede refrescarse mid-session

### 6.2 Remote macOS nodes (Linux Gateway)

Si el Gateway corre en Linux y un nodo macOS esta conectado con `system.run` permitido,
OpenClaw trata skills macOS-only como elegibles cuando los binarios requeridos estan
presentes en ese nodo. El agente ejecuta esos skills via `nodes.run`.

**Advertencia**: si el nodo macOS se desconecta, los skills permanecen visibles en el catalogo
pero las invocaciones fallan hasta reconexion.

### 6.3 Formula exacta de token impact

```
total_chars = 195 + Σ (97 + len(name_escaped) + len(description_escaped) + len(location_escaped))
```

- Base overhead (solo cuando hay ≥1 skill): 195 caracteres
- Per skill: 97 caracteres + longitudes XML-escaped de `name`, `description`, `location`
- XML escaping expande `& < > " '` en entities, incrementando la longitud
- Estimacion aprox. OpenAI-style: ~4 chars/token → **97 chars ≈ 24 tokens** por skill (mas campos)

### 6.4 Sandbox — instalacion de binarios dentro del contenedor

`requires.bins` se verifica en el **host** al cargar el skill.
Si el agente esta sandboxeado, el binario debe existir **tambien dentro del contenedor**.

```json5
{
  agents: {
    defaults: {
      sandbox: {
        docker: {
          setupCommand: "apt-get install -y <paquete>"
        }
      }
    }
  }
}
```

`setupCommand` corre una vez despues de crear el contenedor. Requiere:
- Egreso de red habilitado
- Filesystem root escribible
- Usuario root en el sandbox

---

## 7. Model Providers — Plugin-Owned Functions

> Extiende seccion §4.1 de `openclaw-manual-integral.md`.

Los plugins pueden declarar hasta 25 funciones para ownerear comportamiento de provider.

| Funcion | Que controla |
| --- | --- |
| `auth[].run` | Flujos de onboarding/login interactivos |
| `auth[].runNonInteractive` | Auth headless |
| `wizard.setup` | Labels en `openclaw onboard`, aliases legacy |
| `wizard.modelPicker` | Entradas en onboarding/model pickers |
| `catalog` | Aparicion en `models.providers` |
| `resolveDynamicModel` | Acepta model ids no en catalogo estatico local |
| `prepareDynamicModel` | Metadata refresh antes de reintentar dynamic resolution |
| `normalizeResolvedModel` | Transport o base URL rewrites |
| `capabilities` | Transcript/tooling/provider-family quirks |
| `prepareExtraParams` | Defaults o normalizacion de request params per-model |
| `wrapStreamFn` | Headers/body/model compat wrappers en requests |
| `formatApiKey` | Auth profile → runtime `apiKey` string para transport |
| `refreshOAuth` | OAuth refresh cuando los shared refreshers no son suficientes |
| `buildAuthDoctorHint` | Guidance de reparacion cuando OAuth refresh falla |
| `isCacheTtlEligible` | Cuales model ids soportan prompt-cache TTL |
| `buildMissingAuthMessage` | Error recovery hint provider-especifico |
| `suppressBuiltInModel` | Ocultar upstream rows stale |
| `augmentModelCatalog` | Appendear rows sinteticos/finales post-discovery |
| `isBinaryThinking` | UX de thinking binary on/off |
| `supportsXHighThinking` | Opt-in a nivel `xhigh` |
| `resolveDefaultThinkingLevel` | Politica default de `/think` para una model family |
| `isModernModelRef` | Live/smoke preferred-model matching |
| `prepareRuntimeAuth` | Credencial configurada → token de corta vida |
| `resolveUsageAuth` | Credenciales de usage/quota para `/usage` y reporting |
| `fetchUsageSnapshot` | Fetch/parsing del endpoint de usage del provider |

### 7.1 Catalog injection via plugins

Plugins inyectan catalogos via `registerProvider({ catalog })`.
OpenClaw mergea los catalogos antes de escribir `models.json`.

Orden de catalogo: `simple` (API key planos) → `profile` (gated por auth profiles)
→ `paired` (entradas relacionadas) → `late` (override, gana en colision).

### 7.2 ProviderAuthEnvVars en manifests

Plugins declaran `providerAuthEnvVars` en su manifest para que el probe de env-based
auth generica no necesite cargar el plugin runtime completo.

---

## Referencia de archivos fuente

| Archivo fuente | Tamaño | Relevancia |
| --- | --- | --- |
| `automation/hooks.md` | 36 KB | §1 completo |
| `gateway/cli-backends.md` | 7.9 KB | §2 completo |
| `gateway/authentication.md` | 6 KB | §3 completo |
| `gateway/local-models.md` | 5.5 KB | §4 completo |
| `gateway/configuration-reference.md` | 114 KB | §5 secciones |
| `tools/skills.md` | 13.7 KB | §6 secciones |
| `concepts/model-providers.md` | 21.9 KB | §7 secciones |

*Forjador Especialista v1.0.0 — Delta OpenClaw 2026-03-29*
