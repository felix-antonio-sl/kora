---
_manifest:
  urn: "urn:ops:skill:verificador-diversity-layer:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Ejecutar la capa 3 de verificacion: eval de diversidad. Verificar que el reviewer usa un provider/modelo DIFERENTE al coder. Ejecutar cross-eval donde otro "cerebro" evalua el cambio independientemente. Protege contra alucinacion sistemica (Xanpan::Agents 15.1).

## I/O

- **Input:** coder_info: {provider: string, model: string}, reviewer_info: {provider: string, model: string}, changeset: Changeset
- **Output:** diversity_result: {status: pass|fail, same_provider: boolean, coder_provider: string, reviewer_provider: string, cross_eval: {quality: pass|fail, correctness: pass|fail, spec_adherence: pass|fail, reasoning: string}}

## Procedimiento

1. **Verificar diversidad de provider** (prerequisito):
   - Comparar coder_info.provider vs reviewer_info.provider
   - IF mismo provider → status = fail INMEDIATAMENTE
   - NO ejecutar cross-eval si provider es el mismo
   - Registrar: "Mismo provider ({provider}). Capa fallida. Asignar reviewer de provider diferente."

2. **Ejecutar cross-eval** (solo si providers diferentes):
   - El reviewer analiza el changeset de forma independiente
   - Evaluar 3 dimensiones:
     - **Quality**: Codigo limpio, buenas practicas, mantenibilidad
     - **Correctness**: Logica correcta, edge cases cubiertos, no introduce bugs
     - **Spec Adherence**: Cumple los requisitos del ticket/historia

3. **Evaluar resultado cross-eval**:
   - IF las 3 dimensiones pass → cross_eval global pass
   - IF alguna dimension fail → cross_eval global fail
   - Registrar reasoning del reviewer para cada dimension

4. **Compilar resultado**:
   - IF providers diferentes AND cross_eval pass → status = pass
   - IF providers iguales → status = fail (diversidad)
   - IF cross_eval fail → status = fail (cross-eval)

## Signature Output

```yaml
diversity_result:
  status: "pass"
  same_provider: false
  coder_provider: "Anthropic"
  coder_model: "Claude Opus 4.6"
  reviewer_provider: "OpenAI"
  reviewer_model: "GPT-4o"
  cross_eval:
    quality: "pass"
    correctness: "pass"
    spec_adherence: "pass"
    reasoning: "Codigo limpio, logica correcta, cumple spec de historia US-142. Edge cases cubiertos en tests."
```
