---
_manifest:
  urn: "urn:kora:skill:cartographer-project-classifier:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-PROJECT-CLASSIFIER

## Proposito

Clasificar el estado y contexto de un proyecto de modelado de datos para determinar la fase de entrada al proceso ESCUCHAR→MAPEAR→ELEVAR→CRISTALIZAR.

## Procedimiento

1. Recibir descripcion del proyecto o artefactos disponibles del usuario
2. Clasificar estado del proyecto:
   - NEW_PROJECT: no hay inventario, se parte desde cero
   - HAS_INVENTORY: tiene lista de fuentes pero sin clasificacion ontologica
   - HAS_MAP: tiene clasificacion ontologica pero sin arquitectura de capas
   - HAS_ARCHITECTURE: tiene arquitectura pero sin schema finalizado
   - CONSULT: pregunta puntual sin proyecto activo
3. Identificar fuentes disponibles: YAML | TTL (ontologia) | MD | SQL | conversaciones/requisitos
4. Detectar dominio del proyecto: gobierno | finanzas | salud | educacion | generico
5. Identificar documento de autoridad si existe (MANIFESTO, spec, documento constitucion del sistema)
6. Recomendar fase de entrada y mantra correspondiente

## Output

Clasificacion del proyecto (estado + fase entrada + dominio + fuentes) + mantra de la fase recomendada + pregunta inicial para comenzar esa fase.
