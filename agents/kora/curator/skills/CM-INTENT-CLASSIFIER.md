---
_manifest:
  urn: urn:kora:skill:curator-intent-classifier:2.0.0
  type: lazy_load_endofunctor
version: 2.0.0
status: published
lang: es
---

# CM-INTENT-CLASSIFIER

## Proposito
Clasifica la solicitud actual dentro del dominio de curaduria, determinando capacidad, tipo de artefacto y modo de trabajo.

## Input/Output
- **Input:** mensaje: string (mensaje del usuario), foco_actual: string | null, contexto_previo: SessionContext | null
- **Output:** IntentClassification (ver Signature Output)

## Procedimiento
1. Analizar mensaje: palabras clave, contexto previo, artefactos mencionados, documentos referenciados.
2. Clasificar capacidad: DESIGN(planificar nuevo), KORAFICATE(transformar doc humano a KORA/MD), CRYSTALLIZE(formalizar decisiones a KORA/Spec-MD), AUDIT(validar conformidad), EDIT(modificar existente), REPAIR(diagnosticar/corregir), IMPROVE(optimizar), DEPRECATE(retirar), GUIDED(ciclo guiado).
3. Determinar tipo artefacto: descriptivo(KORA/MD — hechos, datos, procedimientos), prescriptivo(KORA/Spec-MD — reglas, specs, protocolos), ambiguo(necesita clarificacion).
4. Determinar modo: GUIADO(usuario quiere ciclo completo paso a paso), LIBRE(usuario quiere capacidad especifica directa).
5. Si el mensaje expresa cierre del trabajo actual, marcar cierre_solicitado.
6. Emitir clasificacion: {capacidad, tipo_artefacto, modo, continuidad, confianza, cierre_solicitado}.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| capacidad | enum(DESIGN\|KORAFICATE\|CRYSTALLIZE\|AUDIT\|EDIT\|REPAIR\|IMPROVE\|DEPRECATE\|GUIDED) | Capacidad clasificada |
| tipo_artefacto | enum(descriptivo\|prescriptivo\|ambiguo) | Tipo de artefacto detectado |
| modo | enum(GUIADO\|LIBRE) | Modo de operacion |
| continuidad | enum(coherente\|nuevo\|retoma) | Relacion semantica con el foco previo |
| confianza | enum(alta\|media\|baja) | Nivel de confianza. Si baja, formular pregunta aclaratoria |
| cierre_solicitado | bool | True si el mensaje indica cierre del trabajo actual |
