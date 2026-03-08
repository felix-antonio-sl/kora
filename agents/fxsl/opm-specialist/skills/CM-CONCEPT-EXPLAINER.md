---
_manifest:
  urn: "urn:fxsl:skill:opm-specialist-concept-explainer:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Explicar conceptos OPM con precision formal (ISO 19450) y claridad pedagogica, conectando cada concepto con el ecosistema OPM.

## Input/Output

- **Input:** concepto OPM a explicar (string), nivel de detalle (basico|intermedio|avanzado)
- **Output:** explicacion estructurada con definicion, OPL, ejemplo, relaciones

## Procedimiento

1. RESOLVER concepto en KB via kb_route → catalog_resolve
2. EXTRAER definicion formal ISO 19450
3. ESTRUCTURAR explicacion:
   a. **Definicion formal** — que es, segun ISO 19450
   b. **Representacion OPD** — como se ve graficamente (descripcion textual)
   c. **Sintaxis OPL** — oracion OPL correspondiente con grammar correcta
   d. **Ejemplo concreto** — aplicado a un sistema real
   e. **Relacion con otros conceptos** — como se conecta con el ecosistema OPM
   f. **Errores comunes** — confusiones frecuentes a evitar
4. ADAPTAR profundidad segun nivel solicitado:
   - basico: definicion + ejemplo
   - intermedio: + OPL + relaciones
   - avanzado: + ISO formal + errores comunes + variantes (state-specified, control-modified)
5. VERIFICAR OPM_ACCURACY antes de entregar

## Signature Output

Explicacion en Markdown con secciones: Definicion, OPL, Ejemplo, Relaciones.
