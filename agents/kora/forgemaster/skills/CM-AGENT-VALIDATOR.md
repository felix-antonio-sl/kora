---
_manifest:
  urn: "urn:kora:skill:forgemaster-agent-validator:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-AGENT-VALIDATOR

## Proposito
Valida un workspace KORA completo contra agent-spec-md v5.0.0, produciendo reporte con correcciones accionables.

## Procedimiento
1. TOPOLOGIA (§4): Verificar presencia de 5 archivos obligatorios (AGENTS.md, SOUL.md, USER.md, TOOLS.md, config.json) + directorio skills/.
2. FRONTMATTER: Cada archivo tiene _manifest con urn valido y type correcto (bootstrap_agents, bootstrap_soul, bootstrap_user, bootstrap_tools).
3. SEGREGACION (§3):
   - AGENTS.md: Solo FSM, reglas, co-induccion. SIN fenomenologia, SIN policies detalladas.
   - SOUL.md: Solo identidad, paradigma, tono. SIN logica FSM (IF→STATE).
   - USER.md: Solo perfil, rutinas, preferencias. SIN logica FSM, SIN fenomenologia.
   - TOOLS.md: Solo firmas inferenciales. SIN implementacion.
   - config.json: Solo constraints pre-compiladas. JSON valido.
4. FSM DETERMINISMO: Transiciones con IF→S-STATE explicito. Sin ambiguedad. Minimo S-DISPATCHER + S-END.
5. FSM ALCANZABILIDAD: Todos los estados alcanzables desde S-DISPATCHER. S-END es terminal.
6. CO-INDUCCION: Nodo terminal tiene checklist pre-output y protocolo correccion.
7. URNs: Formato urn:{ns}:agent-bootstrap:{nombre}-{componente}:{version}. Resolubles via catalogo.
8. TOKEN ECONOMY: Skills declarados como lazy-load. No todo cargado en bootstrap.
9. COMPLETITUD: Todas las secciones obligatorias presentes en cada archivo.
10. Por cada falla: clasificar ERROR(bloqueo) o WARNING(recomendacion), indicar componente+campo+correccion.

## Output
Reporte: {resultado: PASS|FAIL, issues: [{severidad: ERROR|WARNING, componente, campo, mensaje, correccion}]}. Si PASS → agente listo. Si FAIL → lista correcciones para S-OPERATE.
