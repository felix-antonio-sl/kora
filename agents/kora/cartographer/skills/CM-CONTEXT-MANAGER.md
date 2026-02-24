---
_manifest:
  urn: "urn:kora:skill:cartographer-context-manager:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-CONTEXT-MANAGER

## Proposito

Gestionar el contexto multi-turno del proceso de modelado: preservar la fase activa, los artefactos generados, y detectar cambios de tema o solicitudes de volver a una fase anterior.

## Procedimiento

1. Al inicio de cada turno, comparar tema del mensaje actual vs fase FSM activa (ESCUCHAR | MAPEAR | ELEVAR | CRISTALIZAR)
2. Aplicar mantra de la fase activa como filtro: S-ESCUCHAR("No juzgar. Solo absorber."), S-MAPEAR("Crear mapa antes de redisenar."), S-ELEVAR("Buscar patrones universales."), S-CRISTALIZAR("Elegir UNA solucion.")
3. Detectar senales de cambio: nuevo proyecto no relacionado, solicitud de volver a fase anterior, cambio de dominio del modelo
4. Si continuidad: mantener fase activa, preservar artefactos acumulados (inventario, mapa ontologico, arquitectura)
5. Si retroceso de fase solicitado: confirmar con usuario y cargar artefactos de la fase anterior
6. Si CONTEXT_SHIFT (tema totalmente diferente): redirigir a S-DISPATCHER con resumen de fase en progreso

## Output

Continuidad en la fase activa con mantra aplicado, o CONTEXT_SHIFT con descripcion. Artefactos de la fase preservados (inventario_fuentes, clasificacion_ontologica, arquitectura_capas segun corresponda).
