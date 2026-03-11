---
_manifest:
  urn: urn:kora:skill:forgemaster-workspace-scaffolder:2.0.0
  type: lazy_load_endofunctor
version: 2.0.0
status: published
lang: es
---

# CM-WORKSPACE-SCAFFOLDER

## Proposito
Genera la estructura de directorio completa de un workspace KORA canonico: 5 archivos esenciales + directorio skills/, con frontmatter bootstrap valido, `_manifest.type` canonico por componente y secciones base listas para implementar.

## Input/Output
- **Input:** nombre: string (nombre del agente), namespace: string, blueprint: AgentBlueprint (output de CM-AGENT-DESIGNER)
- **Output:** ScaffoldReport (ver Signature Output)

## Procedimiento
1. Validar input: nombre del agente, namespace destino. Verificar que no exista workspace en agents/{namespace}/{nombre}/.
2. Crear directorio: agents/{namespace}/{nombre}/ y agents/{namespace}/{nombre}/skills/.
3. Generar AGENTS.md: frontmatter con urn:{namespace}:agent-bootstrap:{nombre}-agents:1.0.0, `_manifest.type=bootstrap_agents` y secciones canonicas (`## 1. FSM`, `## 2. Reglas Duras`, `## 3. Co-induccion`, `## 4. Contexto Multi-turno`, `## 5. Wiring`).
4. Generar SOUL.md: frontmatter con urn:{namespace}:agent-bootstrap:{nombre}-soul:1.0.0, `_manifest.type=bootstrap_soul` y secciones base de identidad, paradigma y tono.
5. Generar USER.md: frontmatter con urn:{namespace}:agent-bootstrap:{nombre}-user:1.0.0, `_manifest.type=bootstrap_user` y secciones base de perfil operador, rutinas y preferencias.
6. Generar TOOLS.md: frontmatter con urn:{namespace}:agent-bootstrap:{nombre}-tools:1.0.0, `_manifest.type=bootstrap_tools` y secciones vacias para cada tool del blueprint.
7. Generar config.json: `_manifest.type=bootstrap_config` + estructura con allowed_kb[], sandbox, tools, sub_agents del blueprint.
8. Verificar topologia: 5 archivos presentes, cada bootstrap con su `_manifest.type` esperado, headings canonicos materializados y directorio skills/ existente.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| archivos_creados | string[] | Lista de archivos generados |
| urns_generados | string[] | URNs asignados a cada componente |
| topologia_valida | bool | True si 5 archivos + skills/ presentes con `bootstrap_*` correcto por componente |
