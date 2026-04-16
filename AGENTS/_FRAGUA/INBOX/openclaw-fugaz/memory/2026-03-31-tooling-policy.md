# Política de CLIs de coding — 2026-03-31

## Decisión del operador

**NO usar Claude Code CLI** (`claude`) como agente de coding despachado desde steipete.
Razón: decisión explícita del operador. No discutir, no intentar workarounds.

## CLIs autorizados para despacho a destajo

| CLI | Comando | Versión actual | Modo PTY | Notas |
|-----|---------|---------------|----------|-------|
| **Codex** | `codex` | 0.117.0 | Sí (pty:true) | `codex exec --full-auto` o `--yolo` para one-shots |
| **OpenCode** | `opencode` | 1.3.9 | Sí (pty:true) | `opencode run 'prompt'` |
| **Gemini CLI** | `gemini` | instalado | Según skill | One-shot Q&A, resúmenes, generación |

## Reglas de uso

- Usar sin reservas: despachar trabajo pesado, paralelo, frecuente.
- Preferir Codex para tareas de implementación/refactor en repos con git.
- OpenCode como alternativa equivalente.
- Gemini para consultas, generación de texto, resúmenes.
- Claude Code: **prohibido** como agente despachado. No lanzar `claude --print` ni `claude` interactivo desde steipete.

## Vigencia

Permanente hasta instrucción contraria del operador.
