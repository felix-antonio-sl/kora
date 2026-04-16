# Session: 2026-03-31 21:20:10 UTC

- **Session Key**: agent:mente-omega:telegram:direct:7192195698
- **Session ID**: f8d0fa6c-3d5e-417b-b698-2fec1b0f8b40
- **Source**: telegram

## Conversation Summary

user: [Queued messages while agent was busy]

---
Queued #1
Conversation info (untrusted metadata):
```json
{
  "message_id": "232",
  "sender_id": "7192195698",
  "sender": "Ominono",
  "timestamp": "Tue 2026-03-31 22:50 GMT+2"
}
```

Sender (untrusted metadata):
```json
{
  "label": "Ominono (7192195698)",
  "id": "7192195698",
  "name": "Ominono"
}
```

como vamos?
assistant: Estamos bien. El modelo está en versión 4.0b, 2150+ líneas, 25 PE, 35 déficits, 50+ objetos.

Lo que hicimos hoy:
1. Revisión de consistencia interna: 14 correcciones (enum de estados, referencias huérfanas, PE tautológica, firma desincronizada)
2. Absorción de insights FHIR/HaH: nueva §17 con 4 déficits (D32-D35), mapeo FHIR de 11 objetos, fortalezas confirmadas
3. Integración de la planilla de rutas del 31/03: estructura de 4 zonas, tabla de códigos operacionales (CA, CS, TTO EV, KTM, KTR, FONO, VM INGRESO/EGRESO, ING ENF, ING KTR), descubrimiento del ingreso como fan-out multi-profesional, 3 PE nuevas (PE-23 a PE-25)

Lo pendiente: me pediste integrar dos archivos de análisis GPS de rutas y paradas (ene-mar 2026), pero están en tu Mac local, no en el servidor. Necesito que los subas o me pegues el contenido para integrarlos.

El dato GPS sería valioso — agregaría la dimensión espacial-temporal real a la logística de rutas que modelamos desde la planilla. Distancias recorridas, tiempos entre paradas, cobertura geográfica efectiva vs radio teórico de 20 km.

¿Los subes o seguimos con otra cosa?
assistant: Estamos bien. El modelo está en versión 4.0b, 2150+ líneas, 25 PE, 35 déficits, 50+ objetos.

Lo que hicimos hoy:
1. Revisión de consistencia interna: 14 correcciones (enum de estados, referencias huérfanas, PE tautológica, firma desincronizada)
2. Absorción de insights FHIR/HaH: nueva §17 con 4 déficits (D32-D35), mapeo FHIR de 11 objetos, fortalezas confirmadas
3. Integración de la planilla de rutas del 31/03: estructura de 4 zonas, tabla de códigos operacionales (CA, CS, TTO EV, KTM, KTR, FONO, VM INGRESO/EGRESO, ING ENF, ING KTR), descubrimiento del ingreso como fan-out multi-profesional, 3 PE nuevas (PE-23 a PE-25)

Lo pendiente: me pediste integrar dos archivos de análisis GPS de rutas y paradas (ene-mar 2026), pero están en tu Mac local, no en el servidor. Necesito que los subas o me pegues el contenido para integrarlos.

El dato GPS sería valioso — agregaría la dimensión espacial-temporal real a la logística de rutas que modelamos desde la planilla. Distancias recorridas, tiempos entre paradas, cobertura geográfica efectiva vs radio teórico de 20 km.

¿Los subes o seguimos con otra cosa?
user: [Queued messages while agent was busy]

---
Queued #1
Conversation info (untrusted metadata):
```json
{
  "message_id": "230",
  "sender_id": "7192195698",
  "sender": "Ominono",
  "timestamp": "Tue 2026-03-31 22:47 GMT+2"
}
```

Sender (untrusted metadata):
```json
{
  "label": "Ominono (7192195698)",
  "id": "7192195698",
  "name": "Ominono"
}
```

<media:document>
assistant: Felix, veo que enviaste un documento pero no llegó al servidor — el attachment de Telegram no se descargó como archivo accesible. Los archivos que mencionaste (`drives_stops_report...json` y `analisis-rutas-y-paradas-hodom-ene-mar-2026.md`) siguen en tu Mac local.

Para integrarlos necesito que:
1. **Pegues el contenido del .md** directamente en el chat (el análisis de rutas — probablemente cabe)
2. **Para el JSON** (reporte GPS, probablemente grande): un fragmento representativo o resumen de estructura

¿O prefieres copiarlos al servidor vía scp/rsync?
assistant: Felix, veo que enviaste un documento pero no llegó al servidor — el attachment de Telegram no se descargó como archivo accesible. Los archivos que mencionaste (`drives_stops_report...json` y `analisis-rutas-y-paradas-hodom-ene-mar-2026.md`) siguen en tu Mac local.

Para integrarlos necesito que:
1. **Pegues el contenido del .md** directamente en el chat (el análisis de rutas — probablemente cabe)
2. **Para el JSON** (reporte GPS, probablemente grande): un fragmento representativo o resumen de estructura

¿O prefieres copiarlos al servidor vía scp/rsync?
user: [media attached: 6 files]
[media attached 1/6: /home/felix/.openclaw/media/inbound/hd_routes_operational_analysis_2026-01-01_to_2026-03-24---54f498aa-cc05-44a5-b0a8-3ac2e95fffea.xlsx (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet) | /home/felix/.openclaw/media/inbound/hd_routes_operational_analysis_2026-01-01_to_2026-03-24---54f498aa-cc05-44a5-b0a8-3ac2e95fffea.xlsx]
[media attached 2/6: /home/felix/.openclaw/media/inbound/drives_stops_report_2026_01_01_00_00_00_2026_03_25_00_00_00_---c320b66d-7db5-4954-a441-3662447a391e.csv (text/csv) | /home/felix/.openclaw/media/inbound/drives_stops_report_2026_01_01_00_00_00_2026_03_25_00_00_00_---c320b66d-7db5-4954-a441-3662447a391e.csv]
[media attached 3/6: /home/felix/.openclaw/media/inbound/presentacion-marp-dt-hodom-hsc---46967a2b-5bd4-4845-9783-3c784596dd36.md (text/markdown) | /home/felix/.openclaw/media/inbound/presentacion-marp-dt-hodom-hsc---46967a2b-5bd4-4845-9783-3c784596dd36.md]
[media attached 4/6: /home/felix/.openclaw/media/inbound/guion-presentacion-dt-hodom-hsc---8eb903eb-ae93-40ba-8f79-b48b638d1b13.md (text/markdown) | /home/felix/.openclaw/media/inbound/guion-presentacion-dt-hodom-hsc---8eb903eb-ae93-40ba-8f79-b48b638d1b13.md]
[media attached 5/6: /home/felix/.openclaw/media/inbound/consolidado-estrategico-dt-hodom-hsc-2026-03-25---55e82d09-83b0-47da-87ac-00664fe43da3.md (text/markdown) | /home/felix/.openclaw/media/inbound/consolidado-estrategico-dt-hodom-hsc-2026-03-25---55e82d09-83b0-47da-87ac-00664fe43da3.md]
[media attached 6/6: /home/felix/.openclaw/media/inbound/marco-rol-dt-hodom-hsc---a3bb86e5-277c-4653-8bc2-7a7fc43381db.md (text/markdown) | /home/felix/.openclaw/media/inbound/marco-rol-dt-hodom-hsc---a3bb86e5-277c-4653-8bc2-7a7fc43381db.md]
To send an image back, prefer the message tool (media/path/filePath). If you must inline, use MEDIA:https://example.com/image.jpg (spaces ok, quote if needed) or a safe relative path like MEDIA:./image.jpg. Avoid absolute paths (MEDIA:/...) and ~ paths — they are blocked for security. Keep caption in the text body.
Conversation info (untrusted metadata):
```json
{
  "message_id": "241",
  "sender_id": "7192195698",
  "sender": "Ominono",
  "timestamp": "Tue 2026-03-31 22:56 GMT+2"
}
```

Sender (untrusted metadata):
```json
{
  "label": "Ominono (7192195698)",
  "id": "7192195698",
  "name": "Ominono"
}
```

[Telegram Ominono id:7192195698 +2m Tue 2026-03-31 22:56 GMT+2] <media:document>

<file name="drives_stops_report_2026_01_01_00_00_00_2026_03_25_00_00_00_---c320b66d-7db5-4954-a441-3662447a391e.csv" mime="text/csv">
Dispositivo:,PFFF57- RICARDO ALVIAL,,
Estado,Comienzo,Fin,Duración,Ralentí del motor,Conductor,Posición de parada,Consumo de combustible
Longitud de ruta,Velocidad máxima,Velocidad media
Detenido,2026-01-01 08:18:31,2026-01-01 09:05:35,47min 4s,0s,,"-36.430104, -71.959675",
Movimiento,2026-01-01 09:05:35,2026-01-01 09:08:57,3min 22s,0s,,1.12 Km,41 kph,29 kph,
Detenido,2026-01-01 09:08:57,2026-01-01 09:18:28,9min 31s,0s,,"-36.431717, -71.965235",
Movimiento,2026-01-01 09:18:28,2026-01-01 09:21:03,2min 35s,0s,,1.44 Km,60 kph,37 kph,
Detenido,2026-01-01 09:21:03,2026-01-01 09:33:05,12min 2s,0s,,"-36.424091, -71.96827",
Movimiento,2026-01-01 09:33:05,2026-01-01 09:36:07,3min 2s,0s,,0.83 Km,17 kph,10 kph,
Detenido,2026-01-01 09:36:07,2026-01-01 09:43:10,7min 3s,0s,,"-36.423326, -71.974321",
Movimiento,2026-01-01 09:43:10,2026-01-01 09:48:13,5min 3s,0s,,1.64 Km,42 kph,22 kph,
Detenido,2026-01-01 09:48:13,2026-01-01 10:11:05,22min 52s,0s,,"-36.417333, -71.960944",
Movimiento,2026-01-01 10:11:05,2026-01-01 10:15:00,3min 55s,0s,,1.64 Km,33 kph,22 kph,
Detenido,2026-01-01 10:15:00,2026-01-01 10:18:59,3min 59s,0s,,"-36.430143, -71.959665",
Movimiento,2026-01-01 10:18:59,2026-01-01 10:21:28,2min 29s,0s,,0.62 Km,33 kph,18 kph,
Detenido,2026-01-01 10:21:28,2026-01-01 10:42:08,20min 40s,0s,,"-36.431991, -71.953177",
Movimiento,2026-01-01 10:42:08,2026-01-01 10:47:10,5min 2s,0s,,3.11 Km,62 kph,41 kph,
Detenido,2026-01-01 10:47:10,2026-01-01 11:05:38,18min 28s,0s,,"-36.43454, -71.92876",
Movimiento,2026-01-01 11:05:38,2026-01-01 11:24:17,18min 39s,0s,,15.69 Km,85 kph,49 kph,
Detenido,2026-01-01 11:24:17,2026-01-01 11:46:27,22min 10s,0s,,"-36.49041, -71.857831",
Movimiento,2026-01-01 11:46:27,2026-01-01 12:04:40,18min 13s,0s,,16.03 Km,104 kph,57 kph,
Detenido,2026-01-01 12:04:40,2026-01-01 12:20:41,16min 1s,0s,,"-36.404677, -71.802507",
Movimiento,2026-01-01 12:20:41,2026-01-01 12:33:17,12min 36s,0s,,12.38 Km,91 kph,59 kph,
Detenido,2026-01-01 12:33:17,2026-01-01 12:44:39,11min 22s,58s,,"-36.353832, -71.854262",
Movimiento,2026-01-01 12:44:39,2026-01-01 13:00:17,15min 38s,0s,,13.68 Km,112 kph,54 kph,
Detenido,2026-01-01 13:00:17,2026-01-01 13:10:25,10min 8s,0s,,"-36.428561, -71.960289",
Movimiento,2026-01-01 13:10:25,2026-01-01 13:11:55,1min 30s,0s,,0.12 Km,32 kph,29 kph,
Detenido,2026-01-01 13:11:55,2026-01-01 13:12:56,1min 1s,0s,,"-36.430075, -71.959637",
Movimiento,2026-01-01 13:12:56,2026-01-01 13:14:57,2min 1s,0s,,0.2 Km,29 kph,18 kph,
Detenido,2026-01-01 13:14:57,2026-01-02 08:24:17,19h 9min 20s,0s,,"-36.429295, -71.959506",
Movimiento,2026-01-02 08:24:17,2026-01-02 08:27:19,3min 2s,0s,,1.18 Km,52 kph,44 kph,
Detenido,2026-01-02 08:27:19,2026-01-02 08:27:49,30s,0s,,"-36.425913, -71.949392",
Movimiento,2026-01-02 08:27:49,2026-01-02 08:36:50,9min 1s,37s,,12.35 Km,108 kph,75 kph,
Detenido,2026-01-02 08:36:50,2026-01-02 09:01:24,24min 34s,34s,,"-36.354031, -71.853589",
Movimiento,2026-01-02 09:01:24,2026-01-02 09:13:10,11min 46s,0s,,8.84 Km,76 kph,48 kph,
Detenido,2026-01-02 09:13:10,2026-01-02 09:46:28,33min 18s,0s,,"-36.404817, -71.802535",
Movimiento,2026-01-02 09:46:28,2026-01-02 10:00:35,14min 7s,1min 26s,,13.76 Km,78 kph,60 kph,
Detenido,2026-01-02 10:00:35,2026-01-02 10:37:35,37min 0s,1min 31s,,"-36.434358, -71.928639",
Movimiento,2026-01-02 10:37:35,2026-01-02 10:41:37,4min 2s,0s,,1.55 Km,42 kph,30 kph,
Detenido,2026-01-02 10:41:37,2026-01-02 10:42:37,1min 0s,0s,,"-36.428717, -71.949112",
Movimiento,2026-01-02 10:42:37,2026-01-02 10:47:40,5min 3s,0s,,3.03 Km,69 kph,37 kph,
Detenido,2026-01-02 10:47:40,2026-01-02 11:28:36,40min 56s,0s,,"-36.432076, -71.953228",
Movimiento,2026-01-02 11:28:36,2026-01-02 11:30:35,1min 59s,0s,,0 Km,8 kph,8 kph,
Detenido,2026-01-02 11:30:35,2026-01-02 11:31:37,1min 2s,0s,,"-36.425707, -71.951099",
Movimiento,2026-01-02 11:31:37,2026-01-02 11:36:37,5min 0s,0s,,1.6 Km,32 kph,21 kph,
Detenido,2026-01-02 11:36:37,2026-01-02 12:13:08,36min 31s,0s,,"-36.417318, -71.960967",
Movimiento,2026-01-02 12:13:08,2026-01-02 12:18:41,5min 33s,0s,,1.13 Km,34 kph,23 kph,
Detenido,2026-01-02 12:18:41,2026-01-02 12:21:05,2min 24s,0s,,"-36.425158, -71.955766",
Movimiento,2026-01-02 12:21:05,2026-01-02 12:25:44,4min 39s,0s,,0.61 Km,14 kph,11 kph,
Detenido,2026-01-02 12:25:44,2026-01-02 12:29:15,3min 31s,0s,,"-36.426928, -71.957228",
Movimiento,2026-01-02 12:29:15,2026-01-02 12:32:16,3min 1s,30s,,0.6 Km,20 kph,15 kph,
Detenido,2026-01-02 12:32:16,2026-01-02 15:06:45,2h 34min 29s,0s,,"-36.43011, -71.959653",
Movimiento,2026-01-02 15:06:45,2026-01-02 15:11:52,5min 7s,0s,,0.87 Km,25 kph,14 kph,
Detenido,2026-01-02 15:11:52,2026-01-02 15:13:05,1min 13s,0s,,"-36.433478, -71.966334",
Movimiento,2026-01-02 15:13:05,2026-01-02 15:15:54,2min 49s,0s,,1.32 Km,35 kph,22 kph,
Detenido,2026-01-02 15:15:54,2026-01-02 15:47:41,31min 47s,0s,,"-36.423581, -71.967949",
Movimiento,2026-01-02 15:47:41,2026-01-02 15:49:12,1min 31s,0s,,0.16 Km,17 kph,15 kph,
Detenido,2026-01-02 15:49:12,2026-01-02 16:22:51,33min 39s,0s,,"-36.423329, -71.9743",
Movimiento,2026-01-02 16:22:51,2026-01-02 16:27:04,4min 13s,1min 0s,,1.19 Km,33 kph,23 kph,
Detenido,2026-01-02 16:27:04,2026-01-02 16:31:09,4min 5s,0s,,"-36.432843, -71.969094",
Movimiento,2026-01-02 16:31:09,2026-01-02 16:35:39,4min 30s,0s,,0.99 Km,25 kph,15 kph,
Detenido,2026-01-02 16:35:39,2026-01-03 08:20:46,15h 45min 7s,0s,,"-36.43021, -71.959869",
Movimiento,2026-01-03 08:20:46,2026-01-03 08:24:43,3min 57s,0s,,1.31 Km,30 kph,21 kph,
Detenido,2026-01-03 08:24:43,2026-01-03 08:25:43,1min 0s,0s,,"-36.42597, -71.949092",
Movimiento,2026-01-03 08:25:43,2026-01-03 08:32:47,7min 4s,0s,,9.9 Km,98 kph,91 kph,
Detenido,2026-01-03 08:32:47,2026-01-03 08:36:50,4min 3s,0s,,"-36.357629, -71.871334",
Movimiento,2026-01-03 08:36:50,2026-01-03 08:42:22,5min 32s,0s,,3.45 Km,94 kph,40 kph,
Detenido,2026-01-03 08:42:22,2026-01-03 09:09:49,27min 27s,0s,,"-36.353845, -71.854222",
Movimiento,2026-01-03 09:09:49,2026-01-03 09:19:14,9min 25s,4min 3s,,5.01 Km,59 kph,34 kph,
Detenido,2026-01-03 09:19:14,2026-01-03 09:52:39,33min 25s,4min 33s,,"-36.332295, -71.813976",
Movimiento,2026-01-03 09:52:39,2026-01-03 10:01:32,8min 53s,0s,,10.16 Km,71 kph,57 kph,
Detenido,2026-01-03 10:01:32,2026-01-03 10:15:09,13min 37s,0s,,"-36.404829, -71.802531",
Movimiento,2026-01-03 10:15:09,2026-01-03 10:29:16,14min 7s,0s,,7.71 Km,62 kph,34 kph,
Detenido,2026-01-03 10:29:16,2026-01-03 10:47:54,18min 38s,0s,,"-36.405148, -71.868514",
Movimiento,2026-01-03 10:47:54,2026-01-03 10:52:25,4min 31s,0s,,3.83 Km,75 kph,65 kph,
Detenido,2026-01-03 10:52:25,2026-01-03 10:54:50,2min 25s,0s,,"-36.413313, -71.902688",
Movimiento,2026-01-03 10:54:50,2026-01-03 11:06:32,11min 42s,9s,,6.44 Km,61 kph,31 kph,
Detenido,2026-01-03 11:06:32,2026-01-03 11:15:41,9min 9s,0s,,"-36.430164, -71.959986",
Movimiento,2026-01-03 11:15:41,2026-01-03 11:19:43,4min 2s,0s,,1.31 Km,39 kph,23 kph,
Detenido,2026-01-03 11:19:43,2026-01-03 11:23:15,3min 32s,0s,,"-36.425724, -71.950444",
Movimiento,2026-01-03 11:23:15,2026-01-03 11:48:57,25min 42s,0s,,23.24 Km,104 kph,51 kph,
Detenido,2026-01-03 11:48:57,2026-01-03 12:15:46,26min 49s,0s,,"-36.478992, -71.714502",
Movimiento,2026-01-03 12:15:46,2026-01-03 12:34:24,18min 38s,0s,,13.89 Km,92 kph,48 kph,
Detenido,2026-01-03 12:34:24,2026-01-03 12:35:24,1min 0s,0s,,"-36.450102, -71.837499",
Movimiento,2026-01-03 12:35:24,2026-01-03 12:36:25,1min 1s,0s,,0.01 Km,13 kph,13 kph,
Detenido,2026-01-03 12:36:25,2026-01-03 12:58:41,22min 16s,0s,,"-36.450125, -71.837546",
Movimiento,2026-01-03 12:58:41,2026-01-03 13:12:21,13min 40s,30s,,16.85 Km,103 kph,69 kph,
Detenido,2026-01-03 13:12:21,2026-01-03 13:34:33,22min 12s,0s,,"-36.450209, -71.95388",
Movimiento,2026-01-03 13:34:33,2026-01-03 13:40:36,6min 3s,0s,,4.29 Km,76 kph,37 kph,
Detenido,2026-01-03 13:40:36,2026-01-03 15:45:54,2h 5min 18s,0s,,"-36.430149, -71.9596",
Movimiento,2026-01-03 15:45:54,2026-01-03 15:49:24,3min 30s,30s,,0.58 Km,27 kph,17 kph,
Detenido,2026-01-03 15:49:24,2026-01-03 15:50:55,1min 31s,1min 31s,,"-36.424532, -71.957168",
Movimiento,2026-01-03 15:50:55,2026-01-03 15:53:56,3min 1s,0s,,0.86 Km,39 kph,28 kph,
Detenido,2026-01-03 15:53:56,2026-01-03 16:31:08,37min 12s,0s,,"-36.417356, -71.960932",
Movimiento,2026-01-03 16:31:08,2026-01-03 16:36:45,5min 37s,0s,,1.84 Km,49 kph,26 kph,
Detenido,2026-01-03 16:36:45,2026-01-03 16:38:40,1min 55s,0s,,"-36.425963, -71.948507",
Movimiento,2026-01-03 16:38:40,2026-01-03 16:41:46,3min 6s,0s,,1.05 Km,33 kph,28 kph,
Detenido,2026-01-03 16:41:46,2026-01-03 16:48:50,7min 4s,0s,,"-36.431873, -71.936826",
Movimiento,2026-01-03 16:48:50,2026-01-03 16:49:49,59s,0s,,0.52 Km,50 kph,50 kph,
Detenido,2026-01-03 16:49:49,2026-01-03 17:26:48,36min 59s,31s,,"-36.434548, -71.928775",
Movimiento,2026-01-03 17:26:48,2026-01-03 17:30:19,3min 31s,0s,,1.59 Km,32 kph,29 kph,
Detenido,2026-01-03 17:30:19,2026-01-03 17:33:20,3min 1s,0s,,"-36.426922, -71.94395",
Movimiento,2026-01-03 17:33:20,2026-01-03 17:36:22,3min 2s,0s,,1.29 Km,41 kph,24 kph,
Detenido,2026-01-03 17:36:22,2026-01-03 17:43:27,7min 5s,0s,,"-36.428578, -71.960348",
Movimiento,2026-01-03 17:43:27,2026-01-03 17:45:26,1min 59s,0s,,0.19 Km,17 kph,12 kph,
Detenido,2026-01-03 17:45:26,2026-01-03 17:47:55,2min 29s,46s,,"-36.430142, -71.959644",
Movimiento,2026-01-03 17:47:55,2026-01-03 17:50:30,2min 35s,0s,,0.19 Km,22 kph,10 kph,
Detenido,2026-01-03 17:50:30,2026-01-03 18:07:01,16min 31s,0s,,"-36.429295, -71.959455",
Movimiento,2026-01-03 18:07:01,2026-01-03 18:07:38,37s,0s,,0 Km,6 kph,6 kph,
Detenido,2026-01-03 18:07:38,2026-01-03 18:49:09,41min 31s,0s,,"-36.429269, -71.959543",
Movimiento,2026-01-03 18:49:09,2026-01-03 18:49:53,44s,20s,,0.15 Km,29 kph,29 kph,
Detenido,2026-01-03 18:49:53,2026-01-04 09:04:55,14h 15min 2s,0s,,"-36.430063, -71.960622",
Movimiento,2026-01-04 09:04:55,2026-01-04 09:07:48,2min 53s,0s,,1.33 Km,59 kph,31 kph,
Detenido,2026-01-04 09:07:48,2026-01-04 09:08:49,1min 1s,0s,,"-36.425939, -71.949281",
Movimiento,2026-01-04 09:08:49,2026-01-04 09:17:55,9min 6s,0s,,12 Km,130 kph,83 kph,
Detenido,2026-01-04 09:17:55,2026-01-04 09:50:27,32min 32s,0s,,"-36.353835, -71.854276",
Movimiento,2026-01-04 09:50:27,2026-01-04 09:57:17,6min 50s,29s,,5.72 Km,90 kph,52 kph,
Detenido,2026-01-04 09:57:17,2026-01-04 10:36:23,39min 6s,0s,,"-36.335224, -71.812857",
Movimiento,2026-01-04 10:36:23,2026-01-04 10:51:31,15min 8s,14s,,14.79 Km,97 kph,56 kph,
Detenido,2026-01-04 10:51:31,2026-01-04 11:28:58,37min 27s,28s,,"-36.405153, -71.868469",
Movimiento,2026-01-04 11:28:58,2026-01-04 11:45:07,16min 9s,0s,,11.35 Km,94 kph,45 kph,
Detenido,2026-01-04 11:45:07,2026-01-04 11:52:01,6min 54s,0s,,"-36.430005, -71.959695",
Movimiento,2026-01-04 11:52:01,2026-01-04 11:53:42,1min 41s,0s,,0.56 Km,56 kph,32 kph,
Detenido,2026-01-04 11:53:42,2026-01-04 12:09:49,16min 7s,17s,,"-36.431969, -71.953191",
Movimiento,2026-01-04 12:09:49,2026-01-04 12:12:04,2min 15s,0s,,0.14 Km,33 kph,12 kph,
Detenido,2026-01-04 12:12:04,2026-01-04 12:12:07,3s,0s,,"-36.425777, -71.950036",
Movimiento,2026-01-04 12:12:07,2026-01-04 12:16:36,4min 29s,5s,,2.75 Km,46 kph,30 kph,
Detenido,2026-01-04 12:16:36,2026-01-04 12:38:53,22min 17s,0s,,"-36.434494, -71.928755",
Movimiento,2026-01-04 12:38:53,2026-01-04 12:43:25,4min 32s,0s,,2.62 Km,77 kph,35 kph,
Detenido,2026-01-04 12:43:25,2026-01-04 12:44:26,1min 1s,0s,,"-36.42611, -71.948223",
Movimiento,2026-01-04 12:44:26,2026-01-04 12:50:28,6min 2s,0s,,2.14 Km,42 kph,21 kph,
Detenido,2026-01-04 12:50:28,2026-01-04 12:59:02,8min 34s,0s,,"-36.417315, -71.96094",
Movimiento,2026-01-04 12:59:02,2026-01-04 13:01:34,2min 32s,0s,,0.93 Km,29 kph,20 kph,
Detenido,2026-01-04 13:01:34,2026-01-04 13:03:05,1min 31s,1min 1s,,"-36.425723, -71.962362",
Movimiento,2026-01-04 13:03:05,2026-01-04 13:04:05,1min 0s,8s,,0.55 Km,21 kph,14 kph,
Detenido,2026-01-04 13:04:05,2026-01-04 14:21:49,1h 17min 44s,0s,,"-36.430123, -71.959603",
Movimiento,2026-01-04 14:21:49,2026-01-04 14:27:33,5min 44s,0s,,2.39 Km,47 kph,24 kph,
Detenido,2026-01-04 14:27:33,2026-01-04 14:32:33,5min 0s,0s,,"-36.424052, -71.968356",
Movimiento,2026-01-04 14:32:33,2026-01-04 14:38:05,5min 32s,0s,,1.92 Km,62 kph,24 kph,
Detenido,2026-01-04 14:38:05,2026-01-04 15:59:05,1h 21min 0s,0s,,"-36.430168, -71.959642",
Movimiento,2026-01-04 15:59:05,2026-01-04 16:03:08,4min 3s,0s,,1.25 Km,41 kph,22 kph,
Detenido,2026-01-04 16:03:08,2026-01-04 16:18:08,15min 0s,0s,,"-36.431725, -71.965199",
Movimiento,2026-01-04 16:18:08,2026-01-04 16:21:40,3min 32s,0s,,1.56 Km,34 kph,23 kph,
Detenido,2026-01-04 16:21:40,2026-01-04 17:02:15,40min 35s,0s,,"-36.424103, -71.968294",
Movimiento,2026-01-04 17:02:15,2026-01-04 17:07:14,4min 59s,0s,,1.96 Km,49 kph,31 kph,
Detenido,2026-01-04 17:07:14,2026-01-04 17:23:51,16min 37s,0s,,"-36.430189, -71.959572",
Movimiento,2026-01-04 17:23:51,2026-01-04 17:37:36,13min 45s,0s,,4.03 Km,53 kph,33 kph,
Detenido,2026-01-04 17:37:36,2026-01-04 17:51:33,13min 57s,0s,,"-36.450201, -71.953747",
Movimiento,2026-01-04 17:51:33,2026-01-04 17:57:31,5min 58s,30s,,3.48 Km,102 kph,43 kph,
Detenido,2026-01-04 17:57:31,2026-01-05 08:14:53,14h 17min 22s,58s,,"-36.43014, -71.959621",
Movimiento,2026-01-05 08:14:53,2026-01-05 08:37:07,22min 14s,0s,,18.17 Km,94 kph,51 kph,
Detenido,2026-01-05 08:37:07,2026-01-05 08:39:09,2min 2s,0s,,"-36.329843, -72.060541",
Movimiento,2026-01-05 08:39:09,2026-01-05 08:48:43,9min 34s,0s,,1.95 Km,30 kph,13 kph,
Detenido,2026-01-05 08:48:43,2026-01-05 08:50:11,1min 28s,0s,,"-36.341076, -72.070674",
Movimiento,2026-01-05 08:50:11,2026-01-05 08:54:04,3min 53s,0s,,0.08 Km,15 kph,15 kph,
Detenido,2026-01-05 08:54:04,2026-01-05 09:52:09,58min 5s,2s,,"-36.340973, -72.069722",
Movimiento,2026-01-05 09:52:09,2026-01-05 09:52:21,12s,0s,,0 Km,6 kph,6 kph,
Detenido,2026-01-05 09:52:21,2026-01-05 09:53:47,1min 26s,0s,,"-36.341094, -72.070708",
Movimiento,2026-01-05 09:53:47,2026-01-05 10:02:56,9min 9s,0s,,1.82 Km,33 kph,17 kph,
Detenido,2026-01-05 10:02:56,2026-01-05 10:03:56,1min 0s,0s,,"-36.329823, -72.060527",
Movimiento,2026-01-05 10:03:56,2026-01-05 10:05:56,2min 0s,0s,,0.54 Km,29 kph,25 kph,
Detenido,2026-01-05 10:05:56,2026-01-05 10:06:51,55s,0s,,"-36.321246, -72.054313",
Movimiento,2026-01-05 10:06:51,2026-01-05 10:25:24,18min 33s,1min 52s,,17.05 Km,104 kph,63 kph,
Detenido,2026-01-05 10:25:24,2026-01-05 11:07:28,42min 4s,0s,,"-36.430199, -71.959881",
Movimiento,2026-01-05 11:07:28,2026-01-05 11:25:35,18min 7s,0s,,22.35 Km,118 kph,66 kph,
Detenido,2026-01-05 11:25:35,2026-01-05 11:41:41,16min 6s,0s,,"-36.488934, -72.111092",
Movimiento,2026-01-05 11:41:41,2026-01-05 11:52:40,10min 59s,0s,,8.88 Km,99 kph,54 kph,
Detenido,2026-01-05 11:52:40,2026-01-05 11:54:56,2min 16s,0s,,"-36.521388, -72.046251",
Movimiento,2026-01-05 11:54:56,2026-01-05 11:55:12,16s,0s,,0.03 Km,9 kph,9 kph,
Detenido,2026-01-05 11:55:12,2026-01-05 12:01:34,6min 22s,0s,,"-36.521499, -72.046199",
Movimiento,2026-01-05 12:01:34,2026-01-05 12:15:01,13min 27s,1min 1s,,15.55 Km,117 kph,61 kph,
Detenido,2026-01-05 12:15:01,2026-01-05 12:31:54,16min 53s,0s,,"-36.450208, -71.953832",
Movimiento,2026-01-05 12:31:54,2026-01-05 12:36:56,5min 2s,0s,,3.43 Km,104 kph,58 kph,
Detenido,2026-01-05 12:36:56,2026-01-05 12:52:35,15min 39s,0s,,"-36.431719, -71.965226",
Movimiento,2026-01-05 12:52:35,2026-01-05 12:55:06,2min 31s,0s,,0.58 Km,31 kph,26 kph,
Detenido,2026-01-05 12:55:06,2026-01-05 13:08:39,13min 33s,0s,,"-36.427649, -71.96012",
Movimiento,2026-01-05 13:08:39,2026-01-05 13:09:39,1min 0s,0s,,0.16 Km,17 kph,16 kph,
Detenido,2026-01-05 13:09:39,2026-01-05 14:38:23,1h 28min 44s,0s,,"-36.430081, -71.959688",
Movimiento,2026-01-05 14:38:23,2026-01-05 14:39:54,1min 31s,1min 26s,,0.1 Km,21 kph,19 kph,
Detenido,2026-01-05 14:39:54,2026-01-05 15:44:09,1h 4min 15s,4min 2s,,"-36.429295, -71.959522",
Movimiento,2026-01-05 15:44:09,2026-01-05 15:45:38,1min 29s,0s,,0.16 Km,27 kph,23 kph,
Detenido,2026-01-05 15:45:38,2026-01-06 11:03:14,19h 17min 36s,37s,,"-36.430088, -71.959599",
Movimiento,2026-01-06 11:03:14,2026-01-06 11:10:16,7min 2s,0s,,1.31 Km,39 kph,15 kph,
Detenido,2026-01-06 11:10:16,2026-01-06 11:22:21,12min 5s,30s,,"-36.421148, -71.960335",
Movimiento,2026-01-06 11:22:21,2026-01-06 11:25:22,3min 1s,0s,,0.81 Km,22 kph,9 kph,
Detenido,2026-01-06 11:25:22,2026-01-06 11:36:55,11min 33s,7s,,"-36.430078, -71.95964",
Movimiento,2026-01-06 11:36:55,2026-01-06 11:50:24,13min 29s,0s,,8.41 Km,112 kph,46 kph,
Detenido,2026-01-06 11:50:24,2026-01-06 12:13:16,22min 52s,49s,,"-36.473439, -72.014978",
Movimiento,2026-01-06 12:13:16,2026-01-06 12:27:34,14min 18s,0s,,14.05 Km,107 kph,61 kph,
Detenido,2026-01-06 12:27:34,2026-01-06 12:50:36,23min 2s,0s,,"-36.488867, -72.111121",
Movimiento,2026-01-06 12:50:36,2026-01-06 12:55:21,4min 45s,1min 30s,,2.08 Km,71 kph,52 kph,
Detenido,2026-01-06 12:55:21,2026-01-06 12:56:13,52s,52s,,"-36.519585, -72.096011",
Movimiento,2026-01-06 12:56:13,2026-01-06 13:13:28,17min 15s,0s,,17.68 Km,109 kph,61 kph,
Detenido,2026-01-06 13:13:28,2026-01-06 13:31:02,17min 34s,30s,,"-36.450209, -71.953794",
Movimiento,2026-01-06 13:31:02,2026-01-06 13:37:44,6min 42s,0s,,3.65 Km,70 kph,46 kph,
Detenido,2026-01-06 13:37:44,2026-01-06 15:46:41,2h 8min 57s,43s,,"-36.430139, -71.959903",
Movimiento,2026-01-06 15:46:41,2026-01-06 15:49:30,2min 49s,0s,,1.12 Km,20 kph,12 kph,
Detenido,2026-01-06 15:49:30,2026-01-06 15:52:40,3min 10s,0s,,"-36.426925, -71.951481",
Movimiento,2026-01-06 15:52:40,2026-01-06 16:02:24,9min 44s,35s,,12.63 Km,110 kph,70 kph,
Detenido,2026-01-06 16:02:24,2026-01-06 16:36:53,34min 29s,30s,,"-36.353949, -71.853842",
Movimiento,2026-01-06 16:36:53,2026-01-06 16:48:57,12min 4s,0s,,3.64 Km,77 kph,52 kph,
Detenido,2026-01-06 16:48:57,2026-01-06 16:59:03,10min 6s,2min 1s,,"-36.332128, -71.813814",
Movimiento,2026-01-06 16:59:03,2026-01-06 17:27:17,28min 14s,0s,,23.64 Km,97 kph,52 kph,
Detenido,2026-01-06 17:27:17,2026-01-06 17:48:56,21min 39s,0s,,"-36.479014, -71.714481",
Movimiento,2026-01-06 17:48:56,2026-01-06 18:05:11,16min 15s,1min 8s,,14.16 Km,101 kph,51 kph,
Detenido,2026-01-06 18:05:11,2026-01-06 18:05:34,23s,23s,,"-36.451692, -71.839447",
Movimiento,2026-01-06 18:05:34,2026-01-06 18:06:04,30s,0s,,0.17 Km,23 kph,23 kph,
Detenido,2026-01-06 18:06:04,2026-01-06 18:20:05,14min 1s,0s,,"-36.45013, -71.837489",
Movimiento,2026-01-06 18:20:05,2026-01-06 18:22:06,2min 1s,0s,,0.01 Km,10 kph,10 kph,
Detenido,2026-01-06 18:22:06,2026-01-06 18:29:47,7min 41s,0s,,"-36.450051, -71.837452",
Movimiento,2026-01-06 18:29:47,2026-01-06 18:40:58,11min 11s,0s,,9.74 Km,75 kph,54 kph,
Detenido,2026-01-06 18:40:58,2026-01-06 18:41:06,8s,0s,,"-36.428727, -71.94917",
Movimiento,2026-01-06 18:41:06,2026-01-06 18:46:29,5min 23s,0s,,2.92 Km,64 kph,34 kph,
Detenido,2026-01-06 18:46:29,2026-01-07 08:28:00,13h 41min 31s,0s,,"-36.430172, -71.959641",
Movimiento,2026-01-07 08:28:00,2026-01-07 08:29:00,1min 0s,0s,,0.35 Km,29 kph,25 kph,
Detenido,2026-01-07 08:29:00,2026-01-07 08:30:01,1min 1s,0s,,"-36.430747, -71.956021",
Movimiento,2026-01-07 08:30:01,2026-01-07 08:32:01,2min 0s,30s,,0.93 Km,34 kph,27 kph,
Detenido,2026-01-07 08:32:01,2026-01-07 08:37:03,5min 2s,31s,,"-36.424608, -71.949538",
Movimiento,2026-01-07 08:37:03,2026-01-07 08:40:54,3min 51s,0s,,0.22 Km,66 kph,38 kph,
Detenido,2026-01-07 08:40:54,2026-01-07 08:42:36,1min 42s,39s,,"-36.422833, -71.950098",
Movimiento,2026-01-07 08:42:36,2026-01-07 08:44:21,1min 45s,29s,,0.35 Km,27 kph,17 kph,
Detenido,2026-01-07 08:44:21,2026-01-07 08:57:37,13min 16s,0s,,"-36.424571, -71.949432",
Movimiento,2026-01-07 08:57:37,2026-01-07 09:10:35,12min 58s,1min 18s,,9.53 Km,84 kph,44 kph,
Detenido,2026-01-07 09:10:35,2026-01-07 09:12:06,1min 31s,0s,,"-36.358141, -71.980353",
Movimiento,2026-01-07 09:12:06,2026-01-07 09:14:37,2min 31s,0s,,0.71 Km,19 kph,17 kph,
Detenido,2026-01-07 09:14:37,2026-01-07 09:46:25,31min 48s,0s,,"-36.363243, -71.982324",
Movimiento,2026-01-07 09:46:25,2026-01-07 09:58:24,11min 59s,0s,,8.49 Km,79 kph,47 kph,
Detenido,2026-01-07 09:58:24,2026-01-07 10:00:35,2min 11s,0s,,"-36.414624, -71.969252",
Movimiento,2026-01-07 10:00:35,2026-01-07 10:07:59,7min 24s,0s,,2.26 Km,45 kph,31 kph,
Detenido,2026-01-07 10:07:59,2026-01-07 10:21:15,13min 16s,0s,,"-36.430108, -71.959617",
Movimiento,2026-01-07 10:21:15,2026-01-07 10:30:42,9min 27s,0s,,8.86 Km,107 kph,55 kph,
Detenido,2026-01-07 10:30:42,2026-01-07 10:31:12,30s,0s,,"-36.473558, -72.014387",
Movimiento,2026-01-07 10:31:12,2026-01-07 10:31:42,30s,0s,,0.04 Km,11 kph,11 kph,
Detenido,2026-01-07 10:31:42,2026-01-07 10:53:56,22min 14s,30s,,"-36.473425, -72.014993",
Movimiento,2026-01-07 10:53:56,2026-01-07 10:57:28,3min 32s,0s,,1.41 Km,37 kph,23 kph,
Detenido,2026-01-07 10:57:28,2026-01-07 11:01:00,3min 32s,19s,,"-36.48246, -72.020114",
Movimiento,2026-01-07 11:01:00,2026-01-07 11:07:03,6min 3s,0s,,7.16 Km,118 kph,51 kph,
Detenido,2026-01-07 11:07:03,2026-01-07 11:08:34,1min 31s,0s,,"-36.440235, -71.962956",
Movimiento,2026-01-07 11:08:34,2026-01-07 11:13:06,4min 32s,0s,,2.94 Km,46 kph,34 kph,
Detenido,2026-01-07 11:13:06,2026-01-07 11:30:49,17min 43s,0s,,"-36.450193, -71.953781",
Movimiento,2026-01-07 11:30:49,2026-01-07 11:34:49,4min 0s,1min 29s,,1.6 Km,70 kph,61 kph,
Detenido,2026-01-07 11:34:49,2026-01-07 11:35:11,22s,22s,,"-36.434598, -71.962121",
Movimiento,2026-01-07 11:35:11,2026-01-07 11:37:21,2min 10s,0s,,0.44 Km,44 kph,25 kph,
Detenido,2026-01-07 11:37:21,2026-01-07 11:58:01,20min 40s,0s,,"-36.430809, -71.955999",
Movimiento,2026-01-07 11:58:01,2026-01-07 11:59:02,1min 1s,0s,,0.48 Km,29 kph,29 kph,
Detenido,2026-01-07 11:59:02,2026-01-07 11:59:29,27s,0s,,"-36.425028, -71.954108",
Movimiento,2026-01-07 11:59:29,2026-01-07 12:04:34,5min 5s,0s,,0.91 Km,27 kph,13 kph,
Detenido,2026-01-07 12:04:34,2026-01-07 12:06:15,1min 41s,0s,,"-36.423822, -71.959808",
Movimiento,2026-01-07 12:06:15,2026-01-07 12:09:07,2min 52s,0s,,0.86 Km,39 kph,25 kph,
Detenido,2026-01-07 12:09:07,2026-01-07 17:05:18,4h 56min 11s,0s,,"-36.430164, -71.959936",
Movimiento,2026-01-07 17:05:18,2026-01-07 17:07:55,2min 37s,0s,,0.22 Km,7 kph,6 kph,
Detenido,2026-01-07 17:07:55,2026-01-07 17:54:08,46min 13s,0s,,"-36.429279, -71.959533",
Movimiento,2026-01-07 17:54:08,2026-01-07 17:56:37,2min 29s,0s,,0.48 Km,45 kph,23 kph,
Detenido,2026-01-07 17:56:37,2026-01-07 18:00:30,3min 53s,1min 1s,,"-36.428604, -71.960209",
Movimiento,2026-01-07 18:00:30,2026-01-07 18:01:30,1min 0s,0s,,0.16 Km,20 kph,20 kph,
Detenido,2026-01-07 18:01:30,2026-01-08 10:06:22,16h 4min 52s,0s,,"-36.43012, -71.959607",
Movimiento,2026-01-08 10:06:22,2026-01-08 10:08:29,2min 7s,0s,,0.21 Km,29 kph,20 kph,
Detenido,2026-01-08 10:08:29,2026-01-08 10:09:57,1min 28s,0s,,"-36.432148, -71.957283",
Movimiento,2026-01-08 10:09:57,2026-01-08 10:16:33,6min 36s,0s,,2.22 Km,42 kph,27 kph,
Detenido,2026-01-08 10:16:33,2026-01-08 10:20:27,3min 54s,0s,,"-36.414304, -71.948271",
Movimiento,2026-01-08 10:20:27,2026-01-08 10:26:08,5min 41s,0s,,2.27 Km,50 kph,26 kph,
Detenido,2026-01-08 10:26:08,2026-01-08 10:44:01,17min 53s,0s,,"-36.432131, -71.957264",
Movimiento,2026-01-08 10:44:01,2026-01-08 10:51:24,7min 23s,0s,,0.8 Km,35 kph,15 kph,
Detenido,2026-01-08 10:51:24,2026-01-08 14:39:44,3h 48min 20s,0s,,"-36.43008, -71.959622",
Movimiento,2026-01-08 14:39:44,2026-01-08 14:43:49,4min 5s,0s,,1.29 Km,35 kph,21 kph,
Detenido,2026-01-08 14:43:49,2026-01-08 14:44:53,1min 4s,0s,,"-36.425871, -71.949831",
Movimiento,2026-01-08 14:44:53,2026-01-08 14:53:54,9min 1s,0s,,12.12 Km,108 kph,81 kph,
Detenido,2026-01-08 14:53:54,2026-01-08 15:14:41,20min 47s,1min 1s,,"-36.35383, -71.854301",
Movimiento,2026-01-08 15:14:41,2026-01-08 15:34:20,19min 39s,0s,,5.48 Km,92 kph,60 kph,
Detenido,2026-01-08 15:34:20,2026-01-08 15:37:54,3min 34s,40s,,"-36.332198, -71.81384",
Movimiento,2026-01-08 15:37:54,2026-01-08 15:51:30,13min 36s,0s,,15.08 Km,105 kph,63 kph,
Detenido,2026-01-08 15:51:30,2026-01-08 15:56:55,5min 25s,11s,,"-36.405157, -71.868468",
Movimiento,2026-01-08 15:56:55,2026-01-08 16:19:25,22min 30s,0s,,19.05 Km,110 kph,42 kph,
Detenido,2026-01-08 16:19:25,2026-01-08 16:50:57,31min 32s,34s,,"-36.478968, -71.714553",
Movimiento,2026-01-08 16:50:57,2026-01-08 17:14:15,23min 18s,0s,,15.51 Km,119 kph,30 kph,
Detenido,2026-01-08 17:14:15,2026-01-08 17:35:41,21min 26s,0s,,"-36.450126, -71.83751",
Movimiento,2026-01-08 17:35:41,2026-01-08 17:36:11,30s,0s,,0.01 Km,17 kph,17 kph,
Detenido,2026-01-08 17:36:11,2026-01-08 17:40:14,4min 3s,0s,,"-36.449904, -71.838479",
Movimiento,2026-01-08 17:40:14,2026-01-08 17:55:47,15min 33s,0s,,12.27 Km,85 kph,51 kph,
Detenido,2026-01-08 17:55:47,2026-01-08 17:57:48,2min 1s,0s,,"-36.4261, -71.948247",
Movimiento,2026-01-08 17:57:48,2026-01-08 18:00:40,2min 52s,16s,,1.46 Km,34 kph,23 kph,
Detenido,2026-01-08 18:00:40,2026-01-08 18:27:51,27min 11s,9s,,"-36.432272, -71.956524",
Movimiento,2026-01-08 18:27:51,2026-01-08 18:29:44,1min 53s,0s,,0.26 Km,20 kph,16 kph,
Detenido,2026-01-08 18:29:44,2026-01-08 18:30:15,31s,0s,,"-36.429021, -71.959973",
Movimiento,2026-01-08 18:30:15,2026-01-08 18:32:46,2min 31s,0s,,0.15 Km,13 kph,11 kph,
Detenido,2026-01-08 18:32:46,2026-01-09 08:24:57,13h 52min 11s,0s,,"-36.430118, -71.959668",
Movimiento,2026-01-09 08:24:57,2026-01-09 08:26:58,2min 1s,31s,,0.79 Km,42 kph,34 kph,
Detenido,2026-01-09 08:26:58,2026-01-09 08:29:28,2min 30s,0s,,"-36.426835, -71.951414",
Movimiento,2026-01-09 08:29:28,2026-01-09 08:33:31,4min 3s,0s,,2.38 Km,58 kph,41 kph,
Detenido,2026-01-09 08:33:31,2026-01-09 09:21:00,47min 29s,42s,,"-36.434498, -71.928686",
Movimiento,2026-01-09 09:21:00,2026-01-09 09:26:03,5min 3s,0s,,2.17 Km,60 kph,33 kph,
Detenido,2026-01-09 09:26:03,2026-01-09 09:27:33,1min 30s,0s,,"-36.426097, -71.948332",
Movimiento,2026-01-09 09:27:33,2026-01-09 09:31:04,3min 31s,0s,,1.39 Km,46 kph,25 kph,
Detenido,2026-01-09 09:31:04,2026-01-09 09:44:22,13min 18s,0s,,"-36.430119, -71.959649",
Movimiento,2026-01-09 09:44:22,2026-01-09 09:48:43,4min 21s,0s,,1.48 Km,28 kph,19 kph,
Detenido,2026-01-09 09:48:43,2026-01-09 09:51:53,3min 10s,0s,,"-36.424593, -71.94952",
Movimiento,2026-01-09 09:51:53,2026-01-09 09:53:25,1min 32s,0s,,0.03 Km,9 kph,8 kph,
Detenido,2026-01-09 09:53:25,2026-01-09 10:04:22,10min 57s,0s,,"-36.424646, -71.949304",
Movimiento,2026-01-09 10:04:22,2026-01-09 10:10:59,6min 37s,0s,,1.8 Km,33 kph,20 kph,
Detenido,2026-01-09 10:10:59,2026-01-09 10:22:55,11min 56s,0s,,"-36.430147, -71.959604",
Movimiento,2026-01-09 10:22:55,2026-01-09 10:36:42,13min 47s,0s,,13.29 Km,110 kph,56 kph,
Detenido,2026-01-09 10:36:42,2026-01-09 10:38:50,2min 8s,0s,,"-36.353814, -71.854274",
Movimiento,2026-01-09 10:38:50,2026-01-09 10:45:28,6min 38s,2min 51s,,3.69 Km,94 kph,64 kph,
Detenido,2026-01-09 10:45:28,2026-01-09 10:47:53,2min 25s,2min 25s,,"-36.332141, -71.81387",
Movimiento,2026-01-09 10:47:53,2026-01-09 10:50:48,2min 55s,1min 2s,,4.81 Km,84 kph,66 kph,
Detenido,2026-01-09 10:50:48,2026-01-09 10:51:46,58s,58s,,"-36.364843, -71.771334",
Movimiento,2026-01-09 10:51:46,2026-01-09 11:06:53,15min 7s,0s,,6.87 Km,79 kph,64 kph,
Detenido,2026-01-09 11:06:53,2026-01-09 11:27:42,20min 49s,0s,,"-36.396436, -71.734715",
Movimiento,2026-01-09 11:27:42,2026-01-09 11:43:50,16min 8s,1min 1s,,15.59 Km,93 kph,66 kph,
Detenido,2026-01-09 11:43:50,2026-01-09 11:44:11,21s,21s,,"-36.370944, -71.87315",
Movimiento,2026-01-09 11:44:11,2026-01-09 11:54:53,10min 42s,0s,,10.63 Km,100 kph,55 kph,
Detenido,2026-01-09 11:54:53,2026-01-09 12:03:51,8min 58s,0s,,"-36.416809, -71.956246",
Movimiento,2026-01-09 12:03:51,2026-01-09 12:07:58,4min 7s,0s,,1.52 Km,50 kph,34 kph,
Detenido,2026-01-09 12:07:58,2026-01-09 12:25:51,17min 53s,0s,,"-36.430089, -71.960723",
Movimiento,2026-01-09 12:25:51,2026-01-09 12:27:01,1min 10s,0s,,0.23 Km,41 kph,27 kph,
Detenido,2026-01-09 12:27:01,2026-01-09 12:40:10,13min 9s,1min 1s,,"-36.432132, -71.95723",
Movimiento,2026-01-09 12:40:10,2026-01-09 12:56:18,16min 8s,0s,,12.4 Km,117 kph,44 kph,
Detenido,2026-01-09 12:56:18,2026-01-09 14:27:54,1h 31min 36s,0s,,"-36.405198, -71.868466",
Movimiento,2026-01-09 14:27:54,2026-01-09 14:40:30,12min 36s,0s,,10.95 Km,97 kph,50 kph,
Detenido,2026-01-09 14:40:30,2026-01-09 14:42:00,1min 30s,0s,,"-36.426126, -71.948348",
Movimiento,2026-01-09 14:42:00,2026-01-09 14:46:02,4min 2s,0s,,1 Km,47 kph,32 kph,
Detenido,2026-01-09 14:46:02,2026-01-09 14:47:02,1min 0s,0s,,"-36.429418, -71.95788",
Movimiento,2026-01-09 14:47:02,2026-01-09 14:50:33,3min 31s,0s,,0.37 Km,27 kph,13 kph,
Detenido,2026-01-09 14:50:33,2026-01-09 17:52:34,3h 2min 1s,0s,,"-36.430092, -71.959613",
Movimiento,2026-01-09 17:52:34,2026-01-09 17:52:42,8s,0s,,0.02 Km,14 kph,14 kph,
Detenido,2026-01-09 17:52:42,2026-01-10 08:09:38,14h 16min 56s,13s,,"-36.430105, -71.959354",
Movimiento,2026-01-10 08:09:38,2026-01-10 08:13:55,4min 17s,0s,,1.22 Km,32 kph,21 kph,
Detenido,2026-01-10 08:13:55,2026-01-10 08:22:30,8min 35s,0s,,"-36.421172, -71.960355",
Movimiento,2026-01-10 08:22:30,2026-01-10 08:25:46,3min 16s,0s,,1.17 Km,31 kph,19 kph,
Detenido,2026-01-10 08:25:46,2026-01-10 08:47:31,21min 45s,9s,,"-36.430105, -71.95961",
Movimiento,2026-01-10 08:47:31,2026-01-10 08:47:34,3s,3s,,0.01 Km,7 kph,7 kph,
Detenido,2026-01-10 08:47:34,2026-01-10 12:36:14,3h 48min 40s,0s,,"-36.430091, -71.95973",
Movimiento,2026-01-10 12:36:14,2026-01-10 12:44:47,8min 33s,1min 0s,,5.76 Km,91 kph,50 kph,
Detenido,2026-01-10 12:44:47,2026-01-10 12:47:19,2min 32s,9s,,"-36.434553, -71.928757",
Movimiento,2026-01-10 12:47:19,2026-01-10 12:54:52,7min 33s,2min 1s,,4.3 Km,71 kph,42 kph,
Detenido,2026-01-10 12:54:52,2026-01-10 13:17:06,22min 14s,31s,,"-36.450213, -71.953806",
Movimiento,2026-01-10 13:17:06,2026-01-10 13:24:10,7min 4s,23s,,4.15 Km,62 kph,31 kph,
Detenido,2026-01-10 13:24:10,2026-01-10 13:33:13,9min 3s,28s,,"-36.416067, -71.949218",
Movimiento,2026-01-10 13:33:13,2026-01-10 13:35:17,2min 4s,0s,,0.53 Km,51 kph,40 kph,
Detenido,2026-01-10 13:35:17,2026-01-10 13:35:47,30s,0s,,"-36.424651, -71.955427",
Movimiento,2026-01-10 13:35:47,2026-01-10 13:36:17,30s,0s,,0.11 Km,17 kph,17 kph,
Detenido,2026-01-10 13:36:17,2026-01-10 13:39:19,3min 2s,0s,,"-36.424424, -71.95686",
Movimiento,2026-01-10 13:39:19,2026-01-10 13:42:51,3min 32s,9s,,1.16 Km,46 kph,20 kph,
Detenido,2026-01-10 13:42:51,2026-01-10 14:46:59,1h 4min 8s,8s,,"-36.43008, -71.95984",
Movimiento,2026-01-10 14:46:59,2026-01-10 14:49:12,2min 13s,0s,,0.03 Km,10 kph,8 kph,
Detenido,2026-01-10 14:49:12,2026-01-10 14:49:42,30s,0s,,"-36.431022, -71.956328",
Movimiento,2026-01-10 14:49:42,2026-01-10 14:58:47,9min 5s,0s,,8.99 Km,113 kph,54 kph,
Detenido,2026-01-10 14:58:47,2026-01-10 14:59:42,55s,0s,,"-36.473439, -72.014974",
Movimiento,2026-01-10 14:59:42,2026-01-10 14:59:48,6s,0s,,0.01 Km,7 kph,7 kph,
Detenido,2026-01-10 14:59:48,2026-01-10 15:18:52,19min 4s,7s,,"-36.473491, -72.015045",
Movimiento,2026-01-10 15:18:52,2026-01-10 15:33:36,14min 44s,1min 1s,,13.34 Km,112 kph,46 kph,
Detenido,2026-01-10 15:33:36,2026-01-10 16:02:52,29min 16s,0s,,"-36.507055, -72.116761",
Movimiento,2026-01-10 16:02:52,2026-01-10 16:18:01,15min 9s,18s,,19.76 Km,117 kph,65 kph,
Detenido,2026-01-10 16:18:01,2026-01-10 16:19:32,1min 31s,1min 31s,,"-36.434698, -71.960662",
Movimiento,2026-01-10 16:19:32,2026-01-10 16:20:03,31s,0s,,0.43 Km,18 kph,18 kph,
Detenido,2026-01-10 16:20:03,2026-01-10 16:42:43,22min 40s,30s,,"-36.432209, -71.956444",
Movimiento,2026-01-10 16:42:43,2026-01-10 16:46:45,4min 2s,0s,,1.08 Km,43 kph,19 kph,
Detenido,2026-01-10 16:46:45,2026-01-10 16:48:15,1min 30s,0s,,"-36.425184, -71.960543",
Movimiento,2026-01-10 16:48:15,2026-01-10 16:59:22,11min 7s,0s,,9.48 Km,94 kph,55 kph,
Detenido,2026-01-10 16:59:22,2026-01-10 17:25:04,25min 42s,1min 27s,,"-36.363296, -71.982306",
Movimiento,2026-01-10 17:25:04,2026-01-10 17:29:11,4min 7s,0s,,1.53 Km,71 kph,20 kph,
Detenido,2026-01-10 17:29:11,2026-01-10 17:43:32,14min 21s,12s,,"-36.360788, -71.970684",
Movimiento,2026-01-10 17:43:32,2026-01-10 18:01:34,18min 2s,0s,,13.9 Km,97 kph,41 kph,
Detenido,2026-01-10 18:01:34,2026-01-10 18:22:20,20min 46s,1min 37s,,"-36.423798, -72.033836",
Movimiento,2026-01-10 18:22:20,2026-01-10 18:28:24,6min 4s,0s,,6.06 Km,88 kph,54 kph,
Detenido,2026-01-10 18:28:24,2026-01-10 18:32:46,4min 22s,0s,,"-36.426234, -71.967868",
Movimiento,2026-01-10 18:32:46,2026-01-10 18:36:27,3min 41s,0s,,1.74 Km,52 kph,28 kph,
Detenido,2026-01-10 18:36:27,2026-01-11 08:53:09,14h 16min 42s,0s,,"-36.43014, -71.959596",
Movimiento,2026-01-11 08:53:09,2026-01-11 08:53:16,7s,7s,,0.01 Km,10 kph,10 kph,
Detenido,2026-01-11 08:53:16,2026-01-11 08:54:40,1min 24s,1min 24s,,"-36.430278, -71.959815",
Movimiento,2026-01-11 08:54:40,2026-01-11 08:57:12,2min 32s,0s,,1.4 Km,41 kph,24 kph,
Detenido,2026-01-11 08:57:12,2026-01-11 08:57:29,17s,0s,,"-36.425931, -71.949289",
Movimiento,2026-01-11 08:57:29,2026-01-11 09:00:43,3min 14s,0s,,1.53 Km,56 kph,39 kph,
Detenido,2026-01-11 09:00:43,2026-01-11 09:25:20,24min 37s,0s,,"-36.434502, -71.928769",
Movimiento,2026-01-11 09:25:20,2026-01-11 09:36:39,11min 19s,0s,,8.66 Km,81 kph,37 kph,
Detenido,2026-01-11 09:36:39,2026-01-11 10:05:30,28min 51s,1min 1s,,"-36.450053, -71.837494",
Movimiento,2026-01-11 10:05:30,2026-01-11 10:12:33,7min 3s,0s,,4.01 Km,58 kph,36 kph,
Detenido,2026-01-11 10:12:33,2026-01-11 10:33:45,21min 12s,0s,,"-36.432725, -71.828482",
Movimiento,2026-01-11 10:33:45,2026-01-11 10:39:19,5min 34s,30s,,5.87 Km,76 kph,52 kph,
Detenido,2026-01-11 10:39:19,2026-01-11 11:32:49,53min 30s,1s,,"-36.405134, -71.868501",
Movimiento,2026-01-11 11:32:49,2026-01-11 11:34:50,2min 1s,0s,,0.53 Km,85 kph,46 kph,
Detenido,2026-01-11 11:34:50,2026-01-11 11:35:50,1min 0s,0s,,"-36.39313, -71.885393",
Movimiento,2026-01-11 11:35:50,2026-01-11 11:44:55,9min 5s,0s,,7.16 Km,83 kph,35 kph,
Detenido,2026-01-11 11:44:55,2026-01-11 11:58:33,13min 38s,0s,,"-36.353827, -71.854258",
Movimiento,2026-01-11 11:58:33,2026-01-11 12:05:06,6min 33s,0s,,5.37 Km,76 kph,50 kph,
Detenido,2026-01-11 12:05:06,2026-01-11 12:18:37,13min 31s,2min 55s,,"-36.332134, -71.813982",
Movimiento,2026-01-11 12:18:37,2026-01-11 12:33:54,15min 17s,1min 1s,,12.23 Km,69 kph,47 kph,
Detenido,2026-01-11 12:33:54,2026-01-11 12:34:24,30s,30s,,"-36.397329, -71.733964",
Movimiento,2026-01-11 12:34:24,2026-01-11 12:35:25,1min 1s,0s,,0.09 Km,12 kph,12 kph,
Detenido,2026-01-11 12:35:25,2026-01-11 12:55:37,20min 12s,0s,,"-36.396512, -71.734744",
Movimiento,2026-01-11 12:55:37,2026-01-11 12:56:08,31s,31s,,0.08 Km,13 kph,13 kph,
Detenido,2026-01-11 12:56:08,2026-01-11 12:58:09,2min 1s,0s,,"-36.397365, -71.73386",
Movimiento,2026-01-11 12:58:09,2026-01-11 13:19:21,21min 12s,0s,,24.09 Km,103 kph,61 kph,
Detenido,2026-01-11 13:19:21,2026-01-11 13:38:03,18min 42s,31s,,"-36.424626, -71.949465",
Movimiento,2026-01-11 13:38:03,2026-01-11 13:41:35,3min 32s,21s,,1.51 Km,43 kph,21 kph,
Detenido,2026-01-11 13:41:35,2026-01-11 14:01:43,20min 8s,0s,,"-36.433126, -71.954105",
Movimiento,2026-01-11 14:01:43,2026-01-11 14:06:38,4min 55s,0s,,1.15 Km,36 kph,15 kph,
Detenido,2026-01-11 14:06:38,2026-01-11 16:41:54,2h 35min 16s,26s,,"-36.430126, -71.959623",
Movimiento,2026-01-11 16:41:54,2026-01-11 16:44:26,2min 32s,0s,,0.22 Km,18 kph,11 kph,
Detenido,2026-01-11 16:44:26,2026-01-11 17:27:34,43min 8s,0s,,"-36.429312, -71.959558",
Movimiento,2026-01-11 17:27:34,2026-01-11 17:30:06,2min 32s,0s,,0.4 Km,28 kph,15 kph,
Detenido,2026-01-11 17:30:06,2026-01-11 17:35:27,5min 21s,0s,,"-36.428593, -71.960272",
Movimiento,2026-01-11 17:35:27,2026-01-11 17:36:40,1min 13s,0s,,0.19 Km,20 kph,11 kph,
Detenido,2026-01-11 17:36:40,2026-01-12 08:20:26,14h 43min 46s,6s,,"-36.430097, -71.95963",
Movimiento,2026-01-12 08:20:26,2026-01-12 08:24:53,4min 27s,30s,,1.07 Km,38 kph,18 kph,
Detenido,2026-01-12 08:24:53,2026-01-12 08:25:54,1min 1s,1min 1s,,"-36.422766, -71.953328",
Movimiento,2026-01-12 08:25:54,2026-01-12 08:38:01,12min 7s,0s,,12.65 Km,119 kph,50 kph,
Detenido,2026-01-12 08:38:01,2026-01-12 09:04:47,26min 46s,31s,,"-36.35388, -71.854198",
Movimiento,2026-01-12 09:04:47,2026-01-12 09:16:24,11min 37s,0s,,5 Km,87 kph,69 kph,
Detenido,2026-01-12 09:16:24,2026-01-12 10:03:31,47min 7s,2min 1s,,"-36.332112, -71.813828",
Movimiento,2026-01-12 10:03:31,2026-01-12 10:17:07,13min 36s,0s,,11.84 Km,95 kph,49 kph,
Detenido,2026-01-12 10:17:07,2026-01-12 10:52:47,35min 40s,0s,,"-36.396461, -71.734738",
Movimiento,2026-01-12 10:52:47,2026-01-12 11:09:57,17min 10s,0s,,17.19 Km,98 kph,52 kph,
Detenido,2026-01-12 11:09:57,2026-01-12 11:12:37,2min 40s,0s,,"-36.405167, -71.868467",
Movimiento,2026-01-12 11:12:37,2026-01-12 11:12:49,12s,0s,,0 Km,7 kph,7 kph,
Detenido,2026-01-12 11:12:49,2026-01-12 11:45:33,32min 44s,0s,,"-36.405225, -71.868379",
Movimiento,2026-01-12 11:45:33,2026-01-12 11:59:35,14min 2s,0s,,9.55 Km,89 kph,43 kph,
Detenido,2026-01-12 11:59:35,2026-01-12 12:39:32,39min 57s,0s,,"-36.434784, -71.928744",
Movimiento,2026-01-12 12:39:32,2026-01-12 12:39:50,18s,18s,,0 Km,7 kph,7 kph,
Detenido,2026-01-12 12:39:50,2026-01-12 12:50:02,10min 12s,1min 10s,,"-36.434821, -71.928815",
Movimiento,2026-01-12 12:50:02,2026-01-12 12:51:33,1min 31s,30s,,0.45 Km,46 kph,23 kph,
Detenido,2026-01-12 12:51:33,2026-01-12 12:53:35,2min 2s,2min 2s,,"-36.428736, -71.926317",
Movimiento,2026-01-12 12:53:35,2026-01-12 12:54:35,1min 0s,0s,,1.72 Km,67 kph,61 kph,
Detenido,2026-01-12 12:54:35,2026-01-12 12:57:07,2min 32s,0s,,"-36.42625, -71.947533",
Movimiento,2026-01-12 12:57:07,2026-01-12 12:58:38,1min 31s,0s,,0.13 Km,27 kph,27 kph,
Detenido,2026-01-12 12:58:38,2026-01-12 13:06:20,7min 42s,0s,,"-36.424585, -71.949525",
Movimiento,2026-01-12 13:06:20,2026-01-12 13:14:15,7min 55s,0s,,1.77 Km,34 kph,18 kph,
Detenido,2026-01-12 13:14:15,2026-01-12 15:22:46,2h 8min 31s,19s,,"-36.430134, -71.959605",
Movimiento,2026-01-12 15:22:46,2026-01-12 15:30:02,7min 16s,0s,,1.24 Km,30 kph,16 kph,
Detenido,2026-01-12 15:30:02,2026-01-12 17:03:01,1h 32min 59s,0s,,"-36.430089, -71.959619",
Movimiento,2026-01-12 17:03:01,2026-01-12 17:04:01,1min 0s,7s,,0.63 Km,41 kph,32 kph,
Detenido,2026-01-12 17:04:01,2026-01-12 17:24:44,20min 43s,28s,,"-36.432004, -71.953181",
Movimiento,2026-01-12 17:24:44,2026-01-12 17:42:22,17min 38s,0s,,12.27 Km,95 kph,49 kph,
Detenido,2026-01-12 17:42:22,2026-01-12 18:01:51,19min 29s,0s,,"-36.450116, -71.837543",
Movimiento,2026-01-12 18:01:51,2026-01-12 18:15:03,13min 12s,0s,,12.28 Km,96 kph,55 kph,
Detenido,2026-01-12 18:15:03,2026-01-12 18:17:33,2min 30s,0s,,"-36.426453, -71.946435",
Movimiento,2026-01-12 18:17:33,2026-01-12 18:22:07,4min 34s,0s,,1.19 Km,37 kph,19 kph,
Detenido,2026-01-12 18:22:07,2026-01-12 18:22:23,16s,7s,,"-36.429821, -71.960509",
Movimiento,2026-01-12 18:22:23,2026-01-12 18:23:08,45s,0s,,0.09 Km,14 kph,10 kph,
Detenido,2026-01-12 18:23:08,2026-01-13 11:15:26,16h 52min 18s,50s,,"-36.430093, -71.959614",
Movimiento,2026-01-13 11:15:26,2026-01-13 11:19:09,3min 43s,0s,,0.95 Km,48 kph,26 kph,
Detenido,2026-01-13 11:19:09,2026-01-13 11:32:22,13min 13s,49s,,"-36.433293, -71.96107",
Movimiento,2026-01-13 11:32:22,2026-01-13 11:33:21,59s,0s,,0.24 Km,22 kph,22 kph,
Detenido,2026-01-13 11:33:21,2026-01-13 12:12:19,38min 58s,0s,,"-36.432115, -71.957268",
Movimiento,2026-01-13 12:12:19,2026-01-13 12:25:56,13min 37s,0s,,11.2 Km,116 kph,50 kph,
Detenido,2026-01-13 12:25:56,2026-01-13 12:26:26,30s,0s,,"-36.405176, -71.868444",
Movimiento,2026-01-13 12:26:26,2026-01-13 12:26:42,16s,0s,,0 Km,9 kph,9 kph,
Detenido,2026-01-13 12:26:42,2026-01-13 13:41:32,1h 14min 50s,0s,,"-36.405232, -71.868319",
Movimiento,2026-01-13 13:41:32,2026-01-13 14:02:29,20min 57s,0s,,12.82 Km,78 kph,38 kph,
Detenido,2026-01-13 14:02:29,2026-01-13 15:49:23,1h 46min 54s,0s,,"-36.430087, -71.959613",
Movimiento,2026-01-13 15:49:23,2026-01-13 15:56:56,7min 33s,0s,,2.2 Km,47 kph,19 kph,
Detenido,2026-01-13 15:56:56,2026-01-13 15:58:28,1min 32s,1s,,"-36.429268, -71.958548",
Movimiento,2026-01-13 15:58:28,2026-01-13 15:59:27,59s,0s,,0 Km,8 kph,8 kph,
Detenido,2026-01-13 15:59:27,2026-01-13 16:54:22,54min 55s,0s,,"-36.430116, -71.959614",
Movimiento,2026-01-13 16:54:22,2026-01-13 17:11:32,17min 10s,0s,,21.03 Km,116 kph,71 kph,
Detenido,2026-01-13 17:11:32,2026-01-13 17:27:43,16min 11s,0s,,"-36.507039, -72.116688",
Movimiento,2026-01-13 17:27:43,2026-01-13 18:02:17,34min 34s,0s,,31.08 Km,103 kph,52 kph,
Detenido,2026-01-13 18:02:17,2026-01-13 18:17:59,15min 42s,30s,,"-36.450125, -71.837533",
Movimiento,2026-01-13 18:17:59,2026-01-13 18:38:47,20min 48s,0s,,15.78 Km,101 kph,50 kph,
Detenido,2026-01-13 18:38:47,2026-01-13 18:52:28,13min 41s,58s,,"-36.396499, -71.734706",
Movimiento,2026-01-13 18:52:28,2026-01-13 19:26:18,33min 50s,0s,,29.95 Km,95 kph,51 kph,
Detenido,2026-01-13 19:26:18,2026-01-13 19:32:22,6min 4s,0s,,"-36.428531, -71.960318",
Movimiento,2026-01-13 19:32:22,2026-01-13 19:33:47,1min 25s,0s,,0.16 Km,19 kph,14 kph,
Detenido,2026-01-13 19:33:47,2026-01-13 19:36:32,2min 45s,0s,,"-36.430112, -71.959703",
Movimiento,2026-01-13 19:36:32,2026-01-13 19:37:19,47s,0s,,0.18 Km,14 kph,11 kph,
Detenido,2026-01-13 19:37:19,2026-01-13 20:02:22,25min 3s,34s,,"-36.429196, -71.959146",
Movimiento,2026-01-13 20:02:22,2026-01-13 20:05:15,2min 53s,0s,,0.29 Km,29 kph,15 kph,
Detenido,2026-01-13 20:05:15,2026-01-14 08:14:54,12h 9min 39s,30s,,"-36.430097, -71.959716",
Movimiento,2026-01-14 08:14:54,2026-01-14 08:16:55,2min 1s,0s,,0.13 Km,21 kph,16 kph,
Detenido,2026-01-14 08:16:55,2026-01-14 08:20:04,3min 9s,0s,,"-36.429267, -71.959382",
Movimiento,2026-01-14 08:20:04,2026-01-14 08:30:00,9min 56s,0s,,8.28 Km,110 kph,48 kph,
Detenido,2026-01-14 08:30:00,2026-01-14 08:49:33,19min 33s,1min 8s,,"-36.473418, -72.014959",
Movimiento,2026-01-14 08:49:33,2026-01-14 09:02:39,13min 6s,37s,,13.16 Km,111 kph,47 kph,
Detenido,2026-01-14 09:02:39,2026-01-14 09:10:43,8min 4s,0s,,"-36.507034, -72.116787",
Movimiento,2026-01-14 09:10:43,2026-01-14 09:30:24,19min 41s,0s,,20.61 Km,110 kph,53 kph,
Detenido,2026-01-14 09:30:24,2026-01-14 15:06:08,5h 35min 44s,0s,,"-36.430141, -71.959621",
Movimiento,2026-01-14 15:06:08,2026-01-14 15:12:12,6min 4s,0s,,2.21 Km,49 kph,28 kph,
Detenido,2026-01-14 15:12:12,2026-01-14 15:13:43,1min 31s,0s,,"-36.429023, -71.94321",
Movimiento,2026-01-14 15:13:43,2026-01-14 15:25:50,12min 7s,0s,,10.26 Km,82 kph,55 kph,
Detenido,2026-01-14 15:25:50,2026-01-14 15:57:39,31min 49s,0s,,"-36.450113, -71.837579",
Movimiento,2026-01-14 15:57:39,2026-01-14 16:11:52,14min 13s,0s,,12.34 Km,79 kph,41 kph,
Detenido,2026-01-14 16:11:52,2026-01-14 16:15:59,4min 7s,1min 0s,,"-36.422128, -71.7558",
Movimiento,2026-01-14 16:15:59,2026-01-14 16:16:24,25s,25s,,0.04 Km,34 kph,34 kph,
Detenido,2026-01-14 16:16:24,2026-01-14 16:17:25,1min 1s,1min 1s,,"-36.419637, -71.754133",
Movimiento,2026-01-14 16:17:25,2026-01-14 16:18:56,1min 31s,0s,,0.82 Km,43 kph,41 kph,
Detenido,2026-01-14 16:18:56,2026-01-14 16:22:57,4min 1s,0s,,"-36.410814, -71.747469",
Movimiento,2026-01-14 16:22:57,2026-01-14 16:30:31,7min 34s,0s,,6.98 Km,80 kph,57 kph,
Detenido,2026-01-14 16:30:31,2026-01-14 16:49:40,19min 9s,0s,,"-36.388182, -71.787143",
Movimiento,2026-01-14 16:49:40,2026-01-14 17:00:16,10min 36s,1min 31s,,9.76 Km,70 kph,54 kph,
Detenido,2026-01-14 17:00:16,2026-01-14 17:37:36,37min 20s,15s,,"-36.353889, -71.854029",
Movimiento,2026-01-14 17:37:36,2026-01-14 17:58:15,20min 39s,0s,,13.06 Km,75 kph,45 kph,
Detenido,2026-01-14 17:58:15,2026-01-15 08:23:03,14h 24min 48s,0s,,"-36.42618, -71.959369",
Movimiento,2026-01-15 08:23:03,2026-01-15 08:32:36,9min 33s,0s,,5.23 Km,60 kph,36 kph,
Detenido,2026-01-15 08:32:36,2026-01-15 08:33:37,1min 1s,0s,,"-36.412045, -71.908673",
Movimiento,2026-01-15 08:33:37,2026-01-15 08:38:40,5min 3s,0s,,4.95 Km,101 kph,70 kph,
Detenido,2026-01-15 08:38:40,2026-01-15 09:26:05,47min 25s,0s,,"-36.405169, -71.86843",
Movimiento,2026-01-15 09:26:05,2026-01-15 09:38:07,12min 2s,0s,,10.41 Km,97 kph,57 kph,
Detenido,2026-01-15 09:38:07,2026-01-15 09:40:07,2min 0s,0s,,"-36.426109, -71.948353",
Movimiento,2026-01-15 09:40:07,2026-01-15 09:44:10,4min 3s,31s,,1.5 Km,40 kph,26 kph,
Detenido,2026-01-15 09:44:10,2026-01-15 10:13:37,29min 27s,0s,,"-36.430081, -71.95963",
Movimiento,2026-01-15 10:13:37,2026-01-15 10:16:08,2min 31s,0s,,0.35 Km,18 kph,15 kph,
Detenido,2026-01-15 10:16:08,2026-01-15 10:28:21,12min 13s,0s,,"-36.430775, -71.955993",
Movimiento,2026-01-15 10:28:21,2026-01-15 10:29:16,55s,55s,,0.28 Km,7 kph,7 kph,
Detenido,2026-01-15 10:29:16,2026-01-15 10:48:02,18min 46s,30s,,"-36.428947, -71.953228",
Movimiento,2026-01-15 10:48:02,2026-01-15 11:04:36,16min 34s,0s,,18.02 Km,112 kph,66 kph,
Detenido,2026-01-15 11:04:36,2026-01-15 11:12:10,7min 34s,0s,,"-36.332166, -71.813982",
Movimiento,2026-01-15 11:12:10,2026-01-15 11:30:20,18min 10s,0s,,21.63 Km,112 kph,73 kph,
Detenido,2026-01-15 11:30:20,2026-01-15 11:45:52,15min 32s,1min 23s,,"-36.43007, -71.959613",
Movimiento,2026-01-15 11:45:52,2026-01-15 11:50:32,4min 40s,51s,,0.79 Km,25 kph,15 kph,
Detenido,2026-01-15 11:50:32,2026-01-15 11:56:35,6min 3s,0s,,"-36.430039, -71.95968",
Movimiento,2026-01-15 11:56:35,2026-01-15 12:11:43,15min 8s,0s,,8.78 Km,77 kph,38 kph,
Detenido,2026-01-15 12:11:43,2026-01-15 12:56:05,44min 22s,0s,,"-36.475685, -71.949494",
Movimiento,2026-01-15 12:56:05,2026-01-15 13:07:41,11min 36s,0s,,12.52 Km,99 kph,57 kph,
Detenido,2026-01-15 13:07:41,2026-01-15 13:29:30,21min 49s,0s,,"-36.450105, -71.8375",
Movimiento,2026-01-15 13:29:30,2026-01-15 13:46:09,16min 39s,0s,,12.67 Km,79 kph,41 kph,
Detenido,2026-01-15 13:46:09,2026-01-15 15:41:43,1h 55min 34s,0s,,"-36.43012, -71.959612",
Movimiento,2026-01-15 15:41:43,2026-01-15 15:42:23,40s,0s,,0.07 Km,27 kph,20 kph,
Detenido,2026-01-15 15:42:23,2026-01-15 15:43:54,1min 31s,0s,,"-36.429542, -71.958809",
Movimiento,2026-01-15 15:43:54,2026-01-15 15:44:24,30s,30s,,0.06 Km,9 kph,9 kph,
Detenido,2026-01-15 15:44:24,2026-01-15 16:23:30,39min 6s,37s,,"-36.429327, -71.959526",
Movimiento,2026-01-15 16:23:30,2026-01-15 16:24:38,1min 8s,0s,,0.06 Km,26 kph,17 kph,
Detenido,2026-01-15 16:24:38,2026-01-16 08:57:04,16h 32min 26s,0s,,"-36.430082, -71.959604",
Movimiento,2026-01-16 08:57:04,2026-01-16 08:59:34,2min 30s,0s,,1.25 Km,44 kph,38 kph,
Detenido,2026-01-16 08:59:34,2026-01-16 09:01:03,1min 29s,0s,,"-36.42608, -71.948803",
Movimiento,2026-01-16 09:01:03,2026-01-16 09:10:08,9min 5s,0s,,11.77 Km,105 kph,87 kph,
Detenido,2026-01-16 09:10:08,2026-01-16 09:22:54,12min 46s,0s,,"-36.353823, -71.85428",
Movimiento,2026-01-16 09:22:54,2026-01-16 09:37:43,14min 49s,0s,,11.19 Km,87 kph,45 kph,
Detenido,2026-01-16 09:37:43,2026-01-16 09:40:04,2min 21s,0s,,"-36.38816, -71.78719",
Movimiento,2026-01-16 09:40:04,2026-01-16 09:41:46,1min 42s,0s,,0.01 Km,9 kph,9 kph,
Detenido,2026-01-16 09:41:46,2026-01-16 09:44:30,2min 44s,0s,,"-36.38812, -71.787163",
Movimiento,2026-01-16 09:44:30,2026-01-16 09:44:47,17s,17s,,0.01 Km,11 kph,11 kph,
Detenido,2026-01-16 09:44:47,2026-01-16 09:50:56,6min 9s,0s,,"-36.388151, -71.787156",
Movimiento,2026-01-16 09:50:56,2026-01-16 10:20:12,29min 16s,0s,,25.73 Km,104 kph,50 kph,
Detenido,2026-01-16 10:20:12,2026-01-16 10:59:49,39min 37s,52s,,"-36.475682, -71.949291",
Movimiento,2026-01-16 10:59:49,2026-01-16 11:07:00,7min 11s,0s,,4.62 Km,67 kph,35 kph,
Detenido,2026-01-16 11:07:00,2026-01-16 11:23:09,16min 9s,0s,,"-36.45015, -71.953804",
Movimiento,2026-01-16 11:23:09,2026-01-16 11:30:44,7min 35s,0s,,3.29 Km,59 kph,34 kph,
Detenido,2026-01-16 11:30:44,2026-01-16 11:32:41,1min 57s,0s,,"-36.424746, -71.955107",
Movimiento,2026-01-16 11:32:41,2026-01-16 11:33:46,1min 5s,0s,,0.46 Km,12 kph,9 kph,
Detenido,2026-01-16 11:33:46,2026-01-16 11:53:55,20min 9s,0s,,"-36.425732, -71.962381",
Movimiento,2026-01-16 11:53:55,2026-01-16 11:56:25,2min 30s,0s,,0.78 Km,44 kph,23 kph,
Detenido,2026-01-16 11:56:25,2026-01-16 12:03:24,6min 59s,0s,,"-36.430101, -71.959628",
Movimiento,2026-01-16 12:03:24,2026-01-16 12:08:56,5min 32s,0s,,1.34 Km,28 kph,15 kph,
Detenido,2026-01-16 12:08:56,2026-01-16 12:09:57,1min 1s,0s,,"-36.422957, -71.964505",
Movimiento,2026-01-16 12:09:57,2026-01-16 12:17:30,7min 33s,0s,,6.56 Km,86 kph,52 kph,
Detenido,2026-01-16 12:17:30,2026-01-16 12:17:50,20s,0s,,"-36.365083, -71.966559",
Movimiento,2026-01-16 12:17:50,2026-01-16 12:18:31,41s,0s,,0 Km,7 kph,7 kph,
Detenido,2026-01-16 12:18:31,2026-01-16 12:34:10,15min 39s,0s,,"-36.365102, -71.966411",
Movimiento,2026-01-16 12:34:10,2026-01-16 12:50:38,16min 28s,0s,,7.74 Km,93 kph,36 kph,
Detenido,2026-01-16 12:50:38,2026-01-17 08:42:12,19h 51min 34s,0s,,"-36.430155, -71.959627",
Movimiento,2026-01-17 08:42:12,2026-01-17 08:43:57,1min 45s,19s,,0.25 Km,33 kph,20 kph,
Detenido,2026-01-17 08:43:57,2026-01-17 09:05:51,21min 54s,0s,,"-36.432328, -71.956571",
Movimiento,2026-01-17 09:05:51,2026-01-17 09:07:22,1min 31s,0s,,0.29 Km,28 kph,24 kph,
Detenido,2026-01-17 09:07:22,2026-01-17 09:13:53,6min 31s,0s,,"-36.433258, -71.954126",
Movimiento,2026-01-17 09:13:53,2026-01-17 09:14:16,23s,0s,,0.01 Km,7 kph,7 kph,
Detenido,2026-01-17 09:14:16,2026-01-17 09:24:14,9min 58s,0s,,"-36.43315, -71.954112",
Movimiento,2026-01-17 09:24:14,2026-01-17 09:36:21,12min 7s,0s,,11.65 Km,113 kph,62 kph,
Detenido,2026-01-17 09:36:21,2026-01-17 10:08:44,32min 23s,3s,,"-36.405166, -71.86846",
Movimiento,2026-01-17 10:08:44,2026-01-17 10:24:13,15min 29s,0s,,8.77 Km,82 kph,40 kph,
Detenido,2026-01-17 10:24:13,2026-01-17 10:40:32,16min 19s,0s,,"-36.45004, -71.837456",
Movimiento,2026-01-17 10:40:32,2026-01-17 10:53:00,12min 28s,0s,,12.3 Km,107 kph,49 kph,
Detenido,2026-01-17 10:53:00,2026-01-17 11:38:33,45min 33s,0s,,"-36.475688, -71.949267",
Movimiento,2026-01-17 11:38:33,2026-01-17 11:44:02,5min 29s,0s,,1.41 Km,32 kph,19 kph,
Detenido,2026-01-17 11:44:02,2026-01-17 11:46:03,2min 1s,1min 28s,,"-36.477811, -71.962455",
Movimiento,2026-01-17 11:46:03,2026-01-17 11:50:35,4min 32s,0s,,3.44 Km,61 kph,38 kph,
Detenido,2026-01-17 11:50:35,2026-01-17 12:08:13,17min 38s,0s,,"-36.450184, -71.953779",
Movimiento,2026-01-17 12:08:13,2026-01-17 12:10:44,2min 31s,0s,,1.61 Km,59 kph,43 kph,
Detenido,2026-01-17 12:10:44,2026-01-17 12:20:20,9min 36s,2min 1s,,"-36.433972, -71.951725",
Movimiento,2026-01-17 12:20:20,2026-01-17 12:21:20,1min 0s,0s,,0.33 Km,31 kph,31 kph,
Detenido,2026-01-17 12:21:20,2026-01-17 12:35:14,13min 54s,0s,,"-36.421819, -71.957473",
Movimiento,2026-01-17 12:35:14,2026-01-17 12:38:46,3min 32s,0s,,0.69 Km,51 kph,22 kph,
Detenido,2026-01-17 12:38:46,2026-01-17 12:41:05,2min 19s,0s,,"-36.426171, -71.968003",
Movimiento,2026-01-17 12:41:05,2026-01-17 12:44:49,3min 44s,0s,,1.3 Km,48 kph,31 kph,
Detenido,2026-01-17 12:44:49,2026-01-17 13:03:18,18min 29s,0s,,"-36.426742, -71.965071",
Movimiento,2026-01-17 13:03:18,2026-01-17 13:04:10,52s,0s,,0 Km,11 kph,11 kph,
Detenido,2026-01-17 13:04:10,2026-01-17 13:14:24,10min 14s,0s,,"-36.428479, -71.960093",
Movimiento,2026-01-17 13:14:24,2026-01-17 13:16:14,1min 50s,0s,,0.13 Km,8 kph,7 kph,
Detenido,2026-01-17 13:16:14,2026-01-17 13:45:32,29min 18s,0s,,"-36.430135, -71.959608",
Movimiento,2026-01-17 13:45:32,2026-01-17 13:46:08,36s,19s,,0.17 Km,24 kph,23 kph,
Detenido,2026-01-17 13:46:08,2026-01-17 14:03:31,17min 23s,0s,,"-36.429217, -71.959161",
Movimiento,2026-01-17 14:03:31,2026-01-17 14:12:42,9min 11s,0s,,0.22 Km,21 kph,13 kph,
Detenido,2026-01-17 14:12:42,2026-01-18 09:10:42,18h 58min 0s,0s,,"-36.430102, -71.959562",
Movimiento,2026-01-18 09:10:42,2026-01-18 09:39:17,28min 35s,0s,,24.95 Km,83 kph,51 kph,
Detenido,2026-01-18 09:39:17,2026-01-18 09:58:00,18min 43s,0s,,"-36.396443, -71.734709",
Movimiento,2026-01-18 09:58:00,2026-01-18 10:06:34,8min 34s,0s,,6.69 Km,66 kph,37 kph,
Detenido,2026-01-18 10:06:34,2026-01-18 10:28:17,21min 43s,0s,,"-36.388148, -71.78713",
Movimiento,2026-01-18 10:28:17,2026-01-18 10:31:48,3min 31s,0s,,2.25 Km,61 kph,50 kph,
Detenido,2026-01-18 10:31:48,2026-01-18 10:35:24,3min 36s,0s,,"-36.404909, -71.805495",
Movimiento,2026-01-18 10:35:24,2026-01-18 10:50:31,15min 7s,1min 1s,,9.2 Km,70 kph,36 kph,
Detenido,2026-01-18 10:50:31,2026-01-18 10:50:42,11s,11s,,"-36.46763, -71.838974",
Movimiento,2026-01-18 10:50:42,2026-01-18 11:02:08,11min 26s,1min 1s,,10.18 Km,80 kph,58 kph,
Detenido,2026-01-18 11:02:08,2026-01-18 11:38:14,36min 6s,0s,,"-36.475667, -71.94931",
Movimiento,2026-01-18 11:38:14,2026-01-18 11:49:51,11min 37s,0s,,6.71 Km,80 kph,41 kph,
Detenido,2026-01-18 11:49:51,2026-01-18 11:50:29,38s,0s,,"-36.426276, -71.948584",
Movimiento,2026-01-18 11:50:29,2026-01-18 11:51:52,1min 23s,0s,,0.37 Km,21 kph,18 kph,
Detenido,2026-01-18 11:51:52,2026-01-18 12:10:14,18min 22s,13s,,"-36.424599, -71.949479",
Movimiento,2026-01-18 12:10:14,2026-01-18 12:14:33,4min 19s,0s,,1.15 Km,45 kph,32 kph,
Detenido,2026-01-18 12:14:33,2026-01-18 12:36:47,22min 14s,0s,,"-36.425585, -71.96237",
Movimiento,2026-01-18 12:36:47,2026-01-18 12:39:17,2min 30s,0s,,0.33 Km,32 kph,24 kph,
Detenido,2026-01-18 12:39:17,2026-01-18 12:54:52,15min 35s,0s,,"-36.426724, -71.96486",
Movimiento,2026-01-18 12:54:52,2026-01-18 12:56:25,1min 33s,0s,,0.3 Km,17 kph,13 kph,
Detenido,2026-01-18 12:56:25,2026-01-18 13:18:03,21min 38s,0s,,"-36.427944, -71.95855",
Movimiento,2026-01-18 13:18:03,2026-01-18 13:21:36,3min 33s,0s,,1.03 Km,39 kph,26 kph,
Detenido,2026-01-18 13:21:36,2026-01-19 08:32:17,19h 10min 41s,0s,,"-36.430046, -71.959603",
Movimiento,2026-01-19 08:32:17,2026-01-19 08:34:48,2min 31s,0s,,0.51 Km,30 kph,24 kph,
Detenido,2026-01-19 08:34:48,2026-01-19 08:35:19,31s,0s,,"-36.426859, -71.951472",
Movimiento,2026-01-19 08:35:19,2026-01-19 08:46:26,11min 7s,0s,,10.6 Km,103 kph,54 kph,
Detenido,2026-01-19 08:46:26,2026-01-19 09:00:40,14min 14s,0s,,"-36.405147, -71.868444",
Movimiento,2026-01-19 09:00:40,2026-01-19 09:12:12,11min 32s,0s,,9.49 Km,68 kph,50 kph,
Detenido,2026-01-19 09:12:12,2026-01-19 09:42:38,30min 26s,0s,,"-36.388163, -71.787149",
Movimiento,2026-01-19 09:42:38,2026-01-19 09:51:19,8min 41s,0s,,6.66 Km,76 kph,47 kph,
Detenido,2026-01-19 09:51:19,2026-01-19 10:15:04,23min 45s,0s,,"-36.396463, -71.734751",
Movimiento,2026-01-19 10:15:04,2026-01-19 10:40:02,24min 58s,12s,,25.4 Km,100 kph,49 kph,
Detenido,2026-01-19 10:40:02,2026-01-19 11:18:37,38min 35s,12s,,"-36.475684, -71.94951",
Movimiento,2026-01-19 11:18:37,2026-01-19 11:30:13,11min 36s,0s,,6.66 Km,64 kph,38 kph,
Detenido,2026-01-19 11:30:13,2026-01-19 11:34:01,3min 48s,0s,,"-36.426923, -71.948739",
Movimiento,2026-01-19 11:34:01,2026-01-19 11:37:16,3min 15s,0s,,0.41 Km,29 kph,17 kph,
Detenido,2026-01-19 11:37:16,2026-01-19 12:00:39,23min 23s,0s,,"-36.424586, -71.949496",
Movimiento,2026-01-19 12:00:39,2026-01-19 12:08:13,7min 34s,0s,,1.99 Km,42 kph,21 kph,
Detenido,2026-01-19 12:08:13,2026-01-19 12:27:52,19min 39s,0s,,"-36.426723, -71.965024",
Movimiento,2026-01-19 12:27:52,2026-01-19 12:28:53,1min 1s,30s,,0.39 Km,33 kph,31 kph,
Detenido,2026-01-19 12:28:53,2026-01-19 12:30:55,2min 2s,31s,,"-36.427919, -71.958632",
Movimiento,2026-01-19 12:30:55,2026-01-19 12:32:25,1min 30s,0s,,0.14 Km,7 kph,7 kph,
Detenido,2026-01-19 12:32:25,2026-01-19 12:53:06,20min 41s,0s,,"-36.429113, -71.952832",
Movimiento,2026-01-19 12:53:06,2026-01-19 12:56:08,3min 2s,0s,,0.85 Km,31 kph,18 kph,
Detenido,2026-01-19 12:56:08,2026-01-19 12:56:18,10s,0s,,"-36.428959, -71.960087",
Movimiento,2026-01-19 12:56:18,2026-01-19 12:57:08,50s,30s,,0.13 Km,26 kph,25 kph,
Detenido,2026-01-19 12:57:08,2026-01-19 14:47:47,1h 50min 39s,30s,,"-36.430111, -71.959641",
Movimiento,2026-01-19 14:47:47,2026-01-19 14:49:48,2min 1s,0s,,0.21 Km,19 kph,15 kph,
Detenido,2026-01-19 14:49:48,2026-01-19 15:22:53,33min 5s,30s,,"-36.429325, -71.959565",
Movimiento,2026-01-19 15:22:53,2026-01-19 15:24:24,1min 31s,0s,,0.19 Km,24 kph,17 kph,
Detenido,2026-01-19 15:24:24,2026-01-19 15:30:59,6min 35s,30s,,"-36.428537, -71.960171",
Movimiento,2026-01-19 15:30:59,2026-01-19 15:32:00,1min 1s,0s,,0.17 Km,15 kph,11 kph,
Detenido,2026-01-19 15:32:00,2026-01-20 11:23:23,19h 51min 23s,4s,,"-36.430094, -71.959567",
Movimiento,2026-01-20 11:23:23,2026-01-20 11:27:52,4min 29s,0s,,1.23 Km,48 kph,30 kph,
Detenido,2026-01-20 11:27:52,2026-01-20 11:29:53,2min 1s,0s,,"-36.425702, -71.950476",
Movimiento,2026-01-20 11:29:53,2026-01-20 11:37:27,7min 34s,0s,,4.23 Km,74 kph,52 kph,
Detenido,2026-01-20 11:37:27,2026-01-20 12:01:29,24min 2s,0s,,"-36.462868, -71.958721",
Movimiento,2026-01-20 12:01:29,2026-01-20 12:05:01,3min 32s,0s,,1.52 Km,76 kph,48 kph,
Detenido,2026-01-20 12:05:01,2026-01-20 12:19:46,14min 45s,0s,,"-36.450223, -71.953796",
Movimiento,2026-01-20 12:19:46,2026-01-20 12:28:11,8min 25s,0s,,4.87 Km,61 kph,29 kph,
Detenido,2026-01-20 12:28:11,2026-01-20 12:37:09,8min 58s,0s,,"-36.4757, -71.949299",
Movimiento,2026-01-20 12:37:09,2026-01-20 12:49:47,12min 38s,0s,,12.47 Km,102 kph,63 kph,
Detenido,2026-01-20 12:49:47,2026-01-20 13:16:34,26min 47s,0s,,"-36.450156, -71.837502",
Movimiento,2026-01-20 13:16:34,2026-01-20 13:27:39,11min 5s,0s,,11.36 Km,102 kph,52 kph,
Detenido,2026-01-20 13:27:39,2026-01-20 13:28:40,1min 1s,0s,,"-36.426274, -71.947987",
Movimiento,2026-01-20 13:28:40,2026-01-20 13:33:42,5min 2s,0s,,1.23 Km,32 kph,19 kph,
Detenido,2026-01-20 13:33:42,2026-01-20 15:38:58,2h 5min 16s,0s,,"-36.430151, -71.959656",
Movimiento,2026-01-20 15:38:58,2026-01-20 15:39:11,13s,13s,,0 Km,6 kph,6 kph,
Detenido,2026-01-20 15:39:11,2026-01-21 10:22:46,18h 43min 35s,0s,,"-36.430192, -71.959668",
Movimiento,2026-01-21 10:22:46,2026-01-21 10:43:24,20min 38s,58s,,23.67 Km,122 kph,68 kph,
Detenido,2026-01-21 10:43:24,2026-01-21 11:06:58,23min 34s,0s,,"-36.271164, -71.825923",
Movimiento,2026-01-21 11:06:58,2026-01-21 11:31:42,24min 44s,31s,,21.39 Km,87 kph,48 kph,
Detenido,2026-01-21 11:31:42,2026-01-21 11:42:50,11min 8s,0s,,"-36.396515, -71.734745",
Movimiento,2026-01-21 11:42:50,2026-01-21 11:57:55,15min 5s,0s,,16.23 Km,107 kph,65 kph,
Detenido,2026-01-21 11:57:55,2026-01-21 12:11:04,13min 9s,2s,,"-36.40517, -71.868503",
Movimiento,2026-01-21 12:11:04,2026-01-21 12:11:33,29s,0s,,0 Km,6 kph,6 kph,
Detenido,2026-01-21 12:11:33,2026-01-21 12:37:16,25min 43s,0s,,"-36.405147, -71.868449",
Movimiento,2026-01-21 12:37:16,2026-01-21 12:54:51,17min 35s,0s,,13.61 Km,85 kph,40 kph,
Detenido,2026-01-21 12:54:51,2026-01-21 13:07:04,12min 13s,0s,,"-36.450158, -71.953911",
Movimiento,2026-01-21 13:07:04,2026-01-21 13:14:02,6min 58s,0s,,3.73 Km,69 kph,37 kph,
Detenido,2026-01-21 13:14:02,2026-01-22 08:32:46,19h 18min 44s,0s,,"-36.430188, -71.95965",
Movimiento,2026-01-22 08:32:46,2026-01-22 08:33:16,30s,0s,,0.01 Km,9 kph,9 kph,
Detenido,2026-01-22 08:33:16,2026-01-22 08:56:07,22min 51s,33s,,"-36.430079, -71.959653",
Movimiento,2026-01-22 08:56:07,2026-01-22 09:04:36,8min 29s,0s,,2.97 Km,33 kph,24 kph,
Detenido,2026-01-22 09:04:36,2026-01-22 09:09:41,5min 5s,0s,,"-36.423032, -71.975605",
Movimiento,2026-01-22 09:09:41,2026-01-22 09:18:13,8min 32s,0s,,2.69 Km,31 kph,17 kph,
Detenido,2026-01-22 09:18:13,2026-01-22 09:21:44,3min 31s,0s,,"-36.430124, -71.959602",
Movimiento,2026-01-22 09:21:44,2026-01-22 09:25:45,4min 1s,0s,,1.64 Km,38 kph,24 kph,
Detenido,2026-01-22 09:25:45,2026-01-22 09:39:52,14min 7s,0s,,"-36.422737, -71.952234",
Movimiento,2026-01-22 09:39:52,2026-01-22 09:41:21,1min 29s,54s,,0.32 Km,32 kph,26 kph,
Detenido,2026-01-22 09:41:21,2026-01-22 09:42:44,1min 23s,22s,,"-36.424872, -71.952401",
Movimiento,2026-01-22 09:42:44,2026-01-22 09:44:23,1min 39s,0s,,0.23 Km,37 kph,26 kph,
Detenido,2026-01-22 09:44:23,2026-01-22 09:46:18,1min 55s,0s,,"-36.425945, -71.94932",
Movimiento,2026-01-22 09:46:18,2026-01-22 09:57:00,10min 42s,0s,,8.49 Km,85 kph,42 kph,
Detenido,2026-01-22 09:57:00,2026-01-22 09:58:23,1min 23s,0s,,"-36.495427, -71.945883",
Movimiento,2026-01-22 09:58:23,2026-01-22 10:00:32,2min 9s,1min 31s,,0.48 Km,42 kph,34 kph,
Detenido,2026-01-22 10:00:32,2026-01-22 10:24:39,24min 7s,1min 10s,,"-36.494798, -71.93908",
Movimiento,2026-01-22 10:24:39,2026-01-22 10:38:08,13min 29s,0s,,10.06 Km,104 kph,46 kph,
Detenido,2026-01-22 10:38:08,2026-01-22 10:43:48,5min 40s,0s,,"-36.430113, -71.959583",
Movimiento,2026-01-22 10:43:48,2026-01-22 10:47:48,4min 0s,0s,,1.22 Km,47 kph,27 kph,
Detenido,2026-01-22 10:47:48,2026-01-22 10:48:47,59s,0s,,"-36.425899, -71.949314",
Movimiento,2026-01-22 10:48:47,2026-01-22 11:06:24,17min 37s,0s,,22.4 Km,113 kph,72 kph,
Detenido,2026-01-22 11:06:24,2026-01-22 11:33:26,27min 2s,30s,,"-36.271113, -71.826015",
Movimiento,2026-01-22 11:33:26,2026-01-22 11:49:45,16min 19s,2min 33s,,15.08 Km,109 kph,57 kph,
Detenido,2026-01-22 11:49:45,2026-01-22 11:51:16,1min 31s,1min 31s,,"-36.39276, -71.885807",
Movimiento,2026-01-22 11:51:16,2026-01-22 11:51:46,30s,0s,,1.71 Km,72 kph,72 kph,
Detenido,2026-01-22 11:51:46,2026-01-22 12:22:30,30min 44s,0s,,"-36.405188, -71.86843",
Movimiento,2026-01-22 12:22:30,2026-01-22 12:36:26,13min 56s,0s,,9.3 Km,87 kph,47 kph,
Detenido,2026-01-22 12:36:26,2026-01-22 12:58:10,21min 44s,31s,,"-36.4501, -71.837593",
Movimiento,2026-01-22 12:58:10,2026-01-22 13:11:46,13min 36s,0s,,10.97 Km,75 kph,52 kph,
Detenido,2026-01-22 13:11:46,2026-01-22 13:12:47,1min 1s,0s,,"-36.426162, -71.948061",
Movimiento,2026-01-22 13:12:47,2026-01-22 13:14:48,2min 1s,0s,,0.92 Km,43 kph,21 kph,
Detenido,2026-01-22 13:14:48,2026-01-22 13:17:50,3min 2s,0s,,"-36.424233, -71.958126",
Movimiento,2026-01-22 13:17:50,2026-01-22 13:20:52,3min 2s,0s,,1.35 Km,58 kph,29 kph,
Detenido,2026-01-22 13:20:52,2026-01-22 13:22:53,2min 1s,0s,,"-36.430558, -71.967293",
Movimiento,2026-01-22 13:22:53,2026-01-22 13:29:15,6min 22s,0s,,0.83 Km,37 kph,21 kph,
Detenido,2026-01-22 13:29:15,2026-01-22 14:29:47,1h 32s,0s,,"-36.43009, -71.959691",
Movimiento,2026-01-22 14:29:47,2026-01-22 14:29:49,2s,2s,,0 Km,7 kph,7 kph,
Detenido,2026-01-22 14:29:49,2026-01-23 08:28:51,17h 59min 2s,0s,,"-36.430087, -71.959661",
Movimiento,2026-01-23 08:28:51,2026-01-23 08:31:22,2min 31s,1min 31s,,0.28 Km,29 kph,15 kph,
Detenido,2026-01-23 08:31:22,2026-01-23 08:31:50,28s,28s,,"-36.434355, -71.961843",
Movimiento,2026-01-23 08:31:50,2026-01-23 08:43:00,11min 10s,0s,,8.06 Km,71 kph,36 kph,
Detenido,2026-01-23 08:43:00,2026-01-23 09:10:46,27min 46s,0s,,"-36.475641, -71.949576",
Movimiento,2026-01-23 09:10:46,2026-01-23 09:22:21,11min 35s,0s,,6.66 Km,75 kph,32 kph,
Detenido,2026-01-23 09:22:21,2026-01-23 09:25:22,3min 1s,30s,,"-36.428599, -71.949152",
Movimiento,2026-01-23 09:25:22,2026-01-23 09:25:53,31s,0s,,0.02 Km,15 kph,15 kph,
Detenido,2026-01-23 09:25:53,2026-01-23 09:27:38,1min 45s,0s,,"-36.426629, -71.948673",
Movimiento,2026-01-23 09:27:38,2026-01-23 09:29:55,2min 17s,54s,,0.41 Km,32 kph,17 kph,
Detenido,2026-01-23 09:29:55,2026-01-23 09:31:47,1min 52s,0s,,"-36.424603, -71.949514",
Movimiento,2026-01-23 09:31:47,2026-01-23 09:33:06,1min 19s,9s,,0.29 Km,27 kph,15 kph,
Detenido,2026-01-23 09:33:06,2026-01-23 09:38:02,4min 56s,18s,,"-36.422851, -71.950106",
Movimiento,2026-01-23 09:38:02,2026-01-23 09:40:16,2min 14s,0s,,0.23 Km,25 kph,15 kph,
Detenido,2026-01-23 09:40:16,2026-01-23 09:53:52,13min 36s,0s,,"-36.424547, -71.94954",
Movimiento,2026-01-23 09:53:52,2026-01-23 09:54:46,54s,24s,,0.25 Km,20 kph,16 kph,
Detenido,2026-01-23 09:54:46,2026-01-23 09:57:23,2min 37s,6s,,"-36.424171, -71.951336",
Movimiento,2026-01-23 09:57:23,2026-01-23 10:01:25,4min 2s,0s,,1.46 Km,49 kph,28 kph,
Detenido,2026-01-23 10:01:25,2026-01-23 10:03:07,1min 42s,0s,,"-36.429263, -71.958525",
Movimiento,2026-01-23 10:03:07,2026-01-23 10:06:59,3min 52s,1min 1s,,0.76 Km,40 kph,18 kph,
Detenido,2026-01-23 10:06:59,2026-01-23 10:07:21,22s,22s,,"-36.425061, -71.954066",
Movimiento,2026-01-23 10:07:21,2026-01-23 10:08:07,46s,8s,,0.36 Km,36 kph,18 kph,
Detenido,2026-01-23 10:08:07,2026-01-23 10:15:13,7min 6s,0s,,"-36.424222, -71.95119",
Movimiento,2026-01-23 10:15:13,2026-01-23 10:38:16,23min 3s,0s,,18.88 Km,94 kph,48 kph,
Detenido,2026-01-23 10:38:16,2026-01-23 10:49:21,11min 5s,1min 1s,,"-36.388189, -71.787167",
Movimiento,2026-01-23 10:49:21,2026-01-23 11:07:58,18min 37s,0s,,18.15 Km,88 kph,50 kph,
Detenido,2026-01-23 11:07:58,2026-01-23 11:09:09,1min 11s,0s,,"-36.426087, -71.948378",
Movimiento,2026-01-23 11:09:09,2026-01-23 11:10:30,1min 21s,0s,,0.64 Km,59 kph,29 kph,
Detenido,2026-01-23 11:10:30,2026-01-23 11:12:01,1min 31s,0s,,"-36.430419, -71.95264",
Movimiento,2026-01-23 11:12:01,2026-01-23 11:12:31,30s,0s,,0.51 Km,8 kph,8 kph,
Detenido,2026-01-23 11:12:31,2026-01-23 11:14:35,2min 4s,2s,,"-36.42931, -71.95823",
Movimiento,2026-01-23 11:14:35,2026-01-23 11:15:33,58s,0s,,0.08 Km,14 kph,11 kph,
Detenido,2026-01-23 11:15:33,2026-01-23 11:20:28,4min 55s,0s,,"-36.43006, -71.959601",
Movimiento,2026-01-23 11:20:28,2026-01-23 11:21:36,1min 8s,28s,,0.03 Km,11 kph,7 kph,
Detenido,2026-01-23 11:21:36,2026-01-23 11:23:07,1min 31s,1min 31s,,"-36.430736, -71.957543",
Movimiento,2026-01-23 11:23:07,2026-01-23 11:25:39,2min 32s,0s,,1.17 Km,44 kph,27 kph,
Detenido,2026-01-23 11:25:39,2026-01-23 12:05:54,40min 15s,25s,,"-36.423143, -71.95246",
Movimiento,2026-01-23 12:05:54,2026-01-23 12:07:30,1min 36s,0s,,0.24 Km,25 kph,13 kph,
Detenido,2026-01-23 12:07:30,2026-01-23 12:35:27,27min 57s,1min 0s,,"-36.422775, -71.952301",
Movimiento,2026-01-23 12:35:27,2026-01-23 12:40:30,5min 3s,0s,,0.87 Km,40 kph,22 kph,
Detenido,2026-01-23 12:40:30,2026-01-23 12:58:15,17min 45s,0s,,"-36.426738, -71.965095",
Movimiento,2026-01-23 12:58:15,2026-01-23 13:00:15,2min 0s,0s,,0.64 Km,36 kph,25 kph,
Detenido,2026-01-23 13:00:15,2026-01-23 13:02:33,2min 18s,0s,,"-36.430174, -71.959662",
Movimiento,2026-01-23 13:02:33,2026-01-23 13:04:06,1min 33s,1min 33s,,0.01 Km,9 kph,9 kph,
Detenido,2026-01-23 13:04:06,2026-01-23 17:20:14,4h 16min 8s,0s,,"-36.430108, -71.959631",
Movimiento,2026-01-23 17:20:14,2026-01-23 17:23:46,3min 32s,0s,,1.16 Km,29 kph,16 kph,
Detenido,2026-01-23 17:23:46,2026-01-23 17:24:46,1min 0s,0s,,"-36.425657, -71.95097",
Movimiento,2026-01-23 17:24:46,2026-01-23 17:43:57,19min 11s,0s,,10.92 Km,74 kph,42 kph,
Detenido,2026-01-23 17:43:57,2026-01-23 18:04:34,20min 37s,0s,,"-36.45007, -71.837597",
Movimiento,2026-01-23 18:04:34,2026-01-23 18:24:26,19min 52s,0s,,12.65 Km,82 kph,35 kph,
Detenido,2026-01-23 18:24:26,2026-01-23 18:25:57,1min 31s,0s,,"-36.430162, -71.9596",
Movimiento,2026-01-23 18:25:57,2026-01-23 18:27:58,2min 1s,0s,,0.14 Km,22 kph,18 kph,
Detenido,2026-01-23 18:27:58,2026-01-23 18:43:13,15min 15s,6min 40s,,"-36.429263, -71.959541",
Movimiento,2026-01-23 18:43:13,2026-01-23 18:46:05,2min 52s,0s,,0.48 Km,30 kph,18 kph,
Detenido,2026-01-23 18:46:05,2026-01-23 19:03:51,17min 46s,44s,,"-36.42845, -71.960091",
Movimiento,2026-01-23 19:03:51,2026-01-23 19:04:21,30s,30s,,0.12 Km,20 kph,20 kph,
Detenido,2026-01-23 19:04:21,2026-01-24 08:49:31,13h 45min 10s,0s,,"-36.430107, -71.959606",
Movimiento,2026-01-24 08:49:31,2026-01-24 08:51:11,1min 40s,0s,,0.54 Km,32 kph,20 kph,
Detenido,2026-01-24 08:51:11,2026-01-24 09:04:25,13min 14s,0s,,"-36.428878, -71.953878",
Movimiento,2026-01-24 09:04:25,2026-01-24 09:06:57,2min 32s,0s,,0.2 Km,22 kph,14 kph,
Detenido,2026-01-24 09:06:57,2026-01-24 09:08:04,1min 7s,0s,,"-36.429299, -71.958462",
Movimiento,2026-01-24 09:08:04,2026-01-24 09:10:58,2min 54s,30s,,0.38 Km,17 kph,11 kph,
Detenido,2026-01-24 09:10:58,2026-01-24 09:13:40,2min 42s,4s,,"-36.430102, -71.959646",
Movimiento,2026-01-24 09:13:40,2026-01-24 09:17:01,3min 21s,0s,,1.33 Km,44 kph,20 kph,
Detenido,2026-01-24 09:17:01,2026-01-24 09:18:32,1min 31s,0s,,"-36.425918, -71.94944",
Movimiento,2026-01-24 09:18:32,2026-01-24 09:34:42,16min 10s,0s,,22.8 Km,118 kph,71 kph,
Detenido,2026-01-24 09:34:42,2026-01-24 09:53:59,19min 17s,8s,,"-36.271152, -71.825879",
Movimiento,2026-01-24 09:53:59,2026-01-24 09:54:51,52s,0s,,0.12 Km,18 kph,15 kph,
Detenido,2026-01-24 09:54:51,2026-01-24 09:56:22,1min 31s,0s,,"-36.272539, -71.826378",
Movimiento,2026-01-24 09:56:22,2026-01-24 10:24:21,27min 59s,0s,,33.05 Km,116 kph,68 kph,
Detenido,2026-01-24 10:24:21,2026-01-24 10:47:59,23min 38s,1s,,"-36.495196, -71.938919",
Movimiento,2026-01-24 10:47:59,2026-01-24 11:02:06,14min 7s,0s,,12.91 Km,98 kph,46 kph,
Detenido,2026-01-24 11:02:06,2026-01-24 11:22:50,20min 44s,0s,,"-36.450069, -71.837467",
Movimiento,2026-01-24 11:22:50,2026-01-24 11:37:28,14min 38s,0s,,12.21 Km,100 kph,58 kph,
Detenido,2026-01-24 11:37:28,2026-01-24 11:38:29,1min 1s,0s,,"-36.426293, -71.947314",
Movimiento,2026-01-24 11:38:29,2026-01-24 11:40:00,1min 31s,0s,,0 Km,8 kph,8 kph,
Detenido,2026-01-24 11:40:00,2026-01-24 11:40:30,30s,0s,,"-36.426153, -71.948009",
Movimiento,2026-01-24 11:40:30,2026-01-24 11:46:22,5min 52s,0s,,1.57 Km,74 kph,29 kph,
Detenido,2026-01-24 11:46:22,2026-01-24 11:50:38,4min 16s,0s,,"-36.414297, -71.948257",
Movimiento,2026-01-24 11:50:38,2026-01-24 11:52:57,2min 19s,0s,,0.66 Km,29 kph,14 kph,
Detenido,2026-01-24 11:52:57,2026-01-24 12:18:17,25min 20s,0s,,"-36.418958, -71.949379",
Movimiento,2026-01-24 12:18:17,2026-01-24 12:20:49,2min 32s,0s,,0.65 Km,43 kph,27 kph,
Detenido,2026-01-24 12:20:49,2026-01-24 12:21:49,1min 0s,0s,,"-36.416874, -71.959483",
Movimiento,2026-01-24 12:21:49,2026-01-24 12:26:21,4min 32s,0s,,1.38 Km,51 kph,27 kph,
Detenido,2026-01-24 12:26:21,2026-01-24 12:40:47,14min 26s,0s,,"-36.426747, -71.964987",
Movimiento,2026-01-24 12:40:47,2026-01-24 12:41:17,30s,30s,,0.16 Km,41 kph,41 kph,
Detenido,2026-01-24 12:41:17,2026-01-24 12:42:48,1min 31s,1min 31s,,"-36.427398, -71.961496",
Movimiento,2026-01-24 12:42:48,2026-01-24 12:44:18,1min 30s,30s,,0.59 Km,41 kph,31 kph,
Detenido,2026-01-24 12:44:18,2026-01-24 12:45:19,1min 1s,1min 1s,,"-36.426304, -71.954523",
Movimiento,2026-01-24 12:45:19,2026-01-24 12:46:19,1min 0s,0s,,0.42 Km,27 kph,17 kph,
Detenido,2026-01-24 12:46:19,2026-01-24 13:07:09,20min 50s,0s,,"-36.424286, -71.951188",
Movimiento,2026-01-24 13:07:09,2026-01-24 13:11:22,4min 13s,0s,,0.77 Km,46 kph,17 kph,
Detenido,2026-01-24 13:11:22,2026-01-24 13:13:53,2min 31s,0s,,"-36.426665, -71.951982",
Movimiento,2026-01-24 13:13:53,2026-01-24 13:14:23,30s,0s,,0.03 Km,7 kph,7 kph,
Detenido,2026-01-24 13:14:23,2026-01-24 13:27:28,13min 5s,0s,,"-36.426339, -71.951263",
Movimiento,2026-01-24 13:27:28,2026-01-24 13:33:01,5min 33s,1min 1s,,1.29 Km,40 kph,23 kph,
Detenido,2026-01-24 13:33:01,2026-01-24 13:33:23,22s,22s,,"-36.429872, -71.955607",
Movimiento,2026-01-24 13:33:23,2026-01-24 13:38:34,5min 11s,0s,,1.43 Km,36 kph,19 kph,
Detenido,2026-01-24 13:38:34,2026-01-25 10:02:58,20h 24min 24s,0s,,"-36.430166, -71.959611",
Movimiento,2026-01-25 10:02:58,2026-01-25 10:04:59,2min 1s,0s,,0.95 Km,43 kph,43 kph,
Detenido,2026-01-25 10:04:59,2026-01-25 10:06:20,1min 21s,0s,,"-36.425951, -71.949252",
Movimiento,2026-01-25 10:06:20,2026-01-25 10:16:35,10min 15s,0s,,7.24 Km,79 kph,46 kph,
Detenido,2026-01-25 10:16:35,2026-01-25 10:33:24,16min 49s,0s,,"-36.475704, -71.949272",
Movimiento,2026-01-25 10:33:24,2026-01-25 10:38:14,4min 50s,0s,,2.84 Km,55 kph,32 kph,
Detenido,2026-01-25 10:38:14,2026-01-25 10:58:00,19min 46s,0s,,"-36.495151, -71.938904",
Movimiento,2026-01-25 10:58:00,2026-01-25 11:11:34,13min 34s,0s,,12.75 Km,85 kph,60 kph,
Detenido,2026-01-25 11:11:34,2026-01-25 11:27:33,15min 59s,0s,,"-36.450076, -71.83747",
Movimiento,2026-01-25 11:27:33,2026-01-25 11:43:12,15min 39s,32s,,13.05 Km,106 kph,58 kph,
Detenido,2026-01-25 11:43:12,2026-01-25 12:05:18,22min 6s,13s,,"-36.418936, -71.949229",
Movimiento,2026-01-25 12:05:18,2026-01-25 12:08:06,2min 48s,0s,,0.52 Km,27 kph,15 kph,
Detenido,2026-01-25 12:08:06,2026-01-25 12:31:02,22min 56s,0s,,"-36.420849, -71.952657",
Movimiento,2026-01-25 12:31:02,2026-01-25 12:33:04,2min 2s,0s,,0.49 Km,27 kph,17 kph,
Detenido,2026-01-25 12:33:04,2026-01-25 12:51:01,17min 57s,9s,,"-36.423149, -71.952442",
Movimiento,2026-01-25 12:51:01,2026-01-25 12:51:53,52s,0s,,0.06 Km,34 kph,21 kph,
Detenido,2026-01-25 12:51:53,2026-01-25 13:10:32,18min 39s,0s,,"-36.424217, -71.951226",
Movimiento,2026-01-25 13:10:32,2026-01-25 13:15:09,4min 37s,0s,,1.68 Km,47 kph,26 kph,
Detenido,2026-01-25 13:15:09,2026-01-25 13:18:41,3min 32s,0s,,"-36.430245, -71.953646",
Movimiento,2026-01-25 13:18:41,2026-01-25 13:19:41,1min 0s,0s,,0.24 Km,39 kph,34 kph,
Detenido,2026-01-25 13:19:41,2026-01-25 14:42:28,1h 22min 47s,50s,,"-36.43007, -71.959608",
Movimiento,2026-01-25 14:42:28,2026-01-25 14:44:18,1min 50s,0s,,0.4 Km,26 kph,15 kph,
Detenido,2026-01-25 14:44:18,2026-01-25 15:25:29,41min 11s,0s,,"-36.432462, -71.956056",
Movimiento,2026-01-25 15:25:29,2026-01-25 15:33:09,7min 40s,30s,,2.87 Km,50 kph,33 kph,
Detenido,2026-01-25 15:33:09,2026-01-25 15:48:50,15min 41s,0s,,"-36.423493, -71.975796",
Movimiento,2026-01-25 15:48:50,2026-01-25 15:55:52,7min 2s,0s,,2.11 Km,49 kph,24 kph,
Detenido,2026-01-25 15:55:52,2026-01-25 16:01:29,5min 37s,0s,,"-36.42851, -71.960307",
Movimiento,2026-01-25 16:01:29,2026-01-25 16:02:37,1min 8s,0s,,0.11 Km,16 kph,16 kph,
Detenido,2026-01-25 16:02:37,2026-01-25 16:04:31,1min 54s,24s,,"-36.430106, -71.959602",
Movimiento,2026-01-25 16:04:31,2026-01-25 16:06:07,1min 36s,0s,,0.14 Km,24 kph,19 kph,
Detenido,2026-01-25 16:06:07,2026-01-25 16:26:25,20min 18s,20s,,"-36.429263, -71.959532",
Movimiento,2026-01-25 16:26:25,2026-01-25 16:27:56,1min 31s,0s,,0.11 Km,13 kph,13 kph,
Detenido,2026-01-25 16:27:56,2026-01-26 08:28:27,16h 31s,49s,,"-36.430144, -71.959615",
Movimiento,2026-01-26 08:28:27,2026-01-26 08:29:09,42s,0s,,0.04 Km,15 kph,11 kph,
Detenido,2026-01-26 08:29:09,2026-01-26 08:32:41,3min 32s,0s,,"-36.430425, -71.959268",
Movimiento,2026-01-26 08:32:41,2026-01-26 08:34:12,1min 31s,0s,,0.28 Km,19 kph,14 kph,
Detenido,2026-01-26 08:34:12,2026-01-26 08:38:17,4min 5s,0s,,"-36.434505, -71.961197",
Movimiento,2026-01-26 08:38:17,2026-01-26 08:50:20,12min 3s,0s,,7.12 Km,76 kph,47 kph,
Detenido,2026-01-26 08:50:20,2026-01-26 09:22:34,32min 14s,0s,,"-36.475645, -71.949247",
Movimiento,2026-01-26 09:22:34,2026-01-26 09:32:08,9min 34s,1min 30s,,6.16 Km,69 kph,41 kph,
Detenido,2026-01-26 09:32:08,2026-01-26 09:35:30,3min 22s,0s,,"-36.426993, -71.948793",
Movimiento,2026-01-26 09:35:30,2026-01-26 09:39:41,4min 11s,0s,,0.57 Km,16 kph,11 kph,
Detenido,2026-01-26 09:39:41,2026-01-26 10:14:50,35min 9s,0s,,"-36.426068, -71.951223",
Movimiento,2026-01-26 10:14:50,2026-01-26 10:15:33,43s,0s,,0.01 Km,9 kph,9 kph,
Detenido,2026-01-26 10:15:33,2026-01-26 10:36:33,21min 0s,0s,,"-36.424582, -71.949485",
Movimiento,2026-01-26 10:36:33,2026-01-26 10:38:04,1min 31s,0s,,0.3 Km,24 kph,20 kph,
Detenido,2026-01-26 10:38:04,2026-01-26 11:30:12,52min 8s,0s,,"-36.42315, -71.952431",
Movimiento,2026-01-26 11:30:12,2026-01-26 11:31:18,1min 6s,0s,,0.28 Km,23 kph,18 kph,
Detenido,2026-01-26 11:31:18,2026-01-26 11:58:59,27min 41s,0s,,"-36.422718, -71.952284",
Movimiento,2026-01-26 11:58:59,2026-01-26 12:02:00,3min 1s,5s,,0.34 Km,27 kph,17 kph,
Detenido,2026-01-26 12:02:00,2026-01-26 12:21:38,19min 38s,30s,,"-36.421025, -71.952694",
Movimiento,2026-01-26 12:21:38,2026-01-26 12:25:12,3min 34s,0s,,0.84 Km,27 kph,19 kph,
Detenido,2026-01-26 12:25:12,2026-01-26 12:29:14,4min 2s,0s,,"-36.424947, -71.958877",
Movimiento,2026-01-26 12:29:14,2026-01-26 12:32:14,3min 0s,30s,,0.62 Km,24 kph,17 kph,
Detenido,2026-01-26 12:32:14,2026-01-26 12:47:50,15min 36s,0s,,"-36.430116, -71.959721",
Movimiento,2026-01-26 12:47:50,2026-01-26 12:48:37,47s,0s,,0.01 Km,7 kph,7 kph,
Detenido,2026-01-26 12:48:37,2026-01-26 14:34:11,1h 45min 34s,0s,,"-36.430118, -71.959633",
Movimiento,2026-01-26 14:34:11,2026-01-26 14:48:59,14min 48s,0s,,12.67 Km,109 kph,49 kph,
Detenido,2026-01-26 14:48:59,2026-01-26 15:19:16,30min 17s,0s,,"-36.405213, -71.86848",
Movimiento,2026-01-26 15:19:16,2026-01-26 15:31:53,12min 37s,0s,,9.8 Km,86 kph,49 kph,
Detenido,2026-01-26 15:31:53,2026-01-26 15:33:52,1min 59s,0s,,"-36.426101, -71.948262",
Movimiento,2026-01-26 15:33:52,2026-01-26 15:35:54,2min 2s,0s,,1.43 Km,75 kph,33 kph,
Detenido,2026-01-26 15:35:54,2026-01-26 15:40:25,4min 31s,0s,,"-36.417527, -71.951976",
Movimiento,2026-01-26 15:40:25,2026-01-26 15:44:45,4min 20s,0s,,0.15 Km,40 kph,40 kph,
Detenido,2026-01-26 15:44:45,2026-01-26 16:02:49,18min 4s,0s,,"-36.418853, -71.952314",
Movimiento,2026-01-26 16:02:49,2026-01-26 16:04:50,2min 1s,30s,,0.52 Km,27 kph,24 kph,
Detenido,2026-01-26 16:04:50,2026-01-26 16:06:38,1min 48s,1min 48s,,"-36.423991, -71.95534",
Movimiento,2026-01-26 16:06:38,2026-01-26 16:07:22,44s,44s,,0.33 Km,14 kph,14 kph,
Detenido,2026-01-26 16:07:22,2026-01-26 16:09:34,2min 12s,0s,,"-36.425059, -71.958848",
Movimiento,2026-01-26 16:09:34,2026-01-26 16:11:54,2min 20s,30s,,0.46 Km,26 kph,22 kph,
Detenido,2026-01-26 16:11:54,2026-01-26 16:14:01,2min 7s,0s,,"-36.429766, -71.960485",
Movimiento,2026-01-26 16:14:01,2026-01-26 16:17:57,3min 56s,0s,,1.03 Km,18 kph,9 kph,
Detenido,2026-01-26 16:17:57,2026-01-26 16:38:10,20min 13s,1min 10s,,"-36.426773, -71.964931",
Movimiento,2026-01-26 16:38:10,2026-01-26 16:39:31,1min 21s,0s,,0.08 Km,31 kph,31 kph,
Detenido,2026-01-26 16:39:31,2026-01-26 16:40:34,1min 3s,3s,,"-36.429954, -71.962187",
Movimiento,2026-01-26 16:40:34,2026-01-26 16:42:02,1min 28s,0s,,0.22 Km,13 kph,11 kph,
Detenido,2026-01-26 16:42:02,2026-01-27 00:55:04,8h 13min 2s,0s,,"-36.430117, -71.959631",
Movimiento,2026-01-27 00:55:04,2026-01-27 00:55:12,8s,0s,,0.01 Km,10 kph,10 kph,
Detenido,2026-01-27 00:55:12,2026-01-27 08:27:05,7h 31min 53s,0s,,"-36.430063, -71.959541",
Movimiento,2026-01-27 08:27:05,2026-01-27 08:29:36,2min 31s,0s,,0.32 Km,21 kph,18 kph,
Detenido,2026-01-27 08:29:36,2026-01-27 08:38:49,9min 13s,0s,,"-36.427505, -71.958139",
Movimiento,2026-01-27 08:38:49,2026-01-27 08:40:10,1min 21s,0s,,0.25 Km,29 kph,26 kph,
Detenido,2026-01-27 08:40:10,2026-01-27 08:41:41,1min 31s,0s,,"-36.428652, -71.960115",
Movimiento,2026-01-27 08:41:41,2026-01-27 08:54:53,13min 12s,58s,,8.86 Km,66 kph,33 kph,
Detenido,2026-01-27 08:54:53,2026-01-27 09:41:54,47min 1s,0s,,"-36.475671, -71.94943",
Movimiento,2026-01-27 09:41:54,2026-01-27 09:50:28,8min 34s,0s,,5.95 Km,79 kph,37 kph,
Detenido,2026-01-27 09:50:28,2026-01-27 09:50:37,9s,0s,,"-36.433944, -71.951743",
Movimiento,2026-01-27 09:50:37,2026-01-27 09:52:29,1min 52s,0s,,0.73 Km,55 kph,33 kph,
Detenido,2026-01-27 09:52:29,2026-01-27 09:55:56,3min 27s,0s,,"-36.427219, -71.948799",
Movimiento,2026-01-27 09:55:56,2026-01-27 09:58:02,2min 6s,0s,,0.08 Km,21 kph,19 kph,
Detenido,2026-01-27 09:58:02,2026-01-27 10:25:16,27min 14s,0s,,"-36.426102, -71.951167",
Movimiento,2026-01-27 10:25:16,2026-01-27 10:26:47,1min 31s,0s,,0.15 Km,11 kph,9 kph,
Detenido,2026-01-27 10:26:47,2026-01-27 10:50:51,24min 4s,0s,,"-36.424574, -71.94945",
Movimiento,2026-01-27 10:50:51,2026-01-27 10:52:26,1min 35s,0s,,0.15 Km,33 kph,26 kph,
Detenido,2026-01-27 10:52:26,2026-01-27 11:28:48,36min 22s,36s,,"-36.42313, -71.952477",
Movimiento,2026-01-27 11:28:48,2026-01-27 11:30:43,1min 55s,0s,,0.35 Km,33 kph,20 kph,
Detenido,2026-01-27 11:30:43,2026-01-27 12:18:49,48min 6s,18s,,"-36.422742, -71.952291",
Movimiento,2026-01-27 12:18:49,2026-01-27 12:23:35,4min 46s,0s,,1.22 Km,44 kph,23 kph,
Detenido,2026-01-27 12:23:35,2026-01-27 12:40:45,17min 10s,0s,,"-36.426659, -71.96502",
Movimiento,2026-01-27 12:40:45,2026-01-27 12:42:16,1min 31s,22s,,0.5 Km,7 kph,7 kph,
Detenido,2026-01-27 12:42:16,2026-01-27 16:41:28,3h 59min 12s,28s,,"-36.430039, -71.959816",
Movimiento,2026-01-27 16:41:28,2026-01-27 16:42:28,1min 0s,0s,,0.06 Km,10 kph,9 kph,
Detenido,2026-01-27 16:42:28,2026-01-27 16:43:29,1min 1s,0s,,"-36.429402, -71.95879",
Movimiento,2026-01-27 16:43:29,2026-01-27 16:44:29,1min 0s,0s,,0.05 Km,6 kph,6 kph,
Detenido,2026-01-27 16:44:29,2026-01-27 17:24:25,39min 56s,42s,,"-36.429314, -71.959558",
Movimiento,2026-01-27 17:24:25,2026-01-27 17:26:16,1min 51s,0s,,0.21 Km,17 kph,12 kph,
Detenido,2026-01-27 17:26:16,2026-01-28 08:38:24,15h 12min 8s,0s,,"-36.43015, -71.959622",
Movimiento,2026-01-28 08:38:24,2026-01-28 08:54:01,15min 37s,0s,,8.8 Km,83 kph,29 kph,
Detenido,2026-01-28 08:54:01,2026-01-28 09:45:22,51min 21s,0s,,"-36.475677, -71.949281",
Movimiento,2026-01-28 09:45:22,2026-01-28 09:57:56,12min 34s,0s,,8.3 Km,92 kph,40 kph,
Detenido,2026-01-28 09:57:56,2026-01-28 10:26:57,29min 1s,0s,,"-36.432051, -71.956404",
Movimiento,2026-01-28 10:26:57,2026-01-28 10:30:27,3min 30s,0s,,0.95 Km,26 kph,16 kph,
Detenido,2026-01-28 10:30:27,2026-01-28 11:01:32,31min 5s,0s,,"-36.426094, -71.9512",
Movimiento,2026-01-28 11:01:32,2026-01-28 11:02:13,41s,0s,,0.01 Km,10 kph,10 kph,
Detenido,2026-01-28 11:02:13,2026-01-28 11:45:02,42min 49s,0s,,"-36.424629, -71.949425",
Movimiento,2026-01-28 11:45:02,2026-01-28 11:46:33,1min 31s,0s,,0.21 Km,35 kph,23 kph,
Detenido,2026-01-28 11:46:33,2026-01-28 11:48:04,1min 31s,0s,,"-36.422777, -71.952327",
Movimiento,2026-01-28 11:48:04,2026-01-28 11:49:04,1min 0s,27s,,0.46 Km,47 kph,38 kph,
Detenido,2026-01-28 11:49:04,2026-01-28 11:57:06,8min 2s,14s,,"-36.423822, -71.950465",
Movimiento,2026-01-28 11:57:06,2026-01-28 11:57:50,44s,44s,,0.07 Km,16 kph,16 kph,
Detenido,2026-01-28 11:57:50,2026-01-28 12:08:57,11min 7s,0s,,"-36.422781, -71.952173",
Movimiento,2026-01-28 12:08:57,2026-01-28 12:09:57,1min 0s,0s,,0 Km,8 kph,8 kph,
Detenido,2026-01-28 12:09:57,2026-01-28 12:14:34,4min 37s,0s,,"-36.420887, -71.952664",
Movimiento,2026-01-28 12:14:34,2026-01-28 12:15:30,56s,0s,,0 Km,7 kph,7 kph,
Detenido,2026-01-28 12:15:30,2026-01-28 12:19:35,4min 5s,0s,,"-36.420826, -71.952725",
Movimiento,2026-01-28 12:19:35,2026-01-28 12:21:02,1min 27s,0s,,0.31 Km,42 kph,21 kph,
Detenido,2026-01-28 12:21:02,2026-01-28 12:43:05,22min 3s,0s,,"-36.423192, -71.952305",
Movimiento,2026-01-28 12:43:05,2026-01-28 12:46:37,3min 32s,0s,,0.88 Km,34 kph,30 kph,
Detenido,2026-01-28 12:46:37,2026-01-28 12:47:21,44s,0s,,"-36.428993, -71.96002",
Movimiento,2026-01-28 12:47:21,2026-01-28 12:48:07,46s,0s,,0.13 Km,12 kph,12 kph,
Detenido,2026-01-28 12:48:07,2026-01-28 14:35:12,1h 47min 5s,0s,,"-36.430087, -71.959701",
Movimiento,2026-01-28 14:35:12,2026-01-28 14:38:13,3min 1s,13s,,0.95 Km,35 kph,24 kph,
Detenido,2026-01-28 14:38:13,2026-01-28 14:43:47,5min 34s,0s,,"-36.426752, -71.965054",
Movimiento,2026-01-28 14:43:47,2026-01-28 14:44:47,1min 0s,0s,,0.39 Km,37 kph,37 kph,
Detenido,2026-01-28 14:44:47,2026-01-28 14:45:50,1min 3s,0s,,"-36.427959, -71.958511",
Movimiento,2026-01-28 14:45:50,2026-01-28 14:59:36,13min 46s,1min 44s,,10.63 Km,121 kph,53 kph,
Detenido,2026-01-28 14:59:36,2026-01-28 15:26:21,26min 45s,0s,,"-36.405136, -71.868456",
Movimiento,2026-01-28 15:26:21,2026-01-28 15:32:24,6min 3s,0s,,4.15 Km,73 kph,41 kph,
Detenido,2026-01-28 15:32:24,2026-01-28 15:32:51,27s,0s,,"-36.433699, -71.874903",
Movimiento,2026-01-28 15:32:51,2026-01-28 15:46:30,13min 39s,0s,,8.18 Km,81 kph,36 kph,
Detenido,2026-01-28 15:46:30,2026-01-29 08:24:36,16h 38min 6s,0s,,"-36.430059, -71.959528",
Movimiento,2026-01-29 08:24:36,2026-01-29 08:26:57,2min 21s,0s,,0.57 Km,30 kph,18 kph,
Detenido,2026-01-29 08:26:57,2026-01-29 08:45:38,18min 41s,0s,,"-36.426117, -71.951154",
Movimiento,2026-01-29 08:45:38,2026-01-29 08:57:13,11min 35s,0s,,11.76 Km,121 kph,68 kph,
Detenido,2026-01-29 08:57:13,2026-01-29 09:19:58,22min 45s,11s,,"-36.405158, -71.868407",
Movimiento,2026-01-29 09:19:58,2026-01-29 09:27:15,7min 17s,0s,,5.12 Km,74 kph,49 kph,
Detenido,2026-01-29 09:27:15,2026-01-29 09:52:00,24min 45s,0s,,"-36.411868, -71.907024",
Movimiento,2026-01-29 09:52:00,2026-01-29 09:59:00,7min 0s,0s,,4.03 Km,66 kph,38 kph,
Detenido,2026-01-29 09:59:00,2026-01-29 10:10:00,11min 0s,0s,,"-36.420863, -71.952676",
Movimiento,2026-01-29 10:10:00,2026-01-29 10:11:07,1min 7s,0s,,0.19 Km,39 kph,39 kph,
Detenido,2026-01-29 10:11:07,2026-01-29 10:25:38,14min 31s,0s,,"-36.422815, -71.952257",
Movimiento,2026-01-29 10:25:38,2026-01-29 10:27:35,1min 57s,0s,,0.42 Km,35 kph,24 kph,
Detenido,2026-01-29 10:27:35,2026-01-29 10:58:17,30min 42s,0s,,"-36.423148, -71.952458",
Movimiento,2026-01-29 10:58:17,2026-01-29 10:59:52,1min 35s,48s,,0.28 Km,8 kph,7 kph,
Detenido,2026-01-29 10:59:52,2026-01-29 11:04:21,4min 29s,30s,,"-36.424502, -71.95656",
Movimiento,2026-01-29 11:04:21,2026-01-29 11:07:26,3min 5s,0s,,1.02 Km,49 kph,31 kph,
Detenido,2026-01-29 11:07:26,2026-01-29 11:14:21,6min 55s,0s,,"-36.43009, -71.960728",
Movimiento,2026-01-29 11:14:21,2026-01-29 11:16:58,2min 37s,0s,,0.54 Km,28 kph,20 kph,
Detenido,2026-01-29 11:16:58,2026-01-29 11:22:03,5min 5s,0s,,"-36.426798, -71.964947",
Movimiento,2026-01-29 11:22:03,2026-01-29 11:23:01,58s,0s,,0.46 Km,38 kph,28 kph,
Detenido,2026-01-29 11:23:01,2026-01-29 11:30:02,7min 1s,0s,,"-36.428584, -71.960415",
Movimiento,2026-01-29 11:30:02,2026-01-29 11:31:32,1min 30s,0s,,0.59 Km,31 kph,19 kph,
Detenido,2026-01-29 11:31:32,2026-01-29 12:36:31,1h 4min 59s,0s,,"-36.431922, -71.95653",
Movimiento,2026-01-29 12:36:31,2026-01-29 12:40:33,4min 2s,0s,,0.62 Km,29 kph,20 kph,
Detenido,2026-01-29 12:40:33,2026-01-29 14:36:07,1h 55min 34s,36s,,"-36.430141, -71.95968",
Movimiento,2026-01-29 14:36:07,2026-01-29 14:37:56,1min 49s,59s,,0.16 Km,29 kph,20 kph,
Detenido,2026-01-29 14:37:56,2026-01-29 15:41:32,1h 3min 36s,0s,,"-36.429314, -71.959566",
Movimiento,2026-01-29 15:41:32,2026-01-29 15:43:30,1min 58s,1min 26s,,0.15 Km,26 kph,22 kph,
Detenido,2026-01-29 15:43:30,2026-01-30 08:38:31,16h 55min 1s,0s,,"-36.430019, -71.959628",
Movimiento,2026-01-30 08:38:31,2026-01-30 08:53:18,14min 47s,0s,,12.68 Km,111 kph,51 kph,
Detenido,2026-01-30 08:53:18,2026-01-30 09:16:18,23min 0s,0s,,"-36.405163, -71.868448",
Movimiento,2026-01-30 09:16:18,2026-01-30 09:30:30,14min 12s,0s,,11.35 Km,93 kph,56 kph,
Detenido,2026-01-30 09:30:30,2026-01-30 09:49:25,18min 55s,0s,,"-36.42611, -71.951135",
Movimiento,2026-01-30 09:49:25,2026-01-30 09:51:12,1min 47s,0s,,0.33 Km,13 kph,10 kph,
Detenido,2026-01-30 09:51:12,2026-01-30 10:23:03,31min 51s,0s,,"-36.423151, -71.952411",
Movimiento,2026-01-30 10:23:03,2026-01-30 10:24:53,1min 50s,0s,,0.42 Km,30 kph,16 kph,
Detenido,2026-01-30 10:24:53,2026-01-30 11:01:17,36min 24s,0s,,"-36.422712, -71.952294",
Movimiento,2026-01-30 11:01:17,2026-01-30 11:07:14,5min 57s,0s,,1.38 Km,36 kph,20 kph,
Detenido,2026-01-30 11:07:14,2026-01-30 11:33:58,26min 44s,28s,,"-36.419614, -71.967518",
Movimiento,2026-01-30 11:33:58,2026-01-30 11:36:29,2min 31s,0s,,0.42 Km,35 kph,27 kph,
Detenido,2026-01-30 11:36:29,2026-01-30 11:36:59,30s,0s,,"-36.422938, -71.964807",
Movimiento,2026-01-30 11:36:59,2026-01-30 11:38:00,1min 1s,54s,,0.21 Km,36 kph,28 kph,
Detenido,2026-01-30 11:38:00,2026-01-30 12:18:28,40min 28s,0s,,"-36.426727, -71.965037",
Movimiento,2026-01-30 12:18:28,2026-01-30 12:21:24,2min 56s,0s,,0.68 Km,22 kph,15 kph,
Detenido,2026-01-30 12:21:24,2026-01-30 12:50:30,29min 6s,0s,,"-36.432017, -71.956416",
Movimiento,2026-01-30 12:50:30,2026-01-30 12:55:37,5min 7s,0s,,1.93 Km,45 kph,27 kph,
Detenido,2026-01-30 12:55:37,2026-01-30 13:06:12,10min 35s,0s,,"-36.416126, -71.949126",
Movimiento,2026-01-30 13:06:12,2026-01-30 13:11:10,4min 58s,1min 1s,,1.4 Km,26 kph,19 kph,
Detenido,2026-01-30 13:11:10,2026-01-30 13:11:40,30s,30s,,"-36.424863, -71.958851",
Movimiento,2026-01-30 13:11:40,2026-01-30 13:12:10,30s,0s,,0.06 Km,10 kph,10 kph,
Detenido,2026-01-30 13:12:10,2026-01-30 13:13:41,1min 31s,0s,,"-36.426186, -71.95934",
Movimiento,2026-01-30 13:13:41,2026-01-30 13:15:42,2min 1s,0s,,0.46 Km,27 kph,19 kph,
Detenido,2026-01-30 13:15:42,2026-01-30 17:00:42,3h 45min 0s,0s,,"-36.430166, -71.959645",
Movimiento,2026-01-30 17:00:42,2026-01-30 17:01:45,1min 3s,0s,,0.02 Km,16 kph,16 kph,
Detenido,2026-01-30 17:01:45,2026-01-30 17:02:15,30s,0s,,"-36.430743, -71.957935",
Movimiento,2026-01-30 17:02:15,2026-01-30 17:03:45,1min 30s,1min 0s,,0.44 Km,37 kph,30 kph,
Detenido,2026-01-30 17:03:45,2026-01-30 17:05:16,1min 31s,0s,,"-36.426901, -71.951475",
Movimiento,2026-01-30 17:05:16,2026-01-30 17:05:46,30s,30s,,0.03 Km,11 kph,11 kph,
Detenido,2026-01-30 17:05:46,2026-01-30 17:07:25,1min 39s,1min 39s,,"-36.425712, -71.950715",
Movimiento,2026-01-30 17:07:25,2026-01-30 17:08:47,1min 22s,0s,,0.07 Km,14 kph,14 kph,
Detenido,2026-01-30 17:08:47,2026-01-30 17:09:17,30s,0s,,"-36.425853, -71.949782",
Movimiento,2026-01-30 17:09:17,2026-01-30 17:15:50,6min 33s,0s,,2.13 Km,54 kph,24 kph,
Detenido,2026-01-30 17:15:50,2026-01-30 17:38:56,23min 6s,0s,,"-36.427795, -71.926837",
Movimiento,2026-01-30 17:38:56,2026-01-30 17:41:54,2min 58s,0s,,0.67 Km,63 kph,28 kph,
Detenido,2026-01-30 17:41:54,2026-01-30 17:42:24,30s,0s,,"-36.435413, -71.925551",
Movimiento,2026-01-30 17:42:24,2026-01-30 17:54:01,11min 37s,0s,,7.09 Km,78 kph,50 kph,
Detenido,2026-01-30 17:54:01,2026-01-30 18:15:46,21min 45s,0s,,"-36.45008, -71.837567",
Movimiento,2026-01-30 18:15:46,2026-01-30 18:34:21,18min 35s,1min 1s,,13.82 Km,100 kph,48 kph,
Detenido,2026-01-30 18:34:21,2026-01-31 09:08:18,14h 33min 57s,0s,,"-36.430188, -71.959592",
Movimiento,2026-01-31 09:08:18,2026-01-31 09:10:38,2min 20s,1min 10s,,0.61 Km,39 kph,27 kph,
Detenido,2026-01-31 09:10:38,2026-01-31 09:32:21,21min 43s,31s,,"-36.42688, -71.951476",
Movimiento,2026-01-31 09:32:21,2026-01-31 09:33:20,59s,0s,,0.33 Km,26 kph,26 kph,
Detenido,2026-01-31 09:33:20,2026-01-31 10:24:14,50min 54s,36s,,"-36.423129, -71.952424",
Movimiento,2026-01-31 10:24:14,2026-01-31 10:25:15,1min 1s,0s,,0.46 Km,23 kph,19 kph,
Detenido,2026-01-31 10:25:15,2026-01-31 10:50:32,25min 17s,0s,,"-36.422745, -71.952204",
Movimiento,2026-01-31 10:50:32,2026-01-31 10:51:00,28s,0s,,0.03 Km,24 kph,20 kph,
Detenido,2026-01-31 10:51:00,2026-01-31 11:12:45,21min 45s,0s,,"-36.421363, -71.952828",
Movimiento,2026-01-31 11:12:45,2026-01-31 11:13:09,24s,0s,,0.01 Km,10 kph,10 kph,
Detenido,2026-01-31 11:13:09,2026-01-31 11:15:41,2min 32s,0s,,"-36.418887, -71.952137",
Movimiento,2026-01-31 11:15:41,2026-01-31 11:19:42,4min 1s,0s,,1.49 Km,36 kph,19 kph,
Detenido,2026-01-31 11:19:42,2026-01-31 11:40:51,21min 9s,42s,,"-36.419637, -71.967551",
Movimiento,2026-01-31 11:40:51,2026-01-31 11:44:23,3min 32s,19s,,0.96 Km,37 kph,21 kph,
Detenido,2026-01-31 11:44:23,2026-01-31 12:02:46,18min 23s,4s,,"-36.426673, -71.965128",
Movimiento,2026-01-31 12:02:46,2026-01-31 12:06:01,3min 15s,0s,,1.09 Km,38 kph,20 kph,
Detenido,2026-01-31 12:06:01,2026-01-31 12:44:27,38min 26s,0s,,"-36.431973, -71.956403",
Movimiento,2026-01-31 12:44:27,2026-01-31 12:47:49,3min 22s,0s,,0.57 Km,34 kph,16 kph,
Detenido,2026-01-31 12:47:49,2026-01-31 16:13:25,3h 25min 36s,6s,,"-36.430151, -71.959624",
Movimiento,2026-01-31 16:13:25,2026-01-31 16:15:20,1min 55s,1min 1s,,0.22 Km,24 kph,14 kph,
Detenido,2026-01-31 16:15:20,2026-01-31 16:44:49,29min 29s,0s,,"-36.429271, -71.959522",
Movimiento,2026-01-31 16:44:49,2026-01-31 16:47:50,3min 1s,30s,,0.63 Km,33 kph,13 kph,
Detenido,2026-01-31 16:47:50,2026-01-31 16:49:21,1min 31s,1min 31s,,"-36.424175, -71.960309",
Movimiento,2026-01-31 16:49:21,2026-01-31 16:51:22,2min 1s,0s,,1.37 Km,73 kph,32 kph,
Detenido,2026-01-31 16:51:22,2026-01-31 17:01:47,10min 25s,0s,,"-36.416064, -71.949136",
Movimiento,2026-01-31 17:01:47,2026-01-31 17:08:31,6min 44s,0s,,3.09 Km,54 kph,33 kph,
Detenido,2026-01-31 17:08:31,2026-01-31 17:08:56,25s,0s,,"-36.427453, -71.978836",
Movimiento,2026-01-31 17:08:56,2026-01-31 17:09:31,35s,19s,,0.13 Km,17 kph,11 kph,
Detenido,2026-01-31 17:09:31,2026-01-31 17:10:32,1min 1s,1min 1s,,"-36.427782, -71.979421",
Movimiento,2026-01-31 17:10:32,2026-01-31 17:18:06,7min 34s,0s,,3.23 Km,52 kph,25 kph,
Detenido,2026-01-31 17:18:06,2026-01-31 17:23:29,5min 23s,0s,,"-36.428593, -71.960258",
Movimiento,2026-01-31 17:23:29,2026-01-31 17:24:51,1min 22s,0s,,0.17 Km,31 kph,18 kph,
Detenido,2026-01-31 17:24:51,2026-02-01 09:00:13,15h 35min 22s,30s,,"-36.43012, -71.959584",
Movimiento,2026-02-01 09:00:13,2026-02-01 09:01:13,1min 0s,17s,,0.61 Km,62 kph,42 kph,
Detenido,2026-02-01 09:01:13,2026-02-01 09:28:15,27min 2s,0s,,"-36.431149, -71.952922",
Movimiento,2026-02-01 09:28:15,2026-02-01 09:44:23,16min 8s,0s,,14.71 Km,98 kph,46 kph,
Detenido,2026-02-01 09:44:23,2026-02-01 10:07:32,23min 9s,0s,,"-36.409306, -71.824463",
Movimiento,2026-02-01 10:07:32,2026-02-01 10:16:36,9min 4s,0s,,6.98 Km,115 kph,42 kph,
Detenido,2026-02-01 10:16:36,2026-02-01 10:35:49,19min 13s,0s,,"-36.45009, -71.837437",
Movimiento,2026-02-01 10:35:49,2026-02-01 10:38:33,2min 44s,0s,,0.2 Km,26 kph,23 kph,
Detenido,2026-02-01 10:38:33,2026-02-01 10:41:04,2min 31s,0s,,"-36.448535, -71.847829",
Movimiento,2026-02-01 10:41:04,2026-02-01 10:51:09,10min 5s,0s,,9.35 Km,94 kph,55 kph,
Detenido,2026-02-01 10:51:09,2026-02-01 11:21:45,30min 36s,18s,,"-36.428544, -71.926539",
Movimiento,2026-02-01 11:21:45,2026-02-01 11:29:52,8min 7s,0s,,4.64 Km,83 kph,34 kph,
Detenido,2026-02-01 11:29:52,2026-02-01 11:39:25,9min 33s,0s,,"-36.413778, -71.960805",
Movimiento,2026-02-01 11:39:25,2026-02-01 11:40:16,51s,0s,,0.02 Km,9 kph,8 kph,
Detenido,2026-02-01 11:40:16,2026-02-01 12:04:40,24min 24s,30s,,"-36.413827, -71.960335",
Movimiento,2026-02-01 12:04:40,2026-02-01 12:07:31,2min 51s,30s,,0.51 Km,32 kph,18 kph,
Detenido,2026-02-01 12:07:31,2026-02-01 12:09:04,1min 33s,1min 33s,,"-36.417129, -71.954831",
Movimiento,2026-02-01 12:09:04,2026-02-01 12:11:03,1min 59s,0s,,0.89 Km,30 kph,23 kph,
Detenido,2026-02-01 12:11:03,2026-02-01 12:31:03,20min 0s,0s,,"-36.423169, -71.952296",
Movimiento,2026-02-01 12:31:03,2026-02-01 12:39:38,8min 35s,0s,,2.52 Km,59 kph,21 kph,
Detenido,2026-02-01 12:39:38,2026-02-01 12:51:23,11min 45s,0s,,"-36.419624, -71.967575",
Movimiento,2026-02-01 12:51:23,2026-02-01 12:59:45,8min 22s,0s,,3.27 Km,56 kph,22 kph,
Detenido,2026-02-01 12:59:45,2026-02-01 15:10:48,2h 11min 3s,5s,,"-36.430112, -71.959707",
Movimiento,2026-02-01 15:10:48,2026-02-01 15:15:15,4min 27s,1min 1s,,1.3 Km,34 kph,17 kph,
Detenido,2026-02-01 15:15:15,2026-02-01 15:15:24,9s,9s,,"-36.430788, -71.967259",
Movimiento,2026-02-01 15:15:24,2026-02-01 15:17:46,2min 22s,0s,,0.37 Km,41 kph,21 kph,
Detenido,2026-02-01 15:17:46,2026-02-01 15:25:25,7min 39s,31s,,"-36.431417, -71.968615",
Movimiento,2026-02-01 15:25:25,2026-02-01 15:28:26,3min 1s,0s,,1.02 Km,53 kph,26 kph,
Detenido,2026-02-01 15:28:26,2026-02-01 15:57:15,28min 49s,0s,,"-36.426797, -71.964985",
Movimiento,2026-02-01 15:57:15,2026-02-01 15:57:48,33s,0s,,0.66 Km,21 kph,15 kph,
Detenido,2026-02-01 15:57:48,2026-02-02 11:13:52,19h 16min 4s,0s,,"-36.43012, -71.95969",
Movimiento,2026-02-02 11:13:52,2026-02-02 11:15:27,1min 35s,30s,,0.42 Km,38 kph,17 kph,
Detenido,2026-02-02 11:15:27,2026-02-02 11:22:29,7min 2s,0s,,"-36.431241, -71.955099",
Movimiento,2026-02-02 11:22:29,2026-02-02 11:26:31,4min 2s,30s,,1.07 Km,36 kph,19 kph,
Detenido,2026-02-02 11:26:31,2026-02-02 11:28:02,1min 31s,1s,,"-36.434378, -71.961888",
Movimiento,2026-02-02 11:28:02,2026-02-02 11:29:02,1min 0s,30s,,0.27 Km,19 kph,16 kph,
Detenido,2026-02-02 11:29:02,2026-02-02 11:32:34,3min 32s,31s,,"-36.431387, -71.968646",
Movimiento,2026-02-02 11:32:34,2026-02-02 11:33:04,30s,0s,,0.07 Km,8 kph,7 kph,
Detenido,2026-02-02 11:33:04,2026-02-02 12:03:32,30min 28s,0s,,"-36.43183, -71.96882",
Movimiento,2026-02-02 12:03:32,2026-02-02 12:10:36,7min 4s,0s,,2.3 Km,55 kph,25 kph,
Detenido,2026-02-02 12:10:36,2026-02-02 12:13:37,3min 1s,0s,,"-36.425703, -71.950647",
Movimiento,2026-02-02 12:13:37,2026-02-02 12:14:37,1min 0s,0s,,0.53 Km,13 kph,13 kph,
Detenido,2026-02-02 12:14:37,2026-02-02 12:25:12,10min 35s,0s,,"-36.426914, -71.943396",
Movimiento,2026-02-02 12:25:12,2026-02-02 12:26:13,1min 1s,0s,,1.07 Km,74 kph,74 kph,
Detenido,2026-02-02 12:26:13,2026-02-02 12:27:44,1min 31s,0s,,"-36.428462, -71.927029",
Movimiento,2026-02-02 12:27:44,2026-02-02 12:28:14,30s,0s,,0.08 Km,9 kph,9 kph,
Detenido,2026-02-02 12:28:14,2026-02-02 12:47:49,19min 35s,0s,,"-36.427727, -71.926804",
Movimiento,2026-02-02 12:47:49,2026-02-02 13:03:03,15min 14s,0s,,15.1 Km,102 kph,65 kph,
Detenido,2026-02-02 13:03:03,2026-02-02 13:14:07,11min 4s,59s,,"-36.403552, -71.871897",
Movimiento,2026-02-02 13:14:07,2026-02-02 13:20:09,6min 2s,30s,,6.38 Km,87 kph,53 kph,
Detenido,2026-02-02 13:20:09,2026-02-02 13:41:40,21min 31s,0s,,"-36.409417, -71.824563",
Movimiento,2026-02-02 13:41:40,2026-02-02 13:52:51,11min 11s,0s,,7.07 Km,85 kph,39 kph,
Detenido,2026-02-02 13:52:51,2026-02-02 14:18:22,25min 31s,0s,,"-36.450112, -71.837488",
Movimiento,2026-02-02 14:18:22,2026-02-02 14:31:58,13min 36s,0s,,11.94 Km,111 kph,57 kph,
Detenido,2026-02-02 14:31:58,2026-02-02 14:33:25,1min 27s,26s,,"-36.426177, -71.948174",
Movimiento,2026-02-02 14:33:25,2026-02-02 14:34:49,1min 24s,1min 24s,,0.17 Km,49 kph,49 kph,
Detenido,2026-02-02 14:34:49,2026-02-02 14:35:00,11s,11s,,"-36.430449, -71.952623",
Movimiento,2026-02-02 14:35:00,2026-02-02 14:36:30,1min 30s,0s,,0.31 Km,32 kph,24 kph,
Detenido,2026-02-02 14:36:30,2026-02-02 14:46:17,9min 47s,0s,,"-36.430562, -71.956048",
Movimiento,2026-02-02 14:46:17,2026-02-02 14:48:47,2min 30s,11s,,0.45 Km,45 kph,32 kph,
Detenido,2026-02-02 14:48:47,2026-02-03 06:17:35,15h 28min 48s,0s,,"-36.430162, -71.959863",
Movimiento,2026-02-03 06:17:35,2026-02-03 06:21:18,3min 43s,0s,,0.01 Km,8 kph,8 kph,
Detenido,2026-02-03 06:21:18,2026-02-03 08:28:23,2h 7min 5s,0s,,"-36.430062, -71.959601",
Movimiento,2026-02-03 08:28:23,2026-02-03 08:32:26,4min 3s,0s,,1.36 Km,44 kph,21 kph,
Detenido,2026-02-03 08:32:26,2026-02-03 08:33:19,53s,0s,,"-36.425976, -71.949322",
Movimiento,2026-02-03 08:33:19,2026-02-03 08:44:33,11min 14s,0s,,11.05 Km,88 kph,63 kph,
Detenido,2026-02-03 08:44:33,2026-02-03 09:00:41,16min 8s,0s,,"-36.405193, -71.868458",
Movimiento,2026-02-03 09:00:41,2026-02-03 09:25:56,25min 15s,0s,,22.93 Km,111 kph,49 kph,
Detenido,2026-02-03 09:25:56,2026-02-03 09:47:25,21min 29s,0s,,"-36.47511, -72.05126",
Movimiento,2026-02-03 09:47:25,2026-02-03 10:03:17,15min 52s,0s,,13.29 Km,111 kph,43 kph,
Detenido,2026-02-03 10:03:17,2026-02-03 10:04:18,1min 1s,0s,,"-36.431382, -71.968655",
Movimiento,2026-02-03 10:04:18,2026-02-03 10:04:48,30s,0s,,0.03 Km,10 kph,10 kph,
Detenido,2026-02-03 10:04:48,2026-02-03 10:34:03,29min 15s,0s,,"-36.431835, -71.968787",
Movimiento,2026-02-03 10:34:03,2026-02-03 10:37:05,3min 2s,0s,,0.54 Km,30 kph,20 kph,
Detenido,2026-02-03 10:37:05,2026-02-03 10:54:13,17min 8s,0s,,"-36.426725, -71.965052",
Movimiento,2026-02-03 10:54:13,2026-02-03 10:56:45,2min 32s,0s,,0.64 Km,45 kph,29 kph,
Detenido,2026-02-03 10:56:45,2026-02-03 11:28:55,32min 10s,0s,,"-36.431991, -71.956388",
Movimiento,2026-02-03 11:28:55,2026-02-03 11:30:33,1min 38s,30s,,0.66 Km,47 kph,25 kph,
Detenido,2026-02-03 11:30:33,2026-02-03 11:54:15,23min 42s,0s,,"-36.426883, -71.951481",
Movimiento,2026-02-03 11:54:15,2026-02-03 11:56:16,2min 1s,0s,,0.47 Km,38 kph,23 kph,
Detenido,2026-02-03 11:56:16,2026-02-03 12:22:00,25min 44s,0s,,"-36.422716, -71.952274",
Movimiento,2026-02-03 12:22:00,2026-02-03 12:27:02,5min 2s,0s,,1.37 Km,36 kph,21 kph,
Detenido,2026-02-03 12:27:02,2026-02-03 12:29:03,2min 1s,0s,,"-36.427311, -71.957989",
Movimiento,2026-02-03 12:29:03,2026-02-03 12:33:04,4min 1s,1min 0s,,1.09 Km,34 kph,21 kph,
Detenido,2026-02-03 12:33:04,2026-02-03 12:57:06,24min 2s,0s,,"-36.423168, -71.952343",
Movimiento,2026-02-03 12:57:06,2026-02-03 13:02:47,5min 41s,0s,,1.51 Km,35 kph,19 kph,
Detenido,2026-02-03 13:02:47,2026-02-03 15:06:24,2h 3min 37s,0s,,"-36.430085, -71.959654",
Movimiento,2026-02-03 15:06:24,2026-02-03 15:13:16,6min 52s,30s,,1.92 Km,31 kph,16 kph,
Detenido,2026-02-03 15:13:16,2026-02-03 15:37:09,23min 53s,0s,,"-36.419827, -71.967556",
Movimiento,2026-02-03 15:37:09,2026-02-03 15:42:57,5min 48s,0s,,1.69 Km,42 kph,27 kph,
Detenido,2026-02-03 15:42:57,2026-02-04 08:29:16,16h 46min 19s,0s,,"-36.430173, -71.959652",
Movimiento,2026-02-04 08:29:16,2026-02-04 08:47:39,18min 23s,0s,,13.14 Km,87 kph,44 kph,
Detenido,2026-02-04 08:47:39,2026-02-04 08:49:28,1min 49s,0s,,"-36.439819, -71.821854",
Movimiento,2026-02-04 08:49:28,2026-02-04 08:50:40,1min 12s,0s,,0.01 Km,6 kph,6 kph,
Detenido,2026-02-04 08:50:40,2026-02-04 09:46:44,56min 4s,0s,,"-36.439881, -71.821869",
Movimiento,2026-02-04 09:46:44,2026-02-04 10:08:55,22min 11s,0s,,23.4 Km,112 kph,57 kph,
Detenido,2026-02-04 10:08:55,2026-02-04 10:29:09,20min 14s,0s,,"-36.475192, -72.051355",
Movimiento,2026-02-04 10:29:09,2026-02-04 10:44:19,15min 10s,0s,,13.16 Km,88 kph,45 kph,
Detenido,2026-02-04 10:44:19,2026-02-04 11:13:26,29min 7s,0s,,"-36.432, -71.956375",
Movimiento,2026-02-04 11:13:26,2026-02-04 11:16:07,2min 41s,0s,,0.96 Km,36 kph,23 kph,
Detenido,2026-02-04 11:16:07,2026-02-04 11:35:19,19min 12s,0s,,"-36.426085, -71.951202",
Movimiento,2026-02-04 11:35:19,2026-02-04 11:36:50,1min 31s,0s,,0.54 Km,36 kph,22 kph,
Detenido,2026-02-04 11:36:50,2026-02-04 12:11:25,34min 35s,0s,,"-36.423116, -71.952475",
Movimiento,2026-02-04 12:11:25,2026-02-04 12:13:40,2min 15s,0s,,0.16 Km,33 kph,14 kph,
Detenido,2026-02-04 12:13:40,2026-02-04 12:44:58,31min 18s,30s,,"-36.422736, -71.952154",
Movimiento,2026-02-04 12:44:58,2026-02-04 12:51:32,6min 34s,0s,,0.98 Km,31 kph,16 kph,
Detenido,2026-02-04 12:51:32,2026-02-04 14:55:48,2h 4min 16s,18s,,"-36.430106, -71.959656",
Movimiento,2026-02-04 14:55:48,2026-02-04 15:04:35,8min 47s,0s,,1.78 Km,28 kph,15 kph,
Detenido,2026-02-04 15:04:35,2026-02-04 15:33:47,29min 12s,0s,,"-36.419784, -71.96771",
Movimiento,2026-02-04 15:33:47,2026-02-04 15:37:18,3min 31s,0s,,1 Km,19 kph,14 kph,
Detenido,2026-02-04 15:37:18,2026-02-04 16:07:36,30min 18s,1min 0s,,"-36.426689, -71.965162",
Movimiento,2026-02-04 16:07:36,2026-02-04 16:09:37,2min 1s,0s,,0.52 Km,26 kph,17 kph,
Detenido,2026-02-04 16:09:37,2026-02-04 16:14:12,4min 35s,0s,,"-36.428592, -71.960274",
Movimiento,2026-02-04 16:14:12,2026-02-04 16:16:47,2min 35s,0s,,0.16 Km,18 kph,11 kph,
Detenido,2026-02-04 16:16:47,2026-02-04 16:39:05,22min 18s,30s,,"-36.430145, -71.959642",
Movimiento,2026-02-04 16:39:05,2026-02-04 16:44:26,5min 21s,0s,,0.26 Km,36 kph,16 kph,
Detenido,2026-02-04 16:44:26,2026-02-04 17:06:21,21min 55s,33s,,"-36.42935, -71.959608",
Movimiento,2026-02-04 17:06:21,2026-02-04 17:08:49,2min 28s,0s,,0.28 Km,14 kph,11 kph,
Detenido,2026-02-04 17:08:49,2026-02-05 08:28:53,15h 20min 4s,0s,,"-36.430162, -71.959582",
Movimiento,2026-02-05 08:28:53,2026-02-05 08:40:22,11min 29s,23s,,11.62 Km,110 kph,63 kph,
Detenido,2026-02-05 08:40:22,2026-02-05 08:55:45,15min 23s,0s,,"-36.475117, -72.051336",
Movimiento,2026-02-05 08:55:45,2026-02-05 09:11:51,16min 6s,0s,,12.78 Km,110 kph,47 kph,
Detenido,2026-02-05 09:11:51,2026-02-05 09:16:24,4min 33s,39s,,"-36.430149, -71.959574",
Movimiento,2026-02-05 09:16:24,2026-02-05 09:30:33,14min 9s,40s,,13.07 Km,79 kph,51 kph,
Detenido,2026-02-05 09:30:33,2026-02-05 09:40:15,9min 42s,0s,,"-36.439858, -71.821114",
Movimiento,2026-02-05 09:40:15,2026-02-05 09:45:48,5min 33s,0s,,4.38 Km,77 kph,61 kph,
Detenido,2026-02-05 09:45:48,2026-02-05 10:04:47,18min 59s,0s,,"-36.409416, -71.824548",
Movimiento,2026-02-05 10:04:47,2026-02-05 10:11:20,6min 33s,0s,,5.65 Km,72 kph,48 kph,
Detenido,2026-02-05 10:11:20,2026-02-05 10:31:22,20min 2s,0s,,"-36.405181, -71.868443",
Movimiento,2026-02-05 10:31:22,2026-02-05 10:35:55,4min 33s,0s,,1.9 Km,82 kph,41 kph,
Detenido,2026-02-05 10:35:55,2026-02-05 10:45:44,9min 49s,0s,,"-36.403538, -71.871818",
Movimiento,2026-02-05 10:45:44,2026-02-05 10:52:16,6min 32s,1min 4s,,5.35 Km,99 kph,58 kph,
Detenido,2026-02-05 10:52:16,2026-02-05 10:52:27,11s,11s,,"-36.438145, -71.830568",
Movimiento,2026-02-05 10:52:27,2026-02-05 11:02:21,9min 54s,0s,,3.81 Km,96 kph,43 kph,
Detenido,2026-02-05 11:02:21,2026-02-05 11:04:58,2min 37s,0s,,"-36.450103, -71.837489",
Movimiento,2026-02-05 11:04:58,2026-02-05 11:05:29,31s,0s,,0.02 Km,10 kph,10 kph,
Detenido,2026-02-05 11:05:29,2026-02-05 11:22:15,16min 46s,0s,,"-36.450089, -71.837446",
Movimiento,2026-02-05 11:22:15,2026-02-05 11:35:48,13min 33s,30s,,11.67 Km,85 kph,53 kph,
Detenido,2026-02-05 11:35:48,2026-02-05 11:38:19,2min 31s,25s,,"-36.426848, -71.943352",
Movimiento,2026-02-05 11:38:19,2026-02-05 11:42:21,4min 2s,0s,,1.15 Km,50 kph,24 kph,
Detenido,2026-02-05 11:42:21,2026-02-05 11:42:51,30s,0s,,"-36.426841, -71.957696",
Movimiento,2026-02-05 11:42:51,2026-02-05 11:45:22,2min 31s,30s,,0.72 Km,44 kph,25 kph,
Detenido,2026-02-05 11:45:22,2026-02-05 11:55:48,10min 26s,0s,,"-36.426728, -71.964954",
Movimiento,2026-02-05 11:55:48,2026-02-05 11:57:54,2min 6s,0s,,0.59 Km,27 kph,20 kph,
Detenido,2026-02-05 11:57:54,2026-02-05 15:39:34,3h 41min 40s,0s,,"-36.430066, -71.959698",
Movimiento,2026-02-05 15:39:34,2026-02-05 15:40:30,56s,14s,,0.34 Km,40 kph,24 kph,
Detenido,2026-02-05 15:40:30,2026-02-05 15:58:29,17min 59s,0s,,"-36.43213, -71.957302",
Movimiento,2026-02-05 15:58:29,2026-02-05 16:00:30,2min 1s,0s,,0.38 Km,13 kph,9 kph,
Detenido,2026-02-05 16:00:30,2026-02-05 16:02:01,1min 31s,0s,,"-36.429351, -71.958238",
Movimiento,2026-02-05 16:02:01,2026-02-05 16:02:31,30s,0s,,0.19 Km,17 kph,12 kph,
Detenido,2026-02-05 16:02:31,2026-02-05 16:09:07,6min 36s,0s,,"-36.4301, -71.959616",
Movimiento,2026-02-05 16:09:07,2026-02-05 16:11:08,2min 1s,30s,,0.36 Km,17 kph,10 kph,
Detenido,2026-02-05 16:11:08,2026-02-05 16:13:10,2min 2s,2min 2s,,"-36.427632, -71.958258",
Movimiento,2026-02-05 16:13:10,2026-02-05 16:14:10,1min 0s,0s,,0.27 Km,26 kph,19 kph,
Detenido,2026-02-05 16:14:10,2026-02-05 16:15:11,1min 1s,0s,,"-36.423883, -71.95984",
Movimiento,2026-02-05 16:15:11,2026-02-05 16:15:41,30s,30s,,0.29 Km,11 kph,11 kph,
Detenido,2026-02-05 16:15:41,2026-02-05 16:46:58,31min 17s,0s,,"-36.425649, -71.962364",
Movimiento,2026-02-05 16:46:58,2026-02-05 16:50:50,3min 52s,0s,,1.29 Km,47 kph,19 kph,
Detenido,2026-02-05 16:50:50,2026-02-05 17:11:51,21min 1s,0s,,"-36.431869, -71.96879",
Movimiento,2026-02-05 17:11:51,2026-02-05 17:15:54,4min 3s,0s,,1.1 Km,34 kph,20 kph,
Detenido,2026-02-05 17:15:54,2026-02-06 09:50:34,16h 34min 40s,4s,,"-36.430112, -71.959651",
Movimiento,2026-02-06 09:50:34,2026-02-06 09:50:58,24s,0s,,0 Km,8 kph,8 kph,
Detenido,2026-02-06 09:50:58,2026-02-06 11:01:47,1h 10min 49s,0s,,"-36.430084, -71.959627",
Movimiento,2026-02-06 11:01:47,2026-02-06 11:04:49,3min 2s,30s,,1.02 Km,38 kph,20 kph,
Detenido,2026-02-06 11:04:49,2026-02-06 11:06:25,1min 36s,0s,,"-36.426847, -71.951503",
Movimiento,2026-02-06 11:06:25,2026-02-06 11:07:20,55s,0s,,0.29 Km,29 kph,29 kph,
Detenido,2026-02-06 11:07:20,2026-02-06 11:28:27,21min 7s,48s,,"-36.423152, -71.952488",
Movimiento,2026-02-06 11:28:27,2026-02-06 11:28:57,30s,30s,,0.03 Km,11 kph,11 kph,
Detenido,2026-02-06 11:28:57,2026-02-06 11:30:33,1min 36s,1min 36s,,"-36.425228, -71.952498",
Movimiento,2026-02-06 11:30:33,2026-02-06 11:31:33,1min 0s,30s,,0.65 Km,35 kph,26 kph,
Detenido,2026-02-06 11:31:33,2026-02-06 11:33:34,2min 1s,0s,,"-36.429185, -71.959093",
Movimiento,2026-02-06 11:33:34,2026-02-06 11:37:35,4min 1s,0s,,1.04 Km,32 kph,17 kph,
Detenido,2026-02-06 11:37:35,2026-02-06 12:06:30,28min 55s,0s,,"-36.431859, -71.968791",
Movimiento,2026-02-06 12:06:30,2026-02-06 12:12:08,5min 38s,1min 30s,,1.33 Km,49 kph,19 kph,
Detenido,2026-02-06 12:12:08,2026-02-06 12:12:38,30s,30s,,"-36.417773, -71.963677",
Movimiento,2026-02-06 12:12:38,2026-02-06 12:21:12,8min 34s,0s,,5.51 Km,64 kph,49 kph,
Detenido,2026-02-06 12:21:12,2026-02-06 13:29:12,1h 8min 0s,0s,,"-36.365086, -71.966608",
Movimiento,2026-02-06 13:29:12,2026-02-06 13:40:48,11min 36s,0s,,7.54 Km,70 kph,41 kph,
Detenido,2026-02-06 13:40:48,2026-02-06 14:33:44,52min 56s,0s,,"-36.430268, -71.959976",
Movimiento,2026-02-06 14:33:44,2026-02-06 14:40:47,7min 3s,0s,,1.57 Km,39 kph,19 kph,
Detenido,2026-02-06 14:40:47,2026-02-06 14:44:49,4min 2s,1min 5s,,"-36.416875, -71.964215",
Movimiento,2026-02-06 14:44:49,2026-02-06 15:01:57,17min 8s,0s,,17.36 Km,107 kph,62 kph,
Detenido,2026-02-06 15:01:57,2026-02-06 15:03:37,1min 40s,0s,,"-36.336483, -72.066817",
Movimiento,2026-02-06 15:03:37,2026-02-06 15:09:00,5min 23s,0s,,0.54 Km,17 kph,13 kph,
Detenido,2026-02-06 15:09:00,2026-02-06 15:58:28,49min 28s,54s,,"-36.340974, -72.06972",
Movimiento,2026-02-06 15:58:28,2026-02-06 15:59:05,37s,0s,,0.09 Km,12 kph,12 kph,
Detenido,2026-02-06 15:59:05,2026-02-06 16:00:35,1min 30s,0s,,"-36.340795, -72.068647",
Movimiento,2026-02-06 16:00:35,2026-02-06 16:01:36,1min 1s,0s,,0.12 Km,11 kph,11 kph,
Detenido,2026-02-06 16:01:36,2026-02-06 16:03:05,1min 29s,0s,,"-36.338425, -72.067854",
Movimiento,2026-02-06 16:03:05,2026-02-06 16:29:20,26min 15s,0s,,19.57 Km,91 kph,46 kph,
Detenido,2026-02-06 16:29:20,2026-02-06 16:36:06,6min 46s,0s,,"-36.428394, -71.960089",
Movimiento,2026-02-06 16:36:06,2026-02-06 16:36:52,46s,0s,,0.02 Km,8 kph,8 kph,
Detenido,2026-02-06 16:36:52,2026-02-06 16:44:56,8min 4s,0s,,"-36.428603, -71.960378",
Movimiento,2026-02-06 16:44:56,2026-02-06 16:46:34,1min 38s,0s,,0.18 Km,14 kph,14 kph,
Detenido,2026-02-06 16:46:34,2026-02-06 17:50:33,1h 3min 59s,33s,,"-36.430119, -71.959672",
Movimiento,2026-02-06 17:50:33,2026-02-06 17:53:34,3min 1s,0s,,1.7 Km,70 kph,51 kph,
Detenido,2026-02-06 17:53:34,2026-02-06 17:56:06,2min 32s,1min 31s,,"-36.434594, -71.962035",
Movimiento,2026-02-06 17:56:06,2026-02-06 17:57:37,1min 31s,0s,,0.66 Km,41 kph,26 kph,
Detenido,2026-02-06 17:57:37,2026-02-07 09:17:35,15h 19min 58s,0s,,"-36.430171, -71.959645",
Movimiento,2026-02-07 09:17:35,2026-02-07 09:32:13,14min 38s,0s,,13.13 Km,86 kph,48 kph,
Detenido,2026-02-07 09:32:13,2026-02-07 09:43:47,11min 34s,0s,,"-36.439914, -71.821869",
Movimiento,2026-02-07 09:43:47,2026-02-07 09:54:24,10min 37s,0s,,10.22 Km,82 kph,61 kph,
Detenido,2026-02-07 09:54:24,2026-02-07 09:58:27,4min 3s,0s,,"-36.42797, -71.935652",
Movimiento,2026-02-07 09:58:27,2026-02-07 09:59:58,1min 31s,0s,,0.73 Km,83 kph,26 kph,
Detenido,2026-02-07 09:59:58,2026-02-07 10:12:05,12min 7s,0s,,"-36.426831, -71.942737",
Movimiento,2026-02-07 10:12:05,2026-02-07 10:12:36,31s,0s,,0.06 Km,18 kph,15 kph,
Detenido,2026-02-07 10:12:36,2026-02-07 10:30:14,17min 38s,0s,,"-36.428015, -71.9361",
Movimiento,2026-02-07 10:30:14,2026-02-07 10:31:44,1min 30s,0s,,0.61 Km,30 kph,14 kph,
Detenido,2026-02-07 10:31:44,2026-02-07 10:53:46,22min 2s,0s,,"-36.426795, -71.942975",
Movimiento,2026-02-07 10:53:46,2026-02-07 11:04:33,10min 47s,8s,,12.14 Km,96 kph,58 kph,
Detenido,2026-02-07 11:04:33,2026-02-07 11:19:56,15min 23s,0s,,"-36.475195, -72.051357",
Movimiento,2026-02-07 11:19:56,2026-02-07 11:37:28,17min 32s,0s,,15.67 Km,89 kph,44 kph,
Detenido,2026-02-07 11:37:28,2026-02-07 12:11:50,34min 22s,0s,,"-36.53175, -72.083278",
Movimiento,2026-02-07 12:11:50,2026-02-07 12:29:24,17min 34s,0s,,16.94 Km,104 kph,57 kph,
Detenido,2026-02-07 12:29:24,2026-02-07 12:52:27,23min 3s,0s,,"-36.431975, -71.956399",
Movimiento,2026-02-07 12:52:27,2026-02-07 12:54:28,2min 1s,0s,,0.49 Km,38 kph,24 kph,
Detenido,2026-02-07 12:54:28,2026-02-07 12:59:30,5min 2s,2min 1s,,"-36.430053, -71.952575",
Movimiento,2026-02-07 12:59:30,2026-02-07 13:01:31,2min 1s,0s,,0.29 Km,28 kph,18 kph,
Detenido,2026-02-07 13:01:31,2026-02-07 13:25:33,24min 2s,0s,,"-36.430204, -71.953767",
Movimiento,2026-02-07 13:25:33,2026-02-07 13:29:05,3min 32s,1min 1s,,0.82 Km,35 kph,23 kph,
Detenido,2026-02-07 13:29:05,2026-02-07 13:48:59,19min 54s,0s,,"-36.427877, -71.965409",
Movimiento,2026-02-07 13:48:59,2026-02-07 13:51:47,2min 48s,0s,,1.39 Km,41 kph,29 kph,
Detenido,2026-02-07 13:51:47,2026-02-07 14:31:03,39min 16s,0s,,"-36.421485, -71.956094",
Movimiento,2026-02-07 14:31:03,2026-02-07 14:32:04,1min 1s,30s,,0.37 Km,28 kph,25 kph,
Detenido,2026-02-07 14:32:04,2026-02-07 14:33:21,1min 17s,1min 17s,,"-36.417851, -71.957837",
Movimiento,2026-02-07 14:33:21,2026-02-07 14:36:36,3min 15s,0s,,0.91 Km,38 kph,25 kph,
Detenido,2026-02-07 14:36:36,2026-02-07 15:02:38,26min 2s,0s,,"-36.419641, -71.96754",
Movimiento,2026-02-07 15:02:38,2026-02-07 15:05:39,3min 1s,32s,,0.75 Km,34 kph,24 kph,
Detenido,2026-02-07 15:05:39,2026-02-07 15:30:40,25min 1s,31s,,"-36.425608, -71.970742",
Movimiento,2026-02-07 15:30:40,2026-02-07 15:36:43,6min 3s,0s,,1.92 Km,38 kph,24 kph,
Detenido,2026-02-07 15:36:43,2026-02-07 17:25:07,1h 48min 24s,0s,,"-36.430148, -71.959617",
Movimiento,2026-02-07 17:25:07,2026-02-07 17:28:58,3min 51s,36s,,1.18 Km,37 kph,20 kph,
Detenido,2026-02-07 17:28:58,2026-02-07 17:38:45,9min 47s,0s,,"-36.43016, -71.959604",
Movimiento,2026-02-07 17:38:45,2026-02-07 17:42:33,3min 48s,0s,,0.94 Km,55 kph,27 kph,
Detenido,2026-02-07 17:42:33,2026-02-07 17:43:05,32s,0s,,"-36.426769, -71.951764",
Movimiento,2026-02-07 17:43:05,2026-02-07 17:47:05,4min 0s,0s,,1.24 Km,48 kph,30 kph,
Detenido,2026-02-07 17:47:05,2026-02-07 18:01:11,14min 6s,0s,,"-36.416145, -71.949158",
Movimiento,2026-02-07 18:01:11,2026-02-07 18:04:43,3min 32s,0s,,1.61 Km,40 kph,30 kph,
Detenido,2026-02-07 18:04:43,2026-02-07 18:05:45,1min 2s,0s,,"-36.426735, -71.958097",
Movimiento,2026-02-07 18:05:45,2026-02-07 18:13:24,7min 39s,0s,,0.46 Km,33 kph,30 kph,
Detenido,2026-02-07 18:13:24,2026-02-08 08:06:04,13h 52min 40s,0s,,"-36.430117, -71.959631",
Movimiento,2026-02-08 08:06:04,2026-02-08 08:18:06,12min 2s,0s,,11.75 Km,107 kph,57 kph,
Detenido,2026-02-08 08:18:06,2026-02-08 08:35:07,17min 1s,0s,,"-36.475176, -72.051342",
Movimiento,2026-02-08 08:35:07,2026-02-08 08:47:12,12min 5s,0s,,11.94 Km,110 kph,66 kph,
Detenido,2026-02-08 08:47:12,2026-02-08 09:01:48,14min 36s,0s,,"-36.531718, -72.083249",
Movimiento,2026-02-08 09:01:48,2026-02-08 09:35:05,33min 17s,0s,,30.87 Km,109 kph,52 kph,
Detenido,2026-02-08 09:35:05,2026-02-08 09:35:35,30s,0s,,"-36.450006, -71.838882",
Movimiento,2026-02-08 09:35:35,2026-02-08 09:41:39,6min 4s,0s,,0.95 Km,52 kph,20 kph,
Detenido,2026-02-08 09:41:39,2026-02-08 10:02:42,21min 3s,0s,,"-36.450761, -71.837396",
Movimiento,2026-02-08 10:02:42,2026-02-08 10:03:43,1min 1s,0s,,0.16 Km,12 kph,12 kph,
Detenido,2026-02-08 10:03:43,2026-02-08 10:06:14,2min 31s,0s,,"-36.449575, -71.838644",
Movimiento,2026-02-08 10:06:14,2026-02-08 10:17:53,11min 39s,1min 27s,,7.99 Km,89 kph,56 kph,
Detenido,2026-02-08 10:17:53,2026-02-08 10:29:00,11min 7s,0s,,"-36.405224, -71.868544",
Movimiento,2026-02-08 10:29:00,2026-02-08 10:40:07,11min 7s,0s,,9.95 Km,79 kph,51 kph,
Detenido,2026-02-08 10:40:07,2026-02-08 11:09:01,28min 54s,0s,,"-36.428042, -71.936068",
Movimiento,2026-02-08 11:09:01,2026-02-08 11:10:38,1min 37s,0s,,0.84 Km,63 kph,48 kph,
Detenido,2026-02-08 11:10:38,2026-02-08 11:12:08,1min 30s,0s,,"-36.426081, -71.948309",
Movimiento,2026-02-08 11:12:08,2026-02-08 11:14:40,2min 32s,0s,,0.31 Km,37 kph,31 kph,
Detenido,2026-02-08 11:14:40,2026-02-08 11:34:49,20min 9s,0s,,"-36.422745, -71.952286",
Movimiento,2026-02-08 11:34:49,2026-02-08 11:35:50,1min 1s,0s,,0.07 Km,33 kph,33 kph,
Detenido,2026-02-08 11:35:50,2026-02-08 11:43:23,7min 33s,0s,,"-36.424267, -71.952265",
Movimiento,2026-02-08 11:43:23,2026-02-08 11:44:24,1min 1s,0s,,0.45 Km,36 kph,36 kph,
Detenido,2026-02-08 11:44:24,2026-02-08 11:59:01,14min 37s,0s,,"-36.429304, -71.95397",
Movimiento,2026-02-08 11:59:01,2026-02-08 12:00:01,1min 0s,0s,,0.37 Km,29 kph,28 kph,
Detenido,2026-02-08 12:00:01,2026-02-08 12:20:41,20min 40s,0s,,"-36.430186, -71.953575",
Movimiento,2026-02-08 12:20:41,2026-02-08 12:22:12,1min 31s,1min 1s,,0.51 Km,25 kph,16 kph,
Detenido,2026-02-08 12:22:12,2026-02-08 12:23:12,1min 0s,1min 0s,,"-36.428681, -71.96164",
Movimiento,2026-02-08 12:23:12,2026-02-08 12:24:13,1min 1s,0s,,0.34 Km,12 kph,12 kph,
Detenido,2026-02-08 12:24:13,2026-02-08 12:47:24,23min 11s,0s,,"-36.42789, -71.965384",
Movimiento,2026-02-08 12:47:24,2026-02-08 12:51:57,4min 33s,0s,,1.52 Km,54 kph,33 kph,
Detenido,2026-02-08 12:51:57,2026-02-08 13:16:43,24min 46s,0s,,"-36.42559, -71.970885",
Movimiento,2026-02-08 13:16:43,2026-02-08 13:22:10,5min 27s,30s,,1.93 Km,42 kph,23 kph,
Detenido,2026-02-08 13:22:10,2026-02-08 17:16:55,3h 54min 45s,0s,,"-36.430185, -71.95962",
Movimiento,2026-02-08 17:16:55,2026-02-08 17:18:09,1min 14s,0s,,0.21 Km,15 kph,13 kph,
Detenido,2026-02-08 17:18:09,2026-02-08 17:57:05,38min 56s,27s,,"-36.429336, -71.9595",
Movimiento,2026-02-08 17:57:05,2026-02-08 17:58:05,1min 0s,15s,,0.41 Km,40 kph,28 kph,
Detenido,2026-02-08 17:58:05,2026-02-08 18:03:49,5min 44s,0s,,"-36.428604, -71.960293",
Movimiento,2026-02-08 18:03:49,2026-02-08 18:05:01,1min 12s,0s,,0.19 Km,18 kph,15 kph,
Detenido,2026-02-08 18:05:01,2026-02-09 08:24:55,14h 19min 54s,0s,,"-36.430156, -71.959646",
Movimiento,2026-02-09 08:24:55,2026-02-09 08:27:32,2min 37s,0s,,1.14 Km,42 kph,24 kph,
Detenido,2026-02-09 08:27:32,2026-02-09 08:31:04,3min 32s,30s,,"-36.425804, -71.950066",
Movimiento,2026-02-09 08:31:04,2026-02-09 08:55:17,24min 13s,0s,,25.66 Km,91 kph,58 kph,
Detenido,2026-02-09 08:55:17,2026-02-09 09:34:42,39min 25s,0s,,"-36.397403, -71.7619",
Movimiento,2026-02-09 09:34:42,2026-02-09 09:48:49,14min 7s,0s,,13.75 Km,110 kph,64 kph,
Detenido,2026-02-09 09:48:49,2026-02-09 09:49:19,30s,0s,,"-36.439844, -71.822102",
Movimiento,2026-02-09 09:49:19,2026-02-09 09:50:35,1min 16s,15s,,0.13 Km,16 kph,9 kph,
Detenido,2026-02-09 09:50:35,2026-02-09 10:17:04,26min 29s,0s,,"-36.439916, -71.821838",
Movimiento,2026-02-09 10:17:04,2026-02-09 10:23:08,6min 4s,0s,,3.23 Km,48 kph,34 kph,
Detenido,2026-02-09 10:23:08,2026-02-09 10:56:21,33min 13s,0s,,"-36.450864, -71.837392",
Movimiento,2026-02-09 10:56:21,2026-02-09 11:13:29,17min 8s,0s,,11.29 Km,75 kph,44 kph,
Detenido,2026-02-09 11:13:29,2026-02-09 11:46:48,33min 19s,0s,,"-36.427952, -71.936034",
Movimiento,2026-02-09 11:46:48,2026-02-09 11:48:14,1min 26s,0s,,0.62 Km,49 kph,32 kph,
Detenido,2026-02-09 11:48:14,2026-02-09 12:05:21,17min 7s,0s,,"-36.426847, -71.943353",
Movimiento,2026-02-09 12:05:21,2026-02-09 12:05:51,30s,0s,,0.17 Km,41 kph,41 kph,
Detenido,2026-02-09 12:05:51,2026-02-09 12:08:22,2min 31s,0s,,"-36.426673, -71.945689",
Movimiento,2026-02-09 12:08:22,2026-02-09 12:08:53,31s,31s,,0.04 Km,11 kph,11 kph,
Detenido,2026-02-09 12:08:53,2026-02-09 12:12:24,3min 31s,0s,,"-36.426321, -71.947498",
Movimiento,2026-02-09 12:12:24,2026-02-09 12:14:56,2min 32s,0s,,0.59 Km,35 kph,25 kph,
Detenido,2026-02-09 12:14:56,2026-02-09 12:22:25,7min 29s,0s,,"-36.422735, -71.952449",
Movimiento,2026-02-09 12:22:25,2026-02-09 12:24:31,2min 6s,0s,,0.27 Km,30 kph,17 kph,
Detenido,2026-02-09 12:24:31,2026-02-09 12:44:46,20min 15s,0s,,"-36.424222, -71.952221",
Movimiento,2026-02-09 12:44:46,2026-02-09 12:46:13,1min 27s,0s,,0.64 Km,41 kph,41 kph,
Detenido,2026-02-09 12:46:13,2026-02-09 12:46:44,31s,0s,,"-36.429, -71.959913",
Movimiento,2026-02-09 12:46:44,2026-02-09 12:48:14,1min 30s,0s,,0.18 Km,27 kph,21 kph,
Detenido,2026-02-09 12:48:14,2026-02-09 14:21:50,1h 33min 36s,0s,,"-36.430095, -71.959623",
Movimiento,2026-02-09 14:21:50,2026-02-09 14:30:54,9min 4s,0s,,2.48 Km,39 kph,19 kph,
Detenido,2026-02-09 14:30:54,2026-02-09 14:37:57,7min 3s,0s,,"-36.419654, -71.967531",
Movimiento,2026-02-09 14:37:57,2026-02-09 14:43:30,5min 33s,0s,,1.73 Km,31 kph,18 kph,
Detenido,2026-02-09 14:43:30,2026-02-10 09:43:48,19h 18s,3s,,"-36.430167, -71.959638",
Movimiento,2026-02-10 09:43:48,2026-02-10 09:48:25,4min 37s,0s,,1.08 Km,33 kph,14 kph,
Detenido,2026-02-10 09:48:25,2026-02-10 09:52:58,4min 33s,0s,,"-36.423027, -71.964179",
Movimiento,2026-02-10 09:52:58,2026-02-10 09:53:58,1min 0s,0s,,0.51 Km,47 kph,35 kph,
Detenido,2026-02-10 09:53:58,2026-02-10 09:55:29,1min 31s,0s,,"-36.417841, -71.963647",
Movimiento,2026-02-10 09:55:29,2026-02-10 10:17:13,21min 44s,0s,,18.37 Km,97 kph,48 kph,
Detenido,2026-02-10 10:17:13,2026-02-10 10:18:44,1min 31s,0s,,"-36.336453, -72.066853",
Movimiento,2026-02-10 10:18:44,2026-02-10 10:19:45,1min 1s,0s,,0.2 Km,10 kph,9 kph,
Detenido,2026-02-10 10:19:45,2026-02-10 10:22:16,2min 31s,0s,,"-36.338269, -72.067862",
Movimiento,2026-02-10 10:22:16,2026-02-10 10:24:48,2min 32s,0s,,0.27 Km,7 kph,6 kph,
Detenido,2026-02-10 10:24:48,2026-02-10 10:26:19,1min 31s,0s,,"-36.340689, -72.068616",
Movimiento,2026-02-10 10:26:19,2026-02-10 10:26:49,30s,3s,,0.1 Km,12 kph,10 kph,
Detenido,2026-02-10 10:26:49,2026-02-10 11:04:49,38min 0s,11s,,"-36.340867, -72.069751",
Movimiento,2026-02-10 11:04:49,2026-02-10 11:08:49,4min 0s,30s,,0.34 Km,12 kph,9 kph,
Detenido,2026-02-10 11:08:49,2026-02-10 11:10:42,1min 53s,0s,,"-36.338436, -72.067863",
Movimiento,2026-02-10 11:10:42,2026-02-10 11:15:22,4min 40s,0s,,0.95 Km,35 kph,15 kph,
Detenido,2026-02-10 11:15:22,2026-02-10 11:16:22,1min 0s,0s,,"-36.329792, -72.06053",
Movimiento,2026-02-10 11:16:22,2026-02-10 11:40:22,24min 0s,0s,,18.55 Km,106 kph,53 kph,
Detenido,2026-02-10 11:40:22,2026-02-10 11:42:33,2min 11s,0s,,"-36.43011, -71.959609",
Movimiento,2026-02-10 11:42:33,2026-02-10 11:44:25,1min 52s,0s,,0 Km,7 kph,7 kph,
Detenido,2026-02-10 11:44:25,2026-02-10 12:01:34,17min 9s,1min 0s,,"-36.430075, -71.95958",
Movimiento,2026-02-10 12:01:34,2026-02-10 12:05:43,4min 9s,1min 9s,,0.77 Km,32 kph,20 kph,
Detenido,2026-02-10 12:05:43,2026-02-10 12:06:54,1min 11s,0s,,"-36.423374, -71.963145",
Movimiento,2026-02-10 12:06:54,2026-02-10 12:10:38,3min 44s,0s,,1.04 Km,59 kph,30 kph,
Detenido,2026-02-10 12:10:38,2026-02-10 12:27:43,17min 5s,0s,,"-36.419642, -71.967553",
Movimiento,2026-02-10 12:27:43,2026-02-10 12:34:46,7min 3s,0s,,2.34 Km,52 kph,26 kph,
Detenido,2026-02-10 12:34:46,2026-02-10 14:47:39,2h 12min 53s,0s,,"-36.430109, -71.959618",
Movimiento,2026-02-10 14:47:39,2026-02-10 14:55:16,7min 37s,0s,,2.66 Km,53 kph,31 kph,
Detenido,2026-02-10 14:55:16,2026-02-10 14:57:47,2min 31s,0s,,"-36.422221, -71.968995",
Movimiento,2026-02-10 14:57:47,2026-02-10 14:58:48,1min 1s,0s,,0.01 Km,7 kph,7 kph,
Detenido,2026-02-10 14:58:48,2026-02-10 15:33:57,35min 9s,30s,,"-36.422451, -71.969096",
Movimiento,2026-02-10 15:33:57,2026-02-10 15:43:01,9min 4s,0s,,2.12 Km,46 kph,24 kph,
Detenido,2026-02-10 15:43:01,2026-02-10 16:01:13,18min 12s,0s,,"-36.424374, -71.952291",
Movimiento,2026-02-10 16:01:13,2026-02-10 16:02:14,1min 1s,0s,,0.33 Km,52 kph,52 kph,
Detenido,2026-02-10 16:02:14,2026-02-10 16:19:47,17min 33s,0s,,"-36.429417, -71.954002",
Movimiento,2026-02-10 16:19:47,2026-02-10 16:23:49,4min 2s,0s,,0.65 Km,29 kph,22 kph,
Detenido,2026-02-10 16:23:49,2026-02-10 17:30:09,1h 6min 20s,0s,,"-36.430127, -71.959656",
Movimiento,2026-02-10 17:30:09,2026-02-10 17:31:21,1min 12s,1min 12s,,0.01 Km,8 kph,8 kph,
Detenido,2026-02-10 17:31:21,2026-02-10 17:31:51,30s,30s,,"-36.429456, -71.958893",
Movimiento,2026-02-10 17:31:51,2026-02-10 17:32:52,1min 1s,57s,,0.04 Km,19 kph,13 kph,
Detenido,2026-02-10 17:32:52,2026-02-10 18:39:31,1h 6min 39s,1min 0s,,"-36.429355, -71.959593",
Movimiento,2026-02-10 18:39:31,2026-02-10 18:40:54,1min 23s,0s,,0.37 Km,30 kph,25 kph,
Detenido,2026-02-10 18:40:54,2026-02-10 18:48:24,7min 30s,0s,,"-36.428594, -71.960277",
Movimiento,2026-02-10 18:48:24,2026-02-10 18:48:55,31s,0s,,0.16 Km,25 kph,21 kph,
Detenido,2026-02-10 18:48:55,2026-02-11 08:50:11,14h 1min 16s,36s,,"-36.430103, -71.959627",
Movimiento,2026-02-11 08:50:11,2026-02-11 08:55:38,5min 27s,28s,,2.09 Km,43 kph,27 kph,
Detenido,2026-02-11 08:55:38,2026-02-11 09:27:49,32min 11s,0s,,"-36.425557, -71.970921",
Movimiento,2026-02-11 09:27:49,2026-02-11 09:31:51,4min 2s,30s,,1.81 Km,46 kph,30 kph,
Detenido,2026-02-11 09:31:51,2026-02-11 11:18:13,1h 46min 22s,0s,,"-36.430195, -71.959921",
Movimiento,2026-02-11 11:18:13,2026-02-11 11:22:38,4min 25s,0s,,1.26 Km,33 kph,17 kph,
Detenido,2026-02-11 11:22:38,2026-02-11 11:23:08,30s,0s,,"-36.425932, -71.949399",
Movimiento,2026-02-11 11:23:08,2026-02-11 11:43:57,20min 49s,0s,,13.81 Km,74 kph,58 kph,
Detenido,2026-02-11 11:43:57,2026-02-11 11:59:02,15min 5s,0s,,"-36.409386, -71.824581",
Movimiento,2026-02-11 11:59:02,2026-02-11 12:12:39,13min 37s,31s,,14.24 Km,87 kph,59 kph,
Detenido,2026-02-11 12:12:39,2026-02-11 12:13:43,1min 4s,1min 4s,,"-36.42627, -71.947465",
Movimiento,2026-02-11 12:13:43,2026-02-11 12:15:10,1min 27s,13s,,0.76 Km,47 kph,22 kph,
Detenido,2026-02-11 12:15:10,2026-02-11 12:17:11,2min 1s,2min 1s,,"-36.430431, -71.952652",
Movimiento,2026-02-11 12:17:11,2026-02-11 12:18:42,1min 31s,1min 0s,,0.28 Km,29 kph,18 kph,
Detenido,2026-02-11 12:18:42,2026-02-11 14:14:36,1h 55min 54s,0s,,"-36.430022, -71.959719",
Movimiento,2026-02-11 14:14:36,2026-02-11 14:15:21,45s,0s,,0.04 Km,7 kph,5 kph,
Detenido,2026-02-11 14:15:21,2026-02-11 14:17:26,2min 5s,0s,,"-36.430447, -71.959241",
Movimiento,2026-02-11 14:17:26,2026-02-11 14:26:27,9min 1s,0s,,11.39 Km,111 kph,83 kph,
Detenido,2026-02-11 14:26:27,2026-02-11 14:33:25,6min 58s,0s,,"-36.475227, -72.051327",
Movimiento,2026-02-11 14:33:25,2026-02-11 14:48:36,15min 11s,19s,,13.29 Km,111 kph,53 kph,
Detenido,2026-02-11 14:48:36,2026-02-11 15:13:22,24min 46s,1min 31s,,"-36.430161, -71.954171",
Movimiento,2026-02-11 15:13:22,2026-02-11 15:17:26,4min 4s,0s,,0.72 Km,33 kph,16 kph,
Detenido,2026-02-11 15:17:26,2026-02-11 15:36:04,18min 38s,8s,,"-36.429133, -71.959133",
Movimiento,2026-02-11 15:36:04,2026-02-11 15:37:36,1min 32s,1min 32s,,0.03 Km,13 kph,13 kph,
Detenido,2026-02-11 15:37:36,2026-02-11 15:37:44,8s,8s,,"-36.4295, -71.960417",
Movimiento,2026-02-11 15:37:44,2026-02-11 15:38:36,52s,13s,,0.15 Km,14 kph,9 kph,
Detenido,2026-02-11 15:38:36,2026-02-12 10:59:30,19h 20min 54s,0s,,"-36.43009, -71.959618",
Movimiento,2026-02-12 10:59:30,2026-02-12 11:01:32,2min 2s,0s,,0.14 Km,26 kph,15 kph,
Detenido,2026-02-12 11:01:32,2026-02-12 11:09:56,8min 24s,0s,,"-36.429184, -71.959149",
Movimiento,2026-02-12 11:09:56,2026-02-12 11:11:26,1min 30s,0s,,0.01 Km,8 kph,7 kph,
Detenido,2026-02-12 11:11:26,2026-02-12 11:17:48,6min 22s,0s,,"-36.429238, -71.959231",
Movimiento,2026-02-12 11:17:48,2026-02-12 11:18:30,42s,0s,,0 Km,8 kph,8 kph,
Detenido,2026-02-12 11:18:30,2026-02-12 11:20:33,2min 3s,1min 3s,,"-36.42896, -71.960035",
Movimiento,2026-02-12 11:20:33,2026-02-12 11:24:32,3min 59s,0s,,2.04 Km,54 kph,30 kph,
Detenido,2026-02-12 11:24:32,2026-02-12 11:38:45,14min 13s,7s,,"-36.4225, -71.969072",
Movimiento,2026-02-12 11:38:45,2026-02-12 11:41:39,2min 54s,1min 1s,,0.52 Km,28 kph,18 kph,
Detenido,2026-02-12 11:41:39,2026-02-12 11:59:17,17min 38s,0s,,"-36.423704, -71.975226",
Movimiento,2026-02-12 11:59:17,2026-02-12 12:06:51,7min 34s,0s,,2.5 Km,38 kph,23 kph,
Detenido,2026-02-12 12:06:51,2026-02-12 12:16:22,9min 31s,0s,,"-36.430093, -71.959696",
Movimiento,2026-02-12 12:16:22,2026-02-12 12:17:36,1min 14s,13s,,0.56 Km,31 kph,22 kph,
Detenido,2026-02-12 12:17:36,2026-02-12 12:19:54,2min 18s,2min 18s,,"-36.434973, -71.959025",
Movimiento,2026-02-12 12:19:54,2026-02-12 12:23:56,4min 2s,0s,,1.72 Km,46 kph,28 kph,
Detenido,2026-02-12 12:23:56,2026-02-12 12:30:31,6min 35s,0s,,"-36.423866, -71.973696",
Movimiento,2026-02-12 12:30:31,2026-02-12 12:36:04,5min 33s,29s,,2.32 Km,51 kph,29 kph,
Detenido,2026-02-12 12:36:04,2026-02-12 14:08:12,1h 32min 8s,31s,,"-36.430106, -71.960707",
Movimiento,2026-02-12 14:08:12,2026-02-12 14:10:13,2min 1s,1min 1s,,0.56 Km,10 kph,9 kph,
Detenido,2026-02-12 14:10:13,2026-02-12 14:11:14,1min 1s,1min 1s,,"-36.422244, -71.956357",
Movimiento,2026-02-12 14:11:14,2026-02-12 14:13:45,2min 31s,0s,,1.25 Km,36 kph,29 kph,
Detenido,2026-02-12 14:13:45,2026-02-12 14:16:47,3min 2s,0s,,"-36.416891, -71.964162",
Movimiento,2026-02-12 14:16:47,2026-02-12 14:31:55,15min 8s,31s,,16.65 Km,90 kph,66 kph,
Detenido,2026-02-12 14:31:55,2026-02-12 14:33:26,1min 31s,1min 31s,,"-36.328412, -72.0593",
Movimiento,2026-02-12 14:33:26,2026-02-12 14:35:56,2min 30s,0s,,1.09 Km,33 kph,26 kph,
Detenido,2026-02-12 14:35:56,2026-02-12 14:36:57,1min 1s,0s,,"-36.336567, -72.06685",
Movimiento,2026-02-12 14:36:57,2026-02-12 14:37:57,1min 0s,0s,,0.11 Km,16 kph,16 kph,
Detenido,2026-02-12 14:37:57,2026-02-12 14:39:27,1min 30s,0s,,"-36.338301, -72.067855",
Movimiento,2026-02-12 14:39:27,2026-02-12 14:40:57,1min 30s,0s,,0.08 Km,11 kph,11 kph,
Detenido,2026-02-12 14:40:57,2026-02-12 14:41:57,1min 0s,0s,,"-36.340656, -72.068608",
Movimiento,2026-02-12 14:41:57,2026-02-12 14:43:28,1min 31s,0s,,0.13 Km,10 kph,8 kph,
Detenido,2026-02-12 14:43:28,2026-02-12 15:37:30,54min 2s,0s,,"-36.340982, -72.069695",
Movimiento,2026-02-12 15:37:30,2026-02-12 15:38:39,1min 9s,45s,,0.1 Km,8 kph,7 kph,
Detenido,2026-02-12 15:38:39,2026-02-12 15:43:04,4min 25s,0s,,"-36.340745, -72.068647",
Movimiento,2026-02-12 15:43:04,2026-02-12 15:47:07,4min 3s,0s,,0.29 Km,33 kph,17 kph,
Detenido,2026-02-12 15:47:07,2026-02-12 15:48:07,1min 0s,0s,,"-36.329915, -72.060624",
Movimiento,2026-02-12 15:48:07,2026-02-12 16:03:16,15min 9s,0s,,10.82 Km,95 kph,61 kph,
Detenido,2026-02-12 16:03:16,2026-02-12 16:38:32,35min 16s,0s,,"-36.365249, -71.965884",
Movimiento,2026-02-12 16:38:32,2026-02-12 16:47:36,9min 4s,0s,,6.16 Km,78 kph,49 kph,
Detenido,2026-02-12 16:47:36,2026-02-12 16:48:06,30s,0s,,"-36.422842, -71.964614",
Movimiento,2026-02-12 16:48:06,2026-02-12 16:50:07,2min 1s,38s,,0.62 Km,47 kph,44 kph,
Detenido,2026-02-12 16:50:07,2026-02-12 16:51:08,1min 1s,1min 1s,,"-36.429821, -71.962188",
Movimiento,2026-02-12 16:51:08,2026-02-12 16:52:08,1min 0s,0s,,0.21 Km,10 kph,10 kph,
Detenido,2026-02-12 16:52:08,2026-02-12 17:22:51,30min 43s,1min 52s,,"-36.430171, -71.95959",
Movimiento,2026-02-12 17:22:51,2026-02-12 17:23:31,40s,40s,,0.13 Km,8 kph,8 kph,
Detenido,2026-02-12 17:23:31,2026-02-12 18:00:58,37min 27s,0s,,"-36.429277, -71.95955",
Movimiento,2026-02-12 18:00:58,2026-02-12 18:02:59,2min 1s,0s,,0.4 Km,30 kph,20 kph,
Detenido,2026-02-12 18:02:59,2026-02-12 18:10:15,7min 16s,59s,,"-36.428444, -71.960072",
Movimiento,2026-02-12 18:10:15,2026-02-12 18:11:16,1min 1s,0s,,0.13 Km,16 kph,16 kph,
Detenido,2026-02-12 18:11:16,2026-02-13 08:32:43,14h 21min 27s,52s,,"-36.430166, -71.959622",
Movimiento,2026-02-13 08:32:43,2026-02-13 08:34:45,2min 2s,0s,,1.39 Km,37 kph,22 kph,
Detenido,2026-02-13 08:34:45,2026-02-13 08:36:46,2min 1s,0s,,"-36.425944, -71.949305",
Movimiento,2026-02-13 08:36:46,2026-02-13 08:47:58,11min 12s,0s,,11.88 Km,118 kph,60 kph,
Detenido,2026-02-13 08:47:58,2026-02-13 08:48:59,1min 1s,0s,,"-36.400031, -71.877009",
Movimiento,2026-02-13 08:48:59,2026-02-13 08:51:30,2min 31s,0s,,0.45 Km,36 kph,36 kph,
Detenido,2026-02-13 08:51:30,2026-02-13 09:15:49,24min 19s,1min 1s,,"-36.403457, -71.871268",
Movimiento,2026-02-13 09:15:49,2026-02-13 09:35:00,19min 11s,0s,,18.95 Km,90 kph,54 kph,
Detenido,2026-02-13 09:35:00,2026-02-13 09:57:09,22min 9s,0s,,"-36.397349, -71.761989",
Movimiento,2026-02-13 09:57:09,2026-02-13 09:58:09,1min 0s,0s,,0.51 Km,54 kph,44 kph,
Detenido,2026-02-13 09:58:09,2026-02-13 10:00:11,2min 2s,0s,,"-36.397118, -71.768266",
Movimiento,2026-02-13 10:00:11,2026-02-13 10:25:35,25min 24s,0s,,14.45 Km,82 kph,44 kph,
Detenido,2026-02-13 10:25:35,2026-02-13 10:37:01,11min 26s,0s,,"-36.450802, -71.837395",
Movimiento,2026-02-13 10:37:01,2026-02-13 10:48:57,11min 56s,0s,,10.9 Km,83 kph,48 kph,
Detenido,2026-02-13 10:48:57,2026-02-13 11:10:41,21min 44s,0s,,"-36.427953, -71.935999",
Movimiento,2026-02-13 11:10:41,2026-02-13 11:11:42,1min 1s,0s,,0.64 Km,55 kph,36 kph,
Detenido,2026-02-13 11:11:42,2026-02-13 11:34:55,23min 13s,31s,,"-36.426801, -71.943359",
Movimiento,2026-02-13 11:34:55,2026-02-13 11:39:27,4min 32s,0s,,1.35 Km,101 kph,40 kph,
Detenido,2026-02-13 11:39:27,2026-02-13 11:43:49,4min 22s,0s,,"-36.414229, -71.948268",
Movimiento,2026-02-13 11:43:49,2026-02-13 11:45:31,1min 42s,0s,,0.54 Km,29 kph,23 kph,
Detenido,2026-02-13 11:45:31,2026-02-13 12:06:41,21min 10s,0s,,"-36.414154, -71.953641",
Movimiento,2026-02-13 12:06:41,2026-02-13 12:09:42,3min 1s,0s,,1.43 Km,53 kph,17 kph,
Detenido,2026-02-13 12:09:42,2026-02-13 12:32:26,22min 44s,0s,,"-36.424385, -71.952265",
Movimiento,2026-02-13 12:32:26,2026-02-13 12:35:59,3min 33s,0s,,0.55 Km,24 kph,17 kph,
Detenido,2026-02-13 12:35:59,2026-02-13 12:37:00,1min 1s,0s,,"-36.424273, -71.95789",
Movimiento,2026-02-13 12:37:00,2026-02-13 12:42:59,5min 59s,4s,,1.65 Km,36 kph,22 kph,
Detenido,2026-02-13 12:42:59,2026-02-13 13:11:36,28min 37s,6s,,"-36.422505, -71.969046",
Movimiento,2026-02-13 13:11:36,2026-02-13 13:15:02,3min 26s,1min 31s,,0.76 Km,50 kph,19 kph,
Detenido,2026-02-13 13:15:02,2026-02-13 13:15:24,22s,22s,,"-36.432908, -71.968831",
Movimiento,2026-02-13 13:15:24,2026-02-13 13:18:04,2min 40s,0s,,0.75 Km,28 kph,20 kph,
Detenido,2026-02-13 13:18:04,2026-02-13 14:45:48,1h 27min 44s,31s,,"-36.430061, -71.960831",
Movimiento,2026-02-13 14:45:48,2026-02-13 14:46:18,30s,6s,,0.08 Km,14 kph,11 kph,
Detenido,2026-02-13 14:46:18,2026-02-13 14:48:19,2min 1s,0s,,"-36.430197, -71.959086",
Movimiento,2026-02-13 14:48:19,2026-02-13 14:53:51,5min 32s,0s,,2.57 Km,43 kph,28 kph,
Detenido,2026-02-13 14:53:51,2026-02-13 14:56:46,2min 55s,0s,,"-36.423465, -71.975798",
Movimiento,2026-02-13 14:56:46,2026-02-13 14:56:52,6s,6s,,0 Km,8 kph,8 kph,
Detenido,2026-02-13 14:56:52,2026-02-13 15:14:39,17min 47s,1min 29s,,"-36.423766, -71.974557",
Movimiento,2026-02-13 15:14:39,2026-02-13 15:16:40,2min 1s,0s,,0.86 Km,40 kph,21 kph,
Detenido,2026-02-13 15:16:40,2026-02-13 15:28:06,11min 26s,0s,,"-36.422479, -71.969031",
Movimiento,2026-02-13 15:28:06,2026-02-13 15:48:47,20min 41s,0s,,18.13 Km,101 kph,54 kph,
Detenido,2026-02-13 15:48:47,2026-02-13 15:50:17,1min 30s,0s,,"-36.329868, -72.060561",
Movimiento,2026-02-13 15:50:17,2026-02-13 15:51:48,1min 31s,0s,,0.17 Km,28 kph,28 kph,
Detenido,2026-02-13 15:51:48,2026-02-13 15:52:52,1min 4s,0s,,"-36.336484, -72.06689",
Movimiento,2026-02-13 15:52:52,2026-02-13 15:55:49,2min 57s,2min 0s,,0.17 Km,14 kph,13 kph,
Detenido,2026-02-13 15:55:49,2026-02-13 15:57:21,1min 32s,1min 32s,,"-36.338406, -72.067846",
Movimiento,2026-02-13 15:57:21,2026-02-13 16:00:52,3min 31s,0s,,0.32 Km,11 kph,8 kph,
Detenido,2026-02-13 16:00:52,2026-02-13 16:29:28,28min 36s,0s,,"-36.340987, -72.069728",
Movimiento,2026-02-13 16:29:28,2026-02-13 16:30:45,1min 17s,0s,,0.02 Km,8 kph,7 kph,
Detenido,2026-02-13 16:30:45,2026-02-13 16:30:51,6s,0s,,"-36.340816, -72.068626",
Movimiento,2026-02-13 16:30:51,2026-02-13 16:31:15,24s,0s,,0 Km,6 kph,6 kph,
Detenido,2026-02-13 16:31:15,2026-02-13 16:32:16,1min 1s,0s,,"-36.340714, -72.068599",
Movimiento,2026-02-13 16:32:16,2026-02-13 16:32:46,30s,30s,,0.12 Km,8 kph,8 kph,
Detenido,2026-02-13 16:32:46,2026-02-13 16:35:17,2min 31s,31s,,"-36.339154, -72.068087",
Movimiento,2026-02-13 16:35:17,2026-02-13 16:37:49,2min 32s,0s,,0.16 Km,19 kph,15 kph,
Detenido,2026-02-13 16:37:49,2026-02-13 16:38:49,1min 0s,0s,,"-36.336029, -72.066178",
Movimiento,2026-02-13 16:38:49,2026-02-13 16:40:20,1min 31s,0s,,0.68 Km,37 kph,30 kph,
Detenido,2026-02-13 16:40:20,2026-02-13 16:41:51,1min 31s,0s,,"-36.329954, -72.060601",
Movimiento,2026-02-13 16:41:51,2026-02-13 17:04:31,22min 40s,0s,,18.15 Km,100 kph,50 kph,
Detenido,2026-02-13 17:04:31,2026-02-13 17:06:35,2min 4s,0s,,"-36.427678, -71.96003",
Movimiento,2026-02-13 17:06:35,2026-02-13 17:07:33,58s,58s,,0.15 Km,33 kph,33 kph,
Detenido,2026-02-13 17:07:33,2026-02-13 17:32:45,25min 12s,0s,,"-36.42916, -71.959135",
Movimiento,2026-02-13 17:32:45,2026-02-13 17:33:46,1min 1s,0s,,0.29 Km,34 kph,17 kph,
Detenido,2026-02-13 17:33:46,2026-02-14 08:32:51,14h 59min 5s,0s,,"-36.430152, -71.959675",
Movimiento,2026-02-14 08:32:51,2026-02-14 08:55:04,22min 13s,0s,,29.26 Km,115 kph,72 kph,
Detenido,2026-02-14 08:55:04,2026-02-14 09:13:44,18min 40s,0s,,"-36.292875, -71.900106",
Movimiento,2026-02-14 09:13:44,2026-02-14 09:31:53,18min 9s,0s,,18.07 Km,114 kph,50 kph,
Detenido,2026-02-14 09:31:53,2026-02-14 09:41:21,9min 28s,0s,,"-36.40366, -71.871579",
Movimiento,2026-02-14 09:41:21,2026-02-14 09:55:26,14min 5s,0s,,14.19 Km,93 kph,56 kph,
Detenido,2026-02-14 09:55:26,2026-02-14 10:13:36,18min 10s,0s,,"-36.397387, -71.76188",
Movimiento,2026-02-14 10:13:36,2026-02-14 10:22:11,8min 35s,30s,,10.16 Km,106 kph,73 kph,
Detenido,2026-02-14 10:22:11,2026-02-14 10:24:12,2min 1s,1min 1s,,"-36.466307, -71.770133",
Movimiento,2026-02-14 10:24:12,2026-02-14 10:24:42,30s,0s,,0.09 Km,6 kph,6 kph,
Detenido,2026-02-14 10:24:42,2026-02-14 10:26:11,1min 29s,0s,,"-36.468876, -71.770954",
Movimiento,2026-02-14 10:26:11,2026-02-14 10:26:44,33s,28s,,0.04 Km,9 kph,7 kph,
Detenido,2026-02-14 10:26:44,2026-02-14 10:56:41,29min 57s,0s,,"-36.468891, -71.770944",
Movimiento,2026-02-14 10:56:41,2026-02-14 10:59:28,2min 47s,0s,,2.48 Km,87 kph,41 kph,
Detenido,2026-02-14 10:59:28,2026-02-14 11:04:06,4min 38s,0s,,"-36.467474, -71.793132",
Movimiento,2026-02-14 11:04:06,2026-02-14 11:09:39,5min 33s,1min 28s,,4.97 Km,99 kph,63 kph,
Detenido,2026-02-14 11:09:39,2026-02-14 11:33:11,23min 32s,0s,,"-36.450799, -71.837416",
Movimiento,2026-02-14 11:33:11,2026-02-14 11:50:01,16min 50s,0s,,11.73 Km,59 kph,41 kph,
Detenido,2026-02-14 11:50:01,2026-02-14 11:57:04,7min 3s,0s,,"-36.415634, -71.945061",
Movimiento,2026-02-14 11:57:04,2026-02-14 12:00:36,3min 32s,0s,,1.26 Km,34 kph,28 kph,
Detenido,2026-02-14 12:00:36,2026-02-14 12:33:29,32min 53s,41s,,"-36.412463, -71.928548",
Movimiento,2026-02-14 12:33:29,2026-02-14 12:39:32,6min 3s,0s,,2.42 Km,55 kph,36 kph,
Detenido,2026-02-14 12:39:32,2026-02-14 12:55:24,15min 52s,0s,,"-36.414177, -71.953688",
Movimiento,2026-02-14 12:55:24,2026-02-14 12:56:35,1min 11s,0s,,0.51 Km,31 kph,21 kph,
Detenido,2026-02-14 12:56:35,2026-02-14 12:59:06,2min 31s,0s,,"-36.418014, -71.956612",
Movimiento,2026-02-14 12:59:06,2026-02-14 12:59:36,30s,0s,,0.3 Km,24 kph,24 kph,
Detenido,2026-02-14 12:59:36,2026-02-14 13:00:37,1min 1s,0s,,"-36.4263, -71.959377",
Movimiento,2026-02-14 13:00:37,2026-02-14 13:03:38,3min 1s,0s,,0.49 Km,20 kph,15 kph,
Detenido,2026-02-14 13:03:38,2026-02-14 18:38:23,5h 34min 45s,47s,,"-36.430123, -71.95967",
Movimiento,2026-02-14 18:38:23,2026-02-14 18:40:55,2min 32s,0s,,0.15 Km,41 kph,21 kph,
Detenido,2026-02-14 18:40:55,2026-02-14 19:16:01,35min 6s,0s,,"-36.429317, -71.959548",
Movimiento,2026-02-14 19:16:01,2026-02-14 19:18:42,2min 41s,0s,,0.42 Km,32 kph,14 kph,
Detenido,2026-02-14 19:18:42,2026-02-14 19:22:19,3min 37s,0s,,"-36.428568, -71.960367",
Movimiento,2026-02-14 19:22:19,2026-02-14 19:23:10,51s,0s,,0.23 Km,14 kph,14 kph,
Detenido,2026-02-14 19:23:10,2026-02-15 08:15:18,12h 52min 8s,0s,,"-36.430087, -71.959639",
Movimiento,2026-02-15 08:15:18,2026-02-15 08:18:52,3min 34s,0s,,1.28 Km,40 kph,23 kph,
Detenido,2026-02-15 08:18:52,2026-02-15 08:20:35,1min 43s,0s,,"-36.426005, -71.949107",
Movimiento,2026-02-15 08:20:35,2026-02-15 08:27:57,7min 22s,0s,,10.75 Km,105 kph,67 kph,
Detenido,2026-02-15 08:27:57,2026-02-15 08:30:46,2min 49s,7s,,"-36.357657, -71.871326",
Movimiento,2026-02-15 08:30:46,2026-02-15 08:45:29,14min 43s,23s,,13.26 Km,110 kph,60 kph,
Detenido,2026-02-15 08:45:29,2026-02-15 09:03:45,18min 16s,1min 38s,,"-36.292831, -71.900076",
Movimiento,2026-02-15 09:03:45,2026-02-15 09:20:56,17min 11s,1min 1s,,17.21 Km,104 kph,56 kph,
Detenido,2026-02-15 09:20:56,2026-02-15 09:37:02,16min 6s,0s,,"-36.403465, -71.871388",
Movimiento,2026-02-15 09:37:02,2026-02-15 09:52:41,15min 39s,30s,,13.43 Km,67 kph,46 kph,
Detenido,2026-02-15 09:52:41,2026-02-15 10:18:50,26min 9s,1min 17s,,"-36.468819, -71.770964",
Movimiento,2026-02-15 10:18:50,2026-02-15 10:28:16,9min 26s,0s,,7.51 Km,103 kph,70 kph,
Detenido,2026-02-15 10:28:16,2026-02-15 10:52:02,23min 46s,0s,,"-36.450097, -71.8375",
Movimiento,2026-02-15 10:52:02,2026-02-15 11:09:16,17min 14s,0s,,12.76 Km,77 kph,45 kph,
Detenido,2026-02-15 11:09:16,2026-02-15 11:10:29,1min 13s,0s,,"-36.429266, -71.95856",
Movimiento,2026-02-15 11:10:29,2026-02-15 11:11:17,48s,30s,,0.15 Km,18 kph,14 kph,
Detenido,2026-02-15 11:11:17,2026-02-15 11:23:23,12min 6s,0s,,"-36.430149, -71.959589",
Movimiento,2026-02-15 11:23:23,2026-02-15 11:25:24,2min 1s,0s,,0.42 Km,15 kph,10 kph,
Detenido,2026-02-15 11:25:24,2026-02-15 11:26:55,1min 31s,0s,,"-36.424665, -71.957194",
Movimiento,2026-02-15 11:26:55,2026-02-15 11:29:26,2min 31s,0s,,1.19 Km,23 kph,19 kph,
Detenido,2026-02-15 11:29:26,2026-02-15 11:54:57,25min 31s,0s,,"-36.414186, -71.953641",
Movimiento,2026-02-15 11:54:57,2026-02-15 12:01:31,6min 34s,0s,,1.94 Km,40 kph,19 kph,
Detenido,2026-02-15 12:01:31,2026-02-15 12:27:16,25min 45s,0s,,"-36.41881, -71.970684",
Movimiento,2026-02-15 12:27:16,2026-02-15 12:30:48,3min 32s,9s,,1.35 Km,36 kph,23 kph,
Detenido,2026-02-15 12:30:48,2026-02-15 12:56:02,25min 14s,0s,,"-36.423728, -71.97467",
Movimiento,2026-02-15 12:56:02,2026-02-15 13:06:03,10min 1s,30s,,2.79 Km,49 kph,19 kph,
Detenido,2026-02-15 13:06:03,2026-02-15 13:11:37,5min 34s,0s,,"-36.425059, -71.958928",
Movimiento,2026-02-15 13:11:37,2026-02-15 13:14:08,2min 31s,0s,,0.53 Km,33 kph,19 kph,
Detenido,2026-02-15 13:14:08,2026-02-15 14:18:08,1h 4min 0s,0s,,"-36.430121, -71.959632",
Movimiento,2026-02-15 14:18:08,2026-02-15 14:21:40,3min 32s,0s,,0.68 Km,38 kph,20 kph,
Detenido,2026-02-15 14:21:40,2026-02-15 14:22:10,30s,10s,,"-36.423309, -71.956734",
Movimiento,2026-02-15 14:22:10,2026-02-15 14:25:11,3min 1s,0s,,0.56 Km,22 kph,19 kph,
Detenido,2026-02-15 14:25:11,2026-02-15 14:26:34,1min 23s,0s,,"-36.414174, -71.953686",
Movimiento,2026-02-15 14:26:34,2026-02-15 14:28:13,1min 39s,0s,,0.37 Km,30 kph,25 kph,
Detenido,2026-02-15 14:28:13,2026-02-15 14:31:15,3min 2s,0s,,"-36.412027, -71.950464",
Movimiento,2026-02-15 14:31:15,2026-02-15 14:33:00,1min 45s,2s,,0.53 Km,30 kph,17 kph,
Detenido,2026-02-15 14:33:00,2026-02-15 14:46:25,13min 25s,0s,,"-36.414155, -71.953615",
Movimiento,2026-02-15 14:46:25,2026-02-15 14:51:27,5min 2s,0s,,1.51 Km,36 kph,24 kph,
Detenido,2026-02-15 14:51:27,2026-02-15 15:00:31,9min 4s,0s,,"-36.429134, -71.959152",
Movimiento,2026-02-15 15:00:31,2026-02-15 15:01:31,1min 0s,0s,,0.21 Km,19 kph,11 kph,
Detenido,2026-02-15 15:01:31,2026-02-16 08:22:56,17h 21min 25s,0s,,"-36.430146, -71.959605",
Movimiento,2026-02-16 08:22:56,2026-02-16 08:26:58,4min 2s,0s,,1.14 Km,43 kph,27 kph,
Detenido,2026-02-16 08:26:58,2026-02-16 08:27:28,30s,0s,,"-36.425917, -71.949358",
Movimiento,2026-02-16 08:27:28,2026-02-16 08:38:32,11min 4s,0s,,10.42 Km,108 kph,63 kph,
Detenido,2026-02-16 08:38:32,2026-02-16 09:08:15,29min 43s,0s,,"-36.403672, -71.871532",
Movimiento,2026-02-16 09:08:15,2026-02-16 09:26:05,17min 50s,2min 12s,,13.99 Km,75 kph,49 kph,
Detenido,2026-02-16 09:26:05,2026-02-16 09:41:34,15min 29s,0s,,"-36.397413, -71.761879",
Movimiento,2026-02-16 09:41:34,2026-02-16 09:58:54,17min 20s,46s,,14.74 Km,79 kph,50 kph,
Detenido,2026-02-16 09:58:54,2026-02-16 10:17:01,18min 7s,0s,,"-36.450783, -71.83739",
Movimiento,2026-02-16 10:17:01,2026-02-16 10:29:34,12min 33s,0s,,10.31 Km,83 kph,47 kph,
Detenido,2026-02-16 10:29:34,2026-02-16 10:54:49,25min 15s,0s,,"-36.428087, -71.936075",
Movimiento,2026-02-16 10:54:49,2026-02-16 10:55:50,1min 1s,0s,,0.61 Km,50 kph,41 kph,
Detenido,2026-02-16 10:55:50,2026-02-16 11:13:59,18min 9s,0s,,"-36.426819, -71.943308",
Movimiento,2026-02-16 11:13:59,2026-02-16 11:14:59,1min 0s,0s,,0.06 Km,37 kph,37 kph,
Detenido,2026-02-16 11:14:59,2026-02-16 11:16:00,1min 1s,0s,,"-36.426174, -71.947997",
Movimiento,2026-02-16 11:16:00,2026-02-16 11:19:32,3min 32s,0s,,2.29 Km,85 kph,48 kph,
Detenido,2026-02-16 11:19:32,2026-02-16 11:20:02,30s,0s,,"-36.412444, -71.928553",
Movimiento,2026-02-16 11:20:02,2026-02-16 11:20:32,30s,0s,,0.02 Km,9 kph,9 kph,
Detenido,2026-02-16 11:20:32,2026-02-16 11:51:58,31min 26s,0s,,"-36.412653, -71.928484",
Movimiento,2026-02-16 11:51:58,2026-02-16 11:52:49,51s,0s,,0.07 Km,28 kph,18 kph,
Detenido,2026-02-16 11:52:49,2026-02-16 11:54:50,2min 1s,0s,,"-36.412718, -71.930543",
Movimiento,2026-02-16 11:54:50,2026-02-16 12:01:24,6min 34s,0s,,2.54 Km,49 kph,24 kph,
Detenido,2026-02-16 12:01:24,2026-02-16 12:18:02,16min 38s,0s,,"-36.414169, -71.953696",
Movimiento,2026-02-16 12:18:02,2026-02-16 12:21:03,3min 1s,0s,,1.01 Km,42 kph,24 kph,
Detenido,2026-02-16 12:21:03,2026-02-16 12:39:43,18min 40s,0s,,"-36.424197, -71.952189",
Movimiento,2026-02-16 12:39:43,2026-02-16 12:41:14,1min 31s,0s,,0.67 Km,26 kph,21 kph,
Detenido,2026-02-16 12:41:14,2026-02-16 12:43:45,2min 31s,0s,,"-36.42984, -71.95562",
Movimiento,2026-02-16 12:43:45,2026-02-16 12:45:16,1min 31s,0s,,0.22 Km,21 kph,13 kph,
Detenido,2026-02-16 12:45:16,2026-02-16 14:25:35,1h 40min 19s,0s,,"-36.430128, -71.959656",
Movimiento,2026-02-16 14:25:35,2026-02-16 14:27:04,1min 29s,18s,,0.17 Km,13 kph,9 kph,
Detenido,2026-02-16 14:27:04,2026-02-16 15:03:47,36min 43s,0s,,"-36.42921, -71.959178",
Movimiento,2026-02-16 15:03:47,2026-02-16 15:06:18,2min 31s,1min 24s,,0.57 Km,29 kph,21 kph,
Detenido,2026-02-16 15:06:18,2026-02-16 15:10:43,4min 25s,0s,,"-36.428637, -71.960208",
Movimiento,2026-02-16 15:10:43,2026-02-16 15:11:34,51s,1s,,0.21 Km,20 kph,14 kph,
Detenido,2026-02-16 15:11:34,2026-02-17 08:44:06,17h 32min 32s,29s,,"-36.430202, -71.959934",
Movimiento,2026-02-17 08:44:06,2026-02-17 08:45:37,1min 31s,0s,,0.29 Km,29 kph,27 kph,
Detenido,2026-02-17 08:45:37,2026-02-17 08:48:39,3min 2s,0s,,"-36.427078, -71.958032",
Movimiento,2026-02-17 08:48:39,2026-02-17 08:49:39,1min 0s,0s,,0.73 Km,23 kph,18 kph,
Detenido,2026-02-17 08:49:39,2026-02-17 09:15:06,25min 27s,0s,,"-36.418055, -71.954997",
Movimiento,2026-02-17 09:15:06,2026-02-17 09:34:42,19min 36s,0s,,17.31 Km,93 kph,60 kph,
Detenido,2026-02-17 09:34:42,2026-02-17 09:35:43,1min 1s,0s,,"-36.329922, -72.06067",
Movimiento,2026-02-17 09:35:43,2026-02-17 09:37:13,1min 30s,0s,,0.9 Km,41 kph,33 kph,
Detenido,2026-02-17 09:37:13,2026-02-17 09:38:21,1min 8s,0s,,"-36.336443, -72.066905",
Movimiento,2026-02-17 09:38:21,2026-02-17 09:40:45,2min 24s,0s,,0.17 Km,13 kph,10 kph,
Detenido,2026-02-17 09:40:45,2026-02-17 09:42:16,1min 31s,0s,,"-36.338383, -72.067848",
Movimiento,2026-02-17 09:42:16,2026-02-17 09:43:16,1min 0s,0s,,0.17 Km,8 kph,8 kph,
Detenido,2026-02-17 09:43:16,2026-02-17 09:44:47,1min 31s,1min 5s,,"-36.34068, -72.068614",
Movimiento,2026-02-17 09:44:47,2026-02-17 09:45:18,31s,31s,,0.06 Km,13 kph,13 kph,
Detenido,2026-02-17 09:45:18,2026-02-17 10:43:44,58min 26s,0s,,"-36.340861, -72.069748",
Movimiento,2026-02-17 10:43:44,2026-02-17 10:49:47,6min 3s,0s,,0.64 Km,26 kph,11 kph,
Detenido,2026-02-17 10:49:47,2026-02-17 10:51:11,1min 24s,0s,,"-36.33654, -72.066885",
Movimiento,2026-02-17 10:51:11,2026-02-17 11:32:11,41min 0s,0s,,27.46 Km,106 kph,37 kph,
Detenido,2026-02-17 11:32:11,2026-02-17 11:48:16,16min 5s,0s,,"-36.29288, -71.900188",
Movimiento,2026-02-17 11:48:16,2026-02-17 12:16:01,27min 45s,0s,,23.72 Km,126 kph,47 kph,
Detenido,2026-02-17 12:16:01,2026-02-17 12:33:02,17min 1s,23s,,"-36.423528, -71.974919",
Movimiento,2026-02-17 12:33:02,2026-02-17 12:39:35,6min 33s,0s,,2.17 Km,64 kph,24 kph,
Detenido,2026-02-17 12:39:35,2026-02-17 18:48:26,6h 8min 51s,9s,,"-36.430255, -71.959931",
Movimiento,2026-02-17 18:48:26,2026-02-17 18:54:20,5min 54s,0s,,1.81 Km,37 kph,27 kph,
Detenido,2026-02-17 18:54:20,2026-02-17 19:05:30,11min 10s,0s,,"-36.418064, -71.954991",
Movimiento,2026-02-17 19:05:30,2026-02-17 19:11:32,6min 2s,0s,,1.89 Km,43 kph,25 kph,
Detenido,2026-02-17 19:11:32,2026-02-18 12:18:16,17h 6min 44s,0s,,"-36.430132, -71.959593",
Movimiento,2026-02-18 12:18:16,2026-02-18 12:20:17,2min 1s,0s,,0.07 Km,10 kph,8 kph,
Detenido,2026-02-18 12:20:17,2026-02-18 12:51:30,31min 13s,2s,,"-36.432141, -71.957278",
Movimiento,2026-02-18 12:51:30,2026-02-18 12:53:03,1min 33s,0s,,0.46 Km,32 kph,23 kph,
Detenido,2026-02-18 12:53:03,2026-02-18 12:54:04,1min 1s,0s,,"-36.426278, -71.954532",
Movimiento,2026-02-18 12:54:04,2026-02-18 13:01:08,7min 4s,0s,,1.79 Km,27 kph,18 kph,
Detenido,2026-02-18 13:01:08,2026-02-18 15:25:40,2h 24min 32s,0s,,"-36.430146, -71.959616",
Movimiento,2026-02-18 15:25:40,2026-02-18 15:31:43,6min 3s,0s,,8.63 Km,108 kph,68 kph,
Detenido,2026-02-18 15:31:43,2026-02-18 15:53:25,21min 42s,37s,,"-36.477783, -72.016843",
Movimiento,2026-02-18 15:53:25,2026-02-18 16:01:30,8min 5s,0s,,10.62 Km,109 kph,62 kph,
Detenido,2026-02-18 16:01:30,2026-02-18 16:14:06,12min 36s,0s,,"-36.546184, -72.090646",
Movimiento,2026-02-18 16:14:06,2026-02-18 16:48:30,34min 24s,0s,,27.74 Km,100 kph,55 kph,
Detenido,2026-02-18 16:48:30,2026-02-18 17:03:38,15min 8s,0s,,"-36.45089, -71.837393",
Movimiento,2026-02-18 17:03:38,2026-02-18 17:14:13,10min 35s,0s,,9.88 Km,90 kph,51 kph,
Detenido,2026-02-18 17:14:13,2026-02-18 17:41:56,27min 43s,0s,,"-36.405178, -71.868506",
Movimiento,2026-02-18 17:41:56,2026-02-18 17:54:04,12min 8s,0s,,8.56 Km,101 kph,39 kph,
Detenido,2026-02-18 17:54:04,2026-02-18 17:56:05,2min 1s,0s,,"-36.416366, -71.948622",
Movimiento,2026-02-18 17:56:05,2026-02-18 18:00:07,4min 2s,0s,,0.95 Km,41 kph,16 kph,
Detenido,2026-02-18 18:00:07,2026-02-18 18:19:20,19min 13s,0s,,"-36.421264, -71.9533",
Movimiento,2026-02-18 18:19:20,2026-02-18 18:21:48,2min 28s,0s,,0.36 Km,34 kph,22 kph,
Detenido,2026-02-18 18:21:48,2026-02-18 18:27:20,5min 32s,0s,,"-36.418072, -71.954996",
Movimiento,2026-02-18 18:27:20,2026-02-18 18:29:29,2min 9s,30s,,0.78 Km,39 kph,26 kph,
Detenido,2026-02-18 18:29:29,2026-02-18 18:31:00,1min 31s,1min 31s,,"-36.422713, -71.958157",
Movimiento,2026-02-18 18:31:00,2026-02-18 18:31:50,50s,50s,,0.3 Km,19 kph,19 kph,
Detenido,2026-02-18 18:31:50,2026-02-18 18:38:07,6min 17s,1min 12s,,"-36.42664, -71.959484",
Movimiento,2026-02-18 18:38:07,2026-02-18 18:41:09,3min 2s,0s,,0.31 Km,31 kph,17 kph,
Detenido,2026-02-18 18:41:09,2026-02-18 19:03:14,22min 5s,0s,,"-36.42922, -71.959196",
Movimiento,2026-02-18 19:03:14,2026-02-18 19:05:37,2min 23s,0s,,0.18 Km,31 kph,14 kph,
Detenido,2026-02-18 19:05:37,2026-02-19 08:33:35,13h 27min 58s,0s,,"-36.4301, -71.959655",
Movimiento,2026-02-19 08:33:35,2026-02-19 08:47:44,14min 9s,0s,,18.92 Km,112 kph,71 kph,
Detenido,2026-02-19 08:47:44,2026-02-19 09:14:29,26min 45s,0s,,"-36.546154, -72.090561",
Movimiento,2026-02-19 09:14:29,2026-02-19 09:22:47,8min 18s,1min 15s,,5.57 Km,87 kph,41 kph,
Detenido,2026-02-19 09:22:47,2026-02-19 09:25:32,2min 45s,0s,,"-36.507315, -72.0396",
Movimiento,2026-02-19 09:25:32,2026-02-19 09:47:41,22min 9s,0s,,14.58 Km,88 kph,43 kph,
Detenido,2026-02-19 09:47:41,2026-02-19 10:04:33,16min 52s,0s,,"-36.428058, -71.93603",
Movimiento,2026-02-19 10:04:33,2026-02-19 10:06:53,2min 20s,0s,,0.67 Km,54 kph,24 kph,
Detenido,2026-02-19 10:06:53,2026-02-19 10:12:32,5min 39s,0s,,"-36.426809, -71.943364",
Movimiento,2026-02-19 10:12:32,2026-02-19 10:13:57,1min 25s,0s,,0.43 Km,41 kph,25 kph,
Detenido,2026-02-19 10:13:57,2026-02-19 10:15:12,1min 15s,0s,,"-36.426133, -71.948086",
Movimiento,2026-02-19 10:15:12,2026-02-19 10:20:00,4min 48s,1min 7s,,2.72 Km,58 kph,38 kph,
Detenido,2026-02-19 10:20:00,2026-02-19 10:30:04,10min 4s,0s,,"-36.41259, -71.928609",
Movimiento,2026-02-19 10:30:04,2026-02-19 10:30:15,11s,0s,,0.01 Km,14 kph,14 kph,
Detenido,2026-02-19 10:30:15,2026-02-19 10:51:43,21min 28s,0s,,"-36.412504, -71.928577",
Movimiento,2026-02-19 10:51:43,2026-02-19 10:54:25,2min 42s,0s,,1.87 Km,59 kph,40 kph,
Detenido,2026-02-19 10:54:25,2026-02-19 11:01:43,7min 18s,0s,,"-36.416034, -71.949182",
Movimiento,2026-02-19 11:01:43,2026-02-19 11:05:01,3min 18s,0s,,0.62 Km,39 kph,30 kph,
Detenido,2026-02-19 11:05:01,2026-02-19 11:27:45,22min 44s,0s,,"-36.414184, -71.95369",
Movimiento,2026-02-19 11:27:45,2026-02-19 11:31:46,4min 1s,0s,,1.38 Km,49 kph,37 kph,
Detenido,2026-02-19 11:31:46,2026-02-19 11:33:16,1min 30s,0s,,"-36.424594, -71.94952",
Movimiento,2026-02-19 11:33:16,2026-02-19 11:34:28,1min 12s,0s,,0.29 Km,37 kph,23 kph,
Detenido,2026-02-19 11:34:28,2026-02-19 11:46:36,12min 8s,2s,,"-36.422384, -71.951133",
Movimiento,2026-02-19 11:46:36,2026-02-19 11:50:08,3min 32s,0s,,0.49 Km,34 kph,19 kph,
Detenido,2026-02-19 11:50:08,2026-02-19 11:52:06,1min 58s,0s,,"-36.422069, -71.955832",
Movimiento,2026-02-19 11:52:06,2026-02-19 11:54:10,2min 4s,0s,,0.56 Km,32 kph,15 kph,
Detenido,2026-02-19 11:54:10,2026-02-19 11:55:34,1min 24s,0s,,"-36.418034, -71.958268",
Movimiento,2026-02-19 11:55:34,2026-02-19 12:00:13,4min 39s,0s,,1.16 Km,51 kph,20 kph,
Detenido,2026-02-19 12:00:13,2026-02-19 12:21:55,21min 42s,0s,,"-36.418862, -71.970673",
Movimiento,2026-02-19 12:21:55,2026-02-19 12:23:22,1min 27s,0s,,0.7 Km,24 kph,19 kph,
Detenido,2026-02-19 12:23:22,2026-02-19 12:27:02,3min 40s,0s,,"-36.42241, -71.969066",
Movimiento,2026-02-19 12:27:02,2026-02-19 12:27:53,51s,0s,,0.03 Km,6 kph,6 kph,
Detenido,2026-02-19 12:27:53,2026-02-19 12:52:41,24min 48s,0s,,"-36.42238, -71.968823",
Movimiento,2026-02-19 12:52:41,2026-02-19 12:57:57,5min 16s,0s,,1.66 Km,51 kph,33 kph,
Detenido,2026-02-19 12:57:57,2026-02-19 15:23:07,2h 25min 10s,0s,,"-36.430326, -71.959959",
Movimiento,2026-02-19 15:23:07,2026-02-19 15:24:05,58s,0s,,0.02 Km,9 kph,9 kph,
Detenido,2026-02-19 15:24:05,2026-02-19 15:25:06,1min 1s,0s,,"-36.428885, -71.958626",
Movimiento,2026-02-19 15:25:06,2026-02-19 15:30:39,5min 33s,0s,,1.13 Km,26 kph,13 kph,
Detenido,2026-02-19 15:30:39,2026-02-19 15:52:56,22min 17s,0s,,"-36.421285, -71.953265",
Movimiento,2026-02-19 15:52:56,2026-02-19 16:00:56,8min 0s,12s,,2.99 Km,43 kph,25 kph,
Detenido,2026-02-19 16:00:56,2026-02-19 16:49:31,48min 35s,0s,,"-36.423203, -71.97701",
Movimiento,2026-02-19 16:49:31,2026-02-19 16:58:33,9min 2s,0s,,2.74 Km,40 kph,25 kph,
Detenido,2026-02-19 16:58:33,2026-02-20 09:09:37,16h 11min 4s,0s,,"-36.430153, -71.959628",
Movimiento,2026-02-20 09:09:37,2026-02-20 09:10:23,46s,0s,,0.08 Km,27 kph,16 kph,
Detenido,2026-02-20 09:10:23,2026-02-20 09:11:24,1min 1s,0s,,"-36.429347, -71.958778",
Movimiento,2026-02-20 09:11:24,2026-02-20 09:11:54,30s,9s,,0.1 Km,8 kph,7 kph,
Detenido,2026-02-20 09:11:54,2026-02-20 09:36:01,24min 7s,0s,,"-36.429089, -71.96007",
Movimiento,2026-02-20 09:36:01,2026-02-20 09:37:43,1min 42s,0s,,0.08 Km,11 kph,8 kph,
Detenido,2026-02-20 09:37:43,2026-02-20 09:59:56,22min 13s,0s,,"-36.429408, -71.959471",
Movimiento,2026-02-20 09:59:56,2026-02-20 10:03:37,3min 41s,1min 1s,,0.17 Km,25 kph,12 kph,
Detenido,2026-02-20 10:03:37,2026-02-20 10:03:51,14s,14s,,"-36.430185, -71.959927",
Movimiento,2026-02-20 10:03:51,2026-02-20 10:04:07,16s,16s,,0.02 Km,8 kph,8 kph,
Detenido,2026-02-20 10:04:07,2026-02-20 10:21:11,17min 4s,0s,,"-36.430097, -71.959718",
Movimiento,2026-02-20 10:21:11,2026-02-20 10:24:12,3min 1s,0s,,1.5 Km,52 kph,23 kph,
Detenido,2026-02-20 10:24:12,2026-02-20 10:28:14,4min 2s,0s,,"-36.432973, -71.968297",
Movimiento,2026-02-20 10:28:14,2026-02-20 10:30:48,2min 34s,32s,,1.56 Km,44 kph,25 kph,
Detenido,2026-02-20 10:30:48,2026-02-20 10:56:30,25min 42s,0s,,"-36.422616, -71.977218",
Movimiento,2026-02-20 10:56:30,2026-02-20 11:01:00,4min 30s,24s,,1.8 Km,41 kph,30 kph,
Detenido,2026-02-20 11:01:00,2026-02-20 11:02:08,1min 8s,1min 8s,,"-36.432873, -71.968878",
Movimiento,2026-02-20 11:02:08,2026-02-20 11:16:10,14min 2s,0s,,18.12 Km,112 kph,71 kph,
Detenido,2026-02-20 11:16:10,2026-02-20 11:33:13,17min 3s,0s,,"-36.546118, -72.090616",
Movimiento,2026-02-20 11:33:13,2026-02-20 11:58:23,25min 10s,0s,,28.12 Km,106 kph,68 kph,
Detenido,2026-02-20 11:58:23,2026-02-20 12:09:23,11min 0s,0s,,"-36.450778, -71.837391",
Movimiento,2026-02-20 12:09:23,2026-02-20 12:23:30,14min 7s,0s,,11.3 Km,81 kph,47 kph,
Detenido,2026-02-20 12:23:30,2026-02-20 13:13:27,49min 57s,0s,,"-36.405177, -71.868491",
Movimiento,2026-02-20 13:13:27,2026-02-20 13:22:32,9min 5s,0s,,6.56 Km,89 kph,40 kph,
Detenido,2026-02-20 13:22:32,2026-02-20 13:52:49,30min 17s,0s,,"-36.412677, -71.928476",
Movimiento,2026-02-20 13:52:49,2026-02-20 13:57:21,4min 32s,0s,,2.23 Km,61 kph,30 kph,
Detenido,2026-02-20 13:57:21,2026-02-20 13:58:21,1min 0s,0s,,"-36.421074, -71.954366",
Movimiento,2026-02-20 13:58:21,2026-02-20 14:02:23,4min 2s,0s,,1.05 Km,36 kph,26 kph,
Detenido,2026-02-20 14:02:23,2026-02-20 14:52:43,50min 20s,0s,,"-36.43011, -71.959591",
Movimiento,2026-02-20 14:52:43,2026-02-20 15:03:53,11min 10s,0s,,2.79 Km,48 kph,21 kph,
Detenido,2026-02-20 15:03:53,2026-02-20 15:04:54,1min 1s,0s,,"-36.412878, -71.951229",
Movimiento,2026-02-20 15:04:54,2026-02-20 15:05:24,30s,0s,,0.13 Km,38 kph,38 kph,
Detenido,2026-02-20 15:05:24,2026-02-20 15:17:34,12min 10s,0s,,"-36.414177, -71.953682",
Movimiento,2026-02-20 15:17:34,2026-02-20 15:23:31,5min 57s,0s,,2.2 Km,59 kph,25 kph,
Detenido,2026-02-20 15:23:31,2026-02-20 15:25:02,1min 31s,0s,,"-36.429102, -71.96579",
Movimiento,2026-02-20 15:25:02,2026-02-20 15:33:36,8min 34s,0s,,3.99 Km,89 kph,29 kph,
Detenido,2026-02-20 15:33:36,2026-02-20 15:44:12,10min 36s,0s,,"-36.428073, -71.936087",
Movimiento,2026-02-20 15:44:12,2026-02-20 15:44:42,30s,0s,,0.67 Km,54 kph,32 kph,
Detenido,2026-02-20 15:44:42,2026-02-20 15:58:20,13min 38s,0s,,"-36.42686, -71.943381",
Movimiento,2026-02-20 15:58:20,2026-02-20 15:58:50,30s,0s,,0.16 Km,8 kph,8 kph,
Detenido,2026-02-20 15:58:50,2026-02-20 16:13:27,14min 37s,0s,,"-36.426668, -71.94504",
Movimiento,2026-02-20 16:13:27,2026-02-20 16:13:57,30s,0s,,0.14 Km,26 kph,26 kph,
Detenido,2026-02-20 16:13:57,2026-02-20 16:14:58,1min 1s,0s,,"-36.426192, -71.948238",
Movimiento,2026-02-20 16:14:58,2026-02-20 16:15:28,30s,0s,,0.08 Km,16 kph,16 kph,
Detenido,2026-02-20 16:15:28,2026-02-20 16:17:29,2min 1s,0s,,"-36.425699, -71.950693",
Movimiento,2026-02-20 16:17:29,2026-02-20 16:18:29,1min 0s,30s,,0.25 Km,28 kph,20 kph,
Detenido,2026-02-20 16:18:29,2026-02-20 16:24:01,5min 32s,0s,,"-36.423406, -71.955932",
Movimiento,2026-02-20 16:24:01,2026-02-20 16:28:02,4min 1s,0s,,0.67 Km,38 kph,18 kph,
Detenido,2026-02-20 16:28:02,2026-02-20 16:57:30,29min 28s,27s,,"-36.429296, -71.959547",
Movimiento,2026-02-20 16:57:30,2026-02-20 16:59:04,1min 34s,0s,,0.33 Km,47 kph,27 kph,
Detenido,2026-02-20 16:59:04,2026-02-20 17:00:35,1min 31s,30s,,"-36.425422, -71.960656",
Movimiento,2026-02-20 17:00:35,2026-02-20 17:04:06,3min 31s,0s,,1.57 Km,55 kph,29 kph,
Detenido,2026-02-20 17:04:06,2026-02-20 17:13:08,9min 2s,8s,,"-36.41611, -71.949168",
Movimiento,2026-02-20 17:13:08,2026-02-20 17:17:39,4min 31s,1min 12s,,1.69 Km,48 kph,23 kph,
Detenido,2026-02-20 17:17:39,2026-02-20 17:21:11,3min 32s,0s,,"-36.426101, -71.959259",
Movimiento,2026-02-20 17:21:11,2026-02-20 17:21:42,31s,0s,,0.01 Km,8 kph,8 kph,
Detenido,2026-02-20 17:21:42,2026-02-20 17:25:44,4min 2s,0s,,"-36.428525, -71.960074",
Movimiento,2026-02-20 17:25:44,2026-02-20 17:26:14,30s,0s,,0.02 Km,6 kph,6 kph,
Detenido,2026-02-20 17:26:14,2026-02-20 17:35:51,9min 37s,0s,,"-36.428631, -71.960262",
Movimiento,2026-02-20 17:35:51,2026-02-20 17:36:21,30s,16s,,0.22 Km,20 kph,14 kph,
Detenido,2026-02-20 17:36:21,2026-02-20 21:00:06,3h 23min 45s,0s,,"-36.430123, -71.959609",
Movimiento,2026-02-20 21:00:06,2026-02-20 21:05:36,5min 30s,0s,,0.01 Km,9 kph,9 kph,
Detenido,2026-02-20 21:05:36,2026-02-21 08:44:17,11h 38min 41s,20s,,"-36.430086, -71.959621",
Movimiento,2026-02-21 08:44:17,2026-02-21 08:44:58,41s,0s,,0.02 Km,9 kph,9 kph,
Detenido,2026-02-21 08:44:58,2026-02-21 08:46:29,1min 31s,1min 18s,,"-36.429382, -71.958773",
Movimiento,2026-02-21 08:46:29,2026-02-21 08:48:59,2min 30s,0s,,1 Km,50 kph,39 kph,
Detenido,2026-02-21 08:48:59,2026-02-21 08:51:00,2min 1s,0s,,"-36.423003, -71.964475",
Movimiento,2026-02-21 08:51:00,2026-02-21 08:53:32,2min 32s,0s,,1.17 Km,34 kph,18 kph,
Detenido,2026-02-21 08:53:32,2026-02-21 09:06:39,13min 7s,0s,,"-36.42269, -71.976961",
Movimiento,2026-02-21 09:06:39,2026-02-21 09:08:10,1min 31s,0s,,0.53 Km,25 kph,16 kph,
Detenido,2026-02-21 09:08:10,2026-02-21 09:27:25,19min 15s,0s,,"-36.426793, -71.979049",
Movimiento,2026-02-21 09:27:25,2026-02-21 09:33:55,6min 30s,0s,,1.34 Km,36 kph,16 kph,
Detenido,2026-02-21 09:33:55,2026-02-21 09:51:11,17min 16s,16s,,"-36.422402, -71.969028",
Movimiento,2026-02-21 09:51:11,2026-02-21 09:56:28,5min 17s,0s,,2.03 Km,43 kph,19 kph,
Detenido,2026-02-21 09:56:28,2026-02-21 10:38:02,41min 34s,0s,,"-36.430089, -71.960779",
Movimiento,2026-02-21 10:38:02,2026-02-21 10:41:34,3min 32s,0s,,1.24 Km,33 kph,16 kph,
Detenido,2026-02-21 10:41:34,2026-02-21 10:43:05,1min 31s,0s,,"-36.425893, -71.949689",
Movimiento,2026-02-21 10:43:05,2026-02-21 10:46:36,3min 31s,30s,,2.54 Km,51 kph,33 kph,
Detenido,2026-02-21 10:46:36,2026-02-21 11:16:26,29min 50s,0s,,"-36.412449, -71.928488",
Movimiento,2026-02-21 11:16:26,2026-02-21 11:33:32,17min 6s,26s,,21.38 Km,117 kph,76 kph,
Detenido,2026-02-21 11:33:32,2026-02-21 11:37:51,4min 19s,0s,,"-36.337733, -71.780091",
Movimiento,2026-02-21 11:37:51,2026-02-21 11:37:55,4s,4s,,0.02 Km,9 kph,9 kph,
Detenido,2026-02-21 11:37:55,2026-02-21 11:52:08,14min 13s,0s,,"-36.337475, -71.779931",
Movimiento,2026-02-21 11:52:08,2026-02-21 11:56:41,4min 33s,0s,,3.63 Km,101 kph,62 kph,
Detenido,2026-02-21 11:56:41,2026-02-21 11:57:03,22s,0s,,"-36.36483, -71.771488",
Movimiento,2026-02-21 11:57:03,2026-02-21 12:14:50,17min 47s,0s,,13.91 Km,78 kph,42 kph,
Detenido,2026-02-21 12:14:50,2026-02-21 12:44:23,29min 33s,0s,,"-36.450738, -71.837399",
Movimiento,2026-02-21 12:44:23,2026-02-21 12:55:59,11min 36s,0s,,10.07 Km,84 kph,55 kph,
Detenido,2026-02-21 12:55:59,2026-02-21 13:00:31,4min 32s,0s,,"-36.428032, -71.936053",
Movimiento,2026-02-21 13:00:31,2026-02-21 13:02:02,1min 31s,1min 31s,,0.18 Km,52 kph,52 kph,
Detenido,2026-02-21 13:02:02,2026-02-21 13:04:03,2min 1s,0s,,"-36.426351, -71.947084",
Movimiento,2026-02-21 13:04:03,2026-02-21 13:05:04,1min 1s,0s,,0.01 Km,13 kph,13 kph,
Detenido,2026-02-21 13:05:04,2026-02-21 13:06:48,1min 44s,0s,,"-36.426076, -71.948316",
Movimiento,2026-02-21 13:06:48,2026-02-21 13:09:06,2min 18s,0s,,0.42 Km,35 kph,17 kph,
Detenido,2026-02-21 13:09:06,2026-02-21 13:31:26,22min 20s,0s,,"-36.42457, -71.949496",
Movimiento,2026-02-21 13:31:26,2026-02-21 13:32:48,1min 22s,0s,,0.3 Km,30 kph,23 kph,
Detenido,2026-02-21 13:32:48,2026-02-21 13:34:41,1min 53s,0s,,"-36.425217, -71.952482",
Movimiento,2026-02-21 13:34:41,2026-02-21 13:38:21,3min 40s,0s,,1 Km,31 kph,17 kph,
Detenido,2026-02-21 13:38:21,2026-02-21 13:42:32,4min 11s,0s,,"-36.430125, -71.959595",
Movimiento,2026-02-21 13:42:32,2026-02-21 13:47:04,4min 32s,30s,,0.83 Km,21 kph,13 kph,
Detenido,2026-02-21 13:47:04,2026-02-21 13:50:21,3min 17s,0s,,"-36.422201, -71.956361",
Movimiento,2026-02-21 13:50:21,2026-02-21 13:53:44,3min 23s,0s,,1.02 Km,46 kph,35 kph,
Detenido,2026-02-21 13:53:44,2026-02-21 13:54:52,1min 8s,0s,,"-36.414452, -71.956284",
Movimiento,2026-02-21 13:54:52,2026-02-21 14:01:18,6min 26s,0s,,1.29 Km,35 kph,18 kph,
Detenido,2026-02-21 14:01:18,2026-02-21 14:01:48,30s,0s,,"-36.426773, -71.962814",
Movimiento,2026-02-21 14:01:48,2026-02-21 14:03:19,1min 31s,0s,,0.3 Km,31 kph,29 kph,
Detenido,2026-02-21 14:03:19,2026-02-22 08:34:42,18h 31min 23s,0s,,"-36.430072, -71.960802",
Movimiento,2026-02-22 08:34:42,2026-02-22 08:42:47,8min 5s,0s,,3.5 Km,71 kph,33 kph,
Detenido,2026-02-22 08:42:47,2026-02-22 09:06:35,23min 48s,0s,,"-36.412435, -71.928516",
Movimiento,2026-02-22 09:06:35,2026-02-22 09:14:08,7min 33s,0s,,6.52 Km,76 kph,56 kph,
Detenido,2026-02-22 09:14:08,2026-02-22 09:27:31,13min 23s,0s,,"-36.403669, -71.871531",
Movimiento,2026-02-22 09:27:31,2026-02-22 09:28:52,1min 21s,0s,,0.35 Km,46 kph,14 kph,
Detenido,2026-02-22 09:28:52,2026-02-22 09:35:04,6min 12s,0s,,"-36.405189, -71.868429",
Movimiento,2026-02-22 09:35:04,2026-02-22 09:47:11,12min 7s,0s,,10.29 Km,78 kph,48 kph,
Detenido,2026-02-22 09:47:11,2026-02-22 10:07:39,20min 28s,0s,,"-36.426809, -71.94336",
Movimiento,2026-02-22 10:07:39,2026-02-22 10:10:41,3min 2s,0s,,1.05 Km,54 kph,40 kph,
Detenido,2026-02-22 10:10:41,2026-02-22 10:12:42,2min 1s,0s,,"-36.424747, -71.955395",
Movimiento,2026-02-22 10:12:42,2026-02-22 10:17:15,4min 33s,0s,,1.75 Km,35 kph,24 kph,
Detenido,2026-02-22 10:17:15,2026-02-22 10:27:56,10min 41s,20s,,"-36.422683, -71.976974",
Movimiento,2026-02-22 10:27:56,2026-02-22 10:29:57,2min 1s,1min 1s,,0.31 Km,39 kph,18 kph,
Detenido,2026-02-22 10:29:57,2026-02-22 10:39:09,9min 12s,0s,,"-36.426818, -71.979026",
Movimiento,2026-02-22 10:39:09,2026-02-22 10:44:58,5min 49s,10s,,2.78 Km,50 kph,22 kph,
Detenido,2026-02-22 10:44:58,2026-02-22 10:49:07,4min 9s,0s,,"-36.430171, -71.959612",
Movimiento,2026-02-22 10:49:07,2026-02-22 11:02:14,13min 7s,31s,,19.03 Km,118 kph,73 kph,
Detenido,2026-02-22 11:02:14,2026-02-22 11:13:48,11min 34s,0s,,"-36.546131, -72.090639",
Movimiento,2026-02-22 11:13:48,2026-02-22 11:35:28,21min 40s,1min 25s,,20.79 Km,114 kph,49 kph,
Detenido,2026-02-22 11:35:28,2026-02-22 11:36:28,1min 0s,0s,,"-36.415337, -71.968103",
Movimiento,2026-02-22 11:36:28,2026-02-22 11:38:30,2min 2s,0s,,0.68 Km,33 kph,16 kph,
Detenido,2026-02-22 11:38:30,2026-02-22 11:50:49,12min 19s,0s,,"-36.418838, -71.970726",
Movimiento,2026-02-22 11:50:49,2026-02-22 11:52:50,2min 1s,0s,,0.48 Km,41 kph,28 kph,
Detenido,2026-02-22 11:52:50,2026-02-22 11:53:17,27s,0s,,"-36.422924, -71.96486",
Movimiento,2026-02-22 11:53:17,2026-02-22 11:55:51,2min 34s,0s,,0.97 Km,51 kph,26 kph,
Detenido,2026-02-22 11:55:51,2026-02-22 12:06:24,10min 33s,0s,,"-36.428495, -71.960118",
Movimiento,2026-02-22 12:06:24,2026-02-22 12:07:41,1min 17s,0s,,0.06 Km,31 kph,31 kph,
Detenido,2026-02-22 12:07:41,2026-02-23 08:29:55,20h 22min 14s,0s,,"-36.430113, -71.959617",
Movimiento,2026-02-23 08:29:55,2026-02-23 08:30:56,1min 1s,0s,,0.13 Km,22 kph,17 kph,
Detenido,2026-02-23 08:30:56,2026-02-23 08:38:22,7min 26s,0s,,"-36.428684, -71.958518",
Movimiento,2026-02-23 08:38:22,2026-02-23 08:53:09,14min 47s,0s,,18.52 Km,109 kph,71 kph,
Detenido,2026-02-23 08:53:09,2026-02-23 09:11:50,18min 41s,0s,,"-36.546162, -72.090676",
Movimiento,2026-02-23 09:11:50,2026-02-23 09:40:15,28min 25s,0s,,28.25 Km,99 kph,60 kph,
Detenido,2026-02-23 09:40:15,2026-02-23 10:01:51,21min 36s,0s,,"-36.450778, -71.837393",
Movimiento,2026-02-23 10:01:51,2026-02-23 10:18:01,16min 10s,0s,,10.49 Km,76 kph,41 kph,
Detenido,2026-02-23 10:18:01,2026-02-23 10:36:34,18min 33s,0s,,"-36.405145, -71.868497",
Movimiento,2026-02-23 10:36:34,2026-02-23 10:38:12,1min 38s,0s,,0.24 Km,13 kph,12 kph,
Detenido,2026-02-23 10:38:12,2026-02-23 10:59:24,21min 12s,29s,,"-36.403616, -71.871549",
Movimiento,2026-02-23 10:59:24,2026-02-23 11:04:57,5min 33s,1min 1s,,4.77 Km,76 kph,60 kph,
Detenido,2026-02-23 11:04:57,2026-02-23 11:05:01,4s,4s,,"-36.412237, -71.910707",
Movimiento,2026-02-23 11:05:01,2026-02-23 11:05:27,26s,0s,,0.01 Km,7 kph,7 kph,
Detenido,2026-02-23 11:05:27,2026-02-23 11:08:59,3min 32s,0s,,"-36.412251, -71.910705",
Movimiento,2026-02-23 11:08:59,2026-02-23 11:13:02,4min 3s,0s,,1.78 Km,47 kph,34 kph,
Detenido,2026-02-23 11:13:02,2026-02-23 11:40:30,27min 28s,0s,,"-36.412628, -71.928468",
Movimiento,2026-02-23 11:40:30,2026-02-23 11:45:19,4min 49s,0s,,2.14 Km,73 kph,33 kph,
Detenido,2026-02-23 11:45:19,2026-02-23 11:45:41,22s,0s,,"-36.425827, -71.94852",
Movimiento,2026-02-23 11:45:41,2026-02-23 11:48:21,2min 40s,0s,,1.07 Km,49 kph,29 kph,
Detenido,2026-02-23 11:48:21,2026-02-23 11:49:33,1min 12s,0s,,"-36.42805, -71.93605",
Movimiento,2026-02-23 11:49:33,2026-02-23 11:49:51,18s,0s,,0.02 Km,11 kph,10 kph,
Detenido,2026-02-23 11:49:51,2026-02-23 12:00:28,10min 37s,0s,,"-36.428058, -71.936094",
Movimiento,2026-02-23 12:00:28,2026-02-23 12:07:29,7min 1s,0s,,1.82 Km,66 kph,22 kph,
Detenido,2026-02-23 12:07:29,2026-02-23 12:08:30,1min 1s,31s,,"-36.41897, -71.952065",
Movimiento,2026-02-23 12:08:30,2026-02-23 12:13:02,4min 32s,0s,,1.58 Km,36 kph,23 kph,
Detenido,2026-02-23 12:13:02,2026-02-23 12:38:04,25min 2s,0s,,"-36.418882, -71.970696",
Movimiento,2026-02-23 12:38:04,2026-02-23 12:40:47,2min 43s,0s,,0.77 Km,36 kph,25 kph,
Detenido,2026-02-23 12:40:47,2026-02-23 12:42:16,1min 29s,0s,,"-36.422422, -71.969039",
Movimiento,2026-02-23 12:42:16,2026-02-23 12:42:49,33s,31s,,0.01 Km,17 kph,12 kph,
Detenido,2026-02-23 12:42:49,2026-02-23 13:01:26,18min 37s,0s,,"-36.422382, -71.9688",
Movimiento,2026-02-23 13:01:26,2026-02-23 13:06:53,5min 27s,0s,,2.53 Km,61 kph,21 kph,
Detenido,2026-02-23 13:06:53,2026-02-23 14:08:17,1h 1min 24s,0s,,"-36.430131, -71.959591",
Movimiento,2026-02-23 14:08:17,2026-02-23 14:11:12,2min 55s,0s,,1.15 Km,47 kph,22 kph,
Detenido,2026-02-23 14:11:12,2026-02-23 14:13:13,2min 1s,0s,,"-36.425766, -71.950486",
Movimiento,2026-02-23 14:13:13,2026-02-23 14:15:45,2min 32s,0s,,0.79 Km,70 kph,52 kph,
Detenido,2026-02-23 14:15:45,2026-02-23 14:18:41,2min 56s,3s,,"-36.428085, -71.936098",
Movimiento,2026-02-23 14:18:41,2026-02-23 14:19:17,36s,0s,,0.02 Km,9 kph,9 kph,
Detenido,2026-02-23 14:19:17,2026-02-23 14:22:18,3min 1s,0s,,"-36.428034, -71.936053",
Movimiento,2026-02-23 14:22:18,2026-02-23 14:25:50,3min 32s,0s,,1.5 Km,69 kph,28 kph,
Detenido,2026-02-23 14:25:50,2026-02-23 14:33:22,7min 32s,0s,,"-36.424607, -71.949484",
Movimiento,2026-02-23 14:33:22,2026-02-23 14:35:26,2min 4s,0s,,0.33 Km,38 kph,29 kph,
Detenido,2026-02-23 14:35:26,2026-02-23 14:36:29,1min 3s,0s,,"-36.421969, -71.95613",
Movimiento,2026-02-23 14:36:29,2026-02-23 14:40:28,3min 59s,0s,,1.08 Km,20 kph,14 kph,
Detenido,2026-02-23 14:40:28,2026-02-23 14:48:02,7min 34s,0s,,"-36.422416, -71.969055",
Movimiento,2026-02-23 14:48:02,2026-02-23 14:52:02,4min 0s,0s,,1.13 Km,40 kph,20 kph,
Detenido,2026-02-23 14:52:02,2026-02-23 14:58:06,6min 4s,47s,,"-36.426808, -71.979044",
Movimiento,2026-02-23 14:58:06,2026-02-23 15:04:39,6min 33s,0s,,2.69 Km,47 kph,26 kph,
Detenido,2026-02-23 15:04:39,2026-02-23 16:36:42,1h 32min 3s,0s,,"-36.430152, -71.96078",
Movimiento,2026-02-23 16:36:42,2026-02-23 16:45:14,8min 32s,0s,,2.91 Km,52 kph,29 kph,
Detenido,2026-02-23 16:45:14,2026-02-23 16:59:54,14min 40s,0s,,"-36.426847, -71.979075",
Movimiento,2026-02-23 16:59:54,2026-02-23 17:08:13,8min 19s,0s,,2.6 Km,47 kph,26 kph,
Detenido,2026-02-23 17:08:13,2026-02-24 08:27:40,15h 19min 27s,0s,,"-36.430174, -71.959679",
Movimiento,2026-02-24 08:27:40,2026-02-24 08:30:37,2min 57s,0s,,0.23 Km,25 kph,14 kph,
Detenido,2026-02-24 08:30:37,2026-02-24 08:32:21,1min 44s,0s,,"-36.431979, -71.951577",
Movimiento,2026-02-24 08:32:21,2026-02-24 08:36:40,4min 19s,0s,,4.46 Km,113 kph,68 kph,
Detenido,2026-02-24 08:36:40,2026-02-24 08:51:40,15min 0s,0s,,"-36.452355, -71.988274",
Movimiento,2026-02-24 08:51:40,2026-02-24 08:53:21,1min 41s,0s,,0.01 Km,6 kph,6 kph,
Detenido,2026-02-24 08:53:21,2026-02-24 08:56:39,3min 18s,0s,,"-36.452387, -71.988306",
Movimiento,2026-02-24 08:56:39,2026-02-24 09:08:27,11min 48s,0s,,7.03 Km,64 kph,33 kph,
Detenido,2026-02-24 09:08:27,2026-02-24 09:50:50,42min 23s,0s,,"-36.426878, -71.943408",
Movimiento,2026-02-24 09:50:50,2026-02-24 09:54:52,4min 2s,0s,,1.83 Km,77 kph,45 kph,
Detenido,2026-02-24 09:54:52,2026-02-24 09:55:53,1min 1s,0s,,"-36.412414, -71.92855",
Movimiento,2026-02-24 09:55:53,2026-02-24 09:56:53,1min 0s,0s,,0 Km,6 kph,6 kph,
Detenido,2026-02-24 09:56:53,2026-02-24 11:09:00,1h 12min 7s,1min 21s,,"-36.412663, -71.92848",
Movimiento,2026-02-24 11:09:00,2026-02-24 11:15:33,6min 33s,0s,,5.03 Km,89 kph,67 kph,
Detenido,2026-02-24 11:15:33,2026-02-24 11:33:13,17min 40s,0s,,"-36.403638, -71.871522",
Movimiento,2026-02-24 11:33:13,2026-02-24 11:52:53,19min 40s,0s,,17.55 Km,99 kph,60 kph,
Detenido,2026-02-24 11:52:53,2026-02-24 12:24:40,31min 47s,0s,,"-36.325424, -71.785855",
Movimiento,2026-02-24 12:24:40,2026-02-24 12:49:22,24min 42s,0s,,23.15 Km,110 kph,49 kph,
Detenido,2026-02-24 12:49:22,2026-02-24 12:49:52,30s,0s,,"-36.426264, -71.959364",
Movimiento,2026-02-24 12:49:52,2026-02-24 12:50:22,30s,0s,,0.14 Km,26 kph,26 kph,
Detenido,2026-02-24 12:50:22,2026-02-24 14:18:18,1h 27min 56s,32s,,"-36.428801, -71.960191",
Movimiento,2026-02-24 14:18:18,2026-02-24 14:19:49,1min 31s,0s,,0 Km,9 kph,9 kph,
Detenido,2026-02-24 14:19:49,2026-02-24 14:21:16,1min 27s,0s,,"-36.430115, -71.959626",
Movimiento,2026-02-24 14:21:16,2026-02-24 14:24:21,3min 5s,0s,,0.85 Km,44 kph,17 kph,
Detenido,2026-02-24 14:24:21,2026-02-24 14:26:22,2min 1s,0s,,"-36.425719, -71.963898",
Movimiento,2026-02-24 14:26:22,2026-02-24 14:28:31,2min 9s,0s,,0.97 Km,46 kph,24 kph,
Detenido,2026-02-24 14:28:31,2026-02-24 14:30:52,2min 21s,3s,,"-36.418843, -71.970661",
Movimiento,2026-02-24 14:30:52,2026-02-24 14:31:03,11s,0s,,0.01 Km,6 kph,6 kph,
Detenido,2026-02-24 14:31:03,2026-02-24 14:46:11,15min 8s,0s,,"-36.418891, -71.970666",
Movimiento,2026-02-24 14:46:11,2026-02-24 14:50:13,4min 2s,0s,,1.52 Km,51 kph,24 kph,
Detenido,2026-02-24 14:50:13,2026-02-24 15:06:51,16min 38s,0s,,"-36.422663, -71.977105",
Movimiento,2026-02-24 15:06:51,2026-02-24 15:13:23,6min 32s,0s,,2.75 Km,42 kph,29 kph,
Detenido,2026-02-24 15:13:23,2026-02-24 15:26:59,13min 36s,0s,,"-36.430129, -71.959675",
Movimiento,2026-02-24 15:26:59,2026-02-24 15:30:01,3min 2s,23s,,1.23 Km,36 kph,24 kph,
Detenido,2026-02-24 15:30:01,2026-02-24 15:32:02,2min 1s,0s,,"-36.426043, -71.949118",
Movimiento,2026-02-24 15:32:02,2026-02-24 15:34:03,2min 1s,0s,,0.87 Km,45 kph,44 kph,
Detenido,2026-02-24 15:34:03,2026-02-24 15:37:36,3min 33s,1min 1s,,"-36.428125, -71.936141",
Movimiento,2026-02-24 15:37:36,2026-02-24 15:40:07,2min 31s,0s,,1.11 Km,43 kph,31 kph,
Detenido,2026-02-24 15:40:07,2026-02-24 15:42:08,2min 1s,0s,,"-36.426182, -71.9481",
Movimiento,2026-02-24 15:42:08,2026-02-24 15:45:40,3min 32s,0s,,0.89 Km,35 kph,20 kph,
Detenido,2026-02-24 15:45:40,2026-02-24 15:46:40,1min 0s,0s,,"-36.424263, -71.958486",
Movimiento,2026-02-24 15:46:40,2026-02-24 15:47:41,1min 1s,0s,,0.06 Km,36 kph,36 kph,
Detenido,2026-02-24 15:47:41,2026-02-24 15:48:03,22s,0s,,"-36.423036, -71.964496",
Movimiento,2026-02-24 15:48:03,2026-02-24 15:49:42,1min 39s,0s,,0.64 Km,32 kph,22 kph,
Detenido,2026-02-24 15:49:42,2026-02-24 15:51:42,2min 0s,0s,,"-36.422493, -71.969097",
Movimiento,2026-02-24 15:51:42,2026-02-24 16:00:18,8min 36s,1min 26s,,2.02 Km,36 kph,18 kph,
Detenido,2026-02-24 16:00:18,2026-02-24 16:00:21,3s,3s,,"-36.43025, -71.959873",
Movimiento,2026-02-24 16:00:21,2026-02-24 16:00:48,27s,0s,,0.01 Km,7 kph,7 kph,
Detenido,2026-02-24 16:00:48,2026-02-24 16:43:23,42min 35s,30s,,"-36.43019, -71.959678",
Movimiento,2026-02-24 16:43:23,2026-02-24 16:46:25,3min 2s,0s,,0.74 Km,30 kph,17 kph,
Detenido,2026-02-24 16:46:25,2026-02-24 16:48:56,2min 31s,1min 1s,,"-36.434405, -71.961959",
Movimiento,2026-02-24 16:48:56,2026-02-24 16:52:58,4min 2s,0s,,1.83 Km,48 kph,32 kph,
Detenido,2026-02-24 16:52:58,2026-02-24 17:08:34,15min 36s,0s,,"-36.42686, -71.979031",
Movimiento,2026-02-24 17:08:34,2026-02-24 17:11:05,2min 31s,0s,,0.65 Km,35 kph,27 kph,
Detenido,2026-02-24 17:11:05,2026-02-24 17:14:07,3min 2s,0s,,"-36.426248, -71.968109",
Movimiento,2026-02-24 17:14:07,2026-02-24 17:18:39,4min 32s,0s,,1.85 Km,52 kph,27 kph,
Detenido,2026-02-24 17:18:39,2026-02-24 17:21:41,3min 2s,1min 1s,,"-36.430167, -71.959613",
Movimiento,2026-02-24 17:21:41,2026-02-24 17:22:42,1min 1s,0s,,0.02 Km,7 kph,7 kph,
Detenido,2026-02-24 17:22:42,2026-02-24 17:50:55,28min 13s,0s,,"-36.429338, -71.959532",
Movimiento,2026-02-24 17:50:55,2026-02-24 17:53:24,2min 29s,0s,,0.43 Km,27 kph,16 kph,
Detenido,2026-02-24 17:53:24,2026-02-25 08:25:19,14h 31min 55s,1min 41s,,"-36.427721, -71.959911",
Movimiento,2026-02-25 08:25:19,2026-02-25 08:52:19,27min 0s,30s,,20.22 Km,87 kph,44 kph,
Detenido,2026-02-25 08:52:19,2026-02-25 08:54:08,1min 49s,1min 49s,,"-36.329212, -72.056107",
Movimiento,2026-02-25 08:54:08,2026-02-25 08:55:20,1min 12s,0s,,0.74 Km,37 kph,22 kph,
Detenido,2026-02-25 08:55:20,2026-02-25 08:56:51,1min 31s,0s,,"-36.328422, -72.059327",
Movimiento,2026-02-25 08:56:51,2026-02-25 08:58:52,2min 1s,0s,,0.39 Km,23 kph,14 kph,
Detenido,2026-02-25 08:58:52,2026-02-25 08:59:53,1min 1s,0s,,"-36.326391, -72.056603",
Movimiento,2026-02-25 08:59:53,2026-02-25 09:00:23,30s,0s,,0.03 Km,21 kph,21 kph,
Detenido,2026-02-25 09:00:23,2026-02-25 09:03:11,2min 48s,0s,,"-36.326399, -72.054572",
Movimiento,2026-02-25 09:03:11,2026-02-25 09:03:55,44s,4s,,0.26 Km,27 kph,18 kph,
Detenido,2026-02-25 09:03:55,2026-02-25 09:40:27,36min 32s,0s,,"-36.323999, -72.050644",
Movimiento,2026-02-25 09:40:27,2026-02-25 09:44:29,4min 2s,0s,,0.46 Km,18 kph,13 kph,
Detenido,2026-02-25 09:44:29,2026-02-25 09:47:30,3min 1s,0s,,"-36.326404, -72.05459",
Movimiento,2026-02-25 09:47:30,2026-02-25 09:56:04,8min 34s,0s,,5.87 Km,96 kph,40 kph,
Detenido,2026-02-25 09:56:04,2026-02-25 09:58:36,2min 32s,29s,,"-36.331539, -71.999166",
Movimiento,2026-02-25 09:58:36,2026-02-25 10:17:18,18min 42s,0s,,12.44 Km,92 kph,43 kph,
Detenido,2026-02-25 10:17:18,2026-02-25 10:19:19,2min 1s,0s,,"-36.373265, -71.904658",
Movimiento,2026-02-25 10:19:19,2026-02-25 10:33:58,14min 39s,0s,,14.81 Km,114 kph,55 kph,
Detenido,2026-02-25 10:33:58,2026-02-25 10:44:05,10min 7s,0s,,"-36.325436, -71.785851",
Movimiento,2026-02-25 10:44:05,2026-02-25 10:46:03,1min 58s,0s,,0.05 Km,10 kph,7 kph,
Detenido,2026-02-25 10:46:03,2026-02-25 10:49:02,2min 59s,28s,,"-36.325377, -71.78587",
Movimiento,2026-02-25 10:49:02,2026-02-25 10:49:35,33s,0s,,0.08 Km,14 kph,14 kph,
Detenido,2026-02-25 10:49:35,2026-02-25 10:55:19,5min 44s,0s,,"-36.32542, -71.785877",
Movimiento,2026-02-25 10:55:19,2026-02-25 11:15:01,19min 42s,0s,,17.57 Km,103 kph,57 kph,
Detenido,2026-02-25 11:15:01,2026-02-25 11:42:18,27min 17s,1min 10s,,"-36.403638, -71.871579",
Movimiento,2026-02-25 11:42:18,2026-02-25 11:49:23,7min 5s,0s,,6.54 Km,95 kph,59 kph,
Detenido,2026-02-25 11:49:23,2026-02-25 11:51:24,2min 1s,0s,,"-36.41253, -71.927601",
Movimiento,2026-02-25 11:51:24,2026-02-25 11:51:54,30s,0s,,0.08 Km,6 kph,6 kph,
Detenido,2026-02-25 11:51:54,2026-02-25 12:57:55,1h 6min 1s,0s,,"-36.412692, -71.928564",
Movimiento,2026-02-25 12:57:55,2026-02-25 12:58:07,12s,12s,,0 Km,10 kph,10 kph,
Detenido,2026-02-25 12:58:07,2026-02-25 12:59:37,1min 30s,1min 30s,,"-36.412428, -71.928514",
Movimiento,2026-02-25 12:59:37,2026-02-25 13:07:11,7min 34s,0s,,3.37 Km,60 kph,35 kph,
Detenido,2026-02-25 13:07:11,2026-02-25 13:08:29,1min 18s,0s,,"-36.42732, -71.959681",
Movimiento,2026-02-25 13:08:29,2026-02-25 13:09:12,43s,0s,,0.1 Km,15 kph,11 kph,
Detenido,2026-02-25 13:09:12,2026-02-25 14:41:58,1h 32min 46s,0s,,"-36.430081, -71.959696",
Movimiento,2026-02-25 14:41:58,2026-02-25 14:42:28,30s,0s,,0.14 Km,34 kph,34 kph,
Detenido,2026-02-25 14:42:28,2026-02-25 14:50:30,8min 2s,0s,,"-36.431238, -71.955068",
Movimiento,2026-02-25 14:50:30,2026-02-25 14:52:34,2min 4s,0s,,0.55 Km,39 kph,27 kph,
Detenido,2026-02-25 14:52:34,2026-02-25 14:53:35,1min 1s,0s,,"-36.425883, -71.949741",
Movimiento,2026-02-25 14:53:35,2026-02-25 14:59:38,6min 3s,1min 31s,,2.87 Km,87 kph,27 kph,
Detenido,2026-02-25 14:59:38,2026-02-25 16:15:40,1h 16min 2s,0s,,"-36.412593, -71.928594",
Movimiento,2026-02-25 16:15:40,2026-02-25 16:21:06,5min 26s,1min 1s,,2.02 Km,51 kph,24 kph,
Detenido,2026-02-25 16:21:06,2026-02-25 16:21:36,30s,30s,,"-36.417141, -71.95465",
Movimiento,2026-02-25 16:21:36,2026-02-25 16:28:40,7min 4s,0s,,2.75 Km,56 kph,31 kph,
Detenido,2026-02-25 16:28:40,2026-02-25 16:40:16,11min 36s,0s,,"-36.422685, -71.977052",
Movimiento,2026-02-25 16:40:16,2026-02-25 16:47:20,7min 4s,1min 32s,,2.59 Km,43 kph,26 kph,
Detenido,2026-02-25 16:47:20,2026-02-26 08:49:47,16h 2min 27s,0s,,"-36.430162, -71.959684",
Movimiento,2026-02-26 08:49:47,2026-02-26 09:10:48,21min 1s,0s,,13.73 Km,99 kph,42 kph,
Detenido,2026-02-26 09:10:48,2026-02-26 09:12:19,1min 31s,0s,,"-36.354427, -72.045306",
Movimiento,2026-02-26 09:12:19,2026-02-26 09:12:49,30s,0s,,0.13 Km,20 kph,20 kph,
Detenido,2026-02-26 09:12:49,2026-02-26 09:30:37,17min 48s,0s,,"-36.353218, -72.044679",
Movimiento,2026-02-26 09:30:37,2026-02-26 09:45:15,14min 38s,0s,,11.12 Km,93 kph,45 kph,
Detenido,2026-02-26 09:45:15,2026-02-26 09:46:46,1min 31s,0s,,"-36.329825, -72.060573",
Movimiento,2026-02-26 09:46:46,2026-02-26 09:47:47,1min 1s,0s,,0.91 Km,47 kph,28 kph,
Detenido,2026-02-26 09:47:47,2026-02-26 09:51:49,4min 2s,21s,,"-36.336478, -72.066855",
Movimiento,2026-02-26 09:51:49,2026-02-26 09:55:52,4min 3s,3min 32s,,0.12 Km,9 kph,8 kph,
Detenido,2026-02-26 09:55:52,2026-02-26 09:56:52,1min 0s,6s,,"-36.341, -72.068762",
Movimiento,2026-02-26 09:56:52,2026-02-26 09:57:22,30s,0s,,0.07 Km,10 kph,10 kph,
Detenido,2026-02-26 09:57:22,2026-02-26 10:45:18,47min 56s,11s,,"-36.340947, -72.06973",
Movimiento,2026-02-26 10:45:18,2026-02-26 10:48:53,3min 35s,0s,,0.14 Km,11 kph,10 kph,
Detenido,2026-02-26 10:48:53,2026-02-26 10:49:23,30s,0s,,"-36.340178, -72.06841",
Movimiento,2026-02-26 10:49:23,2026-02-26 10:50:23,1min 0s,0s,,0.15 Km,12 kph,12 kph,
Detenido,2026-02-26 10:50:23,2026-02-26 10:51:50,1min 27s,0s,,"-36.3384, -72.067808",
Movimiento,2026-02-26 10:51:50,2026-02-26 10:55:56,4min 6s,0s,,0.28 Km,25 kph,14 kph,
Detenido,2026-02-26 10:55:56,2026-02-26 10:59:28,3min 32s,0s,,"-36.329917, -72.060686",
Movimiento,2026-02-26 10:59:28,2026-02-26 11:17:06,17min 38s,0s,,15.24 Km,98 kph,65 kph,
Detenido,2026-02-26 11:17:06,2026-02-26 11:19:07,2min 1s,1min 31s,,"-36.417758, -71.958293",
Movimiento,2026-02-26 11:19:07,2026-02-26 11:24:40,5min 33s,0s,,2.41 Km,53 kph,35 kph,
Detenido,2026-02-26 11:24:40,2026-02-26 12:52:30,1h 27min 50s,3s,,"-36.412711, -71.928595",
Movimiento,2026-02-26 12:52:30,2026-02-26 12:58:14,5min 44s,1min 16s,,2.4 Km,69 kph,36 kph,
Detenido,2026-02-26 12:58:14,2026-02-26 12:58:45,31s,31s,,"-36.420981, -71.954318",
Movimiento,2026-02-26 12:58:45,2026-02-26 12:59:15,30s,30s,,0.18 Km,34 kph,34 kph,
Detenido,2026-02-26 12:59:15,2026-02-26 13:00:46,1min 31s,1min 31s,,"-36.424373, -71.955442",
Movimiento,2026-02-26 13:00:46,2026-02-26 13:03:17,2min 31s,0s,,0.84 Km,40 kph,24 kph,
Detenido,2026-02-26 13:03:17,2026-02-26 13:45:44,42min 27s,0s,,"-36.430136, -71.95961",
Movimiento,2026-02-26 13:45:44,2026-02-26 13:50:08,4min 24s,1min 0s,,0.95 Km,36 kph,21 kph,
Detenido,2026-02-26 13:50:08,2026-02-26 13:51:51,1min 43s,1min 43s,,"-36.433049, -71.967983",
Movimiento,2026-02-26 13:51:51,2026-02-26 13:55:10,3min 19s,0s,,1.09 Km,41 kph,36 kph,
Detenido,2026-02-26 13:55:10,2026-02-26 14:04:42,9min 32s,0s,,"-36.422707, -71.976984",
Movimiento,2026-02-26 14:04:42,2026-02-26 14:05:02,20s,19s,,0.51 Km,21 kph,18 kph,
Detenido,2026-02-26 14:05:02,2026-02-26 14:06:45,1min 43s,1min 43s,,"-36.425341, -71.972098",
Movimiento,2026-02-26 14:06:45,2026-02-26 14:10:17,3min 32s,1min 1s,,1.73 Km,38 kph,30 kph,
Detenido,2026-02-26 14:10:17,2026-02-26 14:30:40,20min 23s,0s,,"-36.430162, -71.959622",
Movimiento,2026-02-26 14:30:40,2026-02-26 14:32:28,1min 48s,0s,,0.96 Km,31 kph,18 kph,
Detenido,2026-02-26 14:32:28,2026-02-26 14:35:32,3min 4s,0s,,"-36.425933, -71.94939",
Movimiento,2026-02-26 14:35:32,2026-02-26 14:40:01,4min 29s,1min 27s,,2.74 Km,63 kph,43 kph,
Detenido,2026-02-26 14:40:01,2026-02-26 15:00:24,20min 23s,0s,,"-36.449952, -71.957212",
Movimiento,2026-02-26 15:00:24,2026-02-26 15:02:42,2min 18s,0s,,0.27 Km,26 kph,17 kph,
Detenido,2026-02-26 15:02:42,2026-02-26 15:03:12,30s,7s,,"-36.449965, -71.954968",
Movimiento,2026-02-26 15:03:12,2026-02-26 15:07:14,4min 2s,1min 31s,,2 Km,78 kph,42 kph,
Detenido,2026-02-26 15:07:14,2026-02-26 15:08:09,55s,0s,,"-36.434511, -71.962078",
Movimiento,2026-02-26 15:08:09,2026-02-26 15:10:27,2min 18s,12s,,0.68 Km,38 kph,28 kph,
Detenido,2026-02-26 15:10:27,2026-02-26 15:16:18,5min 51s,0s,,"-36.430242, -71.959934",
Movimiento,2026-02-26 15:16:18,2026-02-26 15:22:21,6min 3s,0s,,1.61 Km,45 kph,23 kph,
Detenido,2026-02-26 15:22:21,2026-02-26 15:22:49,28s,0s,,"-36.416898, -71.962712",
Movimiento,2026-02-26 15:22:49,2026-02-26 15:34:28,11min 39s,0s,,6.28 Km,79 kph,28 kph,
Detenido,2026-02-26 15:34:28,2026-02-26 15:36:59,2min 31s,0s,,"-36.452408, -71.988277",
Movimiento,2026-02-26 15:36:59,2026-02-26 15:40:01,3min 2s,0s,,0.27 Km,15 kph,10 kph,
Detenido,2026-02-26 15:40:01,2026-02-26 15:49:36,9min 35s,0s,,"-36.454245, -71.988295",
Movimiento,2026-02-26 15:49:36,2026-02-26 15:55:39,6min 3s,0s,,3.57 Km,67 kph,30 kph,
Detenido,2026-02-26 15:55:39,2026-02-26 15:55:53,14s,0s,,"-36.427706, -71.960032",
Movimiento,2026-02-26 15:55:53,2026-02-26 15:56:47,54s,0s,,0.13 Km,14 kph,11 kph,
Detenido,2026-02-26 15:56:47,2026-02-26 15:59:08,2min 21s,13s,,"-36.428678, -71.960301",
Movimiento,2026-02-26 15:59:08,2026-02-26 16:00:43,1min 35s,0s,,0.23 Km,14 kph,11 kph,
Detenido,2026-02-26 16:00:43,2026-02-26 16:28:11,27min 28s,0s,,"-36.430129, -71.959628",
Movimiento,2026-02-26 16:28:11,2026-02-26 16:31:15,3min 4s,0s,,0.3 Km,17 kph,12 kph,
Detenido,2026-02-26 16:31:15,2026-02-26 17:12:59,41min 44s,0s,,"-36.429411, -71.959529",
Movimiento,2026-02-26 17:12:59,2026-02-26 17:14:58,1min 59s,0s,,0.25 Km,29 kph,11 kph,
Detenido,2026-02-26 17:14:58,2026-02-27 08:53:29,15h 38min 31s,0s,,"-36.430139, -71.959635",
Movimiento,2026-02-27 08:53:29,2026-02-27 09:01:33,8min 4s,0s,,4.25 Km,67 kph,34 kph,
Detenido,2026-02-27 09:01:33,2026-02-27 09:07:33,6min 0s,0s,,"-36.412681, -71.928466",
Movimiento,2026-02-27 09:07:33,2026-02-27 09:13:04,5min 31s,0s,,2.59 Km,50 kph,30 kph,
Detenido,2026-02-27 09:13:04,2026-02-27 09:14:29,1min 25s,0s,,"-36.42094, -71.954375",
Movimiento,2026-02-27 09:14:29,2026-02-27 09:19:07,4min 38s,0s,,1.31 Km,24 kph,18 kph,
Detenido,2026-02-27 09:19:07,2026-02-27 10:08:20,49min 13s,0s,,"-36.430106, -71.959655",
Movimiento,2026-02-27 10:08:20,2026-02-27 10:16:51,8min 31s,0s,,3.34 Km,44 kph,21 kph,
Detenido,2026-02-27 10:16:51,2026-02-27 10:29:56,13min 5s,0s,,"-36.422654, -71.977158",
Movimiento,2026-02-27 10:29:56,2026-02-27 10:31:27,1min 31s,0s,,0.44 Km,17 kph,12 kph,
Detenido,2026-02-27 10:31:27,2026-02-27 10:36:17,4min 50s,18s,,"-36.426763, -71.979072",
Movimiento,2026-02-27 10:36:17,2026-02-27 10:39:01,2min 44s,0s,,0.96 Km,36 kph,26 kph,
Detenido,2026-02-27 10:39:01,2026-02-27 10:40:32,1min 31s,0s,,"-36.426304, -71.967445",
Movimiento,2026-02-27 10:40:32,2026-02-27 10:45:34,5min 2s,0s,,1.82 Km,35 kph,18 kph,
Detenido,2026-02-27 10:45:34,2026-02-27 11:46:10,1h 36s,0s,,"-36.430035, -71.959714",
Movimiento,2026-02-27 11:46:10,2026-02-27 11:49:24,3min 14s,0s,,1.19 Km,31 kph,20 kph,
Detenido,2026-02-27 11:49:24,2026-02-27 11:50:57,1min 33s,0s,,"-36.425938, -71.949355",
Movimiento,2026-02-27 11:50:57,2026-02-27 12:00:59,10min 2s,0s,,9.3 Km,112 kph,66 kph,
Detenido,2026-02-27 12:00:59,2026-02-27 12:09:34,8min 35s,0s,,"-36.403629, -71.871573",
Movimiento,2026-02-27 12:09:34,2026-02-27 12:17:09,7min 35s,0s,,5.66 Km,75 kph,61 kph,
Detenido,2026-02-27 12:17:09,2026-02-27 12:26:45,9min 36s,0s,,"-36.412803, -71.926126",
Movimiento,2026-02-27 12:26:45,2026-02-27 12:29:45,3min 0s,0s,,1.9 Km,61 kph,60 kph,
Detenido,2026-02-27 12:29:45,2026-02-27 12:30:15,30s,0s,,"-36.425726, -71.948503",
Movimiento,2026-02-27 12:30:15,2026-02-27 12:31:46,1min 31s,0s,,0.41 Km,64 kph,38 kph,
Detenido,2026-02-27 12:31:46,2026-02-27 13:02:29,30min 43s,0s,,"-36.42682, -71.94337",
Movimiento,2026-02-27 13:02:29,2026-02-27 13:11:03,8min 34s,0s,,2.4 Km,39 kph,22 kph,
Detenido,2026-02-27 13:11:03,2026-02-27 13:22:29,11min 26s,0s,,"-36.417558, -71.965493",
Movimiento,2026-02-27 13:22:29,2026-02-27 13:24:09,1min 40s,0s,,0.4 Km,38 kph,21 kph,
Detenido,2026-02-27 13:24:09,2026-02-27 13:39:28,15min 19s,0s,,"-36.418855, -71.970668",
Movimiento,2026-02-27 13:39:28,2026-02-27 13:46:22,6min 54s,0s,,1.52 Km,51 kph,28 kph,
Detenido,2026-02-27 13:46:22,2026-02-27 15:20:30,1h 34min 8s,0s,,"-36.430151, -71.959602",
Movimiento,2026-02-27 15:20:30,2026-02-27 15:28:34,8min 4s,0s,,2.01 Km,48 kph,32 kph,
Detenido,2026-02-27 15:28:34,2026-02-27 15:29:32,58s,0s,,"-36.418852, -71.970686",
Movimiento,2026-02-27 15:29:32,2026-02-27 15:44:39,15min 7s,1min 1s,,5.94 Km,73 kph,31 kph,
Detenido,2026-02-27 15:44:39,2026-02-27 15:45:08,29s,29s,,"-36.450093, -71.95518",
Movimiento,2026-02-27 15:45:08,2026-02-27 15:46:39,1min 31s,0s,,0.02 Km,8 kph,8 kph,
Detenido,2026-02-27 15:46:39,2026-02-27 15:49:40,3min 1s,2min 1s,,"-36.450082, -71.955509",
Movimiento,2026-02-27 15:49:40,2026-02-27 15:52:11,2min 31s,0s,,0.48 Km,13 kph,10 kph,
Detenido,2026-02-27 15:52:11,2026-02-27 16:18:59,26min 48s,0s,,"-36.449866, -71.961034",
Movimiento,2026-02-27 16:18:59,2026-02-27 16:26:34,7min 35s,2min 2s,,2.62 Km,66 kph,29 kph,
Detenido,2026-02-27 16:26:34,2026-02-27 16:31:06,4min 32s,0s,,"-36.427457, -71.94886",
Movimiento,2026-02-27 16:31:06,2026-02-27 16:50:56,19min 50s,0s,,22.28 Km,102 kph,69 kph,
Detenido,2026-02-27 16:50:56,2026-02-27 17:27:37,36min 41s,0s,,"-36.325456, -71.785887",
Movimiento,2026-02-27 17:27:37,2026-02-27 17:38:36,10min 59s,0s,,6.52 Km,47 kph,34 kph,
Detenido,2026-02-27 17:38:36,2026-02-27 17:46:40,8min 4s,0s,,"-36.325801, -71.835887",
Movimiento,2026-02-27 17:46:40,2026-02-27 18:05:21,18min 41s,0s,,21.16 Km,112 kph,62 kph,
Detenido,2026-02-27 18:05:21,2026-02-27 18:09:54,4min 33s,32s,,"-36.452409, -71.988258",
Movimiento,2026-02-27 18:09:54,2026-02-27 18:13:56,4min 2s,0s,,1.62 Km,36 kph,22 kph,
Detenido,2026-02-27 18:13:56,2026-02-27 18:26:03,12min 7s,0s,,"-36.447822, -71.977987",
Movimiento,2026-02-27 18:26:03,2026-02-27 18:28:04,2min 1s,1min 1s,,0.86 Km,35 kph,32 kph,
Detenido,2026-02-27 18:28:04,2026-02-27 18:32:36,4min 32s,0s,,"-36.439584, -71.971656",
Movimiento,2026-02-27 18:32:36,2026-02-27 18:37:38,5min 2s,30s,,1.61 Km,28 kph,21 kph,
Detenido,2026-02-27 18:37:38,2026-02-28 08:27:39,13h 50min 1s,0s,,"-36.430155, -71.959769",
Movimiento,2026-02-28 08:27:39,2026-02-28 08:29:11,1min 32s,0s,,0.01 Km,12 kph,10 kph,
Detenido,2026-02-28 08:29:11,2026-02-28 08:29:41,30s,0s,,"-36.428081, -71.958371",
Movimiento,2026-02-28 08:29:41,2026-02-28 08:33:43,4min 2s,0s,,0.78 Km,31 kph,16 kph,
Detenido,2026-02-28 08:33:43,2026-02-28 08:42:47,9min 4s,0s,,"-36.423231, -71.956353",
Movimiento,2026-02-28 08:42:47,2026-02-28 09:05:00,22min 13s,0s,,18.46 Km,101 kph,51 kph,
Detenido,2026-02-28 09:05:00,2026-02-28 09:05:30,30s,13s,,"-36.326429, -72.056515",
Movimiento,2026-02-28 09:05:30,2026-02-28 09:06:01,31s,0s,,0.04 Km,11 kph,11 kph,
Detenido,2026-02-28 09:06:01,2026-02-28 09:09:02,3min 1s,0s,,"-36.326405, -72.054622",
Movimiento,2026-02-28 09:09:02,2026-02-28 09:09:32,30s,0s,,0.02 Km,12 kph,12 kph,
Detenido,2026-02-28 09:09:32,2026-02-28 09:15:06,5min 34s,0s,,"-36.324769, -72.051782",
Movimiento,2026-02-28 09:15:06,2026-02-28 09:15:36,30s,0s,,0.01 Km,9 kph,8 kph,
Detenido,2026-02-28 09:15:36,2026-02-28 09:30:15,14min 39s,0s,,"-36.323918, -72.050637",
Movimiento,2026-02-28 09:30:15,2026-02-28 09:32:46,2min 31s,0s,,0.28 Km,14 kph,11 kph,
Detenido,2026-02-28 09:32:46,2026-02-28 09:34:17,1min 31s,0s,,"-36.326386, -72.054503",
Movimiento,2026-02-28 09:34:17,2026-02-28 09:34:47,30s,0s,,0.08 Km,22 kph,22 kph,
Detenido,2026-02-28 09:34:47,2026-02-28 09:36:18,1min 31s,0s,,"-36.326454, -72.056519",
Movimiento,2026-02-28 09:36:18,2026-02-28 10:09:06,32min 48s,0s,,34.43 Km,112 kph,59 kph,
Detenido,2026-02-28 10:09:06,2026-02-28 10:38:25,29min 19s,0s,,"-36.325408, -71.785896",
Movimiento,2026-02-28 10:38:25,2026-02-28 11:03:06,24min 41s,0s,,22.5 Km,94 kph,54 kph,
Detenido,2026-02-28 11:03:06,2026-02-28 11:05:30,2min 24s,0s,,"-36.474396, -71.709366",
Movimiento,2026-02-28 11:05:30,2026-02-28 11:06:08,38s,0s,,0.06 Km,13 kph,9 kph,
Detenido,2026-02-28 11:06:08,2026-02-28 11:31:22,25min 14s,0s,,"-36.474347, -71.70937",
Movimiento,2026-02-28 11:31:22,2026-02-28 11:50:33,19min 11s,0s,,21.73 Km,98 kph,70 kph,
Detenido,2026-02-28 11:50:33,2026-02-28 12:06:40,16min 7s,0s,,"-36.426834, -71.943326",
Movimiento,2026-02-28 12:06:40,2026-02-28 12:08:10,1min 30s,0s,,0.24 Km,28 kph,25 kph,
Detenido,2026-02-28 12:08:10,2026-02-28 12:11:12,3min 2s,0s,,"-36.426417, -71.946614",
Movimiento,2026-02-28 12:11:12,2026-02-28 12:12:43,1min 31s,0s,,1.2 Km,78 kph,42 kph,
Detenido,2026-02-28 12:12:43,2026-02-28 12:18:46,6min 3s,0s,,"-36.415614, -71.94494",
Movimiento,2026-02-28 12:18:46,2026-02-28 12:20:48,2min 2s,0s,,1.39 Km,51 kph,47 kph,
Detenido,2026-02-28 12:20:48,2026-02-28 13:35:52,1h 15min 4s,0s,,"-36.41263, -71.928487",
Movimiento,2026-02-28 13:35:52,2026-02-28 13:43:25,7min 33s,19s,,3.55 Km,47 kph,31 kph,
Detenido,2026-02-28 13:43:25,2026-02-28 14:05:01,21min 36s,0s,,"-36.417466, -71.965463",
Movimiento,2026-02-28 14:05:01,2026-02-28 14:11:11,6min 10s,0s,,1.83 Km,47 kph,21 kph,
Detenido,2026-02-28 14:11:11,2026-02-28 17:13:25,3h 2min 14s,0s,,"-36.43017, -71.959634",
Movimiento,2026-02-28 17:13:25,2026-02-28 17:15:24,1min 59s,1min 18s,,0.15 Km,11 kph,10 kph,
Detenido,2026-02-28 17:15:24,2026-02-28 19:13:20,1h 57min 56s,0s,,"-36.429287, -71.95943",
Movimiento,2026-02-28 19:13:20,2026-02-28 19:15:21,2min 1s,0s,,0.45 Km,14 kph,10 kph,
Detenido,2026-02-28 19:15:21,2026-02-28 19:18:29,3min 8s,0s,,"-36.428523, -71.960074",
Movimiento,2026-02-28 19:18:29,2026-02-28 19:19:29,1min 0s,23s,,0.17 Km,16 kph,14 kph,
Detenido,2026-02-28 19:19:29,2026-03-01 09:05:14,13h 45min 45s,0s,,"-36.43014, -71.959637",
Movimiento,2026-03-01 09:05:14,2026-03-01 09:18:52,13min 38s,0s,,12.23 Km,94 kph,43 kph,
Detenido,2026-03-01 09:18:52,2026-03-01 09:51:24,32min 32s,0s,,"-36.4379, -71.830419",
Movimiento,2026-03-01 09:51:24,2026-03-01 10:02:29,11min 5s,0s,,6.49 Km,81 kph,44 kph,
Detenido,2026-03-01 10:02:29,2026-03-01 10:03:20,51s,0s,,"-36.405169, -71.868487",
Movimiento,2026-03-01 10:03:20,2026-03-01 10:31:43,28min 23s,0s,,25.03 Km,113 kph,57 kph,
Detenido,2026-03-01 10:31:43,2026-03-01 10:49:22,17min 39s,0s,,"-36.325392, -71.785908",
Movimiento,2026-03-01 10:49:22,2026-03-01 11:07:33,18min 11s,0s,,17.89 Km,114 kph,58 kph,
Detenido,2026-03-01 11:07:33,2026-03-01 11:12:37,5min 4s,1min 1s,,"-36.360193, -71.930796",
Movimiento,2026-03-01 11:12:37,2026-03-01 11:31:46,19min 9s,0s,,15.95 Km,88 kph,43 kph,
Detenido,2026-03-01 11:31:46,2026-03-01 11:33:10,1min 24s,0s,,"-36.326394, -72.054625",
Movimiento,2026-03-01 11:33:10,2026-03-01 11:34:17,1min 7s,0s,,0.11 Km,15 kph,15 kph,
Detenido,2026-03-01 11:34:17,2026-03-01 11:34:29,12s,0s,,"-36.325052, -72.05322",
Movimiento,2026-03-01 11:34:29,2026-03-01 11:37:19,2min 50s,1min 4s,,0.14 Km,11 kph,9 kph,
Detenido,2026-03-01 11:37:19,2026-03-01 11:39:19,2min 0s,0s,,"-36.324057, -72.050634",
Movimiento,2026-03-01 11:39:19,2026-03-01 11:39:24,5s,5s,,0.01 Km,8 kph,8 kph,
Detenido,2026-03-01 11:39:24,2026-03-01 11:49:24,10min 0s,0s,,"-36.323996, -72.050657",
Movimiento,2026-03-01 11:49:24,2026-03-01 11:51:25,2min 1s,53s,,0.14 Km,10 kph,8 kph,
Detenido,2026-03-01 11:51:25,2026-03-01 11:53:40,2min 15s,0s,,"-36.325202, -72.053258",
Movimiento,2026-03-01 11:53:40,2026-03-01 12:11:35,17min 55s,0s,,16.83 Km,86 kph,56 kph,
Detenido,2026-03-01 12:11:35,2026-03-01 12:12:35,1min 0s,0s,,"-36.417584, -71.9655",
Movimiento,2026-03-01 12:12:35,2026-03-01 12:13:36,1min 1s,0s,,0.01 Km,8 kph,8 kph,
Detenido,2026-03-01 12:13:36,2026-03-01 12:27:14,13min 38s,0s,,"-36.417657, -71.965481",
Movimiento,2026-03-01 12:27:14,2026-03-01 12:34:18,7min 4s,0s,,2.12 Km,31 kph,15 kph,
Detenido,2026-03-01 12:34:18,2026-03-01 12:36:19,2min 1s,0s,,"-36.415561, -71.944685",
Movimiento,2026-03-01 12:36:19,2026-03-01 12:38:20,2min 1s,0s,,0.07 Km,31 kph,21 kph,
Detenido,2026-03-01 12:38:20,2026-03-01 12:38:58,38s,0s,,"-36.412429, -71.928547",
Movimiento,2026-03-01 12:38:58,2026-03-01 12:41:52,2min 54s,0s,,0.04 Km,8 kph,8 kph,
Detenido,2026-03-01 12:41:52,2026-03-01 13:21:08,39min 16s,0s,,"-36.412591, -71.928577",
Movimiento,2026-03-01 13:21:08,2026-03-01 13:29:43,8min 35s,12s,,6 Km,86 kph,50 kph,
Detenido,2026-03-01 13:29:43,2026-03-01 13:43:51,14min 8s,0s,,"-36.44979, -71.961153",
Movimiento,2026-03-01 13:43:51,2026-03-01 13:51:25,7min 34s,0s,,4.38 Km,66 kph,33 kph,
Detenido,2026-03-01 13:51:25,2026-03-02 08:27:48,18h 36min 23s,1min 0s,,"-36.430179, -71.959659",
Movimiento,2026-03-02 08:27:48,2026-03-02 08:33:52,6min 4s,0s,,2.05 Km,61 kph,33 kph,
Detenido,2026-03-02 08:33:52,2026-03-02 08:55:04,21min 12s,0s,,"-36.417595, -71.965437",
Movimiento,2026-03-02 08:55:04,2026-03-02 08:55:13,9s,0s,,0.01 Km,10 kph,10 kph,
Detenido,2026-03-02 08:55:13,2026-03-02 08:59:17,4min 4s,2s,,"-36.417546, -71.965466",
Movimiento,2026-03-02 08:59:17,2026-03-02 09:18:24,19min 7s,0s,,16.81 Km,101 kph,52 kph,
Detenido,2026-03-02 09:18:24,2026-03-02 09:21:33,3min 9s,0s,,"-36.326434, -72.054642",
Movimiento,2026-03-02 09:21:33,2026-03-02 09:21:57,24s,0s,,0.07 Km,14 kph,12 kph,
Detenido,2026-03-02 09:21:57,2026-03-02 09:24:17,2min 20s,0s,,"-36.324788, -72.051785",
Movimiento,2026-03-02 09:24:17,2026-03-02 09:25:29,1min 12s,0s,,0.02 Km,10 kph,7 kph,
Detenido,2026-03-02 09:25:29,2026-03-02 09:35:36,10min 7s,0s,,"-36.324125, -72.050712",
Movimiento,2026-03-02 09:35:36,2026-03-02 09:36:06,30s,0s,,0.03 Km,12 kph,12 kph,
Detenido,2026-03-02 09:36:06,2026-03-02 09:38:19,2min 13s,0s,,"-36.324709, -72.051695",
Movimiento,2026-03-02 09:38:19,2026-03-02 09:39:38,1min 19s,0s,,0.08 Km,28 kph,17 kph,
Detenido,2026-03-02 09:39:38,2026-03-02 09:43:06,3min 28s,0s,,"-36.326389, -72.054516",
Movimiento,2026-03-02 09:43:06,2026-03-02 10:18:12,35min 6s,2s,,34.71 Km,115 kph,53 kph,
Detenido,2026-03-02 10:18:12,2026-03-02 10:34:39,16min 27s,16s,,"-36.325252, -71.786003",
Movimiento,2026-03-02 10:34:39,2026-03-02 10:55:22,20min 43s,0s,,21.62 Km,116 kph,55 kph,
Detenido,2026-03-02 10:55:22,2026-03-02 10:57:53,2min 31s,0s,,"-36.415569, -71.9447",
Movimiento,2026-03-02 10:57:53,2026-03-02 11:00:55,3min 2s,0s,,1.51 Km,63 kph,33 kph,
Detenido,2026-03-02 11:00:55,2026-03-02 12:27:28,1h 26min 33s,30s,,"-36.412622, -71.928449",
Movimiento,2026-03-02 12:27:28,2026-03-02 12:29:29,2min 1s,0s,,2.51 Km,60 kph,48 kph,
Detenido,2026-03-02 12:29:29,2026-03-02 12:31:01,1min 32s,0s,,"-36.425868, -71.948533",
Movimiento,2026-03-02 12:31:01,2026-03-02 12:34:03,3min 2s,0s,,0.64 Km,26 kph,12 kph,
Detenido,2026-03-02 12:34:03,2026-03-02 12:48:10,14min 7s,0s,,"-36.426811, -71.943351",
Movimiento,2026-03-02 12:48:10,2026-03-02 12:56:14,8min 4s,1min 30s,,1.88 Km,41 kph,22 kph,
Detenido,2026-03-02 12:56:14,2026-03-02 15:04:31,2h 8min 17s,1min 0s,,"-36.430124, -71.959794",
Movimiento,2026-03-02 15:04:31,2026-03-02 15:04:44,13s,10s,,0.03 Km,13 kph,10 kph,
Detenido,2026-03-02 15:04:44,2026-03-02 15:05:51,1min 7s,1min 7s,,"-36.429226, -71.959189",
Movimiento,2026-03-02 15:05:51,2026-03-02 15:06:45,54s,0s,,0.01 Km,8 kph,8 kph,
Detenido,2026-03-02 15:06:45,2026-03-02 15:14:27,7min 42s,0s,,"-36.429275, -71.959526",
Movimiento,2026-03-02 15:14:27,2026-03-02 15:14:48,21s,0s,,0 Km,6 kph,6 kph,
Detenido,2026-03-02 15:14:48,2026-03-02 16:16:17,1h 1min 29s,1min 55s,,"-36.429323, -71.959622",
Movimiento,2026-03-02 16:16:17,2026-03-02 16:17:13,56s,19s,,0.28 Km,33 kph,16 kph,
Detenido,2026-03-02 16:17:13,2026-03-02 16:26:58,9min 45s,0s,,"-36.428568, -71.960256",
Movimiento,2026-03-02 16:26:58,2026-03-02 16:29:19,2min 21s,0s,,0.17 Km,25 kph,16 kph,
Detenido,2026-03-02 16:29:19,2026-03-03 08:17:10,15h 47min 51s,0s,,"-36.430145, -71.959681",
Movimiento,2026-03-03 08:17:10,2026-03-03 08:19:41,2min 31s,0s,,0.64 Km,31 kph,22 kph,
Detenido,2026-03-03 08:19:41,2026-03-03 08:21:11,1min 30s,0s,,"-36.424462, -71.957127",
Movimiento,2026-03-03 08:21:11,2026-03-03 08:42:22,21min 11s,0s,,18.39 Km,97 kph,56 kph,
Detenido,2026-03-03 08:42:22,2026-03-03 09:02:05,19min 43s,0s,,"-36.324003, -72.05061",
Movimiento,2026-03-03 09:02:05,2026-03-03 09:20:42,18min 37s,0s,,17 Km,94 kph,60 kph,
Detenido,2026-03-03 09:20:42,2026-03-03 10:14:50,54min 8s,0s,,"-36.417592, -71.965504",
Movimiento,2026-03-03 10:14:50,2026-03-03 10:21:54,7min 4s,0s,,2.58 Km,37 kph,23 kph,
Detenido,2026-03-03 10:21:54,2026-03-03 10:24:55,3min 1s,0s,,"-36.415394, -71.944613",
Movimiento,2026-03-03 10:24:55,2026-03-03 10:28:27,3min 32s,1min 0s,,1.47 Km,43 kph,34 kph,
Detenido,2026-03-03 10:28:27,2026-03-03 10:32:36,4min 9s,0s,,"-36.412604, -71.928588",
Movimiento,2026-03-03 10:32:36,2026-03-03 10:33:30,54s,0s,,0 Km,7 kph,7 kph,
Detenido,2026-03-03
</file>

<file name="presentacion-marp-dt-hodom-hsc---46967a2b-5bd4-4845-9783-3c784596dd36.md" mime="text/markdown">
---
marp: true
theme: default
paginate: true
backgroundColor: #fff
style: |
 section {
 font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
 font-size: 22px;
 padding: 40px 50px;
 }
 h1 { color: #1a5276; font-size: 32px; margin-bottom: 10px; }
 h2 { color: #2471a3; font-size: 26px; margin-bottom: 8px; }
 table { font-size: 17px; width: 100%; }
 th { background-color: #1a5276; color: white; padding: 6px 10px; }
 td { padding: 4px 10px; }
 blockquote { border-left: 4px solid #2471a3; padding: 8px 16px; background: #eaf2f8; font-size: 20px; }
 ul { margin: 4px 0; }
 li { margin: 2px 0; }
 .small { font-size: 15px; }
 .highlight { background: #fdebd0; padding: 12px; border-radius: 6px; border-left: 4px solid #e67e22; }
---

<!-- _paginate: false -->

# HODOM HSC
## Estado actual · Oportunidades · Hoja de ruta

**Dirección Técnica · Hospital de San Carlos**
**Marzo 2026**

---

# Agenda

1. Resultados acumulados de la unidad
2. Contexto hospitalario
3. Perfil de pacientes
4. Estado actual: fortalezas y brechas
5. Hallazgos operacionales (telemetría)
6. Componente médico: análisis L-V
7. Capacidad recuperable
8. Tres horizontes de desarrollo
9. Prioridades inmediatas
10. Capa operativa digital

---

# Resultados acumulados 2023-2025

| | 2023 | 2024 | 2025 | **Total** |
|---|:---:|:---:|:---:|:---:|
| Personas atendidas | 307 | 1.077 | 751 | **2.135** |
| Días persona | 4.037 | 6.508 | 5.480 | **16.025** |
| Visitas domiciliarias | 5.148 | 11.562 | 9.428 | **26.138** |
| Fallecidos no esperados | 0 | 0 | 0 | **0** |
| Reingresos (%) | 16 (5,2%) | 28 (3,3%) | 28 (4,7%) | 72 |

<div class="small">

*2025 sin trabajadora social en el período.*

</div>

---

# Contexto hospitalario

## Oportunidad de hospitalización ≤12h adulto

| 2019 | 2022 | 2023 | 2024 | 2025 |
|:---:|:---:|:---:|:---:|:---:|
| 96,8% | 69,5% | 61,0% | 54,9% | **40,6%** |

## Índice ocupacional 2025

| Medicina | Cirugía | Traumatología | Área quirúrgica |
|:---:|:---:|:---:|:---:|
| **97,5** | **96,0** | **97,9** | **98,1** |

Hospital de 130 camas · Red norte Ñuble · 10 comunas

---

# Perfil de pacientes HODOM

| Variable | Valor |
|---|---|
| Edad promedio | **70,1 años** |
| ≥ 80 años | **35%** |
| FONASA A+B | **87,6%** |
| Mujeres | 54,4% |

**Diagnósticos frecuentes:** ITU (12,2%) · Neumonía (11,0%) · ACV (3,5%)

**Origen:** Medicina 42,7% · Urgencia 32,0% · Traumatología 9,4%

**Prestaciones core:** tratamiento EV (~45%) · kinesiología (~40%) · curaciones (~10%)

---

# Estado actual

## Fortalezas operativas
- Equipo multidisciplinario con experiencia de terreno
- Cartera clínica operativa con resultados demostrables
- Derivación funcional desde los 4 servicios principales
- Enlace piloto con APS / Programa Postrados

## Brechas identificadas
- Protocolo PRO-002 diseñado para campaña, no para unidad permanente
- Registros dispersos (papel + Excel + Drive)
- Sin sistema de información compartido
- Gobernanza clínica no formalizada
- Capacidad operativa con margen de optimización relevante

---

# Telemetría: la operación real

**3 fuentes cruzadas · 83 días · Ene–Mar 2026**

| Indicador | Valor |
|---|---|
| Match programación ↔ GPS | **87,0%** |
| Jornada formal | 08:00 – 20:00 (12h) |
| Ventana operativa real | ~08:30 – 17:30 (9h) |
| Jornada sin operación de ruta | **~2,5 h/día** |
| % productivo sobre 12h | **39,2%** |
| Visitas/día/móvil | 8,1 |
| Capacidad ociosa trimestre | **1.818 horas** |

---

# Telemetría: distribución del tiempo

## Sobre jornada formal de 12 horas

| Componente | % |
|---|---|
| En base (coordinación, registros, almuerzo) | 25,2% |
| En terreno (atención) | 23,1% |
| En movimiento (traslado) | 16,1% |
| **Jornada no operada** | **35,6%** |

## Perfil horario

| Franja | Actividad |
|---|---|
| 09:00–12:00 | Bloque AM — mejor rendimiento (69-73%) |
| 12:00–14:00 | Valle — retorno a base + almuerzo (23%) |
| 14:00–17:30 | Bloque PM activo (64-73%) |
| 17:30–20:00 | Sin operación de ruta (~0%) |

---

# Flota vehicular

| | PFFF57 | RGHB14 | SUV TZXS94 |
|---|:---:|:---:|:---:|
| Límite km/día | 100 | 100 | 80 |
| Disponibilidad | L-D | L-D | **L-V** |
| Km/día real | 73,9 | 81,2 | 63,2 |
| % uso km | 73,9% | 81,2% | 79,0% |
| Visitas/día | 9,3 | 8,8 | 5,6 |
| % tiempo en base | 36,0% | 38,3% | 42,0% |

- Fin de semana: solo 2 móviles (sin SUV)
- Velocidades >100 kph detectadas en rutas rurales

---

# Componente médico: análisis L-V

**Los médicos trabajan L-V (~59 días/trimestre), el resto del equipo en cuarto turno (83 días)**

| Parámetro | Valor |
|---|---|
| Dotación médica | 1 JC + 1 MJ = 1,5 FTE |
| Atenciones con componente médico | ~305-365 en el trimestre |
| **Atenciones/día laborable/FTE** | **3,5 – 4,1** |

## Comparación

| Escenario | Atenciones/día/FTE |
|---|---|
| Actual | 3,5 – 4,1 |
| Con regulación clínica + telecontrol | **6 – 8** |
| Capacidad recuperable | **+70-95%** |

---

# Capacidad recuperable sin recursos adicionales

| Acción | Visitas extra/día |
|---|:---:|
| Activar bloque 17:30-19:30 (visitas urbanas) | **+6-8** |
| Almuerzo escalonado + registros en terreno | **+3** |
| Salida protocolizada ≤08:00 | **+1** |
| Asignación territorial por macrozonas | **+1-2** |
| **Total L-V (3 móviles)** | **+12-16** |

<div class="highlight">

De ~24 a ~36-40 visitas/día (+50-67%). La holgura principal es de **tiempo**, no de km.

</div>

---

# Tres horizontes

## H1 — Mejor rendimiento con lo que tenemos
Regulación clínica · Optimización de tiempos y rutas · Registro digital mínimo · Reactivar O₂ (3 concentradores) y sueroterapia · Telecontrol

## H2 — Cumplimiento normativo y consolidación
DS 1/2022 + NT HD 2024 · Protocolos mínimos · Registros auditables · Indicadores · Seguridad del paciente · Gobernanza

## H3 — Máxima expresión del potencial
Tecnología · Automatización · Digitalización completa · Gestión del conocimiento · Capacitación continua · Calidad e innovación

---

# Prioridades inmediatas (H1)

| Acción | Propósito |
|---|---|
| Briefing diario | Alinear el día, revisar casos |
| Regulación clínica | Ingreso-seguimiento-alta con criterio compartido |
| Registro digital mínimo | Una captura simple desde el celular |
| Escalamiento clínico | Semáforo + NEWS2 |
| Evaluación domicilio/cuidador | Formulario estandarizado |
| O₂ domiciliario | 3 concentradores disponibles |

> Criterio rector: toda herramienta debe reducir carga cognitiva, no aumentarla.

---

# Capa operativa digital

| Módulo | Función |
|---|---|
| Panel general | Censo, cupos, alertas, móviles, pendientes |
| Registro móvil | Formulario breve por disciplina, desde celular |
| Regulación clínica | Ingresos, alertas, egresos, rescates, decisiones |
| Georreferenciación | Mapa de pacientes, macrozonas, rutas |
| Alta/contrarreferencia | Resumen, indicaciones, continuidad APS |
| Telecontrol | Voz/video/chat, sin app, link único |

Mobile-first · Simple · Imprimible · Sin duplicar trabajo

---

# Forma de implementación

| Principio | |
|---|---|
| Avance por capas | Sin cambios masivos de una vez |
| Lo útil primero | Priorizar lo que resuelve problemas reales |
| Formalización justa | Sin burocracia innecesaria |
| Resultados tempranos | Visibles en semanas, no en meses |
| Retroalimentación | Ajustar con el equipo, no contra el equipo |

## Hoja de ruta

| Semana | Foco |
|---|---|
| 1 | Panel + registro móvil + regulación + briefing |
| 2 | Ingreso/evaluación + alta + escalamiento + georef |
| 3 | Indicadores + recursos + personal |
| 4 | Telecontrol + ajustes + cierre primera iteración |

---

# Qué sigue

- Instalación de briefing y regulación clínica desde esta semana
- Primeros prototipos web accesibles por celular
- Cierre de brechas normativas prioritarias
- Reactivación de capacidades clínicas subutilizadas
- Retroalimentación continua del equipo

---

<!-- _paginate: false -->

# HODOM HSC
## Consolidar · Cerrar brechas · Proyectar

**Dirección Técnica · Hospital de San Carlos · 2026**
</file>

<file name="guion-presentacion-dt-hodom-hsc---8eb903eb-ae93-40ba-8f79-b48b638d1b13.md" mime="text/markdown">
# Guión — Primera reunión equipo HODOM HSC
## Director Técnico · Hospital de San Carlos
### 25-30 min exposición + 20-30 min conversación

---

## SLIDE 1 — Portada
**1 min**

Bienvenida breve. Explicar que la reunión tiene dos partes: una lectura del estado actual con datos y una conversación con el equipo.

---

## SLIDE 2 — Agenda
**30 seg**

Recorrer los 10 puntos brevemente. Señalar que al final habrá espacio de conversación.

---

## SLIDE 3 — Resultados acumulados
**2 min**

Ir directo a los números. Más de 2.100 personas atendidas, 26 mil visitas, cero fallecidos no esperados. Reingresos entre 3,3% y 5,2% según año.

Si preguntan por 2025: baja respecto a 2024 asociada a período sin trabajadora social.

---

## SLIDE 4 — Contexto hospitalario
**2 min**

Mostrar la serie de oportunidad de hospitalización: de 96,8% a 40,6% en 6 años. El hospital está operando sobre el 96% de ocupación en los servicios más grandes.

130 camas, centro de referencia de la red norte. HODOM funciona como extensión de la capacidad hospitalaria.

---

## SLIDE 5 — Perfil de pacientes
**1-2 min**

Edad promedio 70 años, 35% sobre 80. Población predominantemente FONASA A/B. Los diagnósticos dominantes son infecciones (ITU, neumonía) y ACV. Llegan desde medicina y urgencia principalmente. El procedimiento core es tratamiento EV.

---

## SLIDE 6 — Estado actual
**2-3 min**

Reconocer fortalezas: equipo con experiencia, cartera operativa, derivación desde los 4 servicios principales, enlace con APS en marcha.

Nombrar brechas como hechos: protocolo diseñado para campaña y no para unidad permanente, registros en múltiples soportes sin integración, sin sistema de información compartido, gobernanza clínica pendiente de formalizar, capacidad operativa con margen.

No es juicio. Es la lectura del punto de partida.

---

## SLIDE 7 — Telemetría: la operación real
**3 min**

Explicar las fuentes: GPS de los 3 vehículos, planillas de programación, consolidado de atenciones. 83 días analizados.

Match de 87% entre lo programado y lo ejecutado. Dato positivo.

Dato clave: la jornada formal es de 12 horas, pero la operación real de ruta se concentra en 9. Las 2,5 horas finales (17:30 a 20:00) no generan visitas detectables. Eso suma 1.818 horas de capacidad vehicular sin usar en un trimestre.

---

## SLIDE 8 — Distribución del tiempo
**2 min**

Sobre 12 horas de jornada formal: 25% en base, 23% en terreno, 16% en movimiento, 35% sin operación. El bloque AM (9-12) es el de mejor rendimiento. El valle de almuerzo cae a 23%. Después de las 17:30 no hay actividad de ruta.

---

## SLIDE 9 — Flota
**1-2 min**

Los 3 vehículos usan entre 74% y 81% de su límite kilométrico. Ahí el margen es limitado. Pero en tiempo hay espacio importante.

Fin de semana: solo 2 móviles. Las visitas rurales lejanas deben concentrarse en días con 3 vehículos.

Mencionar el dato de velocidad: se detectan trayectos frecuentes sobre 100 kph en rutas rurales. Tema de seguridad a abordar.

---

## SLIDE 10 — Componente médico
**2-3 min**

A diferencia del equipo que trabaja en cuarto turno los 7 días, los médicos trabajan de lunes a viernes. Eso son ~59 días laborables en el trimestre.

Con 1,5 FTE médico, el rendimiento actual está en torno a 3,5-4,1 atenciones por día por FTE. Con regulación clínica activa y telecontrol, ese número podría subir a 6-8.

Presentarlo como oportunidad de rediseño del componente médico: no solo visita presencial, sino también regulación, seguimiento remoto y apoyo oportuno al equipo de terreno.

---

## SLIDE 11 — Capacidad recuperable
**2 min**

Ir directo a la tabla: activar bloque tardío, escalonar almuerzo, adelantar salida, mejorar asignación territorial. Total: +12-16 visitas/día sin recursos adicionales.

Pasar de ~24 a ~36-40 visitas/día. La holgura es de tiempo, no de km. Las visitas adicionales del bloque tardío deben ser urbanas.

---

## SLIDE 12 — Tres horizontes
**2 min**

H1: optimizar con lo que ya tenemos. H2: consolidación normativa. H3: máxima expresión con tecnología, IA, capacitación, calidad.

No es un solo salto. Es una secuencia.

---

## SLIDE 13 — Prioridades inmediatas
**2 min**

6 acciones que arrancan esta semana: briefing, regulación clínica, registro digital, escalamiento, evaluación domiciliaria, reactivación de O₂.

Todo con criterio de baja carga cognitiva.

---

## SLIDE 14 — Capa operativa digital
**2-3 min**

6 módulos: panel, registro, regulación, georreferenciación, alta/contrarreferencia, telecontrol.

Si hay prototipos disponibles, mostrarlos aquí.

Todo mobile-first, simple, imprimible cuando se necesite.

---

## SLIDE 15 — Forma de implementación
**1-2 min**

Avance por capas. Lo útil primero. Formalización justa. Resultados tempranos. Retroalimentación del equipo.

Hoja de ruta en 4 semanas para la primera iteración.

---

## SLIDE 16 — Qué sigue
**1 min**

Resumen de acciones inmediatas. Transición a la conversación.

---

## SLIDE 17 — Cierre
**30 seg**

Slide de cierre. Abrir conversación.

---

## Conversación con el equipo
**20-30 min**

Preguntas orientadoras:
1. ¿Qué brecha del día a día sienten más pesada?
2. ¿Qué de lo actual funciona bien y no debería cambiar?
3. ¿Qué mejora concreta tendría más impacto inmediato?

Técnica: anotar lo que digan de forma visible. Si hay silencio, ir a la pregunta 1 directamente. Si alguien se extiende, anotar y pasar. Si hay crítica, acoger sin defensividad.

---

## Preguntas probables

**"¿Vamos a tener más trabajo?"**
→ El objetivo es ordenar lo que ya se hace, no agregar carga. Algunas cosas van a cambiar, pero la dirección es reducir fricción.

**"¿Qué pasa si no hay recursos nuevos?"**
→ Hay una primera capa que se puede mover con lo que existe: orden, protocolo, indicadores, optimización operativa.

**"¿La tecnología va a complicarnos?"**
→ Si complica, está mal diseñada. Tiene que resolver problemas reales del equipo, no crear nuevos.

**"¿Esto es para fiscalizarnos?"**
→ Una unidad que puede mostrar lo que hace y con qué resultados se protege a sí misma. Eso beneficia a todos.

---

## Datos de respaldo rápido

| Dato | Valor |
|---|---|
| Hospital | 130 camas, red norte Ñuble |
| Población objetivo | 67.034 > 18 años |
| Territorio | San Carlos, San Fabián, San Nicolás, Ñiquén |
| Radio operativo | 20 km |
| BIP | 40059567-0 |
| RRHH anual | $344.518.110 |
| Cupos | 20-25 |
| Estada referencial | 7 días |
| Proyección | ~900 pac/año |
| Móviles | 3 |
| Concentradores O₂ | 3 (disponibles) |

---

*Guión de trabajo · Director Técnico HODOM HSC · Marzo 2026*
</file>

<file name="consolidado-estrategico-dt-hodom-hsc-2026-03-25---55e82d09-83b0-47da-87ac-00664fe43da3.md" mime="text/markdown">
# Consolidado estratégico — Dirección Técnica HODOM HSC
## Fecha: 2026-03-25
## Propósito
Documento de consolidación sistemática de todo lo trabajado hasta este momento para la primera reunión de equipo del nuevo Director Técnico HODOM HSC y para la hoja de ruta inmediata de rediseño, regulación, cumplimiento y prototipado operativo.

---

# 1. Contexto y objetivo de uso

Este documento consolida en una sola pieza:
- el diagnóstico actual de la unidad HODOM HSC
- los hallazgos normativos y operativos críticos
- la propuesta narrativa y estratégica para la primera reunión de equipo
- la estructura de horizontes de desarrollo acordada
- el enfoque de implementación respetuoso, progresivo y de baja carga cognitiva
- las prioridades inmediatas de cierre de brechas
- los prototipos web que pueden mostrarse en el corto plazo
- la incorporación del rol dual del usuario como **Director Técnico + médico regulador**

Este documento debe servir como:
1. base para la presentación al equipo
2. recordatorio durable de decisiones ya trabajadas
3. hoja de ruta para iteraciones rápidas con el equipo de desarrollo
4. referencia para próximos turnos de trabajo del agente

---

# 2. Fuentes revisadas e integradas

## 2.1 Documentos y análisis ya consolidados del proyecto HODOM HSC
- `output/hodom-hsc/presentacion-dt-hodom-hsc.md`
- `output/hodom-hsc/checklist-normativo-hodom-hsc.md`
- `output/hodom-hsc/propuesta-hodom-hsc-ideal.md`
- `output/hodom-hsc/specs-sistema-web-hodom-hsc.md`
- `output/hodom-hsc/inventario-e-insights-hodom-hsc.md`
- `output/hodom-hsc/analisis-datos-legacy-hodom-hsc.md`
- `output/hodom-hsc/informe-definitivo-telemetria-hodom-hsc.md`
- `output/hodom-hsc/analisis-rutas-y-paradas-hodom-ene-mar-2026.md`
- `output/hodom-hsc/plan-capacitacion-hodom-hsc.md`
- `output/operacional/plan-90-dias-dt.md`
- `output/operacional/guia-escalamiento-terreno.md`
- `output/operacional/formato-briefing-matinal.md`

## 2.2 Documentos fuente adicionales integrados
- Proyecto BIP / implementación permanente HODOM HSC:
 - `PROYECTO_IMPLEMENTACION_HODOM_HSC_2---972bcda9-90ca-463c-9d77-68e46b2ed970.pdf`
 - `PROYECTO_IMPLEMENTACION_HODOM_HSC_2---ca3e0128-ff6a-4337-b2a0-a438c1c34b6c.docx`
- PPT Enlace HODOM-APS / Programa Postrados:
 - `ENLACE_HODOM_-APS---2e557608-df12-4c5a-89f0-c3f4e765f423.pptx`

## 2.3 Base normativa considerada
- DS N°1/2022 — Reglamento de establecimientos que otorgan prestaciones de hospitalización domiciliaria
- Decreto Exento N°31/2024 — aprueba Norma Técnica HD 2024
- Ley 20.584 — derechos y deberes del paciente
- Ley 19.628 — protección de datos personales
- referencias complementarias del hospital y marco MINSAL utilizado en documentos previos

---

# 3. Diagnóstico consolidado del dispositivo HODOM HSC

## 3.1 Tesis diagnóstica central
HODOM HSC **no es un dispositivo fallido**. Tiene valor demostrado, resultados históricos defendibles y legitimidad institucional creciente. Sin embargo, hoy opera **por debajo de su potencial real**, con una brecha importante entre el valor clínico que ya genera y el nivel de estructura, trazabilidad, soporte normativo, regulación clínica, coordinación interna y soporte tecnológico con que aún funciona.

## 3.2 Formulación diplomática recomendada para el equipo
La formulación recomendada no es describir la unidad como “anárquica” o “mínima”, sino como:

> una unidad valiosa, con resultados reales, pero que aún funciona con alta dependencia del esfuerzo del equipo y con un nivel de formalización, trazabilidad y soporte menor al que una unidad permanente necesita.

## 3.3 Problemas estructurales identificados

### A. Brechas normativas
- protocolo PRO-002 desactualizado para una unidad permanente
- insuficiente formalización de escalamiento clínico
- registros no suficientemente homogéneos ni auditables
- evaluación domiciliaria y red de apoyo no plenamente trazables en formato uniforme
- alta y contrarreferencia aún no suficientemente estructuradas
- coordinación con APS y procesos específicos (ej. O₂) insuficientemente protocolizados

### B. Brechas de rendimiento operativo
- tiempos muertos relevantes al inicio y durante la jornada
- baja utilización efectiva de la jornada formal
- oportunidad de aumentar visitas diarias sin depender primero de más recursos
- uso de kilómetros y rutas subóptimo
- necesidad de mejor planificación diaria, hitos y priorización

### C. Brechas de gobernanza clínica
- fragmentación de la atención médica
- médicos tienden a seguir “sus” pacientes sin adecuada alternancia o regulación compartida
- altas no suficientemente reguladas por una lógica común
- diferencias de criterio no suficientemente contenidas por una instancia estructurada de revisión de casos
- baja productividad médica presencial y dificultad de programación por variabilidad horaria de al menos un médico de media jornada

### D. Brechas de sistema de información
- papel + planillas + registros dispersos
- ausencia de capa operativa compartida y visible para todos
- médicos registran en papel mientras otros perfiles disponen de SGH
- no existe hoy un panel general compartido para censo, alertas, ingresos, altas, pendientes, rutas y coordinación diaria

### E. Brechas de continuidad y red
- Enlace HODOM-APS existe, pero aún en marcha blanca
- contrarreferencia no plenamente formalizada como flujo estándar
- gran oportunidad de fortalecer admission avoidance desde APS / Programa Postrados

---

# 4. Datos duros más relevantes ya consolidados

## 4.1 Presión estructural hospitalaria
### Oportunidad de hospitalización ≤12h adulto
- 2019: 96,8%
- 2022: 69,5%
- 2023: 61,0%
- 2024: 54,9%
- 2025: 40,6%

### Índice ocupacional 2025
- Medicina: 97,5
- Cirugía: 96,0
- Traumatología: 97,9
- Área quirúrgica: 98,1
- Total hospital: 86,6

### Hospital
- 130 camas
- centro de referencia de red norte
- presión adicional por demanda de otras redes y regiones

## 4.2 Resultados históricos HODOM
### 2023
- 307 personas atendidas
- 4.037 días persona
- 0 fallecidos no esperados
- 16 reingresos
- 5.148 visitas

### 2024
- 1.077 personas atendidas
- 6.508 días persona
- 0 fallecidos no esperados
- 28 reingresos
- 11.562 visitas

### 2025
- 751 personas atendidas
- 5.480 días persona
- 0 fallecidos no esperados
- 28 reingresos
- 9.428 visitas
- sin trabajadora social durante el período descrito

## 4.3 Hallazgos logísticos/telemetría
- match programación ↔ GPS ~87%
- jornada formal mayor que jornada efectivamente operada
- capacidad ociosa importante en franja tardía y tiempos en base
- oportunidad de recuperar capacidad con mejor diseño de rutas, tiempos y ventanas operativas
- existe margen relevante de mejora sin partir por más recursos

---

# 5. Legitimidad institucional ya disponible

El proyecto institucional BIP 40059567-0 reconoce formalmente que la HODOM:
- ya ha sido implementada en 3 oportunidades
- ha sido fundamental para mejorar el proceso de hospitalización
- reduce presión asistencial y descongestiona urgencias
- permite destinar camas a pacientes de mayor riesgo
- entrega cuidados comparables en calidad y cantidad a la hospitalización tradicional
- favorece continuidad con nivel primario y secundario

Conclusión estratégica:
> no se está defendiendo una ocurrencia individual del DT, sino una convergencia entre valor ya demostrado por el equipo, necesidad estructural del hospital y reconocimiento institucional formal.

---

# 6. Estructura estratégica acordada: 3 horizontes

## Horizonte 1 — Mejor funcionamiento con lo que ya tenemos
### Idea central
Sacar lo mejor de lo que la unidad ya naturalmente hace, sin partir por pedir más recursos y sin sobrecargar al equipo.

### Orientación práctica
- optimizar funcionamiento actual
- aumentar visitas con los recursos actuales
- usar mejor kilómetros y tiempos
- mejorar coordinación y comunicación
- disminuir tiempos muertos
- mejorar registros
- ordenar planificación diaria, salidas, hitos y seguimiento
- instalar revisión/regulación de casos
- cerrar ya las brechas normativas insostenibles de mayor retorno operativo y cognitivo

### Tesis del horizonte 1
> aumentar el rendimiento real de la unidad con lo que ya tiene, mejorando cómo se organiza, cómo se mueve, cómo se coordina y cómo usa su tiempo.

## Horizonte 2 — Cumplimiento normativo y consolidación formal
### Idea central
Cerrar brechas exigibles y dejar la unidad defendible, trazable y segura.

### Componentes
- alineamiento con DS 1/2022 y NT 2024
- actualización de protocolos mínimos
- registros auditables
- seguridad del paciente
- trazabilidad
- gobernanza
- capacitación e inducción
- indicadores y evidencia de cumplimiento

## Horizonte 3 — Máxima expresión del potencial con los recursos que tenemos
### Idea central
Llevar la unidad a una versión más madura, inteligente y sostenible sin depender linealmente de más gasto.

### Palancas definidas
- nuevas tecnologías útiles
- inteligencia artificial
- automatización
- digitalización
- gestión del conocimiento
- capacitación continua
- gestión de campo
- trabajo en equipo
- cultura organizacional
- calidad
- seguridad
- innovación

---

# 7. Forma de implementación acordada (sin nombrarlo como gestión del cambio)

## Principios acordados
- avanzar por capas, no con cambios masivos de una vez
- partir por lo más útil para el trabajo real
- formalizar solo lo necesario
- usar herramientas breves, claras, absorbibles y fácilmente digeribles
- evitar burocracia innecesaria
- mostrar resultados tempranos
- ajustar con retroalimentación del equipo
- no duplicar trabajo
- diseñar todo para **bajar carga cognitiva**

## Fórmulas clave de lenguaje acordadas
- “ordenar sin rigidizar”
- “formalizar sin burocratizar”
- “mejorar sin sobrecargar”
- “más claridad, menos fricción”
- “todo lo que implementemos debe disminuir carga cognitiva, no aumentarla”

## Instrumentos mínimos y efectivos acordados
- briefing diario corto
- guías operativas de una página
- formatos mínimos estandarizados
- tablero simple de indicadores
- registro más homogéneo
- revisión periódica breve de lo que funcionó, lo que trabó y lo que hay que ajustar

---

# 8. Brechas normativas y operativas que deben cerrarse “ahora ya”

Se acordó priorizar no todas las brechas a la vez, sino las que sean:
- normativamente relevantes
- insostenibles si se dejan abiertas
- de alto retorno operativo
- de alto retorno en menor desgaste y menor carga cognitiva
- prototipables rápidamente

## Prioridad inmediata A
### 1. Revisión / regulación clínica de casos
Tu rol como **DT + médico regulador** debe traducirse en una instancia estable de revisión de casos para:
- priorizar ingresos
- revisar seguimientos complejos
- decidir egresos
- ordenar rescates
- priorizar cupos
- disminuir variabilidad clínica

Formato recomendado:
- presencial o digital
- 10-20 min
- integrado al briefing o posterior inmediato
- con decisión visible y registrada

### 2. Escalamiento clínico
Ya existe base en guía de semáforo/NEWS2. Debe traducirse a:
- regla única
- tiempos de respuesta
- trazabilidad mínima
- soporte real a terreno

### 3. Registro clínico mínimo homogéneo
Debe existir una sola captura operativa simple para:
- ingreso
- atención/visita
- procedimiento
- alerta
- alta

### 4. Formulario de ingreso + evaluación domicilio/cuidador
Debe permitir:
- decisión clínica más consistente
- trazabilidad de elegibilidad
- respaldo normativo
- menor ambigüedad y menor carga mental

### 5. Briefing/tablero diario
Debe permitir:
- ver el censo
- ver alertas
- ver ingresos, altas y pendientes
- ver móviles/rutas
- alinear el día

## Prioridad inmediata B
### 6. Alta y contrarreferencia
### 7. Núcleo mínimo de protocolos usables
- ingreso/elegibilidad
- evaluación domicilio/cuidador
- escalamiento
- alta/contrarreferencia
- O₂ domiciliario
- coordinación APS
- medicamentos y muestras

---

# 9. Panel de control general y prototipos inmediatos

## 9.1 Decisión estratégica
Se definió como objetivo mostrar mañana un **prototipo funcional rápido** de una capa operativa web, visible para todos, accesible por celular y orientada a ordenar el funcionamiento cotidiano.

## 9.2 Contexto técnico relevante
- médicos registran hoy en papel
- otros profesionales tienen relación con SGH
- el usuario ya cuenta con acceso vía CLI a SGH con sus credenciales
- se dispone de dominio e infraestructura para desplegar rápidamente un prototipo funcional
- existe posibilidad de construir en pocas iteraciones de horas varios prototipos web mínimos
- el sistema debe permitir **registrar digital** y luego **imprimir en formato compatible con la ficha papel** si se requiere respaldo físico

## 9.3 Qué debe demostrar el panel mañana
No un sistema grande, sino una **capa operativa mínima compartida** que permita:
- visibilidad común de la unidad
- coordinación diaria
- registros estructurados
- soporte a regulación clínica
- georreferenciación
- reducción de papel operativo
- reducción de pérdida de información
- preparación para continuidad futura

## 9.4 Prototipos web priorizados para mostrar
### Prototipo 1 — Panel general / tablero operativo
- pacientes activos
- cupos
- alertas
- ingresos pendientes
- altas pendientes
- móviles/rutas
- pendientes críticos

### Prototipo 2 — Registro web móvil de atención
- formulario breve por disciplina
- signos/procedimientos/nota corta
- usable desde celular
- imprimible en formato compatible con papel

### Prototipo 3 — Regulación clínica de casos
- ingresos propuestos
- casos complejos
- egresos posibles
- rescates
- decisión del regulador
- responsable

### Prototipo 4 — Georreferenciación y rutas
- mapa de pacientes
- agrupación territorial
- asignación de móvil/ruta
- apoyo a planificación y uso de kilómetros

### Prototipo 5 — Alta y contrarreferencia
- resumen breve
- indicaciones
- continuidad APS
- salida imprimible/enviable

## 9.5 Criterios de diseño acordados
Todo prototipo debe:
- reducir carga cognitiva
- no aumentar pasos innecesarios
- no duplicar trabajo
- permitir visibilidad compartida
- ser mobile-first
- ser simple, breve y usable
- ayudar al trabajo real del equipo

---

# 10. Replanteamiento del componente médico

## Problema identificado
- baja productividad médica presencial
- dificultad de programación por variabilidad horaria de un médico de media jornada
- poca cantidad de visitas médicas de ingreso/egreso/control
- continuidad fragmentada entre médicos
- paradigma actual demasiado centrado en presencialidad

## Decisión estratégica
El valor médico del dispositivo no debe expresarse solo como visita presencial. También debe expresarse como:
- regulación clínica
- revisión de casos
- seguimiento remoto/telemático cuando corresponda
- apoyo oportuno a terreno
- mejor orden de ingresos, egresos, alertas y rescates

## Formulación recomendada
> existe una brecha importante entre la necesidad de regulación y seguimiento médico de la unidad y la forma en que el componente médico está actualmente desplegado. Esto obliga a rediseñar la organización médica, combinando mejor presencialidad, regulación clínica y atención telemática cuando sea pertinente.

---

# 11. Continuidad con APS y admission avoidance

## Estado actual
El enlace HODOM-APS / Programa Postrados debe ser tratado como activo estratégico.

### Elementos ya presentes
- APS puede detectar descompensación/cuadro agudo y remitir informe resumido
- HODOM evalúa cupo y acepta/inicia tratamiento
- HODOM asume tratamiento, evaluación médica, exámenes y radiografías
- APS mantiene curaciones crónicas y cambio de dispositivos invasivos
- se informa alta por epicrisis

## Interpretación estratégica
HODOM no solo debe presentarse como herramienta para liberar camas. También debe presentarse como:
- interfaz hospital-APS
- soporte de continuidad del cuidado
- embrión de admission avoidance en pacientes vulnerables

---

# 12. Narrativa política y técnica acordada para la reunión

## Qué no hacer
- no partir criticando
- no usar lenguaje agresivo (“anárquico”, “desordenado”, “improvisado”)
- no sobreprometer
- no presentar tecnología como solución mágica

## Qué sí hacer
- reconocer al equipo
- reconocer resultados históricos
- mostrar problema estructural del hospital
- explicar que la unidad funciona pero por debajo de su potencial
- mostrar brechas como brechas del dispositivo y del soporte, no como fallas personales
- presentar un camino por horizontes
- mostrar herramientas concretas y alcanzables

## Frases acordadas de alto valor
- “No vengo a partir de cero.”
- “Lo que hoy existe merece ser reconocido, pero también protegido del desorden, la precariedad y la dependencia excesiva de soluciones informales.”
- “La pregunta ya no es si HODOM sirve, sino cuánto más podría aportar si estuviera mejor estructurado.”
- “Todo lo que implementemos debe disminuir carga cognitiva, no aumentarla.”
- “No quiero instalar un sistema pesado; quiero una capa operativa simple que ayude a que la unidad funcione mejor.”
- “Primero optimizar lo que ya existe. Luego consolidarlo. Después amplificar su potencial.”

---

# 13. Estructura de presentación consolidada

Se acordó evolucionar hacia una presentación final breve, fuerte y políticamente inteligente, basada en:
1. reconocimiento del trabajo del equipo
2. valor hospitalario de HODOM
3. diagnóstico actual (valor demostrado + capacidad no desplegada)
4. tres horizontes de desarrollo
5. forma de implementación simple y respetuosa
6. cierres normativos y operativos prioritarios
7. demostración temprana de prototipos web
8. cierre convocando al equipo

---

# 14. Acciones inmediatas sugeridas para mañana / próximas iteraciones

## Mañana
- presentar relato consolidado
- mostrar panel operativo / prototipos si están disponibles
- instalar idea de regulación clínica compartida
- instalar criterio de baja carga cognitiva
- recoger retroalimentación del equipo

## Iteraciones rápidas posteriores
### Sprint 0
- tablero briefing/censo/alertas/cupos
- regulación clínica de casos
- registro móvil mínimo
- escalamiento digital simple

### Sprint 1
- ingreso/evaluación domicilio
- georreferenciación
- rutas
- alta/contrarreferencia

### Sprint 2
- indicadores
- repositorio documental
- auditoría breve
- consolidación del núcleo mínimo de protocolos

---

# 15. Inventario estratégico de artefactos y recursos disponibles para la nueva etapa

## 15.1 Artefactos documentales y operativos ya existentes
Se debe considerar como activo estratégico todo el repositorio histórico acumulado en Google Drive y otras fuentes del programa desde el inicio de HODOM, incluyendo:
- documentación histórica completa de hospitalización domiciliaria desde su inicio
- formularios y registros clínicos actualmente usados e impresos para escritura manual
- planillas y consolidados por profesional/estamento
- rutas programadas históricas
- consolidaciones operativas y productivas
- documentos de entrega de turno
- epicrisis, DAU y documentación clínica histórica
- registros y material asociado a curaciones, educaciones y otros procesos

Conclusión: el nuevo trabajo no parte desde cero. Existe un corpus operativo real que debe ser inventariado, clasificado, simplificado y reutilizado como base para formularios, flujos y prototipos.

## 15.2 Segunda categoría de artefactos: documentación rectora
Debe existir como categoría propia de artefactos para el nuevo trabajo:
- normativa vigente HODOM (DS N°1/2022, NT 2024, regulación complementaria)
- protocolo vigente y sus versiones
- proyecto BIP / formulación institucional
- acuerdos operativos específicos (ej. O₂)
- presentación y flujo de enlace HODOM-APS
- instrumentos locales de calidad, seguridad y reportabilidad

Conclusión: no basta con mirar la operación; también hay que ordenar el corpus rector y normativo que va a guiar los rediseños.

## 15.3 Activos de datos a integrar en la nueva etapa
Se dejó explícito que deben considerarse como activos estructurales a ordenar e integrar:
- catastro de pacientes históricos
- rutas históricas
- geoposicionamiento / geolocalización de pacientes y rutas
- base histórica de visitas y atenciones
- registros impresos y digitales existentes
- telemetría GPS y análisis previos

## 15.4 Recursos humanos y materiales a ordenar y hacer visibles
Debe existir inventario coordinado y visible de:
- planilla completa de trabajadores
- horas y jornadas de cada integrante
- dotación real y disponibilidad operativa
- vehículos y estado operativo
- insumos disponibles
- medicamentos disponibles
- equipamiento clínico disponible
- recursos territoriales/logísticos disponibles

Esto debe pasar a ser parte del panel y de la coordinación operativa de la unidad.

## 15.5 Prioridades clínicas/operativas inmediatas explicitadas
Quedó señalado como prioridad de la nueva etapa debutar con la reactivación o reinstalación de prestaciones actualmente no desplegadas o subutilizadas:
- **sueloterapia**: reinicio/instalación como línea de trabajo concreta
- **oxigenoterapia**: reactivación, considerando que existen **3 concentradores de oxígeno** disponibles y actualmente subutilizados/no utilizados

Conclusión: estas líneas deben tratarse no solo como prestaciones clínicas, sino como prueba visible de capacidad recuperada del dispositivo.

---

# 16. Decisiones y posiciones que no deben olvidarse

1. **El tono diplomático no es debilidad: es una decisión estratégica.**
2. **El diagnóstico de fondo sí reconoce subutilización, baja formalización y alta dependencia del esfuerzo individual.**
3. **La narrativa pública debe hablar de capacidad no plenamente desplegada, no de caos.**
4. **El primer horizonte incluye también cierres normativos insostenibles, no solo eficiencia operativa.**
5. **La baja carga cognitiva es criterio de diseño central para cualquier herramienta o cambio.**
6. **La regulación clínica compartida es prioritaria y debe ser visible.**
7. **El componente médico debe rediseñarse incluyendo regulación y telematicidad, no solo presencialidad.**
8. **El panel web compartido debe estrenarse como símbolo de posibilidad concreta, no como sistema definitivo.**
9. **La documentación que se construya debe ser mínima, absorbible, efectiva y fácilmente actualizable.**
10. **Todo debe quedar nativamente documentado en la plataforma para no depender solo de memoria conversacional.**
11. **El repositorio histórico de Google Drive y los artefactos documentales existentes son activos del rediseño, no solo archivo muerto.**
12. **Los inventarios de RRHH, vehículos, insumos, medicamentos y equipamiento deben integrarse a la coordinación visible de la unidad.**
13. **La reactivación de sueroterapia y oxigenoterapia debe tratarse como prioridad concreta de capacidad clínica recuperada.**

---

# 17. Cierre operativo

Este consolidado debe tratarse como documento madre de la fase actual. Cualquier siguiente producto — presentación final, tablero, backlog, flujos, prototipos o plan de 90 días ajustado — debe derivarse de esta síntesis.

**Estado:** consolidado al 2026-03-25, listo para continuar trabajo sin pérdida de contexto.
</file>

<file name="marco-rol-dt-hodom-hsc---a3bb86e5-277c-4653-8bc2-7a7fc43381db.md" mime="text/markdown">
# Marco de Rol del Director Técnico HODOM HSC
## Autoridad, responsabilidades y fronteras de función
### Versión de trabajo | 2026-03-26

---

# 1. Propósito del rol

El Director Técnico de HODOM es la figura responsable de **conducir clínicamente, ordenar operativamente y resguardar normativamente** la Hospitalización Domiciliaria como dispositivo hospitalario integrado, asegurando que funcione con seguridad, trazabilidad, continuidad del cuidado y pertinencia clínica.

No es solo una jefatura administrativa.
No es solo un médico asistencial.
No es solo un firmante normativo.

**Es la autoridad técnico-clínica que convierte HODOM en una unidad hospitalaria real y gobernable.**

---

# 2. Fórmula simple del cargo

## El DT HODOM es simultáneamente:
1. **Autoridad clínica de la modalidad**
2. **Regulador operativo del flujo de casos**
3. **Responsable normativo y documental del dispositivo**
4. **Conductor del equipo y del modelo de trabajo**
5. **Interfaz formal entre hospital, domicilio y red**

---

# 3. Declaración breve de autoridad

## Autoridad del Director Técnico
El Director Técnico tiene autoridad para:
- definir criterios operativos y clínicos de funcionamiento de HODOM
- validar o rechazar ingresos a la modalidad según criterios establecidos
- regular continuidad, priorización, escalamiento y alta de casos
- establecer estándares mínimos de registro, seguridad y trazabilidad
- ordenar la operación clínica diaria del equipo
- proponer, actualizar y exigir protocolos de trabajo
- supervisar cumplimiento normativo y prepararse para fiscalización
- representar técnicamente a HODOM ante dirección y la red asistencial

## Límite de esa autoridad
No reemplaza la autoridad jerárquica institucional de dirección hospitalaria, ni la jefatura administrativa de RRHH, finanzas o contratos. Su autoridad es **técnico-clínica, operativa y normativa** sobre el dispositivo HODOM.

---

# 4. Responsabilidad principal en una frase

**Que cada paciente que entre, permanezca, transite y egrese de HODOM lo haga con seguridad, pertinencia, registro suficiente, coordinación real y criterio clínico compartido.**

---

# 5. Núcleo del rol: 7 responsabilidades estructurales

## 1. Gobernanza clínica de la modalidad
Debe asegurar que HODOM no opere como suma de decisiones individuales, sino como una unidad con criterio compartido.

Incluye:
- criterios de ingreso, permanencia, rescate y alta
- revisión de casos complejos
- definición de prioridades clínicas
- consistencia del razonamiento clínico de la unidad
- articulación entre atención presencial, teleatención y regulación

## 2. Regulación diaria de casos
Debe instalar y sostener una función de regulación clínica cotidiana.

Incluye:
- revisar ingresos potenciales y pacientes activos
- identificar egresos posibles, rescates y alertas
- asignar prioridad y modalidad de seguimiento
- decidir cuándo basta telecontrol y cuándo requiere visita presencial
- distribuir carga clínica de manera racional

## 3. Seguridad del paciente y escalamiento
Debe garantizar que la modalidad domiciliaria tenga criterios claros de vigilancia, deterioro y respuesta.

Incluye:
- protocolo de escalamiento clínico
- definición de red flags
- criterio de derivación a urgencia/hospital
- revisión de incidentes, eventos adversos y casi fallas
- cierre de brechas de seguridad detectadas

## 4. Cumplimiento normativo y documental
Debe asegurar que HODOM sea defendible ante auditoría, fiscalización o revisión institucional.

Incluye:
- protocolos vigentes
- registros clínicos trazables
- consentimientos
- documentación de procesos críticos
- respaldo de decisiones clínicas relevantes
- alineamiento con normativa HD y teleatención cuando aplique

## 5. Conducción operativa del equipo
Debe ordenar la operación sin burocratizarla.

Incluye:
- briefing diario
- reglas de coordinación
- estandarización mínima de formularios
- definición de responsabilidades por turno/proceso
- disminución de carga cognitiva del equipo
- formación en terreno y retroalimentación breve

## 6. Continuidad hospital-domicilio-red
Debe evitar que HODOM sea una isla.

Incluye:
- mejor derivación desde hospital
- contrarreferencia clara a APS / Postrados / red
- enlace con UEA, medicina, cirugía, traumatología y servicios derivadores
- continuidad en egreso y rescate
- articulación con teleatención y seguimiento remoto

## 7. Desarrollo del modelo y mejora continua
Debe empujar evolución del dispositivo.

Incluye:
- priorizar quick wins
- definir KPIs
- revisar productividad, tiempos muertos, uso de vehículos y cartera clínica
- impulsar reactivación de capacidades subutilizadas (sueroterapia, oxigenoterapia, telecontrol)
- conducir la transición desde campaña a modelo permanente

---

# 6. Qué decide el Director Técnico

## Decide directamente
- criterios operativos de ingreso y exclusión según protocolo
- pertinencia clínica de hospitalización domiciliaria
- intensidad de seguimiento
- modalidad de atención: presencial / telecontrol / mixto
- priorización de casos del día
- necesidad de escalamiento o rescate
- estándar mínimo de registro clínico
- estructura del briefing y revisión de casos
- necesidad de protocolizar procesos críticos
- activación de cartera clínica permitida según capacidad y seguridad

## Decide con otros
- expansión de dotación
- cambios presupuestarios
- ampliación territorial relevante
- modificaciones estructurales del modelo de financiamiento
- integración institucional con otros sistemas formales
- activación de nuevas prestaciones de mayor complejidad

## No decide solo
- contratos y remuneraciones
- asignación presupuestaria global del hospital
- estructura orgánica oficial del establecimiento
- inversiones mayores
- decisiones disciplinarias formales de RRHH

---

# 7. Matriz de autoridad práctica

| Materia | DT HODOM | Dirección hospitalaria | Subdirecciones | Equipo HODOM |
|--------|----------|------------------------|----------------|--------------|
| Ingreso a HODOM | A | I | C | C |
| Alta desde HODOM | A | I | C | C |
| Escalamiento clínico | A | I | C | R |
| Briefing diario | A | I | I | R |
| Protocolos clínico-operativos | A | I/C | C | C/R |
| Registro clínico mínimo | A | I | C | R |
| Consentimiento teleatención | A | I | C | R |
| Distribución del trabajo clínico | A | I | C | R |
| KPIs y tablero | A | I/C | C | R |
| Cartera clínica activa | A/C | I | C/A según nivel | C |
| RRHH contractual | I | A | A/R | I |
| Presupuesto | I | A | A/R | I |

### Leyenda
- **A** = accountable / autoridad final técnica
- **R** = responsible / ejecuta
- **C** = consulted / se consulta
- **I** = informed / informado

---

# 8. Autoridad clínica específica del DT

## A. Sobre ingresos
- puede exigir criterios mínimos de elegibilidad
- puede rechazar ingresos inseguros o mal indicados
- puede pedir evaluación adicional antes de aceptar
- puede ordenar uso de evaluación domiciliaria estructurada

## B. Sobre pacientes activos
- puede redefinir plan de seguimiento
- puede cambiar modalidad de atención
- puede indicar revisión médica prioritaria
- puede escalar a urgencia, hospital o evaluación presencial

## C. Sobre altas
- puede exigir criterios clínicos y operativos de cierre
- puede impedir altas inseguras o mal documentadas
- puede exigir contrarreferencia clara

## D. Sobre teleatención
- puede definir cuándo es pertinente
- puede exigir consentimiento, registro y canal seguro
- puede prohibir su uso en escenarios clínicos no apropiados
- puede usarla como herramienta de regulación, seguimiento y resolución rápida

---

# 9. Responsabilidades indelegables

Estas no deberían diluirse ni quedar tácitamente en nadie más:

1. sostener el criterio clínico común de la unidad
2. asegurar la seguridad del modelo domiciliario
3. validar que el registro clínico sea suficiente y trazable
4. resguardar cumplimiento normativo crítico
5. mantener la función de regulación de casos
6. conducir actualización protocolaria mínima
7. representar técnicamente la unidad ante dirección
8. identificar brechas que comprometan seguridad o sostenibilidad

---

# 10. Responsabilidades delegables

Sí pueden delegarse parcialmente, pero no desaparecer del radar del DT:
- consolidación de datos e indicadores
- preparación documental
- monitoreo de stock e insumos
- coordinación logística diaria
- seguimiento administrativo de consentimientos
- mantenimiento de repositorio documental
- capacitaciones operativas específicas

**Principio:** se puede delegar la ejecución, no la responsabilidad de que exista y funcione.

---

# 11. Qué tiene que verse en la práctica para que el rol exista de verdad

Si tu rol está bien instalado, deberían empezar a observarse estas señales:

- existe briefing diario con revisión real de casos
- ya no hay pacientes “propiedad” de cada médico
- hay criterio común de ingreso, seguimiento y alta
- los casos complejos escalan por una vía clara
- el equipo sabe qué registrar y cómo
- la dirección te reconoce como referente técnico de HODOM
- APS y los servicios clínicos saben con quién hablar
- la cartera empieza a crecer con orden y no por improvisación
- la teleatención se usa con sentido clínico, no como accesorio tecnológico

---

# 12. Riesgos si el rol no se formaliza

- jefatura difusa
- autoridad simbólica pero no operativa
- persistencia de medicina “cada uno con sus pacientes”
- dificultad para exigir registro y estandarización
- incapacidad de ordenar la carga clínica
- teleatención y nuevos procesos usados sin gobernanza
- brechas normativas que quedan “de todos y de nadie”
- desgaste personal del DT por hiperresponsabilidad sin palancas reales

---

# 13. Propuesta de formulación institucional breve

## Opción corta
**El Director Técnico de HODOM es la autoridad técnico-clínica responsable de la conducción, regulación, seguridad, trazabilidad y cumplimiento normativo de la Hospitalización Domiciliaria del Hospital de San Carlos.**

## Opción expandida
**Corresponde al Director Técnico de HODOM conducir el dispositivo de Hospitalización Domiciliaria en sus dimensiones clínica, operativa y normativa, asegurando criterios de ingreso, seguimiento, escalamiento y alta; la coordinación del equipo; la suficiencia del registro clínico; la continuidad hospital-domicilio-red; y la implementación de protocolos, indicadores y mecanismos de mejora continua.**

---

# 14. Tu rol traducido políticamente

## Lo que debes transmitir al equipo
- no vienes a controlar por controlar
- vienes a dar marco, criterio, respaldo y dirección
- vienes a ordenar para proteger lo que el equipo ya construyó
- vienes a disminuir arbitrariedad, no a aumentar burocracia

## Lo que debes transmitir a dirección
- HODOM requiere autoridad técnico-clínica explícita para ser gobernable
- sin esa autoridad, el riesgo normativo y operativo aumenta
- formalizar el rol del DT no es un lujo: es condición de seguridad, trazabilidad y escalabilidad

---

# 15. Frase de identidad del cargo

**Ordenar sin rigidizar. Regular sin enlentecer. Cuidar sin fragmentar. Formalizar sin burocratizar.**

---

# 16. Recomendación operativa inmediata

Para sistematizar tu rol desde ya, instala estas 5 piezas visibles esta semana:

1. **Briefing matinal diario con regulación de casos**
2. **Criterios escritos de ingreso / seguimiento / alta**
3. **Registro clínico mínimo obligatorio**
4. **Canal formal de escalamiento clínico**
5. **Matriz de responsabilidades del equipo**

Eso hace que el rol deje de ser discursivo y empiece a existir como sistema.

---

# 17. Síntesis final

Tu rol en HODOM no debe quedar entendido como “médico del programa” ni como “coordinador administrativo”.

Debe quedar sistematizado como:

> **autoridad técnico-clínica, regulador operativo y responsable normativo del dispositivo HODOM**, con mandato para ordenar la modalidad, proteger al paciente, dar coherencia al equipo y hacer gobernable la hospitalización domiciliaria como unidad hospitalaria real.

---

*Documento de trabajo para formalización interna del rol del Director Técnico HODOM HSC.*
</file>
assistant: Recibidos los 6 archivos. Déjame leer el análisis de rutas (el XLSX) y luego integrar todo.
assistant: Dato muy rico. Tengo 6 archivos: el XLSX de análisis operacional (7 hojas, 1574 visitas programadas, 7587 eventos GPS, 145 direcciones geocodificadas, 1895 anomalías), el CSV raw de telemetría GPS, la presentación Marp del DT, el guión, el consolidado estratégico y el marco de rol del DT.

Integro al modelo los hallazgos nuevos que no estaban capturados.
assistant: Voy a agregar la integración de la dimensión espacial-temporal (telemetría GPS + análisis operacional) como una nueva subsección dentro de §16, y actualizar la firma con las fuentes y hallazgos nuevos.
assistant: Ahora actualizo la firma:
assistant: Integrado. Resumen de lo que se absorbió de los 6 archivos:

**Del XLSX operacional + CSV GPS:**
- Nueva §16.15 "Dimensión Espacial-Temporal" con estructura completa del dataset (planned_visits, gps_events, visit_matches, daily_vehicle_summary, geocoded_addresses)
- 7 hallazgos categóricos: match 87%, productividad 39.2%, 1.818h ociosas/trim, perfiles diferenciados de 3 vehículos, velocidades >100kph, 145 domicilios geocodificados, 1.895 paradas anómalas
- 4 morfismos nuevos (gps_track_of, match_visita, geocode, productividad)
- 2 PE nuevas: PE-26 (geocodificación → PE-5 automático) y PE-27 (match GPS valida ejecución)
- 4 déficits nuevos: D36-D39 (bloque tardío ocioso, velocidades, paradas extra, SUV solo L-V)

**De los documentos del DT:**
- Nueva §16.16 con datos de perfil demográfico exacto (70.1 años promedio, 35% ≥80, ITU 12.2%, neumonía 11%)
- Serie completa de oportunidad de hospitalización ≤12h: 96.8% → 40.6% en 6 años
- Rol dual DT como agente formal no existente previamente en el modelo
- Capacidad recuperable H1: +50-67% visitas/día sin recursos adicionales

Modelo en versión 4.0b, 2323 líneas, 27 PE, 39 déficits, 50+ objetos, 40+ morfismos.
user: [Queued messages while agent was busy]

---
Queued #1
Conversation info (untrusted metadata):
```json
{
  "message_id": "248",
  "sender_id": "7192195698",
  "sender": "Ominono",
  "timestamp": "Tue 2026-03-31 23:01 GMT+2"
}
```

Sender (untrusted metadata):
```json
{
  "label": "Ominono (7192195698)",
  "id": "7192195698",
  "name": "Ominono"
}
```

como vas?

---
Queued #2
Conversation info (untrusted metadata):
```json
{
  "message_id": "252",
  "sender_id": "7192195698",
  "sender": "Ominono",
  "timestamp": "Tue 2026-03-31 23:13 GMT+2"
}
```

Sender (untrusted metadata):
```json
{
  "label": "Ominono (7192195698)",
  "id": "7192195698",
  "name": "Ominono"
}
```

listo?
assistant: 

Listo. Modelo actualizado a 2323 líneas con todo integrado.

Lo que se hizo en esta sesión completa:

1. **Revisión de consistencia** — 14 correcciones (enum de estados 4→7, referencias huérfanas, PE tautológica, firma desincronizada, conteo de categorías, supertipo RegistroClinico)

2. **Absorción FHIR/HaH** — nueva §17 con 4 déficits (RPM, AA/ESD, outcomes, SDOH), mapeo FHIR de 11 objetos, fortalezas confirmadas del modelo chileno

3. **Planilla de rutas 31/03** — estructura de 4 zonas, tabla de 15 códigos operacionales, descubrimiento del ingreso como fan-out multi-profesional (ING ENF + VM INGRESO + ING KTR), PE-23 a PE-25

4. **Telemetría GPS + análisis operacional** — nueva §16.15 con 7.587 eventos GPS, 1.574 visitas programadas, 87% match, 145 geocodificaciones, perfiles de 3 vehículos, 1.818h ociosas/trim, PE-26 y PE-27, D36-D39

5. **Documentos del DT** — §16.16 con perfil demográfico exacto, serie oportunidad hospitalización, rol dual DT como agente formal, capacidad recuperable H1

Estado final: **v4.0b, 2323 líneas, 18 secciones, 27 PE, 39 déficits, 50+ objetos, 40+ morfismos, 27 fuentes integradas.**
assistant: Listo. Modelo actualizado a 2323 líneas con todo integrado.

Lo que se hizo en esta sesión completa:

1. **Revisión de consistencia** — 14 correcciones (enum de estados 4→7, referencias huérfanas, PE tautológica, firma desincronizada, conteo de categorías, supertipo RegistroClinico)

2. **Absorción FHIR/HaH** — nueva §17 con 4 déficits (RPM, AA/ESD, outcomes, SDOH), mapeo FHIR de 11 objetos, fortalezas confirmadas del modelo chileno

3. **Planilla de rutas 31/03** — estructura de 4 zonas, tabla de 15 códigos operacionales, descubrimiento del ingreso como fan-out multi-profesional (ING ENF + VM INGRESO + ING KTR), PE-23 a PE-25

4. **Telemetría GPS + análisis operacional** — nueva §16.15 con 7.587 eventos GPS, 1.574 visitas programadas, 87% match, 145 geocodificaciones, perfiles de 3 vehículos, 1.818h ociosas/trim, PE-26 y PE-27, D36-D39

5. **Documentos del DT** — §16.16 con perfil demográfico exacto, serie oportunidad hospitalización, rol dual DT como agente formal, capacidad recuperable H1

Estado final: **v4.0b, 2323 líneas, 18 secciones, 27 PE, 39 déficits, 50+ objetos, 40+ morfismos, 27 fuentes integradas.**
