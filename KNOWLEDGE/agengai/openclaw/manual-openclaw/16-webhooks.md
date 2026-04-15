---
_manifest:
  urn: urn:agengai:kb:16-webhooks
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.1.0
status: published
tags:
- kora
- manual-openclaw
- '16'
- webhooks
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:agengai:kb:16-webhooks
---

# Capítulo 16 — Webhooks (External Triggers)

> **Propósito:** Entender cómo sistemas externos pueden trigger acciones en el gateway via HTTP. Los webhooks son la puerta de entrada para integraciones: Gmail Pub/Sub, CI/CD, monitoring, IoT, o cualquier sistema que pueda hacer un HTTP POST.

- ---

## 16.1 Concepto: HTTP Ingress para el Gateway

- Los webhooks exponen endpoints HTTP en el gateway que sistemas externos pueden llamar para:

1. **Despertar al agente** (wake) → inyectar un system event en la sesión main
2. **Ejecutar un agent turn** (agent) → run aislado con delivery configurable
3. **Mapear payloads custom** (mapped hooks) → transformar payloads arbitrarios en wake/agent

```
Sistema externo Gateway
┌──────────────┐ ┌──────────────────┐
│ │ POST /hooks/* │ │
│ Gmail │ ────────────────►│ Webhook Ingress │
│ Pub/Sub │ + Bearer token │ │
│ │ │ ├── /hooks/wake │
│ CI/CD │ │ ├── /hooks/agent │
│ │ │ └── /hooks/<name>│
│ Custom │ │ │ │
│ scripts │ │ ▼ │
└──────────────┘ │ Agent turn o │
 │ system event │
 │ │ │
 │ ▼ │
 │ Delivery a │
 │ canal (opcional) │
 └──────────────────┘
```

- ---

## 16.2 Habilitación y Auth

### Config mínima

```json5
{
 hooks: {
 enabled: true,
 token: "${OPENCLAW_HOOKS_TOKEN}", // requerido
 path: "/hooks", // default
 allowedAgentIds: ["main"], // opcional: restringir routing
 }
}
```

### Autenticación

- Toda request debe incluir el token.
- Dos métodos:

```bash
# Método recomendado: header Authorization
curl -H 'Authorization: Bearer SECRET' ...

# Alternativa: header custom
curl -H 'x-openclaw-token: SECRET' ...
```

- **Query string rechazado:** `?token=...` retorna `400`.
- Tokens en URL se pueden loguear, cachear, y filtrar.

### Rate limiting

- Auth failures repetidos desde la misma IP → `429 Too Many Requests` con `Retry-After`.
- Protección contra brute-force.

- ---

## 16.3 Endpoint: /hooks/wake

### Qué hace

- Inyecta un **system event** en la sesión main y opcionalmente trigger un heartbeat inmediato.
- No crea una sesión nueva — va a la sesión main existente.

### Payload

```json
{
 "text": "New email from GORE Ñuble: Convocatoria urgente",
 "mode": "now"
}
```

| Campo | Requerido | Default | Propósito |
|-------|-----------|---------|-----------|
| `text` | ✅ | — | Descripción del evento |
| `mode` | No | `"now"` | `"now"` = heartbeat inmediato; `"next-heartbeat"` = espera al próximo tick |

### Respuesta

```
200 OK
```

### Caso de uso

```bash
# Gmail Pub/Sub notifica un email nuevo
curl -X POST http://127.0.0.1:18789/hooks/wake \
 -H 'Authorization: Bearer SECRET' \
 -H 'Content-Type: application/json' \
 -d '{"text":"New email received from koraxfx@gmail.com","mode":"now"}'
```

- El agente recibe el system event en su próximo turn (inmediato si `mode=now`), ve el texto, y decide qué hacer (leer el email, notificar, ignorar).

- ---

## 16.4 Endpoint: /hooks/agent

### Qué hace

- Ejecuta un **agent turn aislado** (propia sesión) con delivery configurable.
- Es como `sessions_spawn` pero triggered desde fuera.

### Payload

```json
{
 "message": "Summarize this email and notify me if urgent",
 "name": "Gmail",
 "agentId": "main",
 "sessionKey": "hook:gmail:msg-123",
 "wakeMode": "now",
 "deliver": true,
 "channel": "telegram",
 "to": "7192195698",
 "model": "anthropic/claude-haiku-4-5",
 "thinking": "low",
 "timeoutSeconds": 120
}
```

| Campo | Requerido | Default | Propósito |
|-------|-----------|---------|-----------|
| `message` | ✅ | — | Prompt para el agente |
| `name` | No | — | Nombre human-readable (prefix en summaries) |
| `agentId` | No | Default agent | Rutear a un agente específico |
| `sessionKey` | No | Rechazado por default | Solo se acepta si `hooks.allowRequestSessionKey: true` |
| `wakeMode` | No | `"now"` | Cuándo postear summary a main session |
| `deliver` | No | `true` | Enviar respuesta al canal de messaging |
| `channel` | No | `"last"` | Canal de delivery |
| `to` | No | Último recipient | Target de delivery |
| `model` | No | Default | Override de modelo |
| `thinking` | No | Default | Override de thinking level |
| `timeoutSeconds` | No | Default | Timeout del agent run |

### Respuesta

```
200 OK
```

- Async igual: el run se acepta y sigue en background.

### Flujo

```
POST /hooks/agent
 │
 ▼
Auth check → ¿Token válido?
├── NO → 401
└── SÍ → Crear sesión hook:<key>
 │
 ▼
 Agent turn aislado
 (con model/thinking override si especificado)
 │
 ▼
 ¿deliver=true?
 ├── SÍ → Enviar respuesta al canal
 └── NO → Solo interno
 │
 ▼
 Summary posteado a main session
 (controlado por wakeMode)
```

- ---

## 16.4.1 Session Key Policy (breaking change)

- La documentación oficial actual endurece este punto:
- `sessionKey` override en `/hooks/agent` viene **deshabilitado por default**.
- Recomendación: fijar un `hooks.defaultSessionKey` y no permitir overrides del caller.

```json5
{
 hooks: {
 enabled: true,
 token: "${OPENCLAW_HOOKS_TOKEN}",
 defaultSessionKey: "hook:ingress",
 allowRequestSessionKey: false,
 allowedSessionKeyPrefixes: ["hook:"]
 }
}
```

- Si necesitas compatibilidad legacy:

```json5
{
 hooks: {
 allowRequestSessionKey: true,
 allowedSessionKeyPrefixes: ["hook:"]
 }
}
```

## 16.5 Mapped Hooks: /hooks/\<name\>

### Concepto

- Los mapped hooks transforman payloads arbitrarios en acciones `wake` o `agent`.
- Esto permite integrar cualquier sistema que envíe JSON.

### Presets

```json5
{
 hooks: {
 presets: ["gmail"] // habilita /hooks/gmail con mapping built-in
 }
}
```

### Mappings custom

```json5
{
 hooks: {
 mappings: [
 {
 name: "github",
 match: { source: "github" }, // matchea payload.source === "github"
 action: "agent",
 message: "GitHub event: {{event.action}} on {{event.repository.name}}",
 deliver: true,
 channel: "telegram",
 to: "7192195698",
 agentId: "main"
 },
 {
 name: "health-alert",
 match: { source: "monitoring" },
 action: "wake",
 text: "Health alert: {{alert.message}}"
 }
 ]
 }
}
```

### Transform modules (lógica compleja)

- Para transformaciones que necesitan código:

```json5
{
 hooks: {
 transformsDir: "~/.openclaw/hooks/transforms",
 mappings: [{
 name: "complex-hook",
 match: { source: "custom" },
 action: "agent",
 transform: { module: "custom-transform" } // loads custom-transform.ts
 }]
 }
}
```

```typescript
// ~/.openclaw/hooks/transforms/custom-transform.ts
export default function transform(payload: any) {
 return {
 message: `Process: ${payload.data.title}`,
 model: payload.priority === "high" ? "opus" : "haiku"
 };
}
```

- **Seguridad:** `transformsDir` debe estar dentro del directorio de config de OpenClaw.
- Paths que escapen son rechazados.

- ---
