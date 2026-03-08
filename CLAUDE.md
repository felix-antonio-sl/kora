# CLAUDE.md

Guia operativa para agentes que trabajen dentro de este repositorio.

## Que Es Este Repo

KORA es un monorepo gobernado por specs y soportado por una capa formal categorial. No es un proyecto de aplicacion tradicional: el activo principal es la consistencia entre conocimiento, specs, workspaces y toolchain.

## Source Of Truth

- El source of truth es el filesystem con manifests validos.
- `catalog/catalog_master_kora.yml` es una vista materializada generada por `python3 scripts/kora index`.
- No escribas conteos a mano en docs publicas. Usa `python3 scripts/kora sync-docs`.

## Precedencia

1. `specs/gobernanza.md`
2. `specs/spec-md.md` y `specs/md-spec.md`
3. `specs/agent-spec-md.md`, `specs/skill-spec-md.md`, `specs/runtime-spec-md.md`, `specs/swarm-spec-md.md`
4. extensiones de namespace

## Formal Layer

- La unica Formal Layer oficial es `knowledge/kora/categorical-foundations/`.
- `knowledge/fxsl/cat/` es corpus auxiliar.
- `Traces to:` solo puede apuntar a documentos de la Formal Layer oficial.
- Si una idea viene de `fxsl/cat` y no ha sido absorbida formalmente, usala como `Rationale:`, no como traza oficial.

## Modelo Del Workspace

Todo workspace agente KORA se compone de:

- `AGENTS.md`: behavior
- `TOOLS.md`: interfaz semantica declarada
- `SOUL.md` y `USER.md`: estado/contexto
- `config.json`: security + runtime envelope
- `skills/`: capacidades lazy-load

Convenciones duras:

- `TOOLS.md` y `config.json.tools.allow` deben coincidir exactamente.
- `config.json.runtime_capabilities` contiene permisos crudos del runtime.
- `sub_agents.max_concurrent` es ausente o `>= 1`; nunca `0`.
- los skills usan identidad `urn:{namespace}:skill:{id}:{version}`.
- la grammar canonica de skill degenerado es `Proposito`, `Input/Output`, `Procedimiento`, `Signature Output`.

## Comandos Que Debes Usar

```bash
python3 scripts/kora index
python3 scripts/kora resolve "urn:kora:kb:agent-spec-md"
python3 scripts/kora health --strict
python3 scripts/kora validate --profile strict
python3 scripts/kora stats --json
python3 scripts/kora graph --json
python3 scripts/kora migrate --profile transitional
python3 scripts/kora sync-docs
python3 -m unittest discover -s tests
```

## Secuencia De Trabajo

Cuando cambies specs, workspaces o knowledge estructural:

1. aplica cambios
2. `python3 scripts/kora migrate --profile transitional` si hubo deuda legacy
3. `python3 scripts/kora index`
4. `python3 scripts/kora health --strict`
5. `python3 scripts/kora validate --profile strict`
6. `python3 scripts/kora sync-docs`
7. `python3 -m unittest discover -s tests`

## Notas Practicas

- no tomes `README.md` o docs antiguos como autoridad si contradicen la CLI o las specs vigentes.
- usa `python3 scripts/kora graph --json` cuando necesites auditar nodos y morfismos del repo, no inferirlos a mano.
- usa `docs/generated/operating-core-contracts.*` para ver el contrato operativo extraido del nucleo sin releer workspace por workspace.
- si agregas una nueva regla absoluta, debe tener enforcement razonable o bajar a `DEBERIA`.
- si corriges `fxsl/cat`, hazlo para eliminar ruido auditivo o preparar absorcion formal, no para darle autoridad normativa directa.
