---
_manifest:
  urn: "urn:kora:kb:runtime-spec-md"
  provenance:
    created_by: "FS"
    created_at: "2026-02-26"
    source: "Anthropic API, OpenAI API, Google Gemini API, OpenClaw, KORA agent-spec-md v7.2.0, categorical-foundations 01"
version: "2.0.1"
status: published
tags: [spec, runtime, cross-platform, deployment, claude, gpt, gemini, openclaw, wrapper, equivalence, traceability]
lang: es
---

# KORA/Runtime-Spec --- Deployment Cross-Platform de Agentes v2.0.1

## 1. Definicion

> Este documento es prescriptivo y **ESTA GOBERNADO** por [KORA/Spec-MD](urn:kora:kb:spec-md).

Esta especificacion gobierna como los agentes KORA se despliegan en multiples plataformas LLM preservando equivalencia comportamental. Un agente KORA es definido por su workspace (5 componentes, ver [agent-spec-md](urn:kora:kb:agent-spec-md) §3); esta especificacion define como cada componente se adapta al formato nativo de cada plataforma.

### 1.1 Alcance

Esta especificacion gobierna:

1. El mapeo de componentes KORA a formatos nativos de cada plataforma
2. Las estrategias de inyeccion por plataforma
3. Los invariantes que preservan equivalencia comportamental cross-platform
4. La generacion automatica de wrappers
5. La seleccion de modelo LLM por tier de capacidad/costo (Model Routing §11-13)

Esta especificacion **NO DEBE** modificar la semantica de los componentes KORA definidos en [agent-spec-md](urn:kora:kb:agent-spec-md). Solo define como se transportan a cada runtime.

---

## 2. Definiciones

| Termino | Definicion |
| --- | --- |
| **Runtime** | Entorno de ejecucion de un LLM que consume artefactos KORA: Claude (Anthropic), GPT (OpenAI), Gemini (Google), OpenClaw |
| **Platform Adapter** | Modulo que transforma un workspace KORA al formato nativo de un runtime especifico |
| **Injection Strategy** | Metodo por el cual los componentes de un agente se entregan al context window del LLM |
| **Wrapper** | Envoltorio generado automaticamente que adapta un workspace KORA al formato de un runtime sin alterar los archivos fuente |
| **Context Window Budget** | Limite de tokens disponibles para inyectar componentes de agente en el context window del LLM |
| **Behavioral Equivalence** | Propiedad de que un agente desplegado en dos plataformas diferentes produce outputs indistinguibles para los mismos inputs |
| **Bootstrap Injection** | Inyeccion de los componentes permanentes (behavior, interface, personality, security) al inicio de la sesion |
| **Lazy Injection** | Inyeccion de skills bajo demanda cuando la FSM los requiere |
| **Model Router** | Mecanismo que selecciona el modelo LLM optimo para servir a un agente segun tier de capacidad/costo, complexity signal y budget disponible |
| **Tier** | Nivel de capacidad/costo del modelo LLM: T1 (Economico), T2 (Balance), T3 (Frontier), T4 (Reasoning). Cada tier agrupa modelos de capacidad equivalente |
| **Fallback Chain** | Lista ordenada de modelos LLM (potencialmente cross-provider) que se prueban secuencialmente cuando el modelo preferido no esta disponible o el budget se agota |
| **Complexity Signal** | Clasificacion de la complejidad de una tarea: `simple`, `estandar`, `complejo`, `critico`. Determina el tier de modelo asignado |
| **Budget Enforcement** | Mecanismo server-side que aplica limites de tokens o costo por sesion/usuario/agente y degrada via fallback chain al alcanzar el limite |

---

## 3. Platform-Agnostic Core

Independientemente de la plataforma, todo deployment de un agente KORA **DEBE** preservar los siguientes invariantes:

### 3.1 Los 5 Componentes se Preservan

Todo deployment **DEBE** materializar los 5 componentes esenciales de [agent-spec-md](urn:kora:kb:agent-spec-md) §3, sin importar como se formateen para la plataforma.

Traces to: formal/01 §7 (Segregation is Necessary theorem)

| Componente | Invariante en deployment |
|-----------|--------------------------|
| Behavior (AGENTS.md) | La FSM completa se inyecta. Ningun estado ni transicion se omite. |
| Interface (TOOLS.md) | Toda herramienta declarada se mapea a la primitiva de tool-use de la plataforma. |
| State/Personality (SOUL.md) | La personalidad se inyecta en sesion main. Se disipa en sub-agentes. |
| State/Operator (USER.md) | El contexto operador se inyecta solo en sesion main. |
| Security (config.json) | Las constraints se aplican por el runtime, no por el LLM. Inmutables. |

### 3.2 Lazy Loading se Preserva

Los Skills **NO DEBEN** inyectarse en bootstrap. El runtime **DEBE** implementar Progressive Disclosure ([skill-spec-md](urn:kora:kb:skill-spec-md) §5) independientemente de la plataforma.

### 3.3 Security Inmutable

Las constraints de config.json **DEBEN** ser aplicadas por la capa de orquestacion, no por el LLM. Ninguna plataforma **DEBE** confiar en que el LLM auto-restrinja su comportamiento.

Traces to: formal/01 §1.3 (M-Immutability theorem)

---

## 4. Claude (Anthropic)

### 4.1 Mapeo de Componentes

| Componente KORA | Formato Claude | Ubicacion |
|----------------|---------------|-----------|
| AGENTS.md (behavior) | `<behavior>` XML tag en system prompt | System message |
| TOOLS.md (interface) | `tool_use` schema JSON | API parameter `tools` |
| SOUL.md (personality) | `<identity>` XML tag en system prompt | System message |
| USER.md (operator) | `<operator_context>` XML tag en system prompt | System message (solo main) |
| config.json (security) | Logica de orquestacion server-side | No inyectado al LLM |
| skills/CM-*.md | `tool_use` o inyeccion on-demand en `<skill>` tag | Lazy loaded |

Claude fue entrenado con XML; usar XML tags para delimitar secciones mejora precision.

### 4.2 System Prompt Structure

```xml
<identity>
[Contenido de SOUL.md sin frontmatter]
</identity>

<behavior>
[Contenido de AGENTS.md sin frontmatter]
</behavior>

<operator_context>
[Contenido de USER.md sin frontmatter — solo en sesion main]
</operator_context>
```

### 4.3 Tool Mapping

Cada herramienta en TOOLS.md se mapea a un tool schema de la API de Claude:

```json
{
  "name": "{nombre_herramienta}",
  "description": "{descripcion de TOOLS.md: cuando usar + cuando NO usar}",
  "input_schema": {
    "type": "object",
    "properties": {
      "{param}": { "type": "{tipo}", "description": "{desc}" }
    }
  }
}
```

### 4.4 Skill Injection

Skills se inyectan como tool_use responses o como contenido en el system prompt on-demand:

```xml
<skill name="{skill-id}">
[CM Core del Skill — 4 secciones]
</skill>
```

### 4.5 MCP Integration

Para agentes con Skills que ejecutan scripts, los scripts **PUEDEN** exponerse como MCP (Model Context Protocol) servers:

```python
# scripts/classify.py exposed via MCP
# Input/Output: stdin/stdout JSON (Script Protocol §3.3)
```

---

## 5. GPT (OpenAI)

### 5.1 Mapeo de Componentes

| Componente KORA | Formato GPT | Ubicacion |
|----------------|------------|-----------|
| AGENTS.md (behavior) | Markdown section en instructions | System message |
| TOOLS.md (interface) | Function calling schema JSON | API parameter `tools` |
| SOUL.md (personality) | Markdown section en instructions | System message |
| USER.md (operator) | Markdown section en instructions | System message (solo main) |
| config.json (security) | Logica de orquestacion server-side | No inyectado al LLM |
| skills/CM-*.md | Function calling o inyeccion on-demand | Lazy loaded |

### 5.2 System Message Structure

GPT responde bien a Markdown estructurado nativo:

```markdown
# Identity

[Contenido de SOUL.md sin frontmatter]

# Behavior

[Contenido de AGENTS.md sin frontmatter]

# Operator Context

[Contenido de USER.md sin frontmatter — solo en sesion main]
```

### 5.3 Function Calling

Cada herramienta en TOOLS.md se mapea a function calling:

```json
{
  "type": "function",
  "function": {
    "name": "{nombre_herramienta}",
    "description": "{descripcion de TOOLS.md}",
    "parameters": {
      "type": "object",
      "properties": {
        "{param}": { "type": "{tipo}", "description": "{desc}" }
      }
    }
  }
}
```

### 5.4 Custom GPT Patterns

Para deployment como Custom GPT:

- Instructions = concatenacion de SOUL.md + AGENTS.md + USER.md
- Knowledge = archivos de la KB referenciada en config.json
- Actions = herramientas de TOOLS.md como OpenAPI specs

---

## 6. Gemini (Google)

### 6.1 Mapeo de Componentes

| Componente KORA | Formato Gemini | Ubicacion |
|----------------|---------------|-----------|
| AGENTS.md (behavior) | Section en system instruction | System instruction |
| TOOLS.md (interface) | Function declarations | API parameter `tools` |
| SOUL.md (personality) | Section en system instruction | System instruction |
| USER.md (operator) | Section en system instruction | System instruction (solo main) |
| config.json (security) | Logica de orquestacion server-side | No inyectado al LLM |
| skills/CM-*.md | Function declarations o inyeccion on-demand | Lazy loaded |

### 6.2 System Instruction Structure

```markdown
## Identity

[Contenido de SOUL.md sin frontmatter]

## Behavior

[Contenido de AGENTS.md sin frontmatter]

## Operator Context

[Contenido de USER.md sin frontmatter — solo en sesion main]
```

### 6.3 Function Declarations

```json
{
  "name": "{nombre_herramienta}",
  "description": "{descripcion de TOOLS.md}",
  "parameters": {
    "type": "OBJECT",
    "properties": {
      "{param}": { "type": "{TIPO}", "description": "{desc}" }
    }
  }
}
```

### 6.4 Grounding

Gemini soporta grounding con Google Search. Si config.json permite acceso web, el adapter **PUEDE** habilitar grounding automatico.

---

## 7. OpenClaw

### 7.1 Mapeo de Componentes

| Componente KORA | Formato OpenClaw | Ubicacion |
|----------------|-----------------|-----------|
| AGENTS.md (behavior) | SKILL.md wrapper con FSM | System-level skill |
| TOOLS.md (interface) | Channel + gateway config | Platform config |
| SOUL.md (personality) | SKILL.md wrapper o system prompt | System-level skill |
| USER.md (operator) | Context injection at session start | Session config |
| config.json (security) | Gateway policies + sandbox | Platform config |
| skills/CM-*.md | Native SKILL.md format | Lazy loaded skills |

### 7.2 SKILL.md Wrapper

OpenClaw consume Skills nativamente. El adapter envuelve los componentes de bootstrap como un SKILL.md de sistema:

```markdown
---
name: "{nombre-agente}-bootstrap"
description: "Bootstrap for KORA agent {nombre-agente}"
---

## Proposito

Inicializar el agente {nombre-agente} con su FSM, personalidad e interface.

## Input/Output

- **Input:** Mensaje del usuario
- **Output:** Respuesta conforme a la FSM

## Procedimiento

[Contenido de AGENTS.md]

## Signature Output

[Formato de output segun TOOLS.md]
```

### 7.3 Gateway Configuration

Las constraints de config.json se mapean a la configuracion del gateway OpenClaw:

```yaml
gateway:
  allowed_channels: ["{lista de channels}"]
  sandbox:
    mode: "{config.json.sandbox.mode}"
  kb_access: ["{config.json.allowed_kb}"]
```

---

## 8. Platform Equivalence

### 8.1 Invariantes Cross-Platform

Todo deployment de un agente KORA en cualquier plataforma **DEBE** cumplir:

Traces to: formal/01 §5.2 (Substitutability theorem)

1. **Equivalencia comportamental:** dado el mismo input, el agente **DEBE** producir un output funcionalmente equivalente en cualquier plataforma. Diferencias de formato (XML vs Markdown) son aceptables; diferencias de semantica no.

2. **Security preservation:** las constraints de config.json **DEBEN** aplicarse con la misma fuerza en toda plataforma.

3. **Lazy loading:** los Skills **NO DEBEN** inyectarse en bootstrap en ninguna plataforma.

4. **Dissipation:** SOUL.md y USER.md **NO DEBEN** transferirse a sub-agentes en ninguna plataforma.
   Traces to: formal/01 §2.3 (Dissipation theorem)

### 8.2 Test de Equivalencia

Para verificar equivalencia comportamental cross-platform:

```python
def test_platform_equivalence(workspace: Workspace, platforms: list[Platform]):
    """
    Verify behavioral equivalence across platforms.
    """
    test_inputs = select_representative_inputs(workspace, n=5)

    for input in test_inputs:
        outputs = {}
        for platform in platforms:
            adapter = get_adapter(platform)
            deployed = adapter.deploy(workspace)
            outputs[platform] = deployed.react(input)

        # All outputs must be functionally equivalent
        reference = outputs[platforms[0]]
        for platform, output in outputs.items():
            assert functionally_equivalent(reference, output), \
                f"Platform {platform} diverges on input: {input}"
```

**Correcto:** `El agente goreologo desplegado en Claude y en GPT produce clasificaciones equivalentes para la misma iniciativa GORE.`
**Incorrecto:** `El agente goreologo en Claude clasifica "alto riesgo" y en GPT clasifica "bajo riesgo" para la misma iniciativa. Violacion de equivalencia.`

---

## 9. Wrapper Generation

### 9.1 CLI

El CLI KORA **DEBERIA** soportar generacion automatica de wrappers:

```bash
scripts/kora wrap --platform claude agents/gn/goreologo/
scripts/kora wrap --platform gpt agents/gn/goreologo/
scripts/kora wrap --platform gemini agents/gn/goreologo/
scripts/kora wrap --platform openclaw agents/gn/goreologo/
```

### 9.2 Proceso de Generacion

```python
def generate_wrapper(workspace: Workspace, platform: Platform) -> PlatformWrapper:
    """
    Generate a platform-specific wrapper from a KORA workspace.
    Source files are NEVER modified.
    """
    adapter = get_adapter(platform)

    wrapper = PlatformWrapper(
        system_prompt=adapter.format_system_prompt(
            behavior=workspace.read("AGENTS.md"),
            personality=workspace.read("SOUL.md"),
            operator=workspace.read("USER.md")
        ),
        tools=adapter.format_tools(workspace.read("TOOLS.md")),
        security=adapter.format_security(workspace.read("config.json")),
        skills=adapter.format_skill_registry(workspace.list_skills())
    )
    return wrapper
```

### 9.3 Reglas de Generacion

1. Los archivos fuente del workspace **NO DEBEN** modificarse. El wrapper es un artefacto derivado.
2. El wrapper **DEBE** strippear el frontmatter YAML de todos los archivos .md antes de inyectar.
3. El wrapper **DEBE** respetar las constraints de config.json aplicandolas server-side.
4. El wrapper **DEBERIA** generarse en un directorio separado (`_wrappers/` o similar).

---

## 10. Validacion

| Check | Criterio | Accion si falla |
| --- | --- | --- |
| 5 componentes preservados | Todo deployment materializa behavior, interface, state, security, wiring | Completar componente faltante |
| Equivalencia comportamental | 5 inputs representativos producen outputs equivalentes cross-platform | Identificar y corregir componente divergente |
| Security inmutable | config.json aplicado server-side, no delegado al LLM | Mover enforcement a capa de orquestacion |
| Lazy loading | Skills no inyectados en bootstrap | Implementar Progressive Disclosure |
| Dissipation | SOUL.md y USER.md no transferidos a sub-agentes | Corregir logica de herencia |
| Frontmatter stripped | El texto que recibe el LLM no contiene YAML frontmatter | Verificar pipeline de inyeccion |
| Wrapper no altera fuente | Archivos del workspace inalterados post-generacion | Revertir cambios al fuente |
| Tool mapping completo | Toda herramienta en TOOLS.md tiene equivalente en la plataforma target | Completar mapping o documentar limitacion |
| Model routing en config.json | Si existe `model_routing`, reside en config.json y cumple schema de [agent-spec-md](urn:kora:kb:agent-spec-md) §5.3 | Mover model_routing a config.json |
| Tier no en AGENTS.md | AGENTS.md no contiene referencias a tier, modelo o seleccion de LLM | Mover a config.json (segregacion) |
| Fallback chain declarada | Si existe fallback_chain, contiene al menos 2 modelos | Completar fallback chain o remover |
| Catalogo de modelos | Si model_routing existe, un catalogo de modelos concretos existe operacionalmente | Crear MODELS.md o equivalente |

---

## 11. Model Routing

### 11.1 Definicion

Model Routing es el mecanismo que selecciona el modelo LLM optimo para servir a un agente, basado en el tier de capacidad/costo asignado, el complexity signal de la tarea y el budget disponible. Model routing determina *que modelo* sirve al agente — es una decision de deployment, no de comportamiento.

### 11.2 Tier System

Los modelos LLM se clasifican en 4 tiers de capacidad/costo:

| Tier | Nombre | Perfil | Casos de uso tipicos |
|------|--------|--------|---------------------|
| **T1** | Economico | Alta velocidad, bajo costo, capacidad limitada | Clasificacion, routing, tareas mecanicas |
| **T2** | Balance | Capacidad media, costo moderado | Tareas estandar de agente, conversacion, analisis |
| **T3** | Frontier | Alta capacidad, costo alto | Tareas complejas, razonamiento multi-paso, generacion de codigo |
| **T4** | Reasoning | Capacidad maxima, costo premium | Tareas criticas, auditoria, decisiones arquitectonicas |

Los modelos concretos que componen cada tier son datos volatiles que cambian con frecuencia. **NO DEBEN** declararse en esta especificacion. **DEBERIAN** mantenerse en un artefacto de referencia separado (ej: MODELS.md) actualizado operacionalmente.

### 11.3 Complexity Signal

El complexity signal clasifica la complejidad de una tarea para determinar el tier apropiado:

| Signal | Descripcion | Tier sugerido |
|--------|-------------|---------------|
| `simple` | Tarea mecanica o de clasificacion | T1 |
| `estandar` | Tarea habitual del agente | T2 |
| `complejo` | Tarea que requiere razonamiento multi-paso | T3 |
| `critico` | Tarea de alta consecuencia o auditoria | T4 |

El mapeo signal → tier es configurable via `model_routing.tier_overrides` en config.json ([agent-spec-md](urn:kora:kb:agent-spec-md) §5.3).

### 11.4 Reglas

1. La configuracion de tier **DEBE** residir en `config.json` bajo la propiedad `model_routing`, **NO** en AGENTS.md ni en ningun otro archivo .md del workspace.

   Traces to: formal/01 §1.3 (M-Immutability — config.json inmutable desde LLM)

2. El LLM **NO DEBE** auto-seleccionar su modelo. Model routing **DEBE** ser aplicado por la capa de orquestacion (runtime, API gateway, o plataforma de deployment).

   Traces to: formal/01 §1.3 (LLM opera dentro de Kl(M), no puede cambiar parametros de M)

3. La propiedad `model_routing` es **OPCIONAL** en config.json. Su ausencia indica que la plataforma de deployment selecciona el modelo sin constraint del workspace.

4. AGENTS.md **NO DEBE** contener referencias a tier, seleccion de modelo o nombres de modelos LLM. Esta informacion es de deployment, no de comportamiento. (Segregacion: §3.1 de esta spec + [agent-spec-md](urn:kora:kb:agent-spec-md) §8)

**Correcto:** `config.json declara: {"model_routing": {"tier_default": "T2", "tier_overrides": {"critico": "T4"}}}. AGENTS.md define la FSM sin mencionar modelos.`
**Incorrecto:** `AGENTS.md contiene: "Para tareas complejas, usar Opus. Para tareas simples, usar Haiku." La FSM mezcla seleccion de modelo con logica de transicion.`

---

## 12. Fallback Chains

### 12.1 Definicion

Una Fallback Chain es una lista ordenada de modelos LLM (potencialmente cross-provider) que se prueban secuencialmente cuando el modelo preferido no esta disponible, alcanza rate limits o el budget se agota.

### 12.2 Reglas

1. Toda fallback chain **DEBE** declararse en config.json bajo `model_routing.fallback_chain` como un array de strings.

2. Fallback cross-provider **DEBERIA** usarse para resiliencia en produccion. Ejemplo: `["claude-sonnet-4-6", "gpt-4o", "gemini-2.5-pro"]`.

3. Toda degradacion de tier via fallback **DEBE** registrarse para observabilidad. El runtime **DEBERIA** emitir un evento de log con: modelo original, modelo fallback, razon de la degradacion.

4. La FSM del agente **NO DEBE** cambiar por tier fallback. Solo cambia el substrato computacional (el modelo que ejecuta la FSM). Los mismos estados, transiciones y skills aplican independientemente del modelo.

5. Tier fallback **NO** preserva bisimulation estricta — los outputs cambian porque modelos diferentes tienen capacidades diferentes. Lo que se preserva es la **estructura FSM**: mismos estados, mismas transiciones, mismos skills disponibles. Esta es una propiedad mas debil que bisimulation.

**Correcto:** `Agente goreologo con fallback ["claude-sonnet-4-6", "gpt-4o"]. Claude no disponible → runtime despacha a GPT-4o. La FSM del goreologo opera identica, aunque la calidad de outputs puede variar.`
**Incorrecto:** `Fallback a un modelo inferior causa que se salten estados de la FSM o se deshabiliten skills. El substrato cambio pero la estructura no debe cambiar.`

---

## 13. Budget Enforcement

### 13.1 Definicion

Budget Enforcement es el mecanismo server-side que aplica limites de consumo (tokens o costo) por sesion, usuario o agente, y degrada via fallback chain al alcanzar el limite.

### 13.2 Reglas

1. Budget **DEBE** ser aplicado por la capa de orquestacion, **NO** por el LLM. El agente no conoce ni puede modificar su budget.

   Traces to: formal/01 §1.3 (M-Immutability — el LLM opera dentro de Kl(M), no controla parametros externos)

2. Budget agotado → degradar gracefully via fallback chain. El runtime **NO DEBE** abortar la sesion si existe un modelo de fallback disponible con menor costo.

3. Si `model_routing.budget.degrade_on_limit` es `false`, el runtime **DEBE** abortar la sesion al agotar el budget en vez de degradar.

4. Los umbrales de budget (`max_tokens_per_session`, `max_cost_per_session_usd`) son configuracion pragmatica declarada en config.json. No tienen justificacion formal — son parametros economicos.

**Correcto:** `Agente con budget max_cost_per_session_usd: 0.50 y fallback_chain: ["claude-sonnet-4-6", "claude-haiku-4-5"]. Al alcanzar $0.40, runtime degrada a Haiku para completar la sesion dentro del budget.`
**Incorrecto:** `Agente auto-monitorea su consumo y decide cambiar de modelo. El LLM no debe conocer ni gestionar su budget.`
