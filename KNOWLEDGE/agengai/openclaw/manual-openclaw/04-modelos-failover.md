---
_manifest:
  urn: urn:agengai:kb:04-modelos-failover
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.1.0
status: published
tags:
- kora
- manual-openclaw
- '04'
- modelos
- failover
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:agengai:kb:04-modelos-failover
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
├── auth-profiles.json ← Store principal (API keys + OAuth tokens)
└── auth.json ← Cache de runtime (no editar manualmente)
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

- La documentación oficial actual explicita dos matices:
- **OAuth va antes que API keys** en round-robin automático.
- Si mezclas OAuth + API key para el mismo provider, el comportamiento puede parecer "inestable" entre sesiones si no hay pinning explícito.
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

- Si quieres evitar alternancia entre OAuth y API key, fija `auth.order[provider]` o usa `/model ...@profileId`.

### Diagrama de rotación

```
Request llega
 │
 ▼
¿Sesión tiene profile pineado?
├── SÍ → ¿Profile en cooldown/disabled?
│ ├── NO → Usar profile pineado
│ └── SÍ → ¿Auto-pin o user-pin?
│ ├── Auto-pin → Rotar a otro profile del provider
│ └── User-pin → Saltar a model fallback
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
1er fallo → cooldown 1 minuto
2do fallo → cooldown 5 minutos
3er fallo → cooldown 25 minutos
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
3er+ fallo → disabled 24 horas (cap)

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
