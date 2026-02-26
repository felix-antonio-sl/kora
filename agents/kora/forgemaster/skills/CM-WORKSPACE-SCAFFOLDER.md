---
_manifest:
  urn: "urn:kora:skill:forgemaster-workspace-scaffolder:2.0.0"
  type: "lazy_load_endofunctor"
version: "2.0.0"
status: published
lang: es
---
# CM-WORKSPACE-SCAFFOLDER

## Proposito
Genera la estructura de directorio completa de un workspace KORA canonico: 5 archivos esenciales + directorio skills/, con frontmatter y secciones vacias listas para implementar.

## I/O

- **Input:** nombre: string (nombre del agente), namespace: string, blueprint: AgentBlueprint (output de CM-AGENT-DESIGNER)
- **Output:** ScaffoldReport (ver Signature Output)

## Procedimiento
1. Validar input: nombre del agente, namespace destino. Verificar que no exista workspace en agents/{namespace}/{nombre}/.
2. Crear directorio: agents/{namespace}/{nombre}/ y agents/{namespace}/{nombre}/skills/.
3. Generar AGENTS.md: frontmatter con urn:kora:agent-bootstrap:{nombre}-agents:1.0.0, secciones vacias (FSM, Reglas Duras, Co-induccion, Contexto Multi-turno, Wiring).
4. Generar SOUL.md: frontmatter con urn:kora:agent-bootstrap:{nombre}-soul:1.0.0, secciones vacias (Identidad Dialectica, Paradigma Cognitivo, Tono, Saludo, Estilo, Ejemplos).
5. Generar USER.md: frontmatter con urn:kora:agent-bootstrap:{nombre}-user:1.0.0, secciones vacias (Perfil, Rutinas, Preferencias de Output).
6. Generar TOOLS.md: frontmatter con urn:kora:agent-bootstrap:{nombre}-tools:1.0.0, secciones vacias para cada tool del blueprint.
7. Generar config.json: estructura con allowed_kb[], sandbox, tools, sub_agents del blueprint.
8. Verificar topologia: 5 archivos presentes, frontmatter valido, directorio skills/ existe.

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| archivos_creados | string[] | Lista de archivos generados |
| urns_generados | string[] | URNs asignados a cada componente |
| topologia_valida | bool | True si 5 archivos + skills/ presentes |
