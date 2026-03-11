# GEMINI.md - KORA Workspace

> **Contexto de Proyecto:** Este archivo contiene el contexto, instrucciones y convenciones de desarrollo para el monorepo KORA.

## 📌 Visión General del Proyecto (Project Overview)

KORA es un monorepo en Python que gestiona especificaciones, conocimiento y workspaces de agentes gobernados por una capa formal categorial y una toolchain ejecutable (CLI). El objetivo principal del repositorio es mantener la estricta consistencia entre el conocimiento, las especificaciones (specs), los workspaces y su automatización.

### 🏗️ Arquitectura y Estructura de Directorios

El ecosistema KORA se organiza en estratos principales:

- `specs/`: Ley operativa del sistema y la constitución del proyecto.
- `knowledge/`: Artefactos descriptivos KORA/MD (Base de conocimiento por namespace).
  - La **Formal Layer oficial** reside en `knowledge/kora/categorical-foundations/`.
  - El corpus auxiliar categorial vive en `knowledge/fxsl/cat/` (no es normativo de manera directa).
- `agents/`: Workspaces ejecutables de agentes por namespace.
- `scripts/`: Toolchain ejecutable (CLI oficial de KORA) para indexar, validar, migrar y auditar.
- `catalog/`: Vista materializada del grafo de artefactos (generada dinámicamente).
- `docs/generated/`: Salidas vivas y métricas generadas automáticamente por la CLI.
- `schemas/`: Contratos JSON para bootstrap y configuración.
- `tests/`: Suite mínima del auditor categorial.

## 🚀 Construcción y Ejecución (Building and Running)

El proyecto utiliza un entorno Python (`requirements.txt`: PyYAML, jsonschema, pytest). Toda la interacción principal y el mantenimiento del estado se realiza a través de la CLI oficial en `scripts/kora`.

### Comandos Principales (CLI Tools)

- **Indexar y Sincronizar (Source of Truth):**
  - `python3 scripts/kora index` (Actualiza la vista materializada)
  - `python3 scripts/kora sync-docs` (Sincroniza documentos y métricas)
- **Validación y Salud:**
  - `python3 scripts/kora validate --profile strict`
  - `python3 scripts/kora health --strict`
- **Métricas y Análisis:**
  - `python3 scripts/kora stats --json`
  - `python3 scripts/kora graph --json`
- **Migración y Resolución:**
  - `python3 scripts/kora migrate --profile transitional`
  - `python3 scripts/kora resolve "urn:kora:kb:agent-spec-md"`
- **Pruebas (Testing):**
  - `python3 -m unittest discover -s tests`

### Flujo de Trabajo Recomendado (Workflow)

Al realizar cualquier cambio estructural en specs, workspaces o conocimiento, se DEBE ejecutar la siguiente secuencia:
1. `python3 scripts/kora migrate --profile transitional` (si aplica)
2. `python3 scripts/kora index`
3. `python3 scripts/kora health --strict`
4. `python3 scripts/kora validate --profile strict`
5. `python3 scripts/kora sync-docs`
6. `python3 -m unittest discover -s tests`

## 📝 Convenciones de Desarrollo (Development Conventions)

- **Source of Truth (SSOT):** El filesystem con manifiestos válidos es la única fuente de la verdad. No mantener conteos o métricas a mano en las documentaciones; usar siempre la CLI (`sync-docs`) para generarlas en `docs/generated/`.
- **Precedencia Normativa:**
  1. `specs/gobernanza.md`
  2. `specs/spec-md.md` y `specs/md-spec.md`
  3. `specs/agent-spec-md.md`, `specs/skill-spec-md.md`, `specs/runtime-spec-md.md`, `specs/swarm-spec-md.md`
  4. Extensiones de namespace.
- **Trazabilidad estricta:** Los enlaces de `Traces to:` **solo** pueden apuntar a documentos de la Formal Layer oficial. Cualquier idea auxiliar no absorbida formalmente debe ir bajo la sección de `Rationale:`.
- **Modelo de Workspace de Agente:**
  - `AGENTS.md`: Define el comportamiento (Behavior).
  - `TOOLS.md`: Interfaz semántica declarada.
  - `SOUL.md` y `USER.md`: Estado/contexto del agente.
  - `config.json`: Seguridad y boundary del runtime.
  - **Reglas Invariables:**
    - `TOOLS.md` y `config.json.tools.allow` deben coincidir de forma exacta.
    - `config.json.runtime_capabilities` debe reflejar los permisos crudos del runtime.
    - `sub_agents.max_concurrent` no debe ser `0` (debe ser ausente o `>= 1`).
    - Las identidades (URNs) de los skills siguen el formato estándar: `urn:{namespace}:skill:{id}:{version}`.
- **YAML Estricto:** Seguir indentación de 2 espacios, no tabs, sin espacios finales (trailing whitespace) y usar formato multilínea (`|`) según las guías globales de KODA.
