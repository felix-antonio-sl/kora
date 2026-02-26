---
_manifest:
  urn: "urn:fxsl:skill:ontologista-gist-generador:1.0.0"
  type: "lazy_load_endofunctor"
---
## Proposito

Generar alternativas de modelado ontologico mediante variacion, combinacion, inversion y analogia, expandiendo el espacio de soluciones antes de colapsar a una decision.

## I/O

- **Input:** Modelo ontologico en curso, tensiones identificadas desde S-OPERACION
- **Output:** 3 alternativas de modelado con patron Gist, trade-offs y recomendacion

## Procedimiento
1. Variacion: proponer 2-3 variantes del modelo principal cambiando un parametro clave (granularidad, patron, jerarquia).
2. Combinacion: explorar si el dominio puede modelarse combinando 2 patrones Gist distintos (p.ej. TemporalRelation + Magnitude).
3. Inversion: cuestionar el modelo propuesto — que pasaria si la relacion fuera inversa, si la entidad fuera propiedad, o si se usara Category en vez de Class.
4. Analogia: buscar dominios similares ya modelados con Gist y adaptar su solucion al dominio actual.
5. Para cada alternativa: indicar trade-offs clave (complejidad, extensibilidad, conformidad Gist, costo de mantenimiento).
6. Presentar maximas 3 alternativas al usuario con recomendacion justificada.

## Signature Output

3 alternativas de modelado ontologico con: descripcion breve, patron Gist base, trade-offs clave [trade-off], recomendacion motivada. Formato: tabla Alternativa/Patron/Ventaja/Desventaja.
