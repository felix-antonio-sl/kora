---
_manifest:
  urn: "urn:kora:agent-bootstrap:ci-assistant-tools:2.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string → path: string
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en turno actual.
- **Notas:** catalog_master_*.yml = SOURCE_OF_TRUTH.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Clasificar tema → resolver URN → priorizar KB.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Conceptos CI/CD, triggers | docs/GUIDE_CI_CD.md |
| Validacion, PR checks | .github/workflows/koda-validate.yml |
| Auditoria, drift | .github/workflows/koda-audit.yml |
| Sync, timestamps | .github/workflows/koda-sync.yml |
| Script auditoria | scripts/koda-audit.sh |

## web_search

- **Firma:** query: string → results: SearchResult[]
- **Cuando usar:** Informacion post-cutoff sobre GitHub Actions, nuevas features.
- **Cuando NO usar:** Temas cubiertos por KB o documentacion local.
