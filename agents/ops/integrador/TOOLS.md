---
_manifest:
  urn: "urn:ops:agent-bootstrap:integrador-tools:1.0.0"
  type: "bootstrap_tools"
---

## semantic_merge

- **Firma:** pr: {diff: string, files: string[], branch: string, target: string}, main_state: {architecture: ArchInfo, conventions: ConventionSet} → merge_result: {status: coherent|incoherent, issues: SemanticIssue[], auto_fixable: boolean}
- **Cuando usar:** S-MERGE. Verificar coherencia semantica de un PR contra estado actual de main antes de merge.
- **Cuando NO usar:** PR ya mergeado, merge ya verificado en turno actual.
- **Notas:** Analiza: alineacion de tipos, conflictos de imports, convenciones de naming, contratos de interfaz, patrones arquitectonicos.

## coherence_check

- **Firma:** prs: {pr_id: string, diff: string, target_zone: string}[] → coherence_result: {status: coherent|contradictory|duplicate, conflicts: CrossPRConflict[], recommendation: string}
- **Cuando usar:** S-COHERENCIA. Cuando multiples PRs target misma zona del codebase. Verificar que no se contradicen entre si.
- **Cuando NO usar:** PR unico sin overlap con otros PRs en cola.
- **Notas:** Detecta: patrones contradictorios, implementaciones duplicadas de misma feature, asunciones mutuamente excluyentes, interfaces inconsistentes entre PRs.

## conflict_classify

- **Firma:** conflict: {files: string[], diff_a: string, diff_b: string, conflict_markers: string[]} → classification: {type: trivial|substantivo, reason: string, auto_resolvable: boolean, evidence: string[]}
- **Cuando usar:** S-CONFLICTO. Clasificar conflicto detectado entre PRs o entre PR y main.
- **Cuando NO usar:** Conflicto ya clasificado en turno actual.
- **Notas:** Trivial: import order, whitespace, formatting, reorder de funciones. Substantivo: logica conflictuante, implementaciones competidoras, contracts rotos, cambios de signature.

## conflict_resolve

- **Firma:** conflict: {classification: Classification, diff_a: string, diff_b: string} → resolution: {status: resolved|escalated, resolved_diff?: string, escalation_reason?: string, diagnostic?: string}
- **Cuando usar:** S-CONFLICTO despues de clasificacion. Resolver conflicto trivial automaticamente o preparar escalacion para substantivo.
- **Cuando NO usar:** Conflicto no clasificado. NUNCA resolver conflicto substantivo autonomamente.
- **Notas:** Resolucion trivial: aplicar convencion del proyecto (import order, formatting rules). Escalacion substantiva: diagnostico completo con evidencia, opciones, impacto.

## queue_manage

- **Firma:** action: enqueue|dequeue|prioritize|status, pr?: PRInfo, priority?: number → queue_state: {depth: number, throughput: number, avg_time: number, ordered_prs: PRQueueEntry[]}
- **Cuando usar:** S-COLA. Gestionar merge queue: agregar PR, remover, repriorizar, consultar estado.
- **Cuando NO usar:** Cola vacia y sin PRs pendientes.
- **Notas:** Priorizacion por valor de negocio de historia asociada. Reporta: depth, throughput PRs/hora, tiempo promedio en cola.

## backpressure_control

- **Firma:** action: activate|deactivate|status, queue_depth?: number, threshold?: number → backpressure_state: {active: boolean, queue_depth: number, threshold: number, notification_sent: boolean}
- **Cuando usar:** S-COLA cuando queue_depth > threshold. Activar backpressure para reducir tasa generacion PRs.
- **Cuando NO usar:** Cola dentro de threshold. Backpressure ya en estado deseado.
- **Notas:** Activacion notifica al orquestador para reducir tasa. Desactivacion cuando cola drena bajo threshold. Status reporta estado actual.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Clasificar tema → resolver URN → priorizar KB.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Xanpan metodologia, stories, DoD | urn:fxsl:kb:xanpan-agents-metodologia |
| Swarm ops, integracion, pipeline, backpressure | urn:fxsl:kb:swarm-ops-metodologia |
| Agent spec, workspace, FSM | urn:kora:kb:agent-spec-md |
