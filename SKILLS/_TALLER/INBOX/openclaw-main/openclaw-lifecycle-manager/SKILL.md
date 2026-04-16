---
name: openclaw-lifecycle-manager
description: Gestionar el ciclo de vida completo de agentes y skills OpenClaw — crear, validar, desplegar, operar, evolucionar, deprecar y retirar. Usar cuando la operacion cruza multiples fases del ciclo (diseno + deploy + operacion continua) o cuando se necesita orquestar la secuencia completa.
---

## Proposito

Orquestar el ciclo de vida end-to-end de agentes y skills OpenClaw usando procedimientos canonicos, verificando contra docs OMEGA en cada fase.

## Cuando se activa

- La operacion cruza dos o mas fases del ciclo (diseno + config, config + deploy, deploy + operacion).
- Se necesita deprecar o retirar un agente o skill de forma ordenada.
- Se requiere un roadmap completo de lifecycle para un artefacto nuevo.

## Ciclo de vida

### Agentes

| Fase | Descripcion | Skill o comando |
|------|-------------|-----------------|
| Disenar | Blueprint: identidad, topologia, canales, skills, config | `agent-designer` |
| Crear | Materializar workspace con archivos bootstrap | `write`/`edit` + checklist |
| Configurar | Derivar y aplicar `openclaw.json` | `agent-config` + `config-patcher` |
| Validar | `openclaw config validate` + `openclaw doctor` | CLI directo |
| Desplegar | Sincronizar workspace, instalar daemon, verificar health | `agent-deployer` |
| Operar | Restart, reload, logs, sesiones, cron | `operator` |
| Evolucionar | Cambios incrementales con validacion previa | `config-patcher` + `operator` |
| Deprecar | Deshabilitar canales, archivar workspace, notificar | `operator` |
| Retirar | `openclaw agents remove <name>` + limpiar workspace | CLI + `write` |

### Skills

| Fase | Descripcion | Mecanismo |
|------|-------------|-----------|
| Crear | Directorio `skills/<name>/SKILL.md` con frontmatter valido | `write` |
| Validar | `openclaw skills check` | CLI |
| Instalar | Agregar a `skills.entries` en `openclaw.json` via `config.patch` | `gateway` |
| Actualizar | Editar SKILL.md + verificar elegibilidad | `edit` + `openclaw skills list --eligible` |
| Deprecar | Eliminar entrada de `skills.entries` + archivar directorio | `config.patch` + `write` |

## Procedimiento

1. **Clasificar el objeto.** Agent o skill.
2. **Clasificar la fase.** Donde esta ahora y a donde debe llegar.
3. **Verificar precondiciones.** Leer docs OMEGA si hay duda sobre el procedimiento canonico.
4. **Ejecutar fase por fase.** Verificar con `openclaw doctor` o `openclaw config validate` al completar cada fase critica.
5. **Documentar estado.** Actualizar MEMORY.md con el nuevo estado operativo si es relevante.

## Reglas

- No mutar config ni workspace sin verificar precondiciones de la fase.
- Siempre rollback plan antes de cualquier fase destructiva (deprecar, retirar).
- Si una fase falla, diagnosticar antes de reintentar o escalar a la siguiente.
