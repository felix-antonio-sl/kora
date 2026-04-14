---
_manifest:
  urn: urn:gn:skill:digitrans-strategic-guide:2.0.0
  type: lazy_load_endofunctor
---

## Proposito
Interpretar estrategias TDE y sus implicaciones institucionales desde la base documental publicada.

## Input/Output
- **Input:** Consulta sobre estrategia TDE (Gobierno Digital 2030, Datos, Identidad Digital, Capacitaciones, Sistema TDE 2025)
- **Output:** Lectura estrategica con objetivos, ejes, implicaciones institucionales y conexion con marco normativo

## Procedimiento
1. Identificar la estrategia o eje estrategico consultado.
2. Resolver via kb_route y catalog_resolve los artefactos estrategicos pertinentes del corpus TDE.
3. Sintetizar objetivos, ejes y metas relevantes a la consulta.
4. Conectar con el marco normativo habilitante cuando corresponda.
5. Delimitar lo que es estrategia documentada de lo que seria interpretacion institucional.

## Signature Output
Lectura estrategica: [estrategia] + [eje/objetivo relevante] + [implicacion institucional] + [marco normativo vinculado].
