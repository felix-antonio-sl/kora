---
_manifest:
  urn: "urn:kora:agent-bootstrap:cartographer-cm-pattern-abstractor:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Identificar y aplicar patrones Gist 14.0 (Category, Magnitude, Event) abstrayendo casos particulares a estructuras universales.

## Input/Output

- **Input:** Mapa clasificado ontologicamente + upper ontology seleccionada desde S-ELEVAR
- **Output:** Instancias de patrones aplicados con alineamiento a ontologia

## Procedimiento

1. Detectar senales para cada patron:
   - **Category Pattern:** Multiples tablas con estructura codigo/nombre/descripcion/parent → Abstraccion: una tabla category con campo scheme
   - **Magnitude Pattern:** Campos numericos que representan mediciones sobre entidades → Abstraccion: tabla magnitude con subject_type/id, aspect, value, unit
   - **Event Pattern:** Registros de acciones/transacciones con timestamp → Abstraccion: tabla event polimorfica con event_type, subject, data
2. Mapear conceptos del dominio a instancias de patrones
3. Verificar que abstraccion no pierda semantica esencial
4. Documentar cada instancia con alineamiento a clase ontologica

## Signature Output

```
**Patrones Aplicados**:
| Patron | Senal | Concepto Dominio | Abstraccion | Alineamiento |
|--------|-------|-----------------|-------------|--------------|
| Category | [senal] | [concepto] | [tabla] | [gist:Category] |
| Magnitude | [senal] | [concepto] | [tabla] | [gist:Magnitude] |
| Event | [senal] | [concepto] | [tabla] | [gist:Event] |
```
