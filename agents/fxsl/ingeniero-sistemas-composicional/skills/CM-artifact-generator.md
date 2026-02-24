---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:ingeniero-sistemas-composicional-cm-artifact-generator:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Producir artefactos de ingenieria de sistemas desde modelos. Seleccionar formato, aplicar plantilla, mantener trazabilidad y validar consistencia.

## Input/Output

- **Input:** Modelo de sistema (OPM, breakdowns, requisitos) desde S-ARTIFACT-GENERATION
- **Output:** Artefactos concretos en formato seleccionado

## Procedimiento

1. Seleccionar formato(s) de salida segun necesidad
2. Aplicar plantilla estandar del formato
3. Mantener trazabilidad con modelo fuente
4. Validar consistencia interna entre artefactos

### Formatos Soportados

| Formato | Descripcion |
|---------|-------------|
| OPD (Object-Process Diagram) | Diagrama visual del modelo OPM |
| OPL (Object-Process Language) | Descripcion textual del modelo |
| FBS Tree | Arbol de desglose funcional |
| PBS Tree | Arbol de desglose de producto |
| LBS Tree | Arbol de desglose de ubicacion |
| SRS (Requirements Spec) | Especificacion de requisitos |
| Traceability Matrix | Matriz de trazabilidad |
| Work System Snapshot | Vista resumen del sistema de trabajo |
| Wiring Diagram | Diagrama de composicion |
| Interface Control Document | Especificacion de interfaces |

## Signature Output

```
## Artefacto: {formato}
### Metadata
- Modelo fuente: {referencia}
- Fecha: {fecha}

### Contenido
{artefacto generado en formato target}

### Trazabilidad
{referencias al modelo fuente}
```
