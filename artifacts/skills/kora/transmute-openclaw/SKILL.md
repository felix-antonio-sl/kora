---
_manifest:
  urn: urn:kora:artefacto:transmute-openclaw
  type: artefacto
  provenance:
    created_by: FS
    created_at: '2026-04-23'
    source: 'Migracion desde artifacts/skills/_TALLER/INBOX/transmute-openclaw/SKILL.md
      (legacy skill-overlay v1) a shape unified autoria-spec v1.2; URN regimen artefacto:'
version: 2.0.0
status: activo
nombre: transmute-openclaw
descripcion: Transmuta un AGENT.md KORA a un workspace OpenClaw completo (AGENTS.md,
  SOUL.md, USER.md, TOOLS.md, config.json, skills/). Compila las 6 dimensiones categoricas
  del IR al formato nativo de OpenClaw con maxima fidelidad; unico runtime que soporta
  agente-plataforma.
tags:
- transmutacion
- openclaw
- proyeccion
- runtime
- workspace
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 2
      mu: 0
      xi: 2
      lambda: 0
      phi: 1
      sigma:
      - 2
      - 1
      - 3
      - 1
      - 0
    presentacion: accion-primaria
    atlas:
      arnes_categorico: utilidad
      forma_material: habilidad
      metafora_relacional: supertool
    entornos_objetivo:
    - claude-code
    - codex
    nivel_prescripcion: alto
    conocimiento_permitido:
    - urn:kora:kb:autoria-spec
    - urn:kora:kb:transmutation-spec
    - urn:agengai:kb:openclaw-runtime-extension
    componible_con: []
artefacto:
  perfil:
    descripcion: Habilidad de transmutacion que proyecta artefactos KORA/MD a workspaces
      OpenClaw completos con bootstrap, config y trazabilidad.
    dominio:
    - transmutacion de runtime
    - OpenClaw
    - workspaces agenticos
    salidas:
    - workspace OpenClaw
    - config de runtime
    - registro _transmutation.yml
  interfaz:
    herramientas: []
    permisos:
      allow: []
      deny: []
  invariantes:
    reglas_duras:
    - "Toda perdida estructural respecto al IR canonico DEBE registrarse en _transmutation.yml; nunca silenciar."
    - "URN del artefacto fuente DEBE preservarse en config/openclaw.json5.agent.urn; la transmutacion no reescribe identidad."
    - "Si forma_material es agente-plataforma, always_on: true es obligatorio en la config emitida."
    - "Paths absolutos NO deben aparecer en el workspace generado; toda variable debe resolverse al compilar."
---

# Transmute OpenClaw

Funtor T_{openclaw} : IR_KORA -> OpenClaw. Proyecta un artefacto agentico unified a un workspace OpenClaw con archivos bootstrap separados. OpenClaw es el unico runtime que soporta `forma_material: agente-plataforma` (Mu=3 ambiental).

## Objetivo

Emitir un workspace OpenClaw completo desde un `AGENT.md` KORA. El target debe ser funcional para systemd user units y compatible con el gateway OpenClaw actual (puerto 18790 en Clawforge 3G).

## Cuando Usar

- Desplegar un agente KORA al runtime OpenClaw (local o produccion).
- Regenerar workspace OpenClaw tras cambios en el IR.
- Proyectar artefactos `agente-plataforma` (unico runtime soportado).
- Preservar fibras especificas de OpenClaw (bot_handler telegram, ACP, persistencia ambiental).

## Entrada / Salida

### Entrada

- Path al directorio KORA: `artifacts/agents/{ns}/{nombre}/`.
- Directorio de output (default `_BUILD/openclaw/{ns}/{nombre}/`).

### Salida

```
_BUILD/openclaw/{ns}/{nombre}/
  workspace/
    AGENTS.md
    SOUL.md
    USER.md
    TOOLS.md
    skills/
  config/
    openclaw.json5
  DEPLOY.md
  _transmutation.yml
```

## Workflow

### 1. Leer fuente

1. Parsear `AGENT.md`: frontmatter unified + body.
2. Extraer `artefacto.*` (6 dimensiones) y `extensions.openclaw.*`.
3. Resolver URNs en `conocimiento_permitido` via `kora resolve`.
4. Enumerar skills en `artefacto.composicion.sub_agentes` y skills referenciados.

### 2. Compilar `workspace/AGENTS.md`

FSM + transiciones en formato OpenClaw:

```markdown
# {nombre}

## 1. FSM

STATE: {estado_inicial}
Act: {accion del estado}
Trans:
  - IF {condicion} -> {destino} [prioridad {N}]
  ...

{repetir para cada estado}

STATE: S-END
Act: Emitir output final
Trans: (terminal)
```

### 3. Compilar `workspace/SOUL.md`

Desde `artefacto.perfil` + `artefacto.invariantes.compromisos_eticos`:

```markdown
# SOUL — {nombre}

## Identidad

{narrativa del perfil: dominio, paradigma, tono}

## Compromisos eticos

- safety_norm: {...}
- fairness: {...}
- transparency: {...}
- accountability: {...}
- sustainability: {...}

## Invariantes

{reglas_duras listadas}
```

### 4. Compilar `workspace/USER.md`

Desde `artefacto.contexto.perfil_operador` y `artefacto.perfil.disparadores`:

```markdown
# USER — perfil del operador

Rol: {perfil_operador}

Disparadores esperados:
{lista de disparadores}

Salidas esperadas:
{lista de salidas}
```

### 5. Compilar `workspace/TOOLS.md`

Desde `artefacto.interfaz.herramientas` + permisos:

```markdown
# TOOLS

{para cada herramienta:}
## {nombre}

Descripcion: {descripcion}
Cuando usar: {when_to_use}
Cuando NO usar: {when_not_to_use}
Parametros: {parameters}
```

Incluir tabla final de `permissions.allow` / `permissions.deny`.

### 6. Compilar `config/openclaw.json5`

```json5
{
  // Configuracion del agente OpenClaw
  agent: {
    name: "{nombre}",
    namespace: "{ns}",
    urn: "{urn}",
    version: "{version}",
  },
  runtime: {
    bot_handler: "{extensions.openclaw.bot_handler}",
    acp_compliant: {extensions.openclaw.acp_compliant},
    always_on: {true si forma_material == agente-plataforma},
    persistencia: "{extensions.openclaw.persistencia | "session"}",
  },
  model: {
    primary: "{extensions.openclaw.model | inferido}",
    fallback: "{extensions.openclaw.fallback | null}",
  },
  skills: [
    {para cada skill en composicion.sub_agentes:}
    { id: "{skill.id}", required: {skill.required} },
  ],
  gateway: {
    port: 18790,  // default Clawforge 3G
  },
}
```

### 7. Generar `DEPLOY.md`

Instrucciones de despliegue con los comandos concretos:

```markdown
# DEPLOY — {nombre}

## Requisitos

- OpenClaw CLI instalado.
- Gateway activo: `systemctl --user status openclaw-gateway`.
- Credenciales Telegram si `bot_handler: telegram`.

## Pasos

1. Copiar workspace:
   ```bash
   cp -r _BUILD/openclaw/{ns}/{nombre}/ ~/openclaw-fleet/{nombre}/
   ```
2. Validar config:
   ```bash
   openclaw doctor --agent {nombre}
   ```
3. Registrar agente:
   ```bash
   openclaw agent add {nombre}
   ```
4. Activar servicio:
   ```bash
   systemctl --user start openclaw-agent@{nombre}.service
   ```

## Verificacion

- `openclaw health`: gateway + agente verde.
- `journalctl --user -u openclaw-agent@{nombre} -f`: logs limpios.
- Telegram respondiendo al handler declarado.
```

### 8. Emitir `_transmutation.yml`

```yaml
ir_hash: "{sha256 del AGENT.md fuente}"
target: openclaw
output_dir: "_BUILD/openclaw/{ns}/{nombre}/"
transmuted_at: "{YYYY-MM-DD}"
fidelity:
  preserved:
    - artefacto.plan (FSM completa)
    - artefacto.interfaz.herramientas (tools completas)
    - artefacto.invariantes.compromisos_eticos
    - extensions.openclaw (todas las fibras)
  lost: []
  partial: []
```

## Matriz de fidelidad por forma material

| Forma material | Fidelidad | Observacion |
|----------------|-----------|-------------|
| `habilidad` | fiel | Copia a `workspace/skills/{nombre}/` con SKILL.md. |
| `subagente` | fiel | Registra en `composicion.sub_agentes` del padre. |
| `agente-propiamente-tal` | fiel | Workspace completo activable por systemd. |
| `agente-plataforma` | fiel (unico runtime) | Always-on con MEMORY.md y HEARTBEAT.md ambientales. |

## Recursos

Spec gobernante: `urn:agengai:kb:openclaw-runtime-extension`. No requiere recursos auxiliares adicionales.

## Invariantes

- URN **DEBE** conservarse en `config/openclaw.json5.agent.urn`.
- Si `forma_material == agente-plataforma`, `always_on: true` es obligatorio.
- Paths absolutos NO deben aparecer en el workspace generado; se usan paths relativos.
- `DEPLOY.md` **DEBE** ser ejecutable sin editar: toda variable resuelta en compilacion.

## Salida Esperada

- Workspace completo en `_BUILD/openclaw/{ns}/{nombre}/`.
- `_transmutation.yml` con registro de fidelidad.
- Status `ok|degraded|error`; degraded permitido solo si forma material es `agente-plataforma` con fallback documentado.
