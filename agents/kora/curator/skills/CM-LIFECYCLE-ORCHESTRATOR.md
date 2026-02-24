---
_manifest:
  urn: "urn:kora:skill:curator-lifecycle-orchestrator:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-LIFECYCLE-ORCHESTRATOR

## Proposito
Orquesta el ciclo de vida completo de un artefacto en modo guiado: DESIGN → FORGE (KORAFICATE|CRYSTALLIZE) → AUDIT, con checkpoints entre fases y gestion de contexto inter-fase.

## Procedimiento

### Fase 1: DESIGN (checkpoint)
1. Invocar CM-ARTIFACT-DESIGNER.
2. Presentar plan al usuario.
3. Esperar aprobacion antes de continuar.
4. Preservar contexto: {tipo, namespace, urn, fuente, estrategia}.

### Fase 2: FORGE (checkpoint)
1. Segun tipo:
   - Descriptivo → invocar CM-KORAFICATOR (Funtor F).
   - Prescriptivo → invocar CM-CRYSTALLIZER (Funtor G).
2. Presentar artefacto preliminar al usuario.
3. Esperar confirmacion o iteracion.
4. Preservar contexto: {artefacto_generado, metricas}.

### Fase 3: AUDIT (checkpoint)
1. Invocar CM-ARTIFACT-AUDITOR.
2. Presentar reporte al usuario.
3. Si PASS → proceder a cierre.
4. Si FAIL → ofrecer:
   - Reparar automaticamente (→ CM-ARTIFACT-SURGEON).
   - Volver a Fase 2 para re-iterar.
   - Dejar en draft para revision manual.

### Cierre
1. Recordar: ejecutar `kora index` para registrar en catalogo.
2. Sugerir: cambiar status draft → published una vez verificado.
3. Resumen final: tipo, URN, metricas, issues resueltos.

### Gestion de Contexto Inter-Fase
- Mantener estado acumulado entre fases: {fase_actual, plan, artefacto, reporte}.
- Si usuario interrumpe → transicionar a la fase actual en modo libre.
- Si usuario cambia de tema → S-DISPATCHER.

## Output
Artefacto completo, validado. Resumen de ciclo: {fases_completadas[], tipo, urn, metricas_finales, status_sugerido}.
