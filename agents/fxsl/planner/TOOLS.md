---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:planner-tools:1.0.0"
  type: "bootstrap_tools"
---

## okr_structure

- **Firma:** {contexto_negocio: string, ciclo: int} → {objetivos: [{objetivo, key_results: [{kr, baseline, target, actual?}]}], presupuesto_tokens: int}
- **Cuando usar:** S-OKR. Estructurar OKRs para un Ciclo nuevo.
- **Cuando NO usar:** Si los OKRs del Ciclo ya estan definidos y aprobados.
- **Notas:** KRs DEBEN ser analogos (gradiente medible), no binarios. 1-3 Objetivos, 2-4 KRs por Objetivo.

## epic_decompose

- **Firma:** {epica: string, kr_asociado: string} → {historias: [{who_what_why, criterios_aceptacion[], valor, complejidad, riesgo, dependencias[]}]}
- **Cuando usar:** S-EPICA. Descomponer una epica en historias independientes.
- **Cuando NO usar:** Si la epica ya esta descompuesta.
- **Notas:** Cada historia DEBE tener valor de negocio independiente. 4-8 historias por epica tipicamente.

## story_refine

- **Firma:** {historia: string} → {who_what_why, criterios_aceptacion[], valor: int, complejidad: simple|estandar|complejo|critico, riesgo: lectura|escritura|destructiva, dependencias[], tier_modelo: T1|T2|T3|T4}
- **Cuando usar:** S-HISTORIA. Refinar una historia con los 5 elementos completos.
- **Cuando NO usar:** Si la historia ya tiene los 5 elementos verificados.
- **Notas:** Complejidad determina tier de modelo via Model Router. Riesgo determina si requiere aprobacion humana pre-ejecucion.

## backlog_prioritize

- **Firma:** {historias: story[]} → {backlog_ordenado: [{historia, prioridad, formula: valor/(coste×riesgo)}]}
- **Cuando usar:** S-BACKLOG. Priorizar historias pendientes.
- **Cuando NO usar:** Si el backlog ya esta priorizado y no hay historias nuevas.
- **Notas:** Formula: Prioridad = Valor / (Coste_Estimado × Multiplicador_Riesgo). Multiplicador: lectura=1, escritura=1.5, destructiva=3.

## pattern_detect

- **Firma:** {okrs_activos, metricas_producto?, historias_completadas[]} → {propuestas: [{borrador_historia, justificacion, confianza}]}
- **Cuando usar:** S-PREDICTIVO. Proponer historias basadas en patrones.
- **Cuando NO usar:** Si el PO ya tiene backlog nutrido para el Ciclo.
- **Notas:** Las propuestas son BORRADORES para curado del PO, no decisiones. Confianza: alta|media|baja.

## cycle_metrics

- **Firma:** {ciclo: int, historias_done[], presupuesto_tokens, krs[]} → {cph: float, ta: float, cycle_time: float, presupuesto_consumido: float, krs_progreso: [{kr, baseline, target, actual, %completado}]}
- **Cuando usar:** S-RETRO. Recopilar y analizar metricas del Ciclo.
- **Cuando NO usar:** Si no hay datos de ciclo para analizar.
- **Notas:** Metricas segun Xanpan::Agents §8: CpH (tokens/historia), TA (% aceptacion primer intento), Cycle Time (backlog→done).

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Clasificar tema → resolver URN → consultar KB del corpus xanpan.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| OKRs, historias, roles, enjambre, sentinel, evals, tablero, economia tokens, metodologia | urn:fxsl:kb:xanpan-agents-metodologia |
| Stack, arquitectura, frontend, backend, datos, CI/CD, context engineering, model router | urn:fxsl:kb:stack-llm-arquitectura |
| Operaciones, pipeline, deploy, observabilidad, seguridad, IaConversation | urn:fxsl:kb:swarm-ops-metodologia |
| Bootstrap, operador solitario, fases, dual-hat, infraestructura progresiva | urn:fxsl:kb:chapter0-operador-solitario |
