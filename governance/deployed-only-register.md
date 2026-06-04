---
_manifest:
  urn: "urn:kora:kb:deployed-only-register-v1"
  provenance:
    created_by: "FS"
    created_at: "2026-05-07"
    source: "Auditoria post-poda version A. Registra los 9 artefactos desplegados fuera del gobierno KORA (8 agents claude-code + 1 bot OpenClaw) y establece su situacion juridica bajo postura 2 (gobierno selectivo)."
  version: "1.0.0"
  status: publicado
  family: note
  tags: [governance, deployed-only, inventario, postura-2, poda-version-a]
relations:
  cites:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:host-roles"
---

# Registro de artefactos deployed-only

Doctrina: postura 2 (gobierno selectivo). KORA gobierna lo portable
multi-target; lo nativo o single-target se registra aqui sin exigir el
canon completo. Ambiguedad es peor que cualquier decision.

Creado: 2026-05-07. Revisar trimestralmente o cuando una entrada cambie
de estado.

Actualizacion 2026-06-04: este registro conserva el corte historico del
2026-05-07. Para estado vivo usar `python3 toolchain/kora recovery-inventory`
y los handoffs recientes. Quedaron regularizados con fuente `AGENT.md`
productiva y despliegue a Claude Code, Codex, OpenCode y OpenClaw:
`agent-architect`, `forjador-openclaw`, `fugaz`, `ifml-architect`,
`opm-specialist`, `polymath`, `ux-research-design-ai`,
`jobs-healthcare-ux` y `steve-jobs-agentic-designer`.

En el mismo ciclo se decidio que `hospitalista` y `mente-omega` no deben
tener workspace OpenClaw agentico propio: siguen como skills KORA y sus
workspaces OpenClaw activos fueron retirados a
`/home/felix/openclaw-fleet/_retired-agent-workspaces/2026-06-04-skill-only/`.

## Agentes Claude Code (8)

### Registro

| # | Nombre | Situacion | Accion |
|---|--------|-----------|--------|
| 1 | `agent-architect` | off-spec autorizado | Skill futura: diseno de subagentes Claude Code. Valor probado, sin equivalente KORA. |
| 2 | `forjador-openclaw` | off-spec autorizado | Agente operacional: gestiona flota OpenClaw en vivo (systemd, docker, configs). No portable a skill. |
| 3 | `ifml-architect` | redundante | Cubierto por `urn:kora:artefacto:ifml` (v1.0.0, activa). Recomendacion: retirar el agente nativo, usar la skill KORA. |
| 4 | `jobs-healthcare-ux` | off-spec autorizado | Skill futura: UX clinico con 18 principios constitucionales. Dominio unico, sin equivalente KORA. |
| 5 | `opm-specialist` | redundante | Cubierto por `urn:kora:artefacto:modelamiento-opm` (v1.0.0, activa). Recomendacion: retirar el agente nativo, usar la skill KORA. |
| 6 | `polymath` | off-spec autorizado | Skill futura: pensamiento estructural general (complementa cat-thinking). Sin equivalente KORA completo. |
| 7 | `steve-jobs-agentic-designer` | off-spec autorizado | Skill futura: diseno de subagentes Claude Code con 7 principios + 10 anti-patrones. Sin equivalente KORA. |
| 8 | `ux-research-design-ai` | en transicion | Skill en REVIEW: `artifacts/skills/_TALLER/REVIEW/ux-design/SKILL.md` (borrador). Promover y desplegar. |

### Detalle por agente

#### 1. agent-architect

- **Archivo**: `~/.claude/agents/agent-architect.md`
- **Proposito**: Disenar, construir, auditar y refactorizar subagentes Claude Code
- **Herramientas**: Read, Edit, Write, Glob, Grep, Bash
- **Clasificacion**: Skill (conocimiento transferible: spec de subagentes, 9-step protocol, patrones)
- **Estado**: off-spec autorizado. El operador lo usa dia a dia.
- **Plan**: Crear skill `kora/agent-architect` cuando haya ciclo de construccion disponible.

#### 2. forjador-openclaw

- **Archivo**: `~/.claude/agents/forjador-openclaw.md`
- **Proposito**: Ingeniero de ecosistema OpenClaw: deploy, configuracion, troubleshooting, upgrades, federation
- **Herramientas**: Read, Edit, Write, Glob, Grep, Bash
- **Clasificacion**: Agente (gestiona infraestructura viva; no portable a skill)
- **Estado**: off-spec autorizado. Opera sobre 3 generaciones de infraestructura (korvo, Docker, systemd).
- **Conocimiento legacy**: `urn:agengai:kb:forjador-openclaw` en `artifacts/knowledge/agengai/openclaw/specs-legacy/`
- **Plan**: Mantener como agente nativo. Si OpenClaw se convierte en target KORA productivo, considerar ingestion formal.

#### 3. ifml-architect (REDUNDANTE)

- **Archivo**: `~/.claude/agents/ifml-architect.md`
- **Proposito**: Modelado IFML/OMG: auditoria, diseno, optimizacion, revision de consistencia
- **Equivalente KORA**: `urn:kora:artefacto:ifml` (`artifacts/skills/kora/ifml/SKILL.md`, v1.0.0, activa)
- **Estado**: redundante. La skill KORA cubre el mismo dominio con corpus de 9 URNs, canario pasa-estricto y despliegue a 3 targets.
- **Recomendacion**: Retirar `~/.claude/agents/ifml-architect.md`. Usar la skill `ifml` cargada en sesion.

#### 4. jobs-healthcare-ux

- **Archivo**: `~/.claude/agents/jobs-healthcare-ux.md`
- **Proposito**: Diseno UX clinico con 18 principios constitucionales. Contexto: hospitales publicos latinoamericanos.
- **Herramientas**: Read, Grep, Glob, Write, Edit, WebFetch, WebSearch
- **Clasificacion**: Skill (capital intelectual: 18 principios, 9 anti-patrones clinicos, 5 modos de operacion)
- **Estado**: off-spec autorizado. Dominio unico sin equivalente KORA.
- **Plan**: Crear skill `salud/jobs-healthcare-ux` con corpus de principios y anti-patrones.

#### 5. opm-specialist (REDUNDANTE)

- **Archivo**: `~/.claude/agents/opm-specialist.md`
- **Proposito**: Modelado OPM/ISO 19450: explicacion, guia, evaluacion, ejemplos
- **Equivalente KORA**: `urn:kora:artefacto:modelamiento-opm` (`artifacts/skills/kora/modelamiento-opm/SKILL.md`, v1.0.0, activa)
- **Estado**: redundante. La skill KORA cubre el mismo dominio con corpus SSOT en `fxsl/opm/opm-ssot-es/`.
- **Recomendacion**: Retirar `~/.claude/agents/opm-specialist.md`. Usar la skill `modelamiento-opm` cargada en sesion.

#### 6. polymath

- **Archivo**: `~/.claude/agents/polymath.md`
- **Proposito**: Pensador estructural general: analisis, evaluacion, diagnostico, documentos estructurados, exploracion conceptual, revision critica
- **Herramientas**: Read, Grep, Glob, Bash, Write, Edit, WebFetch, WebSearch
- **Clasificacion**: Skill (capital intelectual: FUNCION OBJETIVO, 5 axiomas, triple loop cognitivo, 6 fases, 5 niveles de certidumbre, 9 heuristicas)
- **Estado**: off-spec autorizado. Complementa `cat-thinking` (teoria de categorias) con pensamiento estructural general.
- **Conocimiento relacionado**: `artifacts/knowledge/_SCRIPTORIUM/REVIEW/kora/perfiles/polymath-sigma-cognitive-spec-v3.md`
- **Plan**: Crear skill `kora/polymath` con la spec cognitiva como corpus de conocimiento.

#### 7. steve-jobs-agentic-designer

- **Archivo**: `~/.claude/agents/steve-jobs-agentic-designer.md`
- **Proposito**: Diseno de sistemas agenticos: revision, diseno multi-agente, interaccion humano-agente. 7 principios, 7 preguntas letales, 10 anti-patrones.
- **Herramientas**: Read, Edit, Write, Glob, Grep, Bash
- **Clasificacion**: Skill (capital intelectual: principios de diseno, anti-patrones, metodo de auditoria). Produce archivos .md de agente como output.
- **Estado**: off-spec autorizado. Sin equivalente KORA.
- **Plan**: Crear skill en `dev/` o `kora/` con los 7 principios + 10 anti-patrones como corpus.

#### 8. ux-research-design-ai

- **Archivo**: `~/.claude/agents/ux-research-design-ai.md`
- **Proposito**: Investigacion y diseno UX: 8 modos de auditoria, heuristicas Nielsen, WCAG 2.2 AA, arquitectura de informacion
- **Equivalente KORA**: `artifacts/skills/_TALLER/REVIEW/ux-design/SKILL.md` (borrador, mismo dominio)
- **Estado**: en transicion. Skill KORA promovida: `urn:kora:artefacto:ux-design` (`artifacts/skills/kora/ux-design/SKILL.md`, v1.0.0, activa). Desplegada a claude-code + codex.
- **Recomendacion**: Promover `ux-design` de REVIEW a productivo, transmutar, desplegar, y retirar el agente nativo.

## Bot OpenClaw (1)

### gtd-integral (David)

- **Workspace**: `~/openclaw-fleet/workspaces/gtd-integral/`
- **Proposito**: Agente operacional GTD Integral sobre gateway Clawforge. Loop de 7 movimientos, 3 capas axiomaticas, 6 standing orders, co-agencia.
- **Clasificacion**: Agente (opera en vivo sobre OpenClaw, gestiona superficies operacionales, comunicacion cross-agente)
- **Skill metodologica**: `urn:pro:artefacto:gtd-flow` (`artifacts/skills/pro/gtd-flow/SKILL.md`, v1.0.0, activa). Desplegada a claude-code + codex.
- **Estado**: off-spec autorizado. Agente operacional con skill metodologica en INBOX.
- **Plan**: Promover `gtd-flow` de INBOX a productivo. David es el runtime; gtd-flow es la metodologia reusable.

## Resumen de situacion

| Categoria | Cantidad | Items |
|-----------|----------|-------|
| Redundante (cubierto por skill KORA) | 2 | ifml-architect, opm-specialist |
| Regularizado (skill KORA promovida) | 2 | ux-research-design-ai → `kora/ux-design`, gtd-integral → `pro/gtd-flow` |
| Off-spec autorizado — skill futura | 4 | agent-architect, jobs-healthcare-ux, polymath, steve-jobs-agentic-designer |
| Off-spec autorizado — agente operacional | 1 | forjador-openclaw |

## Acciones completadas (2026-05-07)

1. ✅ `ux-design` promovido de `_TALLER/REVIEW/` → `artifacts/skills/kora/ux-design/`
2. ✅ `ux-design` transmutado y desplegado a claude-code + codex
3. ✅ `gtd-flow` promovido de `_TALLER/INBOX/` → `artifacts/skills/pro/gtd-flow/`
4. ✅ `gtd-flow` transmutado y desplegado a claude-code + codex

## Acciones diferidas (proximo ciclo)

1. Retirar `ifml-architect.md` y `opm-specialist.md` de `~/.claude/agents/`
2. Construir skills para agent-architect, jobs-healthcare-ux, polymath, steve-jobs-agentic-designer
3. Evaluar ingestion formal de forjador-openclaw como agente KORA
