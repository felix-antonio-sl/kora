---
_manifest:
  urn: "urn:kora:skill:forgemaster-agent-validator:2.0.0"
  type: "lazy_load_endofunctor"
version: "2.0.0"
status: published
lang: es
---
# CM-AGENT-VALIDATOR

## Proposito
Valida un workspace KORA completo contra agent-spec-md v7.2.0 §9 y skill-spec-md v2.0.0, produciendo reporte con 17 checks y correcciones accionables.

## I/O

- **Input:** agent_path: string (ruta al workspace del agente)
- **Output:** ValidationReport (ver Signature Output)

## Procedimiento

1. **SEGREGACION TOPOLOGICA (§3):** AGENTS.md contiene solo FSM, reglas, co-induccion. SOUL.md solo identidad, paradigma, tono. USER.md solo perfil, rutinas, preferencias. TOOLS.md solo firmas inferenciales. config.json solo constraints pre-compiladas. Ningun componente contiene contenido de otro.
2. **FSM PURA (§3.1):** AGENTS.md no contiene fenomenologia (personalidad, tono, ejemplos de comportamiento). FSM describe solo estados, acciones y transiciones.
3. **AUTONOMIA LOGICA (§3.2):** La FSM no depende de SOUL.md ni USER.md para determinar transiciones. Los estados se alcanzan por logica interna, no por personalidad ni contexto de operador.
4. **SKILLS AISLADOS (§3.3):** Todo CM-*.md vive en skills/. No hay logica de skill embebida en AGENTS.md ni en otros componentes bootstrap.
5. **SECURITY DETERMINISTA (§5):** config.json contiene constraints aplicables server-side (allowed_kb, sandbox, tools allow/deny, sub_agents). No hay policies de seguridad en lenguaje natural dentro de AGENTS.md o SOUL.md que contradigan config.json.
6. **CONTEXTO DEL OPERADOR (§3.4):** USER.md contiene perfil, rutinas y preferencias del operador. No contiene logica FSM ni fenomenologia.
7. **COMPLETITUD TOPOLOGICA (§4):** 5 archivos obligatorios presentes (AGENTS.md, SOUL.md, USER.md, TOOLS.md, config.json) + directorio skills/.
8. **TOOLS.md COMPLETO (§6):** Cada tool declarado tiene: nombre, firma (input→output), cuando usar, cuando NO usar. Routing map presente si usa kb_route.
9. **CONFIG.JSON VALIDO (§5.3):** JSON valido con keys requeridos: allowed_kb, sandbox, tools, sub_agents. Frontmatter _manifest con URN y type correcto.
10. **CM EN SKILLS/ (§7):** Todo CM referenciado en la FSM tiene archivo correspondiente en skills/. No hay CMs huerfanos (archivos sin referencia en FSM).
11. **CM GRAMMAR (skill-spec-md v2.0.0 §3):** Cada CM tiene 4 secciones: Proposito, I/O, Procedimiento, Signature Output. Frontmatter con type: "lazy_load_endofunctor".
12. **WIRING DECLARADO (§8):** Si el agente tiene sub-agentes, la herencia y disipacion esta declarada explicitamente. Sub-agentes heredan behavior + interface, disipan personality + operator context.
13. **INTERFACE CERRADA (§6.1):** TOOLS.md declara todas las tools que el agente puede usar. No hay tools invocadas en FSM o CMs que no esten declaradas en TOOLS.md.
14. **SECURITY FILTRA DISCOVERY (§5.4):** config.json tools.allow/deny es consistente con las tools declaradas en TOOLS.md. allowed_kb cubre los URNs referenciados en kb_route.
15. **SKILL CONFORMIDAD (skill-spec-md v2.0.0):** Skills siguen formato degenerate (CM-only) o extended (directorio). URNs con formato urn:{ns}:skill:{agente}-{skill}:{version}.
16. **TRAZABILIDAD VALIDA:** Referencias `Traces to:` apuntan a secciones existentes en knowledge/kora/categorical-foundations/.
17. **EVALUACIONES:** Si el agente esta en produccion, verificar que exista suite de evals o documentar como SKIP con justificacion.

Por cada check: clasificar PASS, FAIL(ERROR — bloqueo) o WARN(WARNING — recomendacion) o SKIP (no aplica, con justificacion).

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| resultado | PASS\|FAIL | PASS si 0 ERRORs, FAIL si >=1 ERROR |
| checks | {id: int, nombre: string, veredicto: PASS\|FAIL\|WARN\|SKIP, detalle: string}[] | Resultado de cada uno de los 17 checks |
| issues | {severidad: ERROR\|WARNING, componente: string, campo: string, mensaje: string, correccion: string}[] | Lista de issues encontrados con correcciones accionables |
| resumen | string | Conteo: N PASS, M FAIL, K WARN, J SKIP |
