---
_manifest:
  urn: "urn:kora:kb:start-prompt"
  provenance:
    created_by: "FS"
    created_at: "2026-04-28"
    source: "Prompt de inicio generico para agentes (humanos o LLM) que abren una sesion sobre el repo KORA. Citado por handoffs y memoria persistente como punto de entrada."
version: "1.0.0"
status: publicado
tags: [start-prompt, bootstrap, kora, sesion, agentes, onboarding]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:harness-spec"
    - "urn:kora:kb:autoria-spec"
    - "urn:kora:kb:md-spec"
    - "urn:kora:kb:knowledge-spec"
    - "urn:kora:kb:transmutation-spec"
    - "urn:kora:kb:agent-skill-construction-spec"
---

# Start prompt — inicio generico de sesion KORA

Prompt copiable para arrancar trabajo sobre este repo. Aplica a sesiones
nuevas de Claude Code, Codex, OpenCode u otro agente que opere sobre
KORA.

## Prompt minimo

```
Sesion KORA — bootstrap.

Lee primero, en este orden:

1. AGENTS.md / CLAUDE.md (top-level): doctrina operativa del repo,
   topologia post-reorg v5, comandos vivos.
2. governance/gobernanza.md: precedencia, regimenes URN, lifecycle,
   capas (ontologia / serializacion / runtime / distribucion).
3. El ultimo handoff en docs/reports/handoff-YYYY-MM-DD-*.md por fecha
   descendente. Es el snapshot vivo del repo.
4. ~/.claude/projects/-home-felix-kora/memory/MEMORY.md: index de
   memorias persistentes; leer las mas recientes que apliquen.

Antes de proponer o tocar nada, verifica estado:

  python3 toolchain/kora index
  python3 toolchain/kora check --strict

Si strict no pasa, diagnostica antes de avanzar; no normalices la deuda.

Cuando vayas a producir artefactos:

- Habilidades nuevas: usa la skill urn:kora:artefacto:kora-skills.
- Subagentes / agentes-pt / agentes-plataforma: urn:kora:artefacto:kora-agents.
- Conocimiento descriptivo (notas, guias, atomic): urn:kora:artefacto:artifact-curator.
- Pensamiento estructural-discursivo: urn:kora:artefacto:mente-omega.
- Lectura categorial: urn:kora:artefacto:cat-thinking.

Reglas duras del repo (sin excepciones):

- IR primero: AGENT.md / SKILL.md conformes a autoria-spec antes de
  cualquier transmutacion.
- URNs sin version embebida; version en frontmatter.
- Conocimiento por URN resoluble, jamas por path duro en componible_con
  ni conocimiento_permitido.
- Nada se publica sin pasar por staging (REVIEW) salvo retiros.
- Democion sobre el mismo URN prohibida (autoria-spec §8.2): retira y
  emite uno nuevo con supersedes.
```

## Capas vigentes (resumen)

| Capa | Path | Specs canonicas |
|------|------|------------------|
| Constitucion | `governance/` | `gobernanza.md` |
| Ontologia | `ontology/` | `harness-spec.md`, `qa-spec.md`, `procesos-spec.md`, `risk-register-spec.md` |
| Serializacion | `serialization/` | `autoria-spec.md`, `agent-skill-construction-spec.md`, `md-spec.md`, `knowledge-spec.md` |
| Runtime | `runtime/` | `runtime-spec-md.md`, `transmutation-spec.md`, `multiagente-spec.md`, runtime-extensions (claude-code, codex, gemini, mastra, opencode, openclaw, agentskills) |
| Productivo | `artifacts/{agents,knowledge,skills}/` | shape unificado autoria-spec |
| Toolchain | `toolchain/kora`, `toolchain/kora_lib/` | CLI viva |

## Skills core que cualquier agente puede invocar

| URN | Cuando |
|-----|--------|
| `urn:kora:artefacto:artifact-curator` | ciclo de vida general de artefactos KORA |
| `urn:kora:artefacto:kora-skills` | construir / auditar / evolucionar habilidades |
| `urn:kora:artefacto:kora-agents` | construir / auditar / evolucionar agentes |
| `urn:kora:artefacto:mente-omega` | razonamiento estructural-discursivo (pentamotor Φ Ψ Ξ Δ Σ) |
| `urn:kora:artefacto:cat-thinking` | enmarque categorial (24 piezas ICAS-BoK) |
| `urn:kora:artefacto:atomize` | familia atomic productor canonico |
| `urn:kora:artefacto:knowledge-curator` | KB normal descriptivo en REVIEW |
| `urn:kora:artefacto:curation-conductor` | flujo knowledge end-to-end |

## Personas disponibles (agentes-pt persona)

| URN | Para |
|-----|------|
| `urn:dev:artefacto:steipete` | direccion de ejecucion cognitiva (Peter Steinberger clon) |
| `urn:fxsl:artefacto:allan-kelly` | arquitectura organizacional human-agent |
| `urn:pro:artefacto:david-allen` | claridad operable integral (GTD + regulacion) |

## Targets de transmutacion

```bash
python3 toolchain/kora transmute --target {agentskills|claude-code|codex|gemini|mastra|opencode|openclaw} --agent {ns}/{name} --dry-run
```

## Antipatrones que cortan rapido

- Asumir topologia legacy (`KNOWLEDGE/`, `AGENTS/`, `SKILLS/`, `specs/`,
  `scripts/`): hoy es `artifacts/`, capas top-level y `toolchain/`.
- Editar `docs/generated/*` a mano: es derivado, regenerable con
  `kora index` / `kora sync-docs`.
- Promover knowledge sin pasar por REVIEW.
- Inventar URNs: resolver con `kora resolve <urn>` antes de citar.
- Saltar a runtime sin AGENT.md / SKILL.md fuente conforme a autoria-spec.

## Donde leer mas

- Topologia detallada y comandos: `AGENTS.md` y `CLAUDE.md`.
- Estado vivo: `docs/reports/handoff-*.md` (por fecha descendente).
- Roadmaps: `docs/plans/*.md`.
- Memoria persistente: `~/.claude/projects/-home-felix-kora/memory/MEMORY.md`.
- Specs canonicas: `governance/`, `ontology/`, `serialization/`, `runtime/`.
