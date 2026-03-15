---
title: OpenClaw Workspace Template
status: internal
lang: es
---

# OpenClaw Workspace Template

Estructura de output esperada para una transmutacion KORA → OpenClaw.

## Estructura de directorios

```
{output}/openclaw/{ns}-{agent}/
├── workspace/
│   ├── AGENTS.md            # Behavior adaptado (sin frontmatter KORA)
│   ├── SOUL.md              # Identidad y tono (sin frontmatter KORA)
│   ├── USER.md              # Contexto operador (sin frontmatter KORA)
│   ├── TOOLS.md             # Notas herramientas (sin frontmatter KORA)
│   ├── IDENTITY.md          # Nombre + emoji + theme (derivado de SOUL.md)
│   └── skills/
│       └── {skill-name}/
│           └── SKILL.md     # Skill adaptado (frontmatter OpenClaw)
├── config-snippet.json5     # Entrada para openclaw.json agents.list
└── _transmutation.yml       # Manifest de sincronizacion
```

## Ejemplo AGENTS.md (sin frontmatter)

```markdown
# {namespace}/{nombre}

## 1. FSM

1. STATE: S-DISPATCHER → ACT: ...

## 2. Reglas Duras

- R1: ...

## 3. Co-induccion

### Checklist Pre-Output
1. CHECK_1 — ...
```

## Ejemplo IDENTITY.md

```markdown
name: Goreologo
emoji: 🏛️
theme: gobierno-regional
```

## Ejemplo skill adaptado

```yaml
---
name: intake-classifier
description: Clasifica la consulta del usuario por dimension institucional y complejidad
user-invocable: false
---

# Intake Classifier

## Proposito
...

## Procedimiento
1. ...
```
