---
_manifest:
  urn: "urn:kora:agent-bootstrap:forgemaster-tools:2.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string → path: string
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo. Cadena: URN → buscar catalog → extraer file → retornar path.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en turno actual.
- **Notas:** Debe resolver a un artefacto consultable antes de usar conocimiento del repo.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Clasificar tema → resolver URN → priorizar spec, workspace o documento de la Formal Layer.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Agent spec, 5 componentes, FSM, segregacion, co-induccion, agent-spec-md | urn:kora:kb:agent-spec-md |
| Gobernanza, precedencia, meta-reglas, URN bootstrap | urn:kora:kb:gobernanza |
| Formato prescriptivo, grammar, RFC 2119, spec-md | urn:kora:kb:spec-md |
| Formato descriptivo, koraficacion, md-spec | urn:kora:kb:md-spec |
| Skills, CM grammar, Free/Forget, lazy-load y bundles extendidos, skill-spec-md | urn:kora:kb:skill-spec-md |
| Runtime, model routing, deployment, fallback chains, runtime-spec-md | urn:kora:kb:runtime-spec-md |
| Swarms, multi-agent, golden paths, circuit breakers, sentinel, swarm-spec-md | urn:kora:kb:swarm-spec-md |
| Formal layer oficial, fundamentos, formal/00 | urn:kora:kb:cat-foundations |
| Formal layer agente, determinismo, coalgebra, formal/01 | urn:kora:kb:cat-agent-coalgebra |
| Formal layer skills, adjunction, formal/02 | urn:kora:kb:cat-skill-algebra |
| Formal layer ecosistema, 2-category, formal/03 | urn:kora:kb:cat-ecosystem-2cat |
| Formal layer discovery, presheaf, formal/04 | urn:kora:kb:cat-discovery-presheaf |
| Formal layer gobernanza, precedence, formal/05 | urn:kora:kb:cat-governance-lattice |
| Formal layer auditoria, invariants, formal/06 | urn:kora:kb:cat-audit-invariants |
| Formal layer preservacion, compositional preservation, formal/07 | urn:kora:kb:cat-behavioral-preservation |
| Formal layer puente FXSL, formal/08 | urn:kora:kb:cat-fxsl-bridge |

## workspace_read

- **Firma:** agent_path: string → {agents_md, soul_md, user_md, tools_md, config_json, skills}: AgentComponents
- **Cuando usar:** Leer workspace completo de un agente existente para validar, operar, mejorar o deprecar.
- **Cuando NO usar:** Si solo se necesita un componente especifico (usar lectura directa).
- **Notas:** Lectura integral del workspace canónico preservando la separacion entre componentes y la fibra `skills/`, incluyendo skills degenerados `CM-*.md` y entrypoints extendidos `skills/CM-*/SKILL.md`.

## workspace_write

- **Firma:** {componente: string, contenido: string, agent_path: string} → result: string
- **Cuando usar:** Escribir o actualizar un componente del workspace despues de crear, implementar, operar o mejorar.
- **Cuando NO usar:** Si no hay cambios que persistir.
- **Notas:** Respetar segregacion: cada archivo bootstrap contiene exactamente un componente. En `skills/`, el contenido **DEBE** materializarse como `CM-*.md` o `CM-*/SKILL.md` con sus fibras adjuntas dentro del mismo directorio del Skill.

## spec_consult

- **Firma:** document_name: string → content: string
- **Cuando usar:** Consultar specs fundacionales o documentos de la Formal Layer oficial para verificar conformidad, resolver dudas arquitectonicas o comprobar trazas.
- **Cuando NO usar:** Si la informacion ya esta en contexto de sesion.
- **Notas:** Consultar solo las fuentes requeridas para la decision activa y declarar cuando un check depende del baseline publicado en vez de inspeccion directa.

## agent_list

- **Firma:** namespace: string? → agents: {name, path, namespace}[]
- **Cuando usar:** Listar agentes existentes, opcionalmente filtrado por namespace. Util para identificar dependencias, buscar patrones, verificar unicidad de nombres.
- **Cuando NO usar:** Si ya se conoce la ruta exacta del agente.
- **Notas:** Devuelve workspaces resolubles del namespace consultado.

## health_check

- **Firma:** agent_path: string → {result: PASS|FAIL, checks: {id, nombre, veredicto, detalle}[], issues: {severity, component, field, message, fix}[]}
- **Cuando usar:** Ejecutar validacion de conformidad completa contra el baseline publicado de agent-spec-md y skill-spec-md.
- **Cuando NO usar:** Validaciones parciales o consultas rapidas.
- **Notas:** Devuelve un veredicto estructurado de conformidad contra el baseline vigente, incluyendo trazabilidad oficial cuando el envelope o el baseline auditado expone la Formal Layer necesaria. El baseline auditado soporta Skills degenerados y entrypoints extendidos `skills/CM-*/SKILL.md`.
