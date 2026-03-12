---
title: Audit Stack
status: internal
lang: es
---

# Audit Stack

Recursos del repo ya disponibles para auditoria de artefactos KORA:

- `specs/md-spec.md`
- `specs/spec-md.md`
- `specs/gobernanza.md`
- `knowledge/kora/sys/pipeline-ingesta.md`
- `scripts/kora_lib/validation.py`
- `scripts/kora_lib/artifacts.py`
- `scripts/kora_lib/catalog.py`
- `tests/test_artifacts.py`
- `tests/test_semantic_validation.py`

Uso recomendado:

1. Fijar la spec rectora del artefacto.
2. Ejecutar luego la verificacion mecanica reusable del repo.
3. Separar hallazgos deterministas de los checks que siguen requiriendo juicio humano.
