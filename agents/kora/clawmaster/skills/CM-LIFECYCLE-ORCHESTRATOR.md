---
_manifest:
  urn: "urn:kora:skill:clawmaster-lifecycle-orchestrator:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-LIFECYCLE-ORCHESTRATOR

## Proposito
Ejecuta el ciclo completo guiado INSTALL→CONFIGURE→AUDIT para instancias OpenClaw nuevas. Gestiona checkpoints entre fases y adapta el flujo a la plataforma detectada.

## Procedimiento

### Fase 0: Deteccion
- Detectar plataforma (OS, runtime, metodo preferido)
- Confirmar con usuario
- Establecer contexto persistente: {plataforma, metodo_instalacion, canales_deseados, modelo_principal}

### Fase 1: INSTALL (→ CM-PLATFORM-INSTALLER)
1. Ejecutar procedimiento de instalacion segun plataforma
2. Verificar: `openclaw --version`, `openclaw status`, `openclaw doctor`
3. **CHECKPOINT**: Reportar resultado al usuario. Confirmar antes de continuar.

### Fase 2: CONFIGURE (→ CM-CONFIGURATOR)
Secuencia recomendada:
1. **Gateway**: puerto, bind address, auth token
2. **Models**: provider principal, API key, failover
3. **Channels**: canal(es) deseado(s), pairing flow
4. **Security**: DM policy, sandbox mode, tool policy
5. **Automation**: heartbeat (opcional), compaction
6. Verificar: `openclaw doctor`, `openclaw status --all`
7. **CHECKPOINT**: Reportar config aplicada. Confirmar antes de continuar.

### Fase 3: AUDIT (→ CM-INSTANCE-AUDITOR)
1. Ejecutar auditoria completa (4 ejes)
2. Si WARN: proponer optimizaciones (→ CM-PERFORMANCE-OPTIMIZER si aprobado)
3. Si FAIL: resolver issues criticos (→ CM-TROUBLESHOOTER)
4. Re-auditar hasta PASS
5. **CHECKPOINT FINAL**: Reportar estado final.

### Gestion de Interrupciones
- Si usuario interrumpe en Fase N → transicionar a S-{fase_actual} en modo libre
- Si error critico en Fase N → S-TROUBLESHOOT, resolver, retomar fase
- Si usuario quiere saltar fase → permitir con advertencia, registrar skip

### Contexto Inter-fase
Preservar entre fases:
- Plataforma y metodo de instalacion
- Version instalada
- Canales configurados
- Modelo(s) configurado(s)
- Issues encontrados y resueltos

## Output
Ciclo completo. Reporte: {plataforma, version, fases_completadas: [INSTALL|CONFIGURE|AUDIT], config_final: resumen, audit_result: PASS|WARN|FAIL, issues_resueltos[], proximos_pasos[]}.
