# Curation Conductor Skill Design

## Intento

Crear una skill KORA productiva que determine, conduzca y acompañe la curación
de artefactos de conocimiento KORA de comienzo a fin.

La skill no debe ser un productor único ni una duplicación de `curator`.
Debe actuar como **orquestador procedural** del proceso de curación:

- clasificar el input
- decidir familia documental y funtor
- elegir staging correcto
- decidir si corresponde `atomize` o curación guiada
- correr validaciones y gates
- decidir promote o reingreso
- cerrar con estado explícito y handoff

## Scope

Incluido:

- skill nueva bajo `artifacts/skills/kora/curation-conductor/`
- shape KORA productiva nativa (`SKILL.md` + `referencias/`)
- cobertura del proceso end-to-end de curación de knowledge
- routing explícito entre `KB normal`, `atomic` y reroute fuera de scope cuando el material corresponde a `spec`
- acompañamiento hasta `ready_to_promote` o `published`

Excluido:

- reemplazar `atomize` como productor de `atomic`
- reemplazar `promote` o `validation` como enforcement mecánico
- gobernar curación de agentes o skills; su foco es conocimiento
- automatizar ingestión masiva de archivos arbitrarios sin clasificación previa

## Decisión de diseño

Se elige una skill-conductor, no una skill-productor.

Razones:

- `atomic` ya tiene productor canónico: `atomize`
- `promote` ya gobierna publicación
- `validation.py` ya gobierna gran parte del arbitraje mecánico
- lo que falta es una pieza que tome una fuente y responda correctamente:
  - qué proceso aplica
  - cómo se ejecuta
  - en qué estado queda

## Nombre y ubicación

Nombre propuesto:

- `curation-conductor`

Ubicación:

- `artifacts/skills/kora/curation-conductor/`

Motivo:

- evita colisión de identidad con el agente `curator`
- deja claro que su rol es conducir el proceso, no absorber toda la ontología del agente

## Arquitectura

### 1. Bundle

El bundle debe contener:

- `SKILL.md`
- `referencias/process-map.md`
- `referencias/family-decision-table.md`

No debe contener:

- scripts nuevos si el workflow puede apoyarse en toolchain existente
- assets
- metadatos UI externos al shape KORA del repo

### 2. Fuente de verdad

La skill debe usar como base normativa mínima:

- `governance/gobernanza.md`
- `ontology/harness-spec.md`
- `serialization/autoria-spec.md`
- `serialization/md-spec.md`
- `serialization/knowledge-spec.md`
- `artifacts/knowledge/kora/sys/pipeline-ingesta.md`

Y, como referencias operativas:

- `artifacts/skills/kora/atomize/SKILL.md`
- `artifacts/agents/kora/curator/AGENT.md`
- skills operativas del `curator` cuando aporten workflow concreto

### 3. Contrato de proceso

La skill debe responder explícitamente estas preguntas para cada caso:

1. ¿Qué tipo de input es?
2. ¿El input pertenece realmente al pipeline de knowledge?
3. ¿Qué familia documental corresponde?
4. ¿Qué funtor aplica?
5. ¿En qué zona del pipeline debe entrar?
6. ¿Qué productor o ruta de trabajo corresponde?
7. ¿Qué validaciones/gates aplican?
8. ¿El outcome operativo es `pending`, `processing`, `ready_to_promote`, `published`, `needs_repair` o `rerouted_to_spec`?

### 4. Familias que debe distinguir

Mínimo:

- `KB normal` descriptivo
- `atomic`

La regla fuerte es:

- `atomic` no es default
- `atomic` solo cuando la granularidad proposicional es parte real del objetivo
- si el material es prescriptivo o fundacional, la skill **NO** lo trata como knowledge: lo deriva explícitamente al circuito `spec`

### 5. Relación con `atomize`

`atomize` queda subordinado al conductor:

- si la skill decide `family = atomic`, deriva a `atomize`
- si no, la skill guía koraficación o cristalización sin usar `atomize`

### 6. Relación con `promote`

La skill no reemplaza `kora promote`.

Debe:

- verificar readiness
- explicar si promote corresponde o no
- usar `promote` solo cuando el artefacto ya satisfizo las condiciones

## Workflow end-to-end

1. Diagnosticar el input:
   - crudo
   - curado parcial
   - draft existente
   - artefacto publicado con necesidad de repair
2. Determinar:
   - descriptivo vs prescriptivo
   - familia documental
   - funtor (`F` koraficación / `G` cristalización)
3. Determinar staging:
   - `INBOX`
   - `REVIEW`
   - repair sobre publicado
4. Ejecutar la ruta:
   - `atomic` -> `atomize`
   - `KB normal` -> curación guiada
   - prescriptivo/fundacional -> `rerouted_to_spec`
5. Verificar:
   - shape
   - relaciones
   - fidelidad
   - gates de publicación
6. Emitir estado final y siguiente paso

## Invariantes

- nunca usar `atomic` como curación universal
- nunca publicar sin pasar por `REVIEW`
- nunca confundir productor con orquestador
- nunca tratar `docs/generated/*` como fuente de verdad
- siempre declarar la razón de la familia elegida
- siempre dejar explícito si la salida quedó lista para `promote`

## Salida esperada

La salida del proceso debe incluir:

- diagnóstico del input
- familia elegida
- funtor elegido
- staging elegido
- productor/ruta elegida
- validaciones aplicadas
- estado final
- pendientes / bloqueos

## Testing y validación

La skill queda aceptable si:

- pasa `check --strict`
- sus referencias existen
- su `SKILL.md` deja claro que `atomize` es una ruta especializada
- su workflow cubre intake -> review -> validate -> promote -> handoff

## Riesgos

1. Duplicar doctrina que ya vive en specs.
2. Convertir la skill en `curator` comprimido, en vez de conductor procedural.
3. Usar `atomic` por inercia donde no conviene.
4. Dejar ambigua la frontera entre acompañar el pipeline de knowledge y desbordarse al régimen `spec`.

## Siguiente paso

Si este diseño queda aprobado, el siguiente paso es implementar la skill en:

- `artifacts/skills/kora/curation-conductor/SKILL.md`
- `artifacts/skills/kora/curation-conductor/referencias/process-map.md`
- `artifacts/skills/kora/curation-conductor/referencias/family-decision-table.md`
