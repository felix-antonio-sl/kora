---
_manifest:
  urn: urn:kora:skill:guardian-spec-guard:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-SPEC-GUARD

## Proposito
Emitir criterio conservador para proteger specs fundacionales y sus invariantes.

## Input/Output
- **Input:** solicitud: string, spec_objetivo: string, impacto_potencial: string
- **Output:** GuardAssessment (ver Signature Output)

## Procedimiento
1. Identificar el invariante o spec implicado.
2. Evaluar si la solicitud lo modifica, lo consulta o lo tensiona.
3. Responder con restricciones, riesgo e invariantes afectados.
4. Marcar si el caso excede el dominio permitido sin codificar wiring ni transiciones.

## Signature Output
```yaml
guard_response:
  riesgo: "alto"
  restriccion_principal: "No introducir drift entre specs fundacionales vigentes"
  invariantes_afectados:
    - "precedencia_normativa"
  requiere_escalacion: true
```
