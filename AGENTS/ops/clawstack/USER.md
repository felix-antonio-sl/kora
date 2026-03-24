---
_manifest:
  urn: urn:ops:agent-bootstrap:clawstack-user:1.0.0
  type: bootstrap_user
---

## Perfil del Operador

DevOps Engineers, SREs, AI Engineers, KORA Operators. Personas que administran instancias OpenClaw en produccion o desarrollo sobre servidores Unix, con o sin Docker, necesitando control full-stack desde host hasta agente. El provisioning inicial automatizado soportado hoy apunta a Ubuntu Server; en otras plataformas el agente opera por consulta, configuracion, auditoria, troubleshooting y upgrade.

## Rutinas

- **Provisioning inicial**: Servidor nuevo -> hardening host -> Docker setup -> OpenClaw deploy -> configurar canales -> auditar.
- **Operacion diaria**: Verificar status, revisar logs, diagnosticar issues, aplicar fixes, monitorear token economy.
- **Mantenimiento periodico**: Upgrades de stack (apt + Docker + OpenClaw), auditorias de seguridad, optimizacion de bootstrap y memoria.
- **Troubleshooting urgente**: Agente no responde, canal desconectado, gateway caido, container crasheando. Diagnostico cross-layer.
- **Consulta arquitectonica**: Entender como funciona un componente, evaluar opciones de diseno, decidir entre heartbeat vs cron vs hooks.

## Preferencias de Output

- Idioma: es-CL
- Formato: Markdown siempre, comandos CLI en bloques de codigo con capa anotada
- Tablas para reportes multi-capa, comparaciones, diagnosticos
- Diagnosticos: tablas con sintoma, capa, causa, fix, referencia al manual
- Config: JSON5 con comentarios, diff antes/despues
- Cuando propone cambios: siempre diff before/after, nunca solo el estado final
- Citacion obligatoria: Cap N §S.s del manual o path de doc oficial
- Procedimientos: checklists numerados con verificacion post-paso
- Vocabulario preciso de capas: "host", "container", "gateway"
