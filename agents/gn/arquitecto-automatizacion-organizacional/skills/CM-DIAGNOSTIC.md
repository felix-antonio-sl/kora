---
_manifest:
  urn: "urn:gn:agent-bootstrap:arquitecto-automatizacion-organizacional-cm-diagnostic:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Diagnosticar ineficiencias sistemicas en procesos organizacionales. Clasificar problemas por tipo, impacto y automatizabilidad.

## Input/Output

- **Input:** Modelo de sistema o descripcion de proceso con puntos de friccion
- **Output:** Diagnostico clasificado con impacto estimado y automatizabilidad

## Procedimiento

1. Identificar patrones de ineficiencia:
   - Cuello de botella: flujo se detiene. Sintomas: colas, esperas, backlog creciente. Causa: Capacidad < Demanda.
   - Redundancia: trabajo duplicado sin valor. Sintomas: misma info en multiples lugares, retrabajos. Causa: falta integracion, silos.
   - Friccion: pasos manuales automatizables. Sintomas: copy-paste, tareas repetitivas, errores humanos. Causa: falta automatizacion.
   - Decision lenta: informacion no llega a quien decide. Sintomas: escalaciones lentas, decisiones con info incompleta. Causa: flujos info mal disenados.

2. Estimar impacto: tiempo, costo, errores, satisfaccion

3. Clasificar automatizabilidad:
   - Simple: reglas claras, datos disponibles, APIs existen
   - Con AI: requiere interpretacion, lenguaje natural, decisiones contextuales
   - Requiere rediseno: proceso fundamentalmente roto, automatizar empeoraria

4. Priorizar por ROI: impacto / esfuerzo

## Signature Output

Tabla diagnostico (punto friccion | tipo | impacto | automatizabilidad | prioridad ROI) + Roadmap priorizado de transformacion.
