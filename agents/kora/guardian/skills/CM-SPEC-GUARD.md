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
- **Input:** Solicitud, spec objetivo e impacto potencial identificado.
- **Output:** Respuesta con restricciones, riesgos y ruta de escalamiento.

## Procedimiento
1. Identificar el invariante o spec implicado.
2. Evaluar si la solicitud lo modifica, lo consulta o lo tensiona.
3. Responder con restricciones y ruta segura.
4. Escalar cuando el cambio quede fuera del dominio permitido.

## Signature Output
```yaml
guard_response:
  riesgo: "alto"
  restriccion_principal: "No modificar specs fundacionales desde este workspace"
  escalamiento: "kora/guardian"
```
