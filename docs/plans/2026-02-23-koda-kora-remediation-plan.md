# Remediación Deuda Técnica KODA/KORA — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Eliminar la deuda técnica KODA/KORA: re-fundamentar agent-spec-md categóricamente, diseñar funtor G, limpiar tools, koraficiar 139 KBs, agentificar 40 agentes.

**Architecture:** Fundación por Capas — 5 fases secuenciales donde cada una entrega valor independientemente. La fundamentación categórica (F-coalgebra, 5 componentes esenciales) precede toda instanciación. Design doc: `docs/plans/2026-02-23-koda-kora-remediation-design.md`.

**Tech Stack:** Markdown (KORA/MD, KORA/Spec-MD), YAML (legacy KODA), JSON (config schemas), shell scripts (verificación), `kora` CLI.

---

## Fase 0: Limpiar tools/

### Task 0.1: Auditar dependencias de tools/

**Files:**
- Read: `tools/*.yml` (21 archivos)
- Read: `agents/**/*.yaml` (buscar refs a tools/)
- Read: `catalog/catalog_master_kora.yml`

**Step 1: Generar inventario de tools/ con líneas y referencias**

```bash
# Para cada archivo en tools/, contar líneas y buscar refs en agentes
for f in tools/*.yml tools/*.yaml; do
  name=$(basename "$f" .yml)
  name=$(basename "$name" .yaml)
  lines=$(wc -l < "$f")
  refs=$(grep -rl "$name" agents/ 2>/dev/null | wc -l)
  echo "$name | $lines lines | $refs agent refs"
done
```

**Step 2: Clasificar cada archivo**

Para cada archivo, asignar una de:
- `DELETE` — obsoleto, 0 refs, contenido desactualizado
- `DEPRECATE` — tiene refs pero contenido dudoso
- `KEEP` — vigente y referenciado
- `MIGRATE` — vigente, debe migrar a KORA/MD en Fase 3

Documentar la clasificación en un comentario del commit.

**Step 3: Verificar que ningún agente core depende de archivos a eliminar**

```bash
# Verificar refs de archivos marcados DELETE
grep -rl "NOMBRE_ARCHIVO" agents/core/ agents/architecture/
```

Expected: 0 resultados para archivos marcados DELETE.

---

### Task 0.2: Ejecutar limpieza de tools/

**Files:**
- Delete: archivos clasificados DELETE en Task 0.1
- Modify: `catalog/catalog_master_kora.yml` (remover entradas)

**Step 1: Eliminar archivos obsoletos**

```bash
rm tools/<archivo-delete-1>.yml tools/<archivo-delete-2>.yml ...
```

**Step 2: Marcar deprecated los dudosos**

Para cada archivo DEPRECATE, agregar al inicio:
```yaml
# Status: DEPRECATED — Contenido desactualizado. Será removido o migrado.
```

**Step 3: Actualizar catálogo**

Remover entradas de archivos eliminados de `catalog_master_kora.yml`.

**Step 4: Verificar**

```bash
# No deben quedar refs rotas
grep -r "tools/" agents/ | grep -v "DEPRECATED"
```

**Step 5: Commit**

```bash
git add -A tools/ catalog/catalog_master_kora.yml
git commit -m "chore(tools): auditar y limpiar documentación obsoleta

- DELETE: [lista de archivos eliminados]
- DEPRECATE: [lista de archivos marcados]
- KEEP: [lista de archivos vigentes]
- Catálogo actualizado"
```

---

## Fase 1: Re-fundamentar agent-spec-md.md v5.0.0

### Task 1.1: Reescribir §1 Ontología Categórica y §2 Definiciones

**Files:**
- Modify: `knowledge/foundations/core/kora/agent-spec-md.md`
- Read: `docs/plans/2026-02-23-koda-kora-remediation-design.md` (§2.1, §2.2)
- Read: `/Users/felixsanhueza/Developer/fxsl/knowledge/domains/cat/dynamics/coalgebras.koda.yml`
- Read: `/Users/felixsanhueza/Developer/fxsl/knowledge/domains/cat/dynamics/categorical_systems_theory.koda.yml`

**Step 1: Reescribir §1**

Reemplazar el §1 actual con la fundamentación coalgebraica:
- Un agente es una F-coalgebra `c: U → F(U)` donde `F(U) = (Out × U)^In`
- El update vive en `Kl(M)` (categoría de Kleisli de la mónada M)
- Los 5 componentes esenciales: c, F, U, M, W
- Fuentes: Barbosa (Coalgebra), Spivak (CST/Lenses)
- Preservar la Meta-Cláusula de gobierno por KORA/Spec-MD

**Step 2: Expandir §2 Definiciones**

Agregar a la tabla de definiciones:
- **Lens** — Par (expose, update) que modela la interfaz bidireccional del agente con su entorno
- **Bisimulación** — Relación R entre estados de dos agentes tal que estados relacionados producen outputs indistinguibles
- **Wiring Diagram** — Especificación de cómo los outputs de un agente alimentan los inputs de otro
- **Fibra** — Subestructura ortogonal del espacio de estados U; cada fibra es independientemente evaluable
- **Mónada de Efectos** — Estructura algebraica M que encapsula el tipo de efectos computacionales del agente
- **F-coalgebra** — Par (U, c) donde U es espacio de estados y c: U → F(U) es el morfismo de transición

**Step 3: Actualizar frontmatter**

```yaml
version: "5.0.0"
tags: [spec, agent, architecture, fsm, llm-runtime, coalgebra, lens, categorical]
```

**Step 4: Verificar**

- §1 no menciona topología de archivos (eso va en §4)
- §2 incluye todos los términos nuevos usados en §1
- Ningún término de §2 quedó huérfano (todos se usan en el cuerpo)

**Step 5: Commit**

```bash
git add knowledge/foundations/core/kora/agent-spec-md.md
git commit -m "refactor(agent-spec): §1 ontología coalgebraica + §2 definiciones expandidas

BREAKING: v5.0.0 — fundamentación categórica reemplaza postulados topológicos
- Agente como F-coalgebra c: U → F(U) en Kl(M)
- 5 componentes esenciales: c, F, U, M, W
- Nuevas definiciones: Lens, Bisimulación, Wiring, Fibra, Mónada"
```

---

### Task 1.2: Escribir §3 Componentes Esenciales

**Files:**
- Modify: `knowledge/foundations/core/kora/agent-spec-md.md`

**Step 1: Reemplazar §3 "Primitivas Topológicas" con §3 "Componentes Esenciales"**

§3.1 El Morfismo de Transición c:
- FSM: estados como objetos categóricos, transiciones como morfismos puros
- Propiedades: determinismo (dado estado + input, next-state único en M), composicionalidad (morfismos componen asociativamente), co-inducción (auto-corrección en nodos terminales)
- Ejemplo correcto/incorrecto

§3.2 El Funtor de Interfaz F:
- Define qué tipos de inputs acepta y qué outputs produce
- Incluye semántica de herramientas (tool signatures e invariantes de tipo)
- F(U) = (Out × U)^In para agentes reactivos
- Ejemplo correcto/incorrecto

§3.3 El Espacio de Estados U:
- Descomponible como producto de fibras ortogonales: U = Π(fibras)
- Fibra fenomenológica: personalidad, tono, posicionamiento (cualitativa)
- Fibra de contexto operador: perfil, rutinas, preferencias (externa al agente)
- Fibra episódica: memoria, historia (opcional según plataforma)
- Propiedad: cada fibra es independientemente evaluable
- Ejemplo correcto/incorrecto

§3.4 La Mónada de Efectos M:
- Sandboxing, tool policies, límites de red, credenciales
- Inmutable desde el LLM (pre-compilada por el runtime)
- M encapsula el tipo de efecto: Identity (puro), Powerset (no-determinístico), Distribution (estocástico), Writer (con logging)
- Ejemplo correcto/incorrecto

§3.5 El Diagrama de Wiring W:
- Cómo el agente se compone con otros agentes
- Adjunciones Left ⊣ Right para instanciación de sub-agentes
- Interfaces de routing (qué inputs se conectan a qué agente)
- Propiedad composicional: comportamiento del sistema compuesto calculable desde componentes + wiring
- Ejemplo correcto/incorrecto

**Step 2: Verificar**

- Cada §3.X tiene: definición formal, propiedades, ejemplo correcto/incorrecto
- §3 NO menciona archivos específicos (AGENTS.md, SOUL.md, etc.) — eso va en §4
- Los 5 componentes son mutuamente ortogonales

**Step 3: Commit**

```bash
git add knowledge/foundations/core/kora/agent-spec-md.md
git commit -m "feat(agent-spec): §3 componentes esenciales (c, F, U, M, W)

Reemplaza §3 Primitivas Topológicas con fundamentación categórica:
- §3.1 Morfismo de transición (FSM)
- §3.2 Funtor de interfaz (tipado I/O)
- §3.3 Espacio de estados (fibras ortogonales)
- §3.4 Mónada de efectos (constraints)
- §3.5 Diagrama de wiring (composicionalidad)"
```

---

### Task 1.3: Escribir §4 Instanciación — Topología de Workspace

**Files:**
- Modify: `knowledge/foundations/core/kora/agent-spec-md.md`
- Read: `knowledge/foundations/core/kora/manual-openclaw/02-agente-unidad-fundamental.md`

**Step 1: Escribir §4.1 Principio de Derivación**

La topología es una materialización física de los 5 componentes de §3. Toda topología válida DEBE materializar los 5; PUEDE materializar cada uno en uno o más archivos.

**Step 2: Escribir §4.2 Esquema Canónico KORA**

Tabla de derivación:

| Componente §3 | Archivo | Justificación |
|---|---|---|
| c (§3.1) | AGENTS.md | FSM aislada como grafo de control |
| F (§3.2) | TOOLS.md | Semántica de herramientas segregada |
| U, fibra fenomenológica (§3.3) | SOUL.md | Personalidad aislada del control |
| U, fibra contexto (§3.3) | USER.md | Contexto operador solo en sesión main |
| M (§3.4) | config.json | Policies pre-compiladas, no LLM |
| Endofuntores sobre U | skills/CM-*.md | Lazy evaluation |
| W (§3.5) | Declarado en AGENTS.md §adjunciones | No requiere archivo propio |

IDENTITY.md es OPCIONAL: fibra estática de U para plataformas que separan metadata de identidad de fenomenología.

**Step 3: Escribir §4.3 Extensiones de Plataforma**

Un runtime PUEDE extender la topología canónica. Ejemplo (OpenClaw):
- HEARTBEAT.md, MEMORY.md, memory/, hooks/, BOOTSTRAP.md
- Cada extensión DEBE mapearse a exactamente un componente de §3

**Step 4: Escribir §4.4 Regla de Validez**

Una topología es válida sii:
1. Materializa los 5 componentes de §3
2. Cada archivo pertenece a exactamente un componente
3. Las extensiones no violan invariantes de §8
4. c es evaluable sin archivos de extensión

**Step 5: Verificar**

- §4 se DERIVA de §3 (no postula archivos sin justificación categórica)
- OpenClaw aparece como EJEMPLO, no como mandato
- IDENTITY.md es opcional, no obligatorio

**Step 6: Commit**

```bash
git add knowledge/foundations/core/kora/agent-spec-md.md
git commit -m "feat(agent-spec): §4 topología derivada de componentes categóricos

- §4.1 Principio de derivación (topología ← categorías)
- §4.2 Esquema canónico KORA (6 archivos + skills/)
- §4.3 Extensiones de plataforma (OpenClaw como ejemplo)
- §4.4 Regla de validez (4 criterios)
- IDENTITY.md reclasificado como opcional"
```

---

### Task 1.4: Completar §5 Segregación de Contexto (secciones faltantes)

**Files:**
- Modify: `knowledge/foundations/core/kora/agent-spec-md.md`

**Step 1: Preservar §5.1 (AGENTS.md) y §5.2 (SOUL.md)**

Ya están completos en v4.0.1. Solo ajustar referencias a nueva numeración.

**Step 2: Escribir §5.3 config.json — JSON Schema formal**

Definir el JSON Schema completo:
```json
{
  "type": "object",
  "required": ["allowed_kb", "sandbox"],
  "properties": {
    "allowed_kb": { "type": "array", "items": { "type": "string", "pattern": "^urn:" } },
    "sandbox": { "type": "object", "properties": { "mode": { "enum": ["strict", "permissive"] } } },
    "tools": { "type": "object", "properties": { "allow": { "type": "array" }, "deny": { "type": "array" } } },
    "sub_agents": { "type": "object", "properties": { "max_depth": { "type": "integer" }, "max_concurrent": { "type": "integer" } } }
  }
}
```
Incluir correcto/incorrecto. Invariante: config.json es inmutable desde el LLM.

**Step 3: Expandir §5.4 USER.md**

Agregar grammar completa:
- Frontmatter simplificado (bootstrap schema)
- Secciones obligatorias: Perfil, Rutinas, Preferencias de Output
- Invariante: NO contiene lógica FSM ni policies de seguridad
- NO se inyecta en sub-agentes
- Template completo

**Step 4: Escribir §5.5 TOOLS.md (NUEVO)**

Grammar completa para TOOLS.md:
- Frontmatter simplificado (bootstrap schema)
- Formato por herramienta: nombre, firma inferencial, cuándo usar, cuándo NO usar
- Invariante: TOOLS.md describe semántica, no implementación
- Se inyecta en main + sub-agentes
- Template con ejemplo

**Step 5: Escribir §5.6 skills/CM-*.md (NUEVO)**

Grammar interna para módulos cognitivos:
- Frontmatter: tipo "lazy_load_endofunctor", URN
- Secciones: Propósito, Input/Output, Procedimiento, Signature Output
- Invariante: CM se carga solo cuando la FSM lo invoca
- Template con ejemplo basado en CM-TENSION-EXPLORER

**Step 6: Verificar**

- §5.1-§5.6: cada subsección tiene grammar, template, correcto/incorrecto, invariantes
- No hay huecos: todos los archivos de §4.2 tienen su grammar en §5

**Step 7: Commit**

```bash
git add knowledge/foundations/core/kora/agent-spec-md.md
git commit -m "feat(agent-spec): completar §5 — grammar para config.json, TOOLS.md, CM-*.md

- §5.3 config.json: JSON schema formal + invariante de inmutabilidad
- §5.4 USER.md: grammar expandida + template
- §5.5 TOOLS.md: grammar completa (NUEVO)
- §5.6 skills/CM-*.md: grammar interna (NUEVO)
- Cierra los 4 huecos de v4.0.1"
```

---

### Task 1.5: Actualizar §6-§11 y verificar spec completa

**Files:**
- Modify: `knowledge/foundations/core/kora/agent-spec-md.md`

**Step 1: Preservar §6 Endofuntores Cognitivos**

Ajustar referencias a nueva numeración. Contenido sustancial ya está correcto.

**Step 2: Actualizar §7 Orquestación y Adjunciones**

Agregar referencia formal a W (§3.5). Formalizar que W se materializa como declaraciones de adjunción en AGENTS.md, no como archivo separado.

**Step 3: Preservar §8 Invariantes Topológicos**

Ajustar referencias. Contenido correcto.

**Step 4: Expandir §9 Verificación**

Agregar checks para las nuevas secciones:

| Check | Criterio | Acción si falla |
|---|---|---|
| TOOLS.md completo | Cada tool tiene nombre, firma, cuándo usar/no usar | Completar entradas faltantes |
| config.json válido | Parsea contra JSON schema de §5.3 | Corregir schema |
| CM en skills/ | Todo CM referenciado en AGENTS.md existe como archivo | Crear CM faltante |
| CM grammar | Cada CM tiene: Propósito, I/O, Procedimiento, Signature | Completar secciones |

**Step 5: Actualizar §10 Ejemplo**

Actualizar el ejemplo de workspace bien formado:
- Sin IDENTITY.md obligatorio
- Con TOOLS.md completo
- Con config.json que parsea contra schema

**Step 6: Actualizar §11 Template**

Template actualizado sin IDENTITY.md obligatorio, con templates para todos los archivos.

**Step 7: Verificación completa de la spec**

```bash
# Verificar que no hay secciones vacías o placeholders
grep -n "TODO\|FIXME\|TBD\|PLACEHOLDER" knowledge/foundations/core/kora/agent-spec-md.md
```

Expected: 0 resultados.

```bash
# Verificar que todos los términos de §2 se usan en el cuerpo
# (verificación manual — leer §2 y buscar cada término)
```

**Step 8: Commit**

```bash
git add knowledge/foundations/core/kora/agent-spec-md.md
git commit -m "feat(agent-spec): v5.0.0 completa — §6-§11 actualizados

- §7 Orquestación: W formalizado
- §9 Verificación: checks para TOOLS.md, config.json, CM-*.md
- §10 Ejemplo: actualizado sin IDENTITY.md obligatorio
- §11 Template: completo para todos los archivos del workspace
- agent-spec-md.md v5.0.0 publicada"
```

---

## Fase 2: Diseñar Funtor G (Agentificación)

### Task 2.1: Escribir §12 Agentificación

**Files:**
- Modify: `knowledge/foundations/core/kora/agent-spec-md.md`
- Read: `agents/core/agent_architect.yaml` (ejemplo de input para G₂)

**Step 1: Escribir §12.1 Entrada**

Dos modos del funtor:
- G₁: Requirements → KORA/Agent (construcción desde cero)
- G₂: KODA/Agent.yaml → KORA/Agent (transmutación de legado)

Input aceptado: cualquier YAML monolítico con `KODA_Runtime_Instructions`, estados, identidad.

**Step 2: Escribir §12.2 El Funtor de Transformación G**

Propiedades formales:
- **Fiel:** toda transición del original tiene representación en AGENTS.md
- **Segregador:** separa c, F, U, M en archivos ortogonales
- **Promotor:** inline code → config.json, inline personality → SOUL.md
- **Bisimilar:** G(agent) ≈ agent (comportamiento observable preservado)
- **Idempotente:** G(G(agent)) = G(agent)

**Step 3: Escribir §12.3 Estrategia de Ejecución**

Para G₂ (transmutación):
1. Leer YAML completo y clasificar cada bloque por componente
2. Extraer estados y transiciones → AGENTS.md (grammar de §5.1)
3. Extraer fenomenología (tono, arquetipo, personality) → SOUL.md (grammar de §5.2)
4. Extraer contexto operador → USER.md (grammar de §5.4)
5. Mapear tools/capabilities → TOOLS.md (grammar de §5.5)
6. Extraer policies y sandboxing → config.json (schema de §5.3)
7. Identificar CMs inline (>50 líneas de lógica densa) → skills/CM-*.md (grammar de §5.6)
8. Generar frontmatter para cada archivo
9. Crear directorio workspace con topología de §4.2

Para G₁ (desde cero):
1. Recibir requirements (objetivo, dominio, constraints)
2. Diseñar FSM: estados iniciales, transiciones, nodos terminales
3. Definir interfaz: qué tools necesita, qué outputs produce
4. Definir fenomenología: tono, arquetipo, posicionamiento
5. Definir constraints: qué puede/no puede hacer
6. Generar workspace completo

**Step 4: Escribir §12.4 Verificación Mecánica**

| Check | Método | Criterio de falla |
|---|---|---|
| Conteo de estados | Contar `STATE:` en source vs AGENTS.md | Diferencia > 0 |
| Conteo de CMs | Contar `CM-` en source vs archivos en skills/ | Diferencia > 0 |
| Completitud topológica | Verificar existencia de todos los archivos de §4.2 | Archivo faltante |
| Segregación | Buscar prosa fenomenológica en AGENTS.md | Match encontrado |
| config.json válido | Parsear contra schema §5.3 | Error de parseo |
| Frontmatter | Cada archivo tiene frontmatter de bootstrap | Ausente |

**Step 5: Escribir §12.5 Verificación de Bisimulación**

El agente migrado DEBE ser bisimilar al original:
- Para todo input i del dominio del agente, el output observable del workspace DEBE ser indistinguible del output del YAML monolítico
- Método: seleccionar 5 inputs representativos del dominio, ejecutar contra ambos formatos, comparar outputs
- Si divergencia detectada → identificar qué componente perdió información y corregir

**Step 6: Agregar nuevas definiciones a §2**

Agregar a la tabla: Agentificación, Transmutación, Bisimilaridad de agentes.

**Step 7: Verificar**

- §12 es análogo a md-spec §6 (mismo patrón: entrada, funtor, estrategia, verificación)
- Los pasos de §12.3 referencian las grammars de §5 (no repiten contenido)

**Step 8: Commit**

```bash
git add knowledge/foundations/core/kora/agent-spec-md.md
git commit -m "feat(agent-spec): §12 Agentificación — funtor G para construir/migrar agentes

- §12.1 Entrada: G₁ (desde cero) y G₂ (transmutación KODA→KORA)
- §12.2 Propiedades: fiel, segregador, promotor, bisimilar, idempotente
- §12.3 Estrategia de ejecución (9 pasos para G₂, 6 para G₁)
- §12.4 Verificación mecánica (6 checks)
- §12.5 Verificación de bisimulación"
```

---

## Fase 3: Koraficiar KBs (Template de Proceso)

### Task 3.0: Planificar lote de migración

**Step 1: Listar artefactos del lote actual con metadata**

```bash
# Para el lote actual (ej: gn/gobernanza/)
for f in knowledge/applied/gn/gobernanza/*.yml; do
  name=$(basename "$f")
  lines=$(wc -l < "$f")
  urn=$(grep "urn:" "$f" | head -1)
  echo "$name | $lines | $urn"
done
```

**Step 2: Evaluar pertinencia de cada artefacto**

Para cada archivo: ¿vigente? ¿redundante? ¿obsoleto?
Documentar decisión: MIGRAR / DEPRECAR / FUSIONAR.

---

### Task 3.N: Koraficiar artefacto individual (REPETIR por artefacto)

**Files:**
- Read: `knowledge/applied/{domain}/{archivo}.yml` (source YAML)
- Create: `knowledge/applied/{domain}/{archivo}.md` (target KORA/MD)
- Delete: `knowledge/applied/{domain}/{archivo}.yml` (source, post-verificación)
- Modify: `catalog/catalog_master_kora.yml`

**Step 1: Leer el YAML source completo**

Evaluar: largo (<5K, 5-15K, >15K tokens), estructura, contenido numérico.

**Step 2: Aplicar md-spec §6 (koraficación)**

Seguir la estrategia de ejecución completa:
- §6.4 Evaluación del input
- §6.5 Segmentación si >5K tokens
- §6.6 Telegrafización fiel
- §6.7 Ensamblaje
- §6.8 Normalización (si redundancia)
- §6.9 Frontmatter (nuevo URN: `urn:{ns}:kb:{id}`)
- §6.10 Verificación mecánica
- §6.11 Verificación adversarial si >15K tokens

**Step 3: Verificar**

```bash
# Cifras preservadas
grep -oE '[0-9]+' source.yml | sort -u > /tmp/nums_source
grep -oE '[0-9]+' target.md | sort -u > /tmp/nums_target
diff /tmp/nums_source /tmp/nums_target
```

Expected: sin diferencias (o diferencias justificables como números de versión YAML).

**Step 4: Eliminar source YAML, actualizar catálogo**

**Step 5: Commit (cada 3-5 artefactos)**

```bash
git add knowledge/applied/{domain}/
git commit -m "refactor(kb): koraficiar {N} artefactos de {domain}

- Migrado: {lista}
- Deprecado: {lista si aplica}
- URNs actualizados en catálogo"
```

---

## Fase 4: Agentificar Agentes (Template de Proceso)

### Task 4.N: Agentificar agente individual (REPETIR por agente)

**Files:**
- Read: `agents/{grupo}/agent_{nombre}.yaml` (source YAML monolítico)
- Create: `agents/{grupo}/{nombre}/AGENTS.md`
- Create: `agents/{grupo}/{nombre}/SOUL.md`
- Create: `agents/{grupo}/{nombre}/USER.md`
- Create: `agents/{grupo}/{nombre}/TOOLS.md`
- Create: `agents/{grupo}/{nombre}/config.json`
- Create: `agents/{grupo}/{nombre}/skills/CM-*.md` (si aplica)
- Delete: `agents/{grupo}/agent_{nombre}.yaml` (post-verificación)
- Modify: `catalog/catalog_master_kora.yml`

**Step 1: Leer YAML monolítico y clasificar bloques**

Mapear cada bloque del YAML a un componente categórico:
- `KODA_Runtime_Instructions` / FSM / State Machine → c (AGENTS.md)
- Identity / Personality / Tone → U fibra fenomenológica (SOUL.md)
- User context / Operator → U fibra contexto (USER.md)
- Tools / Capabilities → F (TOOLS.md)
- Policies / Restrictions / KB access → M (config.json)
- Cognitive Models / CMs inline → endofuntores (skills/)

**Step 2: Aplicar agent-spec-md §12.3 (agentificación G₂)**

Generar cada archivo del workspace siguiendo las grammars de §5.

**Step 3: Verificación mecánica (§12.4)**

```bash
# Conteo de estados
grep -c "STATE:" source.yaml
grep -c "STATE:" AGENTS.md
# Deben coincidir

# Segregación: AGENTS.md sin prosa fenomenológica
grep -iE "tono|personalidad|arquetipo|apasionado|empático" AGENTS.md
# Expected: 0 resultados

# config.json parseable
python3 -c "import json; json.load(open('config.json'))"
# Expected: sin error

# Completitud topológica
ls AGENTS.md SOUL.md USER.md TOOLS.md config.json skills/
# Expected: todos presentes
```

**Step 4: Eliminar YAML monolítico, actualizar catálogo**

**Step 5: Commit (cada 2-3 agentes)**

```bash
git add agents/{grupo}/
git commit -m "refactor(agents): agentificar {nombre_1}, {nombre_2} → workspaces

- Aplicado funtor G₂ (KODA/Agent.yaml → KORA/Agent workspace)
- Verificación mecánica: estados, segregación, completitud
- YAML monolíticos eliminados"
```

---

## Fase Final: Gobernanza y Limpieza

### Task F.1: Deprecar artefactos KODA

**Files:**
- Modify: cada archivo en `knowledge/foundations/core/koda/` que tenga sucesor KORA
- Modify: `knowledge/foundations/core/kora/gobernanza.md`
- Modify: `catalog/catalog_master_kora.yml`

**Step 1: Agregar header de deprecación a cada artefacto KODA con sucesor**

```yaml
# Status: DEPRECATED — Sucesor: {URN del sucesor KORA}
# Este artefacto se mantiene para referencia histórica.
```

**Step 2: Actualizar gobernanza.md**

- Agregar al catálogo §3 una columna "Depreca" con URNs KODA reemplazados
- Agregar regla de coexistencia transitoria
- Incrementar versión

**Step 3: Resolver artefactos KODA "Evaluar" del design doc §9**

Para hub-federation, tooling, test, skills-federation:
- Decisión basada en resultados de Fases 1-3
- Si absorbido → marcar deprecated con referencia a dónde se absorbió
- Si necesita sucesor propio → crear artefacto KORA/MD nuevo

**Step 4: Commit**

```bash
git add knowledge/foundations/core/koda/ knowledge/foundations/core/kora/gobernanza.md catalog/
git commit -m "chore(koda): deprecar formalmente artefactos con sucesor KORA

- spec.yml → md-spec.md + spec.yml v2.0
- agent.yml → agent-spec-md.md v5.0
- life.yml → absorbido en agent-spec-md
- transform.yml → md-spec.md §6
- agent-construct.yml → agent-spec-md §12
- [decisiones para hub-federation, tooling, test, skills-federation]"
```

### Task F.2: Actualizar catálogo maestro y verificación final

**Files:**
- Modify: `catalog/catalog_master_kora.yml`

**Step 1: Regenerar catálogo**

```bash
kora index
```

**Step 2: Verificar métricas de éxito**

```bash
# 0 URNs pre-transmutación
grep -r "urn:knowledge:koda:" knowledge/ agents/ | wc -l
# Expected: 0

# 0 YAML en knowledge/applied/
find knowledge/applied/ -name "*.yml" -o -name "*.yaml" | wc -l
# Expected: 0

# 0 YAML monolíticos en agents/
find agents/ -maxdepth 2 -name "agent_*.yaml" | wc -l
# Expected: 0

# Todos los archivos agent-spec-md tienen grammar
grep -c "§5\." knowledge/foundations/core/kora/agent-spec-md.md
# Expected: 6 (§5.1 a §5.6)
```

**Step 3: Commit final**

```bash
git add -A
git commit -m "feat(kora): remediación KODA/KORA completada

Métricas:
- Agentes en workspace: 40/40
- KBs en KORA/MD: 139/139
- URNs pre-transmutación: 0
- Artefactos KODA: todos deprecated
- agent-spec-md v5.0.0: 6/6 secciones con grammar
- tools/: limpio"
```
