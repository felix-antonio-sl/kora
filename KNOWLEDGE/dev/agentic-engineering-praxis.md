---
_manifest:
  urn: "urn:dev:kb:agentic-engineering-praxis"
  type: "knowledge_article"
  version: "1.0.0"
title: "Ingenieria Agéntica: Praxis de Peter Steinberger"
domain: "dev"
tags: [agentic-engineering, methodology, workflow, steipete]
sources:
  - "steipete.me/posts/just-talk-to-it"
  - "steipete.me/posts/2025/optimal-ai-development-workflow"
  - "steipete.me/posts/2025/shipping-at-inference-speed"
  - "Lex Fridman Podcast #491"
  - "The Pragmatic Engineer - I ship code I don't read"
  - "Hanselminutes #1036 - The Rise of The Claw"
  - "Pragma Conf 2025 / Swift Connection 2025 - You Can Just Do Things"
---

# Ingenieria Agéntica: Praxis de Peter Steinberger

## 1. Filosofia Core

### Agentic Engineering vs Vibe Coding

Disciplina estricta. "Vibe coding" es un slur. Agentic engineering requiere planning estratégico, comprensión de capacidades del agente, diseño de sistemas autovalidables. La diferencia entre un junior que "vibes" y un senior que orquesta es la misma que entre alguien que tira comandos random y un sysadmin que diseña pipelines.

### Architecture Over Implementation

Senior skills (diseño de sistema, gestión de dependencias, "gusto" arquitectónico) son irreemplazables. AI maneja transformaciones rutinarias; humanos diseñan. El valor está en saber qué construir y cómo encajan las piezas, no en escribir el código.

### Fun-Driven Development

El éxito de OpenClaw atribuido a "disfrutar genuinamente el proceso creativo". Si no es divertido, algo está mal. La productividad sostenible viene del disfrute, no de la disciplina forzada.

### "You Can Just Do Things"

Rechazar sobreplanificación. Construir lo que siempre quisiste. El lenguaje natural es el meta-lenguaje definitivo. No pedir permiso — construir, iterar, mostrar resultados.

## 2. Los 7 Principios Operativos

### P1: Just Talk To It

Instrucciones mínimas en lenguaje natural. "Often it's just 1-2 sentences + an image." No elaborar prompts complejos — el modelo entiende intención. Dictado semántico (Wispr Flow) para input rápido. Screenshots > prosa para cambios visuales.

### P2: Blast Radius Thinking

Evaluar conscientemente: ¿cuántos archivos? ¿cuánto tiempo? ¿reversible? Esto determina cuántos agentes paralelos usar. Un cambio de 1 archivo no necesita planning; un refactor de 50 archivos necesita descomposición cuidadosa.

### P3: Close The Loop

Agentes deben compilar, lintear, testear y validar su propio trabajo. Cuando tests fallan, iteran automáticamente hasta "green loop". Por eso AI excele en código (provable) vs escritura creativa (unprovable). Un obrero que no cierra el loop no ha terminado.

### P4: Parallel Dispatch

3-8 instancias simultáneas. Calibración por tipo de tarea:
- 1-2 para refactoring (alto riesgo de conflicto)
- ~4 para cleanup/testing (independientes)
- 5-10 para feature velocity (múltiples features independientes)

### P5: Context Hygiene

Ventana de contexto es recurso escaso. Eliminar MCPs innecesarios. Preferir CLIs simples. Mantener CLAUDE.md como documento vivo (~800 líneas). No cargar herramientas que no se usarán.

### P6: Architecture Over Implementation

El valor está en diseño, dependencias, "gusto" arquitectónico. Delegar lo "aburrido" (JSON transforms, Tailwind tweaks) al modelo. Reservar cognición humana para decisiones que requieren juicio.

### P7: Fun-Driven Development

Si no es divertido, algo está mal. Creatividad > disciplina rígida. El flow state es productivo; la resistencia es señal de mal diseño.

## 3. Patrones de Workflow

### Topología

Ghostty en grilla 3x3, Codex CLI como driver principal, Claude Code secundario. Terminal multiplexing para visibilidad de todos los obreros simultáneamente.

### Commits atómicos

Cada agente commitea exactamente los archivos que editó. Un commit = un paquete de trabajo = una intención.

### Trabajo en main

Sin PRs para solo-dev (PRs cuestan velocidad). Para equipos: Prompt Requests > Pull Requests. La branching strategy depende del contexto social, no técnico.

### Code review

"Most code I don't read". Foco en arquitectura y relaciones entre componentes, no line-by-line. Watch the stream, look at key parts.

### Tests after implementation

Dentro del mismo contexto, aprovechando memoria a corto plazo del agente. El agente que implementó escribe los tests — tiene el contexto fresco.

### 20% refactoring

jscpd (duplicación), knip (dead code), ESLint React Compiler, deprecation checks. Dedicar ~20% del tiempo a mantener el codebase limpio.

### Dictado semántico

Wispr Flow para input rápido. Hablar es más rápido que escribir para instrucciones complejas.

### Image-based iteration

Screenshots > prose para UI changes. El modelo interpreta la imagen y produce el código correspondiente.

## 4. Selección de Modelo por Tarea (Configuración Operativa)

| Componente | CLI | Modelo | Razón |
|------------|-----|--------|-------|
| Obrero implementación | Claude Code | Opus 4.6 (1M) | Máxima calidad, contexto completo |
| Obrero cleanup/refactor | Claude Code | Opus 4.6 (1M) | Reestructuración profunda |
| Review de código | Codex CLI | GPT-5.4 | Diversidad de blind spots vs implementador |
| Agente orquestador (steipete) | — | Sonnet 4.6 | Orquestación ligera, no razonamiento profundo |
| Obrero review | — | Modelo != coder | Siempre diferente al que implementó |

**CLIs de primera clase (sin preferencia):** Claude Code, Codex CLI, Gemini CLI, OpenCode. La selección del CLI depende del modelo y la tarea, no de lealtad a un vendor. Los tres CLIs propietarios (Claude Code, Codex, Gemini) y el open-source (OpenCode) son herramientas igualmente válidas.

## 5. Anti-Patrones (Explícitamente Rechazados)

- **RAG/Vector Databases**: Innecesarios con GPT-5 search. Overhead > beneficio.
- **Subagent orchestration compleja**: "Workarounds masking model inefficiencies". Cuando los modelos son buenos, la orquestación simple basta.
- **MCPs**: "Constant context cost and garbage" — CLIs preferibles. Cada MCP consume tokens de contexto permanentemente.
- **Elaborate prompt charades**: Lenguaje motivacional excesivo no ayuda. El modelo no necesita que lo motives.
- **Spec-driven development**: Iterar mientras construyes > especificar antes. Las specs se desactualizan antes de implementarse.
- **Hook-based security**: "No hook will stop them if determined". Sandbox real > hooks de pre-commit.
- **Múltiples suscripciones GUI** (Cursor, etc.): CLI-first siempre. GUIs son overhead visual innecesario.

## 6. Heurísticas Operativas

### Cuándo parar/resetear

Si toma más de lo anticipado, Escape + pedir status. No temer parar a mitad — file changes son atómicos, el modelo retoma. La sesión es desechable; los archivos persisten.

### Session management

Topic en statusline con session ID. "Plan mode and iterating is key". Sesiones cortas y enfocadas > sesiones maratónicas.

### CLAUDE.md como scar tissue organizacional

~800 líneas, escrito por el modelo, actualizado ante cada incidente. Cada bug encontrado, cada patrón descubierto, cada convención establecida queda en CLAUDE.md como memoria persistente del proyecto.

### Cuándo NO leer código

"Ship code I don't read" — delegar código aburrido (transforms, UI tweaks), reservar cognición para arquitectura. No leer lo que el modelo puede verificar automáticamente.

### Agnosticismo de lenguaje

Go para CLIs (compilación rápida), TypeScript para web, Swift para native, Zig para performance. El lenguaje natural es el meta-lenguaje. La elección de lenguaje de programación es pragmática, no tribal.

## 7. Contexto Biográfico

- **PSPDFKit**: 13 años, C++/Objective-C, PDF framework usado por Apple, 1B+ devices, 70 empleados, EUR100M investment de Insight Partners (2021)
- **Burnout**: 3 años fuera de tech
- **Retorno (2024-2026)**: Agentic engineering como nueva disciplina
- **OpenClaw**: Proyecto de fin de semana → 180k+ GitHub stars → fundación open-source
- **OpenAI (Feb 2026)**: "Bringing agents to everyone"
- **Peak**: 6,600+ commits en enero 2026 (~600/día, 5-10 agentes paralelos)
- **Costo**: ~$1k/mes (4 OpenAI subs + 1 Anthropic) — 10x más barato que API

## 8. Arquitectura OpenClaw (Referencia)

- **Hub-and-spoke**: Gateway (Node.js 22+, WebSocket 127.0.0.1:18789)
- **Pipeline**: Ingestion → Access Control → Context Assembly → Model Invocation → Tool Execution → Response Delivery
- **Multi-agent routing** por channel/binding
- **Plugin system**: channel, memory, tool, provider
- **System prompt composable**: AGENTS.md + SOUL.md + TOOLS.md + dynamic context
- **Session**: append-only event logs + automatic compaction
- **Memory**: BM25 + vector similarity hybrid
