# Bootstrap — kora/korax

## Pre-requisitos

- Container kora-personal healthy
- PCA sidecar (kora-pca) healthy y accesible en http://kora-pca:8100/api
- Red kora-federation conectada
- Config aplicada con heartbeat y cron habilitados
- Workspace montado con MEMORY.md, HEARTBEAT.md, skills/

## Inicialización post-deploy

1. Verificar runtime: gateway responde en puerto 18789
2. Verificar PCA: GET http://kora-pca:8100/api/estado devuelve JSON válido
3. Verificar memoria: MEMORY.md existe y memory search habilitado
4. Verificar skills: 12 CMs presentes en skills/
5. Verificar cron jobs: morning_plan, evening_close, biweekly_sync, abandonment_check, collapse_monitor activos
6. Verificar heartbeat: ejecutándose cada 30min en horario activo

## Post-recovery

1. Verificar que el volume kora-personal-data persiste
2. Confirmar que PCA DB no se corrompió (backup en /home/node/srv-kora/backups/)
3. Ejecutar GET /api/estado para validar estado del sistema
4. Verificar conectividad hooks con el resto de la federación

## Contacto de emergencia

- Operador: Ominono (Telegram 7192195698)
