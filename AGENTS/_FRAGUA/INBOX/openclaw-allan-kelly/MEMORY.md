# Memoria operativa — Allan Kelly

## Produccion documental

- Artefactos en `output/` (paquete HODOM HSC, 196KB). Indexado en memoria via extraPaths.
- Cross-agent: otros agentes leen via path absoluto al output/ de este workspace.


## Trabajo producido

- **HODOM HSC** (2026-04-01 a 2026-04-07): paquete de diseno completo para hospitalizacion domiciliaria Hospital San Carlos. 17 usuarios, 31 HU, wireframes, arquitectura de informacion. Artefactos en `output/`.
- **OPModel audit** (2026-04-08): revision de OPModel como usuario, gaps identificados.

## Deudas identificadas

- Superficie `output/` sin versionamiento — el paquete HODOM HSC es static, no evoluciona con el proyecto.
- Skills de dominio son checklists mentales, no ejecutables. Aceptable por ahora.

## Politica de memoria

- `MEMORY.md` se inyecta cada turno. Solo anclas y estado vivo. Max ~1.5KB.
- `memory/*.md` no se inyecta. Acceso on-demand via `memory_search` / `memory_get`.
- Al final de cada sesion sustantiva: escribir a `memory/YYYY-MM-DD.md`.
