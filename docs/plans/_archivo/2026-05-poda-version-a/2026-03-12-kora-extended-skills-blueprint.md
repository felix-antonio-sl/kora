# Blueprint: Skills Extendidos para Agentes KORA

**Fecha:** 2026-03-12
**Status:** Propuesta
**Tipo:** Blueprint de transicion
**Scope:** Habilitar skills con `SKILL.md`, `scripts/`, `references/` y `assets/` sin romper el baseline actual de skills degenerados

---

## 1. Resumen

El repo ya muestra el limite del skill degenerado puro: varios agentes necesitan capacidad ejecutable y determinista que no cabe limpiamente solo en `CM-*.md`.

La propuesta es introducir un segundo regimen opcional, llamado aqui **skill extendido**, manteniendo compatibilidad completa con el baseline vigente:

- El `CM-*.md` sigue siendo obligatorio y sigue siendo el contrato cognitivo puro.
- El skill extendido agrega un bundle gobernado con `SKILL.md`, `scripts/`, `references/` y `assets/`.
- El runtime descubre y activa el bundle solo si existe declaracion explicita.
- El validator separa conformidad del CM de conformidad del bundle.

Esto permite que agentes como `kora/curator` usen validadores, proyectores, plantillas y tooling real sin esconder esa capacidad en prose ni romper segregacion.

---

## 2. Problema que resuelve

Hoy el baseline vigente:

- soporta solo skill degenerado en `skills/CM-*.md`
- descopa explicitamente `SKILL.md`, `scripts/`, `references/` y `assets/`
- no ofrece una forma gobernada de declarar recursos ejecutables asociados a un skill

Consecuencia:

- se sobrecarga `TOOLS.md` con contratos demasiado abstractos
- los skills describen checks o transformaciones que el agente no puede ejecutar de forma reproducible
- los artefactos deterministas del repo quedan fuera del modelo de skill
- el runtime ya anticipa wrappers tipo `SKILL.md`, pero la spec no los reintegra como capacidad oficial

---

## 3. Principio de diseno

No reemplazar el skill degenerado. Encapsularlo.

El skill extendido se modela como:

1. **CM Core**
   `skills/CM-*.md`
   Contrato cognitivo minimo, puro, invocable por la FSM.

2. **Skill Bundle**
   Directorio autocontenido con instrucciones operativas y recursos gobernados.

3. **Runtime Binding**
   Declaracion explicita que conecta CM y bundle sin mezclar behavior con runtime.

El agente sigue razonando con el CM. El bundle entrega capacidad instrumental adicional.

---

## 4. Modelo estructural propuesto

### 4.1 Layout canonico

```text
agents/{namespace}/{agent}/
  AGENTS.md
  SOUL.md
  USER.md
  TOOLS.md
  config.json
  skills/
    CM-KORAFICATOR.md
    CM-ARTIFACT-AUDITOR.md
  skillpacks/
    koraficator/
      SKILL.md
      scripts/
        project_source.py
        fidelity_diff.py
      references/
        md-spec-checklist.md
      assets/
        frontmatter-template.yml
    artifact-auditor/
      SKILL.md
      scripts/
      references/
      assets/
```

### 4.2 Rol de cada superficie

- `skills/CM-*.md`
  Define proposito, input/output, procedimiento y signature output.
- `skillpacks/{id}/SKILL.md`
  Define como usar scripts, referencias y assets del bundle.
- `skillpacks/{id}/scripts/`
  Solo operaciones deterministas o reproducibles.
- `skillpacks/{id}/references/`
  Material auxiliar gobernado y focalizado.
- `skillpacks/{id}/assets/`
  Plantillas, snippets y recursos estaticos.

### 4.3 Regla de compatibilidad

Si un agent no tiene `skillpacks/`, sigue siendo completamente valido bajo el baseline actual.

---

## 5. Invariantes

### 5.1 Invariantes del CM

- Todo `CM-*.md` sigue cumpliendo `skill-spec-md` actual.
- El CM no contiene FSM, wiring, security ni control conversacional.
- El CM no depende semanticamente de detalles internos del bundle.

### 5.2 Invariantes del bundle

- Todo bundle debe estar asociado a un `CM-*.md` existente.
- `SKILL.md` no redefine reglas duras de `AGENTS.md`.
- `scripts/` no pueden ampliar tools no declaradas por el agente.
- `references/` no reemplazan KB oficial ni crean routing oculto.
- `assets/` no contienen estado mutable.

### 5.3 Invariantes del runtime

- La activacion de un bundle debe ser explicita.
- El runtime debe mapear tools declaradas o documentar la limitacion.
- La ausencia del bundle no invalida el CM; solo reduce capacidad instrumental.
- Discovery debe seguir filtrado por security.

---

## 6. Binding propuesto

El binding no debe vivir en `AGENTS.md` ni dentro del CM.

Se propone declararlo en `config.json` como extension runtime del agente:

```json
{
  "extensions": {
    "kora": {
      "skillpacks": {
        "CM-KORAFICATOR": {
          "path": "skillpacks/koraficator",
          "entrypoint": "SKILL.md",
          "status": "experimental"
        },
        "CM-ARTIFACT-AUDITOR": {
          "path": "skillpacks/artifact-auditor",
          "entrypoint": "SKILL.md",
          "status": "experimental"
        }
      }
    }
  }
}
```

Razon:

- `AGENTS.md` sigue siendo behavior puro
- `CM-*.md` sigue siendo cognition pura
- `config.json` declara disponibilidad runtime del bundle

---

## 7. Validator minimo requerido

Antes de promover esta capacidad a spec oficial, el repo necesita validator compatible.

Checks minimos:

1. Todo bundle declarado resuelve a un directorio existente.
2. Todo bundle tiene `SKILL.md`.
3. Todo bundle declarado corresponde a un `CM-*.md` existente.
4. Ningun script del bundle exige tools fuera de `TOOLS.md`.
5. Ningun `SKILL.md` relaja reglas duras del bootstrap.
6. Ningun bundle introduce paths escapando del workspace del agente.
7. `references/` y `assets/` son opcionales, pero si existen deben vivir bajo el bundle declarado.

Checks recomendados:

1. `SKILL.md` referencia solo archivos existentes.
2. `scripts/` compilan o ejecutan `--help` cuando aplique.
3. El bundle declara salida esperada y condiciones de uso.

---

## 8. Impacto en specs

Para formalizar esto sin drift, hacen falta cambios coordinados:

### 8.1 `gobernanza.md`

- restaurar soporte oficial de skill extendido como superficie gobernada
- declarar si el kind sigue siendo `lazy_load_endofunctor` con bundle adjunto o si aparece un kind nuevo

### 8.2 `skill-spec-md.md`

- sacar `SKILL.md`, `scripts/`, `references/`, `assets/` del descope
- definir grammar minima de `SKILL.md`
- declarar pureza requerida entre CM y bundle
- distinguir validator de CM vs validator de bundle

### 8.3 `runtime-spec-md.md`

- normar discovery, activacion y fallback de bundles
- explicitar equivalencia funcional entre skill degenerado solo y skill degenerado + bundle

### 8.4 `agent-spec-md.md`

- permitir declaracion runtime de bundles asociados a skills
- mantener segregacion de componentes sin mover behavior a los bundles

---

## 9. Estrategia de migracion

### Fase 0: Preparacion

- No cambiar specs fundacionales todavia.
- Probar el modelo como blueprint en agentes candidatos.

### Fase 1: Experimental

- Introducir `skillpacks/` en uno o dos agentes de alto valor.
- Candidatos inmediatos:
  - `kora/curator`
  - `kora/forgemaster`

### Fase 2: Validator

- Extender `scripts/kora validate` con un perfil que revise bundles sin romper el baseline actual.

### Fase 3: Spec

- Promover la capacidad a spec oficial solo cuando haya:
  - validator
  - tests repo-wide
  - al menos dos agentes usando el patron con exito

---

## 10. Caso piloto recomendado: `kora/curator`

`curator` es el mejor piloto porque necesita exactamente lo que el skill degenerado no ofrece bien hoy:

- proyeccion de fuentes
- diff de fidelidad
- validacion source-aware
- templates de frontmatter
- checklists por familia documental

Skillpacks iniciales sugeridos:

1. `koraficator`
   - `project_source.py`
   - `fidelity_diff.py`
   - `chunk_family_rules.md`
   - `frontmatter-template.yml`

2. `artifact-auditor`
   - `audit_artifact.py`
   - `catalog_indexability_check.py`
   - `audit-checklist.md`

Esto bajaria la carga heuristica del LLM y moveria lo mecanico a tooling reproducible.

---

## 11. Decisiones recomendadas

1. Aprobar el principio: skill degenerado obligatorio + bundle extendido opcional.
2. No tocar aun las specs fundacionales sin validator.
3. Implementar piloto en `kora/curator`.
4. Si el piloto resulta, abrir cambio coordinado en `gobernanza.md`, `skill-spec-md.md`, `runtime-spec-md.md` y `agent-spec-md.md`.

---

## 12. Criterio de exito

La iniciativa vale la pena si logra estas cuatro cosas simultaneamente:

- mas capacidad ejecutable real por agente
- menos prose fingiendo tooling
- cero drift contra segregacion estructural
- migracion incremental sin invalidar agentes existentes
