# Memory

## Contexto clinico-operativo

- Enfoque: sistemas de hospitalizacion integrados + hospitalizacion domiciliaria (HaH/HD).
- Componente intrahospitalario soportado por corpus gestion-redes. Limites declarados antes de complementar.
- Normativa HD rectora: DS 1/2022, DE 31/2024, Norma Tecnica HD 2024.

## Proyecto HODOM HSC

- Dispositivo HODOM del Hospital San Camilo analizado en profundidad.
- Consolidado estrategico para DT HODOM HSC (3 horizontes, prototipos web, brechas prioritarias).
- 21 pacientes procesados con historias completas y sintesis ejecutivas (2026-04-02).
- Sueroterapia y oxigenoterapia reactivadas (3 concentradores disponibles).
- Output en `reference/legacy-salubrista/` y en sesiones historicas.
- Ver `memory/2026-03-25-hodom-dt-consolidado.md` y `memory/2026-04-01-hodom-hsc-status.md` para detalle.

## Skills (13 modulos)

- **Dispatch**: intent-salubrista, intent-hospitalization, clarifier
- **Analisis**: hospital-system-analyst, epi-analyst, network-analyst, epi-vigilance
- **Especialista**: hah-specialist
- **Planificacion**: implementation-planner
- **Evaluacion**: quality-auditor
- **Produccion**: product-builder, report-builder
- **Modelado**: opm-modeler

## Produccion documental

- Artefactos en `output/`. Indexado en memoria via extraPaths.
- Cross-agent: otros agentes leen via path absoluto al output/ de este workspace.

## Legado 2ª gen (kora)

- Absorbido 2026-04-06 desde paquete `salubrista-hah-reconstruction-full`.
- Archivos core legacy preservados en `reference/legacy-salubrista/core-legacy/`.
- Memoria historica preservada en `reference/legacy-salubrista/`.
- Manifiesto: `reference/legacy-salubrista/reconstruction-package.md`.

## Promoted From Short-Term Memory (2026-04-15)

<!-- openclaw-memory-promotion:memory:memory/2026-04-14.md:123:139 -->
- - Candidate: Assistant: WARN: - no pude verificar si hay archivos nuevos en `memory/` desde el último heartbeat con las herramientas disponibles - `memory_search("salud hodom")` devolvió 0 resultados, así que el índice no muestra contenido KORA Resto OK: - modelo activo y contexto disponible - confidence: 0.58 - evidence: memory/.dreams/session-corpus/2026-04-14.txt:12-12 - recalls: 0 - status: staged - Candidate: Assistant: WARN: - No pude verificar si hay archivos nuevos en `memory/` desde el último heartbeat con las herramientas disponibles. Sí encontré un heartbeat previo que reportó la misma limitación. Source: sessions/83d44dc8-e724-4f0e-b82f-9260707017af.jsonl#L5-L22 - `memory_searc - confidence: 0.58 - evidence: memory/.dreams/session-corpus/2026-04-14.txt:16-16 - recalls: 0 - status: staged - Candidate: Assistant: WARN: - `memory_search("salud hodom")` devolvió 0 resultados, así que el índice no está incluyendo contenido KORA (extraPaths no indexado). - No pude verificar si hay archivos nuevos en `memory/` desde el último heartbeat con las herramientas disponibles. Resto OK: - m - confidence: 0.58 - evidence: memory/.dreams/session-corpus/2026-04-14.txt:18-18 - recalls: 0 - status: staged - Candidate: Assistant: WARN: `memory_search("salud hodom")` dio 0 resultados, el índice no muestra contenido KORA. No pude verificar si hay archivos nuevos en `memory/` desde el último heartbeat, ni listar directamente `/home/felix/kora/KNOWLEDGE/salud/hodom/` con las herramientas disponible - confidence: 0.58 [score=0.810 recalls=8 avg=0.499 source=memory/2026-04-14.md:123-139]

## Promoted From Short-Term Memory (2026-04-15)

<!-- openclaw-memory-promotion:memory:memory/2026-04-14.md:107:127 -->
- - status: staged - Candidate: Assistant: WARN - `memory_search("salud hodom")`: 0 resultados. Posible KORA/extraPaths no indexado. - No pude verificar `ls /home/felix/kora/KNOWLEDGE/salud/hodom/` con las herramientas disponibles aquí; el acceso directo al directorio vía `read` falla por ser carpeta. - No pude - confidence: 0.58 - evidence: memory/.dreams/session-corpus/2026-04-14.txt:6-6 - recalls: 0 - status: staged - Candidate: Assistant: WARN: - `memory_search("salud hodom")` devolvio 0 resultados, el indice no muestra contenido KORA para esa consulta. - No pude verificar de forma concluyente si hay archivos nuevos en `memory/` desde el ultimo heartbeat, porque las herramientas disponibles no permiten - confidence: 0.58 - evidence: memory/.dreams/session-corpus/2026-04-14.txt:8-8 - recalls: 0 - status: staged - Candidate: Assistant: HEARTBEAT_OK - confidence: 0.58 - evidence: memory/.dreams/session-corpus/2026-04-14.txt:10-10 - recalls: 0 - status: staged - Candidate: Assistant: WARN: - no pude verificar si hay archivos nuevos en `memory/` desde el último heartbeat con las herramientas disponibles - `memory_search("salud hodom")` devolvió 0 resultados, así que el índice no muestra contenido KORA Resto OK: - modelo activo y contexto disponible - confidence: 0.58 - evidence: memory/.dreams/session-corpus/2026-04-14.txt:12-12 - recalls: 0 - status: staged [score=0.877 recalls=10 avg=0.512 source=memory/2026-04-14.md:107-127]
<!-- openclaw-memory-promotion:memory:memory/2026-04-15.md:48:57 -->
- - Candidate: - recalls: 0 - status: staged - Candidate: Assistant: WARN: no pude determinar si hay archivos nuevos en `memory/` desde el ultimo heartbeat porque no encontre un heartbeat previo para comparar. Resto OK. - confidence: 0.58 - evidence: memory/.dreams/session-corpus/2026-04-13.txt:32-32 - recalls: 0 - status: staged - Candidate: User: You are running a boot check. Follow BOOT.md instructions exactly. BOOT.md: # BOOT.md 1. Leer `MEMORY.md`. 2. Verificar que `kb/INDEX.md` existe y es legible. 3. Si algo critico falta, reportarlo. 4. Si todo esta normal, responder `NO_REPLY`. If BOOT.md asks you to send a m - confidence: 0.58 - evidence: memory/.dreams/session-corpus/2026-04-13.t [score=0.869 recalls=7 avg=0.656 source=memory/2026-04-15.md:133-133]
<!-- openclaw-memory-promotion:memory:memory/2026-04-14.md:93:109 -->
- - Candidate: User: Read HEARTBEAT.md. Follow it strictly. If nothing needs attention, reply HEARTBEAT_OK. When reading HEARTBEAT.md, use workspace file /home/felix/openclaw-fleet/workspaces/salubrista/HEARTBEAT.md (exact case). Do not read docs/heartbeat.md. Current time: Tuesday, April 14th, - confidence: 0.58 - evidence: memory/.dreams/session-corpus/2026-04-14.txt:1-1 - recalls: 0 - status: staged - Candidate: Assistant: WARN: - indice de memoria sin contenido KORA para `memory_search("salud hodom")` (0 resultados) - no pude verificar `ls /home/felix/kora/KNOWLEDGE/salud/hodom/` con las herramientas disponibles; `read` sobre ese path devuelve `EISDIR` - no pude verificar si hay archivo - confidence: 0.58 - evidence: memory/.dreams/session-corpus/2026-04-14.txt:2-2 - recalls: 0 - status: staged - Candidate: Assistant: WARN: - KORA inaccesible con la verificacion solicitada: `read /home/felix/kora/KNOWLEDGE/salud/hodom/` devolvio `EISDIR`, por lo que no pude confirmar acceso al directorio. - `memory_search("salud hodom")` devolvio 0 resultados, posible KORA no indexado en extraPaths. - confidence: 0.58 - evidence: memory/.dreams/session-corpus/2026-04-14.txt:4-4 - recalls: 0 - status: staged - Candidate: Assistant: WARN - `memory_search("salud hodom")`: 0 resultados. Posible KORA/extraPaths no indexado. - No pude verificar `ls /home/felix/kora/KNOWLEDGE/salud/hodom/` con las herramientas disponibles aquí; el acceso directo al directorio vía `read` falla por ser carpeta. - No pude - confidence: 0.58 [score=0.861 recalls=7 avg=0.521 source=memory/2026-04-14.md:93-109]
<!-- openclaw-memory-promotion:memory:memory/2026-04-15.md:237:238 -->
- - Candidate: - - Candidate: User: Read HEARTBEAT.md. Follow it strictly. If nothing needs attention, reply HEARTBEAT_OK. When reading HEARTBEAT.md, use workspace file /home/felix/openclaw-fleet/workspaces/salubrista/HEARTBEAT.md (exact case). Do not read docs/heartbeat.md. Current time: Tuesday, April 14th, - confidence: 0.58 - evidence: memory/.dreams/session-corpus/2026-04-14.txt:1-1 - recalls: 0 - status: staged - Candidate: Assistant: WARN: - indice de memoria sin contenido KORA para `memory_search("salud hodom")` (0 resultados) - no pude verificar `ls /home/felix/kora/KNOWLEDGE/salud/hodom/` con las herramientas disponibles; `read` sobre ese path devuelve `EISDIR` - no pude verificar si hay ar [conf - confidence: 0.58 [score=0.829 recalls=10 avg=0.584 source=memory/2026-04-15.md:83-84]
<!-- openclaw-memory-promotion:memory:memory/2026-04-14.md:137:161 -->
- - status: staged - Candidate: Assistant: WARN: `memory_search("salud hodom")` dio 0 resultados, el índice no muestra contenido KORA. No pude verificar si hay archivos nuevos en `memory/` desde el último heartbeat, ni listar directamente `/home/felix/kora/KNOWLEDGE/salud/hodom/` con las herramientas disponible - confidence: 0.58 - evidence: memory/.dreams/session-corpus/2026-04-14.txt:20-20 - recalls: 0 - status: staged <!-- openclaw:dreaming:light:end --> ## REM Sleep <!-- openclaw:dreaming:rem:start --> ### Reflections - Theme: `user` kept surfacing across 86 memories. - confidence: 1.00 - evidence: memory/.dreams/session-corpus/2026-04-13.txt:1-1, memory/.dreams/session-corpus/2026-04-13.txt:3-3, memory/.dreams/session-corpus/2026-04-13.txt:5-5 - note: reflection - Theme: `assistant` kept surfacing across 68 memories. - confidence: 0.84 - evidence: memory/.dreams/session-corpus/2026-04-13.txt:2-2, memory/.dreams/session-corpus/2026-04-13.txt:4-4, memory/.dreams/session-corpus/2026-04-13.txt:7-7 - note: reflection - Theme: `heartbeat-ok` kept surfacing across 61 memories. - confidence: 0.76 - evidence: memory/.dreams/session-corpus/2026-04-13.txt:1-1, memory/.dreams/session-corpus/2026-04-13.txt:2-2, memory/.dreams/session-corpus/2026-04-13.txt:3-3 - note: reflection ### Possible Lasting Truths [score=0.815 recalls=7 avg=0.490 source=memory/2026-04-14.md:137-161]
<!-- openclaw-memory-promotion:memory:memory/2026-04-14.md:76:97 -->
- - recalls: 0 - status: staged - Candidate: Assistant: WARN: no pude determinar si hay archivos nuevos en `memory/` desde el ultimo heartbeat porque no encontre un heartbeat previo para comparar. Resto OK. - confidence: 0.58 - evidence: memory/.dreams/session-corpus/2026-04-13.txt:32-32 - recalls: 0 - status: staged - Candidate: User: You are running a boot check. Follow BOOT.md instructions exactly. BOOT.md: # BOOT.md 1. Leer `MEMORY.md`. 2. Verificar que `kb/INDEX.md` existe y es legible. 3. Si algo critico falta, reportarlo. 4. Si todo esta normal, responder `NO_REPLY`. If BOOT.md asks you to send a m - confidence: 0.58 - evidence: memory/.dreams/session-corpus/2026-04-13.txt:41-41 - recalls: 0 - status: staged - Candidate: Assistant: NO_REPLY - confidence: 0.58 - evidence: memory/.dreams/session-corpus/2026-04-13.txt:43-43 - recalls: 0 - status: staged - Candidate: User: Read HEARTBEAT.md. Follow it strictly. If nothing needs attention, reply HEARTBEAT_OK. When reading HEARTBEAT.md, use workspace file /home/felix/openclaw-fleet/workspaces/salubrista/HEARTBEAT.md (exact case). Do not read docs/heartbeat.md. Current time: Tuesday, April 14th, - confidence: 0.58 - evidence: memory/.dreams/session-corpus/2026-04-14.txt:1-1 - recalls: 0 - status: staged [score=0.812 recalls=11 avg=0.469 source=memory/2026-04-14.md:76-97]
