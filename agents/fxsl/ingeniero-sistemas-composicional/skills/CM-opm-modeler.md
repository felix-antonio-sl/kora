---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:ingeniero-sistemas-composicional-cm-opm-modeler:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Modelar sistema usando Object-Process Methodology (OPM). Identificar objetos, estados, procesos y enlaces para producir System Diagram y descripciones OPL.

## Input/Output

- **Input:** Dominio y stakeholders capturados desde S-SYSTEM-MODELING
- **Output:** Modelo OPM con objetos, estados, procesos, enlaces y OPL

## Procedimiento

1. Identificar OBJETOS: cosas que existen (fisicas o informacionales)
2. Definir ESTADOS: estados posibles de cada objeto
3. Identificar PROCESOS: transformaciones (crear, consumir, cambiar estado)
4. Establecer ENLACES ESTRUCTURALES: agregacion, caracterizacion, generalizacion
5. Establecer ENLACES PROCEDURALES: consumo, efecto, resultado, habilitacion
6. Generar SYSTEM DIAGRAM: funcion principal + beneficiario + operando
7. Generar OPL textual

### Templates OPL

- Objeto: `[Object] is [physical|informatical].`
- Estado: `[Object] can be [state1], [state2], or [state3].`
- Proceso: `[Process] [creates|consumes|affects] [Object].`
- Agente: `[Agent] handles [Process].`
- Instrumento: `[Process] requires [Instrument].`

## Signature Output

```
## Modelo OPM
### Objetos y Estados
| Objeto | Tipo | Estados |
|--------|------|---------|

### Procesos
| Proceso | Transforma | De → A |
|---------|-----------|--------|

### OPL
{Descripciones OPL en bloque codigo}

### System Diagram
{Diagrama SD alto nivel}
```
