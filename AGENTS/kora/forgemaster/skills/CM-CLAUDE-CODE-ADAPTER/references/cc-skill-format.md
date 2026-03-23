# Claude Code — Formato Nativo de Skill

Referencia operativa para CM-CLAUDE-CODE-ADAPTER. Fuente: KNOWLEDGE/dev/claude-code-mastery/extensibilidad.md (CC v2.1.81, 2026-03-22).

## Ubicacion

- Proyecto: `.claude/skills/{name}/SKILL.md` o `.claude/skills/{name}.md`
- Global: `~/.claude/skills/`

## Skill Degenerado (archivo unico)

```yaml
---
name: my-skill
description: "Que hace. Usar cuando..."
---

# Contenido del skill en Markdown
```

## Skill Extendido (directorio)

```
.claude/skills/{name}/
  SKILL.md              # Frontmatter + body
  scripts/              # Ejecutables auxiliares
  references/           # Documentacion on-demand
  assets/               # Templates, ejemplos
```

## Frontmatter de Skill

```yaml
---
name: kebab-case-identifier          # max 64 chars
description: "Que hace + cuando usar" # max ~200 chars para token economy
argument-hint: "[argumento-opcional]" # hint para el usuario
allowed-tools: Read, Bash(npm *)      # whitelist de tools
model: sonnet                         # override de modelo
effort: medium                        # override de effort
---
```

## Progressive Disclosure (3 fases)

| Fase | Contenido | Cuando | Token Impact |
|------|-----------|--------|-------------|
| Discover | name + description del frontmatter | Siempre en system prompt | ~100 tokens/skill |
| Activate | Body de SKILL.md completo | Cuando CC detecta relevancia | Variable |
| Execute | scripts/, references/, assets/ | On-demand cuando el skill los lee | Solo si se acceden |

## Restricciones

- Sin caracteres `<>` en frontmatter (seguridad).
- Sin "claude" ni "anthropic" en name (palabras reservadas).
- Body idealmente <= 5000 palabras para token economy.
- Si excede: mover contenido extenso a references/.

## Mapping KORA CM → CC Skill

| KORA | CC |
|------|----|
| CM Core: Proposito | Body: seccion Proposito |
| CM Core: Input/Output | Body: seccion Input/Output |
| CM Core: Procedimiento | Body: seccion Procedimiento |
| CM Core: Signature Output | Body: seccion Signature Output |
| _manifest frontmatter | ELIMINADO (R-TRANSMUTE-2) |
| scripts/ | scripts/ (copiado) |
| references/ | references/ (copiado) |
| assets/ | assets/ (copiado) |
