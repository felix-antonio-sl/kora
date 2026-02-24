---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:ontologista-gist-cm-auditor-gist:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Detectar anti-patrones y verificar conformidad con Gist. Generar reporte de auditoria con recomendaciones.

## Input/Output

- **Input:** Modelo/ontologia del usuario (Turtle, descripcion, diagrama)
- **Output:** Reporte de conformidad con anti-patrones detectados, checks de conformidad, recomendaciones

## Procedimiento

1. Detectar anti-patrones:
   - Namespace Squatting: definir terminos en gist: namespace
   - Class Proliferation: crear clases donde Category basta
   - Direct Datatype for Measurements: usar xsd:decimal sin Magnitude/UoM
   - Missing Temporal Context: relaciones sin considerar temporalidad
   - Conflating Namespace with Ontology IRI
   - Hardcoded Address Components: parsear direcciones en multiples propiedades

2. Ejecutar checks de conformidad:
   - ¿Usa gist: namespace solo para importar, no para definir nuevos terminos?
   - ¿Las extensiones estan en namespace propio?
   - ¿Aplica Category pattern para taxonomias flexibles?
   - ¿Usa Magnitude pattern para valores medibles?
   - ¿Considera TemporalRelation para relaciones con contexto temporal?
   - ¿Las clases disjoint estan correctamente declaradas?

3. Generar reporte con severidad por hallazgo
4. Proponer correcciones siguiendo patrones Gist

## Signature Output

```
ANTI_PATRONES: [{nombre, severidad, descripcion, correccion}]
CONFORMIDAD: [{check, resultado: PASS|FAIL, nota}]
RECOMENDACIONES: [{accion, patron_gist, ejemplo}]
```
