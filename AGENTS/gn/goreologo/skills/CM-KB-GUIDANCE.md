---
_manifest:
  urn: urn:gn:skill:goreologo-kb-guidance:1.0.0
  type: lazy_load_endofunctor
---

# CM-KB-GUIDANCE

## Proposito
Identificar y priorizar las fuentes KB del repositorio KORA relevantes para una consulta sobre GOREs, orientando la busqueda antes de formular la respuesta.

## Input/Output
- **Input:** Tema de consulta sobre GOREs a resolver
- **Output:** Lista priorizada de KB con URNs resueltos, razon de relevancia y gaps de cobertura

## Procedimiento
1. Analizar el tema y mapear a areas del routing map de TOOLS.md (kb_route):
   - Marco legal GORE → area: legal, juridico (LOC, ley presupuestos, CGR, dictamenes)
   - Gestion/inversiones → area: presupuesto, ipr, gestion (presupuesto, rendiciones, IPR, guias fondos)
   - Gobernanza Nuble → area: intro, estrategia (ERD, organigrama, indicadores, vision)
   - Procesos operativos → area: procesos, operacional (BPMN, manuales, compras, RRHH)
   - Guias fondos → area: guias (FNDR, FRIL, FRPD, circular 33, IDI)
   - TDE/digital → area: procesos (TDE, Ley 21.180)
   - Comunicaciones → area: comunicaciones
   - Fuentes consolidadas → area: ssot (SSOT por dominio, indice maestro)
2. Resolver URNs de los KB priorizados via catalog_resolve.
3. Ordenar KB por relevancia directa al tema consultado. Priorizar SSOTs como fuente consolidada cuando exista uno para el dominio consultado.
4. Indicar si el tema requiere cruzar multiples KB (consulta multidimensional).
5. Declarar cuando el tema excede cobertura KB: distinguir [dato KB] de [interpretacion].

## Signature Output
Lista priorizada de KB: [URN] + [subfondo o instrumento cubierto] + [razon de relevancia]. Nota de cruce multidimensional si aplica. Indicacion de gaps de cobertura KB si existen.
