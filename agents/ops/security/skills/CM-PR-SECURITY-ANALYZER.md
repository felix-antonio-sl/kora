---
_manifest:
  urn: "urn:ops:skill:security-pr-security-analyzer:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Analizar la seguridad de un PR con contexto arquitectonico completo. Identificar hallazgos reales priorizados por impacto, no por severidad generica. Pensar como atacante: que explotaria con este cambio?

## I/O

- **Input:** pr: {diff: string, files_changed: string[], metadata: PRInfo}, architecture: ArchDoc, existing_findings: Finding[]
- **Output:** analysis: {findings: Finding[], attack_surfaces_affected: string[], veto: boolean, veto_reason: string|null, summary: string}

## Procedimiento

1. **Leer ARCHITECTURE.md** completo: entender trust boundaries, flujo de datos, servicios expuestos vs internos, mecanismos auth, puntos de entrada externos.
   - IF ARCHITECTURE.md no disponible → REJECT. Retornar error: "Analisis contextual requiere ARCHITECTURE.md."

2. **Clasificar superficie de ataque** del diff:
   - **auth**: cambios en autenticacion, autorizacion, middleware auth, roles, permisos, tokens, sesiones
   - **data**: acceso a datos sensibles, PII, cambios en queries, exposicion de campos, logging de datos sensibles
   - **external_interfaces**: nuevos endpoints, cambios API publica, webhooks, integraciones externas, CORS
   - **crypto**: cambios en cifrado, hashing, generacion tokens, manejo secretos, TLS config
   - **llm_prompt**: cambios en prompts, system instructions, agent-to-agent communication, tool definitions

3. **Analizar cada cambio en contexto**:
   - Para cada archivo modificado: que rol cumple en la arquitectura?
   - El cambio cruza un trust boundary? (interno→externo, autenticado→publico)
   - El cambio modifica un mecanismo de defensa existente?
   - El cambio introduce un nuevo punto de entrada sin proteccion equivalente?
   - El cambio expone datos que antes no estaban accesibles?

4. **Construir hallazgos** (solo hallazgos reales):
   - Para cada hallazgo:
     - severity: critical | high | medium | low
     - evidence: archivo:linea exacta
     - attack_vector: como un atacante explotaria esto
     - real_impact: que conseguiria el atacante (exfiltracion, escalacion, denegacion, manipulacion)
     - suggested_fix: correccion concreta

5. **Priorizar por impacto real**:
   - Consolidar hallazgos. Eliminar duplicados. Agrupar por superficie.
   - Ordenar: critical > high > medium > low
   - IF >10 hallazgos medium → consolidar en patron, no listar individualmente

6. **Decidir veto**:
   - IF hallazgo critical en auth/data con exposicion externa → veto=true
   - IF hallazgo critical en crypto con degradacion → veto=true
   - ELSE → veto=false, hallazgos como recomendaciones

## Signature Output

```yaml
analysis:
  findings:
    - severity: "critical"
      evidence: "src/routes/users.py:42"
      attack_vector: "GET /api/v2/users sin middleware auth, accesible desde internet"
      real_impact: "Exfiltracion datos PII de todos los usuarios sin autenticacion"
      suggested_fix: "Agregar @auth_required decorator, validar scope 'users:read'"
    - severity: "medium"
      evidence: "src/models/user.py:18"
      attack_vector: "Campo email incluido en serializer publico"
      real_impact: "Exposicion email usuarios en respuesta API publica"
      suggested_fix: "Usar PublicUserSerializer sin campo email para endpoints publicos"
  attack_surfaces_affected: ["auth", "data", "external_interfaces"]
  veto: true
  veto_reason: "Endpoint sin autenticacion expone PII a internet"
  summary: "2 hallazgos: 1 critical (endpoint sin auth), 1 medium (email expuesto). VETO emitido por critical."
```
