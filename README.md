# KORA

Monorepo de especificaciones formales para construir y gobernar agentes LLM usando fundamentos de teoria de categorias.

Fusiona 6 repositorios (koda, fxsl, gorenuble, tde, orko, korvo) en una estructura organizada por namespaces. Idioma principal: **es-CL**.

## Numeros

| Metrica | Valor |
|---------|-------|
| Artifacts totales (catalogo) | 470 |
| Knowledge bases | 212 |
| Agentes (workspaces) | 41 |
| Skills (endofuntores lazy-load) | 94 |
| Specs fundacionales | 4 |
| Namespaces activos | 9 |
| Broken URNs | 0 |

## Arquitectura

```
kora/
  specs/           Especificaciones fundacionales (gobernanza, formatos, agentes)
  knowledge/       KBs organizados por namespace (gn, fxsl, tde, legal, ...)
  agents/          41 agentes como workspaces KORA
  catalog/         Registro maestro de URNs
  skills/          Federacion de skills
  scripts/         CLI (kora index/resolve/health/validate/stats)
```

### Jerarquia de Gobernanza

```
gobernanza.md          meta-reglas del ecosistema
  md-spec.md           formato KORA/MD (descriptivo)
  spec-md.md           formato KORA/Spec-MD (prescriptivo)
    agent-spec-md.md   arquitectura de agentes v5.0.0
```

### Modelo de Agente

Un agente LLM es una **F-coalgebra** `c: U -> F(U)` con 5 componentes esenciales:

| # | Componente | Simbolo | Archivo |
|---|-----------|---------|---------|
| 1 | Morfismo de transicion | c | `AGENTS.md` — FSM pura, sin prosa |
| 2 | Funtor de interfaz | F | `TOOLS.md` — firmas de herramientas |
| 3 | Espacio de estados | U | `SOUL.md` + `USER.md` — fibras ortogonales |
| 4 | Monada de efectos | M | `config.json` — sandbox inmutable |
| 5 | Diagrama de wiring | W | Declarado en `AGENTS.md` |

Procesos cognitivos densos se extraen a `skills/CM-*.md` como endofuntores bajo evaluacion diferida (lazy load).

```
agents/{namespace}/{nombre}/
  AGENTS.md        c: FSM estados + transiciones + co-induccion
  SOUL.md          U: identidad, paradigma, tono, ejemplos
  USER.md          U: perfil operador, rutinas, preferencias
  TOOLS.md         F: firmas, routing KB, cuando usar/no usar
  config.json      M: allowed_kb, sandbox, tools, sub_agents
  skills/
    CM-*.md        Endofuntores cognitivos (lazy load)
```

### Principio de Segregacion

La logica de transicion (c) **nunca** se mezcla con la fenomenologia (SOUL.md), el contexto del operador (USER.md), ni las politicas de seguridad (config.json). Dos agentes son sustituibles sii son **bisimilares**: producen outputs indistinguibles para todo input del dominio.

### Sistema URN

```
urn:{namespace}:kb:{id}          Knowledge base
urn:{namespace}:agent-bootstrap:{nombre}-{tipo}:{version}   Archivo de agente
```

Namespaces: **kora**, **fxsl**, **gn**, **tde**, **orko**, **korvo**, **gov**, **legal**, **mgmt**

El catalogo (`catalog/catalog_master_kora.yml`) es la fuente de verdad. `kora health` verifica integridad referencial.

## Comandos

```bash
scripts/kora index      # Reconstruir catalogo desde todos los artifacts
scripts/kora resolve    # Resolver URN a path fisico
scripts/kora health     # Verificar referencias URN rotas
scripts/kora validate   # Validar workspaces (requiere jsonschema)
scripts/kora stats      # Estadisticas del monorepo
```

Requisitos: Python 3 + PyYAML. No hay build system — es un monorepo de especificaciones y documentacion.

## Namespaces

| Namespace | Dominio | Artifacts |
|-----------|---------|-----------|
| **fxsl** | Teoria de categorias, gist, MBT, agentes personales | 136 |
| **gn** | Gobierno Regional de Nuble (GORE) | 134 |
| **kora** | Framework, specs, manual OpenClaw | 115 |
| **tde** | Transformacion digital del Estado | 33 |
| **legal** | Normativa legal chilena | 21 |
| **orko** | Metodologia de complejidad organizacional | 12 |
| **gov** | Gobierno central, plataformas | 9 |
| **korvo** | Asistente personal | 6 |
| **mgmt** | Management, estructura del Estado | 4 |

## Agentes por Namespace

| Namespace | Agentes | Ejemplos |
|-----------|---------|----------|
| **fxsl** | 15 | arquitecto-categorico, ontologista-gist, ingeniero-software-composicional |
| **gn** | 12 | goreologo, ingeniero-goreos, gestor-ipr-360, erp-gore |
| **kora** | 7 | guardian, architect, transformer, cartographer |
| **ops** | 3 | tester, sim-orchestrator, ci-assistant |
| **korvo** | 2 | korvo-assistant, korax |
| **tde** | 1 | digitrans |
| **orko** | 1 | arquitecto-orko |

## Conceptos Clave

- **Koraficacion** (md-spec S6): Transformar documentos humanos a KORA/MD — formato telegrafico optimizado para RAG
- **Agentificacion** (agent-spec S12): Funtor G que transforma YAML monoliticos KODA en workspaces KORA con segregacion categorica
- **Bisimulacion**: Criterio de equivalencia entre agentes — comportamiento observable indistinguible
- **Co-induccion**: Mecanismo de auto-correccion en nodos terminales de la FSM
- **Endofuntor cognitivo**: Proceso denso aislado en `skills/`, convocado bajo evaluacion diferida

## Estado de Migracion

- [x] **Phase 0** — Genesis: reestructuracion por namespaces
- [x] **Phase 1** — Source Mapping: 208 artifacts mapeados
- [x] **Phase 2** — Koraficacion: 175+ KBs YAML a KORA/MD
- [x] **Phase 4** — Agentificacion: 40 YAML monolitos a 41 workspaces KORA
- [ ] **Phase F** — Governance: deprecacion formal KODA, archivado repos fuente

## Fuentes Teoricas

- Barbosa, L. *Coalgebra for the Working Software Engineer* — modelo coalgebraico
- Spivak, D. *Categorical Systems Theory* — lenses, wiring diagrams, sistemas monadicos
- Fong & Spivak. *Seven Sketches in Compositionality* — fundamentos categoricos
- Schultz, Spivak, Vasilakopoulou. *Algebraic Databases* — profuntores, bimodulos
- Spivak. *Functorial Data Migration* — adjunciones Delta/Sigma/Pi

## Licencia

CC-BY-4.0
