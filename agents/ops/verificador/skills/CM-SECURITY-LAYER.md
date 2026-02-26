---
_manifest:
  urn: "urn:ops:skill:verificador-security-layer:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Ejecutar la capa 4 de verificacion: eval de seguridad. Analisis estatico + dinamico + check de privilegios. Contextual con ARCHITECTURE.md. Priorizar hallazgos por impacto real, no por volumen. Alineado con Swarm::Ops 8.2 (agente-security activo).

## I/O

- **Input:** changeset: Changeset, architecture_context?: ArchitectureDoc
- **Output:** security_result: {status: pass|fail, static_analysis: {findings: Finding[], critical: number, high: number, medium: number, low: number}, dynamic_analysis: {status: pass|fail, findings: Finding[]}, privilege_check: {status: pass|fail, escalations: PrivilegeEscalation[]}, contextualized: boolean, prioritized_findings: Finding[]}

## Procedimiento

1. **Analisis estatico (SAST)**:
   - Ejecutar SAST sobre changeset
   - Detectar patrones: inyeccion SQL, XSS, SSRF, path traversal, secrets hardcoded, dependencias vulnerables
   - Clasificar por severidad: critico, alto, medio, bajo

2. **Analisis dinamico (DAST)**:
   - Evaluar comportamiento runtime del cambio
   - Detectar: endpoints sin autenticacion, inputs sin validacion, responses con datos sensibles
   - Verificar headers de seguridad, CORS, rate limiting

3. **Check de privilegios**:
   - Verificar principio de minimo privilegio
   - Detectar: escalada de privilegios, permisos excesivos, roles sobre-asignados
   - Comparar permisos requeridos vs permisos solicitados

4. **Contextualizacion con ARCHITECTURE.md** (si disponible):
   - Evaluar cambio en contexto de arquitectura completa
   - Verificar si introduce nuevas superficies de ataque
   - Evaluar impacto en componentes adyacentes
   - IF sin ARCHITECTURE.md → analisis sin contexto, registrar limitacion

5. **Priorizar hallazgos**:
   - NO reportar 200 hallazgos igualmente "medium"
   - Priorizar por impacto real: exposicion + probabilidad + datos afectados
   - Hallazgos criticos/altos → status = fail
   - Hallazgos medios/bajos → status = pass con warnings

## Signature Output

```yaml
security_result:
  status: "pass"
  static_analysis:
    findings: 2
    critical: 0
    high: 0
    medium: 1
    low: 1
    detail:
      - severity: "medium"
        type: "dependency"
        description: "lodash 4.17.20 tiene CVE conocido, pero no expuesto a input externo"
      - severity: "low"
        type: "informational"
        description: "console.log en endpoint, remover antes de produccion"
  dynamic_analysis:
    status: "pass"
    findings: []
  privilege_check:
    status: "pass"
    escalations: []
  contextualized: true
  architecture_file: "ARCHITECTURE.md"
  prioritized_findings:
    - "medium: lodash CVE (bajo impacto real, no expuesto)"
    - "low: console.log residual"
```
