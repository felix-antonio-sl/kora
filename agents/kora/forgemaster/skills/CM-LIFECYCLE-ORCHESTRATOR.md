---
_manifest:
  urn: "urn:kora:skill:forgemaster-lifecycle-orchestrator:2.0.0"
  type: "lazy_load_endofunctor"
version: "2.0.0"
status: published
lang: es
---
# CM-LIFECYCLE-ORCHESTRATOR

## Proposito
Orquesta la secuencia completa del ciclo de vida DESIGN→CREATE→IMPLEMENT→VALIDATE, gestionando transiciones y checkpoints con el usuario.

## I/O

- **Input:** dominio: string (descripcion del agente a crear), namespace: string, restricciones: string[] | null
- **Output:** LifecycleReport (ver Signature Output)

## Procedimiento
1. INICIAR CICLO: Confirmar con usuario que desea modo guiado. Establecer fase_actual=DESIGN.
2. FASE DESIGN: Invocar CM-AGENT-DESIGNER. Checkpoint: presentar blueprint, esperar aprobacion. IF aprobado → fase_actual=CREATE. IF ajustar → repetir DESIGN.
3. FASE CREATE: Invocar CM-WORKSPACE-SCAFFOLDER. Checkpoint: reportar workspace creado. IF ok → fase_actual=IMPLEMENT. IF error → repetir CREATE.
4. FASE IMPLEMENT: Invocar CM-COMPONENT-BUILDER. Checkpoint: presentar componentes implementados, esperar revision. IF ok → fase_actual=VALIDATE. IF ajustar → repetir IMPLEMENT.
5. FASE VALIDATE: Invocar CM-AGENT-VALIDATOR. Checkpoint: presentar reporte. IF PASS → ciclo completo. IF FAIL → invocar CM-AGENT-SURGEON, luego re-validar.
6. INTERRUPCION: Si usuario interrumpe en cualquier fase, transicionar al estado correspondiente en modo libre (S-DESIGN, S-CREATE, S-IMPLEMENT, S-VALIDATE).
7. COMPLETAR: Resumen del ciclo completo: agente creado, validado, listo.

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| agente | string | Nombre del agente creado |
| fases_completadas | string[] | Fases del ciclo ejecutadas |
| resultado_validacion | enum(PASS\|FAIL) | Resultado final de validacion |
| observaciones | string | Notas relevantes del ciclo |
