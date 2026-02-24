---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:arquitecto-sistemas-informacion-cm-ws-analyzer:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Analizar el Work System que el IS soportara. Mapear procesos, participantes, informacion, tecnologias, clientes y productos/servicios del WS destino.

## Input/Output

- **Input:** Descripcion del IS solicitado desde S-WS-CONTEXT
- **Output:** Work System Snapshot del WS destino con 6 elementos clave

## Procedimiento

1. Identificar PROCESOS: que actividades realiza el WS?
2. Identificar PARTICIPANTES: quienes trabajan en el WS?
3. Mapear INFORMACION ACTUAL: que informacion usa/produce?
4. Inventariar TECNOLOGIAS: que herramientas usa actualmente?
5. Identificar CLIENTES: quienes reciben los outputs del WS?
6. Catalogar PRODUCTOS/SERVICIOS: que produce el WS?
7. Formular preguntas de clarificacion si informacion insuficiente

## Signature Output

```
## Work System que el IS Soportara
| Elemento | Descripcion |
|----------|-------------|
| Procesos | {actividades} |
| Participantes | {quienes} |
| Informacion | {datos actuales} |
| Tecnologias | {herramientas} |
| Clientes | {receptores} |
| Productos/Servicios | {outputs} |
```
