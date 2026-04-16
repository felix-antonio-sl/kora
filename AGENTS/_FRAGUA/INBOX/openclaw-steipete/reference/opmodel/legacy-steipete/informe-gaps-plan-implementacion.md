# opmodel — Informe de Gaps y Plan de Implementación

Fecha: 2026-03-26  
Autor: Steipete  
Baseline: 972 tests, 66 files, commit 323fc0e

---

## 1. Estado actual reconstruido

### 1.1 Arquitectura del proyecto

```
packages/
  core/     — modelo OPM, API, OPL, simulación, validación metodológica, serialización
  web/      — editor visual React (canvas SVG, paneles, layout engine, linting visual)
  cli/      — CLI de modelado (add, remove, refine, validate, etc.)
  nl/       — pipeline de lenguaje natural → modelo OPM
```

### 1.2 Métricas de código

| Módulo | Archivos fuente | LOC aprox |
|--------|----------------|-----------|
| core/src | 15 archivos | ~6,596 |
| web/src/lib | 7 archivos | ~1,756 |
| web/src/components | 16 archivos | ~6,095 |
| web/src/hooks | 1 archivo | ~257 |
| web/src/App.tsx | 1 archivo | ~870 |
| **Total fuente** | **~40** | **~15,574** |
| **Tests** | **66 archivos** | **972 tests** |

### 1.3 Fixtures

| Fixture | Descripción |
|---------|-------------|
| coffee-making.opmodel | Ejemplo introductorio |
| driver-rescuing.opmodel | OnStar, ejemplo ISO clásico |
| hospitalizacion-domiciliaria.opmodel | HODOM legacy (48 things, 82 links, 6 OPDs) |
| hodom-v2.opmodel | HODOM V2 reconstruido con metodología OPM |
| ev-ams.opmodel | EV-AMS canónico (5 OPDs, 49 things, 54 links) |

### 1.4 Features implementados (sesiones 17-actuales)

#### Core engine
- Modelo OPM completo: things, states, links, modifiers, fans, OPDs, appearances
- Tipos estructurales: aggregation, exhibition, generalization, classification, tagged
- Herencia estructural (§11): links heredados visibles en canvas
- Compound states + tagged links + ordered aggregation
- Simulación ECA coalgebraica completa
- Monte Carlo con assertions
- Scenarios, time-based scheduling, unfold cascade
- Exception handling, invocation chains, condition negation
- OPL bilingüe (EN/ES) con renderAll, editsFrom
- Validación metodológica (17 checks, §6.11, §7.6, §10)
- Serialización JSON estable
- Export markdown

#### Visual core (web)
- Canvas SVG interactivo con zoom, pan, fit-to-content
- Editor de propiedades completo
- OPL panel con clickable sentences
- Simulation panel con trace visual
- Settings panel (OPL locale, essence visibility, units, etc.)
- SD Wizard (10-step guided construction)
- Verification Checklist UI
- **Visual lint**: overlaps, orphans, truncated states, degenerate bounds, crowded diagrams, tight spacing
- **Spatial layout engine**: 6 estrategias (in-zoom-sequential, unfold-grid, branching-control, structural-cluster, sd-balanced, none)
- **Post-layout relaxation**: lane-aware, iterativa
- **Visual quality scoring**: grade A-F por OPD + modelo
- **Visual report panel**: resumen de calidad por modelo
- Auto-layout batch para todos los OPDs
- Pin/unpin + lock-size en context menu
- Link filter + label toggle
- Alignment tools + grid snap
- Duplicate visual, Ctrl+A/D
- Fork triangles ISO §6
- Ghost/implicit things toggle

#### Visual audit results (actual)

| Fixture | OPDs | Errors | Warnings | Info | Grades |
|---------|------|--------|----------|------|--------|
| HODOM legacy | 6 | 0 | 4 | 29 | All A (92-97) |
| HODOM V2 | 2 | 0 | 2 | 2 | All A (97-99) |
| EV-AMS | 6 | 0 | 0 | 11 | All A (95-100) |

---

## 2. Diagnóstico de gaps

### 2.1 Categorías de gap

Los gaps se organizan en 5 categorías por prioridad:

- **P0 — Critical**: bloquean uso profesional
- **P1 — High**: limitan significativamente la experiencia
- **P2 — Medium**: mejoran calidad pero no bloquean
- **P3 — Low**: nice-to-have, polish
- **P4 — Future**: expansión post-MVP

---

### 2.2 Gaps identificados

## GAP-V01 — OpdCanvas.tsx monolítico (2,317 LOC)

**Categoría:** P0 — Critical  
**Área:** web/components  
**Impacto:** Mantenibilidad, rendimiento, extensibilidad

El componente principal del canvas es un archivo de 2,317 líneas con ~275 funciones/constantes. Contiene:
- rendering de things (objects, processes)
- rendering de states
- rendering de links (14 tipos)
- rendering de modifiers (events, conditions)
- rendering de forks/fans
- ghost/implicit things
- drag & drop
- selection
- link drawing mode
- simulation overlay
- breadcrumb
- context menu
- keyboard shortcuts

**Acción:** Descomponer en sub-componentes: ThingNode, LinkEdge, ModifierMarker, ForkTriangle, CanvasOverlay, ContextMenu, Breadcrumb. Mantener OpdCanvas como compositor.

---

## GAP-V02 — No hay rendering de links curvados / routing inteligente

**Categoría:** P0 — Critical  
**Área:** web/components  
**Impacto:** Legibilidad visual en diagramas densos

Actualmente los links se dibujan como líneas rectas punto a punto. En diagramas con muchos links (HODOM SD1: 60 links), las líneas se cruzan y superponen haciendo el diagrama difícil de leer.

**Acción:** Implementar edge routing con:
1. Curvas Bézier para links que se cruzan
2. Bundling de links paralelos
3. Detección de cruces y re-routing
4. Orthogonal routing como opción

---

## GAP-V03 — No hay export SVG/PNG/PDF

**Categoría:** P0 — Critical  
**Área:** web  
**Impacto:** Uso profesional — no se pueden generar entregables visuales

El editor no puede exportar los diagramas a formatos de imagen o documento.

**Acción:** Implementar:
1. Export SVG (directo del canvas)
2. Export PNG (via canvas → rasterización)
3. Export PDF (multi-OPD document)

---

## GAP-V04 — No hay undo/redo en UI

**Categoría:** P1 — High  
**Área:** web  
**Impacto:** UX crítico — el usuario no puede deshacer errores

El core tiene `History` (createHistory, pushHistory, undo, redo), y el store lo expone. Verificar si Ctrl+Z/Y están wired en la UI. Si no, conectar.

**Acción:** Verificar wiring de undo/redo en App.tsx y OpdCanvas. Si no está conectado, implementar Ctrl+Z/Ctrl+Y.

---

## GAP-V05 — No hay multi-select + bulk operations

**Categoría:** P1 — High  
**Área:** web/components  
**Impacto:** Productividad de edición

Ctrl+A selecciona todo, pero no hay:
- rubber band selection (drag para seleccionar área)
- shift+click para agregar a selección
- operaciones bulk (mover grupo, alinear grupo, delete grupo)

**Acción:** Implementar SelectionManager con rubber band, shift+click, y bulk move/delete/align.

---

## GAP-V06 — No hay copy/paste de things entre OPDs

**Categoría:** P1 — High  
**Área:** web  
**Impacto:** Productividad de modelado

Para mover o replicar things entre OPDs hay que recrearlos manualmente.

**Acción:** Implementar clipboard interno con copy/cut/paste que maneje appearances cross-OPD.

---

## GAP-V07 — api.ts monolítico (2,076 LOC)

**Categoría:** P1 — High  
**Área:** core/src  
**Impacto:** Mantenibilidad del core

El archivo api.ts contiene TODAS las operaciones CRUD + validate en un solo archivo.

**Acción:** Descomponer en módulos: api-things.ts, api-links.ts, api-opds.ts, api-appearances.ts, api-validate.ts.

---

## GAP-V08 — simulation.ts grande (1,640 LOC)

**Categoría:** P2 — Medium  
**Área:** core/src  
**Impacto:** Mantenibilidad

Archivo grande pero cohesivo (simulación ECA). Menos urgente que api.ts.

**Acción:** Considerar split en simulation-engine.ts (motor), simulation-mc.ts (Monte Carlo), simulation-trace.ts (rendering trace).

---

## GAP-V09 — No hay zoom semántico

**Categoría:** P2 — Medium  
**Área:** web  
**Impacto:** Navegación en modelos grandes

Al hacer zoom out, los detalles (state pills, labels, modifiers) siguen renderizando a la misma escala. En modelos grandes, al alejar no se distingue nada útil.

**Acción:** Implementar niveles de detalle:
- Zoom > 80%: todo visible
- Zoom 40-80%: ocultar state pills, simplificar labels
- Zoom < 40%: solo shapes + nombre principal

---

## GAP-V10 — No hay minimap / overview

**Categoría:** P2 — Medium  
**Área:** web  
**Impacto:** Navegación en diagramas grandes

No hay forma de ver el diagrama completo en miniatura ni navegar rápido a otras áreas.

**Acción:** Implementar minimap en esquina del canvas.

---

## GAP-V11 — Links no tienen waypoints editables

**Categoría:** P2 — Medium  
**Área:** web  
**Impacto:** Control fino de layout de links

Los links van de punto a punto sin posibilidad de agregar puntos intermedios para guiar la ruta.

**Acción:** Implementar waypoints en links: click en link para agregar punto, drag para mover.

---

## GAP-V12 — No hay annotation layer

**Categoría:** P2 — Medium  
**Área:** web  
**Impacto:** Documentación visual

No se pueden agregar notas, labels libres o marcas visuales al diagrama fuera del modelo formal.

**Acción:** Implementar capa de anotaciones: text boxes libres, flechas de anotación, colored regions.

---

## GAP-V13 — PropertiesPanel.tsx grande (1,198 LOC)

**Categoría:** P2 — Medium  
**Área:** web/components  
**Impacto:** Mantenibilidad

Panel de propiedades con muchos sub-editores inline.

**Acción:** Extraer sub-componentes: ThingProperties, StateEditor, LinkProperties, ModifierEditor, etc.

---

## GAP-V14 — No hay dark mode

**Categoría:** P3 — Low  
**Área:** web  
**Impacto:** Preferencia visual

**Acción:** Implementar CSS variables + toggle.

---

## GAP-V15 — No hay keyboard shortcut reference

**Categoría:** P3 — Low  
**Área:** web  
**Impacto:** Discoverability

**Acción:** Modal con lista de shortcuts (Ctrl+? o F1).

---

## GAP-V16 — No hay collaborative editing

**Categoría:** P4 — Future  
**Área:** arquitectura  
**Impacto:** Trabajo en equipo

**Acción:** CRDT o OT sobre el modelo. Post-MVP.

---

## GAP-V17 — No hay import desde otros formatos

**Categoría:** P4 — Future  
**Área:** core  
**Impacto:** Interoperabilidad

Import desde BPMN, SysML, o archimate como mapeo parcial a OPM.

---

## GAP-V18 — NL pipeline sin integración profunda

**Categoría:** P2 — Medium  
**Área:** nl  
**Impacto:** Usabilidad de modelado asistido

El paquete `nl` existe con parse, resolve, pipeline, pero la integración en la UI es via modal de settings. No hay "describe tu sistema y genera el modelo".

**Acción:** Implementar flujo conversacional: text input → pipeline → preview → apply.

---

## GAP-V19 — No hay tests de rendering visual (snapshot tests)

**Categoría:** P2 — Medium  
**Área:** web/tests  
**Impacto:** Regresiones visuales

Los tests actuales validan layout/lint pero no el rendering SVG real.

**Acción:** Implementar snapshot tests del SVG generado por OpdCanvas con fixtures canónicas.

---

## GAP-V20 — No hay performance profiling para modelos grandes

**Categoría:** P2 — Medium  
**Área:** web  
**Impacto:** Escalabilidad

No hay datos sobre rendimiento con modelos de 100+ things o 200+ links.

**Acción:** Crear fixture grande sintético, medir FPS de canvas, identificar bottlenecks.

---

## 3. Resumen de gaps por prioridad

| Prioridad | Count | Gaps |
|-----------|-------|------|
| **P0 — Critical** | 3 | V01, V02, V03 |
| **P1 — High** | 3 | V04, V05, V06 (+ V07 refactor) |
| **P2 — Medium** | 8 | V08, V09, V10, V11, V12, V13, V18, V19, V20 |
| **P3 — Low** | 2 | V14, V15 |
| **P4 — Future** | 2 | V16, V17 |

---

## 4. Plan de implementación

### Fase 1 — Fundamentos de calidad visual (P0)

**Objetivo:** Hacer los diagramas exportables y visualmente profesionales.  
**Estimación:** 3-5 sesiones de trabajo

#### Sprint 1.1 — Descomponer OpdCanvas (GAP-V01)
- Extraer ThingNode.tsx (~300 LOC: rendering de object/process shapes + states)
- Extraer LinkEdge.tsx (~400 LOC: rendering de los 14 tipos de link + arrows + labels)
- Extraer ModifierMarker.tsx (~100 LOC: event/condition rendering)
- Extraer ForkTriangle.tsx (~80 LOC: fan rendering)
- Extraer ContextMenu.tsx (~150 LOC: right-click menu)
- Extraer Breadcrumb.tsx (~50 LOC: OPD navigation)
- OpdCanvas queda como compositor (~800-900 LOC)

**Criterio de éxito:** 972 tests siguen green, canvas se ve idéntico, ningún componente > 500 LOC.

#### Sprint 1.2 — Edge routing (GAP-V02)
- Implementar `edge-router.ts` en web/src/lib/
- Detectar cruces entre links
- Curvas Bézier para links que cruzan otros links
- Bundling de links paralelos (mismo source→target direction)
- Orthogonal routing opcional (toggle en settings)

**Criterio de éxito:** HODOM SD1 (60 links) sin cruces innecesarios, visual audit sin warnings de crossing.

#### Sprint 1.3 — Export SVG/PNG/PDF (GAP-V03)
- Export SVG: serializar el canvas SVG actual con estilos inlined
- Export PNG: SVG → canvas → blob → download
- Export PDF: multi-page, un OPD por página, con header (model name, OPD name)
- Botones en File menu + keyboard shortcuts

**Criterio de éxito:** Los 3 formatos generan output correcto para las 5 fixtures.

---

### Fase 2 — UX de edición (P1)

**Objetivo:** Hacer la edición fluida y productiva.  
**Estimación:** 2-3 sesiones

#### Sprint 2.1 — Undo/Redo + Multi-select (GAP-V04, V05)
- Verificar/completar wiring de Ctrl+Z/Ctrl+Y
- Implementar rubber band selection
- Shift+click para toggle selection
- Bulk move (drag grupo)
- Bulk delete
- Bulk align (usar alignment tools existentes)

**Criterio de éxito:** Undo/redo funciona para todas las operaciones. Rubber band selecciona correctamente.

#### Sprint 2.2 — Copy/Paste cross-OPD (GAP-V06)
- Clipboard interno (no system clipboard por complejidad)
- Copy: serializar selection (things + appearances + states + links internos)
- Paste: deserializar en OPD destino, generar nuevos IDs, crear appearances
- Cut = Copy + Delete

**Criterio de éxito:** Copy thing de SD a SD1 funciona, mantiene states y links internos.

---

### Fase 3 — Refinamiento visual (P2)

**Objetivo:** Polish visual y navegación avanzada.  
**Estimación:** 3-4 sesiones

#### Sprint 3.1 — Zoom semántico + Minimap (GAP-V09, V10)
- Implementar LOD (level of detail) en ThingNode basado en zoom scale
- Minimap con viewport indicator
- Click en minimap para navegar

#### Sprint 3.2 — Waypoints en links (GAP-V11)
- Agregar `waypoints: Point[]` a Link o a una estructura visual separada
- Click en link para agregar waypoint
- Drag waypoint para mover
- Double-click para eliminar waypoint

#### Sprint 3.3 — Annotation layer (GAP-V12)
- Implementar capa de anotaciones sobre el canvas
- Text boxes libres
- Flechas de anotación
- Serialización en el modelo (.opmodel)

#### Sprint 3.4 — NL pipeline integration (GAP-V18)
- Chat input en sidebar
- Text → pipeline → preview de cambios
- Apply / reject
- Historial de prompts

---

### Fase 4 — Refactoring + Testing (P1-P2)

**Objetivo:** Deuda técnica y robustez.  
**Estimación:** 2 sesiones

#### Sprint 4.1 — Descomponer api.ts y PropertiesPanel (GAP-V07, V13)
- Split api.ts en módulos por entidad
- Split PropertiesPanel en sub-componentes

#### Sprint 4.2 — Snapshot tests + Performance (GAP-V19, V20)
- SVG snapshot tests para fixtures canónicas
- Fixture sintética grande (200 things, 300 links)
- Profiling de canvas FPS
- Optimizaciones si hay bottlenecks

---

### Fase 5 — Polish (P3)

**Objetivo:** Calidad de producto.  
**Estimación:** 1 sesión

#### Sprint 5.1 — Dark mode + Shortcuts reference (GAP-V14, V15)
- CSS variables para theming
- Toggle light/dark
- Modal de keyboard shortcuts

---

## 5. Dependencias entre sprints

```
Sprint 1.1 (descomponer canvas) ──→ Sprint 1.2 (edge routing)
                                  ──→ Sprint 2.1 (multi-select)
                                  ──→ Sprint 3.1 (zoom semántico)

Sprint 1.3 (export) ──→ independiente

Sprint 2.1 (undo + multi-select) ──→ Sprint 2.2 (copy/paste)

Sprint 3.1 (zoom + minimap) ──→ independiente
Sprint 3.2 (waypoints) ──→ depende de Sprint 1.2 (edge routing)
Sprint 3.3 (annotations) ──→ independiente
Sprint 3.4 (NL integration) ──→ independiente

Sprint 4.1 (refactor) ──→ independiente (puede paralelizarse)
Sprint 4.2 (testing) ──→ después de Sprint 1.1

Sprint 5.1 (polish) ──→ independiente
```

---

## 6. Ruta crítica recomendada

```
Fase 1.1 → Fase 1.2 → Fase 1.3 → Fase 2.1 → Fase 2.2 → Fase 3.*
```

**Razón:** La descomposición del canvas (1.1) desbloquea todo lo demás. Edge routing (1.2) tiene el mayor impacto visual. Export (1.3) habilita uso profesional. Multi-select (2.1) es la mayor mejora de productividad de edición.

---

## 7. Quick wins (ejecutables en < 1 hora cada uno)

Estos no tienen gap formal pero agregan valor rápido:

1. **Keyboard shortcut overlay** (F1 → modal con lista)
2. **Tooltip mejorado en links** (mostrar tipo + source→target)
3. **Auto-save indicator** en toolbar
4. **OPD tab bar** (además del tree, tabs para OPDs abiertos)
5. **Confirmation dialog** para delete thing con links

---

## 8. Resumen ejecutivo

| Métrica | Actual | Post-Fase 1 | Post-Fase 2 | Post-Todo |
|---------|--------|-------------|-------------|-----------|
| Tests | 972 | ~1,020 | ~1,060 | ~1,150 |
| Max component LOC | 2,317 | ~900 | ~900 | ~500 |
| Export formatos | 1 (.opmodel) | 4 (+SVG, PNG, PDF) | 4 | 4 |
| Link routing | Recto | Curvo+Bundle | Curvo+Waypoints | Completo |
| Multi-select | No | Sí | Sí | Sí |
| Zoom semántico | No | No | No | Sí |
| Visual quality (avg) | A (95+) | A (97+) | A (98+) | A (99+) |

---

## 9. Siguiente paso recomendado

**Empezar por Sprint 1.1: descomponer OpdCanvas.tsx.**

Es el gap que más desbloquea. Sin descomponerlo, cada cambio en el canvas visual es riesgoso y lento. Con la descomposición:

- edge routing se implementa limpio en LinkEdge
- multi-select se integra sin tocar rendering
- zoom semántico se implementa por componente
- los tests de snapshot son viables

¿Confirmas para arrancar con Sprint 1.1?
