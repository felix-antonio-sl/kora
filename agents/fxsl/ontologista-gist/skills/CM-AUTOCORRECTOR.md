---
_manifest:
  urn: "urn:fxsl:skill:ontologista-gist-autocorrector:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-AUTOCORRECTOR

## Proposito
Refinar un modelo ontologico a partir de criticas recibidas (CM-CRITICO o feedback de usuario), ajustando foco, complejidad, conformidad Gist y certeza declarada.

## Procedimiento
1. Foco: verificar que el modelo refinado responde exactamente lo que se pregunto. Eliminar elementos fuera de scope del problema original.
2. Complejidad: aplicar navaja de Occam ontologica — eliminar toda clase, propiedad o axioma que no agregue valor explicito al dominio. Preferir Category sobre Class cuando la formalizacion no es requerida.
3. Principios Gist: re-verificar las 4 reglas criticas:
   - Namespace propio para extensiones.
   - Patron Gist correcto para cada tipo de entidad.
   - No subclases de clases Gist sin justificacion.
   - Propiedades Gist usadas con su semantica correcta.
4. Certeza: marcar con [consolidado] las decisiones ontologicas validadas, [provisional] las que requieren mas informacion, [trade-off] las que implican compromiso explicito.
5. Producir version refinada del modelo con changelog de cambios respecto a version anterior.

## Output
Modelo ontologico refinado con changelog: lista de cambios aplicados (que se elimino, que se cambio, que se agrego) con justificacion. Etiquetas de certeza en cada decision clave. Listo para CM-CALIBRADOR.
