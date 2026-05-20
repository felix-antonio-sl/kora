---
_manifest:
  urn: "urn:kora:kb:operational-memory-2026-04-27-openclaw-kora-live-kb"
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-27"
    source: "Decision operativa generalizada durante transmutaciones OpenClaw de salud/urgenciologo y salud/salubrista: los agentes OpenClaw KORA se despliegan con repo KORA local clonado y actualizado."
version: "1.1.0"
status: publicado
tags: [operational-memory, openclaw, kora-repo, knowledge-mount, urgenciologo, salubrista]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:ops:kb:principios-transmutacion-kora-openclaw"
    - "urn:agengai:kb:openclaw-runtime-extension"
    - "urn:ops:kb:deploy-agente-kora-en-openclaw-p02"
---

# Memoria operativa — OpenClaw con KORA vivo

## Decision

Los agentes OpenClaw de KORA se despliegan en maquinas con KORA clonado y al
dia. Ese repo local es parte del contrato de plataforma, no una optimizacion
ocasional. Los mounts de conocimiento deben apuntar al repo vivo:

```bash
KORA_REPO=/home/felix/kora
$KORA_REPO -> /home/node/repos/kora:ro
$KORA_REPO/artifacts/knowledge/{namespace}/{corpus}
  -> /home/node/knowledge/{namespace}/{corpus}:ro
```

No copiar a `/srv/kora/knowledge` salvo que el `platform_contract` declare
fallback, freeze auditado o ausencia de clon KORA.

## Contrato

El `platform_contract.deployment_hints.kb_mounts[]` debe declarar:

- `sync_strategy: bind_mount_live_kora_clone`
- `kora_repo_path`
- `source` absoluto al path de KORA en el host
- `repo_relative_source`
- `mount` dentro del container
- `mode: ro`

El `_transmutation.yml` OpenClaw debe declarar:

- `kora_repo_access.required: true`
- `kora_repo_access.host_env: KORA_REPO`
- `kora_repo_access.container_mount: /home/node/repos/kora`
- `kora_repo_access.knowledge_root: artifacts/knowledge`

## Preflight

1. Confirmar `KORA_REPO`.
2. Actualizar o validar el clon antes de deploy.
3. Ejecutar `python3 toolchain/kora index` si el catalogo debe resolver URNs.
4. Montar el corpus como read-only.
5. Verificar dentro del container que el path y archivos existen.

## Aplicacion

La transmutacion OpenClaw de `salud/urgenciologo` usa este patron para
`artifacts/knowledge/salud/med-emergencia`. La transmutacion OpenClaw de
`salud/salubrista` lo usa para `artifacts/knowledge/salud/salubrista`,
`artifacts/knowledge/salud/gestion-redes` y HODOM bajo el corpus salubrista.

Esta memoria se considera regla permanente para nuevos agentes OpenClaw KORA:
si existe clon local actualizado, el conocimiento se monta desde ahi y no desde
copias desacopladas.
