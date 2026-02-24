---
_manifest:
  urn: "urn:gn:skill:goreologo-kb-guidance:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-KB-GUIDANCE

## Proposito
Identificar y priorizar las fuentes KB del repositorio KORA relevantes para una consulta sobre GOREs, orientando la busqueda antes de formular la respuesta.

## Procedimiento
1. Analizar el tema y mapear a dominios KB disponibles:
   - Marco legal GORE → knowledge/gn/normativa/ (LOC, ley presupuestos, CGR)
   - Gestion/inversiones → knowledge/gn/gestion/ (presupuesto, rendiciones, IPR)
   - Gobernanza Nuble → knowledge/gn/gobernanza/ (ERD, organigrama, indicadores)
   - Procesos operativos → knowledge/gn/bpmn/, knowledge/gn/manuales/
   - Guias fondos → knowledge/gn/guias/ (FNDR, FRIL, FRPD, circular 33)
   - TDE/digital → knowledge/tde/, knowledge/gov/
   - Normativa legal transversal → knowledge/legal/
2. Resolver URNs de los KB priorizados via catalog_resolve.
3. Ordenar KB por relevancia directa al tema consultado.
4. Indicar si el tema requiere cruzar multiples KB (consulta multidimensional).
5. Declarar cuando el tema excede cobertura KB: distinguir [dato KB] de [interpretacion].

## Output
Lista priorizada de KB: [URN] + [subfondo o instrumento cubierto] + [razon de relevancia]. Nota de cruce multidimensional si aplica. Indicacion de gaps de cobertura KB si existen.
