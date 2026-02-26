---
_manifest:
  urn: "urn:kora:skill:forgemaster-agent-evolver:2.0.0"
  type: "lazy_load_endofunctor"
version: "2.0.0"
status: published
lang: es
---
# CM-AGENT-EVOLVER

## Proposito
Analiza un agente existente y propone mejoras iterativas: optimizar FSM, refinar skills, expandir capacidades, mejorar fenomenologia.

## I/O

- **Input:** agent_path: string (ruta al workspace del agente objetivo)
- **Output:** EvolutionReport (ver Signature Output)

## Procedimiento
1. LEER WORKSPACE: workspace_read del agente objetivo. Entender su dominio, FSM, skills, tools.
2. ANALIZAR EFICIENCIA FSM: ¿Estados innecesarios? ¿Transiciones redundantes? ¿Determinismo respetado? ¿Co-induccion completa?
3. ANALIZAR SKILLS: ¿Cobertura suficiente? ¿Skills demasiado genericos? ¿Logica >5 pasos sin CM? ¿Skills no referenciados en FSM?
4. ANALIZAR FENOMENOLOGIA: ¿SOUL.md refleja el dominio actual? ¿Tono apropiado? ¿Ejemplos relevantes?
5. ANALIZAR TOOLS: ¿Herramientas suficientes? ¿Firmas correctas? ¿Routing map actualizado?
6. PROPONER MEJORAS: Lista priorizada con impacto(alto|medio|bajo) y esfuerzo(alto|medio|bajo). Recomendar quick wins primero.
7. IMPLEMENTAR MEJORAS APROBADAS: Aplicar cambios respetando segregacion. Una modificacion logica por iteracion.
8. RE-VALIDAR: CM-AGENT-VALIDATOR post-mejora.

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| agente | string | Nombre del agente analizado |
| analisis | {fsm: string, skills: string, soul: string, tools: string} | Resultado del analisis por area |
| mejoras_propuestas | {descripcion: string, impacto: enum, esfuerzo: enum}[] | Mejoras priorizadas |
| mejoras_aplicadas | string[] | Mejoras implementadas |
| validacion_post | enum(PASS\|FAIL) | Resultado de re-validacion |
