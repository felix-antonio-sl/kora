---
_manifest:
  urn: urn:kora:kb:cheat-sheet-uso-productivo
  provenance:
    created_by: Claude Opus 4.7
    created_at: '2026-05-19'
    source: Cheat sheet operativo derivado del estado vigente del repo tras refactors
      2026-05-17/18 (knowledge-spec v2.0, md-spec v9.0, agent-skill-construction-spec
      v1.1, autoria-conformance endurecido, relations-laws, coalgebra-conformance
      activable).
version: 1.0.0
status: publicado
tags:
- cheat-sheet
- productivo
- guia
- operativo
- kora
- cli
- lifecycle
lang: es
extensions:
  kora:
    family: guide
    shard_index: 1
    shard_count: 2
    shard_root_urn: urn:kora:kb:cheat-sheet-uso-productivo
relations:
  cites:
  - urn:kora:kb:gobernanza
  - urn:kora:kb:md-spec
  - urn:kora:kb:knowledge-spec
  - urn:kora:kb:autoria-spec
  - urn:kora:kb:harness-spec
  - urn:kora:kb:agent-skill-construction-spec
---

# Cheat Sheet — Uso productivo de KORA


## Resumen

Guia operativa de una sola lectura para producir artefactos KORA validos
en el primer intento. Cubre anclaje, pipelines de curacion, identidad
URN, lifecycle, decisiones rapidas de shape y recuperacion de errores
comunes. Refleja el estado vigente tras los refactors 2026-05-17/18.

## 1. Anclaje al iniciar sesion

```bash
# Confirmar rol del host (primary autoriza push; secondary trabaja via PR)
python3 toolchain/kora host

# Foto del repo antes de tocar nada
python3 toolchain/kora index
python3 toolchain/kora check --strict

# Handoff mas reciente — leer SIEMPRE antes de operar
ls -t docs/handoffs/ | head -3
```

Reglas duras:

1. Specs en **freeze formal**: `harness-spec`, `autoria-spec`,
 `transmutation-spec` (`gobernanza §8.3`). NO se tocan sin HITL
 explicito.
2. WIP del operador (archivos en `M` o `??` no propios) **no se toca**.
3. Si `check --strict` rompe con cambios no propios, investigar antes
 de hacer nada.

## 2. Comandos CLI vivos

| Comando | Uso | Cuando |
| --- | --- | --- |
| `kora host` | Rol del host (primary/secondary) | Inicio de sesion |
| `kora index` | Reconstruye `docs/generated/catalog.yml` | Tras cualquier cambio en artefactos |
| `kora check --strict` | Ejecuta los 34 checks | Antes de commit |
| `kora check --list` | Catalogo de checks con severidad y spec_ref | Diagnostico |
| `kora resolve <urn>` | URN → path local | Localizar artefacto |
| `kora validate` | Schema validation de workspaces | Diagnostico fino |
| `kora lint-md` | Lint estructural de KORA/MD productivos | Antes de promover |
| `kora intake` | Estado fuentes vs artefactos | Vista pipeline |
| `kora atomize` | Productor canonico familia `atomic` | Atomizacion de corpus denso |
| `kora promote <path>` | `_SCRIPTORIUM/REVIEW/` o `_TALLER/REVIEW/` → productivo | Cierre de curacion |
| `kora deprecate <path>` | productivo → deprecado (detecta dependientes) | Retirar artefacto |
| `kora kb-graph --json --orphans` | Grafo + huerfanos | Auditoria de tejido |
| `kora migrate --perfil a-autoria` | Codemod shape legacy → autoria-spec | Migracion masiva |
| `kora transmute --target <X>` | Proyeccion IR → runtime | Deploy |
| `kora doctor` | Salud agregada | Diagnostico rapido |

## 3. Identidad URN — dos regimenes

```text
urn:{namespace}:kb:{id} # conceptual (knowledge, specs)
urn:{namespace}:artefacto:{id} # agentico (agents, skills)
```

Reglas:

1. **Version SIEMPRE fuera del URN**, en campo `version` root.
2. **Namespace del URN coincide con primer subdir** bajo
 `artifacts/{knowledge,agents,skills}/`. Enforcement: `knowledge-zone`
 (knowledge) y `autoria-conformance` (agentes/skills).
3. Referencias a otros artefactos usan URN sin version; la version la
 resuelve el catalogo.
4. URN se preserva durante todo el lifecycle de un artefacto. Cambiar
 URN equivale a emitir un artefacto nuevo (usar `supersedes`).

Correcto:

```text
urn:kora:kb:harness-spec
urn:salud:artefacto:salubrista
urn:kora:artefacto:atomize
```

Incorrecto:

```text
urn:kora:kb:harness-spec:1.0.0 # version embebida
urn:kora:agent:salubrista # regimen retirado
urn:kora:skill:atomize:1.0.0 # regimen retirado
```

## 4. Pipeline de curacion (por tipo de artefacto)

### 4.1 Knowledge — `artifacts/

```text
_SCRIPTORIUM/INBOX/ crudo, pre-categorial, sin URN
 ↓
_SCRIPTORIUM/REVIEW/{ns} borrador, URN provisional
 ↓ kora promote
artifacts/ publicado (productivo) o deprecado
```

Lifecycle conceptual: `borrador → publicado → deprecado`. Sin reversa.

Productor canonico de familia `atomic`: invocar `kora atomize` desde
`artifacts/skills/kora/atomize/` (no escribir atomic a mano).

### 4.2 Skills — `artifacts/skills/`

```text
_TALLER/INBOX/{name}/ pre-categorial
 ↓
_TALLER/REVIEW/{name}/ borrador, shape autoria valido
 ↓ kora promote
artifacts/skills/{ns}/{name}/ activo (productivo)
```

Lifecycle agentico: `borrador → activo → deprecado → retirado`. Sin
reversa.

### 4.3 Agents — `artifacts/agents/`

```text
_FRAGUA/INBOX/{ns}/{name}/ pre-categorial
 ↓
_FRAGUA/REVIEW/{ns}/{name}/ borrador
 ↓ kora promote
artifacts/agents/{ns}/{name}/ activo (productivo)
```

Idem lifecycle agentico. Promocion entre formas materiales
(habilidad → subagente → agente-propiamente-tal → agente-plataforma)
preserva URN y bumpea version major (`autoria-spec §8`).

## 5. Familias documentales

Solo aplicable a knowledge KORA/MD (no a skills/agents). Fuente unica:
`md-spec §5.6`. Resumen operativo:

| Familia | Cuando usar | Invariante distintivo |
| --- | --- | --- |
| `spec` | Documento normativo (vive en `governance/`, `ontology/`, `serialization/`, `runtime/`) | RFC 2119, `Traces to:`, tabla validacion con `Enforcement` |
| `guide` | Manual o cheat sheet operativo | `## Resumen` recomendado |
| `normative` | Texto legal o reglamento koraficado | Numerales como `##` con asunto semantico |
| `glossary` | Glosario | Buckets con alias explicitos |
| `faq` | Preguntas frecuentes | `##` por pregunta |
| `catalog` | Catalogo tabulado | Columnas minimas `id \| urn \| titulo \| resumen` |
| `cq_catalog` | Subperfil catalog para competency questions | `## Resumen` obligatorio |
| `inventory` | Lista operativa | `publication_class=control` queda fuera de KB |
| `organigram` | Estructura organizacional | Dependencias explicitas, no headings-campo |
| `atomic` | Proposiciones atomicas | Productor canonico: `kora atomize` |
| `note` | Nota tecnica | `##` tematico minimo |
| `adr` | Architecture Decision Record | `## Contexto, Alternativas, Decision, Consecuencias, Trazabilidad` |

Auxiliares (clasificacion derivada por toolchain, no se declaran):
`bok`, `source`, `source-alias`, `generic`.

## 6. Estado y lifecycle

### 6.1 Status vigentes

```text
Knowledge: borrador → publicado → deprecado
Agentico: borrador → activo → deprecado → retirado
```

Status DEBE estar en root del frontmatter, NO dentro de `_manifest`.
Si esta dentro de `_manifest`, ejecutar `kora migrate --perfil a-autoria`
para auto-fix.

### 6.2 Coherencia status-por-directorio (enforcement)

| Ubicacion | Status valido |
| --- | --- |
| `_SCRIPTORIUM/INBOX/`, `_TALLER/INBOX/`, `_FRAGUA/INBOX/` | `borrador` o sin `_manifest` |
| `_SCRIPTORIUM/REVIEW/`, `_TALLER/REVIEW/`, `_FRAGUA/REVIEW/` | `borrador` |
| `artifacts/ | `publicado` o `deprecado` |
| `artifacts/agents/{ns}/{name}/` o `artifacts/skills/{ns}/{name}/` | `activo`, `deprecado` o `retirado` |

Violaciones detectadas por `knowledge-zone` y `autoria-conformance`.

## 7. Decisiones rapidas

### 7.1 Forma material (`autoria-spec §5`)

| Vector hint | Forma sugerida | Topologia |
| --- | --- | --- |
| `mu≤1, lambda=0, sin workspace` | `habilidad` | `artifacts/skills/{ns}/{name}/SKILL.md` |
| `Invocado por otro agente, no por humano` | `subagente` | `artifacts/agents/{ns}/{name}/AGENT.md` |
| `Workspace + memoria + ciclo propio` | `agente-propiamente-tal` | `artifacts/agents/{ns}/{name}/AGENT.md` + memoria |
| `Materia ambiental, always-on` | `agente-plataforma` | runtime-extension dependiente (hoy: solo OpenClaw) |

Principio: usar **la forma mas baja** que satisface el objetivo. Sobre-formalizar
deja deuda.

### 7.2 Vector PMI × LFS (`harness-spec §3`)

```text
pi ∈ {0..3} — Plan (monada libre)
mu ∈ {0..3} — Materia (comonada libre)
xi ∈ {0..4} — Interaccion
lambda ∈ {0..3} — Sociotecnico
phi ∈ {0..4} — Acoplamiento humano
sigma ∈ [v1..v5], vᵢ ∈ {0..3} — Etico [safety, fairness, transparency, accountability, sustainability]
```

Leyes inter-eje (`harness-spec §4.1`) que el check `vector-laws` enforza:

- `pi≥3 ⇒ mu≥1` (fixed-points requieren estado)
- `xi=4 ⇒ lambda≥1` (operad dinamica requiere composicion organizacional)
- `phi≥2 ⇒ mu≥1` (colaborativo requiere memoria observable)
- `sigma.accountability≥2 ⇒ sigma.transparency≥2`
- `lambda=3 ⇒ todos los sigma_i ≥ 2`

### 7.3 Cuando activar coalgebra (`autoria-spec §3.5`)

Activar `extensions.kora.verificacion_coalgebraica: true` cuando:

- Agente tiene FSM real con **transiciones explicitas** (no solo lista
 narrativa de estados).
- Quieres invariantes verificables: termination + safety closure.

NO activar si los `estados` son solo fases narrativas; el check
`coalgebra-conformance` fallara.

## 8. Checks vivos — diccionario operativo

| Check | Severidad | Detecta | Fix |
| --- | --- | --- | --- |
| `catalog-exists` | critical | Catalogo ausente | `kora index` |
| `urn-integrity` | high | Referencias URN broken | corregir URN |
| `knowledge-zone` | high | Knowledge productivo sin manifest, mal status o ns | mover a REVIEW o corregir |
| `autoria-conformance` | high | AGENT.md/SKILL.md fuera de shape | `kora migrate --perfil a-autoria` |
| `vector-laws` | high | Violacion de leyes inter-eje | ajustar vector |
| `coalgebra-conformance` | high (si flag true) | FSM mal formado, termination o safety closure | corregir FSM |
| `relations-laws` | high | Ciclos en supersedes/refines o antisimetria | romper ciclo editorial |
| `kb-graph-cycles` | high | Ciclo en grafo `depends` | romper ciclo |
| `lint-md` | low | Formato KORA/MD | `kora lint-md --fix` |
| `skill-structure` | medium | Subdirs no canonicos en habilidad | renombrar a `scripts/referencias/recursos` |
| `traces-requirements-semantics` | high | `traces_requirements` apunta a no-requirement | reclasificar target |
| `supersedes-consistency` | medium | `supersedes` apunta a no-deprecado | deprecar target |
| `formal-trace-discipline` | medium | `Traces to:` fuera de Formal Layer | usar Rationale o corregir URN |
| `spec-traces` | medium | `Traces to:` apunta a formal/XX inexistente | corregir referencia |
| `fidelidad-agentskills` | high | Habilidad no transmuta byte-identical | corregir shape |
| `fidelidad-mastra` | high | Proyeccion Mastra fuera de dominio | ajustar vector o forma |
| `compromisos-eticos-no-todo` | high | Literal `TODO` en compromisos eticos | escribir contenido |
| `construction-*` | varios | Reglas pre-transmutacion | ver `agent-skill-construction-spec §5.2` |
| `staging-vs-productive-divergence` | medium | Nombre duplicado en staging y productivo | renombrar o deprecar |
| `portabilidad-tests` | medium | Paths no portables en tests | usar helpers de `tests/common.py` |
| `spec-procedure-coherence` | medium | Spec con desalineacion version/H1/CLI | sincronizar |
| `claude-code-budget-piso` | medium | `max_turns` < piso derivado | bajar vector o subir budget |
| `tools-config-coherence` | medium | TOOLS.md vs config.json desincronizados | sincronizar |
| `bundle-coherence` | high | AGENT.md declara skill inexistente | crear skill o quitar ref |
| `agentfile-dimensions` | medium | AGENT.md sin dimensiones requeridas | completar shape |

## 9. Antipatrones — que NO hacer

| Antipatron | Falla | Correccion |
| --- | --- | --- |
| Editar `status: borrador → publicado` a mano y mover archivo | Salta el pipeline, ningun check ejecutado | usar `kora promote` |
| Copiar `_manifest.urn` con version embebida | Regimen URN retirado | quitar `:{version}` del URN, usar campo `version` root |
| Declarar `status` o `version` dentro de `_manifest` | Shape mixto invalido | `kora migrate --perfil a-autoria` o mover a root |
| Crear skill con `mu≥2` declarando `forma_material: habilidad` | Dominio invalido | promover a `subagente` o reducir `mu` |
| Editar `docs/generated/catalog.yml` a mano | Vista derivada, no fuente | regenerar con `kora index` |
| Agregar URN en `relations` que apunta a nodo retirado | `urn-integrity` rompe | usar Rationale o re-emitir referencia |
| `supersedes` bidireccional (`A→B` y `B→A`) | Antisimetria rota | decidir direccion temporal, eliminar una arista |
| `_BUILD/{target}/` como fuente primaria | Output derivado, no IR | mover IR a workspace, mantener `_BUILD/` gitignored |
| Productor canonico en staging con URN ya hardcodeado en toolchain | Inconsistencia spec/codigo | promover a productivo (lo que paso con atomize) |
| Mencionar Hermes como target | Bloqueado HITL (`gobernanza §8.2`) | usar runtime activo (claude-code, codex, openclaw...) |
