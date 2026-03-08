# KORA

Monorepo de especificaciones, conocimiento y workspaces de agentes gobernados por una capa formal categorial y una toolchain ejecutable.

## Que Es

KORA organiza el ecosistema en cuatro estratos:

- `specs/`: ley operativa del sistema.
- `knowledge/`: artefactos descriptivos KORA/MD.
- `agents/`: workspaces ejecutables KORA.
- `scripts/`: CLI oficial para indexar, validar, migrar y auditar.

La Formal Layer oficial vive en `knowledge/kora/categorical-foundations/`. El corpus `knowledge/fxsl/cat/` permanece como material auxiliar y solo entra a la ley operativa por absorcion formal explicita.

## Arquitectura

```text
kora/
  specs/                        constitucion y specs derivadas
  knowledge/                    KBs por namespace
    kora/categorical-foundations/   formal layer oficial (00-08)
    fxsl/cat/                       corpus categorial auxiliar
  agents/                       workspaces de agentes por namespace
  catalog/                      vista materializada del grafo de artefactos
  docs/generated/               salidas vivas generadas por la CLI
  schemas/                      contratos JSON para bootstrap y config
  scripts/                      CLI oficial
```

## Gobernanza

La precedencia normativa es:

1. `specs/gobernanza.md`
2. `specs/spec-md.md` y `specs/md-spec.md`
3. `specs/agent-spec-md.md`, `specs/skill-spec-md.md`, `specs/runtime-spec-md.md`, `specs/swarm-spec-md.md`
4. extensiones de namespace

Reglas clave del nuevo regimen:

- `Traces to:` solo puede apuntar a `knowledge/kora/categorical-foundations/`.
- `Rationale:` absorbe apoyo no normativo o pragmatica operativa.
- `TOOLS.md` declara interfaz semantica.
- `config.json.tools.allow` debe coincidir exactamente con esa interfaz.
- `config.json.runtime_capabilities` contiene permisos crudos del runtime.
- el catalogo no es source of truth; es una vista derivada del filesystem y sus manifests.

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
