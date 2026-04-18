---
_manifest:
  urn: "urn:agengai:kb:namespace-curation-map"
  provenance:
    created_by: "OpenAI Codex (encarnando arquitecto-categorico)"
    created_at: "2026-04-19"
    source: "Curacion H7: mapa canónico del namespace `agengai` para absorber nodos aislados del kb-graph mediante relacion declarada de pertenencia corpus."
version: "1.0.0"
status: publicado
tags: [namespace-map, kb-graph, curation, agengai]
lang: es
extensions:
  kora:
    family: note
relations:
  depends:
    - "urn:kora:kb:knowledge-spec"
  cites:
    - "urn:agengai:kb:00-fundamentos-previos"
    - "urn:agengai:kb:00-toc"
    - "urn:agengai:kb:01-arquitectura-gateway"
    - "urn:agengai:kb:02-agente-unidad-fundamental"
    - "urn:agengai:kb:03-sesiones"
    - "urn:agengai:kb:04-modelos-failover"
    - "urn:agengai:kb:05-memoria"
    - "urn:agengai:kb:06-multi-agent-routing"
    - "urn:agengai:kb:07-aislamiento-seguridad"
    - "urn:agengai:kb:08-patrones-multitenant"
    - "urn:agengai:kb:09-sub-agentes"
    - "urn:agengai:kb:10-sub-agentes-anidados"
    - "urn:agengai:kb:11-comunicacion-inter-sesion"
    - "urn:agengai:kb:12-heartbeats"
    - "urn:agengai:kb:13-cron-jobs"
    - "urn:agengai:kb:14-cron-vs-heartbeat"
    - "urn:agengai:kb:15-hooks"
    - "urn:agengai:kb:16-webhooks"
    - "urn:agengai:kb:17-lobster"
    - "urn:agengai:kb:18-modelo-seguridad"
    - "urn:agengai:kb:19-operaciones"
    - "urn:agengai:kb:20-patrones-diseno"
    - "urn:agengai:kb:21-decisiones-arquitectura"
    - "urn:agengai:kb:22-multi-gateway-docker-federation"
    - "urn:agengai:kb:apendices"
    - "urn:agengai:kb:cheatsheet"
    - "urn:agengai:kb:cheatsheet-p02"
    - "urn:agengai:kb:forjador-especialista-openclaw"
    - "urn:agengai:kb:forjador-openclaw"
    - "urn:agengai:kb:openclaw-integration"
    - "urn:agengai:kb:salubrista-openclaw-spec"
    - "urn:agengai:kb:skills-anthropic"
---

# AGENGAI/Namespace-Curation-Map v1.0.0

## 1. Definicion

Mapa canonico de curacion del namespace `agengai`. Su funcion es declarar una
relacion minima, explicita y auditable entre el namespace y los documentos
publicados que permanecian aislados en `kb-graph`.

## 2. Regla de lectura

Cada arista de `relations.cites` en este documento debe leerse como:

> el artefacto citado pertenece al corpus operativo curado de `agengai` aunque
> aun no tenga una relacion mas fina por familia, supersedes o dependencia.

## 3. Alcance

1. Esta pieza corrige orfandad real por ausencia de aristas declaradas.
2. No reemplaza curacion posterior por familia ni supersedes detallado.
3. No altera el contenido de los documentos citados; solo materializa su
   pertenencia al tejido del namespace.
