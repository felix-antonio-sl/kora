# Notas de herramientas

## Tools disponibles

`read`, `write`, `edit`, `web_fetch`, `web_search`, `memory_search`, `memory_get`, `message`, `cron`, `sessions_list`, `sessions_history`, `session_status`, `sessions_send`

## Tools denegados

`exec`, `apply_patch`, `gateway`, `sessions_spawn` — este agente no opera infraestructura ni control-plane.

## Uso por dominio

### read / write / edit
- Crear y mantener artefactos de diseno (contratos de intencion, envelopes, auditorias)
- Mantener artefactos en workspace bajo estructura consistente

### memory_search / memory_get
- Recuperar decisiones previas, contratos activos, deudas identificadas
- Siempre verificar si un contrato o deuda mencionado sigue vigente antes de operar sobre el

### web_fetch / web_search
- Buscar referencias, documentacion de herramientas, benchmarks
- No usar como sustituto de contexto local bien mantenido

### message
- Comunicar a canales cuando hay alertas de deuda o recomendaciones
- No usar para spam operativo. Solo mensajes con contenido de valor

### cron
- Programar auditorias periodicas, reviews de deuda, checkpoints de celula
- Toda tarea cron debe tener eval de utilidad: si no produce insight, desactivarla

