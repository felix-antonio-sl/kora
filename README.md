# KORA

Monorepo de especificaciones, conocimiento y workspaces de agentes gobernados por una capa formal categorial y una toolchain ejecutable.

## Que Es

KORA organiza el ecosistema en cuatro estratos:

- `specs/`: ley operativa del sistema.
- `KNOWLEDGE/`: artefactos descriptivos KORA/MD.
- `AGENTS/`: workspaces ejecutables KORA.
- `scripts/`: CLI oficial y utilitarios auxiliares. La frontera operativa esta documentada en `scripts/README.md`.

Ademas, el repo opera sobre un pipeline de transformacion de artefactos:

- `OPERATIONS/inbox/`: bandeja de entrada operacional local.
- `OPERATIONS/source/`: insumos fuente aun no publicados.
- `OPERATIONS/drafts/`: artefactos transformados en prepublicacion.
- `KNOWLEDGE/`: conocimiento publicado.
- `OPERATIONS/build/`: evidencia tecnica de corridas; no forma parte de la base de conocimiento.

La Formal Layer oficial vive en `KNOWLEDGE/kora/categorical-foundations/`. El corpus `KNOWLEDGE/fxsl/cat/` permanece como material auxiliar y solo entra a la ley operativa por absorcion formal explicita.

## Arquitectura

```text
kora/
  specs/                        constitucion y specs derivadas
  KNOWLEDGE/                    KBs por namespace
    kora/categorical-foundations/   formal layer oficial (00-08)
    fxsl/cat/                       corpus categorial auxiliar
  AGENTS/                       workspaces de agentes por namespace
  catalog/                      vista materializada del grafo de artefactos
  docs/                         capa documental auxiliar (ver docs/README.md)
    generated/                 salidas vivas generadas por la CLI
    plans/                     planes, blueprints y handoffs
    reports/                   evidencia y reportes de corridas
  schemas/                      contratos JSON para bootstrap y config
  scripts/                      CLI oficial + soporte acotado + legacy
  OPERATIONS/                   superficies operacionales locales no portables
    inbox/                      cola operacional de ingesta
    source/                     insumos fuente
    drafts/                     prepublicacion
    build/                      evidencia tecnica de procesos
  KNOWLEDGE/                    conocimiento publicado
```

## Pipeline Operativo

El ciclo normal de incorporacion de artefactos es:

```text
OPERATIONS/inbox/ -> OPERATIONS/source/ -> OPERATIONS/drafts/ -> KNOWLEDGE/
                                         \-> OPERATIONS/build/   (evidencia tecnica paralela)
```

Semantica de cada etapa:

- `OPERATIONS/inbox/`: activa trabajo pendiente o registra una corrida operacional.
- `OPERATIONS/source/`: conserva materia prima o insumo semiestructurado.
- `OPERATIONS/drafts/`: contiene artefactos ya transformados pero aun no promovidos.
- `KNOWLEDGE/`: contiene artefactos publicados y catalogables.
- `OPERATIONS/build/`: guarda locks, projections, reports y evidence; queda fuera de `index`, `graph` y `health` por diseno.

`OPERATIONS/` es local-only: queda fuera del clone portable de KORA y se excluye via `.gitignore`.

## Gobernanza

La precedencia normativa es:

1. `specs/gobernanza.md`
2. `specs/spec-md.md` y `specs/md-spec.md`
3. `specs/agent-spec-md.md`, `specs/skill-spec-md.md`, `specs/runtime-spec-md.md`, `specs/swarm-spec-md.md`
4. extensiones de namespace

Reglas clave del nuevo regimen:

- `Traces to:` solo puede apuntar a `KNOWLEDGE/kora/categorical-foundations/`.
- `Rationale:` absorbe apoyo no normativo o pragmatica operativa.
- `TOOLS.md` declara interfaz semantica.
- `config.json.tools.allow` debe coincidir exactamente con esa interfaz.
- `config.json.runtime_capabilities` contiene permisos crudos del runtime.
- el catalogo no es source of truth; es una vista derivada del filesystem y sus manifests.

## Rol De Docs

`docs/` no es fuente canonica del sistema. Su rol es documental:

- `docs/generated/` contiene artefactos derivados y regenerables.
- `docs/plans/` contiene planes, blueprints y handoffs de trabajo.
- `docs/reports/` contiene reportes de corridas o evidencia historica.

La convencion completa vive en [`docs/README.md`](docs/README.md).

## Valor De Directorios Base

Estos directorios no cumplen el mismo papel. Su valor dentro del repo es distinto:

- `specs/`: constitucion operativa de KORA. Aqui vive la ley del sistema: precedencia, grammar, agent spec, skill spec, runtime spec y swarm spec. Si otro artefacto contradice `specs/`, manda `specs/`.
- `catalog/`: indice materializado del repo. Su valor es operativo: resolver URNs, alimentar stats, graph, health y docs generadas. Es critico para observabilidad y tooling, pero sigue siendo derivado del filesystem y sus manifests.
- `schemas/`: contratos mecanicos minimos para bootstrap y config. Su valor es de enforcement estructural: permiten validar forma, envelope y campos obligatorios antes de entrar a validaciones semanticas mas profundas.
- `scripts/`: toolchain ejecutable del monorepo. Su valor es convertir la ley y el filesystem en operaciones reales: indexar, resolver, validar, auditar, generar docs e intake. La convencion de su superficie soportada vive en `scripts/README.md`.
- `tests/`: verificador ejecutable del sistema. Su valor es institucionalizar supuestos y detectar drift, regresiones o falsos verdes del tooling. Si `specs/` define la ley, `tests/` verifica que la implementacion siga obedeciendola.

Lectura rapida:

- `specs/` define
- `schemas/` restringe
- `scripts/` opera
- `catalog/` indexa
- `tests/` verifica
- `docs/` explica

## Comandos

```bash
python3 scripts/kora index
python3 scripts/kora resolve "urn:kora:kb:agent-spec-md"
python3 scripts/kora health --strict
python3 scripts/kora validate --profile strict
python3 scripts/kora stats --json
python3 scripts/kora graph --json
python3 scripts/kora migrate --profile transitional
python3 scripts/kora sync-docs
python3 scripts/kora intake
```

## Flujo Recomendado

Despues de cambios estructurales:

1. `python3 scripts/kora migrate --profile transitional`
2. `python3 scripts/kora index`
3. `python3 scripts/kora health --strict`
4. `python3 scripts/kora validate --profile strict`
5. `python3 scripts/kora sync-docs`

## Metricas Vivas

No mantengas conteos a mano. Las metricas actuales se generan desde el catalogo vivo:

- [`docs/generated/repo-stats.md`](docs/generated/repo-stats.md)
- [`docs/generated/repo-stats.json`](docs/generated/repo-stats.json)
- [`docs/generated/repo-graph.json`](docs/generated/repo-graph.json)
- [`docs/generated/operating-core-contracts.json`](docs/generated/operating-core-contracts.json)
- [`docs/generated/operating-core-contracts.md`](docs/generated/operating-core-contracts.md)
- [`docs/generated/fxsl-cat-ledger.json`](docs/generated/fxsl-cat-ledger.json)
- [`docs/generated/fxsl-cat-ledger.md`](docs/generated/fxsl-cat-ledger.md)

Regeneracion:

```bash
python3 scripts/kora index
python3 scripts/kora sync-docs
```

## Pruebas

La suite minima del auditor categorial vive en `tests/` y se ejecuta con:

```bash
python3 -m unittest discover -s tests
```

## Licencia

CC-BY-4.0
