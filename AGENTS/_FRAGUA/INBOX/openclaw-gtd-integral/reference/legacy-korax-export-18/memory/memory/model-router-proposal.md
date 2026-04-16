# Model Router — Propuesta de Enrutamiento por Taxonomía de Tareas

*Generado: 2026-02-24*

---

## 1. Inventario de Modelos Disponibles

| Modelo | Alias | Provider | Costo* | Contexto | Output Max | Razón Principal |
|---|---|---|---|---|---|---|
| Claude Opus 4.6 | `opus` | Anthropic | $15/$75 | 200K | 128K | Razonamiento profundo, expert reasoning |
| Claude Sonnet 4.6 | `sonnet` | Anthropic | $3/$15 | 200K | 64K | Default generalista, coding eficiente |
| Claude Haiku 4.5 | `haiku` | Anthropic | $0.25/$1.25 | 200K | 8K | Heartbeats, tareas rápidas |
| GPT-5.3 Codex | `codex-5.3` | OpenAI Codex | ~$5/$15 | 128K | 16K | Terminal coding, agentic development |
| GPT-5.2 Codex | `codex-5.2` | OpenAI Codex | ~$3/$10 | 128K | 16K | Coding general, debugging |
| GPT-5.2 | `gpt-5.2` | OpenAI Codex | ~$2/$8 | 128K | 16K | Fallback coding, quick tasks |
| Kimi K2.5 | `kimi` | Kilo (free) | **$0** | 262K | 65K | Long context, vision, Agent Swarm |
| GLM-5 | `glm5` | Kilo (free) | **$0** | 200K | 128K | Coding + reasoning, agentic tasks |
| MiniMax M2.5 | `minimax-kilo` | Kilo (free) | **$0** | 200K | 32K | General budget, BrowseComp leader |
| Qwen Coder | `qwen-coder` | Qwen Portal | OAuth | 1M | 16K | Ultra-long codebase context |
| Qwen Vision | `qwen-vision` | Qwen Portal | OAuth | 1M | 16K | Image understanding, UI screenshots |
| Gemini 3 Flash | `gemini-flash` | Google | $0.15/$0.60 | 1M | 65K | Budget multimodal, fast |

*\*Costo: Input/Output por 1M tokens*

---

## 2. Benchmarks Clave

| Modelo | SWE-bench | GPQA Diamond | Terminal-Bench | BrowseComp | Math | Context Long |
|---|---|---|---|---|---|---|
| **Opus 4.6** | 80.8% | **91.3%** | 65.4% | — | — | 76% MRCR |
| **Sonnet 4.6** | 79.6% | 74.1% | — | — | 89% | — |
| **GPT-5.3 Codex** | — | — | **77.3%** | — | — | — |
| **Kimi K2.5** | 76.8% | — | 50.8% | 78.4%* | — | 262K |
| **GLM-5** | 77.8% | 86.0% | 56.2% | — | 92.7% | 200K |
| **MiniMax M2.5** | 80.2% | — | — | 76.3% | — | 200K |

*\*con Agent Swarm*

---

## 3. Taxonomía de Tareas

### Tier 1: Razonamiento Profundo (Reasoning-Heavy)
- Planificación arquitectural
- Evaluación de calidad
- Análisis estratégico
- Síntesis multi-documento
- Auditoría de seguridad
- Razonamiento experto (ciencia, legal, médico)

### Tier 2: Coding & Development
- Implementación de features
- Debugging
- Refactoring
- Code review
- Generación de tests
- Terminal operations

### Tier 3: Agentes & Automatización
- Multi-step tasks
- Tool orchestration
- Web research
- Parallel execution
- Long-horizon planning

### Tier 4: Procesamiento de Contenido
- Análisis de imágenes
- OCR / Document extraction
- Translation
- Summarization
- Data extraction

### Tier 5: Tareas Ligeras
- Quick Q&A
- Simple formatting
- Short responses
- Heartbeats
- Notifications

---

## 4. Matriz de Enrutamiento Propuesta

### Por Tipo de Tarea

| Tarea | Primario | Fallback | Rationale |
|---|---|---|---|
| **Planificación arquitectural** | `opus` | `glm5` | Opus: 91.3% GPQA, reasoning depth. GLM-5: free alternative |
| **Evaluación de calidad** | `opus` | `sonnet` | Opus para evaluación profunda, Sonnet para quick reviews |
| **Análisis estratégico** | `opus` | `kimi` | Opus para síntesis, Kimi para long context |
| **Auditoría seguridad** | `opus` | `sonnet` | Opus encontró 500+ vulns en testing |
| **Razonamiento experto (legal/médico)** | `opus` | `glm5` | Opus GPQA 91.3%, GLM-5 86.0% (free) |
| **Implementación features** | `codex-5.3` | `sonnet` | Codex: 77.3% Terminal-Bench, Sonnet: 79.6% SWE-bench |
| **Debugging** | `codex-5.3` | `glm5` | Codex para terminal debugging, GLM-5 free alternative |
| **Refactoring (<10K líneas)** | `sonnet` | `glm5` | Sonnet cost-effective para refactoring estándar |
| **Refactoring (>10K líneas)** | `opus` | `qwen-coder` | Opus para architectural reasoning, Qwen para 1M context |
| **Code review** | `sonnet` | `haiku` | Sonnet balance calidad/costo, Haiku para quick scans |
| **Generación tests** | `codex-5.2` | `sonnet` | Codex especializado en código |
| **Terminal operations** | `codex-5.3` | `glm5` | Codex lidera Terminal-Bench 77.3% |
| **Multi-step agents** | `kimi` | `glm5` | Kimi: Agent Swarm + 262K context. GLM-5: agentic tasks |
| **Web research** | `kimi` | `minimax-kilo` | Kimi: BrowseComp 78.4%, MiniMax: 76.3% (free) |
| **Parallel execution** | `kimi` | — | Agent Swarm feature único |
| **Long-horizon planning** | `glm5` | `kimi` | GLM-5 diseñado para agentic engineering |
| **Análisis imágenes** | `qwen-vision` | `gemini-flash` | Qwen: 1M context vision, Gemini: budget multimodal |
| **OCR / Document extraction** | `kimi` | `qwen-vision` | Kimi: OCRBench 92.3%, strong vision |
| **Translation** | `glm5` | `sonnet` | GLM-5 strong translation, Sonnet general |
| **Summarization** | `haiku` | `glm5` | Haiku: fast/cheap, GLM-5: free |
| **Quick Q&A** | `haiku` | `glm5` | Haiku: $0.25/M, fastest |
| **Heartbeats** | `haiku` | — | Configurado por defecto |
| **Notifications** | `haiku` | — | Minimum viable |

### Por Características del Request

| Característica | Modelo | Rationale |
|---|---|---|
| **Contexto >100K tokens** | `kimi` / `qwen-coder` | 262K / 1M context windows |
| **Output esperado >16K tokens** | `kimi` / `opus` | 65K / 128K output max |
| **Budget crítico** | `glm5` / `kimi` / `minimax-kilo` | Free via Kilo |
| **Speed prioritario** | `haiku` / `gemini-flash` | Lowest latency |
| **Vision required** | `kimi` / `qwen-vision` / `gemini-flash` | Multimodal |
| **Reasoning tokens needed** | `opus` / `glm5` | Extended thinking / reasoning mode |
| **Terminal/CLI context** | `codex-5.3` | Terminal-Bench leader |

---

## 5. Estrategia de Fallbacks Propuesta

### Default Chain (Actual)
```
sonnet → gpt-5.2 → kimi → glm5
```

### Por Perfil de Uso

#### Perfil: Development Work
```yaml
primary: codex-5.3
fallbacks: [sonnet, glm5, kimi]
```

#### Perfil: Research/Analysis
```yaml
primary: opus
fallbacks: [glm5, kimi]
```

#### Perfil: Budget-Conscious
```yaml
primary: glm5
fallbacks: [kimi, minimax-kilo]
```

#### Perfil: Long Context
```yaml
primary: kimi
fallbacks: [qwen-coder, glm5]
```

#### Perfil: Quick Tasks
```yaml
primary: haiku
fallbacks: [glm5]
```

---

## 6. Implementación Recomendada

### Config por Perfil

```json5
// openclaw.json - Perfil Development
{
  agents: {
    defaults: {
      model: {
        primary: "openai-codex/gpt-5.3-codex",
        fallbacks: [
          "anthropic/claude-sonnet-4-6",
          "kilocode/z-ai/glm-5:free",
          "kilocode/moonshotai/kimi-k2.5"
        ]
      }
    }
  }
}
```

### Router Dinámico (Skill)

```yaml
# skills/model-router/SKILL.md
name: model-router
description: "Enrutamiento inteligente de modelos por tipo de tarea"

rules:
  - condition: "task.type == 'architectural_planning' or task.type == 'quality_evaluation'"
    model: opus
    
  - condition: "task.type == 'coding' and task.context == 'terminal'"
    model: codex-5.3
    
  - condition: "task.type == 'web_research' or task.type == 'parallel_execution'"
    model: kimi
    
  - condition: "task.type == 'debugging'"
    model: codex-5.3
    
  - condition: "task.input_tokens > 100000"
    model: kimi
    
  - condition: "task.budget == 'critical'"
    model: glm5
    
  - condition: "task.type == 'heartbeat'"
    model: haiku
```

---

## 7. Costo-Efectividad por Tarea

### Análisis de Costo por 1000 Requests (promedio 10K tokens/request)

| Modelo | Costo/1000 req | Mejor Para |
|---|---|---|
| **Haiku 4.5** | ~$10 | Heartbeats, quick tasks |
| **GLM-5 (free)** | **$0** | Coding, reasoning, agents |
| **Kimi (free)** | **$0** | Long context, vision, research |
| **MiniMax (free)** | **$0** | General, web research |
| **Sonnet 4.6** | ~$126 | Default development |
| **GPT-5.3 Codex** | ~$100 | Terminal coding |
| **Opus 4.6** | ~$630 | Deep reasoning only |

### Ahorro Potencial con Router

| Estrategia | Costo Mensal (30K req) | vs All-Opus |
|---|---|---|
| All Opus | $18,900 | Baseline |
| All Sonnet | $3,780 | -80% |
| Router (90% free / 10% Opus) | ~$2,000 | **-89%** |

---

## 8. Recomendaciones Finales

### Para Korax (Korvo Personal Assistant)

**Perfil híbrido recomendado:**

```yaml
primary: sonnet          # Balance calidad/costo
fallbacks: [gpt-5.2, kimi, glm5]

task_overrides:
  heartbeat: haiku
  planning: opus
  security_audit: opus
  web_research: kimi
  debugging: codex-5.3
  vision: kimi
  budget_critical: glm5
```

### Para Gateway Jurídico (Dedicado)

```yaml
primary: glm5            # Free + strong reasoning (86% GPQA)
fallbacks: [kimi, minimax-kilo]

# GLM-5 ideal para:
# - Análisis legal (reasoning)
# - Redacción documentos (agentic tasks)
# - Long context (200K)
# - Budget crítico (free)
```

### Para Development (Claude Code)

```yaml
primary: codex-5.3       # Terminal-Bench leader
fallbacks: [sonnet, glm5]

# Codex para coding, GLM-5 como free fallback
```

---

## 9. Pendientes

- [ ] Implementar skill `model-router` con reglas de enrutamiento
- [ ] Configurar perfiles en `openclaw.json`
- [ ] Testear fallback chain con cada perfil
- [ ] Monitorear costo-efectividad post-implementación
- [ ] Revisar periódicamente (models landscape cambia rápido)
