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
- **Input:** solicitud: string, contexto_sesion: ContextSummary | null
- **Output:** SpecClassification (ver Signature Output)

## Procedimiento
1. Determinar si la solicitud es governance, validation o end.
2. Estimar riesgo sobre invariantes.
3. Proponer target fundacional relevante.

## Signature Output
```yaml
clasificacion:
  capacidad: "GOVERNANCE"
  riesgo: "medio"
  target: "agent-spec-md"
```
