---
_manifest:
  urn: "urn:kora:skill:forgemaster-agent-designer:2.0.0"
  type: "lazy_load_endofunctor"
version: "2.0.0"
status: published
lang: es
---
# CM-AGENT-DESIGNER

## Proposito
Modela la arquitectura de un agente nuevo: elicita dominio, define estados, capas de estado, interface y security. Produce blueprint arquitectonico completo. Referencia: agent-spec-md v7.2.0 (tabla de equivalencia terminologica v6/v7 en §15).

## I/O

- **Input:** dominio: string (descripcion del dominio del agente), namespace: string, restricciones: string[] | null
- **Output:** AgentBlueprint (ver Signature Output)

## Procedimiento
1. ELICITAR DOMINIO: ¿Que hace el agente? ¿En que namespace vive? ¿Con que agentes interactua? ¿Que restricciones tiene?
2. MODELAR BEHAVIOR (c): Identificar modos comportamentales → mapear a estados. Minimo S-DISPATCHER + S-END. Constraints: determinismo, alcanzabilidad, sin ciclos infinitos.
3. MODELAR STATE (U): Definir identidad dialectica(SOUL.md), contexto operador(USER.md). Verificar ortogonalidad entre capas de estado.
4. MODELAR INTERFACE (F): Identificar herramientas necesarias. Definir firmas inferenciales(input→output). Routing map si usa kb_route.
5. MODELAR SECURITY (M): Definir allowed_kb, sandbox mode, tools allow/deny, sub_agents limits.
6. MODELAR WIRING (W): ¿Es sub-agente de alguien? ¿Tiene sub-agentes? Declarar herencia y disipacion.
7. IDENTIFICAR SKILLS: Logica >5 pasos → CM. Listar CMs necesarios con proposito y estado que los invoca.
8. Presentar blueprint al usuario: tabla de componentes, diagrama FSM, lista de skills.

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| nombre | string | Nombre del agente |
| namespace | string | Namespace destino |
| estados | FSMState[] | Lista de estados con transiciones |
| state | {soul: SoulSpec, user: UserSpec} | Capas de estado (identidad + operador) |
| tools | ToolSpec[] | Herramientas con firmas inferenciales |
| config | ConfigSpec | Security: allowed_kb, sandbox, tools, sub_agents |
| skills | SkillSpec[] | CMs necesarios con proposito |
| wiring | WiringSpec[] | Herencia y disipacion si aplica |
