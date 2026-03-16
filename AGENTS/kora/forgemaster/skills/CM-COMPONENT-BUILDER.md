---
_manifest:
  urn: urn:kora:skill:forgemaster-component-builder:2.0.0
  type: lazy_load_endofunctor
version: 2.0.0
status: published
lang: es
---

# CM-COMPONENT-BUILDER

## Proposito
Rellena cada componente del workspace con contenido real, respetando estrictamente la segregacion por componente (agent-spec-md v8.4.0 §4).

## Input/Output
- **Input:** agent_path: string (ruta al workspace), blueprint: AgentBlueprint (output de CM-AGENT-DESIGNER)
- **Output:** ImplementationReport (ver Signature Output)

## Procedimiento
1. Leer blueprint del agente (output de CM-AGENT-DESIGNER).
2. IMPLEMENTAR AGENTS.md (behavior):
   - FSM numerada: cada estado con ACT conciso + skill/tool invocado + Trans con IF -> S-STATE.
   - Reglas Duras: Scope, Allowed, Forbidden, Rejection.
   - Co-induccion: Checklist Pre-Output + Protocolo Correccion.
   - Contexto Multi-turno: CM-CONTEXT-MANAGER.
   - Wiring: herencia, sub-agentes, disipacion, dependencias inter-agente (del blueprint).
   - INVARIANTE: SIN fenomenologia, SIN policies, SIN tool details, SIN pseudoestados y SIN pasos internos del CM.
3. IMPLEMENTAR SOUL.md (state/personality):
   - Identidad Dialectica, Paradigma Cognitivo, Tono.
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
7. MATERIALIZAR `skills/`:
   - Skill degenerado: crear `skills/CM-{id}.md` con frontmatter `_manifest.type="lazy_load_endofunctor"`, `Proposito`, `Input/Output`, `Procedimiento`, `Signature Output`.
   - Skill extendido: crear `skills/CM-{id}/SKILL.md` con el mismo `CM Core` y metadata de bundle bajo `extensions.{namespace}.skill`.
   - Si el Skill es extendido, crear solo las fibras requeridas: `scripts/`, `references/`, `assets/`.
   - URN del entrypoint: `urn:{ns}:skill:{agente}-{id}:{version}`.
   - INVARIANTE: no coexistir `skills/CM-{id}.md` y `skills/CM-{id}/SKILL.md` para el mismo identificador simbolico.
8. Verificar segregacion cruzada: ningun componente contiene contenido de otro y ningun bundle extendido fuga fuera de la fibra `skills/`.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| componentes_escritos | string[] | Lista de componentes implementados |
| skills_materializados | string[] | Skills creados en `skills/` como `CM-*.md` o `CM-*/SKILL.md` |
| segregacion_ok | bool | True si no hay contaminacion cruzada |
