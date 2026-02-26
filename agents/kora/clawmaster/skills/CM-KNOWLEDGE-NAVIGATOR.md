---
_manifest:
  urn: "urn:kora:skill:clawmaster-knowledge-navigator:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-KNOWLEDGE-NAVIGATOR

## Proposito
Navega las tres fuentes de conocimiento OpenClaw (manual KORA 26 caps, docs oficiales 200+, codigo fuente) para responder consultas con precision y citacion.

## I/O

- **Input:** consulta: string (pregunta del usuario), dominio_hint: string | null
- **Output:** KnowledgeResponse (ver Signature Output)

## Procedimiento
1. CLASIFICAR DOMINIO de la consulta:

| Dominio | Capitulos KORA | Docs Oficiales |
|---------|---------------|----------------|
| Arquitectura, gateway, agent loop | Cap 1 | docs/concepts/architecture, docs/gateway/ |
| Agentes, workspace, bootstrap, skills, tools | Cap 2 | docs/concepts/agent, docs/tools/ |
| Sesiones, keys, scopes, compaction | Cap 3 | docs/concepts/session |
| Modelos, failover, auth, providers | Cap 4 | docs/providers/, docs/concepts/models |
| Memoria, RAG, embeddings | Cap 5 | docs/concepts/memory |
| Multi-agent, routing, bindings | Cap 6 | docs/concepts/multi-agent |
| Seguridad, sandbox, tool policy | Cap 7, 18 | docs/gateway/security/, docs/security/ |
| Multi-tenant, patrones | Cap 8 | — |
| Sub-agentes, orchestration | Cap 9, 10, 11 | docs/tools/subagents |
| Heartbeats | Cap 12 | docs/gateway/heartbeat, docs/automation/ |
| Cron jobs | Cap 13, 14 | docs/automation/cron-jobs |
| Hooks, webhooks | Cap 15, 16 | docs/automation/hooks, docs/automation/webhook |
| Lobster workflows | Cap 17 | docs/tools/lobster |
| Operaciones, diagnostico | Cap 19 | docs/gateway/doctor, docs/cli/ |
| Patrones, decisiones | Cap 20, 21 | — |
| Multi-gateway, federacion | Cap 22 | docs/gateway/multiple-gateways |
| Instalacion, deploy | — | docs/install/, docs/platforms/ |
| Channels especificos | — | docs/channels/ |
| CLI commands | — | docs/cli/ |
| Web UI | — | docs/web/ |

2. RESOLVER FUENTE: kb_route → capitulo KORA como fuente primaria.
3. COMPLEMENTAR: oc_docs_search si se necesita detalle adicional (config reference, platform-specific, provider-specific).
4. PROFUNDIZAR: oc_repo_search solo si la pregunta requiere entender implementacion.
5. SINTETIZAR respuesta: informacion precisa + cita de fuente(s) + ejemplo si aplica.

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| contenido | string | Respuesta factual sintetizada |
| fuentes | {tipo: enum(kora\|docs\|repo), referencia: string}[] | Fuentes consultadas con citacion |
