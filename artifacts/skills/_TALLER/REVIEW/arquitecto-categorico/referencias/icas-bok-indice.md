# ICAS-BoK — Indice operativo del corpus

24 documentos del corpus canonico (`artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/`). Usar este indice para decidir que documento leer segun el problema. Leer solo los documentos pertinentes; nunca todo el corpus de golpe.

## Bloque I — Fundamentos (Parts I, V)

| Doc | Tema | URN | Usar cuando | ICAS Cap |
|-----|------|-----|-------------|----------|
| `00-sintesis` | ADN cognitivo, mapa del corpus | `urn:fxsl:kb:icas-sintesis` | Orientacion general | 1, 80 |
| `01-composicion` | Composicion, asociatividad, identidades | `urn:fxsl:kb:icas-composicion` | Modelar cualquier sistema | 2, 3, 7 |
| `02-preservacion` | Functores, faithfulness, fullness | `urn:fxsl:kb:icas-preservacion` | Traducciones entre sistemas | 5, 13, 34 |
| `03-comparacion` | Transformaciones naturales, equivalencia | `urn:fxsl:kb:icas-comparacion` | Comparar disenos | 3, 7, 26 |
| `04-identidad-es-relacion` | Yoneda, representabilidad | `urn:fxsl:kb:icas-identidad-relacion` | APIs, interfaces, observabilidad | 1, 3, 28 |

## Bloque II — Estructura universal (Parts I, II, X)

| Doc | Tema | URN | Usar cuando | ICAS Cap |
|-----|------|-----|-------------|----------|
| `05-universales` | Limites, colimites, pullback, pushout | `urn:fxsl:kb:icas-universales` | JOINs, merges, requirements | 9, 10, 15, 36 |
| `06-adjunciones` | Adjunciones, Sigma/Delta/Pi, Free/Forget | `urn:fxsl:kb:icas-adjunciones` | Migraciones, abstracciones | 12, 46, 47 |

## Bloque III — Composicion avanzada (Parts II, VI, VII)

| Doc | Tema | Usar cuando | ICAS Cap |
|-----|------|-------------|----------|
| `07-composicion-con-estructura` | Monoidal, string diagrams | Composicion con tensor | 36, 52, 67 |
| `08-enriquecimiento` | V-category, Cost, Bool, [0,1] | Relaciones cuantitativas | 40, 41, 55 |
| `08b-higher-categories` | 2-categorias, (infinity,1)-cat, HoTT | Sistemas con meta-niveles | 77, 78, 80 |
| `09-efectos` | Monadas, Kleisli, coalgebras, bisimulacion | Pipelines con efectos | 4, 5, 6, 17 |
| `10-extension` | Kan extensions, Grothendieck, fibrations | Datos incompletos, data lakes | 34, 46, 48 |

## Bloque IV — Sistemas (Parts IV, VIII, IX)

| Doc | Tema | Usar cuando | ICAS Cap |
|-----|------|-------------|----------|
| `11-interaccion` | Poly, lentes, sistemas dinamicos | APIs bidireccionales, protocolos | 4, 30, 54 |
| `12-topoi` | Topoi, logica interna, sheaves | Feature flags, permisos, consistencia | 42, 48, 50 |
| `12b-safety-alignment` | Safety, alignment, verificacion | Seguridad y alineacion de agentes | 33, 42, 43, 45 |
| `13-escala` | Operads, double categories, SoS | Composicion a escala, jerarquias | 10, 39, 52, 60 |

## Bloque V — Agencia y operaciones (Parts III, IV, XI, XII)

| Doc | Tema | Usar cuando | ICAS Cap |
|-----|------|-------------|----------|
| `14-agencia` | Free monad, cofree comonad, agentes | Disenar agentes, delegacion | 6, 27-33, 69 |
| `14b-protocolos-coreografia` | Session types, coreografia, sagas | Comunicacion multi-agente | 32, 44, 52, 54 |
| `15-tiempo` | Sheaves temporales, event sourcing | Modelar tiempo, consistencia | 4, 18, 19, 49, 50 |
| `16-lifecycle` | Lifecycle recursivo, V-model, DevOps | Ciclos de vida, evoluciones | 21-26 |
| `17-procesos` | Requirements, design, testing, maintenance | Procesos de ingenieria | 8, 9, 12, 13, 16, 17, 20 |
| `18-calidad-riesgo` | Quality attributes, riesgo, metricas | Calidad, riesgo, garantias | 40-45 |
| `19-patrones` | Patrones como construcciones universales | Formalizar patrones | 67-71 |
| `20-infraestructura-autonoma` | IaC, reconciliation, self-healing | Infraestructura, autonomia | 30, 51, 53, 60, 78, 79 |
