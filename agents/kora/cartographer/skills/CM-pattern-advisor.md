---
_manifest:
  urn: "urn:kora:agent-bootstrap:cartographer-cm-pattern-advisor:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Recomendar patron de modelado apropiado para consultas puntuales de diseno de datos.

## Input/Output

- **Input:** Consulta de modelado desde S-CONSULTANT
- **Output:** Patron recomendado con ejemplo concreto aplicable

## Procedimiento

1. Clasificar consulta por tipo:
   - Taxonomia, clasificacion, tipos, estados → **Category Pattern (Gist):** category(scheme, code, label, parent_id)
   - Metricas, mediciones, KPIs, porcentajes → **Magnitude + Aspect Pattern (Gist):** magnitude(subject_type/id, aspect, value, unit)
   - Eventos, transacciones, auditoria, historico → **Event Pattern (Gist):** event(event_type, subject_type/id, occurred_at, data)
   - Relaciones temporales, vigencias, asignaciones → **Temporal Validity Pattern:** valid_from/valid_to con EXCLUDE constraint
2. Adaptar ejemplo al dominio del usuario
3. Explicar beneficio del patron vs alternativa naive
4. Ofrecer aplicar a proyecto si corresponde

## Signature Output

```
**Patron recomendado**: [nombre]
**Estructura**: [schema ejemplo]
**Beneficio**: [por que es mejor que alternativa naive]
**Aplicacion**: [como usarlo en tu dominio]
```
