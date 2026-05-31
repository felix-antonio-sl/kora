---
_manifest:
  urn: "urn:kora:kb:start-prompt"
  provenance:
    created_by: "FS"
    created_at: "2026-04-28"
    source: "Prompt de inicio generico para agentes (humanos o LLM) que abren una sesion sobre el repo KORA. Citado por handoffs y memoria persistente como punto de entrada. v1.1 (2026-05-31) añade seccion 'Que es KORA' con proposito (repositorio/catalogo/produccion/mantenimiento) y los tres tipos de artefacto, alineada con gobernanza v6.1."
version: "1.1.0"
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

## Que es KORA

KORA es el repositorio, catalogo y sistema de produccion y mantenimiento de
**tres tipos de artefacto**:

- **conocimiento** — `.md` en estandar KORA/MD para *consumo* de sistemas LLM
  (se leen como contexto, no se ejecutan);
- **agentes** (`AGENT.md`) y **skills** (`SKILL.md`) — actores y capacidades que
  se *proyectan a runtimes* (claude-code, codex, openclaw, hermes) via
  transmutacion.

Las specs son la ley, no artefactos. "Conocimiento" es un tipo especifico, no
paraguas de los otros dos. La ecuacion `PMI × LFS + autoria + transmutacion
funtorial` es la garantia formal, no la definicion.

## Prompt minimo

```
Sesion KORA — bootstrap.

Lee primero, en este orden:

1. CLAUDE.md (top-level): fuente operativa unica para gestion del repo,
   topologia post-reorg v5 y comandos vivos.
2. governance/gobernanza.md: precedencia, regimenes URN, lifecycle,
   capas (ontologia / serializacion / runtime / distribucion).
3. El ultimo handoff en docs/handoffs/YYYY-MM-DD-*.md por fecha descendente.
   Es el snapshot vivo del repo.
4. ~/.claude/projects/-home-felix-kora/memory/MEMORY.md: index de
   memorias persistentes; leer las mas recientes que apliquen.

Antes de proponer o tocar nada, verifica estado:

  python3 toolchain/kora index
  python3 toolchain/kora check --strict

Si strict no pasa, diagnostica antes de avanzar; no normalices la deuda.

Cuando vayas a producir artefactos:

- Meta-KORA esta en reconstruccion: no uses los artefactos viejos
  `artifact-curator`, `kora-skills`, `kora-agents`, `knowledge-curator`,
  `curation-conductor`, `kora/custodio`, `kora/guardian` ni `kora/clawforge`
  como fuente o runtime. Lee `urn:kora:kb:meta-kora-rebuild-directive`.
- Habilidades nuevas, agentes nuevos y knowledge no-atomic: partir de specs
  vigentes y crear IR fresco en staging.
- Conocimiento `atomic`: usa `urn:kora:artefacto:atomize`.
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
| Runtime | `runtime/` | `runtime-spec-md.md`, `transmutation-spec.md`, `multiagente-spec.md`, runtime-extensions canonicas (claude-code, codex, openclaw, hermes) |
| Productivo | `artifacts/{agents,knowledge,skills}/` | shape unificado autoria-spec |
| Toolchain | `toolchain/kora`, `toolchain/kora_lib/` | CLI viva |

## Skills core que cualquier agente puede invocar

| URN | Cuando |
|-----|--------|
| `urn:kora:artefacto:mente-omega` | razonamiento estructural-discursivo (pentamotor Φ Ψ Ξ Δ Σ) |
| `urn:kora:artefacto:cat-thinking` | enmarque categorial (24 piezas ICAS-BoK) |
| `urn:kora:artefacto:atomize` | familia atomic productor canonico |

## Personas disponibles (agentes-pt persona)

| URN | Para |
|-----|------|
| `urn:dev:artefacto:steipete` | direccion de ejecucion cognitiva (Peter Steinberger clon) |
| `urn:fxsl:artefacto:allan-kelly` | arquitectura organizacional human-agent |
| `urn:pro:artefacto:david-allen` | claridad operable integral (GTD + regulacion) |

## Targets de transmutacion

```bash
python3 toolchain/kora transmute --target {claude-code|codex|openclaw|hermes} --agent {ns}/{name} --dry-run
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

- Topologia detallada y comandos: `CLAUDE.md`.
- Estado vivo: `docs/handoffs/YYYY-MM-DD-*.md` (por fecha descendente).
- Roadmaps: `docs/plans/*.md`.
- Memoria persistente: `~/.claude/projects/-home-felix-kora/memory/MEMORY.md`.
- Specs canonicas: `governance/`, `ontology/`, `serialization/`, `runtime/`.
