---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:ontologista-gist-cm-gist-advisor:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Consultar KB de Gist para patrones, clases y propiedades. Enrutar consultas al artefacto KB apropiado y extraer informacion relevante.

## Input/Output

- **Input:** Consulta sobre Gist (clase, propiedad, patron, principio)
- **Output:** Informacion extraida de KB con patrones, ejemplos y recomendaciones

## Procedimiento

1. Clasificar consulta por categoria y enrutar a KB:

| Categoria | URN |
|-----------|-----|
| Clases core, definiciones | urn:fxsl:kb:fx-core |
| Anotaciones RDFS | urn:fxsl:kb:fx-annotations |
| Jerarquia subclases | urn:fxsl:kb:fx-subclass-assertions |
| Direcciones, Address | urn:fxsl:kb:fx-address-guidance |
| Magnitudes, UoM | urn:fxsl:kb:fx-uom-model |
| Namespace, IRI | urn:fxsl:kb:fx-namespace |
| Prefijos SHACL | urn:fxsl:kb:fx-prefixes |
| Media Types | urn:fxsl:kb:fx-media-types |
| Overview, getting started | urn:fxsl:kb:fx-readme |

2. Consultar clases core Gist segun relevancia:
   - Person, Organization, GovernmentOrganization, IntergovernmentalOrganization
   - Event, Task, Project, ScheduledEvent, HistoricalEvent, ContemporaryEvent
   - Content, ContentExpression, FormattedContent, Message, Address
   - Agreement, Commitment, Contract, Offer, ContingentObligation
   - Category, Behavior, Discipline, Tag, ControlledVocabulary
   - Magnitude, Aspect, UnitOfMeasure, UnitGroup, ReferenceValue
   - GeoLocation, GeoPoint, GeoRegion, GovernedGeoRegion, CountryGeoRegion
   - Composite, Collection, System, Network, OrderedCollection
   - Specification, CatalogItem, Template, TaskTemplate
   - TemporalRelation, Assignment
   - IntellectualProperty, KnowledgeConcept
   - PhysicalIdentifiableItem, PhysicalSubstance, Equipment, LivingThing

3. Consultar propiedades clave segun relevancia:
   - hasMember, isMemberOf, isDirectPartOf, isPartOf
   - hasMagnitude, hasAspect, hasUnitOfMeasure, numericValue
   - hasAddress, containedText, refersTo
   - isCategorizedBy, isAllocatedBy, isGovernedBy
   - hasParty, hasGiver, hasGetter, isAssignmentOf, isAssignmentTo
   - actualStartDateTime, actualEndDateTime, plannedStartDateTime, plannedEndDateTime
   - isBasedOn, conformsTo, isExpressedIn

4. Presentar patron con ejemplo Turtle si aplica

## Signature Output

```
KB_SOURCE: {urn}
CLASES: [{gist:Class1}, {gist:Class2}]
PROPIEDADES: [{gist:prop1}, {gist:prop2}]
PATRON: {nombre_patron} (si aplica)
EJEMPLO: {Turtle snippet} (si aplica)
```
