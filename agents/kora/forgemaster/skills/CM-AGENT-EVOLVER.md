---
_manifest:
  urn: "urn:kora:skill:forgemaster-agent-evolver:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-AGENT-EVOLVER

## Proposito
Analiza un agente existente y propone mejoras iterativas: optimizar FSM, refinar skills, expandir capacidades, mejorar fenomenologia.

## Procedimiento
1. LEER WORKSPACE: workspace_read del agente objetivo. Entender su dominio, FSM, skills, tools.
2. ANALIZAR EFICIENCIA FSM: ¿Estados innecesarios? ¿Transiciones redundantes? ¿Determinismo respetado? ¿Co-induccion completa?
3. ANALIZAR SKILLS: ¿Cobertura suficiente? ¿Skills demasiado genericos? ¿Logica >5 pasos sin CM? ¿Skills no referenciados en FSM?
4. ANALIZAR FENOMENOLOGIA: ¿SOUL.md refleja el dominio actual? ¿Tono apropiado? ¿Ejemplos relevantes?
5. ANALIZAR TOOLS: ¿Herramientas suficientes? ¿Firmas correctas? ¿Routing map actualizado?
6. PROPONER MEJORAS: Lista priorizada con impacto(alto|medio|bajo) y esfuerzo(alto|medio|bajo). Recomendar quick wins primero.
7. IMPLEMENTAR MEJORAS APROBADAS: Aplicar cambios respetando segregacion. Un commit por mejora logica.
8. RE-VALIDAR: CM-AGENT-VALIDATOR post-mejora.

## Output
Reporte de mejora: {agente, analisis: {fsm, skills, soul, tools}, mejoras_propuestas: [{descripcion, impacto, esfuerzo}], mejoras_aplicadas: [], validacion_post: PASS|FAIL}.
