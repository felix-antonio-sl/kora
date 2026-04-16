# Template: Subagent CC Compilado

Esqueleto de referencia para el subagent generado por CM-CLAUDE-CODE-ADAPTER.

```markdown
---
name: {ns}--{name}
description: "{derivado de SOUL.md identity + triggers}"
model: {tier_default}
effort: {effort_level}
maxTurns: {max_turns}
permissionMode: {permission_mode}
tools: {tools_list}
disallowedTools: {disallowed_tools}
skills:
  - {ns}--{name}--{cm1}
  - {ns}--{name}--{cm2}
hooks:
  Stop:
    - hooks:
        - type: prompt
          prompt: "Co-induccion {name}: (1) SCOPE_COMPLIANCE—output dentro del dominio declarado (2) STATE_AWARENESS—coherente con estado FSM activo (3) INTERFACE_DISCIPLINE—solo tools declarados usados. Si alguno falla, indica cual y sugiere correccion. $ARGUMENTS"
          model: {co_induction_model}
---

# {name} — {titulo de SOUL.md Identidad Dialectica}

{SOUL.md stripped: Identidad Dialectica, Paradigma Cognitivo, Tono}

---

{AGENTS.md stripped: FSM, Reglas Duras, Co-induccion, Contexto Multi-turno, Wiring, Comportamiento Operativo}

---

{TOOLS.md stripped: routing maps y semantica de herramientas}

---

## Skills (Lazy Load)

Cuando entres en un estado FSM, invoca el skill correspondiente:

| Estado | Skill | CM |
|--------|-------|----|
| {estado} | {ns}--{name}--{cm} | CM-{CM} |

Para cargar un skill: invocalo como `/{ns}--{name}--{cm}` o consulta `AGENTS/{ns}/{name}/skills/CM-{CM}` directamente.
```

## Notas de compilacion

- Headers H1 (`#`) separan secciones de componentes distintos.
- Separadores `---` delimitan transiciones entre SOUL, AGENTS y TOOLS.
- USER.md excluido (runtime-spec §6.1).
- config.json excluido del body (informo frontmatter).
- Todo frontmatter KORA (_manifest) eliminado (R-TRANSMUTE-2).
- Body total < 20K chars (runtime-spec §9.4).
