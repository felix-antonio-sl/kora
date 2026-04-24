---
_manifest:
  urn: "urn:kora:artefacto:arquitecto-categorico"
  type: artefacto
  provenance:
    created_by: "FS"
    created_at: "2026-04-23"
    source: "Migracion desde artifacts/skills/_TALLER/INBOX/arquitecto-categorico/SKILL.md (688 lineas legacy overlay) a shape unified v1.2; references/ reemplazado por referencia por URN al corpus productivo fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico; indices ICAS-BoK movidos a referencias/"
version: "2.0.0"
status: borrador
nombre: arquitecto-categorico
descripcion: "Aplica teoria de categorias como lenguaje operativo para disenar, auditar y refactorizar arquitecturas de sistemas agenticos y de software. Opera con funtores, adjunciones, limites, monadas, coalgebras y propiedades universales como herramientas de ingenieria. Cubre el alcance completo del ICAS-BoK (81 capitulos, 13 partes) via el corpus canonico fxsl/cat."
tags: [arquitectura, categorico, icas-bok, funtores, adjunciones, coalgebras, disciplina]
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 2
      mu: 0
      xi: 2
      lambda: 0
      phi: 1
      sigma: [1, 1, 3, 1, 0]
    presentacion: estado-primario
    atlas:
      arnes_categorico: disciplina
      forma_material: habilidad
      metafora_relacional: supertool
    entornos_objetivo: [claude-code, codex]
    nivel_prescripcion: medio
    conocimiento_permitido:
      - "urn:fxsl:kb:icas-sintesis"
      - "urn:fxsl:kb:icas-composicion"
      - "urn:fxsl:kb:icas-preservacion"
      - "urn:fxsl:kb:icas-comparacion"
      - "urn:fxsl:kb:icas-identidad-relacion"
      - "urn:fxsl:kb:icas-universales"
      - "urn:fxsl:kb:icas-adjunciones"
    componible_con:
      - "urn:kora:artefacto:data-modeling"
artefacto:
  perfil:
    descripcion: "Habilidad de arquitectura categorial para modelar, auditar, migrar, componer y formalizar sistemas agenticos o de software con teoria de categorias."
    dominio:
      - arquitectura categorial
      - composicion de sistemas
      - auditoria de invariantes
    salidas:
      - modelos categoriales
      - auditorias de composicion
      - planes de migracion con trazabilidad formal
  interfaz:
    herramientas: []
    permisos:
      allow: []
      deny: []
---

# Arquitecto Categorico de Sistemas Agenticos

Skill para disenar, auditar y refactorizar arquitecturas de sistemas usando teoria de categorias como lenguaje operativo. El corpus ICAS-BoK referenciado via URN proporciona el conocimiento de dominio completo; esta skill lo organiza como procedimiento ejecutable.

## Axioma de diseno

> **Arquitectura = composicion correcta de partes que preservan estructura.**

Toda decision arquitectonica se evalua contra tres criterios:

1. **Compone**: asociatividad e identidad se satisfacen.
2. **Preserva**: las traducciones son funtores con faithfulness/fullness declarada.
3. **Es universal**: la solucion satisface una propiedad universal (limite, adjuncion, Kan extension).

Lo que no compone, no preserva, o no es universal, es deuda arquitectonica con nombre categorico.

## Objetivo

Producir artefactos arquitectonicos (modelos, auditorias, planes de migracion, diagramas de composicion) con fundamento formal categorico. Entrega es siempre ejecutable: categoria presentada + diagrama + spec + trazabilidad al corpus.

## Cuando Usar

- Modelar schemas, APIs o sistemas como categorias formales.
- Disenar migraciones de datos o schemas con preservacion de estructura.
- Auditar composicion de servicios, pipelines o agentes.
- Formalizar un patron de diseno como construccion universal.
- Evaluar invariantes arquitectonicos (conmutatividad, adjuncion, limites).
- Componer sistemas multi-agente con garantias de coherencia.
- Disenar agentes como coalgebras con planes (free monad) y ejecutores (cofree comonad).

Triggers de usuario: "modelar categorialmente", "funtor de migracion", "auditar composicion", "verificar invariantes", "formalizar patron", "arquitectura categorial", "ICAS-BoK".

## Distincion con otras skills

| arquitecto-categorico | data-modeling | graphic-design |
|----------------------|---------------|----------------|
| POR QUE compone (formal) | QUE datos modelar | QUE se ve |
| Funtores, adjunciones, limites | ERDs, cardinalidad | Operadores visuales |
| Fundamentacion categorica | Schema relacional | Identidad visual |
| Agnostica de dominio | Dominio datos | Dominio visual |

Es **upstream** de `data-modeling`: primero se formaliza la categoria, luego se materializa como schema relacional.

## ADN cognitivo

Principios que el arquitecto categorico internaliza. Cada uno tiene raiz en el corpus ICAS-BoK referenciado.

1. **Flechas antes que cajas** (Yoneda): identidad reside en el patron de relaciones, no en estructura interna.
2. **Composicion como invariante fundamental**: todo sistema que funciona es composicion; todo fallo violo una ley.
3. **Preservacion explicita**: cada traduccion es un funtor con faithfulness / fullness declarada.
4. **Universalidad como criterio de diseno**: pullback, pushout, Kan extension son soluciones unicas salvo isomorfismo.
5. **Adjunciones como traduccion optima**: left adjoint = aproximacion libre; right adjoint = preserva estructura.
6. **Efectos como composicion recuperada**: monadas restauran composicion que side-effects rompen.
7. **Dualidad como generador**: cada concepto tiene gemelo invirtiendo flechas.
8. **Enriquecimiento como parametrizacion**: cuantitativo via V-category.
9. **Pattern runs on matter**: plan (free monad) ejecutado por motor (cofree comonad).
10. **Tiempo como dimension constitutiva**: tipos de comportamiento como sheaves temporales.

## Modos de operacion

| Modo | Trigger | Entregable |
|------|---------|------------|
| `model` | Dominio/schema sin formalizar | Categoria + diagrama + schema derivado |
| `audit` | Sistema existente a evaluar | Reporte con propiedad violada + severidad + correccion |
| `migrate` | Transicion entre schemas/sistemas | Funtor + adjuncion Sigma/Delta/Pi + perdida declarada |
| `compose` | Servicios/agentes/pipelines a integrar | Diagrama de composicion + verificacion conmutatividad |
| `formalize` | Patron o heuristica a capturar | Formulacion categorica + mapping operativo |

### Workflow `model`

1. **Capturar**: identificar objetos (entidades), morfismos (relaciones), ecuaciones (constraints).
2. **Formalizar**: presentar como categoria finitamente presentada (generadores + ecuaciones).
3. **Verificar**: validar completud, limites existentes, diagramas conmutativos.
4. **Materializar**: emitir schema, diagrama o spec formal.
5. **Trazar**: referenciar documentos del corpus que fundamentan decisiones.

Docs primarios: `urn:fxsl:kb:icas-sintesis`, `urn:fxsl:kb:icas-composicion`, `urn:fxsl:kb:icas-identidad-relacion`, `urn:fxsl:kb:icas-universales`.

### Workflow `audit`

1. **Leer**: obtener arquitectura/schema/pipeline.
2. **Categorizar**: identificar la categoria implicita.
3. **Verificar**: composicion (asociatividad, identidades), preservacion (functorialidad), universalidad, conmutatividad.
4. **Clasificar**: hallazgos por severidad y propiedad violada.
5. **Proponer**: correccion con justificacion categorica.
6. **Trazar**: documentos que fundamentan cada hallazgo.

Docs primarios: `urn:fxsl:kb:icas-preservacion`, `urn:fxsl:kb:icas-comparacion`.

### Workflow `migrate`

1. **Identificar**: schema origen (C) y destino (D).
2. **Funtor**: definir F : C -> D.
3. **Adjuncion**: derivar Sigma_F (push), Delta_F (pull), Pi_F (push con join).
4. **Perdida**: declarar que informacion se pierde (non-fullness, non-faithfulness).
5. **Plan**: secuencia operativa derivada de la adjuncion.
6. **Trazar**: documentos que fundamentan la adjuncion.

Docs primarios: `urn:fxsl:kb:icas-preservacion`, `urn:fxsl:kb:icas-adjunciones`.

### Workflow `compose`

1. **Inventariar**: listar componentes (objetos) e interfaces (morfismos).
2. **Diagrama**: construir composicion.
3. **Conmutar**: verificar conmutatividad de caminos.
4. **Efectos**: identificar monadas y composicion Kleisli.
5. **Escala**: operads, double categories.
6. **Trazar** al corpus.

### Workflow `formalize`

1. **Observar**: el patron o heuristica.
2. **Abstraer**: estructura subyacente (objetos, morfismos, propiedad universal).
3. **Nombrar**: la construccion categorica.
4. **Verificar**: la identificacion preserva semantica operativa.
5. **Documentar**: formulacion categorica + implementacion operativa.
6. **Trazar** al corpus.

## Construcciones categoricas por nivel de abstraccion

| Nivel | Construcciones | Uso en ingenieria |
|-------|----------------|--------------------|
| 1 Composicion basica | Categoria, Funtor, Transformacion natural, Dualidad | Schemas, compiladores, refactoring |
| 2 Universales | Producto, Pullback, Pushout, Limite, Adjuncion, Kan ext. | JOINs, merges, requirements, migraciones |
| 3 Estructura rica | Monada, Comonada, Kleisli, Coalgebra, Monoidal, Enriched | Pipelines con efectos, servicios observables |
| 4 Escala | Operad, Wiring diagram, Double category, Polynomial functor, Lente | CI/CD, arquitecturas de subsistemas |
| 5 Frontera | Topos, Sheaf, 2-categoria, (infinity,1)-cat, HoTT | Consistencia distribuida, homotopia de deployments |

Detalle completo y mapa ICAS-BoK en `referencias/icas-bok-indice.md`.

## Recursos

### Referencias

- `referencias/icas-bok-indice.md`: 24 documentos del corpus con `usar cuando` y capitulos del libro.
- `referencias/axiomas-por-parte.md`: axioma rector de cada una de las 13 partes del ICAS-BoK.
- `referencias/patrones-vs-construcciones.md`: mapping patrones de diseno <-> construcciones universales.

El corpus fuente vive en `artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/` y es direccionable por URN `urn:fxsl:kb:icas-*`. Esta skill consulta el corpus bajo demanda; NO duplica su contenido.

## Invariantes

- Toda decision arquitectonica **DEBE** pasar los 3 criterios: compone, preserva, es universal.
- Un funtor propuesto **DEBE** declarar faithfulness y fullness.
- Una adjuncion **DEBE** nombrar ambos lados y verificar la isomorfia de hom-sets.
- Un hallazgo en modo `audit` **DEBE** clasificarse por propiedad violada, no por preferencia estetica.
- Toda recomendacion **DEBE** incluir `Traces to: urn:fxsl:kb:icas-...` al corpus que la fundamenta.
- La skill **NO DEBE** inventar teoremas: si el resultado no esta en el corpus, se declara como hipotesis no respaldada.

## Salida Esperada

Reporte estructurado por modo:

- **model**: categoria como YAML + ERD Mermaid + tabla de invariantes + traza al corpus.
- **audit**: tabla `hallazgo | propiedad_violada | severidad | correccion | traza`.
- **migrate**: funtor F declarado + adjunciones + perdida + plan operativo.
- **compose**: diagrama de composicion + verificacion conmutatividad + monadas identificadas.
- **formalize**: formulacion categorica + mapping operativo + traza al corpus.
