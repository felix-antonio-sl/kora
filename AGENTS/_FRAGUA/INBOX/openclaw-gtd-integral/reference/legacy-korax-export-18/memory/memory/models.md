# Modelos AI — Configuración y Notas

*Source of truth para la config activa: `~/.openclaw/openclaw.json`. Este archivo es referencia para memory_search.*

---

## Cadena de fallback activa

```
anthropic/claude-sonnet-4-6    ← primary (alias: sonnet)
        ↓
openai-codex/gpt-5.2           ← fallback 1 (alias: gpt-5.2, OAuth)
        ↓
moonshot/kimi-k2.5              ← fallback 2 (alias: kimi, gratis, 262K ctx)
        ↓
zai/glm-5                       ← fallback 3 (alias: glm5, $1/$3.2, reasoning)
```

*Actualizado: 2026-02-20*

## Lógica del stack

1. Nunca dos del mismo proveedor consecutivos — diversidad para máximo uptime
2. Degradación progresiva de costo: gratis → gratis → pagado

## Aliases disponibles (no en cascada automática)

| Alias | Modelo | Uso recomendado |
|-------|--------|-----------------|
| `haiku` | claude-haiku-4-5 | Heartbeats, tareas ligeras |
| `opus` | claude-opus-4-6 | Razonamiento complejo |
| `minimax` | MiniMax-M2.5 | Coding, gratis, 200K ctx |
| `glm-flash` | glm-4.7-flash | Fallback ligero, gratis |
| `glm47` | glm-4.7 | GLM intermedio |
| `qwen-coder` | coder-model (portal) | Coding especializado, gratis |
| `qwen-vision` | vision-model (portal) | Análisis de imágenes, gratis |
| `codex-5.3` | gpt-5.3-codex | OpenAI Codex (OAuth) |
| `codex-5.2` | gpt-5.2-codex | OpenAI Codex (OAuth) |

## Uso diferenciado por caso

| Caso | Modelo | Alias |
|------|--------|-------|
| Conversación general | Sonnet (default) | `sonnet` |
| Heartbeats / cron | Haiku | `haiku` |
| Coding especializado | Qwen Coder | `qwen-coder` |
| Análisis de imágenes | Qwen Vision | `qwen-vision` |
| Razonamiento complejo | Opus o GLM-5 | `opus` / `glm5` |
| Sub-agents batch | Haiku o GLM-Flash | `haiku` / `glm-flash` |

## Proveedores configurados

| Provider | API | Auth | Estado |
|----------|-----|------|--------|
| anthropic | nativo | API key | ✅ |
| openai-codex | OpenAI | OAuth | ✅ |
| moonshot | openai-compat | API key | ✅ |
| zai | openai-compat | API key | ✅ ($5 créditos) |
| minimax-portal | anthropic-messages | OAuth | ✅ |
| qwen-portal | openai-compat | OAuth | ✅ |

## Notas técnicas por proveedor

### Z.AI (GLM)
- Provider correcto: `zai` (no `zhipu`)
- Endpoint: `https://api.z.ai/api/paas/v4`
- GLM-5: reasoning_content consume tokens antes de responder
- GLM-4.7-Flash: gratis, ideal como fallback ligero
- Balance monitoring: alertas cuando balance < $5 USD

### Qwen (Alibaba)
- Qwen 3.5: lanzado 15-feb-2026, 397B-A17B MoE, 1M contexto

### Canales de comunicación

| Canal | Estado | Config |
|-------|--------|--------|
| Telegram | ✅ | @KoraxBot, allowlist (Korvo: 7192195698) |
| Webhooks | ✅ | `/hooks`, preset: `gmail` |

### Credenciales (ubicaciones)

| Tipo | Ubicación |
|------|-----------|
| Google OAuth | `~/.config/gog/credentials.json` |
| OpenClaw Config | `~/.openclaw/openclaw.json` (refs a env vars via `${VAR}`) |
| Secrets | `~/.openclaw/.env` |

### gog (Google Workspace)
- Cuenta: `koraxfx@gmail.com`
- Proyecto GCP: 490503352742
- Gmail Watch Server: puerto 8788 → webhook a `http://localhost:18789/hooks/gmail`

## API Keys

**Embeddings:** OpenAI `text-embedding-3-small` (memory search, no inference)

## Proveedores eliminados

- **DashScope** (qwen3.5-plus / qwen-plus): eliminado 2026-02-24. Bugs: reasoning leak + message ordering conflict.
- **DeepSeek**: eliminado 2026-02-24. Sin API key activa, nunca operativo.
