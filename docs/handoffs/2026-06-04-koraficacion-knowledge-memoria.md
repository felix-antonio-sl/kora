---
_manifest:
  urn: "urn:kora:kb:memoria-koraficacion-knowledge-2026-06-04"
  provenance:
    created_by: "Codex"
    created_at: "2026-06-04"
    source: "Memoria operativa derivada de la recuperacion KORA/MD de curacion y deshidratacion documental legacy KODA."
version: "1.0.0"
status: publicado
tags: [memoria, koraficacion, knowledge, kora-md, curacion]
lang: es
extensions:
  kora:
    family: note
---

# Memoria 2026-06-04 - koraficacion knowledge

- `koraficacion-knowledge` es la skill productiva para convertir documentos
  humanos a KORA/MD con alta fidelidad y deshidratacion semantica.
- No reintroducir YAML KODA, `atomize`, familia `atomic` ni
  `agent_koda_transformer` como fuente runtime.
- El nucleo recuperado del legacy es: `skeleton/meat/fat`, telegrafizacion,
  deduplicacion, auditoria original/salida y FS obligatorio.
- El CR crudo no es gate rigido. Usar `IDC`:
  `IDC = CR observado / CR esperado para el perfil documental`.
- Perfiles iniciales IDC: `prosa-redundante`, `mixto`,
  `denso-estructurado`, `fuente-ya-densa`.
- `audit_korafication.py` es guardrail mecanico; no sustituye el ledger
  semantico de hechos para declarar `FS=100%`.
- Deploy aplicado en Claude Code, Codex, OpenCode y OpenClaw main.
- Handoff completo: `docs/handoffs/2026-06-04-koraficacion-knowledge.md`.
