---
_manifest:
  urn: "urn:kora:kb:skill-spec-md"
  provenance:
    created_by: "FS"
    created_at: "2026-02-26"
    source: "agent-spec-md §5.6, KORA categorical-foundations 02, Seven Sketches (Fong & Spivak)"
version: "2.0.0"
status: published
tags: [spec, skill, cm, progressive-disclosure, lazy-evaluation, script-protocol, wrap-extract, traceability]
lang: es
---

# KORA/Skill-Spec --- Especificacion de Skills v2.0.0

## 1. What is a Skill

> Este documento es prescriptivo y **ESTA GOBERNADO** por [KORA/Spec-MD](urn:kora:kb:spec-md).

Un Skill es la unidad de capacidad cognitiva invocable por un agente KORA bajo evaluacion diferida. Todo Cognitive Model (CM) existente es automaticamente un Skill valido en su forma degenerada, sin modificacion. La forma extendida agrega capacidades (scripts, referencias, assets) que se pierden al extraer el CM Core.

```python
class Skill:
    """
    A Skill wraps a Cognitive Model (CM) with optional executable capabilities.
    Every CM is automatically a valid Skill (degenerate form).
    """
    cm_core: CMCore           # The 4 mandatory sections (always present)
    scripts: Optional[Dir]     # Executable code (extended form only)
    references: Optional[Dir]  # Deep documentation (extended form only)
    assets: Optional[Dir]      # Static files, schemas (extended form only)

    @property
    def is_degenerate(self) -> bool:
        """A degenerate Skill is just a CM with no extras."""
        return self.scripts is None and self.references is None

    def extract_cm(self) -> CMCore:
        """Extract: Skill -> CM Core. Discards scripts/references/assets."""
        return self.cm_core  # Always preserves the 4 sections

    @classmethod
    def wrap(cls, cm: CMCore) -> 'Skill':
        """Wrap: CM -> Skill. Creates extended form with empty directories."""
        return cls(cm_core=cm, scripts=Dir.empty(), references=Dir.empty(), assets=Dir.empty())
```

Traces to: formal/02 §2.3 (eta isomorphism — every CM is a valid Skill)

### 1.1 Alcance

Esta especificacion gobierna:

1. Skills dentro de workspaces de agente (`agents/{ns}/{name}/skills/`)
2. Skills federados en el directorio compartido (`skills/{namespace}/`)
3. La relacion formal entre CM y Skill via los procesos Wrap/Extract

Esta especificacion **NO DEBE** contradecir [agent-spec-md](urn:kora:kb:agent-spec-md). Las reglas de CM grammar (agent-spec-md §5.6) se heredan integramente; esta especificacion las extiende.

---

## 2. Definiciones

La tabla de esta seccion **DEBE** incluir todo termino clave con significado preciso dentro de esta especificacion:

**Correcto:** `El documento usa "Progressive Disclosure" y "Gating"; ambos aparecen definidos en esta tabla.`
**Incorrecto:** `El documento usa "Token Budget" como termino clave y no existe entrada para "Token Budget".`

| Termino | Definicion |
| --- | --- |
| **Skill** | Unidad de capacidad cognitiva invocable bajo evaluacion diferida. Puede ser degenerado (CM puro) o extendido (directorio con SKILL.md) |
| **CM (Cognitive Model)** | Proceso cognitivo aislado definido en agent-spec-md §5.6. Archivo CM-*.md con 4 secciones obligatorias |
| **Wrap** | Proceso que envuelve un CM en un directorio con SKILL.md, agregando scripts, referencias y assets opcionales. CM -> Skill extendido |
| **Extract** | Proceso que extrae las 4 secciones CM Core de un Skill, descartando directorios opcionales. Skill -> CM Core |
| **Progressive Disclosure** | Patron de carga en 3 fases (Discover, Activate, Execute) que minimiza tokens inyectados al LLM exponiendo informacion incrementalmente |
| **SKILL.md** | Archivo core de un Skill extendido; contiene frontmatter extendido y body con secciones CM Core + secciones opcionales |
| **Skill Degenerado** | Skill en forma CM pura: archivo CM-*.md sin directorio envolvente. Isomorfo a su CM via Extract(Wrap(CM)) = CM |
| **Skill Extendido** | Skill en forma directorio: carpeta con SKILL.md + subdirectorios opcionales (scripts/, references/, assets/) |
| **Gating** | Mecanismo por el cual la FSM del agente decide si invocar un Skill; materializado como condicion en las transiciones de AGENTS.md |
| **CM Core** | Las 4 secciones obligatorias de un CM (Proposito, I/O, Procedimiento, Signature Output) que todo Skill **DEBE** preservar |
| **Script Protocol** | Convencion que establece Python 3 como lingua franca para scripts ejecutables dentro de Skills extendidos |

---

## 3. Anatomia del Skill

### 3.1 Forma Degenerada (CM-only)

La forma degenerada es identica a la grammar de agent-spec-md §5.6. Todo archivo CM-*.md existente que cumpla esa grammar es un Skill valido sin modificacion.

Traces to: formal/02 §2.3 (eta isomorphism)

**Grammar --- Secciones obligatorias (CM Core):**

1. **Proposito:** que transformacion cognitiva realiza este Skill.
2. **Input/Output:** que recibe del estado actual y que produce.
3. **Procedimiento:** pasos del proceso cognitivo.
4. **Signature Output:** formato esperado del resultado.

**Frontmatter:**

```yaml
---
_manifest:
  urn: "urn:{namespace}:skill:{nombre-agente}-{skill-id}:{version}"
  type: "lazy_load_endofunctor"
---
```

**Correcto:** `Un archivo CM-evaluador-riesgo.md con las 4 secciones CM Core y frontmatter de bootstrap. Es Skill degenerado valido.`
**Incorrecto:** `Un archivo CM-evaluador-riesgo.md sin seccion Signature Output. Viola CM grammar y por tanto no es Skill valido.`

### 3.2 Forma Extendida

La forma extendida envuelve el CM Core en un directorio con capacidades adicionales. Es el resultado de aplicar Wrap a un CM.

**Topologia:**

```text
{nombre-del-skill}/
  SKILL.md           <- (Obligatorio) CM Core + frontmatter extendido + secciones opcionales
  scripts/           <- (Opcional) Codigo ejecutable y logica
  references/        <- (Opcional) Documentacion tecnica profunda
  assets/            <- (Opcional) Archivos estaticos, esquemas, plantillas
```

**Frontmatter extendido de SKILL.md:**

```yaml
---
_manifest:
  urn: "urn:{namespace}:skill:{nombre-agente}-{skill-id}:{version}"
  type: "skill_extended"
name: "{nombre-del-skill}"
description: "{1-1024 chars. Que hace + gatilladores semanticos}"
version: "{semver}"
status: draft|published|deprecated
lang: "{ISO 639-1}"
compatibility: "{notas de dependencias ambientales, max 500 chars}"
allowed-tools: "{lista separada por espacio de herramientas preaprobadas}"
requires: "{dependencias de runtime}"
---
```

**Reglas del frontmatter extendido:**

- `name` **DEBE** ser 1-64 caracteres, solo minusculas, guiones y alfanumericos. **DEBE** coincidir con el nombre del directorio padre.
- `description` **DEBE** ser 1-1024 caracteres. **DEBE** describir que hace y establecer gatilladores semanticos.
- `allowed-tools` **PUEDE** declarar herramientas preaprobadas. Toda herramienta declarada **DEBE** ser subconjunto de la interface declarada en TOOLS.md del agente contenedor.
- `requires` **PUEDE** declarar dependencias. Toda dependencia **DEBE** ser compatible con security en config.json del agente contenedor.

**Body de SKILL.md --- Secciones:**

| # | Seccion | Obligatoria | Contenido |
|---|---------|-------------|-----------|
| 1 | Proposito | Si (CM Core) | Que transformacion cognitiva realiza |
| 2 | Input/Output | Si (CM Core) | Tipos de entrada y salida |
| 3 | Procedimiento | Si (CM Core) | Pasos del proceso cognitivo |
| 4 | Signature Output | Si (CM Core) | Formato esperado del resultado |
| 5 | Scripts | No | Instrucciones para invocar codigo en scripts/ |
| 6 | References | No | Punteros a documentacion en references/ |
| 7 | Examples | No | Ejemplos concretos de uso |

**Correcto:** `Un directorio analisis-legal/ con SKILL.md que tiene las 4 secciones CM Core + seccion Scripts que referencia scripts/analyze.py.`
**Incorrecto:** `Un directorio analisis-legal/ sin SKILL.md. El directorio existe pero no tiene archivo core.`

### 3.3 Script Protocol

Todo script ejecutable dentro de un Skill extendido **DEBE** seguir el Script Protocol:

1. Todo script **DEBE** ser Python 3. Python es la lingua franca de scripts KORA.
2. Todo I/O **DEBE** ser via stdin/stdout en formato JSON.
3. El SKILL.md **DEBE** documentar el pipeline de scripts en pasos numerados con I/O concreto.
4. La primera linea del script **PUEDE** incluir como comentario una signature formal (opcional, para trazabilidad a la capa categorica).

```python
# Traces to: formal/02 §6 (Kleisli composition)
"""
classify_initiative.py — Classifies GORE initiatives by functional area.

Input (stdin JSON):
  { "description": "string", "area": "string" }

Output (stdout JSON):
  { "classification": "enum(inversiones|rrhh|presupuesto)", "confidence": float }
"""
import json, sys

def classify(data: dict) -> dict:
    # Implementation...
    return {"classification": "inversiones", "confidence": 0.95}

if __name__ == "__main__":
    data = json.load(sys.stdin)
    result = classify(data)
    json.dump(result, sys.stdout)
```

**Correcto:** `scripts/classify.py lee JSON de stdin, produce JSON en stdout. SKILL.md documenta: "Paso 1: ejecutar scripts/classify.py con input {description, area}. Output: {classification, confidence}."`
**Incorrecto:** `scripts/classify.sh es un script Bash que lee de un archivo hardcoded y escribe a otro archivo. Viola lingua franca Python y protocolo stdin/stdout.`

---

## 4. Relationship Between CMs and Skills

### 4.1 Las Dos Operaciones

**Wrap** toma un CM y produce un Skill extendido. **Extract** toma un Skill y extrae su CM Core.

Traces to: formal/02 §2 (Free/Forget adjunction)

### 4.2 Wrap: CM -> Skill Extendido

Wrap toma un CM y produce un Skill extendido:

```python
def wrap(cm: CMCore) -> ExtendedSkill:
    """
    Wrap a CM into an extended Skill directory.
    Preserves all CM content and adds extensible structure.
    """
    return ExtendedSkill(
        skill_md=SkillMD(cm_core=cm, frontmatter=generate_extended_frontmatter(cm)),
        scripts=Dir.empty(),       # Available for extension
        references=Dir.empty(),    # Available for extension
        assets=Dir.empty()         # Available for extension
    )
```

Wrap preserva todo el contenido del CM y agrega la estructura envolvente.

### 4.3 Extract: Skill -> CM Core

Extract toma un Skill y extrae su CM Core:

```python
def extract(skill: Skill) -> CMCore:
    """
    Extract the CM Core from a Skill.
    Discards scripts, references, assets, and sections 5-7.
    """
    return CMCore(
        purpose=skill.cm_core.purpose,
        io=skill.cm_core.io,
        procedure=skill.cm_core.procedure,
        signature_output=skill.cm_core.signature_output
    )
```

### 4.4 Propiedades

1. **Extract(Wrap(CM)) = CM:** Aplicar Wrap a un CM y luego Extract produce un CM identico al original. Las 4 secciones CM Core se preservan exactamente. Esta propiedad garantiza **backward compatibility**: todo CM existente funciona sin modificacion en el ecosistema de Skills.
   Traces to: formal/02 §2.3 (eta isomorphism)

2. **Wrap(Extract(Skill)) es incompleto:** Aplicar Extract a un Skill y luego Wrap produce un Skill que pierde los scripts, referencias y assets del Skill original. La informacion ejecutable no sobrevive el round-trip.

3. **Compatibilidad:**
   - Extraer el Skill reconstruido equivale a extraer el original.
   - Reconstruir un CM envuelto equivale al Skill original (sin extras).

### 4.5 Consecuencia Operacional

La relacion Wrap/Extract se materializa en dos modos de operacion del runtime:

| Modo | Operacion | Cuando | Tokens |
|------|-----------|--------|--------|
| Lazy eval | Extract + inject | FSM invoca CM; runtime inyecta solo CM Core | ~5000 tok |
| Full runtime | Wrap + inject | Skill necesita scripts/assets; runtime monta directorio completo | Variable |

**Correcto:** `El runtime detecta que el Skill es degenerado (CM puro), aplica Extract implicito e inyecta ~3000 tokens de CM Core.`
**Incorrecto:** `El runtime carga el directorio completo de un Skill extendido (scripts + references + assets) cuando la FSM solo necesita el CM Core.`

---

## 5. Progressive Disclosure Lifecycle

El ciclo de vida de un Skill se estructura en 3 fases que minimizan tokens inyectados al LLM:

| Fase | Tokens aprox. | Contenido en context window | Operacion |
|------|---------------|----------------------------|-----------|
| **Discover** | ~100/skill | name + description (del frontmatter) | Registry evaluation |
| **Activate** | <=5000 | CM Core completo (4 secciones) | Extract(Skill) inyectado |
| **Execute** | Variable | CM Core + scripts/references bajo demanda | Full Skill montado |

### 5.1 Fase Discover

El agente conoce la existencia del Skill por su name y description. El costo es ~100 tokens por Skill descubierto. El LLM decide si activar el Skill basandose en el Gating de la FSM.

### 5.2 Fase Activate

La FSM invoca el Skill. El runtime inyecta el CM Core (Extract del Skill) al context window. El presupuesto **NO DEBE** exceder 5000 tokens por Skill activado.

### 5.3 Fase Execute

Si el CM Core referencia scripts o archivos en references/, el runtime los monta bajo demanda. Esta fase solo aplica a Skills extendidos (Wrap). Para Skills degenerados, Execute = Activate.

**Reglas de Token Economy:**

- Un Skill activado **NO DEBE** exceder 5000 tokens en su CM Core.
- Las secciones opcionales (5-7) de un SKILL.md **NO DEBEN** inyectarse en Activate; solo en Execute bajo demanda.
- El runtime **DEBE** implementar Progressive Disclosure: Discover primero, Activate solo cuando la FSM lo requiera, Execute solo cuando el CM Core lo instruya.

**Correcto:** `La FSM transiciona a S-EVAL, invoca CM-evaluador. El runtime inyecta las 4 secciones CM Core (~4000 tok). Si el procedimiento dice "ejecuta scripts/analyze.py", el runtime monta el script.`
**Incorrecto:** `El runtime inyecta al bootstrap todos los Skills del agente (~50000 tok total). Viola Token Economy y evaluacion diferida.`

---

## 6. Topologia del Skill

### 6.1 Dentro de Workspace --- Forma Degenerada

```text
agents/{ns}/{name}/skills/CM-{skill-id}.md
```

Un archivo CM-*.md en el directorio skills/ de un workspace de agente. Es la forma heredada de agent-spec-md §5.6 y **DEBE** seguir siendo valida sin modificacion.

**URN:** `urn:{ns}:skill:{name}-cm-{skill-id}:{version}`

### 6.2 Dentro de Workspace --- Forma Extendida

```text
agents/{ns}/{name}/skills/{nombre-del-skill}/
  SKILL.md
  scripts/
  references/
  assets/
```

Un directorio dentro de skills/ que contiene SKILL.md y subdirectorios opcionales.

**URN:** `urn:{ns}:skill:{name}-{skill-id}:{version}`

### 6.3 Federado

```text
skills/{namespace}/{nombre-del-skill}/
  SKILL.md
  scripts/
  references/
  assets/
```

Un Skill compartido entre multiples agentes, residiendo en el directorio global skills/. Los Skills federados **DEBEN** ser forma extendida (directorio con SKILL.md).

**URN:** `urn:{ns}:skill:{skill-id}:{version}`

### 6.4 Reglas de Coexistencia

- Un Skill degenerado y un Skill extendido con el mismo identificador **NO DEBEN** coexistir en el mismo workspace.
- Un Skill federado **PUEDE** coexistir con un Skill local del mismo nombre si el agente declara precedencia en config.json.
- La **promocion** de un Skill local a federado **DEBE** preservar el CM Core intacto (Extract(Wrap(CM)) = CM).

**Correcto:** `agents/kora/guardian/skills/CM-validador.md existe como Skill degenerado. No hay directorio validador/ en el mismo skills/.`
**Incorrecto:** `agents/kora/guardian/skills/CM-validador.md Y agents/kora/guardian/skills/validador/SKILL.md coexisten para el mismo Skill.`

---

## 7. Integracion con agent-spec-md

Esta especificacion extiende y se integra con [agent-spec-md](urn:kora:kb:agent-spec-md) v7.0.0 en los siguientes puntos:

| Ref agent-spec-md | Relacion | Regla |
|--------------------|----------|-------|
| §5.6 (CM grammar) | Herencia | Las 4 secciones CM Core de esta spec son identicas a la grammar de §5.6 |
| §3.2 (Interface) | Restriccion | `allowed-tools` de un Skill **DEBE** ser subconjunto de interface declarada en TOOLS.md |
| §3.4 (Security) | Restriccion | `requires` de un Skill **DEBE** ser compatible con security en config.json |
| §6 (Lazy eval) | Extension | Progressive Disclosure (§5) extiende lazy eval con 3 fases explicitas |
| §14 (Discovery) | Alimentacion | Los Skills son los objetos que el proceso de discovery descubre e indexa |

**Invariante de integracion:** Ninguna regla de esta especificacion **DEBE** contradecir agent-spec-md. En caso de conflicto percibido, agent-spec-md prevalece conforme a [gobernanza](urn:kora:kb:gobernanza) §4.1.

**Correcto:** `Un Skill declara allowed-tools: ["search_kb", "read_file"]. TOOLS.md del agente declara ambas herramientas. Subconjunto valido.`
**Incorrecto:** `Un Skill declara allowed-tools: ["execute_sql"]. TOOLS.md del agente no declara execute_sql. Violacion de interface.`

---

## 8. Invariantes

### 8.1 Backward Compatibility

Todo CM-*.md existente que cumpla agent-spec-md §5.6 **DEBE** ser un Skill degenerado valido sin modificacion. La introduccion de esta especificacion **NO DEBE** invalidar ningun artefacto existente.

Traces to: formal/02 §2.3 (eta isomorphism)

### 8.2 Round-Trip Preservation

La operacion Extract(Wrap(CM)) **DEBE** producir un CM identico al original. Aplicar Wrap y luego Extract a cualquier CM produce un CM identico al original. Si alguna implementacion viola esta propiedad, la implementacion es incorrecta, no la especificacion.

Traces to: formal/02 §2.3 (eta isomorphism)

### 8.3 Token Economy

El CM Core de un Skill activado **NO DEBE** exceder 5000 tokens. Esta restriccion aplica tanto a Skills degenerados como al CM Core de Skills extendidos.

### 8.4 Segregacion CM Core

Las secciones CM Core (1-4) **NO DEBEN** contener logica de transicion de la FSM, politicas de sandboxing ni personalidad del agente. Un Skill es un proceso cognitivo puro.

### 8.5 Referencia Relativa

Dentro de un SKILL.md, toda referencia a archivos en scripts/, references/ o assets/ **DEBE** usar rutas relativas.

**Correcto:** `"Ejecuta el script: scripts/extract.py"`
**Incorrecto:** `"Ejecuta el script: /Users/dev/kora/agents/gn/goreologo/skills/analisis/scripts/extract.py"`

### 8.6 Name Consistency

El campo `name` del frontmatter de un SKILL.md **DEBE** coincidir exactamente con el nombre del directorio padre.

**Correcto:** `Directorio analisis-legal/ contiene SKILL.md con name: analisis-legal.`
**Incorrecto:** `Directorio analisis-legal/ contiene SKILL.md con name: legal-analyzer.`

---

## 9. Validacion

| Check | Criterio | Accion si falla |
| --- | --- | --- |
| CM grammar | Las 4 secciones CM Core presentes (Proposito, I/O, Procedimiento, Signature Output) | Completar secciones faltantes |
| Name consistency | `name` en frontmatter = nombre del directorio padre (solo Skills extendidos) | Renombrar directorio o campo name |
| Token budget | CM Core <= 5000 tokens | Refactorizar: extraer logica densa a scripts/ |
| Scripts segregados | scripts/ contiene solo codigo ejecutable, no CM Core ni logica FSM | Mover contenido al archivo correcto |
| Script Protocol | Todo script en scripts/ es Python 3 con I/O via stdin/stdout JSON | Reescribir script conforme a §3.3 |
| URN valido | URN sigue patron `urn:{ns}:skill:{id}:{version}` | Corregir URN |
| Frontmatter | Campos obligatorios presentes y validos | Completar frontmatter |
| allowed-tools subconjunto interface | Cada herramienta en allowed-tools esta declarada en TOOLS.md del agente | Remover herramientas no declaradas o actualizar TOOLS.md |
| requires compatible security | Cada dependencia en requires es compatible con config.json del agente | Ajustar requires o config.json |
| Backward compat | Todo CM-*.md existente sigue siendo Skill degenerado valido | No modificar CMs existentes; ajustar implementacion |

---

## 10. Ejemplo

### 10.1 Skill Degenerado (CM-only)

```markdown
---
_manifest:
  urn: "urn:gn:skill:goreologo-cm-evaluador-riesgo:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Evaluar el nivel de riesgo institucional de una iniciativa GORE segun criterios normativos y presupuestarios.

## Input/Output

- **Input:** Descripcion de la iniciativa + contexto regulatorio
- **Output:** Nivel de riesgo (bajo/medio/alto/critico) + justificacion

## Procedimiento

1. Clasificar la iniciativa por area funcional (inversiones, RRHH, presupuesto).
2. Verificar alineacion con normativa vigente (Ley 19.175, SUBDERE).
3. Evaluar impacto presupuestario contra marco fiscal.
4. Determinar nivel de riesgo con justificacion.

## Signature Output

| Campo | Tipo |
|-------|------|
| nivel_riesgo | enum: bajo, medio, alto, critico |
| justificacion | string (max 200 palabras) |
| normativa_aplicable | string[] (URNs de KBs consultadas) |
```

Este CM-*.md es un Skill degenerado valido. Cumple CM grammar (4 secciones), tiene frontmatter de bootstrap, y reside en skills/ del workspace.

### 10.2 Skill Extendido (Directorio)

```text
analisis-legal/
  SKILL.md
  scripts/
    classify_initiative.py
    risk_matrix.py
  references/
    NORMATIVA.md
  assets/
    risk_template.json
```

**SKILL.md:**

```markdown
---
_manifest:
  urn: "urn:gn:skill:goreologo-analisis-legal:1.0.0"
  type: "skill_extended"
name: "analisis-legal"
description: "Analiza iniciativas GORE contra marco legal vigente. Usar cuando el usuario mencione riesgo legal, normativa o cumplimiento regulatorio."
version: "1.0.0"
status: published
lang: es
compatibility: "Requiere python3 con pandas instalado"
allowed-tools: "Bash(python:*) Read search_kb"
requires: "python3 pandas"
---

## Proposito

Analizar iniciativas GORE contra el marco legal vigente, produciendo un informe de cumplimiento y riesgo legal.

## Input/Output

- **Input:** Descripcion de la iniciativa + area funcional
- **Output:** Informe de cumplimiento legal con nivel de riesgo

## Procedimiento

1. Clasificar la iniciativa usando scripts/classify_initiative.py.
2. Consultar normativa aplicable en references/NORMATIVA.md.
3. Evaluar riesgo con la matriz en scripts/risk_matrix.py.
4. Generar informe usando la plantilla en assets/risk_template.json.

## Signature Output

| Campo | Tipo |
|-------|------|
| cumplimiento | enum: conforme, parcial, no_conforme |
| nivel_riesgo | enum: bajo, medio, alto, critico |
| informe | string (formato JSON segun risk_template.json) |

## Scripts

- **classify_initiative.py:** Clasifica la iniciativa por area funcional. Input: descripcion (stdin JSON). Output: clasificacion JSON (stdout).
- **risk_matrix.py:** Evalua riesgo contra matriz parametrizada. Input: clasificacion + normativa (stdin JSON). Output: nivel de riesgo + justificacion (stdout JSON).

## References

- **NORMATIVA.md:** Compilado de normativa GORE aplicable (Ley 19.175, SUBDERE, Contraloria). Consultar cuando el procedimiento lo requiera.

## Examples

Ejemplo: Iniciativa "Construccion de centro comunitario en comuna X".
- Clasificacion: inversiones
- Normativa: Ley 19.175 Art. 36
- Riesgo: medio (requiere evaluacion ambiental)
```

Este Skill extendido tiene CM Core intacto (secciones 1-4), directorio con scripts ejecutables conforme al Script Protocol (§3.3), y frontmatter extendido. Aplicar Extract produce un CM con solo las secciones 1-4, perdiendo scripts/ y references/.
