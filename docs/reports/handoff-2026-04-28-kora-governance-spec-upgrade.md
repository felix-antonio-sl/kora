---
_manifest:
  urn: "urn:kora:kb:handoff-2026-04-28-kora-governance-spec-upgrade"
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-28"
    source: "Cierre de sesion: upgrade de gobernanza, autoria, construccion agentica y transmutacion con checks ejecutables."
version: "1.0.0"
status: publicado
tags: [handoff, gobernanza, specs, autoria, construccion-agentica, transmutacion]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:harness-spec"
    - "urn:kora:kb:autoria-spec"
    - "urn:kora:kb:agent-skill-construction-spec"
    - "urn:kora:kb:transmutation-spec"
    - "urn:kora:kb:runtime-spec-md"
---

# Handoff - KORA Governance/Spec Upgrade

## Estado actual

El repo queda en rama principal local `master`, alineada para commit y push a
`origin/master`. El upgrade integra `agent-skill-construction-spec` como norma
vigente de construccion pre-transmutacion y la conecta al pipeline de checks.

La linea final separa tres fibras:

1. construccion de IR fuente (`Req -> Blueprint -> IR`),
2. transmutacion runtime como derivado,
3. verificacion runtime como preocupacion posterior, no requisito de
   construccion.

## Decisiones

1. `governance/gobernanza.md` mantiene `v4.6.0`, cita
   `agent-skill-construction-spec` y la ubica en la capa de serializacion.
2. `serialization/agent-skill-construction-spec.md` queda publicada como
   `v1.0.0`, sin elevar formatos externos o historicos como fuente productiva.
3. La referencia a canario se retiro de la construccion y de la taxonomia
   constitucional de este upgrade; lo que queda es verificacion runtime general.
4. El check `construction-koda-no-copy` fue reemplazado por
   `construction-authoring-shape`, regla positiva que exige envelope vigente
   `artefacto`.
5. Los agentes productivos activos fueron migrados para retirar overlays
   anteriores (`harness_vector`, `presentation`) y quedar idempotentes bajo
   `a-autoria`.
6. `migrate --profile v2-agentfile` ya no reintroduce overlays retirados:
   normaliza hacia `vector_ontologico` y `presentacion`.

## Artefactos relevantes

- `governance/gobernanza.md`
- `serialization/agent-skill-construction-spec.md`
- `serialization/autoria-spec.md`
- `runtime/transmutation-spec.md`
- `runtime/*-runtime-extension.md`
- `toolchain/kora_lib/checks.py`
- `toolchain/kora_lib/migration.py`
- `toolchain/kora_lib/transmute.py`
- `serialization/schemas/kora-transmutation-schema.json`
- `tests/test_check_pipeline.py`
- `tests/test_cli_smoke.py`
- `tests/test_migrate_autoria.py`

## Checks nuevos o ajustados

El registry queda en 30 checks. Los checks de construccion vigentes son:

- `construction-source-primary`
- `construction-vector-fit`
- `construction-knowledge-explicit`
- `construction-fsm-valid`
- `construction-interface-typed`
- `construction-risk-declared`
- `construction-runtime-separation`
- `construction-categorical-minimality`
- `construction-authoring-shape`

## Validacion ejecutada

- `python3 toolchain/kora index`: OK, 665 artefactos indexados.
- `python3 toolchain/kora check --strict`: 30/30 OK.
- `python3 toolchain/kora validate --profile strict`: 15 valid, 0 invalid.
- `python3 toolchain/kora kb-graph --json --orphans`: 0 broken edges, 0 cycles,
  11 huerfanos reales.
- `python3 -m unittest discover -s tests`: 355 OK, 1 skipped.
- `python3 toolchain/kora migrate --profile a-autoria --dry-run`: 0 cambios.

## Pendientes

1. Al construir el proximo agente o skill, correr el gate por path sobre el
   workspace staging antes de promover.
2. Si el artefacto incluye runtime, transmutar solo despues de que el IR fuente
   pase `check --strict`.
3. Los materiales en `_FRAGUA/INBOX` siguen siendo insumos: deben absorberse a
   `autoria-spec` antes de promocion.
4. Los 11 huerfanos reales del grafo quedan fuera de este perimetro; no bloquean
   el upgrade, pero conviene clasificarlos en una ola posterior.

## Supuestos

- La rama principal operacional del repo es `master`, aunque el usuario la
  nombre como rama principal.
- Los cambios en `docs/generated/` son derivados; no hay diff material despues
  de `index` y `kb-graph`.
- `artifacts/agents/salud/salubrista-hah/AGENT.md` esta deprecado y queda fuera
  del gate productivo.
- Staging puede contener shapes antiguos mientras no se promuevan.

## Riesgos

- Si alguien ejecuta herramientas externas que escriben formatos retirados, el
  gate los detendra, pero staging puede acumular ruido.
- El nuevo schema de transmutacion exige `jsonschema` disponible en el entorno.
- La verificacion runtime estricta depende de la fidelidad de traza declarada
  por cada runtime-extension.
- El push usa remoto SSH `git@github.com:felix-antonio-sl/kora.git`; puede fallar
  si el agente no tiene credenciales SSH disponibles.

## Handoff operativo

Estado listo para commit semantico. El commit debe abarcar este upgrade como
unidad atomica: specs, checks, migraciones, transmutacion, schemas, tests,
handoff y memoria. No separar los agentes productivos migrados, porque son la
evidencia de que el nuevo gate cierra sobre el corpus activo.
