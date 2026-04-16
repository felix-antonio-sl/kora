# Capítulo 5 — Memoria

> **Propósito:** Entender cómo un agente "recuerda" entre sesiones, cómo se indexa y busca esa memoria, y qué decisiones de configuración afectan la calidad del recall. La memoria es lo que transforma un chatbot stateless en un asistente con continuidad — y hacerlo bien requiere entender tanto el diseño de archivos como la infraestructura de búsqueda.

---

## 5.1 El Modelo Mental: Dos Capas de Memoria

Un agente OpenClaw tiene **dos memorias radicalmente diferentes** que se complementan:

```
┌─────────────────────────────────────────────────────────────────┐
│                    CONTEXT WINDOW (efímera)                      │
│                                                                 │
│  Todo lo que el modelo "ve" en este momento:                    │
│  • System prompt + bootstrap files                              │
│  • Historial de conversación (esta sesión)                      │
│  • Tool results acumulados                                      │
│                                                                 │
│  Se pierde con: /new, /reset, compaction (parcial)              │
│  Capacidad: 128K-1M tokens según modelo                        │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                    PERSISTENT MEMORY (durable)                   │
│                                                                 │
│  Archivos Markdown en disco:                                    │
│  • MEMORY.md (curada, inyectada en main)                       │
│  • memory/YYYY-MM-DD.md (daily logs, on-demand)                │
│  • memory/gtd/*.md (productividad, on-demand)                  │
│  • memory/**/*.md (cualquier estructura, on-demand)            │
│                                                                 │
│  Acceso: memory_search (semántico) + memory_get (lectura)      │
│  Sobrevive a: resets, compactions, reinicios del gateway        │
│  Se pierde solo si: se borra el archivo de disco               │
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

Un error común es poner todo en MEMORY.md. Si crece a 20KB (~5,000 tokens), esos tokens se consumen en CADA turn. Mover detalles a daily logs y mantener MEMORY.md como un "índice curado" es la optimización más impactante.

---

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
| GoreOS   | Activo | 2026-02-18      |

## Decisiones importantes
- 2026-02-19: Fallback chain simplificada a sonnet→kimi→glm5
- 2026-02-19: Sandbox mode off (decisión consciente, documentada)

## Preferencias
- Respuestas directas, sin formalidades
- Español semiformal
```

**Buenas prácticas:**
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

**Buenas prácticas:**
- Un archivo por día (append-only durante el día)
- Separar por sesión/tema con headers
- Incluir decisiones explícitamente (son lo más valioso para recall futuro)
- No replicar contenido completo — solo resúmenes y hechos clave

### Estructura libre bajo memory/

```
memory/
├── 2026-02-20.md           ← daily log
├── 2026-02-19.md
├── 2026-02-18.md
├── gtd/                     ← sistema de productividad
│   ├── INBOX.md
│   ├── NEXT.md
│   ├── PROJECTS.md
│   ├── WAITING.md
│   └── SOMEDAY.md
├── heartbeat-state.json     ← estado de heartbeats
└── koda/                    ← índices de proyecto
    └── koda-index.md
```

Todo lo que esté bajo `memory/` con extensión `.md` es indexado automáticamente por el vector search. Puedes crear cualquier estructura que tenga sentido para tu caso de uso.

---

## 5.3 Memory Tools: search y get

El agente accede a la memoria persistente con dos tools:

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

**Retorna:** snippets (~700 chars), file path, line range, score, provider/model de embeddings.

**NO retorna:** el archivo completo. Solo fragmentos relevantes con suficiente contexto para decidir si leer más.

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

**Retorna:** contenido del archivo (o segmento). Solo acepta paths dentro de `MEMORY.md` o `memory/`.

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

---

## 5.4 Búsqueda Híbrida: Vector + BM25

La memoria se busca con **dos señales complementarias** que se combinan:

### ¿Por qué dos señales?

| Tipo de query | Vector search (semántico) | BM25 (keyword) |
|---------------|--------------------------|-----------------|
| "¿Qué decidimos sobre el setup de red?" | ✅ Excelente (parafraseo) | ❌ Mediocre (no dice "red" exacto) |
| "error sqlite-vec unavailable" | ❌ Mediocre (tokens técnicos) | ✅ Excelente (match exacto) |
| "ANTHROPIC_API_KEY" | ❌ Malo (no es lenguaje natural) | ✅ Perfecto (match de token) |
| "cómo configuré el router" | ✅ Bueno | ✅ Bueno |

**Vector search** convierte query y documentos en vectores de embeddings y compara por distancia coseno. Es fuerte en paráfrasis ("setup de red" ≈ "configuré el router") pero débil en tokens exactos.

**BM25** es búsqueda full-text clásica (TF-IDF). Es fuerte en tokens exactos ("sqlite-vec", "ANTHROPIC_API_KEY") pero no entiende sinónimos.

### Cómo se combinan

```
1. Recuperar candidatos de ambos lados:
   Vector: top (maxResults × candidateMultiplier) por cosine similarity
   BM25:   top (maxResults × candidateMultiplier) por FTS5 rank

2. Normalizar scores:
   vectorScore: ya es 0..1 (cosine similarity)
   textScore: 1 / (1 + max(0, bm25Rank))

3. Unión por chunk ID + score ponderado:
   finalScore = vectorWeight × vectorScore + textWeight × textScore

4. Ordenar por finalScore descendente → top maxResults
```

### Configuración

```json5
{
  agents: {
    defaults: {
      memorySearch: {
        query: {
          hybrid: {
            enabled: true,          // default: true
            vectorWeight: 0.7,      // 70% semántico
            textWeight: 0.3,        // 30% keyword
            candidateMultiplier: 4  // pool de candidatos = 4× maxResults
          }
        }
      }
    }
  }
}
```

**Ajuste de pesos:** Si tu memoria es mayormente texto narrativo (diarios, decisiones) → vectorWeight alto (0.7-0.8). Si tiene mucho código, IDs, variables de entorno → textWeight más alto (0.4-0.5).

---

## 5.5 Post-Procesamiento: MMR y Temporal Decay

Después de la búsqueda híbrida, dos filtros opcionales refinan los resultados:

```
Vector + BM25 → Weighted Merge → Temporal Decay → Sort → MMR → Top-K Results
```

### MMR (Maximal Marginal Relevance) — Diversidad

**Problema:** Si buscas "configuración del router", podrías obtener 5 snippets de 5 daily logs diferentes que todos dicen lo mismo ("Configuré el router Omada, VLAN 10 para IoT").

**Solución:** MMR penaliza resultados que son demasiado similares a los ya seleccionados:

```
score_mmr = λ × relevancia − (1−λ) × max_similitud_con_ya_seleccionados
```

```
Sin MMR:                           Con MMR (λ=0.7):
1. 2026-02-10 "router VLAN 10"    1. 2026-02-10 "router VLAN 10"
2. 2026-02-08 "router VLAN 10"    2. memory/network.md "referencia red"
3. memory/network.md "ref red"     3. 2026-02-05 "AdGuard DNS setup"
```

El near-duplicate del 8 de febrero cae; el agente obtiene tres piezas distintas de información.

```json5
mmr: {
  enabled: true,    // default: false
  lambda: 0.7       // 0 = máx diversidad, 1 = máx relevancia
}
```

### Temporal Decay — Boost de recencia

**Problema:** Una nota de hace 6 meses con wording perfecto puede superar a una nota de ayer con la información actualizada.

**Solución:** Multiplica el score por un factor exponencial de decay:

```
decayedScore = score × e^(-λ × ageInDays)
donde λ = ln(2) / halfLifeDays
```

Con halfLife=30 días:

| Antigüedad | Multiplicador |
|------------|--------------|
| Hoy | 100% |
| 7 días | ~84% |
| 30 días | 50% |
| 90 días | 12.5% |
| 180 días | ~1.6% |

**Archivos "evergreen" nunca decaen:**
- `MEMORY.md` (root memory)
- Archivos no-datados en `memory/` (e.g., `memory/projects.md`, `memory/network.md`)
- Estos contienen información de referencia que siempre debe rankear normalmente

**Archivos datados** (`memory/YYYY-MM-DD.md`) usan la fecha del filename. Otros fuentes (e.g., transcripts de sesión) usan mtime.

```json5
temporalDecay: {
  enabled: true,       // default: false
  halfLifeDays: 30     // score se reduce a la mitad cada 30 días
}
```

### Cuándo habilitar cada uno

| Situación | MMR | Temporal Decay |
|-----------|-----|---------------|
| Pocas notas (<50 archivos) | No necesario | No necesario |
| Muchos daily logs con contenido repetitivo | ✅ Sí | Opcional |
| Meses de historial, info vieja outranks nueva | Opcional | ✅ Sí |
| Daily logs abundantes + historial largo | ✅ Sí | ✅ Sí |

---

## 5.6 Embedding Providers

Los embeddings son las representaciones vectoriales que hacen posible la búsqueda semántica. OpenClaw soporta múltiples providers:

### Providers disponibles

| Provider | Modelo default | Costo | Calidad | Notas |
|----------|---------------|-------|---------|-------|
| **OpenAI** | `text-embedding-3-small` | Bajo (~$0.02/1M tokens) | Muy buena | Default. Batch API para indexación barata |
| **Gemini** | `gemini-embedding-001` | Bajo | Buena | Nativo, no requiere OpenAI key |
| **Voyage** | Voyage default | Medio | Excelente | Especializado en embeddings |
| **Local** | GGUF via node-llama-cpp | Gratis (CPU/GPU local) | Variable | Sin llamadas externas. ~0.6GB modelo default |
| **Custom** | Configurable | Variable | Variable | Cualquier endpoint OpenAI-compatible |

### Auto-selección

Si no configuras provider, OpenClaw auto-selecciona en este orden:
1. `local` si hay `modelPath` configurado y el archivo existe
2. `openai` si hay API key de OpenAI disponible
3. `gemini` si hay API key de Gemini
4. `voyage` si hay API key de Voyage
5. Disabled (sin memory search)

### Configuración

```json5
{
  agents: {
    defaults: {
      memorySearch: {
        provider: "openai",               // o "gemini", "local", "voyage"
        model: "text-embedding-3-small",
        fallback: "openai",               // fallback si el primary falla
        remote: {
          apiKey: "${OPENAI_API_KEY}",
          // Para endpoint custom:
          // baseUrl: "https://api.example.com/v1/",
          // headers: { "X-Custom": "value" }
        }
      }
    }
  }
}
```

### Reindexación automática

El índice almacena el **fingerprint** del provider/modelo/endpoint + parámetros de chunking. Si cualquiera de estos cambia, OpenClaw **reindexa automáticamente** todo el store. Esto significa que cambiar de OpenAI a Gemini embeddings trigger un reindex completo.

### Embedding cache

Para evitar re-embeddear texto que no cambió (especialmente útil para session transcripts):

```json5
memorySearch: {
  cache: {
    enabled: true,      // default: true
    maxEntries: 50000
  }
}
```

### Batch indexing (OpenAI + Gemini)

Para corpus grandes, OpenAI Batch API es significativamente más barato y rápido:

```json5
memorySearch: {
  remote: {
    batch: {
      enabled: true,       // default: false
      concurrency: 2,      // jobs paralelos
      // wait, pollIntervalMs, timeoutMinutes disponibles
    }
  }
}
```

---

## 5.7 Almacenamiento e Indexación

### SQLite store (default)

```
~/.openclaw/memory/<agentId>.sqlite
```

El índice vive en SQLite con:
- Chunks de ~400 tokens con 80 tokens de overlap
- Vectores almacenados (si sqlite-vec disponible) o en memoria
- FTS5 para BM25 full-text search
- Metadata: path, line range, provider/model fingerprint

### sqlite-vec (aceleración vectorial)

Cuando disponible, sqlite-vec almacena embeddings en una tabla virtual (`vec0`) y hace vector distance queries en la DB — sin cargar todo a JS.

```json5
memorySearch: {
  store: {
    vector: {
      enabled: true,    // default: true
      // extensionPath: "/path/to/sqlite-vec"  // override si necesario
    }
  }
}
```

Si sqlite-vec no está disponible, OpenClaw usa cosine similarity in-process (más lento para corpus grandes, pero funcional).

### Sincronización

- **Watcher:** OpenClaw observa `MEMORY.md` + `memory/` por cambios (debounce 1.5s)
- **Sync triggers:** al inicio de sesión, en cada search, y por intervalo configurable
- **Async:** la sincronización corre en background; los resultados de búsqueda pueden estar ligeramente desactualizados hasta que termine

---

## 5.8 QMD Backend (Experimental)

QMD es un sidecar de búsqueda local-first que combina BM25 + vectors + reranking, como alternativa al SQLite manager built-in.

### Cuándo considerar QMD

| Criterio | SQLite (default) | QMD |
|----------|------------------|-----|
| Setup | Zero-config | Requiere instalar CLI + Bun |
| Búsqueda | Hybrid (vector + BM25) | Hybrid + reranking local |
| Calidad de resultados | Buena | Potencialmente mejor (reranking) |
| Corpus size | Adecuado hasta ~10K chunks | Diseñado para corpus más grandes |
| Dependencias | Ninguna extra | `qmd` CLI, Bun, SQLite con extensions |
| Paths adicionales | `memorySearch.extraPaths` | `memory.qmd.paths` (más flexible) |

### Configuración básica

```json5
{
  memory: {
    backend: "qmd",
    citations: "auto",    // "auto" | "on" | "off"
    qmd: {
      includeDefaultMemory: true,
      update: { interval: "5m", debounceMs: 15000 },
      limits: { maxResults: 6, timeoutMs: 4000 },
      paths: [
        { name: "docs", path: "~/notes", pattern: "**/*.md" }
      ]
    }
  }
}
```

### Fallback automático

Si QMD falla (CLI no encontrado, JSON parse error, timeout), OpenClaw cae automáticamente al SQLite manager built-in. No hay pérdida de servicio.

---

## 5.9 Session Memory Search (Experimental)

Normalmente, `memory_search` solo busca en archivos Markdown. Con esta feature experimental, también puede buscar en **transcripts de sesiones pasadas**:

```json5
{
  agents: {
    defaults: {
      memorySearch: {
        experimental: { sessionMemory: true },
        sources: ["memory", "sessions"]
      }
    }
  }
}
```

### Qué indexa

- Turns de User + Assistant de los JSONL de sesión
- Indexación asíncrona con delta thresholds (no en cada mensaje)
- Aislado per-agent (solo las sesiones de ese agente)

### Cuándo es útil

- "¿Qué hablamos la semana pasada sobre X?" — si nadie escribió una nota, el transcript puede tener la respuesta
- Recall de conversaciones que no se documentaron explícitamente
- Complemento (no reemplazo) de daily logs bien escritos

### Limitaciones

- `memory_get` sigue limitado a archivos Markdown (no puede leer transcripts directamente)
- Los resultados pueden estar ligeramente desactualizados (indexación async)
- Los transcripts en disco son legibles por cualquier proceso con acceso al filesystem

---

## 5.10 Extra Memory Paths

Puedes indexar archivos Markdown fuera del layout default:

```json5
{
  agents: {
    defaults: {
      memorySearch: {
        extraPaths: [
          "../team-docs",                    // relativo al workspace
          "/srv/shared-notes/overview.md"    // absoluto
        ]
      }
    }
  }
}
```

- Directorios se escanean recursivamente buscando `.md`
- Symlinks se ignoran
- Solo Markdown

Para QMD, usa `memory.qmd.paths` con más opciones (pattern matching, nombres de colección).

---

## 5.11 Memory Scope (Restringir por Sesión)

Por defecto, `memory_search` está disponible en sesiones DM (directas). En grupos puede ser un riesgo de privacidad. El scope controla dónde funciona:

```json5
{
  memory: {
    qmd: {
      scope: {
        default: "deny",
        rules: [
          { action: "allow", match: { chatType: "direct" } },
          { action: "deny", match: { keyPrefix: "discord:channel:" } }
        ]
      }
    }
  }
}
```

Cuando scope deniega una búsqueda, el tool retorna vacío (no error) y OpenClaw loggea un warning para debugging.

---

## 5.12 Memory Flush Pre-Compaction

Este mecanismo conecta la memoria con la compaction (Cap. 3):

```
Sesión se acerca al límite de contexto
      │
      ▼
¿memoryFlush habilitado?
├── NO → Compaction directa (se pierde contexto no documentado)
│
└── SÍ → Turn silencioso:
         System: "Session nearing compaction. Store durable memories now."
         User: "Write lasting notes to memory/YYYY-MM-DD.md; reply NO_REPLY."
              │
              ▼
         El modelo escribe a disco lo que considera importante
              │
              ▼
         Compaction procede normalmente
         (lo escrito a disco sobrevive; lo no escrito se resume)
```

**Esto es una red de seguridad, no una garantía.** La calidad depende de:
- Que el modelo identifique correctamente qué es importante
- Que tenga acceso de escritura al workspace (no funciona con `workspaceAccess: "ro"` o `"none"`)
- Que el `softThresholdTokens` dé suficiente margen (default 4,000 tokens antes del hard limit)

---

## 5.13 Citations

`memory_search` puede incluir footers de citación en los snippets:

```json5
{ memory: { citations: "auto" } }   // "auto" | "on" | "off"
```

- `auto`/`on`: snippets incluyen `Source: <path#line>` para verificabilidad
- `off`: el path se envía internamente (para `memory_get`) pero no aparece en el snippet

---

## Resumen del Capítulo

| Concepto | Decisión de diseño que habilita |
|----------|--------------------------------|
| **MEMORY.md inyectado vs memory/*.md on-demand** | Control fino de costo por turn vs recall cuando necesario |
| **MEMORY.md solo en sesión main** | Privacidad por defecto — no se filtra a grupos |
| **Búsqueda híbrida (vector + BM25)** | Recall robusto tanto para lenguaje natural como tokens exactos |
| **MMR** | Elimina duplicados/near-duplicates del recall |
| **Temporal decay** | Info reciente gana por defecto sin eliminar lo antiguo |
| **Múltiples embedding providers** | Flexibilidad: pagar OpenAI, o correr local, o usar Gemini gratis |
| **Reindexación automática al cambiar provider** | Consistencia garantizada; no hay embeddings "mixtos" |
| **SQLite + sqlite-vec** | Búsqueda vectorial eficiente sin infraestructura externa |
| **QMD como alternativa** | Reranking local para mejor calidad en corpus grandes |
| **Session memory search** | Recall de conversaciones no documentadas |
| **Memory flush pre-compaction** | Red de seguridad contra pérdida de contexto |
| **Memory scope** | Privacidad: memory search solo donde corresponde |

### Diagrama de arquitectura de memoria

```
┌────────────────────────────────────────────────────────────────┐
│                    AGENT WORKSPACE                              │
│                                                                 │
│  MEMORY.md ──── inyectado ────► System prompt (cada turn)      │
│                                                                 │
│  memory/                                                        │
│  ├── 2026-02-20.md ─┐                                          │
│  ├── 2026-02-19.md  ├── indexados ──► SQLite/QMD index         │
│  ├── gtd/INBOX.md   │                    │                     │
│  └── ...            ┘                    │                     │
│                                          ▼                     │
│  Extra paths ────── indexados ──► memory_search (hybrid)       │
│                                     │          │               │
│                              ┌──────┘          └──────┐        │
│                              ▼                        ▼        │
│                        Vector search            BM25 search    │
│                        (embeddings)            (full-text)     │
│                              │                        │        │
│                              └──────┬─────────────────┘        │
│                                     ▼                          │
│                              Weighted merge                    │
│                                     │                          │
│                              Temporal decay (opt)              │
│                                     │                          │
│                              MMR re-rank (opt)                 │
│                                     │                          │
│                              Top-K snippets                    │
│                                     │                          │
│                              memory_get (lectura completa)     │
│                                     │                          │
│                              ► Agente responde con contexto    │
└────────────────────────────────────────────────────────────────┘
```

---

*Siguiente: [Capítulo 6 — Multi-Agent Routing](06-multi-agent-routing.md)*
