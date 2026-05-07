---
canario: ifml-baseline
runtime: claude-code
subagent: ifml
subagent_source: ~/.claude/skills/ifml/SKILL.md
subagent_source_urn: urn:kora:artefacto:ifml
transmuted_at: 2026-05-07T00:00:00+00:00
baseline_captured_at: 2026-05-07
baseline_status: pasa-estricto
invocation_mode: interactivo
capture_mechanism: session log (claude-code system-reminder + tool calls)
kb_edit_propagation: verificado
canario_marker: 2026-05-07-ifml-deep-opm-pro-baseline-v1
---

# Canario baseline — skill IFML (claude-code)

Fixture canónica del input y criterios de aceptación para la primera
invocación productiva con eval de la skill `ifml` proyectada al runtime
`claude-code`.

Mantener este archivo sincronizado con `artifacts/skills/kora/ifml/SKILL.md`.
Si la skill cambia de corpus o de shape, re-transmutar y capturar un nuevo
baseline.

## Prompt canónico

Invocar desde sesión de claude-code con la skill IFML cargada:

```
Modela estructuralmente en IFML la vista principal del modelador OPM
(deep-opm-pro). El código fuente está en ~/deep-opm-pro/src/App.tsx.
La app es una SPA web con canvas interactivo (JointJS), tree panel,
inspector, toolbar y modales. Identifica la composición de
ViewContainers, ViewComponents, patrones IFML aplicables (cita URNs
del corpus), y cualquier fallo estructural o inconsistencia de UX.
```

## Knowledge Contract esperado

La skill declara acceso únicamente a estas URNs del corpus IFML:

- `urn:fxsl:kb:ifml-corpus-index` → ifml-corpus-index.md
- `urn:fxsl:kb:ifml-fundamentos` → ifml-fundamentos.md
- `urn:fxsl:kb:ifml-view-containers` → ifml-view-containers.md
- `urn:fxsl:kb:ifml-view-components` → ifml-view-components.md
- `urn:fxsl:kb:ifml-actions-events` → ifml-actions-events.md
- `urn:fxsl:kb:ifml-extensiones-desktop` → ifml-extensiones-desktop.md
- `urn:fxsl:kb:ifml-extensiones-web` → ifml-extensiones-web.md
- `urn:fxsl:kb:ifml-extensiones-mobile` → ifml-extensiones-mobile.md
- `urn:fxsl:kb:ifml-patrones` → ifml-patrones.md

No debe inventar patrones ni constructos fuera del corpus IFML. Si una
decisión de modelado requiere un constructo no cubierto, debe declarar
el supuesto del modelador explícitamente.

## Gate multinivel

| # | Criterio | Pregunta operacional |
|---|----------|----------------------|
| 1 | Trazabilidad al corpus | ¿Cita al menos 3 URNs del corpus IFML con precisión (código de patrón XY-Z + archivo)? |
| 2 | Composición jerárquica | ¿Produce un árbol de ViewContainers con niveles, tipos (conjuntiva/XOR) y anotaciones de plataforma? |
| 3 | Patrones aplicados | ¿Asigna patrones IFML canónicos (O*, CN-*, DE-*, CS-*, CM-*) a tareas concretas de la UI con justificación? |
| 4 | Hallazgos estructurales | ¿Identifica al menos un fallo de UX no-obvio con diagnóstico IFML (constructo + patrón + solución) y severidad? |
| 5 | Respeto del corpus | ¿No inventa URNs, patrones ni constructos fuera de `urn:fxsl:kb:ifml-*`? |

Criterio #4 es el discriminante: distingue output decorativo (diagrama) de
outcome validado (hallazgo que la intuición no detectó). Si los hallazgos
son obvios sin la lente IFML, el canario es `parcial`.

## Output de referencia

Corresponde al modelo IFML de la vista principal de deep-opm-pro capturado
el 2026-05-07. El output completo está en la sesión de claude-code de esa
fecha (ver Evidencia y trace).

### Encuadre
- Plataforma: Web SPA con interacción canvas tipo desktop (preact + jointjs)
- Roles: 1 (operador único, sin RBAC)
- Adaptación: ContextVariable oplLateral, oplMinimizado, vistaMapaActiva, dirty
- Familias de patrones: O* + CN-* + DE-* + CS-* + CM-*

### Composición (ViewContainer)
```
[D] [L] OPMModelerApp                                     «window-spa»
├── Toolbar                                               (conjuntiva)
├── BarraPestanas                                         (conjuntiva)
├── XOR Workbench-OPL-layout
│   ├── Workbench (oplLateral=false, default)
│   │   ├── TreePane → ArbolOpd                          (Tree desktop ext)
│   │   ├── CanvasPane
│   │   │   └── XOR
│   │   │       ├── [D] JointCanvas
│   │   │       └── MapaSistema
│   │   ├── InspectorPane
│   │   │   ├── Inspector  (Form, DE-PLDF)
│   │   │   ├── Timeline   (List)
│   │   │   └── PanelAvisos (List)
│   │   └── OPLInferior → PanelOpl                       (conjuntivo bottom)
│   └── WorkbenchOplLateral (oplLateral=true)
│       ├── TreePane / CanvasPane / InspectorPane
│       └── OPLLateral → PanelOpl                        (conjuntivo right)
└── XOR Modales
    ├── AsistenteNuevoModelo                             «modal»
    ├── DialogoGuardarComo / DialogoCargarModelo / ...   «modal»
    └── GestionArbolOpd                                  «modal»
```

### Patrones aplicados (tabla)
| Tarea | Patrón | URN |
|-------|--------|-----|
| Layout general top-tabs-tree-canvas-inspector-opl | OD-MCWA | urn:fxsl:kb:ifml-patrones |
| Tree → Canvas selection | CN-MD + Tree extension | urn:fxsl:kb:ifml-extensiones-desktop + urn:fxsl:kb:ifml-view-components |
| Canvas → Inspector (selección) | CN-MD (master-detail) | urn:fxsl:kb:ifml-view-components |
| Wizard nuevo modelo | DE-WIZ | urn:fxsl:kb:ifml-view-components |
| Inspector form precargado con selección | DE-PLDF | urn:fxsl:kb:ifml-view-components |
| Búsqueda local/global | CS-SRC | urn:fxsl:kb:ifml-view-components |
| CRUD de modelo | CM-OCR, CM-OM, CM-ODL | urn:fxsl:kb:ifml-actions-events |
| Vista canvas vs MapaSistema | OD-MWA | urn:fxsl:kb:ifml-patrones |
| Drag entre cosas para crear link | OnDragStart + OnDrop | urn:fxsl:kb:ifml-extensiones-desktop |
| Inspector field auto-save | OnFocusLost | urn:fxsl:kb:ifml-extensiones-desktop |

### Hallazgos estructurales

Hallazgo 1 (alto): InspectorPane mezcla 3 ViewComponent con contratos de
input distintos (Inspector ← seleccionCanvas, Timeline ← pestanaActivaId,
PanelAvisos ← pestanaActivaId). Diagnóstico IFML: tres ViewComponent con
ParameterBinding distintos compartiendo ViewContainer. Solución: CN-DEF con
default selection o empty state explícito.

Hallazgo 2 (alto): Atajos canvas-only sin marca de Context activo (Ctrl+F,
Ctrl+A, etc. dependen de focoCanvas:bool no materializado en UI). Solución:
status bar o color del pane activo.

Hallazgo 3 (medio): GestionArbolOpd rompe convención de control — siempre
montado con auto-control vía store, mientras el resto de modales usan
control centralizado en App. Inconsistencia de patrón.

Hallazgo 4 (medio): Empty state no modelado para "sin OPD activo".
JointCanvas recibe seleccionOpd sin ConditionalExpression.

Hallazgo 5 (medio): Selección canvas↔mapa sin parameter binding declarado.
vistaMapaActiva es XOR entre JointCanvas y MapaSistema; Inspector consume
ambos sin transformación declarada.

### Veredicto: pasa-estricto

El criterio #4 se satisface: los hallazgos 1, 3 y 5 fueron confirmados
como no-obvios por el operador (Felix) sin la lente IFML.

## Evidencia y trace

- Skill cargada vía system-reminder de claude-code
- Tool calls registrados: Read sobre App.tsx de deep-opm-pro + 9 URNs
  del corpus IFML
- Output: modelo estructural completo con 5 hallazgos y tabla de patrones
- Veredicto del operador: al menos uno de los hallazgos 1/3/5 era no-obvio
  → canario PASA
- Invocación registrada: `python3 toolchain/kora record-invocation
  --agent-urn urn:kora:artefacto:ifml --eval-result pasa-estricto`
  el 2026-05-07 (registro en docs/generated/invocations.jsonl)

## Lazo Kelly reproducible

```bash
# 1. Skill ya está desplegada en ~/.claude/skills/ifml/
# 2. Invocar en sesión fresca de claude-code:
#    > Carga la skill IFML y modela estructuralmente la vista principal
#    > de deep-opm-pro (~/deep-opm-pro/src/App.tsx).
# 3. Verificar que el output contiene:
#    - Árbol de ViewContainers con tipos y anotaciones
#    - Tabla de patrones con ≥3 URNs del corpus IFML
#    - Al menos 1 hallazgo con severidad + diagnóstico IFML + solución
# 4. Preguntar al operador: ¿algún hallazgo te era no-obvio?
#    Sí → pasa-estricto. No → parcial (output decorativo).
# 5. Registrar: python3 toolchain/kora record-invocation
#    --agent-urn urn:kora:artefacto:ifml
#    --eval-result {pasa-estricto|parcial}
```

## Deuda registrada

1. Canario manual (invocación interactiva, no headless). Automatizar
   requiere que claude-code soporte invocación de skills con prompt
   programático + captura de trace. Deuda de tooling, no de skill.
2. Fixture único (deep-opm-pro). Ampliar con segundo caso (web app
   distinta, ej. dashboard o e-commerce) para validar generalización.
3. Sin canario adversarial (app sin fallos IFML estructurales). Necesario
   para probar que la skill no sobre-diagnostica.
