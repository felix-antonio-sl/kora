---
_manifest:
  urn: "urn:kora:kb:memoria-poda-scriptorium-inbox-2026-06-01"
  provenance:
    created_by: "Codex"
    created_at: "2026-06-01"
    source: "Memoria operativa derivada de la poda _SCRIPTORIUM/INBOX 2026-06-01."
version: "1.0.0"
status: publicado
tags: [memoria, saneamiento, scriptorium, inbox]
lang: es
extensions:
  kora:
    family: note
---

# Memoria 2026-06-01 - poda _SCRIPTORIUM/INBOX

- Se retiro del repo el corpus crudo versionado en
  `artifacts/knowledge/_SCRIPTORIUM/INBOX/`.
- Copia preservada: `/home/felix/kora-external-sources/2026-06-01-scriptorium-inbox/`.
- Inventario versionado: `source-inventory-2026-06-01.tsv` con 343 fuentes,
  `sha256`, tamano, path original y copia externa.
- Nueva regla: `_SCRIPTORIUM/INBOX` en git conserva solo README e inventarios;
  PDFs, DOCX, JSON dumps, TXT fuente, OCR y exports extensos quedan fuera.
- No se podaron `_FRAGUA` ni `_TALLER`: esos staging contienen semantica
  agentica/skill no promovida y requieren auditoria separada.
- Verificacion: `index` 644 artefactos, `check --strict` 34/34, `kb-graph`
  0 huerfanos/0 broken edges y `unittest` 336 OK.
