---
_manifest:
  urn: "urn:kora:kb:mastra-runtime-extension"
  provenance:
    created_by: "OpenAI Codex (encarnando arquitecto-categorico)"
    created_at: "2026-04-19"
    source: "runtime-spec-md v3.8.0 + transmutation-spec v1.1.0 + documentacion oficial de Mastra sobre agents, workflows, snapshots, runtime context y MCP (consultada 2026-04-19)."
version: "1.0.0"
status: publicado
tags: [spec, runtime, mastra, extension, workflow, mcp, transmutacion]
lang: es
extensions:
  kora:
    precedence_tier: 4
    platform: "mastra"
    baseline_docs_release: "docs oficiales consultadas 2026-04-19"
relations:
  depends:
    - "urn:kora:kb:runtime-spec-md"
    - "urn:kora:kb:transmutation-spec"
    - "urn:kora:kb:multiagente-spec"
  cites:
    - "urn:kora:kb:harness-spec"
    - "urn:kora:kb:qa-spec"
    - "urn:kora:kb:gobernanza"
---

# KORA/Mastra-Runtime-Extension v1.0.0

## 1. Definicion

Esta extension especializa `runtime-spec-md` para **Mastra**, runtime centrado
en agentes, workflows, contexto de ejecucion, MCP y persistencia de snapshots.

Su funcion es:

1. declarar `T_mastra: KORA_IR -> Runtime_mastra`,
2. fijar la matriz de preservacion por eje,
3. definir las superficies nativas que el wrapper **DEBE** privilegiar,
4. habilitar un check de fidelidad analogo a `fidelidad-agentskills`.

## 2. Formas materiales soportadas

| Forma material | Encaje Mastra | Fidelidad |
|----------------|---------------|-----------|
| `habilidad` | tool o step reusable dentro de workflow | partial |
| `subagente` | agent invocable desde workflow o network | full |
| `agente-propiamente-tal` | agent con memory, runtime context y tools | full |
| `agente-plataforma` | server/worker con storage, workflows y supervision externa | partial |

Rationale: Mastra da superficies nativas para agentes y workflows. Una
habilidad aislada no es shape primario del framework; se proyecta como tool o
step. Un agente de plataforma requiere infraestructura de despliegue externa,
por eso la realizacion de `Μ=3` y `Λ>=1` sigue siendo parcialmente extrinseca.

## 3. Matriz de preservacion por eje

### 3.1 Eje Π (plan)

```yaml
pi:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full }
  "2": { projected: 2, fidelity: full }
  "3": { projected: 3, fidelity: partial, comment: "workflow graphs y loops existen, pero el fixed-point completo depende del wrapper aplicativo" }
```

### 3.2 Eje Μ (materia)

```yaml
mu:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full }
  "2": { projected: 2, fidelity: full, comment: "memory + storage + snapshots soportan persistencia cross-session" }
  "3": { projected: 3, fidelity: partial, comment: "always-on depende del host/deploy; Mastra aporta storage y resume, no daemonidad por si solo" }
```

### 3.3 Eje Ξ (interaccion)

```yaml
xi:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full }
  "2": { projected: 2, fidelity: full }
  "3": { projected: 3, fidelity: full, comment: "workflows, suspend/resume y checkpoints humanos realizan protocolos multi-fase" }
  "4": { projected: 4, fidelity: partial, comment: "agent networks y workflow composition aproximan la operad, pero la topologia dinamica completa queda en la app" }
```

### 3.4 Eje Λ (nivel sociotecnico)

```yaml
lambda:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full }
  "2": { projected: 2, fidelity: partial, comment: "MCP, auth y runtime context soportan ecosystem, pero las fronteras organizacionales quedan en la aplicacion" }
  "3": { projected: null, fidelity: none, loss: "society-in-the-loop no es primitive del runtime" }
```

### 3.5 Eje Φ (acoplamiento humano-AI)

```yaml
phi:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full }
  "2": { projected: 2, fidelity: full }
  "3": { projected: 3, fidelity: partial, comment: "human-in-the-loop y runtime context existen, pero la cognicion hibrida completa es aplicativo" }
  "4": { projected: null, fidelity: none, loss: "co-evolutivo no modelado por el runtime" }
```

### 3.6 Eje Σ (vector etico)

```yaml
sigma:
  safety_norm:
    max_supported: 3
    enforcement: "guardrails, policy middleware y approval gates de workflow"
  fairness:
    max_supported: 2
    enforcement: "evals y checks aplicativos; no hay enforcement universal del runtime"
  transparency:
    max_supported: 3
    enforcement: "tracing, logs y snapshots"
  accountability:
    max_supported: 2
    enforcement: "storage, execution logs, request/user context"
  sustainability:
    max_supported: 1
    enforcement: "budgeting aplicativo; no metrica ambiental nativa"
```

## 4. Native-first

Cuando Mastra ofrece superficie nativa, el wrapper **DEBE** usarla antes que
serializarla como texto opaco.

Superficies nativas:

- `Agent`
- `Workflow`
- snapshots / resume
- `runtimeContext`
- `memory`
- `MCPServer` / clientes MCP
- storage y tracing

## 5. Topologia target

La salida derivada **DEBE** vivir bajo:

```text
artifacts/agents/{namespace}/{agent}/_BUILD/mastra/
```

Contrato minimo de salida del wrapper:

1. `_transmutation.yml` obligatorio,
2. blueprint o manifest del wrapper Mastra,
3. referencias a workflows/tools/memory cuando apliquen.

## 6. Runtime state boundary

Quedan fuera de la fuente canonica:

- credenciales,
- storage fisico,
- handles de deploy,
- traces operativos efimeros,
- tokens de auth,
- snapshots runtime materializados fuera del repo.

## 7. Metadata de encaje runtime

Forma canonica recomendada:

```yaml
extensions:
  mastra:
    agent_id: triage-clinico
    workflows: [triage, escalamiento]
    memory_enabled: true
    snapshot_storage: libsql
    runtime_context_keys: [tenant_id, request_id, user_role]
    mcp_enabled: true
    server_mode: node-http
    human_in_loop: true
```

## 8. Check de fidelidad

`fidelidad-mastra` verifica:

1. que el vector del artefacto cae dentro del dominio declarado,
2. que la perdida estructural esta declarada por eje,
3. que la proyeccion dry-run a `mastra` no falla para agentes productivos.

## 9. Invariantes

1. El wrapper Mastra **NO** se vuelve fuente de verdad.
2. Toda degradacion de `Ξ`, `Λ`, `Φ` o `Σ` **DEBE** quedar declarada.
3. `runtimeContext` **NO DEBE** reemplazar al IR; solo lo especializa por
   solicitud o tenant.
4. Los checkpoints humanos **DEBEN** preservar `session_id` y budget vigente.

## 10. Contrato vigente

`mastra-runtime-extension v1.0.0` habilita:

1. target `mastra` en el transmutor,
2. matriz de preservacion declarada,
3. check `fidelidad-mastra`,
4. encaje normativo del wrapper aunque el adapter final siga siendo futuro.
