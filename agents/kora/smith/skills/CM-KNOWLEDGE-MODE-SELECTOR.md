---
_manifest:
  urn: "urn:kora:skill:smith-knowledge-mode-selector:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-KNOWLEDGE-MODE-SELECTOR

## Proposito
Selecciona el Knowledge Mode optimo para el agente en construccion, determinando como accede y prioriza fuentes de conocimiento en tiempo de ejecucion.

## Procedimiento
1. Evaluar necesidades de conocimiento del FTCF: dominio cubierto por KBs existentes, necesidad de informacion en tiempo real, nivel de razonamiento inferencial requerido.
2. Aplicar regla de seleccion por prioridad:
   - KB_BASED: dominio cubierto por artefactos curados en catalogo → usar catalog_resolve + kb_route + CM-KB-GUIDANCE.
   - HYBRID_WEB_KB: requiere KB curada + informacion actualizada → catalog + web_search + CM-KNOWLEDGE-ROUTER.
   - WEB_AUGMENTED: dominio dinamico sin KB curada → web_search + CM-WEB-SEARCH.
   - LLM_NATIVE: dominio de razonamiento general sin fuente externa → CM-LLM-BOUNDARY.
3. Para KB_BASED o HYBRID: verificar que los URNs de KB existen en catalog_master_kora.yml.
4. Documentar justificacion del modo seleccionado y los CMs estandar que se activan.
5. Si KB_BASED: listar los URNs concretos del catalogo que el agente debe tener en `allowed_kb`.

## Output
Modo seleccionado (enum), justificacion (2-3 lineas), lista de URNs de KB si aplica, CMs estandar activados por el modo. Listo para alimentar `knowledge_base` namespace y config.json `allowed_kb`.
