---
_manifest:
  urn: urn:agengai:kb:05-memoria
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.1.0
status: published
tags:
- kora
- manual-openclaw
- '05'
- memoria
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:agengai:kb:05-memoria
---

# Capítulo 5 — Memoria

> **Propósito:** Entender cómo un agente "recuerda" entre sesiones, cómo se indexa y busca esa memoria, y qué decisiones de configuración afectan la calidad del recall. La memoria es lo que transforma un chatbot stateless en un asistente con continuidad — y hacerlo bien requiere entender tanto el diseño de archivos como la infraestructura de búsqueda.

- ---

## 5.1 El Modelo Mental: Dos Capas de Memoria

- Un agente OpenClaw tiene **dos memorias radicalmente diferentes** que se complementan:

```
┌─────────────────────────────────────────────────────────────────┐
│ CONTEXT WINDOW (efímera) │
│ │
│ Todo lo que el modelo "ve" en este momento: │
│ • System prompt + bootstrap files │
│ • Historial de conversación (esta sesión) │
│ • Tool results acumulados │
│ │
│ Se pierde con: /new, /reset, compaction (parcial) │
│ Capacidad: 128K-1M tokens según modelo │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ PERSISTENT MEMORY (durable) │
│ │
│ Archivos Markdown en disco: │
│ • MEMORY.md (curada, inyectada en main) │
│ • memory/YYYY-MM-DD.md (daily logs, on-demand) │
│ • memory/gtd/*.md (productividad, on-demand) │
│ • memory/**/*.md (cualquier estructura, on-demand) │
│ │
│ Acceso: memory_search (semántico) + memory_get (lectura) │
│ Sobrevive a: resets, compactions, reinicios del gateway │
│ Se pierde solo si: se borra el archivo de disco │
└─────────────────────────────────────────────────────────────────┘
```

### La distinción fundamental

| | MEMORY.md | memory/*.md |
|--|-----------|------------|
| **Inyección** | Automática (cada turn de sesión main) | Nunca — solo via `memory_get` |
| **Costo por turn** | ~tokens(contenido) en cada interacción | Cero hasta que se lee explícitamente |
| **Ideal para** | Hechos que el agente necesita SIEMPRE (quién es el usuario, proyectos activos, decisiones) | Notas diarias, logs, detalles contextuales, historial |
| **Riesgo** | Crecimiento → más tokens por turn → compaction más frecuente | Crecimiento → solo afecta el tamaño del índice vectorial |
| **Visibilidad** | Solo en sesión main (privada) | Accesible desde cualquier sesión (via tools) |
| **Frecuencia de edición** | Periódica (curación manual o en heartbeats) | Frecuente (append en cada sesión activa) |

### Regla de diseño

> **Si el agente necesita saberlo en TODA interacción → MEMORY.md.**
> **Si el agente necesita encontrarlo cuando sea relevante → memory/*.md.**

- Un error común es poner todo en MEMORY.md.
- Si crece a 20KB (~5,000 tokens), esos tokens se consumen en CADA turn.
- Mover detalles a daily logs y mantener MEMORY.md como un "índice curado" es la optimización más impactante.

- ---

## 5.2 Anatomía de los Memory Files

### MEMORY.md — Memoria de largo plazo curada

```markdown
# MEMORY.md — Long-Term Memory

## Mi usuario
- Nombre: Félix
- Roles: Médico + Ingeniero de sistemas
- Timezone: Chile (UTC-3/UTC-4)

## Proyectos activos
| Proyecto | Estado | Última actividad |
|----------|--------|-----------------|
| GoreOS | Activo | 2026-02-18 |

## Decisiones importantes
- 2026-02-19: Fallback chain simplificada a sonnet→kimi→glm5
- 2026-02-19: Sandbox mode off (decisión consciente, documentada)

## Preferencias
- Respuestas directas, sin formalidades
- Español semiformal
```

- **Buenas prácticas:**

- Mantener <10KB (~2,500 tokens)
- Estructura con headers para scan rápido
- Solo hechos durables — si cambia cada semana, no va aquí
- Revisar periódicamente (en heartbeats) para podar lo obsoleto

### memory/YYYY-MM-DD.md — Daily logs

```markdown
# 2026-02-20

## Sesión mañana (14:30 Chile)
- Korvo pidió manual de agentes OpenClaw
- Diseñamos TOC de 21 capítulos + apéndices
- Capítulos 1-4 escritos → cabinet/docs/manual-openclaw/

## Decisiones
- Manual va en cabinet/docs/ (no en memory/)
- Formato: fundamentos + nociones para toma de decisiones

## Para recordar
- Gmail watch expira 26-feb → renovar antes
```

- **Buenas prácticas:**

- Un archivo por día (append-only durante el día)
- Separar por sesión/tema con headers
- Incluir decisiones explícitamente (son lo más valioso para recall futuro)
- No replicar contenido completo — solo resúmenes y hechos clave

### Estructura libre bajo memory/

```
memory/
├── 2026-02-20.md ← daily log
├── 2026-02-19.md
├── 2026-02-18.md
├── gtd/ ← sistema de productividad
│ ├── INBOX.md
│ ├── NEXT.md
│ ├── PROJECTS.md
│ ├── WAITING.md
│ └── SOMEDAY.md
├── heartbeat-state.json ← estado de heartbeats
└── koda/ ← índices de proyecto
 └── koda-index.md
```

- Todo lo que esté bajo `memory/` con extensión `.md` es indexado automáticamente por el vector search.
- Puedes crear cualquier estructura que tenga sentido para tu caso de uso.

- ---

## 5.3 Memory Tools: search y get

- El agente accede a la memoria persistente con dos tools:

### memory_search — Búsqueda semántica

```json
{
 "tool": "memory_search",
 "params": {
 "query": "decisión sobre fallback chain de modelos",
 "maxResults": 5,
 "minScore": 0.3
 }
}
```

- **Retorna:** snippets (~700 chars), file path, line range, score, provider/model de embeddings.

- **NO retorna:** el archivo completo.
- Solo fragmentos relevantes con suficiente contexto para decidir si leer más.

### memory_get — Lectura directa

```json
{
 "tool": "memory_get",
 "params": {
 "path": "memory/2026-02-20.md",
 "from": 15,
 "lines": 30
 }
}
```

- **Retorna:** contenido del archivo (o segmento).
- Solo acepta paths dentro de `MEMORY.md` o `memory/`.

### Flujo típico de recall

```
Usuario pregunta: "¿Qué decidimos sobre la cadena de modelos?"
 │
 ▼
Agente ejecuta: memory_search("decisión fallback chain modelos")
 │
 ▼
Resultados:
 1. MEMORY.md#L45 (score 0.89) — "Fallback chain simplificada..."
 2. memory/2026-02-20.md#L12 (score 0.82) — "Cadena corregida: sonnet→kimi→glm5"
 3. memory/2026-02-19.md#L78 (score 0.71) — "qwen-plus removido de fallbacks..."
 │
 ▼
Agente opcionalmente ejecuta: memory_get("memory/2026-02-20.md", from=10, lines=20)
 │
 ▼
Agente responde con contexto completo de la decisión
```

- ---
