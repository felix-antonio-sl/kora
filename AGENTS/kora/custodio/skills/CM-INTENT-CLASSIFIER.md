---
_manifest:
  urn: urn:kora:skill:custodio-intent-classifier:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-INTENT-CLASSIFIER

## Proposito
Clasifica la solicitud actual dentro del dominio operacional del custodio, determinando la capacidad requerida.

## Input/Output
- **Input:** mensaje: string (mensaje del usuario), foco_actual: string | null, contexto_previo: SessionContext | null
- **Output:** IntentClassification (ver Signature Output)

## Procedimiento
1. Analizar mensaje: palabras clave, contexto previo, rutas mencionadas, comandos referenciados.
2. Clasificar capacidad: SALUD(diagnosticar, health, validate, stats), CATALOGO(index, urn, broken, sincronizar), INGESTA(inbox, pipeline, intake, source, drafts), AUDITORIA(estructura, topologia, convenciones, huerfanos), CIRUGIA(reparar, fix, arreglar), EVOLUCION(mejorar, evolucionar, planificar, optimizar).
3. Si el mensaje expresa cierre del trabajo actual, marcar cierre_solicitado.
4. Emitir clasificacion: {capacidad, continuidad, confianza, cierre_solicitado}.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| capacidad | enum(SALUD\|CATALOGO\|INGESTA\|AUDITORIA\|CIRUGIA\|EVOLUCION) | Capacidad clasificada |
| continuidad | enum(coherente\|nuevo\|retoma) | Relacion semantica con el foco previo |
| confianza | enum(alta\|media\|baja) | Nivel de confianza. Si baja, formular pregunta aclaratoria |
| cierre_solicitado | bool | True si el mensaje indica cierre del trabajo actual |
