---
_manifest:
  urn: urn:kora:skill:guardian-spec-classifier:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-SPEC-CLASSIFIER

## Proposito
Clasificar solicitudes relacionadas con specs fundacionales e invariantes estructurales.

## Input/Output
- **Input:** Solicitud del operador y contexto de la sesion.
- **Output:** Clasificacion `{capacidad, riesgo, target}`.

## Procedimiento
1. Determinar si la solicitud es consulta, auditoria o proteccion.
2. Estimar riesgo sobre invariantes.
3. Proponer target fundacional relevante.

## Signature Output
```yaml
clasificacion:
  capacidad: "CONSULTAR"
  riesgo: "medio"
  target: "agent-spec"
```
