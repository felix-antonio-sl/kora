---
_manifest:
  urn: urn:kora:kb:adr-poda-radical-2026-05-21
  provenance:
    created_by: Claude Opus 4.7
    created_at: '2026-05-21'
    source: 'Directiva HITL operador 2026-05-21: sacar todo lo innecesario que no
      aporte a la finalidad de KORA. Aplicacion del criterio de convergencia (KORA
      v9) sobre el corpus completo.'
version: 1.0.0
status: publicado
tags:
- adr
- poda-radical
- simpleza
- retiro-masivo
- convergencia
lang: es
extensions:
  kora:
    family: adr
    adr:
      contexto: 'Directiva HITL del operador 2026-05-21: ''Sacar todo lo innecesario
        y que no aporte a la finalidad de la existencia de kora''. Criterio: el proposito
        vigente de KORA (KORA v7 esencial) es gestionar ciclo de vida de 3 tipos de
        artefactos (conocimiento, agentes, skills, donde estos dos ultimos son el
        mismo objeto agentico variando por arnes per autoria-spec v2.0), transmutables
        a 4 runtimes canonicos (claude-code, codex, openclaw, hermes), en formato
        IR agnostico. Maxima simpleza con rigor y potencia. Estado pre-decision: el
        repo acumulo ~300+ archivos historicos sin clientes vivos (toolchain legacy
        de migraciones cerradas, material crudo retirado, skills meta-KORA en _rebuild_required
        cerrados, handoffs antiguos en docs/reports, planes de usina cumplidos, agent-skill-construction-spec
        con contenido redundante).'
      alternativas:
      - 'Status quo: dejar acumulacion historica (carga visual y conceptual sin valor
        operativo)'
      - 'Poda conservadora: solo dead code obvio (toolchain legacy + constantes ATOMIC_*)'
      - 'Poda radical: eliminar todo lo que no sostenga la finalidad declarada (elegida)'
      factorizacion_elegida: decision = retirar_dead_code ∘ eliminar_material_retirado_residual
        ∘ archivar_handoffs_historicos ∘ retirar_spec_redundante ∘ preservar_URNs_donde_aporten_trazabilidad
      consecuencias:
      - 'toolchain/legacy_migration/: 28 scripts one-shot de migraciones cerradas
        eliminados (incluye atomize.py 1230L dead code post-retiro)'
      - Constantes ATOMIC_* en validation.py eliminadas (71 ocurrencias, dead code
        post-retiro atomize)
      - 'artifacts/knowledge/_SCRIPTORIUM/INBOX/_atomic-retirado-2026-05-20/: 225
        archivos eliminados (material crudo retirado en commit anterior, 4.2 MB)'
      - 'artifacts/skills/_TALLER/INBOX/_rebuild_required/: 4 skills legacy eliminados
        (artifact-curator, curation-conductor sin productivo; kora-agents, kora-skills
        con productivo activo)'
      - 'docs/reports/handoff-*: 23 handoffs antiguos pre-mayo movidos a governance/decisiones-archivadas/handoffs-historicos/'
      - 'docs/plans/: planes de usina cumplidos movidos a _archivo (la politica-handoffs.md
        viva permanece)'
      - 'docs/superpowers/: 6 archivos planes/specs de skills ya productivos eliminados'
      - 'serialization/agent-skill-construction-spec.md: deprecada con contenido vivo
        absorbido en autoria-spec o eliminado; 7 refs vivas actualizadas'
      - 'Reduccion estimada: ~300+ archivos retirados; ~5+ MB de material redundante;
        un spec menos viva'
      estado: aceptada
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:adr-poda-radical-2026-05-21
relations:
  cites:
  - urn:kora:kb:gobernanza
  - urn:kora:kb:adr-kora-v7-esencial
  - urn:kora:kb:adr-kora-v9-separacion-descriptivo-prescriptivo-y-arnes
  - urn:kora:kb:meta-kora-rebuild-directive
  refines:
  - urn:kora:kb:adr-kora-v9-separacion-descriptivo-prescriptivo-y-arnes
---

# ADR — Poda radical (2026-05-21)

## Contexto

Directiva HITL del operador (2026-05-21):

> "Sacar todo lo innecesario y que no aporte a la finalidad de la
> existencia de kora."

### Criterio

El proposito vigente de KORA (cristalizado en KORA v7 esencial):

> Sistema que gestiona con specs estrictas la generacion, mantenimiento,
> catalogo y ciclo de vida de artefactos de conocimiento, agentes y
> skills (en formato agnostico y generico) que se transmuten a las
> plataformas claude-code, codex, openclaw, hermes. Maxima simpleza,
> manteniendo rigor y potencia.

Todo lo que **NO sostiene** esta finalidad sale. Lo que aporta:

| Categoria | Aporta porque |
|-----------|----------------|
| Specs activas (gobernanza, harness, autoria v2, md-spec v11, spec-md v1, knowledge-spec v3, runtime-spec-md, transmutation-spec, multiagente, 4 runtime-extensions canonicas + hermes stub) | Definen ontologia, shape, formato, pipeline, transmutacion |
| Toolchain vigente (kora index, check, promote, migrate, transmute, kb-graph, deprecate, host) | Materializa specs en operaciones |
| Artefactos productivos (6 agents + 35 skills + knowledge KORA/MD) | Son el resultado del sistema |
| ADRs y handoffs recientes (`docs/handoffs/2026-05-*`) | Trazabilidad operativa vigente |
| meta-kora-rebuild-directive | Doctrina activa sobre el rebuild |

### Estado pre-decision: acumulacion historica

Auditoria al 2026-05-21:

- **`toolchain/legacy_migration/`**: 28 scripts one-shot de migraciones
 ya cerradas (`migrate_to_agentfile.py`, `move_agents.py`,
 `consolidate_catalogs.py`, `atomize.py` 1230L dead code post-retiro,
 etc.).
- **Constantes `ATOMIC_*`** en `validation.py`: 71 ocurrencias, dead
 code post-retiro de atomize (2026-05-20).
- **`_SCRIPTORIUM/INBOX/_atomic-retirado-2026-05-20/`**: 225 archivos
 atomic-* retirados ayer; ocupan 4.2 MB.
- **`_TALLER/INBOX/_rebuild_required/2026-05-03/kora/`**: 4 skills
 legacy (`artifact-curator`, `curation-conductor`, `kora-agents`
 legacy, `kora-skills` legacy). `meta-kora-rebuild-directive v1.1`
 declara `status: retirado`, `current_is_source: false`. Sin
 reactivacion pendiente.
- **`docs/reports/handoff-*`**: 23 handoffs pre-mayo (la convencion
 vigente desde 2026-05-07 es `docs/handoffs/`).
- **`docs/plans/`**: planes de usina (2026-04-19), recomendaciones de
 personas. Algunos cumplidos.
- **`docs/superpowers/`**: 6 archivos planes/specs de
 `urgenciologo-walking-skeleton`, `jointjs-open-source`,
 `curation-conductor` (los dos primeros ya estan productivos; el
 tercero quedo cerrado).
- **`serialization/agent-skill-construction-spec.md`**: su contenido
 esta mayormente delegado a `autoria-spec` desde v1.1 (commit
 `ca5467f`). Mantiene 7 refs vivas; valor incremental bajo.

## Alternativas consideradas

### A1. Status quo

Dejar la acumulacion historica.

**Por que NO**: contradice la directiva HITL explicita.

### A2. Poda conservadora

Solo dead code obvio (toolchain legacy + constantes ATOMIC_*).

**Por que NO**: deja la mayoria del ruido. La directiva pide "todo lo
innecesario".

### A3. Poda radical (elegida)

Eliminar todo lo que no sostiene la finalidad declarada. Preservar
URNs solo donde aporten trazabilidad operacional concreta.

**Por que SI**:
- Refleja la directiva.
- Convergencia categorial: lo que queda es necesario.
- Reduce carga visual y conceptual para futuras sesiones.

## Decision

Poda radical en 5 fases, ejecutada en una sesion coordinada.

### Fase A: Toolchain dead code

- Eliminar `toolchain/legacy_migration/` completo (28 scripts).
- Eliminar constantes `ATOMIC_*` en `validation.py` y refs muertas
 (`ATOMIC_ALLOWED_TYPES`, `ATOMIC_HARD_MAX_PROPOSITIONS`,
 `ATOMIC_SOFT_SEGMENT_TARGET_CHARS`, `ATOMIC_PRODUCER_URN`,
 `ATOMIC_PROP_LINE_*`, `ATOMIC_SOURCE_*`, `ATOMIC_SEGMENT_*`).
- Eliminar `atomic` de `FAMILY_MAX_*` mappings.
- Eliminar refs a familia atomic en `_check_lint_md` y funciones
 asociadas.
- `VALID_FAMILIES` saca `atomic`.

### Fase B: Material crudo retirado

- Eliminar `artifacts/
 completo (225 archivos, 4.2 MB). El retiro fue documentado en
 commit `d82c9f1`; mantener el directorio era preservacion excesiva.

### Fase C: Skills meta-KORA en _rebuild_required

- Eliminar `artifacts/skills/_TALLER/INBOX/_rebuild_required/2026-05-03/kora/`
 completo (4 skills). Per `meta-kora-rebuild-directive v1.1` estan
 CERRADOS sin reactivacion pendiente.

### Fase D: Docs historicos

- Mover `docs/reports/handoff-*` (23 archivos pre-mayo) a
 `governance/decisiones-archivadas/handoffs-historicos/`.
- Mover `docs/plans/*` cumplidos a `docs/plans/_archivo/` (estructura
 existente):
 - `2026-04-19-kora-*-usina-*.md` (planes de usina cumplidos)
 - `2026-04-19-kora-hitl-encendido.md` (cumplido)
 - `recomendaciones-*.md` (incorporadas a personas omega productivas)
- Mantener `docs/plans/2026-05-07-politica-handoffs.md` (politica viva).
- Eliminar `docs/superpowers/` completo (6 archivos: skills ya
 productivos; planes/specs sin valor incremental).

### Fase E: agent-skill-construction-spec

- Deprecar `serialization/agent-skill-construction-spec.md`. El
 contenido vivo (modelo categorial Build, fases A-H) ya esta absorbido
 en `autoria-spec v2.0`.
- Actualizar 7 refs vivas:
 - `governance/gobernanza.md` → quitar de §3 lista jerarquica y
 §3.2 capa serializacion.
 - `toolchain/kora_lib/checks.py` → spec_ref que la mencione apunta
 a `autoria-spec`.
 - `artifacts/skills/kora/kora-agents/SKILL.md` → quitar cite o
 apuntar a autoria-spec.
 - `artifacts/skills/kora/custodio-kora/SKILL.md` + canon-operativo
 → quitar cite o apuntar a autoria-spec.
 - `artifacts/skills/kora/kora-skills/SKILL.md` → idem.

### Lo que NO se toca

- **Artefactos productivos**: 6 agents + 35 skills + ~640 knowledge
 KORA/MD.
- **Specs activas** vigentes (10 specs vivas tras Fase E).
- **ADRs en `artifacts/ trazabilidad
 arquitectural.
- **`docs/handoffs/2026-05-*`**: handoffs recientes convencion vigente.
- **`governance/decisiones-archivadas/skills-retiradas/atomize/`**:
 preservacion URN del retiro reciente (`urn:kora:artefacto:atomize`).
- **`governance/decisiones-archivadas/specs-en-pausa/`**: 4
 runtime-extensions archivadas con URN preservado.
- **`governance/decisiones-archivadas/specs-absorbidas/host-roles.md`**
 si existe (preservacion URN).
- **`artifacts/
 doctrina activa sobre el rebuild.
- **`docs/plans/2026-05-07-politica-handoffs.md`**: politica viva.
- **`docs/plans/_archivo/2026-05-poda-version-a/`**: archive vigente.
- **`docs/start-prompt.md`**: bootstrap activo.
- **`docs/README.md`**: README del directorio.

## Consecuencias

### Positivas

- **Repo mas chico**: ~300+ archivos eliminados; ~5+ MB reducidos.
- **Toolchain sin dead code**: validation.py limpio, sin
 legacy_migration/.
- **Una spec menos viva** (agent-skill-construction-spec deprecada).
- **Convergencia continua**: cada cosa que queda esta porque aporta.

### Negativas

- **Refs git history quedan obsoletas**: handoffs antiguos quedan en
 `decisiones-archivadas/`, no eliminados. URNs preservados donde
 aportan.
- **Material crudo perdido**: los 225 atomic-retirados se eliminan
 fisicamente. Si en el futuro se quiere koraficar ese corpus
 (KODA-style sin atomic), hay que recuperar desde sources/ o
 re-acquirir.

### Riesgos

- **Refs a agent-skill-construction-spec en `_BUILD/`**: los outputs
 transmuted de algunos skills citan esta spec. Quedan obsoletos
 cuando se retira; al regenerar `_BUILD/` se reflejara el retiro.

## Trazabilidad

Esta ADR refines `urn:kora:kb:adr-kora-v9-separacion-descriptivo-prescriptivo-y-arnes`
(que ya inicio la convergencia separando regimenes). Este retiro
materializa la convergencia sobre el corpus completo.

## Estado

`aceptada` — implementacion en mismo commit que produce este ADR.
