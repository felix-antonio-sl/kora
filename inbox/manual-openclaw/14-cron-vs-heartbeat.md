---
_manifest:
  urn: urn:kora:kb:14-cron-vs-heartbeat
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.0.0
status: published
tags:
- kora
- manual-openclaw
- '14'
- cron
- vs
lang: es
---

# Capítulo 14 — Cron vs Heartbeat: Árbol de Decisión

> **Propósito:** Consolidar la decisión más frecuente de automatización — cuándo usar heartbeat, cuándo cron, y cuándo combinar ambos. Este capítulo es una referencia rápida de decisión, no una introducción (eso fue Cap. 12-13).

- ---


## 14.1 La Pregunta Correcta

- La pregunta no es "¿heartbeat o cron?" sino:


1. **¿Cuándo debe correr?** (timing)
2. **¿Qué contexto necesita?** (conversacional vs limpio)
3. **¿Cómo se entrega el resultado?** (delivery)
4. **¿Cuánto cuesta?** (tokens)

- Cada combinación de respuestas apunta a un mecanismo diferente.


- ---


## 14.2 Tabla de Decisión Rápida

| Caso de uso | Mecanismo | Por qué |
|-------------|-----------|---------|
| Revisar inbox cada 30 min | **Heartbeat** | Batch con otros checks, contexto conversacional |
| Reporte diario a las 7 AM | **Cron isolated** | Timing exacto, delivery a canal, sin polucionar main |
| Recordatorio en 20 min | **Cron main** (`--at`) | One-shot preciso, integrado con heartbeat |
| Monitorear calendario | **Heartbeat** | Check periódico natural, se batchea con inbox |
| Análisis semanal profundo | **Cron isolated** | Model override (Opus), thinking high, isolated |
| Health check de proyecto | **Heartbeat** | Piggyback en ciclo existente, bajo overhead |
| Gmail watch renewal | **Cron isolated** | Timing exacto (cada 7 días), tarea standalone |
| Check-in casual con el usuario | **Heartbeat** | Contexto-aware (sabe cuándo fue el último contacto) |
| Compilar newsletter semanal | **Cron isolated** | Tarea pesada, modelo específico, delivery a canal |
| "Recuérdame X" (usuario pide) | **Cron main** (`--at`) | One-shot, auto-delete, wake inmediato |

- ---


## 14.3 Flowchart de Decisión

```
¿Timing exacto importa?
│
├── SÍ ("a las 7 AM", "cada lunes a las 9", "en 20 min")
│   │
│   ├── ¿One-shot o recurrente?
│   │   ├── One-shot → Cron main (--at, --delete-after-run)
│   │   └── Recurrente → ¿Necesita contexto conversacional?
│   │                     ├── SÍ → Cron main (system event)
│   │                     └── NO → Cron isolated
│   │
│   └── ¿Necesita model/thinking diferente?
│       ├── SÍ → Cron isolated (--model, --thinking)
│       └── NO → (ya decidido arriba)
│
└── NO ("cada ~30 min", "periódicamente", "de vez en cuando")
    │
    ├── ¿Se puede batchear con otros checks?
    │   ├── SÍ → Heartbeat (agregar a HEARTBEAT.md)
    │   └── NO → ¿Es una tarea pesada/larga?
    │             ├── SÍ → Cron isolated
    │             └── NO → Heartbeat
    │
    └── ¿Necesita aislamiento de main session?
        ├── SÍ → Cron isolated
        └── NO → Heartbeat
```

- ---


## 14.4 Patrón Combinado: La Setup Más Eficiente

- La mayoría de los setups deberían usar **ambos** complementándose:


```
┌──────────────────────────────────────────────────────────┐
│                    HEARTBEAT (cada 30 min)                │
│                                                          │
│  HEARTBEAT.md:                                           │
│  - Scan inbox email urgentes                             │
│  - Check calendario próximas 2h                          │
│  - Revisar GTD inbox pendiente                           │
│  - Check-in si >8h sin contacto                          │
│                                                          │
│  Modelo: Haiku (barato)                                  │
│  Costo: ~$2-3/mes                                        │
│  Contexto: Ve conversación reciente                      │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│                    CRON JOBS (timing preciso)             │
│                                                          │
│  "Morning brief"   → 0 7 * * *  → isolated → telegram   │
│  "Weekly review"   → 0 9 * * 1  → isolated → opus       │
│  "Gmail renew"     → 0 6 */7 * * → isolated → haiku     │
│  (one-shot reminders bajo demanda)                       │
│                                                          │
│  Modelo: varía por job                                   │
│  Costo: ~$1-5/mes según frecuencia y modelo              │
│  Contexto: Fresh (sin historial)                         │
└──────────────────────────────────────────────────────────┘
```

### Por qué funciona

- **Heartbeat batchea** los checks periódicos simples en UN turn cada 30 min → económico
- **Cron maneja** lo que necesita precisión, aislamiento, o modelo diferente → preciso
- **No se duplican:** los checks del heartbeat NO se repiten en cron (y viceversa)
- **Costo total:** ~$3-8/mes con Haiku para heartbeats + mix de modelos para cron

### Lo que NO hacer

| Anti-patrón | Por qué es malo | Qué hacer |
|-------------|-----------------|-----------|
| 5 cron jobs que hacen lo que un heartbeat batchearía | 5 agent turns separados = 5× más caro | Consolidar en HEARTBEAT.md |
| Heartbeat cada 5 min | 288 runs/día × costo = $$$$ | Aumentar a 30m-1h |
| Cron isolated con `--model opus` para un check simple | Opus es ~20× más caro que Haiku | Usar Haiku para checks, Opus para análisis |
| Heartbeat para tarea que necesita timing exacto | El drift del heartbeat puede ser minutos | Usar cron con expression |
| Cron main con model override | Cambia el modelo de toda la sesión main | Usar cron isolated |
| Todo en heartbeat, sin cron | No puedes hacer timing preciso ni model override | Combinar ambos |

- ---


## 14.5 Comparativa de Costo

### Heartbeat (Haiku, 30 min, 15h activas/día)

```
Runs/día:       30
Tokens/run:     ~3,000 (prompt + response)
Costo Haiku:    ~$0.001/K tokens
Costo diario:   ~$0.09
Costo mensual:  ~$2.70
```

### Cron isolated: brief diario (Sonnet)

```
Runs/día:       1
Tokens/run:     ~8,000 (prompt + tools + response)
Costo Sonnet:   ~$0.015/K tokens
Costo diario:   ~$0.12
Costo mensual:  ~$3.60
```

### Cron isolated: análisis semanal (Opus)

```
Runs/semana:    1
Tokens/run:     ~25,000
Costo Opus:     ~$0.075/K tokens
Costo semanal:  ~$1.88
Costo mensual:  ~$7.50
```

### Setup combinado típico

```
Heartbeat (Haiku, 30m):        $2.70/mes
Brief diario (Sonnet):         $3.60/mes
Review semanal (Opus):         $7.50/mes
Reminders one-shot (~5/mes):   $0.50/mes
                               ─────────
Total estimado:                ~$14.30/mes
```

- **Comparado con:** 5 cron jobs aislados con Sonnet reemplazando el heartbeat → ~$18/mes (sin batching).


- ---


## 14.6 Main Session Cron vs Heartbeat

- Ambos corren en la sesión main, pero de forma diferente:


```
HEARTBEAT:
  Scheduler → Heartbeat prompt (con HEARTBEAT.md) → Agent turn → OK/alerta
  
  El agente DECIDE qué revisar basándose en HEARTBEAT.md y contexto.
  Flexible, context-aware, batched.

CRON MAIN (system event):
  Scheduler → System event inyectado → Heartbeat triggered → Agent turn
  
  El agente RECIBE un event específico que debe procesar.
  Preciso, dirigido, single-purpose.
```

### Cuándo cron main

```bash
# "Recuérdame en 20 min"
openclaw cron add --at "20m" --session main \
  --system-event "Reminder: llamar al cliente" --wake now --delete-after-run

# "Revisa el proyecto cada 4 horas"
openclaw cron add --every 14400000 --session main \
  --system-event "Time for project health check" --wake now
```

### Cuándo heartbeat

```markdown
# HEARTBEAT.md
- Si han pasado >4h sin hablar del proyecto, hacer health check
- Revisar inbox, calendario, emails
- Light check-in si >8h sin contacto
```

- **La diferencia sutil:** El cron main es **imperativo** ("haz esto ahora").
- El heartbeat es **declarativo** ("aquí está tu checklist, decide qué hacer").
- Ambos corren en main, pero el modelo de decisión es diferente.


- ---


## 14.7 Diagrama de Arquitectura Integrada

```
┌────────────────────────────────────────────────────────────┐
│                        GATEWAY                              │
│                                                             │
│  ┌──────────────┐     ┌──────────────┐                     │
│  │  HEARTBEAT    │     │  CRON        │                     │
│  │  Scheduler    │     │  Scheduler   │                     │
│  │  (every 30m)  │     │  (per job)   │                     │
│  └──────┬───────┘     └──────┬───────┘                     │
│         │                    │                              │
│         │                    ├── Main session jobs           │
│         │                    │   (system events)             │
│         │                    │        │                      │
│         ▼                    ▼        ▼                      │
│  ┌──────────────────────────────────────┐                   │
│  │         MAIN SESSION                  │                   │
│  │  (contexto conversacional)            │ ← Heartbeat runs │
│  │                                       │ ← System events  │
│  │  HEARTBEAT.md + conversación          │                   │
│  └──────────────────────────────────────┘                   │
│                                                             │
│         ┌── Isolated jobs ──┐                               │
│         │                   │                               │
│         ▼                   ▼                               │
│  ┌──────────────┐  ┌──────────────┐                        │
│  │ cron:morning  │  │ cron:weekly  │   ← Fresh sessions    │
│  │ (Sonnet)      │  │ (Opus)       │   ← Model overrides   │
│  │ → announce    │  │ → announce   │   ← Delivery control  │
│  │   telegram    │  │   telegram   │                        │
│  └──────────────┘  └──────────────┘                        │
└────────────────────────────────────────────────────────────┘
```

- ---


## Resumen del Capítulo

| Criterio | Heartbeat | Cron main | Cron isolated |
|----------|-----------|-----------|---------------|
| **Timing** | ~30m drift OK | Preciso (via wake) | Preciso (cron expr) |
| **Sesión** | Main | Main | `cron:<jobId>` fresh |
| **Contexto** | Conversacional | Conversacional + event | Ninguno (clean) |
| **Model** | Heartbeat model | Main model | Override libre |
| **Batching** | ✅ Múltiples checks | ❌ Un event | ❌ Una tarea |
| **Delivery** | Via target (last/canal) | Via heartbeat | announce/webhook/none |
| **Costo** | Bajo (1 turn batcheado) | Parte del heartbeat turn | Turn completo por job |
| **Ideal para** | Monitoring periódico | Reminders, events | Reportes, análisis, tareas pesadas |

- **Regla de oro:** Si puedes meter el check en HEARTBEAT.md sin complicarlo — hazlo ahí.
- Si necesitas timing, modelo, o aislamiento — cron.


- ---


- *Siguiente: [Capítulo 15 — Hooks (Event-Driven Automation)](15-hooks.md)*

