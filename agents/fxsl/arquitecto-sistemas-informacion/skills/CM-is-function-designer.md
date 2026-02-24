---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:arquitecto-sistemas-informacion-cm-is-function-designer:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Seleccionar y especificar funciones de IS para el WS destino, usando las 11 funciones canonicas como taxonomia. Establecer prioridades y dependencias.

## Input/Output

- **Input:** WS Snapshot desde S-IS-FUNCTIONS
- **Output:** Funciones IS seleccionadas con prioridad, inputs, outputs

## Procedimiento

1. Evaluar cada una de las 11 funciones canonicas contra el WS destino
2. Seleccionar funciones relevantes
3. Especificar cada funcion: inputs, outputs, reglas
4. Establecer prioridades y dependencias entre funciones

### 11 Funciones Canonicas de IS

| ID | Funcion | Descripcion |
|----|---------|-------------|
| F1 | Proveer acceso a informacion | Consulta y recuperacion de datos |
| F2 | Definir/aplicar reglas para recopilar/compartir informacion | Control de captura y acceso |
| F3 | Proveer metodos para agregar informacion | Agregacion, resumen, consolidacion |
| F4 | Proveer metodos para analizar informacion | Analitica, reportes, dashboards |
| F5 | Controlar secuencia actividades en workflows | Orquestacion procesos, estados, transiciones |
| F6 | Aplicar reglas de negocio | Validaciones, restricciones, calculos automaticos |
| F7 | Generar alarmas en condiciones predefinidas | Alertas, notificaciones, escalamientos |
| F8 | Facilitar coordinacion | Comunicacion, asignacion, seguimiento |
| F9 | Sugerir/evaluar decisiones | Recomendaciones, scoring, ranking |
| F10 | Activar funciones automatizadas | Triggers, eventos, integraciones |
| F11 | Realizar tareas totalmente automatizadas | Procesos sin intervencion humana |

## Signature Output

```
## Funciones de IS Seleccionadas
| ID | Funcion | Prioridad | Inputs | Outputs |
|----|---------|-----------|--------|---------|
| {id} | {nombre} | {alta|media|baja} | {entradas} | {salidas} |
```
