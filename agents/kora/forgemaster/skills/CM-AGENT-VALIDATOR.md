---
_manifest:
  urn: urn:kora:skill:forgemaster-agent-validator:2.0.0
  type: lazy_load_endofunctor
version: 2.0.0
status: published
lang: es
---

# CM-AGENT-VALIDATOR

## Proposito
Valida un workspace KORA completo contra agent-spec-md v8.3.0 §9 y skill-spec-md v3.4.0 §7, produciendo un reporte trazable a la spec publicada.

## Input/Output
- **Input:** agent_path: string (ruta al workspace del agente)
- **Output:** ValidationReport (ver Signature Output)

## Procedimiento
1. **GRAMATICA DE BEHAVIOR (§3.1):** `AGENTS.md` contiene FSM, Reglas Duras, Co-induccion, Contexto Multi-turno y Wiring en orden canonico.
2. **FSM CANONICA (§3.2):** Estados `S-*`, transiciones explicitas, `S-DISPATCHER` y `S-END` presentes.
3. **BEHAVIOR PURO (§3.3):** `AGENTS.md` expresa control puro sin fenomenologia ni security inline.
4. **SEGREGACION DE COMPONENTES (§3.4):** `SOUL.md`, `USER.md`, `TOOLS.md` y `config.json` conservan su rol sin contaminacion cruzada.
5. **TOPOLOGIA OBLIGATORIA (§2):** Existen los 5 componentes base y el directorio `skills/`.
6. **INTERFAZ CERRADA (§4):** `TOOLS.md` coincide con `config.json.tools.allow`.
7. **RUNTIME SEGREGADO (§4-§5):** `runtime_capabilities` no reintroduce interfaz semantica.
8. **CONFIG VALIDO (§5):** `config.json` respeta schema, envelope y limites declarados.
9. **SKILLS RESOLUBLES (§6):** Todo `CM-*` referido en `AGENTS.md` existe en `skills/`.
10. **CM CORE CANONICO (skill-spec-md §3):** Cada Skill degenerado conserva `Proposito`, `Input/Output`, `Procedimiento`, `Signature Output`.
11. **SKILL PURITY (skill-spec-md §6):** El Skill no introduce FSM, wiring ni control conversacional impropio.
12. **ROUTING RESOLUBLE (§7):** Toda ruta a otro agente apunta a un workspace real.
13. **TRAZABILIDAD VALIDA:** `Traces to:` referencia la formal layer oficial con anclas existentes.
14. **BASELINE DE SKILLS (skill-spec-md §6):** El workspace no presenta Skills extendidos como capacidad vigente del repo.

Por cada check: clasificar PASS, FAIL(ERROR — bloqueo) o WARN(WARNING — recomendacion) o SKIP (no aplica, con justificacion).

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| resultado | PASS\|FAIL | PASS si 0 ERRORs, FAIL si >=1 ERROR |
| checks | {id: int, nombre: string, veredicto: PASS\|FAIL\|WARN\|SKIP, detalle: string}[] | Resultado de cada check trazado a la spec publicada |
| issues | {severidad: ERROR\|WARNING, componente: string, campo: string, mensaje: string, correccion: string}[] | Lista de issues encontrados con correcciones accionables |
| resumen | string | Conteo resumido por veredicto |
