---
_manifest:
  urn: urn:kora:kb:04-modelos-failover
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.0.0
status: published
tags:
- kora
- manual-openclaw
- '04'
- modelos
- failover
lang: es
---

# Capítulo 4 — Modelos y Failover

> **Propósito:** Entender cómo OpenClaw selecciona, autentica, rota y recupera modelos de IA. Estas decisiones determinan la disponibilidad, el costo, y la calidad de tu agente. Sin una estrategia de modelos clara, tu agente es tan frágil como la API más inestable que uses.

- ---


## 4.1 Model Refs y Aliases

### El formato canónico: `provider/model`

- Toda referencia a un modelo en OpenClaw usa el formato `provider/model`:


```
anthropic/claude-sonnet-4-6
openai-codex/gpt-5.2
moonshot/kimi-k2.5
zai/glm-5
deepseek/deepseek-chat
```

- El provider identifica la API/endpoint, el model identifica qué modelo solicitar.
- Esto es importante porque **el mismo modelo puede estar disponible por múltiples providers** (e.g., `anthropic/claude-opus-4-6` vs `opencode/claude-opus-4-6` vs `openrouter/anthropic/claude-opus-4-6`).


### Aliases: nombres cortos

- Los aliases son atajos configurables que evitan escribir el ref completo:


```json5
{
  agents: {
    defaults: {
      models: {
        "anthropic/claude-sonnet-4-6": { alias: "sonnet" },
        "anthropic/claude-opus-4-6": { alias: "opus" },
        "moonshot/kimi-k2.5": { alias: "kimi" },
        "zai/glm-5": { alias: "glm5" },
        "openai-codex/gpt-5.2": { alias: "gpt-5.2" }
      }
    }
  }
}
```

- Con esto, `/model sonnet` o `/model kimi` funcionan en chat.
- Los aliases también se usan en cron jobs, sub-agentes, y webhooks.


### agents.defaults.models como allowlist

- Si `agents.defaults.models` tiene entries, se convierte en la **allowlist**: solo los modelos listados pueden ser seleccionados via `/model`.
- Si está vacío o ausente, cualquier modelo del catálogo es seleccionable.


- **Implicación de diseño:** Si configuras una allowlist muy restrictiva, un `/model` a un modelo no listado retorna error y el mensaje no se responde.
- Esto puede confundir al usuario si no sabe qué modelos están disponibles.


### Normalización

- Los model refs se normalizan a lowercase.
- Aliases de provider como `z.ai/*` se normalizan a `zai/*`.
- Modelos OpenRouter-style con `/` en el ID requieren el prefijo del provider (e.g., `/model openrouter/moonshotai/kimi-k2`).


- ---


## 4.2 Auth Profiles: Cómo el Gateway se Autentica con Providers

### Dos tipos de credenciales

| Tipo | Almacenamiento | Ejemplo | Renovación |
|------|---------------|---------|------------|
| **API Key** | `auth-profiles.json` | `ANTHROPIC_API_KEY` | No expira (hasta rotación manual) |
| **OAuth** | `auth-profiles.json` | ChatGPT OAuth (Codex) | Access token expira; refresh automático |

### Dónde viven las credenciales

```
~/.openclaw/agents/<agentId>/agent/
├── auth-profiles.json      ← Store principal (API keys + OAuth tokens)
└── auth.json                ← Cache de runtime (no editar manualmente)
```

- **Per-agent:** Cada agente tiene su propio `auth-profiles.json`.
- Si tienes un agente `main` y un agente `work`, cada uno tiene credenciales independientes.
- Nunca comparten referencia.


- **No en openclaw.json:** Las credenciales no van en el config.
- El config puede referenciar variables de entorno (`${ANTHROPIC_API_KEY}`) que el gateway resuelve, pero los tokens OAuth y las API keys resueltas viven en `auth-profiles.json`.


### Profile IDs

- Cada credencial tiene un profile ID que la identifica:


| Situación | Profile ID generado |
|-----------|-------------------|
| API key sin email | `anthropic:default` |
| OAuth con email | `openai-codex:user@gmail.com` |
| Segundo API key | `anthropic:default` (mismo ID, pero se agregan al pool de rotación) |

### Múltiples credenciales por provider

- OpenClaw soporta múltiples API keys por provider:


```bash
# Variables de entorno (en .env o shell)
ANTHROPIC_API_KEY=sk-ant-primary...
ANTHROPIC_API_KEY_1=sk-ant-backup1...
ANTHROPIC_API_KEY_2=sk-ant-backup2...

# Override de alta prioridad (para hot-swap sin restart)
OPENCLAW_LIVE_ANTHROPIC_KEY=sk-ant-emergency...
```

- **Prioridad de resolución:**

1. `OPENCLAW_LIVE_<PROVIDER>_KEY` (hot override, máxima prioridad)
2. `<PROVIDER>_API_KEYS` (lista separada por coma/punto y coma)
3. `<PROVIDER>_API_KEY` (key primaria)
4. `<PROVIDER>_API_KEY_*` (numeradas)

- ---


## 4.3 Rotación de Perfiles: Round-Robin con Stickiness

- Cuando un provider tiene múltiples auth profiles (varias API keys, API key + OAuth, etc.), OpenClaw necesita decidir cuál usar.
- Este es el algoritmo de rotación.


### Orden de selección

```
¿Hay auth.order[provider] explícito en config?
├── SÍ → Usar ese orden fijo
│
└── NO → Round-robin automático:
         1. Agrupar por tipo (OAuth primero, luego API keys)
         2. Dentro de cada tipo, ordenar por lastUsed (más viejo primero)
         3. Mover profiles en cooldown/disabled al final
```

### Session stickiness (el concepto más sutil)

- **OpenClaw NO rota en cada request.** Una vez que una sesión elige un auth profile, lo **pinea** para esa sesión.
- El pinning persiste hasta:


- La sesión se resetea (`/new`, `/reset`)
- Una compaction completa
- El profile entra en cooldown/disabled

- **¿Por qué?** Cache del provider.
- Anthropic, OpenAI y otros cachean el prompt por sesión/API key.
- Si rotaras en cada request, invalidarías el cache constantemente y pagarías re-cache en cada turn.


### Dos tipos de pinning

| Tipo | Cómo se establece | Comportamiento ante fallo |
|------|-------------------|--------------------------|
| **Auto-pin** (default) | El router elige el mejor profile | Si falla, rota a otro profile del mismo provider |
| **User-pin** | `/model provider/model@profileId` | Si falla, NO rota — salta directo al model fallback |

- La diferencia es crucial: un auto-pin es una **preferencia** (se intenta primero, pero hay fallback).
- Un user-pin es una **orden** (se usa ese profile o se falla).


### Diagrama de rotación

```
Request llega
      │
      ▼
¿Sesión tiene profile pineado?
├── SÍ → ¿Profile en cooldown/disabled?
│        ├── NO → Usar profile pineado
│        └── SÍ → ¿Auto-pin o user-pin?
│                 ├── Auto-pin → Rotar a otro profile del provider
│                 └── User-pin → Saltar a model fallback
│
└── NO → Seleccionar profile según round-robin
         → Pinear a la sesión
         → Usar
```

- ---


## 4.4 Cooldowns y Billing Disables

- Cuando una llamada al provider falla, OpenClaw necesita decidir: ¿reintento con el mismo profile? ¿Roto a otro? ¿Me rindo con este provider?


### Cooldowns (errores transitorios)

- Cuando un profile falla por auth/rate-limit/timeout, entra en **cooldown** con backoff exponencial:


```
1er fallo  → cooldown 1 minuto
2do fallo  → cooldown 5 minutos
3er fallo  → cooldown 25 minutos
4to+ fallo → cooldown 1 hora (cap)
```

- State almacenado en `auth-profiles.json`:


```json
{
  "usageStats": {
    "anthropic:default": {
      "lastUsed": 1708444800000,
      "cooldownUntil": 1708445400000,
      "errorCount": 2
    }
  }
}
```

- **Qué errores activan cooldown:**

- Rate limits (429)
- Auth failures (401, 403)
- Timeouts que parecen rate limiting
- Format/validation errors (e.g., tool call ID validation failures)

- **Qué errores NO activan cooldown:**

- Errores de contenido (safety filters)
- Errores de modelo no encontrado
- Errores de red transitorios (se reintentan inmediatamente)

### Billing Disables (errores de crédito)

- Los errores de billing ("insufficient credits", "credit balance too low") son **no-transitorios**.
- No tiene sentido reintentar en 1 minuto — el saldo no se va a recargar solo.


```
1er fallo billing → disabled 5 horas
2do fallo billing → disabled 10 horas
3er+ fallo        → disabled 24 horas (cap)

Reset: si no hay fallo billing por 24 horas, los counters se resetean
```

- State:


```json
{
  "usageStats": {
    "zai:default": {
      "disabledUntil": 1708462800000,
      "disabledReason": "billing"
    }
  }
}
```

### Implicaciones para diseño

- **1.
- Tener fallbacks es crítico.** Sin fallbacks, un cooldown de 1 hora significa 1 hora sin servicio.
- Con fallbacks, el agente cambia de modelo automáticamente.


- **2.
- Los billing disables son trampas silenciosas.** Si solo tienes un provider y se te acaba el crédito, el agente queda muerto por 5+ horas.
- Monitorea créditos.


- **3.
- Los cooldowns se acumulan.** Si un provider tiene problemas intermitentes, el backoff crece.
- Después de 4 fallos, ese profile está en cooldown 1 hora.
- Si todos los profiles del provider están en cooldown, se salta al fallback.


- ---


## 4.5 Model Fallback Chain

- La fallback chain es el mecanismo de **resiliencia**: si el modelo primario falla (todos sus profiles están en cooldown/disabled), OpenClaw pasa al siguiente modelo en la lista.


### Configuración

```json5
{
  agents: {
    defaults: {
      model: {
        primary: "anthropic/claude-sonnet-4-6",
        fallbacks: [
          "openai-codex/gpt-5.2",
          "moonshot/kimi-k2.5",
          "zai/glm-5"
        ]
      }
    }
  }
}
```

### Flujo de fallback

```
Request llega
      │
      ▼
Intentar PRIMARY (anthropic/claude-sonnet-4-6)
  │
  ├── Rotar todos los auth profiles de Anthropic
  │   ├── Profile 1: cooldown → skip
  │   ├── Profile 2: intento → timeout → cooldown
  │   └── Profile 3: intento → rate limit → cooldown
  │
  └── Todos los profiles agotados
      │
      ▼
Intentar FALLBACK 1 (openai-codex/gpt-5.2)
  │
  ├── Profile 1: intento → ¡éxito! → respuesta al usuario
  │
  └── (si falla: seguir con FALLBACK 2...)
      │
      ▼
Intentar FALLBACK 2 (moonshot/kimi-k2.5)
  └── ...y así sucesivamente

Si TODOS los fallbacks fallan → error al usuario
```

### Qué errores activan fallback

- **SÍ activan fallback:**

- Auth failures (todos los profiles del provider agotados)
- Rate limits (todos los profiles en cooldown)
- Timeouts que agotaron rotation

- **NO activan fallback:**

- Errores de contenido/safety
- Errores de formato (se manejan dentro del provider)
- Un solo profile falla pero hay otros disponibles en el mismo provider

### Diseño de una fallback chain efectiva

```
Criterios para ordenar fallbacks:

PRIMARY:    Tu modelo preferido (mejor calidad, cost aceptable)
FALLBACK 1: Modelo comparable, provider diferente (diversidad de riesgo)
FALLBACK 2: Modelo bueno + barato/gratis (para resistir outages largos)
FALLBACK 3: Modelo "último recurso" (premium costoso o modelo legacy)
```

- **Anti-patrones:**


| Anti-patrón | Por qué es malo |
|-------------|-----------------|
| Todos los fallbacks del mismo provider | Si Anthropic se cae, todos fallan |
| Fallback a modelo sin tool support | El agente pierde funcionalidad con tool calls |
| Fallback chain de 8 modelos | Cada fallback agrega latencia de timeout; con 8 puede ser 80+ segundos de espera |
| Sin fallbacks | Un rate limit de 1 hora = agente muerto 1 hora |

- **Patrón recomendado (ejemplo real):**


```json5
{
  model: {
    primary: "anthropic/claude-sonnet-4-6",  // Anthropic: calidad + prompt cache
    fallbacks: [
      "openai-codex/gpt-5.2",               // OpenAI: provider diferente, gratis con suscripción
      "moonshot/kimi-k2.5",                  // Moonshot: gratis, 262K ctx, diferente región
      "zai/glm-5"                            // Z.AI: China, barato, buen razonamiento
    ]
  }
}
```

- Diversidad de: provider, región geográfica, modelo de pricing.
- Si Anthropic se cae, OpenAI toma el relevo.
- Si ambos fallan (improbable), Moonshot y GLM cubren.


- ---


## 4.6 Overrides: Modelo por Contexto

- OpenClaw permite override del modelo en múltiples niveles:


### Jerarquía de resolución

```
Prioridad (mayor a menor):

1. Inline: /model provider/model en el mensaje → solo este mensaje
2. Session override: /model provider/model como mensaje standalone → persiste en la sesión
3. Per-agent: agents.list[].model → para este agente específico
4. Cron/webhook: model en el payload → para este job/hook
5. Sub-agente: model en sessions_spawn → para este sub-agente
6. Primary + fallbacks: agents.defaults.model → default global
```

### Override por sesión (`/model`)

```
/model opus                    ← cambiar a Opus para esta sesión
/model kimi                    ← cambiar a Kimi
/model                         ← ver modelos disponibles (picker)
/model list                    ← igual que /model
/model status                  ← detalle de auth + endpoint
/model default                 ← volver al modelo default
```

- El override persiste hasta:

- Nuevo `/model` explícito
- `/new` o `/reset` (nuevo sessionId)
- Otro override programático

### Override por agente

```json5
{
  agents: {
    list: [
      {
        id: "main",
        model: { primary: "anthropic/claude-sonnet-4-6" }
      },
      {
        id: "coding",
        model: { primary: "openai-codex/gpt-5.3-codex" }
      },
      {
        id: "cheap",
        model: { primary: "moonshot/kimi-k2.5" }
      }
    ]
  }
}
```

- Cada agente puede tener su propio primary + fallbacks.
- Si no se especifica, hereda de `agents.defaults.model`.


### Override por cron job

```bash
openclaw cron add \
  --name "Deep analysis" \
  --cron "0 6 * * 0" \
  --session isolated \
  --model opus \
  --thinking high \
  --message "Weekly codebase analysis..."
```

- El cron job usa Opus con thinking alto, sin afectar el modelo de la sesión main.


### Override por sub-agente

```json
{
  "task": "Analiza este código en profundidad",
  "model": "opus",
  "thinking": "high"
}
```

- El sub-agente usa el modelo especificado
- el parent mantiene su modelo original.


### Override por webhook

```bash
curl -X POST http://127.0.0.1:18789/hooks/agent \
  -H 'Authorization: Bearer SECRET' \
  -H 'Content-Type: application/json' \
  -d '{"message":"Summarize inbox","model":"openai/gpt-5.2-mini"}'
```

### Modelo de imagen (imageModel)

- Separado del modelo de texto.
- Se usa **solo** cuando el primary no soporta imágenes:


```json5
{
  agents: {
    defaults: {
      model: { primary: "deepseek/deepseek-chat" },
      imageModel: { primary: "anthropic/claude-sonnet-4-6" }
    }
  }
}
```

- Si alguien envía una imagen y el modelo primary (DeepSeek) no soporta imágenes, OpenClaw desvía a `imageModel` para ese request.


- ---


## 4.7 Heartbeat Model

- Los heartbeats pueden usar un modelo diferente (típicamente más barato) para reducir costos:


```json5
{
  agents: {
    defaults: {
      heartbeat: {
        every: "30m",
        model: "anthropic/claude-haiku-4-5"  // barato para checks periódicos
      }
    }
  }
}
```

- Si el heartbeat encuentra algo importante, lo reporta.
- Si no, responde `HEARTBEAT_OK`.
- Usar un modelo económico para esto es una optimización de costo sin sacrificar capacidad para las interacciones principales.


- ---


## Resumen del Capítulo

| Concepto | Decisión de diseño que habilita |
|----------|--------------------------------|
| **Model refs = provider/model** | Mismo modelo por múltiples providers; diversidad de acceso |
| **Aliases** | UX limpia en chat (`/model opus` vs `/model anthropic/claude-opus-4-6`) |
| **Auth profiles per-agent** | Aislamiento de credenciales; un agente comprometido no expone otros |
| **Session stickiness** | Optimización de prompt cache; no rotar innecesariamente |
| **Auto-pin vs user-pin** | Flexibilidad vs control explícito |
| **Cooldown exponencial** | Protección contra rate limit storms sin abandonar el provider |
| **Billing disable** | Detección de crédito agotado con backoff largo |
| **Fallback chain** | Resiliencia: provider down ≠ agente down |
| **Diversidad de providers** | Anti-fragilidad geográfica y de pricing |
| **Override por nivel** | Flexibilidad: cron usa opus, heartbeat usa haiku, main usa sonnet |
| **imageModel separado** | Soporte de imágenes sin forzar un modelo multimodal como primary |

### Diagrama de flujo completo

```
Request llega → ¿Override de sesión? → ¿Override de agente?
                     │                        │
                     ▼                        ▼
              Modelo resuelto          agents.defaults.model.primary
                     │
                     ▼
            Auth profile selection
            (round-robin + stickiness)
                     │
              ┌──────┴──────┐
              │              │
           Éxito          Fallo
              │              │
              ▼              ▼
         Respuesta     ¿Más profiles?
                       ├── SÍ → Rotar → Reintentar
                       └── NO → ¿Más fallbacks?
                                ├── SÍ → Siguiente modelo
                                └── NO → Error al usuario
```

- ---


- *Siguiente: [Capítulo 5 — Memoria](05-memoria.md)*

