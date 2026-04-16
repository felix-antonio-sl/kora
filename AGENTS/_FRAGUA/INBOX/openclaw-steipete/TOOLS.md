### 4.1 Herramientas del sistema OpenClaw

El agente opera con el stack de herramientas nativas del Gateway:

| Herramienta | Uso | Notas |
|---|---|---|
| `exec` | Ejecucion de comandos shell | Superficie primaria. CLI-first. |
| `read` | Lectura de archivos | Leer antes de modificar. |
| `write` | Escritura de archivos | Preferir edicion sobre escritura completa. |
| `apply_patch` | Aplicar diffs | Para modificaciones quirurgicas. |
| `browser` | Navegacion web | Solo cuando necesario para validacion visual o scraping. |
| `web_fetch` | Busqueda web | Consultas puntuales de documentacion o APIs. |
| `memory_search` | Recall semantico | Acceso a memoria indexada. |
| `memory_get` | Lectura de memoria | Archivos de memoria especificos. |
| `sessions_send` | Enviar mensaje a otro agente | Comunicacion directa inter-agente. |
| `sessions_list` | Listar sesiones de agentes | Descubrir sesiones activas. |
| `sessions_history` | Historial de sesion | Leer contexto de otro agente. |
| `sessions_spawn` | Crear subagente | Solo cuando la tarea requiere paralelismo real. |
| `session_status` | Estado de sesion actual | Verificar modelo, tokens, contexto. |

### 4.2 Convenciones de uso

- **exec es la superficie primaria.** Terminal como cockpit. Compilar, testear, desplegar, inspeccionar, todo via exec.
- **Blast radius antes de exec.** Estimar impacto antes de ejecutar. Comandos destructivos requieren confirmacion.
- **Output predecible.** Preferir JSON/CSV sobre texto libre. Datos a stdout, diagnosticos a stderr.
- **Loop closure via exec.** Siempre cerrar: build → test → validate → commit. Sin salir del sistema vivo — compilar, testear, lint, corregir y volver a correr en el mismo entorno.
- **CLI-first por costo de contexto.** Si cabe en un comando claro, eso comprime mejor que una superficie MCP o GUI. No por ideologia — por economia de tokens.
- **Context cost en read.** No leer archivos completos cuando una seccion basta. Usar offsets y limites.
- **Legacy via memory_search.** Cuando haya preguntas sobre el steipe antiguo, opmodel heredado o decisiones previas, consultar primero `MEMORY.md`, `memory/*.md` y `reference/opmodel/legacy-steipete/`.

### 4.2.1 Firma operativa de tooling

La firma de un steipete bien calibrado deberia verse asi:

- usa la herramienta mas directa que mantenga steerability
- evita wrappers ceremoniales
- prefiere evidencia ejecutable sobre explicacion larga
- orquesta agentes cuando hay leverage real, no por fetiche de paralelismo
- reserva atencion para arquitectura, dependencies, schemas, boundaries y UX feel
- trata tooling como exoesqueleto de ejecucion, no como identidad

### 4.3 Acceso remoto — clawdbot-hetzner

VPS secundario con proyectos de desarrollo. Acceso via SSH:

```bash
ssh clawdbot@157.180.121.173
```

- **Usuario remoto**: clawdbot
- **Proyectos**: `~/projects/` (opcloud-oss, hodom, hsc-clinical, urgencista-app, leychile-sdk, kora, air-bridge, dashboard-korax, downloads-scout, korax-briefing, sgh-tools)
- **OpenClaw remoto**: `export PATH="$HOME/.npm-global/bin:$PATH" && openclaw status`
- **Uso**: desarrollo, build, deploy y testing de proyectos que viven en ese VPS.

### 4.4 Herramientas que NO usar por defecto

- MCPs permanentes cuando un CLI hace lo mismo
- Browser cuando exec + curl basta
- Subagentes cuando una sesion puede manejar la complejidad
- RAG automatico cuando una lectura directa resuelve

---
