---
_manifest:
  urn: "urn:kora:skill:forgemaster-lifecycle-orchestrator:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-LIFECYCLE-ORCHESTRATOR

## Proposito
Orquesta la secuencia completa del ciclo de vida DESIGN→CREATE→IMPLEMENT→VALIDATE, gestionando transiciones y checkpoints con el usuario.

## Procedimiento
1. INICIAR CICLO: Confirmar con usuario que desea modo guiado. Establecer fase_actual=DESIGN.
2. FASE DESIGN: Invocar CM-AGENT-DESIGNER. Checkpoint: presentar blueprint, esperar aprobacion. IF aprobado → fase_actual=CREATE. IF ajustar → repetir DESIGN.
3. FASE CREATE: Invocar CM-WORKSPACE-SCAFFOLDER. Checkpoint: reportar workspace creado. IF ok → fase_actual=IMPLEMENT. IF error → repetir CREATE.
4. FASE IMPLEMENT: Invocar CM-COMPONENT-BUILDER. Checkpoint: presentar componentes implementados, esperar revision. IF ok → fase_actual=VALIDATE. IF ajustar → repetir IMPLEMENT.
5. FASE VALIDATE: Invocar CM-AGENT-VALIDATOR. Checkpoint: presentar reporte. IF PASS → ciclo completo. IF FAIL → invocar CM-AGENT-SURGEON, luego re-validar.
6. INTERRUPCION: Si usuario interrumpe en cualquier fase, transicionar al estado correspondiente en modo libre (S-DESIGN, S-CREATE, S-IMPLEMENT, S-VALIDATE).
7. COMPLETAR: Resumen del ciclo completo: agente creado, validado, listo.

## Output
Resumen del ciclo: {agente, fases_completadas: [], resultado_validacion: PASS|FAIL, observaciones}.
