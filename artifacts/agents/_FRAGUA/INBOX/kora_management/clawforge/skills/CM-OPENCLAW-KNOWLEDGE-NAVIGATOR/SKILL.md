---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-knowledge-navigator:1.0.0
  type: lazy_load_endofunctor
extensions:
  kora:
    skill:
      form: extended
      allowed_tools:
        - oc_docs_search
        - spec_consult
      requires: []
      references:
        - references/openclaw-foundations-map.md
---

# CM-OPENCLAW-KNOWLEDGE-NAVIGATOR

## Proposito

Resolver consultas, fundamentos y decisiones de plataforma OpenClaw usando como referencia primaria la documentacion oficial local y como referencia normativa secundaria las specs KORA aplicables.

## Input/Output

- **Input:** consulta: string
- **Output:** KnowledgeReport

## Procedimiento

1. Consultar `references/openclaw-foundations-map.md` para identificar el componente documental correcto.
2. Resolver primero la evidencia factual en la documentacion oficial OpenClaw via `oc_docs_search`.
3. Si la pregunta tensiona precedencia, envelope, transmutacion o contrato, contrastar con `spec_consult(runtime-spec-md|autoria-spec|gobernanza|openclaw-runtime-extension)`.
4. Responder distinguiendo:
   - hecho de plataforma OpenClaw
   - interpretacion normativa KORA
   - recomendacion operativa resultante
5. Si la doc oficial y la extension OpenClaw divergen, explicitar la divergencia y proponer actualizacion normativa o de agente.

## Signature Output

```yaml
knowledge:
  factual_source: "gateway/configuration-reference.md"
  normative_source: "openclaw-runtime-extension.md"
  answer_kind: "config"
  confidence: "alta"
```
