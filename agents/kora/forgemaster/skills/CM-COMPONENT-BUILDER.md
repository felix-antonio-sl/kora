---
_manifest:
  urn: "urn:kora:skill:forgemaster-component-builder:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-COMPONENT-BUILDER

## Proposito
Rellena cada componente del workspace con contenido real, respetando estrictamente la segregacion por componente (agent-spec-md §3).

## Procedimiento
1. Leer blueprint del agente (output de CM-AGENT-DESIGNER).
2. IMPLEMENTAR AGENTS.md (c):
   - FSM numerada: cada estado con ACT + CMs invocados + Trans con IF→S-STATE.
   - Reglas Duras: Scope, Allowed, Forbidden, Rejection, Confidentiality.
   - Co-induccion: Checklist Pre-Output + Protocolo Correccion.
   - Contexto Multi-turno: CM-CONTEXT-MANAGER.
   - INVARIANTE: SIN fenomenologia, SIN policies, SIN tool details.
3. IMPLEMENTAR SOUL.md (U fenomenologica):
   - Identidad Dialectica, Paradigma Cognitivo, Tono, Saludo, Estilo, Ejemplos.
   - INVARIANTE: SIN logica FSM (IF→STATE), SIN tools, SIN config.
4. IMPLEMENTAR USER.md (U contexto):
   - Perfil, Rutinas, Preferencias de Output.
   - INVARIANTE: SIN logica FSM, SIN fenomenologia, SIN config.
5. IMPLEMENTAR TOOLS.md (F):
   - Firmas inferenciales: input→output, cuando usar, cuando NO usar, notas.
   - Routing map si usa kb_route.
   - INVARIANTE: SIN implementacion (endpoints, API keys).
6. IMPLEMENTAR config.json (M):
   - allowed_kb, sandbox, tools allow/deny, sub_agents.
   - INVARIANTE: Inmutable desde LLM, prevalece sobre AGENTS.md.
7. MATERIALIZAR skills/ (CMs):
   - Para cada CM: frontmatter _manifest, Proposito, Procedimiento, Output.
   - URN: urn:{ns}:skill:{agente}-{id}:{version}.
8. Verificar segregacion cruzada: ningun componente contiene contenido de otro.

## Output
Workspace implementado. Reporte: {componentes_escritos, skills_materializados, segregacion_ok: bool}.
