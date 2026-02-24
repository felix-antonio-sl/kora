---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:arquitecto-categorico-cm-audit-engine:2.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Auditoria DIK rigurosa de artefactos de datos. Principio: Artefacto bien formado = objeto en categoria verificable. Trigger: S-AUDIT.

## Input/Output

- **Input:** Artefacto a auditar (schema, modelo, API, KB) + clasificacion DIK desde S-AUDIT
- **Output:** Informe con nivel DIK, diagnostico por modo, issues con severidad, mejoras con patron

## Procedimiento

1. **Clasificar DIK** — DATA (instancia I:S→Set), INFORMATION (schema S), KNOWLEDGE (Cat/adjunciones/comportamiento)
2. **Seleccionar modo** segun tipo de artefacto
3. **Ejecutar auditoria** por dimensiones del modo
4. **Clasificar issues** por severidad
5. **Proponer mejoras** con patron de correccion
6. **Generar informe** ordenado por severidad

### Modos de Auditoria

**STATIC** — Schemas, modelos de datos, DDL

| Dimension | Verifica | Severidad si falla |
|-----------|----------|-------------------|
| STRUCTURAL | Identity morfismos, composicion, asociatividad, path equations | CRITICAL |
| REFERENTIAL | Refs internas (IDs existentes), externas (XRef resuelven), FKs | HIGH |
| COMPLETENESS | Instance definida para todos los objetos del schema | MEDIUM |
| QUALITY | Construcciones universales, functorialidad | LOW |

**TEMPORAL** — Migraciones, versionado

| Dimension | Verifica | Severidad si falla |
|-----------|----------|-------------------|
| MIGRATION | Validez del funtor (preserva id/composicion), cuadrados conmutan | HIGH |
| VERSION_CHAIN | Cadena de versiones consistente, composable | MEDIUM |
| CONSTRAINT_PRESERVATION | Restricciones preservadas a traves de migraciones | HIGH |
| TECH_DEBT | Migraciones ad-hoc sin formalizacion | LOW |

**BEHAVIORAL** — APIs, servicios, componentes

| Dimension | Verifica | Severidad si falla |
|-----------|----------|-------------------|
| INTERFACE_CONFORMANCE | API conforme a schema declarado | HIGH |
| BISIMULATION | Componentes sustituibles producen outputs indistinguibles | MEDIUM |
| ACTION_INDEX | Acciones indexadas, trazables, reproducibles | LOW |
| COALG_VALIDITY | Estructura coalgebraica bien formada (c: U → F(U)) | MEDIUM |

**KB_GLOBAL** — Bases de conocimiento completas

| Dimension | Verifica | Severidad si falla |
|-----------|----------|-------------------|
| NO_DANGLING | Toda referencia apunta a artefacto existente | HIGH |
| NO_BAD_CYCLES | Sin ciclos en refinamiento | MEDIUM |
| REQUIRES_ACYCLIC | Grafo requires es DAG | CRITICAL |
| CATALOG_COMPLETE | Todo artefacto registrado en catalogo | MEDIUM |
| URN_UNIQUE | URNs unicas, sin colisiones | CRITICAL |

**DAL_INTEGRATED** — Capas de acceso a datos

| Dimension | Verifica | Severidad si falla |
|-----------|----------|-------------------|
| STORAGE-MODEL-ALIGN | Storage alineado con modelo categorico (lim/colim) | HIGH |
| API-FUNCTOR-PRESERVE | API preserva F(id)=id, F(g∘f)=F(g)∘F(f) | HIGH |
| REPO-BISIM | Repos bisimilares: ∀ops. obs(R₁)=obs(R₂) | MEDIUM |
| ORM-ADJ-VALID | ORM⊣Reflect: η≈id, ε≈id, drift=violacion | MEDIUM |
| PIPELINE-COMMUTE | Diagrama pipeline conmuta | HIGH |

### Severidad

| Nivel | Significado | Accion |
|-------|-------------|--------|
| CRITICAL | Artefacto invalido, no usable | Corregir inmediatamente |
| HIGH | Integridad comprometida | Corregir antes de produccion |
| MEDIUM | Suboptimo, funciona pero mejorable | Planificar correccion |
| LOW | Mejora incremental | Backlog |

### Patrones de Mejora

| Patron | Diagnostico | Correccion |
|--------|-------------|------------|
| BROKEN-DIAGRAM | Paths paralelos no conmutan | Agregar path equation o corregir morfismos |
| ORPHAN-OBJECT | Objeto sin morfismos entrantes/salientes | Conectar o eliminar |
| DANGLING-REF | Referencia a entidad inexistente | Corregir referencia o crear target |
| MISSING-PROC | Proceso operativo ausente | Agregar procedimiento formal |
| VERSION-MISMATCH | Versiones desalineadas | Alinear cadena de versiones |
| AD-HOC-CONSTRUCTION | Construccion sin propiedad universal | Reemplazar con construccion universal |
| NON-FUNCTORIAL | Migracion no preserva estructura | Redefinir como funtor valido |
| REDUNDANT-BISIMILAR | Componentes bisimilares redundantes | Identificar y unificar |

## Signature Output

```
## Auditoria: {nombre artefacto}
Nivel DIK: {DATA | INFORMATION | KNOWLEDGE}
Modo: {STATIC | TEMPORAL | BEHAVIORAL | KB_GLOBAL | DAL_INTEGRATED}

### Issues
| # | Dimension | Severidad | Descripcion | Patron |
|---|-----------|-----------|-------------|--------|
| 1 | {dim} | {sev} | {descripcion} | {patron} |

### Metricas
- Objetos: {n} | Morfismos: {m} | Path Equations: {p}
- Issues: CRITICAL={c} HIGH={h} MEDIUM={m} LOW={l}

### Mejoras Propuestas
1. {patron}: {accion concreta}
```
