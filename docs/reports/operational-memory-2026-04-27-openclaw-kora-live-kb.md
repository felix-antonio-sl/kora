---
_manifest:
  urn: "urn:kora:kb:operational-memory-2026-04-27-openclaw-kora-live-kb"
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-27"
    source: "Decision operativa durante transmutacion OpenClaw de salud/urgenciologo: en hosts con KORA clonado y actualizado, KB se monta desde el repo vivo."
version: "1.0.0"
status: publicado
tags: [operational-memory, openclaw, kora-repo, knowledge-mount, urgenciologo]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:ops:kb:principios-transmutacion-kora-openclaw"
    - "urn:ops:kb:deploy-agente-kora-en-openclaw-p02"
---

# Memoria operativa — OpenClaw con KB desde clon KORA vivo

## Decision

Cuando la maquina donde se desplegaran agentes OpenClaw tenga KORA clonado y al
dia, los KB mounts deben apuntar directamente al repo vivo:

```bash
KORA_REPO=/home/felix/kora
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

## Preflight

1. Confirmar `KORA_REPO`.
2. Actualizar o validar el clon antes de deploy.
3. Ejecutar `python3 toolchain/kora index` si el catalogo debe resolver URNs.
4. Montar el corpus como read-only.
5. Verificar dentro del container que el path y archivos existen.

## Aplicacion inicial

La transmutacion OpenClaw de `salud/urgenciologo` usa este patron para
`artifacts/knowledge/salud/med-emergencia`.
