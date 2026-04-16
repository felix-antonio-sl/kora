# OPModel — resumen destilado desde steipete legacy

## Fuente
Destilado de:
- `/srv/kora/workspaces/steipete/agents/steipete/MEMORY.md`
- `/srv/kora/workspaces/steipete/agents/steipete/memory/2026-03-23.md`
- `/srv/kora/workspaces/steipete/agents/steipete/memory/2026-03-24.md`
- `/srv/kora/workspaces/steipete/agents/steipete/memory/2026-03-25.md`
- `/srv/kora/workspaces/steipete/agents/steipete/memory/2026-03-26.md`

## Estado legado relevante
- Proyecto activo del agente viejo: `opmodel`
- Ruta histórica en contenedor: `/home/node/projects/opmodel`
- Ruta host actual equivalente: `/home/felix/projects/opmodel`
- Web histórica: `https://opmodel.sanixai.com`
- El repo estaba montado directo desde el host; no era conocimiento exclusivo del contenedor.

## Hitos preservados
### Sesión 17 (2026-03-24)
- HODOM legacy: 48 things, 34 states, 82 links, 84 appearances, 6 OPDs.
- Trabajo fuerte en cobertura OPL, ghost positioning, aggregation OPL, exception/invocation semantics.
- Se confirmaron 14 commits atómicos de corrección y enriquecimiento sobre HODOM.

### Sesión 19 (2026-03-24)
- 880 tests / 59 test files.
- Avances: OPL bilingüe, exportMarkdown, modelStats, Monte Carlo sim, clickable OPL, Settings panel, zoom controls, fit-to-content, event triggers, exception handling, assertion verification, duplicate visual, Ctrl+A/D.
- Pendiente estructural identificado: la KB OPM no estaba montada dentro del contenedor legacy; el operador había indicado `/home/felix/kora/KNOWLEDGE/fxsl/opm` como fuente de verdad del dominio.

### Sesión 25 (2026-03-25)
- Se creó `scripts/build-hodom-v2.ts`.
- Fixture `hodom-v2.opmodel` generado y expuesto también en `packages/web/public/`.
- Commit clave: `8d4e02e` — HODOM V2 reconstruido desde metodología OPM + normativa.
- EV-AMS canónico completado con commit `3964894`.
- El operador pidió progreso autónomo continuo con tests verdes y commits atómicos.

### Sesión 20 / 26 (2026-03-26)
- 1,042 tests / 70 files / 16 commits en la sesión extendida.
- `CORE-VISUAL.md` documentó el visual core 360°.
- Cobertura ISO declarada como completa sobre things, states, links, modifiers, forks y OPL sentence types.
- Se generó `informe-gaps-plan-implementacion.md` como baseline de roadmap.

## Decisiones técnicas legadas útiles
- `OpdCanvas` era el hotspot principal de complejidad; se inició descomposición modular.
- Edge routing con curvas Bézier y offset paralelo fue una mejora prioritaria y ya implementada en el repo vivo.
- `opmodel` se trataba como producto con “core visual reusable”, no solo demo puntual.
- Fixtures HODOM/EV-AMS eran usados como verificación práctica del motor visual y metodológico.
- Los workers ACP eran poco confiables para este proyecto; el trabajo directo sobre repo fue más efectivo.

## Gaps/roadmap que sí conviene conservar
- Export PDF
- Zoom semántico
- Minimap/overview
- Copy/paste cross-OPD
- Refactor de `api.ts`
- Waypoints editables en links
- Annotation layer
- Integración más profunda NL → OPM

## Reglas de uso para el nuevo steipete
- La fuente primaria de producto es el repo vivo `/home/felix/projects/opmodel`.
- Esta carpeta legacy sirve para contexto, trazabilidad y memoria operativa, no para reemplazar el repo.
- Toda decisión nueva debe validar contra el estado actual del repo, no contra métricas congeladas del legado.
