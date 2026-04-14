---
title: Anthropic Skills Format Reference
status: internal
lang: es
---

# Anthropic Skills Format Reference

Referencia operativa para el mapeo KORA → Anthropic Skill (Claude Code). Fuente: KNOWLEDGE/agengai/skills-anthropic.md.

## Estructura de un Skill

```
nombre-skill/
├── SKILL.md        # Requerido: frontmatter YAML + instrucciones
├── scripts/        # Opcional: codigo ejecutable
├── references/     # Opcional: documentacion consultable
└── assets/         # Opcional: plantillas, ejemplos
```

## Frontmatter

### Campos obligatorios

| Campo | Restricciones |
|-------|---------------|
| description | Max 1024 chars. Sin `<>`. DEBE incluir QUE hace + CUANDO usarla |

### Campos opcionales

| Campo | Uso |
|-------|-----|
| name | kebab-case. Sin "claude" ni "anthropic" (reservados). Debe coincidir con nombre de carpeta |
| license | MIT, Apache-2.0, etc. |
| compatibility | 1-500 chars. Requisitos de ambiente (Python, bash, network, etc.) |
| allowed-tools | Restriccion de tools: `Bash(python:*) Bash(npm:*) WebFetch` |
| metadata | Objeto key-value libre: author, version, mcp-server, category, tags |

### Restricciones de seguridad

- Frontmatter aparece en system prompt de Claude. Contenido malicioso podria inyectar instrucciones.
- Prohibido: caracteres XML `<>` en frontmatter
- Prohibido: "claude" o "anthropic" en name
- YAML safe parsing (no code execution en YAML)

## Progressive Disclosure (3 niveles)

| Nivel | Carga | Contenido | Token impact |
|-------|-------|-----------|-------------|
| 1. Frontmatter | Siempre en system prompt | name + description | Base 195 chars + 97 chars/skill + len(campos) |
| 2. SKILL.md body | Cuando Claude detecta relevancia | Instrucciones completas | Variable, idealmente ≤5000 palabras |
| 3. Linked files | On-demand cuando se necesita | scripts/, references/, assets/ | Solo cuando modelo los lee |

### Formula token impact (caracteres)

```
total = 195 + Σ (97 + len(name_escaped) + len(description_escaped) + len(location_escaped))
```

XML escaping expande `& < > " '` en entities. Estimacion ~4 chars/token.

### Gestion de tamano

- SKILL.md idealmente ≤5,000 palabras
- Si contenido excede: mover documentacion detallada a `references/`
- Referenciar con: "Consulta `references/api-patterns.md` para..."
- Mas de 20-50 skills simultaneos puede degradar performance

## Composabilidad

- Claude puede cargar multiples skills simultaneamente
- Cada skill DEBE funcionar junto a otros sin asumir exclusividad
- Skills son portables: funcionan en Claude.ai, Claude Code y API sin modificacion

## Description: Campo critico

### Estructura recomendada

```
[Que hace] + [Cuando usarla] + [Capacidades clave]
```

### Ejemplos correctos

```yaml
# Especifico y accionable
description: Analyzes Figma design files and generates developer handoff documentation. Use when user uploads .fig files, asks for "design specs", "component documentation", or "design-to-code handoff".

# Con trigger phrases
description: Manages Linear project workflows including sprint planning, task creation, and status tracking. Use when user mentions "sprint", "Linear tasks", "project planning", or asks to "create tickets".
```

### Ejemplos incorrectos

```yaml
# Demasiado vago
description: Helps with projects.

# Sin triggers
description: Creates sophisticated multi-page documentation systems.

# Demasiado tecnico, sin user triggers
description: Implements the Project entity model with hierarchical relationships.
```

### Debugging de triggers

Preguntar a Claude: "When would you use the [skill name] skill?" — Claude citara la description. Ajustar segun lo que falta.

## Troubleshooting

### Skill no se activa (undertriggering)

- Senales: skill nunca carga automaticamente, usuarios lo habilitan manualmente
- Causa: description demasiado generica o sin trigger phrases
- Fix: agregar keywords especificos y frases que usuarios dicen realmente
- Incluir tipos de archivo si aplica

### Skill se activa demasiado (overtriggering)

- Senales: skill carga para queries irrelevantes, usuarios lo deshabilitan
- Fix 1: agregar negative triggers ("Do NOT use for simple data exploration")
- Fix 2: ser mas especifico ("Processes PDF legal documents" en vez de "Processes documents")
- Fix 3: clarificar scope ("for online payment workflows, not for general financial queries")

### Instrucciones no seguidas

- Instrucciones demasiado verbose → usar bullet points, listas numeradas
- Instrucciones enterradas → poner criticas al inicio con headers `## Important`
- Lenguaje ambiguo → "CRITICAL: Before calling X, verify: [lista especifica]"
- Code > language: para validaciones criticas, usar script en vez de instrucciones textuales

### Problemas de contexto grande

- Skill content demasiado grande → mover a references/
- Muchos skills simultaneos → evaluar si >20-50 activos
- Todo cargado en vez de progressive disclosure → link en vez de inline

### Error de upload

- "Could not find SKILL.md": archivo no nombrado exactamente SKILL.md (case-sensitive)
- "Invalid frontmatter": YAML mal formateado, quotes sin cerrar, delimitadores `---` faltantes
- "Invalid skill name": nombre con espacios o mayusculas

## 5 Patrones de Skills

### Pattern 1: Sequential Workflow Orchestration

Para procesos multi-paso en orden especifico. Pasos explicitos, dependencias entre pasos, validacion en cada etapa, instrucciones de rollback.

### Pattern 2: Multi-MCP Coordination

Para workflows que cruzan multiples servicios. Fases claras, data passing entre MCPs, validacion antes de avanzar, error handling centralizado.

### Pattern 3: Iterative Refinement

Para output que mejora con iteracion. Draft inicial, quality check con script, loop de refinamiento, criterio de parada.

### Pattern 4: Context-Aware Tool Selection

Para misma outcome con diferentes tools segun contexto. Decision tree explicito, fallback options, transparencia sobre elecciones.

### Pattern 5: Domain-Specific Intelligence

Para conocimiento especializado mas alla de tool access. Compliance checks antes de accion, audit trail, documentacion comprehensiva.

## Skills via API

- `/v1/skills` endpoint para listar y gestionar skills
- `container.skills` parameter en Messages API
- Version control via Claude Console
- Compatible con Claude Agent SDK
- Requiere Code Execution Tool beta

## Mapeo KORA → Anthropic Skill

| Componente KORA | Seccion Anthropic | Notas |
|----------------|-------------------|-------|
| AGENTS.md | `<kora_bootstrap component="agents">` | FSM completa como texto |
| SOUL.md | `<kora_bootstrap component="soul">` | Identidad + tono |
| USER.md | NO se incluye | Contexto operador es del runtime |
| TOOLS.md | `<kora_bootstrap component="tools">` | Firmas + routing |
| config.json | NO se incluye | Config es server-side |
| skills/ | Tabla de referencia + lazy-load | NO inlinear, referenciar paths |

### Exclusiones justificadas

- **USER.md**: El operador de Claude Code tiene su propio perfil. USER.md del agente KORA no aplica.
- **config.json**: Las restricciones de seguridad, sandbox, tools allow/deny son del runtime de Claude Code. No se inyectan como texto al LLM (runtime-spec-md §3.2).

### Reglas de compilacion

1. Eliminar todo frontmatter KORA (_manifest, version, status, etc.)
2. Envolver FSM + reglas en `<kora_bootstrap component="agents">`
3. Envolver identidad en `<kora_bootstrap component="soul">`
4. Envolver herramientas en `<kora_bootstrap component="tools">`
5. Skills como tabla de lazy-load con instruccion de leer on-demand
6. Saludo + estado inicial S-DISPATCHER al final
7. Description del frontmatter derivada de SOUL.md identidad + triggers de activacion
