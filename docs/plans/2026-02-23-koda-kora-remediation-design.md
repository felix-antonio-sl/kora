# Remediación de Deuda Técnica KODA/KORA — Design Document

**Fecha:** 2026-02-23
**Autor:** FS + Claude Opus 4.6
**Estado:** Aprobado
**Alcance:** Repositorio kora completo

---

## 1. Contexto

KODA (junio 2025) evolucionó a KORA (febrero 2026) mediante renombramiento parcial y reformas doctrinales sucesivas. La migración fue incompleta:

- **40/40 agentes** (100%) usan `KODA_Runtime_Instructions` y formato YAML monolítico
- **139/139 KBs aplicadas** (100%) en formato YAML KODA, no Markdown KORA/MD
- **5 artefactos KODA** (hub-federation, tooling, test, skills-federation, quickstart) sin sucesor KORA
- **753 URNs** en formato pre-transmutación `urn:knowledge:koda:*`
- **agent-spec-md.md v4.0.1** tiene huecos: IDENTITY.md, TOOLS.md, config.json y CM-*.md sin grammar ni schema
- **tools/** contiene ~44K líneas de documentación mayoritariamente desactualizada
- **gobernanza.md** no reconoce la existencia de KODA en su catálogo

---

## 2. Principio Rector: Fundamentación Categórica

La remediación no es una migración mecánica de formato sino una **re-fundamentación**. El modelo teórico precede a toda instanciación.

### 2.1 Esencia Categórica del Agente

De la KB categórica (Barbosa, Spivak) y el análisis con el Arquitecto Categórico v4, un agente es formalmente una **F-coalgebra con interfaz lens en una categoría de Kleisli**:

```
Agente = (U, c: U → F(U))

donde F(U) = (Out × U)^In    (funtor de autómata reactivo)
y el update vive en Kl(M)     (M = mónada de efectos)
```

### 2.2 Los 5 Componentes Esenciales

| Componente | Símbolo | Qué es | Invariante |
|---|---|---|---|
| Morfismo de transición | c | Comportamiento (FSM) | Determinismo en M |
| Funtor de interfaz | F | Tipado I/O (qué acciones existen) | Álgebra cerrada |
| Espacio de estados | U | Estado interno (descomponible en fibras) | Completitud |
| Mónada de efectos | M | Constraints y seguridad | Límite de efectos |
| Diagrama de wiring | W | Interfaz composicional | Preservación bajo composición |

### 2.3 La Topología Actual como Instanciación

La topología de 7 archivos (AGENTS.md, SOUL.md, USER.md, IDENTITY.md, TOOLS.md, config.json, skills/) es una instanciación razonable pero no canónica:

- IDENTITY.md no es un componente dinámico — es metadata estática (fibra opcional de U)
- TOOLS.md y CM-*.md no tienen grammar definida en la spec
- W (wiring) no tiene materialización propia — está implícito en AGENTS.md

---

## 3. Enfoque: Fundación por Capas

Cinco fases donde cada una entrega valor independientemente y es prerequisito de la siguiente.

```
Fase 0: Limpiar tools/
    ↓
Fase 1: Re-fundamentar agent-spec-md.md v5.0.0
    ↓
Fase 2: Diseñar Funtor G (Agentificación)
    ↓
Fase 3: Koraficiar 139 KBs (YAML→MD)
    ↓
Fase 4: Agentificar 40 agentes (YAML→workspace)
```

---

## 4. Fase 0: Limpiar tools/

### Objetivo

Eliminar documentación desactualizada que contamina el catálogo y consume tokens.

### Acción

Para cada uno de los 21 archivos YAML (~44K líneas) en `tools/`:

1. Evaluar vigencia del contenido
2. Verificar si algún agente lo referencia como dependencia
3. Si obsoleto → eliminar
4. Si dudoso → marcar `status: deprecated`
5. Si vigente → evaluar si debe migrar a KORA/MD (Fase 3)

### Entregable

`tools/` reducido a solo lo vigente. Catálogo actualizado.

---

## 5. Fase 1: Re-fundamentar agent-spec-md.md v5.0.0

### Objetivo

Reescribir la spec para que derive la topología de la descomposición categórica esencial. La topología actual (7 archivos) se convierte en una instanciación derivada, no en un postulado.

### Estructura Propuesta

```
§1. Ontología Categórica (reescrito)
    - Un agente es una F-coalgebra c: U → F(U) en Kl(M)
    - Los 5 componentes esenciales
    - Fuentes: Barbosa (Coalgebra), Spivak (CST/Lenses), Fong & Spivak (Seven Sketches)

§2. Definiciones (expandido)
    - Nuevos términos: Lens, Bisimulación, Wiring Diagram, Fibra, Mónada de Efectos

§3. Componentes Esenciales (NUEVA — reemplaza §3 "Primitivas Topológicas")
    §3.1 El Morfismo de Transición c (comportamiento)
        - Es la FSM: estados como objetos, transiciones como morfismos
        - Propiedades: determinismo, composicionalidad, co-inducción
    §3.2 El Funtor de Interfaz F (tipado I/O)
        - Define qué tipos de inputs acepta y qué outputs produce
        - Incluye semántica de herramientas (tool signatures)
    §3.3 El Espacio de Estados U (fibras)
        - Descomponible como producto de fibras ortogonales
        - Fibra fenomenológica (personalidad, tono, posicionamiento)
        - Fibra de contexto operador (perfil, rutinas, preferencias)
        - Fibra episódica (memoria, historia) — opcional según plataforma
    §3.4 La Mónada de Efectos M (constraints)
        - Sandboxing, tool policies, límites de red
        - Inmutable desde el LLM (pre-compilada por el runtime)
    §3.5 El Diagrama de Wiring W (composicionalidad)
        - Cómo el agente se compone con otros agentes
        - Adjunciones para sub-agentes
        - Interfaces de routing y messaging

§4. Instanciación: Topología de Workspace (derivada de §3)
    §4.1 Principio de Derivación
        La topología es una materialización física de los 5 componentes.
        Toda topología válida DEBE materializar los 5;
        PUEDE materializar cada uno en uno o más archivos.

    §4.2 Esquema Canónico KORA
        /agents/{nombre}/
        ├── AGENTS.md      ← c (morfismo de transición)
        ├── SOUL.md         ← U, fibra fenomenológica
        ├── USER.md         ← U, fibra contexto operador
        ├── TOOLS.md        ← F (funtor de interfaz)
        ├── config.json     ← M (mónada de efectos)
        └── skills/         ← endofuntores sobre U
            └── CM-*.md

        IDENTITY.md es OPCIONAL: fibra estática de U para plataformas
        que requieren separar metadata de identidad de fenomenología.

    §4.3 Extensiones de Plataforma
        Un runtime PUEDE extender la topología con archivos adicionales
        que materialicen capacidades específicas de la plataforma.

        Ejemplo de extensión (runtime tipo OpenClaw):
        - HEARTBEAT.md    → checklist periódico (extensión de c)
        - MEMORY.md       → memoria curada (extensión de U, fibra episódica)
        - memory/         → logs diarios (extensión de U, acceso on-demand)
        - hooks/          → event handlers (extensión de M)
        - BOOTSTRAP.md    → ritual de onboarding (efímero)

        Estas extensiones NO forman parte del esquema canónico KORA.
        Cada extensión DEBE mapearse a exactamente un componente de §3.

    §4.4 Regla de Validez
        Una topología es válida sii:
        1. Materializa los 5 componentes de §3
        2. Cada archivo pertenece a exactamente un componente
        3. Las extensiones no violan invariantes de §8
        4. c es evaluable sin archivos de extensión

§5. Segregación de Contexto (preservado + completado)
    §5.1 AGENTS.md — grammar, template, invariantes (preservado)
    §5.2 SOUL.md — grammar, template, invariantes (preservado)
    §5.3 config.json — JSON schema formal (NUEVO: schema completo)
    §5.4 USER.md — grammar, template, invariantes (expandido)
    §5.5 TOOLS.md — grammar, template, invariantes (NUEVO)
    §5.6 skills/CM-*.md — grammar interna, template (NUEVO)

§6. Endofuntores Cognitivos (preservado)
§7. Orquestación y Adjunciones (preservado, con W formalizado)
§8. Invariantes Topológicos (preservado)
§9. Verificación (expandido con checks para §5.5, §5.6)
§10. Ejemplo (actualizado sin IDENTITY.md obligatorio)
§11. Template (actualizado)
```

### Cambios Clave vs v4.0.1

| Aspecto | v4.0.1 | v5.0.0 |
|---|---|---|
| Fundamentación | Postulada (topología primero) | Derivada (categorías → topología) |
| IDENTITY.md | Obligatorio | Opcional (metadata estática) |
| TOOLS.md | 1 línea en §3 | Sección completa §5.5 |
| config.json | Sin schema | JSON schema formal §5.3 |
| CM-*.md | Sin grammar interna | Grammar completa §5.6 |
| Extensiones de plataforma | No contempladas | §4.3 con ejemplo OpenClaw |
| Wiring (W) | Implícito | Formalizado en §3.5 |

### Entregable

`agent-spec-md.md` v5.0.0 publicada.

---

## 6. Fase 2: Diseñar Funtor G (Agentificación)

### Objetivo

Crear la sección operativa de agent-spec-md.md que define CÓMO construir o migrar agentes (análogo a md-spec §6.3-§6.12 para koraficación).

### Estructura — nueva §12 de agent-spec-md.md

```
§12. Agentificación
    §12.1 Entrada
        - G₁: Requirements → KORA/Agent (construcción desde cero)
        - G₂: KODA/Agent.yaml → KORA/Agent (transmutación)

    §12.2 El Funtor de Transformación G
        Propiedades:
        - Fiel: toda transición del original tiene representación en el workspace
        - Segregador: separa c, F, U, M en archivos ortogonales
        - Promotor: inline code → config.json, inline personality → SOUL.md
        - Bisimilar: G(agent) ≈ agent (comportamiento observable preservado)

    §12.3 Estrategia de Ejecución
        Para G₂ (transmutación de YAML monolítico):
        1. Identificar estados y transiciones → AGENTS.md
        2. Extraer fenomenología (tono, arquetipo) → SOUL.md
        3. Extraer contexto operador → USER.md
        4. Mapear tools/capabilities → TOOLS.md
        5. Extraer policies y sandboxing → config.json
        6. Identificar CMs inline (>50 líneas de lógica densa) → skills/CM-*.md
        7. Generar frontmatter para cada archivo

    §12.4 Verificación Mecánica
        - Conteo de estados: source vs AGENTS.md
        - Conteo de CMs: source vs skills/
        - Completitud topológica: todos los archivos obligatorios presentes
        - Segregación: AGENTS.md sin prosa fenomenológica

    §12.5 Verificación de Bisimulación
        El agente migrado DEBE ser bisimilar al original:
        para todo input i, el output observable del workspace
        DEBE ser indistinguible del output del YAML monolítico.
```

### Entregable

§12 integrada en agent-spec-md.md v5.0.0.

---

## 7. Fase 3: Koraficiar 139 KBs

### Objetivo

Migrar los 139 artefactos YAML de `knowledge/applied/` a formato KORA/MD. Oportunidad para evaluar calidad, pertinencia y actualización.

### Proceso por Artefacto

1. **Evaluar pertinencia:** ¿Sigue vigente? ¿Es redundante con otro artefacto?
   - Si obsoleto → deprecar (no migrar)
   - Si redundante → fusionar con el artefacto canónico
   - Si vigente → continuar

2. **Buscar fuente original:**
   - Si existe documento humano original → koraficiar desde fuente (md-spec §6)
   - Si no existe → koraficiar desde YAML (el YAML es la fuente)

3. **Aplicar md-spec §6 completo:**
   - Evaluación del input (§6.4)
   - Segmentación si >5K tokens (§6.5)
   - Telegrafización fiel (§6.6)
   - Ensamblaje (§6.7)
   - Normalización opcional (§6.8)
   - Frontmatter (§6.9)
   - Verificación mecánica (§6.10)
   - Verificación adversarial si >15K tokens (§6.11)
   - Registro en catálogo (§6.12)

4. **Actualizar URNs:** Migrar de `urn:knowledge:koda:*` a `urn:{namespace}:kb:*`

5. **Actualizar referencias cruzadas:** Todo artefacto que referenciaba al YAML debe apuntar al nuevo MD

### Orden de Migración (por dependencias y criticidad)

| Prioridad | Dominio | Archivos | Justificación |
|---|---|---|---|
| 1 | gn/gobernanza/ | 22 | Estrategia y visión — alta referenciación cruzada |
| 2 | gn/normativa/ | 6 | Marco legal — base para otros artefactos |
| 3 | gn/gestion/ | 10 | Operacional — consumido por agentes de dominio |
| 4 | gn/manuales/ | 16 | Procedimientos — alto volumen |
| 5 | gn/guias/ | 7 | Guías operacionales |
| 6 | gn/bpmn/ | 13 | Procesos — formato especial |
| 7 | gn/ris/ | 10 | Registros de inversión |
| 8 | legal/ | 19 | Marco legal laboral |
| 9 | mgmt/ | 4 | Gestión organizacional |
| 10 | tde/ | ~12 | Transformación digital |

### Entregable

`knowledge/applied/` 100% en formato KORA/MD. URNs actualizados. Catálogo limpio.

---

## 8. Fase 4: Agentificar 40 Agentes

### Objetivo

Migrar los 40 agentes YAML monolíticos a workspaces KORA/Agent aplicando el funtor G₂.

### Proceso por Agente

1. **Aplicar G₂** al YAML monolítico (agent-spec-md §12.3)
2. **Generar workspace** con la topología de §4.2
3. **Verificación mecánica** (§12.4)
4. **Verificación de bisimulación** (§12.5)
5. **Eliminar YAML monolítico** original
6. **Actualizar catálogo**

### Orden de Migración

| Prioridad | Grupo | Agentes | Justificación |
|---|---|---|---|
| 1 | core/ | 6 | Fundacionales — validar G₂ primero aquí |
| 2 | architecture/ | 9 | Consumen KB categórica — alta complejidad |
| 3 | qa_ops/ | 4 | Testing/CI — validar pipeline |
| 4 | engineering/ | 5 | Técnicos |
| 5 | domain/ | 17 | Dominio específico — mayor volumen |

### Entregable

`agents/` 100% en formato workspace. Catálogo actualizado.

---

## 9. Artefactos KODA: Destino

Los 11 artefactos en `knowledge/foundations/core/koda/` requieren decisión explícita:

| Artefacto KODA | Refs | Destino propuesto |
|---|---|---|
| `spec.yml` (KODA/Spec) | Alto | Deprecar. Sucesor: `kora/spec.yml` v2.0 + `md-spec.md` |
| `agent.yml` (KODA/Agent) | Alto | Deprecar. Sucesor: `agent-spec-md.md` v5.0 |
| `life.yml` (KODA/Life) | Medio | Deprecar. Conceptos absorbidos en agent-spec-md v5.0 |
| `transform.yml` | Medio | Deprecar. Sucesor: `md-spec.md` §6 (koraficación) |
| `agent-construct.yml` | Medio | Deprecar. Sucesor: `agent-spec-md.md` §12 (funtor G) |
| `hub-federation.yml` | 21 refs | Evaluar: ¿absorber en gobernanza.md o crear sucesor KORA? |
| `tooling.yml` | 17 refs | Evaluar: ¿absorber en agent-spec-md §5.5 o crear sucesor? |
| `test.yml` | 16 refs | Evaluar: crear sucesor KORA/MD (testing merece spec propia) |
| `skills-federation.yml` | 5 refs | Evaluar: ¿absorber en gobernanza.md §extensiones? |
| `quickstart.yml` | 6 refs | Deprecar. Reemplazar por guía derivada post-migración |
| `schema-versioning.yml` | Bajo | Deprecar. Conceptos en gobernanza.md |

Los marcados "Evaluar" se resuelven durante Fase 1 (al completar agent-spec-md) y Fase 3 (al migrar KBs).

---

## 10. Gobernanza Post-Migración

Al completar las 5 fases, `gobernanza.md` debe actualizarse para reconocer:

1. **Catálogo expandido** — Solo artefactos KORA (KODA deprecado formalmente)
2. **Topología del monorepo** — Si se requiere (sección nueva en gobernanza)
3. **Regla de coexistencia** — Período de transición donde artefactos KODA coexisten con URN redirect

---

## 11. Métricas de Éxito

| Métrica | Estado Actual | Target |
|---|---|---|
| Agentes en formato workspace | 0/40 (0%) | 40/40 (100%) |
| KBs en formato KORA/MD | 0/139 (0%) | 139/139 (100%) |
| URNs pre-transmutación | 753 | 0 |
| Artefactos KODA activos | 11 | 0 (todos deprecated o absorbidos) |
| Secciones de agent-spec-md sin grammar | 4/7 | 0/6 |
| tools/ líneas obsoletas | ~44K | <5K (solo vigente) |

---

## 12. Fuentes

- Barbosa, L. "Coalgebra for the Working Software Engineer" — modelo coalgebraico de agentes
- Spivak, D. "Categorical Systems Theory" — lenses y wiring diagrams
- Fong & Spivak, "Seven Sketches in Compositionality" — fundamentos
- Fukada, 2024. "Action is the Primary Key" — memoria episódica categórica
- KB interna: `/knowledge/domains/cat/` (23 artefactos)
- Agente: Arquitecto Categórico v4 (`/fxsl/agents/arquitecto-categorico-v4/`)
- Manual OpenClaw: `/knowledge/foundations/core/kora/manual-openclaw/` (25 capítulos)
