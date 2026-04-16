# OPModel legacy extraction — steipete antiguo → steipete productivo

## Procedencia
- Runtime legado inspeccionado: `kora-steipete`
- Workspace legado: `/srv/kora/workspaces/steipete/agents/steipete`
- Repo vivo montado por el legado: `/home/felix/projects/opmodel`
- Fecha de extracción: 2026-03-28

## Qué se preservó aquí
- `informe-gaps-plan-implementacion.md` — informe operativo generado por el steipe antiguo sobre gaps, arquitectura y roadmap de implementación.
- `legacy-session-summary.md` — destilado de memoria operativa, hitos, commits y decisiones técnicas relevantes.

## Qué NO se duplicó aquí
- El repo `opmodel` completo no se copió porque ya existe como fuente viva en `/home/felix/projects/opmodel`.
- Los `.opmodel` fixtures, sesiones y docs del repo siguen siendo la fuente primaria de trabajo actual.

## Uso canónico en el nuevo steipete
1. Leer primero `legacy-session-summary.md` para orientación.
2. Consultar después `informe-gaps-plan-implementacion.md` para roadmap/gaps detallados.
3. Contrastar siempre contra el repo vivo en `/home/felix/projects/opmodel`.
4. Para teoría OPM/ISO, usar `/home/felix/kora/KNOWLEDGE/fxsl/opm/`.

## Nota de migración
En el legado, `opmodel` estaba montado como `/home/node/projects/opmodel` dentro del contenedor. En el host actual, la ruta canónica es `/home/felix/projects/opmodel`.
