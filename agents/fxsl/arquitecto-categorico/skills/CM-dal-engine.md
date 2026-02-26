---
_manifest:
  urn: "urn:fxsl:skill:arquitecto-categorico-dal-engine:2.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Disenar y auditar capas de acceso a datos (DAL) con fundamento categorico. Principio: DAL = realizacion de construcciones universales. Trigger: S-DATA-ACCESS-LAYER.

## Input/Output

- **Input:** Dominio con requisitos de persistencia, API, repositorios desde S-DISPATCHER
- **Output:** Arquitectura DAL categorica con seleccion de storage, API, repository, ORM, pipeline

## Procedimiento

1. **Clasificar capa** — STORAGE | API | REPOSITORY | ORM | PIPELINE
2. **Modelar categoricamente** cada capa segun patron
3. **Proponer combinacion optima** segun dominio
4. **Verificar coherencia** inter-capa
5. **Generar checklists** de auditoria por capa

### Storage (Persistencia)

**Limites → SQL (integridad, JOINs, ACID)**
- Product: JOIN cartesiano
- Pullback: JOIN ON shared_key
- Equalizer: WHERE f=g
- Uso: Ecuaciones de caminos fuertes, integridad referencial

**Colimites → NoSQL (flexibilidad, polimorfismo)**
- Coproduct: UNION ALL
- Pushout: UNION + merge/reconcile
- Coequalizer: GROUP BY / DISTINCT
- Uso: Esquema flexible, agregaciones, polimorfismo

**Mixto → Lens asimetrico**
- SQL(write) ↔ Doc(read) via lens
- expose: SQL → Document view
- update: Document → SQL mutations
- Uso: CQRS, read replicas, materializacion

### API (Interfaz)

| Estilo | Funtor | Estructura |
|--------|--------|------------|
| REST | Domain → ResourceCat | Recursos como objetos, CRUD como morfismos |
| GraphQL | Domain → TypeCat + pullback | Tipos como objetos, fields como morfismos, queries como pullbacks |
| gRPC | Domain → ProtoCat | Services como objetos, RPCs como morfismos |
| Streams | Coalgebra | Flujo continuo, accion como primary key |

Verificacion functorial: F(id)=id, F(g∘f)=F(g)∘F(f) para todo funtor API.

### Repository (Patron)

Estructura coalgebraica: c: X → F(X)

- X = conjunto de entidades gestionadas
- F = observaciones + operaciones (find, save, delete, query)
- Bisimulacion: R₁ ~ R₂ ⟺ ∀ops. observe(R₁(ops)) = observe(R₂(ops))
- Sustituibilidad: repos bisimilares son intercambiables

### ORM (Mapeo Objeto-Relacional)

Adjuncion: ORM ⊣ Reflect: DomainCat ⇆ SchemaCat

- Unit η: domain → ORM(Reflect(domain)) ≈ id (round-trip domain)
- Counit ε: Reflect(ORM(schema)) → schema ≈ id (round-trip schema)
- Drift = violacion de η ≈ id o ε ≈ id
- Deteccion: comparar modelo dominio vs schema generado

### Pipeline / Data Lake

Construccion: colim(Dataset_i, Pipeline_ij)

- Grothendieck: ∫F con I = zonas (Raw/Curated/Consumption/Sandbox)
- F(zona) = schema de la zona
- Morfismos = pipelines de transformacion
- Verificacion: diagrama de pipelines conmuta

### Auditoria DAL

| Dimension | Criterio |
|-----------|----------|
| STORAGE-MODEL-ALIGN | Storage alineado con patron categorico elegido |
| API-FUNCTOR-PRESERVE | Funtor API preserva identidad y composicion |
| REPO-BISIM | Repos bisimilares donde se espera sustituibilidad |
| ORM-ADJ-VALID | Adjuncion ORM⊣Reflect con unit/counit ≈ id |
| PIPELINE-COMMUTE | Diagrama de pipelines conmuta |

## Signature Output

```
## DAL: {nombre}
### Storage
Patron: {Limites(SQL) | Colimites(NoSQL) | Mixto(Lens)}
Justificacion: {criterio categorico}

### API
Estilo: {REST | GraphQL | gRPC | Streams}
Funtor: {Domain → TargetCat}

### Repository
Estructura: c: X → F(X)
Bisimulacion: {verificada | pendiente}

### ORM
Adjuncion: ORM ⊣ Reflect
Drift: {detectado | limpio}

### Pipeline
Construccion: {colim | Grothendieck}
Conmutatividad: {verificada | pendiente}
```
