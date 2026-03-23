# Template: Skill CC Compilado

Esqueleto de referencia para cada skill generado por CM-CLAUDE-CODE-ADAPTER.

## Skill Degenerado (CM-*.md → archivo unico)

```markdown
---
name: {ns}--{name}--{cm-kebab}
description: "{derivado de seccion Proposito del CM, max 200 chars}"
---

## Proposito

{contenido de Proposito stripped}

## Input/Output

{contenido de Input/Output stripped}

## Procedimiento

{contenido de Procedimiento stripped}

## Signature Output

{contenido de Signature Output stripped}
```

## Skill Extendido (CM-*/SKILL.md → directorio)

```
.claude/skills/{ns}--{name}--{cm-kebab}/
  SKILL.md              # CM Core con frontmatter CC
  scripts/              # Copiado de fuente KORA
  references/           # Copiado de fuente KORA
  assets/               # Copiado de fuente KORA
```

## Reglas de compilacion

- Strip todo frontmatter KORA (_manifest, urn, version, status, etc.).
- Preservar CM Core: las 4 secciones canonicas intactas (skill-spec §3).
- Derivar `description` de la seccion Proposito, no de _manifest.
- Copiar scripts/, references/, assets/ como subdirectorios sin modificacion.
- name en kebab-case: `CM-AGENT-VALIDATOR` → `agent-validator`.
- Prefijo completo: `{ns}--{name}--{cm-kebab}`.
