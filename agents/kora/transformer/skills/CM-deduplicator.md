---
_manifest:
  urn: "urn:kora:agent-bootstrap:transformer-cm-deduplicator:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Eliminar redundancia en artefacto KODA mediante definiciones unicas y sistema de referencias (Ref intensivo).

## Input/Output

- **Input:** Artefacto KODA preliminar con keyword markup desde S-TELEGRAFIZER
- **Output:** Artefacto KODA deduplicado con IDs unicos y Ref para cada concepto repetido

## Procedimiento

1. Escanear artefacto buscando conceptos repetidos
2. Para cada concepto que aparece mas de una vez:
   - Crear definicion con ID unico en ubicacion canonica
   - Reemplazar TODAS las ocurrencias con Ref: ID
3. Regla intensiva: Si un concepto aparece mas de una vez, DEBE ser definido y referenciado. Sin excepciones.
4. Verificar integridad: todos los Ref apuntan a ID existente
5. Verificar unicidad: no hay IDs duplicados
6. Verificar completitud: ningun concepto repetido sin Ref

## Signature Output

```
**Deduplicacion completada**:
- Conceptos definidos: [N]
- Referencias creadas: [M]
- IDs unicos: [verificado]
- Refs validos: [verificado]
```
