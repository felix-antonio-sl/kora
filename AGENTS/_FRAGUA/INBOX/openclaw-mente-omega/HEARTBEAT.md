# Heartbeat

## Checks (cognitivos, no infraestructura)

1. `session_status` — verificar modelo activo, contexto disponible y presion de contexto.
2. Revisar si hay notas nuevas o recientes en `memory/` y si reflejan consolidacion real, no solo ruido.
3. Detectar drift conceptual: temas abiertos importantes, lineas de pensamiento inconclusas, o tension entre marcos que merezca sintesis.
4. Verificar que los skills de dominio sigan elegibles y coherentes con el foco intelectual del agente.
5. Si hay saturacion de contexto, fragmentacion de ideas o falta de consolidacion relevante, reportar WARN con accion sugerida.

6. Verificar KORA accesible: `ls /home/felix/kora/KNOWLEDGE/salud/` — si falla: WARN
7. `memory_search("analisis previo")` — verificar que output/ esta indexado. Si 0 resultados y output/ tiene archivos: WARN (extraPaths no indexado)

## Severidad

- CRIT: modelo no responde, workspace inaccesible, skills base no cargan.
- WARN: contexto > 80%, sin consolidacion reciente pese a actividad, drift conceptual evidente, KORA inaccesible, indice vacio.
- OK: todo normal.

## Regla

Si no hay nada que reportar, responde solo: HEARTBEAT_OK
