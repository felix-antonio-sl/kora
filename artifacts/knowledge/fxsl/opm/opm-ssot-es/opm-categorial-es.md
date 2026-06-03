---
_manifest:
  urn: urn:fxsl:kb:opm-categorial-es
  provenance:
    created_by: deep-opm-pro/Claude + custodio KORA
    created_at: '2026-06-03'
    source: /home/felix/projects/deep-opm-pro/docs/capa-categorial.md
version: 1.1.0
status: publicado
source_base: opm-iso-19450-es.md v3.0.0; reglas-opm-estrictas-es.md v1.1.0; metodologia-forja-es.md
  v1.4.0; spec-forja-opl-es.md v1.1.0; corpus ICAS-BoK v1.0.0; capa categorial verificada
  por leyes en deep-opm-pro (app/src/leyes/), incluido el eje vertical (F-V1 adjunción,
  F-V2 fibración) en app/src/leyes/refinamiento-adjuncion.test.ts.
derived_from:
- urn:fxsl:kb:opm-es
- urn:fxsl:kb:opd-es
- urn:fxsl:kb:opl-es
- urn:fxsl:kb:metodologia-forja-opm-es
- urn:fxsl:kb:reglas-opm-estrictas-es
- urn:fxsl:kb:icas-sintesis
- urn:fxsl:kb:icas-efectos
- urn:fxsl:kb:icas-universales
- urn:fxsl:kb:icas-higher-categories
- urn:fxsl:kb:icas-adjunciones
- urn:fxsl:kb:icas-extension
scope: 'Puente OPM <-> teoría de categorías (ICAS-BoK): mapa de las primitivas y
  mecanismos de OPM a las construcciones categoriales canónicas que los modelan. Es
  la "nota al margen formal" (metodologia-forja §0.2-0.3) canonizada en un artefacto
  separado — NUNCA se expone al modelador. No redefine OPM ni reemplaza ninguna capa;
  ilumina el eje horizontal (composición, equivalencia, razonamiento) y la dualidad
  simulación/razonamiento, ya operacionalizados y verificados por leyes en deep-opm-pro.

  '
tags:
- opm
- categorial
- icas-bok
- puente
- opforja
- eje-horizontal
- eje-vertical
lang: es
---

# OPM <-> teoría de categorías — puente formal (ICAS-BoK)

## 0. Qué es y qué no es este artefacto

Este documento es un **puente** entre dos corpus de la SSOT: la familia OPM (`urn:fxsl:kb:opm-es` y derivadas) y el corpus categorial ICAS-BoK (`urn:fxsl:kb:icas-sintesis` y familia). Lee OPM con **teoría de categorías como piedra de Rosetta** y mapea cada primitiva/mecanismo OPM a la construcción categorial canónica que lo modela.

**Línea roja (rectora).** La lente categorial es **nota al margen formal, nunca principio para el modelador** (`metodologia-forja-es.md §0.2-0.3`). Este artefacto es justamente *esa* nota al margen, aislada en su propio lugar para que el canon-para-humanos (`opm-es`/`opd-es`/`opl-es`) permanezca **limpio de jerga categorial**. Nada aquí redefine OPM ni añade primitiva: OPM ya es categorialmente bien fundado; este puente solo **nombra con precisión** lo que OPM implica estructuralmente. La superficie del modelador (UI, OPD, OPL) **jamás** muestra este vocabulario.

## 1. Mapa OPM <-> teoría de categorías

| Primitiva / mecanismo OPM | Construcción categorial | URN ICAS-BoK |
|---|---|---|
| Objetos, procesos, enlaces | objetos y morfismos de una categoría | `urn:fxsl:kb:icas-composicion` |
| Hecho OPM (denotación atómica del modelo) | elemento del haz de hechos (presheaf) | `urn:fxsl:kb:icas-topoi` |
| Pegado de OPDs (consistencia entre vistas del mismo modelo) | sheaf / gluing sobre el cubrimiento de OPDs | `urn:fxsl:kb:icas-topoi` |
| Refinamiento (in-zoom) <-> abstracción (out-zoom) | adjunción in-zoom ⊣ out-zoom (unit/counit) + fibración de Grothendieck (lift cartesiano de frontera) | `urn:fxsl:kb:icas-adjunciones`, `urn:fxsl:kb:icas-extension` |
| Composición de modelos por interfaz compartida | pushout / structured cospan | `urn:fxsl:kb:icas-universales` |
| Equivalencia de realizaciones (mismo efecto, interior distinto) | 2-célula / equivalencia por firma de frontera | `urn:fxsl:kb:icas-higher-categories`, `urn:fxsl:kb:icas-comparacion` |
| Simulación (desplegar el comportamiento) | anamorfismo (unfold de una coalgebra) | `urn:fxsl:kb:icas-efectos` |
| Razonamiento (derivar lo implícito) | catamorfismo (fold) — dual de la simulación | `urn:fxsl:kb:icas-efectos` |
| Recurso lineal (se consume, no se clona) | categoría monoidal no-cartesiana | `urn:fxsl:kb:icas-composicion-estructura` |
| Preservación de estructura al migrar/proyectar | funtor (faithful / full) | `urn:fxsl:kb:icas-preservacion` |

## 2. El eje horizontal: dónde la lectura categorial aporta

OPM tiene el **eje vertical** (refinamiento <-> abstracción) muy desarrollado en sus capas. La frontera estaba en el **eje horizontal**: **composición**, **equivalencia** y **razonamiento** entre modelos y realizaciones, más la **linealidad** como dimensión designable. La lectura categorial da a ese eje horizontal una semántica precisa y verificable, sin tocar la superficie OPM:

- **Composición** = pushout por interfaz compartida (`icas-universales`): dos modelos se unen identificando entidades comunes, sin duplicar ni dejar referencias colgantes.
- **Equivalencia** = igualdad de firma de frontera (`icas-higher-categories`): dos realizaciones son funcionalmente intercambiables si presentan el mismo efecto observable sobre su contorno, aunque su interior difiera.
- **Linealidad** = monoidalidad no-cartesiana (`icas-composicion-estructura`): un recurso que se consume no se duplica; dos consumidores del mismo recurso lineal son un conflicto.

El **eje vertical**, siempre maduro como *mecanismo*, carecía de un invariante que lo protegiera; ahora también tiene lectura categorial verificada:

- **Adjunción in-zoom ⊣ out-zoom** (`icas-adjunciones`): refinar y luego abstraer preserva exactamente la **frontera** del proceso (la *unit* η es iso sobre la frontera, "módulo detalle añadido"); in-zoom es idempotente. Es la garantía de coherencia del eje más usado de OPM.
- **Fibración de Grothendieck** (`icas-extension`): el árbol de OPDs fibra sobre la jerarquía de refinamiento; cada enlace derivado del hijo es el **lift cartesiano** de un enlace de frontera del padre (existencia + unicidad + cambio de base coherente). "Traer" un enlace entre niveles = cambio de base funtorial.
- **Puente con la bisimulación:** la frontera que la bisimulación de un in-zoom ejerce es la que la adjunción preserva — lo que convierte la coherencia de frontera de hipótesis en teorema verificable.

## 3. La dualidad central: simulación y razonamiento

La pieza unificadora (`urn:fxsl:kb:icas-efectos`): **simulación (anamorfismo / unfold) y razonamiento (catamorfismo / fold) son duales sobre el mismo sustrato** — el haz de hechos del modelo. La simulación despliega el comportamiento paso a paso; el razonamiento colapsa la estructura a inferencias. Recorren **el mismo grafo de transición de estados**, en sentidos opuestos: lo que la simulación abre, el razonamiento puede cerrar. La consulta de alcanzabilidad de estados es el dual estático del recorrido dinámico.

## 4. Dónde se encarna (capas opforja + implementación)

Este puente es conocimiento; las **reglas normativas** correspondientes viven en las capas prescriptivas de opforja, y la **verdad ejecutable** en las leyes del modelador:

- `urn:fxsl:kb:reglas-opm-estrictas-es §Anexo C` — reglas `R-CAT-LIN` (linealidad), `R-CAT-EQ` (equivalencia por frontera), `R-CAT-COMP` (composición).
- `urn:fxsl:kb:metodologia-forja-opm-es §A0.4` — equivalencia funcional de realizaciones como cierre del método A0; criterio in-zoom <-> out-zoom.
- `urn:fxsl:kb:spec-forja-opl-es §24` — composición por interfaz en OPL (unión deduplicada de párrafos).
- Implementación verificada en `deep-opm-pro`: `app/src/modelo/{hechos,composicion,equivalencia,razonamiento,simulacion}/` y leyes falsificables en `app/src/leyes/` (`law-composicion-*`, `law-derivacion-no-contradice`, integración S⊑F0 / dualidad S->F3 / F1<->S / F2<->S). El **eje vertical** se verifica en `app/src/modelo/equivalencia/verticalidad.ts` (`firmaFronteraEntidad`, `verificarLiftCartesianoFrontera`) y `app/src/leyes/refinamiento-adjuncion.test.ts` (F-V1 adjunción, F-V2 fibración, puente F-V1<->F-D2), cada ley con control de no-tautología. Síntesis viva: `docs/capa-categorial.md` del repo.

## 5. Regla de uso

- Para **modelar** (humano): usar OPM/OPD/OPL en lenguaje de dominio; este artefacto NO se cita al modelador.
- Para **diseñar o auditar** la capa formal de opforja (agente/arquitecto): este puente da el vocabulario y la trazabilidad a ICAS-BoK; cada afirmación categorial DEBE poder anclarse a una URN ICAS específica y, donde se vuelve regla, a su capa propietaria opforja y a una ley ejecutable.
- Cambios a este puente o a las capas que referencia = **propuestas** vía `custodio-kora` + operador; nunca contaminar las capas ISO (`opm-es`/`opd-es`/`opl-es`).
