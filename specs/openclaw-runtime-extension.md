---
_manifest:
  urn: "urn:agengai:kb:openclaw-runtime-extension"
  provenance:
    created_by: "OpenAI"
    created_at: "2026-03-23"
    source: "runtime-spec-md v3.6.0, OpenClaw baseline"
version: "1.0.0"
status: published
tags: [spec, runtime, openclaw, extension, transmutacion, deploy]
lang: es
extensions:
  agengai:
    extends:
      - "urn:kora:kb:runtime-spec-md"
    precedence_tier: 4
    platform: "openclaw"
    baseline_docs_release: "2026.3.22"
---

# AGENGAI/OpenClaw-Runtime-Extension v1.0.0

## 1. Definicion

Esta extension especializa `runtime-spec-md` para el
target OpenClaw. Su funcion es fijar restricciones OpenClaw-specific sin
convertir detalles efimeros de plataforma en ley base de KORA.

### 1.1 Alcance

Gobierna:

1. principio `native-first` para OpenClaw,
2. topologia de output OpenClaw,
3. frontera entre artefactos derivados y estado operativo,
4. checks minimos de despliegue para este target.

## 2. Principio native-first

Cuando OpenClaw ofrezca una superficie nativa para config, permisos, bundles o
instalacion, la transmutacion **DEBE** usar esa superficie antes que un wrapper
textual improvisado.

## 3. Topologia target

La salida derivada **DEBERIA** vivir bajo:

```text
BUILD/openclaw/{namespace}/{agent}/
```

Dentro de ese contenedor pueden existir:

- artefactos del agente ya compilados,
- config nativa OpenClaw,
- registro `_transmutation.yml`.

## 4. Contrato estructurado minimo

Una transmutacion a OpenClaw **DEBE** declarar como minimo:

1. fuente IR,
2. adapter usado,
3. fidelidad por dimension,
4. perdidas o degradaciones,
5. frontera con estado operativo mutable.

## 5. Install surfaces

Skills, plugins o bundles OpenClaw **DEBERIAN** instalarse por vias nativas
cuando existan. El proceso de instalacion **NO DEBE** depender de texto oculto
en el body del agente.

## 6. Runtime state boundary

Quedan fuera de la fuente canonica:

- credenciales,
- pairing stores,
- caches,
- sesiones,
- volúmenes operativos.

Estos artefactos **DEBEN** resolverse en runtime, no en `BUILD/` como si fueran
parte estable del agente.

## 7. Validacion

| Check | Condicion | Enforcement |
| --- | --- | --- |
| Native-first | No se usa wrapper textual cuando hay superficie nativa | manual/lint |
| Output ordenado | La salida vive bajo topologia OpenClaw declarada | lint |
| Registro emitido | `_transmutation.yml` presente | lint |
| Estado excluido | No se serializan credenciales ni caches | lint/manual |

## 8. Migracion

Contrato vigente v1:

- OpenClaw queda fijado como extension de namespace de capa 4,
- especializa runtime y transmutacion sin relajar ley base,
- refuerza la separacion entre output derivado y estado operativo.
