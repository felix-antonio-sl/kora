---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:ingeniero-sistemas-composicional-cm-stakeholder-extractor:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Identificar y caracterizar stakeholders del sistema mediante analisis multidimensional. Producir mapa de stakeholders estructurado para validacion.

## Input/Output

- **Input:** Descripcion del sistema o dominio desde S-STAKEHOLDER-ANALYSIS
- **Output:** Mapa de stakeholders con tipo, necesidades y restricciones

## Procedimiento

1. Analizar dominio por 5 dimensiones:
   - BENEFICIARIOS: Quien obtiene valor del sistema?
   - OPERADORES: Quien opera el sistema directamente?
   - MANTENEDORES: Quien mantiene y evoluciona el sistema?
   - REGULADORES: Que normas/estandares aplican?
   - AFECTADOS: Quien es impactado indirectamente?
2. Para cada stakeholder: identificar necesidades, metas, restricciones
3. Clasificar por tipo y prioridad
4. Detectar conflictos potenciales entre stakeholders
5. Presentar mapa para validacion del usuario

## Signature Output

```
## Mapa de Stakeholders
| Stakeholder | Tipo | Necesidades | Restricciones |
|-------------|------|-------------|---------------|
| {nombre}    | {tipo} | {necesidades} | {restricciones} |
```
