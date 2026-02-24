---
_manifest:
  urn: "urn:kora:agent-bootstrap:architect-cm-koda-agent-construct:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Ejecutar las 5 fases de construccion de agentes KODA-compliant desde requisitos hasta deployment.

## Input/Output

- **Input:** Requisitos de agente (descripcion, dominio, audiencia) desde S-AGENT-BUILDER
- **Output:** agent.yaml completo validado contra 7 principios con instrucciones de deployment

## Procedimiento

1. **P1 — Requirements (FTCF + KB mode + boundaries):**
   - FUNCION: que hace el agente
   - TONO: como comunica
   - CONOCIMIENTO: que fuentes necesita (KB_BASED|LLM_NATIVE|WEB_AUGMENTED|HYBRID)
   - FRONTERAS: que NO hace
   - Documentar boundaries y rejection response
2. **P2 — Architecture (states + CMs):**
   - Modos comportamentales → estados
   - Definir initial_state, transiciones, estados terminales
   - Constraints: role+process(<=5)+transitions
   - Logica >5 pasos → CM
   - Minimo: S-DISPATCHER, S-END
3. **P3 — Construction (7 namespaces):**
   - _manifest
   - KODA_Runtime_Instructions
   - agent_identity
   - knowledge_base
   - workflows_states
   - reasoning_processes
   - io_style + safety_guardrails + self_evaluation + few_shot
4. **P4 — Validation (P1-P7 + security):**
   - P1:Declarativo, P2:Encapsulacion, P3:Separacion, P4:Cartografia, P5:Abstraccion, P6:Categoria, P7:Federacion
   - Guard Set: scope_policy, rejection_response, block_instructions, forbid_jargon
   - process<=5 por estado, CMs ocultos, transiciones→estados existentes
5. **P5 — Deployment (catalog + git):**
   - Entrada catalogo con URN
   - Dependencias y KB resueltas
   - Instrucciones deploy

## Signature Output

```
**Agente construido**: [nombre]
- Fase: [P1-P5 completada]
- Estados: [N]
- CMs: [N]
- Validacion P1-P7: [PASS/FAIL por principio]
- Guard Set: [completo/incompleto]
```
