# Auditoria Guardian: Gaps del Sistema de Specs derivados de Evidencia Operativa

**Fecha:** 2026-03-22
**Auditor:** kora/guardian (encarnado)
**Scope:** 73 sesiones operativas (2026-02-22 → 2026-03-22) vs 7 specs fundacionales
**Estado repo al auditar:** 41 workspaces, 735 artefactos, 0 URNs rotas, 0 workspaces invalidos

---

## 1. Procesos de Auditoria Detectados

6 tipos de proceso auditor operando sin protocolo unificado:

| Proceso | Sesiones | Ejecutor | Criterio |
|---------|----------|----------|----------|
| Auditoria Specs fundacionales | #1-4, #19 | operador | coherencia cruzada n×n |
| Auditoria Agentes (compliance) | #5,7,11,15,35,52-53,58-62,68-73 | forgemaster/operador | agent-spec §9 |
| Auditoria Koraficacion | #17-18,33,36,42,54-55 | curator | md-spec §6.10-§6.11 |
| Auditoria Salud repo | #39,47,48 | custodio | CLI `kora health` |
| Auditoria post-creacion | #8-10,16,57,65-67 | forgemaster | agent-spec §9 + co-induccion |
| Correccion post-auditoria | #3,12-14 | operador/forgemaster | remediacion ad-hoc |

**Hallazgo:** No existe spec que gobierne cuando, como ni con que criterio se ejecutan estos procesos.

---

## 2. Problemas Recurrentes

| # | Problema | Evidencia | Magnitud |
|---|---------|-----------|----------|
| P1 | Namespace mismatches URN-directorio | custodio 2026-03-16 | 84 artefactos |
| P2 | `status:draft` en KNOWLEDGE/ | custodio 2026-03-16 | 107 artefactos |
| P3 | Provenance rota (paths inexistentes) | custodio 2026-03-16 | 26 artefactos |
| P4 | Casing inconsistente (agents vs AGENTS) | cirugia 2026-03-16 | 1467 archivos |
| P5 | Koraficacion baja calidad (CR<1.0, info loss) | re-koraficacion masiva | 167 artefactos |
| P6 | Auditoria manual declara PASS sin validacion mecanica | OPM 2026-03-22 | incidente documentado |
| P7 | Multiples sesiones para un solo audit | steipete(7), goreologo(3) | repeticion costosa |
| P8 | Deprecacion sin protocolo | clawmaster sesion #47 | cascada no gobernada |
| P9 | Wiring KB desincronizado tras nueva KB | curacion batch gn | 5 agentes afectados |
| P10 | Brechas spec-encarnacion | korax v3.1.0 | 11 brechas |

---

## 3. Gaps Identificados

### GAP-01 [ALTA] — No existe spec de PROVENANCE ni NAMESPACE-DIRECTORIO

**Problemas derivados:** P1, P3, P4

- `md-spec §3.1` menciona `source` en frontmatter pero NO especifica correspondencia namespace URN - path directorio, formato valido de provenance, ni enforcement para validar que paths existen.
- `gobernanza §4` define regimenes identidad pero delega layout fisico.
- Ninguna spec define casing canonico de directorios root.

**Evidencia cuantificada:** 84 namespace mismatches + 26 provenance rotas + 1467 archivos afectados por casing.

---

### GAP-02 [CRITICA] — No existe PROTOCOLO DE AUDITORIA

**Problemas derivados:** P6, P7

- `agent-spec §9` y `md-spec §9` tienen tablas validacion pero ninguna spec define:
  - Cuando DEBE ejecutarse una auditoria
  - Quien tiene autoridad para declarar PASS/FAIL
  - Que herramientas DEBEN ejecutarse antes de PASS
  - Criterios de aceptacion cuantificados
  - Clasificacion de severidades (CRITICAL/HIGH/MEDIUM/LOW)
- Evidencia directa: `feedback_curator-audit-discipline` documenta PASS declarado sin ejecutar validador mecanico.

---

### GAP-03 [ALTA] — No existe LIFECYCLE DE STATUS

**Problemas derivados:** P2

- `md-spec §3.1` y `spec-md §3.1` mencionan `status: draft|published|deprecated` como campo.
- Ninguna spec define transiciones validas, restricciones por directorio, ni enforcement.

**Evidencia:** 107 artefactos con `status:draft` en KNOWLEDGE/ corregidos manualmente.

---

### GAP-04 [ALTA] — No existe LIFECYCLE DE AGENTE

**Problemas derivados:** P7, P8, P10

- `agent-spec` define anatomia y validacion pero NO: estados lifecycle (proposed - active - deprecated - retired), cuando re-auditar, como deprecar con cascada, relacion version agente - version spec.
- Deprecacion `ops/clawmaster` (sesion #47) requirio procedimiento ad-hoc.

---

### GAP-05 [MEDIA] — CONTEXTO MULTI-TURNO sin forma canonica

- `agent-spec §4.1` exige `## 4. Contexto Multi-turno` como seccion obligatoria.
- La spec NO define que DEBE contener, forma canonica, ni relacion con CM-CONTEXT-MANAGER.
- Resultado: pseudo-compliance (heading existe, contenido heterogeneo).

---

### GAP-06 [CRITICA] — No existe QUALITY GATE para koraficacion

**Problemas derivados:** P5, P6

- `md-spec §6.10` define verificacion mecanica y `§6.11` define verificacion fidelidad.
- No hay regla DEBE que conecte ejecucion de §6.10/§6.11 con transicion a `status:published`.
- No hay regla que exija toolchain especifico antes de PASS.
- CR<1.5 tiene clausula de justificacion pero no dice DONDE documentarla.

**Evidencia:** 167 re-koraficaciones + PASS declarado sin validacion mecanica (OPM 2026-03-22).

---

### GAP-07 [MEDIA] — No existe validacion WIRING KB-AGENTE

**Problemas derivados:** P9

- `agent-spec §6` define `allowed_kb` en config.json; `§8` define wiring inter-agente.
- Ninguna spec define validacion de que URNs en `allowed_kb` resuelven, ni cascada cuando KB cambia.

**Evidencia:** 5 agentes necesitaron wiring manual tras batch curacion gn.

---

### GAP-08 [MEDIA] — Criterios "razonable/suficiente" sin cuantificar

8 instancias detectadas en 5 specs:

| Spec | Termino | Seccion |
|------|---------|---------|
| gobernanza | "enforcement razonable" | §7 |
| agent-spec | "razonable desde agentes + rutas" | §8 |
| agent-spec | "determinismo es default" | §4.3 |
| runtime-spec | "equivalencia funcional razonable" | §6 |
| runtime-spec | "observabilidad suficiente" | §8.1 |
| swarm-spec | "politica verificable" | §5, §6 |
| md-spec | "naturalidad tecnica minima" | §5.4.2 |
| md-spec | "funcion normativa clara" | §5.4 |

---

### GAP-09 [ALTA] — No existe vinculacion SPEC-TOOLCHAIN

**Problemas derivados:** P6, P7

- Todas las specs tienen tablas validacion con columna `Enforcement` y niveles (schema, lint, runtime, eval, manual).
- Ninguna spec declara que comando CLI implementa cada check, ni que checks carecen de implementacion.

**Verificado:** Busqueda de "toolchain", "kora health", "kora validate", "CLI" en specs: 0 resultados.

---

### GAP-10 [BAJA] — No existe spec de MIGRACION CROSS-NAMESPACE

**Problemas derivados:** P1, P4

- `gobernanza §4` define regimenes identidad; `md-spec §8` menciona versionamiento.
- Ninguna spec define como migrar artefactos entre namespaces, actualizar refs cruzadas, ni toolchain de migracion.

**Evidencia:** gnub-gn: 271 refs migradas manualmente.

---

## 4. Priorizacion

| Prioridad | Gap | Problemas | Impacto |
|-----------|-----|-----------|---------|
| **CRITICA** | GAP-02 | P6, P7 | PASS falsos + sesiones repetidas |
| **CRITICA** | GAP-06 | P5, P6 | 167 re-koraficaciones + PASS sin validar |
| **ALTA** | GAP-01 | P1, P3, P4 | 1577 archivos afectados |
| **ALTA** | GAP-03 | P2 | 107 drafts mal ubicados |
| **ALTA** | GAP-04 | P7, P8, P10 | deprecaciones sin protocolo |
| **ALTA** | GAP-09 | P6, P7 | enforcement declarado no operativo |
| **MEDIA** | GAP-07 | P9 | 5 agentes desincronizados |
| **MEDIA** | GAP-08 | transversal | inconsistencia outcomes |
| **MEDIA** | GAP-05 | compliance | pseudo-compliance |
| **BAJA** | GAP-10 | P1, P4 | infrecuente pero destructivo |

---

## 5. Recomendaciones (criterio conservador Guardian)

Principio: **minimo cambio normativo necesario**.

### R1: Protocolo de Auditoria (cierra GAP-02 + GAP-06)

**Spec afectada:** `gobernanza.md` → v3.3.0 (nueva seccion)

Agregar `## Protocolo de Auditoria` que defina:
- PASS requiere: todos checks `schema`+`lint` automatizados sin fallo + checks `manual` documentados con evidencia
- Toolchain obligatorio antes de PASS: `kora health --strict` + `kora validate --profile strict`
- Para koraficacion: `audit_artifact.py` DEBE ejecutarse antes de transicion a `status:published`
- Severidades: CRITICAL (bloquea PASS), HIGH (bloquea PASS salvo excepcion documentada), MEDIUM (debe documentarse), LOW (informativa)

### R2: Regla Namespace-Directorio (cierra GAP-01 parcial)

**Spec afectada:** `md-spec.md` → v6.2.0

Agregar regla: namespace en URN DEBE coincidir con primer subdirectorio bajo `KNOWLEDGE/` o `AGENTS/`. Enforcement: lint.

### R3: Casing Canonico (cierra GAP-01 parcial)

**Spec afectada:** `gobernanza.md` → v3.3.0

Agregar regla: directorios raiz DEBEN usar MAYUSCULAS (`AGENTS/`, `KNOWLEDGE/`, `OPERATIONS/`). Enforcement: lint.

### R4: Lifecycle Status (cierra GAP-03)

**Spec afectada:** `md-spec.md` → v6.2.0

Agregar subseccion en §3.1:
- Transiciones validas: `draft → published → deprecated`
- `KNOWLEDGE/` solo acepta `status: published|deprecated`
- `OPERATIONS/drafts/` acepta `status: draft`
- Enforcement: schema (validable por toolchain)

### R5: Lifecycle Agente (cierra GAP-04)

**Spec afectada:** `agent-spec-md.md` → v8.5.0

Agregar seccion lifecycle:
- Estados: `active | deprecated | retired`
- Deprecacion DEBE: marcar config.json, actualizar refs en consumidores, ejecutar `kora index`
- Re-auditoria obligatoria tras: major bump de spec gobernante, cambio FSM, cambio tools

### R6: Binding Spec-Toolchain (cierra GAP-09)

**Spec afectada:** `gobernanza.md` → v3.3.0

Agregar tabla mapping:
- `schema` → `kora validate --profile strict`
- `lint` → `kora health --strict` + `kora validate`
- `runtime` → evaluacion deployment
- `eval` → test suite + inputs representativos
- `manual` → documentado en reporte auditoria

### R7: Validacion allowed_kb (cierra GAP-07)

**Spec afectada:** `agent-spec-md.md` → v8.5.0

Agregar a §6: toda URN en `allowed_kb` DEBE resolverse contra catalogo vigente. Enforcement: lint.

### R8: Forma Canonica Contexto Multi-turno (cierra GAP-05)

**Spec afectada:** `agent-spec-md.md` → v8.5.0

Especificar forma minima de §4:
- DEBE declarar skill o mecanismo de deteccion de desvio
- DEBE declarar accion ante desvio (→ S-DISPATCHER o rechazo)
- PUEDE delegar a CM-CONTEXT-MANAGER si existe como skill

### R9: Cuantificacion criterios vagos (cierra GAP-08 parcial)

**Accion:** Evaluar caso por caso. Donde cuantificacion sea posible, agregar rubric. Donde no, mantener `manual` con nota explicita de que el criterio requiere juicio experto.

### R10: Protocolo Migracion (cierra GAP-10)

**Accion:** Evaluar si frecuencia justifica spec o si basta con documentacion operativa en `OPERATIONS/`.

---

## 6. Matriz Trazabilidad Completa

```
P1 (84 mismatches)      → GAP-01 → R2, R3
P2 (107 drafts)          → GAP-03 → R4
P3 (26 provenance)       → GAP-01 → R2
P4 (1467 casing)         → GAP-01 → R3
P5 (167 re-koraficacion) → GAP-06 → R1
P6 (PASS sin validar)    → GAP-02, GAP-06, GAP-09 → R1, R6
P7 (sesiones repetidas)  → GAP-02, GAP-04 → R1, R5
P8 (deprecacion ad-hoc)  → GAP-04 → R5
P9 (wiring desincronizado) → GAP-07 → R7
P10 (brechas encarnacion) → GAP-04 → R5
```
