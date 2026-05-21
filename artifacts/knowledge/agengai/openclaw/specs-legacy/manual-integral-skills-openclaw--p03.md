---
_manifest:
  urn: urn:agengai:kb:openclaw-skills-manual-p03
  provenance:
    created_by: kora/curator
    created_at: '2026-03-26'
    source: 'KNOWLEDGE/agengai/openclaw/documentacion-oficial (tools/skills.md, tools/creating-skills.md,
      tools/skills-config.md, tools/clawhub.md, tools/slash-commands.md, cli/skills.md,
      platforms/mac/skills.md, tools/subagents.md, tools/exec-approvals.md, tools/loop-detection.md,
      tools/multi-agent-sandbox-tools.md, tools/elevated.md, gateway/sandboxing.md,
      gateway/secrets.md, gateway/security/index.md, security/THREAT-MODEL-ATLAS.md,
      concepts/agent.md, concepts/agent-workspace.md, concepts/system-prompt.md, plugins/building-plugins.md,
      plugins/manifest.md, help/testing.md; verificado contra mirror sync 2026-04-05
      commit 2a39141) + fuente web externa: agentskills.io (spec overview, specification,
      quickstart, best-practices, optimizing-descriptions, evaluating-skills, using-scripts,
      client-implementation)'
version: 2.2.0
status: publicado
tags:
- openclaw
- skills
- agentes-ia
- llm
- manual
- ciclo-de-vida
- seguridad
- orquestacion
- agentskills
- interoperabilidad
lang: es
extensions:
  agengai:
    family: note
    scope: Creacion, operacion y evolucion de skills en OpenClaw
    dimensions: 15
    related:
    - urn:agengai:kb:openclaw-manual-integral
  kora:
    shard_index: 3
    shard_count: 5
    shard_root_urn: urn:agengai:kb:openclaw-skills-manual
relations:
  cites:
  - urn:agengai:kb:openclaw-manual-integral
---

# Manual Integral de Skills en OpenClaw - Parte 03

## 7.1 Testing basico de skills

Procedimiento:

1. Verificar carga: `openclaw skills list`
2. Verificar elegibilidad: `openclaw skills list --eligible`
3. Diagnosticar requisitos faltantes: `openclaw skills check`
4. Probar invocacion:
 ```bash
 openclaw agent --message "mensaje que active el skill"
 ```
5. Probar como slash command (si `user-invocable: true`):
 ```
 /nombre_del_skill [argumentos]
 ```

## 7.2 Depuracion de carga

Diagnostico detallado de problemas de carga: ver §17.7.

## 7.3 Recarga de skills

- Iniciar nueva sesion: `/new` o `openclaw gateway restart`
- Hot reload automatico si `skills.load.watch: true` — cambios en `SKILL.md` se reflejan en el siguiente agent turn
- El session snapshot se congela al inicio; hot reload actualiza para el siguiente turn

## 7.4 Debug de slash commands

Comandos utiles:
- `/tools` — ver herramientas disponibles al agente en la sesion actual
- `/tools verbose` — agregar descripciones
- `/context detail` — ver tamano per-skill en el system prompt
- `/verbose on` — habilitar texto detallado de fallos de herramientas (solo para debug)

## 7.5 Optimizacion de descripciones (trigger evals)

La `description` lleva toda la carga del triggering. Si la descripcion no comunica cuando el skill es util, el agente no lo activara.

### Principios para descripciones efectivas

- **Fraseo imperativo** — "Use this skill when..." en vez de "This skill does..."
- **Foco en intent del usuario, no en implementacion** — Describir lo que el usuario intenta lograr
- **Errar hacia lo explicito** — Listar contextos donde aplica, incluyendo casos donde el usuario no nombra el dominio: "even if they don't explicitly mention 'CSV' or 'analysis'"
- **Mantener conciso** — Unas frases a un parrafo corto. Limite duro: 1024 caracteres

### Disenar queries de evaluacion

Crear set de ~20 queries etiquetadas (`should_trigger: true/false`):

- **Should-trigger** (8-10): variar fraseo, explicitud, detalle, complejidad. Las mas utiles son donde el skill ayudaria pero la conexion no es obvia.
- **Should-not-trigger** (8-10): priorizar **near-misses** que comparten keywords pero necesitan algo diferente. "Write a fibonacci function" no testea nada; "write a python script that reads a CSV and uploads each row to postgres" si.

### Calcular trigger rate

Ejecutar cada query multiples veces (minimo 3) y calcular fraccion de ejecuciones donde el skill se activo.
- Should-trigger pasa si trigger rate > 0.5
- Should-not-trigger pasa si trigger rate < 0.5

### Loop de optimizacion

1. Evaluar descripcion actual en sets train (60%) y validation (40%)
2. Identificar fallos en train set
3. Revisar descripcion generalizando (no agregar keywords especificas de queries fallidas)
4. Re-evaluar ambos sets
5. Repetir hasta convergencia (5 iteraciones usualmente suficientes)
6. Seleccionar mejor iteracion por pass rate del validation set

El skill `skill-creator` (`github.com/anthropics/skills/tree/main/skills/skill-creator`) automatiza este loop end-to-end.

## 7.6 Evaluacion de calidad de output (evals)

### Estructura de test cases

Cada test case tiene: **prompt** (mensaje realista), **expected_output** (descripcion de exito), **files** (opcionales).

```json
{
 "skill_name": "csv-analyzer",
 "evals": [
 {
 "id": 1,
 "prompt": "I have a CSV of monthly sales data in data/sales_2025.csv. Can you find the top 3 months by revenue and make a bar chart?",
 "expected_output": "A bar chart image showing the top 3 months by revenue, with labeled axes and values.",
 "files": ["evals/files/sales_2025.csv"],
 "assertions": [
 "The output includes a bar chart image file",
 "The chart shows exactly 3 months",
 "Both axes are labeled",
 "The chart title or caption mentions revenue"
 ]
 }
 ]
}
```

### Ejecucion de evals

Patron: ejecutar cada test case **con skill** y **sin skill** (baseline). Estructura de workspace:

```
mi-skill-workspace/
└── iteration-1/
 ├── eval-caso-1/
 │ ├── with_skill/ (outputs/, timing.json, grading.json)
 │ └── without_skill/ (outputs/, timing.json, grading.json)
 └── benchmark.json (estadisticas agregadas)
```

Cada run en contexto limpio (subagente o sesion separada). Capturar `total_tokens` y `duration_ms`.

### Assertions y grading

Buenas assertions: verificables ("The output file is valid JSON"), especificas ("The bar chart has labeled axes"), contables ("The report includes at least 3 recommendations").

Malas assertions: vagas ("The output is good"), fragiles ("The output uses exactly the phrase 'Total Revenue: $X'").

Grading: evaluar cada assertion como PASS/FAIL con evidencia concreta que cite el output. Requerir evidencia para PASS; no dar beneficio de la duda.

### Benchmark agregado

```json
{
 "run_summary": {
 "with_skill": { "pass_rate": { "mean": 0.83 }, "tokens": { "mean": 3800 } },
 "without_skill": { "pass_rate": { "mean": 0.33 }, "tokens": { "mean": 2100 } },
 "delta": { "pass_rate": 0.50, "tokens": 1700 }
 }
}
```

El delta muestra costo (mas tokens) vs beneficio (mejor pass rate).

### Analisis de patrones

- Eliminar assertions que siempre pasan en ambas configuraciones (no discriminan)
- Investigar assertions que siempre fallan en ambas (assertion rota o test case demasiado dificil)
- Estudiar assertions que pasan con skill pero fallan sin el (valor agregado del skill)
- Endurecer instrucciones cuando resultados son inconsistentes entre runs

### Loop de iteracion

1. Dar senales de eval + `SKILL.md` actual a un LLM para proponer mejoras
2. Revisar y aplicar cambios
3. Re-ejecutar todos los test cases en nuevo `iteration-<N+1>/`
4. Gradear y agregar resultados
5. Revisar con humano. Repetir hasta satisfaccion.

## 7.7 Patrones de instrucciones efectivas

### Secciones de gotchas

Contenido de mayor valor: hechos del entorno que desafian suposiciones razonables. No consejos genericos ("handle errors appropriately") sino correcciones concretas:

```markdown

## Gotchas

- La tabla `users` usa soft deletes. Queries deben incluir
 `WHERE deleted_at IS NULL` o resultados incluiran cuentas desactivadas.
- El user ID es `user_id` en la DB, `uid` en el auth service,
 y `accountId` en el billing API. Los tres refieren al mismo valor.
```

Cuando el agente comete un error que debes corregir, agregar la correccion a gotchas.

#### Templates para formato de output

Proveer templates cuando se necesita output en formato especifico. Templates cortos inline en `SKILL.md`; largos o condicionales en `assets/`.

#### Checklists para workflows multi-paso

Lista explicita ayuda al agente a trackear progreso y no saltar pasos:

```markdown

## Workflow de procesamiento

- [ ] Paso 1: Analizar formulario (`scripts/analyze_form.py`)
- [ ] Paso 2: Crear mapping de campos (`fields.json`)
- [ ] Paso 3: Validar mapping (`scripts/validate_fields.py`)
- [ ] Paso 4: Llenar formulario (`scripts/fill_form.py`)
- [ ] Paso 5: Verificar output (`scripts/verify_output.py`)
```

#### Validation loops

Instruir al agente a validar su propio trabajo antes de avanzar: hacer el trabajo, ejecutar validador, corregir, repetir hasta que pase.

#### Plan-validate-execute

Para operaciones batch o destructivas: crear plan intermedio en formato estructurado, validar contra fuente de verdad, ejecutar solo cuando validacion pasa. El ingrediente clave es un script de validacion que verifica el plan contra la fuente de verdad.

### 7.8 Testing en SDK de plugins

Para plugins que incluyen skills:
- Usar `sdk-testing` del SDK de plugins OpenClaw
- Tests unitarios para herramientas del plugin
- Verificar que skills se cargan correctamente cuando el plugin esta habilitado

## 8. Validacion y aprobaciones

### 8.1 Validacion de elegibilidad

OpenClaw filtra skills en tiempo de carga evaluando secuencialmente:
1. `always: true` — salta todos los filtros
2. `os` — plataforma actual debe estar en la lista
3. `requires.bins` — todos deben existir en PATH del host
4. `requires.anyBins` — al menos uno debe existir
5. `requires.env` — variable debe existir en entorno o estar provista en config
6. `requires.config` — ruta en `openclaw.json` debe ser truthy
7. `enabled` en config — `false` descarta
8. `allowBundled` — si definido, solo bundled listados pasan

### 8.2 Aprobaciones de ejecucion (exec approvals)

Sistema de exec approvals general: ver manual integral §7.4. Cuando un skill invoca herramientas de ejecucion (`exec`), el sistema de aprobaciones controla el acceso:

| Nivel | Comportamiento |
| --- | --- |
| `deny` | Deniega toda ejecucion |
| `allowlist` | Solo comandos en la lista de aprobacion permitidos; nuevos requieren aprobacion |
| `full` | Permite toda ejecucion sin aprobacion |

Configuracion gateway: `tools.exec.security` en `openclaw.json` o `/exec security=<nivel>` en runtime.

**Policy host-local** — ademas de la config del gateway, existe una policy local persistida en `~/.openclaw/exec-approvals.json` que puede forzar prompts de aprobacion aunque la config del gateway diga `full`. La **politica mas estricta prevalece** entre gateway config y host-local policy.

Campos de la policy host-local:

| Campo | Descripcion |
| --- | --- |
| `security` | `deny` / `allowlist` / `full` |
| `ask` | `off` / `on-miss` / `always` — cuando solicitar aprobacion interactiva |
| `askFallback` | `deny` / `allowlist` / `full` — fallback si no hay operador para aprobar |
| `strictInlineEval` | Controla evaluacion de scripts inline |

Allowlists per-agent: patrones glob case-insensitive en la entry del agente. Shell chains se evaluan comando por comando. Skills instalados via `skills.install` auto-registran sus CLIs en el allowlist.

Aprobacion interactiva: `/approve <id> allow-once|allow-always|deny`. Aprobaciones se pueden reenviar a canales de chat.

### 8.3 Herramientas elevadas

Modo elevated general: ver manual integral §7.4. Modo elevated (`/elevated on|off|ask|full`) habilita herramientas restringidas. `full` salta aprobaciones de exec.

Configuracion de allowlists:
- `tools.elevated.allowPatterns` — patrones de comandos permitidos
- `tools.elevated.denyPatterns` — patrones denegados

### 8.4 Deteccion de loops

Deteccion de invocaciones ciclicas de herramientas:
- Monitoreo de patrones repetitivos en llamadas tool
- Interrupcion automatica al detectar ciclo
- Alerta al operador con detalle del loop
