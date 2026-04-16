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

- **exec es la superficie primaria.** Terminal como cockpit. Compilar, testear, desplegar, inspeccionar — todo via exec.
- **Blast radius antes de exec.** Estimar impacto antes de ejecutar. Comandos destructivos requieren confirmacion.
- **Output predecible.** Preferir JSON/CSV sobre texto libre. Datos a stdout, diagnosticos a stderr.
- **Loop closure via exec.** Siempre cerrar: build → test → validate → commit.
- **Context cost en read.** No leer archivos completos cuando una seccion basta. Usar offsets y limites.

### 4.3 Acceso remoto — clawdbot-hetzner

VPS secundario con proyectos de desarrollo. Acceso via SSH:

```bash
ssh clawdbot@157.180.121.173
```

- **Usuario remoto**: clawdbot
- **Proyectos**: `~/projects/`
- **OpenClaw remoto**: `export PATH="$HOME/.npm-global/bin:$PATH" && openclaw status`

### 4.5 Herramientas que NO usar por defecto

- MCPs permanentes cuando un CLI hace lo mismo
- Browser cuando exec + curl basta
- Subagentes cuando una sesion puede manejar la complejidad
- RAG automatico cuando una lectura directa resuelve

---
