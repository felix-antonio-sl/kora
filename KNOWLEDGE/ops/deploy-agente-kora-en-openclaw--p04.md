---
_manifest:
  urn: urn:ops:kb:deploy-agente-kora-en-openclaw-p04
  provenance:
    created_by: ops/clawstack
    created_at: '2026-03-19'
    updated_at: '2026-03-23'
    source: Experiencia operacional desplegando korax v3.4.0, steipete v1.5.1 y salubrista-hah
      v1.0.0 en Hetzner sobre OpenClaw v2026.3.22
version: 1.2.0
status: published
tags:
- deploy
- openclaw
- docker
- tutorial
- operaciones
- transmutacion
- federation
- hooks
- ux
lang: es
extensions:
  kora:
    shard_index: 4
    shard_count: 4
    shard_root_urn: urn:ops:kb:deploy-agente-kora-en-openclaw
relations:
  cites:
  - urn:ops:kb:ux-telegram-openclaw
---


# Tutorial: Desplegar un agente KORA en OpenClaw - Parte 04

## 12. Config UX del canal

Aplicar config UX óptima para el canal (ver `urn:ops:kb:ux-telegram-openclaw` para Telegram):

```json5
channels: {
 telegram: {
 chunkMode: "length",
 markdown: { tables: "bullets" },
 replyToMode: "first",
 silentErrorReplies: true,
 textChunkLimit: 4000,
 linkPreview: false,
 reactionLevel: "minimal",
 },
}
```

---

## Agentes desplegados con este tutorial

| Agente | Versión | Puerto | Arquitectura | Fecha |
|---|---|---|---|---|
| korax | v3.4.0 | 18789 | Caso B (+ sidecar PCA) | 2026-03-19 |
| steipete | v1.5.1 | 18810 | Caso A (puro, workers via exec) | 2026-03-19 |
| salubrista-hah | v1.0.0 | 18830 | Caso A (puro, 13 KBs salud) | 2026-03-23 |
