---
title: Frontmatter Examples
status: internal
lang: es
---

# Frontmatter Examples

## Draft Descriptivo

```yaml
---
_manifest:
  urn: urn:{namespace}:kb:{id}
  provenance:
    source: source/{namespace}/{subdir}/{source_file}.md
version: 1.0.0
status: draft
tags: [tag1, tag2, tag3]
lang: es
extensions:
  kora:
    family: normative
---
```

## Draft Prescriptivo

```yaml
---
_manifest:
  urn: urn:{namespace}:kb:{id}
  provenance:
    source: source/{namespace}/{subdir}/{source_file}.md
version: 1.0.0
status: draft
tags: [spec, protocolo, operacion]
lang: es
---
```
