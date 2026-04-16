# Config notes — steipe antiguo / OPModel

## Runtime legacy observado
- Contenedor: `kora-steipete`
- Estado original al inspeccionar: detenido
- Workspace legacy: `/srv/kora/workspaces/steipete/agents/steipete`
- State dir en contenedor: volumen Docker `compose-steipete_kora-steipete-data` montado en `/home/node/.openclaw`

## Mounts relevantes
- `/srv/kora/workspaces/steipete/agents/steipete` -> `/home/node/.openclaw/workspace`
- `/home/felix/projects/opmodel` -> `/home/node/projects/opmodel`
- `/home/felix/kora` -> `/home/node/repos/kora`
- `/srv/kora/shared/steipete` -> `/home/node/shared/steipete`

## Implicancias
- El repo `opmodel` era fuente viva compartida con el host, no artefacto exclusivo del contenedor legacy.
- Lo específico del agente viejo estaba en su `MEMORY.md`, `memory/*.md` y `output/opmodel/`.
- Para el steipete nuevo, la ruta host canónica es `/home/felix/projects/opmodel`.

## Hallazgos operativos
- La KB OPM/ISO no estaba montada dentro del contenedor viejo en la ruta esperada por el agente (`/home/node/knowledge/`), aunque el operador había declarado `/home/felix/kora/KNOWLEDGE/fxsl/opm` como fuente de verdad.
- El proyecto usaba `bun`, pero el contenedor viejo no tenía `bun` instalado; esto explicaba fricción en algunas operaciones directas.
- Para evitar conflicto con el bot productivo, el contenedor legacy fue arrancado solo para inspección y luego vuelto a detener.
