---
_manifest:
  urn: "urn:kora:skill:custodio-intent-classifier:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-INTENT-CLASSIFIER

## Proposito
Clasifica la intencion del usuario al inicio de cada turno en la FSM WF-CUSTODIO, determinando la capacidad operacional requerida.

## Procedimiento
1. Analizar mensaje: palabras clave, contexto previo, rutas mencionadas, comandos referenciados.
2. Clasificar capacidad: SALUD(diagnosticar, health, validate, stats), CATALOGO(index, urn, broken, sincronizar), INGESTA(inbox, pipeline, intake, source, drafts), AUDITORIA(estructura, topologia, convenciones, huerfanos), CIRUGIA(reparar, fix, arreglar), EVOLUCION(mejorar, evolucionar, planificar, optimizar), END(terminar, fin, salir).
3. Si hay progreso previo, identificar estado actual y continuidad.
4. Emitir clasificacion: {capacidad, confianza}.

## Output
Clasificacion con campos: `capacidad` (enum), `confianza` (alta|media|baja). Si confianza=baja, formular pregunta aclaratoria antes de transicionar.
