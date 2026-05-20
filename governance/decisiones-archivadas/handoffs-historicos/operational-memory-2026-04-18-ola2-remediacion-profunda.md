---
_manifest:
  urn: "urn:kora:kb:operational-memory-2026-04-18-ola2-remediacion-profunda"
  provenance:
    created_by: "Claude Opus 4.7 (encarnando cat-thinking)"
    created_at: "2026-04-18"
    source: "Memoria operativa del cierre de ola-2 remediación profunda. Snapshot de estado + invariantes + comandos."
version: "1.0.0"
status: publicado
tags: [operational-memory, ola-2, snapshot, invariantes, handoff]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-18-ola2-remediacion-profunda"
    - "urn:kora:kb:next-session-prompt-2026-04-18-ola2-remediacion-profunda"
---

# Memoria operativa — Cierre ola-2 remediación profunda

Snapshot del estado de KORA al cierre de la sesión 2026-04-18 (ola-2
profunda). Comandos, numéricos, invariantes verificables.

## Snapshot numérico

| Métrica | Valor | Comando que la verifica |
|---------|-------|--------------------------|
| Specs constitucionales | 11 | `ls governance ontology serialization runtime \| grep "\\.md$" \| wc -l` |
| Checks registry | 15 | `python3 toolchain/kora check --list` |
| Tests suite | 295 (skipped=2) | `python3 -m unittest discover -s tests` |
| Workspaces productivos | 7 | `ls artifacts/agents/*/*/ \| grep -v _FRAGUA \| wc -l` |
| Habilidades productivas | 1 (`kora/atomize`) | `ls artifacts/skills/*/*/SKILL.md` |
| Agentes en staging (INBOX) | 21 | `ls artifacts/agents/_FRAGUA/INBOX/ \| wc -l` |
| Skills en staging (INBOX) | 7 | `ls artifacts/skills/_TALLER/INBOX/ \| wc -l` |
| Knowledge nodos kb-graph | 505 | `kora kb-graph` |
| Knowledge edges | 271 | `kora kb-graph` |
| Huérfanos reales kb | 318 | `kora kb-graph --orphans` |
| Catalog entries | 603 | `kora index` |

## Cohort productivos (derivado de filesystem, post-H12)

```
kora:           clawforge, curator, custodio, forgemaster, guardian
domain_canary:  gn/digitrans, gn/goreologo
```

## Registry de checks (15)

Por phase:

- **index**: `catalog-exists` (critical).
- **verify**: `autoria-conformance` (high), `coalgebra-conformance` (high),
  `vector-laws` (high), `fidelidad-agentskills` (high), `urn-integrity`
  (high), `workspace-validity` (high), `knowledge-zone` (high),
  `agentfile-dimensions` (medium), `skill-structure` (medium),
  `spec-traces` (medium), `tools-config-coherence` (medium).
- **lint**: `lint-md` (low).
- **graph**: `kb-graph-cycles` (high), `supersedes-consistency` (medium).

## Comandos CLI vigentes

```bash
# Indexación
python3 toolchain/kora index
python3 toolchain/kora resolve "urn:kora:kb:harness-spec"

# Validación
python3 toolchain/kora check --strict
python3 toolchain/kora health --strict
python3 toolchain/kora validate

# Stats y grafo
python3 toolchain/kora stats --json
python3 toolchain/kora graph --json
python3 toolchain/kora kb-graph --json --orphans

# Migración
python3 toolchain/kora migrate --perfil a-autoria [--dry-run]
python3 toolchain/migrate_coalgebra.py [--dry-run]

# Transmutación
python3 toolchain/kora transmute --target agentskills --agent kora/atomize
python3 toolchain/kora transmute --target claude-code --agent kora/curator
python3 toolchain/kora roundtrip-check --agent kora/atomize

# Ingesta inversa
python3 toolchain/kora ingest --from claude-code --file <path>

# Lifecycle
python3 toolchain/kora promote <path>
python3 toolchain/kora promote --cohort <ns>
python3 toolchain/kora deprecate <path> [--supersedes URN] [--force] [--retire]

# Docs
python3 toolchain/kora sync-docs
```

## Invariantes duras

1. **Strict verde**: `kora check --strict` pasa 15/15 al cierre de cualquier sesión.
2. **Shape autoria v1.1**: nuevos artefactos productivos cumplen `autoria-spec §3.4`
   obligatorio + §3.5 opcional (coalgebraico) según `verificacion_coalgebraica`.
3. **Legacy purgado**: `harness_vector`, `presentation` (en), `SOUL.md`, `TOOLS.md`,
   `USER.md`, `IDENTITY.md`, `AGENTS.md` (plural), `config.json` NO vuelven a
   productivos. Están en el set `AUTORIA_LEGACY_SCAFFOLDS`.
4. **Cohort derivado**: `OPERATING_CORE_COHORTS` NO se hardcodea — se computa
   desde `artifacts/agents/{ns}/{name}/AGENT.md` con status=activo.
5. **Regenerables fuera del commit de código**: `docs/generated/catalog.yml`,
   `docs/generated/*`, `_BUILD/` no se commitean junto con cambios de código.
6. **URN canónico agéntico**: `urn:{ns}:artefacto:{id}` para forma material
   `habilidad|subagente|agente-propiamente-tal|agente-plataforma`. Sin versión
   embebida.

## Arquitectura vigente (4 capas v4.3)

```
gobernanza v4.3                      [constitución]
    ↑
harness-spec v1.0                    [ontología PMI × LFS]
    ↑
md-spec v8.1 ←→ knowledge-spec v1.2 ←→ autoria-spec v1.1   [serializaciones]
    ↑                                        ↑
runtime-spec-md v3.7 ←→ transmutation-spec v1.0           [runtime]
    ↑
[claude-code|codex|gemini|openclaw|agentskills]-runtime-extension   [fibras]
```

Runtime-extensions:
- `claude-code-runtime-extension v1.0`
- `codex-runtime-extension v1.0`
- `gemini-runtime-extension v1.0`
- `openclaw-runtime-extension v1.1`
- `agentskills-runtime-extension v1.0` (**nueva en ola-2**)

## Deuda diferida (orden functorial para la próxima ola)

1. H6 qa-spec
2. H5 multiagente-spec
3. H7 curación huérfanos (humana)
4. H2 procesos-spec
5. H23 wrapper Mastra
6. H9, H13, H17, H20, H22 (menores)

## Commits de la sesión

- `2812c09` ola-2 arranque (7 frentes; 1456 archivos, dedup agresivo)
- `2a38143` ola-2 profunda (8 frentes; 17 archivos, 1007 insertions)

Push pendiente a `origin/master` al momento de emitir este documento.

## Archivos nuevos emitidos

- `specs/agentskills-runtime-extension.md` v1.0
- `toolchain/migrate_coalgebra.py` (one-shot migrator)
- `docs/generated/kb-orphans.md` (reporte de clasificación)
- `docs/reports/handoff-2026-04-18-ola2-remediacion-profunda.md`
- `docs/reports/next-session-prompt-2026-04-18-ola2-remediacion-profunda.md`
- `docs/reports/operational-memory-2026-04-18-ola2-remediacion-profunda.md` (este doc)

## Contrato de retoma

Si la próxima sesión arranca desde commit `2a38143` (o posterior en master),
puede asumir sin re-verificar:

- strict 15/15 verde
- 7 productivos son objetos coalgebraicos formales verificables
- agentskills tiene spec, transmutor y round-trip check
- cohort deriva del filesystem

Si la próxima sesión parte desde una rama distinta o commit anterior,
**correr las verificaciones mínimas antes de tocar** — ver §"Snapshot numérico".
