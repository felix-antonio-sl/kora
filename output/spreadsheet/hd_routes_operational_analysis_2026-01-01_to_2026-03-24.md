# Análisis operativo de rutas HD Hospital de San Carlos

## 1. Resumen del período
- Ventana comparable: **2026-01-01** a **2026-03-24**.
- Dispositivos GPS comparables: **3**.
- Visitas programadas comparables: **1573**.
- Direcciones únicas geocodificables: **144**; resueltas: **141** (97.9%).
- Matches operativos: **564** (35.9%) entre `alta` y `media`.
- Visitas sin match: **1009**.
- Bloques ambiguos: **69**; bloques con reserva: **20**.

## 2. Perfil por vehículo
- `PFFF57- RICARDO ALVIAL`: 575 visitas programadas, 39.8% con match operativo, 6132.2 km, 361 paradas extra.
- `RGHB14 NAVARA`: 529 visitas programadas, 38.2% con match operativo, 6740.3 km, 383 paradas extra.
- `SUV TZXS94`: 312 visitas programadas, 42.6% con match operativo, 3665.7 km, 148 paradas extra.

## 3. Brechas de cumplimiento
- `2026-01-11` / `RGHB14 NAVARA`: cumplimiento 8.3%, 11 sin match, 9 paradas extra.
- `2026-03-02` / `RGHB14 NAVARA`: cumplimiento 8.7%, 21 sin match, 4 paradas extra.
- `2026-01-09` / `PFFF57- RICARDO ALVIAL`: cumplimiento 11.1%, 8 sin match, 4 paradas extra.
- `2026-01-19` / `SUV TZXS94`: cumplimiento 12.5%, 7 sin match, 2 paradas extra.
- `2026-02-23` / `SUV TZXS94`: cumplimiento 13.3%, 13 sin match, 1 paradas extra.

## 4. Cuellos de botella operativos
- `CACHAPOAL`: desviacion media 1137.1 m en 10 visitas comparables.
- `SAN CARLOS`: desviacion media 603.5 m en 504 visitas comparables.
- `NIQUEN`: desviacion media 474.2 m en 28 visitas comparables.
- `SAN NICOLAS`: desviacion media 402.2 m en 8 visitas comparables.
- `SAN GREGORIO`: desviacion media 142.8 m en 14 visitas comparables.

## 5. Recomendaciones
- Consolidar una llave diaria explicita `vehiculo/bloque` en la planilla para reducir las asignaciones ambiguas.
- Estandarizar direcciones operativas antes de publicar la ruta diaria; las fallas de geocoding se concentran en domicilios con referencias abiertas.
- Revisar dias con `paradas_extra` altas como proxy de tiempos muertos o desvio operativo, en especial cuando coinciden con bajo cumplimiento.
- Mantener el 25 de marzo de 2026 fuera de comparaciones de ejecucion hasta contar con telemetria del mismo dia.

## Notas metodológicas
- El análisis es de **gestión operativa** y no reemplaza el juicio directivo ni clínico.
- Se anonimizaron pacientes en las tablas analíticas mediante identificadores `PAC-XXX`.
- La programación del **2026-03-25** queda fuera de la comparación principal por ausencia de telemetría utilizable en el CSV GPS.
- Los detalles fila a fila están en el workbook [`hd_routes_operational_analysis_2026-01-01_to_2026-03-24.xlsx`](file:///Users/felixsanhueza/Developer/kora/output/spreadsheet/hd_routes_operational_analysis_2026-01-01_to_2026-03-24.xlsx).
