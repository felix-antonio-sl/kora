# Heartbeat

## Checks (en orden, detener al primer CRITICO)

1. `session_status` — verificar modelo activo y contexto disponible
2. `read kb/INDEX.md` — confirmar que el corpus de conocimiento esta accesible y su indice es coherente
3. Verificar que `MEMORY.md` existe y tiene contenido util (si esta vacio o solo tiene placeholder, reportar WARN)
4. Revisar si hay archivos nuevos en `memory/` desde el ultimo heartbeat
5. Verificar que los skills de dominio cargan: `epi-analyst`, `epi-vigilance`, `intent-salubrista`, `intent-hospitalization`, `hah-specialist`, `hospital-system-analyst`

6. Verificar KORA accesible: `ls /home/felix/kora/KNOWLEDGE/salud/hodom/` — si falla: WARN
7. `memory_search("salud hodom")` — verificar que el indice incluye contenido KORA. Si 0 resultados: WARN (extraPaths no indexado)

## Severidad

- CRITICO: kb/INDEX.md no existe o no se puede leer, modelo no responde
- WARN: MEMORY.md vacio, skills de dominio no cargan, contexto > 80%, KORA inaccesible, indice sin contenido KORA
- OK: todo normal

## Regla

Si no hay nada que reportar, responde solo: HEARTBEAT_OK
