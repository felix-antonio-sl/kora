---
_manifest:
  urn: "urn:gn:skill:dgi-virtual-kb-guidance:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-KB-GUIDANCE

## Proposito
Identificar y priorizar las fuentes KB relevantes para una consulta DGI, orientando la busqueda de informacion antes de formular una respuesta.

## I/O

- **Input:** Tema de consulta DGI a resolver
- **Output:** Lista priorizada de KB con URNs resueltos y razon de relevancia

## Procedimiento
1. Analizar el tema de la consulta e identificar el dominio principal (gestion, procesos, TDE, legal, estructura).
2. Mapear el tema a los KB disponibles segun routing:
   - Procesos/BPMN/Lean → knowledge/gn/bpmn/, knowledge/mgmt/
   - Estructura/Meyer → knowledge/mgmt/meyer-org-structure.md
   - TDE/digital → knowledge/tde/, knowledge/gov/
   - Marco legal GORE → knowledge/gn/normativa/, knowledge/legal/
   - Gestion DGI/interna → knowledge/gn/gobernanza/, knowledge/gn/manuales/
   - Presupuesto/rendiciones → knowledge/gn/gestion/
3. Resolver URNs de los KB priorizados via CM-CATALOG-RESOLVER.
4. Indicar al agente cuales KB consultar y en que orden de prioridad.
5. Si ningun KB cubre el tema → declarar incertidumbre y ofrecer orientacion general desde conocimiento DGI.

## Signature Output
Lista priorizada de KB a consultar: [URN] + [razon de relevancia]. Path resueltos via catalog. Nota si el tema excede cobertura KB disponible.
