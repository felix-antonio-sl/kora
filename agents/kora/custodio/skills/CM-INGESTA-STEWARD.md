---
_manifest:
  urn: "urn:kora:skill:custodio-ingesta-steward:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-INGESTA-STEWARD

## Proposito
Gestiona el pipeline de ingesta del repo KORA: monitorea objetos en cada etapa (inbox→source→drafts→knowledge), reporta estado y recomienda acciones.

## Procedimiento
1. Ejecutar `scripts/kora intake` → capturar status de cada etapa del pipeline.
2. Escanear inbox/: listar objetos crudos pendientes de curado (PDFs, libros, datasets).
3. Escanear source/: listar extractos curados listos para transformacion.
4. Escanear drafts/: listar artefactos WIP con su status (draft, review).
5. Reportar conteos por etapa en tabla.
6. Recomendar acciones:
   - inbox→source: curar manualmente o con instrucciones al operador.
   - source→drafts: delegar a kora/curator para koraficacion/cristalizacion.
   - drafts→knowledge: delegar a kora/curator para publicacion.
7. Si usuario aprueba delegacion, formular instruccion para kora/curator.

## Output
Reporte pipeline: tabla {etapa, conteo, objetos[], accion_recomendada}. Instrucciones de delegacion si aplica.
