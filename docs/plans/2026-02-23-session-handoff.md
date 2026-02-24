# Session Handoff — Remediación KODA/KORA

> **Para Claude Code:** Este documento contiene el estado completo de la remediación KODA/KORA al cierre de la sesión del 2026-02-23. Leerlo ANTES de cualquier acción.

**Fecha:** 2026-02-23
**Plan maestro:** `docs/plans/2026-02-23-koda-kora-remediation-plan.md`
**Design doc:** `docs/plans/2026-02-23-koda-kora-remediation-design.md`

---

## 1. Resumen Ejecutivo

Se está ejecutando un plan de 5 fases para eliminar la deuda técnica entre KODA (legacy, junio 2025) y KORA (actual, feb 2026). Las fases 0-2 están completadas y pusheadas. Las fases 3, 4 y F están pendientes.

---

## 2. Estado de Fases

| Fase | Descripción | Estado | Commits |
|------|-------------|--------|---------|
| **0** | Limpiar `tools/` (21 archivos obsoletos) | **COMPLETADA** | `3779cd6` |
| **1** | Re-fundamentar `agent-spec-md.md` v4.0.1 → v5.0.0 | **COMPLETADA** | `c49bda1`..`24ad782` (5 commits) |
| **2** | Diseñar Funtor G (§12 Agentificación) | **COMPLETADA** | `ecc395f` |
| **3** | Koraficiar 139 KBs (YAML → KORA/MD) | **PENDIENTE** | — |
| **4** | Agentificar 40 agentes (YAML → workspace) | **PENDIENTE** | — |
| **F** | Gobernanza, deprecación KODA, cierre | **PENDIENTE** | — |

**Commit HEAD actual:** `82e2742` (docs: agregar CLAUDE.md)

---

## 3. Cambios Sin Commitear

17 archivos borrados (unstaged) — son artefactos KODA y KORA legacy que deben ser commiteados como limpieza:

**`knowledge/foundations/core/koda/` (14 archivos, ~8,650 líneas):**
- `agent-construct.yml` (1406 líneas) — supersedido por agent-spec-md §12
- `agent-schema.json` (607) — schema KODA obsoleto
- `agent.yml` (971) — supersedido por agent-spec-md v5.0.0
- `gn-koda-schema.json` (33) — schema namespace legacy
- `hub-federation.yml` (1666) — pendiente evaluación en Phase F
- `life.yml` (582) — absorbido en agent-spec-md
- `quickstart.yml` (604) — guía KODA obsoleta
- `schema-versioning.yml` (507) — supersedido por convenciones KORA
- `skills-federation.yml` (119) — pendiente evaluación en Phase F
- `spec.yml` (417) — supersedido por md-spec.md + spec-md.md
- `test.yml` (649) — pendiente evaluación en Phase F
- `tooling-schema.json` (101) — schema obsoleto
- `tooling.yml` (449) — supersedido por limpieza tools/
- `transform.yml` (539) — absorbido en md-spec §6

**`knowledge/foundations/core/kora/` (3 archivos, ~442 líneas):**
- `agent-schema.json` (140) — schema legacy pre-v5.0.0
- `agent.yml` (110) — supersedido por agent-spec-md v5.0.0
- `spec.yml` (192) — supersedido por md-spec.md + spec-md.md

**Otros:**
- `scripts/__pycache__/` y `scripts/legacy_migration/__pycache__/` — ignorar (.gitignore)

**Acción recomendada:** Commitear estas eliminaciones como paso previo a Phase 3.

---

## 4. Specs Fundacionales (Estado Final)

| Archivo | Versión | Líneas | Estado |
|---------|---------|--------|--------|
| `knowledge/foundations/core/kora/agent-spec-md.md` | v5.0.0 | 672 | 12 secciones completas, §12 Funtor G incluido |
| `knowledge/foundations/core/kora/md-spec.md` | v2.0.0 | 677 | wf-koraficacion absorbido en §6 |
| `knowledge/foundations/core/kora/spec-md.md` | v2.1.0 | 439 | Sin cambios en esta sesión |
| `knowledge/foundations/core/kora/gobernanza.md` | v1.2.0 | 179 | Sin cambios en esta sesión |

---

## 5. Inventario de Trabajo Pendiente

### Phase 3: Koraficiar 139 KBs

**Distribución por directorio (139 archivos YAML total):**

| Directorio | Cantidad | Dominio |
|------------|----------|---------|
| `knowledge/applied/legal/` | 21 | Normativa legal chilena |
| `knowledge/applied/gn/gobernanza/` | 20 | Gobernanza regional |
| `knowledge/applied/gn/manuales/` | 14 | Manuales operacionales |
| `knowledge/applied/tde/guias/` | 13 | Guías transformación digital |
| `knowledge/applied/gn/bpmn/` | 11 | Procesos BPMN |
| `knowledge/applied/gn/ris/` | 10 | Resoluciones |
| `knowledge/applied/gov/` | 9 | Gobierno central |
| `knowledge/applied/gn/gestion/` | 8 | Gestión |
| `knowledge/applied/gn/guias/` | 7 | Guías GORE |
| `knowledge/applied/tde/plataformas/` | 6 | Plataformas TDE |
| `knowledge/applied/tde/normas_tecnicas/` | 6 | Normas técnicas |
| `knowledge/applied/gn/normativa/` | 6 | Normativa regional |
| `knowledge/applied/mgmt/` | 4 | Management |
| `knowledge/applied/tde/leyes/` | 2 | Leyes TDE |
| `knowledge/applied/tde/estrategia/` | 2 | Estrategia TDE |

**Proceso por artefacto** (plan §3.N):
1. Leer YAML source → evaluar pertinencia (MIGRAR/DEPRECAR/FUSIONAR)
2. Aplicar md-spec §6 (koraficación): segmentar, telegrafizar, ensamblar
3. Verificar (cifras preservadas, estructura KORA/MD válida)
4. Eliminar YAML source, actualizar catálogo
5. Commit cada 3-5 artefactos

### Phase 4: Agentificar 40 Agentes

**Distribución por categoría:**

| Directorio | Agentes |
|------------|---------|
| `agents/core/` | taskmaster, transformer, smith, orquestador-generico, architect, guardian |
| `agents/architecture/` | ~10 agentes (arquitecto-categorico, omega, cartographer, etc.) |
| `agents/qa_ops/` | agentes de QA y operaciones |
| `agents/domain/` | agentes de dominio específico |
| `agents/engineering/` | agentes de ingeniería |

**Proceso por agente** (plan §4.N, agent-spec §12.3):
1. Leer YAML monolítico → clasificar bloques por componente (c, F, U, M, W)
2. Aplicar funtor G₂ → generar workspace: AGENTS.md, SOUL.md, USER.md, TOOLS.md, config.json, skills/CM-*.md
3. Verificación mecánica §12.4 (conteo estados, segregación, completitud)
4. Eliminar YAML monolítico, actualizar catálogo
5. Commit cada 2-3 agentes

### Phase F: Gobernanza y Cierre

1. Deprecar formalmente artefactos KODA con sucesor
2. Resolver artefactos "Evaluar": hub-federation, tooling, test, skills-federation
3. Actualizar gobernanza.md catálogo §3
4. Regenerar catálogo maestro (`kora index`)
5. Verificar métricas finales (0 YAML en applied/, 0 monolitos en agents/, 0 URNs legacy)

---

## 6. Decisiones Pendientes del Operador

Antes de iniciar Phase 3, el operador debe decidir:

1. **Estrategia de triaje**: ¿Hacer inventario/clasificación primero de los 139 KBs (triaje) o migrar directamente namespace por namespace?
2. **Orden de fases**: ¿Phase 3 antes que Phase 4, o invertir (agentes primero)?
3. **Alcance de Phase F**: ¿Los 14 archivos KODA borrados (sin commitear) se consolidan en un commit de limpieza previo, o se postergan hasta Phase F?
4. **Artefactos "Evaluar"**: hub-federation.yml (1666 líneas), test.yml (649), skills-federation.yml (119) — ¿migrar a KORA/MD, absorber en otra spec, o deprecar?

---

## 7. Contexto Técnico Clave

### URN System
- Formato: `urn:{namespace}:{type}:{id}:{version}`
- Catálogo: `catalog/catalog_master_kora.yml`
- CLI: `scripts/kora` (index, resolve, health, validate)

### Modelo de Agente (agent-spec-md v5.0.0)
- F-coalgebra: `c: U → F(U)` con 5 componentes: c (FSM), F (tools), U (estado), M (efectos), W (wiring)
- Workspace canónico: AGENTS.md, SOUL.md, USER.md, TOOLS.md, config.json, skills/CM-*.md
- IDENTITY.md es opcional

### Koraficación (md-spec v2.0.0 §6)
- Funtor F: DocHumano → KORA/MD
- Estilo telegráfico, RAG-optimizado, fidelidad preservada
- Verificación mecánica (cifras, estructura) + adversarial (>15K tokens)

### Agentificación (agent-spec §12)
- Funtor G₂: KODA/Agent.yaml → KORA/Agent workspace
- 5 propiedades: fiel, segregador, promotor, bisimilar, idempotente
- 9 pasos de ejecución, 6 checks mecánicos

---

## 8. Archivos de Referencia

| Archivo | Para qué leerlo |
|---------|-----------------|
| `docs/plans/2026-02-23-koda-kora-remediation-plan.md` | Plan detallado con steps bite-sized para cada fase |
| `docs/plans/2026-02-23-koda-kora-remediation-design.md` | Design doc con análisis categórico y decisiones |
| `knowledge/foundations/core/kora/agent-spec-md.md` | Spec de agentes v5.0.0 (referencia para Phase 4) |
| `knowledge/foundations/core/kora/md-spec.md` | Spec KORA/MD v2.0.0 con §6 koraficación (referencia para Phase 3) |
| `knowledge/foundations/core/kora/gobernanza.md` | Gobernanza del ecosistema |
| `CLAUDE.md` | Guía rápida del repo para Claude Code |

---

## 9. Instrucciones para la Siguiente Sesión

```
Lee docs/plans/2026-02-23-session-handoff.md para contexto completo.

Estado: Fases 0-2 completadas. Hay 17 archivos KODA/KORA legacy borrados
sin commitear (ver §3 del handoff). Fases 3, 4, F pendientes.

Antes de ejecutar: pregúntame cómo quiero abordar las fases pendientes
(triaje vs. directo, orden de fases, qué hacer con los archivos sin commitear).
```
