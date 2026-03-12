---
title: Bootstrap Frontmatter Examples
status: internal
lang: es
---

# Bootstrap Frontmatter Examples

## Bootstrap Markdown

```yaml
---
_manifest:
  urn: urn:{namespace}:agent-bootstrap:{nombre}-agents:1.0.0
  type: bootstrap_agents
---
```

## Bootstrap Config

```json
{
  "_manifest": {
    "urn": "urn:{namespace}:agent-bootstrap:{nombre}-config:1.0.0",
    "type": "bootstrap_config"
  },
  "allowed_kb": [],
  "sandbox": {
    "mode": "strict"
  },
  "tools": {
    "allow": [],
    "deny": []
  },
  "sub_agents": {
    "max_depth": 0,
    "max_concurrent": 1
  }
}
```

## Extended Skill Entrypoint

```yaml
---
_manifest:
  urn: urn:{namespace}:skill:{agente}-{id}:1.0.0
  type: lazy_load_endofunctor
extensions:
  {namespace}:
    skill:
      form: extended
      allowed_tools: []
      requires: []
---
```
