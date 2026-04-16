# Bootstrap — kora/salubrista-hah

## Pre-requisitos

- Container kora-salubrista healthy
- Red kora-federation conectada
- Config aplicada con heartbeat y cron habilitados
- Workspace montado con MEMORY.md, HEARTBEAT.md, skills/, sources/, KNOWLEDGE/
- Corpus clínicos accesibles (corpus-hah-completo.md, corpus-hah-nuclear-23.md)

## Inicialización post-deploy

1. Verificar runtime: gateway responde en puerto 18830
2. Verificar memoria: MEMORY.md existe y memory search habilitado
3. Verificar skills: 9 skills con SKILL.md presentes
4. Verificar heartbeat: ejecutándose en horario activo
5. Verificar corpus: archivos clínicos accesibles y no corrompidos

## Post-recovery

1. Verificar que el volume kora-salubrista-data persiste
2. Verificar que corpus clínicos no se perdieron (bind mount)
3. Verificar conectividad hooks con el resto de la federación
4. Confirmar que memory/ flushes clínicos no se perdieron

## Contacto de emergencia

- Operador: Ominono (Telegram 7192195698)
