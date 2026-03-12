---
_manifest:
  urn: urn:kora:skill:forgemaster-workspace-scaffolder:2.0.0
  type: lazy_load_endofunctor
version: 2.0.0
status: published
lang: es
extensions:
  kora:
    skill:
      form: extended
      allowed_tools:
        - workspace_write
        - workspace_read
      requires: []
      references:
        - references/bootstrap-contract.md
      assets:
        - assets/bootstrap-frontmatter-examples.md
---

# CM-WORKSPACE-SCAFFOLDER

## Proposito
Genera la estructura de directorio completa de un workspace KORA canonico: 5 archivos esenciales + directorio `skills/`, con frontmatter bootstrap valido, `_manifest.type` canonico por componente y topologia lista para materializar Skills degenerados o extendidos, apoyandose en referencias y ejemplos canonicos del repo.

## Input/Output
- **Input:** nombre: string (nombre del agente), namespace: string, blueprint: AgentBlueprint (output de CM-AGENT-DESIGNER)
- **Output:** ScaffoldReport (ver Signature Output)

## Procedimiento
1. Cargar el contrato de bootstrap desde `references/bootstrap-contract.md` y usar `assets/bootstrap-frontmatter-examples.md` como apoyo para la forma minima de manifests y stubs.
2. Validar input: nombre del agente, namespace destino. Verificar que no exista workspace en agents/{namespace}/{nombre}/.
3. Crear directorio: agents/{namespace}/{nombre}/ y agents/{namespace}/{nombre}/skills/.
4. Si el blueprint declara Skills extendidos: crear por cada uno `agents/{namespace}/{nombre}/skills/CM-{id}/` con entrypoint vacio `SKILL.md` y directorios `scripts/`, `references/`, `assets/` solo cuando el blueprint los requiera.
5. Generar AGENTS.md: frontmatter con urn:{namespace}:agent-bootstrap:{nombre}-agents:1.0.0, `_manifest.type=bootstrap_agents` y secciones canonicas (`## 1. FSM`, `## 2. Reglas Duras`, `## 3. Co-induccion`, `## 4. Contexto Multi-turno`, `## 5. Wiring`).
6. Generar SOUL.md: frontmatter con urn:{namespace}:agent-bootstrap:{nombre}-soul:1.0.0, `_manifest.type=bootstrap_soul` y secciones base de identidad, paradigma y tono.
7. Generar USER.md: frontmatter con urn:{namespace}:agent-bootstrap:{nombre}-user:1.0.0, `_manifest.type=bootstrap_user` y secciones base de perfil operador, rutinas y preferencias.
8. Generar TOOLS.md: frontmatter con urn:{namespace}:agent-bootstrap:{nombre}-tools:1.0.0, `_manifest.type=bootstrap_tools` y secciones vacias para cada tool del blueprint.
9. Generar config.json: `_manifest.type=bootstrap_config` + estructura con allowed_kb[], sandbox, tools, sub_agents del blueprint.
10. Verificar topologia: 5 archivos presentes, cada bootstrap con su `_manifest.type` esperado, headings canonicos materializados, directorio `skills/` existente y, si aplica, entrypoints `skills/CM-*/SKILL.md` con fibras adjuntas solo bajo `scripts/`, `references/`, `assets/`.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| archivos_creados | string[] | Lista de archivos generados |
| urns_generados | string[] | URNs asignados a cada componente |
| skills_scaffolded | string[] | Skills degenerados o entrypoints extendidos scaffoldados |
| topologia_valida | bool | True si 5 archivos + skills/ presentes con `bootstrap_*` correcto por componente |
