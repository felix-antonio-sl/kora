---
_manifest:
  urn: "urn:fxsl:skill:ontologista-gist-analizador:1.0.0"
  type: "lazy_load_endofunctor"
---
## Proposito

Analizar un dominio o problema de modelado ontologico en 4 dimensiones: estructura estatica, dinamica temporal, tensiones de diseno y busqueda de patrones Gist aplicables.

## I/O

- **Input:** Dominio o problema de modelado desde S-OPERACION
- **Output:** Analisis estructurado con entidades, tensiones, patrones Gist candidatos, decisiones pendientes

## Procedimiento
1. Estructura: identificar entidades candidatas, relaciones, atributos y jerarquias del dominio.
2. Dinamica: detectar relaciones temporales, ciclos de vida, estados y transiciones que requieren TemporalRelation o Event.
3. Tensiones: identificar tensiones de diseno presentes:
   - Class↔Category (taxonomia formal vs flexible)
   - TBox↔ABox (definicion vs instancia)
   - Extend↔Parallel (subclase Gist vs namespace propio)
   - Magnitude↔Literal (valor con UoM vs dato crudo)
4. Busqueda patrones: mapear cada entidad/relacion a clases y propiedades Gist 14.0 candidatas (Person, Organization, Event, Content, Category, Magnitude, Agreement, Commitment, Address).
5. Registrar decisiones pendientes con razon de la tension.

## Signature Output

Analisis estructurado: tabla Entidad/Clase-Gist-candidata/Tension-identificada. Lista de patrones Gist aplicables priorizados. Decisiones pendientes para CM-GENERADOR.
