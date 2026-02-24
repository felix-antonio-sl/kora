---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:arquitecto-sistemas-informacion-cm-is-artifact-generator:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Producir artefactos de IS desde modelos de datos y funciones. Seleccionar formato, generar artefacto concreto, validar consistencia.

## Input/Output

- **Input:** Modelo datos, funciones IS, flujos desde S-ARTIFACT-GENERATION
- **Output:** Artefactos concretos en formato seleccionado

## Procedimiento

1. Seleccionar formato(s) de salida segun necesidad
2. Aplicar funtor de traduccion modelo → formato target
3. Mantener trazabilidad con modelo fuente
4. Validar consistencia entre artefactos generados

### Formatos Soportados

| Formato | Extension | Template |
|---------|-----------|----------|
| ERD (Mermaid) | .md | erDiagram |
| PostgreSQL DDL | .sql | CREATE TABLE |
| MySQL DDL | .sql | CREATE TABLE |
| GraphQL SDL | .graphql | type definitions |
| JSON Schema | .json | object schema |
| OpenAPI 3.x | .yaml | paths + components |
| Prisma Schema | .prisma | model definitions |
| Data Flow Diagram | .md | flow description |
| Work System Snapshot | .md | WS elements |
| Migration Scripts | .sql | ALTER/CREATE |

## Signature Output

```
## Artefacto: {formato}
### Metadata
- Modelo fuente: {referencia categorica}
- Funtor: {modelo} → {target}

### Contenido
{artefacto generado en formato target}

### Trazabilidad
| Entidad | Obj Categorico | Target Element |
|---------|---------------|----------------|
```
