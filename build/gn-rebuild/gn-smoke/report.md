# GN Rebuild Report gn-smoke

## Boundary
- build/ queda fuera de index, graph y health por diseno; su coherencia se gobierna por esta suite y por la semantica de evidence.
- drafts/gn representa artefactos no promovidos; su evidencia usa catalog_state `draft_unindexed` hasta cutover.

## Structural Diff
- Added: 0
- Removed: 0
- Changed: 78

## Review Gates
- none

## Unused Frozen Sources
- none

## Missing Targets
- none

## Intentional Non-Equivalence
- gn-cqs-master.md: El derivado MD representa solo el scope declarado de CQs y no reemplaza la fuente ontologica completa.
- gobernanza/omega-ipr-gestion-fusion.md: El derivado MD resume objetos Ω, mecanismos, dictámenes y actores sin reemplazar la ontología formal completa.
- gobernanza/organigrama.md: El derivado MD prioriza la estructura funcional del KODA y usa la TTL organizacional como soporte resumido del alcance declarado.
- gobernanza/plan-potenciamiento-dgi.md: El derivado MD toma el plan DGI como fuente principal y resume Meyer/Lean6 como dependencias explícitas dentro del alcance declarado.
