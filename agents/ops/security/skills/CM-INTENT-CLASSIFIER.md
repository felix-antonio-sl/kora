---
_manifest:
  urn: "urn:ops:skill:security-intent-classifier:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Clasificar la intencion del operador en el contexto de seguridad para dirigir a la rama FSM correcta. Mapear input libre a uno de los intents validos del agente de seguridad. Verificar DIVERSITY_CHECK como precondicion antes de clasificar.

## I/O

- **Input:** user_message: string, current_state: FSM_State, swarm_config: {model: string, provider: string}
- **Output:** intent: {type: ANALISIS_PR|RUNTIME|DEPENDENCIAS|ADVERSARIAL|META_EVAL|END, confidence: float, context: string, diversity_verified: boolean}

## Procedimiento

1. **Verificar diversidad**: Comparar modelo/provider propio contra swarm_config. IF mismo → diversity_verified=false, intent.type=ABORT.

2. **Extraer** tokens clave del mensaje: PR, diff, review seguridad, CVE, dependencia, vulnerabilidad, runtime, monitoreo, anomalia, adversarial, pentest, injection, auditoria, meta-eval, quis custodiet.

3. **Mapear** a intent:
   - Tokens PR, diff, review, analizar, seguridad, endpoint, auth → ANALISIS_PR
   - Tokens runtime, monitoreo, anomalia, trafico, patron, produccion, comportamiento → RUNTIME
   - Tokens CVE, dependencia, vulnerabilidad, paquete, version, upgrade, supply chain → DEPENDENCIAS
   - Tokens adversarial, pentest, injection, bypass, escalacion, OWASP, attack → ADVERSARIAL
   - Tokens auditoria, meta-eval, quis custodiet, false positive, degradacion, auto-revision → META_EVAL
   - Tokens terminar, fin, resumen, listo → END

4. **Resolver ambiguedad**: IF multiples intents → priorizar por urgencia: RUNTIME > ANALISIS_PR > ADVERSARIAL > DEPENDENCIAS > META_EVAL > END.

5. **Validar contexto**: IF ANALISIS_PR sin ARCHITECTURE.md disponible → agregar requires_prior: "ARCHITECTURE.md".

## Signature Output

```yaml
intent:
  type: "ANALISIS_PR"
  confidence: 0.94
  context: "PR #87 nuevo endpoint detectado, requiere analisis seguridad"
  diversity_verified: true
  requires_prior: null
```
