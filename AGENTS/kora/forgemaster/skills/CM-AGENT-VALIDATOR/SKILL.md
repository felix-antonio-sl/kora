---
_manifest:
  urn: urn:kora:skill:forgemaster-agent-validator:2.0.0
  type: lazy_load_endofunctor
version: 2.0.0
status: published
lang: es
extensions:
  kora:
    skill:
      form: extended
      allowed_tools:
        - health_check
        - workspace_read
        - spec_consult
      requires: []
      scripts:
        - scripts/validate_workspace.py
      references:
        - references/validation-stack.md
      assets:
        - assets/validation-report-template.md
---

# CM-AGENT-VALIDATOR

## Proposito
Valida un workspace KORA completo contra agent-spec-md v8.4.0 §9, skill-spec-md v4.0.0 §7 y gobernanza.md v3.2.0 §9, produciendo un reporte trazable al baseline publicado y apoyandose en el stack validado del repo cuando conviene ejecutar verificacion mecanica reproducible.

## Input/Output
- **Input:** agent_path: string (ruta al workspace del agente)
- **Output:** ValidationReport (ver Signature Output)

## Procedimiento
1. Cargar el baseline normativo desde `references/validation-stack.md` para fijar spec rectora, schemas y soporte de auditoria disponibles.
2. Si se requiere verificacion mecanica detallada del workspace, usar `scripts/validate_workspace.py` como envoltorio reproducible del stack existente en `scripts/kora_lib/`.
3. **GRAMATICA DE BEHAVIOR (agent-spec-md §4.1):** `AGENTS.md` contiene FSM, Reglas Duras, Co-induccion, Contexto Multi-turno y Wiring en orden canonico.
4. **FSM CANONICA (agent-spec-md §4.2-§4.3):** Estados `S-*`, transiciones explicitas, determinismo declarado, `S-DISPATCHER` y `S-END` presentes.
5. **TOPOLOGIA OBLIGATORIA (agent-spec-md §3):** Existen los 5 componentes base y el directorio `skills/`.
6. **SEGREGACION DE COMPONENTES (agent-spec-md §4.4):** `SOUL.md`, `USER.md`, `TOOLS.md` y `config.json` conservan su rol sin contaminacion cruzada.
7. **BEHAVIOR PURO (agent-spec-md §4.3):** `AGENTS.md` expresa control puro sin fenomenologia ni security inline.
8. **INTERFAZ CERRADA (agent-spec-md §5):** `TOOLS.md` coincide con `config.json.tools.allow`.
9. **RUNTIME SEGREGADO (agent-spec-md §5-§6):** `runtime_capabilities` no reintroduce interfaz semantica y el envelope no contamina la interfaz.
10. **CONFIG VALIDO (agent-spec-md §6):** `config.json` respeta schema, envelope y limites declarados.
11. **SKILLS RESOLUBLES (agent-spec-md §7):** Todo `CM-*` referido en `AGENTS.md` resuelve a `skills/CM-*.md` o `skills/CM-*/SKILL.md`.
12. **UNICIDAD DE MATERIALIZACION (skill-spec-md §3):** Un mismo identificador `CM-*` no coexiste como archivo degenerado y como directorio extendido.
13. **CM CORE CANONICO (skill-spec-md §3):** Cada Skill, degenerado o extendido, conserva `Proposito`, `Input/Output`, `Procedimiento`, `Signature Output`.
14. **SKILL PURITY (skill-spec-md §3 y §6):** El Skill no introduce FSM, wiring ni control conversacional impropio.
15. **BUNDLE GOBERNADO (skill-spec-md §3 y §7):** Si existe `skills/CM-*/SKILL.md`, sus fibras adjuntas viven solo bajo `scripts/`, `references/`, `assets/`, sin identidad ni kind propios.
16. **METADATA ACOTADA (gobernanza.md §6, skill-spec-md §3):** La metadata del bundle vive en `extensions.{namespace}.skill` del entrypoint `SKILL.md`.
17. **ROUTING RESOLUBLE (agent-spec-md §8):** Toda ruta a otro agente apunta a un workspace real.
18. **TRAZABILIDAD VALIDA (gobernanza.md §5 y §8):** `Traces to:` usa solo la Formal Layer oficial y anclas `formal/{doc} §{seccion}`; si la comprobacion efectiva depende del baseline/tooling publicado, declarar ese alcance en el reporte.
19. Emitir el resultado final siguiendo la estructura de `assets/validation-report-template.md`.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| resultado | PASS\|FAIL | PASS si 0 ERRORs, FAIL si >=1 ERROR |
| checks | {id: int, nombre: string, veredicto: PASS\|FAIL\|WARN\|SKIP, detalle: string}[] | Resultado de cada check trazado a la spec publicada |
| issues | {severidad: ERROR\|WARNING, componente: string, campo: string, mensaje: string, correccion: string}[] | Lista de issues encontrados con correcciones accionables |
| resumen | string | Conteo resumido por veredicto |
