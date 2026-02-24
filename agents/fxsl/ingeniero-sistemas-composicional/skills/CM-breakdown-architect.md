---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:ingeniero-sistemas-composicional-cm-breakdown-architect:1.0.0"
  type: "lazy_load_endofuntor"
---

## Proposito

Disenar estructuras de desglose jerarquico (FBS, PBS, LBS) con trazabilidad cruzada. Aplicar principios MECE y codificacion ISO 81346.

## Input/Output

- **Input:** Modelo OPM desde S-BREAKDOWN-DESIGN
- **Output:** FBS, PBS, LBS con trazabilidad y codificacion

## Procedimiento

1. Generar FBS: descomponer funciones (que hace el sistema?)
2. Derivar PBS: descomponer productos (de que esta hecho?)
3. Mapear LBS: descomponer ubicaciones (donde esta?) — si aplica
4. Establecer trazabilidad entre estructuras via funtores:
   - FBS→PBS: Que producto realiza esta funcion?
   - PBS→LBS: Donde esta ubicado este producto?
   - FBS→Requirements: Que requisitos especifican esta funcion?
5. Aplicar codificacion ISO 81346

### Reglas de Breakdown

- Cada nivel MECE (mutuamente excluyente, colectivamente exhaustivo)
- Profundidad maxima: 5-7 niveles para manejabilidad
- Cada elemento debe tener dueno identificable
- Las hojas deben ser verificables/implementables

## Signature Output

```
## FBS - Functional Breakdown Structure
{Arbol funcional en formato codigo}

## PBS - Product Breakdown Structure
{Arbol producto en formato codigo}

## LBS - Location Breakdown Structure
{Arbol ubicacion si aplica}

## Trazabilidad
| Funcion | Producto | Ubicacion | Stakeholder |
|---------|----------|-----------|-------------|
```
