---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:ontologista-gist-cm-modelador-gist:1.0.0"
  type: "lazy_load_endofuntor"
---

## Proposito

Aplicar patrones Gist para modelar dominios especificos. Seleccionar patron apropiado segun caso de uso y generar modelo.

## Input/Output

- **Input:** Dominio a modelar, posicion establecida, tensiones identificadas
- **Output:** Modelo ontologico usando patrones Gist con justificacion

## Procedimiento

1. Evaluar patrones Gist aplicables:

**Category_Pattern:**
- Cuando: Taxonomia flexible, administrada por no-ontologos, sin restricciones formales
- Usar: gist:Category + subclasses (Behavior, Discipline, Tag, etc.)
- Evitar: Crear owl:Class para cada tipo

**TemporalRelation_Pattern:**
- Cuando: Relacion con duracion temporal o contexto temporal
- Usar: gist:TemporalRelation con gist:hasParticipant
- Ejemplo: Employment, Membership, Ownership temporal

**Magnitude_Pattern:**
- Cuando: Cantidad medible con unidad
- Usar: gist:Magnitude + gist:hasAspect + gist:hasUnitOfMeasure + gist:numericValue
- Evitar: Datatype properties directas para valores con unidades

**Address_Pattern:**
- Cuando: Direcciones fisicas o electronicas
- Usar: gist:PhysicalAddress o gist:ElectronicAddress + gist:containedText + gist:refersTo
- Categorias: AddressUsageType, PhysicalAddressType, ElectronicAddressType

**Extension_Pattern:**
- Cuando: Extender Gist con conceptos de dominio
- Usar: Crear subclases en namespace propio, usar gist: para propiedades existentes
- Namespace: Mantener conceptos Gist en gist:, extensiones en ns propio

2. Seleccionar patron(es) segun caso de uso
3. Generar modelo con clases, propiedades, ejemplo Turtle
4. Documentar trade-offs de cada decision

## Signature Output

```
PATRON: {nombre}
CLASES: [{gist:Class1}, {ex:Extension1}]
PROPIEDADES: [{gist:prop1}]
TURTLE: {ejemplo}
TRADE_OFFS: [{descripcion}]
```
