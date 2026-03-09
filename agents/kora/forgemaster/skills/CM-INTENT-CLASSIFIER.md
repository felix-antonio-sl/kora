---
_manifest:
  urn: urn:kora:skill:forgemaster-intent-classifier:2.0.0
  type: lazy_load_endofunctor
version: 2.0.0
status: published
lang: es
---

# CM-INTENT-CLASSIFIER

## Proposito
Clasifica la solicitud actual dentro del ciclo de vida de agentes, determinando capacidad y modo de trabajo.

## Input/Output
- **Input:** mensaje: string (mensaje del usuario), foco_actual: string | null, contexto_previo: SessionContext | null
- **Output:** IntentClassification (ver Signature Output)

## Procedimiento
1. Analizar mensaje: palabras clave, contexto previo, agentes mencionados, artefactos referenciados.
2. Clasificar capacidad: DESIGN(disenar nuevo), CREATE(scaffold workspace), IMPLEMENT(rellenar componentes), VALIDATE(verificar conformidad), OPERATE(diagnosticar/reparar/mantener), IMPROVE(optimizar/expandir), DEPRECATE(retirar), GUIDED(ciclo guiado).
3. Determinar modo: GUIADO(usuario quiere ciclo completo paso a paso), LIBRE(usuario quiere capacidad especifica directa).
4. Si hay progreso previo, estimar continuidad semantica con el foco actual.
5. Si el mensaje expresa cierre del trabajo actual, marcar cierre_solicitado.
6. Emitir clasificacion: {capacidad, modo, continuidad, confianza, cierre_solicitado}.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| capacidad | enum(DESIGN\|CREATE\|IMPLEMENT\|VALIDATE\|OPERATE\|IMPROVE\|DEPRECATE\|GUIDED) | Capacidad clasificada |
| modo | enum(GUIADO\|LIBRE) | Modo de operacion |
| continuidad | enum(coherente\|nuevo\|retoma) | Relacion semantica con el foco previo |
| confianza | enum(alta\|media\|baja) | Nivel de confianza. Si baja, formular pregunta aclaratoria |
| cierre_solicitado | bool | True si el mensaje indica cierre del trabajo actual |
