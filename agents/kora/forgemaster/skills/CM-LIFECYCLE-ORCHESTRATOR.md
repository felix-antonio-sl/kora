---
_manifest:
  urn: urn:kora:skill:forgemaster-lifecycle-orchestrator:2.0.0
  type: lazy_load_endofunctor
version: 2.0.0
status: published
lang: es
---

# CM-LIFECYCLE-ORCHESTRATOR

## Proposito
Orquesta la secuencia completa del ciclo de vida DESIGN→CREATE→IMPLEMENT→VALIDATE, consolidando entregables y contexto inter-fase.

## Input/Output
- **Input:** dominio: string (descripcion del agente a crear), namespace: string, restricciones: string[] | null
- **Output:** LifecycleReport (ver Signature Output)

## Procedimiento
1. INICIAR CICLO: establecer fase_actual=DESIGN y registrar contexto base del workspace objetivo.
2. FASE DESIGN: invocar CM-AGENT-DESIGNER, registrar blueprint y pendientes estructurales.
3. FASE CREATE: invocar CM-WORKSPACE-SCAFFOLDER, registrar workspace creado y componentes bootstrap materializados.
4. FASE IMPLEMENT: invocar CM-COMPONENT-BUILDER, consolidar componentes implementados y skills materializados.
5. FASE VALIDATE: invocar CM-AGENT-VALIDATOR, consolidar veredicto PASS|FAIL e issues accionables.
6. REANUDACION: preservar fase_actual y artefactos de fase para permitir continuidad sin recalcular etapas ya cerradas.
7. COMPLETAR: emitir resumen del ciclo completo con agente, fases ejecutadas, resultado y observaciones.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| agente | string | Nombre del agente creado |
| fases_completadas | string[] | Fases del ciclo ejecutadas |
| resultado_validacion | enum(PASS\|FAIL) | Resultado final de validacion |
| observaciones | string | Notas relevantes del ciclo |
