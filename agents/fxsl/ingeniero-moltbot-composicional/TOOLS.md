---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:ingeniero-moltbot-composicional-tools:1.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string → path: string
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo. Cadena: URN → buscar catalog → extraer file → retornar path.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en turno actual.
- **Notas:** catalog_master_*.yml = SOURCE_OF_TRUTH. Siempre resolver antes de acceder KB.

## web_search

- **Firma:** query: string → results: SearchResult[]
- **Cuando usar:** Busqueda web para documentacion Moltbot en tiempo real. Policy=WEB_ONLY (artefactos KB locales removidos). Scope: domain_specific. Max results: 3. Freshness: month.
- **Cuando NO usar:** Tema ya resuelto en turno actual. Siempre citar URL fuente.
- **Routing Map:**

| Topic | Ruta Web |
|-------|----------|
| Runtime agentes, sesiones, workspace | concepts/agent-runtime |
| Configuracion Gateway | gateway/gateway |
| Canales (WhatsApp, Telegram, Discord, etc.) | channels/channels |
| Operaciones, instalacion | operations/* |
| Grupos, activation | concepts/groups |
| Seguridad, sandbox | concepts/security |

## artifact_generate

- **Firma:** design: MoltbotDesign → artifacts: MoltbotArtifact[]
- **Cuando usar:** S-ARTIFACT-GENERATION. Consolidar moltbot.json + bootstrap files + guia instalacion.
- **Cuando NO usar:** Diseno no formalizado aun (requiere S-GATEWAY-DESIGN → S-TOOLS-DESIGN primero).
- **Outputs:** moltbot.json, AGENTS.md, SOUL.md, USER.md, TOOLS.md, IDENTITY.md, HEARTBEAT.md (si aplica), guia instalacion, comandos CLI.
