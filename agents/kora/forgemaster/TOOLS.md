---
_manifest:
  urn: "urn:kora:agent-bootstrap:forgemaster-tools:2.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string → path: string
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo. Cadena: URN → buscar catalog → extraer file → retornar path.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en turno actual.
- **Notas:** catalog_master_*.yml = SOURCE_OF_TRUTH. Siempre resolver antes de acceder KB.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Clasificar tema → resolver URN → priorizar KB.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Agent spec, 5 componentes, FSM, segregacion, co-induccion, agent-spec-md | urn:kora:kb:agent-spec-md |
| Gobernanza, precedencia, meta-reglas, URN bootstrap | urn:kora:kb:gobernanza |
| Formato prescriptivo, grammar, RFC 2119, spec-md | urn:kora:kb:spec-md |
| Formato descriptivo, koraficacion, md-spec | urn:kora:kb:md-spec |
| Skills, CM grammar, lazy-load, skill lifecycle, skill-spec-md | urn:kora:kb:skill-spec-md |
| Runtime, model routing, deployment, fallback chains, runtime-spec-md | urn:kora:kb:runtime-spec-md |
| Swarms, multi-agent, golden paths, circuit breakers, sentinel, swarm-spec-md | urn:kora:kb:swarm-spec-md |

## workspace_read

- **Firma:** agent_path: string → {agents_md, soul_md, user_md, tools_md, config_json, skills}: AgentComponents
- **Cuando usar:** Leer workspace completo de un agente existente para validar, operar, mejorar o deprecar.
- **Cuando NO usar:** Si solo se necesita un componente especifico (usar lectura directa).
- **Notas:** Leer todos los archivos del workspace: AGENTS.md, SOUL.md, USER.md, TOOLS.md, config.json, skills/*.md.

## workspace_write

- **Firma:** {componente: string, contenido: string, agent_path: string} → result: string
- **Cuando usar:** Escribir o actualizar un componente del workspace despues de crear, implementar, operar o mejorar.
- **Cuando NO usar:** Si no hay cambios que persistir.
- **Notas:** Respetar segregacion: cada archivo contiene exactamente un componente. Preservar frontmatter _manifest.

## spec_consult

- **Firma:** spec_name: string → content: string
- **Cuando usar:** Consultar specs fundacionales para verificar conformidad o resolver dudas arquitectonicas.
- **Cuando NO usar:** Si la informacion ya esta en contexto de sesion.
- **Notas:** Specs disponibles: agent-spec-md, gobernanza, spec-md, md-spec, skill-spec-md, runtime-spec-md, swarm-spec-md.

## agent_list

- **Firma:** namespace: string? → agents: {name, path, namespace}[]
- **Cuando usar:** Listar agentes existentes, opcionalmente filtrado por namespace. Util para identificar dependencias, buscar patrones, verificar unicidad de nombres.
- **Cuando NO usar:** Si ya se conoce la ruta exacta del agente.
- **Notas:** Escanea agents/{namespace}/ buscando workspaces con AGENTS.md.

## health_check

- **Firma:** agent_path: string → {result: PASS|FAIL, checks: {id, nombre, veredicto, detalle}[], issues: {severity, component, field, message, fix}[]}
- **Cuando usar:** Ejecutar validacion de conformidad completa contra agent-spec-md v7.2.0 (17 checks).
- **Cuando NO usar:** Validaciones parciales o consultas rapidas.
- **Notas:** Invoca internamente CM-AGENT-VALIDATOR v2.0.0. Checklist: 17 checks alineados con agent-spec-md v7.2.0 §9 + skill-spec-md v2.0.0.
