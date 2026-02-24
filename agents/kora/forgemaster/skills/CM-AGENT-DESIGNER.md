---
_manifest:
  urn: "urn:kora:skill:forgemaster-agent-designer:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-AGENT-DESIGNER

## Proposito
Modela la F-coalgebra de un agente nuevo: elicita dominio, define estados, fibras, funtor interfaz y monada de efectos. Produce blueprint arquitectonico completo.

## Procedimiento
1. ELICITAR DOMINIO: ¿Que hace el agente? ¿En que namespace vive? ¿Con que agentes interactua? ¿Que restricciones tiene?
2. MODELAR c (transicion): Identificar modos comportamentales → mapear a estados. Minimo S-DISPATCHER + S-END. Constraints: determinismo, alcanzabilidad, sin ciclos infinitos.
3. MODELAR U (fibras): Definir identidad dialectica(SOUL.md), contexto operador(USER.md). Verificar ortogonalidad entre fibras.
4. MODELAR F (interfaz): Identificar herramientas necesarias. Definir firmas inferenciales(input→output). Routing map si usa kb_route.
5. MODELAR M (efectos): Definir allowed_kb, sandbox mode, tools allow/deny, sub_agents limits.
6. MODELAR W (wiring): ¿Es sub-agente de alguien? ¿Tiene sub-agentes? Declarar adjunciones.
7. IDENTIFICAR SKILLS: Logica >5 pasos → CM. Listar CMs necesarios con proposito y estado que los invoca.
8. Presentar blueprint al usuario: tabla de componentes, diagrama FSM, lista de skills.

## Output
Blueprint arquitectonico: {nombre, namespace, estados[], fibras{soul, user}, tools[], config{}, skills[], adjunciones[]}. Presentar para aprobacion antes de crear.
