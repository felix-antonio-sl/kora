---
_manifest:
  urn: "urn:kora:skill:forgemaster-component-builder:2.0.0"
  type: "lazy_load_endofunctor"
version: "2.0.0"
status: published
lang: es
---
# CM-COMPONENT-BUILDER

## Proposito
Rellena cada componente del workspace con contenido real, respetando estrictamente la segregacion por componente (agent-spec-md v7.2.0 §3).

## I/O

- **Input:** agent_path: string (ruta al workspace), blueprint: AgentBlueprint (output de CM-AGENT-DESIGNER)
- **Output:** ImplementationReport (ver Signature Output)

## Procedimiento
1. Leer blueprint del agente (output de CM-AGENT-DESIGNER).
2. IMPLEMENTAR AGENTS.md (behavior):
   - FSM numerada: cada estado con ACT + CMs invocados + Trans con IF→S-STATE.
   - Reglas Duras: Scope, Allowed, Forbidden, Rejection, Confidentiality.
   - Co-induccion: Checklist Pre-Output + Protocolo Correccion.
   - Contexto Multi-turno: CM-CONTEXT-MANAGER.
   - Wiring: herencia, sub-agentes, disipacion, dependencias inter-agente (del blueprint).
   - INVARIANTE: SIN fenomenologia, SIN policies, SIN tool details.
3. IMPLEMENTAR SOUL.md (state/personality):
   - Identidad Dialectica, Paradigma Cognitivo, Tono, Saludo, Estilo, Ejemplos.
   - INVARIANTE: SIN logica FSM (IF→STATE), SIN tools, SIN config.
4. IMPLEMENTAR USER.md (state/operator):
   - Perfil, Rutinas, Preferencias de Output.
   - INVARIANTE: SIN logica FSM, SIN fenomenologia, SIN config.
5. IMPLEMENTAR TOOLS.md (interface):
   - Firmas inferenciales: input→output, cuando usar, cuando NO usar, notas.
   - Routing map si usa kb_route.
   - INVARIANTE: SIN implementacion (endpoints, API keys).
6. IMPLEMENTAR config.json (security):
   - allowed_kb, sandbox, tools allow/deny, sub_agents. Opcional: limits, model_routing.
   - INVARIANTE: Inmutable desde LLM, prevalece sobre AGENTS.md.
7. MATERIALIZAR skills/ (CMs):
   - Para cada CM: frontmatter _manifest con type: "lazy_load_endofunctor", Proposito, I/O, Procedimiento, Signature Output.
   - URN: urn:{ns}:skill:{agente}-{id}:{version}.
8. Verificar segregacion cruzada: ningun componente contiene contenido de otro.

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| componentes_escritos | string[] | Lista de componentes implementados |
| skills_materializados | string[] | CMs creados en skills/ |
| segregacion_ok | bool | True si no hay contaminacion cruzada |
