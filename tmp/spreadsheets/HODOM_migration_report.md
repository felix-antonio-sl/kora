# Reporte de migración HODOM -> estructura ideal

- Fuente: `/Users/felixsanhueza/Downloads/HOMOM 2026 ACT.xlsx`
- Plantilla base: `/Users/felixsanhueza/Developer/kora/tmp/spreadsheets/HODOM_ideal.xlsx`
- Workbook migrado: `/Users/felixsanhueza/Developer/kora/tmp/spreadsheets/HODOM_ideal_migrado.xlsx`
- Días esperados: `455`
- Días completos: `442`
- Días parciales: `13`
- Conflictos totales: `39`
- Notas informativas: `571`

## Resumen por mes

### DICIEMBRE 2024
- Estado: `Validar`
- Migración: `31/31` días, `30` completos, `1` parciales, `122` celdas copiadas
- Conflictos: `egress_total_mismatch` x 1, `header_mismatch` x 1
- Detalle:
  - Encabezado interno no coincide con la pestaña: JULIO 2024
  - Día 31: total egresos no calza con desglose (2 vs 3)

### ENERO 2025
- Estado: `Listo`
- Migración: `31/31` días, `31` completos, `0` parciales, `95` celdas copiadas
- Conflictos: ninguno
- Notas: `egress_total_only` x 20, `income_total_only` x 23
- Detalle:
  - Día 2: migrado usando solo total informado de ingresos (2)
  - Día 3: migrado usando solo total informado de egresos (2)
  - Día 4: migrado usando solo total informado de ingresos (1)
  - Día 5: migrado usando solo total informado de ingresos (1)
  - Día 5: migrado usando solo total informado de egresos (1)
  - Día 6: migrado usando solo total informado de ingresos (7)
  - Día 6: migrado usando solo total informado de egresos (2)
  - Día 7: migrado usando solo total informado de ingresos (2)
  - Día 7: migrado usando solo total informado de egresos (1)
  - Día 8: migrado usando solo total informado de ingresos (1)
  - ... y 33 más

### FEBRERO 2025
- Estado: `Validar`
- Migración: `28/28` días, `28` completos, `0` parciales, `93` celdas copiadas
- Conflictos: `header_mismatch` x 1
- Notas: `egress_total_only` x 20, `income_total_only` x 24
- Detalle:
  - Encabezado interno no coincide con la pestaña: ENERO 2025

### MARZO 2025
- Estado: `Listo`
- Migración: `31/31` días, `31` completos, `0` parciales, `104` celdas copiadas
- Conflictos: ninguno
- Notas: `egress_total_only` x 23, `income_total_only` x 26
- Detalle:
  - Día 1: migrado usando solo total informado de egresos (2)
  - Día 3: migrado usando solo total informado de ingresos (4)
  - Día 3: migrado usando solo total informado de egresos (4)
  - Día 4: migrado usando solo total informado de ingresos (1)
  - Día 4: migrado usando solo total informado de egresos (2)
  - Día 5: migrado usando solo total informado de ingresos (2)
  - Día 5: migrado usando solo total informado de egresos (3)
  - Día 6: migrado usando solo total informado de ingresos (1)
  - Día 6: migrado usando solo total informado de egresos (1)
  - Día 7: migrado usando solo total informado de ingresos (2)
  - ... y 39 más

### ABRIL 2025
- Estado: `Validar`
- Migración: `30/30` días, `30` completos, `0` parciales, `96` celdas copiadas
- Conflictos: `known_manual_summary_month` x 1, `manual_summary_value` x 1
- Notas: `egress_total_only` x 21, `income_total_only` x 23
- Detalle:
  - Resumen manual sospechoso: Personas Atendidas = 71
  - Mes identificado previamente con resumen manual sospechoso

### MAYO 2025
- Estado: `Validar`
- Migración: `31/31` días, `29` completos, `2` parciales, `108` celdas copiadas
- Conflictos: `carry_forward_mismatch` x 1, `daily_balance_issue` x 1, `known_daily_balance_issue` x 1, `known_manual_summary_month` x 1, `manual_summary_value` x 1
- Notas: `egress_total_only` x 1
- Detalle:
  - Resumen manual sospechoso: Personas Atendidas = 55
  - Mes identificado previamente con resumen manual sospechoso
  - Mes identificado previamente con al menos un problema de balance diario
  - Día 30: existencia inicial 19 no coincide con camas ocupadas del día previo 12
  - Día 31: balance diario no calza (20 + 0 - 0 = 20, origen muestra 50)

### JUNIO 2025
- Estado: `Listo`
- Migración: `30/30` días, `30` completos, `0` parciales, `89` celdas copiadas
- Conflictos: ninguno
- Notas: `egress_total_only` x 17, `income_total_only` x 24
- Detalle:
  - Día 1: migrado usando solo total informado de egresos (2)
  - Día 2: migrado usando solo total informado de ingresos (3)
  - Día 2: migrado usando solo total informado de egresos (7)
  - Día 3: migrado usando solo total informado de ingresos (5)
  - Día 3: migrado usando solo total informado de egresos (2)
  - Día 4: migrado usando solo total informado de ingresos (1)
  - Día 4: migrado usando solo total informado de egresos (3)
  - Día 5: migrado usando solo total informado de ingresos (1)
  - Día 5: migrado usando solo total informado de egresos (1)
  - Día 6: migrado usando solo total informado de ingresos (2)
  - ... y 31 más

### JULIO 2025
- Estado: `Validar`
- Migración: `31/31` días, `30` completos, `1` parciales, `108` celdas copiadas
- Conflictos: `carry_forward_mismatch` x 1, `known_manual_summary_month` x 1, `manual_summary_value` x 1
- Notas: `egress_total_only` x 22, `income_total_only` x 23
- Detalle:
  - Resumen manual sospechoso: Personas Atendidas = 68
  - Mes identificado previamente con resumen manual sospechoso
  - Día 31: existencia inicial 14 no coincide con camas ocupadas del día previo 15

### AGOSTO 2025
- Estado: `Validar`
- Migración: `31/31` días, `30` completos, `1` parciales, `102` celdas copiadas
- Conflictos: `carry_forward_mismatch` x 1, `legacy_structure_variant` x 1
- Notas: `egress_total_only` x 23, `income_total_only` x 24
- Detalle:
  - La estructura antigua cambia desde este mes; migrado por detección y no por posición fija
  - Día 30: existencia inicial 15 no coincide con camas ocupadas del día previo 12

### SEPTIEMBRE 2025
- Estado: `Validar`
- Migración: `30/30` días, `28` completos, `2` parciales, `97` celdas copiadas
- Conflictos: `carry_forward_mismatch` x 2, `legacy_structure_variant` x 1
- Notas: `egress_total_only` x 21, `income_total_only` x 24
- Detalle:
  - La estructura antigua cambia desde este mes; migrado por detección y no por posición fija
  - Día 29: existencia inicial 18 no coincide con camas ocupadas del día previo 21
  - Día 30: existencia inicial 21 no coincide con camas ocupadas del día previo 19

### OCTUBRE 2025
- Estado: `Validar`
- Migración: `31/31` días, `30` completos, `1` parciales, `99` celdas copiadas
- Conflictos: `carry_forward_mismatch` x 1, `known_manual_summary_month` x 1, `legacy_structure_variant` x 1, `manual_summary_value` x 1
- Notas: `egress_total_only` x 22, `income_total_only` x 23
- Detalle:
  - Resumen manual sospechoso: Altas = 61
  - Mes identificado previamente con resumen manual sospechoso
  - La estructura antigua cambia desde este mes; migrado por detección y no por posición fija
  - Día 29: existencia inicial 15 no coincide con camas ocupadas del día previo 17

### NOVIEMBRE 2025
- Estado: `Validar`
- Migración: `30/30` días, `28` completos, `2` parciales, `97` celdas copiadas
- Conflictos: `carry_forward_mismatch` x 2, `known_manual_summary_month` x 1, `legacy_structure_variant` x 1, `manual_summary_value` x 1
- Notas: `egress_total_only` x 23, `income_total_only` x 20
- Detalle:
  - Resumen manual sospechoso: Altas = 61
  - Mes identificado previamente con resumen manual sospechoso
  - La estructura antigua cambia desde este mes; migrado por detección y no por posición fija
  - Día 29: existencia inicial 15 no coincide con camas ocupadas del día previo 14
  - Día 30: existencia inicial 14 no coincide con camas ocupadas del día previo 15

### DICIEMBRE 2025
- Estado: `Validar`
- Migración: `31/31` días, `30` completos, `1` parciales, `95` celdas copiadas
- Conflictos: `carry_forward_mismatch` x 1, `known_manual_summary_month` x 1, `legacy_structure_variant` x 1, `manual_summary_value` x 1
- Notas: `egress_total_only` x 19, `income_total_only` x 25
- Detalle:
  - Resumen manual sospechoso: Altas = 61
  - Mes identificado previamente con resumen manual sospechoso
  - La estructura antigua cambia desde este mes; migrado por detección y no por posición fija
  - Día 29: existencia inicial 15 no coincide con camas ocupadas del día previo 14

### ENERO 2026
- Estado: `Validar`
- Migración: `31/31` días, `29` completos, `2` parciales, `101` celdas copiadas
- Conflictos: `carry_forward_mismatch` x 2, `known_manual_summary_month` x 1, `legacy_structure_variant` x 1, `manual_summary_value` x 1
- Notas: `egress_total_only` x 23, `income_total_only` x 23
- Detalle:
  - Resumen manual sospechoso: Altas = 46
  - Mes identificado previamente con resumen manual sospechoso
  - La estructura antigua cambia desde este mes; migrado por detección y no por posición fija
  - Día 29: existencia inicial 15 no coincide con camas ocupadas del día previo 12
  - Día 30: existencia inicial 12 no coincide con camas ocupadas del día previo 17

### FEBRERO 2026
- Estado: `Validar`
- Migración: `28/28` días, `28` completos, `0` parciales, `78` celdas copiadas
- Conflictos: `known_manual_summary_month` x 1, `legacy_structure_variant` x 1, `manual_summary_value` x 1
- Notas: `egress_total_only` x 15, `income_total_only` x 19
- Detalle:
  - Resumen manual sospechoso: Altas = 46
  - Mes identificado previamente con resumen manual sospechoso
  - La estructura antigua cambia desde este mes; migrado por detección y no por posición fija
