---
_manifest:
  urn: "urn:kora:kb:hermes-runtime-extension"
  provenance:
    created_by: "Claude Opus 4.7"
    created_at: "2026-05-20"
    source: "HITL del operador 2026-05-20: activacion de hermes como runtime canonico (decision: urn:kora:kb:adr-kora-v7-esencial). Esta v0.1 es stub: declara dominio inicial y deuda explicita; contenido normativo completo en Fase 2b."
version: "0.1.0"
status: publicado
tags: [spec, runtime, hermes, extension, transmutacion, stub]
lang: es
extensions:
  kora:
    family: spec
    precedence_tier: 4
    platform: "hermes"
    baseline_docs_release: "pendiente"
relations:
  depends:
    - "urn:kora:kb:runtime-spec-md"
    - "urn:kora:kb:transmutation-spec"
  cites:
    - "urn:kora:kb:harness-spec"
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:adr-kora-v7-esencial"
---

# KORA/Hermes-Runtime-Extension v0.1.0 (stub)

## 1. Definicion

Esta extension especializa `runtime-spec-md` para el target **Hermes
Agent** (`hermes` runtime). Hermes es runtime canonico de KORA desde
2026-05-20 (`urn:kora:kb:adr-kora-v7-esencial`); previamente estaba
bloqueado por `gobernanza §8.2` historica.

**v0.1 es stub deliberado**: declara dominio inicial y deuda explicita.
El contenido normativo completo (matriz de realizabilidad final,
fidelity claims, ejemplos, schema runtime) se desarrolla en Fase 2b.

### 1.1 Alcance

Gobernara:

1. Proyeccion `T_{hermes}: KORA_IR → Hermes` segun
   `transmutation-spec`.
2. Shape runtime de skills/agents Hermes (a documentar).
3. Mecanismos de capture y persistencia (a documentar).
4. Permisos, sandbox y trust levels Hermes (a documentar).

### 1.2 Estado v0.1

Esta version solo:

- Declara el URN canonico `urn:kora:kb:hermes-runtime-extension`.
- Reserva el espacio en la topologia `runtime/`.
- Permite que `hermes` aparezca en `entornos_objetivo` sin romper
  `urn-integrity`.
- Documenta la deuda de contenido normativo.

## 2. Dominio inicial declarado (provisional)

Hasta el desarrollo completo en Fase 2b, las siguientes formas
materiales se admiten **provisionalmente** sin garantia de fidelidad:

| Forma material | Soporte provisional |
|----------------|----------------------|
| `habilidad` | provisional — pendiente verificacion |
| `subagente` | provisional — pendiente verificacion |
| `agente-propiamente-tal` | provisional — pendiente verificacion |
| `agente-plataforma` | sin compromiso hasta documentar mecanismo |

**Regla operativa**: transmutaciones a hermes desde v0.1 deben
considerarse experimentales; cualquier artefacto productivo que
declare `entornos_objetivo: [hermes, ...]` y desee garantia formal
debe esperar v1.0 de esta extension.

## 3. Matriz de preservacion (a completar en Fase 2b)

La matriz definitiva por eje del vector PMI × LFS se documenta en
v1.0. Para v0.1, marcador:

```yaml
# Provisional — todos los ejes en "unknown" hasta verificacion empirica
pi:     { status: pending }
mu:     { status: pending }
xi:     { status: pending }
lambda: { status: pending }
phi:    { status: pending }
sigma:  { status: pending }
```

## 4. Encaje runtime (a completar)

`extensions.hermes.*` queda como namespace reservado. Campos
especificos se definen en Fase 2b.

## 5. Deuda explicita

Para cerrar `hermes-runtime-extension v1.0`:

1. Documentar formas materiales soportadas con verificacion empirica
   contra el runtime Hermes real.
2. Completar matriz de preservacion por cada eje PMI × LFS.
3. Definir shape runtime (estructura de carpetas, archivos requeridos,
   metadata).
4. Especificar mecanismos de aprobacion / sandbox / persistencia.
5. Declarar fidelity claims por (arnes, forma_material, target).
6. Integrar con `transmute.py::PRESERVATION_MATRIX["hermes"]` en
   forma definitiva.
7. Producir ejemplos completos de artefacto transmuted a hermes.

## 6. Trazabilidad

- Decision de activacion: `urn:kora:kb:adr-kora-v7-esencial`
- Marco general de runtimes: `urn:kora:kb:runtime-spec-md`
- Leyes functoriales: `urn:kora:kb:transmutation-spec`
- Ontologia base: `urn:kora:kb:harness-spec`

## 7. Estado

`status: publicado` como stub v0.1.0. El contrato completo es
`pendiente` para Fase 2b.
