# 2026-03-28 — Ingesta canónica de OPModel legado

- Se inspeccionó el runtime legado `kora-steipete` para extraer conocimiento OPModel útil sin arrastrar drift de infraestructura.
- Hallazgo clave: el repo `opmodel` no era conocimiento exclusivo del contenedor; estaba bind-mounteado al host y su ruta actual canónica es `/home/felix/projects/opmodel`.
- El conocimiento verdaderamente específico del steipe antiguo estaba en su memoria operativa y en `output/opmodel/informe-gaps-plan-implementacion.md`.
- Se preservó ese material en `reference/opmodel/legacy-steipete/` dentro del workspace del steipete productivo.
- Se creó una skill local `opmodel-knowledge` para que el agente nuevo consulte primero el repo vivo y use el legado como contexto/refuerzo, no como fuente ciega.
- Para teoría OPM/ISO, la fuente de verdad sigue siendo `/home/felix/kora/KNOWLEDGE/fxsl/opm/`.
