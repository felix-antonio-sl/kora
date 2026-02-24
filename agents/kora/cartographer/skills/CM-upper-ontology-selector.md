---
_manifest:
  urn: "urn:kora:agent-bootstrap:cartographer-cm-upper-ontology-selector:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Seleccionar upper ontology apropiada como marco conceptual unificador para el modelo de datos.

## Input/Output

- **Input:** Mapa completo del dominio (clasificacion, grafo, equivalencias) desde S-ELEVAR
- **Output:** Upper ontology seleccionada con justificacion y patrones disponibles

## Procedimiento

1. Evaluar opciones disponibles:
   - **Gist 14.0:** Dominio empresarial/gubernamental. Patterns: Category, Magnitude, Event, Organization, Agreement, Content. Recomendado si ya existe en fuentes.
   - **Schema.org:** Web semantica, SEO, datos publicos. Patterns: Thing, Organization, Event, Place, CreativeWork.
   - **Custom:** Dominio muy especifico sin upper ontology aplicable. Riesgo: alto costo, propenso a errores.
   - **Hybrid:** Upper ontology base + extensiones de dominio. Recomendado por defecto.
2. Evaluar fit con dominio mapeado:
   - ¿Patrones del dominio alinean con patrones de la ontologia?
   - ¿Cubre >80% de conceptos?
   - ¿Extensiones necesarias son minimas?
3. Recomendar opcion con justificacion
4. Listar patrones disponibles de la ontologia seleccionada

## Signature Output

```
**Upper Ontology**: [Gist 14.0 | Schema.org | Custom | Hybrid]
- Justificacion: [razon]
- Fit con dominio: [%]
- Patrones disponibles: [lista]
- Extensiones necesarias: [lista o NINGUNA]
```
