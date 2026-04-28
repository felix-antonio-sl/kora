# KORA

Monorepo de gobernanza, ontologia, serializacion, runtimes y artefactos
agenticos. No es una aplicacion tradicional: el activo principal es la
coherencia entre specs, knowledge, agentes, skills y toolchain.

## Historia corta

- Hasta la reorg v5 del `2026-04-18`, el repo usaba una topologia legacy con
  `specs/`, `AGENTS/`, `SKILLS/`, `KNOWLEDGE/`, `schemas/` y `scripts/`.
- La reorg v5 hizo visibles en el filesystem las capas constitucionales y movio
  los artefactos productivos a `artifacts/` y la CLI a `toolchain/`.
- El cierre estructural del `2026-04-19` agrego `qa-spec`, `procesos-spec`,
  `risk-register-spec`, `multiagente-spec` y el target `mastra`.
- Si encuentras rutas legacy en handoffs viejos o wrappers de compatibilidad,
  tratarlas como historia o fallback, no como topologia actual.

## Composicion actual

| Capa | Path | Rol |
|------|------|-----|
| Constitucion | `governance/` | Precedencia y reglas meta del sistema |
| Ontologia | `ontology/` | Modelo canonico de artefactos y procesos |
| Serializacion | `serialization/` | Shapes de authoring y schemas JSON |
| Runtime | `runtime/` | Proyecciones, transmutacion y extensiones por plataforma |
| Artefactos | `artifacts/` | Knowledge, agentes y skills productivos o en staging |
| Toolchain | `toolchain/` | CLI `kora`, `kora_lib/`, checks y utilitarios soportados |
| Tests | `tests/` | Suite ejecutable del repo |
| Docs derivadas | `docs/generated/` | Vistas materializadas regenerables |
| Handoffs y memoria | `docs/reports/`, `docs/plans/` | Evidencia historica y documentos operativos |

Topologia rapida:

```text
kora/
  governance/
  ontology/
  serialization/
    schemas/
  runtime/
  artifacts/
    knowledge/
    agents/
    skills/
  toolchain/
    kora
    kora_lib/
  tests/
  docs/
    generated/
    reports/
    plans/
```

## Artefactos y staging

Los pipelines activos viven bajo `artifacts/`:

- Knowledge:
  `artifacts/knowledge/_SCRIPTORIUM/INBOX/ -> REVIEW/ -> artifacts/knowledge/{ns}/...`
- Agentes:
  `artifacts/agents/_FRAGUA/INBOX/ -> REVIEW/ -> artifacts/agents/{ns}/{name}/`
- Skills:
  `artifacts/skills/_TALLER/INBOX/ -> REVIEW/ -> artifacts/skills/{ns}/{name}/`

Los directorios de staging son pre-categoriales: no representan namespace
canonico hasta que el artefacto se promueve.

## Source Of Truth

- El source of truth es el filesystem con manifests validos.
- `docs/generated/catalog.yml` es una vista materializada generada por
  `python3 toolchain/kora index`. No es autoritativa.
- `docs/generated/*` es derivado y regenerable. No escribas conteos a mano.
- Si `README.md`, handoffs viejos o wrappers legacy contradicen a la CLI actual
  o a las specs vigentes, manda la CLI actual y las specs.

## Specs vivas

Las capas visibles en el repo son:

- `governance/gobernanza.md`
- `ontology/harness-spec.md`
- `ontology/qa-spec.md`
- `ontology/procesos-spec.md`
- `ontology/risk-register-spec.md`
- `serialization/autoria-spec.md`
- `serialization/agent-skill-construction-spec.md`
- `serialization/md-spec.md`
- `serialization/knowledge-spec.md`
- `runtime/runtime-spec-md.md`
- `runtime/transmutation-spec.md`
- `runtime/multiagente-spec.md`
- `runtime/*-runtime-extension.md`

La Formal Layer oficial vive en
`artifacts/knowledge/kora/categorical-foundations/`. El corpus
`artifacts/knowledge/fxsl/cat/` sigue siendo auxiliar.

## CLI base

Entrypoint soportado: `python3 toolchain/kora`.

Comandos base:

```bash
python3 toolchain/kora index
python3 toolchain/kora resolve "urn:kora:kb:harness-spec"
python3 toolchain/kora check --strict
python3 toolchain/kora check --list
python3 toolchain/kora stats --json
python3 toolchain/kora graph --json
python3 toolchain/kora kb-graph --json --orphans
python3 toolchain/kora transmute --help
python3 toolchain/kora ingest --help
python3 toolchain/kora sync-docs
```

La maintenance gate por defecto ya no es una secuencia manual de `health` y
`validate`: el punto de entrada recomendado es `check --strict`, que compone
los checks activos del repo. Los subcomandos especializados (`health`,
`validate`, `lint-md`, `migrate`, `promote`, `deprecate`) siguen existiendo y
se usan cuando la tarea lo requiere.

## Runtimes target

Segun `python3 toolchain/kora transmute --help`, los siete targets soportados
hoy son:

- `agentskills`
- `claude-code`
- `codex`
- `gemini`
- `mastra`
- `opencode`
- `openclaw`

Cada uno tiene su `runtime/{nombre}-runtime-extension.md` con dominio + matriz
de preservacion.

## Verificacion minima

Despues de cambios estructurales o documentales relevantes:

```bash
python3 toolchain/kora index
python3 toolchain/kora check --strict
python3 -m unittest discover -s tests
python3 toolchain/kora kb-graph --json --orphans
```

Usa `python3 toolchain/kora sync-docs` solo cuando quieras regenerar
explicitamente salidas publicas en `docs/generated/`.

## Notas practicas

- Antes de operar, leer el handoff mas reciente bajo
  `docs/reports/handoff-*.md` por fecha descendente. Bootstrap copiable en
  `docs/start-prompt.md`.
- No asumas que `scripts/` raiz es la toolchain viva; hoy es solo residuo de
  compatibilidad.
- No asumas el layout pre-v5 (`specs/`, `AGENTS/`, `SKILLS/`, `KNOWLEDGE/`,
  `schemas/`) como actual.
- No mantengas snapshots numericos a mano en docs generales; obtenlos con la
  CLI.
- Si necesitas la forma real del repo, inspecciona el arbol y no un handoff
  historico aislado.

## Pruebas

La suite se ejecuta con:

```bash
python3 -m unittest discover -s tests
```

## Licencia

CC-BY-4.0
