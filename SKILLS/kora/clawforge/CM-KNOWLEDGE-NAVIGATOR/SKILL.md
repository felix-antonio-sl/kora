---
_manifest:
  urn: urn:kora:skill:clawforge-knowledge-navigator:1.1.0
  type: lazy_load_endofunctor
extensions:
  ops:
    skill:
      form: extended
      allowed_tools:
        - kb_route
        - oc_docs_search
        - catalog_resolve
      requires: []
      references:
        - references/unix-ubuntu-docs-map.md
        - references/docker-docs-map.md
---

# CM-KNOWLEDGE-NAVIGATOR

## Proposito
Navega tres fuentes de conocimiento (manual KORA curado, docs oficiales OpenClaw, refs locales Unix/Docker basadas en docs oficiales) para responder consultas con precision y citacion obligatoria.

## Input/Output
- **Input:** query: string, capas: string[] (host|docker|openclaw)
- **Output:** KnowledgeResponse (ver Signature Output)

## Procedimiento
1. Clasificar dominio de consulta y resolver fuente primaria:
   - Arquitectura/conceptos/decisiones OpenClaw -> manual KORA via kb_route
   - Detalle API/config/troubleshooting OpenClaw -> oc_docs_search (docs oficiales)
   - Host Unix (SSH, firewall, systemd, APT, networking) -> consultar `references/unix-ubuntu-docs-map.md` y citar el documento oficial Ubuntu correspondiente
   - Docker (images, compose, security, cgroups) -> consultar `references/docker-docs-map.md` y citar el documento oficial Docker correspondiente
2. Jerarquia de fuentes: manual KORA (autoritativo, curado) > docs oficiales OpenClaw > refs locales Unix/Docker basadas en docs oficiales > conocimiento general solo como apoyo explicitamente incierto.
3. Para consultas cross-layer: combinar fuentes de las capas relevantes. Ejemplo: "como funciona sandbox Docker de OpenClaw" -> Cap 7 (aislamiento) + referencia Docker sobre aislamiento/daemon.
4. Sintetizar respuesta con citacion obligatoria: Cap N §S.s o path/URL de doc oficial.
5. Nunca responder host/Docker "de memoria" cuando la afirmacion sea factual u operacional. Si el mapa local no cubre el punto o no identifica una fuente oficial, declarar gap e incertidumbre explicitamente.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| contenido | string | Respuesta sintetizada |
| fuentes | {tipo: manual|docs|unix|docker, referencia: string}[] | Fuentes consultadas con citacion |
| confianza | enum | alta, media, baja |
