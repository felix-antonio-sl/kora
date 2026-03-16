---
_manifest:
  urn: urn:agengai:kb:12-heartbeats
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.0.0
status: published
tags:
- kora
- manual-openclaw
- '12'
- heartbeats
lang: es
---

# Capítulo 12 — Heartbeats

> **Propósito:** Entender los heartbeats como el mecanismo de **proactividad periódica** del agente. Un heartbeat es un agent turn programado que corre en la sesión main, revisa lo que necesita atención, y decide si notificar o callar. Es la diferencia entre un asistente reactivo y uno que trabaja para ti en background.

- ---


## 12.1 Concepto

- Un heartbeat es un **agent turn periódico** inyectado por el gateway en la sesión main del agente.
- No viene de un mensaje del usuario — viene del scheduler interno.


```
┌─────────────────────────────────────────────────────────┐
│                    HEARTBEAT CYCLE                        │
│                                                          │
│  Gateway scheduler (cada 30 min)                         │
│       │                                                  │
│       ▼                                                  │
│  ¿Dentro de activeHours?                                 │
│  ├── NO → Skip, esperar al próximo tick                  │
│  └── SÍ → ¿Main queue libre?                            │
│            ├── NO → Skip, retry después                  │
│            └── SÍ → Inyectar heartbeat prompt            │
│                      como user message en sesión main    │
│                           │                              │
│                           ▼                              │
│                    Agent run normal                       │
│                    (prompt + tools + inference)           │
│                           │                              │
│                           ▼                              │
│                    ¿Resultado?                            │
│                    ├── HEARTBEAT_OK → Silencio           │
│                    └── Alerta → Delivery al canal        │
└─────────────────────────────────────────────────────────┘
```

### Diferencia clave vs cron

| | Heartbeat | Cron job |
|--|-----------|---------|
| **Sesión** | Corre en sesión main (con todo el historial) | Sesión propia (aislada o main) |
| **Contexto** | Ve el historial de conversación reciente | Empieza fresh (si aislado) |
| **Personalidad** | Misma que la conversación (SOUL.md, etc.) | Prompt configurable |
| **Frecuencia** | Intervalo fijo (default 30m) | Cron expression, `at`, o `every` |
| **Propósito** | Monitoring + proactividad periódica | Tareas programadas específicas |
| **Cost pattern** | Tokens cada N minutos (se acumulan) | Tokens por ejecución |

- ---


## 12.2 Configuración

### Mínima

```json5
{
  agents: {
    defaults: {
      heartbeat: {
        every: "30m",       // intervalo
        target: "last"      // enviar al último canal usado
      }
    }
  }
}
```

### Completa

```json5
{
  agents: {
    defaults: {
      heartbeat: {
        every: "30m",
        model: "anthropic/claude-haiku-4-5",    // modelo barato para heartbeats
        target: "last",                          // "last" | "none" | "<channel>"
        to: "7192195698",                        // recipient override
        accountId: "default",                    // para multi-account
        prompt: "Read HEARTBEAT.md if it exists. Follow it strictly. If nothing needs attention, reply HEARTBEAT_OK.",
        ackMaxChars: 300,                        // max chars permitidos con HEARTBEAT_OK
        activeHours: {
          start: "08:00",                        // inclusive
          end: "23:00",                          // exclusive
          timezone: "America/Santiago"
        },
        includeReasoning: false,                 // enviar reasoning por separado
        suppressToolErrorWarnings: false
      }
    }
  }
}
```

### Campos

| Campo | Default | Propósito |
|-------|---------|-----------|
| `every` | `"30m"` | Intervalo entre heartbeats. `"0m"` desactiva |
| `model` | Hereda primary | Modelo para heartbeats (recomendar uno barato) |
| `target` | `"last"` | Dónde enviar alertas: `"last"` (último canal), nombre de canal, o `"none"` |
| `to` | — | Recipient específico (e.g., chat ID de Telegram, número WhatsApp) |
| `accountId` | — | Cuenta del canal (para multi-account) |
| `prompt` | (ver default) | Prompt inyectado como user message |
| `ackMaxChars` | 300 | Si reply tiene HEARTBEAT_OK + ≤N chars extra → se supprime |
| `activeHours` | — | Ventana horaria para heartbeats |
| `includeReasoning` | false | Enviar mensaje separado con reasoning del modelo |
| `session` | `"main"` | Session key override (rare) |
| `suppressToolErrorWarnings` | false | No emitir warnings de tool errors en heartbeats |

- ---


## 12.3 HEARTBEAT.md: El Checklist del Agente

- `HEARTBEAT.md` es un archivo en el workspace que el prompt default le dice al agente que lea.
- Es el **checklist periódico** — lo que el agente debe revisar en cada heartbeat.


### Ejemplo efectivo

```markdown
# HEARTBEAT

## Pasos (tool calls reales)
1. memory_get("memory/gtd/INBOX.md")
2. gog gmail search "in:inbox is:unread" --limit 5
3. gog calendar list --limit 5

## Cuándo notificar
- Inbox GTD con items >24h sin procesar
- Email urgente no leído
- Evento calendario en <2h

## Cuándo callar
- Fuera de horario (23:00-08:00)
- Nada nuevo desde último check
- Todo normal → HEARTBEAT_OK
```

### Reglas de diseño

| Regla | Por qué |
|-------|---------|
| **Mantenerlo pequeño** (<1KB) | Se inyecta en el prompt periódicamente; tokens se acumulan |
| **Instrucciones concretas** | "Ejecuta estos 3 tool calls" > "revisa si hay algo" |
| **Criterios explícitos** | "Notificar si email urgente" > "notificar si es importante" |
| **HEARTBEAT_OK como default** | El agente debe callar a menos que haya algo real |
| **Sin secretos** | Ni API keys, ni tokens, ni datos sensibles |
| **Actualizable por el agente** | El agente puede editar HEARTBEAT.md si se lo pides |

### Archivo vacío = skip

- Si HEARTBEAT.md existe pero solo tiene blank lines y headers → OpenClaw **skippea el heartbeat run** para ahorrar API calls.
- Si el archivo no existe, el heartbeat corre y el modelo decide qué hacer.


- ---


## 12.4 Response Contract: OK vs Alertas

### HEARTBEAT_OK

```
Agente responde: "HEARTBEAT_OK"
      │
      ▼
Gateway detecta HEARTBEAT_OK al inicio/final del reply
      │
      ▼
¿Texto restante ≤ ackMaxChars (300)?
├── SÍ → Reply suprimido (no se envía al canal)
└── NO → Reply se envía (con HEARTBEAT_OK stripped)
```

- **Importante:** HEARTBEAT_OK en el **medio** del reply no se trata especialmente.
- Solo al inicio o final.


### Alertas

- Si el agente encuentra algo que reportar, **no incluye HEARTBEAT_OK**:


```
✅ Correcto:
"📬 Tienes 3 emails no leídos, uno de GORE Ñuble marcado urgente.
📅 Reunión de equipo en 1h30m."

❌ Incorrecto:
"HEARTBEAT_OK - pero hay 3 emails no leídos..."
(El HEARTBEAT_OK haría que se suprima)
```

- ---


## 12.5 Delivery y Visibility

### Target: dónde van las alertas

| Target | Comportamiento |
|--------|---------------|
| `"last"` (default) | Envía al último canal externo usado en esa sesión |
| `"telegram"` | Siempre a Telegram |
| `"whatsapp"` | Siempre a WhatsApp |
| `"none"` | Corre el heartbeat pero no envía nada externamente |

- `"last"` es el más natural: si tu última conversación fue por Telegram, las alertas llegan por Telegram.
- Si fue por WhatsApp, llegan por WhatsApp.


### Visibility controls por canal

```json5
{
  channels: {
    defaults: {
      heartbeat: {
        showOk: false,      // suprimir HEARTBEAT_OK (default)
        showAlerts: true,    // entregar alertas (default)
        useIndicator: true   // emitir eventos de indicador para UIs
      }
    },
    telegram: {
      heartbeat: {
        showOk: true         // mostrar OK en Telegram (debug)
      }
    },
    whatsapp: {
      accounts: {
        work: {
          heartbeat: {
            showAlerts: false  // no alertas en WhatsApp work
          }
        }
      }
    }
  }
}
```

- **Precedencia:** per-account > per-channel > channel defaults > built-in defaults.


- **Si los tres flags son false** → OpenClaw skippea el heartbeat run completo (no gasta API call).


### Patrones comunes

| Goal | Config |
|------|--------|
| Default (OK silent, alertas sí) | _(nada, default)_ |
| Fully silent (solo internal state) | `showOk: false, showAlerts: false, useIndicator: false` |
| Solo indicador (UIs ven, chat no) | `showOk: false, showAlerts: false, useIndicator: true` |
| Debug: ver todo | `showOk: true, showAlerts: true` |
| Alertas en un canal, silencio en otro | Per-channel config |

- ---


## 12.6 Per-Agent Heartbeats

### Regla de exclusividad

- Si **cualquier** agente en `agents.list[]` tiene un bloque `heartbeat`, **solo esos agentes** corren heartbeats.
- Los demás se excluyen.


```json5
{
  agents: {
    defaults: {
      heartbeat: { every: "30m", target: "last" }  // defaults compartidos
    },
    list: [
      { id: "main" },                               // ❌ NO corre heartbeat
      { id: "ops", heartbeat: { every: "1h" } },    // ✅ SÍ corre heartbeat
      { id: "alerts", heartbeat: { every: "15m" } } // ✅ SÍ corre heartbeat
    ]
  }
}
```

- ¿Por qué?
- Si no tuviera esta regla, todos los agentes correrían heartbeats — potencialmente caro y ruidoso.


### Merge de config

- El bloque per-agent **mergea** sobre `agents.defaults.heartbeat`.
- Solo necesitas overridear lo que cambia:


```json5
agents: {
  defaults: {
    heartbeat: {
      every: "30m",
      model: "anthropic/claude-haiku-4-5",
      target: "last"
    }
  },
  list: [{
    id: "ops",
    heartbeat: {
      every: "1h",              // override: cada hora
      target: "telegram",       // override: siempre Telegram
      to: "7192195698"
      // model: hereda haiku de defaults
      // prompt: hereda default
    }
  }]
}
```

- ---


## 12.7 Active Hours

### Configuración

```json5
heartbeat: {
  activeHours: {
    start: "08:00",              // inclusive (HH:MM)
    end: "23:00",                // exclusive
    timezone: "America/Santiago" // IANA timezone
  }
}
```

### Resolución de timezone

```
¿timezone especificado en activeHours?
├── SÍ → Usar ese timezone
└── NO → ¿agents.defaults.userTimezone?
         ├── SÍ → Usar ese
         └── NO → Usar timezone del host
```

### Comportamiento fuera de ventana

```
08:00 ──────── ACTIVE ──────── 23:00
   │                              │
   │  heartbeats corren normal    │
   │  cada 30m                    │
                                  │
23:00 ──────── INACTIVE ──────── 08:00
   │                              │
   │  heartbeats skippeados       │
   │  sin API calls               │
```

### 24/7

- Omitir `activeHours` → heartbeats corren siempre.
- O explícitamente: `{ start: "00:00", end: "24:00" }`.


- **Pitfall:** `{ start: "08:00", end: "08:00" }` = ventana de ancho cero → heartbeats **siempre** skippeados.


- ---


## 12.8 Manual Wake

- Trigger inmediato de heartbeat sin esperar al próximo tick:


```bash
# Inmediato
openclaw system event --text "Check for urgent follow-ups" --mode now

# Esperar al próximo tick programado
openclaw system event --text "Run analysis" --mode next-heartbeat
```

- Si hay múltiples agentes con heartbeat configurado, el manual wake trigger **todos**.


- ---


## 12.9 Costo y Optimización

### El cálculo

```
Costo diario = heartbeats_por_día × tokens_por_heartbeat × costo_por_token

Ejemplo con Haiku (barato):
  Intervalo: 30m, activeHours: 08:00-23:00 (15h)
  Heartbeats/día: 30
  Tokens/heartbeat: ~2,500 (prompt) + ~500 (response) = ~3,000
  Costo Haiku: ~$0.001/K tokens
  
  Costo diario ≈ 30 × 3 × $0.001 = $0.09/día ≈ $2.70/mes

Ejemplo con Sonnet (default):
  Mismos params
  Costo Sonnet: ~$0.015/K tokens (promedio in+out)
  
  Costo diario ≈ 30 × 3 × $0.015 = $1.35/día ≈ $40.50/mes
```

### Optimizaciones

| Optimización | Ahorro | Trade-off |
|-------------|--------|-----------|
| Usar Haiku para heartbeats | ~15× más barato que Sonnet | Menor capacidad de razonamiento |
| Aumentar intervalo a 1h | 50% menos heartbeats | Latencia de detección mayor |
| activeHours restrictivas | Menos heartbeats por día | No-cobertura fuera de ventana |
| `target: "none"` | Sin delivery (solo internal state) | No recibes alertas |
| HEARTBEAT.md vacío/headers-only | Skip del run completo | Sin monitoring |
| HEARTBEAT.md lean (3 checks) | ~1,500 tokens por run | Menos cobertura |

### Recomendación

```json5
heartbeat: {
  every: "30m",
  model: "anthropic/claude-haiku-4-5",    // 15× más barato
  activeHours: { start: "08:00", end: "23:00" },
  target: "last"
}
```

- Costo estimado: ~$2-3/mes.
- Un buen balance entre proactividad y presupuesto.


- ---


## 12.10 Reasoning Delivery

```json5
heartbeat: {
  includeReasoning: true
}
```

- Cuando habilitado, el heartbeat envía **dos mensajes**:


1. El reply normal (alerta o HEARTBEAT_OK)
2. Un mensaje separado con `Reasoning:` (el thinking interno del modelo)

- **Útil para:** Debug, transparencia, entender por qué el agente decidió notificar o no.


- **Riesgo:** Puede exponer detalles internos.
- No habilitar en grupos.


- ---


## Resumen del Capítulo

| Concepto | Decisión de diseño que habilita |
|----------|--------------------------------|
| **Heartbeat = agent turn en main session** | El agente ve todo el contexto conversacional reciente |
| **HEARTBEAT_OK contract** | Silencio como default; alertas solo cuando hay valor |
| **HEARTBEAT.md editable** | Checklist evolutivo sin tocar config |
| **Modelo barato (Haiku)** | 15× reducción de costo vs primary model |
| **activeHours** | Respeta horarios; sin spam nocturno |
| **Per-agent heartbeats exclusivos** | Solo los agentes que lo necesitan lo corren |
| **Visibility per-channel** | OK en un canal, alertas en otro, silencio en un tercero |
| **target: "last"** | Alertas llegan donde estás, no a un canal fijo |
| **Manual wake** | Trigger inmediato sin esperar el scheduler |
| **HEARTBEAT.md vacío = skip** | Ahorro automático cuando no hay nada que revisar |

- ---


- *Siguiente: [Capítulo 13 — Cron Jobs](13-cron-jobs.md)*

