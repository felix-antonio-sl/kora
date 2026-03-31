---
_manifest:
  urn: "urn:ops:kb:ux-telegram-openclaw"
  provenance:
    created_by: "ops/clawstack + kora/curator"
    created_at: "2026-03-23"
    source: "Pruebas empiricas con 3 bots Telegram OpenClaw v2026.3.22 + documentacion oficial"
    updated_at: "2026-03-23"
version: "1.1.0"
status: published
tags: [telegram, ux, configuracion, openclaw, streaming, tablas, chunking, modelo, browser, compaction, memoria]
lang: es
---

# Configuración de comportamiento de agentes OpenClaw

Configuraciones verificadas empíricamente para OpenClaw v2026.3.22+: canal Telegram (UX), modelo (razonamiento), browser, compaction, memoria. Cada config fue probada, su efecto documentado, y las trampas registradas.

---

## Config recomendada

```json5
channels: {
  telegram: {
    chunkMode: "length",
    markdown: { tables: "bullets" },
    replyToMode: "first",
    silentErrorReplies: true,
    textChunkLimit: 4000,
    linkPreview: false,
    reactionLevel: "minimal",
  },
}
```

---

## Detalle por config

### chunkMode

| Valor | Efecto | Recomendación |
|---|---|---|
| `"newline"` | Corta en cada línea en blanco (párrafo). Produce muchas burbujas cortas en Telegram. Fragmenta respuestas largas en 10-15 mensajes. | **NO usar** |
| `"length"` | Corta solo al superar `textChunkLimit`. Mensajes más largos y consolidados. | **Recomendado** |

### markdown.tables

| Valor | Efecto | Recomendación |
|---|---|---|
| `"code"` (default) | Renderiza tablas como bloque `<pre>` monoespaciado. Ilegible en pantalla móvil — columnas desalineadas, scroll horizontal. | **NO usar** |
| `"bullets"` | Convierte cada fila de tabla en lista de bullets (ej: `• Feature: X, Plataforma: Y`). Legible en cualquier pantalla. | **Recomendado** |
| `"off"` | Envía markdown crudo sin transformar. Telegram no soporta tablas nativas — resultado impredecible. | Evitar |

### replyToMode

| Valor | Efecto | Recomendación |
|---|---|---|
| `"off"` (default) | Respuestas llegan como mensajes sueltos sin relación visual con la pregunta. | Aceptable para chat lineal |
| `"first"` | Bot cita el mensaje del usuario al responder. Crea threading visual — claro qué respuesta va con qué pregunta. | **Recomendado** |
| `"all"` | Cita cada mensaje. Ruidoso si hay múltiples mensajes seguidos. | Evitar |

### silentErrorReplies

| Valor | Efecto | Recomendación |
|---|---|---|
| `false` (default) | Errores (API timeout, rate limit) suenan con notificación normal. | Molesto |
| `true` | Errores llegan silenciosos — no vibra el teléfono por un fallo. | **Recomendado** |

### streaming

| Valor | Efecto en Telegram |
|---|---|
| `"off"` | Sin preview. Espera respuesta completa, envía de una vez. Sin feedback visual. |
| `"partial"` | Envía preview message, lo edita via `editMessageText` mientras genera. Muestra tool calls como `<read_file>` en el chat. |
| `"progress"` | **Alias de "partial" en Telegram** — no hay diferencia. Existe para consistencia cross-canal. |
| `"block"` | Legacy. Chunking por bloques de texto. |

`"partial"` es el default y funciona bien. Si las tool calls en el preview molestan, usar `"off"`.

---

## Trampas documentadas

### streaming: "full" no existe

Opciones válidas: `off | partial | block | progress`. `"full"` genera error de schema en `openclaw doctor`. `"progress"` es alias de `"partial"` en Telegram.

### tools.profile: "minimal" no incluye filesystem

`"minimal"` solo provee `session_status`. No incluye `group:fs` ni `group:web`. Para agentes que leen KBs desde filesystem, no restringir tools o usar `"coding"`.

| Profile | Tools incluidos |
|---|---|
| `"minimal"` | `session_status` solamente |
| `"coding"` | `group:fs`, `group:runtime`, `group:sessions`, `image` (nota: docs OpenClaw listan `group:memory` pero este grupo no existe en v2026.3.22) |
| `"messaging"` | `group:messaging`, sessions tools |
| `"full"` | Sin restricción |

### group:memory no existe en v2026.3.22

Genera warning en logs: `tools.allow contains unknown entries (group:memory)`. No bloquea el arranque pero la tool no se carga. Grupos válidos: `group:fs`, `group:web`, `group:runtime`, `group:sessions`, `group:ui`, `group:automation`, `group:messaging`, `group:nodes`, `group:openclaw`.

### Auth es per-agent, no compartida

`auth-profiles.json` vive en `~/.openclaw/agents/{id}/agent/`. Cada agente lee SOLO su propio archivo. Copy manual entre agentes funciona pero no se sincroniza.

### Config no interpola ${ENV_VAR}

`openclaw.json` no soporta interpolación de variables de entorno. Tokens y valores van literales en el JSON. La variable `${OPENCLAW_HOOKS_TOKEN}` queda como string literal.

---

## Config adicional verificada

### thinkingDefault

| Valor | Efecto |
|---|---|
| `"high"` | Thinking extendido siempre. Más tokens, más lento. |
| `"adaptive"` | v2026.3.x — Claude 4.6 ajusta thinking según complejidad. Ahorra tokens en tareas simples. **Recomendado**. |

### session.reset

| Modo | Efecto | Caso de uso |
|---|---|---|
| `mode: "idle", idleMinutes: 120` | Reset tras 2h de inactividad | Agentes reactivos (copiloto on-demand) |
| `mode: "daily", atHour: 4` | Reset diario a las 4AM | Agentes con sesiones de día completo |

### session.maintenance

```json5
session: {
  maintenance: {
    pruneAfter: "30d",
    maxEntries: 500,
  },
}
```

Previene crecimiento descontrolado del session store. Poda sesiones >30 días y limita a 500 entradas.

### gateway.bind en Docker

`"loopback"` (default) escucha en `127.0.0.1` dentro del container. Otros containers en la misma bridge no pueden alcanzarlo. Usar `"lan"` para que escuche en `0.0.0.0`. La seguridad del host la da el port mapping Docker (`127.0.0.1:{port}:{port}`).

---

## Configuración de modelo y razonamiento

### model (agents.defaults.model)

```json5
model: { primary: "anthropic/claude-opus-4-6" },
```

Formato: `{ primary: "provider/model" }`. NO string directo (`model: "anthropic/claude-opus-4-6"` es inválido en v2026.3.x). Soporta `fallbacks: ["provider/model2"]` para failover.

### models (parámetros por modelo)

```json5
models: {
  "anthropic/claude-opus-4-6": {
    params: { cacheRetention: "long" },
  },
},
```

`cacheRetention`: `"none"` | duración (`"5m"`, `"1h"`, `"long"`). `"long"` maximiza cache hit en Anthropic (reduce costo en turnos consecutivos). Debe ir bajo `params:`, no en raíz del modelo.

### thinkingDefault (ampliado)

| Valor | Efecto | Recomendación |
|---|---|---|
| `"off"` | Sin razonamiento extendido. Rápido, barato. | Agentes simples |
| `"low"` / `"medium"` / `"high"` | Nivel fijo de thinking por turno | Predecible pero desperdicia tokens en tareas simples |
| `"adaptive"` | Claude 4.6 ajusta thinking según complejidad de la tarea | **Recomendado v2026.3.x** — ahorra tokens sin perder calidad |

---

## Configuración de browser

```json5
browser: {
  headless: true,
  noSandbox: true,
  defaultProfile: "openclaw",
},
```

| Key | Efecto | Recomendación |
|---|---|---|
| `headless: true` | Browser sin ventana. Obligatorio en containers Docker sin display. | Siempre `true` en producción |
| `noSandbox: true` | Desactiva sandbox de Chromium. Necesario dentro de containers. | `true` en Docker |
| `defaultProfile` | Perfil de browser. `"openclaw"` = aislado. `"user"` = perfil del host. | `"openclaw"` en producción |

Sin esta config, web_fetch y browser tools pueden fallar silenciosamente — Chromium no arranca y el error queda en logs sin llegar al usuario.

---

## Configuración de compaction

Compaction reduce el contexto cuando la sesión crece cerca del límite de la ventana del modelo.

```json5
agents: {
  defaults: {
    compaction: {
      mode: "default",
      reserveTokensFloor: 24000,
      memoryFlush: {
        enabled: true,
        softThresholdTokens: 6000,
      },
    },
  },
},
```

| Key | Efecto | Recomendación |
|---|---|---|
| `mode` | `"default"` (compaction normal) o `"safeguard"` (más conservador) | `"default"` |
| `reserveTokensFloor` | Tokens mínimos reservados para respuesta post-compaction | 24000 |
| `memoryFlush.enabled` | Antes de compactar, guarda notas en memoria persistente | **`true`** para sesiones largas |
| `memoryFlush.softThresholdTokens` | Activa flush cuando quedan menos de N tokens | 6000 |

Especialmente importante para agentes con sesiones largas (steipete coordinando workers, korax acumulando contexto diario).

---

## Configuración de memoria

### memorySearch

```json5
memorySearch: {
  enabled: true,
  provider: "gemini",
},
```

| Key | Efecto |
|---|---|
| `enabled` | Activa búsqueda semántica en memoria persistente |
| `provider` | Backend de embeddings: `"gemini"` (cloud), `"openai"`, `"local"`, `"voyage"` |

Requiere `GEMINI_API_KEY` en `.env` cuando `provider: "gemini"`.

### Hybrid search (v2026.3.x, avanzado)

```json5
memorySearch: {
  query: {
    hybrid: {
      enabled: true,
      vectorWeight: 0.7,
      textWeight: 0.3,
      mmr: { enabled: true, lambda: 0.7 },
      // temporalDecay: REMOVIDO en 2026.3.x — no usar, campo inválido
    },
  },
},
```

Combina BM25 (keyword) + vector (semántico) con diversidad (MMR) y decay temporal. No habilitado en deploy actual.

---

## Config completa recomendada (template)

Base para cualquier nuevo agente OpenClaw sobre Telegram:

```json5
{
  agents: {
    defaults: {
      model: { primary: "anthropic/claude-opus-4-6" },
      models: {
        "anthropic/claude-opus-4-6": {
          params: { cacheRetention: "long" },
        },
      },
      memorySearch: { enabled: true, provider: "gemini" },
      thinkingDefault: "adaptive",
    },
    list: [
      {
        id: "{agent-id}",
        default: true,
        identity: { name: "{Name}", emoji: "{emoji}", theme: "{theme}" },
      },
    ],
  },
  browser: { headless: true, noSandbox: true },
  session: {
    scope: "per-sender",
    reset: { mode: "idle", idleMinutes: 120 },
  },
  hooks: { enabled: true, token: "{hooks-token}" },
  gateway: {
    mode: "local",
    port: "{port}",
    bind: "lan",
    controlUi: { enabled: true, basePath: "/openclaw" },
    auth: { mode: "token" },
  },
  channels: {
    telegram: {
      enabled: true,
      dmPolicy: "allowlist",
      allowFrom: ["{telegram-user-id}"],
      groupPolicy: "disabled",
      streaming: "partial",
      chunkMode: "length",
      markdown: { tables: "bullets" },
      replyToMode: "first",
      silentErrorReplies: true,
      ackReaction: "{emoji}",
      reactionLevel: "minimal",
      linkPreview: false,
      textChunkLimit: 4000,
    },
  },
}
```

---

## Referencias

- Arquitectura completa del stack: `urn:ops:kb:arquitectura-stack-kora`
- Federación cross-gateway: `urn:ops:kb:federacion-kora-v2`
- Tutorial de deploy paso a paso: `urn:ops:kb:deploy-agente-kora-en-openclaw`
- Principios de transmutación (P16 UX): `urn:ops:kb:principios-transmutacion-kora-openclaw`
