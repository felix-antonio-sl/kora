---
_manifest:
  urn: urn:kora:skill:custodio-ingesta-steward:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-INGESTA-STEWARD

## Proposito
Gestiona el pipeline de ingesta del repo KORA usando la interfaz semantica del workspace: monitorea objetos en cada etapa, reporta estado y recomienda acciones.

## Input/Output
- **Input:** (ninguno — escanea pipeline completo)
- **Output:** IngestaReport (ver Signature Output)

## Procedimiento
1. Invocar `intake_pipeline` para capturar el status agregado de cada etapa del pipeline.
2. Si se requiere detalle operativo adicional, invocar `filesystem_scan` sobre `inbox/`, `source/` y `drafts/`.
3. Reportar conteos y objetos visibles por etapa en tabla.
4. Recomendar acciones:
   - inbox -> source: curar manualmente o con instrucciones al operador.
   - source -> drafts: emitir recomendacion estructurada de derivacion a curaduria.
   - drafts -> knowledge: emitir recomendacion estructurada de publicacion via curaduria.
5. Si el usuario aprueba la derivacion, formular la instruccion estructurada correspondiente.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| etapas | {etapa, conteo, objetos, accion_recomendada}[] | Status por etapa del pipeline |
| delegaciones | string[] \| null | Instrucciones para kora/curator si aplica |
