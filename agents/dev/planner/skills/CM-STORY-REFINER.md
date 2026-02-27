---
_manifest:
  urn: "urn:dev:skill:planner-story-refiner:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-STORY-REFINER

## Proposito
Refina una historia individual: verifica los 5 elementos, genera/mejora criterios de aceptacion, clasifica complejidad y riesgo, estima valor, identifica dependencias.

## Procedimiento
1. Leer historia. Verificar que tiene los 5 elementos.
2. Si falta Who/What/Why: elicitar con preguntas al PO.
3. Criterios de aceptacion:
   - Generar 3-7 condiciones testables.
   - Cada AC DEBE ser verificable automaticamente (derivable a test).
   - Formato: "DADO [contexto], CUANDO [accion], ENTONCES [resultado esperado]".
4. Clasificar complejidad:
   - simple: CRUD basico, cambio de estilo, config. → Tier 1-2.
   - estandar: feature con logica, integracion con API. → Tier 2.
   - complejo: multi-componente, migracion, arquitectura. → Tier 3.
   - critico: seguridad, datos financieros, irreversible. → Tier 3-4.
5. Clasificar riesgo:
   - lectura: no modifica estado. → autonomo.
   - escritura: modifica estado recuperable. → autonomo con eval.
   - destructiva: modifica estado irreversible. → requiere aprobacion humana.
6. Estimar valor de negocio (1-5) con justificacion.
7. Identificar dependencias con otras historias.
8. Calcular tier de modelo recomendado segun complejidad.
9. Presentar historia refinada completa.

## Output
Historia refinada: {who_what_why, criterios_aceptacion[], valor, complejidad, riesgo, dependencias[], tier_modelo}.
